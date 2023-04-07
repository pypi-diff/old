# Comparing `tmp/rockalyzer-0.0.1.tar.gz` & `tmp/rockalyzer-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rockalyzer-0.0.1.tar", last modified: Fri Apr  7 13:42:23 2023, max compression
+gzip compressed data, was "rockalyzer-0.0.2.tar", last modified: Fri Apr  7 13:51:35 2023, max compression
```

## Comparing `rockalyzer-0.0.1.tar` & `rockalyzer-0.0.2.tar`

### file list

```diff
@@ -1,17 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 13:42:23.853579 rockalyzer-0.0.1/
--rw-rw-rw-   0        0        0     1089 2023-03-07 15:36:40.000000 rockalyzer-0.0.1/LICENSE
--rw-rw-rw-   0        0        0      971 2023-04-07 13:42:23.852579 rockalyzer-0.0.1/PKG-INFO
--rw-rw-rw-   0        0        0      405 2023-04-07 13:32:17.000000 rockalyzer-0.0.1/README.md
--rw-rw-rw-   0        0        0       42 2023-04-07 13:42:23.853579 rockalyzer-0.0.1/setup.cfg
--rw-rw-rw-   0        0        0      991 2023-04-07 13:38:42.000000 rockalyzer-0.0.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:42:23.848574 rockalyzer-0.0.1/src/
--rw-rw-rw-   0        0        0    32560 2023-03-30 15:25:48.000000 rockalyzer-0.0.1/src/Action.py
--rw-rw-rw-   0        0        0    64295 2023-03-30 20:00:09.000000 rockalyzer-0.0.1/src/Game.py
--rw-rw-rw-   0        0        0      205 2023-03-27 18:56:29.000000 rockalyzer-0.0.1/src/console_colors.py
--rw-rw-rw-   0        0        0     3696 2023-03-29 13:31:43.000000 rockalyzer-0.0.1/src/constants.py
-drwxrwxrwx   0        0        0        0 2023-04-07 13:42:23.852579 rockalyzer-0.0.1/src/rockalyzer.egg-info/
--rw-rw-rw-   0        0        0      971 2023-04-07 13:42:23.000000 rockalyzer-0.0.1/src/rockalyzer.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      280 2023-04-07 13:42:23.000000 rockalyzer-0.0.1/src/rockalyzer.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 13:42:23.000000 rockalyzer-0.0.1/src/rockalyzer.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       17 2023-04-07 13:42:23.000000 rockalyzer-0.0.1/src/rockalyzer.egg-info/requires.txt
--rw-rw-rw-   0        0        0       46 2023-04-07 13:42:23.000000 rockalyzer-0.0.1/src/rockalyzer.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 13:51:35.007264 rockalyzer-0.0.2/
+-rw-rw-rw-   0        0        0     1089 2023-03-07 15:36:40.000000 rockalyzer-0.0.2/LICENSE
+-rw-rw-rw-   0        0        0      971 2023-04-07 13:51:35.007264 rockalyzer-0.0.2/PKG-INFO
+-rw-rw-rw-   0        0        0      405 2023-04-07 13:32:17.000000 rockalyzer-0.0.2/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 13:51:35.008264 rockalyzer-0.0.2/setup.cfg
+-rw-rw-rw-   0        0        0      993 2023-04-07 13:51:31.000000 rockalyzer-0.0.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:51:35.003266 rockalyzer-0.0.2/src/
+-rw-rw-rw-   0        0        0    32560 2023-03-30 15:25:48.000000 rockalyzer-0.0.2/src/Action.py
+-rw-rw-rw-   0        0        0    64295 2023-03-30 20:00:09.000000 rockalyzer-0.0.2/src/Game.py
+-rw-rw-rw-   0        0        0      205 2023-03-27 18:56:29.000000 rockalyzer-0.0.2/src/console_colors.py
+-rw-rw-rw-   0        0        0     3696 2023-03-29 13:31:43.000000 rockalyzer-0.0.2/src/constants.py
+drwxrwxrwx   0        0        0        0 2023-04-07 13:51:35.006264 rockalyzer-0.0.2/src/rockalyzer.egg-info/
+-rw-rw-rw-   0        0        0      971 2023-04-07 13:51:34.000000 rockalyzer-0.0.2/src/rockalyzer.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      298 2023-04-07 13:51:34.000000 rockalyzer-0.0.2/src/rockalyzer.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 13:51:34.000000 rockalyzer-0.0.2/src/rockalyzer.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       17 2023-04-07 13:51:34.000000 rockalyzer-0.0.2/src/rockalyzer.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       48 2023-04-07 13:51:34.000000 rockalyzer-0.0.2/src/rockalyzer.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     4948 2023-04-07 13:04:45.000000 rockalyzer-0.0.2/src/rockalyzer.py
```

### Comparing `rockalyzer-0.0.1/LICENSE` & `rockalyzer-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `rockalyzer-0.0.1/PKG-INFO` & `rockalyzer-0.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rockalyzer
-Version: 0.0.1
+Version: 0.0.2
 Summary: Rocket League Analyzer
 Home-page: https://github.com/eliastheis/rockalyzer
 Author: Elias Theis
 Author-email: mail@eliastheis.de
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
```

### Comparing `rockalyzer-0.0.1/setup.py` & `rockalyzer-0.0.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,22 +3,22 @@
 
 # read the contents of your README file for the long description
 with open('README.md', 'r') as fh:
     long_description = fh.read()
 
 setup(
     name='rockalyzer',
-    version='0.0.1',
+    version='0.0.2',
     description='Rocket League Analyzer',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/eliastheis/rockalyzer',
     author='Elias Theis',
     author_email='mail@eliastheis.de',
-    py_modules=['Replayer', 'Game', 'Action', 'console_colors', 'constants'],
+    py_modules=['rockalyzer', 'Game', 'Action', 'console_colors', 'constants'],
     package_dir={'': 'src'},
     install_requires=[
         'numpy',
         'matplotlib',
     ],
     classifiers=[
         'Programming Language :: Python :: 3',
```

### Comparing `rockalyzer-0.0.1/src/Action.py` & `rockalyzer-0.0.2/src/Action.py`

 * *Files identical despite different names*

### Comparing `rockalyzer-0.0.1/src/Game.py` & `rockalyzer-0.0.2/src/Game.py`

 * *Files identical despite different names*

### Comparing `rockalyzer-0.0.1/src/constants.py` & `rockalyzer-0.0.2/src/constants.py`

 * *Files identical despite different names*

### Comparing `rockalyzer-0.0.1/src/rockalyzer.egg-info/PKG-INFO` & `rockalyzer-0.0.2/src/rockalyzer.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rockalyzer
-Version: 0.0.1
+Version: 0.0.2
 Summary: Rocket League Analyzer
 Home-page: https://github.com/eliastheis/rockalyzer
 Author: Elias Theis
 Author-email: mail@eliastheis.de
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
```

