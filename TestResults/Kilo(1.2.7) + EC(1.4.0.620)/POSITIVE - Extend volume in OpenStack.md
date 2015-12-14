### RESULT:

PASS

### LOGS:

#####FROM BACKEND 1
######2015-12-10 16:17:26.325 2543 INFO cinder.volume.manager [req-69e7aaff-7184-4f71-b004-b830c294e02f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 74c129af-c114-430b-aefa-ae5d2b7274df: extending
######2015-12-10 16:17:26.658 2543 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-69e7aaff-7184-4f71-b004-b830c294e02f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateFileSystem].
######2015-12-10 16:17:26.659 2543 INFO cinder.volume.manager [req-69e7aaff-7184-4f71-b004-b830c294e02f 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 74c129af-c114-430b-aefa-ae5d2b7274df: extended successfully

#####FROM BACKEND 2
######2015-12-10 16:17:45.944 2544 INFO cinder.volume.manager [req-62ee94c3-fe3b-4b40-a293-b54530ad77c2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 687c9648-314d-4ff9-94c0-b7de7b2a2d54: extending
######2015-12-10 16:17:46.289 2544 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-62ee94c3-fe3b-4b40-a293-b54530ad77c2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateFileSystem].
######2015-12-10 16:17:46.290 2544 INFO cinder.volume.manager [req-62ee94c3-fe3b-4b40-a293-b54530ad77c2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 687c9648-314d-4ff9-94c0-b7de7b2a2d54: extended successfully

#####FROM BACKEND 3
######2015-12-10 16:18:07.254 2545 INFO cinder.volume.manager [req-21ab8873-f302-4022-8c32-e9e1ec45da53 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 27790bf5-fcdb-4193-8277-62117ee7b13a: extending
######2015-12-10 16:18:07.570 2545 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-21ab8873-f302-4022-8c32-e9e1ec45da53 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] CloudByte API executed successfully for command [updateFileSystem].
######2015-12-10 16:18:07.570 2545 INFO cinder.volume.manager [req-21ab8873-f302-4022-8c32-e9e1ec45da53 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] volume 27790bf5-fcdb-4193-8277-62117ee7b13a: extended successfully


