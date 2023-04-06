# Comparing `tmp/mesoSPIM-python-tools-0.0.2.tar.gz` & `tmp/mesoSPIM-python-tools-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mesoSPIM-python-tools-0.0.2.tar", last modified: Wed Apr  5 22:38:17 2023, max compression
+gzip compressed data, was "mesoSPIM-python-tools-0.0.3.tar", last modified: Thu Apr  6 22:57:26 2023, max compression
```

## Comparing `mesoSPIM-python-tools-0.0.2.tar` & `mesoSPIM-python-tools-0.0.3.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.628740 mesoSPIM-python-tools-0.0.2/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.624740 mesoSPIM-python-tools-0.0.2/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.624740 mesoSPIM-python-tools-0.0.2/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/.github/workflows/test_and_deploy.yml
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      805 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-04-05 22:38:17.628740 mesoSPIM-python-tools-0.0.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/changelog.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.624740 mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-04-05 22:38:17.000000 mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      575 2023-04-05 22:38:17.000000 mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 22:38:17.000000 mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-05 22:38:17.000000 mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-05 22:38:17.000000 mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.624740 mesoSPIM-python-tools-0.0.2/mesospim_python_tools/
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/mesospim_python_tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/mesospim_python_tools/io.py
--rw-r--r--   0 runner    (1001) docker     (123)     3645 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/mesospim_python_tools/metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 22:38:17.628740 mesoSPIM-python-tools-0.0.2/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.624740 mesoSPIM-python-tools-0.0.2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.624740 mesoSPIM-python-tools-0.0.2/tests/test_integration/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/tests/test_integration/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:17.628740 mesoSPIM-python-tools-0.0.2/tests/test_unit/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/tests/test_unit/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/tests/test_unit/test_placeholder.py
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-05 22:38:08.000000 mesoSPIM-python-tools-0.0.2/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.047337 mesoSPIM-python-tools-0.0.3/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/.github/workflows/test_and_deploy.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      805 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1492 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      863 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/changelog.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      863 2023-04-06 22:57:26.000000 mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      575 2023-04-06 22:57:26.000000 mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 22:57:26.000000 mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-06 22:57:26.000000 mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 22:57:26.000000 mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/mesospim_python_tools/
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/mesospim_python_tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/mesospim_python_tools/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3645 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/mesospim_python_tools/metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/tests/test_integration/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/tests/test_integration/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:26.051337 mesoSPIM-python-tools-0.0.3/tests/test_unit/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/tests/test_unit/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       40 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/tests/test_unit/test_placeholder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-06 22:57:16.000000 mesoSPIM-python-tools-0.0.3/tox.ini
```

### Comparing `mesoSPIM-python-tools-0.0.2/.github/workflows/test_and_deploy.yml` & `mesoSPIM-python-tools-0.0.3/.github/workflows/test_and_deploy.yml`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/.gitignore` & `mesoSPIM-python-tools-0.0.3/.gitignore`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/.pre-commit-config.yaml` & `mesoSPIM-python-tools-0.0.3/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/LICENSE` & `mesoSPIM-python-tools-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/mesoSPIM_python_tools.egg-info/SOURCES.txt` & `mesoSPIM-python-tools-0.0.3/mesoSPIM_python_tools.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/mesospim_python_tools/io.py` & `mesoSPIM-python-tools-0.0.3/mesospim_python_tools/io.py`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/mesospim_python_tools/metadata.py` & `mesoSPIM-python-tools-0.0.3/mesospim_python_tools/metadata.py`

 * *Files identical despite different names*

### Comparing `mesoSPIM-python-tools-0.0.2/pyproject.toml` & `mesoSPIM-python-tools-0.0.3/pyproject.toml`

 * *Files identical despite different names*

