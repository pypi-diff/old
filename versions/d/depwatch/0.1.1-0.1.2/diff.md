# Comparing `tmp/depwatch-0.1.1.tar.gz` & `tmp/depwatch-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "depwatch-0.1.1.tar", last modified: Sat Mar 11 04:05:04 2023, max compression
+gzip compressed data, was "depwatch-0.1.2.tar", last modified: Fri Apr  7 00:06:06 2023, max compression
```

## Comparing `depwatch-0.1.1.tar` & `depwatch-0.1.2.tar`

### file list

```diff
@@ -1,15 +1,18 @@
--rw-r--r--   0        0        0     1067 2023-03-11 04:04:45.021556 depwatch-0.1.1/LICENSE
--rw-r--r--   0        0        0     2071 2023-03-11 04:04:45.021556 depwatch-0.1.1/README.md
--rw-r--r--   0        0        0        0 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/__init__.py
--rw-r--r--   0        0        0      695 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/command.py
--rw-r--r--   0        0        0     1547 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/deployment.py
--rw-r--r--   0        0        0       45 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/exception.py
--rw-r--r--   0        0        0     2047 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/history.py
--rw-r--r--   0        0        0      519 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/main.py
--rw-r--r--   0        0        0      731 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/presentation.py
--rw-r--r--   0        0        0     1294 2023-03-11 04:04:45.021556 depwatch-0.1.1/depwatch/repository.py
--rw-r--r--   0        0        0     1209 2023-03-11 04:04:45.025556 depwatch-0.1.1/pyproject.toml
--rw-r--r--   0        0        0        0 2023-03-11 04:04:45.025556 depwatch-0.1.1/tests/__init__.py
--rw-r--r--   0        0        0     1631 2023-03-11 04:04:45.025556 depwatch-0.1.1/tests/test_command.py
--rw-r--r--   0        0        0     2837 2023-03-11 04:04:45.025556 depwatch-0.1.1/tests/test_history.py
--rw-r--r--   0        0        0     2402 1970-01-01 00:00:00.000000 depwatch-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0     1067 2023-04-07 00:05:48.622200 depwatch-0.1.2/LICENSE
+-rw-r--r--   0        0        0     2071 2023-04-07 00:05:48.622200 depwatch-0.1.2/README.md
+-rw-r--r--   0        0        0        0 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/__init__.py
+-rw-r--r--   0        0        0      689 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/command.py
+-rw-r--r--   0        0        0     1568 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/deployment.py
+-rw-r--r--   0        0        0       45 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/exception.py
+-rw-r--r--   0        0        0     2047 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/history.py
+-rw-r--r--   0        0        0      519 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/main.py
+-rw-r--r--   0        0        0     1293 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/repository.py
+-rw-r--r--   0        0        0      731 2023-04-07 00:05:48.622200 depwatch-0.1.2/depwatch/writer.py
+-rw-r--r--   0        0        0     1209 2023-04-07 00:05:48.622200 depwatch-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-07 00:05:48.622200 depwatch-0.1.2/tests/__init__.py
+-rw-r--r--   0        0        0     1631 2023-04-07 00:05:48.626200 depwatch-0.1.2/tests/test_command.py
+-rw-r--r--   0        0        0     4466 2023-04-07 00:05:48.626200 depwatch-0.1.2/tests/test_deployment.py
+-rw-r--r--   0        0        0     2837 2023-04-07 00:05:48.626200 depwatch-0.1.2/tests/test_history.py
+-rw-r--r--   0        0        0     3217 2023-04-07 00:05:48.626200 depwatch-0.1.2/tests/test_repository.py
+-rw-r--r--   0        0        0     1820 2023-04-07 00:05:48.626200 depwatch-0.1.2/tests/test_writer.py
+-rw-r--r--   0        0        0     2402 1970-01-01 00:00:00.000000 depwatch-0.1.2/PKG-INFO
```

### Comparing `depwatch-0.1.1/LICENSE` & `depwatch-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/README.md` & `depwatch-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/depwatch/command.py` & `depwatch-0.1.2/depwatch/command.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from dotenv import load_dotenv
 
 from depwatch.history import create_histories
 from depwatch.repository import get_main_branch, get_repository_history
 from depwatch.deployment import get_deployment_history
