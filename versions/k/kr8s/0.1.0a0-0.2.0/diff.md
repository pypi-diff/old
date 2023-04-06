# Comparing `tmp/kr8s-0.1.0a0.tar.gz` & `tmp/kr8s-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kr8s-0.1.0a0.tar", max compression
+gzip compressed data, was "kr8s-0.2.0.tar", max compression
```

## Comparing `kr8s-0.1.0a0.tar` & `kr8s-0.2.0.tar`

### file list

```diff
@@ -1,11 +1,19 @@
--rw-r--r--   0        0        0     1549 2023-03-23 14:43:10.894081 kr8s-0.1.0a0/LICENSE
--rw-r--r--   0        0        0       36 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/README.md
--rw-r--r--   0        0        0      263 2023-03-23 14:56:30.518382 kr8s-0.1.0a0/kr8s/__init__.py
--rw-r--r--   0        0        0      722 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/kr8s/conftest.py
--rw-r--r--   0        0        0      895 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/kr8s/mixins.py
--rw-r--r--   0        0        0     7558 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/kr8s/objects.py
--rw-r--r--   0        0        0     2634 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/kr8s/query.py
--rw-r--r--   0        0        0      866 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/kr8s/tests/test_pykube_objects.py
--rw-r--r--   0        0        0      598 2023-03-23 14:43:48.769581 kr8s-0.1.0a0/kr8s/tests/test_query.py
--rw-r--r--   0        0        0     2113 2023-03-23 14:56:30.518382 kr8s-0.1.0a0/pyproject.toml
--rw-r--r--   0        0        0      657 1970-01-01 00:00:00.000000 kr8s-0.1.0a0/PKG-INFO
+-rw-r--r--   0        0        0     1549 2023-03-23 14:43:10.894081 kr8s-0.2.0/LICENSE
+-rw-r--r--   0        0        0     1723 2023-04-06 10:31:33.883067 kr8s-0.2.0/README.md
+-rw-r--r--   0        0        0      253 2023-04-06 13:16:03.716834 kr8s-0.2.0/kr8s/__init__.py
+-rw-r--r--   0        0        0     5981 2023-04-06 13:15:55.624937 kr8s-0.2.0/kr8s/_api.py
+-rw-r--r--   0        0        0     5141 2023-04-05 14:28:29.381766 kr8s-0.2.0/kr8s/_auth.py
+-rw-r--r--   0        0        0      361 2023-04-04 19:30:47.872877 kr8s-0.2.0/kr8s/_data_utils.py
+-rw-r--r--   0        0        0       81 2023-04-03 16:55:51.155586 kr8s-0.2.0/kr8s/_exceptions.py
+-rw-r--r--   0        0        0      672 2023-04-03 16:55:51.155586 kr8s-0.2.0/kr8s/_testutils.py
+-rw-r--r--   0        0        0     3543 2023-04-05 14:28:29.381766 kr8s-0.2.0/kr8s/conftest.py
+-rw-r--r--   0        0        0    18941 2023-04-06 13:15:55.624937 kr8s-0.2.0/kr8s/objects.py
+-rw-r--r--   0        0        0       61 2023-03-31 20:28:17.436142 kr8s-0.2.0/kr8s/tests/resources/serviceaccount.yaml
+-rwxr-xr-x   0        0        0      614 2023-04-03 16:55:51.155586 kr8s-0.2.0/kr8s/tests/scripts/envexec.py
+-rw-r--r--   0        0        0     1500 2023-04-06 11:27:48.029578 kr8s-0.2.0/kr8s/tests/test_api.py
+-rw-r--r--   0        0        0     2346 2023-04-03 16:55:51.155586 kr8s-0.2.0/kr8s/tests/test_auth.py
+-rw-r--r--   0        0        0      300 2023-04-04 19:30:47.872877 kr8s-0.2.0/kr8s/tests/test_data_utils.py
+-rw-r--r--   0        0        0     7333 2023-04-06 13:15:55.624937 kr8s-0.2.0/kr8s/tests/test_objects.py
+-rw-r--r--   0        0        0      622 2023-04-03 16:55:51.155586 kr8s-0.2.0/kr8s/tests/test_testutils.py
+-rw-r--r--   0        0        0     2149 2023-04-06 13:16:03.716834 kr8s-0.2.0/pyproject.toml
+-rw-r--r--   0        0        0     2380 1970-01-01 00:00:00.000000 kr8s-0.2.0/PKG-INFO
```

### Comparing `kr8s-0.1.0a0/LICENSE` & `kr8s-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `kr8s-0.1.0a0/pyproject.toml` & `kr8s-0.2.0/pyproject.toml`

 * *Files 10% similar despite different names*

```diff
@@ -8,22 +8,21 @@
 keywords = ["kubernetes", "kubectl"]
 license = {text = "BSD-3-Clause"}
 classifiers = [
     "Programming Language :: Python :: 3",
 ]
 dependencies = [
     "aiohttp",
-    "pykube",
     'importlib-metadata; python_version<"3.8"',
 ]
 dynamic = ["version"]
 
 [tool.poetry]
 name = "kr8s"
-version = "0.1.0-a.0"  # This will be populated at build time by poetry-dynamic-versioning
+version = "0.2.0"  # This will be populated at build time by poetry-dynamic-versioning
 description = "A Kubernetes API library"
 authors = ["Jacob Tomlinson <jacob@tomlinson.email>"]
 license = "BSD-3-Clause"
 readme = "README.md"
 
 [tool.poetry-dynamic-versioning]
 enable = false
@@ -32,27 +31,30 @@
 
 [tool.poetry-dynamic-versioning.substitution]
 files = ["kr8s/__init__.py"]
 
 [tool.poetry.dependencies]
 python = "^3.8"
 aiohttp = "^3.8.4"
-pykube-ng = "^22.9.0"
+pyyaml = "^6.0"
+asyncio-atexit = "^1.0.1"
 
 
 [tool.poetry.group.test.dependencies]
 pytest = "^7.2.2"
 pytest-asyncio = "^0.20.3"
 pytest-kind = {git = "https://codeberg.org/hjacobs/pytest-kind.git"}
 pytest-timeout = "^2.1.0"
+pytest-rerunfailures = "^11.1.2"
 
 [tool.pytest.ini_options]
 addopts = "-v --keep-cluster --durations=10"
 timeout = 300
-reruns = 5
+reruns = 0
+reruns_delay = 1
 asyncio_mode = "auto"
 
 [build-system]
 requires = ["poetry-core>=1.0.0", "poetry-dynamic-versioning"]
 build-backend = "poetry_dynamic_versioning.backend"
 
 [tool.ruff]
@@ -84,15 +86,14 @@
     "buck-out",
     "build",
     "dist",
     "node_modules",
     "venv",
 ]
 
-# Same as Black.
-line-length = 88
+line-length = 120
 
 # Allow unused variables when underscore-prefixed.
 dummy-variable-rgx = "^(_+|(_+[a-zA-Z0-9_]*[a-zA-Z0-9]+?))$"
 
 # Assume Python 3.10.
 target-version = "py310"
```

