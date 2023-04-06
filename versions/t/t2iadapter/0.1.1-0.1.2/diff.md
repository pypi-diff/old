# Comparing `tmp/t2iadapter-0.1.1.tar.gz` & `tmp/t2iadapter-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\t2iadapter-0.1.1.tar", last modified: Mon Apr  3 03:30:05 2023, max compression
+gzip compressed data, was "dist\t2iadapter-0.1.2.tar", last modified: Thu Apr  6 13:14:12 2023, max compression
```

## Comparing `t2iadapter-0.1.1.tar` & `t2iadapter-0.1.2.tar`

### file list

```diff
@@ -1,90 +1,90 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.395957 t2iadapter-0.1.1/
--rw-rw-rw-   0        0        0      588 2023-04-03 03:30:05.395442 t2iadapter-0.1.1/PKG-INFO
--rw-rw-rw-   0        0        0    19580 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/README.md
--rw-rw-rw-   0        0        0       42 2023-04-03 03:30:05.395957 t2iadapter-0.1.1/setup.cfg
--rw-rw-rw-   0        0        0     3111 2023-03-27 06:58:25.000000 t2iadapter-0.1.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.265974 t2iadapter-0.1.1/t2iadapter/
--rw-rw-rw-   0        0        0       57 2023-03-27 12:25:37.000000 t2iadapter-0.1.1/t2iadapter/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.281709 t2iadapter-0.1.1/t2iadapter/adapters/
--rw-rw-rw-   0        0        0        0 2023-03-27 06:43:06.000000 t2iadapter-0.1.1/t2iadapter/adapters/__init__.py
--rw-rw-rw-   0        0        0     5644 2023-03-27 13:01:16.000000 t2iadapter-0.1.1/t2iadapter/adapters/coadapters.py
--rw-rw-rw-   0        0        0     1997 2023-03-27 09:19:12.000000 t2iadapter-0.1.1/t2iadapter/adapters/t2i_adapters_for_canny.py
--rw-rw-rw-   0        0        0     2801 2023-03-27 13:01:27.000000 t2iadapter-0.1.1/t2iadapter/adapters/t2i_adapters_for_style.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.290301 t2iadapter-0.1.1/t2iadapter/ldm/
--rw-rw-rw-   0        0        0       79 2023-03-27 12:26:15.000000 t2iadapter-0.1.1/t2iadapter/ldm/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.301515 t2iadapter-0.1.1/t2iadapter/ldm/data/
--rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/data/__init__.py
--rw-rw-rw-   0        0        0     1369 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_coco.py
--rw-rw-rw-   0        0        0     1173 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_depth.py
--rw-rw-rw-   0        0        0     5202 2023-03-27 09:14:57.000000 t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_laion.py
--rw-rw-rw-   0        0        0     2218 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_wikiart.py
--rw-rw-rw-   0        0        0     2986 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/data/utils.py
--rw-rw-rw-   0        0        0     8850 2023-03-27 12:49:35.000000 t2iadapter-0.1.1/t2iadapter/ldm/inference_base.py
--rw-rw-rw-   0        0        0     3980 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/lr_scheduler.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.305999 t2iadapter-0.1.1/t2iadapter/ldm/models/
--rw-rw-rw-   0        0        0       39 2023-03-27 12:26:24.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/__init__.py
--rw-rw-rw-   0        0        0     8511 2023-03-27 09:15:26.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/autoencoder.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.313866 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/
--rw-rw-rw-   0        0        0       40 2023-03-27 12:26:46.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/__init__.py
--rw-rw-rw-   0        0        0    15589 2023-03-27 09:15:24.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/ddim.py
--rw-rw-rw-   0        0        0    63203 2023-03-30 12:56:51.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/ddpm.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.320475 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/dpm_solver/
--rw-rw-rw-   0        0        0       37 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/dpm_solver/__init__.py
--rw-rw-rw-   0        0        0    67294 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/dpm_solver/dpm_solver.py
--rw-rw-rw-   0        0        0     3078 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/dpm_solver/sampler.py
--rw-rw-rw-   0        0        0    12977 2023-03-27 09:17:27.000000 t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/plms.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.326258 t2iadapter-0.1.1/t2iadapter/ldm/modules/
--rw-rw-rw-   0        0        0      163 2023-03-27 12:37:23.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/__init__.py
--rw-rw-rw-   0        0        0    11582 2023-03-27 09:15:52.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/attention.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.335971 t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/
--rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/__init__.py
--rw-rw-rw-   0        0        0    30906 2023-03-30 12:18:15.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/model.py
--rw-rw-rw-   0        0        0    31471 2023-03-27 09:17:52.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/openaimodel.py
--rw-rw-rw-   0        0        0    10071 2023-03-27 09:17:48.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/util.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.339876 t2iadapter-0.1.1/t2iadapter/ldm/modules/distributions/
--rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/distributions/__init__.py
--rw-rw-rw-   0        0        0     3062 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/distributions/distributions.py
--rw-rw-rw-   0        0        0     3190 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/ema.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.345130 t2iadapter-0.1.1/t2iadapter/ldm/modules/encoders/
--rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/encoders/__init__.py
--rw-rw-rw-   0        0        0    12478 2023-03-27 09:17:37.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/encoders/adapter.py
--rw-rw-rw-   0        0        0    16144 2023-03-30 12:56:45.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/encoders/modules.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.352254 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/
--rw-rw-rw-   0        0        0     4075 2023-03-28 02:52:29.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/__init__.py
--rw-rw-rw-   0        0        0    10820 2023-03-28 03:00:16.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/api.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.358531 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/
--rw-rw-rw-   0        0        0       20 2023-03-27 12:28:45.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/__init__.py
--rw-rw-rw-   0        0        0     5759 2023-03-27 11:45:51.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/api.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.373727 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/
--rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/__init__.py
--rw-rw-rw-   0        0        0      383 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/base_model.py
--rw-rw-rw-   0        0        0     9584 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/blocks.py
--rw-rw-rw-   0        0        0     3263 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/dpt_depth.py
--rw-rw-rw-   0        0        0     2785 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net.py
--rw-rw-rw-   0        0        0     5334 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net_custom.py
--rw-rw-rw-   0        0        0     8103 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/transforms.py
--rw-rw-rw-   0        0        0    15116 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/vit.py
--rw-rw-rw-   0        0        0     4771 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/utils.py
--rw-rw-rw-   0        0        0    21582 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/model_edge.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.385105 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/
--rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/__init__.py
--rw-rw-rw-   0        0        0     1067 2023-03-27 11:46:06.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/api.py
--rw-rw-rw-   0        0        0    10903 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/body.py
--rw-rw-rw-   0        0        0     3166 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/hand.py
--rw-rw-rw-   0        0        0     8951 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/model.py
--rw-rw-rw-   0        0        0     8646 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/util.py
--rw-rw-rw-   0        0        0     4759 2023-03-27 02:06:47.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/utils.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.393319 t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/
--rw-rw-rw-   0        0        0      232 2023-03-27 09:16:36.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/__init__.py
--rw-rw-rw-   0        0        0    25939 2023-03-27 09:16:26.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/bsrgan.py
--rw-rw-rw-   0        0        0    22928 2023-03-27 09:16:39.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/bsrgan_light.py
--rw-rw-rw-   0        0        0    29939 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/utils_image.py
--rw-rw-rw-   0        0        0     6229 2023-03-26 13:18:10.000000 t2iadapter-0.1.1/t2iadapter/ldm/util.py
--rw-rw-rw-   0        0        0      133 2023-04-03 03:30:04.000000 t2iadapter-0.1.1/t2iadapter/version.py
-drwxrwxrwx   0        0        0        0 2023-04-03 03:30:05.275085 t2iadapter-0.1.1/t2iadapter.egg-info/
--rw-rw-rw-   0        0        0      588 2023-04-03 03:30:05.000000 t2iadapter-0.1.1/t2iadapter.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     3115 2023-04-03 03:30:05.000000 t2iadapter-0.1.1/t2iadapter.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 03:30:05.000000 t2iadapter-0.1.1/t2iadapter.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-03 03:30:05.000000 t2iadapter-0.1.1/t2iadapter.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0      284 2023-04-03 03:30:05.000000 t2iadapter-0.1.1/t2iadapter.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2023-04-03 03:30:05.000000 t2iadapter-0.1.1/t2iadapter.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.877085 t2iadapter-0.1.2/
+-rw-rw-rw-   0        0        0      588 2023-04-06 13:14:12.876088 t2iadapter-0.1.2/PKG-INFO
+-rw-rw-rw-   0        0        0    19580 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-06 13:14:12.877085 t2iadapter-0.1.2/setup.cfg
+-rw-rw-rw-   0        0        0     3111 2023-03-27 06:58:25.000000 t2iadapter-0.1.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.729866 t2iadapter-0.1.2/t2iadapter/
+-rw-rw-rw-   0        0        0       57 2023-03-27 12:25:37.000000 t2iadapter-0.1.2/t2iadapter/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.746927 t2iadapter-0.1.2/t2iadapter/adapters/
+-rw-rw-rw-   0        0        0        0 2023-03-27 06:43:06.000000 t2iadapter-0.1.2/t2iadapter/adapters/__init__.py
+-rw-rw-rw-   0        0        0     5644 2023-03-27 13:01:16.000000 t2iadapter-0.1.2/t2iadapter/adapters/coadapters.py
+-rw-rw-rw-   0        0        0     1997 2023-03-27 09:19:12.000000 t2iadapter-0.1.2/t2iadapter/adapters/t2i_adapters_for_canny.py
+-rw-rw-rw-   0        0        0     2801 2023-03-27 13:01:27.000000 t2iadapter-0.1.2/t2iadapter/adapters/t2i_adapters_for_style.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.756685 t2iadapter-0.1.2/t2iadapter/ldm/
+-rw-rw-rw-   0        0        0       79 2023-03-27 12:26:15.000000 t2iadapter-0.1.2/t2iadapter/ldm/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.772205 t2iadapter-0.1.2/t2iadapter/ldm/data/
+-rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/data/__init__.py
+-rw-rw-rw-   0        0        0     1369 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_coco.py
+-rw-rw-rw-   0        0        0     1173 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_depth.py
+-rw-rw-rw-   0        0        0     5202 2023-03-27 09:14:57.000000 t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_laion.py
+-rw-rw-rw-   0        0        0     2218 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_wikiart.py
+-rw-rw-rw-   0        0        0     2986 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/data/utils.py
+-rw-rw-rw-   0        0        0     8850 2023-03-27 12:49:35.000000 t2iadapter-0.1.2/t2iadapter/ldm/inference_base.py
+-rw-rw-rw-   0        0        0     3980 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/lr_scheduler.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.776196 t2iadapter-0.1.2/t2iadapter/ldm/models/
+-rw-rw-rw-   0        0        0       39 2023-03-27 12:26:24.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/__init__.py
+-rw-rw-rw-   0        0        0     8511 2023-03-27 09:15:26.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/autoencoder.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.786168 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/
+-rw-rw-rw-   0        0        0       40 2023-03-27 12:26:46.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/__init__.py
+-rw-rw-rw-   0        0        0    15589 2023-03-27 09:15:24.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/ddim.py
+-rw-rw-rw-   0        0        0    63203 2023-03-30 12:56:51.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/ddpm.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.797035 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/dpm_solver/
+-rw-rw-rw-   0        0        0       37 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/dpm_solver/__init__.py
+-rw-rw-rw-   0        0        0    67294 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/dpm_solver/dpm_solver.py
+-rw-rw-rw-   0        0        0     3078 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/dpm_solver/sampler.py
+-rw-rw-rw-   0        0        0    12977 2023-03-27 09:17:27.000000 t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/plms.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.803418 t2iadapter-0.1.2/t2iadapter/ldm/modules/
+-rw-rw-rw-   0        0        0      163 2023-03-27 12:37:23.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/__init__.py
+-rw-rw-rw-   0        0        0    11582 2023-03-27 09:15:52.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/attention.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.810585 t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/
+-rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/__init__.py
+-rw-rw-rw-   0        0        0    30906 2023-03-30 12:18:15.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/model.py
+-rw-rw-rw-   0        0        0    31471 2023-03-27 09:17:52.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/openaimodel.py
+-rw-rw-rw-   0        0        0    10071 2023-03-27 09:17:48.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/util.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.815570 t2iadapter-0.1.2/t2iadapter/ldm/modules/distributions/
+-rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/distributions/__init__.py
+-rw-rw-rw-   0        0        0     3062 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/distributions/distributions.py
+-rw-rw-rw-   0        0        0     3190 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/ema.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.822081 t2iadapter-0.1.2/t2iadapter/ldm/modules/encoders/
+-rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/encoders/__init__.py
+-rw-rw-rw-   0        0        0    12556 2023-04-06 06:15:20.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/encoders/adapter.py
+-rw-rw-rw-   0        0        0    16144 2023-03-30 12:56:45.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/encoders/modules.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.830474 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/
+-rw-rw-rw-   0        0        0     4075 2023-04-06 13:04:36.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/__init__.py
+-rw-rw-rw-   0        0        0    10934 2023-04-06 13:06:17.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/api.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.836460 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/
+-rw-rw-rw-   0        0        0       20 2023-03-27 12:28:45.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/__init__.py
+-rw-rw-rw-   0        0        0     5759 2023-03-27 11:45:51.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/api.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.855415 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/
+-rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/__init__.py
+-rw-rw-rw-   0        0        0      383 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/base_model.py
+-rw-rw-rw-   0        0        0     9584 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/blocks.py
+-rw-rw-rw-   0        0        0     3263 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/dpt_depth.py
+-rw-rw-rw-   0        0        0     2785 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net.py
+-rw-rw-rw-   0        0        0     5334 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net_custom.py
+-rw-rw-rw-   0        0        0     8103 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/transforms.py
+-rw-rw-rw-   0        0        0    15116 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/vit.py
+-rw-rw-rw-   0        0        0     4771 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/utils.py
+-rw-rw-rw-   0        0        0    21582 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/model_edge.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.866271 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/
+-rw-rw-rw-   0        0        0        0 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/__init__.py
+-rw-rw-rw-   0        0        0     1067 2023-03-27 11:46:06.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/api.py
+-rw-rw-rw-   0        0        0    10903 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/body.py
+-rw-rw-rw-   0        0        0     3166 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/hand.py
+-rw-rw-rw-   0        0        0     8951 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/model.py
+-rw-rw-rw-   0        0        0     8646 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/util.py
+-rw-rw-rw-   0        0        0     4759 2023-03-27 02:06:47.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.874093 t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/
+-rw-rw-rw-   0        0        0      232 2023-03-27 09:16:36.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/__init__.py
+-rw-rw-rw-   0        0        0    25939 2023-03-27 09:16:26.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/bsrgan.py
+-rw-rw-rw-   0        0        0    22928 2023-03-27 09:16:39.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/bsrgan_light.py
+-rw-rw-rw-   0        0        0    29939 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/utils_image.py
+-rw-rw-rw-   0        0        0     6229 2023-03-26 13:18:10.000000 t2iadapter-0.1.2/t2iadapter/ldm/util.py
+-rw-rw-rw-   0        0        0      133 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter/version.py
+drwxrwxrwx   0        0        0        0 2023-04-06 13:14:12.739967 t2iadapter-0.1.2/t2iadapter.egg-info/
+-rw-rw-rw-   0        0        0      588 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     3115 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0      284 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-04-06 13:14:12.000000 t2iadapter-0.1.2/t2iadapter.egg-info/top_level.txt
```

### Comparing `t2iadapter-0.1.1/PKG-INFO` & `t2iadapter-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: t2iadapter
-Version: 0.1.1
+Version: 0.1.2
 Summary: T2I-Adapter
 Home-page: https://github.com/TencentARC/T2I-Adapter
 Author: TencentARC
 Author-email: arc@tencent.com
 License: Apache License 2.0
 Description: UNKNOWN
 Keywords: computer vision
