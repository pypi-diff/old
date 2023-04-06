# Comparing `tmp/slgs1-0.0.6.tar.gz` & `tmp/slgs1-0.0.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\slgs1-0.0.6.tar", last modified: Thu Apr  6 10:12:42 2023, max compression
+gzip compressed data, was "dist\slgs1-0.0.7.tar", last modified: Thu Apr  6 10:28:20 2023, max compression
```

## Comparing `slgs1-0.0.6.tar` & `slgs1-0.0.7.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 10:12:42.000000 slgs1-0.0.6/
--rw-rw-rw-   0        0        0     1237 2023-04-06 10:12:42.000000 slgs1-0.0.6/PKG-INFO
--rw-rw-rw-   0        0        0      910 2023-04-06 07:55:32.000000 slgs1-0.0.6/README.md
--rw-rw-rw-   0        0        0      585 2023-04-06 08:05:43.000000 slgs1-0.0.6/license.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 10:12:42.000000 slgs1-0.0.6/setup.cfg
--rw-rw-rw-   0        0        0      497 2023-04-06 10:12:21.000000 slgs1-0.0.6/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 10:12:42.000000 slgs1-0.0.6/slgs1/
--rw-rw-rw-   0        0        0       78 2023-04-06 09:15:26.000000 slgs1-0.0.6/slgs1/__init__.py
--rw-rw-rw-   0        0        0     4332 2023-04-06 10:12:07.000000 slgs1-0.0.6/slgs1/tweet_crawler.py
-drwxrwxrwx   0        0        0        0 2023-04-06 10:12:42.000000 slgs1-0.0.6/slgs1.egg-info/
--rw-rw-rw-   0        0        0     1237 2023-04-06 10:12:42.000000 slgs1-0.0.6/slgs1.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      187 2023-04-06 10:12:42.000000 slgs1-0.0.6/slgs1.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 10:12:42.000000 slgs1-0.0.6/slgs1.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-06 10:12:42.000000 slgs1-0.0.6/slgs1.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 10:28:20.000000 slgs1-0.0.7/
+-rw-rw-rw-   0        0        0     1237 2023-04-06 10:28:20.000000 slgs1-0.0.7/PKG-INFO
+-rw-rw-rw-   0        0        0      910 2023-04-06 07:55:32.000000 slgs1-0.0.7/README.md
+-rw-rw-rw-   0        0        0      585 2023-04-06 08:05:43.000000 slgs1-0.0.7/license.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:28:20.000000 slgs1-0.0.7/setup.cfg
+-rw-rw-rw-   0        0        0      497 2023-04-06 10:27:39.000000 slgs1-0.0.7/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:28:20.000000 slgs1-0.0.7/slgs1/
+-rw-rw-rw-   0        0        0       78 2023-04-06 09:15:26.000000 slgs1-0.0.7/slgs1/__init__.py
+-rw-rw-rw-   0        0        0     4286 2023-04-06 10:26:51.000000 slgs1-0.0.7/slgs1/tweet_crawler.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:28:20.000000 slgs1-0.0.7/slgs1.egg-info/
+-rw-rw-rw-   0        0        0     1237 2023-04-06 10:28:20.000000 slgs1-0.0.7/slgs1.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      187 2023-04-06 10:28:20.000000 slgs1-0.0.7/slgs1.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:28:20.000000 slgs1-0.0.7/slgs1.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-06 10:28:20.000000 slgs1-0.0.7/slgs1.egg-info/top_level.txt
```

### Comparing `slgs1-0.0.6/PKG-INFO` & `slgs1-0.0.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slgs1
-Version: 0.0.6
+Version: 0.0.7
 Home-page: https://gitee.com/li-muquan/slgs1
 Author: slgs
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 License-File: license.txt
```

### Comparing `slgs1-0.0.6/README.md` & `slgs1-0.0.7/README.md`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.6/license.txt` & `slgs1-0.0.7/license.txt`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.6/slgs1/tweet_crawler.py` & `slgs1-0.0.7/slgs1/tweet_crawler.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,16 +4,14 @@
 from selenium import webdriver
 from bs4 import BeautifulSoup
 import os
 
 driver = webdriver.Chrome('chromedriver')
 driver.implicitly_wait(10)
 
-UrlPath=()
-
 def connent_url(UrlPath):
     Data_List = []
     print(os.getcwd())
     df = pd.read_csv(UrlPath)
 
     i = 1
     for url in df:
@@ -99,12 +97,10 @@
     TIMEFORMAT = '%Y-%m-%d %H:%M:%S'
     now = datetime.datetime.now().strftime(TIMEFORMAT)
     # ----------------------- csv name -----------------------
     csv_path = '电子科大 top.csv'
     df_Sheet.to_csv(csv_path)
     print('Save - successfully!!!')
 
-def Run():
+def Run(UrlPath):
     Save_Data(UrlPath)
 
-# if __name__ == '__main__':
-#     Run()
```

### Comparing `slgs1-0.0.6/slgs1.egg-info/PKG-INFO` & `slgs1-0.0.7/slgs1.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slgs1
-Version: 0.0.6
+Version: 0.0.7
 Home-page: https://gitee.com/li-muquan/slgs1
 Author: slgs
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 License-File: license.txt
```

