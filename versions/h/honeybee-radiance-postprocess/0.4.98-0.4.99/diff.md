# Comparing `tmp/honeybee-radiance-postprocess-0.4.98.tar.gz` & `tmp/honeybee-radiance-postprocess-0.4.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/honeybee-radiance-postprocess-0.4.98.tar", last modified: Mon Nov  7 20:44:21 2022, max compression
+gzip compressed data, was "dist/honeybee-radiance-postprocess-0.4.99.tar", last modified: Mon Nov  7 21:47:41 2022, max compression
```

## Comparing `honeybee-radiance-postprocess-0.4.98.tar` & `honeybee-radiance-postprocess-0.4.99.tar`

### file list

```diff
@@ -1,41 +1,41 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/
--rw-r--r--   0 runner    (1001) docker     (121)      279 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (121)      445 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (121)    34523 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      181 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1495 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      811 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/dev-requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/
--rw-r--r--   0 runner    (1001) docker     (121)       45 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      104 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1973 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/annual.py
--rw-r--r--   0 runner    (1001) docker     (121)     9439 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/annualdaylight.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/
--rw-r--r--   0 runner    (1001) docker     (121)      777 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3721 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/grid.py
--rw-r--r--   0 runner    (1001) docker     (121)     3072 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/leed.py
--rw-r--r--   0 runner    (1001) docker     (121)     5015 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/mtxop.py
--rw-r--r--   0 runner    (1001) docker     (121)    17758 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/postprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)     3884 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/schedule.py
--rw-r--r--   0 runner    (1001) docker     (121)     4031 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/translate.py
--rw-r--r--   0 runner    (1001) docker     (121)     3155 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/two_phase.py
--rw-r--r--   0 runner    (1001) docker     (121)     4077 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/util.py
--rw-r--r--   0 runner    (1001) docker     (121)      732 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/electriclight.py
--rw-r--r--   0 runner    (1001) docker     (121)     7777 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/en17037.py
--rw-r--r--   0 runner    (1001) docker     (121)    20964 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/leed.py
--rw-r--r--   0 runner    (1001) docker     (121)    13508 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/metrics.py
--rw-r--r--   0 runner    (1001) docker     (121)     2367 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/reader.py
--rw-r--r--   0 runner    (1001) docker     (121)    65488 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/results.py
--rw-r--r--   0 runner    (1001) docker     (121)      802 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/type_hints.py
--rw-r--r--   0 runner    (1001) docker     (121)     5425 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1347 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       97 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)       41 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       30 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       41 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      102 2022-11-07 20:44:21.000000 honeybee-radiance-postprocess-0.4.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1208 2022-11-07 20:43:09.000000 honeybee-radiance-postprocess-0.4.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/
+-rw-r--r--   0 runner    (1001) docker     (121)      279 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (121)      445 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (121)    34523 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      181 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1495 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      811 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/dev-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/
+-rw-r--r--   0 runner    (1001) docker     (121)       45 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      104 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1973 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/annual.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9439 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/annualdaylight.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/
+-rw-r--r--   0 runner    (1001) docker     (121)      777 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3721 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/grid.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3072 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/leed.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5015 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/mtxop.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17758 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/postprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3884 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/schedule.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4031 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/translate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3155 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/two_phase.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4077 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/util.py
+-rw-r--r--   0 runner    (1001) docker     (121)      732 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/electriclight.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7777 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/en17037.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20964 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/leed.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13508 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2367 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/reader.py
+-rw-r--r--   0 runner    (1001) docker     (121)    65488 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/results.py
+-rw-r--r--   0 runner    (1001) docker     (121)      802 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/type_hints.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5425 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1347 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       97 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       41 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       30 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       41 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      102 2022-11-07 21:47:41.000000 honeybee-radiance-postprocess-0.4.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1208 2022-11-07 21:46:21.000000 honeybee-radiance-postprocess-0.4.99/setup.py
```

### Comparing `honeybee-radiance-postprocess-0.4.98/LICENSE` & `honeybee-radiance-postprocess-0.4.99/LICENSE`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/PKG-INFO` & `honeybee-radiance-postprocess-0.4.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-radiance-postprocess
-Version: 0.4.98
+Version: 0.4.99
 Summary: Postprocessing of Radiance results and matrices
 Home-page: https://github.com/ladybug-tools/honeybee-radiance-postprocess
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: GPLv3
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `honeybee-radiance-postprocess-0.4.98/README.md` & `honeybee-radiance-postprocess-0.4.99/README.md`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/dev-requirements.txt` & `honeybee-radiance-postprocess-0.4.99/dev-requirements.txt`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/annual.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/annual.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/annualdaylight.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/annualdaylight.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/__init__.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/grid.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/grid.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/leed.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/leed.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/mtxop.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/mtxop.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/postprocess.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/postprocess.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/schedule.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/schedule.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/translate.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/translate.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/two_phase.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/two_phase.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/cli/util.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/cli/util.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/electriclight.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/electriclight.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/en17037.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/en17037.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/leed.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/leed.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/metrics.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/metrics.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/reader.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/reader.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/results.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/results.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/type_hints.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/type_hints.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess/util.py` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess/util.py`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/PKG-INFO` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: honeybee-radiance-postprocess
-Version: 0.4.98
+Version: 0.4.99
 Summary: Postprocessing of Radiance results and matrices
 Home-page: https://github.com/ladybug-tools/honeybee-radiance-postprocess
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: GPLv3
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `honeybee-radiance-postprocess-0.4.98/honeybee_radiance_postprocess.egg-info/SOURCES.txt` & `honeybee-radiance-postprocess-0.4.99/honeybee_radiance_postprocess.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `honeybee-radiance-postprocess-0.4.98/setup.py` & `honeybee-radiance-postprocess-0.4.99/setup.py`

 * *Files identical despite different names*

