# Comparing `tmp/mypy-boto3-cloudformation-1.26.57.tar.gz` & `tmp/mypy-boto3-cloudformation-1.26.60.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mypy-boto3-cloudformation-1.26.57.tar", last modified: Wed Jan 25 20:48:07 2023, max compression
+gzip compressed data, was "mypy-boto3-cloudformation-1.26.60.tar", last modified: Mon Jan 30 21:06:23 2023, max compression
```

## Comparing `mypy-boto3-cloudformation-1.26.57.tar` & `mypy-boto3-cloudformation-1.26.60.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 20:48:07.696256 mypy-boto3-cloudformation-1.26.57/
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    29888 2023-01-25 20:48:07.696256 mypy-boto3-cloudformation-1.26.57/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    28373 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 20:48:07.680256 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/
--rw-r--r--   0 runner    (1001) docker     (123)     5317 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5315 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/__init__.pyi
--rw-r--r--   0 runner    (1001) docker     (123)      935 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)    63470 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/client.py
--rw-r--r--   0 runner    (1001) docker     (123)    63375 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/client.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    17908 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/literals.py
--rw-r--r--   0 runner    (1001) docker     (123)    17906 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/literals.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    17280 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/paginator.py
--rw-r--r--   0 runner    (1001) docker     (123)    17264 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/paginator.pyi
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    22975 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/service_resource.py
--rw-r--r--   0 runner    (1001) docker     (123)    22931 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/service_resource.pyi
--rw-r--r--   0 runner    (1001) docker     (123)    90523 2023-01-25 20:46:50.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/type_defs.py
--rw-r--r--   0 runner    (1001) docker     (123)    90410 2023-01-25 20:46:49.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/type_defs.pyi
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/version.py
--rw-r--r--   0 runner    (1001) docker     (123)     8787 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/waiter.py
--rw-r--r--   0 runner    (1001) docker     (123)     8779 2023-01-25 20:46:48.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/waiter.pyi
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-25 20:48:07.680256 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    29888 2023-01-25 20:48:07.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      979 2023-01-25 20:48:07.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-25 20:48:07.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-25 20:48:07.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-01-25 20:48:07.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-01-25 20:48:07.000000 mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-25 20:48:07.696256 mypy-boto3-cloudformation-1.26.57/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-01-25 20:46:47.000000 mypy-boto3-cloudformation-1.26.57/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 21:06:23.546471 mypy-boto3-cloudformation-1.26.60/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    29888 2023-01-30 21:06:23.546471 mypy-boto3-cloudformation-1.26.60/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    28373 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 21:06:23.538471 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/
+-rw-r--r--   0 runner    (1001) docker     (123)     5317 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5315 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/__init__.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)      935 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63470 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63375 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/client.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    17908 2023-01-30 21:05:15.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/literals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17906 2023-01-30 21:05:15.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/literals.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    17280 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/paginator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17264 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/paginator.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    22975 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/service_resource.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22931 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/service_resource.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)    90553 2023-01-30 21:05:17.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/type_defs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    90440 2023-01-30 21:05:16.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/type_defs.pyi
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8787 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/waiter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8779 2023-01-30 21:05:14.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/waiter.pyi
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 21:06:23.546471 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    29888 2023-01-30 21:06:23.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      979 2023-01-30 21:06:23.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 21:06:23.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 21:06:23.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-01-30 21:06:23.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-01-30 21:06:23.000000 mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 21:06:23.546471 mypy-boto3-cloudformation-1.26.60/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-01-30 21:05:13.000000 mypy-boto3-cloudformation-1.26.60/setup.py
```

### Comparing `mypy-boto3-cloudformation-1.26.57/LICENSE` & `mypy-boto3-cloudformation-1.26.60/LICENSE`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/PKG-INFO` & `mypy-boto3-cloudformation-1.26.60/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mypy-boto3-cloudformation
-Version: 1.26.57
-Summary: Type annotations for boto3.CloudFormation 1.26.57 service generated with mypy-boto3-builder 7.12.3
+Version: 1.26.60
+Summary: Type annotations for boto3.CloudFormation 1.26.60 service generated with mypy-boto3-builder 7.12.3
 Home-page: https://github.com/youtype/mypy_boto3_builder
 Author: Vlad Emelianov
 Author-email: vlad.emelianov.nz@gmail.com
 License: MIT License
 Project-URL: Documentation, https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/
 Project-URL: Source, https://github.com/youtype/mypy_boto3_builder
 Project-URL: Tracker, https://github.com/youtype/mypy_boto3_builder/issues
@@ -38,15 +38,15 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-cloudformation.svg?color=blue)](https://pypi.org/project/mypy-boto3-cloudformation)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-cloudformation?color=blue)](https://pypistats.org/packages/mypy-boto3-cloudformation)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Type annotations for
-[boto3.CloudFormation 1.26.57](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
+[boto3.CloudFormation 1.26.60](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
 service compatible with [VSCode](https://code.visualstudio.com/),
 [PyCharm](https://www.jetbrains.com/pycharm/),
 [Emacs](https://www.gnu.org/software/emacs/),
 [Sublime Text](https://www.sublimetext.com/),
 [mypy](https://github.com/python/mypy),
 [pyright](https://github.com/microsoft/pyright) and other tools.
```

