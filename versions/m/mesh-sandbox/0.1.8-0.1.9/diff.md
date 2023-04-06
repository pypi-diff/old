# Comparing `tmp/mesh_sandbox-0.1.8-py3-none-any.whl.zip` & `tmp/mesh_sandbox-0.1.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 63970 bytes, number of entries: 61
+Zip file size: 63971 bytes, number of entries: 61
 -rw-r--r--  2.0 unx       22 b- defN 80-Jan-01 00:00 mesh_sandbox/__init__.py
 -rw-r--r--  2.0 unx     3927 b- defN 80-Jan-01 00:00 mesh_sandbox/api.py
 -rw-r--r--  2.0 unx     3071 b- defN 80-Jan-01 00:00 mesh_sandbox/common/__init__.py
 -rw-r--r--  2.0 unx     6504 b- defN 80-Jan-01 00:00 mesh_sandbox/common/constants.py
 -rw-r--r--  2.0 unx     1481 b- defN 80-Jan-01 00:00 mesh_sandbox/common/exceptions.py
 -rw-r--r--  2.0 unx      551 b- defN 80-Jan-01 00:00 mesh_sandbox/common/fernet.py
 -rw-r--r--  2.0 unx      392 b- defN 80-Jan-01 00:00 mesh_sandbox/common/handler_helpers.py
@@ -52,12 +52,12 @@
 -rw-r--r--  2.0 unx      640 b- defN 80-Jan-01 00:00 mesh_sandbox/tests/serialisation.py
 -rw-r--r--  2.0 unx     1237 b- defN 80-Jan-01 00:00 mesh_sandbox/views/__init__.py
 -rw-r--r--  2.0 unx     3885 b- defN 80-Jan-01 00:00 mesh_sandbox/views/error.py
 -rw-r--r--  2.0 unx     5662 b- defN 80-Jan-01 00:00 mesh_sandbox/views/inbox.py
 -rw-r--r--  2.0 unx     2775 b- defN 80-Jan-01 00:00 mesh_sandbox/views/lookup.py
 -rw-r--r--  2.0 unx     4883 b- defN 80-Jan-01 00:00 mesh_sandbox/views/outbox.py
 -rw-r--r--  2.0 unx     8827 b- defN 80-Jan-01 00:00 mesh_sandbox/views/tracking.py
--rw-r--r--  2.0 unx     1051 b- defN 80-Jan-01 00:00 mesh_sandbox-0.1.8.dist-info/LICENSE
-?rw-r--r--  2.0 unx       88 b- defN 16-Jan-01 00:00 mesh_sandbox-0.1.8.dist-info/WHEEL
-?rw-r--r--  2.0 unx     2252 b- defN 16-Jan-01 00:00 mesh_sandbox-0.1.8.dist-info/METADATA
-?rw-r--r--  2.0 unx     5329 b- defN 16-Jan-01 00:00 mesh_sandbox-0.1.8.dist-info/RECORD
-61 files, 203537 bytes uncompressed, 55446 bytes compressed:  72.8%
+-rw-r--r--  2.0 unx     2240 b- defN 80-Jan-01 00:00 mesh_sandbox-0.1.9.dist-info/METADATA
+-rw-r--r--  2.0 unx       88 b- defN 80-Jan-01 00:00 mesh_sandbox-0.1.9.dist-info/WHEEL
+-rw-r--r--  2.0 unx     1051 b- defN 80-Jan-01 00:00 mesh_sandbox-0.1.9.dist-info/LICENSE
+?rw-r--r--  2.0 unx     5329 b- defN 16-Jan-01 00:00 mesh_sandbox-0.1.9.dist-info/RECORD
+61 files, 203525 bytes uncompressed, 55447 bytes compressed:  72.8%
```

## zipnote {}

```diff
@@ -165,20 +165,20 @@
 
 Filename: mesh_sandbox/views/outbox.py
 Comment: 
 
 Filename: mesh_sandbox/views/tracking.py
 Comment: 
 
-Filename: mesh_sandbox-0.1.8.dist-info/LICENSE
+Filename: mesh_sandbox-0.1.9.dist-info/METADATA
 Comment: 
 
-Filename: mesh_sandbox-0.1.8.dist-info/WHEEL
+Filename: mesh_sandbox-0.1.9.dist-info/WHEEL
 Comment: 
 
-Filename: mesh_sandbox-0.1.8.dist-info/METADATA
+Filename: mesh_sandbox-0.1.9.dist-info/LICENSE
 Comment: 
 
-Filename: mesh_sandbox-0.1.8.dist-info/RECORD
+Filename: mesh_sandbox-0.1.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## mesh_sandbox/__init__.py

```diff
@@ -1 +1 @@
-__version__ = "0.1.8"
+__version__ = "0.1.9"
```

