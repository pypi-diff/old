# Comparing `tmp/magento_oauth-0.2.1.tar.gz` & `tmp/magento_oauth-0.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "magento_oauth-0.2.1.tar", last modified: Thu Apr  6 19:00:28 2023, max compression
+gzip compressed data, was "magento_oauth-0.2.2.tar", last modified: Thu Apr  6 19:13:03 2023, max compression
```

## Comparing `magento_oauth-0.2.1.tar` & `magento_oauth-0.2.2.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:00:29.386120 magento_oauth-0.2.1/
--rwxrwxrwx   0 noone     (1000) noone     (1000)      689 2023-04-06 19:00:29.384120 magento_oauth-0.2.1/PKG-INFO
--rwxrwxrwx   0 noone     (1000) noone     (1000)       38 2023-04-06 19:00:29.387121 magento_oauth-0.2.1/setup.cfg
--rwxrwxrwx   0 noone     (1000) noone     (1000)      848 2023-04-06 19:00:12.000000 magento_oauth-0.2.1/setup.py
-drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:00:29.257914 magento_oauth-0.2.1/src/
-drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:00:29.338970 magento_oauth-0.2.1/src/magento_oauth.egg-info/
--rwxrwxrwx   0 noone     (1000) noone     (1000)      689 2023-04-06 19:00:29.000000 magento_oauth-0.2.1/src/magento_oauth.egg-info/PKG-INFO
--rwxrwxrwx   0 noone     (1000) noone     (1000)      285 2023-04-06 19:00:29.000000 magento_oauth-0.2.1/src/magento_oauth.egg-info/SOURCES.txt
--rwxrwxrwx   0 noone     (1000) noone     (1000)        1 2023-04-06 19:00:29.000000 magento_oauth-0.2.1/src/magento_oauth.egg-info/dependency_links.txt
--rwxrwxrwx   0 noone     (1000) noone     (1000)       47 2023-04-06 19:00:29.000000 magento_oauth-0.2.1/src/magento_oauth.egg-info/requires.txt
--rwxrwxrwx   0 noone     (1000) noone     (1000)       14 2023-04-06 19:00:29.000000 magento_oauth-0.2.1/src/magento_oauth.egg-info/top_level.txt
-drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:00:29.367970 magento_oauth-0.2.1/src/oauth_magento/
--rwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 13:45:44.000000 magento_oauth-0.2.1/src/oauth_magento/__init__.py
--rwxrwxrwx   0 noone     (1000) noone     (1000)      879 2023-04-06 13:46:22.000000 magento_oauth-0.2.1/src/oauth_magento/oauth_magento_openedx.py
+drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:13:03.473556 magento_oauth-0.2.2/
+-rwxrwxrwx   0 noone     (1000) noone     (1000)      689 2023-04-06 19:13:03.470555 magento_oauth-0.2.2/PKG-INFO
+-rwxrwxrwx   0 noone     (1000) noone     (1000)       38 2023-04-06 19:13:03.473556 magento_oauth-0.2.2/setup.cfg
+-rwxrwxrwx   0 noone     (1000) noone     (1000)      848 2023-04-06 19:12:27.000000 magento_oauth-0.2.2/setup.py
+drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:13:03.340556 magento_oauth-0.2.2/src/
+drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:13:03.423555 magento_oauth-0.2.2/src/magento_oauth.egg-info/
+-rwxrwxrwx   0 noone     (1000) noone     (1000)      689 2023-04-06 19:13:03.000000 magento_oauth-0.2.2/src/magento_oauth.egg-info/PKG-INFO
+-rwxrwxrwx   0 noone     (1000) noone     (1000)      285 2023-04-06 19:13:03.000000 magento_oauth-0.2.2/src/magento_oauth.egg-info/SOURCES.txt
+-rwxrwxrwx   0 noone     (1000) noone     (1000)        1 2023-04-06 19:13:03.000000 magento_oauth-0.2.2/src/magento_oauth.egg-info/dependency_links.txt
+-rwxrwxrwx   0 noone     (1000) noone     (1000)       47 2023-04-06 19:13:03.000000 magento_oauth-0.2.2/src/magento_oauth.egg-info/requires.txt
+-rwxrwxrwx   0 noone     (1000) noone     (1000)       14 2023-04-06 19:13:03.000000 magento_oauth-0.2.2/src/magento_oauth.egg-info/top_level.txt
+drwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 19:13:03.453557 magento_oauth-0.2.2/src/oauth_magento/
+-rwxrwxrwx   0 noone     (1000) noone     (1000)        0 2023-04-06 13:45:44.000000 magento_oauth-0.2.2/src/oauth_magento/__init__.py
+-rwxrwxrwx   0 noone     (1000) noone     (1000)     1044 2023-04-06 19:11:35.000000 magento_oauth-0.2.2/src/oauth_magento/oauth_magento_openedx.py
```

### Comparing `magento_oauth-0.2.1/PKG-INFO` & `magento_oauth-0.2.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: magento_oauth
-Version: 0.2.1
+Version: 0.2.2
 Summary: A Python package for Magento OAuth2 authentication
 Home-page: https://github.com/Francisco-Huerta/oauth_magento_openedx
 Author: Francisco Huerta Yumha
 Author-email: UNKNOWN
 License: UNKNOWN
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `magento_oauth-0.2.1/setup.py` & `magento_oauth-0.2.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name='magento_oauth',
-    version='0.2.1',
+    version='0.2.2',
     packages=find_packages('src'),
     package_dir={'': 'src'},
     install_requires=[
         'social-auth-core>=4.0,<5.0',
         'requests>=2.25,<3.0'
     ],
     author='Francisco Huerta Yumha',
```

