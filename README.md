## OpenStack installation and configuration against CloudByte Cinder driver

- For testing OpenStack against the ElastiCenter build, it is recommended to use "devstack all in one" setup. 
- For setting up devstack following configuration are required:
```
  OS : Ubuntu 14.04
  MEMORY : 4GB(minimum)(Recommended to use 8GB)
  VCPUS : 6(or more)
  HARD DISK : 60-80GB
```
- Once the system insatllation and setup is done we need to download the devstack and install it. 
- For downloading devstack use the link below:
```
  git clone https://git.openstack.org/openstack-dev/devstack
```
- After downloading devstack go inside the devstack folder and check the version of OpenStack using(By default the branch version will be master):
```
  COMMAND : git status
  OUTPUT :
        On branch master
        Your branch is up-to-date with 'origin/master'.

        nothing to commit, working directory clean
```
- To switch to some specific version run command:
```
  COMMAND : git checkout stable/<STABLE_BRANCH_NAME>
```
- Now we need to create a file "local.conf" and put the following content in it(Required for DevStack installation):
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
- Now start the installation using:
```
  ./stack.sh
```
- The installation takes some time, and after it is done we need to configure our CloudByte Cinder driver.
- To do so we need to edit the following file:
```
  /etc/cinder/cinder.conf
```
- Now we need to add the following entry in [DEFAULT] section and also our backends(Pointing to the VSMs of our ElastiCenter):
```
  [DEFAULT]
  default_volume_type = gold,silver
  enabled_backends = cb-gold,cb-silver
  
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
- The "enabled_backends" variable contains the backend name specificaly pointing to the VSMs in ElastiCenter. Its value can be more than one depending on your choice and they can point to one or more VSMs.
- Also the "default_volume_type" variable contains the volume types pointing to the backends mentioned above. You can have more than one volume type pointing to one or more backends.
- To create the volume type and assigning them to one of the backend use:
```
  NOTE: TO RUN THE BELOW COMMAND GOTO DEVSTACK FOLDER AND RUN 
        - source openrc admin admin
      : NEED TO RUN IT JUST ONCE FOR YOUR SESSION.
  COMMANDS:
    cinder type-create <VOLUME_TYPE_NAME>; (CREATING)
    cinder type-key <VOLUME_TYPE_NAME> set volume_backend_name <ENABLED_BACKEND_NAME>; (ASSIGNING)
```
- You can also associate some qos properties to the volume type, which can be used during volume creation:
```
  COMMAND:
    cinder type-key <VOLUME_TYPE_NAME> set qos:iops=<VALUE> qos:graceallowed<true/false>;
```

## Running Tempest test suite on CloudByte Cinder driver

- OpenStack contains a test suite name "tempest" which runs a bunch of test against any cinder driver.
- In order to run the tempest test suite on our CloudByte Cinder Driver, we need to do some configuration to the file:
```
  FILE:
    /opt/stack/tempest/etc/tempest.conf
  
  CHANGES TO BE ADDED:
    [volume]
    storage_protocol = iSCSI
    vendor_name = CloudByte
    ATTACH_ENCRYPTED_VOLUME_AVAILABLE = False
    backend_names = <BACKEND_NAME1>,<BACKEND_NAME2> #For running temepst tests against multiple backend
    
    [volume-feature-enabled]
    multi_backend = True #For enabling temepst tests against multiple backend
```
- Now use the following command to run tempest test suite:
```
  COMMAND:
    tox -eall -- <tempest-test> --concurrency=1
  
  Since we are testing the cinder so use:
    tox -eall -- volume --concurrency=1
```

### test matrix
```
  OS             ELASTICENTER      TEMPEST     QA      RALLY    CI    UT
  ----           ------------      -------     ---     -----    ---   ---
  MASTER         1.4.0.547         YES                          YES   YES
  KILO 1.2.7     1.4.0.620         YES                                YES
  KILO 1.2.8     1.4.0.620         YES                                YES
  LIBERTY        1.3.0.815
                 1.3.0.754
```

### code contribution 
```
email: openstack-dev@cloudbyte.com
```

### support
```
email: cb-support@cloudbyte.com
```
