# Comparing `tmp/abacusai-0.9.1.tar.gz` & `tmp/abacusai-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/abacusai-0.9.1.tar", last modified: Tue Jul 14 14:14:23 2020, max compression
+gzip compressed data, was "dist/abacusai-0.9.2.tar", last modified: Tue Jul 21 23:11:47 2020, max compression
```

## Comparing `abacusai-0.9.1.tar` & `abacusai-0.9.2.tar`

### file list

```diff
@@ -1,37 +1,38 @@
-drwxr-xr-x   0 austin     (501) staff       (20)        0 2020-07-14 14:14:23.000000 abacusai-0.9.1/
--rw-r--r--   0 austin     (501) staff       (20)      650 2020-07-14 14:14:23.000000 abacusai-0.9.1/PKG-INFO
--rw-r--r--   0 austin     (501) staff       (20)        0 2020-02-10 23:45:50.000000 abacusai-0.9.1/README.md
-drwxr-xr-x   0 austin     (501) staff       (20)        0 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai/
--rw-r--r--   0 austin     (501) staff       (20)      805 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/api_key.py
--rw-r--r--   0 austin     (501) staff       (20)     1931 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/batch_prediction.py
--rw-r--r--   0 austin     (501) staff       (20)      803 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/bucket_verification.py
--rw-r--r--   0 austin     (501) staff       (20)      762 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/bucket_verification_instructions.py
--rw-r--r--   0 austin     (501) staff       (20)      617 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/bucket_verification_result.py
--rw-r--r--   0 austin     (501) staff       (20)    29286 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/client.py
--rw-r--r--   0 austin     (501) staff       (20)     2629 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/dataset.py
--rw-r--r--   0 austin     (501) staff       (20)     2193 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/dataset_upload.py
--rw-r--r--   0 austin     (501) staff       (20)     1021 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/dataset_version.py
--rw-r--r--   0 austin     (501) staff       (20)     2596 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/deployment.py
--rw-r--r--   0 austin     (501) staff       (20)      619 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/deployment_auth_token.py
--rw-r--r--   0 austin     (501) staff       (20)     2629 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/model.py
--rw-r--r--   0 austin     (501) staff       (20)      831 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/model_metrics.py
--rw-r--r--   0 austin     (501) staff       (20)     1037 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/model_version.py
--rw-r--r--   0 austin     (501) staff       (20)     2897 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/project.py
--rw-r--r--   0 austin     (501) staff       (20)      847 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/project_dataset.py
--rw-r--r--   0 austin     (501) staff       (20)      701 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/project_validation.py
--rw-r--r--   0 austin     (501) staff       (20)     2246 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/refresh_pipeline_run.py
--rw-r--r--   0 austin     (501) staff       (20)     1437 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/refresh_policy.py
--rw-r--r--   0 austin     (501) staff       (20)      698 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/schema.py
--rw-r--r--   0 austin     (501) staff       (20)      610 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/streaming_auth_token.py
--rw-r--r--   0 austin     (501) staff       (20)     1214 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/training_config_options.py
--rw-r--r--   0 austin     (501) staff       (20)      702 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/use_case.py
--rw-r--r--   0 austin     (501) staff       (20)      994 2020-07-14 14:14:22.000000 abacusai-0.9.1/abacusai/use_case_requirements.py
-drwxr-xr-x   0 austin     (501) staff       (20)        0 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai.egg-info/
--rw-r--r--   0 austin     (501) staff       (20)      650 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai.egg-info/PKG-INFO
--rw-r--r--   0 austin     (501) staff       (20)      882 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai.egg-info/SOURCES.txt
--rw-r--r--   0 austin     (501) staff       (20)        1 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai.egg-info/dependency_links.txt
--rw-r--r--   0 austin     (501) staff       (20)       19 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai.egg-info/requires.txt
--rw-r--r--   0 austin     (501) staff       (20)        9 2020-07-14 14:14:23.000000 abacusai-0.9.1/abacusai.egg-info/top_level.txt
--rw-r--r--   0 austin     (501) staff       (20)        1 2020-07-14 14:12:22.000000 abacusai-0.9.1/abacusai.egg-info/zip-safe
--rw-r--r--   0 austin     (501) staff       (20)       87 2020-07-14 14:14:23.000000 abacusai-0.9.1/setup.cfg
--rw-r--r--   0 austin     (501) staff       (20)      810 2020-07-14 14:14:22.000000 abacusai-0.9.1/setup.py
+drwxr-xr-x   0 austin     (501) staff       (20)        0 2020-07-21 23:11:47.000000 abacusai-0.9.2/
+-rw-r--r--   0 austin     (501) staff       (20)      650 2020-07-21 23:11:47.000000 abacusai-0.9.2/PKG-INFO
+-rw-r--r--   0 austin     (501) staff       (20)        0 2020-02-10 23:45:50.000000 abacusai-0.9.2/README.md
+drwxr-xr-x   0 austin     (501) staff       (20)        0 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/
+-rw-r--r--   0 austin     (501) staff       (20)      805 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/api_key.py
+-rw-r--r--   0 austin     (501) staff       (20)     1931 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/batch_prediction.py
+-rw-r--r--   0 austin     (501) staff       (20)      803 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/bucket_verification.py
+-rw-r--r--   0 austin     (501) staff       (20)      762 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/bucket_verification_instructions.py
+-rw-r--r--   0 austin     (501) staff       (20)      617 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/bucket_verification_result.py
+-rw-r--r--   0 austin     (501) staff       (20)    29589 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/client.py
+-rw-r--r--   0 austin     (501) staff       (20)     2797 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/dataset.py
+-rw-r--r--   0 austin     (501) staff       (20)     2193 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/dataset_upload.py
+-rw-r--r--   0 austin     (501) staff       (20)     1021 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/dataset_version.py
+-rw-r--r--   0 austin     (501) staff       (20)     3088 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/deployment.py
+-rw-r--r--   0 austin     (501) staff       (20)      619 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/deployment_auth_token.py
+-rw-r--r--   0 austin     (501) staff       (20)      852 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/external_connection.py
+-rw-r--r--   0 austin     (501) staff       (20)     2797 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/model.py
+-rw-r--r--   0 austin     (501) staff       (20)      831 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/model_metrics.py
+-rw-r--r--   0 austin     (501) staff       (20)     1037 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/model_version.py
+-rw-r--r--   0 austin     (501) staff       (20)     2938 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/project.py
+-rw-r--r--   0 austin     (501) staff       (20)      847 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/project_dataset.py
+-rw-r--r--   0 austin     (501) staff       (20)      701 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/project_validation.py
+-rw-r--r--   0 austin     (501) staff       (20)     2246 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/refresh_pipeline_run.py
+-rw-r--r--   0 austin     (501) staff       (20)     1556 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/refresh_policy.py
+-rw-r--r--   0 austin     (501) staff       (20)      698 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/schema.py
+-rw-r--r--   0 austin     (501) staff       (20)      610 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/streaming_auth_token.py
+-rw-r--r--   0 austin     (501) staff       (20)     1214 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/training_config_options.py
+-rw-r--r--   0 austin     (501) staff       (20)      702 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/use_case.py
+-rw-r--r--   0 austin     (501) staff       (20)      994 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai/use_case_requirements.py
+drwxr-xr-x   0 austin     (501) staff       (20)        0 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai.egg-info/
+-rw-r--r--   0 austin     (501) staff       (20)      650 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai.egg-info/PKG-INFO
+-rw-r--r--   0 austin     (501) staff       (20)      914 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai.egg-info/SOURCES.txt
+-rw-r--r--   0 austin     (501) staff       (20)        1 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai.egg-info/dependency_links.txt
+-rw-r--r--   0 austin     (501) staff       (20)       19 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai.egg-info/requires.txt
+-rw-r--r--   0 austin     (501) staff       (20)        9 2020-07-21 23:11:47.000000 abacusai-0.9.2/abacusai.egg-info/top_level.txt
+-rw-r--r--   0 austin     (501) staff       (20)        1 2020-07-14 14:12:22.000000 abacusai-0.9.2/abacusai.egg-info/zip-safe
+-rw-r--r--   0 austin     (501) staff       (20)       87 2020-07-21 23:11:47.000000 abacusai-0.9.2/setup.cfg
+-rw-r--r--   0 austin     (501) staff       (20)      810 2020-07-21 23:11:47.000000 abacusai-0.9.2/setup.py
```

### Comparing `abacusai-0.9.1/PKG-INFO` & `abacusai-0.9.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: abacusai
-Version: 0.9.1
+Version: 0.9.2
 Summary: Abacus.AI Python Client Library
 Home-page: https://abacus.ai
 Author: Abacus.AI
 Author-email: dev@abacus.ai
 License: MIT
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `abacusai-0.9.1/abacusai/api_key.py` & `abacusai-0.9.2/abacusai/api_key.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/batch_prediction.py` & `abacusai-0.9.2/abacusai/batch_prediction.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/bucket_verification.py` & `abacusai-0.9.2/abacusai/bucket_verification.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/bucket_verification_instructions.py` & `abacusai-0.9.2/abacusai/bucket_verification_instructions.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/bucket_verification_result.py` & `abacusai-0.9.2/abacusai/bucket_verification_result.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/client.py` & `abacusai-0.9.2/abacusai/client.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,14 +13,15 @@
 from .bucket_verification_result import BucketVerificationResult
 from .schema import Schema
 from .dataset import Dataset
 from .dataset_upload import DatasetUpload
 from .dataset_version import DatasetVersion
 from .deployment import Deployment
 from .deployment_auth_token import DeploymentAuthToken
+from .external_connection import ExternalConnection
 from .model import Model
 from .model_metrics import ModelMetrics
 from .model_version import ModelVersion
 from .project import Project
 from .project_dataset import ProjectDataset
 from .project_validation import ProjectValidation
 from .refresh_pipeline_run import RefreshPipelineRun
@@ -38,15 +39,15 @@
         self.exception = exception or 'ApiException'
 
     def __str__(self):
         return f'{self.exception}({self.http_status}): {self.message}'
 
 
 class ApiClient():
-    client_version = '0.9.1'
+    client_version = '0.9.2'
 
     def __init__(self, api_key=None, server='https://abacus.ai'):
         self.api_key = api_key
         self.server = server
         # Connection and version check
         try:
             documentation = self._call_api('documentation', 'GET')
@@ -176,17 +177,17 @@
         '''Removes a columnMapping from a column in the dataset.    '''
         return self._call_api('removeColumnMapping', 'DELETE', query_params={'projectId': project_id, 'datasetId': dataset_id, 'column': column}, parse_type=Schema)
 
     def delete_project(self, project_id: str):
         '''Deletes a specified project from your organization.    '''
         return self._call_api('deleteProject', 'DELETE', query_params={'projectId': project_id})
 
-    def create_dataset(self, name: str, location: str, file_format: str = None, project_id: str = None, dataset_type: str = None):
+    def create_dataset(self, name: str, location: str, file_format: str = None, project_id: str = None, dataset_type: str = None, refresh_schedule: str = None):
         '''Creates a Dataset from a file located in cloud storage such as Amazon AWS S3 using the specified dataset name and dataset location.    '''
-        return self._call_api('createDataset', 'POST', body={'name': name, 'location': location, 'fileFormat': file_format, 'projectId': project_id, 'datasetType': dataset_type}, parse_type=Dataset)
+        return self._call_api('createDataset', 'POST', body={'name': name, 'location': location, 'fileFormat': file_format, 'projectId': project_id, 'datasetType': dataset_type, 'refreshSchedule': refresh_schedule}, parse_type=Dataset)
 
     def create_dataset_version(self, dataset_id: str, location: str = None, file_format: str = None):
         '''Creates a new version of the specified Dataset    '''
         return self._call_api('createDatasetVersion', 'POST', body={'datasetId': dataset_id, 'location': location, 'fileFormat': file_format}, parse_type=DatasetVersion)
 
     def create_dataset_from_local_file(self, name: str, file_format: str = None, project_id: str = None, dataset_type: str = None):
         '''Creates a dataset from local file    '''
@@ -276,17 +277,17 @@
         '''Deletes the specified dataset from the organization.    '''
         return self._call_api('deleteDataset', 'DELETE', query_params={'datasetId': dataset_id})
 
     def get_training_config_options(self, project_id: str):
         '''Retrieves the full description of the model training configuration options available for the specified project.    '''
         return self._call_api('getTrainingConfigOptions', 'GET', query_params={'projectId': project_id}, parse_type=TrainingConfigOptions)
 
-    def train_model(self, project_id: str, name: None = None, training_config: dict = {}):
+    def train_model(self, project_id: str, name: None = None, training_config: dict = {}, refresh_schedule: str = None):
         '''Trains a model for the specified project.    '''
-        return self._call_api('trainModel', 'POST', body={'projectId': project_id, 'name': name, 'trainingConfig': training_config}, parse_type=Model)
+        return self._call_api('trainModel', 'POST', body={'projectId': project_id, 'name': name, 'trainingConfig': training_config, 'refreshSchedule': refresh_schedule}, parse_type=Model)
 
     def list_models(self, project_id: str):
         '''Retrieves the list of models in the specified project.    '''
         return self._call_api('listModels', 'GET', query_params={'projectId': project_id}, parse_type=Model)
 
     def describe_model(self, model_id: str):
         '''Retrieves a full description of the specified model.    '''
@@ -380,33 +381,33 @@
         '''Returns a list of anomalies    '''
         return self._call_api('isAnomaly', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data})
 
     def get_forecast(self, deployment_token: str, deployment_id: str, query_data: dict, future_data: dict = None, num_predictions: int = None, prediction_start: str = None):
         '''Returns a list of forecasts for a given entity under the specified project deployment. Note that the inputs to the deployed model will be the column names (e.g., Holiday_YN) mapped to the column mappings in our system (e.g., FUTURE).    '''
         return self._call_api('getForecast', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data, 'futureData': future_data, 'numPredictions': num_predictions, 'predictionStart': prediction_start})
 
-    def get_recommendations(self, deployment_token: str, deployment_id: str, query_data: dict, num_items: int = 50, page: int = 1, include_filters: list = [], exclude_filters: list = []):
+    def get_recommendations(self, deployment_token: str, deployment_id: str, query_data: dict, num_items: int = 50, page: int = 1, include_filters: list = [], exclude_filters: list = [], score_field: str = ''):
         '''Returns a list of predictions for a given entity under the specified project deployment. Note that the inputs to the deployed model will be the column names (e.g., Timestamp) mapped to the column mappings in our system (e.g., TIMESTAMP).    '''
-        return self._call_api('getRecommendations', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data, 'numItems': num_items, 'page': page, 'includeFilters': include_filters, 'excludeFilters': exclude_filters})
+        return self._call_api('getRecommendations', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data, 'numItems': num_items, 'page': page, 'includeFilters': include_filters, 'excludeFilters': exclude_filters, 'scoreField': score_field})
 
     def get_personalized_ranking(self, deployment_token: str, deployment_id: str, query_data: dict):
         '''Returns a list of predictions for the specified personalized re-ranking project deployment.    '''
         return self._call_api('getPersonalizedRanking', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data})
 
     def get_ranked_items(self, deployment_token: str, deployment_id: str, query_data: dict):
         '''Returns a list of predictions for a given entity under the specified project deployment. Note that the inputs to the deployed model will be the column names (e.g., Item_ID) mapped to the column mappings in our system (e.g., ITEM_ID).    '''
         return self._call_api('getRankedItems', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data})
 
     def get_related_items(self, deployment_token: str, deployment_id: str, query_data: dict, num_items: int = 50, page: int = 1, include_filters: list = [], exclude_filters: list = []):
         '''Returns a list of predictions for a given entity under the specified project deployment. Note that the inputs to the deployed model will be the column names (e.g., Action_Type) mapped to the column mappings in our system (e.g., ACTION_TYPE).    '''
         return self._call_api('getRelatedItems', 'POST', body={'deploymentToken': deployment_token, 'deploymentId': deployment_id, 'queryData': query_data, 'numItems': num_items, 'page': page, 'includeFilters': include_filters, 'excludeFilters': exclude_filters})
 
-    def batch_predict(self, deployment_id: str, input_location: str = None, output_location: str = None, name: str = None):
+    def batch_predict(self, deployment_id: str, input_location: str = None, output_location: str = None, name: str = None, refresh_schedule: str = None):
         '''Starts a batch prediction task with the specified deployment ID, input location, output location and batch prediction job name.    '''
-        return self._call_api('batchPredict', 'POST', body={'deploymentId': deployment_id, 'inputLocation': input_location, 'outputLocation': output_location, 'name': name}, parse_type=BatchPrediction)
+        return self._call_api('batchPredict', 'POST', body={'deploymentId': deployment_id, 'inputLocation': input_location, 'outputLocation': output_location, 'name': name, 'refreshSchedule': refresh_schedule}, parse_type=BatchPrediction)
 
     def list_batch_predictions(self, deployment_id: str):
         '''Retrieves a list for the batch prediction jobs for the specified deployment    '''
         return self._call_api('listBatchPredictions', 'GET', query_params={'deploymentId': deployment_id}, parse_type=BatchPrediction)
 
     def describe_batch_prediction(self, batch_prediction_id: str):
         '''Retrieves the status of the specified batch prediction job.    '''
```

