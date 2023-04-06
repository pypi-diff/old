# Comparing `tmp/exodusutils-0.3.7.tar.gz` & `tmp/exodusutils-0.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "exodusutils-0.3.7.tar", max compression
+gzip compressed data, was "exodusutils-0.3.9.tar", max compression
```

## Comparing `exodusutils-0.3.7.tar` & `exodusutils-0.3.9.tar`

### file list

```diff
@@ -1,41 +1,41 @@
--rw-r--r--   0        0        0    11343 2022-12-08 07:38:02.209065 exodusutils-0.3.7/LICENSE
--rw-r--r--   0        0        0     1500 2022-12-08 07:38:02.209065 exodusutils-0.3.7/README.md
--rw-r--r--   0        0        0     1495 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/__init__.py
--rw-r--r--   0        0        0     1199 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/app_utils.py
--rw-r--r--   0        0        0      139 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/configuration/__init__.py
--rw-r--r--   0        0        0     1529 2023-01-31 06:17:14.829593 exodusutils-0.3.7/exodusutils/configuration/configs/configs.py
--rw-r--r--   0        0        0     1392 2023-01-31 06:17:07.121592 exodusutils-0.3.7/exodusutils/configuration/configs/grpc.py
--rw-r--r--   0        0        0     2215 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/configuration/configs/minio.py
--rw-r--r--   0        0        0     5003 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/configuration/configs/mongodb.py
--rw-r--r--   0        0        0      224 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/configuration/configs/utils.py
--rw-r--r--   0        0        0     2491 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/configuration/mongo_instance.py
--rw-r--r--   0        0        0      220 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/constants.py
--rw-r--r--   0        0        0     3588 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/enums.py
--rw-r--r--   0        0        0      158 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/exceptions/__init__.py
--rw-r--r--   0        0        0     1024 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/exceptions/exceptions.py
--rw-r--r--   0        0        0      248 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/feature_engineering/__init__.py
--rw-r--r--   0        0        0     2613 2022-12-08 07:38:02.209065 exodusutils-0.3.7/exodusutils/feature_engineering/label_encoding.py
--rw-r--r--   0        0        0     1588 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/feature_engineering/one_hot_encoding.py
--rw-r--r--   0        0        0     1807 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/feature_engineering/time_component_encoding.py
--rw-r--r--   0        0        0     2846 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/frame_manipulation.py
--rw-r--r--   0        0        0     2154 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/frames.py
--rw-r--r--   0        0        0     8941 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/internal/__init__.py
--rw-r--r--   0        0        0     2431 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/internal/process_unit.py
--rw-r--r--   0        0        0       71 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/migration/__init__.py
--rw-r--r--   0        0        0     1353 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/migration/base_migration.py
--rw-r--r--   0        0        0     1652 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/migration/migration.py
--rw-r--r--   0        0        0      881 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/predict/__init__.py
--rw-r--r--   0        0        0      253 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/preprocessing/__init__.py
--rw-r--r--   0        0        0     2039 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/preprocessing/column_cardinality_limiter.py
--rw-r--r--   0        0        0     1521 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/preprocessing/constant_columns_remover.py
--rw-r--r--   0        0        0     3253 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/preprocessing/imputation.py
--rw-r--r--   0        0        0      374 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/schemas/__init__.py
--rw-r--r--   0        0        0      995 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/schemas/input_file.py
--rw-r--r--   0        0        0    10254 2023-01-31 06:11:19.332574 exodusutils-0.3.7/exodusutils/schemas/requests.py
--rw-r--r--   0        0        0     2533 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/schemas/responses.py
--rw-r--r--   0        0        0    10960 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/schemas/scores.py
--rw-r--r--   0        0        0     3729 2022-12-08 07:38:02.210065 exodusutils-0.3.7/exodusutils/schemas/simple_iid_request.py
--rw-r--r--   0        0        0     3378 2023-01-04 10:14:12.838979 exodusutils-0.3.7/exodusutils/schemas/uri.py
--rw-r--r--   0        0        0     3072 2023-01-31 06:27:07.150623 exodusutils-0.3.7/pyproject.toml
--rw-r--r--   0        0        0     2707 1970-01-01 00:00:00.000000 exodusutils-0.3.7/setup.py
--rw-r--r--   0        0        0     3089 1970-01-01 00:00:00.000000 exodusutils-0.3.7/PKG-INFO
+-rw-r--r--   0        0        0    11343 2022-12-08 07:38:02.209065 exodusutils-0.3.9/LICENSE
+-rw-r--r--   0        0        0     1500 2022-12-08 07:38:02.209065 exodusutils-0.3.9/README.md
+-rw-r--r--   0        0        0     1495 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/__init__.py
+-rw-r--r--   0        0        0     1199 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/app_utils.py
+-rw-r--r--   0        0        0      139 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/configuration/__init__.py
+-rw-r--r--   0        0        0     1597 2023-01-31 06:35:33.966650 exodusutils-0.3.9/exodusutils/configuration/configs/configs.py
+-rw-r--r--   0        0        0     1392 2023-01-31 06:17:07.121592 exodusutils-0.3.9/exodusutils/configuration/configs/grpc.py
+-rw-r--r--   0        0        0     2215 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/configuration/configs/minio.py
+-rw-r--r--   0        0        0     5003 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/configuration/configs/mongodb.py
+-rw-r--r--   0        0        0      224 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/configuration/configs/utils.py
+-rw-r--r--   0        0        0     2491 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/configuration/mongo_instance.py
+-rw-r--r--   0        0        0      220 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/constants.py
+-rw-r--r--   0        0        0     3588 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/enums.py
+-rw-r--r--   0        0        0      158 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/exceptions/__init__.py
+-rw-r--r--   0        0        0     1024 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/exceptions/exceptions.py
+-rw-r--r--   0        0        0      248 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/feature_engineering/__init__.py
+-rw-r--r--   0        0        0     2613 2022-12-08 07:38:02.209065 exodusutils-0.3.9/exodusutils/feature_engineering/label_encoding.py
+-rw-r--r--   0        0        0     1588 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/feature_engineering/one_hot_encoding.py
+-rw-r--r--   0        0        0     1807 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/feature_engineering/time_component_encoding.py
+-rw-r--r--   0        0        0     2846 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/frame_manipulation.py
+-rw-r--r--   0        0        0     2154 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/frames.py
+-rw-r--r--   0        0        0     8941 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/internal/__init__.py
+-rw-r--r--   0        0        0     2431 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/internal/process_unit.py
+-rw-r--r--   0        0        0       71 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/migration/__init__.py
+-rw-r--r--   0        0        0     1353 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/migration/base_migration.py
+-rw-r--r--   0        0        0     1652 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/migration/migration.py
+-rw-r--r--   0        0        0      881 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/predict/__init__.py
+-rw-r--r--   0        0        0      253 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/preprocessing/__init__.py
+-rw-r--r--   0        0        0     2039 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/preprocessing/column_cardinality_limiter.py
+-rw-r--r--   0        0        0     1521 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/preprocessing/constant_columns_remover.py
+-rw-r--r--   0        0        0     3253 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/preprocessing/imputation.py
+-rw-r--r--   0        0        0      374 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/schemas/__init__.py
+-rw-r--r--   0        0        0      995 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/schemas/input_file.py
+-rw-r--r--   0        0        0    10254 2023-01-31 06:11:19.332574 exodusutils-0.3.9/exodusutils/schemas/requests.py
+-rw-r--r--   0        0        0     2533 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/schemas/responses.py
+-rw-r--r--   0        0        0    10960 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/schemas/scores.py
+-rw-r--r--   0        0        0     3729 2022-12-08 07:38:02.210065 exodusutils-0.3.9/exodusutils/schemas/simple_iid_request.py
+-rw-r--r--   0        0        0     3378 2023-01-04 10:14:12.838979 exodusutils-0.3.9/exodusutils/schemas/uri.py
+-rw-r--r--   0        0        0     3072 2023-01-31 06:40:53.646666 exodusutils-0.3.9/pyproject.toml
+-rw-r--r--   0        0        0     2707 1970-01-01 00:00:00.000000 exodusutils-0.3.9/setup.py
+-rw-r--r--   0        0        0     3089 1970-01-01 00:00:00.000000 exodusutils-0.3.9/PKG-INFO
```

### Comparing `exodusutils-0.3.7/LICENSE` & `exodusutils-0.3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/README.md` & `exodusutils-0.3.9/README.md`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/__init__.py` & `exodusutils-0.3.9/exodusutils/__init__.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/app_utils.py` & `exodusutils-0.3.9/exodusutils/app_utils.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/configuration/configs/configs.py` & `exodusutils-0.3.9/exodusutils/configuration/configs/configs.py`

 * *Files 16% similar despite different names*

