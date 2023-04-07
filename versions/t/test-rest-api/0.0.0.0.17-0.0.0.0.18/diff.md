# Comparing `tmp/test_rest_api-0.0.0.0.17.tar.gz` & `tmp/test_rest_api-0.0.0.0.18.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "test_rest_api-0.0.0.0.17.tar", last modified: Fri Apr  7 06:19:03 2023, max compression
+gzip compressed data, was "test_rest_api-0.0.0.0.18.tar", last modified: Fri Apr  7 06:31:31 2023, max compression
```

## Comparing `test_rest_api-0.0.0.0.17.tar` & `test_rest_api-0.0.0.0.18.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.684213 test_rest_api-0.0.0.0.17/
--rw-r--r--   0 trjose     (501) staff       (20)     1067 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/LICENSE
--rw-r--r--   0 trjose     (501) staff       (20)    19425 2023-04-07 06:19:03.683791 test_rest_api-0.0.0.0.17/PKG-INFO
--rw-r--r--   0 trjose     (501) staff       (20)    17892 2023-04-07 06:16:46.000000 test_rest_api-0.0.0.0.17/README.md
--rw-r--r--   0 trjose     (501) staff       (20)       38 2023-04-07 06:19:03.684371 test_rest_api-0.0.0.0.17/setup.cfg
--rw-r--r--   0 trjose     (501) staff       (20)     2619 2023-04-07 06:18:42.000000 test_rest_api-0.0.0.0.17/setup.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.666096 test_rest_api-0.0.0.0.17/test_rest_api/
--rw-r--r--   0 trjose     (501) staff       (20)      236 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1608 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/__main__.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.669622 test_rest_api-0.0.0.0.17/test_rest_api/global_variables/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/global_variables/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1161 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/global_variables/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)     2568 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/global_variables/global_variables.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.670886 test_rest_api-0.0.0.0.17/test_rest_api/logger/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/logger/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1237 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/logger/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      848 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/logger/logger.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.672541 test_rest_api-0.0.0.0.17/test_rest_api/reporting/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-25 09:45:47.000000 test_rest_api-0.0.0.0.17/test_rest_api/reporting/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)    34276 2023-04-04 09:03:46.000000 test_rest_api-0.0.0.0.17/test_rest_api/reporting/html.py
--rw-r--r--   0 trjose     (501) staff       (20)     5404 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/reporting/report.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.674957 test_rest_api-0.0.0.0.17/test_rest_api/rest_api/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:34:23.000000 test_rest_api-0.0.0.0.17/test_rest_api/rest_api/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1824 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/rest_api/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      423 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/rest_api/method.py
--rw-r--r--   0 trjose     (501) staff       (20)      332 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/rest_api/response.py
--rw-r--r--   0 trjose     (501) staff       (20)     5987 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/rest_api/rest_api.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.677803 test_rest_api-0.0.0.0.17/test_rest_api/testing/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:03:23.000000 test_rest_api-0.0.0.0.17/test_rest_api/testing/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     3904 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/testing/bug.py
--rw-r--r--   0 trjose     (501) staff       (20)    14232 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/testing/decorator.py
--rw-r--r--   0 trjose     (501) staff       (20)      863 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/testing/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)    12307 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.17/test_rest_api/testing/runner.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.682839 test_rest_api-0.0.0.0.17/test_rest_api/utils/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)      943 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/aiohttp_session.py
--rw-r--r--   0 trjose     (501) staff       (20)      546 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/colors.py
--rw-r--r--   0 trjose     (501) staff       (20)      247 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/decorator_hints.py
--rw-r--r--   0 trjose     (501) staff       (20)     2027 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/error_msg.py
--rw-r--r--   0 trjose     (501) staff       (20)     1127 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      606 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.17/test_rest_api/utils/logger.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:19:03.668325 test_rest_api-0.0.0.0.17/test_rest_api.egg-info/
--rw-r--r--   0 trjose     (501) staff       (20)    19425 2023-04-07 06:19:03.000000 test_rest_api-0.0.0.0.17/test_rest_api.egg-info/PKG-INFO
--rw-r--r--   0 trjose     (501) staff       (20)     1175 2023-04-07 06:19:03.000000 test_rest_api-0.0.0.0.17/test_rest_api.egg-info/SOURCES.txt
--rw-r--r--   0 trjose     (501) staff       (20)        1 2023-04-07 06:19:03.000000 test_rest_api-0.0.0.0.17/test_rest_api.egg-info/dependency_links.txt
--rw-r--r--   0 trjose     (501) staff       (20)       29 2023-04-07 06:19:03.000000 test_rest_api-0.0.0.0.17/test_rest_api.egg-info/requires.txt
--rw-r--r--   0 trjose     (501) staff       (20)       14 2023-04-07 06:19:03.000000 test_rest_api-0.0.0.0.17/test_rest_api.egg-info/top_level.txt
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.478587 test_rest_api-0.0.0.0.18/
+-rw-r--r--   0 trjose     (501) staff       (20)     1067 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/LICENSE
+-rw-r--r--   0 trjose     (501) staff       (20)    19428 2023-04-07 06:31:31.478287 test_rest_api-0.0.0.0.18/PKG-INFO
+-rw-r--r--   0 trjose     (501) staff       (20)    17895 2023-04-07 06:24:15.000000 test_rest_api-0.0.0.0.18/README.md
+-rw-r--r--   0 trjose     (501) staff       (20)       38 2023-04-07 06:31:31.478689 test_rest_api-0.0.0.0.18/setup.cfg
+-rw-r--r--   0 trjose     (501) staff       (20)     2619 2023-04-07 06:31:01.000000 test_rest_api-0.0.0.0.18/setup.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.461205 test_rest_api-0.0.0.0.18/test_rest_api/
+-rw-r--r--   0 trjose     (501) staff       (20)      236 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1608 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/__main__.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.465443 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1161 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)     2568 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/global_variables.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.466952 test_rest_api-0.0.0.0.18/test_rest_api/logger/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/logger/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1237 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/logger/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      848 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/logger/logger.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.468922 test_rest_api-0.0.0.0.18/test_rest_api/reporting/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-25 09:45:47.000000 test_rest_api-0.0.0.0.18/test_rest_api/reporting/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)    34276 2023-04-04 09:03:46.000000 test_rest_api-0.0.0.0.18/test_rest_api/reporting/html.py
+-rw-r--r--   0 trjose     (501) staff       (20)     5404 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/reporting/report.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.471624 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:34:23.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1824 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      423 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/method.py
+-rw-r--r--   0 trjose     (501) staff       (20)      332 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/response.py
+-rw-r--r--   0 trjose     (501) staff       (20)     5987 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/rest_api.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.474060 test_rest_api-0.0.0.0.18/test_rest_api/testing/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:03:23.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     3904 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/bug.py
+-rw-r--r--   0 trjose     (501) staff       (20)    14232 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/decorator.py
+-rw-r--r--   0 trjose     (501) staff       (20)      863 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)    12307 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/runner.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.477659 test_rest_api-0.0.0.0.18/test_rest_api/utils/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)      943 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/aiohttp_session.py
+-rw-r--r--   0 trjose     (501) staff       (20)      546 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/colors.py
+-rw-r--r--   0 trjose     (501) staff       (20)      247 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/decorator_hints.py
+-rw-r--r--   0 trjose     (501) staff       (20)     2027 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/error_msg.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1127 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      606 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/logger.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.464062 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/
+-rw-r--r--   0 trjose     (501) staff       (20)    19428 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/PKG-INFO
+-rw-r--r--   0 trjose     (501) staff       (20)     1175 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/SOURCES.txt
+-rw-r--r--   0 trjose     (501) staff       (20)        1 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/dependency_links.txt
+-rw-r--r--   0 trjose     (501) staff       (20)       29 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/requires.txt
+-rw-r--r--   0 trjose     (501) staff       (20)       14 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/top_level.txt
```

### Comparing `test_rest_api-0.0.0.0.17/LICENSE` & `test_rest_api-0.0.0.0.18/LICENSE`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/PKG-INFO` & `test_rest_api-0.0.0.0.18/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: test_rest_api
-Version: 0.0.0.0.17
+Version: 0.0.0.0.18
 Summary: Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests
 Author: Troy M Jose
 Author-email: 
 Keywords: test,unittest,restapi,testframework,asyncio,async,asynchronous,testingframework,rest,api,python,python3,testing,unittesting,automation,automationtest,automationtesting,restapitest,restapitesting,restapiunittest,restapiunittesting,restapiautomation,restapiautomationtest,restapiautomationtesting,apitest,apitesting,apiunittest,apiunittesting,apiautomation,apiautomationtest,apiautomationtesting
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -67,23 +67,26 @@
 - __Html test reporting__ with custom logs & summary dashboards
 - Create complex flows using __parameterization__ & __correlation__
 - __Group__ similar tests using hashtags eg: __#smoke__
 - Supports __CI/CD__ test automation integrations
 - Designed to be __easy__ to use & learn
 
 <h2 id="installation">Installation</h2>
+
 If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:
 
 ```pip install test_rest_api```
 
 <h2 id="usage">Usage</h2>
 
 
 - - -
+
 <h4 id="1-basic-usage">1. Basic usage</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" ```
 
 - Tests are executed from the __command line__ using the test_rest_api module directly
