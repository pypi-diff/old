# Comparing `tmp/bigdl_serving-2.3.0b20230405-py2.py3-none-any.whl.zip` & `tmp/bigdl_serving-2.3.0b20230406-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,22 +1,22 @@
-Zip file size: 21604 bytes, number of entries: 20
+Zip file size: 21603 bytes, number of entries: 20
 -rw-r--r--  2.0 unx      940 b- defN 22-Oct-25 01:39 bigdl/__init__.py
 -rw-r--r--  2.0 unx     9965 b- defN 22-Oct-25 01:39 bigdl/serving/client.py
 -rw-r--r--  2.0 unx     2268 b- defN 22-Oct-25 01:39 bigdl/serving/env.py
 -rw-r--r--  2.0 unx     1375 b- defN 22-Oct-25 01:39 bigdl/serving/log4Error.py
 -rw-r--r--  2.0 unx     4990 b- defN 22-Oct-25 01:39 bigdl/serving/schema.py
 -rw-r--r--  2.0 unx     4980 b- defN 22-Oct-25 01:39 bigdl/serving/kafka/client.py
 -rw-r--r--  2.0 unx     1864 b- defN 22-Oct-25 01:39 bigdl/serving/kafka/kafka_example.py
 -rw-r--r--  2.0 unx       92 b- defN 22-Oct-25 01:39 bigdl/share/serving/cluster-serving-py-setup.py
 -rw-r--r--  2.0 unx     4970 b- defN 22-Oct-25 01:39 bigdl/share/serving/perf-benchmark/e2e_throughput.py
--rwxr-xr-x  2.0 unx      644 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-init
--rwxr-xr-x  2.0 unx       82 b- defN 23-Apr-05 11:08 bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-py-setup.py
--rwxr-xr-x  2.0 unx      155 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-shutdown
--rwxr-xr-x  2.0 unx     3177 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-start
--rwxr-xr-x  2.0 unx     5103 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230405.data/scripts/cluster-with-numactl.sh
--rwxr-xr-x  2.0 unx     1300 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230405.data/scripts/config.yaml
--rwxr-xr-x  2.0 unx     2425 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230405.data/scripts/download-serving-jar.sh
--rw-r--r--  2.0 unx     1051 b- defN 23-Apr-05 11:08 bigdl_serving-2.3.0b20230405.dist-info/METADATA
--rw-r--r--  2.0 unx      110 b- defN 23-Apr-05 11:08 bigdl_serving-2.3.0b20230405.dist-info/WHEEL
--rw-r--r--  2.0 unx        7 b- defN 23-Apr-05 11:08 bigdl_serving-2.3.0b20230405.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1979 b- defN 23-Apr-05 11:08 bigdl_serving-2.3.0b20230405.dist-info/RECORD
-20 files, 47477 bytes uncompressed, 18254 bytes compressed:  61.6%
+-rwxr-xr-x  2.0 unx      644 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-init
+-rwxr-xr-x  2.0 unx       82 b- defN 23-Apr-06 12:02 bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-py-setup.py
+-rwxr-xr-x  2.0 unx      155 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-shutdown
+-rwxr-xr-x  2.0 unx     3177 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-start
+-rwxr-xr-x  2.0 unx     5103 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230406.data/scripts/cluster-with-numactl.sh
+-rwxr-xr-x  2.0 unx     1300 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230406.data/scripts/config.yaml
+-rwxr-xr-x  2.0 unx     2425 b- defN 22-Oct-25 01:39 bigdl_serving-2.3.0b20230406.data/scripts/download-serving-jar.sh
+-rw-r--r--  2.0 unx     1051 b- defN 23-Apr-06 12:02 bigdl_serving-2.3.0b20230406.dist-info/METADATA
+-rw-r--r--  2.0 unx      110 b- defN 23-Apr-06 12:02 bigdl_serving-2.3.0b20230406.dist-info/WHEEL
+-rw-r--r--  2.0 unx        7 b- defN 23-Apr-06 12:02 bigdl_serving-2.3.0b20230406.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1979 b- defN 23-Apr-06 12:02 bigdl_serving-2.3.0b20230406.dist-info/RECORD
+20 files, 47477 bytes uncompressed, 18253 bytes compressed:  61.6%
```

## zipnote {}

```diff
@@ -21,41 +21,41 @@
 
 Filename: bigdl/share/serving/cluster-serving-py-setup.py
 Comment: 
 
 Filename: bigdl/share/serving/perf-benchmark/e2e_throughput.py
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-init
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-init
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-py-setup.py
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-py-setup.py
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-shutdown
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-shutdown
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-start
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-start
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/cluster-with-numactl.sh
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/cluster-with-numactl.sh
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/config.yaml
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/config.yaml
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.data/scripts/download-serving-jar.sh
+Filename: bigdl_serving-2.3.0b20230406.data/scripts/download-serving-jar.sh
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.dist-info/METADATA
+Filename: bigdl_serving-2.3.0b20230406.dist-info/METADATA
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.dist-info/WHEEL
+Filename: bigdl_serving-2.3.0b20230406.dist-info/WHEEL
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.dist-info/top_level.txt
+Filename: bigdl_serving-2.3.0b20230406.dist-info/top_level.txt
 Comment: 
 