## Comparing `mesh_sandbox-0.1.8.dist-info/LICENSE` & `mesh_sandbox-0.1.9.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `mesh_sandbox-0.1.8.dist-info/METADATA` & `mesh_sandbox-0.1.9.dist-info/METADATA`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mesh-sandbox
-Version: 0.1.8
+Version: 0.1.9
 Summary: NHSDigital mesh sandbox, a locally testable version of the MESH api
 License: MIT
 Author: spinecore
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
@@ -77,17 +77,17 @@
 Setup
 -----
 using asdf
 [install asdf](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf)
 
 get the required plugins
 ```bash
-adsf plugin install python
-adsf plugin install java
-adsf plugin install poetry
+asdf plugin add python
+asdf plugin add java
+asdf plugin add poetry
 ```
 
 install the tools
 ```bash
 cd <project_dir>
 asdf install
 ```
```

## Comparing `mesh_sandbox-0.1.8.dist-info/RECORD` & `mesh_sandbox-0.1.9.dist-info/RECORD`

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-mesh_sandbox/__init__.py,sha256=C69ADlbQREQlR15trneyA2sk8x0-oH4rDAX5fsv19_U,22
+mesh_sandbox/__init__.py,sha256=XIaxbMbyiP-L3kguR1GhxirFblTXiHR1lMfDVITvHUI,22
 mesh_sandbox/api.py,sha256=Aj_qE5eIXEmLCqvUJdAiuhONgGH_khnooH3JbAhNJoI,3927
 mesh_sandbox/common/__init__.py,sha256=B0eGgN6SGCvNIsalhQOXhFJvxZaE4wJS_ratFOMMwvI,3071
 mesh_sandbox/common/constants.py,sha256=_hnaHDkAQGHWLF7n_WfC5ZHIY5D-fUbOdpSqLusUMNY,6504
 mesh_sandbox/common/exceptions.py,sha256=YQII8w6DQQoKuW0cukEr6PIE9j0rwrqDpCn5lapgmkQ,1481
 mesh_sandbox/common/fernet.py,sha256=f8yygkVnK1cmQLBgcPifoB4PwGpgiOrG8Yk-6OMDy8o,551
 mesh_sandbox/common/handler_helpers.py,sha256=Eg00Tide2mL87EoMFw83fDuxiTL5DgIwxHs2RaJasgE,392
 mesh_sandbox/common/mex_headers.py,sha256=QG4yLmp4b4PyhjDhcKOuE0JJejBbJctmeQj9vXiQ9pE,6065
@@ -51,11 +51,11 @@
 mesh_sandbox/tests/serialisation.py,sha256=zCoP_fAaTCzZ68HpdKQVZLzUJGpbcHTYjHPM2uTtNWQ,640
 mesh_sandbox/views/__init__.py,sha256=nZkb6_1S8jz8Xl_AayfwjgEZG0JD2dfulfGxjJ5W9Ec,1237
 mesh_sandbox/views/error.py,sha256=9lnUr3P93Vm-nOrBTEuAD6nrSBUvpI6-XqXzILWjgGk,3885
 mesh_sandbox/views/inbox.py,sha256=gnaD9Csx5BqilVRefQQ_tXmeq80lwcLJfepW005GrkU,5662
 mesh_sandbox/views/lookup.py,sha256=HHUqZ-Iy22ysC3qaO8Bl5GBQqf_7IiBbe5acyxqS78M,2775
 mesh_sandbox/views/outbox.py,sha256=gd32ClmFn-_sROCBnsPos9SPrkTn9GpY1e4tQ_jWf1g,4883
 mesh_sandbox/views/tracking.py,sha256=UDEHd0DI_iCS5di8r134nh5lY0c9gClb7mdhXA5nMo4,8827
-mesh_sandbox-0.1.8.dist-info/LICENSE,sha256=usgzIvDUpVX5pYZepJTRXQJqIaz0mdd32GuS5a3PFlY,1051
-mesh_sandbox-0.1.8.dist-info/WHEEL,sha256=vxFmldFsRN_Hx10GDvsdv1wroKq8r5Lzvjp6GZ4OO8c,88
-mesh_sandbox-0.1.8.dist-info/METADATA,sha256=TLiLr5rQigPx-tMca87A2hR8Y5PsZ9z8uTba_wNlLCQ,2252
-mesh_sandbox-0.1.8.dist-info/RECORD,,
+mesh_sandbox-0.1.9.dist-info/METADATA,sha256=GlUonPrblasO-yXbNVL6JR6z9ywfngf-hIvnPcrT_zU,2240
+mesh_sandbox-0.1.9.dist-info/WHEEL,sha256=vVCvjcmxuUltf8cYhJ0sJMRDLr1XsPuxEId8YDzbyCY,88
+mesh_sandbox-0.1.9.dist-info/LICENSE,sha256=usgzIvDUpVX5pYZepJTRXQJqIaz0mdd32GuS5a3PFlY,1051
+mesh_sandbox-0.1.9.dist-info/RECORD,,
```

