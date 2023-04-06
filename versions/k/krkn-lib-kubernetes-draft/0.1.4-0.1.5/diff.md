# Comparing `tmp/krkn_lib_kubernetes_draft-0.1.4.tar.gz` & `tmp/krkn_lib_kubernetes_draft-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "krkn_lib_kubernetes_draft-0.1.4.tar", max compression
+gzip compressed data, was "krkn_lib_kubernetes_draft-0.1.5.tar", max compression
```

## Comparing `krkn_lib_kubernetes_draft-0.1.4.tar` & `krkn_lib_kubernetes_draft-0.1.5.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0    10173 2023-04-06 14:37:29.834102 krkn_lib_kubernetes_draft-0.1.4/LICENSE
--rw-r--r--   0        0        0       22 2023-04-06 14:37:29.834102 krkn_lib_kubernetes_draft-0.1.4/README.md
--rw-r--r--   0        0        0      502 2023-04-06 14:37:29.910103 krkn_lib_kubernetes_draft-0.1.4/pyproject.toml
--rw-r--r--   0        0        0       63 2023-04-06 14:37:29.834102 krkn_lib_kubernetes_draft-0.1.4/src/krkn_lib_kubernetes_draft/__init__.py
--rw-r--r--   0        0        0    39679 2023-04-06 14:37:42.654253 krkn_lib_kubernetes_draft-0.1.4/src/krkn_lib_kubernetes_draft/client.py
--rw-r--r--   0        0        0     1690 2023-04-06 14:37:29.834102 krkn_lib_kubernetes_draft-0.1.4/src/krkn_lib_kubernetes_draft/resources.py
--rw-r--r--   0        0        0      671 1970-01-01 00:00:00.000000 krkn_lib_kubernetes_draft-0.1.4/PKG-INFO
+-rw-r--r--   0        0        0    10173 2023-04-06 15:04:10.949030 krkn_lib_kubernetes_draft-0.1.5/LICENSE
+-rw-r--r--   0        0        0       22 2023-04-06 15:04:10.949030 krkn_lib_kubernetes_draft-0.1.5/README.md
+-rw-r--r--   0        0        0      502 2023-04-06 15:04:11.017031 krkn_lib_kubernetes_draft-0.1.5/pyproject.toml
+-rw-r--r--   0        0        0       63 2023-04-06 15:04:10.953030 krkn_lib_kubernetes_draft-0.1.5/src/krkn_lib_kubernetes_draft/__init__.py
+-rw-r--r--   0        0        0    39679 2023-04-06 15:04:22.865116 krkn_lib_kubernetes_draft-0.1.5/src/krkn_lib_kubernetes_draft/client.py
+-rw-r--r--   0        0        0     1690 2023-04-06 15:04:10.953030 krkn_lib_kubernetes_draft-0.1.5/src/krkn_lib_kubernetes_draft/resources.py
+-rw-r--r--   0        0        0      671 1970-01-01 00:00:00.000000 krkn_lib_kubernetes_draft-0.1.5/PKG-INFO
```

### Comparing `krkn_lib_kubernetes_draft-0.1.4/LICENSE` & `krkn_lib_kubernetes_draft-0.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `krkn_lib_kubernetes_draft-0.1.4/src/krkn_lib_kubernetes_draft/client.py` & `krkn_lib_kubernetes_draft-0.1.5/src/krkn_lib_kubernetes_draft/client.py`

 * *Files identical despite different names*

### Comparing `krkn_lib_kubernetes_draft-0.1.4/src/krkn_lib_kubernetes_draft/resources.py` & `krkn_lib_kubernetes_draft-0.1.5/src/krkn_lib_kubernetes_draft/resources.py`

 * *Files identical despite different names*

### Comparing `krkn_lib_kubernetes_draft-0.1.4/PKG-INFO` & `krkn_lib_kubernetes_draft-0.1.5/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: krkn-lib-kubernetes-draft
-Version: 0.1.4
+Version: 0.1.5
 Summary: Kubernetes library for Kraken
 Home-page: https://github.com/redhat-chaos/krkn
 License: Apache-2.0
 Author: Red Hat Chaos Engineering Team
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
```

