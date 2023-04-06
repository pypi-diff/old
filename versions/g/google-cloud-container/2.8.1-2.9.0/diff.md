# Comparing `tmp/google-cloud-container-2.8.1.tar.gz` & `tmp/google-cloud-container-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/google-cloud-container-2.8.1.tar", last modified: Tue Oct  5 10:38:21 2021, max compression
+gzip compressed data, was "google-cloud-container-2.9.0.tar", last modified: Mon Oct 11 16:52:32 2021, max compression
```

## Comparing `google-cloud-container-2.8.1.tar` & `google-cloud-container-2.9.0.tar`

### file list

```diff
@@ -1,77 +1,77 @@
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/
--rw-rw-r--   0 root         (0)     1003    11358 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/LICENSE
--rw-rw-r--   0 root         (0)     1003      860 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/MANIFEST.in
--rw-r--r--   0 root         (0)     1003     3706 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/PKG-INFO
--rw-rw-r--   0 root         (0)     1003     2883 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/README.rst
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.539945 google-cloud-container-2.8.1/google/
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.539945 google-cloud-container-2.8.1/google/cloud/
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.543947 google-cloud-container-2.8.1/google/cloud/container/
--rw-rw-r--   0 root         (0)     1003    11177 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container/__init__.py
--rw-rw-r--   0 root         (0)     1003       77 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.543947 google-cloud-container-2.8.1/google/cloud/container_v1/
--rw-rw-r--   0 root         (0)     1003     8651 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003     8649 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/gapic_metadata.json
--rw-rw-r--   0 root         (0)     1003       77 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.543947 google-cloud-container-2.8.1/google/cloud/container_v1/services/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.543947 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/
--rw-rw-r--   0 root         (0)     1003      769 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/__init__.py
--rw-rw-r--   0 root         (0)     1003   147331 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/async_client.py
--rw-rw-r--   0 root         (0)     1003   158401 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/client.py
--rw-rw-r--   0 root         (0)     1003     6061 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/pagers.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.543947 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/
--rw-rw-r--   0 root         (0)     1003     1194 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/__init__.py
--rw-rw-r--   0 root         (0)     1003    24081 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/base.py
--rw-rw-r--   0 root         (0)     1003    48359 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/grpc.py
--rw-rw-r--   0 root         (0)     1003    49683 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/grpc_asyncio.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.547949 google-cloud-container-2.8.1/google/cloud/container_v1/types/
--rw-rw-r--   0 root         (0)     1003     5648 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/types/__init__.py
--rw-rw-r--   0 root         (0)     1003   159871 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1/types/cluster_service.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.547949 google-cloud-container-2.8.1/google/cloud/container_v1beta1/
--rw-rw-r--   0 root         (0)     1003    11565 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/__init__.py
--rw-rw-r--   0 root         (0)     1003     8903 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/gapic_metadata.json
--rw-rw-r--   0 root         (0)     1003       77 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.547949 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.547949 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/
--rw-rw-r--   0 root         (0)     1003      769 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/__init__.py
--rw-rw-r--   0 root         (0)     1003   151109 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/async_client.py
--rw-rw-r--   0 root         (0)     1003   162053 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/client.py
--rw-rw-r--   0 root         (0)     1003     6106 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/pagers.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.547949 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/
--rw-rw-r--   0 root         (0)     1003     1194 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/__init__.py
--rw-rw-r--   0 root         (0)     1003    25381 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/base.py
--rw-rw-r--   0 root         (0)     1003    49907 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc.py
--rw-rw-r--   0 root         (0)     1003    51262 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc_asyncio.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.547949 google-cloud-container-2.8.1/google/cloud/container_v1beta1/types/
--rw-rw-r--   0 root         (0)     1003     7422 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/types/__init__.py
--rw-rw-r--   0 root         (0)     1003   203821 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/google/cloud/container_v1beta1/types/cluster_service.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/google_cloud_container.egg-info/
--rw-r--r--   0 root         (0)     1003     3706 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/PKG-INFO
--rw-r--r--   0 root         (0)     1003     2536 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0)     1003        1 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0)     1003       20 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/namespace_packages.txt
--rw-r--r--   0 root         (0)     1003        1 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/not-zip-safe
--rw-r--r--   0 root         (0)     1003      125 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/requires.txt
--rw-r--r--   0 root         (0)     1003        7 2021-10-05 10:38:21.000000 google-cloud-container-2.8.1/google_cloud_container.egg-info/top_level.txt
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/scripts/
--rw-rw-r--   0 root         (0)     1003     8793 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/scripts/fixup_container_v1_keywords.py
--rw-rw-r--   0 root         (0)     1003     8909 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/scripts/fixup_container_v1beta1_keywords.py
--rw-rw-r--   0 root         (0)     1003       67 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/setup.cfg
--rw-rw-r--   0 root         (0)     1003     3037 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/setup.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/tests/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.539945 google-cloud-container-2.8.1/tests/system/
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.539945 google-cloud-container-2.8.1/tests/system/gapic/
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/tests/system/gapic/v1/
--rw-rw-r--   0 root         (0)     1003      971 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/system/gapic/v1/test_system_cluster_manager_v1.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/tests/unit/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/unit/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/tests/unit/gapic/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/unit/gapic/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/tests/unit/gapic/container_v1/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/unit/gapic/container_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003   365442 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/unit/gapic/container_v1/test_cluster_manager.py
-drwxr-sr-x   0 root         (0)     1003        0 2021-10-05 10:38:21.551951 google-cloud-container-2.8.1/tests/unit/gapic/container_v1beta1/
--rw-rw-r--   0 root         (0)     1003      600 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/unit/gapic/container_v1beta1/__init__.py
--rw-rw-r--   0 root         (0)     1003   381002 2021-10-05 10:35:44.000000 google-cloud-container-2.8.1/tests/unit/gapic/container_v1beta1/test_cluster_manager.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.891611 google-cloud-container-2.9.0/
+-rw-rw-r--   0 root         (0)     1003    11358 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/LICENSE
+-rw-rw-r--   0 root         (0)     1003      860 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/MANIFEST.in
+-rw-r--r--   0 root         (0)     1003     3706 2021-10-11 16:52:32.891611 google-cloud-container-2.9.0/PKG-INFO
+-rw-rw-r--   0 root         (0)     1003     2883 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/README.rst
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.875603 google-cloud-container-2.9.0/google/
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.875603 google-cloud-container-2.9.0/google/cloud/
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.879605 google-cloud-container-2.9.0/google/cloud/container/
+-rw-rw-r--   0 root         (0)     1003    11177 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container/__init__.py
+-rw-rw-r--   0 root         (0)     1003       77 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.879605 google-cloud-container-2.9.0/google/cloud/container_v1/
+-rw-rw-r--   0 root         (0)     1003     8651 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003     8649 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/gapic_metadata.json
+-rw-rw-r--   0 root         (0)     1003       77 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.879605 google-cloud-container-2.9.0/google/cloud/container_v1/services/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.879605 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/
+-rw-rw-r--   0 root         (0)     1003      769 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/__init__.py
+-rw-rw-r--   0 root         (0)     1003   147472 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/async_client.py
+-rw-rw-r--   0 root         (0)     1003   158649 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/client.py
+-rw-rw-r--   0 root         (0)     1003     6061 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/pagers.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.883607 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/
+-rw-rw-r--   0 root         (0)     1003     1194 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/__init__.py
+-rw-rw-r--   0 root         (0)     1003    24369 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/base.py
+-rw-rw-r--   0 root         (0)     1003    48415 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/grpc.py
+-rw-rw-r--   0 root         (0)     1003    49746 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/grpc_asyncio.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.883607 google-cloud-container-2.9.0/google/cloud/container_v1/types/
+-rw-rw-r--   0 root         (0)     1003     5648 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/types/__init__.py
+-rw-rw-r--   0 root         (0)     1003   159915 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1/types/cluster_service.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.883607 google-cloud-container-2.9.0/google/cloud/container_v1beta1/
+-rw-rw-r--   0 root         (0)     1003    11565 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/__init__.py
+-rw-rw-r--   0 root         (0)     1003     8903 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/gapic_metadata.json
+-rw-rw-r--   0 root         (0)     1003       77 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.883607 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.883607 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/
+-rw-rw-r--   0 root         (0)     1003      769 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/__init__.py
+-rw-rw-r--   0 root         (0)     1003   151250 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/async_client.py
+-rw-rw-r--   0 root         (0)     1003   162301 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/client.py
+-rw-rw-r--   0 root         (0)     1003     6106 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/pagers.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.883607 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/
+-rw-rw-r--   0 root         (0)     1003     1194 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/__init__.py
+-rw-rw-r--   0 root         (0)     1003    25669 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/base.py
+-rw-rw-r--   0 root         (0)     1003    49963 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc.py
+-rw-rw-r--   0 root         (0)     1003    51325 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc_asyncio.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/google/cloud/container_v1beta1/types/
+-rw-rw-r--   0 root         (0)     1003     7422 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/types/__init__.py
+-rw-rw-r--   0 root         (0)     1003   203890 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/google/cloud/container_v1beta1/types/cluster_service.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/google_cloud_container.egg-info/
+-rw-r--r--   0 root         (0)     1003     3706 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0)     1003     2536 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0)     1003        1 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0)     1003       20 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/namespace_packages.txt
+-rw-r--r--   0 root         (0)     1003        1 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0)     1003      125 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/requires.txt
+-rw-r--r--   0 root         (0)     1003        7 2021-10-11 16:52:32.000000 google-cloud-container-2.9.0/google_cloud_container.egg-info/top_level.txt
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/scripts/
+-rw-rw-r--   0 root         (0)     1003     8793 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/scripts/fixup_container_v1_keywords.py
+-rw-rw-r--   0 root         (0)     1003     8909 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/scripts/fixup_container_v1beta1_keywords.py
+-rw-rw-r--   0 root         (0)     1003       67 2021-10-11 16:52:32.891611 google-cloud-container-2.9.0/setup.cfg
+-rw-rw-r--   0 root         (0)     1003     3037 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/setup.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/tests/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.879605 google-cloud-container-2.9.0/tests/system/
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.879605 google-cloud-container-2.9.0/tests/system/gapic/
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/tests/system/gapic/v1/
+-rw-rw-r--   0 root         (0)     1003      971 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/system/gapic/v1/test_system_cluster_manager_v1.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/tests/unit/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/unit/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/tests/unit/gapic/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/unit/gapic/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/tests/unit/gapic/container_v1/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/unit/gapic/container_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003   366929 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/unit/gapic/container_v1/test_cluster_manager.py
+drwxr-sr-x   0 root         (0)     1003        0 2021-10-11 16:52:32.887609 google-cloud-container-2.9.0/tests/unit/gapic/container_v1beta1/
+-rw-rw-r--   0 root         (0)     1003      600 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/unit/gapic/container_v1beta1/__init__.py
+-rw-rw-r--   0 root         (0)     1003   382489 2021-10-11 16:49:45.000000 google-cloud-container-2.9.0/tests/unit/gapic/container_v1beta1/test_cluster_manager.py
```

### Comparing `google-cloud-container-2.8.1/LICENSE` & `google-cloud-container-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/MANIFEST.in` & `google-cloud-container-2.9.0/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/PKG-INFO` & `google-cloud-container-2.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: google-cloud-container
-Version: 2.8.1
+Version: 2.9.0
 Summary: Google Container Engine API client library
 Home-page: https://github.com/googleapis/python-container
 Author: Google LLC
 Author-email: googleapis-packages@google.com
 License: Apache 2.0
 Platform: Posix; MacOS X; Windows
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `google-cloud-container-2.8.1/README.rst` & `google-cloud-container-2.9.0/README.rst`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/gapic_metadata.json` & `google-cloud-container-2.9.0/google/cloud/container_v1/gapic_metadata.json`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/async_client.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/async_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -3487,14 +3487,20 @@
         response = pagers.ListUsableSubnetworksAsyncPager(
             method=rpc, request=request, response=response, metadata=metadata,
         )
 
         # Done; return the response.
         return response
 
+    async def __aenter__(self):
+        return self
+
+    async def __aexit__(self, exc_type, exc, tb):
+        await self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         gapic_version=pkg_resources.get_distribution("google-cloud-container",).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/client.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -325,18 +325,15 @@
                 credentials=credentials,
                 credentials_file=client_options.credentials_file,
                 host=api_endpoint,
                 scopes=client_options.scopes,
                 client_cert_source_for_mtls=client_cert_source_func,
                 quota_project_id=client_options.quota_project_id,
                 client_info=client_info,
-                always_use_jwt_access=(
-                    Transport == type(self).get_transport_class("grpc")
-                    or Transport == type(self).get_transport_class("grpc_asyncio")
-                ),
+                always_use_jwt_access=True,
             )
 
     def list_clusters(
         self,
         request: Union[cluster_service.ListClustersRequest, dict] = None,
         *,
         project_id: str = None,
@@ -3584,14 +3581,27 @@
         response = pagers.ListUsableSubnetworksPager(
             method=rpc, request=request, response=response, metadata=metadata,
         )
 
         # Done; return the response.
         return response
 
+    def __enter__(self):
+        return self
+
+    def __exit__(self, type, value, traceback):
+        """Releases underlying transport's resources.
+
+        .. warning::
+            ONLY use as a context manager if the transport is NOT shared
+            with other clients! Exiting the with block will CLOSE the transport
+            and may cause errors in other clients!
+        """
+        self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         gapic_version=pkg_resources.get_distribution("google-cloud-container",).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/pagers.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/pagers.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/base.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/base.py`

 * *Files 1% similar despite different names*

