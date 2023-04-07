# Comparing `tmp/genesys-0.1.6.tar.gz` & `tmp/genesys-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "genesys-0.1.6.tar", last modified: Sat Feb 11 11:34:23 2023, max compression
+gzip compressed data, was "genesys-0.1.7.tar", last modified: Fri Apr  7 14:26:02 2023, max compression
```

## Comparing `genesys-0.1.6.tar` & `genesys-0.1.7.tar`

### file list

```diff
@@ -1,51 +1,54 @@
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/
--rw-r--r--   0 asuna     (1000) asuna     (1000)     1320 2023-02-11 11:34:23.757258 genesys-0.1.6/PKG-INFO
--rw-r--r--   0 asuna     (1000) asuna     (1000)      487 2021-06-09 17:02:43.000000 genesys-0.1.6/README.rst
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.747258 genesys-0.1.6/genesys/
--rw-r--r--   0 asuna     (1000) asuna     (1000)       21 2023-02-11 11:32:07.000000 genesys-0.1.6/genesys/__init__.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/
--rw-r--r--   0 asuna     (1000) asuna     (1000)      531 2022-10-17 08:29:38.000000 genesys-0.1.6/genesys/app/__init__.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/blueprints/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.6/genesys/app/blueprints/__init__.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/blueprints/asset/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.6/genesys/app/blueprints/asset/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)     2495 2021-07-29 15:11:38.000000 genesys-0.1.6/genesys/app/blueprints/asset/routes.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      962 2021-07-29 14:22:03.000000 genesys-0.1.6/genesys/app/blueprints/asset/utils.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/blueprints/index/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-04-06 14:13:16.000000 genesys-0.1.6/genesys/app/blueprints/index/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      288 2021-04-13 14:23:33.000000 genesys-0.1.6/genesys/app/blueprints/index/routes.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/blueprints/project/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.6/genesys/app/blueprints/project/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)     3972 2021-07-29 14:58:49.000000 genesys-0.1.6/genesys/app/blueprints/project/routes.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      322 2022-02-27 00:51:39.000000 genesys-0.1.6/genesys/app/blueprints/project/utils.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/blueprints/refresh/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2022-10-17 08:25:31.000000 genesys-0.1.6/genesys/app/blueprints/refresh/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)     5165 2023-02-11 11:23:26.000000 genesys-0.1.6/genesys/app/blueprints/refresh/routes.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2022-10-17 09:21:11.000000 genesys-0.1.6/genesys/app/blueprints/refresh/utils.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/blueprints/task/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.6/genesys/app/blueprints/task/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)     6467 2023-02-11 11:31:38.000000 genesys-0.1.6/genesys/app/blueprints/task/routes.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)     4187 2023-02-03 11:39:47.000000 genesys-0.1.6/genesys/app/blueprints/task/utils.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      590 2021-07-29 15:02:48.000000 genesys-0.1.6/genesys/app/config.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/services/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-04-03 13:58:56.000000 genesys-0.1.6/genesys/app/services/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      871 2021-04-13 14:56:40.000000 genesys-0.1.6/genesys/app/services/files_service.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      602 2021-06-08 12:58:11.000000 genesys-0.1.6/genesys/app/services/queue_store.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)     4134 2023-01-09 13:21:59.000000 genesys-0.1.6/genesys/app/services/svn_service.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/template_files/
--rw-r--r--   0 asuna     (1000) asuna     (1000)   729172 2023-02-10 16:17:27.000000 genesys-0.1.6/genesys/app/template_files/blender.blend
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys/app/utils/
--rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.6/genesys/app/utils/__init__.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      511 2021-07-29 15:02:11.000000 genesys-0.1.6/genesys/app/utils/config_helpers.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)       79 2021-03-31 17:04:54.000000 genesys-0.1.6/genesys/debug.py
--rw-r--r--   0 asuna     (1000) asuna     (1000)      154 2021-06-08 12:22:09.000000 genesys-0.1.6/genesys/job_settings.py
-drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-02-11 11:34:23.757258 genesys-0.1.6/genesys.egg-info/
--rw-r--r--   0 asuna     (1000) asuna     (1000)     1320 2023-02-11 11:34:23.000000 genesys-0.1.6/genesys.egg-info/PKG-INFO
--rw-r--r--   0 asuna     (1000) asuna     (1000)     1181 2023-02-11 11:34:23.000000 genesys-0.1.6/genesys.egg-info/SOURCES.txt
--rw-r--r--   0 asuna     (1000) asuna     (1000)        1 2023-02-11 11:34:23.000000 genesys-0.1.6/genesys.egg-info/dependency_links.txt
--rw-r--r--   0 asuna     (1000) asuna     (1000)        1 2021-03-31 19:07:15.000000 genesys-0.1.6/genesys.egg-info/not-zip-safe
--rw-r--r--   0 asuna     (1000) asuna     (1000)      230 2023-02-11 11:34:23.000000 genesys-0.1.6/genesys.egg-info/requires.txt
--rw-r--r--   0 asuna     (1000) asuna     (1000)        8 2023-02-11 11:34:23.000000 genesys-0.1.6/genesys.egg-info/top_level.txt
--rw-r--r--   0 asuna     (1000) asuna     (1000)      100 2021-04-24 09:58:42.000000 genesys-0.1.6/pyproject.toml
--rw-r--r--   0 asuna     (1000) asuna     (1000)     1111 2023-02-11 11:34:23.757258 genesys-0.1.6/setup.cfg
--rw-r--r--   0 asuna     (1000) asuna     (1000)       36 2021-03-31 17:04:54.000000 genesys-0.1.6/setup.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.539669 genesys-0.1.7/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     1320 2023-04-07 14:26:02.539669 genesys-0.1.7/PKG-INFO
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      487 2021-06-09 17:02:43.000000 genesys-0.1.7/README.rst
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)       21 2023-04-07 14:24:27.000000 genesys-0.1.7/genesys/__init__.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      531 2022-10-17 08:29:38.000000 genesys-0.1.7/genesys/app/__init__.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/blueprints/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.7/genesys/app/blueprints/__init__.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/blueprints/asset/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.7/genesys/app/blueprints/asset/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     2495 2021-07-29 15:11:38.000000 genesys-0.1.7/genesys/app/blueprints/asset/routes.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      962 2021-07-29 14:22:03.000000 genesys-0.1.7/genesys/app/blueprints/asset/utils.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/blueprints/index/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-04-06 14:13:16.000000 genesys-0.1.7/genesys/app/blueprints/index/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      288 2021-04-13 14:23:33.000000 genesys-0.1.7/genesys/app/blueprints/index/routes.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/blueprints/project/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.7/genesys/app/blueprints/project/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     3972 2021-07-29 14:58:49.000000 genesys-0.1.7/genesys/app/blueprints/project/routes.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      322 2022-02-27 00:51:39.000000 genesys-0.1.7/genesys/app/blueprints/project/utils.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/blueprints/refresh/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2022-10-17 08:25:31.000000 genesys-0.1.7/genesys/app/blueprints/refresh/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     5165 2023-02-11 11:23:26.000000 genesys-0.1.7/genesys/app/blueprints/refresh/routes.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2022-10-17 09:21:11.000000 genesys-0.1.7/genesys/app/blueprints/refresh/utils.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/blueprints/task/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.7/genesys/app/blueprints/task/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     6467 2023-02-11 11:31:38.000000 genesys-0.1.7/genesys/app/blueprints/task/routes.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     4804 2023-04-07 10:58:00.000000 genesys-0.1.7/genesys/app/blueprints/task/utils.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      590 2021-07-29 15:02:48.000000 genesys-0.1.7/genesys/app/config.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys/app/services/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-04-03 13:58:56.000000 genesys-0.1.7/genesys/app/services/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      871 2021-04-13 14:56:40.000000 genesys-0.1.7/genesys/app/services/files_service.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      602 2021-06-08 12:58:11.000000 genesys-0.1.7/genesys/app/services/queue_store.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     4134 2023-01-09 13:21:59.000000 genesys-0.1.7/genesys/app/services/svn_service.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.539669 genesys-0.1.7/genesys/app/template_files/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)   852452 2023-04-07 14:24:52.000000 genesys-0.1.7/genesys/app/template_files/blender.blend
+-rw-r--r--   0 asuna     (1000) asuna     (1000)   287918 2023-04-07 09:48:42.000000 genesys-0.1.7/genesys/app/template_files/clipstudio.clip
+-rw-r--r--   0 asuna     (1000) asuna     (1000)   117656 2023-04-07 09:45:36.000000 genesys-0.1.7/genesys/app/template_files/flstudio.flp
+-rw-r--r--   0 asuna     (1000) asuna     (1000)    12276 2023-04-07 09:51:58.000000 genesys-0.1.7/genesys/app/template_files/sketchbook.tif
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.539669 genesys-0.1.7/genesys/app/utils/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        0 2021-03-31 17:04:54.000000 genesys-0.1.7/genesys/app/utils/__init__.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      511 2021-07-29 15:02:11.000000 genesys-0.1.7/genesys/app/utils/config_helpers.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)       79 2021-03-31 17:04:54.000000 genesys-0.1.7/genesys/debug.py
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      154 2021-06-08 12:22:09.000000 genesys-0.1.7/genesys/job_settings.py
+drwxr-xr-x   0 asuna     (1000) asuna     (1000)        0 2023-04-07 14:26:02.529669 genesys-0.1.7/genesys.egg-info/
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     1320 2023-04-07 14:26:02.000000 genesys-0.1.7/genesys.egg-info/PKG-INFO
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     1306 2023-04-07 14:26:02.000000 genesys-0.1.7/genesys.egg-info/SOURCES.txt
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        1 2023-04-07 14:26:02.000000 genesys-0.1.7/genesys.egg-info/dependency_links.txt
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        1 2021-03-31 19:07:15.000000 genesys-0.1.7/genesys.egg-info/not-zip-safe
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      230 2023-04-07 14:26:02.000000 genesys-0.1.7/genesys.egg-info/requires.txt
+-rw-r--r--   0 asuna     (1000) asuna     (1000)        8 2023-04-07 14:26:02.000000 genesys-0.1.7/genesys.egg-info/top_level.txt
+-rw-r--r--   0 asuna     (1000) asuna     (1000)      100 2021-04-24 09:58:42.000000 genesys-0.1.7/pyproject.toml
+-rw-r--r--   0 asuna     (1000) asuna     (1000)     1111 2023-04-07 14:26:02.539669 genesys-0.1.7/setup.cfg
+-rw-r--r--   0 asuna     (1000) asuna     (1000)       36 2021-03-31 17:04:54.000000 genesys-0.1.7/setup.py
```

### Comparing `genesys-0.1.6/PKG-INFO` & `genesys-0.1.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: genesys
-Version: 0.1.6
+Version: 0.1.7
 Summary: generates files and dependences for cgi projects
 Home-page: https://eaxum.com
 Author: Aderemi Adesada
 Author-email: adesadaaderemi@gmail.com
 License: UNKNOWN
 Description: genesys is a file management and version control software that is directly intigrated with kitsu.
