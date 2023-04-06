# Comparing `tmp/tb_nightly-2.9.0a20220501-py3-none-any.whl.zip` & `tmp/tb_nightly-2.9.0a20220502-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,8 +1,8 @@
-Zip file size: 5797806 bytes, number of entries: 296
+Zip file size: 5797805 bytes, number of entries: 296
 -rw-r--r--  2.0 unx     4125 b- defN 20-Jan-01 00:00 tensorboard/__init__.py
 -rw-r--r--  2.0 unx     1360 b- defN 20-Jan-01 00:00 tensorboard/assets.py
 -rw-r--r--  2.0 unx     3776 b- defN 20-Jan-01 00:00 tensorboard/auth.py
 -rw-r--r--  2.0 unx     3849 b- defN 20-Jan-01 00:00 tensorboard/context.py
 -rw-r--r--  2.0 unx     6456 b- defN 20-Jan-01 00:00 tensorboard/data_compat.py
 -rw-r--r--  2.0 unx     8610 b- defN 20-Jan-01 00:00 tensorboard/dataclass_compat.py
 -rw-r--r--  2.0 unx     4891 b- defN 20-Jan-01 00:00 tensorboard/default.py
@@ -285,14 +285,14 @@
 -rw-r--r--  2.0 unx      792 b- defN 20-Jan-01 00:00 tensorboard/util/io_util.py
 -rw-r--r--  2.0 unx     4492 b- defN 20-Jan-01 00:00 tensorboard/util/lazy_tensor_creator.py
 -rw-r--r--  2.0 unx     3827 b- defN 20-Jan-01 00:00 tensorboard/util/op_evaluator.py
 -rw-r--r--  2.0 unx      798 b- defN 20-Jan-01 00:00 tensorboard/util/platform_util.py
 -rw-r--r--  2.0 unx      781 b- defN 20-Jan-01 00:00 tensorboard/util/tb_logging.py
 -rw-r--r--  2.0 unx    21802 b- defN 20-Jan-01 00:00 tensorboard/util/tensor_util.py
 -rw-r--r--  2.0 unx     3734 b- defN 20-Jan-01 00:00 tensorboard/util/timing.py
--rw-r--r--  2.0 unx    29236 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220501.dist-info/LICENSE
--rw-r--r--  2.0 unx     1873 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220501.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220501.dist-info/WHEEL
--rw-r--r--  2.0 unx      156 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220501.dist-info/entry_points.txt
--rw-r--r--  2.0 unx       12 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220501.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx    29076 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220501.dist-info/RECORD
-296 files, 10017296 bytes uncompressed, 5750746 bytes compressed:  42.6%
+-rw-r--r--  2.0 unx    29236 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220502.dist-info/LICENSE
+-rw-r--r--  2.0 unx     1873 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220502.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220502.dist-info/WHEEL
+-rw-r--r--  2.0 unx      156 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220502.dist-info/entry_points.txt
+-rw-r--r--  2.0 unx       12 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220502.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx    29076 b- defN 20-Jan-01 00:00 tb_nightly-2.9.0a20220502.dist-info/RECORD
+296 files, 10017296 bytes uncompressed, 5750745 bytes compressed:  42.6%
```

## zipnote {}

```diff
@@ -864,26 +864,26 @@
 
 Filename: tensorboard/util/tensor_util.py
 Comment: 
 
 Filename: tensorboard/util/timing.py
 Comment: 
 
-Filename: tb_nightly-2.9.0a20220501.dist-info/LICENSE
+Filename: tb_nightly-2.9.0a20220502.dist-info/LICENSE
 Comment: 
 
-Filename: tb_nightly-2.9.0a20220501.dist-info/METADATA
+Filename: tb_nightly-2.9.0a20220502.dist-info/METADATA
 Comment: 
 
-Filename: tb_nightly-2.9.0a20220501.dist-info/WHEEL
+Filename: tb_nightly-2.9.0a20220502.dist-info/WHEEL
 Comment: 
 
-Filename: tb_nightly-2.9.0a20220501.dist-info/entry_points.txt
+Filename: tb_nightly-2.9.0a20220502.dist-info/entry_points.txt
 Comment: 
 
-Filename: tb_nightly-2.9.0a20220501.dist-info/top_level.txt
+Filename: tb_nightly-2.9.0a20220502.dist-info/top_level.txt
 Comment: 
 
-Filename: tb_nightly-2.9.0a20220501.dist-info/RECORD
+Filename: tb_nightly-2.9.0a20220502.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## tensorboard/version.py

```diff
@@ -11,8 +11,8 @@
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 # ==============================================================================
 
 """Contains the version string."""
 
-VERSION = "2.9.0a20220501"
+VERSION = "2.9.0a20220502"
```

## Comparing `tb_nightly-2.9.0a20220501.dist-info/LICENSE` & `tb_nightly-2.9.0a20220502.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `tb_nightly-2.9.0a20220501.dist-info/METADATA` & `tb_nightly-2.9.0a20220502.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tb-nightly
-Version: 2.9.0a20220501
+Version: 2.9.0a20220502
 Summary: TensorBoard lets you watch Tensors Flow
 Home-page: https://github.com/tensorflow/tensorboard
 Author: Google Inc.
 Author-email: packages@tensorflow.org
 License: Apache 2.0
 Keywords: tensorflow tensorboard tensor machine learning visualizer
 Platform: UNKNOWN
