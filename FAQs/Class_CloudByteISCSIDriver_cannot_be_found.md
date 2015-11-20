### Cinder Volume Logs :

2015-03-12 20:48:01.499 105289 CRITICAL cinder [-] ImportError: Class CloudByteISCSIDriver cannot be found (['Traceback (most recent call last):\n', '  File "/usr/lib/python2.7/dist-packages/cinder/openstack/common/importutils.py", line 29, in import_class\n    return getattr(sys.modules[mod_str], class_str)\n', "AttributeError: 'module' object has no attribute 'CloudByteISCSIDriver'\n"])

2015-03-12 20:48:01.499 105289 TRACE cinder Traceback (most recent call last):

2015-03-12 20:48:01.499 105289 TRACE cinder   File "/usr/bin/cinder-volume", line 70, in <module>

2015-03-12 20:48:01.499 105289 TRACE cinder     service_name=backend)

2015-03-12 20:48:01.499 105289 TRACE cinder   File "/usr/lib/python2.7/dist-packages/cinder/service.py", line 202, in create

2015-03-12 20:48:01.499 105289 TRACE cinder     service_name=service_name)

2015-03-12 20:48:01.499 105289 TRACE cinder   File "/usr/lib/python2.7/dist-packages/cinder/service.py", line 90, in __init__

2015-03-12 20:48:01.499 105289 TRACE cinder     *args, **kwargs)

2015-03-12 20:48:01.499 105289 TRACE cinder   File "/usr/lib/python2.7/dist-packages/cinder/volume/manager.py", line 208, in __init__

2015-03-12 20:48:01.499 105289 TRACE cinder     host=self.host)

2015-03-12 20:48:01.499 105289 TRACE cinder   File "/usr/lib/python2.7/dist-packages/cinder/openstack/common/importutils.py", line 38, in import_object

2015-03-12 20:48:01.499 105289 TRACE cinder     return import_class(import_str)(*args, **kwargs)

2015-03-12 20:48:01.499 105289 TRACE cinder   File "/usr/lib/python2.7/dist-packages/cinder/openstack/common/importutils.py", line 33, in import_class

2015-03-12 20:48:01.499 105289 TRACE cinder     traceback.format_exception(*sys.exc_info())))

2015-03-12 20:48:01.499 105289 TRACE cinder ImportError: Class CloudByteISCSIDriver cannot be found (['Traceback (most recent call last):\n', '  File "/usr/lib/python2.7/dist-packages/cinder/openstack/common/importutils.py", line 29, in import_class\n    return getattr(sys.modules[mod_str], class_str)\n', "AttributeError: 'module' object has no attribute 'CloudByteISCSIDriver'\n"])


### Observation :

![alt text](https://github.com/CloudByteStorages/openstack/blob/master/FAQs/images/image1.jpg)


### Solution :

Python was not able to find appropriate class due to the presence of a folder and a file of same name i.e. cloudbyte. Renamed the folder from cloudbyte to something else was the solution.

