# Comparing `tmp/hmd_cli_neuronsphere-0.1.98-py3-none-any.whl.zip` & `tmp/hmd_cli_neuronsphere-0.1.99-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,44 +1,88 @@
-Zip file size: 33318 bytes, number of entries: 42
--rw-rw-rw-  2.0 unx        0 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/__init__.py
--rw-rw-rw-  2.0 unx     2093 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/controller.py
--rw-rw-rw-  2.0 unx    12894 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/hmd_cli_neuronsphere.py
--rw-r--r--  2.0 unx     2014 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.airflow.yml
--rw-r--r--  2.0 unx     3248 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.apache-superset.yml
--rw-r--r--  2.0 unx     1237 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.datadog.yml
--rw-r--r--  2.0 unx      340 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.dynamodb.yml
--rw-r--r--  2.0 unx     1305 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.jupyter.yml
--rw-r--r--  2.0 unx      974 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.main.yml
--rw-r--r--  2.0 unx     2196 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.transform.yml
--rw-r--r--  2.0 unx     2975 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/docker-compose.trino.yml
--rw-r--r--  2.0 unx     1885 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/hadoop-hive.env
--rw-r--r--  2.0 unx      494 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/hive/core-site.xml
--rw-r--r--  2.0 unx     1972 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/hive/metastore-log4j2.properties
--rw-r--r--  2.0 unx     1201 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/hive/metastore-site.xml
--rwxr-xr-x  2.0 unx     2342 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/postgres/docker-entrypoint.sh
--rwxr-xr-x  2.0 unx      391 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/postgres/always-initdb.d/airflow.sh
--rwxr-xr-x  2.0 unx      401 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/postgres/always-initdb.d/hmd_ms_deployment.sh
--rwxr-xr-x  2.0 unx      400 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/postgres/always-initdb.d/hmd_ms_transform.sh
--rwxr-xr-x  2.0 unx      393 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/postgres/always-initdb.d/metastore.sh
--rwxr-xr-x  2.0 unx      392 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/postgres/always-initdb.d/superset.sh
--rw-r--r--  2.0 unx     1553 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/.env-non-dev
--rwxr-xr-x  2.0 unx     2059 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/docker-bootstrap.sh
--rwxr-xr-x  2.0 unx     1213 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/docker-ci.sh
--rwxr-xr-x  2.0 unx     1202 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/docker-entrypoint.sh
--rwxr-xr-x  2.0 unx     1136 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/docker-frontend.sh
--rwxr-xr-x  2.0 unx     2640 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/docker-init.sh
--rwxr-xr-x  2.0 unx     1738 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/frontend-mem-nag.sh
--rw-r--r--  2.0 unx       23 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/requirements-local.txt
--rw-r--r--  2.0 unx     4022 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/pythonpath_dev/superset_config.py
--rw-r--r--  2.0 unx     1204 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/superset/pythonpath_dev/superset_config_local.example
--rwxr-xr-x  2.0 unx      170 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/config.properties
--rwxr-xr-x  2.0 unx      171 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/jvm.config
--rwxr-xr-x  2.0 unx       14 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/log.properties
--rwxr-xr-x  2.0 unx       96 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/node.properties
--rwxr-xr-x  2.0 unx      171 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/catalog/hive.properties
--rwxr-xr-x  2.0 unx       94 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/catalog/iceberg.properties
--rwxr-xr-x  2.0 unx       20 b- defN 23-Mar-01 17:22 hmd_cli_neuronsphere/services/trino/config/catalog/tpch.properties
--rw-rw-rw-  2.0 unx     3658 b- defN 23-Mar-01 17:23 hmd_cli_neuronsphere-0.1.98.dist-info/METADATA
--rw-rw-rw-  2.0 unx       92 b- defN 23-Mar-01 17:23 hmd_cli_neuronsphere-0.1.98.dist-info/WHEEL
--rw-rw-rw-  2.0 unx       21 b- defN 23-Mar-01 17:23 hmd_cli_neuronsphere-0.1.98.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     4707 b- defN 23-Mar-01 17:23 hmd_cli_neuronsphere-0.1.98.dist-info/RECORD
-42 files, 65151 bytes uncompressed, 25316 bytes compressed:  61.1%
+Zip file size: 140185 bytes, number of entries: 86
+-rw-rw-rw-  2.0 unx        0 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/__init__.py
+-rw-rw-rw-  2.0 unx     2093 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/controller.py
+-rw-rw-rw-  2.0 unx    13526 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/hmd_cli_neuronsphere.py
+-rw-r--r--  2.0 unx     2014 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.airflow.yml
+-rw-r--r--  2.0 unx     3248 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.apache-superset.yml
+-rw-r--r--  2.0 unx     1237 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.datadog.yml
+-rw-r--r--  2.0 unx      340 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.dynamodb.yml
+-rw-r--r--  2.0 unx     1305 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.jupyter.yml
+-rw-r--r--  2.0 unx      974 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.main.yml
+-rw-r--r--  2.0 unx     2196 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.transform.yml
+-rw-r--r--  2.0 unx     3178 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/docker-compose.trino.yml
+-rw-r--r--  2.0 unx     2191 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop-hive.env
+-rw-r--r--  2.0 unx     4436 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/capacity-scheduler.xml
+-rw-r--r--  2.0 unx     1335 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/configuration.xsl
+-rw-r--r--  2.0 unx      318 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/container-executor.cfg
+-rw-r--r--  2.0 unx     1094 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/core-site.xml
+-rw-r--r--  2.0 unx     3670 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/hadoop-env.cmd
+-rw-r--r--  2.0 unx     4224 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/hadoop-env.sh
+-rw-r--r--  2.0 unx     2490 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/hadoop-metrics.properties
+-rw-r--r--  2.0 unx     2598 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/hadoop-metrics2.properties
+-rw-r--r--  2.0 unx     9683 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/hadoop-policy.xml
+-rw-r--r--  2.0 unx     2385 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/hdfs-site.xml
+-rw-r--r--  2.0 unx     1449 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/httpfs-env.sh
+-rw-r--r--  2.0 unx     1657 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/httpfs-log4j.properties
+-rw-r--r--  2.0 unx       21 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/httpfs-signature.secret
+-rw-r--r--  2.0 unx      620 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/httpfs-site.xml
+-rw-r--r--  2.0 unx     3518 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/kms-acls.xml
+-rw-r--r--  2.0 unx     1527 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/kms-env.sh
+-rw-r--r--  2.0 unx     1631 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/kms-log4j.properties
+-rw-r--r--  2.0 unx     5540 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/kms-site.xml
+-rw-r--r--  2.0 unx    11237 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/log4j.properties
+-rw-r--r--  2.0 unx      951 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/mapred-env.cmd
+-rw-r--r--  2.0 unx     1383 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/mapred-env.sh
+-rw-r--r--  2.0 unx     4113 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/mapred-queues.xml.template
+-rw-r--r--  2.0 unx      841 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/mapred-site.xml
+-rw-r--r--  2.0 unx      758 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/mapred-site.xml.template
+-rw-r--r--  2.0 unx       10 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/slaves
+-rw-r--r--  2.0 unx     2316 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/ssl-client.xml.example
+-rw-r--r--  2.0 unx     2697 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/ssl-server.xml.example
+-rw-r--r--  2.0 unx     2250 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/yarn-env.cmd
+-rw-r--r--  2.0 unx     4567 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/yarn-env.sh
+-rw-r--r--  2.0 unx     2481 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hadoop/yarn-site.xml
+-rw-r--r--  2.0 unx     1596 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/beeline-log4j2.properties
+-rw-r--r--  2.0 unx     1596 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/beeline-log4j2.properties.template
+-rw-r--r--  2.0 unx   257573 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-default.xml.template
+-rw-r--r--  2.0 unx     2378 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-env.sh
+-rw-r--r--  2.0 unx     2365 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-env.sh.template
+-rw-r--r--  2.0 unx     2287 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-exec-log4j2.properties
+-rw-r--r--  2.0 unx     2274 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-exec-log4j2.properties.template
+-rw-r--r--  2.0 unx     2758 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-log4j2.properties
+-rw-r--r--  2.0 unx     2925 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-log4j2.properties.template
+-rw-r--r--  2.0 unx     2246 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/hive-site.xml
+-rw-r--r--  2.0 unx     2049 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/ivysettings.xml
+-rw-r--r--  2.0 unx     2719 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/llap-cli-log4j2.properties.template
+-rw-r--r--  2.0 unx     3885 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/llap-daemon-log4j2.properties
+-rw-r--r--  2.0 unx     7041 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/llap-daemon-log4j2.properties.template
+-rw-r--r--  2.0 unx     1972 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/metastore-log4j2.properties
+-rw-r--r--  2.0 unx     2126 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/metastore-site.xml
+-rw-r--r--  2.0 unx     2662 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/hive/parquet-logging.properties
+-rwxr-xr-x  2.0 unx     2342 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/postgres/docker-entrypoint.sh
+-rwxr-xr-x  2.0 unx      391 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/postgres/always-initdb.d/airflow.sh
+-rwxr-xr-x  2.0 unx      401 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/postgres/always-initdb.d/hmd_ms_deployment.sh
+-rwxr-xr-x  2.0 unx      400 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/postgres/always-initdb.d/hmd_ms_transform.sh
+-rwxr-xr-x  2.0 unx      393 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/postgres/always-initdb.d/metastore.sh
+-rwxr-xr-x  2.0 unx      392 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/postgres/always-initdb.d/superset.sh
+-rw-r--r--  2.0 unx     1553 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/.env-non-dev
+-rwxr-xr-x  2.0 unx     2059 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/docker-bootstrap.sh
+-rwxr-xr-x  2.0 unx     1213 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/docker-ci.sh
+-rwxr-xr-x  2.0 unx     1202 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/docker-entrypoint.sh
+-rwxr-xr-x  2.0 unx     1136 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/docker-frontend.sh
+-rwxr-xr-x  2.0 unx     2640 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/docker-init.sh
+-rwxr-xr-x  2.0 unx     1738 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/frontend-mem-nag.sh
+-rw-r--r--  2.0 unx       23 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/requirements-local.txt
+-rw-r--r--  2.0 unx     4022 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/pythonpath_dev/superset_config.py
+-rw-r--r--  2.0 unx     1204 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/superset/pythonpath_dev/superset_config_local.example
+-rwxr-xr-x  2.0 unx      170 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/config.properties
+-rwxr-xr-x  2.0 unx      171 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/jvm.config
+-rwxr-xr-x  2.0 unx       14 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/log.properties
+-rwxr-xr-x  2.0 unx       96 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/node.properties
+-rwxr-xr-x  2.0 unx      163 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/catalog/hive.properties
+-rwxr-xr-x  2.0 unx       94 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/catalog/iceberg.properties
+-rwxr-xr-x  2.0 unx       20 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere/services/trino/config/catalog/tpch.properties
+-rw-rw-rw-  2.0 unx     3658 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere-0.1.99.dist-info/METADATA
+-rw-rw-rw-  2.0 unx       92 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere-0.1.99.dist-info/WHEEL
+-rw-rw-rw-  2.0 unx       21 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere-0.1.99.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     9688 b- defN 23-Mar-06 15:48 hmd_cli_neuronsphere-0.1.99.dist-info/RECORD
+86 files, 449850 bytes uncompressed, 123883 bytes compressed:  72.5%
```

## zipnote {}

```diff
@@ -30,23 +30,155 @@
 
 Filename: hmd_cli_neuronsphere/services/docker-compose.trino.yml
 Comment: 
 
 Filename: hmd_cli_neuronsphere/services/hadoop-hive.env
 Comment: 
 