### Comparing `abacusai-0.9.1/abacusai/dataset.py` & `abacusai-0.9.2/abacusai/dataset.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,33 +2,34 @@
 
 
 class Dataset():
     '''
 
     '''
 
-    def __init__(self, client, datasetId=None, name=None, sourceType=None, dataSource=None, createdAt=None, latestDatasetVersion={}):
+    def __init__(self, client, datasetId=None, name=None, sourceType=None, dataSource=None, createdAt=None, refreshSchedules=None, latestDatasetVersion={}):
         self.client = client
         self.id = datasetId
         self.dataset_id = datasetId
         self.name = name
         self.source_type = sourceType
         self.data_source = dataSource
         self.created_at = createdAt
+        self.refresh_schedules = refreshSchedules
         self.latest_dataset_version = client._build_class(
             DatasetVersion, latestDatasetVersion)
 
     def __repr__(self):
-        return f"Dataset(dataset_id={repr(self.dataset_id)}, name={repr(self.name)}, source_type={repr(self.source_type)}, data_source={repr(self.data_source)}, created_at={repr(self.created_at)}, latest_dataset_version={repr(self.latest_dataset_version)})"
+        return f"Dataset(dataset_id={repr(self.dataset_id)}, name={repr(self.name)}, source_type={repr(self.source_type)}, data_source={repr(self.data_source)}, created_at={repr(self.created_at)}, refresh_schedules={repr(self.refresh_schedules)}, latest_dataset_version={repr(self.latest_dataset_version)})"
 
     def __eq__(self, other):
         return self.__class__ == other.__class__ and self.id == other.id
 
     def to_dict(self):
