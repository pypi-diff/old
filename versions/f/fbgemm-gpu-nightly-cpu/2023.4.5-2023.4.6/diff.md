# Comparing `tmp/fbgemm_gpu_nightly_cpu-2023.4.5-cp39-cp39-manylinux1_x86_64.whl.zip` & `tmp/fbgemm_gpu_nightly_cpu-2023.4.6-cp39-cp39-manylinux1_x86_64.whl.zip`

## zipinfo {}

```diff
@@ -1,39 +1,39 @@
-Zip file size: 3822079 bytes, number of entries: 37
--rw-r--r--  2.0 unx      566 b- defN 23-Apr-05 13:02 fbgemm_gpu/__init__.py
--rw-r--r--  2.0 unx    14798 b- defN 23-Apr-05 13:02 fbgemm_gpu/_fbgemm_gpu_docs.py
--rw-r--r--  2.0 unx     2746 b- defN 23-Apr-05 13:02 fbgemm_gpu/batched_unary_embeddings_ops.py
--rw-r--r--  2.0 unx      817 b- defN 23-Apr-05 13:02 fbgemm_gpu/enums.py
--rwxr-xr-x  2.0 unx 13284888 b- defN 23-Apr-05 13:02 fbgemm_gpu/fbgemm_gpu_py.so
--rw-r--r--  2.0 unx     5646 b- defN 23-Apr-05 13:02 fbgemm_gpu/metrics.py
--rw-r--r--  2.0 unx     2338 b- defN 23-Apr-05 13:02 fbgemm_gpu/permute_pooled_embedding_modules.py
--rw-r--r--  2.0 unx     2476 b- defN 23-Apr-05 13:02 fbgemm_gpu/permute_pooled_embedding_modules_split.py
--rw-r--r--  2.0 unx     7682 b- defN 23-Apr-05 13:02 fbgemm_gpu/quantize_comm.py
--rw-r--r--  2.0 unx     4004 b- defN 23-Apr-05 13:02 fbgemm_gpu/quantize_utils.py
--rw-r--r--  2.0 unx     5726 b- defN 23-Apr-05 13:02 fbgemm_gpu/split_embedding_configs.py
--rw-r--r--  2.0 unx     8737 b- defN 23-Apr-05 13:02 fbgemm_gpu/split_embedding_inference_converter.py
--rw-r--r--  2.0 unx    20501 b- defN 23-Apr-05 13:02 fbgemm_gpu/split_embedding_utils.py
--rw-r--r--  2.0 unx   132825 b- defN 23-Apr-05 13:02 fbgemm_gpu/split_table_batched_embeddings_ops.py
--rw-r--r--  2.0 unx    39017 b- defN 23-Apr-05 13:02 fbgemm_gpu/ssd_split_table_batched_embeddings_ops.py
--rw-r--r--  2.0 unx      909 b- defN 23-Apr-05 13:02 fbgemm_gpu/uvm.py
--rw-r--r--  2.0 unx     1912 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/__init__.py
--rw-r--r--  2.0 unx     4399 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_adagrad.py
--rw-r--r--  2.0 unx     5220 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_adam.py
--rw-r--r--  2.0 unx     4717 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_rowwise_adagrad.py
--rw-r--r--  2.0 unx     6838 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_rowwise_adagrad_with_counter.py
--rw-r--r--  2.0 unx     4753 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_rowwise_adagrad_with_weight_decay.py
--rw-r--r--  2.0 unx     3918 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_sgd.py
--rw-r--r--  2.0 unx     1532 b- defN 23-Apr-05 12:43 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_args.py
--rw-r--r--  2.0 unx     5220 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_lamb.py
--rw-r--r--  2.0 unx     4653 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_lars_sgd.py
--rw-r--r--  2.0 unx     5252 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_partial_rowwise_adam.py
--rw-r--r--  2.0 unx     5252 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_partial_rowwise_lamb.py
--rw-r--r--  2.0 unx     4703 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad.py
--rw-r--r--  2.0 unx     6824 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad_with_counter.py
--rw-r--r--  2.0 unx     4739 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad_with_weight_decay.py
--rw-r--r--  2.0 unx     4659 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_weighted_adagrad.py
--rw-r--r--  2.0 unx     3904 b- defN 23-Apr-05 13:00 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_sgd.py
--rw-r--r--  2.0 unx     9839 b- defN 23-Apr-05 13:02 fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/METADATA
--rw-r--r--  2.0 unx      102 b- defN 23-Apr-05 13:02 fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/WHEEL
--rw-r--r--  2.0 unx       11 b- defN 23-Apr-05 13:02 fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     4125 b- defN 23-Apr-05 13:02 fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/RECORD
-37 files, 13626248 bytes uncompressed, 3815111 bytes compressed:  72.0%
+Zip file size: 3822081 bytes, number of entries: 37
+-rw-r--r--  2.0 unx      566 b- defN 23-Apr-06 12:59 fbgemm_gpu/__init__.py
+-rw-r--r--  2.0 unx    14798 b- defN 23-Apr-06 12:59 fbgemm_gpu/_fbgemm_gpu_docs.py
+-rw-r--r--  2.0 unx     2746 b- defN 23-Apr-06 12:59 fbgemm_gpu/batched_unary_embeddings_ops.py
+-rw-r--r--  2.0 unx      817 b- defN 23-Apr-06 12:59 fbgemm_gpu/enums.py
+-rwxr-xr-x  2.0 unx 13284888 b- defN 23-Apr-06 12:59 fbgemm_gpu/fbgemm_gpu_py.so
+-rw-r--r--  2.0 unx     5646 b- defN 23-Apr-06 12:59 fbgemm_gpu/metrics.py
+-rw-r--r--  2.0 unx     2338 b- defN 23-Apr-06 12:59 fbgemm_gpu/permute_pooled_embedding_modules.py
+-rw-r--r--  2.0 unx     2476 b- defN 23-Apr-06 12:59 fbgemm_gpu/permute_pooled_embedding_modules_split.py
+-rw-r--r--  2.0 unx     7682 b- defN 23-Apr-06 12:59 fbgemm_gpu/quantize_comm.py
+-rw-r--r--  2.0 unx     4004 b- defN 23-Apr-06 12:59 fbgemm_gpu/quantize_utils.py
+-rw-r--r--  2.0 unx     5726 b- defN 23-Apr-06 12:59 fbgemm_gpu/split_embedding_configs.py
+-rw-r--r--  2.0 unx     8737 b- defN 23-Apr-06 12:59 fbgemm_gpu/split_embedding_inference_converter.py
+-rw-r--r--  2.0 unx    20501 b- defN 23-Apr-06 12:59 fbgemm_gpu/split_embedding_utils.py
+-rw-r--r--  2.0 unx   132825 b- defN 23-Apr-06 12:59 fbgemm_gpu/split_table_batched_embeddings_ops.py
+-rw-r--r--  2.0 unx    39017 b- defN 23-Apr-06 12:59 fbgemm_gpu/ssd_split_table_batched_embeddings_ops.py
+-rw-r--r--  2.0 unx      909 b- defN 23-Apr-06 12:59 fbgemm_gpu/uvm.py
+-rw-r--r--  2.0 unx     1912 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/__init__.py
+-rw-r--r--  2.0 unx     4399 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_adagrad.py
+-rw-r--r--  2.0 unx     5220 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_adam.py
+-rw-r--r--  2.0 unx     4717 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_rowwise_adagrad.py
+-rw-r--r--  2.0 unx     6838 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_rowwise_adagrad_with_counter.py
+-rw-r--r--  2.0 unx     4753 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_rowwise_adagrad_with_weight_decay.py
+-rw-r--r--  2.0 unx     3918 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_approx_sgd.py
+-rw-r--r--  2.0 unx     1532 b- defN 23-Apr-06 12:53 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_args.py
+-rw-r--r--  2.0 unx     5220 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_lamb.py
+-rw-r--r--  2.0 unx     4653 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_lars_sgd.py
+-rw-r--r--  2.0 unx     5252 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_partial_rowwise_adam.py
+-rw-r--r--  2.0 unx     5252 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_partial_rowwise_lamb.py
+-rw-r--r--  2.0 unx     4703 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad.py
+-rw-r--r--  2.0 unx     6824 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad_with_counter.py
+-rw-r--r--  2.0 unx     4739 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad_with_weight_decay.py
+-rw-r--r--  2.0 unx     4659 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_weighted_adagrad.py
+-rw-r--r--  2.0 unx     3904 b- defN 23-Apr-06 12:57 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_sgd.py
+-rw-r--r--  2.0 unx     9839 b- defN 23-Apr-06 12:59 fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/METADATA
+-rw-r--r--  2.0 unx      102 b- defN 23-Apr-06 12:59 fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/WHEEL
+-rw-r--r--  2.0 unx       11 b- defN 23-Apr-06 12:59 fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     4125 b- defN 23-Apr-06 12:59 fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/RECORD
+37 files, 13626248 bytes uncompressed, 3815113 bytes compressed:  72.0%
```