```diff
@@ -17,25 +17,26 @@
     grpc_configs: GPRCConfigs
     cores: int
 
     @classmethod
     def get(cls, name: str):
         mongodb_configs = MongoDBConfigs.get()
         minio_configs = MinioConfigs.get()
+        grpc_configs = GPRCConfigs.get()
         configs = get_configs()
         if configs is None:
             cores_key = f"EXODUS_{name.upper()}_CORES"
             cpus = os.cpu_count()
             default_values = {cores_key: 1 if cpus is None else cpus}
             cores = int(os.environ.get(cores_key, default_values[cores_key]))
         else:
             configs = configs["exodus"]
             cores = int(configs["cores"])
         return cls(
-            mongodb_configs=mongodb_configs, minio_configs=minio_configs, cores=cores
+            mongodb_configs=mongodb_configs, minio_configs=minio_configs, grpc_configs=grpc_configs, cores=cores
         )
 
     @property
     def mongo_instance(self) -> MongoInstance:
         return MongoInstance(self.mongodb_configs)
 
     @property
```

### Comparing `exodusutils-0.3.7/exodusutils/configuration/configs/grpc.py` & `exodusutils-0.3.9/exodusutils/configuration/configs/grpc.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/configuration/configs/minio.py` & `exodusutils-0.3.9/exodusutils/configuration/configs/minio.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/configuration/configs/mongodb.py` & `exodusutils-0.3.9/exodusutils/configuration/configs/mongodb.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/configuration/mongo_instance.py` & `exodusutils-0.3.9/exodusutils/configuration/mongo_instance.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/enums.py` & `exodusutils-0.3.9/exodusutils/enums.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/exceptions/exceptions.py` & `exodusutils-0.3.9/exodusutils/exceptions/exceptions.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/feature_engineering/label_encoding.py` & `exodusutils-0.3.9/exodusutils/feature_engineering/label_encoding.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/feature_engineering/one_hot_encoding.py` & `exodusutils-0.3.9/exodusutils/feature_engineering/one_hot_encoding.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/feature_engineering/time_component_encoding.py` & `exodusutils-0.3.9/exodusutils/feature_engineering/time_component_encoding.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/frame_manipulation.py` & `exodusutils-0.3.9/exodusutils/frame_manipulation.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/frames.py` & `exodusutils-0.3.9/exodusutils/frames.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/internal/__init__.py` & `exodusutils-0.3.9/exodusutils/internal/__init__.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/internal/process_unit.py` & `exodusutils-0.3.9/exodusutils/internal/process_unit.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/migration/base_migration.py` & `exodusutils-0.3.9/exodusutils/migration/base_migration.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/migration/migration.py` & `exodusutils-0.3.9/exodusutils/migration/migration.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/predict/__init__.py` & `exodusutils-0.3.9/exodusutils/predict/__init__.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/preprocessing/column_cardinality_limiter.py` & `exodusutils-0.3.9/exodusutils/preprocessing/column_cardinality_limiter.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/preprocessing/constant_columns_remover.py` & `exodusutils-0.3.9/exodusutils/preprocessing/constant_columns_remover.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/preprocessing/imputation.py` & `exodusutils-0.3.9/exodusutils/preprocessing/imputation.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/schemas/input_file.py` & `exodusutils-0.3.9/exodusutils/schemas/input_file.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/schemas/requests.py` & `exodusutils-0.3.9/exodusutils/schemas/requests.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/schemas/responses.py` & `exodusutils-0.3.9/exodusutils/schemas/responses.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/schemas/scores.py` & `exodusutils-0.3.9/exodusutils/schemas/scores.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/schemas/simple_iid_request.py` & `exodusutils-0.3.9/exodusutils/schemas/simple_iid_request.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/exodusutils/schemas/uri.py` & `exodusutils-0.3.9/exodusutils/schemas/uri.py`

 * *Files identical despite different names*

