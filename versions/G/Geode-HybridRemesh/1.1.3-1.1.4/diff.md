# Comparing `tmp/Geode_HybridRemesh-1.1.3-cp39-cp39-win_amd64.whl.zip` & `tmp/Geode_HybridRemesh-1.1.4-cp39-cp39-win_amd64.whl.zip`

## zipinfo {}

```diff
@@ -1,9 +1,10 @@
-Zip file size: 1050352 bytes, number of entries: 7
--rw-rw-rw-  2.0 fat  2166784 b- defN 23-Mar-30 10:07 geode_hybridremesh/Geode-HybridRemesh_brep.dll
--rw-rw-rw-  2.0 fat       96 b- defN 23-Mar-30 10:06 geode_hybridremesh/__init__.py
--rw-rw-rw-  2.0 fat      200 b- defN 23-Mar-30 10:06 geode_hybridremesh/brep.py
--rw-rw-rw-  2.0 fat     2208 b- defN 23-Mar-30 10:07 Geode_HybridRemesh-1.1.3.dist-info/METADATA
--rw-rw-rw-  2.0 fat      100 b- defN 23-Mar-30 10:07 Geode_HybridRemesh-1.1.3.dist-info/WHEEL
--rw-rw-rw-  2.0 fat       19 b- defN 23-Mar-30 10:07 Geode_HybridRemesh-1.1.3.dist-info/top_level.txt
--rw-rw-r--  2.0 fat      616 b- defN 23-Mar-30 10:07 Geode_HybridRemesh-1.1.3.dist-info/RECORD
-7 files, 2170023 bytes uncompressed, 1049250 bytes compressed:  51.6%
+Zip file size: 2931 bytes, number of entries: 8
+-rw-rw-rw-  2.0 fat       69 b- defN 23-Apr-06 10:12 geode_hybridremesh/__init__.py
+-rw-rw-rw-  2.0 fat      200 b- defN 23-Apr-06 10:12 geode_hybridremesh/brep.py
+-rw-rw-rw-  2.0 fat       86 b- defN 23-Apr-06 10:12 geode_hybridremesh/geode_hybridremesh.py
+-rw-rw-rw-  2.0 fat      199 b- defN 23-Apr-06 10:12 geode_hybridremesh/geode_hybridremesh_brep.py
+-rw-rw-rw-  2.0 fat     2006 b- defN 23-Apr-06 10:12 Geode_HybridRemesh-1.1.4.dist-info/METADATA
+-rw-rw-rw-  2.0 fat      100 b- defN 23-Apr-06 10:12 Geode_HybridRemesh-1.1.4.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat       19 b- defN 23-Apr-06 10:12 Geode_HybridRemesh-1.1.4.dist-info/top_level.txt
+-rw-rw-r--  2.0 fat      706 b- defN 23-Apr-06 10:12 Geode_HybridRemesh-1.1.4.dist-info/RECORD
+8 files, 3385 bytes uncompressed, 1675 bytes compressed:  50.5%
```

## zipnote {}

```diff
@@ -1,22 +1,25 @@
-Filename: geode_hybridremesh/Geode-HybridRemesh_brep.dll
-Comment: 
-
 Filename: geode_hybridremesh/__init__.py
 Comment: 
 
 Filename: geode_hybridremesh/brep.py
 Comment: 
 
-Filename: Geode_HybridRemesh-1.1.3.dist-info/METADATA
+Filename: geode_hybridremesh/geode_hybridremesh.py
+Comment: 
+
+Filename: geode_hybridremesh/geode_hybridremesh_brep.py
+Comment: 
+
+Filename: Geode_HybridRemesh-1.1.4.dist-info/METADATA
 Comment: 
 
-Filename: Geode_HybridRemesh-1.1.3.dist-info/WHEEL
+Filename: Geode_HybridRemesh-1.1.4.dist-info/WHEEL
 Comment: 
 
-Filename: Geode_HybridRemesh-1.1.3.dist-info/top_level.txt
+Filename: Geode_HybridRemesh-1.1.4.dist-info/top_level.txt
 Comment: 
 
-Filename: Geode_HybridRemesh-1.1.3.dist-info/RECORD
+Filename: Geode_HybridRemesh-1.1.4.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## geode_hybridremesh/__init__.py

```diff
@@ -1,5 +1,3 @@
-#
-# Copyright (c) 2019 - 2023 Geode-solutions. All rights reserved.
-#
+## Copyright (c) 2019 - 2023 Geode-solutions
 
 from .brep import *
