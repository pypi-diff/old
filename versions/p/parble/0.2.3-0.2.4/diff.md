# Comparing `tmp/parble-0.2.3.tar.gz` & `tmp/parble-0.2.4.tar.gz`

## Comparing `parble-0.2.3.tar` & `parble-0.2.4.tar`

### file list

```diff
@@ -1,29 +1,29 @@
--rw-r--r--   0        0        0      268 2020-02-02 00:00:00.000000 parble-0.2.3/parble/__init__.py
--rw-r--r--   0        0        0      176 2020-02-02 00:00:00.000000 parble-0.2.3/parble/_version.py
--rw-r--r--   0        0        0     1517 2020-02-02 00:00:00.000000 parble-0.2.3/parble/client.py
--rw-r--r--   0        0        0     4650 2020-02-02 00:00:00.000000 parble-0.2.3/parble/commands.py
--rw-r--r--   0        0        0      458 2020-02-02 00:00:00.000000 parble-0.2.3/parble/exceptions.py
--rw-r--r--   0        0        0     2308 2020-02-02 00:00:00.000000 parble-0.2.3/parble/models.py
--rw-r--r--   0        0        0     2887 2020-02-02 00:00:00.000000 parble-0.2.3/parble/sdk.py
--rw-r--r--   0        0        0     2089 2020-02-02 00:00:00.000000 parble-0.2.3/parble/session.py
--rw-r--r--   0        0        0      961 2020-02-02 00:00:00.000000 parble-0.2.3/parble/settings.py
--rw-r--r--   0        0        0     1391 2020-02-02 00:00:00.000000 parble-0.2.3/parble/utils.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 parble-0.2.3/parble/resources/__init__.py
--rw-r--r--   0        0        0      288 2020-02-02 00:00:00.000000 parble-0.2.3/parble/resources/base.py
--rw-r--r--   0        0        0     1039 2020-02-02 00:00:00.000000 parble-0.2.3/parble/resources/files.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 parble-0.2.3/tests/__init__.py
--rw-r--r--   0        0        0     1572 2020-02-02 00:00:00.000000 parble-0.2.3/tests/conftest.py
--rw-r--r--   0        0        0     1306 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_client.py
--rw-r--r--   0        0        0     4196 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_commands.py
--rw-r--r--   0        0        0      682 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_models.py
--rw-r--r--   0        0        0     2397 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_sdk.py
--rw-r--r--   0        0        0     2208 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_session.py
--rw-r--r--   0        0        0      913 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_settings.py
--rw-r--r--   0        0        0     1111 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_utils.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_resources/__init__.py
--rw-r--r--   0        0        0     2042 2020-02-02 00:00:00.000000 parble-0.2.3/tests/test_resources/test_files.py
--rw-r--r--   0        0        0     1388 2020-02-02 00:00:00.000000 parble-0.2.3/.gitignore
--rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 parble-0.2.3/LICENSE
--rw-r--r--   0        0        0       82 2020-02-02 00:00:00.000000 parble-0.2.3/README.md
--rw-r--r--   0        0        0     2379 2020-02-02 00:00:00.000000 parble-0.2.3/pyproject.toml
--rw-r--r--   0        0        0     1520 2020-02-02 00:00:00.000000 parble-0.2.3/PKG-INFO
+-rw-r--r--   0        0        0      268 2020-02-02 00:00:00.000000 parble-0.2.4/parble/__init__.py
+-rw-r--r--   0        0        0      176 2020-02-02 00:00:00.000000 parble-0.2.4/parble/_version.py
+-rw-r--r--   0        0        0     1517 2020-02-02 00:00:00.000000 parble-0.2.4/parble/client.py
+-rw-r--r--   0        0        0     4650 2020-02-02 00:00:00.000000 parble-0.2.4/parble/commands.py
+-rw-r--r--   0        0        0      458 2020-02-02 00:00:00.000000 parble-0.2.4/parble/exceptions.py
+-rw-r--r--   0        0        0     2318 2020-02-02 00:00:00.000000 parble-0.2.4/parble/models.py
+-rw-r--r--   0        0        0     2887 2020-02-02 00:00:00.000000 parble-0.2.4/parble/sdk.py
+-rw-r--r--   0        0        0     2089 2020-02-02 00:00:00.000000 parble-0.2.4/parble/session.py
+-rw-r--r--   0        0        0      961 2020-02-02 00:00:00.000000 parble-0.2.4/parble/settings.py
+-rw-r--r--   0        0        0     1391 2020-02-02 00:00:00.000000 parble-0.2.4/parble/utils.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 parble-0.2.4/parble/resources/__init__.py
+-rw-r--r--   0        0        0      288 2020-02-02 00:00:00.000000 parble-0.2.4/parble/resources/base.py
+-rw-r--r--   0        0        0     1039 2020-02-02 00:00:00.000000 parble-0.2.4/parble/resources/files.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 parble-0.2.4/tests/__init__.py
+-rw-r--r--   0        0        0     1572 2020-02-02 00:00:00.000000 parble-0.2.4/tests/conftest.py
+-rw-r--r--   0        0        0     1306 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_client.py
+-rw-r--r--   0        0        0     4196 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_commands.py
+-rw-r--r--   0        0        0      932 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_models.py
+-rw-r--r--   0        0        0     2397 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_sdk.py
+-rw-r--r--   0        0        0     2208 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_session.py
+-rw-r--r--   0        0        0      913 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_settings.py
+-rw-r--r--   0        0        0     1111 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_utils.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_resources/__init__.py
+-rw-r--r--   0        0        0     2042 2020-02-02 00:00:00.000000 parble-0.2.4/tests/test_resources/test_files.py
+-rw-r--r--   0        0        0     1388 2020-02-02 00:00:00.000000 parble-0.2.4/.gitignore
+-rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 parble-0.2.4/LICENSE
+-rw-r--r--   0        0        0       82 2020-02-02 00:00:00.000000 parble-0.2.4/README.md
+-rw-r--r--   0        0        0     2379 2020-02-02 00:00:00.000000 parble-0.2.4/pyproject.toml
+-rw-r--r--   0        0        0     1520 2020-02-02 00:00:00.000000 parble-0.2.4/PKG-INFO
```

