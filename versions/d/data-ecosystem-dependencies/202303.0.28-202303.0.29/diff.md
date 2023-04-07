# Comparing `tmp/data_ecosystem_dependencies-202303.0.28.tar.gz` & `tmp/data_ecosystem_dependencies-202303.0.29.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_ecosystem_dependencies-202303.0.28.tar", max compression
+gzip compressed data, was "data_ecosystem_dependencies-202303.0.29.tar", max compression
```

## Comparing `data_ecosystem_dependencies-202303.0.28.tar` & `data_ecosystem_dependencies-202303.0.29.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0      842 2023-04-07 02:25:43.526424 data_ecosystem_dependencies-202303.0.28/data_ecosystem_dependencies/__init__.py
--rw-r--r--   0        0        0    11357 2023-04-07 02:25:43.526424 data_ecosystem_dependencies-202303.0.28/license.md
--rw-r--r--   0        0        0     2542 2023-04-07 02:30:05.109447 data_ecosystem_dependencies-202303.0.28/pyproject.toml
--rw-r--r--   0        0        0      341 2023-04-07 02:25:43.526424 data_ecosystem_dependencies-202303.0.28/readme.md
--rw-r--r--   0        0        0      160 2023-04-07 02:25:43.526424 data_ecosystem_dependencies-202303.0.28/setup.cfg
--rw-r--r--   0        0        0     3051 1970-01-01 00:00:00.000000 data_ecosystem_dependencies-202303.0.28/PKG-INFO
+-rw-r--r--   0        0        0      842 2023-04-07 03:45:02.633220 data_ecosystem_dependencies-202303.0.29/data_ecosystem_dependencies/__init__.py
+-rw-r--r--   0        0        0    11357 2023-04-07 03:45:02.633220 data_ecosystem_dependencies-202303.0.29/license.md
+-rw-r--r--   0        0        0     2542 2023-04-07 03:48:37.658480 data_ecosystem_dependencies-202303.0.29/pyproject.toml
+-rw-r--r--   0        0        0      341 2023-04-07 03:45:02.633220 data_ecosystem_dependencies-202303.0.29/readme.md
+-rw-r--r--   0        0        0      160 2023-04-07 03:45:02.633220 data_ecosystem_dependencies-202303.0.29/setup.cfg
+-rw-r--r--   0        0        0     3051 1970-01-01 00:00:00.000000 data_ecosystem_dependencies-202303.0.29/PKG-INFO
```

### Comparing `data_ecosystem_dependencies-202303.0.28/data_ecosystem_dependencies/__init__.py` & `data_ecosystem_dependencies-202303.0.29/data_ecosystem_dependencies/__init__.py`

 * *Files identical despite different names*

### Comparing `data_ecosystem_dependencies-202303.0.28/license.md` & `data_ecosystem_dependencies-202303.0.29/license.md`

 * *Files identical despite different names*

### Comparing `data_ecosystem_dependencies-202303.0.28/pyproject.toml` & `data_ecosystem_dependencies-202303.0.29/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name="data_ecosystem_dependencies"
-version="202303.0.28"
+version="202303.0.29"
 description="Data Ecosystem  Dependencies - Python (PADE)"
 authors=["John Bowyer <zfi4@cdc.gov>"]
 readme = "readme.md"
 license="Apache"
 homepage="https://github.com/cdcent/data_ecosystem_services"
 repository="https://github.com/cdcent/data_ecosystem_services"
 classifiers=[
```

### Comparing `data_ecosystem_dependencies-202303.0.28/PKG-INFO` & `data_ecosystem_dependencies-202303.0.29/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data-ecosystem-dependencies
-Version: 202303.0.28
+Version: 202303.0.29
 Summary: Data Ecosystem  Dependencies - Python (PADE)
 Home-page: https://github.com/cdcent/data_ecosystem_services
 License: Apache
 Author: John Bowyer
 Author-email: zfi4@cdc.gov
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 4 - Beta
```

