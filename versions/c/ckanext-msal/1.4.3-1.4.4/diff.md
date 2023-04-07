# Comparing `tmp/ckanext-msal-1.4.3.tar.gz` & `tmp/ckanext-msal-1.4.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ckanext-msal-1.4.3.tar", last modified: Thu Apr  6 06:24:44 2023, max compression
+gzip compressed data, was "ckanext-msal-1.4.4.tar", last modified: Fri Apr  7 07:41:15 2023, max compression
```

## Comparing `ckanext-msal-1.4.3.tar` & `ckanext-msal-1.4.4.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/
--rw-rw-r--   0 cherry    (1000) cherry    (1000)    34500 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/LICENSE
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      193 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/MANIFEST.in
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     3861 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/PKG-INFO
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     3308 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/README.md
-drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-06 06:24:44.941140 ckanext-msal-1.4.3/ckanext/
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      219 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/__init__.py
-drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/ckanext/msal/
--rw-rw-r--   0 cherry    (1000) cherry    (1000)        0 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/__init__.py
-drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/ckanext/msal/assets/
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      271 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/assets/webassets.yml
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      865 2022-05-16 12:30:13.000000 ckanext-msal-1.4.3/ckanext/msal/config.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     1298 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/middleware.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     1613 2022-04-05 13:38:24.000000 ckanext-msal-1.4.3/ckanext/msal/plugin.py
-drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/ckanext/msal/tests/
--rw-rw-r--   0 cherry    (1000) cherry    (1000)        0 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/tests/__init__.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)       46 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/tests/fixtures.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     3854 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/tests/test_user.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     1276 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/tests/test_utils.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     8711 2022-05-17 09:24:10.000000 ckanext-msal-1.4.3/ckanext/msal/user.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     4132 2022-04-01 11:40:30.000000 ckanext-msal-1.4.3/ckanext/msal/utils.py
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     2299 2022-04-01 10:37:53.000000 ckanext-msal-1.4.3/ckanext/msal/views.py
-drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/ckanext_msal.egg-info/
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     3861 2023-04-06 06:24:44.000000 ckanext-msal-1.4.3/ckanext_msal.egg-info/PKG-INFO
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      637 2023-04-06 06:24:44.000000 ckanext-msal-1.4.3/ckanext_msal.egg-info/SOURCES.txt
--rw-rw-r--   0 cherry    (1000) cherry    (1000)        1 2023-04-06 06:24:44.000000 ckanext-msal-1.4.3/ckanext_msal.egg-info/dependency_links.txt
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      110 2023-04-06 06:24:44.000000 ckanext-msal-1.4.3/ckanext_msal.egg-info/entry_points.txt
--rw-rw-r--   0 cherry    (1000) cherry    (1000)        8 2023-04-06 06:24:44.000000 ckanext-msal-1.4.3/ckanext_msal.egg-info/namespace_packages.txt
--rw-rw-r--   0 cherry    (1000) cherry    (1000)        8 2023-04-06 06:24:44.000000 ckanext-msal-1.4.3/ckanext_msal.egg-info/top_level.txt
--rw-rw-r--   0 cherry    (1000) cherry    (1000)       65 2022-11-08 12:53:47.000000 ckanext-msal-1.4.3/requirements.txt
--rw-rw-r--   0 cherry    (1000) cherry    (1000)      517 2023-04-06 06:24:44.945140 ckanext-msal-1.4.3/setup.cfg
--rw-rw-r--   0 cherry    (1000) cherry    (1000)     3754 2023-04-06 06:24:01.000000 ckanext-msal-1.4.3/setup.py
+drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)    34500 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/LICENSE
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      193 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/MANIFEST.in
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     3861 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/PKG-INFO
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     3308 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/README.md
+drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/ckanext/
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      219 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/__init__.py
+drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/ckanext/msal/
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)        0 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/__init__.py
+drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/ckanext/msal/assets/
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      271 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/assets/webassets.yml
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      865 2022-05-16 12:30:13.000000 ckanext-msal-1.4.4/ckanext/msal/config.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      998 2023-04-07 07:39:55.000000 ckanext-msal-1.4.4/ckanext/msal/middleware.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     1652 2023-04-07 07:39:55.000000 ckanext-msal-1.4.4/ckanext/msal/plugin.py
+drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/ckanext/msal/tests/
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)        0 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/tests/__init__.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)       46 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/tests/fixtures.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     3854 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/tests/test_user.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     1276 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/tests/test_utils.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     8711 2022-05-17 09:24:10.000000 ckanext-msal-1.4.4/ckanext/msal/user.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     4132 2022-04-01 11:40:30.000000 ckanext-msal-1.4.4/ckanext/msal/utils.py
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     2299 2022-04-01 10:37:53.000000 ckanext-msal-1.4.4/ckanext/msal/views.py
+drwxrwxr-x   0 cherry    (1000) cherry    (1000)        0 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/ckanext_msal.egg-info/
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     3861 2023-04-07 07:41:15.000000 ckanext-msal-1.4.4/ckanext_msal.egg-info/PKG-INFO
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      637 2023-04-07 07:41:15.000000 ckanext-msal-1.4.4/ckanext_msal.egg-info/SOURCES.txt
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)        1 2023-04-07 07:41:15.000000 ckanext-msal-1.4.4/ckanext_msal.egg-info/dependency_links.txt
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      110 2023-04-07 07:41:15.000000 ckanext-msal-1.4.4/ckanext_msal.egg-info/entry_points.txt
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)        8 2023-04-07 07:41:15.000000 ckanext-msal-1.4.4/ckanext_msal.egg-info/namespace_packages.txt
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)        8 2023-04-07 07:41:15.000000 ckanext-msal-1.4.4/ckanext_msal.egg-info/top_level.txt
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)       65 2022-11-08 12:53:47.000000 ckanext-msal-1.4.4/requirements.txt
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)      517 2023-04-07 07:41:15.504333 ckanext-msal-1.4.4/setup.cfg
+-rw-rw-r--   0 cherry    (1000) cherry    (1000)     3754 2023-04-07 07:40:33.000000 ckanext-msal-1.4.4/setup.py
```

### Comparing `ckanext-msal-1.4.3/LICENSE` & `ckanext-msal-1.4.4/LICENSE`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/PKG-INFO` & `ckanext-msal-1.4.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ckanext-msal
-Version: 1.4.3
+Version: 1.4.4
 Summary: Login to CKAN using The Microsoft Authentication Library (MSAL)
 Home-page: https://github.com/mutantsan/ckanext-msal
 Author: Alexandr Cherniavskyi
 Author-email: mutantsan@gmail.com
 License: AGPL
 Keywords: CKAN SSO,CKAN,Microsoft,SAML,MSAL
 Classifier: Development Status :: 4 - Beta
```

