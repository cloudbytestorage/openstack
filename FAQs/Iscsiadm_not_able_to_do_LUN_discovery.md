### Cinder Volume Logs :

2015-03-18 13:39:14.345 5560 WARNING cinder.volume.manager [-] Flow 'volume_create_manager' (d79b2f56-57ab-4379-a7f6-01f738643d59) transitioned into state 'REVERTED' from state 'RUNNING'

2015-03-18 13:39:14.346 5560 ERROR oslo_messaging.rpc.dispatcher [-] Exception during message handling: Failed to copy image to volume: qemu-img: /dev/disk/by-path/ip-20.10.44.25:3260-iscsi-iqn.2015-01.acc1.RMSQL:acc1c0f31d7a19314a1495bfe0c275d6caf9-lun-0: error while converting raw: Could not open device: No such device or address

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher Traceback (most recent call last):

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 142, in _dispatch_and_reply

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     executor_callback))

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 186, in _dispatch

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     executor_callback)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/oslo_messaging/rpc/dispatcher.py", line 130, in _do_dispatch

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     result = func(ctxt, **new_args)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     return f(*args, **kwargs)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/manager.py", line 443, in create_volume
2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     _run_flow()
2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/manager.py", line 436, in _run_flow
2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     flow_engine.run()

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/engines/action_engine/engine.py", line 96, in run

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     for _state in self.run_iter():

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/engines/action_engine/engine.py", line 153, in run_iter

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     failure.Failure.reraise_if_any(failures.values())

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/types/failure.py", line 244, in reraise_if_any

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     failures[0].reraise()

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/types/failure.py", line 251, in reraise

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     six.reraise(*self._exc_info)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/engines/action_engine/executor.py", line 67, in _execute_task

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     result = task.execute(**arguments)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/flows/manager/create_volume.py", line 649, in execute

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     **volume_spec)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/flows/manager/create_volume.py", line 601, in _create_from_image

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     image_id, image_location, image_service)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/flows/manager/create_volume.py", line 500, in _copy_image_to_volume

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher     raise exception.ImageCopyFailure(reason=ex.stderr)

2015-03-18 13:39:14.346 5560 TRACE oslo_messaging.rpc.dispatcher ImageCopyFailure: Failed to copy image to volume: qemu-img: /dev/disk/by-path/ip-20.10.44.25:3260-iscsi-iqn.2015-01.acc1.RMSQL:acc1c0f31d7a19314a1495bfe0c275d6caf9-lun-0: error while converting raw: Could not open device: No such device or address

### Solution :

The VSM is reachable. But iscsiadm is not able to do LUN discovery. Tried to do a discovery from other client. It was working fine. It might happen that this particular client was not responding properly. 