```diff
@@ -369,14 +369,23 @@
             self.list_usable_subnetworks: gapic_v1.method.wrap_method(
                 self.list_usable_subnetworks,
                 default_timeout=None,
                 client_info=client_info,
             ),
         }
 
+    def close(self):
+        """Closes resources associated with the transport.
+
+       .. warning::
+            Only call this method if the transport is NOT shared
+            with other clients - this may cause errors in other clients!
+        """
+        raise NotImplementedError()
+
     @property
     def list_clusters(
         self,
     ) -> Callable[
         [cluster_service.ListClustersRequest],
         Union[
             cluster_service.ListClustersResponse,
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/grpc.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/grpc.py`

 * *Files 0% similar despite different names*

```diff
@@ -1119,9 +1119,12 @@
             self._stubs["list_usable_subnetworks"] = self.grpc_channel.unary_unary(
                 "/google.container.v1.ClusterManager/ListUsableSubnetworks",
                 request_serializer=cluster_service.ListUsableSubnetworksRequest.serialize,
                 response_deserializer=cluster_service.ListUsableSubnetworksResponse.deserialize,
             )
         return self._stubs["list_usable_subnetworks"]
 
+    def close(self):
+        self.grpc_channel.close()
+
 
 __all__ = ("ClusterManagerGrpcTransport",)
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/services/cluster_manager/transports/grpc_asyncio.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/services/cluster_manager/transports/grpc_asyncio.py`

 * *Files 0% similar despite different names*

```diff
@@ -1169,9 +1169,12 @@
             self._stubs["list_usable_subnetworks"] = self.grpc_channel.unary_unary(
                 "/google.container.v1.ClusterManager/ListUsableSubnetworks",
                 request_serializer=cluster_service.ListUsableSubnetworksRequest.serialize,
                 response_deserializer=cluster_service.ListUsableSubnetworksResponse.deserialize,
             )
         return self._stubs["list_usable_subnetworks"]
 
+    def close(self):
+        return self.grpc_channel.close()
+
 
 __all__ = ("ClusterManagerGrpcAsyncIOTransport",)
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/types/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/types/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1/types/cluster_service.py` & `google-cloud-container-2.9.0/google/cloud/container_v1/types/cluster_service.py`

 * *Files 1% similar despite different names*

```diff
@@ -118,14 +118,15 @@
         "ShieldedNodes",
     },
 )
 
 
 class NodeConfig(proto.Message):
     r"""Parameters that describe the nodes in a cluster.
+
     Attributes:
         machine_type (str):
             The name of a Google Compute Engine `machine
             type <https://cloud.google.com/compute/docs/machine-types>`__
 
             If unspecified, the default machine type is ``e2-medium``.
         disk_size_gb (int):
@@ -316,14 +317,15 @@
         proto.MESSAGE, number=20, message="ShieldedInstanceConfig",
     )
     boot_disk_kms_key = proto.Field(proto.STRING, number=23,)
 
 
 class ShieldedInstanceConfig(proto.Message):
     r"""A set of Shielded Instance options.
+
     Attributes:
         enable_secure_boot (bool):
             Defines whether the instance has Secure Boot
             enabled.
             Secure Boot helps ensure that the system only
             runs authentic software by verifying the digital
             signature of all boot components, and halting
@@ -480,14 +482,15 @@
     cluster_ca_certificate = proto.Field(proto.STRING, number=100,)
     client_certificate = proto.Field(proto.STRING, number=101,)
     client_key = proto.Field(proto.STRING, number=102,)
 
 
 class ClientCertificateConfig(proto.Message):
     r"""Configuration for client certificates on the cluster.
+
     Attributes:
         issue_client_certificate (bool):
             Issue a client certificate.
     """
 
     issue_client_certificate = proto.Field(proto.BOOL, number=1,)
 
@@ -585,14 +588,15 @@
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
 
 
 class KubernetesDashboard(proto.Message):
     r"""Configuration for the Kubernetes Dashboard.
+
     Attributes:
         disabled (bool):
             Whether the Kubernetes Dashboard is enabled
             for this cluster.
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
@@ -610,36 +614,39 @@
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
 
 
 class DnsCacheConfig(proto.Message):
     r"""Configuration for NodeLocal DNSCache
+
     Attributes:
         enabled (bool):
             Whether NodeLocal DNSCache is enabled for
             this cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class PrivateClusterMasterGlobalAccessConfig(proto.Message):
     r"""Configuration for controlling master global access settings.
