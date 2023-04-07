# Comparing `tmp/wds-client-0.2.7.tar.gz` & `tmp/wds-client-0.2.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/terra-workspace-data-service/terra-workspace-data-service/wds-client/dist/tmpsy38g879/wds-client-0.2.7.tar", last modified: Tue Nov 22 18:05:31 2022, max compression
+gzip compressed data, was "/home/runner/work/terra-workspace-data-service/terra-workspace-data-service/wds-client/dist/.tmp-v6dee5fu/wds-client-0.2.8.tar", last modified: Tue Nov 29 15:21:47 2022, max compression
```

## Comparing `wds-client-0.2.7.tar` & `wds-client-0.2.8.tar`

### file list

```diff
@@ -1,64 +1,64 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-22 18:05:31.000000 wds-client-0.2.7/
--rw-r--r--   0 runner    (1001) docker     (121)      689 2022-11-22 18:05:31.000000 wds-client-0.2.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     6604 2022-11-22 18:05:23.000000 wds-client-0.2.7/README.md
--rw-r--r--   0 runner    (1001) docker     (121)       69 2022-11-22 18:05:31.000000 wds-client-0.2.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1776 2022-11-22 18:05:23.000000 wds-client-0.2.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-22 18:05:31.000000 wds-client-0.2.7/test/
--rw-r--r--   0 runner    (1001) docker     (121)     1869 2022-11-22 18:05:22.000000 wds-client-0.2.7/test/test_attribute_schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     2773 2022-11-22 18:05:22.000000 wds-client-0.2.7/test/test_batch_operation.py
--rw-r--r--   0 runner    (1001) docker     (121)     2542 2022-11-22 18:05:22.000000 wds-client-0.2.7/test/test_batch_record_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     1820 2022-11-22 18:05:22.000000 wds-client-0.2.7/test/test_batch_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     1983 2022-11-22 18:05:22.000000 wds-client-0.2.7/test/test_error_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     1701 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_general_wds_information_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1752 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_inline_object.py
--rw-r--r--   0 runner    (1001) docker     (121)     1352 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_instances_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1869 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_record_attribute_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     3375 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_record_query_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     2375 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_record_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     2496 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_record_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     2336 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_record_type_schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     2232 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_records_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1818 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_request_body_search.py
--rw-r--r--   0 runner    (1001) docker     (121)     2140 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_schema_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     1691 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_search_operator.py
--rw-r--r--   0 runner    (1001) docker     (121)     1805 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_search_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     1748 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_search_sort_direction.py
--rw-r--r--   0 runner    (1001) docker     (121)     2000 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_stack_trace_element.py
--rw-r--r--   0 runner    (1001) docker     (121)     1866 2022-11-22 18:05:23.000000 wds-client-0.2.7/test/test_tsv_upload_response.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client/
--rw-r--r--   0 runner    (1001) docker     (121)     2429 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client/api/
--rw-r--r--   0 runner    (1001) docker     (121)      319 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9623 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/api/general_wds_information_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    12814 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/api/instances_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    61202 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/api/records_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    49447 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/api/schema_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    26549 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/api_client.py
--rw-r--r--   0 runner    (1001) docker     (121)    12775 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/configuration.py
--rw-r--r--   0 runner    (1001) docker     (121)     4114 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client/models/
--rw-r--r--   0 runner    (1001) docker     (121)     1789 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6580 2022-11-22 18:05:22.000000 wds-client-0.2.7/wds_client/models/attribute_schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     5040 2022-11-22 18:05:22.000000 wds-client-0.2.7/wds_client/models/batch_operation.py
--rw-r--r--   0 runner    (1001) docker     (121)     5419 2022-11-22 18:05:22.000000 wds-client-0.2.7/wds_client/models/batch_record_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     4792 2022-11-22 18:05:22.000000 wds-client-0.2.7/wds_client/models/batch_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     7280 2022-11-22 18:05:22.000000 wds-client-0.2.7/wds_client/models/error_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     3893 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/inline_object.py
--rw-r--r--   0 runner    (1001) docker     (121)     3913 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/record_attribute_definition.py
--rw-r--r--   0 runner    (1001) docker     (121)     6056 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/record_query_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     3911 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/record_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     5355 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/record_response.py
--rw-r--r--   0 runner    (1001) docker     (121)     5858 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/record_type_schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     4648 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/request_body_search.py
--rw-r--r--   0 runner    (1001) docker     (121)     3131 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/search_operator.py
--rw-r--r--   0 runner    (1001) docker     (121)     6551 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/search_request.py
--rw-r--r--   0 runner    (1001) docker     (121)     3157 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/search_sort_direction.py
--rw-r--r--   0 runner    (1001) docker     (121)     6829 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/stack_trace_element.py
--rw-r--r--   0 runner    (1001) docker     (121)     4840 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/models/tsv_upload_response.py
--rw-r--r--   0 runner    (1001) docker     (121)    12642 2022-11-22 18:05:23.000000 wds-client-0.2.7/wds_client/rest.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)      689 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1828 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       48 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       11 2022-11-22 18:05:31.000000 wds-client-0.2.7/wds_client.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-29 15:21:47.000000 wds-client-0.2.8/
+-rw-r--r--   0 runner    (1001) docker     (122)      689 2022-11-29 15:21:47.000000 wds-client-0.2.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     6604 2022-11-29 15:21:34.000000 wds-client-0.2.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)       69 2022-11-29 15:21:47.000000 wds-client-0.2.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1776 2022-11-29 15:21:35.000000 wds-client-0.2.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-29 15:21:47.000000 wds-client-0.2.8/test/
+-rw-r--r--   0 runner    (1001) docker     (122)     1869 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_attribute_schema.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2773 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_batch_operation.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2542 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_batch_record_request.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1820 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_batch_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1983 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_error_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1701 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_general_wds_information_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1752 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_inline_object.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1352 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_instances_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1869 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_record_attribute_definition.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3375 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_record_query_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2375 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_record_request.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2496 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_record_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2407 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_record_type_schema.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2232 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_records_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1818 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_request_body_search.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2140 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_schema_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1691 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_search_operator.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1805 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_search_request.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1748 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_search_sort_direction.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2000 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_stack_trace_element.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1866 2022-11-29 15:21:34.000000 wds-client-0.2.8/test/test_tsv_upload_response.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-29 15:21:47.000000 wds-client-0.2.8/wds_client/
+-rw-r--r--   0 runner    (1001) docker     (122)     2429 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-29 15:21:47.000000 wds-client-0.2.8/wds_client/api/
+-rw-r--r--   0 runner    (1001) docker     (122)      319 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9623 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/api/general_wds_information_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12814 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/api/instances_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)    61202 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/api/records_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)    49447 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/api/schema_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)    26549 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/api_client.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12775 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/configuration.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4114 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-29 15:21:47.000000 wds-client-0.2.8/wds_client/models/
+-rw-r--r--   0 runner    (1001) docker     (122)     1789 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6580 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/attribute_schema.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5040 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/batch_operation.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5419 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/batch_record_request.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4792 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/batch_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7280 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/error_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3893 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/inline_object.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3913 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/record_attribute_definition.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6056 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/record_query_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3911 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/record_request.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5355 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/record_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7055 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/record_type_schema.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4648 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/request_body_search.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3131 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/search_operator.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6551 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/search_request.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3157 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/search_sort_direction.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6829 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/stack_trace_element.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4840 2022-11-29 15:21:34.000000 wds-client-0.2.8/wds_client/models/tsv_upload_response.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12642 2022-11-29 15:21:35.000000 wds-client-0.2.8/wds_client/rest.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-29 15:21:47.000000 wds-client-0.2.8/wds_client.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)      689 2022-11-29 15:21:46.000000 wds-client-0.2.8/wds_client.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1828 2022-11-29 15:21:46.000000 wds-client-0.2.8/wds_client.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2022-11-29 15:21:46.000000 wds-client-0.2.8/wds_client.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       48 2022-11-29 15:21:46.000000 wds-client-0.2.8/wds_client.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       11 2022-11-29 15:21:46.000000 wds-client-0.2.8/wds_client.egg-info/top_level.txt
```

### Comparing `wds-client-0.2.7/PKG-INFO` & `wds-client-0.2.8/PKG-INFO`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wds-client
-Version: 0.2.7
+Version: 0.2.8
 Summary: Workspace Data Service
 Home-page: 
 Author: OpenAPI Generator community
 Author-email: team@openapitools.org
 License: BSD
 Keywords: OpenAPI,OpenAPI-Generator,Workspace Data Service
```