### Comparing `ckanext-msal-1.4.3/README.md` & `ckanext-msal-1.4.4/README.md`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext/msal/config.py` & `ckanext-msal-1.4.4/ckanext/msal/config.py`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext/msal/plugin.py` & `ckanext-msal-1.4.4/ckanext/msal/plugin.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import ckan.plugins as p
 import ckan.plugins.toolkit as tk
 import ckan.model as model
 from ckan.common import session
 
-from ckanext.msal.middleware import SessionInvalidator
+from ckanext.msal.middleware import _invalidate_user_session
 from ckanext.msal.views import get_blueprints
 import ckanext.msal.user as user_funcs
 import ckanext.msal.utils as msal_utils
 
 
 class MsalPlugin(p.SingletonPlugin):
     p.implements(p.IConfigurer)
@@ -18,15 +18,16 @@
     # IConfigurer
 
     def update_config(self, config_):
         tk.add_template_directory(config_, "templates")
 
     # IMiddleware
     def make_middleware(self, app, config):
-        return SessionInvalidator(app)
+        app.before_request(_invalidate_user_session)
+        return app
 
     # IBlueprint
     def get_blueprint(self):
         return get_blueprints()
 
     # IAuthenticator
     def identify(self):
```

### Comparing `ckanext-msal-1.4.3/ckanext/msal/tests/test_user.py` & `ckanext-msal-1.4.4/ckanext/msal/tests/test_user.py`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext/msal/tests/test_utils.py` & `ckanext-msal-1.4.4/ckanext/msal/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext/msal/user.py` & `ckanext-msal-1.4.4/ckanext/msal/user.py`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext/msal/utils.py` & `ckanext-msal-1.4.4/ckanext/msal/utils.py`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext/msal/views.py` & `ckanext-msal-1.4.4/ckanext/msal/views.py`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/ckanext_msal.egg-info/PKG-INFO` & `ckanext-msal-1.4.4/ckanext_msal.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ckanext-msal
-Version: 1.4.3
+Version: 1.4.4
 Summary: Login to CKAN using The Microsoft Authentication Library (MSAL)
 Home-page: https://github.com/mutantsan/ckanext-msal
 Author: Alexandr Cherniavskyi
 Author-email: mutantsan@gmail.com
 License: AGPL
 Keywords: CKAN SSO,CKAN,Microsoft,SAML,MSAL
 Classifier: Development Status :: 4 - Beta
```

### Comparing `ckanext-msal-1.4.3/ckanext_msal.egg-info/SOURCES.txt` & `ckanext-msal-1.4.4/ckanext_msal.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/setup.cfg` & `ckanext-msal-1.4.4/setup.cfg`

 * *Files identical despite different names*

### Comparing `ckanext-msal-1.4.3/setup.py` & `ckanext-msal-1.4.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 setup(
     name='''ckanext-msal''',
 
     # Versions should comply with PEP440.  For a discussion on single-sourcing
     # the version across setup.py and the project code, see
     # http://packaging.python.org/en/latest/tutorial.html#version
-    version='1.4.3',
+    version='1.4.4',
 
     description='''Login to CKAN using The Microsoft Authentication Library (MSAL)''',
     long_description=long_description,
     long_description_content_type="text/markdown",
 
     # The project's main homepage.
     url='https://github.com/mutantsan/ckanext-msal',
```

