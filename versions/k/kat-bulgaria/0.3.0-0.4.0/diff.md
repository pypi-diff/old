# Comparing `tmp/kat_bulgaria-0.3.0.tar.gz` & `tmp/kat_bulgaria-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kat_bulgaria-0.3.0.tar", last modified: Thu Apr  6 09:04:00 2023, max compression
+gzip compressed data, was "kat_bulgaria-0.4.0.tar", last modified: Thu Apr  6 09:29:57 2023, max compression
```

## Comparing `kat_bulgaria-0.3.0.tar` & `kat_bulgaria-0.4.0.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:00.632292 kat_bulgaria-0.3.0/
--rw-r--r--   0 runner    (1001) docker     (123)     5073 2023-04-06 09:04:00.632292 kat_bulgaria-0.3.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4774 2023-04-06 09:03:45.000000 kat_bulgaria-0.3.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:00.632292 kat_bulgaria-0.3.0/kat_bulgaria/
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 09:03:45.000000 kat_bulgaria-0.3.0/kat_bulgaria/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5470 2023-04-06 09:03:45.000000 kat_bulgaria-0.3.0/kat_bulgaria/obligations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:00.632292 kat_bulgaria-0.3.0/kat_bulgaria.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5073 2023-04-06 09:04:00.000000 kat_bulgaria-0.3.0/kat_bulgaria.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 09:04:00.000000 kat_bulgaria-0.3.0/kat_bulgaria.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:04:00.000000 kat_bulgaria-0.3.0/kat_bulgaria.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 09:04:00.000000 kat_bulgaria-0.3.0/kat_bulgaria.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 09:04:00.000000 kat_bulgaria-0.3.0/kat_bulgaria.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:04:00.632292 kat_bulgaria-0.3.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      692 2023-04-06 09:03:45.000000 kat_bulgaria-0.3.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:04:00.632292 kat_bulgaria-0.3.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-06 09:03:45.000000 kat_bulgaria-0.3.0/tests/test_obligations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:29:57.844220 kat_bulgaria-0.4.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     4969 2023-04-06 09:29:57.844220 kat_bulgaria-0.4.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4670 2023-04-06 09:29:36.000000 kat_bulgaria-0.4.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:29:57.844220 kat_bulgaria-0.4.0/kat_bulgaria/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 09:29:36.000000 kat_bulgaria-0.4.0/kat_bulgaria/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6029 2023-04-06 09:29:36.000000 kat_bulgaria-0.4.0/kat_bulgaria/obligations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:29:57.844220 kat_bulgaria-0.4.0/kat_bulgaria.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4969 2023-04-06 09:29:57.000000 kat_bulgaria-0.4.0/kat_bulgaria.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 09:29:57.000000 kat_bulgaria-0.4.0/kat_bulgaria.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 09:29:57.000000 kat_bulgaria-0.4.0/kat_bulgaria.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 09:29:57.000000 kat_bulgaria-0.4.0/kat_bulgaria.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 09:29:57.000000 kat_bulgaria-0.4.0/kat_bulgaria.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 09:29:57.844220 kat_bulgaria-0.4.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      692 2023-04-06 09:29:36.000000 kat_bulgaria-0.4.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 09:29:57.844220 kat_bulgaria-0.4.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-06 09:29:36.000000 kat_bulgaria-0.4.0/tests/test_obligations.py
```

### Comparing `kat_bulgaria-0.3.0/PKG-INFO` & `kat_bulgaria-0.4.0/kat_bulgaria.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: kat_bulgaria
-Version: 0.3.0
+Name: kat-bulgaria
+Version: 0.4.0
 Summary: A library to check for existing obligations to KAT Bulgaria
 Home-page: https://github.com/Nedevski/py_kat_bulgaria
 Author: Nikola Nedevski
 Author-email: nikola.nedevski@gmail.com
 License: MIT
 Description-Content-Type: text/markdown
 
