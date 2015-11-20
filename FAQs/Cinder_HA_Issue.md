### Observation :

* Check for host property in /etc/cinder/cinder.conf

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image4.jpg)

* Check the host column in volumes table in cinder database

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image5.jpg)


### Solution :

Above screenshot typically imply, host property was set to FQDN of the cinder node. This has got issues in the current HA implementation in cinder.

Uncomment the "host=cinder" in "/etc/cinder/cinder.conf".

Update the volumes records host column to cinder irrespective of the host in which the volume was created.
