# Comparing `tmp/water-pipe-0.0.2.tar.gz` & `tmp/water-pipe-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "water-pipe-0.0.2.tar", last modified: Mon Apr  3 08:06:06 2023, max compression
+gzip compressed data, was "water-pipe-0.0.3.tar", last modified: Fri Apr  7 07:52:41 2023, max compression
```

## Comparing `water-pipe-0.0.2.tar` & `water-pipe-0.0.3.tar`

### file list

```diff
@@ -1,26 +1,25 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 08:06:06.722145 water-pipe-0.0.2/
--rw-rw-rw-   0        0        0     1060 2023-04-03 07:53:03.000000 water-pipe-0.0.2/LICENSE
--rw-rw-rw-   0        0        0       26 2023-04-03 07:53:03.000000 water-pipe-0.0.2/MANIFEST.in
--rw-rw-rw-   0        0        0      911 2023-04-03 08:06:06.712144 water-pipe-0.0.2/PKG-INFO
--rw-rw-rw-   0        0        0      239 2023-04-03 07:53:03.000000 water-pipe-0.0.2/README.md
--rw-rw-rw-   0        0        0       42 2023-04-03 08:06:06.724145 water-pipe-0.0.2/setup.cfg
--rw-rw-rw-   0        0        0     3754 2023-04-03 07:53:03.000000 water-pipe-0.0.2/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 08:06:06.484131 water-pipe-0.0.2/water_pipe/
--rw-rw-rw-   0        0        0        0 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/__init__.py
--rw-rw-rw-   0        0        0      352 2023-04-03 08:04:06.000000 water-pipe-0.0.2/water_pipe/__version__.py
--rw-rw-rw-   0        0        0      849 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/base.py
--rw-rw-rw-   0        0        0     4432 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/channel.py
--rw-rw-rw-   0        0        0     2574 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_csv.py
--rw-rw-rw-   0        0        0       16 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_excel.py
--rw-rw-rw-   0        0        0        0 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_greenplum.py
--rw-rw-rw-   0        0        0      241 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_hive.py
--rw-rw-rw-   0        0        0     5253 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_impala.py
--rw-rw-rw-   0        0        0     5496 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_mysql.py
--rw-rw-rw-   0        0        0     6349 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/db_postgres.py
--rw-rw-rw-   0        0        0     1510 2023-04-03 07:53:03.000000 water-pipe-0.0.2/water_pipe/test.py
-drwxrwxrwx   0        0        0        0 2023-04-03 08:06:06.615139 water-pipe-0.0.2/water_pipe.egg-info/
--rw-rw-rw-   0        0        0      911 2023-04-03 08:06:06.000000 water-pipe-0.0.2/water_pipe.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      482 2023-04-03 08:06:06.000000 water-pipe-0.0.2/water_pipe.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 08:06:06.000000 water-pipe-0.0.2/water_pipe.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        7 2023-04-03 08:06:06.000000 water-pipe-0.0.2/water_pipe.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-03 08:06:06.000000 water-pipe-0.0.2/water_pipe.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 07:52:41.520280 water-pipe-0.0.3/
+-rw-rw-rw-   0        0        0     1060 2023-04-03 07:53:03.000000 water-pipe-0.0.3/LICENSE
+-rw-rw-rw-   0        0        0       26 2023-04-03 07:53:03.000000 water-pipe-0.0.3/MANIFEST.in
+-rw-rw-rw-   0        0        0     2463 2023-04-07 07:52:41.518279 water-pipe-0.0.3/PKG-INFO
+-rw-rw-rw-   0        0        0     1740 2023-04-04 08:32:11.000000 water-pipe-0.0.3/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 07:52:41.520280 water-pipe-0.0.3/setup.cfg
+-rw-rw-rw-   0        0        0     3754 2023-04-03 07:53:03.000000 water-pipe-0.0.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:52:41.380272 water-pipe-0.0.3/water_pipe/
+-rw-rw-rw-   0        0        0      219 2023-04-04 09:09:19.000000 water-pipe-0.0.3/water_pipe/__init__.py
+-rw-rw-rw-   0        0        0      693 2023-04-04 09:56:12.000000 water-pipe-0.0.3/water_pipe/__version__.py
+-rw-rw-rw-   0        0        0      849 2023-04-03 07:53:03.000000 water-pipe-0.0.3/water_pipe/base.py
+-rw-rw-rw-   0        0        0     4464 2023-04-04 01:46:11.000000 water-pipe-0.0.3/water_pipe/channel.py
+-rw-rw-rw-   0        0        0     2592 2023-04-04 07:28:39.000000 water-pipe-0.0.3/water_pipe/db_csv.py
+-rw-rw-rw-   0        0        0       16 2023-04-03 07:53:03.000000 water-pipe-0.0.3/water_pipe/db_excel.py
+-rw-rw-rw-   0        0        0        0 2023-04-03 07:53:03.000000 water-pipe-0.0.3/water_pipe/db_greenplum.py
+-rw-rw-rw-   0        0        0      253 2023-04-04 01:24:09.000000 water-pipe-0.0.3/water_pipe/db_hive.py
+-rw-rw-rw-   0        0        0     5272 2023-04-04 07:28:15.000000 water-pipe-0.0.3/water_pipe/db_impala.py
+-rw-rw-rw-   0        0        0     5515 2023-04-04 07:28:08.000000 water-pipe-0.0.3/water_pipe/db_mysql.py
+-rw-rw-rw-   0        0        0     6363 2023-04-04 03:14:13.000000 water-pipe-0.0.3/water_pipe/db_postgres.py
+drwxrwxrwx   0        0        0        0 2023-04-07 07:52:41.515279 water-pipe-0.0.3/water_pipe.egg-info/
+-rw-rw-rw-   0        0        0     2463 2023-04-07 07:52:39.000000 water-pipe-0.0.3/water_pipe.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      463 2023-04-07 07:52:39.000000 water-pipe-0.0.3/water_pipe.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 07:52:39.000000 water-pipe-0.0.3/water_pipe.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 07:52:39.000000 water-pipe-0.0.3/water_pipe.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-07 07:52:39.000000 water-pipe-0.0.3/water_pipe.egg-info/top_level.txt
```

### Comparing `water-pipe-0.0.2/LICENSE` & `water-pipe-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `water-pipe-0.0.2/setup.py` & `water-pipe-0.0.3/setup.py`

 * *Files identical despite different names*

