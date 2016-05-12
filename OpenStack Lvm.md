### OpenStack LVM using CloudByte's iSCSI Volume
To use CloudByte's iSCSI volume as the underlying source for lvm we need to follow some guidelines:
- Create an iSCSI volume in CloudByte ElastiCenter and assign an initiator group.
  - The initiator group can be 'ALL' or user defined pointing to the OpenStack machine
- The following steps were done on Ubuntu 14.04 that hosted the OpenStack setup.

#### iSCSI Initiator Install
- Configure Ubuntu Server as an iSCSI initiator install the open-iscsi package. 
```
  sudo apt install open-iscsi
```

#### iSCSI Initiator Configuration
- Edit */etc/iscsi/iscsid.conf*
```
  node.startup = automatic
```
- Check which targets are available by using the *iscsiadm* utility. Enter the following in a terminal:
```
  sudo iscsiadm -m discovery -t st -p 192.168.0.10
```
  1. -m: determines the mode that iscsiadm executes in.
  2. -t: specifies the type of discovery.
  3. -p: option indicates the target IP address.
```
  NOTE : Change example 192.168.0.10 to the target IP address on your network.
```
- If the target is available you should see output similar to the following:
```
  192.168.0.10:3260,1 iqn.1992-05.com.emc:sl7b92030000520000-2
```
```
  NOTE : The iqn number and IP address above will vary depending on your hardware.
```
- You should now be able to connect to the iSCSI target, and depending on your target setup you may have to enter user credentials. Login to the iSCSI node:
```
  sudo iscsiadm -m node --login
```
- Check to make sure that the new disk has been detected using *dmesg*:

```
dmesg | grep sd

  [    4.322384] sd 2:0:0:0: Attached scsi generic sg1 type 0
  [    4.322797] sd 2:0:0:0: [sda] 41943040 512-byte logical blocks: (21.4 GB/20.0 GiB)
  [    4.322843] sd 2:0:0:0: [sda] Write Protect is off
  [    4.322846] sd 2:0:0:0: [sda] Mode Sense: 03 00 00 00
  [    4.322896] sd 2:0:0:0: [sda] Cache data unavailable
  [    4.322899] sd 2:0:0:0: [sda] Assuming drive cache: write through
  [    4.323230] sd 2:0:0:0: [sda] Cache data unavailable
  [    4.323233] sd 2:0:0:0: [sda] Assuming drive cache: write through
  [    4.325312]  sda: sda1 sda2 < sda5 >
  [    4.325729] sd 2:0:0:0: [sda] Cache data unavailable
  [    4.325732] sd 2:0:0:0: [sda] Assuming drive cache: write through
  [    4.325735] sd 2:0:0:0: [sda] Attached SCSI disk
  [ 2486.941805] sd 4:0:0:3: Attached scsi generic sg3 type 0
  [ 2486.952093] sd 4:0:0:3: [sdb] 1126400000 512-byte logical blocks: (576 GB/537 GiB)
  [ 2486.954195] sd 4:0:0:3: [sdb] Write Protect is off
  [ 2486.954200] sd 4:0:0:3: [sdb] Mode Sense: 8f 00 00 08
  [ 2486.954692] sd 4:0:0:3: [sdb] Write cache: disabled, read cache: enabled, doesn't
  support DPO or FUA
  [ 2486.960577]  sdb: sdb1
  [ 2486.964862] sd 4:0:0:3: [sdb] Attached SCSI disk
```
- In the output above *sdb* is the new iSCSI disk. Remember this is just an example; the output you see on your screen will vary.
- Next, create a partition, format the file system, and mount the new iSCSI disk. In a terminal enter:
```
  sudo fdisk /dev/sdb
  n
  p
  enter
  enter
  w
```
- The above commands are from inside the fdisk utility; see man fdisk for more detailed instructions. Also, the cfdisk utility is sometimes more user friendly.
- Now format the file system:
```
  sudo mkfs.ext4 /dev/sdb1
```

### Configuring and using CloudByte's iSCSI volume as LVM volume group

- After above steps are done we need to proceed with the next steps, which involves the creation of a new lvm group on the iSCSI volume created and added, and to use it for volume and VM creation in OpenStack.
- Now run below command to verify existence of lvm volume groups
```
  sudo vgs
```
  You will get the following output:
```
  VG                        #PV #LV #SN Attr   VSize  VFree
  stack-volumes-default       1   0   0 wz--n- 10.01g 10.01g
  stack-volumes-lvmdriver-1   1   1   0 wz--n- 10.01g  9.01g
```
- Run the following commands to create the new lvm volume group
```
  // Assuming /dev/sdb is the partition you want to use for Cinder LVM integration, 
  sudo pvcreate /dev/sdb1                 			// here /dev/sdb1 is a valid unused device
  sudo vgcreate cinder-volumes /dev/sdb1
```
```
  NOTE : You may get the following error
         sudo pvcreate /dev/sdb1
         Device /dev/sdb1 not found (or ignored by filtering).
  SOLUTION :
          sudo vi /etc/lvm/lvm.conf
          Comment the following line
          global_filter = [ "a|loop0|", "a|loop1|", "r|.*|" ]  # from devstack
```
- Run below command to verify existence of new lvm volume group added.
```
  sudo vgs
  
  VG                        #PV #LV #SN Attr   VSize  VFree
  cinder-volumes              1   1   0 wz--n- 10.00g  9.00g
  stack-volumes-default       1   0   0 wz--n- 10.01g 10.01g
  stack-volumes-lvmdriver-1   1   1   0 wz--n- 10.01g  9.01g
```
- Now we need to create a new LVM backend in *cinder.conf* and add the new volume-group to it:
```
  sudo vi /etc/cinder/cinder.conf
  
  [DEFAULT]
  default_volume_type = lvmdriver-1,cb-lvm
  enabled_backends = lvmdriver-1,cloudbyte-lvm
  
  [cloudbyte-lvm]
  lvm_type = default
  iscsi_helper = tgtadm
  volume_group = cinder-volumes
  volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
  volume_backend_name = cloudbyte-lvm
```
```
  NOTE : After adding the backend create a new volume type for it and assign the volume_backend_name to it as mentioned in     
         default_volume_type.
```
- Now restart the 

  
