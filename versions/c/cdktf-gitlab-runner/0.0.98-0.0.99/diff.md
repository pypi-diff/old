# Comparing `tmp/cdktf-gitlab-runner-0.0.98.tar.gz` & `tmp/cdktf-gitlab-runner-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/__w/cdktf-gitlab-runner/cdktf-gitlab-runner/dist/python/cdktf-gitlab-runner-0.0.98.tar", last modified: Sat Nov 27 00:39:33 2021, max compression
+gzip compressed data, was "/__w/cdktf-gitlab-runner/cdktf-gitlab-runner/dist/python/cdktf-gitlab-runner-0.0.99.tar", last modified: Sun Nov 28 00:41:13 2021, max compression
```

## Comparing `cdktf-gitlab-runner-0.0.98.tar` & `cdktf-gitlab-runner-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/
--rw-r--r--   0 superchain  (1001) superchain  (1001)    11358 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/LICENSE
--rw-r--r--   0 superchain  (1001) superchain  (1001)       23 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/MANIFEST.in
--rw-r--r--   0 superchain  (1001) superchain  (1001)     3187 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/PKG-INFO
--rw-r--r--   0 superchain  (1001) superchain  (1001)     2241 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/README.md
--rw-r--r--   0 superchain  (1001) superchain  (1001)      106 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/pyproject.toml
--rw-r--r--   0 superchain  (1001) superchain  (1001)       38 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/setup.cfg
--rw-r--r--   0 superchain  (1001) superchain  (1001)     1816 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/setup.py
-drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/src/
-drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/
--rw-r--r--   0 superchain  (1001) superchain  (1001)    25397 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/__init__.py
-drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/_jsii/
--rw-r--r--   0 superchain  (1001) superchain  (1001)      425 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/_jsii/__init__.py
--rw-r--r--   0 superchain  (1001) superchain  (1001)    22402 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/_jsii/cdktf-gitlab-runner@0.0.98.jsii.tgz
--rw-r--r--   0 superchain  (1001) superchain  (1001)        1 2021-11-27 00:39:28.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/py.typed
-drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-27 00:39:33.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/
--rw-r--r--   0 superchain  (1001) superchain  (1001)     3187 2021-11-27 00:39:32.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/PKG-INFO
--rw-r--r--   0 superchain  (1001) superchain  (1001)      464 2021-11-27 00:39:32.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/SOURCES.txt
--rw-r--r--   0 superchain  (1001) superchain  (1001)        1 2021-11-27 00:39:32.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/dependency_links.txt
--rw-r--r--   0 superchain  (1001) superchain  (1001)      130 2021-11-27 00:39:32.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/requires.txt
--rw-r--r--   0 superchain  (1001) superchain  (1001)       20 2021-11-27 00:39:32.000000 cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/top_level.txt
+drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/
+-rw-r--r--   0 superchain  (1001) superchain  (1001)    11358 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/LICENSE
+-rw-r--r--   0 superchain  (1001) superchain  (1001)       23 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/MANIFEST.in
+-rw-r--r--   0 superchain  (1001) superchain  (1001)     3187 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/PKG-INFO
+-rw-r--r--   0 superchain  (1001) superchain  (1001)     2241 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/README.md
+-rw-r--r--   0 superchain  (1001) superchain  (1001)      106 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/pyproject.toml
+-rw-r--r--   0 superchain  (1001) superchain  (1001)       38 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/setup.cfg
+-rw-r--r--   0 superchain  (1001) superchain  (1001)     1816 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/setup.py
+drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/
+drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/
+-rw-r--r--   0 superchain  (1001) superchain  (1001)    25397 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/__init__.py
+drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/_jsii/
+-rw-r--r--   0 superchain  (1001) superchain  (1001)      425 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/_jsii/__init__.py
+-rw-r--r--   0 superchain  (1001) superchain  (1001)    22400 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/_jsii/cdktf-gitlab-runner@0.0.99.jsii.tgz
+-rw-r--r--   0 superchain  (1001) superchain  (1001)        1 2021-11-28 00:41:09.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/py.typed
+drwxr-xr-x   0 superchain  (1001) superchain  (1001)        0 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/
+-rw-r--r--   0 superchain  (1001) superchain  (1001)     3187 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/PKG-INFO
+-rw-r--r--   0 superchain  (1001) superchain  (1001)      464 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/SOURCES.txt
+-rw-r--r--   0 superchain  (1001) superchain  (1001)        1 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/dependency_links.txt
+-rw-r--r--   0 superchain  (1001) superchain  (1001)      130 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/requires.txt
+-rw-r--r--   0 superchain  (1001) superchain  (1001)       20 2021-11-28 00:41:13.000000 cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/top_level.txt
```

### Comparing `cdktf-gitlab-runner-0.0.98/LICENSE` & `cdktf-gitlab-runner-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `cdktf-gitlab-runner-0.0.98/PKG-INFO` & `cdktf-gitlab-runner-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdktf-gitlab-runner
-Version: 0.0.98
+Version: 0.0.99
 Summary: The CDK for Terraform Construct for Gitlab Runner on GCP
 Home-page: https://github.com/neilkuan/cdktf-gitlab-runner.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdktf-gitlab-runner.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdktf-gitlab-runner-0.0.98/README.md` & `cdktf-gitlab-runner-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `cdktf-gitlab-runner-0.0.98/setup.py` & `cdktf-gitlab-runner-0.0.99/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdktf-gitlab-runner",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "The CDK for Terraform Construct for Gitlab Runner on GCP",
     "license": "Apache-2.0",
     "url": "https://github.com/neilkuan/cdktf-gitlab-runner.git",
     "long_description_content_type": "text/markdown",
     "author": "Neil Kuan<guan840912@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,23 +22,23 @@
     },
     "packages": [
         "cdktf_gitlab_runner",
         "cdktf_gitlab_runner._jsii"
     ],
     "package_data": {
         "cdktf_gitlab_runner._jsii": [
-            "cdktf-gitlab-runner@0.0.98.jsii.tgz"
+            "cdktf-gitlab-runner@0.0.99.jsii.tgz"
         ],
         "cdktf_gitlab_runner": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
-        "cdktf-cdktf-provider-google>=0.3.207, <0.4.0",
+        "cdktf-cdktf-provider-google>=0.3.213, <0.4.0",
         "cdktf>=0.7.0, <0.8.0",
         "constructs>=10.0.0, <11.0.0",
         "jsii>=1.46.0, <2.0.0",
         "publication>=0.0.3"
     ],
     "classifiers": [
         "Intended Audience :: Developers",
```

### Comparing `cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner/__init__.py` & `cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner/__init__.py`

 * *Files identical despite different names*

### Comparing `cdktf-gitlab-runner-0.0.98/src/cdktf_gitlab_runner.egg-info/PKG-INFO` & `cdktf-gitlab-runner-0.0.99/src/cdktf_gitlab_runner.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdktf-gitlab-runner
-Version: 0.0.98
+Version: 0.0.99
 Summary: The CDK for Terraform Construct for Gitlab Runner on GCP
 Home-page: https://github.com/neilkuan/cdktf-gitlab-runner.git
 Author: Neil Kuan<guan840912@gmail.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/neilkuan/cdktf-gitlab-runner.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

