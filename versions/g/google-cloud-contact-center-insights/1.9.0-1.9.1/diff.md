# Comparing `tmp/google-cloud-contact-center-insights-1.9.0.tar.gz` & `tmp/google-cloud-contact-center-insights-1.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "google-cloud-contact-center-insights-1.9.0.tar", last modified: Thu Mar  2 16:26:33 2023, max compression
+gzip compressed data, was "google-cloud-contact-center-insights-1.9.1.tar", last modified: Mon Mar 27 15:37:06 2023, max compression
```

## Comparing `google-cloud-contact-center-insights-1.9.0.tar` & `google-cloud-contact-center-insights-1.9.1.tar`

### file list

```diff
@@ -1,52 +1,52 @@
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/
--rw-rw-r--   0 root         (0)     1003    11358 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/LICENSE
--rw-rw-r--   0 root         (0)     1003      860 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/MANIFEST.in
--rw-r--r--   0 root         (0)     1003     4882 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/PKG-INFO
--rw-rw-r--   0 root         (0)     1003     3918 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/README.rst
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.514614 google-cloud-contact-center-insights-1.9.0/google/
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.514614 google-cloud-contact-center-insights-1.9.0/google/cloud/
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.518614 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights/
--rw-rw-r--   0 root         (0)     1003     6572 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights/__init__.py
--rw-rw-r--   0 root         (0)     1003      652 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights/gapic_version.py
--rw-rw-r--   0 root         (0)     1003       97 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.518614 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/
--rw-rw-r--   0 root         (0)     1003     6349 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003    14706 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/gapic_metadata.json
--rw-rw-r--   0 root         (0)     1003      652 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/gapic_version.py
--rw-rw-r--   0 root         (0)     1003       97 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/py.typed
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.518614 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/
--rw-rw-r--   0 root         (0)     1003      600 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.518614 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/
--rw-rw-r--   0 root         (0)     1003      797 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/__init__.py
--rw-rw-r--   0 root         (0)     1003   180859 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/async_client.py
--rw-rw-r--   0 root         (0)     1003   200552 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/client.py
--rw-rw-r--   0 root         (0)     1003    21907 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/pagers.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.518614 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/
--rw-rw-r--   0 root         (0)     1003     1519 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/__init__.py
--rw-rw-r--   0 root         (0)     1003    23726 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/base.py
--rw-rw-r--   0 root         (0)     1003    57314 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc.py
--rw-rw-r--   0 root         (0)     1003    58657 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc_asyncio.py
--rw-rw-r--   0 root         (0)     1003   208371 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/rest.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/
--rw-rw-r--   0 root         (0)     1003     6011 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/__init__.py
--rw-rw-r--   0 root         (0)     1003    51783 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/contact_center_insights.py
--rw-rw-r--   0 root         (0)     1003    76597 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/resources.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/
--rw-r--r--   0 root         (0)     1003     4882 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/PKG-INFO
--rw-r--r--   0 root         (0)     1003     2108 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0)     1003        1 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0)     1003       20 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/namespace_packages.txt
--rw-r--r--   0 root         (0)     1003        1 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/not-zip-safe
--rw-r--r--   0 root         (0)     1003      315 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/requires.txt
--rw-r--r--   0 root         (0)     1003        7 2023-03-02 16:26:33.000000 google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/top_level.txt
--rw-rw-r--   0 root         (0)     1003       67 2023-03-02 16:26:33.526615 google-cloud-contact-center-insights-1.9.0/setup.cfg
--rw-rw-r--   0 root         (0)     1003     2991 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/setup.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/tests/
--rw-rw-r--   0 root         (0)     1003      600 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/tests/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/tests/unit/
--rw-rw-r--   0 root         (0)     1003      600 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/tests/unit/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/
--rw-rw-r--   0 root         (0)     1003      600 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/__init__.py
-drwxr-sr-x   0 root         (0)     1003        0 2023-03-02 16:26:33.522615 google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/contact_center_insights_v1/
--rw-rw-r--   0 root         (0)     1003      600 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/contact_center_insights_v1/__init__.py
--rw-rw-r--   0 root         (0)     1003   869971 2023-03-02 16:24:40.000000 google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/contact_center_insights_v1/test_contact_center_insights.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.042635 google-cloud-contact-center-insights-1.9.1/
+-rw-rw-r--   0 root         (0)     1003    11358 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/LICENSE
+-rw-rw-r--   0 root         (0)     1003      860 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/MANIFEST.in
+-rw-r--r--   0 root         (0)     1003     4882 2023-03-27 15:37:06.042635 google-cloud-contact-center-insights-1.9.1/PKG-INFO
+-rw-rw-r--   0 root         (0)     1003     3918 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/README.rst
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.030634 google-cloud-contact-center-insights-1.9.1/google/
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.030634 google-cloud-contact-center-insights-1.9.1/google/cloud/
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.034634 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights/
+-rw-rw-r--   0 root         (0)     1003     6572 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights/__init__.py
+-rw-rw-r--   0 root         (0)     1003      652 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights/gapic_version.py
+-rw-rw-r--   0 root         (0)     1003       97 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.034634 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/
+-rw-rw-r--   0 root         (0)     1003     6349 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003    14706 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/gapic_metadata.json
+-rw-rw-r--   0 root         (0)     1003      652 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/gapic_version.py
+-rw-rw-r--   0 root         (0)     1003       97 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/py.typed
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.034634 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/
+-rw-rw-r--   0 root         (0)     1003      600 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.034634 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/
+-rw-rw-r--   0 root         (0)     1003      797 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/__init__.py
+-rw-rw-r--   0 root         (0)     1003   180763 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/async_client.py
+-rw-rw-r--   0 root         (0)     1003   200456 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/client.py
+-rw-rw-r--   0 root         (0)     1003    21907 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/pagers.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.038634 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/
+-rw-rw-r--   0 root         (0)     1003     1519 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/__init__.py
+-rw-rw-r--   0 root         (0)     1003    23726 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/base.py
+-rw-rw-r--   0 root         (0)     1003    57314 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc.py
+-rw-rw-r--   0 root         (0)     1003    58657 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc_asyncio.py
+-rw-rw-r--   0 root         (0)     1003   208362 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/rest.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.038634 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/
+-rw-rw-r--   0 root         (0)     1003     6011 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/__init__.py
+-rw-rw-r--   0 root         (0)     1003    51783 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/contact_center_insights.py
+-rw-rw-r--   0 root         (0)     1003    76597 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/resources.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.038634 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/
+-rw-r--r--   0 root         (0)     1003     4882 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0)     1003     2108 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0)     1003        1 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0)     1003       20 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/namespace_packages.txt
+-rw-r--r--   0 root         (0)     1003        1 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0)     1003      315 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/requires.txt
+-rw-r--r--   0 root         (0)     1003        7 2023-03-27 15:37:05.000000 google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/top_level.txt
+-rw-rw-r--   0 root         (0)     1003       67 2023-03-27 15:37:06.042635 google-cloud-contact-center-insights-1.9.1/setup.cfg
+-rw-rw-r--   0 root         (0)     1003     2991 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/setup.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.038634 google-cloud-contact-center-insights-1.9.1/tests/
+-rw-rw-r--   0 root         (0)     1003      600 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/tests/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.038634 google-cloud-contact-center-insights-1.9.1/tests/unit/
+-rw-rw-r--   0 root         (0)     1003      600 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/tests/unit/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.038634 google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/
+-rw-rw-r--   0 root         (0)     1003      600 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/__init__.py
+drwxr-sr-x   0 root         (0)     1003        0 2023-03-27 15:37:06.042635 google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/contact_center_insights_v1/
+-rw-rw-r--   0 root         (0)     1003      600 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/contact_center_insights_v1/__init__.py
+-rw-rw-r--   0 root         (0)     1003   869971 2023-03-27 15:35:07.000000 google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/contact_center_insights_v1/test_contact_center_insights.py
```

### Comparing `google-cloud-contact-center-insights-1.9.0/LICENSE` & `google-cloud-contact-center-insights-1.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/MANIFEST.in` & `google-cloud-contact-center-insights-1.9.1/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/PKG-INFO` & `google-cloud-contact-center-insights-1.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: google-cloud-contact-center-insights
-Version: 1.9.0
+Version: 1.9.1
 Summary: Google Cloud Contact Center Insights API client library
 Home-page: https://github.com/googleapis/python-contact-center-insights
 Author: Google LLC
 Author-email: googleapis-packages@google.com
 License: Apache 2.0
 Platform: Posix; MacOS X; Windows
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `google-cloud-contact-center-insights-1.9.0/README.rst` & `google-cloud-contact-center-insights-1.9.1/README.rst`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights/__init__.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights/gapic_version.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights/gapic_version.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,8 +9,8 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
-__version__ = "1.9.0"  # {x-release-please-version}
+__version__ = "1.9.1"  # {x-release-please-version}
```

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/__init__.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/gapic_metadata.json` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/gapic_metadata.json`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/gapic_version.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/gapic_version.py`

 * *Files 0% similar despite different names*

