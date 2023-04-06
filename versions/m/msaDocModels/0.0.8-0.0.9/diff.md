# Comparing `tmp/msaDocModels-0.0.8.tar.gz` & `tmp/msaDocModels-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "msaDocModels-0.0.8.tar", last modified: Thu Nov 24 17:15:28 2022, max compression
+gzip compressed data, was "msaDocModels-0.0.9.tar", last modified: Fri Nov 25 11:39:48 2022, max compression
```

## Comparing `msaDocModels-0.0.8.tar` & `msaDocModels-0.0.9.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 17:15:28.740070 msaDocModels-0.0.8/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1099 2022-11-09 11:53:39.000000 msaDocModels-0.0.8/LICENCE
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3633 2022-11-24 17:15:28.740070 msaDocModels-0.0.8/PKG-INFO
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2153 2022-11-09 11:53:39.000000 msaDocModels-0.0.8/README.md
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 17:15:28.740070 msaDocModels-0.0.8/msaDocModels/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      484 2022-11-24 17:11:50.000000 msaDocModels-0.0.8/msaDocModels/__init__.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      562 2022-11-18 16:38:17.000000 msaDocModels-0.0.8/msaDocModels/health.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3731 2022-11-09 11:53:39.000000 msaDocModels-0.0.8/msaDocModels/msg.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      387 2022-11-22 10:24:03.000000 msaDocModels-0.0.8/msaDocModels/openapi.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2412 2022-11-18 16:38:17.000000 msaDocModels-0.0.8/msaDocModels/scheduler.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    13179 2022-11-24 17:13:14.000000 msaDocModels-0.0.8/msaDocModels/sdu.py
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 17:15:28.740070 msaDocModels-0.0.8/msaDocModels/utils/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-21 13:25:40.000000 msaDocModels-0.0.8/msaDocModels/utils/__init__.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1825 2022-11-10 09:04:48.000000 msaDocModels-0.0.8/msaDocModels/utils/htmlutils.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    22525 2022-11-09 11:53:39.000000 msaDocModels-0.0.8/msaDocModels/wdc.py
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2209 2022-11-09 11:53:39.000000 msaDocModels-0.0.8/msaDocModels/wfl.py
-drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-24 17:15:28.740070 msaDocModels-0.0.8/msaDocModels.egg-info/
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3633 2022-11-24 17:15:28.000000 msaDocModels-0.0.8/msaDocModels.egg-info/PKG-INFO
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      442 2022-11-24 17:15:28.000000 msaDocModels-0.0.8/msaDocModels.egg-info/SOURCES.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        1 2022-11-24 17:15:28.000000 msaDocModels-0.0.8/msaDocModels.egg-info/dependency_links.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)       13 2022-11-24 17:15:28.000000 msaDocModels-0.0.8/msaDocModels.egg-info/top_level.txt
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        1 2022-11-18 15:00:50.000000 msaDocModels-0.0.8/msaDocModels.egg-info/zip-safe
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)       38 2022-11-24 17:15:28.740070 msaDocModels-0.0.8/setup.cfg
--rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2154 2022-11-09 11:53:39.000000 msaDocModels-0.0.8/setup.py
+drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-25 11:39:48.407721 msaDocModels-0.0.9/
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1099 2022-11-09 11:53:39.000000 msaDocModels-0.0.9/LICENCE
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3633 2022-11-25 11:39:48.407721 msaDocModels-0.0.9/PKG-INFO
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2153 2022-11-09 11:53:39.000000 msaDocModels-0.0.9/README.md
+drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-25 11:39:48.407721 msaDocModels-0.0.9/msaDocModels/
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      484 2022-11-25 11:38:58.000000 msaDocModels-0.0.9/msaDocModels/__init__.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      562 2022-11-18 16:38:17.000000 msaDocModels-0.0.9/msaDocModels/health.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3731 2022-11-09 11:53:39.000000 msaDocModels-0.0.9/msaDocModels/msg.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      387 2022-11-22 10:24:03.000000 msaDocModels-0.0.9/msaDocModels/openapi.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2412 2022-11-18 16:38:17.000000 msaDocModels-0.0.9/msaDocModels/scheduler.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    13177 2022-11-25 11:19:58.000000 msaDocModels-0.0.9/msaDocModels/sdu.py
+drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-25 11:39:48.407721 msaDocModels-0.0.9/msaDocModels/utils/
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-21 13:25:40.000000 msaDocModels-0.0.9/msaDocModels/utils/__init__.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     1825 2022-11-10 09:04:48.000000 msaDocModels-0.0.9/msaDocModels/utils/htmlutils.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)    22525 2022-11-09 11:53:39.000000 msaDocModels-0.0.9/msaDocModels/wdc.py
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2209 2022-11-09 11:53:39.000000 msaDocModels-0.0.9/msaDocModels/wfl.py
+drwxrwxr-x   0 vitaliy   (1000) vitaliy   (1000)        0 2022-11-25 11:39:48.407721 msaDocModels-0.0.9/msaDocModels.egg-info/
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     3633 2022-11-25 11:39:48.000000 msaDocModels-0.0.9/msaDocModels.egg-info/PKG-INFO
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)      442 2022-11-25 11:39:48.000000 msaDocModels-0.0.9/msaDocModels.egg-info/SOURCES.txt
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        1 2022-11-25 11:39:48.000000 msaDocModels-0.0.9/msaDocModels.egg-info/dependency_links.txt
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)       13 2022-11-25 11:39:48.000000 msaDocModels-0.0.9/msaDocModels.egg-info/top_level.txt
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)        1 2022-11-18 15:00:50.000000 msaDocModels-0.0.9/msaDocModels.egg-info/zip-safe
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)       38 2022-11-25 11:39:48.407721 msaDocModels-0.0.9/setup.cfg
+-rw-rw-r--   0 vitaliy   (1000) vitaliy   (1000)     2154 2022-11-09 11:53:39.000000 msaDocModels-0.0.9/setup.py
```

### Comparing `msaDocModels-0.0.8/LICENCE` & `msaDocModels-0.0.9/LICENCE`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/PKG-INFO` & `msaDocModels-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: msaDocModels
-Version: 0.0.8
+Version: 0.0.9
 Summary: msaDocModels - MSA Document Pydantic Models and Schemas, used to store Parser, NLP, NLU and AI results for processed documents
 Home-page: https://github.com/swelcker/msaDocModels
 Download-URL: http://pypi.python.org/pypi/msaDocModels
 Author: Stefan Welcker
 Author-email: stefan@u2d.ai
 License: MIT
 Project-URL: Documentation, http://msaDocModels.u2d.ai/
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: msaDocModels Version: 0.0.8 Summary: msaDocModels -
+Metadata-Version: 2.1 Name: msaDocModels Version: 0.0.9 Summary: msaDocModels -
 MSA Document Pydantic Models and Schemas, used to store Parser, NLP, NLU and AI
 results for processed documents Home-page: https://github.com/swelcker/
 msaDocModels Download-URL: http://pypi.python.org/pypi/msaDocModels Author:
 Stefan Welcker Author-email: stefan@u2d.ai License: MIT Project-URL:
 Documentation, http://msaDocModels.u2d.ai/ Project-URL: Source, https://
 github.com/swelcker/msaDocModels Project-URL: Tracker, https://github.com/
 swelcker/msaDocModels/issues Classifier: Development Status :: 4 - Beta
```