@@ -29,33 +29,36 @@
 ## Example:
 ```python
 import asyncio
 from dataclasses import asdict
 from kat_bulgaria.obligations import (
     KatError,
     KatFatalError,
-    async_verify_credentials,
-    async_check_obligations,
-    async_get_obligations,
+    KatApi,
 )
 
 EGN = "0011223344"
 LICENSE_NUMBER = "123456789"
 
 
-def example_func() -> None:
+def example_code():
+    api = KatApi()
+
     try:
         # Validates EGN and Driver License Number locally and with the API
-        is_valid = asyncio.run(async_verify_credentials(EGN, LICENSE_NUMBER))
+        is_valid = asyncio.run(api.async_verify_credentials(EGN, LICENSE_NUMBER))
+        print(is_valid)
 
         # Checks if a person has obligations, returns true or false
-        has_obligations = asyncio.run(async_check_obligations(EGN, LICENSE_NUMBER))
+        has_obligations = asyncio.run(api.async_check_obligations(EGN, LICENSE_NUMBER))
+        print(has_obligations)
 
         # Returns an object with additinal data (if any)
-        obligations = asyncio.run(async_get_obligations(EGN, LICENSE_NUMBER))
+        obligations = asyncio.run(api.async_get_obligations(EGN, LICENSE_NUMBER))
+        print(obligations)
 
     except ValueError as err:
         # Validation error, such as invalid EGN or Driver License Number
         print(f"Error: {str(err)}")
         return
 
     except KatError as err:
@@ -67,20 +70,17 @@
     except KatFatalError as err:
         # Fatal error, this means the KAT website returned an unexpected response.
         # If you get this error this means the website was probably updated and this library
         # needs to reflect that change. Please open a new issue so it can be fixed.
         print(f"Error: {str(err)}")
         return
 
-    print(f"is_valid = {is_valid}")
-    print(f"has_obligations = {has_obligations}")
-    print(f"obligations = {asdict(obligations)}")
 
+example_code()
 
-example_func()
 ```
 
 ## Known raw API responses (debug info):
 
 
 ```python
 # No fines/obligations:
```

### Comparing `kat_bulgaria-0.3.0/README.md` & `kat_bulgaria-0.4.0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -19,33 +19,36 @@
 ## Example:
 ```python
 import asyncio
 from dataclasses import asdict
 from kat_bulgaria.obligations import (
     KatError,
     KatFatalError,
-    async_verify_credentials,
-    async_check_obligations,
-    async_get_obligations,
+    KatApi,
 )
 
 EGN = "0011223344"
 LICENSE_NUMBER = "123456789"
 
 
-def example_func() -> None:
+def example_code():
+    api = KatApi()
+
     try:
         # Validates EGN and Driver License Number locally and with the API
-        is_valid = asyncio.run(async_verify_credentials(EGN, LICENSE_NUMBER))
+        is_valid = asyncio.run(api.async_verify_credentials(EGN, LICENSE_NUMBER))
+        print(is_valid)
 
         # Checks if a person has obligations, returns true or false
-        has_obligations = asyncio.run(async_check_obligations(EGN, LICENSE_NUMBER))
+        has_obligations = asyncio.run(api.async_check_obligations(EGN, LICENSE_NUMBER))
+        print(has_obligations)
 
         # Returns an object with additinal data (if any)
-        obligations = asyncio.run(async_get_obligations(EGN, LICENSE_NUMBER))
+        obligations = asyncio.run(api.async_get_obligations(EGN, LICENSE_NUMBER))
+        print(obligations)
 
     except ValueError as err:
         # Validation error, such as invalid EGN or Driver License Number
         print(f"Error: {str(err)}")
         return
 
     except KatError as err:
@@ -57,20 +60,17 @@
     except KatFatalError as err:
         # Fatal error, this means the KAT website returned an unexpected response.
         # If you get this error this means the website was probably updated and this library
         # needs to reflect that change. Please open a new issue so it can be fixed.
         print(f"Error: {str(err)}")
         return
 
-    print(f"is_valid = {is_valid}")
-    print(f"has_obligations = {has_obligations}")
-    print(f"obligations = {asdict(obligations)}")
 
+example_code()
 
-example_func()
 ```
 
 ## Known raw API responses (debug info):
 
 
 ```python
 # No fines/obligations:
```

### Comparing `kat_bulgaria-0.3.0/kat_bulgaria/obligations.py` & `kat_bulgaria-0.4.0/kat_bulgaria/obligations.py`

 * *Files 8% similar despite different names*

