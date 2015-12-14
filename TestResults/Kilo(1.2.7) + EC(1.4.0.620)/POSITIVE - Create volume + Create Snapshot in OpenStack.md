### RESULT:

PASS

### LOGS:

#####FROM BACKEND 1
######2015-12-10 13:14:23.070 13317 INFO cinder.volume.flows.manager.create_volume [req-59092345-2502-416c-8fbe-f53e97033c29 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 9792a8fe-91a2-42d3-9595-66e8ed08a361: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-9792a8fe-91a2-42d3-9595-66e8ed08a361'}
######2015-12-10 13:14:23.144 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-59092345-2502-416c-8fbe-f53e97033c29 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 13:14:23.327 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 13:14:23.501 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-10 13:14:23.567 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-10 13:14:23.698 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:14:28.045 13320 INFO cinder.volume.manager [req-17cb4dfe-e9e9-4ca6-9286-98e662a3e768 - - - - -] Updating volume status
######2015-12-10 13:14:28.259 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-17cb4dfe-e9e9-4ca6-9286-98e662a3e768 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 13:14:28.632 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:14:33.602 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:14:33.603 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [9792a8fe91a242d3959566e8ed08a361].
######2015-12-10 13:14:33.666 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 13:14:33.695 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 13:14:33.720 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 13:14:34.083 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 13:14:34.084 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] Successfully created a CloudByte volume [9792a8fe91a242d3959566e8ed08a361] w.r.t OpenStack volume [9792a8fe-91a2-42d3-9595-66e8ed08a361].
######2015-12-10 13:14:34.165 13317 INFO cinder.volume.flows.manager.create_volume [req-d2c83c5f-d683-4a0c-bd09-06eab19e46df - - - - -] Volume volume-9792a8fe-91a2-42d3-9595-66e8ed08a361 (9792a8fe-91a2-42d3-9595-66e8ed08a361): created successfully
######2015-12-10 13:14:40.830 13317 INFO cinder.volume.manager [req-6552ffb1-8bdf-49c6-b1ca-b31292a15220 - - - - -] Updating volume status
######2015-12-10 13:14:41.017 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6552ffb1-8bdf-49c6-b1ca-b31292a15220 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 13:14:45.793 13317 INFO cinder.volume.manager [req-38dcb1bc-3eeb-429f-b853-a5bbfca58b2b 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot 99c80f2b-a286-4e50-8989-1040e9b4e471: creating
######2015-12-10 13:14:46.032 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-38dcb1bc-3eeb-429f-b853-a5bbfca58b2b 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [createStorageSnapshot].
######2015-12-10 13:14:46.125 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-38dcb1bc-3eeb-429f-b853-a5bbfca58b2b 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listStorageSnapshots].
######2015-12-10 13:14:46.127 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-38dcb1bc-3eeb-429f-b853-a5bbfca58b2b 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Created CloudByte snapshot [Pool1/OPENSTACK_ACCVSM1/9792a8fe91a242d3959566e8ed08a361@snap_99c80f2ba2864e5089891040e9b4e471] w.r.t CloudByte volume [a6f07bdd-8993-3651-82d7-6b97a34a6a58] and OpenStack volume [9792a8fe-91a2-42d3-9595-66e8ed08a361].
######2015-12-10 13:14:46.206 13317 INFO cinder.volume.manager [req-38dcb1bc-3eeb-429f-b853-a5bbfca58b2b 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot 99c80f2b-a286-4e50-8989-1040e9b4e471: created successfully


