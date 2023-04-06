# Comparing `tmp/apache-airflow-providers-google-8.9.0.tar.gz` & `tmp/apache-airflow-providers-google-8.9.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-google-8.9.0.tar", last modified: Wed Feb  8 07:59:52 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-google-8.9.0rc1.tar", last modified: Wed Feb  8 08:28:17 2023, max compression
```

## Comparing `apache-airflow-providers-google-8.9.0.tar` & `apache-airflow-providers-google-8.9.0rc1.tar`

### file list

```diff
@@ -1,345 +1,345 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/
--rw-r--r--   0 root         (0) root         (0)    10850 2022-10-05 12:15:16.000000 apache-airflow-providers-google-8.9.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1240 2023-02-08 07:59:43.000000 apache-airflow-providers-google-8.9.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2022-10-05 12:15:16.000000 apache-airflow-providers-google-8.9.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    70436 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    68453 2023-02-08 07:59:43.000000 apache-airflow-providers-google-8.9.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/
--rw-r--r--   0 root         (0) root         (0)     1578 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    11312 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/hooks/ads.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/operators/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4743 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/operators/ads.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/transfers/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/transfers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5228 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/transfers/ads_to_gcs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/_internal_client/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/_internal_client/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3730 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/_internal_client/secret_manager_client.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3574 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_nl_text_classification.py
--rw-r--r--   0 root         (0) root         (0)     3666 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_nl_text_sentiment.py
--rw-r--r--   0 root         (0) root         (0)     3726 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_translation.py
--rw-r--r--   0 root         (0) root         (0)     3666 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_classification.py
--rw-r--r--   0 root         (0) root         (0)     3719 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_tracking.py
--rw-r--r--   0 root         (0) root         (0)     3693 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_vision_object_detection.py
--rw-r--r--   0 root         (0) root         (0)    10890 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_cloud_sql_query.py
--rw-r--r--   0 root         (0) root         (0)     7927 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_cloud_storage_transfer_service_aws.py
--rw-r--r--   0 root         (0) root         (0)     1896 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_cloud_task.py
--rw-r--r--   0 root         (0) root         (0)     4274 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_compute.py
--rw-r--r--   0 root         (0) root         (0)     3165 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_compute_ssh.py
--rw-r--r--   0 root         (0) root         (0)    10681 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_dataflow.py
--rw-r--r--   0 root         (0) root         (0)     2801 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_dataflow_flex_template.py
--rw-r--r--   0 root         (0) root         (0)     2586 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_dataflow_sql.py
--rw-r--r--   0 root         (0) root         (0)     4823 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_facebook_ads_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     2320 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_looker.py
--rw-r--r--   0 root         (0) root         (0)     1785 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_postgres_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     7363 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_presto_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     4891 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_salesforce_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)    28718 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_vertex_ai.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:50.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    27055 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/automl.py
--rw-r--r--   0 root         (0) root         (0)   136373 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/bigquery.py
--rw-r--r--   0 root         (0) root         (0)    14391 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/bigquery_dts.py
--rw-r--r--   0 root         (0) root         (0)    12410 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/bigtable.py
--rw-r--r--   0 root         (0) root         (0)    25856 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_build.py
--rw-r--r--   0 root         (0) root         (0)    17570 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_composer.py
--rw-r--r--   0 root         (0) root         (0)    40873 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_memorystore.py
--rw-r--r--   0 root         (0) root         (0)    42574 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_sql.py
--rw-r--r--   0 root         (0) root         (0)    19106 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_storage_transfer_service.py
--rw-r--r--   0 root         (0) root         (0)    39903 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/compute.py
--rw-r--r--   0 root         (0) root         (0)    12939 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/compute_ssh.py
--rw-r--r--   0 root         (0) root         (0)    54442 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/datacatalog.py
--rw-r--r--   0 root         (0) root         (0)    49406 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataflow.py
--rw-r--r--   0 root         (0) root         (0)    24996 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataform.py
--rw-r--r--   0 root         (0) root         (0)    22363 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/datafusion.py
--rw-r--r--   0 root         (0) root         (0)    15517 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataplex.py
--rw-r--r--   0 root         (0) root         (0)     8214 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataprep.py
--rw-r--r--   0 root         (0) root         (0)    76786 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataproc.py
--rw-r--r--   0 root         (0) root         (0)    29423 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataproc_metastore.py
--rw-r--r--   0 root         (0) root         (0)    12124 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/datastore.py
--rw-r--r--   0 root         (0) root         (0)    64796 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dlp.py
--rw-r--r--   0 root         (0) root         (0)     9389 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/functions.py
--rw-r--r--   0 root         (0) root         (0)    49610 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/gcs.py
--rw-r--r--   0 root         (0) root         (0)     4061 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/gdm.py
--rw-r--r--   0 root         (0) root         (0)     6717 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/kms.py
--rw-r--r--   0 root         (0) root         (0)    11423 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/kubernetes_engine.py
--rw-r--r--   0 root         (0) root         (0)     6245 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/life_sciences.py
--rw-r--r--   0 root         (0) root         (0)     8902 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/looker.py
--rw-r--r--   0 root         (0) root         (0)    24449 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/mlengine.py
--rw-r--r--   0 root         (0) root         (0)    11233 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/natural_language.py
--rw-r--r--   0 root         (0) root         (0)     3986 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/os_login.py
--rw-r--r--   0 root         (0) root         (0)    26808 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/pubsub.py
--rw-r--r--   0 root         (0) root         (0)     3734 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/secret_manager.py
--rw-r--r--   0 root         (0) root         (0)    15516 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/spanner.py
--rw-r--r--   0 root         (0) root         (0)     4487 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/speech_to_text.py
--rw-r--r--   0 root         (0) root         (0)    25828 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/stackdriver.py
--rw-r--r--   0 root         (0) root         (0)    26769 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/tasks.py
--rw-r--r--   0 root         (0) root         (0)     5346 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/text_to_speech.py
--rw-r--r--   0 root         (0) root         (0)     4373 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/translate.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:50.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/__init__.py
--rw-r--r--   0 root         (0) root         (0)    78059 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/auto_ml.py
--rw-r--r--   0 root         (0) root         (0)    18893 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/batch_prediction_job.py
--rw-r--r--   0 root         (0) root         (0)   109539 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/custom_job.py
--rw-r--r--   0 root         (0) root         (0)    18266 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/dataset.py
--rw-r--r--   0 root         (0) root         (0)    15811 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/endpoint_service.py
--rw-r--r--   0 root         (0) root         (0)    20790 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/hyperparameter_tuning_job.py
--rw-r--r--   0 root         (0) root         (0)     9235 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/model_service.py
--rw-r--r--   0 root         (0) root         (0)     5879 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/video_intelligence.py
--rw-r--r--   0 root         (0) root         (0)    24951 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vision.py
--rw-r--r--   0 root         (0) root         (0)    16183 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/workflows.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:50.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4775 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/automl.py
--rw-r--r--   0 root         (0) root         (0)     1614 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/base.py
--rw-r--r--   0 root         (0) root         (0)     2525 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/bigquery.py
--rw-r--r--   0 root         (0) root         (0)     1870 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/bigquery_dts.py
--rw-r--r--   0 root         (0) root         (0)     3069 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/bigtable.py
--rw-r--r--   0 root         (0) root         (0)     3606 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_build.py
--rw-r--r--   0 root         (0) root         (0)     2527 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_functions.py
--rw-r--r--   0 root         (0) root         (0)     3862 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_memorystore.py
--rw-r--r--   0 root         (0) root         (0)     2527 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_sql.py
--rw-r--r--   0 root         (0) root         (0)     3990 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_storage_transfer.py
--rw-r--r--   0 root         (0) root         (0)     2766 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_tasks.py
--rw-r--r--   0 root         (0) root         (0)     3657 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/compute.py
--rw-r--r--   0 root         (0) root         (0)     9280 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/data_loss_prevention.py
--rw-r--r--   0 root         (0) root         (0)     3632 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/datacatalog.py
--rw-r--r--   0 root         (0) root         (0)     1781 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataflow.py
--rw-r--r--   0 root         (0) root         (0)     3926 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataform.py
--rw-r--r--   0 root         (0) root         (0)     3891 2023-01-24 18:52:14.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/datafusion.py
--rw-r--r--   0 root         (0) root         (0)     3226 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataplex.py
--rw-r--r--   0 root         (0) root         (0)     2233 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataprep.py
--rw-r--r--   0 root         (0) root         (0)     3740 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataproc.py
--rw-r--r--   0 root         (0) root         (0)     2372 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/datastore.py
--rw-r--r--   0 root         (0) root         (0)     2881 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/kubernetes_engine.py
--rw-r--r--   0 root         (0) root         (0)     1628 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/life_sciences.py
--rw-r--r--   0 root         (0) root         (0)     4217 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/mlengine.py
--rw-r--r--   0 root         (0) root         (0)     2416 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/pubsub.py
--rw-r--r--   0 root         (0) root         (0)     2503 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/spanner.py
--rw-r--r--   0 root         (0) root         (0)     2406 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/stackdriver.py
--rw-r--r--   0 root         (0) root         (0)     9684 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/vertex_ai.py
--rw-r--r--   0 root         (0) root         (0)     3294 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/workflows.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:50.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10254 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/gcs_task_handler.py
--rw-r--r--   0 root         (0) root         (0)    15285 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/stackdriver_task_handler.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:51.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)    50423 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/automl.py
--rw-r--r--   0 root         (0) root         (0)   117648 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/bigquery.py
--rw-r--r--   0 root         (0) root         (0)    17103 2023-01-24 18:52:14.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/bigquery_dts.py
--rw-r--r--   0 root         (0) root         (0)    26677 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/bigtable.py
--rw-r--r--   0 root         (0) root         (0)    46643 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_build.py
--rw-r--r--   0 root         (0) root         (0)    29674 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_composer.py
--rw-r--r--   0 root         (0) root         (0)    70593 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_memorystore.py
--rw-r--r--   0 root         (0) root         (0)    45246 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_sql.py
--rw-r--r--   0 root         (0) root         (0)    45233 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_storage_transfer_service.py
--rw-r--r--   0 root         (0) root         (0)    74295 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/compute.py
--rw-r--r--   0 root         (0) root         (0)    92453 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/datacatalog.py
--rw-r--r--   0 root         (0) root         (0)    61714 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataflow.py
--rw-r--r--   0 root         (0) root         (0)    51175 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataform.py
--rw-r--r--   0 root         (0) root         (0)    45215 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/datafusion.py
--rw-r--r--   0 root         (0) root         (0)    29272 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataplex.py
--rw-r--r--   0 root         (0) root         (0)    10242 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataprep.py
--rw-r--r--   0 root         (0) root         (0)   114746 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataproc.py
--rw-r--r--   0 root         (0) root         (0)    49383 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataproc_metastore.py
--rw-r--r--   0 root         (0) root         (0)    28972 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/datastore.py
--rw-r--r--   0 root         (0) root         (0)   119898 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dlp.py
--rw-r--r--   0 root         (0) root         (0)    19966 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/functions.py
--rw-r--r--   0 root         (0) root         (0)    43410 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/gcs.py
--rw-r--r--   0 root         (0) root         (0)    18082 2023-01-13 19:37:41.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/kubernetes_engine.py
--rw-r--r--   0 root         (0) root         (0)     4110 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/life_sciences.py
--rw-r--r--   0 root         (0) root         (0)     4004 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/looker.py
--rw-r--r--   0 root         (0) root         (0)    63267 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/mlengine.py
--rw-r--r--   0 root         (0) root         (0)    13646 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/natural_language.py
--rw-r--r--   0 root         (0) root         (0)    37069 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/pubsub.py
--rw-r--r--   0 root         (0) root         (0)    24831 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/spanner.py
--rw-r--r--   0 root         (0) root         (0)     5485 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/speech_to_text.py
--rw-r--r--   0 root         (0) root         (0)    44068 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/stackdriver.py
--rw-r--r--   0 root         (0) root         (0)    48085 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/tasks.py
--rw-r--r--   0 root         (0) root         (0)     6798 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/text_to_speech.py
--rw-r--r--   0 root         (0) root         (0)     4947 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/translate.py
--rw-r--r--   0 root         (0) root         (0)     7660 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/translate_speech.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:51.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/__init__.py
--rw-r--r--   0 root         (0) root         (0)    28245 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/auto_ml.py
--rw-r--r--   0 root         (0) root         (0)    27607 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/batch_prediction_job.py
--rw-r--r--   0 root         (0) root         (0)    80183 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/custom_job.py
--rw-r--r--   0 root         (0) root         (0)    26523 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/dataset.py
--rw-r--r--   0 root         (0) root         (0)    30405 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/endpoint_service.py
--rw-r--r--   0 root         (0) root         (0)    25299 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/hyperparameter_tuning_job.py
--rw-r--r--   0 root         (0) root         (0)    17019 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/model_service.py
--rw-r--r--   0 root         (0) root         (0)    14112 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/video_intelligence.py
--rw-r--r--   0 root         (0) root         (0)    66925 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vision.py
--rw-r--r--   0 root         (0) root         (0)    28528 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/workflows.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:51.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/secrets/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/secrets/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7770 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/secrets/secret_manager.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:51.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10663 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/bigquery.py
--rw-r--r--   0 root         (0) root         (0)     6303 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/bigquery_dts.py
--rw-r--r--   0 root         (0) root         (0)     5080 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/bigtable.py
--rw-r--r--   0 root         (0) root         (0)     4596 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/cloud_composer.py
--rw-r--r--   0 root         (0) root         (0)     4774 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/cloud_storage_transfer_service.py
--rw-r--r--   0 root         (0) root         (0)    16546 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataflow.py
--rw-r--r--   0 root         (0) root         (0)     5350 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataform.py
--rw-r--r--   0 root         (0) root         (0)     5905 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/datafusion.py
--rw-r--r--   0 root         (0) root         (0)     5092 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataplex.py
--rw-r--r--   0 root         (0) root         (0)     1912 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataprep.py
--rw-r--r--   0 root         (0) root         (0)     7188 2023-01-24 18:52:14.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataproc.py
--rw-r--r--   0 root         (0) root         (0)    19999 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/gcs.py
--rw-r--r--   0 root         (0) root         (0)     3579 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/looker.py
--rw-r--r--   0 root         (0) root         (0)     7100 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/pubsub.py
--rw-r--r--   0 root         (0) root         (0)     3410 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/tasks.py
--rw-r--r--   0 root         (0) root         (0)     5009 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/workflows.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:51.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7119 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/adls_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     7754 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/azure_fileshare_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     6812 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_bigquery.py
--rw-r--r--   0 root         (0) root         (0)    11841 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     6452 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_mssql.py
--rw-r--r--   0 root         (0) root         (0)     5863 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_mysql.py
--rw-r--r--   0 root         (0) root         (0)     8932 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/calendar_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)    16404 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/cassandra_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)    10435 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/facebook_ads_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)    33823 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_bigquery.py
--rw-r--r--   0 root         (0) root         (0)    21593 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     6250 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_local.py
--rw-r--r--   0 root         (0) root         (0)     8630 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_sftp.py
--rw-r--r--   0 root         (0) root         (0)     4720 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gdrive_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     4163 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gdrive_to_local.py
--rw-r--r--   0 root         (0) root         (0)     5062 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/local_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     3344 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/mssql_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     5266 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/mysql_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     4921 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/oracle_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     5692 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/postgres_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     7204 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/presto_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     9103 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/s3_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     4793 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/salesforce_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     7547 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/sftp_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     5888 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/sheets_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)    20842 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/sql_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     7163 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/trino_to_gcs.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/__init__.py
--rw-r--r--   0 root         (0) root         (0)    22682 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/bigquery.py
--rw-r--r--   0 root         (0) root         (0)     6835 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/bigquery_dts.py
--rw-r--r--   0 root         (0) root         (0)     5893 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/cloud_build.py
--rw-r--r--   0 root         (0) root         (0)     3382 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/cloud_composer.py
--rw-r--r--   0 root         (0) root         (0)     6520 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/dataflow.py
--rw-r--r--   0 root         (0) root         (0)     6190 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/datafusion.py
--rw-r--r--   0 root         (0) root         (0)    13046 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/dataproc.py
--rw-r--r--   0 root         (0) root         (0)     3912 2023-01-11 16:59:28.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/gcs.py
--rw-r--r--   0 root         (0) root         (0)     5258 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/mlengine.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/
--rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1492 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/bigquery.py
--rw-r--r--   0 root         (0) root         (0)     1808 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/bigquery_get_data.py
--rw-r--r--   0 root         (0) root         (0)    15853 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/credentials_provider.py
--rw-r--r--   0 root         (0) root         (0)     7028 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/dataform.py
--rw-r--r--   0 root         (0) root         (0)     6086 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/field_sanitizer.py
--rw-r--r--   0 root         (0) root         (0)    22272 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/field_validator.py
--rw-r--r--   0 root         (0) root         (0)     1116 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/helpers.py
--rw-r--r--   0 root         (0) root         (0)    11222 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/mlengine_operator_utils.py
--rw-r--r--   0 root         (0) root         (0)     7672 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/mlengine_prediction_summary.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/auth_backend/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/auth_backend/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4517 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/auth_backend/google_openid.py
--rw-r--r--   0 root         (0) root         (0)     1050 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/consts.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)    26380 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/base_google.py
--rw-r--r--   0 root         (0) root         (0)     6967 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/discovery_api.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/links/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/links/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2258 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/links/storage.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/utils/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7902 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/common/utils/id_token_credentials.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/config_templates/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/config_templates/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6121 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/hooks/firestore.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/operators/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3818 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/operators/firestore.py
--rw-r--r--   0 root         (0) root         (0)    70584 2023-02-08 07:59:43.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/get_provider_info.py
--rw-r--r--   0 root         (0) root         (0)     1794 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/go_module_utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5752 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/hooks/leveldb.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/operators/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3791 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/operators/leveldb.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/example_dags/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/example_dags/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8618 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/example_dags/example_display_video.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7791 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/analytics.py
--rw-r--r--   0 root         (0) root         (0)    11587 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/campaign_manager.py
--rw-r--r--   0 root         (0) root         (0)     7350 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/display_video.py
--rw-r--r--   0 root         (0) root         (0)     3085 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/search_ads.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)    21219 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/analytics.py
--rw-r--r--   0 root         (0) root         (0)    24934 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/campaign_manager.py
--rw-r--r--   0 root         (0) root         (0)    27706 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/display_video.py
--rw-r--r--   0 root         (0) root         (0)     9293 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/search_ads.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4162 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/campaign_manager.py
--rw-r--r--   0 root         (0) root         (0)     6454 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/display_video.py
--rw-r--r--   0 root         (0) root         (0)     3795 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/search_ads.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/
--rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9303 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/calendar.py
--rw-r--r--   0 root         (0) root         (0)    10043 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/drive.py
--rw-r--r--   0 root         (0) root         (0)    16744 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/sheets.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3394 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/operators/sheets.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/sensors/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3616 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/sensors/drive.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/
--rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7255 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/gcs_to_gdrive.py
--rw-r--r--   0 root         (0) root         (0)     4356 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/gcs_to_sheets.py
--rw-r--r--   0 root         (0) root         (0)     5521 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/local_to_drive.py
--rw-r--r--   0 root         (0) root         (0)     5210 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/sql_to_sheets.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/
--rw-r--r--   0 root         (0) root         (0)    70436 2023-02-08 07:59:48.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    16511 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      104 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)     2404 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-02-08 07:59:49.000000 apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     3814 2023-01-13 19:37:41.000000 apache-airflow-providers-google-8.9.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     3433 2023-02-08 07:59:52.000000 apache-airflow-providers-google-8.9.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2587 2023-02-08 07:59:42.000000 apache-airflow-providers-google-8.9.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2022-10-05 12:15:16.000000 apache-airflow-providers-google-8.9.0rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1240 2023-02-08 08:28:08.000000 apache-airflow-providers-google-8.9.0rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2022-10-05 12:15:16.000000 apache-airflow-providers-google-8.9.0rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    70442 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    68456 2023-02-08 08:28:08.000000 apache-airflow-providers-google-8.9.0rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/
+-rw-r--r--   0 root         (0) root         (0)     1578 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    11312 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/hooks/ads.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/operators/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4743 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/operators/ads.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/transfers/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/transfers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5228 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/transfers/ads_to_gcs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/_internal_client/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/_internal_client/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3730 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/_internal_client/secret_manager_client.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3574 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_nl_text_classification.py
+-rw-r--r--   0 root         (0) root         (0)     3666 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_nl_text_sentiment.py
+-rw-r--r--   0 root         (0) root         (0)     3726 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_translation.py
+-rw-r--r--   0 root         (0) root         (0)     3666 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_classification.py
+-rw-r--r--   0 root         (0) root         (0)     3719 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_tracking.py
+-rw-r--r--   0 root         (0) root         (0)     3693 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_vision_object_detection.py
+-rw-r--r--   0 root         (0) root         (0)    10890 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_cloud_sql_query.py
+-rw-r--r--   0 root         (0) root         (0)     7927 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_cloud_storage_transfer_service_aws.py
+-rw-r--r--   0 root         (0) root         (0)     1896 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_cloud_task.py
+-rw-r--r--   0 root         (0) root         (0)     4274 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_compute.py
+-rw-r--r--   0 root         (0) root         (0)     3165 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_compute_ssh.py
+-rw-r--r--   0 root         (0) root         (0)    10681 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_dataflow.py
+-rw-r--r--   0 root         (0) root         (0)     2801 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_dataflow_flex_template.py
+-rw-r--r--   0 root         (0) root         (0)     2586 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_dataflow_sql.py
+-rw-r--r--   0 root         (0) root         (0)     4823 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_facebook_ads_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     2320 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_looker.py
+-rw-r--r--   0 root         (0) root         (0)     1785 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_postgres_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     7363 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_presto_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     4891 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_salesforce_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)    28718 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_vertex_ai.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    27055 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/automl.py
+-rw-r--r--   0 root         (0) root         (0)   136373 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/bigquery.py
+-rw-r--r--   0 root         (0) root         (0)    14391 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/bigquery_dts.py
+-rw-r--r--   0 root         (0) root         (0)    12410 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/bigtable.py
+-rw-r--r--   0 root         (0) root         (0)    25856 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_build.py
+-rw-r--r--   0 root         (0) root         (0)    17570 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_composer.py
+-rw-r--r--   0 root         (0) root         (0)    40873 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_memorystore.py
+-rw-r--r--   0 root         (0) root         (0)    42574 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_sql.py
+-rw-r--r--   0 root         (0) root         (0)    19106 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_storage_transfer_service.py
+-rw-r--r--   0 root         (0) root         (0)    39903 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/compute.py
+-rw-r--r--   0 root         (0) root         (0)    12939 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/compute_ssh.py
+-rw-r--r--   0 root         (0) root         (0)    54442 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/datacatalog.py
+-rw-r--r--   0 root         (0) root         (0)    49406 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataflow.py
+-rw-r--r--   0 root         (0) root         (0)    24996 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataform.py
+-rw-r--r--   0 root         (0) root         (0)    22363 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/datafusion.py
+-rw-r--r--   0 root         (0) root         (0)    15517 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataplex.py
+-rw-r--r--   0 root         (0) root         (0)     8214 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataprep.py
+-rw-r--r--   0 root         (0) root         (0)    76786 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataproc.py
+-rw-r--r--   0 root         (0) root         (0)    29423 2023-01-11 12:48:25.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataproc_metastore.py
+-rw-r--r--   0 root         (0) root         (0)    12124 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/datastore.py
+-rw-r--r--   0 root         (0) root         (0)    64796 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dlp.py
+-rw-r--r--   0 root         (0) root         (0)     9389 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/functions.py
+-rw-r--r--   0 root         (0) root         (0)    49610 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/gcs.py
+-rw-r--r--   0 root         (0) root         (0)     4061 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/gdm.py
+-rw-r--r--   0 root         (0) root         (0)     6717 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/kms.py
+-rw-r--r--   0 root         (0) root         (0)    11423 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/kubernetes_engine.py
+-rw-r--r--   0 root         (0) root         (0)     6245 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/life_sciences.py
+-rw-r--r--   0 root         (0) root         (0)     8902 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/looker.py
+-rw-r--r--   0 root         (0) root         (0)    24449 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/mlengine.py
+-rw-r--r--   0 root         (0) root         (0)    11233 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/natural_language.py
+-rw-r--r--   0 root         (0) root         (0)     3986 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/os_login.py
+-rw-r--r--   0 root         (0) root         (0)    26808 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/pubsub.py
+-rw-r--r--   0 root         (0) root         (0)     3734 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/secret_manager.py
+-rw-r--r--   0 root         (0) root         (0)    15516 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/spanner.py
+-rw-r--r--   0 root         (0) root         (0)     4487 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/speech_to_text.py
+-rw-r--r--   0 root         (0) root         (0)    25828 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/stackdriver.py
+-rw-r--r--   0 root         (0) root         (0)    26769 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/tasks.py
+-rw-r--r--   0 root         (0) root         (0)     5346 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/text_to_speech.py
+-rw-r--r--   0 root         (0) root         (0)     4373 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/translate.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    78059 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/auto_ml.py
+-rw-r--r--   0 root         (0) root         (0)    18893 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/batch_prediction_job.py
+-rw-r--r--   0 root         (0) root         (0)   109539 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/custom_job.py
+-rw-r--r--   0 root         (0) root         (0)    18266 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/dataset.py
+-rw-r--r--   0 root         (0) root         (0)    15811 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/endpoint_service.py
+-rw-r--r--   0 root         (0) root         (0)    20790 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/hyperparameter_tuning_job.py
+-rw-r--r--   0 root         (0) root         (0)     9235 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/model_service.py
+-rw-r--r--   0 root         (0) root         (0)     5879 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/video_intelligence.py
+-rw-r--r--   0 root         (0) root         (0)    24951 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vision.py
+-rw-r--r--   0 root         (0) root         (0)    16183 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/workflows.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4775 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/automl.py
+-rw-r--r--   0 root         (0) root         (0)     1614 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/base.py
+-rw-r--r--   0 root         (0) root         (0)     2525 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/bigquery.py
+-rw-r--r--   0 root         (0) root         (0)     1870 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/bigquery_dts.py
+-rw-r--r--   0 root         (0) root         (0)     3069 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/bigtable.py
+-rw-r--r--   0 root         (0) root         (0)     3606 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_build.py
+-rw-r--r--   0 root         (0) root         (0)     2527 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_functions.py
+-rw-r--r--   0 root         (0) root         (0)     3862 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_memorystore.py
+-rw-r--r--   0 root         (0) root         (0)     2527 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_sql.py
+-rw-r--r--   0 root         (0) root         (0)     3990 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_storage_transfer.py
+-rw-r--r--   0 root         (0) root         (0)     2766 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_tasks.py
+-rw-r--r--   0 root         (0) root         (0)     3657 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/compute.py
+-rw-r--r--   0 root         (0) root         (0)     9280 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/data_loss_prevention.py
+-rw-r--r--   0 root         (0) root         (0)     3632 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/datacatalog.py
+-rw-r--r--   0 root         (0) root         (0)     1781 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataflow.py
+-rw-r--r--   0 root         (0) root         (0)     3926 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataform.py
+-rw-r--r--   0 root         (0) root         (0)     3891 2023-01-24 18:52:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/datafusion.py
+-rw-r--r--   0 root         (0) root         (0)     3226 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataplex.py
+-rw-r--r--   0 root         (0) root         (0)     2233 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataprep.py
+-rw-r--r--   0 root         (0) root         (0)     3740 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataproc.py
+-rw-r--r--   0 root         (0) root         (0)     2372 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/datastore.py
+-rw-r--r--   0 root         (0) root         (0)     2881 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/kubernetes_engine.py
+-rw-r--r--   0 root         (0) root         (0)     1628 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/life_sciences.py
+-rw-r--r--   0 root         (0) root         (0)     4217 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/mlengine.py
+-rw-r--r--   0 root         (0) root         (0)     2416 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/pubsub.py
+-rw-r--r--   0 root         (0) root         (0)     2503 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/spanner.py
+-rw-r--r--   0 root         (0) root         (0)     2406 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/stackdriver.py
+-rw-r--r--   0 root         (0) root         (0)     9684 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/vertex_ai.py
+-rw-r--r--   0 root         (0) root         (0)     3294 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/workflows.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10254 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/gcs_task_handler.py
+-rw-r--r--   0 root         (0) root         (0)    15285 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/stackdriver_task_handler.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    50423 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/automl.py
+-rw-r--r--   0 root         (0) root         (0)   117648 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/bigquery.py
+-rw-r--r--   0 root         (0) root         (0)    17103 2023-01-24 18:52:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/bigquery_dts.py
+-rw-r--r--   0 root         (0) root         (0)    26677 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/bigtable.py
+-rw-r--r--   0 root         (0) root         (0)    46643 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_build.py
+-rw-r--r--   0 root         (0) root         (0)    29674 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_composer.py
+-rw-r--r--   0 root         (0) root         (0)    70593 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_memorystore.py
+-rw-r--r--   0 root         (0) root         (0)    45246 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_sql.py
+-rw-r--r--   0 root         (0) root         (0)    45233 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_storage_transfer_service.py
+-rw-r--r--   0 root         (0) root         (0)    74295 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/compute.py
+-rw-r--r--   0 root         (0) root         (0)    92453 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/datacatalog.py
+-rw-r--r--   0 root         (0) root         (0)    61714 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataflow.py
+-rw-r--r--   0 root         (0) root         (0)    51175 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataform.py
+-rw-r--r--   0 root         (0) root         (0)    45215 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/datafusion.py
+-rw-r--r--   0 root         (0) root         (0)    29272 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataplex.py
+-rw-r--r--   0 root         (0) root         (0)    10242 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataprep.py
+-rw-r--r--   0 root         (0) root         (0)   114746 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataproc.py
+-rw-r--r--   0 root         (0) root         (0)    49383 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataproc_metastore.py
+-rw-r--r--   0 root         (0) root         (0)    28972 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/datastore.py
+-rw-r--r--   0 root         (0) root         (0)   119898 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dlp.py
+-rw-r--r--   0 root         (0) root         (0)    19966 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/functions.py
+-rw-r--r--   0 root         (0) root         (0)    43410 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/gcs.py
+-rw-r--r--   0 root         (0) root         (0)    18082 2023-01-13 19:37:41.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/kubernetes_engine.py
+-rw-r--r--   0 root         (0) root         (0)     4110 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/life_sciences.py
+-rw-r--r--   0 root         (0) root         (0)     4004 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/looker.py
+-rw-r--r--   0 root         (0) root         (0)    63267 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/mlengine.py
+-rw-r--r--   0 root         (0) root         (0)    13646 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/natural_language.py
+-rw-r--r--   0 root         (0) root         (0)    37069 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/pubsub.py
+-rw-r--r--   0 root         (0) root         (0)    24831 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/spanner.py
+-rw-r--r--   0 root         (0) root         (0)     5485 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/speech_to_text.py
+-rw-r--r--   0 root         (0) root         (0)    44068 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/stackdriver.py
+-rw-r--r--   0 root         (0) root         (0)    48085 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/tasks.py
+-rw-r--r--   0 root         (0) root         (0)     6798 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/text_to_speech.py
+-rw-r--r--   0 root         (0) root         (0)     4947 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/translate.py
+-rw-r--r--   0 root         (0) root         (0)     7660 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/translate_speech.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    28245 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/auto_ml.py
+-rw-r--r--   0 root         (0) root         (0)    27607 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/batch_prediction_job.py
+-rw-r--r--   0 root         (0) root         (0)    80183 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/custom_job.py
+-rw-r--r--   0 root         (0) root         (0)    26523 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/dataset.py
+-rw-r--r--   0 root         (0) root         (0)    30405 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/endpoint_service.py
+-rw-r--r--   0 root         (0) root         (0)    25299 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/hyperparameter_tuning_job.py
+-rw-r--r--   0 root         (0) root         (0)    17019 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/model_service.py
+-rw-r--r--   0 root         (0) root         (0)    14112 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/video_intelligence.py
+-rw-r--r--   0 root         (0) root         (0)    66925 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vision.py
+-rw-r--r--   0 root         (0) root         (0)    28528 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/workflows.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/secrets/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/secrets/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7770 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/secrets/secret_manager.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10663 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/bigquery.py
+-rw-r--r--   0 root         (0) root         (0)     6303 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/bigquery_dts.py
+-rw-r--r--   0 root         (0) root         (0)     5080 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/bigtable.py
+-rw-r--r--   0 root         (0) root         (0)     4596 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/cloud_composer.py
+-rw-r--r--   0 root         (0) root         (0)     4774 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/cloud_storage_transfer_service.py
+-rw-r--r--   0 root         (0) root         (0)    16546 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataflow.py
+-rw-r--r--   0 root         (0) root         (0)     5350 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataform.py
+-rw-r--r--   0 root         (0) root         (0)     5905 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/datafusion.py
+-rw-r--r--   0 root         (0) root         (0)     5092 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataplex.py
+-rw-r--r--   0 root         (0) root         (0)     1912 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataprep.py
+-rw-r--r--   0 root         (0) root         (0)     7188 2023-01-24 18:52:14.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataproc.py
+-rw-r--r--   0 root         (0) root         (0)    19999 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/gcs.py
+-rw-r--r--   0 root         (0) root         (0)     3579 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/looker.py
+-rw-r--r--   0 root         (0) root         (0)     7100 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/pubsub.py
+-rw-r--r--   0 root         (0) root         (0)     3410 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/tasks.py
+-rw-r--r--   0 root         (0) root         (0)     5009 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/workflows.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7119 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/adls_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     7754 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/azure_fileshare_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     6812 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_bigquery.py
+-rw-r--r--   0 root         (0) root         (0)    11841 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     6452 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_mssql.py
+-rw-r--r--   0 root         (0) root         (0)     5863 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_mysql.py
+-rw-r--r--   0 root         (0) root         (0)     8932 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/calendar_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)    16404 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/cassandra_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)    10435 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/facebook_ads_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)    33823 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_bigquery.py
+-rw-r--r--   0 root         (0) root         (0)    21593 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     6250 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_local.py
+-rw-r--r--   0 root         (0) root         (0)     8630 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_sftp.py
+-rw-r--r--   0 root         (0) root         (0)     4720 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gdrive_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     4163 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gdrive_to_local.py
+-rw-r--r--   0 root         (0) root         (0)     5062 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/local_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     3344 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/mssql_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     5266 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/mysql_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     4921 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/oracle_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     5692 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/postgres_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     7204 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/presto_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     9103 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/s3_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     4793 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/salesforce_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     7547 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/sftp_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     5888 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/sheets_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)    20842 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/sql_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     7163 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/trino_to_gcs.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    22682 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/bigquery.py
+-rw-r--r--   0 root         (0) root         (0)     6835 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/bigquery_dts.py
+-rw-r--r--   0 root         (0) root         (0)     5893 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/cloud_build.py
+-rw-r--r--   0 root         (0) root         (0)     3382 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/cloud_composer.py
+-rw-r--r--   0 root         (0) root         (0)     6520 2023-02-02 18:37:35.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/dataflow.py
+-rw-r--r--   0 root         (0) root         (0)     6190 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/datafusion.py
+-rw-r--r--   0 root         (0) root         (0)    13046 2023-02-05 09:48:53.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/dataproc.py
+-rw-r--r--   0 root         (0) root         (0)     3912 2023-01-11 16:59:28.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/gcs.py
+-rw-r--r--   0 root         (0) root         (0)     5258 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/mlengine.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/
+-rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1492 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/bigquery.py
+-rw-r--r--   0 root         (0) root         (0)     1808 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/bigquery_get_data.py
+-rw-r--r--   0 root         (0) root         (0)    15853 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/credentials_provider.py
+-rw-r--r--   0 root         (0) root         (0)     7028 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/dataform.py
+-rw-r--r--   0 root         (0) root         (0)     6086 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/field_sanitizer.py
+-rw-r--r--   0 root         (0) root         (0)    22272 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/field_validator.py
+-rw-r--r--   0 root         (0) root         (0)     1116 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/helpers.py
+-rw-r--r--   0 root         (0) root         (0)    11222 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/mlengine_operator_utils.py
+-rw-r--r--   0 root         (0) root         (0)     7672 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/mlengine_prediction_summary.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/auth_backend/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/auth_backend/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4517 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/auth_backend/google_openid.py
+-rw-r--r--   0 root         (0) root         (0)     1050 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/consts.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    26380 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/base_google.py
+-rw-r--r--   0 root         (0) root         (0)     6967 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/discovery_api.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/links/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/links/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2258 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/links/storage.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/utils/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7902 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/utils/id_token_credentials.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/config_templates/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/config_templates/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6121 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/hooks/firestore.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/operators/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3818 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/operators/firestore.py
+-rw-r--r--   0 root         (0) root         (0)    70584 2023-02-08 08:28:08.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/get_provider_info.py
+-rw-r--r--   0 root         (0) root         (0)     1794 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/go_module_utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5752 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/hooks/leveldb.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/operators/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3791 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/operators/leveldb.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/example_dags/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/example_dags/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     8618 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/example_dags/example_display_video.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7791 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/analytics.py
+-rw-r--r--   0 root         (0) root         (0)    11587 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/campaign_manager.py
+-rw-r--r--   0 root         (0) root         (0)     7350 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/display_video.py
+-rw-r--r--   0 root         (0) root         (0)     3085 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/search_ads.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:16.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    21219 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/analytics.py
+-rw-r--r--   0 root         (0) root         (0)    24934 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/campaign_manager.py
+-rw-r--r--   0 root         (0) root         (0)    27706 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/display_video.py
+-rw-r--r--   0 root         (0) root         (0)     9293 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/search_ads.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4162 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/campaign_manager.py
+-rw-r--r--   0 root         (0) root         (0)     6454 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/display_video.py
+-rw-r--r--   0 root         (0) root         (0)     3795 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/search_ads.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/
+-rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9303 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/calendar.py
+-rw-r--r--   0 root         (0) root         (0)    10043 2023-01-26 14:58:03.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/drive.py
+-rw-r--r--   0 root         (0) root         (0)    16744 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/sheets.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3394 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/operators/sheets.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/sensors/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3616 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/sensors/drive.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/
+-rw-r--r--   0 root         (0) root         (0)      785 2022-10-05 12:15:15.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7255 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/gcs_to_gdrive.py
+-rw-r--r--   0 root         (0) root         (0)     4356 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/gcs_to_sheets.py
+-rw-r--r--   0 root         (0) root         (0)     5521 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/local_to_drive.py
+-rw-r--r--   0 root         (0) root         (0)     5210 2023-01-11 12:48:26.000000 apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/sql_to_sheets.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    70442 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    16511 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      104 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)     2414 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-02-08 08:28:13.000000 apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     3814 2023-01-13 19:37:41.000000 apache-airflow-providers-google-8.9.0rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     3446 2023-02-08 08:28:17.000000 apache-airflow-providers-google-8.9.0rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2587 2023-02-08 08:28:07.000000 apache-airflow-providers-google-8.9.0rc1/setup.py
```

### Comparing `apache-airflow-providers-google-8.9.0/LICENSE` & `apache-airflow-providers-google-8.9.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/MANIFEST.in` & `apache-airflow-providers-google-8.9.0rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/PKG-INFO` & `apache-airflow-providers-google-8.9.0rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-google
-Version: 8.9.0
+Version: 8.9.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-google package
 Home-page: https://airflow.apache.org/
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-google/8.9.0/
@@ -66,15 +66,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-google``
 