```diff
@@ -7,14 +7,16 @@
 
 _REQUEST_TIMEOUT = 5
 _KAT_OBLIGATIONS_URL = "https://e-uslugi.mvr.bg/api/Obligations/AND?mode=1&obligedPersonIdent={egn}&drivingLicenceNumber={license_number}"
 
 _RESP_HAS_NON_HANDED_SLIP = "hasNonHandedSlip"
 _RESP_OBLIGATIONS = "obligations"
 
+_ERR_PREFIX = "[KAT_API]"
+
 REGEX_EGN = r"^[0-9]{2}[0,1,2,4][0-9][0-9]{2}[0-9]{4}$"
 REGEX_DRIVING_LICENSE = r"^[0-9]{9}$"
 
 
 @dataclass
 class KatObligationsSimpleResponse:
     """The obligations response object."""
@@ -68,102 +70,110 @@
 class KatFatalError(Exception):
     """Fatal error wrapper"""
 
     def __init__(self, *args: object) -> None:
         super().__init__(*args)
 
 
-async def async_verify_credentials(egn: str, license_number: str) -> bool:
-    """Confirm that the credentials are correct."""
-    if egn is None:
-        raise ValueError("EGN Missing")
-    else:
-        egn_match = re.search(REGEX_EGN, egn)
-        if egn_match is None:
-            raise ValueError("EGN is not valid")
-
-    if license_number is None:
-        raise ValueError("Driving License Number missing")
-    else:
-        license_match = re.search(REGEX_DRIVING_LICENSE, license_number)
-        if license_match is None:
-            raise ValueError("Driving License Number not valid")
-
-    try:
-        url = _KAT_OBLIGATIONS_URL.format(egn=egn, license_number=license_number)
+class KatApi:
+    """KAT API manager"""
 
-        async with httpx.AsyncClient() as client:
-            resp = await client.get(url, timeout=_REQUEST_TIMEOUT)
-            resp.raise_for_status()
+    def __init__(self):
+        """Constructor"""
 
-    except httpx.HTTPError:
-        return False
+    async def async_verify_credentials(self, egn: str, license_number: str) -> bool:
+        """Confirm that the credentials are correct."""
+        if egn is None:
+            raise ValueError("EGN Missing")
+        else:
+            egn_match = re.search(REGEX_EGN, egn)
+            if egn_match is None:
+                raise ValueError("EGN is not valid")
 
-    return True
+        if license_number is None:
+            raise ValueError("Driving License Number missing")
+        else:
+            license_match = re.search(REGEX_DRIVING_LICENSE, license_number)
+            if license_match is None:
+                raise ValueError("Driving License Number not valid")
 
+        try:
+            url = _KAT_OBLIGATIONS_URL.format(egn=egn, license_number=license_number)
 
-async def async_check_obligations(egn: str, license_number: str) -> bool:
-    """Check if the person has obligations"""
+            async with httpx.AsyncClient() as client:
+                resp = await client.get(url, timeout=_REQUEST_TIMEOUT)
+                resp.raise_for_status()
 
-    data = await _get_obligations_request(egn, license_number)
+        except httpx.HTTPError:
+            return False
 
-    return KatObligationsSimpleResponse(data).has_obligations
+        return True
 
+    async def async_check_obligations(self, egn: str, license_number: str) -> bool:
+        """Check if the person has obligations"""
 
-async def async_get_obligations(
-    egn: str, license_number: str
-) -> KatObligationsResponse:
-    """Get all obligations"""
+        data = await self.__get_obligations_request(egn, license_number)
 
-    data = await _get_obligations_request(egn, license_number)
+        return KatObligationsSimpleResponse(data).has_obligations
 
-    return KatObligationsResponse(data)
+    async def async_get_obligations(
+        self, egn: str, license_number: str
+    ) -> KatObligationsResponse:
+        """Get all obligations"""
 
+        data = await self.__get_obligations_request(egn, license_number)
 
-async def _get_obligations_request(egn: str, license_number: str) -> any:
-    """
-    Calls the public URL to check if an user has any obligations.
+        return KatObligationsResponse(data)
 
-    :param person_egn: EGN of the person
-    :param driving_license_number: Driver License Number
+    async def __get_obligations_request(self, egn: str, license_number: str) -> any:
+        """
+        Calls the public URL to check if an user has any obligations.
 
-    """
-    data = {}
+        :param person_egn: EGN of the person
+        :param driving_license_number: Driver License Number
 
-    try:
-        url = _KAT_OBLIGATIONS_URL.format(egn=egn, license_number=license_number)
+        """
+        data = {}
 
-        async with httpx.AsyncClient() as client:
-            resp = await client.get(url, timeout=_REQUEST_TIMEOUT)
-            resp.raise_for_status()
+        try:
+            url = _KAT_OBLIGATIONS_URL.format(egn=egn, license_number=license_number)
 
-        data = resp.json()
+            async with httpx.AsyncClient() as client:
+                resp = await client.get(url, timeout=_REQUEST_TIMEOUT)
+                data = resp.json()
+                resp.raise_for_status()
 
-    except httpx.TimeoutException as ex:
-        # The requests timeout from time to time, don't worry about it
-        raise KatError(f"KAT_BG: Request timed out for {license_number}") from ex
+        except httpx.TimeoutException as ex:
+            # The requests timeout from time to time, don't worry about it
+            raise KatError(
+                f"{_ERR_PREFIX} Request timed out for {license_number}"
+            ) from ex
 
-    except httpx.HTTPError as ex:
-        if "code" in data:
-            # code = GL_00038_E
-            # Invalid user data => Throw error
-            if data["code"] == "GL_00038_E":
-                raise ValueError(
-                    f"KAT_BG: EGN or Driving License Number was not valid: {str(ex)}"
+        except httpx.HTTPError as ex:
+            if "code" in data:
+                # code = GL_00038_E
+                # Invalid user data => Throw error
+                if data["code"] == "GL_00038_E":
+                    raise ValueError(
+                        f"{_ERR_PREFIX} EGN or Driving License Number was not valid."
+                    ) from ex
+
+                # code = GL_UNDELIVERED_AND_UNPAID_DEBTS_E
+                # This means the KAT website died for a bit
+                if data["code"] == "GL_00038_E":
+                    raise KatError(
+                        f"{_ERR_PREFIX} Website is down temporarily. :("
+                    ) from ex
+
+            else:
+                # If the response is 400 and there is no "code", probably they changed the schema
+                raise KatFatalError(
+                    f"{_ERR_PREFIX} Website returned an unknown error: {str(ex)}"
                 ) from ex
 
-            # code = GL_UNDELIVERED_AND_UNPAID_DEBTS_E
-            # This means the KAT website died for a bit
-            if data["code"] == "GL_00038_E":
-                raise KatError("KAT_BG: Website is down temporarily. :(") from ex
-
-        else:
-            # If the response is 400 and there is no "code", probably they changed the schema
+        if _RESP_HAS_NON_HANDED_SLIP not in data or _RESP_OBLIGATIONS not in data:
+            # This should never happen. If we go in this if, this probably means they changed their schema
             raise KatFatalError(
-                f"KAT_BG: Website returned an unknown error: {str(ex)}"
-            ) from ex
-
-    if _RESP_HAS_NON_HANDED_SLIP not in data or _RESP_OBLIGATIONS not in data:
-        # This should never happen. If we go in this if, this probably means they changed their schema
-        raise KatFatalError(f"KAT_BG: Website returned a malformed response: {data}")
+                f"{_ERR_PREFIX} Website returned a malformed response: {data}"
+            )
 
-    return data
+        return data
```

