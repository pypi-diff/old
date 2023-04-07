# Comparing `tmp/matroid-1.2.3.tar.gz` & `tmp/matroid-1.2.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "matroid-1.2.3.tar", last modified: Fri Sep  2 00:15:15 2022, max compression
+gzip compressed data, was "matroid-1.2.5.tar", last modified: Thu Apr  6 23:56:30 2023, max compression
```

## Comparing `matroid-1.2.3.tar` & `matroid-1.2.5.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:15:15.035631 matroid-1.2.3/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      246 2022-09-02 00:15:15.035631 matroid-1.2.3/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     8690 2022-09-02 00:14:55.000000 matroid-1.2.3/README.md
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:15:15.035631 matroid-1.2.3/matroid/
--rw-r--r--   0 circleci  (3434) circleci  (3434)       83 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3898 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/client.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1217 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/error.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:15:15.035631 matroid-1.2.3/matroid/src/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2187 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/accounts.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7786 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/collections.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10775 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/detectors.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     9042 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/helpers.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3974 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/images.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5225 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/labels.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5563 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/streams.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6415 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/video_summary.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     3349 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/src/videos.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)       18 2022-09-02 00:14:55.000000 matroid-1.2.3/matroid/version.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:15:15.035631 matroid-1.2.3/matroid.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)      246 2022-09-02 00:15:14.000000 matroid-1.2.3/matroid.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      714 2022-09-02 00:15:15.000000 matroid-1.2.3/matroid.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-09-02 00:15:14.000000 matroid-1.2.3/matroid.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        9 2022-09-02 00:15:14.000000 matroid-1.2.3/matroid.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       13 2022-09-02 00:15:14.000000 matroid-1.2.3/matroid.egg-info/top_level.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2022-09-02 00:15:15.035631 matroid-1.2.3/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)      463 2022-09-02 00:14:55.000000 matroid-1.2.3/setup.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:15:15.035631 matroid-1.2.3/test/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2022-09-02 00:14:55.000000 matroid-1.2.3/test/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      969 2022-09-02 00:14:55.000000 matroid-1.2.3/test/conftest.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      803 2022-09-02 00:14:55.000000 matroid-1.2.3/test/data.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)      119 2022-09-02 00:14:55.000000 matroid-1.2.3/test/helper.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1385 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_accounts.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5714 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_collections.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    11943 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_detectors_labels.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2328 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_images.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5659 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_streams.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     7342 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_video_summary.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1385 2022-09-02 00:14:55.000000 matroid-1.2.3/test/test_videos.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:30.693081 matroid-1.2.5/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      246 2023-04-06 23:56:30.693081 matroid-1.2.5/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     8690 2023-04-06 23:56:08.000000 matroid-1.2.5/README.md
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:30.689081 matroid-1.2.5/matroid/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       83 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3925 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/client.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1217 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/error.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:30.689081 matroid-1.2.5/matroid/src/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2193 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/accounts.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7816 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/collections.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10796 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/detectors.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     9121 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/helpers.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3980 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/images.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5243 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/labels.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6724 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/streams.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     6980 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/video_summary.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     3355 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/src/videos.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       18 2023-04-06 23:56:08.000000 matroid-1.2.5/matroid/version.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:30.689081 matroid-1.2.5/matroid.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      246 2023-04-06 23:56:30.000000 matroid-1.2.5/matroid.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      714 2023-04-06 23:56:30.000000 matroid-1.2.5/matroid.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2023-04-06 23:56:30.000000 matroid-1.2.5/matroid.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        9 2023-04-06 23:56:30.000000 matroid-1.2.5/matroid.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       13 2023-04-06 23:56:30.000000 matroid-1.2.5/matroid.egg-info/top_level.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2023-04-06 23:56:30.693081 matroid-1.2.5/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      463 2023-04-06 23:56:08.000000 matroid-1.2.5/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:30.693081 matroid-1.2.5/test/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2023-04-06 23:56:08.000000 matroid-1.2.5/test/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      969 2023-04-06 23:56:08.000000 matroid-1.2.5/test/conftest.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      803 2023-04-06 23:56:08.000000 matroid-1.2.5/test/data.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      119 2023-04-06 23:56:08.000000 matroid-1.2.5/test/helper.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1385 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_accounts.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5714 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_collections.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    11943 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_detectors_labels.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2328 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_images.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7385 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_streams.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     7580 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_video_summary.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1385 2023-04-06 23:56:08.000000 matroid-1.2.5/test/test_videos.py
```

### Comparing `matroid-1.2.3/README.md` & `matroid-1.2.5/README.md`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/matroid/client.py` & `matroid-1.2.5/matroid/client.py`

 * *Files 2% similar despite different names*