-Filename: hmd_cli_neuronsphere/services/hive/core-site.xml
+Filename: hmd_cli_neuronsphere/services/hadoop/capacity-scheduler.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/configuration.xsl
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/container-executor.cfg
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/core-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/hadoop-env.cmd
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/hadoop-env.sh
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/hadoop-metrics.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/hadoop-metrics2.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/hadoop-policy.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/hdfs-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/httpfs-env.sh
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/httpfs-log4j.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/httpfs-signature.secret
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/httpfs-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/kms-acls.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/kms-env.sh
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/kms-log4j.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/kms-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/log4j.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/mapred-env.cmd
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/mapred-env.sh
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/mapred-queues.xml.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/mapred-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/mapred-site.xml.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/slaves
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/ssl-client.xml.example
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/ssl-server.xml.example
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/yarn-env.cmd
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/yarn-env.sh
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hadoop/yarn-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/beeline-log4j2.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/beeline-log4j2.properties.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-default.xml.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-env.sh
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-env.sh.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-exec-log4j2.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-exec-log4j2.properties.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-log4j2.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-log4j2.properties.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/hive-site.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/ivysettings.xml
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/llap-cli-log4j2.properties.template
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/llap-daemon-log4j2.properties
+Comment: 
+
+Filename: hmd_cli_neuronsphere/services/hive/llap-daemon-log4j2.properties.template
 Comment: 
 
 Filename: hmd_cli_neuronsphere/services/hive/metastore-log4j2.properties
 Comment: 
 
 Filename: hmd_cli_neuronsphere/services/hive/metastore-site.xml
 Comment: 
 
