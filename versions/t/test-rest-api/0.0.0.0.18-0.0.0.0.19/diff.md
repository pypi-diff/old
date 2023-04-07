# Comparing `tmp/test_rest_api-0.0.0.0.18.tar.gz` & `tmp/test_rest_api-0.0.0.0.19.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "test_rest_api-0.0.0.0.18.tar", last modified: Fri Apr  7 06:31:31 2023, max compression
+gzip compressed data, was "test_rest_api-0.0.0.0.19.tar", last modified: Fri Apr  7 06:37:18 2023, max compression
```

## Comparing `test_rest_api-0.0.0.0.18.tar` & `test_rest_api-0.0.0.0.19.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.478587 test_rest_api-0.0.0.0.18/
--rw-r--r--   0 trjose     (501) staff       (20)     1067 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/LICENSE
--rw-r--r--   0 trjose     (501) staff       (20)    19428 2023-04-07 06:31:31.478287 test_rest_api-0.0.0.0.18/PKG-INFO
--rw-r--r--   0 trjose     (501) staff       (20)    17895 2023-04-07 06:24:15.000000 test_rest_api-0.0.0.0.18/README.md
--rw-r--r--   0 trjose     (501) staff       (20)       38 2023-04-07 06:31:31.478689 test_rest_api-0.0.0.0.18/setup.cfg
--rw-r--r--   0 trjose     (501) staff       (20)     2619 2023-04-07 06:31:01.000000 test_rest_api-0.0.0.0.18/setup.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.461205 test_rest_api-0.0.0.0.18/test_rest_api/
--rw-r--r--   0 trjose     (501) staff       (20)      236 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1608 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/__main__.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.465443 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1161 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)     2568 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/global_variables/global_variables.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.466952 test_rest_api-0.0.0.0.18/test_rest_api/logger/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/logger/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1237 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/logger/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      848 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/logger/logger.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.468922 test_rest_api-0.0.0.0.18/test_rest_api/reporting/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-25 09:45:47.000000 test_rest_api-0.0.0.0.18/test_rest_api/reporting/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)    34276 2023-04-04 09:03:46.000000 test_rest_api-0.0.0.0.18/test_rest_api/reporting/html.py
--rw-r--r--   0 trjose     (501) staff       (20)     5404 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/reporting/report.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.471624 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:34:23.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     1824 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      423 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/method.py
--rw-r--r--   0 trjose     (501) staff       (20)      332 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/response.py
--rw-r--r--   0 trjose     (501) staff       (20)     5987 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/rest_api/rest_api.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.474060 test_rest_api-0.0.0.0.18/test_rest_api/testing/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:03:23.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)     3904 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/bug.py
--rw-r--r--   0 trjose     (501) staff       (20)    14232 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/decorator.py
--rw-r--r--   0 trjose     (501) staff       (20)      863 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)    12307 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.18/test_rest_api/testing/runner.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.477659 test_rest_api-0.0.0.0.18/test_rest_api/utils/
--rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/__init__.py
--rw-r--r--   0 trjose     (501) staff       (20)      943 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/aiohttp_session.py
--rw-r--r--   0 trjose     (501) staff       (20)      546 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/colors.py
--rw-r--r--   0 trjose     (501) staff       (20)      247 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/decorator_hints.py
--rw-r--r--   0 trjose     (501) staff       (20)     2027 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/error_msg.py
--rw-r--r--   0 trjose     (501) staff       (20)     1127 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/exception.py
--rw-r--r--   0 trjose     (501) staff       (20)      606 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.18/test_rest_api/utils/logger.py
-drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:31:31.464062 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/
--rw-r--r--   0 trjose     (501) staff       (20)    19428 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/PKG-INFO
--rw-r--r--   0 trjose     (501) staff       (20)     1175 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/SOURCES.txt
--rw-r--r--   0 trjose     (501) staff       (20)        1 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/dependency_links.txt
--rw-r--r--   0 trjose     (501) staff       (20)       29 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/requires.txt
--rw-r--r--   0 trjose     (501) staff       (20)       14 2023-04-07 06:31:31.000000 test_rest_api-0.0.0.0.18/test_rest_api.egg-info/top_level.txt
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.285109 test_rest_api-0.0.0.0.19/
+-rw-r--r--   0 trjose     (501) staff       (20)     1067 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/LICENSE
+-rw-r--r--   0 trjose     (501) staff       (20)    19341 2023-04-07 06:37:18.284787 test_rest_api-0.0.0.0.19/PKG-INFO
+-rw-r--r--   0 trjose     (501) staff       (20)    17808 2023-04-07 06:36:13.000000 test_rest_api-0.0.0.0.19/README.md
+-rw-r--r--   0 trjose     (501) staff       (20)       38 2023-04-07 06:37:18.285210 test_rest_api-0.0.0.0.19/setup.cfg
+-rw-r--r--   0 trjose     (501) staff       (20)     2619 2023-04-07 06:32:54.000000 test_rest_api-0.0.0.0.19/setup.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.271078 test_rest_api-0.0.0.0.19/test_rest_api/
+-rw-r--r--   0 trjose     (501) staff       (20)      236 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1608 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/__main__.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.274765 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1161 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)     2568 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/global_variables/global_variables.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.276098 test_rest_api-0.0.0.0.19/test_rest_api/logger/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/logger/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1237 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/logger/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      848 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/logger/logger.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.277652 test_rest_api-0.0.0.0.19/test_rest_api/reporting/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-25 09:45:47.000000 test_rest_api-0.0.0.0.19/test_rest_api/reporting/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)    34276 2023-04-04 09:03:46.000000 test_rest_api-0.0.0.0.19/test_rest_api/reporting/html.py
+-rw-r--r--   0 trjose     (501) staff       (20)     5404 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/reporting/report.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.279470 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:34:23.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1824 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      423 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/method.py
+-rw-r--r--   0 trjose     (501) staff       (20)      332 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/response.py
+-rw-r--r--   0 trjose     (501) staff       (20)     5987 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/rest_api/rest_api.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.281378 test_rest_api-0.0.0.0.19/test_rest_api/testing/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-11 07:03:23.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)     3904 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/bug.py
+-rw-r--r--   0 trjose     (501) staff       (20)    14232 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/decorator.py
+-rw-r--r--   0 trjose     (501) staff       (20)      863 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)    12307 2023-04-04 09:00:40.000000 test_rest_api-0.0.0.0.19/test_rest_api/testing/runner.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.284288 test_rest_api-0.0.0.0.19/test_rest_api/utils/
+-rw-r--r--   0 trjose     (501) staff       (20)        0 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/__init__.py
+-rw-r--r--   0 trjose     (501) staff       (20)      943 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/aiohttp_session.py
+-rw-r--r--   0 trjose     (501) staff       (20)      546 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/colors.py
+-rw-r--r--   0 trjose     (501) staff       (20)      247 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/decorator_hints.py
+-rw-r--r--   0 trjose     (501) staff       (20)     2027 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/error_msg.py
+-rw-r--r--   0 trjose     (501) staff       (20)     1127 2023-04-03 07:06:15.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/exception.py
+-rw-r--r--   0 trjose     (501) staff       (20)      606 2023-03-24 16:41:57.000000 test_rest_api-0.0.0.0.19/test_rest_api/utils/logger.py
+drwxr-xr-x   0 trjose     (501) staff       (20)        0 2023-04-07 06:37:18.273373 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/
+-rw-r--r--   0 trjose     (501) staff       (20)    19341 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/PKG-INFO
+-rw-r--r--   0 trjose     (501) staff       (20)     1175 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/SOURCES.txt
+-rw-r--r--   0 trjose     (501) staff       (20)        1 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/dependency_links.txt
+-rw-r--r--   0 trjose     (501) staff       (20)       29 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/requires.txt
+-rw-r--r--   0 trjose     (501) staff       (20)       14 2023-04-07 06:37:18.000000 test_rest_api-0.0.0.0.19/test_rest_api.egg-info/top_level.txt
```

### Comparing `test_rest_api-0.0.0.0.18/LICENSE` & `test_rest_api-0.0.0.0.19/LICENSE`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/PKG-INFO` & `test_rest_api-0.0.0.0.19/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: test_rest_api
-Version: 0.0.0.0.18
+Version: 0.0.0.0.19
 Summary: Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests
 Author: Troy M Jose
 Author-email: 
 Keywords: test,unittest,restapi,testframework,asyncio,async,asynchronous,testingframework,rest,api,python,python3,testing,unittesting,automation,automationtest,automationtesting,restapitest,restapitesting,restapiunittest,restapiunittesting,restapiautomation,restapiautomationtest,restapiautomationtesting,apitest,apitesting,apiunittest,apiunittesting,apiautomation,apiautomationtest,apiautomationtesting
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -74,63 +74,60 @@
 
 If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:
 
 ```pip install test_rest_api```
 
 <h2 id="usage">Usage</h2>
 
-
-- - -
-
 <h4 id="1-basic-usage">1. Basic usage</h4>
 
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" ```
 
 - Tests are executed from the __command line__ using the test_rest_api module directly
 - The basic usage is by giving a __file path__ or __directory path__ as an argument
 - __-t__ stands for Test suite path
 - We can __organise__ folders, sub folders and python files in any __custom__ structure
 - test_rest_api will __autodetect__ python files and folders as __Test suites__
 