## zipnote {}

```diff
@@ -93,20 +93,20 @@
 
 Filename: fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_weighted_adagrad.py
 Comment: 
 
 Filename: fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_sgd.py
 Comment: 
 
-Filename: fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/METADATA
+Filename: fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/METADATA
 Comment: 
 
-Filename: fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/WHEEL
+Filename: fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/WHEEL
 Comment: 
 
-Filename: fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/top_level.txt
+Filename: fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/top_level.txt
 Comment: 
 
-Filename: fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/RECORD
+Filename: fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/METADATA` & `fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fbgemm-gpu-nightly-cpu
-Version: 2023.4.5
+Version: 2023.4.6
 Home-page: https://github.com/pytorch/fbgemm
 Author: FBGEMM Team
 Author-email: packages@pytorch.org
 License: BSD-3
 Keywords: PyTorch,Recommendation Models,High Performance Computing,GPU,CUDA
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

## Comparing `fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/RECORD` & `fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/RECORD`

 * *Files 4% similar despite different names*

```diff
@@ -27,11 +27,11 @@
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_partial_rowwise_adam.py,sha256=dzvN4ncV0v_CbbNsH1GvSlD4e8NPAXBTsm3jJcjIZXk,5252
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_partial_rowwise_lamb.py,sha256=8DhgL58GU-fRk_F0naL641aES3lRWw5wllP2Zfe2wBo,5252
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad.py,sha256=hN1jKQl_3iWFF96XBx30skWBucd7EnVXzmWND8fKip8,4703
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad_with_counter.py,sha256=wCSrH66-R4cMXNoJ9mnbXuEpZiSRYDe_3rJqaSCJya4,6824
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_adagrad_with_weight_decay.py,sha256=QdQtmO6YCVQSbt7hnrTKuxoIy23ZOkGDmGgG7RMuGMo,4739
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_rowwise_weighted_adagrad.py,sha256=OcL6PJf1eccTqsMphXbcD4bTjOSnWG2QZHnIslFtuR8,4659
 fbgemm_gpu/split_embedding_codegen_lookup_invokers/lookup_sgd.py,sha256=8h7h5UGzaTX4Hs5zwpsmhbUP1DX2pQytYmLe1-yyFyY,3904
-fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/METADATA,sha256=UVPP_BvgW8Y9p4pCw3bIop7W5Vt7FKl_0tldsvfWrsQ,9839
-fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/WHEEL,sha256=7fnRuWrgVZ-We1c67_7QZCYn_AQfJ-Z7mCmVro0eJMM,102
-fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/top_level.txt,sha256=2tlbTWLkPjhqvLF_6BbqKzkcPluSE-oPRVjI8axK76I,11
-fbgemm_gpu_nightly_cpu-2023.4.5.dist-info/RECORD,,
+fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/METADATA,sha256=pScrh6JpvmMqGXZ2PoLsX08b6Nq5BkKkegurHTAH3Qg,9839
+fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/WHEEL,sha256=7fnRuWrgVZ-We1c67_7QZCYn_AQfJ-Z7mCmVro0eJMM,102
+fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/top_level.txt,sha256=2tlbTWLkPjhqvLF_6BbqKzkcPluSE-oPRVjI8axK76I,11
+fbgemm_gpu_nightly_cpu-2023.4.6.dist-info/RECORD,,
```

