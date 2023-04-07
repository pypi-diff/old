# Comparing `tmp/XZGUtil-2.3.0.tar.gz` & `tmp/XZGUtil-2.3.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\XZGUtil-2.3.0.tar", last modified: Mon Mar 20 09:02:48 2023, max compression
+gzip compressed data, was "dist\XZGUtil-2.3.1.tar", last modified: Fri Apr  7 01:39:16 2023, max compression
```

## Comparing `XZGUtil-2.3.0.tar` & `XZGUtil-2.3.1.tar`

### file list

```diff
@@ -1,25 +1,26 @@
-drwxrwxrwx   0        0        0        0 2023-03-20 09:02:48.000000 XZGUtil-2.3.0/
--rw-rw-rw-   0        0        0      608 2023-03-20 09:02:48.000000 XZGUtil-2.3.0/PKG-INFO
--rw-rw-rw-   0        0        0       42 2021-05-31 01:49:13.000000 XZGUtil-2.3.0/README.rst
-drwxrwxrwx   0        0        0        0 2023-03-20 09:02:48.000000 XZGUtil-2.3.0/XZGUtil/
--rw-rw-rw-   0        0        0    77396 2023-03-20 09:02:08.000000 XZGUtil-2.3.0/XZGUtil/DBHelper.py
--rw-rw-rw-   0        0        0     1612 2023-02-15 10:08:17.000000 XZGUtil-2.3.0/XZGUtil/SYCMCryptUtil.py
--rw-rw-rw-   0        0        0      704 2023-03-10 08:44:13.000000 XZGUtil-2.3.0/XZGUtil/__init__.py
--rw-rw-rw-   0        0        0     4214 2023-02-15 07:41:00.000000 XZGUtil-2.3.0/XZGUtil/dealFile.py
--rw-rw-rw-   0        0        0     4893 2022-11-10 03:22:03.000000 XZGUtil-2.3.0/XZGUtil/downFile.py
--rw-rw-rw-   0        0        0    37619 2022-09-21 03:07:37.000000 XZGUtil-2.3.0/XZGUtil/encAndDec.py
--rw-rw-rw-   0        0        0     2469 2022-01-12 08:39:02.000000 XZGUtil-2.3.0/XZGUtil/logger.py
--rw-rw-rw-   0        0        0     1439 2022-11-25 10:54:18.000000 XZGUtil-2.3.0/XZGUtil/messageUtil.py
--rw-rw-rw-   0        0        0     3579 2023-02-14 09:09:37.000000 XZGUtil-2.3.0/XZGUtil/raspberryScan.py
--rw-rw-rw-   0        0        0     1181 2021-06-02 10:25:57.000000 XZGUtil-2.3.0/XZGUtil/re_xzg.py
--rw-rw-rw-   0        0        0    14033 2022-11-25 10:50:05.000000 XZGUtil-2.3.0/XZGUtil/timeUtil.py
--rw-rw-rw-   0        0        0      858 2023-03-10 09:00:37.000000 XZGUtil-2.3.0/XZGUtil/timer.py
--rw-rw-rw-   0        0        0     3140 2022-11-08 10:27:46.000000 XZGUtil-2.3.0/XZGUtil/updateSpider.py
-drwxrwxrwx   0        0        0        0 2023-03-20 09:02:48.000000 XZGUtil-2.3.0/XZGUtil.egg-info/
--rw-rw-rw-   0        0        0      608 2023-03-20 09:02:47.000000 XZGUtil-2.3.0/XZGUtil.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      444 2023-03-20 09:02:47.000000 XZGUtil-2.3.0/XZGUtil.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-20 09:02:47.000000 XZGUtil-2.3.0/XZGUtil.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       34 2023-03-20 09:02:47.000000 XZGUtil-2.3.0/XZGUtil.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2023-03-20 09:02:47.000000 XZGUtil-2.3.0/XZGUtil.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-03-20 09:02:48.000000 XZGUtil-2.3.0/setup.cfg
--rw-rw-rw-   0        0        0     1109 2023-03-20 09:02:44.000000 XZGUtil-2.3.0/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:39:16.000000 XZGUtil-2.3.1/
+-rw-rw-rw-   0        0        0      608 2023-04-07 01:39:16.000000 XZGUtil-2.3.1/PKG-INFO
+-rw-rw-rw-   0        0        0       42 2021-05-31 01:49:13.000000 XZGUtil-2.3.1/README.rst
+drwxrwxrwx   0        0        0        0 2023-04-07 01:39:16.000000 XZGUtil-2.3.1/XZGUtil/
+-rw-rw-rw-   0        0        0    77396 2023-03-20 09:02:08.000000 XZGUtil-2.3.1/XZGUtil/DBHelper.py
+-rw-rw-rw-   0        0        0     1612 2023-02-15 10:08:17.000000 XZGUtil-2.3.1/XZGUtil/SYCMCryptUtil.py
+-rw-rw-rw-   0        0        0      704 2023-03-10 08:44:13.000000 XZGUtil-2.3.1/XZGUtil/__init__.py
+-rw-rw-rw-   0        0        0     4214 2023-02-15 07:41:00.000000 XZGUtil-2.3.1/XZGUtil/dealFile.py
+-rw-rw-rw-   0        0        0     4893 2022-11-10 03:22:03.000000 XZGUtil-2.3.1/XZGUtil/downFile.py
+-rw-rw-rw-   0        0        0   513760 2023-04-04 03:01:05.000000 XZGUtil-2.3.1/XZGUtil/dyXB.py
+-rw-rw-rw-   0        0        0    37619 2022-09-21 03:07:37.000000 XZGUtil-2.3.1/XZGUtil/encAndDec.py
+-rw-rw-rw-   0        0        0     2469 2022-01-12 08:39:02.000000 XZGUtil-2.3.1/XZGUtil/logger.py
+-rw-rw-rw-   0        0        0     1439 2022-11-25 10:54:18.000000 XZGUtil-2.3.1/XZGUtil/messageUtil.py
+-rw-rw-rw-   0        0        0     3579 2023-02-14 09:09:37.000000 XZGUtil-2.3.1/XZGUtil/raspberryScan.py
+-rw-rw-rw-   0        0        0     1181 2021-06-02 10:25:57.000000 XZGUtil-2.3.1/XZGUtil/re_xzg.py
+-rw-rw-rw-   0        0        0    14033 2022-11-25 10:50:05.000000 XZGUtil-2.3.1/XZGUtil/timeUtil.py
+-rw-rw-rw-   0        0        0      858 2023-03-10 09:00:37.000000 XZGUtil-2.3.1/XZGUtil/timer.py
+-rw-rw-rw-   0        0        0     3172 2023-04-07 01:38:48.000000 XZGUtil-2.3.1/XZGUtil/updateSpider.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:39:16.000000 XZGUtil-2.3.1/XZGUtil.egg-info/
+-rw-rw-rw-   0        0        0      608 2023-04-07 01:39:15.000000 XZGUtil-2.3.1/XZGUtil.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      460 2023-04-07 01:39:15.000000 XZGUtil-2.3.1/XZGUtil.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 01:39:15.000000 XZGUtil-2.3.1/XZGUtil.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       34 2023-04-07 01:39:15.000000 XZGUtil-2.3.1/XZGUtil.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-04-07 01:39:15.000000 XZGUtil-2.3.1/XZGUtil.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 01:39:16.000000 XZGUtil-2.3.1/setup.cfg
+-rw-rw-rw-   0        0        0     1109 2023-04-07 01:29:22.000000 XZGUtil-2.3.1/setup.py
```

### Comparing `XZGUtil-2.3.0/PKG-INFO` & `XZGUtil-2.3.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: XZGUtil
-Version: 2.3.0
+Version: 2.3.1
 Summary: xzgutil
 Home-page: UNKNOWN
 Author: xu-zhiguo
 Author-email: x_zg163@163.com
 License: BSD License
 Description: xzgutil
 Platform: all
