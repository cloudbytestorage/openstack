### Observation :

Image Property has

hw_qemu_guest_agent = yes

@ nova compute logs

937447 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] Traceback (most recent call last):

937448 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/compute/manager.py", line 2246, in _build_resources

937449 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     yield resources

937450 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/compute/manager.py", line 2116, in _build_and_run_instance

937451 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     block_device_info=block_device_info)

937452 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/virt/libvirt/driver.py", line 2622, in spawn

937453 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     block_device_info, disk_info=disk_info)

937454 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/virt/libvirt/driver.py", line 4425, in _create_domain_and_network

937455 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     power_on=power_on)

937456 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/virt/libvirt/driver.py", line 4349, in _create_domain

937457 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     LOG.error(err)

937458 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/openstack/common/excutils.py", line 82, in __exit__

937459 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     six.reraise(self.type_, self.value, self.tb)

937460 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/opt/stack/nova/nova/virt/libvirt/driver.py", line 4339, in _create_domain

937461 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     domain.createWithFlags(launch_flags)

937462 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/usr/local/lib/python2.7/dist-packages/eventlet/tpool.py", line 183, in doit

937463 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     result = proxy_call(self._autowrap, f, *args, **kwargs)

937464 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/usr/local/lib/python2.7/dist-packages/eventlet/tpool.py", line 141, in proxy_call

937465 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     rv = execute(f, *args, **kwargs)

937466 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/usr/local/lib/python2.7/dist-packages/eventlet/tpool.py", line 122, in execute

937467 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     six.reraise(c, e, tb)

937468 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/usr/local/lib/python2.7/dist-packages/eventlet/tpool.py", line 80, in tworker

937469 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     rv = meth(*args, **kwargs)

937470 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]   File "/usr/lib/python2.7/dist-packages/libvirt.py", line 896, in createWithFlags

937471 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]     if ret == -1: raise libvirtError ('virDomainCreateWithFlags() failed', dom=self)

937472 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] libvirtError: internal error: process exited while connecting to monitor: qemu-system-x86_64: -cha       rdev socket,id=charchannel0,path=/var/lib/libvirt/qemu/org.qemu.guest_agent.0.instance-00000016.sock,server,nowait: Failed to bind socket: Permission denied

937473 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] qemu-system-x86_64: -chardev socket,id=charchannel0,path=/var/lib/libvirt/qemu/org.qemu.guest_agen       t.0.instance-00000016.sock,server,nowait: chardev: opening backend "socket" failed

937474 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]

937475 2015-03-20 13:49:44.014 27294 TRACE nova.compute.manager [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df]

937476 2015-03-20 13:49:44.015 AUDIT nova.compute.manager [req-78b3b447-a189-46bc-81e9-b1e69eca0a56 admin admin] [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] Terminating instance

937477 2015-03-20 13:49:44.020 27294 INFO nova.virt.libvirt.driver [-] [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] Instance destroyed successfully.

...

2015-03-20 13:49:45.109 27294 DEBUG nova.compute.utils [-] [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] internal error: process exited while connecting to monitor: qemu-system-x86_64: -chardev socket,       id=charchannel0,path=/var/lib/libvirt/qemu/org.qemu.guest_agent.0.instance-00000016.sock,server,nowait: Failed to bind socket: Permission denied

937529 qemu-system-x8 notify_about_instance_usage /opt/stack/nova/nova/compute/utils.py:320

937530 2015-03-20 13:49:45.109 27294 DEBUG nova.compute.manager [-] [instance: cddc4641-3f2d-4282-a8ec-0a2f9eac72df] Build of instance cddc4641-3f2d-4282-a8ec-0a2f9eac72df was re-scheduled: internal error: process exited while connecting to monitor: qemu-system-x86_64: -chardev socket,id=charchannel0,path=/var/lib/libvirt/qemu/org.qemu.guest_agent.0.instance-00000016.sock,server,nowait: Failed to bind socket: Permission denied

937531 qemu-system-x86_64: -chardev socket,id=charchannel0,path=/var/lib/libvirt/qemu/org.qemu.guest_agent.0.instance-00000016.sock,server,nowait: chardev: opening backend "socket" failed

937532  _do_build_and_run_instance /opt/stack/nova/nova/compute/manager.py:2035

...

This may not be related but still as this is a devstack & a permission issue, lets check the sudoers file.

vim /etc/sudoers 

/#
'#' This file MUST be edited with the 'visudo' command as root.
'#'
'#' Please consider adding local content in /etc/sudoers.d/ instead of
'#'directly modifying this file.
'#'
'#' See the man page for details on how to write a sudoers file.
'#'

| Defaults  |     env_reset                                                                  |

| Defaults  |     mail_badpass                                                               |

| Defaults  |     secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" |

'#' Host alias specification

'#' User alias specification

'#' Cmnd alias specification

'#' User privilege specification

root    ALL=(ALL:ALL) ALL

'#' Members of the admin group may gain root privileges

%admin ALL=(ALL) ALL

'#' Allow members of group sudo to execute any command

%sudo   ALL=(ALL:ALL) ALL

'#' See sudoers(5) for more information on "#include" directives:

'#'includedir /etc/sudoers.d

devsosci ALL=(ALL) NOPASSWD: ALL

stack ALL=(ALL) NOPASSWD: ALL

...


### Solution :

For Ubuntu, you need to apply this fix since AppArmor will not allow the creation of the socket:

$ sudo echo "/var/lib/libvirt/qemu/*.sock rw," | sudo tee -a /etc/apparmor.d/abstractions/libvirt-qemu

$ sudo service libvirt-bin restart

$ sudo service nova-compute restart

$ sudo service apparmor reload

After performing these steps instance has to be created.
