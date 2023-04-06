# Comparing `tmp/pepperize.cdk-serverless-cluster-from-snapshot-0.0.98.tar.gz` & `tmp/pepperize.cdk-serverless-cluster-from-snapshot-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-serverless-cluster-from-snapshot-0.0.98.tar", last modified: Thu Feb 24 21:42:07 2022, max compression
+gzip compressed data, was "pepperize.cdk-serverless-cluster-from-snapshot-0.0.99.tar", last modified: Thu Feb 24 21:46:17 2022, max compression
```

## Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98.tar` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:42:07.919844 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       23 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     3057 2022-02-24 21:42:07.919844 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1997 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      106 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-02-24 21:42:07.919844 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2005 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:42:07.915843 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:42:07.915843 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3057 2022-02-24 21:42:07.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      724 2022-02-24 21:42:07.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-02-24 21:42:07.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       92 2022-02-24 21:42:07.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       47 2022-02-24 21:42:07.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:42:07.915843 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/
--rw-r--r--   0 runner    (1001) docker     (121)    31670 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:42:07.915843 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/
--rw-r--r--   0 runner    (1001) docker     (121)      431 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    28627 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/cdk-serverless-cluster-from-snapshot@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-02-24 21:41:54.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (121)     1078 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       23 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     3057 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1997 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      106 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2005 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3057 2022-02-24 21:46:17.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      724 2022-02-24 21:46:17.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-02-24 21:46:17.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       92 2022-02-24 21:46:17.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       47 2022-02-24 21:46:17.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/
+-rw-r--r--   0 runner    (1001) docker     (121)    31670 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-24 21:46:17.791424 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (121)      431 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28628 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/cdk-serverless-cluster-from-snapshot@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-02-24 21:46:04.000000 pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/py.typed
```

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/LICENSE` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/PKG-INFO` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-serverless-cluster-from-snapshot
-Version: 0.0.98
+Version: 0.0.99
 Summary: Deprecated: Use https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_rds.ServerlessClusterFromSnapshot.html
 Home-page: https://github.com/pepperize/cdk-serverless-cluster-from-snapshot.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-serverless-cluster-from-snapshot.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/README.md` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/setup.py` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-serverless-cluster-from-snapshot",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "Deprecated: Use https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_rds.ServerlessClusterFromSnapshot.html",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-serverless-cluster-from-snapshot.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_serverless_cluster_from_snapshot",
         "pepperize_cdk_serverless_cluster_from_snapshot._jsii"
     ],
     "package_data": {
         "pepperize_cdk_serverless_cluster_from_snapshot._jsii": [
-            "cdk-serverless-cluster-from-snapshot@0.0.98.jsii.tgz"
+            "cdk-serverless-cluster-from-snapshot@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_serverless_cluster_from_snapshot": [
             "py.typed"
         ]
     },
     "python_requires": ">=3.6",
     "install_requires": [
```

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/PKG-INFO` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-serverless-cluster-from-snapshot
-Version: 0.0.98
+Version: 0.0.99
 Summary: Deprecated: Use https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_rds.ServerlessClusterFromSnapshot.html
 Home-page: https://github.com/pepperize/cdk-serverless-cluster-from-snapshot.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-serverless-cluster-from-snapshot.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/SOURCES.txt` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/SOURCES.txt`

 * *Files 24% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/SOURCES.txt
 src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/dependency_links.txt
 src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/requires.txt
 src/pepperize.cdk_serverless_cluster_from_snapshot.egg-info/top_level.txt
 src/pepperize_cdk_serverless_cluster_from_snapshot/__init__.py
 src/pepperize_cdk_serverless_cluster_from_snapshot/py.typed
 src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/__init__.py
-src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/cdk-serverless-cluster-from-snapshot@0.0.98.jsii.tgz
+src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/cdk-serverless-cluster-from-snapshot@0.0.99.jsii.tgz
```

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/__init__.py` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/__init__.py`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-serverless-cluster-from-snapshot-0.0.98/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/cdk-serverless-cluster-from-snapshot@0.0.98.jsii.tgz` & `pepperize.cdk-serverless-cluster-from-snapshot-0.0.99/src/pepperize_cdk_serverless_cluster_from_snapshot/_jsii/cdk-serverless-cluster-from-snapshot@0.0.99.jsii.tgz`

 * *Files 12% similar despite different names*

#### Comparing `cdk-serverless-cluster-from-snapshot@0.0.98.jsii.tgz-content` & `cdk-serverless-cluster-from-snapshot@0.0.99.jsii.tgz-content`

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.9444444444444444%*

 * *Differences: {"'fingerprint'": "'JJJzQIO4duLcG91ONrx/xak289nKI8BfrUapN5NdQj0='", "'version'": "'0.0.99'"}*

```diff
@@ -2851,15 +2851,15 @@
         }
     },
     "description": "Deprecated: Use https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_rds.ServerlessClusterFromSnapshot.html",
     "docs": {
         "deprecated": true,
         "stability": "deprecated"
     },
-    "fingerprint": "hFADbEB3O9HzvBvS9H4BRuajRiBTue/aUdT+Wl7JU1c=",
+    "fingerprint": "JJJzQIO4duLcG91ONrx/xak289nKI8BfrUapN5NdQj0=",
     "homepage": "https://github.com/pepperize/cdk-serverless-cluster-from-snapshot.git",
     "jsiiVersion": "1.54.0 (build b1b977a)",
     "keywords": [
         "AWS",
         "Aurora",
         "CDK",
         "Cluster",
@@ -3473,9 +3473,9 @@
                         "fqn": "aws-cdk-lib.aws_ec2.SubnetSelection"
                     }
                 }
             ],
             "symbolId": "src/serverless-cluster:ServerlessClusterFromSnapshotProps"
         }
     },
-    "version": "0.0.98"
+    "version": "0.0.99"
 }
