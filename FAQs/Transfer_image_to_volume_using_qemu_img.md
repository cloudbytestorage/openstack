### Solution :

- ll /dev/disk/by-path/

- date;qemu-img convert -O raw cirros.ami /dev/disk/by-path/ip-172.16.51.78:3260-iscsi-iqn.2015-06.Acc1.TSM1:Acc1testbootvol-lun-0;date


- date;qemu-img convert -O raw /opt/stack/data/glance/images/99d42a41-2288-4e32-85c0-c81e36404012 /dev/disk/by-path/ip-172.16.51.78:3260-iscsi-iqn.2015-06.Acc1.TSM1:Acc1winvoltestboot-lun-0;date
