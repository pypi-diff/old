# Comparing `tmp/datacx-0.3.1.tar.gz` & `tmp/datacx-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/alchemist/Desktop/OpenSource/datacx/dist/.tmp-urwgk1f1/datacx-0.3.1.tar", last modified: Mon Apr  3 09:55:12 2023, max compression
+gzip compressed data, was "/home/alchemist/Desktop/OpenSource/datacx/dist/.tmp-_6cratq5/datacx-0.4.0.tar", last modified: Fri Apr  7 08:37:35 2023, max compression
```

## Comparing `datacx-0.3.1.tar` & `datacx-0.4.0.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     1065 2023-03-30 09:18:16.000000 datacx-0.3.1/LICENSE
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     5286 2023-04-03 09:55:12.000000 datacx-0.3.1/PKG-INFO
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     3517 2023-04-03 09:46:10.000000 datacx-0.3.1/README.md
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      191 2023-04-03 09:53:57.000000 datacx-0.3.1/datacx/__init__.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     3466 2023-04-03 09:47:25.000000 datacx-0.3.1/datacx/core.py
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx/databases/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-28 07:41:49.000000 datacx-0.3.1/datacx/databases/__init__.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     7114 2023-04-03 09:47:15.000000 datacx-0.3.1/datacx/databases/database.py
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx/datalakes/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-25 13:37:38.000000 datacx-0.3.1/datacx/datalakes/__init__.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)    14914 2023-04-01 09:35:29.000000 datacx-0.3.1/datacx/datalakes/datalake.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     5767 2023-04-01 09:34:54.000000 datacx-0.3.1/datacx/datalakes/utils.py
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx/datawarehouses/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-28 07:38:28.000000 datacx-0.3.1/datacx/datawarehouses/__init__.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     6979 2023-03-30 15:32:19.000000 datacx-0.3.1/datacx/datawarehouses/datawarehouse.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     1684 2023-03-28 10:56:42.000000 datacx-0.3.1/datacx/datawarehouses/utils.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      432 2023-03-30 13:59:12.000000 datacx-0.3.1/datacx/exceptions.py
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx/nosql/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-28 07:41:59.000000 datacx-0.3.1/datacx/nosql/__init__.py
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     2780 2023-03-31 19:25:41.000000 datacx-0.3.1/datacx/nosql/nosql.py
-drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx.egg-info/
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     5286 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx.egg-info/PKG-INFO
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      529 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx.egg-info/SOURCES.txt
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        1 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx.egg-info/dependency_links.txt
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      301 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx.egg-info/requires.txt
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        7 2023-04-03 09:55:12.000000 datacx-0.3.1/datacx.egg-info/top_level.txt
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     1538 2023-04-03 09:53:57.000000 datacx-0.3.1/pyproject.toml
--rw-rw-r--   0 alchemist  (1000) alchemist  (1000)       38 2023-04-03 09:55:12.000000 datacx-0.3.1/setup.cfg
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     1065 2023-03-30 09:18:16.000000 datacx-0.4.0/LICENSE
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     5285 2023-04-07 08:37:35.000000 datacx-0.4.0/PKG-INFO
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     3516 2023-04-07 07:58:14.000000 datacx-0.4.0/README.md
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      191 2023-04-07 08:37:01.000000 datacx-0.4.0/datacx/__init__.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     3474 2023-04-07 08:33:56.000000 datacx-0.4.0/datacx/core.py
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx/databases/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-28 07:41:49.000000 datacx-0.4.0/datacx/databases/__init__.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)    10999 2023-04-07 07:56:28.000000 datacx-0.4.0/datacx/databases/database.py
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx/datalakes/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-25 13:37:38.000000 datacx-0.4.0/datacx/datalakes/__init__.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)    14914 2023-04-01 09:35:29.000000 datacx-0.4.0/datacx/datalakes/datalake.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     5767 2023-04-01 09:34:54.000000 datacx-0.4.0/datacx/datalakes/utils.py
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx/datawarehouses/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-28 07:38:28.000000 datacx-0.4.0/datacx/datawarehouses/__init__.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)    11538 2023-04-07 07:50:57.000000 datacx-0.4.0/datacx/datawarehouses/datawarehouse.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     1684 2023-04-06 18:09:59.000000 datacx-0.4.0/datacx/datawarehouses/utils.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      432 2023-03-30 13:59:12.000000 datacx-0.4.0/datacx/exceptions.py
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx/nosql/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        0 2023-03-28 07:41:59.000000 datacx-0.4.0/datacx/nosql/__init__.py
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     3668 2023-04-07 08:36:09.000000 datacx-0.4.0/datacx/nosql/nosql.py
+drwxrwxr-x   0 alchemist  (1000) alchemist  (1000)        0 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx.egg-info/
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     5285 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx.egg-info/PKG-INFO
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      529 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx.egg-info/SOURCES.txt
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        1 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx.egg-info/dependency_links.txt
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)      320 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx.egg-info/requires.txt
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)        7 2023-04-07 08:37:35.000000 datacx-0.4.0/datacx.egg-info/top_level.txt
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)     1564 2023-04-07 08:37:01.000000 datacx-0.4.0/pyproject.toml
+-rw-rw-r--   0 alchemist  (1000) alchemist  (1000)       38 2023-04-07 08:37:35.000000 datacx-0.4.0/setup.cfg
```

### Comparing `datacx-0.3.1/LICENSE` & `datacx-0.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `datacx-0.3.1/PKG-INFO` & `datacx-0.4.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: datacx
-Version: 0.3.1
+Version: 0.4.0
 Summary: Data Connectors for all data sources
 Author-email: Vinish M <vinishuchiha@gmail.com>
 License: MIT License
         
         Copyright (c) 2023 Vinish M
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
@@ -39,19 +39,19 @@
 
 <img src="docs/images/LOGO.png" alt="drawing" width="200"/>
 
 A Data Connector for all the data sources
 
 <div align="left">
 
-This library helps to read and write data from most of the data sources. It accelerate the ML development process without worrying about the multiple data connectors.
+This library helps to read and write data from most of the data sources. It accelerate the ML and ETL process without worrying about the multiple data connectors.
 
 ## Installation
 ```bash