```

##### package/lib/serverless-cluster.js

###### js-beautify {}

```diff
@@ -189,10 +189,10 @@
         };
     }
 }
 exports.ServerlessClusterFromSnapshot = ServerlessClusterFromSnapshot;
 _a = JSII_RTTI_SYMBOL_1;
 ServerlessClusterFromSnapshot[_a] = {
     fqn: "@pepperize/cdk-serverless-cluster-from-snapshot.ServerlessClusterFromSnapshot",
-    version: "0.0.98"
+    version: "0.0.99"
 };
 //# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoic2VydmVybGVzcy1jbHVzdGVyLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vc3JjL3NlcnZlcmxlc3MtY2x1c3Rlci50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7OztBQUFBLDZDQWdCcUI7QUFDckIseURBQWlFO0FBQ2pFLCtEQUk4QztBQWdJOUM7Ozs7R0FJRztBQUNILE1BQWEsNkJBQThCLFNBQVEsc0JBQVE7SUFzQ3pELFlBQVksS0FBZ0IsRUFBRSxFQUFVLEVBQUUsS0FBeUM7O1FBQ2pGLEtBQUssQ0FBQyxLQUFLLEVBQUUsRUFBRSxDQUFDLENBQUM7UUFFakIsSUFBSSxDQUFDLEdBQUcsR0FBRyxLQUFLLENBQUMsR0FBRyxDQUFDO1FBQ3JCLElBQUksQ0FBQyxVQUFVLEdBQUcsS0FBSyxDQUFDLFVBQVUsQ0FBQztRQUVuQyxJQUFJLENBQUMsNkJBQTZCLEdBQUcsS0FBSyxDQUFDLE1BQU0sQ0FBQyw2QkFBNkIsQ0FBQztRQUNoRixJQUFJLENBQUMsNEJBQTRCLEdBQUcsS0FBSyxDQUFDLE1BQU0sQ0FBQyw0QkFBNEIsQ0FBQztRQUU5RSxJQUFJLENBQUMsYUFBYSxHQUFHLEtBQUssQ0FBQyxhQUFhLENBQUM7UUFFekMsTUFBTSxFQUFFLFNBQVMsRUFBRSxHQUFHLElBQUksQ0FBQyxHQUFHLENBQUMsYUFBYSxDQUFDLElBQUksQ0FBQyxVQUFVLENBQUMsQ0FBQztRQUU5RCw2RkFBNkY7UUFDN0YsSUFBSSxTQUFTLENBQUMsTUFBTSxHQUFHLENBQUMsRUFBRTtZQUN4Qix5QkFBVyxDQUFDLEVBQUUsQ0FBQyxJQUFJLENBQUMsQ0FBQyxRQUFRLENBQUMsNENBQTRDLFNBQVMsQ0FBQyxNQUFNLEVBQUUsQ0FBQyxDQUFDO1NBQy9GO1FBRUQsSUFBSSxDQUFDLFdBQVcsU0FDZCxLQUFLLENBQUMsV0FBVyxtQ0FDakIsSUFBSSxxQkFBTyxDQUFDLFdBQVcsQ0FBQyxJQUFJLEVBQUUsU0FBUyxFQUFFO1lBQ3ZDLFdBQVcsRUFBRSxlQUFl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QUMsYUFBYSxLQUFLLEtBQUssRUFBRTtZQUNoQyxNQUFNLElBQUksS0FBSyxDQUFDLDREQUE0RCxDQUFDLENBQUM7U0FDL0U7UUFFRCxJQUFJLENBQUMsYUFBYSxHQUFHLElBQUksQ0FBQztRQUMxQixNQUFNLEdBQUcsR0FBRyxxQkFBTyxDQUFDLEtBQUssQ0FBQyxjQUFjLENBQUM7WUFDdkMsT0FBTztZQUNQLE9BQU8sRUFBRSx3QkFBZ0I7WUFDekIsWUFBWSxFQUFFLENBQUMsR0FBRyxDQUFDO1lBQ25CLEtBQUssRUFBRSxJQUFJO1NBQ1osQ0FBQyxDQUFDO1FBQ0gsTUFBQSxJQUFJLENBQUMsTUFBTSwwQ0FBRSxTQUFTLENBQUMsT0FBTyxFQUFFO1FBQ2hDLE9BQU8sR0FBRyxDQUFDO0lBQ2IsQ0FBQztJQUVEOztPQUVHO0lBQ0ksd0JBQXdCO1FBQzdCLE9BQU87WUFDTCxRQUFRLEVBQUUsSUFBSSxDQUFDLGlCQUFpQjtZQUNoQyxVQUFVLEVBQUUsZ0NBQWtCLENBQUMsb0JBQW9CLENBQUMsY0FBYztTQUNuRSxDQUFDO0lBQ0osQ0FBQzs7QUE1T0gsc0VBNk9DIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHtcbiAgYXdzX2VjMixcbiAgYXdzX2lhbSxcbiAgYXdzX2ttcyxcbiAgYXdzX3NlY3JldHNtYW5hZ2VyLFxuICBhd3NfcmRzLFxuICBjeF9hcGksXG4gIEFubm90YXRpb25zLFxuICBEdXJhdGlvbixcbiAgRmVhdHVyZUZsYWdzLFxuICBMYXp5LFxuICBSZW1vdmFsUG9saWN5LFxuICBUb2tlbixcbiAgUmVzb3VyY2UsXG4gIEFybkZvcm1hdCxcbiAgU3RhY2ssXG59IGZyb20gXCJhd3MtY2RrLWxpYlwiO1xuaW1wb3J0IHsgREFUQV9BUElfQUNUSU9OUyB9IGZyb20gXCJhd3MtY2RrLWxpYi9hd3MtcmRzL2xpYi9wZXJtc1wiO1xuaW1wb3J0IHtcbiAgREVGQVVMVF9QQVNTV09SRF9FWENMVURFX0NIQVJTLFxuICBkZWZhdWx0RGVsZXRpb25Qcm90ZWN0aW9uLFxuICByZW5kZXJDcmVkZW50aWFscyxcbn0gZnJvbSBcImF3cy1jZGstbGliL2F3cy1yZHMvbGliL3ByaXZhdGUvdXRpbFwiO1xuaW1wb3J0IHsgQ29uc3RydWN0IH0gZnJvbSBcImNvbnN0cnVjdHNcIjtcblxuLyoqXG4gKiAgUHJvcGVydGllcyB0byBjb25maWd1cmUgYW4gQXVyb3JhIFNlcnZlcmxlc3MgQ2x1c3RlclxuICpcbiAqL1xuZXhwb3J0IGludGVyZmFjZSBTZXJ2ZXJsZXNzQ2x1c3RlckZyb21TbmFwc2hvdFByb3BzIHtcbiAgLyoqXG4gICAqIFdoYXQga2luZCBvZiBkYXRhYmFzZSB0byBzdGFydFxuICAgKi9cbiAgcmVhZG9ubHkgZW5naW5lOiBhd3NfcmRzLklDbHVzdGVyRW5naW5lO1xuXG4gIC8qKlxuICAgKiBDcmVkZW50aWFscyBmb3IgdGhlIGFkbWluaXN0cmF0aXZlIHVzZXJcbiAgICpcbiAgICogQGRlZmF1bHQgLSBBIHVzZXJuYW1lIG9mICdhZG1pbicgYW5kIFNlY3JldHNNYW5hZ2VyLWdlbmVyYXRlZCBwYXNzd29yZFxuICAgKi9cbiAgcmVhZG9ubHkgY3JlZGVudGlhbHM/OiBhd3NfcmRzLkNyZWRlbnRpYWxzO1xuXG4gIC8qKlxuICAgKiBBbiBvcHRpb25hbCBpZGVudGlmaWVyIGZvciB0aGUgY2x1c3RlclxuICAgKlxuICAgKiBAZGVmYXVsdCAtIEEgbmFtZSBpcyBhdXRvbWF0aWNhbGx5IGdlbmVyYXRlZC5cbiAgICovXG4gIHJlYWRvbmx5IGNsdXN0ZXJJZGVudGlmaWVyPzogc3RyaW5nO1xuXG4gIC8qKlxuICAgKiBUaGUgaWRlbnRpZmllciBmb3IgdGhlIERCIHNuYXBzaG90IG9yIERCIGNsdXN0ZXIgc25hcHNob3QgdG8gcmVzdG9yZSBmcm9tLlxuICAgKlxuICAgKiBZb3UgY2FuIHVzZSBlaXRoZXIgdGhlIG5hbWUgb3IgdGhlIEFtYXpvbiBSZXNvdXJjZSBOYW1lIChBUk4pIHRvIHNwZWNpZnkgYSBEQiBjbHVzdGVyIHNuYXBzaG90LiBIb3dldmVyLCB5b3UgY2FuIHVzZSBvbmx5IHRoZSBBUk4gdG8gc3BlY2lmeSBhIERCIHNuYXBzaG90LlxuICAgKlxuICAgKiBBZnRlciB5b3UgcmVzdG9yZSBhIERCIGNsdXN0ZXIgd2l0aCBhIFNuYXBzaG90SWRlbnRpZmllciBwcm9wZXJ0eSwgeW91IG11c3Qgc3BlY2lmeSB0aGUgc2FtZSBTbmFwc2hvdElkZW50aWZpZXIgcHJvcGVydHkgZm9yIGFueSBmdXR1cmUgdXBkYXRlcyB0byB0aGUgREIgY2x1c3Rlci4gV2hlbiB5b3Ugc3BlY2lmeSB0aGlzIHByb3BlcnR5IGZvciBhbiB1cGRhdGUsIHRoZSBEQiBjbHVzdGVyIGlzIG5vdCByZXN0b3JlZCBmcm9tIHRoZSBzbmFwc2hvdCBhZ2FpbiwgYW5kIHRoZSBkYXRhIGluIHRoZSBkYXRhYmFzZSBpcyBub3QgY2hhbmdlZC4gSG93ZXZlciwgaWYgeW91IGRvbid0IHNwZWNpZnkgdGhlIFNuYXBzaG90SWRlbnRpZmllciBwcm9wZXJ0eSwgYW4gZW1wdHkgREIgY2x1c3RlciBpcyBjcmVhdGVkLCBhbmQgdGhlIG9yaWdpbmFsIERCIGNsdXN0ZXIgaXMgZGVsZXRlZC4gSWYgeW91IHNwZWNpZnkgYSBwcm9wZXJ0eSB0aGF0IGlzIGRpZmZlcmVudCBmcm9tIHRoZSBwcmV2aW91cyBzbmFwc2hvdCByZXN0b3JlIHByb3BlcnR5LCBhIG5ldyBEQiBjbHVzdGVyIGlzIHJlc3RvcmVkIGZyb20gdGhlIHNwZWNpZmllZCBTbmFwc2hvdElkZW50aWZpZXIgcHJvcGVydHksIGFuZCB0aGUgb3JpZ2luYWwgREIgY2x1c3RlciBpcyBkZWxldGVkLlxuICAgKi9cbiAgcmVhZG9ubHkgc25hcHNob3RJZGVudGlmaWVyOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFRoZSBudW1iZXIgb2YgZGF5cyBkdXJpbmcgd2hpY2ggYXV0b21hdGljIERCIHNuYXBzaG90cyBhcmUgcmV0YWluZWQuXG4gICAqIEF1dG9tYXRpYyBiYWNrdXAgcmV0ZW50aW9uIGNhbm5vdCBiZSBkaXNhYmxlZCBvbiBzZXJ2ZXJsZXNzIGNsdXN0ZXJzLlxuICAgKiBNdXN0IGJlIGEgdmFsdWUgZnJvbSAxIGRheSB0byAzNSBkYXlzLlxuICAgKlxuICAgKiBAZGVmYXVsdCBEdXJhdGlvbi5kYXlzKDEpXG4gICAqL1xuICByZWFkb25seSBiYWNrdXBSZXRlbnRpb24/OiBEdXJhdGlvbjtcblxuICAvKipcbiAgICogTmFtZSBvZiBhIGRhdGFiYXNlIHdoaWNoIGlzIGF1dG9tYXRpY2FsbHkgY3JlYXRlZCBpbnNpZGUgdGhlIGNsdXN0ZXJcbiAgICpcbiAgICogQGRlZmF1bHQgLSBEYXRhYmFzZSBpcyBub3QgY3JlYXRlZCBpbiBjbHVzdGVyLlxuICAgKi9cbiAgcmVhZG9ubHkgZGVmYXVsdERhdGFiYXNlTmFtZT86IHN0cmluZztcblxuICAvKipcbiAgICogSW5kaWNhdGVzIHdoZXRoZXIgdGhlIERCIGNsdXN0ZXIgc2hvdWxkIGhhdmUgZGVsZXRpb24gcHJvdGVjdGlvbiBlbmFibGVkLlxuICAgKlxuICAgKiBAZGVmYXVsdCAtIHRydWUgaWYgcmVtb3ZhbFBvbGljeSBpcyBSRVRBSU4sIGZhbHNlIG90aGVyd2lzZVxuICAgKi9cbiAgcmVhZG9ubHkgZGVsZXRpb25Qcm90ZWN0aW9uPzogYm9vbGVhbjtcblxuICAvKipcbiAgICogV2hldGhlciB0byBlbmFibGUgdGhlIERhdGEgQVBJLlxuICAgKlxuICAgKiBAc2VlIGh0dHBzOi8vZG9jcy5hd3MuYW1hem9uLmNvbS9BbWF6b25SRFMvbGF0ZXN0L0F1cm9yYVVzZXJHdWlkZS9kYXRhLWFwaS5odG1sXG4gICAqXG4gICAqIEBkZWZhdWx0IGZhbHNlXG4gICAqL1xuICByZWFkb25seSBlbmFibGVEYXRhQXBpPzogYm9vbGVhbjtcblxuICAvKipcbiAgICogVGhlIFZQQyB0aGF0IHRoaXMgQXVyb3JhIFNlcnZlcmxlc3MgY2x1c3RlciBoYXMgYmVlbiBjcmVhdGVkIGluLlxuICAgKi9cbiAgcmVhZG9ubHkgdnBjOiBhd3NfZWMyLklWcGM7XG5cbiAgLyoqXG4gICAqIFdoZXJlIHRvIHBsYWNlIHRoZSBpbnN0YW5jZXMgd2l0aGluIHRoZSBWUENcbiAgICpcbiAgICogQGRlZmF1bHQgLSB0aGUgVlBDIGRlZmF1bHQgc3RyYXRlZ3kgaWYgbm90IHNwZWNpZmllZC5cbiAgICovXG4gIHJlYWRvbmx5IHZwY1N1Ym5ldHM/OiBhd3NfZWMyLlN1Ym5ldFNlbGVjdGlvbjtcblxuICAvKipcbiAgICogU2NhbGluZyBjb25maWd1cmF0aW9uIG9mIGFuIEF1cm9yYSBTZXJ2ZXJsZXNzIGRhdGFiYXNlIGNsdXN0ZXIuXG4gICAqXG4gICAqIEBkZWZhdWx0IC0gU2VydmVybGVzcyBjbHVzdGVyIGlzIGF1dG9tYXRpY2FsbHkgcGF1c2VkIGFmdGVyIDUgbWludXRlcyBvZiBiZWluZyBpZGxlLlxuICAgKiAgIG1pbmltdW0gY2FwYWNpdHk6IDIgQUNVXG4gICAqICAgbWF4aW11bSBjYXBhY2l0eTogMTYgQUNVXG4gICAqL1xuICByZWFkb25seSBzY2FsaW5nPzogYXdzX3Jkcy5TZXJ2ZXJsZXNzU2NhbGluZ09wdGlvbnM7XG5cbiAgLyoqXG4gICAqIFRoZSByZW1vdmFsIHBvbGljeSB0byBhcHBseSB3aGVuIHRoZSBjbHVzdGVyIGFuZCBpdHMgaW5zdGFuY2VzIGFyZSByZW1vdmVkXG4gICAqIGZyb20gdGhlIHN0YWNrIG9yIHJlcGxhY2VkIGR1cmluZyBhbiB1cGRhdGUuXG4gICAqXG4gICAqIEBkZWZhdWx0IC0gUmVtb3ZhbFBvbGljeS5TTkFQU0hPVCAocmVtb3ZlIHRoZSBjbHVzdGVyIGFuZCBpbnN0YW5jZXMsIGJ1dCByZXRhaW4gYSBzbmFwc2hvdCBvZiB0aGUgZGF0YSlcbiAgICovXG4gIHJlYWRvbmx5IHJlbW92YWxQb2xpY3k/OiBSZW1vdmFsUG9saWN5O1xuXG4gIC8qKlxuICAgKiBTZWN1cml0eSBncm91cC5cbiAgICpcbiAgICogQGRlZmF1bHQgLSBhIG5ldyBzZWN1cml0eSBncm91cCBpcyBjcmVhdGVkLlxuICAgKi9cbiAgcmVhZG9ubHkgc2VjdXJpdHlHcm91cHM/OiBhd3NfZWMyLklTZWN1cml0eUdyb3VwW107XG5cbiAgLyoqXG4gICAqIFRoZSBLTVMga2V5IGZvciBzdG9yYWdlIGVuY3J5cHRpb24uXG4gICAqXG4gICAqIElmIHlvdSBzcGVjaWZ5IHRoZSBTbmFwc2hvdElkZW50aWZpZXIgcHJvcGVydHksIHRoZSBTdG9yYWdlRW5jcnlwdGVkIHByb3BlcnR5IHZhbHVlIGlzIGluaGVyaXRlZCBmcm9tIHRoZSBzbmFwc2hvdCwgYW5kIGlmIHRoZSBEQiBjbHVzdGVyIGlzIGVuY3J5cHRlZCwgdGhlIHNwZWNpZmllZCBLbXNLZXlJZCBwcm9wZXJ0eSBpcyB1c2VkLlxuICAgKlxuICAgKiBAZGVmYXVsdCAtIHRoZSBkZWZhdWx0IG1hc3RlciBrZXkgd2lsbCBiZSB1c2VkIGZvciBzdG9yYWdlIGVuY3J5cHRpb25cbiAgICovXG4gIHJlYWRvbmx5IHN0b3JhZ2VFbmNyeXB0aW9uS2V5PzogYXdzX2ttcy5JS2V5O1xuXG4gIC8qKlxuICAgKiBBZGRpdGlvbmFsIHBhcmFtZXRlcnMgdG8gcGFzcyB0byB0aGUgZGF0YWJhc2UgZW5naW5lXG4gICAqXG4gICAqIEBkZWZhdWx0IC0gbm8gcGFyYW1ldGVyIGdyb3VwLlxuICAgKi9cbiAgcmVhZG9ubHkgcGFyYW1ldGVyR3JvdXA/OiBhd3NfcmRzLklQYXJhbWV0ZXJHcm91cDtcblxuICAvKipcbiAgICogRXhpc3Rpbmcgc3VibmV0IGdyb3VwIGZvciB0aGUgY2x1c3Rlci5cbiAgICpcbiAgICogQGRlZmF1bHQgLSBhIG5ldyBzdWJuZXQgZ3JvdXAgd2lsbCBiZSBjcmVhdGVkLlxuICAgKi9cbiAgcmVhZG9ubHkgc3VibmV0R3JvdXA/OiBhd3NfcmRzLklTdWJuZXRHcm91cDtcbn1cblxuLyoqXG4gKiBBIFNlcnZlcmxlc3MgQ2x1c3RlciByZXN0b3JlZCBmcm9tIGEgc25hcHNob3QuXG4gKlxuICogQHJlc291cmNlIEFXUzo6UkRTOjpEQkluc3RhbmNlXG4gKi9cbmV4cG9ydCBjbGFzcyBTZXJ2ZXJsZXNzQ2x1c3RlckZyb21TbmFwc2hvdCBleHRlbmRzIFJlc291cmNlIGltcGxlbWVudHMgYXdzX3Jkcy5JU2VydmVybGVzc0NsdXN0ZXIge1xuICAvKipcbiAgICogSWRlbnRpZmllciBvZiB0aGUgY2x1c3RlclxuICAgKi9cbiAgcHVibGljIHJlYWRvbmx5IGNsdXN0ZXJJZGVudGlmaWVyOiBzdHJpbmc7XG5cbiAgLyoqXG4gICAqIFRoZSBlbmRwb2ludCB0byB1c2UgZm9yIHJlYWQvd3JpdGUgb3BlcmF0aW9uc1xuICAgKi9cbiAgcHVibGljIHJlYWRvbmx5IGNsdXN0ZXJFbmRwb2ludDogYXdzX3Jkcy5FbmRwb2ludDtcblxuICAvKipcbiAgICogVGhlIGVuZHBvaW50IHRvIHVzZSBmb3IgcmVhZC93cml0ZSBvcGVyYXRpb25zXG4gICAqL1xuICBwdWJsaWMgcmVhZG9ubHkgY2x1c3RlclJlYWRFbmRwb2ludDogYXdzX3Jkcy5FbmRwb2ludDtcblxuICAvKipcbiAgICogQWNjZXNzIHRvIHRoZSBuZXR3b3JrIGNvbm5lY3Rpb25zXG4gICAqL1xuICBwdWJsaWMgcmVhZG9ubHkgY29ubmVjdGlvbnM6IGF3c19lYzIuQ29ubmVjdGlvbnM7XG5cbiAgLyoqXG4gICAqIFRoZSBzZWNyZXQgYXR0YWNoZWQgdG8gdGhpcyBjbHVzdGVyXG4gICAqL1xuICBwdWJsaWMgcmVhZG9ubHkgc2VjcmV0PzogYXdzX3NlY3JldHNtYW5hZ2VyLklTZWNyZXQ7XG5cbiAgcHJvdGVjdGVkIGVuYWJsZURhdGFBcGk/OiBib29sZWFuO1xuXG4gIHByaXZhdGUgcmVhZG9ubHkgc3VibmV0R3JvdXA6IGF3c19yZHMuSVN1Ym5ldEdyb3VwO1xuXG4gIHByaXZhdGUgcmVhZG9ubHkgdnBjOiBhd3NfZWMyLklWcGM7XG5cbiAgcHJpdmF0ZSByZWFkb25seSB2cGNTdWJuZXRzPzogYXdzX2VjMi5TdWJuZXRTZWxlY3Rpb247XG5cbiAgcHJpdmF0ZSByZWFkb25seSBzaW5nbGVVc2VyUm90YXRpb25BcHBsaWNhdGlvbjogYXdzX3NlY3JldHNtYW5hZ2VyLlNlY3JldFJvdGF0aW9uQXBwbGljYXRpb247XG5cbiAgcHJpdmF0ZSByZWFkb25seSBtdWx0aVVzZXJSb3RhdGlvbkFwcGxpY2F0aW9uOiBhd3Nfc2VjcmV0c21hbmFnZXIuU2VjcmV0Um90YXRpb25BcHBsaWNhdGlvbjtcblxuICBjb25zdHJ1Y3RvcihzY29wZTogQ29uc3RydWN0LCBpZDogc3RyaW5nLCBwcm9wczogU2VydmVybGVzc0NsdXN0ZXJGcm9tU25hcHNob3RQcm9wcykge1xuICAgIHN1cGVyKHNjb3BlLCBpZCk7XG5cbiAgICB0aGlzLnZwYyA9IHByb3BzLnZwYztcbiAgICB0aGlzLnZwY1N1Ym5ldHMgPSBwcm9wcy52cGNTdWJuZXRzO1xuXG4gICAgdGhpcy5zaW5nbGVVc2VyUm90YXRpb25BcHBsaWNhdGlvbiA9IHByb3BzLmVuZ2luZS5zaW5nbGVVc2VyUm90YXRpb25BcHBsaWNhdGlvbjtcbiAgICB0aGlzLm11bHRpVXNlclJvdGF0aW9uQXBwbGljYXRpb24gPSBwcm9wcy5lbmdpbmUubXVsdGlVc2VyUm90YXRpb25BcHBsaWNhdGlvbjtcblxuICAgIHRoaXMuZW5hYmxlRGF0YUFwaSA9IHByb3BzLmVuYWJsZURhdGFBcGk7XG5cbiAgICBjb25zdCB7IHN1Ym5ldElkcyB9ID0gdGhpcy52cGMuc2VsZWN0U3VibmV0cyh0aGlzLnZwY1N1Ym5ldHMpO1xuXG4gICAgLy8gQ2Fubm90IHRlc3Qgd2hldGhlciB0aGUgc3VibmV0cyBhcmUgaW4gZGlmZmVyZW50IEFacywgYnV0IGF0IGxlYXN0IHdlIGNhbiB0ZXN0IHRoZSBhbW91bnQuXG4gICAgaWYgKHN1Ym5ldElkcy5sZW5ndGggPCAyKSB7XG4gICAgICBBbm5vdGF0aW9ucy5vZih0aGlzKS5hZGRFcnJvcihgQ2x1c3RlciByZXF1aXJlcyBhdCBsZWFzdCAyIHN1Ym5ldHMsIGdvdCAke3N1Ym5ldElkcy5sZW5ndGh9YCk7XG4gICAgfVxuXG4gICAgdGhpcy5zdWJuZXRHcm91cCA9XG4gICAgICBwcm9wcy5zdWJuZXRHcm91cCA/P1xuICAgICAgbmV3IGF3c19yZHMuU3VibmV0R3JvdXAodGhpcywgXCJTdWJuZXRzXCIsIHtcbiAgICAgICAgZGVzY3JpcHRpb246IGBTdWJuZXRzIGZvciAke2lkfSBkYXRhYmFzZWAsXG4gICAgICAgIHZwYzogcHJvcHMudnBjLFxuICAgICAgICB2cGNTdWJuZXRzOiBwcm9wcy52cGNTdWJuZXRzLFxuICAgICAgICByZW1vdmFsUG9saWN5OiBwcm9wcy5yZW1vdmFsUG9saWN5ID09PSBSZW1vdmFsUG9saWN5LlJFVEFJTiA/IHByb3BzLnJlbW92YWxQb2xpY3kgOiB1bmRlZmluZWQsXG4gICAgICB9KTtcblxuICAgIGlmIChwcm9wcy5iYWNrdXBSZXRlbnRpb24pIHtcbiAgICAgIGNvbnN0IGJhY2t1cFJldGVudGlvbkRheXMgPSBwcm9wcy5iYWNrdXBSZXRlbnRpb24udG9EYXlzKCk7XG4gICAgICBpZiAoYmFja3VwUmV0ZW50aW9uRGF5cyA8IDEgfHwgYmFja3VwUmV0ZW50aW9uRGF5cyA+IDM1KSB7XG4gICAgICAgIHRocm93IG5ldyBFcnJvcihgYmFja3VwIHJldGVudGlvbiBwZXJpb2QgbXVzdCBiZSBiZXR3ZWVuIDEgYW5kIDM1IGRheXMuIHJlY2VpdmVkOiAke2JhY2t1cFJldGVudGlvbkRheXN9YCk7XG4gICAgICB9XG4gICAgfVxuXG4gICAgLy8gYmluZCB0aGUgZW5naW5lIHRvIHRoZSBDbHVzdGVyXG4gICAgY29uc3QgY2x1c3RlckVuZ2luZUJpbmRDb25maWcgPSBwcm9wcy5lbmdpbmUuYmluZFRvQ2x1c3Rlcih0aGlzLCB7XG4gICAgICBwYXJhbWV0ZXJHcm91cDogcHJvcHMucGFyYW1ldGVyR3JvdXAsXG4gICAgfSk7XG4gICAgY29uc3QgY2x1c3RlclBhcmFtZXRlckdyb3VwID0gcHJvcHMucGFyYW1ldGVyR3JvdXAgPz8gY2x1c3RlckVuZ2luZUJpbmRDb25maWcucGFyYW1ldGVyR3JvdXA7XG4gICAgY29uc3QgY2x1c3RlclBhcmFtZXRlckdyb3VwQ29uZmlnID0gY2x1c3RlclBhcmFtZXRlckdyb3VwPy5iaW5kVG9DbHVzdGVyKHt9KTtcblxuICAgIGNvbnN0IHNlY3VyaXR5R3JvdXBzID0gcHJvcHMuc2VjdXJpdHlHcm91cHMgPz8gW1xuICAgICAgbmV3IGF3c19lYzIuU2VjdXJpdHlHcm91cCh0aGlzLCBcIlNlY3VyaXR5R3JvdXBcIiwge1xuICAgICAgICBkZXNjcmlwdGlvbjogXCJSRFMgc2VjdXJpdHkgZ3JvdXBcIixcbiAgICAgICAgdnBjOiB0aGlzLnZwYyxcbiAgICAgIH0pLFxuICAgIF07XG5cbiAgICBjb25zdCBjbHVzdGVySWRlbnRpZmllciA9IEZlYXR1cmVGbGFncy5vZih0aGlzKS5pc0VuYWJsZWQoY3hfYXBpLlJEU19MT1dFUkNBU0VfREJfSURFTlRJRklFUilcbiAgICAgID8gcHJvcHMuY2x1c3RlcklkZW50aWZpZXI/LnRvTG93ZXJDYXNlKClcbiAgICAgIDogcHJvcHMuY2x1c3RlcklkZW50aWZpZXI7XG5cbiAgICBjb25zdCBjbHVzdGVyID0gbmV3IGF3c19yZHMuQ2ZuREJDbHVzdGVyKHRoaXMsIFwiUmVzb3VyY2VcIiwge1xuICAgICAgYmFja3VwUmV0ZW50aW9uUGVyaW9kOiBwcm9wcy5iYWNrdXBSZXRlbnRpb24/LnRvRGF5cygpLFxuICAgICAgZGF0YWJhc2VOYW1lOiBwcm9wcy5kZWZhdWx0RGF0YWJhc2VOYW1lLFxuICAgICAgZGJDbHVzdGVySWRlbnRpZmllcjogY2x1c3RlcklkZW50aWZpZXIsXG4gICAgICBzbmFwc2hvdElkZW50aWZpZXI6IHByb3BzLnNuYXBzaG90SWRlbnRpZmllcixcbiAgICAgIGRiQ2x1c3RlclBhcmFtZXRlckdyb3VwTmFtZTogY2x1c3RlclBhcmFtZXRlckdyb3VwQ29uZmlnPy5wYXJhbWV0ZXJHcm91cE5hbWUsXG4gICAgICBkYlN1Ym5ldEdyb3VwTmFtZTogdGhpcy5zdWJuZXRHcm91cC5zdWJuZXRHcm91cE5hbWUsXG4gICAgICBkZWxldGlvblByb3RlY3Rpb246IGRlZmF1bHREZWxldGlvblByb3RlY3Rpb24ocHJvcHMuZGVsZXRpb25Qcm90ZWN0aW9uLCBwcm9wcy5yZW1vdmFsUG9saWN5KSxcbiAgICAgIGVuZ2luZTogcHJvcHMuZW5naW5lLmVuZ2luZVR5cGUsXG4gICAgICBlbmdpbmVWZXJzaW9uOiBwcm9wcy5lbmdpbmUuZW5naW5lVmVyc2lvbj8uZnVsbFZlcnNpb24sXG4gICAgICBlbmdpbmVNb2RlOiBcInNlcnZlcmxlc3NcIixcbiAgICAgIGVuYWJsZUh0dHBFbmRwb2ludDogTGF6eS5hbnkoeyBwcm9kdWNlOiAoKSA9PiB0aGlzLmVuYWJsZURhdGFBcGkgfSksXG4gICAgICBrbXNLZXlJZDogcHJvcHMuc3RvcmFnZUVuY3J5cHRpb25LZXk/LmtleUFybixcbiAgICAgIHNjYWxpbmdDb25maWd1cmF0aW9uOiBwcm9wcy5zY2FsaW5nID8gdGhpcy5yZW5kZXJTY2FsaW5nQ29uZmlndXJhdGlvbihwcm9wcy5zY2FsaW5nKSA6IHVuZGVmaW5lZCxcbiAgICAgIHZwY1NlY3VyaXR5R3JvdXBJZHM6IHNlY3VyaXR5R3JvdXBzLm1hcCgoc2cpID0+IHNnLnNlY3VyaXR5R3JvdXBJZCksXG4gICAgfSk7XG5cbiAgICB0aGlzLmNsdXN0ZXJJZGVudGlmaWVyID0gY2x1c3Rlci5yZWY7XG5cbiAgICAvLyBjcmVhdGUgYSBudW1iZXIgdG9rZW4gdGhhdCByZXByZXNlbnRzIHRoZSBwb3J0IG9mIHRoZSBjbHVzdGVyXG4gICAgY29uc3QgcG9ydEF0dHJpYnV0ZSA9IFRva2VuLmFzTnVtYmVyKGNsdXN0ZXIuYXR0ckVuZHBvaW50UG9ydCk7XG4gICAgdGhpcy5jbHVzdGVyRW5kcG9pbnQgPSBuZXcgYXdzX3Jkcy5FbmRwb2ludChjbHVzdGVyLmF0dHJFbmRwb2ludEFkZHJlc3MsIHBvcnRBdHRyaWJ1dGUpO1xuICAgIHRoaXMuY2x1c3RlclJlYWRFbmRwb2ludCA9IG5ldyBhd3NfcmRzLkVuZHBvaW50KGNsdXN0ZXIuYXR0clJlYWRFbmRwb2ludEFkZHJlc3MsIHBvcnRBdHRyaWJ1dGUpO1xuICAgIHRoaXMuY29ubmVjdGlvbnMgPSBuZXcgYXdzX2VjMi5Db25uZWN0aW9ucyh7XG4gICAgICBzZWN1cml0eUdyb3VwcyxcbiAgICAgIGRlZmF1bHRQb3J0OiBhd3NfZWMyLlBvcnQudGNwKHRoaXMuY2x1c3RlckVuZHBvaW50LnBvcnQpLFxuICAgIH0pO1xuXG4gICAgY2x1c3Rlci5hcHBseVJlbW92YWxQb2xpY3kocHJvcHMucmVtb3ZhbFBvbGljeSA/PyBSZW1vdmFsUG9saWN5LlNOQVBTSE9UKTtcblxuICAgIGNvbnN0IGNyZWRlbnRpYWxzID0gcmVuZGVyQ3JlZGVudGlhbHModGhpcywgcHJvcHMuZW5naW5lLCBwcm9wcy5jcmVkZW50aWFscyk7XG4gICAgY29uc3Qgc2VjcmV0ID0gY3JlZGVudGlhbHMuc2VjcmV0O1xuICAgIGlmIChzZWNyZXQpIHtcbiAgICAgIHRoaXMuc2VjcmV0ID0gc2VjcmV0LmF0dGFjaCh0aGlzKTtcbiAgICB9XG4gIH1cblxuICAvKipcbiAgICogQWRkcyB0aGUgc2luZ2xlIHVzZXIgcm90YXRpb24gb2YgdGhlIG1hc3RlciBwYXNzd29yZCB0byB0aGlzIGNsdXN0ZXIuXG4gICAqL1xuICBwdWJsaWMgYWRkUm90YXRpb25TaW5nbGVVc2VyKG9wdGlvbnM6IGF3c19yZHMuUm90YXRpb25TaW5nbGVVc2VyT3B0aW9ucyA9IHt9KTogYXdzX3NlY3JldHNtYW5hZ2VyLlNlY3JldFJvdGF0aW9uIHtcbiAgICBpZiAoIXRoaXMuc2VjcmV0KSB7XG4gICAgICB0aHJvdyBuZXcgRXJyb3IoXCJDYW5ub3QgYWRkIHNpbmdsZSB1c2VyIHJvdGF0aW9uIGZvciBhIGNsdXN0ZXIgd2l0aG91dCBzZWNyZXQuXCIpO1xuICAgIH1cblxuICAgIGNvbnN0IGlkID0gXCJSb3RhdGlvblNpbmdsZVVzZXJcIjtcbiAgICBjb25zdCBleGlzdGluZyA9IHRoaXMubm9kZS50cnlGaW5kQ2hpbGQoaWQpO1xuICAgIGlmIChleGlzdGluZykge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKFwiQSBzaW5nbGUgdXNlciByb3RhdGlvbiB3YXMgYWxyZWFkeSBhZGRlZCB0byB0aGlzIGNsdXN0ZXIuXCIpO1xuICAgIH1cblxuICAgIHJldHVybiBuZXcgYXdzX3NlY3JldHNtYW5hZ2VyLlNlY3JldFJvdGF0aW9uKHRoaXMsIGlkLCB7XG4gICAgICBzZWNyZXQ6IHRoaXMuc2VjcmV0LFxuICAgICAgYXBwbGljYXRpb246IHRoaXMuc2luZ2xlVXNlclJvdGF0aW9uQXBwbGljYXRpb24sXG4gICAgICB2cGM6IHRoaXMudnBjLFxuICAgICAgdnBjU3VibmV0czogdGhpcy52cGNTdWJuZXRzLFxuICAgICAgdGFyZ2V0OiB0aGlzLFxuICAgICAgLi4ub3B0aW9ucyxcbiAgICAgIGV4Y2x1ZGVDaGFyYWN0ZXJzOiBvcHRpb25zLmV4Y2x1ZGVDaGFyYWN0ZXJzID8/IERFRkFVTFRfUEFTU1dPUkRfRVhDTFVERV9DSEFSUyxcbiAgICB9KTtcbiAgfVxuXG4gIC8qKlxuICAgKiBBZGRzIHRoZSBtdWx0aSB1c2VyIHJvdGF0aW9uIHRvIHRoaXMgY2x1c3Rlci5cbiAgICovXG4gIHB1YmxpYyBhZGRSb3RhdGlvbk11bHRpVXNlcihcbiAgICBpZDogc3RyaW5nLFxuICAgIG9wdGlvbnM6IGF3c19yZHMuUm90YXRpb25NdWx0aVVzZXJPcHRpb25zXG4gICk6IGF3c19zZWNyZXRzbWFuYWdlci5TZWNyZXRSb3RhdGlvbiB7XG4gICAgaWYgKCF0aGlzLnNlY3JldCkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKFwiQ2Fubm90IGFkZCBtdWx0aSB1c2VyIHJvdGF0aW9uIGZvciBhIGNsdXN0ZXIgd2l0aG91dCBzZWNyZXQuXCIpO1xuICAgIH1cbiAgICByZXR1cm4gbmV3IGF3c19zZWNyZXRzbWFuYWdlci5TZWNyZXRSb3RhdGlvbih0aGlzLCBpZCwge1xuICAgICAgLi4ub3B0aW9ucyxcbiAgICAgIGV4Y2x1ZGVDaGFyYWN0ZXJzOiBvcHRpb25zLmV4Y2x1ZGVDaGFyYWN0ZXJzID8/IERFRkFVTFRfUEFTU1dPUkRfRVhDTFVERV9DSEFSUyxcbiAgICAgIG1hc3RlclNlY3JldDogdGhpcy5zZWNyZXQsXG4gICAgICBhcHBsaWNhdGlvbjogdGhpcy5tdWx0aVVzZXJSb3RhdGlvbkFwcGxpY2F0aW9uLFxuICAgICAgdnBjOiB0aGlzLnZwYyxcbiAgICAgIHZwY1N1Ym5ldHM6IHRoaXMudnBjU3VibmV0cyxcbiAgICAgIHRhcmdldDogdGhpcyxcbiAgICB9KTtcbiAgfVxuICBwcml2YXRlIHJlbmRlclNjYWxpbmdDb25maWd1cmF0aW9uKFxuICAgIG9wdGlvbnM6IGF3c19yZHMuU2VydmVybGVzc1NjYWxpbmdPcHRpb25zXG4gICk6IGF3c19yZHMuQ2ZuREJDbHVzdGVyLlNjYWxpbmdDb25maWd1cmF0aW9uUHJvcGVydHkge1xuICAgIGNvbnN0IG1pbkNhcGFjaXR5ID0gb3B0aW9ucy5taW5DYXBhY2l0eTtcbiAgICBjb25zdCBtYXhDYXBhY2l0eSA9IG9wdGlvbnMubWF4Q2FwYWNpdHk7XG5cbiAgICBpZiAobWluQ2FwYWNpdHkgJiYgbWF4Q2FwYWNpdHkgJiYgbWluQ2FwYWNpdHkgPiBtYXhDYXBhY2l0eSkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKFwiTWF4aW11bSBjYXBhY2l0eSBtdXN0IGJlIGdyZWF0ZXIgdGhhbiBvciBlcXVhbCB0byBtaW5pbXVtIGNhcGFjaXR5LlwiKTtcbiAgICB9XG5cbiAgICBjb25zdCBzZWNvbmRzVG9BdXRvUGF1c2UgPSBvcHRpb25zLmF1dG9QYXVzZT8udG9TZWNvbmRzKCk7XG4gICAgaWYgKHNlY29uZHNUb0F1dG9QYXVzZSAmJiAoc2Vjb25kc1RvQXV0b1BhdXNlIDwgMzAwIHx8IHNlY29uZHNUb0F1dG9QYXVzZSA+IDg2NDAwKSkge1xuICAgICAgdGhyb3cgbmV3IEVycm9yKFwiQXV0byBwYXVzZSB0aW1lIG11c3QgYmUgYmV0d2VlbiA1IG1pbnV0ZXMgYW5kIDEgZGF5LlwiKTtcbiAgICB9XG5cbiAgICByZXR1cm4ge1xuICAgICAgYXV0b1BhdXNlOiBzZWNvbmRzVG9BdXRvUGF1c2UgIT09IDAsXG4gICAgICBtaW5DYXBhY2l0eTogb3B0aW9ucy5taW5DYXBhY2l0eSxcbiAgICAgIG1heENhcGFjaXR5OiBvcHRpb25zLm1heENhcGFjaXR5LFxuICAgICAgc2Vjb25kc1VudGlsQXV0b1BhdXNlOiBzZWNvbmRzVG9BdXRvUGF1c2UgPT09IDAgPyB1bmRlZmluZWQgOiBzZWNvbmRzVG9BdXRvUGF1c2UsXG4gICAgfTtcbiAgfVxuXG4gIC8qKlxuICAgKiBUaGUgQVJOIG9mIHRoZSBjbHVzdGVyXG4gICAqL1xuICBwdWJsaWMgZ2V0IGNsdXN0ZXJBcm4oKTogc3RyaW5nIHtcbiAgICByZXR1cm4gU3RhY2sub2YodGhpcykuZm9ybWF0QXJuKHtcbiAgICAgIHNlcnZpY2U6IFwicmRzXCIsXG4gICAgICByZXNvdXJjZTogXCJjbHVzdGVyXCIsXG4gICAgICBhcm5Gb3JtYXQ6IEFybkZvcm1hdC5DT0xPTl9SRVNPVVJDRV9OQU1FLFxuICAgICAgcmVzb3VyY2VOYW1lOiB0aGlzLmNsdXN0ZXJJZGVudGlmaWVyLFxuICAgIH0pO1xuICB9XG5cbiAgLyoqXG4gICAqIEdyYW50IHRoZSBnaXZlbiBpZGVudGl0eSB0byBhY2Nlc3MgdG8gdGhlIERhdGEgQVBJLCBpbmNsdWRpbmcgcmVhZCBhY2Nlc3MgdG8gdGhlIHNlY3JldCBhdHRhY2hlZCB0byB0aGUgY2x1c3RlciBpZiBwcmVzZW50XG4gICAqXG4gICAqIEBwYXJhbSBncmFudGVlIFRoZSBwcmluY2lwYWwgdG8gZ3JhbnQgYWNjZXNzIHRvXG4gICAqL1xuICBwdWJsaWMgZ3JhbnREYXRhQXBpQWNjZXNzKGdyYW50ZWU6IGF3c19pYW0uSUdyYW50YWJsZSk6IGF3c19pYW0uR3JhbnQge1xuICAgIGlmICh0aGlzLmVuYWJsZURhdGFBcGkgPT09IGZhbHNlKSB7XG4gICAgICB0aHJvdyBuZXcgRXJyb3IoXCJDYW5ub3QgZ3JhbnQgRGF0YSBBUEkgYWNjZXNzIHdoZW4gdGhlIERhdGEgQVBJIGlzIGRpc2FibGVkXCIpO1xuICAgIH1cblxuICAgIHRoaXMuZW5hYmxlRGF0YUFwaSA9IHRydWU7XG4gICAgY29uc3QgcmV0ID0gYXdzX2lhbS5HcmFudC5hZGRUb1ByaW5jaXBhbCh7XG4gICAgICBncmFudGVlLFxuICAgICAgYWN0aW9uczogREFUQV9BUElfQUNUSU9OUyxcbiAgICAgIHJlc291cmNlQXJuczogW1wiKlwiXSxcbiAgICAgIHNjb3BlOiB0aGlzLFxuICAgIH0pO1xuICAgIHRoaXMuc2VjcmV0Py5ncmFudFJlYWQoZ3JhbnRlZSk7XG4gICAgcmV0dXJuIHJldDtcbiAgfVxuXG4gIC8qKlxuICAgKiBSZW5kZXJzIHRoZSBzZWNyZXQgYXR0YWNobWVudCB0YXJnZXQgc3BlY2lmaWNhdGlvbnMuXG4gICAqL1xuICBwdWJsaWMgYXNTZWNyZXRBdHRhY2htZW50VGFyZ2V0KCk6IGF3c19zZWNyZXRzbWFuYWdlci5TZWNyZXRBdHRhY2htZW50VGFyZ2V0UHJvcHMge1xuICAgIHJldHVybiB7XG4gICAgICB0YXJnZXRJZDogdGhpcy5jbHVzdGVySWRlbnRpZmllcixcbiAgICAgIHRhcmdldFR5cGU6IGF3c19zZWNyZXRzbWFuYWdlci5BdHRhY2htZW50VGFyZ2V0VHlwZS5SRFNfREJfQ0xVU1RFUixcbiAgICB9O1xuICB9XG59XG4iXX0=
```

##### package/package.json

###### Pretty-printed

 * *Similarity: 0.9722222222222222%*

 * *Differences: {"'version'": "'0.0.99'"}*

```diff
@@ -143,9 +143,9 @@
         "test:watch": "npx projen test:watch",
         "unbump": "npx projen unbump",
         "upgrade-projen": "npx projen upgrade-projen",
         "watch": "npx projen watch"
     },
     "stability": "deprecated",
     "types": "lib/index.d.ts",
-    "version": "0.0.98"
+    "version": "0.0.99"
 }
```

##### package/changelog.md

```diff
@@ -1,2 +1,2 @@
 
-### [0.0.98](https://github.com/pepperize/cdk-serverless-cluster-from-snapshot/compare/v0.0.97...v0.0.98) (2022-02-24)
+### [0.0.99](https://github.com/pepperize/cdk-serverless-cluster-from-snapshot/compare/v0.0.98...v0.0.99) (2022-02-24)
```

##### package/releasetag.txt

```diff
@@ -1 +1 @@
-v0.0.98
+v0.0.99
```

##### package/version.txt

```diff
@@ -1 +1 @@
-0.0.98
+0.0.99
```

