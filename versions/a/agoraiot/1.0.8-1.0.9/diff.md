# Comparing `tmp/agoraiot-1.0.8-py2.py3-none-any.whl.zip` & `tmp/agoraiot-1.0.9-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 1969 bytes, number of entries: 6
+Zip file size: 1970 bytes, number of entries: 6
 -rw-r--r--  2.0 fat      304 b- defN 23-Feb-13 17:21 agoraiot/__init__.py
--rw-r--r--  2.0 fat       24 b- defN 23-Mar-09 19:16 agoraiot/version.py
--rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agoraiot-1.0.8.dist-info/LICENSE
-?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agoraiot-1.0.8.dist-info/WHEEL
-?rw-r--r--  2.0 fat      835 b- defN 16-Jan-01 00:00 agoraiot-1.0.8.dist-info/METADATA
-?rw-r--r--  2.0 fat      446 b- defN 16-Jan-01 00:00 agoraiot-1.0.8.dist-info/RECORD
-6 files, 1847 bytes uncompressed, 1161 bytes compressed:  37.1%
+-rw-r--r--  2.0 fat       24 b- defN 23-Mar-16 20:19 agoraiot/version.py
+-rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agoraiot-1.0.9.dist-info/LICENSE
+?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agoraiot-1.0.9.dist-info/WHEEL
+?rw-r--r--  2.0 fat      835 b- defN 16-Jan-01 00:00 agoraiot-1.0.9.dist-info/METADATA
+?rw-r--r--  2.0 fat      446 b- defN 16-Jan-01 00:00 agoraiot-1.0.9.dist-info/RECORD
+6 files, 1847 bytes uncompressed, 1162 bytes compressed:  37.1%
```

## zipnote {}

```diff
@@ -1,19 +1,19 @@
 Filename: agoraiot/__init__.py
 Comment: 
 
 Filename: agoraiot/version.py
 Comment: 
 
-Filename: agoraiot-1.0.8.dist-info/LICENSE
+Filename: agoraiot-1.0.9.dist-info/LICENSE
 Comment: 
 
-Filename: agoraiot-1.0.8.dist-info/WHEEL
+Filename: agoraiot-1.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: agoraiot-1.0.8.dist-info/METADATA
+Filename: agoraiot-1.0.9.dist-info/METADATA
 Comment: 
 
-Filename: agoraiot-1.0.8.dist-info/RECORD
+Filename: agoraiot-1.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## agoraiot/version.py

```diff
@@ -1 +1 @@
-__version__ = '1.0.8'
+__version__ = '1.0.9'
```

## Comparing `agoraiot-1.0.8.dist-info/METADATA` & `agoraiot-1.0.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: agoraiot
-Version: 1.0.8
+Version: 1.0.9
 Summary: AgoraIoT Python Libraries
 Author-email: AgoraIoT <agoraiot@slb.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Dist: agora_logging
 Requires-Dist: agora_busclient
 Requires-Dist: agora_config
```

