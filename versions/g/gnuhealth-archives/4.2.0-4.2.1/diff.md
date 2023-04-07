# Comparing `tmp/gnuhealth_archives-4.2.0.tar.gz` & `tmp/gnuhealth_archives-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_archives-4.2.0.tar", last modified: Sat Feb 11 21:55:00 2023, max compression
+gzip compressed data, was "gnuhealth_archives-4.2.1.tar", last modified: Fri Apr  7 10:17:04 2023, max compression
```

## Comparing `gnuhealth_archives-4.2.0.tar` & `gnuhealth_archives-4.2.1.tar`

### file list

```diff
@@ -1,40 +1,40 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.051911 gnuhealth_archives-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5739 2023-02-11 21:55:00.051757 gnuhealth_archives-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      971 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.049960 gnuhealth_archives-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      455 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.051411 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5739 2023-02-11 21:54:59.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1002 2023-02-11 21:55:00.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:54:59.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       68 2023-02-11 21:54:59.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:54:59.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:54:59.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:54:59.000000 gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3069 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/health_archives.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2167 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/health_archives_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.050025 gnuhealth_archives-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     8573 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/icons/archives.svg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.050666 gnuhealth_archives-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4265 2023-02-11 12:36:12.000000 gnuhealth_archives-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3932 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4504 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3915 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3873 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3909 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4292 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2809 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3786 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2458 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:00.051949 gnuhealth_archives-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3569 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.050791 gnuhealth_archives-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      826 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1192 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/tests/test_health_archives.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       77 2023-02-11 12:44:33.000000 gnuhealth_archives-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:00.050916 gnuhealth_archives-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      901 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/view/gnuhealth_paper_archive_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      455 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.0/view/gnuhealth_paper_archive_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.203206 gnuhealth_archives-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5739 2023-04-07 10:17:04.203074 gnuhealth_archives-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      971 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.201314 gnuhealth_archives-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      455 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.202721 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5739 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1002 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       68 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:04.000000 gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3069 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/health_archives.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2167 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/health_archives_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.201378 gnuhealth_archives-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     8573 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.1/icons/archives.svg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.202009 gnuhealth_archives-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4265 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3932 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4504 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3915 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3873 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3909 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4292 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2809 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3786 2022-11-28 22:17:47.000000 gnuhealth_archives-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2458 2023-01-18 16:33:07.000000 gnuhealth_archives-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:04.203239 gnuhealth_archives-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3569 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.202147 gnuhealth_archives-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      826 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1192 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/tests/test_health_archives.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       77 2023-04-07 09:37:21.000000 gnuhealth_archives-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:04.202275 gnuhealth_archives-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      901 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/view/gnuhealth_paper_archive_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      455 2023-04-07 09:17:52.000000 gnuhealth_archives-4.2.1/view/gnuhealth_paper_archive_tree.xml
```

### Comparing `gnuhealth_archives-4.2.0/COPYING` & `gnuhealth_archives-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/PKG-INFO` & `gnuhealth_archives-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_archives
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage paper and legacy clinical records
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_archives-4.2.0/README.rst` & `gnuhealth_archives-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/__init__.py` & `gnuhealth_archives-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/PKG-INFO` & `gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-archives
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage paper and legacy clinical records
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_archives-4.2.0/gnuhealth_archives.egg-info/SOURCES.txt` & `gnuhealth_archives-4.2.1/gnuhealth_archives.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/health_archives.py` & `gnuhealth_archives-4.2.1/health_archives.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/health_archives_view.xml` & `gnuhealth_archives-4.2.1/health_archives_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/icons/archives.svg` & `gnuhealth_archives-4.2.1/icons/archives.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/ar.po` & `gnuhealth_archives-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/de.po` & `gnuhealth_archives-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/el.po` & `gnuhealth_archives-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/es.po` & `gnuhealth_archives-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/fr.po` & `gnuhealth_archives-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/it_IT.po` & `gnuhealth_archives-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/ja_JP.po` & `gnuhealth_archives-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/lo.po` & `gnuhealth_archives-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/pt_BR.po` & `gnuhealth_archives-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/locale/zh_CN.po` & `gnuhealth_archives-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/setup.py` & `gnuhealth_archives-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/tests/__init__.py` & `gnuhealth_archives-4.2.1/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/tests/test_health_archives.py` & `gnuhealth_archives-4.2.1/tests/test_health_archives.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_archives-4.2.0/view/gnuhealth_paper_archive_form.xml` & `gnuhealth_archives-4.2.1/view/gnuhealth_paper_archive_form.xml`

 * *Files identical despite different names*

