
### Positive Test Scenarios
- check the cinder-volume logs for the start timestamp (st)
- create volume @ openstack (os) & verify @ os & elasticenter (ec)
- delete volume @ os & verify @ os & ec
- create volume & snapshot @ os & verify @ os & ec
- delete snapshot & volume @ os & verify @ os & ec
- create volume & snapshot & clone @ os & verify @ os & ec
- delete clone, snapshot & volume @ os & verify @ os & ec
- create clone from volume @ os & verify @ os & ec
- delete clone from volume @ os & verify @ os & ec
  - check if a snapshot remains @ ec <b> IMPORTANT </b>
- create volume with chap @ os & verify @ os & es & run command (rc)
- create volume with initiator group (ig) @ os & verify @ os & ec & rc
- extend volume @ os & verify @ os & ec & rc
  - increase size
  - decrease size
- extend clone @ os & verify @ os & ec & rc
- check the logs for any errors or wranings after the st
  

### Positive Collection Based Test Scenarios
- 

### Negative Test Scenarios
- 
