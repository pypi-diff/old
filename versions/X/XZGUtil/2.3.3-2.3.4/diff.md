# Comparing `tmp/XZGUtil-2.3.3.tar.gz` & `tmp/XZGUtil-2.3.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\XZGUtil-2.3.3.tar", last modified: Fri Apr  7 01:50:34 2023, max compression
+gzip compressed data, was "dist\XZGUtil-2.3.4.tar", last modified: Fri Apr  7 01:55:59 2023, max compression
```

## Comparing `XZGUtil-2.3.3.tar` & `XZGUtil-2.3.4.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 01:50:34.000000 XZGUtil-2.3.3/
--rw-rw-rw-   0        0        0      608 2023-04-07 01:50:34.000000 XZGUtil-2.3.3/PKG-INFO
--rw-rw-rw-   0        0        0       42 2021-05-31 01:49:13.000000 XZGUtil-2.3.3/README.rst
-drwxrwxrwx   0        0        0        0 2023-04-07 01:50:34.000000 XZGUtil-2.3.3/XZGUtil/
--rw-rw-rw-   0        0        0    77396 2023-03-20 09:02:08.000000 XZGUtil-2.3.3/XZGUtil/DBHelper.py
--rw-rw-rw-   0        0        0     1612 2023-02-15 10:08:17.000000 XZGUtil-2.3.3/XZGUtil/SYCMCryptUtil.py
--rw-rw-rw-   0        0        0      704 2023-03-10 08:44:13.000000 XZGUtil-2.3.3/XZGUtil/__init__.py
--rw-rw-rw-   0        0        0     4214 2023-02-15 07:41:00.000000 XZGUtil-2.3.3/XZGUtil/dealFile.py
--rw-rw-rw-   0        0        0     4893 2022-11-10 03:22:03.000000 XZGUtil-2.3.3/XZGUtil/downFile.py
--rw-rw-rw-   0        0        0   513760 2023-04-04 03:01:05.000000 XZGUtil-2.3.3/XZGUtil/dyXB.py
--rw-rw-rw-   0        0        0    37619 2022-09-21 03:07:37.000000 XZGUtil-2.3.3/XZGUtil/encAndDec.py
--rw-rw-rw-   0        0        0     2469 2022-01-12 08:39:02.000000 XZGUtil-2.3.3/XZGUtil/logger.py
--rw-rw-rw-   0        0        0     1439 2022-11-25 10:54:18.000000 XZGUtil-2.3.3/XZGUtil/messageUtil.py
--rw-rw-rw-   0        0        0     3579 2023-02-14 09:09:37.000000 XZGUtil-2.3.3/XZGUtil/raspberryScan.py
--rw-rw-rw-   0        0        0     1181 2021-06-02 10:25:57.000000 XZGUtil-2.3.3/XZGUtil/re_xzg.py
--rw-rw-rw-   0        0        0    14033 2022-11-25 10:50:05.000000 XZGUtil-2.3.3/XZGUtil/timeUtil.py
--rw-rw-rw-   0        0        0      858 2023-03-10 09:00:37.000000 XZGUtil-2.3.3/XZGUtil/timer.py
--rw-rw-rw-   0        0        0     3352 2023-04-07 01:50:07.000000 XZGUtil-2.3.3/XZGUtil/updateSpider.py
-drwxrwxrwx   0        0        0        0 2023-04-07 01:50:34.000000 XZGUtil-2.3.3/XZGUtil.egg-info/
--rw-rw-rw-   0        0        0      608 2023-04-07 01:50:33.000000 XZGUtil-2.3.3/XZGUtil.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      460 2023-04-07 01:50:33.000000 XZGUtil-2.3.3/XZGUtil.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 01:50:33.000000 XZGUtil-2.3.3/XZGUtil.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       34 2023-04-07 01:50:33.000000 XZGUtil-2.3.3/XZGUtil.egg-info/requires.txt
--rw-rw-rw-   0        0        0        8 2023-04-07 01:50:33.000000 XZGUtil-2.3.3/XZGUtil.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 01:50:34.000000 XZGUtil-2.3.3/setup.cfg
--rw-rw-rw-   0        0        0     1109 2023-04-07 01:50:27.000000 XZGUtil-2.3.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/
+-rw-rw-rw-   0        0        0      608 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/PKG-INFO
+-rw-rw-rw-   0        0        0       42 2021-05-31 01:49:13.000000 XZGUtil-2.3.4/README.rst
+drwxrwxrwx   0        0        0        0 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil/
+-rw-rw-rw-   0        0        0    77396 2023-03-20 09:02:08.000000 XZGUtil-2.3.4/XZGUtil/DBHelper.py
+-rw-rw-rw-   0        0        0     1612 2023-02-15 10:08:17.000000 XZGUtil-2.3.4/XZGUtil/SYCMCryptUtil.py
+-rw-rw-rw-   0        0        0      704 2023-03-10 08:44:13.000000 XZGUtil-2.3.4/XZGUtil/__init__.py
+-rw-rw-rw-   0        0        0     4214 2023-02-15 07:41:00.000000 XZGUtil-2.3.4/XZGUtil/dealFile.py
+-rw-rw-rw-   0        0        0     4893 2022-11-10 03:22:03.000000 XZGUtil-2.3.4/XZGUtil/downFile.py
+-rw-rw-rw-   0        0        0   513760 2023-04-04 03:01:05.000000 XZGUtil-2.3.4/XZGUtil/dyXB.py
+-rw-rw-rw-   0        0        0    37619 2022-09-21 03:07:37.000000 XZGUtil-2.3.4/XZGUtil/encAndDec.py
+-rw-rw-rw-   0        0        0     2469 2022-01-12 08:39:02.000000 XZGUtil-2.3.4/XZGUtil/logger.py
+-rw-rw-rw-   0        0        0     1439 2022-11-25 10:54:18.000000 XZGUtil-2.3.4/XZGUtil/messageUtil.py
+-rw-rw-rw-   0        0        0     3579 2023-02-14 09:09:37.000000 XZGUtil-2.3.4/XZGUtil/raspberryScan.py
+-rw-rw-rw-   0        0        0     1181 2021-06-02 10:25:57.000000 XZGUtil-2.3.4/XZGUtil/re_xzg.py
+-rw-rw-rw-   0        0        0    14033 2022-11-25 10:50:05.000000 XZGUtil-2.3.4/XZGUtil/timeUtil.py
+-rw-rw-rw-   0        0        0      858 2023-03-10 09:00:37.000000 XZGUtil-2.3.4/XZGUtil/timer.py
+-rw-rw-rw-   0        0        0     3394 2023-04-07 01:53:41.000000 XZGUtil-2.3.4/XZGUtil/updateSpider.py
+drwxrwxrwx   0        0        0        0 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil.egg-info/
+-rw-rw-rw-   0        0        0      608 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      460 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       34 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        8 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/XZGUtil.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 01:55:59.000000 XZGUtil-2.3.4/setup.cfg
+-rw-rw-rw-   0        0        0     1109 2023-04-07 01:55:45.000000 XZGUtil-2.3.4/setup.py
```

### Comparing `XZGUtil-2.3.3/PKG-INFO` & `XZGUtil-2.3.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: XZGUtil
-Version: 2.3.3
+Version: 2.3.4
 Summary: xzgutil
 Home-page: UNKNOWN
 Author: xu-zhiguo
 Author-email: x_zg163@163.com
 License: BSD License
 Description: xzgutil
 Platform: all
