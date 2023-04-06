# Comparing `tmp/hordelib-0.0.9.tar.gz` & `tmp/hordelib-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hordelib-0.0.9.tar", last modified: Mon Apr  3 15:43:11 2023, max compression
+gzip compressed data, was "hordelib-0.1.0.tar", last modified: Thu Apr  6 15:07:48 2023, max compression
```

## Comparing `hordelib-0.0.9.tar` & `hordelib-0.1.0.tar`

### file list

```diff
@@ -1,45 +1,85 @@
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.214503 hordelib-0.0.9/
--rw-rw-rw-   0        0        0      167 2023-03-31 22:05:53.000000 hordelib-0.0.9/.coveragerc
--rw-rw-rw-   0        0        0       88 2023-03-31 20:31:54.000000 hordelib-0.0.9/.flake8
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.181992 hordelib-0.0.9/.github/
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.189997 hordelib-0.0.9/.github/workflows/
--rw-rw-rw-   0        0        0      549 2023-04-03 15:21:28.000000 hordelib-0.0.9/.github/workflows/tests.yaml
--rw-rw-rw-   0        0        0     2089 2023-04-02 15:06:25.000000 hordelib-0.0.9/.gitignore
--rw-rw-rw-   0        0        0     2280 2023-04-03 15:40:18.000000 hordelib-0.0.9/CHANGELOG.md
--rw-rw-rw-   0        0        0    35821 2023-03-31 20:31:54.000000 hordelib-0.0.9/LICENSE
--rw-rw-rw-   0        0        0    46919 2023-04-03 15:43:11.214503 hordelib-0.0.9/PKG-INFO
--rw-rw-rw-   0        0        0     5093 2023-04-02 20:32:42.000000 hordelib-0.0.9/README.md
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.190995 hordelib-0.0.9/hordelib/
--rw-rw-rw-   0        0        0      448 2023-04-02 20:40:39.000000 hordelib-0.0.9/hordelib/__init__.py
--rw-rw-rw-   0        0        0     8321 2023-04-03 15:07:01.000000 hordelib-0.0.9/hordelib/comfy.py
--rw-rw-rw-   0        0        0     3163 2023-04-02 14:59:49.000000 hordelib-0.0.9/hordelib/horde.py
--rw-rw-rw-   0        0        0     2139 2023-04-02 19:47:46.000000 hordelib-0.0.9/hordelib/install.py
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.208503 hordelib-0.0.9/hordelib/nodes/
--rw-rw-rw-   0        0        0        0 2023-04-01 15:21:44.000000 hordelib-0.0.9/hordelib/nodes/__init__.py
--rw-rw-rw-   0        0        0     1559 2023-04-02 12:02:16.000000 hordelib-0.0.9/hordelib/nodes/node_image_output.py
--rw-rw-rw-   0        0        0     1066 2023-04-02 15:20:45.000000 hordelib-0.0.9/hordelib/nodes/node_model_loader.py
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.208503 hordelib-0.0.9/hordelib/pipeline_designs/
--rw-rw-rw-   0        0        0     5961 2023-04-01 17:53:56.000000 hordelib-0.0.9/hordelib/pipeline_designs/pipeline_stable_diffusion.json
--rw-rw-rw-   0        0        0     8913 2023-04-02 09:22:30.000000 hordelib-0.0.9/hordelib/pipeline_designs/pipeline_stable_diffusion_hires_fix.json
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.209503 hordelib-0.0.9/hordelib/pipelines/
--rw-rw-rw-   0        0        0     1743 2023-04-01 17:55:48.000000 hordelib-0.0.9/hordelib/pipelines/pipeline_stable_diffusion.json
--rw-rw-rw-   0        0        0     2869 2023-04-02 09:24:00.000000 hordelib-0.0.9/hordelib/pipelines/pipeline_stable_diffusion_hires_fix.json
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.206503 hordelib-0.0.9/hordelib.egg-info/
--rw-rw-rw-   0        0        0    46919 2023-04-03 15:43:11.000000 hordelib-0.0.9/hordelib.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      860 2023-04-03 15:43:11.000000 hordelib-0.0.9/hordelib.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-03 15:43:11.000000 hordelib-0.0.9/hordelib.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      181 2023-04-03 15:43:11.000000 hordelib-0.0.9/hordelib.egg-info/requires.txt
--rw-rw-rw-   0        0        0       15 2023-04-03 15:43:11.000000 hordelib-0.0.9/hordelib.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1661 2023-04-02 18:36:39.000000 hordelib-0.0.9/publish.py
--rw-rw-rw-   0        0        0     1264 2023-04-03 15:43:03.000000 hordelib-0.0.9/pyproject.toml
--rw-rw-rw-   0        0        0       71 2023-04-02 20:21:53.000000 hordelib-0.0.9/pytest.ini
--rw-rw-rw-   0        0        0      300 2023-04-03 15:43:03.000000 hordelib-0.0.9/requirements.txt
--rw-rw-rw-   0        0        0       42 2023-04-03 15:43:11.214503 hordelib-0.0.9/setup.cfg
-drwxrwxrwx   0        0        0        0 2023-04-03 15:43:11.213504 hordelib-0.0.9/tests/
--rw-rw-rw-   0        0        0        0 2023-04-03 15:07:52.000000 hordelib-0.0.9/tests/__init__.py
--rw-rw-rw-   0        0        0     4168 2023-04-02 11:24:24.000000 hordelib-0.0.9/tests/test_comfy.py
--rw-rw-rw-   0        0        0     2070 2023-04-03 15:32:43.000000 hordelib-0.0.9/tests/test_comfy_install.py
--rw-rw-rw-   0        0        0     3684 2023-04-02 18:37:11.000000 hordelib-0.0.9/tests/test_horde.py
--rw-rw-rw-   0        0        0     2630 2023-04-02 14:21:52.000000 hordelib-0.0.9/tests/test_inference.py
--rw-rw-rw-   0        0        0      211 2023-04-02 18:40:40.000000 hordelib-0.0.9/tests/test_initialisation.py
--rw-rw-rw-   0        0        0      632 2023-04-03 15:26:55.000000 hordelib-0.0.9/tox.ini
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.519635 hordelib-0.1.0/
+-rw-rw-rw-   0        0        0      167 2023-04-03 21:13:26.000000 hordelib-0.1.0/.coveragerc
+-rw-rw-rw-   0        0        0       88 2023-04-03 21:13:26.000000 hordelib-0.1.0/.flake8
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.461122 hordelib-0.1.0/.github/
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.476123 hordelib-0.1.0/.github/workflows/
+-rw-rw-rw-   0        0        0     2265 2023-04-06 13:01:44.000000 hordelib-0.1.0/.github/workflows/pypi.yml
+-rw-rw-rw-   0        0        0      571 2023-04-03 21:13:26.000000 hordelib-0.1.0/.github/workflows/tests.yaml
+-rw-rw-rw-   0        0        0     2128 2023-04-06 12:58:27.000000 hordelib-0.1.0/.gitignore
+-rw-rw-rw-   0        0        0     2962 2023-04-06 14:58:19.000000 hordelib-0.1.0/CHANGELOG.md
+-rw-rw-rw-   0        0        0    35182 2023-04-05 20:05:31.000000 hordelib-0.1.0/LICENSE
+-rw-rw-rw-   0        0        0    46759 2023-04-06 15:07:48.518636 hordelib-0.1.0/PKG-INFO
+-rw-rw-rw-   0        0        0     5654 2023-04-06 14:52:46.000000 hordelib-0.1.0/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.481122 hordelib-0.1.0/hordelib/
+-rw-rw-rw-   0        0        0       94 2023-04-06 13:01:50.000000 hordelib-0.1.0/hordelib/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.497125 hordelib-0.1.0/hordelib/cache/
+-rw-rw-rw-   0        0        0       60 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/cache/__init__.py
+-rw-rw-rw-   0        0        0     8642 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/cache/cache.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.500635 hordelib-0.1.0/hordelib/clip/
+-rw-rw-rw-   0        0        0      131 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/clip/__init__.py
+-rw-rw-rw-   0        0        0     2426 2023-04-04 18:26:09.000000 hordelib-0.1.0/hordelib/clip/bulk.py
+-rw-rw-rw-   0        0        0     1088 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/clip/coca.py
+-rw-rw-rw-   0        0        0     4627 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/clip/image.py
+-rw-rw-rw-   0        0        0    11906 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/clip/interrogate.py
+-rw-rw-rw-   0        0        0     2979 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/clip/text.py
+-rw-rw-rw-   0        0        0     9164 2023-04-06 14:49:12.000000 hordelib-0.1.0/hordelib/comfy_horde.py
+-rw-rw-rw-   0        0        0      525 2023-04-06 13:45:20.000000 hordelib-0.1.0/hordelib/config_path.py
+-rw-rw-rw-   0        0        0      334 2023-04-06 14:51:30.000000 hordelib-0.1.0/hordelib/consts.py
+-rw-rw-rw-   0        0        0     4029 2023-04-06 14:39:53.000000 hordelib-0.1.0/hordelib/horde.py
+-rw-rw-rw-   0        0        0      574 2023-04-06 14:39:42.000000 hordelib-0.1.0/hordelib/initialisation.py
+-rw-rw-rw-   0        0        0     2578 2023-04-06 12:55:51.000000 hordelib-0.1.0/hordelib/install_comfy.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.508635 hordelib-0.1.0/hordelib/model_manager/
+-rw-rw-rw-   0        0        0        0 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/model_manager/__init__.py
+-rw-rw-rw-   0        0        0     7757 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/aitemplate.py
+-rw-rw-rw-   0        0        0    20755 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/base.py
+-rw-rw-rw-   0        0        0     4132 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/blip.py
+-rw-rw-rw-   0        0        0     6498 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/model_manager/clip.py
+-rw-rw-rw-   0        0        0     3629 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/codeformer.py
+-rw-rw-rw-   0        0        0     2199 2023-04-06 13:28:56.000000 hordelib-0.1.0/hordelib/model_manager/compvis.py
+-rw-rw-rw-   0        0        0     5476 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/controlnet.py
+-rw-rw-rw-   0        0        0     4656 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/model_manager/diffusers.py
+-rw-rw-rw-   0        0        0     5163 2023-04-06 12:32:24.000000 hordelib-0.1.0/hordelib/model_manager/esrgan.py
+-rw-rw-rw-   0        0        0     3213 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/gfpgan.py
+-rw-rw-rw-   0        0        0    16218 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/hyper.py
+-rw-rw-rw-   0        0        0     3317 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/new.py
+-rw-rw-rw-   0        0        0     3490 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/model_manager/safety_checker.py
+-rw-rw-rw-   0        0        0     8575 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/sdu.py
+-rw-rw-rw-   0        0        0     6913 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/model_manager/torch_hijack.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.510636 hordelib-0.1.0/hordelib/nodes/
+-rw-rw-rw-   0        0        0        0 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/nodes/__init__.py
+-rw-rw-rw-   0        0        0     1413 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/nodes/node_clip_similarities.py
+-rw-rw-rw-   0        0        0     1634 2023-04-06 14:10:46.000000 hordelib-0.1.0/hordelib/nodes/node_image_output.py
+-rw-rw-rw-   0        0        0     1225 2023-04-06 14:00:19.000000 hordelib-0.1.0/hordelib/nodes/node_model_loader.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.511634 hordelib-0.1.0/hordelib/pipeline_designs/
+-rw-rw-rw-   0        0        0     6710 2023-04-03 21:25:36.000000 hordelib-0.1.0/hordelib/pipeline_designs/pipeline_stable_diffusion.json
+-rw-rw-rw-   0        0        0     9464 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/pipeline_designs/pipeline_stable_diffusion_hires_fix.json
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.512635 hordelib-0.1.0/hordelib/pipelines/
+-rw-rw-rw-   0        0        0     2051 2023-04-03 21:28:04.000000 hordelib-0.1.0/hordelib/pipelines/pipeline_stable_diffusion.json
+-rw-rw-rw-   0        0        0     2869 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/pipelines/pipeline_stable_diffusion_hires_fix.json
+-rw-rw-rw-   0        0        0     2573 2023-04-06 15:05:18.000000 hordelib-0.1.0/hordelib/run_comfyui.py
+-rw-rw-rw-   0        0        0      505 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/settings.py
+-rw-rw-rw-   0        0        0      930 2023-04-06 14:38:17.000000 hordelib-0.1.0/hordelib/shared_model_manager.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.514637 hordelib-0.1.0/hordelib/utils/
+-rw-rw-rw-   0        0        0        0 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/utils/__init__.py
+-rw-rw-rw-   0        0        0      627 2023-04-03 21:13:26.000000 hordelib-0.1.0/hordelib/utils/cast.py
+-rw-rw-rw-   0        0        0      218 2023-04-06 09:46:54.000000 hordelib-0.1.0/hordelib/utils/switch.py
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.496126 hordelib-0.1.0/hordelib.egg-info/
+-rw-rw-rw-   0        0        0    46759 2023-04-06 15:07:48.000000 hordelib-0.1.0/hordelib.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1926 2023-04-06 15:07:48.000000 hordelib-0.1.0/hordelib.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 15:07:48.000000 hordelib-0.1.0/hordelib.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      225 2023-04-06 15:07:48.000000 hordelib-0.1.0/hordelib.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       15 2023-04-06 15:07:48.000000 hordelib-0.1.0/hordelib.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1659 2023-04-03 21:13:26.000000 hordelib-0.1.0/publish.py
+-rw-rw-rw-   0        0        0     1318 2023-04-06 15:07:42.000000 hordelib-0.1.0/pyproject.toml
+-rw-rw-rw-   0        0        0       71 2023-04-03 21:13:26.000000 hordelib-0.1.0/pytest.ini
+-rw-rw-rw-   0        0        0       28 2023-04-06 09:46:54.000000 hordelib-0.1.0/requirements.dev.txt
+-rw-rw-rw-   0        0        0      348 2023-04-06 15:07:42.000000 hordelib-0.1.0/requirements.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 15:07:48.519635 hordelib-0.1.0/setup.cfg
+drwxrwxrwx   0        0        0        0 2023-04-06 15:07:48.517637 hordelib-0.1.0/tests/
+-rw-rw-rw-   0        0        0       40 2023-04-06 13:10:51.000000 hordelib-0.1.0/tests/__init__.py
+-rw-rw-rw-   0        0        0     4157 2023-04-06 12:46:50.000000 hordelib-0.1.0/tests/test_comfy.py
+-rw-rw-rw-   0        0        0     1550 2023-04-06 13:25:34.000000 hordelib-0.1.0/tests/test_comfy_install.py
+-rw-rw-rw-   0        0        0     8676 2023-04-06 14:42:08.000000 hordelib-0.1.0/tests/test_horde.py
+-rw-rw-rw-   0        0        0     4045 2023-04-06 14:40:46.000000 hordelib-0.1.0/tests/test_inference.py
+-rw-rw-rw-   0        0        0      382 2023-04-06 12:47:28.000000 hordelib-0.1.0/tests/test_initialisation.py
+-rw-rw-rw-   0        0        0      805 2023-04-06 15:01:58.000000 hordelib-0.1.0/tox.ini
```

### Comparing `hordelib-0.0.9/.gitignore` & `hordelib-0.1.0/.gitignore`

 * *Files 2% similar despite different names*

```diff
@@ -133,10 +133,14 @@
 
 # Cython debug symbols
 cython_debug/
 
 # Local
 test-image.png
 hordelib/ComfyUI
