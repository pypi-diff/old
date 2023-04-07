# Comparing `tmp/data_ecosystem_services-202303.0.28.tar.gz` & `tmp/data_ecosystem_services-202303.0.29.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_ecosystem_services-202303.0.28.tar", max compression
+gzip compressed data, was "data_ecosystem_services-202303.0.29.tar", max compression
```

## Comparing `data_ecosystem_services-202303.0.28.tar` & `data_ecosystem_services-202303.0.29.tar`

### file list

```diff
@@ -1,29 +1,29 @@
--rw-r--r--   0        0        0      857 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/__main__.py
--rw-r--r--   0        0        0      916 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/__init__.py
--rw-r--r--   0        0        0     4670 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/environment_logging.py
--rw-r--r--   0        0        0      958 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/__init__.py
--rw-r--r--   0        0        0     3431 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_alation.py
--rw-r--r--   0        0        0    14614 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_core.py
--rw-r--r--   0        0        0     1115 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/__init__.py
--rw-r--r--   0        0        0    41371 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/dataset_metadata.py
--rw-r--r--   0        0        0    32651 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/environment_metadata.py
--rw-r--r--   0        0        0    36036 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/job_metadata.py
--rw-r--r--   0        0        0     2261 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/logging_metadata.py
--rw-r--r--   0        0        0    22304 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/pipeline_metadata.py
--rw-r--r--   0        0        0     1472 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/__init__.py
--rw-r--r--   0        0        0    33731 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_convert.py
--rw-r--r--   0        0        0     8716 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_core.py
--rw-r--r--   0        0        0    24963 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_crud.py
--rw-r--r--   0        0        0     3777 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_extract.py
--rw-r--r--   0        0        0     1997 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_core.py
--rw-r--r--   0        0        0    26185 2023-04-07 02:25:43.522424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_file.py
--rw-r--r--   0        0        0     4589 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_spark.py
--rw-r--r--   0        0        0     4648 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/job_core.py
--rw-r--r--   0        0        0    17224 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/repo_core.py
--rw-r--r--   0        0        0    10094 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_schema/manifest.py
--rw-r--r--   0        0        0    11357 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/license.md
--rw-r--r--   0        0        0     3346 2023-04-07 02:29:33.133077 data_ecosystem_services-202303.0.28/pyproject.toml
--rw-r--r--   0        0        0    47124 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/readme.md
--rw-r--r--   0        0        0      118 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/setup.cfg
--rw-r--r--   0        0        0      127 2023-04-07 02:25:43.526424 data_ecosystem_services-202303.0.28/setup.py
--rw-r--r--   0        0        0    49936 1970-01-01 00:00:00.000000 data_ecosystem_services-202303.0.28/PKG-INFO
+-rw-r--r--   0        0        0      857 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/__main__.py
+-rw-r--r--   0        0        0      916 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/admin_service/__init__.py
+-rw-r--r--   0        0        0     4670 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/admin_service/environment_logging.py
+-rw-r--r--   0        0        0      958 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/security_service/__init__.py
+-rw-r--r--   0        0        0     3431 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/security_service/security_alation.py
+-rw-r--r--   0        0        0    14614 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/security_service/security_core.py
+-rw-r--r--   0        0        0     1115 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/__init__.py
+-rw-r--r--   0        0        0    41371 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/dataset_metadata.py
+-rw-r--r--   0        0        0    32651 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/environment_metadata.py
+-rw-r--r--   0        0        0    36036 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/job_metadata.py
+-rw-r--r--   0        0        0     2261 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/logging_metadata.py
+-rw-r--r--   0        0        0    22304 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/pipeline_metadata.py
+-rw-r--r--   0        0        0     1472 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/__init__.py
+-rw-r--r--   0        0        0    33731 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_convert.py
+-rw-r--r--   0        0        0     8716 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_core.py
+-rw-r--r--   0        0        0    24963 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_crud.py
+-rw-r--r--   0        0        0     3777 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_extract.py
+-rw-r--r--   0        0        0     1997 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/environment_core.py
+-rw-r--r--   0        0        0    26185 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/environment_file.py
+-rw-r--r--   0        0        0     4589 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/environment_spark.py
+-rw-r--r--   0        0        0     4648 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/job_core.py
+-rw-r--r--   0        0        0    17224 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/repo_core.py
+-rw-r--r--   0        0        0    10094 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_schema/manifest.py
+-rw-r--r--   0        0        0    11357 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/license.md
+-rw-r--r--   0        0        0     3346 2023-04-07 03:48:13.305947 data_ecosystem_services-202303.0.29/pyproject.toml
+-rw-r--r--   0        0        0    47124 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/readme.md
+-rw-r--r--   0        0        0      118 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/setup.cfg
+-rw-r--r--   0        0        0      127 2023-04-07 03:45:02.633220 data_ecosystem_services-202303.0.29/setup.py
+-rw-r--r--   0        0        0    49936 1970-01-01 00:00:00.000000 data_ecosystem_services-202303.0.29/PKG-INFO
```

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/__main__.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/__main__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/__init__.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/admin_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/admin_service/environment_logging.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/admin_service/environment_logging.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/__init__.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/security_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_alation.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/security_service/security_alation.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/security_service/security_core.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/security_service/security_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/__init__.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/dataset_metadata.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/dataset_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/environment_metadata.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/environment_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/job_metadata.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/job_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/logging_metadata.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/logging_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/self_service/pipeline_metadata.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/self_service/pipeline_metadata.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/__init__.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_convert.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_convert.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_core.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_crud.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_crud.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/dataset_extract.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/dataset_extract.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_core.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/environment_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_file.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/environment_file.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/environment_spark.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/environment_spark.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/job_core.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/job_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_environment_service/repo_core.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_environment_service/repo_core.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/data_ecosystem_services/tech_schema/manifest.py` & `data_ecosystem_services-202303.0.29/data_ecosystem_services/tech_schema/manifest.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/license.md` & `data_ecosystem_services-202303.0.29/license.md`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/pyproject.toml` & `data_ecosystem_services-202303.0.29/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 [project.urls]
 "Homepage" = "https://test.pypi.org/project/data-ecosystem-services"
 "Documentation" = "https://gift.readthedocs.io"
 "Repository" = "https://github.com/cdcent/data-ecosystem-services"
 
 [tool.poetry]
 name="data_ecosystem_services"
-version="202303.0.28"
+version="202303.0.29"
 description="Program Agnostic Data Ecosystem (PADE) - Python Services"
 authors=["John Bowyer <zfi4@cdc.gov>"]
 readme = "readme.md"
 license="Apache"
 homepage="https://test.pypi.org/project/data-ecosystem-services"
 repository="https://github.com/cdcent/data-ecosystem-services"
 classifiers=[
```

### Comparing `data_ecosystem_services-202303.0.28/readme.md` & `data_ecosystem_services-202303.0.29/readme.md`

 * *Files identical despite different names*

### Comparing `data_ecosystem_services-202303.0.28/PKG-INFO` & `data_ecosystem_services-202303.0.29/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data-ecosystem-services
-Version: 202303.0.28
+Version: 202303.0.29
 Summary: Program Agnostic Data Ecosystem (PADE) - Python Services
 Home-page: https://test.pypi.org/project/data-ecosystem-services
 License: Apache
 Author: John Bowyer
 Author-email: zfi4@cdc.gov
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 4 - Beta
```

