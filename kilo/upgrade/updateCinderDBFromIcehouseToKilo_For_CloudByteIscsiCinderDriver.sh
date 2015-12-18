#!/bin/bash
set -e
echo -n "Enter Mysql Password > "
read pwd
echo "Started updating cinder database"
echo "Logging as root"
mysql -uroot -p$pwd cinder < "updateCinderDBFromIcehouseToKilo_For_CloudByteIscsiCinderDriver.sql"
echo "Updated database cinder successfully"

