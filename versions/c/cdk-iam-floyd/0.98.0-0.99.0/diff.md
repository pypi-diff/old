# Comparing `tmp/cdk-iam-floyd-0.98.0.tar.gz` & `tmp/cdk-iam-floyd-0.99.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/github/workspace/dist/python/cdk-iam-floyd-0.98.0.tar", last modified: Wed Nov 25 02:09:42 2020, max compression
+gzip compressed data, was "/github/workspace/dist/python/cdk-iam-floyd-0.99.0.tar", last modified: Sat Nov 28 12:33:07 2020, max compression
```

## Comparing `cdk-iam-floyd-0.98.0.tar` & `cdk-iam-floyd-0.99.0.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/
--rw-r--r--   0 root         (0) root         (0)       23 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     5001 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     3700 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/README.md
--rw-r--r--   0 root         (0) root         (0)      102 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1569 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/
--rw-r--r--   0 root         (0) root         (0)  6250480 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/_jsii/
--rw-r--r--   0 root         (0) root         (0)      345 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)  2693427 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/_jsii/cdk-iam-floyd@0.98.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2020-11-25 02:09:36.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/
--rw-r--r--   0 root         (0) root         (0)     5001 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      396 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       70 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       14 2020-11-25 02:09:42.000000 cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/
+-rw-r--r--   0 root         (0) root         (0)       23 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     5001 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     3700 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/README.md
+-rw-r--r--   0 root         (0) root         (0)      102 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1569 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/
+-rw-r--r--   0 root         (0) root         (0)  6249560 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      345 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)  2692354 2020-11-28 12:33:01.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/_jsii/cdk-iam-floyd@0.99.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2020-11-28 12:33:02.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     5001 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      396 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       70 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       14 2020-11-28 12:33:07.000000 cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/top_level.txt
```

### Comparing `cdk-iam-floyd-0.98.0/PKG-INFO` & `cdk-iam-floyd-0.99.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 Metadata-Version: 2.1
 Name: cdk-iam-floyd