+ComfyUI
 model.ckpt
 coverage.lcov
-*.png
+*.png
+comfy-prompt.json
+
+.vscode
```

### Comparing `hordelib-0.0.9/CHANGELOG.md` & `hordelib-0.1.0/CHANGELOG.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,28 @@
 ﻿# Changelog
 
 Release history for `hordelib`.
 
+## v0.1.0 - 2023-04-06
+
+### Added
+- Clip skip support.
+- Adds "tox -e comfyui" command to run comfyui web app.
+- Significant refactors and build changes.
+
+### Fixed
+- ComfyUI upgrades work correctly now.
+- Various fixes for Horde Worker integration.
+
+## v0.0.10 - 2023-04-03
+
+### Added
+- CLIP interrogation
+- Model manager
+
 ## v0.0.9 - 2023-04-03
 
 ### Added
 - Adds build helper to package and publish correctly.
 - More thorough tests for ComfyUI install/downgrade/upgrade/etc
 - Working Ci workflow for Github.
```

### Comparing `hordelib-0.0.9/LICENSE` & `hordelib-0.1.0/LICENSE`

 * *Files 8% similar despite different names*

```diff
@@ -1,82 +1,70 @@
-                    GNU GENERAL PUBLIC LICENSE
-                       Version 3, 29 June 2007
+                    GNU AFFERO GENERAL PUBLIC LICENSE
+                       Version 3, 19 November 2007
 
  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
  Everyone is permitted to copy and distribute verbatim copies
  of this license document, but changing it is not allowed.
 
                             Preamble
 
-  The GNU General Public License is a free, copyleft license for
-software and other kinds of works.
+  The GNU Affero General Public License is a free, copyleft license for
+software and other kinds of works, specifically designed to ensure
+cooperation with the community in the case of network server software.
 
   The licenses for most software and other practical works are designed
 to take away your freedom to share and change the works.  By contrast,
-the GNU General Public License is intended to guarantee your freedom to
+our General Public Licenses are intended to guarantee your freedom to
 share and change all versions of a program--to make sure it remains free
-software for all its users.  We, the Free Software Foundation, use the
-GNU General Public License for most of our software; it applies also to
-any other work released this way by its authors.  You can apply it to
-your programs, too.
+software for all its users.
 
   When we speak of free software, we are referring to freedom, not
 price.  Our General Public Licenses are designed to make sure that you
 have the freedom to distribute copies of free software (and charge for
 them if you wish), that you receive source code or can get it if you
 want it, that you can change the software or use pieces of it in new
 free programs, and that you know you can do these things.
 
-  To protect your rights, we need to prevent others from denying you
-these rights or asking you to surrender the rights.  Therefore, you have
-certain responsibilities if you distribute copies of the software, or if
-you modify it: responsibilities to respect the freedom of others.
-
-  For example, if you distribute copies of such a program, whether
-gratis or for a fee, you must pass on to the recipients the same
-freedoms that you received.  You must make sure that they, too, receive
-or can get the source code.  And you must show them these terms so they
-know their rights.
-
-  Developers that use the GNU GPL protect your rights with two steps:
-(1) assert copyright on the software, and (2) offer you this License
-giving you legal permission to copy, distribute and/or modify it.
-
-  For the developers' and authors' protection, the GPL clearly explains
-that there is no warranty for this free software.  For both users' and
-authors' sake, the GPL requires that modified versions be marked as
-changed, so that their problems will not be attributed erroneously to
-authors of previous versions.
-
-  Some devices are designed to deny users access to install or run
-modified versions of the software inside them, although the manufacturer
-can do so.  This is fundamentally incompatible with the aim of
-protecting users' freedom to change the software.  The systematic
-pattern of such abuse occurs in the area of products for individuals to
-use, which is precisely where it is most unacceptable.  Therefore, we
-have designed this version of the GPL to prohibit the practice for those
-products.  If such problems arise substantially in other domains, we
-stand ready to extend this provision to those domains in future versions
-of the GPL, as needed to protect the freedom of users.
-
-  Finally, every program is threatened constantly by software patents.
-States should not allow patents to restrict development and use of
-software on general-purpose computers, but in those that do, we wish to
-avoid the special danger that patents applied to a free program could
-make it effectively proprietary.  To prevent this, the GPL assures that
-patents cannot be used to render the program non-free.
+  Developers that use our General Public Licenses protect your rights
+with two steps: (1) assert copyright on the software, and (2) offer
+you this License which gives you legal permission to copy, distribute
+and/or modify the software.
+
+  A secondary benefit of defending all users' freedom is that
+improvements made in alternate versions of the program, if they
+receive widespread use, become available for other developers to
+incorporate.  Many developers of free software are heartened and
+encouraged by the resulting cooperation.  However, in the case of
+software used on network servers, this result may fail to come about.
+The GNU General Public License permits making a modified version and
+letting the public access it on a server without ever releasing its
+source code to the public.
+
+  The GNU Affero General Public License is designed specifically to
+ensure that, in such cases, the modified source code becomes available
+to the community.  It requires the operator of a network server to
+provide the source code of the modified version running there to the
+users of that server.  Therefore, public use of a modified version, on
+a publicly accessible server, gives the public access to the source
+code of the modified version.
+
+  An older license, called the Affero General Public License and
+published by Affero, was designed to accomplish similar goals.  This is
+a different license, not a version of the Affero GPL, but Affero has
+released a new version of the Affero GPL which permits relicensing under
+this license.
 
   The precise terms and conditions for copying, distribution and
 modification follow.
 
                        TERMS AND CONDITIONS
 
   0. Definitions.
 
-  "This License" refers to version 3 of the GNU General Public License.
+  "This License" refers to version 3 of the GNU Affero General Public License.
 
   "Copyright" also means copyright-like laws that apply to other kinds of
 works, such as semiconductor masks.
 
   "The Program" refers to any copyrightable work licensed under this
 License.  Each licensee is addressed as "you".  "Licensees" and
 "recipients" may be individuals or organizations.
@@ -545,43 +533,53 @@
 covered work so as to satisfy simultaneously your obligations under this
 License and any other pertinent obligations, then as a consequence you may
 not convey it at all.  For example, if you agree to terms that obligate you
 to collect a royalty for further conveying from those to whom you convey
 the Program, the only way you could satisfy both those terms and this
 License would be to refrain entirely from conveying the Program.
 
-  13. Use with the GNU Affero General Public License.
+  13. Remote Network Interaction; Use with the GNU General Public License.
+
+  Notwithstanding any other provision of this License, if you modify the
+Program, your modified version must prominently offer all users
+interacting with it remotely through a computer network (if your version
+supports such interaction) an opportunity to receive the Corresponding
+Source of your version by providing access to the Corresponding Source
+from a network server at no charge, through some standard or customary
+means of facilitating copying of software.  This Corresponding Source
+shall include the Corresponding Source for any work covered by version 3
+of the GNU General Public License that is incorporated pursuant to the
+following paragraph.
 
   Notwithstanding any other provision of this License, you have
 permission to link or combine any covered work with a work licensed
-under version 3 of the GNU Affero General Public License into a single
+under version 3 of the GNU General Public License into a single
 combined work, and to convey the resulting work.  The terms of this
 License will continue to apply to the part which is the covered work,
-but the special requirements of the GNU Affero General Public License,
-section 13, concerning interaction through a network will apply to the
-combination as such.
+but the work with which it is combined will remain governed by version
+3 of the GNU General Public License.
 
   14. Revised Versions of this License.
 
   The Free Software Foundation may publish revised and/or new versions of
-the GNU General Public License from time to time.  Such new versions will
-be similar in spirit to the present version, but may differ in detail to
+the GNU Affero General Public License from time to time.  Such new versions
+will be similar in spirit to the present version, but may differ in detail to
 address new problems or concerns.
 
   Each version is given a distinguishing version number.  If the
-Program specifies that a certain numbered version of the GNU General
+Program specifies that a certain numbered version of the GNU Affero General
 Public License "or any later version" applies to it, you have the
 option of following the terms and conditions either of that numbered
 version or of any later version published by the Free Software
 Foundation.  If the Program does not specify a version number of the
-GNU General Public License, you may choose any version ever published
+GNU Affero General Public License, you may choose any version ever published
 by the Free Software Foundation.
 
   If the Program specifies that a proxy can decide which future
-versions of the GNU General Public License can be used, that proxy's
+versions of the GNU Affero General Public License can be used, that proxy's
 public statement of acceptance of a version permanently authorizes you
 to choose that version for the Program.
 
   Later license versions may give you additional or different
 permissions.  However, no additional obligations are imposed on any
 author or copyright holder as a result of your choosing to follow a
 later version.
@@ -631,44 +629,33 @@
 state the exclusion of warranty; and each file should have at least
 the "copyright" line and a pointer to where the full notice is found.
 
     <one line to give the program's name and a brief idea of what it does.>
     Copyright (C) <year>  <name of author>
 
     This program is free software: you can redistribute it and/or modify
-    it under the terms of the GNU General Public License as published by
-    the Free Software Foundation, either version 3 of the License, or
+    it under the terms of the GNU Affero General Public License as published
+    by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
 
     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-    GNU General Public License for more details.
+    GNU Affero General Public License for more details.
 
-    You should have received a copy of the GNU General Public License
+    You should have received a copy of the GNU Affero General Public License
     along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 Also add information on how to contact you by electronic and paper mail.
 
-  If the program does terminal interaction, make it output a short
-notice like this when it starts in an interactive mode:
-
-    <program>  Copyright (C) <year>  <name of author>
-    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
-    This is free software, and you are welcome to redistribute it
-    under certain conditions; type `show c' for details.
-
-The hypothetical commands `show w' and `show c' should show the appropriate
-parts of the General Public License.  Of course, your program's commands
-might be different; for a GUI interface, you would use an "about box".
+  If your software can interact with users remotely through a computer
+network, you should also make sure that it provides a way for users to
+get its source.  For example, if your program is a web application, its
+interface could display a "Source" link that leads users to an archive
+of the code.  There are many ways you could offer source, and different
+solutions will be better for different programs; see section 13 for the
+specific requirements.
 
   You should also get your employer (if you work as a programmer) or school,
 if any, to sign a "copyright disclaimer" for the program, if necessary.
-For more information on this, and how to apply and follow the GNU GPL, see
-<https://www.gnu.org/licenses/>.
-
-  The GNU General Public License does not permit incorporating your program
-into proprietary programs.  If your program is a subroutine library, you
-may consider it more useful to permit linking proprietary applications with
-the library.  If this is what you want to do, use the GNU Lesser General
-Public License instead of this License.  But first, please read
-<https://www.gnu.org/licenses/why-not-lgpl.html>.
+For more information on this, and how to apply and follow the GNU AGPL, see
+<https://www.gnu.org/licenses/>.
```

### Comparing `hordelib-0.0.9/PKG-INFO` & `hordelib-0.1.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,87 +1,75 @@
 Metadata-Version: 2.1
 Name: hordelib
-Version: 0.0.9
+Version: 0.1.0
 Summary: A thin wrapper around ComfyUI to allow use by AI Horde.
-Author-email: Jug <jugdev@proton.me>
-License:                     GNU GENERAL PUBLIC LICENSE
-                               Version 3, 29 June 2007
+Author-email: Jug <jugdev@proton.me>, db0 <mail@dbzer0.com>
+License:                     GNU AFFERO GENERAL PUBLIC LICENSE
+                               Version 3, 19 November 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
          Everyone is permitted to copy and distribute verbatim copies
          of this license document, but changing it is not allowed.
         
                                     Preamble
         
-          The GNU General Public License is a free, copyleft license for
-        software and other kinds of works.
+          The GNU Affero General Public License is a free, copyleft license for
+        software and other kinds of works, specifically designed to ensure
+        cooperation with the community in the case of network server software.
         
           The licenses for most software and other practical works are designed
         to take away your freedom to share and change the works.  By contrast,
-        the GNU General Public License is intended to guarantee your freedom to
+        our General Public Licenses are intended to guarantee your freedom to
         share and change all versions of a program--to make sure it remains free
-        software for all its users.  We, the Free Software Foundation, use the
-        GNU General Public License for most of our software; it applies also to
-        any other work released this way by its authors.  You can apply it to
-        your programs, too.
+        software for all its users.
         
           When we speak of free software, we are referring to freedom, not
         price.  Our General Public Licenses are designed to make sure that you
         have the freedom to distribute copies of free software (and charge for
         them if you wish), that you receive source code or can get it if you
         want it, that you can change the software or use pieces of it in new
         free programs, and that you know you can do these things.
         
