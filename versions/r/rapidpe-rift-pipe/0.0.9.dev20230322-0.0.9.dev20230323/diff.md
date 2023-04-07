# Comparing `tmp/rapidpe_rift_pipe-0.0.9.dev20230322.tar.gz` & `tmp/rapidpe_rift_pipe-0.0.9.dev20230323.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rapidpe_rift_pipe-0.0.9.dev20230322.tar", last modified: Wed Mar 22 05:15:54 2023, max compression
+gzip compressed data, was "rapidpe_rift_pipe-0.0.9.dev20230323.tar", last modified: Thu Mar 23 05:16:12 2023, max compression
```

## Comparing `rapidpe_rift_pipe-0.0.9.dev20230322.tar` & `rapidpe_rift_pipe-0.0.9.dev20230323.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.264125 rapidpe_rift_pipe-0.0.9.dev20230322/
--rw-rw-rw-   0 root         (0) root         (0)    18046 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/COPYING
--rw-rw-rw-   0 root         (0) root         (0)       59 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1140 2023-03-22 05:15:54.264125 rapidpe_rift_pipe-0.0.9.dev20230322/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      327 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.255125 rapidpe_rift_pipe-0.0.9.dev20230322/bin/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.258125 rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/
--rwxrwxrwx   0 root         (0) root         (0)    12423 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/convert_result_to_txt.py
--rw-rw-rw-   0 root         (0) root         (0)     5745 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/cprofile_summary.py
--rw-rw-rw-   0 root         (0) root         (0)     7599 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/create_summarypage.py
--rw-rw-rw-   0 root         (0) root         (0)    14833 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/plot_intrinsic_posterior.py
--rw-rw-rw-   0 root         (0) root         (0)     3164 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/plot_skymap.py
--rw-rw-rw-   0 root         (0) root         (0)     1348 2023-03-22 05:15:54.266125 rapidpe_rift_pipe-0.0.9.dev20230322/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)       38 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.255125 rapidpe_rift_pipe-0.0.9.dev20230322/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.261125 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/
--rw-rw-rw-   0 root         (0) root         (0)       78 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    35593 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/cli.py
--rw-rw-rw-   0 root         (0) root         (0)    16803 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/config.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.256125 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/config_files/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.264125 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/config_files/search_bias_bounds/
--rw-rw-rw-   0 root         (0) root         (0)     4488 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/config_files/search_bias_bounds/default.json
--rwxrwxrwx   0 root         (0) root         (0)    30455 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/create_submit_dag_one_event.py
--rw-rw-rw-   0 root         (0) root         (0)     9701 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/modules.py
--rw-rw-rw-   0 root         (0) root         (0)    10717 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/postscript_utils.py
--rw-rw-rw-   0 root         (0) root         (0)     2260 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/profiling.py
--rw-rw-rw-   0 root         (0) root         (0)     2412 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/search_bias_bounds.py
--rw-rw-rw-   0 root         (0) root         (0)       75 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/test_cli.py
--rw-rw-rw-   0 root         (0) root         (0)     2064 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/test_config.py
--rw-rw-rw-   0 root         (0) root         (0)      369 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/test_modules.py
--rw-rw-rw-   0 root         (0) root         (0)      199 2023-03-22 05:15:34.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:15:54.264125 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1140 2023-03-22 05:15:54.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1059 2023-03-22 05:15:54.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-22 05:15:54.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       65 2023-03-22 05:15:54.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)       71 2023-03-22 05:15:54.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       18 2023-03-22 05:15:54.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-22 05:15:53.000000 rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/zip-safe
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.997842 rapidpe_rift_pipe-0.0.9.dev20230323/
+-rw-rw-rw-   0 root         (0) root         (0)    18046 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/COPYING
+-rw-rw-rw-   0 root         (0) root         (0)       59 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1140 2023-03-23 05:16:11.997842 rapidpe_rift_pipe-0.0.9.dev20230323/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)      327 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.991842 rapidpe_rift_pipe-0.0.9.dev20230323/bin/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.993842 rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/
+-rwxrwxrwx   0 root         (0) root         (0)    12423 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/convert_result_to_txt.py
+-rw-rw-rw-   0 root         (0) root         (0)     5745 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/cprofile_summary.py
+-rw-rw-rw-   0 root         (0) root         (0)     7599 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/create_summarypage.py
+-rw-rw-rw-   0 root         (0) root         (0)    14833 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/plot_intrinsic_posterior.py
+-rw-rw-rw-   0 root         (0) root         (0)     3164 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/plot_skymap.py
+-rw-rw-rw-   0 root         (0) root         (0)     1348 2023-03-23 05:16:11.999842 rapidpe_rift_pipe-0.0.9.dev20230323/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)       38 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.991842 rapidpe_rift_pipe-0.0.9.dev20230323/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.995842 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/
+-rw-rw-rw-   0 root         (0) root         (0)       78 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    35593 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/cli.py
+-rw-rw-rw-   0 root         (0) root         (0)    16803 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/config.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.991842 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/config_files/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.997842 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/config_files/search_bias_bounds/
+-rw-rw-rw-   0 root         (0) root         (0)     4488 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/config_files/search_bias_bounds/default.json
+-rwxrwxrwx   0 root         (0) root         (0)    30455 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/create_submit_dag_one_event.py
+-rw-rw-rw-   0 root         (0) root         (0)     9701 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/modules.py
+-rw-rw-rw-   0 root         (0) root         (0)    10717 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/postscript_utils.py
+-rw-rw-rw-   0 root         (0) root         (0)     2260 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/profiling.py
+-rw-rw-rw-   0 root         (0) root         (0)     2412 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/search_bias_bounds.py
+-rw-rw-rw-   0 root         (0) root         (0)       75 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/test_cli.py
+-rw-rw-rw-   0 root         (0) root         (0)     2064 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/test_config.py
+-rw-rw-rw-   0 root         (0) root         (0)      369 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/test_modules.py
+-rw-rw-rw-   0 root         (0) root         (0)      199 2023-03-23 05:15:48.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 05:16:11.996842 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1140 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1059 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       65 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)       71 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       18 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-03-23 05:16:11.000000 rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/zip-safe
```

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/COPYING` & `rapidpe_rift_pipe-0.0.9.dev20230323/COPYING`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/PKG-INFO` & `rapidpe_rift_pipe-0.0.9.dev20230323/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rapidpe_rift_pipe
-Version: 0.0.9.dev20230322
+Version: 0.0.9.dev20230323
 Summary: Pipeline for running RapidPE and RIFT parameter estimation codes
 License: GPL-2+
 Keywords: parameter estimation,gravitational waves
 Classifier: Development Status :: 3 - Alpha
 Classifier: License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
 Classifier: Intended Audience :: Science/Research
 Classifier: Natural Language :: English
