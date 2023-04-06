# Comparing `tmp/mmocr-1.0.0rc5.tar.gz` & `tmp/mmocr-1.0.0rc6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/mmocr-1.0.0rc5.tar", last modified: Fri Jan  6 09:36:05 2023, max compression
+gzip compressed data, was "dist/mmocr-1.0.0rc6.tar", last modified: Tue Mar  7 12:27:59 2023, max compression
```

## Comparing `mmocr-1.0.0rc5.tar` & `mmocr-1.0.0rc6.tar`

### file list

```diff
@@ -1,537 +1,566 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/
--rw-r--r--   0 runner    (1001) docker     (123)      155 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    16575 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    13749 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/backbone/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/backbone/oclip/
--rw-r--r--   0 runner    (1001) docker     (123)      420 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/backbone/oclip/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      732 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/datasets/wildreceipt-openset.py
--rw-r--r--   0 runner    (1001) docker     (123)      452 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/datasets/wildreceipt.py
--rw-r--r--   0 runner    (1001) docker     (123)      907 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/default_runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/schedules/
--rw-r--r--   0 runner    (1001) docker     (123)      346 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/schedules/schedule_adam_60e.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/
--rw-r--r--   0 runner    (1001) docker     (123)      937 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_novisual.py
--rw-r--r--   0 runner    (1001) docker     (123)      822 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_unet16.py
--rw-r--r--   0 runner    (1001) docker     (123)      852 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2051 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt-openset.py
--rw-r--r--   0 runner    (1001) docker     (123)      786 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt.py
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      506 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      519 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/icdar2017.py
--rw-r--r--   0 runner    (1001) docker     (123)      518 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/synthtext.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/totaltext.py
--rw-r--r--   0 runner    (1001) docker     (123)      476 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/toy_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/default_runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/schedules/
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/schedules/schedule_adam_600e.py
--rw-r--r--   0 runner    (1001) docker     (123)      365 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_100k.py
--rw-r--r--   0 runner    (1001) docker     (123)      379 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_1200e.py
--rw-r--r--   0 runner    (1001) docker     (123)      558 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/
--rw-r--r--   0 runner    (1001) docker     (123)     2159 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet18_fpnc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2290 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet50-dcnv2_fpnc.py
--rw-r--r--   0 runner    (1001) docker     (123)      859 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_100k_synthtext.py
--rw-r--r--   0 runner    (1001) docker     (123)      860 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     2314 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_totaltext.py
--rw-r--r--   0 runner    (1001) docker     (123)      865 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_100k_synthtext.py
--rw-r--r--   0 runner    (1001) docker     (123)     1041 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      525 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-oclip_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      623 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     2832 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/
--rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/_base_dbnetpp_resnet50-dcnv2_fpnc.py
--rw-r--r--   0 runner    (1001) docker     (123)      895 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_100k_synthtext.py
--rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      527 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-oclip_fpnc_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50_fpnc_1200e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/
--rw-r--r--   0 runner    (1001) docker     (123)     2992 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/_base_drrg_resnet50_fpn-unet.py
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/drrg_resnet50-oclip_fpn-unet_1200e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/drrg_resnet50_fpn-unet_1200e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/
--rw-r--r--   0 runner    (1001) docker     (123)      512 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50-dcnv2_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)     1687 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-dcnv2_fpn_1500e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      401 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-oclip_fpn_1500e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-oclip_fpn_1500e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     3322 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_totaltext.py
--rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/
--rw-r--r--   0 runner    (1001) docker     (123)     1890 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/_base_mask-rcnn_resnet50_fpn.py
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      354 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)     1125 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      507 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2017.py
--rw-r--r--   0 runner    (1001) docker     (123)     2425 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/
--rw-r--r--   0 runner    (1001) docker     (123)     2730 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/_base_panet_resnet18_fpem-ffm.py
--rw-r--r--   0 runner    (1001) docker     (123)      547 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/_base_panet_resnet50_fpem-ffm.py
--rw-r--r--   0 runner    (1001) docker     (123)     1380 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2608 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/panet_resnet50_fpem-ffm_600e_icdar2017.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/
--rw-r--r--   0 runner    (1001) docker     (123)     2286 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/_base_psenet_resnet50_fpnf.py
--rw-r--r--   0 runner    (1001) docker     (123)     2233 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50-oclip_fpnf_600e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      267 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50-oclip_fpnf_600e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2017.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/
--rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/_base_textsnake_resnet50_fpn-unet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/textsnake_resnet50-oclip_fpn-unet_1200e_ctw1500.py
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/textsnake_resnet50_fpn-unet_1200e_ctw1500.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/coco_text_v1.py
--rw-r--r--   0 runner    (1001) docker     (123)      214 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/cute80.py
--rw-r--r--   0 runner    (1001) docker     (123)      232 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2011.py
--rw-r--r--   0 runner    (1001) docker     (123)      570 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2013.py
--rw-r--r--   0 runner    (1001) docker     (123)      572 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2015.py
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/iiit5k.py
--rw-r--r--   0 runner    (1001) docker     (123)      529 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/mjsynth.py
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/svt.py
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/svtp.py
--rw-r--r--   0 runner    (1001) docker     (123)      825 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/synthtext.py
--rw-r--r--   0 runner    (1001) docker     (123)      247 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/synthtext_add.py
--rw-r--r--   0 runner    (1001) docker     (123)      407 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/totaltext.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      410 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/toy_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     1284 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/default_runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/schedules/
--rw-r--r--   0 runner    (1001) docker     (123)      306 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adadelta_5e.py
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adam_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      327 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adam_step_5e.py
--rw-r--r--   0 runner    (1001) docker     (123)      492 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adamw_cos_6e.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/
--rw-r--r--   0 runner    (1001) docker     (123)     3499 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/_base_abinet-vision.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/_base_abinet.py
--rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/abinet-vision_20e_st-an_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     1893 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/abinet_20e_st-an_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     2923 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/aster/
--rw-r--r--   0 runner    (1001) docker     (123)     2187 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/aster/_base_aster.py
--rw-r--r--   0 runner    (1001) docker     (123)     1648 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/aster/aster_resnet45_6e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     1434 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/aster/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/
--rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/_base_crnn_mini-vgg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_toy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1402 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/
--rw-r--r--   0 runner    (1001) docker     (123)     3457 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/_base_master_resnet31.py
--rw-r--r--   0 runner    (1001) docker     (123)     1827 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_st_mj_sa.py
--rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_toy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1477 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/
--rw-r--r--   0 runner    (1001) docker     (123)     1863 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_modality-transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     2026 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_resnet31.py
--rw-r--r--   0 runner    (1001) docker     (123)     3457 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1663 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_toy.py
--rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_resnet31-1by16-1by8_6e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)      109 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_resnet31-1by8-1by4_6e_st_mj.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/
--rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/_base_robustscanner_resnet31.py
--rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_st-sub_mj-sub_sa_real.py
--rw-r--r--   0 runner    (1001) docker     (123)      997 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_toy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/
--rwxr-xr-x   0 runner    (1001) docker     (123)     2086 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/_base_sar_resnet31_parallel-decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2852 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2225 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_st-sub_mj-sub_sa_real.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1000 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_toy.py
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/sar_resnet31_sequential-decoder_5e_st-sub_mj-sub_sa_real.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/
--rw-r--r--   0 runner    (1001) docker     (123)     2040 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/_base_satrn_shallow.py
--rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      547 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/satrn_shallow-small_5e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/satrn_shallow_5e_st_mj.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/
--rw-r--r--   0 runner    (1001) docker     (123)     1146 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/_base_svtr-tiny.py
--rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      431 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/svtr-base_20e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)      488 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/svtr-large_20e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)      218 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/svtr-small_20e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)     4272 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/svtr-tiny_20e_st_mj.py
--rw-r--r--   0 runner    (1001) docker     (123)      740 2023-01-06 09:36:04.000000 mmocr-1.0.0rc5/mmocr/.mim/model-index.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/
--rw-r--r--   0 runner    (1001) docker     (123)    14649 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/browse_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/get_flops.py
--rw-r--r--   0 runner    (1001) docker     (123)     1562 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/offline_eval.py
--rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/print_config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/common/
--rw-r--r--   0 runner    (1001) docker     (123)     4417 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/common/curvedsyntext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2626 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/common/extract_kaist.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/kie/
--rw-r--r--   0 runner    (1001) docker     (123)     4422 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/kie/closeset_to_openset.py
--rw-r--r--   0 runner    (1001) docker     (123)     1898 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/prepare_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/
--rw-r--r--   0 runner    (1001) docker     (123)     4437 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/art_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5319 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/bid_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1933 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/coco_to_line_dict.py
--rw-r--r--   0 runner    (1001) docker     (123)     4162 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/cocotext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7279 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ctw1500_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2047 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/data_migrator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4578 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/detext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4507 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/funsd_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5132 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/hiertext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4879 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ic11_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4748 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ic13_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5837 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/icdar_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5951 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ilst_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4739 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/imgur_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6152 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/kaist_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4055 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/lsvt_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5317 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/lv_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6153 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/mtwi_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5932 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/naf_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5771 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/rctw_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5984 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/rects_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4760 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/sroie_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6177 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/synthtext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/textocr_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)    11836 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/totaltext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5014 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/vintext_converter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/
--rw-r--r--   0 runner    (1001) docker     (123)     3106 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/art_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7592 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/bid_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5647 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/cocotext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3375 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/data_migrator.py
--rw-r--r--   0 runner    (1001) docker     (123)     6481 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/detext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6265 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/funsd_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7696 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/hiertext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1802 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/ic11_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/ic13_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     8074 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/ilst_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5385 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/imgur_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     8392 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/kaist_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5606 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/lmdb_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5743 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/lsvt_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2078 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/lv_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7955 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/mtwi_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     8909 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/naf_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4042 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/openvino_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7464 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/rctw_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     7856 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/rects_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/sroie_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2873 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/svt_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     4787 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/synthtext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3576 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/textocr_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)    11642 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/totaltext_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6812 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/vintext_converter.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      479 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dist_test.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      443 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/dist_train.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/model_converters/
--rwxr-xr-x   0 runner    (1001) docker     (123)     1201 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/model_converters/publish_model.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      485 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/slurm_test.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      622 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/slurm_train.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)     4967 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/test.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4239 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/.mim/tools/train.py
--rw-r--r--   0 runner    (1001) docker     (123)     1535 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/apis/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/
--rw-r--r--   0 runner    (1001) docker     (123)      336 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7685 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/base_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)    10379 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/base_mmocr_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     8029 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/kie_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)    10536 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/mmocr_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)      976 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/textdet_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)      865 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/apis/inferencers/textrec_inferencer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      482 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3340 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/dataset_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     3837 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/icdar_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     3937 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/ocr_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16265 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/config_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    27158 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/data_converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     6052 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/data_obtainer.py
--rw-r--r--   0 runner    (1001) docker     (123)     5345 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/data_preparer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/dumpers/
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/dumpers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/dumpers/dumpers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/
--rw-r--r--   0 runner    (1001) docker     (123)      756 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3612 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4582 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/coco_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1288 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/funsd_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     4810 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/icdar_txt_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     4451 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/naf_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     2942 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/sroie_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/svt_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3393 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/totaltext_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     2957 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/wildreceipt_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     8603 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/recog_lmdb_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     5850 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/recog_text_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/
--rw-r--r--   0 runner    (1001) docker     (123)     1633 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3725 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/adapters.py
--rw-r--r--   0 runner    (1001) docker     (123)    11451 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/formatting.py
--rw-r--r--   0 runner    (1001) docker     (123)    20452 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/loading.py
--rw-r--r--   0 runner    (1001) docker     (123)    28656 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/ocr_transforms.py
--rw-r--r--   0 runner    (1001) docker     (123)    32125 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/textdet_transforms.py
--rw-r--r--   0 runner    (1001) docker     (123)    23383 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/textrecog_transforms.py
--rw-r--r--   0 runner    (1001) docker     (123)    12682 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/transforms/wrappers.py
--rw-r--r--   0 runner    (1001) docker     (123)     7829 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/datasets/wildreceipt_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/engine/
--rw-r--r--   0 runner    (1001) docker     (123)       77 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/engine/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/engine/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/engine/hooks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5306 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/engine/hooks/visualization_hook.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)      112 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/evaluation/evaluator/
--rw-r--r--   0 runner    (1001) docker     (123)      147 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/evaluator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4375 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/evaluator/multi_datasets_evaluator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/evaluation/functional/
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/functional/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1307 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/functional/hmean.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/evaluation/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6706 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/metrics/f_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)    10375 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/metrics/hmean_iou_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)    12352 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/evaluation/metrics/recog_metric.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/backbones/
--rw-r--r--   0 runner    (1001) docker     (123)      141 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/backbones/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3397 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/backbones/clip_resnet.py
--rw-r--r--   0 runner    (1001) docker     (123)    21465 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/backbones/unet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/dictionary/
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/dictionary/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7420 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/dictionary/dictionary.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/layers/
--rw-r--r--   0 runner    (1001) docker     (123)      159 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/layers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6601 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/layers/transformer_layers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/losses/
--rw-r--r--   0 runner    (1001) docker     (123)      572 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8048 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/losses/bce_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/losses/ce_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     3432 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/losses/dice_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     2405 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/losses/l1_loss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/modules/
--rw-r--r--   0 runner    (1001) docker     (123)      361 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/modules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5333 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/modules/transformer_module.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/common/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/plugins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/common/plugins/common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/kie/
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/kie/extractors/
--rw-r--r--   0 runner    (1001) docker     (123)       94 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/extractors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8301 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/extractors/sdmgr.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/kie/heads/
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/heads/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15439 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/heads/sdmgr_head.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/kie/module_losses/
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/module_losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2629 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/module_losses/sdmgr_module_loss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/kie/postprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/postprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7739 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/kie/postprocessors/sdmgr_postprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/
--rw-r--r--   0 runner    (1001) docker     (123)      256 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/data_preprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/data_preprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3955 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/data_preprocessors/data_preprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/
--rw-r--r--   0 runner    (1001) docker     (123)      436 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4061 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      385 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/dbnet.py
--rw-r--r--   0 runner    (1001) docker     (123)      393 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/drrg.py
--rw-r--r--   0 runner    (1001) docker     (123)      408 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/fcenet.py
--rw-r--r--   0 runner    (1001) docker     (123)     6921 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/mmdet_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)      406 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/panet.py
--rw-r--r--   0 runner    (1001) docker     (123)      392 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/psenet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5137 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/single_stage_text_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/detectors/textsnake.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/
--rw-r--r--   0 runner    (1001) docker     (123)      387 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5117 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7442 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/db_head.py
--rw-r--r--   0 runner    (1001) docker     (123)    50385 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/drrg_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     4041 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/fce_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     3060 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/pan_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/pse_head.py
--rw-r--r--   0 runner    (1001) docker     (123)     2827 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/heads/textsnake_head.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1450 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    12225 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/db_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    33570 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/drrg_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    23399 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/fce_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    14050 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/pan_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     5114 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/pse_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     3656 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/seg_based_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    27634 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/textsnake_module_loss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/necks/
--rw-r--r--   0 runner    (1001) docker     (123)      211 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/necks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7017 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpem_ffm.py
--rw-r--r--   0 runner    (1001) docker     (123)     9499 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpn_cat.py
--rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpn_unet.py
--rw-r--r--   0 runner    (1001) docker     (123)     4567 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpnf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      571 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8406 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     6526 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/db_postprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)    17530 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/drrg_postprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)    10125 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/fce_postprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     6599 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/pan_postprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     4417 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/pse_postprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     9788 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/textsnake_postprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/
--rw-r--r--   0 runner    (1001) docker     (123)      437 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2517 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/mini_vgg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1483 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/mobilenet_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1952 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/nrtr_modality_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)    10145 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/resnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5638 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/resnet31_ocr.py
--rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/resnet_abi.py
--rw-r--r--   0 runner    (1001) docker     (123)     2146 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/shallow_cnn.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/data_preprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/data_preprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3773 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/data_preprocessors/data_preprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/
--rwxr-xr-x   0 runner    (1001) docker     (123)     1048 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7274 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/abi_fuser.py
--rw-r--r--   0 runner    (1001) docker     (123)     9125 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/abi_language_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     9375 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/abi_vision_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     7260 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/aster_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     6687 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4005 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/crnn_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)    10077 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/master_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)    10207 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/nrtr_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     8605 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/position_attention_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     6209 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/robust_scanner_fuser.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    22509 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/sar_decoder.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     5459 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/sar_decoder_with_bs.py
--rw-r--r--   0 runner    (1001) docker     (123)     9837 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/sequence_attention_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     3676 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/svtr_decoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/
--rw-r--r--   0 runner    (1001) docker     (123)      523 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3168 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/abi_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/aster_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)      291 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/channel_reduction_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     3944 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/nrtr_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     4343 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/sar_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/satrn_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)    24406 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/svtr_encoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/
--rw-r--r--   0 runner    (1001) docker     (123)      602 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5729 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/conv_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)      782 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/dot_product_attention_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/lstm_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/position_aware_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)      674 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/robust_scanner_fusion_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)     7985 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/layers/satrn_layers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/
--rwxr-xr-x   0 runner    (1001) docker     (123)      312 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/abi_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     5516 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5971 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/ce_module_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     5048 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/ctc_module_loss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/plugins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6935 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/plugins/common.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1484 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/attn_postprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     4292 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1774 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/ctc_postprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/preprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/preprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      295 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/preprocessors/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    11713 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/preprocessors/tps_preprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/
--rw-r--r--   0 runner    (1001) docker     (123)      542 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      402 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/abinet.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/aster.py
--rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      250 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/crnn.py
--rw-r--r--   0 runner    (1001) docker     (123)     5094 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/encoder_decoder_recognizer.py
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/master.py
--rw-r--r--   0 runner    (1001) docker     (123)      288 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/nrtr.py
--rw-r--r--   0 runner    (1001) docker     (123)      315 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/robust_scanner.py
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/sar.py
--rw-r--r--   0 runner    (1001) docker     (123)      286 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/satrn.py
--rw-r--r--   0 runner    (1001) docker     (123)      351 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/svtr.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    18749 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/ocr.py
--rw-r--r--   0 runner    (1001) docker     (123)     3951 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/structures/
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/structures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3688 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/structures/kie_data_sample.py
--rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/structures/textdet_data_sample.py
--rw-r--r--   0 runner    (1001) docker     (123)     2796 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/structures/textrecog_data_sample.py
--rw-r--r--   0 runner    (1001) docker     (123)     2988 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/structures/textspotting_data_sample.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/testing/
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/testing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3533 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/testing/data.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/utils/
--rw-r--r--   0 runner    (1001) docker     (123)     3145 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14466 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/bbox_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1609 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/check_argument.py
--rw-r--r--   0 runner    (1001) docker     (123)      482 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/collect_env.py
--rw-r--r--   0 runner    (1001) docker     (123)     6516 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/data_converter_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3267 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/fileio.py
--rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/img_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/mask_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2829 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/parsers.py
--rw-r--r--   0 runner    (1001) docker     (123)      953 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/point_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    16206 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/polygon_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/setup_env.py
--rw-r--r--   0 runner    (1001) docker     (123)     1334 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/string_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/transform_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1555 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/utils/typing_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      103 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr/visualization/
--rw-r--r--   0 runner    (1001) docker     (123)      475 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/visualization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9744 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/visualization/base_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)    19273 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/visualization/kie_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     7904 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/visualization/textdet_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     5955 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/visualization/textrecog_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     6068 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/mmocr/visualization/textspotting_visualizer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    16575 2023-01-06 09:36:04.000000 mmocr-1.0.0rc5/mmocr.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    22549 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/mmocr.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-06 09:36:04.000000 mmocr-1.0.0rc5/mmocr.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-06 09:36:04.000000 mmocr-1.0.0rc5/mmocr.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      681 2023-01-06 09:36:04.000000 mmocr-1.0.0rc5/mmocr.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-01-06 09:36:04.000000 mmocr-1.0.0rc5/mmocr.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/requirements/
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/albu.txt
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/build.txt
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/docs.txt
--rw-r--r--   0 runner    (1001) docker     (123)       71 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/mminstall.txt
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/optional.txt
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/readthedocs.txt
--rw-r--r--   0 runner    (1001) docker     (123)      166 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/runtime.txt
--rw-r--r--   0 runner    (1001) docker     (123)      207 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/requirements/tests.txt
--rw-r--r--   0 runner    (1001) docker     (123)      768 2023-01-06 09:36:05.000000 mmocr-1.0.0rc5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     7403 2023-01-06 09:35:58.000000 mmocr-1.0.0rc5/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/
+-rw-r--r--   0 runner    (1001) docker     (123)      155 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    19079 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    16077 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/backbone/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/backbone/oclip/
+-rw-r--r--   0 runner    (1001) docker     (123)      420 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/backbone/oclip/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      732 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/datasets/wildreceipt-openset.py
+-rw-r--r--   0 runner    (1001) docker     (123)      452 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/datasets/wildreceipt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      908 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/default_runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/schedules/
+-rw-r--r--   0 runner    (1001) docker     (123)      346 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/schedules/schedule_adam_60e.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/
+-rw-r--r--   0 runner    (1001) docker     (123)      955 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_novisual.py
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_unet16.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2051 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt-openset.py
+-rw-r--r--   0 runner    (1001) docker     (123)      786 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      506 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      519 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/icdar2017.py
+-rw-r--r--   0 runner    (1001) docker     (123)      518 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/synthtext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/totaltext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      476 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/toy_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/default_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/pretrain_runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/schedules/
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/schedules/schedule_adam_600e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      348 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_100k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      379 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_1200e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      558 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     2159 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet18_fpnc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2290 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet50-dcnv2_fpnc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_100k_synthtext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      860 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2314 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_totaltext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      865 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_100k_synthtext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1041 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      525 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-oclip_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      623 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2827 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/
+-rw-r--r--   0 runner    (1001) docker     (123)     2283 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/_base_dbnetpp_resnet50-dcnv2_fpnc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1303 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_100k_synthtext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      527 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-oclip_fpnc_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50_fpnc_1200e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/
+-rw-r--r--   0 runner    (1001) docker     (123)     2992 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/_base_drrg_resnet50_fpn-unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/drrg_resnet50-oclip_fpn-unet_1200e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      844 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/drrg_resnet50_fpn-unet_1200e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      894 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/
+-rw-r--r--   0 runner    (1001) docker     (123)      512 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50-dcnv2_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1687 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-dcnv2_fpn_1500e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      401 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-oclip_fpn_1500e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-oclip_fpn_1500e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3322 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_totaltext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2922 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/
+-rw-r--r--   0 runner    (1001) docker     (123)     1890 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/_base_mask-rcnn_resnet50_fpn.py
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      354 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1125 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      507 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2017.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2441 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/
+-rw-r--r--   0 runner    (1001) docker     (123)     2730 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/_base_panet_resnet18_fpem-ffm.py
+-rw-r--r--   0 runner    (1001) docker     (123)      547 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/_base_panet_resnet50_fpem-ffm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1380 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2608 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1092 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2535 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/panet_resnet50_fpem-ffm_600e_icdar2017.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/
+-rw-r--r--   0 runner    (1001) docker     (123)     2286 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/_base_psenet_resnet50_fpnf.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2233 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50-oclip_fpnf_600e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      267 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50-oclip_fpnf_600e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2017.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/
+-rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/_base_textsnake_resnet50_fpn-unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/textsnake_resnet50-oclip_fpn-unet_1200e_ctw1500.py
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/textsnake_resnet50_fpn-unet_1200e_ctw1500.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/coco_text_v1.py
+-rw-r--r--   0 runner    (1001) docker     (123)      214 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/cute80.py
+-rw-r--r--   0 runner    (1001) docker     (123)      232 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2011.py
+-rw-r--r--   0 runner    (1001) docker     (123)      570 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2013.py
+-rw-r--r--   0 runner    (1001) docker     (123)      572 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2015.py
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/iiit5k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      529 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/mjsynth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/svt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/svtp.py
+-rw-r--r--   0 runner    (1001) docker     (123)      825 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/synthtext.py
+-rw-r--r--   0 runner    (1001) docker     (123)      247 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/synthtext_add.py
+-rw-r--r--   0 runner    (1001) docker     (123)      407 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/totaltext.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      410 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/toy_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/default_runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/schedules/
+-rw-r--r--   0 runner    (1001) docker     (123)      306 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adadelta_5e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adam_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      327 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adam_step_5e.py
+-rw-r--r--   0 runner    (1001) docker     (123)      492 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adamw_cos_6e.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/
+-rw-r--r--   0 runner    (1001) docker     (123)     5292 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/_base_abinet-vision.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/_base_abinet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/abinet-vision_20e_st-an_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1893 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/abinet_20e_st-an_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2923 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/
+-rw-r--r--   0 runner    (1001) docker     (123)     3733 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/_base_aster.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1648 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/aster_resnet45_6e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1434 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/
+-rw-r--r--   0 runner    (1001) docker     (123)     3673 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/_base_crnn_mini-vgg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_toy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/
+-rw-r--r--   0 runner    (1001) docker     (123)     5481 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/_base_master_resnet31.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1827 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_st_mj_sa.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_toy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1477 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/
+-rw-r--r--   0 runner    (1001) docker     (123)     3887 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_modality-transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4050 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_resnet31.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3457 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1663 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_toy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1653 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_resnet31-1by16-1by8_6e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_resnet31-1by8-1by4_6e_st_mj.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/
+-rw-r--r--   0 runner    (1001) docker     (123)     4165 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/_base_robustscanner_resnet31.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1716 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2219 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_st-sub_mj-sub_sa_real.py
+-rw-r--r--   0 runner    (1001) docker     (123)      997 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_toy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4109 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/_base_sar_resnet31_parallel-decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2852 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2225 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_st-sub_mj-sub_sa_real.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1000 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_toy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/sar_resnet31_sequential-decoder_5e_st-sub_mj-sub_sa_real.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/
+-rw-r--r--   0 runner    (1001) docker     (123)     3797 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/_base_satrn_shallow.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2382 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      547 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/satrn_shallow-small_5e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/satrn_shallow_5e_st_mj.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/
+-rw-r--r--   0 runner    (1001) docker     (123)     4901 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/_base_svtr-tiny.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      431 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/svtr-base_20e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)      488 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/svtr-large_20e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)      218 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/svtr-small_20e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2096 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/svtr-tiny_20e_st_mj.py
+-rw-r--r--   0 runner    (1001) docker     (123)      740 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/model-index.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/
+-rw-r--r--   0 runner    (1001) docker     (123)    15741 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/browse_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1400 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/get_flops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/offline_eval.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/print_config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/common/
+-rw-r--r--   0 runner    (1001) docker     (123)     4411 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/common/curvedsyntext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2626 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/common/extract_kaist.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/kie/
+-rw-r--r--   0 runner    (1001) docker     (123)     4422 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/kie/closeset_to_openset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5589 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/prepare_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/
+-rw-r--r--   0 runner    (1001) docker     (123)     4437 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/art_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5319 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/bid_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1933 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/coco_to_line_dict.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4162 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/cocotext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7279 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ctw1500_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2047 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/data_migrator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4578 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/detext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4507 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/funsd_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5132 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/hiertext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4879 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ic11_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4748 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ic13_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5837 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/icdar_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5949 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ilst_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4739 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/imgur_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6152 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/kaist_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4055 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/lsvt_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5317 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/lv_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6153 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/mtwi_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5932 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/naf_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5771 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/rctw_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5984 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/rects_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4760 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/sroie_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6177 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/synthtext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2455 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/textocr_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11836 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/totaltext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5014 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/vintext_converter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/
+-rw-r--r--   0 runner    (1001) docker     (123)     3106 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/art_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7592 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/bid_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5647 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/cocotext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3375 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/data_migrator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6481 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/detext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6265 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/funsd_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7696 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/hiertext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1802 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/ic11_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/ic13_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8074 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/ilst_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5385 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/imgur_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8392 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/kaist_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5606 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/lmdb_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5743 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/lsvt_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2078 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/lv_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7955 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/mtwi_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8909 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/naf_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4042 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/openvino_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7464 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/rctw_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7856 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/rects_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/sroie_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2873 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/svt_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4787 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/synthtext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3576 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/textocr_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11642 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/totaltext_converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6812 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/vintext_converter.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      479 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dist_test.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      443 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/dist_train.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3240 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/infer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/model_converters/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1861 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/model_converters/publish_model.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      485 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/slurm_test.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      622 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/slurm_train.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4985 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/test.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4006 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/.mim/tools/train.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2083 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/apis/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/
+-rw-r--r--   0 runner    (1001) docker     (123)      410 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16603 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/base_mmocr_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12042 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/kie_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17229 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/mmocr_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1963 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/textdet_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1778 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/textrec_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2041 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/apis/inferencers/textspot_inferencer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3340 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/dataset_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3837 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/icdar_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3920 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/ocr_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/config_generators/
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/config_generators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5693 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/config_generators/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4269 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/config_generators/textdet_config_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5622 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/config_generators/textrecog_config_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2694 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/config_generators/textspotting_config_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7680 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/data_preparer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/dumpers/
+-rw-r--r--   0 runner    (1001) docker     (123)      325 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/dumpers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1235 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/dumpers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      569 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/dumpers/json_dumper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5531 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/dumpers/lmdb_dumper.py
+-rw-r--r--   0 runner    (1001) docker     (123)      556 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/dumpers/wild_receipt_openset_dumper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/gatherers/
+-rw-r--r--   0 runner    (1001) docker     (123)      273 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/gatherers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2325 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/gatherers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      907 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/gatherers/mono_gatherer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2396 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/gatherers/naf_gatherer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2298 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/gatherers/pair_gatherer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/obtainers/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/obtainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7055 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/obtainers/naive_data_obtainer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/
+-rw-r--r--   0 runner    (1001) docker     (123)      426 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3405 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/textdet_packer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6237 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/textrecog_packer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3618 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/textspotting_packer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/packers/wildreceipt_packer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4714 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4496 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/coco_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1169 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/funsd_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4889 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/icdar_txt_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4229 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/naf_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2954 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/sroie_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/svt_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3266 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/totaltext_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2984 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/wildreceipt_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6635 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/recog_lmdb_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5850 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/recog_text_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/samplers/
+-rw-r--r--   0 runner    (1001) docker     (123)      118 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/samplers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3534 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/samplers/batch_aug.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/
+-rw-r--r--   0 runner    (1001) docker     (123)     1645 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3725 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/adapters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12621 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/formatting.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17881 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/loading.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28656 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/ocr_transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32125 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/textdet_transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23383 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/textrecog_transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12682 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/transforms/wrappers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9721 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/datasets/wildreceipt_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/engine/
+-rw-r--r--   0 runner    (1001) docker     (123)       77 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/engine/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/engine/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/engine/hooks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5306 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/engine/hooks/visualization_hook.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)      112 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/evaluation/evaluator/
+-rw-r--r--   0 runner    (1001) docker     (123)      147 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/evaluator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4375 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/evaluator/multi_datasets_evaluator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/evaluation/functional/
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/functional/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1307 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/functional/hmean.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/evaluation/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6706 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/metrics/f_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10375 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/metrics/hmean_iou_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12352 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/evaluation/metrics/recog_metric.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/backbones/
+-rw-r--r--   0 runner    (1001) docker     (123)      141 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/backbones/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3397 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/backbones/clip_resnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21465 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/backbones/unet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/dictionary/
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/dictionary/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7420 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/dictionary/dictionary.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/layers/
+-rw-r--r--   0 runner    (1001) docker     (123)      159 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/layers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6601 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/layers/transformer_layers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/losses/
+-rw-r--r--   0 runner    (1001) docker     (123)      572 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8048 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/losses/bce_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/losses/ce_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3432 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/losses/dice_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2405 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/losses/l1_loss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/modules/
+-rw-r--r--   0 runner    (1001) docker     (123)      361 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/modules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5333 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/modules/transformer_module.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/common/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/plugins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/common/plugins/common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/kie/
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/kie/extractors/
+-rw-r--r--   0 runner    (1001) docker     (123)       94 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/extractors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8301 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/extractors/sdmgr.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/kie/heads/
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/heads/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15439 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/heads/sdmgr_head.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/kie/module_losses/
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/module_losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2629 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/module_losses/sdmgr_module_loss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/kie/postprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/postprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7739 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/kie/postprocessors/sdmgr_postprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/
+-rw-r--r--   0 runner    (1001) docker     (123)      256 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/data_preprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/data_preprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3955 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/data_preprocessors/data_preprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/
+-rw-r--r--   0 runner    (1001) docker     (123)      436 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4061 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      385 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/dbnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      393 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/drrg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      408 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/fcenet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6921 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/mmdet_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)      406 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/panet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/psenet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5137 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/single_stage_text_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)      404 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/detectors/textsnake.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/
+-rw-r--r--   0 runner    (1001) docker     (123)      387 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5117 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7442 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/db_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50385 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/drrg_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4041 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/fce_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3060 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/pan_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1431 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/pse_head.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2827 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/heads/textsnake_head.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1450 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12225 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/db_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33570 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/drrg_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23399 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/fce_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14050 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/pan_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5114 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/pse_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3656 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/seg_based_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27634 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/textsnake_module_loss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/necks/
+-rw-r--r--   0 runner    (1001) docker     (123)      211 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/necks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7017 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpem_ffm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9499 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpn_cat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpn_unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4567 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpnf.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      571 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8406 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6526 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/db_postprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17530 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/drrg_postprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10125 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/fce_postprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6599 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/pan_postprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4417 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/pse_postprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9788 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/textsnake_postprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/
+-rw-r--r--   0 runner    (1001) docker     (123)      437 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2517 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/mini_vgg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1483 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/mobilenet_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1952 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/nrtr_modality_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10145 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/resnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5638 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/resnet31_ocr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4396 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/resnet_abi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2146 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/shallow_cnn.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/data_preprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/data_preprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3773 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/data_preprocessors/data_preprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1048 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7274 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/abi_fuser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9125 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/abi_language_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9375 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/abi_vision_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7316 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/aster_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6687 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4005 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/crnn_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10077 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/master_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10207 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/nrtr_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8605 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/position_attention_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6209 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/robust_scanner_fuser.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    22509 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/sar_decoder.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     5459 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/sar_decoder_with_bs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9837 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/sequence_attention_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3676 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/svtr_decoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/
+-rw-r--r--   0 runner    (1001) docker     (123)      523 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3168 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/abi_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/aster_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)      291 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1551 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/channel_reduction_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3944 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/nrtr_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4343 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/sar_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/satrn_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24406 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/svtr_encoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/
+-rw-r--r--   0 runner    (1001) docker     (123)      602 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5729 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/conv_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      782 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/dot_product_attention_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/lstm_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1052 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/position_aware_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      674 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/robust_scanner_fusion_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7985 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/layers/satrn_layers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      312 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/abi_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5516 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5971 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/ce_module_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5048 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/ctc_module_loss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/plugins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6935 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/plugins/common.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1484 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/attn_postprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4292 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1774 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/ctc_postprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/preprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/preprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      295 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/preprocessors/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11713 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/preprocessors/tps_preprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/
+-rw-r--r--   0 runner    (1001) docker     (123)      659 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      402 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/abinet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      380 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/aster.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      250 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/crnn.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5094 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/encoder_decoder_recognizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4240 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/encoder_decoder_recognizer_tta.py
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/master.py
+-rw-r--r--   0 runner    (1001) docker     (123)      288 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/nrtr.py
+-rw-r--r--   0 runner    (1001) docker     (123)      315 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/robust_scanner.py
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/sar.py
+-rw-r--r--   0 runner    (1001) docker     (123)      286 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/satrn.py
+-rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/svtr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6072 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/structures/
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/structures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3688 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/structures/kie_data_sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/structures/textdet_data_sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2796 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/structures/textrecog_data_sample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2988 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/structures/textspotting_data_sample.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/testing/
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/testing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3533 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/testing/data.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     3327 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14466 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/bbox_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2077 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/bezier_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1609 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/check_argument.py
+-rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/collect_env.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6516 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/data_converter_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3267 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/fileio.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/img_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/mask_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2829 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/parsers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      953 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/point_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16572 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/polygon_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2579 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/processing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1958 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/setup_env.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1334 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/string_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1707 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/transform_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1667 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/utils/typing_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      103 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr/visualization/
+-rw-r--r--   0 runner    (1001) docker     (123)      475 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/visualization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11973 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/visualization/base_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19517 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/visualization/kie_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9294 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/visualization/textdet_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6024 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/visualization/textrecog_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6362 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/mmocr/visualization/textspotting_visualizer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    19079 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    23820 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      681 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/mmocr.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/requirements/
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/albu.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/build.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/docs.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/mminstall.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/optional.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/readthedocs.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      166 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/runtime.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      207 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/requirements/tests.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      777 2023-03-07 12:27:59.000000 mmocr-1.0.0rc6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     7412 2023-03-07 12:27:54.000000 mmocr-1.0.0rc6/setup.py
```

### Comparing `mmocr-1.0.0rc5/PKG-INFO` & `mmocr-1.0.0rc6/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mmocr
-Version: 1.0.0rc5
+Version: 1.0.0rc6
 Summary: OpenMMLab Text Detection, OCR, and NLP Toolbox
 Home-page: https://github.com/open-mmlab/mmocr
 Maintainer: MMOCR Authors
 Maintainer-email: openmmlab@gmail.com
 License: Apache License 2.0
 Description: <div align="center">
           <img src="resources/mmocr-logo.png" width="500px"/>
