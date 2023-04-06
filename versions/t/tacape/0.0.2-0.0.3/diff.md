# Comparing `tmp/tacape-0.0.2-py3-none-any.whl.zip` & `tmp/tacape-0.0.3-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,19 +1,19 @@
-Zip file size: 11105 bytes, number of entries: 17
+Zip file size: 11112 bytes, number of entries: 17
 -rw-rw-r--  2.0 unx      232 b- defN 23-Apr-06 13:15 tacape/__init__.py
 -rw-rw-r--  2.0 unx      266 b- defN 23-Apr-06 13:15 tacape/logo.py
 -rw-rw-r--  2.0 unx     1729 b- defN 23-Apr-06 15:28 tacape/run_classifier.py
 -rw-rw-r--  2.0 unx     4485 b- defN 23-Apr-06 18:27 tacape/run_generator.py
 -rw-rw-r--  2.0 unx     3324 b- defN 23-Apr-06 18:29 tacape/train_classifier.py
 -rw-rw-r--  2.0 unx     3187 b- defN 23-Apr-06 15:44 tacape/train_generator.py
 -rw-rw-r--  2.0 unx       30 b- defN 23-Mar-30 15:33 tacape/models/__init__.py
 -rw-rw-r--  2.0 unx     1530 b- defN 23-Mar-30 15:24 tacape/models/layers.py
 -rw-rw-r--  2.0 unx     1167 b- defN 23-Apr-03 18:33 tacape/models/model.py
 -rw-rw-r--  2.0 unx       18 b- defN 23-Apr-03 17:27 tacape/utils/__init__.py
 -rw-rw-r--  2.0 unx      321 b- defN 23-Apr-03 17:27 tacape/utils/load.py
--rw-rw-r--  2.0 unx     1064 b- defN 23-Apr-06 18:34 tacape-0.0.2.dist-info/LICENSE
--rw-rw-r--  2.0 unx     7712 b- defN 23-Apr-06 18:34 tacape-0.0.2.dist-info/METADATA
--rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 18:34 tacape-0.0.2.dist-info/WHEEL
--rw-rw-r--  2.0 unx      215 b- defN 23-Apr-06 18:34 tacape-0.0.2.dist-info/entry_points.txt
--rw-rw-r--  2.0 unx        7 b- defN 23-Apr-06 18:34 tacape-0.0.2.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1339 b- defN 23-Apr-06 18:34 tacape-0.0.2.dist-info/RECORD
-17 files, 26718 bytes uncompressed, 8917 bytes compressed:  66.6%
+-rw-rw-r--  2.0 unx     1064 b- defN 23-Apr-06 18:37 tacape-0.0.3.dist-info/LICENSE
+-rw-rw-r--  2.0 unx     7750 b- defN 23-Apr-06 18:37 tacape-0.0.3.dist-info/METADATA
+-rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 18:37 tacape-0.0.3.dist-info/WHEEL
+-rw-rw-r--  2.0 unx      215 b- defN 23-Apr-06 18:37 tacape-0.0.3.dist-info/entry_points.txt
+-rw-rw-r--  2.0 unx        7 b- defN 23-Apr-06 18:37 tacape-0.0.3.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1339 b- defN 23-Apr-06 18:37 tacape-0.0.3.dist-info/RECORD
+17 files, 26756 bytes uncompressed, 8924 bytes compressed:  66.6%
```

## zipnote {}

```diff
@@ -27,26 +27,26 @@
 
 Filename: tacape/utils/__init__.py
 Comment: 
 
 Filename: tacape/utils/load.py
 Comment: 
 
-Filename: tacape-0.0.2.dist-info/LICENSE
+Filename: tacape-0.0.3.dist-info/LICENSE
 Comment: 
 
-Filename: tacape-0.0.2.dist-info/METADATA
+Filename: tacape-0.0.3.dist-info/METADATA
 Comment: 
 
-Filename: tacape-0.0.2.dist-info/WHEEL
+Filename: tacape-0.0.3.dist-info/WHEEL
 Comment: 
 
