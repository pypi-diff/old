# Comparing `tmp/scrapeanything-0.9.98.tar.gz` & `tmp/scrapeanything-0.9.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "scrapeanything-0.9.98.tar", last modified: Wed Jul 27 08:23:24 2022, max compression
+gzip compressed data, was "scrapeanything-0.9.99.tar", last modified: Wed Jul 27 09:25:00 2022, max compression
```

## Comparing `scrapeanything-0.9.98.tar` & `scrapeanything-0.9.99.tar`

### file list

```diff
@@ -1,43 +1,43 @@
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.434148 scrapeanything-0.9.98/
--rw-rw-rw-   0        0        0     1091 2022-02-28 22:56:57.000000 scrapeanything-0.9.98/LICENSE
--rw-rw-rw-   0        0        0      945 2022-07-27 08:23:24.435148 scrapeanything-0.9.98/PKG-INFO
--rw-rw-rw-   0        0        0      336 2022-03-16 11:25:31.000000 scrapeanything-0.9.98/README.md
--rw-rw-rw-   0        0        0      108 2022-02-28 22:54:46.000000 scrapeanything-0.9.98/pyproject.toml
--rw-rw-rw-   0        0        0     1003 2022-07-27 08:23:24.437160 scrapeanything-0.9.98/setup.cfg
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.307998 scrapeanything-0.9.98/src/
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.328995 scrapeanything-0.9.98/src/scrapeanything/
--rw-rw-rw-   0        0        0        0 2022-02-28 22:52:42.000000 scrapeanything-0.9.98/src/scrapeanything/__init__.py
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.357994 scrapeanything-0.9.98/src/scrapeanything/database/
--rw-rw-rw-   0        0        0        0 2022-03-01 17:28:40.000000 scrapeanything-0.9.98/src/scrapeanything/database/__init__.py
--rw-rw-rw-   0        0        0      582 2022-04-23 12:39:39.000000 scrapeanything-0.9.98/src/scrapeanything/database/connection.py
--rw-rw-rw-   0        0        0      941 2022-03-09 20:51:15.000000 scrapeanything-0.9.98/src/scrapeanything/database/models.py
--rw-rw-rw-   0        0        0    12108 2022-06-17 09:05:59.000000 scrapeanything-0.9.98/src/scrapeanything/database/repository.py
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.373149 scrapeanything-0.9.98/src/scrapeanything/integration/
--rw-rw-rw-   0        0        0        0 2022-03-01 17:28:46.000000 scrapeanything-0.9.98/src/scrapeanything/integration/__init__.py
--rw-rw-rw-   0        0        0      301 2022-03-01 15:45:25.000000 scrapeanything-0.9.98/src/scrapeanything/integration/csv.py
--rw-rw-rw-   0        0        0     5172 2022-03-01 15:45:55.000000 scrapeanything-0.9.98/src/scrapeanything/integration/excel.py
--rw-rw-rw-   0        0        0      152 2022-03-01 15:46:11.000000 scrapeanything-0.9.98/src/scrapeanything/integration/spreadsheet.py
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.383151 scrapeanything-0.9.98/src/scrapeanything/scraper/
--rw-rw-rw-   0        0        0        0 2022-03-01 17:28:21.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/__init__.py
--rw-rw-rw-   0        0        0     3688 2022-07-27 08:22:03.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/parser.py
--rw-rw-rw-   0        0        0     9090 2022-07-17 11:55:18.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/scraper.py
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.400181 scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/
--rw-rw-rw-   0        0        0        0 2022-03-01 17:28:31.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/__init__.py
--rw-rw-rw-   0        0        0      968 2022-03-01 15:52:09.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/requests.py
--rw-rw-rw-   0        0        0      994 2022-03-01 15:52:31.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/requests_html.py
--rw-rw-rw-   0        0        0     9901 2022-07-27 08:19:59.000000 scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/selenium.py
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.431148 scrapeanything-0.9.98/src/scrapeanything/utils/
--rw-rw-rw-   0        0        0        0 2022-03-01 17:28:56.000000 scrapeanything-0.9.98/src/scrapeanything/utils/__init__.py
--rw-rw-rw-   0        0        0      892 2022-06-14 20:30:54.000000 scrapeanything-0.9.98/src/scrapeanything/utils/config.py
--rw-rw-rw-   0        0        0      988 2022-03-26 12:29:27.000000 scrapeanything-0.9.98/src/scrapeanything/utils/constants.py
--rw-rw-rw-   0        0        0     2243 2022-03-01 15:55:57.000000 scrapeanything-0.9.98/src/scrapeanything/utils/dates.py
--rw-rw-rw-   0        0        0     2229 2022-03-01 15:56:07.000000 scrapeanything-0.9.98/src/scrapeanything/utils/log.py
--rw-rw-rw-   0        0        0     1232 2022-04-16 07:47:23.000000 scrapeanything-0.9.98/src/scrapeanything/utils/service.py
--rw-rw-rw-   0        0        0     2826 2022-03-26 22:30:24.000000 scrapeanything-0.9.98/src/scrapeanything/utils/types.py
--rw-rw-rw-   0        0        0     2280 2022-03-01 15:56:39.000000 scrapeanything-0.9.98/src/scrapeanything/utils/utils.py
-drwxrwxrwx   0        0        0        0 2022-07-27 08:23:24.344996 scrapeanything-0.9.98/src/scrapeanything.egg-info/
--rw-rw-rw-   0        0        0      945 2022-07-27 08:23:24.000000 scrapeanything-0.9.98/src/scrapeanything.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1202 2022-07-27 08:23:24.000000 scrapeanything-0.9.98/src/scrapeanything.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-07-27 08:23:24.000000 scrapeanything-0.9.98/src/scrapeanything.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      198 2022-07-27 08:23:24.000000 scrapeanything-0.9.98/src/scrapeanything.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2022-07-27 08:23:24.000000 scrapeanything-0.9.98/src/scrapeanything.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.764942 scrapeanything-0.9.99/
+-rw-rw-rw-   0        0        0     1091 2022-02-28 22:56:57.000000 scrapeanything-0.9.99/LICENSE
+-rw-rw-rw-   0        0        0      945 2022-07-27 09:25:00.765941 scrapeanything-0.9.99/PKG-INFO
+-rw-rw-rw-   0        0        0      336 2022-03-16 11:25:31.000000 scrapeanything-0.9.99/README.md
+-rw-rw-rw-   0        0        0      108 2022-02-28 22:54:46.000000 scrapeanything-0.9.99/pyproject.toml
+-rw-rw-rw-   0        0        0     1003 2022-07-27 09:25:00.767944 scrapeanything-0.9.99/setup.cfg
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.654048 scrapeanything-0.9.99/src/
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.672047 scrapeanything-0.9.99/src/scrapeanything/
+-rw-rw-rw-   0        0        0        0 2022-02-28 22:52:42.000000 scrapeanything-0.9.99/src/scrapeanything/__init__.py
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.699046 scrapeanything-0.9.99/src/scrapeanything/database/
+-rw-rw-rw-   0        0        0        0 2022-03-01 17:28:40.000000 scrapeanything-0.9.99/src/scrapeanything/database/__init__.py
+-rw-rw-rw-   0        0        0      582 2022-04-23 12:39:39.000000 scrapeanything-0.9.99/src/scrapeanything/database/connection.py
+-rw-rw-rw-   0        0        0      941 2022-03-09 20:51:15.000000 scrapeanything-0.9.99/src/scrapeanything/database/models.py
+-rw-rw-rw-   0        0        0    12108 2022-06-17 09:05:59.000000 scrapeanything-0.9.99/src/scrapeanything/database/repository.py
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.713082 scrapeanything-0.9.99/src/scrapeanything/integration/
+-rw-rw-rw-   0        0        0        0 2022-03-01 17:28:46.000000 scrapeanything-0.9.99/src/scrapeanything/integration/__init__.py
+-rw-rw-rw-   0        0        0      301 2022-03-01 15:45:25.000000 scrapeanything-0.9.99/src/scrapeanything/integration/csv.py
+-rw-rw-rw-   0        0        0     5172 2022-03-01 15:45:55.000000 scrapeanything-0.9.99/src/scrapeanything/integration/excel.py
+-rw-rw-rw-   0        0        0      152 2022-03-01 15:46:11.000000 scrapeanything-0.9.99/src/scrapeanything/integration/spreadsheet.py
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.724949 scrapeanything-0.9.99/src/scrapeanything/scraper/
+-rw-rw-rw-   0        0        0        0 2022-03-01 17:28:21.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/__init__.py
+-rw-rw-rw-   0        0        0     3688 2022-07-27 08:22:03.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/parser.py
+-rw-rw-rw-   0        0        0     9090 2022-07-17 11:55:18.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/scraper.py
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.737943 scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/
+-rw-rw-rw-   0        0        0        0 2022-03-01 17:28:31.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/__init__.py
+-rw-rw-rw-   0        0        0      968 2022-03-01 15:52:09.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/requests.py
+-rw-rw-rw-   0        0        0      994 2022-03-01 15:52:31.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/requests_html.py
+-rw-rw-rw-   0        0        0    10389 2022-07-27 09:23:30.000000 scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/selenium.py
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.762943 scrapeanything-0.9.99/src/scrapeanything/utils/
+-rw-rw-rw-   0        0        0        0 2022-03-01 17:28:56.000000 scrapeanything-0.9.99/src/scrapeanything/utils/__init__.py
+-rw-rw-rw-   0        0        0      892 2022-06-14 20:30:54.000000 scrapeanything-0.9.99/src/scrapeanything/utils/config.py
+-rw-rw-rw-   0        0        0      988 2022-03-26 12:29:27.000000 scrapeanything-0.9.99/src/scrapeanything/utils/constants.py
+-rw-rw-rw-   0        0        0     2243 2022-03-01 15:55:57.000000 scrapeanything-0.9.99/src/scrapeanything/utils/dates.py
+-rw-rw-rw-   0        0        0     2229 2022-03-01 15:56:07.000000 scrapeanything-0.9.99/src/scrapeanything/utils/log.py
+-rw-rw-rw-   0        0        0     1232 2022-04-16 07:47:23.000000 scrapeanything-0.9.99/src/scrapeanything/utils/service.py
+-rw-rw-rw-   0        0        0     2826 2022-03-26 22:30:24.000000 scrapeanything-0.9.99/src/scrapeanything/utils/types.py
+-rw-rw-rw-   0        0        0     2280 2022-03-01 15:56:39.000000 scrapeanything-0.9.99/src/scrapeanything/utils/utils.py
+drwxrwxrwx   0        0        0        0 2022-07-27 09:25:00.688046 scrapeanything-0.9.99/src/scrapeanything.egg-info/
+-rw-rw-rw-   0        0        0      945 2022-07-27 09:25:00.000000 scrapeanything-0.9.99/src/scrapeanything.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1202 2022-07-27 09:25:00.000000 scrapeanything-0.9.99/src/scrapeanything.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2022-07-27 09:25:00.000000 scrapeanything-0.9.99/src/scrapeanything.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      198 2022-07-27 09:25:00.000000 scrapeanything-0.9.99/src/scrapeanything.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2022-07-27 09:25:00.000000 scrapeanything-0.9.99/src/scrapeanything.egg-info/top_level.txt
```

### Comparing `scrapeanything-0.9.98/LICENSE` & `scrapeanything-0.9.99/LICENSE`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/PKG-INFO` & `scrapeanything-0.9.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scrapeanything
-Version: 0.9.98
+Version: 0.9.99
 Summary: Library to scrape data from the internet and persist it easier
 Home-page: https://bitbucket.org/scrapeanything-ml/scrapeanything.ml
 Author: Giuseppe Gargiuolo
 Author-email: giuseppegargiuolo@gmail.com
 Project-URL: Bug Tracker, https://bitbucket.org/scrapeanything-ml/scrapeanything.ml/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `scrapeanything-0.9.98/setup.cfg` & `scrapeanything-0.9.99/setup.cfg`

 * *Files 13% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 5b6d 6574 6164 6174 615d 0d0a 6e61 6d65  [metadata]..name
 00000010: 203d 2073 6372 6170 6561 6e79 7468 696e   = scrapeanythin
 00000020: 670d 0a76 6572 7369 6f6e 203d 2030 2e39  g..version = 0.9
-00000030: 2e39 380d 0a61 7574 686f 7220 3d20 4769  .98..author = Gi
+00000030: 2e39 390d 0a61 7574 686f 7220 3d20 4769  .99..author = Gi
 00000040: 7573 6570 7065 2047 6172 6769 756f 6c6f  useppe Gargiuolo
 00000050: 0d0a 6175 7468 6f72 5f65 6d61 696c 203d  ..author_email =
 00000060: 2067 6975 7365 7070 6567 6172 6769 756f   giuseppegargiuo
 00000070: 6c6f 4067 6d61 696c 2e63 6f6d 0d0a 6465  lo@gmail.com..de
 00000080: 7363 7269 7074 696f 6e20 3d20 4c69 6272  scription = Libr
 00000090: 6172 7920 746f 2073 6372 6170 6520 6461  ary to scrape da
 000000a0: 7461 2066 726f 6d20 7468 6520 696e 7465  ta from the inte
```

