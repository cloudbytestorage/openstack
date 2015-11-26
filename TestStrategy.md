
### Positive Test Scenarios
- check the cinder-volume logs for the start timestamp (st)
- create volume @ openstack (os) -> verify @ os & elasticenter (ec)
- delete volume @ os -> verify @ os & ec
- create volume @ os -> create snapshot @ os -> verify @ os & ec
- delete snapshot @ os -> delete volume @ os ->  verify @ os & ec
- create volume @ os -> create snapshot @ os -> create clone @ os -> verify @ os & ec
- delete clone @ os -> delete snapshot @ os -> delete volume @ os -> verify @ os & ec
- create clone from volume @ os -> verify @ os & ec
- delete clone from volume @ os -> verify @ os & ec
  - check if a snapshot remains @ ec <b> IMPORTANT </b>
- create volume with chap @ os -> verify @ os & es & run command (rc)
- create volume with initiator group (ig) @ os -> verify @ os & ec & rc
- extend volume @ os -> verify @ os & ec & rc
  - increase size
  - decrease size
- extend clone @ os -> verify @ os & ec & rc
  - increase size
  - decrease size
- increase volume IOPS @ os -> verify @ os & ec
- decrease volume IOPS @ os -> verify @ os & ec
- increase volume latency @ os -> verify @ os & ec
  - this feature is supported @ os but not @ ec
- decrease volume latency @ os -> verify @ os & ec
  - this feature is supported @ os but not @ ec
- enable grace allowed @ os -> verify @ ec & rc
- disable grace allowed @ os -> verify @ ec & rc
- enable compression @ os -> verify @ ec & rc
- disable compression @ os -> verify @ ec & rc
- enable sync @ os -> verify @ ec & rc
- modify noofcopies @ os -> verify @ ec & rc
- enable readonly @ os -> verify @ ec & rc
- disable readonly @ os -> verify @ ec & rc
- check the scheduler logs 
  - verify if the backends available capacity matches the corresponding VSMs'.
  - check if there is a suitable rc or cli
- check the logs for any errors or warnings after the st
  

### Positive Collection Based Test Scenarios
- 

### Negative Test Scenarios
- shutdown the EC network & verify os, logs
- shutdown EC & verify os, logs
- create volume @ os -> delete from ec -> update IOPS @ os
- create volume @ os -> delete from ec -> delete from os @ verify os logs
- create snapshot @ os -> delete from ec -> delete from os & verify os logs
- create snapshot @ os -> delete from ec -> create clone from os & verify os logs
- create snapshot @ os -> create clone @ os -> delete clone @ ec -> delete clone @ os & verify os logs
- create snapshot @ os -> create clone @ os -> delete clone & snapshot @ ec -> delete clone @ os & verify os logs
- delete VSM @ ec -> verify logs @ os
- delete VSM @ ec -> create volume @ os
- delete VSM @ ec -> delete volume @ os
- delete VSM @ ec -> create snapshot @ os
- delete VSM @ ec -> delete snapshot @ os
- delete VSM @ ec -> create clone @ os
- delete VSM @ ec -> delete clone @ os
