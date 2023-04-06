# Comparing `tmp/visualtest_python-1.1.0-py3-none-any.whl.zip` & `tmp/visualtest_python-1.2.0-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,13 +1,14 @@
-Zip file size: 19909 bytes, number of entries: 11
--rw-r--r--  2.0 unx     1129 b- defN 23-Mar-24 18:57 sbvt/__init__.py
+Zip file size: 28537 bytes, number of entries: 12
+-rw-r--r--  2.0 unx     1129 b- defN 23-Apr-06 21:42 sbvt/__init__.py
 -rw-r--r--  2.0 unx     9191 b- defN 23-Mar-23 22:50 sbvt/api.py
--rw-r--r--  2.0 unx    33032 b- defN 23-Mar-24 00:28 sbvt/browser.py
+-rw-r--r--  2.0 unx    35553 b- defN 23-Apr-04 15:23 sbvt/browser-safari-bug-test.py
+-rw-r--r--  2.0 unx    33376 b- defN 23-Apr-06 21:42 sbvt/browser.py
 -rw-r--r--  2.0 unx     5981 b- defN 22-Sep-08 16:30 sbvt/imagetools.py
 -rw-r--r--  2.0 unx      548 b- defN 22-Sep-08 16:30 sbvt/timer.py
--rw-r--r--  2.0 unx     9871 b- defN 23-Mar-23 20:46 sbvt/visualtest.py
--rw-r--r--  2.0 unx     1073 b- defN 23-Mar-24 18:58 visualtest_python-1.1.0.dist-info/LICENSE
--rw-r--r--  2.0 unx     3872 b- defN 23-Mar-24 18:58 visualtest_python-1.1.0.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Mar-24 18:58 visualtest_python-1.1.0.dist-info/WHEEL
--rw-r--r--  2.0 unx        5 b- defN 23-Mar-24 18:58 visualtest_python-1.1.0.dist-info/top_level.txt
--rw-rw-r--  2.0 unx      868 b- defN 23-Mar-24 18:58 visualtest_python-1.1.0.dist-info/RECORD
-11 files, 65662 bytes uncompressed, 18451 bytes compressed:  71.9%
+-rw-r--r--  2.0 unx    10962 b- defN 23-Apr-06 21:41 sbvt/visualtest.py
+-rw-r--r--  2.0 unx     1073 b- defN 23-Apr-06 21:49 visualtest_python-1.2.0.dist-info/LICENSE
+-rw-r--r--  2.0 unx     3876 b- defN 23-Apr-06 21:49 visualtest_python-1.2.0.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-06 21:49 visualtest_python-1.2.0.dist-info/WHEEL
+-rw-r--r--  2.0 unx        5 b- defN 23-Apr-06 21:49 visualtest_python-1.2.0.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx      958 b- defN 23-Apr-06 21:49 visualtest_python-1.2.0.dist-info/RECORD
+12 files, 102744 bytes uncompressed, 26941 bytes compressed:  73.8%
```

## zipnote {}

```diff
@@ -1,34 +1,37 @@
 Filename: sbvt/__init__.py
 Comment: 
 
 Filename: sbvt/api.py
 Comment: 
 
+Filename: sbvt/browser-safari-bug-test.py
+Comment: 
+
 Filename: sbvt/browser.py
 Comment: 
 
 Filename: sbvt/imagetools.py
 Comment: 
 
 Filename: sbvt/timer.py
 Comment: 
 
 Filename: sbvt/visualtest.py
 Comment: 
 
-Filename: visualtest_python-1.1.0.dist-info/LICENSE
+Filename: visualtest_python-1.2.0.dist-info/LICENSE
 Comment: 
 
-Filename: visualtest_python-1.1.0.dist-info/METADATA
+Filename: visualtest_python-1.2.0.dist-info/METADATA
 Comment: 
 
-Filename: visualtest_python-1.1.0.dist-info/WHEEL
+Filename: visualtest_python-1.2.0.dist-info/WHEEL
 Comment: 
 
-Filename: visualtest_python-1.1.0.dist-info/top_level.txt
+Filename: visualtest_python-1.2.0.dist-info/top_level.txt
 Comment: 
 
-Filename: visualtest_python-1.1.0.dist-info/RECORD
+Filename: visualtest_python-1.2.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## sbvt/__init__.py

