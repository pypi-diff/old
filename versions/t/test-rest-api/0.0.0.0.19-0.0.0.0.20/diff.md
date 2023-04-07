# Comparing `tmp/test_rest_api-0.0.0.0.19.tar.gz` & `tmp/test_rest_api-0.0.0.0.20.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "test_rest_api-0.0.0.0.19.tar", last modified: Fri Apr  7 06:37:18 2023, max compression
+gzip compressed data, was "test_rest_api-0.0.0.0.20.tar", last modified: Fri Apr  7 07:31:18 2023, max compression
```

## Comparing `test_rest_api-0.0.0.0.19.tar` & `test_rest_api-0.0.0.0.20.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.285109 test_rest_api-0.0.0.0.19/
--rw-r--r--   0 trjose     (501) staff       (20)     1067 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/LICENSE
--rw-r--r--   0 trjose     (501) staff       (20)    19341 2023-04-07 06:37:18.284787 test_rest_api-0.0.0.0.19/PKG-INFO
--rw-r--r--   0 trjose     (501) staff       (20)    17808 2023-04-07 06:36:13.000000 test_rest_api-0.0.0.0.19/README.md
--rw-r--r--   0 trjose     (501) staff       (20)       38 2023-04-07 06:37:18.285210 test_rest_api-0.0.0.0.19/setup.cfg
--rw-r--r--   0 trjose     (501) staff       (20)     2619 2023-04-07 06:32:54.000000 test_rest_api-0.0.0.0.19/setup.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.271078 test_rest_api-0.0.0.0.19/test_rest_api/
--rw-r--r--   0 trjose     (501) staff       (20)      236 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1608 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/__main__.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.274765 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1161 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)     2568 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/global_variables.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.276098 test_rest_api-0.0.0.0.19/test_rest_api/logger/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/logger/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1237 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/logger/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      848 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/logger/logger.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.277652 test_rest_api-0.0.0.0.19/test_rest_api/reporting/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-25 09:45:47.000000 test_rest_api-0.0.0.0.19/test_rest_api/reporting/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)    34276 2023-04-04 09:03:46.000000 test_rest_api-0.0.0.0.19/test_rest_api/reporting/html.py
--rw-r--r--   0 trjose     (501) staff       (20)     5404 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/reporting/report.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.279470 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:34:23.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1824 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      423 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/method.py
--rw-r--r--   0 trjose     (501) staff       (20)      332 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/response.py
--rw-r--r--   0 trjose     (501) staff       (20)     5987 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/rest_api.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.281378 test_rest_api-0.0.0.0.19/test_rest_api/testing/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:03:23.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     3904 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/bug.py
--rw-r--r--   0 trjose     (501) staff       (20)    14232 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/decorator.py
--rw-r--r--   0 trjose     (501) staff       (20)      863 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)    12307 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/runner.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.284288 test_rest_api-0.0.0.0.19/test_rest_api/utils/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)      943 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/aiohttp_session.py
--rw-r--r--   0 trjose     (501) staff       (20)      546 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/colors.py
--rw-r--r--   0 trjose     (501) staff       (20)      247 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/decorator_hints.py
--rw-r--r--   0 trjose     (501) staff       (20)     2027 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/error_msg.py
--rw-r--r--   0 trjose     (501) staff       (20)     1127 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      606 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/logger.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.273373 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/
--rw-r--r--   0 trjose     (501) staff       (20)    19341 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/PKG-INFO
--rw-r--r--   0 trjose     (501) staff       (20)     1175 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/SOURCES.txt
--rw-r--r--   0 trjose     (501) staff       (20)        1 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/dependency_links.txt
--rw-r--r--   0 trjose     (501) staff       (20)       29 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/requires.txt
--rw-r--r--   0 trjose     (501) staff       (20)       14 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/top_level.txt
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.592845 test_rest_api-0.0.0.0.20/
+-rw-r--r--   0 trjose     (501) staff       (20)     1067 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/LICENSE
+-rw-r--r--   0 trjose     (501) staff       (20)    19348 2023-04-07 07:31:18.592507 test_rest_api-0.0.0.0.20/PKG-INFO
+-rw-r--r--   0 trjose     (501) staff       (20)    17815 2023-04-07 07:18:33.000000 test_rest_api-0.0.0.0.20/README.md
+-rw-r--r--   0 trjose     (501) staff       (20)       38 2023-04-07 07:31:18.592953 test_rest_api-0.0.0.0.20/setup.cfg
+-rw-r--r--   0 trjose     (501) staff       (20)     2619 2023-04-07 07:15:18.000000 test_rest_api-0.0.0.0.20/setup.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.575254 test_rest_api-0.0.0.0.20/test_rest_api/
+-rw-r--r--   0 trjose     (501) staff       (20)      236 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1608 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/__main__.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.579242 test_rest_api-0.0.0.0.20/test_rest_api/global_variables/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/global_variables/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1161 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/global_variables/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)     2568 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/global_variables/global_variables.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.580841 test_rest_api-0.0.0.0.20/test_rest_api/logger/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/logger/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1237 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/logger/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      848 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/logger/logger.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.582904 test_rest_api-0.0.0.0.20/test_rest_api/reporting/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-25 09:45:47.000000 test_rest_api-0.0.0.0.20/test_rest_api/reporting/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)    34453 2023-04-07 07:30:18.000000 test_rest_api-0.0.0.0.20/test_rest_api/reporting/html.py
+-rw-r--r--   0 trjose     (501) staff       (20)     5404 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/reporting/report.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.585906 test_rest_api-0.0.0.0.20/test_rest_api/rest_api/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:34:23.000000 test_rest_api-0.0.0.0.20/test_rest_api/rest_api/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1824 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/rest_api/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      423 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/rest_api/method.py
+-rw-r--r--   0 trjose     (501) staff       (20)      332 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/rest_api/response.py
+-rw-r--r--   0 trjose     (501) staff       (20)     5987 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/rest_api/rest_api.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.588256 test_rest_api-0.0.0.0.20/test_rest_api/testing/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:03:23.000000 test_rest_api-0.0.0.0.20/test_rest_api/testing/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     3904 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/testing/bug.py
+-rw-r--r--   0 trjose     (501) staff       (20)    14232 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/testing/decorator.py
+-rw-r--r--   0 trjose     (501) staff       (20)      863 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/testing/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)    12307 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.20/test_rest_api/testing/runner.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.591904 test_rest_api-0.0.0.0.20/test_rest_api/utils/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)      943 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/aiohttp_session.py
+-rw-r--r--   0 trjose     (501) staff       (20)      546 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/colors.py
+-rw-r--r--   0 trjose     (501) staff       (20)      247 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/decorator_hints.py
+-rw-r--r--   0 trjose     (501) staff       (20)     2027 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/error_msg.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1127 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      606 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.20/test_rest_api/utils/logger.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 07:31:18.577937 test_rest_api-0.0.0.0.20/test_rest_api.egg-info/
+-rw-r--r--   0 trjose     (501) staff       (20)    19348 2023-04-07 07:31:18.000000 test_rest_api-0.0.0.0.20/test_rest_api.egg-info/PKG-INFO
+-rw-r--r--   0 trjose     (501) staff       (20)     1175 2023-04-07 07:31:18.000000 test_rest_api-0.0.0.0.20/test_rest_api.egg-info/SOURCES.txt
+-rw-r--r--   0 trjose     (501) staff       (20)        1 2023-04-07 07:31:18.000000 test_rest_api-0.0.0.0.20/test_rest_api.egg-info/dependency_links.txt
+-rw-r--r--   0 trjose     (501) staff       (20)       29 2023-04-07 07:31:18.000000 test_rest_api-0.0.0.0.20/test_rest_api.egg-info/requires.txt
+-rw-r--r--   0 trjose     (501) staff       (20)       14 2023-04-07 07:31:18.000000 test_rest_api-0.0.0.0.20/test_rest_api.egg-info/top_level.txt
```

### Comparing `test_rest_api-0.0.0.0.19/LICENSE` & `test_rest_api-0.0.0.0.20/LICENSE`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/PKG-INFO` & `test_rest_api-0.0.0.0.20/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: test_rest_api
-Version: 0.0.0.0.19
+Version: 0.0.0.0.20
 Summary: Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests
 Author: Troy M Jose
 Author-email: 
 Keywords: test,unittest,restapi,testframework,asyncio,async,asynchronous,testingframework,rest,api,python,python3,testing,unittesting,automation,automationtest,automationtesting,restapitest,restapitesting,restapiunittest,restapiunittesting,restapiautomation,restapiautomationtest,restapiautomationtesting,apitest,apitesting,apiunittest,apiunittesting,apiautomation,apiautomationtest,apiautomationtesting
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -22,15 +22,15 @@
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Classifier: Topic :: Software Development :: Libraries :: Application Frameworks
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 
-<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/test_rest_api.png"  width="50%" >
+<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/assets/test_rest_api.png"  width="50%" >
 
 # TEST REST API
 
 Create fast modern __asynchronous__ tests for __REST API__ testing
 
 ```#FAST #EASY #ASYNC #RESTAPI #TESTING #AUTOMATION```