### Comparing `water-pipe-0.0.2/water_pipe/base.py` & `water-pipe-0.0.3/water_pipe/base.py`

 * *Files identical despite different names*

### Comparing `water-pipe-0.0.2/water_pipe/channel.py` & `water-pipe-0.0.3/water_pipe/channel.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,59 +1,60 @@
 from datetime import datetime
 from loguru import logger
 
+
 class DataChannel:
-    
+
     def __init__(self, source_config, sink_config):
         # driver_map = {
         #     # "mysql": MySQLdb.connect(**sink_config.config),
         #     "oracle": "cx_Oracle.connect()",
         #     # "mssql": pymssql.connect(**source_config.config),
         #     # "postgres": psycopg2.connect(**source_config["config"]),
         #     "postgres": PostgresConnect,
         #     # "hive": hive.connect(**source_config["config"]),
         #     "impala": ImpalaConnect,
         # }
-        
+
         # 动态导入, 主要是避免安装所有数据库的依赖包, 用什么数据库安装什么数据库即可
         self.source_driver = source_config["driver"]
         self.sink_driver = sink_config["driver"]
-        source_model = __import__(f"db_{self.source_driver}")
-        sink_model = __import__(f"db_{self.sink_driver}")
-        source_class = getattr(source_model, self.source_driver.capitalize() + "Connect")
-        sink_class = getattr(sink_model, self.sink_driver.capitalize() + "Connect")
+        source_module = __import__(f"water_pipe.db_{self.source_driver}", fromlist=[f"db_{self.source_driver}"])
+        sink_module = __import__(f"water_pipe.db_{self.sink_driver}", fromlist=[f"db_{self.sink_driver}"])
+        source_class = getattr(source_module, self.source_driver.capitalize() + "Connect")
+        sink_class = getattr(sink_module, self.sink_driver.capitalize() + "Connect")
 
         self.source_db = source_class(source_config["config"])
         self.sink_db = sink_class(sink_config["config"])
         self.dataset = []
         self.start_time = datetime.now()
         # print(self.start_time)  # __init__ 比 __enter__ 优先执行
-        
+
     def source_execute(self, sql):
         logger.info("source db execute: " + sql)
         self.source_db.execute(sql)
 
     def sink_execute(self, sql):
         logger.info("sink db execute: " + sql)
         self.sink_db.execute(sql)
-    
+
     def query(self, sql=None):
         self.dataset = self.source_db.query(sql)
         self.sink_db.std_schema_data = self.source_db.std_schema_data
         self.sink_db.dataset_comment = self.source_db.dataset_comment
         self.sink_db.placeholders = self.source_db.placeholders
-    
+
     def table(self, table_name):
         self.dataset = self.source_db.table(table_name)
         self.sink_db.std_schema_data = self.source_db.std_schema_data
         self.sink_db.dataset_comment = self.source_db.dataset_comment
         self.sink_db.placeholders = self.source_db.placeholders
-    
+
     def insert(self, sink_table=None, batch_size=1000, is_create=False, header=True):
-        
+
         if is_create:
             if self.sink_driver in ["csv", "excel"]:
                 self.sink_db.create_table(header=header)
             else:
                 self.sink_db.create_table(sink_table)
 
         i = 0
