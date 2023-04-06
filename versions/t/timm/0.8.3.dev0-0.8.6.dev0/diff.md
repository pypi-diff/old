# Comparing `tmp/timm-0.8.3.dev0.tar.gz` & `tmp/timm-0.8.6.dev0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "timm-0.8.3.dev0.tar", last modified: Sat Dec 24 22:39:42 2022, max compression
+gzip compressed data, was "timm-0.8.6.dev0.tar", last modified: Thu Jan 12 05:34:02 2023, max compression
```

## Comparing `timm-0.8.3.dev0.tar` & `timm-0.8.6.dev0.tar`

### file list

```diff
@@ -1,236 +1,237 @@
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.437850 timm-0.8.3.dev0/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11343 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/LICENSE
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       34 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/MANIFEST.in
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    50821 2022-12-24 22:39:42.437850 timm-0.8.3.dev0/PKG-INFO
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    49688 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/README.md
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      126 2022-12-24 22:39:42.437850 timm-0.8.3.dev0/setup.cfg
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1930 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/setup.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.413850 timm-0.8.3.dev0/timm/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      292 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/__init__.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.417850 timm-0.8.3.dev0/timm/data/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      672 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    35680 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/data/auto_augment.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3350 2022-12-05 18:23:23.000000 timm-0.8.3.dev0/timm/data/config.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      442 2022-12-05 18:23:23.000000 timm-0.8.3.dev0/timm/data/constants.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5768 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/dataset.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6923 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/data/dataset_factory.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5540 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/data/distributed_sampler.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11683 2022-12-05 18:23:23.000000 timm-0.8.3.dev0/timm/data/loader.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14722 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/data/mixup.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4964 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/random_erasing.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.417850 timm-0.8.3.dev0/timm/data/readers/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       72 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      895 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/data/readers/class_map.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1482 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/img_extensions.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      487 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/reader.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1364 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/data/readers/reader_factory.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2431 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/data/readers/reader_hfds.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3315 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/reader_image_folder.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9182 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/reader_image_in_tar.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2644 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/reader_image_tar.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    17529 2022-12-05 18:23:23.000000 timm-0.8.3.dev0/timm/data/readers/reader_tfds.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16328 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/reader_wds.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      303 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/data/readers/shared_count.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1590 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/data/real_labels.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9169 2022-12-05 18:23:23.000000 timm-0.8.3.dev0/timm/data/tf_preprocessing.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11992 2022-12-05 18:23:23.000000 timm-0.8.3.dev0/timm/data/transforms.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9840 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/data/transforms_factory.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.421850 timm-0.8.3.dev0/timm/layers/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3058 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4468 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/activations.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2529 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/activations_jit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5886 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/activations_me.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3890 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/adaptive_avgmax_pool.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4934 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/attention_pool2d.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1594 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/blur_pool.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6895 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/bottleneck_attn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4426 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/cbam.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2320 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/classifier.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5199 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/cond_conv2d.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3069 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/config.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1490 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/conv2d_same.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3188 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/conv_bn_act.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5294 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/create_act.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3514 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/create_attn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1622 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/create_conv2d.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1814 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/create_norm.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3748 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/create_norm_act.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6872 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/drop.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6386 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/eca.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13862 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/evo_norm.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2426 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/fast_norm.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2540 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/filter_response_norm.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3824 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/gather_excite.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2445 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/global_context.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10662 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/halo_attn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1053 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/helpers.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3374 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/inplace_abn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5941 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/lambda_layer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      743 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/linear.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1737 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/median_pool.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1843 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/mixed_conv2d.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7008 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/ml_decoder.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4376 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/mlp.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6218 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/non_local_attn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4519 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/norm.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10397 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/norm_act.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2167 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/padding.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6371 2022-12-24 22:38:03.000000 timm-0.8.3.dev0/timm/layers/patch_embed.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3045 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/pool2d_same.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1644 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/pos_embed.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11619 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/pos_embed_rel.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7316 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/pos_embed_sincos.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5387 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/selective_kernel.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2620 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/separable_conv.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1750 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/space_to_depth.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3076 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/split_attn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3441 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/split_batchnorm.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4327 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/squeeze_excite.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5887 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/std_conv.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1996 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/test_time_pool.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      335 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/trace_utils.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4765 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/layers/weight_init.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.421850 timm-0.8.3.dev0/timm/loss/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      245 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/loss/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3343 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/loss/asymmetric_loss.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2030 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/loss/binary_cross_entropy.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1145 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/loss/cross_entropy.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1595 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/loss/jsd.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.429850 timm-0.8.3.dev0/timm/models/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2823 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    17170 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_builder.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12148 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_efficientnet_blocks.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    19879 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_efficientnet_builder.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4467 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_factory.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12234 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_features.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4345 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_features_fx.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4938 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_helpers.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9377 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_hub.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10086 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_manipulate.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4365 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_pretrained.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4178 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_prune.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9007 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/_registry.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    23325 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/beit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18309 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/byoanet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    64062 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/byobnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16229 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/cait.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    27989 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/coat.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14667 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/convit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4433 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/convmixer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    25666 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/convnext.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    23354 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/crossvit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    38463 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/cspnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    19845 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/deit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16133 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/densenet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18951 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/dla.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13107 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/dpn.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    21517 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/edgenext.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18546 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/efficientformer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    96066 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/efficientnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      150 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/factory.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      151 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/features.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      154 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/fx_features.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    21273 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/gcvit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10098 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/ghostnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11322 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/gluon_resnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9255 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/gluon_xception.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     8115 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/hardcorenas.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      223 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/helpers.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    30236 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/hrnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      145 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/hub.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13508 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/inception_resnet_v2.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18301 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/inception_v3.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11220 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/inception_v4.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.429850 timm-0.8.3.dev0/timm/models/layers/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3432 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/layers/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    22497 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/levit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    78242 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/maxxvit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    26864 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/mlp_mixer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    29987 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/mobilenetv3.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    27391 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/mobilevit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    34836 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/mvitv2.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    26534 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/nasnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    20207 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/nest.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    37893 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/nfnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13963 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/pit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    15346 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/pnasnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11257 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/poolformer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16851 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/pvt_v2.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      151 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/registry.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    32565 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/regnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7792 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/res2net.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9913 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/resnest.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    72786 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/resnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    30131 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/resnetv2.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9973 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/rexnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13561 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/selecsls.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    17993 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/senet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14970 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/sequencer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     8432 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/sknet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    29383 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/swin_transformer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    31576 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/swin_transformer_v2.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    41530 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/swin_transformer_v2_cr.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12352 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/tnt.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12782 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/tresnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18273 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/twins.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10988 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/vgg.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16634 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/visformer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    72700 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/vision_transformer.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14496 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/vision_transformer_hybrid.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    21513 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/vision_transformer_relpos.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    28244 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/volo.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14457 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/vovnet.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7901 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/xception.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13727 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/xception_aligned.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    36901 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/models/xcit.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.429850 timm-0.8.3.dev0/timm/optim/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      507 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/optim/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9827 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/adabelief.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7459 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/adafactor.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6535 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/adahessian.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3574 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/adamp.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5147 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/adamw.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5071 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/optim/adan.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9184 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/lamb.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5256 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/lars.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2463 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/lookahead.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6893 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/madgrad.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3871 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/nadam.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4856 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/nvnovograd.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12682 2022-12-24 00:11:50.000000 timm-0.8.3.dev0/timm/optim/optim_factory.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3468 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/radam.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6143 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/rmsprop_tf.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2296 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/optim/sgdp.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.433850 timm-0.8.3.dev0/timm/scheduler/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      330 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3843 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/cosine_lr.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1930 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/multistep_lr.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3573 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/plateau_lr.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3673 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/poly_lr.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5408 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/scheduler.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6622 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/scheduler_factory.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1732 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/step_lr.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3607 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/scheduler/tanh_lr.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.437850 timm-0.8.3.dev0/timm/utils/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      751 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/utils/__init__.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1624 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/agc.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6133 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/checkpoint_saver.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      796 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/clip_grad.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1703 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/cuda.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1762 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/decay_batch.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4256 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/utils/distributed.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2203 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/jit.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1015 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/log.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      901 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/metrics.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      644 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/misc.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12085 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/model.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5670 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/model_ema.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      178 2022-10-03 21:35:12.000000 timm-0.8.3.dev0/timm/utils/random.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1300 2022-11-23 22:16:11.000000 timm-0.8.3.dev0/timm/utils/summary.py
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       26 2022-12-24 22:38:03.000000 timm-0.8.3.dev0/timm/version.py
-drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2022-12-24 22:39:42.413850 timm-0.8.3.dev0/timm.egg-info/
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    50821 2022-12-24 22:39:42.000000 timm-0.8.3.dev0/timm.egg-info/PKG-INFO
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5648 2022-12-24 22:39:42.000000 timm-0.8.3.dev0/timm.egg-info/SOURCES.txt
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)        1 2022-12-24 22:39:42.000000 timm-0.8.3.dev0/timm.egg-info/dependency_links.txt
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       46 2022-12-24 22:39:42.000000 timm-0.8.3.dev0/timm.egg-info/requires.txt
--rw-rw-r--   0 wiggs     (1000) wiggs     (1000)        5 2022-12-24 22:39:42.000000 timm-0.8.3.dev0/timm.egg-info/top_level.txt
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.058302 timm-0.8.6.dev0/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11343 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/LICENSE
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       34 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/MANIFEST.in
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    48089 2023-01-12 05:34:02.058302 timm-0.8.6.dev0/PKG-INFO
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    46956 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/README.md
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      126 2023-01-12 05:34:02.058302 timm-0.8.6.dev0/setup.cfg
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1930 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/setup.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.014302 timm-0.8.6.dev0/timm/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      292 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/__init__.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.014302 timm-0.8.6.dev0/timm/data/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      672 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    35635 2023-01-05 22:31:53.000000 timm-0.8.6.dev0/timm/data/auto_augment.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3350 2022-12-05 18:23:23.000000 timm-0.8.6.dev0/timm/data/config.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      442 2022-12-05 18:23:23.000000 timm-0.8.6.dev0/timm/data/constants.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5768 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/dataset.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6923 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/data/dataset_factory.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5540 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/data/distributed_sampler.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11683 2022-12-05 18:23:23.000000 timm-0.8.6.dev0/timm/data/loader.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14722 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/data/mixup.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4964 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/random_erasing.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.018302 timm-0.8.6.dev0/timm/data/readers/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       72 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      895 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/data/readers/class_map.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1482 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/img_extensions.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      487 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/reader.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1364 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/data/readers/reader_factory.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2431 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/data/readers/reader_hfds.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3315 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/reader_image_folder.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9182 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/reader_image_in_tar.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2644 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/reader_image_tar.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    17529 2022-12-05 18:23:23.000000 timm-0.8.6.dev0/timm/data/readers/reader_tfds.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16328 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/reader_wds.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      303 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/data/readers/shared_count.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1590 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/data/real_labels.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9169 2022-12-05 18:23:23.000000 timm-0.8.6.dev0/timm/data/tf_preprocessing.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11992 2022-12-05 18:23:23.000000 timm-0.8.6.dev0/timm/data/transforms.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9840 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/data/transforms_factory.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.030302 timm-0.8.6.dev0/timm/layers/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3081 2023-01-05 22:31:53.000000 timm-0.8.6.dev0/timm/layers/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4468 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/activations.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2529 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/activations_jit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5886 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/activations_me.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3890 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/adaptive_avgmax_pool.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4934 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/attention_pool2d.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1594 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/blur_pool.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6895 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/bottleneck_attn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4426 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/cbam.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2320 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/classifier.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5199 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/cond_conv2d.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3069 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/config.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1490 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/conv2d_same.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3188 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/conv_bn_act.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5294 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/create_act.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3514 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/create_attn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1622 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/create_conv2d.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1814 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/create_norm.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3748 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/create_norm_act.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6872 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/drop.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6386 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/eca.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13862 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/evo_norm.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2426 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/fast_norm.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2540 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/filter_response_norm.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3824 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/gather_excite.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2445 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/global_context.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1319 2023-01-05 22:31:53.000000 timm-0.8.6.dev0/timm/layers/grn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10662 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/halo_attn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1053 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/helpers.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3374 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/inplace_abn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5941 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/lambda_layer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      743 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/linear.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1737 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/median_pool.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1843 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/mixed_conv2d.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7008 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/ml_decoder.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6277 2023-01-05 22:31:53.000000 timm-0.8.6.dev0/timm/layers/mlp.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6218 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/non_local_attn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4519 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/norm.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10397 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/norm_act.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2167 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/padding.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6371 2022-12-24 22:38:03.000000 timm-0.8.6.dev0/timm/layers/patch_embed.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3045 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/pool2d_same.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1644 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/pos_embed.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11619 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/pos_embed_rel.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7316 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/pos_embed_sincos.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5387 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/selective_kernel.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2620 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/separable_conv.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1750 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/space_to_depth.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3076 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/split_attn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3441 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/split_batchnorm.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4327 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/squeeze_excite.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5887 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/std_conv.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1996 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/test_time_pool.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      335 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/trace_utils.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4765 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/layers/weight_init.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.030302 timm-0.8.6.dev0/timm/loss/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      245 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/loss/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3343 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/loss/asymmetric_loss.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2030 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/loss/binary_cross_entropy.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1145 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/loss/cross_entropy.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1595 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/loss/jsd.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.050302 timm-0.8.6.dev0/timm/models/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2823 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    17170 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_builder.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12148 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_efficientnet_blocks.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    19879 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_efficientnet_builder.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4467 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_factory.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12234 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_features.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4345 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_features_fx.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4938 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_helpers.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10107 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/_hub.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10086 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_manipulate.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4365 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_pretrained.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4178 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_prune.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9007 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/_registry.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    23325 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/beit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18309 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/byoanet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    66406 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/byobnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16229 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/cait.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    27989 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/coat.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14667 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/convit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4433 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/convmixer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    38533 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/convnext.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    23354 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/crossvit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    39245 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/cspnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    19845 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/deit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16375 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/densenet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18951 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/dla.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13911 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/dpn.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    21517 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/edgenext.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18546 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/efficientformer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    96066 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/efficientnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      150 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/factory.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      151 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/features.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      154 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/fx_features.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    21273 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/gcvit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10098 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/ghostnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11322 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/gluon_resnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9255 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/gluon_xception.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     8115 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/hardcorenas.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      223 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/helpers.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    30236 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/hrnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      145 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/hub.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13508 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/inception_resnet_v2.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18301 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/inception_v3.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11220 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/inception_v4.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.050302 timm-0.8.6.dev0/timm/models/layers/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3432 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/layers/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    22497 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/levit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    79967 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/maxxvit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    26864 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/mlp_mixer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    29987 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/mobilenetv3.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    27501 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/mobilevit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    34836 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/mvitv2.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    26534 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/nasnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    20207 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/nest.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    39482 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/nfnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13963 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/pit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    15346 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/pnasnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    11257 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/poolformer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16851 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/pvt_v2.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      151 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/registry.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    33921 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/regnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     8034 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/res2net.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10221 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/resnest.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    75381 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/resnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    33117 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/resnetv2.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9973 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/rexnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13561 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/selecsls.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    17993 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/senet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14970 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/sequencer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     8914 2023-01-05 22:31:53.000000 timm-0.8.6.dev0/timm/models/sknet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    29383 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/swin_transformer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    31576 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/swin_transformer_v2.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    41530 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/swin_transformer_v2_cr.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12352 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/tnt.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12782 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/tresnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    18273 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/twins.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    10988 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/vgg.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    16634 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/visformer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    72952 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/vision_transformer.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    14496 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/vision_transformer_hybrid.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    21513 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/vision_transformer_relpos.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    28244 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/volo.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    15639 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/models/vovnet.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7901 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/xception.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    13727 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/xception_aligned.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    36901 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/models/xcit.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.054302 timm-0.8.6.dev0/timm/optim/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      507 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/optim/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9827 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/adabelief.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     7459 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/adafactor.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6535 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/adahessian.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3574 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/adamp.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5147 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/adamw.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5071 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/optim/adan.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     9184 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/lamb.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5256 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/lars.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2463 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/lookahead.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6893 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/madgrad.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3871 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/nadam.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4856 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/nvnovograd.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12682 2022-12-24 00:11:50.000000 timm-0.8.6.dev0/timm/optim/optim_factory.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3468 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/radam.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6143 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/rmsprop_tf.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2296 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/optim/sgdp.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.054302 timm-0.8.6.dev0/timm/scheduler/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      330 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3843 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/cosine_lr.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1930 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/multistep_lr.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3573 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/plateau_lr.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3673 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/poly_lr.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5408 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/scheduler.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6622 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/scheduler_factory.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1732 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/step_lr.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     3607 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/scheduler/tanh_lr.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.058302 timm-0.8.6.dev0/timm/utils/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      764 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/utils/__init__.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1624 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/agc.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     6133 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/checkpoint_saver.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      796 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/clip_grad.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1703 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/cuda.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1762 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/decay_batch.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     4256 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/utils/distributed.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     2203 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/jit.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1015 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/log.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      901 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/metrics.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1105 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/utils/misc.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    12085 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/model.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5670 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/model_ema.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)      178 2022-10-03 21:35:12.000000 timm-0.8.6.dev0/timm/utils/random.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     1300 2022-11-23 22:16:11.000000 timm-0.8.6.dev0/timm/utils/summary.py
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       26 2023-01-12 05:33:28.000000 timm-0.8.6.dev0/timm/version.py
+drwxrwxr-x   0 wiggs     (1000) wiggs     (1000)        0 2023-01-12 05:34:02.014302 timm-0.8.6.dev0/timm.egg-info/
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)    48089 2023-01-12 05:34:01.000000 timm-0.8.6.dev0/timm.egg-info/PKG-INFO
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)     5667 2023-01-12 05:34:01.000000 timm-0.8.6.dev0/timm.egg-info/SOURCES.txt
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)        1 2023-01-12 05:34:01.000000 timm-0.8.6.dev0/timm.egg-info/dependency_links.txt
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)       46 2023-01-12 05:34:01.000000 timm-0.8.6.dev0/timm.egg-info/requires.txt
+-rw-rw-r--   0 wiggs     (1000) wiggs     (1000)        5 2023-01-12 05:34:01.000000 timm-0.8.6.dev0/timm.egg-info/top_level.txt
```

### Comparing `timm-0.8.3.dev0/LICENSE` & `timm-0.8.6.dev0/LICENSE`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/PKG-INFO` & `timm-0.8.6.dev0/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,33 +1,7 @@
-Metadata-Version: 2.1
-Name: timm
-Version: 0.8.3.dev0
-Summary: (Unofficial) PyTorch Image Models
-Home-page: https://github.com/rwightman/pytorch-image-models
-Author: Ross Wightman
-Author-email: hello@rwightman.com
-Keywords: pytorch pretrained models efficientnet mobilenetv3 mnasnet resnet vision transformer vit
-Classifier: Development Status :: 4 - Beta
-Classifier: Intended Audience :: Education
-Classifier: Intended Audience :: Science/Research
-Classifier: License :: OSI Approved :: Apache Software License
-Classifier: Programming Language :: Python :: 3.6
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: Topic :: Scientific/Engineering
-Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
-Classifier: Topic :: Software Development
-Classifier: Topic :: Software Development :: Libraries
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Requires-Python: >=3.6
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
 # PyTorch Image Models
 - [Sponsors](#sponsors)
 - [What's New](#whats-new)
 - [Introduction](#introduction)
 - [Models](#models)
 - [Features](#features)
 - [Results](#results)
@@ -43,20 +17,33 @@
 * TPU Research Cloud (TRC) (https://sites.research.google/trc/about/)
 * Nvidia (https://www.nvidia.com/en-us/)
 
 And a big thanks to all GitHub sponsors who helped with some of my costs before I joined Hugging Face.
 
 ## What's New
 
-### 🤗 Survey: Feedback Appreciated 🤗
-
-For a few months now, `timm` has been part of the Hugging Face ecosystem. Yearly, we survey users of our tools to see what we could do better, what we need to continue doing, or what we need to stop doing. 
+* ❗Updates after Oct 10, 2022 are available in 0.8.x pre-releases (`pip install --pre timm`) or cloning main❗
+* Stable releases are 0.6.x and available by normal pip install or clone from [0.6.x](https://github.com/rwightman/pytorch-image-models/tree/0.6.x) branch.
 
-If you have a couple of minutes and want to participate in shaping the future of the ecosystem, please share your thoughts:
-[**hf.co/oss-survey**](https://hf.co/oss-survey) 🙏
+### Jan 11, 2023
+* Update ConvNeXt ImageNet-12k pretrain series w/ two new fine-tuned weights (and pre FT `.in12k` tags)
+  * `convnext_nano.in12k_ft_in1k` - 82.3 @ 224, 82.9 @ 288  (previously released)
+  * `convnext_tiny.in12k_ft_in1k` - 84.2 @ 224, 84.5 @ 288
+  * `convnext_small.in12k_ft_in1k` - 85.2 @ 224, 85.3 @ 288
+
+### Jan 6, 2023
+* Finally got around to adding `--model-kwargs` and `--opt-kwargs` to scripts to pass through rare args directly to model classes from cmd line
+  * `train.py /imagenet --model resnet50 --amp --model-kwargs output_stride=16 act_layer=silu`
+  * `train.py /imagenet --model vit_base_patch16_clip_224 --img-size 240 --amp --model-kwargs img_size=240 patch_size=12`
+* Cleanup some popular models to better support arg passthrough / merge with model configs, more to go. 
+
+### Jan 5, 2023
+* ConvNeXt-V2 models and weights added to existing `convnext.py`
+  * Paper: [ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](http://arxiv.org/abs/2301.00808)
+  * Reference impl: https://github.com/facebookresearch/ConvNeXt-V2 (NOTE: weights currently CC-BY-NC)
 
 ### Dec 23, 2022 🎄☃
 * Add FlexiViT models and weights from https://github.com/google-research/big_vision (check out paper at https://arxiv.org/abs/2212.08013)
   * NOTE currently resizing is static on model creation, on-the-fly dynamic / train patch size sampling is a WIP
 * Many more models updated to multi-weight and downloadable via HF hub now (convnext, efficientnet, mobilenet, vision_transformer*, beit)
 * More model pretrained tag and adjustments, some model names changed (working on deprecation translations, consider main branch DEV branch right now, use 0.6.x for stable use)
 * More ImageNet-12k (subset of 22k) pretrain models popping up:
@@ -358,54 +345,14 @@
   * `mobilenetv2_050` - 65.9
   * `lcnet_100/075/050` - 72.1 / 68.8 / 63.1
   * `semnasnet_075` - 73
   * `fbnetv3_b/d/g` - 79.1 / 79.7 / 82.0
 * TinyNet models added by [rsomani95](https://github.com/rsomani95)
 * LCNet added via MobileNetV3 architecture
 
-### Nov 22, 2021
-* A number of updated weights anew new model defs
-  * `eca_halonext26ts` - 79.5 @ 256
-  * `resnet50_gn` (new) - 80.1 @ 224, 81.3 @ 288
-  * `resnet50` - 80.7 @ 224, 80.9 @ 288 (trained at 176, not replacing current a1 weights as default since these don't scale as well to higher res, [weights](https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/resnet50_a1h2_176-001a1197.pth))
-  * `resnext50_32x4d` - 81.1 @ 224, 82.0 @ 288
-  * `sebotnet33ts_256` (new) - 81.2 @ 224
-  * `lamhalobotnet50ts_256` - 81.5 @ 256
-  * `halonet50ts` - 81.7 @ 256
-  * `halo2botnet50ts_256` - 82.0 @ 256
-  * `resnet101` - 82.0 @ 224, 82.8 @ 288
-  * `resnetv2_101` (new) - 82.1 @ 224, 83.0 @ 288
-  * `resnet152` - 82.8 @ 224, 83.5 @ 288
-  * `regnetz_d8` (new) - 83.5 @ 256, 84.0 @ 320
-  * `regnetz_e8` (new) - 84.5 @ 256, 85.0 @ 320
-* `vit_base_patch8_224` (85.8 top-1) & `in21k` variant weights added thanks [Martins Bruveris](https://github.com/martinsbruveris)
-* Groundwork in for FX feature extraction thanks to [Alexander Soare](https://github.com/alexander-soare)
-  * models updated for tracing compatibility (almost full support with some distlled transformer exceptions)
-
-### Oct 19, 2021
-* ResNet strikes back (https://arxiv.org/abs/2110.00476) weights added, plus any extra training components used. Model weights and some more details here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-rsb-weights)
-* BCE loss and Repeated Augmentation support for RSB paper
-* 4 series of ResNet based attention model experiments being added (implemented across byobnet.py/byoanet.py). These include all sorts of attention, from channel attn like SE, ECA to 2D QKV self-attention layers such as Halo, Bottlneck, Lambda. Details here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-attn-weights)
-* Working implementations of the following 2D self-attention modules (likely to be differences from paper or eventual official impl):
-  * Halo (https://arxiv.org/abs/2103.12731)
-  * Bottleneck Transformer (https://arxiv.org/abs/2101.11605)
-  * LambdaNetworks (https://arxiv.org/abs/2102.08602)
-* A RegNetZ series of models with some attention experiments (being added to). These do not follow the paper (https://arxiv.org/abs/2103.06877) in any way other than block architecture, details of official models are not available. See more here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-attn-weights)
-* ConvMixer (https://openreview.net/forum?id=TVHS5Y4dNvM), CrossVit (https://arxiv.org/abs/2103.14899), and BeiT (https://arxiv.org/abs/2106.08254) architectures + weights added
-* freeze/unfreeze helpers by [Alexander Soare](https://github.com/alexander-soare)
-
-### Aug 18, 2021
-* Optimizer bonanza!
-  * Add LAMB and LARS optimizers, incl trust ratio clipping options. Tweaked to work properly in PyTorch XLA (tested on TPUs w/ `timm bits` [branch](https://github.com/rwightman/pytorch-image-models/tree/bits_and_tpu/timm/bits))
-  * Add MADGRAD from FB research w/ a few tweaks (decoupled decay option, step handling that works with PyTorch XLA)
-  * Some cleanup on all optimizers and factory. No more `.data`, a bit more consistency, unit tests for all!
-  * SGDP and AdamP still won't work with PyTorch XLA but others should (have yet to test Adabelief, Adafactor, Adahessian myself).
-* EfficientNet-V2 XL TF ported weights added, but they don't validate well in PyTorch (L is better). The pre-processing for the V2 TF training is a bit diff and the fine-tuned 21k -> 1k weights are very sensitive and less robust than the 1k weights.
-* Added PyTorch trained EfficientNet-V2 'Tiny' w/ GlobalContext attn weights. Only .1-.2 top-1 better than the SE so more of a curiosity for those interested.
-
 ## Introduction
 
 Py**T**orch **Im**age **M**odels (`timm`) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.
 
 The work of many others is present here. I've tried to make sure all source material is acknowledged via links to github, arxiv papers, etc in the README, documentation, and code docstrings. Please let me know if I missed anything.
 
 ## Models
@@ -418,14 +365,15 @@
 * BEiT - https://arxiv.org/abs/2106.08254
 * Big Transfer ResNetV2 (BiT) - https://arxiv.org/abs/1912.11370
 * Bottleneck Transformers - https://arxiv.org/abs/2101.11605
 * CaiT (Class-Attention in Image Transformers) - https://arxiv.org/abs/2103.17239
 * CoaT (Co-Scale Conv-Attentional Image Transformers) - https://arxiv.org/abs/2104.06399
 * CoAtNet (Convolution and Attention) - https://arxiv.org/abs/2106.04803
 * ConvNeXt - https://arxiv.org/abs/2201.03545
+* ConvNeXt-V2 - http://arxiv.org/abs/2301.00808
 * ConViT (Soft Convolutional Inductive Biases Vision Transformers)- https://arxiv.org/abs/2103.10697
 * CspNet (Cross-Stage Partial Networks) - https://arxiv.org/abs/1911.11929
 * DeiT - https://arxiv.org/abs/2012.12877
 * DeiT-III - https://arxiv.org/pdf/2204.07118.pdf
 * DenseNet - https://arxiv.org/abs/1608.06993
 * DLA - https://arxiv.org/abs/1707.06484
 * DPN (Dual-Path Network) - https://arxiv.org/abs/1707.01629
@@ -440,14 +388,15 @@
     * FBNet-C - https://arxiv.org/abs/1812.03443
     * MixNet - https://arxiv.org/abs/1907.09595
     * MNASNet B1, A1 (Squeeze-Excite), and Small - https://arxiv.org/abs/1807.11626
     * MobileNet-V2 - https://arxiv.org/abs/1801.04381
     * Single-Path NAS - https://arxiv.org/abs/1904.02877
     * TinyNet - https://arxiv.org/abs/2010.14819
 * EVA - https://arxiv.org/abs/2211.07636
+* FlexiViT - https://arxiv.org/abs/2212.08013
 * GCViT (Global Context Vision Transformer) - https://arxiv.org/abs/2206.09959
 * GhostNet - https://arxiv.org/abs/1911.11907
 * gMLP - https://arxiv.org/abs/2105.08050
 * GPU-Efficient Networks - https://arxiv.org/abs/2006.14090
 * Halo Nets - https://arxiv.org/abs/2103.12731
 * HRNet - https://arxiv.org/abs/1908.07919
 * Inception-V3 - https://arxiv.org/abs/1512.00567
```