```

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/convert_result_to_txt.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/convert_result_to_txt.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/cprofile_summary.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/cprofile_summary.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/create_summarypage.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/create_summarypage.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/plot_intrinsic_posterior.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/plot_intrinsic_posterior.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/bin/postscripts/plot_skymap.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/bin/postscripts/plot_skymap.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/setup.cfg` & `rapidpe_rift_pipe-0.0.9.dev20230323/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -45,10 +45,10 @@
 rapidpe_rift_pipe.static = *.html, *.css, *.js
 
 [options.entry_points]
 console_scripts = 
 	rapidpe-rift-pipe = rapidpe_rift_pipe.cli:main
 
 [egg_info]
-tag_build = dev.20230322
+tag_build = dev.20230323
 tag_date = 0
```

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/cli.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/cli.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/config.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/config.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/config_files/search_bias_bounds/default.json` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/config_files/search_bias_bounds/default.json`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/create_submit_dag_one_event.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/create_submit_dag_one_event.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/modules.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/modules.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/postscript_utils.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/postscript_utils.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/profiling.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/profiling.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/search_bias_bounds.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/search_bias_bounds.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe/test_config.py` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe/test_config.py`

 * *Files identical despite different names*

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/PKG-INFO` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rapidpe-rift-pipe
-Version: 0.0.9.dev20230322
+Version: 0.0.9.dev20230323
 Summary: Pipeline for running RapidPE and RIFT parameter estimation codes
 License: GPL-2+
 Keywords: parameter estimation,gravitational waves
 Classifier: Development Status :: 3 - Alpha
 Classifier: License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)
 Classifier: Intended Audience :: Science/Research
 Classifier: Natural Language :: English
```

### Comparing `rapidpe_rift_pipe-0.0.9.dev20230322/src/rapidpe_rift_pipe.egg-info/SOURCES.txt` & `rapidpe_rift_pipe-0.0.9.dev20230323/src/rapidpe_rift_pipe.egg-info/SOURCES.txt`

 * *Files identical despite different names*

