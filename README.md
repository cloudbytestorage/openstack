## OpenStack Cinder CloudByte driver code base

Information related to CloudByte openstack cinder driver

### test matrix
```
  OS             ELASTICENTER      TEMPEST     QA      RALLY    CI    UT
  ----           ------------      -------     ---     -----    ---   ---
  MASTER         1.4.0.547         YES                          YES   YES
  KILO 1.2.7     1.4.0.620         YES                                YES
  KILO 1.2.8     1.4.0.620                                         
  
```


### running tempest
```
tox -eall -- volume --concurrency=1
tox -eall -- <tempest-test> --concurrency=1
```

### code contribution 
```
email: openstack-dev@cloudbyte.com
```

### support
```
email: cb-support@cloudbyte.com
```