```diff
@@ -9,8 +9,8 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 #
-__version__ = "1.9.0"  # {x-release-please-version}
+__version__ = "1.9.1"  # {x-release-please-version}
```

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/__init__.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/__init__.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/async_client.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/async_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -418,16 +418,15 @@
                 response = await client.update_conversation(request=request)
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.UpdateConversationRequest, dict]]):
-                The request object. The request to update a
-                conversation.
+                The request object. The request to update a conversation.
             conversation (:class:`google.cloud.contact_center_insights_v1.types.Conversation`):
                 Required. The new values for the
                 conversation.
 
                 This corresponds to the ``conversation`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -743,16 +742,15 @@
                 )
 
                 # Make the request
                 await client.delete_conversation(request=request)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.DeleteConversationRequest, dict]]):
-                The request object. The request to delete a
-                conversation.
+                The request object. The request to delete a conversation.
             name (:class:`str`):
                 Required. The name of the
                 conversation to delete.
 
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -1668,16 +1666,15 @@
                 response = (await operation).result()
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.CreateIssueModelRequest, dict]]):
-                The request object. The request to create an issue
-                model.
+                The request object. The request to create an issue model.
             parent (:class:`str`):
                 Required. The parent resource of the
                 issue model.
 
                 This corresponds to the ``parent`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -1790,16 +1787,15 @@
                 response = await client.update_issue_model(request=request)
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.UpdateIssueModelRequest, dict]]):
-                The request object. The request to update an issue
-                model.
+                The request object. The request to update an issue model.
             issue_model (:class:`google.cloud.contact_center_insights_v1.types.IssueModel`):
                 Required. The new values for the
                 issue model.
 
                 This corresponds to the ``issue_model`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -2107,16 +2103,15 @@
                 response = (await operation).result()
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.DeleteIssueModelRequest, dict]]):
-                The request object. The request to delete an issue
-                model.
+                The request object. The request to delete an issue model.
             name (:class:`str`):
                 Required. The name of the issue model
                 to delete.
 
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -2235,16 +2230,15 @@
                 response = (await operation).result()
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.DeployIssueModelRequest, dict]]):
-                The request object. The request to deploy an issue
-                model.
+                The request object. The request to deploy an issue model.
             name (:class:`str`):
                 Required. The issue model to deploy.
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
@@ -2870,16 +2864,16 @@
                 response = await client.calculate_issue_model_stats(request=request)
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Optional[Union[google.cloud.contact_center_insights_v1.types.CalculateIssueModelStatsRequest, dict]]):
-                The request object. Request to get statistics of an
-                issue model.
+                The request object. Request to get statistics of an issue
+                model.
             issue_model (:class:`str`):
                 Required. The resource name of the
                 issue model to query against.
 
                 This corresponds to the ``issue_model`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
