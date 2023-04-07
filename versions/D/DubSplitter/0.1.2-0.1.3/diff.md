# Comparing `tmp/DubSplitter-0.1.2.tar.gz` & `tmp/DubSplitter-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "DubSplitter-0.1.2.tar", last modified: Fri Apr  7 02:59:18 2023, max compression
+gzip compressed data, was "DubSplitter-0.1.3.tar", last modified: Fri Apr  7 13:16:09 2023, max compression
```

## Comparing `DubSplitter-0.1.2.tar` & `DubSplitter-0.1.3.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 02:59:18.070647 DubSplitter-0.1.2/
-drwxrwxrwx   0        0        0        0 2023-04-07 02:59:18.066643 DubSplitter-0.1.2/DubSplitter.egg-info/
--rw-rw-rw-   0        0        0     2831 2023-04-07 02:59:18.000000 DubSplitter-0.1.2/DubSplitter.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      502 2023-04-07 02:59:18.000000 DubSplitter-0.1.2/DubSplitter.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 02:59:18.000000 DubSplitter-0.1.2/DubSplitter.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       61 2023-04-07 02:59:18.000000 DubSplitter-0.1.2/DubSplitter.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0        2 2023-04-07 00:03:48.000000 DubSplitter-0.1.2/DubSplitter.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       27 2023-04-07 02:59:18.000000 DubSplitter-0.1.2/DubSplitter.egg-info/requires.txt
--rw-rw-rw-   0        0        0       12 2023-04-07 02:59:18.000000 DubSplitter-0.1.2/DubSplitter.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     2831 2023-04-07 02:59:18.069647 DubSplitter-0.1.2/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-07 02:59:18.067643 DubSplitter-0.1.2/dubSplitter/
--rw-rw-rw-   0        0        0        0 2023-04-07 01:02:52.000000 DubSplitter-0.1.2/dubSplitter/__init__.py
--rw-rw-rw-   0        0        0     1586 2023-04-07 02:57:49.000000 DubSplitter-0.1.2/dubSplitter/constants.py
--rw-rw-rw-   0        0        0     2793 2023-04-07 01:57:24.000000 DubSplitter-0.1.2/dubSplitter/dubSplitter.py
-drwxrwxrwx   0        0        0        0 2023-04-07 02:59:18.069647 DubSplitter-0.1.2/dubSplitter/functions/
--rw-rw-rw-   0        0        0        0 2023-04-07 01:03:14.000000 DubSplitter-0.1.2/dubSplitter/functions/__init__.py
--rw-rw-rw-   0        0        0      628 2023-04-07 01:33:33.000000 DubSplitter-0.1.2/dubSplitter/functions/path.py
--rw-rw-rw-   0        0        0     1521 2023-04-07 01:22:53.000000 DubSplitter-0.1.2/dubSplitter/functions/slicer.py
--rw-rw-rw-   0        0        0      399 2023-04-07 00:58:45.000000 DubSplitter-0.1.2/dubSplitter/functions/stringEx.py
--rw-rw-rw-   0        0        0     2890 2023-04-07 01:23:08.000000 DubSplitter-0.1.2/dubSplitter/functions/voiceRecognition.py
--rw-rw-rw-   0        0        0       42 2023-04-07 02:59:18.070647 DubSplitter-0.1.2/setup.cfg
--rw-rw-rw-   0        0        0     1280 2023-04-07 02:58:57.000000 DubSplitter-0.1.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:16:09.145394 DubSplitter-0.1.3/
+drwxrwxrwx   0        0        0        0 2023-04-07 13:16:09.030570 DubSplitter-0.1.3/DubSplitter.egg-info/
+-rw-rw-rw-   0        0        0     2866 2023-04-07 13:16:08.000000 DubSplitter-0.1.3/DubSplitter.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      502 2023-04-07 13:16:08.000000 DubSplitter-0.1.3/DubSplitter.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:16:08.000000 DubSplitter-0.1.3/DubSplitter.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       61 2023-04-07 13:16:08.000000 DubSplitter-0.1.3/DubSplitter.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0        2 2023-04-07 00:03:48.000000 DubSplitter-0.1.3/DubSplitter.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       27 2023-04-07 13:16:08.000000 DubSplitter-0.1.3/DubSplitter.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       12 2023-04-07 13:16:08.000000 DubSplitter-0.1.3/DubSplitter.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     2866 2023-04-07 13:16:09.144393 DubSplitter-0.1.3/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-07 13:16:09.031570 DubSplitter-0.1.3/dubSplitter/
+-rw-rw-rw-   0        0        0        0 2023-04-07 01:02:52.000000 DubSplitter-0.1.3/dubSplitter/__init__.py
+-rw-rw-rw-   0        0        0     1586 2023-04-07 02:57:49.000000 DubSplitter-0.1.3/dubSplitter/constants.py
+-rw-rw-rw-   0        0        0     2793 2023-04-07 01:57:24.000000 DubSplitter-0.1.3/dubSplitter/dubSplitter.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:16:09.130391 DubSplitter-0.1.3/dubSplitter/functions/
+-rw-rw-rw-   0        0        0        0 2023-04-07 01:03:14.000000 DubSplitter-0.1.3/dubSplitter/functions/__init__.py
+-rw-rw-rw-   0        0        0      628 2023-04-07 01:33:33.000000 DubSplitter-0.1.3/dubSplitter/functions/path.py
+-rw-rw-rw-   0        0        0     1521 2023-04-07 01:22:53.000000 DubSplitter-0.1.3/dubSplitter/functions/slicer.py
+-rw-rw-rw-   0        0        0      399 2023-04-07 00:58:45.000000 DubSplitter-0.1.3/dubSplitter/functions/stringEx.py
+-rw-rw-rw-   0        0        0     2890 2023-04-07 01:23:08.000000 DubSplitter-0.1.3/dubSplitter/functions/voiceRecognition.py
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:16:09.145394 DubSplitter-0.1.3/setup.cfg
+-rw-rw-rw-   0        0        0     1280 2023-04-07 13:12:50.000000 DubSplitter-0.1.3/setup.py
```

### Comparing `DubSplitter-0.1.2/DubSplitter.egg-info/PKG-INFO` & `DubSplitter-0.1.3/DubSplitter.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DubSplitter
-Version: 0.1.2
+Version: 0.1.3
 Summary: an easy tool to split dubs based on given silence
 Home-page: https://github.com/defisym/HibiscusAVGEngine/tree/main/Utilities/DubSplitter
 Author: defisym
 Author-email: defisym@outlook.com
 License: MIT
 Keywords: DubSplitter dub splitter Hibiscus AVG Galgame VisualNovel VN
 Classifier: Development Status :: 4 - Beta
