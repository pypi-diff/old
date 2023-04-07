# Comparing `tmp/dbseeder-0.0.4.tar.gz` & `tmp/dbseeder-0.0.4.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dbseeder-0.0.4.tar", last modified: Fri Apr  7 13:46:10 2023, max compression
+gzip compressed data, was "dbseeder-0.0.4.3.tar", last modified: Fri Apr  7 14:52:18 2023, max compression
```

## Comparing `dbseeder-0.0.4.tar` & `dbseeder-0.0.4.3.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.302214 dbseeder-0.0.4/
--rw-rw-rw-   0        0        0     1086 2023-04-05 14:21:00.000000 dbseeder-0.0.4/LICENSE
--rw-rw-rw-   0        0        0     1599 2023-04-07 13:46:10.302214 dbseeder-0.0.4/PKG-INFO
--rw-rw-rw-   0        0        0     1050 2023-04-06 15:14:49.000000 dbseeder-0.0.4/README.md
--rw-rw-rw-   0        0        0      627 2023-04-07 13:45:48.000000 dbseeder-0.0.4/pyproject.toml
--rw-rw-rw-   0        0        0       42 2023-04-07 13:46:10.303213 dbseeder-0.0.4/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.277214 dbseeder-0.0.4/src/
-drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.289216 dbseeder-0.0.4/src/dbseeder/
--rw-rw-rw-   0        0        0       21 2023-04-07 13:35:06.000000 dbseeder-0.0.4/src/dbseeder/__init__.py
--rw-rw-rw-   0        0        0      247 2023-04-07 13:38:06.000000 dbseeder-0.0.4/src/dbseeder/__main__.py
--rw-rw-rw-   0        0        0     2104 2023-04-07 13:40:02.000000 dbseeder-0.0.4/src/dbseeder/database.py
--rw-rw-rw-   0        0        0     3137 2023-04-06 12:11:43.000000 dbseeder-0.0.4/src/dbseeder/fields.py
--rw-rw-rw-   0        0        0     1101 2023-04-07 13:40:41.000000 dbseeder-0.0.4/src/dbseeder/table.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.301213 dbseeder-0.0.4/src/dbseeder.egg-info/
--rw-rw-rw-   0        0        0     1599 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      314 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        9 2023-04-07 13:46:10.000000 dbseeder-0.0.4/src/dbseeder.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-07 13:46:10.301213 dbseeder-0.0.4/tests/
--rw-rw-rw-   0        0        0      167 2023-04-07 13:28:35.000000 dbseeder-0.0.4/tests/test_run.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:18.792925 dbseeder-0.0.4.3/
+-rw-rw-rw-   0        0        0     1086 2023-04-05 14:21:00.000000 dbseeder-0.0.4.3/LICENSE
+-rw-rw-rw-   0        0        0     1776 2023-04-07 14:52:18.791926 dbseeder-0.0.4.3/PKG-INFO
+-rw-rw-rw-   0        0        0     1225 2023-04-07 14:51:18.000000 dbseeder-0.0.4.3/README.md
+-rw-rw-rw-   0        0        0      629 2023-04-07 14:51:48.000000 dbseeder-0.0.4.3/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 14:52:18.792925 dbseeder-0.0.4.3/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:18.772926 dbseeder-0.0.4.3/src/
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:18.780926 dbseeder-0.0.4.3/src/dbseeder/
+-rw-rw-rw-   0        0        0       63 2023-04-07 14:03:45.000000 dbseeder-0.0.4.3/src/dbseeder/__init__.py
+-rw-rw-rw-   0        0        0     1000 2023-04-07 14:50:47.000000 dbseeder-0.0.4.3/src/dbseeder/__main__.py
+-rw-rw-rw-   0        0        0     2104 2023-04-07 13:40:02.000000 dbseeder-0.0.4.3/src/dbseeder/database.py
+-rw-rw-rw-   0        0        0     3137 2023-04-06 12:11:43.000000 dbseeder-0.0.4.3/src/dbseeder/fields.py
+-rw-rw-rw-   0        0        0     1101 2023-04-07 13:40:41.000000 dbseeder-0.0.4.3/src/dbseeder/table.py
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:18.790925 dbseeder-0.0.4.3/src/dbseeder.egg-info/
+-rw-rw-rw-   0        0        0     1776 2023-04-07 14:52:18.000000 dbseeder-0.0.4.3/src/dbseeder.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      314 2023-04-07 14:52:18.000000 dbseeder-0.0.4.3/src/dbseeder.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 14:52:18.000000 dbseeder-0.0.4.3/src/dbseeder.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        9 2023-04-07 14:52:18.000000 dbseeder-0.0.4.3/src/dbseeder.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 14:52:18.791926 dbseeder-0.0.4.3/tests/
+-rw-rw-rw-   0        0        0      167 2023-04-07 13:28:35.000000 dbseeder-0.0.4.3/tests/test_run.py
```

### Comparing `dbseeder-0.0.4/LICENSE` & `dbseeder-0.0.4.3/LICENSE`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.4/PKG-INFO` & `dbseeder-0.0.4.3/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbseeder
-Version: 0.0.4
+Version: 0.0.4.3
 Summary: A package to make seeds for some relational databases
 Author-email: Long Pham <phamlong15297@gmail.com>
 Project-URL: Homepage, https://github.com/conlacda/auto-seeder
 Project-URL: Bug Tracker, https://github.com/conlacda/auto-seeder/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
@@ -13,23 +13,33 @@
 License-File: LICENSE
 
 # Seeder for Mysql
 [![gh-action-pip-audit](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml/badge.svg)](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml)
 
 > Load database then make seeds for it
 
+## Install
+
+```shell
+$ pip install dbseeder
+```
+
 ## Usage
 ```python
 from dbseeder import Database
 db = Database(host="localhost", user="root", password="", database="seed")
 # Make seed without deleting the existence data
 db.makeSeed(rows_num=100000)
 # Delete data, then make seeds
 db.clearAndMakeSeed(rows_num=100000)
 ```
+OR
+```shell
+$ python -m dbseeder --host localhost --user root --password= --database seed --rows_num 100 --drop
+```
 
 ## TODO
 * Load relationship
 * Add test
 * Add argparser
 
 ## Test
```