### Comparing `timm-0.8.3.dev0/README.md` & `timm-0.8.6.dev0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,33 @@
+Metadata-Version: 2.1
+Name: timm
+Version: 0.8.6.dev0
+Summary: (Unofficial) PyTorch Image Models
+Home-page: https://github.com/rwightman/pytorch-image-models
+Author: Ross Wightman
+Author-email: hello@rwightman.com
+Keywords: pytorch pretrained models efficientnet mobilenetv3 mnasnet resnet vision transformer vit
+Classifier: Development Status :: 4 - Beta
+Classifier: Intended Audience :: Education
+Classifier: Intended Audience :: Science/Research
+Classifier: License :: OSI Approved :: Apache Software License
+Classifier: Programming Language :: Python :: 3.6
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Topic :: Scientific/Engineering
+Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
+Classifier: Topic :: Software Development
+Classifier: Topic :: Software Development :: Libraries
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Requires-Python: >=3.6
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
 # PyTorch Image Models
 - [Sponsors](#sponsors)
 - [What's New](#whats-new)
 - [Introduction](#introduction)
 - [Models](#models)
 - [Features](#features)
 - [Results](#results)
@@ -17,20 +43,33 @@
 * TPU Research Cloud (TRC) (https://sites.research.google/trc/about/)
 * Nvidia (https://www.nvidia.com/en-us/)
 
 And a big thanks to all GitHub sponsors who helped with some of my costs before I joined Hugging Face.
 
 ## What's New
 
-### 🤗 Survey: Feedback Appreciated 🤗
-
-For a few months now, `timm` has been part of the Hugging Face ecosystem. Yearly, we survey users of our tools to see what we could do better, what we need to continue doing, or what we need to stop doing. 
+* ❗Updates after Oct 10, 2022 are available in 0.8.x pre-releases (`pip install --pre timm`) or cloning main❗
+* Stable releases are 0.6.x and available by normal pip install or clone from [0.6.x](https://github.com/rwightman/pytorch-image-models/tree/0.6.x) branch.
 
-If you have a couple of minutes and want to participate in shaping the future of the ecosystem, please share your thoughts:
-[**hf.co/oss-survey**](https://hf.co/oss-survey) 🙏
+### Jan 11, 2023
+* Update ConvNeXt ImageNet-12k pretrain series w/ two new fine-tuned weights (and pre FT `.in12k` tags)
+  * `convnext_nano.in12k_ft_in1k` - 82.3 @ 224, 82.9 @ 288  (previously released)
+  * `convnext_tiny.in12k_ft_in1k` - 84.2 @ 224, 84.5 @ 288
+  * `convnext_small.in12k_ft_in1k` - 85.2 @ 224, 85.3 @ 288
+
+### Jan 6, 2023
+* Finally got around to adding `--model-kwargs` and `--opt-kwargs` to scripts to pass through rare args directly to model classes from cmd line
+  * `train.py /imagenet --model resnet50 --amp --model-kwargs output_stride=16 act_layer=silu`
+  * `train.py /imagenet --model vit_base_patch16_clip_224 --img-size 240 --amp --model-kwargs img_size=240 patch_size=12`
+* Cleanup some popular models to better support arg passthrough / merge with model configs, more to go. 
+
+### Jan 5, 2023
+* ConvNeXt-V2 models and weights added to existing `convnext.py`
+  * Paper: [ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](http://arxiv.org/abs/2301.00808)
+  * Reference impl: https://github.com/facebookresearch/ConvNeXt-V2 (NOTE: weights currently CC-BY-NC)
 
 ### Dec 23, 2022 🎄☃
 * Add FlexiViT models and weights from https://github.com/google-research/big_vision (check out paper at https://arxiv.org/abs/2212.08013)
   * NOTE currently resizing is static on model creation, on-the-fly dynamic / train patch size sampling is a WIP
 * Many more models updated to multi-weight and downloadable via HF hub now (convnext, efficientnet, mobilenet, vision_transformer*, beit)
 * More model pretrained tag and adjustments, some model names changed (working on deprecation translations, consider main branch DEV branch right now, use 0.6.x for stable use)
 * More ImageNet-12k (subset of 22k) pretrain models popping up:
@@ -332,54 +371,14 @@
   * `mobilenetv2_050` - 65.9
   * `lcnet_100/075/050` - 72.1 / 68.8 / 63.1
   * `semnasnet_075` - 73
   * `fbnetv3_b/d/g` - 79.1 / 79.7 / 82.0
 * TinyNet models added by [rsomani95](https://github.com/rsomani95)
 * LCNet added via MobileNetV3 architecture
 
-### Nov 22, 2021
-* A number of updated weights anew new model defs
-  * `eca_halonext26ts` - 79.5 @ 256
-  * `resnet50_gn` (new) - 80.1 @ 224, 81.3 @ 288
-  * `resnet50` - 80.7 @ 224, 80.9 @ 288 (trained at 176, not replacing current a1 weights as default since these don't scale as well to higher res, [weights](https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/resnet50_a1h2_176-001a1197.pth))
-  * `resnext50_32x4d` - 81.1 @ 224, 82.0 @ 288
-  * `sebotnet33ts_256` (new) - 81.2 @ 224
-  * `lamhalobotnet50ts_256` - 81.5 @ 256
-  * `halonet50ts` - 81.7 @ 256
-  * `halo2botnet50ts_256` - 82.0 @ 256
-  * `resnet101` - 82.0 @ 224, 82.8 @ 288
-  * `resnetv2_101` (new) - 82.1 @ 224, 83.0 @ 288
-  * `resnet152` - 82.8 @ 224, 83.5 @ 288
-  * `regnetz_d8` (new) - 83.5 @ 256, 84.0 @ 320
-  * `regnetz_e8` (new) - 84.5 @ 256, 85.0 @ 320
-* `vit_base_patch8_224` (85.8 top-1) & `in21k` variant weights added thanks [Martins Bruveris](https://github.com/martinsbruveris)
-* Groundwork in for FX feature extraction thanks to [Alexander Soare](https://github.com/alexander-soare)
-  * models updated for tracing compatibility (almost full support with some distlled transformer exceptions)
-
-### Oct 19, 2021
-* ResNet strikes back (https://arxiv.org/abs/2110.00476) weights added, plus any extra training components used. Model weights and some more details here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-rsb-weights)
-* BCE loss and Repeated Augmentation support for RSB paper
-* 4 series of ResNet based attention model experiments being added (implemented across byobnet.py/byoanet.py). These include all sorts of attention, from channel attn like SE, ECA to 2D QKV self-attention layers such as Halo, Bottlneck, Lambda. Details here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-attn-weights)
-* Working implementations of the following 2D self-attention modules (likely to be differences from paper or eventual official impl):
-  * Halo (https://arxiv.org/abs/2103.12731)
-  * Bottleneck Transformer (https://arxiv.org/abs/2101.11605)
-  * LambdaNetworks (https://arxiv.org/abs/2102.08602)
-* A RegNetZ series of models with some attention experiments (being added to). These do not follow the paper (https://arxiv.org/abs/2103.06877) in any way other than block architecture, details of official models are not available. See more here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-attn-weights)
-* ConvMixer (https://openreview.net/forum?id=TVHS5Y4dNvM), CrossVit (https://arxiv.org/abs/2103.14899), and BeiT (https://arxiv.org/abs/2106.08254) architectures + weights added
-* freeze/unfreeze helpers by [Alexander Soare](https://github.com/alexander-soare)
-
-### Aug 18, 2021
-* Optimizer bonanza!
-  * Add LAMB and LARS optimizers, incl trust ratio clipping options. Tweaked to work properly in PyTorch XLA (tested on TPUs w/ `timm bits` [branch](https://github.com/rwightman/pytorch-image-models/tree/bits_and_tpu/timm/bits))
-  * Add MADGRAD from FB research w/ a few tweaks (decoupled decay option, step handling that works with PyTorch XLA)
-  * Some cleanup on all optimizers and factory. No more `.data`, a bit more consistency, unit tests for all!
-  * SGDP and AdamP still won't work with PyTorch XLA but others should (have yet to test Adabelief, Adafactor, Adahessian myself).
-* EfficientNet-V2 XL TF ported weights added, but they don't validate well in PyTorch (L is better). The pre-processing for the V2 TF training is a bit diff and the fine-tuned 21k -> 1k weights are very sensitive and less robust than the 1k weights.
-* Added PyTorch trained EfficientNet-V2 'Tiny' w/ GlobalContext attn weights. Only .1-.2 top-1 better than the SE so more of a curiosity for those interested.
-
 ## Introduction
 
 Py**T**orch **Im**age **M**odels (`timm`) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.
 
 The work of many others is present here. I've tried to make sure all source material is acknowledged via links to github, arxiv papers, etc in the README, documentation, and code docstrings. Please let me know if I missed anything.
 
 ## Models
@@ -392,14 +391,15 @@
 * BEiT - https://arxiv.org/abs/2106.08254
 * Big Transfer ResNetV2 (BiT) - https://arxiv.org/abs/1912.11370
 * Bottleneck Transformers - https://arxiv.org/abs/2101.11605
 * CaiT (Class-Attention in Image Transformers) - https://arxiv.org/abs/2103.17239
 * CoaT (Co-Scale Conv-Attentional Image Transformers) - https://arxiv.org/abs/2104.06399
 * CoAtNet (Convolution and Attention) - https://arxiv.org/abs/2106.04803
 * ConvNeXt - https://arxiv.org/abs/2201.03545
+* ConvNeXt-V2 - http://arxiv.org/abs/2301.00808
 * ConViT (Soft Convolutional Inductive Biases Vision Transformers)- https://arxiv.org/abs/2103.10697
 * CspNet (Cross-Stage Partial Networks) - https://arxiv.org/abs/1911.11929
 * DeiT - https://arxiv.org/abs/2012.12877
 * DeiT-III - https://arxiv.org/pdf/2204.07118.pdf
 * DenseNet - https://arxiv.org/abs/1608.06993
 * DLA - https://arxiv.org/abs/1707.06484
 * DPN (Dual-Path Network) - https://arxiv.org/abs/1707.01629
@@ -414,14 +414,15 @@
     * FBNet-C - https://arxiv.org/abs/1812.03443
     * MixNet - https://arxiv.org/abs/1907.09595
     * MNASNet B1, A1 (Squeeze-Excite), and Small - https://arxiv.org/abs/1807.11626
     * MobileNet-V2 - https://arxiv.org/abs/1801.04381
     * Single-Path NAS - https://arxiv.org/abs/1904.02877
     * TinyNet - https://arxiv.org/abs/2010.14819
 * EVA - https://arxiv.org/abs/2211.07636
+* FlexiViT - https://arxiv.org/abs/2212.08013
 * GCViT (Global Context Vision Transformer) - https://arxiv.org/abs/2206.09959
 * GhostNet - https://arxiv.org/abs/1911.11907
 * gMLP - https://arxiv.org/abs/2105.08050
 * GPU-Efficient Networks - https://arxiv.org/abs/2006.14090
 * Halo Nets - https://arxiv.org/abs/2103.12731
 * HRNet - https://arxiv.org/abs/1908.07919
 * Inception-V3 - https://arxiv.org/abs/1512.00567
```

### Comparing `timm-0.8.3.dev0/setup.py` & `timm-0.8.6.dev0/setup.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/__init__.py` & `timm-0.8.6.dev0/timm/data/__init__.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/auto_augment.py` & `timm-0.8.6.dev0/timm/data/auto_augment.py`

 * *Files 1% similar despite different names*

```diff
@@ -737,15 +737,14 @@
 
 
 class RandAugment:
     def __init__(self, ops, num_layers=2, choice_weights=None):
         self.ops = ops
         self.num_layers = num_layers
         self.choice_weights = choice_weights
-        print(self.ops, self.choice_weights)
 
     def __call__(self, img):
         # no replacement when using weighted choice
         ops = np.random.choice(
             self.ops,
             self.num_layers,
             replace=self.choice_weights is None,
```

### Comparing `timm-0.8.3.dev0/timm/data/config.py` & `timm-0.8.6.dev0/timm/data/config.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/dataset.py` & `timm-0.8.6.dev0/timm/data/dataset.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/dataset_factory.py` & `timm-0.8.6.dev0/timm/data/dataset_factory.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/distributed_sampler.py` & `timm-0.8.6.dev0/timm/data/distributed_sampler.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/loader.py` & `timm-0.8.6.dev0/timm/data/loader.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/mixup.py` & `timm-0.8.6.dev0/timm/data/mixup.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/random_erasing.py` & `timm-0.8.6.dev0/timm/data/random_erasing.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/class_map.py` & `timm-0.8.6.dev0/timm/data/readers/class_map.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/img_extensions.py` & `timm-0.8.6.dev0/timm/data/readers/img_extensions.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_factory.py` & `timm-0.8.6.dev0/timm/data/readers/reader_factory.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_hfds.py` & `timm-0.8.6.dev0/timm/data/readers/reader_hfds.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_image_folder.py` & `timm-0.8.6.dev0/timm/data/readers/reader_image_folder.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_image_in_tar.py` & `timm-0.8.6.dev0/timm/data/readers/reader_image_in_tar.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_image_tar.py` & `timm-0.8.6.dev0/timm/data/readers/reader_image_tar.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_tfds.py` & `timm-0.8.6.dev0/timm/data/readers/reader_tfds.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/readers/reader_wds.py` & `timm-0.8.6.dev0/timm/data/readers/reader_wds.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/real_labels.py` & `timm-0.8.6.dev0/timm/data/real_labels.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/tf_preprocessing.py` & `timm-0.8.6.dev0/timm/data/tf_preprocessing.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/transforms.py` & `timm-0.8.6.dev0/timm/data/transforms.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/data/transforms_factory.py` & `timm-0.8.6.dev0/timm/data/transforms_factory.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/__init__.py` & `timm-0.8.6.dev0/timm/layers/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 from .filter_response_norm import FilterResponseNormTlu2d, FilterResponseNormAct2d
 from .gather_excite import GatherExcite
 from .global_context import GlobalContext
 from .helpers import to_ntuple, to_2tuple, to_3tuple, to_4tuple, make_divisible, extend_tuple
 from .inplace_abn import InplaceAbn
 from .linear import Linear
 from .mixed_conv2d import MixedConv2d
-from .mlp import Mlp, GluMlp, GatedMlp, ConvMlp
+from .mlp import Mlp, GluMlp, GatedMlp, ConvMlp, GlobalResponseNormMlp
 from .non_local_attn import NonLocalAttn, BatNonLocalAttn
 from .norm import GroupNorm, GroupNorm1, LayerNorm, LayerNorm2d
 from .norm_act import BatchNormAct2d, GroupNormAct, convert_sync_batchnorm
 from .padding import get_padding, get_same_padding, pad_same
 from .patch_embed import PatchEmbed, resample_patch_embed
 from .pool2d_same import AvgPool2dSame, create_pool2d
 from .pos_embed import resample_abs_pos_embed
```

### Comparing `timm-0.8.3.dev0/timm/layers/activations.py` & `timm-0.8.6.dev0/timm/layers/activations.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/activations_jit.py` & `timm-0.8.6.dev0/timm/layers/activations_jit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/activations_me.py` & `timm-0.8.6.dev0/timm/layers/activations_me.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/adaptive_avgmax_pool.py` & `timm-0.8.6.dev0/timm/layers/adaptive_avgmax_pool.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/attention_pool2d.py` & `timm-0.8.6.dev0/timm/layers/attention_pool2d.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/blur_pool.py` & `timm-0.8.6.dev0/timm/layers/blur_pool.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/bottleneck_attn.py` & `timm-0.8.6.dev0/timm/layers/bottleneck_attn.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/cbam.py` & `timm-0.8.6.dev0/timm/layers/cbam.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/classifier.py` & `timm-0.8.6.dev0/timm/layers/classifier.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/cond_conv2d.py` & `timm-0.8.6.dev0/timm/layers/cond_conv2d.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/config.py` & `timm-0.8.6.dev0/timm/layers/config.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/conv2d_same.py` & `timm-0.8.6.dev0/timm/layers/conv2d_same.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/conv_bn_act.py` & `timm-0.8.6.dev0/timm/layers/conv_bn_act.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/create_act.py` & `timm-0.8.6.dev0/timm/layers/create_act.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/create_attn.py` & `timm-0.8.6.dev0/timm/layers/create_attn.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/create_conv2d.py` & `timm-0.8.6.dev0/timm/layers/create_conv2d.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/create_norm.py` & `timm-0.8.6.dev0/timm/layers/create_norm.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/create_norm_act.py` & `timm-0.8.6.dev0/timm/layers/create_norm_act.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/drop.py` & `timm-0.8.6.dev0/timm/layers/drop.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/eca.py` & `timm-0.8.6.dev0/timm/layers/eca.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/evo_norm.py` & `timm-0.8.6.dev0/timm/layers/evo_norm.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/fast_norm.py` & `timm-0.8.6.dev0/timm/layers/fast_norm.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/filter_response_norm.py` & `timm-0.8.6.dev0/timm/layers/filter_response_norm.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/gather_excite.py` & `timm-0.8.6.dev0/timm/layers/gather_excite.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/global_context.py` & `timm-0.8.6.dev0/timm/layers/global_context.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/halo_attn.py` & `timm-0.8.6.dev0/timm/layers/halo_attn.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/helpers.py` & `timm-0.8.6.dev0/timm/layers/helpers.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/inplace_abn.py` & `timm-0.8.6.dev0/timm/layers/inplace_abn.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/lambda_layer.py` & `timm-0.8.6.dev0/timm/layers/lambda_layer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/linear.py` & `timm-0.8.6.dev0/timm/layers/linear.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/median_pool.py` & `timm-0.8.6.dev0/timm/layers/median_pool.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/mixed_conv2d.py` & `timm-0.8.6.dev0/timm/layers/mixed_conv2d.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/ml_decoder.py` & `timm-0.8.6.dev0/timm/layers/ml_decoder.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/mlp.py` & `timm-0.8.6.dev0/timm/layers/mlp.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,30 +1,43 @@
 """ MLP module w/ dropout and configurable activation layer
 
 Hacked together by / Copyright 2020 Ross Wightman
 """
+from functools import partial
+
 from torch import nn as nn
 
+from .grn import GlobalResponseNorm
 from .helpers import to_2tuple
 
 
 class Mlp(nn.Module):
     """ MLP as used in Vision Transformer, MLP-Mixer and related networks
     """
-    def __init__(self, in_features, hidden_features=None, out_features=None, act_layer=nn.GELU, bias=True, drop=0.):
+    def __init__(
+            self,
+            in_features,
+            hidden_features=None,
+            out_features=None,
+            act_layer=nn.GELU,
+            bias=True,
+            drop=0.,
+            use_conv=False,
+    ):
         super().__init__()
         out_features = out_features or in_features
         hidden_features = hidden_features or in_features
         bias = to_2tuple(bias)
         drop_probs = to_2tuple(drop)
+        linear_layer = partial(nn.Conv2d, kernel_size=1) if use_conv else nn.Linear
 
-        self.fc1 = nn.Linear(in_features, hidden_features, bias=bias[0])
+        self.fc1 = linear_layer(in_features, hidden_features, bias=bias[0])
         self.act = act_layer()
         self.drop1 = nn.Dropout(drop_probs[0])
-        self.fc2 = nn.Linear(hidden_features, out_features, bias=bias[1])
+        self.fc2 = linear_layer(hidden_features, out_features, bias=bias[1])
         self.drop2 = nn.Dropout(drop_probs[1])
 
     def forward(self, x):
         x = self.fc1(x)
         x = self.act(x)
         x = self.drop1(x)
         x = self.fc2(x)
@@ -32,50 +45,68 @@
         return x
 
 
 class GluMlp(nn.Module):
     """ MLP w/ GLU style gating
     See: https://arxiv.org/abs/1612.08083, https://arxiv.org/abs/2002.05202
     """
-    def __init__(self, in_features, hidden_features=None, out_features=None, act_layer=nn.Sigmoid, bias=True, drop=0.):
+    def __init__(
+            self,
+            in_features,
+            hidden_features=None,
+            out_features=None,
+            act_layer=nn.Sigmoid,
+            bias=True,
+            drop=0.,
+            use_conv=False,
+    ):
         super().__init__()
         out_features = out_features or in_features
         hidden_features = hidden_features or in_features
         assert hidden_features % 2 == 0
         bias = to_2tuple(bias)
         drop_probs = to_2tuple(drop)
+        linear_layer = partial(nn.Conv2d, kernel_size=1) if use_conv else nn.Linear
+        self.chunk_dim = 1 if use_conv else -1
 
-        self.fc1 = nn.Linear(in_features, hidden_features, bias=bias[0])
+        self.fc1 = linear_layer(in_features, hidden_features, bias=bias[0])
         self.act = act_layer()
         self.drop1 = nn.Dropout(drop_probs[0])
-        self.fc2 = nn.Linear(hidden_features // 2, out_features, bias=bias[1])
+        self.fc2 = linear_layer(hidden_features // 2, out_features, bias=bias[1])
         self.drop2 = nn.Dropout(drop_probs[1])
 
     def init_weights(self):
         # override init of fc1 w/ gate portion set to weight near zero, bias=1
         fc1_mid = self.fc1.bias.shape[0] // 2
         nn.init.ones_(self.fc1.bias[fc1_mid:])
         nn.init.normal_(self.fc1.weight[fc1_mid:], std=1e-6)
 
     def forward(self, x):
         x = self.fc1(x)
-        x, gates = x.chunk(2, dim=-1)
+        x, gates = x.chunk(2, dim=self.chunk_dim)
         x = x * self.act(gates)
         x = self.drop1(x)
         x = self.fc2(x)
         x = self.drop2(x)
         return x
 
 
 class GatedMlp(nn.Module):
     """ MLP as used in gMLP
     """
     def __init__(
-            self, in_features, hidden_features=None, out_features=None, act_layer=nn.GELU,
-            gate_layer=None, bias=True, drop=0.):
+            self,
+            in_features,
+            hidden_features=None,
+            out_features=None,
+            act_layer=nn.GELU,
+            gate_layer=None,
+            bias=True,
+            drop=0.,
+    ):
         super().__init__()
         out_features = out_features or in_features
         hidden_features = hidden_features or in_features
         bias = to_2tuple(bias)
         drop_probs = to_2tuple(drop)
 
         self.fc1 = nn.Linear(in_features, hidden_features, bias=bias[0])
@@ -100,16 +131,23 @@
         return x
 
 
 class ConvMlp(nn.Module):
     """ MLP using 1x1 convs that keeps spatial dims
     """
     def __init__(
-            self, in_features, hidden_features=None, out_features=None, act_layer=nn.ReLU,
-            norm_layer=None, bias=True, drop=0.):
+            self,
+            in_features,
+            hidden_features=None,
+            out_features=None,
+            act_layer=nn.ReLU,
+            norm_layer=None,
+            bias=True,
+            drop=0.,
+    ):
         super().__init__()
         out_features = out_features or in_features
         hidden_features = hidden_features or in_features
         bias = to_2tuple(bias)
 
         self.fc1 = nn.Conv2d(in_features, hidden_features, kernel_size=1, bias=bias[0])
         self.norm = norm_layer(hidden_features) if norm_layer else nn.Identity()
@@ -120,7 +158,44 @@
     def forward(self, x):
         x = self.fc1(x)
         x = self.norm(x)
         x = self.act(x)
         x = self.drop(x)
         x = self.fc2(x)
         return x
+
+
+class GlobalResponseNormMlp(nn.Module):
+    """ MLP w/ Global Response Norm (see grn.py), nn.Linear or 1x1 Conv2d
+    """
+    def __init__(
+            self,
+            in_features,
+            hidden_features=None,
+            out_features=None,
+            act_layer=nn.GELU,
+            bias=True,
+            drop=0.,
+            use_conv=False,
+    ):
+        super().__init__()
+        out_features = out_features or in_features
+        hidden_features = hidden_features or in_features
+        bias = to_2tuple(bias)
+        drop_probs = to_2tuple(drop)
+        linear_layer = partial(nn.Conv2d, kernel_size=1) if use_conv else nn.Linear
+
+        self.fc1 = linear_layer(in_features, hidden_features, bias=bias[0])
+        self.act = act_layer()
+        self.drop1 = nn.Dropout(drop_probs[0])
+        self.grn = GlobalResponseNorm(hidden_features, channels_last=not use_conv)
+        self.fc2 = linear_layer(hidden_features, out_features, bias=bias[1])
+        self.drop2 = nn.Dropout(drop_probs[1])
+
+    def forward(self, x):
+        x = self.fc1(x)
+        x = self.act(x)
+        x = self.drop1(x)
+        x = self.grn(x)
+        x = self.fc2(x)
+        x = self.drop2(x)
+        return x
```

### Comparing `timm-0.8.3.dev0/timm/layers/non_local_attn.py` & `timm-0.8.6.dev0/timm/layers/non_local_attn.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/norm.py` & `timm-0.8.6.dev0/timm/layers/norm.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/norm_act.py` & `timm-0.8.6.dev0/timm/layers/norm_act.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/padding.py` & `timm-0.8.6.dev0/timm/layers/padding.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/patch_embed.py` & `timm-0.8.6.dev0/timm/layers/patch_embed.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/pool2d_same.py` & `timm-0.8.6.dev0/timm/layers/pool2d_same.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/pos_embed.py` & `timm-0.8.6.dev0/timm/layers/pos_embed.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/pos_embed_rel.py` & `timm-0.8.6.dev0/timm/layers/pos_embed_rel.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/pos_embed_sincos.py` & `timm-0.8.6.dev0/timm/layers/pos_embed_sincos.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/selective_kernel.py` & `timm-0.8.6.dev0/timm/layers/selective_kernel.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/separable_conv.py` & `timm-0.8.6.dev0/timm/layers/separable_conv.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/space_to_depth.py` & `timm-0.8.6.dev0/timm/layers/space_to_depth.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/split_attn.py` & `timm-0.8.6.dev0/timm/layers/split_attn.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/split_batchnorm.py` & `timm-0.8.6.dev0/timm/layers/split_batchnorm.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/squeeze_excite.py` & `timm-0.8.6.dev0/timm/layers/squeeze_excite.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/std_conv.py` & `timm-0.8.6.dev0/timm/layers/std_conv.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/test_time_pool.py` & `timm-0.8.6.dev0/timm/layers/test_time_pool.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/layers/weight_init.py` & `timm-0.8.6.dev0/timm/layers/weight_init.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/loss/asymmetric_loss.py` & `timm-0.8.6.dev0/timm/loss/asymmetric_loss.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/loss/binary_cross_entropy.py` & `timm-0.8.6.dev0/timm/loss/binary_cross_entropy.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/loss/cross_entropy.py` & `timm-0.8.6.dev0/timm/loss/cross_entropy.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/loss/jsd.py` & `timm-0.8.6.dev0/timm/loss/jsd.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/__init__.py` & `timm-0.8.6.dev0/timm/models/__init__.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_builder.py` & `timm-0.8.6.dev0/timm/models/_builder.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_efficientnet_blocks.py` & `timm-0.8.6.dev0/timm/models/_efficientnet_blocks.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_efficientnet_builder.py` & `timm-0.8.6.dev0/timm/models/_efficientnet_builder.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_factory.py` & `timm-0.8.6.dev0/timm/models/_factory.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_features.py` & `timm-0.8.6.dev0/timm/models/_features.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_features_fx.py` & `timm-0.8.6.dev0/timm/models/_features_fx.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_helpers.py` & `timm-0.8.6.dev0/timm/models/_helpers.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_hub.py` & `timm-0.8.6.dev0/timm/models/_hub.py`

 * *Files 9% similar despite different names*

```diff
@@ -205,14 +205,15 @@
     repo_id: str,
     commit_message: str = 'Add model',
     token: Optional[str] = None,
     revision: Optional[str] = None,
     private: bool = False,
     create_pr: bool = False,
     model_config: Optional[dict] = None,
+    model_card: Optional[dict] = None,
 ):
     # Create repo if it doesn't exist yet
     repo_url = create_repo(repo_id, token=token, private=private, exist_ok=True)
 
     # Infer complete repo_id from repo_url
     # Can be different from the input `repo_id` if repo_owner was implicit
     _, repo_owner, repo_name = repo_type_and_id_from_hf_id(repo_url)
@@ -228,17 +229,31 @@
     # Dump model and push to Hub
     with TemporaryDirectory() as tmpdir:
         # Save model weights and config.
         save_for_hf(model, tmpdir, model_config=model_config)
 
         # Add readme if it does not exist
         if not has_readme:
+            model_card = model_card or {}
             model_name = repo_id.split('/')[-1]
             readme_path = Path(tmpdir) / "README.md"
-            readme_text = f'---\ntags:\n- image-classification\n- timm\nlibrary_tag: timm\n---\n# Model card for {model_name}'
+            readme_text = "---\n"
+            readme_text += "tags:\n- image-classification\n- timm\n"
+            readme_text += "library_tag: timm\n"
+            readme_text += f"license: {model_card.get('license', 'apache-2.0')}\n"
+            readme_text += "---\n"
+            readme_text += f"# Model card for {model_name}\n"
+            if 'description' in model_card:
+                readme_text += f"\n{model_card['description']}\n"
+            if 'details' in model_card:
+                readme_text += f"\n## Model Details\n"
+                for k, v in model_card['details'].items():
+                    readme_text += f"- **{k}:** {v}\n"
+            if 'citation' in model_card:
+                readme_text += f"\n## Citation\n```\n{model_card['citation']}```\n"
             readme_path.write_text(readme_text)
 
         # Upload model and return
         return upload_folder(
             repo_id=repo_id,
             folder_path=tmpdir,
             revision=revision,
```

### Comparing `timm-0.8.3.dev0/timm/models/_manipulate.py` & `timm-0.8.6.dev0/timm/models/_manipulate.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_pretrained.py` & `timm-0.8.6.dev0/timm/models/_pretrained.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_prune.py` & `timm-0.8.6.dev0/timm/models/_prune.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/_registry.py` & `timm-0.8.6.dev0/timm/models/_registry.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/beit.py` & `timm-0.8.6.dev0/timm/models/beit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/byoanet.py` & `timm-0.8.6.dev0/timm/models/byoanet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/byobnet.py` & `timm-0.8.6.dev0/timm/models/byobnet.py`

 * *Files 2% similar despite different names*

```diff
@@ -214,15 +214,18 @@
     if groups > 0:
         group_size = lambda chs, idx: chs // groups if (idx + 1) % 2 == 0 else 0
     bcfg = tuple([ByoBlockCfg(type='rep', d=d, c=c * wf, gs=group_size) for d, c, wf in zip(d, c, wf)])
     return bcfg
 
 
 def interleave_blocks(
-        types: Tuple[str, str], d, every: Union[int, List[int]] = 1, first: bool = False, **kwargs
+        types: Tuple[str, str], d,
+        every: Union[int, List[int]] = 1,
+        first: bool = False,
+        **kwargs,
 ) -> Tuple[ByoBlockCfg]:
     """ interleave 2 block types in stack
     """
     assert len(types) == 2
     if isinstance(every, int):
         every = list(range(0 if first else every, d, every + 1))
         if not every:
@@ -958,17 +961,29 @@
 
 
 class BasicBlock(nn.Module):
     """ ResNet Basic Block - kxk + kxk
     """
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=1, dilation=(1, 1), group_size=None, bottle_ratio=1.0,
-            downsample='avg', attn_last=True, linear_out=False, layers: LayerFn = None, drop_block=None,
-            drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=1,
+            dilation=(1, 1),
+            group_size=None,
+            bottle_ratio=1.0,
+            downsample='avg',
+            attn_last=True,
+            linear_out=False,
+            layers: LayerFn = None,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(BasicBlock, self).__init__()
         layers = layers or LayerFn()
         mid_chs = make_divisible(out_chs * bottle_ratio)
         groups = num_groups(group_size, mid_chs)
 
         self.shortcut = create_shortcut(
             downsample, in_chs=in_chs, out_chs=out_chs, stride=stride, dilation=dilation,
@@ -979,15 +994,15 @@
         self.conv2_kxk = layers.conv_norm_act(
             mid_chs, out_chs, kernel_size, dilation=dilation[1], groups=groups, drop_layer=drop_block, apply_act=False)
         self.attn_last = nn.Identity() if not attn_last or layers.attn is None else layers.attn(out_chs)
         self.drop_path = DropPath(drop_path_rate) if drop_path_rate > 0. else nn.Identity()
         self.act = nn.Identity() if linear_out else layers.act(inplace=True)
 
     def init_weights(self, zero_init_last: bool = False):
-        if zero_init_last and self.shortcut is not None:
+        if zero_init_last and self.shortcut is not None and getattr(self.conv2_kxk.bn, 'weight', None) is not None:
             nn.init.zeros_(self.conv2_kxk.bn.weight)
         for attn in (self.attn, self.attn_last):
             if hasattr(attn, 'reset_parameters'):
                 attn.reset_parameters()
 
     def forward(self, x):
         shortcut = x
@@ -1001,17 +1016,31 @@
 
 
 class BottleneckBlock(nn.Module):
     """ ResNet-like Bottleneck Block - 1x1 - kxk - 1x1
     """
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=1, dilation=(1, 1), bottle_ratio=1., group_size=None,
-            downsample='avg', attn_last=False, linear_out=False, extra_conv=False, bottle_in=False,
-            layers: LayerFn = None, drop_block=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1.,
+            group_size=None,
+            downsample='avg',
+            attn_last=False,
+            linear_out=False,
+            extra_conv=False,
+            bottle_in=False,
+            layers: LayerFn = None,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(BottleneckBlock, self).__init__()
         layers = layers or LayerFn()
         mid_chs = make_divisible((in_chs if bottle_in else out_chs) * bottle_ratio)
         groups = num_groups(group_size, mid_chs)
 
         self.shortcut = create_shortcut(
             downsample, in_chs=in_chs, out_chs=out_chs, stride=stride, dilation=dilation,
@@ -1027,15 +1056,15 @@
         self.attn = nn.Identity() if attn_last or layers.attn is None else layers.attn(mid_chs)
         self.conv3_1x1 = layers.conv_norm_act(mid_chs, out_chs, 1, apply_act=False)
         self.attn_last = nn.Identity() if not attn_last or layers.attn is None else layers.attn(out_chs)
         self.drop_path = DropPath(drop_path_rate) if drop_path_rate > 0. else nn.Identity()
         self.act = nn.Identity() if linear_out else layers.act(inplace=True)
 
     def init_weights(self, zero_init_last: bool = False):
-        if zero_init_last and self.shortcut is not None:
+        if zero_init_last and self.shortcut is not None and getattr(self.conv3_1x1.bn, 'weight', None) is not None:
             nn.init.zeros_(self.conv3_1x1.bn.weight)
         for attn in (self.attn, self.attn_last):
             if hasattr(attn, 'reset_parameters'):
                 attn.reset_parameters()
 
     def forward(self, x):
         shortcut = x
@@ -1059,17 +1088,29 @@
     uses strides within the block (external 3x3 or maxpool downsampling is done in front of the block repeats).
 
     If one does want to use a lot of these blocks w/ stride, I'd recommend using the EdgeBlock (3x3 /w stride + 1x1)
     for more optimal compute.
     """
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=1, dilation=(1, 1), bottle_ratio=1.0, group_size=None,
-            downsample='avg', attn_last=True, linear_out=False, layers: LayerFn = None, drop_block=None,
-            drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1.0,
+            group_size=None,
+            downsample='avg',
+            attn_last=True,
+            linear_out=False,
+            layers: LayerFn = None,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(DarkBlock, self).__init__()
         layers = layers or LayerFn()
         mid_chs = make_divisible(out_chs * bottle_ratio)
         groups = num_groups(group_size, mid_chs)
 
         self.shortcut = create_shortcut(
             downsample, in_chs=in_chs, out_chs=out_chs, stride=stride, dilation=dilation,
@@ -1081,15 +1122,15 @@
             mid_chs, out_chs, kernel_size, stride=stride, dilation=dilation[0],
             groups=groups, drop_layer=drop_block, apply_act=False)
         self.attn_last = nn.Identity() if not attn_last or layers.attn is None else layers.attn(out_chs)
         self.drop_path = DropPath(drop_path_rate) if drop_path_rate > 0. else nn.Identity()
         self.act = nn.Identity() if linear_out else layers.act(inplace=True)
 
     def init_weights(self, zero_init_last: bool = False):
-        if zero_init_last and self.shortcut is not None:
+        if zero_init_last and self.shortcut is not None and getattr(self.conv2_kxk.bn, 'weight', None) is not None:
             nn.init.zeros_(self.conv2_kxk.bn.weight)
         for attn in (self.attn, self.attn_last):
             if hasattr(attn, 'reset_parameters'):
                 attn.reset_parameters()
 
     def forward(self, x):
         shortcut = x
@@ -1110,17 +1151,29 @@
     Very similar to the EfficientNet Edge-Residual block but this block it ends with activations, is
     intended to be used with either expansion or bottleneck contraction, and can use DW/group/non-grouped convs.
 
     FIXME is there a more common 3x3 + 1x1 conv block to name this after?
     """
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=1, dilation=(1, 1), bottle_ratio=1.0, group_size=None,
-            downsample='avg', attn_last=False, linear_out=False, layers: LayerFn = None,
-            drop_block=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1.0,
+            group_size=None,
+            downsample='avg',
+            attn_last=False,
+            linear_out=False,
+            layers: LayerFn = None,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(EdgeBlock, self).__init__()
         layers = layers or LayerFn()
         mid_chs = make_divisible(out_chs * bottle_ratio)
         groups = num_groups(group_size, mid_chs)
 
         self.shortcut = create_shortcut(
             downsample, in_chs=in_chs, out_chs=out_chs, stride=stride, dilation=dilation,
@@ -1131,15 +1184,15 @@
         self.attn = nn.Identity() if attn_last or layers.attn is None else layers.attn(mid_chs)
         self.conv2_1x1 = layers.conv_norm_act(mid_chs, out_chs, 1, apply_act=False)
         self.attn_last = nn.Identity() if not attn_last or layers.attn is None else layers.attn(out_chs)
         self.drop_path = DropPath(drop_path_rate) if drop_path_rate > 0. else nn.Identity()
         self.act = nn.Identity() if linear_out else layers.act(inplace=True)
 
     def init_weights(self, zero_init_last: bool = False):
-        if zero_init_last and self.shortcut is not None:
+        if zero_init_last and self.shortcut is not None and getattr(self.conv2_1x1.bn, 'weight', None) is not None:
             nn.init.zeros_(self.conv2_1x1.bn.weight)
         for attn in (self.attn, self.attn_last):
             if hasattr(attn, 'reset_parameters'):
                 attn.reset_parameters()
 
     def forward(self, x):
         shortcut = x
@@ -1158,16 +1211,27 @@
 
     Adapted from impl at https://github.com/DingXiaoH/RepVGG
 
     This version does not currently support the deploy optimization. It is currently fixed in 'train' mode.
     """
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=1, dilation=(1, 1), bottle_ratio=1.0, group_size=None,
-            downsample='', layers: LayerFn = None, drop_block=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1.0,
+            group_size=None,
+            downsample='',
+            layers: LayerFn = None,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(RepVggBlock, self).__init__()
         layers = layers or LayerFn()
         groups = num_groups(group_size, in_chs)
 
         use_ident = in_chs == out_chs and stride == 1 and dilation[0] == dilation[1]
         self.identity = layers.norm_act(out_chs, apply_act=False) if use_ident else None
         self.conv_kxk = layers.conv_norm_act(
@@ -1200,17 +1264,32 @@
 
 
 class SelfAttnBlock(nn.Module):
     """ ResNet-like Bottleneck Block - 1x1 - optional kxk - self attn - 1x1
     """
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=1, dilation=(1, 1), bottle_ratio=1., group_size=None,
-            downsample='avg', extra_conv=False, linear_out=False, bottle_in=False, post_attn_na=True,
-            feat_size=None, layers: LayerFn = None, drop_block=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1.,
+            group_size=None,
+            downsample='avg',
+            extra_conv=False,
+            linear_out=False,
+            bottle_in=False,
+            post_attn_na=True,
+            feat_size=None,
+            layers: LayerFn = None,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(SelfAttnBlock, self).__init__()
         assert layers is not None
         mid_chs = make_divisible((in_chs if bottle_in else out_chs) * bottle_ratio)
         groups = num_groups(group_size, mid_chs)
 
         self.shortcut = create_shortcut(
             downsample, in_chs=in_chs, out_chs=out_chs, stride=stride, dilation=dilation,
@@ -1229,15 +1308,15 @@
         self.self_attn = layers.self_attn(mid_chs, stride=stride, **opt_kwargs)
         self.post_attn = layers.norm_act(mid_chs) if post_attn_na else nn.Identity()
         self.conv3_1x1 = layers.conv_norm_act(mid_chs, out_chs, 1, apply_act=False)
         self.drop_path = DropPath(drop_path_rate) if drop_path_rate > 0. else nn.Identity()
         self.act = nn.Identity() if linear_out else layers.act(inplace=True)
 
     def init_weights(self, zero_init_last: bool = False):
-        if zero_init_last and self.shortcut is not None:
+        if zero_init_last and self.shortcut is not None and getattr(self.conv3_1x1.bn, 'weight', None) is not None:
             nn.init.zeros_(self.conv3_1x1.bn.weight)
         if hasattr(self.self_attn, 'reset_parameters'):
             self.self_attn.reset_parameters()
 
     def forward(self, x):
         shortcut = x
         x = self.conv1_1x1(x)
@@ -1270,16 +1349,25 @@
     assert block in _block_registry, f'Unknown block type ({block}'
     return _block_registry[block](**kwargs)
 
 
 class Stem(nn.Sequential):
 
     def __init__(
-            self, in_chs, out_chs, kernel_size=3, stride=4, pool='maxpool',
-            num_rep=3, num_act=None, chs_decay=0.5, layers: LayerFn = None):
+            self,
+            in_chs,
+            out_chs,
+            kernel_size=3,
+            stride=4,
+            pool='maxpool',
+            num_rep=3,
+            num_act=None,
+            chs_decay=0.5,
+            layers: LayerFn = None,
+    ):
         super().__init__()
         assert stride in (2, 4)
         layers = layers or LayerFn()
 
         if isinstance(out_chs, (list, tuple)):
             num_rep = len(out_chs)
             stem_chs = out_chs
@@ -1315,15 +1403,22 @@
             curr_stride *= 2
             prev_feat = 'pool'
 
         self.feature_info.append(dict(num_chs=prev_chs, reduction=curr_stride, module=prev_feat))
         assert curr_stride == stride
 
 
-def create_byob_stem(in_chs, out_chs, stem_type='', pool_type='', feat_prefix='stem', layers: LayerFn = None):
+def create_byob_stem(
+        in_chs,
+        out_chs,
+        stem_type='',
+        pool_type='',
+        feat_prefix='stem',
+        layers: LayerFn = None,
+):
     layers = layers or LayerFn()
     assert stem_type in ('', 'quad', 'quad2', 'tiered', 'deep', 'rep', '7x7', '3x3')
     if 'quad' in stem_type:
         # based on NFNet stem, stack of 4 3x3 convs
         num_act = 2 if 'quad2' in stem_type else None
         stem = Stem(in_chs, out_chs, num_rep=4, num_act=num_act, pool=pool_type, layers=layers)
     elif 'tiered' in stem_type:
@@ -1403,18 +1498,22 @@
     block_kwargs['layers'] = layer_fns
 
     # add additional block_kwargs specified in block_cfg or model_cfg, precedence to block if set
     block_kwargs.update(override_kwargs(block_cfg.block_kwargs, model_cfg.block_kwargs))
 
 
 def create_byob_stages(
-        cfg: ByoModelCfg, drop_path_rate: float, output_stride: int, stem_feat: Dict[str, Any],
+        cfg: ByoModelCfg,
+        drop_path_rate: float,
+        output_stride: int,
+        stem_feat: Dict[str, Any],
         feat_size: Optional[int] = None,
         layers: Optional[LayerFn] = None,
-        block_kwargs_fn: Optional[Callable] = update_block_kwargs):
+        block_kwargs_fn: Optional[Callable] = update_block_kwargs,
+):
 
     layers = layers or LayerFn()
     feature_info = []
     block_cfgs = [expand_blocks_cfg(s) for s in cfg.blocks]
     depths = [sum([bc.d for bc in stage_bcs]) for stage_bcs in block_cfgs]
     dpr = [x.tolist() for x in torch.linspace(0, drop_path_rate, sum(depths)).split(depths)]
     dilation = 1
@@ -1481,20 +1580,46 @@
 
     A flexible network backbone that allows building model stem + blocks via
     dataclass cfg definition w/ factory functions for module instantiation.
 
     Current assumption is that both stem and blocks are in conv-bn-act order (w/ block ending in act).
     """
     def __init__(
-            self, cfg: ByoModelCfg, num_classes=1000, in_chans=3, global_pool='avg', output_stride=32,
-            zero_init_last=True, img_size=None, drop_rate=0., drop_path_rate=0.):
+            self,
+            cfg: ByoModelCfg,
+            num_classes=1000,
+            in_chans=3,
+            global_pool='avg',
+            output_stride=32,
+            img_size=None,
+            drop_rate=0.,
+            drop_path_rate=0.,
+            zero_init_last=True,
+            **kwargs,
+    ):
+        """
+
+        Args:
+            cfg (ByoModelCfg): Model architecture configuration
+            num_classes (int): Number of classifier classes (default: 1000)
+            in_chans (int): Number of input channels (default: 3)
+            global_pool (str): Global pooling type (default: 'avg')
+            output_stride (int): Output stride of network, one of (8, 16, 32) (default: 32)
+            img_size (Union[int, Tuple[int]): Image size for fixed image size models (i.e. self-attn)
+            drop_rate (float): Dropout rate (default: 0.)
+            drop_path_rate (float): Stochastic depth drop-path rate (default: 0.)
+            zero_init_last (bool): Zero-init last weight of residual path
+            kwargs (dict): Extra kwargs overlayed onto cfg
+        """
         super().__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         self.grad_checkpointing = False
+
+        cfg = replace(cfg, **kwargs)  # overlay kwargs onto cfg
         layers = get_layer_fns(cfg)
         if cfg.fixed_input_size:
             assert img_size is not None, 'img_size argument is required for fixed input size model'
         feat_size = to_2tuple(img_size) if img_size is not None else None
 
         self.feature_info = []
         stem_chs = int(round((cfg.stem_chs or cfg.blocks[0].c) * cfg.width_factor))
```

### Comparing `timm-0.8.3.dev0/timm/models/cait.py` & `timm-0.8.6.dev0/timm/models/cait.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/coat.py` & `timm-0.8.6.dev0/timm/models/coat.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/convit.py` & `timm-0.8.6.dev0/timm/models/convit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/convmixer.py` & `timm-0.8.6.dev0/timm/models/convmixer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/convnext.py` & `timm-0.8.6.dev0/timm/models/convnext.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,29 +1,55 @@
 """ ConvNeXt
 
-Paper: `A ConvNet for the 2020s` - https://arxiv.org/pdf/2201.03545.pdf
+Papers:
+* `A ConvNet for the 2020s` - https://arxiv.org/pdf/2201.03545.pdf
+@Article{liu2022convnet,
+  author  = {Zhuang Liu and Hanzi Mao and Chao-Yuan Wu and Christoph Feichtenhofer and Trevor Darrell and Saining Xie},
+  title   = {A ConvNet for the 2020s},
+  journal = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
+  year    = {2022},
+}
+
+* `ConvNeXt-V2 - Co-designing and Scaling ConvNets with Masked Autoencoders` - https://arxiv.org/abs/2301.00808
+@article{Woo2023ConvNeXtV2,
+  title={ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders},
+  author={Sanghyun Woo, Shoubhik Debnath, Ronghang Hu, Xinlei Chen, Zhuang Liu, In So Kweon and Saining Xie},
+  year={2023},
+  journal={arXiv preprint arXiv:2301.00808},
+}
+
+Original code and weights from:
+* https://github.com/facebookresearch/ConvNeXt, original copyright below
+* https://github.com/facebookresearch/ConvNeXt-V2, original copyright below
 
-Original code and weights from https://github.com/facebookresearch/ConvNeXt, original copyright below
-
-Model defs atto, femto, pico, nano and _ols / _hnf variants are timm specific.
+Model defs atto, femto, pico, nano and _ols / _hnf variants are timm originals.
 
 Modifications and additions for timm hacked together by / Copyright 2022, Ross Wightman
 """
+# ConvNeXt
 # Copyright (c) Meta Platforms, Inc. and affiliates.
 # All rights reserved.
 # This source code is licensed under the MIT license
+
+# ConvNeXt-V2
+# Copyright (c) Meta Platforms, Inc. and affiliates.
+# All rights reserved.
+# This source code is licensed under the license found in the
+# LICENSE file in the root directory of this source tree (Attribution-NonCommercial 4.0 International (CC BY-NC 4.0))
+# No code was used directly from ConvNeXt-V2, however the weights are CC BY-NC 4.0 so beware if using commercially.
+
 from collections import OrderedDict
 from functools import partial
 
 import torch
 import torch.nn as nn
 
 from timm.data import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
-from timm.layers import trunc_normal_, SelectAdaptivePool2d, DropPath, ConvMlp, Mlp, LayerNorm2d, LayerNorm, \
-    create_conv2d, get_act_layer, make_divisible, to_ntuple
+from timm.layers import trunc_normal_, SelectAdaptivePool2d, DropPath, Mlp, GlobalResponseNormMlp, \
+    LayerNorm2d, LayerNorm, create_conv2d, get_act_layer, make_divisible, to_ntuple
 from ._builder import build_model_with_cfg
 from ._manipulate import named_apply, checkpoint_seq
 from ._pretrained import generate_default_cfgs
 from ._registry import register_model
 
 __all__ = ['ConvNeXt']  # model_registry will add each entrypoint fn to this
 
@@ -50,32 +76,32 @@
             out_chs=None,
             kernel_size=7,
             stride=1,
             dilation=1,
             mlp_ratio=4,
             conv_mlp=False,
             conv_bias=True,
+            use_grn=False,
             ls_init_value=1e-6,
             act_layer='gelu',
             norm_layer=None,
             drop_path=0.,
     ):
         super().__init__()
         out_chs = out_chs or in_chs
         act_layer = get_act_layer(act_layer)
         if not norm_layer:
             norm_layer = LayerNorm2d if conv_mlp else LayerNorm
-        mlp_layer = ConvMlp if conv_mlp else Mlp
+        mlp_layer = partial(GlobalResponseNormMlp if use_grn else Mlp, use_conv=conv_mlp)
         self.use_conv_mlp = conv_mlp
-
         self.conv_dw = create_conv2d(
             in_chs, out_chs, kernel_size=kernel_size, stride=stride, dilation=dilation, depthwise=True, bias=conv_bias)
         self.norm = norm_layer(out_chs)
         self.mlp = mlp_layer(out_chs, int(mlp_ratio * out_chs), act_layer=act_layer)
-        self.gamma = nn.Parameter(ls_init_value * torch.ones(out_chs)) if ls_init_value > 0 else None
+        self.gamma = nn.Parameter(ls_init_value * torch.ones(out_chs)) if ls_init_value is not None else None
         self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()
 
     def forward(self, x):
         shortcut = x
         x = self.conv_dw(x)
         if self.use_conv_mlp:
             x = self.norm(x)
@@ -102,14 +128,15 @@
             stride=2,
             depth=2,
             dilation=(1, 1),
             drop_path_rates=None,
             ls_init_value=1.0,
             conv_mlp=False,
             conv_bias=True,
+            use_grn=False,
             act_layer='gelu',
             norm_layer=None,
             norm_layer_cl=None
     ):
         super().__init__()
         self.grad_checkpointing = False
 
@@ -134,16 +161,17 @@
                 out_chs=out_chs,
                 kernel_size=kernel_size,
                 dilation=dilation[1],
                 drop_path=drop_path_rates[i],
                 ls_init_value=ls_init_value,
                 conv_mlp=conv_mlp,
                 conv_bias=conv_bias,
+                use_grn=use_grn,
                 act_layer=act_layer,
-                norm_layer=norm_layer if conv_mlp else norm_layer_cl
+                norm_layer=norm_layer if conv_mlp else norm_layer_cl,
             ))
             in_chs = out_chs
         self.blocks = nn.Sequential(*stage_blocks)
 
     def forward(self, x):
         x = self.downsample(x)
         if self.grad_checkpointing and not torch.jit.is_scripting():
@@ -152,24 +180,14 @@
             x = self.blocks(x)
         return x
 
 
 class ConvNeXt(nn.Module):
     r""" ConvNeXt
         A PyTorch impl of : `A ConvNet for the 2020s`  - https://arxiv.org/pdf/2201.03545.pdf
-
-    Args:
-        in_chans (int): Number of input image channels. Default: 3
-        num_classes (int): Number of classes for classification head. Default: 1000
-        depths (tuple(int)): Number of blocks at each stage. Default: [3, 3, 9, 3]
-        dims (tuple(int)): Feature dimension at each stage. Default: [96, 192, 384, 768]
-        drop_rate (float): Head dropout rate
-        drop_path_rate (float): Stochastic depth rate. Default: 0.
-        ls_init_value (float): Init value for Layer Scale. Default: 1e-6.
-        head_init_scale (float): Init scaling value for classifier weights and biases. Default: 1.
     """
 
     def __init__(
             self,
             in_chans=3,
             num_classes=1000,
             global_pool='avg',
@@ -180,19 +198,42 @@
             ls_init_value=1e-6,
             stem_type='patch',
             patch_size=4,
             head_init_scale=1.,
             head_norm_first=False,
             conv_mlp=False,
             conv_bias=True,
+            use_grn=False,
             act_layer='gelu',
             norm_layer=None,
             drop_rate=0.,
             drop_path_rate=0.,
     ):
+        """
+        Args:
+            in_chans (int): Number of input image channels (default: 3)
+            num_classes (int): Number of classes for classification head (default: 1000)
+            global_pool (str): Global pooling type (default: 'avg')
+            output_stride (int): Output stride of network, one of (8, 16, 32) (default: 32)
+            depths (tuple(int)): Number of blocks at each stage. (default: [3, 3, 9, 3])
+            dims (tuple(int)): Feature dimension at each stage. (default: [96, 192, 384, 768])
+            kernel_sizes (Union[int, List[int]]: Depthwise convolution kernel-sizes for each stage (default: 7)
+            ls_init_value (float): Init value for Layer Scale (default: 1e-6)
+            stem_type (str): Type of stem (default: 'patch')
+            patch_size (int): Stem patch size for patch stem (default: 4)
+            head_init_scale (float): Init scaling value for classifier weights and biases (default: 1)
+            head_norm_first (bool): Apply normalization before global pool + head (default: False)
+            conv_mlp (bool): Use 1x1 conv in MLP, improves speed for small networks w/ chan last (default: False)
+            conv_bias (bool): Use bias layers w/ all convolutions (default: True)
+            use_grn (bool): Use Global Response Norm (ConvNeXt-V2) in MLP (default: False)
+            act_layer (Union[str, nn.Module]): Activation Layer
+            norm_layer (Union[str, nn.Module]): Normalization Layer
+            drop_rate (float): Head dropout rate (default: 0.)
+            drop_path_rate (float): Stochastic depth rate (default: 0.)
+        """
         super().__init__()
         assert output_stride in (8, 16, 32)
         kernel_sizes = to_ntuple(4)(kernel_sizes)
         if norm_layer is None:
             norm_layer = LayerNorm2d
             norm_layer_cl = norm_layer if conv_mlp else LayerNorm
         else:
@@ -243,17 +284,18 @@
                 stride=stride,
                 dilation=(first_dilation, dilation),
                 depth=depths[i],
                 drop_path_rates=dp_rates[i],
                 ls_init_value=ls_init_value,
                 conv_mlp=conv_mlp,
                 conv_bias=conv_bias,
+                use_grn=use_grn,
                 act_layer=act_layer,
                 norm_layer=norm_layer,
-                norm_layer_cl=norm_layer_cl
+                norm_layer_cl=norm_layer_cl,
             ))
             prev_chs = out_chs
             # NOTE feature_info use currently assumes stage 0 == stride 1, rest are stride 2
             self.feature_info += [dict(num_chs=prev_chs, reduction=curr_stride, module=f'stages.{i}')]
         self.stages = nn.Sequential(*stages)
         self.num_features = prev_chs
 
@@ -338,25 +380,34 @@
     import re
     for k, v in state_dict.items():
         k = k.replace('downsample_layers.0.', 'stem.')
         k = re.sub(r'stages.([0-9]+).([0-9]+)', r'stages.\1.blocks.\2', k)
         k = re.sub(r'downsample_layers.([0-9]+).([0-9]+)', r'stages.\1.downsample.\2', k)
         k = k.replace('dwconv', 'conv_dw')
         k = k.replace('pwconv', 'mlp.fc')
+        if 'grn' in k:
+            k = k.replace('grn.beta', 'mlp.grn.bias')
+            k = k.replace('grn.gamma', 'mlp.grn.weight')
+            v = v.reshape(v.shape[-1])
         k = k.replace('head.', 'head.fc.')
         if k.startswith('norm.'):
             k = k.replace('norm', 'head.norm')
         if v.ndim == 2 and 'head' not in k:
             model_shape = model.state_dict()[k].shape
             v = v.reshape(model_shape)
         out_dict[k] = v
     return out_dict
 
 
 def _create_convnext(variant, pretrained=False, **kwargs):
+    if kwargs.get('pretrained_cfg', '') == 'fcmae':
+        # NOTE fcmae pretrained weights have no classifier or final norm-layer (`head.norm`)
+        # This is workaround loading with num_classes=0 w/o removing norm-layer.
+        kwargs.setdefault('pretrained_strict', False)
+
     model = build_model_with_cfg(
         ConvNeXt, variant, pretrained,
         pretrained_filter_fn=checkpoint_filter_fn,
         feature_cfg=dict(out_indices=(0, 1, 2, 3), flatten_sequential=True),
         **kwargs)
     return model
 
@@ -368,14 +419,28 @@
         'crop_pct': 0.875, 'interpolation': 'bicubic',
         'mean': IMAGENET_DEFAULT_MEAN, 'std': IMAGENET_DEFAULT_STD,
         'first_conv': 'stem.0', 'classifier': 'head.fc',
         **kwargs
     }
 
 
+def _cfgv2(url='', **kwargs):
+    return {
+        'url': url,
+        'num_classes': 1000, 'input_size': (3, 224, 224), 'pool_size': (7, 7),
+        'crop_pct': 0.875, 'interpolation': 'bicubic',
+        'mean': IMAGENET_DEFAULT_MEAN, 'std': IMAGENET_DEFAULT_STD,
+        'first_conv': 'stem.0', 'classifier': 'head.fc',
+        'license': 'cc-by-nc-4.0', 'paper_ids': 'arXiv:2301.00808',
+        'paper_name': 'ConvNeXt-V2: Co-designing and Scaling ConvNets with Masked Autoencoders',
+        'origin_url': 'https://github.com/facebookresearch/ConvNeXt-V2',
+        **kwargs
+    }
+
+
 default_cfgs = generate_default_cfgs({
     # timm specific variants
     'convnext_atto.d2_in1k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/convnext_atto_d2-01bb0f51.pth',
         hf_hub_id='timm/',
         test_input_size=(3, 288, 288), test_crop_pct=0.95),
     'convnext_atto_ols.a2_in1k': _cfg(
@@ -409,18 +474,30 @@
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/convnext_nano_ols_d1h-ae424a9a.pth',
         hf_hub_id='timm/',
         crop_pct=0.95, test_input_size=(3, 288, 288), test_crop_pct=1.0),
     'convnext_tiny_hnf.a2h_in1k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/convnext_tiny_hnf_a2h-ab7e9df2.pth',
         hf_hub_id='timm/',
         crop_pct=0.95, test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnext_tiny.in12k_ft_in1k': _cfg(
+        hf_hub_id='timm/',
+        crop_pct=0.95, test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnext_small.in12k_ft_in1k': _cfg(
+        hf_hub_id='timm/',
+        crop_pct=0.95, test_input_size=(3, 288, 288), test_crop_pct=1.0),
 
     'convnext_nano.in12k': _cfg(
         hf_hub_id='timm/',
         crop_pct=0.95, num_classes=11821),
+    'convnext_tiny.in12k': _cfg(
+        hf_hub_id='timm/',
+        crop_pct=0.95, num_classes=11821),
+    'convnext_small.in12k': _cfg(
+        hf_hub_id='timm/',
+        crop_pct=0.95, num_classes=11821),
 
     'convnext_tiny.fb_in1k': _cfg(
         url="https://dl.fbaipublicfiles.com/convnext/convnext_tiny_1k_224_ema.pth",
         hf_hub_id='timm/',
         test_input_size=(3, 288, 288), test_crop_pct=1.0),
     'convnext_small.fb_in1k': _cfg(
         url="https://dl.fbaipublicfiles.com/convnext/convnext_small_1k_224_ema.pth",
@@ -495,14 +572,123 @@
         url="https://dl.fbaipublicfiles.com/convnext/convnext_large_22k_224.pth",
         hf_hub_id='timm/',
         num_classes=21841),
     'convnext_xlarge.fb_in22k': _cfg(
         url="https://dl.fbaipublicfiles.com/convnext/convnext_xlarge_22k_224.pth",
         hf_hub_id='timm/',
         num_classes=21841),
+
+    'convnextv2_nano.fcmae_ft_in22k_in1k': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_nano_22k_224_ema.pt',
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_nano.fcmae_ft_in22k_in1k_384': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_nano_22k_384_ema.pt',
+        hf_hub_id='timm/',
+        input_size=(3, 384, 384), pool_size=(12, 12), crop_pct=1.0, crop_mode='squash'),
+    'convnextv2_tiny.fcmae_ft_in22k_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_tiny_22k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_tiny.fcmae_ft_in22k_in1k_384': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_tiny_22k_384_ema.pt",
+        hf_hub_id='timm/',
+        input_size=(3, 384, 384), pool_size=(12, 12), crop_pct=1.0, crop_mode='squash'),
+    'convnextv2_base.fcmae_ft_in22k_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_base_22k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_base.fcmae_ft_in22k_in1k_384': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_base_22k_384_ema.pt",
+        hf_hub_id='timm/',
+        input_size=(3, 384, 384), pool_size=(12, 12), crop_pct=1.0, crop_mode='squash'),
+    'convnextv2_large.fcmae_ft_in22k_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_large_22k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_large.fcmae_ft_in22k_in1k_384': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_large_22k_384_ema.pt",
+        hf_hub_id='timm/',
+        input_size=(3, 384, 384), pool_size=(12, 12), crop_pct=1.0, crop_mode='squash'),
+    'convnextv2_huge.fcmae_ft_in22k_in1k_384': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_huge_22k_384_ema.pt",
+        hf_hub_id='timm/',
+        input_size=(3, 384, 384), pool_size=(12, 12), crop_pct=1.0, crop_mode='squash'),
+    'convnextv2_huge.fcmae_ft_in22k_in1k_512': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im22k/convnextv2_huge_22k_512_ema.pt",
+        hf_hub_id='timm/',
+        input_size=(3, 512, 512), pool_size=(15, 15), crop_pct=1.0, crop_mode='squash'),
+
+    'convnextv2_atto.fcmae_ft_in1k': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_atto_1k_224_ema.pt',
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=0.95),
+    'convnextv2_femto.fcmae_ft_in1k': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_femto_1k_224_ema.pt',
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=0.95),
+    'convnextv2_pico.fcmae_ft_in1k': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_pico_1k_224_ema.pt',
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=0.95),
+    'convnextv2_nano.fcmae_ft_in1k': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_nano_1k_224_ema.pt',
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_tiny.fcmae_ft_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_tiny_1k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_base.fcmae_ft_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_base_1k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_large.fcmae_ft_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_large_1k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+    'convnextv2_huge.fcmae_ft_in1k': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/im1k/convnextv2_huge_1k_224_ema.pt",
+        hf_hub_id='timm/',
+        test_input_size=(3, 288, 288), test_crop_pct=1.0),
+
+    'convnextv2_atto.fcmae': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_atto_1k_224_fcmae.pt',
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_femto.fcmae': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_femto_1k_224_fcmae.pt',
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_pico.fcmae': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_pico_1k_224_fcmae.pt',
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_nano.fcmae': _cfgv2(
+        url='https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_nano_1k_224_fcmae.pt',
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_tiny.fcmae': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_tiny_1k_224_fcmae.pt",
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_base.fcmae': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_base_1k_224_fcmae.pt",
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_large.fcmae': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_large_1k_224_fcmae.pt",
+        hf_hub_id='timm/',
+        num_classes=0),
+    'convnextv2_huge.fcmae': _cfgv2(
+        url="https://dl.fbaipublicfiles.com/convnext/convnextv2/pt_only/convnextv2_huge_1k_224_fcmae.pt",
+        hf_hub_id='timm/',
+        num_classes=0),
+
+    'convnextv2_small.untrained': _cfg(),
 })
 
 
 @register_model
 def convnext_atto(pretrained=False, **kwargs):
     # timm femto variant (NOTE: still tweaking depths, will vary between 3-4M param, current is 3.7M
     model_args = dict(
@@ -619,7 +805,79 @@
 
 
 @register_model
 def convnext_xxlarge(pretrained=False, **kwargs):
     model_args = dict(depths=[3, 4, 30, 3], dims=[384, 768, 1536, 3072], **kwargs)
     model = _create_convnext('convnext_xxlarge', pretrained=pretrained, **model_args)
     return model
+
+
+@register_model
+def convnextv2_atto(pretrained=False, **kwargs):
+    # timm femto variant (NOTE: still tweaking depths, will vary between 3-4M param, current is 3.7M
+    model_args = dict(
+        depths=(2, 2, 6, 2), dims=(40, 80, 160, 320), use_grn=True, ls_init_value=None, conv_mlp=True, **kwargs)
+    model = _create_convnext('convnextv2_atto', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_femto(pretrained=False, **kwargs):
+    # timm femto variant
+    model_args = dict(
+        depths=(2, 2, 6, 2), dims=(48, 96, 192, 384), use_grn=True, ls_init_value=None, conv_mlp=True, **kwargs)
+    model = _create_convnext('convnextv2_femto', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_pico(pretrained=False, **kwargs):
+    # timm pico variant
+    model_args = dict(
+        depths=(2, 2, 6, 2), dims=(64, 128, 256, 512), use_grn=True, ls_init_value=None, conv_mlp=True, **kwargs)
+    model = _create_convnext('convnextv2_pico', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_nano(pretrained=False, **kwargs):
+    # timm nano variant with standard stem and head
+    model_args = dict(
+        depths=(2, 2, 8, 2), dims=(80, 160, 320, 640), use_grn=True, ls_init_value=None, conv_mlp=True, **kwargs)
+    model = _create_convnext('convnextv2_nano', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_tiny(pretrained=False, **kwargs):
+    model_args = dict(
+        depths=(3, 3, 9, 3), dims=(96, 192, 384, 768), use_grn=True, ls_init_value=None, **kwargs)
+    model = _create_convnext('convnextv2_tiny', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_small(pretrained=False, **kwargs):
+    model_args = dict(depths=[3, 3, 27, 3], dims=[96, 192, 384, 768], use_grn=True, ls_init_value=None, **kwargs)
+    model = _create_convnext('convnextv2_small', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_base(pretrained=False, **kwargs):
+    model_args = dict(depths=[3, 3, 27, 3], dims=[128, 256, 512, 1024], use_grn=True, ls_init_value=None, **kwargs)
+    model = _create_convnext('convnextv2_base', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_large(pretrained=False, **kwargs):
+    model_args = dict(depths=[3, 3, 27, 3], dims=[192, 384, 768, 1536], use_grn=True, ls_init_value=None, **kwargs)
+    model = _create_convnext('convnextv2_large', pretrained=pretrained, **model_args)
+    return model
+
+
+@register_model
+def convnextv2_huge(pretrained=False, **kwargs):
+    model_args = dict(depths=[3, 3, 27, 3], dims=[352, 704, 1408, 2816], use_grn=True, ls_init_value=None, **kwargs)
+    model = _create_convnext('convnextv2_huge', pretrained=pretrained, **model_args)
+    return model
```

### Comparing `timm-0.8.3.dev0/timm/models/crossvit.py` & `timm-0.8.6.dev0/timm/models/crossvit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/cspnet.py` & `timm-0.8.6.dev0/timm/models/cspnet.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 
 Based on paper `CSPNet: A New Backbone that can Enhance Learning Capability of CNN` - https://arxiv.org/abs/1911.11929
 
 Reference impl via darknet cfg files at https://github.com/WongKinYiu/CrossStagePartialNetworks
 
 Hacked together by / Copyright 2020 Ross Wightman
 """
-from dataclasses import dataclass, asdict
+from dataclasses import dataclass, asdict, replace
 from functools import partial
 from typing import Any, Dict, Optional, Tuple, Union
 
 import torch
 import torch.nn as nn
 
 from timm.data import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
@@ -514,15 +514,15 @@
             groups=1,
             first_dilation=None,
             avg_down=False,
             down_growth=False,
             cross_linear=False,
             block_dpr=None,
             block_fn=BottleneckBlock,
-            **block_kwargs
+            **block_kwargs,
     ):
         super(CrossStage, self).__init__()
         first_dilation = first_dilation or dilation
         down_chs = out_chs if down_growth else in_chs  # grow downsample channels to output channels
         self.expand_chs = exp_chs = int(round(out_chs * expand_ratio))
         block_out_chs = int(round(out_chs * block_ratio))
         conv_kwargs = dict(act_layer=block_kwargs.get('act_layer'), norm_layer=block_kwargs.get('norm_layer'))
@@ -554,15 +554,15 @@
             self.blocks.add_module(str(i), block_fn(
                 in_chs=prev_chs,
                 out_chs=block_out_chs,
                 dilation=dilation,
                 bottle_ratio=bottle_ratio,
                 groups=groups,
                 drop_path=block_dpr[i] if block_dpr is not None else 0.,
-                **block_kwargs
+                **block_kwargs,
             ))
             prev_chs = block_out_chs
 
         # transition convs
         self.conv_transition_b = ConvNormAct(prev_chs, exp_chs // 2, kernel_size=1, **conv_kwargs)
         self.conv_transition = ConvNormAct(exp_chs, out_chs, kernel_size=1, **conv_kwargs)
 
@@ -593,15 +593,15 @@
             groups=1,
             first_dilation=None,
             avg_down=False,
             down_growth=False,
             cross_linear=False,
             block_dpr=None,
             block_fn=BottleneckBlock,
-            **block_kwargs
+            **block_kwargs,
     ):
         super(CrossStage3, self).__init__()
         first_dilation = first_dilation or dilation
         down_chs = out_chs if down_growth else in_chs  # grow downsample channels to output channels
         self.expand_chs = exp_chs = int(round(out_chs * expand_ratio))
         block_out_chs = int(round(out_chs * block_ratio))
         conv_kwargs = dict(act_layer=block_kwargs.get('act_layer'), norm_layer=block_kwargs.get('norm_layer'))
@@ -631,15 +631,15 @@
             self.blocks.add_module(str(i), block_fn(
                 in_chs=prev_chs,
                 out_chs=block_out_chs,
                 dilation=dilation,
                 bottle_ratio=bottle_ratio,
                 groups=groups,
                 drop_path=block_dpr[i] if block_dpr is not None else 0.,
-                **block_kwargs
+                **block_kwargs,
             ))
             prev_chs = block_out_chs
 
         # transition convs
         self.conv_transition = ConvNormAct(exp_chs, out_chs, kernel_size=1, **conv_kwargs)
 
     def forward(self, x):
@@ -664,15 +664,15 @@
             block_ratio=1.,
             bottle_ratio=1.,
             groups=1,
             first_dilation=None,
             avg_down=False,
             block_fn=BottleneckBlock,
             block_dpr=None,
-            **block_kwargs
+            **block_kwargs,
     ):
         super(DarkStage, self).__init__()
         first_dilation = first_dilation or dilation
         conv_kwargs = dict(act_layer=block_kwargs.get('act_layer'), norm_layer=block_kwargs.get('norm_layer'))
         aa_layer = block_kwargs.pop('aa_layer', None)
 
         if avg_down:
@@ -711,15 +711,15 @@
         out_chs=32,
         kernel_size=3,
         stride=2,
         pool='',
         padding='',
         act_layer=nn.ReLU,
         norm_layer=nn.BatchNorm2d,
-        aa_layer=None
+        aa_layer=None,
 ):
     stem = nn.Sequential()
     feature_info = []
     if not isinstance(out_chs, (tuple, list)):
         out_chs = [out_chs]
     stem_depth = len(out_chs)
     assert stem_depth
@@ -734,15 +734,15 @@
         if conv_stride > 1 and prev_feat is not None:
             feature_info.append(prev_feat)
         stem.add_module(conv_name, ConvNormAct(
             prev_chs, chs, kernel_size,
             stride=conv_stride,
             padding=padding if i == 0 else '',
             act_layer=act_layer,
-            norm_layer=norm_layer
+            norm_layer=norm_layer,
         ))
         stem_stride *= conv_stride
         prev_chs = chs
         prev_feat = dict(num_chs=prev_chs, reduction=stem_stride, module='.'.join(['stem', conv_name]))
     if pool:
         assert stride > 2
         if prev_feat is not None:
@@ -796,15 +796,15 @@
     return attn_layer, stage_args
 
 
 def create_csp_stages(
         cfg: CspModelCfg,
         drop_path_rate: float,
         output_stride: int,
-        stem_feat: Dict[str, Any]
+        stem_feat: Dict[str, Any],
 ):
     cfg_dict = asdict(cfg.stages)
     num_stages = len(cfg.stages.depth)
     cfg_dict['block_dpr'] = [None] * num_stages if not drop_path_rate else \
         [x.tolist() for x in torch.linspace(0, drop_path_rate, sum(cfg.stages.depth)).split(cfg.stages.depth)]
     stage_args = [dict(zip(cfg_dict.keys(), values)) for values in zip(*cfg_dict.values())]
     block_kwargs = dict(
@@ -864,20 +864,35 @@
             cfg: CspModelCfg,
             in_chans=3,
             num_classes=1000,
             output_stride=32,
             global_pool='avg',
             drop_rate=0.,
             drop_path_rate=0.,
-            zero_init_last=True
+            zero_init_last=True,
+            **kwargs,
     ):
+        """
+        Args:
+            cfg (CspModelCfg): Model architecture configuration
+            in_chans (int): Number of input channels (default: 3)
+            num_classes (int): Number of classifier classes (default: 1000)
+            output_stride (int): Output stride of network, one of (8, 16, 32) (default: 32)
+            global_pool (str): Global pooling type (default: 'avg')
+            drop_rate (float): Dropout rate (default: 0.)
+            drop_path_rate (float): Stochastic depth drop-path rate (default: 0.)
+            zero_init_last (bool): Zero-init last weight of residual path
+            kwargs (dict): Extra kwargs overlayed onto cfg
+        """
         super().__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         assert output_stride in (8, 16, 32)
+
+        cfg = replace(cfg, **kwargs)  # overlay kwargs onto cfg
         layer_args = dict(
             act_layer=cfg.act_layer,
             norm_layer=cfg.norm_layer,
             aa_layer=cfg.aa_layer
         )
         self.feature_info = []
```

### Comparing `timm-0.8.3.dev0/timm/models/deit.py` & `timm-0.8.6.dev0/timm/models/deit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/densenet.py` & `timm-0.8.6.dev0/timm/models/densenet.py`

 * *Files 3% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 import torch
 import torch.nn as nn
 import torch.nn.functional as F
 import torch.utils.checkpoint as cp
 from torch.jit.annotations import List
 
 from timm.data import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
-from timm.layers import BatchNormAct2d, create_norm_act_layer, BlurPool2d, create_classifier
+from timm.layers import BatchNormAct2d, get_norm_act_layer, BlurPool2d, create_classifier
 from ._builder import build_model_with_cfg
 from ._manipulate import MATCH_PREV_GROUP
 from ._registry import register_model
 
 __all__ = ['DenseNet']
 
 
@@ -111,16 +111,23 @@
         return new_features
 
 
 class DenseBlock(nn.ModuleDict):
     _version = 2
 
     def __init__(
-            self, num_layers, num_input_features, bn_size, growth_rate, norm_layer=BatchNormAct2d,
-            drop_rate=0., memory_efficient=False):
+            self,
+            num_layers,
+            num_input_features,
+            bn_size,
+            growth_rate,
+            norm_layer=BatchNormAct2d,
+            drop_rate=0.,
+            memory_efficient=False,
+    ):
         super(DenseBlock, self).__init__()
         for i in range(num_layers):
             layer = DenseLayer(
                 num_input_features + i * growth_rate,
                 growth_rate=growth_rate,
                 bn_size=bn_size,
                 norm_layer=norm_layer,
@@ -161,20 +168,33 @@
         drop_rate (float) - dropout rate after each dense layer
         num_classes (int) - number of classification classes
         memory_efficient (bool) - If True, uses checkpointing. Much more memory efficient,
           but slower. Default: *False*. See `"paper" <https://arxiv.org/pdf/1707.06990.pdf>`_
     """
 
     def __init__(
-            self, growth_rate=32, block_config=(6, 12, 24, 16), num_classes=1000, in_chans=3, global_pool='avg',
-            bn_size=4, stem_type='', norm_layer=BatchNormAct2d, aa_layer=None, drop_rate=0,
-            memory_efficient=False, aa_stem_only=True):
+            self,
+            growth_rate=32,
+            block_config=(6, 12, 24, 16),
+            num_classes=1000,
+            in_chans=3,
+            global_pool='avg',
+            bn_size=4,
+            stem_type='',
+            act_layer='relu',
+            norm_layer='batchnorm2d',
+            aa_layer=None,
+            drop_rate=0,
+            memory_efficient=False,
+            aa_stem_only=True,
+    ):
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         super(DenseNet, self).__init__()
+        norm_layer = get_norm_act_layer(norm_layer, act_layer=act_layer)
 
         # Stem
         deep_stem = 'deep' in stem_type  # 3x3 deep stem
         num_init_features = growth_rate * 2
         if aa_layer is None:
             stem_pool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
         else:
@@ -222,16 +242,19 @@
             num_features = num_features + num_layers * growth_rate
             transition_aa_layer = None if aa_stem_only else aa_layer
             if i != len(block_config) - 1:
                 self.feature_info += [
                     dict(num_chs=num_features, reduction=current_stride, module='features.' + module_name)]
                 current_stride *= 2
                 trans = DenseTransition(
-                    num_input_features=num_features, num_output_features=num_features // 2,
-                    norm_layer=norm_layer, aa_layer=transition_aa_layer)
+                    num_input_features=num_features,
+                    num_output_features=num_features // 2,
+                    norm_layer=norm_layer,
+                    aa_layer=transition_aa_layer,
+                )
                 self.features.add_module(f'transition{i + 1}', trans)
                 num_features = num_features // 2
 
         # Final batch norm
         self.features.add_module('norm5', norm_layer(num_features))
 
         self.feature_info += [dict(num_chs=num_features, reduction=current_stride, module='features.norm5')]
@@ -318,16 +341,16 @@
 
 @register_model
 def densenetblur121d(pretrained=False, **kwargs):
     r"""Densenet-121 model from
     `"Densely Connected Convolutional Networks" <https://arxiv.org/pdf/1608.06993.pdf>`
     """
     model = _create_densenet(
-        'densenetblur121d', growth_rate=32, block_config=(6, 12, 24, 16), pretrained=pretrained, stem_type='deep',
-        aa_layer=BlurPool2d, **kwargs)
+        'densenetblur121d', growth_rate=32, block_config=(6, 12, 24, 16), pretrained=pretrained,
+        stem_type='deep', aa_layer=BlurPool2d, **kwargs)
     return model
 
 
 @register_model
 def densenet121d(pretrained=False, **kwargs):
     r"""Densenet-121 model from
     `"Densely Connected Convolutional Networks" <https://arxiv.org/pdf/1608.06993.pdf>`
@@ -378,19 +401,17 @@
     return model
 
 
 @register_model
 def densenet264d_iabn(pretrained=False, **kwargs):
     r"""Densenet-264 model with deep stem and Inplace-ABN
     """
-    def norm_act_fn(num_features, **kwargs):
-        return create_norm_act_layer('iabn', num_features, act_layer='leaky_relu', **kwargs)
     model = _create_densenet(
         'densenet264d_iabn', growth_rate=48, block_config=(6, 12, 64, 48), stem_type='deep',
-        norm_layer=norm_act_fn, pretrained=pretrained, **kwargs)
+        norm_layer='iabn', act_layer='leaky_relu', pretrained=pretrained, **kwargs)
     return model
 
 
 @register_model
 def tv_densenet121(pretrained=False, **kwargs):
     r"""Densenet-121 model with original Torchvision weights, from
     `"Densely Connected Convolutional Networks" <https://arxiv.org/pdf/1608.06993.pdf>`
```

### Comparing `timm-0.8.3.dev0/timm/models/dla.py` & `timm-0.8.6.dev0/timm/models/dla.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/dpn.py` & `timm-0.8.6.dev0/timm/models/dpn.py`

 * *Files 9% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 from typing import Tuple
 
 import torch
 import torch.nn as nn
 import torch.nn.functional as F
 
 from timm.data import IMAGENET_DPN_MEAN, IMAGENET_DPN_STD, IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
-from timm.layers import BatchNormAct2d, ConvNormAct, create_conv2d, create_classifier
+from timm.layers import BatchNormAct2d, ConvNormAct, create_conv2d, create_classifier, get_norm_act_layer
 from ._builder import build_model_with_cfg
 from ._registry import register_model
 
 __all__ = ['DPN']
 
 
 def _cfg(url='', **kwargs):
@@ -29,14 +29,15 @@
         'mean': IMAGENET_DPN_MEAN, 'std': IMAGENET_DPN_STD,
         'first_conv': 'features.conv1_1.conv', 'classifier': 'classifier',
         **kwargs
     }
 
 
 default_cfgs = {
+    'dpn48b': _cfg(mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD),
     'dpn68': _cfg(
         url='https://github.com/rwightman/pytorch-dpn-pretrained/releases/download/v0.1/dpn68-66bebafa7.pth'),
     'dpn68b': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-weights/dpn68b_ra-a31ca160.pth',
         mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD),
     'dpn92': _cfg(
         url='https://github.com/rwightman/pytorch-dpn-pretrained/releases/download/v0.1/dpn92_extra-b040e4a9b.pth'),
@@ -78,15 +79,24 @@
 
     def forward(self, x):
         return self.conv(self.bn(x))
 
 
 class DualPathBlock(nn.Module):
     def __init__(
-            self, in_chs, num_1x1_a, num_3x3_b, num_1x1_c, inc, groups, block_type='normal', b=False):
+            self,
+            in_chs,
+            num_1x1_a,
+            num_3x3_b,
+            num_1x1_c,
+            inc,
+            groups,
+            block_type='normal',
+            b=False,
+    ):
         super(DualPathBlock, self).__init__()
         self.num_1x1_c = num_1x1_c
         self.inc = inc
         self.b = b
         if block_type == 'proj':
             self.key_stride = 1
             self.has_proj = True
@@ -163,24 +173,39 @@
         resid = x_s1 + out1
         dense = torch.cat([x_s2, out2], dim=1)
         return resid, dense
 
 
 class DPN(nn.Module):
     def __init__(
-            self, small=False, num_init_features=64, k_r=96, groups=32, global_pool='avg',
-            b=False, k_sec=(3, 4, 20, 3), inc_sec=(16, 32, 24, 128), output_stride=32,
-            num_classes=1000, in_chans=3, drop_rate=0., fc_act_layer=nn.ELU):
+            self,
+            k_sec=(3, 4, 20, 3),
+            inc_sec=(16, 32, 24, 128),
+            k_r=96,
+            groups=32,
+            num_classes=1000,
+            in_chans=3,
+            output_stride=32,
+            global_pool='avg',
+            small=False,
+            num_init_features=64,
+            b=False,
+            drop_rate=0.,
+            norm_layer='batchnorm2d',
+            act_layer='relu',
+            fc_act_layer='elu',
+    ):
         super(DPN, self).__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         self.b = b
         assert output_stride == 32  # FIXME look into dilation support
-        norm_layer = partial(BatchNormAct2d, eps=.001)
-        fc_norm_layer = partial(BatchNormAct2d, eps=.001, act_layer=fc_act_layer, inplace=False)
+
+        norm_layer = partial(get_norm_act_layer(norm_layer, act_layer=act_layer), eps=.001)
+        fc_norm_layer = partial(get_norm_act_layer(norm_layer, act_layer=fc_act_layer), eps=.001, inplace=False)
         bw_factor = 1 if small else 4
         blocks = OrderedDict()
 
         # conv1
         blocks['conv1_1'] = ConvNormAct(
             in_chans, num_init_features, kernel_size=3 if small else 7, stride=2, norm_layer=norm_layer)
         blocks['conv1_pool'] = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
@@ -288,52 +313,60 @@
     return build_model_with_cfg(
         DPN, variant, pretrained,
         feature_cfg=dict(feature_concat=True, flatten_sequential=True),
         **kwargs)
 
 
 @register_model
+def dpn48b(pretrained=False, **kwargs):
+    model_kwargs = dict(
+        small=True, num_init_features=10, k_r=128, groups=32,
+        b=True, k_sec=(3, 4, 6, 3), inc_sec=(16, 32, 32, 64), act_layer='silu')
+    return _create_dpn('dpn48b', pretrained=pretrained, **dict(model_kwargs, **kwargs))
+
+
+@register_model
 def dpn68(pretrained=False, **kwargs):
     model_kwargs = dict(
         small=True, num_init_features=10, k_r=128, groups=32,
-        k_sec=(3, 4, 12, 3), inc_sec=(16, 32, 32, 64), **kwargs)
-    return _create_dpn('dpn68', pretrained=pretrained, **model_kwargs)
+        k_sec=(3, 4, 12, 3), inc_sec=(16, 32, 32, 64))
+    return _create_dpn('dpn68', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def dpn68b(pretrained=False, **kwargs):
     model_kwargs = dict(
         small=True, num_init_features=10, k_r=128, groups=32,
-        b=True, k_sec=(3, 4, 12, 3), inc_sec=(16, 32, 32, 64), **kwargs)
-    return _create_dpn('dpn68b', pretrained=pretrained, **model_kwargs)
+        b=True, k_sec=(3, 4, 12, 3), inc_sec=(16, 32, 32, 64))
+    return _create_dpn('dpn68b', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def dpn92(pretrained=False, **kwargs):
     model_kwargs = dict(
         num_init_features=64, k_r=96, groups=32,
-        k_sec=(3, 4, 20, 3), inc_sec=(16, 32, 24, 128), **kwargs)
-    return _create_dpn('dpn92', pretrained=pretrained, **model_kwargs)
+        k_sec=(3, 4, 20, 3), inc_sec=(16, 32, 24, 128))
+    return _create_dpn('dpn92', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def dpn98(pretrained=False, **kwargs):
     model_kwargs = dict(
         num_init_features=96, k_r=160, groups=40,
-        k_sec=(3, 6, 20, 3), inc_sec=(16, 32, 32, 128), **kwargs)
-    return _create_dpn('dpn98', pretrained=pretrained, **model_kwargs)
+        k_sec=(3, 6, 20, 3), inc_sec=(16, 32, 32, 128))
+    return _create_dpn('dpn98', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def dpn131(pretrained=False, **kwargs):
     model_kwargs = dict(
         num_init_features=128, k_r=160, groups=40,
-        k_sec=(4, 8, 28, 3), inc_sec=(16, 32, 32, 128), **kwargs)
-    return _create_dpn('dpn131', pretrained=pretrained, **model_kwargs)
+        k_sec=(4, 8, 28, 3), inc_sec=(16, 32, 32, 128))
+    return _create_dpn('dpn131', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def dpn107(pretrained=False, **kwargs):
     model_kwargs = dict(
         num_init_features=128, k_r=200, groups=50,
-        k_sec=(4, 8, 20, 3), inc_sec=(20, 64, 64, 128), **kwargs)
-    return _create_dpn('dpn107', pretrained=pretrained, **model_kwargs)
+        k_sec=(4, 8, 20, 3), inc_sec=(20, 64, 64, 128))
+    return _create_dpn('dpn107', pretrained=pretrained, **dict(model_kwargs, **kwargs))
```

### Comparing `timm-0.8.3.dev0/timm/models/edgenext.py` & `timm-0.8.6.dev0/timm/models/edgenext.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/efficientformer.py` & `timm-0.8.6.dev0/timm/models/efficientformer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/efficientnet.py` & `timm-0.8.6.dev0/timm/models/efficientnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/gcvit.py` & `timm-0.8.6.dev0/timm/models/gcvit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/ghostnet.py` & `timm-0.8.6.dev0/timm/models/ghostnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/gluon_resnet.py` & `timm-0.8.6.dev0/timm/models/gluon_resnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/gluon_xception.py` & `timm-0.8.6.dev0/timm/models/gluon_xception.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/hardcorenas.py` & `timm-0.8.6.dev0/timm/models/hardcorenas.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/hrnet.py` & `timm-0.8.6.dev0/timm/models/hrnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/inception_resnet_v2.py` & `timm-0.8.6.dev0/timm/models/inception_resnet_v2.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/inception_v3.py` & `timm-0.8.6.dev0/timm/models/inception_v3.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/inception_v4.py` & `timm-0.8.6.dev0/timm/models/inception_v4.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/layers/__init__.py` & `timm-0.8.6.dev0/timm/models/layers/__init__.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/levit.py` & `timm-0.8.6.dev0/timm/models/levit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/maxxvit.py` & `timm-0.8.6.dev0/timm/models/maxxvit.py`

 * *Files 2% similar despite different names*

```diff
@@ -1112,32 +1112,55 @@
         x = self.pre_logits(x)
         if pre_logits:
             return x
         x = self.fc(x)
         return x
 
 
+def _overlay_kwargs(cfg: MaxxVitCfg, **kwargs):
+    transformer_kwargs = {}
+    conv_kwargs = {}
+    base_kwargs = {}
+    for k, v in kwargs.items():
+        if k.startswith('transformer_'):
+            transformer_kwargs[k.replace('transformer_', '')] = v
+        elif k.startswith('conv_'):
+            conv_kwargs[k.replace('conv_', '')] = v
+        else:
+            base_kwargs[k] = v
+    cfg = replace(
+        cfg,
+        transformer_cfg=replace(cfg.transformer_cfg, **transformer_kwargs),
+        conv_cfg=replace(cfg.conv_cfg, **conv_kwargs),
+        **base_kwargs
+    )
+    return cfg
+
+
 class MaxxVit(nn.Module):
     """ CoaTNet + MaxVit base model.
 
     Highly configurable for different block compositions, tensor layouts, pooling types.
     """
 
     def __init__(
             self,
             cfg: MaxxVitCfg,
             img_size: Union[int, Tuple[int, int]] = 224,
             in_chans: int = 3,
             num_classes: int = 1000,
             global_pool: str = 'avg',
             drop_rate: float = 0.,
-            drop_path_rate: float = 0.
+            drop_path_rate: float = 0.,
+            **kwargs,
     ):
         super().__init__()
         img_size = to_2tuple(img_size)
+        if kwargs:
+            cfg = _overlay_kwargs(cfg, **kwargs)
         transformer_cfg = cfg_window_size(cfg.transformer_cfg, img_size)
         self.num_classes = num_classes
         self.global_pool = global_pool
         self.num_features = self.embed_dim = cfg.embed_dim[-1]
         self.drop_rate = drop_rate
         self.grad_checkpointing = False
 
@@ -1653,14 +1676,34 @@
         block_type=('M',) * 4,
         stem_width=(32, 64),
         **_rw_max_cfg(
             rel_pos_type='mlp',
             init_values=1e-6,
         ),
     ),
+    maxvit_rmlp_base_rw_224=MaxxVitCfg(
+        embed_dim=(96, 192, 384, 768),
+        depths=(2, 6, 14, 2),
+        block_type=('M',) * 4,
+        stem_width=(32, 64),
+        head_hidden_size=768,
+        **_rw_max_cfg(
+            rel_pos_type='mlp',
+        ),
+    ),
+    maxvit_rmlp_base_rw_384=MaxxVitCfg(
+        embed_dim=(96, 192, 384, 768),
+        depths=(2, 6, 14, 2),
+        block_type=('M',) * 4,
+        stem_width=(32, 64),
+        head_hidden_size=768,
+        **_rw_max_cfg(
+            rel_pos_type='mlp',
+        ),
+    ),
 
     maxvit_tiny_pm_256=MaxxVitCfg(
         embed_dim=(64, 128, 256, 512),
         depths=(2, 2, 5, 2),
         block_type=('PM',) * 4,
         stem_width=(32, 64),
         **_rw_max_cfg(),
@@ -1835,14 +1878,20 @@
     'maxvit_rmlp_small_rw_224': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-weights-maxx/maxvit_rmlp_small_rw_224_sw-6ef0ae4f.pth',
         crop_pct=0.9,
     ),
     'maxvit_rmlp_small_rw_256': _cfg(
         url='',
         input_size=(3, 256, 256), pool_size=(8, 8)),
+    'maxvit_rmlp_base_rw_224': _cfg(
+        url='',
+    ),
+    'maxvit_rmlp_base_rw_384': _cfg(
+        url='',
+        input_size=(3, 384, 384), pool_size=(12, 12)),
 
     'maxvit_tiny_pm_256': _cfg(url='', input_size=(3, 256, 256), pool_size=(8, 8)),
 
     'maxxvit_rmlp_nano_rw_256': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-weights-maxx/maxxvit_rmlp_nano_rw_256_sw-0325d459.pth',
         input_size=(3, 256, 256), pool_size=(8, 8)),
     'maxxvit_rmlp_tiny_rw_256': _cfg(url='', input_size=(3, 256, 256), pool_size=(8, 8)),
@@ -2065,14 +2114,24 @@
 
 @register_model
 def maxvit_rmlp_small_rw_256(pretrained=False, **kwargs):
     return _create_maxxvit('maxvit_rmlp_small_rw_256', pretrained=pretrained, **kwargs)
 
 
 @register_model
+def maxvit_rmlp_base_rw_224(pretrained=False, **kwargs):
+    return _create_maxxvit('maxvit_rmlp_base_rw_224', pretrained=pretrained, **kwargs)
+
+
+@register_model
+def maxvit_rmlp_base_rw_384(pretrained=False, **kwargs):
+    return _create_maxxvit('maxvit_rmlp_base_rw_384', pretrained=pretrained, **kwargs)
+
+
+@register_model
 def maxvit_tiny_pm_256(pretrained=False, **kwargs):
     return _create_maxxvit('maxvit_tiny_pm_256', pretrained=pretrained, **kwargs)
 
 
 @register_model
 def maxxvit_rmlp_nano_rw_256(pretrained=False, **kwargs):
     return _create_maxxvit('maxxvit_rmlp_nano_rw_256', pretrained=pretrained, **kwargs)
```

### Comparing `timm-0.8.3.dev0/timm/models/mlp_mixer.py` & `timm-0.8.6.dev0/timm/models/mlp_mixer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/mobilenetv3.py` & `timm-0.8.6.dev0/timm/models/mobilenetv3.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/mobilevit.py` & `timm-0.8.6.dev0/timm/models/mobilevit.py`

 * *Files 1% similar despite different names*

```diff
@@ -262,17 +262,24 @@
         self.conv_kxk = layers.conv_norm_act(
             in_chs, in_chs, kernel_size=kernel_size,
             stride=stride, groups=groups, dilation=dilation[0])
         self.conv_1x1 = nn.Conv2d(in_chs, transformer_dim, kernel_size=1, bias=False)
 
         self.transformer = nn.Sequential(*[
             TransformerBlock(
-                transformer_dim, mlp_ratio=mlp_ratio, num_heads=num_heads, qkv_bias=True,
-                attn_drop=attn_drop, drop=drop, drop_path=drop_path_rate,
-                act_layer=layers.act, norm_layer=transformer_norm_layer)
+                transformer_dim,
+                mlp_ratio=mlp_ratio,
+                num_heads=num_heads,
+                qkv_bias=True,
+                attn_drop=attn_drop,
+                drop=drop,
+                drop_path=drop_path_rate,
+                act_layer=layers.act,
+                norm_layer=transformer_norm_layer,
+            )
             for _ in range(transformer_depth)
         ])
         self.norm = transformer_norm_layer(transformer_dim)
 
         self.conv_proj = layers.conv_norm_act(transformer_dim, out_chs, kernel_size=1, stride=1)
 
         if no_fusion:
```

### Comparing `timm-0.8.3.dev0/timm/models/mvitv2.py` & `timm-0.8.6.dev0/timm/models/mvitv2.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/nasnet.py` & `timm-0.8.6.dev0/timm/models/nasnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/nest.py` & `timm-0.8.6.dev0/timm/models/nest.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/nfnet.py` & `timm-0.8.6.dev0/timm/models/nfnet.py`

 * *Files 3% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 * Pretrained weights for two models so far, more to come.
 * Model details updated to closer match official JAX code now that it's released
 * NF-ResNet, NF-RegNet-B, and NFNet-F models supported
 
 Hacked together by / copyright Ross Wightman, 2021.
 """
 from collections import OrderedDict
-from dataclasses import dataclass
+from dataclasses import dataclass, replace
 from functools import partial
 from typing import Tuple, Optional
 
 import torch
 import torch.nn as nn
 
 from timm.data import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
@@ -155,48 +155,104 @@
     std_conv_eps: float = 1e-5
     skipinit: bool = False  # disabled by default, non-trivial performance impact
     zero_init_fc: bool = False
     act_layer: str = 'silu'
 
 
 def _nfres_cfg(
-        depths, channels=(256, 512, 1024, 2048), group_size=None, act_layer='relu', attn_layer=None, attn_kwargs=None):
+        depths,
+        channels=(256, 512, 1024, 2048),
+        group_size=None,
+        act_layer='relu',
+        attn_layer=None,
+        attn_kwargs=None,
+):
     attn_kwargs = attn_kwargs or {}
     cfg = NfCfg(
-        depths=depths, channels=channels, stem_type='7x7_pool', stem_chs=64, bottle_ratio=0.25,
-        group_size=group_size, act_layer=act_layer, attn_layer=attn_layer, attn_kwargs=attn_kwargs)
+        depths=depths,
+        channels=channels,
+        stem_type='7x7_pool',
+        stem_chs=64,
+        bottle_ratio=0.25,
+        group_size=group_size,
+        act_layer=act_layer,
+        attn_layer=attn_layer,
+        attn_kwargs=attn_kwargs,
+    )
     return cfg
 
 
 def _nfreg_cfg(depths, channels=(48, 104, 208, 440)):
     num_features = 1280 * channels[-1] // 440
     attn_kwargs = dict(rd_ratio=0.5)
     cfg = NfCfg(
-        depths=depths, channels=channels, stem_type='3x3', group_size=8, width_factor=0.75, bottle_ratio=2.25,
-        num_features=num_features, reg=True, attn_layer='se', attn_kwargs=attn_kwargs)
+        depths=depths,
+        channels=channels,
+        stem_type='3x3',
+        group_size=8,
+        width_factor=0.75,
+        bottle_ratio=2.25,
+        num_features=num_features,
+        reg=True,
+        attn_layer='se',
+        attn_kwargs=attn_kwargs,
+    )
     return cfg
 
 
 def _nfnet_cfg(
-        depths, channels=(256, 512, 1536, 1536), group_size=128, bottle_ratio=0.5, feat_mult=2.,
-        act_layer='gelu', attn_layer='se', attn_kwargs=None):
+        depths,
+        channels=(256, 512, 1536, 1536),
+        group_size=128,
+        bottle_ratio=0.5,
+        feat_mult=2.,
+        act_layer='gelu',
+        attn_layer='se',
+        attn_kwargs=None,
+):
     num_features = int(channels[-1] * feat_mult)
     attn_kwargs = attn_kwargs if attn_kwargs is not None else dict(rd_ratio=0.5)
     cfg = NfCfg(
-        depths=depths, channels=channels, stem_type='deep_quad', stem_chs=128, group_size=group_size,
-        bottle_ratio=bottle_ratio, extra_conv=True, num_features=num_features, act_layer=act_layer,
-        attn_layer=attn_layer, attn_kwargs=attn_kwargs)
+        depths=depths,
+        channels=channels,
+        stem_type='deep_quad',
+        stem_chs=128,
+        group_size=group_size,
+        bottle_ratio=bottle_ratio,
+        extra_conv=True,
+        num_features=num_features,
+        act_layer=act_layer,
+        attn_layer=attn_layer,
+        attn_kwargs=attn_kwargs,
+    )
     return cfg
 
 
-def _dm_nfnet_cfg(depths, channels=(256, 512, 1536, 1536), act_layer='gelu', skipinit=True):
+def _dm_nfnet_cfg(
+        depths,
+        channels=(256, 512, 1536, 1536),
+        act_layer='gelu',
+        skipinit=True,
+):
     cfg = NfCfg(
-        depths=depths, channels=channels, stem_type='deep_quad', stem_chs=128, group_size=128,
-        bottle_ratio=0.5, extra_conv=True, gamma_in_act=True, same_padding=True, skipinit=skipinit,
-        num_features=int(channels[-1] * 2.0), act_layer=act_layer, attn_layer='se', attn_kwargs=dict(rd_ratio=0.5))
+        depths=depths,
+        channels=channels,
+        stem_type='deep_quad',
+        stem_chs=128,
+        group_size=128,
+        bottle_ratio=0.5,
+        extra_conv=True,
+        gamma_in_act=True,
+        same_padding=True,
+        skipinit=skipinit,
+        num_features=int(channels[-1] * 2.0),
+        act_layer=act_layer,
+        attn_layer='se',
+        attn_kwargs=dict(rd_ratio=0.5),
+    )
     return cfg
 
 
 model_cfgs = dict(
     # NFNet-F models w/ GELU compatible with DeepMind weights
     dm_nfnet_f0=_dm_nfnet_cfg(depths=(1, 2, 6, 3)),
     dm_nfnet_f1=_dm_nfnet_cfg(depths=(2, 4, 12, 6)),
@@ -274,15 +330,22 @@
     def _create(inplace=False):
         return GammaAct(act_type, gamma=gamma, inplace=inplace)
     return _create
 
 
 class DownsampleAvg(nn.Module):
     def __init__(
-            self, in_chs, out_chs, stride=1, dilation=1, first_dilation=None, conv_layer=ScaledStdConv2d):
+            self,
+            in_chs,
+            out_chs,
+            stride=1,
+            dilation=1,
+            first_dilation=None,
+            conv_layer=ScaledStdConv2d,
+    ):
         """ AvgPool Downsampling as in 'D' ResNet variants. Support for dilation."""
         super(DownsampleAvg, self).__init__()
         avg_stride = stride if dilation == 1 else 1
         if stride > 1 or dilation > 1:
             avg_pool_fn = AvgPool2dSame if avg_stride == 1 and dilation > 1 else nn.AvgPool2d
             self.pool = avg_pool_fn(2, avg_stride, ceil_mode=True, count_include_pad=False)
         else:
@@ -295,32 +358,55 @@
 
 @register_notrace_module  # reason: mul_ causes FX to drop a relevant node. https://github.com/pytorch/pytorch/issues/68301
 class NormFreeBlock(nn.Module):
     """Normalization-Free pre-activation block.
     """
 
     def __init__(
-            self, in_chs, out_chs=None, stride=1, dilation=1, first_dilation=None,
-            alpha=1.0, beta=1.0, bottle_ratio=0.25, group_size=None, ch_div=1, reg=True, extra_conv=False,
-            skipinit=False, attn_layer=None, attn_gain=2.0, act_layer=None, conv_layer=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs=None,
+            stride=1,
+            dilation=1,
+            first_dilation=None,
+            alpha=1.0,
+            beta=1.0,
+            bottle_ratio=0.25,
+            group_size=None,
+            ch_div=1,
+            reg=True,
+            extra_conv=False,
+            skipinit=False,
+            attn_layer=None,
+            attn_gain=2.0,
+            act_layer=None,
+            conv_layer=None,
+            drop_path_rate=0.,
+    ):
         super().__init__()
         first_dilation = first_dilation or dilation
         out_chs = out_chs or in_chs
         # RegNet variants scale bottleneck from in_chs, otherwise scale from out_chs like ResNet
         mid_chs = make_divisible(in_chs * bottle_ratio if reg else out_chs * bottle_ratio, ch_div)
         groups = 1 if not group_size else mid_chs // group_size
         if group_size and group_size % ch_div == 0:
             mid_chs = group_size * groups  # correct mid_chs if group_size divisible by ch_div, otherwise error
         self.alpha = alpha
         self.beta = beta
         self.attn_gain = attn_gain
 
         if in_chs != out_chs or stride != 1 or dilation != first_dilation:
             self.downsample = DownsampleAvg(
-                in_chs, out_chs, stride=stride, dilation=dilation, first_dilation=first_dilation, conv_layer=conv_layer)
+                in_chs,
+                out_chs,
+                stride=stride,
+                dilation=dilation,
+                first_dilation=first_dilation,
+                conv_layer=conv_layer,
+            )
         else:
             self.downsample = None
 
         self.act1 = act_layer()
         self.conv1 = conv_layer(in_chs, mid_chs, 1)
         self.act2 = act_layer(inplace=True)
         self.conv2 = conv_layer(mid_chs, mid_chs, 3, stride=stride, dilation=first_dilation, groups=groups)
@@ -448,35 +534,59 @@
             impact in PyTorch when done with the weight scaling there. This likely wasn't a concern in the JAX impl.
         * a config option `gamma_in_act` can be enabled to not apply gamma in StdConv as described above, but
             apply it in each activation. This is slightly slower, numerically different, but matches official impl.
         * skipinit is disabled by default, it seems to have a rather drastic impact on GPU memory use and throughput
             for what it is/does. Approx 8-10% throughput loss.
     """
     def __init__(
-            self, cfg: NfCfg, num_classes=1000, in_chans=3, global_pool='avg', output_stride=32,
-            drop_rate=0., drop_path_rate=0.
+            self,
+            cfg: NfCfg,
+            num_classes=1000,
+            in_chans=3,
+            global_pool='avg',
+            output_stride=32,
+            drop_rate=0.,
+            drop_path_rate=0.,
+            **kwargs,
     ):
+        """
+        Args:
+            cfg (NfCfg): Model architecture configuration
+            num_classes (int): Number of classifier classes (default: 1000)
+            in_chans (int): Number of input channels (default: 3)
+            global_pool (str): Global pooling type (default: 'avg')
+            output_stride (int): Output stride of network, one of (8, 16, 32) (default: 32)
+            drop_rate (float): Dropout rate (default: 0.)
+            drop_path_rate (float): Stochastic depth drop-path rate (default: 0.)
+            kwargs (dict): Extra kwargs overlayed onto cfg
+        """
         super().__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         self.grad_checkpointing = False
 
+        cfg = replace(cfg, **kwargs)
         assert cfg.act_layer in _nonlin_gamma, f"Please add non-linearity constants for activation ({cfg.act_layer})."
         conv_layer = ScaledStdConv2dSame if cfg.same_padding else ScaledStdConv2d
         if cfg.gamma_in_act:
             act_layer = act_with_gamma(cfg.act_layer, gamma=_nonlin_gamma[cfg.act_layer])
             conv_layer = partial(conv_layer, eps=cfg.std_conv_eps)
         else:
             act_layer = get_act_layer(cfg.act_layer)
             conv_layer = partial(conv_layer, gamma=_nonlin_gamma[cfg.act_layer], eps=cfg.std_conv_eps)
         attn_layer = partial(get_attn(cfg.attn_layer), **cfg.attn_kwargs) if cfg.attn_layer else None
 
         stem_chs = make_divisible((cfg.stem_chs or cfg.channels[0]) * cfg.width_factor, cfg.ch_div)
         self.stem, stem_stride, stem_feat = create_stem(
-            in_chans, stem_chs, cfg.stem_type, conv_layer=conv_layer, act_layer=act_layer)
+            in_chans,
+            stem_chs,
+            cfg.stem_type,
+            conv_layer=conv_layer,
+            act_layer=act_layer,
+        )
 
         self.feature_info = [stem_feat]
         drop_path_rates = [x.tolist() for x in torch.linspace(0, drop_path_rate, sum(cfg.depths)).split(cfg.depths)]
         prev_chs = stem_chs
         net_stride = stem_stride
         dilation = 1
         expected_var = 1.0
```

### Comparing `timm-0.8.3.dev0/timm/models/pit.py` & `timm-0.8.6.dev0/timm/models/pit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/pnasnet.py` & `timm-0.8.6.dev0/timm/models/pnasnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/poolformer.py` & `timm-0.8.6.dev0/timm/models/poolformer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/pvt_v2.py` & `timm-0.8.6.dev0/timm/models/pvt_v2.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/regnet.py` & `timm-0.8.6.dev0/timm/models/regnet.py`

 * *Files 4% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 * first layer from BGR -> RGB as most PyTorch models are
 * removed training specific dict entries from checkpoints and keep model state_dict only
 * remap names to match the ones here
 
 Hacked together by / Copyright 2020 Ross Wightman
 """
 import math
-from dataclasses import dataclass
+from dataclasses import dataclass, replace
 from functools import partial
 from typing import Optional, Union, Callable
 
 import numpy as np
 import torch
 import torch.nn as nn
 
@@ -233,15 +233,23 @@
         conv = create_conv2d(in_chs, out_chs, 1, stride=1)
     else:
         conv = ConvNormAct(in_chs, out_chs, 1, stride=1, norm_layer=norm_layer, apply_act=False)
     return nn.Sequential(*[pool, conv])
 
 
 def create_shortcut(
-        downsample_type, in_chs, out_chs, kernel_size, stride, dilation=(1, 1), norm_layer=None, preact=False):
+        downsample_type,
+        in_chs,
+        out_chs,
+        kernel_size,
+        stride,
+        dilation=(1, 1),
+        norm_layer=None,
+        preact=False,
+):
     assert downsample_type in ('avg', 'conv1x1', '', None)
     if in_chs != out_chs or stride != 1 or dilation[0] != dilation[1]:
         dargs = dict(stride=stride, dilation=dilation[0], norm_layer=norm_layer, preact=preact)
         if not downsample_type:
             return None  # no shortcut, no downsample
         elif downsample_type == 'avg':
             return downsample_avg(in_chs, out_chs, **dargs)
@@ -255,17 +263,29 @@
     """ RegNet Bottleneck
 
     This is almost exactly the same as a ResNet Bottlneck. The main difference is the SE block is moved from
     after conv3 to after conv2. Otherwise, it's just redefining the arguments for groups/bottleneck channels.
     """
 
     def __init__(
-            self, in_chs, out_chs, stride=1, dilation=(1, 1), bottle_ratio=1, group_size=1, se_ratio=0.25,
-            downsample='conv1x1', linear_out=False, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d,
-            drop_block=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1,
+            group_size=1,
+            se_ratio=0.25,
+            downsample='conv1x1',
+            linear_out=False,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(Bottleneck, self).__init__()
         act_layer = get_act_layer(act_layer)
         bottleneck_chs = int(round(out_chs * bottle_ratio))
         groups = bottleneck_chs // group_size
 
         cargs = dict(act_layer=act_layer, norm_layer=norm_layer)
         self.conv1 = ConvNormAct(in_chs, bottleneck_chs, kernel_size=1, **cargs)
@@ -303,17 +323,29 @@
     """ RegNet Bottleneck
 
     This is almost exactly the same as a ResNet Bottlneck. The main difference is the SE block is moved from
     after conv3 to after conv2. Otherwise, it's just redefining the arguments for groups/bottleneck channels.
     """
 
     def __init__(
-            self, in_chs, out_chs, stride=1, dilation=(1, 1), bottle_ratio=1, group_size=1, se_ratio=0.25,
-            downsample='conv1x1', linear_out=False, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d,
-            drop_block=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs,
+            stride=1,
+            dilation=(1, 1),
+            bottle_ratio=1,
+            group_size=1,
+            se_ratio=0.25,
+            downsample='conv1x1',
+            linear_out=False,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            drop_block=None,
+            drop_path_rate=0.,
+    ):
         super(PreBottleneck, self).__init__()
         norm_act_layer = get_norm_act_layer(norm_layer, act_layer)
         bottleneck_chs = int(round(out_chs * bottle_ratio))
         groups = bottleneck_chs // group_size
 
         self.norm1 = norm_act_layer(in_chs)
         self.conv1 = create_conv2d(in_chs, bottleneck_chs, kernel_size=1)
@@ -349,30 +381,43 @@
         return x
 
 
 class RegStage(nn.Module):
     """Stage (sequence of blocks w/ the same output shape)."""
 
     def __init__(
-            self, depth, in_chs, out_chs, stride, dilation,
-            drop_path_rates=None, block_fn=Bottleneck, **block_kwargs):
+            self,
+            depth,
+            in_chs,
+            out_chs,
+            stride,
+            dilation,
+            drop_path_rates=None,
+            block_fn=Bottleneck,
+            **block_kwargs,
+    ):
         super(RegStage, self).__init__()
         self.grad_checkpointing = False
 
         first_dilation = 1 if dilation in (1, 2) else 2
         for i in range(depth):
             block_stride = stride if i == 0 else 1
             block_in_chs = in_chs if i == 0 else out_chs
             block_dilation = (first_dilation, dilation)
             dpr = drop_path_rates[i] if drop_path_rates is not None else 0.
             name = "b{}".format(i + 1)
             self.add_module(
                 name, block_fn(
-                    block_in_chs, out_chs, stride=block_stride, dilation=block_dilation,
-                    drop_path_rate=dpr, **block_kwargs)
+                    block_in_chs,
+                    out_chs,
+                    stride=block_stride,
+                    dilation=block_dilation,
+                    drop_path_rate=dpr,
+                    **block_kwargs,
+                )
             )
             first_dilation = dilation
 
     def forward(self, x):
         if self.grad_checkpointing and not torch.jit.is_scripting():
             x = checkpoint_seq(self.children(), x)
         else:
@@ -385,20 +430,43 @@
     """RegNet-X, Y, and Z Models
 
     Paper: https://arxiv.org/abs/2003.13678
     Original Impl: https://github.com/facebookresearch/pycls/blob/master/pycls/models/regnet.py
     """
 
     def __init__(
-            self, cfg: RegNetCfg, in_chans=3, num_classes=1000, output_stride=32, global_pool='avg',
-            drop_rate=0., drop_path_rate=0., zero_init_last=True):
+            self,
+            cfg: RegNetCfg,
+            in_chans=3,
+            num_classes=1000,
+            output_stride=32,
+            global_pool='avg',
+            drop_rate=0.,
+            drop_path_rate=0.,
+            zero_init_last=True,
+            **kwargs,
+    ):
+        """
+
+        Args:
+            cfg (RegNetCfg): Model architecture configuration
+            in_chans (int): Number of input channels (default: 3)
+            num_classes (int): Number of classifier classes (default: 1000)
+            output_stride (int): Output stride of network, one of (8, 16, 32) (default: 32)
+            global_pool (str): Global pooling type (default: 'avg')
+            drop_rate (float): Dropout rate (default: 0.)
+            drop_path_rate (float): Stochastic depth drop-path rate (default: 0.)
+            zero_init_last (bool): Zero-init last weight of residual path
+            kwargs (dict): Extra kwargs overlayed onto cfg
+        """
         super().__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         assert output_stride in (8, 16, 32)
+        cfg = replace(cfg, **kwargs)  # update cfg with extra passed kwargs
 
         # Construct the stem
         stem_width = cfg.stem_width
         na_args = dict(act_layer=cfg.act_layer, norm_layer=cfg.norm_layer)
         if cfg.preact:
             self.stem = create_conv2d(in_chans, stem_width, 3, stride=2)
         else:
@@ -457,16 +525,20 @@
         # Adjust the compatibility of ws and gws
         stage_widths, stage_gs = adjust_widths_groups_comp(stage_widths, stage_br, stage_gs)
         arg_names = ['out_chs', 'stride', 'dilation', 'depth', 'bottle_ratio', 'group_size', 'drop_path_rates']
         per_stage_args = [
             dict(zip(arg_names, params)) for params in
             zip(stage_widths, stage_strides, stage_dilations, stage_depths, stage_br, stage_gs, stage_dpr)]
         common_args = dict(
-            downsample=cfg.downsample, se_ratio=cfg.se_ratio, linear_out=cfg.linear_out,
-            act_layer=cfg.act_layer, norm_layer=cfg.norm_layer)
+            downsample=cfg.downsample,
+            se_ratio=cfg.se_ratio,
+            linear_out=cfg.linear_out,
+            act_layer=cfg.act_layer,
+            norm_layer=cfg.norm_layer,
+        )
         return per_stage_args, common_args
 
     @torch.jit.ignore
     def group_matcher(self, coarse=False):
         return dict(
             stem=r'^stem',
             blocks=r'^s(\d+)' if coarse else r'^s(\d+)\.b(\d+)',
@@ -514,15 +586,14 @@
         if module.bias is not None:
             nn.init.zeros_(module.bias)
     elif zero_init_last and hasattr(module, 'zero_init_last'):
         module.zero_init_last()
 
 
 def _filter_fn(state_dict):
-    """ convert patch embedding weight from manual patchify + linear proj to conv"""
     if 'classy_state_dict' in state_dict:
         import re
         state_dict = state_dict['classy_state_dict']['base_model']['model']
         out = {}
         for k, v in state_dict['trunk'].items():
             k = k.replace('_feature_blocks.conv1.stem.0', 'stem.conv')
             k = k.replace('_feature_blocks.conv1.stem.1', 'stem.bn')
```

### Comparing `timm-0.8.3.dev0/timm/models/res2net.py` & `timm-0.8.6.dev0/timm/models/res2net.py`

 * *Files 10% similar despite different names*

```diff
@@ -47,17 +47,29 @@
 class Bottle2neck(nn.Module):
     """ Res2Net/Res2NeXT Bottleneck
     Adapted from https://github.com/gasvn/Res2Net/blob/master/res2net.py
     """
     expansion = 4
 
     def __init__(
-            self, inplanes, planes, stride=1, downsample=None,
-            cardinality=1, base_width=26, scale=4, dilation=1, first_dilation=None,
-            act_layer=nn.ReLU, norm_layer=None, attn_layer=None, **_):
+            self,
+            inplanes,
+            planes,
+            stride=1,
+            downsample=None,
+            cardinality=1,
+            base_width=26,
+            scale=4,
+            dilation=1,
+            first_dilation=None,
+            act_layer=nn.ReLU,
+            norm_layer=None,
+            attn_layer=None,
+            **_,
+    ):
         super(Bottle2neck, self).__init__()
         self.scale = scale
         self.is_first = stride > 1 or downsample is not None
         self.num_scales = max(1, scale - 1)
         width = int(math.floor(planes * (base_width / 64.0))) * cardinality
         self.width = width
         outplanes = planes * self.expansion
@@ -85,15 +97,16 @@
         self.bn3 = norm_layer(outplanes)
         self.se = attn_layer(outplanes) if attn_layer is not None else None
 
         self.relu = act_layer(inplace=True)
         self.downsample = downsample
 
     def zero_init_last(self):
-        nn.init.zeros_(self.bn3.weight)
+        if getattr(self.bn3, 'weight', None) is not None:
+            nn.init.zeros_(self.bn3.weight)
 
     def forward(self, x):
         shortcut = x
 
         out = self.conv1(x)
         out = self.bn1(out)
         out = self.relu(out)
@@ -139,75 +152,75 @@
 @register_model
 def res2net50_26w_4s(pretrained=False, **kwargs):
     """Constructs a Res2Net-50 26w4s model.
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=26, block_args=dict(scale=4), **kwargs)
-    return _create_res2net('res2net50_26w_4s', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=26, block_args=dict(scale=4))
+    return _create_res2net('res2net50_26w_4s', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def res2net101_26w_4s(pretrained=False, **kwargs):
     """Constructs a Res2Net-101 26w4s model.
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 23, 3], base_width=26, block_args=dict(scale=4), **kwargs)
-    return _create_res2net('res2net101_26w_4s', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 23, 3], base_width=26, block_args=dict(scale=4))
+    return _create_res2net('res2net101_26w_4s', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def res2net50_26w_6s(pretrained=False, **kwargs):
     """Constructs a Res2Net-50 26w6s model.
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=26, block_args=dict(scale=6), **kwargs)
-    return _create_res2net('res2net50_26w_6s', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=26, block_args=dict(scale=6))
+    return _create_res2net('res2net50_26w_6s', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def res2net50_26w_8s(pretrained=False, **kwargs):
     """Constructs a Res2Net-50 26w8s model.
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=26, block_args=dict(scale=8), **kwargs)
-    return _create_res2net('res2net50_26w_8s', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=26, block_args=dict(scale=8))
+    return _create_res2net('res2net50_26w_8s', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def res2net50_48w_2s(pretrained=False, **kwargs):
     """Constructs a Res2Net-50 48w2s model.
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=48, block_args=dict(scale=2), **kwargs)
-    return _create_res2net('res2net50_48w_2s', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=48, block_args=dict(scale=2))
+    return _create_res2net('res2net50_48w_2s', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def res2net50_14w_8s(pretrained=False, **kwargs):
     """Constructs a Res2Net-50 14w8s model.
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=14, block_args=dict(scale=8), **kwargs)
-    return _create_res2net('res2net50_14w_8s', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=14, block_args=dict(scale=8))
+    return _create_res2net('res2net50_14w_8s', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def res2next50(pretrained=False, **kwargs):
     """Construct Res2NeXt-50 4s
     Args:
         pretrained (bool): If True, returns a model pre-trained on ImageNet
     """
     model_args = dict(
-        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=4, cardinality=8, block_args=dict(scale=4), **kwargs)
-    return _create_res2net('res2next50', pretrained, **model_args)
+        block=Bottle2neck, layers=[3, 4, 6, 3], base_width=4, cardinality=8, block_args=dict(scale=4))
+    return _create_res2net('res2next50', pretrained, **dict(model_args, **kwargs))
```

### Comparing `timm-0.8.3.dev0/timm/models/resnest.py` & `timm-0.8.6.dev0/timm/models/resnest.py`

 * *Files 6% similar despite different names*

```diff
@@ -53,18 +53,35 @@
 class ResNestBottleneck(nn.Module):
     """ResNet Bottleneck
     """
     # pylint: disable=unused-argument
     expansion = 4
 
     def __init__(
-            self, inplanes, planes, stride=1, downsample=None,
-            radix=1, cardinality=1, base_width=64, avd=False, avd_first=False, is_first=False,
-            reduce_first=1, dilation=1, first_dilation=None, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d,
-            attn_layer=None, aa_layer=None, drop_block=None, drop_path=None):
+            self,
+            inplanes,
+            planes,
+            stride=1,
+            downsample=None,
+            radix=1,
+            cardinality=1,
+            base_width=64,
+            avd=False,
+            avd_first=False,
+            is_first=False,
+            reduce_first=1,
+            dilation=1,
+            first_dilation=None,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            attn_layer=None,
+            aa_layer=None,
+            drop_block=None,
+            drop_path=None,
+    ):
         super(ResNestBottleneck, self).__init__()
         assert reduce_first == 1  # not supported
         assert attn_layer is None  # not supported
         assert aa_layer is None  # TODO not yet supported
         assert drop_path is None  # TODO not yet supported
 
         group_width = int(planes * (base_width / 64.)) * cardinality
@@ -99,15 +116,16 @@
 
         self.conv3 = nn.Conv2d(group_width, planes * 4, kernel_size=1, bias=False)
         self.bn3 = norm_layer(planes*4)
         self.act3 = act_layer(inplace=True)
         self.downsample = downsample
 
     def zero_init_last(self):
-        nn.init.zeros_(self.bn3.weight)
+        if getattr(self.bn3, 'weight', None) is not None:
+            nn.init.zeros_(self.bn3.weight)
 
     def forward(self, x):
         shortcut = x
 
         out = self.conv1(x)
         out = self.bn1(out)
         out = self.act1(out)
@@ -141,90 +159,90 @@
 @register_model
 def resnest14d(pretrained=False, **kwargs):
     """ ResNeSt-14d model. Weights ported from GluonCV.
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[1, 1, 1, 1],
         stem_type='deep', stem_width=32, avg_down=True, base_width=64, cardinality=1,
-        block_args=dict(radix=2, avd=True, avd_first=False), **kwargs)
-    return _create_resnest('resnest14d', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=2, avd=True, avd_first=False))
+    return _create_resnest('resnest14d', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest26d(pretrained=False, **kwargs):
     """ ResNeSt-26d model. Weights ported from GluonCV.
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[2, 2, 2, 2],
         stem_type='deep', stem_width=32, avg_down=True, base_width=64, cardinality=1,
-        block_args=dict(radix=2, avd=True, avd_first=False), **kwargs)
-    return _create_resnest('resnest26d', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=2, avd=True, avd_first=False))
+    return _create_resnest('resnest26d', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest50d(pretrained=False, **kwargs):
     """ ResNeSt-50d model. Matches paper ResNeSt-50 model, https://arxiv.org/abs/2004.08955
     Since this codebase supports all possible variations, 'd' for deep stem, stem_width 32, avg in downsample.
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[3, 4, 6, 3],
         stem_type='deep', stem_width=32, avg_down=True, base_width=64, cardinality=1,
-        block_args=dict(radix=2, avd=True, avd_first=False), **kwargs)
-    return _create_resnest('resnest50d', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=2, avd=True, avd_first=False))
+    return _create_resnest('resnest50d', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest101e(pretrained=False, **kwargs):
     """ ResNeSt-101e model. Matches paper ResNeSt-101 model, https://arxiv.org/abs/2004.08955
      Since this codebase supports all possible variations, 'e' for deep stem, stem_width 64, avg in downsample.
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[3, 4, 23, 3],
         stem_type='deep', stem_width=64, avg_down=True, base_width=64, cardinality=1,
-        block_args=dict(radix=2, avd=True, avd_first=False), **kwargs)
-    return _create_resnest('resnest101e', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=2, avd=True, avd_first=False))
+    return _create_resnest('resnest101e', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest200e(pretrained=False, **kwargs):
     """ ResNeSt-200e model. Matches paper ResNeSt-200 model, https://arxiv.org/abs/2004.08955
     Since this codebase supports all possible variations, 'e' for deep stem, stem_width 64, avg in downsample.
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[3, 24, 36, 3],
         stem_type='deep', stem_width=64, avg_down=True, base_width=64, cardinality=1,
-        block_args=dict(radix=2, avd=True, avd_first=False), **kwargs)
-    return _create_resnest('resnest200e', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=2, avd=True, avd_first=False))
+    return _create_resnest('resnest200e', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest269e(pretrained=False, **kwargs):
     """ ResNeSt-269e model. Matches paper ResNeSt-269 model, https://arxiv.org/abs/2004.08955
     Since this codebase supports all possible variations, 'e' for deep stem, stem_width 64, avg in downsample.
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[3, 30, 48, 8],
         stem_type='deep', stem_width=64, avg_down=True, base_width=64, cardinality=1,
-        block_args=dict(radix=2, avd=True, avd_first=False), **kwargs)
-    return _create_resnest('resnest269e', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=2, avd=True, avd_first=False))
+    return _create_resnest('resnest269e', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest50d_4s2x40d(pretrained=False, **kwargs):
     """ResNeSt-50 4s2x40d from https://github.com/zhanghang1989/ResNeSt/blob/master/ablation.md
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[3, 4, 6, 3],
         stem_type='deep', stem_width=32, avg_down=True, base_width=40, cardinality=2,
-        block_args=dict(radix=4, avd=True, avd_first=True), **kwargs)
-    return _create_resnest('resnest50d_4s2x40d', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=4, avd=True, avd_first=True))
+    return _create_resnest('resnest50d_4s2x40d', pretrained=pretrained, **dict(model_kwargs, **kwargs))
 
 
 @register_model
 def resnest50d_1s4x24d(pretrained=False, **kwargs):
     """ResNeSt-50 1s4x24d from https://github.com/zhanghang1989/ResNeSt/blob/master/ablation.md
     """
     model_kwargs = dict(
         block=ResNestBottleneck, layers=[3, 4, 6, 3],
         stem_type='deep', stem_width=32, avg_down=True, base_width=24, cardinality=4,
-        block_args=dict(radix=1, avd=True, avd_first=True), **kwargs)
-    return _create_resnest('resnest50d_1s4x24d', pretrained=pretrained, **model_kwargs)
+        block_args=dict(radix=1, avd=True, avd_first=True))
+    return _create_resnest('resnest50d_1s4x24d', pretrained=pretrained, **dict(model_kwargs, **kwargs))
```

### Comparing `timm-0.8.3.dev0/timm/models/resnet.py` & `timm-0.8.6.dev0/timm/models/resnet.py`

 * *Files 5% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 import torch
 import torch.nn as nn
 import torch.nn.functional as F
 
 from timm.data import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD
 from timm.layers import DropBlock2d, DropPath, AvgPool2dSame, BlurPool2d, GroupNorm, create_attn, get_attn, \
-    create_classifier
+    get_act_layer, get_norm_layer, create_classifier
 from ._builder import build_model_with_cfg
 from ._manipulate import checkpoint_seq
 from ._registry import register_model, model_entrypoint
 
 __all__ = ['ResNet', 'BasicBlock', 'Bottleneck']  # model_registry will add each entrypoint fn to this
 
 
@@ -333,17 +333,31 @@
     return aa_layer(stride) if issubclass(aa_layer, nn.AvgPool2d) else aa_layer(channels=channels, stride=stride)
 
 
 class BasicBlock(nn.Module):
     expansion = 1
 
     def __init__(
-            self, inplanes, planes, stride=1, downsample=None, cardinality=1, base_width=64,
-            reduce_first=1, dilation=1, first_dilation=None, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d,
-            attn_layer=None, aa_layer=None, drop_block=None, drop_path=None):
+            self,
+            inplanes,
+            planes,
+            stride=1,
+            downsample=None,
+            cardinality=1,
+            base_width=64,
+            reduce_first=1,
+            dilation=1,
+            first_dilation=None,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            attn_layer=None,
+            aa_layer=None,
+            drop_block=None,
+            drop_path=None,
+    ):
         super(BasicBlock, self).__init__()
 
         assert cardinality == 1, 'BasicBlock only supports cardinality of 1'
         assert base_width == 64, 'BasicBlock does not support changing base width'
         first_planes = planes // reduce_first
         outplanes = planes * self.expansion
         first_dilation = first_dilation or dilation
@@ -366,15 +380,16 @@
         self.act2 = act_layer(inplace=True)
         self.downsample = downsample
         self.stride = stride
         self.dilation = dilation
         self.drop_path = drop_path
 
     def zero_init_last(self):
-        nn.init.zeros_(self.bn2.weight)
+        if getattr(self.bn2, 'weight', None) is not None:
+            nn.init.zeros_(self.bn2.weight)
 
     def forward(self, x):
         shortcut = x
 
         x = self.conv1(x)
         x = self.bn1(x)
         x = self.drop_block(x)
@@ -398,17 +413,31 @@
         return x
 
 
 class Bottleneck(nn.Module):
     expansion = 4
 
     def __init__(
-            self, inplanes, planes, stride=1, downsample=None, cardinality=1, base_width=64,
-            reduce_first=1, dilation=1, first_dilation=None, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d,
-            attn_layer=None, aa_layer=None, drop_block=None, drop_path=None):
+            self,
+            inplanes,
+            planes,
+            stride=1,
+            downsample=None,
+            cardinality=1,
+            base_width=64,
+            reduce_first=1,
+            dilation=1,
+            first_dilation=None,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            attn_layer=None,
+            aa_layer=None,
+            drop_block=None,
+            drop_path=None,
+    ):
         super(Bottleneck, self).__init__()
 
         width = int(math.floor(planes * (base_width / 64)) * cardinality)
         first_planes = width // reduce_first
         outplanes = planes * self.expansion
         first_dilation = first_dilation or dilation
         use_aa = aa_layer is not None and (stride == 2 or first_dilation != dilation)
@@ -433,15 +462,16 @@
         self.act3 = act_layer(inplace=True)
         self.downsample = downsample
         self.stride = stride
         self.dilation = dilation
         self.drop_path = drop_path
 
     def zero_init_last(self):
-        nn.init.zeros_(self.bn3.weight)
+        if getattr(self.bn3, 'weight', None) is not None:
+            nn.init.zeros_(self.bn3.weight)
 
     def forward(self, x):
         shortcut = x
 
         x = self.conv1(x)
         x = self.bn1(x)
         x = self.act1(x)
@@ -466,29 +496,43 @@
         x += shortcut
         x = self.act3(x)
 
         return x
 
 
 def downsample_conv(
-        in_channels, out_channels, kernel_size, stride=1, dilation=1, first_dilation=None, norm_layer=None):
+        in_channels,
+        out_channels,
+        kernel_size,
+        stride=1,
+        dilation=1,
+        first_dilation=None,
+        norm_layer=None,
+):
     norm_layer = norm_layer or nn.BatchNorm2d
     kernel_size = 1 if stride == 1 and dilation == 1 else kernel_size
     first_dilation = (first_dilation or dilation) if kernel_size > 1 else 1
     p = get_padding(kernel_size, stride, first_dilation)
 
     return nn.Sequential(*[
         nn.Conv2d(
             in_channels, out_channels, kernel_size, stride=stride, padding=p, dilation=first_dilation, bias=False),
         norm_layer(out_channels)
     ])
 
 
 def downsample_avg(
-        in_channels, out_channels, kernel_size, stride=1, dilation=1, first_dilation=None, norm_layer=None):
+        in_channels,
+        out_channels,
+        kernel_size,
+        stride=1,
+        dilation=1,
+        first_dilation=None,
+        norm_layer=None,
+):
     norm_layer = norm_layer or nn.BatchNorm2d
     avg_stride = stride if dilation == 1 else 1
     if stride == 1 and dilation == 1:
         pool = nn.Identity()
     else:
         avg_pool_fn = AvgPool2dSame if avg_stride == 1 and dilation > 1 else nn.AvgPool2d
         pool = avg_pool_fn(2, avg_stride, ceil_mode=True, count_include_pad=False)
@@ -504,16 +548,26 @@
     return [
         None, None,
         partial(DropBlock2d, drop_prob=drop_prob, block_size=5, gamma_scale=0.25) if drop_prob else None,
         partial(DropBlock2d, drop_prob=drop_prob, block_size=3, gamma_scale=1.00) if drop_prob else None]
 
 
 def make_blocks(
-        block_fn, channels, block_repeats, inplanes, reduce_first=1, output_stride=32,
-        down_kernel_size=1, avg_down=False, drop_block_rate=0., drop_path_rate=0., **kwargs):
+        block_fn,
+        channels,
+        block_repeats,
+        inplanes,
+        reduce_first=1,
+        output_stride=32,
+        down_kernel_size=1,
+        avg_down=False,
+        drop_block_rate=0.,
+        drop_path_rate=0.,
+        **kwargs,
+):
     stages = []
     feature_info = []
     net_num_blocks = sum(block_repeats)
     net_block_idx = 0
     net_stride = 4
     dilation = prev_dilation = 1
     for stage_idx, (planes, num_blocks, db) in enumerate(zip(channels, block_repeats, drop_blocks(drop_block_rate))):
@@ -524,16 +578,22 @@
             stride = 1
         else:
             net_stride *= stride
 
         downsample = None
         if stride != 1 or inplanes != planes * block_fn.expansion:
             down_kwargs = dict(
-                in_channels=inplanes, out_channels=planes * block_fn.expansion, kernel_size=down_kernel_size,
-                stride=stride, dilation=dilation, first_dilation=prev_dilation, norm_layer=kwargs.get('norm_layer'))
+                in_channels=inplanes,
+                out_channels=planes * block_fn.expansion,
+                kernel_size=down_kernel_size,
+                stride=stride,
+                dilation=dilation,
+                first_dilation=prev_dilation,
+                norm_layer=kwargs.get('norm_layer'),
+            )
             downsample = downsample_avg(**down_kwargs) if avg_down else downsample_conv(**down_kwargs)
 
         block_kwargs = dict(reduce_first=reduce_first, dilation=dilation, drop_block=db, **kwargs)
         blocks = []
         for block_idx in range(num_blocks):
             downsample = downsample if block_idx == 0 else None
             stride = stride if block_idx == 0 else 1
@@ -577,52 +637,80 @@
 
     SE-ResNeXt
       * normal - 7x7 stem, stem_width = 64
       * same c, d, e, s variants as ResNet can be enabled
 
     SENet-154 - 3 layer deep 3x3 stem (same as v1c-v1s), stem_width = 64, cardinality=64,
         reduction by 2 on width of first bottleneck convolution, 3x3 downsample convs after first block
-
-    Parameters
-    ----------
-    block : Block, class for the residual block. Options are BasicBlockGl, BottleneckGl.
-    layers : list of int, number of layers in each block
-    num_classes : int, default 1000, number of classification classes.
-    in_chans : int, default 3, number of input (color) channels.
-    output_stride : int, default 32, output stride of the network, 32, 16, or 8.
-    global_pool : str, Global pooling type. One of 'avg', 'max', 'avgmax', 'catavgmax'
-    cardinality : int, default 1, number of convolution groups for 3x3 conv in Bottleneck.
-    base_width : int, default 64, factor determining bottleneck channels. `planes * base_width / 64 * cardinality`
-    stem_width : int, default 64, number of channels in stem convolutions
-    stem_type : str, default ''
-        The type of stem:
-          * '', default - a single 7x7 conv with a width of stem_width
-          * 'deep' - three 3x3 convolution layers of widths stem_width, stem_width, stem_width * 2
-          * 'deep_tiered' - three 3x3 conv layers of widths stem_width//4 * 3, stem_width, stem_width * 2
-    block_reduce_first : int, default 1
-        Reduction factor for first convolution output width of residual blocks, 1 for all archs except senets, where 2
-    down_kernel_size : int, default 1, kernel size of residual block downsample path, 1x1 for most, 3x3 for senets
-    avg_down : bool, default False, use average pooling for projection skip connection between stages/downsample.
-    act_layer : nn.Module, activation layer
-    norm_layer : nn.Module, normalization layer
-    aa_layer : nn.Module, anti-aliasing layer
-    drop_rate : float, default 0. Dropout probability before classifier, for training
     """
 
     def __init__(
-            self, block, layers, num_classes=1000, in_chans=3, output_stride=32, global_pool='avg',
-            cardinality=1, base_width=64, stem_width=64, stem_type='', replace_stem_pool=False, block_reduce_first=1,
-            down_kernel_size=1, avg_down=False, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d, aa_layer=None,
-            drop_rate=0.0, drop_path_rate=0., drop_block_rate=0., zero_init_last=True, block_args=None):
+            self,
+            block,
+            layers,
+            num_classes=1000,
+            in_chans=3,
+            output_stride=32,
+            global_pool='avg',
+            cardinality=1,
+            base_width=64,
+            stem_width=64,
+            stem_type='',
+            replace_stem_pool=False,
+            block_reduce_first=1,
+            down_kernel_size=1,
+            avg_down=False,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            aa_layer=None,
+            drop_rate=0.0,
+            drop_path_rate=0.,
+            drop_block_rate=0.,
+            zero_init_last=True,
+            block_args=None,
+    ):
+        """
+        Args:
+            block (nn.Module): class for the residual block. Options are BasicBlock, Bottleneck.
+            layers (List[int]) : number of layers in each block
+            num_classes (int): number of classification classes (default 1000)
+            in_chans (int): number of input (color) channels. (default 3)
+            output_stride (int): output stride of the network, 32, 16, or 8. (default 32)
+            global_pool (str): Global pooling type. One of 'avg', 'max', 'avgmax', 'catavgmax' (default 'avg')
+            cardinality (int): number of convolution groups for 3x3 conv in Bottleneck. (default 1)
+            base_width (int): bottleneck channels factor. `planes * base_width / 64 * cardinality` (default 64)
+            stem_width (int): number of channels in stem convolutions (default 64)
+            stem_type (str): The type of stem (default ''):
+                * '', default - a single 7x7 conv with a width of stem_width
+                * 'deep' - three 3x3 convolution layers of widths stem_width, stem_width, stem_width * 2
+                * 'deep_tiered' - three 3x3 conv layers of widths stem_width//4 * 3, stem_width, stem_width * 2
+            replace_stem_pool (bool): replace stem max-pooling layer with a 3x3 stride-2 convolution
+            block_reduce_first (int): Reduction factor for first convolution output width of residual blocks,
+                1 for all archs except senets, where 2 (default 1)
+            down_kernel_size (int): kernel size of residual block downsample path,
+                1x1 for most, 3x3 for senets (default: 1)
+            avg_down (bool): use avg pooling for projection skip connection between stages/downsample (default False)
+            act_layer (str, nn.Module): activation layer
+            norm_layer (str, nn.Module): normalization layer
+            aa_layer (nn.Module): anti-aliasing layer
+            drop_rate (float): Dropout probability before classifier, for training (default 0.)
+            drop_path_rate (float): Stochastic depth drop-path rate (default 0.)
+            drop_block_rate (float): Drop block rate (default 0.)
+            zero_init_last (bool): zero-init the last weight in residual path (usually last BN affine weight)
+            block_args (dict): Extra kwargs to pass through to block module
+        """
         super(ResNet, self).__init__()
         block_args = block_args or dict()
         assert output_stride in (8, 16, 32)
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         self.grad_checkpointing = False
+        
+        act_layer = get_act_layer(act_layer)
+        norm_layer = get_norm_layer(norm_layer)
 
         # Stem
         deep_stem = 'deep' in stem_type
         inplanes = stem_width * 2 if deep_stem else 64
         if deep_stem:
             stem_chs = (stem_width, stem_width)
             if 'tiered' in stem_type:
@@ -659,18 +747,31 @@
                         aa_layer(channels=inplanes, stride=2)])
             else:
                 self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
 
         # Feature Blocks
         channels = [64, 128, 256, 512]
         stage_modules, stage_feature_info = make_blocks(
-            block, channels, layers, inplanes, cardinality=cardinality, base_width=base_width,
-            output_stride=output_stride, reduce_first=block_reduce_first, avg_down=avg_down,
-            down_kernel_size=down_kernel_size, act_layer=act_layer, norm_layer=norm_layer, aa_layer=aa_layer,
-            drop_block_rate=drop_block_rate, drop_path_rate=drop_path_rate, **block_args)
+            block,
+            channels,
+            layers,
+            inplanes,
+            cardinality=cardinality,
+            base_width=base_width,
+            output_stride=output_stride,
+            reduce_first=block_reduce_first,
+            avg_down=avg_down,
+            down_kernel_size=down_kernel_size,
+            act_layer=act_layer,
+            norm_layer=norm_layer,
+            aa_layer=aa_layer,
+            drop_block_rate=drop_block_rate,
+            drop_path_rate=drop_path_rate,
+            **block_args,
+        )
         for stage in stage_modules:
             self.add_module(*stage)  # layer1, layer2, etc
         self.feature_info.extend(stage_feature_info)
 
         # Head (Pooling and Classifier)
         self.num_features = 512 * block.expansion
         self.global_pool, self.fc = create_classifier(self.num_features, self.num_classes, pool_type=global_pool)
@@ -683,17 +784,14 @@
         return entry_fn(pretrained=not load_weights, **kwargs)
 
     @torch.jit.ignore
     def init_weights(self, zero_init_last=True):
         for n, m in self.named_modules():
             if isinstance(m, nn.Conv2d):
                 nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
-            elif isinstance(m, nn.BatchNorm2d):
-                nn.init.ones_(m.weight)
-                nn.init.zeros_(m.bias)
         if zero_init_last:
             for m in self.modules():
                 if hasattr(m, 'zero_init_last'):
                     m.zero_init_last()
 
     @torch.jit.ignore
     def group_matcher(self, coarse=False):
@@ -743,653 +841,644 @@
     return build_model_with_cfg(ResNet, variant, pretrained, **kwargs)
 
 
 @register_model
 def resnet10t(pretrained=False, **kwargs):
     """Constructs a ResNet-10-T model.
     """
-    model_args = dict(
-        block=BasicBlock, layers=[1, 1, 1, 1], stem_width=32, stem_type='deep_tiered', avg_down=True, **kwargs)
-    return _create_resnet('resnet10t', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[1, 1, 1, 1], stem_width=32, stem_type='deep_tiered', avg_down=True)
+    return _create_resnet('resnet10t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet14t(pretrained=False, **kwargs):
     """Constructs a ResNet-14-T model.
     """
-    model_args = dict(
-        block=Bottleneck, layers=[1, 1, 1, 1], stem_width=32, stem_type='deep_tiered', avg_down=True, **kwargs)
-    return _create_resnet('resnet14t', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[1, 1, 1, 1], stem_width=32, stem_type='deep_tiered', avg_down=True)
+    return _create_resnet('resnet14t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet18(pretrained=False, **kwargs):
     """Constructs a ResNet-18 model.
     """
-    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], **kwargs)
-    return _create_resnet('resnet18', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2])
+    return _create_resnet('resnet18', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet18d(pretrained=False, **kwargs):
     """Constructs a ResNet-18-D model.
     """
-    model_args = dict(
-        block=BasicBlock, layers=[2, 2, 2, 2], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet18d', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet18d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet34(pretrained=False, **kwargs):
     """Constructs a ResNet-34 model.
     """
-    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3], **kwargs)
-    return _create_resnet('resnet34', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3])
+    return _create_resnet('resnet34', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet34d(pretrained=False, **kwargs):
     """Constructs a ResNet-34-D model.
     """
-    model_args = dict(
-        block=BasicBlock, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet34d', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet34d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet26(pretrained=False, **kwargs):
     """Constructs a ResNet-26 model.
     """
-    model_args = dict(block=Bottleneck, layers=[2, 2, 2, 2], **kwargs)
-    return _create_resnet('resnet26', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[2, 2, 2, 2])
+    return _create_resnet('resnet26', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet26t(pretrained=False, **kwargs):
     """Constructs a ResNet-26-T model.
     """
-    model_args = dict(
-        block=Bottleneck, layers=[2, 2, 2, 2], stem_width=32, stem_type='deep_tiered', avg_down=True, **kwargs)
-    return _create_resnet('resnet26t', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[2, 2, 2, 2], stem_width=32, stem_type='deep_tiered', avg_down=True)
+    return _create_resnet('resnet26t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet26d(pretrained=False, **kwargs):
     """Constructs a ResNet-26-D model.
     """
-    model_args = dict(block=Bottleneck, layers=[2, 2, 2, 2], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet26d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[2, 2, 2, 2], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet26d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet50(pretrained=False, **kwargs):
     """Constructs a ResNet-50 model.
     """
     model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3],  **kwargs)
-    return _create_resnet('resnet50', pretrained, **model_args)
+    return _create_resnet('resnet50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet50d(pretrained=False, **kwargs) -> ResNet:
     """Constructs a ResNet-50-D model.
     """
-    model_args = dict(
-        block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet50d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet50d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet50t(pretrained=False, **kwargs):
     """Constructs a ResNet-50-T model.
     """
-    model_args = dict(
-        block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep_tiered', avg_down=True, **kwargs)
-    return _create_resnet('resnet50t', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep_tiered', avg_down=True)
+    return _create_resnet('resnet50t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet101(pretrained=False, **kwargs):
     """Constructs a ResNet-101 model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], **kwargs)
-    return _create_resnet('resnet101', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3])
+    return _create_resnet('resnet101', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet101d(pretrained=False, **kwargs):
     """Constructs a ResNet-101-D model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet101d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet101d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet152(pretrained=False, **kwargs):
     """Constructs a ResNet-152 model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3], **kwargs)
