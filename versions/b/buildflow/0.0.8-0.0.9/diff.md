# Comparing `tmp/buildflow-0.0.8.tar.gz` & `tmp/buildflow-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "buildflow-0.0.8.tar", last modified: Thu Mar 16 16:04:06 2023, max compression
+gzip compressed data, was "buildflow-0.0.9.tar", last modified: Thu Mar 16 21:11:25 2023, max compression
```

## Comparing `buildflow-0.0.8.tar` & `buildflow-0.0.9.tar`

### file list

```diff
@@ -1,79 +1,79 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.139634 buildflow-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    10494 2023-03-16 16:03:53.000000 buildflow-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-16 16:04:06.139634 buildflow-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-03-16 16:03:53.000000 buildflow-0.0.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.131633 buildflow-0.0.8/buildflow/
--rw-r--r--   0 runner    (1001) docker     (123)      644 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.131633 buildflow-0.0.8/buildflow/api/
--rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.135634 buildflow-0.0.8/buildflow/api/_vision/
--rw-r--r--   0 runner    (1001) docker     (123)      880 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/_vision/process_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)      839 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/_vision/process_endpoint.py
--rw-r--r--   0 runner    (1001) docker     (123)      627 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/_vision/process_stream.py
--rw-r--r--   0 runner    (1001) docker     (123)     1683 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/_vision/processor_templates.py
--rw-r--r--   0 runner    (1001) docker     (123)      751 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/_vision/templates.py
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/flow.py
--rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/io.py
--rw-r--r--   0 runner    (1001) docker     (123)     1032 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/api/processor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.135634 buildflow-0.0.8/buildflow/migration/
--rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/migration/beam_migrator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.135634 buildflow-0.0.8/buildflow/runtime/
--rw-r--r--   0 runner    (1001) docker     (123)       87 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/flow.py
--rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/processor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.135634 buildflow-0.0.8/buildflow/runtime/ray_io/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4520 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    18777 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/bigquery_io.py
--rw-r--r--   0 runner    (1001) docker     (123)    11464 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/bigquery_io_test.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)     3416 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/duckdb_io.py
--rw-r--r--   0 runner    (1001) docker     (123)      500 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/duckdb_io_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/empty_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     1996 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/empty_io_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1973 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/file_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     1644 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/file_io_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     5866 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/gcs_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     4166 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/gcs_io_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     4757 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/pubsub_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     3473 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/pubsub_io_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/pubsub_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3904 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/redis_stream_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     4801 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/redis_stream_io_test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.135634 buildflow-0.0.8/buildflow/runtime/ray_io/schemas/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/schemas/bigquery.py
--rw-r--r--   0 runner    (1001) docker     (123)     4911 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/ray_io/schemas/bigquery_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     7314 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/runner.py
--rw-r--r--   0 runner    (1001) docker     (123)     2322 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/runtime/tracer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.139634 buildflow-0.0.8/buildflow/samples/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/bigquery_sample.py
--rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/class_sample.py
--rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/csv_bigquery_walkthrough.py
--rw-r--r--   0 runner    (1001) docker     (123)      746 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/decorator_sample.py
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/local_pubsub_publish.py
--rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/local_pubsub_walkthrough.py
--rw-r--r--   0 runner    (1001) docker     (123)     1381 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/samples/pubsub_walkthrough.py
--rw-r--r--   0 runner    (1001) docker     (123)      988 2023-03-16 16:03:53.000000 buildflow-0.0.8/buildflow/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.131633 buildflow-0.0.8/buildflow.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-16 16:04:06.000000 buildflow-0.0.8/buildflow.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2422 2023-03-16 16:04:06.000000 buildflow-0.0.8/buildflow.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 16:04:06.000000 buildflow-0.0.8/buildflow.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      298 2023-03-16 16:04:06.000000 buildflow-0.0.8/buildflow.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-03-16 16:04:06.000000 buildflow-0.0.8/buildflow.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.131633 buildflow-0.0.8/integration_tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.139634 buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/
--rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/pubsub_main.py
--rw-r--r--   0 runner    (1001) docker     (123)      605 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/pubsub_publish.py
--rw-r--r--   0 runner    (1001) docker     (123)      854 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/pubsub_validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.139634 buildflow-0.0.8/integration_tests/pubsub_to_pubsub/
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_pubsub/pubsub_main.py
--rw-r--r--   0 runner    (1001) docker     (123)     1401 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_pubsub/pubsub_publish.py
--rw-r--r--   0 runner    (1001) docker     (123)      999 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_pubsub/pubsub_validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 16:04:06.139634 buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/
--rw-r--r--   0 runner    (1001) docker     (123)      590 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/pubsub_main.py
--rw-r--r--   0 runner    (1001) docker     (123)     1435 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/pubsub_publish.py
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-03-16 16:03:53.000000 buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/pubsub_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1354 2023-03-16 16:03:53.000000 buildflow-0.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-16 16:04:06.139634 buildflow-0.0.8/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.690326 buildflow-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    10494 2023-03-16 21:11:13.000000 buildflow-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-16 21:11:25.690326 buildflow-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2391 2023-03-16 21:11:13.000000 buildflow-0.0.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.678326 buildflow-0.0.9/buildflow/
+-rw-r--r--   0 runner    (1001) docker     (123)      644 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.678326 buildflow-0.0.9/buildflow/api/
+-rw-r--r--   0 runner    (1001) docker     (123)      199 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.682325 buildflow-0.0.9/buildflow/api/_vision/
+-rw-r--r--   0 runner    (1001) docker     (123)      880 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/_vision/process_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      839 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/_vision/process_endpoint.py
+-rw-r--r--   0 runner    (1001) docker     (123)      627 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/_vision/process_stream.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1683 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/_vision/processor_templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/_vision/templates.py
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/flow.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1032 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/api/processor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.682325 buildflow-0.0.9/buildflow/migration/
+-rw-r--r--   0 runner    (1001) docker     (123)      197 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/migration/beam_migrator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.682325 buildflow-0.0.9/buildflow/runtime/
+-rw-r--r--   0 runner    (1001) docker     (123)       87 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/flow.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2033 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/processor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.686326 buildflow-0.0.9/buildflow/runtime/ray_io/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4520 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18777 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/bigquery_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11464 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/bigquery_io_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3416 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/duckdb_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/duckdb_io_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/empty_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1996 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/empty_io_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1973 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/file_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1644 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/file_io_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5866 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/gcs_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4166 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/gcs_io_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4757 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/pubsub_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3473 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/pubsub_io_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/pubsub_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3904 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/redis_stream_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4801 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/redis_stream_io_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.686326 buildflow-0.0.9/buildflow/runtime/ray_io/schemas/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2453 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/schemas/bigquery.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4911 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/ray_io/schemas/bigquery_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7314 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/runner.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2322 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/runtime/tracer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.690326 buildflow-0.0.9/buildflow/samples/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1292 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/bigquery_sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/class_sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/csv_bigquery_walkthrough.py
+-rw-r--r--   0 runner    (1001) docker     (123)      746 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/decorator_sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/local_pubsub_publish.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1406 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/local_pubsub_walkthrough.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/samples/pubsub_walkthrough.py
+-rw-r--r--   0 runner    (1001) docker     (123)      988 2023-03-16 21:11:13.000000 buildflow-0.0.9/buildflow/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.678326 buildflow-0.0.9/buildflow.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3011 2023-03-16 21:11:25.000000 buildflow-0.0.9/buildflow.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2422 2023-03-16 21:11:25.000000 buildflow-0.0.9/buildflow.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 21:11:25.000000 buildflow-0.0.9/buildflow.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      298 2023-03-16 21:11:25.000000 buildflow-0.0.9/buildflow.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-03-16 21:11:25.000000 buildflow-0.0.9/buildflow.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.678326 buildflow-0.0.9/integration_tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.690326 buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/
+-rw-r--r--   0 runner    (1001) docker     (123)      840 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/pubsub_main.py
+-rw-r--r--   0 runner    (1001) docker     (123)      605 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/pubsub_publish.py
+-rw-r--r--   0 runner    (1001) docker     (123)      854 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/pubsub_validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.690326 buildflow-0.0.9/integration_tests/pubsub_to_pubsub/
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_pubsub/pubsub_main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1401 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_pubsub/pubsub_publish.py
+-rw-r--r--   0 runner    (1001) docker     (123)      999 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_pubsub/pubsub_validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 21:11:25.690326 buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/
+-rw-r--r--   0 runner    (1001) docker     (123)      590 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/pubsub_main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1435 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/pubsub_publish.py
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-03-16 21:11:13.000000 buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/pubsub_validation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1354 2023-03-16 21:11:13.000000 buildflow-0.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-16 21:11:25.690326 buildflow-0.0.9/setup.cfg
```

### Comparing `buildflow-0.0.8/LICENSE` & `buildflow-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/PKG-INFO` & `buildflow-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: buildflow
-Version: 0.0.8
+Version: 0.0.9
 Summary: buildflow is a unified **batch** and **streaming** framework that turns any python function into a scalable data pipeline that can read from our supported IO resources.
 Author-email: Caleb Van Dyke <caleb@launchflow.com>, Josh Tanke <josh@launchflow.com>
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.7
```

### Comparing `buildflow-0.0.8/README.md` & `buildflow-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/__init__.py` & `buildflow-0.0.9/buildflow/__init__.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/_vision/process_batch.py` & `buildflow-0.0.9/buildflow/api/_vision/process_batch.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/_vision/process_endpoint.py` & `buildflow-0.0.9/buildflow/api/_vision/process_endpoint.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/_vision/process_stream.py` & `buildflow-0.0.9/buildflow/api/_vision/process_stream.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/_vision/processor_templates.py` & `buildflow-0.0.9/buildflow/api/_vision/processor_templates.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/_vision/templates.py` & `buildflow-0.0.9/buildflow/api/_vision/templates.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/io.py` & `buildflow-0.0.9/buildflow/api/io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/api/processor.py` & `buildflow-0.0.9/buildflow/api/processor.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/flow.py` & `buildflow-0.0.9/buildflow/runtime/flow.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/processor.py` & `buildflow-0.0.9/buildflow/runtime/processor.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/base.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/base.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/bigquery_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/bigquery_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/bigquery_io_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/bigquery_io_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/duckdb_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/duckdb_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/empty_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/empty_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/empty_io_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/empty_io_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/file_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/file_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/file_io_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/file_io_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/gcs_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/gcs_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/gcs_io_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/gcs_io_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/pubsub_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/pubsub_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/pubsub_io_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/pubsub_io_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/pubsub_utils.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/pubsub_utils.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/redis_stream_io.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/redis_stream_io.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/redis_stream_io_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/redis_stream_io_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/schemas/bigquery.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/schemas/bigquery.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/ray_io/schemas/bigquery_test.py` & `buildflow-0.0.9/buildflow/runtime/ray_io/schemas/bigquery_test.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/runner.py` & `buildflow-0.0.9/buildflow/runtime/runner.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/runtime/tracer.py` & `buildflow-0.0.9/buildflow/runtime/tracer.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/bigquery_sample.py` & `buildflow-0.0.9/buildflow/samples/bigquery_sample.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/class_sample.py` & `buildflow-0.0.9/buildflow/samples/class_sample.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/csv_bigquery_walkthrough.py` & `buildflow-0.0.9/buildflow/samples/csv_bigquery_walkthrough.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/decorator_sample.py` & `buildflow-0.0.9/buildflow/samples/decorator_sample.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/local_pubsub_publish.py` & `buildflow-0.0.9/buildflow/samples/local_pubsub_publish.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/local_pubsub_walkthrough.py` & `buildflow-0.0.9/buildflow/samples/local_pubsub_walkthrough.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow/samples/pubsub_walkthrough.py` & `buildflow-0.0.9/buildflow/samples/pubsub_walkthrough.py`

 * *Files 5% similar despite different names*

```diff
@@ -12,15 +12,16 @@
 parser = argparse.ArgumentParser()
 parser.add_argument('--gcp_project', type=str, required=True)
 args, _ = parser.parse_known_args(sys.argv)
 
 # Set up a subscriber for the source.
 # If this subscriber does not exist yet BuildFlow will create it.
 input_sub = buildflow.PubSubSource(
-    subscription=f'projects/{args.gcp_project}/subscriptions/taxiride-sub')
+    subscription=f'projects/{args.gcp_project}/subscriptions/taxiride-sub',
+    topic='projects/pubsub-public-data/topics/taxirides-realtime')
 # Set up a BigQuery table for the sink.
 # If this table does not exist yet BuildFlow will create it.
 output_table = buildflow.BigQuerySink(
     table_id=f'{args.gcp_project}.buildflow_walkthrough.taxi_ride_data')
 
 
 # Define an output type for our pipeline.