-Filename: tacape-0.0.2.dist-info/entry_points.txt
+Filename: tacape-0.0.3.dist-info/entry_points.txt
 Comment: 
 
-Filename: tacape-0.0.2.dist-info/top_level.txt
+Filename: tacape-0.0.3.dist-info/top_level.txt
 Comment: 
 
-Filename: tacape-0.0.2.dist-info/RECORD
+Filename: tacape-0.0.3.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `tacape-0.0.2.dist-info/LICENSE` & `tacape-0.0.3.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `tacape-0.0.2.dist-info/METADATA` & `tacape-0.0.3.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Metadata-Version: 2.1
 Name: tacape
-Version: 0.0.2
+Version: 0.0.3
 Summary: TACaPe: Transformed-based Anti-Cancer Peptide Classification and Generation
-Home-page: UNKNOWN
+Home-page: https://github.com/omixlab/anticancer-peptide
 Author: Isadora Leitzke Guidotti, Frederico Schmitt Kremer
 Author-email: fred.s.kremer@gmail.com
 License: UNKNOWN
 Keywords: bioinformatics machine-learning data science drug discovery QSAR
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

## Comparing `tacape-0.0.2.dist-info/RECORD` & `tacape-0.0.3.dist-info/RECORD`

 * *Files 10% similar despite different names*

```diff
@@ -5,13 +5,13 @@
 tacape/train_classifier.py,sha256=b10JcdBSpIS_1Iy750h0q6swwi96gWQTkmbA34eHh3A,3324
 tacape/train_generator.py,sha256=q5ACcATxD7ECfGQh1J4WXXrIAy4IzFHb1NYGdLBvf6U,3187
 tacape/models/__init__.py,sha256=B_zIwHcareHucr4JqgdnFAVvDfFijR__w-SsyunG2xw,30
 tacape/models/layers.py,sha256=xgp0RICRpUgrbn_18tsvaWkA_D_dZ8CLz43xRDggNCo,1530
 tacape/models/model.py,sha256=e8boh62n5oNWCIe2pawyiC5wYPqj7eWnaITujOwVZdY,1167
 tacape/utils/__init__.py,sha256=AQT2L8X2AdWB_Wk__JStBuwtUvfTGz8wTFcR94_81Zo,18
 tacape/utils/load.py,sha256=XknlskZOrjcd5Z5M9ER5yxzDLqhxiU5YAPp9s388JDg,321
-tacape-0.0.2.dist-info/LICENSE,sha256=lL6wJjUrwH3bCmb2msANo8SHV4OUCyoWfR9FeG-T4XU,1064
-tacape-0.0.2.dist-info/METADATA,sha256=MZGxi6J7Z0lZAKVV_CLYYO_2sdcnPyMjywegjb_98rw,7712
-tacape-0.0.2.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-tacape-0.0.2.dist-info/entry_points.txt,sha256=TfKUjYa52O20d8pXWYEm76xX5T7w0xm-V4d4pkUcSCc,215
-tacape-0.0.2.dist-info/top_level.txt,sha256=2LcJzKwy0vqun3FbnQSXQGlBqZdxGMypEu26pZtvWQ0,7
-tacape-0.0.2.dist-info/RECORD,,
+tacape-0.0.3.dist-info/LICENSE,sha256=lL6wJjUrwH3bCmb2msANo8SHV4OUCyoWfR9FeG-T4XU,1064
+tacape-0.0.3.dist-info/METADATA,sha256=_gOmXLu-Rfepz_DEpFqi9dXHjkJl95DZj3xSvld0Pq4,7750
+tacape-0.0.3.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+tacape-0.0.3.dist-info/entry_points.txt,sha256=TfKUjYa52O20d8pXWYEm76xX5T7w0xm-V4d4pkUcSCc,215
+tacape-0.0.3.dist-info/top_level.txt,sha256=2LcJzKwy0vqun3FbnQSXQGlBqZdxGMypEu26pZtvWQ0,7
+tacape-0.0.3.dist-info/RECORD,,
```