```

### Comparing `genesys-0.1.6/genesys/app/__init__.py` & `genesys-0.1.7/genesys/app/__init__.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/blueprints/asset/routes.py` & `genesys-0.1.7/genesys/app/blueprints/asset/routes.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/blueprints/asset/utils.py` & `genesys-0.1.7/genesys/app/blueprints/asset/utils.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/blueprints/project/routes.py` & `genesys-0.1.7/genesys/app/blueprints/project/routes.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/blueprints/refresh/routes.py` & `genesys-0.1.7/genesys/app/blueprints/refresh/routes.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/blueprints/task/routes.py` & `genesys-0.1.7/genesys/app/blueprints/task/routes.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/blueprints/task/utils.py` & `genesys-0.1.7/genesys/app/blueprints/task/utils.py`

 * *Files 23% similar despite different names*

```diff
@@ -8,19 +8,31 @@
                                 LOGIN_NAME)
 import bpy
 
 def create_task_file(task, project_name, base_file_directory, base_svn_directory, main_file_name):
     "creates file tasks"
     acl_parser = ConfigParser()
     svn_authz_path = os.path.join(SVN_PARENT_PATH, project_name.replace(' ', '_').lower(), 'conf/authz')
-    blend_file_url = os.path.join(SVN_PARENT_URL, base_file_directory)
+    file_url = os.path.join(SVN_PARENT_URL, base_file_directory)
+    file_extension = os.path.basename(base_file_directory).rsplit('.', 1)[1]
+    if file_extension == 'blend':
+        template_file = os.path.join(TEMPLATE_FILES_DIR,'blender.blend')
+    elif file_extension == 'clip':
+        template_file = os.path.join(TEMPLATE_FILES_DIR,'clipstudio.clip')
+    elif file_extension == 'flp':
+        template_file = os.path.join(TEMPLATE_FILES_DIR,'flstudio.flp')
+    elif file_extension == 'tif':
+        template_file = os.path.join(TEMPLATE_FILES_DIR,'sketchbook.tif')
+    else:
+        template_file = os.path.join(TEMPLATE_FILES_DIR,'blender.blend')
+
 
     config_helpers.load_config(svn_authz_path, acl_parser)
 