```

## Comparing `tb_nightly-2.9.0a20220501.dist-info/RECORD` & `tb_nightly-2.9.0a20220502.dist-info/RECORD`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 tensorboard/lazy.py,sha256=jQ6nB0St3fO7tXnP6TThJtsuVeyaEfGip0Beh-J23-8,3555
 tensorboard/main.py,sha256=BEWBybgD-1TGNvAFJ_Tbd0WiAPg6jjymIsncVHFOGqw,1800
 tensorboard/main_lib.py,sha256=-et8A-G-l-sm6tR4-XjHyqrPZfrJ0s3sk8GA20LI2Ac,1959
 tensorboard/manager.py,sha256=nwYd3niVzGt4KGNejx6zqfwnPu6EPtLoQGk0UGRSDIc,16381
 tensorboard/notebook.py,sha256=16nYDCRmO1r5RXntieo0lkyEFxWXh5_Cbgl7F-l8R1o,14704
 tensorboard/plugin_util.py,sha256=WC-DJTflixyrrpZN7p882R2msprV-FLzA0FKZQUBfHM,7491
 tensorboard/program.py,sha256=-Ltbhm0O8ZH3CXp8yBn52SrBAufs-6iV8Swn6gGASqc,34802
-tensorboard/version.py,sha256=H47FPvcr1KTJ-ip3eUg7xywdmDeNcRLWuGcfF9bqBQM,753
+tensorboard/version.py,sha256=8QrN4C7Ltj2dc0UZ7OcnQkT3Tv3wl_J9W71iAlcTYI8,753
 tensorboard/webfiles.zip,sha256=Olxb3AKZ2jPm4-yDn632VPkFvNZJsSWGI_vwaHyznU0,4621116
 tensorboard/_vendor/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 tensorboard/_vendor/bleach/__init__.py,sha256=CtmircSWFH5tn9GO4Ofi0CAB0yUQdU1TkU08GJ98ETk,3769
 tensorboard/_vendor/bleach/callbacks.py,sha256=Lvexc_oncFbfTtsEgItsGzt-rbs5goqQIr-8WtOAKFs,723
 tensorboard/_vendor/bleach/encoding.py,sha256=aq062I1yXRPPjZjYzY4FoMYkCjBA-0QCU-xBhgq4JMQ,2277
 tensorboard/_vendor/bleach/linkifier.py,sha256=djCbTk9lY4MHgGT7LKv7qc2TQiLE4S8B899Af2ZaVhQ,18879
 tensorboard/_vendor/bleach/sanitizer.py,sha256=1JJnx3L56dRX2oAVRv_fU_J0beQh95FdnyX-BlDDpNA,12233
@@ -284,13 +284,13 @@
 tensorboard/util/io_util.py,sha256=pIc9fc5BkMJZIQziZvMx9JKTZh5thk7Ny8_RQmjNxgk,792
 tensorboard/util/lazy_tensor_creator.py,sha256=Nv_tKVqo9dkvuG049mTjby1kjtm1-1RniSOSjEl1hso,4492
 tensorboard/util/op_evaluator.py,sha256=PLrjGRR4MfnGIZcKm0YSYxp__YJgSG0jKuHmTeb5rVw,3827
 tensorboard/util/platform_util.py,sha256=5jr42kvi6GqRzFx6YponSDOFYg7_RL-DTlk6dDefNYM,798
 tensorboard/util/tb_logging.py,sha256=KRWgZ29e_fpK03bCRFP0nFoqN_KkI0RhaeGUVYqNg8M,781
 tensorboard/util/tensor_util.py,sha256=yJvEYRlQ6i-epazSrIzAVr9GTfgY4ACc7pBp2sMIq5U,21802
 tensorboard/util/timing.py,sha256=f2_w98VpKR0TZdA-88kFxeIWdl5y6EHA_Dn6BOispFU,3734
-tb_nightly-2.9.0a20220501.dist-info/LICENSE,sha256=muIndEPx_RqUi7xWKy0zMZVuUyChzEOhHN0z4T0sknk,29236
-tb_nightly-2.9.0a20220501.dist-info/METADATA,sha256=5WQVT05nFB-ObRjpfoV3LAH0Sw19jcnrQfVWv-P2WaA,1873
-tb_nightly-2.9.0a20220501.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-tb_nightly-2.9.0a20220501.dist-info/entry_points.txt,sha256=FV17CwG_RTgFJOgP8RqFKOtLdrm-iCm4EzINTxbyMs8,156
-tb_nightly-2.9.0a20220501.dist-info/top_level.txt,sha256=40P4chmItVOwo2Fz7dRARFaQvcp6ZKme9JhcNbG8d8o,12
-tb_nightly-2.9.0a20220501.dist-info/RECORD,,
+tb_nightly-2.9.0a20220502.dist-info/LICENSE,sha256=muIndEPx_RqUi7xWKy0zMZVuUyChzEOhHN0z4T0sknk,29236
+tb_nightly-2.9.0a20220502.dist-info/METADATA,sha256=ps4WMN7pPCbZkhQysFpy_kvYS3kdaE0K9QOKxoYWe3o,1873
+tb_nightly-2.9.0a20220502.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+tb_nightly-2.9.0a20220502.dist-info/entry_points.txt,sha256=FV17CwG_RTgFJOgP8RqFKOtLdrm-iCm4EzINTxbyMs8,156
+tb_nightly-2.9.0a20220502.dist-info/top_level.txt,sha256=40P4chmItVOwo2Fz7dRARFaQvcp6ZKme9JhcNbG8d8o,12
+tb_nightly-2.9.0a20220502.dist-info/RECORD,,
```

