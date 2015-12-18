#### MYSQL QUERIES FOR SYNCING ICEHOUSE CREATED VOLUMES TO KILO:

Following are the queries that need to be run after the upgarde of OpenStack nodes from Icehouse to Kilo:

- UPDATE volumes INNER JOIN volume_metadata ON (volumes.id = volume_metadata.volume_id and volume_metadata.key = "cb_volume_id" and volume_metadata.deleted = 0) SET volumes.provider_id = volume_metadata.value;

- UPDATE snapshots INNER JOIN volume_metadata ON (snapshots.volume_id = volume_metadata.volume_id and SUBSTRING(volume_metadata.key,18) = snapshots.id and volume_metadata.deleted = 0) SET snapshots.provider_id = volume_metadata.value;