### Comparing `wds-client-0.2.7/README.md` & `wds-client-0.2.8/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 
 As of v0.2, all APIs are subject to change without notice.
 
 
 This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:
 
 - API version: v0.2
-- Package version: 0.2.7
+- Package version: 0.2.8
 - Build package: org.openapitools.codegen.languages.PythonClientCodegen
 
 ## Requirements.
 
 Python 2.7 and 3.4+
 
 ## Installation & Usage
```

### Comparing `wds-client-0.2.7/setup.py` & `wds-client-0.2.8/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,15 +9,15 @@
     Generated by: https://openapi-generator.tech
 """
 
 
 from setuptools import setup, find_packages  # noqa: H301
 
 NAME = "wds-client"
-VERSION = "0.2.7"
+VERSION = "0.2.8"
 # To install the library, run the following
 #
 # python setup.py install
 #
 # prerequisite: setuptools
 # http://pypi.python.org/pypi/setuptools
```

### Comparing `wds-client-0.2.7/test/test_attribute_schema.py` & `wds-client-0.2.8/test/test_attribute_schema.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_batch_operation.py` & `wds-client-0.2.8/test/test_batch_operation.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_batch_record_request.py` & `wds-client-0.2.8/test/test_batch_record_request.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_batch_response.py` & `wds-client-0.2.8/test/test_batch_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_error_response.py` & `wds-client-0.2.8/test/test_error_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_general_wds_information_api.py` & `wds-client-0.2.8/test/test_general_wds_information_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_inline_object.py` & `wds-client-0.2.8/test/test_inline_object.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_instances_api.py` & `wds-client-0.2.8/test/test_instances_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_record_attribute_definition.py` & `wds-client-0.2.8/test/test_record_attribute_definition.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_record_query_response.py` & `wds-client-0.2.8/test/test_record_query_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_record_request.py` & `wds-client-0.2.8/test/test_record_request.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_record_response.py` & `wds-client-0.2.8/test/test_record_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_record_type_schema.py` & `wds-client-0.2.8/test/test_record_type_schema.py`

 * *Files 4% similar despite different names*

```diff
@@ -39,26 +39,28 @@
                 name = '0', 
                 attributes = [
                     wds_client.models.attribute_schema.AttributeSchema(
                         name = '0', 
                         datatype = 'boolean', 
                         relates_to = '0', )
                     ], 
-                count = 56
+                count = 56, 
+                primary_key = '0'
             )
         else :
             return RecordTypeSchema(
                 name = '0',
                 attributes = [
                     wds_client.models.attribute_schema.AttributeSchema(
                         name = '0', 
                         datatype = 'boolean', 
                         relates_to = '0', )
                     ],
                 count = 56,
+                primary_key = '0',
         )
 
     def testRecordTypeSchema(self):
         """Test RecordTypeSchema"""
         inst_req_only = self.make_instance(include_optional=False)
         inst_req_and_optional = self.make_instance(include_optional=True)
```

### Comparing `wds-client-0.2.7/test/test_records_api.py` & `wds-client-0.2.8/test/test_records_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_request_body_search.py` & `wds-client-0.2.8/test/test_request_body_search.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_schema_api.py` & `wds-client-0.2.8/test/test_schema_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_search_operator.py` & `wds-client-0.2.8/test/test_search_operator.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_search_request.py` & `wds-client-0.2.8/test/test_search_request.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_search_sort_direction.py` & `wds-client-0.2.8/test/test_search_sort_direction.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_stack_trace_element.py` & `wds-client-0.2.8/test/test_stack_trace_element.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/test/test_tsv_upload_response.py` & `wds-client-0.2.8/test/test_tsv_upload_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/__init__.py` & `wds-client-0.2.8/wds_client/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     The version of the OpenAPI document: v0.2
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
-__version__ = "0.2.7"
+__version__ = "0.2.8"
 
 # import apis into sdk package
 from wds_client.api.general_wds_information_api import GeneralWDSInformationApi
 from wds_client.api.instances_api import InstancesApi
 from wds_client.api.records_api import RecordsApi
 from wds_client.api.schema_api import SchemaApi
```

### Comparing `wds-client-0.2.7/wds_client/api/general_wds_information_api.py` & `wds-client-0.2.8/wds_client/api/general_wds_information_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/api/instances_api.py` & `wds-client-0.2.8/wds_client/api/instances_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/api/records_api.py` & `wds-client-0.2.8/wds_client/api/records_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/api/schema_api.py` & `wds-client-0.2.8/wds_client/api/schema_api.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/api_client.py` & `wds-client-0.2.8/wds_client/api_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -74,15 +74,15 @@
 
         self.rest_client = rest.RESTClientObject(configuration)
         self.default_headers = {}
         if header_name is not None:
             self.default_headers[header_name] = header_value
         self.cookie = cookie
         # Set default User-Agent.
-        self.user_agent = 'OpenAPI-Generator/0.2.7/python'
+        self.user_agent = 'OpenAPI-Generator/0.2.8/python'
         self.client_side_validation = configuration.client_side_validation
 
     def __enter__(self):
         return self
 
     def __exit__(self, exc_type, exc_value, traceback):
         self.close()
```

### Comparing `wds-client-0.2.7/wds_client/configuration.py` & `wds-client-0.2.8/wds_client/configuration.py`

 * *Files 0% similar despite different names*

```diff
@@ -321,15 +321,15 @@
 
         :return: The report for debugging.
         """
         return "Python SDK Debug Report:\n"\
                "OS: {env}\n"\
                "Python Version: {pyversion}\n"\
                "Version of the API: v0.2\n"\
