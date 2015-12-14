### RESULT:

PASS

### LOGS:

#####FROM BACKEND 1
######2015-12-10 16:13:11.262 2543 INFO cinder.volume.flows.manager.create_volume [req-236641a6-93e7-49ee-ae54-47f9dc4b4777 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 74c129af-c114-430b-aefa-ae5d2b7274df: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-74c129af-c114-430b-aefa-ae5d2b7274df'}
######2015-12-10 16:13:11.338 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-236641a6-93e7-49ee-ae54-47f9dc4b4777 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 16:13:11.522 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 16:13:11.739 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-10 16:13:11.802 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-10 16:13:11.925 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:13:16.885 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:13:20.030 2543 INFO cinder.volume.manager [req-6c1f1688-fee6-42c0-b60c-2b3c2efe17a3 - - - - -] Updating volume status
######2015-12-10 16:13:20.229 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6c1f1688-fee6-42c0-b60c-2b3c2efe17a3 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 16:13:21.837 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:13:21.838 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [74c129afc114430baefaae5d2b7274df].
######2015-12-10 16:13:21.900 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 16:13:21.929 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 16:13:21.956 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 16:13:22.343 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 16:13:22.344 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] Successfully created a CloudByte volume [74c129afc114430baefaae5d2b7274df] w.r.t OpenStack volume [74c129af-c114-430b-aefa-ae5d2b7274df].
######2015-12-10 16:13:22.423 2543 INFO cinder.volume.flows.manager.create_volume [req-9726d451-0e30-4315-9951-a0e6df2997a0 - - - - -] Volume volume-74c129af-c114-430b-aefa-ae5d2b7274df (74c129af-c114-430b-aefa-ae5d2b7274df): created successfully

#####FROM BACKEND 2
######2015-12-10 16:15:12.907 2544 INFO cinder.volume.flows.manager.create_volume [req-e97a232f-a0f9-40d0-9b95-63d0c0a2128e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 687c9648-314d-4ff9-94c0-b7de7b2a2d54: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-687c9648-314d-4ff9-94c0-b7de7b2a2d54'}
######2015-12-10 16:15:13.003 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-e97a232f-a0f9-40d0-9b95-63d0c0a2128e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 16:15:13.202 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 16:15:13.364 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-10 16:15:13.426 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-10 16:15:13.592 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:15:18.519 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:15:23.464 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:15:23.465 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [687c9648314d4ff994c0b7de7b2a2d54].
######2015-12-10 16:15:23.571 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 16:15:23.600 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 16:15:23.626 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 16:15:24.043 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 16:15:24.044 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] Successfully created a CloudByte volume [687c9648314d4ff994c0b7de7b2a2d54] w.r.t OpenStack volume [687c9648-314d-4ff9-94c0-b7de7b2a2d54].
######2015-12-10 16:15:24.166 2544 INFO cinder.volume.flows.manager.create_volume [req-69241873-ea27-4e31-a1e4-c4b44137197d - - - - -] Volume volume-687c9648-314d-4ff9-94c0-b7de7b2a2d54 (687c9648-314d-4ff9-94c0-b7de7b2a2d54): created successfully

#####FROM BACKEND 3
######2015-12-10 16:15:47.280 2545 INFO cinder.volume.flows.manager.create_volume [req-bbcecd2b-d125-4813-89da-251176f36b61 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 27790bf5-fcdb-4193-8277-62117ee7b13a: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-27790bf5-fcdb-4193-8277-62117ee7b13a'}
######2015-12-10 16:15:47.399 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-bbcecd2b-d125-4813-89da-251176f36b61 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 16:15:47.623 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 16:15:47.994 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-10 16:15:48.054 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-10 16:15:48.149 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:15:53.093 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 16:15:53.094 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [27790bf5fcdb4193827762117ee7b13a].
######2015-12-10 16:15:53.240 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 16:15:53.269 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 16:15:53.294 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 16:15:53.702 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 16:15:53.703 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] Successfully created a CloudByte volume [27790bf5fcdb4193827762117ee7b13a] w.r.t OpenStack volume [27790bf5-fcdb-4193-8277-62117ee7b13a].
######2015-12-10 16:15:53.969 2545 INFO cinder.volume.flows.manager.create_volume [req-4c458398-d7fa-406a-aa9c-e78e06796bb1 - - - - -] Volume volume-27790bf5-fcdb-4193-8277-62117ee7b13a (27790bf5-fcdb-4193-8277-62117ee7b13a): created successfully