```

### Comparing `XZGUtil-2.3.0/XZGUtil/DBHelper.py` & `XZGUtil-2.3.1/XZGUtil/DBHelper.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/SYCMCryptUtil.py` & `XZGUtil-2.3.1/XZGUtil/SYCMCryptUtil.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/__init__.py` & `XZGUtil-2.3.1/XZGUtil/__init__.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/dealFile.py` & `XZGUtil-2.3.1/XZGUtil/dealFile.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/downFile.py` & `XZGUtil-2.3.1/XZGUtil/downFile.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/encAndDec.py` & `XZGUtil-2.3.1/XZGUtil/encAndDec.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/logger.py` & `XZGUtil-2.3.1/XZGUtil/logger.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/messageUtil.py` & `XZGUtil-2.3.1/XZGUtil/messageUtil.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/raspberryScan.py` & `XZGUtil-2.3.1/XZGUtil/raspberryScan.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/re_xzg.py` & `XZGUtil-2.3.1/XZGUtil/re_xzg.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/timeUtil.py` & `XZGUtil-2.3.1/XZGUtil/timeUtil.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/timer.py` & `XZGUtil-2.3.1/XZGUtil/timer.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.0/XZGUtil/updateSpider.py` & `XZGUtil-2.3.1/XZGUtil/updateSpider.py`

 * *Files 4% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 # @File    : updateSpider.py
 # @Software: PyCharm
 """
 爬虫更新时间记录
 """
 import datetime
 import os
-import configparser  # 这个用于读取文件，写入文件会将中文注释删除
+from backports import configparser2 as configparser  # 这个用于读取文件，写入文件会将中文注释删除
 from XZGUtil.logger import conlog
 from XZGUtil.timeUtil import get_now_date, getdate
 
 proDir = os.path.split(os.path.realpath(__file__))[0]
 
 
 class upconfig(object):
```

### Comparing `XZGUtil-2.3.0/XZGUtil.egg-info/PKG-INFO` & `XZGUtil-2.3.1/XZGUtil.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: XZGUtil
-Version: 2.3.0
+Version: 2.3.1
 Summary: xzgutil
 Home-page: UNKNOWN
 Author: xu-zhiguo
 Author-email: x_zg163@163.com
 License: BSD License
 Description: xzgutil
 Platform: all
```

### Comparing `XZGUtil-2.3.0/setup.py` & `XZGUtil-2.3.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from distutils.core import setup
 from setuptools import find_packages
 
 with open("README.rst", "r") as f:
   long_description = f.read()
 
 setup(name='XZGUtil',  # 包名
-      version='2.3.0',  # 版本号
+      version='2.3.1',  # 版本号
       description='xzgutil',
       long_description='xzgutil',
       author='xu-zhiguo',
       author_email='x_zg163@163.com',
       url='',
       install_requires=['postcard', 'retrying', 'python-dateutil'],
       license='BSD License',
```