-    file_folder_url = os.path.dirname(blend_file_url)
+    file_folder_url = os.path.dirname(file_url)
     file_name = os.path.basename(base_file_directory).rsplit('.', 1)[0]
 
     for_entity = task["task_type"]["for_entity"]
     if for_entity.lower() == "asset":
         collection_name = main_file_name
         file_map_folder_url = os.path.join(file_folder_url, 'maps', main_file_name)
         base_map_svn_directory = os.path.join(os.path.dirname(base_svn_directory), 'maps', main_file_name)
@@ -30,44 +42,45 @@
         base_map_svn_directory = os.path.join(os.path.dirname(base_svn_directory), 'maps', file_name)
     
 
     if not svn_service.is_svn_url(file_folder_url):
         svn_service.svn_make_dirs(file_folder_url, log_message=f'created {file_folder_url}')
     if not svn_service.is_svn_url(file_map_folder_url):
         svn_service.svn_make_dirs(file_map_folder_url, log_message=f'created {file_map_folder_url}')
-    if not svn_service.is_svn_url(blend_file_url):
+    if not svn_service.is_svn_url(file_url):
         task_type = task['task_type']['name']
         task_id = task['id']
         entity_id = task['entity_id']
         nagato_file_data = {
             'task_type':task_type,
             'task_id':task_id, 
             'entity_id':entity_id,
             'collection_name': collection_name,
             'scene_name': collection_name,
             'main_file_name': main_file_name,
         }
