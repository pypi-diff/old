# Comparing `tmp/alibabacloud_btripopen20220520-1.0.8.tar.gz` & `tmp/alibabacloud_btripopen20220520-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/alibabacloud_btripopen20220520-1.0.8.tar", last modified: Fri Aug 26 02:30:38 2022, max compression
+gzip compressed data, was "dist/alibabacloud_btripopen20220520-1.0.9.tar", last modified: Fri Aug 26 07:37:22 2022, max compression
```

## Comparing `alibabacloud_btripopen20220520-1.0.8.tar` & `alibabacloud_btripopen20220520-1.0.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/
--rw-r--r--   0 root         (0) root         (0)      408 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/ChangeLog.md
--rw-r--r--   0 root         (0) root         (0)      600 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)       29 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2364 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1040 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/README-CN.md
--rw-r--r--   0 root         (0) root         (0)     1125 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520/
--rw-r--r--   0 root         (0) root         (0)       21 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520/__init__.py
--rw-r--r--   0 root         (0) root         (0)   242041 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520/client.py
--rw-r--r--   0 root         (0) root         (0)   730737 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2364 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      468 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      156 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       31 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       73 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2640 2022-08-26 02:30:38.000000 alibabacloud_btripopen20220520-1.0.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-08-26 07:37:22.000000 alibabacloud_btripopen20220520-1.0.9/
+-rw-r--r--   0 root         (0) root         (0)      459 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/ChangeLog.md
+-rw-r--r--   0 root         (0) root         (0)      600 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       29 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2364 2022-08-26 07:37:22.000000 alibabacloud_btripopen20220520-1.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1040 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/README-CN.md
+-rw-r--r--   0 root         (0) root         (0)     1125 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-08-26 07:37:22.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520/
+-rw-r--r--   0 root         (0) root         (0)       21 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   242041 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520/client.py
+-rw-r--r--   0 root         (0) root         (0)   730737 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-08-26 07:37:22.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2364 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      468 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      156 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       31 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       73 2022-08-26 07:37:22.000000 alibabacloud_btripopen20220520-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2640 2022-08-26 07:37:21.000000 alibabacloud_btripopen20220520-1.0.9/setup.py
```

### Comparing `alibabacloud_btripopen20220520-1.0.8/LICENSE` & `alibabacloud_btripopen20220520-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520-1.0.8/PKG-INFO` & `alibabacloud_btripopen20220520-1.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud_btripopen20220520
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud btripOpen (20220520) SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-python-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_btripopen20220520-1.0.8/README-CN.md` & `alibabacloud_btripopen20220520-1.0.9/README-CN.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520-1.0.8/README.md` & `alibabacloud_btripopen20220520-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520/client.py` & `alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520/models.py` & `alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520-1.0.8/alibabacloud_btripopen20220520.egg-info/PKG-INFO` & `alibabacloud_btripopen20220520-1.0.9/alibabacloud_btripopen20220520.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud-btripopen20220520
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud btripOpen (20220520) SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-python-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_btripopen20220520-1.0.8/setup.py` & `alibabacloud_btripopen20220520-1.0.9/setup.py`

 * *Files identical despite different names*

