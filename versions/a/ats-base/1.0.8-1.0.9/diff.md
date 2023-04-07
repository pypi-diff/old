# Comparing `tmp/ats_base-1.0.8.tar.gz` & `tmp/ats_base-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ats_base-1.0.8.tar", last modified: Wed Mar  8 01:49:06 2023, max compression
+gzip compressed data, was "ats_base-1.0.9.tar", last modified: Fri Apr  7 01:09:48 2023, max compression
```

## Comparing `ats_base-1.0.8.tar` & `ats_base-1.0.9.tar`

### file list

```diff
@@ -1,40 +1,39 @@
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:06.014298 ats_base-1.0.8/
--rw-rw-rw-   0        0        0      116 2022-09-15 08:18:29.000000 ats_base-1.0.8/LICENSE
--rw-rw-rw-   0        0        0        0 2022-06-08 07:14:13.000000 ats_base-1.0.8/MANIFEST.in
--rw-rw-rw-   0        0        0     1042 2023-03-08 01:49:06.011305 ats_base-1.0.8/PKG-INFO
--rw-rw-rw-   0        0        0      532 2022-06-13 07:56:24.000000 ats_base-1.0.8/README.md
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.454107 ats_base-1.0.8/ats_base/
--rw-rw-rw-   0        0        0        0 2022-09-15 08:20:17.000000 ats_base-1.0.8/ats_base/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.623235 ats_base-1.0.8/ats_base/base/
--rw-rw-rw-   0        0        0        0 2022-09-15 08:27:28.000000 ats_base-1.0.8/ats_base/base/__init__.py
--rw-rw-rw-   0        0        0      868 2022-10-08 05:21:17.000000 ats_base-1.0.8/ats_base/base/entrance.py
--rw-rw-rw-   0        0        0     1739 2022-09-19 00:42:09.000000 ats_base-1.0.8/ats_base/base/req.py
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.682790 ats_base-1.0.8/ats_base/common/
--rw-rw-rw-   0        0        0        0 2022-05-30 03:34:10.000000 ats_base-1.0.8/ats_base/common/__init__.py
--rw-rw-rw-   0        0        0     3645 2023-03-06 01:40:30.000000 ats_base-1.0.8/ats_base/common/func.py
--rw-rw-rw-   0        0        0      656 2022-10-11 06:12:32.000000 ats_base-1.0.8/ats_base/common/resp.py
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.758584 ats_base-1.0.8/ats_base/config/
--rw-rw-rw-   0        0        0        0 2022-05-26 08:20:18.000000 ats_base-1.0.8/ats_base/config/__init__.py
--rw-rw-rw-   0        0        0      423 2023-03-08 01:39:42.000000 ats_base-1.0.8/ats_base/config/config.ini
--rw-rw-rw-   0        0        0      251 2022-05-30 01:53:51.000000 ats_base-1.0.8/ats_base/config/configure.py
--rw-rw-rw-   0        0        0     1108 2022-12-22 02:31:24.000000 ats_base-1.0.8/ats_base/config/rewrite_config.py
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.795819 ats_base-1.0.8/ats_base/log/
--rw-rw-rw-   0        0        0        0 2022-09-20 00:58:33.000000 ats_base-1.0.8/ats_base/log/__init__.py
--rw-rw-rw-   0        0        0     3460 2023-03-06 01:40:56.000000 ats_base-1.0.8/ats_base/log/logger.py
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.983161 ats_base-1.0.8/ats_base/service/
--rw-rw-rw-   0        0        0        0 2022-05-26 08:20:27.000000 ats_base-1.0.8/ats_base/service/__init__.py
--rw-rw-rw-   0        0        0      225 2022-09-16 06:07:59.000000 ats_base-1.0.8/ats_base/service/app.py
--rw-rw-rw-   0        0        0     1691 2022-10-08 06:47:45.000000 ats_base-1.0.8/ats_base/service/db.py
--rw-rw-rw-   0        0        0      548 2022-10-08 06:47:45.000000 ats_base-1.0.8/ats_base/service/dvs.py
--rw-rw-rw-   0        0        0      436 2022-12-21 08:13:03.000000 ats_base-1.0.8/ats_base/service/em.py
--rw-rw-rw-   0        0        0     8729 2022-10-26 00:59:06.000000 ats_base-1.0.8/ats_base/service/mm.py
--rw-rw-rw-   0        0        0      957 2022-10-09 01:12:00.000000 ats_base-1.0.8/ats_base/service/pro.py
--rw-rw-rw-   0        0        0      960 2023-03-08 01:48:59.000000 ats_base-1.0.8/ats_base/service/udm.py
-drwxrwxrwx   0        0        0        0 2023-03-08 01:49:05.556415 ats_base-1.0.8/ats_base.egg-info/
--rw-rw-rw-   0        0        0     1042 2023-03-08 01:49:04.000000 ats_base-1.0.8/ats_base.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      727 2023-03-08 01:49:05.000000 ats_base-1.0.8/ats_base.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-08 01:49:04.000000 ats_base-1.0.8/ats_base.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       34 2023-03-08 01:49:04.000000 ats_base-1.0.8/ats_base.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-03-08 01:49:04.000000 ats_base-1.0.8/ats_base.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-08 01:49:06.014298 ats_base-1.0.8/setup.cfg
--rw-rw-rw-   0        0        0      947 2023-03-08 01:48:59.000000 ats_base-1.0.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.579570 ats_base-1.0.9/
+-rw-rw-rw-   0        0        0      116 2022-09-15 08:18:29.000000 ats_base-1.0.9/LICENSE
+-rw-rw-rw-   0        0        0        0 2022-06-08 07:14:13.000000 ats_base-1.0.9/MANIFEST.in
+-rw-rw-rw-   0        0        0     1042 2023-04-07 01:09:48.578573 ats_base-1.0.9/PKG-INFO
+-rw-rw-rw-   0        0        0      532 2022-06-13 07:56:24.000000 ats_base-1.0.9/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.026865 ats_base-1.0.9/ats_base/
+-rw-rw-rw-   0        0        0        0 2022-09-15 08:20:17.000000 ats_base-1.0.9/ats_base/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.175826 ats_base-1.0.9/ats_base/base/
+-rw-rw-rw-   0        0        0        0 2022-09-15 08:27:28.000000 ats_base-1.0.9/ats_base/base/__init__.py
+-rw-rw-rw-   0        0        0      868 2022-10-08 05:21:17.000000 ats_base-1.0.9/ats_base/base/entrance.py
+-rw-rw-rw-   0        0        0     1739 2023-04-07 00:56:47.000000 ats_base-1.0.9/ats_base/base/req.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.238417 ats_base-1.0.9/ats_base/common/
+-rw-rw-rw-   0        0        0        0 2022-05-30 03:34:10.000000 ats_base-1.0.9/ats_base/common/__init__.py
+-rw-rw-rw-   0        0        0     3645 2023-03-06 01:40:30.000000 ats_base-1.0.9/ats_base/common/func.py
+-rw-rw-rw-   0        0        0      656 2022-10-11 06:12:32.000000 ats_base-1.0.9/ats_base/common/resp.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.312941 ats_base-1.0.9/ats_base/config/
+-rw-rw-rw-   0        0        0        0 2022-05-26 08:20:18.000000 ats_base-1.0.9/ats_base/config/__init__.py
+-rw-rw-rw-   0        0        0      401 2023-04-07 01:00:41.000000 ats_base-1.0.9/ats_base/config/config.ini
+-rw-rw-rw-   0        0        0      251 2022-05-30 01:53:51.000000 ats_base-1.0.9/ats_base/config/configure.py
+-rw-rw-rw-   0        0        0     1108 2022-12-22 02:31:24.000000 ats_base-1.0.9/ats_base/config/rewrite_config.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.348479 ats_base-1.0.9/ats_base/log/
+-rw-rw-rw-   0        0        0        0 2022-09-20 00:58:33.000000 ats_base-1.0.9/ats_base/log/__init__.py
+-rw-rw-rw-   0        0        0     3460 2023-03-06 01:40:56.000000 ats_base-1.0.9/ats_base/log/logger.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.537682 ats_base-1.0.9/ats_base/service/
+-rw-rw-rw-   0        0        0        0 2022-05-26 08:20:27.000000 ats_base-1.0.9/ats_base/service/__init__.py
+-rw-rw-rw-   0        0        0      225 2022-09-16 06:07:59.000000 ats_base-1.0.9/ats_base/service/app.py
+-rw-rw-rw-   0        0        0     1691 2022-10-08 06:47:45.000000 ats_base-1.0.9/ats_base/service/db.py
+-rw-rw-rw-   0        0        0      436 2022-12-21 08:13:03.000000 ats_base-1.0.9/ats_base/service/em.py
+-rw-rw-rw-   0        0        0     8729 2022-10-26 00:59:06.000000 ats_base-1.0.9/ats_base/service/mm.py
+-rw-rw-rw-   0        0        0      957 2022-10-09 01:12:00.000000 ats_base-1.0.9/ats_base/service/pro.py
+-rw-rw-rw-   0        0        0     1236 2023-04-07 01:08:33.000000 ats_base-1.0.9/ats_base/service/udm.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:09:48.114750 ats_base-1.0.9/ats_base.egg-info/
+-rw-rw-rw-   0        0        0     1042 2023-04-07 01:09:47.000000 ats_base-1.0.9/ats_base.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      703 2023-04-07 01:09:47.000000 ats_base-1.0.9/ats_base.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 01:09:47.000000 ats_base-1.0.9/ats_base.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       34 2023-04-07 01:09:47.000000 ats_base-1.0.9/ats_base.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-07 01:09:47.000000 ats_base-1.0.9/ats_base.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 01:09:48.580568 ats_base-1.0.9/setup.cfg
+-rw-rw-rw-   0        0        0      947 2023-04-07 01:09:28.000000 ats_base-1.0.9/setup.py
```

### Comparing `ats_base-1.0.8/PKG-INFO` & `ats_base-1.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ats_base
-Version: 1.0.8
+Version: 1.0.9
 Summary: Test Script Development Library
 Home-page: https://gitee.com/henry9000/ats_base
 Author: zhangyue
 Author-email: zhangyue@techen.cn
 Project-URL: Bug Tracker, https://gitee.com/henry9000/ats_base/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `ats_base-1.0.8/README.md` & `ats_base-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/base/entrance.py` & `ats_base-1.0.9/ats_base/base/entrance.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/base/req.py` & `ats_base-1.0.9/ats_base/base/req.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import requests
 import json
 