+Filename: hmd_cli_neuronsphere/services/hive/parquet-logging.properties
+Comment: 
+
 Filename: hmd_cli_neuronsphere/services/postgres/docker-entrypoint.sh
 Comment: 
 
 Filename: hmd_cli_neuronsphere/services/postgres/always-initdb.d/airflow.sh
 Comment: 
 
 Filename: hmd_cli_neuronsphere/services/postgres/always-initdb.d/hmd_ms_deployment.sh
@@ -108,20 +240,20 @@
 
 Filename: hmd_cli_neuronsphere/services/trino/config/catalog/iceberg.properties
 Comment: 
 
 Filename: hmd_cli_neuronsphere/services/trino/config/catalog/tpch.properties
 Comment: 
 
-Filename: hmd_cli_neuronsphere-0.1.98.dist-info/METADATA
+Filename: hmd_cli_neuronsphere-0.1.99.dist-info/METADATA
 Comment: 
 
-Filename: hmd_cli_neuronsphere-0.1.98.dist-info/WHEEL
+Filename: hmd_cli_neuronsphere-0.1.99.dist-info/WHEEL
 Comment: 
 
-Filename: hmd_cli_neuronsphere-0.1.98.dist-info/top_level.txt
+Filename: hmd_cli_neuronsphere-0.1.99.dist-info/top_level.txt
 Comment: 
 
