# Comparing `tmp/nomnomdata-engine-1.1.8.post6.dev0.tar.gz` & `tmp/nomnomdata-engine-1.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nomnomdata-engine-1.1.8.post6.dev0.tar", max compression
+gzip compressed data, was "nomnomdata-engine-1.1.9.tar", max compression
```

## Comparing `nomnomdata-engine-1.1.8.post6.dev0.tar` & `nomnomdata-engine-1.1.9.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0      702 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/LICENSE
--rw-r--r--   0        0        0       40 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/README.md
--rw-r--r--   0        0        0      432 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/__init__.py
--rw-r--r--   0        0        0     9869 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/components.py
--rw-r--r--   0        0        0    30556 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/connections.py
--rw-r--r--   0        0        0     5426 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/encoders.py
--rw-r--r--   0        0        0    14368 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/engine.py
--rw-r--r--   0        0        0      516 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/errors.py
--rw-r--r--   0        0        0      290 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/globals.py
--rw-r--r--   0        0        0     2448 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/logging.py
--rw-r--r--   0        0        0    11023 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/nominode.py
--rw-r--r--   0        0        0     9574 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/parameters.py
--rw-r--r--   0        0        0    15475 2021-03-23 15:20:29.842223 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/shared_configs.py
--rw-r--r--   0        0        0     4357 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/testing.py
--rw-r--r--   0        0        0      162 2021-03-23 15:11:12.975634 nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/util.py
--rw-r--r--   0        0        0     1280 2021-03-23 15:23:45.650622 nomnomdata-engine-1.1.8.post6.dev0/pyproject.toml
--rw-r--r--   0        0        0      918 2021-03-23 15:23:46.914777 nomnomdata-engine-1.1.8.post6.dev0/setup.py
--rw-r--r--   0        0        0     1006 2021-03-23 15:23:46.915062 nomnomdata-engine-1.1.8.post6.dev0/PKG-INFO
+-rw-r--r--   0        0        0      702 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/LICENSE
+-rw-r--r--   0        0        0       40 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/README.md
+-rw-r--r--   0        0        0      432 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/__init__.py
+-rw-r--r--   0        0        0     9869 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/components.py
+-rw-r--r--   0        0        0    30556 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/connections.py
+-rw-r--r--   0        0        0     5426 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/encoders.py
+-rw-r--r--   0        0        0    14368 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/engine.py
+-rw-r--r--   0        0        0      516 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/errors.py
+-rw-r--r--   0        0        0      290 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/globals.py
+-rw-r--r--   0        0        0     2448 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/logging.py
+-rw-r--r--   0        0        0    11023 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/nominode.py
+-rw-r--r--   0        0        0     9574 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/parameters.py
+-rw-r--r--   0        0        0    15475 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/shared_configs.py
+-rw-r--r--   0        0        0     4357 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/testing.py
+-rw-r--r--   0        0        0      162 2021-03-23 15:35:19.464848 nomnomdata-engine-1.1.9/nomnomdata/engine/util.py
+-rw-r--r--   0        0        0     1269 2021-03-23 15:35:41.196843 nomnomdata-engine-1.1.9/pyproject.toml
+-rw-r--r--   0        0        0      907 2021-03-23 15:35:42.349421 nomnomdata-engine-1.1.9/setup.py
+-rw-r--r--   0        0        0      995 2021-03-23 15:35:42.349753 nomnomdata-engine-1.1.9/PKG-INFO
```

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/LICENSE` & `nomnomdata-engine-1.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/components.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/components.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/connections.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/connections.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/encoders.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/encoders.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/engine.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/engine.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/errors.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/errors.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/logging.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/logging.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/nominode.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/nominode.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/parameters.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/parameters.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/shared_configs.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/shared_configs.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/nomnomdata/engine/testing.py` & `nomnomdata-engine-1.1.9/nomnomdata/engine/testing.py`

 * *Files identical despite different names*

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/pyproject.toml` & `nomnomdata-engine-1.1.9/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 license = "LGPL-3.0-only"
 name = "nomnomdata-engine"
 packages = [
   {include = "nomnomdata"},
 ]
 readme = "README.md"
 repository = "https://gitlab.com/nomnomdata/tools/nomnomdata-engine"
-version = "1.1.8.post6.dev0"
+version = "1.1.9"
 
 [tool.poetry.dependencies]
 dunamai = "^1.1.0"
 httmock = "^1.3.0"
 nomnomdata-cli = "^0.1.7"
 python = "^3.7"
 pyyaml = "^5.3.1"
```

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/setup.py` & `nomnomdata-engine-1.1.9/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -13,15 +13,15 @@
  'nomnomdata-cli>=0.1.7,<0.2.0',
  'pyyaml>=5.3.1,<6.0.0',
  'requests>=2.23.0,<3.0.0',
  'wrapt>=1.12.1,<2.0.0']
 
 setup_kwargs = {
     'name': 'nomnomdata-engine',
-    'version': '1.1.8.post6.dev0',
+    'version': '1.1.9',
     'description': 'Package containing tooling for developing nominode engines',
     'long_description': 'Package for developing nominode engines\n',
     'author': 'Nom Nom Data Inc',
     'author_email': 'info@nomnomdata.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://gitlab.com/nomnomdata/tools/nomnomdata-engine',
```

### Comparing `nomnomdata-engine-1.1.8.post6.dev0/PKG-INFO` & `nomnomdata-engine-1.1.9/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nomnomdata-engine
-Version: 1.1.8.post6.dev0
+Version: 1.1.9
 Summary: Package containing tooling for developing nominode engines
 Home-page: https://gitlab.com/nomnomdata/tools/nomnomdata-engine
 License: LGPL-3.0-only
 Author: Nom Nom Data Inc
 Author-email: info@nomnomdata.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
```