```

### Comparing `test_rest_api-0.0.0.0.19/README.md` & `test_rest_api-0.0.0.0.20/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/test_rest_api.png"  width="50%" >
+<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/assets/test_rest_api.png"  width="50%" >
 
 # TEST REST API
 
 Create fast modern __asynchronous__ tests for __REST API__ testing
 
 ```#FAST #EASY #ASYNC #RESTAPI #TESTING #AUTOMATION```
```

### Comparing `test_rest_api-0.0.0.0.19/setup.py` & `test_rest_api-0.0.0.0.20/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 
 # Get README.md details
 with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
     long_description = "\n" + f.read()
 
 # Setup
 setup(name="test_rest_api",
-      version="0.0.0.0.19",
+      version="0.0.0.0.20",
       author="Troy M Jose",
       author_email="",
       description="Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests",
       keywords=['test', 'unittest', 'restapi', 'testframework', 'asyncio', 'async', 'asynchronous',
                 'testingframework', 'rest', 'api', 'python', 'python3', 'testing', 'unittesting', 'automation',
                 'automationtest', 'automationtesting',
                 'restapitest', 'restapitesting', 'restapiunittest', 'restapiunittesting', 'restapiautomation',
```

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/__main__.py` & `test_rest_api-0.0.0.0.20/test_rest_api/__main__.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/global_variables/exception.py` & `test_rest_api-0.0.0.0.20/test_rest_api/global_variables/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/global_variables/global_variables.py` & `test_rest_api-0.0.0.0.20/test_rest_api/global_variables/global_variables.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/logger/exception.py` & `test_rest_api-0.0.0.0.20/test_rest_api/logger/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/logger/logger.py` & `test_rest_api-0.0.0.0.20/test_rest_api/logger/logger.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/reporting/html.py` & `test_rest_api-0.0.0.0.20/test_rest_api/reporting/html.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,16 @@
 html_str = """
 <!DOCTYPE html>
 <html lang="en">
   <head>
     <meta charset="utf-8" />
     <meta name="viewport" content="width=device-width, initial-scale=1" />
     <title>REPORT</title>
+    <!-- add icon link -->
+    <link rel = "icon" href = "https://raw.githubusercontent.com/troymjose/test_rest_api/main/assets/test_rest_api.ico" type = "image/x-icon">
     <style>
       html {
         scroll-behavior: smooth;
       }
     </style>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
     <link
@@ -29,15 +31,15 @@
         class="navbar fixed-top bg-dark-subtle shadow-lg p-3 mb-5 bg-body-tertiary"
         data-bs-theme="dark"
       >
         <div class="container-fluid">
           <a class="navbar-brand" style="font-size: x-large;">T E S T -  R E S T - A P I </a>
           <form class="d-flex" role="search">
             <a class="text-light" type="submit" href="https://pypi.org/project/test-rest-api/" target="_blank">
-            <img src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/test_rest_api.ico" alt="" width="50" height="50" class="rounded-circle"></a>
+            <img src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/assets/test_rest_api.ico" alt="" width="50" height="50" class="rounded-circle"></a>
             </a>
           </form>
         </div>
       </nav>
       <!-- Summary Results -->
       <div id="summary-div" style="padding: 30px; text-align: left">
         <br />
```

#### html2text {}

```diff
@@ -1,12 +1,13 @@
 html_str = """
 
 
 
 
+
 T E S T - R E S T - A P I
 
 
 
 
   Summary
 ===============================================================================
```

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/reporting/report.py` & `test_rest_api-0.0.0.0.20/test_rest_api/reporting/report.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/rest_api/exception.py` & `test_rest_api-0.0.0.0.20/test_rest_api/rest_api/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/rest_api/rest_api.py` & `test_rest_api-0.0.0.0.20/test_rest_api/rest_api/rest_api.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/testing/bug.py` & `test_rest_api-0.0.0.0.20/test_rest_api/testing/bug.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/testing/decorator.py` & `test_rest_api-0.0.0.0.20/test_rest_api/testing/decorator.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/testing/exception.py` & `test_rest_api-0.0.0.0.20/test_rest_api/testing/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/testing/runner.py` & `test_rest_api-0.0.0.0.20/test_rest_api/testing/runner.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/utils/aiohttp_session.py` & `test_rest_api-0.0.0.0.20/test_rest_api/utils/aiohttp_session.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/utils/colors.py` & `test_rest_api-0.0.0.0.20/test_rest_api/utils/colors.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/utils/error_msg.py` & `test_rest_api-0.0.0.0.20/test_rest_api/utils/error_msg.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/utils/exception.py` & `test_rest_api-0.0.0.0.20/test_rest_api/utils/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api/utils/logger.py` & `test_rest_api-0.0.0.0.20/test_rest_api/utils/logger.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api.egg-info/PKG-INFO` & `test_rest_api-0.0.0.0.20/test_rest_api.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: test-rest-api
-Version: 0.0.0.0.19
+Version: 0.0.0.0.20
 Summary: Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests
 Author: Troy M Jose
 Author-email: 
 Keywords: test,unittest,restapi,testframework,asyncio,async,asynchronous,testingframework,rest,api,python,python3,testing,unittesting,automation,automationtest,automationtesting,restapitest,restapitesting,restapiunittest,restapiunittesting,restapiautomation,restapiautomationtest,restapiautomationtesting,apitest,apitesting,apiunittest,apiunittesting,apiautomation,apiautomationtest,apiautomationtesting
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -22,15 +22,15 @@
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Classifier: Topic :: Software Development :: Libraries :: Application Frameworks
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 
-<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/test_rest_api.png"  width="50%" >
+<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/assets/test_rest_api.png"  width="50%" >
 
 # TEST REST API
 
 Create fast modern __asynchronous__ tests for __REST API__ testing
 
 ```#FAST #EASY #ASYNC #RESTAPI #TESTING #AUTOMATION```
```

### Comparing `test_rest_api-0.0.0.0.19/test_rest_api.egg-info/SOURCES.txt` & `test_rest_api-0.0.0.0.20/test_rest_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