-        return {'dataset_id': self.dataset_id, 'name': self.name, 'source_type': self.source_type, 'data_source': self.data_source, 'created_at': self.created_at, 'latest_dataset_version': self.latest_dataset_version.to_dict() if self.latest_dataset_version else None}
+        return {'dataset_id': self.dataset_id, 'name': self.name, 'source_type': self.source_type, 'data_source': self.data_source, 'created_at': self.created_at, 'refresh_schedules': self.refresh_schedules, 'latest_dataset_version': self.latest_dataset_version.to_dict() if self.latest_dataset_version else None}
 
     def create_version(self, location=None, file_format=None):
         return self.client.create_dataset_version(self.dataset_id, location, file_format)
 
     def create_version_from_local_file(self, file_format=None):
         return self.client.create_dataset_version_from_local_file(self.dataset_id, file_format)
```

### Comparing `abacusai-0.9.1/abacusai/dataset_upload.py` & `abacusai-0.9.2/abacusai/dataset_upload.py`

 * *Ordering differences only*

 * *Files 4% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-import io
 from multiprocessing import Pool
+import io
 
 
 class DatasetUpload():
     '''
 
     '''
```

### Comparing `abacusai-0.9.1/abacusai/dataset_version.py` & `abacusai-0.9.2/abacusai/dataset_version.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/deployment.py` & `abacusai-0.9.2/abacusai/deployment.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,36 +1,38 @@
 
 
 class Deployment():
     '''
 
     '''
 