-- - -
 <h4 id="2-set-report-path">2. Set report path</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" ```
 
 - In the above example, __html test report__ is saved under the same test folder path
 - We can save the final report to our __custom path__ by providing __-r__ followed by path
 - __-r__ stands for Report path
 - test_rest_api __creates__ beautiful rich test report with summary dashboards
 - We can also add our __custom logs__ to each individual tests in the test report
 
-- - -
 <h4 id="3-set-env-path">3. Set .env path</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" ```
 
 - We can __set variables__ with values, example Domain, Username, Password etc. in __.env file__
 - test_rest_api will __auto fetch__ all these values and save under __Global Variables__ as constants
 - Global Variables can be accessed in tests for __parametrization__
 - One example can be __dynamic__ url creation. Domain can be __parameterised__ in url creation
 - This will also help developers to run the same tests in __different environments__ by creating separate .env files
 - We can __set__ the environment variables by providing __-e__ followed by path
 - __-e__ stands for Environment path
 
-- - -
 <h4 id="4-set-hashtags">4. Set hashtags</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" -h #SMOKE```
 
 - __Group__ your test by providing tags in test creation
@@ -144,16 +141,17 @@
 - In this case it's not practical to add all tags to the login test function
 - Adding __all tags__ will be hard to maintain when we introduce new custom tags
 - To tackle this issue, we can use inbuilt __#ALL tag__
 - __#ALL__ tagged tests will always be executed. It will not be skipped
 - Tests like login, logout etc. are __perfect candidates__ for #ALL
 
 <h2 id="examples">Examples</h2>
