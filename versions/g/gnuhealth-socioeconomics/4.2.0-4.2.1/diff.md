# Comparing `tmp/gnuhealth_socioeconomics-4.2.0.tar.gz` & `tmp/gnuhealth_socioeconomics-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_socioeconomics-4.2.0.tar", last modified: Sat Feb 11 21:57:54 2023, max compression
+gzip compressed data, was "gnuhealth_socioeconomics-4.2.1.tar", last modified: Fri Apr  7 10:19:53 2023, max compression
```

## Comparing `gnuhealth_socioeconomics-4.2.0.tar` & `gnuhealth_socioeconomics-4.2.1.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.375602 gnuhealth_socioeconomics-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_socioeconomics-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_socioeconomics-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5748 2023-02-11 21:57:54.375463 gnuhealth_socioeconomics-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1082 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.373277 gnuhealth_socioeconomics-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      672 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/data/gnuhealth_commands.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.373344 gnuhealth_socioeconomics-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      618 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.375012 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5748 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1244 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       80 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:57:54.000000 gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    13746 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/health_socioeconomics.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3524 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/health_socioeconomics_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.374051 gnuhealth_socioeconomics-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    19259 2023-02-11 12:36:12.000000 gnuhealth_socioeconomics-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    17879 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    21268 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    17733 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    17978 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    16602 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10447 2022-11-28 22:17:48.000000 gnuhealth_socioeconomics-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    14148 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    16180 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    15524 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.374123 gnuhealth_socioeconomics-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6775 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:57:54.375639 gnuhealth_socioeconomics-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3667 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.374255 gnuhealth_socioeconomics-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      241 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      624 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/tests/test_health_socioeconomics.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      146 2023-02-11 12:44:33.000000 gnuhealth_socioeconomics-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:54.374523 gnuhealth_socioeconomics-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2285 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/view/gnuhealth_patient.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2168 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/view/gnuhealth_ses_assessment_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      705 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/view/gnuhealth_ses_assessment_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      462 2023-01-18 16:33:08.000000 gnuhealth_socioeconomics-4.2.0/view/party_form.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.162419 gnuhealth_socioeconomics-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_socioeconomics-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_socioeconomics-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5748 2023-04-07 10:19:53.162286 gnuhealth_socioeconomics-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1082 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.160216 gnuhealth_socioeconomics-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      672 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/data/gnuhealth_commands.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.160280 gnuhealth_socioeconomics-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      618 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.161919 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5748 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1244 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       80 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:53.000000 gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    13746 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/health_socioeconomics.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3524 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/health_socioeconomics_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.160970 gnuhealth_socioeconomics-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    19259 2023-02-11 12:36:12.000000 gnuhealth_socioeconomics-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    17879 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    21268 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    17733 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    17978 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    16602 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10447 2022-11-28 22:17:48.000000 gnuhealth_socioeconomics-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    14148 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    16180 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    15524 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.161044 gnuhealth_socioeconomics-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6775 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:53.162456 gnuhealth_socioeconomics-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3667 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.161175 gnuhealth_socioeconomics-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      241 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      624 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/tests/test_health_socioeconomics.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      146 2023-04-07 09:37:21.000000 gnuhealth_socioeconomics-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:53.161437 gnuhealth_socioeconomics-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2285 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/view/gnuhealth_patient.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2168 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/view/gnuhealth_ses_assessment_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      705 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/view/gnuhealth_ses_assessment_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      462 2023-04-07 09:17:52.000000 gnuhealth_socioeconomics-4.2.1/view/party_form.xml
```

### Comparing `gnuhealth_socioeconomics-4.2.0/COPYING` & `gnuhealth_socioeconomics-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/PKG-INFO` & `gnuhealth_socioeconomics-4.2.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_socioeconomics
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Person and family socioeconomic history and assessment
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_socioeconomics-4.2.0/README.rst` & `gnuhealth_socioeconomics-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/__init__.py` & `gnuhealth_socioeconomics-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/data/gnuhealth_commands.xml` & `gnuhealth_socioeconomics-4.2.1/data/gnuhealth_commands.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/doc/index.rst` & `gnuhealth_socioeconomics-4.2.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/PKG-INFO` & `gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-socioeconomics
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Person and family socioeconomic history and assessment
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_socioeconomics-4.2.0/gnuhealth_socioeconomics.egg-info/SOURCES.txt` & `gnuhealth_socioeconomics-4.2.1/gnuhealth_socioeconomics.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/health_socioeconomics.py` & `gnuhealth_socioeconomics-4.2.1/health_socioeconomics.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/health_socioeconomics_view.xml` & `gnuhealth_socioeconomics-4.2.1/health_socioeconomics_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/ar.po` & `gnuhealth_socioeconomics-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/de.po` & `gnuhealth_socioeconomics-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/el.po` & `gnuhealth_socioeconomics-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/es.po` & `gnuhealth_socioeconomics-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/fr.po` & `gnuhealth_socioeconomics-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/it_IT.po` & `gnuhealth_socioeconomics-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/ja_JP.po` & `gnuhealth_socioeconomics-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/lo.po` & `gnuhealth_socioeconomics-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/pt_BR.po` & `gnuhealth_socioeconomics-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/locale/zh_CN.po` & `gnuhealth_socioeconomics-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/security/access_rights.xml` & `gnuhealth_socioeconomics-4.2.1/security/access_rights.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/setup.py` & `gnuhealth_socioeconomics-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/tests/test_health_socioeconomics.py` & `gnuhealth_socioeconomics-4.2.1/tests/test_health_socioeconomics.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/view/gnuhealth_patient.xml` & `gnuhealth_socioeconomics-4.2.1/view/gnuhealth_patient.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/view/gnuhealth_ses_assessment_form.xml` & `gnuhealth_socioeconomics-4.2.1/view/gnuhealth_ses_assessment_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_socioeconomics-4.2.0/view/gnuhealth_ses_assessment_tree.xml` & `gnuhealth_socioeconomics-4.2.1/view/gnuhealth_ses_assessment_tree.xml`

 * *Files identical despite different names*

