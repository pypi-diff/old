# Comparing `tmp/longitudinal_trends-0.0.4.tar.gz` & `tmp/longitudinal_trends-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "longitudinal_trends-0.0.4.tar", last modified: Wed Apr  5 19:45:59 2023, max compression
+gzip compressed data, was "longitudinal_trends-0.0.5.tar", last modified: Fri Apr  7 07:05:09 2023, max compression
```

## Comparing `longitudinal_trends-0.0.4.tar` & `longitudinal_trends-0.0.5.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0 msakir    (1000) msakir    (1000)        0 2023-04-05 19:45:59.001477 longitudinal_trends-0.0.4/
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)     1104 2023-03-18 15:04:53.000000 longitudinal_trends-0.0.4/LICENSE
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)       34 2023-03-18 16:38:44.000000 longitudinal_trends-0.0.4/MANIFEST.in
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)     9294 2023-04-05 19:45:58.987943 longitudinal_trends-0.0.4/PKG-INFO
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)     8759 2023-04-05 18:58:05.000000 longitudinal_trends-0.0.4/README.md
-drwxrwxrwx   0 msakir    (1000) msakir    (1000)        0 2023-04-05 19:45:58.651531 longitudinal_trends-0.0.4/longitudinal_trends/
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)    17278 2023-04-03 19:40:54.000000 longitudinal_trends-0.0.4/longitudinal_trends/__init__.py
-drwxrwxrwx   0 msakir    (1000) msakir    (1000)        0 2023-04-05 19:45:58.926456 longitudinal_trends-0.0.4/longitudinal_trends.egg-info/
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)     9294 2023-04-05 19:45:58.000000 longitudinal_trends-0.0.4/longitudinal_trends.egg-info/PKG-INFO
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)      307 2023-04-05 19:45:58.000000 longitudinal_trends-0.0.4/longitudinal_trends.egg-info/SOURCES.txt
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)        1 2023-04-05 19:45:58.000000 longitudinal_trends-0.0.4/longitudinal_trends.egg-info/dependency_links.txt
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)       45 2023-04-05 19:45:58.000000 longitudinal_trends-0.0.4/longitudinal_trends.egg-info/requires.txt
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)       20 2023-04-05 19:45:58.000000 longitudinal_trends-0.0.4/longitudinal_trends.egg-info/top_level.txt
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)     1096 2023-04-05 19:45:36.000000 longitudinal_trends-0.0.4/pyproject.toml
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)      136 2023-04-03 18:57:25.000000 longitudinal_trends-0.0.4/requirements.txt
--rwxrwxrwx   0 msakir    (1000) msakir    (1000)       38 2023-04-05 19:45:59.001477 longitudinal_trends-0.0.4/setup.cfg
+drwxrwxrwx   0 msakir    (1000) msakir    (1000)        0 2023-04-07 07:05:09.576433 longitudinal_trends-0.0.5/
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)     1104 2023-03-18 15:04:53.000000 longitudinal_trends-0.0.5/LICENSE
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)       34 2023-03-18 16:38:44.000000 longitudinal_trends-0.0.5/MANIFEST.in
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)     9882 2023-04-07 07:05:09.570425 longitudinal_trends-0.0.5/PKG-INFO
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)     9349 2023-04-07 07:04:07.000000 longitudinal_trends-0.0.5/README.md
+drwxrwxrwx   0 msakir    (1000) msakir    (1000)        0 2023-04-07 07:05:09.268182 longitudinal_trends-0.0.5/longitudinal_trends/
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)    17278 2023-04-03 19:40:54.000000 longitudinal_trends-0.0.5/longitudinal_trends/__init__.py
+drwxrwxrwx   0 msakir    (1000) msakir    (1000)        0 2023-04-07 07:05:09.507698 longitudinal_trends-0.0.5/longitudinal_trends.egg-info/
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)     9882 2023-04-07 07:05:08.000000 longitudinal_trends-0.0.5/longitudinal_trends.egg-info/PKG-INFO
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)      307 2023-04-07 07:05:09.000000 longitudinal_trends-0.0.5/longitudinal_trends.egg-info/SOURCES.txt
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)        1 2023-04-07 07:05:08.000000 longitudinal_trends-0.0.5/longitudinal_trends.egg-info/dependency_links.txt
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)       45 2023-04-07 07:05:08.000000 longitudinal_trends-0.0.5/longitudinal_trends.egg-info/requires.txt
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)       20 2023-04-07 07:05:08.000000 longitudinal_trends-0.0.5/longitudinal_trends.egg-info/top_level.txt
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)     1096 2023-04-07 07:04:37.000000 longitudinal_trends-0.0.5/pyproject.toml
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)      136 2023-04-03 18:57:25.000000 longitudinal_trends-0.0.5/requirements.txt
+-rwxrwxrwx   0 msakir    (1000) msakir    (1000)       38 2023-04-07 07:05:09.578426 longitudinal_trends-0.0.5/setup.cfg
```

### Comparing `longitudinal_trends-0.0.4/LICENSE` & `longitudinal_trends-0.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `longitudinal_trends-0.0.4/PKG-INFO` & `longitudinal_trends-0.0.5/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: longitudinal_trends
-Version: 0.0.4
+Version: 0.0.5
 Summary: Download long-term longitudinal Google Trends
 Author: Mohammad Saleh Ahsan Sakir, Taeyong Park
 Author-email: ahsansakir506@gmail.com, taeyongp@andrew.cmu.edu
 License: MIT
 Project-URL: homepage, https://github.com/Mohammad-sakir/longitudinalTrends
 Keywords: google trends api search longtrends cross section
 Classifier: Programming Language :: Python :: 3
@@ -16,17 +16,19 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # longitudinal_trends
 
 ## Introduction
 
-This is an python library for generating longitudinal google trends data.
+This is a python library for downloading cross-section and time-series Google Trends and converting them to longitudinal data.
 
-As of this moment, Google Trends have restriction on data formats and timeline. If you want to collect daily data for 2 years, you cannot do so in one go. Google Trends automatically provides you weekly data if your request timeline is more than **269 days**. Same applies across all formats. Even after collecting the data individually, it is a hassle to reindex them over time and by region. Thats when `longitudinal_trends` comes in handy. With the minimal coding, you can collect all your required data in an organized format which are also reindexed for you.
+Although Google Trends provides cross-section and time-series search data, longitudinal Google Trends data are not readily available. There exist several practical issues that make it difficult for researchers to generate longitudinal Google Trends data themselves. First, Google Trends provides normalized counts from zero to 100. As a result, combining different regions' time-series Google Trends data does not create desired longitudinal data. For the same reason, combining cross-sectional Google Trends data over time does not create desired longitudinal data. Second, Google Trends has restrictions on data formats and timeline. For instance, if you want to collect daily data for 2 years, you cannot do so. Google Trends automatically provides weekly data if your request timeline is more than 269 days. Similarly, Google Trends automatically provides monthly data if your request timeline is more than 269 weeks even though you want to collect weekly data. 
+
+The longitudinal_trends library resolves the aforementioned issues and allows researchers to generate longitudinal Google Trends. 
 
 This library is built on top of another library `pytrends` which also have few dependencies. As long as `Google Trends API`, `pytrends` and all their dependencies work, `longitudinal_trends` will also work!
 
 ***Note**: This library is still in planning phase and not fully tested.*
 
 ## Table of contents
```