-- - -
+
 <h4 id="1-my-first-test">1. My first test</h4>
+
 - - -
 
 ```python
 from test_rest_api import test
 
 
 @test()
@@ -176,16 +174,16 @@
   python [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
 - Install __test_rest_api__ using __command__ ```pip install test_rest_api```
 - Create new python file (eg: __my_first_testsuite.py__) and paste the above code
 - Execute the test from the __command line__ using the test_rest_api module directly
 
 ``` python -m test_rest_api -t "test file path" -r "result folder path"```
 
-- - -
 <h4 id="2-configure-my-test">2. Configure my test</h4>
+
 - - -
 
 ```python
 from test_rest_api import test
 
 
 @test(name='Custom Name', desc='Description', enabled=True, tags=['SMOKE', 'ABC'], is_async=True, execution_order='1')
@@ -225,16 +223,16 @@
     - Default: True
 - __execution_order__
     - Mandatory: False
     - Data Type: str
     - Expected: Custom text for ordering. This will work only when is_async = False
     - Default: 'zzzzz'
 
-- - -
 <h4 id="3-my-first-logger">3. My first logger</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Logger
 
 
 @test()
@@ -248,16 +246,16 @@
 - Loggers are used to add __custom messages__ to the final html test report
 - Create a new Logger __instance__ inside your test function```logger = Logger()```
 - Logger instance __name__ can be any custom text. Here we have used __logger__
 - Add any number of log messages using __log method__ ```logger.log("my 1st log")```
 - Return logger instance for rich test __reporting__ ```return logger```
 - It is __recommended__ to use logger for all your tests
 
-- - -
 <h4 id="4-set-global-variables-value">4. Set global variables value</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -278,16 +276,16 @@
     - Data Type: str
     - Expected: Custom name for your global variable
 - __value__
     - Mandatory: True
     - Data Type: any
     - Expected: Any python data type can be stored as global variables value
 
