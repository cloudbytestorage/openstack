### Observation :

2015-03-20 13:46:13.999 26841 ERROR oslo.messaging.rpc.dispatcher [req-e1f4df9a-f540-413f-bff6-a4abe3190cc3 5067c6594772458fb6af37beaf0850a7 0bbe5b28f466447d8fddb71333ee3936 - - -] Exception during message handling: Failed to copy image to volume: qemu-img: /dev/disk/by-path/ip-20.10.44.25:3260-iscsi-iqn.2015-01.acc1.RMSQL:acc19671fd10e988465084ef4126c94008d3-lun-0: error while converting raw: Device is too small

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher Traceback (most recent call last):

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     incoming.message))

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     return self._do_dispatch(endpoint, method, ctxt, args)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     result = getattr(endpoint, method)(ctxt, **new_args)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     return f(*args, **kwargs)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/manager.py", line 381, in create_volume

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     _run_flow()

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/manager.py", line 374, in _run_flow

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     flow_engine.run()

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/engines/action_engine/engine.py", line 97, in run

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     for _state in self.run_iter():

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/engines/action_engine/engine.py", line 154, in run_iter

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     failure.Failure.reraise_if_any(failures.values())

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/types/failure.py", line 238, in reraise_if_any

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     failures[0].reraise()

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/types/failure.py", line 245, in reraise

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     six.reraise(*self._exc_info)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/usr/local/lib/python2.7/dist-packages/taskflow/engines/action_engine/executor.py", line 68, in _execute_task

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     result = task.execute(**arguments)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/flows/manager/create_volume.py", line 638, in execute

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     **volume_spec)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/flows/manager/create_volume.py", line 590, in _create_from_image

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     image_id, image_location, image_service)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher   File "/opt/stack/cinder/cinder/volume/flows/manager/create_volume.py", line 492, in _copy_image_to_volume

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher     raise exception.ImageCopyFailure(reason=ex.stderr)

2015-03-20 13:46:13.999 26841 TRACE oslo.messaging.rpc.dispatcher ImageCopyFailure: Failed to copy image to volume: qemu-img: /dev/disk/by-path/ip-20.10.44.25:3260-iscsi-iqn.2015-01.acc1.RMSQL:acc19671fd10e988465084ef4126c94008d3-lun-0: error while converting raw: Device is too small


### Solution :

Create the VM using a high capacity volume.