-pip install datacx
+pip install -U datacx
 ```
 **Install from sources**
 
 Alternatively, you can also clone the latest version from the [repository](https://github.com/VinishUchiha/datacx) and install it directly from the source code:
 
 ```bash
 pip install -e .
@@ -96,26 +96,26 @@
 ## Supported Connectors
   
 |Data Sources| Type | Read | Write |
 |------------|------| ----  | -----|
 |S3|datalake| &#9745;   | &#9745; |
 |GCS|datalake| &#9745;   | &#9745; |
 |Azure Blob Stoarge| datalake| &#9745;   | &#9745; |
-|Snowflake| datawarehouse | &#9745;   | &#9744; |
-|BigQuery| datawarehouse | &#9745;   | &#9744; |
-|StarRocks| datawarehouse | &#9745;   | &#9744; |
-|Redshift| datawarehouse | &#9745;   | &#9744; |
-|PostgreSQL| database | &#9745;   | &#9744; |
-|MySQL| database | &#9745;   | &#9744; |
-|MsSQL| database | &#9745;   | &#9744; |
-|MariaDB| database | &#9745;   | &#9744; |
-|Oracle| database | &#9745;   | &#9744; |
-|SQLite| database | &#9745;   | &#9744; |
+|Snowflake| datawarehouse | &#9745;   | &#9745; |
+|BigQuery| datawarehouse | &#9745;   | &#9745; |
+|StarRocks| datawarehouse | &#9745;   | &#9745; |
+|Redshift| datawarehouse | &#9745;   | &#9745; |
+|PostgreSQL| database | &#9745;   | &#9745; |
+|MySQL| database | &#9745;   | &#9745; |
+|MariaDB| database | &#9745;   | &#9745; |
+|MsSQL| database | &#9745;   | &#9745; |
+|Oracle| database | &#9745;   | &#9745; |
+|SQLite| database | &#9745;   | &#9745; |
 |MongoDB| nosql | &#9745;   | &#9745; |
