# Comparing `tmp/davt_services_python-202304.0.1.tar.gz` & `tmp/davt_services_python-202304.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "davt_services_python-202304.0.1.tar", max compression
+gzip compressed data, was "davt_services_python-202304.0.2.tar", max compression
```

## Comparing `davt_services_python-202304.0.1.tar` & `davt_services_python-202304.0.2.tar`

### file list

```diff
@@ -1,28 +1,28 @@
--rw-r--r--   0        0        0    11357 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/LICENSE.md
--rw-r--r--   0        0        0      324 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/README.md
--rw-r--r--   0        0        0      961 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/davt_services_python/__init__.py
--rw-r--r--   0        0        0      857 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/davt_services_python/__main__.py
--rw-r--r--   0        0        0     1116 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/davt_services_python/creator_service/__init__.py
--rw-r--r--   0        0        0    41323 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/davt_services_python/creator_service/dataset_metadata.py
--rw-r--r--   0        0        0    32631 2023-04-07 02:21:54.285941 davt_services_python-202304.0.1/davt_services_python/creator_service/environment_metadata.py
--rw-r--r--   0        0        0    35950 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/creator_service/job_metadata.py
--rw-r--r--   0        0        0     2251 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/creator_service/logging_metadata.py
--rw-r--r--   0        0        0    22310 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/creator_service/pipeline_metadata.py
--rw-r--r--   0        0        0     1396 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/__init__.py
--rw-r--r--   0        0        0    33691 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_convert.py
--rw-r--r--   0        0        0     8716 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_core.py
--rw-r--r--   0        0        0    24923 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_crud.py
--rw-r--r--   0        0        0     3767 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_extract.py
--rw-r--r--   0        0        0     1990 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/environment_core.py
--rw-r--r--   0        0        0    26168 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/environment_file.py
--rw-r--r--   0        0        0     4656 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/environment_logging.py
--rw-r--r--   0        0        0     4581 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/environment_spark.py
--rw-r--r--   0        0        0     4654 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/job_core.py
--rw-r--r--   0        0        0    17224 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/repo_core.py
--rw-r--r--   0        0        0    14616 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/developer_service/security_core.py
--rw-r--r--   0        0        0      779 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/it_admin_service/__init__.py
--rw-r--r--   0        0        0      835 2023-04-07 02:21:54.289941 davt_services_python-202304.0.1/davt_services_python/version_service/__init__.py
--rw-r--r--   0        0        0     3313 2023-04-07 02:24:58.378708 davt_services_python-202304.0.1/pyproject.toml
--rw-r--r--   0        0        0      162 2023-04-07 02:21:54.293941 davt_services_python-202304.0.1/setup.cfg
--rw-r--r--   0        0        0      125 2023-04-07 02:21:54.297941 davt_services_python-202304.0.1/setup.py
--rw-r--r--   0        0        0     3083 1970-01-01 00:00:00.000000 davt_services_python-202304.0.1/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/LICENSE.md
+-rw-r--r--   0        0        0      324 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/README.md
+-rw-r--r--   0        0        0      961 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/__init__.py
+-rw-r--r--   0        0        0      857 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/__main__.py
+-rw-r--r--   0        0        0     1116 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/creator_service/__init__.py
+-rw-r--r--   0        0        0    41323 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/creator_service/dataset_metadata.py
+-rw-r--r--   0        0        0    32631 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/creator_service/environment_metadata.py
+-rw-r--r--   0        0        0    35950 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/creator_service/job_metadata.py
+-rw-r--r--   0        0        0     2251 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/creator_service/logging_metadata.py
+-rw-r--r--   0        0        0    22367 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/creator_service/pipeline_metadata.py
+-rw-r--r--   0        0        0     1396 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/__init__.py
+-rw-r--r--   0        0        0    33691 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_convert.py
+-rw-r--r--   0        0        0     8716 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_core.py
+-rw-r--r--   0        0        0    24835 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_crud.py
+-rw-r--r--   0        0        0     3767 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_extract.py
+-rw-r--r--   0        0        0     1990 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/environment_core.py
+-rw-r--r--   0        0        0    26168 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/environment_file.py
+-rw-r--r--   0        0        0     4656 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/environment_logging.py
+-rw-r--r--   0        0        0     4581 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/environment_spark.py
+-rw-r--r--   0        0        0     4654 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/job_core.py
+-rw-r--r--   0        0        0    17224 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/repo_core.py
+-rw-r--r--   0        0        0    14616 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/developer_service/security_core.py
+-rw-r--r--   0        0        0      779 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/it_admin_service/__init__.py
+-rw-r--r--   0        0        0      835 2023-04-07 02:56:37.662155 davt_services_python-202304.0.2/davt_services_python/version_service/__init__.py
+-rw-r--r--   0        0        0     3313 2023-04-07 02:58:58.372094 davt_services_python-202304.0.2/pyproject.toml
+-rw-r--r--   0        0        0      162 2023-04-07 02:56:37.670154 davt_services_python-202304.0.2/setup.cfg
+-rw-r--r--   0        0        0      125 2023-04-07 02:56:37.670154 davt_services_python-202304.0.2/setup.py
+-rw-r--r--   0        0        0     3083 1970-01-01 00:00:00.000000 davt_services_python-202304.0.2/PKG-INFO
```

### Comparing `davt_services_python-202304.0.1/LICENSE.md` & `davt_services_python-202304.0.2/LICENSE.md`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/__init__.py` & `davt_services_python-202304.0.2/davt_services_python/__init__.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/__main__.py` & `davt_services_python-202304.0.2/davt_services_python/__main__.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/creator_service/__init__.py` & `davt_services_python-202304.0.2/davt_services_python/creator_service/__init__.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/creator_service/dataset_metadata.py` & `davt_services_python-202304.0.2/davt_services_python/creator_service/dataset_metadata.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/creator_service/environment_metadata.py` & `davt_services_python-202304.0.2/davt_services_python/creator_service/environment_metadata.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/creator_service/job_metadata.py` & `davt_services_python-202304.0.2/davt_services_python/creator_service/job_metadata.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/creator_service/logging_metadata.py` & `davt_services_python-202304.0.2/davt_services_python/creator_service/logging_metadata.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/creator_service/pipeline_metadata.py` & `davt_services_python-202304.0.2/davt_services_python/creator_service/pipeline_metadata.py`

 * *Files 1% similar despite different names*

