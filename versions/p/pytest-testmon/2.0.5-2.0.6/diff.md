# Comparing `tmp/pytest-testmon-2.0.5.tar.gz` & `tmp/pytest-testmon-2.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytest-testmon-2.0.5.tar", last modified: Wed Apr  5 15:01:10 2023, max compression
+gzip compressed data, was "pytest-testmon-2.0.6.tar", last modified: Thu Apr  6 15:30:20 2023, max compression
```

## Comparing `pytest-testmon-2.0.5.tar` & `pytest-testmon-2.0.6.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 poko      (1000) poko      (1000)        0 2023-04-05 15:01:10.151957 pytest-testmon-2.0.5/
--rw-r--r--   0 poko      (1000) poko      (1000)    34633 2023-01-12 14:59:27.000000 pytest-testmon-2.0.5/LICENSE
--rw-r--r--   0 poko      (1000) poko      (1000)       74 2023-03-09 09:22:22.000000 pytest-testmon-2.0.5/MANIFEST.in
--rw-r--r--   0 poko      (1000) poko      (1000)     2429 2023-04-05 15:01:10.151957 pytest-testmon-2.0.5/PKG-INFO
--rw-r--r--   0 poko      (1000) poko      (1000)     1208 2023-03-27 16:31:43.000000 pytest-testmon-2.0.5/README.md
--rw-r--r--   0 poko      (1000) poko      (1000)     1619 2023-04-05 14:50:32.000000 pytest-testmon-2.0.5/pyproject.toml
-drwxr-xr-x   0 poko      (1000) poko      (1000)        0 2023-04-05 15:01:10.151957 pytest-testmon-2.0.5/pytest_testmon.egg-info/
--rw-r--r--   0 poko      (1000) poko      (1000)     2429 2023-04-05 15:01:10.000000 pytest-testmon-2.0.5/pytest_testmon.egg-info/PKG-INFO
--rw-r--r--   0 poko      (1000) poko      (1000)      463 2023-04-05 15:01:10.000000 pytest-testmon-2.0.5/pytest_testmon.egg-info/SOURCES.txt
--rw-r--r--   0 poko      (1000) poko      (1000)        1 2023-04-05 15:01:10.000000 pytest-testmon-2.0.5/pytest_testmon.egg-info/dependency_links.txt
--rw-r--r--   0 poko      (1000) poko      (1000)       51 2023-04-05 15:01:10.000000 pytest-testmon-2.0.5/pytest_testmon.egg-info/entry_points.txt
--rw-r--r--   0 poko      (1000) poko      (1000)       28 2023-04-05 15:01:10.000000 pytest-testmon-2.0.5/pytest_testmon.egg-info/requires.txt
--rw-r--r--   0 poko      (1000) poko      (1000)        8 2023-04-05 15:01:10.000000 pytest-testmon-2.0.5/pytest_testmon.egg-info/top_level.txt
--rw-r--r--   0 poko      (1000) poko      (1000)     1219 2023-04-05 15:01:10.151957 pytest-testmon-2.0.5/setup.cfg
--rw-r--r--   0 poko      (1000) poko      (1000)       69 2023-04-05 14:50:32.000000 pytest-testmon-2.0.5/setup.py
-drwxr-xr-x   0 poko      (1000) poko      (1000)        0 2023-04-05 15:01:10.151957 pytest-testmon-2.0.5/testmon/
--rw-r--r--   0 poko      (1000) poko      (1000)       44 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/__init__.py
--rw-r--r--   0 poko      (1000) poko      (1000)      183 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/common.py
--rw-r--r--   0 poko      (1000) poko      (1000)     3786 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/configure.py
--rw-r--r--   0 poko      (1000) poko      (1000)    22226 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/db.py
--rw-r--r--   0 poko      (1000) poko      (1000)     7867 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/process_code.py
--rw-r--r--   0 poko      (1000) poko      (1000)    17025 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/pytest_testmon.py
--rw-r--r--   0 poko      (1000) poko      (1000)    18875 2023-04-05 14:50:33.000000 pytest-testmon-2.0.5/testmon/testmon_core.py
--rw-r--r--   0 poko      (1000) poko      (1000)     1232 2023-01-12 14:59:27.000000 pytest-testmon-2.0.5/testmon/tox_testmon.py
+drwxr-xr-x   0 poko      (1000) poko      (1000)        0 2023-04-06 15:30:20.021736 pytest-testmon-2.0.6/
+-rw-r--r--   0 poko      (1000) poko      (1000)    34633 2023-01-12 14:59:27.000000 pytest-testmon-2.0.6/LICENSE
+-rw-r--r--   0 poko      (1000) poko      (1000)       74 2023-03-09 09:22:22.000000 pytest-testmon-2.0.6/MANIFEST.in
+-rw-r--r--   0 poko      (1000) poko      (1000)     2429 2023-04-06 15:30:20.021736 pytest-testmon-2.0.6/PKG-INFO
+-rw-r--r--   0 poko      (1000) poko      (1000)     1208 2023-03-27 16:31:43.000000 pytest-testmon-2.0.6/README.md
+-rw-r--r--   0 poko      (1000) poko      (1000)     1619 2023-04-06 15:26:55.000000 pytest-testmon-2.0.6/pyproject.toml
+drwxr-xr-x   0 poko      (1000) poko      (1000)        0 2023-04-06 15:30:20.021736 pytest-testmon-2.0.6/pytest_testmon.egg-info/
+-rw-r--r--   0 poko      (1000) poko      (1000)     2429 2023-04-06 15:30:20.000000 pytest-testmon-2.0.6/pytest_testmon.egg-info/PKG-INFO
+-rw-r--r--   0 poko      (1000) poko      (1000)      463 2023-04-06 15:30:20.000000 pytest-testmon-2.0.6/pytest_testmon.egg-info/SOURCES.txt
+-rw-r--r--   0 poko      (1000) poko      (1000)        1 2023-04-06 15:30:20.000000 pytest-testmon-2.0.6/pytest_testmon.egg-info/dependency_links.txt
+-rw-r--r--   0 poko      (1000) poko      (1000)       51 2023-04-06 15:30:20.000000 pytest-testmon-2.0.6/pytest_testmon.egg-info/entry_points.txt
+-rw-r--r--   0 poko      (1000) poko      (1000)       28 2023-04-06 15:30:20.000000 pytest-testmon-2.0.6/pytest_testmon.egg-info/requires.txt
+-rw-r--r--   0 poko      (1000) poko      (1000)        8 2023-04-06 15:30:20.000000 pytest-testmon-2.0.6/pytest_testmon.egg-info/top_level.txt
+-rw-r--r--   0 poko      (1000) poko      (1000)     1219 2023-04-06 15:30:20.021736 pytest-testmon-2.0.6/setup.cfg
+-rw-r--r--   0 poko      (1000) poko      (1000)       69 2023-04-06 15:26:55.000000 pytest-testmon-2.0.6/setup.py
+drwxr-xr-x   0 poko      (1000) poko      (1000)        0 2023-04-06 15:30:20.021736 pytest-testmon-2.0.6/testmon/
+-rw-r--r--   0 poko      (1000) poko      (1000)       44 2023-04-06 15:26:56.000000 pytest-testmon-2.0.6/testmon/__init__.py
+-rw-r--r--   0 poko      (1000) poko      (1000)      183 2023-04-06 15:26:56.000000 pytest-testmon-2.0.6/testmon/common.py
+-rw-r--r--   0 poko      (1000) poko      (1000)     3786 2023-04-06 15:26:56.000000 pytest-testmon-2.0.6/testmon/configure.py
+-rw-r--r--   0 poko      (1000) poko      (1000)    22226 2023-04-06 15:26:56.000000 pytest-testmon-2.0.6/testmon/db.py
+-rw-r--r--   0 poko      (1000) poko      (1000)     7867 2023-04-06 15:26:56.000000 pytest-testmon-2.0.6/testmon/process_code.py
+-rw-r--r--   0 poko      (1000) poko      (1000)    17025 2023-04-06 15:26:55.000000 pytest-testmon-2.0.6/testmon/pytest_testmon.py
+-rw-r--r--   0 poko      (1000) poko      (1000)    18896 2023-04-06 15:26:56.000000 pytest-testmon-2.0.6/testmon/testmon_core.py
+-rw-r--r--   0 poko      (1000) poko      (1000)     1232 2023-01-12 14:59:27.000000 pytest-testmon-2.0.6/testmon/tox_testmon.py
```

### Comparing `pytest-testmon-2.0.5/LICENSE` & `pytest-testmon-2.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/PKG-INFO` & `pytest-testmon-2.0.6/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytest-testmon
-Version: 2.0.5
+Version: 2.0.6
 Summary: selects tests affected by changed files and methods
 Home-page: https://testmon.org
 Author: Tibor Arpas, Tomas Matlovic
 Author-email: Tibor Arpas <tibor@testmon.org>
 License: AGPL
 Project-URL: Source, https://github.com/tarpas/pytest-testmon
 Keywords: testing,pytest,plugin
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pytest-testmon Version: 2.0.5 Summary: selects
+Metadata-Version: 2.1 Name: pytest-testmon Version: 2.0.6 Summary: selects
 tests affected by changed files and methods Home-page: https://testmon.org
 Author: Tibor Arpas, Tomas Matlovic Author-email: Tibor Arpas
 testmon.org> License: AGPL Project-URL: Source, https://github.com/tarpas/
 pytest-testmon Keywords: testing,pytest,plugin Platform: linux Platform: osx
 Platform: win32 Classifier: Development Status :: 4 - Beta Classifier: Intended
 Audience :: Developers Classifier: Operating System :: POSIX Classifier:
 Operating System :: Microsoft :: Windows Classifier: Operating System :: MacOS
