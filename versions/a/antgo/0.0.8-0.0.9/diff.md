# Comparing `tmp/antgo-0.0.8.tar.gz` & `tmp/antgo-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "antgo-0.0.8.tar", last modified: Wed Sep  1 12:47:48 2021, max compression
+gzip compressed data, was "antgo-0.0.9.tar", last modified: Thu Sep  2 15:55:47 2021, max compression
```

## Comparing `antgo-0.0.8.tar` & `antgo-0.0.9.tar`

### file list

```diff
@@ -1,260 +1,260 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.068114 antgo-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:09.000000 antgo-0.0.8/LICENSE.md
--rwxr-xr-x   0 runner    (1001) docker     (121)      837 2021-09-01 12:47:09.000000 antgo-0.0.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     6073 2021-09-01 12:47:48.068114 antgo-0.0.8/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (121)     4480 2021-09-01 12:47:09.000000 antgo-0.0.8/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.028113 antgo-0.0.8/antgo/
--rwxr-xr-x   0 runner    (1001) docker     (121)      159 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.028113 antgo-0.0.8/antgo/activelearning/
--rw-r--r--   0 runner    (1001) docker     (121)      229 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/activelearning/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.028113 antgo-0.0.8/antgo/activelearning/samplingmethods/
--rw-r--r--   0 runner    (1001) docker     (121)      229 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/activelearning/samplingmethods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3948 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/activelearning/samplingmethods/kcenter_greedy.py
--rw-r--r--   0 runner    (1001) docker     (121)     1008 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/activelearning/samplingmethods/sampling_def.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.028113 antgo-0.0.8/antgo/annotation/
--rwxr-xr-x   0 runner    (1001) docker     (121)      185 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/annotation/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      952 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/annotation/image_tool.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.032113 antgo-0.0.8/antgo/ant/
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    20356 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/activelearning.py
--rw-r--r--   0 runner    (1001) docker     (121)     2891 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/activelearning_api.py
--rw-r--r--   0 runner    (1001) docker     (121)      290 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/analysis.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    12759 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/base.py
--rw-r--r--   0 runner    (1001) docker     (121)    10684 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/batch.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    12412 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/browser.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    28575 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/challenge.py
--rw-r--r--   0 runner    (1001) docker     (121)     3221 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/debug.py
--rw-r--r--   0 runner    (1001) docker     (121)     6661 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/demo.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4162 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/flags.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2445 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/generate.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    56640 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/train.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1697 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/utils.py
--rw-r--r--   0 runner    (1001) docker     (121)     3866 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/warehouse.py
--rw-r--r--   0 runner    (1001) docker     (121)     7232 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/ant/watch.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.032113 antgo-0.0.8/antgo/codebook/
--rwxr-xr-x   0 runner    (1001) docker     (121)      220 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.032113 antgo-0.0.8/antgo/codebook/tf/
--rwxr-xr-x   0 runner    (1001) docker     (121)      221 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2921 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/dataset.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2392 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/layers.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     7136 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/preprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)    18001 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/stublayers.py
--rw-r--r--   0 runner    (1001) docker     (121)    10150 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/tftool_records.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     7809 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/codebook/tf/tftools.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1711 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/config.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      203 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/config.xml
--rwxr-xr-x   0 runner    (1001) docker     (121)     7713 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/context.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.032113 antgo-0.0.8/antgo/crowdsource/
--rwxr-xr-x   0 runner    (1001) docker     (121)      206 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     9216 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/activelearning_server.py
--rw-r--r--   0 runner    (1001) docker     (121)     3125 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/base_server.py
--rw-r--r--   0 runner    (1001) docker     (121)     9086 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/batch_server.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    18437 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/browser_server.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     6412 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/crowdsource_server.py
--rw-r--r--   0 runner    (1001) docker     (121)    24566 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/demo_server.py
--rw-r--r--   0 runner    (1001) docker     (121)      776 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/utils.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     8053 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/crowdsource/watch_server.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.032113 antgo-0.0.8/antgo/cutils/
--rwxr-xr-x   0 runner    (1001) docker     (121)     8249 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/cutils/maskApi.c
--rwxr-xr-x   0 runner    (1001) docker     (121)     2176 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/cutils/maskApi.h
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.032113 antgo-0.0.8/antgo/dataflow/
--rwxr-xr-x   0 runner    (1001) docker     (121)       80 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     5217 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/basic.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    23094 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/common.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    14025 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/core.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.036113 antgo-0.0.8/antgo/dataflow/dataset/
--rwxr-xr-x   0 runner    (1001) docker     (121)     1700 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4058 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/ade20k.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    14996 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/celeba.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     6271 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/cifar.py
--rw-r--r--   0 runner    (1001) docker     (121)    28849 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/coco2017.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    26259 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/dataset.py
--rw-r--r--   0 runner    (1001) docker     (121)      612 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/empty_dataset.py
--rw-r--r--   0 runner    (1001) docker     (121)     6942 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/fashionai_attribute.py
--rw-r--r--   0 runner    (1001) docker     (121)    10135 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/fashionai_landmark.py
--rw-r--r--   0 runner    (1001) docker     (121)     2787 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/flic.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3139 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/horse2zebra.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     9018 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/ilsvrc.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3083 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/iphone2dslr.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     9328 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/lfw.py
--rw-r--r--   0 runner    (1001) docker     (121)     4784 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/lip.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     5680 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/mnist.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3725 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/omniglot.py
--rw-r--r--   0 runner    (1001) docker     (121)     3040 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/parallel_read.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    15883 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/pascal_voc.py
--rw-r--r--   0 runner    (1001) docker     (121)     3517 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/queue_dataset.py
--rw-r--r--   0 runner    (1001) docker     (121)      965 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/random_dataset.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4030 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/simplecsvs.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4465 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/simpleimages.py
--rw-r--r--   0 runner    (1001) docker     (121)     2135 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/simplevideos.py
--rw-r--r--   0 runner    (1001) docker     (121)     7863 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/spider_dataset.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     5891 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/standard.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2970 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/svhn.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     5963 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/dataset/vggface.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.036113 antgo-0.0.8/antgo/dataflow/datasynth/
--rwxr-xr-x   0 runner    (1001) docker     (121)      199 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/datasynth/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.036113 antgo-0.0.8/antgo/dataflow/imgaug/
--rwxr-xr-x   0 runner    (1001) docker     (121)       99 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/imgaug/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4516 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/imgaug/distorted.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3810 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/imgaug/grid.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    10813 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/imgaug/regular.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    20292 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/dataflow/recorder.py
--rw-r--r--   0 runner    (1001) docker     (121)     6229 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/jupytercontext.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    18113 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/main.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.040113 antgo-0.0.8/antgo/measures/
--rwxr-xr-x   0 runner    (1001) docker     (121)     2500 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2608 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/ali_fashion_attribute_error.py
--rw-r--r--   0 runner    (1001) docker     (121)     2955 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/ali_fashion_landmark_ne.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     5903 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/average_precision.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1104 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/base.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4744 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/binary_c.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1554 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/binomial_deviance.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2060 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/confusion_matrix.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    21500 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/crowdsource.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     9036 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/deep_analysis.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     6339 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/error.py
--rw-r--r--   0 runner    (1001) docker     (121)     4166 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/face_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1985 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/kdd_average_precision.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3456 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/matting_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      766 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/moving_statistic.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4826 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/multi_c.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4348 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/multic_task.py
--rw-r--r--   0 runner    (1001) docker     (121)     3724 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/multil_task.py
--rw-r--r--   0 runner    (1001) docker     (121)      226 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/normalized_error.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    45355 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/objdect_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2826 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/pck.py
--rw-r--r--   0 runner    (1001) docker     (121)     2721 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/person_search_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     6784 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/precision_recall.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     8696 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/quadratic_weighted_kappa.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2438 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/regression_metric.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2765 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/regression_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    13252 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/repeat_statistic.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      192 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/retrieval_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     5448 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/roc_auc.py
--rw-r--r--   0 runner    (1001) docker     (121)     6160 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/segmentation_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3467 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/significance.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     7540 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/statistic.py
--rw-r--r--   0 runner    (1001) docker     (121)     9577 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/track_task.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4010 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/measures/yesno_crowdsource.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.040113 antgo-0.0.8/antgo/resource/
--rwxr-xr-x   0 runner    (1001) docker     (121)      200 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.040113 antgo-0.0.8/antgo/resource/batch/
--rw-r--r--   0 runner    (1001) docker     (121)      507 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/index.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.024113 antgo-0.0.8/antgo/resource/batch/static/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.040113 antgo-0.0.8/antgo/resource/batch/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)   229435 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css
--rw-r--r--   0 runner    (1001) docker     (121)   335620 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css.map
--rw-r--r--   0 runner    (1001) docker     (121)    28613 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/css/style.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.044113 antgo-0.0.8/antgo/resource/batch/static/fonts/
--rw-r--r--   0 runner    (1001) docker     (121)   165742 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.674f50d.eot
--rw-r--r--   0 runner    (1001) docker     (121)    77160 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.af7ae50.woff2
--rw-r--r--   0 runner    (1001) docker     (121)   165548 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.b06871f.ttf
--rw-r--r--   0 runner    (1001) docker     (121)    98024 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.fee66e7.woff
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.044113 antgo-0.0.8/antgo/resource/batch/static/img/
--rw-r--r--   0 runner    (1001) docker     (121)     3836 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/img/banner-rank.png
--rw-r--r--   0 runner    (1001) docker     (121)   444379 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/img/fontawesome-webfont.912ec66.svg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.044113 antgo-0.0.8/antgo/resource/batch/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)     7569 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js
--rw-r--r--   0 runner    (1001) docker     (121)    31625 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js.map
--rw-r--r--   0 runner    (1001) docker     (121)      857 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js
--rw-r--r--   0 runner    (1001) docker     (121)     4972 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js.map
--rw-r--r--   0 runner    (1001) docker     (121)  1097514 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js
--rw-r--r--   0 runner    (1001) docker     (121)  3691685 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js.map
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.048113 antgo-0.0.8/antgo/resource/browser/
--rw-r--r--   0 runner    (1001) docker     (121)      514 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/index.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.048113 antgo-0.0.8/antgo/resource/browser/static/
--rw-r--r--   0 runner    (1001) docker     (121)       28 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/config.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.052113 antgo-0.0.8/antgo/resource/browser/static/css/
--rw-r--r--   0 runner    (1001) docker     (121)   229858 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css
--rw-r--r--   0 runner    (1001) docker     (121)   336251 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css.map
--rw-r--r--   0 runner    (1001) docker     (121)    28613 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/css/style.css
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.052113 antgo-0.0.8/antgo/resource/browser/static/fonts/
--rw-r--r--   0 runner    (1001) docker     (121)   165742 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.674f50d.eot
--rw-r--r--   0 runner    (1001) docker     (121)    77160 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.af7ae50.woff2
--rw-r--r--   0 runner    (1001) docker     (121)   165548 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.b06871f.ttf
--rw-r--r--   0 runner    (1001) docker     (121)    98024 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.fee66e7.woff
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.052113 antgo-0.0.8/antgo/resource/browser/static/img/
--rw-r--r--   0 runner    (1001) docker     (121)   444379 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/img/fontawesome-webfont.912ec66.svg
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.052113 antgo-0.0.8/antgo/resource/browser/static/js/
--rw-r--r--   0 runner    (1001) docker     (121)    13831 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js
--rw-r--r--   0 runner    (1001) docker     (121)    58155 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js.map
--rw-r--r--   0 runner    (1001) docker     (121)      857 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js
--rw-r--r--   0 runner    (1001) docker     (121)     4972 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js.map
--rw-r--r--   0 runner    (1001) docker     (121)  1125837 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js
--rw-r--r--   0 runner    (1001) docker     (121)  3815723 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js.map
--rwxr-xr-x   0 runner    (1001) docker     (121)    23363 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/html.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.060114 antgo-0.0.8/antgo/resource/static/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/antgo.css
--rwxr-xr-x   0 runner    (1001) docker     (121)     9662 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/antgo.ico
--rw-r--r--   0 runner    (1001) docker     (121)     8758 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/antgo.js
--rw-r--r--   0 runner    (1001) docker     (121)   292973 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/banner.png
--rw-r--r--   0 runner    (1001) docker     (121)    32806 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/card.png
--rwxr-xr-x   0 runner    (1001) docker     (121)       42 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/crowdsource.js
--rw-r--r--   0 runner    (1001) docker     (121)    32294 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/holder.min.js
--rw-r--r--   0 runner    (1001) docker     (121)   106186 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/static/register.png
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.060114 antgo-0.0.8/antgo/resource/templates/
--rw-r--r--   0 runner    (1001) docker     (121)     5159 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/activelearning.html
--rwxr-xr-x   0 runner    (1001) docker     (121)    16328 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/crowdsource.html
--rw-r--r--   0 runner    (1001) docker     (121)    22276 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/demo.html
--rwxr-xr-x   0 runner    (1001) docker     (121)    61982 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/statistic-report.html
--rw-r--r--   0 runner    (1001) docker     (121)      459 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/task.template
--rw-r--r--   0 runner    (1001) docker     (121)    18210 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/task_main_file.template
--rw-r--r--   0 runner    (1001) docker     (121)      675 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/task_main_param.template
--rw-r--r--   0 runner    (1001) docker     (121)     1348 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/task_shell.template
--rw-r--r--   0 runner    (1001) docker     (121)    30333 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/trainmaster.html
--rw-r--r--   0 runner    (1001) docker     (121)      130 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/trainworker.html
--rwxr-xr-x   0 runner    (1001) docker     (121)     1867 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/resource/templates/yesno_crowdsource.html
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.060114 antgo-0.0.8/antgo/sandbox/
--rwxr-xr-x   0 runner    (1001) docker     (121)      220 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/sandbox/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2542 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/sandbox/sandbox.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.060114 antgo-0.0.8/antgo/task/
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/task/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    11930 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/task/task.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.060114 antgo-0.0.8/antgo/trainer/
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/trainer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    30786 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/trainer/tfgantrainer.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    24441 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/trainer/tfmodel_deploy.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    36436 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/trainer/tftrainer.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     8991 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/trainer/trainer.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.068114 antgo-0.0.8/antgo/utils/
--rwxr-xr-x   0 runner    (1001) docker     (121)      402 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)   273187 2021-09-01 12:47:46.000000 antgo-0.0.8/antgo/utils/_bbox.c
--rwxr-xr-x   0 runner    (1001) docker     (121)     1756 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/_bbox.pyx
--rwxr-xr-x   0 runner    (1001) docker     (121)      614 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/_encode_png.pyx
--rw-r--r--   0 runner    (1001) docker     (121)   643525 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo/utils/_mask.c
--rwxr-xr-x   0 runner    (1001) docker     (121)    11418 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/_mask.pyx
--rw-r--r--   0 runner    (1001) docker     (121)   303393 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo/utils/_nms.c
--rwxr-xr-x   0 runner    (1001) docker     (121)     2237 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/_nms.pyx
--rw-r--r--   0 runner    (1001) docker     (121)   376934 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo/utils/_resize.c
--rwxr-xr-x   0 runner    (1001) docker     (121)     8133 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/_resize.pyx
--rwxr-xr-x   0 runner    (1001) docker     (121)     1150 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/argscope.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     8104 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/concurrency.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1887 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/cpu.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    12823 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/dht.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1242 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/encode.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3628 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/fs.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2915 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/gpu.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4076 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/logger.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     4553 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/mask.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     9588 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/netvis.py
--rw-r--r--   0 runner    (1001) docker     (121)     9007 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/pickledb.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1487 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/processbar.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     1285 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/serialize.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.068114 antgo-0.0.8/antgo/utils/shared_queue/
--rwxr-xr-x   0 runner    (1001) docker     (121)      992 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/shared_queue/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3131 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/shared_queue/queue.py
--rwxr-xr-x   0 runner    (1001) docker     (121)    17513 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/shared_queue/sharedmemory.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     2079 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/timer.py
--rwxr-xr-x   0 runner    (1001) docker     (121)     3959 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/utils/utils.py
--rwxr-xr-x   0 runner    (1001) docker     (121)      163 2021-09-01 12:47:09.000000 antgo-0.0.8/antgo/version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:48.028113 antgo-0.0.8/antgo.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     6073 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     7667 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       43 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)        6 2021-09-01 12:47:47.000000 antgo-0.0.8/antgo.egg-info/top_level.txt
--rwxr-xr-x   0 runner    (1001) docker     (121)      215 2021-09-01 12:47:09.000000 antgo-0.0.8/requirements.txt
--rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-01 12:47:09.000000 antgo-0.0.8/roadmap.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-09-01 12:47:48.068114 antgo-0.0.8/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (121)     3117 2021-09-01 12:47:09.000000 antgo-0.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.734447 antgo-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:06.000000 antgo-0.0.9/LICENSE.md
+-rwxr-xr-x   0 runner    (1001) docker     (121)      837 2021-09-02 15:55:06.000000 antgo-0.0.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     6073 2021-09-02 15:55:47.734447 antgo-0.0.9/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4480 2021-09-02 15:55:06.000000 antgo-0.0.9/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.690446 antgo-0.0.9/antgo/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      159 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.690446 antgo-0.0.9/antgo/activelearning/
+-rw-r--r--   0 runner    (1001) docker     (121)      229 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/activelearning/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.690446 antgo-0.0.9/antgo/activelearning/samplingmethods/
+-rw-r--r--   0 runner    (1001) docker     (121)      229 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/activelearning/samplingmethods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3948 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/activelearning/samplingmethods/kcenter_greedy.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1008 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/activelearning/samplingmethods/sampling_def.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.690446 antgo-0.0.9/antgo/annotation/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      185 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/annotation/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      952 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/annotation/image_tool.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.694447 antgo-0.0.9/antgo/ant/
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    20777 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/activelearning.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2891 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/activelearning_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)      290 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/analysis.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    12719 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10888 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/batch.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    12428 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/browser.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    28627 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/challenge.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3237 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/debug.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6677 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/demo.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4162 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/flags.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2445 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/generate.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    56967 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/train.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1697 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3866 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/warehouse.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7232 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/ant/watch.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.694447 antgo-0.0.9/antgo/codebook/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      220 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.694447 antgo-0.0.9/antgo/codebook/tf/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      221 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2921 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/dataset.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2392 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/layers.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     7136 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/preprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18001 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/stublayers.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10150 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/tftool_records.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     7809 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/codebook/tf/tftools.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1711 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/config.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      236 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/config.xml
+-rwxr-xr-x   0 runner    (1001) docker     (121)     7713 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/context.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.694447 antgo-0.0.9/antgo/crowdsource/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      206 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9216 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/activelearning_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3125 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/base_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9086 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/batch_server.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    18437 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/browser_server.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     6412 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/crowdsource_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24566 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/demo_server.py
+-rw-r--r--   0 runner    (1001) docker     (121)      776 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/utils.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     8053 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/crowdsource/watch_server.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.698447 antgo-0.0.9/antgo/cutils/
+-rwxr-xr-x   0 runner    (1001) docker     (121)     8249 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/cutils/maskApi.c
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2176 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/cutils/maskApi.h
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.698447 antgo-0.0.9/antgo/dataflow/
+-rwxr-xr-x   0 runner    (1001) docker     (121)       80 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     5217 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/basic.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    23094 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/common.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    14025 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/core.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.702447 antgo-0.0.9/antgo/dataflow/dataset/
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1700 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4058 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/ade20k.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    14996 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/celeba.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     6271 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/cifar.py
+-rw-r--r--   0 runner    (1001) docker     (121)    28849 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/coco2017.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    26764 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/dataset.py
+-rw-r--r--   0 runner    (1001) docker     (121)      612 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/empty_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6942 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/fashionai_attribute.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10135 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/fashionai_landmark.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2787 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/flic.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3139 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/horse2zebra.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     9018 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/ilsvrc.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3083 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/iphone2dslr.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     9328 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/lfw.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4784 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/lip.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     5680 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/mnist.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3725 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/omniglot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3040 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/parallel_read.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    15883 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/pascal_voc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3517 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/queue_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (121)      965 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/random_dataset.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4030 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/simplecsvs.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4465 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/simpleimages.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2135 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/simplevideos.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7863 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/spider_dataset.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     5891 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/standard.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2970 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/svhn.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     5963 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/dataset/vggface.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.702447 antgo-0.0.9/antgo/dataflow/datasynth/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      199 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/datasynth/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.702447 antgo-0.0.9/antgo/dataflow/imgaug/
+-rwxr-xr-x   0 runner    (1001) docker     (121)       99 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/imgaug/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4516 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/imgaug/distorted.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3810 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/imgaug/grid.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    10813 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/imgaug/regular.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    20292 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/dataflow/recorder.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6229 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/jupytercontext.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    19101 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/main.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.706447 antgo-0.0.9/antgo/measures/
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2500 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2608 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/ali_fashion_attribute_error.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2955 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/ali_fashion_landmark_ne.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     5903 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/average_precision.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1104 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/base.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4744 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/binary_c.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1554 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/binomial_deviance.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2060 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/confusion_matrix.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    21500 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/crowdsource.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     9036 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/deep_analysis.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     6339 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/error.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4166 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/face_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1985 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/kdd_average_precision.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3456 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/matting_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      766 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/moving_statistic.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4826 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/multi_c.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4348 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/multic_task.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3724 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/multil_task.py
+-rw-r--r--   0 runner    (1001) docker     (121)      226 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/normalized_error.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    45355 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/objdect_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2826 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/pck.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2721 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/person_search_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     6784 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/precision_recall.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     8696 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/quadratic_weighted_kappa.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2438 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/regression_metric.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2765 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/regression_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    13252 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/repeat_statistic.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      192 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/retrieval_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     5448 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/roc_auc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6160 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/segmentation_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3467 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/significance.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     7540 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/statistic.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9577 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/track_task.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4010 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/measures/yesno_crowdsource.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.706447 antgo-0.0.9/antgo/resource/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      200 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.706447 antgo-0.0.9/antgo/resource/batch/
+-rw-r--r--   0 runner    (1001) docker     (121)      507 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/index.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.686447 antgo-0.0.9/antgo/resource/batch/static/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.706447 antgo-0.0.9/antgo/resource/batch/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)   229435 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css
+-rw-r--r--   0 runner    (1001) docker     (121)   335620 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css.map
+-rw-r--r--   0 runner    (1001) docker     (121)    28613 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/css/style.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.706447 antgo-0.0.9/antgo/resource/batch/static/fonts/
+-rw-r--r--   0 runner    (1001) docker     (121)   165742 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.674f50d.eot
+-rw-r--r--   0 runner    (1001) docker     (121)    77160 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.af7ae50.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)   165548 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.b06871f.ttf
+-rw-r--r--   0 runner    (1001) docker     (121)    98024 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.fee66e7.woff
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.706447 antgo-0.0.9/antgo/resource/batch/static/img/
+-rw-r--r--   0 runner    (1001) docker     (121)     3836 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/img/banner-rank.png
+-rw-r--r--   0 runner    (1001) docker     (121)   444379 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/img/fontawesome-webfont.912ec66.svg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.710447 antgo-0.0.9/antgo/resource/batch/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)     7569 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js
+-rw-r--r--   0 runner    (1001) docker     (121)    31625 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)      857 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js
+-rw-r--r--   0 runner    (1001) docker     (121)     4972 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)  1097514 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js
+-rw-r--r--   0 runner    (1001) docker     (121)  3691685 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js.map
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.714447 antgo-0.0.9/antgo/resource/browser/
+-rw-r--r--   0 runner    (1001) docker     (121)      514 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/index.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.714447 antgo-0.0.9/antgo/resource/browser/static/
+-rw-r--r--   0 runner    (1001) docker     (121)       28 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/config.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.714447 antgo-0.0.9/antgo/resource/browser/static/css/
+-rw-r--r--   0 runner    (1001) docker     (121)   229858 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css
+-rw-r--r--   0 runner    (1001) docker     (121)   336251 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css.map
+-rw-r--r--   0 runner    (1001) docker     (121)    28613 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/css/style.css
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.718447 antgo-0.0.9/antgo/resource/browser/static/fonts/
+-rw-r--r--   0 runner    (1001) docker     (121)   165742 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.674f50d.eot
+-rw-r--r--   0 runner    (1001) docker     (121)    77160 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.af7ae50.woff2
+-rw-r--r--   0 runner    (1001) docker     (121)   165548 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.b06871f.ttf
+-rw-r--r--   0 runner    (1001) docker     (121)    98024 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.fee66e7.woff
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.718447 antgo-0.0.9/antgo/resource/browser/static/img/
+-rw-r--r--   0 runner    (1001) docker     (121)   444379 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/img/fontawesome-webfont.912ec66.svg
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.722447 antgo-0.0.9/antgo/resource/browser/static/js/
+-rw-r--r--   0 runner    (1001) docker     (121)    13831 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js
+-rw-r--r--   0 runner    (1001) docker     (121)    58155 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)      857 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js
+-rw-r--r--   0 runner    (1001) docker     (121)     4972 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js.map
+-rw-r--r--   0 runner    (1001) docker     (121)  1125837 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js
+-rw-r--r--   0 runner    (1001) docker     (121)  3815723 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js.map
+-rwxr-xr-x   0 runner    (1001) docker     (121)    23363 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/html.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.726447 antgo-0.0.9/antgo/resource/static/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/antgo.css
+-rwxr-xr-x   0 runner    (1001) docker     (121)     9662 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/antgo.ico
+-rw-r--r--   0 runner    (1001) docker     (121)     8758 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/antgo.js
+-rw-r--r--   0 runner    (1001) docker     (121)   292973 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/banner.png
+-rw-r--r--   0 runner    (1001) docker     (121)    32806 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/card.png
+-rwxr-xr-x   0 runner    (1001) docker     (121)       42 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/crowdsource.js
+-rw-r--r--   0 runner    (1001) docker     (121)    32294 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/holder.min.js
+-rw-r--r--   0 runner    (1001) docker     (121)   106186 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/static/register.png
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.730447 antgo-0.0.9/antgo/resource/templates/
+-rw-r--r--   0 runner    (1001) docker     (121)     5159 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/activelearning.html
+-rwxr-xr-x   0 runner    (1001) docker     (121)    16328 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/crowdsource.html
+-rw-r--r--   0 runner    (1001) docker     (121)    22276 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/demo.html
+-rwxr-xr-x   0 runner    (1001) docker     (121)    61982 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/statistic-report.html
+-rw-r--r--   0 runner    (1001) docker     (121)      459 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/task.template
+-rw-r--r--   0 runner    (1001) docker     (121)    18273 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/task_main_file.template
+-rw-r--r--   0 runner    (1001) docker     (121)      675 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/task_main_param.template
+-rw-r--r--   0 runner    (1001) docker     (121)     1348 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/task_shell.template
+-rw-r--r--   0 runner    (1001) docker     (121)    30333 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/trainmaster.html
+-rw-r--r--   0 runner    (1001) docker     (121)      130 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/trainworker.html
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1867 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/resource/templates/yesno_crowdsource.html
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.730447 antgo-0.0.9/antgo/sandbox/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      220 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/sandbox/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2542 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/sandbox/sandbox.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.730447 antgo-0.0.9/antgo/task/
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/task/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    12009 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/task/task.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.730447 antgo-0.0.9/antgo/trainer/
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/trainer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30786 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/trainer/tfgantrainer.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    24441 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/trainer/tfmodel_deploy.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    36436 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/trainer/tftrainer.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     8991 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/trainer/trainer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.734447 antgo-0.0.9/antgo/utils/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      402 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)   273187 2021-09-02 15:55:46.000000 antgo-0.0.9/antgo/utils/_bbox.c
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1756 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/_bbox.pyx
+-rwxr-xr-x   0 runner    (1001) docker     (121)      614 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/_encode_png.pyx
+-rw-r--r--   0 runner    (1001) docker     (121)   643525 2021-09-02 15:55:46.000000 antgo-0.0.9/antgo/utils/_mask.c
+-rwxr-xr-x   0 runner    (1001) docker     (121)    11418 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/_mask.pyx
+-rw-r--r--   0 runner    (1001) docker     (121)   303393 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo/utils/_nms.c
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2237 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/_nms.pyx
+-rw-r--r--   0 runner    (1001) docker     (121)   376934 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo/utils/_resize.c
+-rwxr-xr-x   0 runner    (1001) docker     (121)     8133 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/_resize.pyx
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1150 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/argscope.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     8104 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/concurrency.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1887 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/cpu.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    12823 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/dht.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1242 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/encode.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3628 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/fs.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2915 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/gpu.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4076 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/logger.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     4553 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/mask.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     9588 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/netvis.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9007 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/pickledb.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1487 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/processbar.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     1285 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/serialize.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.734447 antgo-0.0.9/antgo/utils/shared_queue/
+-rwxr-xr-x   0 runner    (1001) docker     (121)      992 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/shared_queue/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3131 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/shared_queue/queue.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)    17513 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/shared_queue/sharedmemory.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     2079 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/timer.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3959 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/utils/utils.py
+-rwxr-xr-x   0 runner    (1001) docker     (121)      163 2021-09-02 15:55:06.000000 antgo-0.0.9/antgo/version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:47.690446 antgo-0.0.9/antgo.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     6073 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     7667 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       43 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)        6 2021-09-02 15:55:47.000000 antgo-0.0.9/antgo.egg-info/top_level.txt
+-rwxr-xr-x   0 runner    (1001) docker     (121)      215 2021-09-02 15:55:06.000000 antgo-0.0.9/requirements.txt
+-rwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-09-02 15:55:06.000000 antgo-0.0.9/roadmap.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2021-09-02 15:55:47.734447 antgo-0.0.9/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (121)     3117 2021-09-02 15:55:06.000000 antgo-0.0.9/setup.py
```

### Comparing `antgo-0.0.8/MANIFEST.in` & `antgo-0.0.9/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/PKG-INFO` & `antgo-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.0
 Name: antgo
