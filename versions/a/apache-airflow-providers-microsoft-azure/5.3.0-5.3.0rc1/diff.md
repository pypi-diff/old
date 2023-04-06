# Comparing `tmp/apache-airflow-providers-microsoft-azure-5.3.0.tar.gz` & `tmp/apache-airflow-providers-microsoft-azure-5.3.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/apache-airflow-providers-microsoft-azure-5.3.0.tar", last modified: Sun Apr  2 05:40:12 2023, max compression
+gzip compressed data, was "dist/apache-airflow-providers-microsoft-azure-5.3.0rc1.tar", last modified: Sun Apr  2 05:48:58 2023, max compression
```

## Comparing `apache-airflow-providers-microsoft-azure-5.3.0.tar` & `apache-airflow-providers-microsoft-azure-5.3.0rc1.tar`

### file list

```diff
@@ -1,72 +1,72 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:12.000000 apache-airflow-providers-microsoft-azure-5.3.0/
--rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-microsoft-azure-5.3.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:40:09.000000 apache-airflow-providers-microsoft-azure-5.3.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-microsoft-azure-5.3.0/NOTICE
--rw-r--r--   0 root         (0) root         (0)    24630 2023-04-02 05:40:12.000000 apache-airflow-providers-microsoft-azure-5.3.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    23012 2023-04-02 05:40:09.000000 apache-airflow-providers-microsoft-azure-5.3.0/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/__init__.py
--rw-r--r--   0 root         (0) root         (0)    16571 2023-04-02 05:40:09.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/get_provider_info.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8720 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/adx.py
--rw-r--r--   0 root         (0) root         (0)    10986 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/asb.py
--rw-r--r--   0 root         (0) root         (0)     4778 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/base_azure.py
--rw-r--r--   0 root         (0) root         (0)    15288 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/batch.py
--rw-r--r--   0 root         (0) root         (0)     6056 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/container_instance.py
--rw-r--r--   0 root         (0) root         (0)     2458 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/container_registry.py
--rw-r--r--   0 root         (0) root         (0)     4058 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/container_volume.py
--rw-r--r--   0 root         (0) root         (0)    14222 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/cosmos.py
--rw-r--r--   0 root         (0) root         (0)    42973 2023-03-30 19:12:06.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/data_factory.py
--rw-r--r--   0 root         (0) root         (0)    21695 2023-03-10 19:32:05.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/data_lake.py
--rw-r--r--   0 root         (0) root         (0)    12985 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/fileshare.py
--rw-r--r--   0 root         (0) root         (0)     7318 2023-03-16 20:46:35.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/synapse.py
--rw-r--r--   0 root         (0) root         (0)    27566 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/wasb.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/log/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/log/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10038 2023-03-10 19:31:58.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/log/wasb_task_handler.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3788 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/adls.py
--rw-r--r--   0 root         (0) root         (0)     3029 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/adx.py
--rw-r--r--   0 root         (0) root         (0)    29576 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/asb.py
--rw-r--r--   0 root         (0) root         (0)    16252 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/batch.py
--rw-r--r--   0 root         (0) root         (0)    15967 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/container_instances.py
--rw-r--r--   0 root         (0) root         (0)     2766 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/cosmos.py
--rw-r--r--   0 root         (0) root         (0)    11545 2023-03-27 08:32:49.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/data_factory.py
--rw-r--r--   0 root         (0) root         (0)     4422 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/synapse.py
--rw-r--r--   0 root         (0) root         (0)     2687 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/wasb_delete_blob.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/secrets/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/secrets/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7822 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/secrets/key_vault.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/
--rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2643 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/cosmos.py
--rw-r--r--   0 root         (0) root         (0)     5611 2023-03-30 19:12:06.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/data_factory.py
--rw-r--r--   0 root         (0) root         (0)     5957 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/wasb.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/
--rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5293 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/azure_blob_to_gcs.py
--rw-r--r--   0 root         (0) root         (0)     4765 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/local_to_adls.py
--rw-r--r--   0 root         (0) root         (0)     2936 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/local_to_wasb.py
--rw-r--r--   0 root         (0) root         (0)     4575 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/oracle_to_azure_data_lake.py
--rw-r--r--   0 root         (0) root         (0)     8215 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/sftp_to_wasb.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/
--rw-r--r--   0 root         (0) root         (0)      785 2023-03-14 06:24:40.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     8863 2023-03-27 08:32:49.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/data_factory.py
--rw-r--r--   0 root         (0) root         (0)     3889 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/wasb.py
--rw-r--r--   0 root         (0) root         (0)     2804 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:40:12.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/
--rw-r--r--   0 root         (0) root         (0)    24630 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2944 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      112 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/not-zip-safe
--rw-r--r--   0 root         (0) root         (0)      604 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:40:11.000000 apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)     2351 2023-04-02 05:40:12.000000 apache-airflow-providers-microsoft-azure-5.3.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1704 2023-04-02 05:40:09.000000 apache-airflow-providers-microsoft-azure-5.3.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/
+-rw-r--r--   0 root         (0) root         (0)    10850 2023-02-24 18:43:54.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     1122 2023-04-02 05:48:55.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      240 2023-02-24 18:43:54.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/NOTICE
+-rw-r--r--   0 root         (0) root         (0)    24636 2023-04-02 05:48:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    23015 2023-04-02 05:48:55.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    16571 2023-04-02 05:48:55.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/get_provider_info.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     8720 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/adx.py
+-rw-r--r--   0 root         (0) root         (0)    10986 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/asb.py
+-rw-r--r--   0 root         (0) root         (0)     4778 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/base_azure.py
+-rw-r--r--   0 root         (0) root         (0)    15288 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/batch.py
+-rw-r--r--   0 root         (0) root         (0)     6056 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/container_instance.py
+-rw-r--r--   0 root         (0) root         (0)     2458 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/container_registry.py
+-rw-r--r--   0 root         (0) root         (0)     4058 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/container_volume.py
+-rw-r--r--   0 root         (0) root         (0)    14222 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/cosmos.py
+-rw-r--r--   0 root         (0) root         (0)    42973 2023-03-30 19:12:06.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/data_factory.py
+-rw-r--r--   0 root         (0) root         (0)    21695 2023-03-10 19:32:05.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/data_lake.py
+-rw-r--r--   0 root         (0) root         (0)    12985 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/fileshare.py
+-rw-r--r--   0 root         (0) root         (0)     7318 2023-03-16 20:46:35.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/synapse.py
+-rw-r--r--   0 root         (0) root         (0)    27566 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/wasb.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/log/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/log/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10038 2023-03-10 19:31:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/log/wasb_task_handler.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3788 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/adls.py
+-rw-r--r--   0 root         (0) root         (0)     3029 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/adx.py
+-rw-r--r--   0 root         (0) root         (0)    29576 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/asb.py
+-rw-r--r--   0 root         (0) root         (0)    16252 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/batch.py
+-rw-r--r--   0 root         (0) root         (0)    15967 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/container_instances.py
+-rw-r--r--   0 root         (0) root         (0)     2766 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/cosmos.py
+-rw-r--r--   0 root         (0) root         (0)    11545 2023-03-27 08:32:49.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/data_factory.py
+-rw-r--r--   0 root         (0) root         (0)     4422 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/synapse.py
+-rw-r--r--   0 root         (0) root         (0)     2687 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/wasb_delete_blob.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/secrets/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/secrets/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7822 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/secrets/key_vault.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/
+-rw-r--r--   0 root         (0) root         (0)      787 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2643 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/cosmos.py
+-rw-r--r--   0 root         (0) root         (0)     5611 2023-03-30 19:12:06.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/data_factory.py
+-rw-r--r--   0 root         (0) root         (0)     5957 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/wasb.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5293 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/azure_blob_to_gcs.py
+-rw-r--r--   0 root         (0) root         (0)     4765 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/local_to_adls.py
+-rw-r--r--   0 root         (0) root         (0)     2936 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/local_to_wasb.py
+-rw-r--r--   0 root         (0) root         (0)     4575 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/oracle_to_azure_data_lake.py
+-rw-r--r--   0 root         (0) root         (0)     8215 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/sftp_to_wasb.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/
+-rw-r--r--   0 root         (0) root         (0)      785 2023-03-14 06:24:40.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     8863 2023-03-27 08:32:49.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/data_factory.py
+-rw-r--r--   0 root         (0) root         (0)     3889 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/wasb.py
+-rw-r--r--   0 root         (0) root         (0)     2804 2023-02-24 18:43:53.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-02 05:48:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/
+-rw-r--r--   0 root         (0) root         (0)    24636 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2944 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      112 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)      609 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-04-02 05:48:57.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)     5393 2023-04-01 16:40:04.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)     2359 2023-04-02 05:48:58.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1704 2023-04-02 05:48:55.000000 apache-airflow-providers-microsoft-azure-5.3.0rc1/setup.py
```

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/LICENSE` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/MANIFEST.in` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/PKG-INFO` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-microsoft-azure
-Version: 5.3.0
+Version: 5.3.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-microsoft-azure package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/5.3.0/
@@ -51,15 +51,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-microsoft-azure``
 
