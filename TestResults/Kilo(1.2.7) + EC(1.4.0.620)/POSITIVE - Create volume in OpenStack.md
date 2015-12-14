### RESULT:

PASS

### LOGS:

#####FROM BACKEND 1
######2015-12-14 10:49:33.274 2970 INFO cinder.volume.flows.manager.create_volume [req-9bd4d869-ba9e-4973-bae3-05403c82f696 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume b61f3dbe-8704-422e-9961-7e5908e78e3c: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-b61f3dbe-8704-422e-9961-7e5908e78e3c'}
######2015-12-14 10:49:33.354 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-9bd4d869-ba9e-4973-bae3-05403c82f696 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-14 10:49:33.548 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 10:49:33.961 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-14 10:49:34.109 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-14 10:49:34.185 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:49:37.195 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:49:40.147 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:49:40.148 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [b61f3dbe8704422e99617e5908e78e3c].
######2015-12-14 10:49:40.213 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 10:49:40.243 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-14 10:49:40.269 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-14 10:49:40.747 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-14 10:49:40.748 2970 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] Successfully created a CloudByte volume [b61f3dbe8704422e99617e5908e78e3c] w.r.t OpenStack volume [b61f3dbe-8704-422e-9961-7e5908e78e3c].
######2015-12-14 10:49:40.829 2970 INFO cinder.volume.flows.manager.create_volume [req-941ae384-4a57-49bd-ae61-4170e28c7412 - - - - -] Volume volume-b61f3dbe-8704-422e-9961-7e5908e78e3c (b61f3dbe-8704-422e-9961-7e5908e78e3c): created successfully


#####FROM BACKEND 2
######2015-12-14 10:50:10.645 2971 INFO cinder.volume.flows.manager.create_volume [req-f582cc7d-fb84-4d3b-87ef-c5026001441a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 33d25caa-3359-4a54-954a-f439e67c5ad8: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-33d25caa-3359-4a54-954a-f439e67c5ad8'}
######2015-12-14 10:50:10.748 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-f582cc7d-fb84-4d3b-87ef-c5026001441a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-14 10:50:10.960 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 10:50:11.098 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-14 10:50:11.150 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-14 10:50:11.246 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:50:16.247 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:50:21.185 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:50:21.185 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [33d25caa33594a54954af439e67c5ad8].
######2015-12-14 10:50:21.287 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 10:50:21.315 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-14 10:50:21.342 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-14 10:50:21.791 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-14 10:50:21.792 2971 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] Successfully created a CloudByte volume [33d25caa33594a54954af439e67c5ad8] w.r.t OpenStack volume [33d25caa-3359-4a54-954a-f439e67c5ad8].
######2015-12-14 10:50:21.872 2971 INFO cinder.volume.flows.manager.create_volume [req-5207823e-93fb-4586-980b-97d39f5c6f38 - - - - -] Volume volume-33d25caa-3359-4a54-954a-f439e67c5ad8 (33d25caa-3359-4a54-954a-f439e67c5ad8): created successfully


#####FROM BACKEND 3
######2015-12-14 10:52:22.939 2972 INFO cinder.volume.flows.manager.create_volume [req-40cbd4b7-b86f-48df-bbb5-a6dc58470e44 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Volume 27566eb6-7619-459b-b548-54aebb37747f: being created as raw with specification: {'status': u'creating', 'volume_size': 1, 'volume_name': u'volume-27566eb6-7619-459b-b548-54aebb37747f'}
######2015-12-14 10:52:23.066 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-40cbd4b7-b86f-48df-bbb5-a6dc58470e44 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-14 10:52:23.299 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 10:52:23.456 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [addQosGroup].
######2015-12-14 10:52:23.526 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [createVolume].
######2015-12-14 10:52:23.739 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:52:28.600 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:52:33.562 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-14 10:52:33.564 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Create Volume] succeeded for volume [27566eb67619459bb54854aebb37747f].
######2015-12-14 10:52:33.716 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-14 10:52:33.758 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-14 10:52:33.787 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-14 10:52:34.188 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-14 10:52:34.189 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] Successfully created a CloudByte volume [27566eb67619459bb54854aebb37747f] w.r.t OpenStack volume [27566eb6-7619-459b-b548-54aebb37747f].
######2015-12-14 10:52:34.307 2972 INFO cinder.volume.flows.manager.create_volume [req-da3193ac-0ae6-4444-89b6-6f9d50763f50 - - - - -] Volume volume-27566eb6-7619-459b-b548-54aebb37747f (27566eb6-7619-459b-b548-54aebb37747f): created successfully
