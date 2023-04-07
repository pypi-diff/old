# Comparing `tmp/dariusVision-0.0.1.tar.gz` & `tmp/dariusVision-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dariusVision-0.0.1.tar", last modified: Fri Apr  7 08:02:26 2023, max compression
+gzip compressed data, was "dariusVision-0.0.2.tar", last modified: Fri Apr  7 08:13:14 2023, max compression
```

## Comparing `dariusVision-0.0.1.tar` & `dariusVision-0.0.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxr-x   0 gbox3d    (1000) gbox3d    (1000)        0 2023-04-07 08:02:26.548217 dariusVision-0.0.1/
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)    35149 2023-04-07 04:46:45.000000 dariusVision-0.0.1/LICENSE
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      445 2023-04-07 08:02:26.548217 dariusVision-0.0.1/PKG-INFO
-drwxrwxr-x   0 gbox3d    (1000) gbox3d    (1000)        0 2023-04-07 08:02:26.548217 dariusVision-0.0.1/dariusVision/
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      136 2023-04-07 08:01:25.000000 dariusVision-0.0.1/dariusVision/__init__.py
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)     3265 2023-04-07 01:35:34.000000 dariusVision-0.0.1/dariusVision/cam.py
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)     9681 2023-04-07 08:00:19.000000 dariusVision-0.0.1/dariusVision/realsense2.py
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)     2011 2023-04-07 04:29:23.000000 dariusVision-0.0.1/dariusVision/utils.py
-drwxrwxr-x   0 gbox3d    (1000) gbox3d    (1000)        0 2023-04-07 08:02:26.548217 dariusVision-0.0.1/dariusVision.egg-info/
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      445 2023-04-07 08:02:26.000000 dariusVision-0.0.1/dariusVision.egg-info/PKG-INFO
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      289 2023-04-07 08:02:26.000000 dariusVision-0.0.1/dariusVision.egg-info/SOURCES.txt
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)        1 2023-04-07 08:02:26.000000 dariusVision-0.0.1/dariusVision.egg-info/dependency_links.txt
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)       26 2023-04-07 08:02:26.000000 dariusVision-0.0.1/dariusVision.egg-info/requires.txt
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)       13 2023-04-07 08:02:26.000000 dariusVision-0.0.1/dariusVision.egg-info/top_level.txt
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)       38 2023-04-07 08:02:26.548217 dariusVision-0.0.1/setup.cfg
--rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      637 2023-04-07 08:02:17.000000 dariusVision-0.0.1/setup.py
+drwxrwxr-x   0 gbox3d    (1000) gbox3d    (1000)        0 2023-04-07 08:13:14.667246 dariusVision-0.0.2/
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)    35149 2023-04-07 04:46:45.000000 dariusVision-0.0.2/LICENSE
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      445 2023-04-07 08:13:14.667246 dariusVision-0.0.2/PKG-INFO
+drwxrwxr-x   0 gbox3d    (1000) gbox3d    (1000)        0 2023-04-07 08:13:14.667246 dariusVision-0.0.2/dariusVision/
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      136 2023-04-07 08:01:25.000000 dariusVision-0.0.2/dariusVision/__init__.py
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)     3265 2023-04-07 01:35:34.000000 dariusVision-0.0.2/dariusVision/cam.py
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)     9681 2023-04-07 08:00:19.000000 dariusVision-0.0.2/dariusVision/realsense2.py
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)     2011 2023-04-07 04:29:23.000000 dariusVision-0.0.2/dariusVision/utils.py
+drwxrwxr-x   0 gbox3d    (1000) gbox3d    (1000)        0 2023-04-07 08:13:14.667246 dariusVision-0.0.2/dariusVision.egg-info/
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      445 2023-04-07 08:13:14.000000 dariusVision-0.0.2/dariusVision.egg-info/PKG-INFO
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      289 2023-04-07 08:13:14.000000 dariusVision-0.0.2/dariusVision.egg-info/SOURCES.txt
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)        1 2023-04-07 08:13:14.000000 dariusVision-0.0.2/dariusVision.egg-info/dependency_links.txt
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)       33 2023-04-07 08:13:14.000000 dariusVision-0.0.2/dariusVision.egg-info/requires.txt
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)       13 2023-04-07 08:13:14.000000 dariusVision-0.0.2/dariusVision.egg-info/top_level.txt
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)       38 2023-04-07 08:13:14.667246 dariusVision-0.0.2/setup.cfg
+-rw-rw-r--   0 gbox3d    (1000) gbox3d    (1000)      644 2023-04-07 08:13:10.000000 dariusVision-0.0.2/setup.py
```

### Comparing `dariusVision-0.0.1/LICENSE` & `dariusVision-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `dariusVision-0.0.1/dariusVision/cam.py` & `dariusVision-0.0.2/dariusVision/cam.py`

 * *Files identical despite different names*

### Comparing `dariusVision-0.0.1/dariusVision/realsense2.py` & `dariusVision-0.0.2/dariusVision/realsense2.py`

 * *Files identical despite different names*

### Comparing `dariusVision-0.0.1/dariusVision/utils.py` & `dariusVision-0.0.2/dariusVision/utils.py`

 * *Files identical despite different names*

### Comparing `dariusVision-0.0.1/setup.py` & `dariusVision-0.0.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 from setuptools import setup
 
 setup(
     name='dariusVision',
-    version='0.0.1',
+    version='0.0.2',
     description='camera utilities to get last frame',
     long_description='camera utilities to get last frame',
     packages=['dariusVision'],
     install_requires=[
         'numpy',
-        'opencv',
+        'opencv-python',
         'pyrealsense2',
     ],
     author='gbox3d',
     author_email='gbox3d@gmail.com',
     url='https://github.com/gbox3d/dariusVision.git',
     classifiers=[
         'Development Status :: 3 - Alpha',
```

