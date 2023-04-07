# Comparing `tmp/Geode_Conversion-4.4.6-cp39-cp39-win_amd64.whl.zip` & `tmp/Geode_Conversion-4.4.7-cp39-cp39-win_amd64.whl.zip`

## zipinfo {}

```diff
@@ -1,10 +1,10 @@
-Zip file size: 1209061 bytes, number of entries: 8
--rw-rw-rw-  2.0 fat  2395648 b- defN 23-Mar-31 05:07 geode_conversion/Geode-Conversion_model.dll
--rw-rw-rw-  2.0 fat       97 b- defN 23-Mar-31 05:06 geode_conversion/__init__.py
--rw-rw-rw-  2.0 fat   150528 b- defN 23-Mar-31 05:07 geode_conversion/geode_conversion_py_model.cp39-win_amd64.pyd
--rw-rw-rw-  2.0 fat      198 b- defN 23-Mar-31 05:06 geode_conversion/model.py
--rw-rw-rw-  2.0 fat     2038 b- defN 23-Mar-31 05:07 Geode_Conversion-4.4.6.dist-info/METADATA
--rw-rw-rw-  2.0 fat      100 b- defN 23-Mar-31 05:07 Geode_Conversion-4.4.6.dist-info/WHEEL
--rw-rw-rw-  2.0 fat       17 b- defN 23-Mar-31 05:07 Geode_Conversion-4.4.6.dist-info/top_level.txt
--rw-rw-r--  2.0 fat      722 b- defN 23-Mar-31 05:07 Geode_Conversion-4.4.6.dist-info/RECORD
-8 files, 2549348 bytes uncompressed, 1207789 bytes compressed:  52.6%
+Zip file size: 2839 bytes, number of entries: 8
+-rw-rw-rw-  2.0 fat       70 b- defN 23-Apr-07 12:40 geode_conversion/__init__.py
+-rw-rw-rw-  2.0 fat       85 b- defN 23-Apr-07 12:41 geode_conversion/geode_conversion.py
+-rw-rw-rw-  2.0 fat      197 b- defN 23-Apr-07 12:41 geode_conversion/geode_conversion_model.py
+-rw-rw-rw-  2.0 fat      198 b- defN 23-Apr-07 12:40 geode_conversion/model.py
+-rw-rw-rw-  2.0 fat     1952 b- defN 23-Apr-07 12:41 Geode_Conversion-4.4.7.dist-info/METADATA
+-rw-rw-rw-  2.0 fat      100 b- defN 23-Apr-07 12:41 Geode_Conversion-4.4.7.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat       17 b- defN 23-Apr-07 12:41 Geode_Conversion-4.4.7.dist-info/top_level.txt
+-rw-rw-r--  2.0 fat      688 b- defN 23-Apr-07 12:41 Geode_Conversion-4.4.7.dist-info/RECORD
+8 files, 3307 bytes uncompressed, 1619 bytes compressed:  51.0%
```

## zipnote {}

```diff
@@ -1,25 +1,25 @@
-Filename: geode_conversion/Geode-Conversion_model.dll
+Filename: geode_conversion/__init__.py
 Comment: 
 
-Filename: geode_conversion/__init__.py
+Filename: geode_conversion/geode_conversion.py
 Comment: 
 
-Filename: geode_conversion/geode_conversion_py_model.cp39-win_amd64.pyd
+Filename: geode_conversion/geode_conversion_model.py
 Comment: 
 
 Filename: geode_conversion/model.py
 Comment: 
 
-Filename: Geode_Conversion-4.4.6.dist-info/METADATA
+Filename: Geode_Conversion-4.4.7.dist-info/METADATA
 Comment: 
 
-Filename: Geode_Conversion-4.4.6.dist-info/WHEEL
+Filename: Geode_Conversion-4.4.7.dist-info/WHEEL
 Comment: 
 
-Filename: Geode_Conversion-4.4.6.dist-info/top_level.txt
+Filename: Geode_Conversion-4.4.7.dist-info/top_level.txt
 Comment: 
 
-Filename: Geode_Conversion-4.4.6.dist-info/RECORD
+Filename: Geode_Conversion-4.4.7.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## geode_conversion/__init__.py

```diff
@@ -1,5 +1,3 @@
-#
-# Copyright (c) 2019 - 2023 Geode-solutions. All rights reserved.
-#
+## Copyright (c) 2019 - 2023 Geode-solutions
 
 from .model import *
```

## Comparing `Geode_Conversion-4.4.6.dist-info/METADATA` & `Geode_Conversion-4.4.7.dist-info/METADATA`

 * *Files 12% similar despite different names*

```diff
@@ -1,19 +1,17 @@
 Metadata-Version: 2.1
 Name: Geode-Conversion
-Version: 4.4.6
+Version: 4.4.7
 Summary: Conversion module for Geode-solutions OpenGeode modules
 Home-page: https://github.com/Geode-solutions/Geode-Conversion
 Author: Geode-solutions
 Author-email: contact@geode-solutions.com
 License: Proprietary
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
-Requires-Dist: OpenGeode-core (==13.*,>=13.0.0)
-Requires-Dist: Geode-Common (==24.*,>=24.0.0)
 
 <h1 align="center">Geode-Conversion<sup><i>by Geode-solutions</i></sup></h1>
 <h3 align="center">Conversion OpenGeode module</h3>
 
 <p align="center">
   <img src="https://github.com/Geode-solutions/Geode-Conversion_private/workflows/CI/badge.svg" alt="Build Status">
   <img src="https://github.com/Geode-solutions/Geode-Conversion_private/workflows/CD/badge.svg" alt="Deploy Status">
@@ -27,14 +25,14 @@
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
@@ -1,12 +1,11 @@
-Metadata-Version: 2.1 Name: Geode-Conversion Version: 4.4.6 Summary: Conversion
+Metadata-Version: 2.1 Name: Geode-Conversion Version: 4.4.7 Summary: Conversion
 module for Geode-solutions OpenGeode modules Home-page: https://github.com/
 Geode-solutions/Geode-Conversion Author: Geode-solutions Author-email:
 contact@geode-solutions.com License: Proprietary Platform: UNKNOWN Description-
-Content-Type: text/markdown Requires-Dist: OpenGeode-core (==13.*,>=13.0.0)
-Requires-Dist: Geode-Common (==24.*,>=24.0.0)
+Content-Type: text/markdown
                ****** Geode-Conversionby Geode-solutions ******
                      **** Conversion OpenGeode module ****
           [Build Status] [Deploy Status] [Coverage Status] [Version]
              [Windows support] [Ubuntu support] [Red Hat support]
   [Language] [License] [Semantic-release] [Slack_invite] Copyright (c) 2019 -
                             2023, Geode-solutions
```