-- - -
 <h4 id="5-set-global-variables-value-as-constant">5. Set global variables value as constant</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -313,16 +311,16 @@
     - Expected: Any python data type can be stored as global variables value
 - __is_constant__
     - Mandatory: False
     - Data Type: bool
     - Expected: True or False. Provide True, to create constants
     - Default: False
 
-- - -
 <h4 id="6-get-global-variables-value">6. Get global variables value</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -339,16 +337,16 @@
 ```GlobalVariables.get(name='token')```
 
 - __name__
     - Mandatory: True
     - Data Type: str
     - Expected: Valid name of any saved global variable
 
-- - -
 <h4 id="7-my-first-bug">7. My first bug</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Bug
 
 
 @test()
@@ -358,16 +356,16 @@
 
 - Bug is used to __raise issues__ in tests
 - Add custom __checks__ in your tests to validate __rest api response__
 - If __actual result__ is not the __expected result__, just call ```Bug()```
 - This will __terminate__ the current test function execution
 - Bug __details__ can be viewed in final html test __report__
 
-- - -
 <h4 id="8-configure-my-bug">8. Configure my bug</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Bug, Logger
 
 
 @test()
@@ -408,16 +406,16 @@
     - Default: Empty list
 - __steps_to_reproduce__
     - Mandatory: False
     - Data Type: str
     - Expected: Logger instance can be used to auto-populate this field
     - Default: Empty string
 
-- - -
 <h4 id="9-my-first-rest-api">9. My first rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -426,16 +424,16 @@
 ```
 
 - RestApi is used __create__ rest api instance in tests
 - Here we have created a basic rest api with just the __url information__
 - This example is only about creating rest api, no __send action__ is performed here
 - We will use this __instance variable__ for sending the request in upcoming examples
 
-- - -
 <h4 id="10-configure-my-rest-api">10. Configure my rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -464,16 +462,16 @@
     - Default: {}
 - __body__
     - Mandatory: False
     - Data Type: dict
     - Expected: Provide the json request payload
     - Default: {}
 
-- - -
 <h4 id="11-send-my-rest-api">11. Send my rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -488,16 +486,16 @@
 - Now it's time to __send__ them using http methods
 - __Supported__ http methods are GET, POST, PUT, PATCH, DELETE, OPTIONS & HEAD
 - Here we are sending the rest_api using __GET__ http method
 - All the responses (1, 2 & 3) will have the __same result__
 - Because they perform the same functionality with __different syntax__
 - Similarly, __other http methods__ can be used, with your desired syntax
 
-- - -
 <h4 id="12-rest-api-response">12. Rest api response</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -530,16 +528,16 @@
 - __response.content_type__
     - Data Type: str
     - Value: Response content type
 - __response.obj__
     - Data Type: aiohttp.ClientResponse
     - Value: Python aiohttp ClientResponse object
 
-- - -
 <h4 id="13-demo">13. Demo with all the above features</h4>
+
 - - -
 
 ```
 .env file
 ---------
 
 DOMAIN=dummyjson.com
```

### Comparing `test_rest_api-0.0.0.0.18/README.md` & `test_rest_api-0.0.0.0.19/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -46,63 +46,60 @@
 
 If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:
 
 ```pip install test_rest_api```
 
 <h2 id="usage">Usage</h2>
 
-
-- - -
-
 <h4 id="1-basic-usage">1. Basic usage</h4>
 
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" ```
 
 - Tests are executed from the __command line__ using the test_rest_api module directly
 - The basic usage is by giving a __file path__ or __directory path__ as an argument
 - __-t__ stands for Test suite path
 - We can __organise__ folders, sub folders and python files in any __custom__ structure
 - test_rest_api will __autodetect__ python files and folders as __Test suites__
 
-- - -
 <h4 id="2-set-report-path">2. Set report path</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" ```
 
 - In the above example, __html test report__ is saved under the same test folder path
 - We can save the final report to our __custom path__ by providing __-r__ followed by path
 - __-r__ stands for Report path
 - test_rest_api __creates__ beautiful rich test report with summary dashboards
 - We can also add our __custom logs__ to each individual tests in the test report
 
