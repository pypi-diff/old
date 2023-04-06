# Comparing `tmp/pyscora_wrangler-1.1.1.tar.gz` & `tmp/pyscora_wrangler-1.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyscora_wrangler-1.1.1.tar", max compression
+gzip compressed data, was "pyscora_wrangler-1.1.2.tar", max compression
```

## Comparing `pyscora_wrangler-1.1.1.tar` & `pyscora_wrangler-1.1.2.tar`

### file list

```diff
@@ -1,14 +1,18 @@
--rw-r--r--   0        0        0     1049 2023-04-06 15:03:13.032676 pyscora_wrangler-1.1.1/LICENSE
--rw-r--r--   0        0        0      659 2023-04-06 15:03:13.032676 pyscora_wrangler-1.1.1/README.md
--rw-r--r--   0        0        0     1061 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyproject.toml
--rw-r--r--   0        0        0       37 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/__init__.py
--rw-r--r--   0        0        0    14135 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/README.md
--rw-r--r--   0        0        0       85 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/__init__.py
--rw-r--r--   0        0        0     7114 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/athena/__init__.py
--rw-r--r--   0        0        0    15796 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/cognito/__init__.py
--rw-r--r--   0        0        0       88 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/constants.py
--rw-r--r--   0        0        0     6683 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/dynamodb/__init__.py
--rw-r--r--   0        0        0      671 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/aws/utils.py
--rw-r--r--   0        0        0      165 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/constants.py
--rw-r--r--   0        0        0     2692 2023-04-06 15:03:13.036676 pyscora_wrangler-1.1.1/pyscora_wrangler/utils.py
--rw-r--r--   0        0        0     1901 1970-01-01 00:00:00.000000 pyscora_wrangler-1.1.1/PKG-INFO
+-rw-r--r--   0        0        0     1049 2023-04-06 20:21:03.663100 pyscora_wrangler-1.1.2/LICENSE
+-rw-r--r--   0        0        0      659 2023-04-06 20:21:03.663100 pyscora_wrangler-1.1.2/README.md
+-rw-r--r--   0        0        0     1116 2023-04-06 20:21:03.663100 pyscora_wrangler-1.1.2/pyproject.toml
+-rw-r--r--   0        0        0       51 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/__init__.py
+-rw-r--r--   0        0        0    14201 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/README.md
+-rw-r--r--   0        0        0       85 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/__init__.py
+-rw-r--r--   0        0        0     7114 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/athena/__init__.py
+-rw-r--r--   0        0        0    15796 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/cognito/__init__.py
+-rw-r--r--   0        0        0       88 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/constants.py
+-rw-r--r--   0        0        0     6685 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/dynamodb/__init__.py
+-rw-r--r--   0        0        0      671 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/aws/utils.py
+-rw-r--r--   0        0        0      165 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/constants.py
+-rw-r--r--   0        0        0      504 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/ldap/README.md
+-rw-r--r--   0        0        0       60 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/ldap/__init__.py
+-rw-r--r--   0        0        0     7512 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/ldap/service/__init__.py
+-rw-r--r--   0        0        0       22 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/ldap/utils.py
+-rw-r--r--   0        0        0     2692 2023-04-06 20:21:03.667100 pyscora_wrangler-1.1.2/pyscora_wrangler/utils.py
+-rw-r--r--   0        0        0     1998 1970-01-01 00:00:00.000000 pyscora_wrangler-1.1.2/PKG-INFO
```

### Comparing `pyscora_wrangler-1.1.1/LICENSE` & `pyscora_wrangler-1.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pyscora_wrangler-1.1.1/README.md` & `pyscora_wrangler-1.1.2/README.md`

 * *Files identical despite different names*

### Comparing `pyscora_wrangler-1.1.1/pyproject.toml` & `pyscora_wrangler-1.1.2/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 [tool.poetry]
 name = "pyscora-wrangler"
-version = "1.1.1"
-description = ""
+version = "1.1.2"
+description = "Python lib for DE"
 authors = ["Oncase <suporte@oncase.com.br>"]
 maintainers = ["Guilherme Morone <guilherme.morone@oncase.com.br>"]
 license = "MIT"
 readme = "README.md"
 homepage = "https://github.com/oncase/pyscora-wrangler"
 repository = "https://github.com/oncase/pyscora-wrangler"
 keywords = ["wrapper", "scora", "python", "data_engineering"]
