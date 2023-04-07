# Comparing `tmp/pyg-sql-0.0.7.tar.gz` & `tmp/pyg-sql-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyg-sql-0.0.7.tar", last modified: Tue Jul 26 15:07:01 2022, max compression
+gzip compressed data, was "pyg-sql-0.0.8.tar", last modified: Tue Jul 26 15:27:00 2022, max compression
```

## Comparing `pyg-sql-0.0.7.tar` & `pyg-sql-0.0.8.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2022-07-26 15:07:01.881270 pyg-sql-0.0.7/
--rw-rw-rw-   0        0        0    35803 2022-07-21 07:45:10.000000 pyg-sql-0.0.7/LICENSE
--rw-rw-rw-   0        0        0    11160 2022-07-26 15:07:01.882060 pyg-sql-0.0.7/PKG-INFO
--rw-rw-rw-   0        0        0    10619 2022-07-21 07:45:10.000000 pyg-sql-0.0.7/README.md
--rw-rw-rw-   0        0        0      108 2022-07-21 07:45:10.000000 pyg-sql-0.0.7/pyproject.toml
--rw-rw-rw-   0        0        0      753 2022-07-26 15:07:01.884123 pyg-sql-0.0.7/setup.cfg
-drwxrwxrwx   0        0        0        0 2022-07-26 15:07:01.848460 pyg-sql-0.0.7/src/
-drwxrwxrwx   0        0        0        0 2022-07-26 15:07:01.857483 pyg-sql-0.0.7/src/pyg_sql/
--rw-rw-rw-   0        0        0       90 2022-07-25 15:39:26.000000 pyg-sql-0.0.7/src/pyg_sql/__init__.py
--rw-rw-rw-   0        0        0    51763 2022-07-26 15:06:17.000000 pyg-sql-0.0.7/src/pyg_sql/_sql_table.py
-drwxrwxrwx   0        0        0        0 2022-07-26 15:07:01.879950 pyg-sql-0.0.7/src/pyg_sql.egg-info/
--rw-rw-rw-   0        0        0    11160 2022-07-26 15:07:01.000000 pyg-sql-0.0.7/src/pyg_sql.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      266 2022-07-26 15:07:01.000000 pyg-sql-0.0.7/src/pyg_sql.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-07-26 15:07:01.000000 pyg-sql-0.0.7/src/pyg_sql.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       50 2022-07-26 15:07:01.000000 pyg-sql-0.0.7/src/pyg_sql.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2022-07-26 15:07:01.000000 pyg-sql-0.0.7/src/pyg_sql.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2022-07-26 15:27:00.852734 pyg-sql-0.0.8/
+-rw-rw-rw-   0        0        0    35803 2022-07-21 07:45:10.000000 pyg-sql-0.0.8/LICENSE
+-rw-rw-rw-   0        0        0    11160 2022-07-26 15:27:00.852734 pyg-sql-0.0.8/PKG-INFO
+-rw-rw-rw-   0        0        0    10619 2022-07-21 07:45:10.000000 pyg-sql-0.0.8/README.md
+-rw-rw-rw-   0        0        0      108 2022-07-21 07:45:10.000000 pyg-sql-0.0.8/pyproject.toml
+-rw-rw-rw-   0        0        0      753 2022-07-26 15:27:00.854725 pyg-sql-0.0.8/setup.cfg
+drwxrwxrwx   0        0        0        0 2022-07-26 15:27:00.819216 pyg-sql-0.0.8/src/
+drwxrwxrwx   0        0        0        0 2022-07-26 15:27:00.828736 pyg-sql-0.0.8/src/pyg_sql/
+-rw-rw-rw-   0        0        0       90 2022-07-25 15:39:26.000000 pyg-sql-0.0.8/src/pyg_sql/__init__.py
+-rw-rw-rw-   0        0        0    51852 2022-07-26 15:26:09.000000 pyg-sql-0.0.8/src/pyg_sql/_sql_table.py
+drwxrwxrwx   0        0        0        0 2022-07-26 15:27:00.851723 pyg-sql-0.0.8/src/pyg_sql.egg-info/
+-rw-rw-rw-   0        0        0    11160 2022-07-26 15:27:00.000000 pyg-sql-0.0.8/src/pyg_sql.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      266 2022-07-26 15:27:00.000000 pyg-sql-0.0.8/src/pyg_sql.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-07-26 15:27:00.000000 pyg-sql-0.0.8/src/pyg_sql.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       50 2022-07-26 15:27:00.000000 pyg-sql-0.0.8/src/pyg_sql.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2022-07-26 15:27:00.000000 pyg-sql-0.0.8/src/pyg_sql.egg-info/top_level.txt
```

### Comparing `pyg-sql-0.0.7/LICENSE` & `pyg-sql-0.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `pyg-sql-0.0.7/PKG-INFO` & `pyg-sql-0.0.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyg-sql
-Version: 0.0.7
+Version: 0.0.8
 Summary: pyg-sql implements a fully-featured no-sql document-store within sql.
 Home-page: https://github.com/gityoav/pyg-sql
 Author: Yoav Git
 Author-email: yoav.git@gmail.com
 Project-URL: Bug Tracker, https://github.com/gityoav/pyg-sql/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `pyg-sql-0.0.7/README.md` & `pyg-sql-0.0.8/README.md`

 * *Files identical despite different names*

### Comparing `pyg-sql-0.0.7/setup.cfg` & `pyg-sql-0.0.8/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2070 7967 2d73 716c 0d0a 7665 7273   = pyg-sql..vers
-00000020: 696f 6e20 3d20 302e 302e 370d 0a61 7574  ion = 0.0.7..aut
+00000020: 696f 6e20 3d20 302e 302e 380d 0a61 7574  ion = 0.0.8..aut
 00000030: 686f 7220 3d20 596f 6176 2047 6974 0d0a  hor = Yoav Git..
 00000040: 6175 7468 6f72 5f65 6d61 696c 203d 2079  author_email = y
 00000050: 6f61 762e 6769 7440 676d 6169 6c2e 636f  oav.git@gmail.co
 00000060: 6d0d 0a64 6573 6372 6970 7469 6f6e 203d  m..description =
 00000070: 2070 7967 2d73 716c 2069 6d70 6c65 6d65   pyg-sql impleme
 00000080: 6e74 7320 6120 6675 6c6c 792d 6665 6174  nts a fully-feat
 00000090: 7572 6564 206e 6f2d 7371 6c20 646f 6375  ured no-sql docu
```

### Comparing `pyg-sql-0.0.7/src/pyg_sql/_sql_table.py` & `pyg-sql-0.0.8/src/pyg_sql/_sql_table.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,18 @@
 _doc = 'doc'
 _root = 'root'
 _deleted = 'deleted'
 
 
 @cache
 def _servers():
-    return cfg_read().get('sql_server', {})
+    res = cfg_read().get('sql_server', {})
+    if isinstance(res, dict):
+        res[None] = res.get('null', None)
+    return res
 
 @cache
 def _schema():
     return cfg_read().get('sql_schema', None)
 
 @cache
 def _database():
```

### Comparing `pyg-sql-0.0.7/src/pyg_sql.egg-info/PKG-INFO` & `pyg-sql-0.0.8/src/pyg_sql.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyg-sql
-Version: 0.0.7
+Version: 0.0.8
 Summary: pyg-sql implements a fully-featured no-sql document-store within sql.
 Home-page: https://github.com/gityoav/pyg-sql
 Author: Yoav Git
 Author-email: yoav.git@gmail.com
 Project-URL: Bug Tracker, https://github.com/gityoav/pyg-sql/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

