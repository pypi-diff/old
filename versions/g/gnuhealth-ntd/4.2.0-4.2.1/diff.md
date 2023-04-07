# Comparing `tmp/gnuhealth_ntd-4.2.0.tar.gz` & `tmp/gnuhealth_ntd-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_ntd-4.2.0.tar", last modified: Sat Feb 11 21:56:59 2023, max compression
+gzip compressed data, was "gnuhealth_ntd-4.2.1.tar", last modified: Fri Apr  7 10:19:01 2023, max compression
```

## Comparing `gnuhealth_ntd-4.2.0.tar` & `gnuhealth_ntd-4.2.1.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:59.928331 gnuhealth_ntd-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_ntd-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_ntd-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5718 2023-02-11 21:56:59.928171 gnuhealth_ntd-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      786 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:59.927306 gnuhealth_ntd-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1124 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:59.928034 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5718 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)      439 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       58 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:56:59.000000 gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)      809 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/health_ntd.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:59.927371 gnuhealth_ntd-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)        0 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:56:59.928362 gnuhealth_ntd-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3571 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:59.927512 gnuhealth_ntd-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      230 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      580 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.0/tests/test_health_ntd.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       58 2023-02-11 12:44:33.000000 gnuhealth_ntd-4.2.0/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:01.322750 gnuhealth_ntd-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_ntd-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_ntd-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5718 2023-04-07 10:19:01.322612 gnuhealth_ntd-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      786 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:01.321733 gnuhealth_ntd-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1124 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:01.322445 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5718 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)      439 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       58 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:01.000000 gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)      809 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/health_ntd.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:01.321804 gnuhealth_ntd-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)        0 2023-01-18 16:33:08.000000 gnuhealth_ntd-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:01.322791 gnuhealth_ntd-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3571 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:01.321935 gnuhealth_ntd-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      230 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      580 2023-04-07 09:17:52.000000 gnuhealth_ntd-4.2.1/tests/test_health_ntd.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       58 2023-04-07 09:37:21.000000 gnuhealth_ntd-4.2.1/tryton.cfg
```

### Comparing `gnuhealth_ntd-4.2.0/COPYING` & `gnuhealth_ntd-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd-4.2.0/PKG-INFO` & `gnuhealth_ntd-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_ntd
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Neglected Tropical Diseases package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_ntd-4.2.0/README.rst` & `gnuhealth_ntd-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd-4.2.0/__init__.py` & `gnuhealth_ntd-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd-4.2.0/doc/index.rst` & `gnuhealth_ntd-4.2.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd-4.2.0/gnuhealth_ntd.egg-info/PKG-INFO` & `gnuhealth_ntd-4.2.1/gnuhealth_ntd.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-ntd
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Neglected Tropical Diseases package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_ntd-4.2.0/health_ntd.py` & `gnuhealth_ntd-4.2.1/health_ntd.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd-4.2.0/setup.py` & `gnuhealth_ntd-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd-4.2.0/tests/test_health_ntd.py` & `gnuhealth_ntd-4.2.1/tests/test_health_ntd.py`

 * *Files identical despite different names*

