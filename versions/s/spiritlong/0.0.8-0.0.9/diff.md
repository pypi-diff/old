# Comparing `tmp/spiritlong-0.0.8.tar.gz` & `tmp/spiritlong-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "spiritlong-0.0.8.tar", last modified: Sat Mar 25 15:46:37 2023, max compression
+gzip compressed data, was "spiritlong-0.0.9.tar", last modified: Fri Mar 31 05:44:36 2023, max compression
```

## Comparing `spiritlong-0.0.8.tar` & `spiritlong-0.0.9.tar`

### file list

```diff
@@ -1,17 +1,20 @@
-drwxrwxrwx   0        0        0        0 2023-03-25 15:46:37.516283 spiritlong-0.0.8/
--rw-rw-rw-   0        0        0     1449 2023-03-19 05:09:42.000000 spiritlong-0.0.8/LICENSE.txt
--rw-rw-rw-   0        0        0      747 2023-03-25 15:46:37.516283 spiritlong-0.0.8/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-03-25 15:46:37.488761 spiritlong-0.0.8/database/
--rw-rw-rw-   0        0        0       33 2023-03-19 05:09:42.000000 spiritlong-0.0.8/database/__init__.py
--rw-rw-rw-   0        0        0    48181 2023-03-20 11:30:13.000000 spiritlong-0.0.8/database/database.py
-drwxrwxrwx   0        0        0        0 2023-03-25 15:46:37.495283 spiritlong-0.0.8/excel_tool/
--rw-rw-rw-   0        0        0       35 2023-03-19 05:09:42.000000 spiritlong-0.0.8/excel_tool/__init__.py
--rw-rw-rw-   0        0        0     5052 2023-03-25 15:46:07.000000 spiritlong-0.0.8/excel_tool/excel_tool.py
--rw-rw-rw-   0        0        0       42 2023-03-25 15:46:37.516283 spiritlong-0.0.8/setup.cfg
--rw-rw-rw-   0        0        0     1302 2023-03-19 05:09:42.000000 spiritlong-0.0.8/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-25 15:46:37.514282 spiritlong-0.0.8/spiritlong.egg-info/
--rw-rw-rw-   0        0        0      747 2023-03-25 15:46:37.000000 spiritlong-0.0.8/spiritlong.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      279 2023-03-25 15:46:37.000000 spiritlong-0.0.8/spiritlong.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-25 15:46:37.000000 spiritlong-0.0.8/spiritlong.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       38 2023-03-25 15:46:37.000000 spiritlong-0.0.8/spiritlong.egg-info/requires.txt
--rw-rw-rw-   0        0        0       20 2023-03-25 15:46:37.000000 spiritlong-0.0.8/spiritlong.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-31 05:44:36.329077 spiritlong-0.0.9/
+-rw-rw-rw-   0        0        0     1449 2023-03-28 01:19:41.000000 spiritlong-0.0.9/LICENSE.txt
+-rw-rw-rw-   0        0        0      747 2023-03-31 05:44:36.328080 spiritlong-0.0.9/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-03-31 05:44:36.299178 spiritlong-0.0.9/database/
+-rw-rw-rw-   0        0        0       33 2023-03-28 01:19:41.000000 spiritlong-0.0.9/database/__init__.py
+-rw-rw-rw-   0        0        0    48181 2023-03-28 01:19:41.000000 spiritlong-0.0.9/database/database.py
+drwxrwxrwx   0        0        0        0 2023-03-31 05:44:36.302167 spiritlong-0.0.9/excel_tool/
+-rw-rw-rw-   0        0        0       35 2023-03-28 01:19:41.000000 spiritlong-0.0.9/excel_tool/__init__.py
+-rw-rw-rw-   0        0        0     5052 2023-03-28 01:19:41.000000 spiritlong-0.0.9/excel_tool/excel_tool.py
+-rw-rw-rw-   0        0        0       42 2023-03-31 05:44:36.329077 spiritlong-0.0.9/setup.cfg
+-rw-rw-rw-   0        0        0     1302 2023-03-28 01:19:41.000000 spiritlong-0.0.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-31 05:44:36.321103 spiritlong-0.0.9/spiritlong.egg-info/
+-rw-rw-rw-   0        0        0      747 2023-03-31 05:44:36.000000 spiritlong-0.0.9/spiritlong.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      336 2023-03-31 05:44:36.000000 spiritlong-0.0.9/spiritlong.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-31 05:44:36.000000 spiritlong-0.0.9/spiritlong.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       38 2023-03-31 05:44:36.000000 spiritlong-0.0.9/spiritlong.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       34 2023-03-31 05:44:36.000000 spiritlong-0.0.9/spiritlong.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-31 05:44:36.327084 spiritlong-0.0.9/webframe_tool/
+-rw-rw-rw-   0        0        0       41 2023-03-31 03:35:24.000000 spiritlong-0.0.9/webframe_tool/__init__.py
+-rw-rw-rw-   0        0        0     3351 2023-03-31 05:42:53.000000 spiritlong-0.0.9/webframe_tool/webframe_tool.py
```

### Comparing `spiritlong-0.0.8/LICENSE.txt` & `spiritlong-0.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `spiritlong-0.0.8/PKG-INFO` & `spiritlong-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spiritlong
-Version: 0.0.8
+Version: 0.0.9
 Summary: SpiritLong python package from pip
 Home-page: https://spiritlong-exon.com/pip
 Author: SpiritLong
 Author-email: arthuryang@spiritlong.com
 Maintainer: SpiritLong
 Maintainer-email: shun@spiritlong.com
 Classifier: Development Status :: 3 - Alpha
@@ -14,13 +14,13 @@
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 Copyright (c) 2023 Chongqing Spiritlong Technology Co., Ltd.
 All rights reserved.
 
-version	0.0.8
+version	0.0.9
 
 brief	SpiritLong python package from pip
 
 重庆灵悠科技有限公司专用工具包
```

### Comparing `spiritlong-0.0.8/database/database.py` & `spiritlong-0.0.9/database/database.py`

 * *Files identical despite different names*

### Comparing `spiritlong-0.0.8/excel_tool/excel_tool.py` & `spiritlong-0.0.9/excel_tool/excel_tool.py`

 * *Files identical despite different names*

### Comparing `spiritlong-0.0.8/setup.py` & `spiritlong-0.0.9/setup.py`

 * *Files identical despite different names*

### Comparing `spiritlong-0.0.8/spiritlong.egg-info/PKG-INFO` & `spiritlong-0.0.9/spiritlong.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spiritlong
-Version: 0.0.8
+Version: 0.0.9
 Summary: SpiritLong python package from pip
 Home-page: https://spiritlong-exon.com/pip
 Author: SpiritLong
 Author-email: arthuryang@spiritlong.com
 Maintainer: SpiritLong
 Maintainer-email: shun@spiritlong.com
 Classifier: Development Status :: 3 - Alpha
@@ -14,13 +14,13 @@
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 Copyright (c) 2023 Chongqing Spiritlong Technology Co., Ltd.
 All rights reserved.
 
-version	0.0.8
+version	0.0.9
 
 brief	SpiritLong python package from pip
 
 重庆灵悠科技有限公司专用工具包
```

