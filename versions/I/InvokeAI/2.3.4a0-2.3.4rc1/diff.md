# Comparing `tmp/InvokeAI-2.3.4a0.tar.gz` & `tmp/InvokeAI-2.3.4rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "InvokeAI-2.3.4a0.tar", last modified: Fri Apr  7 13:38:03 2023, max compression
+gzip compressed data, was "InvokeAI-2.3.4rc1.tar", last modified: Fri Apr  7 13:55:24 2023, max compression
```

## Comparing `InvokeAI-2.3.4a0.tar` & `InvokeAI-2.3.4rc1.tar`

### file list

```diff
@@ -1,176 +1,176 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.748760 InvokeAI-2.3.4a0/InvokeAI.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    13893 2023-04-07 13:38:03.000000 InvokeAI-2.3.4a0/InvokeAI.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4914 2023-04-07 13:38:03.000000 InvokeAI-2.3.4a0/InvokeAI.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:38:03.000000 InvokeAI-2.3.4a0/InvokeAI.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-07 13:38:03.000000 InvokeAI-2.3.4a0/InvokeAI.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1145 2023-04-07 13:38:03.000000 InvokeAI-2.3.4a0/InvokeAI.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-07 13:38:03.000000 InvokeAI-2.3.4a0/InvokeAI.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-07 13:37:50.000000 InvokeAI-2.3.4a0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    13893 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    12064 2023-04-07 13:37:50.000000 InvokeAI-2.3.4a0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.744760 InvokeAI-2.3.4a0/invokeai/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.744760 InvokeAI-2.3.4a0/invokeai/assets/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.748760 InvokeAI-2.3.4a0/invokeai/assets/web/
--rw-r--r--   0 runner    (1001) docker     (123)    34023 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/assets/web/caution.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.748760 InvokeAI-2.3.4a0/invokeai/backend/
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    70840 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/invoke_ai_web_server.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.748760 InvokeAI-2.3.4a0/invokeai/backend/modules/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/modules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/modules/create_cmd_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/modules/get_canvas_generation_mode.py
--rw-r--r--   0 runner    (1001) docker     (123)     2703 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/modules/parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/backend/modules/parse_seed_weights.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.748760 InvokeAI-2.3.4a0/invokeai/configs/
--rw-r--r--   0 runner    (1001) docker     (123)     3224 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/INITIAL_MODELS.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1791 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/models.yaml.example
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.752760 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)     2631 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-finetune.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-finetune_style.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     2159 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-inference.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     2277 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-inpainting-inference.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     2629 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-m1-finetune.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1815 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v2-inference-v.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v2-inference.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.744760 InvokeAI-2.3.4a0/invokeai/frontend/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.752760 InvokeAI-2.3.4a0/invokeai/frontend/dist/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.756760 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/
--rw-r--r--   0 runner    (1001) docker     (123)   316100 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/Inter-Bold-790c108b.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   803384 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/Inter-b9a8e5e2.ttf
--rw-r--r--   0 runner    (1001) docker     (123)   118734 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/favicon-0d253ced.ico
--rw-r--r--   0 runner    (1001) docker     (123)    51474 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/index-2ab0eb58.css
--rw-r--r--   0 runner    (1001) docker     (123)  1546305 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/index-c1535364.js
--rw-r--r--   0 runner    (1001) docker     (123)    44115 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/logo-13003d72.png
--rw-r--r--   0 runner    (1001) docker     (123)      500 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/index.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.756760 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/
--rw-r--r--   0 runner    (1001) docker     (123)    31098 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ar.json
--rw-r--r--   0 runner    (1001) docker     (123)    25051 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/de.json
--rw-r--r--   0 runner    (1001) docker     (123)    27833 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/en.json
--rw-r--r--   0 runner    (1001) docker     (123)    31063 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/es.json
--rw-r--r--   0 runner    (1001) docker     (123)    27064 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/fr.json
--rw-r--r--   0 runner    (1001) docker     (123)    31035 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/it.json
--rw-r--r--   0 runner    (1001) docker     (123)    22216 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ja.json
--rw-r--r--   0 runner    (1001) docker     (123)    24978 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/nl.json
--rw-r--r--   0 runner    (1001) docker     (123)    22222 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/pl.json
--rw-r--r--   0 runner    (1001) docker     (123)    25471 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/pt_BR.json
--rw-r--r--   0 runner    (1001) docker     (123)        3 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ro.json
--rw-r--r--   0 runner    (1001) docker     (123)    33418 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ru.json
--rw-r--r--   0 runner    (1001) docker     (123)    33231 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/uk.json
--rw-r--r--   0 runner    (1001) docker     (123)    19769 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/zh_CN.json
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.760760 InvokeAI-2.3.4a0/ldm/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.760760 InvokeAI-2.3.4a0/ldm/data/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      738 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/data/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    16282 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/data/imagenet.py
--rw-r--r--   0 runner    (1001) docker     (123)     3497 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/data/lsun.py
--rw-r--r--   0 runner    (1001) docker     (123)     5546 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/data/personalized.py
--rw-r--r--   0 runner    (1001) docker     (123)     5002 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/data/personalized_style.py
--rw-r--r--   0 runner    (1001) docker     (123)    54669 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/generate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.764760 InvokeAI-2.3.4a0/ldm/invoke/
--rw-r--r--   0 runner    (1001) docker     (123)    48345 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/CLI.py
--rw-r--r--   0 runner    (1001) docker     (123)      440 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)    51811 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/args.py
--rw-r--r--   0 runner    (1001) docker     (123)    50246 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/ckpt_to_diffuser.py
--rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/concepts_lib.py
--rw-r--r--   0 runner    (1001) docker     (123)    12166 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/conditioning.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.764760 InvokeAI-2.3.4a0/ldm/invoke/config/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/config/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    29449 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/config/invokeai_configure.py
--rw-r--r--   0 runner    (1001) docker     (123)     3215 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/config/invokeai_update.py
--rw-r--r--   0 runner    (1001) docker     (123)    18393 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/config/model_install.py
--rw-r--r--   0 runner    (1001) docker     (123)    17405 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/config/model_install_backend.py
--rw-r--r--   0 runner    (1001) docker     (123)     6100 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/config/widgets.py
--rw-r--r--   0 runner    (1001) docker     (123)     1960 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/devices.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    16316 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/dynamic_prompts.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.768760 InvokeAI-2.3.4a0/ldm/invoke/generator/
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15960 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    37004 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/diffusers_pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)    26074 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/embiggen.py
--rw-r--r--   0 runner    (1001) docker     (123)     2956 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/img2img.py
--rw-r--r--   0 runner    (1001) docker     (123)    12728 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/inpaint.py
--rw-r--r--   0 runner    (1001) docker     (123)     6493 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/omnibus.py
--rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/txt2img.py
--rw-r--r--   0 runner    (1001) docker     (123)     7334 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/generator/txt2img2img.py
--rw-r--r--   0 runner    (1001) docker     (123)     4174 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/globals.py
--rw-r--r--   0 runner    (1001) docker     (123)     2374 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/image_util.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      873 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/invokeai_metadata.py
--rw-r--r--   0 runner    (1001) docker     (123)     2392 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/log.py
--rw-r--r--   0 runner    (1001) docker     (123)    17330 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/merge_diffusers.py
--rw-r--r--   0 runner    (1001) docker     (123)    49953 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/model_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     7951 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/offloading.py
--rw-r--r--   0 runner    (1001) docker     (123)     1289 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/patchmatch.py
--rw-r--r--   0 runner    (1001) docker     (123)     4940 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/pngwriter.py
--rw-r--r--   0 runner    (1001) docker     (123)    15064 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/readline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.768760 InvokeAI-2.3.4a0/ldm/invoke/restoration/
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4473 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/codeformer.py
--rw-r--r--   0 runner    (1001) docker     (123)    10946 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/codeformer_arch.py
--rw-r--r--   0 runner    (1001) docker     (123)     2821 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/gfpgan.py
--rw-r--r--   0 runner    (1001) docker     (123)     4051 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/outcrop.py
--rw-r--r--   0 runner    (1001) docker     (123)     3543 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/outpaint.py
--rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/realesrgan.py
--rw-r--r--   0 runner    (1001) docker     (123)    15435 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/restoration/vqgan_arch.py
--rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/seamless.py
--rw-r--r--   0 runner    (1001) docker     (123)    12606 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/server.py
--rw-r--r--   0 runner    (1001) docker     (123)    11263 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/server_legacy.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.768760 InvokeAI-2.3.4a0/ldm/invoke/training/
--rwxr-xr-x   0 runner    (1001) docker     (123)    15779 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/training/textual_inversion.py
--rw-r--r--   0 runner    (1001) docker     (123)    35879 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/training/textual_inversion_training.py
--rw-r--r--   0 runner    (1001) docker     (123)     5147 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/invoke/txt2mask.py
--rw-r--r--   0 runner    (1001) docker     (123)     4373 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/lr_scheduler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.772760 InvokeAI-2.3.4a0/ldm/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18770 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/autoencoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.772760 InvokeAI-2.3.4a0/ldm/models/diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11323 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)    29556 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/cross_attention_control.py
--rw-r--r--   0 runner    (1001) docker     (123)     4006 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/cross_attention_map_saving.py
--rw-r--r--   0 runner    (1001) docker     (123)     4260 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/ddim.py
--rw-r--r--   0 runner    (1001) docker     (123)    81805 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/ddpm.py
--rw-r--r--   0 runner    (1001) docker     (123)    11474 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/ksampler.py
--rw-r--r--   0 runner    (1001) docker     (123)     5731 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/plms.py
--rw-r--r--   0 runner    (1001) docker     (123)    15537 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/sampler.py
--rw-r--r--   0 runner    (1001) docker     (123)    26580 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/models/diffusion/shared_invokeai_diffusion.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.772760 InvokeAI-2.3.4a0/ldm/modules/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9038 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/attention.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    35512 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/model.py
--rw-r--r--   0 runner    (1001) docker     (123)    36213 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/openaimodel.py
--rw-r--r--   0 runner    (1001) docker     (123)    10086 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/ldm/modules/distributions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/distributions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3119 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/distributions/distributions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3180 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/ema.py
--rw-r--r--   0 runner    (1001) docker     (123)    14629 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/embedding_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/ldm/modules/encoders/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/encoders/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    30982 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/encoders/modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/ldm/modules/image_degradation/
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/image_degradation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    26558 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/image_degradation/bsrgan.py
--rw-r--r--   0 runner    (1001) docker     (123)    23359 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/image_degradation/bsrgan_light.py
--rw-r--r--   0 runner    (1001) docker     (123)    30058 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/image_degradation/utils_image.py
--rw-r--r--   0 runner    (1001) docker     (123)    12986 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/kohya_lora_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/lora_manager.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/ldm/modules/losses/
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6282 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/losses/contperceptual.py
--rw-r--r--   0 runner    (1001) docker     (123)     8654 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/losses/vqperceptual.py
--rw-r--r--   0 runner    (1001) docker     (123)     3211 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/peft_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    18635 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/textual_inversion_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    21561 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/modules/x_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)      363 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/simplet2i.py
--rw-r--r--   0 runner    (1001) docker     (123)    11287 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/ldm/util.py
--rw-r--r--   0 runner    (1001) docker     (123)     5161 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:38:03.776760 InvokeAI-2.3.4a0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/tests/test_path.py
--rw-r--r--   0 runner    (1001) docker     (123)    15280 2023-04-07 13:37:51.000000 InvokeAI-2.3.4a0/tests/test_textual_inversion.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.530587 InvokeAI-2.3.4rc1/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.482587 InvokeAI-2.3.4rc1/InvokeAI.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    13894 2023-04-07 13:55:24.000000 InvokeAI-2.3.4rc1/InvokeAI.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4914 2023-04-07 13:55:24.000000 InvokeAI-2.3.4rc1/InvokeAI.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:55:24.000000 InvokeAI-2.3.4rc1/InvokeAI.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-07 13:55:24.000000 InvokeAI-2.3.4rc1/InvokeAI.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1145 2023-04-07 13:55:24.000000 InvokeAI-2.3.4rc1/InvokeAI.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-07 13:55:24.000000 InvokeAI-2.3.4rc1/InvokeAI.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    13894 2023-04-07 13:55:24.530587 InvokeAI-2.3.4rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    12064 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.470587 InvokeAI-2.3.4rc1/invokeai/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.470587 InvokeAI-2.3.4rc1/invokeai/assets/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.482587 InvokeAI-2.3.4rc1/invokeai/assets/web/
+-rw-r--r--   0 runner    (1001) docker     (123)    34023 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/assets/web/caution.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.482587 InvokeAI-2.3.4rc1/invokeai/backend/
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    70840 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/invoke_ai_web_server.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.486587 InvokeAI-2.3.4rc1/invokeai/backend/modules/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/modules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/modules/create_cmd_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/modules/get_canvas_generation_mode.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2703 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/modules/parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1224 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/backend/modules/parse_seed_weights.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.486587 InvokeAI-2.3.4rc1/invokeai/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)     3224 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/INITIAL_MODELS.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1791 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/models.yaml.example
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.490587 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)     2631 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-finetune.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-finetune_style.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     2159 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-inference.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     2277 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-inpainting-inference.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     2629 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-m1-finetune.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1815 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v2-inference-v.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1789 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v2-inference.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.470587 InvokeAI-2.3.4rc1/invokeai/frontend/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.490587 InvokeAI-2.3.4rc1/invokeai/frontend/dist/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.494587 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/
+-rw-r--r--   0 runner    (1001) docker     (123)   316100 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/Inter-Bold-790c108b.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   803384 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/Inter-b9a8e5e2.ttf
+-rw-r--r--   0 runner    (1001) docker     (123)   118734 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/favicon-0d253ced.ico
+-rw-r--r--   0 runner    (1001) docker     (123)    51474 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/index-2ab0eb58.css
+-rw-r--r--   0 runner    (1001) docker     (123)  1546305 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/index-c1535364.js
+-rw-r--r--   0 runner    (1001) docker     (123)    44115 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/logo-13003d72.png
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/index.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.498587 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/
+-rw-r--r--   0 runner    (1001) docker     (123)    31098 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ar.json
+-rw-r--r--   0 runner    (1001) docker     (123)    25051 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/de.json
+-rw-r--r--   0 runner    (1001) docker     (123)    27833 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/en.json
+-rw-r--r--   0 runner    (1001) docker     (123)    31063 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/es.json
+-rw-r--r--   0 runner    (1001) docker     (123)    27064 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/fr.json
+-rw-r--r--   0 runner    (1001) docker     (123)    31035 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/it.json
+-rw-r--r--   0 runner    (1001) docker     (123)    22216 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ja.json
+-rw-r--r--   0 runner    (1001) docker     (123)    24978 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/nl.json
+-rw-r--r--   0 runner    (1001) docker     (123)    22222 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/pl.json
+-rw-r--r--   0 runner    (1001) docker     (123)    25471 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/pt_BR.json
+-rw-r--r--   0 runner    (1001) docker     (123)        3 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ro.json
+-rw-r--r--   0 runner    (1001) docker     (123)    33418 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ru.json
+-rw-r--r--   0 runner    (1001) docker     (123)    33231 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/uk.json
+-rw-r--r--   0 runner    (1001) docker     (123)    19769 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/zh_CN.json
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.502587 InvokeAI-2.3.4rc1/ldm/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.502587 InvokeAI-2.3.4rc1/ldm/data/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      738 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/data/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16282 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/data/imagenet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3497 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/data/lsun.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5546 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/data/personalized.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5002 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/data/personalized_style.py
+-rw-r--r--   0 runner    (1001) docker     (123)    54669 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/generate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.510587 InvokeAI-2.3.4rc1/ldm/invoke/
+-rw-r--r--   0 runner    (1001) docker     (123)    48345 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/CLI.py
+-rw-r--r--   0 runner    (1001) docker     (123)      440 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    51811 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/args.py
+-rw-r--r--   0 runner    (1001) docker     (123)    50246 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/ckpt_to_diffuser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9734 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/concepts_lib.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12166 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/conditioning.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.510587 InvokeAI-2.3.4rc1/ldm/invoke/config/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/config/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    29449 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/config/invokeai_configure.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3215 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/config/invokeai_update.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18393 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/config/model_install.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17405 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/config/model_install_backend.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6100 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/config/widgets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1960 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/devices.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    16316 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/dynamic_prompts.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.510587 InvokeAI-2.3.4rc1/ldm/invoke/generator/
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15960 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37004 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/diffusers_pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26074 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/embiggen.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2956 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/img2img.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12728 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/inpaint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6493 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/omnibus.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/txt2img.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7334 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/generator/txt2img2img.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4174 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/globals.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2374 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/image_util.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      873 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/invokeai_metadata.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2392 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/log.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17330 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/merge_diffusers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    49953 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/model_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7951 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/offloading.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1289 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/patchmatch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4940 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/pngwriter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15064 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/readline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.514587 InvokeAI-2.3.4rc1/ldm/invoke/restoration/
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1234 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4473 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/codeformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10946 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/codeformer_arch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2821 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/gfpgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4051 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/outcrop.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3543 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/outpaint.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/realesrgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15435 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/restoration/vqgan_arch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1871 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/seamless.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12606 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/server.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11263 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/server_legacy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.514587 InvokeAI-2.3.4rc1/ldm/invoke/training/
+-rwxr-xr-x   0 runner    (1001) docker     (123)    15779 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/training/textual_inversion.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35879 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/training/textual_inversion_training.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5147 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/invoke/txt2mask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4373 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/lr_scheduler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.514587 InvokeAI-2.3.4rc1/ldm/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18770 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/autoencoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.518587 InvokeAI-2.3.4rc1/ldm/models/diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11323 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/classifier.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29556 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/cross_attention_control.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4006 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/cross_attention_map_saving.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4260 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/ddim.py
+-rw-r--r--   0 runner    (1001) docker     (123)    81805 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/ddpm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11474 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/ksampler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5731 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/plms.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15537 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/sampler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26580 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/models/diffusion/shared_invokeai_diffusion.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.522587 InvokeAI-2.3.4rc1/ldm/modules/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9038 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/attention.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.522587 InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35512 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36213 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/openaimodel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10086 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.526587 InvokeAI-2.3.4rc1/ldm/modules/distributions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/distributions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3119 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/distributions/distributions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3180 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/ema.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14629 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/embedding_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.526587 InvokeAI-2.3.4rc1/ldm/modules/encoders/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/encoders/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30982 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/encoders/modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.526587 InvokeAI-2.3.4rc1/ldm/modules/image_degradation/
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/image_degradation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26558 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/image_degradation/bsrgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23359 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/image_degradation/bsrgan_light.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30058 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/image_degradation/utils_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12986 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/kohya_lora_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2338 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/lora_manager.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.526587 InvokeAI-2.3.4rc1/ldm/modules/losses/
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6282 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/losses/contperceptual.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8654 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/losses/vqperceptual.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3211 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/peft_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18635 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/textual_inversion_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21561 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/modules/x_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      363 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/simplet2i.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11287 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/ldm/util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5161 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 13:55:24.530587 InvokeAI-2.3.4rc1/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:55:24.526587 InvokeAI-2.3.4rc1/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1546 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/tests/test_path.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15280 2023-04-07 13:55:08.000000 InvokeAI-2.3.4rc1/tests/test_textual_inversion.py
```

### Comparing `InvokeAI-2.3.4a0/InvokeAI.egg-info/PKG-INFO` & `InvokeAI-2.3.4rc1/InvokeAI.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: InvokeAI
-Version: 2.3.4a0
+Version: 2.3.4rc1
 Summary: An implementation of Stable Diffusion which provides various new features and options to aid the image generation process
 Author-email: The InvokeAI Project <lincoln.stein@gmail.com>
 License: MIT
 Project-URL: Bug Reports, https://github.com/invoke-ai/InvokeAI/issues
 Project-URL: Discord, https://discord.gg/ZmtBAhwWhy
 Project-URL: Documentation, https://invoke-ai.github.io/InvokeAI/
 Project-URL: Homepage, https://invoke-ai.github.io/InvokeAI/
