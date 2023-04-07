# Comparing `tmp/gnuhealth_federation-4.2.0.tar.gz` & `tmp/gnuhealth_federation-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_federation-4.2.0.tar", last modified: Sat Feb 11 21:55:33 2023, max compression
+gzip compressed data, was "gnuhealth_federation-4.2.1.tar", last modified: Fri Apr  7 10:17:37 2023, max compression
```

## Comparing `gnuhealth_federation-4.2.0.tar` & `gnuhealth_federation-4.2.1.tar`

### file list

```diff
@@ -1,41 +1,41 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.962178 gnuhealth_federation-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_federation-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:47.000000 gnuhealth_federation-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5802 2023-02-11 21:55:33.962030 gnuhealth_federation-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1732 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.960339 gnuhealth_federation-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1493 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/data/federation_objects.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      645 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/data/gnuhealth_commands.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.961245 gnuhealth_federation-4.2.0/data/messages/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1159 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/data/messages/messages.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.960411 gnuhealth_federation-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      324 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/doc/index.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      500 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/exceptions.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.961741 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5802 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1255 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       72 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:33.000000 gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    22588 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/health_federation.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6783 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/health_federation_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.960483 gnuhealth_federation-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     8502 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.960571 gnuhealth_federation-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1406 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:33.962218 gnuhealth_federation-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3662 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.960713 gnuhealth_federation-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      237 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      600 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/tests/test_health_federation.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      174 2023-02-11 12:44:33.000000 gnuhealth_federation-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:33.961134 gnuhealth_federation-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      872 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/view/gnuhealth_federation_config.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      401 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/view/gnuhealth_federation_config_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      412 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/view/gnuhealth_federation_object.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      316 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/view/gnuhealth_federation_object_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      801 2023-01-18 16:33:08.000000 gnuhealth_federation-4.2.0/view/gnuhealth_federation_queue.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      554 2023-01-18 16:33:07.000000 gnuhealth_federation-4.2.0/view/gnuhealth_federation_queue_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.156349 gnuhealth_federation-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_federation-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:47.000000 gnuhealth_federation-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5802 2023-04-07 10:17:37.156173 gnuhealth_federation-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1732 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.154523 gnuhealth_federation-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1493 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/data/federation_objects.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      645 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/data/gnuhealth_commands.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.155406 gnuhealth_federation-4.2.1/data/messages/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1159 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/data/messages/messages.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.154595 gnuhealth_federation-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      324 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/doc/index.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      500 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/exceptions.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.155887 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5802 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1255 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       72 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:37.000000 gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    22588 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/health_federation.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6783 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/health_federation_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.154664 gnuhealth_federation-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     8502 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.154735 gnuhealth_federation-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1406 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:37.156384 gnuhealth_federation-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3662 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.154880 gnuhealth_federation-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      237 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      600 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/tests/test_health_federation.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      174 2023-04-07 09:37:21.000000 gnuhealth_federation-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:37.155290 gnuhealth_federation-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      872 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/view/gnuhealth_federation_config.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      401 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/view/gnuhealth_federation_config_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      412 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/view/gnuhealth_federation_object.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      316 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/view/gnuhealth_federation_object_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      801 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/view/gnuhealth_federation_queue.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      554 2023-04-07 09:17:52.000000 gnuhealth_federation-4.2.1/view/gnuhealth_federation_queue_tree.xml
```

### Comparing `gnuhealth_federation-4.2.0/COPYING` & `gnuhealth_federation-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/PKG-INFO` & `gnuhealth_federation-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_federation
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Federation
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_federation-4.2.0/README.rst` & `gnuhealth_federation-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/__init__.py` & `gnuhealth_federation-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/data/federation_objects.xml` & `gnuhealth_federation-4.2.1/data/federation_objects.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/data/gnuhealth_commands.xml` & `gnuhealth_federation-4.2.1/data/gnuhealth_commands.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/data/messages/messages.xml` & `gnuhealth_federation-4.2.1/data/messages/messages.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/PKG-INFO` & `gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-federation
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Federation
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_federation-4.2.0/gnuhealth_federation.egg-info/SOURCES.txt` & `gnuhealth_federation-4.2.1/gnuhealth_federation.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/health_federation.py` & `gnuhealth_federation-4.2.1/health_federation.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/health_federation_view.xml` & `gnuhealth_federation-4.2.1/health_federation_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/locale/zh_CN.po` & `gnuhealth_federation-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/security/access_rights.xml` & `gnuhealth_federation-4.2.1/security/access_rights.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/setup.py` & `gnuhealth_federation-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/tests/test_health_federation.py` & `gnuhealth_federation-4.2.1/tests/test_health_federation.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/view/gnuhealth_federation_config.xml` & `gnuhealth_federation-4.2.1/view/gnuhealth_federation_config.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/view/gnuhealth_federation_queue.xml` & `gnuhealth_federation-4.2.1/view/gnuhealth_federation_queue.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_federation-4.2.0/view/gnuhealth_federation_queue_tree.xml` & `gnuhealth_federation-4.2.1/view/gnuhealth_federation_queue_tree.xml`

 * *Files identical despite different names*

