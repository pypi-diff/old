# Comparing `tmp/krkn_lib_kubernetes_draft-0.1.6.tar.gz` & `tmp/krkn_lib_kubernetes_draft-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "krkn_lib_kubernetes_draft-0.1.6.tar", max compression
+gzip compressed data, was "krkn_lib_kubernetes_draft-0.1.7.tar", max compression
```

## Comparing `krkn_lib_kubernetes_draft-0.1.6.tar` & `krkn_lib_kubernetes_draft-0.1.7.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0    10173 2023-04-06 15:41:25.728448 krkn_lib_kubernetes_draft-0.1.6/LICENSE
--rw-r--r--   0        0        0       22 2023-04-06 15:41:25.728448 krkn_lib_kubernetes_draft-0.1.6/README.md
--rw-r--r--   0        0        0      502 2023-04-06 15:41:25.804449 krkn_lib_kubernetes_draft-0.1.6/pyproject.toml
--rw-r--r--   0        0        0       63 2023-04-06 15:41:25.728448 krkn_lib_kubernetes_draft-0.1.6/src/krkn_lib_kubernetes_draft/__init__.py
--rw-r--r--   0        0        0    39791 2023-04-06 15:41:37.828721 krkn_lib_kubernetes_draft-0.1.6/src/krkn_lib_kubernetes_draft/client.py
--rw-r--r--   0        0        0     1690 2023-04-06 15:41:25.732448 krkn_lib_kubernetes_draft-0.1.6/src/krkn_lib_kubernetes_draft/resources.py
--rw-r--r--   0        0        0      671 1970-01-01 00:00:00.000000 krkn_lib_kubernetes_draft-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0    10173 2023-04-06 15:46:32.348308 krkn_lib_kubernetes_draft-0.1.7/LICENSE
+-rw-r--r--   0        0        0       22 2023-04-06 15:46:32.348308 krkn_lib_kubernetes_draft-0.1.7/README.md
+-rw-r--r--   0        0        0      539 2023-04-06 15:46:32.412308 krkn_lib_kubernetes_draft-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0       63 2023-04-06 15:46:32.348308 krkn_lib_kubernetes_draft-0.1.7/src/krkn_lib_kubernetes_draft/__init__.py
+-rw-r--r--   0        0        0    39745 2023-04-06 15:46:44.396272 krkn_lib_kubernetes_draft-0.1.7/src/krkn_lib_kubernetes_draft/client.py
+-rw-r--r--   0        0        0     1690 2023-04-06 15:46:32.348308 krkn_lib_kubernetes_draft-0.1.7/src/krkn_lib_kubernetes_draft/resources.py
+-rw-r--r--   0        0        0      732 1970-01-01 00:00:00.000000 krkn_lib_kubernetes_draft-0.1.7/PKG-INFO
```

### Comparing `krkn_lib_kubernetes_draft-0.1.6/LICENSE` & `krkn_lib_kubernetes_draft-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `krkn_lib_kubernetes_draft-0.1.6/src/krkn_lib_kubernetes_draft/client.py` & `krkn_lib_kubernetes_draft-0.1.7/src/krkn_lib_kubernetes_draft/client.py`

 * *Files 0% similar despite different names*

```diff
@@ -124,17 +124,15 @@
 
     def get_host(self) -> str:
         """
         Returns the Kubernetes server URL
         :return: kubernetes server URL
         """
 
-        return (
-            self.cli.api_client.configuration.Configuration.get_default_copy().host  # NOQA
-        )
+        return self.cli.api_client.configuration.get_default_copy().host
 
     def get_clusterversion_string(self) -> str:
         """
         Return clusterversion status text on OpenShift, empty string
         on other distributions
 
         :return: clusterversion status
```

### Comparing `krkn_lib_kubernetes_draft-0.1.6/src/krkn_lib_kubernetes_draft/resources.py` & `krkn_lib_kubernetes_draft-0.1.7/src/krkn_lib_kubernetes_draft/resources.py`

 * *Files identical despite different names*

### Comparing `krkn_lib_kubernetes_draft-0.1.6/PKG-INFO` & `krkn_lib_kubernetes_draft-0.1.7/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 Metadata-Version: 2.1
 Name: krkn-lib-kubernetes-draft
-Version: 0.1.6
+Version: 0.1.7
 Summary: Kubernetes library for Kraken
 Home-page: https://github.com/redhat-chaos/krkn
 License: Apache-2.0
 Author: Red Hat Chaos Engineering Team
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Dist: arcaflow-lib-kubernetes (>=0.1.1,<0.2.0)
 Requires-Dist: kubernetes (>=26.0.0,<27.0.0)
+Requires-Dist: sphinxnotes-markdown-builder (>=0.5.6,<0.6.0)
 Description-Content-Type: text/markdown
 
 # krkn-lib-kubernetes
```

