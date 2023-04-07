# Comparing `tmp/FPC-0.8.tar.gz` & `tmp/FPC-0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\FPC-0.8.tar", last modified: Wed Oct 17 10:52:38 2018, max compression
+gzip compressed data, was "dist\FPC-0.9.tar", last modified: Mon Oct 22 06:50:32 2018, max compression
```

## Comparing `FPC-0.8.tar` & `FPC-0.9.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxrwx   0        0        0        0 2018-10-17 10:52:38.000000 FPC-0.8/
-drwxrwxrwx   0        0        0        0 2018-10-17 10:52:38.000000 FPC-0.8/FPC/
--rw-rw-rw-   0        0        0     3142 2018-10-17 10:52:18.000000 FPC-0.8/FPC/__init__.py
-drwxrwxrwx   0        0        0        0 2018-10-17 10:52:38.000000 FPC-0.8/FPC.egg-info/
--rw-rw-rw-   0        0        0        1 2018-10-17 10:52:38.000000 FPC-0.8/FPC.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      595 2018-10-17 10:52:38.000000 FPC-0.8/FPC.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      142 2018-10-17 10:52:38.000000 FPC-0.8/FPC.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        4 2018-10-17 10:52:38.000000 FPC-0.8/FPC.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      595 2018-10-17 10:52:38.000000 FPC-0.8/PKG-INFO
--rw-rw-rw-   0        0        0       66 2018-09-23 05:26:24.000000 FPC-0.8/README.md
--rw-rw-rw-   0        0        0       42 2018-10-17 10:52:38.000000 FPC-0.8/setup.cfg
--rw-rw-rw-   0        0        0      797 2018-10-17 10:52:30.000000 FPC-0.8/setup.py
+drwxrwxrwx   0        0        0        0 2018-10-22 06:50:32.000000 FPC-0.9/
+drwxrwxrwx   0        0        0        0 2018-10-22 06:50:32.000000 FPC-0.9/FPC/
+-rw-rw-rw-   0        0        0     3216 2018-10-22 06:46:47.000000 FPC-0.9/FPC/__init__.py
+drwxrwxrwx   0        0        0        0 2018-10-22 06:50:32.000000 FPC-0.9/FPC.egg-info/
+-rw-rw-rw-   0        0        0        1 2018-10-22 06:50:31.000000 FPC-0.9/FPC.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      595 2018-10-22 06:50:31.000000 FPC-0.9/FPC.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      142 2018-10-22 06:50:32.000000 FPC-0.9/FPC.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        4 2018-10-22 06:50:31.000000 FPC-0.9/FPC.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      595 2018-10-22 06:50:32.000000 FPC-0.9/PKG-INFO
+-rw-rw-rw-   0        0        0       66 2018-09-23 05:26:24.000000 FPC-0.9/README.md
+-rw-rw-rw-   0        0        0       42 2018-10-22 06:50:32.000000 FPC-0.9/setup.cfg
+-rw-rw-rw-   0        0        0      797 2018-10-22 06:50:21.000000 FPC-0.9/setup.py
```

### Comparing `FPC-0.8/FPC/__init__.py` & `FPC-0.9/FPC/__init__.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,11 +1,17 @@
 import datetime,builtins,platform,time,math
 from urllib import request
 IS_WIN=False if platform.system().find('Linux')>-1 else True
 NOW=math.floor(datetime.datetime.now().timestamp())
+def is_numeric(x):
+	try:
+		float(x)
+		return True
+	except:
+		return False
 def now():return math.floor(datetime.datetime.now().timestamp())
 def print(*a,func=None,time='%m/%d %H:%M:%S',**s):
 	a=list(a)
 	if func:
 		for i,x in enumerate(a):
 			a[i]=func(x)
 	if time:
```

### Comparing `FPC-0.8/FPC.egg-info/PKG-INFO` & `FPC-0.9/FPC.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: FPC
-Version: 0.8
+Version: 0.9
 Summary: Frank's Personal Conllection
 Home-page: http://ff2.pw
 Author: Frank
 Author-email: luoziluojun@126.com
 Maintainer: Frank
 Maintainer-email: luoziluojun@126.com
 License: BSD License
```

### Comparing `FPC-0.8/PKG-INFO` & `FPC-0.9/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: FPC
-Version: 0.8
+Version: 0.9
 Summary: Frank's Personal Conllection
 Home-page: http://ff2.pw
 Author: Frank
 Author-email: luoziluojun@126.com
 Maintainer: Frank
 Maintainer-email: luoziluojun@126.com
 License: BSD License
```

### Comparing `FPC-0.8/setup.py` & `FPC-0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # coding=utf-8
 
 from setuptools import setup
 import setuptools
 setup(
     name='FPC',
-    version='0.8',
+    version='0.9',
     description=(
         'Frank\'s Personal Conllection'
     ),
     long_description='Frank\'s Personal Conllection',
     author='Frank',
     author_email='luoziluojun@126.com',
     maintainer='Frank',
```

