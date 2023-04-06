# Comparing `tmp/passage-identity-2.1.1.tar.gz` & `tmp/passage-identity-2.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "passage-identity-2.1.1.tar", last modified: Mon Oct  3 23:08:28 2022, max compression
+gzip compressed data, was "passage-identity-2.1.2.tar", last modified: Thu Apr  6 15:56:34 2023, max compression
```

## Comparing `passage-identity-2.1.1.tar` & `passage-identity-2.1.2.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 23:08:28.876840 passage-identity-2.1.1/
--rw-r--r--   0 runner    (1001) docker     (121)     1074 2022-10-03 23:08:16.000000 passage-identity-2.1.1/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)     8711 2022-10-03 23:08:28.872840 passage-identity-2.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     8134 2022-10-03 23:08:16.000000 passage-identity-2.1.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 23:08:28.872840 passage-identity-2.1.1/passage_identity.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     8711 2022-10-03 23:08:28.000000 passage-identity-2.1.1/passage_identity.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      379 2022-10-03 23:08:28.000000 passage-identity-2.1.1/passage_identity.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-03 23:08:28.000000 passage-identity-2.1.1/passage_identity.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-10-03 23:08:28.000000 passage-identity-2.1.1/passage_identity.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       16 2022-10-03 23:08:28.000000 passage-identity-2.1.1/passage_identity.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 23:08:28.872840 passage-identity-2.1.1/passageidentity/
--rw-r--r--   0 runner    (1001) docker     (121)      143 2022-10-03 23:08:16.000000 passage-identity-2.1.1/passageidentity/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      381 2022-10-03 23:08:16.000000 passage-identity-2.1.1/passageidentity/errors.py
--rw-r--r--   0 runner    (1001) docker     (121)     2130 2022-10-03 23:08:16.000000 passage-identity-2.1.1/passageidentity/helper.py
--rw-r--r--   0 runner    (1001) docker     (121)    17628 2022-10-03 23:08:16.000000 passage-identity-2.1.1/passageidentity/passage.py
--rw-r--r--   0 runner    (1001) docker     (121)     1752 2022-10-03 23:08:16.000000 passage-identity-2.1.1/passageidentity/requests.py
--rw-r--r--   0 runner    (1001) docker     (121)      104 2022-10-03 23:08:16.000000 passage-identity-2.1.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-03 23:08:28.876840 passage-identity-2.1.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-10-03 23:08:16.000000 passage-identity-2.1.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:34.681238 passage-identity-2.1.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1074 2023-04-06 15:56:19.000000 passage-identity-2.1.2/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     8711 2023-04-06 15:56:34.677238 passage-identity-2.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8134 2023-04-06 15:56:19.000000 passage-identity-2.1.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:34.677238 passage-identity-2.1.2/passage_identity.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8711 2023-04-06 15:56:34.000000 passage-identity-2.1.2/passage_identity.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-04-06 15:56:34.000000 passage-identity-2.1.2/passage_identity.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:56:34.000000 passage-identity-2.1.2/passage_identity.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 15:56:34.000000 passage-identity-2.1.2/passage_identity.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 15:56:34.000000 passage-identity-2.1.2/passage_identity.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:56:34.677238 passage-identity-2.1.2/passageidentity/
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-06 15:56:19.000000 passage-identity-2.1.2/passageidentity/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-04-06 15:56:19.000000 passage-identity-2.1.2/passageidentity/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-06 15:56:19.000000 passage-identity-2.1.2/passageidentity/helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17842 2023-04-06 15:56:19.000000 passage-identity-2.1.2/passageidentity/passage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-04-06 15:56:19.000000 passage-identity-2.1.2/passageidentity/requests.py
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 15:56:19.000000 passage-identity-2.1.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 15:56:34.681238 passage-identity-2.1.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1056 2023-04-06 15:56:19.000000 passage-identity-2.1.2/setup.py
```

### Comparing `passage-identity-2.1.1/LICENSE.txt` & `passage-identity-2.1.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `passage-identity-2.1.1/PKG-INFO` & `passage-identity-2.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: passage-identity
-Version: 2.1.1
+Version: 2.1.2
 Summary: Python library to help manage your Passage application and users
 Home-page: https://github.com/passageidentity/passage-python
 Author: Passage Identity, Inc
 Author-email: support@passage.id
 Project-URL: Bug Tracker, https://github.com/passageidentity/passage-python/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `passage-identity-2.1.1/README.md` & `passage-identity-2.1.2/README.md`

 * *Files identical despite different names*

### Comparing `passage-identity-2.1.1/passage_identity.egg-info/PKG-INFO` & `passage-identity-2.1.2/passage_identity.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: passage-identity
-Version: 2.1.1
+Version: 2.1.2
 Summary: Python library to help manage your Passage application and users
 Home-page: https://github.com/passageidentity/passage-python
 Author: Passage Identity, Inc
 Author-email: support@passage.id
 Project-URL: Bug Tracker, https://github.com/passageidentity/passage-python/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `passage-identity-2.1.1/passageidentity/helper.py` & `passage-identity-2.1.2/passageidentity/helper.py`

 * *Files identical despite different names*

### Comparing `passage-identity-2.1.1/passageidentity/passage.py` & `passage-identity-2.1.2/passageidentity/passage.py`

 * *Files 2% similar despite different names*

```diff
@@ -55,14 +55,16 @@
         session_timeout_length: int
         refresh_enabled: bool
         refresh_absolute_lifetime: int
         refresh_inactivity_lifetime: int
         user_metadata_schema: list
         layouts: list
         default_language: str
+        auth_fallback_method: str
+        auth_fallback_method_ttl: int
 
     class PassageUserType(TypedDict):
         created_at: str
         updated_at: str
         status: UserStatus
         email_verified: bool
         phone_verified: bool
@@ -396,14 +398,16 @@
         self.session_timeout_length = fields["session_timeout_length"]
         self.refresh_enabled = fields["refresh_enabled"]
         self.refresh_absolute_lifetime = fields["refresh_absolute_lifetime"]
         self.refresh_inactivity_lifetime = fields["refresh_inactivity_lifetime"]
         self.user_metadata_schema = fields["user_metadata_schema"]
         self.layouts = fields["layouts"]
         self.default_language = fields["default_language"]
+        self.auth_fallback_method = fields["auth_fallback_method"]
+        self.auth_fallback_method_ttl = fields["auth_fallback_method_ttl"]
 class PassageDevice:
     def __init__(self, fields={}):
         self.id = fields["id"]
         try:
             self.created_at = datetime.strptime(time_to_milliseconds(fields["created_at"]),"%Y-%m-%dT%H:%M:%S.%fZ")
         except:
             self.created_at = datetime.strptime(fields["created_at"],"%Y-%m-%dT%H:%M:%SZ")
```

### Comparing `passage-identity-2.1.1/passageidentity/requests.py` & `passage-identity-2.1.2/passageidentity/requests.py`

 * *Files identical despite different names*

### Comparing `passage-identity-2.1.1/setup.py` & `passage-identity-2.1.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="passage-identity",
-    version="2.1.1",
+    version="2.1.2",
     author="Passage Identity, Inc",
     author_email="support@passage.id",
     description="Python library to help manage your Passage application and users",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/passageidentity/passage-python",
     project_urls={
```

