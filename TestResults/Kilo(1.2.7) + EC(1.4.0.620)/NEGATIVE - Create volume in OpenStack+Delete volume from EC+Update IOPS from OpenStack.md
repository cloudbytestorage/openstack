### LOGS:

######2015-12-14 14:31:19.662 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-ab1de8a0-12ad-4a46-99ca-af65a424709b - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 14:31:19.663 2970 ERROR cinder.volume.manager [req-ab1de8a0-12ad-4a46-99ca-af65a424709b - - - - -] Volume b61f3dbe-8704-422e-9961-7e5908e78e3c: driver error when trying to retype, falling back to generic mechanism.
######2015-12-14 14:31:19.663 2970 ERROR cinder.volume.manager [req-ab1de8a0-12ad-4a46-99ca-af65a424709b - - - - -] 'filesystem'
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager Traceback (most recent call last):
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1743, in retype
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager     host)
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager     return f(*args, **kwargs)
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1309, in retype
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager     cb_volume_list = response['filesystem']
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager KeyError: 'filesystem'
######2015-12-14 14:31:19.663 2970 TRACE cinder.volume.manager
######2015-12-14 14:31:19.724 2970 ERROR oslo_messaging.rpc.dispatcher [req-ab1de8a0-12ad-4a46-99ca-af65a424709b - - - - -] Exception during message handling: Volume migration failed: Retype requires migration but is not allowed.
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher Traceback (most recent call last):
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 142, in _dispatch_and_reply
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback))
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 186, in _dispatch
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback)
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 130, in _do_dispatch
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher     result = func(ctxt, **new_args)
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1767, in retype
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher     raise exception.VolumeMigrationFailed(reason=msg)
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher VolumeMigrationFailed: Volume migration failed: Retype requires migration but is not allowed.
######2015-12-14 14:31:19.724 2970 TRACE oslo_messaging.rpc.dispatcher
######2015-12-14 14:31:32.477 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 14:31:32.477 2970 ERROR cinder.volume.manager [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Volume b61f3dbe-8704-422e-9961-7e5908e78e3c: driver error when trying to retype, falling back to generic mechanism.
######2015-12-14 14:31:32.478 2970 ERROR cinder.volume.manager [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] 'filesystem'
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager Traceback (most recent call last):
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1743, in retype
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager     host)
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager     return f(*args, **kwargs)
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1309, in retype
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager     cb_volume_list = response['filesystem']
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager KeyError: 'filesystem'
######2015-12-14 14:31:32.478 2970 TRACE cinder.volume.manager
######2015-12-14 14:31:32.749 2970 INFO cinder.volume.flows.manager.create_volume [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 4dedaba7-7bba-4a35-a401-7b00647aa5c5: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-4dedaba7-7bba-4a35-a401-7b00647aa5c5'}
######2015-12-14 14:31:32.878 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-14 14:31:33.111 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 14:31:33.271 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-14 14:31:33.338 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-14 14:31:33.465 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:36.399 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:39.374 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:39.375 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [4dedaba77bba4a35a4017b00647aa5c5].
######2015-12-14 14:31:39.538 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 14:31:39.570 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-14 14:31:39.597 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-14 14:31:40.016 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-14 14:31:40.017 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] Successfully created a CloudByte volume [4dedaba77bba4a35a4017b00647aa5c5] w.r.t OpenStack volume [4dedaba7-7bba-4a35-a401-7b00647aa5c5].
######2015-12-14 14:31:40.095 2970 INFO cinder.volume.flows.manager.create_volume [req-f3865c69-f90c-4fdb-8e21-ce6d22981d50 - - - - -] Volume volume-4dedaba7-7bba-4a35-a401-7b00647aa5c5 (4dedaba7-7bba-4a35-a401-7b00647aa5c5): created successfully
######2015-12-14 14:31:45.353 2970 INFO cinder.volume.manager [req-12d3e0ce-e2fa-4133-bb51-9cb105c2d2bd - - - - -] Updating volume status
######2015-12-14 14:31:45.592 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-12d3e0ce-e2fa-4133-bb51-9cb105c2d2bd - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 14:31:47.108 2970 INFO oslo_messaging._drivers.impl_rabbit [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Connecting to AMQP server on 127.0.0.1:5672
######2015-12-14 14:31:47.122 2970 INFO oslo_messaging._drivers.impl_rabbit [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Connected to AMQP server on 127.0.0.1:5672
######2015-12-14 14:31:49.570 2971 INFO cinder.volume.manager [req-473b0a59-9f52-41db-ac92-5e8d982745c9 - - - - -] Updating volume status
######2015-12-14 14:31:49.802 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-473b0a59-9f52-41db-ac92-5e8d982745c9 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 14:31:50.190 2970 WARNING cinder.brick.initiator.connector [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Failed to login iSCSI target iqn.2015-08.OPENSTACKACC.VSM1:OPENSTACKACCb61f3dbe8704422e99617e5908e78e3c on portal 172.16.78.10:3260 (exit code 19).
######2015-12-14 14:31:50.191 2970 WARNING cinder.brick.initiator.connector [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Failed to login to any of the iSCSI targets.
######2015-12-14 14:31:50.192 2970 WARNING cinder.brick.initiator.connector [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] ISCSI volume not yet found at: [u'/dev/disk/by-path/ip-172.16.78.10:3260-iscsi-iqn.######2015-08.OPENSTACKACC.VSM1:OPENSTACKACCb61f3dbe8704422e99617e5908e78e3c-lun-0']. Will rescan & retry.  Try number: 0
######2015-12-14 14:31:50.262 2970 ERROR cinder.volume.driver [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Failed to attach volume b61f3dbe-8704-422e-9961-7e5908e78e3c
######2015-12-14 14:31:51.402 2970 ERROR cinder.volume.manager [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Failed to copy volume b61f3dbe-8704-422e-9961-7e5908e78e3c to 4dedaba7-7bba-4a35-a401-7b00647aa5c5
######2015-12-14 14:31:51.504 2970 INFO cinder.volume.manager [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 4dedaba7-7bba-4a35-a401-7b00647aa5c5: deleting
######2015-12-14 14:31:51.599 2970 ERROR oslo_messaging.rpc.dispatcher [req-7e8e063a-633a-4aa3-8b7e-d71b52c8855a - - - - -] Exception during message handling: Unexpected error while running command.
Command: None
Exit code: -
Stdout: u"Unexpected error while running command.\nCommand: sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-08.OPENSTACKACC.VSM1:OPENSTACKACCb61f3dbe8704422e99617e5908e78e3c -p 172.16.78.10:3260 --rescan\nExit code: 21\nStdout: u''\nStderr: u'iscsiadm: No session found.\\n'"
Stderr: None
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Traceback (most recent call last):
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 142, in _dispatch_and_reply
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback))
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 186, in _dispatch
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 130, in _do_dispatch
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     result = func(ctxt, **new_args)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1796, in retype
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     new_reservations, status_update)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_utils/excutils.py", line 85, in __exit__
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     six.reraise(self.type_, self.value, self.tb)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1792, in retype
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     new_type_id=new_type_id)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1488, in migrate_volume
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     self.db.volume_update(ctxt, volume_ref['id'], updates)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_utils/excutils.py", line 85, in __exit__
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     six.reraise(self.type_, self.value, self.tb)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1473, in migrate_volume
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     new_type_id)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1295, in _migrate_volume_generic
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     new_volume['id'])
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_utils/excutils.py", line 85, in __exit__
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     six.reraise(self.type_, self.value, self.tb)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1275, in _migrate_volume_generic
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     remote='dest')
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/driver.py", line 521, in copy_volume_data
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     properties, force=True, remote=dest_remote)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_utils/excutils.py", line 85, in __exit__
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     six.reraise(self.type_, self.value, self.tb)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/driver.py", line 513, in copy_volume_data
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     remote=src_remote)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/driver.py", line 695, in _attach_volume
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     return (self._connect_device(conn), volume)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/driver.py", line 707, in _connect_device
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     device = connector.connect_volume(conn['data'])
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_concurrency/lockutils.py", line 445, in inner
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/brick/initiator/connector.py", line 333, in connect_volume
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     self._run_iscsiadm(target_props, ("--rescan",))
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/brick/initiator/connector.py", line 456, in _run_iscsiadm
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     check_exit_code=check_exit_code)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_concurrency/processutils.py", line 266, in execute
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     cmd=sanitized_cmd)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher ProcessExecutionError: Unexpected error while running command.
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Command: sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-08.OPENSTACKACC.VSM1:OPENSTACKACCb61f3dbe8704422e99617e5908e78e3c -p 172.16.78.10:3260 --rescan
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Exit code: 21
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Stdout: u''
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Stderr: u'iscsiadm: No session found.\n'
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher
######2015-12-14 14:31:51.732 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 14:31:51.880 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-14 14:31:51.906 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-14 14:31:51.934 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-14 14:31:52.383 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-14 14:31:52.435 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-14 14:31:52.519 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:55.462 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:55.463 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [837607ba-197f-3b0c-b8bf-c49d51646b0c].
######2015-12-14 14:31:55.464 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [837607ba-197f-3b0c-b8bf-c49d51646b0c] at CloudByte corresponding to OpenStack volume [4dedaba7-7bba-4a35-a401-7b00647aa5c5].
######2015-12-14 14:31:55.477 2970 INFO cinder.volume.manager [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 4dedaba7-7bba-4a35-a401-7b00647aa5c5: deleted successfully
######2015-12-14 14:32:08.477 2972 INFO cinder.volume.manager [req-a2d95b62-10ea-4564-ab9a-7b860fcc4516 - - - - -] Updating volume status
######2015-12-14 14:32:08.687 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-a2d95b62-10ea-4564-ab9a-7b860fcc4516 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_concurrency/lockutils.py", line 445, in inner
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/brick/initiator/connector.py", line 333, in connect_volume
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     self._run_iscsiadm(target_props, ("--rescan",))
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/brick/initiator/connector.py", line 456, in _run_iscsiadm
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     check_exit_code=check_exit_code)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_concurrency/processutils.py", line 266, in execute
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher     cmd=sanitized_cmd)
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher ProcessExecutionError: Unexpected error while running command.
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Command: sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-08.OPENSTACKACC.VSM1:OPENSTACKACCb61f3dbe8704422e99617e5908e78e3c -p 172.16.78.10:3260 --rescan
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Exit code: 21
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Stdout: u''
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher Stderr: u'iscsiadm: No session found.\n'
######2015-12-14 14:31:51.599 2970 TRACE oslo_messaging.rpc.dispatcher
######2015-12-14 14:31:51.732 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 14:31:51.880 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-14 14:31:51.906 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-14 14:31:51.934 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-14 14:31:52.383 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-14 14:31:52.435 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-14 14:31:52.519 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:55.462 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 14:31:55.463 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [837607ba-197f-3b0c-b8bf-c49d51646b0c].
######2015-12-14 14:31:55.464 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [837607ba-197f-3b0c-b8bf-c49d51646b0c] at CloudByte corresponding to OpenStack volume [4dedaba7-7bba-4a35-a401-7b00647aa5c5].
######2015-12-14 14:31:55.477 2970 INFO cinder.volume.manager [req-49c52727-14b8-4be6-93fd-9977fc9ea709 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 4dedaba7-7bba-4a35-a401-7b00647aa5c5: deleted successfully