@@ -17,19 +17,21 @@
     "Programming Language :: Python :: 3.10",
     "Programming Language :: Python :: 3.11",
 ]
 include = ["LICENSE"]
 
 [tool.poetry.dependencies]
 python = ">=3.8,<4.0"
-boto3 = "^1.26.107"
+boto3 = "^1.26.108"
 awswrangler = "^2.20.1"
 asyncio = "^3.4.3"
 pyathena = "^2.23.0"
 pyyaml = "^6.0"
+ldap3 = "^2.9.1"
+typeguard = "^3.0.2"
 
 
 [tool.poetry.group.dev.dependencies]
 black = "^23.3.0"
 
 [tool.black]
 line-length = 120
```

### Comparing `pyscora_wrangler-1.1.1/pyscora_wrangler/aws/README.md` & `pyscora_wrangler-1.1.2/pyscora_wrangler/aws/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 This module contains a set of functions to interact with AWS services.
 
 # Athena
 
-_To be done_
+See `./athena/__init__.py` for more details.
 
 # Cognito
 
 ## `add_user_to_group`
 
 ### Adds the specified user to the specified group
 
@@ -210,12 +210,12 @@
 
 ### Returns
 
 `None`
 
 # DynamoDB
 
-_To be done_
+See `./dynamodb/__init__.py` for more details.
 
 # Other Services
 
 Check out [boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) and [awswrangler docs](https://pypi.org/project/awswrangler/) for more information.
```

### Comparing `pyscora_wrangler-1.1.1/pyscora_wrangler/aws/athena/__init__.py` & `pyscora_wrangler-1.1.2/pyscora_wrangler/aws/athena/__init__.py`

 * *Files identical despite different names*

### Comparing `pyscora_wrangler-1.1.1/pyscora_wrangler/aws/cognito/__init__.py` & `pyscora_wrangler-1.1.2/pyscora_wrangler/aws/cognito/__init__.py`

 * *Files identical despite different names*

### Comparing `pyscora_wrangler-1.1.1/pyscora_wrangler/aws/dynamodb/__init__.py` & `pyscora_wrangler-1.1.2/pyscora_wrangler/aws/dynamodb/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -48,15 +48,15 @@
     """Get all data in table
 
     Args:
         table_name (str): The name of the table containing the requested items.
         select ('ALL_ATTRIBUTES' | 'ALL_PROJECTED_ATTRIBUTES' | 'SPECIFIC_ATTRIBUTES' | 'COUNT', optional): The attributes to be returned in the result. Defaults to 'ALL_ATTRIBUTES'.
         boto3_session (Session | None, optional): Custom boto3 session. Defaults to None.
 
-        Additional args can be found athttps://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/scan.html
+        Additional args can be found at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/scan.html
 
     Returns:
         List[Dict[str, Any]]: An array of item attributes that match the scan criteria. Each element in this array consists of an attribute name and the value for that attribute.
     """
 
     session = get_boto3_session(boto3_session)
     client = session.client(DYNAMODB_SERVICE_NAME)
@@ -119,15 +119,15 @@
     boto3_session: Session | None = None, *dynamodb_additional_args: Tuple, **dynamodb_additional_kwargs: Dict[str, Any]
 ) -> List[str]:
     """Returns an array of table names associated with the current account and endpoint
 
     Args:
         boto3_session (Session | None, optional): Custom boto3 session. Defaults to None.
 
-        Additional args can be found athttps://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_tables.html
+        Additional args can be found at https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/list_tables.html
 
     Returns:
         List[str]: The names of the tables.
     """
 
     session = get_boto3_session(boto3_session)
     client = session.client(DYNAMODB_SERVICE_NAME)