```diff
@@ -1,14 +1,14 @@
 import logging
 import os.path
 
 # this import statement is here for context.py in tests folder
 from .visualtest import VisualTest
 
-__version__ = '1.1.0'
+__version__ = '1.2.0'
 
 logPath = 'logs'
 if not os.path.exists(logPath):
     os.makedirs(logPath)
 
 # By generating a new logger as 'vt' we don't affect global logging from other packages
 # Each logger created in our package should be a child by prefacing with 'vt.childname'
```

## sbvt/browser.py

```diff
@@ -3,14 +3,15 @@
 import shutil
 import math
 import logging
 import json
 from .imagetools import ImageTools
 from .timer import StopWatch
 from .api import Api
+from selenium.webdriver.common.by import By
 
 log = logging.getLogger(f'vt.{os.path.basename(__file__)}')
 
 # defaults - can be overridden with limits parameter
 DEFAULT_MAX_IMAGE_SIZE_MB = 20  # 20MB
 DEFAULT_MAX_TIME_MIN = 3.5  # minutes (really for mobiles)
 
@@ -138,14 +139,21 @@
 
         if self._saveDOM: # save at same location and filename as screenshot
             with open(path.replace('.png','.json'), 'w') as outfile:
                 json.dump(dom, outfile, indent=4)
 
         return dom
 
+    def _findElement(self, cssSelector):
+        return self._driver.find_element(By.CSS_SELECTOR, cssSelector)
+    
+    def _injectIgnoreElements(self, ignoreElements):
+        script = 'window.sbvt = { ignoreElements: %s }' % json.dumps(ignoreElements)
+        self._driver.execute_script(script)
+
     def _getPageDimensions(self):
         script = """
             return JSON.stringify({
                 "document": {
                     "height": document.documentElement.clientHeight,
                     "width": document.documentElement.clientWidth
                 },
```

## sbvt/visualtest.py

```diff
@@ -184,14 +184,15 @@
         Args:
             name: the unique name used both in naming the file, and identifying the visual test image 
             options: dictionary
                 - { 'element': WebElement }: value must be a selenium webdriver element and will take an element screenshot
                 - { 'vieport': true }: will capture an image of the browser's current viewport
                 - if neither 'element', nor 'viewport' provided, defaults to capture a fullpage screenshot
                 - { 'lazyload': 1000 }: For fullpage screenshot, will load lazy content before capturing screenshot
+                - { 'ignoreElements': ['.css-selector'] }: For any screenshot, will specify elements to ignore during image comparison
         
         Returns:
             Information about the screenshot result
         """
         if not name:
             raise Exception(f'Name argument is required')
 
@@ -200,14 +201,32 @@
 
         if len(name) > 100:
             raise Exception(f'Name argument cannot be greater than 100 characters')
 
         filePath = os.path.join(self._settings['saveTo'],f'{name}.png')
         imageType = None
 
+        if 'ignoreElements' in options:
+            if not isinstance(options['ignoreElements'], list):
+                raise Exception(f'ignoreElements must be of type "list"')
+            if not all(isinstance(item, str) for item in options['ignoreElements']):
+                raise Exception(f'ignoreElements values must all be strings')
+            
+            elementsNotFound = []
+            for cssSelector in options['ignoreElements']:
+                try:
+                    self.browser._findElement(cssSelector)
+                except:
+                    elementsNotFound.append(cssSelector)
+            
+            if len(elementsNotFound) > 0:
+                raise Exception(f'Some ignoreElements were not found on the page: {",".join(elementsNotFound)}')
+            else:
+                self.browser._injectIgnoreElements(options['ignoreElements'])
+
         if 'element' in options:
             result = self.browser.takeElementScreenshot(options['element'], filePath)
             imageType = 'element'
         elif 'viewport' in options and options['viewport'] == True:
             result = self.browser.takeViewportScreenshot(filePath)
             imageType = 'viewport'
         else:
@@ -226,15 +245,16 @@
             'imageType': imageType,
             'imageExt': 'png',
             'testUrl': self.browser._driver.current_url,
             'viewportWidth': self.browser.viewportWidth,
             'viewportHeight': self.browser.viewportHeight,
             'imageWidth': result['imageSize']['width'],
             'imageHeight': result['imageSize']['height'],
-            'dom': json.dumps(self.browser.dom)
+            'dom': json.dumps(self.browser.dom),
+            'ignoredElements': json.dumps(self.browser.dom['ignoredElementsData'])
         }
         imageData.update(self.browser._deviceInfo) # required information about device/os/browser
 
         # these two are informational and just used to store - not required
         imageData.update({'driverCapabilities': json.dumps(self.browser.capabilities)})
         imageData.update({'userAgentInfo': json.dumps(self.browser._userAgentInfo)})
```

