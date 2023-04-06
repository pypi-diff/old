# Comparing `tmp/nbdev-django-0.0.98.tar.gz` & `tmp/nbdev-django-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nbdev-django-0.0.98.tar", last modified: Wed Jun  1 02:13:14 2022, max compression
+gzip compressed data, was "nbdev-django-0.0.99.tar", last modified: Wed Jun  1 13:56:02 2022, max compression
```

## Comparing `nbdev-django-0.0.98.tar` & `nbdev-django-0.0.99.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 02:13:14.442519 nbdev-django-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-01 01:37:00.000000 nbdev-django-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-01 01:37:00.000000 nbdev-django-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-01 02:13:14.442519 nbdev-django-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-01 01:37:00.000000 nbdev-django-0.0.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 02:13:14.442519 nbdev-django-0.0.98/nbdev_django/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   352420 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django/_modidx.py
--rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django/_nbdev.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 02:13:14.442519 nbdev-django-0.0.98/nbdev_django.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      376 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       47 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       13 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/nbdev_django.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      533 2022-06-01 02:13:14.000000 nbdev-django-0.0.98/settings.ini
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-01 02:13:14.442519 nbdev-django-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-01 01:37:00.000000 nbdev-django-0.0.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:56:02.645723 nbdev-django-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-06-01 13:20:01.000000 nbdev-django-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      111 2022-06-01 13:20:01.000000 nbdev-django-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-01 13:56:02.641723 nbdev-django-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)       67 2022-06-01 13:20:01.000000 nbdev-django-0.0.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:56:02.641723 nbdev-django-0.0.99/nbdev_django/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   352420 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django/_modidx.py
+-rw-r--r--   0 runner    (1001) docker     (121)      308 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django/_nbdev.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-01 13:56:02.641723 nbdev-django-0.0.99/nbdev_django.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      376 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       47 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       13 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/nbdev_django.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      533 2022-06-01 13:56:02.000000 nbdev-django-0.0.99/settings.ini
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-01 13:56:02.645723 nbdev-django-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2746 2022-06-01 13:20:01.000000 nbdev-django-0.0.99/setup.py
```

### Comparing `nbdev-django-0.0.98/LICENSE` & `nbdev-django-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `nbdev-django-0.0.98/PKG-INFO` & `nbdev-django-0.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-django
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for django
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-django-0.0.98/nbdev_django/_modidx.py` & `nbdev-django-0.0.99/nbdev_django/_modidx.py`

 * *Files identical despite different names*

### Comparing `nbdev-django-0.0.98/nbdev_django.egg-info/PKG-INFO` & `nbdev-django-0.0.99/nbdev_django.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nbdev-django
-Version: 0.0.98
+Version: 0.0.99
 Summary: nbdev docs lookup for django
 Home-page: https://github.com/fastai/nbdev-index/tree/master/
 Author: Jeremy Howard
 Author-email: info@fast.ai
 License: Apache Software License 2.0
 Keywords: nbdev fastai python
 Platform: UNKNOWN
```

### Comparing `nbdev-django-0.0.98/settings.ini` & `nbdev-django-0.0.99/settings.ini`

 * *Files 22% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 user = fastai
 description = nbdev docs lookup for django
 keywords = nbdev fastai python
 author = Jeremy Howard
 author_email = info@fast.ai
 copyright = fast.ai, inc
 branch = master
-version = 0.0.98
+version = 0.0.99
 min_python = 3.6
 audience = Developers
 language = English
 license = apache2
 status = 2
 lib_path = nbdev_django
 nbs_path = .
```

### Comparing `nbdev-django-0.0.98/setup.py` & `nbdev-django-0.0.99/setup.py`

 * *Files identical despite different names*

