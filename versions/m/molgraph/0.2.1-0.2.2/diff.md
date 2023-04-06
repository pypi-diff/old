# Comparing `tmp/molgraph-0.2.1.tar.gz` & `tmp/molgraph-0.2.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "molgraph-0.2.1.tar", last modified: Thu Apr  6 15:26:08 2023, max compression
+gzip compressed data, was "molgraph-0.2.2.tar", last modified: Thu Apr  6 15:43:37 2023, max compression
```

## Comparing `molgraph-0.2.1.tar` & `molgraph-0.2.2.tar`

### file list

```diff
@@ -1,99 +1,99 @@
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/
--rw-rw-r--   0 alex      (1000) alex      (1000)     1074 2022-05-10 17:47:45.000000 molgraph-0.2.1/LICENSE
--rw-rw-r--   0 alex      (1000) alex      (1000)     3122 2023-04-06 15:26:08.813001 molgraph-0.2.1/PKG-INFO
--rw-rw-r--   0 alex      (1000) alex      (1000)     2402 2022-09-20 11:35:03.000000 molgraph-0.2.1/README.md
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.805002 molgraph-0.2.1/molgraph/
--rw-rw-r--   0 alex      (1000) alex      (1000)      408 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)      954 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/_filter_warnings.py
--rw-rw-r--   0 alex      (1000) alex      (1000)       22 2023-04-06 15:20:33.000000 molgraph-0.2.1/molgraph/_version.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/chemistry/
--rw-rw-r--   0 alex      (1000) alex      (1000)     1086 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/chemistry/__init__.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/chemistry/benchmark/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-06-29 19:00:10.000000 molgraph-0.2.1/molgraph/chemistry/benchmark/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    36677 2022-08-02 17:30:01.000000 molgraph-0.2.1/molgraph/chemistry/benchmark/configs.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    13653 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/chemistry/benchmark/datasets.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     8971 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/chemistry/benchmark/splitters.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10276 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/chemistry/benchmark/tf_records.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     2718 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/chemistry/conformer_generator.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10471 2022-08-03 19:47:51.000000 molgraph-0.2.1/molgraph/chemistry/conformer_utils.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    15266 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/chemistry/encoders.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    13722 2022-09-20 11:37:26.000000 molgraph-0.2.1/molgraph/chemistry/features.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    21456 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/chemistry/molecular_encoders.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     1840 2022-09-02 12:44:02.000000 molgraph-0.2.1/molgraph/chemistry/ops.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     2724 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/chemistry/vis.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/layers/
--rw-rw-r--   0 alex      (1000) alex      (1000)     3221 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/layers/__init__.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/layers/attentional/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:18.000000 molgraph-0.2.1/molgraph/layers/attentional/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    11266 2022-09-02 16:19:13.000000 molgraph-0.2.1/molgraph/layers/attentional/gat_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     9279 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/attentional/gated_gcn_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    11313 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/attentional/gatv2_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10527 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/attentional/gmm_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    14948 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/attentional/gt_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    12913 2022-09-14 12:21:47.000000 molgraph-0.2.1/molgraph/layers/base.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/layers/convolutional/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:16.000000 molgraph-0.2.1/molgraph/layers/convolutional/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     9916 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/convolutional/gcn_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     9754 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/convolutional/gcnii_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     7748 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/convolutional/gin_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10599 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/convolutional/graph_sage_conv.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/layers/geometric/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-06-10 12:47:57.000000 molgraph-0.2.1/molgraph/layers/geometric/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     1613 2022-09-02 11:38:53.000000 molgraph-0.2.1/molgraph/layers/geometric/_radial_basis.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     9441 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/geometric/dtnn_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10267 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/layers/geometric/gcf_conv.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/layers/message_passing/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-23 17:04:39.000000 molgraph-0.2.1/molgraph/layers/message_passing/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10904 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/message_passing/mpnn_conv.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     6486 2022-09-02 12:17:48.000000 molgraph-0.2.1/molgraph/layers/ops.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph/layers/positional_encoding/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:08.000000 molgraph-0.2.1/molgraph/layers/positional_encoding/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    10714 2022-09-14 10:36:59.000000 molgraph-0.2.1/molgraph/layers/positional_encoding/laplacian.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/layers/postprocessing/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:18:09.000000 molgraph-0.2.1/molgraph/layers/postprocessing/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     1987 2022-08-18 17:05:36.000000 molgraph-0.2.1/molgraph/layers/postprocessing/dot_product_incident.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     2008 2022-08-18 17:05:41.000000 molgraph-0.2.1/molgraph/layers/postprocessing/extract_field.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     2983 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/layers/postprocessing/gather_incident.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/layers/preprocessing/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:11.000000 molgraph-0.2.1/molgraph/layers/preprocessing/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    11055 2022-08-31 15:11:51.000000 molgraph-0.2.1/molgraph/layers/preprocessing/center_scaling.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     9439 2022-09-14 10:36:59.000000 molgraph-0.2.1/molgraph/layers/preprocessing/embedding_lookup.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    11842 2022-08-31 15:11:51.000000 molgraph-0.2.1/molgraph/layers/preprocessing/min_max_scaling.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     6616 2022-08-18 17:06:18.000000 molgraph-0.2.1/molgraph/layers/preprocessing/projection.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    20437 2022-08-31 15:11:51.000000 molgraph-0.2.1/molgraph/layers/preprocessing/standard_scaling.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/layers/readout/
--rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:24.000000 molgraph-0.2.1/molgraph/layers/readout/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     3296 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/layers/readout/segment_pool.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     6250 2022-09-14 11:22:14.000000 molgraph-0.2.1/molgraph/layers/readout/set_gather.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     5418 2022-09-14 10:36:59.000000 molgraph-0.2.1/molgraph/layers/readout/transformer_encoder.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/losses/
--rw-rw-r--   0 alex      (1000) alex      (1000)      456 2022-08-09 16:26:08.000000 molgraph-0.2.1/molgraph/losses/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     2192 2022-06-01 11:22:01.000000 molgraph-0.2.1/molgraph/losses/link_losses.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     5182 2022-08-15 09:20:55.000000 molgraph-0.2.1/molgraph/losses/masked_losses.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/metrics/
--rw-rw-r--   0 alex      (1000) alex      (1000)      342 2022-08-09 16:18:46.000000 molgraph-0.2.1/molgraph/metrics/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     2071 2022-06-01 11:25:29.000000 molgraph-0.2.1/molgraph/metrics/masked_metrics.py
--rw-rw-r--   0 alex      (1000) alex      (1000)      517 2022-06-01 11:21:46.000000 molgraph-0.2.1/molgraph/metrics/mean_relative_error.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/models/
--rw-rw-r--   0 alex      (1000) alex      (1000)      486 2023-04-06 15:13:35.000000 molgraph-0.2.1/molgraph/models/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     7327 2023-04-06 15:13:35.000000 molgraph-0.2.1/molgraph/models/dgin.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     8251 2023-04-06 15:13:35.000000 molgraph-0.2.1/molgraph/models/dmpnn.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/models/interpretability/
--rw-rw-r--   0 alex      (1000) alex      (1000)       84 2022-08-12 12:53:20.000000 molgraph-0.2.1/molgraph/models/interpretability/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)      223 2022-07-14 20:09:09.000000 molgraph-0.2.1/molgraph/models/interpretability/_filter_warnings.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     6733 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/models/interpretability/activation_maps.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    11937 2022-09-20 11:35:03.000000 molgraph-0.2.1/molgraph/models/interpretability/saliency.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     6937 2022-09-02 12:36:26.000000 molgraph-0.2.1/molgraph/models/mpnn.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.813001 molgraph-0.2.1/molgraph/tensors/
--rw-rw-r--   0 alex      (1000) alex      (1000)      184 2022-08-08 12:38:45.000000 molgraph-0.2.1/molgraph/tensors/__init__.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    22917 2022-08-05 18:22:59.000000 molgraph-0.2.1/molgraph/tensors/_graph_tensor.py
--rw-rw-r--   0 alex      (1000) alex      (1000)     1844 2022-08-18 15:00:21.000000 molgraph-0.2.1/molgraph/tensors/graph_keras_tensor.py
--rw-rw-r--   0 alex      (1000) alex      (1000)    34971 2022-09-20 10:07:50.000000 molgraph-0.2.1/molgraph/tensors/graph_tensor.py
-drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:26:08.809002 molgraph-0.2.1/molgraph.egg-info/
--rw-rw-r--   0 alex      (1000) alex      (1000)     3122 2023-04-06 15:26:08.000000 molgraph-0.2.1/molgraph.egg-info/PKG-INFO
--rw-rw-r--   0 alex      (1000) alex      (1000)     2881 2023-04-06 15:26:08.000000 molgraph-0.2.1/molgraph.egg-info/SOURCES.txt
--rw-rw-r--   0 alex      (1000) alex      (1000)        1 2023-04-06 15:26:08.000000 molgraph-0.2.1/molgraph.egg-info/dependency_links.txt
--rw-rw-r--   0 alex      (1000) alex      (1000)       62 2023-04-06 15:26:08.000000 molgraph-0.2.1/molgraph.egg-info/requires.txt
--rw-rw-r--   0 alex      (1000) alex      (1000)        9 2023-04-06 15:26:08.000000 molgraph-0.2.1/molgraph.egg-info/top_level.txt
--rw-rw-r--   0 alex      (1000) alex      (1000)       38 2023-04-06 15:26:08.813001 molgraph-0.2.1/setup.cfg
--rw-rw-r--   0 alex      (1000) alex      (1000)     1486 2022-08-24 13:27:36.000000 molgraph-0.2.1/setup.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1074 2022-05-10 17:47:45.000000 molgraph-0.2.2/LICENSE
+-rw-rw-r--   0 alex      (1000) alex      (1000)     3122 2023-04-06 15:43:37.004628 molgraph-0.2.2/PKG-INFO
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2402 2022-09-20 11:35:03.000000 molgraph-0.2.2/README.md
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:36.996628 molgraph-0.2.2/molgraph/
+-rw-rw-r--   0 alex      (1000) alex      (1000)      408 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)      954 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/_filter_warnings.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)       22 2023-04-06 15:41:44.000000 molgraph-0.2.2/molgraph/_version.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/chemistry/
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1086 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/chemistry/__init__.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/chemistry/benchmark/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-06-29 19:00:10.000000 molgraph-0.2.2/molgraph/chemistry/benchmark/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    36677 2022-08-02 17:30:01.000000 molgraph-0.2.2/molgraph/chemistry/benchmark/configs.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    13653 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/chemistry/benchmark/datasets.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     8971 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/chemistry/benchmark/splitters.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10276 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/chemistry/benchmark/tf_records.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2718 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/chemistry/conformer_generator.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10471 2022-08-03 19:47:51.000000 molgraph-0.2.2/molgraph/chemistry/conformer_utils.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    15266 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/chemistry/encoders.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    13722 2022-09-20 11:37:26.000000 molgraph-0.2.2/molgraph/chemistry/features.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    21456 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/chemistry/molecular_encoders.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1840 2022-09-02 12:44:02.000000 molgraph-0.2.2/molgraph/chemistry/ops.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2724 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/chemistry/vis.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/layers/
+-rw-rw-r--   0 alex      (1000) alex      (1000)     3221 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/layers/__init__.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/layers/attentional/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:18.000000 molgraph-0.2.2/molgraph/layers/attentional/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    11266 2022-09-02 16:19:13.000000 molgraph-0.2.2/molgraph/layers/attentional/gat_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     9279 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/attentional/gated_gcn_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    11313 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/attentional/gatv2_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10527 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/attentional/gmm_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    14948 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/attentional/gt_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    12913 2022-09-14 12:21:47.000000 molgraph-0.2.2/molgraph/layers/base.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/layers/convolutional/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:16.000000 molgraph-0.2.2/molgraph/layers/convolutional/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     9916 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/convolutional/gcn_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     9754 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/convolutional/gcnii_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     7748 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/convolutional/gin_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10599 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/convolutional/graph_sage_conv.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/layers/geometric/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-06-10 12:47:57.000000 molgraph-0.2.2/molgraph/layers/geometric/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1613 2022-09-02 11:38:53.000000 molgraph-0.2.2/molgraph/layers/geometric/_radial_basis.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     9441 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/geometric/dtnn_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10267 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/layers/geometric/gcf_conv.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/layers/message_passing/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-23 17:04:39.000000 molgraph-0.2.2/molgraph/layers/message_passing/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10904 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/message_passing/mpnn_conv.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     6486 2022-09-02 12:17:48.000000 molgraph-0.2.2/molgraph/layers/ops.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph/layers/positional_encoding/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:08.000000 molgraph-0.2.2/molgraph/layers/positional_encoding/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    10714 2022-09-14 10:36:59.000000 molgraph-0.2.2/molgraph/layers/positional_encoding/laplacian.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/layers/postprocessing/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:18:09.000000 molgraph-0.2.2/molgraph/layers/postprocessing/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1987 2022-08-18 17:05:36.000000 molgraph-0.2.2/molgraph/layers/postprocessing/dot_product_incident.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2008 2022-08-18 17:05:41.000000 molgraph-0.2.2/molgraph/layers/postprocessing/extract_field.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2983 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/layers/postprocessing/gather_incident.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/layers/preprocessing/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:11.000000 molgraph-0.2.2/molgraph/layers/preprocessing/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    11055 2022-08-31 15:11:51.000000 molgraph-0.2.2/molgraph/layers/preprocessing/center_scaling.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     9439 2022-09-14 10:36:59.000000 molgraph-0.2.2/molgraph/layers/preprocessing/embedding_lookup.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    11842 2022-08-31 15:11:51.000000 molgraph-0.2.2/molgraph/layers/preprocessing/min_max_scaling.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     6616 2022-08-18 17:06:18.000000 molgraph-0.2.2/molgraph/layers/preprocessing/projection.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    20437 2022-08-31 15:11:51.000000 molgraph-0.2.2/molgraph/layers/preprocessing/standard_scaling.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/layers/readout/
+-rw-rw-r--   0 alex      (1000) alex      (1000)        0 2022-05-10 18:07:24.000000 molgraph-0.2.2/molgraph/layers/readout/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     3296 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/layers/readout/segment_pool.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     6250 2022-09-14 11:22:14.000000 molgraph-0.2.2/molgraph/layers/readout/set_gather.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     5418 2022-09-14 10:36:59.000000 molgraph-0.2.2/molgraph/layers/readout/transformer_encoder.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/losses/
+-rw-rw-r--   0 alex      (1000) alex      (1000)      456 2022-08-09 16:26:08.000000 molgraph-0.2.2/molgraph/losses/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2192 2022-06-01 11:22:01.000000 molgraph-0.2.2/molgraph/losses/link_losses.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     5182 2022-08-15 09:20:55.000000 molgraph-0.2.2/molgraph/losses/masked_losses.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/metrics/
+-rw-rw-r--   0 alex      (1000) alex      (1000)      342 2022-08-09 16:18:46.000000 molgraph-0.2.2/molgraph/metrics/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2071 2022-06-01 11:25:29.000000 molgraph-0.2.2/molgraph/metrics/masked_metrics.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)      517 2022-06-01 11:21:46.000000 molgraph-0.2.2/molgraph/metrics/mean_relative_error.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/models/
+-rw-rw-r--   0 alex      (1000) alex      (1000)      486 2023-04-06 15:13:35.000000 molgraph-0.2.2/molgraph/models/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     7338 2023-04-06 15:41:44.000000 molgraph-0.2.2/molgraph/models/dgin.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     8254 2023-04-06 15:41:44.000000 molgraph-0.2.2/molgraph/models/dmpnn.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/models/interpretability/
+-rw-rw-r--   0 alex      (1000) alex      (1000)       84 2022-08-12 12:53:20.000000 molgraph-0.2.2/molgraph/models/interpretability/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)      223 2022-07-14 20:09:09.000000 molgraph-0.2.2/molgraph/models/interpretability/_filter_warnings.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     6733 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/models/interpretability/activation_maps.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    11937 2022-09-20 11:35:03.000000 molgraph-0.2.2/molgraph/models/interpretability/saliency.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     6937 2023-04-06 15:39:26.000000 molgraph-0.2.2/molgraph/models/mpnn.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.004628 molgraph-0.2.2/molgraph/tensors/
+-rw-rw-r--   0 alex      (1000) alex      (1000)      184 2022-08-08 12:38:45.000000 molgraph-0.2.2/molgraph/tensors/__init__.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    22917 2022-08-05 18:22:59.000000 molgraph-0.2.2/molgraph/tensors/_graph_tensor.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1844 2022-08-18 15:00:21.000000 molgraph-0.2.2/molgraph/tensors/graph_keras_tensor.py
+-rw-rw-r--   0 alex      (1000) alex      (1000)    34971 2022-09-20 10:07:50.000000 molgraph-0.2.2/molgraph/tensors/graph_tensor.py
+drwxrwxr-x   0 alex      (1000) alex      (1000)        0 2023-04-06 15:43:37.000628 molgraph-0.2.2/molgraph.egg-info/
+-rw-rw-r--   0 alex      (1000) alex      (1000)     3122 2023-04-06 15:43:36.000000 molgraph-0.2.2/molgraph.egg-info/PKG-INFO
+-rw-rw-r--   0 alex      (1000) alex      (1000)     2881 2023-04-06 15:43:36.000000 molgraph-0.2.2/molgraph.egg-info/SOURCES.txt
+-rw-rw-r--   0 alex      (1000) alex      (1000)        1 2023-04-06 15:43:36.000000 molgraph-0.2.2/molgraph.egg-info/dependency_links.txt
+-rw-rw-r--   0 alex      (1000) alex      (1000)       62 2023-04-06 15:43:36.000000 molgraph-0.2.2/molgraph.egg-info/requires.txt
+-rw-rw-r--   0 alex      (1000) alex      (1000)        9 2023-04-06 15:43:36.000000 molgraph-0.2.2/molgraph.egg-info/top_level.txt
+-rw-rw-r--   0 alex      (1000) alex      (1000)       38 2023-04-06 15:43:37.004628 molgraph-0.2.2/setup.cfg
+-rw-rw-r--   0 alex      (1000) alex      (1000)     1486 2022-08-24 13:27:36.000000 molgraph-0.2.2/setup.py
```

### Comparing `molgraph-0.2.1/LICENSE` & `molgraph-0.2.2/LICENSE`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/PKG-INFO` & `molgraph-0.2.2/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: molgraph
-Version: 0.2.1
+Version: 0.2.2
 Summary: Implementations of graph neural networks for molecular machine learning
 Home-page: https://github.com/akensert/molgraph
 Author: Alexander Kensert
 Author-email: alexander.kensert@gmail.com
 License: MIT
 Keywords: graph-neural-networks,deep-learning,machine-learning,molecular-machine-learning,molecular-graphs,cheminformatics,bioinformatics
 Classifier: Programming Language :: Python :: 3
```

