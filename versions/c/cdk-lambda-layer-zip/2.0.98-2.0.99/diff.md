# Comparing `tmp/cdk-lambda-layer-zip-2.0.98.tar.gz` & `tmp/cdk-lambda-layer-zip-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-lambda-layer-zip-2.0.98.tar", last modified: Sat May 28 00:51:31 2022, max compression
+gzip compressed data, was "cdk-lambda-layer-zip-2.0.99.tar", last modified: Sun May 29 00:51:56 2022, max compression
```

## Comparing `cdk-lambda-layer-zip-2.0.98.tar` & `cdk-lambda-layer-zip-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-28 00:51:31.186628 cdk-lambda-layer-zip-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     1993 2022-05-28 00:51:31.186628 cdk-lambda-layer-zip-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1063 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-28 00:51:31.186628 cdk-lambda-layer-zip-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1755 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-28 00:51:31.178628 cdk-lambda-layer-zip-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-28 00:51:31.178628 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/
--rw-r--r--   0 runner    (1001) docker     (121)     1718 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-28 00:51:31.178628 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      388 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  6773538 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/_jsii/cdk-lambda-layer-zip@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-28 00:51:19.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-28 00:51:31.178628 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     1993 2022-05-28 00:51:30.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      474 2022-05-28 00:51:31.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-28 00:51:30.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-28 00:51:31.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       21 2022-05-28 00:51:31.000000 cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-29 00:51:56.413483 cdk-lambda-layer-zip-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     1993 2022-05-29 00:51:56.413483 cdk-lambda-layer-zip-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1063 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-29 00:51:56.413483 cdk-lambda-layer-zip-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1755 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-29 00:51:56.405483 cdk-lambda-layer-zip-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-29 00:51:56.409483 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/
+-rw-r--r--   0 runner    (1001) docker     (121)     1718 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-29 00:51:56.409483 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      388 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  6773537 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/_jsii/cdk-lambda-layer-zip@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-29 00:51:42.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-29 00:51:56.409483 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     1993 2022-05-29 00:51:55.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      474 2022-05-29 00:51:56.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-29 00:51:55.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-29 00:51:56.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       21 2022-05-29 00:51:56.000000 cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/top_level.txt
```

### Comparing `cdk-lambda-layer-zip-2.0.98/LICENSE` & `cdk-lambda-layer-zip-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-zip-2.0.98/PKG-INFO` & `cdk-lambda-layer-zip-2.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-layer-zip
-Version: 2.0.98
+Version: 2.0.99
 Summary: Lambda Layer for tar gz 7z
 Home-page: https://github.com/clarencetw/cdk-lambda-layer-zip.git
 Author: clarencetw<mr.lin.clarence@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/clarencetw/cdk-lambda-layer-zip.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-lambda-layer-zip-2.0.98/README.md` & `cdk-lambda-layer-zip-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-zip-2.0.98/setup.py` & `cdk-lambda-layer-zip-2.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-lambda-layer-zip",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "Lambda Layer for tar gz 7z",
     "license": "Apache-2.0",
     "url": "https://github.com/clarencetw/cdk-lambda-layer-zip.git",
     "long_description_content_type": "text/markdown",
     "author": "clarencetw<mr.lin.clarence@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_lambda_layer_zip",
         "cdk_lambda_layer_zip._jsii"
     ],
     "package_data": {
         "cdk_lambda_layer_zip._jsii": [
-            "cdk-lambda-layer-zip@2.0.98.jsii.tgz"
+            "cdk-lambda-layer-zip@2.0.99.jsii.tgz"
         ],
         "cdk_lambda_layer_zip": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/__init__.py` & `cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip/_jsii/cdk-lambda-layer-zip@2.0.98.jsii.tgz` & `cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip/_jsii/cdk-lambda-layer-zip@2.0.99.jsii.tgz`

 * *Files 2% similar despite different names*

#### Comparing `cdk-lambda-layer-zip@2.0.98.jsii.tgz-content` & `cdk-lambda-layer-zip@2.0.99.jsii.tgz-content`

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.9444444444444444%*

 * *Differences: {"'fingerprint'": "'TzzxBcXKS8Fln+1qIPwP+n2Yv4cDTm8TreA1pb3V2JA='", "'version'": "'2.0.99'"}*

```diff
@@ -2771,15 +2771,15 @@
             }
         }
     },
     "description": "Lambda Layer for tar gz 7z",
     "docs": {
         "stability": "stable"
     },
