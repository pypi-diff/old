# Comparing `tmp/cdklabs.cdk-validator-cfnguard-0.0.8.tar.gz` & `tmp/cdklabs.cdk-validator-cfnguard-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdklabs.cdk-validator-cfnguard-0.0.8.tar", last modified: Sat Apr  1 00:20:50 2023, max compression
+gzip compressed data, was "cdklabs.cdk-validator-cfnguard-0.0.9.tar", last modified: Sun Apr  2 00:22:10 2023, max compression
```

## Comparing `cdklabs.cdk-validator-cfnguard-0.0.8.tar` & `cdklabs.cdk-validator-cfnguard-0.0.9.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:20:50.329487 cdklabs.cdk-validator-cfnguard-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     8270 2023-04-01 00:20:50.329487 cdklabs.cdk-validator-cfnguard-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7291 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-01 00:20:50.329487 cdklabs.cdk-validator-cfnguard-0.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1855 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:20:50.321487 cdklabs.cdk-validator-cfnguard-0.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:20:50.321487 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:20:50.321487 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/
--rw-r--r--   0 runner    (1001) docker     (123)    14137 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:20:50.325487 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      409 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)  4394378 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/_jsii/cdk-validator-cfnguard@0.0.8.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-01 00:20:38.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-01 00:20:50.321487 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8270 2023-04-01 00:20:50.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      565 2023-04-01 00:20:50.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-01 00:20:50.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-01 00:20:50.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-01 00:20:50.000000 cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 00:22:10.627936 cdklabs.cdk-validator-cfnguard-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     8270 2023-04-02 00:22:10.627936 cdklabs.cdk-validator-cfnguard-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7291 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-02 00:22:10.627936 cdklabs.cdk-validator-cfnguard-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1855 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 00:22:10.619936 cdklabs.cdk-validator-cfnguard-0.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 00:22:10.619936 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 00:22:10.623936 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/
+-rw-r--r--   0 runner    (1001) docker     (123)    14137 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 00:22:10.623936 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      409 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)  4394375 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/_jsii/cdk-validator-cfnguard@0.0.9.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-02 00:21:57.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-02 00:22:10.623936 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8270 2023-04-02 00:22:10.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      565 2023-04-02 00:22:10.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-02 00:22:10.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-02 00:22:10.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-02 00:22:10.000000 cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/top_level.txt
```

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/LICENSE` & `cdklabs.cdk-validator-cfnguard-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/PKG-INFO` & `cdklabs.cdk-validator-cfnguard-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-validator-cfnguard
-Version: 0.0.8
+Version: 0.0.9
 Summary: @cdklabs/cdk-validator-cfnguard
 Home-page: https://github.com/cdklabs/cdk-validator-cfnguard.git
 Author: Amazon Web Services<aws-cdk-dev@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-validator-cfnguard.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/README.md` & `cdklabs.cdk-validator-cfnguard-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/setup.py` & `cdklabs.cdk-validator-cfnguard-0.0.9/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdklabs.cdk-validator-cfnguard",
-    "version": "0.0.8",
+    "version": "0.0.9",
     "description": "@cdklabs/cdk-validator-cfnguard",
     "license": "Apache-2.0",
     "url": "https://github.com/cdklabs/cdk-validator-cfnguard.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services<aws-cdk-dev@amazon.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdklabs.cdk_validator_cfnguard",
         "cdklabs.cdk_validator_cfnguard._jsii"
     ],
     "package_data": {
         "cdklabs.cdk_validator_cfnguard._jsii": [
-            "cdk-validator-cfnguard@0.0.8.jsii.tgz"
+            "cdk-validator-cfnguard@0.0.9.jsii.tgz"
         ],
         "cdklabs.cdk_validator_cfnguard": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/__init__.py` & `cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/__init__.py`

 * *Files identical despite different names*

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs/cdk_validator_cfnguard/_jsii/cdk-validator-cfnguard@0.0.8.jsii.tgz` & `cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs/cdk_validator_cfnguard/_jsii/cdk-validator-cfnguard@0.0.9.jsii.tgz`

 * *Files 3% similar despite different names*

#### Comparing `cdk-validator-cfnguard@0.0.8.jsii.tgz-content` & `cdk-validator-cfnguard@0.0.9.jsii.tgz-content`

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.9444444444444444%*

 * *Differences: {"'fingerprint'": "'1n9g78QJfyxUcaeivpVx+vsIlcbV8sh6PvMKXWVoKPM='", "'version'": "'0.0.9'"}*

```diff
@@ -3408,15 +3408,15 @@
             }
         }
     },
     "description": "@cdklabs/cdk-validator-cfnguard",
     "docs": {
         "stability": "stable"
     },