### Comparing `molgraph-0.2.1/README.md` & `molgraph-0.2.2/README.md`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/_filter_warnings.py` & `molgraph-0.2.2/molgraph/_filter_warnings.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/__init__.py` & `molgraph-0.2.2/molgraph/chemistry/__init__.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/benchmark/configs.py` & `molgraph-0.2.2/molgraph/chemistry/benchmark/configs.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/benchmark/datasets.py` & `molgraph-0.2.2/molgraph/chemistry/benchmark/datasets.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/benchmark/splitters.py` & `molgraph-0.2.2/molgraph/chemistry/benchmark/splitters.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/benchmark/tf_records.py` & `molgraph-0.2.2/molgraph/chemistry/benchmark/tf_records.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/conformer_generator.py` & `molgraph-0.2.2/molgraph/chemistry/conformer_generator.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/conformer_utils.py` & `molgraph-0.2.2/molgraph/chemistry/conformer_utils.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/encoders.py` & `molgraph-0.2.2/molgraph/chemistry/encoders.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/features.py` & `molgraph-0.2.2/molgraph/chemistry/features.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/molecular_encoders.py` & `molgraph-0.2.2/molgraph/chemistry/molecular_encoders.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/ops.py` & `molgraph-0.2.2/molgraph/chemistry/ops.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/chemistry/vis.py` & `molgraph-0.2.2/molgraph/chemistry/vis.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/__init__.py` & `molgraph-0.2.2/molgraph/layers/__init__.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/attentional/gat_conv.py` & `molgraph-0.2.2/molgraph/layers/attentional/gat_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/attentional/gated_gcn_conv.py` & `molgraph-0.2.2/molgraph/layers/attentional/gated_gcn_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/attentional/gatv2_conv.py` & `molgraph-0.2.2/molgraph/layers/attentional/gatv2_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/attentional/gmm_conv.py` & `molgraph-0.2.2/molgraph/layers/attentional/gmm_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/attentional/gt_conv.py` & `molgraph-0.2.2/molgraph/layers/attentional/gt_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/base.py` & `molgraph-0.2.2/molgraph/layers/base.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/convolutional/gcn_conv.py` & `molgraph-0.2.2/molgraph/layers/convolutional/gcn_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/convolutional/gcnii_conv.py` & `molgraph-0.2.2/molgraph/layers/convolutional/gcnii_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/convolutional/gin_conv.py` & `molgraph-0.2.2/molgraph/layers/convolutional/gin_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/convolutional/graph_sage_conv.py` & `molgraph-0.2.2/molgraph/layers/convolutional/graph_sage_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/geometric/_radial_basis.py` & `molgraph-0.2.2/molgraph/layers/geometric/_radial_basis.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/geometric/dtnn_conv.py` & `molgraph-0.2.2/molgraph/layers/geometric/dtnn_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/geometric/gcf_conv.py` & `molgraph-0.2.2/molgraph/layers/geometric/gcf_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/message_passing/mpnn_conv.py` & `molgraph-0.2.2/molgraph/layers/message_passing/mpnn_conv.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/ops.py` & `molgraph-0.2.2/molgraph/layers/ops.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/positional_encoding/laplacian.py` & `molgraph-0.2.2/molgraph/layers/positional_encoding/laplacian.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/postprocessing/dot_product_incident.py` & `molgraph-0.2.2/molgraph/layers/postprocessing/dot_product_incident.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/postprocessing/extract_field.py` & `molgraph-0.2.2/molgraph/layers/postprocessing/extract_field.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/postprocessing/gather_incident.py` & `molgraph-0.2.2/molgraph/layers/postprocessing/gather_incident.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/preprocessing/center_scaling.py` & `molgraph-0.2.2/molgraph/layers/preprocessing/center_scaling.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/preprocessing/embedding_lookup.py` & `molgraph-0.2.2/molgraph/layers/preprocessing/embedding_lookup.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/preprocessing/min_max_scaling.py` & `molgraph-0.2.2/molgraph/layers/preprocessing/min_max_scaling.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/preprocessing/projection.py` & `molgraph-0.2.2/molgraph/layers/preprocessing/projection.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/preprocessing/standard_scaling.py` & `molgraph-0.2.2/molgraph/layers/preprocessing/standard_scaling.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/readout/segment_pool.py` & `molgraph-0.2.2/molgraph/layers/readout/segment_pool.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/readout/set_gather.py` & `molgraph-0.2.2/molgraph/layers/readout/set_gather.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/layers/readout/transformer_encoder.py` & `molgraph-0.2.2/molgraph/layers/readout/transformer_encoder.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/losses/link_losses.py` & `molgraph-0.2.2/molgraph/losses/link_losses.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/losses/masked_losses.py` & `molgraph-0.2.2/molgraph/losses/masked_losses.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/metrics/masked_metrics.py` & `molgraph-0.2.2/molgraph/metrics/masked_metrics.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/metrics/mean_relative_error.py` & `molgraph-0.2.2/molgraph/metrics/mean_relative_error.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/models/dgin.py` & `molgraph-0.2.2/molgraph/models/dgin.py`

 * *Files 1% similar despite different names*

