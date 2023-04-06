# Comparing `tmp/cdk-eks-karpenter-0.0.7.tar.gz` & `tmp/cdk-eks-karpenter-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cdk-eks-karpenter-0.0.7.tar", last modified: Thu Mar 24 10:56:50 2022, max compression
+gzip compressed data, was "cdk-eks-karpenter-0.0.8.tar", last modified: Tue Mar 29 11:08:54 2022, max compression
```

## Comparing `cdk-eks-karpenter-0.0.7.tar` & `cdk-eks-karpenter-0.0.8.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 10:56:50.587477 cdk-eks-karpenter-0.0.7/
--rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)       66 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/NOTICE
--rw-r--r--   0 runner    (1001) docker     (121)     3913 2022-03-24 10:56:50.587477 cdk-eks-karpenter-0.0.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2925 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-24 10:56:50.587477 cdk-eks-karpenter-0.0.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1777 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 10:56:50.583477 cdk-eks-karpenter-0.0.7/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 10:56:50.587477 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/
--rw-r--r--   0 runner    (1001) docker     (121)     7758 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 10:56:50.587477 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      367 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    24000 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/_jsii/cdk-eks-karpenter@0.0.7.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-24 10:56:38.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-24 10:56:50.587477 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3913 2022-03-24 10:56:50.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      450 2022-03-24 10:56:50.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-24 10:56:50.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-24 10:56:50.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-03-24 10:56:50.000000 cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/
+-rw-r--r--   0 runner    (1001) docker     (121)    11358 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)       66 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (121)     3913 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2925 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1777 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/
+-rw-r--r--   0 runner    (1001) docker     (121)     7758 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      367 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23998 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/_jsii/cdk-eks-karpenter@0.0.8.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-29 11:08:40.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-29 11:08:54.278771 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3913 2022-03-29 11:08:54.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      450 2022-03-29 11:08:54.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-03-29 11:08:54.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       93 2022-03-29 11:08:54.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-03-29 11:08:54.000000 cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/top_level.txt
```

### Comparing `cdk-eks-karpenter-0.0.7/LICENSE` & `cdk-eks-karpenter-0.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `cdk-eks-karpenter-0.0.7/PKG-INFO` & `cdk-eks-karpenter-0.0.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-eks-karpenter
-Version: 0.0.7
+Version: 0.0.8
 Summary: CDK construct library that allows you install Karpenter in an AWS EKS cluster
 Home-page: https://github.com/aws-samples/cdk-eks-karpenter.git
 Author: Andreas Lindh<elindh@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws-samples/cdk-eks-karpenter.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `cdk-eks-karpenter-0.0.7/README.md` & `cdk-eks-karpenter-0.0.8/README.md`

 * *Files identical despite different names*

### Comparing `cdk-eks-karpenter-0.0.7/setup.py` & `cdk-eks-karpenter-0.0.8/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "cdk-eks-karpenter",
-    "version": "0.0.7",
+    "version": "0.0.8",
     "description": "CDK construct library that allows you install Karpenter in an AWS EKS cluster",
     "license": "Apache-2.0",
     "url": "https://github.com/aws-samples/cdk-eks-karpenter.git",
     "long_description_content_type": "text/markdown",
     "author": "Andreas Lindh<elindh@amazon.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "cdk_eks_karpenter",
         "cdk_eks_karpenter._jsii"
     ],
     "package_data": {
         "cdk_eks_karpenter._jsii": [
-            "cdk-eks-karpenter@0.0.7.jsii.tgz"
+            "cdk-eks-karpenter@0.0.8.jsii.tgz"
         ],
         "cdk_eks_karpenter": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter/__init__.py` & `cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter/__init__.py`

 * *Files identical despite different names*

### Comparing `cdk-eks-karpenter-0.0.7/src/cdk_eks_karpenter.egg-info/PKG-INFO` & `cdk-eks-karpenter-0.0.8/src/cdk_eks_karpenter.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cdk-eks-karpenter
-Version: 0.0.7
+Version: 0.0.8
 Summary: CDK construct library that allows you install Karpenter in an AWS EKS cluster
 Home-page: https://github.com/aws-samples/cdk-eks-karpenter.git
 Author: Andreas Lindh<elindh@amazon.com>
 License: Apache-2.0
 Project-URL: Source, https://github.com/aws-samples/cdk-eks-karpenter.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