-Filename: hmd_cli_neuronsphere-0.1.98.dist-info/RECORD
+Filename: hmd_cli_neuronsphere-0.1.99.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## hmd_cli_neuronsphere/hmd_cli_neuronsphere.py

```diff
@@ -146,14 +146,15 @@
     if configs.get("trino").get("enabled"):
         required_dirs += [
             Path("trino", "data"),
             Path("trino", "config"),
             Path("trino", "hadoop", "dfs", "name"),
             Path("trino", "hadoop", "dfs", "data"),
             Path("hive", "config"),
+            Path("hadoop", "config"),
             Path("warehouse"),
             Path("postgresql", "scripts"),
         ]
     if configs.get("transform").get("enabled"):
         required_dirs += [Path("transform", "airflow", "logs")]
         required_dirs += [Path("transform", "airflow", "provider_transforms")]
         required_dirs += [Path("transform", "airflow", "dag_generators")]
@@ -163,15 +164,15 @@
         required_dirs += [Path("datadog", "log")]
         required_dirs += [Path("datadog", "s6")]
     for dir in required_dirs:
         full_dir = _hmd_home / dir
         if not full_dir.exists():
             os.umask(0)
             print("make", str(_hmd_home / dir))
-            (_hmd_home / dir).mkdir(mode=0o777, exist_ok=True, parents=True)
+            os.makedirs(_hmd_home / dir, exist_ok=True)
 
     # Copy over included Postgres Init scripts
     _pg_scripts_path = _services_dir / "postgres"
 
     for root, _, files in os.walk(_pg_scripts_path):
         for f in files:
             dest = (
@@ -204,14 +205,23 @@
         and len(os.listdir(_hmd_home / "hive" / "config")) == 0
     ):
         shutil.copytree(
             _services_dir / "hive",
             _hmd_home / "hive" / "config",
             dirs_exist_ok=True,
         )
+    if (
+        configs.get("trino").get("enabled")
+        and len(os.listdir(_hmd_home / "hadoop" / "config")) == 0
+    ):
+        shutil.copytree(
+            _services_dir / "hadoop",
+            _hmd_home / "hadoop" / "config",
+            dirs_exist_ok=True,
+        )
 
     os.environ["UID"] = getpass.getuser()
 
     command = [
         *_get_base_command(),
         "up",
         "--remove-orphans",
@@ -219,15 +229,24 @@
         "-d",
         "--quiet-pull",
     ]
     _exec(command)
 
 
 def stop_neuronsphere():
-    load_env()
+    load_hmd_env()
+    home_projects_path = _hmd_home / "studio" / "projects"
+    hmd_repo_home = os.environ.get("HMD_REPO_HOME")
+
+    if os.environ.get("HMD_PROJECTS_PATH") is None:
+        os.environ["HMD_PROJECTS_PATH"] = (
+            str(home_projects_path)
+            if os.path.exists(home_projects_path)
+            else hmd_repo_home
+        )
     command = [*_get_base_command(), "down"]
     _exec(command)
 
 
 def merge_configs(config: Dict, default: Dict):
     for key, value in config.items():
         if isinstance(value, dict):
```

