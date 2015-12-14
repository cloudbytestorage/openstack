#####LOGS:

######2015-12-11 12:23:00.594 2970 INFO cinder.volume.manager [req-d436b810-6263-49c5-9228-cdfd8edd2b77 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] snapshot c4a20d28-48f2-4f4c-a5ae-2bec50cfd7ad: deleting
######2015-12-11 12:23:00.849 2970 ERROR oslo_messaging.rpc.dispatcher [req-d436b810-6263-49c5-9228-cdfd8edd2b77 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Exception during message handling: Bad or unexpected response from the storage volume backend API: Failed to execute CloudByte API [deleteSnapshot]. Http status: 431, Error: could not find any snapshots to destroy; check snapshot names.
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher Traceback (most recent call last):
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 142, in _dispatch_and_reply
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback))
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 186, in _dispatch
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 130, in _do_dispatch
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     result = func(ctxt, **new_args)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 179, in lso_inner1
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     return lso_inner2(inst, context, snapshot, **kwargs)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_concurrency/lockutils.py", line 445, in inner
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 178, in lso_inner2
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*_args, **_kwargs)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 725, in delete_snapshot
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     snapshot.save()
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_utils/excutils.py", line 85, in __exit__
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     six.reraise(self.type_, self.value, self.tb)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 715, in delete_snapshot
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     self.driver.delete_snapshot(snapshot)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1227, in delete_snapshot
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     self._api_request_for_cloudbyte('deleteSnapshot', params)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 267, in _api_request_for_cloudbyte
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher     raise exception.VolumeBackendAPIException(data=msg)
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Failed to execute CloudByte API [deleteSnapshot]. Http status: 431, Error: could not find any snapshots to destroy; check snapshot names.
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher .
######2015-12-11 12:23:00.849 2970 TRACE oslo_messaging.rpc.dispatcher