-_timeout_ = 60
+_timeout_ = 90
 _method_ = 'get'
 
 
 def get(url, params: dict = None):
     """
     请求方式 - get
     :param url:
```

### Comparing `ats_base-1.0.8/ats_base/common/func.py` & `ats_base-1.0.9/ats_base/common/func.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/common/resp.py` & `ats_base-1.0.9/ats_base/common/resp.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/config/rewrite_config.py` & `ats_base-1.0.9/ats_base/config/rewrite_config.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/log/logger.py` & `ats_base-1.0.9/ats_base/log/logger.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/service/db.py` & `ats_base-1.0.9/ats_base/service/db.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/service/mm.py` & `ats_base-1.0.9/ats_base/service/mm.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/service/pro.py` & `ats_base-1.0.9/ats_base/service/pro.py`

 * *Files identical despite different names*

### Comparing `ats_base-1.0.8/ats_base/service/udm.py` & `ats_base-1.0.9/ats_base/service/udm.py`

 * *Files 16% similar despite different names*

```diff
@@ -4,37 +4,48 @@
 from ats_base.base import req, entrance
 from ats_base.common import func
 from ats_base.config.configure import CONFIG
 
 udm = entrance.api(CONFIG.get(func.SERVICE, 'udm'))
 
 
-def acv(module: str, function: str, data):
+def acv(module: str, function: str, data, url: str = None):
     """
     数据验证
     :param module:
     :param function:
     :param data:
