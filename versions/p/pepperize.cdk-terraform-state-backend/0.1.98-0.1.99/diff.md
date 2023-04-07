# Comparing `tmp/pepperize.cdk-terraform-state-backend-0.1.98.tar.gz` & `tmp/pepperize.cdk-terraform-state-backend-0.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-terraform-state-backend-0.1.98.tar", last modified: Wed Jun 22 06:47:20 2022, max compression
+gzip compressed data, was "pepperize.cdk-terraform-state-backend-0.1.99.tar", last modified: Wed Jun 22 06:53:33 2022, max compression
```

## Comparing `pepperize.cdk-terraform-state-backend-0.1.98.tar` & `pepperize.cdk-terraform-state-backend-0.1.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     4760 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3699 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2020 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4760 2022-06-22 06:47:20.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      634 2022-06-22 06:47:20.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-22 06:47:20.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      139 2022-06-22 06:47:20.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-22 06:47:20.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/
--rw-r--r--   0 runner    (1001) docker     (121)     7452 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:47:20.627299 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      455 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15294 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/_jsii/cdk-terraform-state-backend@0.1.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-22 06:47:08.000000 pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     4760 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3699 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2020 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4760 2022-06-22 06:53:32.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      634 2022-06-22 06:53:33.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-22 06:53:32.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      139 2022-06-22 06:53:33.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-06-22 06:53:33.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/
+-rw-r--r--   0 runner    (1001) docker     (121)     7452 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-22 06:53:33.472552 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      455 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15294 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/_jsii/cdk-terraform-state-backend@0.1.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-22 06:53:18.000000 pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/py.typed
```

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/LICENSE` & `pepperize.cdk-terraform-state-backend-0.1.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/PKG-INFO` & `pepperize.cdk-terraform-state-backend-0.1.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-terraform-state-backend
-Version: 0.1.98
+Version: 0.1.99
 Summary: This project provides a CDK construct bootstrapping an AWS account with a S3 Bucket and a DynamoDB table as terraform state backend.
 Home-page: https://github.com/pepperize/cdk-terraform-state-backend.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-terraform-state-backend.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/README.md` & `pepperize.cdk-terraform-state-backend-0.1.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/setup.py` & `pepperize.cdk-terraform-state-backend-0.1.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-terraform-state-backend",
-    "version": "0.1.98",
+    "version": "0.1.99",
     "description": "This project provides a CDK construct bootstrapping an AWS account with a S3 Bucket and a DynamoDB table as terraform state backend.",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-terraform-state-backend.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_terraform_state_backend",
         "pepperize_cdk_terraform_state_backend._jsii"
     ],
     "package_data": {
         "pepperize_cdk_terraform_state_backend._jsii": [
-            "cdk-terraform-state-backend@0.1.98.jsii.tgz"
+            "cdk-terraform-state-backend@0.1.99.jsii.tgz"
         ],
         "pepperize_cdk_terraform_state_backend": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/PKG-INFO` & `pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-terraform-state-backend
-Version: 0.1.98
+Version: 0.1.99
 Summary: This project provides a CDK construct bootstrapping an AWS account with a S3 Bucket and a DynamoDB table as terraform state backend.
 Home-page: https://github.com/pepperize/cdk-terraform-state-backend.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-terraform-state-backend.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize.cdk_terraform_state_backend.egg-info/SOURCES.txt` & `pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize.cdk_terraform_state_backend.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_terraform_state_backend.egg-info/SOURCES.txt
 src/pepperize.cdk_terraform_state_backend.egg-info/dependency_links.txt
 src/pepperize.cdk_terraform_state_backend.egg-info/requires.txt
 src/pepperize.cdk_terraform_state_backend.egg-info/top_level.txt
 src/pepperize_cdk_terraform_state_backend/__init__.py
 src/pepperize_cdk_terraform_state_backend/py.typed
 src/pepperize_cdk_terraform_state_backend/_jsii/__init__.py
-src/pepperize_cdk_terraform_state_backend/_jsii/cdk-terraform-state-backend@0.1.98.jsii.tgz
+src/pepperize_cdk_terraform_state_backend/_jsii/cdk-terraform-state-backend@0.1.99.jsii.tgz
```

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/__init__.py` & `pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/__init__.py`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-terraform-state-backend-0.1.98/src/pepperize_cdk_terraform_state_backend/_jsii/cdk-terraform-state-backend@0.1.98.jsii.tgz` & `pepperize.cdk-terraform-state-backend-0.1.99/src/pepperize_cdk_terraform_state_backend/_jsii/cdk-terraform-state-backend@0.1.99.jsii.tgz`

 * *Files 27% similar despite different names*

