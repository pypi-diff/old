# Comparing `tmp/structure_py-0.0.4.tar.gz` & `tmp/structure_py-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "structure_py-0.0.4.tar", last modified: Mon Apr  3 11:58:19 2023, max compression
+gzip compressed data, was "structure_py-0.1.0.tar", last modified: Thu Apr  6 11:26:35 2023, max compression
```

## Comparing `structure_py-0.0.4.tar` & `structure_py-0.1.0.tar`

### file list

```diff
@@ -1,43 +1,43 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.337431 structure_py-0.0.4/
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-04-03 11:58:11.000000 structure_py-0.0.4/LICENSE.md
--rw-r--r--   0 runner    (1001) docker     (123)     2028 2023-04-03 11:58:19.337431 structure_py-0.0.4/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (123)     1759 2023-04-03 11:58:11.000000 structure_py-0.0.4/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 11:58:19.337431 structure_py-0.0.4/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)     1105 2023-04-03 11:58:11.000000 structure_py-0.0.4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.333431 structure_py-0.0.4/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.333431 structure_py-0.0.4/src/sdk/
--rwxr-xr-x   0 runner    (1001) docker     (123)       95 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1513 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/accounts.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4675 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/companies.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.333431 structure_py-0.0.4/src/sdk/models/
--rwxr-xr-x   0 runner    (1001) docker     (123)       76 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.337431 structure_py-0.0.4/src/sdk/models/operations/
--rwxr-xr-x   0 runner    (1001) docker     (123)      689 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1310 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/enrich_company.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      733 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/enrich_person.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1096 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/list_employees.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1086 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/list_jobs.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      490 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/list_users.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      981 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/login.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      483 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/me.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1536 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/search_companies.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1530 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/operations/search_people.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.337431 structure_py-0.0.4/src/sdk/models/shared/
--rwxr-xr-x   0 runner    (1001) docker     (123)      221 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/shared/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      807 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/shared/account.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2571 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/shared/company.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     7557 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/shared/person.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      335 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/models/shared/security.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2756 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/people.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     3225 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/sdk.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2603 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/user.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.337431 structure_py-0.0.4/src/sdk/utils/
--rwxr-xr-x   0 runner    (1001) docker     (123)      120 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/utils/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     3705 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/utils/retries.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    24799 2023-04-03 11:58:11.000000 structure_py-0.0.4/src/sdk/utils/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:58:19.337431 structure_py-0.0.4/src/structure_py.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2028 2023-04-03 11:58:19.000000 structure_py-0.0.4/src/structure_py.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1009 2023-04-03 11:58:19.000000 structure_py-0.0.4/src/structure_py.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 11:58:19.000000 structure_py-0.0.4/src/structure_py.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      321 2023-04-03 11:58:19.000000 structure_py-0.0.4/src/structure_py.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-03 11:58:19.000000 structure_py-0.0.4/src/structure_py.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.498545 structure_py-0.1.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-04-06 11:26:24.000000 structure_py-0.1.0/LICENSE.md
+-rw-r--r--   0 runner    (1001) docker     (123)     3646 2023-04-06 11:26:35.498545 structure_py-0.1.0/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3377 2023-04-06 11:26:24.000000 structure_py-0.1.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:26:35.498545 structure_py-0.1.0/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1105 2023-04-06 11:26:24.000000 structure_py-0.1.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.494545 structure_py-0.1.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.494545 structure_py-0.1.0/src/sdk/
+-rwxr-xr-x   0 runner    (1001) docker     (123)       95 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1513 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/accounts.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4675 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/companies.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.494545 structure_py-0.1.0/src/sdk/models/
+-rwxr-xr-x   0 runner    (1001) docker     (123)       76 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.494545 structure_py-0.1.0/src/sdk/models/operations/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      689 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1310 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/enrich_company.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      733 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/enrich_person.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1096 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/list_employees.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1086 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/list_jobs.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      490 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/list_users.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      981 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/login.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      483 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/me.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1536 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/search_companies.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1530 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/operations/search_people.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.494545 structure_py-0.1.0/src/sdk/models/shared/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      221 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/shared/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      807 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/shared/account.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2571 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/shared/company.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7557 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/shared/person.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      335 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/models/shared/security.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2756 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/people.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3225 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/sdk.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2603 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/user.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.494545 structure_py-0.1.0/src/sdk/utils/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      120 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/utils/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3705 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/utils/retries.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    24799 2023-04-06 11:26:24.000000 structure_py-0.1.0/src/sdk/utils/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:26:35.498545 structure_py-0.1.0/src/structure_py.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3646 2023-04-06 11:26:35.000000 structure_py-0.1.0/src/structure_py.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1009 2023-04-06 11:26:35.000000 structure_py-0.1.0/src/structure_py.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:26:35.000000 structure_py-0.1.0/src/structure_py.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      321 2023-04-06 11:26:35.000000 structure_py-0.1.0/src/structure_py.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-06 11:26:35.000000 structure_py-0.1.0/src/structure_py.egg-info/top_level.txt
```

### Comparing `structure_py-0.0.4/LICENSE.md` & `structure_py-0.1.0/LICENSE.md`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/setup.py` & `structure_py-0.1.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,15 +6,15 @@
     with open("README.md", "r") as fh:
         long_description = fh.read()
 except FileNotFoundError:
     long_description = ""
 
 setuptools.setup(
     name="structure_py",
-    version="0.0.4",
+    version="0.1.0",
     author="Structure",
     description="Python Client SDK Generated by Speakeasy",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(where="src"),
     install_requires=[
         "certifi==2022.12.07",
```