```

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/client.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/client.py`

 * *Files 0% similar despite different names*

```diff
@@ -779,16 +779,15 @@
                 response = client.update_conversation(request=request)
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.UpdateConversationRequest, dict]):
-                The request object. The request to update a
-                conversation.
+                The request object. The request to update a conversation.
             conversation (google.cloud.contact_center_insights_v1.types.Conversation):
                 Required. The new values for the
                 conversation.
 
                 This corresponds to the ``conversation`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -1104,16 +1103,15 @@
                 )
 
                 # Make the request
                 client.delete_conversation(request=request)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.DeleteConversationRequest, dict]):
-                The request object. The request to delete a
-                conversation.
+                The request object. The request to delete a conversation.
             name (str):
                 Required. The name of the
                 conversation to delete.
 
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -2033,16 +2031,15 @@
                 response = operation.result()
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.CreateIssueModelRequest, dict]):
-                The request object. The request to create an issue
-                model.
+                The request object. The request to create an issue model.
             parent (str):
                 Required. The parent resource of the
                 issue model.
 
                 This corresponds to the ``parent`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -2155,16 +2152,15 @@
                 response = client.update_issue_model(request=request)
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.UpdateIssueModelRequest, dict]):
-                The request object. The request to update an issue
-                model.
+                The request object. The request to update an issue model.
             issue_model (google.cloud.contact_center_insights_v1.types.IssueModel):
                 Required. The new values for the
                 issue model.
 
                 This corresponds to the ``issue_model`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -2472,16 +2468,15 @@
                 response = operation.result()
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.DeleteIssueModelRequest, dict]):
-                The request object. The request to delete an issue
-                model.
+                The request object. The request to delete an issue model.
             name (str):
                 Required. The name of the issue model
                 to delete.
 
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
@@ -2600,16 +2595,15 @@
                 response = operation.result()
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.DeployIssueModelRequest, dict]):
-                The request object. The request to deploy an issue
-                model.
+                The request object. The request to deploy an issue model.
             name (str):
                 Required. The issue model to deploy.
                 This corresponds to the ``name`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
             retry (google.api_core.retry.Retry): Designation of what errors, if any,
                 should be retried.
@@ -3235,16 +3229,16 @@
                 response = client.calculate_issue_model_stats(request=request)
 
                 # Handle the response
                 print(response)
 
         Args:
             request (Union[google.cloud.contact_center_insights_v1.types.CalculateIssueModelStatsRequest, dict]):
-                The request object. Request to get statistics of an
-                issue model.
+                The request object. Request to get statistics of an issue
+                model.
             issue_model (str):
                 Required. The resource name of the
                 issue model to query against.
 
                 This corresponds to the ``issue_model`` field
                 on the ``request`` instance; if ``request`` is provided, this
                 should not be set.
```

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/pagers.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/pagers.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/__init__.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/base.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/base.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc_asyncio.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/grpc_asyncio.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/rest.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/services/contact_center_insights/transports/rest.py`

 * *Files 0% similar despite different names*

```diff
@@ -1425,15 +1425,14 @@
             r"""Call the bulk analyze
             conversations method over HTTP.
 
                 Args:
                     request (~.contact_center_insights.BulkAnalyzeConversationsRequest):
                         The request object. The request to analyze conversations
                     in bulk.
-
                     retry (google.api_core.retry.Retry): Designation of what errors, if any,
                         should be retried.
                     timeout (float): The timeout for this request.
                     metadata (Sequence[Tuple[str, str]]): Strings which should be
                         sent along with the request as metadata.
 
                 Returns:
@@ -1528,15 +1527,14 @@
             r"""Call the calculate issue model
             stats method over HTTP.
 
                 Args:
                     request (~.contact_center_insights.CalculateIssueModelStatsRequest):
                         The request object. Request to get statistics of an issue
                     model.
