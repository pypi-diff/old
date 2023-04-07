# Comparing `tmp/pyright_polite-1.0.1.tar.gz` & `tmp/pyright_polite-1.0.2.tar.gz`

## Comparing `pyright_polite-1.0.1.tar` & `pyright_polite-1.0.2.tar`

### file list

```diff
@@ -1,27 +1,18 @@
--rw-r--r--   0        0        0      998 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.justfile
--rw-r--r--   0        0        0     1151 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.pre-commit-config.yaml
--rw-r--r--   0        0        0       96 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.pylintrc
--rw-r--r--   0        0        0      176 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/CHANGELOG.md
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/setup.cfg
--rw-r--r--   0        0        0      119 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.github/dependabot.yml
--rw-r--r--   0        0        0     3792 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.github/workflows/ci.yml
--rw-r--r--   0        0        0     2189 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.github/workflows/publish.yml
--rw-r--r--   0        0        0      154 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/__about__.py
--rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/__init__.py
--rw-r--r--   0        0        0     8832 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/cli.py
--rw-r--r--   0        0        0      858 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/main.py
--rw-r--r--   0        0        0     1525 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/platform.py
--rw-r--r--   0        0        0     9766 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/polite.py
--rw-r--r--   0        0        0     8914 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/src/pyright_polite/pyright.py
--rw-r--r--   0        0        0    22498 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/tests/conftest.py
--rw-r--r--   0        0        0     4106 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/tests/test_cli.py
--rw-r--r--   0        0        0     1360 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/tests/test_main.py
--rw-r--r--   0        0        0     5130 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/tests/test_polite.py
--rw-r--r--   0        0        0     2035 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/tests/test_processlookuperror.py
--rw-r--r--   0        0        0     1982 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/tests/test_traceback.py
--rw-r--r--   0        0        0     3097 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/.gitignore
--rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/LICENSE
--rw-r--r--   0        0        0     6026 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/README.md
--rw-r--r--   0        0        0     1245 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/hatch.toml
--rw-r--r--   0        0        0     2745 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/pyproject.toml
--rw-r--r--   0        0        0     7209 2020-02-02 00:00:00.000000 pyright_polite-1.0.1/PKG-INFO
+-rw-r--r--   0        0        0      998 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/.justfile
+-rw-r--r--   0        0        0     1151 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/.pre-commit-config.yaml
+-rw-r--r--   0        0        0       96 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/.pylintrc
+-rw-r--r--   0        0        0      291 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/CHANGELOG.md
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/setup.cfg
+-rw-r--r--   0        0        0      154 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/__about__.py
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/__init__.py
+-rw-r--r--   0        0        0     8832 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/cli.py
+-rw-r--r--   0        0        0      858 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/main.py
+-rw-r--r--   0        0        0     1525 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/platform.py
+-rw-r--r--   0        0        0     9766 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/polite.py
+-rw-r--r--   0        0        0     8914 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/src/pyright_polite/pyright.py
+-rw-r--r--   0        0        0     5146 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/.gitignore
+-rw-r--r--   0        0        0     1074 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/LICENSE
+-rw-r--r--   0        0        0     6026 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/README.md
+-rw-r--r--   0        0        0     1392 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/hatch.toml
+-rw-r--r--   0        0        0     2785 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/pyproject.toml
+-rw-r--r--   0        0        0     7209 2020-02-02 00:00:00.000000 pyright_polite-1.0.2/PKG-INFO
```

