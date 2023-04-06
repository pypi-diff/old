# Comparing `tmp/snemail-1.1.7.tar.gz` & `tmp/snemail-1.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\snemail-1.1.7.tar", last modified: Thu Apr  6 05:24:53 2023, max compression
+gzip compressed data, was "dist\snemail-1.1.8.tar", last modified: Thu Apr  6 11:49:20 2023, max compression
```

## Comparing `snemail-1.1.7.tar` & `snemail-1.1.8.tar`

### file list

```diff
@@ -1,17 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 05:24:53.000000 snemail-1.1.7/
--rw-rw-rw-   0        0        0     1073 2023-04-05 12:52:43.000000 snemail-1.1.7/LICENSE
--rw-rw-rw-   0        0        0      427 2023-04-06 05:24:53.000000 snemail-1.1.7/PKG-INFO
--rw-rw-rw-   0        0        0        0 2023-04-05 04:13:19.000000 snemail-1.1.7/README.md
--rw-rw-rw-   0        0        0       42 2023-04-06 05:24:53.000000 snemail-1.1.7/setup.cfg
--rw-rw-rw-   0        0        0     1004 2023-04-06 05:24:36.000000 snemail-1.1.7/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 05:24:53.000000 snemail-1.1.7/snemail/
--rw-rw-rw-   0        0        0     7074 2023-04-06 05:22:18.000000 snemail-1.1.7/snemail/package.py
--rw-rw-rw-   0        0        0       22 2023-04-06 05:07:06.000000 snemail-1.1.7/snemail/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-06 05:24:53.000000 snemail-1.1.7/snemail.egg-info/
--rw-rw-rw-   0        0        0        1 2023-04-06 05:24:52.000000 snemail-1.1.7/snemail.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      427 2023-04-06 05:24:52.000000 snemail-1.1.7/snemail.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0        8 2023-04-06 05:24:52.000000 snemail-1.1.7/snemail.egg-info/requires.txt
--rw-rw-rw-   0        0        0      237 2023-04-06 05:24:52.000000 snemail-1.1.7/snemail.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        8 2023-04-06 05:24:52.000000 snemail-1.1.7/snemail.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-04-06 05:24:53.000000 snemail-1.1.7/test/
--rw-rw-rw-   0        0        0      506 2023-04-06 05:22:27.000000 snemail-1.1.7/test/test_demp.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:49:20.000000 snemail-1.1.8/
+-rw-rw-rw-   0        0        0     1073 2023-04-05 12:52:43.000000 snemail-1.1.8/LICENSE
+-rw-rw-rw-   0        0        0     3740 2023-04-06 11:49:20.000000 snemail-1.1.8/PKG-INFO
+-rw-rw-rw-   0        0        0     3320 2023-04-06 11:47:49.000000 snemail-1.1.8/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 11:49:20.000000 snemail-1.1.8/setup.cfg
+-rw-rw-rw-   0        0        0     1006 2023-04-06 11:47:20.000000 snemail-1.1.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:49:20.000000 snemail-1.1.8/snemail/
+-rw-rw-rw-   0        0        0     7074 2023-04-06 11:46:59.000000 snemail-1.1.8/snemail/package.py
+-rw-rw-rw-   0        0        0       22 2023-04-06 05:07:06.000000 snemail-1.1.8/snemail/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 11:49:20.000000 snemail-1.1.8/snemail.egg-info/
+-rw-rw-rw-   0        0        0        1 2023-04-06 11:49:18.000000 snemail-1.1.8/snemail.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0     3740 2023-04-06 11:49:18.000000 snemail-1.1.8/snemail.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      207 2023-04-06 11:49:18.000000 snemail-1.1.8/snemail.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 11:49:18.000000 snemail-1.1.8/snemail.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 11:49:20.000000 snemail-1.1.8/test/
+-rw-rw-rw-   0        0        0      568 2023-04-06 11:40:00.000000 snemail-1.1.8/test/test_demp.py
```

### Comparing `snemail-1.1.7/LICENSE` & `snemail-1.1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `snemail-1.1.7/setup.py` & `snemail-1.1.8/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="snemail",
-    version="1.1.7",
+    version="1.1.8",
     author="manji",
     author_email="pnsm@qq.com",                         # 作者邮箱
     description="发送邮件库",                            # 模块简介
     long_description=long_description,                  # 模块详细介绍
     long_description_content_type="text/markdown",      # 模块详细介绍格式
     url="",
     packages=setuptools.find_packages(),                # 自动找到项目中导入的模块
@@ -19,12 +19,12 @@
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 
     # 依赖模块
     install_requires=[
-        'PyEmail',
+        # 'PyEmail',
     ],
 
     python_requires='>=3' ,                             # 运行的python版本
 )
```

### Comparing `snemail-1.1.7/snemail/package.py` & `snemail-1.1.8/snemail/package.py`

 * *Files identical despite different names*

