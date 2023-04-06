# Comparing `tmp/tbp-nightly-2.9.0a20221129.tar.gz` & `tmp/tbp-nightly-2.9.0a20221130.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tbp-nightly-2.9.0a20221129.tar", last modified: Tue Nov 29 10:03:37 2022, max compression
+gzip compressed data, was "dist/tbp-nightly-2.9.0a20221130.tar", last modified: Wed Nov 30 10:02:52 2022, max compression
```

## Comparing `tbp-nightly-2.9.0a20221129.tar` & `tbp-nightly-2.9.0a20221130.tar`

### file list

```diff
@@ -1,42 +1,42 @@
-drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/
-drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/
--rw-r--r--   0 xprof     (1002) xprof     (1003)       27 2022-11-29 10:03:36.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/top_level.txt
--rw-r--r--   0 xprof     (1002) xprof     (1003)      856 2022-11-29 10:03:36.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/PKG-INFO
--rw-r--r--   0 xprof     (1002) xprof     (1003)        1 2022-11-29 10:03:36.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 xprof     (1002) xprof     (1003)      102 2022-11-29 10:03:36.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/entry_points.txt
--rw-r--r--   0 xprof     (1002) xprof     (1003)     1631 2022-11-29 10:03:36.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 xprof     (1002) xprof     (1003)       82 2022-11-29 10:03:36.000000 tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/requires.txt
--rw-r--r--   0 xprof     (1002) xprof     (1003)      856 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/PKG-INFO
-drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2604 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/profile_plugin_loader.py
-drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     7584 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/tf_data_stats_proto_to_gviz.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     1515 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/diagnostics.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     3489 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/trace_events_json.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     3851 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/kernel_stats_proto_to_gviz.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     7018 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/raw_to_tool_data.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    12507 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/input_pipeline_proto_to_gviz.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     9202 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/overview_page_proto_to_gviz.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     4351 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/tf_stats_proto_to_gviz.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)      923 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/__init__.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    33648 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/profile_plugin.py
-drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    36464 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/tf_data_stats_pb2.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    46086 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/overview_page_pb2.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2968 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/diagnostics_pb2.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    15668 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/trace_events_pb2.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    42850 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/input_pipeline_pb2.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)    15186 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/tf_stats_pb2.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     9234 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/kernel_stats_pb2.py
-drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/
--r-xr-xr-x   0 xprof     (1002) xprof     (1003)  3455509 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/trace_viewer_index.js
--r-xr-xr-x   0 xprof     (1002) xprof     (1003)    75377 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/styles.css
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)       76 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/index.js
--rw-r--r--   0 xprof     (1002) xprof     (1003)    60832 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/materialicons.woff2
--r-xr-xr-x   0 xprof     (1002) xprof     (1003)   129988 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/trace_viewer_index.html
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2725 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/index.html
--r-xr-xr-x   0 xprof     (1002) xprof     (1003) 20667908 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/bundle.js
--r-xr-xr-x   0 xprof     (1002) xprof     (1003)   556073 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/zone.js
--rw-r--r--   0 xprof     (1002) xprof     (1003)       38 2022-11-29 10:03:37.000000 tbp-nightly-2.9.0a20221129/setup.cfg
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2474 2022-11-29 10:03:34.000000 tbp-nightly-2.9.0a20221129/setup.py
--rwxr-xr-x   0 xprof     (1002) xprof     (1003)       26 2022-11-29 10:03:33.000000 tbp-nightly-2.9.0a20221129/README.rst
+drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/
+drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/
+-rw-r--r--   0 xprof     (1002) xprof     (1003)       27 2022-11-30 10:02:51.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/top_level.txt
+-rw-r--r--   0 xprof     (1002) xprof     (1003)      856 2022-11-30 10:02:51.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 xprof     (1002) xprof     (1003)        1 2022-11-30 10:02:51.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 xprof     (1002) xprof     (1003)      102 2022-11-30 10:02:51.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/entry_points.txt
+-rw-r--r--   0 xprof     (1002) xprof     (1003)     1631 2022-11-30 10:02:51.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 xprof     (1002) xprof     (1003)       82 2022-11-30 10:02:51.000000 tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/requires.txt
+-rw-r--r--   0 xprof     (1002) xprof     (1003)      856 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/PKG-INFO
+drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2604 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/profile_plugin_loader.py
+drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     7584 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/tf_data_stats_proto_to_gviz.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     1515 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/diagnostics.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     3489 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/trace_events_json.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     3851 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/kernel_stats_proto_to_gviz.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     7018 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/raw_to_tool_data.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    12507 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/input_pipeline_proto_to_gviz.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     9202 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/overview_page_proto_to_gviz.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     4351 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/tf_stats_proto_to_gviz.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)      923 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/__init__.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    33648 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/profile_plugin.py
+drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    36464 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/tf_data_stats_pb2.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    46086 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/overview_page_pb2.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2968 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/diagnostics_pb2.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    15668 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/trace_events_pb2.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    42850 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/input_pipeline_pb2.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)    15186 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/tf_stats_pb2.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     9234 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/kernel_stats_pb2.py
+drwxr-xr-x   0 xprof     (1002) xprof     (1003)        0 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/
+-r-xr-xr-x   0 xprof     (1002) xprof     (1003)  3455509 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/trace_viewer_index.js
+-r-xr-xr-x   0 xprof     (1002) xprof     (1003)    75377 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/styles.css
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)       76 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/index.js
+-rw-r--r--   0 xprof     (1002) xprof     (1003)    60832 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/materialicons.woff2
+-r-xr-xr-x   0 xprof     (1002) xprof     (1003)   129988 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/trace_viewer_index.html
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2725 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/index.html
+-r-xr-xr-x   0 xprof     (1002) xprof     (1003) 20667908 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/bundle.js
+-r-xr-xr-x   0 xprof     (1002) xprof     (1003)   556073 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/zone.js
+-rw-r--r--   0 xprof     (1002) xprof     (1003)       38 2022-11-30 10:02:52.000000 tbp-nightly-2.9.0a20221130/setup.cfg
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)     2474 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/setup.py
+-rwxr-xr-x   0 xprof     (1002) xprof     (1003)       26 2022-11-30 10:02:49.000000 tbp-nightly-2.9.0a20221130/README.rst
```

### Comparing `tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/PKG-INFO` & `tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tbp-nightly
-Version: 2.9.0a20221129
+Version: 2.9.0a20221130
 Summary: Profile Tensorboard Plugin
 Home-page: https://github.com/tensorflow/profiler
 Author: Google Inc.
 Author-email: packages@tensorflow.org
 License: Apache 2.0
 Keywords: tensorflow tensorboard xprof profile plugin
 Platform: UNKNOWN