-    def __init__(self, client, deploymentId=None, name=None, status=None, description=None, deploymentConfig=None, deployedAt=None, createdAt=None, projectId=None, modelId=None, modelVersion=None):
+    def __init__(self, client, deploymentId=None, name=None, status=None, description=None, deploymentConfig=None, deployedAt=None, createdAt=None, projectId=None, modelId=None, modelVersion=None, refreshSchedules=None, batchPredictionRefreshSchedules=None):
         self.client = client
         self.id = deploymentId
         self.deployment_id = deploymentId
         self.name = name
         self.status = status
         self.description = description
         self.deployment_config = deploymentConfig
         self.deployed_at = deployedAt
         self.created_at = createdAt
         self.project_id = projectId
         self.model_id = modelId
         self.model_version = modelVersion
+        self.refresh_schedules = refreshSchedules
+        self.batch_prediction_refresh_schedules = batchPredictionRefreshSchedules
 
     def __repr__(self):
-        return f"Deployment(deployment_id={repr(self.deployment_id)}, name={repr(self.name)}, status={repr(self.status)}, description={repr(self.description)}, deployment_config={repr(self.deployment_config)}, deployed_at={repr(self.deployed_at)}, created_at={repr(self.created_at)}, project_id={repr(self.project_id)}, model_id={repr(self.model_id)}, model_version={repr(self.model_version)})"
+        return f"Deployment(deployment_id={repr(self.deployment_id)}, name={repr(self.name)}, status={repr(self.status)}, description={repr(self.description)}, deployment_config={repr(self.deployment_config)}, deployed_at={repr(self.deployed_at)}, created_at={repr(self.created_at)}, project_id={repr(self.project_id)}, model_id={repr(self.model_id)}, model_version={repr(self.model_version)}, refresh_schedules={repr(self.refresh_schedules)}, batch_prediction_refresh_schedules={repr(self.batch_prediction_refresh_schedules)})"
 
     def __eq__(self, other):
         return self.__class__ == other.__class__ and self.id == other.id
 
     def to_dict(self):
