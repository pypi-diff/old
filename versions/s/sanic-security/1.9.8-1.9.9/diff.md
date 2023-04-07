# Comparing `tmp/sanic-security-1.9.8.tar.gz` & `tmp/sanic-security-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sanic-security-1.9.8.tar", last modified: Mon Jan 30 21:38:17 2023, max compression
+gzip compressed data, was "sanic-security-1.9.9.tar", last modified: Wed Feb  1 19:03:16 2023, max compression
```

## Comparing `sanic-security-1.9.8.tar` & `sanic-security-1.9.9.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxrwxrwx   0        0        0        0 2023-01-30 21:38:17.119185 sanic-security-1.9.8/
--rw-rw-rw-   0        0        0    35188 2022-09-09 12:39:26.000000 sanic-security-1.9.8/LICENSE
--rw-rw-rw-   0        0        0       92 2022-09-09 12:39:26.000000 sanic-security-1.9.8/MANIFEST.in
--rw-rw-rw-   0        0        0    19177 2023-01-30 21:38:17.111186 sanic-security-1.9.8/PKG-INFO
--rw-rw-rw-   0        0        0    18700 2023-01-30 21:21:55.000000 sanic-security-1.9.8/README.md
-drwxrwxrwx   0        0        0        0 2023-01-30 21:38:17.103187 sanic-security-1.9.8/sanic_security/
--rw-rw-rw-   0        0        0        0 2022-09-09 12:39:26.000000 sanic-security-1.9.8/sanic_security/__init__.py
--rw-rw-rw-   0        0        0     9482 2023-01-30 20:11:41.000000 sanic-security-1.9.8/sanic_security/authentication.py
--rw-rw-rw-   0        0        0     6559 2023-01-30 20:11:41.000000 sanic-security-1.9.8/sanic_security/authorization.py
--rw-rw-rw-   0        0        0     5145 2022-10-27 20:58:41.000000 sanic-security-1.9.8/sanic_security/configuration.py
--rw-rw-rw-   0        0        0     3937 2023-01-30 21:24:25.000000 sanic-security-1.9.8/sanic_security/exceptions.py
--rw-rw-rw-   0        0        0    17480 2023-01-30 21:35:42.000000 sanic-security-1.9.8/sanic_security/models.py
-drwxrwxrwx   0        0        0        0 2023-01-30 21:38:17.111186 sanic-security-1.9.8/sanic_security/test/
--rw-rw-rw-   0        0        0        0 2022-09-09 12:39:26.000000 sanic-security-1.9.8/sanic_security/test/__init__.py
--rw-rw-rw-   0        0        0     9613 2022-09-16 17:11:36.000000 sanic-security-1.9.8/sanic_security/test/server.py
--rw-rw-rw-   0        0        0    16624 2023-01-30 20:11:41.000000 sanic-security-1.9.8/sanic_security/test/tests.py
--rw-rw-rw-   0        0        0     2314 2022-09-16 15:06:09.000000 sanic-security-1.9.8/sanic_security/utils.py
--rw-rw-rw-   0        0        0     7115 2023-01-30 20:11:41.000000 sanic-security-1.9.8/sanic_security/verification.py
-drwxrwxrwx   0        0        0        0 2023-01-30 21:38:17.111186 sanic-security-1.9.8/sanic_security.egg-info/
--rw-rw-rw-   0        0        0    19177 2023-01-30 21:38:17.000000 sanic-security-1.9.8/sanic_security.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      551 2023-01-30 21:38:17.000000 sanic-security-1.9.8/sanic_security.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-01-30 21:38:17.000000 sanic-security-1.9.8/sanic_security.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      172 2023-01-30 21:38:17.000000 sanic-security-1.9.8/sanic_security.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-01-30 21:38:17.000000 sanic-security-1.9.8/sanic_security.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-01-30 21:38:17.119185 sanic-security-1.9.8/setup.cfg
--rw-rw-rw-   0        0        0     1061 2023-01-30 21:24:05.000000 sanic-security-1.9.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-02-01 19:03:16.362583 sanic-security-1.9.9/
+-rw-rw-rw-   0        0        0    35188 2022-09-09 12:39:26.000000 sanic-security-1.9.9/LICENSE
+-rw-rw-rw-   0        0        0       92 2022-09-09 12:39:26.000000 sanic-security-1.9.9/MANIFEST.in
+-rw-rw-rw-   0        0        0    19177 2023-02-01 19:03:16.362583 sanic-security-1.9.9/PKG-INFO
+-rw-rw-rw-   0        0        0    18700 2023-01-30 21:21:55.000000 sanic-security-1.9.9/README.md
+drwxrwxrwx   0        0        0        0 2023-02-01 19:03:16.354562 sanic-security-1.9.9/sanic_security/
+-rw-rw-rw-   0        0        0        0 2022-09-09 12:39:26.000000 sanic-security-1.9.9/sanic_security/__init__.py
+-rw-rw-rw-   0        0        0     9482 2023-01-30 20:11:41.000000 sanic-security-1.9.9/sanic_security/authentication.py
+-rw-rw-rw-   0        0        0     6559 2023-01-30 20:11:41.000000 sanic-security-1.9.9/sanic_security/authorization.py
+-rw-rw-rw-   0        0        0     5145 2022-10-27 20:58:41.000000 sanic-security-1.9.9/sanic_security/configuration.py
+-rw-rw-rw-   0        0        0     3946 2023-02-01 13:42:59.000000 sanic-security-1.9.9/sanic_security/exceptions.py
+-rw-rw-rw-   0        0        0    18037 2023-02-01 13:43:19.000000 sanic-security-1.9.9/sanic_security/models.py
+drwxrwxrwx   0        0        0        0 2023-02-01 19:03:16.362583 sanic-security-1.9.9/sanic_security/test/
+-rw-rw-rw-   0        0        0        0 2022-09-09 12:39:26.000000 sanic-security-1.9.9/sanic_security/test/__init__.py
+-rw-rw-rw-   0        0        0    10158 2023-02-01 13:42:59.000000 sanic-security-1.9.9/sanic_security/test/server.py
+-rw-rw-rw-   0        0        0    17477 2023-02-01 17:55:55.000000 sanic-security-1.9.9/sanic_security/test/tests.py
+-rw-rw-rw-   0        0        0     2314 2022-09-16 15:06:09.000000 sanic-security-1.9.9/sanic_security/utils.py
+-rw-rw-rw-   0        0        0     7115 2023-01-30 20:11:41.000000 sanic-security-1.9.9/sanic_security/verification.py
+drwxrwxrwx   0        0        0        0 2023-02-01 19:03:16.362583 sanic-security-1.9.9/sanic_security.egg-info/
+-rw-rw-rw-   0        0        0    19177 2023-02-01 19:03:16.000000 sanic-security-1.9.9/sanic_security.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      551 2023-02-01 19:03:16.000000 sanic-security-1.9.9/sanic_security.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-02-01 19:03:16.000000 sanic-security-1.9.9/sanic_security.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      172 2023-02-01 19:03:16.000000 sanic-security-1.9.9/sanic_security.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-02-01 19:03:16.000000 sanic-security-1.9.9/sanic_security.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-02-01 19:03:16.362583 sanic-security-1.9.9/setup.cfg
+-rw-rw-rw-   0        0        0     1061 2023-02-01 13:42:59.000000 sanic-security-1.9.9/setup.py
```

### Comparing `sanic-security-1.9.8/LICENSE` & `sanic-security-1.9.9/LICENSE`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/PKG-INFO` & `sanic-security-1.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sanic-security
-Version: 1.9.8
+Version: 1.9.9
 Summary: An effective, simple, and async security library for the Sanic framework.
 Home-page: https://github.com/na-stewart/sanic-security
 Author: Aidan Stewart
 Author-email: na.stewart365@gmail.com
 License: GNU Affero General Public License v3.0
 Platform: any
 Requires-Python: >=3.6
```

