# Comparing `tmp/bobotools-0.4.7.8.tar.gz` & `tmp/bobotools-0.4.7.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bobotools-0.4.7.8.tar", last modified: Tue Jan  3 13:07:27 2023, max compression
+gzip compressed data, was "bobotools-0.4.7.9.tar", last modified: Fri Apr  7 03:18:01 2023, max compression
```

## Comparing `bobotools-0.4.7.8.tar` & `bobotools-0.4.7.9.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-03 13:07:27.336599 bobotools-0.4.7.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-01-03 13:07:27.336599 bobotools-0.4.7.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-03 13:07:27.336599 bobotools-0.4.7.8/bobotools/
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/bobotools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1930 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/bobotools/com.py
--rw-r--r--   0 runner    (1001) docker     (123)     6578 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/bobotools/img_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)      648 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/bobotools/list_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     3850 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/bobotools/torch_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     1482 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/bobotools/txt_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-03 13:07:27.336599 bobotools-0.4.7.8/bobotools.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-01-03 13:07:27.000000 bobotools-0.4.7.8/bobotools.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      337 2023-01-03 13:07:27.000000 bobotools-0.4.7.8/bobotools.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-03 13:07:27.000000 bobotools-0.4.7.8/bobotools.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-01-03 13:07:27.000000 bobotools-0.4.7.8/bobotools.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-03 13:07:27.000000 bobotools-0.4.7.8/bobotools.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-03 13:07:27.336599 bobotools-0.4.7.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1119 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-03 13:07:27.336599 bobotools-0.4.7.8/test/
--rw-r--r--   0 runner    (1001) docker     (123)     3219 2023-01-03 13:07:18.000000 bobotools-0.4.7.8/test/test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:18:01.287969 bobotools-0.4.7.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-04-07 03:18:01.287969 bobotools-0.4.7.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:18:01.287969 bobotools-0.4.7.9/bobotools/
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/bobotools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1930 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/bobotools/com.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6682 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/bobotools/img_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)      648 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/bobotools/list_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3850 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/bobotools/torch_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1482 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/bobotools/txt_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:18:01.287969 bobotools-0.4.7.9/bobotools.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-04-07 03:18:01.000000 bobotools-0.4.7.9/bobotools.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      337 2023-04-07 03:18:01.000000 bobotools-0.4.7.9/bobotools.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 03:18:01.000000 bobotools-0.4.7.9/bobotools.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-07 03:18:01.000000 bobotools-0.4.7.9/bobotools.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 03:18:01.000000 bobotools-0.4.7.9/bobotools.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 03:18:01.287969 bobotools-0.4.7.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1119 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 03:18:01.287969 bobotools-0.4.7.9/test/
+-rw-r--r--   0 runner    (1001) docker     (123)     3219 2023-04-07 03:17:50.000000 bobotools-0.4.7.9/test/test.py
```

### Comparing `bobotools-0.4.7.8/LICENSE` & `bobotools-0.4.7.9/LICENSE`

 * *Files identical despite different names*

### Comparing `bobotools-0.4.7.8/PKG-INFO` & `bobotools-0.4.7.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bobotools
-Version: 0.4.7.8
+Version: 0.4.7.9
 Summary: bobotools
 Author: bobo0810
 License: MIT
 Classifier: Environment :: Console
 Classifier: Natural Language :: English
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `bobotools-0.4.7.8/README.md` & `bobotools-0.4.7.9/README.md`

 * *Files identical despite different names*

### Comparing `bobotools-0.4.7.8/bobotools/com.py` & `bobotools-0.4.7.9/bobotools/com.py`

 * *Files identical despite different names*

### Comparing `bobotools-0.4.7.8/bobotools/img_tools.py` & `bobotools-0.4.7.9/bobotools/img_tools.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 import hashlib
 from tqdm import tqdm
 import numpy as np
 import cv2
-import torch
-import base64
 from multiprocessing import Process
 from urllib.request import urlretrieve
+from PIL import Image
 import os
 from .list_tools import List_Tools
 
 
 class Img_Tools(object):
     """
     Img工具类
@@ -115,16 +114,20 @@
 
         return
         error_list(list): 错误图像的列表。eg:[/home/a.jpg,...]
         """
         error_list = []
         for img_path in tqdm(imgs_list):
             try:
+                # cv2验证
                 image = cv2.imread(img_path, cv2.IMREAD_COLOR)
                 assert type(image) is np.ndarray
+
+                # PIL验证
+                image = Image.open(img_path).load()
             except:
                 error_list.append(img_path)
         return error_list
 
     @staticmethod
     def plot_yolo(img_path,txt_path,class_list,save_path,vis_conf=0.,lw=6):
         '''
```

### Comparing `bobotools-0.4.7.8/bobotools/list_tools.py` & `bobotools-0.4.7.9/bobotools/list_tools.py`

 * *Files identical despite different names*

### Comparing `bobotools-0.4.7.8/bobotools/torch_tools.py` & `bobotools-0.4.7.9/bobotools/torch_tools.py`

 * *Files identical despite different names*

### Comparing `bobotools-0.4.7.8/bobotools/txt_tools.py` & `bobotools-0.4.7.9/bobotools/txt_tools.py`

 * *Files identical despite different names*

### Comparing `bobotools-0.4.7.8/bobotools.egg-info/PKG-INFO` & `bobotools-0.4.7.9/bobotools.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bobotools
-Version: 0.4.7.8
+Version: 0.4.7.9
 Summary: bobotools
 Author: bobo0810
 License: MIT
 Classifier: Environment :: Console
 Classifier: Natural Language :: English
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `bobotools-0.4.7.8/setup.py` & `bobotools-0.4.7.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
     name="bobotools",
     packages=find_packages(),
     license="MIT",
     author="bobo0810",
     description="bobotools",
     long_description=open("README.md", "r").read(),
     long_description_content_type="text/markdown",
-    version="0.4.7.8",  # 版本
+    version="0.4.7.9",  # 版本
     install_requires=install_requires,
     python_requires=">=3.6",
     include_package_data=True,
     classifiers=[
         "Environment :: Console",
         "Natural Language :: English",
         "Development Status :: 4 - Beta",
```

### Comparing `bobotools-0.4.7.8/test/test.py` & `bobotools-0.4.7.9/test/test.py`

 * *Files identical despite different names*

