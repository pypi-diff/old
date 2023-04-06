# Comparing `tmp/lbt-honeybee-0.7.98.tar.gz` & `tmp/lbt-honeybee-0.7.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/lbt-honeybee-0.7.98.tar", last modified: Fri Jan 27 20:20:11 2023, max compression
+gzip compressed data, was "dist/lbt-honeybee-0.7.99.tar", last modified: Fri Jan 27 22:31:23 2023, max compression
```

## Comparing `lbt-honeybee-0.7.98.tar` & `lbt-honeybee-0.7.99.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/.dockerignore
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     3377 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/.github/workflows/ci.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     3966 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/.github/workflows/dependency-release.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/.releaserc.json
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (123)      447 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/Dockerfile
--rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      690 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/deploy.sh
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/dev-requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee/
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/lbt_honeybee/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/lbt_honeybee.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/pass_tests.py
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-01-27 20:20:11.000000 lbt-honeybee-0.7.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-01-27 20:18:57.000000 lbt-honeybee-0.7.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/.dockerignore
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     3377 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/.github/workflows/ci.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     3966 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/.github/workflows/dependency-release.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/.releaserc.json
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (123)      447 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/Dockerfile
+-rw-r--r--   0 runner    (1001) docker     (123)    34523 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2249 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      690 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/deploy.sh
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/dev-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee/
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/lbt_honeybee/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/lbt_honeybee.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/pass_tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-01-27 22:31:23.000000 lbt-honeybee-0.7.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-01-27 22:30:07.000000 lbt-honeybee-0.7.99/setup.py
```

### Comparing `lbt-honeybee-0.7.98/.github/workflows/ci.yaml` & `lbt-honeybee-0.7.99/.github/workflows/ci.yaml`

 * *Files identical despite different names*

### Comparing `lbt-honeybee-0.7.98/.github/workflows/dependency-release.yaml` & `lbt-honeybee-0.7.99/.github/workflows/dependency-release.yaml`

 * *Files identical despite different names*

### Comparing `lbt-honeybee-0.7.98/Dockerfile` & `lbt-honeybee-0.7.99/Dockerfile`

 * *Files identical despite different names*

### Comparing `lbt-honeybee-0.7.98/LICENSE` & `lbt-honeybee-0.7.99/LICENSE`

 * *Files identical despite different names*

### Comparing `lbt-honeybee-0.7.98/PKG-INFO` & `lbt-honeybee-0.7.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lbt-honeybee
-Version: 0.7.98
+Version: 0.7.99
 Summary: Collection of all Honeybee core Python libraries
 Home-page: https://github.com/ladybug-tools/lbt-honeybee
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `lbt-honeybee-0.7.98/README.md` & `lbt-honeybee-0.7.99/README.md`

 * *Files identical despite different names*

### Comparing `lbt-honeybee-0.7.98/deploy.sh` & `lbt-honeybee-0.7.99/deploy.sh`

 * *Files identical despite different names*

### Comparing `lbt-honeybee-0.7.98/lbt_honeybee.egg-info/PKG-INFO` & `lbt-honeybee-0.7.99/lbt_honeybee.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lbt-honeybee
-Version: 0.7.98
+Version: 0.7.99
 Summary: Collection of all Honeybee core Python libraries
 Home-page: https://github.com/ladybug-tools/lbt-honeybee
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `lbt-honeybee-0.7.98/setup.py` & `lbt-honeybee-0.7.99/setup.py`

 * *Files identical despite different names*

