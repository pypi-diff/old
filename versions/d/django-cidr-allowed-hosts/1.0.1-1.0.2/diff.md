# Comparing `tmp/django-cidr-allowed-hosts-1.0.1.tar.gz` & `tmp/django-cidr-allowed-hosts-1.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-cidr-allowed-hosts-1.0.1.tar", last modified: Fri Apr  7 11:48:47 2023, max compression
+gzip compressed data, was "django-cidr-allowed-hosts-1.0.2.tar", last modified: Fri Apr  7 12:17:01 2023, max compression
```

## Comparing `django-cidr-allowed-hosts-1.0.1.tar` & `django-cidr-allowed-hosts-1.0.2.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.987681 django-cidr-allowed-hosts-1.0.1/
--rw-r--r--   0 bwozniak   (501) staff       (20)     1211 2023-04-07 10:22:22.000000 django-cidr-allowed-hosts-1.0.1/LICENSE
--rw-r--r--   0 bwozniak   (501) staff       (20)     2402 2023-04-07 11:48:47.987559 django-cidr-allowed-hosts-1.0.1/PKG-INFO
--rw-r--r--   0 bwozniak   (501) staff       (20)     1470 2023-04-07 11:44:43.000000 django-cidr-allowed-hosts-1.0.1/README.rst
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.986180 django-cidr-allowed-hosts-1.0.1/cidr/
--rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:32:59.000000 django-cidr-allowed-hosts-1.0.1/cidr/__init__.py
--rw-r--r--   0 bwozniak   (501) staff       (20)       83 2023-04-06 20:49:57.000000 django-cidr-allowed-hosts-1.0.1/cidr/apps.py
--rw-r--r--   0 bwozniak   (501) staff       (20)     2753 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.1/cidr/middleware.py
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.986967 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/
--rw-r--r--   0 bwozniak   (501) staff       (20)     2402 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/PKG-INFO
--rw-r--r--   0 bwozniak   (501) staff       (20)      381 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/SOURCES.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)        1 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/dependency_links.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       12 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/requires.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       11 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/top_level.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       38 2023-04-07 11:48:47.987725 django-cidr-allowed-hosts-1.0.1/setup.cfg
--rw-r--r--   0 bwozniak   (501) staff       (20)     1116 2023-04-07 11:48:28.000000 django-cidr-allowed-hosts-1.0.1/setup.py
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.987374 django-cidr-allowed-hosts-1.0.1/tests/
--rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:29:46.000000 django-cidr-allowed-hosts-1.0.1/tests/__init__.py
--rw-r--r--   0 bwozniak   (501) staff       (20)      189 2023-04-06 20:42:12.000000 django-cidr-allowed-hosts-1.0.1/tests/settings.py
--rw-r--r--   0 bwozniak   (501) staff       (20)     4461 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.1/tests/test_middleware.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.221383 django-cidr-allowed-hosts-1.0.2/
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1073 2023-04-07 12:16:02.000000 django-cidr-allowed-hosts-1.0.2/LICENSE
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2388 2023-04-07 12:17:01.221237 django-cidr-allowed-hosts-1.0.2/PKG-INFO
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1470 2023-04-07 11:44:43.000000 django-cidr-allowed-hosts-1.0.2/README.rst
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.219985 django-cidr-allowed-hosts-1.0.2/cidr/
+-rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:32:59.000000 django-cidr-allowed-hosts-1.0.2/cidr/__init__.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)       83 2023-04-06 20:49:57.000000 django-cidr-allowed-hosts-1.0.2/cidr/apps.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2753 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.2/cidr/middleware.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.220638 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2388 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/PKG-INFO
+-rw-r--r--   0 bwozniak   (501) staff       (20)      381 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/SOURCES.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)        1 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/dependency_links.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       12 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/requires.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       11 2023-04-07 12:17:01.000000 django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/top_level.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       38 2023-04-07 12:17:01.221432 django-cidr-allowed-hosts-1.0.2/setup.cfg
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1102 2023-04-07 12:16:21.000000 django-cidr-allowed-hosts-1.0.2/setup.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 12:17:01.221024 django-cidr-allowed-hosts-1.0.2/tests/
+-rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:29:46.000000 django-cidr-allowed-hosts-1.0.2/tests/__init__.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)      189 2023-04-06 20:42:12.000000 django-cidr-allowed-hosts-1.0.2/tests/settings.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)     4461 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.2/tests/test_middleware.py
```

### Comparing `django-cidr-allowed-hosts-1.0.1/PKG-INFO` & `django-cidr-allowed-hosts-1.0.2/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 Metadata-Version: 2.1
 Name: django-cidr-allowed-hosts
-Version: 1.0.1
+Version: 1.0.2
 Summary: Django middleware to allow access from specific CIDR ranges
 Home-page: https://github.com/wozniakpl/django-cidr-allowed-hosts.git
 Author: Barton Woźniak
 Author-email: bwozniakdev@protonmail.com
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.2
 Classifier: Framework :: Django :: 4.0
 Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: The Unlicense (Unlicense)
+Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
```

### Comparing `django-cidr-allowed-hosts-1.0.1/README.rst` & `django-cidr-allowed-hosts-1.0.2/README.rst`

 * *Files identical despite different names*

### Comparing `django-cidr-allowed-hosts-1.0.1/cidr/middleware.py` & `django-cidr-allowed-hosts-1.0.2/cidr/middleware.py`

 * *Files identical despite different names*

### Comparing `django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/PKG-INFO` & `django-cidr-allowed-hosts-1.0.2/django_cidr_allowed_hosts.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 Metadata-Version: 2.1
 Name: django-cidr-allowed-hosts
-Version: 1.0.1
+Version: 1.0.2
 Summary: Django middleware to allow access from specific CIDR ranges
 Home-page: https://github.com/wozniakpl/django-cidr-allowed-hosts.git
 Author: Barton Woźniak
 Author-email: bwozniakdev@protonmail.com
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.2
 Classifier: Framework :: Django :: 4.0
 Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: The Unlicense (Unlicense)
+Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
```

### Comparing `django-cidr-allowed-hosts-1.0.1/setup.py` & `django-cidr-allowed-hosts-1.0.2/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name='django-cidr-allowed-hosts',
-    version='1.0.1',
+    version='1.0.2',
     description='Django middleware to allow access from specific CIDR ranges',
     long_description=open('README.rst').read(),
     url='https://github.com/wozniakpl/django-cidr-allowed-hosts.git',
     author="Barton Woźniak",
     author_email="bwozniakdev@protonmail.com",
     packages=find_packages(),
     install_requires=[
@@ -14,15 +14,15 @@
     ],
     classifiers=[
         "Framework :: Django",
         "Framework :: Django :: 2.2",
         "Framework :: Django :: 3.2",
         "Framework :: Django :: 4.0",
         "Intended Audience :: Developers",
-        "License :: OSI Approved :: The Unlicense (Unlicense)",
+        "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Natural Language :: English",
         "Programming Language :: Python",
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
```

### Comparing `django-cidr-allowed-hosts-1.0.1/tests/test_middleware.py` & `django-cidr-allowed-hosts-1.0.2/tests/test_middleware.py`

 * *Files identical despite different names*

