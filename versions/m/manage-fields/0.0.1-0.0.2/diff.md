# Comparing `tmp/manage-fields-0.0.1.tar.gz` & `tmp/manage-fields-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "manage-fields-0.0.1.tar", last modified: Mon Mar 20 10:50:38 2023, max compression
+gzip compressed data, was "manage-fields-0.0.2.tar", last modified: Fri Apr  7 14:26:57 2023, max compression
```

## Comparing `manage-fields-0.0.1.tar` & `manage-fields-0.0.2.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-03-20 10:50:38.602978 manage-fields-0.0.1/
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      593 2023-03-20 10:50:38.602978 manage-fields-0.0.1/PKG-INFO
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       15 2023-03-20 10:45:39.000000 manage-fields-0.0.1/README.md
-drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-03-20 10:50:38.602978 manage-fields-0.0.1/manage_fields/
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        0 2023-03-20 10:38:56.000000 manage-fields-0.0.1/manage_fields/__init__.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-03-20 10:38:56.000000 manage-fields-0.0.1/manage_fields/admin.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      157 2023-03-20 10:38:56.000000 manage-fields-0.0.1/manage_fields/apps.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      899 2023-03-20 10:40:39.000000 manage-fields-0.0.1/manage_fields/mixins.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       57 2023-03-20 10:38:56.000000 manage-fields-0.0.1/manage_fields/models.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       60 2023-03-20 10:38:56.000000 manage-fields-0.0.1/manage_fields/tests.py
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-03-20 10:38:56.000000 manage-fields-0.0.1/manage_fields/views.py
-drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-03-20 10:50:38.602978 manage-fields-0.0.1/manage_fields.egg-info/
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      593 2023-03-20 10:50:38.000000 manage-fields-0.0.1/manage_fields.egg-info/PKG-INFO
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      367 2023-03-20 10:50:38.000000 manage-fields-0.0.1/manage_fields.egg-info/SOURCES.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        1 2023-03-20 10:50:38.000000 manage-fields-0.0.1/manage_fields.egg-info/dependency_links.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       27 2023-03-20 10:50:38.000000 manage-fields-0.0.1/manage_fields.egg-info/requires.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       14 2023-03-20 10:50:38.000000 manage-fields-0.0.1/manage_fields.egg-info/top_level.txt
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       38 2023-03-20 10:50:38.602978 manage-fields-0.0.1/setup.cfg
--rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      952 2023-03-20 10:46:42.000000 manage-fields-0.0.1/setup.py
+drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:26:57.939703 manage-fields-0.0.2/
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      878 2023-04-07 14:26:57.939703 manage-fields-0.0.2/PKG-INFO
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      345 2023-04-07 14:21:17.000000 manage-fields-0.0.2/README.md
+drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:26:57.939703 manage-fields-0.0.2/manage_fields/
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/__init__.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/admin.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      157 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/apps.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      899 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/mixins.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       57 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/models.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       60 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/tests.py
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       63 2023-04-07 13:59:03.000000 manage-fields-0.0.2/manage_fields/views.py
+drwxrwxr-x   0 asliddin  (1000) asliddin  (1000)        0 2023-04-07 14:26:57.939703 manage-fields-0.0.2/manage_fields.egg-info/
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      878 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/PKG-INFO
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      367 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/SOURCES.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)        1 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/dependency_links.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       27 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/requires.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       14 2023-04-07 14:26:57.000000 manage-fields-0.0.2/manage_fields.egg-info/top_level.txt
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)       38 2023-04-07 14:26:57.943703 manage-fields-0.0.2/setup.cfg
+-rw-rw-r--   0 asliddin  (1000) asliddin  (1000)      962 2023-04-07 14:25:01.000000 manage-fields-0.0.2/setup.py
```

### Comparing `manage-fields-0.0.1/manage_fields/mixins.py` & `manage-fields-0.0.2/manage_fields/mixins.py`

 * *Files identical despite different names*

### Comparing `manage-fields-0.0.1/setup.py` & `manage-fields-0.0.2/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,32 +1,32 @@
 from setuptools import setup, find_packages
 
-VERSION = '0.0.1'
-DESCRIPTION = 'Manage fields package'
+VERSION = "0.0.2"
+DESCRIPTION = "Manage fields by request params"
 
 
 def read(f):
-    return open(f, 'r', encoding='utf-8').read()
+    return open(f, "r", encoding="utf-8").read()
 
 
 # Setting up
 setup(
     name="manage-fields",
     version=VERSION,
     author="Maxmudov Asliddin",
     author_email="<asliddin750750@gmail.com>",
     description=DESCRIPTION,
-    long_description=read('README.md'),
-    long_description_content_type='text/markdown',
+    long_description=read("README.md"),
+    long_description_content_type="text/markdown",
     packages=find_packages(include=[
-        'manage_fields'
+        "manage_fields"
     ]),
     include_package_data=True,
-    install_requires=['Django', 'djangorestframework'],
-    keywords=['python', 'field', 'serializer', 'manage fields'],
+    install_requires=["Django", "djangorestframework"],
+    keywords=["python", "field", "serializer", "manage fields"],
     classifiers=[
         "Development Status :: 1 - Planning",
         "Intended Audience :: Developers",
         "Programming Language :: Python :: 3",
         "Operating System :: Unix",
         "Operating System :: MacOS :: MacOS X",
         "Operating System :: Microsoft :: Windows",
```