### Comparing `longitudinal_trends-0.0.4/README.md` & `longitudinal_trends-0.0.5/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,16 @@
 # longitudinal_trends
 
 ## Introduction
 
-This is an python library for generating longitudinal google trends data.
+This is a python library for downloading cross-section and time-series Google Trends and converting them to longitudinal data.
 
-As of this moment, Google Trends have restriction on data formats and timeline. If you want to collect daily data for 2 years, you cannot do so in one go. Google Trends automatically provides you weekly data if your request timeline is more than **269 days**. Same applies across all formats. Even after collecting the data individually, it is a hassle to reindex them over time and by region. Thats when `longitudinal_trends` comes in handy. With the minimal coding, you can collect all your required data in an organized format which are also reindexed for you.
+Although Google Trends provides cross-section and time-series search data, longitudinal Google Trends data are not readily available. There exist several practical issues that make it difficult for researchers to generate longitudinal Google Trends data themselves. First, Google Trends provides normalized counts from zero to 100. As a result, combining different regions' time-series Google Trends data does not create desired longitudinal data. For the same reason, combining cross-sectional Google Trends data over time does not create desired longitudinal data. Second, Google Trends has restrictions on data formats and timeline. For instance, if you want to collect daily data for 2 years, you cannot do so. Google Trends automatically provides weekly data if your request timeline is more than 269 days. Similarly, Google Trends automatically provides monthly data if your request timeline is more than 269 weeks even though you want to collect weekly data. 
+
+The longitudinal_trends library resolves the aforementioned issues and allows researchers to generate longitudinal Google Trends. 
 
 This library is built on top of another library `pytrends` which also have few dependencies. As long as `Google Trends API`, `pytrends` and all their dependencies work, `longitudinal_trends` will also work!
 
 ***Note**: This library is still in planning phase and not fully tested.*
 
 ## Table of contents