```

## Comparing `Geode_HybridRemesh-1.1.3.dist-info/METADATA` & `Geode_HybridRemesh-1.1.4.dist-info/METADATA`

 * *Files 14% similar despite different names*

```diff
@@ -1,21 +1,17 @@
 Metadata-Version: 2.1
 Name: Geode-HybridRemesh
-Version: 1.1.3
-Summary: Template for creating your own OpenGeode private module
-Home-page: https://github.com/Geode-solutions/Geode-ModuleTemplate
+Version: 1.1.4
+Summary: Hybrid remeshing Geode-solutions OpenGeode module
+Home-page: https://github.com/Geode-solutions/Geode-HybridRemesh
 Author: Geode-solutions
 Author-email: contact@geode-solutions.com
 License: Proprietary
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
-Requires-Dist: OpenGeode-core (==13.*,>=13.0.0)
-Requires-Dist: Geode-Common (==24.*,>=24.0.0)
-Requires-Dist: Geode-Parameterization (==1.*,>=1.16.0)
-Requires-Dist: Geode-SimplexRemesh (==5.*,>=5.2.0)
 
 <h1 align="center">Geode-ModuleTemplate_private<sup><i>by Geode-solutions</i></sup></h1>
 <h3 align="center">Template for creating your own OpenGeode private module</h3>
 
 <p align="center">
   <img src="https://github.com/Geode-solutions/Geode-ModuleTemplate_private/workflows/CI/badge.svg" alt="Build Status">
   <img src="https://github.com/Geode-solutions/Geode-ModuleTemplate_private/workflows/CD/badge.svg" alt="Deploy Status">
@@ -29,14 +25,14 @@
   <img src="https://img.shields.io/static/v1?label=Red%20Hat&logo=Red-Hat&logoColor=white&message=support&color=success" alt="Red Hat support">
 </p>
 
 <p align="center">
   <img src="https://img.shields.io/badge/C%2B%2B-11-blue.svg" alt="Language">
   <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License">
   <img src="https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg" alt="Semantic-release">
-  <a href="https://slackin-opengeode.herokuapp.com">
-    <img src="https://slackin-opengeode.herokuapp.com/badge.svg" alt="Slack invite">
+  <a href="https://opengeode-slack-invite.herokuapp.com">
+    <img src="https://opengeode-slack-invite.herokuapp.com/badge.svg" alt="Slack invite">
   </a>
 
 Copyright (c) 2019 - 2023, Geode-solutions
```

### html2text {}

```diff
@@ -1,14 +1,11 @@
-Metadata-Version: 2.1 Name: Geode-HybridRemesh Version: 1.1.3 Summary: Template
-for creating your own OpenGeode private module Home-page: https://github.com/
-Geode-solutions/Geode-ModuleTemplate Author: Geode-solutions Author-email:
+Metadata-Version: 2.1 Name: Geode-HybridRemesh Version: 1.1.4 Summary: Hybrid
+remeshing Geode-solutions OpenGeode module Home-page: https://github.com/Geode-
+solutions/Geode-HybridRemesh Author: Geode-solutions Author-email:
 contact@geode-solutions.com License: Proprietary Platform: UNKNOWN Description-
-Content-Type: text/markdown Requires-Dist: OpenGeode-core (==13.*,>=13.0.0)
-Requires-Dist: Geode-Common (==24.*,>=24.0.0) Requires-Dist: Geode-
-Parameterization (==1.*,>=1.16.0) Requires-Dist: Geode-SimplexRemesh
-(==5.*,>=5.2.0)
+Content-Type: text/markdown
          ****** Geode-ModuleTemplate_privateby Geode-solutions ******
        **** Template for creating your own OpenGeode private module ****
           [Build Status] [Deploy Status] [Coverage Status] [Version]
              [Windows support] [Ubuntu support] [Red Hat support]
   [Language] [License] [Semantic-release] [Slack_invite] Copyright (c) 2019 -
                             2023, Geode-solutions
```

