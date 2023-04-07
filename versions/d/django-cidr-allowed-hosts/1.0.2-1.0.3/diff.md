# Comparing `tmp/django-cidr-allowed-hosts-1.0.2.tar.gz` & `tmp/django-cidr-allowed-hosts-1.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-cidr-allowed-hosts-1.0.2.tar", last modified: Fri Apr  7 12:17:01 2023, max compression
+gzip compressed data, was "django-cidr-allowed-hosts-1.0.3.tar", last modified: Fri Apr  7 12:17:47 2023, max compression
```

## Comparing `django-cidr-allowed-hosts-1.0.2.tar` & `django-cidr-allowed-hosts-1.0.3.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.221383 django-cidr-allowed-hosts-1.0.2/
--rw-r--r--   0 bwozniak   (501) staff       (20)     1073 2023-04-07 12:16:02.000000 django-cidr-allowed-hosts-1.0.2/LICENSE
--rw-r--r--   0 bwozniak   (501) staff       (20)     2388 2023-04-07 12:17:01.221237 django-cidr-allowed-hosts-1.0.2/PKG-INFO
--rw-r--r--   0 bwozniak   (501) staff       (20)     1470 2023-04-07 11:44:43.000000 django-cidr-allowed-hosts-1.0.2/README.rst
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.219985 django-cidr-allowed-hosts-1.0.2/cidr/
--rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:32:59.000000 django-cidr-allowed-hosts-1.0.2/cidr/__init__.py
--rw-r--r--   0 bwozniak   (501) staff       (20)       83 2023-04-06 20:49:57.000000 django-cidr-allowed-hosts-1.0.2/cidr/apps.py
--rw-r--r--   0 bwozniak   (501) staff       (20)     2753 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.2/cidr/middleware.py
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.220638 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/
--rw-r--r--   0 bwozniak   (501) staff       (20)     2388 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/PKG-INFO
--rw-r--r--   0 bwozniak   (501) staff       (20)      381 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/SOURCES.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)        1 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/dependency_links.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       12 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/requires.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       11 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/top_level.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       38 2023-04-07 12:17:01.221432 django-cidr-allowed-hosts-1.0.2/setup.cfg
--rw-r--r--   0 bwozniak   (501) staff       (20)     1102 2023-04-07 12:16:21.000000 django-cidr-allowed-hosts-1.0.2/setup.py
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.221024 django-cidr-allowed-hosts-1.0.2/tests/
--rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:29:46.000000 django-cidr-allowed-hosts-1.0.2/tests/__init__.py
--rw-r--r--   0 bwozniak   (501) staff       (20)      189 2023-04-06 20:42:12.000000 django-cidr-allowed-hosts-1.0.2/tests/settings.py
--rw-r--r--   0 bwozniak   (501) staff       (20)     4461 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.2/tests/test_middleware.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:47.955242 django-cidr-allowed-hosts-1.0.3/
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1073 2023-04-07 12:17:20.000000 django-cidr-allowed-hosts-1.0.3/LICENSE
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2388 2023-04-07 12:17:47.955117 django-cidr-allowed-hosts-1.0.3/PKG-INFO
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1470 2023-04-07 11:44:43.000000 django-cidr-allowed-hosts-1.0.3/README.rst
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:47.953887 django-cidr-allowed-hosts-1.0.3/cidr/
+-rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:32:59.000000 django-cidr-allowed-hosts-1.0.3/cidr/__init__.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)       83 2023-04-06 20:49:57.000000 django-cidr-allowed-hosts-1.0.3/cidr/apps.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2753 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.3/cidr/middleware.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:47.954501 django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2388 2023-04-07 12:17:47.000000 django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/PKG-INFO
+-rw-r--r--   0 bwozniak   (501) staff       (20)      381 2023-04-07 12:17:47.000000 django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/SOURCES.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)        1 2023-04-07 12:17:47.000000 django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/dependency_links.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       12 2023-04-07 12:17:47.000000 django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/requires.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       11 2023-04-07 12:17:47.000000 django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/top_level.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       38 2023-04-07 12:17:47.955279 django-cidr-allowed-hosts-1.0.3/setup.cfg
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1102 2023-04-07 12:17:43.000000 django-cidr-allowed-hosts-1.0.3/setup.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:47.954871 django-cidr-allowed-hosts-1.0.3/tests/
+-rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:29:46.000000 django-cidr-allowed-hosts-1.0.3/tests/__init__.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)      189 2023-04-06 20:42:12.000000 django-cidr-allowed-hosts-1.0.3/tests/settings.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)     4461 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.3/tests/test_middleware.py
```

### Comparing `django-cidr-allowed-hosts-1.0.2/LICENSE` & `django-cidr-allowed-hosts-1.0.3/LICENSE`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 MIT License
 
-Copyright (c) 2021 Bartosz Woźniak
+Copyright (c) 2023 Bartosz Woźniak
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
```

### Comparing `django-cidr-allowed-hosts-1.0.2/PKG-INFO` & `django-cidr-allowed-hosts-1.0.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-cidr-allowed-hosts
-Version: 1.0.2
+Version: 1.0.3
 Summary: Django middleware to allow access from specific CIDR ranges
 Home-page: https://github.com/wozniakpl/django-cidr-allowed-hosts.git
 Author: Barton Woźniak
 Author-email: bwozniakdev@protonmail.com
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.2
```

### Comparing `django-cidr-allowed-hosts-1.0.2/README.rst` & `django-cidr-allowed-hosts-1.0.3/README.rst`

 * *Files identical despite different names*

### Comparing `django-cidr-allowed-hosts-1.0.2/cidr/middleware.py` & `django-cidr-allowed-hosts-1.0.3/cidr/middleware.py`

 * *Files identical despite different names*

### Comparing `django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/PKG-INFO` & `django-cidr-allowed-hosts-1.0.3/django_cidr_allowed_hosts.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-cidr-allowed-hosts
-Version: 1.0.2
+Version: 1.0.3
 Summary: Django middleware to allow access from specific CIDR ranges
 Home-page: https://github.com/wozniakpl/django-cidr-allowed-hosts.git
 Author: Barton Woźniak
 Author-email: bwozniakdev@protonmail.com
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.2
```

### Comparing `django-cidr-allowed-hosts-1.0.2/setup.py` & `django-cidr-allowed-hosts-1.0.3/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name='django-cidr-allowed-hosts',
-    version='1.0.2',
+    version='1.0.3',
     description='Django middleware to allow access from specific CIDR ranges',
     long_description=open('README.rst').read(),
     url='https://github.com/wozniakpl/django-cidr-allowed-hosts.git',
     author="Barton Woźniak",
     author_email="bwozniakdev@protonmail.com",
     packages=find_packages(),
     install_requires=[
```

### Comparing `django-cidr-allowed-hosts-1.0.2/tests/test_middleware.py` & `django-cidr-allowed-hosts-1.0.3/tests/test_middleware.py`

 * *Files identical despite different names*