-- - -
 <h4 id="3-set-env-path">3. Set .env path</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" ```
 
 - We can __set variables__ with values, example Domain, Username, Password etc. in __.env file__
 - test_rest_api will __auto fetch__ all these values and save under __Global Variables__ as constants
 - Global Variables can be accessed in tests for __parametrization__
 - One example can be __dynamic__ url creation. Domain can be __parameterised__ in url creation
 - This will also help developers to run the same tests in __different environments__ by creating separate .env files
 - We can __set__ the environment variables by providing __-e__ followed by path
 - __-e__ stands for Environment path
 
-- - -
 <h4 id="4-set-hashtags">4. Set hashtags</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" -h #SMOKE```
 
 - __Group__ your test by providing tags in test creation
@@ -116,16 +113,17 @@
 - In this case it's not practical to add all tags to the login test function
 - Adding __all tags__ will be hard to maintain when we introduce new custom tags
 - To tackle this issue, we can use inbuilt __#ALL tag__
 - __#ALL__ tagged tests will always be executed. It will not be skipped
 - Tests like login, logout etc. are __perfect candidates__ for #ALL
 
 <h2 id="examples">Examples</h2>
-- - -
+
 <h4 id="1-my-first-test">1. My first test</h4>
+
 - - -
 
 ```python
 from test_rest_api import test
 
 
 @test()
@@ -148,16 +146,16 @@
   python [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
 - Install __test_rest_api__ using __command__ ```pip install test_rest_api```
 - Create new python file (eg: __my_first_testsuite.py__) and paste the above code
 - Execute the test from the __command line__ using the test_rest_api module directly
 
 ``` python -m test_rest_api -t "test file path" -r "result folder path"```
 
-- - -
 <h4 id="2-configure-my-test">2. Configure my test</h4>
+
 - - -
 
 ```python
 from test_rest_api import test
 
 
 @test(name='Custom Name', desc='Description', enabled=True, tags=['SMOKE', 'ABC'], is_async=True, execution_order='1')
@@ -197,16 +195,16 @@
     - Default: True
 - __execution_order__
     - Mandatory: False
     - Data Type: str
     - Expected: Custom text for ordering. This will work only when is_async = False
     - Default: 'zzzzz'
 
-- - -
 <h4 id="3-my-first-logger">3. My first logger</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Logger
 
 
 @test()
@@ -220,16 +218,16 @@
 - Loggers are used to add __custom messages__ to the final html test report
 - Create a new Logger __instance__ inside your test function```logger = Logger()```
 - Logger instance __name__ can be any custom text. Here we have used __logger__
 - Add any number of log messages using __log method__ ```logger.log("my 1st log")```
 - Return logger instance for rich test __reporting__ ```return logger```
 - It is __recommended__ to use logger for all your tests
 
-- - -
 <h4 id="4-set-global-variables-value">4. Set global variables value</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -250,16 +248,16 @@
     - Data Type: str
     - Expected: Custom name for your global variable
 - __value__
     - Mandatory: True
     - Data Type: any
     - Expected: Any python data type can be stored as global variables value
 
-- - -
 <h4 id="5-set-global-variables-value-as-constant">5. Set global variables value as constant</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -285,16 +283,16 @@
     - Expected: Any python data type can be stored as global variables value
 - __is_constant__
     - Mandatory: False
     - Data Type: bool
     - Expected: True or False. Provide True, to create constants
     - Default: False
 
-- - -
 <h4 id="6-get-global-variables-value">6. Get global variables value</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -311,16 +309,16 @@
 ```GlobalVariables.get(name='token')```
 
 - __name__
     - Mandatory: True
     - Data Type: str
     - Expected: Valid name of any saved global variable
 
-- - -
 <h4 id="7-my-first-bug">7. My first bug</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Bug
 
 
 @test()
@@ -330,16 +328,16 @@
 
 - Bug is used to __raise issues__ in tests
 - Add custom __checks__ in your tests to validate __rest api response__
 - If __actual result__ is not the __expected result__, just call ```Bug()```
 - This will __terminate__ the current test function execution
 - Bug __details__ can be viewed in final html test __report__
 
-- - -
 <h4 id="8-configure-my-bug">8. Configure my bug</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Bug, Logger
 
 
 @test()