```

### Comparing `t2iadapter-0.1.1/README.md` & `t2iadapter-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/setup.py` & `t2iadapter-0.1.2/setup.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/adapters/coadapters.py` & `t2iadapter-0.1.2/t2iadapter/adapters/coadapters.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/adapters/t2i_adapters_for_canny.py` & `t2iadapter-0.1.2/t2iadapter/adapters/t2i_adapters_for_canny.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/adapters/t2i_adapters_for_style.py` & `t2iadapter-0.1.2/t2iadapter/adapters/t2i_adapters_for_style.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_coco.py` & `t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_coco.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_depth.py` & `t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_depth.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_laion.py` & `t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_laion.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/data/dataset_wikiart.py` & `t2iadapter-0.1.2/t2iadapter/ldm/data/dataset_wikiart.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/data/utils.py` & `t2iadapter-0.1.2/t2iadapter/ldm/data/utils.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/inference_base.py` & `t2iadapter-0.1.2/t2iadapter/ldm/inference_base.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/lr_scheduler.py` & `t2iadapter-0.1.2/t2iadapter/ldm/lr_scheduler.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/models/autoencoder.py` & `t2iadapter-0.1.2/t2iadapter/ldm/models/autoencoder.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/ddim.py` & `t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/ddim.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/ddpm.py` & `t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/ddpm.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/dpm_solver/dpm_solver.py` & `t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/dpm_solver/dpm_solver.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/dpm_solver/sampler.py` & `t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/dpm_solver/sampler.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/models/diffusion/plms.py` & `t2iadapter-0.1.2/t2iadapter/ldm/models/diffusion/plms.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/attention.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/attention.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/model.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/model.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/openaimodel.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/openaimodel.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/diffusionmodules/util.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/diffusionmodules/util.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/distributions/distributions.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/distributions/distributions.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/ema.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/ema.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/encoders/adapter.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/encoders/adapter.py`

 * *Files 1% similar despite different names*

```diff
@@ -44,27 +44,26 @@
         super().__init__()
         self.channels = channels
         self.out_channels = out_channels or channels
         self.use_conv = use_conv
         self.dims = dims
         stride = 2 if dims != 3 else (1, 2, 2)
         if use_conv:
-            self.op = conv_nd(
-                dims, self.channels, self.out_channels, 3, stride=stride, padding=padding
-            )
+            self.op = conv_nd(dims, self.channels, self.out_channels, 3, stride=stride, padding=padding)
         else:
             assert self.channels == self.out_channels
             self.op = avg_pool_nd(dims, kernel_size=stride, stride=stride)
 
     def forward(self, x):
         assert x.shape[1] == self.channels
         return self.op(x)
 
 
 class ResnetBlock(nn.Module):
+
     def __init__(self, in_c, out_c, down, ksize=3, sk=False, use_conv=True):
         super().__init__()
         ps = ksize // 2
         if in_c != out_c or sk == False:
             self.in_conv = nn.Conv2d(in_c, out_c, ksize, 1, ps)
         else:
             # print('n_in')
@@ -93,14 +92,15 @@
         if self.skep is not None:
             return h + self.skep(x)
         else:
             return h + x
 
 
 class Adapter(nn.Module):
+
     def __init__(self, channels=[320, 640, 1280, 1280], nums_rb=3, cin=64, ksize=3, sk=False, use_conv=True):
         super(Adapter, self).__init__()
         self.unshuffle = nn.PixelUnshuffle(8)
         self.channels = channels
         self.nums_rb = nums_rb
         self.body = []
         for i in range(len(channels)):
