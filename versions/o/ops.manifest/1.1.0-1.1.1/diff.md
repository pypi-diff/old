# Comparing `tmp/ops.manifest-1.1.0.tar.gz` & `tmp/ops.manifest-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ops.manifest-1.1.0.tar", last modified: Fri Feb 17 21:43:39 2023, max compression
+gzip compressed data, was "ops.manifest-1.1.1.tar", last modified: Thu Apr  6 19:05:56 2023, max compression
```

## Comparing `ops.manifest-1.1.0.tar` & `ops.manifest-1.1.1.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-02-17 21:43:39.751177 ops.manifest-1.1.0/
--rw-rw-r--   0 addyess   (1000) addyess   (1000)    11357 2023-02-06 20:40:33.000000 ops.manifest-1.1.0/LICENSE
--rw-rw-r--   0 addyess   (1000) addyess   (1000)    23732 2023-02-17 21:43:39.751177 ops.manifest-1.1.0/PKG-INFO
--rw-rw-r--   0 addyess   (1000) addyess   (1000)    10740 2022-08-26 13:28:24.000000 ops.manifest-1.1.0/README.md
-drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-02-17 21:43:39.747177 ops.manifest-1.1.0/ops/
-drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-02-17 21:43:39.751177 ops.manifest-1.1.0/ops/manifests/
--rw-rw-r--   0 addyess   (1000) addyess   (1000)      522 2023-02-06 17:02:56.000000 ops.manifest-1.1.0/ops/manifests/__init__.py
--rw-rw-r--   0 addyess   (1000) addyess   (1000)     6614 2023-02-06 17:02:56.000000 ops.manifest-1.1.0/ops/manifests/collector.py
--rw-rw-r--   0 addyess   (1000) addyess   (1000)      197 2023-02-06 17:02:56.000000 ops.manifest-1.1.0/ops/manifests/exceptions.py
--rw-rw-r--   0 addyess   (1000) addyess   (1000)    10984 2023-02-06 20:40:33.000000 ops.manifest-1.1.0/ops/manifests/manifest.py
--rw-rw-r--   0 addyess   (1000) addyess   (1000)     9932 2023-02-17 21:43:29.000000 ops.manifest-1.1.0/ops/manifests/manipulations.py
-drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-02-17 21:43:39.751177 ops.manifest-1.1.0/ops.manifest.egg-info/
--rw-rw-r--   0 addyess   (1000) addyess   (1000)    23732 2023-02-17 21:43:39.000000 ops.manifest-1.1.0/ops.manifest.egg-info/PKG-INFO
--rw-rw-r--   0 addyess   (1000) addyess   (1000)      399 2023-02-17 21:43:39.000000 ops.manifest-1.1.0/ops.manifest.egg-info/SOURCES.txt
--rw-rw-r--   0 addyess   (1000) addyess   (1000)        1 2023-02-17 21:43:39.000000 ops.manifest-1.1.0/ops.manifest.egg-info/dependency_links.txt
--rw-rw-r--   0 addyess   (1000) addyess   (1000)       40 2023-02-17 21:43:39.000000 ops.manifest-1.1.0/ops.manifest.egg-info/requires.txt
--rw-rw-r--   0 addyess   (1000) addyess   (1000)        4 2023-02-17 21:43:39.000000 ops.manifest-1.1.0/ops.manifest.egg-info/top_level.txt
--rw-rw-r--   0 addyess   (1000) addyess   (1000)        1 2023-02-06 18:03:47.000000 ops.manifest-1.1.0/ops.manifest.egg-info/zip-safe
--rw-rw-r--   0 addyess   (1000) addyess   (1000)       80 2023-02-06 20:40:33.000000 ops.manifest-1.1.0/pyproject.toml
--rw-rw-r--   0 addyess   (1000) addyess   (1000)      979 2023-02-17 21:43:39.751177 ops.manifest-1.1.0/setup.cfg
--rw-rw-r--   0 addyess   (1000) addyess   (1000)      116 2023-02-06 20:40:33.000000 ops.manifest-1.1.0/setup.py
+drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-04-06 19:05:56.840496 ops.manifest-1.1.1/
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)    11357 2023-02-06 20:40:33.000000 ops.manifest-1.1.1/LICENSE
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)    23732 2023-04-06 19:05:56.840496 ops.manifest-1.1.1/PKG-INFO
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)    10740 2022-08-26 13:28:24.000000 ops.manifest-1.1.1/README.md
+drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-04-06 19:05:56.836496 ops.manifest-1.1.1/ops/
+drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-04-06 19:05:56.840496 ops.manifest-1.1.1/ops/manifests/
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)      522 2023-02-06 17:02:56.000000 ops.manifest-1.1.1/ops/manifests/__init__.py
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)     6614 2023-02-06 17:02:56.000000 ops.manifest-1.1.1/ops/manifests/collector.py
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)      197 2023-02-06 17:02:56.000000 ops.manifest-1.1.1/ops/manifests/exceptions.py
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)    11154 2023-04-06 19:02:14.000000 ops.manifest-1.1.1/ops/manifests/manifest.py
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)     9932 2023-03-10 16:45:29.000000 ops.manifest-1.1.1/ops/manifests/manipulations.py
+drwxrwxr-x   0 addyess   (1000) addyess   (1000)        0 2023-04-06 19:05:56.840496 ops.manifest-1.1.1/ops.manifest.egg-info/
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)    23732 2023-04-06 19:05:56.000000 ops.manifest-1.1.1/ops.manifest.egg-info/PKG-INFO
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)      399 2023-04-06 19:05:56.000000 ops.manifest-1.1.1/ops.manifest.egg-info/SOURCES.txt
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)        1 2023-04-06 19:05:56.000000 ops.manifest-1.1.1/ops.manifest.egg-info/dependency_links.txt
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)       40 2023-04-06 19:05:56.000000 ops.manifest-1.1.1/ops.manifest.egg-info/requires.txt
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)        4 2023-04-06 19:05:56.000000 ops.manifest-1.1.1/ops.manifest.egg-info/top_level.txt
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)        1 2023-02-06 18:03:47.000000 ops.manifest-1.1.1/ops.manifest.egg-info/zip-safe
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)       80 2023-02-06 20:40:33.000000 ops.manifest-1.1.1/pyproject.toml
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)      979 2023-04-06 19:05:56.840496 ops.manifest-1.1.1/setup.cfg
+-rw-rw-r--   0 addyess   (1000) addyess   (1000)      116 2023-02-06 20:40:33.000000 ops.manifest-1.1.1/setup.py
```

### Comparing `ops.manifest-1.1.0/LICENSE` & `ops.manifest-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `ops.manifest-1.1.0/PKG-INFO` & `ops.manifest-1.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ops.manifest
-Version: 1.1.0
+Version: 1.1.1
 Summary: "Kubernetes manifests for Operators"
 Home-page: https://github.com/canonical/ops-lib-manifest
 Author: Adam Dyess
 Author-email: adam.dyess@canonical.com
 License: Apache
 Keywords: juju,charming,kubernetes,operators,manifests,yaml
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `ops.manifest-1.1.0/README.md` & `ops.manifest-1.1.1/README.md`

 * *Files identical despite different names*

### Comparing `ops.manifest-1.1.0/ops/manifests/__init__.py` & `ops.manifest-1.1.1/ops/manifests/__init__.py`

 * *Files identical despite different names*

### Comparing `ops.manifest-1.1.0/ops/manifests/collector.py` & `ops.manifest-1.1.1/ops/manifests/collector.py`

 * *Files identical despite different names*

### Comparing `ops.manifest-1.1.0/ops/manifests/manifest.py` & `ops.manifest-1.1.1/ops/manifests/manifest.py`

 * *Files 10% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 from collections import OrderedDict, namedtuple
 from functools import lru_cache
 from pathlib import Path
 from typing import Dict, FrozenSet, KeysView, List, Mapping, Optional, Union
 
 import yaml
 from backports.cached_property import cached_property
-from httpx import HTTPStatusError
+from httpx import HTTPError
 from lightkube import Client, codecs
 from lightkube.codecs import AnyResource
 from lightkube.core.exceptions import ApiError
 from lightkube.generic_resource import (
     create_resources_from_crd,
     load_in_cluster_generic_resources,
 )
@@ -91,15 +91,20 @@
         else:
             self.manipulations = manipulations
 
     @cached_property
     def client(self) -> Client:
         """Lazy evaluation of the lightkube client."""
         client = Client(field_manager=f"{self.model.app.name}-{self.name}")
-        load_in_cluster_generic_resources(client)
+        msg = "Failed to load in cluster CRDs"
+        try:
+            load_in_cluster_generic_resources(client)
+        except (ApiError, HTTPError) as ex:
+            log.exception(msg)
+            raise ManifestClientError(msg, ex) from ex
         return client
 
     @property
     def config(self) -> Dict:
         """Retrieve the current available config to use during manifest building."""
         raise NotImplementedError
 
@@ -226,15 +231,15 @@
         for obj in self.resources:
             try:
                 next_rsc = self.client.get(
                     type(obj.resource),
                     obj.name,
                     namespace=obj.namespace,
                 )
-            except (ApiError, HTTPStatusError):
+            except (ApiError, HTTPError):
                 log.exception(f"Didn't find expected resource installed ({obj})")
                 continue
             result[HashableResource(next_rsc)] = None
         return frozenset(result.keys())
 
     def labelled_resources(self) -> FrozenSet[HashableResource]:
         """Any resource ever installed and labeled by this class."""
@@ -271,15 +276,15 @@
         @param *resources: set of resourecs to apply
         """
         for rsc in resources:
             log.info(f"Applying {rsc}")
             msg = f"Failed Applying {rsc}"
             try:
                 self.client.apply(rsc.resource, force=True)
-            except (ApiError, HTTPStatusError) as ex:
+            except (ApiError, HTTPError) as ex:
                 log.exception(msg)
                 raise ManifestClientError(msg, ex) from ex
         log.info(f"Applied {len(resources)} Resources")
 
     def delete_resources(
         self,
         *resources: HashableResource,
@@ -289,15 +294,15 @@
     ):
         """Delete specific resources."""
         for obj in resources:
             log.info(f"Deleting {obj}...")
             try:
                 namespace = obj.namespace or namespace
                 self.client.delete(type(obj.resource), obj.name, namespace=namespace)
-            except (ApiError, HTTPStatusError) as ex:
+            except (ApiError, HTTPError) as ex:
                 msg = str(ex)
                 if hasattr(ex, "status") and ex.status.message is not None:
                     msg = ex.status.message
                 not_found = ignore_not_found and "not found" in msg.lower()
                 unauthed = ignore_unauthorized and "(unauthorized)" in msg.lower()
                 if not_found or unauthed:
                     log.warning(f"Ignored failed delete of resource: {obj}")
```