+
     Attributes:
         enabled (bool):
             Whenever master is accessible globally or
             not.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class PrivateClusterConfig(proto.Message):
     r"""Configuration options for private clusters.
+
     Attributes:
         enable_private_nodes (bool):
             Whether nodes have internal IP addresses
             only. If enabled, all nodes are given only RFC
             1918 private addresses and communicate with the
             master via private networking.
         enable_private_endpoint (bool):
@@ -692,14 +699,15 @@
 
     enabled = proto.Field(proto.BOOL, number=1,)
     security_group = proto.Field(proto.STRING, number=2,)
 
 
 class CloudRunConfig(proto.Message):
     r"""Configuration options for the Cloud Run feature.
+
     Attributes:
         disabled (bool):
             Whether Cloud Run addon is enabled for this
             cluster.
         load_balancer_type (google.cloud.container_v1.types.CloudRunConfig.LoadBalancerType):
             Which load balancer type is installed for
             Cloud Run.
@@ -713,14 +721,15 @@
 
     disabled = proto.Field(proto.BOOL, number=1,)
     load_balancer_type = proto.Field(proto.ENUM, number=3, enum=LoadBalancerType,)
 
 
 class ConfigConnectorConfig(proto.Message):
     r"""Configuration options for the Config Connector add-on.
+
     Attributes:
         enabled (bool):
             Whether Cloud Connector is enabled for this
             cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
@@ -740,14 +749,15 @@
         cidr_blocks (Sequence[google.cloud.container_v1.types.MasterAuthorizedNetworksConfig.CidrBlock]):
             cidr_blocks define up to 50 external networks that could
             access Kubernetes master through HTTPS.
     """
 
     class CidrBlock(proto.Message):
         r"""CidrBlock contains an optional name and one CIDR block.
+
         Attributes:
             display_name (str):
                 display_name is an optional field for users to identify CIDR
                 blocks.
             cidr_block (str):
                 cidr_block must be specified in CIDR notation.
         """
@@ -796,14 +806,15 @@
 
     provider = proto.Field(proto.ENUM, number=1, enum=Provider,)
     enabled = proto.Field(proto.BOOL, number=2,)
 
 
 class BinaryAuthorization(proto.Message):
     r"""Configuration for Binary Authorization.
+
     Attributes:
         enabled (bool):
             Enable Binary Authorization for this cluster.
             If enabled, all container images will be
             validated by Binary Authorization.
     """
 
@@ -943,14 +954,15 @@
     services_ipv4_cidr_block = proto.Field(proto.STRING, number=11,)
     tpu_ipv4_cidr_block = proto.Field(proto.STRING, number=13,)
     use_routes = proto.Field(proto.BOOL, number=15,)
 
 
 class Cluster(proto.Message):
     r"""A Google Kubernetes Engine cluster.
+
     Attributes:
         name (str):
             The name of this cluster. The name must be unique within
             this project and location (e.g. zone or region), and can be
             up to 40 characters with the following restrictions:
 
             -  Lowercase letters, numbers, and hyphens only.
@@ -1571,14 +1583,15 @@
     nodepool_conditions = proto.RepeatedField(
         proto.MESSAGE, number=14, message="StatusCondition",
     )
 
 
 class OperationProgress(proto.Message):
     r"""Information about operation (or operation stage) progress.
+
     Attributes:
         name (str):
             A non-parameterized string describing an
             operation stage. Unset for single-stage
             operations.
         status (google.cloud.container_v1.types.Operation.Status):
             Status of an operation stage.
@@ -1590,14 +1603,15 @@
             "progress scale", double_value: 1.0}]
         stages (Sequence[google.cloud.container_v1.types.OperationProgress]):
             Substages of an operation or a stage.
     """
 
     class Metric(proto.Message):
         r"""Progress metric is (string, int|float|string) pair.
+
         Attributes:
             name (str):
                 Required. Metric name, e.g., "nodes total",
                 "percent done".
             int_value (int):
                 For metrics with integer value.
             double_value (float):
@@ -1616,14 +1630,15 @@
     status = proto.Field(proto.ENUM, number=2, enum="Operation.Status",)
     metrics = proto.RepeatedField(proto.MESSAGE, number=3, message=Metric,)
     stages = proto.RepeatedField(proto.MESSAGE, number=4, message="OperationProgress",)
 
 
 class CreateClusterRequest(proto.Message):
     r"""CreateClusterRequest creates a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -1644,14 +1659,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster = proto.Field(proto.MESSAGE, number=3, message="Cluster",)
     parent = proto.Field(proto.STRING, number=5,)
 
 
 class GetClusterRequest(proto.Message):
     r"""GetClusterRequest gets the settings of a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -1674,14 +1690,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=5,)
 
 
 class UpdateClusterRequest(proto.Message):
     r"""UpdateClusterRequest updates the settings of a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -1955,14 +1972,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     addons_config = proto.Field(proto.MESSAGE, number=4, message="AddonsConfig",)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class SetLocationsRequest(proto.Message):
     r"""SetLocationsRequest sets the locations of the cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -1995,14 +2013,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     locations = proto.RepeatedField(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class UpdateMasterRequest(proto.Message):
     r"""UpdateMasterRequest updates the master of the cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2039,14 +2058,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     master_version = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class SetMasterAuthRequest(proto.Message):
     r"""SetMasterAuthRequest updates the admin password of a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2083,14 +2103,15 @@
     action = proto.Field(proto.ENUM, number=4, enum=Action,)
     update = proto.Field(proto.MESSAGE, number=5, message="MasterAuth",)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class DeleteClusterRequest(proto.Message):
     r"""DeleteClusterRequest deletes a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2113,14 +2134,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=4,)
 
 
 class ListClustersRequest(proto.Message):
     r"""ListClustersRequest lists clusters.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2138,14 +2160,15 @@
     project_id = proto.Field(proto.STRING, number=1,)
     zone = proto.Field(proto.STRING, number=2,)
     parent = proto.Field(proto.STRING, number=4,)
 
 
 class ListClustersResponse(proto.Message):
     r"""ListClustersResponse is the result of ListClustersRequest.
+
     Attributes:
         clusters (Sequence[google.cloud.container_v1.types.Cluster]):
             A list of clusters in the project in the
             specified zone, or across all ones.
         missing_zones (Sequence[str]):
             If any zones are listed here, the list of
             clusters returned may be missing those zones.
@@ -2153,14 +2176,15 @@
 
     clusters = proto.RepeatedField(proto.MESSAGE, number=1, message="Cluster",)
     missing_zones = proto.RepeatedField(proto.STRING, number=2,)
 
 
 class GetOperationRequest(proto.Message):
     r"""GetOperationRequest gets a single operation.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2183,14 +2207,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     operation_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=5,)
 
 
 class ListOperationsRequest(proto.Message):
     r"""ListOperationsRequest lists operations.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2209,14 +2234,15 @@
     project_id = proto.Field(proto.STRING, number=1,)
     zone = proto.Field(proto.STRING, number=2,)
     parent = proto.Field(proto.STRING, number=4,)
 
 
 class CancelOperationRequest(proto.Message):
     r"""CancelOperationRequest cancels a single operation.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2257,14 +2283,15 @@
 
     operations = proto.RepeatedField(proto.MESSAGE, number=1, message="Operation",)
     missing_zones = proto.RepeatedField(proto.STRING, number=2,)
 
 
 class GetServerConfigRequest(proto.Message):
     r"""Gets the current Kubernetes Engine service configuration.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2281,14 +2308,15 @@
     project_id = proto.Field(proto.STRING, number=1,)
     zone = proto.Field(proto.STRING, number=2,)
     name = proto.Field(proto.STRING, number=4,)
 
 
 class ServerConfig(proto.Message):
     r"""Kubernetes Engine service configuration.
+
     Attributes:
         default_cluster_version (str):
             Version of Kubernetes the service deploys by
             default.
         valid_node_versions (Sequence[str]):
             List of valid node upgrade target versions,
             in descending order.
@@ -2330,14 +2358,15 @@
     channels = proto.RepeatedField(
         proto.MESSAGE, number=9, message=ReleaseChannelConfig,
     )
 
 
 class CreateNodePoolRequest(proto.Message):
     r"""CreateNodePoolRequest creates a node pool for a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2363,14 +2392,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     node_pool = proto.Field(proto.MESSAGE, number=4, message="NodePool",)
     parent = proto.Field(proto.STRING, number=6,)
 
 
 class DeleteNodePoolRequest(proto.Message):
     r"""DeleteNodePoolRequest deletes a node pool for a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2398,14 +2428,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     node_pool_id = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class ListNodePoolsRequest(proto.Message):
     r"""ListNodePoolsRequest lists the node pool(s) for a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2428,14 +2459,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     parent = proto.Field(proto.STRING, number=5,)
 
 
 class GetNodePoolRequest(proto.Message):
     r"""GetNodePoolRequest retrieves a node pool for a cluster.