```

### Comparing `test_rest_api-0.0.0.0.17/README.md` & `test_rest_api-0.0.0.0.18/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -39,23 +39,26 @@
 - __Html test reporting__ with custom logs & summary dashboards
 - Create complex flows using __parameterization__ & __correlation__
 - __Group__ similar tests using hashtags eg: __#smoke__
 - Supports __CI/CD__ test automation integrations
 - Designed to be __easy__ to use & learn
 
 <h2 id="installation">Installation</h2>
+
 If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:
 
 ```pip install test_rest_api```
 
 <h2 id="usage">Usage</h2>
 
 
 - - -
+
 <h4 id="1-basic-usage">1. Basic usage</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" ```
 
 - Tests are executed from the __command line__ using the test_rest_api module directly
```

### Comparing `test_rest_api-0.0.0.0.17/setup.py` & `test_rest_api-0.0.0.0.18/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 
 # Get README.md details
 with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
     long_description = "\n" + f.read()
 
 # Setup
 setup(name="test_rest_api",
-      version="0.0.0.0.17",
+      version="0.0.0.0.18",
       author="Troy M Jose",
       author_email="",
       description="Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests",
       keywords=['test', 'unittest', 'restapi', 'testframework', 'asyncio', 'async', 'asynchronous',
                 'testingframework', 'rest', 'api', 'python', 'python3', 'testing', 'unittesting', 'automation',
                 'automationtest', 'automationtesting',
                 'restapitest', 'restapitesting', 'restapiunittest', 'restapiunittesting', 'restapiautomation',
```

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/__main__.py` & `test_rest_api-0.0.0.0.18/test_rest_api/__main__.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/global_variables/exception.py` & `test_rest_api-0.0.0.0.18/test_rest_api/global_variables/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/global_variables/global_variables.py` & `test_rest_api-0.0.0.0.18/test_rest_api/global_variables/global_variables.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/logger/exception.py` & `test_rest_api-0.0.0.0.18/test_rest_api/logger/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/logger/logger.py` & `test_rest_api-0.0.0.0.18/test_rest_api/logger/logger.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/reporting/html.py` & `test_rest_api-0.0.0.0.18/test_rest_api/reporting/html.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/reporting/report.py` & `test_rest_api-0.0.0.0.18/test_rest_api/reporting/report.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/rest_api/exception.py` & `test_rest_api-0.0.0.0.18/test_rest_api/rest_api/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/rest_api/rest_api.py` & `test_rest_api-0.0.0.0.18/test_rest_api/rest_api/rest_api.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/testing/bug.py` & `test_rest_api-0.0.0.0.18/test_rest_api/testing/bug.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/testing/decorator.py` & `test_rest_api-0.0.0.0.18/test_rest_api/testing/decorator.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/testing/exception.py` & `test_rest_api-0.0.0.0.18/test_rest_api/testing/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/testing/runner.py` & `test_rest_api-0.0.0.0.18/test_rest_api/testing/runner.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/utils/aiohttp_session.py` & `test_rest_api-0.0.0.0.18/test_rest_api/utils/aiohttp_session.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/utils/colors.py` & `test_rest_api-0.0.0.0.18/test_rest_api/utils/colors.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/utils/error_msg.py` & `test_rest_api-0.0.0.0.18/test_rest_api/utils/error_msg.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/utils/exception.py` & `test_rest_api-0.0.0.0.18/test_rest_api/utils/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api/utils/logger.py` & `test_rest_api-0.0.0.0.18/test_rest_api/utils/logger.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api.egg-info/PKG-INFO` & `test_rest_api-0.0.0.0.18/test_rest_api.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: test-rest-api
-Version: 0.0.0.0.17
+Version: 0.0.0.0.18
 Summary: Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests
 Author: Troy M Jose
 Author-email: 
 Keywords: test,unittest,restapi,testframework,asyncio,async,asynchronous,testingframework,rest,api,python,python3,testing,unittesting,automation,automationtest,automationtesting,restapitest,restapitesting,restapiunittest,restapiunittesting,restapiautomation,restapiautomationtest,restapiautomationtesting,apitest,apitesting,apiunittest,apiunittesting,apiautomation,apiautomationtest,apiautomationtesting
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -67,23 +67,26 @@
 - __Html test reporting__ with custom logs & summary dashboards
 - Create complex flows using __parameterization__ & __correlation__
 - __Group__ similar tests using hashtags eg: __#smoke__
 - Supports __CI/CD__ test automation integrations
 - Designed to be __easy__ to use & learn
 
 <h2 id="installation">Installation</h2>
+
 If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:
 
 ```pip install test_rest_api```
 
 <h2 id="usage">Usage</h2>
 
 
 - - -
+
 <h4 id="1-basic-usage">1. Basic usage</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" ```
 
 - Tests are executed from the __command line__ using the test_rest_api module directly
```

### Comparing `test_rest_api-0.0.0.0.17/test_rest_api.egg-info/SOURCES.txt` & `test_rest_api-0.0.0.0.18/test_rest_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