### Comparing `ops.manifest-1.1.0/ops/manifests/manipulations.py` & `ops.manifest-1.1.1/ops/manifests/manipulations.py`

 * *Files identical despite different names*

### Comparing `ops.manifest-1.1.0/ops.manifest.egg-info/PKG-INFO` & `ops.manifest-1.1.1/ops.manifest.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ops.manifest
-Version: 1.1.0
+Version: 1.1.1
 Summary: "Kubernetes manifests for Operators"
 Home-page: https://github.com/canonical/ops-lib-manifest
 Author: Adam Dyess
 Author-email: adam.dyess@canonical.com
 License: Apache
 Keywords: juju,charming,kubernetes,operators,manifests,yaml
 Classifier: License :: OSI Approved :: Apache Software License
```

### Comparing `ops.manifest-1.1.0/setup.cfg` & `ops.manifest-1.1.1/setup.cfg`

 * *Files 21% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = ops.manifest
-version = 1.1.0
+version = 1.1.1
 author = Adam Dyess
 author_email = adam.dyess@canonical.com
 description = "Kubernetes manifests for Operators"
 long_description = file: README.md, CHANGELOG.md, LICENSE
 long_description_content_type = text/markdown
 keywords = juju, charming, kubernetes, operators, manifests, yaml
 license = Apache
```

