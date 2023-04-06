# Comparing `tmp/lbt-dragonfly-0.9.98.tar.gz` & `tmp/lbt-dragonfly-0.9.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/lbt-dragonfly-0.9.98.tar", last modified: Tue May 24 21:24:23 2022, max compression
+gzip compressed data, was "dist/lbt-dragonfly-0.9.99.tar", last modified: Fri May 27 00:30:06 2022, max compression
```

## Comparing `lbt-dragonfly-0.9.98.tar` & `lbt-dragonfly-0.9.99.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     2039 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/.github/workflows/ci.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     3860 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/.github/workflows/dependency-release.yaml
--rw-r--r--   0 runner    (1001) docker     (121)      142 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)      294 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/.releaserc.json
--rw-r--r--   0 runner    (1001) docker     (121)      279 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/CODE_OF_CONDUCT.md
--rw-r--r--   0 runner    (1001) docker     (121)      445 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (121)    34523 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     2446 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1770 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      165 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/deploy.sh
--rw-r--r--   0 runner    (1001) docker     (121)       86 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/dev-requirements.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly/
--rw-r--r--   0 runner    (1001) docker     (121)      231 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/lbt_dragonfly/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2446 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      436 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       94 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)       44 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/pass_tests.py
--rw-r--r--   0 runner    (1001) docker     (121)       94 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      102 2022-05-24 21:24:23.000000 lbt-dragonfly-0.9.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1023 2022-05-24 21:23:05.000000 lbt-dragonfly-0.9.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/.github/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)     2039 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/.github/workflows/ci.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)     3860 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/.github/workflows/dependency-release.yaml
+-rw-r--r--   0 runner    (1001) docker     (121)      142 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)      294 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/.releaserc.json
+-rw-r--r--   0 runner    (1001) docker     (121)      279 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (121)      445 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (121)    34523 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     2446 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1770 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      165 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/deploy.sh
+-rw-r--r--   0 runner    (1001) docker     (121)       86 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/dev-requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly/
+-rw-r--r--   0 runner    (1001) docker     (121)      231 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/lbt_dragonfly/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2446 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      436 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       94 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       44 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/pass_tests.py
+-rw-r--r--   0 runner    (1001) docker     (121)       94 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      102 2022-05-27 00:30:06.000000 lbt-dragonfly-0.9.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1023 2022-05-27 00:28:59.000000 lbt-dragonfly-0.9.99/setup.py
```

### Comparing `lbt-dragonfly-0.9.98/.github/workflows/ci.yaml` & `lbt-dragonfly-0.9.99/.github/workflows/ci.yaml`

 * *Files identical despite different names*

### Comparing `lbt-dragonfly-0.9.98/.github/workflows/dependency-release.yaml` & `lbt-dragonfly-0.9.99/.github/workflows/dependency-release.yaml`

 * *Files identical despite different names*

### Comparing `lbt-dragonfly-0.9.98/LICENSE` & `lbt-dragonfly-0.9.99/LICENSE`

 * *Files identical despite different names*

### Comparing `lbt-dragonfly-0.9.98/PKG-INFO` & `lbt-dragonfly-0.9.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lbt-dragonfly
-Version: 0.9.98
+Version: 0.9.99
 Summary: Collection of all Dragonfly core Python libraries
 Home-page: https://github.com/ladybug-tools/lbt-dragonfly
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `lbt-dragonfly-0.9.98/README.md` & `lbt-dragonfly-0.9.99/README.md`

 * *Files identical despite different names*

### Comparing `lbt-dragonfly-0.9.98/lbt_dragonfly.egg-info/PKG-INFO` & `lbt-dragonfly-0.9.99/lbt_dragonfly.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lbt-dragonfly
-Version: 0.9.98
+Version: 0.9.99
 Summary: Collection of all Dragonfly core Python libraries
 Home-page: https://github.com/ladybug-tools/lbt-dragonfly
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: AGPL-3.0
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 2.7
```

### Comparing `lbt-dragonfly-0.9.98/setup.py` & `lbt-dragonfly-0.9.99/setup.py`

 * *Files identical despite different names*