-               "SDK Package Version: 0.2.7".\
+               "SDK Package Version: 0.2.8".\
                format(env=sys.platform, pyversion=sys.version)
 
     def get_host_settings(self):
         """Gets an array of host settings
 
         :return: An array of host settings
         """
```

### Comparing `wds-client-0.2.7/wds_client/exceptions.py` & `wds-client-0.2.8/wds_client/exceptions.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/__init__.py` & `wds-client-0.2.8/wds_client/models/__init__.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/attribute_schema.py` & `wds-client-0.2.8/wds_client/models/attribute_schema.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/batch_operation.py` & `wds-client-0.2.8/wds_client/models/batch_operation.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/batch_record_request.py` & `wds-client-0.2.8/wds_client/models/batch_record_request.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/batch_response.py` & `wds-client-0.2.8/wds_client/models/batch_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/error_response.py` & `wds-client-0.2.8/wds_client/models/error_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/inline_object.py` & `wds-client-0.2.8/wds_client/models/inline_object.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/record_attribute_definition.py` & `wds-client-0.2.8/wds_client/models/record_attribute_definition.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/record_query_response.py` & `wds-client-0.2.8/wds_client/models/record_query_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/record_request.py` & `wds-client-0.2.8/wds_client/models/record_request.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/record_response.py` & `wds-client-0.2.8/wds_client/models/record_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/record_type_schema.py` & `wds-client-0.2.8/wds_client/models/record_type_schema.py`

 * *Files 13% similar despite different names*

```diff
@@ -31,37 +31,41 @@
                             and the value is attribute type.
       attribute_map (dict): The key is attribute name
                             and the value is json key in definition.
     """
     openapi_types = {
         'name': 'str',
         'attributes': 'list[AttributeSchema]',
-        'count': 'int'
+        'count': 'int',
+        'primary_key': 'str'
     }
 
     attribute_map = {
         'name': 'name',
         'attributes': 'attributes',
-        'count': 'count'
+        'count': 'count',
+        'primary_key': 'primaryKey'
     }
 
-    def __init__(self, name=None, attributes=None, count=None, local_vars_configuration=None):  # noqa: E501
+    def __init__(self, name=None, attributes=None, count=None, primary_key=None, local_vars_configuration=None):  # noqa: E501
         """RecordTypeSchema - a model defined in OpenAPI"""  # noqa: E501
         if local_vars_configuration is None:
             local_vars_configuration = Configuration()
         self.local_vars_configuration = local_vars_configuration
 
         self._name = None
         self._attributes = None
         self._count = None
+        self._primary_key = None
         self.discriminator = None
 
         self.name = name
         self.attributes = attributes
         self.count = count
+        self.primary_key = primary_key
 
     @property
     def name(self):
         """Gets the name of this RecordTypeSchema.  # noqa: E501
 
         Record type name, valid characters for record type names are limited to letters, numbers, spaces, dashes, and underscores.  # noqa: E501
 