-    return _create_resnet('resnet152', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3])
+    return _create_resnet('resnet152', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet152d(pretrained=False, **kwargs):
     """Constructs a ResNet-152-D model.
     """
-    model_args = dict(
-        block=Bottleneck, layers=[3, 8, 36, 3], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet152d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet152d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet200(pretrained=False, **kwargs):
     """Constructs a ResNet-200 model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 24, 36, 3], **kwargs)
-    return _create_resnet('resnet200', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 24, 36, 3])
+    return _create_resnet('resnet200', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet200d(pretrained=False, **kwargs):
     """Constructs a ResNet-200-D model.
     """
-    model_args = dict(
-        block=Bottleneck, layers=[3, 24, 36, 3], stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnet200d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 24, 36, 3], stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnet200d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def tv_resnet34(pretrained=False, **kwargs):
     """Constructs a ResNet-34 model with original Torchvision weights.
     """
-    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3], **kwargs)
-    return _create_resnet('tv_resnet34', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3])
+    return _create_resnet('tv_resnet34', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def tv_resnet50(pretrained=False, **kwargs):
     """Constructs a ResNet-50 model with original Torchvision weights.
     """
     model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3],  **kwargs)
-    return _create_resnet('tv_resnet50', pretrained, **model_args)
+    return _create_resnet('tv_resnet50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def tv_resnet101(pretrained=False, **kwargs):
     """Constructs a ResNet-101 model w/ Torchvision pretrained weights.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], **kwargs)