-        return {'deployment_id': self.deployment_id, 'name': self.name, 'status': self.status, 'description': self.description, 'deployment_config': self.deployment_config, 'deployed_at': self.deployed_at, 'created_at': self.created_at, 'project_id': self.project_id, 'model_id': self.model_id, 'model_version': self.model_version}
+        return {'deployment_id': self.deployment_id, 'name': self.name, 'status': self.status, 'description': self.description, 'deployment_config': self.deployment_config, 'deployed_at': self.deployed_at, 'created_at': self.created_at, 'project_id': self.project_id, 'model_id': self.model_id, 'model_version': self.model_version, 'refresh_schedules': self.refresh_schedules, 'batch_prediction_refresh_schedules': self.batch_prediction_refresh_schedules}
 
     def refresh(self):
         self = self.describe()
         return self
 
     def describe(self):
         return self.client.describe_deployment(self.deployment_id)
@@ -43,16 +45,16 @@
 
     def stop(self):
         return self.client.stop_deployment(self.deployment_id)
 
     def delete(self):
         return self.client.delete_deployment(self.deployment_id)
 
-    def batch_predict(self, input_location=None, output_location=None, name=None):
-        return self.client.batch_predict(self.deployment_id, input_location, output_location, name)
+    def batch_predict(self, input_location=None, output_location=None, name=None, refresh_schedule=None):
+        return self.client.batch_predict(self.deployment_id, input_location, output_location, name, refresh_schedule)
 
     def list_batch_predictions(self):
         return self.client.list_batch_predictions(self.deployment_id)
 
     def wait_for_deployment(self, timeout=480):
         return self.client._poll(self, {'PENDING', 'DEPLOYING'}, timeout=timeout)