```

### Comparing `pyscora_wrangler-1.1.1/pyscora_wrangler/aws/utils.py` & `pyscora_wrangler-1.1.2/pyscora_wrangler/aws/utils.py`

 * *Files identical despite different names*

### Comparing `pyscora_wrangler-1.1.1/pyscora_wrangler/utils.py` & `pyscora_wrangler-1.1.2/pyscora_wrangler/utils.py`

 * *Files identical despite different names*

### Comparing `pyscora_wrangler-1.1.1/PKG-INFO` & `pyscora_wrangler-1.1.2/PKG-INFO`

 * *Files 20% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: pyscora-wrangler
-Version: 1.1.1
-Summary: 
+Version: 1.1.2
+Summary: Python lib for DE
 Home-page: https://github.com/oncase/pyscora-wrangler
 License: MIT
 Keywords: wrapper,scora,python,data_engineering
 Author: Oncase
 Author-email: suporte@oncase.com.br
 Maintainer: Guilherme Morone
 Maintainer-email: guilherme.morone@oncase.com.br
@@ -20,17 +20,19 @@
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Requires-Dist: asyncio (>=3.4.3,<4.0.0)
 Requires-Dist: awswrangler (>=2.20.1,<3.0.0)
-Requires-Dist: boto3 (>=1.26.107,<2.0.0)
+Requires-Dist: boto3 (>=1.26.108,<2.0.0)
+Requires-Dist: ldap3 (>=2.9.1,<3.0.0)
 Requires-Dist: pyathena (>=2.23.0,<3.0.0)
 Requires-Dist: pyyaml (>=6.0,<7.0)
+Requires-Dist: typeguard (>=3.0.2,<4.0.0)
 Project-URL: Repository, https://github.com/oncase/pyscora-wrangler
 Description-Content-Type: text/markdown
 
 # Pyscora Wrangler
 
 <p align="center">
 <img alt="Python versions" src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-brightgreen.svg">
```

#### html2text {}

```diff
@@ -1,21 +1,22 @@
-Metadata-Version: 2.1 Name: pyscora-wrangler Version: 1.1.1 Summary: Home-page:
-https://github.com/oncase/pyscora-wrangler License: MIT Keywords:
-wrapper,scora,python,data_engineering Author: Oncase Author-email:
+Metadata-Version: 2.1 Name: pyscora-wrangler Version: 1.1.2 Summary: Python lib
+for DE Home-page: https://github.com/oncase/pyscora-wrangler License: MIT
+Keywords: wrapper,scora,python,data_engineering Author: Oncase Author-email:
 suporte@oncase.com.br Maintainer: Guilherme Morone Maintainer-email:
 guilherme.morone@oncase.com.br Requires-Python: >=3.8,<4.0 Classifier: Intended
 Audience :: Developers Classifier: License :: OSI Approved :: MIT License
 Classifier: Natural Language :: English Classifier: Programming Language ::
 Python :: 3 Classifier: Programming Language :: Python :: 3.8 Classifier:
 Programming Language :: Python :: 3.9 Classifier: Programming Language ::
 Python :: 3.10 Classifier: Programming Language :: Python :: 3.11 Classifier:
 Programming Language :: Python :: 3.10 Classifier: Programming Language ::
 Python :: 3.11 Classifier: Programming Language :: Python :: 3.8 Classifier:
 Programming Language :: Python :: 3.9 Requires-Dist: asyncio (>=3.4.3,<4.0.0)
 Requires-Dist: awswrangler (>=2.20.1,<3.0.0) Requires-Dist: boto3
-(>=1.26.107,<2.0.0) Requires-Dist: pyathena (>=2.23.0,<3.0.0) Requires-Dist:
-pyyaml (>=6.0,<7.0) Project-URL: Repository, https://github.com/oncase/pyscora-
-wrangler Description-Content-Type: text/markdown # Pyscora Wrangler
+(>=1.26.108,<2.0.0) Requires-Dist: ldap3 (>=2.9.1,<3.0.0) Requires-Dist:
+pyathena (>=2.23.0,<3.0.0) Requires-Dist: pyyaml (>=6.0,<7.0) Requires-Dist:
+typeguard (>=3.0.2,<4.0.0) Project-URL: Repository, https://github.com/oncase/
+pyscora-wrangler Description-Content-Type: text/markdown # Pyscora Wrangler
              [Python versions] [License:_MIT] [Code_style:_black]
 Python package that consists mainly of wrappers for Data Engineering tasks. In
 order to see the docs, click on the module that you want inside the folder
 `pyscora_wrangler/${MODULE}`
```

