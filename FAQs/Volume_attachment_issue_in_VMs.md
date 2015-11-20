### Cinder Volume logs :

2015-04-28 12:47:47.672 690 ERROR cinder.volume.manager [req-7ad310ec-8ae1-48d4-8c2b-0ae174695b6c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:47.673 690 ERROR oslo.messaging.rpc.dispatcher [req-7ad310ec-8ae1-48d4-8c2b-0ae174695b6c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Exception during message handling: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher Traceback (most recent call last):

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher 	incoming.message))

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher 	return self._do_dispatch(endpoint, method, ctxt, args)

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher 	result = getattr(endpoint, method)(ctxt, **new_args)

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher 	raise exception.VolumeBackendAPIException(data=err_msg)

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:47.673 690 TRACE oslo.messaging.rpc.dispatcher

2015-04-28 12:47:47.674 690 ERROR oslo.messaging._drivers.common [req-7ad310ec-8ae1-48d4-8c2b-0ae174695b6c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Returning exception Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper. to caller

2015-04-28 12:47:47.675 690 ERROR oslo.messaging._drivers.common [req-7ad310ec-8ae1-48d4-8c2b-0ae174695b6c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] ['Traceback (most recent call last):\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply\n	incoming.message))\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch\n	return self._do_dispatch(endpoint, method, ctxt, args)\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch\n	result = getattr(endpoint, method)(ctxt, **new_args)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection\n	raise exception.VolumeBackendAPIException(data=err_msg)\n', 'VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.\n']

2015-04-28 12:47:48.739 690 ERROR cinder.volume.manager [req-cf34aaaf-2cfc-4016-bf5b-413b4ca4441c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:48.740 690 ERROR oslo.messaging.rpc.dispatcher [req-cf34aaaf-2cfc-4016-bf5b-413b4ca4441c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Exception during message handling: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher Traceback (most recent call last):

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher 	incoming.message))

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher 	return self._do_dispatch(endpoint, method, ctxt, args)

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher 	result = getattr(endpoint, method)(ctxt, **new_args)

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher 	raise exception.VolumeBackendAPIException(data=err_msg)

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:48.740 690 TRACE oslo.messaging.rpc.dispatcher

2015-04-28 12:47:48.741 690 ERROR oslo.messaging._drivers.common [req-cf34aaaf-2cfc-4016-bf5b-413b4ca4441c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Returning exception Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper. to caller

2015-04-28 12:47:48.741 690 ERROR oslo.messaging._drivers.common [req-cf34aaaf-2cfc-4016-bf5b-413b4ca4441c 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] ['Traceback (most recent call last):\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply\n	incoming.message))\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch\n	return self._do_dispatch(endpoint, method, ctxt, args)\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch\n	result = getattr(endpoint, method)(ctxt, **new_args)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection\n	raise exception.VolumeBackendAPIException(data=err_msg)\n', 'VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.\n']

2015-04-28 12:47:50.811 690 ERROR cinder.volume.manager [req-caef9c0b-ea25-415c-a993-d275e005fbf8 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:50.812 690 ERROR oslo.messaging.rpc.dispatcher [req-caef9c0b-ea25-415c-a993-d275e005fbf8 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Exception during message handling: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher Traceback (most recent call last):

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher 	incoming.message))

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher 	return self._do_dispatch(endpoint, method, ctxt, args)

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher 	result = getattr(endpoint, method)(ctxt, **new_args)

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher 	raise exception.VolumeBackendAPIException(data=err_msg)

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:50.812 690 TRACE oslo.messaging.rpc.dispatcher

2015-04-28 12:47:50.813 690 ERROR oslo.messaging._drivers.common [req-caef9c0b-ea25-415c-a993-d275e005fbf8 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Returning exception Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper. to caller

2015-04-28 12:47:50.813 690 ERROR oslo.messaging._drivers.common [req-caef9c0b-ea25-415c-a993-d275e005fbf8 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] ['Traceback (most recent call last):\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply\n	incoming.message))\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch\n	return self._do_dispatch(endpoint, method, ctxt, args)\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch\n	result = getattr(endpoint, method)(ctxt, **new_args)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection\n	raise exception.VolumeBackendAPIException(data=err_msg)\n', 'VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.\n']

2015-04-28 12:47:54.906 690 ERROR cinder.volume.manager [req-3ece5b77-f40f-46b1-9e8c-04a67397e7a0 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:54.907 690 ERROR oslo.messaging.rpc.dispatcher [req-3ece5b77-f40f-46b1-9e8c-04a67397e7a0 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Exception during message handling: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher Traceback (most recent call last):

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher 	incoming.message))

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher 	return self._do_dispatch(endpoint, method, ctxt, args)

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher 	result = getattr(endpoint, method)(ctxt, **new_args)

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher 	return f(*args, **kwargs)

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher   File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher 	raise exception.VolumeBackendAPIException(data=err_msg)

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.

2015-04-28 12:47:54.907 690 TRACE oslo.messaging.rpc.dispatcher

2015-04-28 12:47:54.908 690 ERROR oslo.messaging._drivers.common [req-3ece5b77-f40f-46b1-9e8c-04a67397e7a0 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] Returning exception Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper. to caller

2015-04-28 12:47:54.908 690 ERROR oslo.messaging._drivers.common [req-3ece5b77-f40f-46b1-9e8c-04a67397e7a0 3f3ecfa581fd42b397b06fe9f9aa2578 bd5fdc9a39fd4586bf2ed6182a4c7585 - - -] ['Traceback (most recent call last):\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 134, in _dispatch_and_reply\n	incoming.message))\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 177, in _dispatch\n	return self._do_dispatch(endpoint, method, ctxt, args)\n', '  File "/usr/lib/python2.7/site-packages/oslo/messaging/rpc/dispatcher.py", line 123, in _do_dispatch\n	result = getattr(endpoint, method)(ctxt, **new_args)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/osprofiler/profiler.py", line 105, in wrapper\n	return f(*args, **kwargs)\n', '  File "/usr/lib/python2.7/site-packages/cinder/volume/manager.py", line 902, in initialize_connection\n	raise exception.VolumeBackendAPIException(data=err_msg)\n', 'VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Unable to fetch connection information from backend: Command requested root, but did not specify a root helper.\n']

2015-04-28 12:48:06.853 690 INFO cinder.volume.manager [-] Updating volume status

2015-04-28 12:48:15.217 679 INFO cinder.volume.manager [-] Updating volume status

2015-04-28 12:48:15.297 679 INFO cinder.volume.manager [-] Updating volume replication status.


### Solution :

root cause : tgt service was not started.