-    return _create_resnet('tv_resnet101', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3])
+    return _create_resnet('tv_resnet101', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def tv_resnet152(pretrained=False, **kwargs):
     """Constructs a ResNet-152 model w/ Torchvision pretrained weights.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3], **kwargs)
-    return _create_resnet('tv_resnet152', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3])
+    return _create_resnet('tv_resnet152', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def wide_resnet50_2(pretrained=False, **kwargs):
     """Constructs a Wide ResNet-50-2 model.
     The model is the same as ResNet except for the bottleneck number of channels
     which is twice larger in every block. The number of channels in outer 1x1
     convolutions is the same, e.g. last block in ResNet-50 has 2048-512-2048
     channels, and in Wide ResNet-50-2 has 2048-1024-2048.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], base_width=128, **kwargs)
-    return _create_resnet('wide_resnet50_2', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], base_width=128)
+    return _create_resnet('wide_resnet50_2', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def wide_resnet101_2(pretrained=False, **kwargs):
     """Constructs a Wide ResNet-101-2 model.
     The model is the same as ResNet except for the bottleneck number of channels
     which is twice larger in every block. The number of channels in outer 1x1
     convolutions is the same.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], base_width=128, **kwargs)
-    return _create_resnet('wide_resnet101_2', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], base_width=128)
+    return _create_resnet('wide_resnet101_2', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnet50_gn(pretrained=False, **kwargs):
     """Constructs a ResNet-50 model w/ GroupNorm
     """
     model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3],  **kwargs)
     return _create_resnet('resnet50_gn', pretrained, norm_layer=GroupNorm, **model_args)
 
 
 @register_model
 def resnext50_32x4d(pretrained=False, **kwargs):
     """Constructs a ResNeXt50-32x4d model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('resnext50_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4)
+    return _create_resnet('resnext50_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnext50d_32x4d(pretrained=False, **kwargs):
     """Constructs a ResNeXt50d-32x4d model. ResNext50 w/ deep stem & avg pool downsample
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3],  cardinality=32, base_width=4,
-        stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnext50d_32x4d', pretrained, **model_args)
+        stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnext50d_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnext101_32x4d(pretrained=False, **kwargs):
     """Constructs a ResNeXt-101 32x4d model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('resnext101_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4)
+    return _create_resnet('resnext101_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnext101_32x8d(pretrained=False, **kwargs):
     """Constructs a ResNeXt-101 32x8d model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8, **kwargs)
-    return _create_resnet('resnext101_32x8d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8)
+    return _create_resnet('resnext101_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnext101_64x4d(pretrained=False, **kwargs):
     """Constructs a ResNeXt101-64x4d model.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=64, base_width=4, **kwargs)
-    return _create_resnet('resnext101_64x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=64, base_width=4)
+    return _create_resnet('resnext101_64x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def tv_resnext50_32x4d(pretrained=False, **kwargs):
     """Constructs a ResNeXt50-32x4d model with original Torchvision weights.
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('tv_resnext50_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4)
+    return _create_resnet('tv_resnext50_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ig_resnext101_32x8d(pretrained=False, **kwargs):
     """Constructs a ResNeXt-101 32x8 model pre-trained on weakly-supervised data
     and finetuned on ImageNet from Figure 5 in
     `"Exploring the Limits of Weakly Supervised Pretraining" <https://arxiv.org/abs/1805.00932>`_
     Weights from https://pytorch.org/hub/facebookresearch_WSL-Images_resnext/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8, **kwargs)
-    return _create_resnet('ig_resnext101_32x8d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8)
+    return _create_resnet('ig_resnext101_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ig_resnext101_32x16d(pretrained=False, **kwargs):
     """Constructs a ResNeXt-101 32x16 model pre-trained on weakly-supervised data
     and finetuned on ImageNet from Figure 5 in
     `"Exploring the Limits of Weakly Supervised Pretraining" <https://arxiv.org/abs/1805.00932>`_
     Weights from https://pytorch.org/hub/facebookresearch_WSL-Images_resnext/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=16, **kwargs)
-    return _create_resnet('ig_resnext101_32x16d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=16)
+    return _create_resnet('ig_resnext101_32x16d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ig_resnext101_32x32d(pretrained=False, **kwargs):
     """Constructs a ResNeXt-101 32x32 model pre-trained on weakly-supervised data
     and finetuned on ImageNet from Figure 5 in
     `"Exploring the Limits of Weakly Supervised Pretraining" <https://arxiv.org/abs/1805.00932>`_
     Weights from https://pytorch.org/hub/facebookresearch_WSL-Images_resnext/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=32, **kwargs)
-    return _create_resnet('ig_resnext101_32x32d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=32)
+    return _create_resnet('ig_resnext101_32x32d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ig_resnext101_32x48d(pretrained=False, **kwargs):
     """Constructs a ResNeXt-101 32x48 model pre-trained on weakly-supervised data
     and finetuned on ImageNet from Figure 5 in
     `"Exploring the Limits of Weakly Supervised Pretraining" <https://arxiv.org/abs/1805.00932>`_
     Weights from https://pytorch.org/hub/facebookresearch_WSL-Images_resnext/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=48, **kwargs)
-    return _create_resnet('ig_resnext101_32x48d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=48)
+    return _create_resnet('ig_resnext101_32x48d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ssl_resnet18(pretrained=False, **kwargs):
     """Constructs a semi-supervised ResNet-18 model pre-trained on YFCC100M dataset and finetuned on ImageNet
     `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
     Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], **kwargs)
-    return _create_resnet('ssl_resnet18', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2])
+    return _create_resnet('ssl_resnet18', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ssl_resnet50(pretrained=False, **kwargs):
     """Constructs a semi-supervised ResNet-50 model pre-trained on YFCC100M dataset and finetuned on ImageNet
     `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
     Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
     model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3],  **kwargs)
-    return _create_resnet('ssl_resnet50', pretrained, **model_args)
+    return _create_resnet('ssl_resnet50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ssl_resnext50_32x4d(pretrained=False, **kwargs):
     """Constructs a semi-supervised ResNeXt-50 32x4 model pre-trained on YFCC100M dataset and finetuned on ImageNet
     `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
     Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('ssl_resnext50_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4)
+    return _create_resnet('ssl_resnext50_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ssl_resnext101_32x4d(pretrained=False, **kwargs):
     """Constructs a semi-supervised ResNeXt-101 32x4 model pre-trained on YFCC100M dataset and finetuned on ImageNet
     `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
     Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('ssl_resnext101_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4)
+    return _create_resnet('ssl_resnext101_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ssl_resnext101_32x8d(pretrained=False, **kwargs):
     """Constructs a semi-supervised ResNeXt-101 32x8 model pre-trained on YFCC100M dataset and finetuned on ImageNet
     `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
     Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8, **kwargs)
-    return _create_resnet('ssl_resnext101_32x8d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8)
+    return _create_resnet('ssl_resnext101_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ssl_resnext101_32x16d(pretrained=False, **kwargs):
     """Constructs a semi-supervised ResNeXt-101 32x16 model pre-trained on YFCC100M dataset and finetuned on ImageNet
     `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
     Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=16, **kwargs)
-    return _create_resnet('ssl_resnext101_32x16d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=16)
+    return _create_resnet('ssl_resnext101_32x16d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def swsl_resnet18(pretrained=False, **kwargs):
     """Constructs a semi-weakly supervised Resnet-18 model pre-trained on 1B weakly supervised
        image dataset and finetuned on ImageNet.
        `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
        Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], **kwargs)
-    return _create_resnet('swsl_resnet18', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2])
+    return _create_resnet('swsl_resnet18', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def swsl_resnet50(pretrained=False, **kwargs):
     """Constructs a semi-weakly supervised ResNet-50 model pre-trained on 1B weakly supervised
        image dataset and finetuned on ImageNet.
        `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
        Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
     model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3],  **kwargs)
-    return _create_resnet('swsl_resnet50', pretrained, **model_args)
+    return _create_resnet('swsl_resnet50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def swsl_resnext50_32x4d(pretrained=False, **kwargs):
     """Constructs a semi-weakly supervised ResNeXt-50 32x4 model pre-trained on 1B weakly supervised
        image dataset and finetuned on ImageNet.
        `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
        Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('swsl_resnext50_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4)
+    return _create_resnet('swsl_resnext50_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def swsl_resnext101_32x4d(pretrained=False, **kwargs):
     """Constructs a semi-weakly supervised ResNeXt-101 32x4 model pre-trained on 1B weakly supervised
        image dataset and finetuned on ImageNet.
        `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
        Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4, **kwargs)
-    return _create_resnet('swsl_resnext101_32x4d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4)
+    return _create_resnet('swsl_resnext101_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def swsl_resnext101_32x8d(pretrained=False, **kwargs):
     """Constructs a semi-weakly supervised ResNeXt-101 32x8 model pre-trained on 1B weakly supervised
        image dataset and finetuned on ImageNet.
        `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
        Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8, **kwargs)
-    return _create_resnet('swsl_resnext101_32x8d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8)
+    return _create_resnet('swsl_resnext101_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def swsl_resnext101_32x16d(pretrained=False, **kwargs):
     """Constructs a semi-weakly supervised ResNeXt-101 32x16 model pre-trained on 1B weakly supervised
        image dataset and finetuned on ImageNet.
        `"Billion-scale Semi-Supervised Learning for Image Classification" <https://arxiv.org/abs/1905.00546>`_
        Weights from https://github.com/facebookresearch/semi-supervised-ImageNet1K-models/
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=16, **kwargs)
-    return _create_resnet('swsl_resnext101_32x16d', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=16)
+    return _create_resnet('swsl_resnext101_32x16d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet26t(pretrained=False, **kwargs):
     """Constructs an ECA-ResNeXt-26-T model.
     This is technically a 28 layer ResNet, like a 'D' bag-of-tricks model but with tiered 24, 32, 64 channels
     in the deep stem and ECA attn.
     """
     model_args = dict(
         block=Bottleneck, layers=[2, 2, 2, 2], stem_width=32,
-        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet26t', pretrained, **model_args)
+        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet26t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet50d(pretrained=False, **kwargs):
     """Constructs a ResNet-50-D model with eca.
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet50d', pretrained, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet50d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet50d_pruned(pretrained=False, **kwargs):
     """Constructs a ResNet-50-D model pruned with eca.
         The pruning has been obtained using https://arxiv.org/pdf/2002.08258.pdf
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet50d_pruned', pretrained, pruned=True, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet50d_pruned', pretrained, pruned=True, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet50t(pretrained=False, **kwargs):
     """Constructs an ECA-ResNet-50-T model.
     Like a 'D' bag-of-tricks model but with tiered 24, 32, 64 channels in the deep stem and ECA attn.
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32,
-        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet50t', pretrained, **model_args)
+        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet50t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnetlight(pretrained=False, **kwargs):
     """Constructs a ResNet-50-D light model with eca.
     """
     model_args = dict(
         block=Bottleneck, layers=[1, 1, 11, 3], stem_width=32, avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnetlight', pretrained, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnetlight', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet101d(pretrained=False, **kwargs):
     """Constructs a ResNet-101-D model with eca.
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet101d', pretrained, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet101d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet101d_pruned(pretrained=False, **kwargs):
     """Constructs a ResNet-101-D model pruned with eca.
        The pruning has been obtained using https://arxiv.org/pdf/2002.08258.pdf
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet101d_pruned', pretrained, pruned=True, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet101d_pruned', pretrained, pruned=True, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet200d(pretrained=False, **kwargs):
     """Constructs a ResNet-200-D model with ECA.
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 24, 36, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet200d', pretrained, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet200d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnet269d(pretrained=False, **kwargs):
     """Constructs a ResNet-269-D model with ECA.
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 30, 48, 8], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnet269d', pretrained, **model_args)
+        block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnet269d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnext26t_32x4d(pretrained=False, **kwargs):
     """Constructs an ECA-ResNeXt-26-T model.
     This is technically a 28 layer ResNet, like a 'D' bag-of-tricks model but with tiered 24, 32, 64 channels
     in the deep stem. This model replaces SE module with the ECA module
     """
     model_args = dict(
         block=Bottleneck, layers=[2, 2, 2, 2], cardinality=32, base_width=4, stem_width=32,
-        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnext26t_32x4d', pretrained, **model_args)
+        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnext26t_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def ecaresnext50t_32x4d(pretrained=False, **kwargs):
     """Constructs an ECA-ResNeXt-50-T model.
     This is technically a 28 layer ResNet, like a 'D' bag-of-tricks model but with tiered 24, 32, 64 channels
     in the deep stem. This model replaces SE module with the ECA module
     """
     model_args = dict(
         block=Bottleneck, layers=[2, 2, 2, 2], cardinality=32, base_width=4, stem_width=32,
-        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'), **kwargs)
-    return _create_resnet('ecaresnext50t_32x4d', pretrained, **model_args)
+        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='eca'))
+    return _create_resnet('ecaresnext50t_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet18(pretrained=False, **kwargs):
-    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet18', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet18', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet34(pretrained=False, **kwargs):
-    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3], block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet34', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[3, 4, 6, 3], block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet34', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet50(pretrained=False, **kwargs):
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet50', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet50t(pretrained=False, **kwargs):
     model_args = dict(
-        block=Bottleneck, layers=[3, 4, 6, 3],  stem_width=32, stem_type='deep_tiered', avg_down=True,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet50t', pretrained, **model_args)
+        block=Bottleneck, layers=[3, 4, 6, 3],  stem_width=32, stem_type='deep_tiered',
+        avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet50t', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet101(pretrained=False, **kwargs):
-    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet101', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 23, 3], block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet101', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet152(pretrained=False, **kwargs):
-    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3], block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet152', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 8, 36, 3], block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet152', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet152d(pretrained=False, **kwargs):
     model_args = dict(
-        block=Bottleneck, layers=[3, 8, 36, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet152d', pretrained, **model_args)
+        block=Bottleneck, layers=[3, 8, 36, 3], stem_width=32, stem_type='deep',
+        avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet152d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet200d(pretrained=False, **kwargs):
     """Constructs a ResNet-200-D model with SE attn.
     """
     model_args = dict(
-        block=Bottleneck, layers=[3, 24, 36, 3], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet200d', pretrained, **model_args)
+        block=Bottleneck, layers=[3, 24, 36, 3], stem_width=32, stem_type='deep',
+        avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet200d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnet269d(pretrained=False, **kwargs):
     """Constructs a ResNet-269-D model with SE attn.
     """
     model_args = dict(
-        block=Bottleneck, layers=[3, 30, 48, 8], stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnet269d', pretrained, **model_args)
+        block=Bottleneck, layers=[3, 30, 48, 8], stem_width=32, stem_type='deep',
+        avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnet269d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnext26d_32x4d(pretrained=False, **kwargs):
     """Constructs a SE-ResNeXt-26-D model.`
     This is technically a 28 layer ResNet, using the 'D' modifier from Gluon / bag-of-tricks for
     combination of deep stem and avg_pool in downsample.
     """
     model_args = dict(
         block=Bottleneck, layers=[2, 2, 2, 2], cardinality=32, base_width=4, stem_width=32,
-        stem_type='deep', avg_down=True, block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnext26d_32x4d', pretrained, **model_args)
+        stem_type='deep', avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnext26d_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnext26t_32x4d(pretrained=False, **kwargs):
     """Constructs a SE-ResNet-26-T model.
     This is technically a 28 layer ResNet, like a 'D' bag-of-tricks model but with tiered 24, 32, 64 channels
     in the deep stem.
     """
     model_args = dict(
         block=Bottleneck, layers=[2, 2, 2, 2], cardinality=32, base_width=4, stem_width=32,
-        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnext26t_32x4d', pretrained, **model_args)
+        stem_type='deep_tiered', avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnext26t_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnext26tn_32x4d(pretrained=False, **kwargs):
     """Constructs a SE-ResNeXt-26-T model.
     NOTE I deprecated previous 't' model defs and replaced 't' with 'tn', this was the only tn model of note
     so keeping this def for backwards compat with any uses out there. Old 't' model is lost.
@@ -1397,219 +1486,228 @@
     return seresnext26t_32x4d(pretrained=pretrained, **kwargs)
 
 
 @register_model
 def seresnext50_32x4d(pretrained=False, **kwargs):
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], cardinality=32, base_width=4,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnext50_32x4d', pretrained, **model_args)
+        block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnext50_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnext101_32x4d(pretrained=False, **kwargs):
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=4,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnext101_32x4d', pretrained, **model_args)
+        block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnext101_32x4d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnext101_32x8d(pretrained=False, **kwargs):
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnext101_32x8d', pretrained, **model_args)
+        block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnext101_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnext101d_32x8d(pretrained=False, **kwargs):
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8,
         stem_width=32, stem_type='deep', avg_down=True,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnext101d_32x8d', pretrained, **model_args)
+        block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnext101d_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def senet154(pretrained=False, **kwargs):
     model_args = dict(
         block=Bottleneck, layers=[3, 8, 36, 3], cardinality=64, base_width=4, stem_type='deep',
-        down_kernel_size=3, block_reduce_first=2, block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('senet154', pretrained, **model_args)
+        down_kernel_size=3, block_reduce_first=2, block_args=dict(attn_layer='se'))
+    return _create_resnet('senet154', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetblur18(pretrained=False, **kwargs):
     """Constructs a ResNet-18 model with blur anti-aliasing
     """
-    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], aa_layer=BlurPool2d, **kwargs)
-    return _create_resnet('resnetblur18', pretrained, **model_args)
+    model_args = dict(block=BasicBlock, layers=[2, 2, 2, 2], aa_layer=BlurPool2d)
+    return _create_resnet('resnetblur18', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetblur50(pretrained=False, **kwargs):
     """Constructs a ResNet-50 model with blur anti-aliasing
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=BlurPool2d, **kwargs)
-    return _create_resnet('resnetblur50', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=BlurPool2d)
+    return _create_resnet('resnetblur50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetblur50d(pretrained=False, **kwargs):
     """Constructs a ResNet-50-D model with blur anti-aliasing
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=BlurPool2d,
-        stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnetblur50d', pretrained, **model_args)
+        stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnetblur50d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetblur101d(pretrained=False, **kwargs):
     """Constructs a ResNet-101-D model with blur anti-aliasing
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], aa_layer=BlurPool2d,
-        stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnetblur101d', pretrained, **model_args)
+        stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnetblur101d', pretrained, **dict(model_args, **kwargs))
+
+
+@register_model
+def resnetaa34d(pretrained=False, **kwargs):
+    """Constructs a ResNet-34-D model w/ avgpool anti-aliasing
+    """
+    model_args = dict(
+        block=BasicBlock, layers=[3, 4, 6, 3],  aa_layer=nn.AvgPool2d, stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnetaa34d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetaa50(pretrained=False, **kwargs):
     """Constructs a ResNet-50 model with avgpool anti-aliasing
     """
-    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=nn.AvgPool2d, **kwargs)
-    return _create_resnet('resnetaa50', pretrained, **model_args)
+    model_args = dict(block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=nn.AvgPool2d)
+    return _create_resnet('resnetaa50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetaa50d(pretrained=False, **kwargs):
     """Constructs a ResNet-50-D model with avgpool anti-aliasing
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=nn.AvgPool2d,
-        stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnetaa50d', pretrained, **model_args)
+        stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnetaa50d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetaa101d(pretrained=False, **kwargs):
     """Constructs a ResNet-101-D model with avgpool anti-aliasing
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], aa_layer=nn.AvgPool2d,
-        stem_width=32, stem_type='deep', avg_down=True, **kwargs)
-    return _create_resnet('resnetaa101d', pretrained, **model_args)
+        stem_width=32, stem_type='deep', avg_down=True)
+    return _create_resnet('resnetaa101d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnetaa50d(pretrained=False, **kwargs):
     """Constructs a SE=ResNet-50-D model with avgpool anti-aliasing
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], aa_layer=nn.AvgPool2d,
-        stem_width=32, stem_type='deep', avg_down=True, block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnetaa50d', pretrained, **model_args)
+        stem_width=32, stem_type='deep', avg_down=True, block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnetaa50d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def seresnextaa101d_32x8d(pretrained=False, **kwargs):
     """Constructs a SE=ResNeXt-101-D 32x8d model with avgpool anti-aliasing
     """
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], cardinality=32, base_width=8,
         stem_width=32, stem_type='deep', avg_down=True, aa_layer=nn.AvgPool2d,
-        block_args=dict(attn_layer='se'), **kwargs)
-    return _create_resnet('seresnextaa101d_32x8d', pretrained, **model_args)
+        block_args=dict(attn_layer='se'))
+    return _create_resnet('seresnextaa101d_32x8d', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetrs50(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-50 model.
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 6, 3], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs50', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs50', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetrs101(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-101 model.
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[3, 4, 23, 3], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs101', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs101', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetrs152(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-152 model.
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[3, 8, 36, 3], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs152', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs152', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetrs200(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-200 model.
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[3, 24, 36, 3], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs200', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs200', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetrs270(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-270 model.
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[4, 29, 53, 4], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs270', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs270', pretrained, **dict(model_args, **kwargs))
 
 
 
 @register_model
 def resnetrs350(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-350 model.
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[4, 36, 72, 4], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs350', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs350', pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetrs420(pretrained=False, **kwargs):
     """Constructs a ResNet-RS-420 model
     Paper: Revisiting ResNets - https://arxiv.org/abs/2103.07579
     Pretrained weights from https://github.com/tensorflow/tpu/tree/bee9c4f6/models/official/resnet/resnet_rs
     """
     attn_layer = partial(get_attn('se'), rd_ratio=0.25)
     model_args = dict(
         block=Bottleneck, layers=[4, 44, 87, 4], stem_width=32, stem_type='deep', replace_stem_pool=True,
-        avg_down=True,  block_args=dict(attn_layer=attn_layer), **kwargs)
-    return _create_resnet('resnetrs420', pretrained, **model_args)
+        avg_down=True,  block_args=dict(attn_layer=attn_layer))
+    return _create_resnet('resnetrs420', pretrained, **dict(model_args, **kwargs))
```

### Comparing `timm-0.8.3.dev0/timm/models/resnetv2.py` & `timm-0.8.6.dev0/timm/models/resnetv2.py`

 * *Files 6% similar despite different names*

```diff
@@ -33,15 +33,15 @@
 from functools import partial
 
 import torch
 import torch.nn as nn
 
 from timm.data import IMAGENET_INCEPTION_MEAN, IMAGENET_INCEPTION_STD
 from timm.layers import GroupNormAct, BatchNormAct2d, EvoNorm2dB0, EvoNorm2dS0, FilterResponseNormTlu2d, \
-    ClassifierHead, DropPath, AvgPool2dSame, create_pool2d, StdConv2d, create_conv2d
+    ClassifierHead, DropPath, AvgPool2dSame, create_pool2d, StdConv2d, create_conv2d, get_act_layer, get_norm_act_layer
 from ._builder import build_model_with_cfg
 from ._manipulate import checkpoint_seq, named_apply, adapt_input_conv
 from ._registry import register_model
 
 __all__ = ['ResNetV2']  # model_registry will add each entrypoint fn to this
 
 
@@ -151,16 +151,28 @@
     Follows the implementation of "Identity Mappings in Deep Residual Networks":
     https://github.com/KaimingHe/resnet-1k-layers/blob/master/resnet-pre-act.lua
 
     Except it puts the stride on 3x3 conv when available.
     """
 
     def __init__(
-            self, in_chs, out_chs=None, bottle_ratio=0.25, stride=1, dilation=1, first_dilation=None, groups=1,
-            act_layer=None, conv_layer=None, norm_layer=None, proj_layer=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs=None,
+            bottle_ratio=0.25,
+            stride=1,
+            dilation=1,
+            first_dilation=None,
+            groups=1,
+            act_layer=None,
+            conv_layer=None,
+            norm_layer=None,
+            proj_layer=None,
+            drop_path_rate=0.,
+    ):
         super().__init__()
         first_dilation = first_dilation or dilation
         conv_layer = conv_layer or StdConv2d
         norm_layer = norm_layer or partial(GroupNormAct, num_groups=32)
         out_chs = out_chs or in_chs
         mid_chs = make_div(out_chs * bottle_ratio)
 
@@ -198,16 +210,28 @@
         return x + shortcut
 
 
 class Bottleneck(nn.Module):
     """Non Pre-activation bottleneck block, equiv to V1.5/V1b Bottleneck. Used for ViT.
     """
     def __init__(
-            self, in_chs, out_chs=None, bottle_ratio=0.25, stride=1, dilation=1, first_dilation=None, groups=1,
-            act_layer=None, conv_layer=None, norm_layer=None, proj_layer=None, drop_path_rate=0.):
+            self,
+            in_chs,
+            out_chs=None,
+            bottle_ratio=0.25,
+            stride=1,
+            dilation=1,
+            first_dilation=None,
+            groups=1,
+            act_layer=None,
+            conv_layer=None,
+            norm_layer=None,
+            proj_layer=None,
+            drop_path_rate=0.,
+    ):
         super().__init__()
         first_dilation = first_dilation or dilation
         act_layer = act_layer or nn.ReLU
         conv_layer = conv_layer or StdConv2d
         norm_layer = norm_layer or partial(GroupNormAct, num_groups=32)
         out_chs = out_chs or in_chs
         mid_chs = make_div(out_chs * bottle_ratio)
@@ -225,15 +249,16 @@
         self.norm2 = norm_layer(mid_chs)
         self.conv3 = conv_layer(mid_chs, out_chs, 1)
         self.norm3 = norm_layer(out_chs, apply_act=False)
         self.drop_path = DropPath(drop_path_rate) if drop_path_rate > 0 else nn.Identity()
         self.act3 = act_layer(inplace=True)
 
     def zero_init_last(self):
-        nn.init.zeros_(self.norm3.weight)
+        if getattr(self.norm3, 'weight', None) is not None:
+            nn.init.zeros_(self.norm3.weight)
 
     def forward(self, x):
         # shortcut branch
         shortcut = x
         if self.downsample is not None:
             shortcut = self.downsample(x)
 
@@ -247,28 +272,44 @@
         x = self.drop_path(x)
         x = self.act3(x + shortcut)
         return x
 
 
 class DownsampleConv(nn.Module):
     def __init__(
-            self, in_chs, out_chs, stride=1, dilation=1, first_dilation=None, preact=True,
-            conv_layer=None, norm_layer=None):
+            self,
+            in_chs,
+            out_chs,
+            stride=1,
+            dilation=1,
+            first_dilation=None,
+            preact=True,
+            conv_layer=None,
+            norm_layer=None,
+    ):
         super(DownsampleConv, self).__init__()
         self.conv = conv_layer(in_chs, out_chs, 1, stride=stride)
         self.norm = nn.Identity() if preact else norm_layer(out_chs, apply_act=False)
 
     def forward(self, x):
         return self.norm(self.conv(x))
 
 
 class DownsampleAvg(nn.Module):
     def __init__(
-            self, in_chs, out_chs, stride=1, dilation=1, first_dilation=None,
-            preact=True, conv_layer=None, norm_layer=None):
+            self,
+            in_chs,
+            out_chs,
+            stride=1,
+            dilation=1,
+            first_dilation=None,
+            preact=True,
+            conv_layer=None,
+            norm_layer=None,
+    ):
         """ AvgPool Downsampling as in 'D' ResNet variants. This is not in RegNet space but I might experiment."""
         super(DownsampleAvg, self).__init__()
         avg_stride = stride if dilation == 1 else 1
         if stride > 1 or dilation > 1:
             avg_pool_fn = AvgPool2dSame if avg_stride == 1 and dilation > 1 else nn.AvgPool2d
             self.pool = avg_pool_fn(2, avg_stride, ceil_mode=True, count_include_pad=False)
         else:
@@ -279,46 +320,73 @@
     def forward(self, x):
         return self.norm(self.conv(self.pool(x)))
 
 
 class ResNetStage(nn.Module):
     """ResNet Stage."""
     def __init__(
-            self, in_chs, out_chs, stride, dilation, depth, bottle_ratio=0.25, groups=1,
-            avg_down=False, block_dpr=None, block_fn=PreActBottleneck,
-            act_layer=None, conv_layer=None, norm_layer=None, **block_kwargs):
+            self,
+            in_chs,
+            out_chs,
+            stride,
+            dilation,
+            depth,
+            bottle_ratio=0.25,
+            groups=1,
+            avg_down=False,
+            block_dpr=None,
+            block_fn=PreActBottleneck,
+            act_layer=None,
+            conv_layer=None,
+            norm_layer=None,
+            **block_kwargs,
+    ):
         super(ResNetStage, self).__init__()
         first_dilation = 1 if dilation in (1, 2) else 2
         layer_kwargs = dict(act_layer=act_layer, conv_layer=conv_layer, norm_layer=norm_layer)
         proj_layer = DownsampleAvg if avg_down else DownsampleConv
         prev_chs = in_chs
         self.blocks = nn.Sequential()
         for block_idx in range(depth):
             drop_path_rate = block_dpr[block_idx] if block_dpr else 0.
             stride = stride if block_idx == 0 else 1
             self.blocks.add_module(str(block_idx), block_fn(
-                prev_chs, out_chs, stride=stride, dilation=dilation, bottle_ratio=bottle_ratio, groups=groups,
-                first_dilation=first_dilation, proj_layer=proj_layer, drop_path_rate=drop_path_rate,
-                **layer_kwargs, **block_kwargs))
+                prev_chs,
+                out_chs,
+                stride=stride,
+                dilation=dilation,
+                bottle_ratio=bottle_ratio,
+                groups=groups,
+                first_dilation=first_dilation,
+                proj_layer=proj_layer,
+                drop_path_rate=drop_path_rate,
+                **layer_kwargs,
+                **block_kwargs,
+            ))
             prev_chs = out_chs
             first_dilation = dilation
             proj_layer = None
 
     def forward(self, x):
         x = self.blocks(x)
         return x
 
 
 def is_stem_deep(stem_type):
     return any([s in stem_type for s in ('deep', 'tiered')])
 
 
 def create_resnetv2_stem(
-        in_chs, out_chs=64, stem_type='', preact=True,
-        conv_layer=StdConv2d, norm_layer=partial(GroupNormAct, num_groups=32)):
+        in_chs,
+        out_chs=64,
+        stem_type='',
+        preact=True,
+        conv_layer=StdConv2d,
+        norm_layer=partial(GroupNormAct, num_groups=32),
+):
     stem = OrderedDict()
     assert stem_type in ('', 'fixed', 'same', 'deep', 'deep_fixed', 'deep_same', 'tiered')
 
     # NOTE conv padding mode can be changed by overriding the conv_layer def
     if is_stem_deep(stem_type):
         # A 3 deep 3x3  conv stack as in ResNet V1D models
         if 'tiered' in stem_type:
@@ -353,28 +421,70 @@
 
 
 class ResNetV2(nn.Module):
     """Implementation of Pre-activation (v2) ResNet mode.
     """
 
     def __init__(
-            self, layers, channels=(256, 512, 1024, 2048),
-            num_classes=1000, in_chans=3, global_pool='avg', output_stride=32,
-            width_factor=1, stem_chs=64, stem_type='', avg_down=False, preact=True,
-            act_layer=nn.ReLU, conv_layer=StdConv2d, norm_layer=partial(GroupNormAct, num_groups=32),
-            drop_rate=0., drop_path_rate=0., zero_init_last=False):
+            self,
+            layers,
+            channels=(256, 512, 1024, 2048),
+            num_classes=1000,
+            in_chans=3,
+            global_pool='avg',
+            output_stride=32,
+            width_factor=1,
+            stem_chs=64,
+            stem_type='',
+            avg_down=False,
+            preact=True,
+            act_layer=nn.ReLU,
+            norm_layer=partial(GroupNormAct, num_groups=32),
+            conv_layer=StdConv2d,
+            drop_rate=0.,
+            drop_path_rate=0.,
+            zero_init_last=False,
+    ):
+        """
+        Args:
+            layers (List[int]) : number of layers in each block
+            channels (List[int]) : number of channels in each block:
+            num_classes (int): number of classification classes (default 1000)
+            in_chans (int): number of input (color) channels. (default 3)
+            global_pool (str): Global pooling type. One of 'avg', 'max', 'avgmax', 'catavgmax' (default 'avg')
+            output_stride (int): output stride of the network, 32, 16, or 8. (default 32)
+            width_factor (int): channel (width) multiplication factor
+            stem_chs (int): stem width (default: 64)
+            stem_type (str): stem type (default: '' == 7x7)
+            avg_down (bool): average pooling in residual downsampling (default: False)
+            preact (bool): pre-activiation (default: True)
+            act_layer (Union[str, nn.Module]): activation layer
+            norm_layer (Union[str, nn.Module]): normalization layer
+            conv_layer (nn.Module): convolution module
+            drop_rate: classifier dropout rate (default: 0.)
+            drop_path_rate: stochastic depth rate (default: 0.)
+            zero_init_last: zero-init last weight in residual path (default: False)
+        """
         super().__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
         wf = width_factor
+        norm_layer = get_norm_act_layer(norm_layer, act_layer=act_layer)
+        act_layer = get_act_layer(act_layer)
 
         self.feature_info = []
         stem_chs = make_div(stem_chs * wf)
         self.stem = create_resnetv2_stem(
-            in_chans, stem_chs, stem_type, preact, conv_layer=conv_layer, norm_layer=norm_layer)
+            in_chans,
+            stem_chs,
+            stem_type,
+            preact,
+            conv_layer=conv_layer,
+            norm_layer=norm_layer,
+        )
         stem_feat = ('stem.conv3' if is_stem_deep(stem_type) else 'stem.conv') if preact else 'stem.norm'
         self.feature_info.append(dict(num_chs=stem_chs, reduction=2, module=stem_feat))
 
         prev_chs = stem_chs
         curr_stride = 4
         dilation = 1
         block_dprs = [x.tolist() for x in torch.linspace(0, drop_path_rate, sum(layers)).split(layers)]
@@ -383,16 +493,26 @@
         for stage_idx, (d, c, bdpr) in enumerate(zip(layers, channels, block_dprs)):
             out_chs = make_div(c * wf)
             stride = 1 if stage_idx == 0 else 2
             if curr_stride >= output_stride:
                 dilation *= stride
                 stride = 1
             stage = ResNetStage(
-                prev_chs, out_chs, stride=stride, dilation=dilation, depth=d, avg_down=avg_down,
-                act_layer=act_layer, conv_layer=conv_layer, norm_layer=norm_layer, block_dpr=bdpr, block_fn=block_fn)
+                prev_chs,
+                out_chs,
+                stride=stride,
+                dilation=dilation,
+                depth=d,
+                avg_down=avg_down,
+                act_layer=act_layer,
+                conv_layer=conv_layer,
+                norm_layer=norm_layer,
+                block_dpr=bdpr,
+                block_fn=block_fn,
+            )
             prev_chs = out_chs
             curr_stride *= stride
             self.feature_info += [dict(num_chs=prev_chs, reduction=curr_stride, module=f'stages.{stage_idx}')]
             self.stages.add_module(str(stage_idx), stage)
 
         self.num_features = prev_chs
         self.norm = norm_layer(self.num_features) if preact else nn.Identity()
@@ -622,90 +742,87 @@
     """
     return _create_resnetv2_bit(
         'resnetv2_152x2_bit_teacher_384', pretrained=pretrained, layers=[3, 8, 36, 3], width_factor=2, **kwargs)
 
 
 @register_model
 def resnetv2_50(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50', pretrained=pretrained,
-        layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d, **kwargs)
+    model_args = dict(layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d)
+    return _create_resnetv2('resnetv2_50', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_50d(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50d', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d,
-        stem_type='deep', avg_down=True, **kwargs)
+        stem_type='deep', avg_down=True)
+    return _create_resnetv2('resnetv2_50d', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_50t(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50t', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d,
-        stem_type='tiered', avg_down=True, **kwargs)
+        stem_type='tiered', avg_down=True)
+    return _create_resnetv2('resnetv2_50t', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_101(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_101', pretrained=pretrained,
-        layers=[3, 4, 23, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d, **kwargs)
+    model_args = dict(layers=[3, 4, 23, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d)
+    return _create_resnetv2('resnetv2_101', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_101d(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_101d', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 23, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d,
-        stem_type='deep', avg_down=True, **kwargs)
+        stem_type='deep', avg_down=True)
+    return _create_resnetv2('resnetv2_101d', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_152(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_152', pretrained=pretrained,
-        layers=[3, 8, 36, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d, **kwargs)
+    model_args = dict(layers=[3, 8, 36, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d)
+    return _create_resnetv2('resnetv2_152', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_152d(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_152d', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 8, 36, 3], conv_layer=create_conv2d, norm_layer=BatchNormAct2d,
-        stem_type='deep', avg_down=True, **kwargs)
+        stem_type='deep', avg_down=True)
+    return _create_resnetv2('resnetv2_152d', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 # Experimental configs (may change / be removed)
 
 @register_model
 def resnetv2_50d_gn(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50d_gn', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=GroupNormAct,
-        stem_type='deep', avg_down=True, **kwargs)
+        stem_type='deep', avg_down=True)
+    return _create_resnetv2('resnetv2_50d_gn', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_50d_evob(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50d_evob', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=EvoNorm2dB0,
-        stem_type='deep', avg_down=True, zero_init_last=True, **kwargs)
+        stem_type='deep', avg_down=True, zero_init_last=True)
+    return _create_resnetv2('resnetv2_50d_evob', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_50d_evos(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50d_evos', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=EvoNorm2dS0,
-        stem_type='deep', avg_down=True, **kwargs)
+        stem_type='deep', avg_down=True)
+    return _create_resnetv2('resnetv2_50d_evos', pretrained=pretrained, **dict(model_args, **kwargs))
 
 
 @register_model
 def resnetv2_50d_frn(pretrained=False, **kwargs):
-    return _create_resnetv2(
-        'resnetv2_50d_frn', pretrained=pretrained,
+    model_args = dict(
         layers=[3, 4, 6, 3], conv_layer=create_conv2d, norm_layer=FilterResponseNormTlu2d,
-        stem_type='deep', avg_down=True, **kwargs)
+        stem_type='deep', avg_down=True)
+    return _create_resnetv2('resnetv2_50d_frn', pretrained=pretrained, **dict(model_args, **kwargs))
```

### Comparing `timm-0.8.3.dev0/timm/models/rexnet.py` & `timm-0.8.6.dev0/timm/models/rexnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/selecsls.py` & `timm-0.8.6.dev0/timm/models/selecsls.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/senet.py` & `timm-0.8.6.dev0/timm/models/senet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/sequencer.py` & `timm-0.8.6.dev0/timm/models/sequencer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/sknet.py` & `timm-0.8.6.dev0/timm/models/sknet.py`

 * *Files 8% similar despite different names*

```diff
@@ -43,17 +43,32 @@
 }
 
 
 class SelectiveKernelBasic(nn.Module):
     expansion = 1
 
     def __init__(
-            self, inplanes, planes, stride=1, downsample=None, cardinality=1, base_width=64,
-            sk_kwargs=None, reduce_first=1, dilation=1, first_dilation=None, act_layer=nn.ReLU,
-            norm_layer=nn.BatchNorm2d, attn_layer=None, aa_layer=None, drop_block=None, drop_path=None):
+            self,
+            inplanes,
+            planes,
+            stride=1,
+            downsample=None,
+            cardinality=1,
+            base_width=64,
+            sk_kwargs=None,
+            reduce_first=1,
+            dilation=1,
+            first_dilation=None,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            attn_layer=None,
+            aa_layer=None,
+            drop_block=None,
+            drop_path=None,
+    ):
         super(SelectiveKernelBasic, self).__init__()
 
         sk_kwargs = sk_kwargs or {}
         conv_kwargs = dict(act_layer=act_layer, norm_layer=norm_layer)
         assert cardinality == 1, 'BasicBlock only supports cardinality of 1'
         assert base_width == 64, 'BasicBlock doest not support changing base width'
         first_planes = planes // reduce_first
@@ -67,15 +82,16 @@
             first_planes, outplanes, kernel_size=3, dilation=dilation, apply_act=False, **conv_kwargs)
         self.se = create_attn(attn_layer, outplanes)
         self.act = act_layer(inplace=True)
         self.downsample = downsample
         self.drop_path = drop_path
 
     def zero_init_last(self):
-        nn.init.zeros_(self.conv2.bn.weight)
+        if getattr(self.conv2.bn, 'weight', None) is not None:
+            nn.init.zeros_(self.conv2.bn.weight)
 
     def forward(self, x):
         shortcut = x
         x = self.conv1(x)
         x = self.conv2(x)
         if self.se is not None:
             x = self.se(x)
@@ -88,17 +104,32 @@
         return x
 
 
 class SelectiveKernelBottleneck(nn.Module):
     expansion = 4
 
     def __init__(
-            self, inplanes, planes, stride=1, downsample=None, cardinality=1, base_width=64, sk_kwargs=None,
-            reduce_first=1, dilation=1, first_dilation=None, act_layer=nn.ReLU, norm_layer=nn.BatchNorm2d,
-            attn_layer=None, aa_layer=None, drop_block=None, drop_path=None):
+            self,
+            inplanes,
+            planes,
+            stride=1,
+            downsample=None,
+            cardinality=1,
+            base_width=64,
+            sk_kwargs=None,
+            reduce_first=1,
+            dilation=1,
+            first_dilation=None,
+            act_layer=nn.ReLU,
+            norm_layer=nn.BatchNorm2d,
+            attn_layer=None,
+            aa_layer=None,
+            drop_block=None,
+            drop_path=None,
+    ):
         super(SelectiveKernelBottleneck, self).__init__()
 
         sk_kwargs = sk_kwargs or {}
         conv_kwargs = dict(act_layer=act_layer, norm_layer=norm_layer)
         width = int(math.floor(planes * (base_width / 64)) * cardinality)
         first_planes = width // reduce_first
         outplanes = planes * self.expansion
@@ -111,15 +142,16 @@
         self.conv3 = ConvNormAct(width, outplanes, kernel_size=1, apply_act=False, **conv_kwargs)
         self.se = create_attn(attn_layer, outplanes)
         self.act = act_layer(inplace=True)
         self.downsample = downsample
         self.drop_path = drop_path
 
     def zero_init_last(self):
-        nn.init.zeros_(self.conv3.bn.weight)
+        if getattr(self.conv3.bn, 'weight', None) is not None:
+            nn.init.zeros_(self.conv3.bn.weight)
 
     def forward(self, x):
         shortcut = x
         x = self.conv1(x)
         x = self.conv2(x)
         x = self.conv3(x)
         if self.se is not None:
```

### Comparing `timm-0.8.3.dev0/timm/models/swin_transformer.py` & `timm-0.8.6.dev0/timm/models/swin_transformer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/swin_transformer_v2.py` & `timm-0.8.6.dev0/timm/models/swin_transformer_v2.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/swin_transformer_v2_cr.py` & `timm-0.8.6.dev0/timm/models/swin_transformer_v2_cr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/tnt.py` & `timm-0.8.6.dev0/timm/models/tnt.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/tresnet.py` & `timm-0.8.6.dev0/timm/models/tresnet.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/twins.py` & `timm-0.8.6.dev0/timm/models/twins.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/vgg.py` & `timm-0.8.6.dev0/timm/models/vgg.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/visformer.py` & `timm-0.8.6.dev0/timm/models/visformer.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/vision_transformer.py` & `timm-0.8.6.dev0/timm/models/vision_transformer.py`

 * *Files 6% similar despite different names*

```diff
@@ -693,14 +693,21 @@
         'first_conv': 'patch_embed.proj', 'classifier': 'head',
         **kwargs
     }
 
 
 default_cfgs = generate_default_cfgs({
 
+    # re-finetuned augreg 21k FT on in1k weights
+    'vit_base_patch16_224.augreg2_in21k_ft_in1k': _cfg(
+        hf_hub_id='timm/'),
+    'vit_base_patch16_384.augreg2_in21k_ft_in1k': _cfg(),
+    'vit_base_patch8_224.augreg2_in21k_ft_in1k': _cfg(
+        hf_hub_id='timm/'),
+
     # How to train your ViT (augreg) weights, pretrained on 21k FT on in1k
     'vit_tiny_patch16_224.augreg_in21k_ft_in1k': _cfg(
         url='https://storage.googleapis.com/vit_models/augreg/Ti_16-i21k-300ep-lr_0.001-aug_none-wd_0.03-do_0.0-sd_0.0--imagenet2012-steps_20k-lr_0.03-res_224.npz',
         hf_hub_id='timm/',
         custom_load=True),
     'vit_tiny_patch16_384.augreg_in21k_ft_in1k': _cfg(
         url='https://storage.googleapis.com/vit_models/augreg/Ti_16-i21k-300ep-lr_0.001-aug_none-wd_0.03-do_0.0-sd_0.0--imagenet2012-steps_20k-lr_0.03-res_384.npz',
@@ -747,21 +754,14 @@
         hf_hub_id='timm/',
         custom_load=True),
     'vit_large_patch16_384.augreg_in21k_ft_in1k': _cfg(
         url='https://storage.googleapis.com/vit_models/augreg/L_16-i21k-300ep-lr_0.001-aug_medium1-wd_0.1-do_0.1-sd_0.1--imagenet2012-steps_20k-lr_0.01-res_384.npz',
         hf_hub_id='timm/',
         custom_load=True, input_size=(3, 384, 384), crop_pct=1.0),
 
-    # re-finetuned augreg 21k FT on in1k weights
-    'vit_base_patch16_224.augreg2_in21k_ft_in1k': _cfg(
-        hf_hub_id='timm/'),
-    'vit_base_patch16_384.augreg2_in21k_ft_in1k': _cfg(),
-    'vit_base_patch8_224.augreg2_in21k_ft_in1k': _cfg(
-        hf_hub_id='timm/'),
-
     # patch models (weights from official Google JAX impl) pretrained on in21k FT on in1k
     'vit_base_patch16_224.orig_in21k_ft_in1k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-vitjx/jx_vit_base_p16_224-80ecf9dd.pth',
         hf_hub_id='timm/'),
     'vit_base_patch16_384.orig_in21k_ft_in1k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-vitjx/jx_vit_base_p16_384-83fb41ba.pth',
         hf_hub_id='timm/',
@@ -798,15 +798,14 @@
         custom_load=True, input_size=(3, 384, 384), crop_pct=1.0),
 
     'vit_large_patch14_224.untrained': _cfg(url=''),
     'vit_huge_patch14_224.untrained': _cfg(url=''),
     'vit_giant_patch14_224.untrained': _cfg(url=''),
     'vit_gigantic_patch14_224.untrained': _cfg(url=''),
 
-
     # patch models, imagenet21k (weights from official Google JAX impl)
     'vit_large_patch32_224.orig_in21k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-vitjx/jx_vit_large_patch32_224_in21k-9046d2e7.pth',
         hf_hub_id='timm/',
         num_classes=21843),
     'vit_huge_patch14_224.orig_in21k': _cfg(
         url='https://storage.googleapis.com/vit_models/imagenet21k/ViT-H_14.npz',
@@ -865,26 +864,25 @@
         hf_hub_id='timm/',
         mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD, num_classes=0),
     'vit_base_patch8_224.dino': _cfg(
         url='https://dl.fbaipublicfiles.com/dino/dino_vitbase8_pretrain/dino_vitbase8_pretrain.pth',
         hf_hub_id='timm/',
         mean=IMAGENET_DEFAULT_MEAN, std=IMAGENET_DEFAULT_STD, num_classes=0),
 
-
     # ViT ImageNet-21K-P pretraining by MILL
     'vit_base_patch16_224_miil.in21k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-tresnet/vit_base_patch16_224_in21k_miil-887286df.pth',
         hf_hub_id='timm/',
         mean=(0., 0., 0.), std=(1., 1., 1.), crop_pct=0.875, interpolation='bilinear', num_classes=11221),
     'vit_base_patch16_224_miil.in21k_ft_in1k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-tresnet/vit_base_patch16_224_1k_miil_84_4-2deb18e3.pth',
         hf_hub_id='timm/',
         mean=(0., 0., 0.), std=(1., 1., 1.), crop_pct=0.875, interpolation='bilinear'),
 
-    # custom timm variants
+    # Custom timm variants
     'vit_base_patch16_rpn_224.in1k': _cfg(
         url='https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-tpu-weights/vit_base_patch16_rpn_224-sw-3b07e89d.pth',
         hf_hub_id='timm/'),
     'vit_medium_patch16_gap_240.in12k': _cfg(
         hf_hub_id='timm/',
         input_size=(3, 240, 240), crop_pct=0.95, num_classes=11821),
     'vit_medium_patch16_gap_256.in12k_ft_in1k': _cfg(
@@ -892,60 +890,14 @@
         input_size=(3, 256, 256), crop_pct=0.95),
     'vit_medium_patch16_gap_384.in12k_ft_in1k': _cfg(
         hf_hub_id='timm/',
         input_size=(3, 384, 384), crop_pct=0.95, crop_mode='squash'),
     'vit_base_patch16_gap_224': _cfg(),
 
     # CLIP pretrained image tower and related fine-tuned weights
-    'vit_base_patch32_clip_224.laion2b': _cfg(
-        hf_hub_id='laion/CLIP-ViT-B-32-laion2B-s34B-b79K',
-        hf_hub_filename='open_clip_pytorch_model.bin',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=512),
-    'vit_base_patch16_clip_224.laion2b': _cfg(
-        #hf_hub_id='laion/CLIP-ViT-B-16-laion2B-s34B-b88K',
-        hf_hub_filename='open_clip_pytorch_model.bin',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=512),
-    'vit_large_patch14_clip_224.laion2b': _cfg(
-        hf_hub_id='laion/CLIP-ViT-L-14-laion2B-s32B-b82K',
-        hf_hub_filename='open_clip_pytorch_model.bin',
-        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD, crop_pct=1.0, num_classes=768),
-    'vit_huge_patch14_clip_224.laion2b': _cfg(
-        hf_hub_id='laion/CLIP-ViT-H-14-laion2B-s32B-b79K',
-        hf_hub_filename='open_clip_pytorch_model.bin',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=1024),
-    'vit_giant_patch14_clip_224.laion2b': _cfg(
-        hf_hub_id='laion/CLIP-ViT-g-14-laion2B-s12B-b42K',
-        hf_hub_filename='open_clip_pytorch_model.bin',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=1024),
-
-    'vit_base_patch32_clip_224.laion2b_ft_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
-    'vit_base_patch16_clip_224.laion2b_ft_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
-    'vit_base_patch16_clip_384.laion2b_ft_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
-        crop_pct=1.0, input_size=(3, 384, 384), crop_mode='squash'),
-    'vit_large_patch14_clip_224.laion2b_ft_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD, crop_pct=1.0),
-    'vit_large_patch14_clip_336.laion2b_ft_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD,
-        crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
-    'vit_huge_patch14_clip_224.laion2b_ft_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
-    'vit_huge_patch14_clip_336.laion2b_ft_in1k': _cfg(
-        hf_hub_id='',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
-        crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
-
     'vit_base_patch32_clip_224.laion2b_ft_in12k_in1k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
     'vit_base_patch32_clip_384.laion2b_ft_in12k_in1k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, input_size=(3, 384, 384)),
     'vit_base_patch32_clip_448.laion2b_ft_in12k_in1k': _cfg(
@@ -969,36 +921,60 @@
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
     'vit_huge_patch14_clip_336.laion2b_ft_in12k_in1k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
         crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
 
-    'vit_base_patch32_clip_224.laion2b_ft_in12k': _cfg(
-        #hf_hub_id='timm/vit_base_patch32_clip_224.laion2b_ft_in12k',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=11821),
-    'vit_base_patch16_clip_224.laion2b_ft_in12k': _cfg(
+    'vit_base_patch32_clip_224.openai_ft_in12k_in1k': _cfg(
+        # hf_hub_id='timm/vit_base_patch32_clip_224.openai_ft_in12k_in1k',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
+    'vit_base_patch32_clip_384.openai_ft_in12k_in1k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=11821),
-    'vit_large_patch14_clip_224.laion2b_ft_in12k': _cfg(
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
+        crop_pct=0.95, input_size=(3, 384, 384), crop_mode='squash'),
+    'vit_base_patch16_clip_224.openai_ft_in12k_in1k': _cfg(
         hf_hub_id='timm/',
-        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD, crop_pct=1.0, num_classes=11821),
-    'vit_huge_patch14_clip_224.laion2b_ft_in12k': _cfg(
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=0.95),
+    'vit_base_patch16_clip_384.openai_ft_in12k_in1k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=11821),
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
+        crop_pct=0.95, input_size=(3, 384, 384), crop_mode='squash'),
+    'vit_large_patch14_clip_224.openai_ft_in12k_in1k': _cfg(
+        hf_hub_id='timm/',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
+    'vit_large_patch14_clip_336.openai_ft_in12k_in1k': _cfg(
+        hf_hub_id='timm/',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
+        crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
 
-    'vit_base_patch32_clip_224.openai': _cfg(
+    'vit_base_patch32_clip_224.laion2b_ft_in1k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=512),
-    'vit_base_patch16_clip_224.openai': _cfg(
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
+    'vit_base_patch16_clip_224.laion2b_ft_in1k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=512),
-    'vit_large_patch14_clip_224.openai': _cfg(
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
+    'vit_base_patch16_clip_384.laion2b_ft_in1k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=768),
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
+        crop_pct=1.0, input_size=(3, 384, 384), crop_mode='squash'),
+    'vit_large_patch14_clip_224.laion2b_ft_in1k': _cfg(
+        hf_hub_id='timm/',
+        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD, crop_pct=1.0),
+    'vit_large_patch14_clip_336.laion2b_ft_in1k': _cfg(
+        hf_hub_id='timm/',
+        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD,
+        crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
+    'vit_huge_patch14_clip_224.laion2b_ft_in1k': _cfg(
+        hf_hub_id='timm/',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
+    'vit_huge_patch14_clip_336.laion2b_ft_in1k': _cfg(
+        hf_hub_id='',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
+        crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
 
     'vit_base_patch32_clip_224.openai_ft_in1k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
     'vit_base_patch16_clip_224.openai_ft_in1k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
@@ -1006,46 +982,68 @@
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
         crop_pct=1.0, input_size=(3, 384, 384), crop_mode='squash'),
     'vit_large_patch14_clip_224.openai_ft_in1k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
 
-    'vit_base_patch32_clip_224.openai_ft_in12k_in1k': _cfg(
-        #hf_hub_id='timm/vit_base_patch32_clip_224.openai_ft_in12k_in1k',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD),
-    'vit_base_patch32_clip_384.openai_ft_in12k_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
-        crop_pct=0.95, input_size=(3, 384, 384), crop_mode='squash'),
-    'vit_base_patch16_clip_224.openai_ft_in12k_in1k': _cfg(
-        hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=0.95),
-    'vit_base_patch16_clip_384.openai_ft_in12k_in1k': _cfg(
+    'vit_base_patch32_clip_224.laion2b_ft_in12k': _cfg(
+        #hf_hub_id='timm/vit_base_patch32_clip_224.laion2b_ft_in12k',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=11821),
+    'vit_base_patch16_clip_224.laion2b_ft_in12k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
-        crop_pct=0.95, input_size=(3, 384, 384), crop_mode='squash'),
-    'vit_large_patch14_clip_224.openai_ft_in12k_in1k': _cfg(
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=11821),
+    'vit_large_patch14_clip_224.laion2b_ft_in12k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0),
-    'vit_large_patch14_clip_336.openai_ft_in12k_in1k': _cfg(
+        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD, crop_pct=1.0, num_classes=11821),
+    'vit_huge_patch14_clip_224.laion2b_ft_in12k': _cfg(
         hf_hub_id='timm/',
-        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD,
-        crop_pct=1.0, input_size=(3, 336, 336), crop_mode='squash'),
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=11821),
 
     'vit_base_patch32_clip_224.openai_ft_in12k': _cfg(
-        #hf_hub_id='timm/vit_base_patch32_clip_224.openai_ft_in12k',
+        # hf_hub_id='timm/vit_base_patch32_clip_224.openai_ft_in12k',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=11821),
     'vit_base_patch16_clip_224.openai_ft_in12k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=11821),
     'vit_large_patch14_clip_224.openai_ft_in12k': _cfg(
         hf_hub_id='timm/',
         mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=11821),
 
+    'vit_base_patch32_clip_224.laion2b': _cfg(
+        hf_hub_id='laion/CLIP-ViT-B-32-laion2B-s34B-b79K',
+        hf_hub_filename='open_clip_pytorch_model.bin',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=512),
+    'vit_base_patch16_clip_224.laion2b': _cfg(
+        # hf_hub_id='laion/CLIP-ViT-B-16-laion2B-s34B-b88K',
+        hf_hub_filename='open_clip_pytorch_model.bin',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=512),
+    'vit_large_patch14_clip_224.laion2b': _cfg(
+        hf_hub_id='laion/CLIP-ViT-L-14-laion2B-s32B-b82K',
+        hf_hub_filename='open_clip_pytorch_model.bin',
+        mean=IMAGENET_INCEPTION_MEAN, std=IMAGENET_INCEPTION_STD, crop_pct=1.0, num_classes=768),
+    'vit_huge_patch14_clip_224.laion2b': _cfg(
+        hf_hub_id='laion/CLIP-ViT-H-14-laion2B-s32B-b79K',
+        hf_hub_filename='open_clip_pytorch_model.bin',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=1024),
+    'vit_giant_patch14_clip_224.laion2b': _cfg(
+        hf_hub_id='laion/CLIP-ViT-g-14-laion2B-s12B-b42K',
+        hf_hub_filename='open_clip_pytorch_model.bin',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=1024),
+
+    'vit_base_patch32_clip_224.openai': _cfg(
+        hf_hub_id='timm/',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=512),
+    'vit_base_patch16_clip_224.openai': _cfg(
+        hf_hub_id='timm/',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, num_classes=512),
+    'vit_large_patch14_clip_224.openai': _cfg(
+        hf_hub_id='timm/',
+        mean=OPENAI_CLIP_MEAN, std=OPENAI_CLIP_STD, crop_pct=1.0, num_classes=768),
+
     # experimental (may be removed)
     'vit_base_patch32_plus_256': _cfg(url='', input_size=(3, 256, 256), crop_pct=0.95),
     'vit_base_patch16_plus_240': _cfg(url='', input_size=(3, 240, 240), crop_pct=0.95),
     'vit_small_patch16_36x1_224': _cfg(url=''),
     'vit_small_patch16_18x2_224': _cfg(url=''),
     'vit_base_patch16_18x2_224': _cfg(url=''),
 
@@ -1148,455 +1146,467 @@
     )
 
 
 @register_model
 def vit_tiny_patch16_224(pretrained=False, **kwargs):
     """ ViT-Tiny (Vit-Ti/16)
     """
-    model_kwargs = dict(patch_size=16, embed_dim=192, depth=12, num_heads=3, **kwargs)
-    model = _create_vision_transformer('vit_tiny_patch16_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=192, depth=12, num_heads=3)
+    model = _create_vision_transformer('vit_tiny_patch16_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_tiny_patch16_384(pretrained=False, **kwargs):
     """ ViT-Tiny (Vit-Ti/16) @ 384x384.
     """
-    model_kwargs = dict(patch_size=16, embed_dim=192, depth=12, num_heads=3, **kwargs)
-    model = _create_vision_transformer('vit_tiny_patch16_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=192, depth=12, num_heads=3)
+    model = _create_vision_transformer('vit_tiny_patch16_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch32_224(pretrained=False, **kwargs):
     """ ViT-Small (ViT-S/32)
     """
-    model_kwargs = dict(patch_size=32, embed_dim=384, depth=12, num_heads=6, **kwargs)
-    model = _create_vision_transformer('vit_small_patch32_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=384, depth=12, num_heads=6)
+    model = _create_vision_transformer('vit_small_patch32_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch32_384(pretrained=False, **kwargs):
     """ ViT-Small (ViT-S/32) at 384x384.
     """
-    model_kwargs = dict(patch_size=32, embed_dim=384, depth=12, num_heads=6, **kwargs)
-    model = _create_vision_transformer('vit_small_patch32_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=384, depth=12, num_heads=6)
+    model = _create_vision_transformer('vit_small_patch32_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch16_224(pretrained=False, **kwargs):
     """ ViT-Small (ViT-S/16)
     """
-    model_kwargs = dict(patch_size=16, embed_dim=384, depth=12, num_heads=6, **kwargs)
-    model = _create_vision_transformer('vit_small_patch16_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=384, depth=12, num_heads=6)
+    model = _create_vision_transformer('vit_small_patch16_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch16_384(pretrained=False, **kwargs):
     """ ViT-Small (ViT-S/16)
     """
-    model_kwargs = dict(patch_size=16, embed_dim=384, depth=12, num_heads=6, **kwargs)
-    model = _create_vision_transformer('vit_small_patch16_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=384, depth=12, num_heads=6)
+    model = _create_vision_transformer('vit_small_patch16_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch8_224(pretrained=False, **kwargs):
     """ ViT-Small (ViT-S/8)
     """
-    model_kwargs = dict(patch_size=8, embed_dim=384, depth=12, num_heads=6, **kwargs)
-    model = _create_vision_transformer('vit_small_patch8_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=8, embed_dim=384, depth=12, num_heads=6)
+    model = _create_vision_transformer('vit_small_patch8_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch32_224(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/32) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=32, embed_dim=768, depth=12, num_heads=12, **kwargs)
-    model = _create_vision_transformer('vit_base_patch32_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=768, depth=12, num_heads=12)
+    model = _create_vision_transformer('vit_base_patch32_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch32_384(pretrained=False, **kwargs):
     """ ViT-Base model (ViT-B/32) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 384x384, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=32, embed_dim=768, depth=12, num_heads=12, **kwargs)
-    model = _create_vision_transformer('vit_base_patch32_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=768, depth=12, num_heads=12)
+    model = _create_vision_transformer('vit_base_patch32_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_224(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/16) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 224x224, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12)
+    model = _create_vision_transformer('vit_base_patch16_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_384(pretrained=False, **kwargs):
     """ ViT-Base model (ViT-B/16) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 384x384, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12)
+    model = _create_vision_transformer('vit_base_patch16_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch8_224(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/8) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 224x224, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=8, embed_dim=768, depth=12, num_heads=12, **kwargs)
-    model = _create_vision_transformer('vit_base_patch8_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=8, embed_dim=768, depth=12, num_heads=12)
+    model = _create_vision_transformer('vit_base_patch8_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch32_224(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/32) from original paper (https://arxiv.org/abs/2010.11929). No pretrained weights.
     """
-    model_kwargs = dict(patch_size=32, embed_dim=1024, depth=24, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_large_patch32_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=1024, depth=24, num_heads=16)
+    model = _create_vision_transformer('vit_large_patch32_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch32_384(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/32) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 384x384, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=32, embed_dim=1024, depth=24, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_large_patch32_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=1024, depth=24, num_heads=16)
+    model = _create_vision_transformer('vit_large_patch32_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch16_224(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/16) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 224x224, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=16, embed_dim=1024, depth=24, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_large_patch16_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=1024, depth=24, num_heads=16)
+    model = _create_vision_transformer('vit_large_patch16_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch16_384(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/16) from original paper (https://arxiv.org/abs/2010.11929).
     ImageNet-1k weights fine-tuned from in21k @ 384x384, source https://github.com/google-research/vision_transformer.
     """
-    model_kwargs = dict(patch_size=16, embed_dim=1024, depth=24, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_large_patch16_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=1024, depth=24, num_heads=16)
+    model = _create_vision_transformer('vit_large_patch16_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch14_224(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/14)
     """
-    model_kwargs = dict(patch_size=14, embed_dim=1024, depth=24, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_large_patch14_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1024, depth=24, num_heads=16)
+    model = _create_vision_transformer('vit_large_patch14_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_huge_patch14_224(pretrained=False, **kwargs):
     """ ViT-Huge model (ViT-H/14) from original paper (https://arxiv.org/abs/2010.11929).
     """
-    model_kwargs = dict(patch_size=14, embed_dim=1280, depth=32, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_huge_patch14_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1280, depth=32, num_heads=16)
+    model = _create_vision_transformer('vit_huge_patch14_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_giant_patch14_224(pretrained=False, **kwargs):
     """ ViT-Giant (little-g) model (ViT-g/14) from `Scaling Vision Transformers` - https://arxiv.org/abs/2106.04560
     """
-    model_kwargs = dict(patch_size=14, embed_dim=1408, mlp_ratio=48/11, depth=40, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_giant_patch14_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1408, mlp_ratio=48/11, depth=40, num_heads=16)
+    model = _create_vision_transformer('vit_giant_patch14_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_gigantic_patch14_224(pretrained=False, **kwargs):
     """ ViT-Gigantic (big-G) model (ViT-G/14) from `Scaling Vision Transformers` - https://arxiv.org/abs/2106.04560
     """
-    model_kwargs = dict(patch_size=14, embed_dim=1664, mlp_ratio=64/13, depth=48, num_heads=16, **kwargs)
-    model = _create_vision_transformer('vit_gigantic_patch14_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1664, mlp_ratio=64/13, depth=48, num_heads=16)
+    model = _create_vision_transformer(
+        'vit_gigantic_patch14_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_224_miil(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/16) from original paper (https://arxiv.org/abs/2010.11929).
     Weights taken from: https://github.com/Alibaba-MIIL/ImageNet21K
     """
-    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, qkv_bias=False, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_224_miil', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, qkv_bias=False)
+    model = _create_vision_transformer(
+        'vit_base_patch16_224_miil', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_medium_patch16_gap_240(pretrained=False, **kwargs):
     """ ViT-Medium (ViT-M/16) w/o class token, w/ avg-pool @ 240x240
     """
     model_kwargs = dict(
         patch_size=16, embed_dim=512, depth=12, num_heads=8, class_token=False,
-        global_pool=kwargs.get('global_pool', 'avg'), qkv_bias=False, init_values=1e-6, fc_norm=False, **kwargs)
-    model = _create_vision_transformer('vit_medium_patch16_gap_240', pretrained=pretrained, **model_kwargs)
+        global_pool='avg', qkv_bias=False, init_values=1e-6, fc_norm=False)
+    model = _create_vision_transformer(
+        'vit_medium_patch16_gap_240', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_medium_patch16_gap_256(pretrained=False, **kwargs):
     """ ViT-Medium (ViT-M/16) w/o class token, w/ avg-pool @ 256x256
     """
     model_kwargs = dict(
         patch_size=16, embed_dim=512, depth=12, num_heads=8, class_token=False,
-        global_pool=kwargs.get('global_pool', 'avg'), qkv_bias=False, init_values=1e-6, fc_norm=False, **kwargs)
-    model = _create_vision_transformer('vit_medium_patch16_gap_256', pretrained=pretrained, **model_kwargs)
+        global_pool='avg', qkv_bias=False, init_values=1e-6, fc_norm=False)
+    model = _create_vision_transformer(
+        'vit_medium_patch16_gap_256', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_medium_patch16_gap_384(pretrained=False, **kwargs):
     """ ViT-Medium (ViT-M/16) w/o class token, w/ avg-pool @ 384x384
     """
     model_kwargs = dict(
         patch_size=16, embed_dim=512, depth=12, num_heads=8, class_token=False,
-        global_pool=kwargs.get('global_pool', 'avg'), qkv_bias=False, init_values=1e-6, fc_norm=False, **kwargs)
-    model = _create_vision_transformer('vit_medium_patch16_gap_384', pretrained=pretrained, **model_kwargs)
+        global_pool='avg', qkv_bias=False, init_values=1e-6, fc_norm=False)
+    model = _create_vision_transformer(
+        'vit_medium_patch16_gap_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_gap_224(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/16) w/o class token, w/ avg-pool @ 256x256
     """
     model_kwargs = dict(
-        patch_size=16, embed_dim=768, depth=12, num_heads=16, class_token=False,
-        global_pool=kwargs.get('global_pool', 'avg'), fc_norm=False, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_gap_224', pretrained=pretrained, **model_kwargs)
+        patch_size=16, embed_dim=768, depth=12, num_heads=16, class_token=False, global_pool='avg', fc_norm=False)
+    model = _create_vision_transformer(
+        'vit_base_patch16_gap_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch32_clip_224(pretrained=False, **kwargs):
     """ ViT-B/32 CLIP image tower @ 224x224
     """
     model_kwargs = dict(
-        patch_size=32, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_base_patch32_clip_224', pretrained=pretrained, **model_kwargs)
+        patch_size=32, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_base_patch32_clip_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch32_clip_384(pretrained=False, **kwargs):
     """ ViT-B/32 CLIP image tower @ 384x384
     """
     model_kwargs = dict(
-        patch_size=32, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_base_patch32_clip_384', pretrained=pretrained, **model_kwargs)
+        patch_size=32, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_base_patch32_clip_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch32_clip_448(pretrained=False, **kwargs):
     """ ViT-B/32 CLIP image tower @ 448x448
     """
     model_kwargs = dict(
-        patch_size=32, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_base_patch32_clip_448', pretrained=pretrained, **model_kwargs)
+        patch_size=32, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_base_patch32_clip_448', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_clip_224(pretrained=False, **kwargs):
     """ ViT-B/16 CLIP image tower
     """
-    model_kwargs = dict(
-        patch_size=16, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_clip_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_base_patch16_clip_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_clip_384(pretrained=False, **kwargs):
     """ ViT-B/16 CLIP image tower @ 384x384
     """
-    model_kwargs = dict(
-        patch_size=16, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_clip_384', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_base_patch16_clip_384', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch14_clip_224(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/14) CLIP image tower
     """
-    model_kwargs = dict(
-        patch_size=14, embed_dim=1024, depth=24, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_large_patch14_clip_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1024, depth=24, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_large_patch14_clip_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_large_patch14_clip_336(pretrained=False, **kwargs):
     """ ViT-Large model (ViT-L/14) CLIP image tower @ 336x336
     """
-    model_kwargs = dict(
-        patch_size=14, embed_dim=1024, depth=24, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_large_patch14_clip_336', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1024, depth=24, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_large_patch14_clip_336', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_huge_patch14_clip_224(pretrained=False, **kwargs):
     """ ViT-Huge model (ViT-H/14) CLIP image tower.
     """
-    model_kwargs = dict(
-        patch_size=14, embed_dim=1280, depth=32, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_huge_patch14_clip_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1280, depth=32, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_huge_patch14_clip_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_huge_patch14_clip_336(pretrained=False, **kwargs):
     """ ViT-Huge model (ViT-H/14) CLIP image tower @ 336x336
     """
-    model_kwargs = dict(
-        patch_size=14, embed_dim=1280, depth=32, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_huge_patch14_clip_336', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1280, depth=32, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_huge_patch14_clip_336', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_giant_patch14_clip_224(pretrained=False, **kwargs):
     """ ViT-Giant (little-g) model (ViT-g/14) from `Scaling Vision Transformers` - https://arxiv.org/abs/2106.04560
     Pretrained weights from CLIP image tower.
     """
     model_kwargs = dict(
-        patch_size=14, embed_dim=1408, mlp_ratio=48/11, depth=40, num_heads=16,
-        pre_norm=True, norm_layer=nn.LayerNorm, **kwargs)
-    model = _create_vision_transformer('vit_giant_patch14_clip_224', pretrained=pretrained, **model_kwargs)
+        patch_size=14, embed_dim=1408, mlp_ratio=48/11, depth=40, num_heads=16, pre_norm=True, norm_layer=nn.LayerNorm)
+    model = _create_vision_transformer(
+        'vit_giant_patch14_clip_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 # Experimental models below
 
 @register_model
 def vit_base_patch32_plus_256(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/32+)
     """
-    model_kwargs = dict(patch_size=32, embed_dim=896, depth=12, num_heads=14, init_values=1e-5, **kwargs)
-    model = _create_vision_transformer('vit_base_patch32_plus_256', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=32, embed_dim=896, depth=12, num_heads=14, init_values=1e-5)
+    model = _create_vision_transformer(
+        'vit_base_patch32_plus_256', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_plus_240(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/16+)
     """
-    model_kwargs = dict(patch_size=16, embed_dim=896, depth=12, num_heads=14, init_values=1e-5, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_plus_240', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=896, depth=12, num_heads=14, init_values=1e-5)
+    model = _create_vision_transformer(
+        'vit_base_patch16_plus_240', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_rpn_224(pretrained=False, **kwargs):
     """ ViT-Base (ViT-B/16) w/ residual post-norm
     """
     model_kwargs = dict(
-        patch_size=16, embed_dim=768, depth=12, num_heads=12, qkv_bias=False, init_values=1e-5, class_token=False,
-        block_fn=ResPostBlock, global_pool=kwargs.pop('global_pool', 'avg'), **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_rpn_224', pretrained=pretrained, **model_kwargs)
+        patch_size=16, embed_dim=768, depth=12, num_heads=12, qkv_bias=False, init_values=1e-5,
+        class_token=False, block_fn=ResPostBlock, global_pool='avg')
+    model = _create_vision_transformer(
+        'vit_base_patch16_rpn_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch16_36x1_224(pretrained=False, **kwargs):
     """ ViT-Base w/ LayerScale + 36 x 1 (36 block serial) config. Experimental, may remove.
     Based on `Three things everyone should know about Vision Transformers` - https://arxiv.org/abs/2203.09795
     Paper focuses on 24x2 + 48x1 for 'Small' width but those are extremely slow.
     """
-    model_kwargs = dict(patch_size=16, embed_dim=384, depth=36, num_heads=6, init_values=1e-5, **kwargs)
-    model = _create_vision_transformer('vit_small_patch16_36x1_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=384, depth=36, num_heads=6, init_values=1e-5)
+    model = _create_vision_transformer(
+        'vit_small_patch16_36x1_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_small_patch16_18x2_224(pretrained=False, **kwargs):
     """ ViT-Small w/ LayerScale + 18 x 2 (36 block parallel) config. Experimental, may remove.
     Based on `Three things everyone should know about Vision Transformers` - https://arxiv.org/abs/2203.09795
     Paper focuses on 24x2 + 48x1 for 'Small' width but those are extremely slow.
     """
     model_kwargs = dict(
-        patch_size=16, embed_dim=384, depth=18, num_heads=6, init_values=1e-5, block_fn=ParallelBlock, **kwargs)
-    model = _create_vision_transformer('vit_small_patch16_18x2_224', pretrained=pretrained, **model_kwargs)
+        patch_size=16, embed_dim=384, depth=18, num_heads=6, init_values=1e-5, block_fn=ParallelBlock)
+    model = _create_vision_transformer(
+        'vit_small_patch16_18x2_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def vit_base_patch16_18x2_224(pretrained=False, **kwargs):
     """ ViT-Base w/ LayerScale + 18 x 2 (36 block parallel) config. Experimental, may remove.
     Based on `Three things everyone should know about Vision Transformers` - https://arxiv.org/abs/2203.09795
     """
-    model_kwargs = dict(
-        patch_size=16, embed_dim=768, depth=18, num_heads=12, init_values=1e-5, block_fn=ParallelBlock, **kwargs)
-    model = _create_vision_transformer('vit_base_patch16_18x2_224', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=18, num_heads=12, init_values=1e-5, block_fn=ParallelBlock)
+    model = _create_vision_transformer(
+        'vit_base_patch16_18x2_224', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def eva_large_patch14_196(pretrained=False, **kwargs):
     """ EVA-large model https://arxiv.org/abs/2211.07636 /via MAE MIM pretrain"""
-    model_kwargs = dict(
-        patch_size=14, embed_dim=1024, depth=24, num_heads=16, global_pool='avg', **kwargs)
-    model = _create_vision_transformer('eva_large_patch14_196', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1024, depth=24, num_heads=16, global_pool='avg')
+    model = _create_vision_transformer(
+        'eva_large_patch14_196', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def eva_large_patch14_336(pretrained=False, **kwargs):
     """ EVA-large model https://arxiv.org/abs/2211.07636 via MAE MIM pretrain"""
-    model_kwargs = dict(
-        patch_size=14, embed_dim=1024, depth=24, num_heads=16, global_pool='avg', **kwargs)
-    model = _create_vision_transformer('eva_large_patch14_336', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=14, embed_dim=1024, depth=24, num_heads=16, global_pool='avg')
+    model = _create_vision_transformer('eva_large_patch14_336', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def flexivit_small(pretrained=False, **kwargs):
     """ FlexiViT-Small
     """
-    model_kwargs = dict(patch_size=16, embed_dim=384, depth=12, num_heads=6, no_embed_class=True, **kwargs)
-    model = _create_vision_transformer('flexivit_small', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=384, depth=12, num_heads=6, no_embed_class=True)
+    model = _create_vision_transformer('flexivit_small', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def flexivit_base(pretrained=False, **kwargs):
     """ FlexiViT-Base
     """
-    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, no_embed_class=True, **kwargs)
-    model = _create_vision_transformer('flexivit_base', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=768, depth=12, num_heads=12, no_embed_class=True)
+    model = _create_vision_transformer('flexivit_base', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
 
 
 @register_model
 def flexivit_large(pretrained=False, **kwargs):
     """ FlexiViT-Large
     """
-    model_kwargs = dict(patch_size=16, embed_dim=1024, depth=24, num_heads=16, no_embed_class=True, **kwargs)
-    model = _create_vision_transformer('flexivit_large', pretrained=pretrained, **model_kwargs)
+    model_kwargs = dict(patch_size=16, embed_dim=1024, depth=24, num_heads=16, no_embed_class=True)
+    model = _create_vision_transformer('flexivit_large', pretrained=pretrained, **dict(model_kwargs, **kwargs))
     return model
```

### Comparing `timm-0.8.3.dev0/timm/models/vision_transformer_hybrid.py` & `timm-0.8.6.dev0/timm/models/vision_transformer_hybrid.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/vision_transformer_relpos.py` & `timm-0.8.6.dev0/timm/models/vision_transformer_relpos.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/volo.py` & `timm-0.8.6.dev0/timm/models/volo.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/vovnet.py` & `timm-0.8.6.dev0/timm/models/vovnet.py`

 * *Files 3% similar despite different names*

```diff
@@ -177,16 +177,26 @@
         x = torch.cat(concat_list, dim=1)
         return x
 
 
 class OsaBlock(nn.Module):
 
     def __init__(
-            self, in_chs, mid_chs, out_chs, layer_per_block, residual=False,
-            depthwise=False, attn='', norm_layer=BatchNormAct2d, act_layer=nn.ReLU, drop_path=None):
+            self,
+            in_chs,
+            mid_chs,
+            out_chs,
+            layer_per_block,
+            residual=False,
+            depthwise=False,
+            attn='',
+            norm_layer=BatchNormAct2d,
+            act_layer=nn.ReLU,
+            drop_path=None,
+    ):
         super(OsaBlock, self).__init__()
 
         self.residual = residual
         self.depthwise = depthwise
         conv_kwargs = dict(norm_layer=norm_layer, act_layer=act_layer)
 
         next_in_chs = in_chs
@@ -228,17 +238,28 @@
             x = x + output[0]
         return x
 
 
 class OsaStage(nn.Module):
 
     def __init__(
-            self, in_chs, mid_chs, out_chs, block_per_stage, layer_per_block, downsample=True,
-            residual=True, depthwise=False, attn='ese', norm_layer=BatchNormAct2d, act_layer=nn.ReLU,
-            drop_path_rates=None):
+            self,
+            in_chs,
+            mid_chs,
+            out_chs,
+            block_per_stage,
+            layer_per_block,
+            downsample=True,
+            residual=True,
+            depthwise=False,
+            attn='ese',
+            norm_layer=BatchNormAct2d,
+            act_layer=nn.ReLU,
+            drop_path_rates=None,
+    ):
         super(OsaStage, self).__init__()
         self.grad_checkpointing = False
 
         if downsample:
             self.pool = nn.MaxPool2d(kernel_size=3, stride=2, ceil_mode=True)
         else:
             self.pool = None
@@ -266,24 +287,46 @@
             x = self.blocks(x)
         return x
 
 
 class VovNet(nn.Module):
 
     def __init__(
-            self, cfg, in_chans=3, num_classes=1000, global_pool='avg', drop_rate=0., stem_stride=4,
-            output_stride=32, norm_layer=BatchNormAct2d, act_layer=nn.ReLU, drop_path_rate=0.):
-        """ VovNet (v2)
+            self,
+            cfg,
+            in_chans=3,
+            num_classes=1000,
+            global_pool='avg',
+            output_stride=32,
+            norm_layer=BatchNormAct2d,
+            act_layer=nn.ReLU,
+            drop_rate=0.,
+            drop_path_rate=0.,
+            **kwargs,
+    ):
+        """
+        Args:
+            cfg (dict): Model architecture configuration
+            in_chans (int): Number of input channels (default: 3)
+            num_classes (int): Number of classifier classes (default: 1000)
+            global_pool (str): Global pooling type (default: 'avg')
+            output_stride (int): Output stride of network, one of (8, 16, 32) (default: 32)
+            norm_layer (Union[str, nn.Module]): normalization layer
+            act_layer (Union[str, nn.Module]): activation layer
+            drop_rate (float): Dropout rate (default: 0.)
+            drop_path_rate (float): Stochastic depth drop-path rate (default: 0.)
+            kwargs (dict): Extra kwargs overlayed onto cfg
         """
         super(VovNet, self).__init__()
         self.num_classes = num_classes
         self.drop_rate = drop_rate
-        assert stem_stride in (4, 2)
         assert output_stride == 32  # FIXME support dilation
 
+        cfg = dict(cfg, **kwargs)
+        stem_stride = cfg.get("stem_stride", 4)
         stem_chs = cfg["stem_chs"]
         stage_conv_chs = cfg["stage_conv_chs"]
         stage_out_chs = cfg["stage_out_chs"]
         block_per_stage = cfg["block_per_stage"]
         layer_per_block = cfg["layer_per_block"]
         conv_kwargs = dict(norm_layer=norm_layer, act_layer=act_layer)
 
@@ -303,32 +346,37 @@
         stage_dpr = torch.split(torch.linspace(0, drop_path_rate, sum(block_per_stage)), block_per_stage)
         in_ch_list = stem_chs[-1:] + stage_out_chs[:-1]
         stage_args = dict(residual=cfg["residual"], depthwise=cfg["depthwise"], attn=cfg["attn"], **conv_kwargs)
         stages = []
         for i in range(4):  # num_stages
             downsample = stem_stride == 2 or i > 0  # first stage has no stride/downsample if stem_stride is 4
             stages += [OsaStage(
-                in_ch_list[i], stage_conv_chs[i], stage_out_chs[i], block_per_stage[i], layer_per_block,
-                downsample=downsample, drop_path_rates=stage_dpr[i], **stage_args)
-            ]
+                in_ch_list[i],
+                stage_conv_chs[i],
+                stage_out_chs[i],
+                block_per_stage[i],
+                layer_per_block,
+                downsample=downsample,
+                drop_path_rates=stage_dpr[i],
+                **stage_args,
+            )]
             self.num_features = stage_out_chs[i]
             current_stride *= 2 if downsample else 1
             self.feature_info += [dict(num_chs=self.num_features, reduction=current_stride, module=f'stages.{i}')]
 
         self.stages = nn.Sequential(*stages)
 
         self.head = ClassifierHead(self.num_features, num_classes, pool_type=global_pool, drop_rate=drop_rate)
 
         for n, m in self.named_modules():
             if isinstance(m, nn.Conv2d):
                 nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
             elif isinstance(m, nn.Linear):
                 nn.init.zeros_(m.bias)
 
-
     @torch.jit.ignore
     def group_matcher(self, coarse=False):
         return dict(
             stem=r'^stem',
             blocks=r'^stages\.(\d+)' if coarse else r'^stages\.(\d+).blocks\.(\d+)',
         )
```

### Comparing `timm-0.8.3.dev0/timm/models/xception.py` & `timm-0.8.6.dev0/timm/models/xception.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/xception_aligned.py` & `timm-0.8.6.dev0/timm/models/xception_aligned.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/models/xcit.py` & `timm-0.8.6.dev0/timm/models/xcit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/adabelief.py` & `timm-0.8.6.dev0/timm/optim/adabelief.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/adafactor.py` & `timm-0.8.6.dev0/timm/optim/adafactor.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/adahessian.py` & `timm-0.8.6.dev0/timm/optim/adahessian.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/adamp.py` & `timm-0.8.6.dev0/timm/optim/adamp.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/adamw.py` & `timm-0.8.6.dev0/timm/optim/adamw.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/adan.py` & `timm-0.8.6.dev0/timm/optim/adan.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/lamb.py` & `timm-0.8.6.dev0/timm/optim/lamb.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/lars.py` & `timm-0.8.6.dev0/timm/optim/lars.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/lookahead.py` & `timm-0.8.6.dev0/timm/optim/lookahead.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/madgrad.py` & `timm-0.8.6.dev0/timm/optim/madgrad.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/nadam.py` & `timm-0.8.6.dev0/timm/optim/nadam.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/nvnovograd.py` & `timm-0.8.6.dev0/timm/optim/nvnovograd.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/optim_factory.py` & `timm-0.8.6.dev0/timm/optim/optim_factory.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/radam.py` & `timm-0.8.6.dev0/timm/optim/radam.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/rmsprop_tf.py` & `timm-0.8.6.dev0/timm/optim/rmsprop_tf.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/optim/sgdp.py` & `timm-0.8.6.dev0/timm/optim/sgdp.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/cosine_lr.py` & `timm-0.8.6.dev0/timm/scheduler/cosine_lr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/multistep_lr.py` & `timm-0.8.6.dev0/timm/scheduler/multistep_lr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/plateau_lr.py` & `timm-0.8.6.dev0/timm/scheduler/plateau_lr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/poly_lr.py` & `timm-0.8.6.dev0/timm/scheduler/poly_lr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/scheduler.py` & `timm-0.8.6.dev0/timm/scheduler/scheduler.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/scheduler_factory.py` & `timm-0.8.6.dev0/timm/scheduler/scheduler_factory.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/step_lr.py` & `timm-0.8.6.dev0/timm/scheduler/step_lr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/scheduler/tanh_lr.py` & `timm-0.8.6.dev0/timm/scheduler/tanh_lr.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/__init__.py` & `timm-0.8.6.dev0/timm/utils/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,12 +4,12 @@
 from .cuda import ApexScaler, NativeScaler
 from .decay_batch import decay_batch_step, check_batch_size_retry
 from .distributed import distribute_bn, reduce_tensor, init_distributed_device,\
     world_info_from_env, is_distributed_env, is_primary
 from .jit import set_jit_legacy, set_jit_fuser
 from .log import setup_default_logging, FormatterNoInfo
 from .metrics import AverageMeter, accuracy
-from .misc import natural_key, add_bool_arg
+from .misc import natural_key, add_bool_arg, ParseKwargs
 from .model import unwrap_model, get_state_dict, freeze, unfreeze
 from .model_ema import ModelEma, ModelEmaV2
 from .random import random_seed
 from .summary import update_summary, get_outdir
```

### Comparing `timm-0.8.3.dev0/timm/utils/agc.py` & `timm-0.8.6.dev0/timm/utils/agc.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/checkpoint_saver.py` & `timm-0.8.6.dev0/timm/utils/checkpoint_saver.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/clip_grad.py` & `timm-0.8.6.dev0/timm/utils/clip_grad.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/cuda.py` & `timm-0.8.6.dev0/timm/utils/cuda.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/decay_batch.py` & `timm-0.8.6.dev0/timm/utils/decay_batch.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/distributed.py` & `timm-0.8.6.dev0/timm/utils/distributed.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/jit.py` & `timm-0.8.6.dev0/timm/utils/jit.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/log.py` & `timm-0.8.6.dev0/timm/utils/log.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/metrics.py` & `timm-0.8.6.dev0/timm/utils/metrics.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/model.py` & `timm-0.8.6.dev0/timm/utils/model.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/model_ema.py` & `timm-0.8.6.dev0/timm/utils/model_ema.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm/utils/summary.py` & `timm-0.8.6.dev0/timm/utils/summary.py`

 * *Files identical despite different names*

### Comparing `timm-0.8.3.dev0/timm.egg-info/PKG-INFO` & `timm-0.8.6.dev0/timm.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: timm
-Version: 0.8.3.dev0
+Version: 0.8.6.dev0
 Summary: (Unofficial) PyTorch Image Models
 Home-page: https://github.com/rwightman/pytorch-image-models
 Author: Ross Wightman
 Author-email: hello@rwightman.com
 Keywords: pytorch pretrained models efficientnet mobilenetv3 mnasnet resnet vision transformer vit
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Education
@@ -43,20 +43,33 @@
 * TPU Research Cloud (TRC) (https://sites.research.google/trc/about/)
 * Nvidia (https://www.nvidia.com/en-us/)
 
 And a big thanks to all GitHub sponsors who helped with some of my costs before I joined Hugging Face.
 
 ## What's New
 
-### 🤗 Survey: Feedback Appreciated 🤗
+* ❗Updates after Oct 10, 2022 are available in 0.8.x pre-releases (`pip install --pre timm`) or cloning main❗
+* Stable releases are 0.6.x and available by normal pip install or clone from [0.6.x](https://github.com/rwightman/pytorch-image-models/tree/0.6.x) branch.
 
-For a few months now, `timm` has been part of the Hugging Face ecosystem. Yearly, we survey users of our tools to see what we could do better, what we need to continue doing, or what we need to stop doing. 
-
-If you have a couple of minutes and want to participate in shaping the future of the ecosystem, please share your thoughts:
-[**hf.co/oss-survey**](https://hf.co/oss-survey) 🙏
+### Jan 11, 2023
+* Update ConvNeXt ImageNet-12k pretrain series w/ two new fine-tuned weights (and pre FT `.in12k` tags)
+  * `convnext_nano.in12k_ft_in1k` - 82.3 @ 224, 82.9 @ 288  (previously released)
+  * `convnext_tiny.in12k_ft_in1k` - 84.2 @ 224, 84.5 @ 288
+  * `convnext_small.in12k_ft_in1k` - 85.2 @ 224, 85.3 @ 288
+
+### Jan 6, 2023
+* Finally got around to adding `--model-kwargs` and `--opt-kwargs` to scripts to pass through rare args directly to model classes from cmd line
+  * `train.py /imagenet --model resnet50 --amp --model-kwargs output_stride=16 act_layer=silu`
+  * `train.py /imagenet --model vit_base_patch16_clip_224 --img-size 240 --amp --model-kwargs img_size=240 patch_size=12`
+* Cleanup some popular models to better support arg passthrough / merge with model configs, more to go. 
+
+### Jan 5, 2023
+* ConvNeXt-V2 models and weights added to existing `convnext.py`
+  * Paper: [ConvNeXt V2: Co-designing and Scaling ConvNets with Masked Autoencoders](http://arxiv.org/abs/2301.00808)
+  * Reference impl: https://github.com/facebookresearch/ConvNeXt-V2 (NOTE: weights currently CC-BY-NC)
 
 ### Dec 23, 2022 🎄☃
 * Add FlexiViT models and weights from https://github.com/google-research/big_vision (check out paper at https://arxiv.org/abs/2212.08013)
   * NOTE currently resizing is static on model creation, on-the-fly dynamic / train patch size sampling is a WIP
 * Many more models updated to multi-weight and downloadable via HF hub now (convnext, efficientnet, mobilenet, vision_transformer*, beit)
 * More model pretrained tag and adjustments, some model names changed (working on deprecation translations, consider main branch DEV branch right now, use 0.6.x for stable use)
 * More ImageNet-12k (subset of 22k) pretrain models popping up:
@@ -358,54 +371,14 @@
   * `mobilenetv2_050` - 65.9
   * `lcnet_100/075/050` - 72.1 / 68.8 / 63.1
   * `semnasnet_075` - 73
   * `fbnetv3_b/d/g` - 79.1 / 79.7 / 82.0
 * TinyNet models added by [rsomani95](https://github.com/rsomani95)
 * LCNet added via MobileNetV3 architecture
 
-### Nov 22, 2021
-* A number of updated weights anew new model defs
-  * `eca_halonext26ts` - 79.5 @ 256
-  * `resnet50_gn` (new) - 80.1 @ 224, 81.3 @ 288
-  * `resnet50` - 80.7 @ 224, 80.9 @ 288 (trained at 176, not replacing current a1 weights as default since these don't scale as well to higher res, [weights](https://github.com/rwightman/pytorch-image-models/releases/download/v0.1-rsb-weights/resnet50_a1h2_176-001a1197.pth))
-  * `resnext50_32x4d` - 81.1 @ 224, 82.0 @ 288
-  * `sebotnet33ts_256` (new) - 81.2 @ 224
-  * `lamhalobotnet50ts_256` - 81.5 @ 256
-  * `halonet50ts` - 81.7 @ 256
-  * `halo2botnet50ts_256` - 82.0 @ 256
-  * `resnet101` - 82.0 @ 224, 82.8 @ 288
-  * `resnetv2_101` (new) - 82.1 @ 224, 83.0 @ 288
-  * `resnet152` - 82.8 @ 224, 83.5 @ 288
-  * `regnetz_d8` (new) - 83.5 @ 256, 84.0 @ 320
-  * `regnetz_e8` (new) - 84.5 @ 256, 85.0 @ 320
-* `vit_base_patch8_224` (85.8 top-1) & `in21k` variant weights added thanks [Martins Bruveris](https://github.com/martinsbruveris)
-* Groundwork in for FX feature extraction thanks to [Alexander Soare](https://github.com/alexander-soare)
-  * models updated for tracing compatibility (almost full support with some distlled transformer exceptions)
-
-### Oct 19, 2021
-* ResNet strikes back (https://arxiv.org/abs/2110.00476) weights added, plus any extra training components used. Model weights and some more details here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-rsb-weights)
-* BCE loss and Repeated Augmentation support for RSB paper
-* 4 series of ResNet based attention model experiments being added (implemented across byobnet.py/byoanet.py). These include all sorts of attention, from channel attn like SE, ECA to 2D QKV self-attention layers such as Halo, Bottlneck, Lambda. Details here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-attn-weights)
-* Working implementations of the following 2D self-attention modules (likely to be differences from paper or eventual official impl):
-  * Halo (https://arxiv.org/abs/2103.12731)
-  * Bottleneck Transformer (https://arxiv.org/abs/2101.11605)
-  * LambdaNetworks (https://arxiv.org/abs/2102.08602)
-* A RegNetZ series of models with some attention experiments (being added to). These do not follow the paper (https://arxiv.org/abs/2103.06877) in any way other than block architecture, details of official models are not available. See more here (https://github.com/rwightman/pytorch-image-models/releases/tag/v0.1-attn-weights)
-* ConvMixer (https://openreview.net/forum?id=TVHS5Y4dNvM), CrossVit (https://arxiv.org/abs/2103.14899), and BeiT (https://arxiv.org/abs/2106.08254) architectures + weights added
-* freeze/unfreeze helpers by [Alexander Soare](https://github.com/alexander-soare)
-
-### Aug 18, 2021
-* Optimizer bonanza!
-  * Add LAMB and LARS optimizers, incl trust ratio clipping options. Tweaked to work properly in PyTorch XLA (tested on TPUs w/ `timm bits` [branch](https://github.com/rwightman/pytorch-image-models/tree/bits_and_tpu/timm/bits))
-  * Add MADGRAD from FB research w/ a few tweaks (decoupled decay option, step handling that works with PyTorch XLA)
-  * Some cleanup on all optimizers and factory. No more `.data`, a bit more consistency, unit tests for all!
-  * SGDP and AdamP still won't work with PyTorch XLA but others should (have yet to test Adabelief, Adafactor, Adahessian myself).
-* EfficientNet-V2 XL TF ported weights added, but they don't validate well in PyTorch (L is better). The pre-processing for the V2 TF training is a bit diff and the fine-tuned 21k -> 1k weights are very sensitive and less robust than the 1k weights.
-* Added PyTorch trained EfficientNet-V2 'Tiny' w/ GlobalContext attn weights. Only .1-.2 top-1 better than the SE so more of a curiosity for those interested.
-
 ## Introduction
 
 Py**T**orch **Im**age **M**odels (`timm`) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.
 
 The work of many others is present here. I've tried to make sure all source material is acknowledged via links to github, arxiv papers, etc in the README, documentation, and code docstrings. Please let me know if I missed anything.
 
 ## Models
@@ -418,14 +391,15 @@
 * BEiT - https://arxiv.org/abs/2106.08254
 * Big Transfer ResNetV2 (BiT) - https://arxiv.org/abs/1912.11370
 * Bottleneck Transformers - https://arxiv.org/abs/2101.11605
 * CaiT (Class-Attention in Image Transformers) - https://arxiv.org/abs/2103.17239
 * CoaT (Co-Scale Conv-Attentional Image Transformers) - https://arxiv.org/abs/2104.06399
 * CoAtNet (Convolution and Attention) - https://arxiv.org/abs/2106.04803
 * ConvNeXt - https://arxiv.org/abs/2201.03545
+* ConvNeXt-V2 - http://arxiv.org/abs/2301.00808
 * ConViT (Soft Convolutional Inductive Biases Vision Transformers)- https://arxiv.org/abs/2103.10697
 * CspNet (Cross-Stage Partial Networks) - https://arxiv.org/abs/1911.11929
 * DeiT - https://arxiv.org/abs/2012.12877
 * DeiT-III - https://arxiv.org/pdf/2204.07118.pdf
 * DenseNet - https://arxiv.org/abs/1608.06993
 * DLA - https://arxiv.org/abs/1707.06484
 * DPN (Dual-Path Network) - https://arxiv.org/abs/1707.01629
@@ -440,14 +414,15 @@
     * FBNet-C - https://arxiv.org/abs/1812.03443
     * MixNet - https://arxiv.org/abs/1907.09595
     * MNASNet B1, A1 (Squeeze-Excite), and Small - https://arxiv.org/abs/1807.11626
     * MobileNet-V2 - https://arxiv.org/abs/1801.04381
     * Single-Path NAS - https://arxiv.org/abs/1904.02877
     * TinyNet - https://arxiv.org/abs/2010.14819
 * EVA - https://arxiv.org/abs/2211.07636
+* FlexiViT - https://arxiv.org/abs/2212.08013
 * GCViT (Global Context Vision Transformer) - https://arxiv.org/abs/2206.09959
 * GhostNet - https://arxiv.org/abs/1911.11907
 * gMLP - https://arxiv.org/abs/2105.08050
 * GPU-Efficient Networks - https://arxiv.org/abs/2006.14090
 * Halo Nets - https://arxiv.org/abs/2103.12731
 * HRNet - https://arxiv.org/abs/1908.07919
 * Inception-V3 - https://arxiv.org/abs/1512.00567
```

### Comparing `timm-0.8.3.dev0/timm.egg-info/SOURCES.txt` & `timm-0.8.6.dev0/timm.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -58,14 +58,15 @@
 timm/layers/drop.py
 timm/layers/eca.py
 timm/layers/evo_norm.py
 timm/layers/fast_norm.py
 timm/layers/filter_response_norm.py
 timm/layers/gather_excite.py
 timm/layers/global_context.py
+timm/layers/grn.py
 timm/layers/halo_attn.py
 timm/layers/helpers.py
 timm/layers/inplace_abn.py
 timm/layers/lambda_layer.py
 timm/layers/linear.py
 timm/layers/median_pool.py
 timm/layers/mixed_conv2d.py
```