@@ -168,15 +168,15 @@
 
 
 class StyleAdapter(nn.Module):
 
     def __init__(self, width=1024, context_dim=768, num_head=8, n_layes=3, num_token=4):
         super().__init__()
 
-        scale = width ** -0.5
+        scale = width**-0.5
         self.transformer_layes = nn.Sequential(*[ResidualAttentionBlock(width, num_head) for _ in range(n_layes)])
         self.num_token = num_token
         self.style_embedding = nn.Parameter(torch.randn(1, num_token, width) * scale)
         self.ln_post = LayerNorm(width)
         self.ln_pre = LayerNorm(width)
         self.proj = nn.Parameter(scale * torch.randn(width, context_dim))
 
@@ -193,14 +193,15 @@
         x = self.ln_post(x[:, -self.num_token:, :])
         x = x @ self.proj
 
         return x
 
 
 class ResnetBlock_light(nn.Module):
+
     def __init__(self, in_c):
         super().__init__()
         self.block1 = nn.Conv2d(in_c, in_c, 3, 1, 1)
         self.act = nn.ReLU()
         self.block2 = nn.Conv2d(in_c, in_c, 3, 1, 1)
 
     def forward(self, x):
@@ -208,14 +209,15 @@
         h = self.act(h)
         h = self.block2(h)
 
         return h + x
 
 
 class extractor(nn.Module):
