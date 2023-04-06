# Comparing `tmp/sag-py-auth-0.1.3.tar.gz` & `tmp/sag-py-auth-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sag-py-auth-0.1.3.tar", last modified: Sun Apr  2 18:16:32 2023, max compression
+gzip compressed data, was "sag-py-auth-0.1.4.tar", last modified: Thu Apr  6 11:01:54 2023, max compression
```

## Comparing `sag-py-auth-0.1.3.tar` & `sag-py-auth-0.1.4.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 18:16:32.218851 sag-py-auth-0.1.3/
--rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     4131 2023-04-02 18:16:32.218851 sag-py-auth-0.1.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3231 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 18:16:32.218851 sag-py-auth-0.1.3/sag_py_auth/
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      495 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/auth_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     3449 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/jwt_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     2060 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/models.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)     2198 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/token_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/token_types.py
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/user_name_logging_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/sag_py_auth/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 18:16:32.218851 sag-py-auth-0.1.3/sag_py_auth.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4131 2023-04-02 18:16:32.000000 sag-py-auth-0.1.3/sag_py_auth.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      772 2023-04-02 18:16:32.000000 sag-py-auth-0.1.3/sag_py_auth.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-02 18:16:32.000000 sag-py-auth-0.1.3/sag_py_auth.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-04-02 18:16:32.000000 sag-py-auth-0.1.3/sag_py_auth.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-02 18:16:32.000000 sag-py-auth-0.1.3/sag_py_auth.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-02 18:16:32.218851 sag-py-auth-0.1.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 18:16:32.218851 sag-py-auth-0.1.3/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_auth_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     4606 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_jwt_auth__call.py
--rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_jwt_auth__init.py
--rw-r--r--   0 runner    (1001) docker     (123)     3449 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_jwt_auth__realm_roles.py
--rw-r--r--   0 runner    (1001) docker     (123)     5379 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_jwt_auth__roles.py
--rw-r--r--   0 runner    (1001) docker     (123)     2050 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_jwt_auth__verify_and_decode_token.py
--rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_token_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_user_name_logging_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)      623 2023-04-02 18:16:23.000000 sag-py-auth-0.1.3/tests/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:01:54.324050 sag-py-auth-0.1.4/
+-rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     4845 2023-04-06 11:01:54.324050 sag-py-auth-0.1.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3945 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:01:54.320050 sag-py-auth-0.1.4/sag_py_auth/
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      495 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/auth_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3455 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/jwt_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2136 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     2198 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/token_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/token_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/user_name_logging_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/sag_py_auth/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:01:54.324050 sag-py-auth-0.1.4/sag_py_auth.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4845 2023-04-06 11:01:54.000000 sag-py-auth-0.1.4/sag_py_auth.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      772 2023-04-06 11:01:54.000000 sag-py-auth-0.1.4/sag_py_auth.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:01:54.000000 sag-py-auth-0.1.4/sag_py_auth.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-04-06 11:01:54.000000 sag-py-auth-0.1.4/sag_py_auth.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-06 11:01:54.000000 sag-py-auth-0.1.4/sag_py_auth.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       78 2023-04-06 11:01:54.324050 sag-py-auth-0.1.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:01:54.324050 sag-py-auth-0.1.4/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_auth_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4606 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_jwt_auth__call.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_jwt_auth__init.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3449 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_jwt_auth__realm_roles.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5379 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_jwt_auth__roles.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2050 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_jwt_auth__verify_and_decode_token.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1558 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_token_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_user_name_logging_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      623 2023-04-06 11:01:45.000000 sag-py-auth-0.1.4/tests/test_utils.py
```

### Comparing `sag-py-auth-0.1.3/LICENSE.txt` & `sag-py-auth-0.1.4/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/PKG-INFO` & `sag-py-auth-0.1.4/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sag-py-auth
-Version: 0.1.3
+Version: 0.1.4
 Summary: Keycloak authentication for python projects
 Home-page: https://github.com/SamhammerAG/sag_py_auth
 Author: Samhammer AG
 Author-email: support@samhammer.de
 License: MIT
 Project-URL: Documentation, https://github.com/SamhammerAG/sag_py_auth
 Project-URL: Bug Reports, https://github.com/SamhammerAG/sag_py_auth/issues
