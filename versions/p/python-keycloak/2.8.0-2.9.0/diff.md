# Comparing `tmp/python_keycloak-2.8.0.tar.gz` & `tmp/python_keycloak-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python_keycloak-2.8.0.tar", max compression
+gzip compressed data, was "python_keycloak-2.9.0.tar", max compression
```

## Comparing `python_keycloak-2.8.0.tar` & `python_keycloak-2.9.0.tar`

### file list

```diff
@@ -1,20 +1,20 @@
--rw-r--r--   0        0        0     4044 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/CHANGELOG.md
--rw-r--r--   0        0        0       30 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/CODEOWNERS
--rw-r--r--   0        0        0     3192 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/CONTRIBUTING.md
--rw-r--r--   0        0        0     1111 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/LICENSE
--rw-r--r--   0        0        0    13438 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/README.md
--rw-r--r--   0        0        0     2308 2022-12-29 06:37:01.264939 python_keycloak-2.8.0/pyproject.toml
--rw-r--r--   0        0        0     2230 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/__init__.py
--rw-r--r--   0        0        0     1268 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/_version.py
--rw-r--r--   0        0        0     3687 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/authorization/__init__.py
--rw-r--r--   0        0        0     4421 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/authorization/permission.py
--rw-r--r--   0        0        0     5252 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/authorization/policy.py
--rw-r--r--   0        0        0     2306 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/authorization/role.py
--rw-r--r--   0        0        0     8873 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/connection.py
--rw-r--r--   0        0        0     5464 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/exceptions.py
--rw-r--r--   0        0        0   140344 2022-12-29 06:35:54.096117 python_keycloak-2.8.0/src/keycloak/keycloak_admin.py
--rw-r--r--   0        0        0    23990 2022-12-29 06:35:54.100117 python_keycloak-2.8.0/src/keycloak/keycloak_openid.py
--rw-r--r--   0        0        0     8769 2022-12-29 06:35:54.100117 python_keycloak-2.8.0/src/keycloak/uma_permissions.py
--rw-r--r--   0        0        0    10645 2022-12-29 06:35:54.100117 python_keycloak-2.8.0/src/keycloak/urls_patterns.py
--rw-r--r--   0        0        0    15226 1970-01-01 00:00:00.000000 python_keycloak-2.8.0/setup.py
--rw-r--r--   0        0        0    15283 1970-01-01 00:00:00.000000 python_keycloak-2.8.0/PKG-INFO
+-rw-r--r--   0        0        0     4303 2023-01-11 11:16:19.797310 python_keycloak-2.9.0/CHANGELOG.md
+-rw-r--r--   0        0        0       30 2023-01-11 11:16:19.797310 python_keycloak-2.9.0/CODEOWNERS
+-rw-r--r--   0        0        0     3192 2023-01-11 11:16:19.797310 python_keycloak-2.9.0/CONTRIBUTING.md
+-rw-r--r--   0        0        0     1111 2023-01-11 11:16:19.797310 python_keycloak-2.9.0/LICENSE
+-rw-r--r--   0        0        0    13438 2023-01-11 11:16:19.797310 python_keycloak-2.9.0/README.md
+-rw-r--r--   0        0        0     2308 2023-01-11 11:17:02.808800 python_keycloak-2.9.0/pyproject.toml
+-rw-r--r--   0        0        0     2230 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/__init__.py
+-rw-r--r--   0        0        0     1268 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/_version.py
+-rw-r--r--   0        0        0     3687 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/authorization/__init__.py
+-rw-r--r--   0        0        0     4421 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/authorization/permission.py
+-rw-r--r--   0        0        0     5252 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/authorization/policy.py
+-rw-r--r--   0        0        0     2306 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/authorization/role.py
+-rw-r--r--   0        0        0     8873 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/connection.py
+-rw-r--r--   0        0        0     5464 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/exceptions.py
+-rw-r--r--   0        0        0   142430 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/keycloak_admin.py
+-rw-r--r--   0        0        0    23990 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/keycloak_openid.py
+-rw-r--r--   0        0        0     8769 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/uma_permissions.py
+-rw-r--r--   0        0        0    10791 2023-01-11 11:16:19.801310 python_keycloak-2.9.0/src/keycloak/urls_patterns.py
+-rw-r--r--   0        0        0    15226 1970-01-01 00:00:00.000000 python_keycloak-2.9.0/setup.py
+-rw-r--r--   0        0        0    15283 1970-01-01 00:00:00.000000 python_keycloak-2.9.0/PKG-INFO
```

### Comparing `python_keycloak-2.8.0/CHANGELOG.md` & `python_keycloak-2.9.0/CHANGELOG.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,21 @@
+## v2.8.0 (2022-12-29)
+
+### Feat
+
+- **api**: add tests for create_authz_scopes
+
+### Fix
+
+- fix testing create_client_authz_scopes parameters
+- fix linting
+- add testcase for invalid client id
+- create authz clients test case
+- create authz clients test case
+
 ## v2.7.0 (2022-12-24)
 
 ### Refactor
 
 - code formatting after tox checks
 - remove print statements
