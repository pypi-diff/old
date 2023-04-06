# Comparing `tmp/drift_python_client-0.4.1-py3-none-any.whl.zip` & `tmp/drift_python_client-0.5.0-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,16 +1,16 @@
-Zip file size: 17692 bytes, number of entries: 14
--rw-r--r--  2.0 unx        6 b- defN 23-Feb-21 16:18 drift_client/VERSION
--rw-r--r--  2.0 unx      474 b- defN 23-Feb-21 16:18 drift_client/__init__.py
--rw-r--r--  2.0 unx    10664 b- defN 23-Feb-21 16:18 drift_client/drift_client.py
--rw-r--r--  2.0 unx     3419 b- defN 23-Feb-21 16:18 drift_client/drift_data_package.py
--rw-r--r--  2.0 unx      100 b- defN 23-Feb-21 16:18 drift_client/error.py
--rw-r--r--  2.0 unx     2644 b- defN 23-Feb-21 16:18 drift_client/influxdb_client.py
--rw-r--r--  2.0 unx     1828 b- defN 23-Feb-21 16:18 drift_client/minio_client.py
--rw-r--r--  2.0 unx     4047 b- defN 23-Feb-21 16:18 drift_client/mqtt_client.py
--rw-r--r--  2.0 unx     3307 b- defN 23-Feb-21 16:18 drift_client/reduct_client.py
--rw-r--r--  2.0 unx    16725 b- defN 23-Feb-21 16:18 drift_python_client-0.4.1.dist-info/LICENSE
--rw-r--r--  2.0 unx     3054 b- defN 23-Feb-21 16:18 drift_python_client-0.4.1.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 23-Feb-21 16:18 drift_python_client-0.4.1.dist-info/WHEEL
--rw-r--r--  2.0 unx       13 b- defN 23-Feb-21 16:18 drift_python_client-0.4.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1198 b- defN 23-Feb-21 16:18 drift_python_client-0.4.1.dist-info/RECORD
-14 files, 47571 bytes uncompressed, 15684 bytes compressed:  67.0%
+Zip file size: 17690 bytes, number of entries: 14
+-rw-r--r--  2.0 unx        6 b- defN 23-Apr-06 13:34 drift_client/VERSION
+-rw-r--r--  2.0 unx      474 b- defN 23-Apr-06 13:34 drift_client/__init__.py
+-rw-r--r--  2.0 unx    10664 b- defN 23-Apr-06 13:34 drift_client/drift_client.py
+-rw-r--r--  2.0 unx     3419 b- defN 23-Apr-06 13:34 drift_client/drift_data_package.py
+-rw-r--r--  2.0 unx      100 b- defN 23-Apr-06 13:34 drift_client/error.py
+-rw-r--r--  2.0 unx     2644 b- defN 23-Apr-06 13:34 drift_client/influxdb_client.py
+-rw-r--r--  2.0 unx     1828 b- defN 23-Apr-06 13:34 drift_client/minio_client.py
+-rw-r--r--  2.0 unx     4047 b- defN 23-Apr-06 13:34 drift_client/mqtt_client.py
+-rw-r--r--  2.0 unx     3307 b- defN 23-Apr-06 13:34 drift_client/reduct_client.py
+-rw-r--r--  2.0 unx    16725 b- defN 23-Apr-06 13:34 drift_python_client-0.5.0.dist-info/LICENSE
+-rw-r--r--  2.0 unx     3054 b- defN 23-Apr-06 13:34 drift_python_client-0.5.0.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 23-Apr-06 13:34 drift_python_client-0.5.0.dist-info/WHEEL
+-rw-r--r--  2.0 unx       13 b- defN 23-Apr-06 13:34 drift_python_client-0.5.0.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx     1198 b- defN 23-Apr-06 13:34 drift_python_client-0.5.0.dist-info/RECORD
+14 files, 47571 bytes uncompressed, 15682 bytes compressed:  67.0%
```

## zipnote {}

```diff
@@ -21,23 +21,23 @@
 
 Filename: drift_client/mqtt_client.py
 Comment: 
 
 Filename: drift_client/reduct_client.py
 Comment: 
 
-Filename: drift_python_client-0.4.1.dist-info/LICENSE
+Filename: drift_python_client-0.5.0.dist-info/LICENSE
 Comment: 
 
-Filename: drift_python_client-0.4.1.dist-info/METADATA
+Filename: drift_python_client-0.5.0.dist-info/METADATA
 Comment: 
 
-Filename: drift_python_client-0.4.1.dist-info/WHEEL
+Filename: drift_python_client-0.5.0.dist-info/WHEEL
 Comment: 
 
-Filename: drift_python_client-0.4.1.dist-info/top_level.txt
+Filename: drift_python_client-0.5.0.dist-info/top_level.txt
 Comment: 
 