@@ -39,21 +39,22 @@
 * Verifies auth tokens: signature, expiration, issuer, audience
 * Allows to set permissions by specifying roles and realm roles
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_auth
+pip install sag-py-auth
 
 ### Secure your apis
 
 First create the fast api dependency with the auth config:
 ```python
-from sag_py_auth import AuthConfig, JwtAuth, TokenRole
+from sag_py_auth.models import AuthConfig, TokenRole
+from sag_py_auth.jwt_auth import JwtAuth
 from fastapi import Depends
 
 auth_config = AuthConfig("https://authserver.com/auth/realms/projectName", "myaudience")
 required_roles = [TokenRole("clientname", "adminrole")]
 required_realm_roles = ["additionalrealmrole"]
 requires_admin = Depends(JwtAuth(auth_config, required_roles, required_realm_roles))
 ```
@@ -74,15 +75,15 @@
 
 ### Get user information
 
 The Jwt call directly returns a token object that can be used to get additional information.
 
 Furthermore you can access the context directly:
 ```python
-from sag_py_auth import get_token as get_token_from_context
+from sag_py_auth.auth_context import get_token as get_token_from_context
 token = get_token_from_context()
 ```
 
 This works in async calls but not in sub threads (without additional changes).
 
 See:
 * https://docs.python.org/3/library/contextvars.html
@@ -108,12 +109,40 @@
 console_handler = logging.StreamHandler(sys.stdout)
 console_handler.addFilter(UserNameLoggingFilter())
 
 ```
 
 The filter provides the following two fields as soon as the user is authenticated: user_name, authorized_party
 
+### How a token has to look like
+
+```json
+{
+
+    "iss": "https://authserver.com/auth/realms/projectName",
+    "aud": ["audienceOne", "audienceTwo"],
+    "typ": "Bearer",
+    "azp": "public-project-swagger",
+    "preferred_username": "preferredUsernameValue",
+    .....
+    "realm_access": {
+        "roles": ["myRealmRoleOne"]
+    },
+    "resource_access": {
+        "my-client-one": {
+            "roles": ["a-permission-role", "user"]
+        },
+        "my-client-two": {
+            "roles": ["a-permission-role", "admin"]
+        }
+    }
+}
+```
+
+* realm_access contains the realm roles
+* resource_access contains the token roles for one or multiple clients
+
 ## How to publish
 
 * Update the version in setup.py and commit your change
 * Create a tag with the same version number
 * Let github do the rest
```

### Comparing `sag-py-auth-0.1.3/README.md` & `sag-py-auth-0.1.4/README.md`

 * *Files 20% similar despite different names*

```diff
@@ -16,21 +16,22 @@
 * Verifies auth tokens: signature, expiration, issuer, audience
 * Allows to set permissions by specifying roles and realm roles
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_auth
+pip install sag-py-auth
 
 ### Secure your apis
 
 First create the fast api dependency with the auth config:
 ```python
-from sag_py_auth import AuthConfig, JwtAuth, TokenRole
+from sag_py_auth.models import AuthConfig, TokenRole
+from sag_py_auth.jwt_auth import JwtAuth
 from fastapi import Depends
 
 auth_config = AuthConfig("https://authserver.com/auth/realms/projectName", "myaudience")
 required_roles = [TokenRole("clientname", "adminrole")]
 required_realm_roles = ["additionalrealmrole"]
 requires_admin = Depends(JwtAuth(auth_config, required_roles, required_realm_roles))
 ```
@@ -51,15 +52,15 @@
 
 ### Get user information
 
 The Jwt call directly returns a token object that can be used to get additional information.
 
 Furthermore you can access the context directly:
 ```python
-from sag_py_auth import get_token as get_token_from_context
+from sag_py_auth.auth_context import get_token as get_token_from_context
 token = get_token_from_context()
 ```
 
 This works in async calls but not in sub threads (without additional changes).
 
 See:
 * https://docs.python.org/3/library/contextvars.html
@@ -85,12 +86,40 @@
 console_handler = logging.StreamHandler(sys.stdout)
 console_handler.addFilter(UserNameLoggingFilter())
 
 ```
 
 The filter provides the following two fields as soon as the user is authenticated: user_name, authorized_party
 