+
     Attributes:
         project_id (str):
             Deprecated. The Google Developers Console `project ID or
             project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2703,28 +2735,30 @@
     maintenance_exclusions = proto.MapField(
         proto.STRING, proto.MESSAGE, number=4, message="TimeWindow",
     )
 
 
 class TimeWindow(proto.Message):
     r"""Represents an arbitrary window of time.
+
     Attributes:
         start_time (google.protobuf.timestamp_pb2.Timestamp):
             The time that the window first starts.
         end_time (google.protobuf.timestamp_pb2.Timestamp):
             The time that the window ends. The end time
             should take place after the start time.
     """
 
     start_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
     end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
 
 
 class RecurringTimeWindow(proto.Message):
     r"""Represents an arbitrary window of time that recurs.
+
     Attributes:
         window (google.cloud.container_v1.types.TimeWindow):
             The window of the first recurrence.
         recurrence (str):
             An RRULE
             (https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for
             how this window reccurs. They go on for the span of time
@@ -2767,14 +2801,15 @@
 
     window = proto.Field(proto.MESSAGE, number=1, message="TimeWindow",)
     recurrence = proto.Field(proto.STRING, number=2,)
 
 
 class DailyMaintenanceWindow(proto.Message):
     r"""Time window specified for daily maintenance operations.
+
     Attributes:
         start_time (str):
             Time within the maintenance window to start the maintenance
             operations. Time format should be in
             `RFC3339 <https://www.ietf.org/rfc/rfc3339.txt>`__ format
             "HH:MM", where HH : [00-23] and MM : [00-59] GMT.
         duration (str):
@@ -2907,14 +2942,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     node_pool_id = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class ListNodePoolsResponse(proto.Message):
     r"""ListNodePoolsResponse is the result of ListNodePoolsRequest.
+
     Attributes:
         node_pools (Sequence[google.cloud.container_v1.types.NodePool]):
             A list of node pools for a cluster.
     """
 
     node_pools = proto.RepeatedField(proto.MESSAGE, number=1, message="NodePool",)
 
@@ -3213,14 +3249,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class AcceleratorConfig(proto.Message):
     r"""AcceleratorConfig represents a Hardware Accelerator request.
+
     Attributes:
         accelerator_count (int):
             The number of the accelerator cards exposed
             to an instance.
         accelerator_type (str):
             The accelerator type resource name. List of supported
             accelerators
@@ -3443,14 +3480,15 @@
     """
 
     parent = proto.Field(proto.STRING, number=1,)
 
 
 class Jwk(proto.Message):
     r"""Jwk is a JSON Web Key as specified in RFC 7517
+
     Attributes:
         kty (str):
             Key Type.
         alg (str):
             Algorithm.
         use (str):
             Permitted uses for the public keys.
@@ -3526,14 +3564,15 @@
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class MaxPodsConstraint(proto.Message):
     r"""Constraints applied to pods.
+
     Attributes:
         max_pods_per_node (int):
             Constraint enforced on the max num of pods
             per node.
     """
 
     max_pods_per_node = proto.Field(proto.INT64, number=1,)
@@ -3550,14 +3589,15 @@
     """
 
     workload_pool = proto.Field(proto.STRING, number=2,)
 
 
 class DatabaseEncryption(proto.Message):
     r"""Configuration of etcd encryption.
+
     Attributes:
         state (google.cloud.container_v1.types.DatabaseEncryption.State):
             Denotes the state of etcd encryption.
         key_name (str):
             Name of CloudKMS key to use for the
             encryption of secrets in etcd. Ex. projects/my-
             project/locations/global/keyRings/my-
@@ -3631,14 +3671,15 @@
         proto.MESSAGE, number=1, message="UsableSubnetwork",
     )
     next_page_token = proto.Field(proto.STRING, number=2,)
 
 
 class UsableSubnetworkSecondaryRange(proto.Message):
     r"""Secondary IP range of a usable subnetwork.
+
     Attributes:
         range_name (str):
             The name associated with this subnetwork
             secondary range, used when adding an alias IP
             range to a VM instance.
         ip_cidr_range (str):
             The range of IP addresses belonging to this
@@ -3694,14 +3735,15 @@
         proto.MESSAGE, number=4, message="UsableSubnetworkSecondaryRange",
     )
     status_message = proto.Field(proto.STRING, number=5,)
 
 
 class ResourceUsageExportConfig(proto.Message):
     r"""Configuration for exporting cluster resource usages.
+
     Attributes:
         bigquery_destination (google.cloud.container_v1.types.ResourceUsageExportConfig.BigQueryDestination):
             Configuration to use BigQuery as usage export
             destination.
         enable_network_egress_metering (bool):
             Whether to enable network egress metering for
             this cluster. If enabled, a daemonset will be
@@ -3721,14 +3763,15 @@
                 The ID of a BigQuery Dataset.
         """
 
         dataset_id = proto.Field(proto.STRING, number=1,)
 
     class ConsumptionMeteringConfig(proto.Message):
         r"""Parameters for controlling consumption metering.
+
         Attributes:
             enabled (bool):
                 Whether to enable consumption metering for
                 this cluster. If enabled, a second BigQuery
                 table will be created to hold resource
                 consumption records.
         """
@@ -3767,14 +3810,15 @@
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
 
 
 class ShieldedNodes(proto.Message):
     r"""Configuration of Shielded Nodes feature.
+
     Attributes:
         enabled (bool):
             Whether Shielded Nodes features are enabled
             on all nodes in this cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/gapic_metadata.json` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/gapic_metadata.json`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/async_client.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/async_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -3559,14 +3559,20 @@
 
         # Send the request.
         response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    async def __aenter__(self):
+        return self
+
+    async def __aexit__(self, exc_type, exc, tb):
+        await self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         gapic_version=pkg_resources.get_distribution("google-cloud-container",).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/client.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -337,18 +337,15 @@
                 credentials=credentials,
                 credentials_file=client_options.credentials_file,
                 host=api_endpoint,
                 scopes=client_options.scopes,
                 client_cert_source_for_mtls=client_cert_source_func,
                 quota_project_id=client_options.quota_project_id,
                 client_info=client_info,
-                always_use_jwt_access=(
-                    Transport == type(self).get_transport_class("grpc")
-                    or Transport == type(self).get_transport_class("grpc_asyncio")
-                ),
+                always_use_jwt_access=True,
             )
 
     def list_clusters(
         self,
         request: Union[cluster_service.ListClustersRequest, dict] = None,
         *,
         project_id: str = None,
@@ -3641,14 +3638,27 @@
 
         # Send the request.
         response = rpc(request, retry=retry, timeout=timeout, metadata=metadata,)
 
         # Done; return the response.
         return response
 
+    def __enter__(self):
+        return self
+
+    def __exit__(self, type, value, traceback):
+        """Releases underlying transport's resources.
+
+        .. warning::
+            ONLY use as a context manager if the transport is NOT shared
+            with other clients! Exiting the with block will CLOSE the transport
+            and may cause errors in other clients!
+        """
+        self.transport.close()
+
 
 try:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
         gapic_version=pkg_resources.get_distribution("google-cloud-container",).version,
     )
 except pkg_resources.DistributionNotFound:
     DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/pagers.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/pagers.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/base.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/base.py`

 * *Files 1% similar despite different names*

```diff
@@ -394,14 +394,23 @@
                     deadline=20.0,
                 ),
                 default_timeout=20.0,
                 client_info=client_info,
             ),
         }
 
+    def close(self):
+        """Closes resources associated with the transport.
+
+       .. warning::
+            Only call this method if the transport is NOT shared
+            with other clients - this may cause errors in other clients!
+        """
+        raise NotImplementedError()
+
     @property
     def list_clusters(
         self,
     ) -> Callable[
         [cluster_service.ListClustersRequest],
         Union[
             cluster_service.ListClustersResponse,
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc.py`

 * *Files 0% similar despite different names*

```diff
@@ -1151,9 +1151,12 @@
             self._stubs["list_locations"] = self.grpc_channel.unary_unary(
                 "/google.container.v1beta1.ClusterManager/ListLocations",
                 request_serializer=cluster_service.ListLocationsRequest.serialize,
                 response_deserializer=cluster_service.ListLocationsResponse.deserialize,
             )
         return self._stubs["list_locations"]
 
+    def close(self):
+        self.grpc_channel.close()
+
 
 __all__ = ("ClusterManagerGrpcTransport",)
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc_asyncio.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/services/cluster_manager/transports/grpc_asyncio.py`

 * *Files 1% similar despite different names*

```diff
@@ -1202,9 +1202,12 @@
             self._stubs["list_locations"] = self.grpc_channel.unary_unary(
                 "/google.container.v1beta1.ClusterManager/ListLocations",
                 request_serializer=cluster_service.ListLocationsRequest.serialize,
                 response_deserializer=cluster_service.ListLocationsResponse.deserialize,
             )
         return self._stubs["list_locations"]
 
+    def close(self):
+        return self.grpc_channel.close()
+
 
 __all__ = ("ClusterManagerGrpcAsyncIOTransport",)
```

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/types/__init__.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/types/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/google/cloud/container_v1beta1/types/cluster_service.py` & `google-cloud-container-2.9.0/google/cloud/container_v1beta1/types/cluster_service.py`

 * *Files 1% similar despite different names*

```diff
@@ -189,14 +189,15 @@
     UPGRADE_RESOURCE_TYPE_UNSPECIFIED = 0
     MASTER = 1
     NODE_POOL = 2
 
 
 class LinuxNodeConfig(proto.Message):
     r"""Parameters that can be configured on Linux nodes.
