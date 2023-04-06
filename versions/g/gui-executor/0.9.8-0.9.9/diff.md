# Comparing `tmp/gui-executor-0.9.8.tar.gz` & `tmp/gui-executor-0.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gui-executor-0.9.8.tar", last modified: Fri Oct  7 12:21:06 2022, max compression
+gzip compressed data, was "gui-executor-0.9.9.tar", last modified: Mon Oct 24 14:34:46 2022, max compression
```

## Comparing `gui-executor-0.9.8.tar` & `gui-executor-0.9.9.tar`

### file list

```diff
@@ -1,52 +1,52 @@
-drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-07 12:21:06.059815 gui-executor-0.9.8/
--rw-r--r--   0 rik      (459800007) staff       (20)      901 2022-10-07 12:21:06.059585 gui-executor-0.9.8/PKG-INFO
--rw-r--r--   0 rik      (459800007) staff       (20)      276 2022-09-01 12:19:00.000000 gui-executor-0.9.8/README.md
--rw-r--r--   0 rik      (459800007) staff       (20)       38 2022-10-07 12:21:06.059914 gui-executor-0.9.8/setup.cfg
--rw-r--r--   0 rik      (459800007) staff       (20)     3040 2022-09-18 08:40:56.000000 gui-executor-0.9.8/setup.py
-drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-07 12:21:06.027910 gui-executor-0.9.8/src/
-drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-07 12:21:06.041925 gui-executor-0.9.8/src/gui_executor/
--rw-r--r--   0 rik      (459800007) staff       (20)       83 2022-08-26 10:12:05.000000 gui-executor-0.9.8/src/gui_executor/__init__.py
--rw-r--r--   0 rik      (459800007) staff       (20)     4193 2022-10-07 12:18:33.000000 gui-executor-0.9.8/src/gui_executor/__main__.py
--rw-r--r--   0 rik      (459800007) staff       (20)      118 2022-10-07 12:19:47.000000 gui-executor-0.9.8/src/gui_executor/__version__.py
--rw-r--r--   0 rik      (459800007) staff       (20)     7991 2022-08-17 08:21:53.000000 gui-executor-0.9.8/src/gui_executor/command.py
--rw-r--r--   0 rik      (459800007) staff       (20)     4419 2022-08-17 08:21:53.000000 gui-executor-0.9.8/src/gui_executor/config.py
--rw-r--r--   0 rik      (459800007) staff       (20)     1271 2022-09-12 12:00:30.000000 gui-executor-0.9.8/src/gui_executor/control.py
--rw-r--r--   0 rik      (459800007) staff       (20)     8335 2022-09-27 10:20:23.000000 gui-executor-0.9.8/src/gui_executor/exec.py
--rw-r--r--   0 rik      (459800007) staff       (20)      843 2022-08-31 09:15:51.000000 gui-executor-0.9.8/src/gui_executor/gui.py
-drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-07 12:21:06.058912 gui-executor-0.9.8/src/gui_executor/icons/
--rw-r--r--   0 rik      (459800007) staff       (20)     6172 2022-08-24 12:10:42.000000 gui-executor-0.9.8/src/gui_executor/icons/add.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     2676 2022-08-31 15:47:27.000000 gui-executor-0.9.8/src/gui_executor/icons/arrow-down-selected.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     2657 2022-08-31 15:33:38.000000 gui-executor-0.9.8/src/gui_executor/icons/arrow-down.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     2716 2022-08-31 15:49:00.000000 gui-executor-0.9.8/src/gui_executor/icons/arrow-up-selected.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     2697 2022-08-31 15:32:50.000000 gui-executor-0.9.8/src/gui_executor/icons/arrow-up.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     7715 2022-08-19 13:13:30.000000 gui-executor-0.9.8/src/gui_executor/icons/command.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     7239 2022-08-24 10:55:54.000000 gui-executor-0.9.8/src/gui_executor/icons/delete.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     3996 2022-09-01 09:13:36.000000 gui-executor-0.9.8/src/gui_executor/icons/filename.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     5673 2022-09-01 09:32:21.000000 gui-executor-0.9.8/src/gui_executor/icons/filepath.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     2345 2022-08-31 21:02:09.000000 gui-executor-0.9.8/src/gui_executor/icons/folder.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     9793 2022-09-05 07:38:54.000000 gui-executor-0.9.8/src/gui_executor/icons/hexapod-homing-selected.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     9793 2022-09-05 07:38:33.000000 gui-executor-0.9.8/src/gui_executor/icons/hexapod-homing.svg
--rw-r--r--   0 rik      (459800007) staff       (20)    10219 2022-09-05 07:03:01.000000 gui-executor-0.9.8/src/gui_executor/icons/hexapod-retract-selected.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     7877 2022-09-02 19:45:54.000000 gui-executor-0.9.8/src/gui_executor/icons/hexapod-retract.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     5999 2022-05-18 07:38:46.000000 gui-executor-0.9.8/src/gui_executor/icons/processing.svg
--rw-r--r--   0 rik      (459800007) staff       (20)    15320 2022-08-22 15:46:18.000000 gui-executor-0.9.8/src/gui_executor/icons/reload-kernel.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     5508 2022-08-19 13:35:23.000000 gui-executor-0.9.8/src/gui_executor/icons/reload.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     6864 2022-08-31 08:47:41.000000 gui-executor-0.9.8/src/gui_executor/icons/script-function-selected.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     4498 2022-05-18 07:38:46.000000 gui-executor-0.9.8/src/gui_executor/icons/script-function.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     1581 2022-08-25 16:16:33.000000 gui-executor-0.9.8/src/gui_executor/icons/script_app.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     1294 2022-09-07 14:47:39.000000 gui-executor-0.9.8/src/gui_executor/icons/stop.svg
--rw-r--r--   0 rik      (459800007) staff       (20)    14191 2022-08-17 19:03:57.000000 gui-executor-0.9.8/src/gui_executor/icons/tasks.svg
--rw-r--r--   0 rik      (459800007) staff       (20)     6307 2022-09-19 19:38:06.000000 gui-executor-0.9.8/src/gui_executor/kernel.py
--rw-r--r--   0 rik      (459800007) staff       (20)      854 2022-09-12 12:05:19.000000 gui-executor-0.9.8/src/gui_executor/model.py
--rw-r--r--   0 rik      (459800007) staff       (20)     4190 2022-09-01 21:17:48.000000 gui-executor-0.9.8/src/gui_executor/script_app.py
--rw-r--r--   0 rik      (459800007) staff       (20)     3986 2022-09-18 11:10:01.000000 gui-executor-0.9.8/src/gui_executor/transforms.py
--rw-r--r--   0 rik      (459800007) staff       (20)    12201 2022-09-20 20:54:36.000000 gui-executor-0.9.8/src/gui_executor/utils.py
--rw-r--r--   0 rik      (459800007) staff       (20)     4282 2022-08-29 08:27:55.000000 gui-executor-0.9.8/src/gui_executor/utypes.py
--rw-r--r--   0 rik      (459800007) staff       (20)    51686 2022-09-27 11:00:16.000000 gui-executor-0.9.8/src/gui_executor/view.py
-drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-07 12:21:06.044452 gui-executor-0.9.8/src/gui_executor.egg-info/
--rw-r--r--   0 rik      (459800007) staff       (20)      901 2022-10-07 12:21:05.000000 gui-executor-0.9.8/src/gui_executor.egg-info/PKG-INFO
--rw-r--r--   0 rik      (459800007) staff       (20)     1546 2022-10-07 12:21:05.000000 gui-executor-0.9.8/src/gui_executor.egg-info/SOURCES.txt
--rw-r--r--   0 rik      (459800007) staff       (20)        1 2022-10-07 12:21:05.000000 gui-executor-0.9.8/src/gui_executor.egg-info/dependency_links.txt
--rw-r--r--   0 rik      (459800007) staff       (20)       57 2022-10-07 12:21:05.000000 gui-executor-0.9.8/src/gui_executor.egg-info/entry_points.txt
--rw-r--r--   0 rik      (459800007) staff       (20)      130 2022-10-07 12:21:05.000000 gui-executor-0.9.8/src/gui_executor.egg-info/requires.txt
--rw-r--r--   0 rik      (459800007) staff       (20)       32 2022-10-07 12:21:05.000000 gui-executor-0.9.8/src/gui_executor.egg-info/top_level.txt
+drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-24 14:34:46.878686 gui-executor-0.9.9/
+-rw-r--r--   0 rik      (459800007) staff       (20)      901 2022-10-24 14:34:46.878372 gui-executor-0.9.9/PKG-INFO
+-rw-r--r--   0 rik      (459800007) staff       (20)      276 2022-09-01 12:19:00.000000 gui-executor-0.9.9/README.md
+-rw-r--r--   0 rik      (459800007) staff       (20)       38 2022-10-24 14:34:46.878839 gui-executor-0.9.9/setup.cfg
+-rw-r--r--   0 rik      (459800007) staff       (20)     3040 2022-09-18 08:40:56.000000 gui-executor-0.9.9/setup.py
+drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-24 14:34:46.828778 gui-executor-0.9.9/src/
+drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-24 14:34:46.844001 gui-executor-0.9.9/src/gui_executor/
+-rw-r--r--   0 rik      (459800007) staff       (20)       83 2022-08-26 10:12:05.000000 gui-executor-0.9.9/src/gui_executor/__init__.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     4193 2022-10-07 12:18:33.000000 gui-executor-0.9.9/src/gui_executor/__main__.py
+-rw-r--r--   0 rik      (459800007) staff       (20)      118 2022-10-24 14:33:54.000000 gui-executor-0.9.9/src/gui_executor/__version__.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     7991 2022-08-17 08:21:53.000000 gui-executor-0.9.9/src/gui_executor/command.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     4419 2022-08-17 08:21:53.000000 gui-executor-0.9.9/src/gui_executor/config.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     1271 2022-09-12 12:00:30.000000 gui-executor-0.9.9/src/gui_executor/control.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     8335 2022-09-27 10:20:23.000000 gui-executor-0.9.9/src/gui_executor/exec.py
+-rw-r--r--   0 rik      (459800007) staff       (20)      843 2022-08-31 09:15:51.000000 gui-executor-0.9.9/src/gui_executor/gui.py
+drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-24 14:34:46.877420 gui-executor-0.9.9/src/gui_executor/icons/
+-rw-r--r--   0 rik      (459800007) staff       (20)     6172 2022-08-24 12:10:42.000000 gui-executor-0.9.9/src/gui_executor/icons/add.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     2676 2022-08-31 15:47:27.000000 gui-executor-0.9.9/src/gui_executor/icons/arrow-down-selected.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     2657 2022-08-31 15:33:38.000000 gui-executor-0.9.9/src/gui_executor/icons/arrow-down.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     2716 2022-08-31 15:49:00.000000 gui-executor-0.9.9/src/gui_executor/icons/arrow-up-selected.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     2697 2022-08-31 15:32:50.000000 gui-executor-0.9.9/src/gui_executor/icons/arrow-up.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     7715 2022-08-19 13:13:30.000000 gui-executor-0.9.9/src/gui_executor/icons/command.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     7239 2022-08-24 10:55:54.000000 gui-executor-0.9.9/src/gui_executor/icons/delete.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     3996 2022-09-01 09:13:36.000000 gui-executor-0.9.9/src/gui_executor/icons/filename.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     5673 2022-09-01 09:32:21.000000 gui-executor-0.9.9/src/gui_executor/icons/filepath.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     2345 2022-08-31 21:02:09.000000 gui-executor-0.9.9/src/gui_executor/icons/folder.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     9793 2022-09-05 07:38:54.000000 gui-executor-0.9.9/src/gui_executor/icons/hexapod-homing-selected.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     9793 2022-09-05 07:38:33.000000 gui-executor-0.9.9/src/gui_executor/icons/hexapod-homing.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)    10219 2022-09-05 07:03:01.000000 gui-executor-0.9.9/src/gui_executor/icons/hexapod-retract-selected.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     7877 2022-09-02 19:45:54.000000 gui-executor-0.9.9/src/gui_executor/icons/hexapod-retract.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     5999 2022-05-18 07:38:46.000000 gui-executor-0.9.9/src/gui_executor/icons/processing.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)    15320 2022-08-22 15:46:18.000000 gui-executor-0.9.9/src/gui_executor/icons/reload-kernel.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     5508 2022-08-19 13:35:23.000000 gui-executor-0.9.9/src/gui_executor/icons/reload.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     6864 2022-08-31 08:47:41.000000 gui-executor-0.9.9/src/gui_executor/icons/script-function-selected.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     4498 2022-05-18 07:38:46.000000 gui-executor-0.9.9/src/gui_executor/icons/script-function.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     1581 2022-08-25 16:16:33.000000 gui-executor-0.9.9/src/gui_executor/icons/script_app.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     1294 2022-09-07 14:47:39.000000 gui-executor-0.9.9/src/gui_executor/icons/stop.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)    14191 2022-08-17 19:03:57.000000 gui-executor-0.9.9/src/gui_executor/icons/tasks.svg
+-rw-r--r--   0 rik      (459800007) staff       (20)     6307 2022-09-19 19:38:06.000000 gui-executor-0.9.9/src/gui_executor/kernel.py
+-rw-r--r--   0 rik      (459800007) staff       (20)      854 2022-09-12 12:05:19.000000 gui-executor-0.9.9/src/gui_executor/model.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     4233 2022-10-23 09:01:53.000000 gui-executor-0.9.9/src/gui_executor/script_app.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     3986 2022-09-18 11:10:01.000000 gui-executor-0.9.9/src/gui_executor/transforms.py
+-rw-r--r--   0 rik      (459800007) staff       (20)    12201 2022-09-20 20:54:36.000000 gui-executor-0.9.9/src/gui_executor/utils.py
+-rw-r--r--   0 rik      (459800007) staff       (20)     4282 2022-08-29 08:27:55.000000 gui-executor-0.9.9/src/gui_executor/utypes.py
+-rw-r--r--   0 rik      (459800007) staff       (20)    52507 2022-10-24 13:16:55.000000 gui-executor-0.9.9/src/gui_executor/view.py
+drwxr-xr-x   0 rik      (459800007) staff       (20)        0 2022-10-24 14:34:46.848626 gui-executor-0.9.9/src/gui_executor.egg-info/
+-rw-r--r--   0 rik      (459800007) staff       (20)      901 2022-10-24 14:34:46.000000 gui-executor-0.9.9/src/gui_executor.egg-info/PKG-INFO
+-rw-r--r--   0 rik      (459800007) staff       (20)     1546 2022-10-24 14:34:46.000000 gui-executor-0.9.9/src/gui_executor.egg-info/SOURCES.txt
+-rw-r--r--   0 rik      (459800007) staff       (20)        1 2022-10-24 14:34:46.000000 gui-executor-0.9.9/src/gui_executor.egg-info/dependency_links.txt
+-rw-r--r--   0 rik      (459800007) staff       (20)       57 2022-10-24 14:34:46.000000 gui-executor-0.9.9/src/gui_executor.egg-info/entry_points.txt
+-rw-r--r--   0 rik      (459800007) staff       (20)      130 2022-10-24 14:34:46.000000 gui-executor-0.9.9/src/gui_executor.egg-info/requires.txt
+-rw-r--r--   0 rik      (459800007) staff       (20)       32 2022-10-24 14:34:46.000000 gui-executor-0.9.9/src/gui_executor.egg-info/top_level.txt
```

### Comparing `gui-executor-0.9.8/PKG-INFO` & `gui-executor-0.9.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gui-executor
-Version: 0.9.8
+Version: 0.9.9
 Summary: Execute Python code in an automatically generated GUI App.
 Home-page: https://github.com/rhuygen/gui-executor
 Author: Rik Huygen
 Author-email: rik.huygen@kuleuven.be
 License: MIT
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `gui-executor-0.9.8/setup.py` & `gui-executor-0.9.9/setup.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/__main__.py` & `gui-executor-0.9.9/src/gui_executor/__main__.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/command.py` & `gui-executor-0.9.9/src/gui_executor/command.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/config.py` & `gui-executor-0.9.9/src/gui_executor/config.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/control.py` & `gui-executor-0.9.9/src/gui_executor/control.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/exec.py` & `gui-executor-0.9.9/src/gui_executor/exec.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/gui.py` & `gui-executor-0.9.9/src/gui_executor/gui.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/add.svg` & `gui-executor-0.9.9/src/gui_executor/icons/add.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/arrow-down-selected.svg` & `gui-executor-0.9.9/src/gui_executor/icons/arrow-down-selected.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/arrow-down.svg` & `gui-executor-0.9.9/src/gui_executor/icons/arrow-down.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/arrow-up-selected.svg` & `gui-executor-0.9.9/src/gui_executor/icons/arrow-up-selected.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/arrow-up.svg` & `gui-executor-0.9.9/src/gui_executor/icons/arrow-up.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/command.svg` & `gui-executor-0.9.9/src/gui_executor/icons/command.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/delete.svg` & `gui-executor-0.9.9/src/gui_executor/icons/delete.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/filename.svg` & `gui-executor-0.9.9/src/gui_executor/icons/filename.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/filepath.svg` & `gui-executor-0.9.9/src/gui_executor/icons/filepath.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/folder.svg` & `gui-executor-0.9.9/src/gui_executor/icons/folder.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/hexapod-homing-selected.svg` & `gui-executor-0.9.9/src/gui_executor/icons/hexapod-homing-selected.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/hexapod-homing.svg` & `gui-executor-0.9.9/src/gui_executor/icons/hexapod-homing.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/hexapod-retract-selected.svg` & `gui-executor-0.9.9/src/gui_executor/icons/hexapod-retract-selected.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/hexapod-retract.svg` & `gui-executor-0.9.9/src/gui_executor/icons/hexapod-retract.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/processing.svg` & `gui-executor-0.9.9/src/gui_executor/icons/processing.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/reload-kernel.svg` & `gui-executor-0.9.9/src/gui_executor/icons/reload-kernel.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/reload.svg` & `gui-executor-0.9.9/src/gui_executor/icons/reload.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/script-function-selected.svg` & `gui-executor-0.9.9/src/gui_executor/icons/script-function-selected.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/script-function.svg` & `gui-executor-0.9.9/src/gui_executor/icons/script-function.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/script_app.svg` & `gui-executor-0.9.9/src/gui_executor/icons/script_app.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/stop.svg` & `gui-executor-0.9.9/src/gui_executor/icons/stop.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/icons/tasks.svg` & `gui-executor-0.9.9/src/gui_executor/icons/tasks.svg`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/kernel.py` & `gui-executor-0.9.9/src/gui_executor/kernel.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/model.py` & `gui-executor-0.9.9/src/gui_executor/model.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/script_app.py` & `gui-executor-0.9.9/src/gui_executor/script_app.py`

 * *Files 1% similar despite different names*

```diff
@@ -90,14 +90,15 @@
                 canvas_box.setContentsMargins(0, 0, 0, 0)
                 sc = PlotCanvas(fig)
                 toolbar = NavigationToolbar(sc, self)
                 toolbar.setIconSize(QSize(18, 18))  # TODO: this should be configurable
                 canvas_box.addWidget(sc)
                 canvas_box.addWidget(toolbar)
                 hbox.addLayout(canvas_box)