### Comparing `magento_oauth-0.2.1/src/magento_oauth.egg-info/PKG-INFO` & `magento_oauth-0.2.2/src/magento_oauth.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: magento-oauth
-Version: 0.2.1
+Version: 0.2.2
 Summary: A Python package for Magento OAuth2 authentication
 Home-page: https://github.com/Francisco-Huerta/oauth_magento_openedx
 Author: Francisco Huerta Yumha
 Author-email: UNKNOWN
 License: UNKNOWN
 Description: UNKNOWN
 Platform: UNKNOWN
```

### Comparing `magento_oauth-0.2.1/src/oauth_magento/oauth_magento_openedx.py` & `magento_oauth-0.2.2/src/oauth_magento/oauth_magento_openedx.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,22 +1,26 @@
-from social_core.backends.oauth import BaseOAuth2
+from social_core.backends.oauth import BaseOAuth1
 
-class MagentoOAuth2(BaseOAuth2):
+class MagentoOAuth1(BaseOAuth1):
     name = 'magento'
     ID_KEY = 'id'
+    REQUEST_TOKEN_URL = 'https://docentedigital.app/oauth/initiate'
     AUTHORIZATION_URL = 'https://docentedigital.app/oauth/authorize'
     ACCESS_TOKEN_URL = 'https://docentedigital.app/oauth/token'
-    USER_DATA_URL = 'https://docentedigital.app/oauth/userinfo'
+    USER_DATA_URL = 'https://docentedigital.app/rest/V1/customers/me'
 
     def get_user_details(self, response):
         """Extract user details from the response object."""
         return {
             'email': response.get('email', ''),
-            'first_name': response.get('first_name', ''),
-            'last_name': response.get('last_name', ''),
+            'first_name': response.get('firstname', ''),
+            'last_name': response.get('lastname', ''),
         }
 
-    def user_data(self, access_token, *args, **kwargs):
+    def user_data(self, access_token, access_token_secret, *args, **kwargs):
         """Load user data from the remote service."""
-        headers = {'Authorization': 'Bearer ' + access_token}
+        headers = {
+            'Authorization': 'Bearer ' + access_token,
+            'Content-Type': 'application/json',
+        }
         response = self.get_json(self.USER_DATA_URL, headers=headers)
-        return response
+        return response
```

