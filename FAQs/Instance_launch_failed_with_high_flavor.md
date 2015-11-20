### Observation :

Message

No valid host was found.

Code

500

Details

File "/opt/stack/nova/nova/conductor/manager.py", line 616, in build_instances request_spec, filter_properties) File "/opt/stack/nova/nova/scheduler/client/__init__.py", line 49, in select_destinations context, request_spec, filter_properties) File "/opt/stack/nova/nova/scheduler/client/__init__.py", line 35, in __run_method return getattr(self.instance, __name)(*args, **kwargs) File "/opt/stack/nova/nova/scheduler/client/query.py", line 34, in select_destinations context, request_spec, filter_properties) File "/opt/stack/nova/nova/scheduler/rpcapi.py", line 108, in select_destinations request_spec=request_spec, filter_properties=filter_properties) File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/rpc/client.py", line 152, in call retry=self.retry) File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/transport.py", line 90, in _send timeout=timeout, retry=retry) File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/_drivers/amqpdriver.py", line 408, in send retry=retry) File "/usr/local/lib/python2.7/dist-packages/oslo/messaging/_drivers/amqpdriver.py", line 399, in _send raise result


### Nova-Scheduler logs:

2015-03-20 13:28:22.587 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Starting with 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:70

2015-03-20 13:28:22.588 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter RetryFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.592 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter AvailabilityZoneFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.592 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter RamFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.593 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter ComputeFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.593 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter ComputeCapabilitiesFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.593 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter ImagePropertiesFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.637 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter ServerGroupAntiAffinityFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.638 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter ServerGroupAffinityFilter returned 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:88

2015-03-20 13:28:22.638 DEBUG nova.scheduler.filter_scheduler [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filtered [(devsosci-S1200RP-SE, devsosci-S1200RP-SE) ram:31601 disk:407552 io_ops:0 instances:0] _schedule /opt/stack/nova/nova/scheduler/filter_scheduler.py:281

2015-03-20 13:28:22.638 DEBUG nova.scheduler.filter_scheduler [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Weighed [WeighedHost [host: (devsosci-S1200RP-SE, devsosci-S1200RP-SE) ram:31601 disk:407552 io_ops:0 instances:0, weight: 1.0]] _schedule /opt/stack/nova/nova/scheduler/filter_scheduler.py:286

2015-03-20 13:28:22.639 27358 INFO oslo.messaging._drivers.impl_rabbit [-] Connecting to AMQP server on 20.10.22.158:5672

2015-03-20 13:28:22.644 27358 INFO oslo.messaging._drivers.impl_rabbit [-] Connected to AMQP server on 20.10.22.158:5672

2015-03-20 13:28:49.165 27358 DEBUG nova.openstack.common.periodic_task [-] Running periodic task SchedulerManager._run_periodic_tasks run_periodic_tasks /opt/stack/nova/nova/openstack/common/periodic_task.py:193

2015-03-20 13:28:49.166 27358 DEBUG nova.openstack.common.loopingcall [-] Dynamic looping call <bound method Service.periodic_tasks of <nova.service.Service object at 0x7fe28bd4b810>> sleeping for 3.66 seconds _inner /opt/stack/nova/nova/openstack/common/loopingcall.py:132

2015-03-20 13:28:52.829 27358 DEBUG nova.openstack.common.periodic_task [-] Running periodic task SchedulerManager._expire_reservations run_periodic_tasks /opt/stack/nova/nova/openstack/common/periodic_task.py:193

2015-03-20 13:28:52.832 27358 DEBUG nova.openstack.common.loopingcall [-] Dynamic looping call <bound method Service.periodic_tasks of <nova.service.Service object at 0x7fe28bd4b810>> sleeping for 57.33 seconds _inner /opt/stack/nova/nova/openstack/common/loopingcall.py:132

2015-03-20 13:29:27.853 DEBUG nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Starting with 1 host(s) get_filtered_objects /opt/stack/nova/nova/filters.py:70

2015-03-20 13:29:27.854 DEBUG nova.scheduler.filters.retry_filter [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Host [u'devsosci-S1200RP-SE', u'devsosci-S1200RP-SE'] fails.  Previously tried hosts: [[u'devsosci-S1200RP-SE', u'devsosci-S1200RP-SE']] host_passes /opt/stack/nova/nova/scheduler/filters/retry_filter.py:42

2015-03-20 13:29:27.854 INFO nova.filters [req-6e082969-fa5e-40da-81ea-1dbb4c7b6130 admin admin] Filter RetryFilter returned 0 hosts


### Solution :

Try a different flavor. Check the resources available in your hypervisor.