### Comparing `kat_bulgaria-0.3.0/kat_bulgaria.egg-info/PKG-INFO` & `kat_bulgaria-0.4.0/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: kat-bulgaria
-Version: 0.3.0
+Name: kat_bulgaria
+Version: 0.4.0
 Summary: A library to check for existing obligations to KAT Bulgaria
 Home-page: https://github.com/Nedevski/py_kat_bulgaria
 Author: Nikola Nedevski
 Author-email: nikola.nedevski@gmail.com
 License: MIT
 Description-Content-Type: text/markdown
 
@@ -29,33 +29,36 @@
 ## Example:
 ```python
 import asyncio
 from dataclasses import asdict
 from kat_bulgaria.obligations import (
     KatError,
     KatFatalError,
-    async_verify_credentials,
-    async_check_obligations,
-    async_get_obligations,
+    KatApi,
 )
 
 EGN = "0011223344"
 LICENSE_NUMBER = "123456789"
 
 
-def example_func() -> None:
+def example_code():
+    api = KatApi()
+
     try:
         # Validates EGN and Driver License Number locally and with the API
-        is_valid = asyncio.run(async_verify_credentials(EGN, LICENSE_NUMBER))
+        is_valid = asyncio.run(api.async_verify_credentials(EGN, LICENSE_NUMBER))
+        print(is_valid)
 
         # Checks if a person has obligations, returns true or false
-        has_obligations = asyncio.run(async_check_obligations(EGN, LICENSE_NUMBER))
+        has_obligations = asyncio.run(api.async_check_obligations(EGN, LICENSE_NUMBER))
+        print(has_obligations)
 
         # Returns an object with additinal data (if any)
-        obligations = asyncio.run(async_get_obligations(EGN, LICENSE_NUMBER))
+        obligations = asyncio.run(api.async_get_obligations(EGN, LICENSE_NUMBER))
+        print(obligations)
 
     except ValueError as err:
         # Validation error, such as invalid EGN or Driver License Number
         print(f"Error: {str(err)}")
         return
 
     except KatError as err:
@@ -67,20 +70,17 @@
     except KatFatalError as err:
         # Fatal error, this means the KAT website returned an unexpected response.
         # If you get this error this means the website was probably updated and this library
         # needs to reflect that change. Please open a new issue so it can be fixed.
         print(f"Error: {str(err)}")
         return
 
-    print(f"is_valid = {is_valid}")
-    print(f"has_obligations = {has_obligations}")
-    print(f"obligations = {asdict(obligations)}")
 
+example_code()
 
-example_func()
 ```
 
 ## Known raw API responses (debug info):
 
 
 ```python
 # No fines/obligations:
```

### Comparing `kat_bulgaria-0.3.0/setup.py` & `kat_bulgaria-0.4.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from pathlib import Path
 from setuptools import find_packages, setup
 
 long_description = Path("README.md").read_text()
 
 setup(
     name="kat_bulgaria",
-    version="0.3.0",
+    version="0.4.0",
     description="A library to check for existing obligations to KAT Bulgaria",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Nedevski/py_kat_bulgaria",
     author="Nikola Nedevski",
     author_email="nikola.nedevski@gmail.com",
     license="MIT",
```

