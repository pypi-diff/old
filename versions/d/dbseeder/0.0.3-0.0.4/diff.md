# Comparing `tmp/dbseeder-0.0.3.tar.gz` & `tmp/dbseeder-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dbseeder-0.0.3.tar", last modified: Fri Apr  7 13:16:59 2023, max compression
+gzip compressed data, was "dbseeder-0.0.4.tar", last modified: Fri Apr  7 13:46:10 2023, max compression
```

## Comparing `dbseeder-0.0.3.tar` & `dbseeder-0.0.4.tar`

### file list

```diff
@@ -1,18 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:16:59.659155 dbseeder-0.0.3/
--rw-rw-rw-   0        0        0     1086 2023-04-05 14:21:00.000000 dbseeder-0.0.3/LICENSE
--rw-rw-rw-   0        0        0     1599 2023-04-07 13:16:59.657822 dbseeder-0.0.3/PKG-INFO
--rw-rw-rw-   0        0        0     1050 2023-04-06 15:14:49.000000 dbseeder-0.0.3/README.md
--rw-rw-rw-   0        0        0      627 2023-04-07 13:16:14.000000 dbseeder-0.0.3/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 13:16:59.659155 dbseeder-0.0.3/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 13:16:59.641974 dbseeder-0.0.3/src/
--rw-rw-rw-   0        0        0       30 2023-04-07 12:43:03.000000 dbseeder-0.0.3/src/__init__.py
--rw-rw-rw-   0        0        0     2096 2023-04-07 12:42:14.000000 dbseeder-0.0.3/src/database.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:16:59.656821 dbseeder-0.0.3/src/dbseeder.egg-info/
--rw-rw-rw-   0        0        0     1599 2023-04-07 13:16:59.000000 dbseeder-0.0.3/src/dbseeder.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      253 2023-04-07 13:16:59.000000 dbseeder-0.0.3/src/dbseeder.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:16:59.000000 dbseeder-0.0.3/src/dbseeder.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       31 2023-04-07 13:16:59.000000 dbseeder-0.0.3/src/dbseeder.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     3137 2023-04-06 12:11:43.000000 dbseeder-0.0.3/src/fields.py
--rw-rw-rw-   0        0        0     1093 2023-04-07 12:42:26.000000 dbseeder-0.0.3/src/table.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:16:59.657822 dbseeder-0.0.3/tests/
--rw-rw-rw-   0        0        0      158 2023-04-07 12:40:20.000000 dbseeder-0.0.3/tests/test_run.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.302214 dbseeder-0.0.4/
+-rw-rw-rw-   0        0        0     1086 2023-04-05 14:21:00.000000 dbseeder-0.0.4/LICENSE
+-rw-rw-rw-   0        0        0     1599 2023-04-07 13:46:10.302214 dbseeder-0.0.4/PKG-INFO
+-rw-rw-rw-   0        0        0     1050 2023-04-06 15:14:49.000000 dbseeder-0.0.4/README.md
+-rw-rw-rw-   0        0        0      627 2023-04-07 13:45:48.000000 dbseeder-0.0.4/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:46:10.303213 dbseeder-0.0.4/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.277214 dbseeder-0.0.4/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.289216 dbseeder-0.0.4/src/dbseeder/
+-rw-rw-rw-   0        0        0       21 2023-04-07 13:35:06.000000 dbseeder-0.0.4/src/dbseeder/__init__.py
+-rw-rw-rw-   0        0        0      247 2023-04-07 13:38:06.000000 dbseeder-0.0.4/src/dbseeder/__main__.py
+-rw-rw-rw-   0        0        0     2104 2023-04-07 13:40:02.000000 dbseeder-0.0.4/src/dbseeder/database.py
+-rw-rw-rw-   0        0        0     3137 2023-04-06 12:11:43.000000 dbseeder-0.0.4/src/dbseeder/fields.py
+-rw-rw-rw-   0        0        0     1101 2023-04-07 13:40:41.000000 dbseeder-0.0.4/src/dbseeder/table.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.301213 dbseeder-0.0.4/src/dbseeder.egg-info/
+-rw-rw-rw-   0        0        0     1599 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      314 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        9 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.301213 dbseeder-0.0.4/tests/
+-rw-rw-rw-   0        0        0      167 2023-04-07 13:28:35.000000 dbseeder-0.0.4/tests/test_run.py
```

### Comparing `dbseeder-0.0.3/LICENSE` & `dbseeder-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.3/PKG-INFO` & `dbseeder-0.0.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbseeder
-Version: 0.0.3
+Version: 0.0.4
 Summary: A package to make seeds for some relational databases
 Author-email: Long Pham <phamlong15297@gmail.com>
 Project-URL: Homepage, https://github.com/conlacda/auto-seeder
 Project-URL: Bug Tracker, https://github.com/conlacda/auto-seeder/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `dbseeder-0.0.3/README.md` & `dbseeder-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.3/pyproject.toml` & `dbseeder-0.0.4/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "dbseeder"
-version = "0.0.3"
+version = "0.0.4"
 authors = [
   { name="Long Pham", email="phamlong15297@gmail.com" },
 ]
 description = "A package to make seeds for some relational databases"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `dbseeder-0.0.3/src/database.py` & `dbseeder-0.0.4/src/dbseeder/database.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import mysql.connector
 from tqdm import tqdm
 
-from .table import Table
+from dbseeder.table import Table
 
 
 class Database:
     db = None
     tables = []
     batchSize = 100
     failed_query_num = 0
```

### Comparing `dbseeder-0.0.3/src/dbseeder.egg-info/PKG-INFO` & `dbseeder-0.0.4/src/dbseeder.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbseeder
-Version: 0.0.3
+Version: 0.0.4
 Summary: A package to make seeds for some relational databases
 Author-email: Long Pham <phamlong15297@gmail.com>
 Project-URL: Homepage, https://github.com/conlacda/auto-seeder
 Project-URL: Bug Tracker, https://github.com/conlacda/auto-seeder/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `dbseeder-0.0.3/src/fields.py` & `dbseeder-0.0.4/src/dbseeder/fields.py`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.3/src/table.py` & `dbseeder-0.0.4/src/dbseeder/table.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from dataclasses import dataclass, field
-from .fields import Field
+from dbseeder.fields import Field
 
 
 @dataclass
 class Table:
     name: str = ""
     fields: list = field(default_factory=list)
     ignore_fields = ["id"]
```