-Version: 0.0.8
+Version: 0.0.9
 Summary: machine learning experiment platform
 Home-page: https://github.com/jianzfb/antgo
 Author: jian
 Author-email: jian@mltalker.com
 License: UNKNOWN
 Description: ======================
         Antgo
```

### Comparing `antgo-0.0.8/README.rst` & `antgo-0.0.9/README.rst`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/activelearning/samplingmethods/kcenter_greedy.py` & `antgo-0.0.9/antgo/activelearning/samplingmethods/kcenter_greedy.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/activelearning/samplingmethods/sampling_def.py` & `antgo-0.0.9/antgo/activelearning/samplingmethods/sampling_def.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/annotation/image_tool.py` & `antgo-0.0.9/antgo/annotation/image_tool.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/ant/activelearning.py` & `antgo-0.0.9/antgo/ant/activelearning.py`

 * *Files 3% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 from antgo.crowdsource.activelearning_server import *
 from antgo.dataflow.common import *
 from antgo.dataflow.recorder import *
 from antvis.client.httprpc import *
 from multiprocessing import Process, Queue
 from antgo.task.task import *
 from scipy.stats import entropy
+import traceback
 import subprocess
 import os
 import socket
 import requests
 import json
 import zipfile
 
@@ -61,15 +62,15 @@
                ant_dump_dir,
                ant_token,
                ant_task_config=None,
                **kwargs):
     super(AntActiveLearning, self).__init__(ant_name, ant_context, ant_token, **kwargs)
 
     self.skip_first_training = self.context.params.system['skip_training']
