# Comparing `tmp/abstra-cli-0.8.0.tar.gz` & `tmp/abstra-cli-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/abstra-cli-0.8.0.tar", last modified: Sun Feb 26 01:57:37 2023, max compression
+gzip compressed data, was "dist/abstra-cli-0.9.0.tar", last modified: Sun Feb 26 02:18:54 2023, max compression
```

## Comparing `abstra-cli-0.8.0.tar` & `abstra-cli-0.9.0.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/
--rw-r--r--   0 runner    (1001) docker     (123)    12716 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8801 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli/
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli/apis/
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3216 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/dashes.py
--rw-r--r--   0 runner    (1001) docker     (123)      727 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/files.py
--rw-r--r--   0 runner    (1001) docker     (123)     3222 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/forms.py
--rw-r--r--   0 runner    (1001) docker     (123)     3184 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/hooks.py
--rw-r--r--   0 runner    (1001) docker     (123)     3363 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2539 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/main.py
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/packages.py
--rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/public.py
--rw-r--r--   0 runner    (1001) docker     (123)     1636 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/apis/vars.py
--rw-r--r--   0 runner    (1001) docker     (123)     3717 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      562 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/credentials.py
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/deploy.py
--rw-r--r--   0 runner    (1001) docker     (123)     5205 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/messages.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli/resources/
--rw-r--r--   0 runner    (1001) docker     (123)      211 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7616 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/dashes.py
--rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/files.py
--rw-r--r--   0 runner    (1001) docker     (123)     6503 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/forms.py
--rw-r--r--   0 runner    (1001) docker     (123)     5295 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/hooks.py
--rw-r--r--   0 runner    (1001) docker     (123)     5143 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/jobs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/packages.py
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/resources.py
--rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/resources/vars.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli/utils/
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/utils/file.py
--rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/abstra_cli/utils/main.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12716 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      973 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       73 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/abstra_cli.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-26 01:57:37.000000 abstra-cli-0.8.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1085 2023-02-26 01:57:26.000000 abstra-cli-0.8.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    12716 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8801 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli/
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli/apis/
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/dashes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      727 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/files.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3222 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/forms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3184 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3363 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2539 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/packages.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1202 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/public.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1636 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/apis/vars.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3717 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      562 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/credentials.py
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2010 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/deploy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5205 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/messages.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7616 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/dashes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/files.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6503 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/forms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5295 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5143 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/jobs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1524 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/packages.py
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/resources.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/resources/vars.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1440 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/utils/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/abstra_cli/utils/main.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    12716 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      973 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       73 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/abstra_cli.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-02-26 02:18:54.000000 abstra-cli-0.9.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1085 2023-02-26 02:18:41.000000 abstra-cli-0.9.0/setup.py
```

### Comparing `abstra-cli-0.8.0/PKG-INFO` & `abstra-cli-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: abstra-cli
-Version: 0.8.0
+Version: 0.9.0
 Summary: Abstra CLI
 Home-page: https://github.com/abstra-app/abstra-cli
 License: MIT
 Description: [![pypi](https://img.shields.io/pypi/v/abstra-cli.svg)](https://pypi.python.org/pypi/abstra-cli) [![PyPI Downloads](https://img.shields.io/pypi/dm/abstra-cli.svg)](https://pypi.org/project/abstra-cli/) [![Code check](https://github.com/abstra-app/abstra-cli/actions/workflows/code_check.yml/badge.svg)](https://github.com/abstra-app/abstra-cli/actions/workflows/code_check.yml)
         
         # Abstra CLI
```

### Comparing `abstra-cli-0.8.0/README.md` & `abstra-cli-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/dashes.py` & `abstra-cli-0.9.0/abstra_cli/apis/dashes.py`

 * *Files 8% similar despite different names*

```diff
@@ -18,15 +18,17 @@
 
 
 def add_workspace_dash(data):
     _, workspace_id, _ = api_main.get_auth_info()
     dash_data = {
         "title": data["name"],
         "workspace_id": workspace_id,
+        "path": data["path"],
         "draft_layout": None,
+        "layout": data["layout"],
         "theme": data.get("theme", None),
         "script": {
             "data": {
                 "workspace_id": workspace_id,
                 "enabled": data.get("enabled", True),
                 "file_path": data["code_file_path"],
                 "name": data["name"],
@@ -53,14 +55,15 @@
         .get("returning", {})[0]
     )
 
 
 def update_workspace_dash(path, data):
     dash_data = {
         "title": data["name"],
+        "layout": data["layout"],
         "draft_layout": None,
         "theme": data.get("theme", None),
     }
     script_data = {
         "enabled": data.get("enabled", True),
         "file_path": data["code_file_path"],
         "code": None,
```

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/files.py` & `abstra-cli-0.9.0/abstra_cli/apis/files.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/forms.py` & `abstra-cli-0.9.0/abstra_cli/apis/forms.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/hooks.py` & `abstra-cli-0.9.0/abstra_cli/apis/hooks.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/jobs.py` & `abstra-cli-0.9.0/abstra_cli/apis/jobs.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/main.py` & `abstra-cli-0.9.0/abstra_cli/apis/main.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/packages.py` & `abstra-cli-0.9.0/abstra_cli/apis/packages.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/public.py` & `abstra-cli-0.9.0/abstra_cli/apis/public.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/apis/vars.py` & `abstra-cli-0.9.0/abstra_cli/apis/vars.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/cli.py` & `abstra-cli-0.9.0/abstra_cli/cli.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/credentials.py` & `abstra-cli-0.9.0/abstra_cli/credentials.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/decorators.py` & `abstra-cli-0.9.0/abstra_cli/decorators.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/deploy.py` & `abstra-cli-0.9.0/abstra_cli/deploy.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/messages.py` & `abstra-cli-0.9.0/abstra_cli/messages.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/dashes.py` & `abstra-cli-0.9.0/abstra_cli/resources/dashes.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/files.py` & `abstra-cli-0.9.0/abstra_cli/resources/files.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/forms.py` & `abstra-cli-0.9.0/abstra_cli/resources/forms.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/hooks.py` & `abstra-cli-0.9.0/abstra_cli/resources/hooks.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/jobs.py` & `abstra-cli-0.9.0/abstra_cli/resources/jobs.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/packages.py` & `abstra-cli-0.9.0/abstra_cli/resources/packages.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/resources/vars.py` & `abstra-cli-0.9.0/abstra_cli/resources/vars.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/utils/file.py` & `abstra-cli-0.9.0/abstra_cli/utils/file.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli/utils/main.py` & `abstra-cli-0.9.0/abstra_cli/utils/main.py`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/abstra_cli.egg-info/PKG-INFO` & `abstra-cli-0.9.0/abstra_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: abstra-cli
-Version: 0.8.0
+Version: 0.9.0
 Summary: Abstra CLI
 Home-page: https://github.com/abstra-app/abstra-cli
 License: MIT
 Description: [![pypi](https://img.shields.io/pypi/v/abstra-cli.svg)](https://pypi.python.org/pypi/abstra-cli) [![PyPI Downloads](https://img.shields.io/pypi/dm/abstra-cli.svg)](https://pypi.org/project/abstra-cli/) [![Code check](https://github.com/abstra-app/abstra-cli/actions/workflows/code_check.yml/badge.svg)](https://github.com/abstra-app/abstra-cli/actions/workflows/code_check.yml)
         
         # Abstra CLI
```

### Comparing `abstra-cli-0.8.0/abstra_cli.egg-info/SOURCES.txt` & `abstra-cli-0.9.0/abstra_cli.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `abstra-cli-0.8.0/setup.py` & `abstra-cli-0.9.0/setup.py`

 * *Files identical despite different names*

