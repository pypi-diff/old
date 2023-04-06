# Comparing `tmp/mypy-boto3-1.26.98.tar.gz` & `tmp/mypy-boto3-1.26.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mypy-boto3-1.26.98.tar", last modified: Thu Mar 23 19:33:04 2023, max compression
+gzip compressed data, was "mypy-boto3-1.26.99.tar", last modified: Fri Mar 24 19:32:25 2023, max compression
```

## Comparing `mypy-boto3-1.26.98.tar` & `mypy-boto3-1.26.99.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 19:33:04.411627 mypy-boto3-1.26.98/
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3184 2023-03-23 19:33:04.403627 mypy-boto3-1.26.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1708 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 19:33:04.403627 mypy-boto3-1.26.98/mypy_boto3/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/mypy_boto3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-23 19:31:44.000000 mypy-boto3-1.26.98/mypy_boto3/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-03-23 19:31:44.000000 mypy-boto3-1.26.98/mypy_boto3/boto3_init.py
--rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/mypy_boto3/boto3_init_stub.py
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-23 19:31:44.000000 mypy-boto3-1.26.98/mypy_boto3/boto3_session.py
--rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-03-23 19:31:44.000000 mypy-boto3-1.26.98/mypy_boto3/boto3_session_stub.py
--rw-r--r--   0 runner    (1001) docker     (123)    14127 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/mypy_boto3/main.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-23 19:31:44.000000 mypy-boto3-1.26.98/mypy_boto3/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)   103410 2023-03-23 19:31:44.000000 mypy-boto3-1.26.98/mypy_boto3/submodules.py
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/mypy_boto3/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 19:33:04.403627 mypy-boto3-1.26.98/mypy_boto3.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3184 2023-03-23 19:33:04.000000 mypy-boto3-1.26.98/mypy_boto3.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-23 19:33:04.000000 mypy-boto3-1.26.98/mypy_boto3.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-23 19:33:04.000000 mypy-boto3-1.26.98/mypy_boto3.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-23 19:33:04.000000 mypy-boto3-1.26.98/mypy_boto3.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-23 19:33:04.000000 mypy-boto3-1.26.98/mypy_boto3.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-23 19:33:04.000000 mypy-boto3-1.26.98/mypy_boto3.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-23 19:33:04.411627 mypy-boto3-1.26.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1989 2023-03-23 19:31:43.000000 mypy-boto3-1.26.98/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:25.589893 mypy-boto3-1.26.99/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3184 2023-03-24 19:32:25.589893 mypy-boto3-1.26.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1708 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:25.589893 mypy-boto3-1.26.99/mypy_boto3/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/mypy_boto3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-03-24 19:31:51.000000 mypy-boto3-1.26.99/mypy_boto3/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-03-24 19:31:51.000000 mypy-boto3-1.26.99/mypy_boto3/boto3_init.py
+-rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/mypy_boto3/boto3_init_stub.py
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-24 19:31:51.000000 mypy-boto3-1.26.99/mypy_boto3/boto3_session.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1136 2023-03-24 19:31:51.000000 mypy-boto3-1.26.99/mypy_boto3/boto3_session_stub.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14127 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/mypy_boto3/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 19:31:51.000000 mypy-boto3-1.26.99/mypy_boto3/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)   103410 2023-03-24 19:31:51.000000 mypy-boto3-1.26.99/mypy_boto3/submodules.py
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/mypy_boto3/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 19:32:25.589893 mypy-boto3-1.26.99/mypy_boto3.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3184 2023-03-24 19:32:25.000000 mypy-boto3-1.26.99/mypy_boto3.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-24 19:32:25.000000 mypy-boto3-1.26.99/mypy_boto3.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 19:32:25.000000 mypy-boto3-1.26.99/mypy_boto3.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 19:32:25.000000 mypy-boto3-1.26.99/mypy_boto3.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-03-24 19:32:25.000000 mypy-boto3-1.26.99/mypy_boto3.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-03-24 19:32:25.000000 mypy-boto3-1.26.99/mypy_boto3.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 19:32:25.589893 mypy-boto3-1.26.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1989 2023-03-24 19:31:49.000000 mypy-boto3-1.26.99/setup.py
```

### Comparing `mypy-boto3-1.26.98/LICENSE` & `mypy-boto3-1.26.99/LICENSE`

 * *Files identical despite different names*

### Comparing `mypy-boto3-1.26.98/PKG-INFO` & `mypy-boto3-1.26.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mypy-boto3
-Version: 1.26.98
-Summary: Type annotations for boto3 1.26.98 master module generated with mypy-boto3-builder 7.14.2
+Version: 1.26.99
+Summary: Type annotations for boto3 1.26.99 master module generated with mypy-boto3-builder 7.14.2
 Home-page: https://github.com/youtype/mypy_boto3_builder
 Author: Vlad Emelianov
 Author-email: vlad.emelianov.nz@gmail.com
 License: MIT License
 Project-URL: Documentation, https://youtype.github.io/boto3_stubs_docs/
 Project-URL: Source, https://github.com/youtype/mypy_boto3_builder
 Project-URL: Tracker, https://github.com/youtype/mypy_boto3_builder/issues
