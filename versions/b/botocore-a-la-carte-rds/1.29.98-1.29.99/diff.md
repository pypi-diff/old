# Comparing `tmp/botocore-a-la-carte-rds-1.29.98.tar.gz` & `tmp/botocore-a-la-carte-rds-1.29.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "botocore-a-la-carte-rds-1.29.98.tar", last modified: Fri Mar 24 01:24:36 2023, max compression
+gzip compressed data, was "botocore-a-la-carte-rds-1.29.99.tar", last modified: Sat Mar 25 01:23:03 2023, max compression
```

## Comparing `botocore-a-la-carte-rds-1.29.98.tar` & `botocore-a-la-carte-rds-1.29.99.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.286106 botocore-a-la-carte-rds-1.29.98/
--rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-24 01:24:36.000000 botocore-a-la-carte-rds-1.29.98/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-24 01:24:36.286106 botocore-a-la-carte-rds-1.29.98/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.282106 botocore-a-la-carte-rds-1.29.98/botocore/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.282106 botocore-a-la-carte-rds-1.29.98/botocore/data/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.282106 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.282106 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/
--rw-r--r--   0 runner    (1001) docker     (123)    20411 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     3095 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   326067 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     2645 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.286106 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/
--rw-r--r--   0 runner    (1001) docker     (123)    19575 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/endpoint-rule-set-1.json
--rw-r--r--   0 runner    (1001) docker     (123)    57903 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/examples-1.json
--rw-r--r--   0 runner    (1001) docker     (123)     6308 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/paginators-1.json
--rw-r--r--   0 runner    (1001) docker     (123)   952863 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/service-2.json
--rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/service-2.sdk-extras.json
--rw-r--r--   0 runner    (1001) docker     (123)     9673 2023-03-24 01:23:57.000000 botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/waiters-2.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 01:24:36.286106 botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-24 01:24:36.000000 botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-24 01:24:36.000000 botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 01:24:36.000000 botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-24 01:24:36.000000 botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 01:24:36.286106 botocore-a-la-carte-rds-1.29.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-03-24 01:24:36.000000 botocore-a-la-carte-rds-1.29.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.132773 botocore-a-la-carte-rds-1.29.99/
+-rw-r--r--   0 runner    (1001) docker     (123)    10174 2023-03-25 01:23:02.000000 botocore-a-la-carte-rds-1.29.99/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-25 01:23:03.132773 botocore-a-la-carte-rds-1.29.99/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.128773 botocore-a-la-carte-rds-1.29.99/botocore/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.128773 botocore-a-la-carte-rds-1.29.99/botocore/data/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.128773 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.132773 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/
+-rw-r--r--   0 runner    (1001) docker     (123)    20411 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     3095 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   326067 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     2645 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.132773 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/
+-rw-r--r--   0 runner    (1001) docker     (123)    19575 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/endpoint-rule-set-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)    57903 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/examples-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)     6308 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/paginators-1.json
+-rw-r--r--   0 runner    (1001) docker     (123)   952462 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/service-2.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/service-2.sdk-extras.json
+-rw-r--r--   0 runner    (1001) docker     (123)     9673 2023-03-25 01:22:12.000000 botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/waiters-2.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-25 01:23:03.132773 botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      950 2023-03-25 01:23:03.000000 botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-25 01:23:03.000000 botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-25 01:23:03.000000 botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-25 01:23:03.000000 botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-25 01:23:03.132773 botocore-a-la-carte-rds-1.29.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-03-25 01:23:02.000000 botocore-a-la-carte-rds-1.29.99/setup.py
```

### Comparing `botocore-a-la-carte-rds-1.29.98/LICENSE.txt` & `botocore-a-la-carte-rds-1.29.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/PKG-INFO` & `botocore-a-la-carte-rds-1.29.99/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-rds
-Version: 1.29.98
+Version: 1.29.99
 Summary: rds data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/endpoint-rule-set-1.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/paginators-1.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/service-2.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/service-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-09-01/waiters-2.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-09-01/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/endpoint-rule-set-1.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/endpoint-rule-set-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/examples-1.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/examples-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/paginators-1.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/paginators-1.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/service-2.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/service-2.json`

 * *Files 0% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9997625206111774%*

 * *Differences: {"'operations'": "{'CreateCustomDBEngineVersion': {'errors': {insert: [(4, OrderedDict([('shape', "*

 * *                 "'CreateCustomDBEngineVersionFault')]))]}}, 'CreateDBCluster': {'documentation': "*

 * *                 "'<p>Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.</p> <p>If you "*

 * *                 'create an Aurora DB cluster, the request creates an empty cluster. You must '*

 * *                 'explicitly create the writer instance for your DB cluster using the <a '*

 * *                 'href=" […]*

```diff
@@ -425,14 +425,17 @@
                     "shape": "CustomDBEngineVersionQuotaExceededFault"
                 },
                 {
                     "shape": "Ec2ImagePropertiesNotSupportedFault"
                 },
                 {
                     "shape": "KMSKeyNotAccessibleFault"
+                },
+                {
+                    "shape": "CreateCustomDBEngineVersionFault"
                 }
             ],
             "http": {
                 "method": "POST",
                 "requestUri": "/"
             },
             "input": {
@@ -441,15 +444,15 @@
             "name": "CreateCustomDBEngineVersion",
             "output": {
                 "resultWrapper": "CreateCustomDBEngineVersionResult",
                 "shape": "DBEngineVersion"
             }
         },
         "CreateDBCluster": {
-            "documentation": "<p>Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.</p> <p>You can use the <code>ReplicationSourceIdentifier</code> parameter to create an Amazon Aurora DB cluster as a read replica of another DB cluster or Amazon RDS MySQL or PostgreSQL DB instance. For more information about Amazon Aurora, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html\">What is Amazon Aurora?</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>You can also use the <code>ReplicationSourceIdentifier</code> parameter to create a Multi-AZ DB cluster read replica with an RDS for PostgreSQL DB instance as the source. For more information about Multi-AZ DB clusters, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html\">Multi-AZ DB cluster deployments</a> in the <i>Amazon RDS User Guide</i>.</p>",
+            "documentation": "<p>Creates a new Amazon Aurora DB cluster or Multi-AZ DB cluster.</p> <p>If you create an Aurora DB cluster, the request creates an empty cluster. You must explicitly create the writer instance for your DB cluster using the <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html\">CreateDBInstance</a> operation. If you create a Multi-AZ DB cluster, the request creates a writer and two reader DB instances for you, each in a different Availability Zone.</p> <p>You can use the <code>ReplicationSourceIdentifier</code> parameter to create an Amazon Aurora DB cluster as a read replica of another DB cluster or Amazon RDS MySQL or PostgreSQL DB instance. For more information about Amazon Aurora, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html\">What is Amazon Aurora?</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>You can also use the <code>ReplicationSourceIdentifier</code> parameter to create a Multi-AZ DB cluster read replica with an RDS for PostgreSQL DB instance as the source. For more information about Multi-AZ DB clusters, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html\">Multi-AZ DB cluster deployments</a> in the <i>Amazon RDS User Guide</i>.</p>",
             "errors": [
                 {
                     "shape": "DBClusterAlreadyExistsFault"
                 },
                 {
                     "shape": "InsufficientStorageClusterCapacityFault"
                 },
@@ -3842,15 +3845,15 @@
             "name": "StartDBInstanceAutomatedBackupsReplication",
             "output": {
                 "resultWrapper": "StartDBInstanceAutomatedBackupsReplicationResult",
                 "shape": "StartDBInstanceAutomatedBackupsReplicationResult"
             }
         },
         "StartExportTask": {
-            "documentation": "<p>Starts an export of DB snapshot or DB cluster data to Amazon S3. The provided IAM role must have access to the S3 bucket.</p> <p>You can't export snapshot data from RDS Custom DB instances.</p> <p>You can't export cluster data from Multi-AZ DB clusters.</p> <p>For more information on exporting DB snapshot data, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html\">Exporting DB snapshot data to Amazon S3</a> in the <i>Amazon RDS User Guide</i> or <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/aurora-export-snapshot.html\">Exporting DB cluster snapshot data to Amazon S3</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>For more information on exporting DB cluster data, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/export-cluster-data.html\">Exporting DB cluster data to Amazon S3</a> in the <i>Amazon Aurora User Guide</i>.</p>",
+            "documentation": "<p>Starts an export of DB snapshot or DB cluster data to Amazon S3. The provided IAM role must have access to the S3 bucket.</p> <p>You can't export snapshot data from RDS Custom DB instances.</p> <p>You can't export cluster data from Multi-AZ DB clusters.</p> <p>For more information on exporting DB snapshot data, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html\">Exporting DB snapshot data to Amazon S3</a> in the <i>Amazon RDS User Guide</i> or <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.html\">Exporting DB cluster snapshot data to Amazon S3</a> in the <i>Amazon Aurora User Guide</i>.</p> <p>For more information on exporting DB cluster data, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.html\">Exporting DB cluster data to Amazon S3</a> in the <i>Amazon Aurora User Guide</i>.</p>",
             "errors": [
                 {
                     "shape": "DBSnapshotNotFoundFault"
                 },
                 {
                     "shape": "DBClusterSnapshotNotFoundFault"
                 },
@@ -5030,14 +5033,25 @@
             "members": {
                 "BlueGreenDeployment": {
                     "shape": "BlueGreenDeployment"
                 }
             },
             "type": "structure"
         },
+        "CreateCustomDBEngineVersionFault": {
+            "documentation": "<p>An error occurred while trying to create the CEV.</p>",
+            "error": {
+                "code": "CreateCustomDBEngineVersionFault",
+                "httpStatusCode": 400,
+                "senderFault": true
+            },
+            "exception": true,
+            "members": {},
+            "type": "structure"
+        },
         "CreateCustomDBEngineVersionMessage": {
             "members": {
                 "DatabaseInstallationFilesS3BucketName": {
                     "documentation": "<p>The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is <code>my-custom-installation-files</code>.</p>",
                     "shape": "BucketName"
                 },
                 "DatabaseInstallationFilesS3Prefix": {
@@ -5196,31 +5210,31 @@
                     "shape": "BooleanOptional"
                 },
                 "EnablePerformanceInsights": {
                     "documentation": "<p>A value that indicates whether to turn on Performance Insights for the DB cluster.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html\"> Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for: Multi-AZ DB clusters only</p>",
                     "shape": "BooleanOptional"
                 },
                 "Engine": {
-                    "documentation": "<p>The name of the database engine to be used for this DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora</code> (for MySQL 5.6-compatible Aurora)</p> </li> <li> <p> <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> </ul> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
+                    "documentation": "<p>The name of the database engine to be used for this DB cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> </ul> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
                     "shape": "String"
                 },
                 "EngineMode": {
-                    "documentation": "<p>The DB engine mode of the DB cluster, either <code>provisioned</code>, <code>serverless</code>, <code>parallelquery</code>, <code>global</code>, or <code>multimaster</code>.</p> <p>The <code>parallelquery</code> engine mode isn't required for Aurora MySQL version 1.23 and higher 1.x versions, and version 2.09 and higher 2.x versions.</p> <p>The <code>global</code> engine mode isn't required for Aurora MySQL version 1.22 and higher 1.x versions, and <code>global</code> engine mode isn't required for any 2.x versions.</p> <p>The <code>multimaster</code> engine mode only applies for DB clusters created with Aurora MySQL version 5.6.10a.</p> <p>The <code>serverless</code> engine mode only applies for Aurora Serverless v1 DB clusters.</p> <p>For Aurora PostgreSQL, the <code>global</code> engine mode isn't required, and both the <code>parallelquery</code> and the <code>multimaster</code> engine modes currently aren't supported.</p> <p>Limitations and requirements apply to some DB engine modes. For more information, see the following sections in the <i>Amazon Aurora User Guide</i>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html#aurora-serverless.limitations\">Limitations of Aurora Serverless v1</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html\">Requirements for Aurora Serverless v2</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.html#aurora-mysql-parallel-query-limitations\">Limitations of Parallel Query</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database.limitations\">Limitations of Aurora Global Databases</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-multi-master.html#aurora-multi-master-limitations\">Limitations of Multi-Master Clusters</a> </p> </li> </ul> <p>Valid for: Aurora DB clusters only</p>",
+                    "documentation": "<p>The DB engine mode of the DB cluster, either <code>provisioned</code> or <code>serverless</code>.</p> <p>The <code>serverless</code> engine mode only applies for Aurora Serverless v1 DB clusters.</p> <p>Limitations and requirements apply to some DB engine modes. For more information, see the following sections in the <i>Amazon Aurora User Guide</i>:</p> <ul> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html#aurora-serverless.limitations\">Limitations of Aurora Serverless v1</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html\">Requirements for Aurora Serverless v2</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.html#aurora-mysql-parallel-query-limitations\">Limitations of parallel query</a> </p> </li> <li> <p> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database.limitations\">Limitations of Aurora global databases</a> </p> </li> </ul> <p>Valid for: Aurora DB clusters only</p>",
                     "shape": "String"
                 },
                 "EngineVersion": {
-                    "documentation": "<p>The version number of the database engine to use.</p> <p>To list all of the available engine versions for MySQL 5.6-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html\">MySQL on Amazon RDS Versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html\">Amazon Aurora PostgreSQL releases and engine versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>MySQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt\">MySQL on Amazon RDS Versions</a> in the <i>Amazon RDS User Guide</i>.</p> <p> <b>PostgreSQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts\">Amazon RDS for PostgreSQL versions and extensions</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
+                    "documentation": "<p>The version number of the database engine to use.</p> <p>To list all of the available engine versions for Aurora MySQL version 2 (5.7-compatible) and version 3 (MySQL 8.0-compatible), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>You can supply either <code>5.7</code> or <code>8.0</code> to use the default engine version for Aurora MySQL version 2 or version 3, respectively.</p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html\">Database engine updates for Amazon Aurora MySQL</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html\">Amazon Aurora PostgreSQL releases and engine versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>MySQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt\">Amazon RDS for MySQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p> <b>PostgreSQL</b> </p> <p>For information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts\">Amazon RDS for PostgreSQL</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
                     "shape": "String"
                 },
                 "GlobalClusterIdentifier": {
                     "documentation": "<p>The global cluster ID of an Aurora cluster that becomes the primary cluster in the new global database cluster.</p> <p>Valid for: Aurora DB clusters only</p>",
                     "shape": "String"
                 },
                 "Iops": {
-                    "documentation": "<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS\">Amazon RDS Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting is required to create a Multi-AZ DB cluster.</p> <p>Constraints: Must be a multiple between .5 and 50 of the storage amount for the DB cluster.</p> <p>Valid for: Multi-AZ DB clusters only</p>",
+                    "documentation": "<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS\">Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>This setting is required to create a Multi-AZ DB cluster.</p> <p>Constraints: Must be a multiple between .5 and 50 of the storage amount for the DB cluster.</p> <p>Valid for: Multi-AZ DB clusters only</p>",
                     "shape": "IntegerOptional"
                 },
                 "KmsKeyId": {
                     "documentation": "<p>The Amazon Web Services KMS key identifier for an encrypted DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>When a KMS key isn't specified in <code>KmsKeyId</code>:</p> <ul> <li> <p>If <code>ReplicationSourceIdentifier</code> identifies an encrypted source, then Amazon RDS will use the KMS key used to encrypt the source. Otherwise, Amazon RDS will use your default KMS key.</p> </li> <li> <p>If the <code>StorageEncrypted</code> parameter is enabled and <code>ReplicationSourceIdentifier</code> isn't specified, then Amazon RDS will use your default KMS key.</p> </li> </ul> <p>There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p> <p>If you create a read replica of an encrypted DB cluster in another Amazon Web Services Region, you must set <code>KmsKeyId</code> to a KMS key identifier that is valid in the destination Amazon Web Services Region. This KMS key is used to encrypt the read replica in that Amazon Web Services Region.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
                     "shape": "String"
                 },
                 "ManageMasterUserPassword": {
@@ -9497,15 +9511,15 @@
                     "shape": "String"
                 },
                 "DefaultOnly": {
                     "documentation": "<p>A value that indicates whether only the default version of the specified engine or engine and major version combination is returned.</p>",
                     "shape": "Boolean"
                 },
                 "Engine": {
-                    "documentation": "<p>The database engine to return.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora</code> (for MySQL 5.6-compatible Aurora)</p> </li> <li> <p> <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>",
+                    "documentation": "<p>The database engine to return.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>",
                     "shape": "String"
                 },
                 "EngineVersion": {
                     "documentation": "<p>The database engine version to return.</p> <p>Example: <code>5.1.49</code> </p>",
                     "shape": "String"
                 },
                 "Filters": {
@@ -10235,15 +10249,15 @@
                     "shape": "String"
                 },
                 "DBInstanceClass": {
                     "documentation": "<p>The DB instance class filter value. Specify this parameter to show only the available offerings matching the specified DB instance class.</p>",
                     "shape": "String"
                 },
                 "Engine": {
-                    "documentation": "<p>The name of the engine to retrieve DB instance options for.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora</code> (for MySQL 5.6-compatible Aurora)</p> </li> <li> <p> <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>",
+                    "documentation": "<p>The name of the engine to retrieve DB instance options for.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>",
                     "shape": "String"
                 },
                 "EngineVersion": {
                     "documentation": "<p>The engine version filter value. Specify this parameter to show only the available offerings matching the specified engine version.</p>",
                     "shape": "String"
                 },
                 "Filters": {
@@ -11068,15 +11082,15 @@
                     "shape": "String"
                 },
                 "GlobalClusterIdentifier": {
                     "documentation": "<p>Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database cluster.</p>",
                     "shape": "String"
                 },
                 "GlobalClusterMembers": {
-                    "documentation": "<p>The list of cluster IDs for secondary clusters within the global database cluster. Currently limited to 1 item.</p>",
+                    "documentation": "<p>The list of primary and secondary clusters within the global database cluster.</p>",
                     "shape": "GlobalClusterMemberList"
                 },
                 "GlobalClusterResourceId": {
                     "documentation": "<p>The Amazon Web Services Region-unique, immutable identifier for the global database cluster. This identifier is found in Amazon Web Services CloudTrail log entries whenever the Amazon Web Services KMS key for the DB cluster is accessed.</p>",
                     "shape": "String"
                 },
                 "Status": {
@@ -11886,15 +11900,15 @@
                     "shape": "BooleanOptional"
                 },
                 "EnablePerformanceInsights": {
                     "documentation": "<p>A value that indicates whether to turn on Performance Insights for the DB cluster.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html\"> Using Amazon Performance Insights</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Valid for: Multi-AZ DB clusters only</p>",
                     "shape": "BooleanOptional"
                 },
                 "EngineVersion": {
-                    "documentation": "<p>The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless <code>ApplyImmediately</code> is enabled.</p> <p>To list all of the available engine versions for MySQL 5.6-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
+                    "documentation": "<p>The version number of the database engine to which you want to upgrade. Changing this parameter results in an outage. The change is applied during the next maintenance window unless <code>ApplyImmediately</code> is enabled.</p> <p>To list all of the available engine versions for Aurora MySQL version 2 (5.7-compatible) and version 3 (MySQL 8.0-compatible), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
                     "shape": "String"
                 },
                 "Iops": {
                     "documentation": "<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS\">Amazon RDS Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints: Must be a multiple between .5 and 50 of the storage amount for the DB cluster.</p> <p>Valid for: Multi-AZ DB clusters only</p>",
                     "shape": "IntegerOptional"
                 },
                 "ManageMasterUserPassword": {
@@ -14146,27 +14160,27 @@
                     "shape": "String"
                 },
                 "DomainIAMRoleName": {
                     "documentation": "<p>Specify the name of the IAM role to be used when making API calls to the Directory Service.</p>",
                     "shape": "String"
                 },
                 "EnableCloudwatchLogsExports": {
-                    "documentation": "<p>The list of logs that the restored DB cluster is to export to CloudWatch Logs. The values in the list depend on the DB engine being used.</p> <p> <b>Aurora MySQL</b> </p> <p>Possible values are <code>audit</code>, <code>error</code>, <code>general</code>, and <code>slowquery</code>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>Possible value is <code>postgresql</code>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch\">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p>",
+                    "documentation": "<p>The list of logs that the restored DB cluster is to export to CloudWatch Logs. The values in the list depend on the DB engine being used.</p> <p> <b>Aurora MySQL</b> </p> <p>Possible values are <code>audit</code>, <code>error</code>, <code>general</code>, and <code>slowquery</code>.</p> <p>For more information about exporting CloudWatch Logs for Amazon Aurora, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html#USER_LogAccess.Procedural.UploadtoCloudWatch\">Publishing Database Logs to Amazon CloudWatch Logs</a> in the <i>Amazon Aurora User Guide</i>.</p>",
                     "shape": "LogTypeList"
                 },
                 "EnableIAMDatabaseAuthentication": {
                     "documentation": "<p>A value that indicates whether to enable mapping of Amazon Web Services Identity and Access Management (IAM) accounts to database accounts. By default, mapping isn't enabled.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html\"> IAM Database Authentication</a> in the <i>Amazon Aurora User Guide</i>.</p>",
                     "shape": "BooleanOptional"
                 },
                 "Engine": {
-                    "documentation": "<p>The name of the database engine to be used for this DB cluster.</p> <p>Valid Values: <code>aurora</code> (for MySQL 5.6-compatible Aurora) and <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p>",
+                    "documentation": "<p>The name of the database engine to be used for this DB cluster.</p> <p>Valid Values: <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora)</p>",
                     "shape": "String"
                 },
                 "EngineVersion": {
-                    "documentation": "<p>The version number of the database engine to use.</p> <p>To list all of the available engine versions for <code>aurora</code> (for MySQL 5.6-compatible Aurora), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for <code>aurora-mysql</code> (for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>Example: <code>5.6.10a</code>, <code>5.6.mysql_aurora.1.19.2</code>, <code>5.7.mysql_aurora.2.07.1</code>, <code>8.0.mysql_aurora.3.02.0</code> </p>",
+                    "documentation": "<p>The version number of the database engine to use.</p> <p>To list all of the available engine versions for <code>aurora-mysql</code> (MySQL 5.7-compatible and MySQL 8.0-compatible Aurora), use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>Examples: <code>5.7.mysql_aurora.2.07.1</code>, <code>8.0.mysql_aurora.3.02.0</code> </p>",
                     "shape": "String"
                 },
                 "KmsKeyId": {
                     "documentation": "<p>The Amazon Web Services KMS key identifier for an encrypted DB cluster.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. To use a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN.</p> <p>If the StorageEncrypted parameter is enabled, and you do not specify a value for the <code>KmsKeyId</code> parameter, then Amazon RDS will use your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services Region.</p>",
                     "shape": "String"
                 },
                 "ManageMasterUserPassword": {
@@ -14319,15 +14333,15 @@
                     "shape": "String"
                 },
                 "EngineMode": {
                     "documentation": "<p>The DB engine mode of the DB cluster, either <code>provisioned</code>, <code>serverless</code>, <code>parallelquery</code>, <code>global</code>, or <code>multimaster</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html\"> CreateDBCluster</a>.</p> <p>Valid for: Aurora DB clusters only</p>",
                     "shape": "String"
                 },
                 "EngineVersion": {
-                    "documentation": "<p>The version of the database engine to use for the new DB cluster.</p> <p>To list all of the available engine versions for MySQL 5.6-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html\">MySQL on Amazon RDS Versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html\">Amazon Aurora PostgreSQL releases and engine versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>MySQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt\">MySQL on Amazon RDS Versions</a> in the <i>Amazon RDS User Guide.</i> </p> <p> <b>PostgreSQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts\">Amazon RDS for PostgreSQL versions and extensions</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
+                    "documentation": "<p>The version of the database engine to use for the new DB cluster. If you don't specify an engine version, the default version for the database engine in the Amazon Web Services Region is used.</p> <p>To list all of the available engine versions for MySQL 5.7-compatible and MySQL 8.0-compatible Aurora, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for Aurora PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine aurora-postgresql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for MySQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine mysql --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p>To list all of the available engine versions for RDS for PostgreSQL, use the following command:</p> <p> <code>aws rds describe-db-engine-versions --engine postgres --query \"DBEngineVersions[].EngineVersion\"</code> </p> <p> <b>Aurora MySQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html\">Database engine updates for Amazon Aurora MySQL</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>Aurora PostgreSQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html\">Amazon Aurora PostgreSQL releases and engine versions</a> in the <i>Amazon Aurora User Guide</i>.</p> <p> <b>MySQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html#MySQL.Concepts.VersionMgmt\">Amazon RDS for MySQL</a> in the <i>Amazon RDS User Guide.</i> </p> <p> <b>PostgreSQL</b> </p> <p>See <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html#PostgreSQL.Concepts\">Amazon RDS for PostgreSQL versions and extensions</a> in the <i>Amazon RDS User Guide.</i> </p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
                     "shape": "String"
                 },
                 "Iops": {
                     "documentation": "<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.</p> <p>For information about valid IOPS values, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#USER_PIOPS\">Amazon RDS Provisioned IOPS storage</a> in the <i>Amazon RDS User Guide</i>.</p> <p>Constraints: Must be a multiple between .5 and 50 of the storage amount for the DB instance.</p> <p>Valid for: Aurora DB clusters and Multi-AZ DB clusters</p>",
                     "shape": "IntegerOptional"
                 },
                 "KmsKeyId": {
@@ -15484,15 +15498,15 @@
                     "shape": "StringList"
                 },
                 "ExportTaskIdentifier": {
                     "documentation": "<p>A unique identifier for the export task. This ID isn't an identifier for the Amazon S3 bucket where the data is to be exported.</p>",
                     "shape": "String"
                 },
                 "IamRoleArn": {
-                    "documentation": "<p>The name of the IAM role to use for writing to the Amazon S3 bucket when exporting a snapshot or cluster.</p>",
+                    "documentation": "<p>The name of the IAM role to use for writing to the Amazon S3 bucket when exporting a snapshot or cluster.</p> <p>In the IAM policy attached to your IAM role, include the following required actions to allow the transfer of files from Amazon RDS or Amazon Aurora to an S3 bucket:</p> <ul> <li> <p>s3:PutObject*</p> </li> <li> <p>s3:GetObject*</p> </li> <li> <p>s3:ListBucket</p> </li> <li> <p>s3:DeleteObject*</p> </li> <li> <p>s3:GetBucketLocation </p> </li> </ul> <p>In the policy, include the resources to identify the S3 bucket and objects in the bucket. The following list of resources shows the Amazon Resource Name (ARN) format for accessing S3:</p> <ul> <li> <p> <code>arn:aws:s3:::<i>your-s3-bucket</i> </code> </p> </li> <li> <p> <code>arn:aws:s3:::<i>your-s3-bucket</i>/*</code> </p> </li> </ul>",
                     "shape": "String"
                 },
                 "KmsKeyId": {
                     "documentation": "<p>The ID of the Amazon Web Services KMS key to use to encrypt the data exported to Amazon S3. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. The caller of this operation must be authorized to run the following operations. These can be set in the Amazon Web Services KMS key policy:</p> <ul> <li> <p>kms:Encrypt</p> </li> <li> <p>kms:Decrypt</p> </li> <li> <p>kms:GenerateDataKey</p> </li> <li> <p>kms:GenerateDataKeyWithoutPlaintext</p> </li> <li> <p>kms:ReEncryptFrom</p> </li> <li> <p>kms:ReEncryptTo</p> </li> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> <li> <p>kms:RetireGrant</p> </li> </ul>",
                     "shape": "String"
                 },
                 "S3BucketName": {
@@ -15765,22 +15779,22 @@
                 "BlueGreenDeployment": {
                     "shape": "BlueGreenDeployment"
                 }
             },
             "type": "structure"
         },
         "SwitchoverDetail": {
-            "documentation": "<p>Contains the details about a blue/green deployment.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html\">Using Amazon RDS Blue/Green Deployments for database updates</a> in the <i>Amazon RDS User Guide</i> and <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html\"> Using Amazon RDS Blue/Green Deployments for database updates</a> in the <i>Amazon Aurora User Guide</i>.</p>",
+            "documentation": "<p>Contains the details about a blue/green deployment.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html\">Using Amazon RDS Blue/Green Deployments for database updates</a> in the <i>Amazon RDS User Guide</i> and <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html\">Using Amazon RDS Blue/Green Deployments for database updates</a> in the <i>Amazon Aurora User Guide</i>.</p>",
             "members": {
                 "SourceMember": {
                     "documentation": "<p>The Amazon Resource Name (ARN) of a resource in the blue environment.</p>",
                     "shape": "DatabaseArn"
                 },
                 "Status": {
-                    "documentation": "<p>The switchover status of a resource in a blue/green deployment.</p> <p>Values:</p> <ul> <li> <p> <code>preparing-for-switchover</code> - The resource is being prepared to switch over.</p> </li> <li> <p> <code>ready-for-switchover</code> - The resource is ready to switch over.</p> </li> <li> <p> <code>switchover-in-progress</code> - The resource is being switched over.</p> </li> <li> <p> <code>switchover-completed</code> - The resource has been switched over.</p> </li> <li> <p> <code>switchover-failed</code> - The resource attempted to switch over but failed.</p> </li> </ul>",
+                    "documentation": "<p>The switchover status of a resource in a blue/green deployment.</p> <p>Values:</p> <ul> <li> <p> <code>PROVISIONING</code> - The resource is being prepared to switch over.</p> </li> <li> <p> <code>AVAILABLE</code> - The resource is ready to switch over.</p> </li> <li> <p> <code>SWITCHOVER_IN_PROGRESS</code> - The resource is being switched over.</p> </li> <li> <p> <code>SWITCHOVER_COMPLETED</code> - The resource has been switched over.</p> </li> <li> <p> <code>SWITCHOVER_FAILED</code> - The resource attempted to switch over but failed.</p> </li> <li> <p> <code>MISSING_SOURCE</code> - The source resource has been deleted.</p> </li> <li> <p> <code>MISSING_TARGET</code> - The target resource has been deleted.</p> </li> </ul>",
                     "shape": "SwitchoverDetailStatus"
                 },
                 "TargetMember": {
                     "documentation": "<p>The Amazon Resource Name (ARN) of a resource in the green environment.</p>",
                     "shape": "DatabaseArn"
                 }
             },
```

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/service-2.sdk-extras.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/service-2.sdk-extras.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore/data/rds/2014-10-31/waiters-2.json` & `botocore-a-la-carte-rds-1.29.99/botocore/data/rds/2014-10-31/waiters-2.json`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/PKG-INFO` & `botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: botocore-a-la-carte-rds
-Version: 1.29.98
+Version: 1.29.99
 Summary: rds data for botocore. See the `botocore-a-la-carte` package for more info.
 Home-page: https://github.com/thejcannon/botocore-a-la-carte
 Author: Amazon Web Services
 License: Apache License 2.0
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

### Comparing `botocore-a-la-carte-rds-1.29.98/botocore_a_la_carte_rds.egg-info/SOURCES.txt` & `botocore-a-la-carte-rds-1.29.99/botocore_a_la_carte_rds.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `botocore-a-la-carte-rds-1.29.98/setup.py` & `botocore-a-la-carte-rds-1.29.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 #!/usr/bin/env python
 from setuptools import setup
 
 setup(
     name='botocore-a-la-carte-rds',
-    version="1.29.98",
+    version="1.29.99",
     description='rds data for botocore. See the `botocore-a-la-carte` package for more info.',
     author='Amazon Web Services',
     url='https://github.com/thejcannon/botocore-a-la-carte',
     scripts=[],
     packages=["botocore"],
     package_data={
         'botocore': ['data/rds/*/*.json'],
```

