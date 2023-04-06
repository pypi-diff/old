# Comparing `tmp/neuronsphere-1.0.8-py3-none-any.whl.zip` & `tmp/neuronsphere-1.0.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
 Zip file size: 2480 bytes, number of entries: 6
--rw-rw-rw-  2.0 unx        0 b- defN 23-Feb-16 00:18 neuronsphere/__init__.py
--rw-rw-rw-  2.0 unx        0 b- defN 23-Feb-16 00:18 neuronsphere/neuronsphere.py
--rw-rw-rw-  2.0 unx     3413 b- defN 23-Feb-16 00:18 neuronsphere-1.0.8.dist-info/METADATA
--rw-rw-rw-  2.0 unx       92 b- defN 23-Feb-16 00:18 neuronsphere-1.0.8.dist-info/WHEEL
--rw-rw-rw-  2.0 unx       13 b- defN 23-Feb-16 00:18 neuronsphere-1.0.8.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      478 b- defN 23-Feb-16 00:18 neuronsphere-1.0.8.dist-info/RECORD
+-rw-rw-rw-  2.0 unx        0 b- defN 23-Feb-16 16:06 neuronsphere/__init__.py
+-rw-rw-rw-  2.0 unx        0 b- defN 23-Feb-16 16:06 neuronsphere/neuronsphere.py
+-rw-rw-rw-  2.0 unx     3413 b- defN 23-Feb-16 16:06 neuronsphere-1.0.9.dist-info/METADATA
+-rw-rw-rw-  2.0 unx       92 b- defN 23-Feb-16 16:06 neuronsphere-1.0.9.dist-info/WHEEL
+-rw-rw-rw-  2.0 unx       13 b- defN 23-Feb-16 16:06 neuronsphere-1.0.9.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx      478 b- defN 23-Feb-16 16:06 neuronsphere-1.0.9.dist-info/RECORD
 6 files, 3996 bytes uncompressed, 1602 bytes compressed:  59.9%
```

## zipnote {}

```diff
@@ -1,19 +1,19 @@
 Filename: neuronsphere/__init__.py
 Comment: 
 
 Filename: neuronsphere/neuronsphere.py
 Comment: 
 
-Filename: neuronsphere-1.0.8.dist-info/METADATA
+Filename: neuronsphere-1.0.9.dist-info/METADATA
 Comment: 
 
-Filename: neuronsphere-1.0.8.dist-info/WHEEL
+Filename: neuronsphere-1.0.9.dist-info/WHEEL
 Comment: 
 
-Filename: neuronsphere-1.0.8.dist-info/top_level.txt
+Filename: neuronsphere-1.0.9.dist-info/top_level.txt
 Comment: 
 
-Filename: neuronsphere-1.0.8.dist-info/RECORD
+Filename: neuronsphere-1.0.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `neuronsphere-1.0.8.dist-info/METADATA` & `neuronsphere-1.0.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: neuronsphere
-Version: 1.0.8
+Version: 1.0.9
 Summary: Python bundle for all public NeuronSphere components
 Home-page: UNKNOWN
 Author: Alex Burgoon
 Author-email: alex.burgoon@hmdlabs.io
 License: Apache 2.0
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
@@ -26,19 +26,19 @@
 Requires-Dist: deprecated (==1.2.13)
 Requires-Dist: distlib (==0.3.4)
 Requires-Dist: filelock (==3.6.0)
 Requires-Dist: gitdb (==4.0.9)
 Requires-Dist: gitpython (==3.1.30)
 Requires-Dist: google-auth (==2.9.1)
 Requires-Dist: hmd-cli-app (~=1.0.593)
-Requires-Dist: hmd-cli-configure (~=1.0.30)
+Requires-Dist: hmd-cli-configure (~=1.0.31)
 Requires-Dist: hmd-cli-mickey (~=1.0.41)
 Requires-Dist: hmd-cli-neuronsphere (~=0.1.78)
-Requires-Dist: hmd-cli-repo (~=0.2.84)
-Requires-Dist: hmd-cli-tools (~=1.0.221)
+Requires-Dist: hmd-cli-repo (~=0.2.85)
+Requires-Dist: hmd-cli-tools (~=1.0.222)
 Requires-Dist: identify (==2.4.11)
 Requires-Dist: idna (==3.3)
 Requires-Dist: jinja2 (==3.0.3)
 Requires-Dist: jinja2-time (==0.2.0)
 Requires-Dist: jmespath (==0.10.0)
 Requires-Dist: kubernetes (==24.2.0)
 Requires-Dist: markupsafe (==2.1.0)
```

