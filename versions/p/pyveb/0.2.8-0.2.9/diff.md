# Comparing `tmp/pyveb-0.2.8.tar.gz` & `tmp/pyveb-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyveb-0.2.8.tar", max compression
+gzip compressed data, was "pyveb-0.2.9.tar", max compression
```

## Comparing `pyveb-0.2.8.tar` & `pyveb-0.2.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
--rw-r--r--   0        0        0     1043 2023-02-10 13:11:37.758705 pyveb-0.2.8/LICENSE
--rw-r--r--   0        0        0      913 2023-02-10 13:11:52.890890 pyveb-0.2.8/pyproject.toml
--rw-r--r--   0        0        0      636 2023-02-10 13:11:37.758705 pyveb-0.2.8/readme.md
--rw-r--r--   0        0        0        0 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/__init__.py
--rw-r--r--   0        0        0     9533 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/api_client.py
--rw-r--r--   0        0        0     9981 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/common.py
--rw-r--r--   0        0        0     5704 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/config.py
--rw-r--r--   0        0        0     1054 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/custom_decorators.py
--rw-r--r--   0        0        0     2650 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/ftp_client.py
--rw-r--r--   0        0        0     5580 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/logger.py
--rw-r--r--   0        0        0     6349 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/lynx_client.py
--rw-r--r--   0        0        0     7705 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/parser.py
--rw-r--r--   0        0        0     2170 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/request_client.py
--rw-r--r--   0        0        0    16243 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/rs_client.py
--rw-r--r--   0        0        0    11306 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/s3_client.py
--rw-r--r--   0        0        0     6336 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/selenium_client.py
--rw-r--r--   0        0        0    22706 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/spark_client.py
--rw-r--r--   0        0        0     4085 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/sql_terra_client.py
--rw-r--r--   0        0        0     6726 2023-02-10 13:11:37.758705 pyveb-0.2.8/src/pyveb/tf_client.py
--rw-r--r--   0        0        0     1725 1970-01-01 00:00:00.000000 pyveb-0.2.8/setup.py
--rw-r--r--   0        0        0     2046 1970-01-01 00:00:00.000000 pyveb-0.2.8/PKG-INFO
+-rw-r--r--   0        0        0     1043 2023-02-13 10:30:50.917798 pyveb-0.2.9/LICENSE
+-rw-r--r--   0        0        0      913 2023-02-13 10:31:07.609665 pyveb-0.2.9/pyproject.toml
+-rw-r--r--   0        0        0      636 2023-02-13 10:30:50.917798 pyveb-0.2.9/readme.md
+-rw-r--r--   0        0        0        0 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/__init__.py
+-rw-r--r--   0        0        0     9533 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/api_client.py
+-rw-r--r--   0        0        0     9981 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/common.py
+-rw-r--r--   0        0        0     5844 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/config.py
+-rw-r--r--   0        0        0     1054 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/custom_decorators.py
+-rw-r--r--   0        0        0     2650 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/ftp_client.py
+-rw-r--r--   0        0        0     5580 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/logger.py
+-rw-r--r--   0        0        0     6349 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/lynx_client.py
+-rw-r--r--   0        0        0     7705 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/parser.py
+-rw-r--r--   0        0        0     2170 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/request_client.py
+-rw-r--r--   0        0        0    16243 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/rs_client.py
+-rw-r--r--   0        0        0    11306 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/s3_client.py
+-rw-r--r--   0        0        0     6336 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/selenium_client.py
+-rw-r--r--   0        0        0    22706 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/spark_client.py
+-rw-r--r--   0        0        0     4085 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/sql_terra_client.py
+-rw-r--r--   0        0        0     6726 2023-02-13 10:30:50.917798 pyveb-0.2.9/src/pyveb/tf_client.py
+-rw-r--r--   0        0        0     1725 1970-01-01 00:00:00.000000 pyveb-0.2.9/setup.py
+-rw-r--r--   0        0        0     2046 1970-01-01 00:00:00.000000 pyveb-0.2.9/PKG-INFO
```

### Comparing `pyveb-0.2.8/LICENSE` & `pyveb-0.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/pyproject.toml` & `pyveb-0.2.9/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 
 [tool.poetry]
