# Comparing `tmp/augraphy-8.2.0.tar.gz` & `tmp/augraphy-8.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "augraphy-8.2.0.tar", last modified: Mon Apr  3 11:32:32 2023, max compression
+gzip compressed data, was "augraphy-8.2.1.tar", last modified: Thu Apr  6 13:14:06 2023, max compression
```

## Comparing `augraphy-8.2.0.tar` & `augraphy-8.2.1.tar`

### file list

```diff
@@ -1,65 +1,65 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.625525 augraphy-8.2.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-03 11:32:20.000000 augraphy-8.2.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     8950 2023-04-03 11:32:32.625525 augraphy-8.2.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7448 2023-04-03 11:32:20.000000 augraphy-8.2.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.617524 augraphy-8.2.0/augraphy/
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.621524 augraphy-8.2.0/augraphy/augmentations/
--rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13658 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/badphotocopy.py
--rw-r--r--   0 runner    (1001) docker     (123)    21095 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/bindingsandfasteners.py
--rw-r--r--   0 runner    (1001) docker     (123)     8019 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/bleedthrough.py
--rw-r--r--   0 runner    (1001) docker     (123)    13178 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/bookbinding.py
--rw-r--r--   0 runner    (1001) docker     (123)     3856 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/brightness.py
--rw-r--r--   0 runner    (1001) docker     (123)     3509 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/brightnesstexturize.py
--rw-r--r--   0 runner    (1001) docker     (123)     2140 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/colorpaper.py
--rw-r--r--   0 runner    (1001) docker     (123)    10562 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/dirtydrum.py
--rw-r--r--   0 runner    (1001) docker     (123)     8716 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/dirtyrollers.py
--rw-r--r--   0 runner    (1001) docker     (123)     7563 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/dithering.py
--rw-r--r--   0 runner    (1001) docker     (123)    14347 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/faxify.py
--rw-r--r--   0 runner    (1001) docker     (123)     6164 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/folding.py
--rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/gamma.py
--rw-r--r--   0 runner    (1001) docker     (123)    13048 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/geometric.py
--rw-r--r--   0 runner    (1001) docker     (123)     3124 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/inkbleed.py
--rw-r--r--   0 runner    (1001) docker     (123)     1279 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/jpeg.py
--rw-r--r--   0 runner    (1001) docker     (123)     5118 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/letterpress.py
--rw-r--r--   0 runner    (1001) docker     (123)    17941 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/lib.py
--rw-r--r--   0 runner    (1001) docker     (123)     9169 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/lightinggradient.py
--rw-r--r--   0 runner    (1001) docker     (123)     6252 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/lowinkline.py
--rw-r--r--   0 runner    (1001) docker     (123)     3905 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/lowinkperiodiclines.py
--rw-r--r--   0 runner    (1001) docker     (123)     1840 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/lowinkrandomlines.py
--rw-r--r--   0 runner    (1001) docker     (123)    19480 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/markup.py
--rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/noisetexturize.py
--rw-r--r--   0 runner    (1001) docker     (123)    15090 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/pageborder.py
--rw-r--r--   0 runner    (1001) docker     (123)     7118 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/pencilscribbles.py
--rw-r--r--   0 runner    (1001) docker     (123)     1983 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/subtlenoise.py
--rw-r--r--   0 runner    (1001) docker     (123)     9377 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/augmentations/watermark.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.625525 augraphy-8.2.0/augraphy/base/
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      833 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/augmentation.py
--rw-r--r--   0 runner    (1001) docker     (123)    24009 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/augmentationpipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)      699 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/augmentationresult.py
--rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/augmentationsequence.py
--rw-r--r--   0 runner    (1001) docker     (123)     2205 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/oneof.py
--rw-r--r--   0 runner    (1001) docker     (123)     8979 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/base/paperfactory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.625525 augraphy-8.2.0/augraphy/default/
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/default/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    18605 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/default/pipeline.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.625525 augraphy-8.2.0/augraphy/utilities/
--rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      949 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/composepipelines.py
--rw-r--r--   0 runner    (1001) docker     (123)     3868 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/figsharedownloader.py
--rw-r--r--   0 runner    (1001) docker     (123)     1411 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/function.py
--rw-r--r--   0 runner    (1001) docker     (123)     4119 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/imageoverlay.py
--rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/interop.py
--rw-r--r--   0 runner    (1001) docker     (123)    17618 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/noisegenerator.py
--rw-r--r--   0 runner    (1001) docker     (123)    35472 2023-04-03 11:32:20.000000 augraphy-8.2.0/augraphy/utilities/overlaybuilder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 11:32:32.617524 augraphy-8.2.0/augraphy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8950 2023-04-03 11:32:32.000000 augraphy-8.2.0/augraphy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1876 2023-04-03 11:32:32.000000 augraphy-8.2.0/augraphy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 11:32:32.000000 augraphy-8.2.0/augraphy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-03 11:32:32.000000 augraphy-8.2.0/augraphy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-03 11:32:32.000000 augraphy-8.2.0/augraphy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-03 11:32:20.000000 augraphy-8.2.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 11:32:32.625525 augraphy-8.2.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1111 2023-04-03 11:32:20.000000 augraphy-8.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.160456 augraphy-8.2.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-06 13:13:58.000000 augraphy-8.2.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     8670 2023-04-06 13:14:06.160456 augraphy-8.2.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7216 2023-04-06 13:13:58.000000 augraphy-8.2.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.152457 augraphy-8.2.1/augraphy/
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.156456 augraphy-8.2.1/augraphy/augmentations/
+-rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13658 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/badphotocopy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21095 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/bindingsandfasteners.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8019 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/bleedthrough.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13178 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/bookbinding.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3856 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/brightness.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3509 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/brightnesstexturize.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2140 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/colorpaper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10562 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/dirtydrum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8716 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/dirtyrollers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7563 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/dithering.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14347 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/faxify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6164 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/folding.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/gamma.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14091 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/geometric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3124 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/inkbleed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1279 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/jpeg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5118 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/letterpress.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17941 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/lib.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9169 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/lightinggradient.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6252 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/lowinkline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3905 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/lowinkperiodiclines.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1840 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/lowinkrandomlines.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19480 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/markup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3560 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/noisetexturize.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15090 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/pageborder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7118 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/pencilscribbles.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1983 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/subtlenoise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9377 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/augmentations/watermark.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.156456 augraphy-8.2.1/augraphy/base/
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      833 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/augmentation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26818 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/augmentationpipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)      699 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/augmentationresult.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/augmentationsequence.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2205 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/oneof.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8979 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/base/paperfactory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.160456 augraphy-8.2.1/augraphy/default/
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/default/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23261 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/default/pipeline.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.160456 augraphy-8.2.1/augraphy/utilities/
+-rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      949 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/composepipelines.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3868 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/figsharedownloader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1411 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/function.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4119 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/imageoverlay.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1344 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/interop.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17728 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/noisegenerator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35472 2023-04-06 13:13:58.000000 augraphy-8.2.1/augraphy/utilities/overlaybuilder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:14:06.156456 augraphy-8.2.1/augraphy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8670 2023-04-06 13:14:06.000000 augraphy-8.2.1/augraphy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1876 2023-04-06 13:14:06.000000 augraphy-8.2.1/augraphy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:14:06.000000 augraphy-8.2.1/augraphy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-06 13:14:06.000000 augraphy-8.2.1/augraphy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 13:14:06.000000 augraphy-8.2.1/augraphy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 13:13:58.000000 augraphy-8.2.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:14:06.160456 augraphy-8.2.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-04-06 13:13:58.000000 augraphy-8.2.1/setup.py
```

### Comparing `augraphy-8.2.0/LICENSE` & `augraphy-8.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/PKG-INFO` & `augraphy-8.2.1/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: augraphy
-Version: 8.2.0
+Version: 8.2.1
 Summary: Augmentation pipeline for rendering synthetic paper printing and scanning processes
 Home-page: https://github.com/sparkfish/augraphy
 Author: Sparkfish LLC
 Author-email: packages@sparkfish.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/sparkfish/augraphy/issues
 Description: <p align="center">
