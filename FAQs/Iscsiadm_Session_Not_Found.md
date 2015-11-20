### Cinder Volume Logs :

2015-03-18 12:46:55.489 3625 DEBUG oslo_concurrency.processutils [-] CMD "sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418 -p 192.168.1.252:3260 --login" returned: 8 in 121.624s execute /usr/local/lib/python2.7/dist-packages/oslo_concurrency/processutils.py:225

2015-03-18 12:46:55.490 3625 DEBUG oslo_concurrency.processutils [-] u'sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418 -p 192.168.1.252:3260 --login' failed. Not Retrying. execute /usr/local/lib/python2.7/dist-packages/oslo_concurrency/processutils.py:258

2015-03-18 12:46:55.491 3625 WARNING cinder.brick.initiator.connector [-] Failed to login iSCSI target iqn.

2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418 on portal 192.168.1.252:3260 (exit code 8).

2015-03-18 12:46:55.491 3625 WARNING cinder.brick.initiator.connector [-] Failed to login to any of the iSCSI targets.

2015-03-18 12:46:55.492 3625 WARNING cinder.brick.initiator.connector [-] ISCSI volume not yet found at: [u'/dev/disk/by-path/ip-192.168.1.252:3260-iscsi-iqn.2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418-lun-0']. Will rescan & retry.  Try number: 0

2015-03-18 12:46:55.493 3625 DEBUG oslo_concurrency.processutils [-] Running cmd (subprocess): sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418 -p 192.168.1.252:3260 --rescan execute /usr/local/lib/python2.7/dist-packages/oslo_concurrency/processutils.py:199

2015-03-18 12:46:55.572 3625 DEBUG oslo_concurrency.processutils [-] CMD "sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418 -p 192.168.1.252:3260 --rescan" returned: 21 in 0.079s execute /usr/local/lib/python2.7/dist-packages/oslo_concurrency/processutils.py:225

2015-03-18 12:46:55.573 3625 DEBUG oslo_concurrency.processutils [-] u'sudo cinder-rootwrap /etc/cinder/rootwrap.conf iscsiadm -m node -T iqn.2015-01.acc1.cinder:acc13afa9c71f6d4498cbaae9ee8720c8418 -p 192.168.1.252:3260 --rescan' failed. Not Retrying. execute /usr/local/lib/python2.7/dist-packages/oslo_concurrency/processutils.py:258

2015-03-18 12:46:55.574 3625 DEBUG oslo_concurrency.lockutils [-] Lock "connect_volume" released by "connect_volume" :: held 122.041s inner /usr/local/lib/python2.7/dist-packages/oslo_concurrency/lockutils.py:442

2015-03-18 12:46:55.575 3625 ERROR cinder.volume.flows.manager.create_volume [-] Failed to copy image 9e88aacf-b2aa-4d46-94ad-d3604d61814b to volume: 3afa9c71-f6d4-498c-baae-9ee8720c8418, error: iscsiadm: No session found.

### Solution :

Provide the following in cinder.conf : "cb_initiator_group_name = ALL"