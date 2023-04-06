# Comparing `tmp/flare-capa-5.0.0.tar.gz` & `tmp/flare-capa-5.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/flare-capa-5.0.0.tar", last modified: Wed Feb  8 20:37:44 2023, max compression
+gzip compressed data, was "dist/flare-capa-5.1.0.tar", last modified: Thu Apr  6 11:11:59 2023, max compression
```

## Comparing `flare-capa-5.0.0.tar` & `flare-capa-5.1.0.tar`

### file list

```diff
@@ -1,99 +1,112 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/
--rw-r--r--   0 runner    (1001) docker     (122)    13814 2023-02-08 20:37:44.000000 flare-capa-5.0.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)    11256 2023-02-08 20:37:36.000000 flare-capa-5.0.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    12751 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/engine.py
--rw-r--r--   0 runner    (1001) docker     (122)      207 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/features/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     2466 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/address.py
--rw-r--r--   0 runner    (1001) docker     (122)      841 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/basicblock.py
--rw-r--r--   0 runner    (1001) docker     (122)    15625 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/common.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/features/extractors/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     9622 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/base_extractor.py
--rw-r--r--   0 runner    (1001) docker     (122)     3756 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/common.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     6782 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/extractor.py
--rw-r--r--   0 runner    (1001) docker     (122)     2600 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/file.py
--rw-r--r--   0 runner    (1001) docker     (122)     2029 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/function.py
--rw-r--r--   0 runner    (1001) docker     (122)    13798 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/helpers.py
--rw-r--r--   0 runner    (1001) docker     (122)     8595 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/insn.py
--rw-r--r--   0 runner    (1001) docker     (122)     2595 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile/types.py
--rw-r--r--   0 runner    (1001) docker     (122)     4907 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dnfile_.py
--rw-r--r--   0 runner    (1001) docker     (122)     8241 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/dotnetfile.py
--rw-r--r--   0 runner    (1001) docker     (122)    23805 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/elf.py
--rw-r--r--   0 runner    (1001) docker     (122)     5959 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/elffile.py
--rw-r--r--   0 runner    (1001) docker     (122)     3766 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/features/extractors/ida/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     4235 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/basicblock.py
--rw-r--r--   0 runner    (1001) docker     (122)     3480 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/extractor.py
--rw-r--r--   0 runner    (1001) docker     (122)     7544 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/file.py
--rw-r--r--   0 runner    (1001) docker     (122)     2346 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/function.py
--rw-r--r--   0 runner    (1001) docker     (122)     2043 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/global_.py
--rw-r--r--   0 runner    (1001) docker     (122)    12198 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/helpers.py
--rw-r--r--   0 runner    (1001) docker     (122)    18257 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/ida/insn.py
--rw-r--r--   0 runner    (1001) docker     (122)     1105 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/loops.py
--rw-r--r--   0 runner    (1001) docker     (122)     2337 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/null.py
--rw-r--r--   0 runner    (1001) docker     (122)     7350 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/pefile.py
--rw-r--r--   0 runner    (1001) docker     (122)     2965 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/strings.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/features/extractors/viv/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     5205 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/basicblock.py
--rw-r--r--   0 runner    (1001) docker     (122)     3719 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/extractor.py
--rw-r--r--   0 runner    (1001) docker     (122)     4507 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/file.py
--rw-r--r--   0 runner    (1001) docker     (122)     2808 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/function.py
--rw-r--r--   0 runner    (1001) docker     (122)      815 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/global_.py
--rw-r--r--   0 runner    (1001) docker     (122)      998 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/helpers.py
--rw-r--r--   0 runner    (1001) docker     (122)     5520 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/indirect_calls.py
--rw-r--r--   0 runner    (1001) docker     (122)    25625 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/extractors/viv/insn.py
--rw-r--r--   0 runner    (1001) docker     (122)     1513 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/file.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/features/freeze/
--rw-r--r--   0 runner    (1001) docker     (122)    12446 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/freeze/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    10625 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/freeze/features.py
--rw-r--r--   0 runner    (1001) docker     (122)     4537 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/features/insn.py
--rw-r--r--   0 runner    (1001) docker     (122)     4183 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/ida/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     7892 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/ida/plugin/
--rw-r--r--   0 runner    (1001) docker     (122)     4337 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     9895 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/cache.py
--rw-r--r--   0 runner    (1001) docker     (122)      851 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/capa_explorer.py
--rw-r--r--   0 runner    (1001) docker     (122)      674 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/error.py
--rw-r--r--   0 runner    (1001) docker     (122)     1786 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/extractor.py
--rw-r--r--   0 runner    (1001) docker     (122)    56752 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/form.py
--rw-r--r--   0 runner    (1001) docker     (122)     2168 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/hooks.py
--rw-r--r--   0 runner    (1001) docker     (122)     9048 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/icon.py
--rw-r--r--   0 runner    (1001) docker     (122)    11670 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/item.py
--rw-r--r--   0 runner    (1001) docker     (122)    27440 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/model.py
--rw-r--r--   0 runner    (1001) docker     (122)     7757 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/proxy.py
--rw-r--r--   0 runner    (1001) docker     (122)    49204 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/ida/plugin/view.py
--rw-r--r--   0 runner    (1001) docker     (122)    45048 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/main.py
--rw-r--r--   0 runner    (1001) docker     (122)     2314 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/optimizer.py
--rw-r--r--   0 runner    (1001) docker     (122)      235 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/perf.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/render/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     8878 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/default.py
--rw-r--r--   0 runner    (1001) docker     (122)      844 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/json.py
--rw-r--r--   0 runner    (1001) docker     (122)    18364 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/result_document.py
--rw-r--r--   0 runner    (1001) docker     (122)     2080 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/utils.py
--rw-r--r--   0 runner    (1001) docker     (122)     5575 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/verbose.py
--rw-r--r--   0 runner    (1001) docker     (122)    14768 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/render/vverbose.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/capa/rules/
--rw-r--r--   0 runner    (1001) docker     (122)    54991 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/rules/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     4657 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/rules/cache.py
--rw-r--r--   0 runner    (1001) docker     (122)       95 2023-02-08 20:37:36.000000 flare-capa-5.0.0/capa/version.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)    13814 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     2586 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       41 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (122)      651 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        5 2023-02-08 20:37:44.000000 flare-capa-5.0.0/flare_capa.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)      368 2023-02-08 20:37:44.000000 flare-capa-5.0.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     3664 2023-02-08 20:37:36.000000 flare-capa-5.0.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/
+-rw-r--r--   0 runner    (1001) docker     (122)    13814 2023-04-06 11:11:59.000000 flare-capa-5.1.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    11256 2023-04-06 11:11:47.000000 flare-capa-5.1.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12727 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/engine.py
+-rw-r--r--   0 runner    (1001) docker     (122)      207 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2466 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/address.py
+-rw-r--r--   0 runner    (1001) docker     (122)      841 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/basicblock.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16176 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/common.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/extractors/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9622 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/base_extractor.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/extractors/binja/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4654 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/basicblock.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3734 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/extractor.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6730 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/file.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1827 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/find_binja_api.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3270 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/function.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1803 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/global_.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2100 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (122)    23024 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/binja/insn.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4146 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/common.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6782 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/extractor.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2600 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/file.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2029 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/function.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13798 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8595 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/insn.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2595 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile/types.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4907 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dnfile_.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8241 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/dotnetfile.py
+-rw-r--r--   0 runner    (1001) docker     (122)    27125 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/elf.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5959 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/elffile.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3754 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/extractors/ida/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4235 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/basicblock.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3480 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/extractor.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7593 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/file.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2346 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/function.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2043 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/global_.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12344 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (122)    18253 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/ida/insn.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1105 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/loops.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2337 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/null.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7348 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/pefile.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2965 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/strings.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/extractors/viv/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5201 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/basicblock.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3727 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/extractor.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4505 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/file.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3090 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/function.py
+-rw-r--r--   0 runner    (1001) docker     (122)      815 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/global_.py
+-rw-r--r--   0 runner    (1001) docker     (122)      998 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5520 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/indirect_calls.py
+-rw-r--r--   0 runner    (1001) docker     (122)    25804 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/extractors/viv/insn.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1513 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/file.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/features/freeze/
+-rw-r--r--   0 runner    (1001) docker     (122)    13467 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/freeze/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11948 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/freeze/features.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5801 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/features/insn.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4173 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/ida/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7890 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/ida/plugin/
+-rw-r--r--   0 runner    (1001) docker     (122)     4908 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9895 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/cache.py
+-rw-r--r--   0 runner    (1001) docker     (122)      851 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/capa_explorer.py
+-rw-r--r--   0 runner    (1001) docker     (122)      674 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/error.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1785 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/extractor.py
+-rw-r--r--   0 runner    (1001) docker     (122)    56870 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/form.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2168 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8943 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/icon.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11671 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/item.py
+-rw-r--r--   0 runner    (1001) docker     (122)    27390 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/model.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7757 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/proxy.py
+-rw-r--r--   0 runner    (1001) docker     (122)    48905 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/ida/plugin/view.py
+-rw-r--r--   0 runner    (1001) docker     (122)    48490 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/main.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2314 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/optimizer.py
+-rw-r--r--   0 runner    (1001) docker     (122)      235 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/perf.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/render/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8844 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/default.py
+-rw-r--r--   0 runner    (1001) docker     (122)      844 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/json.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/render/proto/
+-rw-r--r--   0 runner    (1001) docker     (122)    27921 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/proto/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    17713 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/proto/capa_pb2.py
+-rw-r--r--   0 runner    (1001) docker     (122)    24494 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/result_document.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2074 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/utils.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5878 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/verbose.py
+-rw-r--r--   0 runner    (1001) docker     (122)    14696 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/render/vverbose.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/capa/rules/
+-rw-r--r--   0 runner    (1001) docker     (122)    54883 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/rules/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4657 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/rules/cache.py
+-rw-r--r--   0 runner    (1001) docker     (122)       95 2023-04-06 11:11:47.000000 flare-capa-5.1.0/capa/version.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 11:11:59.000000 flare-capa-5.1.0/flare_capa.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)    13814 2023-04-06 11:11:58.000000 flare-capa-5.1.0/flare_capa.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     3032 2023-04-06 11:11:59.000000 flare-capa-5.1.0/flare_capa.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 11:11:58.000000 flare-capa-5.1.0/flare_capa.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       41 2023-04-06 11:11:58.000000 flare-capa-5.1.0/flare_capa.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 11:11:58.000000 flare-capa-5.1.0/flare_capa.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (122)      714 2023-04-06 11:11:58.000000 flare-capa-5.1.0/flare_capa.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        5 2023-04-06 11:11:58.000000 flare-capa-5.1.0/flare_capa.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      368 2023-04-06 11:11:59.000000 flare-capa-5.1.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     3764 2023-04-06 11:11:47.000000 flare-capa-5.1.0/setup.py
```

### Comparing `flare-capa-5.0.0/PKG-INFO` & `flare-capa-5.1.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: flare-capa
-Version: 5.0.0
+Version: 5.1.0
 Summary: The FLARE team's open-source tool to identify capabilities in executable files.
 Home-page: https://www.github.com/mandiant/capa
 Author: Willi Ballenthin, Moritz Raabe
 Author-email: william.ballenthin@mandiant.com, moritz.raabe@mandiant.com
 License: UNKNOWN
 Project-URL: Documentation, https://github.com/mandiant/capa/tree/master/doc
 Project-URL: Rules, https://github.com/mandiant/capa-rules
 Project-URL: Rules Documentation, https://github.com/mandiant/capa-rules/tree/master/doc
 Description: ![capa](https://github.com/mandiant/capa/blob/master/.github/logo.png)
         
         [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flare-capa)](https://pypi.org/project/flare-capa)
         [![Last release](https://img.shields.io/github/v/release/mandiant/capa)](https://github.com/mandiant/capa/releases)
-        [![Number of rules](https://img.shields.io/badge/rules-770-blue.svg)](https://github.com/mandiant/capa-rules)
+        [![Number of rules](https://img.shields.io/badge/rules-794-blue.svg)](https://github.com/mandiant/capa-rules)
         [![CI status](https://github.com/mandiant/capa/workflows/CI/badge.svg)](https://github.com/mandiant/capa/actions?query=workflow%3ACI+event%3Apush+branch%3Amaster)
         [![Downloads](https://img.shields.io/github/downloads/mandiant/capa/total)](https://github.com/mandiant/capa/releases)
         [![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE.txt)
         
         capa detects capabilities in executable files.
         You run it against a PE, ELF, .NET module, or shellcode file and it tells you what it thinks the program can do.
         For example, it might suggest that the file is a backdoor, is capable of installing services, or relies on HTTP to communicate.
```

### Comparing `flare-capa-5.0.0/README.md` & `flare-capa-5.1.0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 ![capa](https://github.com/mandiant/capa/blob/master/.github/logo.png)
 
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flare-capa)](https://pypi.org/project/flare-capa)
 [![Last release](https://img.shields.io/github/v/release/mandiant/capa)](https://github.com/mandiant/capa/releases)
-[![Number of rules](https://img.shields.io/badge/rules-770-blue.svg)](https://github.com/mandiant/capa-rules)
+[![Number of rules](https://img.shields.io/badge/rules-794-blue.svg)](https://github.com/mandiant/capa-rules)
 [![CI status](https://github.com/mandiant/capa/workflows/CI/badge.svg)](https://github.com/mandiant/capa/actions?query=workflow%3ACI+event%3Apush+branch%3Amaster)
 [![Downloads](https://img.shields.io/github/downloads/mandiant/capa/total)](https://github.com/mandiant/capa/releases)
 [![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE.txt)
 
 capa detects capabilities in executable files.
 You run it against a PE, ELF, .NET module, or shellcode file and it tells you what it thinks the program can do.
 For example, it might suggest that the file is a backdoor, is capable of installing services, or relies on HTTP to communicate.
```

### Comparing `flare-capa-5.0.0/capa/engine.py` & `flare-capa-5.1.0/capa/engine.py`

 * *Files 2% similar despite different names*

```diff
@@ -39,18 +39,20 @@
 
     def __init__(self, description=None):
         super().__init__()
         self.name = self.__class__.__name__
         self.description = description
 
     def __str__(self):
+        name = self.name.lower()
+        children = ",".join(map(str, self.get_children()))
         if self.description:
-            return "%s(%s = %s)" % (self.name.lower(), ",".join(map(str, self.get_children())), self.description)
+            return f"{name}({children} = {self.description})"
         else:
-            return "%s(%s)" % (self.name.lower(), ",".join(map(str, self.get_children())))
+            return f"{name}({children})"
 
     def __repr__(self):
         return str(self)
 
     def evaluate(self, features: FeatureSet, short_circuit=True) -> Result:
         """
         classes that inherit `Statement` must implement `evaluate`
@@ -228,17 +230,17 @@
         if self.min == 0 and count == 0:
             return Result(True, self, [])
 
         return Result(self.min <= count <= self.max, self, [], locations=ctx.get(self.child))
 
     def __str__(self):
         if self.max == (1 << 64 - 1):
-            return "range(%s, min=%d, max=infinity)" % (str(self.child), self.min)
+            return f"range({str(self.child)}, min={self.min}, max=infinity)"
         else:
-            return "range(%s, min=%d, max=%d)" % (str(self.child), self.min, self.max)
+            return f"range({str(self.child)}, min={self.min}, max={self.max})"
 
 
 class Subscope(Statement):
     """
     a subscope element is a placeholder in a rule - it should not be evaluated directly.
     the engine should preprocess rules to extract subscope statements into their own rules.
     """
```

### Comparing `flare-capa-5.0.0/capa/features/address.py` & `flare-capa-5.1.0/capa/features/address.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/basicblock.py` & `flare-capa-5.1.0/capa/features/basicblock.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/common.py` & `flare-capa-5.1.0/capa/features/common.py`

 * *Files 4% similar despite different names*

```diff
@@ -145,19 +145,19 @@
         subclasses should override to customize the rendering.
         """
         return str(self.value)
 
     def __str__(self):
         if self.value is not None:
             if self.description:
-                return "%s(%s = %s)" % (self.get_name_str(), self.get_value_str(), self.description)
+                return f"{self.get_name_str()}({self.get_value_str()} = {self.description})"
             else:
-                return "%s(%s)" % (self.get_name_str(), self.get_value_str())
+                return f"{self.get_name_str()}({self.get_value_str()})"
         else:
-            return "%s" % self.get_name_str()
+            return f"{self.get_name_str()}"
 
     def __repr__(self):
         return str(self)
 
     def evaluate(self, ctx: Dict["Feature", Set[Address]], **kwargs) -> Result:
         capa.perf.counters["evaluate.feature"] += 1
         capa.perf.counters["evaluate.feature." + self.name] += 1
@@ -238,15 +238,15 @@
 
     def get_value_str(self) -> str:
         assert isinstance(self.value, str)
         return escape_string(self.value)
 
     def __str__(self):
         assert isinstance(self.value, str)
-        return "substring(%s)" % escape_string(self.value)
+        return f"substring({escape_string(self.value)})"
 
 
 class _MatchedSubstring(Substring):
     """
     this represents specific match instances of a substring feature.
     treat it the same as a `Substring` except it has the `matches` field that contains the complete strings that matched.
 
@@ -263,19 +263,17 @@
         # we want this to collide with the name of `Substring` above,
         # so that it works nicely with the renderers.
         self.name = "substring"
         # this may be None if the substring doesn't match
         self.matches = matches
 
     def __str__(self):
+        matches = ", ".join(map(lambda s: '"' + s + '"', (self.matches or {}).keys()))
         assert isinstance(self.value, str)
-        return 'substring("%s", matches = %s)' % (
-            self.value,
-            ", ".join(map(lambda s: '"' + s + '"', (self.matches or {}).keys())),
-        )
+        return f'substring("{self.value}", matches = {matches})'
 
 
 class Regex(String):
     def __init__(self, value: str, description=None):
         super().__init__(value, description=description)
         self.value = value
 
@@ -286,15 +284,15 @@
             flags |= re.IGNORECASE
         try:
             self.re = re.compile(pat, flags)
         except re.error as exc:
             if value.endswith("/i"):
                 value = value[: -len("i")]
             raise ValueError(
-                "invalid regular expression: %s it should use Python syntax, try it at https://pythex.org" % value
+                f"invalid regular expression: {value} it should use Python syntax, try it at https://pythex.org"
             ) from exc
 
     def evaluate(self, ctx, short_circuit=True):
         capa.perf.counters["evaluate.feature"] += 1
         capa.perf.counters["evaluate.feature.regex"] += 1
 
         # mapping from string value to list of locations.
@@ -332,15 +330,15 @@
             # see #262.
             return Result(True, _MatchedRegex(self, dict(matches)), [], locations=locations)
         else:
             return Result(False, _MatchedRegex(self, {}), [])
 
     def __str__(self):
         assert isinstance(self.value, str)
-        return "regex(string =~ %s)" % self.value
+        return f"regex(string =~ {self.value})"
 
 
 class _MatchedRegex(Regex):
     """
     this represents specific match instances of a regular expression feature.
     treat it the same as a `Regex` except it has the `matches` field that contains the complete strings that matched.
 
@@ -357,19 +355,17 @@
         # we want this to collide with the name of `Regex` above,
         # so that it works nicely with the renderers.
         self.name = "regex"
         # this may be None if the regex doesn't match
         self.matches = matches
 
     def __str__(self):
+        matches = ", ".join(map(lambda s: '"' + s + '"', (self.matches or {}).keys()))
         assert isinstance(self.value, str)
-        return "regex(string =~ %s, matches = %s)" % (
-            self.value,
-            ", ".join(map(lambda s: '"' + s + '"', (self.matches or {}).keys())),
-        )
+        return f"regex(string =~ {self.value}, matches = {matches})"
 
 
 class StringFactory:
     def __new__(cls, value: str, description=None):
         if value.startswith("/") and (value.endswith("/") or value.endswith("/i")):
             return Regex(value, description=description)
         return String(value, description=description)
@@ -417,31 +413,48 @@
 OS_WINDOWS = "windows"
 OS_LINUX = "linux"
 OS_MACOS = "macos"
 # dotnet
 OS_ANY = "any"
 VALID_OS = {os.value for os in capa.features.extractors.elf.OS}
 VALID_OS.update({OS_WINDOWS, OS_LINUX, OS_MACOS, OS_ANY})
+# internal only, not to be used in rules
+OS_AUTO = "auto"
 
 
 class OS(Feature):
     def __init__(self, value: str, description=None):
         super().__init__(value, description=description)
         self.name = "os"
 
+    def evaluate(self, ctx, **kwargs):
+        capa.perf.counters["evaluate.feature"] += 1
+        capa.perf.counters["evaluate.feature." + self.name] += 1
+
+        for feature, locations in ctx.items():
+            if not isinstance(feature, (OS,)):
+                continue
+
+            assert isinstance(feature.value, str)
+            if OS_ANY in (self.value, feature.value) or self.value == feature.value:
+                return Result(True, self, [], locations=locations)
+
+        return Result(False, self, [])
+
 
 FORMAT_PE = "pe"
 FORMAT_ELF = "elf"
 FORMAT_DOTNET = "dotnet"
 VALID_FORMAT = (FORMAT_PE, FORMAT_ELF, FORMAT_DOTNET)
 # internal only, not to be used in rules
 FORMAT_AUTO = "auto"
 FORMAT_SC32 = "sc32"
 FORMAT_SC64 = "sc64"
 FORMAT_FREEZE = "freeze"
+FORMAT_RESULT = "result"
 FORMAT_UNKNOWN = "unknown"
 
 
 class Format(Feature):
     def __init__(self, value: str, description=None):
         super().__init__(value, description=description)
         self.name = "format"
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/base_extractor.py` & `flare-capa-5.1.0/capa/features/extractors/base_extractor.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/common.py` & `flare-capa-5.1.0/capa/features/extractors/common.py`

 * *Files 8% similar despite different names*

```diff
@@ -6,53 +6,77 @@
 
 import pefile
 
 import capa.features
 import capa.features.extractors.elf
 import capa.features.extractors.pefile
 import capa.features.extractors.strings
-from capa.features.common import OS, FORMAT_PE, FORMAT_ELF, OS_WINDOWS, FORMAT_FREEZE, Arch, Format, String, Feature
+from capa.features.common import (
+    OS,
+    OS_ANY,
+    OS_AUTO,
+    ARCH_ANY,
+    FORMAT_PE,
+    FORMAT_ELF,
+    OS_WINDOWS,
+    FORMAT_FREEZE,
+    FORMAT_RESULT,
+    Arch,
+    Format,
+    String,
+    Feature,
+)
 from capa.features.freeze import is_freeze
 from capa.features.address import NO_ADDRESS, Address, FileOffsetAddress
 
 logger = logging.getLogger(__name__)
 
+# match strings for formats
+MATCH_PE = b"MZ"
+MATCH_ELF = b"\x7fELF"
+MATCH_RESULT = b'{"meta":'
+
 
 def extract_file_strings(buf, **kwargs) -> Iterator[Tuple[String, Address]]:
     """
     extract ASCII and UTF-16 LE strings from file
     """
     for s in capa.features.extractors.strings.extract_ascii_strings(buf):
         yield String(s.s), FileOffsetAddress(s.offset)
 
     for s in capa.features.extractors.strings.extract_unicode_strings(buf):
         yield String(s.s), FileOffsetAddress(s.offset)
 
 
 def extract_format(buf) -> Iterator[Tuple[Feature, Address]]:
-    if buf.startswith(b"MZ"):
+    if buf.startswith(MATCH_PE):
         yield Format(FORMAT_PE), NO_ADDRESS
-    elif buf.startswith(b"\x7fELF"):
+    elif buf.startswith(MATCH_ELF):
         yield Format(FORMAT_ELF), NO_ADDRESS
     elif is_freeze(buf):
         yield Format(FORMAT_FREEZE), NO_ADDRESS
+    elif buf.startswith(MATCH_RESULT):
+        yield Format(FORMAT_RESULT), NO_ADDRESS
     else:
         # we likely end up here:
         #  1. handling a file format (e.g. macho)
         #
         # for (1), this logic will need to be updated as the format is implemented.
         logger.debug("unsupported file format: %s", binascii.hexlify(buf[:4]).decode("ascii"))
         return
 
 
 def extract_arch(buf) -> Iterator[Tuple[Feature, Address]]:
-    if buf.startswith(b"MZ"):
+    if buf.startswith(MATCH_PE):
         yield from capa.features.extractors.pefile.extract_file_arch(pe=pefile.PE(data=buf))
 
-    elif buf.startswith(b"\x7fELF"):
+    elif buf.startswith(MATCH_RESULT):
+        yield Arch(ARCH_ANY), NO_ADDRESS
+
+    elif buf.startswith(MATCH_ELF):
         with contextlib.closing(io.BytesIO(buf)) as f:
             arch = capa.features.extractors.elf.detect_elf_arch(f)
 
         if arch not in capa.features.common.VALID_ARCH:
             logger.debug("unsupported arch: %s", arch)
             return
 
@@ -69,18 +93,23 @@
         # rules that rely on arch conditions will fail to match on shellcode.
         #
         # for (2), this logic will need to be updated as the format is implemented.
         logger.debug("unsupported file format: %s, will not guess Arch", binascii.hexlify(buf[:4]).decode("ascii"))
         return
 
 
-def extract_os(buf) -> Iterator[Tuple[Feature, Address]]:
-    if buf.startswith(b"MZ"):
+def extract_os(buf, os=OS_AUTO) -> Iterator[Tuple[Feature, Address]]:
+    if os != OS_AUTO:
+        yield OS(os), NO_ADDRESS
+
+    if buf.startswith(MATCH_PE):
         yield OS(OS_WINDOWS), NO_ADDRESS
-    elif buf.startswith(b"\x7fELF"):
+    elif buf.startswith(MATCH_RESULT):
+        yield OS(OS_ANY), NO_ADDRESS
+    elif buf.startswith(MATCH_ELF):
         with contextlib.closing(io.BytesIO(buf)) as f:
             os = capa.features.extractors.elf.detect_elf_os(f)
 
         if os not in capa.features.common.VALID_OS:
             logger.debug("unsupported os: %s", os)
             return
 
@@ -88,14 +117,12 @@
 
     else:
         # we likely end up here:
         #  1. handling shellcode, or
         #  2. handling a new file format (e.g. macho)
         #
         # for (1) we can't do much - its shellcode and all bets are off.
-        # we could maybe accept a further CLI argument to specify the OS,
-        # but i think this would be rarely used.
         # rules that rely on OS conditions will fail to match on shellcode.
         #
         # for (2), this logic will need to be updated as the format is implemented.
         logger.debug("unsupported file format: %s, will not guess OS", binascii.hexlify(buf[:4]).decode("ascii"))
         return
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile/extractor.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile/extractor.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile/file.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile/file.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile/function.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile/function.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile/helpers.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile/helpers.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile/insn.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile/insn.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile/types.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile/types.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dnfile_.py` & `flare-capa-5.1.0/capa/features/extractors/dnfile_.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/dotnetfile.py` & `flare-capa-5.1.0/capa/features/extractors/dotnetfile.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/elf.py` & `flare-capa-5.1.0/capa/features/extractors/elf.py`

 * *Files 4% similar despite different names*

```diff
@@ -84,14 +84,15 @@
     name: int
     type: int
     flags: int
     addr: int
     offset: int
     size: int
     link: int
+    entsize: int
     buf: bytes
 
 
 class ELF:
     def __init__(self, f: BinaryIO):
         self.f = f
 
@@ -117,22 +118,22 @@
         ei_class, ei_data = struct.unpack_from("BB", self.file_header, 4)
         logger.debug("ei_class: 0x%02x ei_data: 0x%02x", ei_class, ei_data)
         if ei_class == 1:
             self.bitness = 32
         elif ei_class == 2:
             self.bitness = 64
         else:
-            raise CorruptElfFile("invalid ei_class: 0x%02x" % ei_class)
+            raise CorruptElfFile(f"invalid ei_class: 0x{ei_class:02x}")
 
         if ei_data == 1:
             self.endian = "<"
         elif ei_data == 2:
             self.endian = ">"
         else:
-            raise CorruptElfFile("not an ELF file: invalid ei_data: 0x%02x" % ei_data)
+            raise CorruptElfFile(f"not an ELF file: invalid ei_data: 0x{ei_data:02x}")
 
         if self.bitness == 32:
             e_phoff, e_shoff = struct.unpack_from(self.endian + "II", self.file_header, 0x1C)
             self.e_phentsize, self.e_phnum = struct.unpack_from(self.endian + "HH", self.file_header, 0x2A)
             self.e_shentsize, self.e_shnum = struct.unpack_from(self.endian + "HH", self.file_header, 0x2E)
         elif self.bitness == 64:
             e_phoff, e_shoff = struct.unpack_from(self.endian + "QQ", self.file_header, 0x20)
@@ -316,32 +317,32 @@
                 continue
 
     def parse_section_header(self, i) -> Shdr:
         shent_offset = i * self.e_shentsize
         shent = self.shbuf[shent_offset : shent_offset + self.e_shentsize]
 
         if self.bitness == 32:
-            sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size, sh_link = struct.unpack_from(
-                self.endian + "IIIIIII", shent, 0x0
+            sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size, sh_link, _, _, sh_entsize = struct.unpack_from(
+                self.endian + "IIIIIIIIII", shent, 0x0
             )
         elif self.bitness == 64:
-            sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size, sh_link = struct.unpack_from(
-                self.endian + "IIQQQQI", shent, 0x0
+            sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size, sh_link, _, _, sh_entsize = struct.unpack_from(
+                self.endian + "IIQQQQIIQQ", shent, 0x0
             )
         else:
             raise NotImplementedError()
 
         logger.debug("sh:sh_offset: 0x%02x sh_size: 0x%04x", sh_offset, sh_size)
 
         self.f.seek(sh_offset)
         buf = self.f.read(sh_size)
         if len(buf) != sh_size:
             raise ValueError("failed to read section header content")
 
-        return Shdr(sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size, sh_link, buf)
+        return Shdr(sh_name, sh_type, sh_flags, sh_addr, sh_offset, sh_size, sh_link, sh_entsize, buf)
 
     @property
     def section_headers(self):
         for i in range(self.e_shnum):
             try:
                 yield self.parse_section_header(i)
             except ValueError:
@@ -498,14 +499,31 @@
 
         for d_tag, d_val in self.dynamic_entries:
             if d_tag != DT_NEEDED:
                 continue
 
             yield read_cstr(strtab, d_val)
 
+    @property
+    def symtab(self) -> Optional[Tuple[Shdr, Shdr]]:
+        """
+        fetch the Shdr for the symtab and the associated strtab.
+        """
+        SHT_SYMTAB = 0x2
+        for shdr in self.section_headers:
+            if shdr.type != SHT_SYMTAB:
+                continue
+
+            # the linked section contains strings referenced by the symtab structures.
+            strtab_shdr = self.parse_section_header(shdr.link)
+
+            return shdr, strtab_shdr
+
+        return None
+
 
 @dataclass
 class ABITag:
     os: OS
     kmajor: int
     kminor: int
     kpatch: int
@@ -599,19 +617,84 @@
         if not os:
             return None
 
         logger.debug("abi tag: %s earliest compatible kernel: %d.%d.%d", os, kmajor, kminor, kpatch)
         return ABITag(os, kmajor, kminor, kpatch)
 
 
-def guess_os_from_osabi(elf) -> Optional[OS]:
+@dataclass
+class Symbol:
+    name_offset: int
+    value: int
+    size: int
+    info: int
+    other: int
+    shndx: int
+
+
+class SymTab:
+    def __init__(
+        self,
+        endian: str,
+        bitness: int,
+        symtab: Shdr,
+        strtab: Shdr,
+    ) -> None:
+        self.symbols: List[Symbol] = []
+
+        self.symtab = symtab
+        self.strtab = strtab
+
+        self._parse(endian, bitness, symtab.buf)
+
+    def _parse(self, endian: str, bitness: int, symtab_buf: bytes) -> None:
+        """
+        return the symbol's information in
+        the order specified by sys/elf32.h
+        """
+        for i in range(int(len(self.symtab.buf) / self.symtab.entsize)):
+            if bitness == 32:
+                name_offset, value, size, info, other, shndx = struct.unpack_from(
+                    endian + "IIIBBH", symtab_buf, i * self.symtab.entsize
+                )
+            elif bitness == 64:
+                name_offset, info, other, shndx, value, size = struct.unpack_from(
+                    endian + "IBBBQQ", symtab_buf, i * self.symtab.entsize
+                )
+
+            self.symbols.append(Symbol(name_offset, value, size, info, other, shndx))
+
+    def get_name(self, symbol: Symbol) -> str:
+        """
+        fetch a symbol's name from symtab's
+        associated strings' section (SHT_STRTAB)
+        """
+        if not self.strtab:
+            raise ValueError("no strings found")
+
+        for i in range(symbol.name_offset, self.strtab.size):
+            if self.strtab.buf[i] == 0:
+                return self.strtab.buf[symbol.name_offset : i].decode("utf-8")
+
+        raise ValueError("symbol name not found")
+
+    def get_symbols(self) -> Iterator[Symbol]:
+        """
+        return a tuple: (name, value, size, info, other, shndx)
+        for each symbol contained in the symbol table
+        """
+        for symbol in self.symbols:
+            yield symbol
+
+
+def guess_os_from_osabi(elf: ELF) -> Optional[OS]:
     return elf.ei_osabi
 
 
-def guess_os_from_ph_notes(elf) -> Optional[OS]:
+def guess_os_from_ph_notes(elf: ELF) -> Optional[OS]:
     # search for PT_NOTE sections that specify an OS
     # for example, on Linux there is a GNU section with minimum kernel version
     PT_NOTE = 0x4
     for phdr in elf.program_headers:
         if phdr.type != PT_NOTE:
             continue
 
@@ -642,15 +725,15 @@
             else:
                 # cannot make a guess about the OS, but probably linux or hurd
                 pass
 
     return None
 
 
-def guess_os_from_sh_notes(elf) -> Optional[OS]:
+def guess_os_from_sh_notes(elf: ELF) -> Optional[OS]:
     # search for notes stored in sections that aren't visible in program headers.
     # e.g. .note.Linux in Linux kernel modules.
     SHT_NOTE = 0x7
     for shdr in elf.section_headers:
         if shdr.type != SHT_NOTE:
             continue
 
@@ -675,25 +758,25 @@
             else:
                 # cannot make a guess about the OS, but probably linux or hurd
                 pass
 
     return None
 
 
-def guess_os_from_linker(elf) -> Optional[OS]:
+def guess_os_from_linker(elf: ELF) -> Optional[OS]:
     # search for recognizable dynamic linkers (interpreters)
     # for example, on linux, we see file paths like: /lib64/ld-linux-x86-64.so.2
     linker = elf.linker
     if linker and "ld-linux" in elf.linker:
         return OS.LINUX
 
     return None
 
 
-def guess_os_from_abi_versions_needed(elf) -> Optional[OS]:
+def guess_os_from_abi_versions_needed(elf: ELF) -> Optional[OS]:
     # then lets look for GLIBC symbol versioning requirements.
     # this will let us guess about linux/hurd in some cases.
 
     versions_needed = elf.versions_needed
     if any(map(lambda abi: abi.startswith("GLIBC"), itertools.chain(*versions_needed.values()))):
         # there are any GLIBC versions needed
 
@@ -716,24 +799,51 @@
             else:
                 # we don't have any good guesses based on versions needed
                 pass
 
     return None
 
 
-def guess_os_from_needed_dependencies(elf) -> Optional[OS]:
+def guess_os_from_needed_dependencies(elf: ELF) -> Optional[OS]:
     for needed in elf.needed:
         if needed.startswith("libmachuser.so"):
             return OS.HURD
         if needed.startswith("libhurduser.so"):
             return OS.HURD
 
     return None
 
 
+def guess_os_from_symtab(elf: ELF) -> Optional[OS]:
+    shdrs = elf.symtab
+    if not shdrs:
+        # executable does not contain a symbol table
+        # or the symbol's names are stripped
+        return None
+
+    symtab_shdr, strtab_shdr = shdrs
+    symtab = SymTab(elf.endian, elf.bitness, symtab_shdr, strtab_shdr)
+
+    keywords = {
+        OS.LINUX: [
+            "linux",
+            "/linux/",
+        ],
+    }
+
+    for symbol in symtab.get_symbols():
+        sym_name = symtab.get_name(symbol)
+
+        for os, hints in keywords.items():
+            if any(map(lambda x: x in sym_name, hints)):
+                return os
+
+    return None
+
+
 def detect_elf_os(f) -> str:
     """
     f: type Union[BinaryIO, IDAIO]
     """
     elf = ELF(f)
 
     osabi_guess = guess_os_from_osabi(elf)
@@ -750,14 +860,17 @@
 
     abi_versions_needed_guess = guess_os_from_abi_versions_needed(elf)
     logger.debug("guess: ABI versions needed: %s", abi_versions_needed_guess)
 
     needed_dependencies_guess = guess_os_from_needed_dependencies(elf)
     logger.debug("guess: needed dependencies: %s", needed_dependencies_guess)
 
+    symtab_guess = guess_os_from_symtab(elf)
+    logger.debug("guess: pertinent symbol name: %s", symtab_guess)
+
     ret = None
 
     if osabi_guess:
         ret = osabi_guess
 
     elif ph_notes_guess:
         ret = ph_notes_guess
@@ -770,12 +883,15 @@
 
     elif abi_versions_needed_guess:
         ret = abi_versions_needed_guess
 
     elif needed_dependencies_guess:
         ret = needed_dependencies_guess
 
+    elif symtab_guess:
+        ret = symtab_guess
+
     return ret.value if ret is not None else "unknown"
 
 
 def detect_elf_arch(f: BinaryIO) -> str:
     return ELF(f).e_machine or "unknown"
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/elffile.py` & `flare-capa-5.1.0/capa/features/extractors/elffile.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/helpers.py` & `flare-capa-5.1.0/capa/features/extractors/helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -51,23 +51,23 @@
       - CreateFileA
       - CreateFile
     """
     # normalize dll name
     dll = dll.lower()
 
     # kernel32.CreateFileA
-    yield "%s.%s" % (dll, symbol)
+    yield f"{dll}.{symbol}"
 
     if not is_ordinal(symbol):
         # CreateFileA
         yield symbol
 
     if is_aw_function(symbol):
         # kernel32.CreateFile
-        yield "%s.%s" % (dll, symbol[:-1])
+        yield f"{dll}.{symbol[:-1]}"
 
         if not is_ordinal(symbol):
             # CreateFile
             yield symbol[:-1]
 
 
 def all_zeros(bytez: bytes) -> bool:
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/basicblock.py` & `flare-capa-5.1.0/capa/features/extractors/ida/basicblock.py`

 * *Files 1% similar despite different names*

```diff
@@ -30,15 +30,15 @@
     elif op.dtype == idaapi.dt_word:
         chars = struct.pack("<H", op_val)
     elif op.dtype == idaapi.dt_dword:
         chars = struct.pack("<I", op_val)
     elif op.dtype == idaapi.dt_qword:
         chars = struct.pack("<Q", op_val)
     else:
-        raise ValueError("Unhandled operand data type 0x%x." % op.dtype)
+        raise ValueError(f"Unhandled operand data type 0x{op.dtype:x}.")
 
     def is_printable_ascii(chars_: bytes):
         return all(c < 127 and chr(c) in string.printable for c in chars_)
 
     def is_printable_utf16le(chars_: bytes):
         if all(c == 0x00 for c in chars_[1::2]):
             return is_printable_ascii(chars_[::2])
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/extractor.py` & `flare-capa-5.1.0/capa/features/extractors/ida/extractor.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/file.py` & `flare-capa-5.1.0/capa/features/extractors/ida/file.py`

 * *Files 7% similar despite different names*

```diff
@@ -17,57 +17,61 @@
 import capa.features.extractors.helpers
 import capa.features.extractors.strings
 import capa.features.extractors.ida.helpers
 from capa.features.file import Export, Import, Section, FunctionName
 from capa.features.common import FORMAT_PE, FORMAT_ELF, Format, String, Feature, Characteristic
 from capa.features.address import NO_ADDRESS, Address, FileOffsetAddress, AbsoluteVirtualAddress
 
+MAX_OFFSET_PE_AFTER_MZ = 0x200
+
 
 def check_segment_for_pe(seg: idaapi.segment_t) -> Iterator[Tuple[int, int]]:
     """check segment for embedded PE
 
     adapted for IDA from:
-    https://github.com/vivisect/vivisect/blob/7be4037b1cecc4551b397f840405a1fc606f9b53/PE/carve.py#L19
+    https://github.com/vivisect/vivisect/blob/91e8419a861f49779f18316f155311967e696836/PE/carve.py#L25
     """
     seg_max = seg.end_ea
     mz_xor = [
         (
             capa.features.extractors.helpers.xor_static(b"MZ", i),
             capa.features.extractors.helpers.xor_static(b"PE", i),
             i,
         )
         for i in range(256)
     ]
 
     todo = []
     for mzx, pex, i in mz_xor:
+        # find all segment offsets containing XOR'd "MZ" bytes
         for off in capa.features.extractors.ida.helpers.find_byte_sequence(seg.start_ea, seg.end_ea, mzx):
             todo.append((off, mzx, pex, i))
 
     while len(todo):
         off, mzx, pex, i = todo.pop()
 
-        # The MZ header has one field we will check e_lfanew is at 0x3c
+        # MZ header has one field we will check e_lfanew is at 0x3c
         e_lfanew = off + 0x3C
 
         if seg_max < (e_lfanew + 4):
             continue
 
         newoff = struct.unpack("<I", capa.features.extractors.helpers.xor_static(idc.get_bytes(e_lfanew, 4), i))[0]
 
+        # assume XOR'd "PE" bytes exist within threshold
+        if newoff > MAX_OFFSET_PE_AFTER_MZ:
+            continue
+
         peoff = off + newoff
         if seg_max < (peoff + 2):
             continue
 
         if idc.get_bytes(peoff, 2) == pex:
             yield off, i
 
-        for nextres in capa.features.extractors.ida.helpers.find_byte_sequence(off + 1, seg.end_ea, mzx):
-            todo.append((nextres, mzx, pex, i))
-
 
 def extract_file_embedded_pe() -> Iterator[Tuple[Feature, Address]]:
     """extract embedded PE features
 
     IDA must load resource sections for this to be complete
         - '-R' from console
         - Check 'Load resource sections' when opening binary in IDA manually
@@ -98,21 +102,21 @@
         addr = AbsoluteVirtualAddress(ea)
         if info[1] and info[2]:
             # e.g. in mimikatz: ('cabinet', 'FCIAddFile', 11L)
             # extract by name here and by ordinal below
             for name in capa.features.extractors.helpers.generate_symbols(info[0], info[1]):
                 yield Import(name), addr
             dll = info[0]
-            symbol = "#%d" % (info[2])
+            symbol = f"#{info[2]}"
         elif info[1]:
             dll = info[0]
             symbol = info[1]
         elif info[2]:
             dll = info[0]
-            symbol = "#%d" % (info[2])
+            symbol = f"#{info[2]}"
         else:
             continue
 
         for name in capa.features.extractors.helpers.generate_symbols(dll, symbol):
             yield Import(name), addr
 
     for ea, info in capa.features.extractors.ida.helpers.get_file_externs().items():
@@ -172,15 +176,15 @@
         yield Format(FORMAT_PE), NO_ADDRESS
     elif file_info.filetype == idaapi.f_ELF:
         yield Format(FORMAT_ELF), NO_ADDRESS
     elif file_info.filetype == idaapi.f_BIN:
         # no file type to return when processing a binary file, but we want to continue processing
         return
     else:
-        raise NotImplementedError("unexpected file format: %d" % file_info.filetype)
+        raise NotImplementedError(f"unexpected file format: {file_info.filetype}")
 
 
 def extract_features() -> Iterator[Tuple[Feature, Address]]:
     """extract file features"""
     for file_handler in FILE_HANDLERS:
         for feature, addr in file_handler():
             yield feature, addr
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/function.py` & `flare-capa-5.1.0/capa/features/extractors/ida/function.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/global_.py` & `flare-capa-5.1.0/capa/features/extractors/ida/global_.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/helpers.py` & `flare-capa-5.1.0/capa/features/extractors/ida/helpers.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,15 +21,15 @@
     """yield all ea of a given byte sequence
 
     args:
         start: min virtual address
         end: max virtual address
         seq: bytes to search e.g. b"\x01\x03"
     """
-    seqstr = " ".join(["%02x" % b for b in seq])
+    seqstr = " ".join([f"{b:02x}" for b in seq])
     while True:
         # TODO find_binary: Deprecated. Please use ida_bytes.bin_search() instead.
         ea = idaapi.find_binary(start, end, seqstr, 0, idaapi.SEARCH_DOWN)
         if ea == idaapi.BADADDR:
             break
         start = ea + 1
         yield ea
@@ -86,16 +86,19 @@
 
     for idx in range(idaapi.get_import_module_qty()):
         library = idaapi.get_import_module_name(idx)
 
         if not library:
             continue
 
-        # IDA uses section names for the library of ELF imports, like ".dynsym"
-        library = library.lstrip(".")
+        # IDA uses section names for the library of ELF imports, like ".dynsym".
+        # These are not useful to us, we may need to expand this list over time
+        # TODO: exhaust this list, see #1419
+        if library == ".dynsym":
+            library = ""
 
         def inspect_import(ea, function, ordinal):
             if function and function.startswith("__imp_"):
                 # handle mangled PE imports
                 function = function[len("__imp_") :]
 
             if function and "@@" in function:
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/ida/insn.py` & `flare-capa-5.1.0/capa/features/extractors/ida/insn.py`

 * *Files 0% similar despite different names*

```diff
@@ -168,15 +168,15 @@
     if idaapi.is_call_insn(insn):
         return
 
     ref = capa.features.extractors.ida.helpers.find_data_reference_from_insn(insn)
     if ref != insn.ea:
         extracted_bytes = capa.features.extractors.ida.helpers.read_bytes_at(ref, MAX_BYTES_FEATURE_SIZE)
         if extracted_bytes and not capa.features.extractors.helpers.all_zeros(extracted_bytes):
-            if not capa.features.extractors.ida.helpers.find_string_at(insn.ea):
+            if not capa.features.extractors.ida.helpers.find_string_at(ref):
                 # don't extract byte features for obvious strings
                 yield Bytes(extracted_bytes), ih.address
 
 
 def extract_insn_string_features(
     fh: FunctionHandle, bbh: BBHandle, ih: InsnHandle
 ) -> Iterator[Tuple[Feature, Address]]:
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/loops.py` & `flare-capa-5.1.0/capa/features/extractors/loops.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/null.py` & `flare-capa-5.1.0/capa/features/extractors/null.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/pefile.py` & `flare-capa-5.1.0/capa/features/extractors/pefile.py`

 * *Files 1% similar despite different names*

```diff
@@ -60,15 +60,15 @@
                 continue
 
             # strip extension
             modname = modname.rpartition(".")[0].lower()
 
             for imp in dll.imports:
                 if imp.import_by_ordinal:
-                    impname = "#%s" % imp.ordinal
+                    impname = f"#{imp.ordinal}"
                 else:
                     try:
                         impname = imp.name.partition(b"\x00")[0].decode("ascii")
                     except UnicodeDecodeError:
                         continue
 
                 for name in capa.features.extractors.helpers.generate_symbols(modname, impname):
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/strings.py` & `flare-capa-5.1.0/capa/features/extractors/strings.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/basicblock.py` & `flare-capa-5.1.0/capa/features/extractors/viv/basicblock.py`

 * *Files 2% similar despite different names*

```diff
@@ -117,15 +117,15 @@
     elif oper.tsize == 2:
         chars = struct.pack("<H", oper.imm)
     elif oper.tsize == 4:
         chars = struct.pack("<I", oper.imm)
     elif oper.tsize == 8:
         chars = struct.pack("<Q", oper.imm)
     else:
-        raise ValueError("unexpected oper.tsize: %d" % (oper.tsize))
+        raise ValueError(f"unexpected oper.tsize: {oper.tsize}")
 
     if is_printable_ascii(chars):
         return oper.tsize
     elif is_printable_utf16le(chars):
         return oper.tsize / 2
     else:
         return 0
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/extractor.py` & `flare-capa-5.1.0/capa/features/extractors/viv/extractor.py`

 * *Files 2% similar despite different names*

```diff
@@ -21,25 +21,25 @@
 from capa.features.address import Address, AbsoluteVirtualAddress
 from capa.features.extractors.base_extractor import BBHandle, InsnHandle, FunctionHandle, FeatureExtractor
 
 logger = logging.getLogger(__name__)
 
 
 class VivisectFeatureExtractor(FeatureExtractor):
-    def __init__(self, vw, path):
+    def __init__(self, vw, path, os):
         super().__init__()
         self.vw = vw
         self.path = path
         with open(self.path, "rb") as f:
             self.buf = f.read()
 
         # pre-compute these because we'll yield them at *every* scope.
         self.global_features: List[Tuple[Feature, Address]] = []
         self.global_features.extend(capa.features.extractors.viv.file.extract_file_format(self.buf))
-        self.global_features.extend(capa.features.extractors.common.extract_os(self.buf))
+        self.global_features.extend(capa.features.extractors.common.extract_os(self.buf, os))
         self.global_features.extend(capa.features.extractors.viv.global_.extract_arch(self.vw))
 
     def get_base_address(self):
         # assume there is only one file loaded into the vw
         return AbsoluteVirtualAddress(list(self.vw.filemeta.values())[0]["imagebase"])
 
     def extract_global_features(self):
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/file.py` & `flare-capa-5.1.0/capa/features/extractors/viv/file.py`

 * *Files 1% similar despite different names*

```diff
@@ -40,15 +40,15 @@
      - importname
     """
     for va, _, _, tinfo in vw.getImports():
         # vivisect source: tinfo = "%s.%s" % (libname, impname)
         modname, impname = tinfo.split(".", 1)
         if is_viv_ord_impname(impname):
             # replace ord prefix with #
-            impname = "#%s" % impname[len("ord") :]
+            impname = "#" + impname[len("ord") :]
 
         addr = AbsoluteVirtualAddress(va)
         for name in capa.features.extractors.helpers.generate_symbols(modname, impname):
             yield Import(name), addr
 
 
 def is_viv_ord_impname(impname: str) -> bool:
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/function.py` & `flare-capa-5.1.0/capa/features/extractors/viv/function.py`

 * *Files 10% similar despite different names*

```diff
@@ -43,14 +43,18 @@
     f: viv_utils.Function = fhandle.inner
 
     edges = []
 
     for bb in f.basic_blocks:
         if len(bb.instructions) > 0:
             for bva, bflags in bb.instructions[-1].getBranches():
+                if bva is None:
+                    # vivisect may be unable to recover the call target, e.g. on dynamic calls like `call esi`
+                    # for this bva is None, and we don't want to add it for loop detection, ref: vivisect#574
+                    continue
                 # vivisect does not set branch flags for non-conditional jmp so add explicit check
                 if (
                     bflags & envi.BR_COND
                     or bflags & envi.BR_FALL
                     or bflags & envi.BR_TABLE
                     or bb.instructions[-1].mnem == "jmp"
                 ):
```

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/global_.py` & `flare-capa-5.1.0/capa/features/extractors/viv/global_.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/helpers.py` & `flare-capa-5.1.0/capa/features/extractors/viv/helpers.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/indirect_calls.py` & `flare-capa-5.1.0/capa/features/extractors/viv/indirect_calls.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/extractors/viv/insn.py` & `flare-capa-5.1.0/capa/features/extractors/viv/insn.py`

 * *Files 1% similar despite different names*

```diff
@@ -171,16 +171,21 @@
 
     this is a "do what i mean" type of helper function.
     """
     depth = 0
     while True:
         if not vw.isValidPointer(p):
             return
+
         yield p
 
+        if vw.isProbablyString(p) or vw.isProbablyUnicode(p):
+            # don't deref strings that coincidentally are pointers
+            return
+
         try:
             next = vw.readMemoryPtr(p)
         except Exception:
             # if not enough bytes can be read, such as end of the section.
             # unfortunately, viv returns a plain old generic `Exception` for this.
             return
 
@@ -267,15 +272,15 @@
                 buf = read_bytes(f.vw, v)
             except envi.exc.SegmentationViolation:
                 continue
 
             if capa.features.extractors.helpers.all_zeros(buf):
                 continue
 
-            if f.vw.isProbablyString(v):
+            if f.vw.isProbablyString(v) or f.vw.isProbablyUnicode(v):
                 # don't extract byte features for obvious strings
                 continue
 
             yield Bytes(buf), ih.address
 
 
 def read_string(vw, offset: int) -> str:
```

### Comparing `flare-capa-5.0.0/capa/features/file.py` & `flare-capa-5.1.0/capa/features/file.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/features/freeze/__init__.py` & `flare-capa-5.1.0/capa/features/freeze/__init__.py`

 * *Files 15% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 Unless required by applicable law or agreed to in writing, software distributed under the License
  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and limitations under the License.
 """
 import zlib
 import logging
 from enum import Enum
-from typing import Any, List, Tuple
+from typing import Any, List, Tuple, Union
 
 from pydantic import Field, BaseModel
 
 import capa.helpers
 import capa.version
 import capa.features.file
 import capa.features.insn
@@ -42,15 +42,15 @@
     DN_TOKEN = "dn token"
     DN_TOKEN_OFFSET = "dn token offset"
     NO_ADDRESS = "no address"
 
 
 class Address(HashableModel):
     type: AddressType
-    value: Any
+    value: Union[int, Tuple[int, int], None]
 
     @classmethod
     def from_capa(cls, a: capa.features.address.Address) -> "Address":
         if isinstance(a, capa.features.address.AbsoluteVirtualAddress):
             return cls(type=AddressType.ABSOLUTE, value=int(a))
 
         elif isinstance(a, capa.features.address.RelativeVirtualAddress):
@@ -75,27 +75,34 @@
             raise ValueError("don't use an Address instance directly")
 
         else:
             assert_never(a)
 
     def to_capa(self) -> capa.features.address.Address:
         if self.type is AddressType.ABSOLUTE:
+            assert isinstance(self.value, int)
             return capa.features.address.AbsoluteVirtualAddress(self.value)
 
         elif self.type is AddressType.RELATIVE:
+            assert isinstance(self.value, int)
             return capa.features.address.RelativeVirtualAddress(self.value)
 
         elif self.type is AddressType.FILE:
+            assert isinstance(self.value, int)
             return capa.features.address.FileOffsetAddress(self.value)
 
         elif self.type is AddressType.DN_TOKEN:
+            assert isinstance(self.value, int)
             return capa.features.address.DNTokenAddress(self.value)
 
         elif self.type is AddressType.DN_TOKEN_OFFSET:
+            assert isinstance(self.value, tuple)
             token, offset = self.value
+            assert isinstance(token, int)
+            assert isinstance(offset, int)
             return capa.features.address.DNTokenOffsetAddress(token, offset)
 
         elif self.type is AddressType.NO_ADDRESS:
             return capa.features.address.NO_ADDRESS
 
         else:
             assert_never(self.type)
@@ -104,15 +111,19 @@
         if self.type != other.type:
             return self.type < other.type
 
         if self.type is AddressType.NO_ADDRESS:
             return True
 
         else:
-            return self.value < other.value
+            assert self.type == other.type
+            # mypy doesn't realize we've proven that either
+            # both are ints, or both are tuples of ints.
+            # and both of these are comparable.
+            return self.value < other.value  # type: ignore
 
 
 class GlobalFeature(HashableModel):
     feature: Feature
 
 
 class FileFeature(HashableModel):
@@ -253,15 +264,16 @@
         for bb in extractor.get_basic_blocks(f):
             bbaddr = Address.from_capa(bb.address)
             bbfeatures = [
                 BasicBlockFeature(
                     basic_block=bbaddr,
                     address=Address.from_capa(addr),
                     feature=feature_from_capa(feature),
-                )
+                )  # type: ignore
+                # Mypy is unable to recognise `basic_block` as a argument due to alias
                 for feature, addr in extractor.extract_basic_block_features(f, bb)
             ]
 
             instructions = []
             for insn in extractor.get_instructions(f, bb):
                 iaddr = Address.from_capa(insn.address)
                 ifeatures = [
@@ -272,57 +284,60 @@
                     )
                     for feature, addr in extractor.extract_insn_features(f, bb, insn)
                 ]
 
                 instructions.append(
                     InstructionFeatures(
                         address=iaddr,
-                        features=ifeatures,
+                        features=tuple(ifeatures),
                     )
                 )
 
             basic_blocks.append(
                 BasicBlockFeatures(
                     address=bbaddr,
-                    features=bbfeatures,
-                    instructions=instructions,
+                    features=tuple(bbfeatures),
+                    instructions=tuple(instructions),
                 )
             )
 
         function_features.append(
             FunctionFeatures(
                 address=faddr,
-                features=ffeatures,
+                features=tuple(ffeatures),
                 basic_blocks=basic_blocks,
-            )
+            )  # type: ignore
+            # Mypy is unable to recognise `basic_blocks` as a argument due to alias
         )
 
     features = Features(
         global_=global_features,
-        file=file_features,
-        functions=function_features,
-    )
+        file=tuple(file_features),
+        functions=tuple(function_features),
+    )  # type: ignore
+    # Mypy is unable to recognise `global_` as a argument due to alias
 
     freeze = Freeze(
         version=2,
         base_address=Address.from_capa(extractor.get_base_address()),
         extractor=Extractor(name=extractor.__class__.__name__),
         features=features,
-    )
+    )  # type: ignore
+    # Mypy is unable to recognise `base_address` as a argument due to alias
 
     return freeze.json()
 
 
 def loads(s: str) -> capa.features.extractors.base_extractor.FeatureExtractor:
     """deserialize a set of features (as a NullFeatureExtractor) from a string."""
     import capa.features.extractors.null as null
 
     freeze = Freeze.parse_raw(s)
     if freeze.version != 2:
-        raise ValueError("unsupported freeze format version: %d", freeze.version)
+        raise ValueError(f"unsupported freeze format version: {freeze.version}")
 
     return null.NullFeatureExtractor(
         base_address=freeze.base_address.to_capa(),
         global_features=[f.feature.to_capa() for f in freeze.features.global_],
         file_features=[(f.address.to_capa(), f.feature.to_capa()) for f in freeze.features.file],
         functions={
             f.address.to_capa(): null.FunctionFeatures(
@@ -370,22 +385,22 @@
 
     import capa.main
 
     if argv is None:
         argv = sys.argv[1:]
 
     parser = argparse.ArgumentParser(description="save capa features to a file")
-    capa.main.install_common_args(parser, {"sample", "format", "backend", "signatures"})
+    capa.main.install_common_args(parser, {"sample", "format", "backend", "os", "signatures"})
     parser.add_argument("output", type=str, help="Path to output file")
     args = parser.parse_args(args=argv)
     capa.main.handle_common_args(args)
 
     sigpaths = capa.main.get_signatures(args.signatures)
 
-    extractor = capa.main.get_extractor(args.sample, args.format, args.backend, sigpaths, False)
+    extractor = capa.main.get_extractor(args.sample, args.format, args.os, args.backend, sigpaths, False)
 
     with open(args.output, "wb") as f:
         f.write(dump(extractor))
 
     return 0
```

### Comparing `flare-capa-5.0.0/capa/features/freeze/features.py` & `flare-capa-5.1.0/capa/features/freeze/features.py`

 * *Files 11% similar despite different names*

```diff
@@ -97,85 +97,111 @@
 
         else:
             raise NotImplementedError(f"Feature.to_capa({type(self)}) not implemented")
 
 
 def feature_from_capa(f: capa.features.common.Feature) -> "Feature":
     if isinstance(f, capa.features.common.OS):
+        assert isinstance(f.value, str)
         return OSFeature(os=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.Arch):
+        assert isinstance(f.value, str)
         return ArchFeature(arch=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.Format):
+        assert isinstance(f.value, str)
         return FormatFeature(format=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.MatchedRule):
+        assert isinstance(f.value, str)
         return MatchFeature(match=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.Characteristic):
+        assert isinstance(f.value, str)
         return CharacteristicFeature(characteristic=f.value, description=f.description)
 
     elif isinstance(f, capa.features.file.Export):
+        assert isinstance(f.value, str)
         return ExportFeature(export=f.value, description=f.description)
 
     elif isinstance(f, capa.features.file.Import):
-        return ImportFeature(import_=f.value, description=f.description)
+        assert isinstance(f.value, str)
+        return ImportFeature(import_=f.value, description=f.description)  # type: ignore
+        # Mypy is unable to recognise `import_` as a argument due to alias
 
     elif isinstance(f, capa.features.file.Section):
+        assert isinstance(f.value, str)
         return SectionFeature(section=f.value, description=f.description)
 
     elif isinstance(f, capa.features.file.FunctionName):
-        return FunctionNameFeature(function_name=f.value, description=f.description)
+        assert isinstance(f.value, str)
+        return FunctionNameFeature(function_name=f.value, description=f.description)  # type: ignore
+        # Mypy is unable to recognise `function_name` as a argument due to alias
 
     # must come before check for String due to inheritance
     elif isinstance(f, capa.features.common.Substring):
+        assert isinstance(f.value, str)
         return SubstringFeature(substring=f.value, description=f.description)
 
     # must come before check for String due to inheritance
     elif isinstance(f, capa.features.common.Regex):
+        assert isinstance(f.value, str)
         return RegexFeature(regex=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.String):
+        assert isinstance(f.value, str)
         return StringFeature(string=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.Class):
-        return ClassFeature(class_=f.value, description=f.description)
+        assert isinstance(f.value, str)
+        return ClassFeature(class_=f.value, description=f.description)  # type: ignore
+        # Mypy is unable to recognise `class_` as a argument due to alias
 
     elif isinstance(f, capa.features.common.Namespace):
+        assert isinstance(f.value, str)
         return NamespaceFeature(namespace=f.value, description=f.description)
 
     elif isinstance(f, capa.features.basicblock.BasicBlock):
         return BasicBlockFeature(description=f.description)
 
     elif isinstance(f, capa.features.insn.API):
+        assert isinstance(f.value, str)
         return APIFeature(api=f.value, description=f.description)
 
     elif isinstance(f, capa.features.insn.Property):
+        assert isinstance(f.value, str)
         return PropertyFeature(property=f.value, access=f.access, description=f.description)
 
     elif isinstance(f, capa.features.insn.Number):
+        assert isinstance(f.value, (int, float))
         return NumberFeature(number=f.value, description=f.description)
 
     elif isinstance(f, capa.features.common.Bytes):
         buf = f.value
         assert isinstance(buf, bytes)
         return BytesFeature(bytes=binascii.hexlify(buf).decode("ascii"), description=f.description)
 
     elif isinstance(f, capa.features.insn.Offset):
+        assert isinstance(f.value, int)
         return OffsetFeature(offset=f.value, description=f.description)
 
     elif isinstance(f, capa.features.insn.Mnemonic):
+        assert isinstance(f.value, str)
         return MnemonicFeature(mnemonic=f.value, description=f.description)
 
     elif isinstance(f, capa.features.insn.OperandNumber):
-        return OperandNumberFeature(index=f.index, operand_number=f.value, description=f.description)
+        assert isinstance(f.value, int)
+        return OperandNumberFeature(index=f.index, operand_number=f.value, description=f.description)  # type: ignore
+        # Mypy is unable to recognise `operand_number` as a argument due to alias
 
     elif isinstance(f, capa.features.insn.OperandOffset):
-        return OperandOffsetFeature(index=f.index, operand_offset=f.value, description=f.description)
+        assert isinstance(f.value, int)
+        return OperandOffsetFeature(index=f.index, operand_offset=f.value, description=f.description)  # type: ignore
+        # Mypy is unable to recognise `operand_offset` as a argument due to alias
 
     else:
         raise NotImplementedError(f"feature_from_capa({type(f)}) not implemented")
 
 
 class OSFeature(FeatureModel):
     type: str = "os"
```

### Comparing `flare-capa-5.0.0/capa/features/insn.py` & `flare-capa-5.1.0/capa/features/insn.py`

 * *Files 27% similar despite different names*

```diff
@@ -11,31 +11,31 @@
 import capa.helpers
 from capa.features.common import VALID_FEATURE_ACCESS, Feature
 
 
 def hex(n: int) -> str:
     """render the given number using upper case hex, like: 0x123ABC"""
     if n < 0:
-        return "-0x%X" % (-n)
+        return f"-0x{(-n):X}"
     else:
-        return "0x%X" % n
+        return f"0x{(n):X}"
 
 
 class API(Feature):
     def __init__(self, name: str, description=None):
         super().__init__(name, description=description)
 
 
 class _AccessFeature(Feature, abc.ABC):
     # superclass: don't use directly
     def __init__(self, value: str, access: Optional[str] = None, description: Optional[str] = None):
         super().__init__(value, description=description)
         if access is not None:
             if access not in VALID_FEATURE_ACCESS:
-                raise ValueError("%s access type %s not valid" % (self.name, access))
+                raise ValueError(f"{self.name} access type {access} not valid")
         self.access = access
 
     def __hash__(self):
         return hash((self.name, self.value, self.access))
 
     def __eq__(self, other):
         return super().__eq__(other) and self.access == other.access
@@ -49,31 +49,48 @@
 class Property(_AccessFeature):
     def __init__(self, value: str, access: Optional[str] = None, description=None):
         super().__init__(value, access=access, description=description)
 
 
 class Number(Feature):
     def __init__(self, value: Union[int, float], description=None):
+        """
+        args:
+          value (int or float): positive or negative integer, or floating point number.
+
+        the range of the value is:
+          - if positive, the range of u64
+          - if negative, the range of i64
+          - if floating, the range and precision of double
+        """
         super().__init__(value, description=description)
 
     def get_value_str(self):
         if isinstance(self.value, int):
             return capa.helpers.hex(self.value)
         elif isinstance(self.value, float):
             return str(self.value)
         else:
-            raise ValueError("invalid value type")
+            raise ValueError(f"invalid value type {type(self.value)}")
 
 
 # max recognized structure size (and therefore, offset size)
 MAX_STRUCTURE_SIZE = 0x10000
 
 
 class Offset(Feature):
     def __init__(self, value: int, description=None):
+        """
+        args:
+          value (int): the offset, which can be positive or negative.
+
+        the range of the value is:
+          - if positive, the range of u64
+          - if negative, the range of i64
+        """
         super().__init__(value, description=description)
 
     def get_value_str(self):
         assert isinstance(self.value, int)
         return hex(self.value)
 
 
@@ -88,44 +105,65 @@
 MAX_OPERAND_COUNT = 4
 MAX_OPERAND_INDEX = MAX_OPERAND_COUNT - 1
 
 
 class _Operand(Feature, abc.ABC):
     # superclass: don't use directly
     # subclasses should set self.name and provide the value string formatter
-    def __init__(self, index: int, value: int, description=None):
+    def __init__(self, index: int, value: Union[int, float], description=None):
         super().__init__(value, description=description)
         self.index = index
 
     def __hash__(self):
         return hash((self.name, self.value))
 
     def __eq__(self, other):
         return super().__eq__(other) and self.index == other.index
 
 
 class OperandNumber(_Operand):
     # cached names so we don't do extra string formatting every ctor
-    NAMES = ["operand[%d].number" % i for i in range(MAX_OPERAND_COUNT)]
+    NAMES = [f"operand[{i}].number" for i in range(MAX_OPERAND_COUNT)]
 
     # operand[i].number: 0x12
-    def __init__(self, index: int, value: int, description=None):
+    def __init__(self, index: int, value: Union[int, float], description=None):
+        """
+        args:
+          value (int or float): positive or negative integer, or floating point number.
+
+        the range of the value is:
+          - if positive, the range of u64
+          - if negative, the range of i64
+          - if floating, the range and precision of double
+        """
         super().__init__(index, value, description=description)
         self.name = self.NAMES[index]
 
     def get_value_str(self) -> str:
-        assert isinstance(self.value, int)
-        return hex(self.value)
+        if isinstance(self.value, int):
+            return capa.helpers.hex(self.value)
+        elif isinstance(self.value, float):
+            return str(self.value)
+        else:
+            raise ValueError("invalid value type")
 
 
 class OperandOffset(_Operand):
     # cached names so we don't do extra string formatting every ctor
-    NAMES = ["operand[%d].offset" % i for i in range(MAX_OPERAND_COUNT)]
+    NAMES = [f"operand[{i}].offset" for i in range(MAX_OPERAND_COUNT)]
 
     # operand[i].offset: 0x12
     def __init__(self, index: int, value: int, description=None):
+        """
+        args:
+          value (int): the offset, which can be positive or negative.
+
+        the range of the value is:
+          - if positive, the range of u64
+          - if negative, the range of i64
+        """
         super().__init__(index, value, description=description)
         self.name = self.NAMES[index]
 
     def get_value_str(self) -> str:
         assert isinstance(self.value, int)
         return hex(self.value)
```

### Comparing `flare-capa-5.0.0/capa/helpers.py` & `flare-capa-5.1.0/capa/helpers.py`

 * *Files 3% similar despite different names*

```diff
@@ -18,37 +18,37 @@
 
 logger = logging.getLogger("capa")
 
 
 def hex(n: int) -> str:
     """render the given number using upper case hex, like: 0x123ABC"""
     if n < 0:
-        return "-0x%X" % (-n)
+        return f"-0x{(-n):X}"
     else:
-        return "0x%X" % n
+        return f"0x{(n):X}"
 
 
 def get_file_taste(sample_path: str) -> bytes:
     if not os.path.exists(sample_path):
-        raise IOError("sample path %s does not exist or cannot be accessed" % sample_path)
+        raise IOError(f"sample path {sample_path} does not exist or cannot be accessed")
     with open(sample_path, "rb") as f:
         taste = f.read(8)
     return taste
 
 
 def is_runtime_ida():
     try:
         import idc
     except ImportError:
         return False
     else:
         return True
 
 
-def assert_never(value: NoReturn) -> NoReturn:
+def assert_never(value) -> NoReturn:
     assert False, f"Unhandled value: {value} ({type(value).__name__})"
 
 
 def get_format_from_extension(sample: str) -> str:
     if sample.endswith(EXTENSIONS_SHELLCODE_32):
         return FORMAT_SC32
     elif sample.endswith(EXTENSIONS_SHELLCODE_64):
```

### Comparing `flare-capa-5.0.0/capa/ida/helpers.py` & `flare-capa-5.1.0/capa/ida/helpers.py`

 * *Files 0% similar despite different names*

```diff
@@ -41,15 +41,15 @@
 
 CAPA_NETNODE = f"$ com.mandiant.capa.v{capa.version.__version__}"
 NETNODE_RESULTS = "results"
 NETNODE_RULES_CACHE_ID = "rules-cache-id"
 
 
 def inform_user_ida_ui(message):
-    idaapi.info("%s. Please refer to IDA Output window for more information." % message)
+    idaapi.info(f"{message}. Please refer to IDA Output window for more information.")
 
 
 def is_supported_ida_version():
     version = float(idaapi.get_kernel_version())
     if version < 7.4 or version >= 9:
         warning_msg = "This plugin does not support your IDA Pro version"
         logger.warning(warning_msg)
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/__init__.py` & `flare-capa-5.1.0/capa/ida/plugin/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -34,14 +34,20 @@
         """initialize plugin"""
         self.form = None
 
     def init(self):
         """called when IDA is loading the plugin"""
         logging.basicConfig(level=logging.INFO)
 
+        # do not load plugin unless hosted in idaq (IDA Qt)
+        if not idaapi.is_idaq():
+            # note: it does not appear that IDA calls "init" by default when hosted in idat; we keep this
+            # check here for good measure
+            return idaapi.PLUGIN_SKIP
+
         import capa.ida.helpers
 
         # do not load plugin if IDA version/file type not supported
         if not capa.ida.helpers.is_supported_ida_version():
             return idaapi.PLUGIN_SKIP
         if not capa.ida.helpers.is_supported_file_type():
             return idaapi.PLUGIN_SKIP
@@ -57,15 +63,24 @@
         """
         called when IDA is running the plugin as a script
 
         args:
           arg (int): bitflag. Setting LSB enables automatic analysis upon
           loading. The other bits are currently undefined. See `form.Options`.
         """
-        self.form = CapaExplorerForm(self.PLUGIN_NAME, arg)
+        if not self.form:
+            self.form = CapaExplorerForm(self.PLUGIN_NAME, arg)
+        else:
+            widget = idaapi.find_widget(self.form.form_title)
+            if widget:
+                idaapi.activate_widget(widget, True)
+            else:
+                self.form.Show()
+                self.form.load_capa_results(False, True)
+
         return True
 
 
 # set the capa plugin icon.
 #
 # TL;DR: temporarily install a UI hook set the icon.
 #
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/cache.py` & `flare-capa-5.1.0/capa/ida/plugin/cache.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/ida/plugin/capa_explorer.py` & `flare-capa-5.1.0/capa/ida/plugin/capa_explorer.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/ida/plugin/error.py` & `flare-capa-5.1.0/capa/ida/plugin/error.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/ida/plugin/extractor.py` & `flare-capa-5.1.0/capa/ida/plugin/extractor.py`

 * *Files 7% similar despite different names*

```diff
@@ -22,23 +22,23 @@
     def update(self, text):
         """emit progress update
 
         check if user cancelled action, raise exception for parent function to catch
         """
         if ida_kernwin.user_cancelled():
             raise UserCancelledError("user cancelled")
-        self.progress.emit("extracting features from %s" % text)
+        self.progress.emit(f"extracting features from {text}")
 
 
 class CapaExplorerFeatureExtractor(IdaFeatureExtractor):
     """subclass the IdaFeatureExtractor
 
     track progress during feature extraction, also allow user to cancel feature extraction
     """
 
     def __init__(self):
         super().__init__()
         self.indicator = CapaExplorerProgressIndicator()
 
     def extract_function_features(self, fh: FunctionHandle):
-        self.indicator.update("function at 0x%X" % fh.inner.start_ea)
+        self.indicator.update(f"function at {hex(fh.inner.start_ea)}")
         return super().extract_function_features(fh)
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/form.py` & `flare-capa-5.1.0/capa/ida/plugin/form.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,15 +25,15 @@
 import capa.render.json
 import capa.features.common
 import capa.render.result_document
 import capa.features.extractors.ida.extractor
 from capa.rules import Rule
 from capa.engine import FeatureSet
 from capa.rules.cache import compute_ruleset_cache_identifier
-from capa.ida.plugin.icon import QICON
+from capa.ida.plugin.icon import ICON
 from capa.ida.plugin.view import (
     CapaExplorerQtreeView,
     CapaExplorerRulegenEditor,
     CapaExplorerRulegenPreview,
     CapaExplorerRulegenFeatures,
 )
 from capa.ida.plugin.cache import CapaRuleGenFeatureCache
@@ -79,21 +79,21 @@
         save_file.write(data)
 
 
 def trim_function_name(f, max_length=25):
     """ """
     n = idaapi.get_name(f.start_ea)
     if len(n) > max_length:
-        n = "%s..." % n[:max_length]
+        n = f"{n[:max_length]}..."
     return n
 
 
 def update_wait_box(text):
     """update the IDA wait box"""
-    ida_kernwin.replace_wait_box("capa explorer...%s" % text)
+    ida_kernwin.replace_wait_box(f"capa explorer...{text}")
 
 
 class QLineEditClicked(QtWidgets.QLineEdit):
     def __init__(self, content, parent=None):
         """ """
         super().__init__(content, parent)
 
@@ -234,15 +234,19 @@
 
     def OnCreate(self, form):
         """called when plugin form is created
 
         load interface and install hooks but do not analyze database
         """
         self.parent = self.FormToPyQtWidget(form)
-        self.parent.setWindowIcon(QICON)
+
+        pixmap = QtGui.QPixmap()
+        pixmap.loadFromData(ICON)
+
+        self.parent.setWindowIcon(QtGui.QIcon(pixmap))
 
         self.load_interface()
         self.load_ida_hooks()
 
     def Show(self):
         """creates form if not already create, else brings plugin to front"""
         return super().Show(
@@ -622,25 +626,25 @@
         if not self.ensure_capa_settings_rule_path():
             return False
 
         rule_path: str = settings.user.get(CAPA_SETTINGS_RULE_PATH, "")
         try:
 
             def on_load_rule(_, i, total):
-                update_wait_box("loading capa rules from %s (%d of %d)" % (rule_path, i + 1, total))
+                update_wait_box(f"loading capa rules from {rule_path} ({i+1} of {total})")
                 if ida_kernwin.user_cancelled():
                     raise UserCancelledError("user cancelled")
 
             return capa.main.get_rules([rule_path], on_load_rule=on_load_rule)
         except UserCancelledError:
             logger.info("User cancelled analysis.")
             return None
         except Exception as e:
             capa.ida.helpers.inform_user_ida_ui(
-                "Failed to load capa rules from %s" % settings.user[CAPA_SETTINGS_RULE_PATH]
+                f"Failed to load capa rules from {settings.user[CAPA_SETTINGS_RULE_PATH]}"
             )
 
             logger.error("Failed to load capa rules from %s (error: %s).", settings.user[CAPA_SETTINGS_RULE_PATH], e)
             logger.error(
                 "Make sure your file directory contains properly "
                 "formatted capa rules. You can download and extract the official rules from %s. "
                 "Or, for more details, see the rules documentation here: %s",
@@ -683,18 +687,17 @@
 
                     if ida_kernwin.user_cancelled():
                         logger.info("User cancelled analysis.")
                         return False
 
                     update_wait_box("verifying cached results")
 
-                    view_status_rules: str = "%s (%d rules)" % (
-                        settings.user[CAPA_SETTINGS_RULE_PATH],
-                        self.program_analysis_ruleset_cache.source_rule_count,
-                    )
+                    count_source_rules = self.program_analysis_ruleset_cache.source_rule_count
+                    user_settings = settings.user[CAPA_SETTINGS_RULE_PATH]
+                    view_status_rules: str = f"{user_settings} ({count_source_rules} rules)"
 
                     # warn user about potentially outdated rules, depending on the use-case this may be expected
                     if (
                         compute_ruleset_cache_identifier(self.program_analysis_ruleset_cache)
                         != capa.ida.helpers.load_rules_cache_id()
                     ):
                         # expand items and resize columns, otherwise view looks incomplete until user closes the popup
@@ -702,30 +705,28 @@
 
                         capa.ida.helpers.inform_user_ida_ui("Cached results were generated using different capas rules")
                         logger.warning(
                             "capa is showing you cached results from a previous analysis run. Your rules have changed since and you should reanalyze the program to see new results."
                         )
                         view_status_rules = "no rules matched for cache"
 
-                    new_view_status = "capa rules: %s, cached results (created %s)" % (
-                        view_status_rules,
-                        self.resdoc_cache.meta.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
-                    )
+                    cached_results_time = self.resdoc_cache.meta.timestamp.strftime("%Y-%m-%d %H:%M:%S")
+                    new_view_status = f"capa rules: {view_status_rules}, cached results (created {cached_results_time})"
                 except Exception as e:
                     logger.error("Failed to load cached capa results (error: %s).", e, exc_info=True)
                     return False
             else:
                 # load results from fresh anlaysis
                 self.resdoc_cache = None
                 self.process_total = 0
                 self.process_count = 1
 
                 def slot_progress_feature_extraction(text):
                     """slot function to handle feature extraction progress updates"""
-                    update_wait_box("%s (%d of %d)" % (text, self.process_count, self.process_total))
+                    update_wait_box(f"{text} ({self.process_count} of {self.process_total})")
                     self.process_count += 1
 
                 update_wait_box("initializing feature extractor")
 
                 try:
                     extractor = CapaExplorerFeatureExtractor()
                     extractor.indicator.progress.connect(slot_progress_feature_extraction)
@@ -835,20 +836,17 @@
                     capa.ida.helpers.save_cached_results(self.resdoc_cache)
                     ruleset_id = compute_ruleset_cache_identifier(ruleset)
                     capa.ida.helpers.save_rules_cache_id(ruleset_id)
                     logger.info("Saved cached results to database")
                 except Exception as e:
                     logger.error("Failed to save results to database (error: %s)", e, exc_info=True)
                     return False
-
-                new_view_status = "capa rules: %s (%d rules)" % (
-                    settings.user[CAPA_SETTINGS_RULE_PATH],
-                    self.program_analysis_ruleset_cache.source_rule_count,
-                )
-
+                user_settings = settings.user[CAPA_SETTINGS_RULE_PATH]
+                count_source_rules = self.program_analysis_ruleset_cache.source_rule_count
+                new_view_status = f"capa rules: {user_settings} ({count_source_rules} rules)"
         # regardless of new analysis, render results - e.g. we may only want to render results after checking
         # show results by function
 
         if ida_kernwin.user_cancelled():
             logger.info("User cancelled analysis.")
             return False
 
@@ -1086,15 +1084,15 @@
                 settings.user.get(CAPA_SETTINGS_RULEGEN_AUTHOR, "<insert_author>"),
                 settings.user.get(CAPA_SETTINGS_RULEGEN_SCOPE, "function"),
             )
 
             self.view_rulegen_features.load_features(all_file_features, all_function_features)
 
             self.set_view_status_label(
-                "capa rules: %s (%d rules)" % (settings.user[CAPA_SETTINGS_RULE_PATH], ruleset.source_rule_count)
+                f"capa rules: {settings.user[CAPA_SETTINGS_RULE_PATH]} ({settings.user[CAPA_SETTINGS_RULE_PATH]} rules)"
             )
         except Exception as e:
             logger.error("Failed to render views (error: %s)", e, exc_info=True)
             return False
 
         return True
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/hooks.py` & `flare-capa-5.1.0/capa/ida/plugin/hooks.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/ida/plugin/icon.py` & `flare-capa-5.1.0/capa/ida/plugin/icon.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,13 +1,7 @@
 import base64
 
-from PyQt5 import QtGui
-
 # this is just `capa/.github/icon.png`.
 # embed it in source so we don't have to figure out how to package into pypi release.
 ICON = base64.b64decode(
     "iVBORw0KGgoAAAANSUhEUgAAAIcAAACJCAYAAAAG7St6AAAACXBIWXMAAAsSAAALEgHS3X78AAAZYklEQVR4nO1de3gUVZY/HR4hMQkhoAhBeYgxOCNE2SE4LBJeDg/XgI9lnI0Q9RNnQhTizI6Ku7PO+ELX/dAx5g+HccDJrs6qEFTQGVGiuOPA6CA4StugBAjykEceEAya9H6/SlWoVN+qurfura4G+/d9fqa7q6uLrl+fc+45v3NuKBqNUhJJsJCS/FaSsEOSHEnYIkmOJGyRJEcStkiSIwlbJMnBgbzKcHbCX6QPSC5lHZBXGS4lot/pRzQS0aJIef7yhLxYH3BGkcN0M1cQ0X2R8vw6iXMNIaKdlqebIuX5veWv9PTAGeNW8irDRaZf+Tzc2LzK8CyJUz7OeC5rcdXK5qVV1aUS5z1tcCbFHPdZn+hO7X+Y+dSfZ4ieKK8yDNdRzHrto2j/DBvinHE4I9yKHjAetXt9AB37wz7K+HGkPL/B5TxF+o0f5XTc9SmfUD9qubSirORDmetOdHQ/Q/4dju5jH2XMCVF0Zl5l+CUiqiGihkh5fq0eV+C/Iv0cjqQwsLr9IvpB6LNfEdHVKv8RiYbT3nLoVgO/4MHx/Nye1EZDQg23vrpg3DLe9+RVhu/TiTgBHIuU58vERL7jTCBHjTk+yM3qQfeO70/bvvyKntx0yPfPP4u+fuU49fhFpDzf1sU4uKuJsGC+X6RHnLbk0C1GTOD4yJQBNFtfbYYPtdLVz1tXo+4Y0a8X3Tv+HO24BzccpG2HvuJ52xYiwo2u0y2Z4bJs3dXQUANNC+1YXVFWkpAWJHBy6KYWNxrBYh1Pkkn/JS5nuZIP5udRZs9Ti7BV4Ua6a90+7usBMaqvOb/zHHubv6bi5+uoqbVN4F/Fh4HUTMUpn+LYiRVlJQlnQQINSPWA8D8szyGH8HikPL+GcSxIUar77BjApZiJAcCKbNzbQiu3NbpeT1ZqN6qamdvlHLmZPWjeqD5+u6hFutVJKAS9WmGZU9z4CXmVYfy9SzfTTDJYMSizB/N5xCBZPbvR8i1HbN9bmJuuHZfLOMc1I3r7Qo5DlG78mZC1m6DJUeDy+mCRVQhcAguwBIvHn0O3F/bTAlXt2LN7xVgZO4AwiGVE3BMPTlI32hnN1mKPRETQ5PBc+2BhyrAMx9dBhjG56Y7H2AHuCe/dtLeFtn3ZqrkqzkDVEVuj/UEOtx9JIAg0INWD0c6YA2Yd/n3dzmP05MZDXF8+3AHM/pRhmVyWADe36WR7pwVBwLm36WvmsbBEmakpnZ+DmCS/X2rn680n22nd580aUdZ9fiwmaEUMBFdX7/AZwLjQHhoZOjC7oqykxvagABA0OZbrRTIN1pXGQxsO2sYJIETpqJwuN8sKLGVx44xfudMNEgGIAuKMGZSu/W1cM0gNsiC+wfUZ1wYSjX464vgJs1LCHzxaNusflFygIgRNjjpzTBEpz485Bl/43ev2ab9K/BKvye9NpQU5tlbCuEGsX7JfAFE6rFcGM6AFbly1WyOpHZBxvSR08JnnFky8JS4XzYHAyKHnKtabn6uefT4zJmjW3YBdvABXsTLcGFdC2AFEKS3oE+PmnKygGZnU+j/NlLrArUgYDwRJjg+tmUNzdpMHSHD9etMhZe6itT5M7SeaKHXQCEpJy5Q6F+ITWLl5BX00ayKSTEuhaEs7hV7Qi4S1BlH0H9QsI2Gov6Y0qDcjEHJYA1EDt4/pp/3nBtWkAL586WFqqH1W+xvE6F/yMGWMnKzk3HA5+Hc1t7ZTyardSqxb+4lmOvrW7z47/FrVcCUXyUDcyWHRZXYBvsQlkwfYvhfxxIMbDiglBdC0cRUdqF4c8/wFj26StiBmgCD4NyKGcoo/eLB7yWz6+sheeuyxqptgQSrKSpRbkLgqwXSLwSSGE2CSEdCVralXTgygYf2zzOePrl+h9HOQZYVrMZbeXnGg+h5q3RvWrIf+ffoieo5LEoxHYWXnUvCF+lnXOLF9k/ZFswA302fiPKXWAy5FJtMKIjdt7EiHZA+/zHjalySaEnLkVYYLTGqqWkbJ2jEFzgpEYS1UmF83HF5baXsEfplNf1lF2RPn+noNvIAbOfzaqestGFtk/OmLIl6aHIwYgqtIRnpEj+WrNZGFpWnZ2r2+L0thNU7s+KvjMUdrVyQMOY6srTRciYb+fXOMP9/24/NUxBxDrE8gWYUb7wQ7YmAloiqidwMCUTd8c+QLruP8BqyG4U4YOD1iDqS0F+sqKrgG6CiQoDIHknbEuPvNfVy6CxVw+bK7AK4nq3B2XK7LDse3vOn0si+5DhWWo4tIxShUkV7qRpC5fu4FWlyBCD0RiEG6ieYFrMexrY43x3ewrNfO+npfP1aaHLpAdrXxGClsFhBwVs3IpfdvvTBwYmiBJqfVMNCgeFkrCtaKqm77J75+pqo8R+c3jeonklW8iDcxyGP+AoErAtgggLQ+Cwe3vkN7DjeRX0tZVeToIsvHEhTxhhuQv4g3MWA1jDS5KI56fJ/8NTfZvvbCmldJTyMohxJyWHs2sNK42yXRg1VJPPpKrIDVMC8HRXB865taIJtIqN/4Gr25JVy8tKo6ZtUoCyXk0JNgXYDkld3NhwgH/SBBQHZZKhLIqgKqxE54/fdP0HuR3cqXs6rcCpO1IIfVvUCbcZcu3ok3QAysPGSAQDbe1gPpe6cUftuJY7Ty6YcnfO+GO3+r9HMVnYfp81jJMF5tqB9wSpWLwK5Q5yfc5AMgyPvPL72593ev2J1z5a3/qOJSVJGDOczkkckDuqihkBbnUUP5ARVWwwDO5TVu8YqzRk7hu7aPN5x39I1lG1L7D2vJGDl5c+Zl02v7FN24yMvHSpMjrzK8iFX4QcLLKuu76021fR8iQAFNFTShTZzzHrAc3XMGch9/8uDOtOMfvVVwbPPrExrerl7a6/zvHO077SdCkwikyKE3M8dM1CGtzeCcLo+fVKzcEgFPgU0UXpfDMug7o9zzu1v3fJKdFW2pEnmPZ3LoxKhlWQ2IWcwqbASlK7bYDt7xHapiDTM6sqzxLcihvpOaG6vQ58Xk0SNnLK2qrl1aVc3VfumJHCZiMMU7VtEOrEZQqnCsLFRbDQN+kM4NZ197j6f3dUvLoO8M6k+6pIJr5IMwOXRVV4xy3ABiDavViHcW1Aw/8xJBlPPTLhxDacO/J/y+aTcuND/kmmXmWrLXrUQpr6qrdFSfLo+DyIIaECnLewWWtfEu5yP2qP/1PI4jO/DdGXNp8qhOd9TIO+jO0XLomU+4j6VEtNCNGGgNNK9QOnpJ+YtwqhGPbCaqpfEuyIlYD7iTayddYX6Ke4aqm+VgBpwQ9LA62pH0MgPuJKhYAwFjvDQYiD0GLYzv6iV74jyuWGrAyPHUO61TIvFLkWZtN3LUWWMLWIfFlmWqHYKMNWQKbKIwyvn4RccLRt7DLbE3alSnQr1RdLiuW0Aac7Jth1o1d+EGFNeCSpPLlOW9IgidaQZH1jQjLc34s6airESo/9aNHDX6lLxOwE2UrNztSpAgrcaxrevint4OoiAnGAgLR+aO5EADb6Q8v6AXfbPH/DwsghtB/O43cUIQ+QcKoJyfOihfJKUu3LXPlec4N3Tsqh7U3iWyNAgC92EFchtBuRSVBTbxz66Ju8Vycy0yImQucvxpwditX1NKzM9CI8iqWIJsOo2thmzrY7wLcm5BsIwIWSRDylQaIQZ54/Ouv5agXApWDLJWY+CtcuRCIBxP65HuQg4ZETI3OZxmexdaSvOYthcEZK0GEkv4JWYVep82He9yPiydWzHulbe0AUrCImTR2gqzJ9Oa/Aoi3lBRljdK4jkSpXEKYFmLwNQJO2pfpI/rDwiLkJUowcyFtqDiDdm2Afz6DP/dIyfXU3HLQLwLcqm5zgJkYPnj99H/hevio+cwYLUaTRwJMtVAfuG4ZKrc2kkvI6yhOC+n3SwH6RrTmmWPTL949oL/5D2vKDlixitY540bw1/jCdn8AnIF1oQSrIiMsCae/bXd++ZyHQeCbKup+ln6kEuael9+nesmQtzkYPWmJAJUlOX7FLHL37JzOeLVXws3KIITu/6e2fSXl26BrtTpbSKWg1nqtYqItzGSYn5CVjiMaD9rLDsNDWsiIuq1Isj+Wh5AVzrnziUP2h3KRQ6T4McVzXEs0asosGUXzXVMfNlZFV7EK/bwGkCH2tsWQ1fKeo3Xcixn6TrQsIStKYKCirK8ndUwvy6TNYX1SLT+WgMQAhXmafqtCaxlris59JlfMRvwQmG++odDaMpQ520s/ISs1UCyy81fgxiwLjIIor/WDYMKp1Ppoi5dJTHksBX7mHpSFlpfEx1D7QdUdJ3xJrtgPY689pTnz0HAjM8SDRz9QHpuHt0wd76hRDfQyNpjjmk59GGydSxiIFUeNDFIUaqc92bhOJmUOgXUX2tFz5wB9K8VP7cSY4Vdaj3GcuhuJGYuuQFDCca7BZYfUFGWF01y4Zcvs2TGNeMzVQ68FcWNt/3UrCeFiKvUSYnOusOO+XdDCcbScZDDPmsqIbt8NafKeSGbUve7IOfmYhFjmCwGNlYscmtRYJHDVTGEwho288U8L+v8DfM0QT+gosDmNbklm1L3s5xvN6LbwPUzrzI/nMWjJ2XdyeVW3agdoBPFoHcz3IbTykI21mClynkBayOTFOtol1gn+Q2IA7HGeX2zjPet8NzUZOhGR4f2PXNR6LDrCeBmzFrSEQ57rskCU/VkrYZsd1oiFuTspg0aOOfCLpUP5lQEFmx9wJjQ3p9OCu3cUhz6VNt/zAnmYpu1SqsSDbVyPhvBIHZBkAE0mzJBpR/lfKdpg0B237ONP3eJ7MtiSw74pIqykoKBoebZPwh99ooTQcz1FGg7/HAtKgpssBqyqwUVSTHV1qOFv34jtCW6a/SI9rn/WnD11YNDjf9ud4xVM+qHa1GRZVS1+4Fbyt0NsB4qC3JuwagJQjPSuZcWaxZ8/4Ge1PYB6zWrLNDrrs92UNH3ypMq54WKpJhK69Fav83x9YP13ubmC607T1K3B1jPY5yTeUlrFRzLQkmBTfGYBNnzqSrnw926JQQPb/+bp3MLkSNSnl+jN+TGwKwdVWk5VJTlDVW5SsgqxUiREJmHYFCAvfzeZhJtT/CSsWKuka1xh8wGd2YgGyprNbIlVyj255WLYVT01/Janz+vfY4aWr6aJHJuL5vx1LK0pNi/3YypwzK0bcNlcVRy+Uq6XE+FZC8lPYv6Ti/vFPTCtWA/WhnyItDGHrZewRuLnTyyj555cWVmdnov1FO4RmEr2akJuY3bC7sOieuwHHJzR1X1vaocGAeV+6A7VnS6KSxrgyrngxgixMQQ/YdampfxjmNQUgi5Y0y/mCotHsu6lqC65d1gzivILmtJopB43EMq/tBH73Z7L7KbK2HkhRwxQU1uJjsrOpUxGooX+FUE1S0vAiVaDw8FOZnl/eYtmyELdCWIF3LECEOwPQZ2Z7LO64AoyGu2NOhts5xgHXuQLSlC9lLOlxlQ0ytdW02iPdJx9SJEDl0IFCMDQxIMW4mPfjqiVWnNJJlnGT3JAz/GUatC/5KHYjrM8FhG60EelrVeXS7GTt48c6rx0LGjgDsgdZpzbgaIgm0zjKFypQU52mhrkamCQW2X5QYQwy75hdhDhtBGQY4nuSYyagLl+vNHjqPRowpoYN8+5tI9uWl3RCxHjdscUgPYNsPImCIwFbEeKvpe/UDO9AWON062AYoErAHvcbAS9yy+n8quL9ZaECzEwNhJxx87b1NTkcg25KRvAmgA1oM39khEGT8CTh4dh2wDFE85n8floh9l5vx7Nfdh0oxCGvgEEU0koqFuxCABtyI8+AMZUwSp6GsxrIfbqOt4jKMWBYjBm6SCazn8WqVUUgzLWicLtb/afTD++Gvnm8dZA7/E2FDVoyYNeGqifnDDgc7gFNbDTQiUCPJ9M84aOVkoe6lC6+FUkMP34xZrDC+6jq6+/FLjIepgs2ElRIlBAuRYpPc3CAHVWgSnpMce947vb/v2IPYvcQKKaud6SGurSIqxYgp8P7BKToA7+ZerppmPWCQyztoKLnJEyvPrIuX5pcWhT2shGxwX2kM8+lLSg1OjYgsXY5c1VVFgUwUQA7PMvajGVCTFYD2sulC4E7fvZ2jhNHOM8QRvDcUOQnmOgaHmmwaGmleMDB2gSaGddHPKZsLfbjDvIYtWSlZw2uaig4wXsOLwSgwDsjPFyKILRSaUZwU34fKxxp+NIkJiOwiRA+LUirISJE7g1CamUlvFuNCeFdNCOxxFyFruY9Mp97JkyoCYY2SFuyqAzx9461PS1wHrgZyI1/PAchkbDSNIP8ARhAKmpqXlXmIMK0LRaFT2HIQ9wz6N9l32VnTotU7HRcpPRdAPbTjI3EZUVB3V8eUtFnoPC7iRg+54lmu+luj1fXOYX7ORkpbV5Rp2L5nNpRHNHn4Z/aKiwnh4KW9vihOUlOx1ll435amNv90d7X0z6xhrmyQyqLAoVpGQqGKrifNX5QS/iEG6FfGqXYXFEBAPd0IFMUjhpsMa1i0ovKUntX3Geq3pZFtM62TVzEFSvbWqNtzBpnp+EEMGWLaK5HxajnQmHZmzYr1AeWPrSer2M9bzWNZOXPEZsq2dxTnEH1Uzcz1XblWscJzqJUEBS/ovV4oto6H0ajyhdh6bcnI4iZANmLfkgBakevb5nggiKyFMVGJ4jaFeeusdcpuSIAK/WuJd7aF5S478fqnCBJGVECKTeSYRA9i2fiX+N5h3U2E3+EUOri4a85YcogSRmdGBJJXXzXv9giwxSG9B0LFIxWUGN55HhzYMZtVuWhVu1Aiyft4FrkGqTLe9SCEtXkC6XMVy3IQzgxykE+Sudfu03AdQfc35jgTx2m2P5FIiEQPB9Be/KZdSr5uBYXA6lAxtU5LnYMBTcQFJMeQ90OYw4uxU5tYcHQU68VqSUS9JFMD6ieYxzKouAwcOH6GWEy10Sd5w6yA4aSgnR15leIjdPvc8MPSodvAyV0umkOYH4EZErAWqraNnlNAPJ41jvMoU53FNZnKDH5ZD2VKKBdGyvpb9TBBieLEWcBW33bbQKvHbpa8IzSYU3ztWKbWqMqR+kEO64GMH0eWrkRYPmhiaFmNtpXBDOIiBuaGmMrxWba0oKxHaWdorlBTerMirDDeYg6JMOkmZ1JG9a6ZUaqaens7LW4Qin+slvDD6Ubw0LcGV/Nv9j1vnhs4SGdskC18C0kh5fvb1T709ZwA1P59KbdCBdHkdBAlH+9LWaH+k27nOiWqtiDkOkhgypDAAHaiFGEUqyvAi8MVyGFhaVd1gWVbtMiXIhrRSt8HvRwdqJHEDfDXvKiWotDgIDNcnK5LGqmTJ/Y8aD+FKhsSbGOTjUlZDRVlJtt5yh2CpwTp8Hds4jAvtKc2hEz+vjQ5JszuPiCo9e0KJ8kEtTgAhUBlGe6Kq3t68sVPNDxcFQQzy23LwArWATdHc//0gOmAq6y2iSz/S5X7YkLdjAs8IZS5Gc2/1YWrZsUn72w/d65yFDxj7oGA0pK+rPyf4ajl4of8yrryi8v0/7aeMGIJ4GfvU0SBU08XiIN+BQNWwLN0sqiszQADoWnHzMZCNZ/aWKuSfd65xJimBsCwSghwG9lPGP6dQ9It2CnW6GBX7qhgwAtpEbdI2UH+4gXp3ZDuF5oaqRkLUVgxgtHY7hR41P5eoA1z8xLGWzrKBkmSWVySU5dBRY+z3ItJNnuhAQqtnWgb1TM+gky3HNFnfySPssVgmt1IQpPVIOHJEyvM/hJSQEngUAy+wJP3+jBtoQsHF5pxFJzZGdtEf16ykhh2n5oSeM/IK5rFBIBEth4ZEHcXAC8uQFDO26CWGhsK8wdmFeRVDNkZ2aUuTj7dHaOrYQvOxSbfCQGPD+meZmoRuPXrS9JLb6cKhwygrPZXCe/bTzvp6qtv+CR3c+k7Q162lvbHroqV8vkvvQGNO8VtaVY0pBvcV5g02j7lYHVR+w0BC5DmsGHb/+iW7Hi6+y7pK6ZWWTgsWLabcQewZMnsON9ELa17VRioGhVvuecxKDNchKQZ0kpA+8mJ5POsoLCQkObr3PrusrelQl6yXhRhb9BzAh3o6vkEP3vBf0cbIruIXn15i1lQKAbEC6XJ/EVhcSSPPPmqJjIQkRygUqrOqWG6av4guGTW6Ud/R0DGXjrT8e5Hdy1c+/fAEHoKADAUTi5lqqo/rD9BHkR304frVjmRhVFGVtCQGiYQjRygUQrp4p/m5q4rnbJ505VUvi5rai/5p/n9HXv3Nj+xed1ZYadil/18j6jNr3qC/r2WvoLD74p1zOz+K25UkMhKRHPC3601P3RSNRj2nkXsNuOCr1v2fx6wNHQLHx1lqKr2AWLTy3ffvf/e5J2Km74659scGyQKroqpGIpIjW0/8QIdaEY1GpVRPWWOKVzX/9eUYwbMlcBRSWOVNm7tt+x9/31mUsXS4r9DHVJz2SLilbDQabfA6g4yF7pk5z1vV8JYNeIUDx8jrz46Yc+fFD/5t8weLm44cpJ/M7TIH7LSOM8xIyIBUNXpfft2ytv3bf3S8bmsaMpC4mSoCx6VV1WgeWmp66u2KshLhyYuJim8FOehUzLDZ8rS0C8DKSO8wG6KvpE77WMPAt4Yc1HEjS/V538hErj7TbqZqfKvIkYQYEkrPkURiIUmOJGyRJEcStkiSIwk2iOj/ASgkysfS5t/gAAAAAElFTkSuQmCC"
 )
-
-pixmap = QtGui.QPixmap()
-pixmap.loadFromData(ICON)
-QICON = QtGui.QIcon(pixmap)
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/item.py` & `flare-capa-5.1.0/capa/ida/plugin/item.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,15 @@
         return display.split("(")[1].rstrip(")")
     except IndexError:
         return ""
 
 
 def ea_to_hex(ea):
     """convert effective address (ea) to hex for display"""
-    return "%08X" % ea
+    return f"{hex(ea)}"
 
 
 class CapaExplorerDataItem:
     """store data for CapaExplorerDataModel"""
 
     def __init__(self, parent: Optional["CapaExplorerDataItem"], data: List[str], can_check=True):
         """initialize item"""
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/model.py` & `flare-capa-5.1.0/capa/ida/plugin/model.py`

 * *Files 2% similar despite different names*

```diff
@@ -365,54 +365,54 @@
         @param doc: result doc
         """
 
         if isinstance(statement, rd.CompoundStatement):
             if statement.type != rd.CompoundStatementType.NOT:
                 display = statement.type
                 if statement.description:
-                    display += " (%s)" % statement.description
+                    display += f" ({statement.description})"
                 return CapaExplorerDefaultItem(parent, display)
         elif isinstance(statement, rd.CompoundStatement) and statement.type == rd.CompoundStatementType.NOT:
             # TODO: do we display 'not'
             pass
         elif isinstance(statement, rd.SomeStatement):
-            display = "%d or more" % statement.count
+            display = f"{statement.count} or more"
             if statement.description:
-                display += " (%s)" % statement.description
+                display += f" ({statement.description})"
             return CapaExplorerDefaultItem(parent, display)
         elif isinstance(statement, rd.RangeStatement):
             # `range` is a weird node, its almost a hybrid of statement + feature.
             # it is a specific feature repeated multiple times.
             # there's no additional logic in the feature part, just the existence of a feature.
             # so, we have to inline some of the feature rendering here.
-            display = "count(%s): " % self.capa_doc_feature_to_display(statement.child)
+            display = f"count({self.capa_doc_feature_to_display(statement.child)}): "
 
             if statement.max == statement.min:
-                display += "%d" % (statement.min)
+                display += f"{statement.min}"
             elif statement.min == 0:
-                display += "%d or fewer" % (statement.max)
+                display += f"{statement.max} or fewer"
             elif statement.max == (1 << 64 - 1):
-                display += "%d or more" % (statement.min)
+                display += f"{statement.min} or more"
             else:
-                display += "between %d and %d" % (statement.min, statement.max)
+                display += f"between {statement.min} and {statement.max}"
 
             if statement.description:
-                display += " (%s)" % statement.description
+                display += f" ({statement.description})"
 
             parent2 = CapaExplorerFeatureItem(parent, display=display)
 
             for location in locations:
                 # for each location render child node for range statement
                 self.render_capa_doc_feature(parent2, match, statement.child, location, doc)
 
             return parent2
         elif isinstance(statement, rd.SubscopeStatement):
             display = str(statement.scope)
             if statement.description:
-                display += " (%s)" % statement.description
+                display += f" ({statement.description})"
             return CapaExplorerSubscopeItem(parent, display)
         else:
             raise RuntimeError("unexpected match statement type: " + str(statement))
 
     def render_capa_doc_match(self, parent: CapaExplorerDataItem, match: rd.Match, doc: rd.ResultDocument):
         """render capa match read from doc
 
@@ -533,29 +533,29 @@
         @param feature: capa feature read from doc
         """
         key = feature.type
         value = feature.dict(by_alias=True).get(feature.type)
 
         if value:
             if isinstance(feature, frzf.StringFeature):
-                value = '"%s"' % capa.features.common.escape_string(value)
+                value = f'"{capa.features.common.escape_string(value)}"'
 
             if isinstance(feature, frzf.PropertyFeature) and feature.access is not None:
                 key = f"property/{feature.access}"
             elif isinstance(feature, frzf.OperandNumberFeature):
                 key = f"operand[{feature.index}].number"
             elif isinstance(feature, frzf.OperandOffsetFeature):
                 key = f"operand[{feature.index}].offset"
 
             if feature.description:
-                return "%s(%s = %s)" % (key, value, feature.description)
+                return f"{key}({value} = {feature.description})"
             else:
-                return "%s(%s)" % (key, value)
+                return f"{key}({value})"
         else:
-            return "%s" % key
+            return f"{key}"
 
     def render_capa_doc_feature_node(
         self,
         parent: CapaExplorerDataItem,
         match: rd.Match,
         feature: frzf.Feature,
         locations: List[Address],
@@ -665,15 +665,15 @@
         elif isinstance(feature, frzf.SectionFeature):
             # display byte preview
             return CapaExplorerByteViewItem(parent, display, location)
 
         elif isinstance(feature, frzf.StringFeature):
             # display string preview
             return CapaExplorerStringViewItem(
-                parent, display, location, '"%s"' % capa.features.common.escape_string(feature.string)
+                parent, display, location, f'"{capa.features.common.escape_string(feature.string)}"'
             )
 
         elif isinstance(
             feature,
             (
                 frzf.ImportFeature,
                 frzf.ExportFeature,
```

### Comparing `flare-capa-5.0.0/capa/ida/plugin/proxy.py` & `flare-capa-5.1.0/capa/ida/plugin/proxy.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/ida/plugin/view.py` & `flare-capa-5.1.0/capa/ida/plugin/view.py`

 * *Files 3% similar despite different names*

```diff
@@ -54,69 +54,63 @@
         # first, we need to grab the comment, if exists
         # next, we need to check for an embedded description
         feature, _, comment = feature.partition("#")
         m = re.search(r"- count\(([a-zA-Z]+)\((.+)\s+=\s+(.+)\)\):\s*(.+)", feature)
         if m:
             # reconstruct count without description
             feature, value, description, count = m.groups()
-            feature = "- count(%s(%s)): %s" % (feature, value, count)
+            feature = f"- count({feature}({value})): {count}"
     elif not feature.startswith("#"):
         feature, _, comment = feature.partition("#")
         feature, _, description = feature.partition("=")
 
     return map(lambda o: o.strip(), (feature, description, comment))
 
 
 def parse_node_for_feature(feature, description, comment, depth):
     """ """
     depth = (depth * 2) + 4
     display = ""
 
     if feature.startswith("#"):
-        display += "%s%s\n" % (" " * depth, feature)
+        display += f"{' '*depth}{feature}\n"
     elif description:
         if feature.startswith(("- and", "- or", "- optional", "- basic block", "- not", "- instruction:")):
-            display += "%s%s" % (" " * depth, feature)
+            display += f"{' '*depth}{feature}\n"
             if comment:
-                display += " # %s" % comment
-            display += "\n%s- description: %s\n" % (" " * (depth + 2), description)
+                display += f" # {comment}"
+            display += f"\n{' '*(depth+2)}- description: {description}\n"
         elif feature.startswith("- string"):
-            display += "%s%s" % (" " * depth, feature)
+            display += f"{' '*depth}{feature}\n"
             if comment:
-                display += " # %s" % comment
-            display += "\n%sdescription: %s\n" % (" " * (depth + 2), description)
+                display += f" # {comment}"
+            display += f"\n{' '*(depth+2)}description: {description}\n"
         elif feature.startswith("- count"):
             # count is weird, we need to format description based on feature type, so we parse with regex
             # assume format - count(<feature_name>(<feature_value>)): <count>
             m = re.search(r"- count\(([a-zA-Z]+)\((.+)\)\): (.+)", feature)
             if m:
                 name, value, count = m.groups()
                 if name in ("string",):
-                    display += "%s%s" % (" " * depth, feature)
+                    display += f"{' '*depth}{feature}"
                     if comment:
-                        display += " # %s" % comment
-                    display += "\n%sdescription: %s\n" % (" " * (depth + 2), description)
+                        display += f" # {comment}"
+                    display += f"\n{' '*(depth+2)}description: {description}\n"
                 else:
-                    display += "%s- count(%s(%s = %s)): %s" % (
-                        " " * depth,
-                        name,
-                        value,
-                        description,
-                        count,
-                    )
+                    display += f"{' '*depth}- count({name}({value} = {description})): {count}"
                     if comment:
-                        display += " # %s\n" % comment
+                        display += f" # {comment}\n"
         else:
-            display += "%s%s = %s" % (" " * depth, feature, description)
+            display += f"{' '*depth}{feature} = {description}"
             if comment:
-                display += " # %s\n" % comment
+                display += f" # {comment}\n"
     else:
-        display += "%s%s" % (" " * depth, feature)
+        display += f"{' '*depth}{feature}"
         if comment:
-            display += " # %s\n" % comment
+            display += f" # {comment}\n"
 
     return display if display.endswith("\n") else display + "\n"
 
 
 def iterate_tree(o):
     """ """
     itr = QtWidgets.QTreeWidgetItemIterator(o)
@@ -194,22 +188,22 @@
         metadata_default = [
             "# generated using capa explorer for IDA Pro",
             "rule:",
             "  meta:",
             "    name: <insert_name>",
             "    namespace: <insert_namespace>",
             "    authors:",
-            "      - %s" % author,
-            "    scope: %s" % scope,
+            f"      - {author}",
+            f"    scope: {scope}",
             "    references:",
             "      - <insert_references>",
             "    examples:",
-            "      - %s:0x%X" % (capa.ida.helpers.get_file_md5().upper(), ea)
+            f"      - {capa.ida.helpers.get_file_md5().upper()}:{hex(ea)}"
             if ea
-            else "      - %s" % (capa.ida.helpers.get_file_md5().upper()),
+            else f"      - {capa.ida.helpers.get_file_md5().upper()}",
             "  features:",
         ]
         self.setText("\n".join(metadata_default))
 
     def keyPressEvent(self, e):
         """intercept key press events"""
         if e.key() in (QtCore.Qt.Key_Tab, QtCore.Qt.Key_Backtab):
@@ -535,15 +529,15 @@
             ("optional", ("- optional:",), self.slot_nest_features),
             ("basic block", ("- basic block:",), self.slot_nest_features),
             ("instruction", ("- instruction:",), self.slot_nest_features),
         )
 
         # build submenu with modify actions
         sub_menu = build_context_menu(self.parent(), sub_actions)
-        sub_menu.setTitle("Nest feature%s" % ("" if len(tuple(self.get_features(selected=True))) == 1 else "s"))
+        sub_menu.setTitle(f"Nest feature{'' if len(tuple(self.get_features(selected=True))) == 1 else 's'}")
 
         # build main menu with submenu + main actions
         menu = build_context_menu(self.parent(), (sub_menu,) + actions)
 
         menu.exec_(self.viewport().mapToGlobal(pos))
 
     def load_custom_context_menu_expression(self, pos):
@@ -650,29 +644,29 @@
 
         # build feature counts
         counted = list(zip(Counter(features).keys(), Counter(features).values()))
 
         # single features
         for k, v in filter(lambda t: t[1] == 1, counted):
             if isinstance(k, (capa.features.common.String,)):
-                value = '"%s"' % capa.features.common.escape_string(k.get_value_str())
+                value = f'"{capa.features.common.escape_string(k.get_value_str())}"'
             else:
                 value = k.get_value_str()
-            self.new_feature_node(top_node, ("- %s: %s" % (k.name.lower(), value), ""))
+            self.new_feature_node(top_node, (f"- {k.name.lower()}: {value}", ""))
 
         # n > 1 features
         for k, v in filter(lambda t: t[1] > 1, counted):
             if k.value:
                 if isinstance(k, (capa.features.common.String,)):
-                    value = '"%s"' % capa.features.common.escape_string(k.get_value_str())
+                    value = f'"{capa.features.common.escape_string(k.get_value_str())}"'
                 else:
                     value = k.get_value_str()
-                display = "- count(%s(%s)): %d" % (k.name.lower(), value, v)
+                display = f"- count({k.name.lower()}({value})): {v}"
             else:
-                display = "- count(%s): %d" % (k.name.lower(), v)
+                display = f"- count({k.name.lower()}): {v}"
             self.new_feature_node(top_node, (display, ""))
 
         self.update_preview()
         expand_tree(self.invisibleRootItem())
         resize_columns_to_content(self.header())
 
     def make_child_node_from_feature(self, parent, feature):
@@ -876,15 +870,15 @@
             return
 
         if selected_items_count == 1:
             action_add_features_fmt = "Add feature"
             if isinstance(self.selectedItems()[0].data(0, 0x100), capa.features.common.Bytes):
                 actions.append(("Add n bytes...", (), self.slot_add_n_bytes_feature))
         else:
-            action_add_features_fmt = "Add %d features" % selected_items_count
+            action_add_features_fmt = f"Add {selected_items_count} features"
 
         actions.append((action_add_features_fmt, (), self.slot_add_selected_features))
 
         menu = build_context_menu(self.parent(), actions)
         menu.exec_(self.viewport().mapToGlobal(pos))
 
     def slot_item_double_clicked(self, o, column):
@@ -1025,25 +1019,25 @@
 
     def parse_features_for_tree(self, parent, features):
         """ """
         self.parent_items = {}
 
         def format_address(e):
             if isinstance(e, AbsoluteVirtualAddress):
-                return "%X" % int(e)
+                return f"{hex(int(e))}"
             else:
                 return ""
 
         def format_feature(feature):
             """ """
             name = feature.name.lower()
             value = feature.get_value_str()
             if isinstance(feature, (capa.features.common.String,)):
-                value = '"%s"' % capa.features.common.escape_string(value)
-            return "%s(%s)" % (name, value)
+                value = f'"{capa.features.common.escape_string(value)}"'
+            return f"{name}({value})"
 
         for feature, addrs in sorted(features.items(), key=lambda k: sorted(k[1])):
             if isinstance(feature, capa.features.basicblock.BasicBlock):
                 # filter basic blocks for now, we may want to add these back in some time
                 # in the future
                 continue
```

### Comparing `flare-capa-5.0.0/capa/main.py` & `flare-capa-5.1.0/capa/main.py`

 * *Files 5% similar despite different names*

```diff
@@ -54,29 +54,35 @@
     get_auto_format,
     log_unsupported_os_error,
     log_unsupported_arch_error,
     log_unsupported_format_error,
 )
 from capa.exceptions import UnsupportedOSError, UnsupportedArchError, UnsupportedFormatError, UnsupportedRuntimeError
 from capa.features.common import (
+    OS_AUTO,
+    OS_LINUX,
+    OS_MACOS,
     FORMAT_PE,
     FORMAT_ELF,
+    OS_WINDOWS,
     FORMAT_AUTO,
     FORMAT_SC32,
     FORMAT_SC64,
     FORMAT_DOTNET,
     FORMAT_FREEZE,
+    FORMAT_RESULT,
 )
 from capa.features.address import NO_ADDRESS, Address
 from capa.features.extractors.base_extractor import BBHandle, InsnHandle, FunctionHandle, FeatureExtractor
 
 RULES_PATH_DEFAULT_STRING = "(embedded rules)"
 SIGNATURES_PATH_DEFAULT_STRING = "(embedded signatures)"
 BACKEND_VIV = "vivisect"
 BACKEND_DOTNET = "dotnet"
+BACKEND_BINJA = "binja"
 
 E_MISSING_RULES = 10
 E_MISSING_FILE = 11
 E_INVALID_RULE = 12
 E_CORRUPT_FILE = 13
 E_FILE_LIMITATION = 14
 E_INVALID_SIG = 15
@@ -257,17 +263,17 @@
     pb = pbar(functions, desc="matching", unit=" functions", postfix="skipped 0 library functions")
     for f in pb:
         if extractor.is_library_function(f.address):
             function_name = extractor.get_function_name(f.address)
             logger.debug("skipping library function 0x%x (%s)", f.address, function_name)
             meta["library_functions"][f.address] = function_name
             n_libs = len(meta["library_functions"])
-            percentage = 100 * (n_libs / n_funcs)
+            percentage = round(100 * (n_libs / n_funcs))
             if isinstance(pb, tqdm.tqdm):
-                pb.set_postfix_str("skipped %d library functions (%d%%)" % (n_libs, percentage))
+                pb.set_postfix_str(f"skipped {n_libs} library functions ({percentage}%)")
             continue
 
         function_matches, bb_matches, insn_matches, feature_count = find_code_capabilities(ruleset, extractor, f)
         meta["feature_counts"]["functions"][f.address] = feature_count
         logger.debug("analyzed function 0x%x and extracted %d features", f.address, feature_count)
 
         for rule_name, res in function_matches.items():
@@ -393,16 +399,16 @@
 def get_meta_str(vw):
     """
     Return workspace meta information string
     """
     meta = []
     for k in ["Format", "Platform", "Architecture"]:
         if k in vw.metadata:
-            meta.append("%s: %s" % (k.lower(), vw.metadata[k]))
-    return "%s, number of functions: %d" % (", ".join(meta), len(vw.getFunctions()))
+            meta.append(f"{k.lower()}: {vw.metadata[k]}")
+    return f"{', '.join(meta)}, number of functions: {len(vw.getFunctions())}"
 
 
 def is_running_standalone() -> bool:
     """
     are we running from a PyInstaller'd executable?
     if so, then we'll be able to access `sys._MEIPASS` for the packaged resources.
     """
@@ -486,37 +492,70 @@
 
     logger.debug("%s", get_meta_str(vw))
     return vw
 
 
 # TODO get_extractors -> List[FeatureExtractor]?
 def get_extractor(
-    path: str, format_: str, backend: str, sigpaths: List[str], should_save_workspace=False, disable_progress=False
+    path: str,
+    format_: str,
+    os_: str,
+    backend: str,
+    sigpaths: List[str],
+    should_save_workspace=False,
+    disable_progress=False,
 ) -> FeatureExtractor:
     """
     raises:
       UnsupportedFormatError
       UnsupportedArchError
       UnsupportedOSError
     """
     if format_ not in (FORMAT_SC32, FORMAT_SC64):
         if not is_supported_format(path):
             raise UnsupportedFormatError()
 
         if not is_supported_arch(path):
             raise UnsupportedArchError()
 
-        if not is_supported_os(path):
+        if os_ == OS_AUTO and not is_supported_os(path):
             raise UnsupportedOSError()
 
     if format_ == FORMAT_DOTNET:
         import capa.features.extractors.dnfile.extractor
 
         return capa.features.extractors.dnfile.extractor.DnfileFeatureExtractor(path)
 
+    elif backend == BACKEND_BINJA:
+        from capa.features.extractors.binja.find_binja_api import find_binja_path
+
+        # When we are running as a standalone executable, we cannot directly import binaryninja
+        # We need to fist find the binja API installation path and add it into sys.path
+        if is_running_standalone():
+            bn_api = find_binja_path()
+            if os.path.exists(bn_api):
+                sys.path.append(bn_api)
+
+        try:
+            from binaryninja import BinaryView, BinaryViewType
+        except ImportError:
+            raise RuntimeError(
+                "Cannot import binaryninja module. Please install the Binary Ninja Python API first: "
+                "https://docs.binary.ninja/dev/batch.html#install-the-api)."
+            )
+
+        import capa.features.extractors.binja.extractor
+
+        with halo.Halo(text="analyzing program", spinner="simpleDots", stream=sys.stderr, enabled=not disable_progress):
+            bv: BinaryView = BinaryViewType.get_view_of_file(path)
+            if bv is None:
+                raise RuntimeError(f"Binary Ninja cannot open file {path}")
+
+        return capa.features.extractors.binja.extractor.BinjaFeatureExtractor(bv)
+
     # default to use vivisect backend
     else:
         import capa.features.extractors.viv.extractor
 
         with halo.Halo(text="analyzing program", spinner="simpleDots", stream=sys.stderr, enabled=not disable_progress):
             vw = get_workspace(path, format_, sigpaths)
 
@@ -526,15 +565,15 @@
                     vw.saveWorkspace()
                 except IOError:
                     # see #168 for discussion around how to handle non-writable directories
                     logger.info("source directory is not writable, won't save intermediate workspace")
             else:
                 logger.debug("CAPA_SAVE_WORKSPACE unset, not saving workspace")
 
-        return capa.features.extractors.viv.extractor.VivisectFeatureExtractor(vw, path)
+        return capa.features.extractors.viv.extractor.VivisectFeatureExtractor(vw, path, os_)
 
 
 def get_file_extractors(sample: str, format_: str) -> List[FeatureExtractor]:
     file_extractors: List[FeatureExtractor] = list()
 
     if format_ == FORMAT_PE:
         file_extractors.append(capa.features.extractors.pefile.PefileFeatureExtractor(sample))
@@ -565,15 +604,15 @@
 def collect_rule_file_paths(rule_paths: List[str]) -> List[str]:
     """
     collect all rule file paths, including those in subdirectories.
     """
     rule_file_paths = []
     for rule_path in rule_paths:
         if not os.path.exists(rule_path):
-            raise IOError("rule path %s does not exist or cannot be accessed" % rule_path)
+            raise IOError(f"rule path {rule_path} does not exist or cannot be accessed")
 
         if os.path.isfile(rule_path):
             rule_file_paths.append(rule_path)
         elif os.path.isdir(rule_path):
             logger.debug("reading rules from directory %s", rule_path)
             for root, _, files in os.walk(rule_path):
                 if ".git" in root:
@@ -656,15 +695,15 @@
     capa.rules.cache.cache_ruleset(cache_dir, ruleset)
 
     return ruleset
 
 
 def get_signatures(sigs_path):
     if not os.path.exists(sigs_path):
-        raise IOError("signatures path %s does not exist or cannot be accessed" % sigs_path)
+        raise IOError(f"signatures path {sigs_path} does not exist or cannot be accessed")
 
     paths = []
     if os.path.isfile(sigs_path):
         paths.append(sigs_path)
     elif os.path.isdir(sigs_path):
         logger.debug("reading signatures from directory %s", os.path.abspath(os.path.normpath(sigs_path)))
         for root, _, files in os.walk(sigs_path):
@@ -685,14 +724,16 @@
 
     return paths
 
 
 def collect_metadata(
     argv: List[str],
     sample_path: str,
+    format_: str,
+    os_: str,
     rules_path: List[str],
     extractor: capa.features.extractors.base_extractor.FeatureExtractor,
 ):
     md5 = hashlib.md5()
     sha1 = hashlib.sha1()
     sha256 = hashlib.sha256()
 
@@ -702,17 +743,17 @@
     md5.update(buf)
     sha1.update(buf)
     sha256.update(buf)
 
     if rules_path != [RULES_PATH_DEFAULT_STRING]:
         rules_path = [os.path.abspath(os.path.normpath(r)) for r in rules_path]
 
-    format_ = get_format(sample_path)
+    format_ = get_format(sample_path) if format_ == FORMAT_AUTO else format_
     arch = get_arch(sample_path)
-    os_ = get_os(sample_path)
+    os_ = get_os(sample_path) if os_ == OS_AUTO else os_
 
     return {
         "timestamp": datetime.datetime.now().isoformat(),
         "version": capa.version.__version__,
         "argv": argv,
         "sample": {
             "md5": md5.hexdigest(),
@@ -786,14 +827,15 @@
     see `handle_common_args` to do common configuration.
 
     args:
       parser (argparse.ArgumentParser): a parser to update in place, adding common arguments.
       wanted (Set[str]): collection of arguments to opt-into, including:
         - "sample": required positional argument to input file.
         - "format": flag to override file format.
+        - "os": flag to override file operating system.
         - "backend": flag to override analysis backend.
         - "rules": flag to override path to capa rules.
         - "tag": flag to override/specify which rules to match.
     """
     if wanted is None:
         wanted = set()
 
@@ -819,14 +861,15 @@
     )
 
     #
     # arguments that may be opted into:
     #
     #   - sample
     #   - format
+    #   - os
     #   - rules
     #   - tag
     #
 
     if "sample" in wanted:
         parser.add_argument(
             "sample",
@@ -840,32 +883,47 @@
             (FORMAT_PE, "Windows PE file"),
             (FORMAT_DOTNET, ".NET PE file"),
             (FORMAT_ELF, "Executable and Linkable Format"),
             (FORMAT_SC32, "32-bit shellcode"),
             (FORMAT_SC64, "64-bit shellcode"),
             (FORMAT_FREEZE, "features previously frozen by capa"),
         ]
-        format_help = ", ".join(["%s: %s" % (f[0], f[1]) for f in formats])
+        format_help = ", ".join([f"{f[0]}: {f[1]}" for f in formats])
         parser.add_argument(
             "-f",
             "--format",
             choices=[f[0] for f in formats],
             default=FORMAT_AUTO,
-            help="select sample format, %s" % format_help,
+            help=f"select sample format, {format_help}",
         )
 
-        if "backend" in wanted:
-            parser.add_argument(
-                "-b",
-                "--backend",
-                type=str,
-                help="select the backend to use",
-                choices=(BACKEND_VIV,),
-                default=BACKEND_VIV,
-            )
+    if "backend" in wanted:
+        parser.add_argument(
+            "-b",
+            "--backend",
+            type=str,
+            help="select the backend to use",
+            choices=(BACKEND_VIV, BACKEND_BINJA),
+            default=BACKEND_VIV,
+        )
+
+    if "os" in wanted:
+        oses = [
+            (OS_AUTO, "detect OS automatically - default"),
+            (OS_LINUX,),
+            (OS_MACOS,),
+            (OS_WINDOWS,),
+        ]
+        os_help = ", ".join([f"{o[0]} ({o[1]})" if len(o) == 2 else o[0] for o in oses])
+        parser.add_argument(
+            "--os",
+            choices=[o[0] for o in oses],
+            default=OS_AUTO,
+            help=f"select sample OS: {os_help}",
+        )
 
     if "rules" in wanted:
         parser.add_argument(
             "-r",
             "--rules",
             type=str,
             default=[RULES_PATH_DEFAULT_STRING],
@@ -976,14 +1034,21 @@
             logger.debug(" Using default embedded signatures.")
             logger.debug(
                 " To provide your own signatures, use the form `capa.exe --signature ./path/to/signatures/  /path/to/mal.exe`."
             )
             logger.debug("-" * 80)
 
             sigs_path = os.path.join(get_default_root(), "sigs")
+            if not os.path.exists(sigs_path):
+                logger.error(
+                    "Using default signature path, but it doesn't exist. "
+                    "Please install the signatures first: "
+                    "https://github.com/mandiant/capa/blob/master/doc/installation.md#method-2-using-capa-as-a-python-library."
+                )
+                raise IOError(f"signatures path {sigs_path} does not exist or cannot be accessed")
         else:
             sigs_path = args.signatures
             logger.debug("using signatures path: %s", sigs_path)
 
         args.signatures = sigs_path
 
 
@@ -1022,15 +1087,15 @@
             capa -t "create TCP socket" suspicious.exe
          """
     )
 
     parser = argparse.ArgumentParser(
         description=desc, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter
     )
-    install_common_args(parser, {"sample", "format", "backend", "signatures", "rules", "tag"})
+    install_common_args(parser, {"sample", "format", "backend", "os", "signatures", "rules", "tag"})
     parser.add_argument("-j", "--json", action="store_true", help="emit JSON instead of text")
     args = parser.parse_args(args=argv)
     ret = handle_common_args(args)
     if ret is not None and ret != 0:
         return ret
 
     try:
@@ -1120,55 +1185,80 @@
         if has_file_limitation(rules, pure_file_capabilities):
             # bail if capa encountered file limitation e.g. a packed binary
             # do show the output in verbose mode, though.
             if not (args.verbose or args.vverbose or args.json):
                 logger.debug("file limitation short circuit, won't analyze fully.")
                 return E_FILE_LIMITATION
 
-    if format_ == FORMAT_FREEZE:
-        with open(args.sample, "rb") as f:
-            extractor = capa.features.freeze.load(f.read())
+    # TODO: #1411 use a real type, not a dict here.
+    meta: Dict[str, Any]
+    capabilities: MatchResults
+    counts: Dict[str, Any]
+
+    if format_ == FORMAT_RESULT:
+        # result document directly parses into meta, capabilities
+        result_doc = capa.render.result_document.ResultDocument.parse_file(args.sample)
+        meta, capabilities = result_doc.to_capa()
+
     else:
-        try:
-            if format_ == FORMAT_PE:
-                sig_paths = get_signatures(args.signatures)
-            else:
-                sig_paths = []
-                logger.debug("skipping library code matching: only have native PE signatures")
-        except IOError as e:
-            logger.error("%s", str(e))
-            return E_INVALID_SIG
+        # all other formats we must create an extractor
+        # and use that to extract meta and capabilities
 
-        should_save_workspace = os.environ.get("CAPA_SAVE_WORKSPACE") not in ("0", "no", "NO", "n", None)
+        if format_ == FORMAT_FREEZE:
+            # freeze format deserializes directly into an extractor
+            with open(args.sample, "rb") as f:
+                extractor = capa.features.freeze.load(f.read())
+        else:
+            # all other formats we must create an extractor,
+            # such as viv, binary ninja, etc. workspaces
+            # and use those for extracting.
+
+            try:
+                if format_ == FORMAT_PE:
+                    sig_paths = get_signatures(args.signatures)
+                else:
+                    sig_paths = []
+                    logger.debug("skipping library code matching: only have native PE signatures")
+            except IOError as e:
+                logger.error("%s", str(e))
+                return E_INVALID_SIG
+
+            should_save_workspace = os.environ.get("CAPA_SAVE_WORKSPACE") not in ("0", "no", "NO", "n", None)
+
+            try:
+                extractor = get_extractor(
+                    args.sample,
+                    format_,
+                    args.os,
+                    args.backend,
+                    sig_paths,
+                    should_save_workspace,
+                    disable_progress=args.quiet,
+                )
+            except UnsupportedFormatError:
+                log_unsupported_format_error()
+                return E_INVALID_FILE_TYPE
+            except UnsupportedArchError:
+                log_unsupported_arch_error()
+                return E_INVALID_FILE_ARCH
+            except UnsupportedOSError:
+                log_unsupported_os_error()
+                return E_INVALID_FILE_OS
+
+        meta = collect_metadata(argv, args.sample, args.format, args.os, args.rules, extractor)
+
+        capabilities, counts = find_capabilities(rules, extractor, disable_progress=args.quiet)
+        meta["analysis"].update(counts)
+        meta["analysis"]["layout"] = compute_layout(rules, extractor, capabilities)
 
-        try:
-            extractor = get_extractor(
-                args.sample, format_, args.backend, sig_paths, should_save_workspace, disable_progress=args.quiet
-            )
-        except UnsupportedFormatError:
-            log_unsupported_format_error()
-            return E_INVALID_FILE_TYPE
-        except UnsupportedArchError:
-            log_unsupported_arch_error()
-            return E_INVALID_FILE_ARCH
-        except UnsupportedOSError:
-            log_unsupported_os_error()
-            return E_INVALID_FILE_OS
-
-    meta = collect_metadata(argv, args.sample, args.rules, extractor)
-
-    capabilities, counts = find_capabilities(rules, extractor, disable_progress=args.quiet)
-    meta["analysis"].update(counts)
-    meta["analysis"]["layout"] = compute_layout(rules, extractor, capabilities)
-
-    if has_file_limitation(rules, capabilities):
-        # bail if capa encountered file limitation e.g. a packed binary
-        # do show the output in verbose mode, though.
-        if not (args.verbose or args.vverbose or args.json):
-            return E_FILE_LIMITATION
+        if has_file_limitation(rules, capabilities):
+            # bail if capa encountered file limitation e.g. a packed binary
+            # do show the output in verbose mode, though.
+            if not (args.verbose or args.vverbose or args.json):
+                return E_FILE_LIMITATION
 
     if args.json:
         print(capa.render.json.render(meta, rules, capabilities))
     elif args.vverbose:
         print(capa.render.vverbose.render(meta, rules, capabilities))
     elif args.verbose:
         print(capa.render.verbose.render(meta, rules, capabilities))
```

### Comparing `flare-capa-5.0.0/capa/optimizer.py` & `flare-capa-5.1.0/capa/optimizer.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/render/default.py` & `flare-capa-5.1.0/capa/render/default.py`

 * *Files 4% similar despite different names*

```diff
@@ -93,15 +93,15 @@
             # see #224
             continue
 
         count = len(rule.matches)
         if count == 1:
             capability = rutils.bold(rule.meta.name)
         else:
-            capability = "%s (%d matches)" % (rutils.bold(rule.meta.name), count)
+            capability = f"{rutils.bold(rule.meta.name)} ({count} matches)"
         rows.append((capability, rule.meta.namespace))
 
     if rows:
         ostream.write(
             tabulate.tabulate(rows, headers=[width("CAPABILITY", 50), width("NAMESPACE", 50)], tablefmt="psql")
         )
         ostream.write("\n")
@@ -131,17 +131,17 @@
             tactics[attack.tactic].add((attack.technique, attack.subtechnique, attack.id))
 
     rows = []
     for tactic, techniques in sorted(tactics.items()):
         inner_rows = []
         for technique, subtechnique, id in sorted(techniques):
             if not subtechnique:
-                inner_rows.append("%s %s" % (rutils.bold(technique), id))
+                inner_rows.append(f"{rutils.bold(technique)} {id}")
             else:
-                inner_rows.append("%s::%s %s" % (rutils.bold(technique), subtechnique, id))
+                inner_rows.append(f"{rutils.bold(technique)}::{subtechnique} {id}")
         rows.append(
             (
                 rutils.bold(tactic.upper()),
                 "\n".join(inner_rows),
             )
         )
 
@@ -174,17 +174,17 @@
             objectives[mbc.objective].add((mbc.behavior, mbc.method, mbc.id))
 
     rows = []
     for objective, behaviors in sorted(objectives.items()):
         inner_rows = []
         for behavior, method, id in sorted(behaviors):
             if not method:
-                inner_rows.append("%s [%s]" % (rutils.bold(behavior), id))
+                inner_rows.append(f"{rutils.bold(behavior)} [{id}]")
             else:
-                inner_rows.append("%s::%s [%s]" % (rutils.bold(behavior), method, id))
+                inner_rows.append(f"{rutils.bold(behavior)}::{method} [{id}]")
         rows.append(
             (
                 rutils.bold(objective.upper()),
                 "\n".join(inner_rows),
             )
         )
```

### Comparing `flare-capa-5.0.0/capa/render/json.py` & `flare-capa-5.1.0/capa/render/json.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/capa/render/result_document.py` & `flare-capa-5.1.0/capa/render/result_document.py`

 * *Files 18% similar despite different names*

```diff
@@ -2,15 +2,16 @@
 # Licensed under the Apache License, Version 2.0 (the "License");
 #  you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at: [package root]/LICENSE.txt
 # Unless required by applicable law or agreed to in writing, software distributed under the License
 #  is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and limitations under the License.
 import datetime
-from typing import Any, Dict, Tuple, Union, Optional
+import collections
+from typing import Any, Dict, List, Tuple, Union, Optional
 
 from pydantic import Field, BaseModel
 
 import capa.rules
 import capa.engine
 import capa.features.common
 import capa.features.freeze as frz
@@ -20,14 +21,15 @@
 from capa.engine import MatchResults
 from capa.helpers import assert_never
 
 
 class FrozenModel(BaseModel):
     class Config:
         frozen = True
+        extra = "forbid"
 
 
 class Sample(FrozenModel):
     md5: str
     sha1: str
     sha256: str
     path: str
@@ -120,14 +122,49 @@
                 library_functions=tuple(
                     LibraryFunction(address=frz.Address.from_capa(address), name=name)
                     for address, name in meta["analysis"]["library_functions"].items()
                 ),
             ),
         )
 
+    def to_capa(self) -> Dict[str, Any]:
+        capa_meta = {
+            "timestamp": self.timestamp.isoformat(),
+            "version": self.version,
+            "sample": {
+                "md5": self.sample.md5,
+                "sha1": self.sample.sha1,
+                "sha256": self.sample.sha256,
+                "path": self.sample.path,
+            },
+            "analysis": {
+                "format": self.analysis.format,
+                "arch": self.analysis.arch,
+                "os": self.analysis.os,
+                "extractor": self.analysis.extractor,
+                "rules": self.analysis.rules,
+                "base_address": self.analysis.base_address.to_capa(),
+                "layout": {
+                    "functions": {
+                        f.address.to_capa(): {
+                            "matched_basic_blocks": [bb.address.to_capa() for bb in f.matched_basic_blocks]
+                        }
+                        for f in self.analysis.layout.functions
+                    }
+                },
+                "feature_counts": {
+                    "file": self.analysis.feature_counts.file,
+                    "functions": {fc.address.to_capa(): fc.count for fc in self.analysis.feature_counts.functions},
+                },
+                "library_functions": {lf.address.to_capa(): lf.name for lf in self.analysis.library_functions},
+            },
+        }
+
+        return capa_meta
+
 
 class CompoundStatementType:
     AND = "and"
     OR = "or"
     NOT = "not"
     OPTIONAL = "optional"
 
@@ -222,15 +259,63 @@
     elif isinstance(node, capa.engine.Feature):
         return FeatureNode(feature=frz.feature_from_capa(node))
 
     else:
         assert_never(node)
 
 
-class Match(BaseModel):
+def node_to_capa(
+    node: Node, children: List[Union[capa.engine.Statement, capa.engine.Feature]]
+) -> Union[capa.engine.Statement, capa.engine.Feature]:
+    if isinstance(node, StatementNode):
+        if isinstance(node.statement, CompoundStatement):
+            if node.statement.type == CompoundStatementType.AND:
+                return capa.engine.And(description=node.statement.description, children=children)
+
+            elif node.statement.type == CompoundStatementType.OR:
+                return capa.engine.Or(description=node.statement.description, children=children)
+
+            elif node.statement.type == CompoundStatementType.NOT:
+                return capa.engine.Not(description=node.statement.description, child=children[0])
+
+            elif node.statement.type == CompoundStatementType.OPTIONAL:
+                return capa.engine.Some(description=node.statement.description, count=0, children=children)
+
+            else:
+                assert_never(node.statement.type)
+
+        elif isinstance(node.statement, SomeStatement):
+            return capa.engine.Some(
+                description=node.statement.description, count=node.statement.count, children=children
+            )
+
+        elif isinstance(node.statement, RangeStatement):
+            return capa.engine.Range(
+                description=node.statement.description,
+                min=node.statement.min,
+                max=node.statement.max,
+                child=node.statement.child.to_capa(),
+            )
+
+        elif isinstance(node.statement, SubscopeStatement):
+            return capa.engine.Subscope(
+                description=node.statement.description, scope=node.statement.scope, child=children[0]
+            )
+
+        else:
+            assert_never(node.statement)
+
+    elif isinstance(node, FeatureNode):
+        return node.feature.to_capa()
+
+    else:
+        assert_never(node)
+
+
+class Match(FrozenModel):
     """
     args:
       success: did the node match?
       node: the logic node or feature node.
       children: any children of the logic node. not relevent for features, can be empty.
       locations: where the feature matched. not relevant for logic nodes (except range), can be empty.
       captures: captured values from the string/regex feature, and the locations of those values.
@@ -349,17 +434,50 @@
                             # so, grab only the locations for current rule.
                             if location in rule_matches:
                                 children.append(Match.from_capa(rules, capabilities, rule_matches[location]))
 
         return cls(
             success=success,
             node=node,
+            children=tuple(children),
+            locations=tuple(locations),
+            captures={capture: tuple(captures[capture]) for capture in captures},
+        )
+
+    def to_capa(self, rules_by_name: Dict[str, capa.rules.Rule]) -> capa.engine.Result:
+        children = [child.to_capa(rules_by_name) for child in self.children]
+        statement = node_to_capa(self.node, [child.statement for child in children])
+
+        if isinstance(self.node, FeatureNode):
+            feature = self.node.feature
+
+            if isinstance(feature, (frzf.SubstringFeature, frzf.RegexFeature)):
+                matches = {capture: {loc.to_capa() for loc in locs} for capture, locs in self.captures.items()}
+
+                if isinstance(feature, frzf.SubstringFeature):
+                    assert isinstance(statement, capa.features.common.Substring)
+                    statement = capa.features.common._MatchedSubstring(statement, matches)
+                elif isinstance(feature, frzf.RegexFeature):
+                    assert isinstance(statement, capa.features.common.Regex)
+                    statement = capa.features.common._MatchedRegex(statement, matches)
+                else:
+                    assert_never(feature)
+
+        # apparently we don't have to fixup match and subscope entries here.
+        # at least, default, verbose, and vverbose renderers seem to work well without any special handling here.
+        #
+        # children contains a single tree of results, corresponding to the logic of the matched rule.
+        # self.node.feature.match contains the name of the rule that was matched.
+        # so its all available to reconstruct, if necessary.
+
+        return capa.features.common.Result(
+            success=self.success,
+            statement=statement,
+            locations={loc.to_capa() for loc in self.locations},
             children=children,
-            locations=locations,
-            captures=captures,
         )
 
 
 def parse_parts_id(s: str):
     id_ = ""
     parts = s.split("::")
     if len(parts) > 0:
@@ -480,48 +598,50 @@
     @classmethod
     def from_capa(cls, rule: capa.rules.Rule) -> "RuleMetadata":
         return cls(
             name=rule.meta.get("name"),
             namespace=rule.meta.get("namespace"),
             authors=rule.meta.get("authors"),
             scope=capa.rules.Scope(rule.meta.get("scope")),
-            attack=list(map(AttackSpec.from_str, rule.meta.get("att&ck", []))),
-            mbc=list(map(MBCSpec.from_str, rule.meta.get("mbc", []))),
+            attack=tuple(map(AttackSpec.from_str, rule.meta.get("att&ck", []))),
+            mbc=tuple(map(MBCSpec.from_str, rule.meta.get("mbc", []))),
             references=rule.meta.get("references", []),
             examples=rule.meta.get("examples", []),
             description=rule.meta.get("description", ""),
             lib=rule.meta.get("lib", False),
-            capa_subscope=rule.meta.get("capa/subscope", False),
+            is_subscope_rule=rule.meta.get("capa/subscope", False),
             maec=MaecMetadata(
                 analysis_conclusion=rule.meta.get("maec/analysis-conclusion"),
                 analysis_conclusion_ov=rule.meta.get("maec/analysis-conclusion-ov"),
                 malware_family=rule.meta.get("maec/malware-family"),
                 malware_category=rule.meta.get("maec/malware-category"),
                 malware_category_ov=rule.meta.get("maec/malware-category-ov"),
-            ),
-        )
+            ),  # type: ignore
+            # Mypy is unable to recognise arguments due to alias
+        )  # type: ignore
+        # Mypy is unable to recognise arguments due to alias
 
     class Config:
         frozen = True
         allow_population_by_field_name = True
 
 
-class RuleMatches(BaseModel):
+class RuleMatches(FrozenModel):
     """
     args:
         meta: the metadata from the rule
         source: the raw rule text
     """
 
     meta: RuleMetadata
     source: str
     matches: Tuple[Tuple[frz.Address, Match], ...]
 
 
-class ResultDocument(BaseModel):
+class ResultDocument(FrozenModel):
     meta: Metadata
     rules: Dict[str, RuleMatches]
 
     @classmethod
     def from_capa(cls, meta, rules: RuleSet, capabilities: MatchResults) -> "ResultDocument":
         rule_matches: Dict[str, RuleMatches] = {}
         for rule_name, matches in capabilities.items():
@@ -536,7 +656,26 @@
                 matches=tuple(
                     (frz.Address.from_capa(addr), Match.from_capa(rules, capabilities, match))
                     for addr, match in matches
                 ),
             )
 
         return ResultDocument(meta=Metadata.from_capa(meta), rules=rule_matches)
+
+    def to_capa(self) -> Tuple[Dict, Dict]:
+        meta = self.meta.to_capa()
+        capabilities: Dict[
+            str, List[Tuple[capa.features.address.Address, capa.features.common.Result]]
+        ] = collections.defaultdict(list)
+
+        # this doesn't quite work because we don't have the rule source for rules that aren't matched.
+        rules_by_name = {
+            rule_name: capa.rules.Rule.from_yaml(rule_match.source) for rule_name, rule_match in self.rules.items()
+        }
+
+        for rule_name, rule_match in self.rules.items():
+            for addr, match in rule_match.matches:
+                result: capa.engine.Result = match.to_capa(rules_by_name)
+
+                capabilities[rule_name].append((addr.to_capa(), result))
+
+        return meta, capabilities
```

### Comparing `flare-capa-5.0.0/capa/render/utils.py` & `flare-capa-5.1.0/capa/render/utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 import termcolor
 
 import capa.render.result_document as rd
 
 
 def bold(s: str) -> str:
     """draw attention to the given string"""
-    return termcolor.colored(s, "blue")
+    return termcolor.colored(s, "cyan")
 
 
 def bold2(s: str) -> str:
     """draw attention to the given string, within a `bold` section"""
     return termcolor.colored(s, "green")
 
 
@@ -28,15 +28,15 @@
     return termcolor.colored(s, "yellow")
 
 
 def format_parts_id(data: Union[rd.AttackSpec, rd.MBCSpec]):
     """
     format canonical representation of ATT&CK/MBC parts and ID
     """
-    return "%s [%s]" % ("::".join(data.parts), data.id)
+    return f"{'::'.join(data.parts)} [{data.id}]"
 
 
 def capability_rules(doc: rd.ResultDocument) -> Iterator[rd.RuleMatches]:
     """enumerate the rules in (namespace, name) order that are 'capability' rules (not lib/subscope/disposition/etc)."""
     for _, _, rule in sorted(map(lambda rule: (rule.meta.namespace or "", rule.meta.name, rule), doc.rules.values())):
         if rule.meta.lib:
             continue
```

### Comparing `flare-capa-5.0.0/capa/render/verbose.py` & `flare-capa-5.1.0/capa/render/verbose.py`

 * *Files 10% similar despite different names*

```diff
@@ -33,23 +33,30 @@
 import capa.render.result_document as rd
 from capa.rules import RuleSet
 from capa.engine import MatchResults
 
 
 def format_address(address: frz.Address) -> str:
     if address.type == frz.AddressType.ABSOLUTE:
+        assert isinstance(address.value, int)
         return capa.helpers.hex(address.value)
     elif address.type == frz.AddressType.RELATIVE:
+        assert isinstance(address.value, int)
         return f"base address+{capa.helpers.hex(address.value)}"
     elif address.type == frz.AddressType.FILE:
+        assert isinstance(address.value, int)
         return f"file+{capa.helpers.hex(address.value)}"
     elif address.type == frz.AddressType.DN_TOKEN:
+        assert isinstance(address.value, int)
         return f"token({capa.helpers.hex(address.value)})"
     elif address.type == frz.AddressType.DN_TOKEN_OFFSET:
+        assert isinstance(address.value, tuple)
         token, offset = address.value
+        assert isinstance(token, int)
+        assert isinstance(offset, int)
         return f"token({capa.helpers.hex(token)})+{capa.helpers.hex(offset)}"
     elif address.type == frz.AddressType.NO_ADDRESS:
         return "global"
     else:
         raise ValueError("unexpected address type")
 
 
@@ -110,15 +117,15 @@
     """
     had_match = False
     for rule in rutils.capability_rules(doc):
         count = len(rule.matches)
         if count == 1:
             capability = rutils.bold(rule.meta.name)
         else:
-            capability = "%s (%d matches)" % (rutils.bold(rule.meta.name), count)
+            capability = f"{rutils.bold(rule.meta.name)} ({count} matches)"
 
         ostream.writeln(capability)
         had_match = True
 
         rows = []
         for key in ("namespace", "description", "scope"):
             v = getattr(rule.meta, key)
```

### Comparing `flare-capa-5.0.0/capa/render/vverbose.py` & `flare-capa-5.1.0/capa/render/vverbose.py`

 * *Files 6% similar despite different names*

```diff
@@ -39,15 +39,15 @@
     if len(locations) == 1:
         ostream.write(v.format_address(locations[0]))
 
     elif len(locations) > 4:
         # don't display too many locations, because it becomes very noisy.
         # probably only the first handful of locations will be useful for inspection.
         ostream.write(", ".join(map(v.format_address, locations[0:4])))
-        ostream.write(", and %d more..." % (len(locations) - 4))
+        ostream.write(f", and {(len(locations) - 4)} more...")
 
     elif len(locations) > 1:
         ostream.write(", ".join(map(v.format_address, locations)))
 
     else:
         raise RuntimeError("unreachable")
 
@@ -58,75 +58,75 @@
     if isinstance(statement, rd.SubscopeStatement):
         # emit `basic block:`
         # rather than `subscope:`
         ostream.write(statement.scope)
 
         ostream.write(":")
         if statement.description:
-            ostream.write(" = %s" % statement.description)
+            ostream.write(f" = {statement.description}")
         ostream.writeln("")
 
     elif isinstance(statement, (rd.CompoundStatement)):
         # emit `and:`  `or:`  `optional:`  `not:`
         ostream.write(statement.type)
 
         ostream.write(":")
         if statement.description:
-            ostream.write(" = %s" % statement.description)
+            ostream.write(f" = {statement.description}")
         ostream.writeln("")
 
     elif isinstance(statement, rd.SomeStatement):
-        ostream.write("%d or more:" % (statement.count))
+        ostream.write(f"{statement.count} or more:")
 
         if statement.description:
-            ostream.write(" = %s" % statement.description)
+            ostream.write(f" = {statement.description}")
         ostream.writeln("")
 
     elif isinstance(statement, rd.RangeStatement):
         # `range` is a weird node, its almost a hybrid of statement+feature.
         # it is a specific feature repeated multiple times.
         # there's no additional logic in the feature part, just the existence of a feature.
         # so, we have to inline some of the feature rendering here.
 
         child = statement.child
         value = child.dict(by_alias=True).get(child.type)
 
         if value:
             if isinstance(child, frzf.StringFeature):
-                value = '"%s"' % capa.features.common.escape_string(value)
+                value = f'"{capa.features.common.escape_string(value)}"'
 
             value = rutils.bold2(value)
 
             if child.description:
-                ostream.write("count(%s(%s = %s)): " % (child.type, value, child.description))
+                ostream.write(f"count({child.type}({value} = {child.description})): ")
             else:
-                ostream.write("count(%s(%s)): " % (child.type, value))
+                ostream.write(f"count({child.type}({value})): ")
         else:
-            ostream.write("count(%s): " % child.type)
+            ostream.write(f"count({child.type}): ")
 
         if statement.max == statement.min:
-            ostream.write("%d" % (statement.min))
+            ostream.write(f"{statement.min}")
         elif statement.min == 0:
-            ostream.write("%d or fewer" % (statement.max))
+            ostream.write(f"{statement.max} or fewer")
         elif statement.max == (1 << 64 - 1):
-            ostream.write("%d or more" % (statement.min))
+            ostream.write(f"{statement.min} or more")
         else:
-            ostream.write("between %d and %d" % (statement.min, statement.max))
+            ostream.write(f"between {statement.min} and {statement.max}")
 
         if statement.description:
-            ostream.write(" = %s" % statement.description)
+            ostream.write(f" = {statement.description}")
         render_locations(ostream, match.locations)
         ostream.writeln("")
 
     else:
         raise RuntimeError("unexpected match statement type: " + str(statement))
 
 
 def render_string_value(s: str) -> str:
-    return '"%s"' % capa.features.common.escape_string(s)
+    return f'"{capa.features.common.escape_string(s)}"'
 
 
 def render_feature(ostream, match: rd.Match, feature: frzf.Feature, indent=0):
     ostream.write("  " * indent)
 
     key = feature.type
     if isinstance(feature, frzf.BasicBlockFeature):
@@ -139,15 +139,15 @@
     elif isinstance(feature, frzf.ClassFeature):
         value = feature.class_
     else:
         # convert attributes to dictionary using aliased names, if applicable
         value = feature.dict(by_alias=True).get(key, None)
 
     if value is None:
-        raise ValueError("%s contains None" % key)
+        raise ValueError(f"{key} contains None")
 
     if not isinstance(feature, (frzf.RegexFeature, frzf.SubstringFeature)):
         # like:
         #   number: 10 = SOME_CONSTANT @ 0x401000
         if isinstance(feature, frzf.StringFeature):
             value = render_string_value(value)
 
@@ -286,19 +286,19 @@
             continue
 
         lib_info = ""
         count = len(rule.matches)
         if count == 1:
             if rule.meta.lib:
                 lib_info = " (library rule)"
-            capability = "%s%s" % (rutils.bold(rule.meta.name), lib_info)
+            capability = f"{rutils.bold(rule.meta.name)}{lib_info}"
         else:
             if rule.meta.lib:
                 lib_info = ", only showing first match of library rule"
-            capability = "%s (%d matches%s)" % (rutils.bold(rule.meta.name), count, lib_info)
+            capability = f"{rutils.bold(rule.meta.name)} ({count} matches{lib_info})"
 
         ostream.writeln(capability)
         had_match = True
 
         rows = []
         if not rule.meta.lib:
             # library rules should not have a namespace
@@ -341,15 +341,15 @@
         if rule.meta.scope == capa.rules.FILE_SCOPE:
             matches = doc.rules[rule.meta.name].matches
             if len(matches) != 1:
                 # i think there should only ever be one match per file-scope rule,
                 # because we do the file-scope evaluation a single time.
                 # but i'm not 100% sure if this is/will always be true.
                 # so, lets be explicit about our assumptions and raise an exception if they fail.
-                raise RuntimeError("unexpected file scope match count: %d" % (len(matches)))
+                raise RuntimeError(f"unexpected file scope match count: {len(matches)}")
             first_address, first_match = matches[0]
             render_match(ostream, first_match, indent=0)
         else:
             for location, match in sorted(doc.rules[rule.meta.name].matches):
                 ostream.write(rule.meta.scope)
                 ostream.write(" @ ")
                 ostream.write(capa.render.verbose.format_address(location))
```

### Comparing `flare-capa-5.0.0/capa/rules/__init__.py` & `flare-capa-5.1.0/capa/rules/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -159,59 +159,59 @@
 
 class InvalidRule(ValueError):
     def __init__(self, msg):
         super().__init__()
         self.msg = msg
 
     def __str__(self):
-        return "invalid rule: %s" % (self.msg)
+        return f"invalid rule: {self.msg}"
 
     def __repr__(self):
         return str(self)
 
 
 class InvalidRuleWithPath(InvalidRule):
     def __init__(self, path, msg):
         super().__init__(msg)
         self.path = path
         self.msg = msg
         self.__cause__ = None
 
     def __str__(self):
-        return "invalid rule: %s: %s" % (self.path, self.msg)
+        return f"invalid rule: {self.path}: {self.msg}"
 
 
 class InvalidRuleSet(ValueError):
     def __init__(self, msg):
         super().__init__()
         self.msg = msg
 
     def __str__(self):
-        return "invalid rule set: %s" % (self.msg)
+        return f"invalid rule set: {self.msg}"
 
     def __repr__(self):
         return str(self)
 
 
 def ensure_feature_valid_for_scope(scope: str, feature: Union[Feature, Statement]):
     # if the given feature is a characteristic,
     # check that is a valid characteristic for the given scope.
     if (
         isinstance(feature, capa.features.common.Characteristic)
         and isinstance(feature.value, str)
         and capa.features.common.Characteristic(feature.value) not in SUPPORTED_FEATURES[scope]
     ):
-        raise InvalidRule("feature %s not supported for scope %s" % (feature, scope))
+        raise InvalidRule(f"feature {feature} not supported for scope {scope}")
 
     if not isinstance(feature, capa.features.common.Characteristic):
         # features of this scope that are not Characteristics will be Type instances.
         # check that the given feature is one of these types.
         types_for_scope = filter(lambda t: isinstance(t, type), SUPPORTED_FEATURES[scope])
         if not isinstance(feature, tuple(types_for_scope)):  # type: ignore
-            raise InvalidRule("feature %s not supported for scope %s" % (feature, scope))
+            raise InvalidRule(f"feature {feature} not supported for scope {scope}")
 
 
 def parse_int(s: str) -> int:
     if s.startswith("0x"):
         return int(s, 0x10)
     else:
         return int(s, 10)
@@ -220,18 +220,18 @@
 def parse_range(s: str):
     """
     parse a string "(0, 1)" into a range (min, max).
     min and/or max may by None to indicate an unbound range.
     """
     # we want to use `{` characters, but this is a dict in yaml.
     if not s.startswith("("):
-        raise InvalidRule("invalid range: %s" % (s))
+        raise InvalidRule(f"invalid range: {s}")
 
     if not s.endswith(")"):
-        raise InvalidRule("invalid range: %s" % (s))
+        raise InvalidRule(f"invalid range: {s}")
 
     s = s[len("(") : -len(")")]
     min_spec, _, max_spec = s.partition(",")
     min_spec = min_spec.strip()
     max_spec = max_spec.strip()
 
     min_ = None
@@ -292,33 +292,33 @@
     elif key == "class":
         return capa.features.common.Class
     elif key == "namespace":
         return capa.features.common.Namespace
     elif key == "property":
         return capa.features.insn.Property
     else:
-        raise InvalidRule("unexpected statement: %s" % key)
+        raise InvalidRule(f"unexpected statement: {key}")
 
 
 # this is the separator between a feature value and its description
 # when using the inline description syntax, like:
 #
 #     number: 42 = ENUM_FAVORITE_NUMBER
 DESCRIPTION_SEPARATOR = " = "
 
 
 def parse_bytes(s: str) -> bytes:
     try:
         b = codecs.decode(s.replace(" ", "").encode("ascii"), "hex")
     except binascii.Error:
-        raise InvalidRule('unexpected bytes value: must be a valid hex sequence: "%s"' % s)
+        raise InvalidRule(f'unexpected bytes value: must be a valid hex sequence: "{s}"')
 
     if len(b) > MAX_BYTES_FEATURE_SIZE:
         raise InvalidRule(
-            "unexpected bytes value: byte sequences must be no larger than %s bytes" % MAX_BYTES_FEATURE_SIZE
+            f"unexpected bytes value: byte sequences must be no larger than {MAX_BYTES_FEATURE_SIZE} bytes"
         )
 
     return b
 
 
 def parse_description(s: Union[str, int, bytes], value_type: str, description=None):
     if value_type == "string":
@@ -333,23 +333,22 @@
             if DESCRIPTION_SEPARATOR in s:
                 if description:
                     # there is already a description passed in as a sub node, like:
                     #
                     #     - number: 10 = CONST_FOO
                     #       description: CONST_FOO
                     raise InvalidRule(
-                        'unexpected value: "%s", only one description allowed (inline description with `%s`)'
-                        % (s, DESCRIPTION_SEPARATOR)
+                        f'unexpected value: "{s}", only one description allowed (inline description with `{DESCRIPTION_SEPARATOR}`)'
                     )
 
                 value, _, description = s.partition(DESCRIPTION_SEPARATOR)
                 if description == "":
                     # sanity check:
                     # there is an empty description, like `number: 10 =`
-                    raise InvalidRule('unexpected value: "%s", description cannot be empty' % s)
+                    raise InvalidRule(f'unexpected value: "{s}", description cannot be empty')
             else:
                 # this is a string, but there is no description,
                 # like: `api: CreateFileA`
                 value = s
 
             # cast from the received string value to the appropriate type.
             #
@@ -368,15 +367,15 @@
                     value_type.startswith("operand[")
                     and (value_type.endswith("].number") or value_type.endswith("].offset"))
                 )
             ):
                 try:
                     value = parse_int(value)
                 except ValueError:
-                    raise InvalidRule('unexpected value: "%s", must begin with numerical value' % value)
+                    raise InvalidRule(f'unexpected value: "{value}", must begin with numerical value')
 
         else:
             # the value might be a number, like: `number: 10`
             value = s
 
     return value, description
 
@@ -528,17 +527,17 @@
             min = None
             max = parse_int(count[: -len(" or fewer")])
             return ceng.Range(feature, min=min, max=max, description=description)
         elif count.startswith("("):
             min, max = parse_range(count)
             return ceng.Range(feature, min=min, max=max, description=description)
         else:
-            raise InvalidRule("unexpected range: %s" % (count))
+            raise InvalidRule(f"unexpected range: {count}")
     elif key == "string" and not isinstance(d[key], str):
-        raise InvalidRule("ambiguous string value %s, must be defined as explicit string" % d[key])
+        raise InvalidRule(f"ambiguous string value {d[key]}, must be defined as explicit string")
 
     elif key.startswith("operand[") and key.endswith("].number"):
         index = key[len("operand[") : -len("].number")]
         try:
             index = int(index)
         except ValueError as e:
             raise InvalidRule("operand index must be an integer") from e
@@ -569,20 +568,20 @@
         return feature
 
     elif (
         (key == "os" and d[key] not in capa.features.common.VALID_OS)
         or (key == "format" and d[key] not in capa.features.common.VALID_FORMAT)
         or (key == "arch" and d[key] not in capa.features.common.VALID_ARCH)
     ):
-        raise InvalidRule("unexpected %s value %s" % (key, d[key]))
+        raise InvalidRule(f"unexpected {key} value {d[key]}")
 
     elif key.startswith("property/"):
         access = key[len("property/") :]
         if access not in capa.features.common.VALID_FEATURE_ACCESS:
-            raise InvalidRule("unexpected %s access %s" % (key, access))
+            raise InvalidRule(f"unexpected {key} access {access}")
 
         value, description = parse_description(d[key], key, d.get("description"))
         try:
             feature = capa.features.insn.Property(value, access=access, description=description)
         except ValueError as e:
             raise InvalidRule(str(e)) from e
         ensure_feature_valid_for_scope(scope, feature)
@@ -613,18 +612,18 @@
         self.name = name
         self.scope = scope
         self.statement = statement
         self.meta = meta
         self.definition = definition
 
     def __str__(self):
-        return "Rule(name=%s)" % (self.name)
+        return f"Rule(name={self.name})"
 
     def __repr__(self):
-        return "Rule(scope=%s, name=%s)" % (self.scope, self.name)
+        return f"Rule(scope={self.scope}, name={self.name})"
 
     def get_dependencies(self, namespaces):
         """
         fetch the names of rules this rule relies upon.
         these are only the direct dependencies; a user must
          compute the transitive dependency graph themself, if they want it.
 
@@ -994,15 +993,15 @@
     # we evaluate `rules` multiple times, so if its a generator, realize it into a list.
     rules = list(rules)
     namespaces = index_rules_by_namespace(rules)
     rules_by_name = {rule.name: rule for rule in rules}
     for rule in rules_by_name.values():
         for dep in rule.get_dependencies(namespaces):
             if dep not in rules_by_name:
-                raise InvalidRule('rule "%s" depends on missing rule "%s"' % (rule.name, dep))
+                raise InvalidRule(f'rule "{rule.name}" depends on missing rule "{dep}"')
 
 
 def index_rules_by_namespace(rules: List[Rule]) -> Dict[str, List[Rule]]:
     """
     compute the rules that fit into each namespace found within the given rules.
 
     for example, given:
```

### Comparing `flare-capa-5.0.0/capa/rules/cache.py` & `flare-capa-5.1.0/capa/rules/cache.py`

 * *Files identical despite different names*

### Comparing `flare-capa-5.0.0/flare_capa.egg-info/PKG-INFO` & `flare-capa-5.1.0/flare_capa.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: flare-capa
-Version: 5.0.0
+Version: 5.1.0
 Summary: The FLARE team's open-source tool to identify capabilities in executable files.
 Home-page: https://www.github.com/mandiant/capa
 Author: Willi Ballenthin, Moritz Raabe
 Author-email: william.ballenthin@mandiant.com, moritz.raabe@mandiant.com
 License: UNKNOWN
 Project-URL: Documentation, https://github.com/mandiant/capa/tree/master/doc
 Project-URL: Rules, https://github.com/mandiant/capa-rules
 Project-URL: Rules Documentation, https://github.com/mandiant/capa-rules/tree/master/doc
 Description: ![capa](https://github.com/mandiant/capa/blob/master/.github/logo.png)
         
         [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flare-capa)](https://pypi.org/project/flare-capa)
         [![Last release](https://img.shields.io/github/v/release/mandiant/capa)](https://github.com/mandiant/capa/releases)
-        [![Number of rules](https://img.shields.io/badge/rules-770-blue.svg)](https://github.com/mandiant/capa-rules)
+        [![Number of rules](https://img.shields.io/badge/rules-794-blue.svg)](https://github.com/mandiant/capa-rules)
         [![CI status](https://github.com/mandiant/capa/workflows/CI/badge.svg)](https://github.com/mandiant/capa/actions?query=workflow%3ACI+event%3Apush+branch%3Amaster)
         [![Downloads](https://img.shields.io/github/downloads/mandiant/capa/total)](https://github.com/mandiant/capa/releases)
         [![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE.txt)
         
         capa detects capabilities in executable files.
         You run it against a PE, ELF, .NET module, or shellcode file and it tells you what it thinks the program can do.
         For example, it might suggest that the file is a backdoor, is capable of installing services, or relies on HTTP to communicate.
```

### Comparing `flare-capa-5.0.0/flare_capa.egg-info/SOURCES.txt` & `flare-capa-5.1.0/flare_capa.egg-info/SOURCES.txt`

 * *Files 3% similar despite different names*

```diff
@@ -23,14 +23,23 @@
 capa/features/extractors/elf.py
 capa/features/extractors/elffile.py
 capa/features/extractors/helpers.py
 capa/features/extractors/loops.py
 capa/features/extractors/null.py
 capa/features/extractors/pefile.py
 capa/features/extractors/strings.py
+capa/features/extractors/binja/__init__.py
+capa/features/extractors/binja/basicblock.py
+capa/features/extractors/binja/extractor.py
+capa/features/extractors/binja/file.py
+capa/features/extractors/binja/find_binja_api.py
+capa/features/extractors/binja/function.py
+capa/features/extractors/binja/global_.py
+capa/features/extractors/binja/helpers.py
+capa/features/extractors/binja/insn.py
 capa/features/extractors/dnfile/__init__.py
 capa/features/extractors/dnfile/extractor.py
 capa/features/extractors/dnfile/file.py
 capa/features/extractors/dnfile/function.py
 capa/features/extractors/dnfile/helpers.py
 capa/features/extractors/dnfile/insn.py
 capa/features/extractors/dnfile/types.py
@@ -70,14 +79,16 @@
 capa/render/__init__.py
 capa/render/default.py
 capa/render/json.py
 capa/render/result_document.py
 capa/render/utils.py
 capa/render/verbose.py
 capa/render/vverbose.py
+capa/render/proto/__init__.py
+capa/render/proto/capa_pb2.py
 capa/rules/__init__.py
 capa/rules/cache.py
 flare_capa.egg-info/PKG-INFO
 flare_capa.egg-info/SOURCES.txt
 flare_capa.egg-info/dependency_links.txt
 flare_capa.egg-info/entry_points.txt
 flare_capa.egg-info/not-zip-safe
```

### Comparing `flare-capa-5.0.0/setup.py` & `flare-capa-5.1.0/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 # See the License for the specific language governing permissions and limitations under the License.
 
 import os
 
 import setuptools
 
 requirements = [
-    "tqdm==4.64.1",
+    "tqdm==4.65.0",
     "pyyaml==6.0",
     "tabulate==0.9.0",
     "colorama==0.4.5",
     "termcolor==2.2.0",
     "wcwidth==0.2.6",
     "ida-settings==2.1.0",
     "viv-utils[flirt]==0.7.7",
@@ -23,15 +23,16 @@
     "networkx==2.5.1",  # newer versions no longer support py3.7.
     "ruamel.yaml==0.17.21",
     "vivisect==1.0.8",
     "pefile==2022.5.30",
     "pyelftools==0.29",
     "dnfile==0.13.0",
     "dncil==1.0.2",
-    "pydantic==1.10.4",
+    "pydantic==1.10.7",
+    "protobuf==4.22.1",
 ]
 
 # this sets __version__
 # via: http://stackoverflow.com/a/7071358/87207
 # and: http://stackoverflow.com/a/2073599/87207
 with open(os.path.join("capa", "version.py"), "r") as f:
     exec(f.read())
@@ -66,34 +67,36 @@
     },
     include_package_data=True,
     install_requires=requirements,
     extras_require={
         "dev": [
             "pytest==7.1.3",
             "pytest-sugar==0.9.4",
-            "pytest-instafail==0.4.2",
+            "pytest-instafail==0.5.0",
             "pytest-cov==4.0.0",
             "pycodestyle==2.10.0",
-            "black==23.1.0",
+            "black==23.3.0",
             "isort==5.11.4",
-            "mypy==0.991",
+            "mypy==1.1.1",
             "psutil==5.9.2",
             "stix2==3.0.1",
             "requests==2.28.0",
+            "mypy-protobuf==3.4.0",
             # type stubs for mypy
             "types-backports==0.1.3",
             "types-colorama==0.4.15",
             "types-PyYAML==6.0.8",
-            "types-tabulate==0.9.0.0",
+            "types-tabulate==0.9.0.1",
             "types-termcolor==1.1.4",
             "types-psutil==5.8.23",
             "types_requests==2.28.1",
+            "types-protobuf==4.22.0.1",
         ],
         "build": [
-            "pyinstaller==5.7.0",
+            "pyinstaller==5.9.0",
         ],
     },
     zip_safe=False,
     keywords="capa malware analysis capability detection FLARE",
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
```