+    :param url:
     :return:
     """
-    result = req.post('{}/{}/{}'.format('{}/{}'.format(udm, 'acv'), module, function), jsons=data)
+    s_url = _get_service_url(url)
+    result = req.post('{}/{}/{}'.format('{}/{}'.format(s_url, 'acv'), module, function), jsons=data)
 
     if result['code'] == 500:
         raise Exception(result['message'])
 
     return result['data']
 
 
-def built_in(module: str, function: str, data):
+def built_in(module: str, function: str, data, url: str = None):
     """
-    数据验证
+    内置函数
     :param module:
     :param function:
     :param data:
+    :param url:
     :return:
     """
-    result = req.post('{}/{}/{}'.format('{}/{}'.format(udm, 'built_in'), module, function), jsons=data)
+    s_url = _get_service_url(url)
+    result = req.post('{}/{}/{}'.format('{}/{}'.format(s_url, 'built_in'), module, function), jsons=data)
 
     if result['code'] == 500:
         raise Exception(result['message'])
 
     return result['data']
+
+
+def _get_service_url(url: str = None):
+    if url is not None and func.is_valid_url(url):
+        return url
+
+    return udm
```

### Comparing `ats_base-1.0.8/ats_base.egg-info/PKG-INFO` & `ats_base-1.0.9/ats_base.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ats-base
-Version: 1.0.8
+Version: 1.0.9
 Summary: Test Script Development Library
 Home-page: https://gitee.com/henry9000/ats_base
 Author: zhangyue
 Author-email: zhangyue@techen.cn
 Project-URL: Bug Tracker, https://gitee.com/henry9000/ats_base/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `ats_base-1.0.8/ats_base.egg-info/SOURCES.txt` & `ats_base-1.0.9/ats_base.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -19,12 +19,11 @@
 ats_base/config/configure.py
 ats_base/config/rewrite_config.py
 ats_base/log/__init__.py
 ats_base/log/logger.py
 ats_base/service/__init__.py
 ats_base/service/app.py
 ats_base/service/db.py
-ats_base/service/dvs.py
 ats_base/service/em.py
 ats_base/service/mm.py
 ats_base/service/pro.py
 ats_base/service/udm.py
```

### Comparing `ats_base-1.0.8/setup.py` & `ats_base-1.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="ats_base",
-    version="1.0.8",
+    version="1.0.9",
     py_modules=['ats_base'],
     author="zhangyue",
     author_email="zhangyue@techen.cn",
     description="Test Script Development Library",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitee.com/henry9000/ats_base",
```

