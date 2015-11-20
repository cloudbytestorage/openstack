### Observation :

[root@fuel ~]# ssh -i cloud.key ubuntu@20.10.87.53

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that the RSA host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
ff:aa:5e:3b:76:51:1f:7d:21:74:64:3b:5b:d8:e9.
Please contact your system administrator.
Add correct host key in /root/.ssh/known_hosts to get rid of this message.
Offending key in /root/.ssh/known_hosts:9
RSA host key for 20.10.87.53 has changed and you have requested strict checking.
Host key verification failed.


### Solution :

[root@fuel ~]# vim /root/.ssh/known_hosts

Delete the 9th line from this file, save 7 exit.

[root@fuel ~]# ssh -i cloud.key ubuntu@20.10.87.53
The authenticity of host '20.10.87.53 (20.10.87.53)' can't be established.
RSA key fingerprint is ff:aa:5e:3b:76:51:1f:7d:21:74:64:3b:5b:d8:e9.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '20.10.87.53' (RSA) to the list of known hosts.
Welcome to Ubuntu 14.04.1 LTS (GNU/Linux 3.13.0-40-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  System information as of Thu Mar 19 09:03:04 UTC 2015

| Property        | Output          |
| :------:        | :-----:         |
| System load     | 0.0             |
| Memory usage    | 2%  	          |
| Processes       | 52              |
| Usage of        | 56.1% of 1.32GB |
| Swap usage      | 0%  					  |
| Users logged in | 0               |

  Graph this data and manage this system at:
  
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
  
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.

0 updates are security updates.

The programs included with the Ubuntu system are free software; the exact distribution terms for each program are described in the individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.
