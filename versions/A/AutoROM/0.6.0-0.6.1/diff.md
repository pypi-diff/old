# Comparing `tmp/AutoROM-0.6.0.tar.gz` & `tmp/AutoROM-0.6.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "AutoROM-0.6.0.tar", last modified: Mon Mar 20 12:35:46 2023, max compression
+gzip compressed data, was "AutoROM-0.6.1.tar", last modified: Thu Apr  6 15:28:40 2023, max compression
```

## Comparing `AutoROM-0.6.0.tar` & `AutoROM-0.6.1.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:46.990408 AutoROM-0.6.0/
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:46.990408 AutoROM-0.6.0/AutoROM.egg-info/
--rw-rw-r--   0 jet       (1000) jet       (1000)     2216 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/PKG-INFO
--rw-rw-r--   0 jet       (1000) jet       (1000)      349 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/SOURCES.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/dependency_links.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)       85 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/entry_points.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/not-zip-safe
--rw-rw-r--   0 jet       (1000) jet       (1000)      122 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/requires.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)        8 2023-03-20 12:35:46.000000 AutoROM-0.6.0/AutoROM.egg-info/top_level.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)     1074 2022-12-13 15:13:49.000000 AutoROM-0.6.0/LICENSE.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)       18 2022-12-13 15:13:49.000000 AutoROM-0.6.0/MANIFEST.in
--rw-rw-r--   0 jet       (1000) jet       (1000)     2216 2023-03-20 12:35:46.990408 AutoROM-0.6.0/PKG-INFO
--rw-rw-r--   0 jet       (1000) jet       (1000)     1504 2023-03-17 17:03:14.000000 AutoROM-0.6.0/README.md
--rw-rw-r--   0 jet       (1000) jet       (1000)       74 2023-02-27 17:00:22.000000 AutoROM-0.6.0/pyproject.toml
--rw-rw-r--   0 jet       (1000) jet       (1000)      891 2023-03-20 12:35:46.990408 AutoROM-0.6.0/setup.cfg
--rw-rw-r--   0 jet       (1000) jet       (1000)      423 2022-12-13 15:13:49.000000 AutoROM-0.6.0/setup.py
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:46.990408 AutoROM-0.6.0/src/
--rw-rw-r--   0 jet       (1000) jet       (1000)    12853 2023-03-17 17:04:23.000000 AutoROM-0.6.0/src/AutoROM.py
--rw-rw-r--   0 jet       (1000) jet       (1000)       31 2022-12-13 15:13:49.000000 AutoROM-0.6.0/src/__init__.py
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:46.990408 AutoROM-0.6.0/src/roms/
--rw-rw-r--   0 jet       (1000) jet       (1000)      362 2022-12-13 15:13:49.000000 AutoROM-0.6.0/src/roms/__init__.py
--rw-rw-r--   0 jet       (1000) jet       (1000)        6 2023-03-17 17:22:13.000000 AutoROM-0.6.0/version.txt
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:40.286857 AutoROM-0.6.1/
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:40.286857 AutoROM-0.6.1/AutoROM.egg-info/
+-rw-rw-r--   0 jet       (1000) jet       (1000)     2216 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/PKG-INFO
+-rw-rw-r--   0 jet       (1000) jet       (1000)      349 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/SOURCES.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/dependency_links.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)       85 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/entry_points.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/not-zip-safe
+-rw-rw-r--   0 jet       (1000) jet       (1000)      111 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/requires.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)        8 2023-04-06 15:28:40.000000 AutoROM-0.6.1/AutoROM.egg-info/top_level.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)     1074 2022-12-13 15:13:49.000000 AutoROM-0.6.1/LICENSE.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)       18 2022-12-13 15:13:49.000000 AutoROM-0.6.1/MANIFEST.in
+-rw-rw-r--   0 jet       (1000) jet       (1000)     2216 2023-04-06 15:28:40.286857 AutoROM-0.6.1/PKG-INFO
+-rw-rw-r--   0 jet       (1000) jet       (1000)     1504 2023-03-17 17:03:14.000000 AutoROM-0.6.1/README.md
+-rw-rw-r--   0 jet       (1000) jet       (1000)       74 2023-02-27 17:00:22.000000 AutoROM-0.6.1/pyproject.toml
+-rw-rw-r--   0 jet       (1000) jet       (1000)      879 2023-04-06 15:28:40.286857 AutoROM-0.6.1/setup.cfg
+-rw-rw-r--   0 jet       (1000) jet       (1000)      423 2022-12-13 15:13:49.000000 AutoROM-0.6.1/setup.py
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:40.286857 AutoROM-0.6.1/src/
+-rw-rw-r--   0 jet       (1000) jet       (1000)    12853 2023-03-17 17:04:23.000000 AutoROM-0.6.1/src/AutoROM.py
+-rw-rw-r--   0 jet       (1000) jet       (1000)       31 2022-12-13 15:13:49.000000 AutoROM-0.6.1/src/__init__.py
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:40.286857 AutoROM-0.6.1/src/roms/
+-rw-rw-r--   0 jet       (1000) jet       (1000)      362 2022-12-13 15:13:49.000000 AutoROM-0.6.1/src/roms/__init__.py
+-rw-rw-r--   0 jet       (1000) jet       (1000)        6 2023-04-06 15:22:54.000000 AutoROM-0.6.1/version.txt
```

### Comparing `AutoROM-0.6.0/AutoROM.egg-info/PKG-INFO` & `AutoROM-0.6.1/AutoROM.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: AutoROM
-Version: 0.6.0
+Version: 0.6.1
 Summary: Automated installation of Atari ROMs for Gym/ALE-Py
 Home-page: https://github.com/Farama-Foundation/AutoROM
 Author: Farama Foundation
 Author-email: contact@farama.org
 License: MIT
 Keywords: Reinforcement Learning,game,RL,AI,gym
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `AutoROM-0.6.0/LICENSE.txt` & `AutoROM-0.6.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `AutoROM-0.6.0/PKG-INFO` & `AutoROM-0.6.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: AutoROM
-Version: 0.6.0
+Version: 0.6.1
 Summary: Automated installation of Atari ROMs for Gym/ALE-Py
 Home-page: https://github.com/Farama-Foundation/AutoROM
 Author: Farama Foundation
 Author-email: contact@farama.org
 License: MIT
 Keywords: Reinforcement Learning,game,RL,AI,gym
 Classifier: Programming Language :: Python :: 3.7
```

### Comparing `AutoROM-0.6.0/README.md` & `AutoROM-0.6.1/README.md`

 * *Files identical despite different names*

### Comparing `AutoROM-0.6.0/setup.cfg` & `AutoROM-0.6.1/setup.cfg`

 * *Files 12% similar despite different names*

```diff
@@ -24,15 +24,14 @@
 
 [options]
 python_requires = >=3.7
 zip_safe = False
 install_requires = 
 	click
 	requests
-	libtorrent
 	importlib-resources; python_version < '3.9'
 
 [options.extras_require]
 tests = 
 	ale_py
 	multi_agent_ale_py
```

### Comparing `AutoROM-0.6.0/src/AutoROM.py` & `AutoROM-0.6.1/src/AutoROM.py`

 * *Files identical despite different names*