```diff
@@ -33,15 +33,15 @@
     >>> # Build Functional model
     >>> inputs = tf.keras.layers.Input(type_spec=graph_tensor.unspecific_spec)
     >>> x = molgraph.models.DGIN(units=32, name='dgin')(inputs)
     >>> x = molgraph.layers.SetGatherReadout(name='readout')(x)
     >>> outputs = tf.keras.layers.Dense(10, activation='sigmoid')(x)
     >>> dgin_classifier = tf.keras.Model(inputs, outputs)
     >>> # Make predictions
-    >>> preds = dgin_classifier.predict(graph_tensor)
+    >>> preds = dgin_classifier.predict(graph_tensor, verbose=0)
     >>> preds.shape
     (2, 10)
  
     Args:
         units (int, None):
             Number of hiden units of the message passing. These include the
             dense layers associated with the message functions, and GRU cells
```

### Comparing `molgraph-0.2.1/molgraph/models/dmpnn.py` & `molgraph-0.2.2/molgraph/models/dmpnn.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,20 +26,20 @@
     ...             [[1.0, 0.0], [1.0, 0.0]],
     ...             [[1.0, 0.0], [1.0, 0.0], [0.0, 1.0]]
     ...         ],
     ...     }
     ... )
     >>> # Build Functional model
     >>> inputs = tf.keras.layers.Input(type_spec=graph_tensor.unspecific_spec)
