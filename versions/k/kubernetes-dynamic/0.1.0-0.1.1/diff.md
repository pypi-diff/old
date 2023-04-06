# Comparing `tmp/kubernetes-dynamic-0.1.0.tar.gz` & `tmp/kubernetes-dynamic-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kubernetes-dynamic-0.1.0.tar", last modified: Thu Apr  6 11:47:11 2023, max compression
+gzip compressed data, was "kubernetes-dynamic-0.1.1.tar", last modified: Thu Apr  6 17:38:40 2023, max compression
```

## Comparing `kubernetes-dynamic-0.1.0.tar` & `kubernetes-dynamic-0.1.1.tar`

### file list

```diff
@@ -1,61 +1,63 @@
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/
--rw-r--r--   0 akobor    (1000) akobor    (1000)      538 2023-03-28 15:57:58.000000 kubernetes-dynamic-0.1.0/LICENSE
--rw-r--r--   0 akobor    (1000) akobor    (1000)     3312 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/PKG-INFO
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2434 2023-04-04 08:18:12.000000 kubernetes-dynamic-0.1.0/README.md
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/kubernetes_dynamic/
--rw-r--r--   0 akobor    (1000) akobor    (1000)      713 2023-04-06 10:41:23.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/__init__.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)      821 2023-04-06 09:49:15.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/_kubernetes.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)       22 2023-04-06 10:40:14.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/_version.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    14242 2023-04-06 10:30:23.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/client.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1636 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/config.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     3373 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/events.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1279 2023-04-06 09:06:15.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/exceptions.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1807 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/formatters.py
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/
--rw-r--r--   0 akobor    (1000) akobor    (1000)        0 2023-04-06 08:52:24.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/__init__.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2620 2023-04-06 08:55:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/dateutil.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    17528 2023-04-06 10:34:53.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/discovery.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     3895 2023-04-06 09:13:20.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/exceptions.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     3618 2023-04-06 08:58:17.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/exec_provider.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     4499 2023-04-06 08:58:21.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/incluster_config.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    32113 2023-04-06 09:30:16.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/kube_config.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    20272 2023-04-06 11:29:54.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/resource_api.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    22528 2023-04-06 09:12:10.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/ws_client.py
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/
--rw-r--r--   0 akobor    (1000) akobor    (1000)    28915 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/__init__.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)   140534 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/all.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2483 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/common.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1855 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/configmap.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)      830 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/ingress.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1092 2023-04-06 10:50:43.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/namespace.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     4174 2023-04-06 10:59:33.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/pod.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     8305 2023-04-06 10:50:03.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/resource_item.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2857 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/resource_value.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2944 2023-04-06 10:50:56.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/secret.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)      480 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/stateful_set.py
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/
--rw-r--r--   0 akobor    (1000) akobor    (1000)        0 2023-04-06 08:45:10.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/__init__.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    27737 2023-04-06 10:42:24.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/api_client.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    15174 2023-04-06 09:13:43.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/configuration.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     5104 2023-04-06 08:50:35.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/exceptions.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)    12499 2023-04-06 09:14:24.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/rest.py
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/
--rw-r--r--   0 akobor    (1000) akobor    (1000)     3312 2023-04-06 11:47:11.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/PKG-INFO
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1745 2023-04-06 11:47:11.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/SOURCES.txt
--rw-r--r--   0 akobor    (1000) akobor    (1000)        1 2023-04-06 11:47:11.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/dependency_links.txt
--rw-r--r--   0 akobor    (1000) akobor    (1000)      117 2023-04-06 11:47:11.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/requires.txt
--rw-r--r--   0 akobor    (1000) akobor    (1000)       19 2023-04-06 11:47:11.000000 kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/top_level.txt
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1415 2023-04-03 12:59:55.000000 kubernetes-dynamic-0.1.0/pyproject.toml
--rw-r--r--   0 akobor    (1000) akobor    (1000)      117 2023-04-06 10:42:13.000000 kubernetes-dynamic-0.1.0/requirements.txt
--rw-r--r--   0 akobor    (1000) akobor    (1000)       38 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/setup.cfg
-drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 11:47:11.492714 kubernetes-dynamic-0.1.0/tests/
--rw-r--r--   0 akobor    (1000) akobor    (1000)     7240 2023-04-06 11:16:08.000000 kubernetes-dynamic-0.1.0/tests/test_client.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)      921 2023-03-30 08:05:36.000000 kubernetes-dynamic-0.1.0/tests/test_config.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2010 2023-04-03 11:54:29.000000 kubernetes-dynamic-0.1.0/tests/test_configmap.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)      623 2023-04-03 11:54:58.000000 kubernetes-dynamic-0.1.0/tests/test_ingress.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     1636 2023-04-06 10:51:07.000000 kubernetes-dynamic-0.1.0/tests/test_namespace.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     5097 2023-04-06 11:09:52.000000 kubernetes-dynamic-0.1.0/tests/test_pod.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     4222 2023-04-06 11:30:59.000000 kubernetes-dynamic-0.1.0/tests/test_resource_api.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     4804 2023-04-06 10:50:03.000000 kubernetes-dynamic-0.1.0/tests/test_resource_item.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)      761 2023-04-03 20:50:33.000000 kubernetes-dynamic-0.1.0/tests/test_resource_value.py
--rw-r--r--   0 akobor    (1000) akobor    (1000)     2770 2023-04-03 12:49:49.000000 kubernetes-dynamic-0.1.0/tests/test_secret.py
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.472063 kubernetes-dynamic-0.1.1/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      538 2023-03-28 15:57:58.000000 kubernetes-dynamic-0.1.1/LICENSE
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     3312 2023-04-06 17:38:40.472063 kubernetes-dynamic-0.1.1/PKG-INFO
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2434 2023-04-04 08:18:12.000000 kubernetes-dynamic-0.1.1/README.md
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.462063 kubernetes-dynamic-0.1.1/kubernetes_dynamic/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      713 2023-04-06 10:41:23.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/__init__.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      821 2023-04-06 09:49:15.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/_kubernetes.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)       22 2023-04-06 17:38:25.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/_version.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    14313 2023-04-06 12:50:21.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/client.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1636 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/config.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     3373 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/events.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1279 2023-04-06 09:06:15.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/exceptions.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2195 2023-04-06 12:50:11.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/formatters.py
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.462063 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)        0 2023-04-06 08:52:24.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/__init__.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2620 2023-04-06 08:55:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/dateutil.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    17528 2023-04-06 10:34:53.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/discovery.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     3895 2023-04-06 09:13:20.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/exceptions.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     3618 2023-04-06 08:58:17.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/exec_provider.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     4499 2023-04-06 08:58:21.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/incluster_config.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    32113 2023-04-06 09:30:16.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/kube_config.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    20042 2023-04-06 15:56:41.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/resource_api.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    22528 2023-04-06 09:12:10.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/ws_client.py
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.462063 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    28915 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/__init__.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)   140097 2023-04-06 12:52:17.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/all.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2483 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/common.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1855 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/configmap.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      830 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/ingress.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1092 2023-04-06 10:50:43.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/namespace.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     4659 2023-04-06 13:00:47.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/pod.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      843 2023-04-06 12:52:00.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/replica_set.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     8305 2023-04-06 10:50:03.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/resource_item.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2857 2023-04-05 15:49:31.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/resource_value.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2944 2023-04-06 10:50:56.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/secret.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1333 2023-04-06 15:52:26.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/service.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      761 2023-04-06 12:35:43.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/stateful_set.py
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.472063 kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)        0 2023-04-06 08:45:10.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/__init__.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    27737 2023-04-06 10:42:24.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/api_client.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    15174 2023-04-06 09:13:43.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/configuration.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     5104 2023-04-06 08:50:35.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/exceptions.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)    12499 2023-04-06 09:14:24.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/rest.py
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.462063 kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     3312 2023-04-06 17:38:40.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/PKG-INFO
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1823 2023-04-06 17:38:40.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/SOURCES.txt
+-rw-r--r--   0 akobor    (1000) akobor    (1000)        1 2023-04-06 17:38:40.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/dependency_links.txt
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      117 2023-04-06 17:38:40.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/requires.txt
+-rw-r--r--   0 akobor    (1000) akobor    (1000)       19 2023-04-06 17:38:40.000000 kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/top_level.txt
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1415 2023-04-03 12:59:55.000000 kubernetes-dynamic-0.1.1/pyproject.toml
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      117 2023-04-06 10:42:13.000000 kubernetes-dynamic-0.1.1/requirements.txt
+-rw-r--r--   0 akobor    (1000) akobor    (1000)       38 2023-04-06 17:38:40.472063 kubernetes-dynamic-0.1.1/setup.cfg
+drwxr-xr-x   0 akobor    (1000) akobor    (1000)        0 2023-04-06 17:38:40.472063 kubernetes-dynamic-0.1.1/tests/
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     7240 2023-04-06 11:16:08.000000 kubernetes-dynamic-0.1.1/tests/test_client.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      921 2023-03-30 08:05:36.000000 kubernetes-dynamic-0.1.1/tests/test_config.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2010 2023-04-03 11:54:29.000000 kubernetes-dynamic-0.1.1/tests/test_configmap.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      623 2023-04-03 11:54:58.000000 kubernetes-dynamic-0.1.1/tests/test_ingress.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     1636 2023-04-06 10:51:07.000000 kubernetes-dynamic-0.1.1/tests/test_namespace.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     5097 2023-04-06 11:09:52.000000 kubernetes-dynamic-0.1.1/tests/test_pod.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     4222 2023-04-06 11:30:59.000000 kubernetes-dynamic-0.1.1/tests/test_resource_api.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     4804 2023-04-06 10:50:03.000000 kubernetes-dynamic-0.1.1/tests/test_resource_item.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)      761 2023-04-03 20:50:33.000000 kubernetes-dynamic-0.1.1/tests/test_resource_value.py
+-rw-r--r--   0 akobor    (1000) akobor    (1000)     2770 2023-04-03 12:49:49.000000 kubernetes-dynamic-0.1.1/tests/test_secret.py
```

### Comparing `kubernetes-dynamic-0.1.0/LICENSE` & `kubernetes-dynamic-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/PKG-INFO` & `kubernetes-dynamic-0.1.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kubernetes-dynamic
-Version: 0.1.0
+Version: 0.1.1
 Summary: Kubernetes Dynamic client
 Author-email: Attila Kobor <atti92@gmail.com>, Balazs Hamorszky <balihb@gmail.com>
 License: BSD-3-Clause
 Project-URL: homepage, https://github.com/atti92/kubernetes-dynamic
 Project-URL: documentation, https://github.com/atti92/kubernetes-dynamic
 Project-URL: repository, https://github.com/atti92/kubernetes-dynamic.git
 Project-URL: changelog, https://github.com/atti92/kubernetes-dynamic/blob/main/README.md