```

### Comparing `pytest-testmon-2.0.5/README.md` & `pytest-testmon-2.0.6/README.md`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/pyproject.toml` & `pytest-testmon-2.0.6/pyproject.toml`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/pytest_testmon.egg-info/PKG-INFO` & `pytest-testmon-2.0.6/pytest_testmon.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pytest-testmon
-Version: 2.0.5
+Version: 2.0.6
 Summary: selects tests affected by changed files and methods
 Home-page: https://testmon.org
 Author: Tibor Arpas, Tomas Matlovic
 Author-email: Tibor Arpas <tibor@testmon.org>
 License: AGPL
 Project-URL: Source, https://github.com/tarpas/pytest-testmon
 Keywords: testing,pytest,plugin
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: pytest-testmon Version: 2.0.5 Summary: selects
+Metadata-Version: 2.1 Name: pytest-testmon Version: 2.0.6 Summary: selects
 tests affected by changed files and methods Home-page: https://testmon.org
 Author: Tibor Arpas, Tomas Matlovic Author-email: Tibor Arpas
 testmon.org> License: AGPL Project-URL: Source, https://github.com/tarpas/
 pytest-testmon Keywords: testing,pytest,plugin Platform: linux Platform: osx
 Platform: win32 Classifier: Development Status :: 4 - Beta Classifier: Intended
 Audience :: Developers Classifier: Operating System :: POSIX Classifier:
 Operating System :: Microsoft :: Windows Classifier: Operating System :: MacOS
