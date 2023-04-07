# Comparing `tmp/gnuhealth_orthanc-4.2.0.tar.gz` & `tmp/gnuhealth_orthanc-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_orthanc-4.2.0.tar", last modified: Sat Feb 11 21:57:16 2023, max compression
+gzip compressed data, was "gnuhealth_orthanc-4.2.1.tar", last modified: Fri Apr  7 10:19:18 2023, max compression
```

## Comparing `gnuhealth_orthanc-4.2.0.tar` & `gnuhealth_orthanc-4.2.1.tar`

### file list

```diff
@@ -1,42 +1,42 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.261864 gnuhealth_orthanc-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_orthanc-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       64 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5726 2023-02-11 21:57:16.261727 gnuhealth_orthanc-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1404 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.259825 gnuhealth_orthanc-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5712 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/data/data.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.261362 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5726 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1095 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       66 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       47 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:57:16.000000 gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    16367 2023-01-24 11:11:34.000000 gnuhealth_orthanc-4.2.0/health_orthanc.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5643 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/health_orthanc_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.259894 gnuhealth_orthanc-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1767 2022-11-28 22:17:48.000000 gnuhealth_orthanc-4.2.0/icons/orthanc_logo.svg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.260029 gnuhealth_orthanc-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9612 2022-11-28 22:17:48.000000 gnuhealth_orthanc-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9686 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:57:16.261900 gnuhealth_orthanc-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3741 2023-01-27 11:47:26.000000 gnuhealth_orthanc-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.260163 gnuhealth_orthanc-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      826 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1180 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/tests/test_health_orthanc.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      103 2023-02-11 12:44:33.000000 gnuhealth_orthanc-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.260748 gnuhealth_orthanc-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      688 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/add_orthanc_server.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      275 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/add_orthanc_server_result.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1330 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/config_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      430 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/config_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      457 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/imaging_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      958 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/patient_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      460 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/patient_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      812 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/study_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      514 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/view/study_tree.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:16.260880 gnuhealth_orthanc-4.2.0/wizard/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      290 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4097 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.0/wizard/wizard.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.463113 gnuhealth_orthanc-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_orthanc-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       64 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5726 2023-04-07 10:19:18.462972 gnuhealth_orthanc-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1404 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.461017 gnuhealth_orthanc-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5712 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/data/data.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.462621 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5726 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1095 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       66 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       47 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:18.000000 gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    16367 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/health_orthanc.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5643 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/health_orthanc_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.461091 gnuhealth_orthanc-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1767 2022-11-28 22:17:48.000000 gnuhealth_orthanc-4.2.1/icons/orthanc_logo.svg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.461230 gnuhealth_orthanc-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9612 2022-11-28 22:17:48.000000 gnuhealth_orthanc-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9686 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:18.463147 gnuhealth_orthanc-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3741 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.461370 gnuhealth_orthanc-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      826 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1180 2023-01-18 16:33:08.000000 gnuhealth_orthanc-4.2.1/tests/test_health_orthanc.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      103 2023-04-07 09:37:21.000000 gnuhealth_orthanc-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.461982 gnuhealth_orthanc-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      688 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/add_orthanc_server.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      275 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/add_orthanc_server_result.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1330 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/config_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      430 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/config_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      457 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/imaging_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      958 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/patient_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      460 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/patient_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      812 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/study_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      514 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/view/study_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:18.462116 gnuhealth_orthanc-4.2.1/wizard/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      290 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4097 2023-04-07 09:17:52.000000 gnuhealth_orthanc-4.2.1/wizard/wizard.py
```

### Comparing `gnuhealth_orthanc-4.2.0/COPYING` & `gnuhealth_orthanc-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/PKG-INFO` & `gnuhealth_orthanc-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_orthanc
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Orthanc PACS server integration package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_orthanc-4.2.0/README.rst` & `gnuhealth_orthanc-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/__init__.py` & `gnuhealth_orthanc-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/data/data.xml` & `gnuhealth_orthanc-4.2.1/data/data.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/PKG-INFO` & `gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-orthanc
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Orthanc PACS server integration package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_orthanc-4.2.0/gnuhealth_orthanc.egg-info/SOURCES.txt` & `gnuhealth_orthanc-4.2.1/gnuhealth_orthanc.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/health_orthanc.py` & `gnuhealth_orthanc-4.2.1/health_orthanc.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/health_orthanc_view.xml` & `gnuhealth_orthanc-4.2.1/health_orthanc_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/icons/orthanc_logo.svg` & `gnuhealth_orthanc-4.2.1/icons/orthanc_logo.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/locale/es.po` & `gnuhealth_orthanc-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/locale/zh_CN.po` & `gnuhealth_orthanc-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/setup.py` & `gnuhealth_orthanc-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/tests/__init__.py` & `gnuhealth_orthanc-4.2.1/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/tests/test_health_orthanc.py` & `gnuhealth_orthanc-4.2.1/tests/test_health_orthanc.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/view/add_orthanc_server.xml` & `gnuhealth_orthanc-4.2.1/view/add_orthanc_server.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/view/config_form.xml` & `gnuhealth_orthanc-4.2.1/view/config_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/view/patient_form.xml` & `gnuhealth_orthanc-4.2.1/view/patient_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/view/study_form.xml` & `gnuhealth_orthanc-4.2.1/view/study_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/view/study_tree.xml` & `gnuhealth_orthanc-4.2.1/view/study_tree.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_orthanc-4.2.0/wizard/wizard.py` & `gnuhealth_orthanc-4.2.1/wizard/wizard.py`

 * *Files identical despite different names*

