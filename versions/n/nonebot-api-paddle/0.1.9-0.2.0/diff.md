# Comparing `tmp/nonebot_api_paddle-0.1.9.tar.gz` & `tmp/nonebot_api_paddle-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nonebot_api_paddle-0.1.9.tar", last modified: Thu Apr  6 14:43:59 2023, max compression
+gzip compressed data, was "nonebot_api_paddle-0.2.0.tar", last modified: Thu Apr  6 14:51:04 2023, max compression
```

## Comparing `nonebot_api_paddle-0.1.9.tar` & `nonebot_api_paddle-0.2.0.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 14:43:59.841827 nonebot_api_paddle-0.1.9/
--rw-rw-rw-   0        0        0    12533 2023-04-02 14:35:33.000000 nonebot_api_paddle-0.1.9/LICENSE.txt
--rw-rw-rw-   0        0        0      858 2023-04-06 14:43:59.840829 nonebot_api_paddle-0.1.9/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-06 14:43:59.835847 nonebot_api_paddle-0.1.9/nonebot_api_paddle/
--rw-rw-rw-   0        0        0     5228 2023-04-06 14:20:19.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle/__init__.py
--rw-rw-rw-   0        0        0     3143 2023-04-06 12:04:09.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle/api_excel.py
--rw-rw-rw-   0        0        0     2410 2023-04-06 07:39:32.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle/api_ocr.py
--rw-rw-rw-   0        0        0     2461 2023-04-04 12:52:45.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle/api_voice.py
-drwxrwxrwx   0        0        0        0 2023-04-06 14:43:59.839833 nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/
--rw-rw-rw-   0        0        0      858 2023-04-06 14:43:59.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      354 2023-04-06 14:43:59.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 14:43:59.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      141 2023-04-06 14:43:59.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/requires.txt
--rw-rw-rw-   0        0        0       19 2023-04-06 14:43:59.000000 nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 14:43:59.841827 nonebot_api_paddle-0.1.9/setup.cfg
--rw-rw-rw-   0        0        0     1246 2023-04-06 14:43:57.000000 nonebot_api_paddle-0.1.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:51:04.314407 nonebot_api_paddle-0.2.0/
+-rw-rw-rw-   0        0        0    12533 2023-04-02 14:35:33.000000 nonebot_api_paddle-0.2.0/LICENSE.txt
+-rw-rw-rw-   0        0        0      858 2023-04-06 14:51:04.313408 nonebot_api_paddle-0.2.0/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 14:51:04.307428 nonebot_api_paddle-0.2.0/nonebot_api_paddle/
+-rw-rw-rw-   0        0        0     5228 2023-04-06 14:20:19.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle/__init__.py
+-rw-rw-rw-   0        0        0     3143 2023-04-06 12:04:09.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle/api_excel.py
+-rw-rw-rw-   0        0        0     2410 2023-04-06 07:39:32.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle/api_ocr.py
+-rw-rw-rw-   0        0        0     2461 2023-04-04 12:52:45.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle/api_voice.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:51:04.312412 nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/
+-rw-rw-rw-   0        0        0      858 2023-04-06 14:51:04.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      354 2023-04-06 14:51:04.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:51:04.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      141 2023-04-06 14:51:04.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       19 2023-04-06 14:51:04.000000 nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:51:04.314407 nonebot_api_paddle-0.2.0/setup.cfg
+-rw-rw-rw-   0        0        0     1245 2023-04-06 14:50:52.000000 nonebot_api_paddle-0.2.0/setup.py
```

### Comparing `nonebot_api_paddle-0.1.9/LICENSE.txt` & `nonebot_api_paddle-0.2.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-0.1.9/PKG-INFO` & `nonebot_api_paddle-0.2.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nonebot_api_paddle
-Version: 0.1.9
+Version: 0.2.0
 Summary: nonbot_api_paddle
 Home-page: https://github.com/canxin121/nonebot_api_paddle
 Author: canxin
 Author-email: 1969730106@qq.com
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
```

### Comparing `nonebot_api_paddle-0.1.9/nonebot_api_paddle/__init__.py` & `nonebot_api_paddle-0.2.0/nonebot_api_paddle/__init__.py`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-0.1.9/nonebot_api_paddle/api_excel.py` & `nonebot_api_paddle-0.2.0/nonebot_api_paddle/api_excel.py`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-0.1.9/nonebot_api_paddle/api_ocr.py` & `nonebot_api_paddle-0.2.0/nonebot_api_paddle/api_ocr.py`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-0.1.9/nonebot_api_paddle/api_voice.py` & `nonebot_api_paddle-0.2.0/nonebot_api_paddle/api_voice.py`

 * *Files identical despite different names*

### Comparing `nonebot_api_paddle-0.1.9/nonebot_api_paddle.egg-info/PKG-INFO` & `nonebot_api_paddle-0.2.0/nonebot_api_paddle.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nonebot-api-paddle
-Version: 0.1.9
+Version: 0.2.0
 Summary: nonbot_api_paddle
 Home-page: https://github.com/canxin121/nonebot_api_paddle
 Author: canxin
 Author-email: 1969730106@qq.com
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.8
 Classifier: License :: OSI Approved :: GNU Affero General Public License v3
```

### Comparing `nonebot_api_paddle-0.1.9/setup.py` & `nonebot_api_paddle-0.2.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
-with open("readme.rst", "r", encoding="utf-8") as f:
+with open("readme.md", "r", encoding="utf-8") as f:
     long_description = f.read()
 
 setuptools.setup(
     name="nonebot_api_paddle",  # 项目名称，保证它的唯一性，不要跟已存在的包名冲突即可
-    version="0.1.9",  # 程序版本
+    version="0.2.0",  # 程序版本
     author="canxin",  # 项目作者
     author_email="1969730106@qq.com",  # 作者邮件
     description="nonbot_api_paddle",  # 项目的一句话描述
     long_description=long_description,  # 加长版描述
     long_description_content_type="text/markdown",  # 描述使用Markdown
     url="https://github.com/canxin121/nonebot_api_paddle",  # 项目地址
     packages=setuptools.find_packages(),  # 无需修改
```

