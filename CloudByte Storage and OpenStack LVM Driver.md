
### OpenStack LVM using CloudByte's iSCSI Volume
To use CloudByte's iSCSI volume as the underlying source for lvm we need to follow some guidelines:

Following steps were done on
- Ubuntu 14.04 that hosted the OpenStack Liberty
- ElastiCenter 1.3.0.824

### Using ElastiCenter UI
- Create an iSCSI volume in CloudByte ElastiCenter.
- Set the initiator group to 'ALL' for this new volume.


### On Ubuntu box
#### Install iSCSI Initiator
- Configure Ubuntu Server as an iSCSI initiator install the open-iscsi package. 
```
  sudo apt install open-iscsi
```

#### iSCSI Initiator Configuration
- Edit */etc/iscsi/iscsid.conf*
```
  node.startup = automatic
```

- Check the available targets
```
  sudo iscsiadm -m discovery -t st -p 192.168.0.10
  
  options
  -m: determines the mode that iscsiadm executes in.
  -t: specifies the type of discovery.
  -p: option indicates the target IP address.
  
  NOTE : Change example 192.168.0.10 to the target IP address on your network.
```

- If the target is available you should see output similar to the following:
```
  192.168.0.10:3260,1 iqn.1992-05.com.emc:sl7b92030000520000-2
  
  NOTE : The iqn number and IP address above will vary depending on your hardware.
```

- Connect to the iSCSI target
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

- In the output above **sdb** is the new iSCSI disk. 
  - this is just an example; the output you see on your screen will vary.
- Next Steps: 
  - create a partition, 
  - format the file system, and
  - mount the new iSCSI disk. 
```
  sudo fdisk /dev/sdb
  n
  p
  enter
  enter
  w
  
  NOTE :  The above commands are from inside the fdisk utility; see man fdisk for more detailed instructions. 
  NOTE : cfdisk utility is sometimes more user friendly.
```

- Format the file system
```
  sudo mkfs.ext4 /dev/sdb1
```

#### Configuring CloudByte's iSCSI volume as LVM volume group

- Verify existence of lvm volume groups
```
  sudo vgs
  
  You may get the following output:
  VG                        #PV #LV #SN Attr   VSize  VFree
  stack-volumes-default       1   0   0 wz--n- 10.01g 10.01g
  stack-volumes-lvmdriver-1   1   1   0 wz--n- 10.01g  9.01g
```

- Create a new lvm volume group on above created partition
```
  sudo pvcreate /dev/sdb1 
  sudo vgcreate cinder-cb-volumes /dev/sdb1
  
  NOTE : Assuming /dev/sdb is the partition you want to use 
  NOTE : here /dev/sdb1 is a valid unused device
  
  NOTE : If executing 'pvcreate' results into below error
         Device /dev/sdb1 not found (or ignored by filtering).
  Try below :
        sudo vi /etc/lvm/lvm.conf
        Comment the following line
        global_filter = [ "a|loop0|", "a|loop1|", "r|.*|" ]  # from devstack
```
  
- Verify existence of new lvm volume group that was just added.
```
  sudo vgs
  
  VG                        #PV #LV #SN Attr   VSize  VFree
  cinder-cb-volumes           1   1   0 wz--n- 10.00g  9.00g
  stack-volumes-default       1   0   0 wz--n- 10.01g 10.01g
  stack-volumes-lvmdriver-1   1   1   0 wz--n- 10.01g  9.01g
```

- Register a new LVM backend in **cinder.conf** and
- Add the newly created volume-group to this new LVM backend
  - e.g. below edit 
    - registers a new backend called 'cloudbyte-lvm'
    - adds 'cinder-cb-volumes' as the volume group
```
  sudo vi /etc/cinder/cinder.conf
  
  [DEFAULT]
  default_volume_type = lvmdriver-1,cb-lvm
  enabled_backends = lvmdriver-1, cloudbyte-lvm
  
  [cloudbyte-lvm]
  lvm_type = default
  iscsi_helper = tgtadm
  volume_group = cinder-cb-volumes
  volume_driver = cinder.volume.drivers.lvm.LVMVolumeDriver
  volume_backend_name = cloudbyte-lvm
```

- Create a new volume type for the backend that was newly created
```
  cinder type-create cb-lvm
  cinder type-key cb-lvm set volume_backend_name cloudbyte-lvm
```

- Restart the cinder-services
```
```

- Verify the volume types & specs associated with them
```
    cinder extra-specs-list
  +--------------------------------------+-------------+--------------------------------------------+
  |                  ID                  |     Name    |                extra_specs                 |
  +--------------------------------------+-------------+--------------------------------------------+
  | 7011905b-1427-4205-8075-3996c8fcefe6 | lvmdriver-1 |  {u'volume_backend_name': u'lvmdriver-1'}  |
  | b19f5d36-032c-4e77-a498-875cebfa325a |    cb-lvm   | {u'volume_backend_name': u'cloudbyte-lvm'} |
  +--------------------------------------+-------------+--------------------------------------------+
```

  
