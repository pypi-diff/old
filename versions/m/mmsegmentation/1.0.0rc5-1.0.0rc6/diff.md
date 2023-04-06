# Comparing `tmp/mmsegmentation-1.0.0rc5.tar.gz` & `tmp/mmsegmentation-1.0.0rc6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/mmsegmentation-1.0.0rc5.tar", last modified: Wed Feb  1 13:53:29 2023, max compression
+gzip compressed data, was "dist/mmsegmentation-1.0.0rc6.tar", last modified: Fri Mar  3 09:29:29 2023, max compression
```

## Comparing `mmsegmentation-1.0.0rc5.tar` & `mmsegmentation-1.0.0rc6.tar`

### file list

```diff
@@ -1,1146 +1,1151 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    14232 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    11658 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/ade20k.py
--rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/ade20k_640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     2364 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/chase_db1.py
--rw-r--r--   0 runner    (1001) docker     (123)     2207 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes.py
--rw-r--r--   0 runner    (1001) docker     (123)      995 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      993 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_768x768.py
--rw-r--r--   0 runner    (1001) docker     (123)      993 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      993 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)     2335 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/coco-stuff10k.py
--rw-r--r--   0 runner    (1001) docker     (123)     2220 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/coco-stuff164k.py
--rw-r--r--   0 runner    (1001) docker     (123)     2353 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/drive.py
--rw-r--r--   0 runner    (1001) docker     (123)     2353 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/hrf.py
--rw-r--r--   0 runner    (1001) docker     (123)     2359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/isaid.py
--rw-r--r--   0 runner    (1001) docker     (123)     2225 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/loveda.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     2417 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_context_59.py
--rw-r--r--   0 runner    (1001) docker     (123)     2313 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_voc12.py
--rw-r--r--   0 runner    (1001) docker     (123)     2639 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_voc12_aug.py
--rw-r--r--   0 runner    (1001) docker     (123)     2224 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/potsdam.py
--rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/stare.py
--rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/synapse.py
--rw-r--r--   0 runner    (1001) docker     (123)     2224 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/vaihingen.py
--rw-r--r--   0 runner    (1001) docker     (123)      434 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/default_runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/
--rw-r--r--   0 runner    (1001) docker     (123)     1571 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ann_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/apcnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     2239 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/bisenetv1_r18-d32.py
--rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/bisenetv2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1483 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ccnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1335 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/cgnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/danet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1498 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/deeplabv3_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1724 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/deeplabv3_unet_s5-d16.py
--rw-r--r--   0 runner    (1001) docker     (123)     1568 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/deeplabv3plus_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/dmnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/dnl_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/dpt_vit-b16.py
--rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/emanet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1660 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/encnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/erfnet_fcn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fast_scnn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1727 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fastfcn_r50-d32_jpu_psp.py
--rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fcn_hr18.py
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fcn_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fcn_unet_s5-d16.py
--rw-r--r--   0 runner    (1001) docker     (123)     1593 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fpn_poolformer_s12.py
--rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fpn_r50.py
--rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/gcnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     2379 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/icnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/isanet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)      991 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/lraspp_m-v3-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1540 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/nonlocal_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     2421 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ocrnet_hr18.py
--rw-r--r--   0 runner    (1001) docker     (123)     1610 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ocrnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/pointrend_r50.py
--rw-r--r--   0 runner    (1001) docker     (123)     1631 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/psanet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/pspnet_r50-d8.py
--rw-r--r--   0 runner    (1001) docker     (123)     1722 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/pspnet_unet_s5-d16.py
--rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/segformer_mit-b0.py
--rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/segmenter_vit-b16_mask.py
--rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/setr_mla.py
--rw-r--r--   0 runner    (1001) docker     (123)     2590 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/setr_naive.py
--rw-r--r--   0 runner    (1001) docker     (123)     2591 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/setr_pup.py
--rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/stdc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1667 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_upernet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1721 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_beit.py
--rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_convnext.py
--rw-r--r--   0 runner    (1001) docker     (123)     1696 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_mae.py
--rw-r--r--   0 runner    (1001) docker     (123)     1526 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_r50.py
--rw-r--r--   0 runner    (1001) docker     (123)     1815 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_swin.py
--rw-r--r--   0 runner    (1001) docker     (123)     1936 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_vit-b16_ln_mln.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_160k.py
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_20k.py
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_320k.py
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_40k.py
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_80k.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/
--rw-r--r--   0 runner    (1001) docker     (123)     9937 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann.yml
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/
--rw-r--r--   0 runner    (1001) docker     (123)     7891 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/
--rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)      684 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640_ms.py
--rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)      675 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640_ms.py
--rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/
--rw-r--r--   0 runner    (1001) docker     (123)     8662 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1.yml
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r101-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1918 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r101-d32_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      975 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb4-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      339 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      211 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb8-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      819 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32-in1k-pre_4xb4-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1713 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1917 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_coco-stuff164k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/
--rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2.yml
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      227 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-amp-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-ohem-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb8-160k_cityscapes-1024x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/
--rw-r--r--   0 runner    (1001) docker     (123)    10164 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/
--rw-r--r--   0 runner    (1001) docker     (123)     1810 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/cgnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb4-60k_cityscapes-680x680.py
--rw-r--r--   0 runner    (1001) docker     (123)     1145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb8-60k_cityscapes-512x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/
--rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     1790 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-large_upernet_8xb2-amp-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-small_upernet_8xb2-amp-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-tiny_upernet_8xb2-amp-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1795 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-xlarge_upernet_8xb2-amp-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     4516 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/
--rw-r--r--   0 runner    (1001) docker     (123)    10050 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/
--rw-r--r--   0 runner    (1001) docker     (123)    26875 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3.yml
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d16-mg124_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d16-mg124_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      251 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-20k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-320k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      163 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r101b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r18-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r18-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      292 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r18b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      291 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r18b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      282 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      282 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      364 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      376 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-20k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      376 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-320k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      587 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      587 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50b-d8_4xb2-80k_cityscapes-769x769.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/
--rw-r--r--   0 runner    (1001) docker     (123)    30163 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus.yml
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d16-mg124_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d16-mg124_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      149 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      149 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      167 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      334 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      329 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      330 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      331 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      333 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      347 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      346 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      368 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      379 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      588 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      379 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      364 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      588 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      368 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      370 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50b-d8_4xb2-80k_cityscapes-769x769.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/
--rw-r--r--   0 runner    (1001) docker     (123)     7793 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      573 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     7530 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnlnet.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dpt/
--rw-r--r--   0 runner    (1001) docker     (123)     1065 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dpt/dpt.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1168 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dpt/dpt_vit-b16_8xb2-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/
--rw-r--r--   0 runner    (1001) docker     (123)     3296 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/emanet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/emanet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/emanet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/emanet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/emanet_r50-d8_4xb2-80k_cityscapes-769x769.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/
--rw-r--r--   0 runner    (1001) docker     (123)     7785 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      398 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet_r50s-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/erfnet/
--rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/erfnet/erfnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      414 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/erfnet/erfnet_fcn_4xb4-160k_cityscapes-512x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/
--rw-r--r--   0 runner    (1001) docker     (123)     8419 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn.yml
--rw-r--r--   0 runner    (1001) docker     (123)      629 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      626 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      224 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      791 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      788 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      430 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb4-80k_cityscapes-512x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastscnn/
--rw-r--r--   0 runner    (1001) docker     (123)      605 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastscnn/fast_scnn_8xb4-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastscnn/fastscnn.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/
--rw-r--r--   0 runner    (1001) docker     (123)      140 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      140 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r101b-d16_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      161 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r101b-d16_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      417 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      542 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      417 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      542 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      140 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50b-d16_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50b-d16_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)    26880 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn.yml
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      157 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r101b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      274 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r18-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r18-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      286 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r18b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r18b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      574 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      574 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50b-d8_4xb2-80k_cityscapes-769x769.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/
--rw-r--r--   0 runner    (1001) docker     (123)    10180 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      455 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb2-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      274 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      274 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      318 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      531 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      318 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      307 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      307 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      531 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      310 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      378 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb2-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      383 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      383 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      414 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb2-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      413 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      409 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      410 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      419 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      410 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      407 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      416 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      419 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      409 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)    22609 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/hrnet.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/
--rw-r--r--   0 runner    (1001) docker     (123)     7403 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      247 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r101-d8-in1k-pre_4xb2-160k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r101-d8-in1k-pre_4xb2-80k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r101-d8_4xb2-160k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r101-d8_4xb2-80k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r18-d8-in1k-pre_4xb2-160k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r18-d8-in1k-pre_4xb2-80k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      147 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r18-d8_4xb2-160k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r18-d8_4xb2-80k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r50-d8-in1k-pre_4xb2-160k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r50-d8-in1k-pre_4xb2-80k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r50-d8_4xb2-160k_cityscapes-832x832.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet_r50-d8_4xb2-80k_cityscapes-832x832.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/
--rw-r--r--   0 runner    (1001) docker     (123)    11816 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/
--rw-r--r--   0 runner    (1001) docker     (123)     3466 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_deeplabv3_8xb2-adamw-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     3482 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_fcn_8xb2-adamw-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     3463 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_pspnet_8xb2-adamw-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_upernet_8xb2-adamw-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      835 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_swin-t_upernet_8xb2-adamw-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     5642 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/
--rw-r--r--   0 runner    (1001) docker     (123)      686 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512-ms.py
--rw-r--r--   0 runner    (1001) docker     (123)     1645 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      729 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/mae.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/
--rw-r--r--   0 runner    (1001) docker     (123)    10209 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former.yml
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_r101_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_r101_8xb2-90k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     7098 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     7057 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-90k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     8163 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-b-in1k-384x384-pre_8xb2-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)      314 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     1623 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-l-in22k-384x384-pre_8xb2-160k_ade20k-640x640.py
--rw-r--r--   0 runner    (1001) docker     (123)     1625 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-90k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1881 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1885 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-90k_cityscapes-512x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/
--rw-r--r--   0 runner    (1001) docker     (123)     3389 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer.yml
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_r101-d32_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     4619 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_r50-d32_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_swin-s_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_swin-t_upernet_8xb2-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      471 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      510 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3plus_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3plus_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_fcn_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      459 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_fcn_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      469 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_pspnet_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_pspnet_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     5716 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet_v2.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/
--rw-r--r--   0 runner    (1001) docker     (123)      779 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-s_lraspp_4xb4-320k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      729 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-scratch-s_lraspp_4xb4-320k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      505 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-scratch_lraspp_4xb4-320k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      569 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8_lraspp_4xb4-320k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     3533 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet_v3.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/
--rw-r--r--   0 runner    (1001) docker     (123)    10571 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_net.yml
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      140 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      140 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      458 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      458 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      362 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/
--rw-r--r--   0 runner    (1001) docker     (123)    14941 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb2-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1332 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      381 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb2-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      376 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1375 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      651 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      651 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-80k_cityscapes-512x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/
--rw-r--r--   0 runner    (1001) docker     (123)     3336 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/point_rend.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/pointrend_r101_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/pointrend_r101_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      522 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/pointrend_r50_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/pointrend_r50_4xb4-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/fpn_poolformer_m36_8xb4-40k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/fpn_poolformer_m48_8xb4-40k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2817 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/fpn_poolformer_s12_8xb4-40k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      394 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/fpn_poolformer_s24_8xb4-40k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/fpn_poolformer_s36_8x4_512x512_40k_ade20k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3232 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/poolformer.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/
--rw-r--r--   0 runner    (1001) docker     (123)    10372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      381 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/
--rw-r--r--   0 runner    (1001) docker     (123)    36141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-512x1024_dark-zurich-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-512x1024_night-driving-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-20k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-320k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      145 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      190 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-512x1024_dark-zurich-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      192 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-512x1024_night-driving-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r18b-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d32_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d32_rsb_4xb2-adamw-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8-rsb_4xb2-adamw-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      855 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_dark-zurich-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      881 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_night-driving-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      856 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_dark-zurich-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      881 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_night-driving-1920x1080.py
--rw-r--r--   0 runner    (1001) docker     (123)      456 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-160k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-20k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-320k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_coco-stuff10k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      372 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_coco-stuff164k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_isaid-896x896.py
--rw-r--r--   0 runner    (1001) docker     (123)      356 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_loveda-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      581 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-59-480x480.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_potsdam-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_vaihingen-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      405 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50b-d32_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      139 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50b-d8_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50b-d8_4xb2-80k_cityscapes-769x769.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/
--rw-r--r--   0 runner    (1001) docker     (123)     5870 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest.yml
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      292 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3plus_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3plus_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      264 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_fcn_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_fcn_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      270 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_pspnet_4xb2-80k_cityscapes512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest_s101-d8_pspnet_4xb4-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/
--rw-r--r--   0 runner    (1001) docker     (123)     9969 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb1-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b1_8xb1-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b1_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b2_8xb1-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b2_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b3_8xb1-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b3_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b4_8xb1-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b4_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb1-160k_cityscapes-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1313 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb2-160k_ade20k-640x640.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/
--rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter.yml
--rw-r--r--   0 runner    (1001) docker     (123)      510 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-b_mask_8xb1-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-l_mask_8xb1-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-s_fcn_8xb1-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1177 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-s_mask_8xb1-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      884 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-t_mask_8xb1-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/fpn_r101_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      243 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/fpn_r101_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/fpn_r50_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/fpn_r50_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     3137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/sem_fpn.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/
--rw-r--r--   0 runner    (1001) docker     (123)     5244 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2878 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l-mla_8xb1-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      808 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_mla_8xb1-80k_cityscapes-768x768.py
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_mla_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      805 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb1-80k_cityscapes-768x768.py
--rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2193 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb1-80k_cityscapes-768x768.py
--rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb2-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/
--rw-r--r--   0 runner    (1001) docker     (123)     2825 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc.yml
--rw-r--r--   0 runner    (1001) docker     (123)      653 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc1_4xb12-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      299 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc1_in1k-pre_4xb12-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      121 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc2_4xb12-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      299 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc2_in1k-pre_4xb12-80k_cityscapes-512x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/
--rw-r--r--   0 runner    (1001) docker     (123)      614 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-base-patch4-window12-in1k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-base-patch4-window12-in22k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      560 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-base-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      343 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-base-patch4-window7-in22k-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      407 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-large-patch4-window12-in22k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-large-patch4-window7-in22k-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-small-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-tiny-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     4610 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/
--rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins.yml
--rw-r--r--   0 runner    (1001) docker     (123)      323 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-b_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      485 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-b_uperhead_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      322 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-l_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      486 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-l_uperhead_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      430 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-s_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      827 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-s_uperhead_8xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-b_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      490 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-b_uperhead_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      478 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-l_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      523 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-l_uperhead_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      989 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-s_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-s_uperhead_8xb2-160k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/
--rw-r--r--   0 runner    (1001) docker     (123)      340 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-40k_drive-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-40k_hrf-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-40k_stare-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      269 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_chase-db1-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      263 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)      263 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_hrf-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-160k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      342 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_chase-db1-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      334 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_drive-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)      338 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_hrf-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      338 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_stare-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      263 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_chase-db1-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_hrf-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      259 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_chase-db1-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      337 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_drive-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_hrf-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_stare-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      266 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_chase-db1-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_hrf-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)    14416 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet_s5-d16_deeplabv3_4xb4-40k_chase-db1-128x128.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/
--rw-r--r--   0 runner    (1001) docker     (123)    10158 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet.yml
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r101_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r18_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r18_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      377 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r18_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      388 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r18_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      388 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r18_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      376 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r18_4xb4-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb2-40k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      454 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb2-40k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      277 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb2-80k_cityscapes-512x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)      454 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb2-80k_cityscapes-769x769.py
--rw-r--r--   0 runner    (1001) docker     (123)      359 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb4-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      370 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb4-20k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      370 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb4-40k_voc12aug-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      358 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet_r50_4xb4-80k_ade20k-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/
--rw-r--r--   0 runner    (1001) docker     (123)     7946 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit.yml
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-b16-ln_mln_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-b16_mln_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-b16_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-b16_upernet_8xb2-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-s16-ln_mln_upernet_512x512_160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      410 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-s16_mln_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-s16_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_deit-s16_upernet_8xb2-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_vit-b16-ln_mln_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1291 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-160k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1289 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-80k_ade20k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1384 2023-02-01 13:53:28.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/model-index.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/
--rw-r--r--   0 runner    (1001) docker     (123)     4478 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/analyze_logs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4292 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/benchmark.py
--rw-r--r--   0 runner    (1001) docker     (123)     6193 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/confusion_matrix.py
--rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/get_flops.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/
--rw-r--r--   0 runner    (1001) docker     (123)     3195 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/chase_db1.py
--rw-r--r--   0 runner    (1001) docker     (123)     1905 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/cityscapes.py
--rw-r--r--   0 runner    (1001) docker     (123)     6777 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/coco_stuff10k.py
--rw-r--r--   0 runner    (1001) docker     (123)     5186 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/coco_stuff164k.py
--rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/drive.py
--rw-r--r--   0 runner    (1001) docker     (123)     4355 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/hrf.py
--rw-r--r--   0 runner    (1001) docker     (123)     8147 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/isaid.py
--rw-r--r--   0 runner    (1001) docker     (123)     2662 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/loveda.py
--rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/pascal_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     5879 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/potsdam.py
--rw-r--r--   0 runner    (1001) docker     (123)     5992 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/stare.py
--rw-r--r--   0 runner    (1001) docker     (123)     5122 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/synapse.py
--rw-r--r--   0 runner    (1001) docker     (123)     5937 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/vaihingen.py
--rw-r--r--   0 runner    (1001) docker     (123)     3156 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/voc_aug.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/deployment/
--rw-r--r--   0 runner    (1001) docker     (123)     6064 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/deployment/pytorch2torchscript.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      458 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dist_test.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      421 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dist_train.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/
--rw-r--r--   0 runner    (1001) docker     (123)     2334 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/browse_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/print_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/publish_model.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/
--rw-r--r--   0 runner    (1001) docker     (123)     1757 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/beit2mmseg.py
--rw-r--r--   0 runner    (1001) docker     (123)     3081 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/mit2mmseg.py
--rw-r--r--   0 runner    (1001) docker     (123)     2319 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/stdc2mmseg.py
--rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/swin2mmseg.py
--rw-r--r--   0 runner    (1001) docker     (123)     2764 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/twins2mmseg.py
--rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/vit2mmseg.py
--rw-r--r--   0 runner    (1001) docker     (123)     4683 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/vitjax2mmseg.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      566 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/slurm_test.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      539 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/slurm_train.sh
--rw-r--r--   0 runner    (1001) docker     (123)     4078 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/test.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/
--rw-r--r--   0 runner    (1001) docker     (123)     3748 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/mmseg2torchserve.py
--rw-r--r--   0 runner    (1001) docker     (123)     1849 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/mmseg_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     1779 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/test_torchserve.py
--rw-r--r--   0 runner    (1001) docker     (123)     3678 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/.mim/tools/train.py
--rw-r--r--   0 runner    (1001) docker     (123)     2360 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/apis/
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/apis/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7684 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/apis/inference.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)     2565 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5763 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/ade.py
--rw-r--r--   0 runner    (1001) docker     (123)    11498 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/basesegdataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     1023 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/chase_db1.py
--rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/cityscapes.py
--rw-r--r--   0 runner    (1001) docker     (123)     6515 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/coco_stuff.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/dark_zurich.py
--rw-r--r--   0 runner    (1001) docker     (123)     4435 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/dataset_wrappers.py
--rw-r--r--   0 runner    (1001) docker     (123)     3260 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/decathlon.py
--rw-r--r--   0 runner    (1001) docker     (123)     1016 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/drive.py
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/hrf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1644 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/isaid.py
--rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/isprs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1419 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/lip.py
--rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/loveda.py
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/night_driving.py
--rw-r--r--   0 runner    (1001) docker     (123)     5777 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/pascal_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     1041 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/potsdam.py
--rw-r--r--   0 runner    (1001) docker     (123)     1005 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/stare.py
--rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/synapse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/
--rw-r--r--   0 runner    (1001) docker     (123)     1388 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3399 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/formatting.py
--rw-r--r--   0 runner    (1001) docker     (123)    15127 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/loading.py
--rw-r--r--   0 runner    (1001) docker     (123)    73873 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/transforms.py
--rw-r--r--   0 runner    (1001) docker     (123)     1507 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/datasets/voc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/engine/
--rw-r--r--   0 runner    (1001) docker     (123)      330 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/engine/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/engine/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)      137 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/engine/hooks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/engine/hooks/visualization_hook.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/engine/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/engine/optimizers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7969 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/engine/optimizers/layer_decay_optimizer_constructor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/evaluation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/evaluation/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/evaluation/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5732 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/evaluation/metrics/citys_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)    10560 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/evaluation/metrics/iou_metric.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/
--rw-r--r--   0 runner    (1001) docker     (123)      611 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    22825 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/beit.py
--rw-r--r--   0 runner    (1001) docker     (123)    11883 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/bisenetv1.py
--rw-r--r--   0 runner    (1001) docker     (123)    22936 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/bisenetv2.py
--rw-r--r--   0 runner    (1001) docker     (123)    13333 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/cgnet.py
--rw-r--r--   0 runner    (1001) docker     (123)    12993 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/erfnet.py
--rw-r--r--   0 runner    (1001) docker     (123)    15548 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/fast_scnn.py
--rw-r--r--   0 runner    (1001) docker     (123)    25089 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/hrnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5858 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/icnet.py
--rw-r--r--   0 runner    (1001) docker     (123)    10588 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/mae.py
--rw-r--r--   0 runner    (1001) docker     (123)    17436 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/mit.py
--rw-r--r--   0 runner    (1001) docker     (123)     7608 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/mobilenet_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)    10819 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/mobilenet_v3.py
--rw-r--r--   0 runner    (1001) docker     (123)    10203 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/resnest.py
--rw-r--r--   0 runner    (1001) docker     (123)    25701 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/resnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5291 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/resnext.py
--rw-r--r--   0 runner    (1001) docker     (123)    16047 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/stdc.py
--rw-r--r--   0 runner    (1001) docker     (123)    29703 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/swin.py
--rw-r--r--   0 runner    (1001) docker     (123)     1943 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/timm_backbone.py
--rw-r--r--   0 runner    (1001) docker     (123)    23612 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/twins.py
--rw-r--r--   0 runner    (1001) docker     (123)    18470 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/unet.py
--rw-r--r--   0 runner    (1001) docker     (123)    17736 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/backbones/vit.py
--rw-r--r--   0 runner    (1001) docker     (123)     1643 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     6229 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/data_preprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/
--rw-r--r--   0 runner    (1001) docker     (123)     1702 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9144 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/ann_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     5563 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/apc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/aspp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2291 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/cascade_decode_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/cc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     5852 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/da_head.py
--rw-r--r--   0 runner    (1001) docker     (123)    14265 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/decode_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     5018 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/dm_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4850 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/dnl_head.py
--rw-r--r--   0 runner    (1001) docker     (123)    10320 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/dpt_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     5803 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/ema_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     7159 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/enc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3317 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/fcn_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2416 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/fpn_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1634 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/gc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4923 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/isa_head.py
--rw-r--r--   0 runner    (1001) docker     (123)    19105 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/knet_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/lraspp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/mask2former_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     6709 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/maskformer_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1600 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/nl_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4218 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/ocr_head.py
--rw-r--r--   0 runner    (1001) docker     (123)    15249 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/point_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     7524 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/psa_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3867 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/psp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/segformer_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4858 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/segmenter_mask_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3474 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/sep_aspp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/sep_fcn_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2152 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/setr_mla_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/setr_up_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/stdc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4494 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/uper_head.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/
--rw-r--r--   0 runner    (1001) docker     (123)      681 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3618 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/accuracy.py
--rw-r--r--   0 runner    (1001) docker     (123)    11972 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/cross_entropy_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     4919 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/dice_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    15001 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/focal_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    12233 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/lovasz_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     4821 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/tversky_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     3961 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/losses/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2403 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/featurepyramid.py
--rw-r--r--   0 runner    (1001) docker     (123)     9209 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     5330 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/ic_neck.py
--rw-r--r--   0 runner    (1001) docker     (123)     5078 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/jpu.py
--rw-r--r--   0 runner    (1001) docker     (123)     3852 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/mla_neck.py
--rw-r--r--   0 runner    (1001) docker     (123)     2739 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/necks/multilevel_neck.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/segmentors/
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/segmentors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7923 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/segmentors/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5575 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/segmentors/cascade_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)    14523 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/segmentors/encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1703 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/segmentors/seg_tta.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12178 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/embed.py
--rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/encoding.py
--rw-r--r--   0 runner    (1001) docker     (123)     7116 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/inverted_residual.py
--rw-r--r--   0 runner    (1001) docker     (123)     1279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/make_divisible.py
--rw-r--r--   0 runner    (1001) docker     (123)     3384 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/res_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2160 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/se_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)     6187 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/self_attention_block.py
--rw-r--r--   0 runner    (1001) docker     (123)     3589 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/shape_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/up_conv_block.py
--rw-r--r--   0 runner    (1001) docker     (123)     1861 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/models/utils/wrappers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/registry/
--rw-r--r--   0 runner    (1001) docker     (123)      689 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/registry/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3963 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/registry/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/structures/
--rw-r--r--   0 runner    (1001) docker     (123)      270 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/structures/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/structures/sampler/
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/structures/sampler/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      332 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/structures/sampler/base_pixel_sampler.py
--rw-r--r--   0 runner    (1001) docker     (123)      433 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/structures/sampler/builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     3516 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/structures/sampler/ohem_pixel_sampler.py
--rw-r--r--   0 runner    (1001) docker     (123)     3039 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/structures/seg_data_sample.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/utils/
--rw-r--r--   0 runner    (1001) docker     (123)     1710 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16241 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/class_names.py
--rw-r--r--   0 runner    (1001) docker     (123)      491 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/collect_env.py
--rw-r--r--   0 runner    (1001) docker     (123)     1267 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/io.py
--rw-r--r--   0 runner    (1001) docker     (123)     4591 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/misc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1859 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/set_env.py
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/utils/typing_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      504 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmseg/visualization/
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/visualization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8107 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/mmseg/visualization/local_visualizer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    14232 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    65030 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/requirements/
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/requirements/docs.txt
--rw-r--r--   0 runner    (1001) docker     (123)      125 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/requirements/mminstall.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/requirements/optional.txt
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/requirements/readthedocs.txt
--rw-r--r--   0 runner    (1001) docker     (123)       45 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/requirements/runtime.txt
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/requirements/tests.txt
--rw-r--r--   0 runner    (1001) docker     (123)      623 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (123)     7365 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6088 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_digit_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/test_models/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5691 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_beit.py
--rw-r--r--   0 runner    (1001) docker     (123)     3410 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_bisenetv1.py
--rw-r--r--   0 runner    (1001) docker     (123)     1843 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_bisenetv2.py
--rw-r--r--   0 runner    (1001) docker     (123)     7340 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_blocks.py
--rw-r--r--   0 runner    (1001) docker     (123)     5214 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_cgnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5419 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_erfnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_fast_scnn.py
--rw-r--r--   0 runner    (1001) docker     (123)     4279 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_hrnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1526 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_icnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5773 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_mae.py
--rw-r--r--   0 runner    (1001) docker     (123)     4378 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_mit.py
--rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_mobilenet_v3.py
--rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_resnest.py
--rw-r--r--   0 runner    (1001) docker     (123)    20396 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_resnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_resnext.py
--rw-r--r--   0 runner    (1001) docker     (123)     4458 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_stdc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3209 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_swin.py
--rw-r--r--   0 runner    (1001) docker     (123)     4674 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_timm_backbone.py
--rw-r--r--   0 runner    (1001) docker     (123)     5967 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_twins.py
--rw-r--r--   0 runner    (1001) docker     (123)    30200 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_unet.py
--rw-r--r--   0 runner    (1001) docker     (123)     6203 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_vit.py
--rw-r--r--   0 runner    (1001) docker     (123)     1306 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2242 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_data_preprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     8229 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_forward.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      538 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_ann_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1751 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_apc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_aspp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      546 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_cc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     6943 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_decode_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1754 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_dm_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1584 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_dnl_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_dpt_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      647 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_ema_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4524 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_fcn_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      491 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_gc_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      521 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_isa_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_lraspp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     5549 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_mask2former_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1862 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_maskformer_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      491 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_nl_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      637 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_ocr_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3617 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_psa_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_psp_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_segformer_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      697 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_segmenter_mask_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_setr_mla_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1616 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_setr_up_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_uper_head.py
--rw-r--r--   0 runner    (1001) docker     (123)      627 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_heads/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1383 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_feature2pyramid.py
--rw-r--r--   0 runner    (1001) docker     (123)      967 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1559 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_ic_neck.py
--rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_jpu.py
--rw-r--r--   0 runner    (1001) docker     (123)      518 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_mla_neck.py
--rw-r--r--   0 runner    (1001) docker     (123)     1051 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_multilevel_neck.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1832 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/test_cascade_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     3335 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/test_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1956 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/test_seg_tta_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     3991 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-01 13:53:29.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_utils/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12979 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_utils/test_embed.py
--rw-r--r--   0 runner    (1001) docker     (123)     2423 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_models/test_utils/test_shape_convert.py
--rw-r--r--   0 runner    (1001) docker     (123)     2963 2023-02-01 13:53:26.000000 mmsegmentation-1.0.0rc5/tests/test_sampler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    16265 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    13475 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)     2276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/ade20k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/ade20k_640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/chase_db1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2190 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      995 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      993 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_768x768.py
+-rw-r--r--   0 runner    (1001) docker     (123)      993 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      993 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2318 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/coco-stuff10k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/coco-stuff164k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2336 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2336 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/hrf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2342 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/isaid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2208 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/loveda.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2400 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_context_59.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_voc12.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2622 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_voc12_aug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2207 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/potsdam.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3013 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/refuge.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/stare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/synapse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2207 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/vaihingen.py
+-rw-r--r--   0 runner    (1001) docker     (123)      434 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/default_runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/
+-rw-r--r--   0 runner    (1001) docker     (123)     1571 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ann_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/apcnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2239 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/bisenetv1_r18-d32.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/bisenetv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1483 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ccnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1335 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/cgnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/danet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1498 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/deeplabv3_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1724 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/deeplabv3_unet_s5-d16.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1568 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/deeplabv3plus_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/dmnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1541 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/dnl_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/dpt_vit-b16.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1554 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/emanet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1660 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/encnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/erfnet_fcn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fast_scnn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1727 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fastfcn_r50-d32_jpu_psp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fcn_hr18.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fcn_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1737 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fcn_unet_s5-d16.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fpn_poolformer_s12.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fpn_r50.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/gcnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2379 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/icnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/isanet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)      991 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/lraspp_m-v3-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1540 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/nonlocal_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2421 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ocrnet_hr18.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1610 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ocrnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/pointrend_r50.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1631 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/psanet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/pspnet_r50-d8.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1722 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/pspnet_unet_s5-d16.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1218 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/segformer_mit-b0.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/segmenter_vit-b16_mask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/setr_mla.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2590 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/setr_naive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2591 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/setr_pup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2946 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/stdc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1667 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1912 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_upernet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1721 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_beit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1752 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_convnext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1696 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_mae.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1526 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_r50.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1815 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_swin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1936 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_vit-b16_ln_mln.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_160k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_20k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_320k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_40k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      878 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_80k.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/
+-rw-r--r--   0 runner    (1001) docker     (123)     9937 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     7891 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/
+-rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)      684 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640_ms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)      675 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640_ms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1423 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/
+-rw-r--r--   0 runner    (1001) docker     (123)     8662 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r101-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1918 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r101-d32_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      975 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb4-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      339 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb8-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      819 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32-in1k-pre_4xb4-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32-in1k-pre_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1713 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1917 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_coco-stuff164k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/
+-rw-r--r--   0 runner    (1001) docker     (123)     3111 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-amp-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-ohem-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb8-160k_cityscapes-1024x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/
+-rw-r--r--   0 runner    (1001) docker     (123)    10164 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     1810 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/cgnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb4-60k_cityscapes-680x680.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb8-60k_cityscapes-512x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/
+-rw-r--r--   0 runner    (1001) docker     (123)     1281 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1790 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-large_upernet_8xb2-amp-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-small_upernet_8xb2-amp-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-tiny_upernet_8xb2-amp-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1795 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-xlarge_upernet_8xb2-amp-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4516 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/
+-rw-r--r--   0 runner    (1001) docker     (123)    10050 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/
+-rw-r--r--   0 runner    (1001) docker     (123)    26875 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d16-mg124_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d16-mg124_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      251 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-20k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-320k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      163 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r101b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r18-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r18-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      292 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r18b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      291 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r18b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      282 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      282 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      376 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-20k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      376 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-320k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      587 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      587 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50b-d8_4xb2-80k_cityscapes-769x769.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/
+-rw-r--r--   0 runner    (1001) docker     (123)    30163 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d16-mg124_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d16-mg124_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      149 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      149 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101-d8_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      167 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r101b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      334 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      329 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      330 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      331 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      333 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18-d8_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      347 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      346 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r18b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      588 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      364 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      588 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      368 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      370 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50b-d8_4xb2-80k_cityscapes-769x769.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     7793 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      573 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7530 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnlnet.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dpt/
+-rw-r--r--   0 runner    (1001) docker     (123)     1065 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dpt/dpt.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1168 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dpt/dpt_vit-b16_8xb2-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/
+-rw-r--r--   0 runner    (1001) docker     (123)     3296 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/emanet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/emanet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/emanet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/emanet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/emanet_r50-d8_4xb2-80k_cityscapes-769x769.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     7785 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      398 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet_r50s-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/erfnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     1220 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/erfnet/erfnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      414 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/erfnet/erfnet_fcn_4xb4-160k_cityscapes-512x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/
+-rw-r--r--   0 runner    (1001) docker     (123)     8419 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      629 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      626 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      791 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      788 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      430 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_psp_4xb4-80k_cityscapes-512x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastscnn/
+-rw-r--r--   0 runner    (1001) docker     (123)      605 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastscnn/fast_scnn_8xb4-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastscnn/fastscnn.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/
+-rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r101-d16_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r101b-d16_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      161 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r101b-d16_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      417 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      542 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      417 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      542 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50b-d16_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50b-d16_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26880 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      157 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r101b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      274 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r18-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r18-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      286 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r18b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r18b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      574 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      365 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      574 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50b-d8_4xb2-80k_cityscapes-769x769.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/
+-rw-r--r--   0 runner    (1001) docker     (123)    10180 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      455 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb2-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      274 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      274 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      318 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      531 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      318 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      307 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      531 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      310 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      378 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb2-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      383 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      383 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18s_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      414 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb2-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      413 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      413 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      409 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      410 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      419 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      410 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      416 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      419 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      409 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr48_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22609 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/hrnet.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     7403 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      247 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r101-d8-in1k-pre_4xb2-160k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r101-d8-in1k-pre_4xb2-80k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r101-d8_4xb2-160k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r101-d8_4xb2-80k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r18-d8-in1k-pre_4xb2-160k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r18-d8-in1k-pre_4xb2-80k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      147 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r18-d8_4xb2-160k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r18-d8_4xb2-80k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r50-d8-in1k-pre_4xb2-160k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r50-d8-in1k-pre_4xb2-80k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r50-d8_4xb2-160k_cityscapes-832x832.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet_r50-d8_4xb2-80k_cityscapes-832x832.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/
+-rw-r--r--   0 runner    (1001) docker     (123)    11816 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/
+-rw-r--r--   0 runner    (1001) docker     (123)     3466 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_deeplabv3_8xb2-adamw-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3482 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_fcn_8xb2-adamw-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3463 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_pspnet_8xb2-adamw-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_upernet_8xb2-adamw-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      835 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2023 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_swin-t_upernet_8xb2-adamw-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5642 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/
+-rw-r--r--   0 runner    (1001) docker     (123)      686 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512-ms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1645 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      729 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/mae.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/
+-rw-r--r--   0 runner    (1001) docker     (123)    10209 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_r101_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_r101_8xb2-90k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7098 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6982 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-90k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8089 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-b-in1k-384x384-pre_8xb2-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1623 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-l-in22k-384x384-pre_8xb2-160k_ade20k-640x640.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1625 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1478 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-90k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1881 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1885 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-90k_cityscapes-512x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/
+-rw-r--r--   0 runner    (1001) docker     (123)     3389 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_r101-d32_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4619 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_r50-d32_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_swin-s_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2512 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_swin-t_upernet_8xb2-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/
+-rw-r--r--   0 runner    (1001) docker     (123)      475 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      471 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      510 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3plus_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_deeplabv3plus_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_fcn_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      459 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_fcn_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      469 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_pspnet_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet-v2-d8_pspnet_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5769 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet_v2.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/
+-rw-r--r--   0 runner    (1001) docker     (123)      779 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-s_lraspp_4xb4-320k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      729 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-scratch-s_lraspp_4xb4-320k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      505 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-scratch_lraspp_4xb4-320k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      569 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8_lraspp_4xb4-320k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3533 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet_v3.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/
+-rw-r--r--   0 runner    (1001) docker     (123)    10571 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_net.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      140 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      281 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      458 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      281 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      458 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      362 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/
+-rw-r--r--   0 runner    (1001) docker     (123)    14952 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb2-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1333 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1332 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb2-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      376 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18s_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1375 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      651 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      651 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-80k_cityscapes-512x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/
+-rw-r--r--   0 runner    (1001) docker     (123)     3336 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/point_rend.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/pointrend_r101_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/pointrend_r101_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      522 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/pointrend_r50_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/pointrend_r50_4xb4-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/fpn_poolformer_m36_8xb4-40k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/fpn_poolformer_m48_8xb4-40k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2817 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/fpn_poolformer_s12_8xb4-40k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      394 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/fpn_poolformer_s24_8xb4-40k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/fpn_poolformer_s36_8x4_512x512_40k_ade20k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3232 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/poolformer.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/
+-rw-r--r--   0 runner    (1001) docker     (123)    10372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      381 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet_r50-d8_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/
+-rw-r--r--   0 runner    (1001) docker     (123)    36141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-512x1024_dark-zurich-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-512x1024_night-driving-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb2-amp-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-20k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-320k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      145 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101-d8_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      190 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-512x1024_dark-zurich-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      192 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-512x1024_night-driving-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r101b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18-d8_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r18b-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d32_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1101 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d32_rsb_4xb2-adamw-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1039 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8-rsb_4xb2-adamw-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      855 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_dark-zurich-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      881 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_night-driving-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      856 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_dark-zurich-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      881 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_night-driving-1920x1080.py
+-rw-r--r--   0 runner    (1001) docker     (123)      456 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-160k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-20k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-320k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_coco-stuff10k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      372 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_coco-stuff164k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_isaid-896x896.py
+-rw-r--r--   0 runner    (1001) docker     (123)      356 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_loveda-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      581 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-59-480x480.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_potsdam-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_vaihingen-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      405 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50b-d32_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      139 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50b-d8_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50b-d8_4xb2-80k_cityscapes-769x769.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/
+-rw-r--r--   0 runner    (1001) docker     (123)     5870 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      292 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3plus_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_deeplabv3plus_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      264 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_fcn_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_fcn_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      270 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_pspnet_4xb2-80k_cityscapes512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest_s101-d8_pspnet_4xb4-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/
+-rw-r--r--   0 runner    (1001) docker     (123)     9969 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb1-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b1_8xb1-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b1_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b2_8xb1-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b2_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b3_8xb1-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b3_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b4_8xb1-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b4_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb1-160k_cityscapes-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1313 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb2-160k_ade20k-640x640.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/
+-rw-r--r--   0 runner    (1001) docker     (123)     4136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      510 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-b_mask_8xb1-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1076 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-l_mask_8xb1-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-s_fcn_8xb1-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1177 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-s_mask_8xb1-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      884 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-t_mask_8xb1-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/fpn_r101_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      243 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/fpn_r101_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/fpn_r50_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/fpn_r50_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/sem_fpn.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/
+-rw-r--r--   0 runner    (1001) docker     (123)     5244 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2878 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l-mla_8xb1-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      808 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_mla_8xb1-80k_cityscapes-768x768.py
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_mla_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      805 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb1-80k_cityscapes-768x768.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2193 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb1-80k_cityscapes-768x768.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb2-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/
+-rw-r--r--   0 runner    (1001) docker     (123)     2825 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      653 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc1_4xb12-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      299 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc1_in1k-pre_4xb12-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      121 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc2_4xb12-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      299 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc2_in1k-pre_4xb12-80k_cityscapes-512x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/
+-rw-r--r--   0 runner    (1001) docker     (123)      614 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-base-patch4-window12-in1k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-base-patch4-window12-in22k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      560 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-base-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      343 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-base-patch4-window7-in22k-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-large-patch4-window12-in22k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-large-patch4-window7-in22k-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-small-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-tiny-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4610 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/
+-rw-r--r--   0 runner    (1001) docker     (123)     8775 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      323 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-b_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      485 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-b_uperhead_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-l_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      486 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-l_uperhead_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      430 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-s_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      827 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-s_uperhead_8xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-b_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      490 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-b_uperhead_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      478 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-l_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      523 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-l_uperhead_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      989 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-s_fpn_fpnhead_8xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-s_uperhead_8xb2-160k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/
+-rw-r--r--   0 runner    (1001) docker     (123)      340 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-40k_drive-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)      344 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-40k_hrf-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      344 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-40k_stare-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_chase-db1-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_hrf-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_deeplabv3_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      600 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-160k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      342 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_chase-db1-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      334 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_drive-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)      338 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_hrf-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      338 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-40k_stare-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_chase-db1-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_hrf-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      259 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_chase-db1-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      337 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_drive-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_hrf-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-40k_stare-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      266 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_chase-db1-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_drive-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_hrf-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_pspnet_4xb4-ce-1.0-dice-3.0-40k_stare-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14416 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet_s5-d16_deeplabv3_4xb4-40k_chase-db1-128x128.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/
+-rw-r--r--   0 runner    (1001) docker     (123)    10158 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r101_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r18_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r18_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      377 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r18_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r18_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r18_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      376 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r18_4xb4-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb2-40k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      454 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb2-40k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb2-80k_cityscapes-512x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)      454 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb2-80k_cityscapes-769x769.py
+-rw-r--r--   0 runner    (1001) docker     (123)      359 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb4-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      370 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb4-20k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      370 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb4-40k_voc12aug-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      358 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet_r50_4xb4-80k_ade20k-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/
+-rw-r--r--   0 runner    (1001) docker     (123)     7946 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-b16-ln_mln_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-b16_mln_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-b16_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-b16_upernet_8xb2-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-s16-ln_mln_upernet_512x512_160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      410 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-s16_mln_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-s16_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_deit-s16_upernet_8xb2-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1347 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_vit-b16-ln_mln_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1291 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-160k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1289 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-80k_ade20k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1384 2023-03-03 09:29:28.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/model-index.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/
+-rw-r--r--   0 runner    (1001) docker     (123)     4478 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/analyze_logs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4329 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/benchmark.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/browse_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6193 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/confusion_matrix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1728 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/get_flops.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/
+-rw-r--r--   0 runner    (1001) docker     (123)     3195 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/chase_db1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1905 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/cityscapes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6777 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/coco_stuff10k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5186 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/coco_stuff164k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4355 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/hrf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8147 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/isaid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2662 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/loveda.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/pascal_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5879 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/potsdam.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3773 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/refuge.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5992 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/stare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5122 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/synapse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5937 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/vaihingen.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3156 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/voc_aug.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/deployment/
+-rw-r--r--   0 runner    (1001) docker     (123)     6064 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/deployment/pytorch2torchscript.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      458 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dist_test.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      421 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dist_train.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)     2343 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/browse_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/print_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/publish_model.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/
+-rw-r--r--   0 runner    (1001) docker     (123)     1757 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/beit2mmseg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3081 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/mit2mmseg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2319 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/stdc2mmseg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/swin2mmseg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2764 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/twins2mmseg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/vit2mmseg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4683 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/vitjax2mmseg.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      566 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/slurm_test.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      539 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/slurm_train.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     3845 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/
+-rw-r--r--   0 runner    (1001) docker     (123)     3748 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/mmseg2torchserve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1849 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/mmseg_handler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1779 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/test_torchserve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3443 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/.mim/tools/train.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2360 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/apis/
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/apis/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7795 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/apis/inference.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15559 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/apis/mmseg_inferencer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5763 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/ade.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11637 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/basesegdataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1023 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/chase_db1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/cityscapes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6515 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/coco_stuff.py
+-rw-r--r--   0 runner    (1001) docker     (123)      501 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/dark_zurich.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4435 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/dataset_wrappers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3260 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/decathlon.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1016 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/drive.py
+-rw-r--r--   0 runner    (1001) docker     (123)      994 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/hrf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1644 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/isaid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/isprs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1419 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/lip.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/loveda.py
+-rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/night_driving.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5777 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/pascal_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1041 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/potsdam.py
+-rw-r--r--   0 runner    (1001) docker     (123)      948 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/refuge.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1005 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/stare.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/synapse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/
+-rw-r--r--   0 runner    (1001) docker     (123)     1388 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/formatting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16855 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/loading.py
+-rw-r--r--   0 runner    (1001) docker     (123)    73873 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1507 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/datasets/voc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/engine/
+-rw-r--r--   0 runner    (1001) docker     (123)      330 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/engine/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/engine/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)      137 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/engine/hooks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3941 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/engine/hooks/visualization_hook.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/engine/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/engine/optimizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7969 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/engine/optimizers/layer_decay_optimizer_constructor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/evaluation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/evaluation/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/evaluation/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5732 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/evaluation/metrics/citys_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10560 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/evaluation/metrics/iou_metric.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      611 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22825 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/beit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11883 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/bisenetv1.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22936 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/bisenetv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13333 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/cgnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12993 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/erfnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15548 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/fast_scnn.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25089 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/hrnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5858 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/icnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10588 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/mae.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17436 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/mit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7608 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/mobilenet_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10819 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/mobilenet_v3.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10203 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/resnest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25701 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/resnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5291 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/resnext.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16047 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/stdc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29703 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/swin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1943 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/timm_backbone.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23612 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/twins.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18470 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17736 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/backbones/vit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1643 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6229 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/data_preprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/
+-rw-r--r--   0 runner    (1001) docker     (123)     1702 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9144 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/ann_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5563 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/apc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3922 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/aspp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2291 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/cascade_decode_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/cc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5852 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/da_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14265 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/decode_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5018 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/dm_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4850 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/dnl_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10320 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/dpt_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5803 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/ema_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7159 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/enc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3317 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/fcn_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2416 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/fpn_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1634 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/gc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4923 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/isa_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19105 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/knet_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/lraspp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6112 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/mask2former_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6709 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/maskformer_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1600 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/nl_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4218 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/ocr_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15249 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/point_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7524 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/psa_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3867 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/psp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2038 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/segformer_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4858 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/segmenter_mask_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3474 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/sep_aspp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/sep_fcn_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2152 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/setr_mla_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2951 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/setr_up_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/stdc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4494 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/uper_head.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/
+-rw-r--r--   0 runner    (1001) docker     (123)      681 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3618 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/accuracy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11972 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/cross_entropy_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4919 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/dice_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15001 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/focal_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12233 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/lovasz_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4821 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/tversky_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3961 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/losses/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2403 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/featurepyramid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9209 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5330 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/ic_neck.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5078 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/jpu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3852 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/mla_neck.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2739 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/necks/multilevel_neck.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/segmentors/
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/segmentors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7923 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/segmentors/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5637 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/segmentors/cascade_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14523 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/segmentors/encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1703 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/segmentors/seg_tta.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12178 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/embed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/encoding.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7116 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/inverted_residual.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/make_divisible.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3384 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/res_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2160 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/se_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6187 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/self_attention_block.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3589 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/shape_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/up_conv_block.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1861 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/models/utils/wrappers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/registry/
+-rw-r--r--   0 runner    (1001) docker     (123)      836 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/registry/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4846 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/registry/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/structures/
+-rw-r--r--   0 runner    (1001) docker     (123)      270 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/structures/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/structures/sampler/
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/structures/sampler/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      332 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/structures/sampler/base_pixel_sampler.py
+-rw-r--r--   0 runner    (1001) docker     (123)      433 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/structures/sampler/builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3516 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/structures/sampler/ohem_pixel_sampler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3039 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/structures/seg_data_sample.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     1710 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16241 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/class_names.py
+-rw-r--r--   0 runner    (1001) docker     (123)      491 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/collect_env.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1267 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4591 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/misc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1859 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/set_env.py
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/utils/typing_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      504 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmseg/visualization/
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/visualization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10686 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/mmseg/visualization/local_visualizer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    16265 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    65227 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      327 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/requirements/
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/requirements/docs.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/requirements/mminstall.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/requirements/optional.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/requirements/readthedocs.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       45 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/requirements/runtime.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/requirements/tests.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      623 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7365 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6097 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1089 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_digit_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/test_models/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5691 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_beit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3410 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_bisenetv1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1843 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_bisenetv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7340 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_blocks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5214 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_cgnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5419 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_erfnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_fast_scnn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4279 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_hrnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1526 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_icnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5773 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_mae.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4378 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_mit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1961 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_mobilenet_v3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1468 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_resnest.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20396 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_resnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1982 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_resnext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4458 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_stdc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3209 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_swin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4674 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_timm_backbone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5967 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_twins.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30209 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6203 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_vit.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1306 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2242 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_data_preprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8238 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_forward.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      538 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_ann_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1751 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_apc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_aspp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      546 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_cc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6943 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_decode_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1754 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_dm_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1584 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_dnl_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_dpt_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      647 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_ema_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4524 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_fcn_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      491 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_gc_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      521 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_isa_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2093 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_lraspp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5549 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_mask2former_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_maskformer_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      491 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_nl_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      637 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_ocr_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3617 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_psa_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_psp_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_segformer_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      697 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_segmenter_mask_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1887 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_setr_mla_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1616 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_setr_up_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_uper_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)      627 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_heads/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1383 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_feature2pyramid.py
+-rw-r--r--   0 runner    (1001) docker     (123)      967 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1559 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_ic_neck.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_jpu.py
+-rw-r--r--   0 runner    (1001) docker     (123)      518 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_mla_neck.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1051 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_multilevel_neck.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1832 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/test_cascade_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3335 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/test_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1965 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/test_seg_tta_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3991 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 09:29:29.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12979 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_utils/test_embed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2423 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_models/test_utils/test_shape_convert.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2963 2023-03-03 09:29:19.000000 mmsegmentation-1.0.0rc6/tests/test_sampler.py
```

### Comparing `mmsegmentation-1.0.0rc5/PKG-INFO` & `mmsegmentation-1.0.0rc6/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mmsegmentation
-Version: 1.0.0rc5
+Version: 1.0.0rc6
 Summary: Open MMLab Semantic Segmentation Toolbox and Benchmark
 Home-page: http://github.com/open-mmlab/mmsegmentation
 Author: MMSegmentation Contributors
 Author-email: openmmlab@gmail.com
 License: Apache License 2.0
 Description: <div align="center">
           <img src="resources/mmseg-logo.png" width="600"/>
