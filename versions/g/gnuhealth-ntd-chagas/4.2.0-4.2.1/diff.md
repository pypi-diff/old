# Comparing `tmp/gnuhealth_ntd_chagas-4.2.0.tar.gz` & `tmp/gnuhealth_ntd_chagas-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_ntd_chagas-4.2.0.tar", last modified: Sat Feb 11 21:57:03 2023, max compression
+gzip compressed data, was "gnuhealth_ntd_chagas-4.2.1.tar", last modified: Fri Apr  7 10:19:04 2023, max compression
```

## Comparing `gnuhealth_ntd_chagas-4.2.0.tar` & `gnuhealth_ntd_chagas-4.2.1.tar`

### file list

```diff
@@ -1,42 +1,42 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.016819 gnuhealth_ntd_chagas-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5733 2023-02-11 21:57:03.016677 gnuhealth_ntd_chagas-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1083 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.014755 gnuhealth_ntd_chagas-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      816 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/data/health_ntd_chagas_sequence.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)    12509 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/data/lab_test_data.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.014826 gnuhealth_ntd_chagas-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      685 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.016309 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5733 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1133 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       72 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       21 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:57:02.000000 gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4306 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/health_ntd_chagas.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1517 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/health_ntd_chagas_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.015506 gnuhealth_ntd_chagas-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11023 2023-02-11 12:36:12.000000 gnuhealth_ntd_chagas-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9701 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11211 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10282 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10537 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10372 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9578 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     8080 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9906 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10111 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2412 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/sequences.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:57:03.016854 gnuhealth_ntd_chagas-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3628 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.015641 gnuhealth_ntd_chagas-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      237 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      606 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/tests/test_health_ntd_chagas.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      151 2023-02-11 12:44:33.000000 gnuhealth_ntd_chagas-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:03.015771 gnuhealth_ntd_chagas-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2255 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/view/gnuhealth_chagas_du_survey_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      533 2023-01-18 16:33:08.000000 gnuhealth_ntd_chagas-4.2.0/view/gnuhealth_chagas_du_survey_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.524163 gnuhealth_ntd_chagas-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5733 2023-04-07 10:19:04.524027 gnuhealth_ntd_chagas-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1083 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.522127 gnuhealth_ntd_chagas-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      816 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/data/health_ntd_chagas_sequence.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)    12509 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/data/lab_test_data.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.522199 gnuhealth_ntd_chagas-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      685 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.523677 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5733 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1133 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       72 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       21 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:04.000000 gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4306 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/health_ntd_chagas.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1517 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/health_ntd_chagas_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.522863 gnuhealth_ntd_chagas-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11023 2023-02-11 12:36:12.000000 gnuhealth_ntd_chagas-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9701 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11211 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10282 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10537 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10372 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9578 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     8080 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9906 2022-11-28 22:17:48.000000 gnuhealth_ntd_chagas-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10111 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2412 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/sequences.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:04.524199 gnuhealth_ntd_chagas-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3628 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.523028 gnuhealth_ntd_chagas-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      237 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      606 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/tests/test_health_ntd_chagas.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      151 2023-04-07 09:37:21.000000 gnuhealth_ntd_chagas-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:04.523157 gnuhealth_ntd_chagas-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2255 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/view/gnuhealth_chagas_du_survey_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      533 2023-04-07 09:17:52.000000 gnuhealth_ntd_chagas-4.2.1/view/gnuhealth_chagas_du_survey_tree.xml
```

### Comparing `gnuhealth_ntd_chagas-4.2.0/COPYING` & `gnuhealth_ntd_chagas-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/PKG-INFO` & `gnuhealth_ntd_chagas-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_ntd_chagas
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Neglected Tropical Diseases. Chagas package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_ntd_chagas-4.2.0/README.rst` & `gnuhealth_ntd_chagas-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/__init__.py` & `gnuhealth_ntd_chagas-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/data/health_ntd_chagas_sequence.xml` & `gnuhealth_ntd_chagas-4.2.1/data/health_ntd_chagas_sequence.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/data/lab_test_data.xml` & `gnuhealth_ntd_chagas-4.2.1/data/lab_test_data.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/doc/index.rst` & `gnuhealth_ntd_chagas-4.2.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/PKG-INFO` & `gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-ntd-chagas
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Neglected Tropical Diseases. Chagas package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_ntd_chagas-4.2.0/gnuhealth_ntd_chagas.egg-info/SOURCES.txt` & `gnuhealth_ntd_chagas-4.2.1/gnuhealth_ntd_chagas.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/health_ntd_chagas.py` & `gnuhealth_ntd_chagas-4.2.1/health_ntd_chagas.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/health_ntd_chagas_view.xml` & `gnuhealth_ntd_chagas-4.2.1/health_ntd_chagas_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/ar.po` & `gnuhealth_ntd_chagas-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/de.po` & `gnuhealth_ntd_chagas-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/el.po` & `gnuhealth_ntd_chagas-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/es.po` & `gnuhealth_ntd_chagas-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/fr.po` & `gnuhealth_ntd_chagas-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/it_IT.po` & `gnuhealth_ntd_chagas-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/ja_JP.po` & `gnuhealth_ntd_chagas-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/lo.po` & `gnuhealth_ntd_chagas-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/pt_BR.po` & `gnuhealth_ntd_chagas-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/locale/zh_CN.po` & `gnuhealth_ntd_chagas-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/sequences.py` & `gnuhealth_ntd_chagas-4.2.1/sequences.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/setup.py` & `gnuhealth_ntd_chagas-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/tests/test_health_ntd_chagas.py` & `gnuhealth_ntd_chagas-4.2.1/tests/test_health_ntd_chagas.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/view/gnuhealth_chagas_du_survey_form.xml` & `gnuhealth_ntd_chagas-4.2.1/view/gnuhealth_chagas_du_survey_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_ntd_chagas-4.2.0/view/gnuhealth_chagas_du_survey_tree.xml` & `gnuhealth_ntd_chagas-4.2.1/view/gnuhealth_chagas_du_survey_tree.xml`

 * *Files identical despite different names*

