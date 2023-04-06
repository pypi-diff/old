# Comparing `tmp/AutoROM.accept-rom-license-0.6.0.tar.gz` & `tmp/AutoROM.accept-rom-license-0.6.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "AutoROM.accept-rom-license-0.6.0.tar", last modified: Mon Mar 20 12:35:53 2023, max compression
+gzip compressed data, was "AutoROM.accept-rom-license-0.6.1.tar", last modified: Thu Apr  6 15:28:47 2023, max compression
```

## Comparing `AutoROM.accept-rom-license-0.6.0.tar` & `AutoROM.accept-rom-license-0.6.1.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:53.486372 AutoROM.accept-rom-license-0.6.0/
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:53.486372 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/
--rw-rw-r--   0 jet       (1000) jet       (1000)     2222 2023-03-20 12:35:53.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/PKG-INFO
--rw-rw-r--   0 jet       (1000) jet       (1000)      436 2023-03-20 12:35:53.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/SOURCES.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-03-20 12:35:53.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/dependency_links.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-03-20 12:35:53.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/not-zip-safe
--rw-rw-r--   0 jet       (1000) jet       (1000)      108 2023-03-20 12:35:53.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/requires.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)        8 2023-03-20 12:35:53.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/top_level.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)    12853 2023-03-17 17:04:23.000000 AutoROM.accept-rom-license-0.6.0/AutoROM.py
--rw-rw-r--   0 jet       (1000) jet       (1000)     1074 2022-12-13 15:13:49.000000 AutoROM.accept-rom-license-0.6.0/LICENSE.txt
--rw-rw-r--   0 jet       (1000) jet       (1000)       18 2022-12-13 15:13:49.000000 AutoROM.accept-rom-license-0.6.0/MANIFEST.in
--rw-rw-r--   0 jet       (1000) jet       (1000)     2222 2023-03-20 12:35:53.486372 AutoROM.accept-rom-license-0.6.0/PKG-INFO
--rw-rw-r--   0 jet       (1000) jet       (1000)     1504 2023-03-17 17:03:14.000000 AutoROM.accept-rom-license-0.6.0/README.md
--rw-rw-r--   0 jet       (1000) jet       (1000)   414352 2023-03-17 17:08:28.000000 AutoROM.accept-rom-license-0.6.0/Roms.tar.gz
-drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-03-20 12:35:53.486372 AutoROM.accept-rom-license-0.6.0/__pycache__/
--rw-rw-r--   0 jet       (1000) jet       (1000)    11838 2023-03-17 17:08:28.000000 AutoROM.accept-rom-license-0.6.0/__pycache__/AutoROM.cpython-310.pyc
--rw-rw-r--   0 jet       (1000) jet       (1000)      180 2023-03-17 17:09:41.000000 AutoROM.accept-rom-license-0.6.0/pyproject.toml
--rw-rw-r--   0 jet       (1000) jet       (1000)      891 2023-03-20 12:35:53.486372 AutoROM.accept-rom-license-0.6.0/setup.cfg
--rw-rw-r--   0 jet       (1000) jet       (1000)      470 2023-02-16 21:09:41.000000 AutoROM.accept-rom-license-0.6.0/setup.py
--rw-rw-r--   0 jet       (1000) jet       (1000)        6 2023-03-17 17:22:13.000000 AutoROM.accept-rom-license-0.6.0/version.txt
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:47.142782 AutoROM.accept-rom-license-0.6.1/
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:47.142782 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/
+-rw-rw-r--   0 jet       (1000) jet       (1000)     2222 2023-04-06 15:28:47.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/PKG-INFO
+-rw-rw-r--   0 jet       (1000) jet       (1000)      436 2023-04-06 15:28:47.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/SOURCES.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-04-06 15:28:47.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/dependency_links.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)        1 2023-04-06 15:28:47.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/not-zip-safe
+-rw-rw-r--   0 jet       (1000) jet       (1000)       97 2023-04-06 15:28:47.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/requires.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)        8 2023-04-06 15:28:47.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/top_level.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)    12853 2023-03-17 17:04:23.000000 AutoROM.accept-rom-license-0.6.1/AutoROM.py
+-rw-rw-r--   0 jet       (1000) jet       (1000)     1074 2022-12-13 15:13:49.000000 AutoROM.accept-rom-license-0.6.1/LICENSE.txt
+-rw-rw-r--   0 jet       (1000) jet       (1000)       18 2022-12-13 15:13:49.000000 AutoROM.accept-rom-license-0.6.1/MANIFEST.in
+-rw-rw-r--   0 jet       (1000) jet       (1000)     2222 2023-04-06 15:28:47.142782 AutoROM.accept-rom-license-0.6.1/PKG-INFO
+-rw-rw-r--   0 jet       (1000) jet       (1000)     1504 2023-03-17 17:03:14.000000 AutoROM.accept-rom-license-0.6.1/README.md
+-rw-rw-r--   0 jet       (1000) jet       (1000)   414352 2023-03-17 17:08:28.000000 AutoROM.accept-rom-license-0.6.1/Roms.tar.gz
+drwxrwxr-x   0 jet       (1000) jet       (1000)        0 2023-04-06 15:28:47.142782 AutoROM.accept-rom-license-0.6.1/__pycache__/
+-rw-rw-r--   0 jet       (1000) jet       (1000)    11838 2023-03-17 17:08:28.000000 AutoROM.accept-rom-license-0.6.1/__pycache__/AutoROM.cpython-310.pyc
+-rw-rw-r--   0 jet       (1000) jet       (1000)      180 2023-03-17 17:09:41.000000 AutoROM.accept-rom-license-0.6.1/pyproject.toml
+-rw-rw-r--   0 jet       (1000) jet       (1000)      879 2023-04-06 15:28:47.142782 AutoROM.accept-rom-license-0.6.1/setup.cfg
+-rw-rw-r--   0 jet       (1000) jet       (1000)      470 2023-02-16 21:09:41.000000 AutoROM.accept-rom-license-0.6.1/setup.py
+-rw-rw-r--   0 jet       (1000) jet       (1000)        6 2023-04-06 15:22:54.000000 AutoROM.accept-rom-license-0.6.1/version.txt
```

### Comparing `AutoROM.accept-rom-license-0.6.0/AutoROM.accept_rom_license.egg-info/PKG-INFO` & `AutoROM.accept-rom-license-0.6.1/AutoROM.accept_rom_license.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: AutoROM.accept-rom-license
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

