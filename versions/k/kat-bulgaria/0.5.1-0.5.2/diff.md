# Comparing `tmp/kat_bulgaria-0.5.1.tar.gz` & `tmp/kat_bulgaria-0.5.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kat_bulgaria-0.5.1.tar", last modified: Thu Apr  6 11:46:54 2023, max compression
+gzip compressed data, was "kat_bulgaria-0.5.2.tar", last modified: Thu Apr  6 13:35:36 2023, max compression
```

## Comparing `kat_bulgaria-0.5.1.tar` & `kat_bulgaria-0.5.2.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:46:54.856852 kat_bulgaria-0.5.1/
--rw-r--r--   0 runner    (1001) docker     (123)     4555 2023-04-06 11:46:54.856852 kat_bulgaria-0.5.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4256 2023-04-06 11:46:43.000000 kat_bulgaria-0.5.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:46:54.852852 kat_bulgaria-0.5.1/kat_bulgaria/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 11:46:43.000000 kat_bulgaria-0.5.1/kat_bulgaria/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8110 2023-04-06 11:46:43.000000 kat_bulgaria-0.5.1/kat_bulgaria/obligations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:46:54.852852 kat_bulgaria-0.5.1/kat_bulgaria.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4555 2023-04-06 11:46:54.000000 kat_bulgaria-0.5.1/kat_bulgaria.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 11:46:54.000000 kat_bulgaria-0.5.1/kat_bulgaria.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:46:54.000000 kat_bulgaria-0.5.1/kat_bulgaria.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 11:46:54.000000 kat_bulgaria-0.5.1/kat_bulgaria.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 11:46:54.000000 kat_bulgaria-0.5.1/kat_bulgaria.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:46:54.856852 kat_bulgaria-0.5.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      692 2023-04-06 11:46:43.000000 kat_bulgaria-0.5.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:46:54.856852 kat_bulgaria-0.5.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-06 11:46:43.000000 kat_bulgaria-0.5.1/tests/test_obligations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:36.214019 kat_bulgaria-0.5.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     4650 2023-04-06 13:35:36.214019 kat_bulgaria-0.5.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4351 2023-04-06 13:35:21.000000 kat_bulgaria-0.5.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:36.214019 kat_bulgaria-0.5.2/kat_bulgaria/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 13:35:21.000000 kat_bulgaria-0.5.2/kat_bulgaria/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8215 2023-04-06 13:35:21.000000 kat_bulgaria-0.5.2/kat_bulgaria/obligations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:36.214019 kat_bulgaria-0.5.2/kat_bulgaria.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4650 2023-04-06 13:35:36.000000 kat_bulgaria-0.5.2/kat_bulgaria.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 13:35:36.000000 kat_bulgaria-0.5.2/kat_bulgaria.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:35:36.000000 kat_bulgaria-0.5.2/kat_bulgaria.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 13:35:36.000000 kat_bulgaria-0.5.2/kat_bulgaria.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 13:35:36.000000 kat_bulgaria-0.5.2/kat_bulgaria.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:35:36.214019 kat_bulgaria-0.5.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      692 2023-04-06 13:35:21.000000 kat_bulgaria-0.5.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:36.214019 kat_bulgaria-0.5.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-06 13:35:21.000000 kat_bulgaria-0.5.2/tests/test_obligations.py
```

### Comparing `kat_bulgaria-0.5.1/PKG-INFO` & `kat_bulgaria-0.5.2/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kat_bulgaria
-Version: 0.5.1
+Version: 0.5.2
 Summary: A library to check for existing obligations to KAT Bulgaria
 Home-page: https://github.com/Nedevski/py_kat_bulgaria
 Author: Nikola Nedevski
 Author-email: nikola.nedevski@gmail.com
 License: MIT
 Description-Content-Type: text/markdown
 
@@ -37,29 +37,32 @@
 
 EGN = "0011223344"
 LICENSE_NUMBER = "123456789"
 
 
 def example_code():
     """Example Code"""