@@ -380,16 +378,16 @@
     - Default: Empty list
 - __steps_to_reproduce__
     - Mandatory: False
     - Data Type: str
     - Expected: Logger instance can be used to auto-populate this field
     - Default: Empty string
 
-- - -
 <h4 id="9-my-first-rest-api">9. My first rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -398,16 +396,16 @@
 ```
 
 - RestApi is used __create__ rest api instance in tests
 - Here we have created a basic rest api with just the __url information__
 - This example is only about creating rest api, no __send action__ is performed here
 - We will use this __instance variable__ for sending the request in upcoming examples
 
-- - -
 <h4 id="10-configure-my-rest-api">10. Configure my rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -436,16 +434,16 @@
     - Default: {}
 - __body__
     - Mandatory: False
     - Data Type: dict
     - Expected: Provide the json request payload
     - Default: {}
 
-- - -
 <h4 id="11-send-my-rest-api">11. Send my rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -460,16 +458,16 @@
 - Now it's time to __send__ them using http methods
 - __Supported__ http methods are GET, POST, PUT, PATCH, DELETE, OPTIONS & HEAD
 - Here we are sending the rest_api using __GET__ http method
 - All the responses (1, 2 & 3) will have the __same result__
 - Because they perform the same functionality with __different syntax__
 - Similarly, __other http methods__ can be used, with your desired syntax
 
-- - -
 <h4 id="12-rest-api-response">12. Rest api response</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -502,16 +500,16 @@
 - __response.content_type__
     - Data Type: str
     - Value: Response content type
 - __response.obj__
     - Data Type: aiohttp.ClientResponse
     - Value: Python aiohttp ClientResponse object
 
-- - -
 <h4 id="13-demo">13. Demo with all the above features</h4>
+
 - - -
 
 ```
 .env file
 ---------
 
 DOMAIN=dummyjson.com
