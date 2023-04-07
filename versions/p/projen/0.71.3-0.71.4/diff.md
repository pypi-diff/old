# Comparing `tmp/projen-0.71.3.tar.gz` & `tmp/projen-0.71.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "projen-0.71.3.tar", last modified: Fri Apr  7 11:40:15 2023, max compression
+gzip compressed data, was "projen-0.71.4.tar", last modified: Fri Apr  7 13:13:48 2023, max compression
```

## Comparing `projen-0.71.3.tar` & `projen-0.71.4.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.474150 projen-0.71.3/
--rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-07 11:39:59.000000 projen-0.71.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 11:39:59.000000 projen-0.71.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-07 11:40:15.474150 projen-0.71.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    54524 2023-04-07 11:39:59.000000 projen-0.71.3/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-07 11:39:59.000000 projen-0.71.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 11:40:15.474150 projen-0.71.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-07 11:39:59.000000 projen-0.71.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.454150 projen-0.71.3/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.458150 projen-0.71.3/src/projen/
--rw-r--r--   0 runner    (1001) docker     (123)   579961 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.462150 projen-0.71.3/src/projen/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/_jsii/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.462150 projen-0.71.3/src/projen/_jsii/bin/
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/_jsii/bin/projen
--rw-r--r--   0 runner    (1001) docker     (123)  3351094 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/_jsii/projen@0.71.3.jsii.tgz
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.466150 projen-0.71.3/src/projen/awscdk/
--rw-r--r--   0 runner    (1001) docker     (123)  1031755 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/awscdk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.466150 projen-0.71.3/src/projen/build/
--rw-r--r--   0 runner    (1001) docker     (123)    39873 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/build/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.466150 projen-0.71.3/src/projen/cdk/
--rw-r--r--   0 runner    (1001) docker     (123)   475242 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/cdk/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.466150 projen-0.71.3/src/projen/cdk8s/
--rw-r--r--   0 runner    (1001) docker     (123)   568788 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/cdk8s/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.466150 projen-0.71.3/src/projen/cdktf/
--rw-r--r--   0 runner    (1001) docker     (123)   210451 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/cdktf/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.466150 projen-0.71.3/src/projen/circleci/
--rw-r--r--   0 runner    (1001) docker     (123)    75837 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/circleci/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/github/
--rw-r--r--   0 runner    (1001) docker     (123)   275214 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/github/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)   235582 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/github/workflows/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/gitlab/
--rw-r--r--   0 runner    (1001) docker     (123)   192753 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/gitlab/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/java/
--rw-r--r--   0 runner    (1001) docker     (123)   174928 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/java/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/javascript/
--rw-r--r--   0 runner    (1001) docker     (123)   585936 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/javascript/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/python/
--rw-r--r--   0 runner    (1001) docker     (123)   187110 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/python/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/release/
--rw-r--r--   0 runner    (1001) docker     (123)   246151 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/release/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.470150 projen-0.71.3/src/projen/typescript/
--rw-r--r--   0 runner    (1001) docker     (123)   423064 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/typescript/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.474150 projen-0.71.3/src/projen/vscode/
--rw-r--r--   0 runner    (1001) docker     (123)    54316 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/vscode/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.474150 projen-0.71.3/src/projen/web/
--rw-r--r--   0 runner    (1001) docker     (123)   745214 2023-04-07 11:39:59.000000 projen-0.71.3/src/projen/web/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:40:15.458150 projen-0.71.3/src/projen.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-07 11:40:15.000000 projen-0.71.3/src/projen.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-07 11:40:15.000000 projen-0.71.3/src/projen.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:40:15.000000 projen-0.71.3/src/projen.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-07 11:40:15.000000 projen-0.71.3/src/projen.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 11:40:15.000000 projen-0.71.3/src/projen.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.410616 projen-0.71.4/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-07 13:13:35.000000 projen-0.71.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 13:13:35.000000 projen-0.71.4/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-07 13:13:48.410616 projen-0.71.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    54524 2023-04-07 13:13:35.000000 projen-0.71.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-07 13:13:35.000000 projen-0.71.4/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 13:13:48.410616 projen-0.71.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-07 13:13:35.000000 projen-0.71.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.394615 projen-0.71.4/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.398615 projen-0.71.4/src/projen/
+-rw-r--r--   0 runner    (1001) docker     (123)   579961 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.398615 projen-0.71.4/src/projen/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/_jsii/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.402616 projen-0.71.4/src/projen/_jsii/bin/
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/_jsii/bin/projen
+-rw-r--r--   0 runner    (1001) docker     (123)  3351176 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/_jsii/projen@0.71.4.jsii.tgz
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.402616 projen-0.71.4/src/projen/awscdk/
+-rw-r--r--   0 runner    (1001) docker     (123)  1031818 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/awscdk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/build/
+-rw-r--r--   0 runner    (1001) docker     (123)    39873 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/build/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/cdk/
+-rw-r--r--   0 runner    (1001) docker     (123)   475284 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/cdk/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/cdk8s/
+-rw-r--r--   0 runner    (1001) docker     (123)   568830 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/cdk8s/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/cdktf/
+-rw-r--r--   0 runner    (1001) docker     (123)   210472 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/cdktf/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/circleci/
+-rw-r--r--   0 runner    (1001) docker     (123)    75837 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/circleci/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/github/
+-rw-r--r--   0 runner    (1001) docker     (123)   275214 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/github/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)   235582 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/github/workflows/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/gitlab/
+-rw-r--r--   0 runner    (1001) docker     (123)   192753 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/gitlab/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/java/
+-rw-r--r--   0 runner    (1001) docker     (123)   174928 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/java/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.406616 projen-0.71.4/src/projen/javascript/
+-rw-r--r--   0 runner    (1001) docker     (123)   585936 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/javascript/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.410616 projen-0.71.4/src/projen/python/
+-rw-r--r--   0 runner    (1001) docker     (123)   187110 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/python/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.410616 projen-0.71.4/src/projen/release/
+-rw-r--r--   0 runner    (1001) docker     (123)   246151 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/release/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.410616 projen-0.71.4/src/projen/typescript/
+-rw-r--r--   0 runner    (1001) docker     (123)   423106 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/typescript/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.410616 projen-0.71.4/src/projen/vscode/
+-rw-r--r--   0 runner    (1001) docker     (123)    54316 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/vscode/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.410616 projen-0.71.4/src/projen/web/
+-rw-r--r--   0 runner    (1001) docker     (123)   745256 2023-04-07 13:13:35.000000 projen-0.71.4/src/projen/web/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:13:48.398615 projen-0.71.4/src/projen.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    55403 2023-04-07 13:13:48.000000 projen-0.71.4/src/projen.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-07 13:13:48.000000 projen-0.71.4/src/projen.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:13:48.000000 projen-0.71.4/src/projen.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-04-07 13:13:48.000000 projen-0.71.4/src/projen.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 13:13:48.000000 projen-0.71.4/src/projen.egg-info/top_level.txt
```

### Comparing `projen-0.71.3/LICENSE` & `projen-0.71.4/LICENSE`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/PKG-INFO` & `projen-0.71.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: projen
-Version: 0.71.3
+Version: 0.71.4
 Summary: CDK for software projects
 Home-page: https://github.com/projen/projen.git
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/projen/projen.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `projen-0.71.3/README.md` & `projen-0.71.4/README.md`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/setup.py` & `projen-0.71.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "projen",
-    "version": "0.71.3",
+    "version": "0.71.4",
     "description": "CDK for software projects",
     "license": "Apache-2.0",
     "url": "https://github.com/projen/projen.git",
     "long_description_content_type": "text/markdown",
     "author": "Amazon Web Services",
     "bdist_wheel": {
         "universal": true
@@ -38,15 +38,15 @@
         "projen.release",
         "projen.typescript",
         "projen.vscode",
         "projen.web"
     ],
     "package_data": {
         "projen._jsii": [
-            "projen@0.71.3.jsii.tgz"
+            "projen@0.71.4.jsii.tgz"
         ],
         "projen": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `projen-0.71.3/src/projen/__init__.py` & `projen-0.71.4/src/projen/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/awscdk/__init__.py` & `projen-0.71.4/src/projen/awscdk/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -8398,14 +8398,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