```

### Comparing `abacusai-0.9.1/abacusai/deployment_auth_token.py` & `abacusai-0.9.2/abacusai/deployment_auth_token.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/model.py` & `abacusai-0.9.2/abacusai/model.py`

 * *Files 4% similar despite different names*

```diff
@@ -2,35 +2,36 @@
 
 
 class Model():
     '''
 
     '''
 
-    def __init__(self, client, name=None, modelId=None, modelConfig=None, createdAt=None, projectId=None, shared=None, sharedAt=None, latestModelVersion={}):
+    def __init__(self, client, name=None, modelId=None, modelConfig=None, createdAt=None, projectId=None, shared=None, sharedAt=None, refreshSchedules=None, latestModelVersion={}):
         self.client = client
         self.id = modelId
         self.name = name
         self.model_id = modelId
         self.model_config = modelConfig
         self.created_at = createdAt
         self.project_id = projectId
         self.shared = shared
         self.shared_at = sharedAt
+        self.refresh_schedules = refreshSchedules
         self.latest_model_version = client._build_class(
             ModelVersion, latestModelVersion)
 
     def __repr__(self):
-        return f"Model(name={repr(self.name)}, model_id={repr(self.model_id)}, model_config={repr(self.model_config)}, created_at={repr(self.created_at)}, project_id={repr(self.project_id)}, shared={repr(self.shared)}, shared_at={repr(self.shared_at)}, latest_model_version={repr(self.latest_model_version)})"
+        return f"Model(name={repr(self.name)}, model_id={repr(self.model_id)}, model_config={repr(self.model_config)}, created_at={repr(self.created_at)}, project_id={repr(self.project_id)}, shared={repr(self.shared)}, shared_at={repr(self.shared_at)}, refresh_schedules={repr(self.refresh_schedules)}, latest_model_version={repr(self.latest_model_version)})"
 
     def __eq__(self, other):
         return self.__class__ == other.__class__ and self.id == other.id
 
     def to_dict(self):