-Release: ``8.9.0``
+Release: ``8.9.0rc1``
 
 
 Google services including:
 
   - `Google Ads <https://ads.google.com/>`__
   - `Google Cloud (GCP) <https://cloud.google.com/>`__
   - `Google Firebase <https://firebase.google.com/>`__
```

### Comparing `apache-airflow-providers-google-8.9.0/README.rst` & `apache-airflow-providers-google-8.9.0rc1/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-google``
 
-Release: ``8.9.0``
+Release: ``8.9.0rc1``
 
 
 Google services including:
 
   - `Google Ads <https://ads.google.com/>`__
   - `Google Cloud (GCP) <https://cloud.google.com/>`__
   - `Google Firebase <https://firebase.google.com/>`__
```

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/hooks/ads.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/hooks/ads.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/operators/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/operators/ads.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/operators/ads.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/transfers/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/transfers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/ads/transfers/ads_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/ads/transfers/ads_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/_internal_client/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/_internal_client/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/_internal_client/secret_manager_client.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/_internal_client/secret_manager_client.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_nl_text_classification.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_nl_text_classification.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_nl_text_sentiment.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_nl_text_sentiment.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_translation.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_translation.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_classification.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_classification.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_tracking.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_video_intelligence_tracking.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_automl_vision_object_detection.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_automl_vision_object_detection.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_cloud_sql_query.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_cloud_sql_query.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_cloud_storage_transfer_service_aws.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_cloud_storage_transfer_service_aws.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_cloud_task.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_cloud_task.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_compute.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_compute.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_compute_ssh.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_compute_ssh.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_dataflow.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_dataflow.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_dataflow_flex_template.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_dataflow_flex_template.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_dataflow_sql.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_dataflow_sql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_facebook_ads_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_facebook_ads_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_looker.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_looker.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_postgres_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_postgres_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_presto_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_presto_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_salesforce_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_salesforce_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/example_dags/example_vertex_ai.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/example_dags/example_vertex_ai.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/automl.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/automl.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/bigquery_dts.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/bigquery_dts.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/bigtable.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/bigtable.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_build.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_build.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_composer.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_composer.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_memorystore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_memorystore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_sql.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_sql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/cloud_storage_transfer_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/cloud_storage_transfer_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/compute.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/compute.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/compute_ssh.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/compute_ssh.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/datacatalog.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/datacatalog.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataflow.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataflow.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataform.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataform.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/datafusion.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/datafusion.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataplex.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataplex.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataprep.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataprep.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataproc.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataproc.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dataproc_metastore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dataproc_metastore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/datastore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/datastore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/dlp.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/dlp.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/functions.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/functions.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/gdm.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/gdm.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/kms.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/kms.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/kubernetes_engine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/kubernetes_engine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/life_sciences.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/life_sciences.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/looker.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/looker.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/mlengine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/mlengine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/natural_language.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/natural_language.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/os_login.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/os_login.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/pubsub.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/pubsub.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/secret_manager.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/secret_manager.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/spanner.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/spanner.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/speech_to_text.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/speech_to_text.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/stackdriver.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/stackdriver.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/tasks.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/tasks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/text_to_speech.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/text_to_speech.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/translate.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/translate.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/auto_ml.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/auto_ml.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/batch_prediction_job.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/batch_prediction_job.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/custom_job.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/custom_job.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/dataset.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/dataset.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/endpoint_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/endpoint_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/hyperparameter_tuning_job.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/hyperparameter_tuning_job.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vertex_ai/model_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vertex_ai/model_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/video_intelligence.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/video_intelligence.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/vision.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/vision.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/hooks/workflows.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/hooks/workflows.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/automl.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/automl.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/base.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/base.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/bigquery_dts.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/bigquery_dts.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/bigtable.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/bigtable.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_build.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_build.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_functions.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_functions.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_memorystore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_memorystore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_sql.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_sql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_storage_transfer.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_storage_transfer.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/cloud_tasks.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/cloud_tasks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/compute.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/compute.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/data_loss_prevention.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/data_loss_prevention.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/datacatalog.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/datacatalog.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataflow.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataflow.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataform.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataform.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/datafusion.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/datafusion.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataplex.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataplex.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataprep.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataprep.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/dataproc.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/dataproc.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/datastore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/datastore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/kubernetes_engine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/kubernetes_engine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/life_sciences.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/life_sciences.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/mlengine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/mlengine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/pubsub.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/pubsub.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/spanner.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/spanner.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/stackdriver.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/stackdriver.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/vertex_ai.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/vertex_ai.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/links/workflows.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/links/workflows.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/gcs_task_handler.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/gcs_task_handler.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/log/stackdriver_task_handler.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/log/stackdriver_task_handler.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/automl.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/automl.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/bigquery_dts.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/bigquery_dts.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/bigtable.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/bigtable.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_build.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_build.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_composer.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_composer.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_memorystore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_memorystore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_sql.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_sql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/cloud_storage_transfer_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/cloud_storage_transfer_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/compute.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/compute.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/datacatalog.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/datacatalog.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataflow.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataflow.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataform.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataform.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/datafusion.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/datafusion.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataplex.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataplex.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataprep.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataprep.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataproc.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataproc.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dataproc_metastore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dataproc_metastore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/datastore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/datastore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/dlp.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/dlp.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/functions.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/functions.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/kubernetes_engine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/kubernetes_engine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/life_sciences.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/life_sciences.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/looker.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/looker.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/mlengine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/mlengine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/natural_language.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/natural_language.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/pubsub.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/pubsub.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/spanner.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/spanner.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/speech_to_text.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/speech_to_text.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/stackdriver.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/stackdriver.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/tasks.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/tasks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/text_to_speech.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/text_to_speech.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/translate.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/translate.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/translate_speech.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/translate_speech.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/auto_ml.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/auto_ml.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/batch_prediction_job.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/batch_prediction_job.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/custom_job.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/custom_job.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/dataset.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/dataset.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/endpoint_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/endpoint_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/hyperparameter_tuning_job.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/hyperparameter_tuning_job.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vertex_ai/model_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vertex_ai/model_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/video_intelligence.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/video_intelligence.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/vision.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/vision.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/operators/workflows.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/operators/workflows.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/secrets/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/secrets/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/secrets/secret_manager.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/secrets/secret_manager.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/bigquery_dts.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/bigquery_dts.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/bigtable.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/bigtable.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/cloud_composer.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/cloud_composer.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/cloud_storage_transfer_service.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/cloud_storage_transfer_service.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataflow.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataflow.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataform.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataform.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/datafusion.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/datafusion.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataplex.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataplex.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataprep.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataprep.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/dataproc.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/dataproc.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/looker.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/looker.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/pubsub.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/pubsub.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/tasks.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/tasks.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/sensors/workflows.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/sensors/workflows.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/adls_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/adls_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/azure_fileshare_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/azure_fileshare_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_mssql.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_mssql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/bigquery_to_mysql.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/bigquery_to_mysql.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/calendar_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/calendar_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/cassandra_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/cassandra_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/facebook_ads_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/facebook_ads_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_local.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_local.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gcs_to_sftp.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gcs_to_sftp.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gdrive_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gdrive_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/gdrive_to_local.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/gdrive_to_local.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/local_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/local_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/mssql_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/mssql_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/mysql_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/mysql_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/oracle_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/oracle_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/postgres_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/postgres_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/presto_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/presto_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/s3_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/s3_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/salesforce_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/salesforce_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/sftp_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/sftp_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/sheets_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/sheets_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/sql_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/sql_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/transfers/trino_to_gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/transfers/trino_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/bigquery_dts.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/bigquery_dts.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/cloud_build.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/cloud_build.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/cloud_composer.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/cloud_composer.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/dataflow.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/dataflow.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/datafusion.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/datafusion.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/dataproc.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/dataproc.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/gcs.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/triggers/mlengine.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/triggers/mlengine.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/bigquery.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/bigquery.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/bigquery_get_data.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/bigquery_get_data.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/credentials_provider.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/credentials_provider.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/dataform.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/dataform.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/field_sanitizer.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/field_sanitizer.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/field_validator.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/field_validator.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/helpers.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/helpers.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/mlengine_operator_utils.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/mlengine_operator_utils.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/cloud/utils/mlengine_prediction_summary.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/cloud/utils/mlengine_prediction_summary.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/auth_backend/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/auth_backend/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/auth_backend/google_openid.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/auth_backend/google_openid.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/consts.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/consts.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/base_google.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/base_google.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/hooks/discovery_api.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/hooks/discovery_api.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/links/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/links/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/links/storage.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/links/storage.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/utils/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/common/utils/id_token_credentials.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/common/utils/id_token_credentials.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/config_templates/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/config_templates/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/hooks/firestore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/hooks/firestore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/operators/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/firebase/operators/firestore.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/firebase/operators/firestore.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/get_provider_info.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/go_module_utils.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/go_module_utils.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/hooks/leveldb.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/hooks/leveldb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/operators/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/leveldb/operators/leveldb.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/leveldb/operators/leveldb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/example_dags/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/example_dags/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/example_dags/example_display_video.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/example_dags/example_display_video.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/analytics.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/analytics.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/campaign_manager.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/campaign_manager.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/display_video.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/display_video.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/hooks/search_ads.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/hooks/search_ads.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/analytics.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/analytics.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/campaign_manager.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/campaign_manager.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/display_video.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/display_video.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/operators/search_ads.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/operators/search_ads.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/campaign_manager.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/campaign_manager.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/display_video.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/display_video.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/marketing_platform/sensors/search_ads.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/marketing_platform/sensors/search_ads.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/calendar.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/calendar.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/drive.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/drive.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/hooks/sheets.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/hooks/sheets.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/operators/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/operators/sheets.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/operators/sheets.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/sensors/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/sensors/drive.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/sensors/drive.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/__init__.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/gcs_to_gdrive.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/gcs_to_gdrive.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/gcs_to_sheets.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/gcs_to_sheets.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/local_to_drive.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/local_to_drive.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/airflow/providers/google/suite/transfers/sql_to_sheets.py` & `apache-airflow-providers-google-8.9.0rc1/airflow/providers/google/suite/transfers/sql_to_sheets.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/PKG-INFO` & `apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-google
-Version: 8.9.0
+Version: 8.9.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-google package
 Home-page: https://airflow.apache.org/
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-google/8.9.0/
@@ -66,15 +66,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-google``
 
-Release: ``8.9.0``
+Release: ``8.9.0rc1``
 
 
 Google services including:
 
   - `Google Ads <https://ads.google.com/>`__
   - `Google Cloud (GCP) <https://cloud.google.com/>`__
   - `Google Firebase <https://firebase.google.com/>`__
