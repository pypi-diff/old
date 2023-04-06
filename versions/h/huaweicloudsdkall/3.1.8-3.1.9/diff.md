# Comparing `tmp/huaweicloudsdkall-3.1.8-py2.py3-none-any.whl.zip` & `tmp/huaweicloudsdkall-3.1.9-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 2741 bytes, number of entries: 6
--rw-------  2.0 unx        1 b- defN 22-Nov-03 08:27 huaweicloudsdkall/__init__.py
--rw-------  2.0 unx      604 b- defN 22-Nov-03 08:28 huaweicloudsdkall-3.1.8.dist-info/LICENSE
--rw-------  2.0 unx     6694 b- defN 22-Nov-03 08:28 huaweicloudsdkall-3.1.8.dist-info/METADATA
--rw-------  2.0 unx      110 b- defN 22-Nov-03 08:28 huaweicloudsdkall-3.1.8.dist-info/WHEEL
--rw-------  2.0 unx       18 b- defN 22-Nov-03 08:28 huaweicloudsdkall-3.1.8.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      519 b- defN 22-Nov-03 08:28 huaweicloudsdkall-3.1.8.dist-info/RECORD
-6 files, 7946 bytes uncompressed, 1787 bytes compressed:  77.5%
+Zip file size: 2744 bytes, number of entries: 6
+-rw-------  2.0 unx        1 b- defN 22-Nov-08 07:42 huaweicloudsdkall/__init__.py
+-rw-------  2.0 unx      604 b- defN 22-Nov-08 07:42 huaweicloudsdkall-3.1.9.dist-info/LICENSE
+-rw-------  2.0 unx     6694 b- defN 22-Nov-08 07:42 huaweicloudsdkall-3.1.9.dist-info/METADATA
+-rw-------  2.0 unx      110 b- defN 22-Nov-08 07:42 huaweicloudsdkall-3.1.9.dist-info/WHEEL
+-rw-------  2.0 unx       18 b- defN 22-Nov-08 07:42 huaweicloudsdkall-3.1.9.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx      519 b- defN 22-Nov-08 07:42 huaweicloudsdkall-3.1.9.dist-info/RECORD
+6 files, 7946 bytes uncompressed, 1790 bytes compressed:  77.5%
```

## zipnote {}

```diff
@@ -1,19 +1,19 @@
 Filename: huaweicloudsdkall/__init__.py
 Comment: 
 
-Filename: huaweicloudsdkall-3.1.8.dist-info/LICENSE
+Filename: huaweicloudsdkall-3.1.9.dist-info/LICENSE
 Comment: 
 
-Filename: huaweicloudsdkall-3.1.8.dist-info/METADATA
+Filename: huaweicloudsdkall-3.1.9.dist-info/METADATA
 Comment: 
 
-Filename: huaweicloudsdkall-3.1.8.dist-info/WHEEL
+Filename: huaweicloudsdkall-3.1.9.dist-info/WHEEL
 Comment: 
 
-Filename: huaweicloudsdkall-3.1.8.dist-info/top_level.txt
+Filename: huaweicloudsdkall-3.1.9.dist-info/top_level.txt
 Comment: 
 
