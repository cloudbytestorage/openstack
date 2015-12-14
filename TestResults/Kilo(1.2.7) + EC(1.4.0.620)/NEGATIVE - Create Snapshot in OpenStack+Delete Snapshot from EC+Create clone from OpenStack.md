#####LOGS:

######2015-12-11 12:36:06.755 2970 ERROR oslo_messaging.rpc.dispatcher [req-a3f085a7-2813-4e1c-881b-e5fcc76819b2 0481e16fe3d642039a6d72191d89c4d5 c6e21a95552c464d97c1e96851825dd7 - - -] Exception during message handling: Bad or unexpected response from the storage volume backend API: Failed to execute CloudByte API [cloneDatasetSnapshot]. Http status: 530, Error: Failed to create clone due to timeout..
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher Traceback (most recent call last):
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 142, in _dispatch_and_reply
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback))
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 186, in _dispatch
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     executor_callback)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 130, in _do_dispatch
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     result = func(ctxt, **new_args)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 470, in create_volume
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     _run_flow_locked()
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/oslo_concurrency/lockutils.py", line 445, in inner
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 460, in _run_flow_locked
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     _run_flow()
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 456, in _run_flow
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     flow_engine.run()
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/taskflow/engines/action_engine/engine.py", line 96, in run
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     for _state in self.run_iter():
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/taskflow/engines/action_engine/engine.py", line 153, in run_iter
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     failure.Failure.reraise_if_any(failures.values())
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/taskflow/types/failure.py", line 244, in reraise_if_any
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     failures[0].reraise()
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/taskflow/types/failure.py", line 251, in reraise
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     six.reraise(*self._exc_info)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/taskflow/engines/action_engine/executor.py", line 67, in _execute_task
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     result = task.execute(**arguments)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/flows/manager/create_volume.py", line 643, in execute
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     **volume_spec)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/flows/manager/create_volume.py", line 421, in _create_from_snapshot
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     snapshot)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1161, in create_volume_from_snapshot
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     self._api_request_for_cloudbyte('cloneDatasetSnapshot', params))
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 267, in _api_request_for_cloudbyte
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher     raise exception.VolumeBackendAPIException(data=msg)
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Failed to execute CloudByte API [cloneDatasetSnapshot]. Http status: 530, Error: Failed to create clone due to timeout..
######2015-12-11 12:36:06.755 2970 TRACE oslo_messaging.rpc.dispatcher
