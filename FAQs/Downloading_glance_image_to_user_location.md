### Solution :

* glance image-list

* glance image-download your_image_id_here > your_image_name.your_image_format

example

glance image-download 5dde2692-e20c-4c16-a5ff-e9478e14114c > cirros_32bit.qcow2


### Alternatively :

root@icehouse:~# mysql -uroot -ptest123

Welcome to the MySQL monitor.  Commands end with ; or \g.

Your MySQL connection id is 794

Server version: 5.5.43-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use glance;

Reading table information for completion of table and column names

You can turn off this feature to get a quicker startup with -A

Database changed

mysql> select value from image_locations where image_id="99d42a41-2288-4e32-85c0-c81e36404012";

| value                                                                     |

| file:///opt/stack/data/glance/images/99d42a41-2288-4e32-85c0-c81e36404012 |


1 row in set (0.00 sec)

