# Comparing `tmp/phonemeRecognizerWrapper-0.1.3.tar.gz` & `tmp/phonemeRecognizerWrapper-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "phonemeRecognizerWrapper-0.1.3.tar", last modified: Fri Apr  7 12:21:31 2023, max compression
+gzip compressed data, was "phonemeRecognizerWrapper-0.1.4.tar", last modified: Fri Apr  7 12:48:28 2023, max compression
```

## Comparing `phonemeRecognizerWrapper-0.1.3.tar` & `phonemeRecognizerWrapper-0.1.4.tar`

### file list

```diff
@@ -1,16 +1,17 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 12:21:31.702145 phonemeRecognizerWrapper-0.1.3/
--rw-rw-rw-   0        0        0     1088 2022-09-08 13:30:25.000000 phonemeRecognizerWrapper-0.1.3/LICENSE.txt
--rw-rw-rw-   0        0        0        0 2022-09-08 13:30:25.000000 phonemeRecognizerWrapper-0.1.3/MANIFEST.in
--rw-rw-rw-   0        0        0     3701 2023-04-07 12:21:31.701650 phonemeRecognizerWrapper-0.1.3/PKG-INFO
--rw-rw-rw-   0        0        0     3229 2023-04-07 12:13:00.000000 phonemeRecognizerWrapper-0.1.3/README.md
-drwxrwxrwx   0        0        0        0 2023-04-07 12:21:31.675391 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper/
--rw-rw-rw-   0        0        0        0 2022-09-08 13:30:25.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper/__init__.py
--rw-rw-rw-   0        0        0     8429 2023-04-07 12:14:15.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper/recognize.py
-drwxrwxrwx   0        0        0        0 2023-04-07 12:21:31.699170 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/
--rw-rw-rw-   0        0        0     3701 2023-04-07 12:21:31.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      356 2023-04-07 12:21:31.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 12:21:31.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       28 2023-04-07 12:21:31.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/requires.txt
--rw-rw-rw-   0        0        0       25 2023-04-07 12:21:31.000000 phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 12:21:31.702145 phonemeRecognizerWrapper-0.1.3/setup.cfg
--rw-rw-rw-   0        0        0      984 2023-04-07 12:13:12.000000 phonemeRecognizerWrapper-0.1.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:48:28.556300 phonemeRecognizerWrapper-0.1.4/
+-rw-rw-rw-   0        0        0     1088 2023-04-07 12:36:20.000000 phonemeRecognizerWrapper-0.1.4/LICENSE.txt
+-rw-rw-rw-   0        0        0        0 2022-09-08 13:30:25.000000 phonemeRecognizerWrapper-0.1.4/MANIFEST.in
+-rw-rw-rw-   0        0        0     5359 2023-04-07 12:48:28.554820 phonemeRecognizerWrapper-0.1.4/PKG-INFO
+-rw-rw-rw-   0        0        0     3229 2023-04-07 12:13:00.000000 phonemeRecognizerWrapper-0.1.4/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 12:48:28.542436 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper/
+-rw-rw-rw-   0        0        0        0 2022-09-08 13:30:25.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper/__init__.py
+-rw-rw-rw-   0        0        0     8429 2023-04-07 12:14:15.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper/recognize.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:48:28.552856 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/
+-rw-rw-rw-   0        0        0     5359 2023-04-07 12:48:28.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      371 2023-04-07 12:48:28.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 12:48:28.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       28 2023-04-07 12:48:28.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       25 2023-04-07 12:48:28.000000 phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      997 2023-04-07 12:47:49.000000 phonemeRecognizerWrapper-0.1.4/pyproject.toml
+-rw-rw-rw-   0        0        0       42 2023-04-07 12:48:28.556796 phonemeRecognizerWrapper-0.1.4/setup.cfg
+-rw-rw-rw-   0        0        0      984 2023-04-07 12:38:18.000000 phonemeRecognizerWrapper-0.1.4/setup.py
```

### Comparing `phonemeRecognizerWrapper-0.1.3/LICENSE.txt` & `phonemeRecognizerWrapper-0.1.4/LICENSE.txt`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 MIT License
 
-Copyright (c) 2022 Petr Krýže
+Copyright (c) 2023 Petr Krýže
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
```