-Filename: drift_python_client-0.4.1.dist-info/RECORD
+Filename: drift_python_client-0.5.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## drift_client/VERSION

```diff
@@ -1 +1 @@
-0.4.1
+0.5.0
```

## Comparing `drift_python_client-0.4.1.dist-info/LICENSE` & `drift_python_client-0.5.0.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `drift_python_client-0.4.1.dist-info/METADATA` & `drift_python_client-0.5.0.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 Metadata-Version: 2.1
 Name: drift-python-client
-Version: 0.4.1
+Version: 0.5.0
 Summary: Drift Python Client
 Home-page: https://github.com/panda-official/DriftPythonClient
 Author: PANDA, GmbH
 Author-email: info@panda.technology
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 License-File: LICENSE
 Requires-Dist: influxdb-client (==1.30.0)
 Requires-Dist: drift-protocol (<1.0,>=0.3.0)
-Requires-Dist: wavelet-buffer (<1.0,>=0.4.0)
+Requires-Dist: wavelet-buffer (<1.0,>=0.6.0)
 Requires-Dist: paho-mqtt (==1.6.1)
 Requires-Dist: numpy (==1.23.1)
 Requires-Dist: deprecation (==2.1.0)
 Requires-Dist: reduct-py (~=1.3)
 Requires-Dist: minio (==7.1.10)
 Provides-Extra: docs
 Requires-Dist: mkdocs (~=1.3) ; extra == 'docs'
```

## Comparing `drift_python_client-0.4.1.dist-info/RECORD` & `drift_python_client-0.5.0.dist-info/RECORD`

 * *Files 18% similar despite different names*

```diff
@@ -1,14 +1,14 @@
-drift_client/VERSION,sha256=9iGEzuh4fy9pQcggQaVyXU7cmqKT6-Xb9mRAboLsH-E,6
+drift_client/VERSION,sha256=oK1QZAE5pST4ZZEVcUW_HUZ06pwGW_6iFVjw97BEMMg,6
 drift_client/__init__.py,sha256=KwSDABVc-Qmyou53upDzz9SEtxspVQg3_pp0qR9f56E,474
 drift_client/drift_client.py,sha256=h1-kb0FNc1ctwY6UVkI_Khjul7EKlU0NpzZB0ywtcXk,10664
 drift_client/drift_data_package.py,sha256=-v8Wbhv7PU3WlpfWIAO6aVkhciD0Pox8onKOCBTrkL0,3419
 drift_client/error.py,sha256=VSSWHJiakIsRjtGx8sHyJ0nqS0uYavrc9TCFIuD7atA,100
 drift_client/influxdb_client.py,sha256=n_7rNPOI_h3r7Ry0uBgZV59ECDk2mSaJaW5lMhLYZDM,2644
 drift_client/minio_client.py,sha256=-l5ty2sam073B_tsLRwqM1e9TiTSahXX-2H_mjcX1jo,1828
 drift_client/mqtt_client.py,sha256=4-r4ZomTrw7YHqLZ6SU-PLmhxuw8CGqeMxzANFxz2wk,4047
 drift_client/reduct_client.py,sha256=bGkt6AO0gU-KADm0UjtTqjwN3mSeETCG7R7vM7X7Kk8,3307
-drift_python_client-0.4.1.dist-info/LICENSE,sha256=HyVuytGSiAUQ6ErWBHTqt1iSGHhLmlC8fO7jTCuR8dU,16725
-drift_python_client-0.4.1.dist-info/METADATA,sha256=Qn7oAqd9tc4gXusqQQ4B5GV4p-AQdHNlUro3VcUmCnU,3054
-drift_python_client-0.4.1.dist-info/WHEEL,sha256=2wepM1nk4DS4eFpYrW1TTqPcoGNfHhhO_i5m4cOimbo,92
-drift_python_client-0.4.1.dist-info/top_level.txt,sha256=g36GfF0WcMjKkwPW7zawUU5n5XsLJT-4oLxcVgeobno,13
-drift_python_client-0.4.1.dist-info/RECORD,,
+drift_python_client-0.5.0.dist-info/LICENSE,sha256=HyVuytGSiAUQ6ErWBHTqt1iSGHhLmlC8fO7jTCuR8dU,16725
+drift_python_client-0.5.0.dist-info/METADATA,sha256=BBizqeldbQAC8rqCrmdXceak3qSLLe4-Rv9W1spH8HM,3054
+drift_python_client-0.5.0.dist-info/WHEEL,sha256=pkctZYzUS4AYVn6dJ-7367OJZivF2e8RA9b_ZBjif18,92
+drift_python_client-0.5.0.dist-info/top_level.txt,sha256=g36GfF0WcMjKkwPW7zawUU5n5XsLJT-4oLxcVgeobno,13
+drift_python_client-0.5.0.dist-info/RECORD,,
```