+
     def __init__(self, in_c, inter_c, out_c, nums_rb, down=False):
         super().__init__()
         self.in_conv = nn.Conv2d(in_c, inter_c, 1, 1, 0)
         self.body = []
         for _ in range(nums_rb):
             self.body.append(ResnetBlock_light(inter_c))
         self.body = nn.Sequential(*self.body)
@@ -231,25 +233,29 @@
         x = self.body(x)
         x = self.out_conv(x)
 
         return x
 
 
 class Adapter_light(nn.Module):
+
     def __init__(self, channels=[320, 640, 1280, 1280], nums_rb=3, cin=64):
         super(Adapter_light, self).__init__()
         self.unshuffle = nn.PixelUnshuffle(8)
         self.channels = channels
         self.nums_rb = nums_rb
         self.body = []
         for i in range(len(channels)):
             if i == 0:
-                self.body.append(extractor(in_c=cin, inter_c=channels[i]//4, out_c=channels[i], nums_rb=nums_rb, down=False))
+                self.body.append(
+                    extractor(in_c=cin, inter_c=channels[i] // 4, out_c=channels[i], nums_rb=nums_rb, down=False))
             else:
-                self.body.append(extractor(in_c=channels[i-1], inter_c=channels[i]//4, out_c=channels[i], nums_rb=nums_rb, down=True))
+                self.body.append(
+                    extractor(
+                        in_c=channels[i - 1], inter_c=channels[i] // 4, out_c=channels[i], nums_rb=nums_rb, down=True))
         self.body = nn.ModuleList(self.body)
 
     def forward(self, x):
         # unshuffle
         x = self.unshuffle(x)
         # extract features
         features = []
@@ -257,17 +263,18 @@
             x = self.body[i](x)
             features.append(x)
 
         return features
 
 
 class CoAdapterFuser(nn.Module):
+
     def __init__(self, unet_channels=[320, 640, 1280, 1280], width=768, num_head=8, n_layes=3):
         super(CoAdapterFuser, self).__init__()
-        scale = width ** 0.5
+        scale = width**0.5
         # 16, maybe large enough for the number of adapters?
         self.task_embedding = nn.Parameter(scale * torch.randn(16, width))
         self.positional_embedding = nn.Parameter(scale * torch.randn(len(unet_channels), width))
         self.spatial_feat_mapping = nn.ModuleList()
         for ch in unet_channels:
             self.spatial_feat_mapping.append(nn.Sequential(
                 nn.SiLU(),
@@ -310,26 +317,27 @@
 
         ret_feat_map = None
         ret_feat_seq = None
         cur_seq_idx = 0
         for cond_name in features.keys():
             if not isinstance(features[cond_name], list):
                 length = features[cond_name].size(1)
-                transformed_feature = features[cond_name] * ((x[:, cur_seq_idx:cur_seq_idx+length] @ self.seq_proj) + 1)
+                transformed_feature = features[cond_name] * (
+                    (x[:, cur_seq_idx:cur_seq_idx + length] @ self.seq_proj) + 1)
                 if ret_feat_seq is None:
                     ret_feat_seq = transformed_feature
                 else:
                     ret_feat_seq = torch.cat([ret_feat_seq, transformed_feature], dim=1)
                 cur_seq_idx += length
                 continue
 
             length = len(features[cond_name])
             transformed_feature_list = []
             for idx in range(length):
-                alpha = self.spatial_ch_projs[idx](x[:, cur_seq_idx+idx])
+                alpha = self.spatial_ch_projs[idx](x[:, cur_seq_idx + idx])
                 alpha = alpha.unsqueeze(-1).unsqueeze(-1) + 1
                 transformed_feature_list.append(features[cond_name][idx] * alpha)
             if ret_feat_map is None:
                 ret_feat_map = transformed_feature_list
             else:
                 ret_feat_map = list(map(lambda x, y: x + y, ret_feat_map, transformed_feature_list))
             cur_seq_idx += length
```

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/encoders/modules.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/encoders/modules.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/__init__.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/__init__.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/api.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/api.py`

 * *Files 4% similar despite different names*

```diff
@@ -20,41 +20,41 @@
     openpose = 7
     zoedepth = 8
 
 
 def get_cond_model(opt, cond_type: ExtraCondition):
     if cond_type == ExtraCondition.sketch:
         from t2iadapter.ldm.modules.extra_condition import init_sketch_model
-        model = init_sketch_model(model_name='pidinet')
+        model = init_sketch_model(model_name='pidinet', device=opt.device)
         return model
     elif cond_type == ExtraCondition.seg:
         raise NotImplementedError
     elif cond_type == ExtraCondition.keypose:
         from t2iadapter.ldm.modules.extra_condition import init_keypose_model
-        model = init_keypose_model(model_name='mmpose')
+        model = init_keypose_model(model_name='mmpose', device=opt.device)
         return model
     elif cond_type == ExtraCondition.depth:
         from t2iadapter.ldm.modules.extra_condition import init_depth_model
-        model = init_depth_model(model_name='midas')
+        model = init_depth_model(model_name='midas', device=opt.device)
         return model
     elif cond_type == ExtraCondition.zoedepth:
         from t2iadapter.ldm.modules.extra_condition import init_zoedepth_model
-        model = init_zoedepth_model(model_name='zoedepth')
+        model = init_zoedepth_model(model_name='zoedepth', device=opt.device)
         return model
     elif cond_type == ExtraCondition.canny:
         return None
     elif cond_type == ExtraCondition.style:
         from t2iadapter.ldm.modules.extra_condition import init_style_model
-        model = init_style_model(model_name='clip-vit-large')
+        model = init_style_model(model_name='clip-vit-large', device=opt.device)
         return model
     elif cond_type == ExtraCondition.color:
         return None
     elif cond_type == ExtraCondition.openpose:
         from t2iadapter.ldm.modules.extra_condition import init_openpose_model
-        model = init_openpose_model(model_name='openpose')
+        model = init_openpose_model(model_name='openpose', device=opt.device)
         return model
     else:
         raise NotImplementedError
 
 
 def get_cond_sketch(opt, cond_image, cond_inp_type, cond_model=None):
     if isinstance(cond_image, str):
```

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/api.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/api.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/blocks.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/blocks.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/dpt_depth.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/dpt_depth.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net_custom.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/midas_net_custom.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/transforms.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/transforms.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/midas/vit.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/midas/vit.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/midas/utils.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/midas/utils.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/model_edge.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/model_edge.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/api.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/api.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/body.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/body.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/hand.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/hand.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/model.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/model.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/openpose/util.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/openpose/util.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/extra_condition/utils.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/extra_condition/utils.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/bsrgan.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/bsrgan.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/bsrgan_light.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/bsrgan_light.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/modules/image_degradation/utils_image.py` & `t2iadapter-0.1.2/t2iadapter/ldm/modules/image_degradation/utils_image.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter/ldm/util.py` & `t2iadapter-0.1.2/t2iadapter/ldm/util.py`

 * *Files identical despite different names*

### Comparing `t2iadapter-0.1.1/t2iadapter.egg-info/PKG-INFO` & `t2iadapter-0.1.2/t2iadapter.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: t2iadapter
-Version: 0.1.1
+Version: 0.1.2
 Summary: T2I-Adapter
 Home-page: https://github.com/TencentARC/T2I-Adapter
 Author: TencentARC
 Author-email: arc@tencent.com
 License: Apache License 2.0
 Description: UNKNOWN
 Keywords: computer vision
```

### Comparing `t2iadapter-0.1.1/t2iadapter.egg-info/SOURCES.txt` & `t2iadapter-0.1.2/t2iadapter.egg-info/SOURCES.txt`

 * *Files identical despite different names*

