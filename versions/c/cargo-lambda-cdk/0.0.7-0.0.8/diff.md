# Comparing `tmp/cargo-lambda-cdk-0.0.7.tar.gz` & `tmp/cargo-lambda-cdk-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cargo-lambda-cdk-0.0.7.tar", last modified: Thu Apr  6 23:59:05 2023, max compression
+gzip compressed data, was "cargo-lambda-cdk-0.0.8.tar", last modified: Fri Apr  7 00:18:27 2023, max compression
```

## Comparing `cargo-lambda-cdk-0.0.7.tar` & `cargo-lambda-cdk-0.0.8.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/
--rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     5050 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4130 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1753 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/
--rw-r--r--   0 runner    (1001) docker     (123)    86374 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      399 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   184309 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/_jsii/cargo-lambda-cdk@0.0.7.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 23:58:50.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:59:05.719474 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5050 2023-04-06 23:59:05.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      433 2023-04-06 23:59:05.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 23:59:05.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-06 23:59:05.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 23:59:05.000000 cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:18:27.797302 cargo-lambda-cdk-0.0.8/
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5081 2023-04-07 00:18:27.797302 cargo-lambda-cdk-0.0.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4130 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 00:18:27.797302 cargo-lambda-cdk-0.0.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1803 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:18:27.793302 cargo-lambda-cdk-0.0.8/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:18:27.797302 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/
+-rw-r--r--   0 runner    (1001) docker     (123)    86374 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:18:27.797302 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      399 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   195676 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/_jsii/cargo-lambda-cdk@0.0.8.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:18:13.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 00:18:27.797302 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5081 2023-04-07 00:18:27.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      433 2023-04-07 00:18:27.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 00:18:27.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-07 00:18:27.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-07 00:18:27.000000 cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/top_level.txt
```

### Comparing `cargo-lambda-cdk-0.0.7/LICENSE` & `cargo-lambda-cdk-0.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `cargo-lambda-cdk-0.0.7/PKG-INFO` & `cargo-lambda-cdk-0.0.8/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: cargo-lambda-cdk
-Version: 0.0.7
+Version: 0.0.8
 Summary: CDK Construct to build Rust functions with Cargo Lambda
 Home-page: https://github.com/cargo-lambda/cargo-lambda-cdk.git
 Author: David Calavera
 License: MIT
 Project-URL: Source, https://github.com/cargo-lambda/cargo-lambda-cdk.git
-Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: JavaScript
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Typing :: Typed
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: License :: OSI Approved
 Requires-Python: ~=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
@@ -148,9 +148,7 @@
 Depending on how you structure your Rust application, you may want to change the `assetHashType` parameter.
 By default this parameter is set to `AssetHashType.OUTPUT` which means that the CDK will calculate the asset hash
 (and determine whether or not your code has changed) based on the Rust executable that is created.
 
 If you specify `AssetHashType.SOURCE`, the CDK will calculate the asset hash by looking at the folder
 that contains your `Cargo.toml` file. If you are deploying a single Lambda function, or you want to redeploy
 all of your functions if anything changes, then `AssetHashType.SOURCE` will probaby work.
-
-
```

### Comparing `cargo-lambda-cdk-0.0.7/README.md` & `cargo-lambda-cdk-0.0.8/README.md`

 * *Files identical despite different names*

### Comparing `cargo-lambda-cdk-0.0.7/setup.py` & `cargo-lambda-cdk-0.0.8/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cargo-lambda-cdk",
-    "version": "0.0.7",
+    "version": "0.0.8",
     "description": "CDK Construct to build Rust functions with Cargo Lambda",
     "license": "MIT",
     "url": "https://github.com/cargo-lambda/cargo-lambda-cdk.git",
     "long_description_content_type": "text/markdown",
     "author": "David Calavera",
     "bdist_wheel": {
         "universal": true
@@ -22,37 +22,38 @@
     },
     "packages": [
         "cargo_lambda_cdk",
         "cargo_lambda_cdk._jsii"
     ],
     "package_data": {
         "cargo_lambda_cdk._jsii": [
-            "cargo-lambda-cdk@0.0.7.jsii.tgz"
+            "cargo-lambda-cdk@0.0.8.jsii.tgz"
         ],
         "cargo_lambda_cdk": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
         "aws-cdk-lib>=2.1.0, <3.0.0",
         "constructs>=10.0.5, <11.0.0",
-        "jsii>=1.72.0, <2.0.0",
+        "jsii>=1.80.0, <2.0.0",
         "publication>=0.0.3",
         "typeguard~=2.13.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
         "Operating System :: OS Independent",
         "Programming Language :: JavaScript",
         "Programming Language :: Python :: 3 :: Only",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
         "Typing :: Typed",
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved"
     ],
     "scripts": []
 }
 """
```

### Comparing `cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk/__init__.py` & `cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk/__init__.py`

 * *Files identical despite different names*

### Comparing `cargo-lambda-cdk-0.0.7/src/cargo_lambda_cdk.egg-info/PKG-INFO` & `cargo-lambda-cdk-0.0.8/src/cargo_lambda_cdk.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 Metadata-Version: 2.1
 Name: cargo-lambda-cdk
-Version: 0.0.7
+Version: 0.0.8
 Summary: CDK Construct to build Rust functions with Cargo Lambda
 Home-page: https://github.com/cargo-lambda/cargo-lambda-cdk.git
 Author: David Calavera
 License: MIT
 Project-URL: Source, https://github.com/cargo-lambda/cargo-lambda-cdk.git
-Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: JavaScript
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Typing :: Typed
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: License :: OSI Approved
 Requires-Python: ~=3.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
@@ -148,9 +148,7 @@
 Depending on how you structure your Rust application, you may want to change the `assetHashType` parameter.
 By default this parameter is set to `AssetHashType.OUTPUT` which means that the CDK will calculate the asset hash
 (and determine whether or not your code has changed) based on the Rust executable that is created.
 
 If you specify `AssetHashType.SOURCE`, the CDK will calculate the asset hash by looking at the folder
 that contains your `Cargo.toml` file. If you are deploying a single Lambda function, or you want to redeploy
 all of your functions if anything changes, then `AssetHashType.SOURCE` will probaby work.
-
-
```

