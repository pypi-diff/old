# Comparing `tmp/delierium-0.9.0.dev5-py3-none-any.whl.zip` & `tmp/delierium-0.9.0.dev6-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,11 +1,11 @@
-Zip file size: 15455 bytes, number of entries: 9
+Zip file size: 15456 bytes, number of entries: 9
 -rw-rw-r--  2.0 unx     6136 b- defN 23-Apr-05 11:00 delierium/DerivativeOperators.py
 -rw-rw-r--  2.0 unx    13186 b- defN 23-Apr-06 17:30 delierium/Infinitesimals.py
 -rw-rw-r--  2.0 unx      538 b- defN 23-Apr-05 13:25 delierium/__init__.py
 -rw-rw-r--  2.0 unx    15332 b- defN 23-Apr-05 11:00 delierium/helpers.py
--rw-rw-r--  2.0 unx     1065 b- defN 23-Apr-06 17:31 delierium-0.9.0.dev5.dist-info/LICENSE
--rw-rw-r--  2.0 unx     4504 b- defN 23-Apr-06 17:31 delierium-0.9.0.dev5.dist-info/METADATA
--rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 17:31 delierium-0.9.0.dev5.dist-info/WHEEL
--rw-rw-r--  2.0 unx       16 b- defN 23-Apr-06 17:31 delierium-0.9.0.dev5.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      750 b- defN 23-Apr-06 17:31 delierium-0.9.0.dev5.dist-info/RECORD
-9 files, 41619 bytes uncompressed, 14161 bytes compressed:  66.0%
+-rw-rw-r--  2.0 unx     1065 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/LICENSE
+-rw-rw-r--  2.0 unx     4504 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/METADATA
+-rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/WHEEL
+-rw-rw-r--  2.0 unx       16 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx      750 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/RECORD
+9 files, 41619 bytes uncompressed, 14162 bytes compressed:  66.0%
```

## zipnote {}

```diff
@@ -6,23 +6,23 @@
 
 Filename: delierium/__init__.py
 Comment: 
 
 Filename: delierium/helpers.py
 Comment: 
 
-Filename: delierium-0.9.0.dev5.dist-info/LICENSE
+Filename: delierium-0.9.0.dev6.dist-info/LICENSE
 Comment: 
 
-Filename: delierium-0.9.0.dev5.dist-info/METADATA
+Filename: delierium-0.9.0.dev6.dist-info/METADATA
 Comment: 
 
-Filename: delierium-0.9.0.dev5.dist-info/WHEEL
+Filename: delierium-0.9.0.dev6.dist-info/WHEEL
 Comment: 
 
-Filename: delierium-0.9.0.dev5.dist-info/top_level.txt
+Filename: delierium-0.9.0.dev6.dist-info/top_level.txt
 Comment: 
 
-Filename: delierium-0.9.0.dev5.dist-info/RECORD
+Filename: delierium-0.9.0.dev6.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `delierium-0.9.0.dev5.dist-info/LICENSE` & `delierium-0.9.0.dev6.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `delierium-0.9.0.dev5.dist-info/METADATA` & `delierium-0.9.0.dev6.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: delierium
-Version: 0.9.0.dev5
+Version: 0.9.0.dev6
 Summary: Symmetry Analysis for ODEs/PDEs using SageMath
 Home-page: UNKNOWN
 Author: Martin Mayerhofer-Schöpf
 Author-email: tapir@aon.at
 License: MIT
 Project-URL: Source, https://github.com/tapir442/delierium
 Keywords: ODE PDE Lie Symmetry
```

## Comparing `delierium-0.9.0.dev5.dist-info/RECORD` & `delierium-0.9.0.dev6.dist-info/RECORD`

 * *Files 18% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 delierium/DerivativeOperators.py,sha256=XxKIkum-7bXdlMTqnhDeysjaKKeV_7OR-DDqEdo4NnQ,6136
 delierium/Infinitesimals.py,sha256=eevvunPuVF5OMN-HnTOmMwd_OPq2DFraleqZvWMslQQ,13186
 delierium/__init__.py,sha256=L3MQwe09Vc6HW5X5NINVtM2MUqS2bAO84Y5Vse0bCdo,538
 delierium/helpers.py,sha256=zRTx7S-s50gBLmYqmNEGPtihRSkOd0IPqk61DVIUWXo,15332
-delierium-0.9.0.dev5.dist-info/LICENSE,sha256=ZcfIKbSmoFLTRZMbjWIpVYj_ZEN8BuULitryeWVU6sY,1065
-delierium-0.9.0.dev5.dist-info/METADATA,sha256=NlZosBLtUkY5uXct3q7dUGN4pulqLgklFNk4BaLf0wY,4504
-delierium-0.9.0.dev5.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-delierium-0.9.0.dev5.dist-info/top_level.txt,sha256=8DqLv98rXmQHRO0RT49fWKTYUwiQgsOlqlPAMepy6lA,16
-delierium-0.9.0.dev5.dist-info/RECORD,,
+delierium-0.9.0.dev6.dist-info/LICENSE,sha256=ZcfIKbSmoFLTRZMbjWIpVYj_ZEN8BuULitryeWVU6sY,1065
+delierium-0.9.0.dev6.dist-info/METADATA,sha256=dyndW_9QH-2n_apolrLw4HYrcmGjWPhZ8CqaBLzG9Zs,4504
+delierium-0.9.0.dev6.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+delierium-0.9.0.dev6.dist-info/top_level.txt,sha256=8DqLv98rXmQHRO0RT49fWKTYUwiQgsOlqlPAMepy6lA,16
+delierium-0.9.0.dev6.dist-info/RECORD,,
```

