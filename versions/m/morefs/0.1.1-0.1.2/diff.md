# Comparing `tmp/morefs-0.1.1.tar.gz` & `tmp/morefs-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "morefs-0.1.1.tar", last modified: Fri Apr  7 07:58:36 2023, max compression
+gzip compressed data, was "morefs-0.1.2.tar", last modified: Fri Apr  7 10:35:30 2023, max compression
```

## Comparing `morefs-0.1.1.tar` & `morefs-0.1.2.tar`

### file list

```diff
@@ -1,41 +1,41 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.512231 morefs-0.1.1/
--rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-07 07:58:08.000000 morefs-0.1.1/.cruft.json
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-07 07:58:08.000000 morefs-0.1.1/.gitattributes
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.508231 morefs-0.1.1/.github/
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-07 07:58:08.000000 morefs-0.1.1/.github/dependabot.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.508231 morefs-0.1.1/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 07:58:08.000000 morefs-0.1.1/.github/workflows/release.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-04-07 07:58:08.000000 morefs-0.1.1/.github/workflows/tests.yml
--rw-r--r--   0 runner    (1001) docker     (123)      298 2023-04-07 07:58:08.000000 morefs-0.1.1/.github/workflows/update-template.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     2035 2023-04-07 07:58:08.000000 morefs-0.1.1/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     1477 2023-04-07 07:58:08.000000 morefs-0.1.1/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     5396 2023-04-07 07:58:08.000000 morefs-0.1.1/CODE_OF_CONDUCT.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2642 2023-04-07 07:58:08.000000 morefs-0.1.1/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (123)    11340 2023-04-07 07:58:08.000000 morefs-0.1.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2791 2023-04-07 07:58:36.512231 morefs-0.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2041 2023-04-07 07:58:08.000000 morefs-0.1.1/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-04-07 07:58:08.000000 morefs-0.1.1/noxfile.py
--rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-04-07 07:58:08.000000 morefs-0.1.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1560 2023-04-07 07:58:36.512231 morefs-0.1.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.504231 morefs-0.1.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.508231 morefs-0.1.1/src/morefs/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:08.000000 morefs-0.1.1/src/morefs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2917 2023-04-07 07:58:08.000000 morefs-0.1.1/src/morefs/asyn_local.py
--rw-r--r--   0 runner    (1001) docker     (123)     9445 2023-04-07 07:58:08.000000 morefs-0.1.1/src/morefs/dict.py
--rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-07 07:58:08.000000 morefs-0.1.1/src/morefs/memory.py
--rw-r--r--   0 runner    (1001) docker     (123)     5728 2023-04-07 07:58:08.000000 morefs-0.1.1/src/morefs/overlay.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:08.000000 morefs-0.1.1/src/morefs/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.512231 morefs-0.1.1/src/morefs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2791 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 07:58:36.000000 morefs-0.1.1/src/morefs.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:58:36.512231 morefs-0.1.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-07 07:58:08.000000 morefs-0.1.1/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4060 2023-04-07 07:58:08.000000 morefs-0.1.1/tests/test_asyn_local.py
--rw-r--r--   0 runner    (1001) docker     (123)     7531 2023-04-07 07:58:08.000000 morefs-0.1.1/tests/test_dictfs.py
--rw-r--r--   0 runner    (1001) docker     (123)     5207 2023-04-07 07:58:08.000000 morefs-0.1.1/tests/test_memfs.py
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-07 07:58:08.000000 morefs-0.1.1/tests/test_morefs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.029251 morefs-0.1.2/
+-rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-07 10:35:03.000000 morefs-0.1.2/.cruft.json
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-07 10:35:03.000000 morefs-0.1.2/.gitattributes
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.025251 morefs-0.1.2/.github/
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-07 10:35:03.000000 morefs-0.1.2/.github/dependabot.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.025251 morefs-0.1.2/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 10:35:03.000000 morefs-0.1.2/.github/workflows/release.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1203 2023-04-07 10:35:03.000000 morefs-0.1.2/.github/workflows/tests.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      298 2023-04-07 10:35:03.000000 morefs-0.1.2/.github/workflows/update-template.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     2035 2023-04-07 10:35:03.000000 morefs-0.1.2/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     1477 2023-04-07 10:35:03.000000 morefs-0.1.2/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     5396 2023-04-07 10:35:03.000000 morefs-0.1.2/CODE_OF_CONDUCT.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2642 2023-04-07 10:35:03.000000 morefs-0.1.2/CONTRIBUTING.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    11340 2023-04-07 10:35:03.000000 morefs-0.1.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-04-07 10:35:30.029251 morefs-0.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3978 2023-04-07 10:35:03.000000 morefs-0.1.2/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-04-07 10:35:03.000000 morefs-0.1.2/noxfile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1856 2023-04-07 10:35:03.000000 morefs-0.1.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1560 2023-04-07 10:35:30.029251 morefs-0.1.2/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.021251 morefs-0.1.2/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.025251 morefs-0.1.2/src/morefs/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:03.000000 morefs-0.1.2/src/morefs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3677 2023-04-07 10:35:03.000000 morefs-0.1.2/src/morefs/asyn_local.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9445 2023-04-07 10:35:03.000000 morefs-0.1.2/src/morefs/dict.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-07 10:35:03.000000 morefs-0.1.2/src/morefs/memory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5728 2023-04-07 10:35:03.000000 morefs-0.1.2/src/morefs/overlay.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:03.000000 morefs-0.1.2/src/morefs/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.025251 morefs-0.1.2/src/morefs.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4728 2023-04-07 10:35:29.000000 morefs-0.1.2/src/morefs.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-07 10:35:30.000000 morefs-0.1.2/src/morefs.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:35:29.000000 morefs-0.1.2/src/morefs.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-07 10:35:29.000000 morefs-0.1.2/src/morefs.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:35:29.000000 morefs-0.1.2/src/morefs.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-07 10:35:29.000000 morefs-0.1.2/src/morefs.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 10:35:29.000000 morefs-0.1.2/src/morefs.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:35:30.029251 morefs-0.1.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-07 10:35:03.000000 morefs-0.1.2/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4060 2023-04-07 10:35:03.000000 morefs-0.1.2/tests/test_asyn_local.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7531 2023-04-07 10:35:03.000000 morefs-0.1.2/tests/test_dictfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5207 2023-04-07 10:35:03.000000 morefs-0.1.2/tests/test_memfs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-04-07 10:35:03.000000 morefs-0.1.2/tests/test_morefs.py
```

### Comparing `morefs-0.1.1/.cruft.json` & `morefs-0.1.2/.cruft.json`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/.github/dependabot.yml` & `morefs-0.1.2/.github/dependabot.yml`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/.github/workflows/release.yml` & `morefs-0.1.2/.github/workflows/release.yml`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/.github/workflows/tests.yml` & `morefs-0.1.2/.github/workflows/tests.yml`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/.gitignore` & `morefs-0.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/.pre-commit-config.yaml` & `morefs-0.1.2/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/CODE_OF_CONDUCT.rst` & `morefs-0.1.2/CODE_OF_CONDUCT.rst`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/CONTRIBUTING.rst` & `morefs-0.1.2/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/LICENSE` & `morefs-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/noxfile.py` & `morefs-0.1.2/noxfile.py`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/pyproject.toml` & `morefs-0.1.2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/setup.cfg` & `morefs-0.1.2/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -39,15 +39,15 @@
 	%(memfs)s
 	%(asynclocalfs)s
 tests = 
 	pytest==7.2.0
 	pytest-sugar==0.9.5
 	pytest-cov==3.0.0
 	pytest-mock==3.8.2