@@ -58,22 +58,16 @@
         augmented = data["output"]
         ```
         
         # Documentation
         For full documentation, including installation and tutorials, check the [doc directory](https://github.com/sparkfish/augraphy/tree/dev/doc).
         
         # Benchmark Results
-        The benchmarks results are computed with Augraphy 8.20 and Tobacco3482 dataset (resume subset with a total of 120 images). It is evaluated with a 2 cores machine - Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz.
-        To run the benchmark with different images, you can run with run_benchmarks.py in the folder of /benchmark using the following command:
+        The benchmark results are computed with Augraphy 8.20 and Tobacco3482 dataset (resume subset with a total of 120 images). It is evaluated with a 2 cores machine - Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz.
         
-        ```
-        python run_benchmarks.py --folder_path folder_path_with_images
-        ```
-        
-        # Benchmarking results
         |    Augmentation    |Images per second|Memory usage (MB)|
         |--------------------|----------------:|----------------:|
         |BadPhotoCopy        |             0.31|           138.25|
         |BindingsAndFasteners|            26.11|            20.81|
         |BleedThrough        |             0.27|           684.69|
         |BookBinding         |             0.06|           683.50|
         |Brightness          |             3.31|           147.99|
@@ -110,15 +104,15 @@
         
         BibTeX:
         ```
         @software{augraphy_library,
             author = {The Augraphy Project},
             title = {Augraphy: an augmentation pipeline for rendering synthetic paper printing, faxing, scanning and copy machine processes},
             url = {https://github.com/sparkfish/augraphy},
-            version = {8.2.0}
+            version = {8.2.1}
         }
         ```
         
         # License
         Copyright 2023 Sparkfish LLC
         
         Augraphy is free and open-source software distributed under the terms of the [**MIT**](https://github.com/sparkfish/augraphy/blob/dev/LICENSE) license.
```

### Comparing `augraphy-8.2.0/README.md` & `augraphy-8.2.1/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -49,22 +49,16 @@
 augmented = data["output"]
 ```
 
 # Documentation
 For full documentation, including installation and tutorials, check the [doc directory](https://github.com/sparkfish/augraphy/tree/dev/doc).
 
 # Benchmark Results
-The benchmarks results are computed with Augraphy 8.20 and Tobacco3482 dataset (resume subset with a total of 120 images). It is evaluated with a 2 cores machine - Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz.
-To run the benchmark with different images, you can run with run_benchmarks.py in the folder of /benchmark using the following command:
+The benchmark results are computed with Augraphy 8.20 and Tobacco3482 dataset (resume subset with a total of 120 images). It is evaluated with a 2 cores machine - Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz.
 
-```
-python run_benchmarks.py --folder_path folder_path_with_images
-```
-
-# Benchmarking results
 |    Augmentation    |Images per second|Memory usage (MB)|
 |--------------------|----------------:|----------------:|
 |BadPhotoCopy        |             0.31|           138.25|
 |BindingsAndFasteners|            26.11|            20.81|
 |BleedThrough        |             0.27|           684.69|
 |BookBinding         |             0.06|           683.50|
 |Brightness          |             3.31|           147.99|
@@ -101,15 +95,15 @@
 
 BibTeX:
 ```
 @software{augraphy_library,
     author = {The Augraphy Project},
     title = {Augraphy: an augmentation pipeline for rendering synthetic paper printing, faxing, scanning and copy machine processes},
     url = {https://github.com/sparkfish/augraphy},
-    version = {8.2.0}
+    version = {8.2.1}
 }
 ```
 
 # License
 Copyright 2023 Sparkfish LLC
 
 Augraphy is free and open-source software distributed under the terms of the [**MIT**](https://github.com/sparkfish/augraphy/blob/dev/LICENSE) license.
```

### Comparing `augraphy-8.2.0/augraphy/augmentations/__init__.py` & `augraphy-8.2.1/augraphy/augmentations/__init__.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/badphotocopy.py` & `augraphy-8.2.1/augraphy/augmentations/badphotocopy.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/bindingsandfasteners.py` & `augraphy-8.2.1/augraphy/augmentations/bindingsandfasteners.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/bleedthrough.py` & `augraphy-8.2.1/augraphy/augmentations/bleedthrough.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/bookbinding.py` & `augraphy-8.2.1/augraphy/augmentations/bookbinding.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/brightness.py` & `augraphy-8.2.1/augraphy/augmentations/brightness.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/brightnesstexturize.py` & `augraphy-8.2.1/augraphy/augmentations/brightnesstexturize.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/colorpaper.py` & `augraphy-8.2.1/augraphy/augmentations/colorpaper.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/dirtydrum.py` & `augraphy-8.2.1/augraphy/augmentations/dirtydrum.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/dirtyrollers.py` & `augraphy-8.2.1/augraphy/augmentations/dirtyrollers.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/dithering.py` & `augraphy-8.2.1/augraphy/augmentations/dithering.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/faxify.py` & `augraphy-8.2.1/augraphy/augmentations/faxify.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/folding.py` & `augraphy-8.2.1/augraphy/augmentations/folding.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/gamma.py` & `augraphy-8.2.1/augraphy/augmentations/gamma.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/geometric.py` & `augraphy-8.2.1/augraphy/augmentations/geometric.py`

 * *Files 4% similar despite different names*

```diff
@@ -9,29 +9,40 @@
 
 class Geometric(Augmentation):
     """Applies basic geometric transformations such as resizing, flips and rotation.
 
     :param scale: Pair of floats determining new scale of image.
     :type scale: tuple, optional
     :param translation: Pair of values determining x and y translation value.
-            The translation value will be in percentage of the image size if the value is less than 1.
+            The translation value will be in percentage of the image size if the value is in between 0 - 1:
+            x (int) = image width  * x (float and 0 - 1)
+            y (int) = image height * y (float and 0 - 1)
     :type translation: tuple, optional
     :param fliplr: Flag to flip image in left right direction.
     :type fliplr: int, optional
     :param flipud: Flag to flip image in up down direction.
     :type flipud: int, optional
     :param crop: Tuple of 4 (x0, y0, xn, yn) to crop section of image.
+             The value will be in percentage of the image size if the value is in between 0 - 1:
+             x0 (int) = image width  * x0 (float and 0 - 1)
+             y0 (int) = image height * y0 (float and 0 - 1)
+             xn (int) = image width  * xn (float and 0 - 1)
+             yn (int) = image height * yn (float and 0 - 1)
     :type crop: tuple, optional
     :param rotate_range: Pair of ints determining the range from which to sample
            the image rotation.
     :type rotate_range: tuple, optional
     :param randomize: Flag to apply random geometric transformations.
     :type randomize: int, optional
     :param padding: Padding amount on each (left, right, top, bottom) side.
-            The padding amount will be in percentage of the image size if the value is less than 1.
+            The padding amount will be in percentage of the image size if the value is in between 0 - 1:
+            left   (int) = image width  * left   (float and 0 - 1)
+            right  (int) = image height * right  (float and 0 - 1)
+            top    (int) = image width  * top    (float and 0 - 1)
+            bottom (int) = image height * bottom (float and 0 - 1)
     :type padding: tuple, optional
     :param padding_type: Padding methods, select from fill,duplicate and mirror.
     :type paddng_type: string, optional
     :param padding_value: Padding value (in BGR) for fill padding method.
     :type paddng_value: tuple, optional
     :param p: The probability that this Augmentation will be applied.
     :type p: float, optional
@@ -107,14 +118,21 @@
 
             # crop image
             if self.crop:
                 # make sure there's only 4 inputs, x0, y0, xn, yn
                 if len(self.crop) == 4:
                     ysize, xsize = image.shape[:2]
                     xstart, ystart, xend, yend = self.crop
+
+                    if xstart < 1 and ystart < 1 and (xend <= 1 and xend > 0) and (yend <= 1 and yend > 0):
+                        xstart = int(xstart * xsize)
+                        ystart = int(ystart * ysize)
+                        xend = int(xend * xsize)
+                        yend = int(yend * ysize)
+
                     # when value is set to -1, it takes image size
                     if yend == -1:
                         yend = ysize
                     if xend == -1:
                         xend = xsize
                     # condition to make sure cropping range is valid
                     check_y = yend > ystart and ystart >= 0
```

### Comparing `augraphy-8.2.0/augraphy/augmentations/inkbleed.py` & `augraphy-8.2.1/augraphy/augmentations/inkbleed.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/jpeg.py` & `augraphy-8.2.1/augraphy/augmentations/jpeg.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/letterpress.py` & `augraphy-8.2.1/augraphy/augmentations/letterpress.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/lib.py` & `augraphy-8.2.1/augraphy/augmentations/lib.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/lightinggradient.py` & `augraphy-8.2.1/augraphy/augmentations/lightinggradient.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/lowinkline.py` & `augraphy-8.2.1/augraphy/augmentations/lowinkline.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/lowinkperiodiclines.py` & `augraphy-8.2.1/augraphy/augmentations/lowinkperiodiclines.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/lowinkrandomlines.py` & `augraphy-8.2.1/augraphy/augmentations/lowinkrandomlines.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/markup.py` & `augraphy-8.2.1/augraphy/augmentations/markup.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/noisetexturize.py` & `augraphy-8.2.1/augraphy/augmentations/noisetexturize.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/pageborder.py` & `augraphy-8.2.1/augraphy/augmentations/pageborder.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/pencilscribbles.py` & `augraphy-8.2.1/augraphy/augmentations/pencilscribbles.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/subtlenoise.py` & `augraphy-8.2.1/augraphy/augmentations/subtlenoise.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/augmentations/watermark.py` & `augraphy-8.2.1/augraphy/augmentations/watermark.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/base/augmentation.py` & `augraphy-8.2.1/augraphy/base/augmentation.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/base/augmentationpipeline.py` & `augraphy-8.2.1/augraphy/base/augmentationpipeline.py`

 * *Files 10% similar despite different names*

```diff
@@ -88,15 +88,71 @@
     def wrapListMaybe(self, augs):
         """Converts a bare list to an AugmentationSequence, or does nothing."""
         if type(augs) is list:
             return AugmentationSequence(augs)
         else:
             return augs
 
-    def augment(self, image):
+    def augment(self, image, return_dict=1):
+        """Applies the Augmentations in each phase of the pipeline.
+
+        :param image: The image to apply Augmentations to. Minimum 30x30 pixels.
+        :type image: numpy.array or list
+        :return: 1. A dictionary of AugmentationResults representing the changes in each phase of the pipeline if the input is image.
+                 2. A list contains output images if the input is list of images.
+                 3. A four dimensional numpy array if the input is a four dimensional numpy array (batch size, channels, height, width).
+        :rtype: 1. dictionary
+                2. list
+                3. numpy array (B, C, H, W)
+        :param return_dict: Flag to return output in dictionary format.
+                Not applicable when input is 4 dimensional array.
+                When input is 4 dimensional numpy array, output will be a 4 dimensional array too.
+        :type return_dict: int
+        """
+
+        # image is a list of images
+        if isinstance(image, list):
+            output = []
+            for single_image in image:
+                data = self.augment_single_image(single_image)
+                if return_dict:
+                    output.append(data)
+                else:
+                    output.append(data["output"])
+
+        # image is a 4 dimensional numpy array
+        elif len(image.shape) == 4:
+            batch_size, channels, height, width = image.shape
+            output = np.zeros((batch_size, channels, height, width), dtype=image.dtype)
+            for i in range(batch_size):
+                single_image = image[i].reshape(height, width, channels)
+                output_image = self.augment_single_image(single_image)["output"]
+
+                # output is color image but input is in grayscale, convert output to grayscale
+                if len(output_image.shape) > channels:
+                    output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2GRAY)
+                # output is in grayscale but input is color image, convert output to color image
+                if len(output_image.shape) != channels:
+                    output_image = cv2.cvtColor(output_image, cv2.COLOR_GRAY2BGR)
+                # rescale image size if the image size is changes after the augmentation
+                if output_image.shape[0] != height or output_image.shape[1] != width:
+                    output_image = cv2.resize(output_image, (width, height), interpolation=cv2.INTER_AREA)
+                output[i] = output_image.reshape(channels, height, width)
+
+        # single image
+        else:
+            data = self.augment_single_image(image)
+            if return_dict:
+                output = data
+            else:
+                output = data["output"]
+
+        return output
+
+    def augment_single_image(self, image):
         """Applies the Augmentations in each phase of the pipeline.
 
         :param image: The image to apply Augmentations to. Minimum 30x30 pixels.
         :type image: numpy.array
         :return: A dictionary of AugmentationResults representing the changes
                  in each phase of the pipeline.
         :rtype: dictionary
@@ -105,16 +161,17 @@
         # Check if image has correct channel
         if len(image.shape) > 2 and (image.shape[2] != 3):
             raise Exception(
                 "Image should have channel number of 3 (BGR), but actual dimensions were {}.".format(
                     image.shape,
                 ),
             )
+
         # Check that image is the correct size.
-        elif (image.shape[0] < 30) or (image.shape[1] < 30):
+        if (image.shape[0] < 30) or (image.shape[1] < 30):
             raise Exception(
                 "Image should have dimensions greater than 30x30, but actual dimensions were {}.".format(
                     image.shape,
                 ),
             )
 
         # get and check valid image type ( uint or float)
@@ -569,8 +626,8 @@
         r += f"AugraphyPipeline(ink_phase, paper_phase, post_phase, overlay_type={self.overlay_type}, overlay_alpha={self.overlay_alpha}, ink_color_range={self.ink_color_range}, paper_color_range={self.paper_color_range}, save_outputs={self.save_outputs}, log={self.log}, random_seed={self.random_seed})"
         return r
 
     def visualize(self):
         print(repr(self))
 
     def __call__(self, image):
-        return self.augment(image)["output"]
+        return self.augment(image, return_dict=0)
```

### Comparing `augraphy-8.2.0/augraphy/base/augmentationresult.py` & `augraphy-8.2.1/augraphy/base/augmentationresult.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/base/augmentationsequence.py` & `augraphy-8.2.1/augraphy/base/augmentationsequence.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/base/oneof.py` & `augraphy-8.2.1/augraphy/base/oneof.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/base/paperfactory.py` & `augraphy-8.2.1/augraphy/base/paperfactory.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/default/pipeline.py` & `augraphy-8.2.1/augraphy/default/pipeline.py`

 * *Files 8% similar despite different names*

```diff
@@ -267,14 +267,112 @@
 def default_augment(img):
 
     default_pipeline = default_augraphy_pipeline()
 
     return default_pipeline.augment(img)
 
 
+def pipeline_archetype1():
+
+    ink_phase = [
+        Geometric(
+            padding=(0, 0, 0.05, 0),
+            randomize=0,
+        ),
+        BindingsAndFasteners(
+            overlay_types="darken",
+            effect_type="punch_holes",
+            ntimes=(3, 3),
+            nscales=(1.0, 1.0),
+            edge="top",
+            edge_offset=(0.01, 0.01),
+        ),
+        InkBleed(
+            intensity_range=(0.1, 0.2),
+            color_range=(0, 5),
+            kernel_size=(3, 3),
+            severity=(0.2, 0.2),
+        ),
+    ]
+
+    paper_phase = [
+        PageBorder(
+            side="right",
+            border_background_value=(0, 0),
+            pages=1,
+            width_range=(2, 3),
+            same_page_border=0,
+        ),
+        Geometric(
+            translation=(-0.1, 0.2),
+            randomize=0,
+        ),
+        Geometric(
+            translation=(0, -0.05),
+            randomize=0,
+        ),
+    ]
+
+    post_phase = [
+        Geometric(
+            rotate_range=(-1, -1),
+            randomize=0,
+        ),
+        Faxify(
+            monochrome=1,
+            monochrome_method="threshold_otsu",
+            halftone=0,
+        ),
+        Brightness(
+            brightness_range=(2.0, 2.0),
+            min_brightness=1,
+            min_brightness_value=(50, 50),
+        ),
+        Gamma(
+            gamma_range=(1.5, 1.5),
+        ),
+        Letterpress(
+            n_samples=(1000, 1000),
+            n_clusters=(500, 500),
+            std_range=(400, 400),
+            value_range=(200, 255),
+            value_threshold_range=(255, 255),
+            blur=0,
+        ),
+        BadPhotoCopy(
+            noise_type=1,
+            noise_side="bottom",
+            noise_iteration=(1, 1),
+            noise_size=(5, 7),
+            noise_value=(0, 64),
+            noise_sparsity=(0.01, 0.01),
+            noise_concentration=(0.01, 0.01),
+            blur_noise=1,
+            wave_pattern=0,
+            edge_effect=0,
+        ),
+        BadPhotoCopy(
+            noise_type=4,
+            noise_side="random",
+            noise_iteration=(4, 5),
+            noise_size=(1, 4),
+            noise_value=(0, 64),
+            noise_sparsity=(0.5, 0.6),
+            noise_concentration=(0.5, 0.5),
+            blur_noise=1,
+            wave_pattern=0,
+            edge_effect=0,
+        ),
+    ]
+
+    pipeline = AugraphyPipeline(ink_phase, paper_phase, post_phase)
+
+    return pipeline
+
+
 def pipeline_archetype2():
 
     ink_phase = [
         Markup(
             num_lines_range=(3, 4),
             markup_length_range=(0.5, 1),
             markup_thickness_range=(3, 5),
@@ -500,14 +598,102 @@
     ]
 
     pipeline = AugraphyPipeline(ink_phase, paper_phase, post_phase)
 
     return pipeline
 
 
+def pipeline_archetype4():
+
+    ink_phase = [
+        Geometric(
+            crop=(0.12, 0.08, 0.85, 0.9),
+            randomize=0,
+        ),
+        BindingsAndFasteners(
+            overlay_types="darken",
+            effect_type="punch_holes",
+            ntimes=(3, 3),
+            nscales=(1.0, 1.0),
+            edge="left",
+            edge_offset=(10, 10),
+        ),
+        InkBleed(
+            intensity_range=(0.5, 0.5),
+            color_range=(0, 0),
+            kernel_size=(3, 3),
+            severity=(0.5, 0.5),
+        ),
+    ]
+
+    paper_phase = [
+        PageBorder(
+            side="top",
+            border_background_value=(0, 0),
+            pages=1,
+            width_range=(0.03, 0.03),
+            same_page_border=0,
+        ),
+        PageBorder(
+            side="bottom",
+            border_background_value=(0, 0),
+            pages=1,
+            width_range=(0.05, 0.05),
+            same_page_border=0,
+        ),
+    ]
+
+    post_phase = [
+        Faxify(
+            monochrome=1,
+            monochrome_method="threshold_otsu",
+            halftone=0,
+        ),
+        Geometric(
+            rotate_range=(-1, -1),
+            padding=(0, 0.05, 0, 0),
+            randomize=0,
+        ),
+        Geometric(
+            crop=(0, 0.02, 1, 0.99),
+            randomize=0,
+        ),
+        BadPhotoCopy(
+            noise_type=4,
+            noise_side="random",
+            noise_iteration=(2, 3),
+            noise_size=(5, 7),
+            noise_value=(0, 64),
+            noise_sparsity=(0.2, 0.3),
+            noise_concentration=(0.05, 0.05),
+            blur_noise=0,
+            blur_noise_kernel=(5, 5),
+            wave_pattern=0,
+            edge_effect=0,
+        ),
+        BadPhotoCopy(
+            noise_type=1,
+            noise_side="top_left",
+            noise_iteration=(1, 1),
+            noise_size=(9, 11),
+            noise_value=(0, 64),
+            noise_sparsity=(0.01, 0.01),
+            noise_concentration=(0.02, 0.02),
+            blur_noise=0,
+            blur_noise_kernel=(5, 5),
+            wave_pattern=0,
+            edge_effect=0,
+        ),
+    ]
+
+    pipeline = AugraphyPipeline(ink_phase, paper_phase, post_phase)
+
+    return pipeline
+
+
 def pipeline_archetype5():
 
     ink_phase = [
         Faxify(
             monochrome=1,
             monochrome_method="threshold_otsu",
             halftone=0,
```

### Comparing `augraphy-8.2.0/augraphy/utilities/composepipelines.py` & `augraphy-8.2.1/augraphy/utilities/composepipelines.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/utilities/figsharedownloader.py` & `augraphy-8.2.1/augraphy/utilities/figsharedownloader.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/utilities/function.py` & `augraphy-8.2.1/augraphy/utilities/function.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/utilities/imageoverlay.py` & `augraphy-8.2.1/augraphy/utilities/imageoverlay.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/utilities/interop.py` & `augraphy-8.2.1/augraphy/utilities/interop.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy/utilities/noisegenerator.py` & `augraphy-8.2.1/augraphy/utilities/noisegenerator.py`

 * *Files 1% similar despite different names*

```diff
@@ -459,18 +459,22 @@
 
         # initialize blank noise mask
         img_mask = np.full((xsize, ysize), fill_value=background_value).astype("int")
 
         # any invalid noise type will reset noise type to 0
         if self.noise_type not in [1, 2, 3, 4]:
             noise_type = random.randint(1, 4)
+        else:
+            noise_type = self.noise_type
 
         # random location with no sides if no side is chosen
         if self.noise_side not in self.sides:
             noise_side = random.choice(self.sides)
+        else:
+            noise_side = self.noise_side
 
         # loop each iterations
         for _ in range(iterations):
 
             # divider to rescale noise mask to larger size
             y_divider = random.randint(noise_size[0], noise_size[1])
             x_divider = random.randint(noise_size[0], noise_size[1])
```

### Comparing `augraphy-8.2.0/augraphy/utilities/overlaybuilder.py` & `augraphy-8.2.1/augraphy/utilities/overlaybuilder.py`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/augraphy.egg-info/PKG-INFO` & `augraphy-8.2.1/augraphy.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: augraphy
-Version: 8.2.0
+Version: 8.2.1
 Summary: Augmentation pipeline for rendering synthetic paper printing and scanning processes
 Home-page: https://github.com/sparkfish/augraphy
 Author: Sparkfish LLC
 Author-email: packages@sparkfish.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/sparkfish/augraphy/issues
 Description: <p align="center">
@@ -58,22 +58,16 @@
         augmented = data["output"]
         ```
         
         # Documentation
         For full documentation, including installation and tutorials, check the [doc directory](https://github.com/sparkfish/augraphy/tree/dev/doc).
         
         # Benchmark Results
-        The benchmarks results are computed with Augraphy 8.20 and Tobacco3482 dataset (resume subset with a total of 120 images). It is evaluated with a 2 cores machine - Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz.
-        To run the benchmark with different images, you can run with run_benchmarks.py in the folder of /benchmark using the following command:
+        The benchmark results are computed with Augraphy 8.20 and Tobacco3482 dataset (resume subset with a total of 120 images). It is evaluated with a 2 cores machine - Intel(R) Xeon(R) Gold 6226R CPU @ 2.90GHz.
         
-        ```
-        python run_benchmarks.py --folder_path folder_path_with_images
-        ```
-        
-        # Benchmarking results
         |    Augmentation    |Images per second|Memory usage (MB)|
         |--------------------|----------------:|----------------:|
         |BadPhotoCopy        |             0.31|           138.25|
         |BindingsAndFasteners|            26.11|            20.81|
         |BleedThrough        |             0.27|           684.69|
         |BookBinding         |             0.06|           683.50|
         |Brightness          |             3.31|           147.99|
@@ -110,15 +104,15 @@
         
         BibTeX:
         ```
         @software{augraphy_library,
             author = {The Augraphy Project},
             title = {Augraphy: an augmentation pipeline for rendering synthetic paper printing, faxing, scanning and copy machine processes},
             url = {https://github.com/sparkfish/augraphy},
-            version = {8.2.0}
+            version = {8.2.1}
         }
         ```
         
         # License
         Copyright 2023 Sparkfish LLC
         
         Augraphy is free and open-source software distributed under the terms of the [**MIT**](https://github.com/sparkfish/augraphy/blob/dev/LICENSE) license.
```

### Comparing `augraphy-8.2.0/augraphy.egg-info/SOURCES.txt` & `augraphy-8.2.1/augraphy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `augraphy-8.2.0/setup.py` & `augraphy-8.2.1/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -24,13 +24,14 @@
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     packages=setuptools.find_packages(),
     python_requires=">=3.7",
     install_requires=[
+        "numba",
         "numpy >= 1.20.1",
         "opencv-python >= 4.5.1.48",
         "scikit-learn >= 0.0",
         "scipy >= 1.6.3",
     ],
 )
```