### Comparing `dbseeder-0.0.4/README.md` & `dbseeder-0.0.4.3/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -1,21 +1,31 @@
 # Seeder for Mysql
 [![gh-action-pip-audit](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml/badge.svg)](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml)
 
 > Load database then make seeds for it
 
+## Install
+
+```shell
+$ pip install dbseeder
+```
+
 ## Usage
 ```python
 from dbseeder import Database
 db = Database(host="localhost", user="root", password="", database="seed")
 # Make seed without deleting the existence data
 db.makeSeed(rows_num=100000)
 # Delete data, then make seeds
 db.clearAndMakeSeed(rows_num=100000)
 ```
+OR
+```shell
+$ python -m dbseeder --host localhost --user root --password= --database seed --rows_num 100 --drop
+```
 
 ## TODO
 * Load relationship
 * Add test
 * Add argparser
 
 ## Test
```

### Comparing `dbseeder-0.0.4/pyproject.toml` & `dbseeder-0.0.4.3/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "dbseeder"
-version = "0.0.4"
+version = "0.0.4.3"
 authors = [
   { name="Long Pham", email="phamlong15297@gmail.com" },
 ]
 description = "A package to make seeds for some relational databases"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `dbseeder-0.0.4/src/dbseeder/database.py` & `dbseeder-0.0.4.3/src/dbseeder/database.py`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.4/src/dbseeder/fields.py` & `dbseeder-0.0.4.3/src/dbseeder/fields.py`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.4/src/dbseeder/table.py` & `dbseeder-0.0.4.3/src/dbseeder/table.py`

 * *Files identical despite different names*

### Comparing `dbseeder-0.0.4/src/dbseeder.egg-info/PKG-INFO` & `dbseeder-0.0.4.3/src/dbseeder.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbseeder
-Version: 0.0.4
+Version: 0.0.4.3
 Summary: A package to make seeds for some relational databases
 Author-email: Long Pham <phamlong15297@gmail.com>
 Project-URL: Homepage, https://github.com/conlacda/auto-seeder
 Project-URL: Bug Tracker, https://github.com/conlacda/auto-seeder/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
@@ -13,23 +13,33 @@
 License-File: LICENSE
 
 # Seeder for Mysql
 [![gh-action-pip-audit](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml/badge.svg)](https://github.com/conlacda/auto-seeder/actions/workflows/gh-action-pip-audit.yml)
 
 > Load database then make seeds for it
 
+## Install
+
+```shell
+$ pip install dbseeder
+```
+
 ## Usage
 ```python
 from dbseeder import Database
 db = Database(host="localhost", user="root", password="", database="seed")
 # Make seed without deleting the existence data
 db.makeSeed(rows_num=100000)
 # Delete data, then make seeds
 db.clearAndMakeSeed(rows_num=100000)
 ```
+OR
+```shell
+$ python -m dbseeder --host localhost --user root --password= --database seed --rows_num 100 --drop
+```
 
 ## TODO
 * Load relationship
 * Add test
 * Add argparser
 
 ## Test
```

