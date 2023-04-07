# Comparing `tmp/cdk-lambda-layer-curl-2.0.98.tar.gz` & `tmp/cdk-lambda-layer-curl-2.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-lambda-layer-curl-2.0.98.tar", last modified: Tue May 17 01:46:40 2022, max compression
+gzip compressed data, was "cdk-lambda-layer-curl-2.0.99.tar", last modified: Wed May 18 01:30:28 2022, max compression
```

## Comparing `cdk-lambda-layer-curl-2.0.98.tar` & `cdk-lambda-layer-curl-2.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-17 01:46:40.751838 cdk-lambda-layer-curl-2.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2004 2022-05-17 01:46:40.751838 cdk-lambda-layer-curl-2.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1072 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-17 01:46:40.751838 cdk-lambda-layer-curl-2.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-17 01:46:40.747837 cdk-lambda-layer-curl-2.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-17 01:46:40.751838 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/
--rw-r--r--   0 runner    (1001) docker     (121)     1724 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-17 01:46:40.751838 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)  1569979 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/_jsii/cdk-lambda-layer-curl@2.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-17 01:46:29.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-17 01:46:40.751838 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2004 2022-05-17 01:46:40.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      484 2022-05-17 01:46:40.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-17 01:46:40.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-17 01:46:40.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       22 2022-05-17 01:46:40.000000 cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-18 01:30:28.292109 cdk-lambda-layer-curl-2.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     2004 2022-05-18 01:30:28.292109 cdk-lambda-layer-curl-2.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1072 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-05-18 01:30:28.292109 cdk-lambda-layer-curl-2.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1762 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-18 01:30:28.288109 cdk-lambda-layer-curl-2.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-18 01:30:28.288109 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/
+-rw-r--r--   0 runner    (1001) docker     (121)     1724 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-18 01:30:28.292109 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)  1569980 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/_jsii/cdk-lambda-layer-curl@2.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-18 01:30:16.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-05-18 01:30:28.288109 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     2004 2022-05-18 01:30:27.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      484 2022-05-18 01:30:28.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-05-18 01:30:27.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-05-18 01:30:28.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       22 2022-05-18 01:30:28.000000 cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/top_level.txt
```

### Comparing `cdk-lambda-layer-curl-2.0.98/LICENSE` & `cdk-lambda-layer-curl-2.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-curl-2.0.98/PKG-INFO` & `cdk-lambda-layer-curl-2.0.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-layer-curl
-Version: 2.0.98
+Version: 2.0.99
 Summary: For lambda layer use curl
 Home-page: https://github.com/clarencetw/cdk-lambda-layer-curl.git
 Author: clarencetw<mr.lin.clarence@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/clarencetw/cdk-lambda-layer-curl.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-lambda-layer-curl-2.0.98/README.md` & `cdk-lambda-layer-curl-2.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-curl-2.0.98/setup.py` & `cdk-lambda-layer-curl-2.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-lambda-layer-curl",
-    "version": "2.0.98",
+    "version": "2.0.99",
     "description": "For lambda layer use curl",
     "license": "Apache-2.0",
     "url": "https://github.com/clarencetw/cdk-lambda-layer-curl.git",
     "long_description_content_type": "text/markdown",
     "author": "clarencetw<mr.lin.clarence@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_lambda_layer_curl",
         "cdk_lambda_layer_curl._jsii"
     ],
     "package_data": {
         "cdk_lambda_layer_curl._jsii": [
-            "cdk-lambda-layer-curl@2.0.98.jsii.tgz"
+            "cdk-lambda-layer-curl@2.0.99.jsii.tgz"
         ],
         "cdk_lambda_layer_curl": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/__init__.py` & `cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl/_jsii/cdk-lambda-layer-curl@2.0.98.jsii.tgz` & `cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl/_jsii/cdk-lambda-layer-curl@2.0.99.jsii.tgz`

 * *Files 21% similar despite different names*

#### Comparing `cdk-lambda-layer-curl@2.0.98.jsii.tgz-content` & `cdk-lambda-layer-curl@2.0.99.jsii.tgz-content`

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.9444444444444444%*

 * *Differences: {"'fingerprint'": "'caBzftlZgITTzrsU37JSFHDCpRFk/oGY+p3VAq2AM5E='", "'version'": "'2.0.99'"}*

```diff
@@ -2771,15 +2771,15 @@
             }
         }
     },
     "description": "For lambda layer use curl",
     "docs": {
         "stability": "stable"
     },
-    "fingerprint": "R1N+BTMZEA4sOAb4KQVsxA2AcOMeUxpKoT2cJ1NamgI=",
+    "fingerprint": "caBzftlZgITTzrsU37JSFHDCpRFk/oGY+p3VAq2AM5E=",
     "homepage": "https://github.com/clarencetw/cdk-lambda-layer-curl.git",
     "jsiiVersion": "1.59.0 (build eb02c92)",
     "keywords": [
         "aws",
         "cdk",
         "curl"
     ],
@@ -2847,9 +2847,9 @@
                 "filename": "src/index.ts",
                 "line": 10
             },
             "name": "CurlLayer",
             "symbolId": "src/index:CurlLayer"
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
 exports.CurlLayer = CurlLayer;
 _a = JSII_RTTI_SYMBOL_1;
 CurlLayer[_a] = {
     fqn: "cdk-lambda-layer-curl.CurlLayer",
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

 * *Differences: {"'devDependencies'": "{'projen': '^0.56.16'}", "'version'": "'2.0.99'"}*

```diff
@@ -25,15 +25,15 @@
         "jest-junit": "^13",
         "jsii": "^1.59.0",
         "jsii-diff": "^1.59.0",
         "jsii-docgen": "^4.2.44",
         "jsii-pacmak": "^1.59.0",
         "json-schema": "^0.4.0",
         "npm-check-updates": "^12",
-        "projen": "^0.56.15",
+        "projen": "^0.56.16",
         "standard-version": "^9",
         "ts-jest": "^27",
         "typescript": "^4.6.4"
     },
     "jest": {
         "clearMocks": true,
         "collectCoverage": true,
@@ -131,9 +131,9 @@
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
 
-### [2.0.98](https://github.com/clarencetw/cdk-lambda-layer-curl/compare/v2.0.97...v2.0.98) (2022-05-17)
+### [2.0.99](https://github.com/clarencetw/cdk-lambda-layer-curl/compare/v2.0.98...v2.0.99) (2022-05-18)
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

### Comparing `cdk-lambda-layer-curl-2.0.98/src/cdk_lambda_layer_curl.egg-info/PKG-INFO` & `cdk-lambda-layer-curl-2.0.99/src/cdk_lambda_layer_curl.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-lambda-layer-curl
-Version: 2.0.98
+Version: 2.0.99
 Summary: For lambda layer use curl
 Home-page: https://github.com/clarencetw/cdk-lambda-layer-curl.git
 Author: clarencetw<mr.lin.clarence@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/clarencetw/cdk-lambda-layer-curl.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