```

### Comparing `kubernetes-dynamic-0.1.0/README.md` & `kubernetes-dynamic-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/__init__.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/__init__.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/_kubernetes.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/_kubernetes.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/client.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/client.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 from typing import Any, Callable, List, Optional, Type, TypeVar, overload
 
 import pydantic
 import yaml
 
 import kubernetes_dynamic.kube.ws_client as ws_client
 import kubernetes_dynamic.models as models
+from kubernetes_dynamic.formatters import to_lower_camel
 
 from . import _kubernetes
 from .config import K8sConfig
 from .exceptions import (
     ConfigException,
     InvalidParameter,
     ResourceNotUniqueError,
@@ -324,15 +325,15 @@
         _request_timeout = params.pop("_request_timeout", None)
 
         # Authentication setting
         auth_settings = ["BearerToken"]
 
         for key, value in params.items():
             if value is not None:
-                query_params.append((key.lstrip("_"), value))
+                query_params.append((to_lower_camel(key.lstrip("_")), value))
 
         api_response = self.client.call_api(
             path,
             method.upper(),
             path_params,
             query_params,
             header_params,
@@ -368,9 +369,7 @@
             data = [data]
 
         items = []
         for item in data:
             resource = self.get_api(kind=item["kind"], api_version=item["apiVersion"].split("/")[-1])
             items.append(resource.apply(item, namespace))
         return items
-
-
```

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/config.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/config.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/events.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/events.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/exceptions.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/exceptions.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/formatters.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/formatters.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-
 from typing import Union
 
 SelectorTypes = Union[None, str, dict, list, tuple]
 
+
 def _format_dict_selector(selector: dict):
     items = []
     for key, value in selector.items():
         exists = True
         if key.startswith("!"):
             exists = False
             key = key[1:]
@@ -16,14 +16,15 @@
             items.append(f"{key}{'!' if not exists else ''}={value}")
         elif not exists or value is False:
             items.append(f"!{key}")
         else:
             items.append(key)
     return format_selector(items)
 
+
 def format_selector(selector: SelectorTypes):
     """Format kubernetes selector.
 
     Args:
         selector: The selector object to convert.
             - string: no conversion done.
             - list, tuple: the object is concatenated by `,`.
@@ -40,7 +41,20 @@
         Kubernetes compatible string selector
     """
     if isinstance(selector, (list, tuple)):
         return ",".join(selector)
     if isinstance(selector, dict):
         return _format_dict_selector(selector)
     return selector
+
+
+def to_camel(string: str) -> str:
+    """Convert snake_case to CamelCase"""
+    return "".join(word.capitalize() for word in string.split("_"))
+
+
+def to_lower_camel(string: str) -> str:
+    """Convert snake_case to lowerCamelCase"""
+    if len(string) >= 1:
+        pascal_string = to_camel(string)
+        return pascal_string[0].lower() + pascal_string[1:]
+    return string.lower()
```

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/dateutil.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/dateutil.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/discovery.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/discovery.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/exceptions.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/exceptions.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/exec_provider.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/exec_provider.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/incluster_config.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/incluster_config.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/kube_config.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/kube_config.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/resource_api.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/resource_api.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,20 +1,7 @@
-# Copyright 2019 The Kubernetes Authors.
-#
-# Licensed under the Apache License, Version 2.0 (the "License");
-# you may not use this file except in compliance with the License.
-# You may obtain a copy of the License at
-#
-#     http://www.apache.org/licenses/LICENSE-2.0
-#
-# Unless required by applicable law or agreed to in writing, software
-# distributed under the License is distributed on an "AS IS" BASIS,
-# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-# See the License for the specific language governing permissions and
-# limitations under the License.
 from __future__ import annotations
 
 import re
 from typing import TYPE_CHECKING, Callable, Generic, Iterator, Optional, Type, TypeVar, cast, overload
 
 from kubernetes_dynamic.events import Event, Watch
 from kubernetes_dynamic.exceptions import EventTimeoutError
@@ -54,15 +41,14 @@
         singularName=None,
         shortNames=None,
         categories=None,
         subresources=None,
         resource_type=None,
         **kwargs,
     ):
-
         if None in (api_version, kind, prefix):
             raise ValueError("At least prefix, kind, and api_version must be provided")
 
         self.prefix = prefix
         self.group = group
         self.api_version = api_version
         self.kind = kind
@@ -197,14 +183,15 @@
         ...  # pragma: no cover
 
     def read(
         self, name: Optional[str] = None, namespace: Optional[str | _Missing] = MISSING, **kwargs
     ) -> R | ItemList[R]:
         namespace = self.ensure_namespace_param(namespace, allow_all=not name)
         path = self.path(name=name, namespace=namespace)
+        kwargs.setdefault("serializer", self.resource_type)
         return self.client.request("get", path, **kwargs)
 
     @overload
     def get(
         self,
         *,
         namespace: Optional[str | _Missing] = MISSING,
@@ -259,14 +246,15 @@
                 items.append(item)
         return items
 
     def create(self, body: dict | R, namespace: Optional[str | _Missing] = MISSING, **kwargs) -> R:
         body = self.serialize_body(body)
         namespace = self.ensure_namespace_param(namespace, body)
         path = self.path(namespace=namespace)
+        kwargs.setdefault("serializer", self.resource_type)
         return self.client.request("post", path, body=body, **kwargs)
 
     @overload
     def delete(
         self, name: str, namespace: Optional[str | _Missing] = MISSING, body: Optional[dict | R] = None, **kwargs
     ) -> R:
         ...  # pragma: no cover
@@ -293,37 +281,39 @@
         **kwargs,
     ) -> ItemList[R] | R:
         if not (name or label_selector or field_selector):
             raise ValueError("At least one of name|label_selector|field_selector is required")
         if self.namespaced and not (label_selector or field_selector):
             namespace = self.ensure_namespace_param(namespace, allow_all=not name)
         path = self.path(name=name, namespace=namespace)
+        kwargs.setdefault("serializer", self.resource_type)
         return self.client.request(
             "delete", path, body=body, label_selector=label_selector, field_selector=field_selector, **kwargs
         )
 
     def replace(
         self, body: dict | R, name: Optional[str] = None, namespace: Optional[str | _Missing] = MISSING, **kwargs
     ) -> R:
         body = self.serialize_body(body)
         name = self.ensure_name_param(name, body)
         namespace = self.ensure_namespace_param(namespace, body)
         path = self.path(name=name, namespace=namespace)
+        kwargs.setdefault("serializer", self.resource_type)
         return self.client.request("put", path, body=body, **kwargs)
 
     def patch(
         self, body: dict | R, name: Optional[str] = None, namespace: Optional[str | _Missing] = MISSING, **kwargs
     ) -> R:
         body = self.serialize_body(body)
         name = self.ensure_name_param(name, body)
         namespace = self.ensure_namespace_param(namespace, body)
 
         content_type = kwargs.pop("content_type", "application/strategic-merge-patch+json")
         path = self.path(name=name, namespace=namespace)
-
+        kwargs.setdefault("serializer", self.resource_type)
         return self.client.request("patch", path, body=body, content_type=content_type, **kwargs)
 
     def server_side_apply(
         self,
         body: dict | R,
         name: Optional[str] = None,
         namespace: Optional[str | _Missing] = MISSING,
@@ -332,15 +322,15 @@
     ) -> R:
         body = self.serialize_body(body)
         name = self.ensure_name_param(name, body)
         namespace = self.ensure_namespace_param(namespace, body)
 
         kwargs.update({"content_type": "application/apply-patch+yaml"})
         path = self.path(name=name, namespace=namespace)
-
+        kwargs.setdefault("serializer", self.resource_type)
         return self.client.request("patch", path, body=body, force_conflicts=force_conflicts, **kwargs)
 
     def watch(
         self,
         namespace: Optional[str | _Missing] = MISSING,
         name: Optional[str] = None,
         label_selector: Optional[str] = None,
```

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/kube/ws_client.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/kube/ws_client.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/__init__.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/__init__.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/all.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/all.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,17 +9,19 @@
 from .common import V1ListMeta as V1ListMeta
 from .common import V1ManagedFieldsEntry as V1ManagedFieldsEntry
 from .common import V1ObjectMeta, V1OwnerReference
 from .configmap import V1ConfigMap
 from .ingress import V1Ingress as V1Ingress
 from .namespace import V1Namespace as V1Namespace
 from .pod import V1Pod as V1Pod
+from .replica_set import V1ReplicaSet as V1ReplicaSet
 from .resource_item import ResourceItem
 from .resource_value import ResourceValue
 from .secret import V1Secret as V1Secret
+from .service import V1Service as V1Service
 from .stateful_set import V1StatefulSet as V1StatefulSet
 
 
 class V2HorizontalPodAutoscalerList(ResourceItem):
     items: List[V2HorizontalPodAutoscaler] = Field(default_factory=list)
     metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
 
@@ -951,20 +953,14 @@
     publishNotReadyAddresses: Optional[bool] = None
     selector: Dict[str, str] = Field(default_factory=dict)
     sessionAffinity: Optional[str] = None
     sessionAffinityConfig: V1SessionAffinityConfig = Field(default_factory=lambda: V1SessionAffinityConfig())
     type: Optional[str] = None
 
 
-class V1Service(ResourceItem):
-    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())
-    spec: V1ServiceSpec = Field(default_factory=lambda: V1ServiceSpec())
-    status: V1ServiceStatus = Field(default_factory=lambda: V1ServiceStatus())
-
-
 class V1ResourceRule(ResourceValue):
     apiGroups: List[str] = Field(default_factory=list)
     resourceNames: List[str] = Field(default_factory=list)
     resources: List[str] = Field(default_factory=list)
     verbs: List[str] = Field(default_factory=list)
 
 
@@ -1155,20 +1151,14 @@
 class V1ReplicaSetSpec(ResourceValue):
     minReadySeconds: Optional[int] = None
     replicas: Optional[int] = None
     selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())
     template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
 
 
-class V1ReplicaSet(ResourceItem):
-    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())
-    spec: V1ReplicaSetSpec = Field(default_factory=lambda: V1ReplicaSetSpec())
-    status: V1ReplicaSetStatus = Field(default_factory=lambda: V1ReplicaSetStatus())
-
-
 class V1PriorityClassList(ResourceItem):
     items: List[V1PriorityClass] = Field(default_factory=list)
     metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
 
 
 class V1PriorityClass(ResourceItem):
     description: Optional[str] = None
```

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/common.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/common.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/configmap.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/configmap.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/ingress.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/ingress.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/namespace.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/namespace.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/pod.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/pod.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 from __future__ import annotations
 
 from typing import TYPE_CHECKING, Iterator, Optional
 
+from more_itertools import first
 from pydantic import Field
 from urllib3 import HTTPResponse
 
 from .common import get_default
 from .resource_item import ResourceItem
 
 if TYPE_CHECKING:
@@ -112,7 +113,17 @@
         controller = "Deployment" if controller == "ReplicaSet" else controller
         return controller
 
     def get_env(self) -> dict[str, str]:
         """Get environment variables from a pod."""
         env = self.exec("env")
         return {item.split("=", 1)[0]: item.split("=", 1)[1] for item in env.splitlines()}
+
+    def get_port(self, port: str | int) -> Optional[int]:
+        """Get the first matching port number with name."""
+        if isinstance(port, int):
+            return first(
+                (p.containerPort for c in self.spec.containers for p in c.ports if p.containerPort == port), None
+            )
+        return first(
+            (p.containerPort for c in self.spec.containers for p in c.ports if p.name == port or not port), None
+        )
```

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/resource_item.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/resource_item.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/resource_value.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/resource_value.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/models/secret.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/models/secret.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/api_client.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/api_client.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/configuration.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/configuration.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/exceptions.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/exceptions.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic/openapi_client/rest.py` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic/openapi_client/rest.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/PKG-INFO` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kubernetes-dynamic
-Version: 0.1.0
+Version: 0.1.1
 Summary: Kubernetes Dynamic client
 Author-email: Attila Kobor <atti92@gmail.com>, Balazs Hamorszky <balihb@gmail.com>
 License: BSD-3-Clause
 Project-URL: homepage, https://github.com/atti92/kubernetes-dynamic
 Project-URL: documentation, https://github.com/atti92/kubernetes-dynamic
 Project-URL: repository, https://github.com/atti92/kubernetes-dynamic.git
 Project-URL: changelog, https://github.com/atti92/kubernetes-dynamic/blob/main/README.md
```

### Comparing `kubernetes-dynamic-0.1.0/kubernetes_dynamic.egg-info/SOURCES.txt` & `kubernetes-dynamic-0.1.1/kubernetes_dynamic.egg-info/SOURCES.txt`

 * *Files 13% similar despite different names*

```diff
@@ -27,17 +27,19 @@
 kubernetes_dynamic/models/__init__.py
 kubernetes_dynamic/models/all.py
 kubernetes_dynamic/models/common.py
 kubernetes_dynamic/models/configmap.py
 kubernetes_dynamic/models/ingress.py
 kubernetes_dynamic/models/namespace.py
 kubernetes_dynamic/models/pod.py
+kubernetes_dynamic/models/replica_set.py
 kubernetes_dynamic/models/resource_item.py
 kubernetes_dynamic/models/resource_value.py
 kubernetes_dynamic/models/secret.py
+kubernetes_dynamic/models/service.py
 kubernetes_dynamic/models/stateful_set.py
 kubernetes_dynamic/openapi_client/__init__.py
 kubernetes_dynamic/openapi_client/api_client.py
 kubernetes_dynamic/openapi_client/configuration.py
 kubernetes_dynamic/openapi_client/exceptions.py
 kubernetes_dynamic/openapi_client/rest.py
 tests/test_client.py
```

### Comparing `kubernetes-dynamic-0.1.0/pyproject.toml` & `kubernetes-dynamic-0.1.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_client.py` & `kubernetes-dynamic-0.1.1/tests/test_client.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_config.py` & `kubernetes-dynamic-0.1.1/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_configmap.py` & `kubernetes-dynamic-0.1.1/tests/test_configmap.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_ingress.py` & `kubernetes-dynamic-0.1.1/tests/test_ingress.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_namespace.py` & `kubernetes-dynamic-0.1.1/tests/test_namespace.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_pod.py` & `kubernetes-dynamic-0.1.1/tests/test_pod.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_resource_api.py` & `kubernetes-dynamic-0.1.1/tests/test_resource_api.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_resource_item.py` & `kubernetes-dynamic-0.1.1/tests/test_resource_item.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_resource_value.py` & `kubernetes-dynamic-0.1.1/tests/test_resource_value.py`

 * *Files identical despite different names*

### Comparing `kubernetes-dynamic-0.1.0/tests/test_secret.py` & `kubernetes-dynamic-0.1.1/tests/test_secret.py`

 * *Files identical despite different names*

