# Copyright 2015 CloudByte Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from oslo_log import log as logging
import six

from cinder import context
from cinder.volume.drivers.cloudbyte import cloudbyte
from cinder.i18n import _, _LE, _LI
from cinder import exception

LOG = logging.getLogger(__name__)

class CloudByteISCSIDriver130(cloudbyte.CloudByteISCSIDriver):
    def __init__(self, *args, **kwargs):
        super(CloudByteISCSIDriver130, self).__init__(*args, **kwargs)
        
    def _get_volume_size(self, volume):
        size = volume.get('size')
        return six.text_type(size) + "G"

    def _add_qos_group_request(self,
                               volume,
                               tsmid,
                               datasetid,
                               volume_name,
                               qos_group_params):

        # Prepare the user input params
        params = {
            "name": "QoS_" + volume_name,
            "tsmid": tsmid,
            "datasetid": datasetid,
            "datasetname": volume_name,
            "quotasize": self._get_volume_size(volume)
        }
        # Get qos related params from configuration
        params.update(self.configuration.cb_add_qosgroup)

        # Override the default configuration by qos specs
        if qos_group_params:
            params.update(qos_group_params)
            
        params.update({'throughput': 4 * int(params['iops'])})

        data = self._api_request_for_cloudbyte("addQosGroup", params)
        return data
        
    def _create_volume_request(self, volume, datasetid, qosgroupid,
                               tsmid, poolid, volume_name, file_system_params):

        # Prepare the user input params
        params = {
            "datasetid": datasetid,
            "name": volume_name,
            "qosgroupid": qosgroupid,
            "tsmid": tsmid,
            "quotasize": self._get_volume_size(volume),
            "poolid": poolid
        }

        # Get the additional params from configuration
        params.update(self.configuration.cb_create_volume)

        # Override the default configuration by qos specs
        if file_system_params:
            params.update(file_system_params)

        data = self._api_request_for_cloudbyte("addVolume2", params)
        return data
    
    def _get_tsm_details(self, data, tsm_name, account_name):
        # Filter required tsm's details
        tsms = data['listTsmResponse'].get('listTsm')

        if tsms is None:
            msg = (_("No TSM was found in CloudByte storage "
                     "for account [%(account)s].") %
                   {'account': account_name})
            raise exception.VolumeBackendAPIException(data=msg)

        tsmdetails = {}
        for tsm in tsms:
            if tsm['name'] == tsm_name:
                tsmdetails = tsm
                break
        
        if not tsmdetails:
            msg = (_("TSM [%(tsm)s] was not found in CloudByte storage "
                     "for account [%(account)s].") %
                   {'tsm': tsm_name, 'account': account_name})
            raise exception.VolumeBackendAPIException(data=msg)
        
        return tsmdetails
    
    def _get_volume_from_response(self, cb_volumes, volume_name):
        """Search the volume in CloudByte storage."""

        vol_res = cb_volumes.get('listFilesystemResponse')

        if vol_res is None:
            msg = _("Null response received from CloudByte's "
                    "list filesystem.")
            raise exception.VolumeBackendAPIException(data=msg)

        volumes = vol_res.get('filesystem')

        if volumes is None:
            msg = _('No volumes found in CloudByte storage.')
            raise exception.VolumeBackendAPIException(data=msg)

        cb_volume = None

        for vol in volumes:
            if vol['name'] == volume_name:
                cb_volume = vol
                break

        if cb_volume is None:
            msg = _("Volume [%s] not found in CloudByte "
                    "storage.") % volume_name
            raise exception.VolumeBackendAPIException(data=msg)

        return cb_volume
    
    def _build_provider_details_from_volume(self, volume, chap):
        model_update = {}

        model_update['provider_location'] = (
            '%s %s %s' % (volume['ipaddress'] + ':3260', volume['path'], 0)
        )

        # CHAP Authentication related
        model_update['provider_auth'] = None

        if chap:
            model_update['provider_auth'] = ('CHAP %(username)s %(password)s'
                                             % chap)

        model_update['provider_id'] = volume['id']

        LOG.debug("CloudByte volume iqn: [%(iqn)s] provider id: [%(proid)s].",
                  {'iqn': volume['path'], 'proid': volume['id']})

        return model_update
    
    def _add_volume_iscsi_service(self, volumeid):
        params = {
            "volumeid": volumeid,
            "status": 'true'
        }

        self._api_request_for_cloudbyte(
            'addVolumeiSCSIService', params)
        
    def _update_qos_group_on_controller(self, qosid, tsmid):
        params = {
            "type": "qosgroup",
            "qosid": qosid,
            "tsmid": tsmid
        }

        self._api_request_for_cloudbyte(
            'updateController', params)
        
    def _update_storage_on_controller(self, storageid, tsmid):
        params = {
            "type": "storage",
            "storageid": storageid,
            "tsmid": tsmid
        }

        self._api_request_for_cloudbyte(
            'updateController', params)
    
    def _configure_volume_iscsi_on_controller(self, viscsiid):
        params = {
            "type": 'configurevolumeiscsi',
            "viscsiid": viscsiid
        }

        self._api_request_for_cloudbyte(
            'updateController', params)

    def create_volume(self, volume):

        qos_group_params = {}
        file_system_params = {}

        tsm_name = self.configuration.cb_tsm_name
        account_name = self.configuration.cb_account_name

        # Get account id of this account
        account_id = self._get_account_id_from_name(account_name)

        ctxt = context.get_admin_context()
        type_id = volume.get('volume_type_id')
        
        if type_id is not None:
            # extract all the extra specs from volume type
            extra_specs = self._get_extra_specs_by_volume_type(ctxt, type_id)
    
            # check if the creation is meant for OpenStack migration purposes 
            if self._check_create_for_migration(volume, extra_specs):
                provider = self._create_volume_for_migration(volume, extra_specs)
                if provider is not None:
                    return provider
                else:
                    msg = _("create cb volume - failed "
                            "- error during create for migration "
                            "- volume: '%s'") % volume['id']
                    raise exception.VolumeBackendAPIException(data=msg)

        
            qos_group_params, file_system_params = (
                self._get_qos_by_volume_type(ctxt, type_id, extra_specs))

        # Set backend storage volume name using OpenStack volume id
        cb_volume_name = volume['id'].replace("-", "")

        LOG.debug("Will create a volume [%(cb_vol)s] in TSM [%(tsm)s] "
                  "at CloudByte storage w.r.t "
                  "OpenStack volume [%(stack_vol)s].",
                  {'cb_vol': cb_volume_name,
                   'stack_vol': volume.get('id'),
                   'tsm': tsm_name})

        tsm_data = self._request_tsm_details(account_id)
        tsm_details = self._get_tsm_details(tsm_data, tsm_name, account_name)

        # Send request to create a qos group before creating a volume
        LOG.debug("Creating qos group for CloudByte volume [%s].",
                  cb_volume_name)
        
        qos_data = self._add_qos_group_request(
            volume, tsm_details.get('id'), tsm_details.get('datasetid'), cb_volume_name, qos_group_params)

        # Extract the qos group id from response
        qosgroupid = qos_data['addqosgroupresponse']['qosgroup']['id']

        LOG.debug("Successfully created qos group for CloudByte volume [%s].",
                  cb_volume_name)

        # Send a create volume request to CloudByte API
        vol_data = self._create_volume_request(
            volume, tsm_details.get('datasetid'), qosgroupid,
            tsm_details.get('id'), tsm_details.get('poolid'), cb_volume_name, file_system_params)

        # Since create volume is an async call;
        # need to confirm the creation before proceeding further
        #self._wait_for_volume_creation(vol_data, cb_volume_name)

        # Fetch iscsi id
        cb_volumes = self._api_request_for_cloudbyte(
            'listFileSystem', params={})
        cb_volume = self._get_volume_from_response(cb_volumes,
                                                      cb_volume_name)
        
        self._add_volume_iscsi_service(cb_volume['id'])
        self._update_qos_group_on_controller(cb_volume['groupid'], tsm_details.get('id'))
        self._update_storage_on_controller(cb_volume['id'], tsm_details.get('id'))
        
        params = {"storageid": cb_volume['id']}

        iscsi_service_data = self._api_request_for_cloudbyte(
            'listVolumeiSCSIService', params)
        iscsi_id = self._get_iscsi_service_id_from_response(
            cb_volume['id'], iscsi_service_data)

        self._configure_volume_iscsi_on_controller(iscsi_id)
        
        # Fetch the initiator group ID
        params = {"accountid": account_id}

        iscsi_initiator_data = self._api_request_for_cloudbyte(
            'listiSCSIInitiator', params)

        ig_name = self.configuration.cb_initiator_group_name

        ig_id = self._get_initiator_group_id_from_response(
            iscsi_initiator_data, ig_name)

        LOG.debug("Updating iscsi service for CloudByte volume [%s].",
                  cb_volume_name)

        ag_id = None
        chap_info = {}

        if self.cb_use_chap is True:
            chap_info = self._get_chap_info(account_id)
            ag_id = chap_info['ag_id']

        # Update the iscsi service with above fetched iscsi_id & ig_id
        self._request_update_iscsi_service(iscsi_id, ig_id, ag_id)

        LOG.debug("CloudByte volume [%(vol)s] updated with "
                  "iscsi id [%(iscsi)s] and initiator group [%(ig)s] and "
                  "authentication group [%(ag)s].",
                  {'vol': cb_volume_name, 'iscsi': iscsi_id,
                   'ig': ig_id, 'ag': ag_id})

        # Provide the model after successful completion of above steps
        provider = self._build_provider_details_from_response(
            cb_volumes, cb_volume_name, chap_info)

        LOG.info(_LI("Successfully created a CloudByte volume [%(cb_vol)s] "
                     "w.r.t OpenStack volume [%(stack_vol)s]."),
                 {'cb_vol': cb_volume_name, 'stack_vol': volume.get('id')})

        return provider