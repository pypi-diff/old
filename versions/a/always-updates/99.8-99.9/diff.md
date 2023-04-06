# Comparing `tmp/always_updates-99.8.tar.gz` & `tmp/always_updates-99.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/always_updates-99.8.tar", last modified: Thu Dec 29 21:42:52 2022, max compression
+gzip compressed data, was "dist/always_updates-99.9.tar", last modified: Sun Jan  1 18:35:41 2023, max compression
```

## Comparing `always_updates-99.8.tar` & `always_updates-99.9.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-29 21:42:52.000000 always_updates-99.8/
--rw-r--r--   0 runner    (1001) docker     (123)      845 2022-12-29 21:42:52.000000 always_updates-99.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      234 2022-12-29 21:42:49.000000 always_updates-99.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2022-12-29 21:42:49.000000 always_updates-99.8/always_updates/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2022-12-29 21:42:49.000000 always_updates-99.8/always_updates/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      845 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      302 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)       27 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       64 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2022-12-29 21:42:52.000000 always_updates-99.8/always_updates.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-29 21:42:52.000000 always_updates-99.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1302 2022-12-29 21:42:49.000000 always_updates-99.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-01 18:35:41.000000 always_updates-99.9/
+-rw-r--r--   0 runner    (1001) docker     (123)      845 2023-01-01 18:35:41.000000 always_updates-99.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-01-01 18:35:36.000000 always_updates-99.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-01 18:35:36.000000 always_updates-99.9/always_updates/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-01-01 18:35:36.000000 always_updates-99.9/always_updates/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      845 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       27 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-01-01 18:35:41.000000 always_updates-99.9/always_updates.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-01 18:35:41.000000 always_updates-99.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1302 2023-01-01 18:35:36.000000 always_updates-99.9/setup.py
```

### Comparing `always_updates-99.8/PKG-INFO` & `always_updates-99.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: always_updates
-Version: 99.8
+Version: 99.9
 Summary: always_updates updates your system, always.
 Home-page: https://github.com/alwaysupdates/always_updates
 Author: Always Updates
 Author-email: alwaysupdates@sixsixsigma.com
 License: MIT
 Download-URL: https://aupd.19700101t000000z.com
 Description: # always_updates
```

### Comparing `always_updates-99.8/always_updates.egg-info/PKG-INFO` & `always_updates-99.9/always_updates.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: always-updates
-Version: 99.8
+Version: 99.9
 Summary: always_updates updates your system, always.
 Home-page: https://github.com/alwaysupdates/always_updates
 Author: Always Updates
 Author-email: alwaysupdates@sixsixsigma.com
 License: MIT
 Download-URL: https://aupd.19700101t000000z.com
 Description: # always_updates
```

### Comparing `always_updates-99.8/setup.py` & `always_updates-99.9/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -13,15 +13,15 @@
     not x.startswith('#')) and (not x.startswith('-'))]
 dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                     if 'git+' not in x]
 
 setup (
 	name = 'always_updates',
 	description = 'always_updates updates your system, always.',
-	version = '99.8',
+	version = '99.9',
 	packages = find_packages(), # list of all packages
 	install_requires = install_requires,
 	python_requires='>=3.0',
 	entry_points='''
 	    [console_scripts]
 	    aupd=always_updates.__main__:main
 	''',
```

