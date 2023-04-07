# Comparing `tmp/manage-fields-0.0.2.tar.gz` & `tmp/manage-fields-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "manage-fields-0.0.2.tar", last modified: Fri Apr  7 14:26:57 2023, max compression
+gzip compressed data, was "manage-fields-0.0.3.tar", last modified: Fri Apr  7 14:32:17 2023, max compression
```

## Comparing `manage-fields-0.0.2.tar` & `manage-fields-0.0.3.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:26:57.939703 manage-fields-0.0.2/
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      878 2023-04-07 14:26:57.939703 manage-fields-0.0.2/PKG-INFO
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      345 2023-04-07 14:21:17.000000 manage-fields-0.0.2/README.md
-drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:26:57.939703 manage-fields-0.0.2/manage_fields/
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/__init__.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/admin.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      157 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/apps.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      899 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/mixins.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       57 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/models.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       60 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/tests.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/views.py
-drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:26:57.939703 manage-fields-0.0.2/manage_fields.egg-info/
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      878 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/PKG-INFO
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      367 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/SOURCES.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        1 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/dependency_links.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       27 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/requires.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       14 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/top_level.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       38 2023-04-07 14:26:57.943703 manage-fields-0.0.2/setup.cfg
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      962 2023-04-07 14:25:01.000000 manage-fields-0.0.2/setup.py
+drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:32:17.578091 manage-fields-0.0.3/
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      971 2023-04-07 14:32:17.578091 manage-fields-0.0.3/PKG-INFO
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      438 2023-04-07 14:30:53.000000 manage-fields-0.0.3/README.md
+drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:32:17.574091 manage-fields-0.0.3/manage_fields/
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/__init__.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/admin.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      157 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/apps.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      899 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/mixins.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       57 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/models.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       60 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/tests.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-04-07 13:59:03.000000 manage-fields-0.0.3/manage_fields/views.py
+drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:32:17.578091 manage-fields-0.0.3/manage_fields.egg-info/
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      971 2023-04-07 14:32:17.000000 manage-fields-0.0.3/manage_fields.egg-info/PKG-INFO
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      367 2023-04-07 14:32:17.000000 manage-fields-0.0.3/manage_fields.egg-info/SOURCES.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        1 2023-04-07 14:32:17.000000 manage-fields-0.0.3/manage_fields.egg-info/dependency_links.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       27 2023-04-07 14:32:17.000000 manage-fields-0.0.3/manage_fields.egg-info/requires.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       14 2023-04-07 14:32:17.000000 manage-fields-0.0.3/manage_fields.egg-info/top_level.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       38 2023-04-07 14:32:17.578091 manage-fields-0.0.3/setup.cfg
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      962 2023-04-07 14:31:05.000000 manage-fields-0.0.3/setup.py
```

### Comparing `manage-fields-0.0.2/PKG-INFO` & `manage-fields-0.0.3/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manage-fields
-Version: 0.0.2
+Version: 0.0.3
 Summary: Manage fields by request params
 Author: Maxmudov Asliddin
 Author-email: <asliddin750750@gmail.com>
 Keywords: python,field,serializer,manage fields
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
@@ -21,21 +21,25 @@
     ...,
     'manage_fields'
 ]
 ```
 
 **views.py**
 ```pycon
+from manage_fields.mixins import MFViewMixin
+
 class MyView(MFViewMixin, ...):
     serializer_class = MySerializer
     ....
 ```
 
 **serializers.py**
 ```pycon
+from manage_fields.mixins import MFSerializer
+
 class MySerializer(MFSerializer, ...):
     ...
 ```
 
 **Request**
 ```text
 https://abcd.com/?allow_fields={id,name}
```

### Comparing `manage-fields-0.0.2/manage_fields/mixins.py` & `manage-fields-0.0.3/manage_fields/mixins.py`

 * *Files identical despite different names*

### Comparing `manage-fields-0.0.2/manage_fields.egg-info/PKG-INFO` & `manage-fields-0.0.3/manage_fields.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: manage-fields
-Version: 0.0.2
+Version: 0.0.3
 Summary: Manage fields by request params
 Author: Maxmudov Asliddin
 Author-email: <asliddin750750@gmail.com>
 Keywords: python,field,serializer,manage fields
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
@@ -21,21 +21,25 @@
     ...,
     'manage_fields'
 ]
 ```
 
 **views.py**
 ```pycon
+from manage_fields.mixins import MFViewMixin
+
 class MyView(MFViewMixin, ...):
     serializer_class = MySerializer
     ....
 ```
 
 **serializers.py**
 ```pycon
+from manage_fields.mixins import MFSerializer
+
 class MySerializer(MFSerializer, ...):
     ...
 ```
 
 **Request**
 ```text
 https://abcd.com/?allow_fields={id,name}
```

### Comparing `manage-fields-0.0.2/setup.py` & `manage-fields-0.0.3/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from setuptools import setup, find_packages
 
-VERSION = "0.0.2"
+VERSION = "0.0.3"
 DESCRIPTION = "Manage fields by request params"
 
 
 def read(f):
     return open(f, "r", encoding="utf-8").read()
```

