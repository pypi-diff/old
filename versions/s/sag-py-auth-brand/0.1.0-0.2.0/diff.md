# Comparing `tmp/sag-py-auth-brand-0.1.0.tar.gz` & `tmp/sag-py-auth-brand-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sag-py-auth-brand-0.1.0.tar", last modified: Mon Apr  3 07:10:17 2023, max compression
+gzip compressed data, was "sag-py-auth-brand-0.2.0.tar", last modified: Thu Apr  6 11:14:33 2023, max compression
```

## Comparing `sag-py-auth-brand-0.1.0.tar` & `sag-py-auth-brand-0.2.0.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 07:10:17.963141 sag-py-auth-brand-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     5088 2023-04-03 07:10:17.963141 sag-py-auth-brand-0.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4143 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 07:10:17.959141 sag-py-auth-brand-0.1.0/sag_py_auth_brand/
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3361 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand/brand_jwt_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)      368 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand/models.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand/request_brand_context.py
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand/request_brand_logging_filter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 07:10:17.963141 sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5088 2023-04-03 07:10:17.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-03 07:10:17.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 07:10:17.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       71 2023-04-03 07:10:17.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-03 07:10:17.000000 sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-03 07:10:17.963141 sag-py-auth-brand-0.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1391 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 07:10:17.963141 sag-py-auth-brand-0.1.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1891 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__call.py
--rw-r--r--   0 runner    (1001) docker     (123)     1522 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__init.py
--rw-r--r--   0 runner    (1001) docker     (123)     1590 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__verify_brand.py
--rw-r--r--   0 runner    (1001) docker     (123)     2609 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__verify_brand_alias.py
--rw-r--r--   0 runner    (1001) docker     (123)     1261 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/tests/test_request_brand_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-04-03 07:10:02.000000 sag-py-auth-brand-0.1.0/tests/test_request_brand_logging_filter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:14:33.598403 sag-py-auth-brand-0.2.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     5088 2023-04-06 11:14:33.598403 sag-py-auth-brand-0.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4143 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:14:33.598403 sag-py-auth-brand-0.2.0/sag_py_auth_brand/
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3361 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand/brand_jwt_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand/request_brand_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand/request_brand_logging_filter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:14:33.598403 sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5088 2023-04-06 11:14:33.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-06 11:14:33.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:14:33.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-04-06 11:14:33.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       18 2023-04-06 11:14:33.000000 sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-06 11:14:33.602403 sag-py-auth-brand-0.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1391 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:14:33.598403 sag-py-auth-brand-0.2.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1891 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__call.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1522 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__init.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1590 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__verify_brand.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2609 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__verify_brand_alias.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1261 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/tests/test_request_brand_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1729 2023-04-06 11:14:18.000000 sag-py-auth-brand-0.2.0/tests/test_request_brand_logging_filter.py
```

### Comparing `sag-py-auth-brand-0.1.0/LICENSE.txt` & `sag-py-auth-brand-0.2.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/PKG-INFO` & `sag-py-auth-brand-0.2.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sag-py-auth-brand
-Version: 0.1.0
+Version: 0.2.0
 Summary: Keycloak brand/instance authentication for python projects
 Home-page: https://github.com/SamhammerAG/sag_py_auth_brand
 Author: Samhammer AG
 Author-email: support@samhammer.de
 License: MIT
 Project-URL: Documentation, https://github.com/SamhammerAG/sag_py_auth_brand
 Project-URL: Bug Reports, https://github.com/SamhammerAG/sag_py_auth_brand/issues
@@ -43,15 +43,15 @@
 * Verifies the stage over a realm role
 * Allows to set additional permissions by specifying further token roles
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_auth_brand
+pip install sag-py-auth-brand
 
 ### Secure your apis
 
 First create the fast api dependency with the auth config:
 ```python
 from sag_py_auth import TokenRole
 from sag_py_auth_brand.models import AuthConfig
```

### Comparing `sag-py-auth-brand-0.1.0/README.md` & `sag-py-auth-brand-0.2.0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 * Verifies the stage over a realm role
 * Allows to set additional permissions by specifying further token roles
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_auth_brand
+pip install sag-py-auth-brand
 
 ### Secure your apis
 
 First create the fast api dependency with the auth config:
 ```python
 from sag_py_auth import TokenRole
 from sag_py_auth_brand.models import AuthConfig
```

### Comparing `sag-py-auth-brand-0.1.0/sag_py_auth_brand/brand_jwt_auth.py` & `sag-py-auth-brand-0.2.0/sag_py_auth_brand/brand_jwt_auth.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/sag_py_auth_brand/request_brand_context.py` & `sag-py-auth-brand-0.2.0/sag_py_auth_brand/request_brand_context.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/PKG-INFO` & `sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sag-py-auth-brand
-Version: 0.1.0
+Version: 0.2.0
 Summary: Keycloak brand/instance authentication for python projects
 Home-page: https://github.com/SamhammerAG/sag_py_auth_brand
 Author: Samhammer AG
 Author-email: support@samhammer.de
 License: MIT
 Project-URL: Documentation, https://github.com/SamhammerAG/sag_py_auth_brand
 Project-URL: Bug Reports, https://github.com/SamhammerAG/sag_py_auth_brand/issues
@@ -43,15 +43,15 @@
 * Verifies the stage over a realm role
 * Allows to set additional permissions by specifying further token roles
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_auth_brand
+pip install sag-py-auth-brand
 
 ### Secure your apis
 
 First create the fast api dependency with the auth config:
 ```python
 from sag_py_auth import TokenRole
 from sag_py_auth_brand.models import AuthConfig
```

### Comparing `sag-py-auth-brand-0.1.0/sag_py_auth_brand.egg-info/SOURCES.txt` & `sag-py-auth-brand-0.2.0/sag_py_auth_brand.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/setup.py` & `sag-py-auth-brand-0.2.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     LONG_DESCRIPTION = fh.read()
 
 with open("requirements.txt", "r") as fin:
     REQS = fin.read().splitlines()
 
 setuptools.setup(
     name="sag-py-auth-brand",
-    version="0.1.0",
+    version="0.2.0",
     description="Keycloak brand/instance authentication for python projects",
     long_description=LONG_DESCRIPTION,
     long_description_content_type="text/markdown",
     url="https://github.com/SamhammerAG/sag_py_auth_brand",
     author="Samhammer AG",
     author_email="support@samhammer.de",
     license="MIT",
```

### Comparing `sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__call.py` & `sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__call.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__init.py` & `sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__init.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__verify_brand.py` & `sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__verify_brand.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/tests/test_brand_jwt_auth__verify_brand_alias.py` & `sag-py-auth-brand-0.2.0/tests/test_brand_jwt_auth__verify_brand_alias.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/tests/test_request_brand_context.py` & `sag-py-auth-brand-0.2.0/tests/test_request_brand_context.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-brand-0.1.0/tests/test_request_brand_logging_filter.py` & `sag-py-auth-brand-0.2.0/tests/test_request_brand_logging_filter.py`

 * *Files identical despite different names*

