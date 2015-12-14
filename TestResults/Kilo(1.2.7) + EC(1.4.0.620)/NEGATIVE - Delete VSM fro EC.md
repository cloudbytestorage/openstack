#####LOGS:

- Get storage info log from cinder

######2015-12-11 15:49:44.285 2970 ERROR cinder.volume.drivers.cloudbyte.cloudbyte [req-e0d9bd0d-f480-4d05-b620-afd3a35580c1 - - - - -] TSM [VSM1] not found in CloudByte storage.

- (Create volume + Delete volume + Create Snapshot + Delete Snapshot + Create Clone + Delete Clone) Logs

######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager Traceback (most recent call last):
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/taskflow/engines/action_engine/executor.py", line 67, in _execute_task
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     result = task.execute(**arguments)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/flows/manager/create_volume.py", line 639, in execute
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     **volume_spec)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/flows/manager/create_volume.py", line 613, in _create_raw_volume
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     return self.driver.create_volume(volume_ref)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     return f(*args, **kwargs)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 932, in create_volume
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     volume, tsm_details.get('tsmid'), cb_volume_name, qos_group_params)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 298, in _add_qos_group_request
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     data = self._api_request_for_cloudbyte("addQosGroup", params)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 267, in _api_request_for_cloudbyte
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager     raise exception.VolumeBackendAPIException(data=msg)
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager VolumeBackendAPIException: Bad or unexpected response from the storage volume backend API: Failed to execute CloudByte API [addQosGroup]. Http status: 431, Error: Unable to execute API command addqosgroup due to missing parameter tsmid.
######2015-12-11 15:50:24.276 2970 TRACE cinder.volume.manager
