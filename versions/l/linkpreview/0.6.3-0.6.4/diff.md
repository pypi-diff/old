# Comparing `tmp/linkpreview-0.6.3.tar.gz` & `tmp/linkpreview-0.6.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "linkpreview-0.6.3.tar", last modified: Thu Apr  6 21:02:08 2023, max compression
+gzip compressed data, was "linkpreview-0.6.4.tar", last modified: Thu Apr  6 21:05:55 2023, max compression
```

## Comparing `linkpreview-0.6.3.tar` & `linkpreview-0.6.4.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:02:08.977183 linkpreview-0.6.3/
--rw-r--r--   0 runner    (1001) docker     (122)     1062 2023-04-06 21:01:42.000000 linkpreview-0.6.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)     4562 2023-04-06 21:02:08.977183 linkpreview-0.6.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     2892 2023-04-06 21:01:42.000000 linkpreview-0.6.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:02:08.977183 linkpreview-0.6.3/linkpreview/
--rw-r--r--   0 runner    (1001) docker     (122)      275 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)      512 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/compose.py
--rw-r--r--   0 runner    (1001) docker     (122)      231 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (122)     2254 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/grabber.py
--rw-r--r--   0 runner    (1001) docker     (122)      962 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/helpers.py
--rw-r--r--   0 runner    (1001) docker     (122)     1068 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/link.py
--rw-r--r--   0 runner    (1001) docker     (122)     2388 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/linkpreview.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:02:08.977183 linkpreview-0.6.3/linkpreview/preview/
--rw-r--r--   0 runner    (1001) docker     (122)      242 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)      511 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/base.py
--rw-r--r--   0 runner    (1001) docker     (122)     1894 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/generic.py
--rw-r--r--   0 runner    (1001) docker     (122)      964 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/jsonld.py
--rw-r--r--   0 runner    (1001) docker     (122)      455 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/metabase.py
--rw-r--r--   0 runner    (1001) docker     (122)     1190 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/microdata.py
--rw-r--r--   0 runner    (1001) docker     (122)      596 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/opengraph.py
--rw-r--r--   0 runner    (1001) docker     (122)     1356 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/schemabase.py
--rw-r--r--   0 runner    (1001) docker     (122)      601 2023-04-06 21:01:42.000000 linkpreview-0.6.3/linkpreview/preview/twittercard.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:02:08.977183 linkpreview-0.6.3/linkpreview.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     4562 2023-04-06 21:02:08.000000 linkpreview-0.6.3/linkpreview.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      654 2023-04-06 21:02:08.000000 linkpreview-0.6.3/linkpreview.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 21:02:08.000000 linkpreview-0.6.3/linkpreview.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       39 2023-04-06 21:02:08.000000 linkpreview-0.6.3/linkpreview.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       12 2023-04-06 21:02:08.000000 linkpreview-0.6.3/linkpreview.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 21:02:08.977183 linkpreview-0.6.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1290 2023-04-06 21:01:42.000000 linkpreview-0.6.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:05:55.093410 linkpreview-0.6.4/
+-rw-r--r--   0 runner    (1001) docker     (122)     1062 2023-04-06 21:05:20.000000 linkpreview-0.6.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     4562 2023-04-06 21:05:55.093410 linkpreview-0.6.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     2892 2023-04-06 21:05:20.000000 linkpreview-0.6.4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:05:55.089410 linkpreview-0.6.4/linkpreview/
+-rw-r--r--   0 runner    (1001) docker     (122)      275 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      512 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/compose.py
+-rw-r--r--   0 runner    (1001) docker     (122)      231 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2254 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/grabber.py
+-rw-r--r--   0 runner    (1001) docker     (122)      962 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1068 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/link.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2388 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/linkpreview.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:05:55.093410 linkpreview-0.6.4/linkpreview/preview/
+-rw-r--r--   0 runner    (1001) docker     (122)      242 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      511 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/base.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1894 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/generic.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1002 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/jsonld.py
+-rw-r--r--   0 runner    (1001) docker     (122)      455 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/metabase.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1190 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/microdata.py
+-rw-r--r--   0 runner    (1001) docker     (122)      596 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/opengraph.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1356 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/schemabase.py
+-rw-r--r--   0 runner    (1001) docker     (122)      601 2023-04-06 21:05:20.000000 linkpreview-0.6.4/linkpreview/preview/twittercard.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:05:55.089410 linkpreview-0.6.4/linkpreview.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     4562 2023-04-06 21:05:55.000000 linkpreview-0.6.4/linkpreview.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      654 2023-04-06 21:05:55.000000 linkpreview-0.6.4/linkpreview.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 21:05:55.000000 linkpreview-0.6.4/linkpreview.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       39 2023-04-06 21:05:55.000000 linkpreview-0.6.4/linkpreview.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       12 2023-04-06 21:05:55.000000 linkpreview-0.6.4/linkpreview.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 21:05:55.093410 linkpreview-0.6.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1290 2023-04-06 21:05:20.000000 linkpreview-0.6.4/setup.py
```

### Comparing `linkpreview-0.6.3/LICENSE` & `linkpreview-0.6.4/LICENSE`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/PKG-INFO` & `linkpreview-0.6.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: linkpreview
-Version: 0.6.3
+Version: 0.6.4
 Summary: Get link (URL) preview
 Home-page: UNKNOWN
 Author: MeyT
 License: MIT
 Description: # linkpreview
         
         [![Build Status](https://www.travis-ci.com/meyt/linkpreview.svg?branch=master)](https://www.travis-ci.com/meyt/linkpreview)
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: linkpreview Version: 0.6.3 Summary: Get link (URL)
+Metadata-Version: 2.1 Name: linkpreview Version: 0.6.4 Summary: Get link (URL)
 preview Home-page: UNKNOWN Author: MeyT License: MIT Description: # linkpreview
 [![Build Status](https://www.travis-ci.com/meyt/linkpreview.svg?branch=master)]
 (https://www.travis-ci.com/meyt/linkpreview) [![Coverage Status](https://
 coveralls.io/repos/github/meyt/linkpreview/badge.svg?branch=master)](https://
 coveralls.io/github/meyt/linkpreview?branch=master) [![pypi](https://
 img.shields.io/pypi/pyversions/linkpreview.svg)](https://pypi.python.org/pypi/
 linkpreview) Get link preview in python Gathering data from: 1. [OpenGraph]
```

