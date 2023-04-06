# Comparing `tmp/agora_logging-1.0.8-py2.py3-none-any.whl.zip` & `tmp/agora_logging-1.0.9-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,14 +1,14 @@
-Zip file size: 6489 bytes, number of entries: 12
+Zip file size: 6488 bytes, number of entries: 12
 -rw-r--r--  2.0 fat       67 b- defN 23-Feb-13 16:55 agora_logging/__init__.py
 -rw-r--r--  2.0 fat     5933 b- defN 23-Jan-31 08:54 agora_logging/agora_logger.py
 -rw-r--r--  2.0 fat     1618 b- defN 23-Feb-07 13:03 agora_logging/colored_text.py
 -rw-r--r--  2.0 fat      993 b- defN 22-Dec-07 13:53 agora_logging/log_level.py
--rw-r--r--  2.0 fat       24 b- defN 23-Mar-09 19:16 agora_logging/version.py
+-rw-r--r--  2.0 fat       24 b- defN 23-Mar-16 20:19 agora_logging/version.py
 -rw-r--r--  2.0 fat        0 b- defN 23-Jan-23 15:58 agora_logging/handlers/__init__.py
 -rw-r--r--  2.0 fat     2824 b- defN 23-Feb-07 12:33 agora_logging/handlers/base_handler.py
 -rw-r--r--  2.0 fat      895 b- defN 23-Jan-25 14:34 agora_logging/handlers/stream_handler.py
--rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agora_logging-1.0.8.dist-info/LICENSE
-?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_logging-1.0.8.dist-info/WHEEL
-?rw-r--r--  2.0 fat      718 b- defN 16-Jan-01 00:00 agora_logging-1.0.8.dist-info/METADATA
-?rw-r--r--  2.0 fat     1008 b- defN 16-Jan-01 00:00 agora_logging-1.0.8.dist-info/RECORD
-12 files, 14318 bytes uncompressed, 4773 bytes compressed:  66.7%
+-rw-r--r--  2.0 fat      139 b- defN 23-Mar-07 09:10 agora_logging-1.0.9.dist-info/LICENSE
+?rw-r--r--  2.0 fat       99 b- defN 16-Jan-01 00:00 agora_logging-1.0.9.dist-info/WHEEL
+?rw-r--r--  2.0 fat      718 b- defN 16-Jan-01 00:00 agora_logging-1.0.9.dist-info/METADATA
+?rw-r--r--  2.0 fat     1008 b- defN 16-Jan-01 00:00 agora_logging-1.0.9.dist-info/RECORD
+12 files, 14318 bytes uncompressed, 4772 bytes compressed:  66.7%
```

## zipnote {}

```diff
@@ -18,20 +18,20 @@
 
 Filename: agora_logging/handlers/base_handler.py
 Comment: 
 
 Filename: agora_logging/handlers/stream_handler.py
 Comment: 
 
-Filename: agora_logging-1.0.8.dist-info/LICENSE
+Filename: agora_logging-1.0.9.dist-info/LICENSE
 Comment: 
 
-Filename: agora_logging-1.0.8.dist-info/WHEEL
+Filename: agora_logging-1.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: agora_logging-1.0.8.dist-info/METADATA
+Filename: agora_logging-1.0.9.dist-info/METADATA
 Comment: 
 
-Filename: agora_logging-1.0.8.dist-info/RECORD
+Filename: agora_logging-1.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## agora_logging/version.py

```diff
@@ -1 +1 @@
-__version__ = '1.0.8'
+__version__ = '1.0.9'
```

## Comparing `agora_logging-1.0.8.dist-info/METADATA` & `agora_logging-1.0.9.dist-info/METADATA`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: agora_logging
-Version: 1.0.8
+Version: 1.0.9
 Summary: Logging libraries for the Agora Edge Apps SDK 2.0 (Python)
 Author-email: AgoraIoT <agoraiot@slb.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: Apache Software License
 Project-URL: Home, https://agoraiot.github.io
```

## Comparing `agora_logging-1.0.8.dist-info/RECORD` & `agora_logging-1.0.9.dist-info/RECORD`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 agora_logging/__init__.py,sha256=PPi6BVmhWVjdeOMQYg-FEj51McSHrNif9p05X9otteo,67
 agora_logging/agora_logger.py,sha256=lpTlV7nZia8G_0jU4xGkJ6pA1cdrd6ve1K_jcNAaV0o,5933
 agora_logging/colored_text.py,sha256=b2sPEecFHco5Nye5EmqUK3sOJqVUBtwPADf9-rlZQD8,1618
 agora_logging/log_level.py,sha256=sNp1II2mLhfRoWyVOrXGbraoJJujY245xLzAgtRRImY,993
-agora_logging/version.py,sha256=HXG2Fim729WF9R0Op7tVdzk8ojlvSCoafD127Cl88T4,24
+agora_logging/version.py,sha256=-nHdmfbrEEZoCUg1nFNZBjmdzMhPwWALABnXcptli_o,24
 agora_logging/handlers/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 agora_logging/handlers/base_handler.py,sha256=rEfP6S3PZL8TsYX1qISy5kCYHQpS3Le9toV2itWQqzc,2824
 agora_logging/handlers/stream_handler.py,sha256=jX4zNGMHlHgSiXuq8-1MZ_Nx2-2q6xp_vtO23OPrELE,895
-agora_logging-1.0.8.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
-agora_logging-1.0.8.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
-agora_logging-1.0.8.dist-info/METADATA,sha256=oZXMlhFYhFKZnmvh0d9IO0SiUvDibCGdfYz_D32lPk4,718
-agora_logging-1.0.8.dist-info/RECORD,,
+agora_logging-1.0.9.dist-info/LICENSE,sha256=0FV-B2w7SRxv5WB_RriZppfctNE6t4pLFm_BUw2Ajcw,139
+agora_logging-1.0.9.dist-info/WHEEL,sha256=kdeDBNPvBI0w3meLKPoGgAnEr54n1jzrZWUoaLmGzVY,99
+agora_logging-1.0.9.dist-info/METADATA,sha256=YbviV0LLcTU1aFGVolNGRv4A6LRmcDQNEwQZmrPKSaI,718
+agora_logging-1.0.9.dist-info/RECORD,,
```