-from depwatch.presentation import write_histories
+from depwatch.writer import write_histories
 
 
 def generate_histories(name: str, code_only: bool, limit: int):
     load_dotenv()
 
     base = get_main_branch(name)
```

### Comparing `depwatch-0.1.1/depwatch/deployment.py` & `depwatch-0.1.2/depwatch/deployment.py`

 * *Files 13% similar despite different names*

```diff
@@ -5,37 +5,38 @@
 from requests.models import Response
 from typing import cast
 
 from depwatch.history import DeploymentHistory
 
 
 def get_deployment_history(name: str, base: str, limit: int) -> list[DeploymentHistory]:
+    def __get_pipeline_workflow(p):
+        try:
+            return ci.get_pipeline_workflow(p.get("id"))
+        except HTTPError as e:
+            if cast(Response, e.response).status_code == 404:
+                return []
+            else:
+                raise e
+
     histories = []
 
     ci = Api(
         token=os.environ.get("CIRCLECI_ACCESS_TOKEN"), url="https://circleci.com/api"
     )
     user_name, project = name.split("/")
     pipelines = ci.get_project_pipelines(
         user_name, project, branch=base, paginate=True, limit=limit
     )
 
     for p in pipelines:
         if len(p.get("errors")) != 0:
             continue
 
-        try:
-            workflows = ci.get_pipeline_workflow(p.get("id"))
-        except HTTPError as e:
-            if cast(Response, e.response).status_code == 404:
-                continue
-            else:
-                raise e
-
-        workflows = ci.get_pipeline_workflow(p.get("id"))
+        workflows = __get_pipeline_workflow(p)
 
         stopped_at_list = [w.get("stopped_at") for w in workflows]
         latest_stopped_at = None
         for s in stopped_at_list:
             if s is None:
                 continue
```

### Comparing `depwatch-0.1.1/depwatch/history.py` & `depwatch-0.1.2/depwatch/history.py`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/depwatch/main.py` & `depwatch-0.1.2/depwatch/main.py`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/depwatch/presentation.py` & `depwatch-0.1.2/depwatch/writer.py`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/depwatch/repository.py` & `depwatch-0.1.2/depwatch/repository.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 from github import Github
 import os
 from datetime import datetime, timezone
 from depwatch.exception import DepwatchException
-
 from depwatch.history import RepositoryHistory
 
 
 def get_main_branch(name: str) -> str:
     gh = Github(os.environ.get("GITHUB_ACCESS_TOKEN"))
 
     repo = gh.get_repo(name)
```

### Comparing `depwatch-0.1.1/pyproject.toml` & `depwatch-0.1.2/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "depwatch"
-version = "0.1.1"
+version = "0.1.2"
 description = "A Simple command-line tool for collecting the times of various events in a project's lifecycle"
 authors = [
     { name = "hamakou108", email = "hamakou108@gmail.com" },
 ]
 dependencies = [
     "typer[all]>=0.7.0",
     "PyGithub>=1.58.0",
```

### Comparing `depwatch-0.1.1/tests/test_command.py` & `depwatch-0.1.2/tests/test_command.py`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/tests/test_history.py` & `depwatch-0.1.2/tests/test_history.py`

 * *Files identical despite different names*

### Comparing `depwatch-0.1.1/PKG-INFO` & `depwatch-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: depwatch
-Version: 0.1.1
+Version: 0.1.2
 Summary: A Simple command-line tool for collecting the times of various events in a project's lifecycle
 License: MIT
 Author-email: hamakou108 <hamakou108@gmail.com>
 Requires-Python: >=3.11
 Classifier: Programming Language :: Python :: 3
 Description-Content-Type: text/markdown
```

