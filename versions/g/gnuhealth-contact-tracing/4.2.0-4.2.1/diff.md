# Comparing `tmp/gnuhealth_contact_tracing-4.2.0.tar.gz` & `tmp/gnuhealth_contact_tracing-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_contact_tracing-4.2.0.tar", last modified: Sat Feb 11 21:55:11 2023, max compression
+gzip compressed data, was "gnuhealth_contact_tracing-4.2.1.tar", last modified: Fri Apr  7 10:17:15 2023, max compression
```

## Comparing `gnuhealth_contact_tracing-4.2.0.tar` & `gnuhealth_contact_tracing-4.2.1.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.550312 gnuhealth_contact_tracing-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_contact_tracing-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:47.000000 gnuhealth_contact_tracing-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5732 2023-02-11 21:55:11.550163 gnuhealth_contact_tracing-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      994 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.548757 gnuhealth_contact_tracing-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      380 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.549897 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5732 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)      915 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       82 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:11.000000 gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2704 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/health_contact_tracing.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2231 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/health_contact_tracing_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.548841 gnuhealth_contact_tracing-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11269 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/icons/contact_tracing.svg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.549110 gnuhealth_contact_tracing-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4438 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4345 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4350 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3795 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:11.550343 gnuhealth_contact_tracing-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3656 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.549245 gnuhealth_contact_tracing-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      242 2023-01-18 16:33:08.000000 gnuhealth_contact_tracing-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      626 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/tests/test_health_contact_tracing.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       84 2023-02-11 12:44:33.000000 gnuhealth_contact_tracing-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:11.549379 gnuhealth_contact_tracing-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1056 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/view/gnuhealth_contact_tracing_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      628 2023-01-18 16:33:07.000000 gnuhealth_contact_tracing-4.2.0/view/gnuhealth_contact_tracing_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.894490 gnuhealth_contact_tracing-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_contact_tracing-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:47.000000 gnuhealth_contact_tracing-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5732 2023-04-07 10:17:15.894350 gnuhealth_contact_tracing-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      994 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.893015 gnuhealth_contact_tracing-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      380 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.894091 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5732 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)      915 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       82 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:15.000000 gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2704 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/health_contact_tracing.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2231 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/health_contact_tracing_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.893082 gnuhealth_contact_tracing-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11269 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/icons/contact_tracing.svg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.893350 gnuhealth_contact_tracing-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4438 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4345 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4350 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3795 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:15.894526 gnuhealth_contact_tracing-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3656 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.893483 gnuhealth_contact_tracing-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      242 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      626 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/tests/test_health_contact_tracing.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       84 2023-04-07 09:37:21.000000 gnuhealth_contact_tracing-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:15.893615 gnuhealth_contact_tracing-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1056 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/view/gnuhealth_contact_tracing_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      628 2023-04-07 09:17:52.000000 gnuhealth_contact_tracing-4.2.1/view/gnuhealth_contact_tracing_tree.xml
```

### Comparing `gnuhealth_contact_tracing-4.2.0/COPYING` & `gnuhealth_contact_tracing-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/PKG-INFO` & `gnuhealth_contact_tracing-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_contact_tracing
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package for epidemics contact tracing
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_contact_tracing-4.2.0/README.rst` & `gnuhealth_contact_tracing-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/__init__.py` & `gnuhealth_contact_tracing-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/PKG-INFO` & `gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-contact-tracing
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package for epidemics contact tracing
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_contact_tracing-4.2.0/gnuhealth_contact_tracing.egg-info/SOURCES.txt` & `gnuhealth_contact_tracing-4.2.1/gnuhealth_contact_tracing.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/health_contact_tracing.py` & `gnuhealth_contact_tracing-4.2.1/health_contact_tracing.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/health_contact_tracing_view.xml` & `gnuhealth_contact_tracing-4.2.1/health_contact_tracing_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/icons/contact_tracing.svg` & `gnuhealth_contact_tracing-4.2.1/icons/contact_tracing.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/locale/de.po` & `gnuhealth_contact_tracing-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/locale/es.po` & `gnuhealth_contact_tracing-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/locale/fr.po` & `gnuhealth_contact_tracing-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/locale/zh_CN.po` & `gnuhealth_contact_tracing-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/setup.py` & `gnuhealth_contact_tracing-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/tests/test_health_contact_tracing.py` & `gnuhealth_contact_tracing-4.2.1/tests/test_health_contact_tracing.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/view/gnuhealth_contact_tracing_form.xml` & `gnuhealth_contact_tracing-4.2.1/view/gnuhealth_contact_tracing_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_contact_tracing-4.2.0/view/gnuhealth_contact_tracing_tree.xml` & `gnuhealth_contact_tracing-4.2.1/view/gnuhealth_contact_tracing_tree.xml`

 * *Files identical despite different names*