-Filename: huaweicloudsdkall-3.1.8.dist-info/RECORD
+Filename: huaweicloudsdkall-3.1.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `huaweicloudsdkall-3.1.8.dist-info/LICENSE` & `huaweicloudsdkall-3.1.9.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `huaweicloudsdkall-3.1.8.dist-info/METADATA` & `huaweicloudsdkall-3.1.9.dist-info/METADATA`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: huaweicloudsdkall
-Version: 3.1.8
+Version: 3.1.9
 Summary: HuaweiCloud SDK Python All
 Home-page: https://github.com/huaweicloud/huaweicloud-sdk-python-v3
 Author: HuaweiCloud SDK
 Author-email: hwcloudsdk@huawei.com
 License: Apache LICENSE 2.0
 Keywords: huaweicloud,sdk,all
 Platform: any
@@ -19,133 +19,133 @@
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Software Development
 Requires-Python: >=2.7,!=3.0.*,!=3.1.*,!=3.2.*
 Description-Content-Type: text/markdown
 License-File: LICENSE
-Requires-Dist: huaweicloudsdkcore (==3.1.8)
-Requires-Dist: huaweicloudsdkantiddos (==3.1.8)
-Requires-Dist: huaweicloudsdkaom (==3.1.8)
-Requires-Dist: huaweicloudsdkapig (==3.1.8)
-Requires-Dist: huaweicloudsdkapm (==3.1.8)
-Requires-Dist: huaweicloudsdkas (==3.1.8)
-Requires-Dist: huaweicloudsdkbcs (==3.1.8)
-Requires-Dist: huaweicloudsdkbms (==3.1.8)
-Requires-Dist: huaweicloudsdkbss (==3.1.8)
-Requires-Dist: huaweicloudsdkbssintl (==3.1.8)
-Requires-Dist: huaweicloudsdkcae (==3.1.8)
-Requires-Dist: huaweicloudsdkcampusgo (==3.1.8)
-Requires-Dist: huaweicloudsdkcbh (==3.1.8)
-Requires-Dist: huaweicloudsdkcbr (==3.1.8)
-Requires-Dist: huaweicloudsdkcbs (==3.1.8)
-Requires-Dist: huaweicloudsdkcc (==3.1.8)
-Requires-Dist: huaweicloudsdkcce (==3.1.8)
-Requires-Dist: huaweicloudsdkccm (==3.1.8)
-Requires-Dist: huaweicloudsdkcdm (==3.1.8)
-Requires-Dist: huaweicloudsdkcdn (==3.1.8)
-Requires-Dist: huaweicloudsdkces (==3.1.8)
-Requires-Dist: huaweicloudsdkcgs (==3.1.8)
-Requires-Dist: huaweicloudsdkclassroom (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudartifact (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudbuild (==3.1.8)
-Requires-Dist: huaweicloudsdkclouddeploy (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudide (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudpipeline (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudrtc (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudtable (==3.1.8)
-Requires-Dist: huaweicloudsdkcloudtest (==3.1.8)
-Requires-Dist: huaweicloudsdkcodecheck (==3.1.8)
-Requires-Dist: huaweicloudsdkcodecraft (==3.1.8)
-Requires-Dist: huaweicloudsdkcodehub (==3.1.8)
-Requires-Dist: huaweicloudsdkcph (==3.1.8)
-Requires-Dist: huaweicloudsdkcpts (==3.1.8)
-Requires-Dist: huaweicloudsdkcse (==3.1.8)
-Requires-Dist: huaweicloudsdkcsms (==3.1.8)
-Requires-Dist: huaweicloudsdkcss (==3.1.8)
-Requires-Dist: huaweicloudsdkcts (==3.1.8)
-Requires-Dist: huaweicloudsdkdas (==3.1.8)
-Requires-Dist: huaweicloudsdkdbss (==3.1.8)
-Requires-Dist: huaweicloudsdkdcs (==3.1.8)
-Requires-Dist: huaweicloudsdkddm (==3.1.8)
-Requires-Dist: huaweicloudsdkdds (==3.1.8)
-Requires-Dist: huaweicloudsdkdeh (==3.1.8)
-Requires-Dist: huaweicloudsdkdevsecurity (==3.1.8)
-Requires-Dist: huaweicloudsdkdevstar (==3.1.8)
-Requires-Dist: huaweicloudsdkdgc (==3.1.8)
-Requires-Dist: huaweicloudsdkdli (==3.1.8)
-Requires-Dist: huaweicloudsdkdms (==3.1.8)
-Requires-Dist: huaweicloudsdkdns (==3.1.8)
-Requires-Dist: huaweicloudsdkdrs (==3.1.8)
-Requires-Dist: huaweicloudsdkdsc (==3.1.8)
-Requires-Dist: huaweicloudsdkdws (==3.1.8)
-Requires-Dist: huaweicloudsdkecs (==3.1.8)
-Requires-Dist: huaweicloudsdkeg (==3.1.8)
-Requires-Dist: huaweicloudsdkeihealth (==3.1.8)
-Requires-Dist: huaweicloudsdkeip (==3.1.8)
-Requires-Dist: huaweicloudsdkelb (==3.1.8)
-Requires-Dist: huaweicloudsdkeps (==3.1.8)
-Requires-Dist: huaweicloudsdker (==3.1.8)
-Requires-Dist: huaweicloudsdkevs (==3.1.8)
-Requires-Dist: huaweicloudsdkfrs (==3.1.8)
-Requires-Dist: huaweicloudsdkfunctiongraph (==3.1.8)
-Requires-Dist: huaweicloudsdkga (==3.1.8)
-Requires-Dist: huaweicloudsdkgaussdb (==3.1.8)
-Requires-Dist: huaweicloudsdkgaussdbfornosql (==3.1.8)
-Requires-Dist: huaweicloudsdkgaussdbforopengauss (==3.1.8)
-Requires-Dist: huaweicloudsdkges (==3.1.8)
-Requires-Dist: huaweicloudsdkgsl (==3.1.8)
-Requires-Dist: huaweicloudsdkhilens (==3.1.8)
-Requires-Dist: huaweicloudsdkhss (==3.1.8)
-Requires-Dist: huaweicloudsdkiam (==3.1.8)
-Requires-Dist: huaweicloudsdkiec (==3.1.8)
-Requires-Dist: huaweicloudsdkief (==3.1.8)
-Requires-Dist: huaweicloudsdkies (==3.1.8)
-Requires-Dist: huaweicloudsdkimage (==3.1.8)
-Requires-Dist: huaweicloudsdkimagesearch (==3.1.8)
-Requires-Dist: huaweicloudsdkims (==3.1.8)
-Requires-Dist: huaweicloudsdkiotanalytics (==3.1.8)
-Requires-Dist: huaweicloudsdkiotda (==3.1.8)
-Requires-Dist: huaweicloudsdkiotedge (==3.1.8)
-Requires-Dist: huaweicloudsdkivs (==3.1.8)
-Requires-Dist: huaweicloudsdkkafka (==3.1.8)
-Requires-Dist: huaweicloudsdkkms (==3.1.8)
-Requires-Dist: huaweicloudsdkkps (==3.1.8)
-Requires-Dist: huaweicloudsdklive (==3.1.8)
-Requires-Dist: huaweicloudsdklts (==3.1.8)
-Requires-Dist: huaweicloudsdkmeeting (==3.1.8)
-Requires-Dist: huaweicloudsdkmoderation (==3.1.8)
-Requires-Dist: huaweicloudsdkmpc (==3.1.8)
-Requires-Dist: huaweicloudsdkmrs (==3.1.8)
-Requires-Dist: huaweicloudsdknat (==3.1.8)
-Requires-Dist: huaweicloudsdknlp (==3.1.8)
-Requires-Dist: huaweicloudsdkocr (==3.1.8)
-Requires-Dist: huaweicloudsdkoms (==3.1.8)
-Requires-Dist: huaweicloudsdkosm (==3.1.8)
-Requires-Dist: huaweicloudsdkprojectman (==3.1.8)
-Requires-Dist: huaweicloudsdkrabbitmq (==3.1.8)
-Requires-Dist: huaweicloudsdkrds (==3.1.8)
-Requires-Dist: huaweicloudsdkres (==3.1.8)
-Requires-Dist: huaweicloudsdkrms (==3.1.8)
-Requires-Dist: huaweicloudsdkrocketmq (==3.1.8)
-Requires-Dist: huaweicloudsdkroma (==3.1.8)
-Requires-Dist: huaweicloudsdksa (==3.1.8)
-Requires-Dist: huaweicloudsdkscm (==3.1.8)
-Requires-Dist: huaweicloudsdksdrs (==3.1.8)
-Requires-Dist: huaweicloudsdkservicestage (==3.1.8)
-Requires-Dist: huaweicloudsdksfsturbo (==3.1.8)
-Requires-Dist: huaweicloudsdksis (==3.1.8)
-Requires-Dist: huaweicloudsdksmn (==3.1.8)
-Requires-Dist: huaweicloudsdksms (==3.1.8)
-Requires-Dist: huaweicloudsdkswr (==3.1.8)
-Requires-Dist: huaweicloudsdktms (==3.1.8)
-Requires-Dist: huaweicloudsdkugo (==3.1.8)
-Requires-Dist: huaweicloudsdkvas (==3.1.8)
-Requires-Dist: huaweicloudsdkvcm (==3.1.8)
-Requires-Dist: huaweicloudsdkvod (==3.1.8)
-Requires-Dist: huaweicloudsdkvpc (==3.1.8)
-Requires-Dist: huaweicloudsdkvpcep (==3.1.8)
-Requires-Dist: huaweicloudsdkvss (==3.1.8)
-Requires-Dist: huaweicloudsdkwaf (==3.1.8)
-Requires-Dist: huaweicloudsdkworkspace (==3.1.8)
+Requires-Dist: huaweicloudsdkcore (==3.1.9)
+Requires-Dist: huaweicloudsdkantiddos (==3.1.9)
+Requires-Dist: huaweicloudsdkaom (==3.1.9)
+Requires-Dist: huaweicloudsdkapig (==3.1.9)
+Requires-Dist: huaweicloudsdkapm (==3.1.9)
+Requires-Dist: huaweicloudsdkas (==3.1.9)
+Requires-Dist: huaweicloudsdkbcs (==3.1.9)
+Requires-Dist: huaweicloudsdkbms (==3.1.9)
+Requires-Dist: huaweicloudsdkbss (==3.1.9)
+Requires-Dist: huaweicloudsdkbssintl (==3.1.9)
+Requires-Dist: huaweicloudsdkcae (==3.1.9)
+Requires-Dist: huaweicloudsdkcampusgo (==3.1.9)
+Requires-Dist: huaweicloudsdkcbh (==3.1.9)
+Requires-Dist: huaweicloudsdkcbr (==3.1.9)
+Requires-Dist: huaweicloudsdkcbs (==3.1.9)
+Requires-Dist: huaweicloudsdkcc (==3.1.9)
+Requires-Dist: huaweicloudsdkcce (==3.1.9)
+Requires-Dist: huaweicloudsdkccm (==3.1.9)
+Requires-Dist: huaweicloudsdkcdm (==3.1.9)
+Requires-Dist: huaweicloudsdkcdn (==3.1.9)
+Requires-Dist: huaweicloudsdkces (==3.1.9)
+Requires-Dist: huaweicloudsdkcgs (==3.1.9)
+Requires-Dist: huaweicloudsdkclassroom (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudartifact (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudbuild (==3.1.9)
+Requires-Dist: huaweicloudsdkclouddeploy (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudide (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudpipeline (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudrtc (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudtable (==3.1.9)
+Requires-Dist: huaweicloudsdkcloudtest (==3.1.9)
+Requires-Dist: huaweicloudsdkcodecheck (==3.1.9)
+Requires-Dist: huaweicloudsdkcodecraft (==3.1.9)
+Requires-Dist: huaweicloudsdkcodehub (==3.1.9)
+Requires-Dist: huaweicloudsdkcph (==3.1.9)
+Requires-Dist: huaweicloudsdkcpts (==3.1.9)
+Requires-Dist: huaweicloudsdkcse (==3.1.9)
+Requires-Dist: huaweicloudsdkcsms (==3.1.9)
+Requires-Dist: huaweicloudsdkcss (==3.1.9)
+Requires-Dist: huaweicloudsdkcts (==3.1.9)
+Requires-Dist: huaweicloudsdkdas (==3.1.9)
+Requires-Dist: huaweicloudsdkdbss (==3.1.9)
+Requires-Dist: huaweicloudsdkdcs (==3.1.9)
+Requires-Dist: huaweicloudsdkddm (==3.1.9)
+Requires-Dist: huaweicloudsdkdds (==3.1.9)
+Requires-Dist: huaweicloudsdkdeh (==3.1.9)
+Requires-Dist: huaweicloudsdkdevsecurity (==3.1.9)
+Requires-Dist: huaweicloudsdkdevstar (==3.1.9)
+Requires-Dist: huaweicloudsdkdgc (==3.1.9)
+Requires-Dist: huaweicloudsdkdli (==3.1.9)
+Requires-Dist: huaweicloudsdkdms (==3.1.9)
+Requires-Dist: huaweicloudsdkdns (==3.1.9)
+Requires-Dist: huaweicloudsdkdrs (==3.1.9)
+Requires-Dist: huaweicloudsdkdsc (==3.1.9)
+Requires-Dist: huaweicloudsdkdws (==3.1.9)
+Requires-Dist: huaweicloudsdkecs (==3.1.9)
+Requires-Dist: huaweicloudsdkeg (==3.1.9)
+Requires-Dist: huaweicloudsdkeihealth (==3.1.9)
+Requires-Dist: huaweicloudsdkeip (==3.1.9)
+Requires-Dist: huaweicloudsdkelb (==3.1.9)
+Requires-Dist: huaweicloudsdkeps (==3.1.9)
+Requires-Dist: huaweicloudsdker (==3.1.9)
+Requires-Dist: huaweicloudsdkevs (==3.1.9)
+Requires-Dist: huaweicloudsdkfrs (==3.1.9)
+Requires-Dist: huaweicloudsdkfunctiongraph (==3.1.9)
+Requires-Dist: huaweicloudsdkga (==3.1.9)
+Requires-Dist: huaweicloudsdkgaussdb (==3.1.9)
+Requires-Dist: huaweicloudsdkgaussdbfornosql (==3.1.9)
+Requires-Dist: huaweicloudsdkgaussdbforopengauss (==3.1.9)
+Requires-Dist: huaweicloudsdkges (==3.1.9)
+Requires-Dist: huaweicloudsdkgsl (==3.1.9)
+Requires-Dist: huaweicloudsdkhilens (==3.1.9)
+Requires-Dist: huaweicloudsdkhss (==3.1.9)
+Requires-Dist: huaweicloudsdkiam (==3.1.9)
+Requires-Dist: huaweicloudsdkiec (==3.1.9)
+Requires-Dist: huaweicloudsdkief (==3.1.9)
+Requires-Dist: huaweicloudsdkies (==3.1.9)
+Requires-Dist: huaweicloudsdkimage (==3.1.9)
+Requires-Dist: huaweicloudsdkimagesearch (==3.1.9)
+Requires-Dist: huaweicloudsdkims (==3.1.9)
+Requires-Dist: huaweicloudsdkiotanalytics (==3.1.9)
+Requires-Dist: huaweicloudsdkiotda (==3.1.9)
+Requires-Dist: huaweicloudsdkiotedge (==3.1.9)
+Requires-Dist: huaweicloudsdkivs (==3.1.9)
+Requires-Dist: huaweicloudsdkkafka (==3.1.9)
+Requires-Dist: huaweicloudsdkkms (==3.1.9)
+Requires-Dist: huaweicloudsdkkps (==3.1.9)
+Requires-Dist: huaweicloudsdklive (==3.1.9)
+Requires-Dist: huaweicloudsdklts (==3.1.9)
+Requires-Dist: huaweicloudsdkmeeting (==3.1.9)
+Requires-Dist: huaweicloudsdkmoderation (==3.1.9)
+Requires-Dist: huaweicloudsdkmpc (==3.1.9)
+Requires-Dist: huaweicloudsdkmrs (==3.1.9)
+Requires-Dist: huaweicloudsdknat (==3.1.9)
+Requires-Dist: huaweicloudsdknlp (==3.1.9)
+Requires-Dist: huaweicloudsdkocr (==3.1.9)
+Requires-Dist: huaweicloudsdkoms (==3.1.9)
+Requires-Dist: huaweicloudsdkosm (==3.1.9)
+Requires-Dist: huaweicloudsdkprojectman (==3.1.9)
+Requires-Dist: huaweicloudsdkrabbitmq (==3.1.9)
+Requires-Dist: huaweicloudsdkrds (==3.1.9)
+Requires-Dist: huaweicloudsdkres (==3.1.9)
+Requires-Dist: huaweicloudsdkrms (==3.1.9)
+Requires-Dist: huaweicloudsdkrocketmq (==3.1.9)
+Requires-Dist: huaweicloudsdkroma (==3.1.9)
+Requires-Dist: huaweicloudsdksa (==3.1.9)
+Requires-Dist: huaweicloudsdkscm (==3.1.9)
+Requires-Dist: huaweicloudsdksdrs (==3.1.9)
+Requires-Dist: huaweicloudsdkservicestage (==3.1.9)
+Requires-Dist: huaweicloudsdksfsturbo (==3.1.9)
+Requires-Dist: huaweicloudsdksis (==3.1.9)
+Requires-Dist: huaweicloudsdksmn (==3.1.9)
+Requires-Dist: huaweicloudsdksms (==3.1.9)
+Requires-Dist: huaweicloudsdkswr (==3.1.9)
+Requires-Dist: huaweicloudsdktms (==3.1.9)
+Requires-Dist: huaweicloudsdkugo (==3.1.9)
+Requires-Dist: huaweicloudsdkvas (==3.1.9)
+Requires-Dist: huaweicloudsdkvcm (==3.1.9)
+Requires-Dist: huaweicloudsdkvod (==3.1.9)
+Requires-Dist: huaweicloudsdkvpc (==3.1.9)
+Requires-Dist: huaweicloudsdkvpcep (==3.1.9)
+Requires-Dist: huaweicloudsdkvss (==3.1.9)
+Requires-Dist: huaweicloudsdkwaf (==3.1.9)
+Requires-Dist: huaweicloudsdkworkspace (==3.1.9)
 
 See detailed information in [huaweicloud-sdk-python-v3](https://github.com/huaweicloud/huaweicloud-sdk-python-v3).
```

