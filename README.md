## OpenStack Cinder CloudByte driver code base

Information related to CloudByte openstack cinder driver

### test matrix
```
  KILO      ELASTICENTER      TEMPEST     QA      RALLY
  ----      ------------      -------     ---     -----
  1.2.6     1.4.0.620         YES       
  
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
