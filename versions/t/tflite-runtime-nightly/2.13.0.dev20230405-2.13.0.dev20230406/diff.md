# Comparing `tmp/tflite_runtime_nightly-2.13.0.dev20230405-cp39-cp39-manylinux2014_x86_64.whl.zip` & `tmp/tflite_runtime_nightly-2.13.0.dev20230406-cp39-cp39-manylinux2014_x86_64.whl.zip`

## zipinfo {}

```diff
@@ -1,11 +1,11 @@
 Zip file size: 2546419 bytes, number of entries: 9
--rw-rw-r--  2.0 unx       80 b- defN 23-Apr-06 04:51 tflite_runtime/__init__.py
--rwxrwxr-x  2.0 unx  7379728 b- defN 23-Apr-06 04:53 tflite_runtime/_pywrap_tensorflow_interpreter_wrapper.so
--rw-rw-r--  2.0 unx    38775 b- defN 23-Apr-06 04:51 tflite_runtime/interpreter.py
--rw-rw-r--  2.0 unx     1542 b- defN 23-Apr-06 04:51 tflite_runtime/metrics_interface.py
--rw-rw-r--  2.0 unx     2048 b- defN 23-Apr-06 04:51 tflite_runtime/metrics_portable.py
--rw-rw-r--  2.0 unx     1440 b- defN 23-Apr-06 04:53 tflite_runtime_nightly-2.13.0.dev20230405.dist-info/METADATA
--rw-rw-r--  2.0 unx      111 b- defN 23-Apr-06 04:53 tflite_runtime_nightly-2.13.0.dev20230405.dist-info/WHEEL
--rw-rw-r--  2.0 unx       15 b- defN 23-Apr-06 04:53 tflite_runtime_nightly-2.13.0.dev20230405.dist-info/top_level.txt
--rw-rw-r--  2.0 unx      878 b- defN 23-Apr-06 04:53 tflite_runtime_nightly-2.13.0.dev20230405.dist-info/RECORD
+-rw-rw-r--  2.0 unx       80 b- defN 23-Apr-07 04:53 tflite_runtime/__init__.py
+-rwxrwxr-x  2.0 unx  7379728 b- defN 23-Apr-07 04:55 tflite_runtime/_pywrap_tensorflow_interpreter_wrapper.so
+-rw-rw-r--  2.0 unx    38775 b- defN 23-Apr-07 04:53 tflite_runtime/interpreter.py
+-rw-rw-r--  2.0 unx     1542 b- defN 23-Apr-07 04:53 tflite_runtime/metrics_interface.py
+-rw-rw-r--  2.0 unx     2048 b- defN 23-Apr-07 04:53 tflite_runtime/metrics_portable.py
+-rw-rw-r--  2.0 unx     1440 b- defN 23-Apr-07 04:55 tflite_runtime_nightly-2.13.0.dev20230406.dist-info/METADATA
+-rw-rw-r--  2.0 unx      111 b- defN 23-Apr-07 04:55 tflite_runtime_nightly-2.13.0.dev20230406.dist-info/WHEEL
+-rw-rw-r--  2.0 unx       15 b- defN 23-Apr-07 04:55 tflite_runtime_nightly-2.13.0.dev20230406.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx      878 b- defN 23-Apr-07 04:55 tflite_runtime_nightly-2.13.0.dev20230406.dist-info/RECORD
 9 files, 7424617 bytes uncompressed, 2544873 bytes compressed:  65.7%
```

## zipnote {}