+
     Attributes:
         sysctls (Sequence[google.cloud.container_v1beta1.types.LinuxNodeConfig.SysctlsEntry]):
             The Linux kernel parameters to be applied to the nodes and
             all pods running on the nodes.
 
             The following parameters are supported.
 
@@ -207,14 +208,15 @@
     """
 
     sysctls = proto.MapField(proto.STRING, proto.STRING, number=1,)
 
 
 class NodeKubeletConfig(proto.Message):
     r"""Node kubelet configs.
+
     Attributes:
         cpu_manager_policy (str):
             Control the CPU management policy on the
             node. See
             https://kubernetes.io/docs/tasks/administer-
             cluster/cpu-management-policies/
             The following values are allowed.
@@ -254,14 +256,15 @@
         proto.MESSAGE, number=2, message=wrappers_pb2.BoolValue,
     )
     cpu_cfs_quota_period = proto.Field(proto.STRING, number=3,)
 
 
 class NodeConfig(proto.Message):
     r"""Parameters that describe the nodes in a cluster.
+
     Attributes:
         machine_type (str):
             The name of a Google Compute Engine `machine
             type <https://cloud.google.com/compute/docs/machine-types>`__.
 
             If unspecified, the default machine type is ``e2-medium``.
         disk_size_gb (int):
@@ -467,14 +470,15 @@
         proto.MESSAGE, number=24, message="EphemeralStorageConfig",
     )
     gvnic = proto.Field(proto.MESSAGE, number=29, message="VirtualNIC",)
 
 
 class NodeNetworkConfig(proto.Message):
     r"""Parameters for node pool-level network config.
+
     Attributes:
         create_pod_range (bool):
             Input only. Whether to create a new range for pod IPs in
             this node pool. Defaults are provided for ``pod_range`` and
             ``pod_ipv4_cidr_block`` if they are not specified.
 
             If neither ``create_pod_range`` or ``pod_range`` are
@@ -522,14 +526,15 @@
     create_pod_range = proto.Field(proto.BOOL, number=4,)
     pod_range = proto.Field(proto.STRING, number=5,)
     pod_ipv4_cidr_block = proto.Field(proto.STRING, number=6,)
 
 
 class ShieldedInstanceConfig(proto.Message):
     r"""A set of Shielded Instance options.
+
     Attributes:
         enable_secure_boot (bool):
             Defines whether the instance has Secure Boot
             enabled.
             Secure Boot helps ensure that the system only
             runs authentic software by verifying the digital
             signature of all boot components, and halting
@@ -741,14 +746,15 @@
     cluster_ca_certificate = proto.Field(proto.STRING, number=100,)
     client_certificate = proto.Field(proto.STRING, number=101,)
     client_key = proto.Field(proto.STRING, number=102,)
 
 
 class ClientCertificateConfig(proto.Message):
     r"""Configuration for client certificates on the cluster.
+
     Attributes:
         issue_client_certificate (bool):
             Issue a client certificate.
     """
 
     issue_client_certificate = proto.Field(proto.BOOL, number=1,)
 
@@ -860,14 +866,15 @@
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
 
 
 class KubernetesDashboard(proto.Message):
     r"""Configuration for the Kubernetes Dashboard.
+
     Attributes:
         disabled (bool):
             Whether the Kubernetes Dashboard is enabled
             for this cluster.
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
@@ -885,68 +892,74 @@
     """
 
     disabled = proto.Field(proto.BOOL, number=1,)
 
 
 class DnsCacheConfig(proto.Message):
     r"""Configuration for NodeLocal DNSCache
+
     Attributes:
         enabled (bool):
             Whether NodeLocal DNSCache is enabled for
             this cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class KalmConfig(proto.Message):
     r"""Configuration options for the KALM addon.
+
     Attributes:
         enabled (bool):
             Whether KALM is enabled for this cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class ConfigConnectorConfig(proto.Message):
     r"""Configuration options for the Config Connector add-on.
+
     Attributes:
         enabled (bool):
             Whether Cloud Connector is enabled for this
             cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class GcePersistentDiskCsiDriverConfig(proto.Message):
     r"""Configuration for the Compute Engine PD CSI driver.
+
     Attributes:
         enabled (bool):
             Whether the Compute Engine PD CSI driver is
             enabled for this cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class PrivateClusterMasterGlobalAccessConfig(proto.Message):
     r"""Configuration for controlling master global access settings.
+
     Attributes:
         enabled (bool):
             Whenever master is accessible globally or
             not.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class PrivateClusterConfig(proto.Message):
     r"""Configuration options for private clusters.
+
     Attributes:
         enable_private_nodes (bool):
             Whether nodes have internal IP addresses
             only. If enabled, all nodes are given only RFC
             1918 private addresses and communicate with the
             master via private networking.
         enable_private_endpoint (bool):
@@ -981,14 +994,15 @@
     master_global_access_config = proto.Field(
         proto.MESSAGE, number=8, message="PrivateClusterMasterGlobalAccessConfig",
     )
 
 
 class IstioConfig(proto.Message):
     r"""Configuration options for Istio addon.
+
     Attributes:
         disabled (bool):
             Whether Istio is enabled for this cluster.
         auth (google.cloud.container_v1beta1.types.IstioConfig.IstioAuthMode):
             The specified Istio auth mode, either none,
             or mutual TLS.
     """
@@ -1002,14 +1016,15 @@
 
     disabled = proto.Field(proto.BOOL, number=1,)
     auth = proto.Field(proto.ENUM, number=2, enum=IstioAuthMode,)
 
 
 class CloudRunConfig(proto.Message):
     r"""Configuration options for the Cloud Run feature.
+
     Attributes:
         disabled (bool):
             Whether Cloud Run addon is enabled for this
             cluster.
         load_balancer_type (google.cloud.container_v1beta1.types.CloudRunConfig.LoadBalancerType):
             Which load balancer type is installed for
             Cloud Run.
@@ -1039,14 +1054,15 @@
         cidr_blocks (Sequence[google.cloud.container_v1beta1.types.MasterAuthorizedNetworksConfig.CidrBlock]):
             cidr_blocks define up to 10 external networks that could
             access Kubernetes master through HTTPS.
     """
 
     class CidrBlock(proto.Message):
         r"""CidrBlock contains an optional name and one CIDR block.
+
         Attributes:
             display_name (str):
                 display_name is an optional field for users to identify CIDR
                 blocks.
             cidr_block (str):
                 cidr_block must be specified in CIDR notation.
         """
@@ -1250,26 +1266,28 @@
     allow_route_overlap = proto.Field(proto.BOOL, number=12,)
     tpu_ipv4_cidr_block = proto.Field(proto.STRING, number=13,)
     use_routes = proto.Field(proto.BOOL, number=15,)
 
 
 class BinaryAuthorization(proto.Message):
     r"""Configuration for Binary Authorization.
+
     Attributes:
         enabled (bool):
             Enable Binary Authorization for this cluster.
             If enabled, all container images will be
             validated by Google Binauthz.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class PodSecurityPolicyConfig(proto.Message):
     r"""Configuration for the PodSecurityPolicy feature.
+
     Attributes:
         enabled (bool):
             Enable the PodSecurityPolicy controller for
             this cluster. If enabled, pods must be valid
             under a PodSecurityPolicy to be created.
     """
 
@@ -1292,14 +1310,15 @@
 
     enabled = proto.Field(proto.BOOL, number=1,)
     security_group = proto.Field(proto.STRING, number=2,)
 
 
 class ClusterTelemetry(proto.Message):
     r"""Telemetry integration for the cluster.
+
     Attributes:
         type_ (google.cloud.container_v1beta1.types.ClusterTelemetry.Type):
             Type of the integration.
     """
 
     class Type(proto.Enum):
         r"""Type of the integration."""
@@ -1309,14 +1328,15 @@
         SYSTEM_ONLY = 3
 
     type_ = proto.Field(proto.ENUM, number=1, enum=Type,)
 
 
 class Cluster(proto.Message):
     r"""A Google Kubernetes Engine cluster.
+
     Attributes:
         name (str):
             The name of this cluster. The name must be unique within
             this project and location (e.g. zone or region), and can be
             up to 40 characters with the following restrictions:
 
             -  Lowercase letters, numbers, and hyphens only.
@@ -1736,27 +1756,29 @@
     monitoring_config = proto.Field(
         proto.MESSAGE, number=133, message="MonitoringConfig",
     )
 
 
 class NodePoolDefaults(proto.Message):
     r"""Subset of Nodepool message that has defaults.