### Comparing `parble-0.2.3/parble/client.py` & `parble-0.2.4/parble/client.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/parble/commands.py` & `parble-0.2.4/parble/commands.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/parble/models.py` & `parble-0.2.4/parble/models.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 
 class Timings(BaseModel):
     """
     Timings information for a file
     """
 
     upload: datetime
-    done: datetime
+    done: Optional[datetime]
 
 
 class Classification(BaseModel):
     """
     Classification information about a single document
     """
```

### Comparing `parble-0.2.3/parble/sdk.py` & `parble-0.2.4/parble/sdk.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/parble/session.py` & `parble-0.2.4/parble/session.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/parble/settings.py` & `parble-0.2.4/parble/settings.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/parble/utils.py` & `parble-0.2.4/parble/utils.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/parble/resources/files.py` & `parble-0.2.4/parble/resources/files.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/conftest.py` & `parble-0.2.4/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_client.py` & `parble-0.2.4/tests/test_client.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_commands.py` & `parble-0.2.4/tests/test_commands.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_sdk.py` & `parble-0.2.4/tests/test_sdk.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_session.py` & `parble-0.2.4/tests/test_session.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_settings.py` & `parble-0.2.4/tests/test_settings.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_utils.py` & `parble-0.2.4/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/tests/test_resources/test_files.py` & `parble-0.2.4/tests/test_resources/test_files.py`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/.gitignore` & `parble-0.2.4/.gitignore`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/LICENSE` & `parble-0.2.4/LICENSE`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/pyproject.toml` & `parble-0.2.4/pyproject.toml`

 * *Files identical despite different names*

### Comparing `parble-0.2.3/PKG-INFO` & `parble-0.2.4/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: parble
-Version: 0.2.3
+Version: 0.2.4
 Summary: Parble Python SDK
 Project-URL: Documentation, https://github.com/parblelabs/parble-python#readme
 Project-URL: Issues, https://github.com/parblelabs/parble-python/issues
 Project-URL: Source, https://github.com/parblelabs/parble-python
 Author-email: Timothé Perez <timothe@parble.com>
 License-File: LICENSE
 Classifier: Development Status :: 4 - Beta
```