#####FROM BACKEND 2
######2015-12-10 13:25:55.512 13320 INFO cinder.volume.flows.manager.create_volume [req-af2f63cb-111c-423e-80d8-64bd5ec3b4b7 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume ad4db3df-133f-47e5-bbb1-2750f351b5c3: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-ad4db3df-133f-47e5-bbb1-2750f351b5c3'}
######2015-12-10 13:25:55.586 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-af2f63cb-111c-423e-80d8-64bd5ec3b4b7 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 13:25:55.770 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 13:25:55.907 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-10 13:25:55.973 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-10 13:25:56.085 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:25:58.921 13322 INFO cinder.volume.manager [req-20ae0d78-6a8c-4fc8-8b55-0a55540ced7e - - - - -] Updating volume status
######2015-12-10 13:25:59.127 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-20ae0d78-6a8c-4fc8-8b55-0a55540ced7e - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 13:26:01.075 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:26:06.010 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:26:06.011 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [ad4db3df133f47e5bbb12750f351b5c3].
######2015-12-10 13:26:06.074 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 13:26:06.106 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 13:26:06.138 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 13:26:06.534 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 13:26:06.535 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] Successfully created a CloudByte volume [ad4db3df133f47e5bbb12750f351b5c3] w.r.t OpenStack volume [ad4db3df-133f-47e5-bbb1-2750f351b5c3].
######2015-12-10 13:26:06.612 13320 INFO cinder.volume.flows.manager.create_volume [req-5215ce08-a8c6-49e6-b8c7-74e175c46e2f - - - - -] Volume volume-ad4db3df-133f-47e5-bbb1-2750f351b5c3 (ad4db3df-133f-47e5-bbb1-2750f351b5c3): created successfully
######2015-12-10 13:26:13.541 13320 INFO cinder.volume.manager [req-c3531f7a-0fc1-4e2a-b1d0-5ffbd4096eb8 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot 05883aa0-075b-4934-9573-76e93d1da10b: creating
######2015-12-10 13:26:13.759 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-c3531f7a-0fc1-4e2a-b1d0-5ffbd4096eb8 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [createStorageSnapshot].
######2015-12-10 13:26:13.847 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-c3531f7a-0fc1-4e2a-b1d0-5ffbd4096eb8 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listStorageSnapshots].
######2015-12-10 13:26:13.848 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-c3531f7a-0fc1-4e2a-b1d0-5ffbd4096eb8 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Created CloudByte snapshot [Pool1/OPENSTACK_ACCVSM2/ad4db3df133f47e5bbb12750f351b5c3@snap_05883aa0075b4934957376e93d1da10b] w.r.t CloudByte volume [303d23f3-b14c-388e-885f-51f0626ccb68] and OpenStack volume [ad4db3df-133f-47e5-bbb1-2750f351b5c3].
######2015-12-10 13:26:13.930 13320 INFO cinder.volume.manager [req-c3531f7a-0fc1-4e2a-b1d0-5ffbd4096eb8 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot 05883aa0-075b-4934-9573-76e93d1da10b: created successfully


#####FROM BACKEND 3
######2015-12-10 14:11:17.933 13322 INFO cinder.volume.flows.manager.create_volume [req-ae611a5e-2943-46bb-83f9-8e60875d2254 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume fc04a30e-fce6-44e8-a5fe-9395dfcf0293: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-fc04a30e-fce6-44e8-a5fe-9395dfcf0293'}
######2015-12-10 14:11:18.007 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-ae611a5e-2943-46bb-83f9-8e60875d2254 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 14:11:18.191 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 14:11:18.325 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-10 14:11:18.395 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-10 14:11:18.508 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 14:11:23.492 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 14:11:23.493 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [fc04a30efce644e8a5fe9395dfcf0293].
######2015-12-10 14:11:23.556 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 14:11:23.585 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 14:11:23.611 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 14:11:23.996 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 14:11:23.998 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] Successfully created a CloudByte volume [fc04a30efce644e8a5fe9395dfcf0293] w.r.t OpenStack volume [fc04a30e-fce6-44e8-a5fe-9395dfcf0293].
######2015-12-10 14:11:24.077 13322 INFO cinder.volume.flows.manager.create_volume [req-e03ec0a8-9a84-49b6-84e9-58796e174689 - - - - -] Volume volume-fc04a30e-fce6-44e8-a5fe-9395dfcf0293 (fc04a30e-fce6-44e8-a5fe-9395dfcf0293): created successfully
######2015-12-10 14:11:27.968 13320 INFO cinder.volume.manager [req-d815ab66-e385-4c94-aea0-c1e438124d84 - - - - -] Updating volume status
######2015-12-10 14:11:28.168 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-d815ab66-e385-4c94-aea0-c1e438124d84 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 14:11:32.394 13322 INFO cinder.volume.manager [req-5749b337-c506-45ce-99bf-bf2ebc3b4f08 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot d9f42e53-1547-4e94-a248-32c97735e127: creating
######2015-12-10 14:11:32.820 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5749b337-c506-45ce-99bf-bf2ebc3b4f08 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [createStorageSnapshot].
######2015-12-10 14:11:32.910 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5749b337-c506-45ce-99bf-bf2ebc3b4f08 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listStorageSnapshots].
######2015-12-10 14:11:32.911 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5749b337-c506-45ce-99bf-bf2ebc3b4f08 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Created CloudByte snapshot [Pool1/OPENSTACK_ACCVSM3/fc04a30efce644e8a5fe9395dfcf0293@snap_d9f42e5315474e94a24832c97735e127] w.r.t CloudByte volume [b6d34254-02cc-35f8-823e-6b92b08d3135] and OpenStack volume [fc04a30e-fce6-44e8-a5fe-9395dfcf0293].
######2015-12-10 14:11:32.990 13322 INFO cinder.volume.manager [req-5749b337-c506-45ce-99bf-bf2ebc3b4f08 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot d9f42e53-1547-4e94-a248-32c97735e127: created successfully