#### Comparing `cdk-terraform-state-backend@0.1.98.jsii.tgz-content` & `cdk-terraform-state-backend@0.1.99.jsii.tgz-content`

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.9444444444444444%*

 * *Differences: {"'fingerprint'": "'DvhfuxjM88rHmKh3ylTMv9u25VW0oplPtJZxlUKQE1o='", "'version'": "'0.1.99'"}*

```diff
@@ -2873,15 +2873,15 @@
             }
         }
     },
     "description": "This project provides a CDK construct bootstrapping an AWS account with a S3 Bucket and a DynamoDB table as terraform state backend.",
     "docs": {
         "stability": "stable"
     },
-    "fingerprint": "b1+gHiLdfzqVXnnBSazXBCAeg1pcCaB0IC0YjL8IxGY=",
+    "fingerprint": "DvhfuxjM88rHmKh3ylTMv9u25VW0oplPtJZxlUKQE1o=",
     "homepage": "https://github.com/pepperize/cdk-terraform-state-backend.git",
     "jsiiVersion": "1.61.0 (build abf4039)",
     "keywords": [
         "aws",
         "backend",
         "cdk",
         "dynamodb",
@@ -3078,9 +3078,9 @@
                         "primitive": "string"
                     }
                 }
             ],
             "symbolId": "src/terraform-state-backend:TerraformStateBackendProps"
         }
     },
-    "version": "0.1.98"
+    "version": "0.1.99"
 }
```

##### package/lib/terraform-state-backend.js

###### js-beautify {}