@@ -21,30 +21,44 @@
             <sup>
               <a href="https://platform.openmmlab.com">
                 <i><font size="4">TRY IT OUT</font></i>
               </a>
             </sup>
           </div>
           <div>&nbsp;</div>
-        </div>
-        <br />
         
         [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmsegmentation)](https://pypi.org/project/mmsegmentation/)
         [![PyPI](https://img.shields.io/pypi/v/mmsegmentation)](https://pypi.org/project/mmsegmentation)
         [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmsegmentation.readthedocs.io/en/1.x/)
         [![badge](https://github.com/open-mmlab/mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/mmsegmentation/actions)
         [![codecov](https://codecov.io/gh/open-mmlab/mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmsegmentation)
         [![license](https://img.shields.io/github/license/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/1.x/LICENSE)
         [![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
         [![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
         
         Documentation: <https://mmsegmentation.readthedocs.io/en/1.x/>
         
         English | [简体中文](README_zh-CN.md)
         
+        </div>
+        
+        <div align="center">
+          <a href="https://openmmlab.medium.com/" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218352562-cdded397-b0f3-4ca1-b8dd-a60df8dca75b.png" width="3%" alt="" /></a>
+          <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+          <a href="https://discord.gg/raweFPmdzG" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218347213-c080267f-cbb6-443e-8532-8e1ed9a58ea9.png" width="3%" alt="" /></a>
+          <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+          <a href="https://twitter.com/OpenMMLab" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218346637-d30c8a0f-3eba-4699-8131-512fb06d46db.png" width="3%" alt="" /></a>
+          <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+          <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
+        </div>
+        
         ## Introduction
         
         MMSegmentation is an open source semantic segmentation toolbox based on PyTorch.
         It is a part of the OpenMMLab project.
         
         The 1.x branch works with **PyTorch 1.6+**.
         
@@ -66,40 +80,41 @@
         
         - **High efficiency**
         
           The training speed is faster than or comparable to other codebases.
         
         ## What's New
         
-        v1.0.0rc5 was released on 01/02/2023.
+        v1.0.0rc6 was released on 03/03/2023.
         Please refer to [changelog.md](docs/en/notes/changelog.md) for details and release history.
         
-        - Support ISNet (ICCV'2021) in projects ([#2400](https://github.com/open-mmlab/mmsegmentation/pull/2400))
-        - Support HSSN (CVPR'2022) in projects ([#2444](https://github.com/open-mmlab/mmsegmentation/pull/2444))
+        - Support MMSegInferencer ([#2413](https://github.com/open-mmlab/mmsegmentation/pull/2413), [#2658](https://github.com/open-mmlab/mmsegmentation/pull/2658))
+        - Support REFUGE dataset ([#2554](https://github.com/open-mmlab/mmsegmentation/pull/2554))
         
         ## Installation
         
         Please refer to [get_started.md](docs/en/get_started.md#installation) for installation and [dataset_prepare.md](docs/en/user_guides/2_dataset_prepare.md#prepare-datasets) for dataset preparation.
         
         ## Get Started
         
         Please see [Overview](docs/en/overview.md) for the general introduction of MMSegmentation.
         
         Please see [user guides](https://mmsegmentation.readthedocs.io/en/1.x/user_guides/index.html#) for the basic usage of MMSegmentation.
         There are also [advanced tutorials](https://mmsegmentation.readthedocs.io/en/dev-1.x/advanced_guides/index.html) for in-depth understanding of mmseg design and implementation .
         
         A Colab tutorial is also provided. You may preview the notebook [here](demo/MMSegmentation_Tutorial.ipynb) or directly [run](https://colab.research.google.com/github/open-mmlab/mmsegmentation/blob/1.x/demo/MMSegmentation_Tutorial.ipynb) on Colab.
         
-        To migrate from MMSegmentation 1.x, please refer to [migration](docs/en/migration.md).
+        To migrate from MMSegmentation 1.x, please refer to [migration](docs/en/migration).
         
         ## Benchmark and model zoo
         
         Results and models are available in the [model zoo](docs/en/model_zoo.md).
         
-        Supported backbones:
+        <details open>
+        <summary>Supported backbones:</summary>
         
         - [x] ResNet (CVPR'2016)
         - [x] ResNeXt (CVPR'2017)
         - [x] [HRNet (CVPR'2019)](configs/hrnet)
         - [x] [ResNeSt (ArXiv'2020)](configs/resnest)
         - [x] [MobileNetV2 (CVPR'2018)](configs/mobilenet_v2)
         - [x] [MobileNetV3 (ICCV'2019)](configs/mobilenet_v3)
@@ -107,15 +122,18 @@
         - [x] [Swin Transformer (ICCV'2021)](configs/swin)
         - [x] [Twins (NeurIPS'2021)](configs/twins)
         - [x] [BEiT (ICLR'2022)](configs/beit)
         - [x] [ConvNeXt (CVPR'2022)](configs/convnext)
         - [x] [MAE (CVPR'2022)](configs/mae)
         - [x] [PoolFormer (CVPR'2022)](configs/poolformer)
         
-        Supported methods:
+        </details>
+        
+        <details open>
+        <summary>Supported methods:</summary>
         
         - [x] [FCN (CVPR'2015/TPAMI'2017)](configs/fcn)
         - [x] [ERFNet (T-ITS'2017)](configs/erfnet)
         - [x] [UNet (MICCAI'2016/Nat. Methods'2019)](configs/unet)
         - [x] [PSPNet (CVPR'2017)](configs/pspnet)
         - [x] [DeepLabV3 (ArXiv'2017)](configs/deeplabv3)
         - [x] [BiSeNetV1 (ECCV'2018)](configs/bisenetv1)
@@ -146,15 +164,18 @@
         - [x] [DPT (ArXiv'2021)](configs/dpt)
         - [x] [Segmenter (ICCV'2021)](configs/segmenter)
         - [x] [SegFormer (NeurIPS'2021)](configs/segformer)
         - [x] [K-Net (NeurIPS'2021)](configs/knet)
         - [x] [MaskFormer (NeurIPS'2021)](configs/maskformer)
         - [x] [Mask2Former (CVPR'2022)](configs/mask2former)
         
-        Supported datasets:
+        </details>
+        
+        <details open>
+        <summary>Supported datasets:</summary>
         
         - [x] [Cityscapes](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#cityscapes)
         - [x] [PASCAL VOC](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-voc)
         - [x] [ADE20K](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#ade20k)
         - [x] [Pascal Context](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-context)
         - [x] [COCO-Stuff 10k](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#coco-stuff-10k)
         - [x] [COCO-Stuff 164k](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#coco-stuff-164k)
@@ -165,16 +186,22 @@
         - [x] [Dark Zurich](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#dark-zurich)
         - [x] [Nighttime Driving](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#nighttime-driving)
         - [x] [LoveDA](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#loveda)
         - [x] [Potsdam](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isprs-potsdam)
         - [x] [Vaihingen](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isprs-vaihingen)
         - [x] [iSAID](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isaid)
         
+        </details>
+        
         Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions.
         
+        ## Projects
+        
+        [Here](projects/README.md) are some implementations of SOTA models and solutions built on MMSegmentation, which are supported and maintained by community users. These projects demonstrate the best practices based on MMSegmentation for research and product development. We welcome and appreciate all the contributions to OpenMMLab ecosystem.
+        
         ## Contributing
         
         We appreciate all contributions to improve MMSegmentation. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.
         
         ## Acknowledgement
         
         MMSegmentation is an open source project that welcome any contribution and feedback.
@@ -195,15 +222,15 @@
         }
         ```
         
         ## License
         
         This project is released under the [Apache 2.0 license](LICENSE).
         
-        ## Projects in OpenMMLab
+        ## OpenMMLab Family
         
         - [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models
         - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
         - [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
         - [MMEval](https://github.com/open-mmlab/mmeval): A unified evaluation library for multiple machine learning libraries.
         - [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
         - [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
```

#### html2text {}

```diff
@@ -1,70 +1,72 @@
-Metadata-Version: 2.1 Name: mmsegmentation Version: 1.0.0rc5 Summary: Open
+Metadata-Version: 2.1 Name: mmsegmentation Version: 1.0.0rc6 Summary: Open
 MMLab Semantic Segmentation Toolbox and Benchmark Home-page: http://github.com/
 open-mmlab/mmsegmentation Author: MMSegmentation Contributors Author-email:
 openmmlab@gmail.com License: Apache License 2.0 Description:
                           [resources/mmseg-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
-
-[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/
-mmsegmentation)](https://pypi.org/project/mmsegmentation/) [![PyPI](https://
+       [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/
+ mmsegmentation)](https://pypi.org/project/mmsegmentation/) [![PyPI](https://
 img.shields.io/pypi/v/mmsegmentation)](https://pypi.org/project/mmsegmentation)
-[![docs](https://img.shields.io/badge/docs-latest-blue)](https://
+       [![docs](https://img.shields.io/badge/docs-latest-blue)](https://
 mmsegmentation.readthedocs.io/en/1.x/) [![badge](https://github.com/open-mmlab/
-mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/
-mmsegmentation/actions) [![codecov](https://codecov.io/gh/open-mmlab/
-mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-
-mmlab/mmsegmentation) [![license](https://img.shields.io/github/license/open-
-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/
+   mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/
+     mmsegmentation/actions) [![codecov](https://codecov.io/gh/open-mmlab/
+  mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-
+ mmlab/mmsegmentation) [![license](https://img.shields.io/github/license/open-
+ mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/
 1.x/LICENSE) [![issue resolution](https://isitmaintained.com/badge/resolution/
-open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/
-issues) [![open issues](https://isitmaintained.com/badge/open/open-mmlab/
-mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
-Documentation:
-mmsegmentation.readthedocs.io/en/1.x/> English | [ç®ä½ä¸­æ](README_zh-
-CN.md) ## Introduction MMSegmentation is an open source semantic segmentation
-toolbox based on PyTorch. It is a part of the OpenMMLab project. The 1.x branch
-works with **PyTorch 1.6+**. ![demo image](resources/seg_demo.gif) ### Major
-features - **Unified Benchmark** We provide a unified benchmark toolbox for
-various semantic segmentation methods. - **Modular Design** We decompose the
-semantic segmentation framework into different components and one can easily
-construct a customized semantic segmentation framework by combining different
-modules. - **Support of multiple methods out of box** The toolbox directly
-supports popular and contemporary semantic segmentation frameworks, *e.g.*
-PSPNet, DeepLabV3, PSANet, DeepLabV3+, etc. - **High efficiency** The training
-speed is faster than or comparable to other codebases. ## What's New v1.0.0rc5
-was released on 01/02/2023. Please refer to [changelog.md](docs/en/notes/
-changelog.md) for details and release history. - Support ISNet (ICCV'2021) in
-projects ([#2400](https://github.com/open-mmlab/mmsegmentation/pull/2400)) -
-Support HSSN (CVPR'2022) in projects ([#2444](https://github.com/open-mmlab/
-mmsegmentation/pull/2444)) ## Installation Please refer to [get_started.md]
-(docs/en/get_started.md#installation) for installation and [dataset_prepare.md]
-(docs/en/user_guides/2_dataset_prepare.md#prepare-datasets) for dataset
-preparation. ## Get Started Please see [Overview](docs/en/overview.md) for the
-general introduction of MMSegmentation. Please see [user guides](https://
+ open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/
+   issues) [![open issues](https://isitmaintained.com/badge/open/open-mmlab/
+   mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
+                                Documentation:
+  mmsegmentation.readthedocs.io/en/1.x/> English | [ç®ä½ä¸­æ](README_zh-
+                                    CN.md)
+
+## Introduction MMSegmentation is an open source semantic segmentation toolbox
+based on PyTorch. It is a part of the OpenMMLab project. The 1.x branch works
+with **PyTorch 1.6+**. ![demo image](resources/seg_demo.gif) ### Major features
+- **Unified Benchmark** We provide a unified benchmark toolbox for various
+semantic segmentation methods. - **Modular Design** We decompose the semantic
+segmentation framework into different components and one can easily construct a
+customized semantic segmentation framework by combining different modules. -
+**Support of multiple methods out of box** The toolbox directly supports
+popular and contemporary semantic segmentation frameworks, *e.g.* PSPNet,
+DeepLabV3, PSANet, DeepLabV3+, etc. - **High efficiency** The training speed is
+faster than or comparable to other codebases. ## What's New v1.0.0rc6 was
+released on 03/03/2023. Please refer to [changelog.md](docs/en/notes/
+changelog.md) for details and release history. - Support MMSegInferencer (
+[#2413](https://github.com/open-mmlab/mmsegmentation/pull/2413), [#2658](https:
+//github.com/open-mmlab/mmsegmentation/pull/2658)) - Support REFUGE dataset (
+[#2554](https://github.com/open-mmlab/mmsegmentation/pull/2554)) ##
+Installation Please refer to [get_started.md](docs/en/
+get_started.md#installation) for installation and [dataset_prepare.md](docs/en/
+user_guides/2_dataset_prepare.md#prepare-datasets) for dataset preparation. ##
+Get Started Please see [Overview](docs/en/overview.md) for the general
+introduction of MMSegmentation. Please see [user guides](https://
 mmsegmentation.readthedocs.io/en/1.x/user_guides/index.html#) for the basic
 usage of MMSegmentation. There are also [advanced tutorials](https://
 mmsegmentation.readthedocs.io/en/dev-1.x/advanced_guides/index.html) for in-
 depth understanding of mmseg design and implementation . A Colab tutorial is
 also provided. You may preview the notebook [here](demo/
 MMSegmentation_Tutorial.ipynb) or directly [run](https://
 colab.research.google.com/github/open-mmlab/mmsegmentation/blob/1.x/demo/
 MMSegmentation_Tutorial.ipynb) on Colab. To migrate from MMSegmentation 1.x,
-please refer to [migration](docs/en/migration.md). ## Benchmark and model zoo
+please refer to [migration](docs/en/migration). ## Benchmark and model zoo
 Results and models are available in the [model zoo](docs/en/model_zoo.md).
 Supported backbones: - [x] ResNet (CVPR'2016) - [x] ResNeXt (CVPR'2017) - [x]
 [HRNet (CVPR'2019)](configs/hrnet) - [x] [ResNeSt (ArXiv'2020)](configs/
 resnest) - [x] [MobileNetV2 (CVPR'2018)](configs/mobilenet_v2) - [x]
 [MobileNetV3 (ICCV'2019)](configs/mobilenet_v3) - [x] [Vision Transformer
 (ICLR'2021)](configs/vit) - [x] [Swin Transformer (ICCV'2021)](configs/swin) -
 [x] [Twins (NeurIPS'2021)](configs/twins) - [x] [BEiT (ICLR'2022)](configs/
 beit) - [x] [ConvNeXt (CVPR'2022)](configs/convnext) - [x] [MAE (CVPR'2022)]
-(configs/mae) - [x] [PoolFormer (CVPR'2022)](configs/poolformer) Supported
+(configs/mae) - [x] [PoolFormer (CVPR'2022)](configs/poolformer)   Supported
 methods: - [x] [FCN (CVPR'2015/TPAMI'2017)](configs/fcn) - [x] [ERFNet (T-
 ITS'2017)](configs/erfnet) - [x] [UNet (MICCAI'2016/Nat. Methods'2019)]
 (configs/unet) - [x] [PSPNet (CVPR'2017)](configs/pspnet) - [x] [DeepLabV3
 (ArXiv'2017)](configs/deeplabv3) - [x] [BiSeNetV1 (ECCV'2018)](configs/
 bisenetv1) - [x] [PSANet (ECCV'2018)](configs/psanet) - [x] [DeepLabV3+
 (CVPR'2018)](configs/deeplabv3plus) - [x] [UPerNet (ECCV'2018)](configs/
 upernet) - [x] [ICNet (ECCV'2018)](configs/icnet) - [x] [NonLocal Net
@@ -79,16 +81,16 @@
 (configs/ocrnet) - [x] [DNLNet (ECCV'2020)](configs/dnlnet) - [x] [PointRend
 (CVPR'2020)](configs/point_rend) - [x] [CGNet (TIP'2020)](configs/cgnet) - [x]
 [BiSeNetV2 (IJCV'2021)](configs/bisenetv2) - [x] [STDC (CVPR'2021)](configs/
 stdc) - [x] [SETR (CVPR'2021)](configs/setr) - [x] [DPT (ArXiv'2021)](configs/
 dpt) - [x] [Segmenter (ICCV'2021)](configs/segmenter) - [x] [SegFormer
 (NeurIPS'2021)](configs/segformer) - [x] [K-Net (NeurIPS'2021)](configs/knet) -
 [x] [MaskFormer (NeurIPS'2021)](configs/maskformer) - [x] [Mask2Former
-(CVPR'2022)](configs/mask2former) Supported datasets: - [x] [Cityscapes](https:
-//github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
+(CVPR'2022)](configs/mask2former)   Supported datasets: - [x] [Cityscapes]
+(https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#cityscapes) - [x] [PASCAL VOC](https://github.com/open-
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-
 voc) - [x] [ADE20K](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/
 en/user_guides/2_dataset_prepare.md#ade20k) - [x] [Pascal Context](https://
 github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#pascal-context) - [x] [COCO-Stuff 10k](https://github.com/
 open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
@@ -108,59 +110,63 @@
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#loveda)
 - [x] [Potsdam](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/
 user_guides/2_dataset_prepare.md#isprs-potsdam) - [x] [Vaihingen](https://
 github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#isprs-vaihingen) - [x] [iSAID](https://github.com/open-
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isaid)
 Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions. ##
-Contributing We appreciate all contributions to improve MMSegmentation. Please
-refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing
-guideline. ## Acknowledgement MMSegmentation is an open source project that
-welcome any contribution and feedback. We wish that the toolbox and benchmark
-could serve the growing research community by providing a flexible as well as
-standardized toolkit to reimplement existing methods and develop their own new
-semantic segmentation methods. ## Citation If you find this project useful in
-your research, please consider cite: ```bibtex @misc{mmseg2020, title={
-{MMSegmentation}: OpenMMLab Semantic Segmentation Toolbox and Benchmark},
-author={MMSegmentation Contributors}, howpublished = {\url{https://github.com/
-open-mmlab/mmsegmentation}}, year={2020} } ``` ## License This project is
-released under the [Apache 2.0 license](LICENSE). ## Projects in OpenMMLab -
-[MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational
-library for training deep learning models - [MMCV](https://github.com/open-
-mmlab/mmcv): OpenMMLab foundational library for computer vision. - [MIM](https:
-//github.com/open-mmlab/mim): MIM installs OpenMMLab packages. - [MMEval]
-(https://github.com/open-mmlab/mmeval): A unified evaluation library for
-multiple machine learning libraries. - [MMClassification](https://github.com/
-open-mmlab/mmclassification): OpenMMLab image classification toolbox and
-benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection):
-OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
-github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for
-general 3D object detection. - [MMRotate](https://github.com/open-mmlab/
-mmrotate): OpenMMLab rotated object detection toolbox and benchmark. - [MMYOLO]
-(https://github.com/open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and
-benchmark. - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation):
-OpenMMLab semantic segmentation toolbox and benchmark. - [MMOCR](https://
-github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and
-understanding toolbox. - [MMPose](https://github.com/open-mmlab/mmpose):
-OpenMMLab pose estimation toolbox and benchmark. - [MMHuman3D](https://
-github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox
-and benchmark. - [MMSelfSup](https://github.com/open-mmlab/mmselfsup):
-OpenMMLab self-supervised learning toolbox and benchmark. - [MMRazor](https://
-github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and
-benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab
-fewshot learning toolbox and benchmark. - [MMAction2](https://github.com/open-
-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and
-benchmark. - [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab
-video perception toolbox and benchmark. - [MMFlow](https://github.com/open-
-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark. - [MMEditing]
-(https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing
-toolbox. - [MMGeneration](https://github.com/open-mmlab/mmgeneration):
-OpenMMLab image and video generative models toolbox. - [MMDeploy](https://
-github.com/open-mmlab/mmdeploy): OpenMMLab Model Deployment Framework.
-Keywords: computer vision,semantic segmentation Platform: UNKNOWN Classifier:
-Development Status :: 4 - Beta Classifier: License :: OSI Approved :: Apache
-Software License Classifier: Operating System :: OS Independent Classifier:
-Programming Language :: Python :: 3.6 Classifier: Programming Language ::
-Python :: 3.7 Classifier: Programming Language :: Python :: 3.8 Classifier:
-Programming Language :: Python :: 3.9 Description-Content-Type: text/markdown
-Provides-Extra: all Provides-Extra: tests Provides-Extra: optional Provides-
-Extra: mim
+Projects [Here](projects/README.md) are some implementations of SOTA models and
+solutions built on MMSegmentation, which are supported and maintained by
+community users. These projects demonstrate the best practices based on
+MMSegmentation for research and product development. We welcome and appreciate
+all the contributions to OpenMMLab ecosystem. ## Contributing We appreciate all
+contributions to improve MMSegmentation. Please refer to [CONTRIBUTING.md]
+(.github/CONTRIBUTING.md) for the contributing guideline. ## Acknowledgement
+MMSegmentation is an open source project that welcome any contribution and
+feedback. We wish that the toolbox and benchmark could serve the growing
+research community by providing a flexible as well as standardized toolkit to
+reimplement existing methods and develop their own new semantic segmentation
+methods. ## Citation If you find this project useful in your research, please
+consider cite: ```bibtex @misc{mmseg2020, title={{MMSegmentation}: OpenMMLab
+Semantic Segmentation Toolbox and Benchmark}, author={MMSegmentation
+Contributors}, howpublished = {\url{https://github.com/open-mmlab/
+mmsegmentation}}, year={2020} } ``` ## License This project is released under
+the [Apache 2.0 license](LICENSE). ## OpenMMLab Family - [MMEngine](https://
+github.com/open-mmlab/mmengine): OpenMMLab foundational library for training
+deep learning models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab
+foundational library for computer vision. - [MIM](https://github.com/open-
+mmlab/mim): MIM installs OpenMMLab packages. - [MMEval](https://github.com/
+open-mmlab/mmeval): A unified evaluation library for multiple machine learning
+libraries. - [MMClassification](https://github.com/open-mmlab/
+mmclassification): OpenMMLab image classification toolbox and benchmark. -
+[MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
+toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
+mmdetection3d): OpenMMLab's next-generation platform for general 3D object
+detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
+rotated object detection toolbox and benchmark. - [MMYOLO](https://github.com/
+open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and benchmark. -
+[MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab
+semantic segmentation toolbox and benchmark. - [MMOCR](https://github.com/open-
+mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
+- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation
+toolbox and benchmark. - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d):
+OpenMMLab 3D human parametric model toolbox and benchmark. - [MMSelfSup](https:
+//github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox
+and benchmark. - [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab
+model compression toolbox and benchmark. - [MMFewShot](https://github.com/open-
+mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark. -
+[MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-
+generation action understanding toolbox and benchmark. - [MMTracking](https://
+github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and
+benchmark. - [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical
+flow toolbox and benchmark. - [MMEditing](https://github.com/open-mmlab/
+mmediting): OpenMMLab image and video editing toolbox. - [MMGeneration](https:/
+/github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative
+models toolbox. - [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab
+Model Deployment Framework. Keywords: computer vision,semantic segmentation
+Platform: UNKNOWN Classifier: Development Status :: 4 - Beta Classifier:
+License :: OSI Approved :: Apache Software License Classifier: Operating System
+:: OS Independent Classifier: Programming Language :: Python :: 3.6 Classifier:
+Programming Language :: Python :: 3.7 Classifier: Programming Language ::
+Python :: 3.8 Classifier: Programming Language :: Python :: 3.9 Description-
+Content-Type: text/markdown Provides-Extra: all Provides-Extra: tests Provides-
+Extra: optional Provides-Extra: mim
```

### Comparing `mmsegmentation-1.0.0rc5/README.md` & `mmsegmentation-1.0.0rc6/README.md`

 * *Files 14% similar despite different names*

```diff
@@ -13,30 +13,44 @@
     <sup>
       <a href="https://platform.openmmlab.com">
         <i><font size="4">TRY IT OUT</font></i>
       </a>
     </sup>
   </div>
   <div>&nbsp;</div>
-</div>
-<br />
 
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmsegmentation)](https://pypi.org/project/mmsegmentation/)
 [![PyPI](https://img.shields.io/pypi/v/mmsegmentation)](https://pypi.org/project/mmsegmentation)
 [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmsegmentation.readthedocs.io/en/1.x/)
 [![badge](https://github.com/open-mmlab/mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/mmsegmentation/actions)
 [![codecov](https://codecov.io/gh/open-mmlab/mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmsegmentation)
 [![license](https://img.shields.io/github/license/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/1.x/LICENSE)
 [![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
 [![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
 
 Documentation: <https://mmsegmentation.readthedocs.io/en/1.x/>
 
 English | [简体中文](README_zh-CN.md)
 
+</div>
+
+<div align="center">
+  <a href="https://openmmlab.medium.com/" style="text-decoration:none;">
+    <img src="https://user-images.githubusercontent.com/25839884/218352562-cdded397-b0f3-4ca1-b8dd-a60df8dca75b.png" width="3%" alt="" /></a>
+  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+  <a href="https://discord.gg/raweFPmdzG" style="text-decoration:none;">
+    <img src="https://user-images.githubusercontent.com/25839884/218347213-c080267f-cbb6-443e-8532-8e1ed9a58ea9.png" width="3%" alt="" /></a>
+  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+  <a href="https://twitter.com/OpenMMLab" style="text-decoration:none;">
+    <img src="https://user-images.githubusercontent.com/25839884/218346637-d30c8a0f-3eba-4699-8131-512fb06d46db.png" width="3%" alt="" /></a>
+  <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+  <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
+    <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
+</div>
+
 ## Introduction
 
 MMSegmentation is an open source semantic segmentation toolbox based on PyTorch.
 It is a part of the OpenMMLab project.
 
 The 1.x branch works with **PyTorch 1.6+**.
 
@@ -58,40 +72,41 @@
 
 - **High efficiency**
 
   The training speed is faster than or comparable to other codebases.
 
 ## What's New
 
-v1.0.0rc5 was released on 01/02/2023.
+v1.0.0rc6 was released on 03/03/2023.
 Please refer to [changelog.md](docs/en/notes/changelog.md) for details and release history.
 
-- Support ISNet (ICCV'2021) in projects ([#2400](https://github.com/open-mmlab/mmsegmentation/pull/2400))
-- Support HSSN (CVPR'2022) in projects ([#2444](https://github.com/open-mmlab/mmsegmentation/pull/2444))
+- Support MMSegInferencer ([#2413](https://github.com/open-mmlab/mmsegmentation/pull/2413), [#2658](https://github.com/open-mmlab/mmsegmentation/pull/2658))
+- Support REFUGE dataset ([#2554](https://github.com/open-mmlab/mmsegmentation/pull/2554))
 
 ## Installation
 
 Please refer to [get_started.md](docs/en/get_started.md#installation) for installation and [dataset_prepare.md](docs/en/user_guides/2_dataset_prepare.md#prepare-datasets) for dataset preparation.
 
 ## Get Started
 
 Please see [Overview](docs/en/overview.md) for the general introduction of MMSegmentation.
 
 Please see [user guides](https://mmsegmentation.readthedocs.io/en/1.x/user_guides/index.html#) for the basic usage of MMSegmentation.
 There are also [advanced tutorials](https://mmsegmentation.readthedocs.io/en/dev-1.x/advanced_guides/index.html) for in-depth understanding of mmseg design and implementation .
 
 A Colab tutorial is also provided. You may preview the notebook [here](demo/MMSegmentation_Tutorial.ipynb) or directly [run](https://colab.research.google.com/github/open-mmlab/mmsegmentation/blob/1.x/demo/MMSegmentation_Tutorial.ipynb) on Colab.
 
-To migrate from MMSegmentation 1.x, please refer to [migration](docs/en/migration.md).
+To migrate from MMSegmentation 1.x, please refer to [migration](docs/en/migration).
 
 ## Benchmark and model zoo
 
 Results and models are available in the [model zoo](docs/en/model_zoo.md).
 
-Supported backbones:
+<details open>
+<summary>Supported backbones:</summary>
 
 - [x] ResNet (CVPR'2016)
 - [x] ResNeXt (CVPR'2017)
 - [x] [HRNet (CVPR'2019)](configs/hrnet)
 - [x] [ResNeSt (ArXiv'2020)](configs/resnest)
 - [x] [MobileNetV2 (CVPR'2018)](configs/mobilenet_v2)
 - [x] [MobileNetV3 (ICCV'2019)](configs/mobilenet_v3)
@@ -99,15 +114,18 @@
 - [x] [Swin Transformer (ICCV'2021)](configs/swin)
 - [x] [Twins (NeurIPS'2021)](configs/twins)
 - [x] [BEiT (ICLR'2022)](configs/beit)
 - [x] [ConvNeXt (CVPR'2022)](configs/convnext)
 - [x] [MAE (CVPR'2022)](configs/mae)
 - [x] [PoolFormer (CVPR'2022)](configs/poolformer)
 
-Supported methods:
+</details>
+
+<details open>
+<summary>Supported methods:</summary>
 
 - [x] [FCN (CVPR'2015/TPAMI'2017)](configs/fcn)
 - [x] [ERFNet (T-ITS'2017)](configs/erfnet)
 - [x] [UNet (MICCAI'2016/Nat. Methods'2019)](configs/unet)
 - [x] [PSPNet (CVPR'2017)](configs/pspnet)
 - [x] [DeepLabV3 (ArXiv'2017)](configs/deeplabv3)
 - [x] [BiSeNetV1 (ECCV'2018)](configs/bisenetv1)
@@ -138,15 +156,18 @@
 - [x] [DPT (ArXiv'2021)](configs/dpt)
 - [x] [Segmenter (ICCV'2021)](configs/segmenter)
 - [x] [SegFormer (NeurIPS'2021)](configs/segformer)
 - [x] [K-Net (NeurIPS'2021)](configs/knet)
 - [x] [MaskFormer (NeurIPS'2021)](configs/maskformer)
 - [x] [Mask2Former (CVPR'2022)](configs/mask2former)
 
-Supported datasets:
+</details>
+
+<details open>
+<summary>Supported datasets:</summary>
 
 - [x] [Cityscapes](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#cityscapes)
 - [x] [PASCAL VOC](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-voc)
 - [x] [ADE20K](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#ade20k)
 - [x] [Pascal Context](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-context)
 - [x] [COCO-Stuff 10k](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#coco-stuff-10k)
 - [x] [COCO-Stuff 164k](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#coco-stuff-164k)
@@ -157,16 +178,22 @@
 - [x] [Dark Zurich](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#dark-zurich)
 - [x] [Nighttime Driving](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#nighttime-driving)
 - [x] [LoveDA](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#loveda)
 - [x] [Potsdam](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isprs-potsdam)
 - [x] [Vaihingen](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isprs-vaihingen)
 - [x] [iSAID](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isaid)
 
+</details>
+
 Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions.
 
+## Projects
+
+[Here](projects/README.md) are some implementations of SOTA models and solutions built on MMSegmentation, which are supported and maintained by community users. These projects demonstrate the best practices based on MMSegmentation for research and product development. We welcome and appreciate all the contributions to OpenMMLab ecosystem.
+
 ## Contributing
 
 We appreciate all contributions to improve MMSegmentation. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.
 
 ## Acknowledgement
 
 MMSegmentation is an open source project that welcome any contribution and feedback.
@@ -187,15 +214,15 @@
 }
 ```
 
 ## License
 
 This project is released under the [Apache 2.0 license](LICENSE).
 
-## Projects in OpenMMLab
+## OpenMMLab Family
 
 - [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models
 - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
 - [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
 - [MMEval](https://github.com/open-mmlab/mmeval): A unified evaluation library for multiple machine learning libraries.
 - [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
 - [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
```

#### html2text {}

```diff
@@ -1,66 +1,68 @@
                           [resources/mmseg-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
-
-[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/
-mmsegmentation)](https://pypi.org/project/mmsegmentation/) [![PyPI](https://
+       [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/
+ mmsegmentation)](https://pypi.org/project/mmsegmentation/) [![PyPI](https://
 img.shields.io/pypi/v/mmsegmentation)](https://pypi.org/project/mmsegmentation)
-[![docs](https://img.shields.io/badge/docs-latest-blue)](https://
+       [![docs](https://img.shields.io/badge/docs-latest-blue)](https://
 mmsegmentation.readthedocs.io/en/1.x/) [![badge](https://github.com/open-mmlab/
-mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/
-mmsegmentation/actions) [![codecov](https://codecov.io/gh/open-mmlab/
-mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-
-mmlab/mmsegmentation) [![license](https://img.shields.io/github/license/open-
-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/
+   mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/
+     mmsegmentation/actions) [![codecov](https://codecov.io/gh/open-mmlab/
+  mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-
+ mmlab/mmsegmentation) [![license](https://img.shields.io/github/license/open-
+ mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/
 1.x/LICENSE) [![issue resolution](https://isitmaintained.com/badge/resolution/
-open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/
-issues) [![open issues](https://isitmaintained.com/badge/open/open-mmlab/
-mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
-Documentation:
-mmsegmentation.readthedocs.io/en/1.x/> English | [ç®ä½ä¸­æ](README_zh-
-CN.md) ## Introduction MMSegmentation is an open source semantic segmentation
-toolbox based on PyTorch. It is a part of the OpenMMLab project. The 1.x branch
-works with **PyTorch 1.6+**. ![demo image](resources/seg_demo.gif) ### Major
-features - **Unified Benchmark** We provide a unified benchmark toolbox for
-various semantic segmentation methods. - **Modular Design** We decompose the
-semantic segmentation framework into different components and one can easily
-construct a customized semantic segmentation framework by combining different
-modules. - **Support of multiple methods out of box** The toolbox directly
-supports popular and contemporary semantic segmentation frameworks, *e.g.*
-PSPNet, DeepLabV3, PSANet, DeepLabV3+, etc. - **High efficiency** The training
-speed is faster than or comparable to other codebases. ## What's New v1.0.0rc5
-was released on 01/02/2023. Please refer to [changelog.md](docs/en/notes/
-changelog.md) for details and release history. - Support ISNet (ICCV'2021) in
-projects ([#2400](https://github.com/open-mmlab/mmsegmentation/pull/2400)) -
-Support HSSN (CVPR'2022) in projects ([#2444](https://github.com/open-mmlab/
-mmsegmentation/pull/2444)) ## Installation Please refer to [get_started.md]
-(docs/en/get_started.md#installation) for installation and [dataset_prepare.md]
-(docs/en/user_guides/2_dataset_prepare.md#prepare-datasets) for dataset
-preparation. ## Get Started Please see [Overview](docs/en/overview.md) for the
-general introduction of MMSegmentation. Please see [user guides](https://
+ open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/
+   issues) [![open issues](https://isitmaintained.com/badge/open/open-mmlab/
+   mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
+                                Documentation:
+  mmsegmentation.readthedocs.io/en/1.x/> English | [ç®ä½ä¸­æ](README_zh-
+                                    CN.md)
+
+## Introduction MMSegmentation is an open source semantic segmentation toolbox
+based on PyTorch. It is a part of the OpenMMLab project. The 1.x branch works
+with **PyTorch 1.6+**. ![demo image](resources/seg_demo.gif) ### Major features
+- **Unified Benchmark** We provide a unified benchmark toolbox for various
+semantic segmentation methods. - **Modular Design** We decompose the semantic
+segmentation framework into different components and one can easily construct a
+customized semantic segmentation framework by combining different modules. -
+**Support of multiple methods out of box** The toolbox directly supports
+popular and contemporary semantic segmentation frameworks, *e.g.* PSPNet,
+DeepLabV3, PSANet, DeepLabV3+, etc. - **High efficiency** The training speed is
+faster than or comparable to other codebases. ## What's New v1.0.0rc6 was
+released on 03/03/2023. Please refer to [changelog.md](docs/en/notes/
+changelog.md) for details and release history. - Support MMSegInferencer (
+[#2413](https://github.com/open-mmlab/mmsegmentation/pull/2413), [#2658](https:
+//github.com/open-mmlab/mmsegmentation/pull/2658)) - Support REFUGE dataset (
+[#2554](https://github.com/open-mmlab/mmsegmentation/pull/2554)) ##
+Installation Please refer to [get_started.md](docs/en/
+get_started.md#installation) for installation and [dataset_prepare.md](docs/en/
+user_guides/2_dataset_prepare.md#prepare-datasets) for dataset preparation. ##
+Get Started Please see [Overview](docs/en/overview.md) for the general
+introduction of MMSegmentation. Please see [user guides](https://
 mmsegmentation.readthedocs.io/en/1.x/user_guides/index.html#) for the basic
 usage of MMSegmentation. There are also [advanced tutorials](https://
 mmsegmentation.readthedocs.io/en/dev-1.x/advanced_guides/index.html) for in-
 depth understanding of mmseg design and implementation . A Colab tutorial is
 also provided. You may preview the notebook [here](demo/
 MMSegmentation_Tutorial.ipynb) or directly [run](https://
 colab.research.google.com/github/open-mmlab/mmsegmentation/blob/1.x/demo/
 MMSegmentation_Tutorial.ipynb) on Colab. To migrate from MMSegmentation 1.x,
-please refer to [migration](docs/en/migration.md). ## Benchmark and model zoo
+please refer to [migration](docs/en/migration). ## Benchmark and model zoo
 Results and models are available in the [model zoo](docs/en/model_zoo.md).
 Supported backbones: - [x] ResNet (CVPR'2016) - [x] ResNeXt (CVPR'2017) - [x]
 [HRNet (CVPR'2019)](configs/hrnet) - [x] [ResNeSt (ArXiv'2020)](configs/
 resnest) - [x] [MobileNetV2 (CVPR'2018)](configs/mobilenet_v2) - [x]
 [MobileNetV3 (ICCV'2019)](configs/mobilenet_v3) - [x] [Vision Transformer
 (ICLR'2021)](configs/vit) - [x] [Swin Transformer (ICCV'2021)](configs/swin) -
 [x] [Twins (NeurIPS'2021)](configs/twins) - [x] [BEiT (ICLR'2022)](configs/
 beit) - [x] [ConvNeXt (CVPR'2022)](configs/convnext) - [x] [MAE (CVPR'2022)]
-(configs/mae) - [x] [PoolFormer (CVPR'2022)](configs/poolformer) Supported
+(configs/mae) - [x] [PoolFormer (CVPR'2022)](configs/poolformer)   Supported
 methods: - [x] [FCN (CVPR'2015/TPAMI'2017)](configs/fcn) - [x] [ERFNet (T-
 ITS'2017)](configs/erfnet) - [x] [UNet (MICCAI'2016/Nat. Methods'2019)]
 (configs/unet) - [x] [PSPNet (CVPR'2017)](configs/pspnet) - [x] [DeepLabV3
 (ArXiv'2017)](configs/deeplabv3) - [x] [BiSeNetV1 (ECCV'2018)](configs/
 bisenetv1) - [x] [PSANet (ECCV'2018)](configs/psanet) - [x] [DeepLabV3+
 (CVPR'2018)](configs/deeplabv3plus) - [x] [UPerNet (ECCV'2018)](configs/
 upernet) - [x] [ICNet (ECCV'2018)](configs/icnet) - [x] [NonLocal Net
@@ -75,16 +77,16 @@
 (configs/ocrnet) - [x] [DNLNet (ECCV'2020)](configs/dnlnet) - [x] [PointRend
 (CVPR'2020)](configs/point_rend) - [x] [CGNet (TIP'2020)](configs/cgnet) - [x]
 [BiSeNetV2 (IJCV'2021)](configs/bisenetv2) - [x] [STDC (CVPR'2021)](configs/
 stdc) - [x] [SETR (CVPR'2021)](configs/setr) - [x] [DPT (ArXiv'2021)](configs/
 dpt) - [x] [Segmenter (ICCV'2021)](configs/segmenter) - [x] [SegFormer
 (NeurIPS'2021)](configs/segformer) - [x] [K-Net (NeurIPS'2021)](configs/knet) -
 [x] [MaskFormer (NeurIPS'2021)](configs/maskformer) - [x] [Mask2Former
-(CVPR'2022)](configs/mask2former) Supported datasets: - [x] [Cityscapes](https:
-//github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
+(CVPR'2022)](configs/mask2former)   Supported datasets: - [x] [Cityscapes]
+(https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#cityscapes) - [x] [PASCAL VOC](https://github.com/open-
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-
 voc) - [x] [ADE20K](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/
 en/user_guides/2_dataset_prepare.md#ade20k) - [x] [Pascal Context](https://
 github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#pascal-context) - [x] [COCO-Stuff 10k](https://github.com/
 open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
@@ -104,51 +106,56 @@
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#loveda)
 - [x] [Potsdam](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/
 user_guides/2_dataset_prepare.md#isprs-potsdam) - [x] [Vaihingen](https://
 github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#isprs-vaihingen) - [x] [iSAID](https://github.com/open-
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isaid)
 Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions. ##
-Contributing We appreciate all contributions to improve MMSegmentation. Please
-refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing
-guideline. ## Acknowledgement MMSegmentation is an open source project that
-welcome any contribution and feedback. We wish that the toolbox and benchmark
-could serve the growing research community by providing a flexible as well as
-standardized toolkit to reimplement existing methods and develop their own new
-semantic segmentation methods. ## Citation If you find this project useful in
-your research, please consider cite: ```bibtex @misc{mmseg2020, title={
-{MMSegmentation}: OpenMMLab Semantic Segmentation Toolbox and Benchmark},
-author={MMSegmentation Contributors}, howpublished = {\url{https://github.com/
-open-mmlab/mmsegmentation}}, year={2020} } ``` ## License This project is
-released under the [Apache 2.0 license](LICENSE). ## Projects in OpenMMLab -
-[MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational
-library for training deep learning models - [MMCV](https://github.com/open-
-mmlab/mmcv): OpenMMLab foundational library for computer vision. - [MIM](https:
-//github.com/open-mmlab/mim): MIM installs OpenMMLab packages. - [MMEval]
-(https://github.com/open-mmlab/mmeval): A unified evaluation library for
-multiple machine learning libraries. - [MMClassification](https://github.com/
-open-mmlab/mmclassification): OpenMMLab image classification toolbox and
-benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection):
-OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
-github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for
-general 3D object detection. - [MMRotate](https://github.com/open-mmlab/
-mmrotate): OpenMMLab rotated object detection toolbox and benchmark. - [MMYOLO]
-(https://github.com/open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and
-benchmark. - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation):
-OpenMMLab semantic segmentation toolbox and benchmark. - [MMOCR](https://
-github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and
-understanding toolbox. - [MMPose](https://github.com/open-mmlab/mmpose):
-OpenMMLab pose estimation toolbox and benchmark. - [MMHuman3D](https://
-github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox
-and benchmark. - [MMSelfSup](https://github.com/open-mmlab/mmselfsup):
-OpenMMLab self-supervised learning toolbox and benchmark. - [MMRazor](https://
-github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and
-benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab
-fewshot learning toolbox and benchmark. - [MMAction2](https://github.com/open-
-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and
-benchmark. - [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab
-video perception toolbox and benchmark. - [MMFlow](https://github.com/open-
-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark. - [MMEditing]
-(https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing
-toolbox. - [MMGeneration](https://github.com/open-mmlab/mmgeneration):
-OpenMMLab image and video generative models toolbox. - [MMDeploy](https://
-github.com/open-mmlab/mmdeploy): OpenMMLab Model Deployment Framework.
+Projects [Here](projects/README.md) are some implementations of SOTA models and
+solutions built on MMSegmentation, which are supported and maintained by
+community users. These projects demonstrate the best practices based on
+MMSegmentation for research and product development. We welcome and appreciate
+all the contributions to OpenMMLab ecosystem. ## Contributing We appreciate all
+contributions to improve MMSegmentation. Please refer to [CONTRIBUTING.md]
+(.github/CONTRIBUTING.md) for the contributing guideline. ## Acknowledgement
+MMSegmentation is an open source project that welcome any contribution and
+feedback. We wish that the toolbox and benchmark could serve the growing
+research community by providing a flexible as well as standardized toolkit to
+reimplement existing methods and develop their own new semantic segmentation
+methods. ## Citation If you find this project useful in your research, please
+consider cite: ```bibtex @misc{mmseg2020, title={{MMSegmentation}: OpenMMLab
+Semantic Segmentation Toolbox and Benchmark}, author={MMSegmentation
+Contributors}, howpublished = {\url{https://github.com/open-mmlab/
+mmsegmentation}}, year={2020} } ``` ## License This project is released under
+the [Apache 2.0 license](LICENSE). ## OpenMMLab Family - [MMEngine](https://
+github.com/open-mmlab/mmengine): OpenMMLab foundational library for training
+deep learning models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab
+foundational library for computer vision. - [MIM](https://github.com/open-
+mmlab/mim): MIM installs OpenMMLab packages. - [MMEval](https://github.com/
+open-mmlab/mmeval): A unified evaluation library for multiple machine learning
+libraries. - [MMClassification](https://github.com/open-mmlab/
+mmclassification): OpenMMLab image classification toolbox and benchmark. -
+[MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
+toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
+mmdetection3d): OpenMMLab's next-generation platform for general 3D object
+detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
+rotated object detection toolbox and benchmark. - [MMYOLO](https://github.com/
+open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and benchmark. -
+[MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab
+semantic segmentation toolbox and benchmark. - [MMOCR](https://github.com/open-
+mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
+- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation
+toolbox and benchmark. - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d):
+OpenMMLab 3D human parametric model toolbox and benchmark. - [MMSelfSup](https:
+//github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox
+and benchmark. - [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab
+model compression toolbox and benchmark. - [MMFewShot](https://github.com/open-
+mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark. -
+[MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-
+generation action understanding toolbox and benchmark. - [MMTracking](https://
+github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and
+benchmark. - [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical
+flow toolbox and benchmark. - [MMEditing](https://github.com/open-mmlab/
+mmediting): OpenMMLab image and video editing toolbox. - [MMGeneration](https:/
+/github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative
+models toolbox. - [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab
+Model Deployment Framework.
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/ade20k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/chase_db1.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,68 +1,75 @@
 # dataset settings
-dataset_type = 'ADE20KDataset'
-data_root = 'data/ade/ADEChallengeData2016'
-crop_size = (512, 512)
+dataset_type = 'ChaseDB1Dataset'
+data_root = 'data/CHASE_DB1'
+img_scale = (960, 999)
+crop_size = (128, 128)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='LoadAnnotations', reduce_zero_label=True),
+    dict(type='LoadAnnotations'),
     dict(
         type='RandomResize',
-        scale=(2048, 512),
+        scale=img_scale,
         ratio_range=(0.5, 2.0),
         keep_ratio=True),
     dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
     dict(type='RandomFlip', prob=0.5),
     dict(type='PhotoMetricDistortion'),
     dict(type='PackSegInputs')
 ]
 test_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='Resize', scale=(2048, 512), keep_ratio=True),
+    dict(type='Resize', scale=img_scale, keep_ratio=True),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
-    dict(type='LoadAnnotations', reduce_zero_label=True),
+    dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
             [
                 dict(type='RandomFlip', prob=0., direction='horizontal'),
                 dict(type='RandomFlip', prob=1., direction='horizontal')
             ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
         ])
 ]
+
 train_dataloader = dict(
     batch_size=4,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
     dataset=dict(
-        type=dataset_type,
-        data_root=data_root,
-        data_prefix=dict(
-            img_path='images/training', seg_map_path='annotations/training'),
-        pipeline=train_pipeline))
+        type='RepeatDataset',
+        times=40000,
+        dataset=dict(
+            type=dataset_type,
+            data_root=data_root,
+            data_prefix=dict(
+                img_path='images/training',
+                seg_map_path='annotations/training'),
+            pipeline=train_pipeline)))
+
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
         data_root=data_root,
         data_prefix=dict(
             img_path='images/validation',
             seg_map_path='annotations/validation'),
         pipeline=test_pipeline))
 test_dataloader = val_dataloader
 
-val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
+val_evaluator = dict(type='IoUMetric', iou_metrics=['mDice'])
 test_evaluator = val_evaluator
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/ade20k_640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/ade20k_640x640.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/chase_db1.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/drive.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # dataset settings
-dataset_type = 'ChaseDB1Dataset'
-data_root = 'data/CHASE_DB1'
-img_scale = (960, 999)
-crop_size = (128, 128)
+dataset_type = 'DRIVEDataset'
+data_root = 'data/DRIVE'
+img_scale = (584, 565)
+crop_size = (64, 64)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations'),
     dict(
         type='RandomResize',
         scale=img_scale,
         ratio_range=(0.5, 2.0),
@@ -22,29 +22,28 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
             [
                 dict(type='RandomFlip', prob=0., direction='horizontal'),
                 dict(type='RandomFlip', prob=1., direction='horizontal')
             ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
         ])
 ]
-
 train_dataloader = dict(
     batch_size=4,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
     dataset=dict(
         type='RepeatDataset',
@@ -52,15 +51,14 @@
         dataset=dict(
             type=dataset_type,
             data_root=data_root,
             data_prefix=dict(
                 img_path='images/training',
                 seg_map_path='annotations/training'),
             pipeline=train_pipeline)))
-
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/hrf.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,67 +1,73 @@
 # dataset settings
-dataset_type = 'CityscapesDataset'
-data_root = 'data/cityscapes/'
-crop_size = (512, 1024)
+dataset_type = 'HRFDataset'
+data_root = 'data/HRF'
+img_scale = (2336, 3504)
+crop_size = (256, 256)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations'),
     dict(
         type='RandomResize',
-        scale=(2048, 1024),
+        scale=img_scale,
         ratio_range=(0.5, 2.0),
         keep_ratio=True),
     dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
     dict(type='RandomFlip', prob=0.5),
     dict(type='PhotoMetricDistortion'),
     dict(type='PackSegInputs')
 ]
 test_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='Resize', scale=(2048, 1024), keep_ratio=True),
+    dict(type='Resize', scale=img_scale, keep_ratio=True),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
             [
                 dict(type='RandomFlip', prob=0., direction='horizontal'),
                 dict(type='RandomFlip', prob=1., direction='horizontal')
             ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
         ])
 ]
 train_dataloader = dict(
-    batch_size=2,
-    num_workers=2,
+    batch_size=4,
+    num_workers=4,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
     dataset=dict(
-        type=dataset_type,
-        data_root=data_root,
-        data_prefix=dict(
-            img_path='leftImg8bit/train', seg_map_path='gtFine/train'),
-        pipeline=train_pipeline))
+        type='RepeatDataset',
+        times=40000,
+        dataset=dict(
+            type=dataset_type,
+            data_root=data_root,
+            data_prefix=dict(
+                img_path='images/training',
+                seg_map_path='annotations/training'),
+            pipeline=train_pipeline)))
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
         data_root=data_root,
         data_prefix=dict(
-            img_path='leftImg8bit/val', seg_map_path='gtFine/val'),
+            img_path='images/validation',
+            seg_map_path='annotations/validation'),
         pipeline=test_pipeline))
 test_dataloader = val_dataloader
 
-val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
+val_evaluator = dict(type='IoUMetric', iou_metrics=['mDice'])
 test_evaluator = val_evaluator
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_768x768.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_768x768.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_769x769.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_769x769.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/cityscapes_832x832.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes_832x832.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/coco-stuff10k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/coco-stuff10k.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/coco-stuff164k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/coco-stuff164k.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/drive.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/stare.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # dataset settings
-dataset_type = 'DRIVEDataset'
-data_root = 'data/DRIVE'
-img_scale = (584, 565)
-crop_size = (64, 64)
+dataset_type = 'STAREDataset'
+data_root = 'data/STARE'
+img_scale = (605, 700)
+crop_size = (128, 128)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations'),
     dict(
         type='RandomResize',
         scale=img_scale,
         ratio_range=(0.5, 2.0),
@@ -22,15 +22,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/hrf.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/cityscapes.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,73 +1,67 @@
 # dataset settings
-dataset_type = 'HRFDataset'
-data_root = 'data/HRF'
-img_scale = (2336, 3504)
-crop_size = (256, 256)
+dataset_type = 'CityscapesDataset'
+data_root = 'data/cityscapes/'
+crop_size = (512, 1024)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations'),
     dict(
         type='RandomResize',
-        scale=img_scale,
+        scale=(2048, 1024),
         ratio_range=(0.5, 2.0),
         keep_ratio=True),
     dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
     dict(type='RandomFlip', prob=0.5),
     dict(type='PhotoMetricDistortion'),
     dict(type='PackSegInputs')
 ]
 test_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='Resize', scale=img_scale, keep_ratio=True),
+    dict(type='Resize', scale=(2048, 1024), keep_ratio=True),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
             [
                 dict(type='RandomFlip', prob=0., direction='horizontal'),
                 dict(type='RandomFlip', prob=1., direction='horizontal')
             ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
         ])
 ]
 train_dataloader = dict(
-    batch_size=4,
-    num_workers=4,
+    batch_size=2,
+    num_workers=2,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
     dataset=dict(
-        type='RepeatDataset',
-        times=40000,
-        dataset=dict(
-            type=dataset_type,
-            data_root=data_root,
-            data_prefix=dict(
-                img_path='images/training',
-                seg_map_path='annotations/training'),
-            pipeline=train_pipeline)))
+        type=dataset_type,
+        data_root=data_root,
+        data_prefix=dict(
+            img_path='leftImg8bit/train', seg_map_path='gtFine/train'),
+        pipeline=train_pipeline))
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
         data_root=data_root,
         data_prefix=dict(
-            img_path='images/validation',
-            seg_map_path='annotations/validation'),
+            img_path='leftImg8bit/val', seg_map_path='gtFine/val'),
         pipeline=test_pipeline))
 test_dataloader = val_dataloader
 
-val_evaluator = dict(type='IoUMetric', iou_metrics=['mDice'])
+val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
 test_evaluator = val_evaluator
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/isaid.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/isaid.py`

 * *Files 2% similar despite different names*

```diff
@@ -28,15 +28,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/loveda.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/loveda.py`

 * *Files 6% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_context.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_context.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_context_59.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_context_59.py`

 * *Files 12% similar despite different names*

```diff
@@ -24,15 +24,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_voc12.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_voc12_aug.py`

 * *Files 5% similar despite different names*

```diff
@@ -9,52 +9,64 @@
         type='RandomResize',
         scale=(2048, 512),
         ratio_range=(0.5, 2.0),
         keep_ratio=True),
     dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
     dict(type='RandomFlip', prob=0.5),
     dict(type='PhotoMetricDistortion'),
+    dict(type='Pad', size=crop_size),
     dict(type='PackSegInputs')
 ]
+
 test_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='Resize', scale=(2048, 512), keep_ratio=True),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
             [
                 dict(type='RandomFlip', prob=0., direction='horizontal'),
                 dict(type='RandomFlip', prob=1., direction='horizontal')
             ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
         ])
 ]
+dataset_train = dict(
+    type=dataset_type,
+    data_root=data_root,
+    data_prefix=dict(img_path='JPEGImages', seg_map_path='SegmentationClass'),
+    ann_file='ImageSets/Segmentation/train.txt',
+    pipeline=train_pipeline)
+
+dataset_aug = dict(
+    type=dataset_type,
+    data_root=data_root,
+    data_prefix=dict(
+        img_path='JPEGImages', seg_map_path='SegmentationClassAug'),
+    ann_file='ImageSets/Segmentation/aug.txt',
+    pipeline=train_pipeline)
+
 train_dataloader = dict(
     batch_size=4,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
-    dataset=dict(
-        type=dataset_type,
-        data_root=data_root,
-        data_prefix=dict(
-            img_path='JPEGImages', seg_map_path='SegmentationClass'),
-        ann_file='ImageSets/Segmentation/train.txt',
-        pipeline=train_pipeline))
+    dataset=dict(type='ConcatDataset', datasets=[dataset_train, dataset_aug]))
+
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/pascal_voc12_aug.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/refuge.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,32 +1,42 @@
 # dataset settings
-dataset_type = 'PascalVOCDataset'
-data_root = 'data/VOCdevkit/VOC2012'
+dataset_type = 'REFUGEDataset'
+data_root = 'data/REFUGE'
+train_img_scale = (2056, 2124)
+val_img_scale = (1634, 1634)
+test_img_scale = (1634, 1634)
 crop_size = (512, 512)
+
 train_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='LoadAnnotations'),
+    dict(type='LoadAnnotations', reduce_zero_label=False),
     dict(
         type='RandomResize',
-        scale=(2048, 512),
+        scale=train_img_scale,
         ratio_range=(0.5, 2.0),
         keep_ratio=True),
     dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
     dict(type='RandomFlip', prob=0.5),
     dict(type='PhotoMetricDistortion'),
-    dict(type='Pad', size=crop_size),
     dict(type='PackSegInputs')
 ]
-
+val_pipeline = [
+    dict(type='LoadImageFromFile'),
+    dict(type='Resize', scale=val_img_scale, keep_ratio=True),
+    # add loading annotation after ``Resize`` because ground truth
+    # does not need to do resize data transform
+    dict(type='LoadAnnotations', reduce_zero_label=False),
+    dict(type='PackSegInputs')
+]
 test_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='Resize', scale=(2048, 512), keep_ratio=True),
+    dict(type='Resize', scale=test_img_scale, keep_ratio=True),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
-    dict(type='LoadAnnotations'),
+    dict(type='LoadAnnotations', reduce_zero_label=False),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
     dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
     dict(
         type='TestTimeAug',
@@ -37,45 +47,44 @@
             ],
             [
                 dict(type='RandomFlip', prob=0., direction='horizontal'),
                 dict(type='RandomFlip', prob=1., direction='horizontal')
             ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
         ])
 ]
-dataset_train = dict(
-    type=dataset_type,
-    data_root=data_root,
-    data_prefix=dict(img_path='JPEGImages', seg_map_path='SegmentationClass'),
-    ann_file='ImageSets/Segmentation/train.txt',
-    pipeline=train_pipeline)
-
-dataset_aug = dict(
-    type=dataset_type,
-    data_root=data_root,
-    data_prefix=dict(
-        img_path='JPEGImages', seg_map_path='SegmentationClassAug'),
-    ann_file='ImageSets/Segmentation/aug.txt',
-    pipeline=train_pipeline)
-
 train_dataloader = dict(
     batch_size=4,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
-    dataset=dict(type='ConcatDataset', datasets=[dataset_train, dataset_aug]))
-
+    dataset=dict(
+        type=dataset_type,
+        data_root=data_root,
+        data_prefix=dict(
+            img_path='images/training', seg_map_path='annotations/training'),
+        pipeline=train_pipeline))
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
         data_root=data_root,
         data_prefix=dict(
-            img_path='JPEGImages', seg_map_path='SegmentationClass'),
-        ann_file='ImageSets/Segmentation/val.txt',
-        pipeline=test_pipeline))
-test_dataloader = val_dataloader
+            img_path='images/validation',
+            seg_map_path='annotations/validation'),
+        pipeline=val_pipeline))
+test_dataloader = dict(
+    batch_size=1,
+    num_workers=4,
+    persistent_workers=True,
+    sampler=dict(type='DefaultSampler', shuffle=False),
+    dataset=dict(
+        type=dataset_type,
+        data_root=data_root,
+        data_prefix=dict(
+            img_path='images/test', seg_map_path='annotations/test'),
+        pipeline=val_pipeline))
 
-val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
+val_evaluator = dict(type='IoUMetric', iou_metrics=['mDice'])
 test_evaluator = val_evaluator
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/potsdam.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/vaihingen.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # dataset settings
-dataset_type = 'PotsdamDataset'
-data_root = 'data/potsdam'
+dataset_type = 'ISPRSDataset'
+data_root = 'data/vaihingen'
 crop_size = (512, 512)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(
         type='RandomResize',
         scale=(512, 512),
@@ -21,15 +21,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/stare.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/pascal_voc12.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,36 +1,35 @@
 # dataset settings
-dataset_type = 'STAREDataset'
-data_root = 'data/STARE'
-img_scale = (605, 700)
-crop_size = (128, 128)
+dataset_type = 'PascalVOCDataset'
+data_root = 'data/VOCdevkit/VOC2012'
+crop_size = (512, 512)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations'),
     dict(
         type='RandomResize',
-        scale=img_scale,
+        scale=(2048, 512),
         ratio_range=(0.5, 2.0),
         keep_ratio=True),
     dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
     dict(type='RandomFlip', prob=0.5),
     dict(type='PhotoMetricDistortion'),
     dict(type='PackSegInputs')
 ]
 test_pipeline = [
     dict(type='LoadImageFromFile'),
-    dict(type='Resize', scale=img_scale, keep_ratio=True),
+    dict(type='Resize', scale=(2048, 512), keep_ratio=True),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations'),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
@@ -42,32 +41,29 @@
 ]
 train_dataloader = dict(
     batch_size=4,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='InfiniteSampler', shuffle=True),
     dataset=dict(
-        type='RepeatDataset',
-        times=40000,
-        dataset=dict(
-            type=dataset_type,
-            data_root=data_root,
-            data_prefix=dict(
-                img_path='images/training',
-                seg_map_path='annotations/training'),
-            pipeline=train_pipeline)))
+        type=dataset_type,
+        data_root=data_root,
+        data_prefix=dict(
+            img_path='JPEGImages', seg_map_path='SegmentationClass'),
+        ann_file='ImageSets/Segmentation/train.txt',
+        pipeline=train_pipeline))
 val_dataloader = dict(
     batch_size=1,
     num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type=dataset_type,
         data_root=data_root,
         data_prefix=dict(
-            img_path='images/validation',
-            seg_map_path='annotations/validation'),
+            img_path='JPEGImages', seg_map_path='SegmentationClass'),
+        ann_file='ImageSets/Segmentation/val.txt',
         pipeline=test_pipeline))
 test_dataloader = val_dataloader
 
-val_evaluator = dict(type='IoUMetric', iou_metrics=['mDice'])
+val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
 test_evaluator = val_evaluator
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/synapse.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/synapse.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/datasets/vaihingen.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/potsdam.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # dataset settings
-dataset_type = 'ISPRSDataset'
-data_root = 'data/vaihingen'
+dataset_type = 'PotsdamDataset'
+data_root = 'data/potsdam'
 crop_size = (512, 512)
 train_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(
         type='RandomResize',
         scale=(512, 512),
@@ -21,15 +21,15 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadAnnotations', reduce_zero_label=True),
     dict(type='PackSegInputs')
 ]
 img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
 tta_pipeline = [
-    dict(type='LoadImageFromFile', backend_args=dict(backend='local')),
+    dict(type='LoadImageFromFile', backend_args=None),
     dict(
         type='TestTimeAug',
         transforms=[
             [
                 dict(type='Resize', scale_factor=r, keep_ratio=True)
                 for r in img_ratios
             ],
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ann_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ann_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/apcnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/apcnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/bisenetv1_r18-d32.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/bisenetv1_r18-d32.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/bisenetv2.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/bisenetv2.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ccnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ccnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/cgnet.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/cgnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/danet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/danet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/deeplabv3_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/deeplabv3_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/deeplabv3_unet_s5-d16.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/deeplabv3_unet_s5-d16.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/deeplabv3plus_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/deeplabv3plus_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/dmnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/dmnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/dnl_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/dnl_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/dpt_vit-b16.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/dpt_vit-b16.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/emanet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/emanet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/encnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/encnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/erfnet_fcn.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/erfnet_fcn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fast_scnn.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fast_scnn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fastfcn_r50-d32_jpu_psp.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fastfcn_r50-d32_jpu_psp.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fcn_hr18.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fcn_hr18.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fcn_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fcn_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fcn_unet_s5-d16.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fcn_unet_s5-d16.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fpn_poolformer_s12.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/fpn_r50.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,37 +1,31 @@
 # model settings
 norm_cfg = dict(type='SyncBN', requires_grad=True)
-checkpoint_file = 'https://download.openmmlab.com/mmclassification/v0/poolformer/poolformer-s12_3rdparty_32xb128_in1k_20220414-f8d83051.pth'  # noqa
-custom_imports = dict(imports='mmcls.models', allow_failed_imports=False)
 data_preprocessor = dict(
     type='SegDataPreProcessor',
     mean=[123.675, 116.28, 103.53],
     std=[58.395, 57.12, 57.375],
     bgr_to_rgb=True,
     pad_val=0,
     seg_pad_val=255)
 model = dict(
     type='EncoderDecoder',
     data_preprocessor=data_preprocessor,
+    pretrained='open-mmlab://resnet50_v1c',
     backbone=dict(
-        type='mmcls.PoolFormer',
-        arch='s12',
-        init_cfg=dict(
-            type='Pretrained', checkpoint=checkpoint_file, prefix='backbone.'),
-        in_patch_size=7,
-        in_stride=4,
-        in_pad=2,
-        down_patch_size=3,
-        down_stride=2,
-        down_pad=1,
-        drop_rate=0.,
-        drop_path_rate=0.,
-        out_indices=(0, 2, 4, 6),
-        frozen_stages=0,
-    ),
+        type='ResNetV1c',
+        depth=50,
+        num_stages=4,
+        out_indices=(0, 1, 2, 3),
+        dilations=(1, 1, 1, 1),
+        strides=(1, 2, 2, 2),
+        norm_cfg=norm_cfg,
+        norm_eval=False,
+        style='pytorch',
+        contract_dilation=True),
     neck=dict(
         type='FPN',
         in_channels=[256, 512, 1024, 2048],
         out_channels=256,
         num_outs=4),
     decode_head=dict(
         type='FPNHead',
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/fpn_r50.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_swin.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,44 +1,62 @@
 # model settings
 norm_cfg = dict(type='SyncBN', requires_grad=True)
+backbone_norm_cfg = dict(type='LN', requires_grad=True)
 data_preprocessor = dict(
     type='SegDataPreProcessor',
     mean=[123.675, 116.28, 103.53],
     std=[58.395, 57.12, 57.375],
     bgr_to_rgb=True,
     pad_val=0,
     seg_pad_val=255)
 model = dict(
     type='EncoderDecoder',
     data_preprocessor=data_preprocessor,
-    pretrained='open-mmlab://resnet50_v1c',
+    pretrained=None,
     backbone=dict(
-        type='ResNetV1c',
-        depth=50,
-        num_stages=4,
+        type='SwinTransformer',
+        pretrain_img_size=224,
+        embed_dims=96,
+        patch_size=4,
+        window_size=7,
+        mlp_ratio=4,
+        depths=[2, 2, 6, 2],
+        num_heads=[3, 6, 12, 24],
+        strides=(4, 2, 2, 2),
         out_indices=(0, 1, 2, 3),
-        dilations=(1, 1, 1, 1),
-        strides=(1, 2, 2, 2),
-        norm_cfg=norm_cfg,
-        norm_eval=False,
-        style='pytorch',
-        contract_dilation=True),
-    neck=dict(
-        type='FPN',
-        in_channels=[256, 512, 1024, 2048],
-        out_channels=256,
-        num_outs=4),
+        qkv_bias=True,
+        qk_scale=None,
+        patch_norm=True,
+        drop_rate=0.,
+        attn_drop_rate=0.,
+        drop_path_rate=0.3,
+        use_abs_pos_embed=False,
+        act_cfg=dict(type='GELU'),
+        norm_cfg=backbone_norm_cfg),
     decode_head=dict(
-        type='FPNHead',
-        in_channels=[256, 256, 256, 256],
+        type='UPerHead',
+        in_channels=[96, 192, 384, 768],
         in_index=[0, 1, 2, 3],
-        feature_strides=[4, 8, 16, 32],
-        channels=128,
+        pool_scales=(1, 2, 3, 6),
+        channels=512,
         dropout_ratio=0.1,
         num_classes=19,
         norm_cfg=norm_cfg,
         align_corners=False,
         loss_decode=dict(
             type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
+    auxiliary_head=dict(
+        type='FCNHead',
+        in_channels=384,
+        in_index=2,
+        channels=256,
+        num_convs=1,
+        concat_input=False,
+        dropout_ratio=0.1,
+        num_classes=19,
+        norm_cfg=norm_cfg,
+        align_corners=False,
+        loss_decode=dict(
+            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
     # model training and testing settings
     train_cfg=dict(),
     test_cfg=dict(mode='whole'))
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/gcnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/gcnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/icnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/icnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/isanet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/isanet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/lraspp_m-v3-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/lraspp_m-v3-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/nonlocal_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/nonlocal_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ocrnet_hr18.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ocrnet_hr18.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/ocrnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/ocrnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/pointrend_r50.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/pointrend_r50.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/psanet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/psanet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/pspnet_r50-d8.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/pspnet_r50-d8.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/pspnet_unet_s5-d16.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/pspnet_unet_s5-d16.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/segformer_mit-b0.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/segformer_mit-b0.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/segmenter_vit-b16_mask.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/segmenter_vit-b16_mask.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/setr_mla.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/setr_mla.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/setr_naive.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/setr_naive.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/setr_pup.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/setr_pup.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/stdc.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/stdc.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_fpn.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_fpn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_upernet.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/twins_pcpvt-s_upernet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_beit.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_beit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_convnext.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_convnext.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_mae.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_mae.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_r50.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_r50.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_swin.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-160k_cityscapes-512x1024.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,62 +1,39 @@
-# model settings
+_base_ = './ocrnet_hr18_4xb2-160k_cityscapes-512x1024.py'
 norm_cfg = dict(type='SyncBN', requires_grad=True)
-backbone_norm_cfg = dict(type='LN', requires_grad=True)
-data_preprocessor = dict(
-    type='SegDataPreProcessor',
-    mean=[123.675, 116.28, 103.53],
-    std=[58.395, 57.12, 57.375],
-    bgr_to_rgb=True,
-    pad_val=0,
-    seg_pad_val=255)
 model = dict(
-    type='EncoderDecoder',
-    data_preprocessor=data_preprocessor,
-    pretrained=None,
+    pretrained='open-mmlab://msra/hrnetv2_w48',
     backbone=dict(
-        type='SwinTransformer',
-        pretrain_img_size=224,
-        embed_dims=96,
-        patch_size=4,
-        window_size=7,
-        mlp_ratio=4,
-        depths=[2, 2, 6, 2],
-        num_heads=[3, 6, 12, 24],
-        strides=(4, 2, 2, 2),
-        out_indices=(0, 1, 2, 3),
-        qkv_bias=True,
-        qk_scale=None,
-        patch_norm=True,
-        drop_rate=0.,
-        attn_drop_rate=0.,
-        drop_path_rate=0.3,
-        use_abs_pos_embed=False,
-        act_cfg=dict(type='GELU'),
-        norm_cfg=backbone_norm_cfg),
-    decode_head=dict(
-        type='UPerHead',
-        in_channels=[96, 192, 384, 768],
-        in_index=[0, 1, 2, 3],
-        pool_scales=(1, 2, 3, 6),
-        channels=512,
-        dropout_ratio=0.1,
-        num_classes=19,
-        norm_cfg=norm_cfg,
-        align_corners=False,
-        loss_decode=dict(
-            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0)),
-    auxiliary_head=dict(
-        type='FCNHead',
-        in_channels=384,
-        in_index=2,
-        channels=256,
-        num_convs=1,
-        concat_input=False,
-        dropout_ratio=0.1,
-        num_classes=19,
-        norm_cfg=norm_cfg,
-        align_corners=False,
-        loss_decode=dict(
-            type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
-    # model training and testing settings
-    train_cfg=dict(),
-    test_cfg=dict(mode='whole'))
+        extra=dict(
+            stage2=dict(num_channels=(48, 96)),
+            stage3=dict(num_channels=(48, 96, 192)),
+            stage4=dict(num_channels=(48, 96, 192, 384)))),
+    decode_head=[
+        dict(
+            type='FCNHead',
+            in_channels=[48, 96, 192, 384],
+            channels=sum([48, 96, 192, 384]),
+            input_transform='resize_concat',
+            in_index=(0, 1, 2, 3),
+            kernel_size=1,
+            num_convs=1,
+            norm_cfg=norm_cfg,
+            concat_input=False,
+            dropout_ratio=-1,
+            num_classes=19,
+            align_corners=False,
+            loss_decode=dict(
+                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
+        dict(
+            type='OCRHead',
+            in_channels=[48, 96, 192, 384],
+            channels=512,
+            ocr_channels=256,
+            input_transform='resize_concat',
+            in_index=(0, 1, 2, 3),
+            norm_cfg=norm_cfg,
+            dropout_ratio=-1,
+            num_classes=19,
+            align_corners=False,
+            loss_decode=dict(
+                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
+    ])
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/models/upernet_vit-b16_ln_mln.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/models/upernet_vit-b16_ln_mln.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_160k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_160k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_20k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_20k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_320k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_320k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_40k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_40k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/_base_/schedules/schedule_80k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/schedules/schedule_80k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ann/ann.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ann/ann.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/apcnet/apcnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/apcnet/apcnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640_ms.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-base_upernet_8xb2-160k_ade20k-640x640_ms.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640_ms.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit-large_upernet_8xb1-amp-160k_ade20k-640x640_ms.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/beit/beit.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/beit/beit.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r101-d32_4xb4-160k_coco-stuff164k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r101-d32_4xb4-160k_coco-stuff164k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb4-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32-in1k-pre_4xb4-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_coco-stuff164k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r18-d32_4xb4-160k_coco-stuff164k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_coco-stuff164k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv1/bisenetv1_r50-d32_4xb4-160k_coco-stuff164k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-ohem-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb4-ohem-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb8-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/bisenetv2/bisenetv2_fcn_4xb8-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ccnet/ccnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ccnet/ccnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/cgnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/cgnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb4-60k_cityscapes-680x680.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb4-60k_cityscapes-680x680.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb8-60k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/cgnet/cgnet_fcn_4xb8-60k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-base_upernet_8xb2-amp-160k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-large_upernet_8xb2-amp-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-large_upernet_8xb2-amp-160k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-small_upernet_8xb2-amp-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-small_upernet_8xb2-amp-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-tiny_upernet_8xb2-amp-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-tiny_upernet_8xb2-amp-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext-xlarge_upernet_8xb2-amp-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext-xlarge_upernet_8xb2-amp-160k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/convnext/convnext.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/convnext/convnext.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/danet/danet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/danet/danet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-40k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3/deeplabv3_r50-d8_4xb4-80k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-40k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/deeplabv3plus/deeplabv3plus_r50-d8_4xb4-80k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dmnet/dmnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dmnet/dmnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-80k_cityscapes-769x769.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnl_r50-d8_4xb2-80k_cityscapes-769x769.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dnlnet/dnlnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dnlnet/dnlnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dpt/dpt.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dpt/dpt.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/dpt/dpt_vit-b16_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/dpt/dpt_vit-b16_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/emanet/emanet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/emanet/emanet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/encnet/encnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/encnet/encnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/erfnet/erfnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/erfnet/erfnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb2-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb2-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_aspp_4xb4-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb2-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb2-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastfcn/fastfcn_r50-d32_jpu_enc_4xb4-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastscnn/fast_scnn_8xb4-160k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastscnn/fast_scnn_8xb4-160k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fastscnn/fastscnn.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fastscnn/fastscnn.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-40k_cityscapes-769x769.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-40k_cityscapes-769x769.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-80k_cityscapes-769x769.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn-d6_r50-d16_4xb2-80k_cityscapes-769x769.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-40k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/fcn/fcn_r50-d8_4xb4-80k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/gcnet/gcnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/gcnet/gcnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-40k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/fcn_hr18_4xb4-80k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/hrnet/hrnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/hrnet/hrnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/icnet/icnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/icnet/icnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/isanet/isanet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/isanet/isanet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_deeplabv3_8xb2-adamw-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_deeplabv3_8xb2-adamw-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_fcn_8xb2-adamw-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_fcn_8xb2-adamw-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_pspnet_8xb2-adamw-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_pspnet_8xb2-adamw-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_r50-d8_upernet_8xb2-adamw-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_r50-d8_upernet_8xb2-adamw-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_swin-l_upernet_8xb2-adamw-80k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet-s3_swin-t_upernet_8xb2-adamw-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet-s3_swin-t_upernet_8xb2-adamw-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/knet/knet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/knet/knet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512-ms.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512-ms.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/mae-base_upernet_8xb2-amp-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mae/mae.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mae/mae.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-90k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_r50_8xb2-90k_cityscapes-512x1024.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
 _base_ = ['../_base_/default_runtime.py', '../_base_/datasets/cityscapes.py']
 
-custom_imports = dict(imports='mmdet.models', allow_failed_imports=False)
-
 crop_size = (512, 1024)
 data_preprocessor = dict(
     type='SegDataPreProcessor',
     mean=[123.675, 116.28, 103.53],
     std=[58.395, 57.12, 57.375],
     bgr_to_rgb=True,
     pad_val=0,
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-b-in1k-384x384-pre_8xb2-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-b-in1k-384x384-pre_8xb2-160k_ade20k-640x640.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 _base_ = [
     '../_base_/default_runtime.py', '../_base_/datasets/ade20k_640x640.py'
 ]
 
 pretrained = 'https://download.openmmlab.com/mmsegmentation/v0.5/pretrain/swin/swin_base_patch4_window12_384_20220317-55b0104a.pth'  # noqa
-custom_imports = dict(imports='mmdet.models', allow_failed_imports=False)
 
 crop_size = (640, 640)
 data_preprocessor = dict(
     type='SegDataPreProcessor',
     mean=[123.675, 116.28, 103.53],
     std=[58.395, 57.12, 57.375],
     bgr_to_rgb=True,
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-b-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-l-in22k-384x384-pre_8xb2-90k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-90k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-s_8xb2-90k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-90k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mask2former/mask2former_swin-t_8xb2-90k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_r50-d32_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_r50-d32_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_swin-s_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_swin-s_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/maskformer/maskformer_swin-t_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/maskformer/maskformer_swin-t_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v2/mobilenet_v2.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v2/mobilenet_v2.yml`

 * *Files 7% similar despite different names*

```diff
@@ -13,17 +13,18 @@
       mode: FP32
       resolution: (512,1024)
     Training Memory (GB): 3.4
   Results:
   - Task: Semantic Segmentation
     Dataset: Cityscapes
     Metrics:
-      mIoU: 61.54
+      mIoU: 71.19
+      mIoU(ms+flip): 73.34
   Config: configs/mobilenet_v2/mobilenet-v2-d8_fcn_4xb2-80k_cityscapes-512x1024.py
-  Weights: https://download.openmmlab.com/mmsegmentation/v0.5/mobilenet_v2/fcn_m-v2-d8_512x1024_80k_cityscapes/fcn_m-v2-d8_512x1024_80k_cityscapes_20200825_124817-d24c28c1.pth
+  Weights: https://download.openmmlab.com/mmsegmentation/v0.5/mobilenet_v2/mobilenet-v2-d8_fcn_4xb2-80k_cityscapes-512x1024/mobilenet-v2-d8_fcn_4xb2-80k_cityscapes-512x1024-20230224_185436-13fef4ea.pth
 - Name: mobilenet-v2-d8_pspnet_4xb2-80k_cityscapes-512x1024
   In Collection: PSPNet
   Metadata:
     backbone: M-V2-D8
     crop size: (512,1024)
     lr schd: 80000
     inference time (ms/im):
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-s_lraspp_4xb4-320k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-s_lraspp_4xb4-320k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-scratch-s_lraspp_4xb4-320k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8-scratch-s_lraspp_4xb4-320k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8_lraspp_4xb4-320k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet-v3-d8_lraspp_4xb4-320k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/mobilenet_v3/mobilenet_v3.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/mobilenet_v3/mobilenet_v3.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/nonlocal_net/nonlocal_net.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/nonlocal_net/nonlocal_net.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet.yml`

 * *Files 1% similar despite different names*

```diff
@@ -29,18 +29,18 @@
       mode: FP32
       resolution: (512,1024)
     Training Memory (GB): 3.5
   Results:
   - Task: Semantic Segmentation
     Dataset: Cityscapes
     Metrics:
-      mIoU: 74.3
-      mIoU(ms+flip): 75.95
+      mIoU: 76.61
+      mIoU(ms+flip): 78.01
   Config: configs/ocrnet/ocrnet_hr18s_4xb2-40k_cityscapes-512x1024.py
-  Weights: https://download.openmmlab.com/mmsegmentation/v0.5/ocrnet/ocrnet_hr18s_512x1024_40k_cityscapes/ocrnet_hr18s_512x1024_40k_cityscapes_20200601_033304-fa2436c2.pth
+  Weights: https://download.openmmlab.com/mmsegmentation/v0.5/ocrnet/ocrnet_hr18s_4xb2-40k_cityscapes-512x1024/ocrnet_hr18s_4xb2-40k_cityscapes-512x1024_20230227_145026-6c052a14.pth
 - Name: ocrnet_hr18_4xb2-40k_cityscapes-512x1024
   In Collection: OCRNet
   Metadata:
     backbone: HRNetV2p-W18
     crop size: (512,1024)
     lr schd: 40000
     inference time (ms/im):
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-20k_voc12aug-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-20k_voc12aug-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-40k_voc12aug-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-40k_voc12aug-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr18_4xb4-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-160k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-80k_cityscapes-512x1024.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-_base_ = './ocrnet_hr18_4xb2-160k_cityscapes-512x1024.py'
+_base_ = './ocrnet_hr18_4xb2-80k_cityscapes-512x1024.py'
 norm_cfg = dict(type='SyncBN', requires_grad=True)
 model = dict(
     pretrained='open-mmlab://msra/hrnetv2_w48',
     backbone=dict(
         extra=dict(
             stage2=dict(num_channels=(48, 96)),
             stage3=dict(num_channels=(48, 96, 192)),
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-40k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-40k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb2-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-160k_ade20k-512x512.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-_base_ = './ocrnet_hr18_4xb2-80k_cityscapes-512x1024.py'
+_base_ = './ocrnet_hr18_4xb4-160k_ade20k-512x512.py'
 norm_cfg = dict(type='SyncBN', requires_grad=True)
 model = dict(
     pretrained='open-mmlab://msra/hrnetv2_w48',
     backbone=dict(
         extra=dict(
             stage2=dict(num_channels=(48, 96)),
             stage3=dict(num_channels=(48, 96, 192)),
@@ -15,25 +15,25 @@
             input_transform='resize_concat',
             in_index=(0, 1, 2, 3),
             kernel_size=1,
             num_convs=1,
             norm_cfg=norm_cfg,
             concat_input=False,
             dropout_ratio=-1,
-            num_classes=19,
+            num_classes=150,
             align_corners=False,
             loss_decode=dict(
                 type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
         dict(
             type='OCRHead',
             in_channels=[48, 96, 192, 384],
             channels=512,
             ocr_channels=256,
             input_transform='resize_concat',
             in_index=(0, 1, 2, 3),
             norm_cfg=norm_cfg,
             dropout_ratio=-1,
-            num_classes=19,
+            num_classes=150,
             align_corners=False,
             loss_decode=dict(
                 type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
     ])
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-80k_ade20k-512x512.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-_base_ = './ocrnet_hr18_4xb4-160k_ade20k-512x512.py'
+_base_ = './ocrnet_hr18_4xb4-80k_ade20k-512x512.py'
 norm_cfg = dict(type='SyncBN', requires_grad=True)
 model = dict(
     pretrained='open-mmlab://msra/hrnetv2_w48',
     backbone=dict(
         extra=dict(
             stage2=dict(num_channels=(48, 96)),
             stage3=dict(num_channels=(48, 96, 192)),
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-20k_voc12aug-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-20k_voc12aug-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-40k_voc12aug-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-40k_voc12aug-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_hr48_4xb4-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb1-80k_cityscapes-768x768.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,39 +1,70 @@
-_base_ = './ocrnet_hr18_4xb4-80k_ade20k-512x512.py'
+_base_ = [
+    '../_base_/models/setr_pup.py', '../_base_/datasets/cityscapes_768x768.py',
+    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
+]
+crop_size = (768, 768)
+data_preprocessor = dict(size=crop_size)
 norm_cfg = dict(type='SyncBN', requires_grad=True)
+crop_size = (768, 768)
 model = dict(
-    pretrained='open-mmlab://msra/hrnetv2_w48',
+    data_preprocessor=data_preprocessor,
+    pretrained=None,
     backbone=dict(
-        extra=dict(
-            stage2=dict(num_channels=(48, 96)),
-            stage3=dict(num_channels=(48, 96, 192)),
-            stage4=dict(num_channels=(48, 96, 192, 384)))),
-    decode_head=[
+        drop_rate=0.,
+        init_cfg=dict(
+            type='Pretrained', checkpoint='pretrain/vit_large_p16.pth')),
+    auxiliary_head=[
         dict(
-            type='FCNHead',
-            in_channels=[48, 96, 192, 384],
-            channels=sum([48, 96, 192, 384]),
-            input_transform='resize_concat',
-            in_index=(0, 1, 2, 3),
-            kernel_size=1,
-            num_convs=1,
+            type='SETRUPHead',
+            in_channels=1024,
+            channels=256,
+            in_index=0,
+            num_classes=19,
+            dropout_ratio=0,
             norm_cfg=norm_cfg,
-            concat_input=False,
-            dropout_ratio=-1,
-            num_classes=150,
+            num_convs=2,
+            up_scale=4,
+            kernel_size=3,
             align_corners=False,
             loss_decode=dict(
                 type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
         dict(
-            type='OCRHead',
-            in_channels=[48, 96, 192, 384],
-            channels=512,
-            ocr_channels=256,
-            input_transform='resize_concat',
-            in_index=(0, 1, 2, 3),
+            type='SETRUPHead',
+            in_channels=1024,
+            channels=256,
+            in_index=1,
+            num_classes=19,
+            dropout_ratio=0,
             norm_cfg=norm_cfg,
-            dropout_ratio=-1,
-            num_classes=150,
+            num_convs=2,
+            up_scale=4,
+            kernel_size=3,
             align_corners=False,
             loss_decode=dict(
-                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=1.0))
-    ])
+                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
+        dict(
+            type='SETRUPHead',
+            in_channels=1024,
+            channels=256,
+            in_index=2,
+            num_classes=19,
+            dropout_ratio=0,
+            norm_cfg=norm_cfg,
+            num_convs=2,
+            up_scale=4,
+            kernel_size=3,
+            align_corners=False,
+            loss_decode=dict(
+                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4))
+    ],
+    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(512, 512)))
+
+optimizer = dict(weight_decay=0.0)
+optim_wrapper = dict(
+    type='OptimWrapper',
+    optimizer=optimizer,
+    paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)}))
+
+train_dataloader = dict(batch_size=1)
+val_dataloader = dict(batch_size=1)
+test_dataloader = val_dataloader
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-40k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-40k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/ocrnet/ocrnet_r101-d8_8xb2-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/point_rend.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/point_rend.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/pointrend_r50_4xb2-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/pointrend_r50_4xb2-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/point_rend/pointrend_r50_4xb4-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/point_rend/pointrend_r50_4xb4-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/fpn_poolformer_s12_8xb4-40k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/fpn_poolformer_s12_8xb4-40k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/poolformer/poolformer.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/poolformer/poolformer.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/psanet/psanet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/psanet/psanet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d32_rsb_4xb2-adamw-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d32_rsb_4xb2-adamw-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8-rsb_4xb2-adamw-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8-rsb_4xb2-adamw-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_dark-zurich-1920x1080.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_dark-zurich-1920x1080.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_night-driving-1920x1080.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_night-driving-1920x1080.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_dark-zurich-1920x1080.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_dark-zurich-1920x1080.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_night-driving-1920x1080.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb2-80k_cityscapes-512x1024_night-driving-1920x1080.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-40k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-59-480x480.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/pspnet/pspnet_r50-d8_4xb4-80k_pascal-context-59-480x480.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/resnest/resnest.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/resnest/resnest.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb1-160k_cityscapes-1024x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb1-160k_cityscapes-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b0_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb2-160k_ade20k-640x640.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segformer/segformer_mit-b5_8xb2-160k_ade20k-640x640.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-l_mask_8xb1-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-l_mask_8xb1-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-s_mask_8xb1-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-s_mask_8xb1-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/segmenter/segmenter_vit-t_mask_8xb1-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/segmenter/segmenter_vit-t_mask_8xb1-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/sem_fpn/sem_fpn.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/sem_fpn/sem_fpn.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l-mla_8xb1-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l-mla_8xb1-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_mla_8xb1-80k_cityscapes-768x768.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_mla_8xb1-80k_cityscapes-768x768.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb1-80k_cityscapes-768x768.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb1-80k_cityscapes-768x768.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_naive_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb1-80k_cityscapes-768x768.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb2-160k_ade20k-512x512.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,70 +1,72 @@
 _base_ = [
-    '../_base_/models/setr_pup.py', '../_base_/datasets/cityscapes_768x768.py',
-    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
+    '../_base_/models/setr_pup.py', '../_base_/datasets/ade20k.py',
+    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
 ]
-crop_size = (768, 768)
+crop_size = (512, 512)
 data_preprocessor = dict(size=crop_size)
 norm_cfg = dict(type='SyncBN', requires_grad=True)
-crop_size = (768, 768)
 model = dict(
     data_preprocessor=data_preprocessor,
     pretrained=None,
     backbone=dict(
+        img_size=(512, 512),
         drop_rate=0.,
         init_cfg=dict(
             type='Pretrained', checkpoint='pretrain/vit_large_p16.pth')),
+    decode_head=dict(num_classes=150),
     auxiliary_head=[
         dict(
             type='SETRUPHead',
             in_channels=1024,
             channels=256,
             in_index=0,
-            num_classes=19,
+            num_classes=150,
             dropout_ratio=0,
             norm_cfg=norm_cfg,
+            act_cfg=dict(type='ReLU'),
             num_convs=2,
-            up_scale=4,
             kernel_size=3,
             align_corners=False,
             loss_decode=dict(
                 type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
         dict(
             type='SETRUPHead',
             in_channels=1024,
             channels=256,
             in_index=1,
-            num_classes=19,
+            num_classes=150,
             dropout_ratio=0,
             norm_cfg=norm_cfg,
+            act_cfg=dict(type='ReLU'),
             num_convs=2,
-            up_scale=4,
             kernel_size=3,
             align_corners=False,
             loss_decode=dict(
                 type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
         dict(
             type='SETRUPHead',
             in_channels=1024,
             channels=256,
             in_index=2,
-            num_classes=19,
+            num_classes=150,
             dropout_ratio=0,
             norm_cfg=norm_cfg,
+            act_cfg=dict(type='ReLU'),
             num_convs=2,
-            up_scale=4,
             kernel_size=3,
             align_corners=False,
             loss_decode=dict(
-                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4))
+                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
     ],
-    test_cfg=dict(mode='slide', crop_size=crop_size, stride=(512, 512)))
+    test_cfg=dict(mode='slide', crop_size=(512, 512), stride=(341, 341)),
+)
 
-optimizer = dict(weight_decay=0.0)
+optimizer = dict(lr=0.001, weight_decay=0.0)
 optim_wrapper = dict(
     type='OptimWrapper',
     optimizer=optimizer,
     paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)}))
-
-train_dataloader = dict(batch_size=1)
+# num_gpus: 8 -> batch_size: 16
+train_dataloader = dict(batch_size=2)
 val_dataloader = dict(batch_size=1)
 test_dataloader = val_dataloader
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/setr/setr_vit-l_pup_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/_base_/datasets/ade20k.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,72 +1,68 @@
-_base_ = [
-    '../_base_/models/setr_pup.py', '../_base_/datasets/ade20k.py',
-    '../_base_/default_runtime.py', '../_base_/schedules/schedule_160k.py'
-]
+# dataset settings
+dataset_type = 'ADE20KDataset'
+data_root = 'data/ade/ADEChallengeData2016'
 crop_size = (512, 512)
-data_preprocessor = dict(size=crop_size)
-norm_cfg = dict(type='SyncBN', requires_grad=True)
-model = dict(
-    data_preprocessor=data_preprocessor,
-    pretrained=None,
-    backbone=dict(
-        img_size=(512, 512),
-        drop_rate=0.,
-        init_cfg=dict(
-            type='Pretrained', checkpoint='pretrain/vit_large_p16.pth')),
-    decode_head=dict(num_classes=150),
-    auxiliary_head=[
-        dict(
-            type='SETRUPHead',
-            in_channels=1024,
-            channels=256,
-            in_index=0,
-            num_classes=150,
-            dropout_ratio=0,
-            norm_cfg=norm_cfg,
-            act_cfg=dict(type='ReLU'),
-            num_convs=2,
-            kernel_size=3,
-            align_corners=False,
-            loss_decode=dict(
-                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
-        dict(
-            type='SETRUPHead',
-            in_channels=1024,
-            channels=256,
-            in_index=1,
-            num_classes=150,
-            dropout_ratio=0,
-            norm_cfg=norm_cfg,
-            act_cfg=dict(type='ReLU'),
-            num_convs=2,
-            kernel_size=3,
-            align_corners=False,
-            loss_decode=dict(
-                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
-        dict(
-            type='SETRUPHead',
-            in_channels=1024,
-            channels=256,
-            in_index=2,
-            num_classes=150,
-            dropout_ratio=0,
-            norm_cfg=norm_cfg,
-            act_cfg=dict(type='ReLU'),
-            num_convs=2,
-            kernel_size=3,
-            align_corners=False,
-            loss_decode=dict(
-                type='CrossEntropyLoss', use_sigmoid=False, loss_weight=0.4)),
-    ],
-    test_cfg=dict(mode='slide', crop_size=(512, 512), stride=(341, 341)),
-)
-
-optimizer = dict(lr=0.001, weight_decay=0.0)
-optim_wrapper = dict(
-    type='OptimWrapper',
-    optimizer=optimizer,
-    paramwise_cfg=dict(custom_keys={'head': dict(lr_mult=10.)}))
-# num_gpus: 8 -> batch_size: 16
-train_dataloader = dict(batch_size=2)
-val_dataloader = dict(batch_size=1)
+train_pipeline = [
+    dict(type='LoadImageFromFile'),
+    dict(type='LoadAnnotations', reduce_zero_label=True),
+    dict(
+        type='RandomResize',
+        scale=(2048, 512),
+        ratio_range=(0.5, 2.0),
+        keep_ratio=True),
+    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
+    dict(type='RandomFlip', prob=0.5),
+    dict(type='PhotoMetricDistortion'),
+    dict(type='PackSegInputs')
+]
+test_pipeline = [
+    dict(type='LoadImageFromFile'),
+    dict(type='Resize', scale=(2048, 512), keep_ratio=True),
+    # add loading annotation after ``Resize`` because ground truth
+    # does not need to do resize data transform
+    dict(type='LoadAnnotations', reduce_zero_label=True),
+    dict(type='PackSegInputs')
+]
+img_ratios = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
+tta_pipeline = [
+    dict(type='LoadImageFromFile', backend_args=None),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(type='Resize', scale_factor=r, keep_ratio=True)
+                for r in img_ratios
+            ],
+            [
+                dict(type='RandomFlip', prob=0., direction='horizontal'),
+                dict(type='RandomFlip', prob=1., direction='horizontal')
+            ], [dict(type='LoadAnnotations')], [dict(type='PackSegInputs')]
+        ])
+]
+train_dataloader = dict(
+    batch_size=4,
+    num_workers=4,
+    persistent_workers=True,
+    sampler=dict(type='InfiniteSampler', shuffle=True),
+    dataset=dict(
+        type=dataset_type,
+        data_root=data_root,
+        data_prefix=dict(
+            img_path='images/training', seg_map_path='annotations/training'),
+        pipeline=train_pipeline))
+val_dataloader = dict(
+    batch_size=1,
+    num_workers=4,
+    persistent_workers=True,
+    sampler=dict(type='DefaultSampler', shuffle=False),
+    dataset=dict(
+        type=dataset_type,
+        data_root=data_root,
+        data_prefix=dict(
+            img_path='images/validation',
+            seg_map_path='annotations/validation'),
+        pipeline=test_pipeline))
 test_dataloader = val_dataloader
+
+val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
+test_evaluator = val_evaluator
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/stdc/stdc1_4xb12-80k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/stdc/stdc1_4xb12-80k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-base-patch4-window12-in1k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-base-patch4-window12-in1k-384x384-pre_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-base-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-base-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-large-patch4-window7-in22k-pre_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-large-patch4-window7-in22k-pre_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin-tiny-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin-tiny-patch4-window7-in1k-pre_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/swin/swin.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/swin/swin.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_pcpvt-s_uperhead_8xb4-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_pcpvt-s_uperhead_8xb4-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-l_uperhead_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-l_uperhead_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-s_fpn_fpnhead_8xb4-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-s_fpn_fpnhead_8xb4-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/twins/twins_svt-s_uperhead_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/twins/twins_svt-s_uperhead_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-160k_cityscapes-512x1024.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet-s5-d16_fcn_4xb4-160k_cityscapes-512x1024.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/unet/unet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/unet/unet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/upernet/upernet.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/upernet/upernet.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_vit-b16-ln_mln_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_vit-b16-ln_mln_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-160k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-160k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-80k_ade20k-512x512.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/configs/vit/vit_vit-b16_mln_upernet_8xb2-80k_ade20k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/model-index.yml` & `mmsegmentation-1.0.0rc6/mmseg/.mim/model-index.yml`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/analyze_logs.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/analyze_logs.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/benchmark.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/benchmark.py`

 * *Files 2% similar despite different names*

```diff
@@ -4,19 +4,19 @@
 import time
 
 import numpy as np
 import torch
 from mmengine import Config
 from mmengine.fileio import dump
 from mmengine.model.utils import revert_sync_batchnorm
+from mmengine.registry import init_default_scope
 from mmengine.runner import Runner, load_checkpoint
 from mmengine.utils import mkdir_or_exist
 
 from mmseg.registry import MODELS
-from mmseg.utils import register_all_modules
 
 
 def parse_args():
     parser = argparse.ArgumentParser(description='MMSeg benchmark a model')
     parser.add_argument('config', help='test config file path')
     parser.add_argument('checkpoint', help='checkpoint file')
     parser.add_argument(
@@ -28,16 +28,18 @@
     parser.add_argument('--repeat-times', type=int, default=1)
     args = parser.parse_args()
     return args
 
 
 def main():
     args = parse_args()
-    register_all_modules()
     cfg = Config.fromfile(args.config)
+
+    init_default_scope(cfg.get('default_scope', 'mmseg'))
+
     timestamp = time.strftime('%Y%m%d_%H%M%S', time.localtime())
     if args.work_dir is not None:
         mkdir_or_exist(osp.abspath(args.work_dir))
         json_file = osp.join(args.work_dir, f'fps_{timestamp}.json')
     else:
         # use config filename as default work_dir if cfg.work_dir is None
         work_dir = osp.join('./work_dirs',
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/confusion_matrix.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/confusion_matrix.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/analysis_tools/get_flops.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/analysis_tools/get_flops.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/chase_db1.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/chase_db1.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/cityscapes.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/cityscapes.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/coco_stuff10k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/coco_stuff10k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/coco_stuff164k.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/coco_stuff164k.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/drive.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/drive.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/hrf.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/hrf.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/isaid.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/isaid.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/loveda.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/loveda.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/pascal_context.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/pascal_context.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/potsdam.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/potsdam.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/stare.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/stare.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/synapse.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/synapse.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/vaihingen.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/vaihingen.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/dataset_converters/voc_aug.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/dataset_converters/voc_aug.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/deployment/pytorch2torchscript.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/deployment/pytorch2torchscript.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/browse_dataset.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/browse_dataset.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import argparse
 import os.path as osp
 
 from mmengine import Config, DictAction
+from mmengine.registry import init_default_scope
 from mmengine.utils import ProgressBar
 
 from mmseg.registry import DATASETS, VISUALIZERS
-from mmseg.utils import register_all_modules
 
 
 def parse_args():
     parser = argparse.ArgumentParser(description='Browse a dataset')
     parser.add_argument('config', help='train config file path')
     parser.add_argument(
         '--output-dir',
@@ -40,15 +40,15 @@
 def main():
     args = parse_args()
     cfg = Config.fromfile(args.config)
     if args.cfg_options is not None:
         cfg.merge_from_dict(args.cfg_options)
 
     # register all modules in mmseg into the registries
-    register_all_modules()
+    init_default_scope('mmseg')
 
     dataset = DATASETS.build(cfg.train_dataloader.dataset)
     cfg.visualizer['save_dir'] = args.output_dir
     visualizer = VISUALIZERS.build(cfg.visualizer)
     visualizer.dataset_meta = dataset.METAINFO
 
     progress_bar = ProgressBar(len(dataset))
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/print_config.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/print_config.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/misc/publish_model.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/misc/publish_model.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/beit2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/beit2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/mit2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/mit2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/stdc2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/stdc2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/swin2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/swin2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/twins2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/twins2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/vit2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/vit2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/model_converters/vitjax2mmseg.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/model_converters/vitjax2mmseg.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/slurm_test.sh` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/slurm_test.sh`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/slurm_train.sh` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/slurm_train.sh`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/test.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/test.py`

 * *Files 8% similar despite different names*

```diff
@@ -2,16 +2,14 @@
 import argparse
 import os
 import os.path as osp
 
 from mmengine.config import Config, DictAction
 from mmengine.runner import Runner
 
-from mmseg.utils import register_all_modules
-
 
 # TODO: support fuse_conv_bn, visualization, and format_only
 def parse_args():
     parser = argparse.ArgumentParser(
         description='MMSeg test (and eval) a model')
     parser.add_argument('config', help='train config file path')
     parser.add_argument('checkpoint', help='checkpoint file')
@@ -73,18 +71,14 @@
 
     return cfg
 
 
 def main():
     args = parse_args()
 
-    # register all modules in mmseg into the registries
-    # do not init the default scope here because it will be init in the runner
-    register_all_modules(init_default_scope=False)
-
     # load config
     cfg = Config.fromfile(args.config)
     cfg.launcher = args.launcher
     if args.cfg_options is not None:
         cfg.merge_from_dict(args.cfg_options)
 
     # work_dir is determined in this priority: CLI > segment in file > filename
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/mmseg2torchserve.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/mmseg2torchserve.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/mmseg_handler.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/mmseg_handler.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/torchserve/test_torchserve.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/torchserve/test_torchserve.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/.mim/tools/train.py` & `mmsegmentation-1.0.0rc6/mmseg/.mim/tools/train.py`

 * *Files 12% similar despite different names*

```diff
@@ -2,18 +2,17 @@
 import argparse
 import logging
 import os
 import os.path as osp
 
 from mmengine.config import Config, DictAction
 from mmengine.logging import print_log
-from mmengine.registry import RUNNERS
 from mmengine.runner import Runner
 
-from mmseg.utils import register_all_modules
+from mmseg.registry import RUNNERS
 
 
 def parse_args():
     parser = argparse.ArgumentParser(description='Train a segmentor')
     parser.add_argument('config', help='train config file path')
     parser.add_argument('--work-dir', help='the dir to save logs and models')
     parser.add_argument(
@@ -48,18 +47,14 @@
 
     return args
 
 
 def main():
     args = parse_args()
 
-    # register all modules in mmseg into the registries
-    # do not init the default scope here because it will be init in the runner
-    register_all_modules(init_default_scope=False)
-
     # load config
     cfg = Config.fromfile(args.config)
     cfg.launcher = args.launcher
     if args.cfg_options is not None:
         cfg.merge_from_dict(args.cfg_options)
 
     # work_dir is determined in this priority: CLI > segment in file > filename
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 import mmengine
 from packaging.version import parse
 
 from .version import __version__, version_info
 
 MMCV_MIN = '2.0.0rc4'
 MMCV_MAX = '2.1.0'
-MMENGINE_MIN = '0.2.0'
+MMENGINE_MIN = '0.5.0'
 MMENGINE_MAX = '1.0.0'
 
 
 def digit_version(version_str: str, length: int = 4):
     """Convert a version string into a tuple of integers.
 
     This method is usually used for comparing two versions. For pre-release
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/apis/inference.py` & `mmsegmentation-1.0.0rc6/mmseg/apis/inference.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 from typing import Optional, Sequence, Union
 
 import mmcv
 import numpy as np
 import torch
 from mmengine import Config
 from mmengine.dataset import Compose
+from mmengine.registry import init_default_scope
 from mmengine.runner import load_checkpoint
 from mmengine.utils import mkdir_or_exist
 
 from mmseg.models import BaseSegmentor
 from mmseg.registry import MODELS
 from mmseg.structures import SegDataSample
 from mmseg.utils import SampleList, dataset_aliases, get_classes, get_palette
@@ -44,14 +45,16 @@
                         'but got {}'.format(type(config)))
     if cfg_options is not None:
         config.merge_from_dict(cfg_options)
     elif 'init_cfg' in config.model.backbone:
         config.model.backbone.init_cfg = None
     config.model.pretrained = None
     config.model.train_cfg = None
+    init_default_scope(config.get('default_scope', 'mmseg'))
+
     model = MODELS.build(config.model)
     if checkpoint is not None:
         checkpoint = load_checkpoint(model, checkpoint, map_location='cpu')
         dataset_meta = checkpoint['meta'].get('dataset_meta', None)
         # save the dataset_meta in the model for convenience
         if 'dataset_meta' in checkpoint.get('meta', {}):
             # mmseg 1.x
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -13,14 +13,15 @@
 from .isaid import iSAIDDataset
 from .isprs import ISPRSDataset
 from .lip import LIPDataset
 from .loveda import LoveDADataset
 from .night_driving import NightDrivingDataset
 from .pascal_context import PascalContextDataset, PascalContextDataset59
 from .potsdam import PotsdamDataset
+from .refuge import REFUGEDataset
 from .stare import STAREDataset
 from .synapse import SynapseDataset
 # yapf: disable
 from .transforms import (CLAHE, AdjustGamma, BioMedical3DPad,
                          BioMedical3DRandomCrop, BioMedical3DRandomFlip,
                          BioMedicalGaussianBlur, BioMedicalGaussianNoise,
                          BioMedicalRandomGamma, GenerateEdge, LoadAnnotations,
@@ -44,9 +45,9 @@
     'RandomRotate', 'AdjustGamma', 'CLAHE', 'Rerange', 'RGB2Gray',
     'RandomCutOut', 'RandomMosaic', 'PackSegInputs', 'ResizeToMultiple',
     'LoadImageFromNDArray', 'LoadBiomedicalImageFromFile',
     'LoadBiomedicalAnnotation', 'LoadBiomedicalData', 'GenerateEdge',
     'DecathlonDataset', 'LIPDataset', 'ResizeShortestEdge',
     'BioMedicalGaussianNoise', 'BioMedicalGaussianBlur',
     'BioMedicalRandomGamma', 'BioMedical3DPad', 'RandomRotFlip',
-    'SynapseDataset'
+    'SynapseDataset', 'REFUGEDataset'
 ]
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/ade.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/ade.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/basesegdataset.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/basesegdataset.py`

 * *Files 2% similar despite different names*

```diff
@@ -69,46 +69,44 @@
             save time by set ``lazy_init=True``. Defaults to False.
         max_refetch (int, optional): If ``Basedataset.prepare_data`` get a
             None img. The maximum extra number of cycles to get a valid
             image. Defaults to 1000.
         ignore_index (int): The label index to be ignored. Default: 255
         reduce_zero_label (bool): Whether to mark label zero as ignored.
             Default to False.
-        backend_args (dict): Arguments to instantiate a file backend.
+        backend_args (dict, Optional): Arguments to instantiate a file backend.
             See https://mmengine.readthedocs.io/en/latest/api/fileio.htm
-            for details. Defaults to ``dict(backend='local')``
+            for details. Defaults to None.
             Notes: mmcv>=2.0.0rc4, mmengine>=0.2.0 required.
     """
     METAINFO: dict = dict()
 
-    def __init__(
-        self,
-        ann_file: str = '',
-        img_suffix='.jpg',
-        seg_map_suffix='.png',
-        metainfo: Optional[dict] = None,
-        data_root: Optional[str] = None,
-        data_prefix: dict = dict(img_path='', seg_map_path=''),
-        filter_cfg: Optional[dict] = None,
-        indices: Optional[Union[int, Sequence[int]]] = None,
-        serialize_data: bool = True,
-        pipeline: List[Union[dict, Callable]] = [],
-        test_mode: bool = False,
-        lazy_init: bool = False,
-        max_refetch: int = 1000,
-        ignore_index: int = 255,
-        reduce_zero_label: bool = False,
-        backend_args: dict = dict(backend='local')
-    ) -> None:
+    def __init__(self,
+                 ann_file: str = '',
+                 img_suffix='.jpg',
+                 seg_map_suffix='.png',
+                 metainfo: Optional[dict] = None,
+                 data_root: Optional[str] = None,
+                 data_prefix: dict = dict(img_path='', seg_map_path=''),
+                 filter_cfg: Optional[dict] = None,
+                 indices: Optional[Union[int, Sequence[int]]] = None,
+                 serialize_data: bool = True,
+                 pipeline: List[Union[dict, Callable]] = [],
+                 test_mode: bool = False,
+                 lazy_init: bool = False,
+                 max_refetch: int = 1000,
+                 ignore_index: int = 255,
+                 reduce_zero_label: bool = False,
+                 backend_args: Optional[dict] = None) -> None:
 
         self.img_suffix = img_suffix
         self.seg_map_suffix = seg_map_suffix
         self.ignore_index = ignore_index
         self.reduce_zero_label = reduce_zero_label
-        self.backend_args = backend_args.copy()
+        self.backend_args = backend_args.copy() if backend_args else None
 
         self.data_root = data_root
         self.data_prefix = copy.copy(data_prefix)
         self.ann_file = ann_file
         self.filter_cfg = copy.deepcopy(filter_cfg)
         self._indices = indices
         self.serialize_data = serialize_data
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/chase_db1.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/chase_db1.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/cityscapes.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/cityscapes.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/coco_stuff.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/coco_stuff.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/dataset_wrappers.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/dataset_wrappers.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/decathlon.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/decathlon.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/drive.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/drive.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/hrf.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/hrf.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/isaid.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/isaid.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/isprs.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/isprs.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/lip.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/lip.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/loveda.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/loveda.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/night_driving.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/night_driving.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/pascal_context.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/pascal_context.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/potsdam.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/potsdam.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/stare.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/stare.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/synapse.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/synapse.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/formatting.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/formatting.py`

 * *Files 7% similar despite different names*

```diff
@@ -59,16 +59,20 @@
                 sample.
         """
         packed_results = dict()
         if 'img' in results:
             img = results['img']
             if len(img.shape) < 3:
                 img = np.expand_dims(img, -1)
-            img = np.ascontiguousarray(img.transpose(2, 0, 1))
-            packed_results['inputs'] = to_tensor(img)
+            if not img.flags.c_contiguous:
+                img = to_tensor(np.ascontiguousarray(img.transpose(2, 0, 1)))
+            else:
+                img = img.transpose(2, 0, 1)
+                img = to_tensor(img).contiguous()
+            packed_results['inputs'] = img
 
         data_sample = SegDataSample()
         if 'gt_seg_map' in results:
             gt_sem_seg_data = dict(
                 data=to_tensor(results['gt_seg_map'][None,
                                                      ...].astype(np.int64)))
             data_sample.gt_sem_seg = PixelData(**gt_sem_seg_data)
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/loading.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/loading.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import warnings
-from typing import Dict
+from typing import Dict, Optional, Union
 
 import mmcv
 import mmengine.fileio as fileio
 import numpy as np
 from mmcv.transforms import BaseTransform
 from mmcv.transforms import LoadAnnotations as MMCV_LoadAnnotations
 from mmcv.transforms import LoadImageFromFile
@@ -52,22 +52,22 @@
             Defaults to None.
         imdecode_backend (str): The image decoding backend type. The backend
             argument for :func:``mmcv.imfrombytes``.
             See :fun:``mmcv.imfrombytes`` for details.
             Defaults to 'pillow'.
         backend_args (dict): Arguments to instantiate a file backend.
             See https://mmengine.readthedocs.io/en/latest/api/fileio.htm
-            for details. Defaults to ``dict(backend='local')``
+            for details. Defaults to None.
             Notes: mmcv>=2.0.0rc4, mmengine>=0.2.0 required.
     """
 
     def __init__(
         self,
         reduce_zero_label=None,
-        backend_args=dict(backend='local'),
+        backend_args=None,
         imdecode_backend='pillow',
     ) -> None:
         super().__init__(
             with_bbox=False,
             with_label=False,
             with_seg=True,
             with_keypoints=False,
@@ -199,31 +199,29 @@
             'numpy', the the axis is ZYX. The data will be transposed if the
             backend is 'nifti'. Defaults to 'nifti'.
         to_xyz (bool): Whether transpose data from Z, Y, X to X, Y, Z.
             Defaults to False.
         to_float32 (bool): Whether to convert the loaded image to a float32
             numpy array. If set to False, the loaded image is an float64 array.
             Defaults to True.
-        backend_args (dict): Arguments to instantiate a file backend.
+        backend_args (dict, Optional): Arguments to instantiate a file backend.
             See https://mmengine.readthedocs.io/en/latest/api/fileio.htm
-            for details. Defaults to ``dict(backend='local')``
+            for details. Defaults to None.
             Notes: mmcv>=2.0.0rc4, mmengine>=0.2.0 required.
     """
 
-    def __init__(
-        self,
-        decode_backend: str = 'nifti',
-        to_xyz: bool = False,
-        to_float32: bool = True,
-        backend_args: dict = dict(backend='local')
-    ) -> None:
+    def __init__(self,
+                 decode_backend: str = 'nifti',
+                 to_xyz: bool = False,
+                 to_float32: bool = True,
+                 backend_args: Optional[dict] = None) -> None:
         self.decode_backend = decode_backend
         self.to_xyz = to_xyz
         self.to_float32 = to_float32
-        self.backend_args = backend_args.copy()
+        self.backend_args = backend_args.copy() if backend_args else None
 
     def transform(self, results: Dict) -> Dict:
         """Functions to load image.
 
         Args:
             results (dict): Result dict from :obj:``mmcv.BaseDataset``.
 
@@ -291,32 +289,30 @@
             'numpy', the the axis is ZYX. The data will be transposed if the
             backend is 'nifti'. Defaults to 'nifti'.
         to_xyz (bool): Whether transpose data from Z, Y, X to X, Y, Z.
             Defaults to False.
         to_float32 (bool): Whether to convert the loaded seg map to a float32
             numpy array. If set to False, the loaded image is an float64 array.
             Defaults to True.
-        backend_args (dict): Arguments to instantiate a file backend.
+        backend_args (dict, Optional): Arguments to instantiate a file backend.
             See :class:`mmengine.fileio` for details.
-            Defaults to ``dict(backend='local')``.
+            Defaults to None.
             Notes: mmcv>=2.0.0rc4, mmengine>=0.2.0 required.
     """
 
-    def __init__(
-        self,
-        decode_backend: str = 'nifti',
-        to_xyz: bool = False,
-        to_float32: bool = True,
-        backend_args: dict = dict(backend='local')
-    ) -> None:
+    def __init__(self,
+                 decode_backend: str = 'nifti',
+                 to_xyz: bool = False,
+                 to_float32: bool = True,
+                 backend_args: Optional[dict] = None) -> None:
         super().__init__()
         self.decode_backend = decode_backend
         self.to_xyz = to_xyz
         self.to_float32 = to_float32
-        self.backend_args = backend_args.copy()
+        self.backend_args = backend_args.copy() if backend_args else None
 
     def transform(self, results: Dict) -> Dict:
         """Functions to load image.
 
         Args:
             results (dict): Result dict from :obj:``mmcv.BaseDataset``.
 
@@ -380,31 +376,29 @@
         decode_backend (str): The data decoding backend type. Options are
             'numpy'and 'nifti', and there is a convention that when backend is
             'nifti' the axis of data loaded is XYZ, and when backend is
             'numpy', the the axis is ZYX. The data will be transposed if the
             backend is 'nifti'. Defaults to 'nifti'.
         to_xyz (bool): Whether transpose data from Z, Y, X to X, Y, Z.
             Defaults to False.
-        backend_args (dict): Arguments to instantiate a file backend.
+        backend_args (dict, Optional): Arguments to instantiate a file backend.
             See https://mmengine.readthedocs.io/en/latest/api/fileio.htm
-            for details. Defaults to ``dict(backend='local')``
+            for details. Defaults to None.
             Notes: mmcv>=2.0.0rc4, mmengine>=0.2.0 required.
     """
 
-    def __init__(
-        self,
-        with_seg=False,
-        decode_backend: str = 'numpy',
-        to_xyz: bool = False,
-        backend_args: dict = dict(backend='local')
-    ) -> None:  # noqa
+    def __init__(self,
+                 with_seg=False,
+                 decode_backend: str = 'numpy',
+                 to_xyz: bool = False,
+                 backend_args: Optional[dict] = None) -> None:  # noqa
         self.with_seg = with_seg
         self.decode_backend = decode_backend
         self.to_xyz = to_xyz
-        self.backend_args = backend_args.copy()
+        self.backend_args = backend_args.copy() if backend_args else None
 
     def transform(self, results: Dict) -> Dict:
         """Functions to load image.
 
         Args:
             results (dict): Result dict from :obj:``mmcv.BaseDataset``.
 
@@ -439,7 +433,63 @@
     def __repr__(self) -> str:
         repr_str = (f'{self.__class__.__name__}('
                     f'with_seg={self.with_seg}, '
                     f"decode_backend='{self.decode_backend}', "
                     f'to_xyz={self.to_xyz}, '
                     f'backend_args={self.backend_args})')
         return repr_str
+
+
+@TRANSFORMS.register_module()
+class InferencerLoader(BaseTransform):
+    """Load an image from ``results['img']``.
+
+    Similar with :obj:`LoadImageFromFile`, but the image has been loaded as
+    :obj:`np.ndarray` in ``results['img']``. Can be used when loading image
+    from webcam.
+
+    Required Keys:
+
+    - img
+
+    Modified Keys:
+
+    - img
+    - img_path
+    - img_shape
+    - ori_shape
+
+    Args:
+        to_float32 (bool): Whether to convert the loaded image to a float32
+            numpy array. If set to False, the loaded image is an uint8 array.
+            Defaults to False.
+    """
+
+    def __init__(self, **kwargs) -> None:
+        super().__init__()
+        self.from_file = TRANSFORMS.build(
+            dict(type='LoadImageFromFile', **kwargs))
+        self.from_ndarray = TRANSFORMS.build(
+            dict(type='LoadImageFromNDArray', **kwargs))
+
+    def transform(self, single_input: Union[str, np.ndarray, dict]) -> dict:
+        """Transform function to add image meta information.
+
+        Args:
+            results (dict): Result dict with Webcam read image in
+                ``results['img']``.
+
+        Returns:
+            dict: The dict contains loaded image and meta information.
+        """
+        if isinstance(single_input, str):
+            inputs = dict(img_path=single_input)
+        elif isinstance(single_input, np.ndarray):
+            inputs = dict(img=single_input)
+        elif isinstance(single_input, dict):
+            inputs = single_input
+        else:
+            raise NotImplementedError
+
+        if 'img' in inputs:
+            return self.from_ndarray(inputs)
+        return self.from_file(inputs)
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/transforms/transforms.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/transforms/transforms.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/datasets/voc.py` & `mmsegmentation-1.0.0rc6/mmseg/datasets/voc.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/engine/hooks/visualization_hook.py` & `mmsegmentation-1.0.0rc6/mmseg/engine/hooks/visualization_hook.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import os.path as osp
 import warnings
-from typing import Sequence
+from typing import Optional, Sequence
 
 import mmcv
 import mmengine.fileio as fileio
 from mmengine.hooks import Hook
 from mmengine.runner import Runner
 
 from mmseg.registry import HOOKS
@@ -26,40 +26,40 @@
 
     Args:
         draw (bool): whether to draw prediction results. If it is False,
             it means that no drawing will be done. Defaults to False.
         interval (int): The interval of visualization. Defaults to 50.
         show (bool): Whether to display the drawn image. Default to False.
         wait_time (float): The interval of show (s). Defaults to 0.
-        backend_args (dict): Arguments to instantiate a file backend.
+        backend_args (dict, Optional): Arguments to instantiate a file backend.
             See https://mmengine.readthedocs.io/en/latest/api/fileio.htm
-            for details. Defaults to ``dict(backend='local')``
+            for details. Defaults to None.
             Notes: mmcv>=2.0.0rc4, mmengine>=0.2.0 required.
     """
 
     def __init__(self,
                  draw: bool = False,
                  interval: int = 50,
                  show: bool = False,
                  wait_time: float = 0.,
-                 backend_args: dict = dict(backend='local')):
+                 backend_args: Optional[dict] = None):
         self._visualizer: SegLocalVisualizer = \
             SegLocalVisualizer.get_current_instance()
         self.interval = interval
         self.show = show
         if self.show:
             # No need to think about vis backends.
             self._visualizer._vis_backends = {}
             warnings.warn('The show is True, it means that only '
                           'the prediction results are visualized '
                           'without storing data, so vis_backends '
                           'needs to be excluded.')
 
         self.wait_time = wait_time
-        self.backend_args = backend_args.copy()
+        self.backend_args = backend_args.copy() if backend_args else None
         self.draw = draw
         if not self.draw:
             warnings.warn('The draw is False, it means that the '
                           'hook for visualization will not take '
                           'effect. The results will NOT be '
                           'visualized or stored.')
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/engine/optimizers/layer_decay_optimizer_constructor.py` & `mmsegmentation-1.0.0rc6/mmseg/engine/optimizers/layer_decay_optimizer_constructor.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/evaluation/metrics/citys_metric.py` & `mmsegmentation-1.0.0rc6/mmseg/evaluation/metrics/citys_metric.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/evaluation/metrics/iou_metric.py` & `mmsegmentation-1.0.0rc6/mmseg/evaluation/metrics/iou_metric.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/models/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/beit.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/beit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/bisenetv1.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/bisenetv1.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/bisenetv2.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/bisenetv2.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/cgnet.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/cgnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/erfnet.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/erfnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/fast_scnn.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/fast_scnn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/hrnet.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/hrnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/icnet.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/icnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/mae.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/mae.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/mit.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/mit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/mobilenet_v2.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/mobilenet_v2.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/mobilenet_v3.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/mobilenet_v3.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/resnest.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/resnest.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/resnet.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/resnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/resnext.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/resnext.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/stdc.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/stdc.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/swin.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/swin.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/timm_backbone.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/timm_backbone.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/twins.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/twins.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/unet.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/unet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/backbones/vit.py` & `mmsegmentation-1.0.0rc6/mmseg/models/backbones/vit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/builder.py` & `mmsegmentation-1.0.0rc6/mmseg/models/builder.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/data_preprocessor.py` & `mmsegmentation-1.0.0rc6/mmseg/models/data_preprocessor.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/ann_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/ann_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/apc_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/apc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/aspp_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/aspp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/cascade_decode_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/cascade_decode_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/cc_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/cc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/da_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/da_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/decode_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/decode_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/dm_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/dm_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/dnl_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/dnl_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/dpt_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/dpt_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/ema_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/ema_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/enc_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/enc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/fcn_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/fcn_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/fpn_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/fpn_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/gc_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/gc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/isa_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/isa_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/knet_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/knet_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/lraspp_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/lraspp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/mask2former_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/mask2former_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/maskformer_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/maskformer_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/nl_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/nl_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/ocr_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/ocr_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/point_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/point_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/psa_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/psa_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/psp_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/psp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/segformer_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/segformer_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/segmenter_mask_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/segmenter_mask_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/sep_aspp_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/sep_aspp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/sep_fcn_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/sep_fcn_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/setr_mla_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/setr_mla_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/setr_up_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/setr_up_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/stdc_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/stdc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/decode_heads/uper_head.py` & `mmsegmentation-1.0.0rc6/mmseg/models/decode_heads/uper_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/accuracy.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/accuracy.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/cross_entropy_loss.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/cross_entropy_loss.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/dice_loss.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/dice_loss.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/focal_loss.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/focal_loss.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/lovasz_loss.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/lovasz_loss.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/tversky_loss.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/tversky_loss.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/losses/utils.py` & `mmsegmentation-1.0.0rc6/mmseg/models/losses/utils.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/necks/featurepyramid.py` & `mmsegmentation-1.0.0rc6/mmseg/models/necks/featurepyramid.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/necks/fpn.py` & `mmsegmentation-1.0.0rc6/mmseg/models/necks/fpn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/necks/ic_neck.py` & `mmsegmentation-1.0.0rc6/mmseg/models/necks/ic_neck.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/necks/jpu.py` & `mmsegmentation-1.0.0rc6/mmseg/models/necks/jpu.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/necks/mla_neck.py` & `mmsegmentation-1.0.0rc6/mmseg/models/necks/mla_neck.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/necks/multilevel_neck.py` & `mmsegmentation-1.0.0rc6/mmseg/models/necks/multilevel_neck.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/segmentors/base.py` & `mmsegmentation-1.0.0rc6/mmseg/models/segmentors/base.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/segmentors/cascade_encoder_decoder.py` & `mmsegmentation-1.0.0rc6/mmseg/models/segmentors/cascade_encoder_decoder.py`

 * *Files 2% similar despite different names*

```diff
@@ -64,14 +64,15 @@
         assert isinstance(decode_head, list)
         assert len(decode_head) == self.num_stages
         self.decode_head = nn.ModuleList()
         for i in range(self.num_stages):
             self.decode_head.append(MODELS.build(decode_head[i]))
         self.align_corners = self.decode_head[-1].align_corners
         self.num_classes = self.decode_head[-1].num_classes
+        self.out_channels = self.decode_head[-1].out_channels
 
     def encode_decode(self, inputs: Tensor,
                       batch_img_metas: List[dict]) -> Tensor:
         """Encode images with backbone and decode into a semantic segmentation
         map of the same size as input."""
         x = self.extract_feat(inputs)
         out = self.decode_head[0].forward(x)
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/segmentors/encoder_decoder.py` & `mmsegmentation-1.0.0rc6/mmseg/models/segmentors/encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/segmentors/seg_tta.py` & `mmsegmentation-1.0.0rc6/mmseg/models/segmentors/seg_tta.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/embed.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/embed.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/encoding.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/encoding.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/inverted_residual.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/inverted_residual.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/make_divisible.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/make_divisible.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/res_layer.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/res_layer.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/se_layer.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/se_layer.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/self_attention_block.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/self_attention_block.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/shape_convert.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/shape_convert.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/up_conv_block.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/up_conv_block.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/models/utils/wrappers.py` & `mmsegmentation-1.0.0rc6/mmseg/models/utils/wrappers.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/registry/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/registry/__init__.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,13 +1,15 @@
 # Copyright (c) OpenMMLab. All rights reserved.
-from .registry import (DATA_SAMPLERS, DATASETS, HOOKS, LOOPS, METRICS,
-                       MODEL_WRAPPERS, MODELS, OPTIM_WRAPPER_CONSTRUCTORS,
-                       OPTIMIZERS, PARAM_SCHEDULERS, RUNNER_CONSTRUCTORS,
-                       RUNNERS, TASK_UTILS, TRANSFORMS, VISBACKENDS,
-                       VISUALIZERS, WEIGHT_INITIALIZERS)
+from .registry import (DATA_SAMPLERS, DATASETS, EVALUATOR, HOOKS, INFERENCERS,
+                       LOG_PROCESSORS, LOOPS, METRICS, MODEL_WRAPPERS, MODELS,
+                       OPTIM_WRAPPER_CONSTRUCTORS, OPTIM_WRAPPERS, OPTIMIZERS,
+                       PARAM_SCHEDULERS, RUNNER_CONSTRUCTORS, RUNNERS,
+                       TASK_UTILS, TRANSFORMS, VISBACKENDS, VISUALIZERS,
+                       WEIGHT_INITIALIZERS)
 
 __all__ = [
-    'RUNNERS', 'RUNNER_CONSTRUCTORS', 'HOOKS', 'DATASETS', 'DATA_SAMPLERS',
-    'TRANSFORMS', 'MODELS', 'WEIGHT_INITIALIZERS', 'OPTIMIZERS',
-    'OPTIM_WRAPPER_CONSTRUCTORS', 'TASK_UTILS', 'PARAM_SCHEDULERS', 'METRICS',
-    'MODEL_WRAPPERS', 'LOOPS', 'VISBACKENDS', 'VISUALIZERS'
+    'HOOKS', 'DATASETS', 'DATA_SAMPLERS', 'TRANSFORMS', 'MODELS',
+    'WEIGHT_INITIALIZERS', 'OPTIMIZERS', 'OPTIM_WRAPPER_CONSTRUCTORS',
+    'TASK_UTILS', 'PARAM_SCHEDULERS', 'METRICS', 'MODEL_WRAPPERS',
+    'VISBACKENDS', 'VISUALIZERS', 'RUNNERS', 'RUNNER_CONSTRUCTORS', 'LOOPS',
+    'EVALUATOR', 'LOG_PROCESSORS', 'OPTIM_WRAPPERS', 'INFERENCERS'
 ]
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/registry/registry.py` & `mmsegmentation-1.0.0rc6/mmseg/registry/registry.py`

 * *Files 25% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 https://mmengine.readthedocs.io/en/latest/tutorials/registry.html.
 """
 
 from mmengine.registry import DATA_SAMPLERS as MMENGINE_DATA_SAMPLERS
 from mmengine.registry import DATASETS as MMENGINE_DATASETS
 from mmengine.registry import EVALUATOR as MMENGINE_EVALUATOR
 from mmengine.registry import HOOKS as MMENGINE_HOOKS
+from mmengine.registry import INFERENCERS as MMENGINE_INFERENCERS
 from mmengine.registry import LOG_PROCESSORS as MMENGINE_LOG_PROCESSORS
 from mmengine.registry import LOOPS as MMENGINE_LOOPS
 from mmengine.registry import METRICS as MMENGINE_METRICS
 from mmengine.registry import MODEL_WRAPPERS as MMENGINE_MODEL_WRAPPERS
 from mmengine.registry import MODELS as MMENGINE_MODELS
 from mmengine.registry import \
     OPTIM_WRAPPER_CONSTRUCTORS as MMENGINE_OPTIM_WRAPPER_CONSTRUCTORS
@@ -35,49 +36,86 @@
 RUNNERS = Registry('runner', parent=MMENGINE_RUNNERS)
 # manage runner constructors that define how to initialize runners
 RUNNER_CONSTRUCTORS = Registry(
     'runner constructor', parent=MMENGINE_RUNNER_CONSTRUCTORS)
 # manage all kinds of loops like `EpochBasedTrainLoop`
 LOOPS = Registry('loop', parent=MMENGINE_LOOPS)
 # manage all kinds of hooks like `CheckpointHook`
-HOOKS = Registry('hook', parent=MMENGINE_HOOKS)
+HOOKS = Registry(
+    'hook', parent=MMENGINE_HOOKS, locations=['mmseg.engine.hooks'])
 
 # manage data-related modules
-DATASETS = Registry('dataset', parent=MMENGINE_DATASETS)
-DATA_SAMPLERS = Registry('data sampler', parent=MMENGINE_DATA_SAMPLERS)
-TRANSFORMS = Registry('transform', parent=MMENGINE_TRANSFORMS)
+DATASETS = Registry(
+    'dataset', parent=MMENGINE_DATASETS, locations=['mmseg.datasets'])
+DATA_SAMPLERS = Registry(
+    'data sampler',
+    parent=MMENGINE_DATA_SAMPLERS,
+    locations=['mmseg.datasets.samplers'])
+TRANSFORMS = Registry(
+    'transform',
+    parent=MMENGINE_TRANSFORMS,
+    locations=['mmseg.datasets.transforms'])
 
 # mangage all kinds of modules inheriting `nn.Module`
-MODELS = Registry('model', parent=MMENGINE_MODELS)
+MODELS = Registry('model', parent=MMENGINE_MODELS, locations=['mmseg.models'])
 # mangage all kinds of model wrappers like 'MMDistributedDataParallel'
-MODEL_WRAPPERS = Registry('model_wrapper', parent=MMENGINE_MODEL_WRAPPERS)
+MODEL_WRAPPERS = Registry(
+    'model_wrapper',
+    parent=MMENGINE_MODEL_WRAPPERS,
+    locations=['mmseg.models'])
 # mangage all kinds of weight initialization modules like `Uniform`
 WEIGHT_INITIALIZERS = Registry(
-    'weight initializer', parent=MMENGINE_WEIGHT_INITIALIZERS)
+    'weight initializer',
+    parent=MMENGINE_WEIGHT_INITIALIZERS,
+    locations=['mmseg.models'])
 
 # mangage all kinds of optimizers like `SGD` and `Adam`
-OPTIMIZERS = Registry('optimizer', parent=MMENGINE_OPTIMIZERS)
+OPTIMIZERS = Registry(
+    'optimizer',
+    parent=MMENGINE_OPTIMIZERS,
+    locations=['mmseg.engine.optimizers'])
 # manage optimizer wrapper
-OPTIM_WRAPPERS = Registry('optim_wrapper', parent=MMENGINE_OPTIM_WRAPPERS)
+OPTIM_WRAPPERS = Registry(
+    'optim_wrapper',
+    parent=MMENGINE_OPTIM_WRAPPERS,
+    locations=['mmseg.engine.optimizers'])
 # manage constructors that customize the optimization hyperparameters.
 OPTIM_WRAPPER_CONSTRUCTORS = Registry(
     'optimizer wrapper constructor',
-    parent=MMENGINE_OPTIM_WRAPPER_CONSTRUCTORS)
+    parent=MMENGINE_OPTIM_WRAPPER_CONSTRUCTORS,
+    locations=['mmseg.engine.optimizers'])
 # mangage all kinds of parameter schedulers like `MultiStepLR`
 PARAM_SCHEDULERS = Registry(
-    'parameter scheduler', parent=MMENGINE_PARAM_SCHEDULERS)
+    'parameter scheduler',
+    parent=MMENGINE_PARAM_SCHEDULERS,
+    locations=['mmseg.engine.schedulers'])
 
 # manage all kinds of metrics
-METRICS = Registry('metric', parent=MMENGINE_METRICS)
+METRICS = Registry(
+    'metric', parent=MMENGINE_METRICS, locations=['mmseg.evaluation'])
 # manage evaluator
-EVALUATOR = Registry('evaluator', parent=MMENGINE_EVALUATOR)
+EVALUATOR = Registry(
+    'evaluator', parent=MMENGINE_EVALUATOR, locations=['mmseg.evaluation'])
 
 # manage task-specific modules like ohem pixel sampler
-TASK_UTILS = Registry('task util', parent=MMENGINE_TASK_UTILS)
+TASK_UTILS = Registry(
+    'task util', parent=MMENGINE_TASK_UTILS, locations=['mmseg.models'])
 
 # manage visualizer
-VISUALIZERS = Registry('visualizer', parent=MMENGINE_VISUALIZERS)
+VISUALIZERS = Registry(
+    'visualizer',
+    parent=MMENGINE_VISUALIZERS,
+    locations=['mmseg.visualization'])
 # manage visualizer backend
-VISBACKENDS = Registry('vis_backend', parent=MMENGINE_VISBACKENDS)
+VISBACKENDS = Registry(
+    'vis_backend',
+    parent=MMENGINE_VISBACKENDS,
+    locations=['mmseg.visualization'])
 
 # manage logprocessor
-LOG_PROCESSORS = Registry('log_processor', parent=MMENGINE_LOG_PROCESSORS)
+LOG_PROCESSORS = Registry(
+    'log_processor',
+    parent=MMENGINE_LOG_PROCESSORS,
+    locations=['mmseg.visualization'])
+
+# manage inferencer
+INFERENCERS = Registry('inferencer', parent=MMENGINE_INFERENCERS)
```

### Comparing `mmsegmentation-1.0.0rc5/mmseg/structures/sampler/ohem_pixel_sampler.py` & `mmsegmentation-1.0.0rc6/mmseg/structures/sampler/ohem_pixel_sampler.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/structures/seg_data_sample.py` & `mmsegmentation-1.0.0rc6/mmseg/structures/seg_data_sample.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/utils/__init__.py` & `mmsegmentation-1.0.0rc6/mmseg/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/utils/class_names.py` & `mmsegmentation-1.0.0rc6/mmseg/utils/class_names.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/utils/io.py` & `mmsegmentation-1.0.0rc6/mmseg/utils/io.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/utils/misc.py` & `mmsegmentation-1.0.0rc6/mmseg/utils/misc.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/utils/set_env.py` & `mmsegmentation-1.0.0rc6/mmseg/utils/set_env.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/utils/typing_utils.py` & `mmsegmentation-1.0.0rc6/mmseg/utils/typing_utils.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/mmseg/visualization/local_visualizer.py` & `mmsegmentation-1.0.0rc6/mmseg/visualization/local_visualizer.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 # Copyright (c) OpenMMLab. All rights reserved.
-from typing import Dict, List, Optional, Tuple, Union
+from typing import Dict, List, Optional
 
 import mmcv
 import numpy as np
 from mmengine.dist import master_only
 from mmengine.structures import PixelData
 from mmengine.visualization import Visualizer
 
@@ -20,14 +20,25 @@
         name (str): Name of the instance. Defaults to 'visualizer'.
         image (np.ndarray, optional): the origin image to draw. The format
             should be RGB. Defaults to None.
         vis_backends (list, optional): Visual backend config list.
             Defaults to None.
         save_dir (str, optional): Save file dir for all storage backends.
             If it is None, the backend storage will not save any data.
+        classes (list, optional): Input classes for result rendering, as the
+            prediction of segmentation model is a segment map with label
+            indices, `classes` is a list which includes items responding to the
+            label indices. If classes is not defined, visualizer will take
+            `cityscapes` classes by default. Defaults to None.
+        palette (list, optional): Input palette for result rendering, which is
+            a list of color palette responding to the classes. Defaults to None.
+        dataset_name (str, optional): `Dataset name or alias <https://github.com/open-mmlab/mmsegmentation/blob/dev-1.x/mmseg/utils/class_names.py#L302-L317>`_
+            visulizer will use the meta information of the dataset i.e. classes
+            and palette, but the `classes` and `palette` have higher priority.
+            Defaults to None.
         alpha (int, float): The transparency of segmentation mask.
                 Defaults to 0.8.
 
     Examples:
         >>> import numpy as np
         >>> import torch
         >>> from mmengine.structures import PixelData
@@ -45,51 +56,48 @@
         >>>     classes=('background', 'foreground'),
         >>>     palette=[[120, 120, 120], [6, 230, 230]])
         >>> seg_local_visualizer.add_datasample('visualizer_example',
         ...                         image, gt_seg_data_sample)
         >>> seg_local_visualizer.add_datasample(
         ...                        'visualizer_example', image,
         ...                         gt_seg_data_sample, show=True)
-    """
+    """ # noqa
 
     def __init__(self,
                  name: str = 'visualizer',
                  image: Optional[np.ndarray] = None,
                  vis_backends: Optional[Dict] = None,
                  save_dir: Optional[str] = None,
-                 palette: Optional[Union[str, List]] = None,
-                 classes: Optional[Union[str, List]] = None,
+                 classes: Optional[List] = None,
+                 palette: Optional[List] = None,
                  dataset_name: Optional[str] = None,
                  alpha: float = 0.8,
                  **kwargs):
         super().__init__(name, image, vis_backends, save_dir, **kwargs)
         self.alpha: float = alpha
-        # Set default value. When calling
-        # `SegLocalVisualizer().dataset_meta=xxx`,
-        # it will override the default value.
-        if dataset_name is None:
-            dataset_name = 'cityscapes'
-        classes = classes if classes else get_classes(dataset_name)
-        palette = palette if palette else get_palette(dataset_name)
-        assert len(classes) == len(
-            palette), 'The length of classes should be equal to palette'
-        self.dataset_meta: dict = {'classes': classes, 'palette': palette}
+        self.set_dataset_meta(palette, classes, dataset_name)
 
     def _draw_sem_seg(self, image: np.ndarray, sem_seg: PixelData,
-                      classes: Optional[Tuple[str]],
-                      palette: Optional[List[List[int]]]) -> np.ndarray:
+                      classes: Optional[List],
+                      palette: Optional[List]) -> np.ndarray:
         """Draw semantic seg of GT or prediction.
 
         Args:
             image (np.ndarray): The image to draw.
-            sem_seg (:obj:`PixelData`): Data structure for
-                pixel-level annotations or predictions.
-            classes (Tuple[str], optional): Category information.
-            palette (List[List[int]], optional): The palette of
-                segmentation map.
+            sem_seg (:obj:`PixelData`): Data structure for pixel-level
+                annotations or predictions.
+            classes (list, optional): Input classes for result rendering, as
+                the prediction of segmentation model is a segment map with
+                label indices, `classes` is a list which includes items
+                responding to the label indices. If classes is not defined,
+                visualizer will take `cityscapes` classes by default.
+                Defaults to None.
+            palette (list, optional): Input palette for result rendering, which
+                is a list of color palette responding to the classes.
+                Defaults to None.
 
         Returns:
             np.ndarray: the drawn image which channel is RGB.
         """
         num_classes = len(classes)
 
         sem_seg = sem_seg.cpu().data
@@ -105,14 +113,46 @@
         # draw semantic masks
         for label, color in zip(labels, colors):
             self.draw_binary_masks(
                 sem_seg == label, colors=[color], alphas=self.alpha)
 
         return self.get_image()
 
+    def set_dataset_meta(self,
+                         classes: Optional[List] = None,
+                         palette: Optional[List] = None,
+                         dataset_name: Optional[str] = None) -> None:
+        """Set meta information to visualizer.
+
+        Args:
+            classes (list, optional): Input classes for result rendering, as
+                the prediction of segmentation model is a segment map with
+                label indices, `classes` is a list which includes items
+                responding to the label indices. If classes is not defined,
+                visualizer will take `cityscapes` classes by default.
+                Defaults to None.
+            palette (list, optional): Input palette for result rendering, which
+                is a list of color palette responding to the classes.
+                Defaults to None.
+            dataset_name (str, optional): `Dataset name or alias <https://github.com/open-mmlab/mmsegmentation/blob/dev-1.x/mmseg/utils/class_names.py#L302-L317>`_
+                visulizer will use the meta information of the dataset i.e.
+                classes and palette, but the `classes` and `palette` have
+                higher priority. Defaults to None.
+        """ # noqa
+        # Set default value. When calling
+        # `SegLocalVisualizer().dataset_meta=xxx`,
+        # it will override the default value.
+        if dataset_name is None:
+            dataset_name = 'cityscapes'
+        classes = classes if classes else get_classes(dataset_name)
+        palette = palette if palette else get_palette(dataset_name)
+        assert len(classes) == len(
+            palette), 'The length of classes should be equal to palette'
+        self.dataset_meta: dict = {'classes': classes, 'palette': palette}
+
     @master_only
     def add_datasample(
             self,
             name: str,
             image: np.ndarray,
             data_sample: Optional[SegDataSample] = None,
             draw_gt: bool = True,
@@ -182,10 +222,10 @@
         else:
             drawn_img = pred_img_data
 
         if show:
             self.show(drawn_img, win_name=name, wait_time=wait_time)
 
         if out_file is not None:
-            mmcv.imwrite(drawn_img, out_file)
+            mmcv.imwrite(mmcv.bgr2rgb(drawn_img), out_file)
         else:
             self.add_image(name, drawn_img, step)
```

### Comparing `mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/PKG-INFO` & `mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mmsegmentation
-Version: 1.0.0rc5
+Version: 1.0.0rc6
 Summary: Open MMLab Semantic Segmentation Toolbox and Benchmark
 Home-page: http://github.com/open-mmlab/mmsegmentation
 Author: MMSegmentation Contributors
 Author-email: openmmlab@gmail.com
 License: Apache License 2.0
 Description: <div align="center">
           <img src="resources/mmseg-logo.png" width="600"/>
@@ -21,30 +21,44 @@
             <sup>
               <a href="https://platform.openmmlab.com">
                 <i><font size="4">TRY IT OUT</font></i>
               </a>
             </sup>
           </div>
           <div>&nbsp;</div>
-        </div>
-        <br />
         
         [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mmsegmentation)](https://pypi.org/project/mmsegmentation/)
         [![PyPI](https://img.shields.io/pypi/v/mmsegmentation)](https://pypi.org/project/mmsegmentation)
         [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmsegmentation.readthedocs.io/en/1.x/)
         [![badge](https://github.com/open-mmlab/mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/mmsegmentation/actions)
         [![codecov](https://codecov.io/gh/open-mmlab/mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmsegmentation)
         [![license](https://img.shields.io/github/license/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/1.x/LICENSE)
         [![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
         [![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
         
         Documentation: <https://mmsegmentation.readthedocs.io/en/1.x/>
         
         English | [简体中文](README_zh-CN.md)
         
+        </div>
+        
+        <div align="center">
+          <a href="https://openmmlab.medium.com/" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218352562-cdded397-b0f3-4ca1-b8dd-a60df8dca75b.png" width="3%" alt="" /></a>
+          <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+          <a href="https://discord.gg/raweFPmdzG" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218347213-c080267f-cbb6-443e-8532-8e1ed9a58ea9.png" width="3%" alt="" /></a>
+          <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+          <a href="https://twitter.com/OpenMMLab" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218346637-d30c8a0f-3eba-4699-8131-512fb06d46db.png" width="3%" alt="" /></a>
+          <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
+          <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
+            <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
+        </div>
+        
         ## Introduction
         
         MMSegmentation is an open source semantic segmentation toolbox based on PyTorch.
         It is a part of the OpenMMLab project.
         
         The 1.x branch works with **PyTorch 1.6+**.
         
@@ -66,40 +80,41 @@
         
         - **High efficiency**
         
           The training speed is faster than or comparable to other codebases.
         
         ## What's New
         
-        v1.0.0rc5 was released on 01/02/2023.
+        v1.0.0rc6 was released on 03/03/2023.
         Please refer to [changelog.md](docs/en/notes/changelog.md) for details and release history.
         
-        - Support ISNet (ICCV'2021) in projects ([#2400](https://github.com/open-mmlab/mmsegmentation/pull/2400))
-        - Support HSSN (CVPR'2022) in projects ([#2444](https://github.com/open-mmlab/mmsegmentation/pull/2444))
+        - Support MMSegInferencer ([#2413](https://github.com/open-mmlab/mmsegmentation/pull/2413), [#2658](https://github.com/open-mmlab/mmsegmentation/pull/2658))
+        - Support REFUGE dataset ([#2554](https://github.com/open-mmlab/mmsegmentation/pull/2554))
         
         ## Installation
         
         Please refer to [get_started.md](docs/en/get_started.md#installation) for installation and [dataset_prepare.md](docs/en/user_guides/2_dataset_prepare.md#prepare-datasets) for dataset preparation.
         
         ## Get Started
         
         Please see [Overview](docs/en/overview.md) for the general introduction of MMSegmentation.
         
         Please see [user guides](https://mmsegmentation.readthedocs.io/en/1.x/user_guides/index.html#) for the basic usage of MMSegmentation.
         There are also [advanced tutorials](https://mmsegmentation.readthedocs.io/en/dev-1.x/advanced_guides/index.html) for in-depth understanding of mmseg design and implementation .
         
         A Colab tutorial is also provided. You may preview the notebook [here](demo/MMSegmentation_Tutorial.ipynb) or directly [run](https://colab.research.google.com/github/open-mmlab/mmsegmentation/blob/1.x/demo/MMSegmentation_Tutorial.ipynb) on Colab.
         
-        To migrate from MMSegmentation 1.x, please refer to [migration](docs/en/migration.md).
+        To migrate from MMSegmentation 1.x, please refer to [migration](docs/en/migration).
         
         ## Benchmark and model zoo
         
         Results and models are available in the [model zoo](docs/en/model_zoo.md).
         
-        Supported backbones:
+        <details open>
+        <summary>Supported backbones:</summary>
         
         - [x] ResNet (CVPR'2016)
         - [x] ResNeXt (CVPR'2017)
         - [x] [HRNet (CVPR'2019)](configs/hrnet)
         - [x] [ResNeSt (ArXiv'2020)](configs/resnest)
         - [x] [MobileNetV2 (CVPR'2018)](configs/mobilenet_v2)
         - [x] [MobileNetV3 (ICCV'2019)](configs/mobilenet_v3)
@@ -107,15 +122,18 @@
         - [x] [Swin Transformer (ICCV'2021)](configs/swin)
         - [x] [Twins (NeurIPS'2021)](configs/twins)
         - [x] [BEiT (ICLR'2022)](configs/beit)
         - [x] [ConvNeXt (CVPR'2022)](configs/convnext)
         - [x] [MAE (CVPR'2022)](configs/mae)
         - [x] [PoolFormer (CVPR'2022)](configs/poolformer)
         
-        Supported methods:
+        </details>
+        
+        <details open>
+        <summary>Supported methods:</summary>
         
         - [x] [FCN (CVPR'2015/TPAMI'2017)](configs/fcn)
         - [x] [ERFNet (T-ITS'2017)](configs/erfnet)
         - [x] [UNet (MICCAI'2016/Nat. Methods'2019)](configs/unet)
         - [x] [PSPNet (CVPR'2017)](configs/pspnet)
         - [x] [DeepLabV3 (ArXiv'2017)](configs/deeplabv3)
         - [x] [BiSeNetV1 (ECCV'2018)](configs/bisenetv1)
@@ -146,15 +164,18 @@
         - [x] [DPT (ArXiv'2021)](configs/dpt)
         - [x] [Segmenter (ICCV'2021)](configs/segmenter)
         - [x] [SegFormer (NeurIPS'2021)](configs/segformer)
         - [x] [K-Net (NeurIPS'2021)](configs/knet)
         - [x] [MaskFormer (NeurIPS'2021)](configs/maskformer)
         - [x] [Mask2Former (CVPR'2022)](configs/mask2former)
         
-        Supported datasets:
+        </details>
+        
+        <details open>
+        <summary>Supported datasets:</summary>
         
         - [x] [Cityscapes](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#cityscapes)
         - [x] [PASCAL VOC](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-voc)
         - [x] [ADE20K](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#ade20k)
         - [x] [Pascal Context](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-context)
         - [x] [COCO-Stuff 10k](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#coco-stuff-10k)
         - [x] [COCO-Stuff 164k](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#coco-stuff-164k)
@@ -165,16 +186,22 @@
         - [x] [Dark Zurich](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#dark-zurich)
         - [x] [Nighttime Driving](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#nighttime-driving)
         - [x] [LoveDA](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#loveda)
         - [x] [Potsdam](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isprs-potsdam)
         - [x] [Vaihingen](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isprs-vaihingen)
         - [x] [iSAID](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isaid)
         
+        </details>
+        
         Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions.
         
+        ## Projects
+        
+        [Here](projects/README.md) are some implementations of SOTA models and solutions built on MMSegmentation, which are supported and maintained by community users. These projects demonstrate the best practices based on MMSegmentation for research and product development. We welcome and appreciate all the contributions to OpenMMLab ecosystem.
+        
         ## Contributing
         
         We appreciate all contributions to improve MMSegmentation. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.
         
         ## Acknowledgement
         
         MMSegmentation is an open source project that welcome any contribution and feedback.
@@ -195,15 +222,15 @@
         }
         ```
         
         ## License
         
         This project is released under the [Apache 2.0 license](LICENSE).
         
-        ## Projects in OpenMMLab
+        ## OpenMMLab Family
         
         - [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models
         - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
         - [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
         - [MMEval](https://github.com/open-mmlab/mmeval): A unified evaluation library for multiple machine learning libraries.
         - [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
         - [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
```

#### html2text {}

```diff
@@ -1,70 +1,72 @@
-Metadata-Version: 2.1 Name: mmsegmentation Version: 1.0.0rc5 Summary: Open
+Metadata-Version: 2.1 Name: mmsegmentation Version: 1.0.0rc6 Summary: Open
 MMLab Semantic Segmentation Toolbox and Benchmark Home-page: http://github.com/
 open-mmlab/mmsegmentation Author: MMSegmentation Contributors Author-email:
 openmmlab@gmail.com License: Apache License 2.0 Description:
                           [resources/mmseg-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
-
-[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/
-mmsegmentation)](https://pypi.org/project/mmsegmentation/) [![PyPI](https://
+       [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/
+ mmsegmentation)](https://pypi.org/project/mmsegmentation/) [![PyPI](https://
 img.shields.io/pypi/v/mmsegmentation)](https://pypi.org/project/mmsegmentation)
-[![docs](https://img.shields.io/badge/docs-latest-blue)](https://
+       [![docs](https://img.shields.io/badge/docs-latest-blue)](https://
 mmsegmentation.readthedocs.io/en/1.x/) [![badge](https://github.com/open-mmlab/
-mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/
-mmsegmentation/actions) [![codecov](https://codecov.io/gh/open-mmlab/
-mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-
-mmlab/mmsegmentation) [![license](https://img.shields.io/github/license/open-
-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/
+   mmsegmentation/workflows/build/badge.svg)](https://github.com/open-mmlab/
+     mmsegmentation/actions) [![codecov](https://codecov.io/gh/open-mmlab/
+  mmsegmentation/branch/master/graph/badge.svg)](https://codecov.io/gh/open-
+ mmlab/mmsegmentation) [![license](https://img.shields.io/github/license/open-
+ mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/blob/
 1.x/LICENSE) [![issue resolution](https://isitmaintained.com/badge/resolution/
-open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/
-issues) [![open issues](https://isitmaintained.com/badge/open/open-mmlab/
-mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
-Documentation:
-mmsegmentation.readthedocs.io/en/1.x/> English | [ç®ä½ä¸­æ](README_zh-
-CN.md) ## Introduction MMSegmentation is an open source semantic segmentation
-toolbox based on PyTorch. It is a part of the OpenMMLab project. The 1.x branch
-works with **PyTorch 1.6+**. ![demo image](resources/seg_demo.gif) ### Major
-features - **Unified Benchmark** We provide a unified benchmark toolbox for
-various semantic segmentation methods. - **Modular Design** We decompose the
-semantic segmentation framework into different components and one can easily
-construct a customized semantic segmentation framework by combining different
-modules. - **Support of multiple methods out of box** The toolbox directly
-supports popular and contemporary semantic segmentation frameworks, *e.g.*
-PSPNet, DeepLabV3, PSANet, DeepLabV3+, etc. - **High efficiency** The training
-speed is faster than or comparable to other codebases. ## What's New v1.0.0rc5
-was released on 01/02/2023. Please refer to [changelog.md](docs/en/notes/
-changelog.md) for details and release history. - Support ISNet (ICCV'2021) in
-projects ([#2400](https://github.com/open-mmlab/mmsegmentation/pull/2400)) -
-Support HSSN (CVPR'2022) in projects ([#2444](https://github.com/open-mmlab/
-mmsegmentation/pull/2444)) ## Installation Please refer to [get_started.md]
-(docs/en/get_started.md#installation) for installation and [dataset_prepare.md]
-(docs/en/user_guides/2_dataset_prepare.md#prepare-datasets) for dataset
-preparation. ## Get Started Please see [Overview](docs/en/overview.md) for the
-general introduction of MMSegmentation. Please see [user guides](https://
+ open-mmlab/mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/
+   issues) [![open issues](https://isitmaintained.com/badge/open/open-mmlab/
+   mmsegmentation.svg)](https://github.com/open-mmlab/mmsegmentation/issues)
+                                Documentation:
+  mmsegmentation.readthedocs.io/en/1.x/> English | [ç®ä½ä¸­æ](README_zh-
+                                    CN.md)
+
+## Introduction MMSegmentation is an open source semantic segmentation toolbox
+based on PyTorch. It is a part of the OpenMMLab project. The 1.x branch works
+with **PyTorch 1.6+**. ![demo image](resources/seg_demo.gif) ### Major features
+- **Unified Benchmark** We provide a unified benchmark toolbox for various
+semantic segmentation methods. - **Modular Design** We decompose the semantic
+segmentation framework into different components and one can easily construct a
+customized semantic segmentation framework by combining different modules. -
+**Support of multiple methods out of box** The toolbox directly supports
+popular and contemporary semantic segmentation frameworks, *e.g.* PSPNet,
+DeepLabV3, PSANet, DeepLabV3+, etc. - **High efficiency** The training speed is
+faster than or comparable to other codebases. ## What's New v1.0.0rc6 was
+released on 03/03/2023. Please refer to [changelog.md](docs/en/notes/
+changelog.md) for details and release history. - Support MMSegInferencer (
+[#2413](https://github.com/open-mmlab/mmsegmentation/pull/2413), [#2658](https:
+//github.com/open-mmlab/mmsegmentation/pull/2658)) - Support REFUGE dataset (
+[#2554](https://github.com/open-mmlab/mmsegmentation/pull/2554)) ##
+Installation Please refer to [get_started.md](docs/en/
+get_started.md#installation) for installation and [dataset_prepare.md](docs/en/
+user_guides/2_dataset_prepare.md#prepare-datasets) for dataset preparation. ##
+Get Started Please see [Overview](docs/en/overview.md) for the general
+introduction of MMSegmentation. Please see [user guides](https://
 mmsegmentation.readthedocs.io/en/1.x/user_guides/index.html#) for the basic
 usage of MMSegmentation. There are also [advanced tutorials](https://
 mmsegmentation.readthedocs.io/en/dev-1.x/advanced_guides/index.html) for in-
 depth understanding of mmseg design and implementation . A Colab tutorial is
 also provided. You may preview the notebook [here](demo/
 MMSegmentation_Tutorial.ipynb) or directly [run](https://
 colab.research.google.com/github/open-mmlab/mmsegmentation/blob/1.x/demo/
 MMSegmentation_Tutorial.ipynb) on Colab. To migrate from MMSegmentation 1.x,
-please refer to [migration](docs/en/migration.md). ## Benchmark and model zoo
+please refer to [migration](docs/en/migration). ## Benchmark and model zoo
 Results and models are available in the [model zoo](docs/en/model_zoo.md).
 Supported backbones: - [x] ResNet (CVPR'2016) - [x] ResNeXt (CVPR'2017) - [x]
 [HRNet (CVPR'2019)](configs/hrnet) - [x] [ResNeSt (ArXiv'2020)](configs/
 resnest) - [x] [MobileNetV2 (CVPR'2018)](configs/mobilenet_v2) - [x]
 [MobileNetV3 (ICCV'2019)](configs/mobilenet_v3) - [x] [Vision Transformer
 (ICLR'2021)](configs/vit) - [x] [Swin Transformer (ICCV'2021)](configs/swin) -
 [x] [Twins (NeurIPS'2021)](configs/twins) - [x] [BEiT (ICLR'2022)](configs/
 beit) - [x] [ConvNeXt (CVPR'2022)](configs/convnext) - [x] [MAE (CVPR'2022)]
-(configs/mae) - [x] [PoolFormer (CVPR'2022)](configs/poolformer) Supported
+(configs/mae) - [x] [PoolFormer (CVPR'2022)](configs/poolformer)   Supported
 methods: - [x] [FCN (CVPR'2015/TPAMI'2017)](configs/fcn) - [x] [ERFNet (T-
 ITS'2017)](configs/erfnet) - [x] [UNet (MICCAI'2016/Nat. Methods'2019)]
 (configs/unet) - [x] [PSPNet (CVPR'2017)](configs/pspnet) - [x] [DeepLabV3
 (ArXiv'2017)](configs/deeplabv3) - [x] [BiSeNetV1 (ECCV'2018)](configs/
 bisenetv1) - [x] [PSANet (ECCV'2018)](configs/psanet) - [x] [DeepLabV3+
 (CVPR'2018)](configs/deeplabv3plus) - [x] [UPerNet (ECCV'2018)](configs/
 upernet) - [x] [ICNet (ECCV'2018)](configs/icnet) - [x] [NonLocal Net
@@ -79,16 +81,16 @@
 (configs/ocrnet) - [x] [DNLNet (ECCV'2020)](configs/dnlnet) - [x] [PointRend
 (CVPR'2020)](configs/point_rend) - [x] [CGNet (TIP'2020)](configs/cgnet) - [x]
 [BiSeNetV2 (IJCV'2021)](configs/bisenetv2) - [x] [STDC (CVPR'2021)](configs/
 stdc) - [x] [SETR (CVPR'2021)](configs/setr) - [x] [DPT (ArXiv'2021)](configs/
 dpt) - [x] [Segmenter (ICCV'2021)](configs/segmenter) - [x] [SegFormer
 (NeurIPS'2021)](configs/segformer) - [x] [K-Net (NeurIPS'2021)](configs/knet) -
 [x] [MaskFormer (NeurIPS'2021)](configs/maskformer) - [x] [Mask2Former
-(CVPR'2022)](configs/mask2former) Supported datasets: - [x] [Cityscapes](https:
-//github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
+(CVPR'2022)](configs/mask2former)   Supported datasets: - [x] [Cityscapes]
+(https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#cityscapes) - [x] [PASCAL VOC](https://github.com/open-
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#pascal-
 voc) - [x] [ADE20K](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/
 en/user_guides/2_dataset_prepare.md#ade20k) - [x] [Pascal Context](https://
 github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#pascal-context) - [x] [COCO-Stuff 10k](https://github.com/
 open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
@@ -108,59 +110,63 @@
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#loveda)
 - [x] [Potsdam](https://github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/
 user_guides/2_dataset_prepare.md#isprs-potsdam) - [x] [Vaihingen](https://
 github.com/open-mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/
 2_dataset_prepare.md#isprs-vaihingen) - [x] [iSAID](https://github.com/open-
 mmlab/mmsegmentation/blob/1.x/docs/en/user_guides/2_dataset_prepare.md#isaid)
 Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions. ##
-Contributing We appreciate all contributions to improve MMSegmentation. Please
-refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing
-guideline. ## Acknowledgement MMSegmentation is an open source project that
-welcome any contribution and feedback. We wish that the toolbox and benchmark
-could serve the growing research community by providing a flexible as well as
-standardized toolkit to reimplement existing methods and develop their own new
-semantic segmentation methods. ## Citation If you find this project useful in
-your research, please consider cite: ```bibtex @misc{mmseg2020, title={
-{MMSegmentation}: OpenMMLab Semantic Segmentation Toolbox and Benchmark},
-author={MMSegmentation Contributors}, howpublished = {\url{https://github.com/
-open-mmlab/mmsegmentation}}, year={2020} } ``` ## License This project is
-released under the [Apache 2.0 license](LICENSE). ## Projects in OpenMMLab -
-[MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational
-library for training deep learning models - [MMCV](https://github.com/open-
-mmlab/mmcv): OpenMMLab foundational library for computer vision. - [MIM](https:
-//github.com/open-mmlab/mim): MIM installs OpenMMLab packages. - [MMEval]
-(https://github.com/open-mmlab/mmeval): A unified evaluation library for
-multiple machine learning libraries. - [MMClassification](https://github.com/
-open-mmlab/mmclassification): OpenMMLab image classification toolbox and
-benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection):
-OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
-github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for
-general 3D object detection. - [MMRotate](https://github.com/open-mmlab/
-mmrotate): OpenMMLab rotated object detection toolbox and benchmark. - [MMYOLO]
-(https://github.com/open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and
-benchmark. - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation):
-OpenMMLab semantic segmentation toolbox and benchmark. - [MMOCR](https://
-github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and
-understanding toolbox. - [MMPose](https://github.com/open-mmlab/mmpose):
-OpenMMLab pose estimation toolbox and benchmark. - [MMHuman3D](https://
-github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox
-and benchmark. - [MMSelfSup](https://github.com/open-mmlab/mmselfsup):
-OpenMMLab self-supervised learning toolbox and benchmark. - [MMRazor](https://
-github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and
-benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab
-fewshot learning toolbox and benchmark. - [MMAction2](https://github.com/open-
-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and
-benchmark. - [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab
-video perception toolbox and benchmark. - [MMFlow](https://github.com/open-
-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark. - [MMEditing]
-(https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing
-toolbox. - [MMGeneration](https://github.com/open-mmlab/mmgeneration):
-OpenMMLab image and video generative models toolbox. - [MMDeploy](https://
-github.com/open-mmlab/mmdeploy): OpenMMLab Model Deployment Framework.
-Keywords: computer vision,semantic segmentation Platform: UNKNOWN Classifier:
-Development Status :: 4 - Beta Classifier: License :: OSI Approved :: Apache
-Software License Classifier: Operating System :: OS Independent Classifier:
-Programming Language :: Python :: 3.6 Classifier: Programming Language ::
-Python :: 3.7 Classifier: Programming Language :: Python :: 3.8 Classifier:
-Programming Language :: Python :: 3.9 Description-Content-Type: text/markdown
-Provides-Extra: all Provides-Extra: tests Provides-Extra: optional Provides-
-Extra: mim
+Projects [Here](projects/README.md) are some implementations of SOTA models and
+solutions built on MMSegmentation, which are supported and maintained by
+community users. These projects demonstrate the best practices based on
+MMSegmentation for research and product development. We welcome and appreciate
+all the contributions to OpenMMLab ecosystem. ## Contributing We appreciate all
+contributions to improve MMSegmentation. Please refer to [CONTRIBUTING.md]
+(.github/CONTRIBUTING.md) for the contributing guideline. ## Acknowledgement
+MMSegmentation is an open source project that welcome any contribution and
+feedback. We wish that the toolbox and benchmark could serve the growing
+research community by providing a flexible as well as standardized toolkit to
+reimplement existing methods and develop their own new semantic segmentation
+methods. ## Citation If you find this project useful in your research, please
+consider cite: ```bibtex @misc{mmseg2020, title={{MMSegmentation}: OpenMMLab
+Semantic Segmentation Toolbox and Benchmark}, author={MMSegmentation
+Contributors}, howpublished = {\url{https://github.com/open-mmlab/
+mmsegmentation}}, year={2020} } ``` ## License This project is released under
+the [Apache 2.0 license](LICENSE). ## OpenMMLab Family - [MMEngine](https://
+github.com/open-mmlab/mmengine): OpenMMLab foundational library for training
+deep learning models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab
+foundational library for computer vision. - [MIM](https://github.com/open-
+mmlab/mim): MIM installs OpenMMLab packages. - [MMEval](https://github.com/
+open-mmlab/mmeval): A unified evaluation library for multiple machine learning
+libraries. - [MMClassification](https://github.com/open-mmlab/
+mmclassification): OpenMMLab image classification toolbox and benchmark. -
+[MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
+toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
+mmdetection3d): OpenMMLab's next-generation platform for general 3D object
+detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
+rotated object detection toolbox and benchmark. - [MMYOLO](https://github.com/
+open-mmlab/mmyolo): OpenMMLab YOLO series toolbox and benchmark. -
+[MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab
+semantic segmentation toolbox and benchmark. - [MMOCR](https://github.com/open-
+mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
+- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation
+toolbox and benchmark. - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d):
+OpenMMLab 3D human parametric model toolbox and benchmark. - [MMSelfSup](https:
+//github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox
+and benchmark. - [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab
+model compression toolbox and benchmark. - [MMFewShot](https://github.com/open-
+mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark. -
+[MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-
+generation action understanding toolbox and benchmark. - [MMTracking](https://
+github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and
+benchmark. - [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical
+flow toolbox and benchmark. - [MMEditing](https://github.com/open-mmlab/
+mmediting): OpenMMLab image and video editing toolbox. - [MMGeneration](https:/
+/github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative
+models toolbox. - [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab
+Model Deployment Framework. Keywords: computer vision,semantic segmentation
+Platform: UNKNOWN Classifier: Development Status :: 4 - Beta Classifier:
+License :: OSI Approved :: Apache Software License Classifier: Operating System
+:: OS Independent Classifier: Programming Language :: Python :: 3.6 Classifier:
+Programming Language :: Python :: 3.7 Classifier: Programming Language ::
+Python :: 3.8 Classifier: Programming Language :: Python :: 3.9 Description-
+Content-Type: text/markdown Provides-Extra: all Provides-Extra: tests Provides-
+Extra: optional Provides-Extra: mim
```

### Comparing `mmsegmentation-1.0.0rc5/mmsegmentation.egg-info/SOURCES.txt` & `mmsegmentation-1.0.0rc6/mmsegmentation.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 mmseg/.mim/configs/_base_/datasets/isaid.py
 mmseg/.mim/configs/_base_/datasets/loveda.py
 mmseg/.mim/configs/_base_/datasets/pascal_context.py
 mmseg/.mim/configs/_base_/datasets/pascal_context_59.py
 mmseg/.mim/configs/_base_/datasets/pascal_voc12.py
 mmseg/.mim/configs/_base_/datasets/pascal_voc12_aug.py
 mmseg/.mim/configs/_base_/datasets/potsdam.py
+mmseg/.mim/configs/_base_/datasets/refuge.py
 mmseg/.mim/configs/_base_/datasets/stare.py
 mmseg/.mim/configs/_base_/datasets/synapse.py
 mmseg/.mim/configs/_base_/datasets/vaihingen.py
 mmseg/.mim/configs/_base_/models/ann_r50-d8.py
 mmseg/.mim/configs/_base_/models/apcnet_r50-d8.py
 mmseg/.mim/configs/_base_/models/bisenetv1_r18-d32.py
 mmseg/.mim/configs/_base_/models/bisenetv2.py
@@ -792,26 +793,28 @@
 mmseg/.mim/tools/dist_train.sh
 mmseg/.mim/tools/slurm_test.sh
 mmseg/.mim/tools/slurm_train.sh
 mmseg/.mim/tools/test.py
 mmseg/.mim/tools/train.py
 mmseg/.mim/tools/analysis_tools/analyze_logs.py
 mmseg/.mim/tools/analysis_tools/benchmark.py
+mmseg/.mim/tools/analysis_tools/browse_dataset.py
 mmseg/.mim/tools/analysis_tools/confusion_matrix.py
 mmseg/.mim/tools/analysis_tools/get_flops.py
 mmseg/.mim/tools/dataset_converters/chase_db1.py
 mmseg/.mim/tools/dataset_converters/cityscapes.py
 mmseg/.mim/tools/dataset_converters/coco_stuff10k.py
 mmseg/.mim/tools/dataset_converters/coco_stuff164k.py
 mmseg/.mim/tools/dataset_converters/drive.py
 mmseg/.mim/tools/dataset_converters/hrf.py
 mmseg/.mim/tools/dataset_converters/isaid.py
 mmseg/.mim/tools/dataset_converters/loveda.py
 mmseg/.mim/tools/dataset_converters/pascal_context.py
 mmseg/.mim/tools/dataset_converters/potsdam.py
+mmseg/.mim/tools/dataset_converters/refuge.py
 mmseg/.mim/tools/dataset_converters/stare.py
 mmseg/.mim/tools/dataset_converters/synapse.py
 mmseg/.mim/tools/dataset_converters/vaihingen.py
 mmseg/.mim/tools/dataset_converters/voc_aug.py
 mmseg/.mim/tools/deployment/pytorch2torchscript.py
 mmseg/.mim/tools/misc/browse_dataset.py
 mmseg/.mim/tools/misc/print_config.py
@@ -824,14 +827,15 @@
 mmseg/.mim/tools/model_converters/vit2mmseg.py
 mmseg/.mim/tools/model_converters/vitjax2mmseg.py
 mmseg/.mim/tools/torchserve/mmseg2torchserve.py
 mmseg/.mim/tools/torchserve/mmseg_handler.py
 mmseg/.mim/tools/torchserve/test_torchserve.py
 mmseg/apis/__init__.py
 mmseg/apis/inference.py
+mmseg/apis/mmseg_inferencer.py
 mmseg/datasets/__init__.py
 mmseg/datasets/ade.py
 mmseg/datasets/basesegdataset.py
 mmseg/datasets/chase_db1.py
 mmseg/datasets/cityscapes.py
 mmseg/datasets/coco_stuff.py
 mmseg/datasets/dark_zurich.py
@@ -842,14 +846,15 @@
 mmseg/datasets/isaid.py
 mmseg/datasets/isprs.py
 mmseg/datasets/lip.py
 mmseg/datasets/loveda.py
 mmseg/datasets/night_driving.py
 mmseg/datasets/pascal_context.py
 mmseg/datasets/potsdam.py
+mmseg/datasets/refuge.py
 mmseg/datasets/stare.py
 mmseg/datasets/synapse.py
 mmseg/datasets/voc.py
 mmseg/datasets/transforms/__init__.py
 mmseg/datasets/transforms/formatting.py
 mmseg/datasets/transforms/loading.py
 mmseg/datasets/transforms/transforms.py
```

### Comparing `mmsegmentation-1.0.0rc5/setup.cfg` & `mmsegmentation-1.0.0rc6/setup.cfg`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/setup.py` & `mmsegmentation-1.0.0rc6/setup.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_config.py` & `mmsegmentation-1.0.0rc6/tests/test_config.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,18 +2,18 @@
 import glob
 import os
 from os.path import dirname, exists, isdir, join, relpath
 
 import numpy as np
 from mmengine import Config
 from mmengine.dataset import Compose
+from mmengine.registry import init_default_scope
 from torch import nn
 
 from mmseg.models import build_segmentor
-from mmseg.utils import register_all_modules
 
 
 def _get_config_directory():
     """Find the predefined segmentor config directory."""
     try:
         # Assume we are running in the source mmsegmentation repo
         repo_dpath = dirname(dirname(__file__))
@@ -66,15 +66,15 @@
 def test_config_data_pipeline():
     """Test whether the data pipeline is valid and can process corner cases.
 
     CommandLine:
         xdoctest -m tests/test_config.py test_config_build_data_pipeline
     """
 
-    register_all_modules()
+    init_default_scope('mmseg')
     config_dpath = _get_config_directory()
     print(f'Found config_dpath = {config_dpath!r}')
 
     import glob
     config_fpaths = list(glob.glob(join(config_dpath, '**', '*.py')))
     config_fpaths = [p for p in config_fpaths if p.find('_base_') == -1]
     config_names = [relpath(p, config_dpath) for p in config_fpaths]
```

### Comparing `mmsegmentation-1.0.0rc5/tests/test_digit_version.py` & `mmsegmentation-1.0.0rc6/tests/test_digit_version.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_beit.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_beit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_bisenetv1.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_bisenetv1.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_bisenetv2.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_bisenetv2.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_blocks.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_blocks.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_cgnet.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_cgnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_erfnet.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_erfnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_fast_scnn.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_fast_scnn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_hrnet.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_hrnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_icnet.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_icnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_mae.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_mae.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_mit.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_mit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_mobilenet_v3.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_mobilenet_v3.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_resnest.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_resnest.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_resnet.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_resnet.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_resnext.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_resnext.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_stdc.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_stdc.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_swin.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_swin.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_timm_backbone.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_timm_backbone.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_twins.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_twins.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_unet.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_unet.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import pytest
 import torch
 from mmcv.cnn import ConvModule
+from mmengine.registry import init_default_scope
 
 from mmseg.models.backbones.unet import (BasicConvBlock, DeconvModule,
                                          InterpConv, UNet, UpConvBlock)
 from mmseg.models.utils import Upsample
-from mmseg.utils import register_all_modules
 from .utils import check_norm_state
 
-register_all_modules()
+init_default_scope('mmseg')
 
 
 def test_unet_basic_conv_block():
     with pytest.raises(AssertionError):
         # Not implemented yet.
         dcn = dict(type='DCN', deform_groups=1, fallback_on_stride=False)
         BasicConvBlock(64, 64, dcn=dcn)
```

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/test_vit.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/test_vit.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_backbones/utils.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_backbones/utils.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_data_preprocessor.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_data_preprocessor.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_forward.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_forward.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,22 +5,22 @@
 from unittest.mock import patch
 
 import numpy as np
 import pytest
 import torch
 import torch.nn as nn
 from mmengine.model.utils import revert_sync_batchnorm
+from mmengine.registry import init_default_scope
 from mmengine.structures import PixelData
 from mmengine.utils import is_list_of, is_tuple_of
 from torch import Tensor
 
 from mmseg.structures import SegDataSample
-from mmseg.utils import register_all_modules
 
-register_all_modules()
+init_default_scope('mmseg')
 
 
 def _demo_mm_inputs(batch_size=2, image_shapes=(3, 32, 32), num_classes=5):
     """Create a superset of inputs needed to run test or train batches.
 
     Args:
         batch_size (int): batch size. Default to 2.
```

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_ann_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_ann_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_apc_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_apc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_aspp_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_aspp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_cc_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_cc_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_decode_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_decode_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_dm_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_dm_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_dnl_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_dnl_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_dpt_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_dpt_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_ema_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_ema_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_fcn_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_fcn_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_isa_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_isa_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_lraspp_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_lraspp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_mask2former_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_mask2former_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_maskformer_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_maskformer_head.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from os.path import dirname, join
 
 import torch
 from mmengine import Config
+from mmengine.registry import init_default_scope
 from mmengine.structures import PixelData
 
 from mmseg.registry import MODELS
 from mmseg.structures import SegDataSample
-from mmseg.utils import register_all_modules
 
 
 def test_maskformer_head():
-    register_all_modules()
+    init_default_scope('mmseg')
     repo_dpath = dirname(dirname(__file__))
     cfg = Config.fromfile(
         join(
             repo_dpath,
             '../../configs/maskformer/maskformer_r50-d32_8xb2-160k_ade20k-512x512.py'  # noqa
         ))
     cfg.model.train_cfg = None
```

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_ocr_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_ocr_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_psa_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_psa_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_psp_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_psp_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_segformer_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_segformer_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_segmenter_mask_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_segmenter_mask_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_setr_mla_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_setr_mla_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_setr_up_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_setr_up_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/test_uper_head.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/test_uper_head.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_heads/utils.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_heads/utils.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_feature2pyramid.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_feature2pyramid.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_fpn.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_fpn.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_ic_neck.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_ic_neck.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_jpu.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_jpu.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_mla_neck.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_mla_neck.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_necks/test_multilevel_neck.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_necks/test_multilevel_neck.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/test_cascade_encoder_decoder.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/test_cascade_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/test_encoder_decoder.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/test_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/test_seg_tta_model.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/test_seg_tta_model.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import torch
 from mmengine import ConfigDict
 from mmengine.model import BaseTTAModel
+from mmengine.registry import init_default_scope
 from mmengine.structures import PixelData
 
 from mmseg.registry import MODELS
 from mmseg.structures import SegDataSample
-from mmseg.utils import register_all_modules
 from .utils import *  # noqa: F401,F403
 
-register_all_modules()
+init_default_scope('mmseg')
 
 
 def test_encoder_decoder_tta():
 
     segmentor_cfg = ConfigDict(
         type='EncoderDecoder',
         backbone=dict(type='ExampleBackbone'),
```

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_segmentors/utils.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_segmentors/utils.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_utils/test_embed.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_utils/test_embed.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_models/test_utils/test_shape_convert.py` & `mmsegmentation-1.0.0rc6/tests/test_models/test_utils/test_shape_convert.py`

 * *Files identical despite different names*

### Comparing `mmsegmentation-1.0.0rc5/tests/test_sampler.py` & `mmsegmentation-1.0.0rc6/tests/test_sampler.py`

 * *Files identical despite different names*

