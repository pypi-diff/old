# Comparing `tmp/nvosscript-1.1.2.tar.gz` & `tmp/nvosscript-1.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nvosscript-1.1.2.tar", last modified: Thu Apr  6 10:32:55 2023, max compression
+gzip compressed data, was "nvosscript-1.1.3.tar", last modified: Thu Apr  6 11:34:07 2023, max compression
```

## Comparing `nvosscript-1.1.2.tar` & `nvosscript-1.1.3.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 10:32:55.389426 nvosscript-1.1.2/
--rw-r--r--   0 andre.zhao   (503) staff       (20)     1073 2023-03-22 09:01:10.000000 nvosscript-1.1.2/LICENSE
--rw-r--r--   0 andre.zhao   (503) staff       (20)      333 2023-04-06 10:32:55.389273 nvosscript-1.1.2/PKG-INFO
--rw-r--r--   0 andre.zhao   (503) staff       (20)       78 2023-03-22 09:07:29.000000 nvosscript-1.1.2/README.md
-drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 10:32:55.387200 nvosscript-1.1.2/nvos/
--rw-r--r--   0 andre.zhao   (503) staff       (20)        0 2023-03-21 08:49:46.000000 nvosscript-1.1.2/nvos/__init__.py
--rw-r--r--   0 andre.zhao   (503) staff       (20)    12412 2023-04-03 03:55:32.000000 nvosscript-1.1.2/nvos/file.py
--rw-r--r--   0 andre.zhao   (503) staff       (20)     1662 2023-04-06 06:54:07.000000 nvosscript-1.1.2/nvos/login.py
--rw-r--r--   0 andre.zhao   (503) staff       (20)     6051 2023-04-06 10:28:38.000000 nvosscript-1.1.2/nvos/remote.py
--rw-r--r--   0 andre.zhao   (503) staff       (20)     3885 2023-04-06 08:59:52.000000 nvosscript-1.1.2/nvos/run.py
--rw-r--r--   0 andre.zhao   (503) staff       (20)      812 2023-03-30 03:32:22.000000 nvosscript-1.1.2/nvos/utils.py
-drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 10:32:55.388456 nvosscript-1.1.2/nvosscript.egg-info/
--rw-r--r--   0 andre.zhao   (503) staff       (20)      333 2023-04-06 10:32:55.000000 nvosscript-1.1.2/nvosscript.egg-info/PKG-INFO
--rw-r--r--   0 andre.zhao   (503) staff       (20)      372 2023-04-06 10:32:55.000000 nvosscript-1.1.2/nvosscript.egg-info/SOURCES.txt
--rw-r--r--   0 andre.zhao   (503) staff       (20)        1 2023-04-06 10:32:55.000000 nvosscript-1.1.2/nvosscript.egg-info/dependency_links.txt
--rw-r--r--   0 andre.zhao   (503) staff       (20)       41 2023-04-06 10:32:55.000000 nvosscript-1.1.2/nvosscript.egg-info/entry_points.txt
--rw-r--r--   0 andre.zhao   (503) staff       (20)       47 2023-04-06 10:32:55.000000 nvosscript-1.1.2/nvosscript.egg-info/requires.txt
--rw-r--r--   0 andre.zhao   (503) staff       (20)       21 2023-04-06 10:32:55.000000 nvosscript-1.1.2/nvosscript.egg-info/top_level.txt
--rw-r--r--   0 andre.zhao   (503) staff       (20)       38 2023-04-06 10:32:55.389473 nvosscript-1.1.2/setup.cfg
--rw-r--r--   0 andre.zhao   (503) staff       (20)      805 2023-04-06 10:32:43.000000 nvosscript-1.1.2/setup.py
-drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 10:32:55.388777 nvosscript-1.1.2/start/
--rw-r--r--   0 andre.zhao   (503) staff       (20)        0 2023-04-04 03:24:28.000000 nvosscript-1.1.2/start/__init__.py
--rw-r--r--   0 andre.zhao   (503) staff       (20)     3504 2023-04-06 10:32:49.000000 nvosscript-1.1.2/start/main.py
-drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 10:32:55.388929 nvosscript-1.1.2/win/
--rw-r--r--   0 andre.zhao   (503) staff       (20)     1283 2023-04-06 07:02:53.000000 nvosscript-1.1.2/win/win_auto_script.py
+drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 11:34:07.523738 nvosscript-1.1.3/
+-rw-r--r--   0 andre.zhao   (503) staff       (20)     1073 2023-03-22 09:01:10.000000 nvosscript-1.1.3/LICENSE
+-rw-r--r--   0 andre.zhao   (503) staff       (20)      333 2023-04-06 11:34:07.523524 nvosscript-1.1.3/PKG-INFO
+-rw-r--r--   0 andre.zhao   (503) staff       (20)       78 2023-03-22 09:07:29.000000 nvosscript-1.1.3/README.md
+drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 11:34:07.521432 nvosscript-1.1.3/nvos/
+-rw-r--r--   0 andre.zhao   (503) staff       (20)        0 2023-03-21 08:49:46.000000 nvosscript-1.1.3/nvos/__init__.py
+-rw-r--r--   0 andre.zhao   (503) staff       (20)    12412 2023-04-03 03:55:32.000000 nvosscript-1.1.3/nvos/file.py
+-rw-r--r--   0 andre.zhao   (503) staff       (20)     1662 2023-04-06 06:54:07.000000 nvosscript-1.1.3/nvos/login.py
+-rw-r--r--   0 andre.zhao   (503) staff       (20)     6338 2023-04-06 11:31:52.000000 nvosscript-1.1.3/nvos/remote.py
+-rw-r--r--   0 andre.zhao   (503) staff       (20)     3885 2023-04-06 08:59:52.000000 nvosscript-1.1.3/nvos/run.py
+-rw-r--r--   0 andre.zhao   (503) staff       (20)      812 2023-03-30 03:32:22.000000 nvosscript-1.1.3/nvos/utils.py
+drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 11:34:07.522725 nvosscript-1.1.3/nvosscript.egg-info/
+-rw-r--r--   0 andre.zhao   (503) staff       (20)      333 2023-04-06 11:34:07.000000 nvosscript-1.1.3/nvosscript.egg-info/PKG-INFO
+-rw-r--r--   0 andre.zhao   (503) staff       (20)      372 2023-04-06 11:34:07.000000 nvosscript-1.1.3/nvosscript.egg-info/SOURCES.txt
+-rw-r--r--   0 andre.zhao   (503) staff       (20)        1 2023-04-06 11:34:07.000000 nvosscript-1.1.3/nvosscript.egg-info/dependency_links.txt
+-rw-r--r--   0 andre.zhao   (503) staff       (20)       41 2023-04-06 11:34:07.000000 nvosscript-1.1.3/nvosscript.egg-info/entry_points.txt
+-rw-r--r--   0 andre.zhao   (503) staff       (20)       47 2023-04-06 11:34:07.000000 nvosscript-1.1.3/nvosscript.egg-info/requires.txt
+-rw-r--r--   0 andre.zhao   (503) staff       (20)       21 2023-04-06 11:34:07.000000 nvosscript-1.1.3/nvosscript.egg-info/top_level.txt
+-rw-r--r--   0 andre.zhao   (503) staff       (20)       38 2023-04-06 11:34:07.523799 nvosscript-1.1.3/setup.cfg
+-rw-r--r--   0 andre.zhao   (503) staff       (20)      805 2023-04-06 11:33:54.000000 nvosscript-1.1.3/setup.py
+drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 11:34:07.522970 nvosscript-1.1.3/start/
+-rw-r--r--   0 andre.zhao   (503) staff       (20)        0 2023-04-04 03:24:28.000000 nvosscript-1.1.3/start/__init__.py
+-rw-r--r--   0 andre.zhao   (503) staff       (20)     3504 2023-04-06 11:33:59.000000 nvosscript-1.1.3/start/main.py
+drwxr-xr-x   0 andre.zhao   (503) staff       (20)        0 2023-04-06 11:34:07.523104 nvosscript-1.1.3/win/
+-rw-r--r--   0 andre.zhao   (503) staff       (20)     1283 2023-04-06 07:02:53.000000 nvosscript-1.1.3/win/win_auto_script.py
```

### Comparing `nvosscript-1.1.2/LICENSE` & `nvosscript-1.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `nvosscript-1.1.2/nvos/file.py` & `nvosscript-1.1.3/nvos/file.py`

 * *Files identical despite different names*

