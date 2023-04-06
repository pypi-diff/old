# Comparing `tmp/pspsmgen-0.0.1.tar.gz` & `tmp/pspsmgen-0.0.2.tar.gz`

## Comparing `pspsmgen-0.0.1.tar` & `pspsmgen-0.0.2.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/__init__.py
--rw-r--r--   0        0        0    57581 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/psgen.py
--rw-r--r--   0        0        0       18 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/requirements.txt
--rw-r--r--   0        0        0     1187 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/setup.py
--rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/LICENSE.txt
--rw-r--r--   0        0        0      200 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/README.md
--rw-r--r--   0        0        0      577 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/pyproject.toml
--rw-r--r--   0        0        0      694 2020-02-02 00:00:00.000000 pspsmgen-0.0.1/PKG-INFO
+-rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/__init__.py
+-rw-r--r--   0        0        0    57581 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/pspsmgen.py
+-rw-r--r--   0        0        0       18 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/requirements.txt
+-rw-r--r--   0        0        0     1187 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/setup.py
+-rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/LICENSE.txt
+-rw-r--r--   0        0        0      602 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/README.md
+-rw-r--r--   0        0        0      577 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/pyproject.toml
+-rw-r--r--   0        0        0     1085 2020-02-02 00:00:00.000000 pspsmgen-0.0.2/PKG-INFO
```

### Comparing `pspsmgen-0.0.1/psgen.py` & `pspsmgen-0.0.2/pspsmgen.py`

 * *Files identical despite different names*

### Comparing `pspsmgen-0.0.1/setup.py` & `pspsmgen-0.0.2/setup.py`

 * *Files identical despite different names*

### Comparing `pspsmgen-0.0.1/LICENSE.txt` & `pspsmgen-0.0.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pspsmgen-0.0.1/pyproject.toml` & `pspsmgen-0.0.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 [project]
 name = "pspsmgen"
-version = "0.0.1"
+version = "0.0.2"
 authors = [
   { name="ronaldohj", email="ronaldohj@hotmail.com" },
 ]
 description = "Pspsmgen is a 3d pore-scale Pre-Salt model generator to simulate	petrophysical properties."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

