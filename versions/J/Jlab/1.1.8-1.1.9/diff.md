# Comparing `tmp/Jlab-1.1.8.tar.gz` & `tmp/Jlab-1.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Jlab-1.1.8.tar", last modified: Mon Apr  3 11:40:49 2023, max compression
+gzip compressed data, was "Jlab-1.1.9.tar", last modified: Mon Apr  3 19:13:12 2023, max compression
```

## Comparing `Jlab-1.1.8.tar` & `Jlab-1.1.9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 shihyu    (1000) shihyu    (1000)        0 2023-04-03 11:40:49.538626 Jlab-1.1.8/
-drwxr-xr-x   0 shihyu    (1000) shihyu    (1000)        0 2023-04-03 11:40:49.534626 Jlab-1.1.8/Jlab/
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)      144 2023-04-03 11:19:06.000000 Jlab-1.1.8/Jlab/__init__.py
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)     3394 2023-04-02 18:06:01.000000 Jlab-1.1.8/Jlab/shioaji_wrapper.py
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)     1753 2023-04-03 11:32:42.000000 Jlab-1.1.8/Jlab/utils.py
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)      519 2023-04-02 17:27:12.000000 Jlab-1.1.8/Jlab/watcher.py
-drwxr-xr-x   0 shihyu    (1000) shihyu    (1000)        0 2023-04-03 11:40:49.538626 Jlab-1.1.8/Jlab.egg-info/
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)      634 2023-04-03 11:40:49.000000 Jlab-1.1.8/Jlab.egg-info/PKG-INFO
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)      240 2023-04-03 11:40:49.000000 Jlab-1.1.8/Jlab.egg-info/SOURCES.txt
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)        1 2023-04-03 11:40:49.000000 Jlab-1.1.8/Jlab.egg-info/dependency_links.txt
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)       15 2023-04-03 11:40:49.000000 Jlab-1.1.8/Jlab.egg-info/requires.txt
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)        5 2023-04-03 11:40:49.000000 Jlab-1.1.8/Jlab.egg-info/top_level.txt
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)     1068 2023-04-01 11:22:33.000000 Jlab-1.1.8/LICENSE.txt
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)      634 2023-04-03 11:40:49.538626 Jlab-1.1.8/PKG-INFO
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)       51 2023-04-01 12:27:33.000000 Jlab-1.1.8/README.md
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)       38 2023-04-03 11:40:49.538626 Jlab-1.1.8/setup.cfg
--rw-r--r--   0 shihyu    (1000) shihyu    (1000)      944 2023-04-03 11:40:45.000000 Jlab-1.1.8/setup.py
+drwxr-xr-x   0 shihyu    (1000) shihyu    (1000)        0 2023-04-03 19:13:12.865791 Jlab-1.1.9/
+drwxr-xr-x   0 shihyu    (1000) shihyu    (1000)        0 2023-04-03 19:13:12.865791 Jlab-1.1.9/Jlab/
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)      189 2023-04-03 19:11:58.000000 Jlab-1.1.9/Jlab/__init__.py
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)     3394 2023-04-03 18:24:51.000000 Jlab-1.1.9/Jlab/shioaji_wrapper.py
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)     2360 2023-04-03 19:12:15.000000 Jlab-1.1.9/Jlab/utils.py
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)      519 2023-04-03 18:24:51.000000 Jlab-1.1.9/Jlab/watcher.py
+drwxr-xr-x   0 shihyu    (1000) shihyu    (1000)        0 2023-04-03 19:13:12.865791 Jlab-1.1.9/Jlab.egg-info/
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)      634 2023-04-03 19:13:12.000000 Jlab-1.1.9/Jlab.egg-info/PKG-INFO
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)      240 2023-04-03 19:13:12.000000 Jlab-1.1.9/Jlab.egg-info/SOURCES.txt
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)        1 2023-04-03 19:13:12.000000 Jlab-1.1.9/Jlab.egg-info/dependency_links.txt
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)       15 2023-04-03 19:13:12.000000 Jlab-1.1.9/Jlab.egg-info/requires.txt
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)        5 2023-04-03 19:13:12.000000 Jlab-1.1.9/Jlab.egg-info/top_level.txt
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)     1068 2023-04-03 18:24:51.000000 Jlab-1.1.9/LICENSE.txt
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)      634 2023-04-03 19:13:12.865791 Jlab-1.1.9/PKG-INFO
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)       51 2023-04-03 18:24:51.000000 Jlab-1.1.9/README.md
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)       38 2023-04-03 19:13:12.865791 Jlab-1.1.9/setup.cfg
+-rw-r--r--   0 shihyu    (1000) shihyu    (1000)      944 2023-04-03 19:12:55.000000 Jlab-1.1.9/setup.py
```

### Comparing `Jlab-1.1.8/Jlab/shioaji_wrapper.py` & `Jlab-1.1.9/Jlab/shioaji_wrapper.py`

 * *Files identical despite different names*

### Comparing `Jlab-1.1.8/Jlab/utils.py` & `Jlab-1.1.9/Jlab/utils.py`

 * *Files 16% similar despite different names*

```diff
@@ -2,15 +2,36 @@
 from retry import retry
 from github import Github
 import os
 import time
 
 
 @retry(exceptions=Exception, tries=3, delay=2, backoff=2)
-def update_github(token, repo_name, filename):
+def download_github_file(token, repo_name, filename):
+    # 獲取當前工作目錄路徑
+    cwd = os.path.abspath(os.getcwd())
+
+    # 使用 token 連接 Github API
+    g = Github(token)
+    user = g.get_user()
+    repo = user.get_repo(repo_name)
+
+    # 獲取檔案內容
+    file_content = repo.get_contents(filename)
+    file_content_str = file_content.decoded_content.decode("utf-8")
+
+    # 寫入本地檔案
+    with open(os.path.join(cwd, filename), "w") as f:
+        f.write(file_content_str)
+
+    print(f"{filename} downloaded")
+
+
+@retry(exceptions=Exception, tries=3, delay=2, backoff=2)
+def update_github_file(token, repo_name, filename):
     # 獲取當前工作目錄路徑
     cwd = os.path.abspath(os.getcwd())
 
     # 使用 token 連接 Github API
     g = Github(token)
     user = g.get_user()
     repo = user.get_repo(repo_name)
```

### Comparing `Jlab-1.1.8/Jlab/watcher.py` & `Jlab-1.1.9/Jlab/watcher.py`

 * *Files identical despite different names*

### Comparing `Jlab-1.1.8/Jlab.egg-info/PKG-INFO` & `Jlab-1.1.9/Jlab.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Jlab
-Version: 1.1.8
+Version: 1.1.9
 Summary: Jlab is a package for data analysis
 Author: twfxjjbw
 Author-email: twfxjjbw@gmail.com
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

### Comparing `Jlab-1.1.8/LICENSE.txt` & `Jlab-1.1.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `Jlab-1.1.8/PKG-INFO` & `Jlab-1.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Jlab
-Version: 1.1.8
+Version: 1.1.9
 Summary: Jlab is a package for data analysis
 Author: twfxjjbw
 Author-email: twfxjjbw@gmail.com
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
```

### Comparing `Jlab-1.1.8/setup.py` & `Jlab-1.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     long_description = fh.read()
 
 with open("requirements.txt", "r", encoding="utf-8") as f:
     requirements = f.read().split("\n")
 
 setuptools.setup(
     name="Jlab",
-    version="1.1.8",
+    version="1.1.9",
     author="twfxjjbw",
     author_email="twfxjjbw@gmail.com",
     description="Jlab is a package for data analysis",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
```