-    
+
     api = KatApi()
 
     try:
         # Validates EGN and Driver License Number locally and with the API
         verify = asyncio.run(api.async_verify_credentials(EGN, LICENSE_NUMBER))
-        print(f"Valid: {verify.data}")
+        print(f"IsValid: {verify.data}")
+        print(f"{verify}\n")
 
         # Checks if a person has obligations, returns true or false
         has_obligations = asyncio.run(api.async_check_obligations(EGN, LICENSE_NUMBER))
         print(f"HasObligations: {has_obligations.data}")
+        print(f"{has_obligations}\n")
 
         # Returns an object with additinal data (if any)
         obligations = asyncio.run(api.async_get_obligations(EGN, LICENSE_NUMBER))
-        print(f"Obligations details: {obligations.data}")
+        print(f"ObligationDetails: {obligations.data}")
+        print(f"{obligations}")
 
     except KatError as err:
         # Malformed response.
         # If you get this probably KAT updated their website.
         # Open an issue or contact me for fix.
         print(f"Error: {str(err)}")
         return
```

### Comparing `kat_bulgaria-0.5.1/README.md` & `kat_bulgaria-0.5.2/kat_bulgaria.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,7 +1,17 @@
+Metadata-Version: 2.1
+Name: kat-bulgaria
+Version: 0.5.2
+Summary: A library to check for existing obligations to KAT Bulgaria
+Home-page: https://github.com/Nedevski/py_kat_bulgaria
+Author: Nikola Nedevski
+Author-email: nikola.nedevski@gmail.com
+License: MIT
+Description-Content-Type: text/markdown
+
 ## Summary
 
 [![PyPI Link](https://img.shields.io/pypi/v/kat_bulgaria?style=flat-square)](https://pypi.org/project/kat-bulgaria/)
 ![Last release](https://img.shields.io/github/release-date/nedevski/py_kat_bulgaria?style=flat-square)
 ![PyPI License](https://img.shields.io/pypi/l/kat_bulgaria?style=flat-square)
 ![PyPI Downloads](https://img.shields.io/pypi/dm/kat_bulgaria?style=flat-square)
 ![Code size](https://img.shields.io/github/languages/code-size/nedevski/py_kat_bulgaria?style=flat-square)
@@ -27,29 +37,32 @@
 
 EGN = "0011223344"
 LICENSE_NUMBER = "123456789"
 
 
 def example_code():
     """Example Code"""
-    
+
     api = KatApi()
 
     try:
         # Validates EGN and Driver License Number locally and with the API
         verify = asyncio.run(api.async_verify_credentials(EGN, LICENSE_NUMBER))
-        print(f"Valid: {verify.data}")
+        print(f"IsValid: {verify.data}")
+        print(f"{verify}\n")
 
         # Checks if a person has obligations, returns true or false
         has_obligations = asyncio.run(api.async_check_obligations(EGN, LICENSE_NUMBER))
         print(f"HasObligations: {has_obligations.data}")
+        print(f"{has_obligations}\n")
 
         # Returns an object with additinal data (if any)
         obligations = asyncio.run(api.async_get_obligations(EGN, LICENSE_NUMBER))
-        print(f"Obligations details: {obligations.data}")
+        print(f"ObligationDetails: {obligations.data}")
+        print(f"{obligations}")
 
     except KatError as err:
         # Malformed response.
         # If you get this probably KAT updated their website.
         # Open an issue or contact me for fix.
         print(f"Error: {str(err)}")
         return
@@ -110,8 +123,8 @@
 {"code":"GL_UNDELIVERED_AND_UNPAID_DEBTS_E","message":"По технически причини към момента не може да бъде извършена справка за невръчени и неплатени НП и/или електронни фишове по Закона за движението по пътищата и/или по Кодекса за застраховането."}
 
 # Timeout:
 # From time to time the API hangs and it takes more than 10s to load.
 # You can retry immediately, you can wait a couple of minutes
 # Господине, не виждате ли че сме в обедна почивка???
 # At this point it's out of your hands
-```
+```
```

### Comparing `kat_bulgaria-0.5.1/kat_bulgaria/obligations.py` & `kat_bulgaria-0.5.2/kat_bulgaria/obligations.py`

 * *Files 6% similar despite different names*

```diff
@@ -17,14 +17,37 @@
 _ERR_PREFIX = "[KAT]"
 _ERR_PREFIX_API = "[KAT_API]"
 
 REGEX_EGN = r"^[0-9]{2}[0,1,2,4][0-9][0-9]{2}[0-9]{4}$"
 REGEX_DRIVING_LICENSE = r"^[0-9]{9}$"
 
 
+# region ----- Errors
+
+
+class KatError(Exception):
+    """Error wrapper"""
+
+    def __init__(self, *args: object) -> None:
+        super().__init__(*args)
+
+
+class KatErrorType(Enum):
+    """Different KAT api error types"""
+
+    VALIDATION_ERROR = 1
+    API_UNAVAILABLE = 2
+    TIMEOUT = 3
+
+
+# endregion
+
+# region ----- Responses
+
+
 @dataclass
 class KatObligationsSimpleResponse:
     """The obligations response object."""
 
     def __init__(self, data: any) -> None:
         self.has_obligations = (
             data[_RESP_HAS_NON_HANDED_SLIP] or len(data[_RESP_OBLIGATIONS]) > 0
@@ -60,50 +83,14 @@
                         "person_name": obligation["obligedPersonName"],
                         "person_identifier": obligation["obligedPersonIdent"],
                         "discount": obligation["additionalData"]["discount"],
                     }
                 )
 
 
-class KatErrorType(Enum):
-    """Different KAT api error types"""
-
-    VALIDATION_ERROR = 1
-    API_UNAVAILABLE = 2
-    TIMEOUT = 3
-
-
-@dataclass
-class _WebResponse:
-    """Wrapper for the HTTP response"""
-
-    raw_data: any
-    error_message: str
-    error_type: KatErrorType
-    success: bool
-
-    def __init__(
-        self,
-        raw_data: any,
-        error_message: str = None,
-        error_type: KatErrorType = None,
-    ):
-        self.raw_data = raw_data
-        self.error_message = error_message
-        self.error_type = None
-
-        if error_message is None:
-            self.success = True
-        else:
-            self.success = False
-
-        if error_type is not None:
-            self.error_type: error_type
-
-
 T = TypeVar("T", KatObligationsResponse, KatObligationsSimpleResponse, bool)
 
 
 @dataclass
 class KatApiResponse(Generic[T]):
     """Wrapper for different responses"""
 
@@ -121,19 +108,40 @@
             self.success = False
 
         self.data = data
         self.error_message = error_message
         self.error_type = error_type
 
 
-class KatError(Exception):
-    """Error wrapper"""
+# endregion
 
-    def __init__(self, *args: object) -> None:
-        super().__init__(*args)
+
+@dataclass
+class _WebResponse:
+    """Wrapper for the HTTP response"""
+
+    raw_data: any
+    error_message: str
+    error_type: KatErrorType
+    success: bool
+
+    def __init__(
+        self,
+        raw_data: any,
+        error_message: str = None,
+        error_type: KatErrorType = None,
+    ):
+        self.raw_data = raw_data
+        self.error_message = error_message
+        self.error_type = error_type
+
+        if error_message is None:
+            self.success = True
+        else:
+            self.success = False
 
 
 class KatApi:
     """KAT API manager"""
 
     def __init__(self):
         """Constructor"""
@@ -192,17 +200,19 @@
 
     async def async_get_obligations(
         self, egn: str, license_number: str
     ) -> KatApiResponse[KatObligationsResponse]:
         """Get all obligations"""
 
         res = await self.__get_obligations_request(egn, license_number)
-        data = KatObligationsResponse(res.raw_data)
 
-        return KatApiResponse(data)
+        if res.success:
+            return KatApiResponse(KatObligationsResponse(res.raw_data))
+        else:
+            return KatApiResponse(None, res.error_message, res.error_type)
 
     async def __get_obligations_request(
         self, egn: str, license_number: str
     ) -> _WebResponse:
         """
         Calls the public URL to check if an user has any obligations.
```

### Comparing `kat_bulgaria-0.5.1/kat_bulgaria.egg-info/PKG-INFO` & `kat_bulgaria-0.5.2/README.md`

 * *Files 13% similar despite different names*

```diff
@@ -1,17 +1,7 @@
-Metadata-Version: 2.1
-Name: kat-bulgaria
-Version: 0.5.1
-Summary: A library to check for existing obligations to KAT Bulgaria
-Home-page: https://github.com/Nedevski/py_kat_bulgaria
-Author: Nikola Nedevski
-Author-email: nikola.nedevski@gmail.com
-License: MIT
-Description-Content-Type: text/markdown
-
 ## Summary
 
 [![PyPI Link](https://img.shields.io/pypi/v/kat_bulgaria?style=flat-square)](https://pypi.org/project/kat-bulgaria/)
 ![Last release](https://img.shields.io/github/release-date/nedevski/py_kat_bulgaria?style=flat-square)
 ![PyPI License](https://img.shields.io/pypi/l/kat_bulgaria?style=flat-square)
 ![PyPI Downloads](https://img.shields.io/pypi/dm/kat_bulgaria?style=flat-square)
 ![Code size](https://img.shields.io/github/languages/code-size/nedevski/py_kat_bulgaria?style=flat-square)
@@ -37,29 +27,32 @@
 
 EGN = "0011223344"
 LICENSE_NUMBER = "123456789"
 
 
 def example_code():
     """Example Code"""
-    
+
     api = KatApi()
 
     try:
         # Validates EGN and Driver License Number locally and with the API
         verify = asyncio.run(api.async_verify_credentials(EGN, LICENSE_NUMBER))
-        print(f"Valid: {verify.data}")
+        print(f"IsValid: {verify.data}")
+        print(f"{verify}\n")
 
         # Checks if a person has obligations, returns true or false
         has_obligations = asyncio.run(api.async_check_obligations(EGN, LICENSE_NUMBER))
         print(f"HasObligations: {has_obligations.data}")
+        print(f"{has_obligations}\n")
 
         # Returns an object with additinal data (if any)
         obligations = asyncio.run(api.async_get_obligations(EGN, LICENSE_NUMBER))
-        print(f"Obligations details: {obligations.data}")
+        print(f"ObligationDetails: {obligations.data}")
+        print(f"{obligations}")
 
     except KatError as err:
         # Malformed response.
         # If you get this probably KAT updated their website.
         # Open an issue or contact me for fix.
         print(f"Error: {str(err)}")
         return
@@ -120,8 +113,8 @@
 {"code":"GL_UNDELIVERED_AND_UNPAID_DEBTS_E","message":"По технически причини към момента не може да бъде извършена справка за невръчени и неплатени НП и/или електронни фишове по Закона за движението по пътищата и/или по Кодекса за застраховането."}
 
 # Timeout:
 # From time to time the API hangs and it takes more than 10s to load.
 # You can retry immediately, you can wait a couple of minutes
 # Господине, не виждате ли че сме в обедна почивка???
 # At this point it's out of your hands
-```
+```
```

### Comparing `kat_bulgaria-0.5.1/setup.py` & `kat_bulgaria-0.5.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from pathlib import Path
 from setuptools import find_packages, setup
 
 long_description = Path("README.md").read_text()
 
 setup(
     name="kat_bulgaria",
-    version="0.5.1",
+    version="0.5.2",
     description="A library to check for existing obligations to KAT Bulgaria",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Nedevski/py_kat_bulgaria",
     author="Nikola Nedevski",
     author_email="nikola.nedevski@gmail.com",
     license="MIT",
```