```

### Comparing `apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/SOURCES.txt` & `apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/apache_airflow_providers_google.egg-info/requires.txt` & `apache-airflow-providers-google-8.9.0rc1/apache_airflow_providers_google.egg-info/requires.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 PyOpenSSL
-apache-airflow-providers-common-sql>=1.3.1
-apache-airflow>=2.3.0
+apache-airflow-providers-common-sql>=1.3.1.dev0
+apache-airflow>=2.3.0.dev0
 asgiref>=3.5.2
 gcloud-aio-auth<5.0.0,>=4.0.0
 gcloud-aio-bigquery>=6.1.2
 gcloud-aio-storage
 google-ads>=15.1.1
 google-api-core<3.0.0,>=2.7.0
 google-api-python-client<2.0.0,>=1.6.0
```

### Comparing `apache-airflow-providers-google-8.9.0/pyproject.toml` & `apache-airflow-providers-google-8.9.0rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-google-8.9.0/setup.cfg` & `apache-airflow-providers-google-8.9.0rc1/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -43,16 +43,16 @@
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
 	PyOpenSSL
-	apache-airflow-providers-common-sql>=1.3.1
-	apache-airflow>=2.3.0
+	apache-airflow-providers-common-sql>=1.3.1.dev0
+	apache-airflow>=2.3.0.dev0
 	asgiref>=3.5.2
 	gcloud-aio-auth>=4.0.0,<5.0.0
 	gcloud-aio-bigquery>=6.1.2
 	gcloud-aio-storage
 	google-ads>=15.1.1
 	google-api-core>=2.7.0,<3.0.0
 	google-api-python-client>=1.6.0,<2.0.0
@@ -105,10 +105,10 @@
 apache_airflow_provider = 
 	provider_info=airflow.providers.google.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.google
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-google-8.9.0/setup.py` & `apache-airflow-providers-google-8.9.0rc1/setup.py`

 * *Files identical despite different names*