### Comparing `AutoROM.accept-rom-license-0.6.0/AutoROM.py` & `AutoROM.accept-rom-license-0.6.1/AutoROM.py`

 * *Files identical despite different names*

### Comparing `AutoROM.accept-rom-license-0.6.0/LICENSE.txt` & `AutoROM.accept-rom-license-0.6.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `AutoROM.accept-rom-license-0.6.0/PKG-INFO` & `AutoROM.accept-rom-license-0.6.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: AutoROM.accept-rom-license
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

### Comparing `AutoROM.accept-rom-license-0.6.0/README.md` & `AutoROM.accept-rom-license-0.6.1/README.md`

 * *Files identical despite different names*

### Comparing `AutoROM.accept-rom-license-0.6.0/Roms.tar.gz` & `AutoROM.accept-rom-license-0.6.1/Roms.tar.gz`

 * *Files identical despite different names*

### Comparing `AutoROM.accept-rom-license-0.6.0/__pycache__/AutoROM.cpython-310.pyc` & `AutoROM.accept-rom-license-0.6.1/__pycache__/AutoROM.cpython-310.pyc`

 * *Files identical despite different names*

### Comparing `AutoROM.accept-rom-license-0.6.0/setup.cfg` & `AutoROM.accept-rom-license-0.6.1/setup.cfg`

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