-Filename: bigdl_serving-2.3.0b20230405.dist-info/RECORD
+Filename: bigdl_serving-2.3.0b20230406.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-init` & `bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-init`

 * *Files identical despite different names*

## Comparing `bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-start` & `bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-start`

 * *Files identical despite different names*

## Comparing `bigdl_serving-2.3.0b20230405.data/scripts/cluster-with-numactl.sh` & `bigdl_serving-2.3.0b20230406.data/scripts/cluster-with-numactl.sh`

 * *Files identical despite different names*

## Comparing `bigdl_serving-2.3.0b20230405.data/scripts/config.yaml` & `bigdl_serving-2.3.0b20230406.data/scripts/config.yaml`

 * *Files identical despite different names*

## Comparing `bigdl_serving-2.3.0b20230405.data/scripts/download-serving-jar.sh` & `bigdl_serving-2.3.0b20230406.data/scripts/download-serving-jar.sh`

 * *Files identical despite different names*

## Comparing `bigdl_serving-2.3.0b20230405.dist-info/METADATA` & `bigdl_serving-2.3.0b20230406.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bigdl-serving
-Version: 2.3.0b20230405
+Version: 2.3.0b20230406
 Summary: Distributed and Automated Model Inference on Big Data Streaming Frameworks
 Home-page: https://github.com/intel-analytics/BigDL
 Author: BigDL Authors
 Author-email: bigdl-user-group@googlegroups.com
 License: Apache License, Version 2.0
 Platform: mac
 Platform: linux
```

## Comparing `bigdl_serving-2.3.0b20230405.dist-info/RECORD` & `bigdl_serving-2.3.0b20230406.dist-info/RECORD`

 * *Files 12% similar despite different names*

```diff
@@ -3,18 +3,18 @@
 bigdl/serving/env.py,sha256=wtYtsQvSsoOn2mm2Pkf0HM97_NdQgXB9EOFGVu2S4tQ,2268
 bigdl/serving/log4Error.py,sha256=qyCRx-Ab829_qBuh788-9BAnMcwNAkYwmxRCX0N8ZGE,1375
 bigdl/serving/schema.py,sha256=JfNnYFI5wcKo5oyPYLG-1hWLpWrm-LiGZphYHHuUz1k,4990
 bigdl/serving/kafka/client.py,sha256=nZU4-Ppgtj_rElPXFPBmuPEmLWFK7lnj0GbFGWxxvVc,4980
 bigdl/serving/kafka/kafka_example.py,sha256=SogG-jPKX-PyWxeVoyaEEcqmkrSkoE-esAKZIJlirlY,1864
 bigdl/share/serving/cluster-serving-py-setup.py,sha256=GF6KNG_IFhJuHkoJJmHhJH9Mky9N2QXbQjsNT5ggauE,92
 bigdl/share/serving/perf-benchmark/e2e_throughput.py,sha256=tx0tniyFYDrKjRRuSzOKCiVFcLn_xJVW3l_OD_zWIk4,4970
-bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-init,sha256=i_ts4WZhBE5BS90wrKIJ5rWJ9dEdz6AcIk2wnSVo4NQ,644
-bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-py-setup.py,sha256=_6fOziD-sOP7BErTziDyZtJ0BfkfiJlqK6OSAzX3LDQ,82
-bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-shutdown,sha256=otaPFBrbMqAasN-7XnoLR_FmIc9xZzRSVH2ocHxual4,155
-bigdl_serving-2.3.0b20230405.data/scripts/cluster-serving-start,sha256=MSnBLkZh1ZYyDrzPk-u8ZamjqGlgeJ6esic86FDnSbw,3177
-bigdl_serving-2.3.0b20230405.data/scripts/cluster-with-numactl.sh,sha256=bTNz-uI4Bygo4Qe-1wvjE7wn3YgdCln6rxE6Oq--5OI,5103
-bigdl_serving-2.3.0b20230405.data/scripts/config.yaml,sha256=z9SWfSY8iLSeI4ddF9gTCQj89bLqjjGiy7EHHIXKEwk,1300
-bigdl_serving-2.3.0b20230405.data/scripts/download-serving-jar.sh,sha256=LGiI3_6c2oqyGCsEcIlvi-K91QT9yv-REwgCniT3gEI,2425
-bigdl_serving-2.3.0b20230405.dist-info/METADATA,sha256=t9pryhsRoEho3aTzF-PHFGjnRIcDzeNVfecw1CUKDH4,1051
-bigdl_serving-2.3.0b20230405.dist-info/WHEEL,sha256=z9j0xAa_JmUKMpmz72K0ZGALSM_n-wQVmGbleXx2VHg,110
-bigdl_serving-2.3.0b20230405.dist-info/top_level.txt,sha256=cBagmJYb6wgwvnIPkoHIjt6ZCR0nXudViJidCXcTXnQ,7
-bigdl_serving-2.3.0b20230405.dist-info/RECORD,,
+bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-init,sha256=i_ts4WZhBE5BS90wrKIJ5rWJ9dEdz6AcIk2wnSVo4NQ,644
+bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-py-setup.py,sha256=_6fOziD-sOP7BErTziDyZtJ0BfkfiJlqK6OSAzX3LDQ,82
+bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-shutdown,sha256=otaPFBrbMqAasN-7XnoLR_FmIc9xZzRSVH2ocHxual4,155
+bigdl_serving-2.3.0b20230406.data/scripts/cluster-serving-start,sha256=MSnBLkZh1ZYyDrzPk-u8ZamjqGlgeJ6esic86FDnSbw,3177
+bigdl_serving-2.3.0b20230406.data/scripts/cluster-with-numactl.sh,sha256=bTNz-uI4Bygo4Qe-1wvjE7wn3YgdCln6rxE6Oq--5OI,5103
+bigdl_serving-2.3.0b20230406.data/scripts/config.yaml,sha256=z9SWfSY8iLSeI4ddF9gTCQj89bLqjjGiy7EHHIXKEwk,1300
+bigdl_serving-2.3.0b20230406.data/scripts/download-serving-jar.sh,sha256=LGiI3_6c2oqyGCsEcIlvi-K91QT9yv-REwgCniT3gEI,2425
+bigdl_serving-2.3.0b20230406.dist-info/METADATA,sha256=KmangKsxWvHINtFhCF-HXulUuzLZ2WjrCiwr7PRJHRI,1051
+bigdl_serving-2.3.0b20230406.dist-info/WHEEL,sha256=z9j0xAa_JmUKMpmz72K0ZGALSM_n-wQVmGbleXx2VHg,110
+bigdl_serving-2.3.0b20230406.dist-info/top_level.txt,sha256=cBagmJYb6wgwvnIPkoHIjt6ZCR0nXudViJidCXcTXnQ,7
+bigdl_serving-2.3.0b20230406.dist-info/RECORD,,
```

