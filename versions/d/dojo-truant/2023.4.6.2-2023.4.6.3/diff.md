# Comparing `tmp/dojo_truant-2023.4.6.2.tar.gz` & `tmp/dojo_truant-2023.4.6.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dojo_truant-2023.4.6.2.tar", last modified: Fri Apr  7 05:11:42 2023, max compression
+gzip compressed data, was "dojo_truant-2023.4.6.3.tar", last modified: Fri Apr  7 05:25:07 2023, max compression
```

## Comparing `dojo_truant-2023.4.6.2.tar` & `dojo_truant-2023.4.6.3.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:11:42.074000 dojo_truant-2023.4.6.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1469 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-07 05:11:42.070001 dojo_truant-2023.4.6.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:11:42.070001 dojo_truant-2023.4.6.2/dojo/
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11207 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/api.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/api_multi.py
--rw-r--r--   0 runner    (1001) docker     (123)      933 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/dojo_group.py
--rw-r--r--   0 runner    (1001) docker     (123)     3194 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/product.py
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/product_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     2366 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/dojo/write_chain.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:11:42.070001 dojo_truant-2023.4.6.2/dojo_truant.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-07 05:11:42.000000 dojo_truant-2023.4.6.2/dojo_truant.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-04-07 05:11:42.000000 dojo_truant-2023.4.6.2/dojo_truant.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 05:11:42.000000 dojo_truant-2023.4.6.2/dojo_truant.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 05:11:42.000000 dojo_truant-2023.4.6.2/dojo_truant.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-07 05:11:42.000000 dojo_truant-2023.4.6.2/dojo_truant.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      613 2023-04-07 05:11:27.000000 dojo_truant-2023.4.6.2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 05:11:42.074000 dojo_truant-2023.4.6.2/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:25:07.833753 dojo_truant-2023.4.6.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1469 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-07 05:25:07.833753 dojo_truant-2023.4.6.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:25:07.833753 dojo_truant-2023.4.6.3/dojo/
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11207 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/api_multi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      933 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/dojo_group.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3194 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/product.py
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/product_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2367 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/dojo/write_chain.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 05:25:07.833753 dojo_truant-2023.4.6.3/dojo_truant.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-07 05:25:07.000000 dojo_truant-2023.4.6.3/dojo_truant.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-04-07 05:25:07.000000 dojo_truant-2023.4.6.3/dojo_truant.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 05:25:07.000000 dojo_truant-2023.4.6.3/dojo_truant.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 05:25:07.000000 dojo_truant-2023.4.6.3/dojo_truant.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-07 05:25:07.000000 dojo_truant-2023.4.6.3/dojo_truant.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      613 2023-04-07 05:24:53.000000 dojo_truant-2023.4.6.3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 05:25:07.833753 dojo_truant-2023.4.6.3/setup.cfg
```

### Comparing `dojo_truant-2023.4.6.2/LICENSE.txt` & `dojo_truant-2023.4.6.3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `dojo_truant-2023.4.6.2/PKG-INFO` & `dojo_truant-2023.4.6.3/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dojo_truant
-Version: 2023.4.6.2
+Version: 2023.4.6.3
 Summary: A minimal client for deject dojo to be used by me in my projects. Some functionality may be absent.
 Author-email: Chris Halbersma <chalbersma@auditboard.com>
 License: BSD-3-Clause
 Keywords: defectDojo
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.9
 Description-Content-Type: text/markdown
```

### Comparing `dojo_truant-2023.4.6.2/dojo/api.py` & `dojo_truant-2023.4.6.3/dojo/api.py`

 * *Files identical despite different names*

### Comparing `dojo_truant-2023.4.6.2/dojo/dojo_group.py` & `dojo_truant-2023.4.6.3/dojo/dojo_group.py`

 * *Files identical despite different names*

### Comparing `dojo_truant-2023.4.6.2/dojo/product.py` & `dojo_truant-2023.4.6.3/dojo/product.py`

 * *Files identical despite different names*

### Comparing `dojo_truant-2023.4.6.2/dojo/product_type.py` & `dojo_truant-2023.4.6.3/dojo/product_type.py`

 * *Files identical despite different names*

### Comparing `dojo_truant-2023.4.6.2/dojo/write_chain.py` & `dojo_truant-2023.4.6.3/dojo/write_chain.py`

 * *Files 0% similar despite different names*

```diff
@@ -34,15 +34,15 @@
     elif isinstance(data, string.Template):
         expanded_data = data.safe_substitute(**expanded_template)
     else:
         expanded_data = data
 
     return expanded_data
 
-def write_chain(chain=[], *kwargs):
+def write_chain(chain=[], **kwargs):
     '''
     Write this chain of objects
     :param chain:
     :return:
     '''
 
     logger = logging.getLogger("dojo.write_chain")
```

### Comparing `dojo_truant-2023.4.6.2/dojo_truant.egg-info/PKG-INFO` & `dojo_truant-2023.4.6.3/dojo_truant.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dojo-truant
-Version: 2023.4.6.2
+Version: 2023.4.6.3
 Summary: A minimal client for deject dojo to be used by me in my projects. Some functionality may be absent.
 Author-email: Chris Halbersma <chalbersma@auditboard.com>
 License: BSD-3-Clause
 Keywords: defectDojo
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.9
 Description-Content-Type: text/markdown
```

### Comparing `dojo_truant-2023.4.6.2/pyproject.toml` & `dojo_truant-2023.4.6.3/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -3,15 +3,15 @@
   "twine",
   "setuptools"
 ]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "dojo_truant"
-version = "2023.04.06.2"
+version = "2023.04.06.3"
 authors = [
     {name = "Chris Halbersma", email = "chalbersma@auditboard.com"},
 ]
 description = "A minimal client for deject dojo to be used by me in my projects. Some functionality may be absent."
 readme = "README.md"
 requires-python = ">=3.9"
 keywords = ["defectDojo"]
```