```

### Comparing `XZGUtil-2.3.3/XZGUtil/DBHelper.py` & `XZGUtil-2.3.4/XZGUtil/DBHelper.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/SYCMCryptUtil.py` & `XZGUtil-2.3.4/XZGUtil/SYCMCryptUtil.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/__init__.py` & `XZGUtil-2.3.4/XZGUtil/__init__.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/dealFile.py` & `XZGUtil-2.3.4/XZGUtil/dealFile.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/downFile.py` & `XZGUtil-2.3.4/XZGUtil/downFile.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/dyXB.py` & `XZGUtil-2.3.4/XZGUtil/dyXB.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/encAndDec.py` & `XZGUtil-2.3.4/XZGUtil/encAndDec.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/logger.py` & `XZGUtil-2.3.4/XZGUtil/logger.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/messageUtil.py` & `XZGUtil-2.3.4/XZGUtil/messageUtil.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/raspberryScan.py` & `XZGUtil-2.3.4/XZGUtil/raspberryScan.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/re_xzg.py` & `XZGUtil-2.3.4/XZGUtil/re_xzg.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/timeUtil.py` & `XZGUtil-2.3.4/XZGUtil/timeUtil.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/timer.py` & `XZGUtil-2.3.4/XZGUtil/timer.py`

 * *Files identical despite different names*

### Comparing `XZGUtil-2.3.3/XZGUtil/updateSpider.py` & `XZGUtil-2.3.4/XZGUtil/updateSpider.py`

 * *Files 3% similar despite different names*

```diff
@@ -30,15 +30,15 @@
     def get_information(self, name):
         """
         获取更新日期
         :param name:
         :return:
         """
         try:
-            with open('new_config.ini') as f:
+            with open(self.updatePath, encoding="utf-8-sig") as f:
                 self.config.read_file(f)
             data = self.config.get(self.update_tag, f'{name}')
         except:
             data = None
         return data
 
     def set_information(self, name, date=get_now_date()):
@@ -61,15 +61,15 @@
         """
         检查今日是否更新
         :param name: 检查对象
         :param difference: 时间对比基准点，默认为0（今日），如果为 difference=1 则代表：如果上次更新日期是前一天，则返回False，代表更新完成，不需要更新
         :return:
         """
         try:
-            with open('new_config.ini') as f:
+            with open(self.updatePath, encoding="utf-8-sig") as f:
                 self.config.read_file(f)
             value = self.config.get(self.update_tag, f'{name}')
         except:
             try:
                 self.config.set(self.update_tag, f'{name}', getdate(1))  # 如果报错说明没有这个则需要创建一个，并赋值为前一日
             except configparser.NoSectionError:
                 with open(self.updatePath, 'a') as f:
```

### Comparing `XZGUtil-2.3.3/XZGUtil.egg-info/PKG-INFO` & `XZGUtil-2.3.4/XZGUtil.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: XZGUtil
-Version: 2.3.3
+Version: 2.3.4
 Summary: xzgutil
 Home-page: UNKNOWN
 Author: xu-zhiguo
 Author-email: x_zg163@163.com
 License: BSD License
 Description: xzgutil
 Platform: all
```

### Comparing `XZGUtil-2.3.3/setup.py` & `XZGUtil-2.3.4/setup.py`

 * *Files 11% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 from distutils.core import setup
 from setuptools import find_packages
 
 with open("README.rst", "r") as f:
   long_description = f.read()
 
 setup(name='XZGUtil',  # 包名
-      version='2.3.3',  # 版本号
+      version='2.3.4',  # 版本号
       description='xzgutil',
       long_description='xzgutil',
       author='xu-zhiguo',
       author_email='x_zg163@163.com',
       url='',
       install_requires=['postcard', 'retrying', 'python-dateutil'],
       license='BSD License',
```

