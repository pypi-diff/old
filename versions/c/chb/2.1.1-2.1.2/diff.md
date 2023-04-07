# Comparing `tmp/chb-2.1.1.tar.gz` & `tmp/chb-2.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/chb-2.1.1.tar", last modified: Fri Apr  7 03:14:27 2023, max compression
+gzip compressed data, was "dist/chb-2.1.2.tar", last modified: Fri Apr  7 05:46:05 2023, max compression
```

## Comparing `chb-2.1.1.tar` & `chb-2.1.2.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxr-x   0 chb       (1000) chb       (1000)        0 2023-04-07 03:14:27.909933 chb-2.1.1/
--rw-rw-r--   0 chb       (1000) chb       (1000)     1073 2023-03-13 03:16:24.000000 chb-2.1.1/LICENSE.txt
--rw-rw-r--   0 chb       (1000) chb       (1000)      615 2023-04-07 03:14:27.909933 chb-2.1.1/PKG-INFO
--rw-rw-r--   0 chb       (1000) chb       (1000)      199 2023-03-13 03:16:24.000000 chb-2.1.1/README.md
-drwxrwxr-x   0 chb       (1000) chb       (1000)        0 2023-04-07 03:14:27.909933 chb-2.1.1/chb/
--rw-rw-r--   0 chb       (1000) chb       (1000)     5320 2023-03-13 03:16:24.000000 chb-2.1.1/chb/__init__.py
--rw-rw-r--   0 chb       (1000) chb       (1000)     8292 2023-04-07 03:13:23.000000 chb-2.1.1/chb/_dao.py
--rw-rw-r--   0 chb       (1000) chb       (1000)     3340 2023-03-13 03:16:24.000000 chb-2.1.1/chb/_importable.py
--rw-rw-r--   0 chb       (1000) chb       (1000)     3873 2023-03-13 03:16:24.000000 chb-2.1.1/chb/_imports.py
--rw-rw-r--   0 chb       (1000) chb       (1000)     4525 2023-03-13 03:16:24.000000 chb-2.1.1/chb/_log.py
--rw-rw-r--   0 chb       (1000) chb       (1000)    23950 2023-03-13 03:46:28.000000 chb-2.1.1/chb/_utils.py
-drwxrwxr-x   0 chb       (1000) chb       (1000)        0 2023-04-07 03:14:27.909933 chb-2.1.1/chb.egg-info/
--rw-rw-r--   0 chb       (1000) chb       (1000)      615 2023-04-07 03:14:27.000000 chb-2.1.1/chb.egg-info/PKG-INFO
--rw-rw-r--   0 chb       (1000) chb       (1000)      237 2023-04-07 03:14:27.000000 chb-2.1.1/chb.egg-info/SOURCES.txt
--rw-rw-r--   0 chb       (1000) chb       (1000)        1 2023-04-07 03:14:27.000000 chb-2.1.1/chb.egg-info/dependency_links.txt
--rw-rw-r--   0 chb       (1000) chb       (1000)        4 2023-04-07 03:14:27.000000 chb-2.1.1/chb.egg-info/top_level.txt
--rw-rw-r--   0 chb       (1000) chb       (1000)       79 2023-04-07 03:14:27.909933 chb-2.1.1/setup.cfg
--rw-rw-r--   0 chb       (1000) chb       (1000)     1004 2023-04-07 03:13:35.000000 chb-2.1.1/setup.py
+drwxrwxr-x   0 chb       (1000) chb       (1000)        0 2023-04-07 05:46:05.550513 chb-2.1.2/
+-rw-rw-r--   0 chb       (1000) chb       (1000)     1073 2023-03-13 03:16:24.000000 chb-2.1.2/LICENSE.txt
+-rw-rw-r--   0 chb       (1000) chb       (1000)      615 2023-04-07 05:46:05.554513 chb-2.1.2/PKG-INFO
+-rw-rw-r--   0 chb       (1000) chb       (1000)      199 2023-03-13 03:16:24.000000 chb-2.1.2/README.md
+drwxrwxr-x   0 chb       (1000) chb       (1000)        0 2023-04-07 05:46:05.550513 chb-2.1.2/chb/
+-rw-rw-r--   0 chb       (1000) chb       (1000)     5320 2023-03-13 03:16:24.000000 chb-2.1.2/chb/__init__.py
+-rw-rw-r--   0 chb       (1000) chb       (1000)     8292 2023-04-07 05:45:16.000000 chb-2.1.2/chb/_dao.py
+-rw-rw-r--   0 chb       (1000) chb       (1000)     3340 2023-03-13 03:16:24.000000 chb-2.1.2/chb/_importable.py
+-rw-rw-r--   0 chb       (1000) chb       (1000)     3873 2023-03-13 03:16:24.000000 chb-2.1.2/chb/_imports.py
+-rw-rw-r--   0 chb       (1000) chb       (1000)     4525 2023-03-13 03:16:24.000000 chb-2.1.2/chb/_log.py
+-rw-rw-r--   0 chb       (1000) chb       (1000)    23950 2023-03-13 03:46:28.000000 chb-2.1.2/chb/_utils.py
+drwxrwxr-x   0 chb       (1000) chb       (1000)        0 2023-04-07 05:46:05.550513 chb-2.1.2/chb.egg-info/
+-rw-rw-r--   0 chb       (1000) chb       (1000)      615 2023-04-07 05:46:05.000000 chb-2.1.2/chb.egg-info/PKG-INFO
+-rw-rw-r--   0 chb       (1000) chb       (1000)      237 2023-04-07 05:46:05.000000 chb-2.1.2/chb.egg-info/SOURCES.txt
+-rw-rw-r--   0 chb       (1000) chb       (1000)        1 2023-04-07 05:46:05.000000 chb-2.1.2/chb.egg-info/dependency_links.txt
+-rw-rw-r--   0 chb       (1000) chb       (1000)        4 2023-04-07 05:46:05.000000 chb-2.1.2/chb.egg-info/top_level.txt
+-rw-rw-r--   0 chb       (1000) chb       (1000)       79 2023-04-07 05:46:05.554513 chb-2.1.2/setup.cfg
+-rw-rw-r--   0 chb       (1000) chb       (1000)     1004 2023-04-07 05:45:43.000000 chb-2.1.2/setup.py
```

### Comparing `chb-2.1.1/LICENSE.txt` & `chb-2.1.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `chb-2.1.1/PKG-INFO` & `chb-2.1.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: chb
-Version: 2.1.1
+Version: 2.1.2
 Summary: chb常用代码库
 Home-page: https://github.com/ChenHuabin321/pypi
 Author: chenhuabin
 Author-email: chenhuabin321@163.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `chb-2.1.1/chb/__init__.py` & `chb-2.1.2/chb/__init__.py`

 * *Files identical despite different names*

### Comparing `chb-2.1.1/chb/_dao.py` & `chb-2.1.2/chb/_dao.py`

 * *Files 0% similar despite different names*

```diff
@@ -238,15 +238,15 @@
         """
         向名为set_name的hash队列中添加一个键值对
         """
         if isinstance(value, (dict, list)):
             value = json.dumps(value)
         self.db.hset(set_name, key, value)
 