-    "fingerprint": "nNOTZEGJLN9k6w8hxgfZJzK0n5qGkafouC4P5N03Usg=",
+    "fingerprint": "1n9g78QJfyxUcaeivpVx+vsIlcbV8sh6PvMKXWVoKPM=",
     "homepage": "https://github.com/cdklabs/cdk-validator-cfnguard.git",
     "jsiiVersion": "5.0.2 (build fc559a8)",
     "keywords": [
         "cdk",
         "policy as code",
         "validator"
     ],
@@ -3620,9 +3620,9 @@
                         }
                     }
                 }
             ],
             "symbolId": "src/plugin:CfnGuardValidatorProps"
         }
     },
-    "version": "0.0.8"
+    "version": "0.0.9"
 }
```

##### package/lib/plugin.js

###### js-beautify {}

```diff
@@ -116,15 +116,15 @@
             violations: violations,
         };
     }
 }
 _a = JSII_RTTI_SYMBOL_1;
 CfnGuardValidator[_a] = {
     fqn: "@cdklabs/cdk-validator-cfnguard.CfnGuardValidator",
-    version: "0.0.8"
+    version: "0.0.9"
 };
 exports.CfnGuardValidator = CfnGuardValidator;
 /**
  * Guard does not have a standard JSON schema and the schema
  * that is returned can be dependent on the type of rule or type
  * of check that was executed. The results are very much an attempt to
  * display the internals of guard to the user. Trying to make sense of that
```

##### package/package.json

###### Pretty-printed

 * *Similarity: 0.9689542483660131%*

 * *Differences: {"'devDependencies'": "{'cdklabs-projen-project-types': '^0.1.63', 'jsii-docgen': '^7.1.43', "*

 * *                      "'projen': '^0.70.5'}",*

 * * "'version'": "'0.0.9'"}*

```diff
@@ -10,29 +10,29 @@
         "@octokit/types": "^9.0.0",
         "@types/jest": "^27",
         "@types/mock-fs": "^4.13.1",
         "@types/node": "^14",
         "@typescript-eslint/eslint-plugin": "^5",
         "@typescript-eslint/parser": "^5",
         "aws-cdk-lib": "2.71.0",
-        "cdklabs-projen-project-types": "^0.1.62",
+        "cdklabs-projen-project-types": "^0.1.63",
         "constructs": "^10.1.298",
         "eslint": "^8",
         "eslint-import-resolver-node": "^0.3.7",
         "eslint-import-resolver-typescript": "^3.5.4",
         "eslint-plugin-import": "^2.27.5",
         "jest": "^27",
         "jest-junit": "^15",
         "jsii": "~5.0.0",
         "jsii-diff": "^1.79.0",
-        "jsii-docgen": "^7.1.42",
+        "jsii-docgen": "^7.1.43",
         "jsii-pacmak": "^1.79.0",
         "mock-fs": "^5.2.0",
         "npm-check-updates": "^16",
-        "projen": "^0.70.4",
+        "projen": "^0.70.5",
         "standard-version": "^9",
         "ts-jest": "^27",
         "ts-node": "^10.9.1",
         "typescript": "^4.9.5"
     },
     "engines": {
         "node": ">= 14.18.0"
@@ -149,9 +149,9 @@
         "unbump": "npx projen unbump",
         "update-guard": "npx projen update-guard",
         "upgrade": "npx projen upgrade",
         "watch": "npx projen watch"
     },
     "stability": "stable",
     "types": "lib/index.d.ts",
-    "version": "0.0.8"
+    "version": "0.0.9"
 }
```

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/PKG-INFO` & `cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdklabs.cdk-validator-cfnguard
-Version: 0.0.8
+Version: 0.0.9
 Summary: @cdklabs/cdk-validator-cfnguard
 Home-page: https://github.com/cdklabs/cdk-validator-cfnguard.git
 Author: Amazon Web Services<aws-cdk-dev@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/cdklabs/cdk-validator-cfnguard.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `cdklabs.cdk-validator-cfnguard-0.0.8/src/cdklabs.cdk_validator_cfnguard.egg-info/SOURCES.txt` & `cdklabs.cdk-validator-cfnguard-0.0.9/src/cdklabs.cdk_validator_cfnguard.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/cdklabs.cdk_validator_cfnguard.egg-info/SOURCES.txt
 src/cdklabs.cdk_validator_cfnguard.egg-info/dependency_links.txt
 src/cdklabs.cdk_validator_cfnguard.egg-info/requires.txt
 src/cdklabs.cdk_validator_cfnguard.egg-info/top_level.txt
 src/cdklabs/cdk_validator_cfnguard/__init__.py
 src/cdklabs/cdk_validator_cfnguard/py.typed
 src/cdklabs/cdk_validator_cfnguard/_jsii/__init__.py
-src/cdklabs/cdk_validator_cfnguard/_jsii/cdk-validator-cfnguard@0.0.8.jsii.tgz
+src/cdklabs/cdk_validator_cfnguard/_jsii/cdk-validator-cfnguard@0.0.9.jsii.tgz
```