```

### Comparing `InvokeAI-2.3.4a0/InvokeAI.egg-info/SOURCES.txt` & `InvokeAI-2.3.4rc1/InvokeAI.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/InvokeAI.egg-info/entry_points.txt` & `InvokeAI-2.3.4rc1/InvokeAI.egg-info/entry_points.txt`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/InvokeAI.egg-info/requires.txt` & `InvokeAI-2.3.4rc1/InvokeAI.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/LICENSE` & `InvokeAI-2.3.4rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/PKG-INFO` & `InvokeAI-2.3.4rc1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: InvokeAI
-Version: 2.3.4a0
+Version: 2.3.4rc1
 Summary: An implementation of Stable Diffusion which provides various new features and options to aid the image generation process
 Author-email: The InvokeAI Project <lincoln.stein@gmail.com>
 License: MIT
 Project-URL: Bug Reports, https://github.com/invoke-ai/InvokeAI/issues
 Project-URL: Discord, https://discord.gg/ZmtBAhwWhy
 Project-URL: Documentation, https://invoke-ai.github.io/InvokeAI/
 Project-URL: Homepage, https://invoke-ai.github.io/InvokeAI/
```

### Comparing `InvokeAI-2.3.4a0/README.md` & `InvokeAI-2.3.4rc1/README.md`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/assets/web/caution.png` & `InvokeAI-2.3.4rc1/invokeai/assets/web/caution.png`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/backend/invoke_ai_web_server.py` & `InvokeAI-2.3.4rc1/invokeai/backend/invoke_ai_web_server.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/backend/modules/create_cmd_parser.py` & `InvokeAI-2.3.4rc1/invokeai/backend/modules/create_cmd_parser.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/backend/modules/get_canvas_generation_mode.py` & `InvokeAI-2.3.4rc1/invokeai/backend/modules/get_canvas_generation_mode.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/backend/modules/parameters.py` & `InvokeAI-2.3.4rc1/invokeai/backend/modules/parameters.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/backend/modules/parse_seed_weights.py` & `InvokeAI-2.3.4rc1/invokeai/backend/modules/parse_seed_weights.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/INITIAL_MODELS.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/INITIAL_MODELS.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/models.yaml.example` & `InvokeAI-2.3.4rc1/invokeai/configs/models.yaml.example`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-finetune.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-finetune.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-finetune_style.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-finetune_style.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-inference.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-inference.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-inpainting-inference.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-inpainting-inference.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v1-m1-finetune.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v1-m1-finetune.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v2-inference-v.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v2-inference-v.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/configs/stable-diffusion/v2-inference.yaml` & `InvokeAI-2.3.4rc1/invokeai/configs/stable-diffusion/v2-inference.yaml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/Inter-Bold-790c108b.ttf` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/Inter-Bold-790c108b.ttf`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/Inter-b9a8e5e2.ttf` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/Inter-b9a8e5e2.ttf`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/favicon-0d253ced.ico` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/favicon-0d253ced.ico`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/index-2ab0eb58.css` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/index-2ab0eb58.css`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/index-c1535364.js` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/index-c1535364.js`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/assets/logo-13003d72.png` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/assets/logo-13003d72.png`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ar.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ar.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/de.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/de.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/en.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/en.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/es.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/es.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/fr.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/fr.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/it.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/it.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ja.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ja.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/nl.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/nl.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/pl.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/pl.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/pt_BR.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/pt_BR.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/ru.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/ru.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/uk.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/uk.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/invokeai/frontend/dist/locales/zh_CN.json` & `InvokeAI-2.3.4rc1/invokeai/frontend/dist/locales/zh_CN.json`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/data/base.py` & `InvokeAI-2.3.4rc1/ldm/data/base.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/data/imagenet.py` & `InvokeAI-2.3.4rc1/ldm/data/imagenet.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/data/lsun.py` & `InvokeAI-2.3.4rc1/ldm/data/lsun.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/data/personalized.py` & `InvokeAI-2.3.4rc1/ldm/data/personalized.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/data/personalized_style.py` & `InvokeAI-2.3.4rc1/ldm/data/personalized_style.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/generate.py` & `InvokeAI-2.3.4rc1/ldm/generate.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/CLI.py` & `InvokeAI-2.3.4rc1/ldm/invoke/CLI.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/args.py` & `InvokeAI-2.3.4rc1/ldm/invoke/args.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/ckpt_to_diffuser.py` & `InvokeAI-2.3.4rc1/ldm/invoke/ckpt_to_diffuser.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/concepts_lib.py` & `InvokeAI-2.3.4rc1/ldm/invoke/concepts_lib.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/conditioning.py` & `InvokeAI-2.3.4rc1/ldm/invoke/conditioning.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/config/invokeai_configure.py` & `InvokeAI-2.3.4rc1/ldm/invoke/config/invokeai_configure.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/config/invokeai_update.py` & `InvokeAI-2.3.4rc1/ldm/invoke/config/invokeai_update.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/config/model_install.py` & `InvokeAI-2.3.4rc1/ldm/invoke/config/model_install.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/config/model_install_backend.py` & `InvokeAI-2.3.4rc1/ldm/invoke/config/model_install_backend.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/config/widgets.py` & `InvokeAI-2.3.4rc1/ldm/invoke/config/widgets.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/devices.py` & `InvokeAI-2.3.4rc1/ldm/invoke/devices.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/dynamic_prompts.py` & `InvokeAI-2.3.4rc1/ldm/invoke/dynamic_prompts.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/base.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/base.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/diffusers_pipeline.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/diffusers_pipeline.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/embiggen.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/embiggen.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/img2img.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/img2img.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/inpaint.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/inpaint.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/omnibus.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/omnibus.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/txt2img.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/txt2img.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/generator/txt2img2img.py` & `InvokeAI-2.3.4rc1/ldm/invoke/generator/txt2img2img.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/globals.py` & `InvokeAI-2.3.4rc1/ldm/invoke/globals.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/image_util.py` & `InvokeAI-2.3.4rc1/ldm/invoke/image_util.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/invokeai_metadata.py` & `InvokeAI-2.3.4rc1/ldm/invoke/invokeai_metadata.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/log.py` & `InvokeAI-2.3.4rc1/ldm/invoke/log.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/merge_diffusers.py` & `InvokeAI-2.3.4rc1/ldm/invoke/merge_diffusers.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/model_manager.py` & `InvokeAI-2.3.4rc1/ldm/invoke/model_manager.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/offloading.py` & `InvokeAI-2.3.4rc1/ldm/invoke/offloading.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/patchmatch.py` & `InvokeAI-2.3.4rc1/ldm/invoke/patchmatch.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/pngwriter.py` & `InvokeAI-2.3.4rc1/ldm/invoke/pngwriter.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/readline.py` & `InvokeAI-2.3.4rc1/ldm/invoke/readline.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/base.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/base.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/codeformer.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/codeformer.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/codeformer_arch.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/codeformer_arch.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/gfpgan.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/gfpgan.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/outcrop.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/outcrop.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/outpaint.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/outpaint.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/realesrgan.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/realesrgan.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/restoration/vqgan_arch.py` & `InvokeAI-2.3.4rc1/ldm/invoke/restoration/vqgan_arch.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/seamless.py` & `InvokeAI-2.3.4rc1/ldm/invoke/seamless.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/server.py` & `InvokeAI-2.3.4rc1/ldm/invoke/server.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/server_legacy.py` & `InvokeAI-2.3.4rc1/ldm/invoke/server_legacy.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/training/textual_inversion.py` & `InvokeAI-2.3.4rc1/ldm/invoke/training/textual_inversion.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/training/textual_inversion_training.py` & `InvokeAI-2.3.4rc1/ldm/invoke/training/textual_inversion_training.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/invoke/txt2mask.py` & `InvokeAI-2.3.4rc1/ldm/invoke/txt2mask.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/lr_scheduler.py` & `InvokeAI-2.3.4rc1/ldm/lr_scheduler.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/autoencoder.py` & `InvokeAI-2.3.4rc1/ldm/models/autoencoder.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/classifier.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/classifier.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/cross_attention_control.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/cross_attention_control.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/cross_attention_map_saving.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/cross_attention_map_saving.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/ddim.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/ddim.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/ddpm.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/ddpm.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/ksampler.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/ksampler.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/plms.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/plms.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/sampler.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/sampler.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/models/diffusion/shared_invokeai_diffusion.py` & `InvokeAI-2.3.4rc1/ldm/models/diffusion/shared_invokeai_diffusion.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/attention.py` & `InvokeAI-2.3.4rc1/ldm/modules/attention.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/model.py` & `InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/model.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/openaimodel.py` & `InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/openaimodel.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/diffusionmodules/util.py` & `InvokeAI-2.3.4rc1/ldm/modules/diffusionmodules/util.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/distributions/distributions.py` & `InvokeAI-2.3.4rc1/ldm/modules/distributions/distributions.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/ema.py` & `InvokeAI-2.3.4rc1/ldm/modules/ema.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/embedding_manager.py` & `InvokeAI-2.3.4rc1/ldm/modules/embedding_manager.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/encoders/modules.py` & `InvokeAI-2.3.4rc1/ldm/modules/encoders/modules.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/image_degradation/bsrgan.py` & `InvokeAI-2.3.4rc1/ldm/modules/image_degradation/bsrgan.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/image_degradation/bsrgan_light.py` & `InvokeAI-2.3.4rc1/ldm/modules/image_degradation/bsrgan_light.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/image_degradation/utils_image.py` & `InvokeAI-2.3.4rc1/ldm/modules/image_degradation/utils_image.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/kohya_lora_manager.py` & `InvokeAI-2.3.4rc1/ldm/modules/kohya_lora_manager.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/lora_manager.py` & `InvokeAI-2.3.4rc1/ldm/modules/lora_manager.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/losses/contperceptual.py` & `InvokeAI-2.3.4rc1/ldm/modules/losses/contperceptual.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/losses/vqperceptual.py` & `InvokeAI-2.3.4rc1/ldm/modules/losses/vqperceptual.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/peft_manager.py` & `InvokeAI-2.3.4rc1/ldm/modules/peft_manager.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/textual_inversion_manager.py` & `InvokeAI-2.3.4rc1/ldm/modules/textual_inversion_manager.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/modules/x_transformer.py` & `InvokeAI-2.3.4rc1/ldm/modules/x_transformer.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/ldm/util.py` & `InvokeAI-2.3.4rc1/ldm/util.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/pyproject.toml` & `InvokeAI-2.3.4rc1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/tests/test_path.py` & `InvokeAI-2.3.4rc1/tests/test_path.py`

 * *Files identical despite different names*

### Comparing `InvokeAI-2.3.4a0/tests/test_textual_inversion.py` & `InvokeAI-2.3.4rc1/tests/test_textual_inversion.py`

 * *Files identical despite different names*

