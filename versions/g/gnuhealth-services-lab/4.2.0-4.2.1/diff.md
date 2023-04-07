# Comparing `tmp/gnuhealth_services_lab-4.2.0.tar.gz` & `tmp/gnuhealth_services_lab-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_services_lab-4.2.0.tar", last modified: Sat Feb 11 21:57:50 2023, max compression
+gzip compressed data, was "gnuhealth_services_lab-4.2.1.tar", last modified: Fri Apr  7 10:19:49 2023, max compression
```

## Comparing `gnuhealth_services_lab-4.2.0.tar` & `gnuhealth_services_lab-4.2.1.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.955985 gnuhealth_services_lab-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_services_lab-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_services_lab-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5739 2023-02-11 21:57:50.955851 gnuhealth_services_lab-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1213 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.953676 gnuhealth_services_lab-4.2.0/data/
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.955084 gnuhealth_services_lab-4.2.0/data/messages/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      601 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/data/messages/messages.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.954550 gnuhealth_services_lab-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      474 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/doc/index.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      488 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/exceptions.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.955546 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5739 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)      887 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       76 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       47 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:57:50.000000 gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2712 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/health_services_lab.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1309 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/health_services_lab_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.954615 gnuhealth_services_lab-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2168 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.955632 gnuhealth_services_lab-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)        0 2023-01-08 17:59:28.000000 gnuhealth_services_lab-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:57:50.956018 gnuhealth_services_lab-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3700 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.954746 gnuhealth_services_lab-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      239 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      610 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/tests/test_health_services_lab.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      105 2023-02-11 12:44:33.000000 gnuhealth_services_lab-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.954883 gnuhealth_services_lab-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      673 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/view/gnuhealth_lab_request.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      558 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/view/gnuhealth_lab_start_request.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:50.955729 gnuhealth_services_lab-4.2.0/wizard/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)      364 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1159 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/wizard/create_health_service_invoice.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3603 2023-01-18 16:33:08.000000 gnuhealth_services_lab-4.2.0/wizard/wizard_health_services.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.989944 gnuhealth_services_lab-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_services_lab-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_services_lab-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5739 2023-04-07 10:19:49.989802 gnuhealth_services_lab-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1213 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.987518 gnuhealth_services_lab-4.2.1/data/
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.988998 gnuhealth_services_lab-4.2.1/data/messages/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      601 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/data/messages/messages.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.988446 gnuhealth_services_lab-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      474 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/doc/index.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      488 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/exceptions.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.989481 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5739 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)      887 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       76 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       47 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:49.000000 gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2712 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/health_services_lab.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1309 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/health_services_lab_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.988514 gnuhealth_services_lab-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2168 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.989571 gnuhealth_services_lab-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)        0 2023-01-08 17:59:28.000000 gnuhealth_services_lab-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:49.989997 gnuhealth_services_lab-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3700 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.988651 gnuhealth_services_lab-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      239 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      610 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/tests/test_health_services_lab.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      105 2023-04-07 09:37:21.000000 gnuhealth_services_lab-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.988790 gnuhealth_services_lab-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      673 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/view/gnuhealth_lab_request.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      558 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/view/gnuhealth_lab_start_request.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:49.989669 gnuhealth_services_lab-4.2.1/wizard/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)      364 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1159 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/wizard/create_health_service_invoice.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3603 2023-04-07 09:17:52.000000 gnuhealth_services_lab-4.2.1/wizard/wizard_health_services.py
```

### Comparing `gnuhealth_services_lab-4.2.0/COPYING` & `gnuhealth_services_lab-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/PKG-INFO` & `gnuhealth_services_lab-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_services_lab
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage Laboratoy associated services
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_services_lab-4.2.0/README.rst` & `gnuhealth_services_lab-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/__init__.py` & `gnuhealth_services_lab-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/data/messages/messages.xml` & `gnuhealth_services_lab-4.2.1/data/messages/messages.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/PKG-INFO` & `gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-services-lab
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage Laboratoy associated services
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_services_lab-4.2.0/gnuhealth_services_lab.egg-info/SOURCES.txt` & `gnuhealth_services_lab-4.2.1/gnuhealth_services_lab.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/health_services_lab.py` & `gnuhealth_services_lab-4.2.1/health_services_lab.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/health_services_lab_view.xml` & `gnuhealth_services_lab-4.2.1/health_services_lab_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/locale/zh_CN.po` & `gnuhealth_services_lab-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/setup.py` & `gnuhealth_services_lab-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/tests/test_health_services_lab.py` & `gnuhealth_services_lab-4.2.1/tests/test_health_services_lab.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/view/gnuhealth_lab_request.xml` & `gnuhealth_services_lab-4.2.1/view/gnuhealth_lab_request.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/view/gnuhealth_lab_start_request.xml` & `gnuhealth_services_lab-4.2.1/view/gnuhealth_lab_start_request.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/wizard/create_health_service_invoice.xml` & `gnuhealth_services_lab-4.2.1/wizard/create_health_service_invoice.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services_lab-4.2.0/wizard/wizard_health_services.py` & `gnuhealth_services_lab-4.2.1/wizard/wizard_health_services.py`

 * *Files identical despite different names*