### Comparing `mypy-boto3-cloudformation-1.26.57/README.md` & `mypy-boto3-cloudformation-1.26.60/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-cloudformation.svg?color=blue)](https://pypi.org/project/mypy-boto3-cloudformation)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-cloudformation?color=blue)](https://pypistats.org/packages/mypy-boto3-cloudformation)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Type annotations for
-[boto3.CloudFormation 1.26.57](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
+[boto3.CloudFormation 1.26.60](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
 service compatible with [VSCode](https://code.visualstudio.com/),
 [PyCharm](https://www.jetbrains.com/pycharm/),
 [Emacs](https://www.gnu.org/software/emacs/),
 [Sublime Text](https://www.sublimetext.com/),
 [mypy](https://github.com/python/mypy),
 [pyright](https://github.com/microsoft/pyright) and other tools.
```

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/__init__.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/__init__.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/__init__.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/__init__.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/__main__.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/__main__.py`

 * *Files 3% similar despite different names*

```diff
@@ -5,28 +5,28 @@
 
 
 def print_info() -> None:
     """
     Print package info to stdout.
     """
     print(
-        "Type annotations for boto3.CloudFormation 1.26.57\nVersion:         1.26.57\nBuilder"
+        "Type annotations for boto3.CloudFormation 1.26.60\nVersion:         1.26.60\nBuilder"
         " version: 7.12.3\nDocs:           "
         " https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation//\nBoto3 docs:     "
         " https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation\nOther"
         " services:  https://pypi.org/project/boto3-stubs/\nChangelog:      "
         " https://github.com/youtype/mypy_boto3_builder/releases"
     )
 
 
 def print_version() -> None:
     """
     Print package version to stdout.
     """
-    print("1.26.57")
+    print("1.26.60")
 
 
 def main() -> None:
     """
     Main CLI entrypoint.
     """
     if "--version" in sys.argv:
```

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/client.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/client.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/client.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/client.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/literals.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/literals.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/literals.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/literals.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/paginator.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/paginator.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/paginator.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/paginator.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/service_resource.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/service_resource.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/service_resource.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/service_resource.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/type_defs.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/type_defs.py`

 * *Files 0% similar despite different names*

```diff
@@ -2926,14 +2926,15 @@
         "AdministrationRoleARN": str,
         "ExecutionRoleName": str,
         "StackSetDriftDetectionDetails": StackSetDriftDetectionDetailsTypeDef,
         "AutoDeployment": AutoDeploymentTypeDef,
         "PermissionModel": PermissionModelsType,
         "OrganizationalUnitIds": List[str],
         "ManagedExecution": ManagedExecutionTypeDef,
+        "Regions": List[str],
     },
     total=False,
 )
 
 StackSetOperationSummaryTypeDef = TypedDict(
     "StackSetOperationSummaryTypeDef",
     {
```

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/type_defs.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/type_defs.pyi`

 * *Files 0% similar despite different names*

```diff
@@ -2823,14 +2823,15 @@
         "AdministrationRoleARN": str,
         "ExecutionRoleName": str,
         "StackSetDriftDetectionDetails": StackSetDriftDetectionDetailsTypeDef,
         "AutoDeployment": AutoDeploymentTypeDef,
         "PermissionModel": PermissionModelsType,
         "OrganizationalUnitIds": List[str],
         "ManagedExecution": ManagedExecutionTypeDef,
+        "Regions": List[str],
     },
     total=False,
 )
 
 StackSetOperationSummaryTypeDef = TypedDict(
     "StackSetOperationSummaryTypeDef",
     {
```

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/waiter.py` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/waiter.py`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation/waiter.pyi` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation/waiter.pyi`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/PKG-INFO` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: mypy-boto3-cloudformation
-Version: 1.26.57
-Summary: Type annotations for boto3.CloudFormation 1.26.57 service generated with mypy-boto3-builder 7.12.3
+Version: 1.26.60
+Summary: Type annotations for boto3.CloudFormation 1.26.60 service generated with mypy-boto3-builder 7.12.3
 Home-page: https://github.com/youtype/mypy_boto3_builder
 Author: Vlad Emelianov
 Author-email: vlad.emelianov.nz@gmail.com
 License: MIT License
 Project-URL: Documentation, https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/
 Project-URL: Source, https://github.com/youtype/mypy_boto3_builder
 Project-URL: Tracker, https://github.com/youtype/mypy_boto3_builder/issues
@@ -38,15 +38,15 @@
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypy-boto3-cloudformation.svg?color=blue)](https://pypi.org/project/mypy-boto3-cloudformation)
 [![Docs](https://img.shields.io/readthedocs/mypy-boto3-builder.svg?color=blue)](https://mypy-boto3-builder.readthedocs.io/)
 [![PyPI - Downloads](https://img.shields.io/pypi/dm/mypy-boto3-cloudformation?color=blue)](https://pypistats.org/packages/mypy-boto3-cloudformation)
 
 ![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)
 
 Type annotations for
-[boto3.CloudFormation 1.26.57](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
+[boto3.CloudFormation 1.26.60](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudformation.html#CloudFormation)
 service compatible with [VSCode](https://code.visualstudio.com/),
 [PyCharm](https://www.jetbrains.com/pycharm/),
 [Emacs](https://www.gnu.org/software/emacs/),
 [Sublime Text](https://www.sublimetext.com/),
 [mypy](https://github.com/python/mypy),
 [pyright](https://github.com/microsoft/pyright) and other tools.
```

### Comparing `mypy-boto3-cloudformation-1.26.57/mypy_boto3_cloudformation.egg-info/SOURCES.txt` & `mypy-boto3-cloudformation-1.26.60/mypy_boto3_cloudformation.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mypy-boto3-cloudformation-1.26.57/setup.py` & `mypy-boto3-cloudformation-1.26.60/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -6,22 +6,22 @@
 from setuptools import setup
 
 LONG_DESCRIPTION = open(dirname(abspath(__file__)) + "/README.md", "r").read()
 
 
 setup(
     name="mypy-boto3-cloudformation",
-    version="1.26.57",
+    version="1.26.60",
     packages=["mypy_boto3_cloudformation"],
     url="https://github.com/youtype/mypy_boto3_builder",
     license="MIT License",
     author="Vlad Emelianov",
     author_email="vlad.emelianov.nz@gmail.com",
     description=(
-        "Type annotations for boto3.CloudFormation 1.26.57 service generated with"
+        "Type annotations for boto3.CloudFormation 1.26.60 service generated with"
         " mypy-boto3-builder 7.12.3"
     ),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "Environment :: Console",
         "License :: OSI Approved :: MIT License",
```

