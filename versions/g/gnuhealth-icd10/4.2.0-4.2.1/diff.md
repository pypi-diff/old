# Comparing `tmp/gnuhealth_icd10-4.2.0.tar.gz` & `tmp/gnuhealth_icd10-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_icd10-4.2.0.tar", last modified: Sat Feb 11 21:55:56 2023, max compression
+gzip compressed data, was "gnuhealth_icd10-4.2.1.tar", last modified: Fri Apr  7 10:17:59 2023, max compression
```

## Comparing `gnuhealth_icd10-4.2.0.tar` & `gnuhealth_icd10-4.2.1.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:56.555164 gnuhealth_icd10-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_icd10-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:47.000000 gnuhealth_icd10-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5826 2023-02-11 21:55:56.554981 gnuhealth_icd10-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      786 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:56.520469 gnuhealth_icd10-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    55916 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/data/disease_categories.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1351687 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/data/disease_groups.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)  3574633 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/data/diseases.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:56.527066 gnuhealth_icd10-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      344 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:56.554350 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5826 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1141 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       62 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       34 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:56.000000 gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)      786 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/health_icd10.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:56.549791 gnuhealth_icd10-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1634663 2023-02-11 12:36:12.000000 gnuhealth_icd10-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  2549910 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1954938 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1608943 2022-11-28 22:17:48.000000 gnuhealth_icd10-4.2.0/locale/eo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  2460053 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  2710647 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1609363 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/id.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1634234 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  2304294 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1609234 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/ka.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1619474 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1608946 2022-11-28 22:17:48.000000 gnuhealth_icd10-4.2.0/locale/nb_NO.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1610257 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/pl.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  2319416 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1610136 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/sq.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1609752 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/sv.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1609442 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/uk.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  2076669 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1609906 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/locale/zh_Hant.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:56.555210 gnuhealth_icd10-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3728 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:56.550694 gnuhealth_icd10-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      232 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      588 2023-01-18 16:33:08.000000 gnuhealth_icd10-4.2.0/tests/test_health_icd10.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      130 2023-02-11 12:44:33.000000 gnuhealth_icd10-4.2.0/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:59.995264 gnuhealth_icd10-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_icd10-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:47.000000 gnuhealth_icd10-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5826 2023-04-07 10:17:59.994523 gnuhealth_icd10-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      786 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:59.931859 gnuhealth_icd10-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    55916 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/data/disease_categories.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1351687 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/data/disease_groups.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)  3574633 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/data/diseases.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:59.934840 gnuhealth_icd10-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      344 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:59.991886 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5826 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1141 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       62 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       34 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:59.000000 gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)      786 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/health_icd10.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:59.984494 gnuhealth_icd10-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1634663 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  2549910 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1954938 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1608943 2022-11-28 22:17:48.000000 gnuhealth_icd10-4.2.1/locale/eo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  2460053 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  2710647 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1609363 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/id.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1634234 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  2304294 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1609234 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/ka.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1619474 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1608946 2022-11-28 22:17:48.000000 gnuhealth_icd10-4.2.1/locale/nb_NO.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1610257 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/pl.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  2319416 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1610136 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/sq.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1609752 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/sv.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1609442 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/uk.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  2076669 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1609906 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/locale/zh_Hant.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:59.995549 gnuhealth_icd10-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3728 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:59.988633 gnuhealth_icd10-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      232 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      588 2023-04-07 09:17:52.000000 gnuhealth_icd10-4.2.1/tests/test_health_icd10.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      130 2023-04-07 09:37:21.000000 gnuhealth_icd10-4.2.1/tryton.cfg
```

### Comparing `gnuhealth_icd10-4.2.0/COPYING` & `gnuhealth_icd10-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/PKG-INFO` & `gnuhealth_icd10-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_icd10
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WHO ICD10 Module
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_icd10-4.2.0/README.rst` & `gnuhealth_icd10-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/__init__.py` & `gnuhealth_icd10-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/data/disease_categories.xml` & `gnuhealth_icd10-4.2.1/data/disease_categories.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/data/disease_groups.xml` & `gnuhealth_icd10-4.2.1/data/disease_groups.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/data/diseases.xml` & `gnuhealth_icd10-4.2.1/data/diseases.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/PKG-INFO` & `gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-icd10
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health WHO ICD10 Module
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_icd10-4.2.0/gnuhealth_icd10.egg-info/SOURCES.txt` & `gnuhealth_icd10-4.2.1/gnuhealth_icd10.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/health_icd10.py` & `gnuhealth_icd10-4.2.1/health_icd10.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/ar.po` & `gnuhealth_icd10-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/de.po` & `gnuhealth_icd10-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/el.po` & `gnuhealth_icd10-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/eo.po` & `gnuhealth_icd10-4.2.1/locale/eo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/es.po` & `gnuhealth_icd10-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/fr.po` & `gnuhealth_icd10-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/id.po` & `gnuhealth_icd10-4.2.1/locale/id.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/it_IT.po` & `gnuhealth_icd10-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/ja_JP.po` & `gnuhealth_icd10-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/ka.po` & `gnuhealth_icd10-4.2.1/locale/ka.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/lo.po` & `gnuhealth_icd10-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/nb_NO.po` & `gnuhealth_icd10-4.2.1/locale/nb_NO.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/pl.po` & `gnuhealth_icd10-4.2.1/locale/pl.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/pt_BR.po` & `gnuhealth_icd10-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/sq.po` & `gnuhealth_icd10-4.2.1/locale/sq.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/sv.po` & `gnuhealth_icd10-4.2.1/locale/sv.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/uk.po` & `gnuhealth_icd10-4.2.1/locale/uk.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/zh_CN.po` & `gnuhealth_icd10-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/locale/zh_Hant.po` & `gnuhealth_icd10-4.2.1/locale/zh_Hant.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/setup.py` & `gnuhealth_icd10-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_icd10-4.2.0/tests/test_health_icd10.py` & `gnuhealth_icd10-4.2.1/tests/test_health_icd10.py`

 * *Files identical despite different names*