-    "fingerprint": "G5Xq2UNO7cdP8GZTFWN4qKRkPkWjs16rAQgbrkm4IE4=",
+    "fingerprint": "TzzxBcXKS8Fln+1qIPwP+n2Yv4cDTm8TreA1pb3V2JA=",
     "homepage": "https://github.com/clarencetw/cdk-lambda-layer-zip.git",
     "jsiiVersion": "1.59.0 (build eb02c92)",
     "keywords": [
         "7z",
         "aws",
         "cdk",
         "gz",
@@ -2849,9 +2849,9 @@
                 "filename": "src/index.ts",
                 "line": 10
             },
             "name": "ZipLayer",
             "symbolId": "src/index:ZipLayer"
         }
     },
-    "version": "2.0.98"
+    "version": "2.0.99"
 }
```

##### package/lib/index.js

###### js-beautify {}

```diff
@@ -23,15 +23,15 @@
         });
     }
 }
 exports.ZipLayer = ZipLayer;
 _a = JSII_RTTI_SYMBOL_1;
 ZipLayer[_a] = {
     fqn: "cdk-lambda-layer-zip.ZipLayer",
-    version: "2.0.98"
+    version: "2.0.99"
 };
 
 function hashFile(fileName) {
     return crypto
         .createHash('sha256')
         .update(fs.readFileSync(fileName))
         .digest('hex');
```

##### package/package.json

###### Pretty-printed

 * *Similarity: 0.9715909090909091%*

 * *Differences: {"'devDependencies'": "{'projen': '^0.56.37'}", "'version'": "'2.0.99'"}*

```diff
@@ -25,15 +25,15 @@
         "jest-junit": "^13",
         "jsii": "^1.59.0",
         "jsii-diff": "^1.59.0",
         "jsii-docgen": "^4.2.44",
         "jsii-pacmak": "^1.59.0",
         "json-schema": "^0.4.0",
         "npm-check-updates": "^12",
-        "projen": "^0.56.36",
+        "projen": "^0.56.37",
         "standard-version": "^9",
         "ts-jest": "^27",
         "typescript": "^4.7.2"
     },
     "jest": {
         "clearMocks": true,
         "collectCoverage": true,
@@ -133,9 +133,9 @@
         "test:watch": "npx projen test:watch",
         "unbump": "npx projen unbump",
         "upgrade": "npx projen upgrade",
         "watch": "npx projen watch"
     },
     "stability": "stable",
     "types": "lib/index.d.ts",
-    "version": "2.0.98"
+    "version": "2.0.99"
 }
```

##### package/changelog.md

```diff
@@ -1,2 +1,2 @@
 
-### [2.0.98](https://github.com/clarencetw/cdk-lambda-layer-zip/compare/v2.0.97...v2.0.98) (2022-05-28)
+### [2.0.99](https://github.com/clarencetw/cdk-lambda-layer-zip/compare/v2.0.98...v2.0.99) (2022-05-29)
```

##### package/releasetag.txt

```diff
@@ -1 +1 @@
-v2.0.98
+v2.0.99
```

##### package/version.txt

```diff
@@ -1 +1 @@
-2.0.98
+2.0.99
```

### Comparing `cdk-lambda-layer-zip-2.0.98/src/cdk_lambda_layer_zip.egg-info/PKG-INFO` & `cdk-lambda-layer-zip-2.0.99/src/cdk_lambda_layer_zip.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-layer-zip
-Version: 2.0.98
+Version: 2.0.99
 Summary: Lambda Layer for tar gz 7z
 Home-page: https://github.com/clarencetw/cdk-lambda-layer-zip.git
 Author: clarencetw<mr.lin.clarence@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/clarencetw/cdk-lambda-layer-zip.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