```

### Comparing `tbp-nightly-2.9.0a20221129/tbp_nightly.egg-info/SOURCES.txt` & `tbp-nightly-2.9.0a20221130/tbp_nightly.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/PKG-INFO` & `tbp-nightly-2.9.0a20221130/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tbp-nightly
-Version: 2.9.0a20221129
+Version: 2.9.0a20221130
 Summary: Profile Tensorboard Plugin
 Home-page: https://github.com/tensorflow/profiler
 Author: Google Inc.
 Author-email: packages@tensorflow.org
 License: Apache 2.0
 Keywords: tensorflow tensorboard xprof profile plugin
 Platform: UNKNOWN
```

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/profile_plugin_loader.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/profile_plugin_loader.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/tf_data_stats_proto_to_gviz.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/tf_data_stats_proto_to_gviz.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/diagnostics.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/diagnostics.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/trace_events_json.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/trace_events_json.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/kernel_stats_proto_to_gviz.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/kernel_stats_proto_to_gviz.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/raw_to_tool_data.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/raw_to_tool_data.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/input_pipeline_proto_to_gviz.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/input_pipeline_proto_to_gviz.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/overview_page_proto_to_gviz.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/overview_page_proto_to_gviz.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/convert/tf_stats_proto_to_gviz.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/convert/tf_stats_proto_to_gviz.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/__init__.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/__init__.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/profile_plugin.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/profile_plugin.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/tf_data_stats_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/tf_data_stats_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/overview_page_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/overview_page_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/diagnostics_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/diagnostics_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/trace_events_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/trace_events_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/input_pipeline_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/input_pipeline_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/tf_stats_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/tf_stats_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/protobuf/kernel_stats_pb2.py` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/protobuf/kernel_stats_pb2.py`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/trace_viewer_index.js` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/trace_viewer_index.js`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/styles.css` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/styles.css`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/materialicons.woff2` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/materialicons.woff2`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/trace_viewer_index.html` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/trace_viewer_index.html`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/index.html` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/index.html`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/bundle.js` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/bundle.js`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/tensorboard_plugin_profile/static/zone.js` & `tbp-nightly-2.9.0a20221130/tensorboard_plugin_profile/static/zone.js`

 * *Files identical despite different names*

### Comparing `tbp-nightly-2.9.0a20221129/setup.py` & `tbp-nightly-2.9.0a20221130/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 from __future__ import absolute_import
 from __future__ import division
 from __future__ import print_function
 
 import setuptools
 
 PROJECT_NAME = 'tbp-nightly'
-VERSION = '2.9.0a20221129'
+VERSION = '2.9.0a20221130'
 REQUIRED_PACKAGES = [
     'gviz_api >= 1.9.0',
     'protobuf >= 3.12.0',
     'setuptools >= 41.0.0',
     'six >= 1.10.0',
     'werkzeug >= 0.11.15',
 ]
```