@@ -14104,14 +14105,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
@@ -17120,14 +17122,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
```

### Comparing `projen-0.71.3/src/projen/build/__init__.py` & `projen-0.71.4/src/projen/build/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/cdk/__init__.py` & `projen-0.71.4/src/projen/cdk/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -4265,14 +4265,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
@@ -7797,14 +7798,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
```

### Comparing `projen-0.71.3/src/projen/cdk8s/__init__.py` & `projen-0.71.4/src/projen/cdk8s/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -5450,14 +5450,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
@@ -8857,14 +8858,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
```

### Comparing `projen-0.71.3/src/projen/cdktf/__init__.py` & `projen-0.71.4/src/projen/cdktf/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -3137,14 +3137,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
```

### Comparing `projen-0.71.3/src/projen/circleci/__init__.py` & `projen-0.71.4/src/projen/circleci/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/github/__init__.py` & `projen-0.71.4/src/projen/github/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/github/workflows/__init__.py` & `projen-0.71.4/src/projen/github/workflows/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/gitlab/__init__.py` & `projen-0.71.4/src/projen/gitlab/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/java/__init__.py` & `projen-0.71.4/src/projen/java/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/javascript/__init__.py` & `projen-0.71.4/src/projen/javascript/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/python/__init__.py` & `projen-0.71.4/src/projen/python/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/release/__init__.py` & `projen-0.71.4/src/projen/release/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/typescript/__init__.py` & `projen-0.71.4/src/projen/typescript/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -3295,14 +3295,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[ProjenrcOptions]:
         '''(experimental) Options for .projenrc.ts.
@@ -6755,14 +6756,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[ProjenrcOptions]:
         '''(experimental) Options for .projenrc.ts.