-        return {'name': self.name, 'model_id': self.model_id, 'model_config': self.model_config, 'created_at': self.created_at, 'project_id': self.project_id, 'shared': self.shared, 'shared_at': self.shared_at, 'latest_model_version': self.latest_model_version.to_dict() if self.latest_model_version else None}
+        return {'name': self.name, 'model_id': self.model_id, 'model_config': self.model_config, 'created_at': self.created_at, 'project_id': self.project_id, 'shared': self.shared, 'shared_at': self.shared_at, 'refresh_schedules': self.refresh_schedules, 'latest_model_version': self.latest_model_version.to_dict() if self.latest_model_version else None}
 
     def refresh(self):
         self = self.describe()
         return self
 
     def describe(self):
         return self.client.describe_model(self.model_id)
```

### Comparing `abacusai-0.9.1/abacusai/model_metrics.py` & `abacusai-0.9.2/abacusai/model_metrics.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/model_version.py` & `abacusai-0.9.2/abacusai/model_version.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/project.py` & `abacusai-0.9.2/abacusai/project.py`

 * *Files 4% similar despite different names*

```diff
@@ -55,16 +55,16 @@
 
     def create_streaming_dataset(self):
         return self.client.create_streaming_dataset(self.project_id)
 
     def get_training_config_options(self):
         return self.client.get_training_config_options(self.project_id)
 
-    def train_model(self, name=None, training_config={}):
-        return self.client.train_model(self.project_id, name, training_config)
+    def train_model(self, name=None, training_config={}, refresh_schedule=None):
+        return self.client.train_model(self.project_id, name, training_config, refresh_schedule)
 
     def list_models(self):
         return self.client.list_models(self.project_id)
 
     def create_deployment_token(self):
         return self.client.create_deployment_token(self.project_id)
```

### Comparing `abacusai-0.9.1/abacusai/project_dataset.py` & `abacusai-0.9.2/abacusai/project_dataset.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/project_validation.py` & `abacusai-0.9.2/abacusai/project_validation.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/refresh_pipeline_run.py` & `abacusai-0.9.2/abacusai/refresh_pipeline_run.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/refresh_policy.py` & `abacusai-0.9.2/abacusai/refresh_policy.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,28 +1,29 @@
 
 
 class RefreshPolicy():
     '''
 
     '''
 
-    def __init__(self, client, refreshPolicyId=None, name=None, cron=None, nextRunTime=None, createdAt=None, refreshType=None, datasetIds=None, modelIds=None, deploymentIds=None):
+    def __init__(self, client, refreshPolicyId=None, name=None, cron=None, nextRunTime=None, createdAt=None, refreshType=None, projectId=None, datasetIds=None, modelIds=None, deploymentIds=None):
         self.client = client
         self.id = refreshPolicyId
         self.refresh_policy_id = refreshPolicyId
         self.name = name
         self.cron = cron
         self.next_run_time = nextRunTime
         self.created_at = createdAt
         self.refresh_type = refreshType
