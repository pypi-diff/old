# Comparing `tmp/bs_admin_utils-1.0.0.tar.gz` & `tmp/bs_admin_utils-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bs_admin_utils-1.0.0.tar", last modified: Fri Apr  7 04:21:44 2023, max compression
+gzip compressed data, was "bs_admin_utils-1.0.1.tar", last modified: Fri Apr  7 04:37:17 2023, max compression
```

## Comparing `bs_admin_utils-1.0.0.tar` & `bs_admin_utils-1.0.1.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:21:44.559937 bs_admin_utils-1.0.0/
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     1067 2023-04-07 03:25:03.000000 bs_admin_utils-1.0.0/LICENSE
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       35 2023-04-07 04:04:08.000000 bs_admin_utils-1.0.0/MANIFEST.in
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      260 2023-04-07 04:21:44.559937 bs_admin_utils-1.0.0/PKG-INFO
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      206 2023-04-07 03:35:29.000000 bs_admin_utils-1.0.0/README.md
-drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:21:44.559937 bs_admin_utils-1.0.0/bs_admin_utils/
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       13 2023-04-07 03:39:05.000000 bs_admin_utils-1.0.0/bs_admin_utils/__init__.py
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     3943 2023-04-07 03:49:11.000000 bs_admin_utils-1.0.0/bs_admin_utils/api.py
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      490 2023-04-07 04:11:32.000000 bs_admin_utils-1.0.0/bs_admin_utils/decorators.py
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     1034 2023-04-07 03:48:50.000000 bs_admin_utils-1.0.0/bs_admin_utils/model.py
-drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:21:44.559937 bs_admin_utils-1.0.0/bs_admin_utils/static/
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)   367112 2023-04-07 03:52:07.000000 bs_admin_utils-1.0.0/bs_admin_utils/static/arial.ttf
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     2331 2023-04-07 04:20:26.000000 bs_admin_utils-1.0.0/bs_admin_utils/vercode.py
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     2868 2023-04-07 04:10:45.000000 bs_admin_utils-1.0.0/bs_admin_utils/websocket.py
-drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:21:44.559937 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      260 2023-04-07 04:21:44.000000 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/PKG-INFO
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      448 2023-04-07 04:21:44.000000 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/SOURCES.txt
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)        1 2023-04-07 04:21:44.000000 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/dependency_links.txt
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       44 2023-04-07 04:21:44.000000 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/requires.txt
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       15 2023-04-07 04:21:44.000000 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/top_level.txt
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)        1 2023-04-07 04:21:44.000000 bs_admin_utils-1.0.0/bs_admin_utils.egg-info/zip-safe
--rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       38 2023-04-07 04:21:44.559937 bs_admin_utils-1.0.0/setup.cfg
--rwxr-xr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)      620 2023-04-07 04:02:00.000000 bs_admin_utils-1.0.0/setup.py
+drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:37:17.584243 bs_admin_utils-1.0.1/
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     1067 2023-04-07 03:25:03.000000 bs_admin_utils-1.0.1/LICENSE
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       35 2023-04-07 04:04:08.000000 bs_admin_utils-1.0.1/MANIFEST.in
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      260 2023-04-07 04:37:17.584243 bs_admin_utils-1.0.1/PKG-INFO
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      206 2023-04-07 03:35:29.000000 bs_admin_utils-1.0.1/README.md
+drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:37:17.584243 bs_admin_utils-1.0.1/bs_admin_utils/
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       13 2023-04-07 03:39:05.000000 bs_admin_utils-1.0.1/bs_admin_utils/__init__.py
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     3943 2023-04-07 03:49:11.000000 bs_admin_utils-1.0.1/bs_admin_utils/api.py
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      490 2023-04-07 04:11:32.000000 bs_admin_utils-1.0.1/bs_admin_utils/decorators.py
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     1034 2023-04-07 03:48:50.000000 bs_admin_utils-1.0.1/bs_admin_utils/model.py
+drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:37:17.584243 bs_admin_utils-1.0.1/bs_admin_utils/static/
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)   367112 2023-04-07 03:52:07.000000 bs_admin_utils-1.0.1/bs_admin_utils/static/arial.ttf
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     2320 2023-04-07 04:36:50.000000 bs_admin_utils-1.0.1/bs_admin_utils/vercode.py
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)     2868 2023-04-07 04:10:45.000000 bs_admin_utils-1.0.1/bs_admin_utils/websocket.py
+drwxrwxr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)        0 2023-04-07 04:37:17.584243 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      260 2023-04-07 04:37:17.000000 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/PKG-INFO
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)      448 2023-04-07 04:37:17.000000 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/SOURCES.txt
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)        1 2023-04-07 04:37:17.000000 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/dependency_links.txt
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       44 2023-04-07 04:37:17.000000 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/requires.txt
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       15 2023-04-07 04:37:17.000000 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/top_level.txt
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)        1 2023-04-07 04:37:17.000000 bs_admin_utils-1.0.1/bs_admin_utils.egg-info/zip-safe
+-rw-rw-r--   0 kiki-kanri  (1000) kiki-kanri  (1000)       38 2023-04-07 04:37:17.584243 bs_admin_utils-1.0.1/setup.cfg
+-rwxr-xr-x   0 kiki-kanri  (1000) kiki-kanri  (1000)      620 2023-04-07 04:36:55.000000 bs_admin_utils-1.0.1/setup.py
```

### Comparing `bs_admin_utils-1.0.0/LICENSE` & `bs_admin_utils-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `bs_admin_utils-1.0.0/bs_admin_utils/api.py` & `bs_admin_utils-1.0.1/bs_admin_utils/api.py`

 * *Files identical despite different names*

### Comparing `bs_admin_utils-1.0.0/bs_admin_utils/model.py` & `bs_admin_utils-1.0.1/bs_admin_utils/model.py`

 * *Files identical despite different names*

### Comparing `bs_admin_utils-1.0.0/bs_admin_utils/static/arial.ttf` & `bs_admin_utils-1.0.1/bs_admin_utils/static/arial.ttf`

 * *Files identical despite different names*

### Comparing `bs_admin_utils-1.0.0/bs_admin_utils/vercode.py` & `bs_admin_utils-1.0.1/bs_admin_utils/vercode.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,15 +15,15 @@
     bg_color = (0, 0, 0, 0)
     font_size = 32
     image_height = 50
     image_width = 150
     image_size = (image_width, image_height)
     vercode_length = 4
 
-    font = ImageFont.truetype('./static/arial.ttf', size=font_size)
+    font = ImageFont.truetype(font_path, size=font_size)
     font_base_x = (image_width - font_size * 4) / 2
     font_base_y = (image_height - font_size) / 2
     font_pos = []
 
     for i in range(vercode_length):
         font_pos.append((font_base_x + font_size * i, font_base_y))
```

### Comparing `bs_admin_utils-1.0.0/bs_admin_utils/websocket.py` & `bs_admin_utils-1.0.1/bs_admin_utils/websocket.py`

 * *Files identical despite different names*

### Comparing `bs_admin_utils-1.0.0/setup.py` & `bs_admin_utils-1.0.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
     ],
     packages=find_packages(),
     package_data={
         'bs_admin_utils': ['*.ttf']
     },
     include_package_data=True,
     zip_safe=True,
-    version='1.0.0',
+    version='1.0.1',
     description='Blacksheep admin backend utils classes and function.',
     author='kiki-kanri',
     author_email='a470666@gmail.com',
     keywords=[],
     install_requires=[
         'beanie',
         'blacksheep',
```

