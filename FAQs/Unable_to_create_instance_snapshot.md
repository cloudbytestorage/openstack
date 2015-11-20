### Observation :

2015-04-28 08:33:22.405 2792 ERROR cinder.volume.drivers.cloudbyte.cloudbyte [req-6855e855-4d51-49e8-b2eb-adf2d604ef24 32946fd09dc94bd2bdf3b8cca8e341a5 ee64e3d8145848b68c2b074b7343b8a6 - - -] Error executing CloudByte API createStorageSnapshot, Error: No JSON object could be decoded

2015-04-28 08:33:22.491 2792 ERROR oslo.messaging.rpc.dispatcher [req-6855e855-4d51-49e8-b2eb-adf2d604ef24 32946fd09dc94bd2bdf3b8cca8e341a5 ee64e3d8145848b68c2b074b7343b8a6 - - -] Exception during message handling: Error executing CloudByte API createStorageSnapshot, Error: No JSON object could be decoded

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher Traceback (most recent call last):

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/oslo/messaging/rpc/dispatcher.py", line 137, in _dispatch_and_reply

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     incoming.message))

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/oslo/messaging/rpc/dispatcher.py", line 180, in _dispatch

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     return self._do_dispatch(endpoint, method, ctxt, args)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/oslo/messaging/rpc/dispatcher.py", line 126, in _do_dispatch

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     result = getattr(endpoint, method)(ctxt, **new_args)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     return f(*args, **kwargs)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/cinder/volume/manager.py", line 536, in create_snapshot

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     {'status': 'error'})

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/cinder/openstack/common/excutils.py", line 82, in __exit__

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     six.reraise(self.type_, self.value, self.tb)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/cinder/volume/manager.py", line 527, in create_snapshot

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     model_update = self.driver.create_snapshot(snapshot_ref)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     return f(*args, **kwargs)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1100, in create_snapshot

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     self._api_request_for_cloudbyte('createStorageSnapshot', params)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.6/site-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 226, in _api_request_for_cloudbyte

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher     raise exception.VolumeBackendAPIException(msg)

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher VolumeBackendAPIException: Error executing CloudByte API createStorageSnapshot, Error: No JSON object could be decoded

2015-04-28 08:33:22.491 2792 TRACE oslo.messaging.rpc.dispatcher


### Solution :

Solved in master, need to do the same in icehouse and juno.