+                fig.set_tight_layout(True)
 
             widget = QWidget()
             width = 960
             widget.setLayout(hbox)
             widget.setMinimumSize(width, int(width / self.ratio))
 
             self.figures_layout.addWidget(widget)
```

### Comparing `gui-executor-0.9.8/src/gui_executor/transforms.py` & `gui-executor-0.9.9/src/gui_executor/transforms.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/utils.py` & `gui-executor-0.9.9/src/gui_executor/utils.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/utypes.py` & `gui-executor-0.9.9/src/gui_executor/utypes.py`

 * *Files identical despite different names*

### Comparing `gui-executor-0.9.8/src/gui_executor/view.py` & `gui-executor-0.9.9/src/gui_executor/view.py`

 * *Files 1% similar despite different names*

```diff
@@ -1155,14 +1155,34 @@
         info = self._kernel.get_kernel_info()
         if 'banner' in info['content']:
             self._console_panel.append(info['content']['banner'])
 
         # make sure the user doesn't by accident quit the kernel
         self._kernel.run_snippet("del quit, exit")
 
+        # If there is a startup script, run it now
+        try:
+            startup = os.environ["PYTHONSTARTUP"]
+            self._console_panel.append(f"Loading Python startup file from {startup}.")
+            self._kernel.run_snippet(
+                textwrap.dedent("""\
+                    import os
+                    import runpy
+                    
+                    try:
+                        startup = os.environ["PYTHONSTARTUP"]
+                        runpy.run_path(path_name=startup)
+                    except KeyError:
+                        raise Warning("Couldn't load startup script, PYTHONSTARTUP not defined.")
+                    """
+                )
+            )
+        except KeyError:
+            self._console_panel.append("Couldn't load startup script, PYTHONSTARTUP not defined.")
+
         if self.cmd_log:
             self._console_panel.append(
                 f"Loading [blue]gui_executor.transforms[/] extension...log file in '{self.cmd_log}'")
             self._kernel.run_snippet(
                 textwrap.dedent(
                     f"""\
                     from gui_executor import transforms
```

### Comparing `gui-executor-0.9.8/src/gui_executor.egg-info/PKG-INFO` & `gui-executor-0.9.9/src/gui_executor.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gui-executor
-Version: 0.9.8
+Version: 0.9.9
 Summary: Execute Python code in an automatically generated GUI App.
 Home-page: https://github.com/rhuygen/gui-executor
 Author: Rik Huygen
 Author-email: rik.huygen@kuleuven.be
 License: MIT
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `gui-executor-0.9.8/src/gui_executor.egg-info/SOURCES.txt` & `gui-executor-0.9.9/src/gui_executor.egg-info/SOURCES.txt`

 * *Files identical despite different names*

