### RESULT:

PASS

### LOGS:

#####FROM BACKEND 1
######2015-12-10 13:04:49.273 13317 INFO cinder.volume.manager [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 4af53f83-c1ef-42f2-9ab6-149fd5970651: deleting
######2015-12-10 13:04:49.402 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 13:04:49.544 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 13:04:49.568 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 13:04:49.597 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 13:04:49.970 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 13:04:50.023 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-10 13:04:50.098 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:04:55.052 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:04:55.053 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [fdeb495a-c149-3ffc-9997-074ac5006092].
######2015-12-10 13:04:55.054 13317 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-6f33e16a-1078-4256-adbc-186f470ba166 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [fdeb495a-c149-3ffc-9997-074ac5006092] at CloudByte corresponding to OpenStack volume [4af53f83-c1ef-42f2-9ab6-149fd5970651].
######2015-12-10 13:04:55.100 13317 INFO cinder.volume.manager [req-49ccf770-1256-4228-b1da-c76353020e69 - - - - -] volume 4af53f83-c1ef-42f2-9ab6-149fd5970651: deleted successfully


#####FROM BACKEND 2
######2015-12-10 13:05:52.967 13320 INFO cinder.volume.manager [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 96317df0-ddab-4f5c-9755-e706b4f9ffd7: deleting
######2015-12-10 13:05:53.063 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 13:05:53.185 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 13:05:53.210 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 13:05:53.238 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 13:05:53.642 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 13:05:53.694 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-10 13:05:53.778 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:05:58.722 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:05:58.723 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [e5afea07-ec00-3495-8c40-b03844b938f2].
######2015-12-10 13:05:58.723 13320 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-1043ecf7-1f8a-4d3e-a16f-73ef7a45a91f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [e5afea07-ec00-3495-8c40-b03844b938f2] at CloudByte corresponding to OpenStack volume [96317df0-ddab-4f5c-9755-e706b4f9ffd7].
######2015-12-10 13:05:58.767 13320 INFO cinder.volume.manager [req-cbfabc2b-a777-4123-9134-a7ed728ae432 - - - - -] volume 96317df0-ddab-4f5c-9755-e706b4f9ffd7: deleted successfully


#####FROM BACKEND 3
######2015-12-10 13:06:49.842 13322 INFO cinder.volume.manager [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 9d019010-1078-4df5-a611-b2d7b67a1a79: deleting
######2015-12-10 13:06:49.902 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listFileSystem].
######2015-12-10 13:06:50.000 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listAccount].
######2015-12-10 13:06:50.025 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listiSCSIInitiator].
######2015-12-10 13:06:50.054 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [listVolumeiSCSIService].
######2015-12-10 13:06:50.424 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateVolumeiSCSIService].
######2015-12-10 13:06:50.479 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [deleteFileSystem].
######2015-12-10 13:06:50.555 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:06:55.507 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte API executed successfully for command [queryAsyncJobResult].
######2015-12-10 13:06:55.509 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [-] CloudByte operation [Delete Volume] succeeded for volume [d11f41dc-d815-37d6-80f2-707a33e546ba].
######2015-12-10 13:06:55.510 13322 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-77783bd4-8ade-4032-bda6-34d01f9b0351 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Successfully deleted volume [d11f41dc-d815-37d6-80f2-707a33e546ba] at CloudByte corresponding to OpenStack volume [9d019010-1078-4df5-a611-b2d7b67a1a79].
######2015-12-10 13:06:55.556 13322 INFO cinder.volume.manager [req-77ab8996-6a24-47d5-af2f-e8e085232915 - - - - -] volume 9d019010-1078-4df5-a611-b2d7b67a1a79: deleted successfully

