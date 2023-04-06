# Comparing `tmp/currensees-1.0.3.tar.gz` & `tmp/currensees-1.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/currensees-1.0.3.tar", last modified: Thu Apr  6 08:29:08 2023, max compression
+gzip compressed data, was "dist/currensees-1.0.4.tar", last modified: Thu Apr  6 12:39:31 2023, max compression
```

## Comparing `currensees-1.0.3.tar` & `currensees-1.0.4.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 finn       (501) staff       (20)        0 2023-04-06 08:29:08.601031 currensees-1.0.3/
--rw-r--r--   0 finn       (501) staff       (20)     5289 2023-04-06 08:29:08.601254 currensees-1.0.3/PKG-INFO
--rw-r--r--   0 finn       (501) staff       (20)     2393 2023-04-06 08:19:45.000000 currensees-1.0.3/README.md
-drwxr-xr-x   0 finn       (501) staff       (20)        0 2023-04-06 08:29:08.597969 currensees-1.0.3/currensees/
--rw-r--r--   0 finn       (501) staff       (20)      163 2023-04-05 11:07:01.000000 currensees-1.0.3/currensees/__init__.py
--rw-r--r--   0 finn       (501) staff       (20)      584 2023-04-05 16:38:00.000000 currensees-1.0.3/currensees/auth.py
--rw-r--r--   0 finn       (501) staff       (20)      781 2023-04-05 16:54:46.000000 currensees-1.0.3/currensees/convert.py
--rw-r--r--   0 finn       (501) staff       (20)      671 2023-04-05 16:57:18.000000 currensees-1.0.3/currensees/convert_all.py
--rw-r--r--   0 finn       (501) staff       (20)      940 2023-04-05 16:52:00.000000 currensees-1.0.3/currensees/currencies.py
--rw-r--r--   0 finn       (501) staff       (20)     1030 2023-04-05 17:02:43.000000 currensees-1.0.3/currensees/historical.py
--rw-r--r--   0 finn       (501) staff       (20)       17 2023-04-06 08:28:37.000000 currensees-1.0.3/currensees/version.py
-drwxr-xr-x   0 finn       (501) staff       (20)        0 2023-04-06 08:29:08.600687 currensees-1.0.3/currensees.egg-info/
--rw-r--r--   0 finn       (501) staff       (20)     5289 2023-04-06 08:29:08.000000 currensees-1.0.3/currensees.egg-info/PKG-INFO
--rw-r--r--   0 finn       (501) staff       (20)      392 2023-04-06 08:29:08.000000 currensees-1.0.3/currensees.egg-info/SOURCES.txt
--rw-r--r--   0 finn       (501) staff       (20)        1 2023-04-06 08:29:08.000000 currensees-1.0.3/currensees.egg-info/dependency_links.txt
--rw-r--r--   0 finn       (501) staff       (20)        1 2023-04-06 08:25:42.000000 currensees-1.0.3/currensees.egg-info/not-zip-safe
--rw-r--r--   0 finn       (501) staff       (20)        9 2023-04-06 08:29:08.000000 currensees-1.0.3/currensees.egg-info/requires.txt
--rw-r--r--   0 finn       (501) staff       (20)       11 2023-04-06 08:29:08.000000 currensees-1.0.3/currensees.egg-info/top_level.txt
--rw-r--r--   0 finn       (501) staff       (20)       38 2023-04-06 08:29:08.601727 currensees-1.0.3/setup.cfg
--rw-r--r--   0 finn       (501) staff       (20)     2646 2023-04-06 08:28:37.000000 currensees-1.0.3/setup.py
+drwxr-xr-x   0 finn       (501) staff       (20)        0 2023-04-06 12:39:31.064783 currensees-1.0.4/
+-rw-r--r--   0 finn       (501) staff       (20)     5283 2023-04-06 12:39:31.065095 currensees-1.0.4/PKG-INFO
+-rw-r--r--   0 finn       (501) staff       (20)     2390 2023-04-06 12:38:19.000000 currensees-1.0.4/README.md
+drwxr-xr-x   0 finn       (501) staff       (20)        0 2023-04-06 12:39:31.059869 currensees-1.0.4/currensees/
+-rw-r--r--   0 finn       (501) staff       (20)      163 2023-04-05 11:07:01.000000 currensees-1.0.4/currensees/__init__.py
+-rw-r--r--   0 finn       (501) staff       (20)      584 2023-04-05 16:38:00.000000 currensees-1.0.4/currensees/auth.py
+-rw-r--r--   0 finn       (501) staff       (20)      781 2023-04-05 16:54:46.000000 currensees-1.0.4/currensees/convert.py
+-rw-r--r--   0 finn       (501) staff       (20)      671 2023-04-05 16:57:18.000000 currensees-1.0.4/currensees/convert_all.py
+-rw-r--r--   0 finn       (501) staff       (20)      940 2023-04-05 16:52:00.000000 currensees-1.0.4/currensees/currencies.py
+-rw-r--r--   0 finn       (501) staff       (20)     1030 2023-04-05 17:02:43.000000 currensees-1.0.4/currensees/historical.py
+-rw-r--r--   0 finn       (501) staff       (20)       17 2023-04-06 12:38:54.000000 currensees-1.0.4/currensees/version.py
+drwxr-xr-x   0 finn       (501) staff       (20)        0 2023-04-06 12:39:31.064020 currensees-1.0.4/currensees.egg-info/
+-rw-r--r--   0 finn       (501) staff       (20)     5283 2023-04-06 12:39:30.000000 currensees-1.0.4/currensees.egg-info/PKG-INFO
+-rw-r--r--   0 finn       (501) staff       (20)      392 2023-04-06 12:39:30.000000 currensees-1.0.4/currensees.egg-info/SOURCES.txt
+-rw-r--r--   0 finn       (501) staff       (20)        1 2023-04-06 12:39:30.000000 currensees-1.0.4/currensees.egg-info/dependency_links.txt
+-rw-r--r--   0 finn       (501) staff       (20)        1 2023-04-06 12:39:15.000000 currensees-1.0.4/currensees.egg-info/not-zip-safe
+-rw-r--r--   0 finn       (501) staff       (20)        9 2023-04-06 12:39:30.000000 currensees-1.0.4/currensees.egg-info/requires.txt
+-rw-r--r--   0 finn       (501) staff       (20)       11 2023-04-06 12:39:30.000000 currensees-1.0.4/currensees.egg-info/top_level.txt
+-rw-r--r--   0 finn       (501) staff       (20)       38 2023-04-06 12:39:31.065980 currensees-1.0.4/setup.cfg
+-rw-r--r--   0 finn       (501) staff       (20)     2646 2023-04-06 12:38:54.000000 currensees-1.0.4/setup.py
```

### Comparing `currensees-1.0.3/PKG-INFO` & `currensees-1.0.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: currensees
-Version: 1.0.3
+Version: 1.0.4
 Summary: Python library for integrating with the Currency API.
 Home-page: https://moatsystems.com/currency-api/
 Author: Moat Systems Limited
 Author-email: support@moatsystems.com
 License: BSD 3-Clause
 Project-URL: Bug Tracker, https://github.com/moatsystems/currensees_sdk/issues
 Project-URL: Changes, https://github.com/moatsystems/currensees_sdk/blob/main/CHANGELOG.md