```

### Comparing `longitudinal_trends-0.0.4/longitudinal_trends/__init__.py` & `longitudinal_trends-0.0.5/longitudinal_trends/__init__.py`

 * *Files identical despite different names*

### Comparing `longitudinal_trends-0.0.4/longitudinal_trends.egg-info/PKG-INFO` & `longitudinal_trends-0.0.5/longitudinal_trends.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: longitudinal-trends
-Version: 0.0.4
+Version: 0.0.5
 Summary: Download long-term longitudinal Google Trends
 Author: Mohammad Saleh Ahsan Sakir, Taeyong Park
 Author-email: ahsansakir506@gmail.com, taeyongp@andrew.cmu.edu
 License: MIT
 Project-URL: homepage, https://github.com/Mohammad-sakir/longitudinalTrends
 Keywords: google trends api search longtrends cross section
 Classifier: Programming Language :: Python :: 3
@@ -16,17 +16,19 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # longitudinal_trends
 
 ## Introduction
 
-This is an python library for generating longitudinal google trends data.
+This is a python library for downloading cross-section and time-series Google Trends and converting them to longitudinal data.
 
-As of this moment, Google Trends have restriction on data formats and timeline. If you want to collect daily data for 2 years, you cannot do so in one go. Google Trends automatically provides you weekly data if your request timeline is more than **269 days**. Same applies across all formats. Even after collecting the data individually, it is a hassle to reindex them over time and by region. Thats when `longitudinal_trends` comes in handy. With the minimal coding, you can collect all your required data in an organized format which are also reindexed for you.
+Although Google Trends provides cross-section and time-series search data, longitudinal Google Trends data are not readily available. There exist several practical issues that make it difficult for researchers to generate longitudinal Google Trends data themselves. First, Google Trends provides normalized counts from zero to 100. As a result, combining different regions' time-series Google Trends data does not create desired longitudinal data. For the same reason, combining cross-sectional Google Trends data over time does not create desired longitudinal data. Second, Google Trends has restrictions on data formats and timeline. For instance, if you want to collect daily data for 2 years, you cannot do so. Google Trends automatically provides weekly data if your request timeline is more than 269 days. Similarly, Google Trends automatically provides monthly data if your request timeline is more than 269 weeks even though you want to collect weekly data. 
+
+The longitudinal_trends library resolves the aforementioned issues and allows researchers to generate longitudinal Google Trends. 
 
 This library is built on top of another library `pytrends` which also have few dependencies. As long as `Google Trends API`, `pytrends` and all their dependencies work, `longitudinal_trends` will also work!
 
 ***Note**: This library is still in planning phase and not fully tested.*
 
 ## Table of contents
```

### Comparing `longitudinal_trends-0.0.4/pyproject.toml` & `longitudinal_trends-0.0.5/pyproject.toml`

 * *Files 9% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools"]#, "setuptools-scm"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "longitudinal_trends"
-version='0.0.4'
+version='0.0.5'
 description="Download long-term longitudinal Google Trends"
 urls = {homepage = "https://github.com/Mohammad-sakir/longitudinalTrends"}
 requires-python = ">=3.6"
 authors = [
     {name = "Mohammad Saleh Ahsan Sakir"},
     {name = "Taeyong Park"}, 
     {email="ahsansakir506@gmail.com"},
```