```

### Comparing `python_keycloak-2.8.0/CONTRIBUTING.md` & `python_keycloak-2.9.0/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/LICENSE` & `python_keycloak-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/README.md` & `python_keycloak-2.9.0/README.md`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/pyproject.toml` & `python_keycloak-2.9.0/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "python-keycloak"
-version = "v2.8.0"
+version = "v2.9.0"
 description = "python-keycloak is a Python package providing access to the Keycloak API."
 license = "MIT"
 readme = "README.md"
 keywords = [ "keycloak", "openid", "oidc" ]
 authors = [
     "Marcos Pereira <marcospereira.mpj@gmail.com>",
     "Richard Nemeth <ryshoooo@gmail.com>"
```

### Comparing `python_keycloak-2.8.0/src/keycloak/__init__.py` & `python_keycloak-2.9.0/src/keycloak/__init__.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/_version.py` & `python_keycloak-2.9.0/src/keycloak/_version.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/authorization/__init__.py` & `python_keycloak-2.9.0/src/keycloak/authorization/__init__.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/authorization/permission.py` & `python_keycloak-2.9.0/src/keycloak/authorization/permission.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/authorization/policy.py` & `python_keycloak-2.9.0/src/keycloak/authorization/policy.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/authorization/role.py` & `python_keycloak-2.9.0/src/keycloak/authorization/role.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/connection.py` & `python_keycloak-2.9.0/src/keycloak/connection.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/exceptions.py` & `python_keycloak-2.9.0/src/keycloak/exceptions.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/keycloak_admin.py` & `python_keycloak-2.9.0/src/keycloak/keycloak_admin.py`

 * *Files 1% similar despite different names*