+
     Attributes:
         node_config_defaults (google.cloud.container_v1beta1.types.NodeConfigDefaults):
             Subset of NodeConfig message that has
             defaults.
     """
 
     node_config_defaults = proto.Field(
         proto.MESSAGE, number=1, message="NodeConfigDefaults",
     )
 
 
 class NodeConfigDefaults(proto.Message):
-    r"""Subset of NodeConfig message that has defaults.    """
+    r"""Subset of NodeConfig message that has defaults.
+    """
 
 
 class ClusterUpdate(proto.Message):
     r"""ClusterUpdate describes an update to the cluster. Exactly one
     update can be applied to a cluster with each request, so at most
     one field can be provided.
 
@@ -2109,14 +2131,15 @@
         proto.MESSAGE, number=14, message="StatusCondition",
     )
     error = proto.Field(proto.MESSAGE, number=15, message=status_pb2.Status,)
 
 
 class OperationProgress(proto.Message):
     r"""Information about operation (or operation stage) progress.
+
     Attributes:
         name (str):
             A non-parameterized string describing an
             operation stage. Unset for single-stage
             operations.
         status (google.cloud.container_v1beta1.types.Operation.Status):
             Status of an operation stage.
@@ -2128,14 +2151,15 @@
             "progress scale", double_value: 1.0}]
         stages (Sequence[google.cloud.container_v1beta1.types.OperationProgress]):
             Substages of an operation or a stage.
     """
 
     class Metric(proto.Message):
         r"""Progress metric is (string, int|float|string) pair.
+
         Attributes:
             name (str):
                 Required. Metric name, e.g., "nodes total",
                 "percent done".
             int_value (int):
                 For metrics with integer value.
             double_value (float):
@@ -2154,14 +2178,15 @@
     status = proto.Field(proto.ENUM, number=2, enum="Operation.Status",)
     metrics = proto.RepeatedField(proto.MESSAGE, number=3, message=Metric,)
     stages = proto.RepeatedField(proto.MESSAGE, number=4, message="OperationProgress",)
 
 
 class CreateClusterRequest(proto.Message):
     r"""CreateClusterRequest creates a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2182,14 +2207,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster = proto.Field(proto.MESSAGE, number=3, message="Cluster",)
     parent = proto.Field(proto.STRING, number=5,)
 
 
 class GetClusterRequest(proto.Message):
     r"""GetClusterRequest gets the settings of a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2212,14 +2238,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=5,)
 
 
 class UpdateClusterRequest(proto.Message):
     r"""UpdateClusterRequest updates the settings of a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2245,14 +2272,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     update = proto.Field(proto.MESSAGE, number=4, message="ClusterUpdate",)
     name = proto.Field(proto.STRING, number=5,)
 
 
 class UpdateNodePoolRequest(proto.Message):
     r"""SetNodePoolVersionRequest updates the version of a node pool.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2485,14 +2513,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     monitoring_service = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class SetAddonsConfigRequest(proto.Message):
     r"""SetAddonsRequest sets the addons associated with the cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2519,14 +2548,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     addons_config = proto.Field(proto.MESSAGE, number=4, message="AddonsConfig",)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class SetLocationsRequest(proto.Message):
     r"""SetLocationsRequest sets the locations of the cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2559,14 +2589,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     locations = proto.RepeatedField(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class UpdateMasterRequest(proto.Message):
     r"""UpdateMasterRequest updates the master of the cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2603,14 +2634,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     master_version = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class SetMasterAuthRequest(proto.Message):
     r"""SetMasterAuthRequest updates the admin password of a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2647,14 +2679,15 @@
     action = proto.Field(proto.ENUM, number=4, enum=Action,)
     update = proto.Field(proto.MESSAGE, number=5, message="MasterAuth",)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class DeleteClusterRequest(proto.Message):
     r"""DeleteClusterRequest deletes a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2677,14 +2710,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=4,)
 
 
 class ListClustersRequest(proto.Message):
     r"""ListClustersRequest lists clusters.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2702,14 +2736,15 @@
     project_id = proto.Field(proto.STRING, number=1,)
     zone = proto.Field(proto.STRING, number=2,)
     parent = proto.Field(proto.STRING, number=4,)
 
 
 class ListClustersResponse(proto.Message):
     r"""ListClustersResponse is the result of ListClustersRequest.
+
     Attributes:
         clusters (Sequence[google.cloud.container_v1beta1.types.Cluster]):
             A list of clusters in the project in the
             specified zone, or across all ones.
         missing_zones (Sequence[str]):
             If any zones are listed here, the list of
             clusters returned may be missing those zones.
@@ -2717,14 +2752,15 @@
 
     clusters = proto.RepeatedField(proto.MESSAGE, number=1, message="Cluster",)
     missing_zones = proto.RepeatedField(proto.STRING, number=2,)
 
 
 class GetOperationRequest(proto.Message):
     r"""GetOperationRequest gets a single operation.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2747,14 +2783,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     operation_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=5,)
 
 
 class ListOperationsRequest(proto.Message):
     r"""ListOperationsRequest lists operations.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2773,14 +2810,15 @@
     project_id = proto.Field(proto.STRING, number=1,)
     zone = proto.Field(proto.STRING, number=2,)
     parent = proto.Field(proto.STRING, number=4,)
 
 
 class CancelOperationRequest(proto.Message):
     r"""CancelOperationRequest cancels a single operation.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2821,14 +2859,15 @@
 
     operations = proto.RepeatedField(proto.MESSAGE, number=1, message="Operation",)
     missing_zones = proto.RepeatedField(proto.STRING, number=2,)
 
 
 class GetServerConfigRequest(proto.Message):
     r"""Gets the current Kubernetes Engine service configuration.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -2845,14 +2884,15 @@
     project_id = proto.Field(proto.STRING, number=1,)
     zone = proto.Field(proto.STRING, number=2,)
     name = proto.Field(proto.STRING, number=4,)
 
 
 class ServerConfig(proto.Message):
     r"""Kubernetes Engine service configuration.
+
     Attributes:
         default_cluster_version (str):
             Version of Kubernetes the service deploys by
             default.
         valid_node_versions (Sequence[str]):
             List of valid node upgrade target versions,
             in descending order.
@@ -2886,14 +2926,15 @@
                 the valid_versions field.
             valid_versions (Sequence[str]):
                 List of valid versions for the channel.
         """
 
         class AvailableVersion(proto.Message):
             r"""Deprecated.
+
             Attributes:
                 version (str):
                     Kubernetes version.
                 reason (str):
                     Reason for availability.
             """
 
@@ -2920,21 +2961,23 @@
     windows_version_maps = proto.MapField(
         proto.STRING, proto.MESSAGE, number=10, message="WindowsVersions",
     )
 
 
 class WindowsVersions(proto.Message):
     r"""Windows server versions.
+
     Attributes:
         windows_versions (Sequence[google.cloud.container_v1beta1.types.WindowsVersions.WindowsVersion]):
             List of Windows server versions.
     """
 
     class WindowsVersion(proto.Message):
         r"""Windows server version.
+
         Attributes:
             image_type (str):
                 Windows server image type
             os_version (str):
                 Windows server build number
             support_end_date (google.type.date_pb2.Date):
                 Mainstream support end date
@@ -2947,14 +2990,15 @@
     windows_versions = proto.RepeatedField(
         proto.MESSAGE, number=1, message=WindowsVersion,
     )
 
 
 class CreateNodePoolRequest(proto.Message):
     r"""CreateNodePoolRequest creates a node pool for a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -2980,14 +3024,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     node_pool = proto.Field(proto.MESSAGE, number=4, message="NodePool",)
     parent = proto.Field(proto.STRING, number=6,)
 
 
 class DeleteNodePoolRequest(proto.Message):
     r"""DeleteNodePoolRequest deletes a node pool for a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -3015,14 +3060,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     node_pool_id = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class ListNodePoolsRequest(proto.Message):
     r"""ListNodePoolsRequest lists the node pool(s) for a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the parent
             field.
@@ -3045,14 +3091,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     parent = proto.Field(proto.STRING, number=5,)
 
 
 class GetNodePoolRequest(proto.Message):
     r"""GetNodePoolRequest retrieves a node pool for a cluster.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://developers.google.com/console/help/new/#projectnumber>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -3185,14 +3232,15 @@
         RUNNING_WITH_ERROR = 3
         RECONCILING = 4
         STOPPING = 5
         ERROR = 6
 
     class UpgradeSettings(proto.Message):
         r"""
+
         Attributes:
             max_surge (int):
                 The maximum number of nodes that can be
                 created beyond the current size of the node pool
                 during the upgrade process.
             max_unavailable (int):
                 The maximum number of nodes that can be
