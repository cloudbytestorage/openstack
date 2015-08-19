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

from oslo.config import cfg

cloudbyte_connection_opts = [
    cfg.IntOpt('cb_version',
               default=140528,
               help=('Elasticenter version information.')),
    cfg.StrOpt('cb_apikey',
               default=None,
               help=('Elasticenter authorization purpose.')),
    cfg.StrOpt('cb_account_name',
               default=None,
               help=('Is mapped against a VSM.')),
    cfg.StrOpt('tsm_name',
               default=None,
               help=('Used to create volume.')),
    cfg.StrOpt('cb_account_id',
               default=None,
               help=('Account ID of super admin or account admin')),
    cfg.StrOpt('cb_dataset_id',
               default=None,
               help=('The VSM dataset_id.')),
    cfg.StrOpt('cb_tsm_id',
               default=None,
               help=('Refers to VSM ID.')),
    cfg.IntOpt('confirm_vol_sleep_interval',
               default=2,
               help=('Sleep value is in seconds.')),
    cfg.IntOpt('confirm_vol_sleep_counter',
               default=3,
               help=('Will confirm a successful volume '
                     'creation by making this many attempts.')), ]

cloudbyte_add_qosgroup_opts = [
    cfg.DictOpt('add_qosgroup',
                default={
                    'iops': '10',
                    'latency': '15',
                    'graceallowed': 'false',
                    'networkspeed': '0',
                    'memlimit': '0',
                    'tpcontrol': 'false',
                    'throughput': '0',
                    'iopscontrol': 'true'
                },
                help=('These values will be used by addQos api.')), ]

cloudbyte_create_volume_opts = [
    cfg.DictOpt('create_volume',
                default={
                    'blocklength': '512B',
                    'compression': 'off',
                    'deduplication': 'off',
                    'sync': 'always',
                    'recordsize': '128k',
                    'protocoltype': 'ISCSI'
                },
                help=('These values will be used by createVolume api.')), ]

cloudbyte_initiator_group_opts = [
    cfg.StrOpt('cb_initiator_group_name',
               default='None',
               help=('Initiator group name is assigned to a volume.'
                     'Based on this name CloudByte storage verifies whether '
                     'iscsi connection made to this volume was initiatied '
                     'from the expected host.')), ]

CONF = cfg.CONF
CONF.register_opts(cloudbyte_add_qosgroup_opts)
CONF.register_opts(cloudbyte_create_volume_opts)
CONF.register_opts(cloudbyte_connection_opts)
CONF.register_opts(cloudbyte_initiator_group_opts)
