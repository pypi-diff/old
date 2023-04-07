# Comparing `tmp/squad_ds_utils-0.1.2.tar.gz` & `tmp/squad_ds_utils-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "squad_ds_utils-0.1.2.tar", max compression
+gzip compressed data, was "squad_ds_utils-0.1.3.tar", max compression
```

## Comparing `squad_ds_utils-0.1.2.tar` & `squad_ds_utils-0.1.3.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0        0 2023-03-29 09:21:34.776499 squad_ds_utils-0.1.2/README.md
--rw-r--r--   0        0        0      362 2023-03-29 11:04:26.185442 squad_ds_utils-0.1.2/pyproject.toml
--rw-r--r--   0        0        0        0 2023-03-29 09:21:34.776499 squad_ds_utils-0.1.2/squad_ds_utils/__init__.py
--rw-r--r--   0        0        0       40 2023-03-29 09:21:34.776499 squad_ds_utils-0.1.2/squad_ds_utils/exceptions.py
--rw-r--r--   0        0        0     2321 2023-03-29 11:03:54.293222 squad_ds_utils-0.1.2/squad_ds_utils/recordings_fetcher.py
--rw-r--r--   0        0        0      628 2023-03-29 09:21:34.776499 squad_ds_utils-0.1.2/squad_ds_utils/secrets.py
--rw-r--r--   0        0        0      636 1970-01-01 00:00:00.000000 squad_ds_utils-0.1.2/setup.py
--rw-r--r--   0        0        0      582 1970-01-01 00:00:00.000000 squad_ds_utils-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0        0 2023-04-07 11:48:06.845887 squad_ds_utils-0.1.3/README.md
+-rw-r--r--   0        0        0      362 2023-04-07 11:55:37.460758 squad_ds_utils-0.1.3/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-07 11:48:06.846392 squad_ds_utils-0.1.3/squad_ds_utils/__init__.py
+-rw-r--r--   0        0        0       40 2023-04-07 11:48:06.846491 squad_ds_utils-0.1.3/squad_ds_utils/exceptions.py
+-rw-r--r--   0        0        0      563 2023-04-07 11:57:21.111450 squad_ds_utils-0.1.3/squad_ds_utils/parse.py
+-rw-r--r--   0        0        0     2321 2023-04-07 11:48:06.846610 squad_ds_utils-0.1.3/squad_ds_utils/recordings_fetcher.py
+-rw-r--r--   0        0        0      628 2023-04-07 11:48:06.846724 squad_ds_utils-0.1.3/squad_ds_utils/secrets.py
+-rw-r--r--   0        0        0      582 1970-01-01 00:00:00.000000 squad_ds_utils-0.1.3/PKG-INFO
```

### Comparing `squad_ds_utils-0.1.2/squad_ds_utils/recordings_fetcher.py` & `squad_ds_utils-0.1.3/squad_ds_utils/recordings_fetcher.py`

 * *Files identical despite different names*

### Comparing `squad_ds_utils-0.1.2/squad_ds_utils/secrets.py` & `squad_ds_utils-0.1.3/squad_ds_utils/secrets.py`

 * *Files identical despite different names*

### Comparing `squad_ds_utils-0.1.2/PKG-INFO` & `squad_ds_utils-0.1.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: squad-ds-utils
-Version: 0.1.2
+Version: 0.1.3
 Summary: 
 Author: Ayush Shanker
 Author-email: ayush+pypi@squadstack.com
 Requires-Python: >=3.7,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
```

