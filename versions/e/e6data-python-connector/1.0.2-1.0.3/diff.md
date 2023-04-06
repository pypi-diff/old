# Comparing `tmp/e6data-python-connector-1.0.2.tar.gz` & `tmp/e6data-python-connector-1.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "e6data-python-connector-1.0.2.tar", last modified: Mon Apr  3 12:40:47 2023, max compression
+gzip compressed data, was "e6data-python-connector-1.0.3.tar", last modified: Thu Apr  6 10:30:43 2023, max compression
```

## Comparing `e6data-python-connector-1.0.2.tar` & `e6data-python-connector-1.0.3.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-03 12:40:47.061944 e6data-python-connector-1.0.2/
--rw-r--r--   0 vishal     (501) staff       (20)    11357 2023-04-03 09:33:07.000000 e6data-python-connector-1.0.2/LICENSE
--rw-r--r--   0 vishal     (501) staff       (20)       55 2023-04-03 09:29:00.000000 e6data-python-connector-1.0.2/MANIFEST.in
--rw-r--r--   0 vishal     (501) staff       (20)     5754 2023-04-03 12:40:47.062190 e6data-python-connector-1.0.2/PKG-INFO
--rw-r--r--   0 vishal     (501) staff       (20)     5075 2023-04-03 12:40:10.000000 e6data-python-connector-1.0.2/README.md
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-03 12:40:47.009667 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/
--rw-r--r--   0 vishal     (501) staff       (20)     5754 2023-04-03 12:40:46.000000 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/PKG-INFO
--rw-r--r--   0 vishal     (501) staff       (20)      632 2023-04-03 12:40:46.000000 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/SOURCES.txt
--rw-r--r--   0 vishal     (501) staff       (20)        1 2023-04-03 12:40:46.000000 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/dependency_links.txt
--rw-r--r--   0 vishal     (501) staff       (20)       62 2023-04-03 12:40:46.000000 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/entry_points.txt
--rw-r--r--   0 vishal     (501) staff       (20)       66 2023-04-03 12:40:46.000000 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/requires.txt
--rw-r--r--   0 vishal     (501) staff       (20)        6 2023-04-03 12:40:46.000000 e6data-python-connector-1.0.2/e6data_python_connector.egg-info/top_level.txt
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-03 12:40:47.029659 e6data-python-connector-1.0.2/e6xdb/
--rw-r--r--   0 vishal     (501) staff       (20)      334 2022-04-08 08:47:22.000000 e6data-python-connector-1.0.2/e6xdb/__init__.py
--rw-r--r--   0 vishal     (501) staff       (20)     9958 2022-08-30 11:00:15.000000 e6data-python-connector-1.0.2/e6xdb/common.py
--rw-r--r--   0 vishal     (501) staff       (20)      682 2023-01-02 09:34:23.000000 e6data-python-connector-1.0.2/e6xdb/constants.py
--rw-r--r--   0 vishal     (501) staff       (20)     6052 2023-03-15 05:26:00.000000 e6data-python-connector-1.0.2/e6xdb/datainputstream.py
--rw-r--r--   0 vishal     (501) staff       (20)    13623 2023-03-15 05:26:00.000000 e6data-python-connector-1.0.2/e6xdb/date_time_utils.py
--rw-r--r--   0 vishal     (501) staff       (20)    15412 2023-03-29 10:27:35.000000 e6data-python-connector-1.0.2/e6xdb/e6x.py
--rw-r--r--   0 vishal     (501) staff       (20)      382 2022-04-08 08:47:22.000000 e6data-python-connector-1.0.2/e6xdb/exceptions.py
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-03 12:40:47.060105 e6data-python-connector-1.0.2/e6xdb/server/
--rw-r--r--   0 vishal     (501) staff       (20)   133637 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.2/e6xdb/server/QueryEngineService.py
--rw-r--r--   0 vishal     (501) staff       (20)       56 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.2/e6xdb/server/__init__.py
--rw-r--r--   0 vishal     (501) staff       (20)      366 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.2/e6xdb/server/constants.py
--rw-r--r--   0 vishal     (501) staff       (20)    11878 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.2/e6xdb/server/ttypes.py
--rw-r--r--   0 vishal     (501) staff       (20)    11833 2022-08-30 11:00:15.000000 e6data-python-connector-1.0.2/e6xdb/sqlalchemy_e6x.py
--rw-r--r--   0 vishal     (501) staff       (20)     1777 2022-04-08 08:47:22.000000 e6data-python-connector-1.0.2/e6xdb/typeId.py
--rw-r--r--   0 vishal     (501) staff       (20)       64 2023-04-03 09:31:35.000000 e6data-python-connector-1.0.2/pyproject.toml
--rw-r--r--   0 vishal     (501) staff       (20)       73 2023-04-03 12:40:47.065331 e6data-python-connector-1.0.2/setup.cfg
--rw-r--r--   0 vishal     (501) staff       (20)     1925 2023-04-03 12:40:10.000000 e6data-python-connector-1.0.2/setup.py
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-06 10:30:43.400998 e6data-python-connector-1.0.3/
+-rw-r--r--   0 vishal     (501) staff       (20)    11357 2023-04-03 09:33:07.000000 e6data-python-connector-1.0.3/LICENSE
+-rw-r--r--   0 vishal     (501) staff       (20)       55 2023-04-03 09:29:00.000000 e6data-python-connector-1.0.3/MANIFEST.in
+-rw-r--r--   0 vishal     (501) staff       (20)     5869 2023-04-06 10:30:43.401428 e6data-python-connector-1.0.3/PKG-INFO
+-rw-r--r--   0 vishal     (501) staff       (20)     5189 2023-04-06 10:09:39.000000 e6data-python-connector-1.0.3/README.md
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-06 10:30:43.328382 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/
+-rw-r--r--   0 vishal     (501) staff       (20)     5869 2023-04-06 10:30:42.000000 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/PKG-INFO
+-rw-r--r--   0 vishal     (501) staff       (20)      632 2023-04-06 10:30:43.000000 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/SOURCES.txt
+-rw-r--r--   0 vishal     (501) staff       (20)        1 2023-04-06 10:30:42.000000 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/dependency_links.txt
+-rw-r--r--   0 vishal     (501) staff       (20)       62 2023-04-06 10:30:42.000000 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/entry_points.txt
+-rw-r--r--   0 vishal     (501) staff       (20)       66 2023-04-06 10:30:42.000000 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/requires.txt
+-rw-r--r--   0 vishal     (501) staff       (20)        6 2023-04-06 10:30:42.000000 e6data-python-connector-1.0.3/e6data_python_connector.egg-info/top_level.txt
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-06 10:30:43.389431 e6data-python-connector-1.0.3/e6xdb/
+-rw-r--r--   0 vishal     (501) staff       (20)      334 2022-04-08 08:47:22.000000 e6data-python-connector-1.0.3/e6xdb/__init__.py
+-rw-r--r--   0 vishal     (501) staff       (20)     9958 2022-08-30 11:00:15.000000 e6data-python-connector-1.0.3/e6xdb/common.py
+-rw-r--r--   0 vishal     (501) staff       (20)      682 2023-01-02 09:34:23.000000 e6data-python-connector-1.0.3/e6xdb/constants.py
+-rw-r--r--   0 vishal     (501) staff       (20)     6052 2023-03-15 05:26:00.000000 e6data-python-connector-1.0.3/e6xdb/datainputstream.py
+-rw-r--r--   0 vishal     (501) staff       (20)    13623 2023-03-15 05:26:00.000000 e6data-python-connector-1.0.3/e6xdb/date_time_utils.py
+-rw-r--r--   0 vishal     (501) staff       (20)    15415 2023-04-06 10:02:43.000000 e6data-python-connector-1.0.3/e6xdb/e6x.py
+-rw-r--r--   0 vishal     (501) staff       (20)      382 2022-04-08 08:47:22.000000 e6data-python-connector-1.0.3/e6xdb/exceptions.py
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-04-06 10:30:43.399473 e6data-python-connector-1.0.3/e6xdb/server/
+-rw-r--r--   0 vishal     (501) staff       (20)   133637 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.3/e6xdb/server/QueryEngineService.py
+-rw-r--r--   0 vishal     (501) staff       (20)       56 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.3/e6xdb/server/__init__.py
+-rw-r--r--   0 vishal     (501) staff       (20)      366 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.3/e6xdb/server/constants.py
+-rw-r--r--   0 vishal     (501) staff       (20)    11878 2023-03-29 06:00:44.000000 e6data-python-connector-1.0.3/e6xdb/server/ttypes.py
+-rw-r--r--   0 vishal     (501) staff       (20)    11833 2022-08-30 11:00:15.000000 e6data-python-connector-1.0.3/e6xdb/sqlalchemy_e6x.py
+-rw-r--r--   0 vishal     (501) staff       (20)     1777 2022-04-08 08:47:22.000000 e6data-python-connector-1.0.3/e6xdb/typeId.py
+-rw-r--r--   0 vishal     (501) staff       (20)       64 2023-04-03 09:31:35.000000 e6data-python-connector-1.0.3/pyproject.toml
+-rw-r--r--   0 vishal     (501) staff       (20)       73 2023-04-06 10:30:43.405369 e6data-python-connector-1.0.3/setup.cfg
+-rw-r--r--   0 vishal     (501) staff       (20)     1925 2023-04-06 10:09:39.000000 e6data-python-connector-1.0.3/setup.py
```

### Comparing `e6data-python-connector-1.0.2/LICENSE` & `e6data-python-connector-1.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/PKG-INFO` & `e6data-python-connector-1.0.3/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: e6data-python-connector
-Version: 1.0.2
+Version: 1.0.3
 Summary: Client for the e6data distributed SQL Engine.
 Home-page: https://github.com/e6x-labs/e6data-python-connector
 Author: Uniphi, Inc.
 Author-email: info@e6data.com
 License: Apache 2.0
 Classifier: Operating System :: POSIX :: Linux
 Classifier: License :: OSI Approved :: Apache Software License