```diff
@@ -41,14 +41,15 @@
         delete_monitoring,
         delete_stream,
         get_monitoring_result,
         kill_monitoring,
         monitor_stream,
         search_monitorings,
         search_streams,
+        update_monitoring,
     )
     from matroid.src.labels import (
         create_label_with_images,
         delete_label,
         get_annotations,
         get_label_images,
         update_annotations,
```

### Comparing `matroid-1.2.3/matroid/error.py` & `matroid-1.2.5/matroid/error.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/matroid/src/accounts.py` & `matroid-1.2.5/matroid/src/accounts.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import requests
 
 from matroid import error
 from matroid.src.helpers import api_call
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Accounts-RefreshToken
+# https://staging.app.matroid.com/docs/api/documentation#api-Accounts-RefreshToken
 
 
 def retrieve_token(self, options={}):
     """
     Generates an OAuth token. The API client will intelligently refresh the Access Token for you
     However, if you would like to manually expire an existing token and create a new token,
     call this method manually and pass in 'expire_token': True in the options argument.
@@ -40,15 +40,15 @@
     self.check_errors(response, error.AuthorizationError)
 
     self.save_token(response)
 
     return response.json()
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Accounts-GetAccount
+# https://staging.app.matroid.com/docs/api/documentation#api-Accounts-GetAccount
 @api_call(error.InvalidQueryError)
 def account_info(self):
     """Get user account and credits information"""
     (endpoint, method) = self.endpoints["account_info"]
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
```

### Comparing `matroid-1.2.3/matroid/src/collections.py` & `matroid-1.2.5/matroid/src/collections.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 import os
 import requests
 import json
 
 from matroid import error
 from matroid.src.helpers import api_call
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-PostApiVersionCollectionsCollectionidCollectionTasks
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-PostApiVersionCollectionsCollectionidCollectionTasks
 @api_call(error.InvalidQueryError)
 def create_collection_index(self, collectionId, detectorId, fileTypes):
     """Create an index on a collection with a detector"""
     (endpoint, method) = self.endpoints["create_collection_index"]
     endpoint = endpoint.replace(":key", collectionId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         data = {"detectorId": detectorId, "fileTypes": fileTypes}
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-PostCollections
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-PostCollections
 @api_call(error.InvalidQueryError)
 def create_collection(self, name, url, sourceType, **options):
     """Creates a new collection from a web or S3 url. Automatically kick off default indexes"""
     (endpoint, method) = self.endpoints["create_collection"]
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
@@ -36,86 +36,86 @@
         }
 
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-DeleteCollectionTasksTaskid
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-DeleteCollectionTasksTaskid
 @api_call(error.InvalidQueryError)
 def delete_collection_index(self, taskId):
     """Deletes a completed collection mananger task"""
     (endpoint, method) = self.endpoints["delete_collection_index"]
     endpoint = endpoint.replace(":key", taskId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-DeleteCollectionsCollectionid
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-DeleteCollectionsCollectionid
 @api_call(error.InvalidQueryError)
 def delete_collection(self, collectionId):
     """Deletes a collection with no active indexing tasks"""
     (endpoint, method) = self.endpoints["delete_collection"]
     endpoint = endpoint.replace(":key", collectionId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-GetCollectionTasksTaskid
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-GetCollectionTasksTaskid
 @api_call(error.InvalidQueryError)
 def get_collection_task(self, taskId):
     """Creates a new collection from a web or S3 url"""
     (endpoint, method) = self.endpoints["get_collection_task"]
     endpoint = endpoint.replace(":key", taskId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-GetCollectionsCollectionid
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-GetCollectionsCollectionid
 @api_call(error.InvalidQueryError)
 def get_collection(self, collectionId):
     """Get information about a specific collection"""
     (endpoint, method) = self.endpoints["get_collection"]
     endpoint = endpoint.replace(":key", collectionId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-PostCollectionTasksTaskidKill
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-PostCollectionTasksTaskidKill
 @api_call(error.InvalidQueryError)
 def kill_collection_index(self, taskId, includeCollectionInfo):
     """Kills an active collection indexing task"""
     (endpoint, method) = self.endpoints["kill_collection_index"]
     endpoint = endpoint.replace(":key", taskId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         data = {"includeCollectionInfo": "true" if includeCollectionInfo else ""}
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-PostApiVersionCollectionTasksTaskidScoresQuery
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-PostApiVersionCollectionTasksTaskidScoresQuery
 @api_call(error.InvalidQueryError)
 def query_collection_by_scores(self, taskId, thresholds, **options):
     """
     Query against a collection index using a set of labels and scores as a query.
     Takes in a map of thresholds, and returns media in the collection with detections above those thresholds
     """
     (endpoint, method) = self.endpoints["query_collection_by_scores"]
@@ -128,15 +128,15 @@
             "numResults": options.get("numResults"),
         }
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-PostApiCollectionTasksTaskidImageQuery
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-PostApiCollectionTasksTaskidImageQuery
 @api_call(error.InvalidQueryError)
 def query_collection_by_image(self, taskId, url=None, file=None, **options):
     """
     Query against a collection index (CollectionManagerTask) using an image as key.
     Takes in an image file or url and returns similar media from the collection.
     """
     (endpoint, method) = self.endpoints["query_collection_by_image"]
@@ -171,15 +171,15 @@
     except Exception as e:
         raise error.APIConnectionError(message=e)
     finally:
         if file_to_upload:
             file_to_upload.close()
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Collections-PutApiVersionCollectionTasksTaskid
+# https://staging.app.matroid.com/docs/api/documentation#api-Collections-PutApiVersionCollectionTasksTaskid
 @api_call(error.InvalidQueryError)
 def update_collection_index(self, taskId, updateIndex):
     """Update a collection index"""
     (endpoint, method) = self.endpoints["update_collection_index"]
     endpoint = endpoint.replace(":key", taskId)
 
     try:
```

### Comparing `matroid-1.2.3/matroid/src/detectors.py` & `matroid-1.2.5/matroid/src/detectors.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import os
 import requests
 import json
 
 from matroid import error
 from matroid.src.helpers import api_call
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-PostDetectors
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-PostDetectors
 @api_call(error.InvalidQueryError)
 def create_detector(self, file, name, detectorType, **options):
     """
     Create a new detector with the contents of the zip file
 
     detector_type: general, facial_recognition, or facial_characteristics
     name: the detector's display name