### Comparing `phonemeRecognizerWrapper-0.1.3/PKG-INFO` & `phonemeRecognizerWrapper-0.1.4/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -1,18 +1,7 @@
-Metadata-Version: 2.1
-Name: phonemeRecognizerWrapper
-Version: 0.1.3
-Summary: Package containing one wrapper script over the Allosaurus phoneme recognition library, designed for passing the Allosaurus output data to MATLAB scripts for further analysis.
-Home-page: https://github.com/PetrKryze/phonemeRecognizerWrapper
-Author: Petr Krýže
-Author-email: petr.kryze@gmail.com
-License: LICENSE.txt
-Description-Content-Type: text/markdown
-License-File: LICENSE.txt
-
 # phonemeRecognizerWrapper
 Package containing one wrapper script over the Allosaurus phoneme recognition library, designed for passing the Allosaurus output data to MATLAB scripts for further analysis.
 
 ## Installation
 1. [Install Python 3](https://www.python.org/downloads/)
    - To see if Python is installed, use `py --version` in command line
    - `pip` is automatically included in the Python installation, but to check or update the pip version use: `py -m ensurepip --upgrade`
```

### Comparing `phonemeRecognizerWrapper-0.1.3/README.md` & `phonemeRecognizerWrapper-0.1.4/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,7 +1,45 @@
+Metadata-Version: 2.1
+Name: phonemeRecognizerWrapper
+Version: 0.1.4
+Summary: Package containing one wrapper script over the Allosaurus phoneme recognition library, designed for passing the Allosaurus output data to MATLAB scripts for further analysis.
+Home-page: https://github.com/PetrKryze/phonemeRecognizerWrapper
+Author: Petr Krýže
+Author-email: Petr Krýže <petr.kryze@gmail.com>
+License: MIT License
+        
+        Copyright (c) 2023 Petr Krýže
+        
+        Permission is hereby granted, free of charge, to any person obtaining a copy
+        of this software and associated documentation files (the "Software"), to deal
+        in the Software without restriction, including without limitation the rights
+        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
+        copies of the Software, and to permit persons to whom the Software is
+        furnished to do so, subject to the following conditions:
+        
+        The above copyright notice and this permission notice shall be included in all
+        copies or substantial portions of the Software.
+        
+        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
+        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
+        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
+        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
+        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
+        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
+        SOFTWARE.
+Project-URL: Homepage, https://github.com/PetrKryze/phonemeRecognizerWrapper
+Project-URL: Bug Tracker, https://github.com/PetrKryze/phonemeRecognizerWrapper/issues
+Keywords: phoneme,transcript,allosaurus,MATLAB,wrapper,recognizer
+Classifier: Programming Language :: Python :: 3
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE.txt
+
 # phonemeRecognizerWrapper
 Package containing one wrapper script over the Allosaurus phoneme recognition library, designed for passing the Allosaurus output data to MATLAB scripts for further analysis.
 
 ## Installation
 1. [Install Python 3](https://www.python.org/downloads/)
    - To see if Python is installed, use `py --version` in command line
    - `pip` is automatically included in the Python installation, but to check or update the pip version use: `py -m ensurepip --upgrade`
```

### Comparing `phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper/recognize.py` & `phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper/recognize.py`

 * *Files identical despite different names*

### Comparing `phonemeRecognizerWrapper-0.1.3/phonemeRecognizerWrapper.egg-info/PKG-INFO` & `phonemeRecognizerWrapper-0.1.4/phonemeRecognizerWrapper.egg-info/PKG-INFO`

 * *Files 23% similar despite different names*

```diff
@@ -1,15 +1,42 @@
 Metadata-Version: 2.1
 Name: phonemeRecognizerWrapper
-Version: 0.1.3
+Version: 0.1.4
 Summary: Package containing one wrapper script over the Allosaurus phoneme recognition library, designed for passing the Allosaurus output data to MATLAB scripts for further analysis.
 Home-page: https://github.com/PetrKryze/phonemeRecognizerWrapper
 Author: Petr Krýže
-Author-email: petr.kryze@gmail.com
-License: LICENSE.txt
+Author-email: Petr Krýže <petr.kryze@gmail.com>
+License: MIT License
+        
+        Copyright (c) 2023 Petr Krýže
+        
+        Permission is hereby granted, free of charge, to any person obtaining a copy
+        of this software and associated documentation files (the "Software"), to deal
+        in the Software without restriction, including without limitation the rights
+        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
+        copies of the Software, and to permit persons to whom the Software is
+        furnished to do so, subject to the following conditions:
+        
+        The above copyright notice and this permission notice shall be included in all
+        copies or substantial portions of the Software.
+        
+        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
+        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
+        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
+        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
+        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
+        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
+        SOFTWARE.
+Project-URL: Homepage, https://github.com/PetrKryze/phonemeRecognizerWrapper
+Project-URL: Bug Tracker, https://github.com/PetrKryze/phonemeRecognizerWrapper/issues
+Keywords: phoneme,transcript,allosaurus,MATLAB,wrapper,recognizer
+Classifier: Programming Language :: Python :: 3
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # phonemeRecognizerWrapper
 Package containing one wrapper script over the Allosaurus phoneme recognition library, designed for passing the Allosaurus output data to MATLAB scripts for further analysis.
 
 ## Installation
```

### Comparing `phonemeRecognizerWrapper-0.1.3/setup.py` & `phonemeRecognizerWrapper-0.1.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup
 
 setup(
     # Application name:
     name='phonemeRecognizerWrapper',
 
     # Version number (initial):
-    version='0.1.3',
+    version='0.1.4',
 
     # Application author details:
     author='Petr Krýže',
     author_email='petr.kryze@gmail.com',
 
     # Packages
     packages=['phonemeRecognizerWrapper'],
```

