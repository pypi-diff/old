# Comparing `tmp/gnuhealth_icd9procs-4.2.0.tar.gz` & `tmp/gnuhealth_icd9procs-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_icd9procs-4.2.0.tar", last modified: Sat Feb 11 21:56:20 2023, max compression
+gzip compressed data, was "gnuhealth_icd9procs-4.2.1.tar", last modified: Fri Apr  7 10:18:21 2023, max compression
```

## Comparing `gnuhealth_icd9procs-4.2.0.tar` & `gnuhealth_icd9procs-4.2.1.tar`

### file list

```diff
@@ -1,36 +1,36 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:20.696094 gnuhealth_icd9procs-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5729 2023-02-11 21:56:20.695859 gnuhealth_icd9procs-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      786 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:20.690463 gnuhealth_icd9procs-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   675178 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/data/icd9procs.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:20.690944 gnuhealth_icd9procs-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      286 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:20.694832 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5729 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)      803 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       70 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:56:20.000000 gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)      787 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/health_icd9procs.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:20.693911 gnuhealth_icd9procs-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   471980 2023-02-11 12:36:12.000000 gnuhealth_icd9procs-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   645836 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   487529 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   467138 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   469426 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   577528 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:56:20.696145 gnuhealth_icd9procs-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3619 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:20.694301 gnuhealth_icd9procs-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      236 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      605 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.0/tests/test_health_icd9procs.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       71 2023-02-11 12:44:33.000000 gnuhealth_icd9procs-4.2.0/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:21.330308 gnuhealth_icd9procs-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5729 2023-04-07 10:18:21.330158 gnuhealth_icd9procs-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      786 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:21.325592 gnuhealth_icd9procs-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   675178 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/data/icd9procs.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:21.326032 gnuhealth_icd9procs-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      286 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:21.329810 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5729 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)      803 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       70 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:18:21.000000 gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)      787 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/health_icd9procs.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:21.328900 gnuhealth_icd9procs-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   471980 2023-02-11 12:36:12.000000 gnuhealth_icd9procs-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   645836 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   487529 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   467138 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   467138 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   469426 2022-11-28 22:17:48.000000 gnuhealth_icd9procs-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   577528 2023-01-18 16:33:08.000000 gnuhealth_icd9procs-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:18:21.330347 gnuhealth_icd9procs-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3619 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:21.329292 gnuhealth_icd9procs-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      236 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      605 2023-04-07 09:17:52.000000 gnuhealth_icd9procs-4.2.1/tests/test_health_icd9procs.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       71 2023-04-07 09:37:21.000000 gnuhealth_icd9procs-4.2.1/tryton.cfg
```

### Comparing `gnuhealth_icd9procs-4.2.0/COPYING` & `gnuhealth_icd9procs-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/PKG-INFO` & `gnuhealth_icd9procs-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_icd9procs
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WHO ICD9 - Volume 3 - procedures package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_icd9procs-4.2.0/README.rst` & `gnuhealth_icd9procs-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/__init__.py` & `gnuhealth_icd9procs-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/data/icd9procs.xml` & `gnuhealth_icd9procs-4.2.1/data/icd9procs.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/PKG-INFO` & `gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-icd9procs
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WHO ICD9 - Volume 3 - procedures package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_icd9procs-4.2.0/gnuhealth_icd9procs.egg-info/SOURCES.txt` & `gnuhealth_icd9procs-4.2.1/gnuhealth_icd9procs.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/health_icd9procs.py` & `gnuhealth_icd9procs-4.2.1/health_icd9procs.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/ar.po` & `gnuhealth_icd9procs-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/de.po` & `gnuhealth_icd9procs-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/el.po` & `gnuhealth_icd9procs-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/es.po` & `gnuhealth_icd9procs-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/fr.po` & `gnuhealth_icd9procs-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/it_IT.po` & `gnuhealth_icd9procs-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/ja_JP.po` & `gnuhealth_icd9procs-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/lo.po` & `gnuhealth_icd9procs-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/pt_BR.po` & `gnuhealth_icd9procs-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/locale/zh_CN.po` & `gnuhealth_icd9procs-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/setup.py` & `gnuhealth_icd9procs-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd9procs-4.2.0/tests/test_health_icd9procs.py` & `gnuhealth_icd9procs-4.2.1/tests/test_health_icd9procs.py`

 * *Files identical despite different names*