@@ -14,98 +14,96 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # e6data Python Connector
 
-![version](https://img.shields.io/badge/version-1.0.2-blue.svg)
+![version](https://img.shields.io/badge/version-1.0.3-blue.svg)
 
 ## Introduction
 
 The e6data Connector for Python provides an interface for writing Python applications that can connect to e6data and perform operations.
 
 To install the Python package, use the command below:
 ```shell
 pip install e6data-python-connector
 ```
 ### Prerequisites
 
 * Open Inbound Port 9000 in the Engine Cluster.
 * Limit access to Port 9000 according to your organizational security policy. Public access is not encouraged.
-* Generated Access Token in the e6data console.
+* Access Token generated in the e6data console.
 
-### Creating connection
+### Create a Connection
 
-Use your e6data email id as a username and access token as a password.
+Use your e6data Email ID as the username and your access token as the password.
 
 ```python
 import e6xdb.e6x as edb
 
-username = '<username>'  # Your e6data email id.
-password = '<password>'  # Generated Access Token from e6data console.
+username = '<username>'  # Your e6data Email ID.
+password = '<password>'  # Access Token generated in the e6data console.
 
-host = '<host>'  # Host name or IP address of you cluster.
-database = '<database>'  # Database name where you want to perform query.
-
-port = 9000  # Engine port.
+host = '<host>'  # IP address or hostname of the cluster to be used.
+database = '<database>'  # # Database to perform the query on.
+port = 9000  # Port of the e6data engine.
 
 conn = edb.connect(
     host=host,
     port=port,
     username=username,
     database=database,
     password=password
 )
 ```
 
-### Performing query
-Performing query
+### Perform a Queries & Get Results
 
 ```python
 
-query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the actual query.
+query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the query.
 
 cursor = conn.cursor()
-query_id = cursor.execute(query)  # execute function returns query id, can be use for aborting the query.
+query_id = cursor.execute(query)  # The execute function returns a unique query ID, which can be use to abort the query.
 all_records = cursor.fetchall()
 for row in all_records:
    print(row)
 ```
 
-To fetch all the records.
+To fetch all the records:
 ```python
 records = cursor.fetchall()
 ```
 
-To fetch one record.
+To fetch one record:
 ```python
 record = cursor.fetchone()
 ```
 
-To fetch limited records.
+To fetch limited records:
 ```python
 limit = 500
 records = cursor.fetchmany(limit)
 ```
 
-To get execution plan after query execution.
+To get the execution plan after query execution:
 ```python
 import json
 
 query_planner = json.loads(cursor.explain_analyse())
 ```
 
-To abort running query.
+To abort a running query:
 ```python
 query_id = '<query_id>'  # query id from execute function response.
 cursor.cancel(query_id)
 ```
 
-Switch database in existing connection.
+Switch database in an existing connection:
 ```python
 database = '<new_database_name>'  # Replace with the new database.
 cursor = conn.cursor(database)
 ```
 
 ### Get Query Time Metrics
 ```python
@@ -120,15 +118,15 @@
 
 execution_time = query_planner.get("total_query_time")  # In milliseconds
 queue_time = query_planner.get("executionQueueingTime")  # In milliseconds
 parsing_time = query_planner.get("parsingTime")  # In milliseconds
 row_count = query_planner.get('row_count_out')
 ```
 
-### Get list of databases, tables or columns
+### Get Schema - a list of Databases, Tables or Columns
 The following code returns a dictionary of all databases, all tables and all columns connected to the cluster currently in use.
 This function can be used without passing database name to get list of all databases.
 
 ```python
 databases = conn.get_schema_names()  # To get list of databases.
 print(databases)
 
@@ -154,26 +152,25 @@
 ```python
 cursor.clear() # Not needed when aborting a query
 cursor.close()
 conn.close()
 ```
 
 ### Code Example
-The following code is an example.
+The following code is an example which combines a few functions described above.
 ```python
 import e6xdb.e6x as edb
 import json
 
-username = '<username>'  # Your e6data email id.
-password = '<password>'  # Generated Access Token from e6data console.
-
-host = '<host>'  # Host name or IP address of you cluster.
-database = '<database>'  # Database name where you want to perform query.
+username = '<username>'  # Your e6data Email ID.
+password = '<password>'  # Access Token generated in the e6data console.
 
-port = 9000  # Engine port.
+host = '<host>'  # IP address or hostname of the cluster to be used.
+database = '<database>'  # # Database to perform the query on.
+port = 9000  # Port of the e6data engine.
 
 sql_query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the actual query.
 
 conn = edb.connect(
     host=host,
     port=port,
     username=username,
@@ -183,15 +180,15 @@
 
 cursor = conn.cursor(db_name=database)
 query_id = cursor.execute(sql_query)
 all_records = cursor.fetchall()
 planner_result = json.loads(cursor.explain_analyse())
 execution_time = planner_result.get("total_query_time") / 1000  # Converting into seconds.
 row_count = planner_result.get('row_count_out')
-columns = [col[0] for col in cursor.description]  # Get the column names and merge with the records.
+columns = [col[0] for col in cursor.description]  # Get the column names and merge them with the results.
 results = []
 for row in all_records:
    row = dict(zip(columns, row))
    results.append(row)
    print(row)
 print('Total row count {}, Execution Time (seconds): {}'.format(row_count, execution_time))
 cursor.clear()
```

### Comparing `e6data-python-connector-1.0.2/README.md` & `e6data-python-connector-1.0.3/README.md`

 * *Files 18% similar despite different names*

```diff
@@ -1,93 +1,91 @@
 # e6data Python Connector
 
-![version](https://img.shields.io/badge/version-1.0.2-blue.svg)
+![version](https://img.shields.io/badge/version-1.0.3-blue.svg)
 
 ## Introduction
 
 The e6data Connector for Python provides an interface for writing Python applications that can connect to e6data and perform operations.
 
 To install the Python package, use the command below:
 ```shell
 pip install e6data-python-connector
 ```
 ### Prerequisites
 
 * Open Inbound Port 9000 in the Engine Cluster.
 * Limit access to Port 9000 according to your organizational security policy. Public access is not encouraged.
-* Generated Access Token in the e6data console.
+* Access Token generated in the e6data console.
 
-### Creating connection
+### Create a Connection
 
-Use your e6data email id as a username and access token as a password.
+Use your e6data Email ID as the username and your access token as the password.
 
 ```python
 import e6xdb.e6x as edb
 
-username = '<username>'  # Your e6data email id.
-password = '<password>'  # Generated Access Token from e6data console.
+username = '<username>'  # Your e6data Email ID.
+password = '<password>'  # Access Token generated in the e6data console.
 
-host = '<host>'  # Host name or IP address of you cluster.
-database = '<database>'  # Database name where you want to perform query.
-
-port = 9000  # Engine port.
+host = '<host>'  # IP address or hostname of the cluster to be used.
+database = '<database>'  # # Database to perform the query on.
+port = 9000  # Port of the e6data engine.
 
 conn = edb.connect(
     host=host,
     port=port,
     username=username,
     database=database,
     password=password
 )
 ```
 
-### Performing query
-Performing query
+### Perform a Queries & Get Results
 
 ```python
 
-query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the actual query.
+query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the query.
 
 cursor = conn.cursor()
-query_id = cursor.execute(query)  # execute function returns query id, can be use for aborting the query.
+query_id = cursor.execute(query)  # The execute function returns a unique query ID, which can be use to abort the query.
 all_records = cursor.fetchall()
 for row in all_records:
    print(row)
 ```
 
-To fetch all the records.
+To fetch all the records:
 ```python
 records = cursor.fetchall()
 ```
 
-To fetch one record.
+To fetch one record:
 ```python
 record = cursor.fetchone()
 ```
 
-To fetch limited records.
+To fetch limited records:
 ```python
 limit = 500
 records = cursor.fetchmany(limit)
 ```
 
-To get execution plan after query execution.
+To get the execution plan after query execution:
 ```python
 import json
 
 query_planner = json.loads(cursor.explain_analyse())
 ```
 
-To abort running query.
+To abort a running query:
 ```python
 query_id = '<query_id>'  # query id from execute function response.
 cursor.cancel(query_id)
 ```
 
-Switch database in existing connection.
+Switch database in an existing connection:
 ```python
 database = '<new_database_name>'  # Replace with the new database.
 cursor = conn.cursor(database)
 ```
 
 ### Get Query Time Metrics
 ```python
@@ -102,15 +100,15 @@
 
 execution_time = query_planner.get("total_query_time")  # In milliseconds
 queue_time = query_planner.get("executionQueueingTime")  # In milliseconds
 parsing_time = query_planner.get("parsingTime")  # In milliseconds
 row_count = query_planner.get('row_count_out')
 ```
 
-### Get list of databases, tables or columns
+### Get Schema - a list of Databases, Tables or Columns
 The following code returns a dictionary of all databases, all tables and all columns connected to the cluster currently in use.
 This function can be used without passing database name to get list of all databases.
 
 ```python
 databases = conn.get_schema_names()  # To get list of databases.
 print(databases)
 
@@ -136,26 +134,25 @@
 ```python
 cursor.clear() # Not needed when aborting a query
 cursor.close()
 conn.close()
 ```
 
 ### Code Example
-The following code is an example.
+The following code is an example which combines a few functions described above.
 ```python
 import e6xdb.e6x as edb
 import json
 
-username = '<username>'  # Your e6data email id.
-password = '<password>'  # Generated Access Token from e6data console.
-
-host = '<host>'  # Host name or IP address of you cluster.
-database = '<database>'  # Database name where you want to perform query.
+username = '<username>'  # Your e6data Email ID.
+password = '<password>'  # Access Token generated in the e6data console.
 
-port = 9000  # Engine port.
+host = '<host>'  # IP address or hostname of the cluster to be used.
+database = '<database>'  # # Database to perform the query on.
+port = 9000  # Port of the e6data engine.
 
 sql_query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the actual query.
 
 conn = edb.connect(
     host=host,
     port=port,
     username=username,
@@ -165,18 +162,18 @@
 
 cursor = conn.cursor(db_name=database)
 query_id = cursor.execute(sql_query)
 all_records = cursor.fetchall()
 planner_result = json.loads(cursor.explain_analyse())
 execution_time = planner_result.get("total_query_time") / 1000  # Converting into seconds.
 row_count = planner_result.get('row_count_out')
-columns = [col[0] for col in cursor.description]  # Get the column names and merge with the records.
+columns = [col[0] for col in cursor.description]  # Get the column names and merge them with the results.
 results = []
 for row in all_records:
    row = dict(zip(columns, row))
    results.append(row)
    print(row)
 print('Total row count {}, Execution Time (seconds): {}'.format(row_count, execution_time))
 cursor.clear()
 cursor.close()
 conn.close()
-```
+```
```

### Comparing `e6data-python-connector-1.0.2/e6data_python_connector.egg-info/PKG-INFO` & `e6data-python-connector-1.0.3/e6data_python_connector.egg-info/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: e6data-python-connector
-Version: 1.0.2
+Version: 1.0.3
 Summary: Client for the e6data distributed SQL Engine.
 Home-page: https://github.com/e6x-labs/e6data-python-connector
 Author: Uniphi, Inc.
 Author-email: info@e6data.com
 License: Apache 2.0
 Classifier: Operating System :: POSIX :: Linux
 Classifier: License :: OSI Approved :: Apache Software License
@@ -14,98 +14,96 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # e6data Python Connector
 
-![version](https://img.shields.io/badge/version-1.0.2-blue.svg)
+![version](https://img.shields.io/badge/version-1.0.3-blue.svg)
 
 ## Introduction
 
 The e6data Connector for Python provides an interface for writing Python applications that can connect to e6data and perform operations.
 
 To install the Python package, use the command below:
 ```shell
 pip install e6data-python-connector
 ```
 ### Prerequisites
 
 * Open Inbound Port 9000 in the Engine Cluster.
 * Limit access to Port 9000 according to your organizational security policy. Public access is not encouraged.
-* Generated Access Token in the e6data console.
+* Access Token generated in the e6data console.
 
-### Creating connection
+### Create a Connection
 
-Use your e6data email id as a username and access token as a password.
+Use your e6data Email ID as the username and your access token as the password.
 
 ```python
 import e6xdb.e6x as edb
 
-username = '<username>'  # Your e6data email id.
-password = '<password>'  # Generated Access Token from e6data console.
+username = '<username>'  # Your e6data Email ID.
+password = '<password>'  # Access Token generated in the e6data console.
 
-host = '<host>'  # Host name or IP address of you cluster.
-database = '<database>'  # Database name where you want to perform query.
-
-port = 9000  # Engine port.
+host = '<host>'  # IP address or hostname of the cluster to be used.
+database = '<database>'  # # Database to perform the query on.
+port = 9000  # Port of the e6data engine.
 
 conn = edb.connect(
     host=host,
     port=port,
     username=username,
     database=database,
     password=password
 )
 ```
 
-### Performing query
-Performing query
+### Perform a Queries & Get Results
 
 ```python
 
-query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the actual query.
+query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the query.
 
 cursor = conn.cursor()
-query_id = cursor.execute(query)  # execute function returns query id, can be use for aborting the query.
+query_id = cursor.execute(query)  # The execute function returns a unique query ID, which can be use to abort the query.
 all_records = cursor.fetchall()
 for row in all_records:
    print(row)
 ```
 
-To fetch all the records.
+To fetch all the records:
 ```python
 records = cursor.fetchall()
 ```
 
-To fetch one record.
+To fetch one record:
 ```python
 record = cursor.fetchone()
 ```
 
-To fetch limited records.
+To fetch limited records:
 ```python
 limit = 500
 records = cursor.fetchmany(limit)
 ```
 
-To get execution plan after query execution.
+To get the execution plan after query execution:
 ```python
 import json
 
 query_planner = json.loads(cursor.explain_analyse())
 ```
 
-To abort running query.
+To abort a running query:
 ```python
 query_id = '<query_id>'  # query id from execute function response.
 cursor.cancel(query_id)
 ```
 
-Switch database in existing connection.
+Switch database in an existing connection:
 ```python
 database = '<new_database_name>'  # Replace with the new database.
 cursor = conn.cursor(database)
 ```
 
 ### Get Query Time Metrics
 ```python
@@ -120,15 +118,15 @@
 
 execution_time = query_planner.get("total_query_time")  # In milliseconds
 queue_time = query_planner.get("executionQueueingTime")  # In milliseconds
 parsing_time = query_planner.get("parsingTime")  # In milliseconds
 row_count = query_planner.get('row_count_out')
 ```
 
-### Get list of databases, tables or columns
+### Get Schema - a list of Databases, Tables or Columns
 The following code returns a dictionary of all databases, all tables and all columns connected to the cluster currently in use.
 This function can be used without passing database name to get list of all databases.
 
 ```python
 databases = conn.get_schema_names()  # To get list of databases.
 print(databases)
 
@@ -154,26 +152,25 @@
 ```python
 cursor.clear() # Not needed when aborting a query
 cursor.close()
 conn.close()
 ```
 
 ### Code Example
-The following code is an example.
+The following code is an example which combines a few functions described above.
 ```python
 import e6xdb.e6x as edb
 import json
 
-username = '<username>'  # Your e6data email id.
-password = '<password>'  # Generated Access Token from e6data console.
-
-host = '<host>'  # Host name or IP address of you cluster.
-database = '<database>'  # Database name where you want to perform query.
+username = '<username>'  # Your e6data Email ID.
+password = '<password>'  # Access Token generated in the e6data console.
 
-port = 9000  # Engine port.
+host = '<host>'  # IP address or hostname of the cluster to be used.
+database = '<database>'  # # Database to perform the query on.
+port = 9000  # Port of the e6data engine.
 
 sql_query = 'SELECT * FROM <TABLE_NAME>'  # Replace with the actual query.
 
 conn = edb.connect(
     host=host,
     port=port,
     username=username,
@@ -183,15 +180,15 @@
 
 cursor = conn.cursor(db_name=database)
 query_id = cursor.execute(sql_query)
 all_records = cursor.fetchall()
 planner_result = json.loads(cursor.explain_analyse())
 execution_time = planner_result.get("total_query_time") / 1000  # Converting into seconds.
 row_count = planner_result.get('row_count_out')
-columns = [col[0] for col in cursor.description]  # Get the column names and merge with the records.
+columns = [col[0] for col in cursor.description]  # Get the column names and merge them with the results.
 results = []
 for row in all_records:
    row = dict(zip(columns, row))
    results.append(row)
    print(row)
 print('Total row count {}, Execution Time (seconds): {}'.format(row_count, execution_time))
 cursor.clear()
```

### Comparing `e6data-python-connector-1.0.2/e6data_python_connector.egg-info/SOURCES.txt` & `e6data-python-connector-1.0.3/e6data_python_connector.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/common.py` & `e6data-python-connector-1.0.3/e6xdb/common.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/constants.py` & `e6data-python-connector-1.0.3/e6xdb/constants.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/datainputstream.py` & `e6data-python-connector-1.0.3/e6xdb/datainputstream.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/date_time_utils.py` & `e6data-python-connector-1.0.3/e6xdb/date_time_utils.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/e6x.py` & `e6data-python-connector-1.0.3/e6xdb/e6x.py`

 * *Files 1% similar despite different names*

```diff
@@ -97,15 +97,15 @@
 class Connection(object):
     """Wraps a http e6xdb session"""
 
     def __init__(
             self,
             host=None,
             port=None,
-            scheme='e6xdb',
+            scheme='e6data',
             username=None,
             database='default',
             auth=None,
             configuration=None,
             kerberos_service_name=None,
             password=None,
             check_hostname=None,
@@ -116,16 +116,16 @@
         self.__password = password
         self._database = database
         self._session_id = None
 
         # service_name = 'E6x'  # E6x  QueryExecutor
         service_name = 'QueryEngine'  # E6x  QueryExecutor
 
-        if scheme != "e6xdb":
-            raise ValueError("scheme is not e6xdb")
+        if scheme != "e6data":
+            raise ValueError("scheme is not e6data")
 
         if not self.__username or not self.__password:
             raise ValueError("username or password cannot be empty.")
         if port is None:
             port = 9000
         self._transport = TSocket.TSocket(host, port)
         self._transport = TTransport.TBufferedTransport(self._transport)
```

### Comparing `e6data-python-connector-1.0.2/e6xdb/server/QueryEngineService.py` & `e6data-python-connector-1.0.3/e6xdb/server/QueryEngineService.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/server/ttypes.py` & `e6data-python-connector-1.0.3/e6xdb/server/ttypes.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/sqlalchemy_e6x.py` & `e6data-python-connector-1.0.3/e6xdb/sqlalchemy_e6x.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/e6xdb/typeId.py` & `e6data-python-connector-1.0.3/e6xdb/typeId.py`

 * *Files identical despite different names*

### Comparing `e6data-python-connector-1.0.2/setup.py` & `e6data-python-connector-1.0.3/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 import os
 
 import setuptools
 
 envstring = lambda var: os.environ.get(var) or ""
 
-VERSION = [1, 0, 2]
+VERSION = [1, 0, 3]
 
 
 def get_long_desc():
     with open("README.md", "r") as fh:
         long_description = fh.read()
     return long_description
```

