# Comparing `tmp/sdkit-1.0.8.tar.gz` & `tmp/sdkit-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sdkit-1.0.8.tar", last modified: Mon Dec 26 06:28:49 2022, max compression
+gzip compressed data, was "sdkit-1.0.9.tar", last modified: Mon Dec 26 06:53:41 2022, max compression
```

## Comparing `sdkit-1.0.8.tar` & `sdkit-1.0.9.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.911803 sdkit-1.0.8/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     4121 2022-12-23 10:54:05.000000 sdkit-1.0.8/LICENSE
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)    10561 2022-12-26 06:28:49.911803 sdkit-1.0.8/PKG-INFO
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     9417 2022-12-25 12:59:22.000000 sdkit-1.0.8/README.md
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1202 2022-12-26 06:28:24.000000 sdkit-1.0.8/pyproject.toml
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:48.586438 sdkit-1.0.8/sdkit/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1558 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/__init__.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:48.805440 sdkit-1.0.8/sdkit/filter/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       41 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/filter/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1080 2022-12-23 17:45:58.000000 sdkit-1.0.8/sdkit/filter/apply_filters.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      967 2022-12-24 15:54:42.000000 sdkit-1.0.8/sdkit/filter/gfpgan.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      348 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/filter/realesrgan.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:48.892438 sdkit-1.0.8/sdkit/generate/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       54 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/generate/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     3797 2022-12-24 15:27:25.000000 sdkit-1.0.8/sdkit/generate/image_generator.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2442 2022-12-24 14:19:36.000000 sdkit-1.0.8/sdkit/generate/prompt_parser.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.050436 sdkit-1.0.8/sdkit/generate/sampler/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       39 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/generate/sampler/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2258 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/generate/sampler/default_samplers.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2493 2022-12-23 13:03:14.000000 sdkit-1.0.8/sdkit/generate/sampler/k_samplers.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1929 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/generate/sampler/sampler_main.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.142365 sdkit-1.0.8/sdkit/models/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      259 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     5404 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/model_downloader.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.267705 sdkit-1.0.8/sdkit/models/model_loader/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1116 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/model_loader/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      551 2022-12-24 15:57:14.000000 sdkit-1.0.8/sdkit/models/model_loader/gfpgan.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.345842 sdkit-1.0.8/sdkit/models/model_loader/hypernetwork/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1855 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/model_loader/hypernetwork/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     4196 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/model_loader/hypernetwork/hypernetwork.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1171 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/model_loader/realesrgan.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.440030 sdkit-1.0.8/sdkit/models/model_loader/stable_diffusion/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     4026 2022-12-25 11:34:33.000000 sdkit-1.0.8/sdkit/models/model_loader/stable_diffusion/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     9543 2022-12-26 05:19:42.000000 sdkit-1.0.8/sdkit/models/model_loader/stable_diffusion/optimizations.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1474 2022-12-24 16:01:04.000000 sdkit-1.0.8/sdkit/models/model_loader/vae.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.626059 sdkit-1.0.8/sdkit/models/models_db/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      688 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/models_db/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      483 2022-12-26 06:24:39.000000 sdkit-1.0.8/sdkit/models/models_db/gfpgan.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1286 2022-12-26 06:17:24.000000 sdkit-1.0.8/sdkit/models/models_db/print_quick_hashes.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      546 2022-12-26 06:24:50.000000 sdkit-1.0.8/sdkit/models/models_db/realesrgan.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     9883 2022-12-26 06:24:26.000000 sdkit-1.0.8/sdkit/models/models_db/stable_diffusion.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      205 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/models/scan_models.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.676495 sdkit-1.0.8/sdkit/train/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       39 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/train/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1999 2022-12-26 04:43:58.000000 sdkit-1.0.8/sdkit/train/merge_models.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:49.880503 sdkit-1.0.8/sdkit/utils/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      805 2022-12-26 05:50:49.000000 sdkit-1.0.8/sdkit/utils/__init__.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      210 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/utils/device_utils.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2638 2022-12-26 04:21:30.000000 sdkit-1.0.8/sdkit/utils/file_utils.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1508 2022-12-26 06:25:26.000000 sdkit-1.0.8/sdkit/utils/hash_utils.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      986 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/utils/http_utils.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2082 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/utils/image_utils.py
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2194 2022-12-23 10:54:05.000000 sdkit-1.0.8/sdkit/utils/latent_utils.py
-drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:28:48.694439 sdkit-1.0.8/sdkit.egg-info/
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)    10561 2022-12-26 06:28:47.000000 sdkit-1.0.8/sdkit.egg-info/PKG-INFO
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1439 2022-12-26 06:28:48.000000 sdkit-1.0.8/sdkit.egg-info/SOURCES.txt
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        1 2022-12-26 06:28:47.000000 sdkit-1.0.8/sdkit.egg-info/dependency_links.txt
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       85 2022-12-26 06:28:47.000000 sdkit-1.0.8/sdkit.egg-info/requires.txt
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        6 2022-12-26 06:28:47.000000 sdkit-1.0.8/sdkit.egg-info/top_level.txt
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       38 2022-12-26 06:28:49.911803 sdkit-1.0.8/setup.cfg
--rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      288 2022-12-23 10:54:05.000000 sdkit-1.0.8/setup.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.901213 sdkit-1.0.9/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     4121 2022-12-23 10:54:05.000000 sdkit-1.0.9/LICENSE
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)    10561 2022-12-26 06:53:41.901213 sdkit-1.0.9/PKG-INFO
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     9417 2022-12-25 12:59:22.000000 sdkit-1.0.9/README.md
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1202 2022-12-26 06:53:21.000000 sdkit-1.0.9/pyproject.toml
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:40.786016 sdkit-1.0.9/sdkit/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1558 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/__init__.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:40.978753 sdkit-1.0.9/sdkit/filter/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       41 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/filter/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1080 2022-12-23 17:45:58.000000 sdkit-1.0.9/sdkit/filter/apply_filters.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      967 2022-12-24 15:54:42.000000 sdkit-1.0.9/sdkit/filter/gfpgan.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      348 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/filter/realesrgan.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.053355 sdkit-1.0.9/sdkit/generate/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       54 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/generate/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     3797 2022-12-24 15:27:25.000000 sdkit-1.0.9/sdkit/generate/image_generator.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2442 2022-12-24 14:19:36.000000 sdkit-1.0.9/sdkit/generate/prompt_parser.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.155566 sdkit-1.0.9/sdkit/generate/sampler/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       39 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/generate/sampler/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2258 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/generate/sampler/default_samplers.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2493 2022-12-23 13:03:14.000000 sdkit-1.0.9/sdkit/generate/sampler/k_samplers.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1929 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/generate/sampler/sampler_main.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.234088 sdkit-1.0.9/sdkit/models/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      259 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     5404 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/model_downloader.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.359482 sdkit-1.0.9/sdkit/models/model_loader/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1116 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/model_loader/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      551 2022-12-24 15:57:14.000000 sdkit-1.0.9/sdkit/models/model_loader/gfpgan.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.422375 sdkit-1.0.9/sdkit/models/model_loader/hypernetwork/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1855 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/model_loader/hypernetwork/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     4196 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/model_loader/hypernetwork/hypernetwork.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1171 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/model_loader/realesrgan.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.500383 sdkit-1.0.9/sdkit/models/model_loader/stable_diffusion/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     4026 2022-12-25 11:34:33.000000 sdkit-1.0.9/sdkit/models/model_loader/stable_diffusion/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     9418 2022-12-26 06:51:41.000000 sdkit-1.0.9/sdkit/models/model_loader/stable_diffusion/optimizations.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1474 2022-12-24 16:01:04.000000 sdkit-1.0.9/sdkit/models/model_loader/vae.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.656056 sdkit-1.0.9/sdkit/models/models_db/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      688 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/models_db/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      483 2022-12-26 06:24:39.000000 sdkit-1.0.9/sdkit/models/models_db/gfpgan.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1286 2022-12-26 06:17:24.000000 sdkit-1.0.9/sdkit/models/models_db/print_quick_hashes.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      546 2022-12-26 06:24:50.000000 sdkit-1.0.9/sdkit/models/models_db/realesrgan.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     9883 2022-12-26 06:40:39.000000 sdkit-1.0.9/sdkit/models/models_db/stable_diffusion.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      205 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/models/scan_models.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.703314 sdkit-1.0.9/sdkit/train/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       39 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/train/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1999 2022-12-26 04:43:58.000000 sdkit-1.0.9/sdkit/train/merge_models.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:41.881083 sdkit-1.0.9/sdkit/utils/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      805 2022-12-26 05:50:49.000000 sdkit-1.0.9/sdkit/utils/__init__.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      210 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/utils/device_utils.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2638 2022-12-26 04:21:30.000000 sdkit-1.0.9/sdkit/utils/file_utils.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1508 2022-12-26 06:25:26.000000 sdkit-1.0.9/sdkit/utils/hash_utils.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      986 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/utils/http_utils.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2082 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/utils/image_utils.py
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     2194 2022-12-23 10:54:05.000000 sdkit-1.0.9/sdkit/utils/latent_utils.py
+drwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        0 2022-12-26 06:53:40.883117 sdkit-1.0.9/sdkit.egg-info/
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)    10561 2022-12-26 06:53:40.000000 sdkit-1.0.9/sdkit.egg-info/PKG-INFO
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)     1439 2022-12-26 06:53:40.000000 sdkit-1.0.9/sdkit.egg-info/SOURCES.txt
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        1 2022-12-26 06:53:40.000000 sdkit-1.0.9/sdkit.egg-info/dependency_links.txt
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       85 2022-12-26 06:53:40.000000 sdkit-1.0.9/sdkit.egg-info/requires.txt
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)        6 2022-12-26 06:53:40.000000 sdkit-1.0.9/sdkit.egg-info/top_level.txt
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)       38 2022-12-26 06:53:41.901213 sdkit-1.0.9/setup.cfg
+-rwxrwxrwx   0 sshekhar  (1000) sshekhar  (1000)      288 2022-12-23 10:54:05.000000 sdkit-1.0.9/setup.py
```

### Comparing `sdkit-1.0.8/LICENSE` & `sdkit-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/PKG-INFO` & `sdkit-1.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sdkit
-Version: 1.0.8
+Version: 1.0.9
 Summary: sdkit (stable diffusion kit) is an easy-to-use library for using Stable Diffusion in your AI Art projects. It is fast, feature-packed, and memory-efficient. It bundles Stable Diffusion along with commonly-used features (like GFPGAN, RealESRGAN, k-samplers, custom VAE, hypernetworks etc). It also includes a model-downloader with a database of commonly used models, and advanced features like running in parallel on multiple GPUs, auto-scanning for malicious models etc. Supports Stable Diffusion 2.1!
 Author-email: cmdr2 <secondary.cmdr2@gmail.com>
 Project-URL: Homepage, https://github.com/easydiffusion/sdkit
 Project-URL: Bug Tracker, https://github.com/easydiffusion/sdkit/issues
 Keywords: stable diffusion,ai,art
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `sdkit-1.0.8/README.md` & `sdkit-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/pyproject.toml` & `sdkit-1.0.9/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "sdkit"
-version = "1.0.8"
+version = "1.0.9"
 authors = [
   {name="cmdr2", email="secondary.cmdr2@gmail.com"},
 ]
 description = "sdkit (stable diffusion kit) is an easy-to-use library for using Stable Diffusion in your AI Art projects. It is fast, feature-packed, and memory-efficient. It bundles Stable Diffusion along with commonly-used features (like GFPGAN, RealESRGAN, k-samplers, custom VAE, hypernetworks etc). It also includes a model-downloader with a database of commonly used models, and advanced features like running in parallel on multiple GPUs, auto-scanning for malicious models etc. Supports Stable Diffusion 2.1!"
 readme = "README.md"
 requires-python = ">=3.8.5"
 classifiers = [
```