@@ -38,15 +38,15 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3.svg?color=blue)](https://pypi.org/project/mypy-boto3)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3?color=blue)](https://pypistats.org/packages/mypy-boto3)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Dynamic
-[boto3 1.26.98](https://boto3.amazonaws.com/v1/documentation/api/1.26.98/index.html)
+[boto3 1.26.99](https://boto3.amazonaws.com/v1/documentation/api/1.26.99/index.html)
 type annotations builder for
 [boto3-stubs](https://pypi.org/project/boto3-stubs/).
 
 Generated by
 [mypy-boto3-builder 7.14.2](https://github.com/youtype/mypy_boto3_builder).
 
 More information can be found on
```

### Comparing `mypy-boto3-1.26.98/README.md` & `mypy-boto3-1.26.99/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3.svg?color=blue)](https://pypi.org/project/mypy-boto3)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3?color=blue)](https://pypistats.org/packages/mypy-boto3)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Dynamic
-[boto3 1.26.98](https://boto3.amazonaws.com/v1/documentation/api/1.26.98/index.html)
+[boto3 1.26.99](https://boto3.amazonaws.com/v1/documentation/api/1.26.99/index.html)
 type annotations builder for
 [boto3-stubs](https://pypi.org/project/boto3-stubs/).
 
 Generated by
 [mypy-boto3-builder 7.14.2](https://github.com/youtype/mypy_boto3_builder).
 
 More information can be found on
```

### Comparing `mypy-boto3-1.26.98/mypy_boto3/boto3_init_stub.py` & `mypy-boto3-1.26.99/mypy_boto3/boto3_init_stub.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-1.26.98/mypy_boto3/boto3_session_stub.py` & `mypy-boto3-1.26.99/mypy_boto3/boto3_session_stub.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-1.26.98/mypy_boto3/main.py` & `mypy-boto3-1.26.99/mypy_boto3/main.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-1.26.98/mypy_boto3/submodules.py` & `mypy-boto3-1.26.99/mypy_boto3/submodules.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-1.26.98/mypy_boto3.egg-info/PKG-INFO` & `mypy-boto3-1.26.99/mypy_boto3.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mypy-boto3
-Version: 1.26.98
-Summary: Type annotations for boto3 1.26.98 master module generated with mypy-boto3-builder 7.14.2
+Version: 1.26.99
+Summary: Type annotations for boto3 1.26.99 master module generated with mypy-boto3-builder 7.14.2
 Home-page: https://github.com/youtype/mypy_boto3_builder
 Author: Vlad Emelianov
 Author-email: vlad.emelianov.nz@gmail.com
 License: MIT License
 Project-URL: Documentation, https://youtype.github.io/boto3_stubs_docs/
 Project-URL: Source, https://github.com/youtype/mypy_boto3_builder
 Project-URL: Tracker, https://github.com/youtype/mypy_boto3_builder/issues
@@ -38,15 +38,15 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3.svg?color=blue)](https://pypi.org/project/mypy-boto3)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3?color=blue)](https://pypistats.org/packages/mypy-boto3)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Dynamic
-[boto3 1.26.98](https://boto3.amazonaws.com/v1/documentation/api/1.26.98/index.html)
+[boto3 1.26.99](https://boto3.amazonaws.com/v1/documentation/api/1.26.99/index.html)
 type annotations builder for
 [boto3-stubs](https://pypi.org/project/boto3-stubs/).
 
 Generated by
 [mypy-boto3-builder 7.14.2](https://github.com/youtype/mypy_boto3_builder).
 
 More information can be found on
```

### Comparing `mypy-boto3-1.26.98/setup.py` & `mypy-boto3-1.26.99/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -6,24 +6,24 @@
 from setuptools import setup
 
 LONG_DESCRIPTION = (Path(__file__).parent / "README.md").read_text()
 
 
 setup(
     name="mypy-boto3",
-    version="1.26.98",
+    version="1.26.99",
     packages=[
         "mypy_boto3",
     ],
     url="https://github.com/youtype/mypy_boto3_builder",
     license="MIT License",
     author="Vlad Emelianov",
     author_email="vlad.emelianov.nz@gmail.com",
     description=(
-        "Type annotations for boto3 1.26.98 master module generated with mypy-boto3-builder 7.14.2"
+        "Type annotations for boto3 1.26.99 master module generated with mypy-boto3-builder 7.14.2"
     ),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "Environment :: Console",
         "License :: OSI Approved :: MIT License",
         "Natural Language :: English",
```