## Comparing `visualtest_python-1.1.0.dist-info/LICENSE` & `visualtest_python-1.2.0.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `visualtest_python-1.1.0.dist-info/METADATA` & `visualtest_python-1.2.0.dist-info/METADATA`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: visualtest-python
-Version: 1.1.0
+Version: 1.2.0
 Summary: Python SDK for SmartBear VisualTest via Selenium WebDriver
-Home-page: https://github.com/SmartBear/visual-testing-sdks/python
+Home-page: https://github.com/SmartBear/visualtest-python
 Author: Luke Kende
 Author-email: luke.kende@smartbear.com
 Keywords: visual testing,UI testing,GUI testing,UX testing,screenshots,full page screenshots,image comparisons,regression testing
-Classifier: Development Status :: 4 - Beta
+Classifier: Development Status :: 5 - Production/Stable
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Information Technology
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Description-Content-Type: text/markdown
```

## Comparing `visualtest_python-1.1.0.dist-info/RECORD` & `visualtest_python-1.2.0.dist-info/RECORD`

 * *Files 22% similar despite different names*

```diff
@@ -1,11 +1,12 @@
-sbvt/__init__.py,sha256=bP7FIaIwKUCX1YJKdpujjHJkLnGGsZEFqQnegxpV2Oo,1129
+sbvt/__init__.py,sha256=O1nvWpg3l7hxGYGbMZ_NPAvVfdM2vf4kwyuDK32YLmU,1129
 sbvt/api.py,sha256=q9VDvuoozKhDfK7AW3GF_qSrgBWS8XGJ4mc4Sy1GZpc,9191
-sbvt/browser.py,sha256=3i6PrTcjQxil-07r1R0KUep44G8lQ-nwAVN0DYtzrGQ,33032
+sbvt/browser-safari-bug-test.py,sha256=fBvEvdCCfydxstaz90RSpINg2KNBepseRbdObDtuGVo,35553
+sbvt/browser.py,sha256=_IAJSWUA4LW9jwJSeZtBjSMAz1WtL6GYW5fvI0I5WdE,33376
 sbvt/imagetools.py,sha256=6z4MA2Wfet8jMlTlKTU68JXSADXNj78fOXQhl7f_ONQ,5981
 sbvt/timer.py,sha256=ciQJQUYSTChdIbsLiYiEzPa6yw8YwSqaeWc7DU4gSrE,548
-sbvt/visualtest.py,sha256=c5Uudogjb8CyLkJMJTqVxsDAp9UuU88aJ0Mp4LeoLdo,9871
-visualtest_python-1.1.0.dist-info/LICENSE,sha256=8vhEBNg7g2MxrQdwP-_ugxe3PDk5EbsBeMa--tc1xEA,1073
-visualtest_python-1.1.0.dist-info/METADATA,sha256=YU2b1-e0DZUuCOCWhCjsHaGyBYWpM4kY5F1bcGu1Ass,3872
-visualtest_python-1.1.0.dist-info/WHEEL,sha256=pkctZYzUS4AYVn6dJ-7367OJZivF2e8RA9b_ZBjif18,92
-visualtest_python-1.1.0.dist-info/top_level.txt,sha256=t2tNJSI9vPU6KzikQCU2NYIJmbBaVTvOSJajc6IoRD0,5
-visualtest_python-1.1.0.dist-info/RECORD,,
+sbvt/visualtest.py,sha256=2KrDPx_pOYSl1AEn8dkFhvYpIU10oI4EKzDLNk6nVHY,10962
+visualtest_python-1.2.0.dist-info/LICENSE,sha256=8vhEBNg7g2MxrQdwP-_ugxe3PDk5EbsBeMa--tc1xEA,1073
+visualtest_python-1.2.0.dist-info/METADATA,sha256=Ax3iZfKsb9if7s1Tbs8PeUr3lukrfG_u5Cy1JOWLfKA,3876
+visualtest_python-1.2.0.dist-info/WHEEL,sha256=pkctZYzUS4AYVn6dJ-7367OJZivF2e8RA9b_ZBjif18,92
+visualtest_python-1.2.0.dist-info/top_level.txt,sha256=t2tNJSI9vPU6KzikQCU2NYIJmbBaVTvOSJajc6IoRD0,5
+visualtest_python-1.2.0.dist-info/RECORD,,
```