-          To protect your rights, we need to prevent others from denying you
-        these rights or asking you to surrender the rights.  Therefore, you have
-        certain responsibilities if you distribute copies of the software, or if
-        you modify it: responsibilities to respect the freedom of others.
-        
-          For example, if you distribute copies of such a program, whether
-        gratis or for a fee, you must pass on to the recipients the same
-        freedoms that you received.  You must make sure that they, too, receive
-        or can get the source code.  And you must show them these terms so they
-        know their rights.
-        
-          Developers that use the GNU GPL protect your rights with two steps:
-        (1) assert copyright on the software, and (2) offer you this License
-        giving you legal permission to copy, distribute and/or modify it.
-        
-          For the developers' and authors' protection, the GPL clearly explains
-        that there is no warranty for this free software.  For both users' and
-        authors' sake, the GPL requires that modified versions be marked as
-        changed, so that their problems will not be attributed erroneously to
-        authors of previous versions.
-        
-          Some devices are designed to deny users access to install or run
-        modified versions of the software inside them, although the manufacturer
-        can do so.  This is fundamentally incompatible with the aim of
-        protecting users' freedom to change the software.  The systematic
-        pattern of such abuse occurs in the area of products for individuals to
-        use, which is precisely where it is most unacceptable.  Therefore, we
-        have designed this version of the GPL to prohibit the practice for those
-        products.  If such problems arise substantially in other domains, we
-        stand ready to extend this provision to those domains in future versions
-        of the GPL, as needed to protect the freedom of users.
-        
-          Finally, every program is threatened constantly by software patents.
-        States should not allow patents to restrict development and use of
-        software on general-purpose computers, but in those that do, we wish to
-        avoid the special danger that patents applied to a free program could
-        make it effectively proprietary.  To prevent this, the GPL assures that
-        patents cannot be used to render the program non-free.
+          Developers that use our General Public Licenses protect your rights
+        with two steps: (1) assert copyright on the software, and (2) offer
+        you this License which gives you legal permission to copy, distribute
+        and/or modify the software.
+        
+          A secondary benefit of defending all users' freedom is that
+        improvements made in alternate versions of the program, if they
+        receive widespread use, become available for other developers to
+        incorporate.  Many developers of free software are heartened and
+        encouraged by the resulting cooperation.  However, in the case of
+        software used on network servers, this result may fail to come about.
+        The GNU General Public License permits making a modified version and
+        letting the public access it on a server without ever releasing its
+        source code to the public.
+        
+          The GNU Affero General Public License is designed specifically to
+        ensure that, in such cases, the modified source code becomes available
+        to the community.  It requires the operator of a network server to
+        provide the source code of the modified version running there to the
+        users of that server.  Therefore, public use of a modified version, on
+        a publicly accessible server, gives the public access to the source
+        code of the modified version.
+        
+          An older license, called the Affero General Public License and
+        published by Affero, was designed to accomplish similar goals.  This is
+        a different license, not a version of the Affero GPL, but Affero has
+        released a new version of the Affero GPL which permits relicensing under
+        this license.
         
           The precise terms and conditions for copying, distribution and
         modification follow.
         
                                TERMS AND CONDITIONS
         
           0. Definitions.
         
-          "This License" refers to version 3 of the GNU General Public License.
+          "This License" refers to version 3 of the GNU Affero General Public License.
         
           "Copyright" also means copyright-like laws that apply to other kinds of
         works, such as semiconductor masks.
         
           "The Program" refers to any copyrightable work licensed under this
         License.  Each licensee is addressed as "you".  "Licensees" and
         "recipients" may be individuals or organizations.
@@ -550,43 +538,53 @@
         covered work so as to satisfy simultaneously your obligations under this
         License and any other pertinent obligations, then as a consequence you may
         not convey it at all.  For example, if you agree to terms that obligate you
         to collect a royalty for further conveying from those to whom you convey
         the Program, the only way you could satisfy both those terms and this
         License would be to refrain entirely from conveying the Program.
         
-          13. Use with the GNU Affero General Public License.
+          13. Remote Network Interaction; Use with the GNU General Public License.
+        
+          Notwithstanding any other provision of this License, if you modify the
+        Program, your modified version must prominently offer all users
+        interacting with it remotely through a computer network (if your version
+        supports such interaction) an opportunity to receive the Corresponding
+        Source of your version by providing access to the Corresponding Source
+        from a network server at no charge, through some standard or customary
+        means of facilitating copying of software.  This Corresponding Source
+        shall include the Corresponding Source for any work covered by version 3
+        of the GNU General Public License that is incorporated pursuant to the
+        following paragraph.
         
           Notwithstanding any other provision of this License, you have
         permission to link or combine any covered work with a work licensed
-        under version 3 of the GNU Affero General Public License into a single
+        under version 3 of the GNU General Public License into a single
         combined work, and to convey the resulting work.  The terms of this
         License will continue to apply to the part which is the covered work,
-        but the special requirements of the GNU Affero General Public License,
-        section 13, concerning interaction through a network will apply to the
-        combination as such.
+        but the work with which it is combined will remain governed by version
+        3 of the GNU General Public License.
         
           14. Revised Versions of this License.
         
           The Free Software Foundation may publish revised and/or new versions of
-        the GNU General Public License from time to time.  Such new versions will
-        be similar in spirit to the present version, but may differ in detail to
+        the GNU Affero General Public License from time to time.  Such new versions
+        will be similar in spirit to the present version, but may differ in detail to
         address new problems or concerns.
         
           Each version is given a distinguishing version number.  If the
-        Program specifies that a certain numbered version of the GNU General
+        Program specifies that a certain numbered version of the GNU Affero General
         Public License "or any later version" applies to it, you have the
         option of following the terms and conditions either of that numbered
         version or of any later version published by the Free Software
         Foundation.  If the Program does not specify a version number of the
-        GNU General Public License, you may choose any version ever published
+        GNU Affero General Public License, you may choose any version ever published
         by the Free Software Foundation.
         
           If the Program specifies that a proxy can decide which future
-        versions of the GNU General Public License can be used, that proxy's
+        versions of the GNU Affero General Public License can be used, that proxy's
         public statement of acceptance of a version permanently authorizes you
         to choose that version for the Program.
         
           Later license versions may give you additional or different
         permissions.  However, no additional obligations are imposed on any
         author or copyright holder as a result of your choosing to follow a
         later version.
@@ -636,91 +634,88 @@
         state the exclusion of warranty; and each file should have at least
         the "copyright" line and a pointer to where the full notice is found.
         
             <one line to give the program's name and a brief idea of what it does.>
             Copyright (C) <year>  <name of author>
         
             This program is free software: you can redistribute it and/or modify
-            it under the terms of the GNU General Public License as published by
-            the Free Software Foundation, either version 3 of the License, or
+            it under the terms of the GNU Affero General Public License as published
+            by the Free Software Foundation, either version 3 of the License, or
             (at your option) any later version.
         
             This program is distributed in the hope that it will be useful,
             but WITHOUT ANY WARRANTY; without even the implied warranty of
             MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-            GNU General Public License for more details.
+            GNU Affero General Public License for more details.
         
-            You should have received a copy of the GNU General Public License
+            You should have received a copy of the GNU Affero General Public License
             along with this program.  If not, see <https://www.gnu.org/licenses/>.
         
         Also add information on how to contact you by electronic and paper mail.
         
-          If the program does terminal interaction, make it output a short
-        notice like this when it starts in an interactive mode:
-        
-            <program>  Copyright (C) <year>  <name of author>
-            This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
-            This is free software, and you are welcome to redistribute it
-            under certain conditions; type `show c' for details.
-        
-        The hypothetical commands `show w' and `show c' should show the appropriate
-        parts of the General Public License.  Of course, your program's commands
-        might be different; for a GUI interface, you would use an "about box".
+          If your software can interact with users remotely through a computer
+        network, you should also make sure that it provides a way for users to
+        get its source.  For example, if your program is a web application, its
+        interface could display a "Source" link that leads users to an archive
+        of the code.  There are many ways you could offer source, and different
+        solutions will be better for different programs; see section 13 for the
+        specific requirements.
         
           You should also get your employer (if you work as a programmer) or school,
         if any, to sign a "copyright disclaimer" for the program, if necessary.
-        For more information on this, and how to apply and follow the GNU GPL, see
+        For more information on this, and how to apply and follow the GNU AGPL, see
         <https://www.gnu.org/licenses/>.
-        
-          The GNU General Public License does not permit incorporating your program
-        into proprietary programs.  If your program is a subroutine library, you
-        may consider it more useful to permit linking proprietary applications with
-        the library.  If this is what you want to do, use the GNU Lesser General
-        Public License instead of this License.  But first, please read
-        <https://www.gnu.org/licenses/why-not-lgpl.html>.
 Project-URL: Homepage, https://github.com/jug-dev/hordelib
 Project-URL: Bug Tracker, https://github.com/jug-dev/hordelib/issues
 Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
+Classifier: License :: OSI Approved :: GNU Affero General Public License v3
 Classifier: Operating System :: OS Independent
 Classifier: Development Status :: 2 - Pre-Alpha
 Requires-Python: <3.11,>=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # hordelib
 
