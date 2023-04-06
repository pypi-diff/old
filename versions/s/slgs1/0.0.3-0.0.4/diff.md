# Comparing `tmp/slgs1-0.0.3.tar.gz` & `tmp/slgs1-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\slgs1-0.0.3.tar", last modified: Thu Apr  6 09:26:45 2023, max compression
+gzip compressed data, was "dist\slgs1-0.0.4.tar", last modified: Thu Apr  6 09:29:42 2023, max compression
```

## Comparing `slgs1-0.0.3.tar` & `slgs1-0.0.4.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 09:26:45.000000 slgs1-0.0.3/
--rw-rw-rw-   0        0        0     1237 2023-04-06 09:26:45.000000 slgs1-0.0.3/PKG-INFO
--rw-rw-rw-   0        0        0      910 2023-04-06 07:55:32.000000 slgs1-0.0.3/README.md
--rw-rw-rw-   0        0        0      585 2023-04-06 08:05:43.000000 slgs1-0.0.3/license.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 09:26:45.000000 slgs1-0.0.3/setup.cfg
--rw-rw-rw-   0        0        0      497 2023-04-06 09:25:47.000000 slgs1-0.0.3/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-06 09:26:45.000000 slgs1-0.0.3/slgs1/
--rw-rw-rw-   0        0        0       78 2023-04-06 09:15:26.000000 slgs1-0.0.3/slgs1/__init__.py
--rw-rw-rw-   0        0        0     4372 2023-04-06 07:55:32.000000 slgs1-0.0.3/slgs1/tweet_crawler.py
-drwxrwxrwx   0        0        0        0 2023-04-06 09:26:45.000000 slgs1-0.0.3/slgs1.egg-info/
--rw-rw-rw-   0        0        0     1237 2023-04-06 09:26:45.000000 slgs1-0.0.3/slgs1.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      187 2023-04-06 09:26:45.000000 slgs1-0.0.3/slgs1.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 09:26:45.000000 slgs1-0.0.3/slgs1.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        6 2023-04-06 09:26:45.000000 slgs1-0.0.3/slgs1.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 09:29:42.000000 slgs1-0.0.4/
+-rw-rw-rw-   0        0        0     1237 2023-04-06 09:29:42.000000 slgs1-0.0.4/PKG-INFO
+-rw-rw-rw-   0        0        0      910 2023-04-06 07:55:32.000000 slgs1-0.0.4/README.md
+-rw-rw-rw-   0        0        0      585 2023-04-06 08:05:43.000000 slgs1-0.0.4/license.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 09:29:42.000000 slgs1-0.0.4/setup.cfg
+-rw-rw-rw-   0        0        0      497 2023-04-06 09:28:43.000000 slgs1-0.0.4/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:29:42.000000 slgs1-0.0.4/slgs1/
+-rw-rw-rw-   0        0        0       78 2023-04-06 09:15:26.000000 slgs1-0.0.4/slgs1/__init__.py
+-rw-rw-rw-   0        0        0     4376 2023-04-06 09:28:20.000000 slgs1-0.0.4/slgs1/tweet_crawler.py
+drwxrwxrwx   0        0        0        0 2023-04-06 09:29:42.000000 slgs1-0.0.4/slgs1.egg-info/
+-rw-rw-rw-   0        0        0     1237 2023-04-06 09:29:42.000000 slgs1-0.0.4/slgs1.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      187 2023-04-06 09:29:42.000000 slgs1-0.0.4/slgs1.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 09:29:42.000000 slgs1-0.0.4/slgs1.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        6 2023-04-06 09:29:42.000000 slgs1-0.0.4/slgs1.egg-info/top_level.txt
```

### Comparing `slgs1-0.0.3/PKG-INFO` & `slgs1-0.0.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slgs1
-Version: 0.0.3
+Version: 0.0.4
 Home-page: https://gitee.com/li-muquan/slgs1
 Author: slgs
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 License-File: license.txt
```

### Comparing `slgs1-0.0.3/README.md` & `slgs1-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.3/license.txt` & `slgs1-0.0.4/license.txt`

 * *Files identical despite different names*

### Comparing `slgs1-0.0.3/slgs1/tweet_crawler.py` & `slgs1-0.0.4/slgs1/tweet_crawler.py`

 * *Files 2% similar despite different names*

```diff
@@ -100,9 +100,9 @@
     csv_path = '电子科大 top.csv'
     df_Sheet.to_csv(csv_path)
     print('Save - successfully!!!')
 
 def Run():
     Save_Data(UrlPath='C:/Users/99573/Desktop/tweet_1/script/twitter_url.txt')
 
-if __name__ == '__main__':
-    Run()
+# if __name__ == '__main__':
+#     Run()
```

### Comparing `slgs1-0.0.3/slgs1.egg-info/PKG-INFO` & `slgs1-0.0.4/slgs1.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: slgs1
-Version: 0.0.3
+Version: 0.0.4
 Home-page: https://gitee.com/li-muquan/slgs1
 Author: slgs
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 License-File: license.txt
```

