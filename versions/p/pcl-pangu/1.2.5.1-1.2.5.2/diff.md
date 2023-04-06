# Comparing `tmp/pcl_pangu-1.2.5.1.tar.gz` & `tmp/pcl_pangu-1.2.5.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pcl_pangu-1.2.5.1.tar", last modified: Thu Apr  6 09:13:43 2023, max compression
+gzip compressed data, was "dist/pcl_pangu-1.2.5.2.tar", last modified: Thu Apr  6 10:14:27 2023, max compression
```

## Comparing `pcl_pangu-1.2.5.1.tar` & `pcl_pangu-1.2.5.2.tar`

### file list

```diff
@@ -1,186 +1,186 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/
--rw-r--r--   0 root         (0) root         (0)      289 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/PKG-INFO
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/
--rw-r--r--   0 root         (0) root         (0)      246 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2549 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/tokenization_jieba.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/
--rw-r--r--   0 root         (0) root         (0)    14949 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/tokenizer.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/__init__.py
--rw-r--r--   0 root         (0) root         (0)  2423393 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/spm.128k.model.1
--rw-r--r--   0 root         (0) root         (0)  1991068 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/data_dict.128k.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/bpe_4w_pcl/
--rw-r--r--   0 root         (0) root         (0)   879697 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.model
--rw-r--r--   0 root         (0) root         (0)   717452 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.vocab
--rw-r--r--   0 root         (0) root         (0)      208 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/
--rw-r--r--   0 root         (0) root         (0)     1537 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/ms_2_numpy.py
--rw-r--r--   0 root         (0) root         (0)     1354 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/merge_pytorch_model.py
--rw-r--r--   0 root         (0) root         (0)     1664 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/split_pytorch_model.py
--rw-r--r--   0 root         (0) root         (0)      220 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1298 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/numpy_2_pt.py
--rw-r--r--   0 root         (0) root         (0)    15563 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model_converter/_numpy_ckpt_2_pytorch.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/dataset/
--rw-r--r--   0 root         (0) root         (0)     7133 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/dataset/txt2mindrecord.py
--rw-r--r--   0 root         (0) root         (0)      151 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/dataset/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3754 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/dataset/txt2bin.py
--rw-r--r--   0 root         (0) root         (0)     5255 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/dataset/preprocess_data_pangu.py
--rw-r--r--   0 root         (0) root         (0)    14926 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/dataset/pre_process_chinese.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/
--rw-r--r--   0 root         (0) root         (0)      212 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/infer/
--rw-r--r--   0 root         (0) root         (0)     3337 2023-04-06 01:27:22.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/infer/pangu_evolution_dto.py
--rw-r--r--   0 root         (0) root         (0)     3229 2023-04-06 09:12:13.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/infer/infer.py
--rw-r--r--   0 root         (0) root         (0)       86 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/infer/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2968 2023-04-06 01:32:40.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/infer/pangu_alpha_dto.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/modelinfo/
--rw-r--r--   0 root         (0) root         (0)     1166 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/modelinfo/modelinfo.py
--rw-r--r--   0 root         (0) root         (0)       86 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/online/modelinfo/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/
--rw-r--r--   0 root         (0) root         (0)     3653 2023-03-30 09:53:40.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/infer.py
--rw-r--r--   0 root         (0) root         (0)     7867 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/test.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/
--rw-r--r--   0 root         (0) root         (0)     2125 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/config.py
--rw-r--r--   0 root         (0) root         (0)     9132 2023-04-03 13:53:20.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/model_onnx_gpu.py
--rw-r--r--   0 root         (0) root         (0)     9588 2023-04-03 13:33:22.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/model.py
--rw-r--r--   0 root         (0) root         (0)     1435 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/utils.py
--rw-r--r--   0 root         (0) root         (0)     5040 2023-03-30 09:23:46.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/sample.py
--rw-r--r--   0 root         (0) root         (0)     3911 2023-04-04 01:24:04.000000 pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/conver_pt_onnx.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/
--rw-r--r--   0 root         (0) root         (0)    15353 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/inference_alpha_ms13.py
--rw-r--r--   0 root         (0) root         (0)    22639 2023-04-05 08:36:41.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/train_alpha_ms13.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/
--rw-r--r--   0 root         (0) root         (0)    12303 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_wrapcell.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2505 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/tokenization_jieba.py
--rw-r--r--   0 root         (0) root         (0)     9244 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/dataset.py
--rw-r--r--   0 root         (0) root         (0)     6406 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_config.py
--rw-r--r--   0 root         (0) root         (0)    68987 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/serialization.py
--rw-r--r--   0 root         (0) root         (0)    36469 2023-04-03 06:24:29.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/utils_pangu.py
--rw-r--r--   0 root         (0) root         (0)     9209 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/preprocess.py
--rw-r--r--   0 root         (0) root         (0)    64752 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha.py
--rw-r--r--   0 root         (0) root         (0)    17636 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/generate.py
--rw-r--r--   0 root         (0) root         (0)      130 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/evolution/
--rw-r--r--   0 root         (0) root         (0)     4576 2023-03-30 10:24:57.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/evolution/config_evolution.py
--rw-r--r--   0 root         (0) root         (0)      210 2023-04-03 01:24:00.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/evolution/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5982 2023-03-30 10:26:27.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/evolution/evolution.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/
--rw-r--r--   0 root         (0) root         (0)     2220 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference-en.md
--rw-r--r--   0 root         (0) root         (0)     1011 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/testLayerNorm.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/
--rw-r--r--   0 root         (0) root         (0)    10948 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_Pangu.py
--rw-r--r--   0 root         (0) root         (0)    11619 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/merge_mp_partitions.py
--rw-r--r--   0 root         (0) root         (0)     7896 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/preprocess_data_pangu.py
--rw-r--r--   0 root         (0) root         (0)     1295 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/linter.py
--rw-r--r--   0 root         (0) root         (0)    16425 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/change_MspCkpt_ToMgt.py
--rw-r--r--   0 root         (0) root         (0)     8699 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/split_full_model_into_mp_model.py
--rw-r--r--   0 root         (0) root         (0)      941 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/create_doc_index.py
--rw-r--r--   0 root         (0) root         (0)    10812 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_epangu.py
--rw-r--r--   0 root         (0) root         (0)     9474 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/splitMergedCkpt_v0.py
--rw-r--r--   0 root         (0) root         (0)     3624 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_gpt2.py
--rw-r--r--   0 root         (0) root         (0)    14695 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/LICENSE
--rw-r--r--   0 root         (0) root         (0)       67 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)    23337 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/mergeMpCkpt.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/__init__.py
--rw-r--r--   0 root         (0) root         (0)    31808 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/README_mgt.md
--rw-r--r--   0 root         (0) root         (0)     8683 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/README-en.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/
--rw-r--r--   0 root         (0) root         (0)     5188 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/memory.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/
--rw-r--r--   0 root         (0) root         (0)     6864 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenizer.py
--rw-r--r--   0 root         (0) root         (0)      731 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3389 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenization_jieba.py
--rw-r--r--   0 root         (0) root         (0)    13952 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/bert_tokenization.py
--rw-r--r--   0 root         (0) root         (0)    13780 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/gpt2_tokenization.py
--rw-r--r--   0 root         (0) root         (0)     5909 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/initialize.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/
--rw-r--r--   0 root         (0) root         (0)     2393 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.cpp
--rw-r--r--   0 root         (0) root         (0)     2337 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2959 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax_cuda.cu
--rw-r--r--   0 root         (0) root         (0)    19953 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.h
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/
--rw-r--r--   0 root         (0) root         (0)     8331 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16util.py
--rw-r--r--   0 root         (0) root         (0)      971 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/__init__.py
--rw-r--r--   0 root         (0) root         (0)    32911 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16.py
--rw-r--r--   0 root         (0) root         (0)    10504 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/loss_scaler.py
--rw-r--r--   0 root         (0) root         (0)     1408 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/__init__.py
--rw-r--r--   0 root         (0) root         (0)    11011 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/checkpointing.py
--rw-r--r--   0 root         (0) root         (0)     7538 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/global_vars.py
--rw-r--r--   0 root         (0) root         (0)     1249 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/package_info.py
--rw-r--r--   0 root         (0) root         (0)     4182 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/indexer.py
--rw-r--r--   0 root         (0) root         (0)    16248 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/text_generation_utils.py
--rw-r--r--   0 root         (0) root         (0)    21991 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/training.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/
--rw-r--r--   0 root         (0) root         (0)    16415 2023-03-30 03:21:36.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/layers.py
--rw-r--r--   0 root         (0) root         (0)     5733 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/initialize.py
--rw-r--r--   0 root         (0) root         (0)    13208 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/random.py
--rw-r--r--   0 root         (0) root         (0)     2144 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5025 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/grads.py
--rw-r--r--   0 root         (0) root         (0)     2781 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/utils.py
--rw-r--r--   0 root         (0) root         (0)     4915 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/cross_entropy.py
--rw-r--r--   0 root         (0) root         (0)     4134 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/data.py
--rw-r--r--   0 root         (0) root         (0)     4444 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/mappings.py
--rw-r--r--   0 root         (0) root         (0)     6779 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/utils.py
--rw-r--r--   0 root         (0) root         (0)     1148 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/module.py
--rw-r--r--   0 root         (0) root         (0)    23215 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/arguments.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/
--rw-r--r--   0 root         (0) root         (0)     3890 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_softmax.py
--rw-r--r--   0 root         (0) root         (0)     5852 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/gpt2_model.py
--rw-r--r--   0 root         (0) root         (0)      936 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/__init__.py
--rw-r--r--   0 root         (0) root         (0)      995 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/mpu_utils.py
--rw-r--r--   0 root         (0) root         (0)     4752 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/multiple_choice.py
--rw-r--r--   0 root         (0) root         (0)     2151 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_bias_gelu.py
--rw-r--r--   0 root         (0) root         (0)     3161 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/utils.py
--rw-r--r--   0 root         (0) root         (0)    36536 2023-03-30 03:27:44.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/transformer.py
--rw-r--r--   0 root         (0) root         (0)    27501 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/language_model.py
--rw-r--r--   0 root         (0) root         (0)     8874 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/realm_model.py
--rw-r--r--   0 root         (0) root         (0)     8364 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/bert_model.py
--rw-r--r--   0 root         (0) root         (0)     4283 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/classification.py
--rw-r--r--   0 root         (0) root         (0)     5151 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/distributed.py
--rw-r--r--   0 root         (0) root         (0)    11546 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/alpha_enhanced_model.py
--rw-r--r--   0 root         (0) root         (0)     5054 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/learning_rates.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/
--rw-r--r--   0 root         (0) root         (0)    18923 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/dataset_utils.py
--rw-r--r--   0 root         (0) root         (0)     9038 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_index.py
--rw-r--r--   0 root         (0) root         (0)    13647 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/gpt2_dataset.py
--rw-r--r--   0 root         (0) root         (0)    25244 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/helpers.cpp
--rw-r--r--   0 root         (0) root         (0)       31 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/__init__.py
--rw-r--r--   0 root         (0) root         (0)    19128 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/indexed_dataset.py
--rw-r--r--   0 root         (0) root         (0)      288 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/Makefile
--rw-r--r--   0 root         (0) root         (0)     7721 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_dataset_utils.py
--rw-r--r--   0 root         (0) root         (0)     6203 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/samplers.py
--rw-r--r--   0 root         (0) root         (0)     9841 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/bert_dataset.py
--rw-r--r--   0 root         (0) root         (0)     5695 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/ict_dataset.py
--rw-r--r--   0 root         (0) root         (0)     5268 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_ict.py
--rw-r--r--   0 root         (0) root         (0)     3106 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/setup.py
--rw-r--r--   0 root         (0) root         (0)     3960 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_bert.py
--rw-r--r--   0 root         (0) root         (0)       36 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/requirements.txt
--rw-r--r--   0 root         (0) root         (0)     2267 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference.md
--rw-r--r--   0 root         (0) root         (0)     8335 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/README.md
--rw-r--r--   0 root         (0) root         (0)     3681 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_evolution.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/mPangu/
--rw-r--r--   0 root         (0) root         (0)     5707 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/mPangu/mPangu.py
--rw-r--r--   0 root         (0) root         (0)      203 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/mPangu/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7213 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/mPangu/config_mPangu.py
--rw-r--r--   0 root         (0) root         (0)     2762 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/launcher_torch.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/alpha/
--rw-r--r--   0 root         (0) root         (0)     7356 2023-03-30 09:05:32.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/alpha/alpha.py
--rw-r--r--   0 root         (0) root         (0)      259 2023-03-30 09:00:28.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/alpha/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7659 2023-04-03 04:58:33.000000 pcl_pangu-1.2.5.1/pcl_pangu/model/alpha/config_alpha.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu/context/
--rw-r--r--   0 root         (0) root         (0)      452 2023-03-30 08:59:08.000000 pcl_pangu-1.2.5.1/pcl_pangu/context/context.py
--rw-r--r--   0 root         (0) root         (0)      263 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/context/__init__.py
--rw-r--r--   0 root         (0) root         (0)      314 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.1/pcl_pangu/context/check_context.py
--rw-r--r--   0 root         (0) root         (0)     1955 2023-04-06 09:12:44.000000 pcl_pangu-1.2.5.1/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/pcl_pangu.egg-info/
--rw-r--r--   0 root         (0) root         (0)       10 2023-04-06 09:13:42.000000 pcl_pangu-1.2.5.1/pcl_pangu.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      289 2023-04-06 09:13:42.000000 pcl_pangu-1.2.5.1/pcl_pangu.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 09:13:42.000000 pcl_pangu-1.2.5.1/pcl_pangu.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)     8394 2023-04-06 09:13:42.000000 pcl_pangu-1.2.5.1/pcl_pangu.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)      114 2023-04-06 09:13:42.000000 pcl_pangu-1.2.5.1/pcl_pangu.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 09:13:43.000000 pcl_pangu-1.2.5.1/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     7675 2023-04-06 01:29:53.000000 pcl_pangu-1.2.5.1/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/
+-rw-r--r--   0 root         (0) root         (0)      289 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/
+-rw-r--r--   0 root         (0) root         (0)      246 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2549 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/tokenization_jieba.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/
+-rw-r--r--   0 root         (0) root         (0)    14949 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/tokenizer.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/__init__.py
+-rw-r--r--   0 root         (0) root         (0)  2423393 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/spm.128k.model.1
+-rw-r--r--   0 root         (0) root         (0)  1991068 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/data_dict.128k.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/bpe_4w_pcl/
+-rw-r--r--   0 root         (0) root         (0)   879697 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.model
+-rw-r--r--   0 root         (0) root         (0)   717452 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.vocab
+-rw-r--r--   0 root         (0) root         (0)      208 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/
+-rw-r--r--   0 root         (0) root         (0)     1537 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/ms_2_numpy.py
+-rw-r--r--   0 root         (0) root         (0)     1354 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/merge_pytorch_model.py
+-rw-r--r--   0 root         (0) root         (0)     1664 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/split_pytorch_model.py
+-rw-r--r--   0 root         (0) root         (0)      220 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1298 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/numpy_2_pt.py
+-rw-r--r--   0 root         (0) root         (0)    15563 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model_converter/_numpy_ckpt_2_pytorch.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/dataset/
+-rw-r--r--   0 root         (0) root         (0)     7133 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/dataset/txt2mindrecord.py
+-rw-r--r--   0 root         (0) root         (0)      151 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/dataset/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3754 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/dataset/txt2bin.py
+-rw-r--r--   0 root         (0) root         (0)     5255 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/dataset/preprocess_data_pangu.py
+-rw-r--r--   0 root         (0) root         (0)    14926 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/dataset/pre_process_chinese.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/
+-rw-r--r--   0 root         (0) root         (0)      212 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/infer/
+-rw-r--r--   0 root         (0) root         (0)     3337 2023-04-06 10:10:09.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/infer/pangu_evolution_dto.py
+-rw-r--r--   0 root         (0) root         (0)     3229 2023-04-06 09:12:13.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/infer/infer.py
+-rw-r--r--   0 root         (0) root         (0)       86 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/infer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2968 2023-04-06 10:11:00.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/infer/pangu_alpha_dto.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/modelinfo/
+-rw-r--r--   0 root         (0) root         (0)     1166 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/modelinfo/modelinfo.py
+-rw-r--r--   0 root         (0) root         (0)       86 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/online/modelinfo/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/
+-rw-r--r--   0 root         (0) root         (0)     3653 2023-03-30 09:53:40.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/infer.py
+-rw-r--r--   0 root         (0) root         (0)     7867 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/test.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/
+-rw-r--r--   0 root         (0) root         (0)     2125 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/config.py
+-rw-r--r--   0 root         (0) root         (0)     9132 2023-04-03 13:53:20.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/model_onnx_gpu.py
+-rw-r--r--   0 root         (0) root         (0)     9588 2023-04-03 13:33:22.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/model.py
+-rw-r--r--   0 root         (0) root         (0)     1435 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/utils.py
+-rw-r--r--   0 root         (0) root         (0)     5040 2023-03-30 09:23:46.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/sample.py
+-rw-r--r--   0 root         (0) root         (0)     3911 2023-04-04 01:24:04.000000 pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/conver_pt_onnx.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/
+-rw-r--r--   0 root         (0) root         (0)    15353 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/inference_alpha_ms13.py
+-rw-r--r--   0 root         (0) root         (0)    22639 2023-04-05 08:36:41.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/train_alpha_ms13.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/
+-rw-r--r--   0 root         (0) root         (0)    12303 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_wrapcell.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2505 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/tokenization_jieba.py
+-rw-r--r--   0 root         (0) root         (0)     9244 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/dataset.py
+-rw-r--r--   0 root         (0) root         (0)     6406 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_config.py
+-rw-r--r--   0 root         (0) root         (0)    68987 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/serialization.py
+-rw-r--r--   0 root         (0) root         (0)    36469 2023-04-03 06:24:29.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/utils_pangu.py
+-rw-r--r--   0 root         (0) root         (0)     9209 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/preprocess.py
+-rw-r--r--   0 root         (0) root         (0)    64752 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha.py
+-rw-r--r--   0 root         (0) root         (0)    17636 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/generate.py
+-rw-r--r--   0 root         (0) root         (0)      130 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/evolution/
+-rw-r--r--   0 root         (0) root         (0)     4576 2023-03-30 10:24:57.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/evolution/config_evolution.py
+-rw-r--r--   0 root         (0) root         (0)      210 2023-04-03 01:24:00.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/evolution/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5982 2023-03-30 10:26:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/evolution/evolution.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/
+-rw-r--r--   0 root         (0) root         (0)     2220 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference-en.md
+-rw-r--r--   0 root         (0) root         (0)     1011 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/testLayerNorm.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/
+-rw-r--r--   0 root         (0) root         (0)    10948 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_Pangu.py
+-rw-r--r--   0 root         (0) root         (0)    11619 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/merge_mp_partitions.py
+-rw-r--r--   0 root         (0) root         (0)     7896 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/preprocess_data_pangu.py
+-rw-r--r--   0 root         (0) root         (0)     1295 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/linter.py
+-rw-r--r--   0 root         (0) root         (0)    16425 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/change_MspCkpt_ToMgt.py
+-rw-r--r--   0 root         (0) root         (0)     8699 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/split_full_model_into_mp_model.py
+-rw-r--r--   0 root         (0) root         (0)      941 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/create_doc_index.py
+-rw-r--r--   0 root         (0) root         (0)    10812 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_epangu.py
+-rw-r--r--   0 root         (0) root         (0)     9474 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/splitMergedCkpt_v0.py
+-rw-r--r--   0 root         (0) root         (0)     3624 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_gpt2.py
+-rw-r--r--   0 root         (0) root         (0)    14695 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       67 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)    23337 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/mergeMpCkpt.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    31808 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/README_mgt.md
+-rw-r--r--   0 root         (0) root         (0)     8683 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/README-en.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/
+-rw-r--r--   0 root         (0) root         (0)     5188 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/memory.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/
+-rw-r--r--   0 root         (0) root         (0)     6864 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenizer.py
+-rw-r--r--   0 root         (0) root         (0)      731 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3389 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenization_jieba.py
+-rw-r--r--   0 root         (0) root         (0)    13952 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/bert_tokenization.py
+-rw-r--r--   0 root         (0) root         (0)    13780 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/gpt2_tokenization.py
+-rw-r--r--   0 root         (0) root         (0)     5909 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/initialize.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/
+-rw-r--r--   0 root         (0) root         (0)     2393 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.cpp
+-rw-r--r--   0 root         (0) root         (0)     2337 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2959 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax_cuda.cu
+-rw-r--r--   0 root         (0) root         (0)    19953 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.h
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/
+-rw-r--r--   0 root         (0) root         (0)     8331 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16util.py
+-rw-r--r--   0 root         (0) root         (0)      971 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    32911 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16.py
+-rw-r--r--   0 root         (0) root         (0)    10504 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/loss_scaler.py
+-rw-r--r--   0 root         (0) root         (0)     1408 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    11011 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/checkpointing.py
+-rw-r--r--   0 root         (0) root         (0)     7538 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/global_vars.py
+-rw-r--r--   0 root         (0) root         (0)     1249 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/package_info.py
+-rw-r--r--   0 root         (0) root         (0)     4182 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/indexer.py
+-rw-r--r--   0 root         (0) root         (0)    16248 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/text_generation_utils.py
+-rw-r--r--   0 root         (0) root         (0)    21991 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/training.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/
+-rw-r--r--   0 root         (0) root         (0)    16415 2023-03-30 03:21:36.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/layers.py
+-rw-r--r--   0 root         (0) root         (0)     5733 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/initialize.py
+-rw-r--r--   0 root         (0) root         (0)    13208 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/random.py
+-rw-r--r--   0 root         (0) root         (0)     2144 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5025 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/grads.py
+-rw-r--r--   0 root         (0) root         (0)     2781 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/utils.py
+-rw-r--r--   0 root         (0) root         (0)     4915 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/cross_entropy.py
+-rw-r--r--   0 root         (0) root         (0)     4134 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/data.py
+-rw-r--r--   0 root         (0) root         (0)     4444 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/mappings.py
+-rw-r--r--   0 root         (0) root         (0)     6779 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/utils.py
+-rw-r--r--   0 root         (0) root         (0)     1148 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/module.py
+-rw-r--r--   0 root         (0) root         (0)    23215 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/arguments.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/
+-rw-r--r--   0 root         (0) root         (0)     3890 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_softmax.py
+-rw-r--r--   0 root         (0) root         (0)     5852 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/gpt2_model.py
+-rw-r--r--   0 root         (0) root         (0)      936 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      995 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/mpu_utils.py
+-rw-r--r--   0 root         (0) root         (0)     4752 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/multiple_choice.py
+-rw-r--r--   0 root         (0) root         (0)     2151 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_bias_gelu.py
+-rw-r--r--   0 root         (0) root         (0)     3161 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/utils.py
+-rw-r--r--   0 root         (0) root         (0)    36536 2023-03-30 03:27:44.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/transformer.py
+-rw-r--r--   0 root         (0) root         (0)    27501 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/language_model.py
+-rw-r--r--   0 root         (0) root         (0)     8874 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/realm_model.py
+-rw-r--r--   0 root         (0) root         (0)     8364 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/bert_model.py
+-rw-r--r--   0 root         (0) root         (0)     4283 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/classification.py
+-rw-r--r--   0 root         (0) root         (0)     5151 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/distributed.py
+-rw-r--r--   0 root         (0) root         (0)    11546 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/alpha_enhanced_model.py
+-rw-r--r--   0 root         (0) root         (0)     5054 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/learning_rates.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/
+-rw-r--r--   0 root         (0) root         (0)    18923 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/dataset_utils.py
+-rw-r--r--   0 root         (0) root         (0)     9038 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_index.py
+-rw-r--r--   0 root         (0) root         (0)    13647 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/gpt2_dataset.py
+-rw-r--r--   0 root         (0) root         (0)    25244 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/helpers.cpp
+-rw-r--r--   0 root         (0) root         (0)       31 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    19128 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/indexed_dataset.py
+-rw-r--r--   0 root         (0) root         (0)      288 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/Makefile
+-rw-r--r--   0 root         (0) root         (0)     7721 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_dataset_utils.py
+-rw-r--r--   0 root         (0) root         (0)     6203 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/samplers.py
+-rw-r--r--   0 root         (0) root         (0)     9841 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/bert_dataset.py
+-rw-r--r--   0 root         (0) root         (0)     5695 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/ict_dataset.py
+-rw-r--r--   0 root         (0) root         (0)     5268 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_ict.py
+-rw-r--r--   0 root         (0) root         (0)     3106 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/setup.py
+-rw-r--r--   0 root         (0) root         (0)     3960 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_bert.py
+-rw-r--r--   0 root         (0) root         (0)       36 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/requirements.txt
+-rw-r--r--   0 root         (0) root         (0)     2267 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference.md
+-rw-r--r--   0 root         (0) root         (0)     8335 2023-04-06 01:31:51.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/README.md
+-rw-r--r--   0 root         (0) root         (0)     3681 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_evolution.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/mPangu/
+-rw-r--r--   0 root         (0) root         (0)     5707 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/mPangu/mPangu.py
+-rw-r--r--   0 root         (0) root         (0)      203 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/mPangu/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7213 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/mPangu/config_mPangu.py
+-rw-r--r--   0 root         (0) root         (0)     2762 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/launcher_torch.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/alpha/
+-rw-r--r--   0 root         (0) root         (0)     7356 2023-03-30 09:05:32.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/alpha/alpha.py
+-rw-r--r--   0 root         (0) root         (0)      259 2023-03-30 09:00:28.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/alpha/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7659 2023-04-03 04:58:33.000000 pcl_pangu-1.2.5.2/pcl_pangu/model/alpha/config_alpha.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu/context/
+-rw-r--r--   0 root         (0) root         (0)      452 2023-03-30 08:59:08.000000 pcl_pangu-1.2.5.2/pcl_pangu/context/context.py
+-rw-r--r--   0 root         (0) root         (0)      263 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/context/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      314 2023-03-09 08:17:18.000000 pcl_pangu-1.2.5.2/pcl_pangu/context/check_context.py
+-rw-r--r--   0 root         (0) root         (0)     1955 2023-04-06 10:16:03.000000 pcl_pangu-1.2.5.2/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/pcl_pangu.egg-info/
+-rw-r--r--   0 root         (0) root         (0)       10 2023-04-06 10:14:26.000000 pcl_pangu-1.2.5.2/pcl_pangu.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      289 2023-04-06 10:14:26.000000 pcl_pangu-1.2.5.2/pcl_pangu.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 10:14:26.000000 pcl_pangu-1.2.5.2/pcl_pangu.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)     8394 2023-04-06 10:14:26.000000 pcl_pangu-1.2.5.2/pcl_pangu.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)      114 2023-04-06 10:14:26.000000 pcl_pangu-1.2.5.2/pcl_pangu.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 10:14:27.000000 pcl_pangu-1.2.5.2/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     7675 2023-04-06 01:29:53.000000 pcl_pangu-1.2.5.2/README.md
```

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/tokenization_jieba.py` & `pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/tokenization_jieba.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/tokenizer.py` & `pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/tokenizer.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/spm.128k.model.1` & `pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/spm.128k.model.1`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/spm_13w/data_dict.128k.txt` & `pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/spm_13w/data_dict.128k.txt`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.model` & `pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.model`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.vocab` & `pcl_pangu-1.2.5.2/pcl_pangu/tokenizer/bpe_4w_pcl/vocab.vocab`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model_converter/ms_2_numpy.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model_converter/ms_2_numpy.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model_converter/merge_pytorch_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model_converter/merge_pytorch_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model_converter/split_pytorch_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model_converter/split_pytorch_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model_converter/numpy_2_pt.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model_converter/numpy_2_pt.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model_converter/_numpy_ckpt_2_pytorch.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model_converter/_numpy_ckpt_2_pytorch.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/dataset/txt2mindrecord.py` & `pcl_pangu-1.2.5.2/pcl_pangu/dataset/txt2mindrecord.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/dataset/txt2bin.py` & `pcl_pangu-1.2.5.2/pcl_pangu/dataset/txt2bin.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/dataset/preprocess_data_pangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/dataset/preprocess_data_pangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/dataset/pre_process_chinese.py` & `pcl_pangu-1.2.5.2/pcl_pangu/dataset/pre_process_chinese.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/online/infer/pangu_evolution_dto.py` & `pcl_pangu-1.2.5.2/pcl_pangu/online/infer/pangu_evolution_dto.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/online/infer/infer.py` & `pcl_pangu-1.2.5.2/pcl_pangu/online/infer/infer.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/online/infer/pangu_alpha_dto.py` & `pcl_pangu-1.2.5.2/pcl_pangu/online/infer/pangu_alpha_dto.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/online/modelinfo/modelinfo.py` & `pcl_pangu-1.2.5.2/pcl_pangu/online/modelinfo/modelinfo.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/infer.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/infer.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/test.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/test.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/config.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/config.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/model_onnx_gpu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/model_onnx_gpu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/pangu/sample.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/pangu/sample.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/onnx_inference/conver_pt_onnx.py` & `pcl_pangu-1.2.5.2/pcl_pangu/onnx_inference/conver_pt_onnx.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/inference_alpha_ms13.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/inference_alpha_ms13.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/train_alpha_ms13.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/train_alpha_ms13.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_wrapcell.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_wrapcell.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/tokenization_jieba.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/tokenization_jieba.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/dataset.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/dataset.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_config.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha_config.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/serialization.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/serialization.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/utils_pangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/utils_pangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/preprocess.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/preprocess.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/pangu_alpha.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_mindspore/src/generate.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_mindspore/src/generate.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/evolution/config_evolution.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/evolution/config_evolution.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/evolution/evolution.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/evolution/evolution.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference-en.md` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference-en.md`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/testLayerNorm.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/testLayerNorm.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_Pangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_Pangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/merge_mp_partitions.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/merge_mp_partitions.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/preprocess_data_pangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/preprocess_data_pangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/linter.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/linter.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/change_MspCkpt_ToMgt.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/change_MspCkpt_ToMgt.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/split_full_model_into_mp_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/split_full_model_into_mp_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/create_doc_index.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/create_doc_index.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_epangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/generate_samples_epangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/tools/splitMergedCkpt_v0.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/tools/splitMergedCkpt_v0.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_gpt2.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_gpt2.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/LICENSE` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/LICENSE`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/mergeMpCkpt.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/mergeMpCkpt.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/README_mgt.md` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/README_mgt.md`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/README-en.md` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/README-en.md`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/memory.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/memory.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenizer.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenizer.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/__init__.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/__init__.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenization_jieba.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/tokenization_jieba.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/bert_tokenization.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/bert_tokenization.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/gpt2_tokenization.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/tokenizer/gpt2_tokenization.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/initialize.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/initialize.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.cpp` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.cpp`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/__init__.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/__init__.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax_cuda.cu` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax_cuda.cu`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.h` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fused_kernels/scaled_upper_triang_masked_softmax.h`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16util.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16util.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/__init__.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/__init__.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/fp16.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/loss_scaler.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/fp16/loss_scaler.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/__init__.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/__init__.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/checkpointing.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/checkpointing.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/global_vars.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/global_vars.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/package_info.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/package_info.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/indexer.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/indexer.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/text_generation_utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/text_generation_utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/training.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/training.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/layers.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/layers.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/initialize.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/initialize.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/random.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/random.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/__init__.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/__init__.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/grads.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/grads.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/cross_entropy.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/cross_entropy.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/data.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/data.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/mappings.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/mpu/mappings.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/module.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/module.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/arguments.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/arguments.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_softmax.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_softmax.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/gpt2_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/gpt2_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/__init__.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/__init__.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/mpu_utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/mpu_utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/multiple_choice.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/multiple_choice.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_bias_gelu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/fused_bias_gelu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/transformer.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/transformer.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/language_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/language_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/realm_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/realm_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/bert_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/bert_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/classification.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/classification.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/distributed.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/distributed.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/model/alpha_enhanced_model.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/model/alpha_enhanced_model.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/learning_rates.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/learning_rates.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/dataset_utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/dataset_utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_index.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_index.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/gpt2_dataset.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/gpt2_dataset.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/helpers.cpp` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/helpers.cpp`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/indexed_dataset.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/indexed_dataset.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_dataset_utils.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/realm_dataset_utils.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/samplers.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/samplers.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/bert_dataset.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/bert_dataset.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/megatron/data/ict_dataset.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/megatron/data/ict_dataset.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_ict.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_ict.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/setup.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/setup.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_bert.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_bert.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference.md` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/3-minus-inference.md`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/README.md` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/README.md`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/panguAlpha_pytorch/pretrain_evolution.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/panguAlpha_pytorch/pretrain_evolution.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/mPangu/mPangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/mPangu/mPangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/mPangu/config_mPangu.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/mPangu/config_mPangu.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/launcher_torch.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/launcher_torch.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/alpha/alpha.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/alpha/alpha.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu/model/alpha/config_alpha.py` & `pcl_pangu-1.2.5.2/pcl_pangu/model/alpha/config_alpha.py`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/setup.py` & `pcl_pangu-1.2.5.2/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -45,15 +45,15 @@
  'loguru>=0.3.0']
 
 extras_require = \
 {':python_version < "3.7"': ['dataclasses==0.6']}
 
 setup_kwargs = {
     'name': 'pcl_pangu',
-    'version': '1.2.5.1',
+    'version': '1.2.5.2',
     'description': 'pcl_pangu',
     'long_description': '# pcl_pangu ',
     'author': '2022 PCL',
     'author_email': 'pcl.openi@pcl.ac.cn',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://openi.pcl.ac.cn/PCL-Platform.Intelligence/pcl_pangu',
```

### Comparing `pcl_pangu-1.2.5.1/pcl_pangu.egg-info/SOURCES.txt` & `pcl_pangu-1.2.5.2/pcl_pangu.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pcl_pangu-1.2.5.1/README.md` & `pcl_pangu-1.2.5.2/README.md`

 * *Files identical despite different names*