-`hordelib` is a thin wrapper around [ComfyUI](https://github.com/comfyanonymous/ComfyUI) primarily to enable the [AI Horde](https://aihorde.net/) to run inference pipelines designed in ComfyUI. `hordelib` and ComfyUI is are licensed under the terms of the GNU General Public License.
+`hordelib` is a thin wrapper around [ComfyUI](https://github.com/comfyanonymous/ComfyUI) primarily to enable the [AI Horde](https://aihorde.net/) to run inference pipelines designed in ComfyUI. `hordelib` and ComfyUI are licensed under the terms of the GNU General Public License.
+
+The developers of this project can be found in the AI Horde Discord server: https://discord.gg/3DxrhksKznb
 
 ## Purpose
 
 The goal here is to be able to design inference pipelines in the excellent ComfyUI, and then call those inference pipelines programmatically, in a manner ultimately suitable for use in stable horde.
 
 ## Installation
 
 If being installed from pypi, use a requirements file of the form:
 ```
 --extra-index-url https://download.pytorch.org/whl/cu117
 hordelib
 
-...your other dependancies...
+...your other dependencies...
 ```
 
 ## Usage
 
 Horde payloads can be processed simply with (for example):
 
 ```python
 import os
+import hordelib
+hordelib.initialise()
+
 from hordelib.horde import HordeLib
+from hordelib.shared_model_manager import SharedModelManager
 
 # Wherever your models are
 os.environ["AIWORKER_CACHE_HOME"] = "f:/ai/models"
 
 generate = HordeLib()
+SharedModelManager.loadModelManagers(compvis=True)
+SharedModelManager.manager.load("Deliberate")
 
 data = {
     "sampler_name": "k_dpmpp_2m",
     "cfg_scale": 7.5,
     "denoising_strength": 1.0,
     "seed": 123456789,
     "height": 512,
@@ -731,26 +726,42 @@
     "clip_skip": 1,
     "control_type": "canny",
     "image_is_control": False,
     "return_control_map": False,
     "prompt": "an ancient llamia monster",
     "ddim_steps": 25,
     "n_iter": 1,
-    "model": "Deliberate.ckpt",
+    "model": "Deliberate",
 }
 pil_image = generate.text_to_image(data)
 pil_image.save("test.png")
 ```
 
 ## Development
 
 Requirements:
 - `git` (install git)
 - `tox` (`pip install tox`)
-- Copy _any_ checkpoint model into the project root named `model.ckpt`
+- Set the environmental variable `AIWORKER_CACHE_HOME` to point to a model directory.
+
+Note the model directory must currently be in the original AI Horde directory structure:
+```
+<AIWORKER_CACHE_HOME>\
+   nataili\
+        clip\
+        codeformer\
+        compvis\
+            Deliberate.ckpt
+            ...etc...
+        controlnet\
+        embeds\
+        esrgan\
+        gfpgan\
+        safety_checker\
+```
 
 ### Running the Tests
 
 Simply execute: `tox` (or `tox -q` for less noisy output)
 
 This will take a while the first time as it installs all the dependencies.
 
@@ -766,57 +777,55 @@
 Contains ComfyUI pipelines in a format that can be opened by the ComfyUI web app. These saved directly from the web app.
 
 `hordelib/pipelines/`
 Contains the above pipeline JSON files converted to the format required by the backend pipeline processor. These are converted from the web app, see _Converting ComfyUI pipelines_ below.
 
 `hordelib/nodes/` These are the custom ComfyUI nodes we use for `hordelib` specific processing.
 
+### Running ComfyUI Web Application
+
+`tox -e comfyui`
+
+Then open a browser at: http://127.0.0.1:8188/
+
 ### Designing ComfyUI Pipelines
 
 Use the standard ComfyUI web app. Use the "title" attribute to name the nodes, these names become parameter names in the `hordelib`. For example, a KSampler with the "title" of "sampler2" would become a parameter `sampler2.seed`, `sampler2.cfg`, etc. Load the pipeline `hordelib/pipeline_designs/pipeline_stable_diffusion.json` in the ComfyUI web app for an example.
 
 Save any new pipeline in `hordelib/pipeline_designs` using the naming convention "pipeline_\<name\>.json".
 
 Convert the JSON for the model (see _Converting ComfyUI pipelines_ below) and save the resulting JSON in `hordelib/pipelines` using the same filename as the previous JSON file.
 
 That is all. This can then be called from `hordelib` using the `run_image_pipeline()` method in `hordelib.comfy.Comfy()`
 
 ### Converting ComfyUI pipelines
 
-The quickest way to get from a pipeline diagram in the ComfyUI web app to a usable JSON file is to simply patch the ComfyUI backend to save the JSON we require when the web app submits the inference pipeline for rendering.
-
-Patch `ComfyUI/execution.py:validate_prompt()` to include the following just before the final `return` statement:
-```python
-    with open("prompt.json", "wt", encoding="utf-8") as f:
-        f.write(json.dumps(prompt, indent=4))
-```
-
-This will create the file `prompt.json` in the root of the ComfyUI project for the submitted pipeline job.
+In addition to the design file saved from the UI, we need to save the pipeline file in the backend format. This file is created in the `hordelib` project root named `comfy-prompt.json` automatically if you run a pipeline through the ComfyUI version embedded in `hordelib`. Running ComfyUI with `tox -e comfyui` automatically patches ComfyUI so this JSON file is saved.
 
 ### Build Configuration
 
 The main config files for the project are: `pyproject.toml`, `tox.ini` and `requirements.txt`
 
 ### PyPi Publishing
 
 Three steps:
-1. Bump the version in `hordelib/__init__.py`
+1. Bump the version in `hordelib/cosnts.py`
 1. `tox` _make sure everything works_
 1. `python publish.py` _builds the dist files_
 1. `twine upload -r pypi dist/*`
 
 ### Updating the embedded version of ComfyUI
 
-We use a ComfyUI version pinned to a specific commit, see `hordelib/__init__.py:COMFYUI_VERSION`
+We use a ComfyUI version pinned to a specific commit, see `hordelib/consts.py:COMFYUI_VERSION`
 
 To test if the latest version works and upgrade to it, from the project root simply:
 
 1. `cd hordelib/Comfy` _Change CWD to the embedded comfy_
 1. `git checkout master` _Switch to master branch_
 1. `git pull` _Get the latest comfyui code_
 1. `git rev-parse HEAD` _Print the commit hash we'll need this_
 1. `cd ../../` _Get back to the hordelib project root_
 1. `tox` _See if everything still works_
 
-If everything still works. Take the commit hash printed above and put it in `hordelib/__init__.py:COMFYUI_VERSION`
+If everything still works. Take the commit hash printed above and put it in `hordelib/consts.py:COMFYUI_VERSION`
 
 Now ComfyUI is pinned to a new version.
```

### Comparing `hordelib-0.0.9/README.md` & `hordelib-0.1.0/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -1,37 +1,45 @@
 # hordelib
 
-`hordelib` is a thin wrapper around [ComfyUI](https://github.com/comfyanonymous/ComfyUI) primarily to enable the [AI Horde](https://aihorde.net/) to run inference pipelines designed in ComfyUI. `hordelib` and ComfyUI is are licensed under the terms of the GNU General Public License.
+`hordelib` is a thin wrapper around [ComfyUI](https://github.com/comfyanonymous/ComfyUI) primarily to enable the [AI Horde](https://aihorde.net/) to run inference pipelines designed in ComfyUI. `hordelib` and ComfyUI are licensed under the terms of the GNU General Public License.
+
+The developers of this project can be found in the AI Horde Discord server: https://discord.gg/3DxrhksKznb
 
 ## Purpose
 
 The goal here is to be able to design inference pipelines in the excellent ComfyUI, and then call those inference pipelines programmatically, in a manner ultimately suitable for use in stable horde.
 
 ## Installation
 
 If being installed from pypi, use a requirements file of the form:
 ```
 --extra-index-url https://download.pytorch.org/whl/cu117
 hordelib
 
-...your other dependancies...
+...your other dependencies...
 ```
 
 ## Usage
 
 Horde payloads can be processed simply with (for example):
 
 ```python
 import os
+import hordelib
+hordelib.initialise()
+
 from hordelib.horde import HordeLib
+from hordelib.shared_model_manager import SharedModelManager
 
 # Wherever your models are
 os.environ["AIWORKER_CACHE_HOME"] = "f:/ai/models"
 
 generate = HordeLib()
+SharedModelManager.loadModelManagers(compvis=True)
+SharedModelManager.manager.load("Deliberate")
 
 data = {
     "sampler_name": "k_dpmpp_2m",
     "cfg_scale": 7.5,
     "denoising_strength": 1.0,
     "seed": 123456789,
     "height": 512,
@@ -42,26 +50,42 @@
     "clip_skip": 1,
     "control_type": "canny",
     "image_is_control": False,
     "return_control_map": False,
     "prompt": "an ancient llamia monster",
     "ddim_steps": 25,
     "n_iter": 1,
-    "model": "Deliberate.ckpt",
+    "model": "Deliberate",
 }
 pil_image = generate.text_to_image(data)
 pil_image.save("test.png")
 ```
 
 ## Development
 
 Requirements:
 - `git` (install git)
 - `tox` (`pip install tox`)
-- Copy _any_ checkpoint model into the project root named `model.ckpt`
+- Set the environmental variable `AIWORKER_CACHE_HOME` to point to a model directory.
+
+Note the model directory must currently be in the original AI Horde directory structure:
+```
+<AIWORKER_CACHE_HOME>\
+   nataili\
+        clip\
+        codeformer\
+        compvis\
+            Deliberate.ckpt
+            ...etc...
+        controlnet\
+        embeds\
+        esrgan\
+        gfpgan\
+        safety_checker\
+```
 
 ### Running the Tests
 
 Simply execute: `tox` (or `tox -q` for less noisy output)
 
 This will take a while the first time as it installs all the dependencies.
 
@@ -77,57 +101,55 @@
 Contains ComfyUI pipelines in a format that can be opened by the ComfyUI web app. These saved directly from the web app.
 
 `hordelib/pipelines/`
 Contains the above pipeline JSON files converted to the format required by the backend pipeline processor. These are converted from the web app, see _Converting ComfyUI pipelines_ below.
 
 `hordelib/nodes/` These are the custom ComfyUI nodes we use for `hordelib` specific processing.
 
+### Running ComfyUI Web Application
+
+`tox -e comfyui`
+
+Then open a browser at: http://127.0.0.1:8188/
+
 ### Designing ComfyUI Pipelines
 
 Use the standard ComfyUI web app. Use the "title" attribute to name the nodes, these names become parameter names in the `hordelib`. For example, a KSampler with the "title" of "sampler2" would become a parameter `sampler2.seed`, `sampler2.cfg`, etc. Load the pipeline `hordelib/pipeline_designs/pipeline_stable_diffusion.json` in the ComfyUI web app for an example.
 
 Save any new pipeline in `hordelib/pipeline_designs` using the naming convention "pipeline_\<name\>.json".
 
 Convert the JSON for the model (see _Converting ComfyUI pipelines_ below) and save the resulting JSON in `hordelib/pipelines` using the same filename as the previous JSON file.
 
 That is all. This can then be called from `hordelib` using the `run_image_pipeline()` method in `hordelib.comfy.Comfy()`
 
 ### Converting ComfyUI pipelines
 
-The quickest way to get from a pipeline diagram in the ComfyUI web app to a usable JSON file is to simply patch the ComfyUI backend to save the JSON we require when the web app submits the inference pipeline for rendering.
-
-Patch `ComfyUI/execution.py:validate_prompt()` to include the following just before the final `return` statement:
-```python
-    with open("prompt.json", "wt", encoding="utf-8") as f:
-        f.write(json.dumps(prompt, indent=4))
-```
-
-This will create the file `prompt.json` in the root of the ComfyUI project for the submitted pipeline job.
+In addition to the design file saved from the UI, we need to save the pipeline file in the backend format. This file is created in the `hordelib` project root named `comfy-prompt.json` automatically if you run a pipeline through the ComfyUI version embedded in `hordelib`. Running ComfyUI with `tox -e comfyui` automatically patches ComfyUI so this JSON file is saved.
 
 ### Build Configuration
 
 The main config files for the project are: `pyproject.toml`, `tox.ini` and `requirements.txt`
 
 ### PyPi Publishing
 
 Three steps:
-1. Bump the version in `hordelib/__init__.py`
+1. Bump the version in `hordelib/cosnts.py`
 1. `tox` _make sure everything works_
 1. `python publish.py` _builds the dist files_
 1. `twine upload -r pypi dist/*`
 
 ### Updating the embedded version of ComfyUI
 
-We use a ComfyUI version pinned to a specific commit, see `hordelib/__init__.py:COMFYUI_VERSION`
+We use a ComfyUI version pinned to a specific commit, see `hordelib/consts.py:COMFYUI_VERSION`
 
 To test if the latest version works and upgrade to it, from the project root simply:
 
 1. `cd hordelib/Comfy` _Change CWD to the embedded comfy_
 1. `git checkout master` _Switch to master branch_
 1. `git pull` _Get the latest comfyui code_
 1. `git rev-parse HEAD` _Print the commit hash we'll need this_
 1. `cd ../../` _Get back to the hordelib project root_
 1. `tox` _See if everything still works_
 
-If everything still works. Take the commit hash printed above and put it in `hordelib/__init__.py:COMFYUI_VERSION`
+If everything still works. Take the commit hash printed above and put it in `hordelib/consts.py:COMFYUI_VERSION`
 
 Now ComfyUI is pinned to a new version.
```

### Comparing `hordelib-0.0.9/hordelib/comfy.py` & `hordelib-0.1.0/hordelib/comfy_horde.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,128 +1,137 @@
 # comfy.py
 # Wrapper around comfy to allow usage by the horde worker.
 import copy
 import glob
 import json
 import os
 import re
-from PIL import Image
 from io import BytesIO
 
 from loguru import logger
+from PIL import Image
 
-from hordelib.ComfyUI import execution
-
+# Do not change the order of these imports
+# fmt: off
+import execution
+from comfy.sd import load_checkpoint_guess_config
+# fmt: on
 
-class Comfy:
+class Comfy_Horde:
+    """Handles horde-specific behavior against ComfyUI."""
 
     # Lookup of ComfyUI standard nodes to hordelib custom nodes
     NODE_REPLACEMENTS = {
         "CheckpointLoaderSimple": "HordeCheckpointLoader",
         "SaveImage": "HordeImageOutput",
     }
 
-    def __init__(self):
+    def __init__(self) -> None:
         self.pipelines = {}
         self.unit_testing = os.getenv("HORDELIB_TESTING", "")
 
-        # FIXME Temporary hack for model dir
+        # XXX Temporary hack for model dir
         model_dir = os.getenv("AIWORKER_CACHE_HOME", "")
         if not model_dir:
             os.environ["HORDE_MODEL_DIR_CHECKPOINTS"] = self._this_dir("../")
         else:
             os.environ["HORDE_MODEL_DIR_CHECKPOINTS"] = os.path.join(
                 model_dir, "nataili", "compvis"
             )
 
         # Load our pipelines
         self._load_pipelines()
 
-    def _this_dir(self, filename, subdir=""):
+    def _this_dir(self, filename: str, subdir="") -> str:
         target_dir = os.path.dirname(os.path.realpath(__file__))
         if subdir:
             target_dir = os.path.join(target_dir, subdir)
         return os.path.join(target_dir, filename)
 
-    def _load_node(self, filename):
+    def _load_node(self, filename: str) -> None:
         try:
             execution.nodes.load_custom_node(self._this_dir(filename, subdir="nodes"))
         except Exception:
             logger.error(f"Failed to load custom pipeline node: {filename}")
             return
         logger.debug(f"Loaded custom pipeline node: {filename}")
 
-    def _load_custom_nodes(self):
+    def _load_custom_nodes(self) -> None:
         files = glob.glob(self._this_dir("node_*.py", subdir="nodes"))
         for file in files:
             self._load_node(os.path.basename(file))
 
-    def _fix_pipeline_types(self, data):
+    def _fix_pipeline_types(self, data: dict) -> dict:
         # We have a list of nodes and each node has a class type, which we may want to change
         for nodename, node in data.items():
-            if "class_type" in node:
-                if node["class_type"] in Comfy.NODE_REPLACEMENTS:
-                    data[nodename]["class_type"] = Comfy.NODE_REPLACEMENTS[
-                        node["class_type"]
-                    ]
+            if ("class_type" in node) and (
+                node["class_type"] in Comfy_Horde.NODE_REPLACEMENTS
+            ):
+                data[nodename]["class_type"] = Comfy_Horde.NODE_REPLACEMENTS[
+                    node["class_type"]
+                ]
         return data
 
-    def _fix_node_names(self, data, design):
+    def _fix_node_names(self, data: dict, design: dict) -> dict:
         # We have a list of nodes, attempt to rename them to the "title" set
         # in the design file. These must be unique names.
         newnodes = {}
         renames = {}
         nodes = design["nodes"]
         for nodename, oldnode in data.items():
             newname = nodename
             for node in nodes:
-                if str(node["id"]) == str(nodename):
-                    if "title" in node:
-                        newname = node["title"]
-                        break
+                if str(node["id"]) == str(nodename) and "title" in node:
+                    newname = node["title"]
+                    break
             renames[nodename] = newname
             newnodes[newname] = oldnode
         # Now we've renamed the node names, change any references to them also
-        for nodename, node in newnodes.items():
+        for node in newnodes.values():
             if "inputs" in node:
                 for _, input in node["inputs"].items():
                     if type(input) is list:
                         if input and input[0] in renames:
                             input[0] = renames[input[0]]
         return newnodes
 
     # We are passed a valid comfy pipeline and a design file from the comfyui web app.
     # Why?
     #
     # 1. We replace some nodes with our own hordelib nodes, for example "CheckpointLoaderSimple"
-    #    with "HordeModelLoader".
+    #    with "HordeCheckpointLoader".
     # 2. We replace unfriendly node names like "3" and "7" with friendly names taken from the
     #    "title" attribute in the webui so we can have nicer parameter names when we call the
     #    inference pipeline.
     #
     # Note that point 1 does not actually need a design file, and point 2 is not technically
     # essential.
     #
     # Note also that the format of the design files from web app is expected to change at a fast
     # pace. This is why the only thing that partially relies on that format, is in fact, optional.
-    def _patch_pipeline(self, data, design):
+    def _patch_pipeline(self, data: dict, design: dict) -> dict:
         # First replace comfyui standard types with hordelib node types
         data = self._fix_pipeline_types(data)
         # Now try to find better parameter names
         data = self._fix_node_names(data, design)
         return data
 
-    def _load_pipeline(self, filename):
+    def _load_pipeline(self, filename: str) -> bool | None:
         if not os.path.exists(filename):
             logger.error(f"No such inference pipeline file: {filename}")
-            return
+            return None
 
         try:
             with open(filename) as jsonfile:
-                pipeline_name = re.match(r".*pipeline_(.*)\.json", filename)[1]
+                pipeline_name_rematches = re.match(r".*pipeline_(.*)\.json", filename)
+                if pipeline_name_rematches is None:
+                    logger.error(f"Regex parsing failed for: {filename}")
+                    return None
+
+                pipeline_name = pipeline_name_rematches[1]
                 data = json.loads(jsonfile.read())
                 # Do we have a design file for this pipeline?
                 design = os.path.join(
                     os.path.dirname(os.path.dirname(filename)),
                     "pipeline_designs",
                     os.path.basename(filename),
                 )
@@ -134,51 +143,56 @@
                     data = self._patch_pipeline(data, designdata)
                 self.pipelines[pipeline_name] = data
                 logger.debug(f"Loaded inference pipeline: {pipeline_name}")
                 return True
         except (OSError, ValueError):
             logger.error(f"Invalid inference pipeline file: {filename}")
 
-    def _load_pipelines(self):
+    def _load_pipelines(self) -> int:
         files = glob.glob(self._this_dir("pipeline_*.json", subdir="pipelines"))
         loaded_count = 0
         for file in files:
             if self._load_pipeline(file):
                 loaded_count += 1
         return loaded_count
 
     # Inject parameters into a pre-configured pipeline
     # We allow "inputs" to be missing from the key name, if it is we insert it.
-    def _set(self, dct, **kwargs):
+    def _set(self, dct, **kwargs) -> None:
         for key, value in kwargs.items():
             keys = key.split(".")
             if "inputs" not in keys:
                 keys.insert(1, "inputs")
             current = dct
 
             for k in keys[:-1]:
                 if k not in current:
                     logger.error(f"Attempt to set unknown pipeline parameter {key}")
                     break
-                else:
-                    current = current[k]
+
+                current = current[k]
 
             current[keys[-1]] = value
 
     # Execute the named pipeline and pass the pipeline the parameter provided.
     # For the horde we assume the pipeline returns an array of images.
-    def run_pipeline(self, pipeline_name, params):
-
+    def run_pipeline(self, pipeline_name: str, params: dict) -> dict | None:
         # Sanity
         if pipeline_name not in self.pipelines:
             logger.error(f"Unknown inference pipeline: {pipeline_name}")
-            return
+            return None
 
         # Grab a copy of the pipeline
         pipeline = copy.copy(self.pipelines[pipeline_name])
+
+        # Inject our model manager if required
+        from hordelib.shared_model_manager import SharedModelManager
+        if "model_loader.model_manager" not in params:
+            params["model_loader.model_manager"] = SharedModelManager
+
         # Set the pipeline parameters
         self._set(pipeline, **params)
 
         # Fake it!
         if self.unit_testing:
             img = Image.new("RGB", (64, 64), (0, 0, 0))
             byte_stream = BytesIO()
@@ -194,19 +208,23 @@
         # Load our custom nodes
         self._load_custom_nodes()
         inference.execute(pipeline)
 
         return inference.outputs
 
     # Run a pipeline that returns an image in pixel space
-    def run_image_pipeline(self, pipeline_name, params):
+    def run_image_pipeline(self, pipeline_name: str, params: dict) -> list[dict] | None:
         # From the horde point of view, let us assume the output we are interested in
         # is always in a HordeImageOutput node named "output_image". This is an array of
         # dicts of the form:
         # [ {
         #     "imagedata": <BytesIO>,
         #     "type": "PNG"
         #   },
         # ]
         # See node_image_output.py
         result = self.run_pipeline(pipeline_name, params)
-        return result["output_image"]["images"]
+
+        if result:
+            return result["output_image"]["images"]
+
+        return None
```

### Comparing `hordelib-0.0.9/hordelib/nodes/node_image_output.py` & `hordelib-0.1.0/hordelib/nodes/node_image_output.py`

 * *Files 5% similar despite different names*

```diff
@@ -22,27 +22,27 @@
     FUNCTION = "get_image"
 
     OUTPUT_NODE = True
 
     CATEGORY = "image"
 
     def get_image(self, images, prompt=None, extra_pnginfo=None):
-
         results = []
         for image in images:
             # Create a PNG
             i = 255.0 * image.cpu().numpy()
             img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
             metadata = PngInfo()
             # Save the full pipeline and variables into the PNG metadata
-            if prompt is not None:
-                metadata.add_text("prompt", json.dumps(prompt))
-            if extra_pnginfo is not None:
-                for x in extra_pnginfo:
-                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))
+            # FIXME we don't have a model manager JSON serialiser
+            # if prompt is not None:
+            #     metadata.add_text("prompt", json.dumps(prompt))
+            # if extra_pnginfo is not None:
+            #     for x in extra_pnginfo:
+            #         metadata.add_text(x, json.dumps(extra_pnginfo[x]))
 
             byte_stream = BytesIO()
             img.save(byte_stream, format="PNG", pnginfo=metadata, compress_level=4)
             byte_stream.seek(0)
 
             results.append({"imagedata": byte_stream, "type": "PNG"})
```

### Comparing `hordelib-0.0.9/hordelib/pipeline_designs/pipeline_stable_diffusion.json` & `hordelib-0.1.0/hordelib/pipeline_designs/pipeline_stable_diffusion.json`

 * *Files 3% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.8209025065104167%*

 * *Differences: {"'last_link_id'": '13',*

 * * "'last_node_id'": '10',*

 * * "'links'": "{insert: [(7, [11, 10, 0, 6, 0, 'CLIP']), (8, [12, 4, 1, 10, 0, 'CLIP']), (9, [13, "*

 * *            "10, 0, 7, 0, 'CLIP'])], delete: [4, 2]}",*

 * * "'nodes'": "{0: {'id': 5, 'type': 'EmptyLatentImage', 'pos': [510, 549], 'size': {'0': 315, '1': "*

 * *            "106}, 'order': 0, 'outputs': {0: {'name': 'LATENT', 'type': 'LATENT', 'links': [2]}}, "*

 * *            "'title': 'empty_latent_image', 'properties': {'Node name for S&R': "*

 * *            "'EmptyLatentI […]*

```diff
@@ -1,13 +1,13 @@
 {
     "config": {},
     "extra": {},
     "groups": [],
-    "last_link_id": 9,
-    "last_node_id": 9,
+    "last_link_id": 13,
+    "last_node_id": 10,
     "links": [
         [
             1,
             4,
             0,
             3,
             0,
@@ -18,38 +18,22 @@
             5,
             0,
             3,
             3,
             "LATENT"
         ],
         [
-            3,
-            4,
-            1,
-            6,
-            0,
-            "CLIP"
-        ],
-        [
             4,
             6,
             0,
             3,
             1,
             "CONDITIONING"
         ],
         [
-            5,
-            4,
-            1,
-            7,
-            0,
-            "CLIP"
-        ],
-        [
             6,
             7,
             0,
             3,
             2,
             "CONDITIONING"
         ],
@@ -72,128 +56,142 @@
         [
             9,
             8,
             0,
             9,
             0,
             "IMAGE"
+        ],
+        [
+            11,
+            10,
+            0,
+            6,
+            0,
+            "CLIP"
+        ],
+        [
+            12,
+            4,
+            1,
+            10,
+            0,
+            "CLIP"
+        ],
+        [
+            13,
+            10,
+            0,
+            7,
+            0,
+            "CLIP"
         ]
     ],
     "nodes": [
         {
             "flags": {},
-            "id": 7,
-            "inputs": [
-                {
-                    "link": 5,
-                    "name": "clip",
-                    "type": "CLIP"
-                }
-            ],
+            "id": 5,
             "mode": 0,
-            "order": 3,
+            "order": 0,
             "outputs": [
                 {
                     "links": [
-                        6
+                        2
                     ],
-                    "name": "CONDITIONING",
+                    "name": "LATENT",
                     "slot_index": 0,
-                    "type": "CONDITIONING"
+                    "type": "LATENT"
                 }
             ],
             "pos": [
-                413,
-                389
+                510,
+                549
             ],
             "properties": {
-                "Node name for S&R": "CLIPTextEncode"
+                "Node name for S&R": "EmptyLatentImage"
             },
             "size": {
-                "0": 425.27801513671875,
-                "1": 180.6060791015625
+                "0": 315,
+                "1": 106
             },
-            "title": "negative_prompt",
-            "type": "CLIPTextEncode",
+            "title": "empty_latent_image",
+            "type": "EmptyLatentImage",
             "widgets_values": [
-                "bad hands"
+                512,
+                512,
+                1
             ]
         },
         {
             "flags": {},
-            "id": 6,
+            "id": 9,
             "inputs": [
                 {
-                    "link": 3,
-                    "name": "clip",
-                    "type": "CLIP"
+                    "link": 9,
+                    "name": "images",
+                    "type": "IMAGE"
                 }
             ],
             "mode": 0,
-            "order": 2,
-            "outputs": [
-                {
-                    "links": [
-                        4
-                    ],
-                    "name": "CONDITIONING",
-                    "slot_index": 0,
-                    "type": "CONDITIONING"
-                }
-            ],
+            "order": 7,
             "pos": [
-                415,
-                186
+                1627,
+                432
             ],
-            "properties": {
-                "Node name for S&R": "CLIPTextEncode"
-            },
+            "properties": {},
             "size": {
-                "0": 422.84503173828125,
-                "1": 164.31304931640625
+                "0": 210,
+                "1": 58
             },
-            "title": "prompt",
-            "type": "CLIPTextEncode",
+            "title": "output_image",
+            "type": "SaveImage",
             "widgets_values": [
-                "masterpiece best quality girl"
+                "ComfyUI"
             ]
         },
         {
             "flags": {},
-            "id": 5,
+            "id": 8,
+            "inputs": [
+                {
+                    "link": 7,
+                    "name": "samples",
+                    "type": "LATENT"
+                },
+                {
+                    "link": 8,
+                    "name": "vae",
+                    "type": "VAE"
+                }
+            ],
             "mode": 0,
-            "order": 0,
+            "order": 6,
             "outputs": [
                 {
                     "links": [
-                        2
+                        9
                     ],
-                    "name": "LATENT",
+                    "name": "IMAGE",
                     "slot_index": 0,
-                    "type": "LATENT"
+                    "type": "IMAGE"
                 }
             ],
             "pos": [
-                473,
-                609
+                1384,
+                398
             ],
             "properties": {
-                "Node name for S&R": "EmptyLatentImage"
+                "Node name for S&R": "VAEDecode"
             },
             "size": {
-                "0": 315,
-                "1": 106
+                "0": 210,
+                "1": 46
             },
-            "title": "empty_latent_image",
-            "type": "EmptyLatentImage",
-            "widgets_values": [
-                512,
-                512,
-                1
-            ]
+            "title": "vae",
+            "type": "VAEDecode"
         },
         {
             "flags": {},
             "id": 3,
             "inputs": [
                 {
                     "link": 1,
@@ -213,28 +211,28 @@
                 {
                     "link": 2,
                     "name": "latent_image",
                     "type": "LATENT"
                 }
             ],
             "mode": 0,
-            "order": 4,
+            "order": 5,
             "outputs": [
                 {
                     "links": [
                         7
                     ],
                     "name": "LATENT",
                     "slot_index": 0,
                     "type": "LATENT"
                 }
             ],
             "pos": [
-                863,
-                186
+                1019,
+                107
             ],
             "properties": {
                 "Node name for S&R": "KSampler"
             },
             "size": {
                 "0": 315,
                 "1": 262
@@ -249,125 +247,175 @@
                 "euler",
                 "normal",
                 1
             ]
         },
         {
             "flags": {},
-            "id": 8,
-            "inputs": [
-                {
-                    "link": 7,
-                    "name": "samples",
-                    "type": "LATENT"
-                },
-                {
-                    "link": 8,
-                    "name": "vae",
-                    "type": "VAE"
-                }
-            ],
+            "id": 4,
             "mode": 0,
-            "order": 5,
+            "order": 1,
             "outputs": [
                 {
                     "links": [
-                        9
+                        1
                     ],
-                    "name": "IMAGE",
+                    "name": "MODEL",
                     "slot_index": 0,
-                    "type": "IMAGE"
+                    "type": "MODEL"
+                },
+                {
+                    "links": [
+                        12
+                    ],
+                    "name": "CLIP",
+                    "slot_index": 1,
+                    "type": "CLIP"
+                },
+                {
+                    "links": [
+                        8
+                    ],
+                    "name": "VAE",
+                    "slot_index": 2,
+                    "type": "VAE"
                 }
             ],
             "pos": [
-                1209,
-                188
+                23,
+                254
             ],
             "properties": {
-                "Node name for S&R": "VAEDecode"
+                "Node name for S&R": "CheckpointLoaderSimple"
             },
             "size": {
-                "0": 210,
-                "1": 46
+                "0": 315,
+                "1": 98
             },
-            "title": "vae",
-            "type": "VAEDecode"
+            "title": "model_loader",
+            "type": "CheckpointLoaderSimple",
+            "widgets_values": [
+                "v1-5-pruned-emaonly.ckpt"
+            ]
         },
         {
             "flags": {},
-            "id": 9,
+            "id": 7,
             "inputs": [
                 {
-                    "link": 9,
-                    "name": "images",
-                    "type": "IMAGE"
+                    "link": 13,
+                    "name": "clip",
+                    "slot_index": 0,
+                    "type": "CLIP"
                 }
             ],
             "mode": 0,
-            "order": 6,
+            "order": 4,
+            "outputs": [
+                {
+                    "links": [
+                        6
+                    ],
+                    "name": "CONDITIONING",
+                    "slot_index": 0,
+                    "type": "CONDITIONING"
+                }
+            ],
             "pos": [
-                1451,
-                189
+                588,
+                409
             ],
-            "properties": {},
-            "size": {
-                "0": 210,
-                "1": 58
+            "properties": {
+                "Node name for S&R": "CLIPTextEncode"
             },
-            "title": "output_image",
-            "type": "SaveImage",
+            "size": [
+                243.0001220703125,
+                90.3333740234375
+            ],
+            "title": "negative_prompt",
+            "type": "CLIPTextEncode",
             "widgets_values": [
-                "ComfyUI"
+                "bad hands"
             ]
         },
         {
             "flags": {},
-            "id": 4,
+            "id": 6,
+            "inputs": [
+                {
+                    "link": 11,
+                    "name": "clip",
+                    "type": "CLIP"
+                }
+            ],
             "mode": 0,
-            "order": 1,
+            "order": 3,
             "outputs": [
                 {
                     "links": [
-                        1
+                        4
                     ],
-                    "name": "MODEL",
+                    "name": "CONDITIONING",
                     "slot_index": 0,
-                    "type": "MODEL"
-                },
+                    "type": "CONDITIONING"
+                }
+            ],
+            "pos": [
+                650,
+                54
+            ],
+            "properties": {
+                "Node name for S&R": "CLIPTextEncode"
+            },
+            "size": [
+                236.33343505859375,
+                83.00006103515625
+            ],
+            "title": "prompt",
+            "type": "CLIPTextEncode",
+            "widgets_values": [
+                "masterpiece best quality girl"
+            ]
+        },
+        {
+            "flags": {},
+            "id": 10,
+            "inputs": [
                 {
-                    "links": [
-                        3,
-                        5
-                    ],
-                    "name": "CLIP",
-                    "slot_index": 1,
+                    "link": 12,
+                    "name": "clip",
                     "type": "CLIP"
-                },
+                }
+            ],
+            "mode": 0,
+            "order": 2,
+            "outputs": [
                 {
                     "links": [
-                        8
+                        11,
+                        13
                     ],
-                    "name": "VAE",
-                    "slot_index": 2,
-                    "type": "VAE"
+                    "name": "CLIP",
+                    "slot_index": 0,
+                    "type": "CLIP"
                 }
             ],
             "pos": [
-                26,
-                474
+                376,
+                145
             ],
             "properties": {
-                "Node name for S&R": "CheckpointLoaderSimple"
+                "Node name for S&R": "CLIPSetLastLayer"
             },
-            "size": {
-                "0": 315,
-                "1": 98
-            },
-            "title": "model_loader",
-            "type": "CheckpointLoaderSimple",
+            "size": [
+                210,
+                58
+            ],
+            "title": "clip_skip",
+            "type": "CLIPSetLastLayer",
             "widgets_values": [
-                "v1-5-pruned-emaonly.ckpt"
+                -1
             ]
         }
     ],
     "version": 0.4
 }
```

### Comparing `hordelib-0.0.9/hordelib/pipelines/pipeline_stable_diffusion.json` & `hordelib-0.1.0/hordelib/pipelines/pipeline_stable_diffusion.json`

 * *Files 10% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.86640625%*

 * *Differences: {"'10'": "OrderedDict([('inputs', OrderedDict([('stop_at_clip_layer', -1), ('clip', ['4', 1])])), "*

 * *         "('class_type', 'CLIPSetLastLayer')])",*

 * * "'3'": "{'inputs': {'seed': 449976276651529}}",*

 * * "'6'": "{'inputs': {'clip': ['10', 0]}}",*

 * * "'7'": "{'inputs': {'clip': ['10', 0]}}"}*

```diff
@@ -1,8 +1,18 @@
 {
+    "10": {
+        "class_type": "CLIPSetLastLayer",
+        "inputs": {
+            "clip": [
+                "4",
+                1
+            ],
+            "stop_at_clip_layer": -1
+        }
+    },
     "3": {
         "class_type": "KSampler",
         "inputs": {
             "cfg": 8.0,
             "denoise": 1.0,
             "latent_image": [
                 "5",
@@ -18,15 +28,15 @@
             ],
             "positive": [
                 "6",
                 0
             ],
             "sampler_name": "euler",
             "scheduler": "normal",
-            "seed": 8566257,
+            "seed": 449976276651529,
             "steps": 20
         }
     },
     "4": {
         "class_type": "CheckpointLoaderSimple",
         "inputs": {
             "ckpt_name": "Deliberate.ckpt"
@@ -40,26 +50,26 @@
             "width": 512
         }
     },
     "6": {
         "class_type": "CLIPTextEncode",
         "inputs": {
             "clip": [
-                "4",
-                1
+                "10",
+                0
             ],
             "text": "masterpiece best quality girl"
         }
     },
     "7": {
         "class_type": "CLIPTextEncode",
         "inputs": {
             "clip": [
-                "4",
-                1
+                "10",
+                0
             ],
             "text": "bad hands"
         }
     },
     "8": {
         "class_type": "VAEDecode",
         "inputs": {
```

### Comparing `hordelib-0.0.9/hordelib/pipelines/pipeline_stable_diffusion_hires_fix.json` & `hordelib-0.1.0/hordelib/pipelines/pipeline_stable_diffusion_hires_fix.json`

 * *Files identical despite different names*

### Comparing `hordelib-0.0.9/hordelib.egg-info/PKG-INFO` & `hordelib-0.1.0/hordelib.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,87 +1,75 @@
 Metadata-Version: 2.1
 Name: hordelib
-Version: 0.0.9
+Version: 0.1.0
 Summary: A thin wrapper around ComfyUI to allow use by AI Horde.
-Author-email: Jug <jugdev@proton.me>
-License:                     GNU GENERAL PUBLIC LICENSE
-                               Version 3, 29 June 2007
+Author-email: Jug <jugdev@proton.me>, db0 <mail@dbzer0.com>
+License:                     GNU AFFERO GENERAL PUBLIC LICENSE
+                               Version 3, 19 November 2007
         
          Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
          Everyone is permitted to copy and distribute verbatim copies
          of this license document, but changing it is not allowed.
         
                                     Preamble
         
-          The GNU General Public License is a free, copyleft license for
-        software and other kinds of works.
+          The GNU Affero General Public License is a free, copyleft license for
+        software and other kinds of works, specifically designed to ensure
+        cooperation with the community in the case of network server software.
         
           The licenses for most software and other practical works are designed
         to take away your freedom to share and change the works.  By contrast,
-        the GNU General Public License is intended to guarantee your freedom to
+        our General Public Licenses are intended to guarantee your freedom to
         share and change all versions of a program--to make sure it remains free
-        software for all its users.  We, the Free Software Foundation, use the
-        GNU General Public License for most of our software; it applies also to
-        any other work released this way by its authors.  You can apply it to
-        your programs, too.
+        software for all its users.
         
           When we speak of free software, we are referring to freedom, not
         price.  Our General Public Licenses are designed to make sure that you
         have the freedom to distribute copies of free software (and charge for
         them if you wish), that you receive source code or can get it if you
         want it, that you can change the software or use pieces of it in new
         free programs, and that you know you can do these things.
         
-          To protect your rights, we need to prevent others from denying you
-        these rights or asking you to surrender the rights.  Therefore, you have
-        certain responsibilities if you distribute copies of the software, or if
-        you modify it: responsibilities to respect the freedom of others.
-        
-          For example, if you distribute copies of such a program, whether
-        gratis or for a fee, you must pass on to the recipients the same
-        freedoms that you received.  You must make sure that they, too, receive
-        or can get the source code.  And you must show them these terms so they
-        know their rights.
-        
-          Developers that use the GNU GPL protect your rights with two steps:
-        (1) assert copyright on the software, and (2) offer you this License
-        giving you legal permission to copy, distribute and/or modify it.
-        
-          For the developers' and authors' protection, the GPL clearly explains
-        that there is no warranty for this free software.  For both users' and
-        authors' sake, the GPL requires that modified versions be marked as
-        changed, so that their problems will not be attributed erroneously to
-        authors of previous versions.
-        
-          Some devices are designed to deny users access to install or run
-        modified versions of the software inside them, although the manufacturer
-        can do so.  This is fundamentally incompatible with the aim of
-        protecting users' freedom to change the software.  The systematic
-        pattern of such abuse occurs in the area of products for individuals to
-        use, which is precisely where it is most unacceptable.  Therefore, we
-        have designed this version of the GPL to prohibit the practice for those
-        products.  If such problems arise substantially in other domains, we
-        stand ready to extend this provision to those domains in future versions
-        of the GPL, as needed to protect the freedom of users.
-        
-          Finally, every program is threatened constantly by software patents.
-        States should not allow patents to restrict development and use of
-        software on general-purpose computers, but in those that do, we wish to
-        avoid the special danger that patents applied to a free program could
-        make it effectively proprietary.  To prevent this, the GPL assures that
-        patents cannot be used to render the program non-free.
+          Developers that use our General Public Licenses protect your rights
+        with two steps: (1) assert copyright on the software, and (2) offer
+        you this License which gives you legal permission to copy, distribute
+        and/or modify the software.
+        
+          A secondary benefit of defending all users' freedom is that
+        improvements made in alternate versions of the program, if they
+        receive widespread use, become available for other developers to
+        incorporate.  Many developers of free software are heartened and
+        encouraged by the resulting cooperation.  However, in the case of
+        software used on network servers, this result may fail to come about.
+        The GNU General Public License permits making a modified version and
+        letting the public access it on a server without ever releasing its
+        source code to the public.
+        
+          The GNU Affero General Public License is designed specifically to
+        ensure that, in such cases, the modified source code becomes available
+        to the community.  It requires the operator of a network server to
+        provide the source code of the modified version running there to the
+        users of that server.  Therefore, public use of a modified version, on
+        a publicly accessible server, gives the public access to the source
+        code of the modified version.
+        
+          An older license, called the Affero General Public License and
+        published by Affero, was designed to accomplish similar goals.  This is
+        a different license, not a version of the Affero GPL, but Affero has
+        released a new version of the Affero GPL which permits relicensing under
+        this license.
         
           The precise terms and conditions for copying, distribution and
         modification follow.
         
                                TERMS AND CONDITIONS
         
           0. Definitions.
         
-          "This License" refers to version 3 of the GNU General Public License.
+          "This License" refers to version 3 of the GNU Affero General Public License.
         
           "Copyright" also means copyright-like laws that apply to other kinds of
         works, such as semiconductor masks.
         
           "The Program" refers to any copyrightable work licensed under this
         License.  Each licensee is addressed as "you".  "Licensees" and
         "recipients" may be individuals or organizations.
@@ -550,43 +538,53 @@
         covered work so as to satisfy simultaneously your obligations under this
         License and any other pertinent obligations, then as a consequence you may
         not convey it at all.  For example, if you agree to terms that obligate you
         to collect a royalty for further conveying from those to whom you convey
         the Program, the only way you could satisfy both those terms and this
         License would be to refrain entirely from conveying the Program.
         
-          13. Use with the GNU Affero General Public License.
+          13. Remote Network Interaction; Use with the GNU General Public License.
+        
+          Notwithstanding any other provision of this License, if you modify the
+        Program, your modified version must prominently offer all users
+        interacting with it remotely through a computer network (if your version
+        supports such interaction) an opportunity to receive the Corresponding
+        Source of your version by providing access to the Corresponding Source
+        from a network server at no charge, through some standard or customary
+        means of facilitating copying of software.  This Corresponding Source
+        shall include the Corresponding Source for any work covered by version 3
+        of the GNU General Public License that is incorporated pursuant to the
+        following paragraph.
         
           Notwithstanding any other provision of this License, you have
         permission to link or combine any covered work with a work licensed
-        under version 3 of the GNU Affero General Public License into a single
+        under version 3 of the GNU General Public License into a single
         combined work, and to convey the resulting work.  The terms of this
         License will continue to apply to the part which is the covered work,
-        but the special requirements of the GNU Affero General Public License,
-        section 13, concerning interaction through a network will apply to the
-        combination as such.
+        but the work with which it is combined will remain governed by version
+        3 of the GNU General Public License.
         
           14. Revised Versions of this License.
         
           The Free Software Foundation may publish revised and/or new versions of
-        the GNU General Public License from time to time.  Such new versions will
-        be similar in spirit to the present version, but may differ in detail to
+        the GNU Affero General Public License from time to time.  Such new versions
+        will be similar in spirit to the present version, but may differ in detail to
         address new problems or concerns.
         
           Each version is given a distinguishing version number.  If the
-        Program specifies that a certain numbered version of the GNU General
+        Program specifies that a certain numbered version of the GNU Affero General
         Public License "or any later version" applies to it, you have the
         option of following the terms and conditions either of that numbered
         version or of any later version published by the Free Software
         Foundation.  If the Program does not specify a version number of the
-        GNU General Public License, you may choose any version ever published
+        GNU Affero General Public License, you may choose any version ever published
         by the Free Software Foundation.
         
           If the Program specifies that a proxy can decide which future
-        versions of the GNU General Public License can be used, that proxy's
+        versions of the GNU Affero General Public License can be used, that proxy's
         public statement of acceptance of a version permanently authorizes you
         to choose that version for the Program.
         
           Later license versions may give you additional or different
         permissions.  However, no additional obligations are imposed on any
         author or copyright holder as a result of your choosing to follow a
         later version.
@@ -636,91 +634,88 @@
         state the exclusion of warranty; and each file should have at least
         the "copyright" line and a pointer to where the full notice is found.
         
             <one line to give the program's name and a brief idea of what it does.>
             Copyright (C) <year>  <name of author>
         
             This program is free software: you can redistribute it and/or modify
-            it under the terms of the GNU General Public License as published by
-            the Free Software Foundation, either version 3 of the License, or
+            it under the terms of the GNU Affero General Public License as published
+            by the Free Software Foundation, either version 3 of the License, or
             (at your option) any later version.
         
             This program is distributed in the hope that it will be useful,
             but WITHOUT ANY WARRANTY; without even the implied warranty of
             MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-            GNU General Public License for more details.
+            GNU Affero General Public License for more details.
         
-            You should have received a copy of the GNU General Public License
+            You should have received a copy of the GNU Affero General Public License
             along with this program.  If not, see <https://www.gnu.org/licenses/>.
         
         Also add information on how to contact you by electronic and paper mail.
         
-          If the program does terminal interaction, make it output a short
-        notice like this when it starts in an interactive mode:
-        
-            <program>  Copyright (C) <year>  <name of author>
-            This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
-            This is free software, and you are welcome to redistribute it
-            under certain conditions; type `show c' for details.
-        
-        The hypothetical commands `show w' and `show c' should show the appropriate
-        parts of the General Public License.  Of course, your program's commands
-        might be different; for a GUI interface, you would use an "about box".
+          If your software can interact with users remotely through a computer
+        network, you should also make sure that it provides a way for users to
+        get its source.  For example, if your program is a web application, its
+        interface could display a "Source" link that leads users to an archive
+        of the code.  There are many ways you could offer source, and different
+        solutions will be better for different programs; see section 13 for the
+        specific requirements.
         
           You should also get your employer (if you work as a programmer) or school,
         if any, to sign a "copyright disclaimer" for the program, if necessary.
-        For more information on this, and how to apply and follow the GNU GPL, see
+        For more information on this, and how to apply and follow the GNU AGPL, see
         <https://www.gnu.org/licenses/>.
-        
-          The GNU General Public License does not permit incorporating your program
-        into proprietary programs.  If your program is a subroutine library, you
-        may consider it more useful to permit linking proprietary applications with
-        the library.  If this is what you want to do, use the GNU Lesser General
-        Public License instead of this License.  But first, please read
-        <https://www.gnu.org/licenses/why-not-lgpl.html>.
 Project-URL: Homepage, https://github.com/jug-dev/hordelib
 Project-URL: Bug Tracker, https://github.com/jug-dev/hordelib/issues
 Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
+Classifier: License :: OSI Approved :: GNU Affero General Public License v3
 Classifier: Operating System :: OS Independent
 Classifier: Development Status :: 2 - Pre-Alpha
 Requires-Python: <3.11,>=3.10
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # hordelib
 
-`hordelib` is a thin wrapper around [ComfyUI](https://github.com/comfyanonymous/ComfyUI) primarily to enable the [AI Horde](https://aihorde.net/) to run inference pipelines designed in ComfyUI. `hordelib` and ComfyUI is are licensed under the terms of the GNU General Public License.
+`hordelib` is a thin wrapper around [ComfyUI](https://github.com/comfyanonymous/ComfyUI) primarily to enable the [AI Horde](https://aihorde.net/) to run inference pipelines designed in ComfyUI. `hordelib` and ComfyUI are licensed under the terms of the GNU General Public License.
+
+The developers of this project can be found in the AI Horde Discord server: https://discord.gg/3DxrhksKznb
 
 ## Purpose
 
 The goal here is to be able to design inference pipelines in the excellent ComfyUI, and then call those inference pipelines programmatically, in a manner ultimately suitable for use in stable horde.
 
 ## Installation
 
 If being installed from pypi, use a requirements file of the form:
 ```
 --extra-index-url https://download.pytorch.org/whl/cu117
 hordelib
 
-...your other dependancies...
+...your other dependencies...
 ```
 
 ## Usage
 
 Horde payloads can be processed simply with (for example):
 
 ```python
 import os
+import hordelib
+hordelib.initialise()
+
 from hordelib.horde import HordeLib
+from hordelib.shared_model_manager import SharedModelManager
 
 # Wherever your models are
 os.environ["AIWORKER_CACHE_HOME"] = "f:/ai/models"
 
 generate = HordeLib()
+SharedModelManager.loadModelManagers(compvis=True)
+SharedModelManager.manager.load("Deliberate")
 
 data = {
     "sampler_name": "k_dpmpp_2m",
     "cfg_scale": 7.5,
     "denoising_strength": 1.0,
     "seed": 123456789,
     "height": 512,
@@ -731,26 +726,42 @@
     "clip_skip": 1,
     "control_type": "canny",
     "image_is_control": False,
     "return_control_map": False,
     "prompt": "an ancient llamia monster",
     "ddim_steps": 25,
     "n_iter": 1,
-    "model": "Deliberate.ckpt",
+    "model": "Deliberate",
 }
 pil_image = generate.text_to_image(data)
 pil_image.save("test.png")
 ```
 
 ## Development
 
 Requirements:
 - `git` (install git)
 - `tox` (`pip install tox`)
-- Copy _any_ checkpoint model into the project root named `model.ckpt`
+- Set the environmental variable `AIWORKER_CACHE_HOME` to point to a model directory.
+
+Note the model directory must currently be in the original AI Horde directory structure:
+```
+<AIWORKER_CACHE_HOME>\
+   nataili\
+        clip\
+        codeformer\
+        compvis\
+            Deliberate.ckpt
+            ...etc...
+        controlnet\
+        embeds\
+        esrgan\
+        gfpgan\
+        safety_checker\
+```
 
 ### Running the Tests
 
 Simply execute: `tox` (or `tox -q` for less noisy output)
 
 This will take a while the first time as it installs all the dependencies.
 
@@ -766,57 +777,55 @@
 Contains ComfyUI pipelines in a format that can be opened by the ComfyUI web app. These saved directly from the web app.
 
 `hordelib/pipelines/`
 Contains the above pipeline JSON files converted to the format required by the backend pipeline processor. These are converted from the web app, see _Converting ComfyUI pipelines_ below.
 
 `hordelib/nodes/` These are the custom ComfyUI nodes we use for `hordelib` specific processing.
 
+### Running ComfyUI Web Application
+
+`tox -e comfyui`
+
+Then open a browser at: http://127.0.0.1:8188/
+
 ### Designing ComfyUI Pipelines
 
 Use the standard ComfyUI web app. Use the "title" attribute to name the nodes, these names become parameter names in the `hordelib`. For example, a KSampler with the "title" of "sampler2" would become a parameter `sampler2.seed`, `sampler2.cfg`, etc. Load the pipeline `hordelib/pipeline_designs/pipeline_stable_diffusion.json` in the ComfyUI web app for an example.
 
 Save any new pipeline in `hordelib/pipeline_designs` using the naming convention "pipeline_\<name\>.json".
 
 Convert the JSON for the model (see _Converting ComfyUI pipelines_ below) and save the resulting JSON in `hordelib/pipelines` using the same filename as the previous JSON file.
 
 That is all. This can then be called from `hordelib` using the `run_image_pipeline()` method in `hordelib.comfy.Comfy()`
 
 ### Converting ComfyUI pipelines
 
-The quickest way to get from a pipeline diagram in the ComfyUI web app to a usable JSON file is to simply patch the ComfyUI backend to save the JSON we require when the web app submits the inference pipeline for rendering.
-
-Patch `ComfyUI/execution.py:validate_prompt()` to include the following just before the final `return` statement:
-```python
-    with open("prompt.json", "wt", encoding="utf-8") as f:
-        f.write(json.dumps(prompt, indent=4))
-```
-
-This will create the file `prompt.json` in the root of the ComfyUI project for the submitted pipeline job.
+In addition to the design file saved from the UI, we need to save the pipeline file in the backend format. This file is created in the `hordelib` project root named `comfy-prompt.json` automatically if you run a pipeline through the ComfyUI version embedded in `hordelib`. Running ComfyUI with `tox -e comfyui` automatically patches ComfyUI so this JSON file is saved.
 
 ### Build Configuration
 
 The main config files for the project are: `pyproject.toml`, `tox.ini` and `requirements.txt`
 
 ### PyPi Publishing
 
 Three steps:
-1. Bump the version in `hordelib/__init__.py`
+1. Bump the version in `hordelib/cosnts.py`
 1. `tox` _make sure everything works_
 1. `python publish.py` _builds the dist files_
 1. `twine upload -r pypi dist/*`
 
 ### Updating the embedded version of ComfyUI
 
-We use a ComfyUI version pinned to a specific commit, see `hordelib/__init__.py:COMFYUI_VERSION`
+We use a ComfyUI version pinned to a specific commit, see `hordelib/consts.py:COMFYUI_VERSION`
 
 To test if the latest version works and upgrade to it, from the project root simply:
 
 1. `cd hordelib/Comfy` _Change CWD to the embedded comfy_
 1. `git checkout master` _Switch to master branch_
 1. `git pull` _Get the latest comfyui code_
 1. `git rev-parse HEAD` _Print the commit hash we'll need this_
 1. `cd ../../` _Get back to the hordelib project root_
 1. `tox` _See if everything still works_
 
-If everything still works. Take the commit hash printed above and put it in `hordelib/__init__.py:COMFYUI_VERSION`
+If everything still works. Take the commit hash printed above and put it in `hordelib/consts.py:COMFYUI_VERSION`
 
 Now ComfyUI is pinned to a new version.
```

### Comparing `hordelib-0.0.9/publish.py` & `hordelib-0.1.0/publish.py`

 * *Files 9% similar despite different names*

```diff
@@ -16,15 +16,15 @@
     for line in data:
         if not unpatch and line.startswith("--"):
             newfile.append(f"#{line}")
         elif unpatch and line.startswith("#--"):
             newfile.append(f"{line[1:]}")
         else:
             newfile.append(line)
-    with open("requirements.txt", "wt") as outfile:
+    with open("requirements.txt", "w") as outfile:
         outfile.writelines(newfile)
 
 
 def patch_toml(unpatch=False):
     with open("pyproject.toml") as infile:
         data = infile.readlines()
     newfile = []
@@ -35,15 +35,15 @@
             newfile.append(f"{line[1:]}")
         elif unpatch and line.startswith('#dynamic=["version"]'):
             newfile.append(f"{line[1:]}")
         elif unpatch and line.startswith('dynamic=["version", "dependencies"]'):
             newfile.append(f"#{line}")
         else:
             newfile.append(line)
-    with open("pyproject.toml", "wt") as outfile:
+    with open("pyproject.toml", "w") as outfile:
         outfile.writelines(newfile)
 
 
 patch_requirements()
 patch_toml()
 
 try:
```

### Comparing `hordelib-0.0.9/pyproject.toml` & `hordelib-0.1.0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -3,35 +3,36 @@
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "hordelib"
 description = "A thin wrapper around ComfyUI to allow use by AI Horde."
 authors = [
     {name = "Jug", email = "jugdev@proton.me"},
+    {name = "db0", email = "mail@dbzer0.com"},
 ]
 readme = "README.md"
 requires-python = ">=3.10,<3.11"
 license = { file="LICENSE" }
 classifiers = [
     "Programming Language :: Python :: 3",
-    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
+    "License :: OSI Approved :: GNU Affero General Public License v3",
     "Operating System :: OS Independent",
     "Development Status :: 2 - Pre-Alpha",
 ]
 
 # Don't specify dynamic deps for tox, only for build
 #dynamic=["version"]
 dynamic=["version", "dependencies"]
 
 [project.urls]
 "Homepage" = "https://github.com/jug-dev/hordelib"
 "Bug Tracker" = "https://github.com/jug-dev/hordelib/issues"
 
 [tool.setuptools.dynamic]
-version = {attr = "hordelib.VERSION"}
+version = {attr = "hordelib.consts.VERSION"}
 dependencies = {file = ["requirements.txt"]}
 
 [tool.setuptools.packages.find]
 exclude = ["hordelib.ComfyUI"]
 namespaces = false
 
 [options.index-client]
```

### Comparing `hordelib-0.0.9/tests/test_comfy.py` & `hordelib-0.1.0/tests/test_comfy.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,46 +1,47 @@
 # test_setup.py
 import pytest
-from hordelib.comfy import Comfy
 
+from hordelib.comfy_horde import Comfy_Horde
 
-class TestSetup:
 
+class TestSetup:
     NUMBER_OF_PIPELINES = 2
+    comfy: Comfy_Horde
 
     @pytest.fixture(autouse=True)
     def setup_and_teardown(self):
-        self.comfy = Comfy()
+        self.comfy = Comfy_Horde()
         yield
-        self.comfy = None
+        del self.comfy
 
     def test_load_pipelines(self):
         loaded = self.comfy._load_pipelines()
         assert loaded == TestSetup.NUMBER_OF_PIPELINES
         # Check the built in pipelines
-        assert "stable_diffusion" in self.comfy.pipelines.keys()
-        assert "stable_diffusion_hires_fix" in self.comfy.pipelines.keys()
+        assert "stable_diffusion" in self.comfy.pipelines
+        assert "stable_diffusion_hires_fix" in self.comfy.pipelines
 
     def test_load_invalid_pipeline(self):
         loaded = self.comfy._load_pipeline("no-such-pipeline")
         assert loaded is None
 
     def test_load_invalid_node(self, capsys):
         self.comfy._load_node("no-such-node")
         captured = capsys.readouterr()
         assert "No such file or directory" in str(captured)
 
     def test_load_custom_nodes(self):
         self.comfy._load_custom_nodes()
 
         # Look for our nodes in the ComfyUI nodes list
-        from hordelib.ComfyUI import execution
+        import execution
 
-        assert "HordeCheckpointLoader" in execution.nodes.NODE_CLASS_MAPPINGS.keys()
-        assert "HordeImageOutput" in execution.nodes.NODE_CLASS_MAPPINGS.keys()
+        assert "HordeCheckpointLoader" in execution.nodes.NODE_CLASS_MAPPINGS
+        assert "HordeImageOutput" in execution.nodes.NODE_CLASS_MAPPINGS
 
     def test_parameter_injection(self):
         test_dict = {
             "a": {
                 "inputs": {"b": False},
             },
             "c": {"inputs": {"d": {"e": False, "f": False}}},
```

### Comparing `hordelib-0.0.9/tests/test_inference.py` & `hordelib-0.1.0/tests/test_inference.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,19 +1,28 @@
 # test_inference.py
 import pytest
-from hordelib.comfy import Comfy
 from PIL import Image
 
+from hordelib.comfy_horde import Comfy_Horde
+from hordelib.shared_model_manager import SharedModelManager
+
 
 class TestInference:
+    comfy: Comfy_Horde
+
     @pytest.fixture(autouse=True)
     def setup_and_teardown(self):
-        self.comfy = Comfy()
+        self.comfy = Comfy_Horde()
+        SharedModelManager.loadModelManagers(compvis=True)
+        assert SharedModelManager.manager is not None
+        SharedModelManager.manager.load("Deliberate")
         yield
-        self.comfy = None
+        del self.comfy
+        SharedModelManager._instance = None
+        SharedModelManager.manager = None
 
     def test_unknown_pipeline(self):
         result = self.comfy.run_pipeline("non-existent-pipeline", {})
         assert result is None
 
     def test_stable_diffusion_pipeline(self):
         params = {
@@ -24,45 +33,70 @@
             "empty_latent_image.width": 768,
             "empty_latent_image.height": 768,
             "empty_latent_image.batch_size": 1,
             "sampler.scheduler": "karras",
             "sampler.steps": 25,
             "prompt.text": "a closeup photo of a confused dog",
             "negative_prompt.text": "cat, black and white, deformed",
-            "model_loader.ckpt_name": "model.ckpt",
+            "model_loader.ckpt_name": "Deliberate",
+            "clip_skip.stop_at_clip_layer": -1,
         }
         images = self.comfy.run_image_pipeline("stable_diffusion", params)
+        assert images is not None
 
         image = Image.open(images[0]["imagedata"])
         image.save("pipeline_stable_diffusion.png")
 
+    def test_stable_diffusion_pipeline_clip_skip(self):
+        params = {
+            "sampler.sampler_name": "dpmpp_2m",
+            "sampler.cfg": 7.5,
+            "sampler.denoise": 1.0,
+            "sampler.seed": 12345,
+            "empty_latent_image.width": 768,
+            "empty_latent_image.height": 768,
+            "empty_latent_image.batch_size": 1,
+            "sampler.scheduler": "karras",
+            "sampler.steps": 25,
+            "prompt.text": "a closeup photo of a confused dog",
+            "negative_prompt.text": "cat, black and white, deformed",
+            "model_loader.ckpt_name": "Deliberate",
+            "clip_skip.stop_at_clip_layer": -2,
+        }
+        images = self.comfy.run_image_pipeline("stable_diffusion", params)
+        assert images is not None
+
+        image = Image.open(images[0]["imagedata"])
+        image.save("pipeline_stable_diffusion_clip_skip_2.png")
+
     def test_stable_diffusion_hires_fix_pipeline(self):
         params = {
             "sampler.seed": 12345,
             "sampler.cfg": 7.5,
             "sampler.scheduler": "normal",
             "sampler.sampler_name": "dpmpp_sde",
             "sampler.denoise": 1.0,
             "sampler.steps": 12,
             "prompt.text": (
                 "(masterpiece) HDR victorian portrait painting of (girl), "
                 "blonde hair, mountain nature, blue sky"
             ),
             "negative_prompt.text": "bad hands, text, watermark",
-            "model_loader.ckpt_name": "model.ckpt",
+            "model_loader.ckpt_name": "Deliberate",
             "empty_latent_image.width": 768,
             "empty_latent_image.height": 768,
             "latent_upscale.width": 1216,
             "latent_upscale.height": 1216,
             "latent_upscale.crop": "disabled",
             "latent_upscale.upscale_method": "nearest-exact",
             "upscale_sampler.seed": 45678,
             "upscale_sampler.steps": 15,
             "upscale_sampler.cfg": 8.0,
             "upscale_sampler.sampler_name": "dpmpp_2m",
             "upscale_sampler.scheduler": "simple",
             "upscale_sampler.denoise": 0.5,
         }
         images = self.comfy.run_image_pipeline("stable_diffusion_hires_fix", params)
+        assert images is not None
 
         image = Image.open(images[0]["imagedata"])
         image.save("pipeline_stable_diffusion_hires_fix.png")
```

### Comparing `hordelib-0.0.9/tox.ini` & `hordelib-0.1.0/tox.ini`

 * *Files 11% similar despite different names*

```diff
@@ -1,40 +1,51 @@
 00000000: 5b74 6f78 5d0d 0a65 6e76 5f6c 6973 7420  [tox]..env_list 
-00000010: 3d0d 0a20 2020 2066 6f72 6d61 740d 0a20  =..    format.. 
-00000020: 2020 2074 6573 7473 0d0a 0d0a 5b74 6573     tests....[tes
-00000030: 7465 6e76 5d0d 0a64 6573 6372 6970 7469  tenv]..descripti
-00000040: 6f6e 203d 2062 6173 6520 6576 6972 6f6e  on = base eviron
-00000050: 6d65 6e74 2077 6974 6820 616c 6c20 6465  ment with all de
-00000060: 7065 6e64 616e 6369 6573 0d0a 7061 7373  pendancies..pass
-00000070: 656e 7620 3d0d 0a20 2020 2048 4f52 4445  env =..    HORDE
-00000080: 4c49 425f 5445 5354 494e 470d 0a64 6570  LIB_TESTING..dep
-00000090: 7320 3d0d 0a20 2020 2070 7974 6573 743e  s =..    pytest>
-000000a0: 3d37 0d0a 2020 2020 7079 7465 7374 2d73  =7..    pytest-s
-000000b0: 7567 6172 0d0a 2020 2020 7079 7465 7374  ugar..    pytest
-000000c0: 2d63 6f76 0d0a 2020 2020 7265 7175 6573  -cov..    reques
-000000d0: 7473 0d0a 2020 2020 7069 6c6c 6f77 0d0a  ts..    pillow..
-000000e0: 2020 2020 2d72 2072 6571 7569 7265 6d65      -r requireme
-000000f0: 6e74 732e 7478 740d 0a0d 0a5b 7465 7374  nts.txt....[test
-00000100: 656e 763a 666f 726d 6174 5d0d 0a64 6573  env:format]..des
-00000110: 6372 6970 7469 6f6e 203d 206c 696e 7420  cription = lint 
-00000120: 6368 6563 6b20 616e 6420 7265 666f 726d  check and reform
-00000130: 6174 0d0a 7061 7373 656e 7620 3d0d 0a20  at..passenv =.. 
-00000140: 2020 2048 4f52 4445 4c49 425f 5445 5354     HORDELIB_TEST
-00000150: 494e 470d 0a64 6570 7320 3d0d 0a20 2020  ING..deps =..   
-00000160: 2062 6c61 636b 3d3d 3232 2e33 2e30 0d0a   black==22.3.0..
-00000170: 736b 6970 5f69 6e73 7461 6c6c 203d 2074  skip_install = t
-00000180: 7275 650d 0a63 6f6d 6d61 6e64 7320 3d20  rue..commands = 
-00000190: 626c 6163 6b20 2e0d 0a0d 0a5b 7465 7374  black .....[test
-000001a0: 656e 763a 7465 7374 735d 0d0a 6465 7363  env:tests]..desc
-000001b0: 7269 7074 696f 6e20 3d20 696e 7374 616c  ription = instal
-000001c0: 6c20 7079 7465 7374 2069 6e20 6120 7669  l pytest in a vi
-000001d0: 7274 7561 6c20 656e 7669 726f 6e6d 656e  rtual environmen
-000001e0: 7420 616e 6420 696e 766f 6b65 2069 7420  t and invoke it 
-000001f0: 6f6e 2074 6865 2074 6573 7473 2066 6f6c  on the tests fol
-00000200: 6465 720d 0a70 6173 7365 6e76 203d 0d0a  der..passenv =..
-00000210: 2020 2020 484f 5244 454c 4942 5f54 4553      HORDELIB_TES
-00000220: 5449 4e47 0d0a 636f 6d6d 616e 6473 203d  TING..commands =
-00000230: 0d0a 2020 2020 7079 7465 7374 2074 6573  ..    pytest tes
-00000240: 7473 207b 706f 7361 7267 737d 202d 2d63  ts {posargs} --c
-00000250: 6f76 202d 2d63 6f76 2d72 6570 6f72 743d  ov --cov-report=
-00000260: 7465 726d 202d 2d63 6f76 2d72 6570 6f72  term --cov-repor
-00000270: 743d 6c63 6f76 0d0a                      t=lcov..
+00000010: 3d0d 0a20 2020 2074 6573 7473 0d0a 0d0a  =..    tests....
+00000020: 5b74 6573 7465 6e76 5d0d 0a64 6573 6372  [testenv]..descr
+00000030: 6970 7469 6f6e 203d 2062 6173 6520 6576  iption = base ev
+00000040: 6972 6f6e 6d65 6e74 2077 6974 6820 616c  ironment with al
+00000050: 6c20 6465 7065 6e64 616e 6369 6573 0d0a  l dependancies..
+00000060: 7061 7373 656e 7620 3d0d 0a20 2020 2048  passenv =..    H
+00000070: 4f52 4445 4c49 425f 5445 5354 494e 470d  ORDELIB_TESTING.
+00000080: 0a20 2020 2041 4957 4f52 4b45 525f 4341  .    AIWORKER_CA
+00000090: 4348 455f 484f 4d45 0d0a 6465 7073 203d  CHE_HOME..deps =
+000000a0: 0d0a 2020 2020 7079 7465 7374 3e3d 370d  ..    pytest>=7.
+000000b0: 0a20 2020 2070 7974 6573 742d 7375 6761  .    pytest-suga
+000000c0: 720d 0a20 2020 2070 7974 6573 742d 636f  r..    pytest-co
+000000d0: 760d 0a20 2020 2072 6571 7565 7374 730d  v..    requests.
+000000e0: 0a20 2020 202d 7220 7265 7175 6972 656d  .    -r requirem
+000000f0: 656e 7473 2e74 7874 0d0a 0d0a 5b74 6573  ents.txt....[tes
+00000100: 7465 6e76 3a66 6f72 6d61 745d 0d0a 6465  tenv:format]..de
+00000110: 7363 7269 7074 696f 6e20 3d20 6c69 6e74  scription = lint
+00000120: 2063 6865 636b 2061 6e64 2072 6566 6f72   check and refor
+00000130: 6d61 740d 0a70 6173 7365 6e76 203d 0d0a  mat..passenv =..
+00000140: 2020 2020 484f 5244 454c 4942 5f54 4553      HORDELIB_TES
+00000150: 5449 4e47 0d0a 2020 2020 4149 574f 524b  TING..    AIWORK
+00000160: 4552 5f43 4143 4845 5f48 4f4d 450d 0a64  ER_CACHE_HOME..d
+00000170: 6570 7320 3d0d 0a20 2020 2062 6c61 636b  eps =..    black
+00000180: 3d3d 3232 2e33 2e30 0d0a 736b 6970 5f69  ==22.3.0..skip_i
+00000190: 6e73 7461 6c6c 203d 2074 7275 650d 0a63  nstall = true..c
+000001a0: 6f6d 6d61 6e64 7320 3d20 626c 6163 6b20  ommands = black 
+000001b0: 2e0d 0a0d 0a5b 7465 7374 656e 763a 636f  .....[testenv:co
+000001c0: 6d66 7975 695d 0d0a 6465 7363 7269 7074  mfyui]..descript
+000001d0: 696f 6e20 3d20 7275 6e20 636f 6d66 7975  ion = run comfyu
+000001e0: 690d 0a73 6b69 705f 696e 7374 616c 6c20  i..skip_install 
+000001f0: 3d20 7472 7565 0d0a 636f 6d6d 616e 6473  = true..commands
+00000200: 203d 0d0a 2020 2020 7b65 6e76 7079 7468   =..    {envpyth
+00000210: 6f6e 7d20 2d6d 2068 6f72 6465 6c69 622e  on} -m hordelib.
+00000220: 7275 6e5f 636f 6d66 7975 690d 0a0d 0a5b  run_comfyui....[
+00000230: 7465 7374 656e 763a 7465 7374 735d 0d0a  testenv:tests]..
+00000240: 6465 7363 7269 7074 696f 6e20 3d20 696e  description = in
+00000250: 7374 616c 6c20 7079 7465 7374 2069 6e20  stall pytest in 
+00000260: 6120 7669 7274 7561 6c20 656e 7669 726f  a virtual enviro
+00000270: 6e6d 656e 7420 616e 6420 696e 766f 6b65  nment and invoke
+00000280: 2069 7420 6f6e 2074 6865 2074 6573 7473   it on the tests
+00000290: 2066 6f6c 6465 720d 0a70 6173 7365 6e76   folder..passenv
+000002a0: 203d 0d0a 2020 2020 484f 5244 454c 4942   =..    HORDELIB
+000002b0: 5f54 4553 5449 4e47 0d0a 2020 2020 4149  _TESTING..    AI
+000002c0: 574f 524b 4552 5f43 4143 4845 5f48 4f4d  WORKER_CACHE_HOM
+000002d0: 450d 0a63 6f6d 6d61 6e64 7320 3d0d 0a20  E..commands =.. 
+000002e0: 2020 2070 7974 6573 7420 7465 7374 7320     pytest tests 
+000002f0: 7b70 6f73 6172 6773 7d20 2d2d 636f 7620  {posargs} --cov 
+00000300: 2d2d 636f 762d 7265 706f 7274 3d74 6572  --cov-report=ter
+00000310: 6d20 2d2d 636f 762d 7265 706f 7274 3d6c  m --cov-report=l
+00000320: 636f 760d 0a                             cov..
```

