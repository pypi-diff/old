# Comparing `tmp/vanilla_violin-0.1.2.tar.gz` & `tmp/vanilla_violin-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vanilla_violin-0.1.2.tar", last modified: Thu Apr  6 10:42:07 2023, max compression
+gzip compressed data, was "vanilla_violin-0.1.3.tar", last modified: Thu Apr  6 11:03:01 2023, max compression
```

## Comparing `vanilla_violin-0.1.2.tar` & `vanilla_violin-0.1.3.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.508327 vanilla_violin-0.1.2/
--rw-rw-rw-   0 root         (0) root         (0)     1068 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/LICENSE
--rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 10:42:07.508327 vanilla_violin-0.1.2/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      448 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 10:42:07.508327 vanilla_violin-0.1.2/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      405 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.503327 vanilla_violin-0.1.2/tests/
--rw-rw-rw-   0 root         (0) root         (0)      583 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/tests/test_gitlab.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.503327 vanilla_violin-0.1.2/vanilla_violin/
--rw-rw-rw-   0 root         (0) root         (0)       40 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.507327 vanilla_violin-0.1.2/vanilla_violin/aws/
--rw-rw-rw-   0 root         (0) root         (0)       18 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/aws/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4734 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/aws/aws.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.507327 vanilla_violin-0.1.2/vanilla_violin/gitlab/
--rw-rw-rw-   0 root         (0) root         (0)       21 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/gitlab/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     9423 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/gitlab/gitlab.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.506327 vanilla_violin-0.1.2/vanilla_violin.egg-info/
--rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      432 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       40 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)       82 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       15 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:03:01.533763 vanilla_violin-0.1.3/
+-rw-rw-rw-   0 root         (0) root         (0)     1068 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/LICENSE
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 11:03:01.533763 vanilla_violin-0.1.3/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)      448 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 11:03:01.533763 vanilla_violin-0.1.3/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      409 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:03:01.528763 vanilla_violin-0.1.3/tests/
+-rw-rw-rw-   0 root         (0) root         (0)      583 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/tests/test_gitlab.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:03:01.528763 vanilla_violin-0.1.3/vanilla_violin/
+-rw-rw-rw-   0 root         (0) root         (0)       40 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/vanilla_violin/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:03:01.532763 vanilla_violin-0.1.3/vanilla_violin/aws/
+-rw-rw-rw-   0 root         (0) root         (0)       18 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/vanilla_violin/aws/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4734 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/vanilla_violin/aws/aws.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:03:01.532763 vanilla_violin-0.1.3/vanilla_violin/gitlab/
+-rw-rw-rw-   0 root         (0) root         (0)       21 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/vanilla_violin/gitlab/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     9796 2023-04-06 11:02:35.000000 vanilla_violin-0.1.3/vanilla_violin/gitlab/gitlab.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 11:03:01.531763 vanilla_violin-0.1.3/vanilla_violin.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 11:03:01.000000 vanilla_violin-0.1.3/vanilla_violin.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      432 2023-04-06 11:03:01.000000 vanilla_violin-0.1.3/vanilla_violin.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 11:03:01.000000 vanilla_violin-0.1.3/vanilla_violin.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       40 2023-04-06 11:03:01.000000 vanilla_violin-0.1.3/vanilla_violin.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)       82 2023-04-06 11:03:01.000000 vanilla_violin-0.1.3/vanilla_violin.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       15 2023-04-06 11:03:01.000000 vanilla_violin-0.1.3/vanilla_violin.egg-info/top_level.txt
```

### Comparing `vanilla_violin-0.1.2/LICENSE` & `vanilla_violin-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `vanilla_violin-0.1.2/tests/test_gitlab.py` & `vanilla_violin-0.1.3/tests/test_gitlab.py`

 * *Files identical despite different names*

### Comparing `vanilla_violin-0.1.2/vanilla_violin/aws/aws.py` & `vanilla_violin-0.1.3/vanilla_violin/aws/aws.py`

 * *Files identical despite different names*

### Comparing `vanilla_violin-0.1.2/vanilla_violin/gitlab/gitlab.py` & `vanilla_violin-0.1.3/vanilla_violin/gitlab/gitlab.py`

 * *Files 2% similar despite different names*

```diff
@@ -224,14 +224,28 @@
   def find_base_group_by_path(self, path, array_of_objs):
     for obj in array_of_objs:
       if obj['path'] == path and obj['full_path'] == path :
         return obj
 
     return []
 
+  def get_project_id(self, full_path):
+    paths = full_path.split('/')
+    parent_id = None
+
+    try:
+      for path in paths[:-1]:
+        parent_id = self.find_base_group_by_path(path, self.get_groups(parent_id))['id']
+
+      proj = self.find_object_by_path(path, self.list_group_projects(parent_id))
+      return proj['id']
+
+    except Exception as ex:
+      raise ex
+
   def build_request_chain(self, full_path):
 
     print(f'--- BUILDING FOR {full_path} ---')
 
     paths = full_path.split('/')
     try:
       parent_id = self.find_base_group_by_path(paths[0], self.get_groups())['id']
```