```

### Comparing `pytest-testmon-2.0.5/setup.cfg` & `pytest-testmon-2.0.6/setup.cfg`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/testmon/configure.py` & `pytest-testmon-2.0.6/testmon/configure.py`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/testmon/db.py` & `pytest-testmon-2.0.6/testmon/db.py`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/testmon/process_code.py` & `pytest-testmon-2.0.6/testmon/process_code.py`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/testmon/pytest_testmon.py` & `pytest-testmon-2.0.6/testmon/pytest_testmon.py`

 * *Files identical despite different names*

### Comparing `pytest-testmon-2.0.5/testmon/testmon_core.py` & `pytest-testmon-2.0.6/testmon/testmon_core.py`

 * *Files 0% similar despite different names*

```diff
@@ -155,15 +155,15 @@
 
         try:
             git_head_sha = None
             try:
                 git_head_sha = (
                     check_output(["git", "rev-parse", "HEAD"]).decode("ascii").strip()
                 )
-            except CalledProcessError:
+            except (CalledProcessError, FileNotFoundError):
                 pass
             result = self.db.initiate_execution(
                 self.environment,
                 system_packages,
                 python_version,
                 {
                     "tm_client_version": TM_CLIENT_VERSION,
```

### Comparing `pytest-testmon-2.0.5/testmon/tox_testmon.py` & `pytest-testmon-2.0.6/testmon/tox_testmon.py`

 * *Files identical despite different names*

