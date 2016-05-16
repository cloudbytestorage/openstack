### OpenStack installation and configuring CloudByte storage as the cinder driver

- To try/test OpenStack against CloudByte storage;
  - one can start with the easy way i.e. using "devstack all in one" setup. 

- Devstack requirements:
```
  OS : Ubuntu 14.04
  MEMORY : 4GB(minimum)(Recommended to use 8GB)
  VCPUS : 6(or more)
  HARD DISK : 60-80GB
```

- Once the system installation and setup is done
- We need to download the devstack and install it. 
```
  >> git clone https://git.openstack.org/openstack-dev/devstack

  NOTE :  After downloading devstack go inside the devstack folder and
          check the version of OpenStack

  >> git status
  OUTPUT :
        On branch master
        Your branch is up-to-date with 'origin/master'.

        nothing to commit, working directory clean

  NOTE : To switch to some specific version run command:

  >> git checkout stable/<STABLE_BRANCH_NAME>
```

- Create a file "local.conf" and paste the following content
  - required for devstack installation
```
  [[local|localrc]]
  ADMIN_PASSWORD=test123
  MYSQL_PASSWORD=test123
  RABBIT_PASSWORD=test123
  SERVICE_PASSWORD=test123
  SERVICE_TOKEN=password
  SCREEN_LOGDIR=/opt/stack/logs/screen
  LOGFILE=/opt/stack/logs/stack.sh.log
  VERBOSE=True
  SYSLOG=True
  SERVICE_TIMEOUT=60
  API_RATE_LIMIT=False
  ENABLED_SERVICES=c-api,c-sch,c-vol,g-api,g-reg,horizon,key,mysql,n-api,n-cond,n-cpu,n-crt,n-obj,n-sch,nova,rabbit,tempest,n-novnc,n-xvnc,n-cauth,n-net
```

- Start installation by running below command:
```
  ./stack.sh
```

- Installation takes some time, and once installation is complete
  - configure CloudByte cinder driver.
- Edit following file:
```
  /etc/cinder/cinder.conf
```

- Add the following entries:
```
  [DEFAULT]
  default_volume_type = gold, silver
  enabled_backends = cb-gold, cb-silver
  
  [cb-gold]
  volume_driver = cinder.volume.drivers.cloudbyte.cloudbyte.CloudByteISCSIDriver
  volume_backend_name = cb-gold
  san_ip = <ELASTICENETER_IP>
  san_login = admin
  san_password = na
  cb_tsm_name = <VSM_NAME>
  cb_account_name = <ACC_NAME>
  cb_apikey = <ELASTICENETER_APIKEY>
  cb_confirm_volume_create_retries = 15
  cb_confirm_volume_create_retry_interval = 5
  cb_confirm_volume_delete_retries = 15
  cb_confirm_volume_delete_retry_interval = 5
  cb_add_qosgroup = latency:15,graceallowed:true,iopscontrol:true,memlimit:0,tpcontrol:false,throughput:0,iops:20,networkspeed:0
  cb_create_volume = compression:off,deduplication:off,blocklength:512B,sync:always,protocoltype:ISCSI,recordsize:4k

  [cb-silver]
  volume_driver = cinder.volume.drivers.cloudbyte.cloudbyte.CloudByteISCSIDriver
  volume_backend_name = cb-silver
  san_ip = <ELASTICENETER_IP>
  san_login = admin
  san_password = na
  cb_tsm_name = <VSM_NAME>
  cb_account_name = <ACC_NAME>
  cb_apikey = <ELASTICENETER_APIKEY>
  cb_confirm_volume_create_retries = 15
  cb_confirm_volume_create_retry_interval = 5
  cb_confirm_volume_delete_retries = 15
  cb_confirm_volume_delete_retry_interval = 5
  cb_add_qosgroup = latency:15,graceallowed:true,iopscontrol:true,memlimit:0,tpcontrol:false,throughput:0,iops:20,networkspeed:0
  cb_create_volume = compression:off,deduplication:off,blocklength:512B,sync:always,protocoltype:ISCSI,recordsize:4k
```

- NOTE : "enabled_backends" property contains the backend name pointing to VSMs (Virtual Storage Machines) of ElastiCenter. 
  - Its value can be more than one.
  - In other words it can point to one or more VSMs.
- NOTE :  "default_volume_type" property contains the volume types
  - Volume type are registered against a backend.
  - There can be more than one volume types, each corresponding to a backend.

- Create the volume type and assign them to backend
```
  NOTE : Run below command (per session)
  >> cd < devstack folder >
  >> source openrc admin admin
  
  >> cinder type-create <VOLUME_TYPE_NAME>
  >> cinder type-key <VOLUME_TYPE_NAME> set volume_backend_name <ENABLED_BACKEND_NAME>
```

- You can also associate QOS properties against the volume type
```
  >> cinder type-key <VOLUME_TYPE_NAME> set qos:iops=<VALUE> qos:graceallowed=<true/false>;
```

### Running tempest test suite on CloudByte cinder driver

- OpenStack contains a test suite name "tempest" which runs a bunch of test against any cinder driver.
- In order to run the tempest test suite on CloudByte cinder driver, we need to do some configuration to the file:
```
  FILE:
  >> vi /opt/stack/tempest/etc/tempest.conf
  
  CHANGES TO BE ADDED:
    [volume]
    storage_protocol = iSCSI
    vendor_name = CloudByte
    ATTACH_ENCRYPTED_VOLUME_AVAILABLE = False
    backend_names = <BACKEND_NAME1>, <BACKEND_NAME2> #For running temepst tests against multiple backend
    
    [volume-feature-enabled]
    multi_backend = True #For enabling temepst tests against multiple backend
```

- Run following command to run tempest test suite:
```
  >> tox -eall -- volume --concurrency=1
```

### Test matrix
```
  OS             ELASTICENTER      TEMPEST     QA      RALLY    CI    UT
  ----           ------------      -------     ---     -----    ---   ---
  MASTER         1.4.0.547         YES                          YES   YES
  KILO 1.2.7     1.4.0.620         YES                                YES
  KILO 1.2.8     1.4.0.620         YES                                YES
  LIBERTY        1.3.0.815
                 1.3.0.754
```

### Code contribution
```
email: openstack-dev@cloudbyte.com
```

### Support related queries
```
email: cb-support@cloudbyte.com
```
