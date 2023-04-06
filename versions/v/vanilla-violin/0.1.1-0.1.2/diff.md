# Comparing `tmp/vanilla_violin-0.1.1.tar.gz` & `tmp/vanilla_violin-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vanilla_violin-0.1.1.tar", last modified: Tue Mar 21 11:02:20 2023, max compression
+gzip compressed data, was "vanilla_violin-0.1.2.tar", last modified: Thu Apr  6 10:42:07 2023, max compression
```

## Comparing `vanilla_violin-0.1.1.tar` & `vanilla_violin-0.1.2.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 11:02:20.900918 vanilla_violin-0.1.1/
--rw-rw-rw-   0 root         (0) root         (0)     1068 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/LICENSE
--rw-r--r--   0 root         (0) root         (0)      380 2023-03-21 11:02:20.899918 vanilla_violin-0.1.1/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      448 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-21 11:02:20.900918 vanilla_violin-0.1.1/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      409 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 11:02:20.895918 vanilla_violin-0.1.1/tests/
--rw-rw-rw-   0 root         (0) root         (0)      583 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/tests/test_gitlab.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 11:02:20.895918 vanilla_violin-0.1.1/vanilla_violin/
--rw-rw-rw-   0 root         (0) root         (0)       40 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/vanilla_violin/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 11:02:20.898918 vanilla_violin-0.1.1/vanilla_violin/aws/
--rw-rw-rw-   0 root         (0) root         (0)       18 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/vanilla_violin/aws/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     4734 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/vanilla_violin/aws/aws.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 11:02:20.899918 vanilla_violin-0.1.1/vanilla_violin/gitlab/
--rw-rw-rw-   0 root         (0) root         (0)       21 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/vanilla_violin/gitlab/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     8982 2023-03-21 11:01:53.000000 vanilla_violin-0.1.1/vanilla_violin/gitlab/gitlab.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 11:02:20.897918 vanilla_violin-0.1.1/vanilla_violin.egg-info/
--rw-r--r--   0 root         (0) root         (0)      380 2023-03-21 11:02:20.000000 vanilla_violin-0.1.1/vanilla_violin.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      432 2023-03-21 11:02:20.000000 vanilla_violin-0.1.1/vanilla_violin.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-21 11:02:20.000000 vanilla_violin-0.1.1/vanilla_violin.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       40 2023-03-21 11:02:20.000000 vanilla_violin-0.1.1/vanilla_violin.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)       82 2023-03-21 11:02:20.000000 vanilla_violin-0.1.1/vanilla_violin.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       15 2023-03-21 11:02:20.000000 vanilla_violin-0.1.1/vanilla_violin.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.508327 vanilla_violin-0.1.2/
+-rw-rw-rw-   0 root         (0) root         (0)     1068 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/LICENSE
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 10:42:07.508327 vanilla_violin-0.1.2/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)      448 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 10:42:07.508327 vanilla_violin-0.1.2/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      405 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.503327 vanilla_violin-0.1.2/tests/
+-rw-rw-rw-   0 root         (0) root         (0)      583 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/tests/test_gitlab.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.503327 vanilla_violin-0.1.2/vanilla_violin/
+-rw-rw-rw-   0 root         (0) root         (0)       40 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.507327 vanilla_violin-0.1.2/vanilla_violin/aws/
+-rw-rw-rw-   0 root         (0) root         (0)       18 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/aws/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4734 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/aws/aws.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.507327 vanilla_violin-0.1.2/vanilla_violin/gitlab/
+-rw-rw-rw-   0 root         (0) root         (0)       21 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/gitlab/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     9423 2023-04-06 10:41:42.000000 vanilla_violin-0.1.2/vanilla_violin/gitlab/gitlab.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:42:07.506327 vanilla_violin-0.1.2/vanilla_violin.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      380 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      432 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       40 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)       82 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       15 2023-04-06 10:42:07.000000 vanilla_violin-0.1.2/vanilla_violin.egg-info/top_level.txt
```

### Comparing `vanilla_violin-0.1.1/LICENSE` & `vanilla_violin-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `vanilla_violin-0.1.1/tests/test_gitlab.py` & `vanilla_violin-0.1.2/tests/test_gitlab.py`

 * *Files identical despite different names*

### Comparing `vanilla_violin-0.1.1/vanilla_violin/aws/aws.py` & `vanilla_violin-0.1.2/vanilla_violin/aws/aws.py`

 * *Files identical despite different names*

### Comparing `vanilla_violin-0.1.1/vanilla_violin/gitlab/gitlab.py` & `vanilla_violin-0.1.2/vanilla_violin/gitlab/gitlab.py`

 * *Files 1% similar despite different names*

```diff
@@ -155,14 +155,25 @@
       headers=self.request_headers
     )
     return {
       'text': json.loads(response.text),
       'status_code': response.status_code
     }
 
+  def trigger_pipeline(self, project_id, ref='main'):
+
+    response = requests.post(
+      f'{self.base_url}{self.api_url}projects/{project_id}/pipeline?ref={ref}',
+      headers=self.request_headers,
+    )
+    return {
+      'text': json.loads(response.text),
+      'status_code': response.status_code
+    }
+
   def create_pages_domain_if_available(self, project_id, domain, auto_ssl_enabled = True):
 
     print('--- BUILDING PAGES ---')
     pages_create = self.create_pages_domain(project_id, domain, auto_ssl_enabled)
 
     if pages_create['status_code'] == 404:
       print(f"--- {pages_create['text']['message']}")
@@ -218,15 +229,20 @@
     return []
 
   def build_request_chain(self, full_path):
 
     print(f'--- BUILDING FOR {full_path} ---')
 
     paths = full_path.split('/')
-    parent_id = self.find_base_group_by_path(paths[0], self.get_groups())['id']
+    try:
+      parent_id = self.find_base_group_by_path(paths[0], self.get_groups())['id']
+
+    except Exception as ex:
+      print(ex)
+      raise Exception('Check path, check if user has permissions to repo')
 
     for path in paths[1:-1]:
       parent_id = self.build_group(path, parent_id)['id']
 
     projs = paths[-1].split('+')
     projs_ids = []
     for path in projs:
```