### Comparing `sdkit-1.0.8/sdkit/__init__.py` & `sdkit-1.0.9/sdkit/__init__.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/filter/apply_filters.py` & `sdkit-1.0.9/sdkit/filter/apply_filters.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/filter/gfpgan.py` & `sdkit-1.0.9/sdkit/filter/gfpgan.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/generate/image_generator.py` & `sdkit-1.0.9/sdkit/generate/image_generator.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/generate/prompt_parser.py` & `sdkit-1.0.9/sdkit/generate/prompt_parser.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/generate/sampler/default_samplers.py` & `sdkit-1.0.9/sdkit/generate/sampler/default_samplers.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/generate/sampler/k_samplers.py` & `sdkit-1.0.9/sdkit/generate/sampler/k_samplers.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/generate/sampler/sampler_main.py` & `sdkit-1.0.9/sdkit/generate/sampler/sampler_main.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_downloader.py` & `sdkit-1.0.9/sdkit/models/model_downloader.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/__init__.py` & `sdkit-1.0.9/sdkit/models/model_loader/__init__.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/gfpgan.py` & `sdkit-1.0.9/sdkit/models/model_loader/gfpgan.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/hypernetwork/__init__.py` & `sdkit-1.0.9/sdkit/models/model_loader/hypernetwork/__init__.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/hypernetwork/hypernetwork.py` & `sdkit-1.0.9/sdkit/models/model_loader/hypernetwork/hypernetwork.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/realesrgan.py` & `sdkit-1.0.9/sdkit/models/model_loader/realesrgan.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/stable_diffusion/__init__.py` & `sdkit-1.0.9/sdkit/models/model_loader/stable_diffusion/__init__.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/stable_diffusion/optimizations.py` & `sdkit-1.0.9/sdkit/models/model_loader/stable_diffusion/optimizations.py`

 * *Files 2% similar despite different names*

