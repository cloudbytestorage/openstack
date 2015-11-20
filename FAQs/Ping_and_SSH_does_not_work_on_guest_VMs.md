### Solution :

You need to enable ping and ssh on your VMs for network access. This can be done with either the nova or euca2ools commands.


### Steps to follow :

Run these commands as root only if the credentials used to interact with nova-api are in /root/.bashrc. If the EC2 credentials in the .bashrc file are for an unprivileged user, you must run these commands as that user instead.

Enable ping and SSH with nova commands:

$ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
$ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0           

Enable ping and SSH with euca2ools:

$ euca-authorize -P icmp -t -1:-1 -s 0.0.0.0/0 default
$ euca-authorize -P tcp -p 22 -s 0.0.0.0/0 default         

If you have run these commands and still cannot ping or SSH your instances, check the number of running dnsmasq processes, there should be two. If not, kill the processes and restart the service with these commands: command:

- killall dnsmasq
- service nova-network restart

Enable RDP for the above things to work:

- Go to Access & Security and select  Security Groups
- In the Security Groups section select default group’s Manage Rules

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image2.jpg)

- In Manage rules add a new rule as follows and save it

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image3.jpg)