@@ -3319,28 +3367,30 @@
     maintenance_exclusions = proto.MapField(
         proto.STRING, proto.MESSAGE, number=4, message="TimeWindow",
     )
 
 
 class TimeWindow(proto.Message):
     r"""Represents an arbitrary window of time.
+
     Attributes:
         start_time (google.protobuf.timestamp_pb2.Timestamp):
             The time that the window first starts.
         end_time (google.protobuf.timestamp_pb2.Timestamp):
             The time that the window ends. The end time
             should take place after the start time.
     """
 
     start_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
     end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
 
 
 class RecurringTimeWindow(proto.Message):
     r"""Represents an arbitrary window of time that recurs.
+
     Attributes:
         window (google.cloud.container_v1beta1.types.TimeWindow):
             The window of the first recurrence.
         recurrence (str):
             An RRULE
             (https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for
             how this window reccurs. They go on for the span of time
@@ -3383,14 +3433,15 @@
 
     window = proto.Field(proto.MESSAGE, number=1, message="TimeWindow",)
     recurrence = proto.Field(proto.STRING, number=2,)
 
 
 class DailyMaintenanceWindow(proto.Message):
     r"""Time window specified for daily maintenance operations.
+
     Attributes:
         start_time (str):
             Time within the maintenance window to start the maintenance
             operations. It must be in format "HH:MM", where HH : [00-23]
             and MM : [00-59] GMT.
         duration (str):
             [Output only] Duration of the time window, automatically
@@ -3440,14 +3491,15 @@
     node_pool_id = proto.Field(proto.STRING, number=4,)
     management = proto.Field(proto.MESSAGE, number=5, message="NodeManagement",)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class SetNodePoolSizeRequest(proto.Message):
     r"""SetNodePoolSizeRequest sets the size of a node pool.
+
     Attributes:
         project_id (str):
             Required. Deprecated. The Google Developers Console `project
             ID or project
             number <https://support.google.com/cloud/answer/6158840>`__.
             This field has been deprecated and replaced by the name
             field.
@@ -3517,14 +3569,15 @@
     cluster_id = proto.Field(proto.STRING, number=3,)
     node_pool_id = proto.Field(proto.STRING, number=4,)
     name = proto.Field(proto.STRING, number=6,)
 
 
 class ListNodePoolsResponse(proto.Message):
     r"""ListNodePoolsResponse is the result of ListNodePoolsRequest.
+
     Attributes:
         node_pools (Sequence[google.cloud.container_v1beta1.types.NodePool]):
             A list of node pools for a cluster.
     """
 
     node_pools = proto.RepeatedField(proto.MESSAGE, number=1, message="NodePool",)
 
@@ -3849,14 +3902,15 @@
     zone = proto.Field(proto.STRING, number=2,)
     cluster_id = proto.Field(proto.STRING, number=3,)
     name = proto.Field(proto.STRING, number=7,)
 
 
 class AcceleratorConfig(proto.Message):
     r"""AcceleratorConfig represents a Hardware Accelerator request.
+
     Attributes:
         accelerator_count (int):
             The number of the accelerator cards exposed
             to an instance.
         accelerator_type (str):
             The accelerator type resource name. List of supported
             accelerators
@@ -4132,14 +4186,15 @@
     service_external_ips_config = proto.Field(
         proto.MESSAGE, number=15, message="ServiceExternalIPsConfig",
     )
 
 
 class ServiceExternalIPsConfig(proto.Message):
     r"""Config to block services with externalIPs field.
+
     Attributes:
         enabled (bool):
             Whether Services with ExternalIPs field are
             allowed or not.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
@@ -4202,14 +4257,15 @@
         proto.MESSAGE, number=1, message="UsableSubnetwork",
     )
     next_page_token = proto.Field(proto.STRING, number=2,)
 
 
 class UsableSubnetworkSecondaryRange(proto.Message):
     r"""Secondary IP range of a usable subnetwork.
+
     Attributes:
         range_name (str):
             The name associated with this subnetwork
             secondary range, used when adding an alias IP
             range to a VM instance.
         ip_cidr_range (str):
             The range of IP addresses belonging to this
@@ -4350,14 +4406,15 @@
     cluster_dns = proto.Field(proto.ENUM, number=1, enum=Provider,)
     cluster_dns_scope = proto.Field(proto.ENUM, number=2, enum=DNSScope,)
     cluster_dns_domain = proto.Field(proto.STRING, number=3,)
 
 
 class MaxPodsConstraint(proto.Message):
     r"""Constraints applied to pods.
+
     Attributes:
         max_pods_per_node (int):
             Constraint enforced on the max num of pods
             per node.
     """
 
     max_pods_per_node = proto.Field(proto.INT64, number=1,)
@@ -4406,14 +4463,15 @@
     enable_certificates = proto.Field(
         proto.MESSAGE, number=1, message=wrappers_pb2.BoolValue,
     )
 
 
 class DatabaseEncryption(proto.Message):
     r"""Configuration of etcd encryption.
+
     Attributes:
         state (google.cloud.container_v1beta1.types.DatabaseEncryption.State):
             Denotes the state of etcd encryption.
         key_name (str):
             Name of CloudKMS key to use for the
             encryption of secrets in etcd. Ex. projects/my-
             project/locations/global/keyRings/my-
@@ -4428,14 +4486,15 @@
 
     state = proto.Field(proto.ENUM, number=2, enum=State,)
     key_name = proto.Field(proto.STRING, number=1,)
 
 
 class ResourceUsageExportConfig(proto.Message):
     r"""Configuration for exporting cluster resource usages.
+
     Attributes:
         bigquery_destination (google.cloud.container_v1beta1.types.ResourceUsageExportConfig.BigQueryDestination):
             Configuration to use BigQuery as usage export
             destination.
         enable_network_egress_metering (bool):
             Whether to enable network egress metering for
             this cluster. If enabled, a daemonset will be
@@ -4455,14 +4514,15 @@
                 The ID of a BigQuery Dataset.
         """
 
         dataset_id = proto.Field(proto.STRING, number=1,)
 
     class ConsumptionMeteringConfig(proto.Message):
         r"""Parameters for controlling consumption metering.
+
         Attributes:
             enabled (bool):
                 Whether to enable consumption metering for
                 this cluster. If enabled, a second BigQuery
                 table will be created to hold resource
                 consumption records.
         """
@@ -4476,25 +4536,27 @@
     consumption_metering_config = proto.Field(
         proto.MESSAGE, number=3, message=ConsumptionMeteringConfig,
     )
 
 
 class ShieldedNodes(proto.Message):
     r"""Configuration of Shielded Nodes feature.
+
     Attributes:
         enabled (bool):
             Whether Shielded Nodes features are enabled
             on all nodes in this cluster.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class VirtualNIC(proto.Message):
     r"""Configuration of gVNIC feature.
+
     Attributes:
         enabled (bool):
             Whether gVNIC features are enabled in the
             node pool.
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
@@ -4560,14 +4622,15 @@
     """
 
     parent = proto.Field(proto.STRING, number=1,)
 
 
 class Jwk(proto.Message):
     r"""Jwk is a JSON Web Key as specified in RFC 7517
+
     Attributes:
         kty (str):
             Key Type.
         alg (str):
             Algorithm.
         use (str):
             Permitted uses for the public keys.
@@ -4630,14 +4693,15 @@
         STABLE = 3
 
     channel = proto.Field(proto.ENUM, number=1, enum=Channel,)
 
 
 class TpuConfig(proto.Message):
     r"""Configuration for Cloud TPU.
+
     Attributes:
         enabled (bool):
             Whether Cloud TPU integration is enabled or
             not.
         use_service_networking (bool):
             Whether to use service networking for Cloud
             TPU or not.
@@ -4648,15 +4712,16 @@
 
     enabled = proto.Field(proto.BOOL, number=1,)
     use_service_networking = proto.Field(proto.BOOL, number=2,)
     ipv4_cidr_block = proto.Field(proto.STRING, number=3,)
 
 
 class Master(proto.Message):
-    r"""Master is the configuration for components on master.    """
+    r"""Master is the configuration for components on master.
+    """
 
 
 class Autopilot(proto.Message):
     r"""Autopilot is the configuration for Autopilot settings on the
     cluster.
 
     Attributes:
@@ -4665,21 +4730,23 @@
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class NotificationConfig(proto.Message):
     r"""NotificationConfig is the configuration of notifications.
+
     Attributes:
         pubsub (google.cloud.container_v1beta1.types.NotificationConfig.PubSub):
             Notification config for Pub/Sub.
     """
 
     class PubSub(proto.Message):
         r"""Pub/Sub specific notification config.
+
         Attributes:
             enabled (bool):
                 Enable notifications for Pub/Sub.
             topic (str):
                 The desired Pub/Sub topic to which notifications will be
                 sent by GKE. Format is
                 ``projects/{project}/topics/{topic}``.
@@ -4773,14 +4840,15 @@
     """
 
     enabled = proto.Field(proto.BOOL, number=1,)
 
 
 class LoggingConfig(proto.Message):
     r"""LoggingConfig is cluster logging configuration.