## hmd_cli_neuronsphere/services/docker-compose.trino.yml

```diff
@@ -33,14 +33,15 @@
         target: /user/hive/warehouse
     environment:
       - CLUSTER_NAME=test
     env_file:
       - ./hadoop-hive.env
     ports:
       - '9870:9870'
+      - '8020:8020'
   datanode:
     container_name: datanode
     image: ${HMD_CONTAINER_REGISTRY:-ghcr.io/neuronsphere}/hmd-img-hdfs-datanode:${HMD_IMG_HDFS_DATANODE_VERSION:-stable}
     volumes:
       - type: bind
         source: ${HMD_HOME}/trino/hadoop/dfs/data
         target: /hadoop/dfs/data
@@ -57,26 +58,33 @@
     ports:
       - '9864:9864'
   metastore:
     container_name: metastore
     image: ${HMD_CONTAINER_REGISTRY:-ghcr.io/neuronsphere}/hmd-inf-hive-metastore:${HMD_INF_HIVE_METASTORE_VERSION:-stable}
     env_file:
       - ./hadoop-hive.env
+    environment:
+      - HADOOP_CONF_DIR=/opt/hadoop-3.2.3/conf
+      - USER=root
     ports:
       - '9083:9083'
     volumes:
       - type: bind
         source: ${HMD_HOME}/data
         target: /hmd/data
       - type: bind
         source: ${HMD_HOME}/warehouse
         target: /user/hive/warehouse
       - type: bind
         source: ${HMD_HOME}/hive/config
         target: /opt/metastore/conf
+      - type: bind
+        source: ${HMD_HOME}/hadoop/config
+        target: /opt/hadoop-3.2.3/conf
+
     depends_on:
       - db
       - namenode
       - datanode
 
   trino:
     container_name: trino
```

## hmd_cli_neuronsphere/services/hadoop-hive.env