### Comparing `structure_py-0.0.4/src/sdk/accounts.py` & `structure_py-0.1.0/src/sdk/accounts.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/companies.py` & `structure_py-0.1.0/src/sdk/companies.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/__init__.py` & `structure_py-0.1.0/src/sdk/models/operations/__init__.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/enrich_company.py` & `structure_py-0.1.0/src/sdk/models/operations/enrich_company.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/enrich_person.py` & `structure_py-0.1.0/src/sdk/models/operations/enrich_person.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/list_employees.py` & `structure_py-0.1.0/src/sdk/models/operations/list_employees.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/list_jobs.py` & `structure_py-0.1.0/src/sdk/models/operations/list_jobs.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/login.py` & `structure_py-0.1.0/src/sdk/models/operations/login.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/search_companies.py` & `structure_py-0.1.0/src/sdk/models/operations/search_companies.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/operations/search_people.py` & `structure_py-0.1.0/src/sdk/models/operations/search_people.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/shared/account.py` & `structure_py-0.1.0/src/sdk/models/shared/account.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/shared/company.py` & `structure_py-0.1.0/src/sdk/models/shared/company.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/models/shared/person.py` & `structure_py-0.1.0/src/sdk/models/shared/person.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/people.py` & `structure_py-0.1.0/src/sdk/people.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/sdk.py` & `structure_py-0.1.0/src/sdk/sdk.py`

 * *Files 4% similar despite different names*

```diff
@@ -24,16 +24,16 @@
     user: User
     r"""User"""
 
     _client: requests_http.Session
     _security_client: requests_http.Session
     _server_url: str = SERVERS[0]
     _language: str = "python"
-    _sdk_version: str = "0.0.4"
-    _gen_version: str = "2.16.7"
+    _sdk_version: str = "0.1.0"
+    _gen_version: str = "2.17.8"
 
     def __init__(self,
                  security: shared.Security = None,
                  server_url: str = None,
                  url_params: dict[str, str] = None,
                  client: requests_http.Session = None
                  ) -> None:
```

### Comparing `structure_py-0.0.4/src/sdk/user.py` & `structure_py-0.1.0/src/sdk/user.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/utils/retries.py` & `structure_py-0.1.0/src/sdk/utils/retries.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/sdk/utils/utils.py` & `structure_py-0.1.0/src/sdk/utils/utils.py`

 * *Files identical despite different names*

### Comparing `structure_py-0.0.4/src/structure_py.egg-info/SOURCES.txt` & `structure_py-0.1.0/src/structure_py.egg-info/SOURCES.txt`

 * *Files identical despite different names*

