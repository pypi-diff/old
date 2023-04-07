# Comparing `tmp/gnuhealth_iss-4.2.0.tar.gz` & `tmp/gnuhealth_iss-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_iss-4.2.0.tar", last modified: Sat Feb 11 21:56:47 2023, max compression
+gzip compressed data, was "gnuhealth_iss-4.2.1.tar", last modified: Fri Apr  7 10:18:48 2023, max compression
```

## Comparing `gnuhealth_iss-4.2.0.tar` & `gnuhealth_iss-4.2.1.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:47.251968 gnuhealth_iss-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_iss-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5717 2023-02-11 21:56:47.251828 gnuhealth_iss-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      947 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:47.251700 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5717 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)      615 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       58 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:56:47.000000 gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9910 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/health_iss.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2039 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/health_iss_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:47.250748 gnuhealth_iss-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    16001 2023-02-11 12:36:12.000000 gnuhealth_iss-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    15042 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    16870 2022-11-28 22:17:48.000000 gnuhealth_iss-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    15090 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    15029 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    13980 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    15233 2022-11-28 22:17:48.000000 gnuhealth_iss-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    12298 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    13669 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    13632 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:56:47.252003 gnuhealth_iss-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3571 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:47.250969 gnuhealth_iss-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      230 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      580 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/tests/test_health_iss.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       73 2023-02-11 12:44:33.000000 gnuhealth_iss-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:47.251174 gnuhealth_iss-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3010 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/view/health_iss_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      417 2023-01-18 16:33:08.000000 gnuhealth_iss-4.2.0/view/health_iss_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:48.200797 gnuhealth_iss-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_iss-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5717 2023-04-07 10:18:48.200654 gnuhealth_iss-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      947 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:48.200486 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5717 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)      615 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       58 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:18:48.000000 gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9910 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/health_iss.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2039 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/health_iss_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:48.199685 gnuhealth_iss-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    16001 2023-02-11 12:36:12.000000 gnuhealth_iss-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    15042 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    16870 2022-11-28 22:17:48.000000 gnuhealth_iss-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    15090 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    15029 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    13980 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    15233 2022-11-28 22:17:48.000000 gnuhealth_iss-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    12298 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    13669 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    13632 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:18:48.200832 gnuhealth_iss-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3571 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:48.199844 gnuhealth_iss-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      230 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      580 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/tests/test_health_iss.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       73 2023-04-07 09:37:21.000000 gnuhealth_iss-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:48.199979 gnuhealth_iss-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3010 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/view/health_iss_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      417 2023-04-07 09:17:52.000000 gnuhealth_iss-4.2.1/view/health_iss_tree.xml
```

### Comparing `gnuhealth_iss-4.2.0/COPYING` & `gnuhealth_iss-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/PKG-INFO` & `gnuhealth_iss-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_iss
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Injury Surveillance System package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_iss-4.2.0/README.rst` & `gnuhealth_iss-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/__init__.py` & `gnuhealth_iss-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/PKG-INFO` & `gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-iss
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Injury Surveillance System package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_iss-4.2.0/gnuhealth_iss.egg-info/SOURCES.txt` & `gnuhealth_iss-4.2.1/gnuhealth_iss.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/health_iss.py` & `gnuhealth_iss-4.2.1/health_iss.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/health_iss_view.xml` & `gnuhealth_iss-4.2.1/health_iss_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/ar.po` & `gnuhealth_iss-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/de.po` & `gnuhealth_iss-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/el.po` & `gnuhealth_iss-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/es.po` & `gnuhealth_iss-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/fr.po` & `gnuhealth_iss-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/it_IT.po` & `gnuhealth_iss-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/ja_JP.po` & `gnuhealth_iss-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/lo.po` & `gnuhealth_iss-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/pt_BR.po` & `gnuhealth_iss-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/locale/zh_CN.po` & `gnuhealth_iss-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/setup.py` & `gnuhealth_iss-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/tests/test_health_iss.py` & `gnuhealth_iss-4.2.1/tests/test_health_iss.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_iss-4.2.0/view/health_iss_form.xml` & `gnuhealth_iss-4.2.1/view/health_iss_form.xml`

 * *Files identical despite different names*

