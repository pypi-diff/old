# Comparing `tmp/PLAN-Tools-0.4.tar.gz` & `tmp/PLAN-Tools-0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PLAN-Tools-0.4.tar", last modified: Thu Apr  6 15:34:06 2023, max compression
+gzip compressed data, was "PLAN-Tools-0.5.tar", last modified: Thu Apr  6 18:08:05 2023, max compression
```

## Comparing `PLAN-Tools-0.4.tar` & `PLAN-Tools-0.5.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:34:06.562231 PLAN-Tools-0.4/
--rw-r--r--   0 runner    (1001) docker     (122)     8806 2023-04-06 15:34:06.562231 PLAN-Tools-0.4/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:34:06.562231 PLAN-Tools-0.4/PLAN_Tools.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     8806 2023-04-06 15:34:06.000000 PLAN-Tools-0.4/PLAN_Tools.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      371 2023-04-06 15:34:06.000000 PLAN-Tools-0.4/PLAN_Tools.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 15:34:06.000000 PLAN-Tools-0.4/PLAN_Tools.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       53 2023-04-06 15:34:06.000000 PLAN-Tools-0.4/PLAN_Tools.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (122)       11 2023-04-06 15:34:06.000000 PLAN-Tools-0.4/PLAN_Tools.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)     7637 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:34:06.562231 PLAN-Tools-0.4/plan_tools/
--rw-r--r--   0 runner    (1001) docker     (122)       34 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/plan_tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    12715 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/plan_tools/entry_point.py
--rw-r--r--   0 runner    (1001) docker     (122)     1761 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/plan_tools/runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 15:34:06.562231 PLAN-Tools-0.4/plan_tools/tests/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/plan_tools/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     1487 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/plan_tools/tests/test_entry_point.py
--rw-r--r--   0 runner    (1001) docker     (122)      415 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/plan_tools/tests/test_runtime.py
--rw-r--r--   0 runner    (1001) docker     (122)      170 2023-04-06 15:34:06.562231 PLAN-Tools-0.4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1134 2023-04-06 15:33:54.000000 PLAN-Tools-0.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:08:05.370363 PLAN-Tools-0.5/
+-rw-r--r--   0 runner    (1001) docker     (122)     8806 2023-04-06 18:08:05.370363 PLAN-Tools-0.5/PKG-INFO
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:08:05.370363 PLAN-Tools-0.5/PLAN_Tools.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     8806 2023-04-06 18:08:05.000000 PLAN-Tools-0.5/PLAN_Tools.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      371 2023-04-06 18:08:05.000000 PLAN-Tools-0.5/PLAN_Tools.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 18:08:05.000000 PLAN-Tools-0.5/PLAN_Tools.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       53 2023-04-06 18:08:05.000000 PLAN-Tools-0.5/PLAN_Tools.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       11 2023-04-06 18:08:05.000000 PLAN-Tools-0.5/PLAN_Tools.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     7637 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:08:05.370363 PLAN-Tools-0.5/plan_tools/
+-rw-r--r--   0 runner    (1001) docker     (122)       34 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/plan_tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12720 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/plan_tools/entry_point.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1761 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/plan_tools/runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:08:05.370363 PLAN-Tools-0.5/plan_tools/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/plan_tools/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1487 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/plan_tools/tests/test_entry_point.py
+-rw-r--r--   0 runner    (1001) docker     (122)      415 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/plan_tools/tests/test_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (122)      170 2023-04-06 18:08:05.374363 PLAN-Tools-0.5/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1134 2023-04-06 18:07:53.000000 PLAN-Tools-0.5/setup.py
```

### Comparing `PLAN-Tools-0.4/PKG-INFO` & `PLAN-Tools-0.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PLAN-Tools
-Version: 0.4
+Version: 0.5
 Summary: A set of tools to help with Pip Links And Nonsense
 Home-page: https://github.com/Myoldmopar/PlanTools
 Author: Edwin Lee
 Author-email: 
 License: UNKNOWN
 Description: # PLAN-TOOLS
```

### Comparing `PLAN-Tools-0.4/PLAN_Tools.egg-info/PKG-INFO` & `PLAN-Tools-0.5/PLAN_Tools.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: PLAN-Tools
-Version: 0.4
+Version: 0.5
 Summary: A set of tools to help with Pip Links And Nonsense
 Home-page: https://github.com/Myoldmopar/PlanTools
 Author: Edwin Lee
 Author-email: 
 License: UNKNOWN
 Description: # PLAN-TOOLS
```

### Comparing `PLAN-Tools-0.4/README.md` & `PLAN-Tools-0.5/README.md`

 * *Files identical despite different names*

### Comparing `PLAN-Tools-0.4/plan_tools/entry_point.py` & `PLAN-Tools-0.5/plan_tools/entry_point.py`

 * *Files 0% similar despite different names*

```diff
@@ -89,15 +89,15 @@
                 # maybe someday we could actually test this in CI
                 # noinspection PyUnresolvedReferences
                 from win32com.client import Dispatch
                 shell = Dispatch('WScript.Shell')
                 s = shell.CreateShortCut(str(desktop_file))
                 s.Targetpath = str(target_exe)
                 s.WorkingDirectory = str(scripts_dir)
-                s.IconLocation = icon_file_string
+                s.IconLocation = str(icon_file_string)
                 s.save()
         elif system() == 'Linux':
             desktop_file_contents = f"""[Desktop Entry]
 Name={self.pretty_link_name}
 Comment={self.description}
 Exec={target_exe}
 Icon={icon_file_string}
```

### Comparing `PLAN-Tools-0.4/plan_tools/runtime.py` & `PLAN-Tools-0.5/plan_tools/runtime.py`

 * *Files identical despite different names*

### Comparing `PLAN-Tools-0.4/plan_tools/tests/test_entry_point.py` & `PLAN-Tools-0.5/plan_tools/tests/test_entry_point.py`

 * *Files identical despite different names*

### Comparing `PLAN-Tools-0.4/setup.py` & `PLAN-Tools-0.5/setup.py`

 * *Files identical despite different names*

