# Comparing `tmp/luminesce-sdk-preview-1.9.88.tar.gz` & `tmp/luminesce-sdk-preview-1.9.92.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/luminesce-sdk-preview-1.9.88.tar", last modified: Tue May 31 11:32:36 2022, max compression
+gzip compressed data, was "dist/luminesce-sdk-preview-1.9.92.tar", last modified: Tue May 31 14:25:05 2022, max compression
```

## Comparing `luminesce-sdk-preview-1.9.88.tar` & `luminesce-sdk-preview-1.9.92.tar`

### file list

```diff
@@ -1,54 +1,54 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/
--rw-r--r--   0 root         (0) root         (0)       45 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      354 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    12526 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce/
--rw-r--r--   0 root         (0) root         (0)     2789 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/__init__.py
--rw-r--r--   0 root         (0) root         (0)       23 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/__version__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce/api/
--rw-r--r--   0 root         (0) root         (0)      554 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6492 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/application_metadata_api.py
--rw-r--r--   0 root         (0) root         (0)     8953 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/current_table_field_catalog_api.py
--rw-r--r--   0 root         (0) root         (0)    46349 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/historically_executed_queries_api.py
--rw-r--r--   0 root         (0) root         (0)    28903 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/multi_query_execution_api.py
--rw-r--r--   0 root         (0) root         (0)   118594 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/sql_background_execution_api.py
--rw-r--r--   0 root         (0) root         (0)    97231 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api/sql_execution_api.py
--rw-r--r--   0 root         (0) root         (0)    27384 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/api_client.py
--rw-r--r--   0 root         (0) root         (0)    16612 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/configuration.py
--rw-r--r--   0 root         (0) root         (0)     5098 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce/models/
--rw-r--r--   0 root         (0) root         (0)     1920 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5781 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/access_controlled_action.py
--rw-r--r--   0 root         (0) root         (0)     7631 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/access_controlled_resource.py
--rw-r--r--   0 root         (0) root         (0)     9625 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/access_controlled_resource_identifier_part_schema_attribute.py
--rw-r--r--   0 root         (0) root         (0)     7221 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/action_id.py
--rw-r--r--   0 root         (0) root         (0)     7374 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/background_multi_query_progress_response.py
--rw-r--r--   0 root         (0) root         (0)    13695 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/background_multi_query_response.py
--rw-r--r--   0 root         (0) root         (0)     6958 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/background_query_cancel_response.py
--rw-r--r--   0 root         (0) root         (0)    12530 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/background_query_progress_response.py
--rw-r--r--   0 root         (0) root         (0)    12015 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/background_query_response.py
--rw-r--r--   0 root         (0) root         (0)     3744 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/background_query_state.py
--rw-r--r--   0 root         (0) root         (0)    12029 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/column.py
--rw-r--r--   0 root         (0) root         (0)     3401 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/condition_attributes.py
--rw-r--r--   0 root         (0) root         (0)     3501 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/data_type.py
--rw-r--r--   0 root         (0) root         (0)    10334 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/feedback_event_args.py
--rw-r--r--   0 root         (0) root         (0)     3785 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/feedback_level.py
--rw-r--r--   0 root         (0) root         (0)     7728 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/id_selector_definition.py
--rw-r--r--   0 root         (0) root         (0)     6415 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/link.py
--rw-r--r--   0 root         (0) root         (0)    10136 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/lusid_problem_details.py
--rw-r--r--   0 root         (0) root         (0)     3778 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/multi_query_definition_type.py
--rw-r--r--   0 root         (0) root         (0)     7704 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/resource_list_of_access_controlled_resource.py
--rw-r--r--   0 root         (0) root         (0)     3659 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/models/task_status.py
--rw-r--r--   0 root         (0) root         (0)    12755 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/rest.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce/utilities/
--rw-r--r--   0 root         (0) root         (0)       56 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/utilities/__init__.py
--rw-r--r--   0 root         (0) root         (0)      944 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/utilities/config_keys.json
--rw-r--r--   0 root         (0) root         (0)      296 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/luminesce/utilities/config_keys.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/
--rw-r--r--   0 root         (0) root         (0)      354 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1758 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       98 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       10 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       38 2022-05-31 11:32:36.000000 luminesce-sdk-preview-1.9.88/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2215 2022-05-31 11:32:00.000000 luminesce-sdk-preview-1.9.88/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/
+-rw-r--r--   0 root         (0) root         (0)       45 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      354 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    12526 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce/
+-rw-r--r--   0 root         (0) root         (0)     2789 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/__init__.py
+-rw-r--r--   0 root         (0) root         (0)       23 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/__version__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce/api/
+-rw-r--r--   0 root         (0) root         (0)      554 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6492 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/application_metadata_api.py
+-rw-r--r--   0 root         (0) root         (0)     8953 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/current_table_field_catalog_api.py
+-rw-r--r--   0 root         (0) root         (0)    46349 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/historically_executed_queries_api.py
+-rw-r--r--   0 root         (0) root         (0)    28903 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/multi_query_execution_api.py
+-rw-r--r--   0 root         (0) root         (0)   118594 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/sql_background_execution_api.py
+-rw-r--r--   0 root         (0) root         (0)    97231 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api/sql_execution_api.py
+-rw-r--r--   0 root         (0) root         (0)    27384 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/api_client.py
+-rw-r--r--   0 root         (0) root         (0)    16612 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/configuration.py
+-rw-r--r--   0 root         (0) root         (0)     5098 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce/models/
+-rw-r--r--   0 root         (0) root         (0)     1920 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5781 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/access_controlled_action.py
+-rw-r--r--   0 root         (0) root         (0)     7631 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/access_controlled_resource.py
+-rw-r--r--   0 root         (0) root         (0)     9625 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/access_controlled_resource_identifier_part_schema_attribute.py
+-rw-r--r--   0 root         (0) root         (0)     7221 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/action_id.py
+-rw-r--r--   0 root         (0) root         (0)     7374 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/background_multi_query_progress_response.py
+-rw-r--r--   0 root         (0) root         (0)    13695 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/background_multi_query_response.py
+-rw-r--r--   0 root         (0) root         (0)     6958 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/background_query_cancel_response.py
+-rw-r--r--   0 root         (0) root         (0)    12530 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/background_query_progress_response.py
+-rw-r--r--   0 root         (0) root         (0)    12015 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/background_query_response.py
+-rw-r--r--   0 root         (0) root         (0)     3744 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/background_query_state.py
+-rw-r--r--   0 root         (0) root         (0)    12029 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/column.py
+-rw-r--r--   0 root         (0) root         (0)     3401 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/condition_attributes.py
+-rw-r--r--   0 root         (0) root         (0)     3501 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/data_type.py
+-rw-r--r--   0 root         (0) root         (0)    10334 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/feedback_event_args.py
+-rw-r--r--   0 root         (0) root         (0)     3785 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/feedback_level.py
+-rw-r--r--   0 root         (0) root         (0)     7728 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/id_selector_definition.py
+-rw-r--r--   0 root         (0) root         (0)     6415 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/link.py
+-rw-r--r--   0 root         (0) root         (0)    10136 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/lusid_problem_details.py
+-rw-r--r--   0 root         (0) root         (0)     3778 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/multi_query_definition_type.py
+-rw-r--r--   0 root         (0) root         (0)     7704 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/resource_list_of_access_controlled_resource.py
+-rw-r--r--   0 root         (0) root         (0)     3659 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/models/task_status.py
+-rw-r--r--   0 root         (0) root         (0)    12755 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/rest.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce/utilities/
+-rw-r--r--   0 root         (0) root         (0)       56 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/utilities/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      944 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/utilities/config_keys.json
+-rw-r--r--   0 root         (0) root         (0)      296 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/luminesce/utilities/config_keys.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      354 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1758 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       98 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       10 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2022-05-31 14:25:05.000000 luminesce-sdk-preview-1.9.92/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2215 2022-05-31 14:23:45.000000 luminesce-sdk-preview-1.9.92/setup.py
```

### Comparing `luminesce-sdk-preview-1.9.88/README.md` & `luminesce-sdk-preview-1.9.92/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # luminesce-sdk
 FINBOURNE Technology
 
 This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:
 