@@ -64,15 +64,15 @@
             return requests.request(
                 method, endpoint, **{"headers": headers, "files": files, "data": data}
             )
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-DeleteDetectorsDetector_id
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-DeleteDetectorsDetector_id
 @api_call(error.InvalidQueryError)
 def delete_detector(self, detectorId):
     """
     Requires processing=false.
     Note: Users can only delete pending detectors; once finalized, the only way to delete is via the Web UI.
     """
     (endpoint, method) = self.endpoints["delete_detector"]
@@ -82,15 +82,15 @@
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-PostDetectorsDetector_idFinalize
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-PostDetectorsDetector_idFinalize
 @api_call(error.InvalidQueryError)
 def finalize_detector(self, detectorId):
     """Begin training the detector"""
     (endpoint, method) = self.endpoints["finalize_detector"]
 
     endpoint = endpoint.replace(":key", detectorId)
 
@@ -101,15 +101,15 @@
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
 train_detector = finalize_detector
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-GetDetectorsDetector_id
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-GetDetectorsDetector_id
 @api_call(error.InvalidQueryError)
 def get_detector_info(self, detectorId):
     """Get information about detector"""
     (endpoint, method) = self.endpoints["get_detector_info"]
 
     endpoint = endpoint.replace(":key", detectorId)
 
@@ -118,15 +118,15 @@
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
 detector_info = get_detector_info
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-PostDetectorsUpload
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-PostDetectorsUpload
 @api_call(error.InvalidQueryError)
 def import_detector(self, name, **options):
     """
     Note: certain combination of parameters can be supplied: file_detector, file_proto + file_label (+ file_label_ind), or file_proto + labels (+ label_inds). Parentheses part can be optionally supplied for object detection.
     """
     (endpoint, method) = self.endpoints["import_detector"]
 
@@ -176,15 +176,15 @@
         raise error.APIConnectionError(message=e)
     finally:
         for file_keyword, file_obj in file_objs.items():
             if isinstance(file_obj, io.IOBase):
                 file_obj.close()
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-PostDetectorsDetector_idRedo
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-PostDetectorsDetector_idRedo
 @api_call(error.InvalidQueryError)
 def redo_detector(self, detectorId, **options):
     """
     Redo a detector
     Note: a deep copy of the trained detector with different detector_id will be made
     """
     (endpoint, method) = self.endpoints["redo_detector"]