```diff
@@ -984,15 +984,15 @@
         :rtype: bytes
         """
         params_path = {"realm-name": self.realm_name, "id": user_id}
         params_query = {"client_id": client_id, "lifespan": lifespan, "redirect_uri": redirect_uri}
         data_raw = self.raw_put(
             urls_patterns.URL_ADMIN_SEND_UPDATE_ACCOUNT.format(**params_path),
             data=json.dumps(payload),
-            **params_query
+            **params_query,
         )
         return raise_error_from_response(data_raw, KeycloakPutError)
 
     def send_verify_email(self, user_id, client_id=None, redirect_uri=None):
         """Send a update account email to the user.
 
         An email contains a link the user can click to perform a set of required actions.
@@ -1008,15 +1008,15 @@
         :rtype: bytes
         """
         params_path = {"realm-name": self.realm_name, "id": user_id}
         params_query = {"client_id": client_id, "redirect_uri": redirect_uri}
         data_raw = self.raw_put(
             urls_patterns.URL_ADMIN_SEND_VERIFY_EMAIL.format(**params_path),
             data={},
-            **params_query
+            **params_query,
         )
         return raise_error_from_response(data_raw, KeycloakPutError)
 
     def get_sessions(self, user_id):
         """Get sessions associated with the user.
 
         UserSessionRepresentation
@@ -1653,14 +1653,70 @@
         """
         query = query or dict()
         params_path = {"realm-name": self.realm_name, "role-name": role_name}
         return self.__fetch_all(
             urls_patterns.URL_ADMIN_REALM_ROLES_MEMBERS.format(**params_path), query
         )
 
+    def get_default_realm_role_id(self):
+        """Get the ID of the default realm role.
+
+        :return: Realm role ID
+        :rtype: str
+        """
+        all_realm_roles = self.get_realm_roles()
+        default_realm_roles = [
+            realm_role
+            for realm_role in all_realm_roles
+            if realm_role["name"] == f"default-roles-{self.realm_name}"
+        ]
+        return default_realm_roles[0]["id"]
+
+    def get_realm_default_roles(self):
+        """Get all the default realm roles.
+
+        :return: Keycloak Server Response (UserRepresentation)
+        :rtype: list
+        """
+        params_path = {"realm-name": self.realm_name, "role-id": self.get_default_realm_role_id()}
+        data_raw = self.raw_get(
+            urls_patterns.URL_ADMIN_REALM_ROLE_COMPOSITES_REALM.format(**params_path)
+        )
+        return raise_error_from_response(data_raw, KeycloakGetError)
+
+    def remove_realm_default_roles(self, payload):
+        """Remove a set of default realm roles.
+
+        :param payload: List of RoleRepresentations
+        :type payload: list
+        :return: Keycloak Server Response
+        :rtype: dict
+        """
+        params_path = {"realm-name": self.realm_name, "role-id": self.get_default_realm_role_id()}
+        data_raw = self.raw_delete(
+            urls_patterns.URL_ADMIN_REALM_ROLE_COMPOSITES.format(**params_path),
+            data=json.dumps(payload),
+        )
+        return raise_error_from_response(data_raw, KeycloakDeleteError)
+
+    def add_realm_default_roles(self, payload):
+        """Add a set of default realm roles.
+
+        :param payload: List of RoleRepresentations
+        :type payload: list
+        :return: Keycloak Server Response
+        :rtype: dict
+        """
+        params_path = {"realm-name": self.realm_name, "role-id": self.get_default_realm_role_id()}
+        data_raw = self.raw_post(
+            urls_patterns.URL_ADMIN_REALM_ROLE_COMPOSITES.format(**params_path),
+            data=json.dumps(payload),
+        )
+        return raise_error_from_response(data_raw, KeycloakPostError)
+
     def get_client_roles(self, client_id, brief_representation=True):
         """Get all roles for the client.
 
         RoleRepresentation
         https://www.keycloak.org/docs-api/18.0/rest-api/index.html#_rolerepresentation
 
         :param client_id: id of client (not client-id)
@@ -2660,15 +2716,15 @@
         data = {"action": action}
         params_query = {"action": action}
 
         params_path = {"realm-name": self.realm_name, "id": storage_id}
         data_raw = self.raw_post(
             urls_patterns.URL_ADMIN_USER_STORAGE.format(**params_path),
             data=json.dumps(data),
-            **params_query
+            **params_query,
         )
         return raise_error_from_response(data_raw, KeycloakPostError)
 
     def get_client_scopes(self):
         """Get client scopes.
 
         Get representation of the client scopes for the realm where we are connected to
```

### Comparing `python_keycloak-2.8.0/src/keycloak/keycloak_openid.py` & `python_keycloak-2.9.0/src/keycloak/keycloak_openid.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/uma_permissions.py` & `python_keycloak-2.9.0/src/keycloak/uma_permissions.py`

 * *Files identical despite different names*

### Comparing `python_keycloak-2.8.0/src/keycloak/urls_patterns.py` & `python_keycloak-2.9.0/src/keycloak/urls_patterns.py`

 * *Files 2% similar despite different names*