-Release: ``5.3.0``
+Release: ``5.3.0rc1``
 
 
 `Microsoft Azure <https://azure.microsoft.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/README.rst` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -15,15 +15,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-microsoft-azure``
 
-Release: ``5.3.0``
+Release: ``5.3.0rc1``
 
 
 `Microsoft Azure <https://azure.microsoft.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/get_provider_info.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/get_provider_info.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/adx.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/adx.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/asb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/asb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/base_azure.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/base_azure.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/batch.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/batch.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/container_instance.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/container_instance.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/container_registry.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/container_registry.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/container_volume.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/container_volume.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/cosmos.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/cosmos.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/data_factory.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/data_factory.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/data_lake.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/data_lake.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/fileshare.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/fileshare.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/synapse.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/synapse.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/hooks/wasb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/hooks/wasb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/log/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/log/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/log/wasb_task_handler.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/log/wasb_task_handler.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/adls.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/adls.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/adx.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/adx.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/asb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/asb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/batch.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/batch.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/container_instances.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/container_instances.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/cosmos.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/cosmos.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/data_factory.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/data_factory.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/synapse.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/synapse.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/operators/wasb_delete_blob.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/operators/wasb_delete_blob.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/secrets/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/secrets/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/secrets/key_vault.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/secrets/key_vault.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/cosmos.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/cosmos.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/data_factory.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/data_factory.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/sensors/wasb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/sensors/wasb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/azure_blob_to_gcs.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/azure_blob_to_gcs.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/local_to_adls.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/local_to_adls.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/local_to_wasb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/local_to_wasb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/oracle_to_azure_data_lake.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/oracle_to_azure_data_lake.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/transfers/sftp_to_wasb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/transfers/sftp_to_wasb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/__init__.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/__init__.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/data_factory.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/data_factory.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/triggers/wasb.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/triggers/wasb.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/airflow/providers/microsoft/azure/utils.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/airflow/providers/microsoft/azure/utils.py`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/PKG-INFO` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: apache-airflow-providers-microsoft-azure
-Version: 5.3.0
+Version: 5.3.0rc1
 Summary: Provider for Apache Airflow. Implements apache-airflow-providers-microsoft-azure package
 Home-page: https://airflow.apache.org/
 Download-URL: https://archive.apache.org/dist/airflow/providers
 Author: Apache Software Foundation
 Author-email: dev@airflow.apache.org
 License: Apache License 2.0
 Project-URL: Documentation, https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/5.3.0/
@@ -51,15 +51,15 @@
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.
 
 
 Package ``apache-airflow-providers-microsoft-azure``
 
-Release: ``5.3.0``
+Release: ``5.3.0rc1``
 
 
 `Microsoft Azure <https://azure.microsoft.com/>`__
 
 
 Provider package
 ----------------