-        bpy.ops.wm.read_homefile()
-        default_collection = bpy.data.collections.get('Collection')
-        for obj in default_collection.objects:
-            bpy.data.objects.remove(obj, do_unlink=True)  
-        bpy.data.collections.remove(default_collection)
-        main_collection = bpy.data.collections.new(collection_name)
-        bpy.context.scene.collection.children.link(main_collection)
-
-        # assets = bpy.data.collections.new("assets")
-        # main_collection.children.link(assets)
-
-        bpy.data.scenes['Scene'].name = collection_name
-        scene = bpy.data.scenes.get(collection_name)
-        scene['nagato_file_data'] = nagato_file_data
-        bpy.ops.wm.save_as_mainfile(filepath=os.path.join(TEMPLATE_FILES_DIR,'blender.blend'))
-        svn_service.svn_import(path=os.path.join(TEMPLATE_FILES_DIR,'blender.blend'),
-                                    repo_url=blend_file_url,
-                                    log_message=f'created {blend_file_url}')
+        if file_extension == 'blend':
+            bpy.ops.wm.read_homefile()
+            default_collection = bpy.data.collections.get('Collection')
+            for obj in default_collection.objects:
+                bpy.data.objects.remove(obj, do_unlink=True)  
+            bpy.data.collections.remove(default_collection)
+            main_collection = bpy.data.collections.new(collection_name)
+            bpy.context.scene.collection.children.link(main_collection)
+
+            # assets = bpy.data.collections.new("assets")
+            # main_collection.children.link(assets)
+
+            bpy.data.scenes['Scene'].name = collection_name
+            scene = bpy.data.scenes.get(collection_name)
+            scene['nagato_file_data'] = nagato_file_data
+            bpy.ops.wm.save_as_mainfile(filepath=os.path.join(TEMPLATE_FILES_DIR,'blender.blend'))
+        svn_service.svn_import(path=template_file,
+                                    repo_url=file_url,
+                                    log_message=f'created {file_url}')
                                    
     create_new_task_acl(base_svn_directory=base_svn_directory, base_map_svn_directory=base_map_svn_directory, acl_parser=acl_parser)
     config_helpers.write_config(svn_authz_path, acl_parser)
 
 def create_new_task_acl(base_svn_directory:str, base_map_svn_directory:str, acl_parser):
     "create svn access entry for task file and set all users to no acces"
     if base_svn_directory in acl_parser:
```

### Comparing `genesys-0.1.6/genesys/app/config.py` & `genesys-0.1.7/genesys/app/config.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/services/files_service.py` & `genesys-0.1.7/genesys/app/services/files_service.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/services/queue_store.py` & `genesys-0.1.7/genesys/app/services/queue_store.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys/app/services/svn_service.py` & `genesys-0.1.7/genesys/app/services/svn_service.py`

 * *Files identical despite different names*

### Comparing `genesys-0.1.6/genesys.egg-info/PKG-INFO` & `genesys-0.1.7/genesys.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: genesys
-Version: 0.1.6
+Version: 0.1.7
 Summary: generates files and dependences for cgi projects
 Home-page: https://eaxum.com
 Author: Aderemi Adesada
 Author-email: adesadaaderemi@gmail.com
 License: UNKNOWN
 Description: genesys is a file management and version control software that is directly intigrated with kitsu.
```

### Comparing `genesys-0.1.6/genesys.egg-info/SOURCES.txt` & `genesys-0.1.7/genesys.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -29,9 +29,12 @@
 genesys/app/blueprints/task/routes.py
 genesys/app/blueprints/task/utils.py
 genesys/app/services/__init__.py
 genesys/app/services/files_service.py
 genesys/app/services/queue_store.py
 genesys/app/services/svn_service.py
 genesys/app/template_files/blender.blend
+genesys/app/template_files/clipstudio.clip
+genesys/app/template_files/flstudio.flp
+genesys/app/template_files/sketchbook.tif
 genesys/app/utils/__init__.py
 genesys/app/utils/config_helpers.py
```

### Comparing `genesys-0.1.6/setup.cfg` & `genesys-0.1.7/setup.cfg`

 * *Files identical despite different names*