@@ -65,24 +66,24 @@
                 n = len(data)
                 j = i + n
 
                 if self.sink_driver in ["csv", "excel"]:
                     self.sink_db.insert(data)
                 else:
                     self.sink_db.insert(sink_table, data)
-                    
+
                 elapsed_time = datetime.now() - start_time
                 duration = 1 if elapsed_time.seconds == 0 else elapsed_time.seconds
                 speed = int(j / duration)
                 # progress = "{:.2f}".format(j / row_count * 100)
                 logger.info(f"insert into {sink_table} {j} data succeed, speed {speed} records/s, elapsed time {elapsed_time}")
                 i += n
             else:
                 break
-            
+
     def __enter__(self):
         logger.debug("init at " + str(datetime.now()))
         return self
 
     def __exit__(self, exc_type, exc_val, exc_tb):
         if hasattr(self.source_db, "cursor") and self.source_db.cursor:
             self.source_db.cursor.close()
@@ -94,8 +95,8 @@
             self.source_db.connect.commit()
             self.source_db.connect.close()
             logger.debug(str(self.source_db.connect) + " connect closed")
         if hasattr(self.sink_db, "connect") and self.sink_db.connect:
             self.sink_db.connect.commit()
             self.sink_db.connect.close()
             logger.debug(str(self.sink_db.connect) + " connect closed")
-        logger.info(f"Total time: {datetime.now() - self.start_time}s")
+        logger.info(f"Total time: {datetime.now() - self.start_time}s")
```

### Comparing `water-pipe-0.0.2/water_pipe/db_csv.py` & `water-pipe-0.0.3/water_pipe/db_csv.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 import csv
 from pathlib import Path
 
-from base import Connect, DTYPE
+from water_pipe.base import Connect, DTYPE
 
 class CsvConnect(Connect):
     def __init__(self, norm_config) -> None:
         """
         norm_config = {
             "path": "/home/",
             "filename": "data",
             "separator": ",",
             "quoting": "",  # 
             ......
         }
         """
-        config = norm_config
+        config = norm_config.copy()
         
         # self.connect = None
         self.cursor = None
         
         self.std_schema_data = []
         self.dataset_comment = ""
         self.placeholders = ""
```

### Comparing `water-pipe-0.0.2/water_pipe/db_impala.py` & `water-pipe-0.0.3/water_pipe/db_impala.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,26 +1,27 @@
-from base import Connect, DTYPE
 from impala import dbapi
 from itertools import chain
 import re
 
+from water_pipe.base import Connect, DTYPE
+
 class ImpalaConnect(Connect):
 
     def __init__(self, norm_config) -> None:
         """
         norm_config = {
             "host": "127.0.0.1",
             "username": "admin",
             "password": "admin123",
             "database": "test",
             "port": 5432,
             ......
         }
         """
-        config = norm_config
+        config = norm_config.copy()
         config["user"] = norm_config.pop("username")
 
         self.connect = dbapi.connect(**config)
         self.cursor = self.connect.cursor()
 
         self.std_schema_data = []
         self.dataset_comment = ""
```

### Comparing `water-pipe-0.0.2/water_pipe/db_mysql.py` & `water-pipe-0.0.3/water_pipe/db_mysql.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 from itertools import chain
-from base import Connect, DTYPE
 import MySQLdb
 
+from water_pipe.base import Connect, DTYPE
+
 class MysqlConnect(Connect):
         
     def __init__(self, norm_config) -> None:
         """
         norm_config = {
             "host": "127.0.0.1",
             "username": "admin",
             "password": "admin123",
             "database": "test",
             "port": 3306,
             ......
         }
         """
-        config = norm_config
+        config = norm_config.copy()
         config["user"] = norm_config.pop("username")
         
         self.connect = MySQLdb.connect(**config)
         self.cursor = self.connect.cursor()
         
         self.std_schema_data = []
         self.dataset_comment = ""
```

### Comparing `water-pipe-0.0.2/water_pipe/db_postgres.py` & `water-pipe-0.0.3/water_pipe/db_postgres.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 from itertools import chain
-from base import Connect, DTYPE
 import psycopg2
 import re
 
+from water_pipe.base import Connect, DTYPE
+
 class PostgresConnect(Connect):
     
     def __init__(self, norm_config) -> None:
         """
         norm_config = {
             "host": "127.0.0.1",
             "username": "admin",
             "password": "admin123",
             "database": "test",
             "port": 5432,
             ......
         }
         """
-        config = norm_config
-        config["user"] = norm_config.pop("username")
+        config = norm_config.copy()
+        config["user"] = config.pop("username")
         
         self.connect = psycopg2.connect(**config)
         self.cursor = self.connect.cursor()
         
         self.std_schema_data = []
         self.dataset_comment = ""
         self.placeholders = ""
```