```diff
@@ -185,17 +185,17 @@
 )
 
 URL_ADMIN_EVENTS = "admin/realms/{realm-name}/events"
 URL_ADMIN_EVENTS_CONFIG = URL_ADMIN_EVENTS + "/config"
 URL_ADMIN_CLIENT_SESSION_STATS = "admin/realms/{realm-name}/client-session-stats"
 
 URL_ADMIN_GROUPS_CLIENT_ROLES_COMPOSITE = URL_ADMIN_GROUPS_CLIENT_ROLES + "/composite"
-URL_ADMIN_CLIENT_ROLE_CHILDREN = (
-    "admin/realms/{realm-name}/roles-by-id/{role-id}/composites/clients/{client-id}"
-)
+URL_ADMIN_REALM_ROLE_COMPOSITES = "admin/realms/{realm-name}/roles-by-id/{role-id}/composites"
+URL_ADMIN_REALM_ROLE_COMPOSITES_REALM = URL_ADMIN_REALM_ROLE_COMPOSITES + "/realm"
+URL_ADMIN_CLIENT_ROLE_CHILDREN = URL_ADMIN_REALM_ROLE_COMPOSITES + "/clients/{client-id}"
 URL_ADMIN_CLIENT_CERT_UPLOAD = URL_ADMIN_CLIENT_CERTS + "/upload-certificate"
 URL_ADMIN_REQUIRED_ACTIONS = URL_ADMIN_REALM + "/authentication/required-actions"
 URL_ADMIN_REQUIRED_ACTIONS_ALIAS = URL_ADMIN_REQUIRED_ACTIONS + "/{action-alias}"
 
 URL_ADMIN_ATTACK_DETECTION = "admin/realms/{realm-name}/attack-detection/brute-force/users"
 URL_ADMIN_ATTACK_DETECTION_USER = (
     "admin/realms/{realm-name}/attack-detection/brute-force/users/{id}"
```