```diff
@@ -153,18 +153,16 @@
         r1 = torch.zeros(q.shape[0], q.shape[1], v.shape[2], device=q.device, dtype=q.dtype)
         steps = get_steps(q, k)
         slice_size = q.shape[1] // steps if (q.shape[1] % steps) == 0 else q.shape[1]
         for i in range(0, q.shape[1], slice_size):
             end = i + slice_size
             if attn_precision == "fp32":
                 with torch.autocast(enabled=False, device_type=autocast_device):
-                    q, k = q.float(), k.float()
-                    s1 = einsum('b i d, b j d -> b i j', q[:, i:end], k)
-                    # q_fp, k_fp = q[:, i:end].float(), k.float()
-                    # s1 = einsum('b i d, b j d -> b i j', q_fp, k_fp)
+                    q_fp, k_fp = q[:, i:end].float(), k.float()
+                    s1 = einsum('b i d, b j d -> b i j', q_fp, k_fp)
             else:
                 s1 = einsum('b i d, b j d -> b i j', q[:, i:end], k)
 
             s2 = s1.softmax(dim=-1, dtype=q.dtype)
             del s1
 
             r1[:, i:end] = einsum('b i j, b j d -> b i d', s2, v)
```

### Comparing `sdkit-1.0.8/sdkit/models/model_loader/vae.py` & `sdkit-1.0.9/sdkit/models/model_loader/vae.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/models_db/__init__.py` & `sdkit-1.0.9/sdkit/models/models_db/__init__.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/models_db/print_quick_hashes.py` & `sdkit-1.0.9/sdkit/models/models_db/print_quick_hashes.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/models_db/realesrgan.py` & `sdkit-1.0.9/sdkit/models/models_db/realesrgan.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/models/models_db/stable_diffusion.py` & `sdkit-1.0.9/sdkit/models/models_db/stable_diffusion.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/train/merge_models.py` & `sdkit-1.0.9/sdkit/train/merge_models.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/utils/__init__.py` & `sdkit-1.0.9/sdkit/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/utils/file_utils.py` & `sdkit-1.0.9/sdkit/utils/file_utils.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/utils/hash_utils.py` & `sdkit-1.0.9/sdkit/utils/hash_utils.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/utils/http_utils.py` & `sdkit-1.0.9/sdkit/utils/http_utils.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/utils/image_utils.py` & `sdkit-1.0.9/sdkit/utils/image_utils.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit/utils/latent_utils.py` & `sdkit-1.0.9/sdkit/utils/latent_utils.py`

 * *Files identical despite different names*

### Comparing `sdkit-1.0.8/sdkit.egg-info/PKG-INFO` & `sdkit-1.0.9/sdkit.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sdkit
-Version: 1.0.8
+Version: 1.0.9
 Summary: sdkit (stable diffusion kit) is an easy-to-use library for using Stable Diffusion in your AI Art projects. It is fast, feature-packed, and memory-efficient. It bundles Stable Diffusion along with commonly-used features (like GFPGAN, RealESRGAN, k-samplers, custom VAE, hypernetworks etc). It also includes a model-downloader with a database of commonly used models, and advanced features like running in parallel on multiple GPUs, auto-scanning for malicious models etc. Supports Stable Diffusion 2.1!
 Author-email: cmdr2 <secondary.cmdr2@gmail.com>
 Project-URL: Homepage, https://github.com/easydiffusion/sdkit
 Project-URL: Bug Tracker, https://github.com/easydiffusion/sdkit/issues
 Keywords: stable diffusion,ai,art
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `sdkit-1.0.8/sdkit.egg-info/SOURCES.txt` & `sdkit-1.0.9/sdkit.egg-info/SOURCES.txt`

 * *Files identical despite different names*

