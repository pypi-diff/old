# Comparing `tmp/iam-floyd-0.98.0.tar.gz` & `tmp/iam-floyd-0.99.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/github/workspace/dist/python/iam-floyd-0.98.0.tar", last modified: Wed Nov 25 02:07:12 2020, max compression
+gzip compressed data, was "/github/workspace/dist/python/iam-floyd-0.99.0.tar", last modified: Sat Nov 28 12:30:30 2020, max compression
```

## Comparing `iam-floyd-0.98.0.tar` & `iam-floyd-0.99.0.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/
--rw-r--r--   0 root         (0) root         (0)       23 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     4985 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     3700 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/README.md
--rw-r--r--   0 root         (0) root         (0)      102 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1490 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/src/
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/src/iam_floyd/
--rw-r--r--   0 root         (0) root         (0)  5730936 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/src/iam_floyd/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/src/iam_floyd/_jsii/
--rw-r--r--   0 root         (0) root         (0)      307 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/src/iam_floyd/_jsii/__init__.py
--rw-r--r--   0 root         (0) root         (0)  2688483 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/src/iam_floyd/_jsii/iam-floyd@0.98.0.jsii.tgz
--rw-r--r--   0 root         (0) root         (0)        1 2020-11-25 02:07:04.000000 iam-floyd-0.98.0/src/iam_floyd/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-25 02:07:12.000000 iam-floyd-0.98.0/src/iam_floyd.egg-info/
--rw-r--r--   0 root         (0) root         (0)     4985 2020-11-25 02:07:11.000000 iam-floyd-0.98.0/src/iam_floyd.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      356 2020-11-25 02:07:11.000000 iam-floyd-0.98.0/src/iam_floyd.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2020-11-25 02:07:11.000000 iam-floyd-0.98.0/src/iam_floyd.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       39 2020-11-25 02:07:11.000000 iam-floyd-0.98.0/src/iam_floyd.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       10 2020-11-25 02:07:11.000000 iam-floyd-0.98.0/src/iam_floyd.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/
+-rw-r--r--   0 root         (0) root         (0)       23 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     4985 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     3700 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/README.md
+-rw-r--r--   0 root         (0) root         (0)      102 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     1490 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd/
+-rw-r--r--   0 root         (0) root         (0)  5730016 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/src/iam_floyd/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd/_jsii/
+-rw-r--r--   0 root         (0) root         (0)      307 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/src/iam_floyd/_jsii/__init__.py
+-rw-r--r--   0 root         (0) root         (0)  2687396 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/src/iam_floyd/_jsii/iam-floyd@0.99.0.jsii.tgz
+-rw-r--r--   0 root         (0) root         (0)        1 2020-11-28 12:30:24.000000 iam-floyd-0.99.0/src/iam_floyd/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     4985 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      356 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       39 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       10 2020-11-28 12:30:30.000000 iam-floyd-0.99.0/src/iam_floyd.egg-info/top_level.txt
```

### Comparing `iam-floyd-0.98.0/PKG-INFO` & `iam-floyd-0.99.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 Metadata-Version: 2.1
 Name: iam-floyd
-Version: 0.98.0
+Version: 0.99.0
 Summary: AWS IAM policy statement generator with fluent interface
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

### Comparing `iam-floyd-0.98.0/README.md` & `iam-floyd-0.99.0/README.md`

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

### Comparing `iam-floyd-0.98.0/setup.py` & `iam-floyd-0.99.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "iam-floyd",
-    "version": "0.98.0",
+    "version": "0.99.0",
     "description": "AWS IAM policy statement generator with fluent interface",
     "license": "Apache-2.0",
     "url": "https://github.com/udondan/iam-floyd",
     "long_description_content_type": "text/markdown",
     "author": "Daniel Schroeder",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "iam_floyd",
         "iam_floyd._jsii"
     ],
     "package_data": {
         "iam_floyd._jsii": [
-            "iam-floyd@0.98.0.jsii.tgz"
+            "iam-floyd@0.99.0.jsii.tgz"
         ],
         "iam_floyd": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `iam-floyd-0.98.0/src/iam_floyd/__init__.py` & `iam-floyd-0.99.0/src/iam_floyd/__init__.py`

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
 
@@ -1706,30 +1706,21 @@
 
         stability
         :stability: experimental
         """
         jsii.create(PolicyStatementWithEffect, self, [sid])
 
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
@@ -1756,30 +1747,14 @@
         """
         return jsii.get(self, "effect")
 
     @effect.setter # type: ignore
     def effect(self, value: "Effect") -> None:
         jsii.set(self, "effect", value)
 
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
     jsii_type="iam-floyd.PolicyStatementWithPrincipal",
 ):
     """Adds "principal" functionality to the Policy Statement.
```

### Comparing `iam-floyd-0.98.0/src/iam_floyd.egg-info/PKG-INFO` & `iam-floyd-0.99.0/src/iam_floyd.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 Metadata-Version: 2.1
 Name: iam-floyd
-Version: 0.98.0
+Version: 0.99.0
 Summary: AWS IAM policy statement generator with fluent interface
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

