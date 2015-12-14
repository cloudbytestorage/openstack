### LOGS:

######2015-12-11 11:31:12.413 8183 ERROR cinder.openstack.common.periodic_task [req-f8da8098-ee2e-4d0e-8d7b-3d2959330005 - - - - -] Error during VolumeManager._report_driver_status: [Errno 113] EHOSTUNREACH
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task Traceback (most recent call last):
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/openstack/common/periodic_task.py", line 224, in run_periodic_tasks
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     task(self, context)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 1507, in _report_driver_status
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     volume_stats = self.driver.get_volume_stats(refresh=True)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/osprofiler/profiler.py", line 105, in wrapper
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     return f(*args, **kwargs)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 1273, in get_volume_stats
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     data = self._get_storage_info(tsm_name)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 714, in _get_storage_info
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     tsm_list = self._api_request_for_cloudbyte('listTsm', params={})
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 248, in _api_request_for_cloudbyte
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     res_obj = self._execute_and_get_response_details(host, url)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/cinder/volume/drivers/cloudbyte/cloudbyte.py", line 200, in _execute_and_get_response_details
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     connection.request('GET', url)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/httplib.py", line 979, in request
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     self._send_request(method, url, body, headers)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/httplib.py", line 1013, in _send_request
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     self.endheaders(body)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/httplib.py", line 975, in endheaders
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     self._send_output(message_body)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/httplib.py", line 835, in _send_output
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     self.send(msg)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/httplib.py", line 797, in send
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     self.connect()
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/httplib.py", line 1178, in connect
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     self.timeout, self.source_address)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task   File "/usr/lib/python2.7/dist-packages/eventlet/green/socket.py", line 61, in create_connection
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task     raise error(msg)
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task error: [Errno 113] EHOSTUNREACH
######2015-12-11 11:31:12.413 8183 TRACE cinder.openstack.common.periodic_task
######2015-12-11 11:31:12.420 8183 WARNING cinder.openstack.common.loopingcall [req-f8da8098-ee2e-4d0e-8d7b-3d2959330005 - - - - -] task u'<bound method Service.periodic_tasks of <cinder.service.Service object #####FROM 0xb6a7266c>>' run outlasted interval by 6.16 sec
