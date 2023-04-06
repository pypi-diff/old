# Comparing `tmp/im-squonk2-client-2.1.1.tar.gz` & `tmp/im-squonk2-client-2.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "im-squonk2-client-2.1.1.tar", last modified: Wed Oct 26 16:01:48 2022, max compression
+gzip compressed data, was "im-squonk2-client-2.1.2.tar", last modified: Wed Oct 26 17:00:16 2022, max compression
```

## Comparing `im-squonk2-client-2.1.1.tar` & `im-squonk2-client-2.1.2.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 16:01:48.748862 im-squonk2-client-2.1.1/
--rw-r--r--   0 runner    (1001) docker     (121)     1080 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       41 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     7858 2022-10-26 16:01:48.748862 im-squonk2-client-2.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7124 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/README.rst
--rw-r--r--   0 runner    (1001) docker     (121)       85 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       52 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-26 16:01:48.748862 im-squonk2-client-2.1.1/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (121)     1579 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 16:01:48.744862 im-squonk2-client-2.1.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 16:01:48.748862 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     7858 2022-10-26 16:01:48.000000 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      454 2022-10-26 16:01:48.000000 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 16:01:48.000000 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 16:01:48.000000 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       46 2022-10-26 16:01:48.000000 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        8 2022-10-26 16:01:48.000000 im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 16:01:48.748862 im-squonk2-client-2.1.1/src/squonk2/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/src/squonk2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    19931 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/src/squonk2/as_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     4751 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/src/squonk2/auth.py
--rw-r--r--   0 runner    (1001) docker     (121)    46803 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/src/squonk2/dm_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     9767 2022-10-26 16:01:40.000000 im-squonk2-client-2.1.1/src/squonk2/environment.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 17:00:16.214166 im-squonk2-client-2.1.2/
+-rw-r--r--   0 runner    (1001) docker     (121)     1080 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       41 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     7885 2022-10-26 17:00:16.210166 im-squonk2-client-2.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     7151 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/README.rst
+-rw-r--r--   0 runner    (1001) docker     (121)       85 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       52 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-26 17:00:16.214166 im-squonk2-client-2.1.2/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1579 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 17:00:16.210166 im-squonk2-client-2.1.2/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 17:00:16.210166 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     7885 2022-10-26 17:00:16.000000 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      454 2022-10-26 17:00:16.000000 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 17:00:16.000000 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-26 17:00:15.000000 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       46 2022-10-26 17:00:16.000000 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        8 2022-10-26 17:00:16.000000 im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-26 17:00:16.210166 im-squonk2-client-2.1.2/src/squonk2/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/src/squonk2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19931 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/src/squonk2/as_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4751 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/src/squonk2/auth.py
+-rw-r--r--   0 runner    (1001) docker     (121)    46803 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/src/squonk2/dm_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9935 2022-10-26 17:00:06.000000 im-squonk2-client-2.1.2/src/squonk2/environment.py
```

### Comparing `im-squonk2-client-2.1.1/LICENSE` & `im-squonk2-client-2.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `im-squonk2-client-2.1.1/PKG-INFO` & `im-squonk2-client-2.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: im-squonk2-client
-Version: 2.1.1
+Version: 2.1.2
 Summary: Squonk2 Python Client
 Home-page: https://github.com/informaticsmatters/squonk2-python-client
 Author: Alan Christie
 Author-email: achristie@informaticsmatters.com
 License: MIT
 Keywords: api
 Platform: any
@@ -196,14 +196,15 @@
 
 **Using the Environment**
 
 ..  code-block:: python
 
     from squonk2.environment import Environment
 
+    _ = Environment.load()
     environment: Environment = Environment('site-a')
     # Get the AS API for 'local'
     # The hostname is augmented so you will get (for the above example)
     # the value 'https://as.example.com/account-server-api'
     as_api: str = environment.as_api()
 
 Documentation
```

### Comparing `im-squonk2-client-2.1.1/README.rst` & `im-squonk2-client-2.1.2/README.rst`

 * *Files 0% similar despite different names*

```diff
@@ -175,14 +175,15 @@
 
 **Using the Environment**
 
 ..  code-block:: python
 
     from squonk2.environment import Environment
 
+    _ = Environment.load()
     environment: Environment = Environment('site-a')
     # Get the AS API for 'local'
     # The hostname is augmented so you will get (for the above example)
     # the value 'https://as.example.com/account-server-api'
     as_api: str = environment.as_api()
 
 Documentation
```

### Comparing `im-squonk2-client-2.1.1/setup.py` & `im-squonk2-client-2.1.2/setup.py`

 * *Files identical despite different names*

