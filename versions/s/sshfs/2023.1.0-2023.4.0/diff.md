# Comparing `tmp/sshfs-2023.1.0.tar.gz` & `tmp/sshfs-2023.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sshfs-2023.1.0.tar", last modified: Sun Jan 22 23:03:40 2023, max compression
+gzip compressed data, was "sshfs-2023.4.0.tar", last modified: Thu Apr  6 09:08:49 2023, max compression
```

## Comparing `sshfs-2023.1.0.tar` & `sshfs-2023.4.0.tar`

### file list

```diff
@@ -1,39 +1,39 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.610728 sshfs-2023.1.0/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.598728 sshfs-2023.1.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.602728 sshfs-2023.1.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-01-22 23:03:31.000000 sshfs-2023.1.0/.github/workflows/pre-commit.yml
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-22 23:03:31.000000 sshfs-2023.1.0/.github/workflows/publish.yml
--rw-r--r--   0 runner    (1001) docker     (123)      793 2023-01-22 23:03:31.000000 sshfs-2023.1.0/.github/workflows/test.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-01-22 23:03:31.000000 sshfs-2023.1.0/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-01-22 23:03:31.000000 sshfs-2023.1.0/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    11345 2023-01-22 23:03:31.000000 sshfs-2023.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-01-22 23:03:40.610728 sshfs-2023.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2623 2023-01-22 23:03:31.000000 sshfs-2023.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-01-22 23:03:31.000000 sshfs-2023.1.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-01-22 23:03:31.000000 sshfs-2023.1.0/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-01-22 23:03:40.610728 sshfs-2023.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-22 23:03:31.000000 sshfs-2023.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.606728 sshfs-2023.1.0/sshfs/
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      634 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/file.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.606728 sshfs-2023.1.0/sshfs/pools/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/pools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2472 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/pools/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/pools/hard.py
--rw-r--r--   0 runner    (1001) docker     (123)     1725 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/pools/soft.py
--rw-r--r--   0 runner    (1001) docker     (123)     9176 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/spec.py
--rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-01-22 23:03:31.000000 sshfs-2023.1.0/sshfs/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.606728 sshfs-2023.1.0/sshfs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-01-22 23:03:40.000000 sshfs-2023.1.0/sshfs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      616 2023-01-22 23:03:40.000000 sshfs-2023.1.0/sshfs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-22 23:03:40.000000 sshfs-2023.1.0/sshfs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-01-22 23:03:40.000000 sshfs-2023.1.0/sshfs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-22 23:03:40.000000 sshfs-2023.1.0/sshfs.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.606728 sshfs-2023.1.0/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-22 23:03:40.610728 sshfs-2023.1.0/tests/static/
--rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-01-22 23:03:31.000000 sshfs-2023.1.0/tests/static/user.key
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-01-22 23:03:31.000000 sshfs-2023.1.0/tests/static/user.key.pub
--rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-01-22 23:03:31.000000 sshfs-2023.1.0/tests/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4206 2023-01-22 23:03:31.000000 sshfs-2023.1.0/tests/test_sftp_pools.py
--rw-r--r--   0 runner    (1001) docker     (123)     8733 2023-01-22 23:03:31.000000 sshfs-2023.1.0/tests/test_sshfs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.278503 sshfs-2023.4.0/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.github/workflows/pre-commit.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.github/workflows/publish.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.github/workflows/test.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-04-06 09:08:39.000000 sshfs-2023.4.0/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    11345 2023-04-06 09:08:39.000000 sshfs-2023.4.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 09:08:49.278503 sshfs-2023.4.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2623 2023-04-06 09:08:39.000000 sshfs-2023.4.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-04-06 09:08:39.000000 sshfs-2023.4.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 09:08:39.000000 sshfs-2023.4.0/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 09:08:49.278503 sshfs-2023.4.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:08:39.000000 sshfs-2023.4.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/sshfs/
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      634 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/sshfs/pools/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2472 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/hard.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2231 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/pools/soft.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9176 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/spec.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-04-06 09:08:39.000000 sshfs-2023.4.0/sshfs/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.274503 sshfs-2023.4.0/sshfs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      616 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 09:08:49.000000 sshfs-2023.4.0/sshfs.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.278503 sshfs-2023.4.0/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:08:49.278503 sshfs-2023.4.0/tests/static/
+-rw-r--r--   0 runner    (1001) docker     (123)     2610 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/static/user.key
+-rw-r--r--   0 runner    (1001) docker     (123)      573 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/static/user.key.pub
+-rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4206 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/test_sftp_pools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8733 2023-04-06 09:08:39.000000 sshfs-2023.4.0/tests/test_sshfs.py
```

### Comparing `sshfs-2023.1.0/.github/workflows/publish.yml` & `sshfs-2023.4.0/.github/workflows/publish.yml`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/.github/workflows/test.yml` & `sshfs-2023.4.0/.github/workflows/test.yml`

 * *Files 3% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 jobs:
   test:
     runs-on: ${{ matrix.os }}
     strategy:
       fail-fast: true
 
       matrix:
-        os: [ubuntu-18.04, macos-10.15]
+        os: [ubuntu-latest, macos-latest]
         pyv: ["3.7", "3.8", "3.9", "3.10", "3.11.0-rc - 3.11"]
 
     steps:
     - uses: actions/checkout@v2
 
     - uses: actions/setup-python@v2
       with:
```

### Comparing `sshfs-2023.1.0/.gitignore` & `sshfs-2023.4.0/.gitignore`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/.pre-commit-config.yaml` & `sshfs-2023.4.0/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/LICENSE` & `sshfs-2023.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/PKG-INFO` & `sshfs-2023.4.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sshfs
-Version: 2023.1.0
+Version: 2023.4.0
 Summary: SSH Filesystem -- Async SSH/SFTP backend for fsspec
 License: Apache License 2.0
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `sshfs-2023.1.0/README.md` & `sshfs-2023.4.0/README.md`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/setup.cfg` & `sshfs-2023.4.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs/config.py` & `sshfs-2023.4.0/sshfs/config.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs/file.py` & `sshfs-2023.4.0/sshfs/file.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs/pools/base.py` & `sshfs-2023.4.0/sshfs/pools/base.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs/pools/hard.py` & `sshfs-2023.4.0/sshfs/pools/hard.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs/spec.py` & `sshfs-2023.4.0/sshfs/spec.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs/utils.py` & `sshfs-2023.4.0/sshfs/utils.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/sshfs.egg-info/PKG-INFO` & `sshfs-2023.4.0/sshfs.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sshfs
-Version: 2023.1.0
+Version: 2023.4.0
 Summary: SSH Filesystem -- Async SSH/SFTP backend for fsspec
 License: Apache License 2.0
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `sshfs-2023.1.0/sshfs.egg-info/SOURCES.txt` & `sshfs-2023.4.0/sshfs.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/tests/static/user.key` & `sshfs-2023.4.0/tests/static/user.key`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/tests/static/user.key.pub` & `sshfs-2023.4.0/tests/static/user.key.pub`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/tests/test_config.py` & `sshfs-2023.4.0/tests/test_config.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/tests/test_sftp_pools.py` & `sshfs-2023.4.0/tests/test_sftp_pools.py`

 * *Files identical despite different names*

### Comparing `sshfs-2023.1.0/tests/test_sshfs.py` & `sshfs-2023.4.0/tests/test_sshfs.py`

 * *Files identical despite different names*

