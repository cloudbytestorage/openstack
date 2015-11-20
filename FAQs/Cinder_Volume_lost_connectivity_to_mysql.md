### Observation :

@/etc/cinder/cinder.conf
…
[database]
idle_timeout=3600
max_pool_size=10
max_retries=-1
max_overflow=30
connection=mysql:///cinder:FCv56ZEZ@198.18.16.2/cinder?charset=utf8&read_timeout=60
…

ping to 198.18.16.2 worked fine.


### Solution :

There were three slashes ‘///’. Removed the extra / present in the connection.
Below is the correct value for connection.
connection=mysql://cinder:FCv56ZEZ@198.18.16.2/cinder?charset=utf8&read_timeout=60