-version = "0.2.8"
+version = "0.2.9"
 name = "pyveb"
 authors = ["pieter <pieter.de.petter@veb.be>"]
 description = "Package containing common code and reusable components for pipelines and dags"
 readme = "readme.md"
 license = "MIT"
 classifiers = [
     "Programming Language :: Python :: 3",
```

### Comparing `pyveb-0.2.8/readme.md` & `pyveb-0.2.9/readme.md`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/api_client.py` & `pyveb-0.2.9/src/pyveb/api_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/common.py` & `pyveb-0.2.9/src/pyveb/common.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/config.py` & `pyveb-0.2.9/src/pyveb/config.py`

 * *Files 4% similar despite different names*

```diff
@@ -36,15 +36,15 @@
     year = execution_date.year
     return f"year={year}/month={month}/day={day}/"
 
 class Config():
 
     CONFIG_NAME = 'config.yml'
     CONFIG_PATH_AWS = f'/app/{CONFIG_NAME}'
-    REQUIRED_GENERAL_KEYS = ['pipeline_name', 'pipeline_bucket', 'pipeline_type', 'prefix_logs', 'prefix_raw', 'prefix_processed', 'tasks']
+    REQUIRED_GENERAL_KEYS = ['pipeline_name', 'pipeline_bucket', 'pipeline_type', 'prefix_env', 'prefix_logs', 'prefix_raw', 'prefix_processed', 'tasks']
 
     def __init__(self, **kwargs):
         self.env = kwargs.get('env')
         self.pipeline_type = kwargs.get('type')
         self.airflow_execution_date = kwargs.get('airflow_execution_date')
         self.task = kwargs.get('task')
         self.event_bucket = kwargs.get('event_bucket')
@@ -72,33 +72,34 @@
         return config
 
     def _parse_general(self) -> dict:
         """
             General section is valid for all environments
         """
         if self.file.general:
-            d = self.file.general
-
+            dic = self.file.general
+            
             # check of all required keys are set up in config, are <> null/empty and have correct type
             for i in Config.REQUIRED_GENERAL_KEYS:
                 try:
-                    d[i]
+                    dic[i]
                 except KeyError as e:
                     logging.error(f'Key \'{i}\' not found in config.yml')
                 # print(i)
-                assert d[i], f"key general.{i} is empty or NULL"
+                assert dic[i], f"key general.{i} is empty or NULL"
                 if i in  ['tasks', 'pipeline_type']:
-                    assert isinstance(d[i], list), f"key general.{i} is not a list"
+                    assert isinstance(dic[i], list), f"key general.{i} is not a list"
                 else: 
-                    assert isinstance(d[i], str), f"key general.{i} is not a str"    
-
+                    assert isinstance(dic[i], str), f"key general.{i} is not a str" 
+            
+            dic['prefix_env'] = getattr(dic.prefix_env, self.env)   
             # add additional 'calculated' fields to config 
-            d['partition_raw'] = f'{self.env}/{d.pipeline_name}/{self.pipeline_type}/{d.prefix_raw}/{self.task}/{create_partition_key(self.airflow_execution_date)}'
-            d['partition_processed'] = f'{self.env}/{d.pipeline_name}/{self.pipeline_type}/{d.prefix_processed}/{self.task}/{create_partition_key(self.airflow_execution_date)}'
-            return d
+            dic['partition_raw'] = f'{dic.prefix_env}/{dic.pipeline_name}/{self.pipeline_type}/{dic.prefix_raw}/{self.task}/{create_partition_key(self.airflow_execution_date)}'
+            dic['partition_processed'] = f'{dic.prefix_env}/{dic.pipeline_name}/{self.pipeline_type}/{dic.prefix_processed}/{self.task}/{create_partition_key(self.airflow_execution_date)}'
+            return dic
         logging.error('Mandatory general section not found')
         sys.exit(1)
 
     ## TO DO - add proper error handling in case env or task is not setup for a required attribute
     def _parse_source(self) -> dict:
         if self.file.source:
             dic = self.file.source
```

### Comparing `pyveb-0.2.8/src/pyveb/custom_decorators.py` & `pyveb-0.2.9/src/pyveb/custom_decorators.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/ftp_client.py` & `pyveb-0.2.9/src/pyveb/ftp_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/logger.py` & `pyveb-0.2.9/src/pyveb/logger.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/lynx_client.py` & `pyveb-0.2.9/src/pyveb/lynx_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/parser.py` & `pyveb-0.2.9/src/pyveb/parser.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/request_client.py` & `pyveb-0.2.9/src/pyveb/request_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/rs_client.py` & `pyveb-0.2.9/src/pyveb/rs_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/s3_client.py` & `pyveb-0.2.9/src/pyveb/s3_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/selenium_client.py` & `pyveb-0.2.9/src/pyveb/selenium_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/spark_client.py` & `pyveb-0.2.9/src/pyveb/spark_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/sql_terra_client.py` & `pyveb-0.2.9/src/pyveb/sql_terra_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/src/pyveb/tf_client.py` & `pyveb-0.2.9/src/pyveb/tf_client.py`

 * *Files identical despite different names*

### Comparing `pyveb-0.2.8/setup.py` & `pyveb-0.2.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,15 @@
  'selenium>=4.5.0,<5.0.0',
  'simple-ddl-parser==0.26.5',
  'webdriver-manager==3.4.1',
  'xlrd>=2.0.0,<3.0.0']
 
 setup_kwargs = {
     'name': 'pyveb',
-    'version': '0.2.8',
+    'version': '0.2.9',
     'description': 'Package containing common code and reusable components for pipelines and dags',
     'long_description': '# General \n\nPackage containing resuable code components for data pipelines and dags deployed to pypi.\n\n# Usage\n\nInstall/Upgrade locally: \n\n```\n$ pip3 install pyveb\n$ pip3 install pyveb --upgrade\n```\n\nImport in python\n\n```\nimport pyveb\nfrom pyveb import selenium_client\n```\n\n\n# Update package\n\nPackage is automaticly deployed to pypi via github actions. Just commit and open a pull request. During the action workflow, the version will be automatically bumped and updated pyproject.toml is commited back. \n\n! in case a dependency is added to pyproject.toml, no workflow is started unless there are also changes to src/pyveb/** \n\n\n\n\n\n\n\n\n\n',
     'author': 'pieter',
     'author_email': 'pieter.de.petter@veb.be',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `pyveb-0.2.8/PKG-INFO` & `pyveb-0.2.9/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyveb
-Version: 0.2.8
+Version: 0.2.9
 Summary: Package containing common code and reusable components for pipelines and dags
 License: MIT
 Author: pieter
 Author-email: pieter.de.petter@veb.be
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

