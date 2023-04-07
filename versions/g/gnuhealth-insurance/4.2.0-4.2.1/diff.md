# Comparing `tmp/gnuhealth_insurance-4.2.0.tar.gz` & `tmp/gnuhealth_insurance-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_insurance-4.2.0.tar", last modified: Sat Feb 11 21:56:43 2023, max compression
+gzip compressed data, was "gnuhealth_insurance-4.2.1.tar", last modified: Fri Apr  7 10:18:45 2023, max compression
```

## Comparing `gnuhealth_insurance-4.2.0.tar` & `gnuhealth_insurance-4.2.1.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.602265 gnuhealth_insurance-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5741 2023-02-11 21:56:43.602110 gnuhealth_insurance-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1219 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.598990 gnuhealth_insurance-4.2.0/data/
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.599977 gnuhealth_insurance-4.2.0/data/messages/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1777 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/data/messages/messages.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.600044 gnuhealth_insurance-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      313 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/doc/index.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      779 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/exceptions.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.601721 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5741 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1296 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       70 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       43 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:56:43.000000 gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3506 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/health_insurance.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2783 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/health_insurance_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.600700 gnuhealth_insurance-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2947 2023-02-11 12:36:12.000000 gnuhealth_insurance-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2755 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3113 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2816 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2790 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2775 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2073 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2073 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2727 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3667 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:56:43.602299 gnuhealth_insurance-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3681 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.600829 gnuhealth_insurance-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      236 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      604 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/tests/test_health_insurance.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      129 2023-02-11 12:44:33.000000 gnuhealth_insurance-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.601085 gnuhealth_insurance-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      513 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/view/gnuhealth_health_service.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      398 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/view/gnuhealth_insurance_plan.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      525 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/view/gnuhealth_insurance_plan_product_policy.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      448 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/view/gnuhealth_insurance_plan_product_policy_tree.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:43.601214 gnuhealth_insurance-4.2.0/wizard/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)      365 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9238 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.0/wizard/wizard_health_insurance.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.351591 gnuhealth_insurance-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5741 2023-04-07 10:18:45.351443 gnuhealth_insurance-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1219 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.348348 gnuhealth_insurance-4.2.1/data/
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.349316 gnuhealth_insurance-4.2.1/data/messages/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1777 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/data/messages/messages.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.349383 gnuhealth_insurance-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      313 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/doc/index.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      779 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/exceptions.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.351056 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5741 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1296 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       70 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       43 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:18:45.000000 gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3506 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/health_insurance.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2783 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/health_insurance_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.350048 gnuhealth_insurance-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2947 2023-02-11 12:36:12.000000 gnuhealth_insurance-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2755 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3113 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2816 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2790 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2775 2023-01-18 16:33:08.000000 gnuhealth_insurance-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2073 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2073 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2727 2022-11-28 22:17:48.000000 gnuhealth_insurance-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3667 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:18:45.351623 gnuhealth_insurance-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3681 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.350196 gnuhealth_insurance-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      236 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      604 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/tests/test_health_insurance.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      129 2023-04-07 09:37:21.000000 gnuhealth_insurance-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.350451 gnuhealth_insurance-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      513 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/view/gnuhealth_health_service.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      398 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/view/gnuhealth_insurance_plan.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      525 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/view/gnuhealth_insurance_plan_product_policy.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      448 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/view/gnuhealth_insurance_plan_product_policy_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:45.350579 gnuhealth_insurance-4.2.1/wizard/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)      365 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9238 2023-04-07 09:17:52.000000 gnuhealth_insurance-4.2.1/wizard/wizard_health_insurance.py
```

### Comparing `gnuhealth_insurance-4.2.0/COPYING` & `gnuhealth_insurance-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/PKG-INFO` & `gnuhealth_insurance-4.2.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_insurance
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage insurances and associated services
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_insurance-4.2.0/README.rst` & `gnuhealth_insurance-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/__init__.py` & `gnuhealth_insurance-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/data/messages/messages.xml` & `gnuhealth_insurance-4.2.1/data/messages/messages.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/exceptions.py` & `gnuhealth_insurance-4.2.1/exceptions.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/PKG-INFO` & `gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-insurance
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage insurances and associated services
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_insurance-4.2.0/gnuhealth_insurance.egg-info/SOURCES.txt` & `gnuhealth_insurance-4.2.1/gnuhealth_insurance.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/health_insurance.py` & `gnuhealth_insurance-4.2.1/health_insurance.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/health_insurance_view.xml` & `gnuhealth_insurance-4.2.1/health_insurance_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/ar.po` & `gnuhealth_insurance-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/de.po` & `gnuhealth_insurance-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/el.po` & `gnuhealth_insurance-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/es.po` & `gnuhealth_insurance-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/fr.po` & `gnuhealth_insurance-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/it_IT.po` & `gnuhealth_insurance-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/ja_JP.po` & `gnuhealth_insurance-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/lo.po` & `gnuhealth_insurance-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/pt_BR.po` & `gnuhealth_insurance-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/locale/zh_CN.po` & `gnuhealth_insurance-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/setup.py` & `gnuhealth_insurance-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/tests/test_health_insurance.py` & `gnuhealth_insurance-4.2.1/tests/test_health_insurance.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/view/gnuhealth_health_service.xml` & `gnuhealth_insurance-4.2.1/view/gnuhealth_health_service.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/view/gnuhealth_insurance_plan_product_policy.xml` & `gnuhealth_insurance-4.2.1/view/gnuhealth_insurance_plan_product_policy.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_insurance-4.2.0/wizard/wizard_health_insurance.py` & `gnuhealth_insurance-4.2.1/wizard/wizard_health_insurance.py`

 * *Files identical despite different names*