-    self.max_iterators = getattr(self.context.params, 'max_iterators', 100)
+    self.max_iterators = self.context.params.activelearning.get('max_iterators', 100)
     if self.max_iterators is None:
       self.max_iterators = 100
 
     self.dump_dir = ant_dump_dir
     self.web_server_port = self.context.params.system['port']
     self.web_server_port = int(self.web_server_port) if self.web_server_port is not None else None
     self.html_template = kwargs.get('html_template', None)
@@ -103,15 +104,15 @@
   def _unform_sampling_algorithm(self, unlabeled_pool, num):
     if num > len(unlabeled_pool):
       return unlabeled_pool
     
     return np.random.choice(unlabeled_pool, num, False)
 
   def _waiting_label_sample_select(self, unlabeled_pool, num):
-    sampling_strategy = getattr(self.context.params, 'sampling_strategy', 'entropy')
+    sampling_strategy = self.context.params.activelearning.get('sampling_strategy', 'entropy')
     if sampling_strategy == 'coreset':
       return self._core_set_algorithm(unlabeled_pool, num)
     elif sampling_strategy == 'entropy':
       return self._entroy_algorithm(unlabeled_pool, num)
     elif sampling_strategy == 'random':
       return self._unform_sampling_algorithm(unlabeled_pool, num)
     else:
@@ -159,17 +160,16 @@
     # 配置html模板信息
     self.keywords_template['TASK_TITLE'] = running_ant_task.task_name
     self.keywords_template['TASK_TYPE'] = running_ant_task.task_type
     self.keywords_template['UNLABELED_NUM'] = 0
     self.keywords_template['LABEL_COMPLEX'] = 0
 
     # dataset
-    dataset = running_ant_task.dataset('train',
-                                       os.path.join(self.ant_data_source, running_ant_task.dataset_name),
-                                       running_ant_task.dataset_params)
+    dataset = \
+        running_ant_task.dataset('unlabel',os.path.join(self.ant_data_source, running_ant_task.dataset_name), running_ant_task.dataset_params)
 
     # prepare workspace
     if not os.path.exists(os.path.join(self.main_folder, 'web', 'static', 'data')):
       os.makedirs(os.path.join(self.main_folder, 'web', 'static', 'data'))
 
     annotation_folder = os.path.join(self.main_folder, 'web', 'static', 'data', 'annotations')
     if not os.path.exists(annotation_folder):
@@ -218,15 +218,15 @@
     # prepare waiting unlabeled data
     try_iter = 0
     experiment_id = None
     while try_iter < self.max_iterators:
       unlabeled_dataset_size = dataset.unlabeled_size()
       labeled_dataset_size = dataset.candidates_size()
 
-      min_sampling_num = getattr(self.context.params, 'min_sampling_num', None)
+      min_sampling_num = self.context.params.activelearning.get('min_sampling_num', None)
       if min_sampling_num is not None:
         min_sampling_num = (int)(min_sampling_num)
         if unlabeled_dataset_size < min_sampling_num:
           logger.info('Active learning is over. (unlabeled sample size < %d).'%min_sampling_num)
           return
 
       if unlabeled_dataset_size < 10:
@@ -246,27 +246,28 @@
       analyze_start_time = time.time()
       if try_iter == 0:
         experiment_id = self.context.from_experiment
 
       if (not self.skip_first_training or try_iter > 0) and labeled_dataset_size > 0:
         # shell call
         logger.info('Start training using all labeled data (%d iter).'%try_iter)
+
         if os.path.exists(os.path.join(self.dump_dir, 'try_round_train_%d'%try_iter)):
           shutil.rmtree(os.path.join(self.dump_dir, 'try_round_train_%d'%try_iter))
         os.makedirs(os.path.join(self.dump_dir, 'try_round_train_%d'%try_iter))
 
         cmd_shell = 'antgo train --main_file=%s --main_param=%s' % (self.main_file, self.main_param)
         cmd_shell += ' --dump=%s/%s' % (self.dump_dir, 'try_round_train_%d'%try_iter)
         cmd_shell += ' --main_folder=%s' % self.main_folder
         cmd_shell += ' --task=%s' % self.ant_task_config.split('/')[-1]
         if experiment_id is not None:
           cmd_shell += ' --from_experiment=%s' % experiment_id
         cmd_shell += ' --devices=%s' % self.devices
         cmd_shell += ' --dataset=%s' % running_ant_task.dataset_name
-        cmd_shell += ' --name=%s' % self.ant_name
+        cmd_shell += ' --name=%s_train_round_%d' % (self.ant_name, try_iter)
         training_p = \
             subprocess.Popen('%s > %s.log' % (cmd_shell, '%s_try_rounnd_train_%d'%(self.name, try_iter)), 
                               shell=True, 
                               cwd=self.main_folder)
 
         # waiting untile finish training
         training_p.wait()
@@ -296,19 +297,19 @@
 
       logger.info('Start analyze all unlabeled data distribution (%d iter).'%try_iter)
       cmd_shell = 'antgo predict --main_file=%s --main_param=%s'%(self.main_file, self.main_param)
       cmd_shell += ' --main_folder=%s' % self.main_folder
       cmd_shell += ' --dump=%s/%s' % (self.dump_dir, 'try_round_analyze_%d'%try_iter)
       if experiment_id is not None:
         cmd_shell += ' --from_experiment=%s' % experiment_id
-      cmd_shell += ' --task=%s' % self.ant_task_config.split('/')[-1]
+      cmd_shell += ' --task_t=%s' % running_ant_task.task_type
       cmd_shell += ' --unlabel'
       cmd_shell += ' --devices=%s' % self.devices
-      cmd_shell += ' --dataset=%s' % running_ant_task.dataset_name
-      cmd_shell += ' --name=%s' % self.ant_name
+      cmd_shell += ' --dataset=%s/unlabel' % running_ant_task.dataset_name
+      cmd_shell += ' --name=%s_predict_round_%d' % (self.ant_name, try_iter)
       inference_p = subprocess.Popen('%s > %s.log' %(cmd_shell, '%s_try_rounnd_analyze_%d'%(self.name, try_iter)), 
                                       shell=True, 
                                       cwd=self.main_folder)
 
       # waiting untile finish inference
       inference_p.wait()
 
@@ -330,17 +331,17 @@
       
       record_reader = RecordReader(os.path.join(self.dump_dir, inference_experiment_prefix, inference_experiment_id, 'record'))
       unlabeled_pool = []
       for ss in record_reader.iterate_read('groundtruth', 'predict'):
         gt, feature = ss
         unlabeled_pool.append({'file_id': gt['file_id'], 'feature': feature, 'id': gt['id']})
 
-      select_size = getattr(self.context.params, 'min_sampling_num', None)
+      select_size = self.context.params.activelearning.get('min_sampling_num', None)
       if select_size is None:
-        min_sampling_ratio = getattr(self.context.params, 'min_sampling_ratio', None)
+        min_sampling_ratio = self.context.params.activelearning.get('min_sampling_ratio', None)
         if min_sampling_ratio is None:
           min_sampling_ratio = 0.1
         select_size = int(len(unlabeled_pool) * min_sampling_ratio)
         if select_size == 0:
           select_size = len(unlabeled_pool)
 
       if select_size == 0:
@@ -348,15 +349,15 @@
         return
 
       next_selected = self._waiting_label_sample_select(unlabeled_pool, select_size)
       if len(next_selected) == 0:
         logger.info("Active learning is over. (selecting size == 0).")
         return
 
-      logger.info("Round %d, selecting size %d by %s method."%(try_iter, select_size, getattr(self.context.params, 'sampling_strategy', 'entropy')))
+      logger.info("Round %d, selecting size %d by %s method."%(try_iter, select_size, self.context.params.activelearning.get('sampling_strategy', 'entropy')))
 
       # 结束分析时间
       analyze_end_time = time.time()
 
       # 获得平均分析时间
       avg_analyze_time = (avg_analyze_time * try_iter + (analyze_end_time - analyze_start_time)) / (try_iter + 1)
 
@@ -368,27 +369,33 @@
       tar_file = "round_%d.tar.gz"%try_iter
       tar_path = os.path.join(download_folder, tar_file)
       if os.path.exists(tar_path):
         os.remove(tar_path)
 
       tar = tarfile.open(tar_path, "w:gz")
       for next_unlabeled_sample_id, _ in next_unlabeled_sample_ids:
-        tar.add(os.path.join(dataset.unlabeled_folder, next_unlabeled_sample_id),
+        tar.add(os.path.join(dataset.dir, next_unlabeled_sample_id),
                 arcname="round_%d/%s"%(try_iter,next_unlabeled_sample_id))
       tar.close()
 
       # 研究模式，在研究模式下，标注结果自动获取
       if self.context.params.system['research']:
         # 获取标注数据，并打包保存
         logger.info("Research: auto get label data.")
         if not os.path.exists(os.path.join(self.dump_dir, 'try_round_auto_label_%d'%try_iter)):
           os.makedirs(os.path.join(self.dump_dir, 'try_round_auto_label_%d'%try_iter))
 
         for file_id, id in next_unlabeled_sample_ids:
           _, label = dataset.at(id)
+          label.update({'file_id': file_id, 'id': id})
+          
+          # 自动生成子目录
+          if '/' in file_id:
+            if not os.path.exists(os.path.join(self.dump_dir, 'try_round_auto_label_%d'%try_iter, file_id.split('/')[0])):
+              os.makedirs(os.path.join(self.dump_dir, 'try_round_auto_label_%d'%try_iter, file_id.split('/')[0]))
 
           # label 写成文件
           with open(os.path.join(self.dump_dir, 'try_round_auto_label_%d'%try_iter, file_id), 'w') as fp:
             json.dump(label, fp)
 
         # 使用tar,打包
         logger.info("Research: warp label data.")
```

### Comparing `antgo-0.0.8/antgo/ant/activelearning_api.py` & `antgo-0.0.9/antgo/ant/activelearning_api.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/ant/base.py` & `antgo-0.0.9/antgo/ant/base.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,14 @@
 from antgo.utils.fs import *
 from antgo import config
 from antgo.ant.utils import *
 import yaml
 from antgo.utils.utils import *
 from datetime import datetime
 from antgo.ant.warehouse import *
-import antvis.client.mlogger as mlogger
 from antgo.context import *
 import socket
 
 
 if sys.version > '3':
   PY3 = True
 else:
```

### Comparing `antgo-0.0.8/antgo/ant/batch.py` & `antgo-0.0.9/antgo/ant/batch.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,24 +1,27 @@
 # -*- coding: UTF-8 -*-
 # @Time    : 18-9-22
 # @File    : batch.py
 # @Author  : jian<jian@mltalker.com>
 from __future__ import division
 from __future__ import print_function
 from __future__ import unicode_literals
+
+from cv2 import log
 from antgo.dataflow.dataset.spider_dataset import SpiderDataset
 from antgo.ant.base import *
 from antgo.ant.base import _pick_idle_port
 from antgo.task.task import *
 from antgo.dataflow.common import *
 from antgo.dataflow.basic import *
 from antgo.dataflow.recorder import *
 from antgo.crowdsource.batch_server import *
 from antvis.client.httprpc import *
 import json
+import traceback
 
 
 class AntBatch(AntBase):
     def __init__(self,
                  ant_context,
                  ant_name,
                  ant_host_ip,
@@ -142,23 +145,25 @@
                 # 更新web页面
                 if is_launch_web_server:
                     self.rpc.config.post(config_data=json.dumps(running_info))
                 return
 
             # 4.step load dataset
             logger.info('Load task dataset and split.')
-
+            
             dataset_name = ''
             selected_dataset_stages = []
             if len(running_ant_task.dataset_name.split('/')) == 2:
                 dataset_name, dataset_stage = running_ant_task.dataset_name.split('/')
                 selected_dataset_stages.append(dataset_stage)
             else:
                 dataset_name = running_ant_task.dataset_name
                 selected_dataset_stages = ['test']
+            
+            logger.info('Using dataset %s/%s'%(dataset_name, selected_dataset_stages[0]))
 
             # 5.step prepare ablation blocks
             logger.info('Prepare model ablation blocks.')
             ablation_blocks = getattr(self.ant_context.params, 'ablation', [])
             if ablation_blocks is None:
                 ablation_blocks = []
             for b in ablation_blocks:
@@ -176,14 +181,15 @@
                         SpiderDataset(self.command_queue,
                                         os.path.join(self.ant_data_source, dataset_name), None)
                 else:
                     ant_test_dataset = \
                         running_ant_task.dataset(dataset_stage,
                                                     os.path.join(self.ant_data_source, dataset_name),
                                                     running_ant_task.dataset_params)
+
                 # using unlabel
                 if self.unlabel:
                     ant_test_dataset = UnlabeledDataset(ant_test_dataset)
 
                 output_dir = experiment_dump_dir
                 if is_launch_web_server:
                     output_dir = os.path.join(experiment_dump_dir, 'batch', 'static', 'data', dataset_stage)
@@ -226,14 +232,15 @@
                 with safe_recorder_manager(self.context.recorder):
                     # 完成推断过程
                     try:
                         self.context.call_infer_process(ant_test_dataset, dump_dir=output_dir)
                     except Exception as e:
                         if type(e.__cause__) != StopIteration:
                             print(e)
+                            traceback.print_exc()
 
                 self.context.recorder.close()
             return
 
         # 5.step 启动bach server
         if is_launch_web_server:
             # 在独立线程中启动预测
```

### Comparing `antgo-0.0.8/antgo/ant/browser.py` & `antgo-0.0.9/antgo/ant/browser.py`

 * *Files 0% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 from antgo.dataflow.recorder import *
 from antgo.dataflow.dataset.parallel_read import MultiprocessReader
 from antvis.client.httprpc import *
 from antgo.dataflow.dataset.parallel_read import *
 import requests
 import json
 from jinja2 import Environment, FileSystemLoader
-
+import traceback
 
 class BrowserDataRecorder(object):
   def __init__(self, maxsize=30):
     self.queue = queue.Queue()  # 不设置队列最大缓冲
     self.prepare_queue = queue.Queue(maxsize=maxsize)
     self.dump_dir = ''
     self.dataset_flag = 'TRAIN'
```

### Comparing `antgo-0.0.8/antgo/ant/challenge.py` & `antgo-0.0.9/antgo/ant/challenge.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 from antgo.measures.deep_analysis import *
 from antgo.measures.significance import *
 import shutil
 import tarfile
 from datetime import datetime
 from antgo.measures import *
 from antgo.measures.yesno_crowdsource import *
-
+import traceback
 
 class AntChallenge(AntBase):
   def __init__(self, ant_context,
                ant_name,
                ant_data_folder,
                ant_dump_dir,
                ant_token,
@@ -150,14 +150,15 @@
           
         with performance_statistic_region(self.ant_name):
           try:
             self.context.call_infer_process(ant_test_dataset, infer_dump_dir)
           except Exception as e:
             if type(e.__cause__) != StopIteration:
               print(e)
+              traceback.print_exc()
 
         task_running_statictic = get_performance_statistic(self.ant_name)
         task_running_statictic = {self.ant_name: task_running_statictic}
         task_running_elapsed_time = task_running_statictic[self.ant_name]['time']['elapsed_time']
         task_running_statictic[self.ant_name]['time']['elapsed_time_per_sample'] = \
             task_running_elapsed_time / float(ant_test_dataset.size)
```

### Comparing `antgo-0.0.8/antgo/ant/debug.py` & `antgo-0.0.9/antgo/ant/debug.py`

 * *Files 2% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 import sys
 import yaml
 from datetime import datetime
 from types import FunctionType
 from antgo import config
 from antgo.dataflow.recorder import *
 from antgo.dataflow.common import *
-
+import traceback
 
 def debug_training_process(dataset_func, param_config=None, dump_dir=None):
   # 0.step get global context
   ctx = get_global_context()
   ctx.debug = True
 
   # 1.step parse params config file
```

### Comparing `antgo-0.0.8/antgo/ant/demo.py` & `antgo-0.0.9/antgo/ant/demo.py`

 * *Files 2% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 from antgo.crowdsource.demo_server import *
 from antgo.utils import logger
 from antvis.client.httprpc import *
 try:
     import queue
 except:
     import Queue as queue
-
+import traceback
 
 class AntDemo(AntBase):
   def __init__(self, ant_context,
                ant_name,
                ant_dump_dir,
                ant_token,
                ant_task_config,
@@ -163,17 +163,17 @@
                   if item['type'] in ['IMAGE', 'VIDEO', 'FILE']:
                       item['data'] = '%s/record/%s'%(infer_dump_dir, item['data'])
                 
             self.rpc.response.post(response=json.dumps(record_content))
                     
         self.context.recorder =  LocalRecorderNodeV2(_callback_func)
         self.context.call_infer_process(demo_dataset, dump_dir=infer_dump_dir)
-      except:
+      except Exception as e:
+        print(e)
         traceback.print_exc()
-        raise sys.exc_info()[0]
 
     process = threading.Thread(target=_run_infer_process)
     process.daemon = True
     process.start()
 
     # 6.step 启动web服务
     demo_server_start(demo_name,demo_type,demo_config,os.getpid(),dataset_queue, request_waiting_time)
```

### Comparing `antgo-0.0.8/antgo/ant/flags.py` & `antgo-0.0.9/antgo/ant/flags.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/ant/generate.py` & `antgo-0.0.9/antgo/ant/generate.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/ant/train.py` & `antgo-0.0.9/antgo/ant/train.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 from antgo.utils.serialize import *
 from antgo.resource.html import *
 from antgo.utils.concurrency import *
 from antgo.measures.statistic import *
 from antgo.measures.repeat_statistic import *
 from antgo.measures.deep_analysis import *
 import signal
+import traceback
 if sys.version > '3':
     PY3 = True
 else:
     PY3 = False
 
 FLAGS = flags.AntFLAGS
 
@@ -669,14 +670,15 @@
       logger.info('Start training process.')
       ant_train_dataset.reset_state()
       try:
         self.context.call_training_process(ant_train_dataset, train_dump_dir)
       except Exception as e:
         if type(e.__cause__) != StopIteration:
           print(e)
+          traceback.print_exc()
       
       self.context.from_experiment = train_dump_dir
       logger.info('Stop training process.')
 
   def _holdout_validation(self, train_dataset, running_ant_task, now_time):
     # 1.step split train set and validation set
     part_train_dataset, part_validation_dataset = \
@@ -694,14 +696,15 @@
       # training model
       logger.info("Traning process.")
       try:
         self.context.call_training_process(part_train_dataset, dump_dir)
       except Exception as e:
           if type(e.__cause__) != StopIteration:
             print(e)
+            traceback.print_exc()
 
       self.context.from_experiment = dump_dir
     
     logger.info("Infer process.")
     # data_annotation_branch = DataAnnotationBranch(Node.inputs(part_validation_dataset))
     self.context.recorder = RecorderNode2()
     intermediate_dump_dir = os.path.join(self.ant_dump_dir, dump_dir, 'record')
@@ -710,14 +713,15 @@
       # self.context.recorder.dump_dir = intermediate_dump_dir
       with performance_statistic_region(self.ant_name):
         try:
           self.context.call_infer_process(part_validation_dataset, dump_dir)
         except Exception as e:
           if type(e.__cause__) != StopIteration:
             print(e)
+            traceback.print_exc()
 
     task_running_statictic = get_performance_statistic(self.ant_name)
     task_running_statictic = {self.ant_name: task_running_statictic}
     task_running_elapsed_time = task_running_statictic[self.ant_name]['time']['elapsed_time']
     task_running_statictic[self.ant_name]['time']['elapsed_time_per_sample'] = \
       task_running_elapsed_time / float(part_validation_dataset.size)
 
@@ -813,14 +817,15 @@
       self.context.from_experiment = from_experiment
       logger.info('Start training process at repeathold %d round.'%repeat)
       try:
         self.context.call_training_process(part_train_dataset, dump_dir)
       except Exception as e:
           if type(e.__cause__) != StopIteration:
             print(e)
+            traceback.print_exc()
 
       self.context.from_experiment = dump_dir
       logger.info('Stop training process at repeathold %d round.' % repeat)
       
       # 3.step evaluation measures
       # split data and label
       logger.info('Start infer process at repeathold %d round.' % repeat)
@@ -832,14 +837,15 @@
       with safe_recorder_manager(self.context.recorder):
         with performance_statistic_region(self.ant_name):
           try:
             self.context.call_infer_process(data_annotation_branch.output(0), dump_dir)
           except Exception as e:
             if type(e.__cause__) != StopIteration:
               print(e)
+              traceback.print_exc()
 
       logger.info('Start infer process at repeathold %d round.' % repeat)
       
       # clear
       self.context.recorder = None
 
       task_running_statictic = get_performance_statistic(self.ant_name)
@@ -892,14 +898,15 @@
       self.context.from_experiment = from_experiment
       logger.info('Start training process at bootstrap %d round.'%bootstrap_i)
       try:
         self.context.call_training_process(part_train_dataset, dump_dir)
       except Exception as e:
           if type(e.__cause__) != StopIteration:
             print(e)
+            traceback.print_exc()
 
       self.context.from_experiment = dump_dir
       logger.info('Stop training process at bootstrap %d round.' % bootstrap_i)
       
       # 3.step evaluation measures
       # split data and label
       logger.info('Start infer process at bootstrap %d round.' % bootstrap_i)
@@ -910,14 +917,15 @@
       with safe_recorder_manager(self.context.recorder):
         with performance_statistic_region(self.ant_name):
           try:
             self.context.call_infer_process(data_annotation_branch.output(0), dump_dir)
           except Exception as e:
             if type(e.__cause__) != StopIteration:
               print(e)
+              traceback.print_exc()
 
       logger.info('Stop infer process at bootstrap %d round.' % bootstrap_i)
       
       # clear
       self.context.recorder = None
 
       task_running_statictic = get_performance_statistic(self.ant_name)
@@ -970,14 +978,15 @@
       logger.info('Start training process at kfold %d round.'%k)
       self.context.from_experiment = from_experiment
       try:
         self.context.call_training_process(part_train_dataset, dump_dir)
       except Exception as e:
           if type(e.__cause__) != StopIteration:
             print(e)
+            traceback.print_exc()
 
       self.context.from_experiment = dump_dir
       logger.info('Stop training process at kfold %d round.'%k)
 
       # 3.step evaluation measures
       # split data and label
       logger.info('Start infer process at kfold %d round.'%k)
@@ -989,14 +998,15 @@
       with safe_recorder_manager(self.context.recorder):
         with performance_statistic_region(self.ant_name):
           try:
             self.context.call_infer_process(data_annotation_branch.output(0), dump_dir)
           except Exception as e:
             if type(e.__cause__) != StopIteration:
               print(e)
+              traceback.print_exc()
 
       logger.info('Stop infer process at kfold %d round.'%k)
       # clear
       self.context.recorder = None
 
       task_running_statictic = get_performance_statistic(self.ant_name)
       task_running_statictic = {self.ant_name: task_running_statictic}
```

### Comparing `antgo-0.0.8/antgo/ant/utils.py` & `antgo-0.0.9/antgo/ant/utils.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/ant/warehouse.py` & `antgo-0.0.9/antgo/ant/warehouse.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/ant/watch.py` & `antgo-0.0.9/antgo/ant/watch.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/codebook/tf/dataset.py` & `antgo-0.0.9/antgo/codebook/tf/dataset.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/codebook/tf/layers.py` & `antgo-0.0.9/antgo/codebook/tf/layers.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/codebook/tf/preprocess.py` & `antgo-0.0.9/antgo/codebook/tf/preprocess.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/codebook/tf/stublayers.py` & `antgo-0.0.9/antgo/codebook/tf/stublayers.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/codebook/tf/tftool_records.py` & `antgo-0.0.9/antgo/codebook/tf/tftool_records.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/codebook/tf/tftools.py` & `antgo-0.0.9/antgo/codebook/tf/tftools.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/config.py` & `antgo-0.0.9/antgo/config.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/context.py` & `antgo-0.0.9/antgo/context.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/activelearning_server.py` & `antgo-0.0.9/antgo/crowdsource/activelearning_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/base_server.py` & `antgo-0.0.9/antgo/crowdsource/base_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/batch_server.py` & `antgo-0.0.9/antgo/crowdsource/batch_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/browser_server.py` & `antgo-0.0.9/antgo/crowdsource/browser_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/crowdsource_server.py` & `antgo-0.0.9/antgo/crowdsource/crowdsource_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/demo_server.py` & `antgo-0.0.9/antgo/crowdsource/demo_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/utils.py` & `antgo-0.0.9/antgo/crowdsource/utils.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/crowdsource/watch_server.py` & `antgo-0.0.9/antgo/crowdsource/watch_server.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/cutils/maskApi.c` & `antgo-0.0.9/antgo/cutils/maskApi.c`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/cutils/maskApi.h` & `antgo-0.0.9/antgo/cutils/maskApi.h`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/basic.py` & `antgo-0.0.9/antgo/dataflow/basic.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/common.py` & `antgo-0.0.9/antgo/dataflow/common.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/core.py` & `antgo-0.0.9/antgo/dataflow/core.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/__init__.py` & `antgo-0.0.9/antgo/dataflow/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/ade20k.py` & `antgo-0.0.9/antgo/dataflow/dataset/ade20k.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/celeba.py` & `antgo-0.0.9/antgo/dataflow/dataset/celeba.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/cifar.py` & `antgo-0.0.9/antgo/dataflow/dataset/cifar.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/coco2017.py` & `antgo-0.0.9/antgo/dataflow/dataset/coco2017.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/dataset.py` & `antgo-0.0.9/antgo/dataflow/dataset/dataset.py`

 * *Files 0% similar despite different names*

```diff
@@ -99,19 +99,24 @@
 
   def unlabeled_size(self):
     unlabeled_folder = os.path.join(self.dir, self.unlabeled_tag)
     if not os.path.exists(unlabeled_folder):
       return 0
 
     if not os.path.exists(os.path.join(self.dir, 'unlabeled_list.txt')):
+      unorder_list = []
+      for file in os.listdir(unlabeled_folder):
+        if file[0] == '.':
+          continue
+        unorder_list.append(file)
+      
+      order_list = sorted(unorder_list)
       with open(os.path.join(self.dir, 'unlabeled_list.txt'), 'w') as fp:
-        for file in os.listdir(unlabeled_folder):
-          if file[0] == '.':
-            continue
-          fp.write('%s,%d\n' % (file, 0))
+        for file in order_list:
+          fp.write('%s/%s,%d\n' % (self.unlabeled_tag, file, 0))
 
     has_labeled_list = []
     if os.path.exists(os.path.join(self.dir, 'candidates.txt')):
       with open(os.path.join(self.dir, 'candidates.txt'), 'r') as fp:
         line_content = fp.readline()
         while line_content:
           _, data_file, _ = line_content.split(',')
@@ -123,32 +128,37 @@
         pass
 
     unlabeled_list = []
     with open(os.path.join(self.dir, 'unlabeled_list.txt'), 'r') as fp:
       line_content = fp.readline()
       while line_content:
         file_name, _ = line_content.split(',')
-        if file_name not in has_labeled_list:
+        if file_name.split('/')[-1] not in has_labeled_list:
           unlabeled_list.append(file_name)
 
         line_content = fp.readline()
 
     return len(unlabeled_list)
 
   def unlabeled(self, tag=''):
     unlabeled_folder = os.path.join(self.dir, self.unlabeled_tag)
     if not os.path.exists(unlabeled_folder):
       return None
 
     if not os.path.exists(os.path.join(self.dir, 'unlabeled_list.txt')):
+      unorder_list = []
+      for file in os.listdir(unlabeled_folder):
+        if file[0] == '.':
+          continue
+        unorder_list.append(file)
+      
+      order_list = sorted(unorder_list)
       with open(os.path.join(self.dir, 'unlabeled_list.txt'), 'w') as fp:
-        for file in os.listdir(unlabeled_folder):
-          if file[0] == '.':
-            continue
-          fp.write('%s,%d\n' % (file, 0))
+        for file in order_list:
+          fp.write('%s/%s,%d\n' % (self.unlabeled_tag, file, 0))
 
     has_labeled_list = []
     if os.path.exists(os.path.join(self.dir, 'candidates.txt')):
       with open(os.path.join(self.dir, 'candidates.txt'), 'r') as fp:
         line_content = fp.readline()
         while line_content:
           _, data_file, _ = line_content.split(',')
@@ -166,36 +176,36 @@
         file_name, _ = line_content.split(',')
         unlabeled_list.append(file_name)
 
         line_content = fp.readline()
     
     unlabeled_data = []
     for index, file in enumerate(unlabeled_list):
-      if file not in has_labeled_list:
-        unlabeled_data.append((os.path.join(self.dir, self.unlabeled_tag, file), {'id': index, 'file_id': file}))
+      if file.split('/')[-1] not in has_labeled_list:
+        unlabeled_data.append({'id': index, 'file_id': file})
 
     return unlabeled_data
 
   def make_candidate(self, unlabeled_id, unlabeled_file, label_file, status=''):
     # status: 'SKIP/OK'
     if not os.path.exists(os.path.join(self.dir, 'candidates')):
       os.makedirs(os.path.join(self.dir, 'candidates'))
       os.makedirs(os.path.join(self.dir, 'candidates', 'data'))
       os.makedirs(os.path.join(self.dir, 'candidates', 'label'))
 
     with open(os.path.join(self.dir, 'candidates.txt'), 'a') as fp:
       if status == 'OK':
         # copy data file to candidates/data
-        shutil.copy(os.path.join(self.dir, self.unlabeled_tag, unlabeled_file), os.path.join(self.dir, 'candidates', 'data'))
+        shutil.copy(os.path.join(self.dir, unlabeled_file), os.path.join(self.dir, 'candidates', 'data'))
 
         # copy label file to candidates/label
         shutil.copy(label_file, os.path.join(self.dir, 'candidates', 'label'))
 
         # write to canndidates.txt
-        fp.write('%d,%s,%s\n'%(unlabeled_id, 'candidates/data/%s'%unlabeled_file, 'candidates/label/%s'%label_file.split('/')[-1]))
+        fp.write('%d,%s,%s\n'%(unlabeled_id, 'candidates/data/%s'%unlabeled_file.split('/')[-1], 'candidates/label/%s'%label_file.split('/')[-1]))
 
   def check_candidate(self, unlabeled_files, finished_label_folder):
     # 检查准备进入候选列表的标注数据，与等待的未标注数据一致
     consistent_sample_num = 0
     logger.info("Finshed label folder %s"%finished_label_folder)
 
     for sample_file, _ in unlabeled_files:
@@ -808,27 +818,31 @@
                          'put it at %s'%(f, target_path))
             os._exit(-1)
 
 
 class UnlabeledDataset(Dataset):
   def __init__(self, dataset):
     super(UnlabeledDataset, self).__init__()
-    self.data = dataset.unlabeled()
+    self.dataset = dataset
+    self.unlabeled_data = dataset.unlabeled()
 
   def data_pool(self):
     for id in range(self.size):
       yield self.at(id)
 
-  def at(self, id):
-    print(id)
-    return self.data[id]
+  def at(self, unlabeled_id):
+    id = self.unlabeled_data[unlabeled_id]['id']
+    file_id = self.unlabeled_data[unlabeled_id]['file_id']
+    data = self.dataset.at(id)
+    data[1].update({'file_id': file_id, 'id': id})
+    return data
 
   @property
   def size(self):
-    return len(self.data)
+    return len(self.unlabeled_data)
 
 class DataAnnotationSplitDataset(object):
   def __init__(self, dataset):
       super().__init__()
       self.dataset = dataset
     
   def data_pool(self):
```

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/empty_dataset.py` & `antgo-0.0.9/antgo/dataflow/dataset/empty_dataset.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/fashionai_attribute.py` & `antgo-0.0.9/antgo/dataflow/dataset/fashionai_attribute.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/fashionai_landmark.py` & `antgo-0.0.9/antgo/dataflow/dataset/fashionai_landmark.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/flic.py` & `antgo-0.0.9/antgo/dataflow/dataset/flic.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/horse2zebra.py` & `antgo-0.0.9/antgo/dataflow/dataset/horse2zebra.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/ilsvrc.py` & `antgo-0.0.9/antgo/dataflow/dataset/ilsvrc.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/iphone2dslr.py` & `antgo-0.0.9/antgo/dataflow/dataset/iphone2dslr.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/lfw.py` & `antgo-0.0.9/antgo/dataflow/dataset/lfw.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/lip.py` & `antgo-0.0.9/antgo/dataflow/dataset/lip.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/mnist.py` & `antgo-0.0.9/antgo/dataflow/dataset/mnist.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/omniglot.py` & `antgo-0.0.9/antgo/dataflow/dataset/omniglot.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/parallel_read.py` & `antgo-0.0.9/antgo/dataflow/dataset/parallel_read.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/pascal_voc.py` & `antgo-0.0.9/antgo/dataflow/dataset/pascal_voc.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/queue_dataset.py` & `antgo-0.0.9/antgo/dataflow/dataset/queue_dataset.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/random_dataset.py` & `antgo-0.0.9/antgo/dataflow/dataset/random_dataset.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/simplecsvs.py` & `antgo-0.0.9/antgo/dataflow/dataset/simplecsvs.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/simpleimages.py` & `antgo-0.0.9/antgo/dataflow/dataset/simpleimages.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/simplevideos.py` & `antgo-0.0.9/antgo/dataflow/dataset/simplevideos.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/spider_dataset.py` & `antgo-0.0.9/antgo/dataflow/dataset/spider_dataset.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/standard.py` & `antgo-0.0.9/antgo/dataflow/dataset/standard.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/svhn.py` & `antgo-0.0.9/antgo/dataflow/dataset/svhn.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/dataset/vggface.py` & `antgo-0.0.9/antgo/dataflow/dataset/vggface.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/imgaug/distorted.py` & `antgo-0.0.9/antgo/dataflow/imgaug/distorted.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/imgaug/grid.py` & `antgo-0.0.9/antgo/dataflow/imgaug/grid.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/imgaug/regular.py` & `antgo-0.0.9/antgo/dataflow/imgaug/regular.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/dataflow/recorder.py` & `antgo-0.0.9/antgo/dataflow/recorder.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/jupytercontext.py` & `antgo-0.0.9/antgo/jupytercontext.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/main.py` & `antgo-0.0.9/antgo/main.py`

 * *Files 10% similar despite different names*

```diff
@@ -2,29 +2,31 @@
 # @Time    : 17-3-3
 # @File    : main.py
 # @Author  : jian<jian@mltalker.com>
 from __future__ import division
 from __future__ import print_function
 from __future__ import unicode_literals
 import sys
-# sys.path.append('/workspace/workspace/portrait_code/tool/antgo')
-# sys.path.append('/workspace/workspace/portrait_code/tool/antgo/antgo')
+from typing import NamedTuple
+sys.path.append('/workspace/workspace/portrait_code/tool/antgo')
+sys.path.append('/workspace/workspace/portrait_code/tool/antgo/antgo')
 from antgo.ant.generate import *
 from antgo.ant.demo import *
 from antgo.ant.train import *
 from antgo.ant.challenge import *
 from antgo.ant.browser import *
 from antgo.ant.batch import *
 from antgo.ant.activelearning import *
 from antgo.ant import activelearning_api
 from antgo.ant.utils import *
 from antgo.sandbox.sandbox import *
 from antgo.utils.utils import *
 from antgo.utils.dht import *
 from antgo import version
+import traceback
 from jinja2 import Environment, FileSystemLoader
 
 import multiprocessing
 import subprocess
 
 if sys.version > '3':
     PY3 = True
@@ -106,25 +108,48 @@
 
   # token
   token = FLAGS.token()
   if not PY3 and token is not None:
     token = unicode(token)
 
   if sys.argv[1] == 'config':
+    if not os.path.exists(os.path.join(os.environ['HOME'], '.config', 'antgo')):
+      os.makedirs(os.path.join(os.environ['HOME'], '.config', 'antgo'))
+
     if FLAGS.config() is not None:
       # 使用指定配置文件更新
-      if not os.path.exists(os.path.join(os.environ['HOME'], '.config', 'antgo')):
-        os.makedirs(os.path.join(os.environ['HOME'], '.config', 'antgo'))
-
       shutil.copy(FLAGS.config(), os.path.join(os.environ['HOME'], '.config', 'antgo', 'config.xml'))
       logger.info('Success update config file.')
     else:
       # 在当前目录生成默认配置文件
-      shutil.copy(os.path.join('/'.join(os.path.realpath(__file__).split('/')[0:-1]), 'config.xml'), "./config.xml")
-      logger.info('Build default config file.')
+      # --dataset, --token, 自动配置
+      config_data = {'DATASET_FACTORY': '', 'USER_TOKEN': ''}
+      if FLAGS.dataset() is not None:
+        if not os.path.exists(FLAGS.dataset()):
+          logger.error('Dataset factory path dont exist.')
+          return
+        config_data['DATASET_FACTORY'] = FLAGS.dataset()
+
+      if FLAGS.token() is not None:
+         config_data['USER_TOKEN'] = FLAGS.token()
+
+      env = Environment(loader=FileSystemLoader('/'.join(os.path.realpath(__file__).split('/')[0:-1])))
+      config_template = env.get_template('config.xml')
+      config_content = config_template.render(**config_data)
+
+      if config_data['DATASET_FACTORY'] != '':
+        with open(os.path.join(os.environ['HOME'], '.config', 'antgo', 'config.xml'),'w') as fp:
+          fp.write(config_content)
+        
+        logger.info('Finish antgo global config.')
+      else:
+        with open('./config.xml','w') as fp:
+          fp.write(config_content)
+
+        logger.info('Please fill ./config.xml, then call (antgo config --config=./config.xml) to finish global config.')
     return
 
   # 检查配置文件是否存在
   if not os.path.exists(os.path.join(os.environ['HOME'], '.config', 'antgo', 'config.xml')):
     logger.error('Missing config file, please run antgo config.')
     return
 
@@ -134,15 +159,15 @@
 
   # 检查最低版本与当前版本的兼容性
   if FLAGS.running_platform == 'local' and FLAGS.version() is not None:
     a, b, c = FLAGS.version().split('.')
     sys_a, sys_b, sys_c = version.split('.')
     if int(sys_a) < int(a) or int(sys_b) < int(b) or int(sys_c) < int(c):
       logger.error('Antgo version dont satisfy task minimum request (%s).'%FLAGS.version())
-      sys.exit(-1)
+      return
 
   # 4.step check factory
   factory = getattr(Config, 'factory', None)
   if factory is None or \
       factory == '' or not os.path.exists(Config.factory):
     logger.error('Factory folder is missing, please run antgo config.')
     return
@@ -261,15 +286,15 @@
       os.makedirs(dump_dir)
 
   # 7.4 check main file
   main_file = FLAGS.main_file()
   if main_file is None or not os.path.exists(os.path.join(main_folder, main_file)):
     if not (FLAGS.worker() or FLAGS.master()):
       logger.error('Main executing file dont exist.')
-      sys.exit(-1)
+      return
 
   # 8 step ant running
   # 8.1 step what is task
   task = FLAGS.task()
   if task is not None:
     if os.path.exists(os.path.join(task_factory, task)):
       task = os.path.join(task_factory, task)
@@ -283,26 +308,27 @@
       task_content = '<task><task_name>%s</task_name><task_type>%s</task_type><task_badcase><badcase_num>%d</badcase_num><badcase_category>%d</badcase_category></task_badcase>' \
                      '<input>' \
                      '<source_data><data_set_name>%s</data_set_name>' \
                      '</source_data>' \
                      '<estimation_procedure><type>%s</type></estimation_procedure>' \
                      '<evaluation_measures><evaluation_measure>%s</evaluation_measure></evaluation_measures>' \
                      '</input>' \
-                     '</task>'%('default-task', FLAGS.task_t(), FLAGS.task_badcase_num(), FLAGS.task_badcase_category(),dataset, FLAGS.task_ep(), FLAGS.task_em())
+                     '</task>'%(name, FLAGS.task_t(), FLAGS.task_badcase_num(), FLAGS.task_badcase_category(), dataset, FLAGS.task_ep(), FLAGS.task_em())
       fp.write(task_content)
     task = os.path.join(task_factory, '%s.xml'%name)
 
   # 8.2 step load ant context
   ant_context = None
   if main_file is not None and main_file != '':
     try:
       ant_context = main_context(main_file, main_folder)
     except Exception as e:
-      print(e)
+      traceback.print_exc()
       print('Fail to load main_file %s.'%main_file)
+      return
   else:
     ant_context = Context()
   
   # 8.3 step load model config
   main_param = FLAGS.main_param()
   if main_param is not None:
     main_config_path = os.path.join(main_folder, main_param)
@@ -318,16 +344,17 @@
                     'ip': FLAGS.host_ip(),
                     'port': FLAGS.host_port(),
                     'devices': FLAGS.devices(),
                     'running_platform': FLAGS.running_platform()},
         })
         ant_context.params = params
     except Exception as e:
-      print(e)
+      traceback.print_exc()
       print('Fail to load main_param %s.'%main_param)
+      return
 
   ant_context.name = name
   ant_context.data_factory = data_factory
   ant_context.task_factory = task_factory
 
   # 8.4 step load experiment
   if FLAGS.from_experiment() is not None and \
@@ -338,15 +365,15 @@
       # 绝对路径指定的实验
       experiment_path = FLAGS.from_experiment()
     else:
       experiment_path = os.path.join(dump_dir, FLAGS.from_experiment())
 
     if not os.path.exists(experiment_path):
       logger.error('Couldnt find experiment %s.'%FLAGS.from_experiment())
-      exit(-1)
+      return
 
     # 设置实验目录
     ant_context.from_experiment = experiment_path
 
   # time stamp
   time_stamp = timestamp()
   if ant_cmd == "train":
```

### Comparing `antgo-0.0.8/antgo/measures/__init__.py` & `antgo-0.0.9/antgo/measures/__init__.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/ali_fashion_attribute_error.py` & `antgo-0.0.9/antgo/measures/ali_fashion_attribute_error.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/ali_fashion_landmark_ne.py` & `antgo-0.0.9/antgo/measures/ali_fashion_landmark_ne.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/average_precision.py` & `antgo-0.0.9/antgo/measures/average_precision.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/base.py` & `antgo-0.0.9/antgo/measures/base.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/binary_c.py` & `antgo-0.0.9/antgo/measures/binary_c.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/binomial_deviance.py` & `antgo-0.0.9/antgo/measures/binomial_deviance.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/confusion_matrix.py` & `antgo-0.0.9/antgo/measures/confusion_matrix.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/crowdsource.py` & `antgo-0.0.9/antgo/measures/crowdsource.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/deep_analysis.py` & `antgo-0.0.9/antgo/measures/deep_analysis.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/error.py` & `antgo-0.0.9/antgo/measures/error.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/face_task.py` & `antgo-0.0.9/antgo/measures/face_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/kdd_average_precision.py` & `antgo-0.0.9/antgo/measures/kdd_average_precision.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/matting_task.py` & `antgo-0.0.9/antgo/measures/matting_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/moving_statistic.py` & `antgo-0.0.9/antgo/measures/moving_statistic.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/multi_c.py` & `antgo-0.0.9/antgo/measures/multi_c.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/multic_task.py` & `antgo-0.0.9/antgo/measures/multic_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/multil_task.py` & `antgo-0.0.9/antgo/measures/multil_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/objdect_task.py` & `antgo-0.0.9/antgo/measures/objdect_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/pck.py` & `antgo-0.0.9/antgo/measures/pck.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/person_search_task.py` & `antgo-0.0.9/antgo/measures/person_search_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/precision_recall.py` & `antgo-0.0.9/antgo/measures/precision_recall.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/quadratic_weighted_kappa.py` & `antgo-0.0.9/antgo/measures/quadratic_weighted_kappa.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/regression_metric.py` & `antgo-0.0.9/antgo/measures/regression_metric.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/regression_task.py` & `antgo-0.0.9/antgo/measures/regression_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/repeat_statistic.py` & `antgo-0.0.9/antgo/measures/repeat_statistic.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/roc_auc.py` & `antgo-0.0.9/antgo/measures/roc_auc.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/segmentation_task.py` & `antgo-0.0.9/antgo/measures/segmentation_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/significance.py` & `antgo-0.0.9/antgo/measures/significance.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/statistic.py` & `antgo-0.0.9/antgo/measures/statistic.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/track_task.py` & `antgo-0.0.9/antgo/measures/track_task.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/measures/yesno_crowdsource.py` & `antgo-0.0.9/antgo/measures/yesno_crowdsource.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css` & `antgo-0.0.9/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css.map` & `antgo-0.0.9/antgo/resource/batch/static/css/app.80a5a508dc70f5d36d07622a58fec6b8.css.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/css/style.css` & `antgo-0.0.9/antgo/resource/batch/static/css/style.css`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.674f50d.eot` & `antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.674f50d.eot`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.af7ae50.woff2` & `antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.af7ae50.woff2`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.b06871f.ttf` & `antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.b06871f.ttf`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/fonts/fontawesome-webfont.fee66e7.woff` & `antgo-0.0.9/antgo/resource/batch/static/fonts/fontawesome-webfont.fee66e7.woff`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/img/banner-rank.png` & `antgo-0.0.9/antgo/resource/batch/static/img/banner-rank.png`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/img/fontawesome-webfont.912ec66.svg` & `antgo-0.0.9/antgo/resource/batch/static/img/fontawesome-webfont.912ec66.svg`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js` & `antgo-0.0.9/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js.map` & `antgo-0.0.9/antgo/resource/batch/static/js/app.526eb671e561af3c7330.js.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js` & `antgo-0.0.9/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js.map` & `antgo-0.0.9/antgo/resource/batch/static/js/manifest.2ae2e69a05c33dfc65f8.js.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js` & `antgo-0.0.9/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js.map` & `antgo-0.0.9/antgo/resource/batch/static/js/vendor.fa05c43dde0fec3359dc.js.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/index.html` & `antgo-0.0.9/antgo/resource/browser/index.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css` & `antgo-0.0.9/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css.map` & `antgo-0.0.9/antgo/resource/browser/static/css/app.27413d0985788f849d5ec9f108344d80.css.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/css/style.css` & `antgo-0.0.9/antgo/resource/browser/static/css/style.css`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.674f50d.eot` & `antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.674f50d.eot`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.af7ae50.woff2` & `antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.af7ae50.woff2`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.b06871f.ttf` & `antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.b06871f.ttf`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/fonts/fontawesome-webfont.fee66e7.woff` & `antgo-0.0.9/antgo/resource/browser/static/fonts/fontawesome-webfont.fee66e7.woff`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/img/fontawesome-webfont.912ec66.svg` & `antgo-0.0.9/antgo/resource/browser/static/img/fontawesome-webfont.912ec66.svg`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js` & `antgo-0.0.9/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js.map` & `antgo-0.0.9/antgo/resource/browser/static/js/app.87aa4d64f2a2a01ae55c.js.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js` & `antgo-0.0.9/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js.map` & `antgo-0.0.9/antgo/resource/browser/static/js/manifest.2ae2e69a05c33dfc65f8.js.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js` & `antgo-0.0.9/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js.map` & `antgo-0.0.9/antgo/resource/browser/static/js/vendor.7806dd61f57e3835a5f6.js.map`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/html.py` & `antgo-0.0.9/antgo/resource/html.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/static/antgo.ico` & `antgo-0.0.9/antgo/resource/static/antgo.ico`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/static/antgo.js` & `antgo-0.0.9/antgo/resource/static/antgo.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/static/banner.png` & `antgo-0.0.9/antgo/resource/static/banner.png`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/static/card.png` & `antgo-0.0.9/antgo/resource/static/card.png`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/static/holder.min.js` & `antgo-0.0.9/antgo/resource/static/holder.min.js`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/static/register.png` & `antgo-0.0.9/antgo/resource/static/register.png`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/activelearning.html` & `antgo-0.0.9/antgo/resource/templates/activelearning.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/crowdsource.html` & `antgo-0.0.9/antgo/resource/templates/crowdsource.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/demo.html` & `antgo-0.0.9/antgo/resource/templates/demo.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/statistic-report.html` & `antgo-0.0.9/antgo/resource/templates/statistic-report.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/task_main_file.template` & `antgo-0.0.9/antgo/resource/templates/task_main_file.template`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,17 @@
 # -*- coding: UTF-8 -*-
 # @Time    : {{ModelTime}}
 # @File    : {{ModelName}}_main.py
 # @Author  : {{ModelAuthor}}
 from __future__ import division
 from __future__ import unicode_literals
 from __future__ import print_function
-
+import os
+import sys
+sys.path.append(os.path.dirname(__file__))
 from antgo.dataflow.common import *
 from antgo.context import *
 from antgo.dataflow.dataset import *
 from antgo.measures import *
 from antgo.measures.base import *
 from antgo.trainer.trainer import *
 from antgo.ant.debug import *
```

### Comparing `antgo-0.0.8/antgo/resource/templates/task_main_param.template` & `antgo-0.0.9/antgo/resource/templates/task_main_param.template`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/task_shell.template` & `antgo-0.0.9/antgo/resource/templates/task_shell.template`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/trainmaster.html` & `antgo-0.0.9/antgo/resource/templates/trainmaster.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/resource/templates/yesno_crowdsource.html` & `antgo-0.0.9/antgo/resource/templates/yesno_crowdsource.html`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/sandbox/sandbox.py` & `antgo-0.0.9/antgo/sandbox/sandbox.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/task/task.py` & `antgo-0.0.9/antgo/task/task.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,14 @@
                ext_params=None,
                ant_context=None):
     self._task_id = task_id
     self._task_name = task_name
     self._task_type_id = task_type_id
     self._task_type = task_type
     self._dataset_id = dataset_id
-    self._dataset_name = dataset_name
     self._dataset_params = dataset_params
     self._dataset_url = dataset_url
     self._estimation_procedure_type = estimation_procedure_type
     self._estimation_procedure_params = estimation_procedure_params
     self._evaluation_measure = evaluation_measure
     self._cost_matrix = cost_matrix
     self._ant_context = ant_context
@@ -43,31 +42,35 @@
     
     if self._dataset_params is None:
       self._dataset_params = {}
       
     if self._dataset_url is not None and len(self._dataset_url) > 0:
       self._dataset_params['dataset_url'] = self._dataset_url
 
-    self._dataset_params['dataset_name'] = self._dataset_name
+    # 
+    self._dataset_name = dataset_name
+    if len(dataset_name.split('/')) != 1:
+      dataset_name = dataset_name.split('/')[0]
+    self._dataset_params['dataset_name'] = dataset_name
 
     # dataset class
-    if self._dataset_name is not None:
+    if dataset_name is not None:
       parse_flag = ''
       if self._dataset_url is not None and len(self._dataset_url) > 0:
         parse_flag = self._dataset_url.split('/')[-2]
-
-      self._ant_dataset = AntDatasetFactory.dataset(self._dataset_name, parse_flag)
+      self._ant_dataset = AntDatasetFactory.dataset(dataset_name, parse_flag)
 
     # related evaluation measures
     self._ant_measures = AntMeasuresFactory(self)
     self._class_label = class_label
 
   @property
   def dataset_name(self):
     return self._dataset_name
+
   @dataset_name.setter
   def dataset_name(self, name):
     self._dataset_name = name
 
   @property
   def dataset_params(self):
     '''
```

### Comparing `antgo-0.0.8/antgo/trainer/tfgantrainer.py` & `antgo-0.0.9/antgo/trainer/tfgantrainer.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/trainer/tfmodel_deploy.py` & `antgo-0.0.9/antgo/trainer/tfmodel_deploy.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/trainer/tftrainer.py` & `antgo-0.0.9/antgo/trainer/tftrainer.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/trainer/trainer.py` & `antgo-0.0.9/antgo/trainer/trainer.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_bbox.c` & `antgo-0.0.9/antgo/utils/_bbox.c`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_bbox.pyx` & `antgo-0.0.9/antgo/utils/_bbox.pyx`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_encode_png.pyx` & `antgo-0.0.9/antgo/utils/_encode_png.pyx`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_mask.c` & `antgo-0.0.9/antgo/utils/_mask.c`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_mask.pyx` & `antgo-0.0.9/antgo/utils/_mask.pyx`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_nms.c` & `antgo-0.0.9/antgo/utils/_nms.c`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_nms.pyx` & `antgo-0.0.9/antgo/utils/_nms.pyx`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_resize.c` & `antgo-0.0.9/antgo/utils/_resize.c`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/_resize.pyx` & `antgo-0.0.9/antgo/utils/_resize.pyx`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/argscope.py` & `antgo-0.0.9/antgo/utils/argscope.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/concurrency.py` & `antgo-0.0.9/antgo/utils/concurrency.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/cpu.py` & `antgo-0.0.9/antgo/utils/cpu.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/dht.py` & `antgo-0.0.9/antgo/utils/dht.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/encode.py` & `antgo-0.0.9/antgo/utils/encode.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/fs.py` & `antgo-0.0.9/antgo/utils/fs.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/gpu.py` & `antgo-0.0.9/antgo/utils/gpu.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/logger.py` & `antgo-0.0.9/antgo/utils/logger.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/mask.py` & `antgo-0.0.9/antgo/utils/mask.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/netvis.py` & `antgo-0.0.9/antgo/utils/netvis.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/pickledb.py` & `antgo-0.0.9/antgo/utils/pickledb.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/processbar.py` & `antgo-0.0.9/antgo/utils/processbar.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/serialize.py` & `antgo-0.0.9/antgo/utils/serialize.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/shared_queue/__init__.py` & `antgo-0.0.9/antgo/utils/shared_queue/__init__.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/shared_queue/queue.py` & `antgo-0.0.9/antgo/utils/shared_queue/queue.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/shared_queue/sharedmemory.py` & `antgo-0.0.9/antgo/utils/shared_queue/sharedmemory.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/timer.py` & `antgo-0.0.9/antgo/utils/timer.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo/utils/utils.py` & `antgo-0.0.9/antgo/utils/utils.py`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/antgo.egg-info/PKG-INFO` & `antgo-0.0.9/antgo.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.0
 Name: antgo
-Version: 0.0.8
+Version: 0.0.9
 Summary: machine learning experiment platform
 Home-page: https://github.com/jianzfb/antgo
 Author: jian
 Author-email: jian@mltalker.com
 License: UNKNOWN
 Description: ======================
         Antgo
```

### Comparing `antgo-0.0.8/antgo.egg-info/SOURCES.txt` & `antgo-0.0.9/antgo.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `antgo-0.0.8/setup.py` & `antgo-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 
 def readme():
     with open('README.rst') as f:
         return f.read()
 
 
 setup(name='antgo',
-      version='0.0.8',
+      version='0.0.9',
       description='machine learning experiment platform',
       __short_description__='machine learning experiment platform',
       url='https://github.com/jianzfb/antgo',
       author='jian',
       author_email='jian@mltalker.com',
       packages=['antgo',
                 'antgo.ant',
```