+### How a token has to look like
+
+```json
+{
+
+    "iss": "https://authserver.com/auth/realms/projectName",
+    "aud": ["audienceOne", "audienceTwo"],
+    "typ": "Bearer",
+    "azp": "public-project-swagger",
+    "preferred_username": "preferredUsernameValue",
+    .....
+    "realm_access": {
+        "roles": ["myRealmRoleOne"]
+    },
+    "resource_access": {
+        "my-client-one": {
+            "roles": ["a-permission-role", "user"]
+        },
+        "my-client-two": {
+            "roles": ["a-permission-role", "admin"]
+        }
+    }
+}
+```
+
+* realm_access contains the realm roles
+* resource_access contains the token roles for one or multiple clients
+
 ## How to publish
 
 * Update the version in setup.py and commit your change
 * Create a tag with the same version number
 * Let github do the rest
```

### Comparing `sag-py-auth-0.1.3/sag_py_auth/jwt_auth.py` & `sag-py-auth-0.1.4/sag_py_auth/jwt_auth.py`

 * *Files 2% similar despite different names*

```diff
@@ -71,12 +71,12 @@
             self._raise_auth_error(HTTP_403_FORBIDDEN, "Missing role.")
 
     def _verify_realm_roles(self, token: Optional[Token]) -> None:
         token_realm_roles: List[str] = token.get_realm_roles() if token is not None else []
         has_all_realm_roles: bool = all(realm_role in token_realm_roles for realm_role in self.required_realm_roles)
 
         if not has_all_realm_roles:
-            logger.warning("User requires realm roles '%s'", self.required_roles)
+            logger.warning("User requires realm roles '%s'", self.required_realm_roles)
             self._raise_auth_error(HTTP_403_FORBIDDEN, "Missing realm role.")
 
     def _raise_auth_error(self, status_code: int, detail: str) -> NoReturn:
         raise HTTPException(status_code=status_code, detail=detail, headers={"WWW-Authenticate": "Bearer"})
