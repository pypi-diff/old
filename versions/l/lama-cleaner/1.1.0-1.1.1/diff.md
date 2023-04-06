# Comparing `tmp/lama-cleaner-1.1.0.tar.gz` & `tmp/lama-cleaner-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lama-cleaner-1.1.0.tar", last modified: Thu Apr  6 14:13:20 2023, max compression
+gzip compressed data, was "lama-cleaner-1.1.1.tar", last modified: Thu Apr  6 14:56:34 2023, max compression
```

## Comparing `lama-cleaner-1.1.0.tar` & `lama-cleaner-1.1.1.tar`

### file list

```diff
@@ -1,102 +1,102 @@
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.173211 lama-cleaner-1.1.0/
--rw-r--r--   0 cwq        (501) staff       (20)    11357 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/LICENSE
--rw-r--r--   0 cwq        (501) staff       (20)     4640 2023-04-06 14:13:20.173106 lama-cleaner-1.1.0/PKG-INFO
--rw-r--r--   0 cwq        (501) staff       (20)     3213 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/README.md
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.160224 lama-cleaner-1.1.0/lama_cleaner/
--rw-r--r--   0 cwq        (501) staff       (20)      488 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/__init__.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.157409 lama-cleaner-1.1.0/lama_cleaner/app/
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.161423 lama-cleaner-1.1.0/lama_cleaner/app/build/
--rw-r--r--   0 cwq        (501) staff       (20)      742 2023-04-02 08:11:55.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/asset-manifest.json
--rw-r--r--   0 cwq        (501) staff       (20)      681 2023-04-02 08:11:55.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/index.html
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.157646 lama-cleaner-1.1.0/lama_cleaner/app/build/static/
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.161656 lama-cleaner-1.1.0/lama_cleaner/app/build/static/css/
--rw-r--r--   0 cwq        (501) staff       (20)    33113 2023-04-02 08:11:55.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/css/main.6ca672e8.css
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.162815 lama-cleaner-1.1.0/lama_cleaner/app/build/static/js/
--rw-r--r--   0 cwq        (501) staff       (20)   765660 2023-04-02 08:11:55.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/js/main.44aac645.js
--rw-r--r--   0 cwq        (501) staff       (20)     1971 2023-04-02 08:11:55.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/js/main.44aac645.js.LICENSE.txt
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.165205 lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/
--rw-r--r--   0 cwq        (501) staff       (20)   192104 2023-04-02 08:11:31.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-Black.67c2c5a144333953880b.ttf
--rw-r--r--   0 cwq        (501) staff       (20)   192548 2023-04-02 08:11:31.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-Bold.2bea7a7f7d052c74da25.ttf
--rw-r--r--   0 cwq        (501) staff       (20)   192140 2023-04-02 08:11:31.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-Regular.bb287b894b27372d8ea7.ttf
--rw-r--r--   0 cwq        (501) staff       (20)   192596 2023-04-02 08:11:31.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-SemiBold.1e98db4eb705b586728e.ttf
--rw-r--r--   0 cwq        (501) staff       (20)   431724 2023-04-02 08:11:31.000000 lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/coffee-machine-lineal.ee32631219cc3986f861.gif
--rw-r--r--   0 cwq        (501) staff       (20)     3244 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/benchmark.py
--rw-r--r--   0 cwq        (501) staff       (20)     4509 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/const.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.166020 lama-cleaner-1.1.0/lama_cleaner/file_manager/
--rw-r--r--   0 cwq        (501) staff       (20)       38 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/file_manager/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)     8685 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/file_manager/file_manager.py
--rw-r--r--   0 cwq        (501) staff       (20)     1293 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/file_manager/storage_backends.py
--rw-r--r--   0 cwq        (501) staff       (20)     1758 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/file_manager/utils.py
--rw-r--r--   0 cwq        (501) staff       (20)     8296 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/helper.py
--rw-r--r--   0 cwq        (501) staff       (20)      232 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/installer.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.167911 lama-cleaner-1.1.0/lama_cleaner/model/
--rw-r--r--   0 cwq        (501) staff       (20)        0 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/model/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)     9488 2023-02-19 13:09:51.000000 lama-cleaner-1.1.0/lama_cleaner/model/base.py
--rw-r--r--   0 cwq        (501) staff       (20)     6980 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model/controlnet.py
--rw-r--r--   0 cwq        (501) staff       (20)     6881 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/model/ddim_sampler.py
--rw-r--r--   0 cwq        (501) staff       (20)    57098 2023-02-27 13:02:16.000000 lama-cleaner-1.1.0/lama_cleaner/model/fcf.py
--rw-r--r--   0 cwq        (501) staff       (20)     3175 2023-03-01 13:56:56.000000 lama-cleaner-1.1.0/lama_cleaner/model/instruct_pix2pix.py
--rw-r--r--   0 cwq        (501) staff       (20)     1480 2023-02-27 13:02:16.000000 lama-cleaner-1.1.0/lama_cleaner/model/lama.py
--rw-r--r--   0 cwq        (501) staff       (20)    11275 2023-02-27 13:02:16.000000 lama-cleaner-1.1.0/lama_cleaner/model/ldm.py
--rw-r--r--   0 cwq        (501) staff       (20)     2884 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model/manga.py
--rw-r--r--   0 cwq        (501) staff       (20)    62625 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model/mat.py
--rw-r--r--   0 cwq        (501) staff       (20)      716 2023-02-19 13:09:51.000000 lama-cleaner-1.1.0/lama_cleaner/model/opencv2.py
--rw-r--r--   0 cwq        (501) staff       (20)     2934 2023-03-01 13:56:56.000000 lama-cleaner-1.1.0/lama_cleaner/model/paint_by_example.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.168334 lama-cleaner-1.1.0/lama_cleaner/model/pipeline/
--rw-r--r--   0 cwq        (501) staff       (20)      108 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model/pipeline/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)    28149 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model/pipeline/pipeline_stable_diffusion_controlnet_inpaint.py
--rw-r--r--   0 cwq        (501) staff       (20)    11851 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/model/plms_sampler.py
--rw-r--r--   0 cwq        (501) staff       (20)     6642 2023-04-03 14:39:48.000000 lama-cleaner-1.1.0/lama_cleaner/model/sd.py
--rw-r--r--   0 cwq        (501) staff       (20)    33811 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model/utils.py
--rw-r--r--   0 cwq        (501) staff       (20)    15395 2023-02-27 13:02:16.000000 lama-cleaner-1.1.0/lama_cleaner/model/zits.py
--rw-r--r--   0 cwq        (501) staff       (20)     2497 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/model_manager.py
--rw-r--r--   0 cwq        (501) staff       (20)     8313 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/parse_args.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.169839 lama-cleaner-1.1.0/lama_cleaner/plugins/
--rw-r--r--   0 cwq        (501) staff       (20)      231 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)      280 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/base_plugin.py
--rw-r--r--   0 cwq        (501) staff       (20)     2400 2023-04-03 05:14:59.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/gfpgan_plugin.py
--rw-r--r--   0 cwq        (501) staff       (20)     2750 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/gfpganer.py
--rw-r--r--   0 cwq        (501) staff       (20)     4156 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/gif.py
--rw-r--r--   0 cwq        (501) staff       (20)     2555 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/interactive_seg.py
--rw-r--r--   0 cwq        (501) staff       (20)     3573 2023-04-03 05:31:35.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/realesrgan.py
--rw-r--r--   0 cwq        (501) staff       (20)     1018 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/remove_bg.py
--rw-r--r--   0 cwq        (501) staff       (20)     1747 2023-04-03 05:15:02.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/restoreformer.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.170180 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/
--rw-r--r--   0 cwq        (501) staff       (20)      363 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)     2929 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/build_sam.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.171020 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/
--rw-r--r--   0 cwq        (501) staff       (20)      385 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)     1479 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/common.py
--rw-r--r--   0 cwq        (501) staff       (20)    14407 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/image_encoder.py
--rw-r--r--   0 cwq        (501) staff       (20)     6614 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/mask_decoder.py
--rw-r--r--   0 cwq        (501) staff       (20)     8594 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/prompt_encoder.py
--rw-r--r--   0 cwq        (501) staff       (20)     7225 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/sam.py
--rw-r--r--   0 cwq        (501) staff       (20)     8396 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/transformer.py
--rw-r--r--   0 cwq        (501) staff       (20)    11837 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/predictor.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.171259 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/utils/
--rw-r--r--   0 cwq        (501) staff       (20)      197 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/utils/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)     4054 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/utils/transforms.py
--rw-r--r--   0 cwq        (501) staff       (20)     1309 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/runtime.py
--rw-r--r--   0 cwq        (501) staff       (20)     3306 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/schema.py
--rw-r--r--   0 cwq        (501) staff       (20)    17556 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/server.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.172905 lama-cleaner-1.1.0/lama_cleaner/tests/
--rw-r--r--   0 cwq        (501) staff       (20)        0 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/tests/__init__.py
--rw-r--r--   0 cwq        (501) staff       (20)     2951 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_controlnet.py
--rw-r--r--   0 cwq        (501) staff       (20)     2320 2023-02-14 05:56:20.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_instruct_pix2pix.py
--rw-r--r--   0 cwq        (501) staff       (20)      596 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_load_img.py
--rw-r--r--   0 cwq        (501) staff       (20)     5826 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_model.py
--rw-r--r--   0 cwq        (501) staff       (20)     1491 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_model_md5.py
--rw-r--r--   0 cwq        (501) staff       (20)     3985 2023-02-05 13:09:10.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_paint_by_example.py
--rw-r--r--   0 cwq        (501) staff       (20)     2631 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_plugins.py
--rw-r--r--   0 cwq        (501) staff       (20)      875 2023-02-08 03:34:52.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_save_exif.py
--rw-r--r--   0 cwq        (501) staff       (20)     7647 2023-04-02 07:46:39.000000 lama-cleaner-1.1.0/lama_cleaner/tests/test_sd_model.py
--rw-r--r--   0 cwq        (501) staff       (20)     7330 2023-04-03 15:00:04.000000 lama-cleaner-1.1.0/lama_cleaner/web_config.py
-drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:13:20.161038 lama-cleaner-1.1.0/lama_cleaner.egg-info/
--rw-r--r--   0 cwq        (501) staff       (20)     4640 2023-04-06 14:13:20.000000 lama-cleaner-1.1.0/lama_cleaner.egg-info/PKG-INFO
--rw-r--r--   0 cwq        (501) staff       (20)     3287 2023-04-06 14:13:20.000000 lama-cleaner-1.1.0/lama_cleaner.egg-info/SOURCES.txt
--rw-r--r--   0 cwq        (501) staff       (20)        1 2023-04-06 14:13:20.000000 lama-cleaner-1.1.0/lama_cleaner.egg-info/dependency_links.txt
--rw-r--r--   0 cwq        (501) staff       (20)       59 2023-04-06 14:13:20.000000 lama-cleaner-1.1.0/lama_cleaner.egg-info/entry_points.txt
--rw-r--r--   0 cwq        (501) staff       (20)      251 2023-04-06 14:13:20.000000 lama-cleaner-1.1.0/lama_cleaner.egg-info/requires.txt
--rw-r--r--   0 cwq        (501) staff       (20)       13 2023-04-06 14:13:20.000000 lama-cleaner-1.1.0/lama_cleaner.egg-info/top_level.txt
--rw-r--r--   0 cwq        (501) staff       (20)       38 2023-04-06 14:13:20.173247 lama-cleaner-1.1.0/setup.cfg
--rw-r--r--   0 cwq        (501) staff       (20)     1616 2023-04-06 14:12:49.000000 lama-cleaner-1.1.0/setup.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.774998 lama-cleaner-1.1.1/
+-rw-r--r--   0 cwq        (501) staff       (20)    11357 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/LICENSE
+-rw-r--r--   0 cwq        (501) staff       (20)     4640 2023-04-06 14:56:34.774861 lama-cleaner-1.1.1/PKG-INFO
+-rw-r--r--   0 cwq        (501) staff       (20)     3213 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/README.md
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.751259 lama-cleaner-1.1.1/lama_cleaner/
+-rw-r--r--   0 cwq        (501) staff       (20)      488 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/__init__.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.739412 lama-cleaner-1.1.1/lama_cleaner/app/
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.752303 lama-cleaner-1.1.1/lama_cleaner/app/build/
+-rw-r--r--   0 cwq        (501) staff       (20)      742 2023-04-02 08:11:55.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/asset-manifest.json
+-rw-r--r--   0 cwq        (501) staff       (20)      681 2023-04-02 08:11:55.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/index.html
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.739645 lama-cleaner-1.1.1/lama_cleaner/app/build/static/
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.752430 lama-cleaner-1.1.1/lama_cleaner/app/build/static/css/
+-rw-r--r--   0 cwq        (501) staff       (20)    33113 2023-04-02 08:11:55.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/css/main.6ca672e8.css
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.753154 lama-cleaner-1.1.1/lama_cleaner/app/build/static/js/
+-rw-r--r--   0 cwq        (501) staff       (20)   765660 2023-04-02 08:11:55.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/js/main.44aac645.js
+-rw-r--r--   0 cwq        (501) staff       (20)     1971 2023-04-02 08:11:55.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/js/main.44aac645.js.LICENSE.txt
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.754314 lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/
+-rw-r--r--   0 cwq        (501) staff       (20)   192104 2023-04-02 08:11:31.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-Black.67c2c5a144333953880b.ttf
+-rw-r--r--   0 cwq        (501) staff       (20)   192548 2023-04-02 08:11:31.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-Bold.2bea7a7f7d052c74da25.ttf
+-rw-r--r--   0 cwq        (501) staff       (20)   192140 2023-04-02 08:11:31.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-Regular.bb287b894b27372d8ea7.ttf
+-rw-r--r--   0 cwq        (501) staff       (20)   192596 2023-04-02 08:11:31.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-SemiBold.1e98db4eb705b586728e.ttf
+-rw-r--r--   0 cwq        (501) staff       (20)   431724 2023-04-02 08:11:31.000000 lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/coffee-machine-lineal.ee32631219cc3986f861.gif
+-rw-r--r--   0 cwq        (501) staff       (20)     3244 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/benchmark.py
+-rw-r--r--   0 cwq        (501) staff       (20)     4628 2023-04-06 14:55:53.000000 lama-cleaner-1.1.1/lama_cleaner/const.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.755034 lama-cleaner-1.1.1/lama_cleaner/file_manager/
+-rw-r--r--   0 cwq        (501) staff       (20)       38 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/file_manager/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)     8685 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/file_manager/file_manager.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1293 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/file_manager/storage_backends.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1758 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/file_manager/utils.py
+-rw-r--r--   0 cwq        (501) staff       (20)     8296 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/helper.py
+-rw-r--r--   0 cwq        (501) staff       (20)      232 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/installer.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.756948 lama-cleaner-1.1.1/lama_cleaner/model/
+-rw-r--r--   0 cwq        (501) staff       (20)        0 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/model/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)     9488 2023-02-19 13:09:51.000000 lama-cleaner-1.1.1/lama_cleaner/model/base.py
+-rw-r--r--   0 cwq        (501) staff       (20)     6980 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model/controlnet.py
+-rw-r--r--   0 cwq        (501) staff       (20)     6881 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/model/ddim_sampler.py
+-rw-r--r--   0 cwq        (501) staff       (20)    57098 2023-02-27 13:02:16.000000 lama-cleaner-1.1.1/lama_cleaner/model/fcf.py
+-rw-r--r--   0 cwq        (501) staff       (20)     3175 2023-03-01 13:56:56.000000 lama-cleaner-1.1.1/lama_cleaner/model/instruct_pix2pix.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1480 2023-02-27 13:02:16.000000 lama-cleaner-1.1.1/lama_cleaner/model/lama.py
+-rw-r--r--   0 cwq        (501) staff       (20)    11275 2023-02-27 13:02:16.000000 lama-cleaner-1.1.1/lama_cleaner/model/ldm.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2884 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model/manga.py
+-rw-r--r--   0 cwq        (501) staff       (20)    62625 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model/mat.py
+-rw-r--r--   0 cwq        (501) staff       (20)      716 2023-02-19 13:09:51.000000 lama-cleaner-1.1.1/lama_cleaner/model/opencv2.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2934 2023-03-01 13:56:56.000000 lama-cleaner-1.1.1/lama_cleaner/model/paint_by_example.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.757203 lama-cleaner-1.1.1/lama_cleaner/model/pipeline/
+-rw-r--r--   0 cwq        (501) staff       (20)      108 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model/pipeline/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)    28149 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model/pipeline/pipeline_stable_diffusion_controlnet_inpaint.py
+-rw-r--r--   0 cwq        (501) staff       (20)    11851 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/model/plms_sampler.py
+-rw-r--r--   0 cwq        (501) staff       (20)     6642 2023-04-03 14:39:48.000000 lama-cleaner-1.1.1/lama_cleaner/model/sd.py
+-rw-r--r--   0 cwq        (501) staff       (20)    33811 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model/utils.py
+-rw-r--r--   0 cwq        (501) staff       (20)    15395 2023-02-27 13:02:16.000000 lama-cleaner-1.1.1/lama_cleaner/model/zits.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2497 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/model_manager.py
+-rw-r--r--   0 cwq        (501) staff       (20)     8313 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/parse_args.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.771414 lama-cleaner-1.1.1/lama_cleaner/plugins/
+-rw-r--r--   0 cwq        (501) staff       (20)      231 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)      280 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/base_plugin.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2400 2023-04-03 05:14:59.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/gfpgan_plugin.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2750 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/gfpganer.py
+-rw-r--r--   0 cwq        (501) staff       (20)     4156 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/gif.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2555 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/interactive_seg.py
+-rw-r--r--   0 cwq        (501) staff       (20)     3573 2023-04-03 05:31:35.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/realesrgan.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1018 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/remove_bg.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1747 2023-04-03 05:15:02.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/restoreformer.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.771901 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/
+-rw-r--r--   0 cwq        (501) staff       (20)      363 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2929 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/build_sam.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.773051 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/
+-rw-r--r--   0 cwq        (501) staff       (20)      385 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1479 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/common.py
+-rw-r--r--   0 cwq        (501) staff       (20)    14407 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/image_encoder.py
+-rw-r--r--   0 cwq        (501) staff       (20)     6614 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/mask_decoder.py
+-rw-r--r--   0 cwq        (501) staff       (20)     8594 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/prompt_encoder.py
+-rw-r--r--   0 cwq        (501) staff       (20)     7225 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/sam.py
+-rw-r--r--   0 cwq        (501) staff       (20)     8396 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/transformer.py
+-rw-r--r--   0 cwq        (501) staff       (20)    11837 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/predictor.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.773359 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/utils/
+-rw-r--r--   0 cwq        (501) staff       (20)      197 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/utils/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)     4054 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/utils/transforms.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1309 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/runtime.py
+-rw-r--r--   0 cwq        (501) staff       (20)     3306 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/schema.py
+-rw-r--r--   0 cwq        (501) staff       (20)    17556 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/server.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.774636 lama-cleaner-1.1.1/lama_cleaner/tests/
+-rw-r--r--   0 cwq        (501) staff       (20)        0 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/tests/__init__.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2951 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_controlnet.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2320 2023-02-14 05:56:20.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_instruct_pix2pix.py
+-rw-r--r--   0 cwq        (501) staff       (20)      596 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_load_img.py
+-rw-r--r--   0 cwq        (501) staff       (20)     5826 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_model.py
+-rw-r--r--   0 cwq        (501) staff       (20)     1491 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_model_md5.py
+-rw-r--r--   0 cwq        (501) staff       (20)     3985 2023-02-05 13:09:10.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_paint_by_example.py
+-rw-r--r--   0 cwq        (501) staff       (20)     2631 2023-04-06 14:12:49.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_plugins.py
+-rw-r--r--   0 cwq        (501) staff       (20)      875 2023-02-08 03:34:52.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_save_exif.py
+-rw-r--r--   0 cwq        (501) staff       (20)     7647 2023-04-02 07:46:39.000000 lama-cleaner-1.1.1/lama_cleaner/tests/test_sd_model.py
+-rw-r--r--   0 cwq        (501) staff       (20)     7330 2023-04-03 15:00:04.000000 lama-cleaner-1.1.1/lama_cleaner/web_config.py
+drwxr-xr-x   0 cwq        (501) staff       (20)        0 2023-04-06 14:56:34.752039 lama-cleaner-1.1.1/lama_cleaner.egg-info/
+-rw-r--r--   0 cwq        (501) staff       (20)     4640 2023-04-06 14:56:34.000000 lama-cleaner-1.1.1/lama_cleaner.egg-info/PKG-INFO
+-rw-r--r--   0 cwq        (501) staff       (20)     3287 2023-04-06 14:56:34.000000 lama-cleaner-1.1.1/lama_cleaner.egg-info/SOURCES.txt
+-rw-r--r--   0 cwq        (501) staff       (20)        1 2023-04-06 14:56:34.000000 lama-cleaner-1.1.1/lama_cleaner.egg-info/dependency_links.txt
+-rw-r--r--   0 cwq        (501) staff       (20)       59 2023-04-06 14:56:34.000000 lama-cleaner-1.1.1/lama_cleaner.egg-info/entry_points.txt
+-rw-r--r--   0 cwq        (501) staff       (20)      251 2023-04-06 14:56:34.000000 lama-cleaner-1.1.1/lama_cleaner.egg-info/requires.txt
+-rw-r--r--   0 cwq        (501) staff       (20)       13 2023-04-06 14:56:34.000000 lama-cleaner-1.1.1/lama_cleaner.egg-info/top_level.txt
+-rw-r--r--   0 cwq        (501) staff       (20)       38 2023-04-06 14:56:34.775045 lama-cleaner-1.1.1/setup.cfg
+-rw-r--r--   0 cwq        (501) staff       (20)     1616 2023-04-06 14:56:14.000000 lama-cleaner-1.1.1/setup.py
```

### Comparing `lama-cleaner-1.1.0/LICENSE` & `lama-cleaner-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/PKG-INFO` & `lama-cleaner-1.1.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lama-cleaner
-Version: 1.1.0
+Version: 1.1.1
 Summary: Image inpainting tool powered by SOTA AI Model
 Home-page: https://github.com/Sanster/lama-cleaner
 Author: PanicByte
 Author-email: cwq1913@gmail.com
 License: UNKNOWN
 Description: <h1 align="center">Lama Cleaner</h1>
         <p align="center">A free and open-source inpainting tool powered by SOTA AI model.</p>
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: lama-cleaner Version: 1.1.0 Summary: Image
+Metadata-Version: 2.1 Name: lama-cleaner Version: 1.1.1 Summary: Image
 inpainting tool powered by SOTA AI Model Home-page: https://github.com/Sanster/
 lama-cleaner Author: PanicByte Author-email: cwq1913@gmail.com License: UNKNOWN
 Description:
                           ****** Lama Cleaner ******
        A free and open-source inpainting tool powered by SOTA AI model.
    [total_download] [version] [Open_in_Colab] [Hugging_Face_Spaces] [python
                               version] [version]
