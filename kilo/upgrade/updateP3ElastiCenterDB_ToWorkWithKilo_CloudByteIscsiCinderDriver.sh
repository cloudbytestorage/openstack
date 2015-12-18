set -e
echo -n "Enter Mysql Password > "
stty -echo
read pwd
stty echo
echo "Started updating ElastiCenter database"
echo "Logging as root"
mysql -uroot -p$pwd cloud < "updateP3ElastiCenterDB_ToWorkWithKilo_CloudByteIscsiCinderDriver.sql"
echo "Updated ElastiCenter database successfully"