```

### Comparing `test_rest_api-0.0.0.0.18/setup.py` & `test_rest_api-0.0.0.0.19/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 
 # Get README.md details
 with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
     long_description = "\n" + f.read()
 
 # Setup
 setup(name="test_rest_api",
-      version="0.0.0.0.18",
+      version="0.0.0.0.19",
       author="Troy M Jose",
       author_email="",
       description="Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests",
       keywords=['test', 'unittest', 'restapi', 'testframework', 'asyncio', 'async', 'asynchronous',
                 'testingframework', 'rest', 'api', 'python', 'python3', 'testing', 'unittesting', 'automation',
                 'automationtest', 'automationtesting',
                 'restapitest', 'restapitesting', 'restapiunittest', 'restapiunittesting', 'restapiautomation',
```

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/__main__.py` & `test_rest_api-0.0.0.0.19/test_rest_api/__main__.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/global_variables/exception.py` & `test_rest_api-0.0.0.0.19/test_rest_api/global_variables/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/global_variables/global_variables.py` & `test_rest_api-0.0.0.0.19/test_rest_api/global_variables/global_variables.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/logger/exception.py` & `test_rest_api-0.0.0.0.19/test_rest_api/logger/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/logger/logger.py` & `test_rest_api-0.0.0.0.19/test_rest_api/logger/logger.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/reporting/html.py` & `test_rest_api-0.0.0.0.19/test_rest_api/reporting/html.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/reporting/report.py` & `test_rest_api-0.0.0.0.19/test_rest_api/reporting/report.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/rest_api/exception.py` & `test_rest_api-0.0.0.0.19/test_rest_api/rest_api/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/rest_api/rest_api.py` & `test_rest_api-0.0.0.0.19/test_rest_api/rest_api/rest_api.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/testing/bug.py` & `test_rest_api-0.0.0.0.19/test_rest_api/testing/bug.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/testing/decorator.py` & `test_rest_api-0.0.0.0.19/test_rest_api/testing/decorator.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/testing/exception.py` & `test_rest_api-0.0.0.0.19/test_rest_api/testing/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/testing/runner.py` & `test_rest_api-0.0.0.0.19/test_rest_api/testing/runner.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/utils/aiohttp_session.py` & `test_rest_api-0.0.0.0.19/test_rest_api/utils/aiohttp_session.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/utils/colors.py` & `test_rest_api-0.0.0.0.19/test_rest_api/utils/colors.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/utils/error_msg.py` & `test_rest_api-0.0.0.0.19/test_rest_api/utils/error_msg.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/utils/exception.py` & `test_rest_api-0.0.0.0.19/test_rest_api/utils/exception.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api/utils/logger.py` & `test_rest_api-0.0.0.0.19/test_rest_api/utils/logger.py`

 * *Files identical despite different names*

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api.egg-info/PKG-INFO` & `test_rest_api-0.0.0.0.19/test_rest_api.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: test-rest-api
-Version: 0.0.0.0.18
+Version: 0.0.0.0.19
 Summary: Asynchronous Test Framework #HighPerformance #EasyToLearn #FastToCode #AsyncTests
 Author: Troy M Jose
 Author-email: 
 Keywords: test,unittest,restapi,testframework,asyncio,async,asynchronous,testingframework,rest,api,python,python3,testing,unittesting,automation,automationtest,automationtesting,restapitest,restapitesting,restapiunittest,restapiunittesting,restapiautomation,restapiautomationtest,restapiautomationtesting,apitest,apitesting,apiunittest,apiunittesting,apiautomation,apiautomationtest,apiautomationtesting
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -74,63 +74,60 @@
 
 If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:
 
 ```pip install test_rest_api```
 
 <h2 id="usage">Usage</h2>
 
-
-- - -
-
 <h4 id="1-basic-usage">1. Basic usage</h4>
 
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" ```
 
 - Tests are executed from the __command line__ using the test_rest_api module directly
 - The basic usage is by giving a __file path__ or __directory path__ as an argument
 - __-t__ stands for Test suite path
 - We can __organise__ folders, sub folders and python files in any __custom__ structure
 - test_rest_api will __autodetect__ python files and folders as __Test suites__
 
-- - -
 <h4 id="2-set-report-path">2. Set report path</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" ```
 
 - In the above example, __html test report__ is saved under the same test folder path
 - We can save the final report to our __custom path__ by providing __-r__ followed by path
 - __-r__ stands for Report path
 - test_rest_api __creates__ beautiful rich test report with summary dashboards
 - We can also add our __custom logs__ to each individual tests in the test report
 
-- - -
 <h4 id="3-set-env-path">3. Set .env path</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" ```
 
 - We can __set variables__ with values, example Domain, Username, Password etc. in __.env file__
 - test_rest_api will __auto fetch__ all these values and save under __Global Variables__ as constants
 - Global Variables can be accessed in tests for __parametrization__
 - One example can be __dynamic__ url creation. Domain can be __parameterised__ in url creation
 - This will also help developers to run the same tests in __different environments__ by creating separate .env files
 - We can __set__ the environment variables by providing __-e__ followed by path
 - __-e__ stands for Environment path
 
-- - -
 <h4 id="4-set-hashtags">4. Set hashtags</h4>
+
 - - -
 
 __Syntax__
 
 ``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" -h #SMOKE```
 
 - __Group__ your test by providing tags in test creation
@@ -144,16 +141,17 @@
 - In this case it's not practical to add all tags to the login test function
 - Adding __all tags__ will be hard to maintain when we introduce new custom tags
 - To tackle this issue, we can use inbuilt __#ALL tag__
 - __#ALL__ tagged tests will always be executed. It will not be skipped
 - Tests like login, logout etc. are __perfect candidates__ for #ALL
 
 <h2 id="examples">Examples</h2>
-- - -
+
 <h4 id="1-my-first-test">1. My first test</h4>
+
 - - -
 
 ```python
 from test_rest_api import test
 
 
 @test()
@@ -176,16 +174,16 @@
   python [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
 - Install __test_rest_api__ using __command__ ```pip install test_rest_api```
 - Create new python file (eg: __my_first_testsuite.py__) and paste the above code
 - Execute the test from the __command line__ using the test_rest_api module directly
 
 ``` python -m test_rest_api -t "test file path" -r "result folder path"```
 
-- - -
 <h4 id="2-configure-my-test">2. Configure my test</h4>
+
 - - -
 
 ```python
 from test_rest_api import test
 
 
 @test(name='Custom Name', desc='Description', enabled=True, tags=['SMOKE', 'ABC'], is_async=True, execution_order='1')
@@ -225,16 +223,16 @@
     - Default: True
 - __execution_order__
     - Mandatory: False
     - Data Type: str
     - Expected: Custom text for ordering. This will work only when is_async = False
     - Default: 'zzzzz'
 
-- - -
 <h4 id="3-my-first-logger">3. My first logger</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Logger
 
 
 @test()
@@ -248,16 +246,16 @@
 - Loggers are used to add __custom messages__ to the final html test report
 - Create a new Logger __instance__ inside your test function```logger = Logger()```
 - Logger instance __name__ can be any custom text. Here we have used __logger__
 - Add any number of log messages using __log method__ ```logger.log("my 1st log")```
 - Return logger instance for rich test __reporting__ ```return logger```
 - It is __recommended__ to use logger for all your tests
 
-- - -
 <h4 id="4-set-global-variables-value">4. Set global variables value</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -278,16 +276,16 @@
     - Data Type: str
     - Expected: Custom name for your global variable
 - __value__
     - Mandatory: True
     - Data Type: any
     - Expected: Any python data type can be stored as global variables value
 
-- - -
 <h4 id="5-set-global-variables-value-as-constant">5. Set global variables value as constant</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -313,16 +311,16 @@
     - Expected: Any python data type can be stored as global variables value
 - __is_constant__
     - Mandatory: False
     - Data Type: bool
     - Expected: True or False. Provide True, to create constants
     - Default: False
 
-- - -
 <h4 id="6-get-global-variables-value">6. Get global variables value</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, GlobalVariables
 
 
 @test()
@@ -339,16 +337,16 @@
 ```GlobalVariables.get(name='token')```
 
 - __name__
     - Mandatory: True
     - Data Type: str
     - Expected: Valid name of any saved global variable
 
-- - -
 <h4 id="7-my-first-bug">7. My first bug</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Bug
 
 
 @test()
@@ -358,16 +356,16 @@
 
 - Bug is used to __raise issues__ in tests
 - Add custom __checks__ in your tests to validate __rest api response__
 - If __actual result__ is not the __expected result__, just call ```Bug()```
 - This will __terminate__ the current test function execution
 - Bug __details__ can be viewed in final html test __report__
 
-- - -
 <h4 id="8-configure-my-bug">8. Configure my bug</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, Bug, Logger
 
 
 @test()
@@ -408,16 +406,16 @@
     - Default: Empty list
 - __steps_to_reproduce__
     - Mandatory: False
     - Data Type: str
     - Expected: Logger instance can be used to auto-populate this field
     - Default: Empty string
 
-- - -
 <h4 id="9-my-first-rest-api">9. My first rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -426,16 +424,16 @@
 ```
 
 - RestApi is used __create__ rest api instance in tests
 - Here we have created a basic rest api with just the __url information__
 - This example is only about creating rest api, no __send action__ is performed here
 - We will use this __instance variable__ for sending the request in upcoming examples
 
-- - -
 <h4 id="10-configure-my-rest-api">10. Configure my rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -464,16 +462,16 @@
     - Default: {}
 - __body__
     - Mandatory: False
     - Data Type: dict
     - Expected: Provide the json request payload
     - Default: {}
 
-- - -
 <h4 id="11-send-my-rest-api">11. Send my rest api</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -488,16 +486,16 @@
 - Now it's time to __send__ them using http methods
 - __Supported__ http methods are GET, POST, PUT, PATCH, DELETE, OPTIONS & HEAD
 - Here we are sending the rest_api using __GET__ http method
 - All the responses (1, 2 & 3) will have the __same result__
 - Because they perform the same functionality with __different syntax__
 - Similarly, __other http methods__ can be used, with your desired syntax
 
-- - -
 <h4 id="12-rest-api-response">12. Rest api response</h4>
+
 - - -
 
 ```python
 from test_rest_api import test, RestApi
 
 
 @test()
@@ -530,16 +528,16 @@
 - __response.content_type__
     - Data Type: str
     - Value: Response content type
 - __response.obj__
     - Data Type: aiohttp.ClientResponse
     - Value: Python aiohttp ClientResponse object
 
-- - -
 <h4 id="13-demo">13. Demo with all the above features</h4>
+
 - - -
 
 ```
 .env file
 ---------
 
 DOMAIN=dummyjson.com
```

### Comparing `test_rest_api-0.0.0.0.18/test_rest_api.egg-info/SOURCES.txt` & `test_rest_api-0.0.0.0.19/test_rest_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