```

### Comparing `projen-0.71.3/src/projen/vscode/__init__.py` & `projen-0.71.4/src/projen/vscode/__init__.py`

 * *Files identical despite different names*

### Comparing `projen-0.71.3/src/projen/web/__init__.py` & `projen-0.71.4/src/projen/web/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -5942,14 +5942,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
@@ -9790,14 +9791,15 @@
     @builtins.property
     def projenrc_ts(self) -> typing.Optional[builtins.bool]:
         '''(experimental) Use TypeScript for your projenrc file (``.projenrc.ts``).
 
         :default: false
 
         :stability: experimental
+        :pjnew: true
         '''
         result = self._values.get("projenrc_ts")
         return typing.cast(typing.Optional[builtins.bool], result)
 
     @builtins.property
     def projenrc_ts_options(self) -> typing.Optional[_ProjenrcOptions_514ec2ee]:
         '''(experimental) Options for .projenrc.ts.
```

### Comparing `projen-0.71.3/src/projen.egg-info/PKG-INFO` & `projen-0.71.4/src/projen.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: projen
-Version: 0.71.3
+Version: 0.71.4
 Summary: CDK for software projects
 Home-page: https://github.com/projen/projen.git
 Author: Amazon Web Services
 License: Apache-2.0
 Project-URL: Source, https://github.com/projen/projen.git
 Classifier: Intended Audience :: Developers
 Classifier: Operating System :: OS Independent
```

### Comparing `projen-0.71.3/src/projen.egg-info/SOURCES.txt` & `projen-0.71.4/src/projen.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 src/projen/py.typed
 src/projen.egg-info/PKG-INFO
 src/projen.egg-info/SOURCES.txt
 src/projen.egg-info/dependency_links.txt
 src/projen.egg-info/requires.txt
 src/projen.egg-info/top_level.txt
 src/projen/_jsii/__init__.py
-src/projen/_jsii/projen@0.71.3.jsii.tgz
+src/projen/_jsii/projen@0.71.4.jsii.tgz
 src/projen/_jsii/bin/projen
 src/projen/awscdk/__init__.py
 src/projen/build/__init__.py
 src/projen/cdk/__init__.py
 src/projen/cdk8s/__init__.py
 src/projen/cdktf/__init__.py
 src/projen/circleci/__init__.py
```

