#####LOGS:

######2015-12-14 10:41:08.407 2972 INFO cinder.volume.manager [req-467aca39-973c-42e2-a789-45e2b7fc973d - - - - -] Updating volume status
######2015-12-14 10:41:08.429 2972 INFO cinder.volume.drivers.cloudbyte.cloudbyte [req-467aca39-973c-42e2-a789-45e2b7fc973d - - - - -] CloudByte API executed successfully for command [listTsm].
######2015-12-14 10:41:08.429 2972 ERROR cinder.openstack.common.periodic_task [req-467aca39-973c-42e2-a789-45e2b7fc973d - - - - -] Error during VolumeManager._report_driver_status: 'NoneType' object is not iterable
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task Traceback (most recent call last):
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/openstack/common/periodic_task.py", line 224, in run_periodic_tasks
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task     task(self, context)
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1507, in _report_driver_status
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task     volume_stats = self.driver.get_volume_stats(refresh=True)
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task     return f(*args, **kwargs)
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1273, in get_volume_stats
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task     data = self._get_storage_info(tsm_name)
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 728, in _get_storage_info
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task     for tsms in tsm_details:
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task TypeError: 'NoneType' object is not iterable
######2015-12-14 10:41:08.429 2972 TRACE cinder.openstack.common.periodic_task
