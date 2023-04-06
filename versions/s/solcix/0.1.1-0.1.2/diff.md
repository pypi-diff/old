# Comparing `tmp/solcix-0.1.1.tar.gz` & `tmp/solcix-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "solcix-0.1.1.tar", max compression
+gzip compressed data, was "solcix-0.1.2.tar", max compression
```

## Comparing `solcix-0.1.1.tar` & `solcix-0.1.2.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0     5104 2023-04-06 11:59:09.004164 solcix-0.1.1/README.md
--rw-r--r--   0        0        0      934 2023-04-06 13:02:02.602566 solcix-0.1.1/pyproject.toml
--rw-r--r--   0        0        0     1103 2023-04-06 08:51:29.868152 solcix-0.1.1/solcix/__init__.py
--rw-r--r--   0        0        0     6469 2023-04-06 12:57:41.589225 solcix-0.1.1/solcix/__main__.py
--rw-r--r--   0        0        0       22 2023-04-06 13:01:57.070536 solcix-0.1.1/solcix/__version__.py
--rw-r--r--   0        0        0      182 2023-04-06 06:47:58.651981 solcix-0.1.1/solcix/compile/__init__.py
--rw-r--r--   0        0        0    19134 2023-04-06 09:25:41.021963 solcix-0.1.1/solcix/compile/solc.py
--rw-r--r--   0        0        0      618 2023-04-05 16:12:30.242253 solcix-0.1.1/solcix/constant.py
--rw-r--r--   0        0        0      110 2023-04-05 14:24:43.655338 solcix-0.1.1/solcix/datatypes/__init__.py
--rw-r--r--   0        0        0     3949 2023-04-06 08:39:27.233614 solcix-0.1.1/solcix/datatypes/datatypes.py
--rw-r--r--   0        0        0     3407 2023-04-06 08:32:26.769062 solcix-0.1.1/solcix/errors.py
--rw-r--r--   0        0        0    19449 2023-04-06 11:09:01.513052 solcix-0.1.1/solcix/installer.py
--rw-r--r--   0        0        0      247 2023-04-05 17:30:43.390279 solcix-0.1.1/solcix/manage/__init__.py
--rw-r--r--   0        0        0     4791 2023-04-06 12:52:31.048054 solcix-0.1.1/solcix/manage/manage.py
--rw-r--r--   0        0        0    10403 2023-04-05 18:06:59.201642 solcix-0.1.1/solcix/resolver.py
--rw-r--r--   0        0        0      597 2023-04-06 08:38:41.565504 solcix-0.1.1/solcix/utils.py
--rw-r--r--   0        0        0     6310 1970-01-01 00:00:00.000000 solcix-0.1.1/PKG-INFO
+-rw-r--r--   0        0        0     5104 2023-04-06 11:59:09.004164 solcix-0.1.2/README.md
+-rw-r--r--   0        0        0      935 2023-04-06 13:08:08.136419 solcix-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0     1103 2023-04-06 08:51:29.868152 solcix-0.1.2/solcix/__init__.py
+-rw-r--r--   0        0        0     6469 2023-04-06 12:57:41.589225 solcix-0.1.2/solcix/__main__.py
+-rw-r--r--   0        0        0       22 2023-04-06 13:06:39.195988 solcix-0.1.2/solcix/__version__.py
+-rw-r--r--   0        0        0      182 2023-04-06 06:47:58.651981 solcix-0.1.2/solcix/compile/__init__.py
+-rw-r--r--   0        0        0    19134 2023-04-06 09:25:41.021963 solcix-0.1.2/solcix/compile/solc.py
+-rw-r--r--   0        0        0      618 2023-04-05 16:12:30.242253 solcix-0.1.2/solcix/constant.py
+-rw-r--r--   0        0        0      110 2023-04-05 14:24:43.655338 solcix-0.1.2/solcix/datatypes/__init__.py
+-rw-r--r--   0        0        0     3949 2023-04-06 08:39:27.233614 solcix-0.1.2/solcix/datatypes/datatypes.py
+-rw-r--r--   0        0        0     3407 2023-04-06 08:32:26.769062 solcix-0.1.2/solcix/errors.py
+-rw-r--r--   0        0        0    19449 2023-04-06 11:09:01.513052 solcix-0.1.2/solcix/installer.py
+-rw-r--r--   0        0        0      247 2023-04-05 17:30:43.390279 solcix-0.1.2/solcix/manage/__init__.py
+-rw-r--r--   0        0        0     4799 2023-04-06 13:03:26.451012 solcix-0.1.2/solcix/manage/manage.py
+-rw-r--r--   0        0        0    10403 2023-04-05 18:06:59.201642 solcix-0.1.2/solcix/resolver.py
+-rw-r--r--   0        0        0      597 2023-04-06 08:38:41.565504 solcix-0.1.2/solcix/utils.py
+-rw-r--r--   0        0        0     6310 1970-01-01 00:00:00.000000 solcix-0.1.2/PKG-INFO
```

### Comparing `solcix-0.1.1/README.md` & `solcix-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/pyproject.toml` & `solcix-0.1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "solcix"
-version = "0.1.1"
+version = "0.1.2"
 description = "A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts."
 authors = ["alan890104 <alan890104@gmail.com>"]
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = "^3.8"
 cfgv = "3.3.1"