### Comparing `pyright_polite-1.0.1/.justfile` & `pyright_polite-1.0.2/.justfile`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/.pre-commit-config.yaml` & `pyright_polite-1.0.2/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/src/pyright_polite/cli.py` & `pyright_polite-1.0.2/src/pyright_polite/cli.py`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/src/pyright_polite/main.py` & `pyright_polite-1.0.2/src/pyright_polite/main.py`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/src/pyright_polite/platform.py` & `pyright_polite-1.0.2/src/pyright_polite/platform.py`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/src/pyright_polite/polite.py` & `pyright_polite-1.0.2/src/pyright_polite/polite.py`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/src/pyright_polite/pyright.py` & `pyright_polite-1.0.2/src/pyright_polite/pyright.py`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/LICENSE` & `pyright_polite-1.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pyright_polite-1.0.1/README.md` & `pyright_polite-1.0.2/README.md`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -55,29 +55,29 @@
 Searching for source files
 Found 7 source files
 pyright 1.1.300
 0 errors, 0 warnings, 0 informations
 Completed in 1.006sec
 ```
 
-Error messages are still shown (eg, if your config file is invalid).
-
 Now pyright is just as polite as your other tools:
 
 ```console
 $ hatch run lint
 cmd [1] | - ruff check .
 cmd [2] | - black --quiet --check --diff .
 cmd [3] | - pyright-polite
 Found 8 source files
 0 errors, 0 warnings, 0 informations
 cmd [4] | - ssort --check --diff .
 8 files would be left unchanged
 ```
 
+Error messages are still shown (eg, if your config file is invalid).
+
 ## Installation
 
 You need `pyright` installed (ie, available somewhere in your `PATH`).
 
 See pyright's installation instructions [here][installation]. Usually people install
 either the [pyright npm][pkg_npm] or the [pyright PyPI][pkg_pypi] package.
```

### Comparing `pyright_polite-1.0.1/pyproject.toml` & `pyright_polite-1.0.2/pyproject.toml`

 * *Files 3% similar despite different names*

```diff
@@ -86,14 +86,15 @@
 pydocstyle.convention = "google"
 select = [
   "A", "ARG", "B", "BLE", "C", "C4", "C90", "COM", "D", "DTZ", "E", "EXE", "F", "FBT",
   "G", "I", "INP", "ISC", "N", "PIE", "PT", "PTH", "PYI", "RET", "RSE", "RUF", "S",
   "SIM", "SLF", "T10", "T20", "TCH", "TRY", "W", "YTT"
 ]
 ignore = [ "COM812", "TRY003" ]
+exclude = [ "tests/test_integration/" ]
 [tool.ruff.per-file-ignores]
 "__init__.py" = ["F401"]
 "tests/conftest.py" = ["PT004"]
 "tests/*" = ["D", "E501", "FBT", "INP001", "RUF001", "RUF002", "RUF003", "S", "SIM117"]
 [tool.ruff.mccabe]
 max-complexity = 10
```

### Comparing `pyright_polite-1.0.1/PKG-INFO` & `pyright_polite-1.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyright-polite
-Version: 1.0.1
+Version: 1.0.2
 Summary: An intelligent cross-platform wrapper for pyright that makes it less noisy.
 Project-URL: Homepage, https://github.com/jamielinux/pyright-polite
 Project-URL: Issues, https://github.com/jamielinux/pyright-polite/issues
 Project-URL: Source, https://github.com/jamielinux/pyright-polite
 Author-email: Jamie Nguyen <j@jamielinux.com>
 License-Expression: MIT
 License-File: LICENSE
@@ -82,29 +82,29 @@
 Searching for source files
 Found 7 source files
 pyright 1.1.300
 0 errors, 0 warnings, 0 informations
 Completed in 1.006sec
 ```
 
-Error messages are still shown (eg, if your config file is invalid).
-
 Now pyright is just as polite as your other tools:
 
 ```console
 $ hatch run lint
 cmd [1] | - ruff check .
 cmd [2] | - black --quiet --check --diff .
 cmd [3] | - pyright-polite
 Found 8 source files
 0 errors, 0 warnings, 0 informations
 cmd [4] | - ssort --check --diff .
 8 files would be left unchanged
 ```
 
+Error messages are still shown (eg, if your config file is invalid).
+
 ## Installation
 
 You need `pyright` installed (ie, available somewhere in your `PATH`).
 
 See pyright's installation instructions [here][installation]. Usually people install
 either the [pyright npm][pkg_npm] or the [pyright PyPI][pkg_pypi] package.
```