-	pytest-asyncio==0.19.0
+	pytest-asyncio==0.21.0
 	pylint==2.15.0
 	mypy==0.971
 	%(all)s
 dev = 
 	%(tests)s
 	%(all)s
 	types-aiofiles
```

### Comparing `morefs-0.1.1/src/morefs/dict.py` & `morefs-0.1.2/src/morefs/dict.py`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/src/morefs/memory.py` & `morefs-0.1.2/src/morefs/memory.py`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/src/morefs/overlay.py` & `morefs-0.1.2/src/morefs/overlay.py`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/src/morefs.egg-info/SOURCES.txt` & `morefs-0.1.2/src/morefs.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/src/morefs.egg-info/requires.txt` & `morefs-0.1.2/src/morefs.egg-info/requires.txt`

 * *Files 11% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 typing_extensions>=3.10.0
 
 [dev]
 pytest==7.2.0
 pytest-sugar==0.9.5
 pytest-cov==3.0.0
 pytest-mock==3.8.2
-pytest-asyncio==0.19.0
+pytest-asyncio==0.21.0
 pylint==2.15.0
 mypy==0.971
 pygtrie>=2.3.2
 fsspec>=2022.10.0
 aiofile<4,>=3.8.5
 types-aiofiles
 
@@ -42,15 +42,15 @@
 pygtrie>=2.3.2
 
 [tests]
 pytest==7.2.0
 pytest-sugar==0.9.5
 pytest-cov==3.0.0
 pytest-mock==3.8.2
-pytest-asyncio==0.19.0
+pytest-asyncio==0.21.0
 pylint==2.15.0
 mypy==0.971
 pygtrie>=2.3.2
 fsspec>=2022.10.0
 aiofile<4,>=3.8.5
 
 [tests:python_version < "3.10"]
```

### Comparing `morefs-0.1.1/tests/test_asyn_local.py` & `morefs-0.1.2/tests/test_asyn_local.py`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/tests/test_dictfs.py` & `morefs-0.1.2/tests/test_dictfs.py`

 * *Files identical despite different names*

### Comparing `morefs-0.1.1/tests/test_memfs.py` & `morefs-0.1.2/tests/test_memfs.py`

 * *Files identical despite different names*

