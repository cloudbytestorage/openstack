### Steps to follow :

1. nova-manage floating create --pool POOL_NAME --ip_range

2. Now go to openstack horizon and do the following:
- Go to Access & Security -> Floating IPs -> Allocate IP to Project

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image6.jpg)

- Now select the pool you created and allocate the IP.

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image7.jpg)

- Now go the the IP and associate it with the Instance you wanted.

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image8.jpg)