### Comparing `sanic-security-1.9.8/README.md` & `sanic-security-1.9.9/README.md`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/sanic_security/authentication.py` & `sanic-security-1.9.9/sanic_security/authentication.py`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/sanic_security/authorization.py` & `sanic-security-1.9.9/sanic_security/authorization.py`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/sanic_security/configuration.py` & `sanic-security-1.9.9/sanic_security/configuration.py`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/sanic_security/exceptions.py` & `sanic-security-1.9.9/sanic_security/exceptions.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 from sanic.exceptions import SanicException
 
 from sanic_security.utils import json
 
-
 """
 An effective, simple, and async security library for the Sanic framework.
 Copyright (C) 2020-present Aidan Stewart
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
@@ -67,15 +66,15 @@
 
 
 class DisabledError(AccountError):
     """
     Raised when account is disabled.
     """
 
-    def __init__(self, message="Account is deactivated.", code: int = 401):
+    def __init__(self, message: str = "Account is disabled.", code: int = 401):
         super().__init__(message, code)
 
 
 class UnverifiedError(AccountError):
     """
     Raised when account is unverified.
     """
@@ -103,15 +102,15 @@
 
 
 class DeactivatedError(SessionError):
     """
     Raised when session is deactivated.
     """
 
-    def __init__(self, message="Session is deactivated.", code: int = 401):
+    def __init__(self, message: str = "Session is deactivated.", code: int = 401):
         super().__init__(message, code)
 
 
 class ExpiredError(SessionError):
     """
     Raised when session has expired.
     """
```

### Comparing `sanic-security-1.9.8/sanic_security/models.py` & `sanic-security-1.9.9/sanic_security/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -134,23 +134,23 @@
         elif not self.verified:
             raise UnverifiedError()
         elif self.disabled:
             raise DisabledError()
 
     async def disable(self):
         """
