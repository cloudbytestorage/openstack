# Copyright 2014 CloudByte Inc.
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

import json
import time

import httplib

from cinder import context
from cinder import exception
from cinder.openstack.common import log as logging
from cinder.volume.drivers.cloudbyte.options import (
    cloudbyte_create_volume_opts
)
from cinder.volume.drivers.cloudbyte.options import cloudbyte_add_qosgroup_opts
from cinder.volume.drivers.cloudbyte.options import cloudbyte_connection_opts
from cinder.volume.drivers.cloudbyte.options import (
    cloudbyte_initiator_group_opts
)
from cinder.volume.drivers.san.san import SanISCSIDriver

LOG = logging.getLogger(__name__)


class CloudByteISCSIDriver(SanISCSIDriver):

    """CloudByte ISCSI Driver.

    Version history:
        1.0.0 - Initial driver
        1.1.0 - Dynamic VSM changes
        1.1.1 - Initiator Group changes
        1.2.0 - Optimzied API request changes
        1.2.1 - Setup Error Detection
              - Volume Create failure detection
              - Update ig to None before delete volume
              - Delete wait logic
    """

    # Version of this Cinder driver
    VERSION = '1.2.1'

    # Params used for CB REST calls.
    # These are provided from Cinder API layer
    SAN_IP = 'san_ip'
    API_KEY = 'apiKey'

    TSM_ID = 'tsmid'
    ACCOUNT_ID = 'accountid'
    DATASET_ID = 'datasetid'
    QOS_GROUP_ID = 'qosgroupid'

    ACCOUNT_NAME = 'account_name'
    TSM_NAME = 'tsm_name'

    # QOS RELATED
    IOPS = 'iops'
    LATENCY = 'latency'
    GRACEALLOWED = 'graceallowed'
    NETWORKSPEED = 'networkspeed'
    MEMLIMIT = 'memlimit'
    TPCONTROL = 'tpcontrol'
    THROUGHPUT = 'throughput'
    IOPSCONTROL = 'iopscontrol'

    # CREATE VOL RELATED
    BLOCKLENGTH = 'blocklength'
    COMPRESSION = 'compression'
    DEDUPLICATION = 'deduplication'
    SYNC = 'sync'
    RECORDSIZE = 'recordsize'
    PROTOCOLTYPE = 'protocoltype'

    volume_stats = {}

    def __init__(self, *args, **kwargs):
        super(CloudByteISCSIDriver, self).__init__(*args, **kwargs)
        self.configuration.append_config_values(cloudbyte_add_qosgroup_opts)
        self.configuration.append_config_values(cloudbyte_create_volume_opts)
        self.configuration.append_config_values(cloudbyte_connection_opts)
        self.configuration.append_config_values(cloudbyte_initiator_group_opts)
        self.get_volume_stats()

    def _get_url(self, cmd, params):
        """Will prepare URL that connects to CloudByte."""

        url = ('/client/api?' + 'command=' + cmd + '&response=json')

        for key in params:
            value = params[key]

            # build the URL string excluding the apiKey
            if value is not None and key != self.API_KEY:
                url += '&' + key + '=' + str(value)

            # set the api key that will be included later
            if value is not None and key == self.API_KEY:
                apistring = '&' + key + '=' + str(value)

        LOG.debug("CloudByte URL to be executed: %s", url)

        # add the apikey now
        url = url + apistring

        return url

    def check_for_setup_error(self):
        """Returns an error if config values aren't correct."""

        id_params = {}
        name_params = {}

        # Gathering ID's from /etc/cinder/cinder.conf
        id_params = self._fetch_volume_params_by_ids_from_config()

        # Gathering NAME's from /etc/cinder/cinder.conf
        if id_params is None:
            name_params = self._fetch_volume_params_by_names_from_config()

        cmd = "listTsm"

        tsm_data = self._api_request_for_cloudbyte(cmd, {})
        tsm_data = tsm_data["listTsmResponse"]
        tsm_data = tsm_data["listTsm"]
        tsm_data = tsm_data[0]

        # If IDs then check for valid IDs
        if id_params is not None:
            self._ids_validity_check(id_params, tsm_data)
        # If Names then check for valid names
        else:
            self._names_validity_check(name_params, tsm_data)

        return

    def _ids_validity_check(self, id_params, tsm_data):
        """Throws an exception if ID values aren't correct."""

        # Gathering ID's from params
        cb_accountid = id_params.get(self.ACCOUNT_ID)
        cb_datasetid = id_params.get(self.DATASET_ID)
        cb_tsmid = id_params.get(self.TSM_ID)

        # Invalid ID's List
        invalid_ids = []

        if (cb_accountid is not None and
           cb_accountid != tsm_data.get("accountid")):
            invalid_ids.append("cb_account_id")

        if cb_tsmid is not None and cb_tsmid != tsm_data.get("id"):
            invalid_ids.append("cb_tsm_id")

        if (cb_datasetid is not None and
           cb_datasetid != tsm_data.get("datasetid")):
            invalid_ids.append("cb_dataset_id")

        if invalid_ids:
            raise exception.InvalidInput(
                reason=("Cinder configuration has invalid values"
                        " [%s] w.r.t CloudByte Storage.") %
                ', '.join(invalid_ids))

        return

    def _names_validity_check(self, name_params, tsm_data):
        """Throws an exception if ID values aren't correct."""

        # Gathering Name's from params
        tsm_name = name_params.get(self.TSM_NAME)
        cb_accountname = name_params.get(self.ACCOUNT_NAME)

        # Invalid NAME's List
        invalid_names = []

        if tsm_name is not None and tsm_name != tsm_data.get("name"):
            invalid_names.append("tsm_name")

        if (cb_accountname is not None and
           cb_accountname != tsm_data.get("accountname")):
            invalid_names.append("cb_account_name")

        if invalid_names:
            raise exception.InvalidInput(
                reason=("Cinder configuration has invalid values"
                        " [%s] w.r.t CloudByte Storage.") %
                ', '.join(invalid_names))
        return

    def _extract_http_error(self, error_data):
        # extract the error message from error_data
        error_msg = ""

        keys = list(error_data)
        if keys is not None and len(keys) > 0:
            # error_data is a single key value dict
            msg = error_data.get(keys[0])
            # we are interested for the error
            error_msg = msg.get('errortext')

        return error_msg

    def _get_response_details(self, host, url):
        """Will prepare response after executing an http request."""

        res_details = {}
        try:
            # prepare the connection
            connection = httplib.HTTPSConnection(host)
            # make the connection
            connection.request('GET', url)
            # extract the response as the connection was successful
            response = connection.getresponse()
            # read the response
            data = response.read()
            # transform the json string into a py object
            data = json.loads(data)
            # extract http error msg if any
            error_details = None
            if response.status is not 200:
                error_details = self._extract_http_error(data)

            # prepare the return object
            res_details['data'] = data
            res_details['error'] = error_details
            res_details['http_status'] = response.status

        finally:
            connection.close()
            LOG.debug("CloudByte connection was closed successfully.")

        return res_details

    def _api_request_for_cloudbyte(self, cmd, params):
        """Make http calls to CloudByte."""
        LOG.debug("Executing CloudByte API for cmd " + cmd)

        api_key = params.get(self.API_KEY)
        if api_key is None:
            # fetch from configuration
            api_key = self.configuration.cb_apikey
            params[self.API_KEY] = api_key

        host = params.get(self.SAN_IP)
        if host is None:
            # fetch from configuration
            host = self.configuration.san_ip

        # construct the CloudByte URL with query params
        url = self._get_url(cmd, params)

        # response data container
        data = {}

        # response error container
        error_msg = None

        try:
            # Flag that determines if CloudByte API should be called
            is_first_call = True
            # Flag that determines a retry of the same API request
            is_retry_call = False
            # response details container
            res_obj = {}

            while is_first_call or is_retry_call:
                # reset the first call
                is_first_call = False
                # reset the error message
                error_msg = None
                # execute CloudByte API & frame the response
                res_obj = self._get_response_details(host, url)
                # extract data from response
                data = res_obj['data']
                # extract error from response if any
                error_details = res_obj['error']
                # extract http status of response
                http_status = res_obj['http_status']
                # check if it was an error response from CloudByte
                if http_status is not 200:
                    error_msg = ("Failed executing CloudByte API " + cmd +
                                 ". Http status: " + str(http_status) +
                                 ", Error: ") + str(error_details)
                    LOG.error(error_msg)

                    # Try again if there was no error message from CloudByte
                    # & it was not a success as well on its first attempt.
                    if error_details is None and not is_retry_call:
                        # Sleep for couple of seconds
                        time.sleep(2)
                        # set retry to true
                        is_retry_call = True
                        # log the retry
                        LOG.debug("Will retry CloudByte API for command "
                                  + cmd)
                    else:
                        # This seems to be a genuine error.
                        # Or retry attempt is exhausted.
                        # Hence, no more retries.
                        is_retry_call = False
                else:
                    # We received 200 as http status. Hence, no retries.
                    is_retry_call = False

        except Exception as ex:
            msg = ("Error executing CloudByte API %(cmd)s, Error: %(err)s" %
                   {'cmd': cmd, 'err': ex})
            LOG.error(msg)
            raise exception.VolumeBackendAPIException(msg)

        if error_msg is not None:
            raise exception.VolumeBackendAPIException(error_msg)

        LOG.debug("CloudByte API executed successfully for cmd " + cmd)
        return data

    def _request_tsm_details(self, account_id, vol_metadata):
        params = {}
        params[self.ACCOUNT_ID] = account_id

        self._update_http_conn_params(params, vol_metadata)

        # list all CloudByte tsm
        data = self._api_request_for_cloudbyte("listTsm", params)
        return data

    def _override_params(self, filtered_user_dict, default_dict):
        """This method fetches default config values from configuration file.

        These default values are overridden with user provided values.
        """

        if filtered_user_dict is None or len(filtered_user_dict) == 0:
            # Nothing to override
            return default_dict

        # Do not override default_dict
        new_opts_dict = {}

        for key, value in default_dict.iteritems():
            # fill the dict with default options
            if value is not None:
                new_opts_dict[key] = value

        # iterate the user provided dict & override the new dict
        for key, value in filtered_user_dict.iteritems():
            # override the default dict with user provided dict
            if value is not None:
                new_opts_dict[key] = value

        return new_opts_dict

    def _get_qos_props(self, volume_metadata):
        qos_props = {}

        # Set QoS related properties
        # The right hand constants are this driver specific
        # The right hand constants may or maynot match CB storage
        qos_props['iops'] = volume_metadata.get(self.IOPS)
        qos_props['latency'] = volume_metadata.get(self.LATENCY)
        qos_props['graceallowed'] = volume_metadata.get(self.GRACEALLOWED)
        qos_props['networkspeed'] = volume_metadata.get(self.NETWORKSPEED)
        qos_props['memlimit'] = volume_metadata.get(self.MEMLIMIT)
        qos_props['tpcontrol'] = volume_metadata.get(self.TPCONTROL)
        qos_props['throughput'] = volume_metadata.get(self.THROUGHPUT)
        qos_props['iopscontrol'] = volume_metadata.get(self.IOPSCONTROL)

        return qos_props

    def _get_vol_props(self, volume_metadata):

        vol_props = {}

        # Set volume related properties
        # The right hand constants are this driver specific
        # The right hand constants may or maynot match CB storage
        vol_props['blocklength'] = volume_metadata.get(self.BLOCKLENGTH)
        vol_props['compression'] = volume_metadata.get(self.COMPRESSION)
        vol_props['deduplication'] = volume_metadata.get(self.DEDUPLICATION)
        vol_props['sync'] = volume_metadata.get(self.SYNC)
        vol_props['recordsize'] = volume_metadata.get(self.RECORDSIZE)
        vol_props['protocoltype'] = volume_metadata.get(self.PROTOCOLTYPE)

        return vol_props

    def _add_qos_group_request(self, volume, tsmid, volume_name,
                               volume_metadata):
        # extract qos_params from volume_metadata
        qos_params = self._get_qos_props(volume_metadata)

        # Add missing params from config file
        params = self._override_params(qos_params,
                                       self.configuration.add_qosgroup)

        # CloudByte specific requirements
        params['name'] = "QoS_" + volume_name
        params[self.TSM_ID] = tsmid

        # update the params with http conn info
        self._update_http_conn_params(params, volume_metadata)

        data = self._api_request_for_cloudbyte("addQosGroup", params)
        return data

    def _add_qos_params_to_volume_params(self, create_volume_params,
                                         volume_metadata):
        # extract qos_params from volume_metadata
        qos_params = self._get_qos_props(volume_metadata)

        # Add missing params from config file
        all_qos_params = self._override_params(
            qos_params,
            self.configuration.add_qosgroup)

        # Add qos params to create volume params
        for key, value in all_qos_params.iteritems():
            # fill the dict with default options
            if value is not None:
                create_volume_params[key] = value

    def _create_volume_request(self, volume, volume_name,
                               create_volume_params, vol_metadata):

        size = volume.get('size')
        quotasize = str(size) + "G"

        # prepare the user input params
        params = {}

        params[self.DATASET_ID] = create_volume_params[self.DATASET_ID]
        params['name'] = volume_name

        # qos group id is optional from v2 onwards
        if create_volume_params.get(self.QOS_GROUP_ID) is not None:
            params['qosgroupid'] = create_volume_params[self.QOS_GROUP_ID]

        params[self.TSM_ID] = create_volume_params[self.TSM_ID]
        params['quotasize'] = quotasize

        # Add the qos related props
        params['iops'] = create_volume_params.get(self.IOPS)
        params['latency'] = create_volume_params.get(self.LATENCY)
        params['graceallowed'] = create_volume_params.get(self.GRACEALLOWED)
        params['networkspeed'] = create_volume_params.get(self.NETWORKSPEED)
        params['memlimit'] = create_volume_params.get(self.MEMLIMIT)
        params['tpcontrol'] = create_volume_params.get(self.TPCONTROL)
        params['throughput'] = create_volume_params.get(self.THROUGHPUT)
        params['iopscontrol'] = create_volume_params.get(self.IOPSCONTROL)

        # Add volume related props
        params['blocklength'] = create_volume_params.get(self.BLOCKLENGTH)
        params['compression'] = create_volume_params.get(self.COMPRESSION)
        params['deduplication'] = create_volume_params.get(self.DEDUPLICATION)
        params['sync'] = create_volume_params.get(self.SYNC)
        params['recordsize'] = create_volume_params.get(self.RECORDSIZE)
        params['protocoltype'] = create_volume_params.get(self.PROTOCOLTYPE)

        # update the params with http connection info
        self._update_http_conn_params(params, vol_metadata)

        data = self._api_request_for_cloudbyte("createVolume", params)

        return data

    def _query_asyncjobresult_request(self, jobid, vol_metadata):
        async_cmd = "queryAsyncJobResult"
        params = {
            "jobId": jobid,
        }

        # update the params with http conn info
        self._update_http_conn_params(params, vol_metadata)

        data = self._api_request_for_cloudbyte(async_cmd, params)
        return data

    def _get_volume_metadata(self, volume):
        # Get the volume params from volume's metadata
        # This will be user entered params
        volume_params = volume.get('volume_metadata')

        # loop through the user volume params & perform falsy checks
        final_vol_params = {}

        # return empty dict if there is no metadata for this volume
        if volume_params is None:
            return final_vol_params

        for vol_param in volume_params:
            if vol_param.value is not None and vol_param.value != 'None':
                final_vol_params[vol_param.key] = vol_param.value

        return final_vol_params

    def _get_update_qos_params(self, vol_metadata):
        qos_params = {}

        # filter  user input params
        for key, value in vol_metadata.iteritems():
            if key == 'iops' or key == 'graceallowed':
                qos_params[key] = value
        return qos_params

    def _get_update_filesystem_params(self, vol_metadata):
        fs_params = {}
        # filter user input params
        for key, value in vol_metadata.iteritems():
            if key == 'compression' or key == 'deduplication' or key == 'sync':
                fs_params[key] = value
        return fs_params

    def _filter_tsm(self, data, tsm_name):
        # filter required tsm's details
        tsms = data['listTsmResponse']['listTsm']
        tsmdetails = {}
        for tsm in tsms:
            if tsm['name'] == tsm_name:
                tsmdetails['datasetid'] = tsm['datasetid']
                tsmdetails['tsmid'] = tsm['id']
                break

        return tsmdetails

    def _parse_create_volume_job_resp(self, job_response):
        parsed_job_response = {}

        if job_response is None:
            return parsed_job_response

        job_result = job_response.get('jobresult')

        if job_result is None:
            return parsed_job_response

        filesystem = job_result.get('filesystem')

        if filesystem is not None:
            parsed_job_response['ipaddress'] = filesystem.get('ipaddress')
            parsed_job_response['iqnname'] = filesystem.get('iqnname')
            parsed_job_response['id'] = filesystem.get('id')

        return parsed_job_response

    def _confirm_volume_creation(self, volume_response, volume_name,
                                 vol_metadata):

        vol_res = volume_response.get('createvolumeresponse')

        if vol_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received while creating volume [%s] "
                "in CloudByte storage." % volume_name)

        jobid = vol_res.get('jobid')

        if jobid is None:
            raise exception.VolumeBackendAPIException(
                "Error: Jobid not found w.r.t CloudByte's "
                " create volume [%s]." % volume_name)

        success_job_response = {}
        counter = 1
        while True:
            # wait for n seconds -- mentioned in configuration
            time.sleep(self.configuration.confirm_volume_create_retry_interval)
            # query the CloudByte with this jobid
            volume_response = (
                self._query_asyncjobresult_request(jobid, vol_metadata))
            # check the status
            result_res = volume_response.get('queryasyncjobresultresponse')

            status = 0
            if result_res is not None:
                status = result_res.get('jobstatus')
                LOG.debug("Volume [%(vol)s] creation status [%(stat)s]." %
                          {'vol': volume_name, 'stat': status})

            if status == 1:
                LOG.debug("Volume [%s] created successfully in "
                          "CloudByte", volume_name)
                success_job_response = self._parse_create_volume_job_resp(
                    result_res)
                break

            elif status == 2:
                job_result = result_res.get("jobresult")
                err_msg = job_result.get("errortext")
                err_code = job_result.get("errorcode")
                msg = ('Error creating volume [%(vol_name)s] '
                       'in CloudByte storage: [%(cb_error)s], '
                       'error code: [%(error_code)s] ' %
                       {'cb_error': err_msg,
                        'error_code': err_code,
                        'vol_name': volume_name})

                LOG.error(msg)
                raise exception.VolumeBackendAPIException(msg)

            elif counter == (
                self.configuration.confirm_volume_create_sleep_counter
            ):
                # All attempts exhausted
                err_msg = None
                err_code = None
                if(result_res.get("msg") == "1" or result_res.get("msg") == 1):
                    job_result = result_res.get("jobresult")
                    if(job_result is not None):
                        err_msg = job_result.get("errortext")
                        err_code = job_result.get("errorcode")

                msg = ('Delay or Error creating volume [%(vol_name)s] '
                       'in CloudByte storage: [%(cb_error)s], '
                       'error code: [%(error_code)s] ' %
                       {'cb_error': err_msg,
                        'error_code': err_code,
                        'vol_name': volume_name})

                LOG.error(msg)
                raise exception.VolumeBackendAPIException(msg)

            else:
                counter += 1
                LOG.debug("Will re-confirm [%(count)s] the volume [%(vol)s] "
                          "creation at CloudByte storage." %
                          {'count': counter, 'vol': volume_name})

        return success_job_response

    def _confirm_volume_deletion(self, volume_response, volume_id,
                                 vol_metadata):

        vol_res = volume_response.get('deleteFileSystemResponse')

        if vol_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received while deleting volume [%s] "
                "in CloudByte storage." % volume_id)

        jobid = vol_res.get('jobid')

        if jobid is None:
            raise exception.VolumeBackendAPIException(
                "Error: Jobid not found w.r.t CloudByte's "
                " delete volume [%s]." % volume_id)

        counter = 1
        while True:
            # wait for n seconds -- mentioned in configuration
            time.sleep(self.configuration.confirm_volume_delete_retry_interval)
            # query the CloudByte with this jobid
            volume_response = (
                self._query_asyncjobresult_request(jobid, vol_metadata))
            # check the status
            result_res = volume_response.get('queryasyncjobresultresponse')

            status = 0
            if result_res is not None:
                status = result_res.get('jobstatus')
                LOG.debug("Volume [%(vol)s] deletion status [%(stat)s]." %
                          {'vol': volume_id, 'stat': status})

            if status == 1:
                LOG.debug("Volume [%s] deleted successfully in "
                          "CloudByte", volume_id)
                break

            elif status == 2:
                job_result = result_res.get("jobresult")
                err_msg = job_result.get("errortext")
                err_code = job_result.get("errorcode")
                msg = ('Error deleting volume [%(vol_name)s] '
                       'in CloudByte storage: [%(cb_error)s], '
                       'error code: [%(error_code)s] ' %
                       {'cb_error': err_msg,
                        'error_code': err_code,
                        'vol_id': volume_id})

                LOG.error(msg)
                raise exception.VolumeBackendAPIException(msg)

            elif counter == (
                self.configuration.confirm_volume_create_sleep_counter
            ):
                # All attempts exhausted
                err_msg = None
                err_code = None
                if(result_res.get("msg") == "1" or result_res.get("msg") == 1):
                    job_result = result_res.get("jobresult")
                    if(job_result is not None):
                        err_msg = job_result.get("errortext")
                        err_code = job_result.get("errorcode")

                msg = ('Delay or Error deleting volume [%(vol_name)s] '
                       'in CloudByte storage: [%(cb_error)s], '
                       'error code: [%(error_code)s] ' %
                       {'cb_error': err_msg,
                        'error_code': err_code,
                        'vol_id': volume_id})

                LOG.error(msg)
                raise exception.VolumeBackendAPIException(msg)

            else:
                counter += 1
                LOG.debug("Will re-confirm [%(count)s] the volume [%(vol)s] "
                          "deletion at CloudByte storage." %
                          {'count': counter, 'vol': volume_id})

    def _get_volume_id_from_response(self, cb_volumes, volume_name):
        """Search the volume in CloudByte."""

        vol_res = cb_volumes.get('listFilesystemResponse')

        if vol_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received from CloudByte's "
                "list filesystem API.")

        volumes = vol_res.get('filesystem')

        if volumes is None:
            raise exception.VolumeBackendAPIException(
                'Error: No volumes found in CloudByte storage.')

        volume_id = None

        for vol in volumes:
            if vol['name'] == volume_name:
                volume_id = vol['id']
                break

        if volume_id is None:
            raise exception.VolumeBackendAPIException(
                "Error: Volume [%s] not found in CloudByte storage."
                % volume_name)

        return volume_id

    def _get_qosgroupid_id_from_response(self, cb_volumes, volume_id):

        volumes = cb_volumes['listFilesystemResponse']['filesystem']
        qosgroup_id = None

        for vol in volumes:
            if vol['id'] == volume_id:
                qosgroup_id = vol['groupid']
                break

        return qosgroup_id

    def _build_provider_details_from_volume(self, volume):
        model_update = {}

        model_update['provider_location'] = (
            '%s %s %s' % (volume['ipaddress'] + ':3260', volume['iqnname'], 0)
        )

        model_update['provider_auth'] = ('CHAP %s %s' % (None, None))

        LOG.debug("CloudByte volume [%(vol)s] properties: [%(props)s]" %
                  {'vol': volume['iqnname'], 'props': model_update})

        return model_update

    def _build_provider_details_from_params(self, ip_address, iqn_name):
        model_update = {}

        model_update['provider_location'] = (
            '%s %s %s' % (ip_address + ':3260', iqn_name, 0)
        )

        model_update['provider_auth'] = ('CHAP %s %s' % (None, None))

        LOG.debug("CloudByte volume properties: [%(props)s]" %
                  {'props': model_update['provider_location']})

        return model_update

    def _build_provider_details_from_response(self, cb_volumes, volume_name):
        """Get provider information."""

        model_update = {}
        volumes = cb_volumes['listFilesystemResponse']['filesystem']

        for vol in volumes:
            if vol['name'] == volume_name:
                model_update = self._build_provider_details_from_volume(vol)
                break

        return model_update

    def _build_provider_details(self, successful_vol_create_resp, volume):

        if (successful_vol_create_resp.get('ipaddress') is not None and
                successful_vol_create_resp.get('iqnname') is not None):

            return self._build_provider_details_from_params(
                successful_vol_create_resp.get('ipaddress'),
                successful_vol_create_resp.get('iqnname'))
        else:
            return self._build_provider_details_from_volume(volume)

    def _get_initiator_group_id_from_response(self, data, ig_filter):
        """Find iSCSI initiator group id."""

        ig_list_res = data.get('listInitiatorsResponse')

        if ig_list_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received from CloudByte's "
                "list iscsi initiators API.")

        ig_list = ig_list_res.get('initiator')

        if ig_list is None:
            raise exception.VolumeBackendAPIException(
                'Error: No iscsi initiators were found in CloudByte storage.')

        ig_id = None

        # Filter the initiator group set in configuration
        # It is expected to have this initiator group name available
        # in CloudByte storage
        for ig in ig_list:
            if ig.get('initiatorgroup') == ig_filter:
                LOG.debug("Initiator group [%(ig)s] "
                          "will be set against the CloudByte storage volume.",
                          {'ig': ig_filter})
                ig_id = ig['id']
                break

        if ig_id is None:
            raise exception.VolumeBackendAPIException(
                "Initiator group [%s] not found at CloudByte "
                "storage." % ig_filter)

        return ig_id

    def _get_iscsi_service_id_from_response(self, volume_id, data):

        iscsi_service_res = data.get('listVolumeiSCSIServiceResponse')

        if iscsi_service_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received from CloudByte's "
                "list volume iscsi service API.")

        iscsi_service_list = iscsi_service_res.get('iSCSIService')

        if iscsi_service_list is None:
            raise exception.VolumeBackendAPIException(
                'Error: No iscsi services found in CloudByte storage.')

        iscsi_id = None

        for iscsi_service in iscsi_service_list:
            if iscsi_service['volume_id'] == volume_id:
                iscsi_id = iscsi_service['id']
                break

        if iscsi_id is None:
            raise exception.VolumeBackendAPIException(
                'Error: No iscsi service found for CloudByte volume [%s].'
                % volume_id)
        else:
            return iscsi_id

    def _request_update_iscsi_service(self, iscsi_id, ig_id, vol_metadata):

        params = {
            "id": iscsi_id,
            "igid": ig_id
        }

        self._update_http_conn_params(params, vol_metadata)

        self._api_request_for_cloudbyte(
            'updateVolumeiSCSIService', params)

    def _get_cb_snapshot_path(self, snapshot, volume_id, vol_metadata):
        """Find CloudByte snapshot path."""

        params = {
            "id": volume_id
        }

        self._update_http_conn_params(params, vol_metadata)

        # list all snapshot from CloudByte
        cb_snapshots_list = self._api_request_for_cloudbyte(
            'listStorageSnapshots', params)

        # filter required snapshot from list
        cb_snap_res = cb_snapshots_list.get('listDatasetSnapshotsResponse')

        cb_snapshot = {}
        if cb_snap_res is not None:
            cb_snapshot = cb_snap_res.get('snapshot')

        path = None

        # filter snapshot path
        for snap in cb_snapshot:
            if snap['name'] == snapshot['display_name']:
                path = snap['path']
                LOG.debug("snapshot path: %s", path)
                break

        return path

    def _get_storage_info(self, tsmname):
        """Get CloudByte tsm that is associated with openstack."""

        # list all tsms from CloudByte
        tsm_list = self._api_request_for_cloudbyte('listTsm', params={})

        tsm_details_res = tsm_list.get('listTsmResponse')

        if tsm_details_res is None:
            raise exception.VolumeBackendAPIException(
                'Error: Null response from CloudByte list tsm API.')

        tsm_details = tsm_details_res.get('listTsm')

        data = {}
        flag = 0
        # filter required tsm and get storage info
        for tsms in tsm_details:

            if tsms['name'] == tsmname:
                flag = 1
                storage_buckets = {}
                storage_buckets = tsms['storageBuckets']
                quota = 0
                for bucket in storage_buckets:
                    quota = bucket['quota']
                    break

                data['total_capacity_gb'] = quota
                data['free_capacity_gb'] = (
                    int(int(tsms['availablequota']) / 1000))

        # tsm not found in CloudByte
        if flag == 0:
            data['total_capacity_gb'] = 0
            data['free_capacity_gb'] = 0

        return data

    def _get_account_id_from_name(self, account_name, vol_metadata):

        params = {}

        self._update_http_conn_params(params, vol_metadata)

        data = self._api_request_for_cloudbyte("listAccount", params)
        accounts = data["listAccountResponse"]["account"]

        account_id = None
        for account in accounts:
            if account.get("name") == account_name:
                account_id = account.get("id")
                break

        if account_id is None:
            raise exception.VolumeBackendAPIException(
                "Error: Failed to get CloudByte storage account details"
                " for account name [%s]." % account_name)

        return account_id

    def _search_volume_id(self, cb_volumes, cb_volume_id):
        """Filter the volume from the list passed."""

        volumes_res = cb_volumes.get('listFilesystemResponse')

        if volumes_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received from CloudByte's "
                "list filesystem API.")

        volumes = volumes_res.get('filesystem')

        volume_id = None

        if volumes is not None:
            for vol in volumes:
                if vol['id'] == cb_volume_id:
                    volume_id = vol['id']
                    break

        return volume_id

    def _generate_clone_name(self):
        """Generates clone name when it is not provided."""

        clone_name = ("clone" + time.strftime("%d%m%Y") +
                      time.strftime("%H%M%S"))
        return clone_name

    def _generate_snapshot_name(self):
        """Generates snapshot_name when it is not provided."""

        snapshot_name = ("snap" + time.strftime("%d%m%Y") +
                         time.strftime("%H%M%S"))
        return snapshot_name

    def _update_http_conn_params(self, params, vol_metadata):
        """Updates the params with http related info."""

        api_key = None
        san_ip = None

        if params is None:
            params = {}

        if vol_metadata is not None:
            api_key = vol_metadata.get(self.API_KEY)
            san_ip = vol_metadata.get(self.SAN_IP)

        if api_key is not None:
            params[self.API_KEY] = api_key

        if san_ip is not None:
            params[self.SAN_IP] = san_ip

    def _fetch_volume_param_ids_from_names(self, names,
                                           vol_metadata):
        if names is None:
            return None

        # get account id from account_name
        account_id = self._get_account_id_from_name(
            names[self.ACCOUNT_NAME],
            vol_metadata)
        # get tsm details from account_id
        tsm_data = self._request_tsm_details(account_id, vol_metadata)
        # filter the required tsm based on tsm_name
        tsm_details = self._filter_tsm(tsm_data, names[self.TSM_NAME])

        # validate & raise exception if validation failed
        if(len(tsm_details) <= 0):
            raise exception.VolumeBackendAPIException(
                "TSM [%s] not found at CloudByte storage."
                % names[self.TSM_NAME])

        # populate the ids of tsm, dataset & account
        ids = {}
        # set the account_id
        ids[self.ACCOUNT_ID] = account_id
        # extract dataset id & update the dict
        ids[self.DATASET_ID] = tsm_details.get('datasetid')
        # extract tsmid & update the dict
        ids[self.TSM_ID] = tsm_details.get('tsmid')

        return ids

    def _fetch_volume_params_by_ids_from_meta(self, vol_metadata):
        params = None
        tsm_id = None
        dataset_id = None
        account_id = None

        if vol_metadata is not None:
            # Fetch them from metadata using IDs (fast)
            tsm_id = vol_metadata.get(self.TSM_ID)
            dataset_id = vol_metadata.get(self.DATASET_ID)
            account_id = vol_metadata.get(self.ACCOUNT_ID)

        if (tsm_id and dataset_id and account_id):
            # All parameters are provided
            params = {}
            params[self.TSM_ID] = tsm_id
            params[self.DATASET_ID] = dataset_id
            params[self.ACCOUNT_ID] = account_id
        elif (tsm_id or dataset_id or account_id):
            # It is expected to provide All or None
            raise exception.VolumeBackendAPIException(
                "TSM ID, Dataset ID and Account ID should be set "
                "in the metadata to create volume at CloudByte storage.")

        return params

    def _fetch_volume_params_by_names_from_meta(self, vol_metadata):
        params = None
        tsm_name = None
        account_name = None

        # fetch by names
        if vol_metadata is not None:
            tsm_name = vol_metadata.get(self.TSM_NAME)
            account_name = vol_metadata.get(self.ACCOUNT_NAME)

        if tsm_name and account_name:
            LOG.debug("TSM [%(tsm)s] and Account [%(ac)s]"
                      " will be used to create a volume at CloudByte storage.",
                      {'tsm': tsm_name, 'ac': account_name})
            params = {}
            params[self.TSM_NAME] = tsm_name
            params[self.ACCOUNT_NAME] = account_name
        elif tsm_name or account_name:
            raise exception.VolumeBackendAPIException(
                'Both TSM name and Account name should be set in the metadata '
                'to create a volume at CloudByte storage.')

        return params

    def _fetch_volume_params_by_ids_from_config(self):
        # populate the ids of tsm, dataset & account
        params = {}
        # set the account_id
        params[self.ACCOUNT_ID] = (
            self.configuration.safe_get('cb_account_id') or None)

        # extract dataset id & update the params dict
        params[self.DATASET_ID] = (
            self.configuration.safe_get('cb_dataset_id') or None)

        # extract tsmid & update the params dict
        params[self.TSM_ID] = (
            self.configuration.safe_get('cb_tsm_id') or None)

        if (params[self.ACCOUNT_ID] is not None
                and params[self.DATASET_ID] is not None
                and params[self.TSM_ID] is not None):
            return params
        elif (params[self.ACCOUNT_ID] is not None
              or params[self.DATASET_ID] is not None
              or params[self.TSM_ID] is not None):
            # It is expected to provide All or None
            raise exception.VolumeBackendAPIException(
                "TSM ID, Dataset ID and Account ID must be set in the config "
                "to create volume at CloudByte storage.")
        else:
            return None

    def _fetch_volume_params_by_names_from_config(self):
        tsm_name = None
        account_name = None

        # Get TSM/VSM & Account names from configuration
        tsm_name = self.configuration.tsm_name
        account_name = self.configuration.cb_account_name

        # Raise exception if tsm_name is not found
        if (tsm_name is None
                or tsm_name == ''
                or account_name is None
                or account_name == ''):
            raise exception.VolumeBackendAPIException(
                'TSM Name and Account Name must be set in the config '
                'create a volume at CloudByte storage.')

        params = {}
        params[self.TSM_NAME] = tsm_name
        params[self.ACCOUNT_NAME] = account_name
        return params

    def _build_create_volume_params(self, vol_metadata):
        """Returns the required params to create a volume
        in CloudByte."""
        params = None

        # Fetch them from metadata using IDs (fast)
        params = self._fetch_volume_params_by_ids_from_meta(vol_metadata)

        if params is None:
            # Fetch them from metadata using Names (slow)
            params = self._fetch_volume_params_by_names_from_meta(vol_metadata)
            params = self._fetch_volume_param_ids_from_names(
                params,
                vol_metadata)

        if params is None:
            # Fetch them from config using IDs (fast)
            params = self._fetch_volume_params_by_ids_from_config()

        if params is None:
            # Fetch them from config using Names (slow)
            params = self._fetch_volume_params_by_names_from_config()
            params = self._fetch_volume_param_ids_from_names(
                params,
                vol_metadata)

        return params

    def _sanitize_name(self, name):

        # Will remove the characters not supported by this driver
        substitutions = [
            ('-', ''),
            ('_', ''),
            ('+', ''),
            (' ', '')]

        for search, replacement in substitutions:
            name = name.replace(search, replacement)

        return name

    def create_volume(self, volume):

        # getting admin context
        ctxt = context.get_admin_context()
        vol_metadata = {"cb_volume_id": 'None'}

        # Insert volume id in volume_metadata
        # This is a new record inserted by this plugin
        self.db.volume_metadata_update(
            ctxt, volume.get('id'), vol_metadata, False)

        # Below volume metadata refers to the dict that user had sent
        # during volume creation.
        # It will also have above record that was just created.
        vol_metadata = self.db.volume_metadata_get(
            ctxt, volume.get('id'))

        # get/create the volume name
        volume_name = None
        if volume['display_name'] is not None and volume['display_name'] != '':
            volume_name = volume['display_name']
            volume_name = self._sanitize_name(volume_name)
        else:
            volume_name = self._sanitize_name(volume['id'])

        # get the create volume params
        create_volume_params = self._build_create_volume_params(vol_metadata)

        self._add_volume_props_to_volume_params(
            ctxt,
            create_volume_params,
            vol_metadata)

        self._create_qos_group(
            ctxt,
            create_volume_params,
            volume_name,
            vol_metadata)

        # Send a create volume request to CloudByte API
        vol_data = self._create_volume_request(
            volume,
            volume_name,
            create_volume_params,
            vol_metadata)

        # Since create volume is an async call;
        # need to confirm the creation before proceeding further
        success_job_response = (
            self._confirm_volume_creation(vol_data, volume_name, vol_metadata))

        # CB Volume
        cb_volume = None
        volume_id = success_job_response.get('id')

        if volume_id is None:
            cb_volume = self._get_cb_volume_from_metadata(
                vol_metadata,
                volume_name)

            volume_id = cb_volume.get('id')

        # Fetch iscsi ID
        list_vol_iscsi_ser_params = {
            "storageid": volume_id
        }
        self._update_http_conn_params(list_vol_iscsi_ser_params, vol_metadata)

        iscsi_service_data = self._api_request_for_cloudbyte(
            'listVolumeiSCSIService', list_vol_iscsi_ser_params)

        iscsi_id = self._get_iscsi_service_id_from_response(
            volume_id, iscsi_service_data)

        # fetch the initiator group ID
        list_iscsi_init_params = {}

        list_iscsi_init_params[self.ACCOUNT_ID] = create_volume_params[
            self.ACCOUNT_ID]

        self._update_http_conn_params(list_iscsi_init_params, vol_metadata)

        iscsi_initiator_data = self._api_request_for_cloudbyte(
            'listiSCSIInitiator', list_iscsi_init_params)

        ig_name = self.configuration.cb_initiator_group_name

        ig_id = self._get_initiator_group_id_from_response(
            iscsi_initiator_data, ig_name)

        LOG.debug("Updating iscsi service for CloudByte volume: [%s]",
                  volume_name)

        # update the iscsi service with above fetched iscsi_id & ig_id
        self._request_update_iscsi_service(iscsi_id, ig_id, vol_metadata)

        LOG.debug("CloudByte Volume: [%(vol)s] updated with "
                  "iscsi id: [%(iscsi)s] and ig id: [%(ig)s]",
                  {'vol': volume_name, 'iscsi': iscsi_id, 'ig': ig_id})

        # Update CloudByte volume id in volume_metadata
        vol_metadata = {"cb_volume_id": volume_id}
        self.db.volume_metadata_update(
            ctxt, volume['id'], vol_metadata, False)

        # provide the model after successful completion of above steps
        provider = self._build_provider_details(
            success_job_response,
            cb_volume)

        LOG.info("Successfully created a CloudByte volume [%(cb_vol)s] "
                 "w.r.t openstack volume [%(stack_vol)s]",
                 {'cb_vol': volume_name, 'stack_vol': volume.get('id')})

        return provider

    def _add_volume_props_to_volume_params(self, context,
                                           create_volume_params,
                                           volume_metadata):
        # Extract vol props from volume_metadata
        vol_props = self._get_vol_props(volume_metadata)

        # Add the missing vol props from configuration
        vol_props = self._override_params(
            vol_props,
            self.configuration.create_volume)

        vol_props = self._filter_vol_props(vol_props)

        # Add vol params to create volume params
        for key, value in vol_props.iteritems():
            if value is not None:
                create_volume_params[key] = value

    def _filter_vol_props(self, all_props):
        vol_props = {}

        if all_props:
            qos = ['blocklength', 'compression', 'deduplication', 'sync',
                   'recordsize', 'protocoltype']
            for key, value in all_props.iteritems():
                if key in qos and value is not None:
                    vol_props[key] = value
        return vol_props

    def _create_qos_group(self, context, create_volume_params,
                          volume_name,
                          vol_metadata):
        """This will create a QoS Group or will provide QoS props."""

        qosgroupid = None

        # send request to create a qos group
        LOG.debug("Creating qos group for CloudByte volume [%s].", volume_name)
        qos_data = self._add_qos_group_request(
            context,
            create_volume_params[self.TSM_ID],
            volume_name,
            vol_metadata)

        # extract the qos group id from response
        qosgroupid = qos_data['addqosgroupresponse']['qosgroup']['id']

        LOG.debug(
            "Successfully created qos group for"
            " CloudByte volume [%s]", volume_name)

        create_volume_params[self.QOS_GROUP_ID] = qosgroupid

    def _get_cb_volume_from_metadata(self, vol_metadata, volume_name):
        listfilesysparams = {}
        self._update_http_conn_params(listfilesysparams, vol_metadata)

        cb_volumes = self._api_request_for_cloudbyte(
            'listFileSystem', listfilesysparams)

        cb_volume = self._get_cb_volume_from_list(
            cb_volumes,
            volume_name)

        return cb_volume

    def _get_cb_volume_from_list(self, cb_volumes, volume_name):
        """Search the volume in CloudByte."""

        vol_res = cb_volumes.get('listFilesystemResponse')

        if vol_res is None:
            raise exception.VolumeBackendAPIException(
                "Error: Null response received from CloudByte's "
                "list filesystem API.")

        volumes = vol_res.get('filesystem')

        if volumes is None:
            raise exception.VolumeBackendAPIException(
                'Error: No volumes found at CloudByte storage.')

        volume = None

        for vol in volumes:
            if vol['name'] == volume_name:
                volume = vol
                break

        if volume is None:
            raise exception.VolumeBackendAPIException(
                "Error: Volume [%s] not found at CloudByte storage."
                % volume_name)

        return volume

    def delete_volume(self, volume):

        # get admin context
        ctxt = context.get_admin_context()

        # openstack source volume id
        source_volume_id = volume['id']

        # get volume metadata
        vol_metadata = self.db.volume_metadata_get(
            ctxt, source_volume_id)

        # finding CB volume id w.r.t. openstack source volume
        cb_volume_id = vol_metadata.get('cb_volume_id')

        LOG.debug("CloudByte storage volume [%(cb_vol)s] will be deleted "
                  " w.r.t OpenStack volume [%(stack_vol)s]",
                  {'cb_vol': cb_volume_id, 'stack_vol': source_volume_id})

        #  delete volume at CloudByte
        if cb_volume_id is not None and cb_volume_id != 'None':

            params = {}

            self._update_http_conn_params(params, vol_metadata)

            cb_volumes = self._api_request_for_cloudbyte(
                'listFileSystem', params)

            # search cb_volume_id in CloudByte volumes
            # incase it has already been deleted from CloudByte
            cb_volume_id = self._search_volume_id(cb_volumes, cb_volume_id)

            # delete volume at CloudByte
            if cb_volume_id is not None:
                # Need to set the initiator group to None before deleting
                self._update_initiator_group(
                    cb_volume_id,
                    'None',
                    vol_metadata)

                LOG.debug("Will delete CloudByte storage volume [%(cb_vol)s] "
                          "w.r.t OpenStack volume [%(stack_vol)s]",
                          {'cb_vol': cb_volume_id,
                           'stack_vol': source_volume_id})

                params = {
                    "id": cb_volume_id
                }

                self._update_http_conn_params(params, vol_metadata)

                del_res = (
                    self._api_request_for_cloudbyte('deleteFileSystem', params)
                )

                # Volume delete retry call
                self._confirm_volume_deletion(
                    del_res,
                    cb_volume_id,
                    vol_metadata)

                LOG.info("Successfully deleted CloudByte storage volume "
                         "[%(cb_vol)s] w.r.t OpenStack volume [%(stack_vol)s]",
                         {'cb_vol': cb_volume_id,
                          'stack_vol': source_volume_id})

            else:
                LOG.error("CloudByte storage does not have any volume "
                          "corresponding to OpenStack volume [%s]",
                          source_volume_id)

        else:
            LOG.error("CloudByte volume details (i.e. metadata) is not "
                      "available for its corresponding OpenStack "
                      "volume [%s]", source_volume_id)

    def create_snapshot(self, snapshot):
        """Creates a snapshot at CloudByte."""

        # volume id of openstack
        source_volume_id = snapshot['volume_id']

        # get admin context
        ctxt = context.get_admin_context()

        # Create snapshot metadata before snapshot creation @ CloudByte
        # i.e. db create the snapshot metadata
        snapshot_metadata = {"cb_snapshot_path_" + snapshot['id']: 'None'}
        self.db.volume_metadata_update(
            ctxt, source_volume_id, snapshot_metadata, False)

        # Fetch source volume metadata record
        src_vol_metadata = self.db.volume_metadata_get(
            ctxt, source_volume_id)

        # Get CloudByte volume that is mapped with OpenStack's volume
        cb_volume_id = src_vol_metadata['cb_volume_id']

        if cb_volume_id is not None and cb_volume_id != 'None':

            snapshot_name = snapshot['display_name']
            if snapshot_name is None or snapshot_name == '':
                # generate the snapshot name
                snapshot_name = self._generate_snapshot_name()

            snapshot_name = self._sanitize_name(snapshot_name)

            # update the snapshot dict for later use
            snapshot['display_name'] = snapshot_name

            params = {
                "name": snapshot_name,
                "id": cb_volume_id
            }

            self._update_http_conn_params(params, src_vol_metadata)

            LOG.debug("Will create CloudByte snapshot [%(cb_snap)s] "
                      " w.r.t CloudByte volume [%(cb_vol)s]"
                      " and OpenStack volume [%(stack_vol)s]",
                      {'cb_snap': snapshot_name,
                       'cb_vol': cb_volume_id,
                       'stack_vol': source_volume_id})

            self._api_request_for_cloudbyte('createStorageSnapshot', params)

            # get the snapshot path from CloudByte
            path = self._get_cb_snapshot_path(snapshot,
                                              cb_volume_id, src_vol_metadata)

            LOG.info("Successfully created CloudByte snapshot [%(cb_snap)s] "
                     " w.r.t CloudByte volume [%(cb_vol)s]"
                     " and OpenStack volume [%(stack_vol)s]",
                     {'cb_snap': path,
                      'cb_vol': cb_volume_id,
                      'stack_vol': source_volume_id})

            # Update this snapshot path in snapshot metadata
            # i.e. db update
            snapshot_metadata = {"cb_snapshot_path_" + snapshot['id']: path}
            self.db.volume_metadata_update(
                ctxt, source_volume_id, snapshot_metadata, False)

        else:

            raise exception.VolumeBackendAPIException(
                "Error: CloudByte volume metadata not found for "
                "OpenStack volume [%s]. Failed to create snapshot." %
                source_volume_id)

    def create_cloned_volume(self, cloned_volume, src_volume):
        """Create a clone of an existing volume at CloudByte storage.

        First it will create a snapshot of the source/parent volume,
        then it creates a clone of this newly created snapshot.
        """

        # extract necessary information from input params
        parent_volume_id = cloned_volume.get('source_volid')
        cloned_volume_id = cloned_volume.get('id')

        # get admin context
        ctxt = context.get_admin_context()

        # Create clone metadata before clone creation @ CloudByte
        # i.e. db create the volume metadata record
        cloned_volume_metadata = {"cb_volume_id": 'None'}

        self.db.volume_metadata_update(
            ctxt, cloned_volume_id, cloned_volume_metadata, False)

        # generating name and id for snapshot
        # as this is not user entered in this particular usecase
        snapshot_name = self._generate_snapshot_name()

        snapshot_id = (str(parent_volume_id) + "_" +
                       time.strftime("%d%m%Y") + time.strftime("%H%M%S"))

        # prepare the params for create_snapshot
        # as well as create_volume_from_snapshot method
        snapshot_params = {
            'id': snapshot_id,
            'display_name': snapshot_name,
            'volume_id': parent_volume_id,
        }

        # create a snapshot
        self.create_snapshot(snapshot_params)

        # create a clone of above snapshot
        return self.create_volume_from_snapshot(cloned_volume, snapshot_params)

    def create_volume_from_snapshot(self, cloned_volume, snapshot):
        """Create a clone from an existing snapshot at CloudByte storage."""

        # getting necessary data from input params
        parent_volume_id = snapshot['volume_id']
        cloned_volume_id = cloned_volume['id']
        cloned_volume_name = cloned_volume['display_name']

        # check if the volume to be cloned has got any name
        if cloned_volume_name is None or cloned_volume_name == '':
            cloned_volume_name = self._generate_clone_name()

        cloned_volume_name = self._sanitize_name(cloned_volume_name)

        # openstack snapshot id
        snapshot_id = snapshot['id']

        # get admin context
        ctxt = context.get_admin_context()

        # Create clone metadata before clone creation @ CloudByte.
        # store (i.e. db create) metadata related to clone
        cloned_vol_metadata = {"cb_volume_id": 'None'}
        self.db.volume_metadata_update(
            ctxt, cloned_volume_id, cloned_vol_metadata, False)

        # Fetch the CloudByte volume that is mapped with OpenStack's volume
        # i.e. the parent/source volume of this clone
        src_vol_metadata = (
            self.db.volume_metadata_get(ctxt, parent_volume_id)
        )

        # get CloudByte volume id
        cb_volume_id = src_vol_metadata['cb_volume_id']

        # get CloudByte snapshot path
        cb_snapshot_path = src_vol_metadata[
            "cb_snapshot_path_" + snapshot_id]

        params = {
            "id": cb_volume_id,
            "clonename": cloned_volume_name,
            "path": cb_snapshot_path
        }

        self._update_http_conn_params(params, src_vol_metadata)

        LOG.debug("Will create CloudByte clone [%(cb_clone)s] "
                  " at CloudByte snapshot path [%(cb_snap)s]"
                  " w.r.t parent OpenStack volume [%(stack_vol)s]",
                  {'cb_clone': cloned_volume_name,
                   'cb_snap': cb_snapshot_path,
                   'stack_vol': parent_volume_id})

        # create clone of the snapshot
        clone_dataset_snapshot_res = (
            self._api_request_for_cloudbyte('cloneDatasetSnapshot', params))

        cb_snap = clone_dataset_snapshot_res.get('cloneDatasetSnapshot')

        cb_vol = {}
        if cb_snap is not None:
            cb_vol = cb_snap.get('filesystem')
        else:
            raise exception.VolumeBackendAPIException(
                "Error: CloudByte clone creation failed for "
                "OpenStack volume [%(vol)s] with snapshot path [%(path)s]" %
                {'vol': parent_volume_id, 'path': cb_snapshot_path})

        # CloudByte volume id for this newly created clone
        cb_vol_id = cb_vol.get('id')

        LOG.info("Successfully created CloudByte clone [%(cb_clone)s] "
                 " at CloudByte snapshot path [%(cb_snap)s]"
                 " w.r.t parent OpenStack volume [%(stack_vol)s]",
                 {'cb_clone': cloned_volume_name,
                  'cb_snap': cb_snapshot_path,
                  'stack_vol': parent_volume_id})

        # Store connection info derived from the parent volume
        # along with the current volume's id.
        # The connection info is required for storage operations on the clone
        cloned_vol_metadata = {'cb_volume_id': cb_vol_id}
        self._update_http_conn_params(cloned_vol_metadata, src_vol_metadata)

        self.db.volume_metadata_update(
            ctxt, cloned_volume_id, cloned_vol_metadata, False)

        return self._build_provider_details_from_volume(cb_vol)

    def delete_snapshot(self, snapshot):
        """Delete a snapshot at CloudByte storage."""

        # getting admin context to get & update volume_admin_metadata
        ctxt = context.get_admin_context()

        # find source volume id
        source_volume_id = snapshot['volume_id']

        # get volume metadata
        vol_metadata = self.db.volume_metadata_get(
            ctxt, source_volume_id)

        # get the CloudByte volume that was mapped with openstack volume
        cb_volume_id = vol_metadata['cb_volume_id']

        # get the CloudByte snapshot path
        cb_snapshot_path = vol_metadata.get(
            'cb_snapshot_path_' + snapshot['id'])

        # if cb_snapshot_path is 'None'
        # then no need to execute CloudByte API
        if cb_snapshot_path is not None and cb_snapshot_path != 'None':

            params = {
                "id": cb_volume_id,
                "path": cb_snapshot_path
            }

            self._update_http_conn_params(params, vol_metadata)

            LOG.debug("Will delete CloudByte snapshot [%(snap)s] w.r.t "
                      "CloudByte volume [%(cb_vol)s] "
                      "and OpenStack volume [%(stack_vol)s]",
                      {'snap': cb_snapshot_path,
                       'cb_vol': cb_volume_id,
                       'stack_vol': source_volume_id})

            try:
                # Execute CloudByte API
                self._api_request_for_cloudbyte('deleteSnapshot', params)
                LOG.info("Successfully deleted CloudByte snapshot [%(snap)s] "
                         "w.r.t CloudByte volume [%(cb_vol)s] "
                         "and OpenStack volume [%(stack_vol)s]",
                         {'snap': cb_snapshot_path,
                          'cb_vol': cb_volume_id,
                          'stack_vol': source_volume_id})

            except Exception:
                # NOTE(AmitD): Let it pass
                # CloudByte complains if the snapshot has any clones.
                # Openstack treats snapshot & its clones as decoupled.
                LOG.info("Marked as deleted the CloudByte snapshot [%(snap)s] "
                         "w.r.t CloudByte volume [%(cb_vol)s] "
                         "and OpenStack volume [%(stack_vol)s]",
                         {'snap': cb_snapshot_path,
                          'cb_vol': cb_volume_id,
                          'stack_vol': source_volume_id})
                pass

        else:
            LOG.error("CloudByte snapshot metadata is not avaliable"
                      " for OpenStack volume [%s]", source_volume_id)

    def extend_volume(self, volume, new_size):
        """Extend the volume at CloudByte storage."""

        # get admin context
        ctxt = context.get_admin_context()

        # find volume id
        volume_id = volume['id']

        # get volume metadata
        vol_metadata = self.db.volume_metadata_get(ctxt, volume_id)

        # get CloudByte volume id from the metadata
        cb_volume_id = vol_metadata['cb_volume_id']

        params = {
            "id": cb_volume_id,
            "quotasize": str(new_size) + 'G'
        }

        self._update_http_conn_params(params, vol_metadata)

        # request the CloudByte api to update the volume
        self._api_request_for_cloudbyte("updateFileSystem", params)

    def update_volume_metadata(self, volume, metadata):
        """Update the volume metadata at CloudByte storage."""

        # get admin context
        ctxt = context.get_admin_context()

        # find source volume id
        volume_id = volume['id']

        # get volume metadata
        vol_metadata = self.db.volume_metadata_get(ctxt, volume_id)

        # get CloudByte volume id from the metadata
        cb_volume_id = vol_metadata['cb_volume_id']

        if cb_volume_id != 'None':

            params = {}

            self._update_http_conn_params(params, vol_metadata)

            # update filesystem
            fs_params = self._get_update_filesystem_params(vol_metadata)
            fs_params['id'] = cb_volume_id

            self._update_http_conn_params(fs_params, vol_metadata)

            # update the filesystem props
            self._api_request_for_cloudbyte('updateFileSystem', fs_params)

            # get the volume list
            cb_volumes = self._api_request_for_cloudbyte(
                'listFileSystem', params)

            # extract the qosgroup id from above list
            group_id = self._get_qosgroupid_id_from_response(
                cb_volumes, cb_volume_id)

            # prepare params for qos update API
            qos_params = self._get_update_qos_params(vol_metadata)
            qos_params['id'] = group_id

            self._update_http_conn_params(qos_params, vol_metadata)

            # update the qos props
            self._api_request_for_cloudbyte('updateQosGroup', qos_params)

    def create_export(self, context, volume):
        """Setup the iscsi export info."""

        model_update = {}
        model_update['provider_auth'] = ('CHAP %s %s' % (None, None))

        return model_update

    def ensure_export(self, context, volume):
        """Verify the iscsi export info."""

        model_update = {}
        model_update['provider_auth'] = ('CHAP %s %s' % (None, None))

        return model_update

    def get_volume_stats(self, refresh=False):
        """Get volume statistics.

        If 'refresh' is True, update/refresh the statistics.
        """

        if refresh:
            data = {}

            # Currently hard coding to infinite to void the
            # decisions taken by the cinder scheduler as it does not
            # take into account the multi-tenancy categorization of a
            # storage backend. In addition runtime provision of a storage
            # backend is not possible without restarting the cinder services.
            # Hence, avoiding the scheduler based decisions.
            data['total_capacity_gb'] = float("inf")
            data['free_capacity_gb'] = float("inf")

            data["volume_backend_name"] = (
                self.configuration.volume_backend_name)
            data["vendor_name"] = 'CloudByte'
            data['reserved_percentage'] = 0
            data["driver_version"] = CloudByteISCSIDriver.VERSION
            data["storage_protocol"] = 'iSCSI'

            LOG.debug("CloudByte storage statistics: [%s]", data)
            self.volume_stats = data

        return self.volume_stats

    def _update_initiator_group(self, volume_id, ig_name, vol_metadata):

        # Get account id of this account
        account_name = self.configuration.cb_account_name
        account_id = self._get_account_id_from_name(account_name, vol_metadata)

        # Fetch the initiator group ID
        params = {"accountid": account_id}

        iscsi_initiator_data = self._api_request_for_cloudbyte(
            'listiSCSIInitiator', params)

        # Filter the list of initiator groups with the name
        ig_id = self._get_initiator_group_id_from_response(
            iscsi_initiator_data, ig_name)

        params = {"storageid": volume_id}

        iscsi_service_data = self._api_request_for_cloudbyte(
            'listVolumeiSCSIService', params)
        iscsi_id = self._get_iscsi_service_id_from_response(
            volume_id, iscsi_service_data)

        # Update the iscsi service with above fetched iscsi_id
        self._request_update_iscsi_service(iscsi_id, ig_id, None)

        LOG.debug("CloudByte initiator group updated successfully for volume "
                  "[%(vol)s] with ig [%(ig)s].",
                  {'vol': volume_id,
                   'ig': ig_name})