### Comparing `python_keycloak-2.8.0/setup.py` & `python_keycloak-2.9.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,15 @@
           'sphinx-rtd-theme>=1.0.0,<2.0.0',
           'readthedocs-sphinx-ext>=2.1.9,<3.0.0',
           'm2r2>=0.3.2,<0.4.0',
           'sphinx-autoapi>=2.0.0,<3.0.0']}
 
 setup_kwargs = {
     'name': 'python-keycloak',
-    'version': '2.8.0',
+    'version': '2.9.0',
     'description': 'python-keycloak is a Python package providing access to the Keycloak API.',
     'long_description': '[![CircleCI](https://github.com/marcospereirampj/python-keycloak/actions/workflows/daily.yaml/badge.svg)](https://github.com/marcospereirampj/python-keycloak/)\n[![Documentation Status](https://readthedocs.org/projects/python-keycloak/badge/?version=latest)](http://python-keycloak.readthedocs.io/en/latest/?badge=latest)\n\n# Python Keycloak\n\nFor review- see https://github.com/marcospereirampj/python-keycloak\n\n**python-keycloak** is a Python package providing access to the Keycloak API.\n\n## Installation\n\n### Via Pypi Package:\n\n`$ pip install python-keycloak`\n\n### Manually\n\n`$ python setup.py install`\n\n## Dependencies\n\npython-keycloak depends on:\n\n- Python 3\n- [requests](https://requests.readthedocs.io)\n- [python-jose](http://python-jose.readthedocs.io/en/latest/)\n- [urllib3](https://urllib3.readthedocs.io/en/stable/)\n\n### Tests Dependencies\n\n- [tox](https://tox.readthedocs.io/)\n- [pytest](https://docs.pytest.org/en/latest/)\n- [pytest-cov](https://github.com/pytest-dev/pytest-cov)\n- [wheel](https://github.com/pypa/wheel)\n\n## Bug reports\n\nPlease report bugs and feature requests at\nhttps://github.com/marcospereirampj/python-keycloak/issues\n\n## Documentation\n\nThe documentation for python-keycloak is available on [readthedocs](http://python-keycloak.readthedocs.io).\n\n## Contributors\n\n- [Agriness Team](http://www.agriness.com/pt/)\n- [Marcos Pereira](marcospereira.mpj@gmail.com)\n- [Martin Devlin](https://bitbucket.org/devlinmpearson/)\n- [Shon T. Urbas](https://bitbucket.org/surbas/)\n- [Markus Spanier](https://bitbucket.org/spanierm/)\n- [Remco Kranenburg](https://bitbucket.org/Remco47/)\n- [Armin](https://bitbucket.org/arminfelder/)\n- [njordr](https://bitbucket.org/njordr/)\n- [Josha Inglis](https://bitbucket.org/joshainglis/)\n- [Alex](https://bitbucket.org/alex_zel/)\n- [Ewan Jone](https://bitbucket.org/kisamoto/)\n- [Lukas Martini](https://github.com/lutoma)\n- [Adamatics](https://www.adamatics.com)\n\n## Usage\n\n```python\nfrom keycloak import KeycloakOpenID\n\n# Configure client\nkeycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/auth/",\n                                 client_id="example_client",\n                                 realm_name="example_realm",\n                                 client_secret_key="secret")\n\n# Get WellKnow\nconfig_well_known = keycloak_openid.well_known()\n\n# Get Code With Oauth Authorization Request\nauth_url = keycloak_openid.auth_url(\n    redirect_uri="your_call_back_url",\n    scope="email",\n    state="your_state_info")\n\n# Get Access Token With Code\naccess_token = keycloak_openid.token(\n    grant_type=\'authorization_code\',\n    code=\'the_code_you_get_from_auth_url_callback\',\n    redirect_uri="your_call_back_url")\n\n\n# Get Token\ntoken = keycloak_openid.token("user", "password")\ntoken = keycloak_openid.token("user", "password", totp="012345")\n\n# Get token using Token Exchange\ntoken = keycloak_openid.exchange_token(token[\'access_token\'], "my_client", "other_client", "some_user")\n\n# Get Userinfo\nuserinfo = keycloak_openid.userinfo(token[\'access_token\'])\n\n# Refresh token\ntoken = keycloak_openid.refresh_token(token[\'refresh_token\'])\n\n# Logout\nkeycloak_openid.logout(token[\'refresh_token\'])\n\n# Get Certs\ncerts = keycloak_openid.certs()\n\n# Get RPT (Entitlement)\ntoken = keycloak_openid.token("user", "password")\nrpt = keycloak_openid.entitlement(token[\'access_token\'], "resource_id")\n\n# Instropect RPT\ntoken_rpt_info = keycloak_openid.introspect(keycloak_openid.introspect(token[\'access_token\'], rpt=rpt[\'rpt\'],\n                                                                       token_type_hint="requesting_party_token"))\n\n# Introspect Token\ntoken_info = keycloak_openid.introspect(token[\'access_token\'])\n\n# Decode Token\nKEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\\n" + keycloak_openid.public_key() + "\\n-----END PUBLIC KEY-----"\noptions = {"verify_signature": True, "verify_aud": True, "verify_exp": True}\ntoken_info = keycloak_openid.decode_token(token[\'access_token\'], key=KEYCLOAK_PUBLIC_KEY, options=options)\n\n# Get permissions by token\ntoken = keycloak_openid.token("user", "password")\nkeycloak_openid.load_authorization_config("example-authz-config.json")\npolicies = keycloak_openid.get_policies(token[\'access_token\'], method_token_info=\'decode\', key=KEYCLOAK_PUBLIC_KEY)\npermissions = keycloak_openid.get_permissions(token[\'access_token\'], method_token_info=\'introspect\')\n\n# Get UMA-permissions by token\ntoken = keycloak_openid.token("user", "password")\npermissions = keycloak_openid.uma_permissions(token[\'access_token\'])\n\n# Get UMA-permissions by token with specific resource and scope requested\ntoken = keycloak_openid.token("user", "password")\npermissions = keycloak_openid.uma_permissions(token[\'access_token\'], permissions="Resource#Scope")\n\n# Get auth status for a specific resource and scope by token\ntoken = keycloak_openid.token("user", "password")\nauth_status = keycloak_openid.has_uma_access(token[\'access_token\'], "Resource#Scope")\n\n\n# KEYCLOAK ADMIN\n\nfrom keycloak import KeycloakAdmin\n\nkeycloak_admin = KeycloakAdmin(server_url="http://localhost:8080/auth/",\n                               username=\'example-admin\',\n                               password=\'secret\',\n                               realm_name="master",\n                               user_realm_name="only_if_other_realm_than_master",\n                               client_secret_key="client-secret",\n                               verify=True)\n\n# Add user\nnew_user = keycloak_admin.create_user({"email": "example@example.com",\n                                       "username": "example@example.com",\n                                       "enabled": True,\n                                       "firstName": "Example",\n                                       "lastName": "Example"})\n\n# Add user and raise exception if username already exists\n# exist_ok currently defaults to True for backwards compatibility reasons\nnew_user = keycloak_admin.create_user({"email": "example@example.com",\n                                       "username": "example@example.com",\n                                       "enabled": True,\n                                       "firstName": "Example",\n                                       "lastName": "Example"},\n                                      exist_ok=False)\n\n# Add user and set password\nnew_user = keycloak_admin.create_user({"email": "example@example.com",\n                                       "username": "example@example.com",\n                                       "enabled": True,\n                                       "firstName": "Example",\n                                       "lastName": "Example",\n                    "credentials": [{"value": "secret","type": "password",}]})\n\n# Add user and specify a locale\nnew_user = keycloak_admin.create_user({"email": "example@example.fr",\n                                       "username": "example@example.fr",\n                                       "enabled": True,\n                                       "firstName": "Example",\n                                       "lastName": "Example",\n                                       "attributes": {\n                                           "locale": ["fr"]\n                                       }})\n\n# User counter\ncount_users = keycloak_admin.users_count()\n\n# Get users Returns a list of users, filtered according to query parameters\nusers = keycloak_admin.get_users({})\n\n# Get user ID from username\nuser_id_keycloak = keycloak_admin.get_user_id("username-keycloak")\n\n# Get User\nuser = keycloak_admin.get_user("user-id-keycloak")\n\n# Update User\nresponse = keycloak_admin.update_user(user_id="user-id-keycloak",\n                                      payload={\'firstName\': \'Example Update\'})\n\n# Update User Password\nresponse = keycloak_admin.set_user_password(user_id="user-id-keycloak", password="secret", temporary=True)\n\n# Get User Credentials\ncredentials = keycloak_admin.get_credentials(user_id=\'user_id\')\n\n# Get User Credential by ID\ncredential = keycloak_admin.get_credential(user_id=\'user_id\', credential_id=\'credential_id\')\n\n# Delete User Credential\nresponse = keycloak_admin.delete_credential(user_id=\'user_id\', credential_id=\'credential_id\')\n\n# Delete User\nresponse = keycloak_admin.delete_user(user_id="user-id-keycloak")\n\n# Get consents granted by the user\nconsents = keycloak_admin.consents_user(user_id="user-id-keycloak")\n\n# Send User Action\nresponse = keycloak_admin.send_update_account(user_id="user-id-keycloak",\n                                              payload=[\'UPDATE_PASSWORD\'])\n\n# Send Verify Email\nresponse = keycloak_admin.send_verify_email(user_id="user-id-keycloak")\n\n# Get sessions associated with the user\nsessions = keycloak_admin.get_sessions(user_id="user-id-keycloak")\n\n# Get themes, social providers, auth providers, and event listeners available on this server\nserver_info = keycloak_admin.get_server_info()\n\n# Get clients belonging to the realm Returns a list of clients belonging to the realm\nclients = keycloak_admin.get_clients()\n\n# Get client - id (not client-id) from client by name\nclient_id = keycloak_admin.get_client_id("my-client")\n\n# Get representation of the client - id of client (not client-id)\nclient = keycloak_admin.get_client(client_id="client_id")\n\n# Get all roles for the realm or client\nrealm_roles = keycloak_admin.get_realm_roles()\n\n# Get all roles for the client\nclient_roles = keycloak_admin.get_client_roles(client_id="client_id")\n\n# Get client role\nrole = keycloak_admin.get_client_role(client_id="client_id", role_name="role_name")\n\n# Warning: Deprecated\n# Get client role id from name\nrole_id = keycloak_admin.get_client_role_id(client_id="client_id", role_name="test")\n\n# Create client role\nkeycloak_admin.create_client_role(client_role_id=\'client_id\', payload={\'name\': \'roleName\', \'clientRole\': True})\n\n# Assign client role to user. Note that BOTH role_name and role_id appear to be required.\nkeycloak_admin.assign_client_role(client_id="client_id", user_id="user_id", role_id="role_id", role_name="test")\n\n# Retrieve client roles of a user.\nkeycloak_admin.get_client_roles_of_user(user_id="user_id", client_id="client_id")\n\n# Retrieve available client roles of a user.\nkeycloak_admin.get_available_client_roles_of_user(user_id="user_id", client_id="client_id")\n\n# Retrieve composite client roles of a user.\nkeycloak_admin.get_composite_client_roles_of_user(user_id="user_id", client_id="client_id")\n\n# Delete client roles of a user.\nkeycloak_admin.delete_client_roles_of_user(client_id="client_id", user_id="user_id", roles={"id": "role-id"})\nkeycloak_admin.delete_client_roles_of_user(client_id="client_id", user_id="user_id", roles=[{"id": "role-id_1"}, {"id": "role-id_2"}])\n\n# Get all client authorization resources\nclient_resources = get_client_authz_resources(client_id="client_id")\n\n# Get all client authorization scopes\nclient_scopes = get_client_authz_scopes(client_id="client_id")\n\n# Get all client authorization permissions\nclient_permissions = get_client_authz_permissions(client_id="client_id")\n\n# Get all client authorization policies\nclient_policies = get_client_authz_policies(client_id="client_id")\n\n# Create new group\ngroup = keycloak_admin.create_group({"name": "Example Group"})\n\n# Get all groups\ngroups = keycloak_admin.get_groups()\n\n# Get group\ngroup = keycloak_admin.get_group(group_id=\'group_id\')\n\n# Get group by name\ngroup = keycloak_admin.get_group_by_path(path=\'/group/subgroup\', search_in_subgroups=True)\n\n# Function to trigger user sync from provider\nsync_users(storage_id="storage_di", action="action")\n\n# Get client role id from name\nrole_id = keycloak_admin.get_client_role_id(client_id=client_id, role_name="test")\n\n# Get all roles for the realm or client\nrealm_roles = keycloak_admin.get_roles()\n\n# Assign client role to user. Note that BOTH role_name and role_id appear to be required.\nkeycloak_admin.assign_client_role(client_id=client_id, user_id=user_id, role_id=role_id, role_name="test")\n\n# Assign realm roles to user\nkeycloak_admin.assign_realm_roles(user_id=user_id, roles=realm_roles)\n\n# Assign realm roles to client\'s scope\nkeycloak_admin.assign_realm_roles_to_client_scope(client_id=client_id, roles=realm_roles)\n\n# Get realm roles assigned to client\'s scope\nkeycloak_admin.get_realm_roles_of_client_scope(client_id=client_id)\n\n# Remove realm roles assigned to client\'s scope\nkeycloak_admin.delete_realm_roles_of_client_scope(client_id=client_id, roles=realm_roles)\n\nanother_client_id = keycloak_admin.get_client_id("my-client-2")\n\n# Assign client roles to client\'s scope\nkeycloak_admin.assign_client_roles_to_client_scope(client_id=another_client_id, client_roles_owner_id=client_id, roles=client_roles)\n\n# Get client roles assigned to client\'s scope\nkeycloak_admin.get_client_roles_of_client_scope(client_id=another_client_id, client_roles_owner_id=client_id)\n\n# Remove client roles assigned to client\'s scope\nkeycloak_admin.delete_client_roles_of_client_scope(client_id=another_client_id, client_roles_owner_id=client_id, roles=client_roles)\n\n# Get all ID Providers\nidps = keycloak_admin.get_idps()\n\n# Create a new Realm\nkeycloak_admin.create_realm(payload={"realm": "demo"}, skip_exists=False)\n\n# Changing Realm\nkeycloak_admin = KeycloakAdmin(realm_name="main", ...)\nkeycloak_admin.get_users() # Get user in main realm\nkeycloak_admin.realm_name = "demo" # Change realm to \'demo\'\nkeycloak_admin.get_users() # Get users in realm \'demo\'\nkeycloak_admin.create_user(...) # Creates a new user in \'demo\'\n```\n',
     'author': 'Marcos Pereira',
     'author_email': 'marcospereira.mpj@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `python_keycloak-2.8.0/PKG-INFO` & `python_keycloak-2.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-keycloak
-Version: 2.8.0
+Version: 2.9.0
 Summary: python-keycloak is a Python package providing access to the Keycloak API.
 License: MIT
 Keywords: keycloak,openid,oidc
 Author: Marcos Pereira
 Author-email: marcospereira.mpj@gmail.com
 Requires-Python: >=3.7,<4.0
 Classifier: Development Status :: 3 - Alpha
```