@@ -82,16 +82,16 @@
             print(historical_rates.get_historical_rates())
         
             # Retrieve currencies historical rates by uuid
             historical_rates = HistoricalRates(username, '2023_04_02', '02', '04', '2023')
             print(historical_rates.get_historical_rate_by_uuid('fe86014c-d162-11ed-a2dc-acde48001122'))
         
         
-        Setting up an Currency API Account
-        ----------------------------------
+        Setting up Currency API Account
+        -------------------------------
         
         Subscribe here for a `user account`_.
         
         .. _user account: https://moatsystems.com/currency-api/
         
         
         Using the Currency API
```

### Comparing `currensees-1.0.3/README.md` & `currensees-1.0.4/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -61,15 +61,15 @@
 print(historical_rates.get_historical_rates())
 
 # Retrieve currencies historical rates by uuid
 historical_rates = HistoricalRates(username, '2023_04_02', '02', '04', '2023')
 print(historical_rates.get_historical_rate_by_uuid('fe86014c-d162-11ed-a2dc-acde48001122'))
 ```
 
-## Setting up an Currency API Account
+## Setting up Currency API Account
 
 Subscribe here for a [user account](https://moatsystems.com/currency-api/).
 
 
 ## Using the Currency API
 
 You can read the [API documentation](https://docs.currensees.com/) to understand what's possible with the Currency API. If you need further assistance, don't hesitate to [contact us](https://moatsystems.com/contact/).
```

### Comparing `currensees-1.0.3/currensees/auth.py` & `currensees-1.0.4/currensees/auth.py`

 * *Files identical despite different names*

### Comparing `currensees-1.0.3/currensees/convert.py` & `currensees-1.0.4/currensees/convert.py`

 * *Files identical despite different names*

### Comparing `currensees-1.0.3/currensees/convert_all.py` & `currensees-1.0.4/currensees/convert_all.py`

 * *Files identical despite different names*

### Comparing `currensees-1.0.3/currensees/currencies.py` & `currensees-1.0.4/currensees/currencies.py`

 * *Files identical despite different names*

### Comparing `currensees-1.0.3/currensees/historical.py` & `currensees-1.0.4/currensees/historical.py`

 * *Files identical despite different names*

### Comparing `currensees-1.0.3/currensees.egg-info/PKG-INFO` & `currensees-1.0.4/currensees.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: currensees
-Version: 1.0.3
+Version: 1.0.4
 Summary: Python library for integrating with the Currency API.
 Home-page: https://moatsystems.com/currency-api/
 Author: Moat Systems Limited
 Author-email: support@moatsystems.com
 License: BSD 3-Clause
 Project-URL: Bug Tracker, https://github.com/moatsystems/currensees_sdk/issues
 Project-URL: Changes, https://github.com/moatsystems/currensees_sdk/blob/main/CHANGELOG.md
@@ -82,16 +82,16 @@
             print(historical_rates.get_historical_rates())
         
             # Retrieve currencies historical rates by uuid
             historical_rates = HistoricalRates(username, '2023_04_02', '02', '04', '2023')
             print(historical_rates.get_historical_rate_by_uuid('fe86014c-d162-11ed-a2dc-acde48001122'))
         
         
-        Setting up an Currency API Account
-        ----------------------------------
+        Setting up Currency API Account
+        -------------------------------
         
         Subscribe here for a `user account`_.
         
         .. _user account: https://moatsystems.com/currency-api/
         
         
         Using the Currency API
```

### Comparing `currensees-1.0.3/setup.py` & `currensees-1.0.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 import sys
 from setuptools import setup, find_packages  # noqa: H301
 from distutils.core import Extension
 
 NAME = "currensees"
-VERSION = "1.0.3"
+VERSION = "1.0.4"
 REQUIRES = ["requests"]
 
 # read the contents of your README file
 from os import path
 this_directory = path.abspath(path.dirname(__file__))
 with open(path.join(this_directory, 'LONG_DESCRIPTION.rst')) as f:
     long_description = f.read()
```

