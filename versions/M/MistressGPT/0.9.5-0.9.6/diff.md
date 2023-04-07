# Comparing `tmp/MistressGPT-0.9.5.tar.gz` & `tmp/MistressGPT-0.9.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "MistressGPT-0.9.5.tar", last modified: Thu Apr  6 02:41:07 2023, max compression
+gzip compressed data, was "MistressGPT-0.9.6.tar", last modified: Fri Apr  7 00:40:45 2023, max compression
```

## Comparing `MistressGPT-0.9.5.tar` & `MistressGPT-0.9.6.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-06 02:41:07.993934 MistressGPT-0.9.5/
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-06 02:41:07.990446 MistressGPT-0.9.5/MistressGPT.egg-info/
--rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-06 02:41:07.000000 MistressGPT-0.9.5/MistressGPT.egg-info/PKG-INFO
--rw-r--r--   0 huzi       (501) staff       (20)      648 2023-04-06 02:41:07.000000 MistressGPT-0.9.5/MistressGPT.egg-info/SOURCES.txt
--rw-r--r--   0 huzi       (501) staff       (20)        1 2023-04-06 02:41:07.000000 MistressGPT-0.9.5/MistressGPT.egg-info/dependency_links.txt
--rw-r--r--   0 huzi       (501) staff       (20)       63 2023-04-06 02:41:07.000000 MistressGPT-0.9.5/MistressGPT.egg-info/entry_points.txt
--rw-r--r--   0 huzi       (501) staff       (20)      102 2023-04-06 02:41:07.000000 MistressGPT-0.9.5/MistressGPT.egg-info/requires.txt
--rw-r--r--   0 huzi       (501) staff       (20)       13 2023-04-06 02:41:07.000000 MistressGPT-0.9.5/MistressGPT.egg-info/top_level.txt
--rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-06 02:41:07.993796 MistressGPT-0.9.5/PKG-INFO
--rw-r--r--   0 huzi       (501) staff       (20)     1261 2023-04-06 00:01:40.000000 MistressGPT-0.9.5/README.md
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-06 02:41:07.991829 MistressGPT-0.9.5/chatmistress/
--rw-r--r--   0 huzi       (501) staff       (20)        0 2023-03-30 05:12:33.000000 MistressGPT-0.9.5/chatmistress/__init__.py
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-06 02:41:07.992955 MistressGPT-0.9.5/chatmistress/assets/
--rw-r--r--   0 huzi       (501) staff       (20)     2956 2023-04-02 06:57:10.000000 MistressGPT-0.9.5/chatmistress/assets/Kelpy-Codos.js
--rw-r--r--   0 huzi       (501) staff       (20)     8644 2023-04-02 06:57:10.000000 MistressGPT-0.9.5/chatmistress/assets/custom.css
--rw-r--r--   0 huzi       (501) staff       (20)       25 2023-04-02 06:57:10.000000 MistressGPT-0.9.5/chatmistress/assets/custom.js
--rw-r--r--   0 huzi       (501) staff       (20)    15406 2023-04-02 06:57:10.000000 MistressGPT-0.9.5/chatmistress/assets/favicon.ico
--rw-r--r--   0 huzi       (501) staff       (20)     4296 2023-04-06 00:11:42.000000 MistressGPT-0.9.5/chatmistress/chatmistress.py
--rw-r--r--   0 huzi       (501) staff       (20)     8871 2023-04-05 23:52:03.000000 MistressGPT-0.9.5/chatmistress/core.py
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-06 02:41:07.993352 MistressGPT-0.9.5/chatmistress/roles/
--rw-r--r--   0 huzi       (501) staff       (20)      758 2023-03-30 00:07:04.000000 MistressGPT-0.9.5/chatmistress/roles/landlady.yml
--rw-r--r--   0 huzi       (501) staff       (20)      964 2023-03-30 04:46:54.000000 MistressGPT-0.9.5/chatmistress/roles/wife.yml
-drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-06 02:41:07.993617 MistressGPT-0.9.5/chatmistress/templates/
--rw-r--r--   0 huzi       (501) staff       (20)     1104 2023-03-30 00:08:37.000000 MistressGPT-0.9.5/chatmistress/templates/role_play_summary.txt
--rw-r--r--   0 huzi       (501) staff       (20)     1113 2023-03-30 00:27:26.000000 MistressGPT-0.9.5/chatmistress/templates/role_play_sys.txt
--rw-r--r--   0 huzi       (501) staff       (20)     1239 2023-04-06 02:40:08.000000 MistressGPT-0.9.5/chatmistress/utils.py
--rw-r--r--   0 huzi       (501) staff       (20)     1876 2023-03-30 05:13:12.000000 MistressGPT-0.9.5/chatmistress/webbot.py
--rw-r--r--   0 huzi       (501) staff       (20)    20647 2023-04-06 00:30:48.000000 MistressGPT-0.9.5/chatmistress/webbot2.py
--rw-r--r--   0 huzi       (501) staff       (20)       38 2023-04-06 02:41:07.993970 MistressGPT-0.9.5/setup.cfg
--rw-r--r--   0 huzi       (501) staff       (20)      819 2023-04-06 02:40:57.000000 MistressGPT-0.9.5/setup.py
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.532644 MistressGPT-0.9.6/
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.528035 MistressGPT-0.9.6/MistressGPT.egg-info/
+-rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/PKG-INFO
+-rw-r--r--   0 huzi       (501) staff       (20)      648 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/SOURCES.txt
+-rw-r--r--   0 huzi       (501) staff       (20)        1 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/dependency_links.txt
+-rw-r--r--   0 huzi       (501) staff       (20)       63 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/entry_points.txt
+-rw-r--r--   0 huzi       (501) staff       (20)      102 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/requires.txt
+-rw-r--r--   0 huzi       (501) staff       (20)       13 2023-04-07 00:40:45.000000 MistressGPT-0.9.6/MistressGPT.egg-info/top_level.txt
+-rw-r--r--   0 huzi       (501) staff       (20)     1410 2023-04-07 00:40:45.532498 MistressGPT-0.9.6/PKG-INFO
+-rw-r--r--   0 huzi       (501) staff       (20)     1261 2023-04-06 00:01:40.000000 MistressGPT-0.9.6/README.md
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.529566 MistressGPT-0.9.6/chatmistress/
+-rw-r--r--   0 huzi       (501) staff       (20)        0 2023-03-30 05:12:33.000000 MistressGPT-0.9.6/chatmistress/__init__.py
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.531156 MistressGPT-0.9.6/chatmistress/assets/
+-rw-r--r--   0 huzi       (501) staff       (20)     2956 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/Kelpy-Codos.js
+-rw-r--r--   0 huzi       (501) staff       (20)     8644 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/custom.css
+-rw-r--r--   0 huzi       (501) staff       (20)       25 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/custom.js
+-rw-r--r--   0 huzi       (501) staff       (20)    15406 2023-04-02 06:57:10.000000 MistressGPT-0.9.6/chatmistress/assets/favicon.ico
+-rw-r--r--   0 huzi       (501) staff       (20)     4296 2023-04-06 00:11:42.000000 MistressGPT-0.9.6/chatmistress/chatmistress.py
+-rw-r--r--   0 huzi       (501) staff       (20)     8871 2023-04-05 23:52:03.000000 MistressGPT-0.9.6/chatmistress/core.py
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.531630 MistressGPT-0.9.6/chatmistress/roles/
+-rw-r--r--   0 huzi       (501) staff       (20)      758 2023-03-30 00:07:04.000000 MistressGPT-0.9.6/chatmistress/roles/landlady.yml
+-rw-r--r--   0 huzi       (501) staff       (20)      964 2023-03-30 04:46:54.000000 MistressGPT-0.9.6/chatmistress/roles/wife.yml
+drwxr-xr-x   0 huzi       (501) staff       (20)        0 2023-04-07 00:40:45.532164 MistressGPT-0.9.6/chatmistress/templates/
+-rw-r--r--   0 huzi       (501) staff       (20)     1104 2023-03-30 00:08:37.000000 MistressGPT-0.9.6/chatmistress/templates/role_play_summary.txt
+-rw-r--r--   0 huzi       (501) staff       (20)     1113 2023-03-30 00:27:26.000000 MistressGPT-0.9.6/chatmistress/templates/role_play_sys.txt
+-rw-r--r--   0 huzi       (501) staff       (20)     1239 2023-04-06 02:40:08.000000 MistressGPT-0.9.6/chatmistress/utils.py
+-rw-r--r--   0 huzi       (501) staff       (20)     1876 2023-03-30 05:13:12.000000 MistressGPT-0.9.6/chatmistress/webbot.py
+-rw-r--r--   0 huzi       (501) staff       (20)    20647 2023-04-06 00:30:48.000000 MistressGPT-0.9.6/chatmistress/webbot2.py
+-rw-r--r--   0 huzi       (501) staff       (20)       38 2023-04-07 00:40:45.532689 MistressGPT-0.9.6/setup.cfg
+-rw-r--r--   0 huzi       (501) staff       (20)      819 2023-04-07 00:40:32.000000 MistressGPT-0.9.6/setup.py
```

### Comparing `MistressGPT-0.9.5/MistressGPT.egg-info/PKG-INFO` & `MistressGPT-0.9.6/MistressGPT.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MistressGPT
-Version: 0.9.5
+Version: 0.9.6
 Summary: MistressGPT: 基于GPT3.5的女王聊天室
 Description-Content-Type: text/markdown
 
 # MistressGPT: 基于 GPT3.5 的女王聊天室
 
 ## 介绍