@@ -25,15 +25,15 @@
 virtualenv = "20.21.0"
 pytest-mock = "^3.10.0"
 colorama = "^0.4.6"
 pyfiglet = "^0.8.post1"
 
 [tool.poetry.group.dev.dependencies]
 black = "23.3.0"
-pre-commit = "3.2.2"
+pre-commit = "^3.2.2"
 pytest-cov = "^4.0.0"
 pytest = "^7.2.2"
 
 [tool.poetry.scripts]
 solcix = "solcix.__main__:cli"
 solc = "solcix.__main__:solc"
```

### Comparing `solcix-0.1.1/solcix/__init__.py` & `solcix-0.1.2/solcix/__init__.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/__main__.py` & `solcix-0.1.2/solcix/__main__.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/compile/solc.py` & `solcix-0.1.2/solcix/compile/solc.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/constant.py` & `solcix-0.1.2/solcix/constant.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/datatypes/datatypes.py` & `solcix-0.1.2/solcix/datatypes/datatypes.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/errors.py` & `solcix-0.1.2/solcix/errors.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/installer.py` & `solcix-0.1.2/solcix/installer.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/manage/manage.py` & `solcix-0.1.2/solcix/manage/manage.py`

 * *Files 4% similar despite different names*

```diff
@@ -33,15 +33,15 @@
         source = source_path.as_posix()
 
         if source_path.is_file():
             with open(source_path, encoding="utf-8") as f:
                 version = f.read()
         else:
             raise NotInstalledError(
-                "💫 No solc version set. Run `solcix global VERSION`, `solcix local Version` or set SOLC_VERSION environment variable. 💫"
+                "💫 No solc version set. Run `solcix use global VERSION`, `solcix use local Version` or set SOLC_VERSION environment variable. 💫"
             )
 
     versions: List[str] = get_installed_versions()
 
     if version not in versions:
         raise NotInstalledError(
             f"\n😱 Version '{version}' not installed (set by {source}). 😱"
```

### Comparing `solcix-0.1.1/solcix/resolver.py` & `solcix-0.1.2/solcix/resolver.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/solcix/utils.py` & `solcix-0.1.2/solcix/utils.py`

 * *Files identical despite different names*

### Comparing `solcix-0.1.1/PKG-INFO` & `solcix-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: solcix
-Version: 0.1.1
+Version: 0.1.2
 Summary: A Python wrapper for the Solidity compiler. Switch between versions, compile, and manage artifacts.
 Author: alan890104
 Author-email: alan890104@gmail.com
 Requires-Python: >=3.8,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