```diff
@@ -9,20 +9,20 @@
 
 Filename: tflite_runtime/metrics_interface.py
 Comment: 
 
 Filename: tflite_runtime/metrics_portable.py
 Comment: 
 
-Filename: tflite_runtime_nightly-2.13.0.dev20230405.dist-info/METADATA
+Filename: tflite_runtime_nightly-2.13.0.dev20230406.dist-info/METADATA
 Comment: 
 
-Filename: tflite_runtime_nightly-2.13.0.dev20230405.dist-info/WHEEL
+Filename: tflite_runtime_nightly-2.13.0.dev20230406.dist-info/WHEEL
 Comment: 
 
-Filename: tflite_runtime_nightly-2.13.0.dev20230405.dist-info/top_level.txt
+Filename: tflite_runtime_nightly-2.13.0.dev20230406.dist-info/top_level.txt
 Comment: 
 
-Filename: tflite_runtime_nightly-2.13.0.dev20230405.dist-info/RECORD
+Filename: tflite_runtime_nightly-2.13.0.dev20230406.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## tflite_runtime/__init__.py

```diff
@@ -1,2 +1,2 @@
-__version__ = '2.13.0dev20230405'
-__git_version__ = '0.6.0-146003-g200d5840d88'
+__version__ = '2.13.0dev20230406'
+__git_version__ = '0.6.0-146048-g21dbbea0635'
```

## Comparing `tflite_runtime_nightly-2.13.0.dev20230405.dist-info/METADATA` & `tflite_runtime_nightly-2.13.0.dev20230406.dist-info/METADATA`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tflite-runtime-nightly
-Version: 2.13.0.dev20230405
+Version: 2.13.0.dev20230406
 Summary: TensorFlow Lite is for mobile and embedded devices.
 Home-page: https://www.tensorflow.org/lite/
 Author: Google, LLC
 Author-email: packages@tensorflow.org
 License: Apache 2.0
 Keywords: tflite tensorflow tensor machine learning
 Classifier: Development Status :: 5 - Production/Stable
```

## Comparing `tflite_runtime_nightly-2.13.0.dev20230405.dist-info/RECORD` & `tflite_runtime_nightly-2.13.0.dev20230406.dist-info/RECORD`

 * *Files 15% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-tflite_runtime/__init__.py,sha256=NB09vBeKDkHls7Di5tejb_E8M97OlqjKmSA84_MTB2U,80
+tflite_runtime/__init__.py,sha256=Dad1s1lcEtnzfC3QuxPRTxkHVKIkpbGVxkIXhEJb-1I,80
 tflite_runtime/_pywrap_tensorflow_interpreter_wrapper.so,sha256=fk_-x2JsOC4iUUWrxjktaJdYUyL2zCNKgBD1ZqRtBjs,7379728
 tflite_runtime/interpreter.py,sha256=WdMKqxuFdoGPyOKoCsZsHbvsVQXs_81OrG7VUE8p5JU,38775
 tflite_runtime/metrics_interface.py,sha256=dVu6SmbnQUntPgE5o6BxHVMyemwli-7F6tDfVMGrlYI,1542
 tflite_runtime/metrics_portable.py,sha256=YBiMNokP9JtoQaUcCRRY1T_iFSZGeWCjr6L0iUR6eY8,2048
-tflite_runtime_nightly-2.13.0.dev20230405.dist-info/METADATA,sha256=VSJ1EgKj0VptLegDFP94ejqPP5-RomJh8ItfFP5Zj5U,1440
-tflite_runtime_nightly-2.13.0.dev20230405.dist-info/WHEEL,sha256=IoSdNuZzCHbwOfmM81cEV5tUXku8iYpWuW3ThlGJK8I,111
-tflite_runtime_nightly-2.13.0.dev20230405.dist-info/top_level.txt,sha256=uNbSt_JkE5qb43UeqR4Wx6_Y6A5613g6gtS49welF08,15
-tflite_runtime_nightly-2.13.0.dev20230405.dist-info/RECORD,,
+tflite_runtime_nightly-2.13.0.dev20230406.dist-info/METADATA,sha256=cVTGBBRVP90MA7tMQu8nTt7EprBDcWFO7fhMgabfl6Q,1440
+tflite_runtime_nightly-2.13.0.dev20230406.dist-info/WHEEL,sha256=IoSdNuZzCHbwOfmM81cEV5tUXku8iYpWuW3ThlGJK8I,111
+tflite_runtime_nightly-2.13.0.dev20230406.dist-info/top_level.txt,sha256=uNbSt_JkE5qb43UeqR4Wx6_Y6A5613g6gtS49welF08,15
+tflite_runtime_nightly-2.13.0.dev20230406.dist-info/RECORD,,
```