@@ -128,14 +132,39 @@
         :type: int
         """
         if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
             raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501
 
         self._count = count
 
+    @property
+    def primary_key(self):
+        """Gets the primary_key of this RecordTypeSchema.  # noqa: E501
+
+        Attribute name that contains the value to uniquely identify each record, defined as a primary key column in the underlying table.  # noqa: E501
+
+        :return: The primary_key of this RecordTypeSchema.  # noqa: E501
+        :rtype: str
+        """
+        return self._primary_key
+
+    @primary_key.setter
+    def primary_key(self, primary_key):
+        """Sets the primary_key of this RecordTypeSchema.
+
+        Attribute name that contains the value to uniquely identify each record, defined as a primary key column in the underlying table.  # noqa: E501
+
+        :param primary_key: The primary_key of this RecordTypeSchema.  # noqa: E501
+        :type: str
+        """
+        if self.local_vars_configuration.client_side_validation and primary_key is None:  # noqa: E501
+            raise ValueError("Invalid value for `primary_key`, must not be `None`")  # noqa: E501
+
+        self._primary_key = primary_key
+
     def to_dict(self):
         """Returns the model properties as a dict"""
         result = {}
 
         for attr, _ in six.iteritems(self.openapi_types):
             value = getattr(self, attr)
             if isinstance(value, list):
```

### Comparing `wds-client-0.2.7/wds_client/models/request_body_search.py` & `wds-client-0.2.8/wds_client/models/request_body_search.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/search_operator.py` & `wds-client-0.2.8/wds_client/models/search_operator.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/search_request.py` & `wds-client-0.2.8/wds_client/models/search_request.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/search_sort_direction.py` & `wds-client-0.2.8/wds_client/models/search_sort_direction.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/stack_trace_element.py` & `wds-client-0.2.8/wds_client/models/stack_trace_element.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/models/tsv_upload_response.py` & `wds-client-0.2.8/wds_client/models/tsv_upload_response.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client/rest.py` & `wds-client-0.2.8/wds_client/rest.py`

 * *Files identical despite different names*

### Comparing `wds-client-0.2.7/wds_client.egg-info/PKG-INFO` & `wds-client-0.2.8/wds_client.egg-info/PKG-INFO`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: wds-client
-Version: 0.2.7
+Version: 0.2.8
 Summary: Workspace Data Service
 Home-page: 
 Author: OpenAPI Generator community
 Author-email: team@openapitools.org
 License: BSD
 Keywords: OpenAPI,OpenAPI-Generator,Workspace Data Service
```

### Comparing `wds-client-0.2.7/wds_client.egg-info/SOURCES.txt` & `wds-client-0.2.8/wds_client.egg-info/SOURCES.txt`

 * *Files identical despite different names*

