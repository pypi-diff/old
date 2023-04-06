# Comparing `tmp/procaine-0.4.0.tar.gz` & `tmp/procaine-0.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "procaine-0.4.0.tar", last modified: Tue Apr  4 13:08:48 2023, max compression
+gzip compressed data, was "procaine-0.4.1.tar", last modified: Thu Apr  6 13:16:41 2023, max compression
```

## Comparing `procaine-0.4.0.tar` & `procaine-0.4.1.tar`

### file list

```diff
@@ -1,7 +1,6 @@
--rw-r--r--   0        0        0    18092 2022-07-08 17:29:10.701129 procaine-0.4.0/LICENSE.txt
--rw-r--r--   0        0        0     1232 2022-10-28 16:18:46.290248 procaine-0.4.0/README.rst
--rw-r--r--   0        0        0        0 2023-03-16 16:41:42.869159 procaine-0.4.0/procaine/#__init__.py#
--rw-r--r--   0        0        0        0 2022-07-08 17:29:10.701129 procaine-0.4.0/procaine/__init__.py
--rw-r--r--   0        0        0    20349 2023-04-04 13:01:33.126604 procaine-0.4.0/procaine/aicore.py
--rw-r--r--   0        0        0     1382 2023-04-04 13:04:59.254875 procaine-0.4.0/pyproject.toml
--rw-r--r--   0        0        0     2559 1970-01-01 00:00:00.000000 procaine-0.4.0/PKG-INFO
+-rw-r--r--   0        0        0    18092 2022-07-08 17:29:10.701129 procaine-0.4.1/LICENSE.txt
+-rw-r--r--   0        0        0     1232 2022-10-28 16:18:46.290248 procaine-0.4.1/README.rst
+-rw-r--r--   0        0        0        0 2022-07-08 17:29:10.701129 procaine-0.4.1/procaine/__init__.py
+-rw-r--r--   0        0        0    20351 2023-04-06 13:10:23.628329 procaine-0.4.1/procaine/aicore.py
+-rw-r--r--   0        0        0     1382 2023-04-06 13:14:08.292948 procaine-0.4.1/pyproject.toml
+-rw-r--r--   0        0        0     2559 1970-01-01 00:00:00.000000 procaine-0.4.1/PKG-INFO
```

### Comparing `procaine-0.4.0/LICENSE.txt` & `procaine-0.4.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `procaine-0.4.0/README.rst` & `procaine-0.4.1/README.rst`

 * *Files identical despite different names*

### Comparing `procaine-0.4.0/procaine/aicore.py` & `procaine-0.4.1/procaine/aicore.py`

 * *Files 0% similar despite different names*

```diff
@@ -548,15 +548,15 @@
         """Shows pods' logs of a deployment.
 
         :param deployment: Deployment object or ID.
         """
         logs = self.sess.get(
             urljoin(self.url, f"/v2/lm/deployments/{getid(deployment)}/logs")
         ).json()
-        return "".join([x["msg"] for x in logs["data"]["result"]])
+        return "\n".join([x["msg"] for x in logs["data"]["result"]])
 
     def stop_deployment(self, deployment):
         """Stops a model server.
 
         :param deployment: Deployment object or ID.
         """
         return self.sess.patch(
```

### Comparing `procaine-0.4.0/pyproject.toml` & `procaine-0.4.1/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "procaine"
-version = "0.4.0"
+version = "0.4.1"
 description = "A REST client library for SAP AI Core API."
 readme = "README.rst"
 requires-python = ">=3.7"
 license = {file = "LICENSE.txt"}
 keywords = ["AI Core", "AICore", "AI API", "ai-api"]
 authors = [{name = "romk"}]
 classifiers = [
```

### Comparing `procaine-0.4.0/PKG-INFO` & `procaine-0.4.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: procaine
-Version: 0.4.0
+Version: 0.4.1
 Summary: A REST client library for SAP AI Core API.
 Keywords: AI Core,AICore,AI API,ai-api
 Author: romk
 Requires-Python: >=3.7
 Description-Content-Type: text/x-rst
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