-- API version: 1.9.88
-- Package version: 1.9.88
+- API version: 1.9.92
+- Package version: 1.9.92
 - Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen
 For more information, please visit [https://www.finbourne.com](https://www.finbourne.com)
 
 ## Requirements.
 
 Python 2.7 and 3.4+
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/__init__.py` & `luminesce-sdk-preview-1.9.92/luminesce/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,23 +3,23 @@
 # flake8: noqa
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
-__version__ = "1.9.88"
+__version__ = "1.9.92"
 
 # import apis into sdk package
 from luminesce.api.application_metadata_api import ApplicationMetadataApi
 from luminesce.api.current_table_field_catalog_api import CurrentTableFieldCatalogApi
 from luminesce.api.historically_executed_queries_api import HistoricallyExecutedQueriesApi
 from luminesce.api.multi_query_execution_api import MultiQueryExecutionApi
 from luminesce.api.sql_background_execution_api import SqlBackgroundExecutionApi
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/__init__.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/__init__.py`

 * *Files identical despite different names*

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/application_metadata_api.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/application_metadata_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/current_table_field_catalog_api.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/current_table_field_catalog_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/historically_executed_queries_api.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/historically_executed_queries_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/multi_query_execution_api.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/multi_query_execution_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -500,15 +500,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             202: "BackgroundMultiQueryResponse",
             400: "LusidProblemDetails",
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/sql_background_execution_api.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/sql_background_execution_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 00000010: 0a22 2222 0a20 2020 2046 494e 424f 5552  .""".    FINBOUR
 00000020: 4e45 2048 6f6e 6579 636f 6d62 2057 6562  NE Honeycomb Web
 00000030: 2041 5049 0a0a 2020 2020 4649 4e42 4f55   API..    FINBOU
 00000040: 524e 4520 5465 6368 6e6f 6c6f 6779 2020  RNE Technology  
 00000050: 2320 6e6f 7161 3a20 4535 3031 0a0a 2020  # noqa: E501..  
 00000060: 2020 5468 6520 7665 7273 696f 6e20 6f66    The version of
 00000070: 2074 6865 204f 7065 6e41 5049 2064 6f63   the OpenAPI doc
-00000080: 756d 656e 743a 2031 2e39 2e38 380a 2020  ument: 1.9.88.  
+00000080: 756d 656e 743a 2031 2e39 2e39 320a 2020  ument: 1.9.92.  
 00000090: 2020 436f 6e74 6163 743a 2069 6e66 6f40    Contact: info@
 000000a0: 6669 6e62 6f75 726e 652e 636f 6d0a 2020  finbourne.com.  
 000000b0: 2020 4765 6e65 7261 7465 6420 6279 3a20    Generated by: 
 000000c0: 6874 7470 733a 2f2f 6f70 656e 6170 692d  https://openapi-
 000000d0: 6765 6e65 7261 746f 722e 7465 6368 0a22  generator.tech."
 000000e0: 2222 0a0a 0a66 726f 6d20 5f5f 6675 7475  ""...from __futu
 000000f0: 7265 5f5f 2069 6d70 6f72 7420 6162 736f  re__ import abso
@@ -7344,15 +7344,15 @@
 0001caf0: 6572 0a20 2020 2020 2020 2068 6561 6465  er.        heade
 0001cb00: 725f 7061 7261 6d73 5b27 582d 4c55 5349  r_params['X-LUSI
 0001cb10: 442d 5344 4b2d 4c61 6e67 7561 6765 275d  D-SDK-Language']
 0001cb20: 203d 2027 5079 7468 6f6e 270a 2020 2020   = 'Python'.    
 0001cb30: 2020 2020 6865 6164 6572 5f70 6172 616d      header_param
 0001cb40: 735b 2758 2d4c 5553 4944 2d53 444b 2d56  s['X-LUSID-SDK-V
 0001cb50: 6572 7369 6f6e 275d 203d 2027 312e 392e  ersion'] = '1.9.
-0001cb60: 3838 270a 0a20 2020 2020 2020 2023 2041  88'..        # A
+0001cb60: 3932 270a 0a20 2020 2020 2020 2023 2041  92'..        # A
 0001cb70: 7574 6865 6e74 6963 6174 696f 6e20 7365  uthentication se
 0001cb80: 7474 696e 670a 2020 2020 2020 2020 6175  tting.        au
 0001cb90: 7468 5f73 6574 7469 6e67 7320 3d20 5b27  th_settings = ['
 0001cba0: 6f61 7574 6832 275d 2020 2320 6e6f 7161  oauth2']  # noqa
 0001cbb0: 3a20 4535 3031 0a20 2020 2020 2020 200a  : E501.        .
 0001cbc0: 2020 2020 2020 2020 7265 7370 6f6e 7365          response
 0001cbd0: 5f74 7970 6573 5f6d 6170 203d 207b 0a20  _types_map = {.
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api/sql_execution_api.py` & `luminesce-sdk-preview-1.9.92/luminesce/api/sql_execution_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -954,15 +954,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             200: "str",
             400: "LusidProblemDetails",
@@ -1114,15 +1114,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             200: "str",
             400: "LusidProblemDetails",
@@ -1281,15 +1281,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             200: "str",
             400: "LusidProblemDetails",
@@ -1448,15 +1448,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             200: "str",
             400: "LusidProblemDetails",
@@ -1608,15 +1608,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             200: "str",
             400: "LusidProblemDetails",
@@ -1831,15 +1831,15 @@
 
         # HTTP header `Content-Type`
         header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
             ['text/plain'])  # noqa: E501
 
         # set the LUSID header
         header_params['X-LUSID-SDK-Language'] = 'Python'
-        header_params['X-LUSID-SDK-Version'] = '1.9.88'
+        header_params['X-LUSID-SDK-Version'] = '1.9.92'
 
         # Authentication setting
         auth_settings = ['oauth2']  # noqa: E501
         
         response_types_map = {
             200: "str",
             400: "LusidProblemDetails",
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/api_client.py` & `luminesce-sdk-preview-1.9.92/luminesce/api_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # coding: utf-8
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 from __future__ import absolute_import
 
 import atexit
@@ -75,15 +75,15 @@
 
         self.rest_client = rest.RESTClientObject(configuration)
         self.default_headers = {}
         if header_name is not None:
             self.default_headers[header_name] = header_value
         self.cookie = cookie
         # Set default User-Agent.
-        self.user_agent = 'OpenAPI-Generator/1.9.88/python'
+        self.user_agent = 'OpenAPI-Generator/1.9.92/python'
         self.client_side_validation = configuration.client_side_validation
 
     def __enter__(self):
         return self
 
     def __exit__(self, exc_type, exc_value, traceback):
         self.close()
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/configuration.py` & `luminesce-sdk-preview-1.9.92/luminesce/configuration.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
@@ -392,16 +392,16 @@
         """Gets the essential information for debugging.
 
         :return: The report for debugging.
         """
         return "Python SDK Debug Report:\n"\
                "OS: {env}\n"\
                "Python Version: {pyversion}\n"\
-               "Version of the API: 1.9.88\n"\
-               "SDK Package Version: 1.9.88".\
+               "Version of the API: 1.9.92\n"\
+               "SDK Package Version: 1.9.92".\
                format(env=sys.platform, pyversion=sys.version)
 
     def get_host_settings(self):
         """Gets an array of host settings
 
         :return: An array of host settings
         """
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/exceptions.py` & `luminesce-sdk-preview-1.9.92/luminesce/exceptions.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 import six
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/__init__.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 # flake8: noqa
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/access_controlled_action.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/access_controlled_action.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/access_controlled_resource.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/access_controlled_resource.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/access_controlled_resource_identifier_part_schema_attribute.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/access_controlled_resource_identifier_part_schema_attribute.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/action_id.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/action_id.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/background_multi_query_progress_response.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/background_multi_query_progress_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/background_multi_query_response.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/background_multi_query_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/background_query_cancel_response.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/background_query_cancel_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/background_query_progress_response.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/background_query_progress_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/background_query_response.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/background_query_response.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/background_query_state.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/background_query_state.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/column.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/column.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/condition_attributes.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/condition_attributes.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/data_type.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/data_type.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
@@ -29,24 +29,24 @@
     Do not edit the class manually.
     """
 
     """
     allowed enum values
     """
     BOOLEAN = "Boolean"
+    DATE = "Date"
+    DATETIME = "DateTime"
+    DECIMAL = "Decimal"
+    DOUBLE = "Double"
     INT = "Int"
     BIGINT = "BigInt"
-    DOUBLE = "Double"
-    DECIMAL = "Decimal"
     TEXT = "Text"
-    DATE = "Date"
-    DATETIME = "DateTime"
     TABLE = "Table"
 
-    allowable_values = [BOOLEAN, INT, BIGINT, DOUBLE, DECIMAL, TEXT, DATE, DATETIME, TABLE]  # noqa: E501
+    allowable_values = [BOOLEAN, DATE, DATETIME, DECIMAL, DOUBLE, INT, BIGINT, TEXT, TABLE]  # noqa: E501
 
     """
     Attributes:
       openapi_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/feedback_event_args.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/feedback_event_args.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/feedback_level.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/feedback_level.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
@@ -34,21 +34,21 @@
     """
     NONE = "None"
     PROGRESS = "Progress"
     DEBUG = "Debug"
     INFORMATION = "Information"
     WARNING = "Warning"
     ERROR = "Error"
-    EXECUTIONKEEPALIVE = "ExecutionKeepAlive"
-    PROGRESSANDDEBUG = "ProgressAndDebug"
-    PROGRESSANDINFORMATION = "ProgressAndInformation"
-    PROGRESSANDWARNING = "ProgressAndWarning"
     PROGRESSANDERROR = "ProgressAndError"
+    PROGRESSANDWARNING = "ProgressAndWarning"
+    PROGRESSANDINFORMATION = "ProgressAndInformation"
+    PROGRESSANDDEBUG = "ProgressAndDebug"
+    EXECUTIONKEEPALIVE = "ExecutionKeepAlive"
 
-    allowable_values = [NONE, PROGRESS, DEBUG, INFORMATION, WARNING, ERROR, EXECUTIONKEEPALIVE, PROGRESSANDDEBUG, PROGRESSANDINFORMATION, PROGRESSANDWARNING, PROGRESSANDERROR]  # noqa: E501
+    allowable_values = [NONE, PROGRESS, DEBUG, INFORMATION, WARNING, ERROR, PROGRESSANDERROR, PROGRESSANDWARNING, PROGRESSANDINFORMATION, PROGRESSANDDEBUG, EXECUTIONKEEPALIVE]  # noqa: E501
 
     """
     Attributes:
       openapi_types (dict): The key is attribute name
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/id_selector_definition.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/id_selector_definition.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/link.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/link.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/lusid_problem_details.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/lusid_problem_details.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/multi_query_definition_type.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/multi_query_definition_type.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/resource_list_of_access_controlled_resource.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/resource_list_of_access_controlled_resource.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/models/task_status.py` & `luminesce-sdk-preview-1.9.92/luminesce/models/task_status.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 try:
     from inspect import getfullargspec
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/rest.py` & `luminesce-sdk-preview-1.9.92/luminesce/rest.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # coding: utf-8
 
 """
     FINBOURNE Honeycomb Web API
 
     FINBOURNE Technology  # noqa: E501
 
-    The version of the OpenAPI document: 1.9.88
+    The version of the OpenAPI document: 1.9.92
     Contact: info@finbourne.com
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
```

### Comparing `luminesce-sdk-preview-1.9.88/luminesce/utilities/config_keys.json` & `luminesce-sdk-preview-1.9.92/luminesce/utilities/config_keys.json`

 * *Files identical despite different names*

### Comparing `luminesce-sdk-preview-1.9.88/luminesce_sdk_preview.egg-info/SOURCES.txt` & `luminesce-sdk-preview-1.9.92/luminesce_sdk_preview.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `luminesce-sdk-preview-1.9.88/setup.py` & `luminesce-sdk-preview-1.9.92/setup.py`

 * *Files identical despite different names*