-Version: 0.98.0
+Version: 0.99.0
 Summary: AWS IAM policy statement generator with fluent interface for AWS CDK
 Home-page: https://github.com/udondan/iam-floyd
 Author: Daniel Schroeder
 License: Apache-2.0
 Project-URL: Source, https://github.com/udondan/iam-floyd.git
 Description: # IAM Floyd
         
         [![Source](https://img.shields.io/github/stars/udondan/iam-floyd?logo=github&label=GitHub%20Stars)](https://github.com/udondan/iam-floyd)
         [![iam-floyd](https://img.shields.io/github/v/release/udondan/iam-floyd)](https://github.com/udondan/iam-floyd)
         [![libraries.io](https://img.shields.io/badge/packages-libraries.io-yellow)](https://libraries.io/search?q=iam-floyd)
         [![Documentation](https://img.shields.io/badge/Documentation-Read%20the%20Docs-orange)](https://iam-floyd.readthedocs.io/en/latest/)
-        [![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.98.0)
+        [![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.99.0)
         [![GitHub](https://img.shields.io/github/license/udondan/iam-floyd)](https://github.com/udondan/iam-floyd/blob/main/LICENSE)
         [![Maintainability](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/maintainability)](https://codeclimate.com/github/udondan/iam-floyd/maintainability)
         
         <!-- put back - when we actually have tests
         [![Test Coverage](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/test_coverage)](https://codeclimate.com/github/udondan/iam-floyd/test_coverage)
         -->
```

### Comparing `cdk-iam-floyd-0.98.0/README.md` & `cdk-iam-floyd-0.99.0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # IAM Floyd
 
 [![Source](https://img.shields.io/github/stars/udondan/iam-floyd?logo=github&label=GitHub%20Stars)](https://github.com/udondan/iam-floyd)
 [![iam-floyd](https://img.shields.io/github/v/release/udondan/iam-floyd)](https://github.com/udondan/iam-floyd)
 [![libraries.io](https://img.shields.io/badge/packages-libraries.io-yellow)](https://libraries.io/search?q=iam-floyd)
 [![Documentation](https://img.shields.io/badge/Documentation-Read%20the%20Docs-orange)](https://iam-floyd.readthedocs.io/en/latest/)
-[![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.98.0)
+[![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.99.0)
 [![GitHub](https://img.shields.io/github/license/udondan/iam-floyd)](https://github.com/udondan/iam-floyd/blob/main/LICENSE)
 [![Maintainability](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/maintainability)](https://codeclimate.com/github/udondan/iam-floyd/maintainability)
 
 <!-- put back - when we actually have tests
 [![Test Coverage](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/test_coverage)](https://codeclimate.com/github/udondan/iam-floyd/test_coverage)
 -->
```

### Comparing `cdk-iam-floyd-0.98.0/setup.py` & `cdk-iam-floyd-0.99.0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-iam-floyd",
-    "version": "0.98.0",
+    "version": "0.99.0",
     "description": "AWS IAM policy statement generator with fluent interface for AWS CDK",
     "license": "Apache-2.0",
     "url": "https://github.com/udondan/iam-floyd",
     "long_description_content_type": "text/markdown",
     "author": "Daniel Schroeder",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_iam_floyd",
         "cdk_iam_floyd._jsii"
     ],
     "package_data": {
         "cdk_iam_floyd._jsii": [
-            "cdk-iam-floyd@0.98.0.jsii.tgz"
+            "cdk-iam-floyd@0.99.0.jsii.tgz"
         ],
         "cdk_iam_floyd": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `cdk-iam-floyd-0.98.0/src/cdk_iam_floyd/__init__.py` & `cdk-iam-floyd-0.99.0/src/cdk_iam_floyd/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 """
 # IAM Floyd
 
 [![Source](https://img.shields.io/github/stars/udondan/iam-floyd?logo=github&label=GitHub%20Stars)](https://github.com/udondan/iam-floyd)
 [![iam-floyd](https://img.shields.io/github/v/release/udondan/iam-floyd)](https://github.com/udondan/iam-floyd)
 [![libraries.io](https://img.shields.io/badge/packages-libraries.io-yellow)](https://libraries.io/search?q=iam-floyd)
 [![Documentation](https://img.shields.io/badge/Documentation-Read%20the%20Docs-orange)](https://iam-floyd.readthedocs.io/en/latest/)
-[![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.98.0)
+[![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.99.0)
 [![GitHub](https://img.shields.io/github/license/udondan/iam-floyd)](https://github.com/udondan/iam-floyd/blob/main/LICENSE)
 [![Maintainability](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/maintainability)](https://codeclimate.com/github/udondan/iam-floyd/maintainability)
 
 <!-- put back - when we actually have tests
 [![Test Coverage](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/test_coverage)](https://codeclimate.com/github/udondan/iam-floyd/test_coverage)
 -->
 
@@ -1819,30 +1819,21 @@
             resources=resources,
             sid=sid,
         )
 
         jsii.create(PolicyStatementWithEffect, self, [props])
 
     @jsii.member(jsii_name="allow")
-    def allow(
-        self,
-        explicit: typing.Optional[builtins.bool] = None,
-    ) -> "PolicyStatementWithEffect":
+    def allow(self) -> "PolicyStatementWithEffect":
         """Allow the actions in this statement.
 
-        The default ``Effect`` is ``Allow``. Therefore by default the ``Effect`` key
-        will not be present in the statement. To enforce the ``Effect`` key, pass
-        ``true`` as argument.
-
-        :param explicit: Enforce the ``Effect`` key to be present in the statement.
-
         stability
         :stability: experimental
         """
-        return jsii.invoke(self, "allow", [explicit])
+        return jsii.invoke(self, "allow", [])
 
     @jsii.member(jsii_name="deny")
     def deny(self) -> "PolicyStatementWithEffect":
         """Deny the actions in this statement.
 
         stability
         :stability: experimental
@@ -1856,30 +1847,14 @@
         Only relevant for the main package. In CDK mode this only calls super.
 
         stability
         :stability: experimental
         """
         return jsii.invoke(self, "toJSON", [])
 
-    @builtins.property # type: ignore
-    @jsii.member(jsii_name="explicitAllow")
-    def _explicit_allow(self) -> builtins.bool:
-        """When ``true``, an "Effect: Allow" will be put into the policy statement.
-
-        By default it will be omitted, since ``Allow`` is the default anyway.
-
-        stability
-        :stability: experimental
-        """
-        return jsii.get(self, "explicitAllow")
-
-    @_explicit_allow.setter # type: ignore
-    def _explicit_allow(self, value: builtins.bool) -> None:
-        jsii.set(self, "explicitAllow", value)
-
 
 class PolicyStatementWithPrincipal(
     PolicyStatementWithEffect,
     metaclass=jsii.JSIIMeta,
     jsii_type="cdk-iam-floyd.PolicyStatementWithPrincipal",
 ):
     """Adds "principal" functionality to the Policy Statement.
```

### Comparing `cdk-iam-floyd-0.98.0/src/cdk_iam_floyd.egg-info/PKG-INFO` & `cdk-iam-floyd-0.99.0/src/cdk_iam_floyd.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 Metadata-Version: 2.1
 Name: cdk-iam-floyd
-Version: 0.98.0
+Version: 0.99.0
 Summary: AWS IAM policy statement generator with fluent interface for AWS CDK
 Home-page: https://github.com/udondan/iam-floyd
 Author: Daniel Schroeder
 License: Apache-2.0
 Project-URL: Source, https://github.com/udondan/iam-floyd.git
 Description: # IAM Floyd
         
         [![Source](https://img.shields.io/github/stars/udondan/iam-floyd?logo=github&label=GitHub%20Stars)](https://github.com/udondan/iam-floyd)
         [![iam-floyd](https://img.shields.io/github/v/release/udondan/iam-floyd)](https://github.com/udondan/iam-floyd)
         [![libraries.io](https://img.shields.io/badge/packages-libraries.io-yellow)](https://libraries.io/search?q=iam-floyd)
         [![Documentation](https://img.shields.io/badge/Documentation-Read%20the%20Docs-orange)](https://iam-floyd.readthedocs.io/en/latest/)
-        [![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.98.0)
+        [![CDKio](https://img.shields.io/badge/awscdk.io-cdk--iam--floyd-orange)](https://awscdk.io/packages/cdk-iam-floyd@0.99.0)
         [![GitHub](https://img.shields.io/github/license/udondan/iam-floyd)](https://github.com/udondan/iam-floyd/blob/main/LICENSE)
         [![Maintainability](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/maintainability)](https://codeclimate.com/github/udondan/iam-floyd/maintainability)
         
         <!-- put back - when we actually have tests
         [![Test Coverage](https://api.codeclimate.com/v1/badges/cdb84b5646c6805b1a23/test_coverage)](https://codeclimate.com/github/udondan/iam-floyd/test_coverage)
         -->
```