```

### Comparing `lama-cleaner-1.1.0/README.md` & `lama-cleaner-1.1.1/README.md`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/asset-manifest.json` & `lama-cleaner-1.1.1/lama_cleaner/app/build/asset-manifest.json`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/index.html` & `lama-cleaner-1.1.1/lama_cleaner/app/build/index.html`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/css/main.6ca672e8.css` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/css/main.6ca672e8.css`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/js/main.44aac645.js` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/js/main.44aac645.js`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/js/main.44aac645.js.LICENSE.txt` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/js/main.44aac645.js.LICENSE.txt`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-Black.67c2c5a144333953880b.ttf` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-Black.67c2c5a144333953880b.ttf`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-Bold.2bea7a7f7d052c74da25.ttf` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-Bold.2bea7a7f7d052c74da25.ttf`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-Regular.bb287b894b27372d8ea7.ttf` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-Regular.bb287b894b27372d8ea7.ttf`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/WorkSans-SemiBold.1e98db4eb705b586728e.ttf` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/WorkSans-SemiBold.1e98db4eb705b586728e.ttf`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/app/build/static/media/coffee-machine-lineal.ee32631219cc3986f861.gif` & `lama-cleaner-1.1.1/lama_cleaner/app/build/static/media/coffee-machine-lineal.ee32631219cc3986f861.gif`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/benchmark.py` & `lama-cleaner-1.1.1/lama_cleaner/benchmark.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/const.py` & `lama-cleaner-1.1.1/lama_cleaner/const.py`

 * *Files 2% similar despite different names*

```diff
@@ -136,18 +136,21 @@
     enable_xformers: bool = False
     local_files_only: bool = False
     model_dir: str = DEFAULT_MODEL_DIR
     input: str = None
     output_dir: str = None
     # plugins
     enable_interactive_seg: bool = False