```

### Comparing `sag-py-auth-0.1.3/sag_py_auth/models.py` & `sag-py-auth-0.1.4/sag_py_auth/models.py`

 * *Files 6% similar despite different names*

```diff
@@ -70,11 +70,14 @@
     Define required token auth roles
     """
 
     def __init__(self, client: str, role: str) -> None:
         self.client: str = client
         self.role: str = role
 
+    def __repr__(self) -> str:
+        return f"{self.client}.{self.role}"
+
 
 class UserInfoLogRecord(LogRecord):
     user_name: str
     authorized_party: str
```

### Comparing `sag-py-auth-0.1.3/sag_py_auth/token_decoder.py` & `sag-py-auth-0.1.4/sag_py_auth/token_decoder.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/sag_py_auth/user_name_logging_filter.py` & `sag-py-auth-0.1.4/sag_py_auth/user_name_logging_filter.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/sag_py_auth.egg-info/PKG-INFO` & `sag-py-auth-0.1.4/sag_py_auth.egg-info/PKG-INFO`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sag-py-auth
-Version: 0.1.3
+Version: 0.1.4
 Summary: Keycloak authentication for python projects
 Home-page: https://github.com/SamhammerAG/sag_py_auth
 Author: Samhammer AG
 Author-email: support@samhammer.de
 License: MIT
 Project-URL: Documentation, https://github.com/SamhammerAG/sag_py_auth
 Project-URL: Bug Reports, https://github.com/SamhammerAG/sag_py_auth/issues
@@ -39,21 +39,22 @@
 * Verifies auth tokens: signature, expiration, issuer, audience
 * Allows to set permissions by specifying roles and realm roles
 
 ## How to use
 
 ### Installation
 
-pip install sag_py_auth
+pip install sag-py-auth
 
 ### Secure your apis
 
 First create the fast api dependency with the auth config:
 ```python
-from sag_py_auth import AuthConfig, JwtAuth, TokenRole
+from sag_py_auth.models import AuthConfig, TokenRole
+from sag_py_auth.jwt_auth import JwtAuth
 from fastapi import Depends
 
 auth_config = AuthConfig("https://authserver.com/auth/realms/projectName", "myaudience")
 required_roles = [TokenRole("clientname", "adminrole")]
 required_realm_roles = ["additionalrealmrole"]
 requires_admin = Depends(JwtAuth(auth_config, required_roles, required_realm_roles))
 ```
@@ -74,15 +75,15 @@
 
 ### Get user information
 
 The Jwt call directly returns a token object that can be used to get additional information.
 
 Furthermore you can access the context directly:
 ```python
-from sag_py_auth import get_token as get_token_from_context
+from sag_py_auth.auth_context import get_token as get_token_from_context
 token = get_token_from_context()
 ```
 
 This works in async calls but not in sub threads (without additional changes).
 
 See:
 * https://docs.python.org/3/library/contextvars.html
@@ -108,12 +109,40 @@
 console_handler = logging.StreamHandler(sys.stdout)
 console_handler.addFilter(UserNameLoggingFilter())
 
 ```
 
 The filter provides the following two fields as soon as the user is authenticated: user_name, authorized_party
 
+### How a token has to look like
+
+```json
+{
+
+    "iss": "https://authserver.com/auth/realms/projectName",
+    "aud": ["audienceOne", "audienceTwo"],
+    "typ": "Bearer",
+    "azp": "public-project-swagger",
+    "preferred_username": "preferredUsernameValue",
+    .....
+    "realm_access": {
+        "roles": ["myRealmRoleOne"]
+    },
+    "resource_access": {
+        "my-client-one": {
+            "roles": ["a-permission-role", "user"]
+        },
+        "my-client-two": {
+            "roles": ["a-permission-role", "admin"]
+        }
+    }
+}
+```
+
+* realm_access contains the realm roles
+* resource_access contains the token roles for one or multiple clients
+
 ## How to publish
 
 * Update the version in setup.py and commit your change
 * Create a tag with the same version number
 * Let github do the rest
```

### Comparing `sag-py-auth-0.1.3/sag_py_auth.egg-info/SOURCES.txt` & `sag-py-auth-0.1.4/sag_py_auth.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/setup.py` & `sag-py-auth-0.1.4/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     LONG_DESCRIPTION = fh.read()
 
 with open("requirements.txt", "r") as fin:
     REQS = fin.read().splitlines()
 
 setuptools.setup(
     name="sag-py-auth",
-    version="0.1.3",
+    version="0.1.4",
     description="Keycloak authentication for python projects",
     long_description=LONG_DESCRIPTION,
     long_description_content_type="text/markdown",
     url="https://github.com/SamhammerAG/sag_py_auth",
     author="Samhammer AG",
     author_email="support@samhammer.de",
     license="MIT",
```

### Comparing `sag-py-auth-0.1.3/tests/test_auth_context.py` & `sag-py-auth-0.1.4/tests/test_auth_context.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_jwt_auth__call.py` & `sag-py-auth-0.1.4/tests/test_jwt_auth__call.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_jwt_auth__init.py` & `sag-py-auth-0.1.4/tests/test_jwt_auth__init.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_jwt_auth__realm_roles.py` & `sag-py-auth-0.1.4/tests/test_jwt_auth__realm_roles.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_jwt_auth__roles.py` & `sag-py-auth-0.1.4/tests/test_jwt_auth__roles.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_jwt_auth__verify_and_decode_token.py` & `sag-py-auth-0.1.4/tests/test_jwt_auth__verify_and_decode_token.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_models.py` & `sag-py-auth-0.1.4/tests/test_models.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_token_decoder.py` & `sag-py-auth-0.1.4/tests/test_token_decoder.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_user_name_logging_filter.py` & `sag-py-auth-0.1.4/tests/test_user_name_logging_filter.py`

 * *Files identical despite different names*

### Comparing `sag-py-auth-0.1.3/tests/test_utils.py` & `sag-py-auth-0.1.4/tests/test_utils.py`

 * *Files identical despite different names*