## Comparing `huaweicloudsdkall-3.1.8.dist-info/RECORD` & `huaweicloudsdkall-3.1.9.dist-info/RECORD`

 * *Files 22% similar despite different names*

```diff
@@ -1,6 +1,6 @@
 huaweicloudsdkall/__init__.py,sha256=AbpHGcgLb-kRsJGnwFEktk7uzpZOCcBY74-YBdrKVGs,1
-huaweicloudsdkall-3.1.8.dist-info/LICENSE,sha256=4_VSTLuxcsybRG9N4Isktlj1rAIBBsfl0Tjc0gBTijo,604
-huaweicloudsdkall-3.1.8.dist-info/METADATA,sha256=pA0uEm0nRRYXqyPgr8lO6Y8qAeeApyexmqPUNwqvogo,6694
-huaweicloudsdkall-3.1.8.dist-info/WHEEL,sha256=i6ErtKpGt3EuCna4OpOTBhgJrMWAh_eDBLj9VXrKHUE,110
-huaweicloudsdkall-3.1.8.dist-info/top_level.txt,sha256=3zNGA8EzECoGWbYN8v-8zOtqzLiVJeKnZWNEZUcZBS4,18
-huaweicloudsdkall-3.1.8.dist-info/RECORD,,
+huaweicloudsdkall-3.1.9.dist-info/LICENSE,sha256=4_VSTLuxcsybRG9N4Isktlj1rAIBBsfl0Tjc0gBTijo,604
+huaweicloudsdkall-3.1.9.dist-info/METADATA,sha256=Ku6iG6HscZ8eatIf4VbL8IM8idlhlVTcg4UZh04nQ0Q,6694
+huaweicloudsdkall-3.1.9.dist-info/WHEEL,sha256=80-DJ2LKJ1J1HZBp_8xaVylYn7Z7dOPLIAOHWs5d_ss,110
+huaweicloudsdkall-3.1.9.dist-info/top_level.txt,sha256=3zNGA8EzECoGWbYN8v-8zOtqzLiVJeKnZWNEZUcZBS4,18
+huaweicloudsdkall-3.1.9.dist-info/RECORD,,
```