### Comparing `im-squonk2-client-2.1.1/src/im_squonk2_client.egg-info/PKG-INFO` & `im-squonk2-client-2.1.2/src/im_squonk2_client.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: im-squonk2-client
-Version: 2.1.1
+Version: 2.1.2
 Summary: Squonk2 Python Client
 Home-page: https://github.com/informaticsmatters/squonk2-python-client
 Author: Alan Christie
 Author-email: achristie@informaticsmatters.com
 License: MIT
 Keywords: api
 Platform: any
@@ -196,14 +196,15 @@
 
 **Using the Environment**
 
 ..  code-block:: python
 
     from squonk2.environment import Environment
 
+    _ = Environment.load()
     environment: Environment = Environment('site-a')
     # Get the AS API for 'local'
     # The hostname is augmented so you will get (for the above example)
     # the value 'https://as.example.com/account-server-api'
     as_api: str = environment.as_api()
 
 Documentation
```

### Comparing `im-squonk2-client-2.1.1/src/squonk2/as_api.py` & `im-squonk2-client-2.1.2/src/squonk2/as_api.py`

 * *Files identical despite different names*

### Comparing `im-squonk2-client-2.1.1/src/squonk2/auth.py` & `im-squonk2-client-2.1.2/src/squonk2/auth.py`

 * *Files identical despite different names*

### Comparing `im-squonk2-client-2.1.1/src/squonk2/dm_api.py` & `im-squonk2-client-2.1.2/src/squonk2/dm_api.py`

 * *Files identical despite different names*

### Comparing `im-squonk2-client-2.1.1/src/squonk2/environment.py` & `im-squonk2-client-2.1.2/src/squonk2/environment.py`

 * *Files 6% similar despite different names*

```diff
@@ -160,82 +160,94 @@
         self.__keycloak_as_client_id: Optional[str] = self.__get_config_value(
             _KEYCLOAK_AS_CLIENT_ID_KEY, optional=True
         )
         self.__as_hostname: Optional[str] = self.__get_config_value(
             _AS_HOSTNAME_KEY, optional=True
         )
 
+    @property
     def environment(self) -> str:
         """Return the environment name."""
         return self.__environment
 
+    @property
     def keycloak_hostname(self) -> str:
         """Return the keycloak hostname. This is the unmodified
         value found in the environment.
         """
         return self.__keycloak_hostname
 
+    @property
     def keycloak_url(self) -> str:
         """Return the keycloak URL. This is the hostname
         plus the 'http' prefix and '/auth' postfix.
         """
         if not self.__keycloak_hostname.startswith("http"):
             ret_val: str = f"https://{self.__keycloak_hostname}"
         else:
             ret_val = self.__keycloak_hostname
         if not ret_val.endswith("/auth"):
             ret_val += "/auth"
         return ret_val
 
+    @property
     def keycloak_realm(self) -> str:
         """Return the keycloak realm."""
         return self.__keycloak_realm
 
+    @property
     def keycloak_as_client_id(self) -> Optional[str]:
         """Return the keycloak Account Server client ID."""
         return self.__keycloak_as_client_id
 
+    @property
     def keycloak_dm_client_id(self) -> str:
         """Return the keycloak Data Manager client ID."""
         return self.__keycloak_dm_client_id
 
+    @property
     def admin_user(self) -> str:
         """Return the keycloak username."""
         return self.__admin_user
 
+    @property
     def admin_password(self) -> str:
         """Return the keycloak user's password."""
         return self.__admin_password
 
+    @property
     def as_hostname(self) -> Optional[str]:
         """Return the keycloak hostname. This is the unmodified
         value found in the environment but can be None
         """
         return self.__as_hostname
 
+    @property
     def as_api(self) -> Optional[str]:
         """Return the AS API. This is the environment hostname
         with a 'http' prefix and '/account-server-api' postfix.
         """
         if not self.__as_hostname:
             return None
         if not self.__as_hostname.startswith("http"):
             ret_val: str = f"https://{self.__as_hostname}"
         else:
             ret_val = self.__as_hostname
         if not ret_val.endswith("/account-server-api"):
             ret_val += "/account-server-api"
         return ret_val
 
+    @property
     def dm_hostname(self) -> str:
         """Return the keycloak hostname. This is the unmodified
         value found in the environment.
         """
         return self.__dm_hostname
 
+    @property
     def dm_api(self) -> str:
         """Return the DM API. This is the environment hostname
         with a 'http' prefix and '/data-manager-api' postfix.
         """
         if not self.__dm_hostname.startswith("http"):
             ret_val: str = f"https://{self.__dm_hostname}"
         else:
```

