echo -n "Enter Mysql Password > "
stty -echo
read pwd
stty echo
echo "Started updating ElastiCenter database"
echo "Logging as root"
mysql -uroot -p$pwd cloud < "updateP3ElastiCenterDB_ToWorkWithKilo_CloudByteIscsiCinderDriver.sql"
if [ "$?" = "0" ]; then
	echo "Updated ElastiCenter database successfully"
else
	echo "Failed to Updated ElastiCenter database"
fi