-    def gset(self, set_name, key):
+    def hget(self, set_name, key):
         """
         从名为set_name的hash队列中获取一个键值对
         """
         value = self.db.hset(set_name, key)
         if isinstance(value, (dict, list)):
             value = json.loads(value)
         return value
```

### Comparing `chb-2.1.1/chb/_importable.py` & `chb-2.1.2/chb/_importable.py`

 * *Files identical despite different names*

### Comparing `chb-2.1.1/chb/_imports.py` & `chb-2.1.2/chb/_imports.py`

 * *Files identical despite different names*

### Comparing `chb-2.1.1/chb/_log.py` & `chb-2.1.2/chb/_log.py`

 * *Files identical despite different names*

### Comparing `chb-2.1.1/chb/_utils.py` & `chb-2.1.2/chb/_utils.py`

 * *Files identical despite different names*

### Comparing `chb-2.1.1/chb.egg-info/PKG-INFO` & `chb-2.1.2/chb.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: chb
-Version: 2.1.1
+Version: 2.1.2
 Summary: chb常用代码库
 Home-page: https://github.com/ChenHuabin321/pypi
 Author: chenhuabin
 Author-email: chenhuabin321@163.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `chb-2.1.1/setup.py` & `chb-2.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools  # 导入setuptools打包工具
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="chb",  # 用自己的名替换其中的YOUR_USERNAME_
-    version="2.1.1",  # 包版本号，便于维护版本
+    version="2.1.2",  # 包版本号，便于维护版本
     author="chenhuabin",  # 作者，可以写自己的姓名
     author_email="chenhuabin321@163.com",  # 作者联系方式，可写自己的邮箱地址
     description="chb常用代码库",  # 包的简述
     long_description=long_description,  # 包的详细介绍，一般在README.md文件内
     long_description_content_type="text/markdown",
     url="https://github.com/ChenHuabin321/pypi",  # 自己项目地址，比如github的项目地址
     packages=setuptools.find_packages(),
```