```

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/SOURCES.txt` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/apache_airflow_providers_microsoft_azure.egg-info/requires.txt` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/apache_airflow_providers_microsoft_azure.egg-info/requires.txt`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 adal>=1.2.7
-apache-airflow>=2.3.0
+apache-airflow>=2.3.0.dev0
 azure-batch>=8.0.0
 azure-cosmos>=4.0.0
 azure-datalake-store>=0.0.45
 azure-identity>=1.3.1
 azure-keyvault-secrets>=4.1.0
 azure-kusto-data<0.1,>=0.0.43
 azure-mgmt-containerinstance<2.0,>=1.5.0
```

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/pyproject.toml` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/setup.cfg` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/setup.cfg`

 * *Files 5% similar despite different names*

```diff
@@ -43,15 +43,15 @@
 python_requires = ~=3.7
 packages = find:
 setup_requires = 
 	setuptools
 	wheel
 install_requires = 
 	adal>=1.2.7
-	apache-airflow>=2.3.0
+	apache-airflow>=2.3.0.dev0
 	azure-batch>=8.0.0
 	azure-cosmos>=4.0.0
 	azure-datalake-store>=0.0.45
 	azure-identity>=1.3.1
 	azure-keyvault-secrets>=4.1.0
 	azure-kusto-data>=0.0.43,<0.1
 	azure-mgmt-containerinstance>=1.5.0,<2.0
@@ -69,10 +69,10 @@
 apache_airflow_provider = 
 	provider_info=airflow.providers.microsoft.azure.get_provider_info:get_provider_info
 
 [files]
 packages = airflow.providers.microsoft.azure
 
 [egg_info]
-tag_build = 
+tag_build = rc1
 tag_date = 0
```

### Comparing `apache-airflow-providers-microsoft-azure-5.3.0/setup.py` & `apache-airflow-providers-microsoft-azure-5.3.0rc1/setup.py`

 * *Files identical despite different names*

