# Comparing `tmp/wizata-dsapi-0.0.98.tar.gz` & `tmp/wizata-dsapi-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "wizata-dsapi-0.0.98.tar", last modified: Wed Mar 15 14:46:34 2023, max compression
+gzip compressed data, was "wizata-dsapi-0.0.99.tar", last modified: Wed Mar 15 21:02:15 2023, max compression
```

## Comparing `wizata-dsapi-0.0.98.tar` & `wizata-dsapi-0.0.99.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxrwxrwx   0        0        0        0 2023-03-15 14:46:34.758936 wizata-dsapi-0.0.98/
--rw-rw-rw-   0        0        0    11556 2023-03-03 13:11:49.000000 wizata-dsapi-0.0.98/LICENSE.txt
--rw-rw-rw-   0        0        0      177 2023-03-15 14:46:34.758936 wizata-dsapi-0.0.98/PKG-INFO
--rw-rw-rw-   0        0        0      253 2023-03-03 13:11:49.000000 wizata-dsapi-0.0.98/README.rst
--rw-rw-rw-   0        0        0       42 2023-03-15 14:46:34.759930 wizata-dsapi-0.0.98/setup.cfg
--rw-rw-rw-   0        0        0     1213 2023-03-15 14:45:36.000000 wizata-dsapi-0.0.98/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-15 14:46:34.735931 wizata-dsapi-0.0.98/wizata_dsapi/
--rw-rw-rw-   0        0        0      430 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/__init__.py
--rw-rw-rw-   0        0        0     1909 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/dataframe_toolkit.py
--rw-rw-rw-   0        0        0      702 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/ds_dataframe.py
--rw-rw-rw-   0        0        0     3122 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/dsapi_json_encoder.py
--rw-rw-rw-   0        0        0     4273 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/execution.py
--rw-rw-rw-   0        0        0     2644 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/mlmodel.py
--rw-rw-rw-   0        0        0     1313 2023-03-10 09:04:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/model_toolkit.py
--rw-rw-rw-   0        0        0     1018 2023-03-15 14:45:36.000000 wizata-dsapi-0.0.98/wizata_dsapi/plot.py
--rw-rw-rw-   0        0        0     7229 2023-03-10 09:04:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/request.py
--rw-rw-rw-   0        0        0     3166 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/script.py
--rw-rw-rw-   0        0        0      487 2023-03-06 18:04:49.000000 wizata-dsapi-0.0.98/wizata_dsapi/wizard_function.py
--rw-rw-rw-   0        0        0    13837 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.98/wizata_dsapi/wizata_dsapi_client.py
-drwxrwxrwx   0        0        0        0 2023-03-15 14:46:34.756971 wizata-dsapi-0.0.98/wizata_dsapi.egg-info/
--rw-rw-rw-   0        0        0      177 2023-03-15 14:46:34.000000 wizata-dsapi-0.0.98/wizata_dsapi.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      549 2023-03-15 14:46:34.000000 wizata-dsapi-0.0.98/wizata_dsapi.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-15 14:46:34.000000 wizata-dsapi-0.0.98/wizata_dsapi.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      538 2023-03-15 14:46:34.000000 wizata-dsapi-0.0.98/wizata_dsapi.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-03-15 14:46:34.000000 wizata-dsapi-0.0.98/wizata_dsapi.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-15 21:02:15.261933 wizata-dsapi-0.0.99/
+-rw-rw-rw-   0        0        0    11556 2023-03-03 13:11:49.000000 wizata-dsapi-0.0.99/LICENSE.txt
+-rw-rw-rw-   0        0        0      177 2023-03-15 21:02:15.259607 wizata-dsapi-0.0.99/PKG-INFO
+-rw-rw-rw-   0        0        0      253 2023-03-03 13:11:49.000000 wizata-dsapi-0.0.99/README.rst
+-rw-rw-rw-   0        0        0       42 2023-03-15 21:02:15.261933 wizata-dsapi-0.0.99/setup.cfg
+-rw-rw-rw-   0        0        0     1213 2023-03-15 21:02:11.000000 wizata-dsapi-0.0.99/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-15 21:02:15.210656 wizata-dsapi-0.0.99/wizata_dsapi/
+-rw-rw-rw-   0        0        0      430 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/__init__.py
+-rw-rw-rw-   0        0        0     1909 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/dataframe_toolkit.py
+-rw-rw-rw-   0        0        0      702 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/ds_dataframe.py
+-rw-rw-rw-   0        0        0     3122 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/dsapi_json_encoder.py
+-rw-rw-rw-   0        0        0     4273 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/execution.py
+-rw-rw-rw-   0        0        0     2644 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/mlmodel.py
+-rw-rw-rw-   0        0        0     1313 2023-03-10 09:04:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/model_toolkit.py
+-rw-rw-rw-   0        0        0     1010 2023-03-15 21:02:11.000000 wizata-dsapi-0.0.99/wizata_dsapi/plot.py
+-rw-rw-rw-   0        0        0     7229 2023-03-10 09:04:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/request.py
+-rw-rw-rw-   0        0        0     3166 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/script.py
+-rw-rw-rw-   0        0        0      487 2023-03-06 18:04:49.000000 wizata-dsapi-0.0.99/wizata_dsapi/wizard_function.py
+-rw-rw-rw-   0        0        0    13837 2023-03-15 13:29:01.000000 wizata-dsapi-0.0.99/wizata_dsapi/wizata_dsapi_client.py
+drwxrwxrwx   0        0        0        0 2023-03-15 21:02:15.256776 wizata-dsapi-0.0.99/wizata_dsapi.egg-info/
+-rw-rw-rw-   0        0        0      177 2023-03-15 21:02:15.000000 wizata-dsapi-0.0.99/wizata_dsapi.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      549 2023-03-15 21:02:15.000000 wizata-dsapi-0.0.99/wizata_dsapi.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-15 21:02:15.000000 wizata-dsapi-0.0.99/wizata_dsapi.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      538 2023-03-15 21:02:15.000000 wizata-dsapi-0.0.99/wizata_dsapi.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-03-15 21:02:15.000000 wizata-dsapi-0.0.99/wizata_dsapi.egg-info/top_level.txt
```

### Comparing `wizata-dsapi-0.0.98/LICENSE.txt` & `wizata-dsapi-0.0.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/setup.py` & `wizata-dsapi-0.0.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup
 
 setup(
     name='wizata-dsapi',
-    version='0.0.98',
+    version='0.0.99',
     description='Wizata Data Science Toolkit',
     author='Wizata S.A.',
     author_email='info@wizata.com',
     packages=['wizata_dsapi'],
     install_requires=[
         'dill==0.3.6',
         'pandas==1.5.3',
```

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/dataframe_toolkit.py` & `wizata-dsapi-0.0.99/wizata_dsapi/dataframe_toolkit.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/ds_dataframe.py` & `wizata-dsapi-0.0.99/wizata_dsapi/ds_dataframe.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/dsapi_json_encoder.py` & `wizata-dsapi-0.0.99/wizata_dsapi/dsapi_json_encoder.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/execution.py` & `wizata-dsapi-0.0.99/wizata_dsapi/execution.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/mlmodel.py` & `wizata-dsapi-0.0.99/wizata_dsapi/mlmodel.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/model_toolkit.py` & `wizata-dsapi-0.0.99/wizata_dsapi/model_toolkit.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/plot.py` & `wizata-dsapi-0.0.99/wizata_dsapi/plot.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,24 +9,20 @@
         else:
             self.plot_id = plot_id
         self.name = None
         self.generatedById = None
         self.figure = None
 
     def from_json(self, json):
-
         if "id" in json.keys():
             self.plot_id = uuid.UUID(json["id"])
-
         if "name" in json.keys():
             self.name = json["name"]
-
         if "figure" in json.keys():
             self.figure = json["figure"]
-
         if "generatedById" in json.keys():
             self.generatedById = json["generatedById"]
 
     def to_json(self):
         obj = {
             "id": str(self.plot_id)
         }
```

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/request.py` & `wizata-dsapi-0.0.99/wizata_dsapi/request.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/script.py` & `wizata-dsapi-0.0.99/wizata_dsapi/script.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi/wizata_dsapi_client.py` & `wizata-dsapi-0.0.99/wizata_dsapi/wizata_dsapi_client.py`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi.egg-info/SOURCES.txt` & `wizata-dsapi-0.0.99/wizata_dsapi.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `wizata-dsapi-0.0.98/wizata_dsapi.egg-info/requires.txt` & `wizata-dsapi-0.0.99/wizata_dsapi.egg-info/requires.txt`

 * *Files identical despite different names*