```

### Comparing `buildflow-0.0.8/buildflow/utils.py` & `buildflow-0.0.9/buildflow/utils.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/buildflow.egg-info/PKG-INFO` & `buildflow-0.0.9/buildflow.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: buildflow
-Version: 0.0.8
+Version: 0.0.9
 Summary: buildflow is a unified **batch** and **streaming** framework that turns any python function into a scalable data pipeline that can read from our supported IO resources.
 Author-email: Caleb Van Dyke <caleb@launchflow.com>, Josh Tanke <josh@launchflow.com>
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Software Development
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.7
```

### Comparing `buildflow-0.0.8/buildflow.egg-info/SOURCES.txt` & `buildflow-0.0.9/buildflow.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/pubsub_main.py` & `buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/pubsub_main.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/pubsub_publish.py` & `buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/pubsub_publish.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_local_parquet/pubsub_validation.py` & `buildflow-0.0.9/integration_tests/pubsub_to_local_parquet/pubsub_validation.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_pubsub/pubsub_main.py` & `buildflow-0.0.9/integration_tests/pubsub_to_pubsub/pubsub_main.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_pubsub/pubsub_publish.py` & `buildflow-0.0.9/integration_tests/pubsub_to_pubsub/pubsub_publish.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_pubsub/pubsub_validation.py` & `buildflow-0.0.9/integration_tests/pubsub_to_pubsub/pubsub_validation.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/pubsub_main.py` & `buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/pubsub_main.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/pubsub_publish.py` & `buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/pubsub_publish.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/integration_tests/pubsub_to_pubsub_multi_output/pubsub_validation.py` & `buildflow-0.0.9/integration_tests/pubsub_to_pubsub_multi_output/pubsub_validation.py`

 * *Files identical despite different names*

### Comparing `buildflow-0.0.8/pyproject.toml` & `buildflow-0.0.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=64.0.0", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "buildflow"
-version = "0.0.8"
+version = "0.0.9"
 authors = [
     { name = "Caleb Van Dyke", email = "caleb@launchflow.com" },
     { name = "Josh Tanke", email = "josh@launchflow.com" },
 ]
 description = "buildflow is a unified **batch** and **streaming** framework that turns any python function into a scalable data pipeline that can read from our supported IO resources."
 readme = "README.md"
 requires-python = ">=3.7"
```