+        self.project_id = projectId
         self.dataset_ids = datasetIds
         self.model_ids = modelIds
         self.deployment_ids = deploymentIds
 
     def __repr__(self):
-        return f"RefreshPolicy(refresh_policy_id={repr(self.refresh_policy_id)}, name={repr(self.name)}, cron={repr(self.cron)}, next_run_time={repr(self.next_run_time)}, created_at={repr(self.created_at)}, refresh_type={repr(self.refresh_type)}, dataset_ids={repr(self.dataset_ids)}, model_ids={repr(self.model_ids)}, deployment_ids={repr(self.deployment_ids)})"
+        return f"RefreshPolicy(refresh_policy_id={repr(self.refresh_policy_id)}, name={repr(self.name)}, cron={repr(self.cron)}, next_run_time={repr(self.next_run_time)}, created_at={repr(self.created_at)}, refresh_type={repr(self.refresh_type)}, project_id={repr(self.project_id)}, dataset_ids={repr(self.dataset_ids)}, model_ids={repr(self.model_ids)}, deployment_ids={repr(self.deployment_ids)})"
 
     def __eq__(self, other):
         return self.__class__ == other.__class__ and self.id == other.id
 
     def to_dict(self):
-        return {'refresh_policy_id': self.refresh_policy_id, 'name': self.name, 'cron': self.cron, 'next_run_time': self.next_run_time, 'created_at': self.created_at, 'refresh_type': self.refresh_type, 'dataset_ids': self.dataset_ids, 'model_ids': self.model_ids, 'deployment_ids': self.deployment_ids}
+        return {'refresh_policy_id': self.refresh_policy_id, 'name': self.name, 'cron': self.cron, 'next_run_time': self.next_run_time, 'created_at': self.created_at, 'refresh_type': self.refresh_type, 'project_id': self.project_id, 'dataset_ids': self.dataset_ids, 'model_ids': self.model_ids, 'deployment_ids': self.deployment_ids}
```

### Comparing `abacusai-0.9.1/abacusai/schema.py` & `abacusai-0.9.2/abacusai/schema.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/streaming_auth_token.py` & `abacusai-0.9.2/abacusai/streaming_auth_token.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/training_config_options.py` & `abacusai-0.9.2/abacusai/training_config_options.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/use_case.py` & `abacusai-0.9.2/abacusai/use_case.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai/use_case_requirements.py` & `abacusai-0.9.2/abacusai/use_case_requirements.py`

 * *Files identical despite different names*

### Comparing `abacusai-0.9.1/abacusai.egg-info/PKG-INFO` & `abacusai-0.9.2/abacusai.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: abacusai
-Version: 0.9.1
+Version: 0.9.2
 Summary: Abacus.AI Python Client Library
 Home-page: https://abacus.ai
 Author: Abacus.AI
 Author-email: dev@abacus.ai
 License: MIT
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `abacusai-0.9.1/abacusai.egg-info/SOURCES.txt` & `abacusai-0.9.2/abacusai.egg-info/SOURCES.txt`

 * *Files 6% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 abacusai/bucket_verification_result.py
 abacusai/client.py
 abacusai/dataset.py
 abacusai/dataset_upload.py
 abacusai/dataset_version.py
 abacusai/deployment.py
 abacusai/deployment_auth_token.py
+abacusai/external_connection.py
 abacusai/model.py
 abacusai/model_metrics.py
 abacusai/model_version.py
 abacusai/project.py
 abacusai/project_dataset.py
 abacusai/project_validation.py
 abacusai/refresh_pipeline_run.py
```

### Comparing `abacusai-0.9.1/setup.py` & `abacusai-0.9.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from setuptools import setup
 setup(name='abacusai',
-      version='0.9.1',
+      version='0.9.2',
       description='Abacus.AI Python Client Library',
       url='https://abacus.ai',
       author='Abacus.AI',
       author_email='dev@abacus.ai',
       license='MIT',
       packages=['abacusai'],
       install_requires=['packaging', 'requests'],
```