```diff
@@ -184,15 +184,16 @@
         dir_name_python = "".join([base_path, "/autogenerated/python/"])
         # clean up double slashes
         dir_name_python = dir_name_python.replace('//','/')
         pipeline_name = pipeline_name.replace(project_id, "")
         pipeline_name = pipeline_name.replace(".", "")
         pipeline_name = project_id + "_" + pipeline_name
         path_to_execute = "".join([dir_name_python, pipeline_name])
-        database_prefix = "davt_" + project_id + "_" + environment
+        # database_prefix = "davt_" + project_id + "_" + environment
+        database_prefix = config["davt_database_name"]
         arg_dictionary["live_prefix"] = live_prefix
         arg_dictionary["environment_for_live"] = environment_for_live
         arg_dictionary["database_prefix"] = database_prefix
 
         config_pipeline["arg_dictionary"] = arg_dictionary
         config_pipeline["path_to_execute"] = path_to_execute
         print(f"config_pipeline:{str(config_pipeline)}")
```

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/__init__.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/__init__.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_convert.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_convert.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_core.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_core.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_crud.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_crud.py`

 * *Files 1% similar despite different names*

```diff
@@ -114,18 +114,15 @@
         if mm_param is None:
             mm_param = ""
 
         if dd_param is None:
             dd_param = ""
 
         dataset_name_list = full_dataset_name.split(".")
-        if dataset_name_list[0] is not None:
-            database_name = dataset_name_list[0]
-        else:
-            database_name = None
+        database_name = config["davt_database_name"]
 
         if dataset_name_list[1] is not None:
             dataset_name = dataset_name_list[1]
         else:
             dataset_name = None
 
         if file_format == "delta":
```

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/dataset_extract.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/dataset_extract.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/environment_core.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/environment_core.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/environment_file.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/environment_file.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/environment_logging.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/environment_logging.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/environment_spark.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/environment_spark.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/job_core.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/job_core.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/repo_core.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/repo_core.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/developer_service/security_core.py` & `davt_services_python-202304.0.2/davt_services_python/developer_service/security_core.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/it_admin_service/__init__.py` & `davt_services_python-202304.0.2/davt_services_python/it_admin_service/__init__.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/davt_services_python/version_service/__init__.py` & `davt_services_python-202304.0.2/davt_services_python/version_service/__init__.py`

 * *Files identical despite different names*

### Comparing `davt_services_python-202304.0.1/pyproject.toml` & `davt_services_python-202304.0.2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 [project.urls]
 "Homepage" = "https://test.pypi.org/project/davt-services-python"
 "Documentation" = "https://gift.readthedocs.io"
 "Repository" = "https://github.com/cdcent/davt"
 
 [tool.poetry]
 name="davt_services_python"
-version="202304.0.1"
+version="202304.0.2"
 description="Data, Analytics and Visualization Templates (DAVT) - Python Services"
 authors=["John Bowyer <zfi4@cdc.gov>"]
 readme = "README.md"
 license="Apache"
 homepage="https://test.pypi.org/project/davt-services-python"
 repository="https://github.com/cdcent/davt"
 classifiers=[
```

### Comparing `davt_services_python-202304.0.1/PKG-INFO` & `davt_services_python-202304.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: davt-services-python
-Version: 202304.0.1
+Version: 202304.0.2
 Summary: Data, Analytics and Visualization Templates (DAVT) - Python Services
 Home-page: https://test.pypi.org/project/davt-services-python
 License: Apache
 Author: John Bowyer
 Author-email: zfi4@cdc.gov
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 4 - Beta
```

