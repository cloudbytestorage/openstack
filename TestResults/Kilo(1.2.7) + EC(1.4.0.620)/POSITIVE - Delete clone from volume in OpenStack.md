### RESULT:

PASS

### LOGS:

#####FROM BACKEND 1
######2015-12-10 15:07:54.301 13317 INFO cinder.volume.manager [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 705db87a-62ad-4730-a1dd-259698c0b6a2: deleting
######2015-12-10 15:07:54.399 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 15:07:54.513 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 15:07:54.538 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 15:07:54.567 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 15:07:54.958 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 15:07:55.002 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-10 15:07:55.091 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 15:07:58.946 13322 INFO cinder.volume.manager [req-abe1c0e6-9dbd-446f-881d-5d9d3d0169ab - - - - -] Updating volume status
######2015-12-10 15:07:59.142 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-abe1c0e6-9dbd-446f-881d-5d9d3d0169ab - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 15:08:00.032 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 15:08:00.033 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [3f05f6a7-cddb-3be3-9071-ae12a7469eae].
######2015-12-10 15:08:00.034 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-45adbe6e-9e3c-4b95-a294-2d0542aa3c5e 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [3f05f6a7-cddb-3be3-9071-ae12a7469eae] #####FROM CloudByte corresponding to OpenStack volume [705db87a-62ad-4730-a1dd-259698c0b6a2].
######2015-12-10 15:08:00.127 13317 INFO cinder.volume.manager [req-32af6b41-f8da-416a-879b-2f220faa51ba - - - - -] volume 705db87a-62ad-4730-a1dd-259698c0b6a2: deleted successfully

#####FROM BACKEND 2
######2015-12-10 15:10:40.856 13317 INFO cinder.volume.manager [req-120e3c2e-1cf1-48ea-9805-eeb4a01b70bd - - - - -] Updating volume status
######2015-12-10 15:10:41.062 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-120e3c2e-1cf1-48ea-9805-eeb4a01b70bd - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 15:10:43.848 13320 INFO cinder.volume.manager [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 58f10097-ddce-49cd-8bea-f2b3614b51f4: deleting
######2015-12-10 15:10:43.946 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 15:10:44.060 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 15:10:44.084 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 15:10:44.114 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 15:10:44.482 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 15:10:44.773 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-10 15:10:44.883 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 15:10:49.803 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 15:10:49.804 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [15cf6b05-deb3-3654-921f-02f4e39a2f86].
######2015-12-10 15:10:49.804 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-09e35b45-590e-49a2-9d17-44dbbeed9c2a 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [15cf6b05-deb3-3654-921f-02f4e39a2f86] #####FROM CloudByte corresponding to OpenStack volume [58f10097-ddce-49cd-8bea-f2b3614b51f4].
######2015-12-10 15:10:50.041 13320 INFO cinder.volume.manager [req-91094669-b812-48c1-8299-18bfe63f0ffc - - - - -] volume 58f10097-ddce-49cd-8bea-f2b3614b51f4: deleted successfully


#####FROM BACKEND 3
######2015-12-10 15:12:39.399 13322 INFO cinder.volume.manager [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume abfc1561-fbb3-4123-96dc-e9d665cd973a: deleting
######2015-12-10 15:12:39.499 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 15:12:39.611 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 15:12:39.635 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 15:12:39.663 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 15:12:40.032 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 15:12:40.092 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-10 15:12:40.179 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 15:12:40.857 13317 INFO cinder.volume.manager [req-29018060-d247-4030-b64b-0ae57e47e178 - - - - -] Updating volume status
######2015-12-10 15:12:41.059 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-29018060-d247-4030-b64b-0ae57e47e178 - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-10 15:12:45.121 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 15:12:45.121 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [10165ea5-9eca-32d8-8571-b60f78fffe49].
######2015-12-10 15:12:45.122 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-55bd4d22-5d2f-4a90-8c9a-134bb25e95e2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [10165ea5-9eca-32d8-8571-b60f78fffe49] #####FROM CloudByte corresponding to OpenStack volume [abfc1561-fbb3-4123-96dc-e9d665cd973a].
######2015-12-10 15:12:45.165 13322 INFO cinder.volume.manager [req-8464b13b-7002-4492-92b3-d1a2d8839025 - - - - -] volume abfc1561-fbb3-4123-96dc-e9d665cd973a: deleted successfully