### Comparing `msaDocModels-0.0.8/README.md` & `msaDocModels-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels/health.py` & `msaDocModels-0.0.9/msaDocModels/health.py`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels/msg.py` & `msaDocModels-0.0.9/msaDocModels/msg.py`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels/scheduler.py` & `msaDocModels-0.0.9/msaDocModels/scheduler.py`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels/sdu.py` & `msaDocModels-0.0.9/msaDocModels/sdu.py`

 * *Files 0% similar despite different names*

```diff
@@ -97,15 +97,15 @@
     code: str = "unknown"  # Short de, en etc.
     lang: str = "unknown"  # Language name like german.
     reliable: bool = False  # is the detected result reliable.
     proportion: int = -1  # Proportion of the text in this language.
     bytes: int = -1  # Bytes of the text in this language.
     confidence: float = -1  # Confidence from 0.01 to 1.0.
     winner: Optional[str] = None  # Selected overall Winner
-    details: Optional[Tuple] = tuple()  # Details of the top 3 detected languages.
+    details: Optional[List] = List()  # Details of the top 3 detected languages.
 
     class Config:
         orm_mode = False
 
 
 class SDUStatistic(BaseModel):
     """Text Statistics Pydantic Model."""
```

### Comparing `msaDocModels-0.0.8/msaDocModels/utils/htmlutils.py` & `msaDocModels-0.0.9/msaDocModels/utils/htmlutils.py`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels/wdc.py` & `msaDocModels-0.0.9/msaDocModels/wdc.py`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels/wfl.py` & `msaDocModels-0.0.9/msaDocModels/wfl.py`

 * *Files identical despite different names*

### Comparing `msaDocModels-0.0.8/msaDocModels.egg-info/PKG-INFO` & `msaDocModels-0.0.9/msaDocModels.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: msaDocModels
-Version: 0.0.8
+Version: 0.0.9
 Summary: msaDocModels - MSA Document Pydantic Models and Schemas, used to store Parser, NLP, NLU and AI results for processed documents
 Home-page: https://github.com/swelcker/msaDocModels
 Download-URL: http://pypi.python.org/pypi/msaDocModels
 Author: Stefan Welcker
 Author-email: stefan@u2d.ai
 License: MIT
 Project-URL: Documentation, http://msaDocModels.u2d.ai/
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: msaDocModels Version: 0.0.8 Summary: msaDocModels -
+Metadata-Version: 2.1 Name: msaDocModels Version: 0.0.9 Summary: msaDocModels -
 MSA Document Pydantic Models and Schemas, used to store Parser, NLP, NLU and AI
 results for processed documents Home-page: https://github.com/swelcker/
 msaDocModels Download-URL: http://pypi.python.org/pypi/msaDocModels Author:
 Stefan Welcker Author-email: stefan@u2d.ai License: MIT Project-URL:
 Documentation, http://msaDocModels.u2d.ai/ Project-URL: Source, https://
 github.com/swelcker/msaDocModels Project-URL: Tracker, https://github.com/
 swelcker/msaDocModels/issues Classifier: Development Status :: 4 - Beta
```

### Comparing `msaDocModels-0.0.8/setup.py` & `msaDocModels-0.0.9/setup.py`

 * *Files identical despite different names*