-
                     retry (google.api_core.retry.Retry): Designation of what errors, if any,
                         should be retried.
                     timeout (float): The timeout for this request.
                     metadata (Sequence[Tuple[str, str]]): Strings which should be
                         sent along with the request as metadata.
 
                 Returns:
@@ -1622,15 +1620,14 @@
         ) -> contact_center_insights.CalculateStatsResponse:
             r"""Call the calculate stats method over HTTP.
 
             Args:
                 request (~.contact_center_insights.CalculateStatsRequest):
                     The request object. The request for calculating
                 conversation statistics.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
 
             Returns:
@@ -2508,15 +2505,14 @@
         ):
             r"""Call the delete phrase matcher method over HTTP.
 
             Args:
                 request (~.contact_center_insights.DeletePhraseMatcherRequest):
                     The request object. The request to delete a phrase
                 matcher.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
             """
 
@@ -3202,15 +3198,14 @@
         ) -> resources.PhraseMatcher:
             r"""Call the get phrase matcher method over HTTP.
 
             Args:
                 request (~.contact_center_insights.GetPhraseMatcherRequest):
                     The request object. The request to get a a phrase
                 matcher.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
 
             Returns:
@@ -3292,15 +3287,14 @@
         ) -> resources.Settings:
             r"""Call the get settings method over HTTP.
 
             Args:
                 request (~.contact_center_insights.GetSettingsRequest):
                     The request object. The request to get project-level
                 settings.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
 
             Returns:
@@ -4090,15 +4084,14 @@
         ) -> operations_pb2.Operation:
             r"""Call the undeploy issue model method over HTTP.
 
             Args:
                 request (~.contact_center_insights.UndeployIssueModelRequest):
                     The request object. The request to undeploy an issue
                 model.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
 
             Returns:
@@ -4479,15 +4472,14 @@
         ) -> resources.PhraseMatcher:
             r"""Call the update phrase matcher method over HTTP.
 
             Args:
                 request (~.contact_center_insights.UpdatePhraseMatcherRequest):
                     The request object. The request to update a phrase
                 matcher.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
 
             Returns:
@@ -4580,15 +4572,14 @@
         ) -> resources.Settings:
             r"""Call the update settings method over HTTP.
 
             Args:
                 request (~.contact_center_insights.UpdateSettingsRequest):
                     The request object. The request to update project-level
                 settings.
-
                 retry (google.api_core.retry.Retry): Designation of what errors, if any,
                     should be retried.
                 timeout (float): The timeout for this request.
                 metadata (Sequence[Tuple[str, str]]): Strings which should be
                     sent along with the request as metadata.
 
             Returns:
```

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/__init__.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/contact_center_insights.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/contact_center_insights.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google/cloud/contact_center_insights_v1/types/resources.py` & `google-cloud-contact-center-insights-1.9.1/google/cloud/contact_center_insights_v1/types/resources.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/PKG-INFO` & `google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: google-cloud-contact-center-insights
-Version: 1.9.0
+Version: 1.9.1
 Summary: Google Cloud Contact Center Insights API client library
 Home-page: https://github.com/googleapis/python-contact-center-insights
 Author: Google LLC
 Author-email: googleapis-packages@google.com
 License: Apache 2.0
 Platform: Posix; MacOS X; Windows
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `google-cloud-contact-center-insights-1.9.0/google_cloud_contact_center_insights.egg-info/SOURCES.txt` & `google-cloud-contact-center-insights-1.9.1/google_cloud_contact_center_insights.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/setup.py` & `google-cloud-contact-center-insights-1.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/tests/__init__.py` & `google-cloud-contact-center-insights-1.9.1/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/tests/unit/__init__.py` & `google-cloud-contact-center-insights-1.9.1/tests/unit/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/__init__.py` & `google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/contact_center_insights_v1/__init__.py` & `google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/contact_center_insights_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `google-cloud-contact-center-insights-1.9.0/tests/unit/gapic/contact_center_insights_v1/test_contact_center_insights.py` & `google-cloud-contact-center-insights-1.9.1/tests/unit/gapic/contact_center_insights_v1/test_contact_center_insights.py`

 * *Files identical despite different names*