```diff
@@ -10,14 +10,21 @@
 # HIVE_SITE_CONF_datanucleus_schema_autoCreateAll=true
 HIVE_SITE_CONF_datanucleus_schema_autoCreateTables=true
 HIVE_SITE_CONF_hive_metastore_uris=thrift://metastore:9083
 HIVE_SITE_CONF_hive_metastore_schema_verification=false
 HDFS_CONF_dfs_namenode_datanode_registration_ip___hostname___check=false
 HIVE_SITE_CONF_hive_root_logger=INFO,Console
 
+HDFS_CONF_dfs_namenode_rpc___bind___host=0.0.0.0
+HDFS_CONF_dfs_namenode_servicerpc___bind___host=0.0.0.0
+HDFS_CONF_dfs_namenode_http___bind___host=0.0.0.0
+HDFS_CONF_dfs_namenode_https___bind___host=0.0.0.0
+HDFS_CONF_dfs_client_use_datanode_hostname=true
+HDFS_CONF_dfs_datanode_user_datanode_hostname=true
+
 CORE_CONF_fs_defaultFS=hdfs://namenode:8020
 CORE_CONF_hadoop_http_staticuser_user=root
 CORE_CONF_hadoop_proxyuser_root_hosts=*
 CORE_CONF_hadoop_proxyuser_root_groups=*
 
 HDFS_CONF_dfs_webhdfs_enabled=true
 HDFS_CONF_dfs_permissions_enabled=false
```

## hmd_cli_neuronsphere/services/hive/metastore-site.xml

### hmd_cli_neuronsphere/services/hive/metastore-site.xml

```diff
@@ -1,36 +1,56 @@
 <?xml version="1.0" encoding="utf-8"?>
 <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
+<!--
+   Licensed to the Apache Software Foundation (ASF) under one or more
+   contributor license agreements.  See the NOTICE file distributed with
+   this work for additional information regarding copyright ownership.
+   The ASF licenses this file to You under the Apache License, Version 2.0
+   (the "License"); you may not use this file except in compliance with
+   the License.  You may obtain a copy of the License at
+
+       http://www.apache.org/licenses/LICENSE-2.0
+
+   Unless required by applicable law or agreed to in writing, software
+   distributed under the License is distributed on an "AS IS" BASIS,
+   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
+   See the License for the specific language governing permissions and
+   limitations under the License.
+-->
 <configuration>
   <property>
-    <name>metastore.thrift.uris</name>
+    <name>hive.metastore.uris</name>
     <value>thrift://metastore:9083</value>
   </property>
   <property>
-    <name>hive.metastore.schema.verification</name>
-    <value>true</value>
+    <name>hive.root.logger</name>
+    <value>INFO,Console</value>
   </property>
   <property>
-    <name>datanucleus.schema.autoCreateTables</name>
-    <value>true</value>
+    <name>javax.jdo.option.ConnectionURL</name>
+    <value>jdbc:postgresql://db/metastore</value>
   </property>
   <property>
     <name>javax.jdo.option.ConnectionDriverName</name>
     <value>org.postgresql.Driver</value>
   </property>
   <property>
-    <name>javax.jdo.option.ConnectionURL</name>
-    <value>jdbc:postgresql://db/metastore</value>
+    <name>datanucleus.schema.autoCreateTables</name>
+    <value>true</value>
   </property>
   <property>
-    <name>javax.jdo.option.ConnectionUserName</name>
+    <name>javax.jdo.option.ConnectionPassword</name>
     <value>metastore</value>
   </property>
   <property>
-    <name>javax.jdo.option.ConnectionPassword</name>
+    <name>hive.metastore.schema.verification</name>
+    <value>false</value>
+  </property>
+  <property>
+    <name>javax.jdo.option.ConnectionUserName</name>
     <value>metastore</value>
   </property>
   <property>
     <name>metastore.task.threads.always</name>
     <value>org.apache.hadoop.hive.metastore.events.EventCleanerTask</value>
   </property>
   <property>
```

## hmd_cli_neuronsphere/services/trino/config/catalog/hive.properties

```diff
@@ -1,5 +1,5 @@
-connector.name=hive-hadoop2
+connector.name=hive
 hive.metastore.uri=thrift://metastore:9083
 hive.security=allow-all
 hive.recursive-directories=true
 hive.allow-register-partition-procedure=true
```

## Comparing `hmd_cli_neuronsphere-0.1.98.dist-info/METADATA` & `hmd_cli_neuronsphere-0.1.99.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hmd-cli-neuronsphere
-Version: 0.1.98
+Version: 0.1.99
 Summary: Local NeuronSphere Control CLI
 Home-page: UNKNOWN
 Author: Adam Stortz
 Author-email: adam.stortz@hmdlabs.io
 License: Apache 2.0
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