-        Renders account unusable
+        Renders account unusable.
 
         Raises:
             DisabledError
         """
         if self.disabled:
             raise DisabledError("Account is already disabled.")
         else:
-            self.disabled = False
+            self.disabled = True
             await self.save(update_fields=["disabled"])
 
     @staticmethod
     async def get_via_email(email: str):
         """
         Retrieve an account with an email.
 
@@ -317,14 +317,33 @@
 
         Returns:
             session
         """
         raise NotImplementedError()
 
     @classmethod
+    async def get_related(cls, account: Account):
+        """
+        Retrieves sessions associated to an account.
+
+        Args:
+            account (Request): Account associated with sessions being retrieved.
+
+        Returns:
+            sessions
+
+        Raises:
+            NotFoundError
+        """
+        sessions = await cls.filter(bearer=account).prefetch_related("bearer").all()
+        if not sessions:
+            raise NotFoundError("No sessions associated to account were found.")
+        return sessions
+
+    @classmethod
     def decode_raw(cls, request: Request) -> dict:
         """
         Decodes JWT token from client cookie into a python dict.
 
         Args:
             request (Request): Sanic request parameter.
```

### Comparing `sanic-security-1.9.8/sanic_security/test/server.py` & `sanic-security-1.9.9/sanic_security/test/server.py`

 * *Files 6% similar despite different names*

```diff
@@ -12,25 +12,24 @@
 from sanic_security.authorization import (
     assign_role,
     check_permissions,
     check_roles,
 )
 from sanic_security.configuration import config as security_config
 from sanic_security.exceptions import SecurityError, CredentialsError
-from sanic_security.models import Account, CaptchaSession
+from sanic_security.models import Account, CaptchaSession, AuthenticationSession
 from sanic_security.utils import json
 from sanic_security.verification import (
     request_two_step_verification,
     requires_two_step_verification,
     verify_account,
     request_captcha,
     requires_captcha,
 )
 
-
 """
 An effective, simple, and async security library for the Sanic framework.
 Copyright (C) 2020-present Aidan Stewart
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
@@ -41,15 +40,14 @@
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.
 
 You should have received a copy of the GNU Affero General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
 """
 
-
 app = Sanic("security-test")
 password_hasher = PasswordHasher()
 
 
 @app.post("api/test/auth/register")
 async def on_register(request):
     """
@@ -110,14 +108,29 @@
     Authenticate client session and account.
     """
     response = json("Authenticated!", authentication_session.bearer.json())
     authentication_session.encode(response)
     return response
 
 
+@app.post("api/test/auth/related")
+@requires_authentication()
+async def on_get_related_authentication_sessions(request, authentication_session):
+    """
+    Retrieves authentication sessions associated with logged in account.
+    """
+    authentication_sessions = await AuthenticationSession.get_related(
+        authentication_session.bearer
+    )
+    return json(
+        "Related authentication sessions retrieved!",
+        [auth_session.json() for auth_session in authentication_sessions],
+    )
+
+
 @app.get("api/test/capt/request")
 async def on_captcha_request(request):
     """
     Request captcha with solution in response.
     """
     captcha_session = await request_captcha(request)
     response = json("Captcha request successful!", captcha_session.code)
