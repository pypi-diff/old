# Comparing `tmp/data_ecosystem_services-202303.0.27.tar.gz` & `tmp/data_ecosystem_services-202303.0.28.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_ecosystem_services-202303.0.27.tar", max compression
+gzip compressed data, was "data_ecosystem_services-202303.0.28.tar", max compression
```

## Comparing `data_ecosystem_services-202303.0.27.tar` & `data_ecosystem_services-202303.0.28.tar`

### file list

```diff
@@ -1,29 +1,29 @@
--rw-r--r--   0        0        0      857 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/__main__.py
--rw-r--r--   0        0        0      916 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/admin_service/__init__.py
--rw-r--r--   0        0        0     4670 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/admin_service/environment_logging.py
--rw-r--r--   0        0        0      958 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/security_service/__init__.py
--rw-r--r--   0        0        0     3431 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/security_service/security_alation.py
--rw-r--r--   0        0        0    14614 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/security_service/security_core.py
--rw-r--r--   0        0        0     1115 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/__init__.py
--rw-r--r--   0        0        0    41337 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/dataset_metadata.py
--rw-r--r--   0        0        0    32651 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/environment_metadata.py
--rw-r--r--   0        0        0    36036 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/job_metadata.py
--rw-r--r--   0        0        0     2261 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/logging_metadata.py
--rw-r--r--   0        0        0    22310 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/pipeline_metadata.py
--rw-r--r--   0        0        0     1472 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/__init__.py
--rw-r--r--   0        0        0    33731 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_convert.py
--rw-r--r--   0        0        0     8716 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_core.py
--rw-r--r--   0        0        0    24963 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_crud.py
--rw-r--r--   0        0        0     3777 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_extract.py
--rw-r--r--   0        0        0     1997 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/environment_core.py
--rw-r--r--   0        0        0    26185 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/environment_file.py
--rw-r--r--   0        0        0     4589 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/environment_spark.py
--rw-r--r--   0        0        0     4654 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/job_core.py
--rw-r--r--   0        0        0    17224 2023-04-04 17:29:48.525811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/repo_core.py
--rw-r--r--   0        0        0    10094 2023-04-04 17:29:48.529811 data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_schema/manifest.py
--rw-r--r--   0        0        0    11357 2023-04-04 17:29:48.529811 data_ecosystem_services-202303.0.27/license.md
--rw-r--r--   0        0        0     3346 2023-04-04 17:33:17.210501 data_ecosystem_services-202303.0.27/pyproject.toml
--rw-r--r--   0        0        0    47124 2023-04-04 17:29:48.529811 data_ecosystem_services-202303.0.27/readme.md
--rw-r--r--   0        0        0      118 2023-04-04 17:29:48.529811 data_ecosystem_services-202303.0.27/setup.cfg
--rw-r--r--   0        0        0      127 2023-04-04 17:29:48.529811 data_ecosystem_services-202303.0.27/setup.py
--rw-r--r--   0        0        0    49936 1970-01-01 00:00:00.000000 data_ecosystem_services-202303.0.27/PKG-INFO
+-rw-r--r--   0        0        0      857 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/__main__.py
+-rw-r--r--   0        0        0      916 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/__init__.py
+-rw-r--r--   0        0        0     4670 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/environment_logging.py
+-rw-r--r--   0        0        0      958 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/__init__.py
+-rw-r--r--   0        0        0     3431 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_alation.py
+-rw-r--r--   0        0        0    14614 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_core.py
+-rw-r--r--   0        0        0     1115 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/__init__.py
+-rw-r--r--   0        0        0    41371 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/dataset_metadata.py
+-rw-r--r--   0        0        0    32651 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/environment_metadata.py
+-rw-r--r--   0        0        0    36036 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/job_metadata.py
+-rw-r--r--   0        0        0     2261 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/logging_metadata.py
+-rw-r--r--   0        0        0    22304 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/pipeline_metadata.py
+-rw-r--r--   0        0        0     1472 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/__init__.py
+-rw-r--r--   0        0        0    33731 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_convert.py
+-rw-r--r--   0        0        0     8716 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_core.py
+-rw-r--r--   0        0        0    24963 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_crud.py
+-rw-r--r--   0        0        0     3777 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_extract.py
+-rw-r--r--   0        0        0     1997 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_core.py
+-rw-r--r--   0        0        0    26185 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_file.py
+-rw-r--r--   0        0        0     4589 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_spark.py
+-rw-r--r--   0        0        0     4648 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/job_core.py
+-rw-r--r--   0        0        0    17224 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/repo_core.py
+-rw-r--r--   0        0        0    10094 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_schema/manifest.py
+-rw-r--r--   0        0        0    11357 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/license.md
+-rw-r--r--   0        0        0     3346 2023-04-07 02:29:33.133077 data_ecosystem_services-202303.0.28/pyproject.toml
+-rw-r--r--   0        0        0    47124 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/readme.md
+-rw-r--r--   0        0        0      118 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/setup.cfg
+-rw-r--r--   0        0        0      127 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/setup.py
+-rw-r--r--   0        0        0    49936 1970-01-01 00:00:00.000000 data_ecosystem_services-202303.0.28/PKG-INFO
```

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/__main__.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/__main__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/admin_service/__init__.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/admin_service/environment_logging.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/environment_logging.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/security_service/__init__.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/security_service/security_alation.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_alation.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/security_service/security_core.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/__init__.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/dataset_metadata.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/dataset_metadata.py`

 * *Files 0% similar despite different names*