### Comparing `nvosscript-1.1.2/nvos/login.py` & `nvosscript-1.1.3/nvos/login.py`

 * *Files identical despite different names*

### Comparing `nvosscript-1.1.2/nvos/remote.py` & `nvosscript-1.1.3/nvos/remote.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import time
 
 import boto3
 import os
 import requests
 import hashlib
 import json
+import re
 import concurrent.futures
 import multiprocessing
 from tqdm import tqdm
 from nvos import login
 import logging
 
 # 导入全局日志记录器
@@ -26,28 +27,30 @@
 
 def upload_file(file_path_list, project_space_list):
     s3_secret = get_s3_secret()
     bucket_name = s3_secret["bucket"]
     aws_ak = s3_secret["ak"]
     aws_sk = s3_secret["sk"]
     aws_region = s3_secret["regionId"]
-    logger.info(f"upload_file execute bucket {bucket_name} {aws_region} {aws_ak} {aws_sk}")
     s3 = boto3.resource('s3', region_name=aws_region, aws_access_key_id=aws_ak,
                         aws_secret_access_key=aws_sk)
     bucket = s3.Bucket(bucket_name)
     upload_list = []
+    filter_upload_re = filter_upload_dir()
     for project_space in project_space_list:
-        flag = False
-        for temp in filter_upload_dir():
-            if temp in project_space["project_space"]:
-                flag = True
-                break
-        if not flag:
-            continue
         for file_path in file_path_list:
+            flag = False
+            for temp in filter_upload_re:
+                matchObj = re.match(temp, file_path["file_path"], re.M | re.I)
+                if matchObj:
+                    flag = True
+                    break
+            if not flag:
+                continue
+
             if project_space["project_space"] in file_path["file_path"]:
                 file_name = "%s/%s/%s" % (login.get_user_id(), md5(project_space["git_branch"], project_space["project_space"]),
                                             file_path["file_path"][file_path["file_path"]
                                           .find(os.path.basename(project_space["project_space"])):])
                 file_name = file_name.replace("\\", "/")
                 local_file_path = file_path["file_path"]
                 temp_file = {"local_file_path": local_file_path, "file_name": file_name}
@@ -69,21 +72,25 @@
             progress.update(global_var - addition)
             addition = global_var
             if (global_var == len(upload_list) or global_var >= len(upload_list) - 20):
                 break
             if time_count == 60:
                 break
 
+
 def uploading_file(file, bucket):
     global global_var
-    local_file_path = file["local_file_path"]
-    file_name = file["file_name"]
-    logger.info(f"upload file ossUrl:{file_name} file local full path:{local_file_path}")
-    bucket.upload_file(local_file_path, file_name)
-    global_var += 1
+    try:
+        local_file_path = file["local_file_path"]
+        file_name = file["file_name"]
+        bucket.upload_file(local_file_path, file_name)
+        logger.info(f"upload file ossUrl:{file_name} file local full path:{local_file_path}")
+        global_var += 1
+    except Exception:
+        logger.exception("uploading_file error")
 
 
 
 def download_file(project_space):
     s3_secret = get_s3_secret()
     bucket_name = s3_secret["bucket"]
     aws_ak = s3_secret["ak"]
@@ -131,16 +138,17 @@
     string = "%s%s" % (git_branch, project_space)
     hash_object = hashlib.md5(string.encode())
     md5_hash = hash_object.hexdigest()
     return md5_hash
 
 
 def filter_upload_dir():
-
-    return ["ecus", "platform"]
+    get_current_env()
+    url = "%s%s" % (daemon_network, "/workspace/getFilePathRegular")
+    return post_data(url, {})
 
 def get_s3_secret():
     get_current_env()
     url = "%s%s" % (daemon_network, "/file/config")
     headers = {"content-type": "application/json"}
     logger.info(f'request url:{url}')
     response = requests.post(url, headers=headers, data=json.dumps({}))
@@ -157,11 +165,11 @@
     with open(os.path.expanduser(os.path.join('~','nvos_env')),'w') as f:
         f.writelines(val)
     print(f"this script current env:{env} and cloud linked:{val}")
 
 
 def get_current_env():
     global daemon_network
-    if os.path.exists(os.path.expanduser(os.path.join('~','nvos_env'))):
+    if os.path.exists(os.path.expanduser(os.path.join('~', 'nvos_env'))):
         with open(os.path.expanduser(os.path.join('~', 'nvos_env')), 'r')as f:
             daemon_network = f.readline()
-
+    logger.info(f"get_current_env this env:{daemon_network}")
```

### Comparing `nvosscript-1.1.2/nvos/run.py` & `nvosscript-1.1.3/nvos/run.py`

 * *Files identical despite different names*

### Comparing `nvosscript-1.1.2/nvos/utils.py` & `nvosscript-1.1.3/nvos/utils.py`

 * *Files identical despite different names*

### Comparing `nvosscript-1.1.2/setup.py` & `nvosscript-1.1.3/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_namespace_packages
 
 setup(
     name='nvosscript',
-    version='1.1.2',
+    version='1.1.3',
     description='nvos toolchain script',
     packages=find_namespace_packages(),
     author = 'andre.zhao',
     author_email = 'andre.zhao@nio.com',
     keywords='pack',
     readme = "README.md",
     install_requires=[
```

### Comparing `nvosscript-1.1.2/start/main.py` & `nvosscript-1.1.3/start/main.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,15 +45,15 @@
     elif args.subcommand == "async":
         run.command_async()
     elif args.subcommand == "pull":
         run.command_pull()
     elif args.subcommand == "push":
         run.command_push()
     elif args.subcommand == "version":
-        print("1.1.2")
+        print("1.1.3")
     elif args.subcommand == 'env':
         run.command_env(args.switch)
     elif args.subcommand == "path":
         current_file_path = os.path.abspath(__file__)
         current_file_dir = os.path.dirname(current_file_path)
         current_file_dir = os.path.dirname(current_file_dir)
         win_path = os.path.join(current_file_dir, 'win', 'win_auto_script.py')
```

### Comparing `nvosscript-1.1.2/win/win_auto_script.py` & `nvosscript-1.1.3/win/win_auto_script.py`

 * *Files identical despite different names*