-    >>> x = molgraph.models.MPNN(units=32, steps=4, name='dmpnn')(inputs)
+    >>> x = molgraph.models.DMPNN(units=32, name='dmpnn')(inputs)
     >>> x = molgraph.layers.SetGatherReadout(name='readout')(x)
     >>> outputs = tf.keras.layers.Dense(10, activation='sigmoid')(x)
     >>> dmpnn_classifier = tf.keras.Model(inputs, outputs)
     >>> # Make predictions
-    >>> preds = dmpnn_classifier.predict(graph_tensor)
+    >>> preds = dmpnn_classifier.predict(graph_tensor, verbose=0)
     >>> preds.shape
     (2, 10)
  
     Args:
         units (int, None):
             Number of hiden units of the message passing. These include the
             dense layers associated with the message functions, and GRU cells
```

### Comparing `molgraph-0.2.1/molgraph/models/interpretability/activation_maps.py` & `molgraph-0.2.2/molgraph/models/interpretability/activation_maps.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/models/interpretability/saliency.py` & `molgraph-0.2.2/molgraph/models/interpretability/saliency.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/models/mpnn.py` & `molgraph-0.2.2/molgraph/models/mpnn.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/tensors/_graph_tensor.py` & `molgraph-0.2.2/molgraph/tensors/_graph_tensor.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/tensors/graph_keras_tensor.py` & `molgraph-0.2.2/molgraph/tensors/graph_keras_tensor.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph/tensors/graph_tensor.py` & `molgraph-0.2.2/molgraph/tensors/graph_tensor.py`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/molgraph.egg-info/PKG-INFO` & `molgraph-0.2.2/molgraph.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: molgraph
-Version: 0.2.1
+Version: 0.2.2
 Summary: Implementations of graph neural networks for molecular machine learning
 Home-page: https://github.com/akensert/molgraph
 Author: Alexander Kensert
 Author-email: alexander.kensert@gmail.com
 License: MIT
 Keywords: graph-neural-networks,deep-learning,machine-learning,molecular-machine-learning,molecular-graphs,cheminformatics,bioinformatics
 Classifier: Programming Language :: Python :: 3
```

### Comparing `molgraph-0.2.1/molgraph.egg-info/SOURCES.txt` & `molgraph-0.2.2/molgraph.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `molgraph-0.2.1/setup.py` & `molgraph-0.2.2/setup.py`

 * *Files identical despite different names*