```diff
@@ -700,16 +700,18 @@
                 encoding = row["encoding"].upper().strip()
             else:
                 encoding = "UTF-8"
                 print("Error encoding:{str(encoding)} is not a string")
 
         config_dataset["encoding"] = encoding
 
+        database_name = config["davt_database_name"]
+        
         full_dataset_name = (
-            "davt_" + project_id + "_" + environment + "." + dataset_name
+           database_name + "." + dataset_name
         )
         config_dataset["full_dataset_name"] = full_dataset_name
 
         frequency = row["frequency"]
         if frequency is None:
             frequency = "daily"
         else:
```

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/environment_metadata.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/environment_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/job_metadata.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/job_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/logging_metadata.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/logging_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/self_service/pipeline_metadata.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/pipeline_metadata.py`

 * *Files 1% similar despite different names*

```diff
@@ -184,15 +184,17 @@
         dir_name_python = "".join([base_path, "/autogenerated/python/"])
         # clean up double slashes
         dir_name_python = dir_name_python.replace('//','/')
         pipeline_name = pipeline_name.replace(project_id, "")
         pipeline_name = pipeline_name.replace(".", "")
         pipeline_name = project_id + "_" + pipeline_name
         path_to_execute = "".join([dir_name_python, pipeline_name])
-        database_prefix = "davt_" + project_id + "_" + environment
+
+        database_prefix = config["davt_database_name"]
+    
         arg_dictionary["live_prefix"] = live_prefix
         arg_dictionary["environment_for_live"] = environment_for_live
         arg_dictionary["database_prefix"] = database_prefix
 
         config_pipeline["arg_dictionary"] = arg_dictionary
         config_pipeline["path_to_execute"] = path_to_execute
         print(f"config_pipeline:{str(config_pipeline)}")
```

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/__init__.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_convert.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_convert.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_core.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_crud.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_crud.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/dataset_extract.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_extract.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/environment_core.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/environment_file.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_file.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/environment_spark.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_spark.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/job_core.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/job_core.py`

 * *Files 2% similar despite different names*

```diff
@@ -35,30 +35,30 @@
         virtual_env = os.path.basename(os.path.normpath(sys.prefix))
 
         if len(virtual_env.rsplit('_', 1)) == 1:
             if len(path.parts) > 2:
                 project_id = os.path.basename(os.path.normpath(path))
                 virtual_env = project_id + "_dev"
             else:
-                virtual_env = 'ddt_ops_dev'
-                project_id = "ddt_ops"
+                virtual_env = 'ocio_pade_dev'
+                project_id = "ocio_pade"
 
             if environment is None or environment == "":
                 environment = "dev"
         else:
             virtual_env = virtual_env.lower()
             project_id = virtual_env.rsplit('_', 1)[0]
             if environment is None or environment == "":
                 environment = virtual_env.rsplit('_', 1)[1]
 
+        print("virtual_env: " + virtual_env)
+
         project_id_root = project_id.split('_', 1)[0]
         project_id_individual = project_id.split('_', 1)[1]
 
-        print("virtual_env: " + virtual_env)
-
         if dbutils is None:
             running_local = True
             repository_path = str(path.parent.parent)
             yyyy_param = str(date.today().year)
             mm_param = f"{format(date.today().month,'02')}"
             dd_param = ""
         else:
@@ -90,15 +90,15 @@
             if mm_param is None:
                 mm_param = f"{format(date.today().month,'02')}"
 
             dd_param = dbutils.widgets.get("report_dd")
             if dd_param is None:
                 dd_param = f"{format(date.today().day,'02')}"
 
-        azure_client_secret_key = "PADE_" + virtual_env.upper() + "_AZURE_CLIENT_SECRET"
+        azure_client_secret_key = virtual_env.upper() + "_AZURE_CLIENT_SECRET"
         project_id_root = project_id.rsplit('_', 1)[0]
         project_id_individual = project_id.rsplit('_', 1)[1]
 
         dataset_name = 'all'
         cicd_action = 'pull_request'
 
         parameters = {
```

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_environment_service/repo_core.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/repo_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/data_ecosystem_services/tech_schema/manifest.py` & `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_schema/manifest.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/license.md` & `data_ecosystem_services-202303.0.28/license.md`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/pyproject.toml` & `data_ecosystem_services-202303.0.28/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 [project.urls]
 "Homepage" = "https://test.pypi.org/project/data-ecosystem-services"
 "Documentation" = "https://gift.readthedocs.io"
 "Repository" = "https://github.com/cdcent/data-ecosystem-services"
 
 [tool.poetry]
 name="data_ecosystem_services"
-version="202303.0.27"
+version="202303.0.28"
 description="Program Agnostic Data Ecosystem (PADE) - Python Services"
 authors=["John Bowyer <zfi4@cdc.gov>"]
 readme = "readme.md"
 license="Apache"
 homepage="https://test.pypi.org/project/data-ecosystem-services"
 repository="https://github.com/cdcent/data-ecosystem-services"
 classifiers=[
```

### Comparing `data_ecosystem_services-202303.0.27/readme.md` & `data_ecosystem_services-202303.0.28/readme.md`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.27/PKG-INFO` & `data_ecosystem_services-202303.0.28/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data-ecosystem-services
-Version: 202303.0.27
+Version: 202303.0.28
 Summary: Program Agnostic Data Ecosystem (PADE) - Python Services
 Home-page: https://test.pypi.org/project/data-ecosystem-services
 License: Apache
 Author: John Bowyer
 Author-email: zfi4@cdc.gov
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 4 - Beta
```

