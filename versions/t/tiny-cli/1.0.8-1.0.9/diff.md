# Comparing `tmp/tiny-cli-1.0.8.tar.gz` & `tmp/tiny-cli-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tiny-cli-1.0.8.tar", last modified: Mon Mar 20 18:29:26 2023, max compression
+gzip compressed data, was "tiny-cli-1.0.9.tar", last modified: Mon Mar 20 18:38:38 2023, max compression
```

## Comparing `tiny-cli-1.0.8.tar` & `tiny-cli-1.0.9.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-03-20 18:29:26.653898 tiny-cli-1.0.8/
--rw-r--r--   0 vishal     (501) staff       (20)     6722 2023-03-20 18:29:26.653769 tiny-cli-1.0.8/PKG-INFO
--rw-r--r--   0 vishal     (501) staff       (20)     6443 2023-03-19 15:27:20.000000 tiny-cli-1.0.8/README.md
--rw-r--r--   0 vishal     (501) staff       (20)       38 2023-03-20 18:29:26.653930 tiny-cli-1.0.8/setup.cfg
--rw-r--r--   0 vishal     (501) staff       (20)      613 2023-03-19 15:27:20.000000 tiny-cli-1.0.8/setup.py
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-03-20 18:29:26.652646 tiny-cli-1.0.8/tiny/
--rw-r--r--   0 vishal     (501) staff       (20)       39 2023-03-17 20:02:24.000000 tiny-cli-1.0.8/tiny/__init__.py
--rw-r--r--   0 vishal     (501) staff       (20)     5270 2023-03-19 15:27:20.000000 tiny-cli-1.0.8/tiny/main.py
--rw-r--r--   0 vishal     (501) staff       (20)      125 2023-03-20 18:28:36.000000 tiny-cli-1.0.8/tiny/settings.py
--rw-r--r--   0 vishal     (501) staff       (20)     4628 2023-03-19 15:44:34.000000 tiny-cli-1.0.8/tiny/storage.py
--rw-r--r--   0 vishal     (501) staff       (20)     2132 2023-03-19 15:27:20.000000 tiny-cli-1.0.8/tiny/workflow.py
-drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-03-20 18:29:26.653587 tiny-cli-1.0.8/tiny_cli.egg-info/
--rw-r--r--   0 vishal     (501) staff       (20)     6722 2023-03-20 18:29:26.000000 tiny-cli-1.0.8/tiny_cli.egg-info/PKG-INFO
--rw-r--r--   0 vishal     (501) staff       (20)      288 2023-03-20 18:29:26.000000 tiny-cli-1.0.8/tiny_cli.egg-info/SOURCES.txt
--rw-r--r--   0 vishal     (501) staff       (20)        1 2023-03-20 18:29:26.000000 tiny-cli-1.0.8/tiny_cli.egg-info/dependency_links.txt
--rw-r--r--   0 vishal     (501) staff       (20)        1 2022-11-30 23:14:47.000000 tiny-cli-1.0.8/tiny_cli.egg-info/not-zip-safe
--rw-r--r--   0 vishal     (501) staff       (20)       39 2023-03-20 18:29:26.000000 tiny-cli-1.0.8/tiny_cli.egg-info/requires.txt
--rw-r--r--   0 vishal     (501) staff       (20)        5 2023-03-20 18:29:26.000000 tiny-cli-1.0.8/tiny_cli.egg-info/top_level.txt
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-03-20 18:38:38.237666 tiny-cli-1.0.9/
+-rw-r--r--   0 vishal     (501) staff       (20)     6722 2023-03-20 18:38:38.237544 tiny-cli-1.0.9/PKG-INFO
+-rw-r--r--   0 vishal     (501) staff       (20)     6443 2023-03-19 15:27:20.000000 tiny-cli-1.0.9/README.md
+-rw-r--r--   0 vishal     (501) staff       (20)       38 2023-03-20 18:38:38.237700 tiny-cli-1.0.9/setup.cfg
+-rw-r--r--   0 vishal     (501) staff       (20)      628 2023-03-20 18:38:28.000000 tiny-cli-1.0.9/setup.py
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-03-20 18:38:38.236459 tiny-cli-1.0.9/tiny/
+-rw-r--r--   0 vishal     (501) staff       (20)       39 2023-03-17 20:02:24.000000 tiny-cli-1.0.9/tiny/__init__.py
+-rw-r--r--   0 vishal     (501) staff       (20)     6128 2023-03-20 18:38:28.000000 tiny-cli-1.0.9/tiny/main.py
+-rw-r--r--   0 vishal     (501) staff       (20)      125 2023-03-20 18:37:32.000000 tiny-cli-1.0.9/tiny/settings.py
+-rw-r--r--   0 vishal     (501) staff       (20)     4628 2023-03-19 15:44:34.000000 tiny-cli-1.0.9/tiny/storage.py
+-rw-r--r--   0 vishal     (501) staff       (20)     2132 2023-03-19 15:27:20.000000 tiny-cli-1.0.9/tiny/workflow.py
+drwxr-xr-x   0 vishal     (501) staff       (20)        0 2023-03-20 18:38:38.237376 tiny-cli-1.0.9/tiny_cli.egg-info/
+-rw-r--r--   0 vishal     (501) staff       (20)     6722 2023-03-20 18:38:38.000000 tiny-cli-1.0.9/tiny_cli.egg-info/PKG-INFO
+-rw-r--r--   0 vishal     (501) staff       (20)      288 2023-03-20 18:38:38.000000 tiny-cli-1.0.9/tiny_cli.egg-info/SOURCES.txt
+-rw-r--r--   0 vishal     (501) staff       (20)        1 2023-03-20 18:38:38.000000 tiny-cli-1.0.9/tiny_cli.egg-info/dependency_links.txt
+-rw-r--r--   0 vishal     (501) staff       (20)        1 2022-11-30 23:14:47.000000 tiny-cli-1.0.9/tiny_cli.egg-info/not-zip-safe
+-rw-r--r--   0 vishal     (501) staff       (20)       47 2023-03-20 18:38:38.000000 tiny-cli-1.0.9/tiny_cli.egg-info/requires.txt
+-rw-r--r--   0 vishal     (501) staff       (20)        5 2023-03-20 18:38:38.000000 tiny-cli-1.0.9/tiny_cli.egg-info/top_level.txt
```

### Comparing `tiny-cli-1.0.8/PKG-INFO` & `tiny-cli-1.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tiny-cli
-Version: 1.0.8
+Version: 1.0.9
 Summary: TinyBio genome analysis tool
 Home-page: https://github.com/tinybio-cloud/tiny
 Author: TinyBio LLC
 Author-email: tiny-packages@tinybio.cloud
 License: MIT
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `tiny-cli-1.0.8/README.md` & `tiny-cli-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `tiny-cli-1.0.8/setup.py` & `tiny-cli-1.0.9/setup.py`

 * *Files 19% similar despite different names*

```diff
@@ -6,19 +6,20 @@
         return f.read()
 
 
 dependencies = [
     "httpcore[http2]",
     "httpx==0.23.1",
     "tabulate",
+    "anytree",
 ]
 
 setup(
     name='tiny-cli',
-    version='1.0.8',
+    version='1.0.9',
     description='TinyBio genome analysis tool',
     long_description_content_type='text/markdown',
     url='https://github.com/tinybio-cloud/tiny',
     long_description=readme(),
     author='TinyBio LLC',
     author_email='tiny-packages@tinybio.cloud',
     license='MIT',
```

### Comparing `tiny-cli-1.0.8/tiny/main.py` & `tiny-cli-1.0.9/tiny/main.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 from datetime import datetime
 from typing import List, Tuple
 
 import httpx
 from tabulate import tabulate
+from anytree import Node, RenderTree
 
 from .storage import upload_files, download_file, list_files_in_bucket, upload_file_path
 from .workflow import execute_workflow, get_job, get_job_logs, JobStatus
 from .settings import PROD_BASE_URL
 
 
 def print_table(headers, table_data):
@@ -93,15 +94,38 @@
 
     def file_exists_in_bucket(self, file):
         input_file_path = f'input/{file}'
         return input_file_path in list_files_in_bucket(self.bucket_name,
                                                        auth_token=self.auth.get_access_token()), input_file_path
 
     def list_files(self):
-        return list_files_in_bucket(self.bucket_name, auth_token=self.auth.get_access_token())
+        files = list_files_in_bucket(self.bucket_name, auth_token=self.auth.get_access_token())
+        root = Node(self.bucket_name)
+        for file in files:
+            file_name = file.get('name')
+            file_size = file.get('size')
+
+            path = file_name.split("/")
+            node = root
+            for i in range(len(path)):
+                name = path[i]
+                if name not in [child.name for child in node.children]:
+                    node = Node(name, parent=node)
+                else:
+                    node = [child for child in node.children if child.name == name][0]
+            if file.get('size') is not None:
+                Node(f"{file_name} ({file_size})", parent=node)
+            else:
+                Node(file_name, parent=node)
+
+        output = ""
+        for pre, _, node in RenderTree(root):
+            output += f"{pre}{node.name}\n"
+
+        print(output)
 
     def upload_job(self, files: List[Tuple[str, str]], method: str = 'curl'):
         upload_jobs = upload_file_path(self.bucket_name, files=files, method=method,
                                        auth_token=self.auth.get_access_token())
         table = []
         for job in upload_jobs:
             job = Job(job_id=job.get('id'), tool=method, full_command=f'{method} {job.get("input")}', workbench=self)
```

### Comparing `tiny-cli-1.0.8/tiny/storage.py` & `tiny-cli-1.0.9/tiny/storage.py`

 * *Files identical despite different names*

### Comparing `tiny-cli-1.0.8/tiny/workflow.py` & `tiny-cli-1.0.9/tiny/workflow.py`

 * *Files identical despite different names*

### Comparing `tiny-cli-1.0.8/tiny_cli.egg-info/PKG-INFO` & `tiny-cli-1.0.9/tiny_cli.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tiny-cli
-Version: 1.0.8
+Version: 1.0.9
 Summary: TinyBio genome analysis tool
 Home-page: https://github.com/tinybio-cloud/tiny
 Author: TinyBio LLC
 Author-email: tiny-packages@tinybio.cloud
 License: MIT
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