@@ -195,15 +195,15 @@
         headers = {"Authorization": self.token.authorization_header()}
         data = {"feedbackOnly": "true" if options.get("feedbackOnly") else "false"}
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Detectors-Search
+# https://staging.app.matroid.com/docs/api/documentation#api-Detectors-Search
 @api_call(error.InvalidQueryError)
 def search_detectors(self, **query):
     """Lists the available detectors"""
     (endpoint, method) = self.endpoints["detectors"]
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
```

### Comparing `matroid-1.2.3/matroid/src/helpers.py` & `matroid-1.2.5/matroid/src/helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -196,14 +196,15 @@
         # streams
         "create_stream": (base_url + "/streams", "POST"),
         "delete_monitoring": (base_url + "/monitorings/:key", "DELETE"),
         "delete_stream": (base_url + "/streams/:key", "DELETE"),
         "get_monitoring_result": (base_url + "/monitorings/:key", "GET"),
         "kill_monitoring": (base_url + "/monitorings/:key/kill", "POST"),
         "monitor_stream": (base_url + "/streams/:streamId/monitor/:detectorId", "POST"),
+        "update_monitoring": (base_url + "/monitorings/:monitoringId", "PUT"),
         "search_monitorings": (base_url + "/monitorings", "GET"),
         "search_streams": (base_url + "/streams", "GET"),
         # labels
         "create_label_with_images": (base_url + "/detectors/:key/labels", "POST"),
         "delete_label": (base_url + "/detectors/:detectorId/labels/:labelId", "DELETE"),
         "get_annotations": (base_url + "/images/annotations", "GET"),
         "get_label_images": (
```

### Comparing `matroid-1.2.3/matroid/src/images.py` & `matroid-1.2.5/matroid/src/images.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import os
 import requests
 
 from matroid import error
 from matroid.src.helpers import api_call, batch_file_request
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Images-Classify
+# https://staging.app.matroid.com/docs/api/documentation#api-Images-Classify
 @api_call(error.InvalidQueryError)
 def classify_image(self, detectorId, file=None, url=None, **options):
     """
     Classify an image with a detector
 
     detectorId: a unique id for the detector
     file: path to local image file to classify
@@ -42,15 +42,15 @@
         raise e
     except error.InvalidQueryError as e:
         raise e
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Images-PostLocalize
+# https://staging.app.matroid.com/docs/api/documentation#api-Images-PostLocalize
 @api_call(error.InvalidQueryError)
 def localize_image(self, localizer, localizerLabel, **options):
     """
     Note: this API is very similar to Images/Classify;
     however, it can be used to update bounding boxes of existing training images
     by supplying update=true, labelId, and one of imageId or imageIds, and it has
     access to the internal face localizer
```

### Comparing `matroid-1.2.3/matroid/src/labels.py` & `matroid-1.2.5/matroid/src/labels.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import requests
 import json
 
 from matroid import error
 from matroid.src.helpers import api_call, batch_file_request
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Labels-PostDetectorsDetector_idLabels
+# https://staging.app.matroid.com/docs/api/documentation#api-Labels-PostDetectorsDetector_idLabels
 @api_call(error.InvalidQueryError)
 def create_label_with_images(self, detectorId, name, imageFiles, **options):
     """Create a label. Requires processing=false. Creates label asynchronously (turn processing to true)"""
     (endpoint, method) = self.endpoints["create_label_with_images"]
     endpoint = endpoint.replace(":key", detectorId)
 
     try:
@@ -31,30 +31,30 @@
         raise e
     except error.InvalidQueryError as e:
         raise e
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Labels-DeleteDetectorsDetector_idLabelsLabel_id
+# https://staging.app.matroid.com/docs/api/documentation#api-Labels-DeleteDetectorsDetector_idLabelsLabel_id
 @api_call(error.InvalidQueryError)
 def delete_label(self, detectorId, labelId):
     """Delete a label. Requires processing=false"""
     (endpoint, method) = self.endpoints["delete_label"]
     endpoint = endpoint.replace(":detectorId", detectorId)
     endpoint = endpoint.replace(":labelId", labelId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Labels-GetImagesAnnotationsQuery
+# https://staging.app.matroid.com/docs/api/documentation#api-Labels-GetImagesAnnotationsQuery
 @api_call(error.InvalidQueryError)
 def get_annotations(self, **options):
     """Get annotations. Requires processing=false. Note: you need to provide at least one of the three ids to query"""
     (endpoint, method) = self.endpoints["get_annotations"]
 
     detector_id = options.get("detectorId")
     label_ids = options.get("labelIds")
@@ -75,29 +75,29 @@
         return requests.request(
             method, endpoint, **{"headers": headers, "params": params}
         )
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Labels-GetDetectorsDetector_idLabelsLabel_id
+# https://staging.app.matroid.com/docs/api/documentation#api-Labels-GetDetectorsDetector_idLabelsLabel_id
 @api_call(error.InvalidQueryError)
 def get_label_images(self, detectorId, labelId):
     (endpoint, method) = self.endpoints["get_label_images"]
     endpoint = endpoint.replace(":detectorId", detectorId)
     endpoint = endpoint.replace(":labelId", labelId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Labels-UpdateAnnotations
+# https://staging.app.matroid.com/docs/api/documentation#api-Labels-UpdateAnnotations
 @api_call(error.InvalidQueryError)
 def update_annotations(self, detectorId, labelId, images, **options):
     (endpoint, method) = self.endpoints["update_annotations"]
     endpoint = endpoint.replace(":detectorId", detectorId)
     endpoint = endpoint.replace(":labelId", labelId)
 
     try:
@@ -108,15 +108,15 @@
         data.update(options)
 
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Labels-PostDetectorsDetector_idLabelsLabel_idImages
+# https://staging.app.matroid.com/docs/api/documentation#api-Labels-PostDetectorsDetector_idLabelsLabel_idImages
 @api_call(error.InvalidQueryError)
 def update_label_with_images(self, detectorId, labelId, imageFiles, **options):
     """Requires processing=false. Updates label asynchronously (turn processing to true)"""
     (endpoint, method) = self.endpoints["update_label_with_images"]
     endpoint = endpoint.replace(":detectorId", detectorId)
     endpoint = endpoint.replace(":labelId", labelId)
```

### Comparing `matroid-1.2.3/matroid/src/streams.py` & `matroid-1.2.5/matroid/src/streams.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import requests
 import json
 
 from matroid import error
 from matroid.src.helpers import api_call
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-PostStreams
+
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-PostStreams
 @api_call(error.InvalidQueryError)
 def create_stream(self, url, name, **options):
     (endpoint, method) = self.endpoints["create_stream"]
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         data = {"name": name, "url": url}
@@ -18,41 +19,42 @@
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
 # register_stream is now DEPRECATED in favor of create_stream (kept for backwards-compatibility)
 register_stream = create_stream
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-DeleteMonitoringsMonitoring_id
+
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-DeleteMonitoringsMonitoring_id
 @api_call(error.InvalidQueryError)
 def delete_monitoring(self, monitoringId):
     (endpoint, method) = self.endpoints["delete_monitoring"]
     endpoint = endpoint.replace(":key", monitoringId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-DeleteStreamsStream_id
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-DeleteStreamsStream_id
 @api_call(error.InvalidQueryError)
 def delete_stream(self, streamId):
     (endpoint, method) = self.endpoints["delete_stream"]
     endpoint = endpoint.replace(":key", streamId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-GetMonitoringsMonitoring_idQuery
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-GetMonitoringsMonitoring_idQuery
 @api_call(error.InvalidQueryError)
 def get_monitoring_result(self, monitoringId, **options):
     (endpoint, method) = self.endpoints["get_monitoring_result"]
     endpoint = endpoint.replace(":key", monitoringId)
 
     if options.get("format") == "csv" and self.json_format:
         print(
@@ -73,28 +75,28 @@
         return requests.request(
             method, endpoint, **{"headers": headers, "params": params}
         )
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-PostMonitoringsMonitoring_idKill
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-PostMonitoringsMonitoring_idKill
 @api_call(error.InvalidQueryError)
 def kill_monitoring(self, monitoringId):
     (endpoint, method) = self.endpoints["kill_monitoring"]
     endpoint = endpoint.replace(":key", monitoringId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-PostStreamsStream_idMonitorDetector_id
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-PostStreamsStream_idMonitorDetector_id
 @api_call(error.InvalidQueryError)
 def monitor_stream(self, streamId, detectorId, thresholds, **options):
     (endpoint, method) = self.endpoints["monitor_stream"]
     endpoint = endpoint.replace(":detectorId", detectorId)
     endpoint = endpoint.replace(":streamId", streamId)
 
     try:
@@ -102,22 +104,51 @@
         data = {
             "thresholds": json.dumps(thresholds),
             "sendEmailNotifications": "true"
             if options.get("sendEmailNotifications")
             else "false",
             "regionEnabled": "true" if options.get("regionEnabled") else "false",
         }
+
+        if options.get("minDetectionInterval"):
+            try:
+                data["minDetectionInterval"] = int(options.get("minDetectionInterval"))
+            except ValueError:
+                pass  # doesnt parse to int
+
         data.update(options)
 
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-GetMonitoringsQuery
+@api_call(error.InvalidQueryError)
+def update_monitoring(self, monitoringId, **options):
+    (endpoint, method) = self.endpoints["update_monitoring"]
+    endpoint = endpoint.replace(":monitoringId", monitoringId)
+
+    try:
+        headers = {"Authorization": self.token.authorization_header()}
+        data = {
+            "detection": options.get("detection") if options.get("detection") else {},
+            "schedule": options.get("schedule") if options.get("schedule") else {},
+            "registeredEndpoint": options.get("registeredEndpoint")
+            if options.get("registeredEndpoint")
+            else {},
+            "region": options.get("region") if options.get("region") else {},
+        }
+
+        data.update(options)
+        return requests.request(method, endpoint, **{"headers": headers, "json": data})
+    except Exception as e:
+        raise error.APIConnectionError(message=e)
+
+
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-GetMonitoringsQuery
 @api_call(error.InvalidQueryError)
 def search_monitorings(self, **options):
     (endpoint, method) = self.endpoints["search_monitorings"]
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         params = {}
@@ -126,15 +157,15 @@
         return requests.request(
             method, endpoint, **{"headers": headers, "params": params}
         )
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Streams-GetStreamsQuery
+# https://staging.app.matroid.com/docs/api/documentation#api-Streams-GetStreamsQuery
 @api_call(error.InvalidQueryError)
 def search_streams(self, **options):
     (endpoint, method) = self.endpoints["search_streams"]
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         params = {
```

### Comparing `matroid-1.2.3/matroid/src/video_summary.py` & `matroid-1.2.5/matroid/src/video_summary.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,27 +1,32 @@
 import requests
 
 from matroid import error
 from matroid.src.helpers import api_call
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-PostSummarize
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-PostSummarize
 @api_call(error.InvalidQueryError)
 def create_video_summary(
     self,
     detectorId,
+    name=None,
     labels=None,
     url=None,
     videoId=None,
     file=None,
     fps=None,
-    featureWeight=None,
-    motionWeight=None,
-    matchingDistance=None,
+    mc_lambda=None,
+    matching_distance=None,
+    n_init=None,
+    nn_budget=None,
+    max_iou_dist=None,
+    max_age=None,
+    detection_threshold=None,
 ):
-    """Create an video summary with provided url or file"""
+    """Create a video summary with provided url or file"""
     (endpoint, method) = self.endpoints["create_video_summary"]
 
     if not detectorId:
         raise error.InvalidQueryError(message="Missing required parameter: detectorID")
 
     if not file and not url:
         raise error.InvalidQueryError(message="Missing required parameter: file or url")
@@ -30,20 +35,25 @@
         raise error.InvalidQueryError(
             message="You may only specify a file or a URL, not both"
         )
     try:
         file_to_upload = None
         headers = {"Authorization": self.token.authorization_header()}
         data = {
+            "name": name,
             "detectorId": detectorId,
             "labels": labels,
             "fps": fps,
-            "featureWeight": featureWeight,
-            "motionWeight": motionWeight,
-            "matchingDistance": matchingDistance,
+            "mc_lambda": mc_lambda,
+            "matching_distance": matching_distance,
+            "n_init": n_init,
+            "nn_budget": nn_budget,
+            "max_iou_dist": max_iou_dist,
+            "max_age": max_age,
+            "detection_threshold": detection_threshold,
         }
         if file:
             file_to_upload = self.filereader.get_file(file)
             files = {"file": file_to_upload}
 
             return requests.request(
                 method, endpoint, **{"headers": headers, "files": files, "data": data}
@@ -63,126 +73,136 @@
     except Exception as e:
         raise error.APIConnectionError(message=e)
     finally:
         if file_to_upload:
             file_to_upload.close()
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-GetSummariesSummaryid
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-GetSummariesSummaryid
 @api_call(error.InvalidQueryError)
 def get_video_summary(self, summaryId):
     """Fetch a video summary"""
     (endpoint, method) = self.endpoints["get_video_summary"]
     endpoint = endpoint.replace(":summaryId", summaryId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
 
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-GetSummariesSummaryidTracksCsv
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-GetSummariesSummaryidTracksCsv
 @api_call(error.InvalidQueryError)
 def get_video_summary_tracks(self, summaryId):
     """Fetch a video summary track CSV"""
     (endpoint, method) = self.endpoints["get_video_summary_tracks"]
     endpoint = endpoint.replace(":summaryId", summaryId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
 
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-GetSummariesSummaryidVideoMp4
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-GetSummariesSummaryidVideoMp4
 @api_call(error.InvalidQueryError)
 def get_video_summary_file(self, summaryId):
     """Fetch a video summary video file"""
     (endpoint, method) = self.endpoints["get_video_summary_file"]
     endpoint = endpoint.replace(":summaryId", summaryId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
 
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-DeleteSummariesSummaryid
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-DeleteSummariesSummaryid
 @api_call(error.InvalidQueryError)
 def delete_video_summary(self, summaryId):
     """Delete a video summary"""
     (endpoint, method) = self.endpoints["delete_video_summary"]
     endpoint = endpoint.replace(":summaryId", summaryId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
 
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-GetStreamsStreamidSummaries
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-GetStreamsStreamidSummaries
 @api_call(error.InvalidQueryError)
 def get_stream_summaries(self, streamId):
     """Fetch all video summaries for a stream"""
     (endpoint, method) = self.endpoints["get_stream_summaries"]
     endpoint = endpoint.replace(":streamId", streamId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
 
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Video_Summary-PostStreamsStreamidSummarize
+# https://staging.app.matroid.com/docs/api/documentation#api-Video_Summary-PostStreamsStreamidSummarize
 @api_call(error.InvalidQueryError)
 def create_stream_summary(
     self,
     streamId,
     startTime,
     endTime,
     detectorId,
+    name=None,
     labels=None,
     fps=None,
-    featureWeight=None,
-    motionWeight=None,
-    matchingDistance=None,
+    mc_lambda=None,
+    matching_distance=None,
+    n_init=None,
+    nn_budget=None,
+    max_iou_dist=None,
+    max_age=None,
+    detection_threshold=None,
 ):
     """Create a video summary for a stream"""
     (endpoint, method) = self.endpoints["create_stream_summary"]
     endpoint = endpoint.replace(":streamId", streamId)
 
     try:
         headers = {"Authorization": self.token.authorization_header()}
         data = {
+            "name": name,
             "startTime": startTime,
             "endTime": endTime,
             "detectorId": detectorId,
             "labels": labels,
             "fps": fps,
-            "featureWeight": featureWeight,
-            "motionWeight": motionWeight,
-            "matchingDistance": matchingDistance,
+            "mc_lambda": mc_lambda,
+            "matching_distance": matching_distance,
+            "n_init": n_init,
+            "nn_budget": nn_budget,
+            "max_iou_dist": max_iou_dist,
+            "max_age": max_age,
+            "detection_threshold": detection_threshold,
         }
 
         return requests.request(method, endpoint, **{"headers": headers, "data": data})
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.dev.matroid.com/docs/api/index.html#api-Video_Summary-GetSummaries
+# https://staging.dev.matroid.com/docs/api/documentation#api-Video_Summary-GetSummaries
 @api_call(error.InvalidQueryError)
 def get_existing_summaries(self):
     (endpoint, method) = self.endpoints["get_existing_summaries"]
     try:
         headers = {"Authorization": self.token.authorization_header()}
         return requests.request(method, endpoint, **{"headers": headers})
     except Exception as e:
```

### Comparing `matroid-1.2.3/matroid/src/videos.py` & `matroid-1.2.5/matroid/src/videos.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import os
 import requests
 
 from matroid import error
 from matroid.src.helpers import api_call
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Videos-PostDetectorsDetector_idClassify_video
+# https://staging.app.matroid.com/docs/api/documentation#api-Videos-PostDetectorsDetector_idClassify_video
 @api_call(error.InvalidQueryError)
 def classify_video(self, detectorId, url=None, file=None, **options):
     """
     Classify a video from a url with a detector
 
     detectorId: a unique id for the detector
     url: internet URL for the video to classify
@@ -61,15 +61,15 @@
                 )
     except error.InvalidQueryError as e:
         raise e
     except Exception as e:
         raise error.APIConnectionError(message=e)
 
 
-# https://staging.app.matroid.com/docs/api/index.html#api-Videos-GetVideosVideo_idQuery
+# https://staging.app.matroid.com/docs/api/documentation#api-Videos-GetVideosVideo_idQuery
 @api_call(error.InvalidQueryError)
 def get_video_results(self, videoId, **options):
     """
     Get the current classifications for a given video ID
 
     videoId: a unique id for the classified video
     threshold: the cutoff for confidence level in the detection at each timestamp
```

### Comparing `matroid-1.2.3/matroid.egg-info/SOURCES.txt` & `matroid-1.2.5/matroid.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/conftest.py` & `matroid-1.2.5/test/conftest.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/data.py` & `matroid-1.2.5/test/data.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/test_accounts.py` & `matroid-1.2.5/test/test_accounts.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/test_collections.py` & `matroid-1.2.5/test/test_collections.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/test_detectors_labels.py` & `matroid-1.2.5/test/test_detectors_labels.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/test_images.py` & `matroid-1.2.5/test/test_images.py`

 * *Files identical despite different names*

### Comparing `matroid-1.2.3/test/test_video_summary.py` & `matroid-1.2.5/test/test_video_summary.py`

 * *Files 8% similar despite different names*

```diff
@@ -56,44 +56,50 @@
                 self.delete_video_summary_test(summaryId=local_video_summary_id)
             if stream_summary_id:
                 self.delete_video_summary_test(summaryId=stream_summary_id)
             if stream_id:
                 self.delete_stream_test(streamId=stream_id)
 
     # test cases
-    def create_video_summary_test(self, url=None, videoId=None, file=None):
+    def create_video_summary_test(
+        self, url=None, videoId=None, file=None, name="Summary"
+    ):
         if url and file:
             with pytest.raises(APIError) as e:
                 self.api.create_video_summary(
                     detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
                     url=url,
                     file=file,
                     labels=DETECTOR_LABELS,
+                    name=name,
                 )
             assert "You may only specify a file or a URL, not both" in str(e)
 
         if url:
             with pytest.raises(APIError) as e:
                 self.api.create_video_summary(
                     detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
                     url=TEST_LOCAL_VIDEO_URL,
                     labels=DETECTOR_LABELS,
+                    name=name,
                 )
             assert "You provided an invalid URL" in str(e)
 
             res = self.api.create_video_summary(
                 detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
                 url=url,
                 labels=DETECTOR_LABELS,
+                name=name,
             )
         if file:
             res = self.api.create_video_summary(
                 detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
                 file=file,
                 labels=DETECTOR_LABELS,
+                name=name,
             )
 
         assert res["summary"]["video"] != None
         assert res["summary"]["network"] == EVERYDAY_OBJECT_DETECTOR_ID
 
         print_test_pass()
         return res["summary"]["_id"]
@@ -124,14 +130,15 @@
 
         print_test_pass()
 
     def create_stream_summary_test(self, streamId, startTime, endTime):
         with pytest.raises(APIError) as e:
             self.api.create_stream_summary(
                 streamId=streamId,
+                name="Summary",
                 startTime="test",
                 endTime=endTime,
                 detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
                 labels=DETECTOR_LABELS,
             )
         assert "Invalid dates provided" in str(e)
         with pytest.raises(APIError) as e:
@@ -139,23 +146,25 @@
                 detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
                 labels=DETECTOR_LABELS,
                 streamId=streamId,
                 startTime=datetime.utcfromtimestamp(
                     int(time.time()) - (24 * 60 * 60 * 8)
                 ),
                 endTime=endTime,
+                name="Summary",
             )
         assert "Provided dates are not within your stream" in str(e)
 
         res = self.api.create_stream_summary(
             streamId,
             startTime,
             endTime,
             detectorId=EVERYDAY_OBJECT_DETECTOR_ID,
             labels=DETECTOR_LABELS,
+            name="Summary",
         )
         assert res["summary"]["feed"] == streamId
         assert (
             datetime.strptime(res["summary"]["startTime"], "%Y-%m-%dT%H:%M:%S.000Z")
             == startTime
         )
         assert (
```

### Comparing `matroid-1.2.3/test/test_videos.py` & `matroid-1.2.5/test/test_videos.py`

 * *Files identical despite different names*