```diff
@@ -47,10 +47,10 @@
         });
     }
 }
 exports.TerraformStateBackend = TerraformStateBackend;
 _a = JSII_RTTI_SYMBOL_1;
 TerraformStateBackend[_a] = {
     fqn: "@pepperize/cdk-terraform-state-backend.TerraformStateBackend",
-    version: "0.1.98"
+    version: "0.1.99"
 };
 //# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoidGVycmFmb3JtLXN0YXRlLWJhY2tlbmQuanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyIuLi9zcmMvdGVycmFmb3JtLXN0YXRlLWJhY2tlbmQudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7QUFBQSxzRUFBOEQ7QUFDOUQsNkNBQW1FO0FBQ25FLDJDQUF1QztBQVF2QyxNQUFhLHFCQUFzQixTQUFRLHNCQUFTO0lBS2xELFlBQW1CLEtBQWdCLEVBQUUsRUFBVSxFQUFFLEtBQWlDO1FBQ2hGLEtBQUssQ0FBQyxLQUFLLEVBQUUsRUFBRSxDQUFDLENBQUM7UUFFakIsTUFBTSxFQUFFLFVBQVUsRUFBRSxVQUFVLEVBQUUsU0FBUyxFQUFFLEdBQUcsS0FBSyxDQUFDO1FBRXBELElBQUksQ0FBQyxNQUFNLEdBQUcsSUFBSSxrQ0FBYSxDQUFDLElBQUksRUFBRSxRQUFRLEVBQUU7WUFDOUMsVUFBVSxFQUFFLFVBQVUsSUFBSSwyQkFBMkIsbUJBQUssQ0FBQyxFQUFFLENBQUMsSUFBSSxDQUFDLENBQUMsT0FBTyxJQUFJLG1CQUFLLENBQUMsRUFBRSxDQUFDLElBQUksQ0FBQyxDQUFDLE1BQU0sRUFBRTtZQUN0RyxTQUFTLEVBQUUsSUFBSTtTQUNoQixDQUFDLENBQUM7UUFFSCxJQUFJLENBQUMsS0FBSyxHQUFHLElBQUksMEJBQVksQ0FBQyxLQUFLLENBQUMsSUFBSSxFQUFFLE9BQU8sRUFBRTtZQUNqRCxTQUFTLEVBQUUsU0FBUyxJQUFJLHlCQUF5QjtZQUNqRCxXQUFXLEVBQUUsMEJBQVksQ0FBQyxXQUFXLENBQUMsZUFBZTtZQUNyRCxZQUFZLEVBQUU7Z0JBQ1osSUFBSSxFQUFFLFFBQVE7Z0JBQ2QsSUFBSSxFQUFFLDBCQUFZLENBQUMsYUFBYSxDQUFDLE1BQU07YUFDeEM7WUFDRCxVQUFVLEVBQUUsMEJBQVksQ0FBQyxlQUFlLENBQUMsT0FBTztZQUNoRCxtQkFBbUIsRUFBRSxJQUFJO1NBQzFCLENBQUMsQ0FBQztRQUVILElBQUksQ0FBQyxNQUFNLEdBQUcsSUFBSSxxQkFBTyxDQUFDLE1BQU0sQ0FBQyxJQUFJLEVBQUUsUUFBUSxFQUFFO1lBQy9DLFVBQVUsRUFBRSxVQUFVLElBQUkseUJBQXlCO1lBQ25ELFVBQVUsRUFBRTtnQkFDVixJQUFJLHFCQUFPLENBQUMsZUFBZSxDQUFDO29CQUMxQixNQUFNLEVBQUUscUJBQU8sQ0FBQyxNQUFNLENBQUMsS0FBSztvQkFDNUIsT0FBTyxFQUFFLENBQUMsZUFBZSxFQUFFLGNBQWMsRUFBRSxjQUFjLEVBQUUsaUJBQWlCLENBQUM7b0JBQzdFLFNBQVMsRUFBRSxDQUFDLEdBQUcsSUFBSSxDQUFDLE1BQU0sQ0FBQyxTQUFTLEVBQUUsRUFBRSxHQUFHLElBQUksQ0FBQyxNQUFNLENBQUMsU0FBUyxJQUFJLENBQUM7aUJBQ3RFLENBQUM7Z0JBQ0YsSUFBSSxxQkFBTyxDQUFDLGVBQWUsQ0FBQztvQkFDMUIsTUFBTSxFQUFFLHFCQUFPLENBQUMsTUFBTSxDQUFDLEtBQUs7b0JBQzVCLE9BQU8sRUFBRSxDQUFDLGtCQUFrQixFQUFFLGtCQUFrQixFQUFFLHFCQUFxQixDQUFDO29CQUN4RSxTQUFTLEVBQUUsQ0FBQyxHQUFHLElBQUksQ0FBQyxLQUFLLENBQUMsUUFBUSxFQUFFLENBQUM7aUJBQ3RDLENBQUM7YUFDSDtTQUNGLENBQUMsQ0FBQztJQUNMLENBQUM7O0FBekNILHNEQTBDQyIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IFByaXZhdGVCdWNrZXQgfSBmcm9tIFwiQHBlcHBlcml6ZS9jZGstcHJpdmF0ZS1idWNrZXRcIjtcbmltcG9ydCB7IGF3c19keW5hbW9kYiwgYXdzX2lhbSwgYXdzX3MzLCBTdGFjayB9IGZyb20gXCJhd3MtY2RrLWxpYlwiO1xuaW1wb3J0IHsgQ29uc3RydWN0IH0gZnJvbSBcImNvbnN0cnVjdHNcIjtcblxuZXhwb3J0IGludGVyZmFjZSBUZXJyYWZvcm1TdGF0ZUJhY2tlbmRQcm9wcyB7XG4gIHJlYWRvbmx5IGJ1Y2tldE5hbWU/OiBzdHJpbmc7XG4gIHJlYWRvbmx5IHBvbGljeU5hbWU/OiBzdHJpbmc7XG4gIHJlYWRvbmx5IHRhYmxlTmFtZT86IHN0cmluZztcbn1cblxuZXhwb3J0IGNsYXNzIFRlcnJhZm9ybVN0YXRlQmFja2VuZCBleHRlbmRzIENvbnN0cnVjdCB7XG4gIHJlYWRvbmx5IGJ1Y2tldDogYXdzX3MzLklCdWNrZXQ7XG4gIHJlYWRvbmx5IHRhYmxlOiBhd3NfZHluYW1vZGIuSVRhYmxlO1xuICByZWFkb25seSBwb2xpY3k6IGF3c19pYW0uSVBvbGljeTtcblxuICBwdWJsaWMgY29uc3RydWN0b3Ioc2NvcGU6IENvbnN0cnVjdCwgaWQ6IHN0cmluZywgcHJvcHM6IFRlcnJhZm9ybVN0YXRlQmFja2VuZFByb3BzKSB7XG4gICAgc3VwZXIoc2NvcGUsIGlkKTtcblxuICAgIGNvbnN0IHsgYnVja2V0TmFtZSwgcG9saWN5TmFtZSwgdGFibGVOYW1lIH0gPSBwcm9wcztcblxuICAgIHRoaXMuYnVja2V0ID0gbmV3IFByaXZhdGVCdWNrZXQodGhpcywgXCJCdWNrZXRcIiwge1xuICAgICAgYnVja2V0TmFtZTogYnVja2V0TmFtZSA/PyBgdGVycmFmb3JtLXN0YXRlLWJhY2tlbmQtJHtTdGFjay5vZih0aGlzKS5hY2NvdW50fS0ke1N0YWNrLm9mKHRoaXMpLnJlZ2lvbn1gLFxuICAgICAgdmVyc2lvbmVkOiB0cnVlLFxuICAgIH0pO1xuXG4gICAgdGhpcy50YWJsZSA9IG5ldyBhd3NfZHluYW1vZGIuVGFibGUodGhpcywgXCJUYWJsZVwiLCB7XG4gICAgICB0YWJsZU5hbWU6IHRhYmxlTmFtZSA/PyBgdGVycmFmb3JtLXN0YXRlLWJhY2tlbmRgLFxuICAgICAgYmlsbGluZ01vZGU6IGF3c19keW5hbW9kYi5CaWxsaW5nTW9kZS5QQVlfUEVSX1JFUVVFU1QsXG4gICAgICBwYXJ0aXRpb25LZXk6IHtcbiAgICAgICAgbmFtZTogXCJMb2NrSURcIixcbiAgICAgICAgdHlwZTogYXdzX2R5bmFtb2RiLkF0dHJpYnV0ZVR5cGUuU1RSSU5HLFxuICAgICAgfSxcbiAgICAgIGVuY3J5cHRpb246IGF3c19keW5hbW9kYi5UYWJsZUVuY3J5cHRpb24uREVGQVVMVCxcbiAgICAgIHBvaW50SW5UaW1lUmVjb3Zlcnk6IHRydWUsXG4gICAgfSk7XG5cbiAgICB0aGlzLnBvbGljeSA9IG5ldyBhd3NfaWFtLlBvbGljeSh0aGlzLCBcIlBvbGljeVwiLCB7XG4gICAgICBwb2xpY3lOYW1lOiBwb2xpY3lOYW1lID8/IGB0ZXJyYWZvcm0tc3RhdGUtYmFja2VuZGAsXG4gICAgICBzdGF0ZW1lbnRzOiBbXG4gICAgICAgIG5ldyBhd3NfaWFtLlBvbGljeVN0YXRlbWVudCh7XG4gICAgICAgICAgZWZmZWN0OiBhd3NfaWFtLkVmZmVjdC5BTExPVyxcbiAgICAgICAgICBhY3Rpb25zOiBbXCJzMzpMaXN0QnVja2V0XCIsIFwiczM6R2V0T2JqZWN0XCIsIFwiczM6UHV0T2JqZWN0XCIsIFwiczM6RGVsZXRlT2JqZWN0XCJdLFxuICAgICAgICAgIHJlc291cmNlczogW2Ake3RoaXMuYnVja2V0LmJ1Y2tldEFybn1gLCBgJHt0aGlzLmJ1Y2tldC5idWNrZXRBcm59LypgXSxcbiAgICAgICAgfSksXG4gICAgICAgIG5ldyBhd3NfaWFtLlBvbGljeVN0YXRlbWVudCh7XG4gICAgICAgICAgZWZmZWN0OiBhd3NfaWFtLkVmZmVjdC5BTExPVyxcbiAgICAgICAgICBhY3Rpb25zOiBbXCJkeW5hbW9kYjpHZXRJdGVtXCIsIFwiZHluYW1vZGI6UHV0SXRlbVwiLCBcImR5bmFtb2RiOkRlbGV0ZUl0ZW1cIl0sXG4gICAgICAgICAgcmVzb3VyY2VzOiBbYCR7dGhpcy50YWJsZS50YWJsZUFybn1gXSxcbiAgICAgICAgfSksXG4gICAgICBdLFxuICAgIH0pO1xuICB9XG59XG4iXX0=
```

##### package/package.json

###### Pretty-printed

 * *Similarity: 0.9705882352941176%*

 * *Differences: {"'version'": "'0.1.99'"}*

```diff
@@ -150,9 +150,9 @@
         "test:watch": "npx projen test:watch",
         "unbump": "npx projen unbump",
         "upgrade-projen": "npx projen upgrade-projen",
         "watch": "npx projen watch"
     },
     "stability": "stable",
     "types": "lib/index.d.ts",
-    "version": "0.1.98"
+    "version": "0.1.99"
 }
```

##### package/changelog.md

```diff
@@ -1,2 +1,2 @@
 
-### [0.1.98](https://github.com/pepperize/cdk-terraform-state-backend/compare/v0.1.97...v0.1.98) (2022-06-22)
+### [0.1.99](https://github.com/pepperize/cdk-terraform-state-backend/compare/v0.1.98...v0.1.99) (2022-06-22)
```

##### package/releasetag.txt

```diff
@@ -1 +1 @@
-v0.1.98
+v0.1.99
```

##### package/version.txt

```diff
@@ -1 +1 @@
-0.1.98
+0.1.99
```

