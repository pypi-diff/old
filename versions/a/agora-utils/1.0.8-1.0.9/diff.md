# Comparing `tmp/agora_utils-1.0.8-py2.py3-none-any.whl.zip` & `tmp/agora_utils-1.0.9-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,10 +1,10 @@
 Zip file size: 2445 bytes, number of entries: 8
 -rw-r--r--  2.0 fat       74 b- defN 23-Feb-13 15:17 agora_utils/__init__.py
 -rw-r--r--  2.0 fat       22 b- defN 23-Jan-23 16:40 agora_utils/_version.py
 -rw-r--r--  2.0 fat      486 b- defN 23-Feb-13 14:30 agora_utils/agora_time.py
--rw-r--r--  2.0 fat       24 b- defN 23-Mar-09 19:16 agora_utils/version.py
--rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agora_utils-1.0.8.dist-info/LICENSE
-?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_utils-1.0.8.dist-info/WHEEL
-?rw-r--r--  2.0 fat      719 b- defN 16-Jan-01 00:00 agora_utils-1.0.8.dist-info/METADATA
-?rw-r--r--  2.0 fat      622 b- defN 16-Jan-01 00:00 agora_utils-1.0.8.dist-info/RECORD
+-rw-r--r--  2.0 fat       24 b- defN 23-Mar-16 20:19 agora_utils/version.py
+-rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agora_utils-1.0.9.dist-info/LICENSE
+?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_utils-1.0.9.dist-info/WHEEL
+?rw-r--r--  2.0 fat      719 b- defN 16-Jan-01 00:00 agora_utils-1.0.9.dist-info/METADATA
+?rw-r--r--  2.0 fat      622 b- defN 16-Jan-01 00:00 agora_utils-1.0.9.dist-info/RECORD
 8 files, 2185 bytes uncompressed, 1353 bytes compressed:  38.1%
```

## zipnote {}

```diff
@@ -6,20 +6,20 @@
 
 Filename: agora_utils/agora_time.py
 Comment: 
 
 Filename: agora_utils/version.py
 Comment: 
 
-Filename: agora_utils-1.0.8.dist-info/LICENSE
+Filename: agora_utils-1.0.9.dist-info/LICENSE
 Comment: 
 
-Filename: agora_utils-1.0.8.dist-info/WHEEL
+Filename: agora_utils-1.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: agora_utils-1.0.8.dist-info/METADATA
+Filename: agora_utils-1.0.9.dist-info/METADATA
 Comment: 
 
-Filename: agora_utils-1.0.8.dist-info/RECORD
+Filename: agora_utils-1.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## agora_utils/version.py

```diff
@@ -1 +1 @@
-__version__ = '1.0.8'
+__version__ = '1.0.9'
```

## Comparing `agora_utils-1.0.8.dist-info/METADATA` & `agora_utils-1.0.9.dist-info/METADATA`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: agora_utils
-Version: 1.0.8
+Version: 1.0.9
 Summary: Utilities libraries for the Agora Edge Apps SDK 2.0 (Python)
 Author-email: AgoraIoT <agoraiot@slb.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: Apache Software License
 Project-URL: Home, https://agoraiot.github.io
```

## Comparing `agora_utils-1.0.8.dist-info/RECORD` & `agora_utils-1.0.9.dist-info/RECORD`

 * *Files 22% similar despite different names*

```diff
@@ -1,8 +1,8 @@
 agora_utils/__init__.py,sha256=yaeBDtk1bda23UFxgKCq1wZtP-VLTnww64aYcQJd0sU,74
 agora_utils/_version.py,sha256=acuR_XSJzp4OrQ5T8-Ac5gYe48mUwObuwjRmisFmZ7k,22
 agora_utils/agora_time.py,sha256=wzC_iUcx1GZtn5OJCkgQ3Ld7oyclak-7nyGjtLl5r2k,486
-agora_utils/version.py,sha256=HXG2Fim729WF9R0Op7tVdzk8ojlvSCoafD127Cl88T4,24
-agora_utils-1.0.8.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
-agora_utils-1.0.8.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
-agora_utils-1.0.8.dist-info/METADATA,sha256=AjNWGiI4qMvkDqYfJAmMi_LYajvmtkxcb1u8gKR2AgQ,719
-agora_utils-1.0.8.dist-info/RECORD,,
+agora_utils/version.py,sha256=-nHdmfbrEEZoCUg1nFNZBjmdzMhPwWALABnXcptli_o,24
+agora_utils-1.0.9.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
+agora_utils-1.0.9.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
+agora_utils-1.0.9.dist-info/METADATA,sha256=sIU1ZyAKyEkCi0mjwPFAV9pSwU8SCq9ZydfNC2cfckc,719
+agora_utils-1.0.9.dist-info/RECORD,,
```

