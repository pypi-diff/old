# Comparing `tmp/StackingNonlinearTransformations-0.0.3-py3.8.egg` & `tmp/StackingNonlinearTransformations-0.0.4-py3.8.egg`

## zipinfo {}

```diff
@@ -1,8 +1,9 @@
-Zip file size: 11279 bytes, number of entries: 6
--rw-rw-rw-  2.0 fat    56672 b- defN 23-Apr-07 12:54 EGG-INFO/PKG-INFO
--rw-rw-rw-  2.0 fat      287 b- defN 23-Apr-07 12:54 EGG-INFO/SOURCES.txt
--rw-rw-rw-  2.0 fat        1 b- defN 23-Apr-07 12:54 EGG-INFO/dependency_links.txt
--rw-rw-rw-  2.0 fat       39 b- defN 23-Apr-07 12:54 EGG-INFO/requires.txt
--rw-rw-rw-  2.0 fat        1 b- defN 23-Apr-07 12:54 EGG-INFO/top_level.txt
--rw-rw-rw-  2.0 fat        2 b- defN 23-Apr-07 12:54 EGG-INFO/zip-safe
-6 files, 57002 bytes uncompressed, 10549 bytes compressed:  81.5%
+Zip file size: 14106 bytes, number of entries: 7
+-rw-rw-rw-  2.0 fat    56762 b- defN 23-Apr-07 14:20 EGG-INFO/PKG-INFO
+-rw-rw-rw-  2.0 fat      277 b- defN 23-Apr-07 14:20 EGG-INFO/SOURCES.txt
+-rw-rw-rw-  2.0 fat        1 b- defN 23-Apr-07 14:20 EGG-INFO/dependency_links.txt
+-rw-rw-rw-  2.0 fat       33 b- defN 23-Apr-07 14:20 EGG-INFO/top_level.txt
+-rw-rw-rw-  2.0 fat        2 b- defN 23-Apr-07 14:20 EGG-INFO/zip-safe
+-rw-rw-rw-  2.0 fat     3463 b- defN 23-Apr-07 14:10 stackingnonlineartransformations/__init__.py
+-rw-rw-rw-  2.0 fat     2784 b- defN 23-Apr-07 14:20 stackingnonlineartransformations/__pycache__/__init__.cpython-38.pyc
+7 files, 63322 bytes uncompressed, 13118 bytes compressed:  79.3%
```

## zipnote «TEMP»/diffoscope_szqwok_i_003004/tmp2llzltf__.zip

```diff
@@ -3,17 +3,20 @@
 
 Filename: EGG-INFO/SOURCES.txt
 Comment: 
 
 Filename: EGG-INFO/dependency_links.txt
 Comment: 
 
-Filename: EGG-INFO/requires.txt
-Comment: 
-
 Filename: EGG-INFO/top_level.txt
 Comment: 
 
 Filename: EGG-INFO/zip-safe
 Comment: 
 
+Filename: stackingnonlineartransformations/__init__.py
+Comment: 
+
+Filename: stackingnonlineartransformations/__pycache__/__init__.cpython-38.pyc
+Comment: 
+
 Zip file comment:
```

## EGG-INFO/PKG-INFO

```diff
@@ -1,15 +1,16 @@
 Metadata-Version: 2.1
 Name: StackingNonlinearTransformations
-Version: 0.0.3
+Version: 0.0.4
 Summary: Stacking algorithm optimization 
 Home-page: https://gitee.com/caoxinyu123/prostate_cancer_related_research/blob/STN/StackingNonlinearTransformations.py
 Author: caoxinyu
 Author-email: 398424191@qqc.om
 License: UNKNOWN
+Keywords: python,windows,mac,linux
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 
@@ -959,9 +960,11 @@
      [2.41687444e-01 4.72064771e-01 2.86247785e-01]
      [8.28419375e-02 4.11308528e-01 5.05849534e-01]
      [4.40553422e-05 2.35332311e-05 9.99932411e-01]
      [2.78964612e-01 4.59652130e-01 2.61383258e-01]
      [2.97970311e-02 2.75009795e-02 9.42701989e-01]]
     0.85625
     
+# upload log
 
+0.0.4 更新正确的Class调用方法
```

## EGG-INFO/SOURCES.txt

```diff
@@ -1,6 +1,6 @@
 setup.py
 StackingNonlinearTransformations.egg-info/PKG-INFO
 StackingNonlinearTransformations.egg-info/SOURCES.txt
 StackingNonlinearTransformations.egg-info/dependency_links.txt
-StackingNonlinearTransformations.egg-info/requires.txt
-StackingNonlinearTransformations.egg-info/top_level.txt
+StackingNonlinearTransformations.egg-info/top_level.txt
+stackingnonlineartransformations/__init__.py
```

## EGG-INFO/top_level.txt

```diff
@@ -1 +1,3 @@
-00000000: 0a                                       .
+00000000: 7374 6163 6b69 6e67 6e6f 6e6c 696e 6561  stackingnonlinea
+00000010: 7274 7261 6e73 666f 726d 6174 696f 6e73  rtransformations
+00000020: 0a                                       .
```