@@ -201,15 +214,15 @@
     """
     if await Account.filter(email=request.form.get("email").lower()).exists():
         raise CredentialsError("An account with this email already exists.", 409)
     elif await Account.filter(username=request.form.get("username")).exists():
         raise CredentialsError("An account with this username already exists.", 409)
     account = await Account.create(
         username=request.form.get("username"),
-        email=request.form.get("email"),
+        email=request.form.get("email").lower(),
         password=password_hasher.hash("password"),
         verified=True,
         dbisabled=False,
     )
     response = json("Account creation successful!", account.json())
     return response
```

### Comparing `sanic-security-1.9.8/sanic_security/test/tests.py` & `sanic-security-1.9.9/sanic_security/test/tests.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,14 @@
 import os
 from unittest import TestCase
 
 import httpx
 
 from sanic_security.configuration import Config
 
-
 """
 An effective, simple, and async security library for the Sanic framework.
 Copyright (C) 2020-present Aidan Stewart
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as published
 by the Free Software Foundation, either version 3 of the License, or
@@ -288,15 +287,15 @@
         )
         assert (
             captcha_attempt_response.status_code == 200
         ), captcha_attempt_response.text
 
     def test_two_step_verification(self):
         """
-        Two step verification request and attempt.
+        Two-step verification request and attempt.
         """
         self.client.post(
             "http://127.0.0.1:8000/api/test/account",
             data={"email": "two_step@verification.com", "username": "two_step"},
         )
         two_step_verification_request_response = self.client.post(
             "http://127.0.0.1:8000/api/test/two-step/request",
@@ -431,20 +430,43 @@
             data={"role": "InvalidRole"},
         )
         assert (
             prohibited_authorization_response.status_code == 403
         ), prohibited_authorization_response.text
 
 
-class ConfigurationTest(TestCase):
+class MiscTest(TestCase):
     """
-    Tests configuration.
+    Miscellaneous tests that cannot be categorized.
     """
 
+    def setUp(self):
+        self.client = httpx.Client()
+
+    def tearDown(self):
+        self.client.close()
+
     def test_environment_variable_load(self):
         """
         Config loads environment variables.
         """
         os.environ["SANIC_SECURITY_SECRET"] = "test-secret"
         security_config = Config()
         security_config.load_environment_variables()
         assert security_config.SECRET == "test-secret"
+
+    def test_get_related_sessions(self):
+        self.client.post(
+            "http://127.0.0.1:8000/api/test/account",
+            data={"email": "get_related_sessions@misc.com", "username": "get_related"},
+        )
+        login_response = self.client.post(
+            "http://127.0.0.1:8000/api/test/auth/login",
+            auth=("get_related_sessions@misc.com", "password"),
+        )
+        assert login_response.status_code == 200, login_response.text
+        retrieve_related_response = self.client.post(
+            "http://127.0.0.1:8000/api/test/auth/related"
+        )
+        assert (
+            retrieve_related_response.status_code == 200
+        ), retrieve_related_response.text
```

### Comparing `sanic-security-1.9.8/sanic_security/utils.py` & `sanic-security-1.9.9/sanic_security/utils.py`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/sanic_security/verification.py` & `sanic-security-1.9.9/sanic_security/verification.py`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/sanic_security.egg-info/PKG-INFO` & `sanic-security-1.9.9/sanic_security.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sanic-security
-Version: 1.9.8
+Version: 1.9.9
 Summary: An effective, simple, and async security library for the Sanic framework.
 Home-page: https://github.com/na-stewart/sanic-security
 Author: Aidan Stewart
 Author-email: na.stewart365@gmail.com
 License: GNU Affero General Public License v3.0
 Platform: any
 Requires-Python: >=3.6
```

### Comparing `sanic-security-1.9.8/sanic_security.egg-info/SOURCES.txt` & `sanic-security-1.9.9/sanic_security.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sanic-security-1.9.8/setup.py` & `sanic-security-1.9.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
     author="Aidan Stewart",
     author_email="na.stewart365@gmail.com",
     description="An effective, simple, and async security library for the Sanic framework.",
     url="https://github.com/na-stewart/sanic-security",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license="GNU Affero General Public License v3.0",
-    version="1.9.8",
+    version="1.9.9",
     packages=setuptools.find_packages(),
     python_requires=">=3.6",
     install_requires=[
         "tortoise-orm>=0.17.0",
         "pyjwt>=1.7.0",
         "captcha",
         "argon2-cffi>=20.1.0",
```

