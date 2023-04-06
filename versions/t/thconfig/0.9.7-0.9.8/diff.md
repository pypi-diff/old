# Comparing `tmp/thconfig-0.9.7.tar.gz` & `tmp/thconfig-0.9.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "thconfig-0.9.7.tar", max compression
+gzip compressed data, was "thconfig-0.9.8.tar", max compression
```

## Comparing `thconfig-0.9.7.tar` & `thconfig-0.9.8.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0     1497 2023-04-06 13:17:58.138151 thconfig-0.9.7/LICENSE
--rw-r--r--   0        0        0     5912 2023-04-06 13:17:58.138151 thconfig-0.9.7/README.md
--rw-r--r--   0        0        0     1181 2023-04-06 13:17:58.139151 thconfig-0.9.7/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/__init__.py
--rw-r--r--   0        0        0      759 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/config.py
--rw-r--r--   0        0        0      245 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/error.py
--rw-r--r--   0        0        0       27 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/file/__init__.py
--rw-r--r--   0        0        0     2968 2023-04-06 13:17:58.140151 thconfig-0.9.7/thconfig/file/file_config.py
--rw-r--r--   0        0        0      168 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/__init__.py
--rw-r--r--   0        0        0     6799 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/couch_config.py
--rw-r--r--   0        0        0     2153 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/etcd_config.py
--rw-r--r--   0        0        0       98 2023-04-06 13:17:58.141151 thconfig-0.9.7/thconfig/http/http_config.py
--rw-r--r--   0        0        0     7159 1970-01-01 00:00:00.000000 thconfig-0.9.7/PKG-INFO
+-rw-r--r--   0        0        0     1497 2023-04-06 13:44:48.180362 thconfig-0.9.8/LICENSE
+-rw-r--r--   0        0        0     5912 2023-04-06 13:44:48.180362 thconfig-0.9.8/README.md
+-rw-r--r--   0        0        0     1223 2023-04-06 13:44:48.181362 thconfig-0.9.8/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/__init__.py
+-rw-r--r--   0        0        0      759 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/config.py
+-rw-r--r--   0        0        0      245 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/error.py
+-rw-r--r--   0        0        0       27 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/file/__init__.py
+-rw-r--r--   0        0        0     2968 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/file/file_config.py
+-rw-r--r--   0        0        0      168 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/http/__init__.py
+-rw-r--r--   0        0        0     6799 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/http/couch_config.py
+-rw-r--r--   0        0        0     2153 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/http/etcd_config.py
+-rw-r--r--   0        0        0       98 2023-04-06 13:44:48.182362 thconfig-0.9.8/thconfig/http/http_config.py
+-rw-r--r--   0        0        0     7141 1970-01-01 00:00:00.000000 thconfig-0.9.8/PKG-INFO
```

### Comparing `thconfig-0.9.7/LICENSE` & `thconfig-0.9.8/LICENSE`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.7/README.md` & `thconfig-0.9.8/README.md`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.7/pyproject.toml` & `thconfig-0.9.8/pyproject.toml`

 * *Files 15% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # Refference: https://python-poetry.org/docs/pyproject/
 [tool.poetry]
 name = "thconfig"
-version = "0.9.7"
+version = "0.9.8"
 description = "TangledHub Config reader/writter"
 license = "BSD 3-clause"
 authors = ["TangledHub <info@tangledgroup.com>"]
 readme = "README.md"
 repository = "https://gitlab.com/tangledlabs/thconfig"
 keywords = ["tangled", "tangledhub", "tangledlabs", "thconfig"]
 # Classifiers reference: https://pypi.org/classifiers/
@@ -24,15 +24,18 @@
 [tool.poetry.dependencies]
 python = "^3.10"
 thresult = "^0.9.25"
 aiohttp = "^3.8.3"
 toml = "^0.10.2"
 json5 = "^0.9.10"
 PyYAML = "^6.0"
-aetcd = "^1.0.0a2"
+# aetcd = "^1.0.0a2"
+
+[tool.poetry.extras]
+aetcd = ["aetcd"]
 
 [tool.poetry.dev-dependencies]
 #pytest = "^6.2.5"
 #coverage ="^6.2"
 
 #[tool.poetry.scripts]
```

### Comparing `thconfig-0.9.7/thconfig/config.py` & `thconfig-0.9.8/thconfig/config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.7/thconfig/file/file_config.py` & `thconfig-0.9.8/thconfig/file/file_config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.7/thconfig/http/couch_config.py` & `thconfig-0.9.8/thconfig/http/couch_config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.7/thconfig/http/etcd_config.py` & `thconfig-0.9.8/thconfig/http/etcd_config.py`

 * *Files identical despite different names*

### Comparing `thconfig-0.9.7/PKG-INFO` & `thconfig-0.9.8/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: thconfig
-Version: 0.9.7
+Version: 0.9.8
 Summary: TangledHub Config reader/writter
 Home-page: https://gitlab.com/tangledlabs/thconfig
 License: BSD 3-clause
 Keywords: tangled,tangledhub,tangledlabs,thconfig
 Author: TangledHub
 Author-email: info@tangledgroup.com
 Requires-Python: >=3.10,<4.0
@@ -16,16 +16,16 @@
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Provides-Extra: aetcd
 Requires-Dist: PyYAML (>=6.0,<7.0)
-Requires-Dist: aetcd (>=1.0.0a2,<2.0.0)
 Requires-Dist: aiohttp (>=3.8.3,<4.0.0)
 Requires-Dist: json5 (>=0.9.10,<0.10.0)
 Requires-Dist: thresult (>=0.9.25,<0.10.0)
 Requires-Dist: toml (>=0.10.2,<0.11.0)
 Project-URL: Repository, https://gitlab.com/tangledlabs/thconfig
 Description-Content-Type: text/markdown
```