+
     Attributes:
         component_config (google.cloud.container_v1beta1.types.LoggingComponentConfig):
             Logging components configuration
     """
 
     component_config = proto.Field(
         proto.MESSAGE, number=1, message="LoggingComponentConfig",
@@ -4804,14 +4872,15 @@
         WORKLOADS = 2
 
     enable_components = proto.RepeatedField(proto.ENUM, number=1, enum=Component,)
 
 
 class MonitoringConfig(proto.Message):
     r"""MonitoringConfig is cluster monitoring configuration.
+
     Attributes:
         component_config (google.cloud.container_v1beta1.types.MonitoringComponentConfig):
             Monitoring components configuration
     """
 
     component_config = proto.Field(
         proto.MESSAGE, number=1, message="MonitoringComponentConfig",
```

### Comparing `google-cloud-container-2.8.1/google_cloud_container.egg-info/PKG-INFO` & `google-cloud-container-2.9.0/google_cloud_container.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: google-cloud-container
-Version: 2.8.1
+Version: 2.9.0
 Summary: Google Container Engine API client library
 Home-page: https://github.com/googleapis/python-container
 Author: Google LLC
 Author-email: googleapis-packages@google.com
 License: Apache 2.0
 Platform: Posix; MacOS X; Windows
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `google-cloud-container-2.8.1/google_cloud_container.egg-info/SOURCES.txt` & `google-cloud-container-2.9.0/google_cloud_container.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/scripts/fixup_container_v1_keywords.py` & `google-cloud-container-2.9.0/scripts/fixup_container_v1_keywords.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/scripts/fixup_container_v1beta1_keywords.py` & `google-cloud-container-2.9.0/scripts/fixup_container_v1beta1_keywords.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/setup.py` & `google-cloud-container-2.9.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 import setuptools
 
 
 # Package metadata.
 
 name = "google-cloud-container"
 description = "Google Container Engine API client library"
-version = "2.8.1"
+version = "2.9.0"
 # Should be one of:
 # 'Development Status :: 3 - Alpha'
 # 'Development Status :: 4 - Beta'
 # 'Development Status :: 5 - Production/Stable'
 release_status = "Development Status :: 5 - Production/Stable"
 dependencies = [
     # NOTE: Maintainers, please do not require google-api-core>=2.x.x
```

### Comparing `google-cloud-container-2.8.1/tests/__init__.py` & `google-cloud-container-2.9.0/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/tests/system/gapic/v1/test_system_cluster_manager_v1.py` & `google-cloud-container-2.9.0/tests/system/gapic/v1/test_system_cluster_manager_v1.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/tests/unit/__init__.py` & `google-cloud-container-2.9.0/tests/unit/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/tests/unit/gapic/__init__.py` & `google-cloud-container-2.9.0/tests/unit/gapic/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/tests/unit/gapic/container_v1/__init__.py` & `google-cloud-container-2.9.0/tests/unit/gapic/container_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/tests/unit/gapic/container_v1/test_cluster_manager.py` & `google-cloud-container-2.9.0/tests/unit/gapic/container_v1/test_cluster_manager.py`

 * *Files 0% similar despite different names*

```diff
@@ -25,14 +25,15 @@
 
 
 from google.api_core import client_options
 from google.api_core import exceptions as core_exceptions
 from google.api_core import gapic_v1
 from google.api_core import grpc_helpers
 from google.api_core import grpc_helpers_async
+from google.api_core import path_template
 from google.auth import credentials as ga_credentials
 from google.auth.exceptions import MutualTLSChannelError
 from google.cloud.container_v1.services.cluster_manager import ClusterManagerAsyncClient
 from google.cloud.container_v1.services.cluster_manager import ClusterManagerClient
 from google.cloud.container_v1.services.cluster_manager import pagers
 from google.cloud.container_v1.services.cluster_manager import transports
 from google.cloud.container_v1.services.cluster_manager.transports.base import (
@@ -8770,14 +8771,17 @@
         "set_maintenance_policy",
         "list_usable_subnetworks",
     )
     for method in methods:
         with pytest.raises(NotImplementedError):
             getattr(transport, method)(request=object())
 
+    with pytest.raises(NotImplementedError):
+        transport.close()
+
 
 @requires_google_auth_gte_1_25_0
 def test_cluster_manager_base_transport_with_credentials_file():
     # Instantiate the base transport with a credentials file
     with mock.patch.object(
         google.auth, "load_credentials_from_file", autospec=True
     ) as load_creds, mock.patch(
@@ -9228,7 +9232,53 @@
         transports.ClusterManagerTransport, "_prep_wrapped_messages"
     ) as prep:
         transport_class = ClusterManagerClient.get_transport_class()
         transport = transport_class(
             credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
         )
         prep.assert_called_once_with(client_info)
+
+
+@pytest.mark.asyncio
+async def test_transport_close_async():
+    client = ClusterManagerAsyncClient(
+        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
+    )
+    with mock.patch.object(
+        type(getattr(client.transport, "grpc_channel")), "close"
+    ) as close:
+        async with client:
+            close.assert_not_called()
+        close.assert_called_once()
+
+
+def test_transport_close():
+    transports = {
+        "grpc": "_grpc_channel",
+    }
+
+    for transport, close_name in transports.items():
+        client = ClusterManagerClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        with mock.patch.object(
+            type(getattr(client.transport, close_name)), "close"
+        ) as close:
+            with client:
+                close.assert_not_called()
+            close.assert_called_once()
+
+
+def test_client_ctx():
+    transports = [
+        "grpc",
+    ]
+    for transport in transports:
+        client = ClusterManagerClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        # Test client calls underlying transport.
+        with mock.patch.object(type(client.transport), "close") as close:
+            close.assert_not_called()
+            with client:
+                pass
+            close.assert_called()
```

### Comparing `google-cloud-container-2.8.1/tests/unit/gapic/container_v1beta1/__init__.py` & `google-cloud-container-2.9.0/tests/unit/gapic/container_v1beta1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-container-2.8.1/tests/unit/gapic/container_v1beta1/test_cluster_manager.py` & `google-cloud-container-2.9.0/tests/unit/gapic/container_v1beta1/test_cluster_manager.py`

 * *Files 0% similar despite different names*

```diff
@@ -25,14 +25,15 @@
 
 
 from google.api_core import client_options
 from google.api_core import exceptions as core_exceptions
 from google.api_core import gapic_v1
 from google.api_core import grpc_helpers
 from google.api_core import grpc_helpers_async
+from google.api_core import path_template
 from google.auth import credentials as ga_credentials
 from google.auth.exceptions import MutualTLSChannelError
 from google.cloud.container_v1beta1.services.cluster_manager import (
     ClusterManagerAsyncClient,
 )
 from google.cloud.container_v1beta1.services.cluster_manager import ClusterManagerClient
 from google.cloud.container_v1beta1.services.cluster_manager import pagers
@@ -9133,14 +9134,17 @@
         "list_usable_subnetworks",
         "list_locations",
     )
     for method in methods:
         with pytest.raises(NotImplementedError):
             getattr(transport, method)(request=object())
 
+    with pytest.raises(NotImplementedError):
+        transport.close()
+
 
 @requires_google_auth_gte_1_25_0
 def test_cluster_manager_base_transport_with_credentials_file():
     # Instantiate the base transport with a credentials file
     with mock.patch.object(
         google.auth, "load_credentials_from_file", autospec=True
     ) as load_creds, mock.patch(
@@ -9611,7 +9615,53 @@
         transports.ClusterManagerTransport, "_prep_wrapped_messages"
     ) as prep:
         transport_class = ClusterManagerClient.get_transport_class()
         transport = transport_class(
             credentials=ga_credentials.AnonymousCredentials(), client_info=client_info,
         )
         prep.assert_called_once_with(client_info)
+
+
+@pytest.mark.asyncio
+async def test_transport_close_async():
+    client = ClusterManagerAsyncClient(
+        credentials=ga_credentials.AnonymousCredentials(), transport="grpc_asyncio",
+    )
+    with mock.patch.object(
+        type(getattr(client.transport, "grpc_channel")), "close"
+    ) as close:
+        async with client:
+            close.assert_not_called()
+        close.assert_called_once()
+
+
+def test_transport_close():
+    transports = {
+        "grpc": "_grpc_channel",
+    }
+
+    for transport, close_name in transports.items():
+        client = ClusterManagerClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        with mock.patch.object(
+            type(getattr(client.transport, close_name)), "close"
+        ) as close:
+            with client:
+                close.assert_not_called()
+            close.assert_called_once()
+
+
+def test_client_ctx():
+    transports = [
+        "grpc",
+    ]
+    for transport in transports:
+        client = ClusterManagerClient(
+            credentials=ga_credentials.AnonymousCredentials(), transport=transport
+        )
+        # Test client calls underlying transport.
+        with mock.patch.object(type(client.transport), "close") as close:
+            close.assert_not_called()
+            with client:
+                pass
+            close.assert_called()
```