### Comparing `exodusutils-0.3.7/pyproject.toml` & `exodusutils-0.3.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "exodusutils"
-version = "0.3.7"
+version = "0.3.9"
 license = "Apache-2.0"
 readme = "README.md"
 description = "Utility functions and helper classes for Exodus project"
 authors = ["Tsung-Ju Lii <andylii@mobagel.com>"]
 classifiers = [
   "Development Status :: 1 - Planning",
   "Intended Audience :: Developers",
```

### Comparing `exodusutils-0.3.7/setup.py` & `exodusutils-0.3.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,15 @@
  'pymongo[encryption]>=4.0.1,<5.0.0',
  'python-Levenshtein>=0.12.2,<0.13.0',
  'requests>=2.28.1,<3.0.0',
  'scikit-learn>=0.23.1']
 
 setup_kwargs = {
     'name': 'exodusutils',
-    'version': '0.3.7',
+    'version': '0.3.9',
     'description': 'Utility functions and helper classes for Exodus project',
     'long_description': "# Exodus common utilities\n\nThis is the library defining the schemas for exodus utilities.\n\n## Structure\n\n### `exodusutils`\n\nContains helpful utility functions.\n\n### `schemas`\n\nIn the `schemas` folder you can find the following:\n- Schema definitions for the model algorithm's incoming requests\n- Schema definitions for the model algorithm's responses\n- Definitions for `RegressionScores` and `ClassificationScores`\n- Definitions for types such as `Attribute` and `Column`\n\n### `predict`\n\nThe `predict` folder contains helper functions for prediction.\n\n### `enums.py`\n\nContains enums used by Exodus. Current contains the following:\n- `TimeUnit`, with helper methods to convert timestamps to different formats\n- `DataType`, with helper methods to convert from `Pandas` types\n\n### `feature_engineering.py`\n\nContains commonly used feature engineering methods. Currently includes:\n- One-hot encoding\n- Label encoding\n- Time component encoding\nIt is recommended to use at least 1 method in this file during training.\n\n### `frame_manipulation.py`\n\nContains multiple frame manipulation methods. Used during prediction, should pick the method that corresponds to the one used during training.\n\n### `frames.py`\n\nContains definitions and helper functions for the following classes:\n- `SplitFrames`: A 3-tuple with a training dataframe, a testing dataframe, and a validation dataframe.\n- `CVFrames`: A list of `SplitFrames`. Should not be instantiated manually, user should use `CVFrames.iid` helper classmethod.\n",
     'author': 'Tsung-Ju Lii',
     'author_email': 'andylii@mobagel.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `exodusutils-0.3.7/PKG-INFO` & `exodusutils-0.3.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: exodusutils
-Version: 0.3.7
+Version: 0.3.9
 Summary: Utility functions and helper classes for Exodus project
 License: Apache-2.0
 Author: Tsung-Ju Lii
 Author-email: andylii@mobagel.com
 Requires-Python: >=3.8.0,<4.0.0
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
```