-|ElasticSearch| nosql | &#9745;   | &#9744; |
+|ElasticSearch| nosql | &#9745;   | &#9745; |
 
 ## Acknowledgement
 
 Some functionalities of DataCX are inspired by the following packages.
 
 - [ConnectorX](https://github.com/sfu-db/connector-x)
```

### Comparing `datacx-0.3.1/README.md` & `datacx-0.4.0/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -2,19 +2,19 @@
 
 <img src="docs/images/LOGO.png" alt="drawing" width="200"/>
 
 A Data Connector for all the data sources
 
 <div align="left">
 
-This library helps to read and write data from most of the data sources. It accelerate the ML development process without worrying about the multiple data connectors.
+This library helps to read and write data from most of the data sources. It accelerate the ML and ETL process without worrying about the multiple data connectors.
 
 ## Installation
 ```bash
-pip install datacx
+pip install -U datacx
 ```
 **Install from sources**
 
 Alternatively, you can also clone the latest version from the [repository](https://github.com/VinishUchiha/datacx) and install it directly from the source code:
 
 ```bash
 pip install -e .
@@ -59,26 +59,26 @@
 ## Supported Connectors
   
 |Data Sources| Type | Read | Write |
 |------------|------| ----  | -----|
 |S3|datalake| &#9745;   | &#9745; |
 |GCS|datalake| &#9745;   | &#9745; |
 |Azure Blob Stoarge| datalake| &#9745;   | &#9745; |
-|Snowflake| datawarehouse | &#9745;   | &#9744; |
-|BigQuery| datawarehouse | &#9745;   | &#9744; |
-|StarRocks| datawarehouse | &#9745;   | &#9744; |
-|Redshift| datawarehouse | &#9745;   | &#9744; |
-|PostgreSQL| database | &#9745;   | &#9744; |
-|MySQL| database | &#9745;   | &#9744; |
-|MsSQL| database | &#9745;   | &#9744; |
-|MariaDB| database | &#9745;   | &#9744; |
-|Oracle| database | &#9745;   | &#9744; |
-|SQLite| database | &#9745;   | &#9744; |
+|Snowflake| datawarehouse | &#9745;   | &#9745; |
+|BigQuery| datawarehouse | &#9745;   | &#9745; |
+|StarRocks| datawarehouse | &#9745;   | &#9745; |
+|Redshift| datawarehouse | &#9745;   | &#9745; |
+|PostgreSQL| database | &#9745;   | &#9745; |
+|MySQL| database | &#9745;   | &#9745; |
+|MariaDB| database | &#9745;   | &#9745; |
+|MsSQL| database | &#9745;   | &#9745; |
+|Oracle| database | &#9745;   | &#9745; |
+|SQLite| database | &#9745;   | &#9745; |
 |MongoDB| nosql | &#9745;   | &#9745; |
-|ElasticSearch| nosql | &#9745;   | &#9744; |
+|ElasticSearch| nosql | &#9745;   | &#9745; |
 
 ## Acknowledgement
 
 Some functionalities of DataCX are inspired by the following packages.
 
 - [ConnectorX](https://github.com/sfu-db/connector-x)
```

### Comparing `datacx-0.3.1/datacx/core.py` & `datacx-0.4.0/datacx/core.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import yaml
 from .datalakes.datalake import S3, GCS, AzureBlob
 from .datawarehouses.datawarehouse import BigQuery, SnowFlake, Redshift, StarRocks
-from .databases.database import Postgres, MySQL, Oracle, MsSQL, Sqlite
+from .databases.database import Postgres, MySQL, Oracle, MsSQL, Sqlite, MariaDB
 from .nosql.nosql import ElasticSearch, MongoDB
 from .exceptions import ConfigMissingException, UnSupportedDataSourceException
 
 DATA_SOURCES = {
     's3': S3, # AWS S3
     'gcs': GCS, # Google Cloud Storage
     'azureblob': AzureBlob, # Azure Blob Storage
@@ -13,15 +13,15 @@
     'snowflake': SnowFlake, # SnowFlake
     'redshift': Redshift, # AWS Redshift
     'starrocks': StarRocks, # StarRocks
     'postgresql': Postgres, # PostgreSQL
     'mysql': MySQL, # MySQL
     'oracle': Oracle, # Oracle
     'mssql': MsSQL, # MsSQL, SQLServer
-#    'mariadb': MariaDB, # MariaDB
+    'mariadb': MariaDB, # MariaDB
     'sqlite': Sqlite, # Sqlite
     'elasticsearch': ElasticSearch, # ElasticSearch
     'mongodb': MongoDB, # MongoDB
 
 }
 
 DATA_SOURCE_GROUP = {
```

### Comparing `datacx-0.3.1/datacx/datalakes/datalake.py` & `datacx-0.4.0/datacx/datalakes/datalake.py`

 * *Files identical despite different names*

### Comparing `datacx-0.3.1/datacx/datalakes/utils.py` & `datacx-0.4.0/datacx/datalakes/utils.py`

 * *Files identical despite different names*

### Comparing `datacx-0.3.1/datacx/datawarehouses/utils.py` & `datacx-0.4.0/datacx/datawarehouses/utils.py`

 * *Files identical despite different names*

### Comparing `datacx-0.3.1/datacx.egg-info/PKG-INFO` & `datacx-0.4.0/datacx.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: datacx
-Version: 0.3.1
+Version: 0.4.0
 Summary: Data Connectors for all data sources
 Author-email: Vinish M <vinishuchiha@gmail.com>
 License: MIT License
         
         Copyright (c) 2023 Vinish M
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
@@ -39,19 +39,19 @@
 
 <img src="docs/images/LOGO.png" alt="drawing" width="200"/>
 
 A Data Connector for all the data sources
 
 <div align="left">
 
-This library helps to read and write data from most of the data sources. It accelerate the ML development process without worrying about the multiple data connectors.
+This library helps to read and write data from most of the data sources. It accelerate the ML and ETL process without worrying about the multiple data connectors.
 
 ## Installation
 ```bash
-pip install datacx
+pip install -U datacx
 ```
 **Install from sources**
 
 Alternatively, you can also clone the latest version from the [repository](https://github.com/VinishUchiha/datacx) and install it directly from the source code:
 
 ```bash
 pip install -e .
@@ -96,26 +96,26 @@
 ## Supported Connectors
   
 |Data Sources| Type | Read | Write |
 |------------|------| ----  | -----|
 |S3|datalake| &#9745;   | &#9745; |
 |GCS|datalake| &#9745;   | &#9745; |
 |Azure Blob Stoarge| datalake| &#9745;   | &#9745; |
-|Snowflake| datawarehouse | &#9745;   | &#9744; |
-|BigQuery| datawarehouse | &#9745;   | &#9744; |
-|StarRocks| datawarehouse | &#9745;   | &#9744; |
-|Redshift| datawarehouse | &#9745;   | &#9744; |
-|PostgreSQL| database | &#9745;   | &#9744; |
-|MySQL| database | &#9745;   | &#9744; |
-|MsSQL| database | &#9745;   | &#9744; |
-|MariaDB| database | &#9745;   | &#9744; |
-|Oracle| database | &#9745;   | &#9744; |
-|SQLite| database | &#9745;   | &#9744; |
+|Snowflake| datawarehouse | &#9745;   | &#9745; |
+|BigQuery| datawarehouse | &#9745;   | &#9745; |
+|StarRocks| datawarehouse | &#9745;   | &#9745; |
+|Redshift| datawarehouse | &#9745;   | &#9745; |
+|PostgreSQL| database | &#9745;   | &#9745; |
+|MySQL| database | &#9745;   | &#9745; |
+|MariaDB| database | &#9745;   | &#9745; |
+|MsSQL| database | &#9745;   | &#9745; |
+|Oracle| database | &#9745;   | &#9745; |
+|SQLite| database | &#9745;   | &#9745; |
 |MongoDB| nosql | &#9745;   | &#9745; |
-|ElasticSearch| nosql | &#9745;   | &#9744; |
+|ElasticSearch| nosql | &#9745;   | &#9745; |
 
 ## Acknowledgement
 
 Some functionalities of DataCX are inspired by the following packages.
 
 - [ConnectorX](https://github.com/sfu-db/connector-x)
```

### Comparing `datacx-0.3.1/datacx.egg-info/SOURCES.txt` & `datacx-0.4.0/datacx.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `datacx-0.3.1/pyproject.toml` & `datacx-0.4.0/pyproject.toml`

 * *Files 10% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "datacx"
-version = "0.3.1"
+version = "0.4.0"
 description = "Data Connectors for all data sources"
 readme = "README.md"
 authors = [{ name = "Vinish M", email = "vinishuchiha@gmail.com" }]
 license = { file = "LICENSE" }
 classifiers = [
     "License :: OSI Approved :: MIT License",
     "Programming Language :: Python",
@@ -21,14 +21,15 @@
     "azure-storage-blob >= 12.15.0",
     "pandas >= 1.0.0",
     "PyYAML",
     "connectorx",
     "snowflake-connector-python[pandas]",
     "mysql-connector-python-rf",
     "elasticsearch > 8.0.0",
+    "sqlalchemy==1.4.46",
     "pymongo",
     # "mariadb",
     "fastparquet",
     "openpyxl",
     "xlrd",
     "xlwt",
     'tomli; python_version < "3.11"',
@@ -39,15 +40,15 @@
 dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]
 
 [project.urls]
 Homepage = "https://github.com/VinishUchiha/datacx"
 
 
 [tool.bumpver]
-current_version = "0.3.1"
+current_version = "0.4.0"
 version_pattern = "MAJOR.MINOR.PATCH"
 commit_message = "bump version {old_version} -> {new_version}"
 commit = true
 tag = true
 push = false
 
 [tool.bumpver.file_patterns]
```