### Comparing `linkpreview-0.6.3/README.md` & `linkpreview-0.6.4/README.md`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/compose.py` & `linkpreview-0.6.4/linkpreview/compose.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/grabber.py` & `linkpreview-0.6.4/linkpreview/grabber.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/helpers.py` & `linkpreview-0.6.4/linkpreview/helpers.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/link.py` & `linkpreview-0.6.4/linkpreview/link.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/linkpreview.py` & `linkpreview-0.6.4/linkpreview/linkpreview.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/preview/generic.py` & `linkpreview-0.6.4/linkpreview/preview/generic.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/preview/jsonld.py` & `linkpreview-0.6.4/linkpreview/preview/jsonld.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 try:
     import orjson as json
-except ModuleNotFoundError:
+except ModuleNotFoundError:  # pragma: nocover
     try:
         import ujson as json
-    except ModuleNotFoundError:
+    except ModuleNotFoundError:  # pragma: nocover
         import json
 
 from linkpreview.preview.schemabase import SchemaPreviewBase
 
 
 class JsonLd(SchemaPreviewBase):
     """
```

### Comparing `linkpreview-0.6.3/linkpreview/preview/microdata.py` & `linkpreview-0.6.4/linkpreview/preview/microdata.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/preview/opengraph.py` & `linkpreview-0.6.4/linkpreview/preview/opengraph.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/preview/schemabase.py` & `linkpreview-0.6.4/linkpreview/preview/schemabase.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview/preview/twittercard.py` & `linkpreview-0.6.4/linkpreview/preview/twittercard.py`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/linkpreview.egg-info/PKG-INFO` & `linkpreview-0.6.4/linkpreview.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: linkpreview
-Version: 0.6.3
+Version: 0.6.4
 Summary: Get link (URL) preview
 Home-page: UNKNOWN
 Author: MeyT
 License: MIT
 Description: # linkpreview
         
         [![Build Status](https://www.travis-ci.com/meyt/linkpreview.svg?branch=master)](https://www.travis-ci.com/meyt/linkpreview)
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: linkpreview Version: 0.6.3 Summary: Get link (URL)
+Metadata-Version: 2.1 Name: linkpreview Version: 0.6.4 Summary: Get link (URL)
 preview Home-page: UNKNOWN Author: MeyT License: MIT Description: # linkpreview
 [![Build Status](https://www.travis-ci.com/meyt/linkpreview.svg?branch=master)]
 (https://www.travis-ci.com/meyt/linkpreview) [![Coverage Status](https://
 coveralls.io/repos/github/meyt/linkpreview/badge.svg?branch=master)](https://
 coveralls.io/github/meyt/linkpreview?branch=master) [![pypi](https://
 img.shields.io/pypi/pyversions/linkpreview.svg)](https://pypi.python.org/pypi/
 linkpreview) Get link preview in python Gathering data from: 1. [OpenGraph]
```

### Comparing `linkpreview-0.6.3/linkpreview.egg-info/SOURCES.txt` & `linkpreview-0.6.4/linkpreview.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `linkpreview-0.6.3/setup.py` & `linkpreview-0.6.4/setup.py`

 * *Files identical despite different names*