@@ -44,14 +44,45 @@
         </div>
         
         <div align="center">
         
         English | [简体中文](README_zh-CN.md)
         
         </div>
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
+        ## Latest Updates
+        
+        **The default branch has been switched to `1.x` from `main`, and we encourage
+        users to migrate to the latest version, though it comes with some cost. Please refer to [Migration Guide](https://mmocr.readthedocs.io/en/dev-1.x/migration/overview.html) for more
+        details.**
+        
+        v1.0.0rc6 was released in 2023-03-07.
+        
+        1. Two new models, ABCNet v2 (inference only) and SPTS are added to `projects/` folder.
+        2. Announcing `Inferencer`, a unified inference interface in OpenMMLab for everyone's easy access and quick inference with all the pre-trained weights. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/inference.html)
+        3. Users can use test-time augmentation for text recognition tasks. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/train_test.html#test-time-augmentation)
+        4. Support [batch augmentation](https://openaccess.thecvf.com/content_CVPR_2020/papers/Hoffer_Augment_Your_Batch_Improving_Generalization_Through_Instance_Repetition_CVPR_2020_paper.pdf) through [`BatchAugSampler`](https://github.com/open-mmlab/mmocr/pull/1757), which is a technique used in SPTS.
+        5. Dataset Preparer has been refactored to allow more flexible configurations. Besides, users are now able to prepare text recognition datasets in LMDB formats. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/dataset_preparer.html#lmdb-format)
+        6. Some textspotting datasets have been revised to enhance the correctness and consistency with the common practice.
+        7. Potential spurious warnings from `shapely` have been eliminated.
+        
+        Read [Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for more details!
         
         ## Introduction
         
         MMOCR is an open-source toolbox based on PyTorch and mmdetection for text detection, text recognition, and the corresponding downstream tasks including key information extraction. It is part of the [OpenMMLab](https://openmmlab.com/) project.
         
         The main branch works with **PyTorch 1.6+**.
         
@@ -73,25 +104,14 @@
         
           The modular design of MMOCR enables users to define their own optimizers, data preprocessors, and model components such as backbones, necks and heads as well as losses. Please refer to [Overview](https://mmocr.readthedocs.io/en/dev-1.x/get_started/overview.html) for how to construct a customized model.
         
         - **Numerous Utilities**
         
           The toolbox provides a comprehensive set of utilities which can help users assess the performance of models. It includes visualizers which allow visualization of images, ground truths as well as predicted bounding boxes, and a validation tool for evaluating checkpoints during training.  It also includes data converters to demonstrate how to convert your own data to the annotation files which the toolbox supports.
         
-        ## Latest Updates
-        
-        v1.0.0rc5 was released in 2023-01-06.
-        
-        1. Two models, Aster and SVTR, are added to our model zoo. The full implementation of ABCNet is also available now.
-        2. Dataset Preparer supports 5 more datasets: CocoTextV2, FUNSD, TextOCR, NAF, SROIE.
-        3. We have 4 more text recognition transforms, and two more helper transforms.
-        4. The transform, `FixInvalidPolygon`, is getting smarter at dealing with invalid polygons, and now capable of handling more weird annotations. As a result, a complete training cycle on TotalText dataset can be performed bug-free. The weights of DBNet and FCENet pretrained on TotalText are also released.
-        
-        Read [Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for more details!
-        
         ## What's New in MMOCR 1.0
         
         1. **New engines**. MMOCR 1.x is based on [MMEngine](https://github.com/open-mmlab/mmengine), which provides a general and powerful runner that allows more flexible customizations and significantly simplifies the entrypoints of high-level interfaces.
         
         2. **Unified interfaces**. As a part of the OpenMMLab 2.0 projects, MMOCR 1.x unifies and refactors the interfaces and internal logics of train, testing, datasets, models, evaluation, and visualization. All the OpenMMLab 2.0 projects share the same design in those interfaces and logics to allow the emergence of multi-task/modality algorithms.
         
         3. **Cross project calling**. Benefiting from the unified design, you can use the models implemented in other OpenMMLab projects, such as MMDet. We provide an example of how to use MMDetection's Mask R-CNN through `MMDetWrapper`. Check our documents for more details. More wrappers will be released in the future.
@@ -175,14 +195,16 @@
         
         </details>
         
         <details open>
         <summary>Text Spotting</summary>
         
         - [x] [ABCNet](projects/ABCNet/README.md) (CVPR'2020)
+        - [x] [ABCNetV2](projects/ABCNet/README_V2.md) (TPAMI'2021)
+        - [x] [SPTS](projects/SPTS/README.md) (ACM MM'2022)
         
         </details>
         
         Please refer to [model_zoo](https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more details.
         
         ## Contributing
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: mmocr Version: 1.0.0rc5 Summary: OpenMMLab Text
+Metadata-Version: 2.1 Name: mmocr Version: 1.0.0rc6 Summary: OpenMMLab Text
 Detection, OCR, and NLP Toolbox Home-page: https://github.com/open-mmlab/mmocr
 Maintainer: MMOCR Authors Maintainer-email: openmmlab@gmail.com License: Apache
 License 2.0 Description:
                           [resources/mmocr-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
@@ -21,19 +21,41 @@
  2.amazonaws.com/assets/try_on_tiyaro_badge.svg] [ðDocumentation](https://
       mmocr.readthedocs.io/en/dev-1.x/) | [ð ï¸Installation](https://
   mmocr.readthedocs.io/en/dev-1.x/get_started/install.html) | [ðModel Zoo]
   (https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) | [ðUpdate News]
 (https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) | [ð¤Reporting
         Issues](https://github.com/open-mmlab/mmocr/issues/new/choose)
                    English | [ç®ä½ä¸­æ](README_zh-CN.md)
-## Introduction MMOCR is an open-source toolbox based on PyTorch and
-mmdetection for text detection, text recognition, and the corresponding
-downstream tasks including key information extraction. It is part of the
-[OpenMMLab](https://openmmlab.com/) project. The main branch works with
-**PyTorch 1.6+**.
+
+## Latest Updates **The default branch has been switched to `1.x` from `main`,
+and we encourage users to migrate to the latest version, though it comes with
+some cost. Please refer to [Migration Guide](https://mmocr.readthedocs.io/en/
+dev-1.x/migration/overview.html) for more details.** v1.0.0rc6 was released in
+2023-03-07. 1. Two new models, ABCNet v2 (inference only) and SPTS are added to
+`projects/` folder. 2. Announcing `Inferencer`, a unified inference interface
+in OpenMMLab for everyone's easy access and quick inference with all the pre-
+trained weights. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/
+inference.html) 3. Users can use test-time augmentation for text recognition
+tasks. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/
+train_test.html#test-time-augmentation) 4. Support [batch augmentation](https:/
+/openaccess.thecvf.com/content_CVPR_2020/papers/
+Hoffer_Augment_Your_Batch_Improving_Generalization_Through_Instance_Repetition_CVPR_2020_paper.pdf)
+through [`BatchAugSampler`](https://github.com/open-mmlab/mmocr/pull/1757),
+which is a technique used in SPTS. 5. Dataset Preparer has been refactored to
+allow more flexible configurations. Besides, users are now able to prepare text
+recognition datasets in LMDB formats. [Docs](https://mmocr.readthedocs.io/en/
+dev-1.x/user_guides/data_prepare/dataset_preparer.html#lmdb-format) 6. Some
+textspotting datasets have been revised to enhance the correctness and
+consistency with the common practice. 7. Potential spurious warnings from
+`shapely` have been eliminated. Read [Changelog](https://mmocr.readthedocs.io/
+en/dev-1.x/notes/changelog.html) for more details! ## Introduction MMOCR is an
+open-source toolbox based on PyTorch and mmdetection for text detection, text
+recognition, and the corresponding downstream tasks including key information
+extraction. It is part of the [OpenMMLab](https://openmmlab.com/) project. The
+main branch works with **PyTorch 1.6+**.
  [https://user-images.githubusercontent.com/24622904/187838618-1fdc61c0-2d46-
                           49f9-8502-976ffdf01f28.png]
 ### Major Features - **Comprehensive Pipeline** The toolbox supports not only
 text detection and text recognition, but also their downstream tasks such as
 key information extraction. - **Multiple Models** The toolbox supports a wide
 variety of state-of-the-art models for text detection, text recognition and key
 information extraction. - **Modular Design** The modular design of MMOCR
@@ -42,44 +64,35 @@
 to [Overview](https://mmocr.readthedocs.io/en/dev-1.x/get_started/
 overview.html) for how to construct a customized model. - **Numerous
 Utilities** The toolbox provides a comprehensive set of utilities which can
 help users assess the performance of models. It includes visualizers which
 allow visualization of images, ground truths as well as predicted bounding
 boxes, and a validation tool for evaluating checkpoints during training. It
 also includes data converters to demonstrate how to convert your own data to
-the annotation files which the toolbox supports. ## Latest Updates v1.0.0rc5
-was released in 2023-01-06. 1. Two models, Aster and SVTR, are added to our
-model zoo. The full implementation of ABCNet is also available now. 2. Dataset
-Preparer supports 5 more datasets: CocoTextV2, FUNSD, TextOCR, NAF, SROIE. 3.
-We have 4 more text recognition transforms, and two more helper transforms. 4.
-The transform, `FixInvalidPolygon`, is getting smarter at dealing with invalid
-polygons, and now capable of handling more weird annotations. As a result, a
-complete training cycle on TotalText dataset can be performed bug-free. The
-weights of DBNet and FCENet pretrained on TotalText are also released. Read
-[Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for
-more details! ## What's New in MMOCR 1.0 1. **New engines**. MMOCR 1.x is based
-on [MMEngine](https://github.com/open-mmlab/mmengine), which provides a general
-and powerful runner that allows more flexible customizations and significantly
-simplifies the entrypoints of high-level interfaces. 2. **Unified interfaces**.
-As a part of the OpenMMLab 2.0 projects, MMOCR 1.x unifies and refactors the
-interfaces and internal logics of train, testing, datasets, models, evaluation,
-and visualization. All the OpenMMLab 2.0 projects share the same design in
-those interfaces and logics to allow the emergence of multi-task/modality
-algorithms. 3. **Cross project calling**. Benefiting from the unified design,
-you can use the models implemented in other OpenMMLab projects, such as MMDet.
-We provide an example of how to use MMDetection's Mask R-CNN through
-`MMDetWrapper`. Check our documents for more details. More wrappers will be
-released in the future. 4. **Stronger visualization**. We provide a series of
-useful tools which are mostly based on brand-new visualizers. As a result, it
-is more convenient for the users to explore the models and datasets now. 5.
-**More documentation and tutorials**. We add a bunch of documentation and
-tutorials to help users get started more smoothly. Read it [here](https://
-mmocr.readthedocs.io/en/dev-1.x/). 6. **One-stop Dataset Preparaion**. Multiple
-datasets are instantly ready with only one line of command, via our [Dataset
-Preparer](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/
+the annotation files which the toolbox supports. ## What's New in MMOCR 1.0 1.
+**New engines**. MMOCR 1.x is based on [MMEngine](https://github.com/open-
+mmlab/mmengine), which provides a general and powerful runner that allows more
+flexible customizations and significantly simplifies the entrypoints of high-
+level interfaces. 2. **Unified interfaces**. As a part of the OpenMMLab 2.0
+projects, MMOCR 1.x unifies and refactors the interfaces and internal logics of
+train, testing, datasets, models, evaluation, and visualization. All the
+OpenMMLab 2.0 projects share the same design in those interfaces and logics to
+allow the emergence of multi-task/modality algorithms. 3. **Cross project
+calling**. Benefiting from the unified design, you can use the models
+implemented in other OpenMMLab projects, such as MMDet. We provide an example
+of how to use MMDetection's Mask R-CNN through `MMDetWrapper`. Check our
+documents for more details. More wrappers will be released in the future. 4.
+**Stronger visualization**. We provide a series of useful tools which are
+mostly based on brand-new visualizers. As a result, it is more convenient for
+the users to explore the models and datasets now. 5. **More documentation and
+tutorials**. We add a bunch of documentation and tutorials to help users get
+started more smoothly. Read it [here](https://mmocr.readthedocs.io/en/dev-1.x/
+). 6. **One-stop Dataset Preparaion**. Multiple datasets are instantly ready
+with only one line of command, via our [Dataset Preparer](https://
+mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/
 dataset_preparer.html). 7. **Embracing more `projects/`**: We now introduce
 `projects/` folder, where some experimental features, frameworks and models can
 be placed, only needed to satisfy the minimum requirement on the code quality.
 Everyone is welcome to post their implementation of any great ideas in this
 folder! Learn more from our [example project](https://github.com/open-mmlab/
 mmocr/blob/dev-1.x/projects/example_project/). 8. **More models**. MMOCR 1.0
 supports more tasks and more state-of-the-art models! ## Installation MMOCR
@@ -109,66 +122,68 @@
 README.md) (PR'2021) - [x] [NRTR](configs/textrecog/nrtr/README.md)
 (ICDAR'2019) - [x] [RobustScanner](configs/textrecog/robust_scanner/README.md)
 (ECCV'2020) - [x] [SAR](configs/textrecog/sar/README.md) (AAAI'2019) - [x]
 [SATRN](configs/textrecog/satrn/README.md) (CVPR'2020 Workshop on Text and
 Documents in the Deep Learning Era) - [x] [SVTR](configs/textrecog/svtr/
 README.md) (IJCAI'2022)   Key Information Extraction - [x] [SDMG-R](configs/
 kie/sdmgr/README.md) (ArXiv'2021)   Text Spotting - [x] [ABCNet](projects/
-ABCNet/README.md) (CVPR'2020)  Please refer to [model_zoo](https://
-mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more details. ##
-Contributing We appreciate all contributions to improve MMOCR. Please refer to
-[CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guidelines. ##
-Acknowledgement MMOCR is an open-source project that is contributed by
-researchers and engineers from various colleges and companies. We appreciate
-all the contributors who implement their methods or add new features, as well
-as users who give valuable feedbacks. We hope the toolbox and benchmark could
-serve the growing research community by providing a flexible toolkit to
-reimplement existing methods and develop their own new OCR methods. ## Citation
-If you find this project useful in your research, please consider cite:
-```bibtex @article{mmocr2021, title={MMOCR: A Comprehensive Toolbox for Text
-Detection, Recognition and Understanding}, author={Kuang, Zhanghui and Sun,
-Hongbin and Li, Zhizhong and Yue, Xiaoyu and Lin, Tsui Hin and Chen, Jianyong
-and Wei, Huaqiang and Zhu, Yiqin and Gao, Tong and Zhang, Wenwei and Chen, Kai
-and Zhang, Wayne and Lin, Dahua}, journal= {arXiv preprint arXiv:2108.06543},
-year={2021} } ``` ## License This project is released under the [Apache 2.0
-license](LICENSE). ## Projects in OpenMMLab - [MMEngine](https://github.com/
-open-mmlab/mmengine): OpenMMLab foundational library for training deep learning
-models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational
-library for computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM
-installs OpenMMLab packages. - [MMClassification](https://github.com/open-
-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
-- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
-toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
-mmdetection3d): OpenMMLab's next-generation platform for general 3D object
-detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
-rotated object detection toolbox and benchmark. - [MMSegmentation](https://
-github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox
-and benchmark. - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text
-detection, recognition, and understanding toolbox. - [MMPose](https://
-github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
-- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human
-parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/open-
-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark. -
-[MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression
-toolbox and benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot):
-OpenMMLab fewshot learning toolbox and benchmark. - [MMAction2](https://
-github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action
-understanding toolbox and benchmark. - [MMTracking](https://github.com/open-
-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark. - [MMFlow]
-(https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and
-benchmark. - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab
-image and video editing toolbox. - [MMGeneration](https://github.com/open-
-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox. -
-[MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment
-framework. ## Welcome to the OpenMMLab community Scan the QR code below to
-follow the OpenMMLab team's [**Zhihu Official Account**](https://www.zhihu.com/
-people/openmmlab) and join the OpenMMLab team's [**QQ Group**](https://
-jq.qq.com/?_wv=1027&k=aCvMxdr3), or join the official communication WeChat
-group by adding the WeChat, or join our [**Slack**](https://join.slack.com/t/
-mmocrworkspace/shared_invite/zt-1ifqhfla8-yKnLO_aKhVA2h71OrK8GZw)
+ABCNet/README.md) (CVPR'2020) - [x] [ABCNetV2](projects/ABCNet/README_V2.md)
+(TPAMI'2021) - [x] [SPTS](projects/SPTS/README.md) (ACM MM'2022)  Please refer
+to [model_zoo](https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more
+details. ## Contributing We appreciate all contributions to improve MMOCR.
+Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing
+guidelines. ## Acknowledgement MMOCR is an open-source project that is
+contributed by researchers and engineers from various colleges and companies.
+We appreciate all the contributors who implement their methods or add new
+features, as well as users who give valuable feedbacks. We hope the toolbox and
+benchmark could serve the growing research community by providing a flexible
+toolkit to reimplement existing methods and develop their own new OCR methods.
+## Citation If you find this project useful in your research, please consider
+cite: ```bibtex @article{mmocr2021, title={MMOCR: A Comprehensive Toolbox for
+Text Detection, Recognition and Understanding}, author={Kuang, Zhanghui and
+Sun, Hongbin and Li, Zhizhong and Yue, Xiaoyu and Lin, Tsui Hin and Chen,
+Jianyong and Wei, Huaqiang and Zhu, Yiqin and Gao, Tong and Zhang, Wenwei and
+Chen, Kai and Zhang, Wayne and Lin, Dahua}, journal= {arXiv preprint arXiv:
+2108.06543}, year={2021} } ``` ## License This project is released under the
+[Apache 2.0 license](LICENSE). ## Projects in OpenMMLab - [MMEngine](https://
+github.com/open-mmlab/mmengine): OpenMMLab foundational library for training
+deep learning models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab
+foundational library for computer vision. - [MIM](https://github.com/open-
+mmlab/mim): MIM installs OpenMMLab packages. - [MMClassification](https://
+github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox
+and benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection):
+OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
+github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for
+general 3D object detection. - [MMRotate](https://github.com/open-mmlab/
+mmrotate): OpenMMLab rotated object detection toolbox and benchmark. -
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
+model deployment framework. ## Welcome to the OpenMMLab community Scan the QR
+code below to follow the OpenMMLab team's [**Zhihu Official Account**](https://
+www.zhihu.com/people/openmmlab) and join the OpenMMLab team's [**QQ Group**]
+(https://jq.qq.com/?_wv=1027&k=aCvMxdr3), or join the official communication
+WeChat group by adding the WeChat, or join our [**Slack**](https://
+join.slack.com/t/mmocrworkspace/shared_invite/zt-1ifqhfla8-
+yKnLO_aKhVA2h71OrK8GZw)
   [https://raw.githubusercontent.com/open-mmlab/mmcv/master/docs/en/_static/
  zhihu_qrcode.jpg] [https://raw.githubusercontent.com/open-mmlab/mmcv/master/
  docs/en/_static/qq_group_qrcode.jpg] [https://raw.githubusercontent.com/open-
              mmlab/mmcv/master/docs/en/_static/wechat_qrcode.jpg]
 We will provide you with the OpenMMLab community - ð¢ share the latest core
 technologies of AI frameworks - ð» Explaining PyTorch common module source
 Code - ð° News related to the release of OpenMMLab - ð Introduction of
```

### Comparing `mmocr-1.0.0rc5/README.md` & `mmocr-1.0.0rc6/README.md`

 * *Files 14% similar despite different names*

```diff
@@ -36,14 +36,45 @@
 </div>
 
 <div align="center">
 
 English | [简体中文](README_zh-CN.md)
 
 </div>
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
+## Latest Updates
+
+**The default branch has been switched to `1.x` from `main`, and we encourage
+users to migrate to the latest version, though it comes with some cost. Please refer to [Migration Guide](https://mmocr.readthedocs.io/en/dev-1.x/migration/overview.html) for more
+details.**
+
+v1.0.0rc6 was released in 2023-03-07.
+
+1. Two new models, ABCNet v2 (inference only) and SPTS are added to `projects/` folder.
+2. Announcing `Inferencer`, a unified inference interface in OpenMMLab for everyone's easy access and quick inference with all the pre-trained weights. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/inference.html)
+3. Users can use test-time augmentation for text recognition tasks. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/train_test.html#test-time-augmentation)
+4. Support [batch augmentation](https://openaccess.thecvf.com/content_CVPR_2020/papers/Hoffer_Augment_Your_Batch_Improving_Generalization_Through_Instance_Repetition_CVPR_2020_paper.pdf) through [`BatchAugSampler`](https://github.com/open-mmlab/mmocr/pull/1757), which is a technique used in SPTS.
+5. Dataset Preparer has been refactored to allow more flexible configurations. Besides, users are now able to prepare text recognition datasets in LMDB formats. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/dataset_preparer.html#lmdb-format)
+6. Some textspotting datasets have been revised to enhance the correctness and consistency with the common practice.
+7. Potential spurious warnings from `shapely` have been eliminated.
+
+Read [Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for more details!
 
 ## Introduction
 
 MMOCR is an open-source toolbox based on PyTorch and mmdetection for text detection, text recognition, and the corresponding downstream tasks including key information extraction. It is part of the [OpenMMLab](https://openmmlab.com/) project.
 
 The main branch works with **PyTorch 1.6+**.
 
@@ -65,25 +96,14 @@
 
   The modular design of MMOCR enables users to define their own optimizers, data preprocessors, and model components such as backbones, necks and heads as well as losses. Please refer to [Overview](https://mmocr.readthedocs.io/en/dev-1.x/get_started/overview.html) for how to construct a customized model.
 
 - **Numerous Utilities**
 
   The toolbox provides a comprehensive set of utilities which can help users assess the performance of models. It includes visualizers which allow visualization of images, ground truths as well as predicted bounding boxes, and a validation tool for evaluating checkpoints during training.  It also includes data converters to demonstrate how to convert your own data to the annotation files which the toolbox supports.
 
-## Latest Updates
-
-v1.0.0rc5 was released in 2023-01-06.
-
-1. Two models, Aster and SVTR, are added to our model zoo. The full implementation of ABCNet is also available now.
-2. Dataset Preparer supports 5 more datasets: CocoTextV2, FUNSD, TextOCR, NAF, SROIE.
-3. We have 4 more text recognition transforms, and two more helper transforms.
-4. The transform, `FixInvalidPolygon`, is getting smarter at dealing with invalid polygons, and now capable of handling more weird annotations. As a result, a complete training cycle on TotalText dataset can be performed bug-free. The weights of DBNet and FCENet pretrained on TotalText are also released.
-
-Read [Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for more details!
-
 ## What's New in MMOCR 1.0
 
 1. **New engines**. MMOCR 1.x is based on [MMEngine](https://github.com/open-mmlab/mmengine), which provides a general and powerful runner that allows more flexible customizations and significantly simplifies the entrypoints of high-level interfaces.
 
 2. **Unified interfaces**. As a part of the OpenMMLab 2.0 projects, MMOCR 1.x unifies and refactors the interfaces and internal logics of train, testing, datasets, models, evaluation, and visualization. All the OpenMMLab 2.0 projects share the same design in those interfaces and logics to allow the emergence of multi-task/modality algorithms.
 
 3. **Cross project calling**. Benefiting from the unified design, you can use the models implemented in other OpenMMLab projects, such as MMDet. We provide an example of how to use MMDetection's Mask R-CNN through `MMDetWrapper`. Check our documents for more details. More wrappers will be released in the future.
@@ -167,14 +187,16 @@
 
 </details>
 
 <details open>
 <summary>Text Spotting</summary>
 
 - [x] [ABCNet](projects/ABCNet/README.md) (CVPR'2020)
+- [x] [ABCNetV2](projects/ABCNet/README_V2.md) (TPAMI'2021)
+- [x] [SPTS](projects/SPTS/README.md) (ACM MM'2022)
 
 </details>
 
 Please refer to [model_zoo](https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more details.
 
 ## Contributing
```

#### html2text {}

```diff
@@ -17,19 +17,41 @@
  2.amazonaws.com/assets/try_on_tiyaro_badge.svg] [ðDocumentation](https://
       mmocr.readthedocs.io/en/dev-1.x/) | [ð ï¸Installation](https://
   mmocr.readthedocs.io/en/dev-1.x/get_started/install.html) | [ðModel Zoo]
   (https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) | [ðUpdate News]
 (https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) | [ð¤Reporting
         Issues](https://github.com/open-mmlab/mmocr/issues/new/choose)
                    English | [ç®ä½ä¸­æ](README_zh-CN.md)
-## Introduction MMOCR is an open-source toolbox based on PyTorch and
-mmdetection for text detection, text recognition, and the corresponding
-downstream tasks including key information extraction. It is part of the
-[OpenMMLab](https://openmmlab.com/) project. The main branch works with
-**PyTorch 1.6+**.
+
+## Latest Updates **The default branch has been switched to `1.x` from `main`,
+and we encourage users to migrate to the latest version, though it comes with
+some cost. Please refer to [Migration Guide](https://mmocr.readthedocs.io/en/
+dev-1.x/migration/overview.html) for more details.** v1.0.0rc6 was released in
+2023-03-07. 1. Two new models, ABCNet v2 (inference only) and SPTS are added to
+`projects/` folder. 2. Announcing `Inferencer`, a unified inference interface
+in OpenMMLab for everyone's easy access and quick inference with all the pre-
+trained weights. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/
+inference.html) 3. Users can use test-time augmentation for text recognition
+tasks. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/
+train_test.html#test-time-augmentation) 4. Support [batch augmentation](https:/
+/openaccess.thecvf.com/content_CVPR_2020/papers/
+Hoffer_Augment_Your_Batch_Improving_Generalization_Through_Instance_Repetition_CVPR_2020_paper.pdf)
+through [`BatchAugSampler`](https://github.com/open-mmlab/mmocr/pull/1757),
+which is a technique used in SPTS. 5. Dataset Preparer has been refactored to
+allow more flexible configurations. Besides, users are now able to prepare text
+recognition datasets in LMDB formats. [Docs](https://mmocr.readthedocs.io/en/
+dev-1.x/user_guides/data_prepare/dataset_preparer.html#lmdb-format) 6. Some
+textspotting datasets have been revised to enhance the correctness and
+consistency with the common practice. 7. Potential spurious warnings from
+`shapely` have been eliminated. Read [Changelog](https://mmocr.readthedocs.io/
+en/dev-1.x/notes/changelog.html) for more details! ## Introduction MMOCR is an
+open-source toolbox based on PyTorch and mmdetection for text detection, text
+recognition, and the corresponding downstream tasks including key information
+extraction. It is part of the [OpenMMLab](https://openmmlab.com/) project. The
+main branch works with **PyTorch 1.6+**.
  [https://user-images.githubusercontent.com/24622904/187838618-1fdc61c0-2d46-
                           49f9-8502-976ffdf01f28.png]
 ### Major Features - **Comprehensive Pipeline** The toolbox supports not only
 text detection and text recognition, but also their downstream tasks such as
 key information extraction. - **Multiple Models** The toolbox supports a wide
 variety of state-of-the-art models for text detection, text recognition and key
 information extraction. - **Modular Design** The modular design of MMOCR
@@ -38,44 +60,35 @@
 to [Overview](https://mmocr.readthedocs.io/en/dev-1.x/get_started/
 overview.html) for how to construct a customized model. - **Numerous
 Utilities** The toolbox provides a comprehensive set of utilities which can
 help users assess the performance of models. It includes visualizers which
 allow visualization of images, ground truths as well as predicted bounding
 boxes, and a validation tool for evaluating checkpoints during training. It
 also includes data converters to demonstrate how to convert your own data to
-the annotation files which the toolbox supports. ## Latest Updates v1.0.0rc5
-was released in 2023-01-06. 1. Two models, Aster and SVTR, are added to our
-model zoo. The full implementation of ABCNet is also available now. 2. Dataset
-Preparer supports 5 more datasets: CocoTextV2, FUNSD, TextOCR, NAF, SROIE. 3.
-We have 4 more text recognition transforms, and two more helper transforms. 4.
-The transform, `FixInvalidPolygon`, is getting smarter at dealing with invalid
-polygons, and now capable of handling more weird annotations. As a result, a
-complete training cycle on TotalText dataset can be performed bug-free. The
-weights of DBNet and FCENet pretrained on TotalText are also released. Read
-[Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for
-more details! ## What's New in MMOCR 1.0 1. **New engines**. MMOCR 1.x is based
-on [MMEngine](https://github.com/open-mmlab/mmengine), which provides a general
-and powerful runner that allows more flexible customizations and significantly
-simplifies the entrypoints of high-level interfaces. 2. **Unified interfaces**.
-As a part of the OpenMMLab 2.0 projects, MMOCR 1.x unifies and refactors the
-interfaces and internal logics of train, testing, datasets, models, evaluation,
-and visualization. All the OpenMMLab 2.0 projects share the same design in
-those interfaces and logics to allow the emergence of multi-task/modality
-algorithms. 3. **Cross project calling**. Benefiting from the unified design,
-you can use the models implemented in other OpenMMLab projects, such as MMDet.
-We provide an example of how to use MMDetection's Mask R-CNN through
-`MMDetWrapper`. Check our documents for more details. More wrappers will be
-released in the future. 4. **Stronger visualization**. We provide a series of
-useful tools which are mostly based on brand-new visualizers. As a result, it
-is more convenient for the users to explore the models and datasets now. 5.
-**More documentation and tutorials**. We add a bunch of documentation and
-tutorials to help users get started more smoothly. Read it [here](https://
-mmocr.readthedocs.io/en/dev-1.x/). 6. **One-stop Dataset Preparaion**. Multiple
-datasets are instantly ready with only one line of command, via our [Dataset
-Preparer](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/
+the annotation files which the toolbox supports. ## What's New in MMOCR 1.0 1.
+**New engines**. MMOCR 1.x is based on [MMEngine](https://github.com/open-
+mmlab/mmengine), which provides a general and powerful runner that allows more
+flexible customizations and significantly simplifies the entrypoints of high-
+level interfaces. 2. **Unified interfaces**. As a part of the OpenMMLab 2.0
+projects, MMOCR 1.x unifies and refactors the interfaces and internal logics of
+train, testing, datasets, models, evaluation, and visualization. All the
+OpenMMLab 2.0 projects share the same design in those interfaces and logics to
+allow the emergence of multi-task/modality algorithms. 3. **Cross project
+calling**. Benefiting from the unified design, you can use the models
+implemented in other OpenMMLab projects, such as MMDet. We provide an example
+of how to use MMDetection's Mask R-CNN through `MMDetWrapper`. Check our
+documents for more details. More wrappers will be released in the future. 4.
+**Stronger visualization**. We provide a series of useful tools which are
+mostly based on brand-new visualizers. As a result, it is more convenient for
+the users to explore the models and datasets now. 5. **More documentation and
+tutorials**. We add a bunch of documentation and tutorials to help users get
+started more smoothly. Read it [here](https://mmocr.readthedocs.io/en/dev-1.x/
+). 6. **One-stop Dataset Preparaion**. Multiple datasets are instantly ready
+with only one line of command, via our [Dataset Preparer](https://
+mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/
 dataset_preparer.html). 7. **Embracing more `projects/`**: We now introduce
 `projects/` folder, where some experimental features, frameworks and models can
 be placed, only needed to satisfy the minimum requirement on the code quality.
 Everyone is welcome to post their implementation of any great ideas in this
 folder! Learn more from our [example project](https://github.com/open-mmlab/
 mmocr/blob/dev-1.x/projects/example_project/). 8. **More models**. MMOCR 1.0
 supports more tasks and more state-of-the-art models! ## Installation MMOCR
@@ -105,66 +118,68 @@
 README.md) (PR'2021) - [x] [NRTR](configs/textrecog/nrtr/README.md)
 (ICDAR'2019) - [x] [RobustScanner](configs/textrecog/robust_scanner/README.md)
 (ECCV'2020) - [x] [SAR](configs/textrecog/sar/README.md) (AAAI'2019) - [x]
 [SATRN](configs/textrecog/satrn/README.md) (CVPR'2020 Workshop on Text and
 Documents in the Deep Learning Era) - [x] [SVTR](configs/textrecog/svtr/
 README.md) (IJCAI'2022)   Key Information Extraction - [x] [SDMG-R](configs/
 kie/sdmgr/README.md) (ArXiv'2021)   Text Spotting - [x] [ABCNet](projects/
-ABCNet/README.md) (CVPR'2020)  Please refer to [model_zoo](https://
-mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more details. ##
-Contributing We appreciate all contributions to improve MMOCR. Please refer to
-[CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guidelines. ##
-Acknowledgement MMOCR is an open-source project that is contributed by
-researchers and engineers from various colleges and companies. We appreciate
-all the contributors who implement their methods or add new features, as well
-as users who give valuable feedbacks. We hope the toolbox and benchmark could
-serve the growing research community by providing a flexible toolkit to
-reimplement existing methods and develop their own new OCR methods. ## Citation
-If you find this project useful in your research, please consider cite:
-```bibtex @article{mmocr2021, title={MMOCR: A Comprehensive Toolbox for Text
-Detection, Recognition and Understanding}, author={Kuang, Zhanghui and Sun,
-Hongbin and Li, Zhizhong and Yue, Xiaoyu and Lin, Tsui Hin and Chen, Jianyong
-and Wei, Huaqiang and Zhu, Yiqin and Gao, Tong and Zhang, Wenwei and Chen, Kai
-and Zhang, Wayne and Lin, Dahua}, journal= {arXiv preprint arXiv:2108.06543},
-year={2021} } ``` ## License This project is released under the [Apache 2.0
-license](LICENSE). ## Projects in OpenMMLab - [MMEngine](https://github.com/
-open-mmlab/mmengine): OpenMMLab foundational library for training deep learning
-models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational
-library for computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM
-installs OpenMMLab packages. - [MMClassification](https://github.com/open-
-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
-- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
-toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
-mmdetection3d): OpenMMLab's next-generation platform for general 3D object
-detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
-rotated object detection toolbox and benchmark. - [MMSegmentation](https://
-github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox
-and benchmark. - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text
-detection, recognition, and understanding toolbox. - [MMPose](https://
-github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
-- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human
-parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/open-
-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark. -
-[MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression
-toolbox and benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot):
-OpenMMLab fewshot learning toolbox and benchmark. - [MMAction2](https://
-github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action
-understanding toolbox and benchmark. - [MMTracking](https://github.com/open-
-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark. - [MMFlow]
-(https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and
-benchmark. - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab
-image and video editing toolbox. - [MMGeneration](https://github.com/open-
-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox. -
-[MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment
-framework. ## Welcome to the OpenMMLab community Scan the QR code below to
-follow the OpenMMLab team's [**Zhihu Official Account**](https://www.zhihu.com/
-people/openmmlab) and join the OpenMMLab team's [**QQ Group**](https://
-jq.qq.com/?_wv=1027&k=aCvMxdr3), or join the official communication WeChat
-group by adding the WeChat, or join our [**Slack**](https://join.slack.com/t/
-mmocrworkspace/shared_invite/zt-1ifqhfla8-yKnLO_aKhVA2h71OrK8GZw)
+ABCNet/README.md) (CVPR'2020) - [x] [ABCNetV2](projects/ABCNet/README_V2.md)
+(TPAMI'2021) - [x] [SPTS](projects/SPTS/README.md) (ACM MM'2022)  Please refer
+to [model_zoo](https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more
+details. ## Contributing We appreciate all contributions to improve MMOCR.
+Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing
+guidelines. ## Acknowledgement MMOCR is an open-source project that is
+contributed by researchers and engineers from various colleges and companies.
+We appreciate all the contributors who implement their methods or add new
+features, as well as users who give valuable feedbacks. We hope the toolbox and
+benchmark could serve the growing research community by providing a flexible
+toolkit to reimplement existing methods and develop their own new OCR methods.
+## Citation If you find this project useful in your research, please consider
+cite: ```bibtex @article{mmocr2021, title={MMOCR: A Comprehensive Toolbox for
+Text Detection, Recognition and Understanding}, author={Kuang, Zhanghui and
+Sun, Hongbin and Li, Zhizhong and Yue, Xiaoyu and Lin, Tsui Hin and Chen,
+Jianyong and Wei, Huaqiang and Zhu, Yiqin and Gao, Tong and Zhang, Wenwei and
+Chen, Kai and Zhang, Wayne and Lin, Dahua}, journal= {arXiv preprint arXiv:
+2108.06543}, year={2021} } ``` ## License This project is released under the
+[Apache 2.0 license](LICENSE). ## Projects in OpenMMLab - [MMEngine](https://
+github.com/open-mmlab/mmengine): OpenMMLab foundational library for training
+deep learning models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab
+foundational library for computer vision. - [MIM](https://github.com/open-
+mmlab/mim): MIM installs OpenMMLab packages. - [MMClassification](https://
+github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox
+and benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection):
+OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
+github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for
+general 3D object detection. - [MMRotate](https://github.com/open-mmlab/
+mmrotate): OpenMMLab rotated object detection toolbox and benchmark. -
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
+model deployment framework. ## Welcome to the OpenMMLab community Scan the QR
+code below to follow the OpenMMLab team's [**Zhihu Official Account**](https://
+www.zhihu.com/people/openmmlab) and join the OpenMMLab team's [**QQ Group**]
+(https://jq.qq.com/?_wv=1027&k=aCvMxdr3), or join the official communication
+WeChat group by adding the WeChat, or join our [**Slack**](https://
+join.slack.com/t/mmocrworkspace/shared_invite/zt-1ifqhfla8-
+yKnLO_aKhVA2h71OrK8GZw)
   [https://raw.githubusercontent.com/open-mmlab/mmcv/master/docs/en/_static/
  zhihu_qrcode.jpg] [https://raw.githubusercontent.com/open-mmlab/mmcv/master/
  docs/en/_static/qq_group_qrcode.jpg] [https://raw.githubusercontent.com/open-
              mmlab/mmcv/master/docs/en/_static/wechat_qrcode.jpg]
 We will provide you with the OpenMMLab community - ð¢ share the latest core
 technologies of AI frameworks - ð» Explaining PyTorch common module source
 Code - ð° News related to the release of OpenMMLab - ð Introduction of
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/datasets/wildreceipt-openset.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/datasets/wildreceipt-openset.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/_base_/default_runtime.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/_base_/default_runtime.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 default_scope = 'mmocr'
 env_cfg = dict(
-    cudnn_benchmark=True,
+    cudnn_benchmark=False,
     mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
     dist_cfg=dict(backend='nccl'),
 )
 randomness = dict(seed=None)
 
 default_hooks = dict(
     timer=dict(type='IterTimerHook'),
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_novisual.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_novisual.py`

 * *Files 3% similar despite different names*

```diff
@@ -6,15 +6,15 @@
         type='SDMGRHead',
         visual_dim=16,
         num_classes=num_classes,
         module_loss=dict(type='SDMGRModuleLoss'),
         postprocessor=dict(type='SDMGRPostProcessor')),
     dictionary=dict(
         type='Dictionary',
-        dict_file='data/kie/wildreceipt/dict.txt',
+        dict_file='{{ fileDirname }}/../../../dicts/sdmgr_dict.txt',
         with_padding=True,
         with_unknown=True,
         unknown_token=None),
 )
 
 train_pipeline = [
     dict(type='LoadKIEAnnotations'),
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_unet16.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_unet16.py`

 * *Files 9% similar despite different names*

```diff
@@ -20,9 +20,9 @@
     dict(type='Resize', scale=(1024, 512), keep_ratio=True),
     dict(type='PackKIEInputs')
 ]
 test_pipeline = [
     dict(type='LoadImageFromFile'),
     dict(type='LoadKIEAnnotations'),
     dict(type='Resize', scale=(1024, 512), keep_ratio=True),
-    dict(type='PackKIEInputs'),
+    dict(type='PackKIEInputs', meta_keys=('img_path', )),
 ]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt-openset.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt-openset.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/icdar2017.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/icdar2017.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/datasets/synthtext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/datasets/synthtext.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/default_runtime.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/default_runtime.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 default_scope = 'mmocr'
 env_cfg = dict(
-    cudnn_benchmark=True,
+    cudnn_benchmark=False,
     mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
     dist_cfg=dict(backend='nccl'),
 )
 randomness = dict(seed=None)
 
 default_hooks = dict(
     timer=dict(type='IterTimerHook'),
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_base.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/_base_/schedules/schedule_sgd_base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet18_fpnc.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet18_fpnc.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet50-dcnv2_fpnc.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/_base_dbnet_resnet50-dcnv2_fpnc.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_100k_synthtext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_100k_synthtext.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 _base_ = [
-    '_base_dbnet_resnet18_fpnc.py',
-    '../_base_/datasets/synthtext.py',
+    '_base_dbnet_resnet50-dcnv2_fpnc.py',
     '../_base_/default_runtime.py',
+    '../_base_/datasets/synthtext.py',
     '../_base_/schedules/schedule_sgd_100k.py',
 ]
 
 # dataset settings
 synthtext_textdet_train = _base_.synthtext_textdet_train
 synthtext_textdet_train.pipeline = _base_.train_pipeline
 synthtext_textdet_test = _base_.synthtext_textdet_test
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_totaltext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet18_fpnc_1200e_totaltext.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_100k_synthtext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/drrg_resnet50_fpn-unet_1200e_ctw1500.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 _base_ = [
-    '_base_dbnet_resnet50-dcnv2_fpnc.py',
+    '_base_drrg_resnet50_fpn-unet.py',
+    '../_base_/datasets/ctw1500.py',
     '../_base_/default_runtime.py',
-    '../_base_/datasets/synthtext.py',
-    '../_base_/schedules/schedule_sgd_100k.py',
+    '../_base_/schedules/schedule_sgd_1200e.py',
 ]
 
 # dataset settings
-synthtext_textdet_train = _base_.synthtext_textdet_train
-synthtext_textdet_train.pipeline = _base_.train_pipeline
-synthtext_textdet_test = _base_.synthtext_textdet_test
-synthtext_textdet_test.pipeline = _base_.test_pipeline
+ctw1500_textdet_train = _base_.ctw1500_textdet_train
+ctw1500_textdet_train.pipeline = _base_.train_pipeline
+ctw1500_textdet_test = _base_.ctw1500_textdet_test
+ctw1500_textdet_test.pipeline = _base_.test_pipeline
 
 train_dataloader = dict(
-    batch_size=16,
-    num_workers=8,
+    batch_size=4,
+    num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=True),
-    dataset=synthtext_textdet_train)
+    dataset=ctw1500_textdet_train)
 
 val_dataloader = dict(
     batch_size=1,
-    num_workers=4,
+    num_workers=1,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
-    dataset=synthtext_textdet_test)
+    dataset=ctw1500_textdet_test)
 
 test_dataloader = val_dataloader
 
 auto_scale_lr = dict(base_batch_size=16)
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-oclip_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50-oclip_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/dbnet_resnet50_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnet/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnet/metafile.yml`

 * *Files 2% similar despite different names*

```diff
@@ -53,15 +53,15 @@
     Weights: https://download.openmmlab.com/mmocr/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015_20220828_124917-452c443c.pth
 
   - Name: dbnet_resnet50-oclip_fpnc_1200e_icdar2015
     In Collection: DBNet
     Alias:
       - DB_r50
       - DBNet
-    Config: configs/textdet/dbnet/dbnet_resnet50-dcnv2_fpnc_1200e_icdar2015.py
+    Config: configs/textdet/dbnet/dbnet_resnet50-oclip_1200e_icdar2015.py
     Metadata:
       Training Data: ICDAR2015
     Results:
       - Task: Text Detection
         Dataset: ICDAR2015
         Metrics:
           hmean-iou: 0.8644
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/_base_dbnetpp_resnet50-dcnv2_fpnc.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/_base_dbnetpp_resnet50-dcnv2_fpnc.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_100k_synthtext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_toy.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,34 +1,36 @@
 _base_ = [
-    '_base_dbnetpp_resnet50-dcnv2_fpnc.py',
+    '../_base_/datasets/toy_data.py',
     '../_base_/default_runtime.py',
-    '../_base_/datasets/synthtext.py',
-    '../_base_/schedules/schedule_sgd_100k.py',
+    '../_base_/schedules/schedule_adam_step_5e.py',
+    '_base_sar_resnet31_parallel-decoder.py',
 ]
 
 # dataset settings
-train_list = [_base_.synthtext_textdet_train]
-test_list = [_base_.synthtext_textdet_test]
+train_list = [_base_.toy_rec_train]
+test_list = [_base_.toy_rec_test]
+default_hooks = dict(logger=dict(type='LoggerHook', interval=1))
 
 train_dataloader = dict(
-    batch_size=16,
-    num_workers=8,
+    batch_size=1,
+    num_workers=4,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=True),
     dataset=dict(
         type='ConcatDataset',
         datasets=train_list,
         pipeline=_base_.train_pipeline))
 
 val_dataloader = dict(
-    batch_size=16,
-    num_workers=8,
+    batch_size=1,
+    num_workers=4,
     persistent_workers=True,
+    drop_last=False,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=dict(
         type='ConcatDataset',
         datasets=test_list,
         pipeline=_base_.test_pipeline))
-
 test_dataloader = val_dataloader
 
-auto_scale_lr = dict(base_batch_size=16)
+val_evaluator = dict(dataset_prefixes=['Toy'])
+test_evaluator = val_evaluator
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-dcnv2_fpnc_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-oclip_fpnc_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50-oclip_fpnc_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50_fpnc_1200e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/dbnetpp_resnet50_fpnc_1200e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/dbnetpp/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/dbnetpp/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/_base_drrg_resnet50_fpn-unet.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/_base_drrg_resnet50_fpn-unet.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/drrg_resnet50_fpn-unet_1200e_ctw1500.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/textsnake_resnet50_fpn-unet_1200e_ctw1500.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 _base_ = [
-    '_base_drrg_resnet50_fpn-unet.py',
+    '_base_textsnake_resnet50_fpn-unet.py',
     '../_base_/datasets/ctw1500.py',
     '../_base_/default_runtime.py',
     '../_base_/schedules/schedule_sgd_1200e.py',
 ]
 
 # dataset settings
 ctw1500_textdet_train = _base_.ctw1500_textdet_train
@@ -23,8 +23,8 @@
     num_workers=1,
     persistent_workers=True,
     sampler=dict(type='DefaultSampler', shuffle=False),
     dataset=ctw1500_textdet_test)
 
 test_dataloader = val_dataloader
 
-auto_scale_lr = dict(base_batch_size=16)
+auto_scale_lr = dict(base_batch_size=4)
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/drrg/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/drrg/metafile.yml`

 * *Files 22% similar despite different names*

```diff
@@ -22,19 +22,7 @@
       Training Data: CTW1500
     Results:
       - Task: Text Detection
         Dataset: CTW1500
         Metrics:
           hmean-iou: 0.8467
     Weights: https://download.openmmlab.com/mmocr/textdet/drrg/drrg_resnet50_fpn-unet_1200e_ctw1500/drrg_resnet50_fpn-unet_1200e_ctw1500_20220827_105233-d5c702dd.pth
-
-  - Name: drrg_resnet50-oclip_fpn-unet_1200e_ctw1500
-    In Collection: DRRG
-    Config: configs/textdet/drrg/drrg_resnet50-oclip_fpn-unet_1200e_ctw1500.py
-    Metadata:
-      Training Data: CTW1500
-    Results:
-      - Task: Text Detection
-        Dataset: CTW1500
-        Metrics:
-          hmean-iou:
-    Weights:
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50-dcnv2_fpn.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50-dcnv2_fpn.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50_fpn.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/_base_fcenet_resnet50_fpn.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-dcnv2_fpn_1500e_ctw1500.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50-dcnv2_fpn_1500e_ctw1500.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_totaltext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/fcenet_resnet50_fpn_1500e_totaltext.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/fcenet/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/fcenet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/_base_mask-rcnn_resnet50_fpn.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/_base_mask-rcnn_resnet50_fpn.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_ctw1500.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_ctw1500.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/maskrcnn/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/maskrcnn/metafile.yml`

 * *Files 10% similar despite different names*

```diff
@@ -22,47 +22,47 @@
     Config: configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_ctw1500.py
     Metadata:
       Training Data: CTW1500
     Results:
       - Task: Text Detection
         Dataset: CTW1500
         Metrics:
-          hmean: 0.7458
+          hmean-iou: 0.7458
     Weights: https://download.openmmlab.com/mmocr/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_ctw1500/mask-rcnn_resnet50_fpn_160e_ctw1500_20220826_154755-ce68ee8e.pth
 
   - Name: mask-rcnn_resnet50-oclip_fpn_160e_ctw1500
     In Collection: Mask R-CNN
     Config: configs/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_ctw1500.py
     Metadata:
       Training Data: CTW1500
     Results:
       - Task: Text Detection
         Dataset: CTW1500
         Metrics:
-          hmean: 0.7562
+          hmean-iou: 0.7562
     Weights: https://download.openmmlab.com/mmocr/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_ctw1500/mask-rcnn_resnet50-oclip_fpn_160e_ctw1500_20221101_154448-6e9e991c.pth
 
   - Name: mask-rcnn_resnet50_fpn_160e_icdar2015
     In Collection: Mask R-CNN
     Alias: MaskRCNN_IC15
     Config: configs/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2015.py
     Metadata:
       Training Data: ICDAR2015
     Results:
       - Task: Text Detection
         Dataset: ICDAR2015
         Metrics:
-          hmean: 0.8182
+          hmean-iou: 0.8182
     Weights: https://download.openmmlab.com/mmocr/textdet/maskrcnn/mask-rcnn_resnet50_fpn_160e_icdar2015/mask-rcnn_resnet50_fpn_160e_icdar2015_20220826_154808-ff5c30bf.pth
 
   - Name: mask-rcnn_resnet50-oclip_fpn_160e_icdar2015
     In Collection: Mask R-CNN
     Alias: MaskRCNN
     Config: configs/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_icdar2015.py
     Metadata:
       Training Data: ICDAR2015
     Results:
       - Task: Text Detection
         Dataset: ICDAR2015
         Metrics:
-          hmean: 0.8513
+          hmean-iou: 0.8513
     Weights: https://download.openmmlab.com/mmocr/textdet/maskrcnn/mask-rcnn_resnet50-oclip_fpn_160e_icdar2015/mask-rcnn_resnet50-oclip_fpn_160e_icdar2015_20221101_131357-a19f7802.pth
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/_base_panet_resnet18_fpem-ffm.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/_base_panet_resnet18_fpem-ffm.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/_base_panet_resnet50_fpem-ffm.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/_base_panet_resnet50_fpem-ffm.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_ctw1500.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_ctw1500.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/panet_resnet18_fpem-ffm_600e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/panet/panet_resnet50_fpem-ffm_600e_icdar2017.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/panet/panet_resnet50_fpem-ffm_600e_icdar2017.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/_base_psenet_resnet50_fpnf.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/_base_psenet_resnet50_fpnf.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_ctw1500.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_ctw1500.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2017.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/psenet/psenet_resnet50_fpnf_600e_icdar2017.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/_base_textsnake_resnet50_fpn-unet.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/_base_textsnake_resnet50_fpn-unet.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textdet/textsnake/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textdet/textsnake/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2013.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2013.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2015.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/icdar2015.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/mjsynth.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/mjsynth.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/datasets/synthtext.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/datasets/synthtext.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/default_runtime.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/default_runtime.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 default_scope = 'mmocr'
 env_cfg = dict(
-    cudnn_benchmark=True,
+    cudnn_benchmark=False,
     mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0),
     dist_cfg=dict(backend='nccl'),
 )
 randomness = dict(seed=None)
 
 default_hooks = dict(
     timer=dict(type='IterTimerHook'),
@@ -42,7 +42,9 @@
 
 # Visualization
 vis_backends = [dict(type='LocalVisBackend')]
 visualizer = dict(
     type='TextRecogLocalVisualizer',
     name='visualizer',
     vis_backends=vis_backends)
+
+tta_model = dict(type='EncoderDecoderRecognizerTTAModel')
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adam_base.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/_base_/schedules/schedule_adam_base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/_base_abinet-vision.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/_base_aster.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,118 +1,110 @@
+file_client_args = dict(backend='disk')
+
 dictionary = dict(
     type='Dictionary',
-    dict_file='{{ fileDirname }}/../../../dicts/lower_english_digits.txt',
-    with_start=True,
-    with_end=True,
+    dict_file='{{ fileDirname }}/../../../dicts/english_digits_symbols.txt',
+    with_padding=True,
+    with_unknown=True,
     same_start_end=True,
-    with_padding=False,
-    with_unknown=False)
+    with_start=True,
+    with_end=True)
 
 model = dict(
-    type='ABINet',
-    backbone=dict(type='ResNetABI'),
-    encoder=dict(
-        type='ABIEncoder',
-        n_layers=3,
-        n_head=8,
-        d_model=512,
-        d_inner=2048,
-        dropout=0.1,
-        max_len=8 * 32,
-    ),
+    type='ASTER',
+    preprocessor=dict(
+        type='STN',
+        in_channels=3,
+        resized_image_size=(32, 64),
+        output_image_size=(32, 100),
+        num_control_points=20),
+    backbone=dict(
+        type='ResNet',
+        in_channels=3,
+        stem_channels=[32],
+        block_cfgs=dict(type='BasicBlock', use_conv1x1='True'),
+        arch_layers=[3, 4, 6, 6, 3],
+        arch_channels=[32, 64, 128, 256, 512],
+        strides=[(2, 2), (2, 2), (2, 1), (2, 1), (2, 1)],
+        init_cfg=[
+            dict(type='Kaiming', layer='Conv2d'),
+            dict(type='Constant', val=1, layer='BatchNorm2d'),
+        ]),
+    encoder=dict(type='ASTEREncoder', in_channels=512),
     decoder=dict(
-        type='ABIFuser',
-        vision_decoder=dict(
-            type='ABIVisionDecoder',
-            in_channels=512,
-            num_channels=64,
-            attn_height=8,
-            attn_width=32,
-            attn_mode='nearest',
-            init_cfg=dict(type='Xavier', layer='Conv2d')),
-        module_loss=dict(type='ABIModuleLoss', letter_case='lower'),
+        type='ASTERDecoder',
+        max_seq_len=25,
+        in_channels=512,
+        emb_dims=512,
+        attn_dims=512,
+        hidden_size=512,
         postprocessor=dict(type='AttentionPostprocessor'),
+        module_loss=dict(
+            type='CEModuleLoss', flatten=True, ignore_first_char=True),
         dictionary=dictionary,
-        max_seq_len=26,
     ),
     data_preprocessor=dict(
         type='TextRecogDataPreprocessor',
-        mean=[123.675, 116.28, 103.53],
-        std=[58.395, 57.12, 57.375]))
-
-file_client_args = dict(backend='disk')
+        mean=[127.5, 127.5, 127.5],
+        std=[127.5, 127.5, 127.5]))
 
 train_pipeline = [
     dict(
         type='LoadImageFromFile',
         file_client_args=file_client_args,
         ignore_empty=True,
-        min_size=2),
+        min_size=5),
     dict(type='LoadOCRAnnotations', with_text=True),
-    dict(type='Resize', scale=(128, 32)),
-    dict(
-        type='RandomApply',
-        prob=0.5,
-        transforms=[
-            dict(
-                type='RandomChoice',
-                transforms=[
-                    dict(
-                        type='RandomRotate',
-                        max_angle=15,
-                    ),
-                    dict(
-                        type='TorchVisionWrapper',
-                        op='RandomAffine',
-                        degrees=15,
-                        translate=(0.3, 0.3),
-                        scale=(0.5, 2.),
-                        shear=(-45, 45),
-                    ),
-                    dict(
-                        type='TorchVisionWrapper',
-                        op='RandomPerspective',
-                        distortion_scale=0.5,
-                        p=1,
-                    ),
-                ])
-        ],
-    ),
-    dict(
-        type='RandomApply',
-        prob=0.25,
-        transforms=[
-            dict(type='PyramidRescale'),
-            dict(
-                type='mmdet.Albu',
-                transforms=[
-                    dict(type='GaussNoise', var_limit=(20, 20), p=0.5),
-                    dict(type='MotionBlur', blur_limit=6, p=0.5),
-                ]),
-        ]),
-    dict(
-        type='RandomApply',
-        prob=0.25,
-        transforms=[
-            dict(
-                type='TorchVisionWrapper',
-                op='ColorJitter',
-                brightness=0.5,
-                saturation=0.5,
-                contrast=0.5,
-                hue=0.1),
-        ]),
+    dict(type='Resize', scale=(256, 64)),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
 
 test_pipeline = [
     dict(type='LoadImageFromFile', file_client_args=file_client_args),
-    dict(type='Resize', scale=(128, 32)),
-    # add loading annotation after ``Resize`` because ground truth
-    # does not need to do resize data transform
+    dict(type='Resize', scale=(256, 64)),
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
-        meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
+        meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio',
+                   'instances'))
+]
+
+tta_pipeline = [
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[[
+            dict(
+                type='ConditionApply',
+                true_transforms=[
+                    dict(
+                        type='ImgAugWrapper',
+                        args=[dict(cls='Rot90', k=0, keep_size=False)])
+                ],
+                condition="results['img_shape'][1]<results['img_shape'][0]"),
+            dict(
+                type='ConditionApply',
+                true_transforms=[
+                    dict(
+                        type='ImgAugWrapper',
+                        args=[dict(cls='Rot90', k=1, keep_size=False)])
+                ],
+                condition="results['img_shape'][1]<results['img_shape'][0]"),
+            dict(
+                type='ConditionApply',
+                true_transforms=[
+                    dict(
+                        type='ImgAugWrapper',
+                        args=[dict(cls='Rot90', k=3, keep_size=False)])
+                ],
+                condition="results['img_shape'][1]<results['img_shape'][0]"),
+        ], [dict(type='Resize', scale=(256, 64))],
+                    [dict(type='LoadOCRAnnotations', with_text=True)],
+                    [
+                        dict(
+                            type='PackTextRecogInputs',
+                            meta_keys=('img_path', 'ori_shape', 'img_shape',
+                                       'valid_ratio', 'instances'))
+                    ]])
 ]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/abinet-vision_20e_st-an_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/abinet-vision_20e_st-an_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/abinet_20e_st-an_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/abinet_20e_st-an_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/abinet/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/abinet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/aster/aster_resnet45_6e_st_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/aster_resnet45_6e_st_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/aster/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/aster/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/_base_crnn_mini-vgg.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/_base_satrn_shallow.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,53 +1,113 @@
+file_client_args = dict(backend='disk')
+
 dictionary = dict(
     type='Dictionary',
-    dict_file='{{ fileDirname }}/../../../dicts/lower_english_digits.txt',
-    with_padding=True)
+    dict_file='{{ fileDirname }}/../../../dicts/english_digits_symbols.txt',
+    with_padding=True,
+    with_unknown=True,
+    same_start_end=True,
+    with_start=True,
+    with_end=True)
 
 model = dict(
-    type='CRNN',
-    preprocessor=None,
-    backbone=dict(type='MiniVGG', leaky_relu=False, input_channels=1),
-    encoder=None,
+    type='SATRN',
+    backbone=dict(type='ShallowCNN', input_channels=3, hidden_dim=512),
+    encoder=dict(
+        type='SATRNEncoder',
+        n_layers=12,
+        n_head=8,
+        d_k=512 // 8,
+        d_v=512 // 8,
+        d_model=512,
+        n_position=100,
+        d_inner=512 * 4,
+        dropout=0.1),
     decoder=dict(
-        type='CRNNDecoder',
-        in_channels=512,
-        rnn_flag=True,
-        module_loss=dict(type='CTCModuleLoss', letter_case='lower'),
-        postprocessor=dict(type='CTCPostProcessor'),
-        dictionary=dictionary),
+        type='NRTRDecoder',
+        n_layers=6,
+        d_embedding=512,
+        n_head=8,
+        d_model=512,
+        d_inner=512 * 4,
+        d_k=512 // 8,
+        d_v=512 // 8,
+        module_loss=dict(
+            type='CEModuleLoss', flatten=True, ignore_first_char=True),
+        dictionary=dictionary,
+        max_seq_len=25,
+        postprocessor=dict(type='AttentionPostprocessor')),
     data_preprocessor=dict(
-        type='TextRecogDataPreprocessor', mean=[127], std=[127]))
+        type='TextRecogDataPreprocessor',
+        mean=[123.675, 116.28, 103.53],
+        std=[58.395, 57.12, 57.375]))
 
-file_client_args = dict(backend='disk')
 train_pipeline = [
     dict(
         type='LoadImageFromFile',
-        color_type='grayscale',
         file_client_args=file_client_args,
         ignore_empty=True,
         min_size=2),
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(type='Resize', scale=(100, 32), keep_ratio=False),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
 
 test_pipeline = [
-    dict(
-        type='LoadImageFromFile',
-        color_type='grayscale',
-        file_client_args=file_client_args),
-    dict(
-        type='RescaleToHeight',
-        height=32,
-        min_width=32,
-        max_width=None,
-        width_divisor=16),
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(type='Resize', scale=(100, 32), keep_ratio=False),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
+
+tta_pipeline = [
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=0, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=1, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=3, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+            ],
+            [dict(type='Resize', scale=(100, 32), keep_ratio=False)],
+            # add loading annotation after ``Resize`` because ground truth
+            # does not need to do resize data transform
+            [dict(type='LoadOCRAnnotations', with_text=True)],
+            [
+                dict(
+                    type='PackTextRecogInputs',
+                    meta_keys=('img_path', 'ori_shape', 'img_shape',
+                               'valid_ratio'))
+            ]
+        ])
+]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_toy.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/crnn_mini-vgg_5e_toy.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/crnn/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/metafile.yml`

 * *Files 1% similar despite different names*

```diff
@@ -12,15 +12,15 @@
       - CRNNDecoder
   Paper:
     URL: https://arxiv.org/pdf/1507.05717.pdf
     Title: 'An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition'
   README: configs/textrecog/crnn/README.md
 
 Models:
-  - Name: crnn_mini-vgg_5e_mj-123
+  - Name: crnn_mini-vgg_5e_mj
     Alias: CRNN
     In Collection: CRNN
     Config: configs/textrecog/crnn/crnn_mini-vgg_5e_mj.py
     Metadata:
       Training Data: Syn90k
     Results:
       - Task: Text Recognition
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/_base_master_resnet31.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/_base_master_resnet31.py`

 * *Files 24% similar despite different names*

```diff
@@ -105,7 +105,62 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
+
+tta_pipeline = [
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=0, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=1, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=3, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+            ],
+            [
+                dict(
+                    type='RescaleToHeight',
+                    height=48,
+                    min_width=48,
+                    max_width=160,
+                    width_divisor=16)
+            ],
+            [dict(type='PadToWidth', width=160)],
+            # add loading annotation after ``Resize`` because ground truth
+            # does not need to do resize data transform
+            [dict(type='LoadOCRAnnotations', with_text=True)],
+            [
+                dict(
+                    type='PackTextRecogInputs',
+                    meta_keys=('img_path', 'ori_shape', 'img_shape',
+                               'valid_ratio'))
+            ]
+        ])
+]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_st_mj_sa.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_st_mj_sa.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_toy.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/master_resnet31_12e_toy.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/master/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/master/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_modality-transform.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_modality-transform.py`

 * *Files 23% similar despite different names*

```diff
@@ -56,7 +56,62 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
+
+tta_pipeline = [
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=0, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=1, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=3, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+            ],
+            [
+                dict(
+                    type='RescaleToHeight',
+                    height=32,
+                    min_width=32,
+                    max_width=160,
+                    width_divisor=16)
+            ],
+            [dict(type='PadToWidth', width=160)],
+            # add loading annotation after ``Resize`` because ground truth
+            # does not need to do resize data transform
+            [dict(type='LoadOCRAnnotations', with_text=True)],
+            [
+                dict(
+                    type='PackTextRecogInputs',
+                    meta_keys=('img_path', 'ori_shape', 'img_shape',
+                               'valid_ratio'))
+            ]
+        ])
+]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_resnet31.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/_base_nrtr_resnet31.py`

 * *Files 21% similar despite different names*

```diff
@@ -62,7 +62,62 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
+
+tta_pipeline = [
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=0, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=1, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=3, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+            ],
+            [
+                dict(
+                    type='RescaleToHeight',
+                    height=32,
+                    min_width=32,
+                    max_width=160,
+                    width_divisor=16)
+            ],
+            [dict(type='PadToWidth', width=160)],
+            # add loading annotation after ``Resize`` because ground truth
+            # does not need to do resize data transform
+            [dict(type='LoadOCRAnnotations', with_text=True)],
+            [
+                dict(
+                    type='PackTextRecogInputs',
+                    meta_keys=('img_path', 'ori_shape', 'img_shape',
+                               'valid_ratio'))
+            ]
+        ])
+]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_st_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_st_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_toy.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_modality-transform_6e_toy.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/nrtr/nrtr_resnet31-1by16-1by8_6e_st_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/nrtr/nrtr_resnet31-1by16-1by8_6e_st_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/_base_robustscanner_resnet31.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/_base_robustscanner_resnet31.py`

 * *Files 21% similar despite different names*

```diff
@@ -62,7 +62,62 @@
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
+
+tta_pipeline = [
+    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=0, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=1, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=3, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+            ],
+            [
+                dict(
+                    type='RescaleToHeight',
+                    height=48,
+                    min_width=48,
+                    max_width=160,
+                    width_divisor=4),
+            ],
+            [dict(type='PadToWidth', width=160)],
+            # add loading annotation after ``Resize`` because ground truth
+            # does not need to do resize data transform
+            [dict(type='LoadOCRAnnotations', with_text=True)],
+            [
+                dict(
+                    type='PackTextRecogInputs',
+                    meta_keys=('img_path', 'ori_shape', 'img_shape',
+                               'valid_ratio'))
+            ]
+        ])
+]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_st-sub_mj-sub_sa_real.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_st-sub_mj-sub_sa_real.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_toy.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/robust_scanner/robustscanner_resnet31_5e_toy.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/_base_sar_resnet31_parallel-decoder.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/crnn/_base_crnn_mini-vgg.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,73 +1,110 @@
 dictionary = dict(
     type='Dictionary',
-    dict_file='{{ fileDirname }}/../../../dicts/english_digits_symbols.txt',
-    with_start=True,
-    with_end=True,
-    same_start_end=True,
-    with_padding=True,
-    with_unknown=True)
+    dict_file='{{ fileDirname }}/../../../dicts/lower_english_digits.txt',
+    with_padding=True)
 
 model = dict(
-    type='SARNet',
-    data_preprocessor=dict(
-        type='TextRecogDataPreprocessor',
-        mean=[127, 127, 127],
-        std=[127, 127, 127]),
-    backbone=dict(type='ResNet31OCR'),
-    encoder=dict(
-        type='SAREncoder',
-        enc_bi_rnn=False,
-        enc_do_rnn=0.1,
-        enc_gru=False,
-    ),
+    type='CRNN',
+    preprocessor=None,
+    backbone=dict(type='MiniVGG', leaky_relu=False, input_channels=1),
+    encoder=None,
     decoder=dict(
-        type='ParallelSARDecoder',
-        enc_bi_rnn=False,
-        dec_bi_rnn=False,
-        dec_do_rnn=0,
-        dec_gru=False,
-        pred_dropout=0.1,
-        d_k=512,
-        pred_concat=True,
-        postprocessor=dict(type='AttentionPostprocessor'),
-        module_loss=dict(
-            type='CEModuleLoss', ignore_first_char=True, reduction='mean'),
-        dictionary=dictionary,
-        max_seq_len=30))
+        type='CRNNDecoder',
+        in_channels=512,
+        rnn_flag=True,
+        module_loss=dict(type='CTCModuleLoss', letter_case='lower'),
+        postprocessor=dict(type='CTCPostProcessor'),
+        dictionary=dictionary),
+    data_preprocessor=dict(
+        type='TextRecogDataPreprocessor', mean=[127], std=[127]))
 
 file_client_args = dict(backend='disk')
 train_pipeline = [
     dict(
         type='LoadImageFromFile',
+        color_type='grayscale',
         file_client_args=file_client_args,
         ignore_empty=True,
         min_size=2),
     dict(type='LoadOCRAnnotations', with_text=True),
-    dict(
-        type='RescaleToHeight',
-        height=48,
-        min_width=48,
-        max_width=160,
-        width_divisor=4),
-    dict(type='PadToWidth', width=160),
+    dict(type='Resize', scale=(100, 32), keep_ratio=False),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
 
 test_pipeline = [
-    dict(type='LoadImageFromFile', file_client_args=file_client_args),
+    dict(
+        type='LoadImageFromFile',
+        color_type='grayscale',
+        file_client_args=file_client_args),
     dict(
         type='RescaleToHeight',
-        height=48,
-        min_width=48,
-        max_width=160,
-        width_divisor=4),
-    dict(type='PadToWidth', width=160),
+        height=32,
+        min_width=32,
+        max_width=None,
+        width_divisor=16),
     # add loading annotation after ``Resize`` because ground truth
     # does not need to do resize data transform
     dict(type='LoadOCRAnnotations', with_text=True),
     dict(
         type='PackTextRecogInputs',
         meta_keys=('img_path', 'ori_shape', 'img_shape', 'valid_ratio'))
 ]
+
+tta_pipeline = [
+    dict(
+        type='LoadImageFromFile',
+        color_type='grayscale',
+        file_client_args=file_client_args),
+    dict(
+        type='TestTimeAug',
+        transforms=[
+            [
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=0, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=1, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+                dict(
+                    type='ConditionApply',
+                    true_transforms=[
+                        dict(
+                            type='ImgAugWrapper',
+                            args=[dict(cls='Rot90', k=3, keep_size=False)])
+                    ],
+                    condition="results['img_shape'][1]<results['img_shape'][0]"
+                ),
+            ],
+            [
+                dict(
+                    type='RescaleToHeight',
+                    height=32,
+                    min_width=32,
+                    max_width=None,
+                    width_divisor=16)
+            ],
+            # add loading annotation after ``Resize`` because ground truth
+            # does not need to do resize data transform
+            [dict(type='LoadOCRAnnotations', with_text=True)],
+            [
+                dict(
+                    type='PackTextRecogInputs',
+                    meta_keys=('img_path', 'ori_shape', 'img_shape',
+                               'valid_ratio'))
+            ]
+        ])
+]
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_st-sub_mj-sub_sa_real.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/sar/sar_resnet31_parallel-decoder_5e_st-sub_mj-sub_sa_real.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/satrn_shallow-small_5e_st_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/satrn_shallow-small_5e_st_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/satrn/satrn_shallow_5e_st_mj.py` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/satrn/satrn_shallow_5e_st_mj.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/configs/textrecog/svtr/metafile.yml` & `mmocr-1.0.0rc6/mmocr/.mim/configs/textrecog/svtr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/model-index.yml` & `mmocr-1.0.0rc6/mmocr/.mim/model-index.yml`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/browse_dataset.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/browse_dataset.py`

 * *Files 6% similar despite different names*

```diff
@@ -5,19 +5,19 @@
 from typing import Optional, Tuple
 
 import cv2
 import mmcv
 import numpy as np
 from mmengine.config import Config, DictAction
 from mmengine.dataset import Compose
+from mmengine.registry import init_default_scope
 from mmengine.utils import ProgressBar
 from mmengine.visualization import Visualizer
 
 from mmocr.registry import DATASETS, VISUALIZERS
-from mmocr.utils import register_all_modules
 
 
 # TODO: Support for printing the change in key of results
 def parse_args():
     parser = argparse.ArgumentParser(description='Browse a dataset')
     parser.add_argument('config', help='Path to model or dataset config.')
     parser.add_argument(
@@ -105,18 +105,21 @@
         int: The adaptive scale.
     """
     short_edge_length = min(img_shape)
     scale = short_edge_length / 224.
     return min(max(scale, min_scale), max_scale)
 
 
-def make_grid(imgs, names):
+def make_grid(imgs, infos):
     """Concat list of pictures into a single big picture, align height here."""
     visualizer = Visualizer.get_current_instance()
-    ori_shapes = [img.shape[:2] for img in imgs]
+    names = [info['name'] for info in infos]
+    ori_shapes = [
+        info['dataset_sample'].metainfo['img_shape'] for info in infos
+    ]
     max_height = int(max(img.shape[0] for img in imgs) * 1.1)
     min_width = min(img.shape[1] for img in imgs)
     horizontal_gap = min_width // 10
     img_scale = _get_adaptive_scale((max_height, min_width))
 
     texts = []
     text_positions = []
@@ -158,25 +161,21 @@
     """
 
     def __init__(self, transforms, intermediate_imgs):
         super().__init__(transforms=transforms)
         self.intermediate_imgs = intermediate_imgs
 
     def __call__(self, data):
-        if 'img' in data:
-            self.intermediate_imgs.append({
-                'name': 'original',
-                'img': data['img'].copy()
-            })
         self.ptransforms = [
             self.transforms[i] for i in range(len(self.transforms) - 1)
         ]
         for t in self.ptransforms:
             data = t(data)
-            # Keep the same meta_keys in the PackDetInputs
+            # Keep the same meta_keys in the PackTextDetInputs
+            # or PackTextRecogInputs
             self.transforms[-1].meta_keys = [key for key in data]
             data_sample = self.transforms[-1](data)
             if data is None:
                 return None
             if 'img' in data:
                 self.intermediate_imgs.append({
                     'name':
@@ -295,15 +294,37 @@
     dataloader_name = f'{phase}_dataloader'
     if dataloader_name in cfg:
         dataset = cfg.get(dataloader_name).dataset
         visualizer = cfg.visualizer
 
         if mode == 'original':
             default_cfg = default_cfgs[infer_dataset_task(task, dataset)]
+            # Image can be stored in other methods, like LMDB,
+            # which LoadImageFromFile can not handle
+            if dataset.pipeline is not None:
+                all_transform_types = [tfm['type'] for tfm in dataset.pipeline]
+                if any([
+                        tfm_type.startswith('LoadImageFrom')
+                        for tfm_type in all_transform_types
+                ]):
+                    for tfm in dataset.pipeline:
+                        if tfm['type'].startswith('LoadImageFrom'):
+                            # update LoadImageFrom** transform
+                            default_cfg['pipeline'][0] = tfm
             dataset.pipeline = default_cfg['pipeline']
+        else:
+            # In test_pipeline LoadOCRAnnotations is placed behind
+            # other transforms. Transform will not be applied on
+            # gt annotation.
+            if phase == 'test':
+                all_transform_types = [tfm['type'] for tfm in dataset.pipeline]
+                load_ocr_ann_tfm_index = all_transform_types.index(
+                    'LoadOCRAnnotations')
+                load_ocr_ann_tfm = dataset.pipeline.pop(load_ocr_ann_tfm_index)
+                dataset.pipeline.insert(1, load_ocr_ann_tfm)
 
         return dataset, visualizer
 
     # Dataset config mode
 
     for key in cfg.keys():
         if key.endswith(phase) and cfg[key]['type'].endswith('Dataset'):
@@ -327,16 +348,15 @@
 
 def main():
     args = parse_args()
     cfg = Config.fromfile(args.config)
     if args.cfg_options is not None:
         cfg.merge_from_dict(args.cfg_options)
 
-    # register all modules in mmyolo into the registries
-    register_all_modules()
+    init_default_scope(cfg.get('default_scope', 'mmocr'))
 
     dataset_cfg, visualizer_cfg = obtain_dataset_cfg(cfg, args.phase,
                                                      args.mode, args.task)
     dataset = DATASETS.build(dataset_cfg)
     visualizer = VISUALIZERS.build(visualizer_cfg)
     visualizer.dataset_meta = dataset.metainfo
 
@@ -357,27 +377,27 @@
     progress_bar = ProgressBar(display_number)
     # fetching items from dataset is a must for visualization
     for i, _ in zip(range(display_number), dataset):
         image_i = []
         result_i = [result['dataset_sample'] for result in intermediate_imgs]
         for k, datasample in enumerate(result_i):
             image = datasample.img
-            image = image[..., [2, 1, 0]]  # bgr to rgb
+            if len(image.shape) == 3:
+                image = image[..., [2, 1, 0]]  # bgr to rgb
             image_show = visualizer.add_datasample(
                 'result',
                 image,
                 datasample,
                 draw_pred=False,
                 draw_gt=True,
                 show=False)
             image_i.append(image_show)
 
         if args.mode == 'pipeline':
-            image = make_grid([result for result in image_i],
-                              [result['name'] for result in intermediate_imgs])
+            image = make_grid(image_i, intermediate_imgs)
         else:
             image = image_i[-1]
 
         if hasattr(datasample, 'img_path'):
             filename = osp.basename(datasample.img_path)
         else:
             # some dataset have not image path
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/get_flops.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/get_flops.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,18 +1,16 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import argparse
 
 import torch
 from fvcore.nn import FlopCountAnalysis, flop_count_table
 from mmengine import Config
+from mmengine.registry import init_default_scope
 
 from mmocr.registry import MODELS
-from mmocr.utils import register_all_modules
-
-register_all_modules()
 
 
 def parse_args():
     parser = argparse.ArgumentParser(description='Train a detector')
     parser.add_argument('config', help='train config file path')
     parser.add_argument(
         '--shape',
@@ -34,14 +32,15 @@
         h, w = args.shape
     else:
         raise ValueError('invalid input shape, please use --shape h w')
 
     input_shape = (1, 3, h, w)
 
     cfg = Config.fromfile(args.config)
+    init_default_scope(cfg.get('default_scope', 'mmocr'))
     model = MODELS.build(cfg.model)
 
     flops = FlopCountAnalysis(model, torch.ones(input_shape))
 
     # params = parameter_count_table(model)
     flops_data = flop_count_table(flops)
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/offline_eval.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/offline_eval.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import argparse
 import json
 
 import mmengine
 from mmengine.config import Config, DictAction
 from mmengine.evaluator import Evaluator
-
-from mmocr.utils import register_all_modules
+from mmengine.registry import init_default_scope
 
 
 def parse_args():
     parser = argparse.ArgumentParser(description='Offline evaluation of the '
                                      'prediction saved in pkl format')
     parser.add_argument('config', help='Config of the model')
     parser.add_argument(
@@ -29,18 +28,17 @@
     args = parser.parse_args()
     return args
 
 
 def main():
     args = parse_args()
 
-    register_all_modules()
-
     # load config
     cfg = Config.fromfile(args.config)
+    init_default_scope(cfg.get('default_scope', 'mmocr'))
     if args.cfg_options is not None:
         cfg.merge_from_dict(args.cfg_options)
 
     predictions = mmengine.load(args.pkl_results)
 
     evaluator = Evaluator(cfg.test_evaluator)
     eval_results = evaluator.offline_evaluate(predictions)
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/analysis_tools/print_config.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/analysis_tools/print_config.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/common/curvedsyntext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/common/curvedsyntext_converter.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import argparse
 import os.path as osp
 from functools import partial
 
 import mmengine
 import numpy as np
 
-from mmocr.utils import bezier_to_polygon, sort_points
+from mmocr.utils import bezier2polygon, sort_points
 
 # The default dictionary used by CurvedSynthText
 dict95 = [
     ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.',
     '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
     '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
@@ -34,15 +34,15 @@
         res.append(dict95[d])
     return ''.join(res)
 
 
 def modify_annotation(ann, num_sample, start_img_id=0, start_ann_id=0):
     ann['text'] = digit2text(ann.pop('rec'))
     # Get hide egmentation points
-    polygon_pts = bezier_to_polygon(ann['bezier_pts'], num_sample=num_sample)
+    polygon_pts = bezier2polygon(ann['bezier_pts'], num_sample=num_sample)
     ann['segmentation'] = np.asarray(sort_points(polygon_pts)).reshape(
         1, -1).tolist()
     ann['image_id'] += start_img_id
     ann['id'] += start_ann_id
     return ann
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/common/extract_kaist.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/common/extract_kaist.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/kie/closeset_to_openset.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/kie/closeset_to_openset.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/art_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/art_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/bid_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/bid_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/coco_to_line_dict.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/coco_to_line_dict.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/cocotext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/cocotext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ctw1500_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ctw1500_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/data_migrator.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/data_migrator.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/detext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/detext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/funsd_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/funsd_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/hiertext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/hiertext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ic11_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ic11_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ic13_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ic13_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/icdar_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/icdar_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/ilst_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/ilst_converter.py`

 * *Files 0% similar despite different names*

```diff
@@ -151,15 +151,15 @@
     return img_info
 
 
 def split_train_val_list(full_list, val_ratio):
     """Split list by val_ratio.
 
     Args:
-        full_list (list): List to be splited
+        full_list (list): List to be split
         val_ratio (float): Split ratio for val set
 
     return:
         list(list, list): Train_list and val_list
     """
 
     n_total = len(full_list)
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/imgur_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/imgur_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/kaist_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/kaist_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/lsvt_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/lsvt_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/lv_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/lv_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/mtwi_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/mtwi_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/naf_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/naf_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/rctw_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/rctw_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/rects_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/rects_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/sroie_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/sroie_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/synthtext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/synthtext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/textocr_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/textocr_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/totaltext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/totaltext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textdet/vintext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textdet/vintext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/art_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/art_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/bid_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/bid_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/cocotext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/cocotext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/data_migrator.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/data_migrator.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/detext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/detext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/funsd_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/funsd_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/hiertext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/hiertext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/ic11_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/ic11_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/ic13_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/ic13_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/ilst_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/ilst_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/imgur_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/imgur_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/kaist_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/kaist_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/lmdb_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/lmdb_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/lsvt_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/lsvt_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/lv_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/lv_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/mtwi_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/mtwi_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/naf_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/naf_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/openvino_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/openvino_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/rctw_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/rctw_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/rects_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/rects_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/sroie_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/sroie_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/svt_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/svt_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/synthtext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/synthtext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/textocr_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/textocr_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/totaltext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/totaltext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/dataset_converters/textrecog/vintext_converter.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/textrecog/vintext_converter.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/slurm_train.sh` & `mmocr-1.0.0rc6/mmocr/.mim/tools/slurm_train.sh`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/test.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/test.py`

 * *Files 9% similar despite different names*

```diff
@@ -3,16 +3,14 @@
 import os
 import os.path as osp
 
 from mmengine.config import Config, DictAction
 from mmengine.registry import RUNNERS
 from mmengine.runner import Runner
 
-from mmocr.utils import register_all_modules
-
 
 def parse_args():
     parser = argparse.ArgumentParser(description='Test (and eval) a model')
     parser.add_argument('config', help='Test config file path')
     parser.add_argument('checkpoint', help='Checkpoint file')
     parser.add_argument(
         '--work-dir',
@@ -41,14 +39,16 @@
         'Note that the quotation marks are necessary and that no white space '
         'is allowed.')
     parser.add_argument(
         '--launcher',
         choices=['none', 'pytorch', 'slurm', 'mpi'],
         default='none',
         help='Job launcher')
+    parser.add_argument(
+        '--tta', action='store_true', help='Test time augmentation')
     parser.add_argument('--local_rank', type=int, default=0)
     args = parser.parse_args()
     if 'LOCAL_RANK' not in os.environ:
         os.environ['LOCAL_RANK'] = str(args.local_rank)
     return args
 
 
@@ -74,18 +74,14 @@
 
     return cfg
 
 
 def main():
     args = parse_args()
 
-    # register all modules in mmocr into the registries
-    # do not init the default scope here because it will be init in the runner
-    register_all_modules(init_default_scope=False)
-
     # load config
     cfg = Config.fromfile(args.config)
     cfg.launcher = args.launcher
     if args.cfg_options is not None:
         cfg.merge_from_dict(args.cfg_options)
 
     # work_dir is determined in this priority: CLI > segment in file > filename
@@ -103,14 +99,19 @@
     if args.show and args.show_dir:
         raise NotImplementedError('--show and --show-dir cannot be set '
                                   'at the same time')
 
     if args.show or args.show_dir:
         cfg = trigger_visualization_hook(cfg, args)
 
+    if args.tta:
+        cfg.test_dataloader.dataset.pipeline = cfg.tta_pipeline
+        cfg.tta_model.module = cfg.model
+        cfg.model = cfg.tta_model
+
     # save predictions
     if args.save_preds:
         dump_metric = dict(
             type='DumpResults',
             out_file_path=osp.join(
                 cfg.work_dir,
                 f'{osp.basename(args.checkpoint)}_predictions.pkl'))
```

### Comparing `mmocr-1.0.0rc5/mmocr/.mim/tools/train.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/train.py`

 * *Files 8% similar despite different names*

```diff
@@ -5,16 +5,14 @@
 import os.path as osp
 
 from mmengine.config import Config, DictAction
 from mmengine.logging import print_log
 from mmengine.registry import RUNNERS
 from mmengine.runner import Runner
 
-from mmocr.utils import register_all_modules
-
 
 def parse_args():
     parser = argparse.ArgumentParser(description='Train a model')
     parser.add_argument('config', help='Train config file path')
     parser.add_argument('--work-dir', help='The dir to save logs and models')
     parser.add_argument(
         '--resume', action='store_true', help='Whether to resume checkpoint.')
@@ -50,18 +48,14 @@
 
     return args
 
 
 def main():
     args = parse_args()
 
-    # register all modules in mmdet into the registries
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

### Comparing `mmocr-1.0.0rc5/mmocr/__init__.py` & `mmocr-1.0.0rc6/mmocr/__init__.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,36 +1,51 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 
 import mmcv
 import mmdet
-import mmengine
-from mmengine.utils import digit_version
+
+try:
+    import mmengine
+    from mmengine.utils import digit_version
+except ImportError:
+    mmengine = None
+    from mmcv import digit_version
 
 from .version import __version__, short_version
 
-mmcv_minimum_version = '2.0.0rc1'
+mmcv_minimum_version = '2.0.0rc4'
 mmcv_maximum_version = '2.1.0'
 mmcv_version = digit_version(mmcv.__version__)
-mmengine_minimum_version = '0.1.0'
-mmengine_maximum_version = '1.0.0'
-mmengine_version = digit_version(mmengine.__version__)
+if mmengine is not None:
+    mmengine_minimum_version = '0.6.0'
+    mmengine_maximum_version = '1.0.0'
+    mmengine_version = digit_version(mmengine.__version__)
+
+if mmcv_version < digit_version('2.0.0rc0') or mmdet.__version__ < '3.0.0rc0':
+    raise RuntimeError(
+        'MMOCR 1.0 only runs with MMEngine, MMCV 2.0.0rc0+ and '
+        'MMDetection 3.0.0rc0+, but got MMCV '
+        f'{mmcv.__version__} and MMDetection '
+        f'{mmdet.__version__}. For more information, please refer to '
+        'https://mmocr.readthedocs.io/en/dev-1.x/migration/overview.html'
+    )  # noqa
 
 assert (mmcv_version >= digit_version(mmcv_minimum_version)
         and mmcv_version < digit_version(mmcv_maximum_version)), \
     f'MMCV {mmcv.__version__} is incompatible with MMOCR {__version__}. ' \
     f'Please use MMCV >= {mmcv_minimum_version}, ' \
     f'< {mmcv_maximum_version} instead.'
 
 assert (mmengine_version >= digit_version(mmengine_minimum_version)
         and mmengine_version < digit_version(mmengine_maximum_version)), \
     f'MMEngine=={mmengine.__version__} is used but incompatible. ' \
     f'Please install mmengine>={mmengine_minimum_version}, ' \
     f'<{mmengine_maximum_version}.'
 
-mmdet_minimum_version = '3.0.0rc0'
+mmdet_minimum_version = '3.0.0rc5'
 mmdet_maximum_version = '3.1.0'
 mmdet_version = digit_version(mmdet.__version__)
 
 assert (mmdet_version >= digit_version(mmdet_minimum_version)
         and mmdet_version < digit_version(mmdet_maximum_version)), \
     f'MMDetection {mmdet.__version__} is incompatible ' \
     f'with MMOCR {__version__}. ' \
```

### Comparing `mmocr-1.0.0rc5/mmocr/apis/inferencers/base_mmocr_inferencer.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/fce_postprocessor.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,267 +1,239 @@
 # Copyright (c) OpenMMLab. All rights reserved.
-import os.path as osp
-from typing import Dict, List, Optional, Sequence, Tuple, Union
+from typing import Dict, List, Sequence
 
-import mmcv
+import cv2
 import numpy as np
-from mmengine.dataset import Compose
+import torch
 from mmengine.structures import InstanceData
+from numpy.fft import ifft
 
-from mmocr.utils import ConfigType
-from .base_inferencer import BaseInferencer
+from mmocr.registry import MODELS
+from mmocr.structures import TextDetDataSample
+from mmocr.utils import fill_hole
+from .base import BaseTextDetPostProcessor
 
-InstanceList = List[InstanceData]
-InputType = Union[str, np.ndarray]
-InputsType = Union[InputType, Sequence[InputType]]
-PredType = Union[InstanceData, InstanceList]
-ImgType = Union[np.ndarray, Sequence[np.ndarray]]
-ResType = Union[Dict, List[Dict], InstanceData, List[InstanceData]]
 
-
-class BaseMMOCRInferencer(BaseInferencer):
-    """Base inferencer.
+@MODELS.register_module()
+class FCEPostprocessor(BaseTextDetPostProcessor):
+    """Decoding predictions of FCENet to instances.
 
     Args:
-        model (str or ConfigType): Model config or the path to it.
-        ckpt (str, optional): Path to the checkpoint.
-        device (str, optional): Device to run inference. If None, the best
-            device will be automatically used.
-        show (bool): Whether to display the image in a popup window.
-            Defaults to False.
-        wait_time (float): The interval of show (s). Defaults to 0.
-        draw_pred (bool): Whether to draw predicted bounding boxes.
-            Defaults to True.
-        pred_score_thr (float): Minimum score of bboxes to draw.
-            Defaults to 0.3.
-        img_out_dir (str): Output directory of images. Defaults to ''.
-        pred_out_file: File to save the inference results. If left as empty, no
-            file will be saved.
-        print_result (bool): Whether to print the result.
-            Defaults to False.
+        fourier_degree (int): The maximum Fourier transform degree k.
+        num_reconstr_points (int): The points number of the polygon
+            reconstructed from predicted Fourier coefficients.
+        rescale_fields (list[str]): The bbox/polygon field names to
+            be rescaled. If None, no rescaling will be performed. Defaults to
+            ['polygons'].
+        scales (list[int]) : The down-sample scale of each layer. Defaults
+            to [8, 16, 32].
+        text_repr_type (str): Boundary encoding type 'poly' or 'quad'. Defaults
+            to 'poly'.
+         alpha (float): The parameter to calculate final scores
+            :math:`Score_{final} = (Score_{text region} ^ alpha)
+            * (Score_{text center_region}^ beta)`. Defaults to 1.0.
+        beta (float): The parameter to calculate final score. Defaults to 2.0.
+        score_thr (float): The threshold used to filter out the final
+            candidates.Defaults to 0.3.
+        nms_thr (float): The threshold of nms. Defaults to 0.1.
     """
 
-    func_kwargs = dict(
-        preprocess=[],
-        forward=[],
-        visualize=[
-            'show', 'wait_time', 'draw_pred', 'pred_score_thr', 'img_out_dir'
-        ],
-        postprocess=['print_result', 'pred_out_file', 'get_datasample'])
-
     def __init__(self,
-                 config: Union[ConfigType, str],
-                 ckpt: Optional[str],
-                 device: Optional[str] = None,
+                 fourier_degree: int,
+                 num_reconstr_points: int,
+                 rescale_fields: Sequence[str] = ['polygons'],
+                 scales: Sequence[int] = [8, 16, 32],
+                 text_repr_type: str = 'poly',
+                 alpha: float = 1.0,
+                 beta: float = 2.0,
+                 score_thr: float = 0.3,
+                 nms_thr: float = 0.1,
                  **kwargs) -> None:
-        # A global counter tracking the number of images processed, for
-        # naming of the output images
-        self.num_visualized_imgs = 0
-        super().__init__(config=config, ckpt=ckpt, device=device, **kwargs)
-
-    def _init_pipeline(self, cfg: ConfigType) -> None:
-        """Initialize the test pipeline."""
-        pipeline_cfg = cfg.test_dataloader.dataset.pipeline
-
-        # For inference, the key of ``instances`` is not used.
-        if 'meta_keys' in pipeline_cfg[-1]:
-            pipeline_cfg[-1]['meta_keys'] = tuple(
-                meta_key for meta_key in pipeline_cfg[-1]['meta_keys']
-                if meta_key != 'instances')
-
-        # Loading annotations is also not applicable
-        idx = self._get_transform_idx(pipeline_cfg, 'LoadOCRAnnotations')
-        if idx != -1:
-            del pipeline_cfg[idx]
-
-        self.file_pipeline = Compose(pipeline_cfg)
-
-        load_img_idx = self._get_transform_idx(pipeline_cfg,
-                                               'LoadImageFromFile')
-        if load_img_idx == -1:
-            raise ValueError(
-                'LoadImageFromFile is not found in the test pipeline')
-        pipeline_cfg[load_img_idx]['type'] = 'LoadImageFromNDArray'
-        self.ndarray_pipeline = Compose(pipeline_cfg)
+        super().__init__(
+            text_repr_type=text_repr_type,
+            rescale_fields=rescale_fields,
+            **kwargs)
+        self.fourier_degree = fourier_degree
+        self.num_reconstr_points = num_reconstr_points
+        self.scales = scales
+        self.alpha = alpha
+        self.beta = beta
+        self.score_thr = score_thr
+        self.nms_thr = nms_thr
+
+    def split_results(self, pred_results: List[Dict]) -> List[List[Dict]]:
+        """Split batched elements in pred_results along the first dimension
+        into ``batch_num`` sub-elements and regather them into a list of dicts.
 
-    def _get_transform_idx(self, pipeline_cfg: ConfigType, name: str) -> int:
-        """Returns the index of the transform in a pipeline.
+        Args:
+            pred_results (list[dict]): A list of dict with keys of ``cls_res``,
+                ``reg_res`` corresponding to the classification result and
+                regression result computed from the input tensor with the
+                same index. They have the shapes of :math:`(N, C_{cls,i},
+                H_i, W_i)` and :math:`(N, C_{out,i}, H_i, W_i)`.
 
-        If the transform is not found, returns -1.
+        Returns:
+            list[list[dict]]: N lists. Each list contains three dicts from
+            different feature level.
         """
-        for i, transform in enumerate(pipeline_cfg):
-            if transform['type'] == name:
-                return i
-        return -1
+        assert isinstance(pred_results, list) and len(pred_results) == len(
+            self.scales)
 
-    def preprocess(self, inputs: InputsType) -> Dict:
-        """Process the inputs into a model-feedable format."""
+        fields = list(pred_results[0].keys())
+        batch_num = len(pred_results[0][fields[0]])
+        level_num = len(pred_results)
         results = []
-        for single_input in inputs:
-            if isinstance(single_input, str):
-                if osp.isdir(single_input):
-                    raise ValueError('Feeding a directory is not supported')
-                    # for img_path in os.listdir(single_input):
-                    #     data_ =dict(img_path=osp.join(single_input,img_path))
-                    #     results.append(self.file_pipeline(data_))
-                else:
-                    data_ = dict(img_path=single_input)
-                    results.append(self.file_pipeline(data_))
-            elif isinstance(single_input, np.ndarray):
-                data_ = dict(img=single_input)
-                results.append(self.ndarray_pipeline(data_))
-            else:
-                raise ValueError(
-                    f'Unsupported input type: {type(single_input)}')
-
-        return self._collate(results)
-
-    def _collate(self, results: List[Dict]) -> Dict:
-        """Collate the results from different images."""
-        results = {key: [d[key] for d in results] for key in results[0]}
+        for i in range(batch_num):
+            batch_list = []
+            for level in range(level_num):
+                feat_dict = {}
+                for field in fields:
+                    feat_dict[field] = pred_results[level][field][i]
+                batch_list.append(feat_dict)
+            results.append(batch_list)
         return results
 
-    def __call__(self, user_inputs: InputsType,
-                 **kwargs) -> Union[Dict, List[Dict]]:
-        """Call the inferencer.
+    def get_text_instances(self, pred_results: Sequence[Dict],
+                           data_sample: TextDetDataSample
+                           ) -> TextDetDataSample:
+        """Get text instance predictions of one image.
 
         Args:
-            user_inputs: Inputs for the inferencer.
-            kwargs: Keyword arguments for the inferencer.
-        """
-
-        # Detect if user_inputs are in a batch
-        is_batch = isinstance(user_inputs, (list, tuple))
-        inputs = user_inputs if is_batch else [user_inputs]
-
-        params = self._dispatch_kwargs(**kwargs)
-        preprocess_kwargs = self.base_params[0].copy()
-        preprocess_kwargs.update(params[0])
-        forward_kwargs = self.base_params[1].copy()
-        forward_kwargs.update(params[1])
-        visualize_kwargs = self.base_params[2].copy()
-        visualize_kwargs.update(params[2])
-        postprocess_kwargs = self.base_params[3].copy()
-        postprocess_kwargs.update(params[3])
-
-        data = self.preprocess(inputs, **preprocess_kwargs)
-        preds = self.forward(data, **forward_kwargs)
-        imgs = self.visualize(inputs, preds, **visualize_kwargs)
-        results = self.postprocess(
-            preds, imgs, is_batch=is_batch, **postprocess_kwargs)
-        return results
-
-    def visualize(self,
-                  inputs: InputsType,
-                  preds: PredType,
-                  show: bool = False,
-                  wait_time: int = 0,
-                  draw_pred: bool = True,
-                  pred_score_thr: float = 0.3,
-                  img_out_dir: str = '') -> List[np.ndarray]:
-        """Visualize predictions.
+            pred_results (List[dict]): A list of dict with keys of ``cls_res``,
+                ``reg_res`` corresponding to the classification result and
+                regression result computed from the input tensor with the
+                same index. They have the shapes of :math:`(N, C_{cls,i}, H_i,
+                W_i)` and :math:`(N, C_{out,i}, H_i, W_i)`.
+            data_sample (TextDetDataSample): Datasample of an image.
 
-        Args:
-            inputs (List[Union[str, np.ndarray]]): Inputs for the inferencer.
-            preds (List[Dict]): Predictions of the model.
-            show (bool): Whether to display the image in a popup window.
-                Defaults to False.
-            wait_time (float): The interval of show (s). Defaults to 0.
-            draw_pred (bool): Whether to draw predicted bounding boxes.
-                Defaults to True.
-            pred_score_thr (float): Minimum score of bboxes to draw.
-                Defaults to 0.3.
-            img_out_dir (str): Output directory of images. Defaults to ''.
+        Returns:
+            TextDetDataSample: A new DataSample with predictions filled in.
+            Polygons and results are saved in
+            ``TextDetDataSample.pred_instances.polygons``. The confidence
+            scores are saved in ``TextDetDataSample.pred_instances.scores``.
         """
-        if self.visualizer is None or not show and img_out_dir == '':
-            return None
-
-        if getattr(self, 'visualizer') is None:
-            raise ValueError('Visualization needs the "visualizer" term'
-                             'defined in the config, but got None.')
-
-        results = []
-
-        for single_input, pred in zip(inputs, preds):
-            if isinstance(single_input, str):
-                img = mmcv.imread(single_input)
-                img = img[:, :, ::-1]
-                img_name = osp.basename(single_input)
-            elif isinstance(single_input, np.ndarray):
-                img = single_input.copy()
-                img_num = str(self.num_visualized_imgs).zfill(8)
-                img_name = f'{img_num}.jpg'
-            else:
-                raise ValueError('Unsupported input type: '
-                                 f'{type(single_input)}')
-
-            out_file = osp.join(img_out_dir, img_name) if img_out_dir != '' \
-                else None
-
-            self.visualizer.add_datasample(
-                img_name,
-                img,
-                pred,
-                show=show,
-                wait_time=wait_time,
-                draw_gt=False,
-                draw_pred=draw_pred,
-                pred_score_thr=pred_score_thr,
-                out_file=out_file,
-            )
-            results.append(img)
-            self.num_visualized_imgs += 1
+        assert len(pred_results) == len(self.scales)
+        data_sample.pred_instances = InstanceData()
+        data_sample.pred_instances.polygons = []
+        data_sample.pred_instances.scores = []
+
+        result_polys = []
+        result_scores = []
+        for idx, pred_result in enumerate(pred_results):
+            # TODO: Scale can be calculated given image shape and feature
+            # shape. This param can be removed in the future.
+            polygons, scores = self._get_text_instances_single(
+                pred_result, self.scales[idx])
+            result_polys += polygons
+            result_scores += scores
+        result_polys, result_scores = self.poly_nms(result_polys,
+                                                    result_scores,
+                                                    self.nms_thr)
+        for result_poly, result_score in zip(result_polys, result_scores):
+            result_poly = np.array(result_poly, dtype=np.float32)
+            data_sample.pred_instances.polygons.append(result_poly)
+            data_sample.pred_instances.scores.append(result_score)
+        data_sample.pred_instances.scores = torch.FloatTensor(
+            data_sample.pred_instances.scores)
 
-        return results
+        return data_sample
 
-    def postprocess(
-        self,
-        preds: PredType,
-        imgs: Optional[List[np.ndarray]] = None,
-        is_batch: bool = False,
-        print_result: bool = False,
-        pred_out_file: str = '',
-        get_datasample: bool = False,
-    ) -> Union[ResType, Tuple[ResType, np.ndarray]]:
-        """Postprocess predictions.
+    def _get_text_instances_single(self, pred_result: Dict, scale: int):
+        """Get text instance predictions from one feature level.
 
         Args:
-            preds (List[Dict]): Predictions of the model.
-            imgs (Optional[np.ndarray]): Visualized predictions.
-            is_batch (bool): Whether the inputs are in a batch.
-                Defaults to False.
-            print_result (bool): Whether to print the result.
-                Defaults to False.
-            pred_out_file (str): Output file name to store predictions
-                without images. Supported file formats are “json”, “yaml/yml”
-                and “pickle/pkl”. Defaults to ''.
-            get_datasample (bool): Whether to use Datasample to store
-                inference results. If False, dict will be used.
+            pred_result (dict): A dict with keys of ``cls_res``, ``reg_res``
+                corresponding to the classification result and regression
+                result computed from the input tensor with the same index.
+                They have the shapes of :math:`(1, C_{cls,i}, H_i, W_i)` and
+                :math:`(1, C_{out,i}, H_i, W_i)`.
+            scale (int): Scale of current feature map which equals to
+                img_size / feat_size.
 
         Returns:
-            TODO
+            result_polys (list[ndarray]): A list of polygons after postprocess.
+            result_scores (list[ndarray]): A list of scores after postprocess.
         """
-        results = preds
-        if not get_datasample:
-            results = []
-            for pred in preds:
-                result = self.pred2dict(pred)
-                results.append(result)
-        if not is_batch:
-            results = results[0]
-        if print_result:
-            print(results)
-        # Add img to the results after printing
-        if pred_out_file != '':
-            mmcv.dump(results, pred_out_file)
-        if imgs is None:
-            return results
-        return results, imgs
-
-    def pred2dict(self, data_sample: InstanceData) -> Dict:
-        """Extract elements necessary to represent a prediction into a
-        dictionary.
 
-        It's better to contain only basic data elements such as strings and
-        numbers in order to guarantee it's json-serializable.
-        """
-        raise NotImplementedError
+        cls_pred = pred_result['cls_res']
+        tr_pred = cls_pred[0:2].softmax(dim=0).data.cpu().numpy()
+        tcl_pred = cls_pred[2:].softmax(dim=0).data.cpu().numpy()
+
+        reg_pred = pred_result['reg_res'].permute(1, 2, 0).data.cpu().numpy()
+        x_pred = reg_pred[:, :, :2 * self.fourier_degree + 1]
+        y_pred = reg_pred[:, :, 2 * self.fourier_degree + 1:]
+
+        score_pred = (tr_pred[1]**self.alpha) * (tcl_pred[1]**self.beta)
+        tr_pred_mask = (score_pred) > self.score_thr
+        tr_mask = fill_hole(tr_pred_mask)
+
+        tr_contours, _ = cv2.findContours(
+            tr_mask.astype(np.uint8), cv2.RETR_TREE,
+            cv2.CHAIN_APPROX_SIMPLE)  # opencv4
+
+        mask = np.zeros_like(tr_mask)
+
+        result_polys = []
+        result_scores = []
+        for cont in tr_contours:
+            deal_map = mask.copy().astype(np.int8)
+            cv2.drawContours(deal_map, [cont], -1, 1, -1)
+
+            score_map = score_pred * deal_map
+            score_mask = score_map > 0
+            xy_text = np.argwhere(score_mask)
+            dxy = xy_text[:, 1] + xy_text[:, 0] * 1j
+
+            x, y = x_pred[score_mask], y_pred[score_mask]
+            c = x + y * 1j
+            c[:, self.fourier_degree] = c[:, self.fourier_degree] + dxy
+            c *= scale
+
+            polygons = self._fourier2poly(c, self.num_reconstr_points)
+            scores = score_map[score_mask].reshape(-1, 1).tolist()
+            polygons, scores = self.poly_nms(polygons, scores, self.nms_thr)
+            result_polys += polygons
+            result_scores += scores
+
+        result_polys, result_scores = self.poly_nms(result_polys,
+                                                    result_scores,
+                                                    self.nms_thr)
+
+        if self.text_repr_type == 'quad':
+            new_polys = []
+            for poly in result_polys:
+                poly = np.array(poly).reshape(-1, 2).astype(np.float32)
+                points = cv2.boxPoints(cv2.minAreaRect(poly))
+                points = np.int0(points)
+                new_polys.append(points.reshape(-1))
+
+            return new_polys, result_scores
+        return result_polys, result_scores
+
+    def _fourier2poly(self,
+                      fourier_coeff: np.ndarray,
+                      num_reconstr_points: int = 50):
+        """ Inverse Fourier transform
+            Args:
+                fourier_coeff (ndarray): Fourier coefficients shaped (n, 2k+1),
+                    with n and k being candidates number and Fourier degree
+                    respectively.
+                num_reconstr_points (int): Number of reconstructed polygon
+                    points. Defaults to 50.
+
+            Returns:
+                List[ndarray]: The reconstructed polygons.
+            """
+
+        a = np.zeros((len(fourier_coeff), num_reconstr_points),
+                     dtype='complex')
+        k = (len(fourier_coeff[0]) - 1) // 2
+
+        a[:, 0:k + 1] = fourier_coeff[:, k:]
+        a[:, -k:] = fourier_coeff[:, :k]
+
+        poly_complex = ifft(a) * num_reconstr_points
+        polygon = np.zeros((len(fourier_coeff), num_reconstr_points, 2))
+        polygon[:, :, 0] = poly_complex.real
+        polygon[:, :, 1] = poly_complex.imag
+        return polygon.astype('int32').reshape(
+            (len(fourier_coeff), -1)).tolist()
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/dataset_wrapper.py` & `mmocr-1.0.0rc6/mmocr/datasets/dataset_wrapper.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/icdar_dataset.py` & `mmocr-1.0.0rc6/mmocr/datasets/icdar_dataset.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/ocr_dataset.py` & `mmocr-1.0.0rc6/mmocr/datasets/ocr_dataset.py`

 * *Files 5% similar despite different names*

```diff
@@ -45,16 +45,16 @@
 
     Args:
         ann_file (str): Annotation file path. Defaults to ''.
         metainfo (dict, optional): Meta information for dataset, such as class
             information. Defaults to None.
         data_root (str, optional): The root directory for ``data_prefix`` and
             ``ann_file``. Defaults to None.
-        data_prefix (dict, optional): Prefix for training data. Defaults to
-            dict(img=None, ann=None).
+        data_prefix (dict): Prefix for training data. Defaults to
+            dict(img_path='').
         filter_cfg (dict, optional): Config for filter data. Defaults to None.
         indices (int or Sequence[int], optional): Support using first few
             data in annotation file to facilitate training/testing on a smaller
             dataset. Defaults to None which means using all ``data_infos``.
         serialize_data (bool, optional): Whether to hold memory using
             serialized objects, when enabled, data loader workers can use
             shared RAM from master process instead of making a copy. Defaults
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/data_obtainer.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/obtainers/naive_data_obtainer.py`

 * *Files 12% similar despite different names*

```diff
@@ -5,31 +5,35 @@
 import shutil
 import ssl
 import urllib.request as request
 from typing import Dict, List, Optional, Tuple
 
 from mmengine import mkdir_or_exist
 
+from mmocr.registry import DATA_OBTAINERS
 from mmocr.utils import check_integrity, is_archive
-from .data_preparer import DATA_OBTAINERS
 
 ssl._create_default_https_context = ssl._create_unverified_context
 
 
 @DATA_OBTAINERS.register_module()
 class NaiveDataObtainer:
     """A naive pipeline for obtaining dataset.
 
     download -> extract -> move
 
     Args:
         files (list[dict]): A list of file information.
         cache_path (str): The path to cache the downloaded files.
-        data_root (str): The root path of the dataset.
-        task (str): The task of the dataset.
+        data_root (str): The root path of the dataset. It is usually set auto-
+            matically and users do not need to set it manually in config file
+            in most cases.
+        task (str): The task of the dataset. It is usually set automatically
+            and users do not need to set it manually in config file
+            in most cases.
     """
 
     def __init__(self, files: List[Dict], cache_path: str, data_root: str,
                  task: str) -> None:
         self.files = files
         self.cache_path = cache_path
         self.data_root = data_root
@@ -110,14 +114,31 @@
             return
 
         zip_name = osp.basename(src_path).split('.')[0]
         if dst_path is None:
             dst_path = osp.join(osp.dirname(src_path), zip_name)
         else:
             dst_path = osp.join(dst_path, zip_name)
+
+        extracted = False
+        if osp.exists(dst_path):
+            name = set(os.listdir(dst_path))
+            if '.finish' in name:
+                extracted = True
+            elif '.finish' not in name and len(name) > 0:
+                while True:
+                    c = input(f'{dst_path} already exists when extracting '
+                              '{zip_name}, unzip again? (y/N) ') or 'N'
+                    if c.lower() in ['y', 'n']:
+                        extracted = c == 'n'
+                        break
+        if extracted:
+            open(osp.join(dst_path, '.finish'), 'w').close()
+            print(f'{zip_name} has been extracted. Skip')
+            return
         mkdir_or_exist(dst_path)
         print(f'Extracting: {osp.basename(src_path)}')
         if src_path.endswith('.zip'):
             try:
                 import zipfile
             except ImportError:
                 raise ImportError(
@@ -132,14 +153,16 @@
             try:
                 import tarfile
             except ImportError:
                 raise ImportError(
                     'Please install tarfile by running "pip install tarfile".')
             with tarfile.open(src_path, mode) as tar_ref:
                 tar_ref.extractall(dst_path)
+
+        open(osp.join(dst_path, '.finish'), 'w').close()
         if delete:
             os.remove(src_path)
 
     def move(self, mapping: List[Tuple[str, str]]) -> None:
         """Rename and move dataset files one by one.
 
         Args:
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/data_preparer.py` & `mmocr-1.0.0rc6/mmocr/.mim/tools/dataset_converters/prepare_dataset.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,139 +1,153 @@
 # Copyright (c) OpenMMLab. All rights reserved.
+import argparse
 import os.path as osp
 import time
+import warnings
 
-from mmengine import Registry
-from mmengine.config import Config
+from mmengine import Config
 
-DATA_OBTAINERS = Registry('data_obtainer')
-DATA_CONVERTERS = Registry('data_converter')
-DATA_PARSERS = Registry('data_parser')
-DATA_DUMPERS = Registry('data_dumper')
-CFG_GENERATORS = Registry('cfg_generator')
-
-
-class DatasetPreparer:
-    """Base class of dataset preparer.
-
-    Dataset preparer is used to prepare dataset for MMOCR. It mainly consists
-    of three steps:
-
-      1. Obtain the dataset
-            - Download
-            - Extract
-            - Move/Rename
-      2. Process the dataset
-            - Parse original annotations
-            - Convert to mmocr format
-            - Dump the annotation file
-            - Clean useless files
-      3. Generate the base config for this dataset
-
-    After all these steps, the original datasets have been prepared for
-    usage in MMOCR. Check out the dataset format used in MMOCR here:
-    https://mmocr.readthedocs.io/en/dev-1.x/user_guides/dataset_prepare.html
+from mmocr.datasets.preparers import DatasetPreparer
+
+
+def parse_args():
+    parser = argparse.ArgumentParser(
+        description='Preparing datasets used in MMOCR.')
+    parser.add_argument(
+        'datasets',
+        help='A list of the dataset names that would like to prepare.',
+        nargs='+')
+    parser.add_argument(
+        '--nproc', help='Number of processes to run', default=4, type=int)
+    parser.add_argument(
+        '--task',
+        default='textdet',
+        choices=['textdet', 'textrecog', 'textspotting', 'kie'],
+        help='Task type. Options are "textdet", "textrecog", "textspotting"'
+        ' and "kie".')
+    parser.add_argument(
+        '--splits',
+        default=['train', 'test', 'val'],
+        help='A list of the split that would like to prepare.',
+        nargs='+')
+    parser.add_argument(
+        '--lmdb',
+        action='store_true',
+        default=False,
+        help='Whether to dump the textrecog dataset to LMDB format, It\'s a '
+        'shortcut to force the dataset to be dumped in lmdb format. '
+        'Applicable when --task=textrecog')
+    parser.add_argument(
+        '--overwrite-cfg',
+        action='store_true',
+        default=False,
+        help='Whether to overwrite the dataset config file if it already'
+        ' exists. If not specified, Dataset Preparer will not generate'
+        ' new config for datasets whose configs are already in base.')
+    parser.add_argument(
+        '--dataset-zoo-path',
+        default='./dataset_zoo',
+        help='Path to dataset zoo config files.')
+    args = parser.parse_args()
+    return args
+
+
+def parse_meta(task: str, meta_path: str) -> None:
+    """Parse meta file.
 
     Args:
-        cfg_path (str): Path to dataset config file.
-        dataset_name (str): Dataset name.
-        task (str): Task type. Options are 'textdet', 'textrecog',
-            'textspotter', and 'kie'. Defaults to 'textdet'.
-        nproc (int): Number of parallel processes. Defaults to 4.
-        overwrite_cfg (bool): Whether to overwrite the dataset config file if
-            it already exists. If False, Dataset Preparer will not generate new
-            config for datasets whose configs are already in base.
+        cfg_path (str): Path to meta file.
     """
+    try:
+        meta = Config.fromfile(meta_path)
+    except FileNotFoundError:
+        return
+    assert task in meta['Data']['Tasks'], \
+        f'Task {task} not supported!'
+    # License related
+    if meta['Data']['License']['Type']:
+        print(f"\033[1;33;40mDataset Name: {meta['Name']}")
+        print(f"License Type: {meta['Data']['License']['Type']}")
+        print(f"License Link: {meta['Data']['License']['Link']}")
+        print(f"BibTeX: {meta['Paper']['BibTeX']}\033[0m")
+        print('\033[1;31;43mMMOCR does not own the dataset. Using this '
+              'dataset you must accept the license provided by the owners, '
+              'and cite the corresponding papers appropriately.')
+        print('If you do not agree with the above license, please cancel '
+              'the progress immediately by pressing ctrl+c. Otherwise, '
+              'you are deemed to accept the terms and conditions.\033[0m')
+        for i in range(5):
+            print(f'{5-i}...')
+            time.sleep(1)
+
 
-    def __init__(self,
-                 cfg_path: str,
-                 dataset_name: str,
-                 task: str = 'textdet',
-                 nproc: int = 4,
-                 overwrite_cfg: bool = False) -> None:
-        cfg_path = osp.join(cfg_path, dataset_name)
-        self.nproc = nproc
-        self.task = task
-        self.dataset_name = dataset_name
-        self.overwrite_cfg = overwrite_cfg
-        self.parse_meta(cfg_path)
-        self.parse_cfg(cfg_path)
-
-    def __call__(self):
-        """Prepare the dataset."""
-        if self.with_obtainer:
-            print('Obtaining Dataset...')
-            self.data_obtainer()
-        if self.with_converter:
-            print('Converting Dataset...')
-            self.data_converter()
-        if self.with_config_generator:
-            print('Generating base configs...')
-            self.config_generator()
-
-    def parse_meta(self, cfg_path: str) -> None:
-        """Parse meta file.
-
-        Args:
-            cfg_path (str): Path to meta file.
-        """
-        try:
-            meta = Config.fromfile(osp.join(cfg_path, 'metafile.yml'))
-        except FileNotFoundError:
-            return
-        assert self.task in meta['Data']['Tasks'], \
-            f'Task {self.task} not supported!'
-        # License related
-        if meta['Data']['License']['Type']:
-            print(f"\033[1;33;40mDataset Name: {meta['Name']}")
-            print(f"License Type: {meta['Data']['License']['Type']}")
-            print(f"License Link: {meta['Data']['License']['Link']}")
-            print(f"BibTeX: {meta['Paper']['BibTeX']}\033[0m")
-            print(
-                '\033[1;31;43mMMOCR does not own the dataset. Using this '
-                'dataset you must accept the license provided by the owners, '
-                'and cite the corresponding papers appropriately.')
-            print('If you do not agree with the above license, please cancel '
-                  'the progress immediately by pressing ctrl+c. Otherwise, '
-                  'you are deemed to accept the terms and conditions.\033[0m')
-            for i in range(5):
-                print(f'{5-i}...')
-                time.sleep(1)
-
-    def parse_cfg(self, cfg_path: str) -> None:
-        """Parse dataset config file.
-
-        Args:
-            cfg_path (str): Path to dataset config file.
-        """
-        cfg_path = osp.join(cfg_path, self.task + '.py')
-        assert osp.exists(cfg_path), f'Config file {cfg_path} not found!'
+def force_lmdb(cfg):
+    """Force the dataset to be dumped in lmdb format.
+
+    Args:
+        cfg (Config): Config object.
+
+    Returns:
+        Config: Config object.
+    """
+    for split in ['train', 'val', 'test']:
+        preparer_cfg = cfg.get(f'{split}_preparer')
+        if preparer_cfg:
+            if preparer_cfg.get('dumper') is None:
+                raise ValueError(
+                    f'{split} split does not come with a dumper, '
+                    'so most likely the annotations are MMOCR-ready and do '
+                    'not need any adaptation, and it '
+                    'cannot be dumped in LMDB format.')
+            preparer_cfg.dumper['type'] = 'TextRecogLMDBDumper'
+
+    cfg.config_generator['dataset_name'] = f'{cfg.dataset_name}_lmdb'
+
+    for split in ['train_anns', 'val_anns', 'test_anns']:
+        if split in cfg.config_generator:
+            # It can be None when users want to clear out the default
+            # value
+            if not cfg.config_generator[split]:
+                continue
+            ann_list = cfg.config_generator[split]
+            for ann_dict in ann_list:
+                ann_dict['ann_file'] = (
+                    osp.splitext(ann_dict['ann_file'])[0] + '.lmdb')
+        else:
+            if split == 'train_anns':
+                ann_list = [dict(ann_file='textrecog_train.lmdb')]
+            elif split == 'test_anns':
+                ann_list = [dict(ann_file='textrecog_test.lmdb')]
+            else:
+                ann_list = []
+        cfg.config_generator[split] = ann_list
+
+    return cfg
+
+
+def main():
+    args = parse_args()
+    if args.lmdb and args.task != 'textrecog':
+        raise ValueError('--lmdb only works with --task=textrecog')
+    for dataset in args.datasets:
+        if not osp.isdir(osp.join(args.dataset_zoo_path, dataset)):
+            warnings.warn(f'{dataset} is not supported yet. Please check '
+                          'dataset zoo for supported datasets.')
+            continue
+        meta_path = osp.join(args.dataset_zoo_path, dataset, 'metafile.yml')
+        parse_meta(args.task, meta_path)
+        cfg_path = osp.join(args.dataset_zoo_path, dataset, args.task + '.py')
         cfg = Config.fromfile(cfg_path)
+        if args.overwrite_cfg and cfg.get('config_generator',
+                                          None) is not None:
+            cfg.config_generator.overwrite_cfg = args.overwrite_cfg
+        cfg.nproc = args.nproc
+        cfg.task = args.task
+        cfg.dataset_name = dataset
+        if args.lmdb:
+            cfg = force_lmdb(cfg)
+        preparer = DatasetPreparer.from_file(cfg)
+        preparer.run(args.splits)
+
 
-        if 'data_obtainer' in cfg:
-            cfg.data_obtainer.update(task=self.task)
-            self.data_obtainer = DATA_OBTAINERS.build(cfg.data_obtainer)
-        if 'data_converter' in cfg:
-            cfg.data_converter.update(
-                dict(nproc=self.nproc, dataset_name=self.dataset_name))
-            self.data_converter = DATA_CONVERTERS.build(cfg.data_converter)
-        if 'config_generator' in cfg:
-            cfg.config_generator.update(
-                dict(
-                    dataset_name=self.dataset_name,
-                    overwrite_cfg=self.overwrite_cfg))
-            self.config_generator = CFG_GENERATORS.build(cfg.config_generator)
-
-    @property
-    def with_obtainer(self) -> bool:
-        """bool: whether the data preparer has an obtainer"""
-        return getattr(self, 'data_obtainer', None) is not None
-
-    @property
-    def with_converter(self) -> bool:
-        """bool: whether the data preparer has an converter"""
-        return getattr(self, 'data_converter', None) is not None
-
-    @property
-    def with_config_generator(self) -> bool:
-        """bool: whether the data preparer has a config generator"""
-        return getattr(self, 'config_generator', None) is not None
+if __name__ == '__main__':
+    main()
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/__init__.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 # Copyright (c) OpenMMLab. All rights reserved.
+from .base import BaseParser
 from .coco_parser import COCOTextDetAnnParser
 from .funsd_parser import FUNSDTextDetAnnParser
 from .icdar_txt_parser import (ICDARTxtTextDetAnnParser,
                                ICDARTxtTextRecogAnnParser)
 from .naf_parser import NAFAnnParser
 from .sroie_parser import SROIETextDetAnnParser
 from .svt_parser import SVTTextDetAnnParser
 from .totaltext_parser import TotaltextTextDetAnnParser
 from .wildreceipt_parser import WildreceiptKIEAnnParser
 
 __all__ = [
-    'ICDARTxtTextDetAnnParser', 'ICDARTxtTextRecogAnnParser',
+    'BaseParser', 'ICDARTxtTextDetAnnParser', 'ICDARTxtTextRecogAnnParser',
     'TotaltextTextDetAnnParser', 'WildreceiptKIEAnnParser',
     'COCOTextDetAnnParser', 'SVTTextDetAnnParser', 'FUNSDTextDetAnnParser',
     'SROIETextDetAnnParser', 'NAFAnnParser'
 ]
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/coco_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/coco_parser.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import os.path as osp
-from typing import Dict, Tuple
+from typing import List
 
 from mmdet.datasets.api_wrappers import COCO
 
-from mmocr.datasets.preparers.data_preparer import DATA_PARSERS
 from mmocr.datasets.preparers.parsers.base import BaseParser
+from mmocr.registry import DATA_PARSERS
 
 
 @DATA_PARSERS.register_module()
 class COCOTextDetAnnParser(BaseParser):
     """COCO-like Format Text Detection Parser.
 
     Args:
@@ -17,33 +17,33 @@
         nproc (int): The number of processes to parse the annotation. Defaults
             to 1.
         variant (str): Variant of COCO dataset, options are ['standard',
             'cocotext', 'textocr']. Defaults to 'standard'.
     """
 
     def __init__(self,
-                 data_root: str = None,
+                 split: str,
                  nproc: int = 1,
                  variant: str = 'standard') -> None:
 
-        super().__init__(nproc=nproc, data_root=data_root)
+        super().__init__(nproc=nproc, split=split)
         assert variant in ['standard', 'cocotext', 'textocr'], \
             f'variant {variant} is not supported'
         self.variant = variant
 
-    def parse_files(self, files: Tuple, split: str = None) -> Dict:
+    def parse_files(self, img_dir: str, ann_path: str) -> List:
         """Parse single annotation."""
         samples = list()
-        coco = COCO(files)
+        coco = COCO(ann_path)
         if self.variant == 'cocotext' or self.variant == 'textocr':
             # cocotext stores both 'train' and 'val' split in one annotation
             # file, and uses the 'set' field to distinguish them.
             if self.variant == 'cocotext':
                 for img in coco.dataset['imgs']:
-                    if split == coco.dataset['imgs'][img]['set']:
+                    if self.split == coco.dataset['imgs'][img]['set']:
                         coco.imgs[img] = coco.dataset['imgs'][img]
             # textocr stores 'train' and 'val'split separately
             elif self.variant == 'textocr':
                 coco.imgs = coco.dataset['imgs']
             # both cocotext and textocr stores the annotation ID in the
             # 'imgToAnns' field, so we need to convert it to the 'anns' field
             for img in coco.dataset['imgToAnns']:
@@ -56,16 +56,14 @@
                 coco.anns = coco.dataset['anns']
         img_ids = coco.get_img_ids()
         total_ann_ids = []
         for img_id in img_ids:
             img_info = coco.load_imgs([img_id])[0]
             img_info['img_id'] = img_id
             img_path = img_info['file_name']
-            if self.data_root is not None:
-                img_path = osp.join(self.data_root, img_path)
             ann_ids = coco.get_ann_ids(img_ids=[img_id])
             if len(ann_ids) == 0:
                 continue
             ann_ids = [str(ann_id) for ann_id in ann_ids]
             ann_info = coco.load_anns(ann_ids)
             total_ann_ids.extend(ann_ids)
             instances = list()
@@ -86,16 +84,16 @@
                     instances.append(
                         dict(
                             poly=ann['mask'],
                             text=ann.get('utf8_string', None),
                             ignore=ann['legibility'] == 'illegible'))
                 elif self.variant == 'textocr':
                     # textocr use 'utf8_string' field to store the text and
-                    # the 'points' field to store the polygon, ignore flag
-                    # is not available.
+                    # the 'points' field to store the polygon, '.' is used to
+                    # represent the ignored text.
+                    text = ann.get('utf8_string', None)
                     instances.append(
                         dict(
-                            poly=ann['points'],
-                            text=ann.get('utf8_string', None),
-                            ignore=False))
-            samples.append((img_path, instances))
+                            poly=ann['points'], text=text, ignore=text == '.'))
+            samples.append((osp.join(img_dir,
+                                     osp.basename(img_path)), instances))
         return samples
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/funsd_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/funsd_parser.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,37 +1,33 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import json
 from typing import Tuple
 
+from mmocr.registry import DATA_PARSERS
 from mmocr.utils import bbox2poly
-from ..data_preparer import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class FUNSDTextDetAnnParser(BaseParser):
     """FUNSD Text Detection Annotation Parser. See
     dataset_zoo/funsd/sample_anno.md for annotation example.
 
     Args:
         nproc (int): The number of processes to parse the annotation. Defaults
             to 1.
     """
 
-    def __init__(self, nproc: int = 1) -> None:
-        super().__init__(nproc=nproc)
-
-    def parse_file(self, file: Tuple, split: str) -> Tuple:
+    def parse_file(self, img_path: str, ann_path: str) -> Tuple:
         """Parse single annotation."""
-        img_file, json_file = file
         instances = list()
-        for poly, text, ignore in self.loader(json_file):
+        for poly, text, ignore in self.loader(ann_path):
             instances.append(dict(poly=poly, text=text, ignore=ignore))
 
-        return img_file, instances
+        return img_path, instances
 
     def loader(self, file_path: str):
         with open(file_path, 'r') as f:
             data = json.load(f)
             for form in data['form']:
                 for word in form['words']:
                     poly = bbox2poly(word['box']).tolist()
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/icdar_txt_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/icdar_txt_parser.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 # Copyright (c) OpenMMLab. All rights reserved.
+import os.path as osp
 from typing import List, Optional, Tuple
 
+from mmocr.registry import DATA_PARSERS
 from mmocr.utils import bbox2poly
-from ..data_preparer import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class ICDARTxtTextDetAnnParser(BaseParser):
     """ICDAR Txt Format Text Detection Annotation Parser.
 
@@ -31,30 +32,29 @@
     """
 
     def __init__(self,
                  separator: str = ',',
                  ignore: str = '###',
                  format: str = 'x1,y1,x2,y2,x3,y3,x4,y4,trans',
                  encoding: str = 'utf-8',
-                 nproc: int = 1,
                  remove_strs: Optional[List[str]] = None,
-                 mode: str = None) -> None:
+                 mode: str = None,
+                 **kwargs) -> None:
         self.sep = separator
         self.format = format
         self.encoding = encoding
         self.ignore = ignore
         self.mode = mode
         self.remove_strs = remove_strs
-        super().__init__(nproc=nproc)
+        super().__init__(**kwargs)
 
-    def parse_file(self, file: Tuple, split: str) -> Tuple:
+    def parse_file(self, img_path: str, ann_path: str) -> Tuple:
         """Parse single annotation."""
-        img_file, txt_file = file
         instances = list()
-        for anno in self.loader(txt_file, self.sep, self.format,
+        for anno in self.loader(ann_path, self.sep, self.format,
                                 self.encoding):
             anno = list(anno.values())
             if self.remove_strs is not None:
                 for strs in self.remove_strs:
                     for i in range(len(anno)):
                         if strs in anno[i]:
                             anno[i] = anno[i].replace(strs, '')
@@ -62,15 +62,15 @@
             if self.mode is not None:
                 poly = bbox2poly(poly, self.mode)
                 poly = poly.tolist()
             text = anno[-1]
             instances.append(
                 dict(poly=poly, text=text, ignore=text == self.ignore))
 
-        return img_file, instances
+        return img_path, instances
 
 
 @DATA_PARSERS.register_module()
 class ICDARTxtTextRecogAnnParser(BaseParser):
     """ICDAR Txt Format Text Recognition Annotation Parser.
 
     The original annotation format of this dataset is stored in txt files,
@@ -93,33 +93,35 @@
     """
 
     def __init__(self,
                  separator: str = ',',
                  ignore: str = '#',
                  format: str = 'img,text',
                  encoding: str = 'utf-8',
-                 nproc: int = 1,
-                 remove_strs: Optional[List[str]] = ['"']) -> None:
+                 remove_strs: Optional[List[str]] = ['"'],
+                 **kwargs) -> None:
         self.sep = separator
         self.format = format
         self.encoding = encoding
         self.ignore = ignore
         self.remove_strs = remove_strs
-        super().__init__(nproc=nproc)
+        super().__init__(**kwargs)
 
-    def parse_files(self, files: str, split: str) -> List:
+    def parse_files(self, img_dir: str, ann_path: str) -> List:
         """Parse annotations."""
-        assert isinstance(files, str)
+        assert isinstance(ann_path, str)
         samples = list()
         for anno in self.loader(
-                file_path=files,
+                file_path=ann_path,
                 format=self.format,
                 encoding=self.encoding,
                 separator=self.sep):
             text = anno['text'].strip()
             if self.remove_strs is not None:
                 for strs in self.remove_strs:
                     text = text.replace(strs, '')
+            if text == self.ignore:
+                continue
             img_name = anno['img']
-            samples.append((img_name, text))
+            samples.append((osp.join(img_dir, osp.basename(img_name)), text))
 
         return samples
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/naf_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/naf_parser.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import json
-from typing import Dict, List, Tuple
+from typing import List, Tuple
 
 import numpy as np
 
-from ..data_preparer import DATA_PARSERS
+from mmocr.registry import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class NAFAnnParser(BaseParser):
     """NAF dataset parser.
 
@@ -24,40 +24,36 @@
     Some special characters are used in the transcription:
     "«text»" indicates that "text" had a strikethrough
     "¿" indicates the transcriber could not read a character
     "§" indicates the whole line or word was illegible
     "" (empty string) is if the field was blank
 
     Args:
-        data_root (str): Path to the dataset root.
         ignore (list(str)): The text of the ignored instances. Default: ['#'].
         det (bool): Whether to parse the detection annotation. Default: True.
             If False, the parser will consider special case in NAF dataset
             where the transcription is not available.
-        nproc (int): Number of processes to load the data. Default: 1.
     """
 
     def __init__(self,
-                 data_root: str,
                  ignore: List[str] = ['#'],
                  det: bool = True,
-                 nproc: int = 1) -> None:
+                 **kwargs) -> None:
         self.ignore = ignore
         self.det = det
-        super().__init__(data_root=data_root, nproc=nproc)
+        super().__init__(**kwargs)
 
-    def parse_file(self, file: Tuple, split: str) -> Dict:
+    def parse_file(self, img_path: str, ann_path: str) -> Tuple:
         """Convert single annotation."""
-        img_file, json_file = file
         instances = list()
-        for poly, text in self.loader(json_file):
+        for poly, text in self.loader(ann_path):
             instances.append(
                 dict(poly=poly, text=text, ignore=text in self.ignore))
 
-        return img_file, instances
+        return img_path, instances
 
     def loader(self, file_path: str) -> str:
         """Load the annotation of the NAF dataset.
 
         Args:
             file_path (str): Path to the json file
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/sroie_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/sroie_parser.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from typing import List, Optional, Tuple
 
+from mmocr.registry import DATA_PARSERS
 from mmocr.utils import bbox2poly
-from ..data_preparer import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class SROIETextDetAnnParser(BaseParser):
     """SROIE Txt Format Text Detection Annotation Parser.
 
@@ -27,37 +27,37 @@
         remove_strs (List[str], Optional): Used to remove redundant strings in
             the transcription. Defaults to None.
         mode (str, optional): The mode of the box converter. Supported modes
             are 'xywh' and 'xyxy'. Defaults to None.
     """
 
     def __init__(self,
+                 split: str,
                  separator: str = ',',
                  ignore: str = '###',
                  format: str = 'x1,y1,x2,y2,x3,y3,x4,y4,trans',
                  encoding: str = 'utf-8-sig',
                  nproc: int = 1,
                  remove_strs: Optional[List[str]] = None,
                  mode: str = None) -> None:
         self.sep = separator
         self.format = format
         self.encoding = encoding
         self.ignore = ignore
         self.mode = mode
         self.remove_strs = remove_strs
-        super().__init__(nproc=nproc)
+        super().__init__(nproc=nproc, split=split)
 
-    def parse_file(self, file: Tuple, split: str) -> Tuple:
+    def parse_file(self, img_path: str, ann_path: str) -> Tuple:
         """Parse single annotation."""
-        img_file, txt_file = file
         instances = list()
         try:
             # there might be some illegal symbols in the annotation
             # which cannot be parsed by loader
-            for anno in self.loader(txt_file, self.sep, self.format,
+            for anno in self.loader(ann_path, self.sep, self.format,
                                     self.encoding):
                 anno = list(anno.values())
                 if self.remove_strs is not None:
                     for strs in self.remove_strs:
                         for i in range(len(anno)):
                             if strs in anno[i]:
                                 anno[i] = anno[i].replace(strs, '')
@@ -67,8 +67,8 @@
                     poly = poly.tolist()
                 text = anno[-1]
                 instances.append(
                     dict(poly=poly, text=text, ignore=text == self.ignore))
         except Exception:
             pass
 
-        return img_file, instances
+        return img_path, instances
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/svt_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/svt_parser.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,35 +1,33 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import os.path as osp
 import xml.etree.ElementTree as ET
 from typing import List, Tuple
 
-from ..data_preparer import DATA_PARSERS
+from mmocr.registry import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class SVTTextDetAnnParser(BaseParser):
     """SVT Text Detection Parser.
 
     Args:
         data_root (str): The root of the dataset. Defaults to None.
         nproc (int): The number of processes to parse the annotation. Defaults
             to 1.
     """
 
-    def __init__(self, data_root: str = None, nproc: int = 1) -> None:
-        super().__init__(data_root=data_root, nproc=nproc)
-
-    def parse_files(self, files: str, split: str) -> List:
+    def parse_files(self, img_dir: str, ann_path: str) -> List:
         """Parse annotations."""
-        assert isinstance(files, str)
+        assert isinstance(ann_path, str)
         samples = list()
-        for img_name, instance in self.loader(files):
-            samples.append((img_name, instance))
+        for img_name, instance in self.loader(ann_path):
+            samples.append((osp.join(img_dir,
+                                     osp.basename(img_name)), instance))
 
         return samples
 
     def loader(self, file_path: str) -> Tuple[str, List]:
         """Load annotation from SVT xml format file. See annotation example in
         dataset_zoo/svt/sample_anno.md.
 
@@ -41,16 +39,15 @@
 
         Yields:
             Iterator[Tuple[str, List]]: The image name and the annotation list.
         """
         tree = ET.parse(file_path)
         root = tree.getroot()
         for image in root.findall('image'):
-            image_name = osp.join(self.data_root, 'textdet_imgs',
-                                  image.find('imageName').text)
+            image_name = image.find('imageName').text
             instances = list()
             for rectangle in image.find('taggedRectangles'):
                 x = int(rectangle.get('x'))
                 y = int(rectangle.get('y'))
                 w = int(rectangle.get('width'))
                 h = int(rectangle.get('height'))
                 # The text annotation of this dataset is not case sensitive.
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/totaltext_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/totaltext_parser.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import re
 from typing import Dict, Tuple
 
 import yaml
 
-from ..data_preparer import DATA_PARSERS
+from mmocr.registry import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class TotaltextTextDetAnnParser(BaseParser):
     """TotalText Text Detection Parser.
 
@@ -19,30 +19,26 @@
 
     Args:
         data_root (str): Path to the dataset root.
         ignore (str): The text of the ignored instances. Default: '#'.
         nproc (int): Number of processes to load the data. Default: 1.
     """
 
-    def __init__(self,
-                 data_root: str,
-                 ignore: str = '#',
-                 nproc: int = 1) -> None:
+    def __init__(self, ignore: str = '#', **kwargs) -> None:
         self.ignore = ignore
-        super().__init__(data_root=data_root, nproc=nproc)
+        super().__init__(**kwargs)
 
-    def parse_file(self, file: Tuple, split: str) -> Dict:
+    def parse_file(self, img_path: str, ann_path: str) -> Dict:
         """Convert single annotation."""
-        img_file, txt_file = file
         instances = list()
-        for poly, text in self.loader(txt_file):
+        for poly, text in self.loader(ann_path):
             instances.append(
                 dict(poly=poly, text=text, ignore=text == self.ignore))
 
-        return img_file, instances
+        return img_path, instances
 
     def loader(self, file_path: str) -> str:
         """The annotation of the totaltext dataset may be stored in multiple
         lines, this loader is designed for this special case.
 
         Args:
             file_path (str): Path to the txt file
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/preparers/parsers/wildreceipt_parser.py` & `mmocr-1.0.0rc6/mmocr/datasets/preparers/parsers/wildreceipt_parser.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import json
 import os.path as osp
-from typing import Dict, Tuple
+from typing import Dict
 
+from mmocr.registry import DATA_PARSERS
 from mmocr.utils import list_from_file
-from ..data_preparer import DATA_PARSERS
 from .base import BaseParser
 
 
 @DATA_PARSERS.register_module()
 class WildreceiptTextDetAnnParser(BaseParser):
     """Wildreceipt Text Detection Parser.
 
@@ -26,29 +26,26 @@
     Args:
         data_root (str): The root path of the dataset.
         ignore (int): The label to be ignored. Defaults to 0.
         nproc (int): The number of processes to parse the annotation. Defaults
             to 1.
     """
 
-    def __init__(self,
-                 data_root: str,
-                 ignore: int = 0,
-                 nproc: int = 1) -> None:
+    def __init__(self, ignore: int = 0, **kwargs) -> None:
         self.ignore = ignore
-        super().__init__(data_root=data_root, nproc=nproc)
+        super().__init__(**kwargs)
 
-    def parse_files(self, files: Tuple, split: str) -> Dict:
+    def parse_files(self, img_dir: str, ann_path) -> Dict:
         """Convert single annotation."""
-        closeset_lines = list_from_file(files)
+        closeset_lines = list_from_file(ann_path)
         samples = list()
         for line in closeset_lines:
             instances = list()
             line = json.loads(line)
-            img_file = osp.join(self.data_root, line['file_name'])
+            img_file = osp.join(img_dir, osp.basename(line['file_name']))
             for anno in line['annotations']:
                 poly = anno['box']
                 text = anno['text']
                 label = anno['label']
                 instances.append(
                     dict(poly=poly, text=text, ignore=label == self.ignore))
             samples.append((img_file, instances))
@@ -68,25 +65,27 @@
         "annotations": [
             "box": [x1, y1, x2, y2, x3, y3, x4, y4],
             "text": "xxx",
             "label": 25,
         ]}
 
     Args:
-        data_root (str): The root path of the dataset.
         ignore (int): The label to be ignored. Defaults to 0.
         nproc (int): The number of processes to parse the annotation. Defaults
             to 1.
     """
 
-    def __init__(self,
-                 data_root: str,
-                 ignore: int = 0,
-                 nproc: int = 1) -> None:
+    def __init__(self, ignore: int = 0, **kwargs) -> None:
         self.ignore = ignore
-        super().__init__(data_root=data_root, nproc=nproc)
+        super().__init__(**kwargs)
 
-    def parse_files(self, files: Tuple, split: str) -> Dict:
+    def parse_files(self, img_dir: str, ann_path: str) -> Dict:
         """Convert single annotation."""
-        closeset_lines = list_from_file(files)
+        closeset_lines = list_from_file(ann_path)
+        samples = list()
+        for line in closeset_lines:
+            json_line = json.loads(line)
+            img_file = osp.join(img_dir, osp.basename(json_line['file_name']))
+            json_line['file_name'] = img_file
+            samples.append(json.dumps(json_line))
 
-        return closeset_lines
+        return samples
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/recog_text_dataset.py` & `mmocr-1.0.0rc6/mmocr/datasets/recog_text_dataset.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/__init__.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from .adapters import MMDet2MMOCR, MMOCR2MMDet
 from .formatting import PackKIEInputs, PackTextDetInputs, PackTextRecogInputs
-from .loading import (LoadImageFromFile, LoadImageFromLMDB,
+from .loading import (InferencerLoader, LoadImageFromFile,
                       LoadImageFromNDArray, LoadKIEAnnotations,
                       LoadOCRAnnotations)
 from .ocr_transforms import (FixInvalidPolygon, RandomCrop, RandomRotate,
                              RemoveIgnored, Resize)
 from .textdet_transforms import (BoundedScaleAspectJitter, RandomFlip,
                                  ShortScaleAspectJitter, SourceImagePad,
                                  TextDetRandomCrop, TextDetRandomCropFlip)
@@ -17,11 +17,11 @@
 __all__ = [
     'LoadOCRAnnotations', 'RandomRotate', 'ImgAugWrapper', 'SourceImagePad',
     'TextDetRandomCropFlip', 'PyramidRescale', 'TorchVisionWrapper', 'Resize',
     'RandomCrop', 'TextDetRandomCrop', 'RandomCrop', 'PackTextDetInputs',
     'PackTextRecogInputs', 'RescaleToHeight', 'PadToWidth',
     'ShortScaleAspectJitter', 'RandomFlip', 'BoundedScaleAspectJitter',
     'PackKIEInputs', 'LoadKIEAnnotations', 'FixInvalidPolygon', 'MMDet2MMOCR',
-    'MMOCR2MMDet', 'LoadImageFromLMDB', 'LoadImageFromFile',
-    'LoadImageFromNDArray', 'CropHeight', 'TextRecogGeneralAug',
-    'ImageContentJitter', 'ReversePixels', 'RemoveIgnored', 'ConditionApply'
+    'MMOCR2MMDet', 'LoadImageFromFile', 'LoadImageFromNDArray', 'CropHeight',
+    'InferencerLoader', 'RemoveIgnored', 'ConditionApply', 'CropHeight',
+    'TextRecogGeneralAug', 'ImageContentJitter', 'ReversePixels'
 ]
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/adapters.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/adapters.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/formatting.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/formatting.py`

 * *Files 14% similar despite different names*

```diff
@@ -86,16 +86,25 @@
               sample.
         """
         packed_results = dict()
         if 'img' in results:
             img = results['img']
             if len(img.shape) < 3:
                 img = np.expand_dims(img, -1)
-            img = np.ascontiguousarray(img.transpose(2, 0, 1))
-            packed_results['inputs'] = to_tensor(img)
+            # A simple trick to speedup formatting by 3-5 times when
+            # OMP_NUM_THREADS != 1
+            # Refer to https://github.com/open-mmlab/mmdetection/pull/9533
+            # for more details
+            if img.flags.c_contiguous:
+                img = to_tensor(img)
+                img = img.permute(2, 0, 1).contiguous()
+            else:
+                img = np.ascontiguousarray(img.transpose(2, 0, 1))
+                img = to_tensor(img)
+            packed_results['inputs'] = img
 
         data_sample = TextDetDataSample()
         instance_data = InstanceData()
         for key in self.mapping_table.keys():
             if key not in results:
                 continue
             if key in ['gt_bboxes', 'gt_bboxes_labels', 'gt_ignored']:
@@ -170,16 +179,25 @@
                 of the sample.
         """
         packed_results = dict()
         if 'img' in results:
             img = results['img']
             if len(img.shape) < 3:
                 img = np.expand_dims(img, -1)
-            img = np.ascontiguousarray(img.transpose(2, 0, 1))
-            packed_results['inputs'] = to_tensor(img)
+            # A simple trick to speedup formatting by 3-5 times when
+            # OMP_NUM_THREADS != 1
+            # Refer to https://github.com/open-mmlab/mmdetection/pull/9533
+            # for more details
+            if img.flags.c_contiguous:
+                img = to_tensor(img)
+                img = img.permute(2, 0, 1).contiguous()
+            else:
+                img = np.ascontiguousarray(img.transpose(2, 0, 1))
+                img = to_tensor(img)
+            packed_results['inputs'] = img
 
         data_sample = TextRecogDataSample()
         gt_text = LabelData()
 
         if results.get('gt_texts', None):
             assert len(
                 results['gt_texts']
@@ -268,16 +286,25 @@
               sample.
         """
         packed_results = dict()
         if 'img' in results:
             img = results['img']
             if len(img.shape) < 3:
                 img = np.expand_dims(img, -1)
-            img = np.ascontiguousarray(img.transpose(2, 0, 1))
-            packed_results['inputs'] = to_tensor(img)
+            # A simple trick to speedup formatting by 3-5 times when
+            # OMP_NUM_THREADS != 1
+            # Refer to https://github.com/open-mmlab/mmdetection/pull/9533
+            # for more details
+            if img.flags.c_contiguous:
+                img = to_tensor(img)
+                img = img.permute(2, 0, 1).contiguous()
+            else:
+                img = np.ascontiguousarray(img.transpose(2, 0, 1))
+                img = to_tensor(img)
+            packed_results['inputs'] = img
         else:
             packed_results['inputs'] = torch.FloatTensor().reshape(0, 0, 0)
 
         data_sample = KIEDataSample()
         instance_data = InstanceData()
         for key in self.mapping_table.keys():
             if key not in results:
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/loading.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/loading.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import copy
-import os
 import warnings
-from typing import Optional
+from typing import Optional, Union
 
 import mmcv
 import mmengine
 import numpy as np
 from mmcv.transforms import BaseTransform
 from mmcv.transforms import LoadAnnotations as MMCV_LoadAnnotations
 from mmcv.transforms import LoadImageFromFile as MMCV_LoadImageFromFile
@@ -64,19 +63,14 @@
         self.min_size = min_size
 
     def transform(self, results: dict) -> Optional[dict]:
         """Functions to load image.
 
         Args:
             results (dict): Result dict from :obj:``mmcv.BaseDataset``.
-        """
-        """Functions to load image.
-
-        Args:
-            results (dict): Result dict from :obj:``mmcv.BaseDataset``.
 
         Returns:
             dict: The dict contains loaded image and meta information.
         """
 
         filename = results['img_path']
         try:
@@ -151,22 +145,72 @@
         """
 
         img = results['img']
         if self.to_float32:
             img = img.astype(np.float32)
         if self.color_type == 'grayscale':
             img = mmcv.image.rgb2gray(img)
-        results['img_path'] = None
         results['img'] = img
+        if results.get('img_path', None) is None:
+            results['img_path'] = None
         results['img_shape'] = img.shape[:2]
         results['ori_shape'] = img.shape[:2]
         return results
 
 
 @TRANSFORMS.register_module()
+class InferencerLoader(BaseTransform):
+    """Load the image in Inferencer's pipeline.
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
+            single_input (str or dict or np.ndarray): The raw input from
+                inferencer.
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
+
+        return self.from_file(inputs)
+
+
+@TRANSFORMS.register_module()
 class LoadOCRAnnotations(MMCV_LoadAnnotations):
     """Load and process the ``instances`` annotation provided by dataset.
 
     The annotation format is as the following:
 
     .. code-block:: python
 
@@ -483,118 +527,7 @@
 
     def __repr__(self) -> str:
         repr_str = self.__class__.__name__
         repr_str += f'(with_bbox={self.with_bbox}, '
         repr_str += f'with_label={self.with_label}, '
         repr_str += f'with_text={self.with_text})'
         return repr_str
-
-
-@TRANSFORMS.register_module()
-class LoadImageFromLMDB(BaseTransform):
-    """Load an image from lmdb file. Only support LMDB file at disk.
-
-    LMDB file is organized with the following structure:
-        lmdb
-            |__data.mdb
-            |__lock.mdb
-
-    Required Keys:
-
-    - img_path (In LMDB img_path is a key in the format of "image-{i:09d}".)
-
-    Modified Keys:
-
-    - img
-    - img_shape
-    - ori_shape
-
-    Args:
-        to_float32 (bool): Whether to convert the loaded image to a float32
-            numpy array. If set to False, the loaded image is an uint8 array.
-            Defaults to False.
-        color_type (str): The flag argument for :func:``mmcv.imfrombytes``.
-            Defaults to 'color'.
-        imdecode_backend (str): The image decoding backend type. The backend
-            argument for :func:``mmcv.imfrombytes``.
-            See :func:``mmcv.imfrombytes`` for details.
-            Defaults to 'cv2'.
-        file_client_args (dict): Arguments to instantiate a FileClient except
-            for ``backend`` and ``db_path``. See
-            :class:`mmengine.fileio.FileClient` for details.
-            Defaults to ``dict()``.
-        ignore_empty (bool): Whether to allow loading empty image or file path
-            not existent. Defaults to False.
-    """
-
-    def __init__(
-            self,
-            to_float32: bool = False,
-            color_type: str = 'color',
-            imdecode_backend: str = 'cv2',
-            file_client_args: dict = dict(),
-            ignore_empty: bool = False,
-    ) -> None:
-        self.ignore_empty = ignore_empty
-        self.to_float32 = to_float32
-        self.color_type = color_type
-        self.imdecode_backend = imdecode_backend
-        self.file_clients = {}
-        if 'backend' in file_client_args or 'db_path' in file_client_args:
-            raise ValueError(
-                '"file_client_args" should not contain "backend" and "db_path"'
-            )
-        self.file_client_args = file_client_args
-
-    def _get_client(self, db_path: str) -> mmengine.FileClient:
-        """Get a FileClient bound to the given db_path.
-
-        If the client for this db_path is not initialized, initialize it.
-        """
-        if self.file_clients.get(db_path) is None:
-            self.file_clients[db_path] = mmengine.FileClient(
-                backend='lmdb', db_path=db_path, **self.file_client_args)
-        return self.file_clients.get(db_path)
-
-    def transform(self, results: dict) -> Optional[dict]:
-        """Functions to load image from LMDB file.
-
-        Args:
-            results (dict): Result dict from :obj:``mmcv.BaseDataset``.
-
-        Returns:
-            dict: The dict contains loaded image and meta information.
-        """
-        filename = results['img_path']
-        lmdb_path = os.path.dirname(filename)
-        image_key = os.path.basename(filename)
-        file_client = self._get_client(lmdb_path)
-        img_bytes = file_client.get(image_key)
-
-        if img_bytes is None:
-            if self.ignore_empty:
-                return None
-            raise KeyError(f'Image not found in lmdb: {filename}')
-
-        img = mmcv.imfrombytes(img_bytes, flag=self.color_type)
-
-        if img is None:
-            if self.ignore_empty:
-                return None
-            raise IOError(f'{filename} is broken')
-
-        if self.to_float32:
-            img = img.astype(np.float32)
-
-        results['img'] = img
-        results['img_shape'] = img.shape[:2]
-        results['ori_shape'] = img.shape[:2]
-        return results
-
-    def __repr__(self):
-        repr_str = (f'{self.__class__.__name__}('
-                    f'ignore_empty={self.ignore_empty}, '
-                    f'to_float32={self.to_float32}, '
-                    f"color_type='{self.color_type}', "
-                    f"imdecode_backend='{self.imdecode_backend}', "
-                    f'file_client_args={self.file_client_args})')
-        return repr_str
```

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/ocr_transforms.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/ocr_transforms.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/textdet_transforms.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/textdet_transforms.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/textrecog_transforms.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/textrecog_transforms.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/transforms/wrappers.py` & `mmocr-1.0.0rc6/mmocr/datasets/transforms/wrappers.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/datasets/wildreceipt_dataset.py` & `mmocr-1.0.0rc6/mmocr/datasets/recog_lmdb_dataset.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,205 +1,179 @@
 # Copyright (c) OpenMMLab. All rights reserved.
-import copy
-from typing import Callable, List, Optional, Sequence, Union
+from typing import Any, Callable, List, Optional, Sequence, Tuple, Union
 
-import numpy as np
+import mmcv
 from mmengine.dataset import BaseDataset
-from mmengine.fileio import list_from_file
 
 from mmocr.registry import DATASETS
-from mmocr.utils.parsers import LineJsonParser
-from mmocr.utils.polygon_utils import sort_vertex8
 
 
 @DATASETS.register_module()
-class WildReceiptDataset(BaseDataset):
-    """WildReceipt Dataset for key information extraction. There are two files
-    to be loaded: metainfo and annotation. The metainfo file contains the
-    mapping between classes and labels. The annotation file contains the all
-    necessary information about the image, such as bounding boxes, texts, and
-    labels etc.
-
-    The metainfo file is a text file with the following format:
-
-    .. code-block:: none
-
-        0 Ignore
-        1 Store_name_value
-        2 Store_name_key
-
-    The annotation format is shown as follows.
-
-    .. code-block:: json
-
-        {
-            "file_name": "a.jpeg",
-            "height": 348,
-            "width": 348,
-            "annotations": [
-                {
-                    "box": [
-                        114.0,
-                        19.0,
-                        230.0,
-                        19.0,
-                        230.0,
-                        1.0,
-                        114.0,
-                        1.0
-                    ],
-                    "text": "CHOEUN",
-                    "label": 1
-                },
-                {
-                    "box": [
-                        97.0,
-                        35.0,
-                        236.0,
-                        35.0,
-                        236.0,
-                        19.0,
-                        97.0,
-                        19.0
-                    ],
-                    "text": "KOREANRESTAURANT",
-                    "label": 2
-                }
-            ]
-        }
+class RecogLMDBDataset(BaseDataset):
+    r"""RecogLMDBDataset for text recognition.
+
+    The annotation format should be in lmdb format. The lmdb file should
+    contain three keys: 'num-samples', 'label-xxxxxxxxx' and 'image-xxxxxxxxx',
+    where 'xxxxxxxxx' is the index of the image. The value of 'num-samples' is
+    the total number of images. The value of 'label-xxxxxxx' is the text label
+    of the image, and the value of 'image-xxxxxxx' is the image data.
+
+    following keys:
+    Each item fetched from this dataset will be a dict containing the
+    following keys:
+
+        - img (ndarray): The loaded image.
+        - img_path (str): The image key.
+        - instances (list[dict]): The list of annotations for the image.
 
     Args:
-        directed (bool): Whether to use directed graph. Defaults to False.
         ann_file (str): Annotation file path. Defaults to ''.
-        metainfo (str or dict, optional): Meta information for dataset, such as
-            class information. If it's a string, it will be treated as a path
-            to the class file from which the class information will be loaded.
-            Defaults to None.
-        data_root (str, optional): The root directory for ``data_prefix`` and
+        img_color_type (str): The flag argument for :func:``mmcv.imfrombytes``,
+            which determines how the image bytes will be parsed. Defaults to
+            'color'.
+        metainfo (dict, optional): Meta information for dataset, such as class
+            information. Defaults to None.
+        data_root (str): The root directory for ``data_prefix`` and
             ``ann_file``. Defaults to ''.
-        data_prefix (dict, optional): Prefix for training data. Defaults to
-            dict(img_path='').
+        data_prefix (dict): Prefix for training data. Defaults to
+            ``dict(img_path='')``.
         filter_cfg (dict, optional): Config for filter data. Defaults to None.
         indices (int or Sequence[int], optional): Support using first few
             data in annotation file to facilitate training/testing on a smaller
             dataset. Defaults to None which means using all ``data_infos``.
         serialize_data (bool, optional): Whether to hold memory using
             serialized objects, when enabled, data loader workers can use
             shared RAM from master process instead of making a copy. Defaults
             to True.
         pipeline (list, optional): Processing pipeline. Defaults to [].
         test_mode (bool, optional): ``test_mode=True`` means in test phase.
             Defaults to False.
         lazy_init (bool, optional): Whether to load annotation during
             instantiation. In some cases, such as visualization, only the meta
             information of the dataset is needed, which is not necessary to
-            load annotation file. ``Basedataset`` can skip load annotations to
-            save time by set ``lazy_init=False``. Defaults to False.
-        max_refetch (int, optional): If ``Basedataset.prepare_data`` get a
+            load annotation file. ``RecogLMDBDataset`` can skip load
+            annotations to save time by set ``lazy_init=False``.
+            Defaults to False.
+        max_refetch (int, optional): If ``RecogLMDBdataset.prepare_data`` get a
             None img. The maximum extra number of cycles to get a valid
             image. Defaults to 1000.
     """
 
-    def __init__(self,
-                 directed: bool = False,
-                 ann_file: str = '',
-                 metainfo: Optional[Union[dict, str]] = None,
-                 data_root: str = '',
-                 data_prefix: dict = dict(img_path=''),
-                 filter_cfg: Optional[dict] = None,
-                 indices: Optional[Union[int, Sequence[int]]] = None,
-                 serialize_data: bool = True,
-                 pipeline: List[Union[dict, Callable]] = ...,
-                 test_mode: bool = False,
-                 lazy_init: bool = False,
-                 max_refetch: int = 1000):
-        self.directed = directed
-        super().__init__(ann_file, metainfo, data_root, data_prefix,
-                         filter_cfg, indices, serialize_data, pipeline,
-                         test_mode, lazy_init, max_refetch)
-        self._metainfo['dataset_type'] = 'WildReceiptDataset'
-        self._metainfo['task_name'] = 'KIE'
-
-    @classmethod
-    def _load_metainfo(cls, metainfo: Union[str, dict] = None) -> dict:
-        """Collect meta information from path to the class list or the
-        dictionary of meta.
+    def __init__(
+        self,
+        ann_file: str = '',
+        img_color_type: str = 'color',
+        metainfo: Optional[dict] = None,
+        data_root: Optional[str] = '',
+        data_prefix: dict = dict(img_path=''),
+        filter_cfg: Optional[dict] = None,
+        indices: Optional[Union[int, Sequence[int]]] = None,
+        serialize_data: bool = True,
+        pipeline: List[Union[dict, Callable]] = [],
+        test_mode: bool = False,
+        lazy_init: bool = False,
+        max_refetch: int = 1000,
+    ) -> None:
+
+        super().__init__(
+            ann_file=ann_file,
+            metainfo=metainfo,
+            data_root=data_root,
+            data_prefix=data_prefix,
+            filter_cfg=filter_cfg,
+            indices=indices,
+            serialize_data=serialize_data,
+            pipeline=pipeline,
+            test_mode=test_mode,
+            lazy_init=lazy_init,
+            max_refetch=max_refetch)
 
-        Args:
-            metainfo (str or dict): Path to the class list, or a meta
-            information dict. If ``metainfo`` contains existed filename, it
-            will be parsed by ``list_from_file``.
-
-        Returns:
-            dict: Parsed meta information.
-        """
-        cls_metainfo = copy.deepcopy(cls.METAINFO)
-        if isinstance(metainfo, str):
-            cls_metainfo['category'] = []
-            for line in list_from_file(metainfo):
-                k, v = line.split()
-                cls_metainfo['category'].append({'id': k, 'name': v})
-            return cls_metainfo
-        else:
-            return super()._load_metainfo(metainfo)
+        self.color_type = img_color_type
 
     def load_data_list(self) -> List[dict]:
-        """Load data list from annotation file.
+        """Load annotations from an annotation file named as ``self.ann_file``
 
         Returns:
-            List[dict]: A list of annotation dict.
+            List[dict]: A list of annotation.
         """
-        parser = LineJsonParser(
-            keys=['file_name', 'height', 'width', 'annotations'])
+        if not hasattr(self, 'env'):
+            self._make_env()
+            with self.env.begin(write=False) as txn:
+                self.total_number = int(
+                    txn.get(b'num-samples').decode('utf-8'))
+
         data_list = []
-        for line in list_from_file(self.ann_file):
-            data_info = parser(line)
-            data_info = self.parse_data_info(data_info)
-            data_list.append(data_info)
+        with self.env.begin(write=False) as txn:
+            for i in range(self.total_number):
+                idx = i + 1
+                label_key = f'label-{idx:09d}'
+                img_key = f'image-{idx:09d}'
+                text = txn.get(label_key.encode('utf-8')).decode('utf-8')
+                line = [img_key, text]
+                data_list.append(self.parse_data_info(line))
         return data_list
 
-    def parse_data_info(self, raw_data_info: dict) -> dict:
-        """Parse data info from raw data info.
+    def parse_data_info(self,
+                        raw_anno_info: Tuple[Optional[str],
+                                             str]) -> Union[dict, List[dict]]:
+        """Parse raw annotation to target format.
 
         Args:
-            raw_data_info (dict): Raw data info.
+            raw_anno_info (str): One raw data information loaded
+                from ``ann_file``.
 
         Returns:
-            dict: Parsed data info.
+            (dict): Parsed annotation.
+        """
+        data_info = {}
+        img_key, text = raw_anno_info
+        data_info['img_key'] = img_key
+        data_info['instances'] = [dict(text=text)]
+        return data_info
+
+    def prepare_data(self, idx) -> Any:
+        """Get data processed by ``self.pipeline``.
+
+        Args:
+            idx (int): The index of ``data_info``.
 
-            - img_path (str): Path to the image.
-            - img_shape (tuple(int, int)): Image shape in (H, W).
-            - instances (list[dict]): A list of instances.
-              - bbox (ndarray(dtype=np.float32)): Shape (4, ). Bounding box.
-              - text (str): Annotation text.
-              - edge_label (int): Edge label.
-              - bbox_label (int): Bounding box label.
+        Returns:
+            Any: Depends on ``self.pipeline``.
         """
+        data_info = self.get_data_info(idx)
+        with self.env.begin(write=False) as txn:
+            img_bytes = txn.get(data_info['img_key'].encode('utf-8'))
+            if img_bytes is None:
+                return None
+            data_info['img'] = mmcv.imfrombytes(
+                img_bytes, flag=self.color_type)
+        return self.pipeline(data_info)
+
+    def _make_env(self):
+        """Create lmdb environment from self.ann_file and save it to
+        ``self.env``.
 
-        raw_data_info['img_path'] = raw_data_info['file_name']
-        data_info = super().parse_data_info(raw_data_info)
-        annotations = data_info['annotations']
-
-        assert 'box' in annotations[0]
-        assert 'text' in annotations[0]
-
-        instances = []
-
-        for ann in annotations:
-            instance = {}
-            bbox = np.array(sort_vertex8(ann['box']), dtype=np.int32)
-            bbox = np.array([
-                bbox[0::2].min(), bbox[1::2].min(), bbox[0::2].max(),
-                bbox[1::2].max()
-            ],
-                            dtype=np.int32)
-
-            instance['bbox'] = bbox
-            instance['text'] = ann['text']
-            instance['bbox_label'] = ann.get('label', 0)
-            instance['edge_label'] = ann.get('edge', 0)
-            instances.append(instance)
-
-        return dict(
-            instances=instances,
-            img_path=data_info['img_path'],
-            img_shape=(data_info['height'], data_info['width']))
+        Returns:
+            Lmdb environment.
+        """
+        try:
+            import lmdb
+        except ImportError:
+            raise ImportError(
+                'Please install lmdb to enable RecogLMDBDataset.')
+        if hasattr(self, 'env'):
+            return
+
+        self.env = lmdb.open(
+            self.ann_file,
+            max_readers=1,
+            readonly=True,
+            lock=False,
+            readahead=False,
+            meminit=False,
+        )
+
+    def close(self):
+        """Close lmdb environment."""
+        if hasattr(self, 'env'):
+            self.env.close()
+            del self.env
```

### Comparing `mmocr-1.0.0rc5/mmocr/engine/hooks/visualization_hook.py` & `mmocr-1.0.0rc6/mmocr/engine/hooks/visualization_hook.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/evaluation/evaluator/multi_datasets_evaluator.py` & `mmocr-1.0.0rc6/mmocr/evaluation/evaluator/multi_datasets_evaluator.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/evaluation/functional/hmean.py` & `mmocr-1.0.0rc6/mmocr/evaluation/functional/hmean.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/evaluation/metrics/f_metric.py` & `mmocr-1.0.0rc6/mmocr/evaluation/metrics/f_metric.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/evaluation/metrics/hmean_iou_metric.py` & `mmocr-1.0.0rc6/mmocr/evaluation/metrics/hmean_iou_metric.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/evaluation/metrics/recog_metric.py` & `mmocr-1.0.0rc6/mmocr/evaluation/metrics/recog_metric.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/backbones/clip_resnet.py` & `mmocr-1.0.0rc6/mmocr/models/common/backbones/clip_resnet.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/backbones/unet.py` & `mmocr-1.0.0rc6/mmocr/models/common/backbones/unet.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/dictionary/dictionary.py` & `mmocr-1.0.0rc6/mmocr/models/common/dictionary/dictionary.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/layers/transformer_layers.py` & `mmocr-1.0.0rc6/mmocr/models/common/layers/transformer_layers.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/losses/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/common/losses/__init__.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/losses/bce_loss.py` & `mmocr-1.0.0rc6/mmocr/models/common/losses/bce_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/losses/dice_loss.py` & `mmocr-1.0.0rc6/mmocr/models/common/losses/dice_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/losses/l1_loss.py` & `mmocr-1.0.0rc6/mmocr/models/common/losses/l1_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/modules/transformer_module.py` & `mmocr-1.0.0rc6/mmocr/models/common/modules/transformer_module.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/common/plugins/common.py` & `mmocr-1.0.0rc6/mmocr/models/common/plugins/common.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/kie/extractors/sdmgr.py` & `mmocr-1.0.0rc6/mmocr/models/kie/extractors/sdmgr.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/kie/heads/sdmgr_head.py` & `mmocr-1.0.0rc6/mmocr/models/kie/heads/sdmgr_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/kie/module_losses/sdmgr_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/kie/module_losses/sdmgr_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/kie/postprocessors/sdmgr_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/kie/postprocessors/sdmgr_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/data_preprocessors/data_preprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/data_preprocessors/data_preprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/detectors/base.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/detectors/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/detectors/mmdet_wrapper.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/detectors/mmdet_wrapper.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/detectors/single_stage_text_detector.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/detectors/single_stage_text_detector.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/base.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/db_head.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/db_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/drrg_head.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/drrg_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/fce_head.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/fce_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/pan_head.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/pan_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/pse_head.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/pse_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/heads/textsnake_head.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/heads/textsnake_head.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/__init__.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/base.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/db_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/db_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/drrg_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/drrg_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/fce_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/fce_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/pan_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/pan_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/pse_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/pse_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/seg_based_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/seg_based_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/module_losses/textsnake_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/module_losses/textsnake_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpem_ffm.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpem_ffm.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpn_cat.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpn_cat.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpn_unet.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpn_unet.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/necks/fpnf.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/necks/fpnf.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/__init__.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/base.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/db_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/db_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/drrg_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/drrg_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/pan_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/pan_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/pse_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/pse_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textdet/postprocessors/textsnake_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textdet/postprocessors/textsnake_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/mini_vgg.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/mini_vgg.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/mobilenet_v2.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/mobilenet_v2.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/nrtr_modality_transformer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/nrtr_modality_transformer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/resnet.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/resnet.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/resnet31_ocr.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/resnet31_ocr.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/resnet_abi.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/resnet_abi.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/backbones/shallow_cnn.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/backbones/shallow_cnn.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/data_preprocessors/data_preprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/data_preprocessors/data_preprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/__init__.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/abi_fuser.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/abi_fuser.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/abi_language_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/abi_language_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/abi_vision_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/abi_vision_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/aster_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/aster_decoder.py`

 * *Files 1% similar despite different names*

```diff
@@ -67,14 +67,15 @@
         self.gru = nn.GRU(
             input_size=self.in_channels + self.embedding_dim,
             hidden_size=self.hidden_size,
             batch_first=True)
 
         # Prediction layer
         self.fc = nn.Linear(hidden_size, self.dictionary.num_classes)
+        self.softmax = nn.Softmax(dim=-1)
 
     def _attention(self, feat: torch.Tensor, prev_hidden: torch.Tensor,
                    prev_char: torch.Tensor
                    ) -> Tuple[torch.Tensor, torch.Tensor]:
         """Implement the attention mechanism.
 
         Args:
@@ -173,8 +174,8 @@
             else:
                 prev_char = predicted
 
             output, state = self._attention(out_enc, state, prev_char)
             outputs.append(output)
             _, predicted = output.max(-1)
         outputs = torch.cat([_.unsqueeze(1) for _ in outputs], 1)
-        return outputs
+        return self.softmax(outputs)
```

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/base.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/crnn_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/crnn_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/master_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/master_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/nrtr_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/nrtr_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/position_attention_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/position_attention_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/robust_scanner_fuser.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/robust_scanner_fuser.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/sar_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/sar_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/sar_decoder_with_bs.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/sar_decoder_with_bs.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/sequence_attention_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/sequence_attention_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/decoders/svtr_decoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/decoders/svtr_decoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/__init__.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/abi_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/abi_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/aster_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/aster_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/channel_reduction_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/channel_reduction_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/nrtr_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/nrtr_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/sar_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/sar_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/satrn_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/satrn_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/encoders/svtr_encoder.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/encoders/svtr_encoder.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/__init__.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/conv_layer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/conv_layer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/dot_product_attention_layer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/dot_product_attention_layer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/lstm_layer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/lstm_layer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/position_aware_layer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/position_aware_layer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/robust_scanner_fusion_layer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/robust_scanner_fusion_layer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/layers/satrn_layers.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/layers/satrn_layers.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/abi_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/abi_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/base.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/ce_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/ce_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/module_losses/ctc_module_loss.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/module_losses/ctc_module_loss.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/plugins/common.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/plugins/common.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/attn_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/attn_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/base.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/postprocessors/ctc_postprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/postprocessors/ctc_postprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/preprocessors/tps_preprocessor.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/preprocessors/tps_preprocessor.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/__init__.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,17 +1,19 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from .abinet import ABINet
 from .aster import ASTER
 from .base import BaseRecognizer
 from .crnn import CRNN
 from .encoder_decoder_recognizer import EncoderDecoderRecognizer
+from .encoder_decoder_recognizer_tta import EncoderDecoderRecognizerTTAModel
 from .master import MASTER
 from .nrtr import NRTR
 from .robust_scanner import RobustScanner
 from .sar import SARNet
 from .satrn import SATRN
 from .svtr import SVTR
 
 __all__ = [
     'BaseRecognizer', 'EncoderDecoderRecognizer', 'CRNN', 'SARNet', 'NRTR',
-    'RobustScanner', 'SATRN', 'ABINet', 'MASTER', 'SVTR', 'ASTER'
+    'RobustScanner', 'SATRN', 'ABINet', 'MASTER', 'SVTR', 'ASTER',
+    'EncoderDecoderRecognizerTTAModel'
 ]
```

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/base.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/base.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/models/textrecog/recognizers/encoder_decoder_recognizer.py` & `mmocr-1.0.0rc6/mmocr/models/textrecog/recognizers/encoder_decoder_recognizer.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/structures/kie_data_sample.py` & `mmocr-1.0.0rc6/mmocr/structures/kie_data_sample.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/structures/textdet_data_sample.py` & `mmocr-1.0.0rc6/mmocr/structures/textdet_data_sample.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/structures/textrecog_data_sample.py` & `mmocr-1.0.0rc6/mmocr/structures/textrecog_data_sample.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/structures/textspotting_data_sample.py` & `mmocr-1.0.0rc6/mmocr/structures/textspotting_data_sample.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/testing/data.py` & `mmocr-1.0.0rc6/mmocr/testing/data.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/__init__.py` & `mmocr-1.0.0rc6/mmocr/utils/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from .bbox_utils import (bbox2poly, bbox_center_distance, bbox_diag_distance,
                          bezier2polygon, is_on_same_line, rescale_bbox,
                          rescale_bboxes, stitch_boxes_into_lines)
+from .bezier_utils import bezier2poly, poly2bezier
 from .check_argument import (equal_len, is_2dlist, is_3dlist, is_none_or_type,
                              is_type_list, valid_boundary)
 from .collect_env import collect_env
 from .data_converter_utils import dump_ocr_data, recog_anno_to_imginfo
 from .fileio import (check_integrity, get_md5, is_archive, list_files,
                      list_from_file, list_to_file)
 from .img_utils import crop_img, warp_img
@@ -14,14 +15,15 @@
 from .point_utils import point_distance, points_center
 from .polygon_utils import (boundary_iou, crop_polygon, is_poly_inside_rect,
                             offset_polygon, poly2bbox, poly2shapely,
                             poly_intersection, poly_iou, poly_make_valid,
                             poly_union, polys2shapely, rescale_polygon,
                             rescale_polygons, shapely2poly, sort_points,
                             sort_vertex, sort_vertex8)
+from .processing import track_parallel_progress_multi_args
 from .setup_env import register_all_modules
 from .string_utils import StringStripper
 from .transform_utils import remove_pipeline_elements
 from .typing_utils import (ColorType, ConfigType, DetSampleList,
                            InitConfigType, InstanceList, KIESampleList,
                            LabelList, MultiConfig, OptConfigType,
                            OptDetSampleList, OptInitConfigType,
@@ -43,9 +45,10 @@
     'fill_hole', 'LineJsonParser', 'LineStrParser', 'shapely2poly', 'crop_img',
     'warp_img', 'ConfigType', 'DetSampleList', 'RecForwardResults',
     'InitConfigType', 'OptConfigType', 'OptDetSampleList', 'OptInitConfigType',
     'OptMultiConfig', 'OptRecSampleList', 'RecSampleList', 'MultiConfig',
     'OptTensor', 'ColorType', 'OptKIESampleList', 'KIESampleList',
     'is_archive', 'check_integrity', 'list_files', 'get_md5', 'InstanceList',
     'LabelList', 'OptInstanceList', 'OptLabelList', 'RangeType',
-    'remove_pipeline_elements'
+    'remove_pipeline_elements', 'bezier2poly', 'poly2bezier',
+    'track_parallel_progress_multi_args'
 ]
```

### Comparing `mmocr-1.0.0rc5/mmocr/utils/bbox_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/bbox_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/check_argument.py` & `mmocr-1.0.0rc6/mmocr/utils/check_argument.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/data_converter_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/data_converter_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/fileio.py` & `mmocr-1.0.0rc6/mmocr/utils/fileio.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/img_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/img_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/mask_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/mask_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/parsers.py` & `mmocr-1.0.0rc6/mmocr/utils/parsers.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/point_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/point_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/polygon_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/polygon_utils.py`

 * *Files 4% similar despite different names*

```diff
@@ -44,40 +44,44 @@
     scale_factor = np.array(scale_factor, dtype=float)
     if mode == 'div':
         scale_factor = 1 / scale_factor
     polygon = (reshape_polygon * scale_factor[None]).reshape(poly_shape)
     return polygon
 
 
-def rescale_polygons(polygons: Sequence[ArrayLike],
+def rescale_polygons(polygons: Union[ArrayLike, Sequence[ArrayLike]],
                      scale_factor: Tuple[int, int],
-                     mode: str = 'mul') -> Sequence[np.ndarray]:
+                     mode: str = 'mul'
+                     ) -> Union[ArrayLike, Sequence[np.ndarray]]:
     """Rescale polygons according to scale_factor.
 
     The behavior is different depending on the mode. When mode is 'mul', the
     coordinates will be multiplied by scale_factor, which is usually used in
     preprocessing transforms such as :func:`Resize`.
     The coordinates will be divided by scale_factor if mode is 'div'. It can be
     used in postprocessors to recover the polygon in the original
     image size.
 
     Args:
-        polygons (list[ArrayLike]): A list of polygons, each written in
-            [x1, y1, x2, y2, ...] and in any form can be converted
+        polygons (list[ArrayLike] or ArrayLike): A list of polygons, each
+            written in [x1, y1, x2, y2, ...] and in any form can be converted
             to an 1-D numpy array. E.g. list[list[float]],
             list[np.ndarray], or list[torch.Tensor].
         scale_factor (tuple(int, int)): (w_scale, h_scale).
         model (str): Rescale mode. Can be 'mul' or 'div'. Defaults to 'mul'.
 
     Returns:
-        list[np.ndarray]: Rescaled polygons.
+        list[np.ndarray] or np.ndarray: Rescaled polygons. The type of the
+        return value depends on the type of the input polygons.
     """
     results = []
     for polygon in polygons:
         results.append(rescale_polygon(polygon, scale_factor, mode))
+    if isinstance(polygons, np.ndarray):
+        results = np.array(results)
     return results
 
 
 def poly2bbox(polygon: ArrayLike) -> np.array:
     """Converting a polygon to a bounding box.
 
     Args:
@@ -144,16 +148,16 @@
         polygon (ndarray): polygon in shape (N, ).
         crop_box (ndarray): target box region in shape (4, ).
 
     Returns:
         np.array or None: Cropped polygon. If the polygon is not within the
             crop box, return None.
     """
-    poly = poly2shapely(polygon)
-    crop_poly = poly2shapely(bbox2poly(crop_box))
+    poly = poly_make_valid(poly2shapely(polygon))
+    crop_poly = poly_make_valid(poly2shapely(bbox2poly(crop_box)))
     poly_cropped = poly.intersection(crop_poly)
     if poly_cropped.area == 0. or not isinstance(
             poly_cropped, shapely.geometry.polygon.Polygon):
         # If polygon is outside crop_box region or the intersection is not a
         # polygon, return None.
         return None
     else:
@@ -204,31 +208,34 @@
         return_poly (bool): Whether to return the polygon of the intersection
             Defaults to False.
 
     Returns:
         float or tuple(float, Polygon): Returns the intersection area or
         a tuple ``(area, Optional[poly_obj])``, where the `area` is the
         intersection area between two polygons and `poly_obj` is The Polygon
-        object of the intersection area. Set as `None` if the input is invalid.
-        Set as `None` if the input is invalid. `poly_obj` will be returned
-        only if `return_poly` is `True`.
+        object of the intersection area, which will be `None` if the input is
+        invalid. `poly_obj` will be returned only if `return_poly` is `True`.
     """
     assert isinstance(poly_a, Polygon)
     assert isinstance(poly_b, Polygon)
     assert invalid_ret is None or isinstance(invalid_ret, (float, int))
 
     if invalid_ret is None:
         poly_a = poly_make_valid(poly_a)
         poly_b = poly_make_valid(poly_b)
 
     poly_obj = None
     area = invalid_ret
     if poly_a.is_valid and poly_b.is_valid:
-        poly_obj = poly_a.intersection(poly_b)
-        area = poly_obj.area
+        if poly_a.intersects(poly_b):
+            poly_obj = poly_a.intersection(poly_b)
+            area = poly_obj.area
+        else:
+            poly_obj = Polygon()
+            area = 0.0
     return (area, poly_obj) if return_poly else area
 
 
 def poly_union(
     poly_a: Polygon,
     poly_b: Polygon,
     invalid_ret: Optional[Union[float, int]] = None,
@@ -328,15 +335,15 @@
         return an empty array.
     """
     poly = np.array(poly).reshape(-1, 2)
     pco = pyclipper.PyclipperOffset()
     pco.AddPath(poly, pyclipper.JT_ROUND, pyclipper.ET_CLOSEDPOLYGON)
     # Returned result will be in type of int32, convert it back to float32
     # following MMOCR's convention
-    result = np.array(pco.Execute(distance))
+    result = np.array(pco.Execute(distance), dtype=object)
     if len(result) > 0 and isinstance(result[0], list):
         # The processed polygon has been split into several parts
         result = np.array([])
     result = result.astype(np.float32)
     # Always use the first polygon since only one polygon is expected
     # But when the resulting polygon is invalid, return the empty array
     # as it is
```

### Comparing `mmocr-1.0.0rc5/mmocr/utils/setup_env.py` & `mmocr-1.0.0rc6/mmocr/utils/setup_env.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/string_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/string_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/transform_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/transform_utils.py`

 * *Files identical despite different names*

### Comparing `mmocr-1.0.0rc5/mmocr/utils/typing_utils.py` & `mmocr-1.0.0rc6/mmocr/utils/typing_utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -6,35 +6,37 @@
 import numpy as np
 import torch
 from mmengine.config import ConfigDict
 from mmengine.structures import InstanceData, LabelData
 
 from mmocr import digit_version
 from mmocr.structures import (KIEDataSample, TextDetDataSample,
-                              TextRecogDataSample)
+                              TextRecogDataSample, TextSpottingDataSample)
 
 # Config
 ConfigType = Union[ConfigDict, Dict]
 OptConfigType = Optional[ConfigType]
 MultiConfig = Union[ConfigType, List[ConfigType]]
 OptMultiConfig = Optional[MultiConfig]
 InitConfigType = Union[Dict, List[Dict]]
 OptInitConfigType = Optional[InitConfigType]
 
 # Data
 InstanceList = List[InstanceData]
 OptInstanceList = Optional[InstanceList]
 LabelList = List[LabelData]
 OptLabelList = Optional[LabelList]
+E2ESampleList = List[TextSpottingDataSample]
 RecSampleList = List[TextRecogDataSample]
 DetSampleList = List[TextDetDataSample]
 KIESampleList = List[KIEDataSample]
 OptRecSampleList = Optional[RecSampleList]
 OptDetSampleList = Optional[DetSampleList]
 OptKIESampleList = Optional[KIESampleList]
+OptE2ESampleList = Optional[E2ESampleList]
 
 OptTensor = Optional[torch.Tensor]
 
 RecForwardResults = Union[Dict[str, torch.Tensor], List[TextRecogDataSample],
                           Tuple[torch.Tensor], torch.Tensor]
 
 # Visualization
```

### Comparing `mmocr-1.0.0rc5/mmocr/visualization/base_visualizer.py` & `mmocr-1.0.0rc6/mmocr/visualization/base_visualizer.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import math
-from typing import List, Sequence, Union
+from typing import List, Optional, Sequence, Union
 
 import numpy as np
 import torch
+from matplotlib.font_manager import FontProperties
 from mmengine.visualization import Visualizer
 
 from mmocr.registry import VISUALIZERS
 
 
 @VISUALIZERS.register_module()
 class BaseLocalVisualizer(Visualizer):
@@ -23,14 +24,26 @@
             If it is None, the backend storage will not save any data.
         fig_save_cfg (dict): Keyword parameters of figure for saving.
             Defaults to empty dict.
         fig_show_cfg (dict): Keyword parameters of figure for showing.
             Defaults to empty dict.
         is_openset (bool, optional): Whether the visualizer is used in
             OpenSet. Defaults to False.
+        font_families (Union[str, List[str]]): The font families of labels.
+            Defaults to 'sans-serif'.
+        font_properties (Union[str, FontProperties], optional):
+            The font properties of texts. The format should be a path str
+            to font file or a `font_manager.FontProperties()` object.
+            If you want to draw Chinese texts, you need to prepare
+            a font file that can show Chinese characters properly.
+            For example: `simhei.ttf`,`simsun.ttc`,`simkai.ttf` and so on.
+            Then set font_properties=matplotlib.font_manager.FontProperties
+            (fname='path/to/font_file') or font_properties='path/to/font_file'
+            This function need mmengine version >=0.6.0.
+            Defaults to None.
     """
     PALETTE = [(220, 20, 60), (119, 11, 32), (0, 0, 142), (0, 0, 230),
                (106, 0, 228), (0, 60, 100), (0, 80, 100), (0, 0, 70),
                (0, 0, 192), (250, 170, 30), (100, 170, 30), (220, 220, 0),
                (175, 116, 175), (250, 0, 30), (165, 42, 42), (255, 77, 255),
                (0, 226, 252), (182, 182, 255), (0, 82, 0), (120, 166, 157),
                (110, 76, 0), (174, 57, 255), (199, 100, 0), (72, 0, 118),
@@ -49,27 +62,44 @@
                (127, 167, 115), (59, 105, 106), (142, 108, 45), (196, 172, 0),
                (95, 54, 80), (128, 76, 255), (201, 57, 1), (246, 0, 122),
                (191, 162, 208)]
 
     def __init__(self,
                  name: str = 'visualizer',
                  font_families: Union[str, List[str]] = 'sans-serif',
+                 font_properties: Optional[Union[str, FontProperties]] = None,
                  **kwargs) -> None:
         super().__init__(name=name, **kwargs)
         self.font_families = font_families
+        self.font_properties = self._set_font_properties(font_properties)
 
-    def get_labels_image(self,
-                         image: np.ndarray,
-                         labels: Union[np.ndarray, torch.Tensor],
-                         bboxes: Union[np.ndarray, torch.Tensor],
-                         colors: Union[str, Sequence[str]] = 'k',
-                         font_size: Union[int, float] = 10,
-                         auto_font_size: bool = False,
-                         font_families: Union[str, List[str]] = 'sans-serif'
-                         ) -> np.ndarray:
+    def _set_font_properties(self,
+                             fp: Optional[Union[str, FontProperties]] = None):
+        if fp is None:
+            return None
+        elif isinstance(fp, str):
+            return FontProperties(fname=fp)
+        elif isinstance(fp, FontProperties):
+            return fp
+        else:
+            raise ValueError(
+                'font_properties argument type should be'
+                ' `str` or `matplotlib.font_manager.FontProperties`')
+
+    def get_labels_image(
+        self,
+        image: np.ndarray,
+        labels: Union[np.ndarray, torch.Tensor],
+        bboxes: Union[np.ndarray, torch.Tensor],
+        colors: Union[str, Sequence[str]] = 'k',
+        font_size: Union[int, float] = 10,
+        auto_font_size: bool = False,
+        font_families: Union[str, List[str]] = 'sans-serif',
+        font_properties: Optional[Union[str, FontProperties]] = None
+    ) -> np.ndarray:
         """Draw labels on image.
 
         Args:
             image (np.ndarray): The origin image to draw. The format
                 should be RGB.
             labels (Union[np.ndarray, torch.Tensor]): The labels to draw.
             bboxes (Union[np.ndarray, torch.Tensor]): The bboxes to draw.
@@ -80,15 +110,28 @@
                 formats that are accepted. Defaults to 'k'.
             font_size (Union[int, float]): The font size of labels. Defaults
                 to 10.
             auto_font_size (bool): Whether to automatically adjust font size.
                 Defaults to False.
             font_families (Union[str, List[str]]): The font families of labels.
                 Defaults to 'sans-serif'.
+            font_properties (Union[str, FontProperties], optional):
+                The font properties of texts. The format should be a path str
+                to font file or a `font_manager.FontProperties()` object.
+                If you want to draw Chinese texts, you need to prepare
+                a font file that can show Chinese characters properly.
+                For example: `simhei.ttf`,`simsun.ttc`,`simkai.ttf` and so on.
+                Then set font_properties=matplotlib.font_manager.FontProperties
+                (fname='path/to/font_file') or
+                font_properties='path/to/font_file'.
+                This function need mmengine version >=0.6.0.
+                Defaults to None.
         """
+        if not labels and not bboxes:
+            return image
         if colors is not None and isinstance(colors, (list, tuple)):
             size = math.ceil(len(labels) / len(colors))
             colors = (colors * size)[:len(labels)]
         if auto_font_size:
             assert font_size is not None and isinstance(
                 font_size, (int, float))
             font_size = (bboxes[:, 2:] - bboxes[:, :2]).min(-1) * font_size
@@ -96,15 +139,16 @@
         self.set_image(image)
         self.draw_texts(
             labels, (bboxes[:, :2] + bboxes[:, 2:]) / 2,
             vertical_alignments='center',
             horizontal_alignments='center',
             colors='k',
             font_sizes=font_size,
-            font_families=font_families)
+            font_families=font_families,
+            font_properties=font_properties)
         return self.get_image()
 
     def get_polygons_image(self,
                            image: np.ndarray,
                            polygons: Sequence[np.ndarray],
                            colors: Union[str, Sequence[str]] = 'g',
                            filling: bool = False,
```

### Comparing `mmocr-1.0.0rc5/mmocr/visualization/kie_visualizer.py` & `mmocr-1.0.0rc6/mmocr/visualization/kie_visualizer.py`

 * *Files 11% similar despite different names*

```diff
@@ -86,22 +86,24 @@
         self.set_image(image)
         if key_texts:
             self.draw_texts(
                 key_texts, (bboxes[key_index, :2] + bboxes[key_index, 2:]) / 2,
                 colors='k',
                 horizontal_alignments='center',
                 vertical_alignments='center',
-                font_families=self.font_families)
+                font_families=self.font_families,
+                font_properties=self.font_properties)
         if val_texts:
             self.draw_texts(
                 val_texts, (bboxes[val_index, :2] + bboxes[val_index, 2:]) / 2,
                 colors='k',
                 horizontal_alignments='center',
                 vertical_alignments='center',
-                font_families=self.font_families)
+                font_families=self.font_families,
+                font_properties=self.font_properties)
         self.draw_arrows(
             x_data,
             y_data,
             colors=arrow_colors,
             line_widths=0.3,
             arrow_tail_widths=0.05,
             arrow_head_widths=5,
@@ -149,23 +151,28 @@
             np.ndarray: The image with instances drawn.
         """
         img_shape = image.shape[:2]
         empty_shape = (img_shape[0], img_shape[1], 3)
 
         text_image = np.full(empty_shape, 255, dtype=np.uint8)
         text_image = self.get_labels_image(
-            text_image, texts, bboxes, font_families=self.font_families)
+            text_image,
+            texts,
+            bboxes,
+            font_families=self.font_families,
+            font_properties=self.font_properties)
 
         classes_image = np.full(empty_shape, 255, dtype=np.uint8)
         bbox_classes = [class_names[int(i)]['name'] for i in bbox_labels]
         classes_image = self.get_labels_image(
             classes_image,
             bbox_classes,
             bboxes,
-            font_families=self.font_families)
+            font_families=self.font_families,
+            font_properties=self.font_properties)
         if polygons:
             polygons = [polygon.reshape(-1, 2) for polygon in polygons]
             image = self.get_polygons_image(
                 image, polygons, filling=True, colors=self.PALETTE)
             text_image = self.get_polygons_image(
                 text_image, polygons, colors=self.PALETTE)
             classes_image = self.get_polygons_image(
```

### Comparing `mmocr-1.0.0rc5/mmocr/visualization/textdet_visualizer.py` & `mmocr-1.0.0rc6/mmocr/visualization/textdet_visualizer.py`

 * *Files 14% similar despite different names*

```diff
@@ -26,14 +26,20 @@
             If it is None, the backend storage will not save any data.
         gt_color (Union[str, tuple, list[str], list[tuple]]): The
             colors of GT polygons and bboxes. ``colors`` can have the same
             length with lines or just single value. If ``colors`` is single
             value, all the lines will have the same colors. Refer to
             `matplotlib.colors` for full list of formats that are accepted.
             Defaults to 'g'.
+        gt_ignored_color (Union[str, tuple, list[str], list[tuple]]): The
+            colors of ignored GT polygons and bboxes. ``colors`` can have
+            the same length with lines or just single value. If ``colors``
+            is single value, all the lines will have the same colors. Refer
+            to `matplotlib.colors` for full list of formats that are accepted.
+            Defaults to 'b'.
         pred_color (Union[str, tuple, list[str], list[tuple]]): The
             colors of pred polygons and bboxes. ``colors`` can have the same
             length with lines or just single value. If ``colors`` is single
             value, all the lines will have the same colors. Refer to
             `matplotlib.colors` for full list of formats that are accepted.
             Defaults to 'r'.
         line_width (int, float): The linewidth of lines. Defaults to 2.
@@ -44,25 +50,28 @@
                  name: str = 'visualizer',
                  image: Optional[np.ndarray] = None,
                  with_poly: bool = True,
                  with_bbox: bool = False,
                  vis_backends: Optional[Dict] = None,
                  save_dir: Optional[str] = None,
                  gt_color: Union[str, Tuple, List[str], List[Tuple]] = 'g',
+                 gt_ignored_color: Union[str, Tuple, List[str],
+                                         List[Tuple]] = 'b',
                  pred_color: Union[str, Tuple, List[str], List[Tuple]] = 'r',
                  line_width: Union[int, float] = 2,
                  alpha: float = 0.8) -> None:
         super().__init__(
             name=name,
             image=image,
             vis_backends=vis_backends,
             save_dir=save_dir)
         self.with_poly = with_poly
         self.with_bbox = with_bbox
         self.gt_color = gt_color
+        self.gt_ignored_color = gt_ignored_color
         self.pred_color = pred_color
         self.line_width = line_width
         self.alpha = alpha
 
     def _draw_instances(
         self,
         image: np.ndarray,
@@ -138,17 +147,30 @@
                 and masks. Defaults to 0.3.
             step (int): Global step value to record. Defaults to 0.
         """
         cat_images = []
         if data_sample is not None:
             if draw_gt and 'gt_instances' in data_sample:
                 gt_instances = data_sample.gt_instances
+                gt_img_data = image.copy()
+                if gt_instances.get('ignored', None) is not None:
+                    ignore_flags = gt_instances.ignored
+                    gt_ignored_instances = gt_instances[ignore_flags]
+                    gt_ignored_polygons = gt_ignored_instances.get(
+                        'polygons', None)
+                    gt_ignored_bboxes = gt_ignored_instances.get(
+                        'bboxes', None)
+                    gt_img_data = self._draw_instances(gt_img_data,
+                                                       gt_ignored_bboxes,
+                                                       gt_ignored_polygons,
+                                                       self.gt_ignored_color)
+                    gt_instances = gt_instances[~ignore_flags]
                 gt_polygons = gt_instances.get('polygons', None)
                 gt_bboxes = gt_instances.get('bboxes', None)
-                gt_img_data = self._draw_instances(image.copy(), gt_bboxes,
+                gt_img_data = self._draw_instances(gt_img_data, gt_bboxes,
                                                    gt_polygons, self.gt_color)
                 cat_images.append(gt_img_data)
             if draw_pred and 'pred_instances' in data_sample:
                 pred_instances = data_sample.pred_instances
                 pred_instances = pred_instances[
                     pred_instances.scores > pred_score_thr].cpu()
                 pred_polygons = pred_instances.get('polygons', None)
```

### Comparing `mmocr-1.0.0rc5/mmocr/visualization/textrecog_visualizer.py` & `mmocr-1.0.0rc6/mmocr/visualization/textrecog_visualizer.py`

 * *Files 3% similar despite different names*

```diff
@@ -56,23 +56,24 @@
 
         Returns:
             np.ndarray: The image with text drawn.
         """
         height, width = image.shape[:2]
         empty_img = np.full_like(image, 255)
         self.set_image(empty_img)
-        font_size = 0.5 * width / (len(text) + 1)
+        font_size = min(0.5 * width / (len(text) + 1), 0.5 * height)
         self.draw_texts(
             text,
             np.array([width / 2, height / 2]),
             colors=self.gt_color,
             font_sizes=font_size,
             vertical_alignments='center',
             horizontal_alignments='center',
-            font_families=self.font_families)
+            font_families=self.font_families,
+            font_properties=self.font_properties)
         text_image = self.get_image()
         return text_image
 
     def add_datasample(self,
                        name: str,
                        image: np.ndarray,
                        data_sample: Optional['TextRecogDataSample'] = None,
```

### Comparing `mmocr-1.0.0rc5/mmocr/visualization/textspotting_visualizer.py` & `mmocr-1.0.0rc6/mmocr/visualization/textspotting_visualizer.py`

 * *Files 3% similar despite different names*

```diff
@@ -40,26 +40,28 @@
 
         Returns:
             np.ndarray: The image with instances drawn.
         """
         img_shape = image.shape[:2]
         empty_shape = (img_shape[0], img_shape[1], 3)
         text_image = np.full(empty_shape, 255, dtype=np.uint8)
-        text_image = self.get_labels_image(
-            text_image,
-            labels=texts,
-            bboxes=bboxes,
-            font_families=self.font_families)
+        if texts:
+            text_image = self.get_labels_image(
+                text_image,
+                labels=texts,
+                bboxes=bboxes,
+                font_families=self.font_families,
+                font_properties=self.font_properties)
         if polygons:
             polygons = [polygon.reshape(-1, 2) for polygon in polygons]
             image = self.get_polygons_image(
                 image, polygons, filling=True, colors=self.PALETTE)
             text_image = self.get_polygons_image(
                 text_image, polygons, colors=self.PALETTE)
-        else:
+        elif len(bboxes) > 0:
             image = self.get_bboxes_image(
                 image, bboxes, filling=True, colors=self.PALETTE)
             text_image = self.get_bboxes_image(
                 text_image, bboxes, colors=self.PALETTE)
         return np.concatenate([image, text_image], axis=1)
 
     def add_datasample(self,
@@ -99,35 +101,36 @@
             out_file (str): Path to output file. Defaults to None.
             pred_score_thr (float): The threshold to visualize the bboxes
                 and masks. Defaults to 0.3.
             step (int): Global step value to record. Defaults to 0.
         """
         cat_images = []
 
-        if draw_gt:
-            gt_bboxes = data_sample.gt_instances.get('bboxes', None)
-            gt_texts = data_sample.gt_instances.texts
-            gt_polygons = data_sample.gt_instances.get('polygons', None)
-            gt_img_data = self._draw_instances(image, gt_bboxes, gt_polygons,
-                                               gt_texts)
-            cat_images.append(gt_img_data)
-
-        if draw_pred:
-            pred_instances = data_sample.pred_instances
-            pred_instances = pred_instances[
-                pred_instances.scores > pred_score_thr].cpu().numpy()
-            pred_bboxes = pred_instances.get('bboxes', None)
-            pred_texts = pred_instances.texts
-            pred_polygons = pred_instances.get('polygons', None)
-            if pred_bboxes is None:
-                pred_bboxes = [poly2bbox(poly) for poly in pred_polygons]
-                pred_bboxes = np.array(pred_bboxes)
-            pred_img_data = self._draw_instances(image, pred_bboxes,
-                                                 pred_polygons, pred_texts)
-            cat_images.append(pred_img_data)
+        if data_sample is not None:
+            if draw_gt and 'gt_instances' in data_sample:
+                gt_bboxes = data_sample.gt_instances.get('bboxes', None)
+                gt_texts = data_sample.gt_instances.texts
+                gt_polygons = data_sample.gt_instances.get('polygons', None)
+                gt_img_data = self._draw_instances(image, gt_bboxes,
+                                                   gt_polygons, gt_texts)
+                cat_images.append(gt_img_data)
+
+            if draw_pred and 'pred_instances' in data_sample:
+                pred_instances = data_sample.pred_instances
+                pred_instances = pred_instances[
+                    pred_instances.scores > pred_score_thr].cpu().numpy()
+                pred_bboxes = pred_instances.get('bboxes', None)
+                pred_texts = pred_instances.texts
+                pred_polygons = pred_instances.get('polygons', None)
+                if pred_bboxes is None:
+                    pred_bboxes = [poly2bbox(poly) for poly in pred_polygons]
+                    pred_bboxes = np.array(pred_bboxes)
+                pred_img_data = self._draw_instances(image, pred_bboxes,
+                                                     pred_polygons, pred_texts)
+                cat_images.append(pred_img_data)
 
         cat_images = self._cat_image(cat_images, axis=0)
         if cat_images is None:
             cat_images = image
 
         if show:
             self.show(cat_images, win_name=name, wait_time=wait_time)
```

### Comparing `mmocr-1.0.0rc5/mmocr.egg-info/PKG-INFO` & `mmocr-1.0.0rc6/mmocr.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mmocr
-Version: 1.0.0rc5
+Version: 1.0.0rc6
 Summary: OpenMMLab Text Detection, OCR, and NLP Toolbox
 Home-page: https://github.com/open-mmlab/mmocr
 Maintainer: MMOCR Authors
 Maintainer-email: openmmlab@gmail.com
 License: Apache License 2.0
 Description: <div align="center">
           <img src="resources/mmocr-logo.png" width="500px"/>
@@ -44,14 +44,45 @@
         </div>
         
         <div align="center">
         
         English | [简体中文](README_zh-CN.md)
         
         </div>
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
+        ## Latest Updates
+        
+        **The default branch has been switched to `1.x` from `main`, and we encourage
+        users to migrate to the latest version, though it comes with some cost. Please refer to [Migration Guide](https://mmocr.readthedocs.io/en/dev-1.x/migration/overview.html) for more
+        details.**
+        
+        v1.0.0rc6 was released in 2023-03-07.
+        
+        1. Two new models, ABCNet v2 (inference only) and SPTS are added to `projects/` folder.
+        2. Announcing `Inferencer`, a unified inference interface in OpenMMLab for everyone's easy access and quick inference with all the pre-trained weights. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/inference.html)
+        3. Users can use test-time augmentation for text recognition tasks. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/train_test.html#test-time-augmentation)
+        4. Support [batch augmentation](https://openaccess.thecvf.com/content_CVPR_2020/papers/Hoffer_Augment_Your_Batch_Improving_Generalization_Through_Instance_Repetition_CVPR_2020_paper.pdf) through [`BatchAugSampler`](https://github.com/open-mmlab/mmocr/pull/1757), which is a technique used in SPTS.
+        5. Dataset Preparer has been refactored to allow more flexible configurations. Besides, users are now able to prepare text recognition datasets in LMDB formats. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/dataset_preparer.html#lmdb-format)
+        6. Some textspotting datasets have been revised to enhance the correctness and consistency with the common practice.
+        7. Potential spurious warnings from `shapely` have been eliminated.
+        
+        Read [Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for more details!
         
         ## Introduction
         
         MMOCR is an open-source toolbox based on PyTorch and mmdetection for text detection, text recognition, and the corresponding downstream tasks including key information extraction. It is part of the [OpenMMLab](https://openmmlab.com/) project.
         
         The main branch works with **PyTorch 1.6+**.
         
@@ -73,25 +104,14 @@
         
           The modular design of MMOCR enables users to define their own optimizers, data preprocessors, and model components such as backbones, necks and heads as well as losses. Please refer to [Overview](https://mmocr.readthedocs.io/en/dev-1.x/get_started/overview.html) for how to construct a customized model.
         
         - **Numerous Utilities**
         
           The toolbox provides a comprehensive set of utilities which can help users assess the performance of models. It includes visualizers which allow visualization of images, ground truths as well as predicted bounding boxes, and a validation tool for evaluating checkpoints during training.  It also includes data converters to demonstrate how to convert your own data to the annotation files which the toolbox supports.
         
-        ## Latest Updates
-        
-        v1.0.0rc5 was released in 2023-01-06.
-        
-        1. Two models, Aster and SVTR, are added to our model zoo. The full implementation of ABCNet is also available now.
-        2. Dataset Preparer supports 5 more datasets: CocoTextV2, FUNSD, TextOCR, NAF, SROIE.
-        3. We have 4 more text recognition transforms, and two more helper transforms.
-        4. The transform, `FixInvalidPolygon`, is getting smarter at dealing with invalid polygons, and now capable of handling more weird annotations. As a result, a complete training cycle on TotalText dataset can be performed bug-free. The weights of DBNet and FCENet pretrained on TotalText are also released.
-        
-        Read [Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for more details!
-        
         ## What's New in MMOCR 1.0
         
         1. **New engines**. MMOCR 1.x is based on [MMEngine](https://github.com/open-mmlab/mmengine), which provides a general and powerful runner that allows more flexible customizations and significantly simplifies the entrypoints of high-level interfaces.
         
         2. **Unified interfaces**. As a part of the OpenMMLab 2.0 projects, MMOCR 1.x unifies and refactors the interfaces and internal logics of train, testing, datasets, models, evaluation, and visualization. All the OpenMMLab 2.0 projects share the same design in those interfaces and logics to allow the emergence of multi-task/modality algorithms.
         
         3. **Cross project calling**. Benefiting from the unified design, you can use the models implemented in other OpenMMLab projects, such as MMDet. We provide an example of how to use MMDetection's Mask R-CNN through `MMDetWrapper`. Check our documents for more details. More wrappers will be released in the future.
@@ -175,14 +195,16 @@
         
         </details>
         
         <details open>
         <summary>Text Spotting</summary>
         
         - [x] [ABCNet](projects/ABCNet/README.md) (CVPR'2020)
+        - [x] [ABCNetV2](projects/ABCNet/README_V2.md) (TPAMI'2021)
+        - [x] [SPTS](projects/SPTS/README.md) (ACM MM'2022)
         
         </details>
         
         Please refer to [model_zoo](https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more details.
         
         ## Contributing
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: mmocr Version: 1.0.0rc5 Summary: OpenMMLab Text
+Metadata-Version: 2.1 Name: mmocr Version: 1.0.0rc6 Summary: OpenMMLab Text
 Detection, OCR, and NLP Toolbox Home-page: https://github.com/open-mmlab/mmocr
 Maintainer: MMOCR Authors Maintainer-email: openmmlab@gmail.com License: Apache
 License 2.0 Description:
                           [resources/mmocr-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
@@ -21,19 +21,41 @@
  2.amazonaws.com/assets/try_on_tiyaro_badge.svg] [ðDocumentation](https://
       mmocr.readthedocs.io/en/dev-1.x/) | [ð ï¸Installation](https://
   mmocr.readthedocs.io/en/dev-1.x/get_started/install.html) | [ðModel Zoo]
   (https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) | [ðUpdate News]
 (https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) | [ð¤Reporting
         Issues](https://github.com/open-mmlab/mmocr/issues/new/choose)
                    English | [ç®ä½ä¸­æ](README_zh-CN.md)
-## Introduction MMOCR is an open-source toolbox based on PyTorch and
-mmdetection for text detection, text recognition, and the corresponding
-downstream tasks including key information extraction. It is part of the
-[OpenMMLab](https://openmmlab.com/) project. The main branch works with
-**PyTorch 1.6+**.
+
+## Latest Updates **The default branch has been switched to `1.x` from `main`,
+and we encourage users to migrate to the latest version, though it comes with
+some cost. Please refer to [Migration Guide](https://mmocr.readthedocs.io/en/
+dev-1.x/migration/overview.html) for more details.** v1.0.0rc6 was released in
+2023-03-07. 1. Two new models, ABCNet v2 (inference only) and SPTS are added to
+`projects/` folder. 2. Announcing `Inferencer`, a unified inference interface
+in OpenMMLab for everyone's easy access and quick inference with all the pre-
+trained weights. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/
+inference.html) 3. Users can use test-time augmentation for text recognition
+tasks. [Docs](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/
+train_test.html#test-time-augmentation) 4. Support [batch augmentation](https:/
+/openaccess.thecvf.com/content_CVPR_2020/papers/
+Hoffer_Augment_Your_Batch_Improving_Generalization_Through_Instance_Repetition_CVPR_2020_paper.pdf)
+through [`BatchAugSampler`](https://github.com/open-mmlab/mmocr/pull/1757),
+which is a technique used in SPTS. 5. Dataset Preparer has been refactored to
+allow more flexible configurations. Besides, users are now able to prepare text
+recognition datasets in LMDB formats. [Docs](https://mmocr.readthedocs.io/en/
+dev-1.x/user_guides/data_prepare/dataset_preparer.html#lmdb-format) 6. Some
+textspotting datasets have been revised to enhance the correctness and
+consistency with the common practice. 7. Potential spurious warnings from
+`shapely` have been eliminated. Read [Changelog](https://mmocr.readthedocs.io/
+en/dev-1.x/notes/changelog.html) for more details! ## Introduction MMOCR is an
+open-source toolbox based on PyTorch and mmdetection for text detection, text
+recognition, and the corresponding downstream tasks including key information
+extraction. It is part of the [OpenMMLab](https://openmmlab.com/) project. The
+main branch works with **PyTorch 1.6+**.
  [https://user-images.githubusercontent.com/24622904/187838618-1fdc61c0-2d46-
                           49f9-8502-976ffdf01f28.png]
 ### Major Features - **Comprehensive Pipeline** The toolbox supports not only
 text detection and text recognition, but also their downstream tasks such as
 key information extraction. - **Multiple Models** The toolbox supports a wide
 variety of state-of-the-art models for text detection, text recognition and key
 information extraction. - **Modular Design** The modular design of MMOCR
@@ -42,44 +64,35 @@
 to [Overview](https://mmocr.readthedocs.io/en/dev-1.x/get_started/
 overview.html) for how to construct a customized model. - **Numerous
 Utilities** The toolbox provides a comprehensive set of utilities which can
 help users assess the performance of models. It includes visualizers which
 allow visualization of images, ground truths as well as predicted bounding
 boxes, and a validation tool for evaluating checkpoints during training. It
 also includes data converters to demonstrate how to convert your own data to
-the annotation files which the toolbox supports. ## Latest Updates v1.0.0rc5
-was released in 2023-01-06. 1. Two models, Aster and SVTR, are added to our
-model zoo. The full implementation of ABCNet is also available now. 2. Dataset
-Preparer supports 5 more datasets: CocoTextV2, FUNSD, TextOCR, NAF, SROIE. 3.
-We have 4 more text recognition transforms, and two more helper transforms. 4.
-The transform, `FixInvalidPolygon`, is getting smarter at dealing with invalid
-polygons, and now capable of handling more weird annotations. As a result, a
-complete training cycle on TotalText dataset can be performed bug-free. The
-weights of DBNet and FCENet pretrained on TotalText are also released. Read
-[Changelog](https://mmocr.readthedocs.io/en/dev-1.x/notes/changelog.html) for
-more details! ## What's New in MMOCR 1.0 1. **New engines**. MMOCR 1.x is based
-on [MMEngine](https://github.com/open-mmlab/mmengine), which provides a general
-and powerful runner that allows more flexible customizations and significantly
-simplifies the entrypoints of high-level interfaces. 2. **Unified interfaces**.
-As a part of the OpenMMLab 2.0 projects, MMOCR 1.x unifies and refactors the
-interfaces and internal logics of train, testing, datasets, models, evaluation,
-and visualization. All the OpenMMLab 2.0 projects share the same design in
-those interfaces and logics to allow the emergence of multi-task/modality
-algorithms. 3. **Cross project calling**. Benefiting from the unified design,
-you can use the models implemented in other OpenMMLab projects, such as MMDet.
-We provide an example of how to use MMDetection's Mask R-CNN through
-`MMDetWrapper`. Check our documents for more details. More wrappers will be
-released in the future. 4. **Stronger visualization**. We provide a series of
-useful tools which are mostly based on brand-new visualizers. As a result, it
-is more convenient for the users to explore the models and datasets now. 5.
-**More documentation and tutorials**. We add a bunch of documentation and
-tutorials to help users get started more smoothly. Read it [here](https://
-mmocr.readthedocs.io/en/dev-1.x/). 6. **One-stop Dataset Preparaion**. Multiple
-datasets are instantly ready with only one line of command, via our [Dataset
-Preparer](https://mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/
+the annotation files which the toolbox supports. ## What's New in MMOCR 1.0 1.
+**New engines**. MMOCR 1.x is based on [MMEngine](https://github.com/open-
+mmlab/mmengine), which provides a general and powerful runner that allows more
+flexible customizations and significantly simplifies the entrypoints of high-
+level interfaces. 2. **Unified interfaces**. As a part of the OpenMMLab 2.0
+projects, MMOCR 1.x unifies and refactors the interfaces and internal logics of
+train, testing, datasets, models, evaluation, and visualization. All the
+OpenMMLab 2.0 projects share the same design in those interfaces and logics to
+allow the emergence of multi-task/modality algorithms. 3. **Cross project
+calling**. Benefiting from the unified design, you can use the models
+implemented in other OpenMMLab projects, such as MMDet. We provide an example
+of how to use MMDetection's Mask R-CNN through `MMDetWrapper`. Check our
+documents for more details. More wrappers will be released in the future. 4.
+**Stronger visualization**. We provide a series of useful tools which are
+mostly based on brand-new visualizers. As a result, it is more convenient for
+the users to explore the models and datasets now. 5. **More documentation and
+tutorials**. We add a bunch of documentation and tutorials to help users get
+started more smoothly. Read it [here](https://mmocr.readthedocs.io/en/dev-1.x/
+). 6. **One-stop Dataset Preparaion**. Multiple datasets are instantly ready
+with only one line of command, via our [Dataset Preparer](https://
+mmocr.readthedocs.io/en/dev-1.x/user_guides/data_prepare/
 dataset_preparer.html). 7. **Embracing more `projects/`**: We now introduce
 `projects/` folder, where some experimental features, frameworks and models can
 be placed, only needed to satisfy the minimum requirement on the code quality.
 Everyone is welcome to post their implementation of any great ideas in this
 folder! Learn more from our [example project](https://github.com/open-mmlab/
 mmocr/blob/dev-1.x/projects/example_project/). 8. **More models**. MMOCR 1.0
 supports more tasks and more state-of-the-art models! ## Installation MMOCR
@@ -109,66 +122,68 @@
 README.md) (PR'2021) - [x] [NRTR](configs/textrecog/nrtr/README.md)
 (ICDAR'2019) - [x] [RobustScanner](configs/textrecog/robust_scanner/README.md)
 (ECCV'2020) - [x] [SAR](configs/textrecog/sar/README.md) (AAAI'2019) - [x]
 [SATRN](configs/textrecog/satrn/README.md) (CVPR'2020 Workshop on Text and
 Documents in the Deep Learning Era) - [x] [SVTR](configs/textrecog/svtr/
 README.md) (IJCAI'2022)   Key Information Extraction - [x] [SDMG-R](configs/
 kie/sdmgr/README.md) (ArXiv'2021)   Text Spotting - [x] [ABCNet](projects/
-ABCNet/README.md) (CVPR'2020)  Please refer to [model_zoo](https://
-mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more details. ##
-Contributing We appreciate all contributions to improve MMOCR. Please refer to
-[CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guidelines. ##
-Acknowledgement MMOCR is an open-source project that is contributed by
-researchers and engineers from various colleges and companies. We appreciate
-all the contributors who implement their methods or add new features, as well
-as users who give valuable feedbacks. We hope the toolbox and benchmark could
-serve the growing research community by providing a flexible toolkit to
-reimplement existing methods and develop their own new OCR methods. ## Citation
-If you find this project useful in your research, please consider cite:
-```bibtex @article{mmocr2021, title={MMOCR: A Comprehensive Toolbox for Text
-Detection, Recognition and Understanding}, author={Kuang, Zhanghui and Sun,
-Hongbin and Li, Zhizhong and Yue, Xiaoyu and Lin, Tsui Hin and Chen, Jianyong
-and Wei, Huaqiang and Zhu, Yiqin and Gao, Tong and Zhang, Wenwei and Chen, Kai
-and Zhang, Wayne and Lin, Dahua}, journal= {arXiv preprint arXiv:2108.06543},
-year={2021} } ``` ## License This project is released under the [Apache 2.0
-license](LICENSE). ## Projects in OpenMMLab - [MMEngine](https://github.com/
-open-mmlab/mmengine): OpenMMLab foundational library for training deep learning
-models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational
-library for computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM
-installs OpenMMLab packages. - [MMClassification](https://github.com/open-
-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
-- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
-toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
-mmdetection3d): OpenMMLab's next-generation platform for general 3D object
-detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
-rotated object detection toolbox and benchmark. - [MMSegmentation](https://
-github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox
-and benchmark. - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text
-detection, recognition, and understanding toolbox. - [MMPose](https://
-github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
-- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human
-parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/open-
-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark. -
-[MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression
-toolbox and benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot):
-OpenMMLab fewshot learning toolbox and benchmark. - [MMAction2](https://
-github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action
-understanding toolbox and benchmark. - [MMTracking](https://github.com/open-
-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark. - [MMFlow]
-(https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and
-benchmark. - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab
-image and video editing toolbox. - [MMGeneration](https://github.com/open-
-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox. -
-[MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment
-framework. ## Welcome to the OpenMMLab community Scan the QR code below to
-follow the OpenMMLab team's [**Zhihu Official Account**](https://www.zhihu.com/
-people/openmmlab) and join the OpenMMLab team's [**QQ Group**](https://
-jq.qq.com/?_wv=1027&k=aCvMxdr3), or join the official communication WeChat
-group by adding the WeChat, or join our [**Slack**](https://join.slack.com/t/
-mmocrworkspace/shared_invite/zt-1ifqhfla8-yKnLO_aKhVA2h71OrK8GZw)
+ABCNet/README.md) (CVPR'2020) - [x] [ABCNetV2](projects/ABCNet/README_V2.md)
+(TPAMI'2021) - [x] [SPTS](projects/SPTS/README.md) (ACM MM'2022)  Please refer
+to [model_zoo](https://mmocr.readthedocs.io/en/dev-1.x/modelzoo.html) for more
+details. ## Contributing We appreciate all contributions to improve MMOCR.
+Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing
+guidelines. ## Acknowledgement MMOCR is an open-source project that is
+contributed by researchers and engineers from various colleges and companies.
+We appreciate all the contributors who implement their methods or add new
+features, as well as users who give valuable feedbacks. We hope the toolbox and
+benchmark could serve the growing research community by providing a flexible
+toolkit to reimplement existing methods and develop their own new OCR methods.
+## Citation If you find this project useful in your research, please consider
+cite: ```bibtex @article{mmocr2021, title={MMOCR: A Comprehensive Toolbox for
+Text Detection, Recognition and Understanding}, author={Kuang, Zhanghui and
+Sun, Hongbin and Li, Zhizhong and Yue, Xiaoyu and Lin, Tsui Hin and Chen,
+Jianyong and Wei, Huaqiang and Zhu, Yiqin and Gao, Tong and Zhang, Wenwei and
+Chen, Kai and Zhang, Wayne and Lin, Dahua}, journal= {arXiv preprint arXiv:
+2108.06543}, year={2021} } ``` ## License This project is released under the
+[Apache 2.0 license](LICENSE). ## Projects in OpenMMLab - [MMEngine](https://
+github.com/open-mmlab/mmengine): OpenMMLab foundational library for training
+deep learning models - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab
+foundational library for computer vision. - [MIM](https://github.com/open-
+mmlab/mim): MIM installs OpenMMLab packages. - [MMClassification](https://
+github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox
+and benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection):
+OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
+github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for
+general 3D object detection. - [MMRotate](https://github.com/open-mmlab/
+mmrotate): OpenMMLab rotated object detection toolbox and benchmark. -
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
+model deployment framework. ## Welcome to the OpenMMLab community Scan the QR
+code below to follow the OpenMMLab team's [**Zhihu Official Account**](https://
+www.zhihu.com/people/openmmlab) and join the OpenMMLab team's [**QQ Group**]
+(https://jq.qq.com/?_wv=1027&k=aCvMxdr3), or join the official communication
+WeChat group by adding the WeChat, or join our [**Slack**](https://
+join.slack.com/t/mmocrworkspace/shared_invite/zt-1ifqhfla8-
+yKnLO_aKhVA2h71OrK8GZw)
   [https://raw.githubusercontent.com/open-mmlab/mmcv/master/docs/en/_static/
  zhihu_qrcode.jpg] [https://raw.githubusercontent.com/open-mmlab/mmcv/master/
  docs/en/_static/qq_group_qrcode.jpg] [https://raw.githubusercontent.com/open-
              mmlab/mmcv/master/docs/en/_static/wechat_qrcode.jpg]
 We will provide you with the OpenMMLab community - ð¢ share the latest core
 technologies of AI frameworks - ð» Explaining PyTorch common module source
 Code - ð° News related to the release of OpenMMLab - ð Introduction of
```

### Comparing `mmocr-1.0.0rc5/mmocr.egg-info/SOURCES.txt` & `mmocr-1.0.0rc6/mmocr.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 MANIFEST.in
 README.md
 setup.cfg
 setup.py
 mmocr/__init__.py
-mmocr/ocr.py
 mmocr/registry.py
 mmocr/version.py
 mmocr.egg-info/PKG-INFO
 mmocr.egg-info/SOURCES.txt
 mmocr.egg-info/dependency_links.txt
 mmocr.egg-info/not-zip-safe
 mmocr.egg-info/requires.txt
@@ -21,14 +20,15 @@
 mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_novisual.py
 mmocr/.mim/configs/kie/sdmgr/_base_sdmgr_unet16.py
 mmocr/.mim/configs/kie/sdmgr/metafile.yml
 mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt-openset.py
 mmocr/.mim/configs/kie/sdmgr/sdmgr_novisual_60e_wildreceipt.py
 mmocr/.mim/configs/kie/sdmgr/sdmgr_unet16_60e_wildreceipt.py
 mmocr/.mim/configs/textdet/_base_/default_runtime.py
+mmocr/.mim/configs/textdet/_base_/pretrain_runtime.py
 mmocr/.mim/configs/textdet/_base_/datasets/ctw1500.py
 mmocr/.mim/configs/textdet/_base_/datasets/icdar2015.py
 mmocr/.mim/configs/textdet/_base_/datasets/icdar2017.py
 mmocr/.mim/configs/textdet/_base_/datasets/synthtext.py
 mmocr/.mim/configs/textdet/_base_/datasets/totaltext.py
 mmocr/.mim/configs/textdet/_base_/datasets/toy_data.py
 mmocr/.mim/configs/textdet/_base_/schedules/schedule_adam_600e.py
@@ -145,14 +145,15 @@
 mmocr/.mim/configs/textrecog/svtr/metafile.yml
 mmocr/.mim/configs/textrecog/svtr/svtr-base_20e_st_mj.py
 mmocr/.mim/configs/textrecog/svtr/svtr-large_20e_st_mj.py
 mmocr/.mim/configs/textrecog/svtr/svtr-small_20e_st_mj.py
 mmocr/.mim/configs/textrecog/svtr/svtr-tiny_20e_st_mj.py
 mmocr/.mim/tools/dist_test.sh
 mmocr/.mim/tools/dist_train.sh
+mmocr/.mim/tools/infer.py
 mmocr/.mim/tools/slurm_test.sh
 mmocr/.mim/tools/slurm_train.sh
 mmocr/.mim/tools/test.py
 mmocr/.mim/tools/train.py
 mmocr/.mim/tools/analysis_tools/browse_dataset.py
 mmocr/.mim/tools/analysis_tools/get_flops.py
 mmocr/.mim/tools/analysis_tools/offline_eval.py
@@ -212,44 +213,64 @@
 mmocr/.mim/tools/dataset_converters/textrecog/synthtext_converter.py
 mmocr/.mim/tools/dataset_converters/textrecog/textocr_converter.py
 mmocr/.mim/tools/dataset_converters/textrecog/totaltext_converter.py
 mmocr/.mim/tools/dataset_converters/textrecog/vintext_converter.py
 mmocr/.mim/tools/model_converters/publish_model.py
 mmocr/apis/__init__.py
 mmocr/apis/inferencers/__init__.py
-mmocr/apis/inferencers/base_inferencer.py
 mmocr/apis/inferencers/base_mmocr_inferencer.py
 mmocr/apis/inferencers/kie_inferencer.py
 mmocr/apis/inferencers/mmocr_inferencer.py
 mmocr/apis/inferencers/textdet_inferencer.py
 mmocr/apis/inferencers/textrec_inferencer.py
+mmocr/apis/inferencers/textspot_inferencer.py
 mmocr/datasets/__init__.py
 mmocr/datasets/dataset_wrapper.py
 mmocr/datasets/icdar_dataset.py
 mmocr/datasets/ocr_dataset.py
 mmocr/datasets/recog_lmdb_dataset.py
 mmocr/datasets/recog_text_dataset.py
 mmocr/datasets/wildreceipt_dataset.py
 mmocr/datasets/preparers/__init__.py
-mmocr/datasets/preparers/config_generator.py
-mmocr/datasets/preparers/data_converter.py
-mmocr/datasets/preparers/data_obtainer.py
 mmocr/datasets/preparers/data_preparer.py
+mmocr/datasets/preparers/config_generators/__init__.py
+mmocr/datasets/preparers/config_generators/base.py
+mmocr/datasets/preparers/config_generators/textdet_config_generator.py
+mmocr/datasets/preparers/config_generators/textrecog_config_generator.py
+mmocr/datasets/preparers/config_generators/textspotting_config_generator.py
 mmocr/datasets/preparers/dumpers/__init__.py
-mmocr/datasets/preparers/dumpers/dumpers.py
+mmocr/datasets/preparers/dumpers/base.py
+mmocr/datasets/preparers/dumpers/json_dumper.py
+mmocr/datasets/preparers/dumpers/lmdb_dumper.py
+mmocr/datasets/preparers/dumpers/wild_receipt_openset_dumper.py
+mmocr/datasets/preparers/gatherers/__init__.py
+mmocr/datasets/preparers/gatherers/base.py
+mmocr/datasets/preparers/gatherers/mono_gatherer.py
+mmocr/datasets/preparers/gatherers/naf_gatherer.py
+mmocr/datasets/preparers/gatherers/pair_gatherer.py
+mmocr/datasets/preparers/obtainers/__init__.py
+mmocr/datasets/preparers/obtainers/naive_data_obtainer.py
+mmocr/datasets/preparers/packers/__init__.py
+mmocr/datasets/preparers/packers/base.py
+mmocr/datasets/preparers/packers/textdet_packer.py
+mmocr/datasets/preparers/packers/textrecog_packer.py
+mmocr/datasets/preparers/packers/textspotting_packer.py
+mmocr/datasets/preparers/packers/wildreceipt_packer.py
 mmocr/datasets/preparers/parsers/__init__.py
 mmocr/datasets/preparers/parsers/base.py
 mmocr/datasets/preparers/parsers/coco_parser.py
 mmocr/datasets/preparers/parsers/funsd_parser.py
 mmocr/datasets/preparers/parsers/icdar_txt_parser.py
 mmocr/datasets/preparers/parsers/naf_parser.py
 mmocr/datasets/preparers/parsers/sroie_parser.py
 mmocr/datasets/preparers/parsers/svt_parser.py
 mmocr/datasets/preparers/parsers/totaltext_parser.py
 mmocr/datasets/preparers/parsers/wildreceipt_parser.py
+mmocr/datasets/samplers/__init__.py
+mmocr/datasets/samplers/batch_aug.py
 mmocr/datasets/transforms/__init__.py
 mmocr/datasets/transforms/adapters.py
 mmocr/datasets/transforms/formatting.py
 mmocr/datasets/transforms/loading.py
 mmocr/datasets/transforms/ocr_transforms.py
 mmocr/datasets/transforms/textdet_transforms.py
 mmocr/datasets/transforms/textrecog_transforms.py
@@ -394,14 +415,15 @@
 mmocr/models/textrecog/preprocessors/tps_preprocessor.py
 mmocr/models/textrecog/recognizers/__init__.py
 mmocr/models/textrecog/recognizers/abinet.py
 mmocr/models/textrecog/recognizers/aster.py
 mmocr/models/textrecog/recognizers/base.py
 mmocr/models/textrecog/recognizers/crnn.py
 mmocr/models/textrecog/recognizers/encoder_decoder_recognizer.py
+mmocr/models/textrecog/recognizers/encoder_decoder_recognizer_tta.py
 mmocr/models/textrecog/recognizers/master.py
 mmocr/models/textrecog/recognizers/nrtr.py
 mmocr/models/textrecog/recognizers/robust_scanner.py
 mmocr/models/textrecog/recognizers/sar.py
 mmocr/models/textrecog/recognizers/satrn.py
 mmocr/models/textrecog/recognizers/svtr.py
 mmocr/structures/__init__.py
@@ -409,23 +431,25 @@
 mmocr/structures/textdet_data_sample.py
 mmocr/structures/textrecog_data_sample.py
 mmocr/structures/textspotting_data_sample.py
 mmocr/testing/__init__.py
 mmocr/testing/data.py
 mmocr/utils/__init__.py
 mmocr/utils/bbox_utils.py
+mmocr/utils/bezier_utils.py
 mmocr/utils/check_argument.py
 mmocr/utils/collect_env.py
 mmocr/utils/data_converter_utils.py
 mmocr/utils/fileio.py
 mmocr/utils/img_utils.py
 mmocr/utils/mask_utils.py
 mmocr/utils/parsers.py
 mmocr/utils/point_utils.py
 mmocr/utils/polygon_utils.py
+mmocr/utils/processing.py
 mmocr/utils/setup_env.py
 mmocr/utils/string_utils.py
 mmocr/utils/transform_utils.py
 mmocr/utils/typing_utils.py
 mmocr/visualization/__init__.py
 mmocr/visualization/base_visualizer.py
 mmocr/visualization/kie_visualizer.py
```

### Comparing `mmocr-1.0.0rc5/mmocr.egg-info/requires.txt` & `mmocr-1.0.0rc6/mmocr.egg-info/requires.txt`

 * *Files 2% similar despite different names*

```diff
@@ -39,17 +39,17 @@
 
 [build]
 numpy
 pyclipper
 torch>=1.1
 
 [mim]
-mmcv<2.1.0,>==2.0.0rc1
-mmdet<3.1.0,>=3.0.0rc0
-mmengine<1.0.0,>=0.1.0
+mmcv<2.1.0,>==2.0.0rc4
+mmdet<3.1.0,>=3.0.0rc5
+mmengine<1.0.0,>=0.6.0
 
 [optional]
 
 [tests]
 asynctest
 codecov
 flake8
```

### Comparing `mmocr-1.0.0rc5/setup.cfg` & `mmocr-1.0.0rc6/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 split_penalty_after_opening_bracket = 800
 
 [isort]
 line_length = 79
 multi_line_output = 0
 extra_standard_library = setuptools
 known_first_party = mmocr
-known_third_party = PIL,cv2,imgaug,lanms,lmdb,matplotlib,mmcv,mmdet,numpy,packaging,pyclipper,pytest,pytorch_sphinx_theme,rapidfuzz,requests,scipy,shapely,skimage,titlecase,torch,torchvision,ts,yaml
+known_third_party = PIL,cv2,imgaug,lanms,lmdb,matplotlib,mmcv,mmdet,numpy,packaging,pyclipper,pytest,pytorch_sphinx_theme,rapidfuzz,requests,scipy,shapely,skimage,titlecase,torch,torchvision,ts,yaml,mmengine
 no_lines_before = STDLIB,LOCALFOLDER
 default_section = THIRDPARTY
 
 [style]
 based_on_style = pep8
 blank_line_before_nested_class_or_def = true
 split_before_expression_after_opening_paren = true
```

### Comparing `mmocr-1.0.0rc5/setup.py` & `mmocr-1.0.0rc6/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -31,15 +31,15 @@
     elif 'sdist' in sys.argv or 'bdist_wheel' in sys.argv:
         # installed by `pip install .`
         # or create source distribution by `python setup.py sdist`
         mode = 'copy'
     else:
         return
 
-    filenames = ['tools', 'configs', 'model-index.yml']
+    filenames = ['tools', 'configs', 'model-index.yml', 'dicts']
     repo_path = osp.dirname(__file__)
     mim_path = osp.join(repo_path, 'mmocr', '.mim')
     os.makedirs(mim_path, exist_ok=True)
 
     for filename in filenames:
         if osp.exists(filename):
             src_path = osp.join(repo_path, filename)
```