+    interactive_seg_model: str = "vit_l"
+    interactive_seg_device: str = "cuda"
     enable_remove_bg: bool = False
     enable_realesrgan: bool = False
     realesrgan_device: str = "cpu"
     realesrgan_model: str = RealESRGANModelName.realesr_general_x4v3.value
+    realesrgan_no_half: bool = False
     enable_gfpgan: bool = False
     gfpgan_device: str = "cpu"
     enable_restoreformer: bool = False
     restoreformer_device: str = "cpu"
     enable_gif: bool = False
```

### Comparing `lama-cleaner-1.1.0/lama_cleaner/file_manager/file_manager.py` & `lama-cleaner-1.1.1/lama_cleaner/file_manager/file_manager.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/file_manager/storage_backends.py` & `lama-cleaner-1.1.1/lama_cleaner/file_manager/storage_backends.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/file_manager/utils.py` & `lama-cleaner-1.1.1/lama_cleaner/file_manager/utils.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/helper.py` & `lama-cleaner-1.1.1/lama_cleaner/helper.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/base.py` & `lama-cleaner-1.1.1/lama_cleaner/model/base.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/controlnet.py` & `lama-cleaner-1.1.1/lama_cleaner/model/controlnet.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/ddim_sampler.py` & `lama-cleaner-1.1.1/lama_cleaner/model/ddim_sampler.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/fcf.py` & `lama-cleaner-1.1.1/lama_cleaner/model/fcf.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/instruct_pix2pix.py` & `lama-cleaner-1.1.1/lama_cleaner/model/instruct_pix2pix.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/lama.py` & `lama-cleaner-1.1.1/lama_cleaner/model/lama.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/ldm.py` & `lama-cleaner-1.1.1/lama_cleaner/model/ldm.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/manga.py` & `lama-cleaner-1.1.1/lama_cleaner/model/manga.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/mat.py` & `lama-cleaner-1.1.1/lama_cleaner/model/mat.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/opencv2.py` & `lama-cleaner-1.1.1/lama_cleaner/model/opencv2.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/paint_by_example.py` & `lama-cleaner-1.1.1/lama_cleaner/model/paint_by_example.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/pipeline/pipeline_stable_diffusion_controlnet_inpaint.py` & `lama-cleaner-1.1.1/lama_cleaner/model/pipeline/pipeline_stable_diffusion_controlnet_inpaint.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/plms_sampler.py` & `lama-cleaner-1.1.1/lama_cleaner/model/plms_sampler.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/sd.py` & `lama-cleaner-1.1.1/lama_cleaner/model/sd.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/utils.py` & `lama-cleaner-1.1.1/lama_cleaner/model/utils.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model/zits.py` & `lama-cleaner-1.1.1/lama_cleaner/model/zits.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/model_manager.py` & `lama-cleaner-1.1.1/lama_cleaner/model_manager.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/parse_args.py` & `lama-cleaner-1.1.1/lama_cleaner/parse_args.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/gfpgan_plugin.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/gfpgan_plugin.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/gfpganer.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/gfpganer.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/gif.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/gif.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/interactive_seg.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/interactive_seg.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/realesrgan.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/realesrgan.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/remove_bg.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/remove_bg.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/restoreformer.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/restoreformer.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/build_sam.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/build_sam.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/common.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/common.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/image_encoder.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/image_encoder.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/mask_decoder.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/mask_decoder.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/prompt_encoder.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/prompt_encoder.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/sam.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/sam.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/modeling/transformer.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/modeling/transformer.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/predictor.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/predictor.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/plugins/segment_anything/utils/transforms.py` & `lama-cleaner-1.1.1/lama_cleaner/plugins/segment_anything/utils/transforms.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/runtime.py` & `lama-cleaner-1.1.1/lama_cleaner/runtime.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/schema.py` & `lama-cleaner-1.1.1/lama_cleaner/schema.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/server.py` & `lama-cleaner-1.1.1/lama_cleaner/server.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_controlnet.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_controlnet.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_instruct_pix2pix.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_instruct_pix2pix.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_load_img.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_load_img.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_model.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_model.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_model_md5.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_model_md5.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_paint_by_example.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_paint_by_example.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_plugins.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_plugins.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_save_exif.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_save_exif.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/tests/test_sd_model.py` & `lama-cleaner-1.1.1/lama_cleaner/tests/test_sd_model.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner/web_config.py` & `lama-cleaner-1.1.1/lama_cleaner/web_config.py`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/lama_cleaner.egg-info/PKG-INFO` & `lama-cleaner-1.1.1/lama_cleaner.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lama-cleaner
-Version: 1.1.0
+Version: 1.1.1
 Summary: Image inpainting tool powered by SOTA AI Model
 Home-page: https://github.com/Sanster/lama-cleaner
 Author: PanicByte
 Author-email: cwq1913@gmail.com
 License: UNKNOWN
 Description: <h1 align="center">Lama Cleaner</h1>
         <p align="center">A free and open-source inpainting tool powered by SOTA AI model.</p>
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: lama-cleaner Version: 1.1.0 Summary: Image
+Metadata-Version: 2.1 Name: lama-cleaner Version: 1.1.1 Summary: Image
 inpainting tool powered by SOTA AI Model Home-page: https://github.com/Sanster/
 lama-cleaner Author: PanicByte Author-email: cwq1913@gmail.com License: UNKNOWN
 Description:
                           ****** Lama Cleaner ******
        A free and open-source inpainting tool powered by SOTA AI model.
    [total_download] [version] [Open_in_Colab] [Hugging_Face_Spaces] [python
                               version] [version]
```

### Comparing `lama-cleaner-1.1.0/lama_cleaner.egg-info/SOURCES.txt` & `lama-cleaner-1.1.1/lama_cleaner.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `lama-cleaner-1.1.0/setup.py` & `lama-cleaner-1.1.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -17,15 +17,15 @@
                 requires.append(line.strip())
     return requires
 
 
 # https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
 setuptools.setup(
     name="lama-cleaner",
-    version="1.1.0",
+    version="1.1.1",
     author="PanicByte",
     author_email="cwq1913@gmail.com",
     description="Image inpainting tool powered by SOTA AI Model",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/Sanster/lama-cleaner",
     packages=setuptools.find_packages("./"),
```