### Comparing `scrapeanything-0.9.98/src/scrapeanything/database/connection.py` & `scrapeanything-0.9.99/src/scrapeanything/database/connection.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/database/models.py` & `scrapeanything-0.9.99/src/scrapeanything/database/models.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/database/repository.py` & `scrapeanything-0.9.99/src/scrapeanything/database/repository.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/integration/excel.py` & `scrapeanything-0.9.99/src/scrapeanything/integration/excel.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/scraper/parser.py` & `scrapeanything-0.9.99/src/scrapeanything/scraper/parser.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/scraper/scraper.py` & `scrapeanything-0.9.99/src/scrapeanything/scraper/scraper.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/requests.py` & `scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/requests.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/requests_html.py` & `scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/requests_html.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/scraper/scrapers/selenium.py` & `scrapeanything-0.9.99/src/scrapeanything/scraper/scrapers/selenium.py`

 * *Files 15% similar despite different names*

```diff
@@ -11,26 +11,36 @@
 from selenium.webdriver.support import expected_conditions as EC
 from selenium.webdriver.common.keys import Keys
 from selenium.webdriver.support.ui import Select
 from selenium.common.exceptions import NoSuchElementException        
 from selenium.common.exceptions import StaleElementReferenceException
 from selenium.webdriver.common.action_chains import ActionChains
 from selenium.webdriver.remote.remote_connection import LOGGER
-from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
-from selenium.webdriver.chrome.options import Options
+import undetected_chromedriver.v2 as uc
 
 import logging
 import platform
 import base64
 
 class Selenium(Scraper):
 
     def __init__(self, config: Config, headless: bool=True, window: dict={}, user_dir: str=None):
 
-        options = webdriver.ChromeOptions()
+        if user_dir is None:
+            options = webdriver.ChromeOptions()
+        else:
+            options = uc.ChromeOptions()
+
+            # another way to set profile is the below (which takes precedence if both variants are used
+            options.add_argument(f'--user-data-dir={user_dir}')
+            # just some options passing in to skip annoying popups
+            options.add_argument('--no-first-run --no-service-autorun --password-store=basic')            
+
+        #Remove navigator.webdriver Flag using JavaScript
+        options.add_argument('--disable-blink-features=AutomationControlled')
 
         #region options
         options.add_argument('--no-sandbox')
         options.add_argument('--log-level=3')
         options.add_argument('disable-infobars')
         options.add_argument('--disable-extensions')
         options.add_argument('--disable-dev-shm-usage')
@@ -47,22 +57,21 @@
             options.add_argument('headless')
 
         LOGGER.setLevel(logging.WARNING)
 
         options.add_argument('--disable-blink-features=AutomationControlled')
         options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")
 
-        if user_dir is not None:
-            options.add_argument(f'user-data-dir={user_dir}')
-
         #endregion options
 
         url = config.get(section='SELENIUM', key='url')
 
-        if url is not None:
+        if user_dir is not None:
+            self.driver = uc.Chrome(options=options)            
+        elif url is not None:
             self.driver = webdriver.Remote(command_executor=f'{url}', desired_capabilities={'browserName': 'chrome'}, options=options)
         elif platform.system() == 'Windows':
             self.driver = webdriver.Chrome(executable_path='c:\chromedriver.exe', options=options)
         elif platform.system() == 'Linux':
             self.driver = webdriver.Chrome(executable_path='/chromedriver', options=options)
 
         if len(window_size) > 0:
```

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/config.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/config.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/constants.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/constants.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/dates.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/dates.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/log.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/log.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/service.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/service.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/types.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/types.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything/utils/utils.py` & `scrapeanything-0.9.99/src/scrapeanything/utils/utils.py`

 * *Files identical despite different names*

### Comparing `scrapeanything-0.9.98/src/scrapeanything.egg-info/PKG-INFO` & `scrapeanything-0.9.99/src/scrapeanything.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scrapeanything
-Version: 0.9.98
+Version: 0.9.99
 Summary: Library to scrape data from the internet and persist it easier
 Home-page: https://bitbucket.org/scrapeanything-ml/scrapeanything.ml
 Author: Giuseppe Gargiuolo
 Author-email: giuseppegargiuolo@gmail.com
 Project-URL: Bug Tracker, https://bitbucket.org/scrapeanything-ml/scrapeanything.ml/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `scrapeanything-0.9.98/src/scrapeanything.egg-info/SOURCES.txt` & `scrapeanything-0.9.99/src/scrapeanything.egg-info/SOURCES.txt`

 * *Files identical despite different names*