```

### Comparing `MistressGPT-0.9.5/MistressGPT.egg-info/SOURCES.txt` & `MistressGPT-0.9.6/MistressGPT.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/PKG-INFO` & `MistressGPT-0.9.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: MistressGPT
-Version: 0.9.5
+Version: 0.9.6
 Summary: MistressGPT: 基于GPT3.5的女王聊天室
 Description-Content-Type: text/markdown
 
 # MistressGPT: 基于 GPT3.5 的女王聊天室
 
 ## 介绍
```

### Comparing `MistressGPT-0.9.5/README.md` & `MistressGPT-0.9.6/README.md`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/assets/Kelpy-Codos.js` & `MistressGPT-0.9.6/chatmistress/assets/Kelpy-Codos.js`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/assets/custom.css` & `MistressGPT-0.9.6/chatmistress/assets/custom.css`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/assets/favicon.ico` & `MistressGPT-0.9.6/chatmistress/assets/favicon.ico`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/chatmistress.py` & `MistressGPT-0.9.6/chatmistress/chatmistress.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/core.py` & `MistressGPT-0.9.6/chatmistress/core.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/roles/landlady.yml` & `MistressGPT-0.9.6/chatmistress/roles/landlady.yml`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/roles/wife.yml` & `MistressGPT-0.9.6/chatmistress/roles/wife.yml`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/templates/role_play_summary.txt` & `MistressGPT-0.9.6/chatmistress/templates/role_play_summary.txt`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/templates/role_play_sys.txt` & `MistressGPT-0.9.6/chatmistress/templates/role_play_sys.txt`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/utils.py` & `MistressGPT-0.9.6/chatmistress/utils.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/webbot.py` & `MistressGPT-0.9.6/chatmistress/webbot.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/chatmistress/webbot2.py` & `MistressGPT-0.9.6/chatmistress/webbot2.py`

 * *Files identical despite different names*

### Comparing `MistressGPT-0.9.5/setup.py` & `MistressGPT-0.9.6/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 from setuptools import setup, find_packages
 
-with open("readme.md", "r", encoding="utf-8") as fh:
+with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setup(
     name='MistressGPT',
     description='MistressGPT: 基于GPT3.5的女王聊天室',
     long_description=long_description,
     long_description_content_type='text/markdown',
-    version='0.9.5',
+    version='0.9.6',
     packages=find_packages(),
     entry_points={
         'console_scripts': [
             'mistressgpt=chatmistress.chatmistress:main'
         ]
     },
     package_data={
```