@@ -30,25 +30,30 @@
 |-------------------|--------|---------------------------------------------------------------------------------------------------------------------------|
 | -f, --fileName    | option | file to process                                                                                                           |
 | -o, --outFilePath | option | output folder, if not set, will use `scriptPath + \\Out\\` (as script), or `userPath + \\DubSplitter\\Out\\` (as package) |
 | -s, --silence     | option | silence time, in ms, default is `1000`ms                                                                                  |
 | -r, --range       | option | range, default is `100`ms. e.g., silence = `400`, range = `100` will slice in `400`ms and `500`ms                         |
 | --step            | option | loop step, default is `100`ms                                                                                             |
 | --noVR            | option | don't use voice recognition, default is `false`                                                                           |
-| --step            | option | whisper model, default is `base`                                                                                          |
-| --step            | option | language used in whisper, default is `chinese`                                                                            |
+| --model           | option | whisper model, default is `base`                                                                                          |
+| --language        | option | language used in whisper, default is `chinese`                                                                            |
 
 ## Usage
 
 open folder in terminal, then run `python main.py`
 
-or use command `pip install DubSplitter` to install [package](https://pypi.org/project/DubSplitter/), then run `dubSplitter`
+or use command `pip install DubSplitter` to install [package](https://pypi.org/project/DubSplitter/), then
+run `dubSplitter`
 
 ## Changelog
 
+### 230407 0.1.3
+
+- fix typo
+
 ### 230407 0.1.2
 
 - optimize `update_path`
 
 ### 230407 0.1.1
 
 - update readme
```

### Comparing `DubSplitter-0.1.2/PKG-INFO` & `DubSplitter-0.1.3/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DubSplitter
-Version: 0.1.2
+Version: 0.1.3
 Summary: an easy tool to split dubs based on given silence
 Home-page: https://github.com/defisym/HibiscusAVGEngine/tree/main/Utilities/DubSplitter
 Author: defisym
 Author-email: defisym@outlook.com
 License: MIT
 Keywords: DubSplitter dub splitter Hibiscus AVG Galgame VisualNovel VN
 Classifier: Development Status :: 4 - Beta
@@ -30,25 +30,30 @@
 |-------------------|--------|---------------------------------------------------------------------------------------------------------------------------|
 | -f, --fileName    | option | file to process                                                                                                           |
 | -o, --outFilePath | option | output folder, if not set, will use `scriptPath + \\Out\\` (as script), or `userPath + \\DubSplitter\\Out\\` (as package) |
 | -s, --silence     | option | silence time, in ms, default is `1000`ms                                                                                  |
 | -r, --range       | option | range, default is `100`ms. e.g., silence = `400`, range = `100` will slice in `400`ms and `500`ms                         |
 | --step            | option | loop step, default is `100`ms                                                                                             |
 | --noVR            | option | don't use voice recognition, default is `false`                                                                           |
-| --step            | option | whisper model, default is `base`                                                                                          |
-| --step            | option | language used in whisper, default is `chinese`                                                                            |
+| --model           | option | whisper model, default is `base`                                                                                          |
+| --language        | option | language used in whisper, default is `chinese`                                                                            |
 
 ## Usage
 
 open folder in terminal, then run `python main.py`
 
-or use command `pip install DubSplitter` to install [package](https://pypi.org/project/DubSplitter/), then run `dubSplitter`
+or use command `pip install DubSplitter` to install [package](https://pypi.org/project/DubSplitter/), then
+run `dubSplitter`
 
 ## Changelog
 
+### 230407 0.1.3
+
+- fix typo
+
 ### 230407 0.1.2
 
 - optimize `update_path`
 
 ### 230407 0.1.1
 
 - update readme
```

### Comparing `DubSplitter-0.1.2/dubSplitter/constants.py` & `DubSplitter-0.1.3/dubSplitter/constants.py`

 * *Files identical despite different names*

### Comparing `DubSplitter-0.1.2/dubSplitter/dubSplitter.py` & `DubSplitter-0.1.3/dubSplitter/dubSplitter.py`

 * *Files identical despite different names*

### Comparing `DubSplitter-0.1.2/dubSplitter/functions/path.py` & `DubSplitter-0.1.3/dubSplitter/functions/path.py`

 * *Files identical despite different names*

### Comparing `DubSplitter-0.1.2/dubSplitter/functions/slicer.py` & `DubSplitter-0.1.3/dubSplitter/functions/slicer.py`

 * *Files identical despite different names*

### Comparing `DubSplitter-0.1.2/dubSplitter/functions/voiceRecognition.py` & `DubSplitter-0.1.3/dubSplitter/functions/voiceRecognition.py`

 * *Files identical despite different names*

### Comparing `DubSplitter-0.1.2/setup.py` & `DubSplitter-0.1.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from setuptools import find_packages
 from setuptools import setup
 
-VERSION = '0.1.2'
+VERSION = '0.1.3'
 
 with open('ReadMe.md') as f:
     LONG_DESCRIPTION = f.read()
 
 setup(
     name='DubSplitter',
     version=VERSION,
```

