# Comparing `tmp/eons-2.3.3.tar.gz` & `tmp/eons-2.3.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "eons-2.3.3.tar", last modified: Thu Apr  6 23:55:10 2023, max compression
+gzip compressed data, was "eons-2.3.4.tar", last modified: Fri Apr  7 00:12:49 2023, max compression
```

## Comparing `eons-2.3.3.tar` & `eons-2.3.4.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:55:10.974755 eons-2.3.3/
--rw-r--r--   0 runner    (1001) docker     (123)    16886 2023-04-06 23:55:10.974755 eons-2.3.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    16599 2023-04-06 23:54:54.000000 eons-2.3.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:55:10.970755 eons-2.3.3/pkg/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:55:10.970755 eons-2.3.3/pkg/eons/
--rw-r--r--   0 runner    (1001) docker     (123)       20 2023-04-06 23:55:02.000000 eons-2.3.3/pkg/eons/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    81469 2023-04-06 23:55:02.000000 eons-2.3.3/pkg/eons/eons.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:55:10.974755 eons-2.3.3/pkg/eons/resolve/
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 23:55:02.000000 eons-2.3.3/pkg/eons/resolve/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-04-06 23:54:43.000000 eons-2.3.3/pkg/eons/resolve/resolve_find_by_fetch.py
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-04-06 23:54:43.000000 eons-2.3.3/pkg/eons/resolve/resolve_import_module.py
--rw-r--r--   0 runner    (1001) docker     (123)      490 2023-04-06 23:54:43.000000 eons-2.3.3/pkg/eons/resolve/resolve_install_from_repo.py
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-06 23:54:43.000000 eons-2.3.3/pkg/eons/resolve/resolve_install_from_repo_with_default_package_type.py
--rw-r--r--   0 runner    (1001) docker     (123)      390 2023-04-06 23:54:43.000000 eons-2.3.3/pkg/eons/resolve/resolve_install_with_pip.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:55:10.970755 eons-2.3.3/pkg/eons.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    16886 2023-04-06 23:55:10.000000 eons-2.3.3/pkg/eons.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      507 2023-04-06 23:55:10.000000 eons-2.3.3/pkg/eons.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 23:55:10.000000 eons-2.3.3/pkg/eons.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-06 23:55:10.000000 eons-2.3.3/pkg/eons.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 23:55:10.000000 eons-2.3.3/pkg/eons.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 23:55:02.000000 eons-2.3.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-06 23:55:10.974755 eons-2.3.3/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:12:49.618333 eons-2.3.4/
+-rw-r--r--   0 runner    (1001) docker     (123)    16886 2023-04-07 00:12:49.622333 eons-2.3.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    16599 2023-04-07 00:12:33.000000 eons-2.3.4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:12:49.610333 eons-2.3.4/pkg/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:12:49.614333 eons-2.3.4/pkg/eons/
+-rw-r--r--   0 runner    (1001) docker     (123)       20 2023-04-07 00:12:41.000000 eons-2.3.4/pkg/eons/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    81469 2023-04-07 00:12:41.000000 eons-2.3.4/pkg/eons/eons.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:12:49.618333 eons-2.3.4/pkg/eons/resolve/
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:12:41.000000 eons-2.3.4/pkg/eons/resolve/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3398 2023-04-07 00:12:20.000000 eons-2.3.4/pkg/eons/resolve/resolve_find_by_fetch.py
+-rw-r--r--   0 runner    (1001) docker     (123)      552 2023-04-07 00:12:20.000000 eons-2.3.4/pkg/eons/resolve/resolve_import_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)      490 2023-04-07 00:12:20.000000 eons-2.3.4/pkg/eons/resolve/resolve_install_from_repo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      594 2023-04-07 00:12:20.000000 eons-2.3.4/pkg/eons/resolve/resolve_install_from_repo_with_default_package_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)      390 2023-04-07 00:12:20.000000 eons-2.3.4/pkg/eons/resolve/resolve_install_with_pip.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:12:49.614333 eons-2.3.4/pkg/eons.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    16886 2023-04-07 00:12:49.000000 eons-2.3.4/pkg/eons.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      507 2023-04-07 00:12:49.000000 eons-2.3.4/pkg/eons.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:12:49.000000 eons-2.3.4/pkg/eons.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-07 00:12:49.000000 eons-2.3.4/pkg/eons.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-07 00:12:49.000000 eons-2.3.4/pkg/eons.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-07 00:12:41.000000 eons-2.3.4/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-07 00:12:49.622333 eons-2.3.4/setup.cfg
```

### Comparing `eons-2.3.3/PKG-INFO` & `eons-2.3.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eons
-Version: 2.3.3
+Version: 2.3.4
 Summary: Eons Python Framework
 Home-page: https://github.com/eons-dev/eons.lib
 Author: Eons
 Author-email: support@eons.llc
 Project-URL: Bug Tracker, https://github.com/eons-dev/eons.lib/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `eons-2.3.3/README.md` & `eons-2.3.4/README.md`

 * *Files identical despite different names*

### Comparing `eons-2.3.3/pkg/eons/eons.py` & `eons-2.3.4/pkg/eons/eons.py`

 * *Files identical despite different names*

### Comparing `eons-2.3.3/pkg/eons/resolve/resolve_find_by_fetch.py` & `eons-2.3.4/pkg/eons/resolve/resolve_find_by_fetch.py`

 * *Files identical despite different names*

### Comparing `eons-2.3.3/pkg/eons/resolve/resolve_import_module.py` & `eons-2.3.4/pkg/eons/resolve/resolve_import_module.py`

 * *Files identical despite different names*

### Comparing `eons-2.3.3/pkg/eons.egg-info/PKG-INFO` & `eons-2.3.4/pkg/eons.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eons
-Version: 2.3.3
+Version: 2.3.4
 Summary: Eons Python Framework
 Home-page: https://github.com/eons-dev/eons.lib
 Author: Eons
 Author-email: support@eons.llc
 Project-URL: Bug Tracker, https://github.com/eons-dev/eons.lib/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `eons-2.3.3/setup.cfg` & `eons-2.3.4/setup.cfg`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = eons
-version = 2.3.3
+version = 2.3.4
 author = Eons
 author_email = support@eons.llc
 description = Eons Python Framework
 license_files = LICENSE.txt
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/eons-dev/eons.lib
@@ -18,18 +18,18 @@
 
 [options]
 package_dir = 
 	= pkg
 packages = find:
 python_requires = >=3.7
 install_requires = 
+	requests
 	tqdm
-	jsonpickle
 	pyyaml
-	requests
+	jsonpickle
 
 [options.packages.find]
 where = pkg
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

