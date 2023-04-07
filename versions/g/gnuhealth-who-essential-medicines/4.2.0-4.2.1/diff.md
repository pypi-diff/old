# Comparing `tmp/gnuhealth_who_essential_medicines-4.2.0.tar.gz` & `tmp/gnuhealth_who_essential_medicines-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_who_essential_medicines-4.2.0.tar", last modified: Sat Feb 11 21:58:09 2023, max compression
+gzip compressed data, was "gnuhealth_who_essential_medicines-4.2.1.tar", last modified: Fri Apr  7 10:20:06 2023, max compression
```

## Comparing `gnuhealth_who_essential_medicines-4.2.0.tar` & `gnuhealth_who_essential_medicines-4.2.1.tar`

### file list

```diff
@@ -1,38 +1,38 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:09.569195 gnuhealth_who_essential_medicines-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5734 2023-02-11 21:58:09.569027 gnuhealth_who_essential_medicines-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      857 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:09.566689 gnuhealth_who_essential_medicines-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   177806 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/data/WHO_list_of_essential_medicines.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)   192295 2023-01-24 11:43:23.000000 gnuhealth_who_essential_medicines-4.2.0/data/WHO_products.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)    34404 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/data/medicament_categories.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:09.566774 gnuhealth_who_essential_medicines-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      985 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:09.568702 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5734 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1083 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       98 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:58:09.000000 gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)      786 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/health_who_essential_medicines.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:09.567930 gnuhealth_who_essential_medicines-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   122224 2023-02-11 12:36:12.000000 gnuhealth_who_essential_medicines-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   109170 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   126021 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   110692 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   111889 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   110415 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   116564 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    92871 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   110912 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   107965 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:58:09.569232 gnuhealth_who_essential_medicines-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3707 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:58:09.568120 gnuhealth_who_essential_medicines-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      250 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      656 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.0/tests/test_health_who_essential_medicines.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      154 2023-02-11 12:44:33.000000 gnuhealth_who_essential_medicines-4.2.0/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:06.521733 gnuhealth_who_essential_medicines-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5734 2023-04-07 10:20:06.521587 gnuhealth_who_essential_medicines-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      857 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:06.519221 gnuhealth_who_essential_medicines-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   177806 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/data/WHO_list_of_essential_medicines.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)   192295 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/data/WHO_products.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)    34404 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/data/medicament_categories.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:06.519318 gnuhealth_who_essential_medicines-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      985 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:06.521263 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5734 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1083 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       98 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:20:06.000000 gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)      786 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/health_who_essential_medicines.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:06.520503 gnuhealth_who_essential_medicines-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   122224 2023-02-11 12:36:12.000000 gnuhealth_who_essential_medicines-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   109170 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   126021 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   110692 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   111889 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   110415 2023-01-18 16:33:08.000000 gnuhealth_who_essential_medicines-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   116564 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    92871 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   110912 2022-11-28 22:17:48.000000 gnuhealth_who_essential_medicines-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   107965 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:20:06.521768 gnuhealth_who_essential_medicines-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3707 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:20:06.520692 gnuhealth_who_essential_medicines-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      250 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      656 2023-04-07 09:17:52.000000 gnuhealth_who_essential_medicines-4.2.1/tests/test_health_who_essential_medicines.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      154 2023-04-07 09:37:21.000000 gnuhealth_who_essential_medicines-4.2.1/tryton.cfg
```

### Comparing `gnuhealth_who_essential_medicines-4.2.0/COPYING` & `gnuhealth_who_essential_medicines-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/PKG-INFO` & `gnuhealth_who_essential_medicines-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_who_essential_medicines
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WHO Essential Medicines package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_who_essential_medicines-4.2.0/README.rst` & `gnuhealth_who_essential_medicines-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/__init__.py` & `gnuhealth_who_essential_medicines-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/data/WHO_list_of_essential_medicines.xml` & `gnuhealth_who_essential_medicines-4.2.1/data/WHO_list_of_essential_medicines.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/data/WHO_products.xml` & `gnuhealth_who_essential_medicines-4.2.1/data/WHO_products.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/data/medicament_categories.xml` & `gnuhealth_who_essential_medicines-4.2.1/data/medicament_categories.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/doc/index.rst` & `gnuhealth_who_essential_medicines-4.2.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/PKG-INFO` & `gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-who-essential-medicines
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WHO Essential Medicines package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_who_essential_medicines-4.2.0/gnuhealth_who_essential_medicines.egg-info/SOURCES.txt` & `gnuhealth_who_essential_medicines-4.2.1/gnuhealth_who_essential_medicines.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/health_who_essential_medicines.py` & `gnuhealth_who_essential_medicines-4.2.1/health_who_essential_medicines.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/ar.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/de.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/el.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/es.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/fr.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/it_IT.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/ja_JP.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/lo.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/pt_BR.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/locale/zh_CN.po` & `gnuhealth_who_essential_medicines-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/setup.py` & `gnuhealth_who_essential_medicines-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_who_essential_medicines-4.2.0/tests/test_health_who_essential_medicines.py` & `gnuhealth_who_essential_medicines-4.2.1/tests/test_health_who_essential_medicines.py`

 * *Files identical despite different names*

