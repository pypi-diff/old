# Comparing `tmp/alibabacloud_btripopen20220520_py2-1.0.8.tar.gz` & `tmp/alibabacloud_btripopen20220520_py2-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/alibabacloud_btripopen20220520_py2-1.0.8.tar", last modified: Thu Sep  1 08:05:56 2022, max compression
+gzip compressed data, was "dist/alibabacloud_btripopen20220520_py2-1.0.9.tar", last modified: Tue Sep  6 03:42:26 2022, max compression
```

## Comparing `alibabacloud_btripopen20220520_py2-1.0.8.tar` & `alibabacloud_btripopen20220520_py2-1.0.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/
--rw-r--r--   0 root         (0) root         (0)      378 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/ChangeLog.md
--rw-r--r--   0 root         (0) root         (0)      588 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)       28 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2508 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1051 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/README-CN.md
--rw-r--r--   0 root         (0) root         (0)     1134 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520/
--rw-r--r--   0 root         (0) root         (0)       21 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520/__init__.py
--rw-r--r--   0 root         (0) root         (0)   102966 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520/client.py
--rw-r--r--   0 root         (0) root         (0)   734601 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2508 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      488 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      172 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       31 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       73 2022-09-01 08:05:56.000000 alibabacloud_btripopen20220520_py2-1.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2933 2022-09-01 08:05:55.000000 alibabacloud_btripopen20220520_py2-1.0.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/
+-rw-r--r--   0 root         (0) root         (0)      421 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/ChangeLog.md
+-rw-r--r--   0 root         (0) root         (0)      588 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       28 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2508 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1051 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/README-CN.md
+-rw-r--r--   0 root         (0) root         (0)     1134 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520/
+-rw-r--r--   0 root         (0) root         (0)       21 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   102966 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520/client.py
+-rw-r--r--   0 root         (0) root         (0)   734601 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2508 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      488 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      172 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       31 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       73 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2933 2022-09-06 03:42:26.000000 alibabacloud_btripopen20220520_py2-1.0.9/setup.py
```

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/LICENSE` & `alibabacloud_btripopen20220520_py2-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/PKG-INFO` & `alibabacloud_btripopen20220520_py2-1.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud_btripopen20220520_py2
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud btripOpen (20220520) SDK Library for Python2
 Home-page: https://github.com/aliyun/alibabacloud-python2-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/README-CN.md` & `alibabacloud_btripopen20220520_py2-1.0.9/README-CN.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/README.md` & `alibabacloud_btripopen20220520_py2-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520/client.py` & `alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520/client.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520/models.py` & `alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520/models.py`

 * *Files identical despite different names*

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/alibabacloud_btripopen20220520_py2.egg-info/PKG-INFO` & `alibabacloud_btripopen20220520_py2-1.0.9/alibabacloud_btripopen20220520_py2.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud-btripopen20220520-py2
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud btripOpen (20220520) SDK Library for Python2
 Home-page: https://github.com/aliyun/alibabacloud-python2-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_btripopen20220520_py2-1.0.8/setup.py` & `alibabacloud_btripopen20220520_py2-1.0.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 import os
 import sys
 from setuptools import setup, find_packages
 
 """
 setup module for alibabacloud_btripopen20220520_py2.
 
-Created on 01/09/2022
+Created on 06/09/2022
 
 @author: Alibaba Cloud SDK
 """
 
 PACKAGE = "alibabacloud_btripopen20220520"
 NAME = "alibabacloud_btripopen20220520_py2" or "alibabacloud-package"
 DESCRIPTION = "Alibaba Cloud btripOpen (20220520) SDK Library for Python2"
```

