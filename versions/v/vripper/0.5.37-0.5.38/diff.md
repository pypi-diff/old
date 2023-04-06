# Comparing `tmp/vripper-0.5.37.tar.gz` & `tmp/vripper-0.5.38.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vripper-0.5.37.tar", last modified: Tue Apr  4 14:26:40 2023, max compression
+gzip compressed data, was "vripper-0.5.38.tar", last modified: Thu Apr  6 13:33:57 2023, max compression
```

## Comparing `vripper-0.5.37.tar` & `vripper-0.5.38.tar`

### file list

```diff
@@ -1,84 +1,84 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.066422 vripper-0.5.37/
--rw-r--r--   0 runner    (1001) docker     (123)     4229 2023-04-04 14:26:40.066422 vripper-0.5.37/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3906 2023-04-04 14:26:30.000000 vripper-0.5.37/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 14:26:40.066422 vripper-0.5.37/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      776 2023-04-04 14:26:30.000000 vripper-0.5.37/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.058421 vripper-0.5.37/vripper/
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.058421 vripper-0.5.37/vripper/download/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/gdlwrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/imagedownloader.py
--rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/postdownloader.py
--rw-r--r--   0 runner    (1001) docker     (123)     1443 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/postprogress.py
--rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/threaddownloader.py
--rw-r--r--   0 runner    (1001) docker     (123)     1303 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/download/threadprogress.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.062421 vripper-0.5.37/vripper/enum/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/enum/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/enum/downloadmode.py
--rw-r--r--   0 runner    (1001) docker     (123)       66 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/enum/outputformat.py
--rw-r--r--   0 runner    (1001) docker     (123)      134 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/enum/processingpriority.py
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/error.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.062421 vripper-0.5.37/vripper/forum/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.062421 vripper-0.5.37/vripper/forum/provider/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1633 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/buondua.py
--rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/dirtyship.py
--rw-r--r--   0 runner    (1001) docker     (123)      776 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/nlegs.py
--rw-r--r--   0 runner    (1001) docker     (123)      871 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/superbeautygirlx.py
--rw-r--r--   0 runner    (1001) docker     (123)      764 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/thaihotmodels.py
--rw-r--r--   0 runner    (1001) docker     (123)     1010 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/v2ph.py
--rw-r--r--   0 runner    (1001) docker     (123)     1993 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/provider/vipergirls.py
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/forum/threadfactory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.062421 vripper-0.5.37/vripper/model/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/model/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      648 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/model/vimage.py
--rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/model/vparams.py
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/model/vpost.py
--rw-r--r--   0 runner    (1001) docker     (123)      336 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/model/vthread.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.066422 vripper-0.5.37/vripper/parser/
--rw-r--r--   0 runner    (1001) docker     (123)      423 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1197 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/_common.py
--rw-r--r--   0 runner    (1001) docker     (123)      520 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/_def.py
--rw-r--r--   0 runner    (1001) docker     (123)      118 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/_template.py
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/acidimg.py
--rw-r--r--   0 runner    (1001) docker     (123)      201 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/damimage.py
--rw-r--r--   0 runner    (1001) docker     (123)      328 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/dirtyship.py
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imagebam.py
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imagedecode.py
--rw-r--r--   0 runner    (1001) docker     (123)      202 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imagenimage.py
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imageporter.py
--rw-r--r--   0 runner    (1001) docker     (123)      306 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imagetwist.py
--rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imagevenue.py
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imagezilla.py
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgbabes.py
--rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgbox.py
--rw-r--r--   0 runner    (1001) docker     (123)      543 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgclick.py
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgflare.py
--rw-r--r--   0 runner    (1001) docker     (123)      520 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imghit.py
--rw-r--r--   0 runner    (1001) docker     (123)       99 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgmoney.py
--rw-r--r--   0 runner    (1001) docker     (123)      120 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgproof.py
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgspice.py
--rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgtaxi.py
--rw-r--r--   0 runner    (1001) docker     (123)      176 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgtown.py
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/imgzeus.py
--rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/nlegs.py
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/photolot.py
--rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/picstate.py
--rw-r--r--   0 runner    (1001) docker     (123)      121 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/picszsite.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/pixhost.py
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/pixxxelscc.py
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/postimgcc.py
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/turboimagehost.py
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/uplimg.py
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/parser/viprim.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.066422 vripper-0.5.37/vripper/postprocess/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/postprocess/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2598 2023-04-04 14:26:30.000000 vripper-0.5.37/vripper/postprocess/imgproc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 14:26:40.058421 vripper-0.5.37/vripper.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4229 2023-04-04 14:26:40.000000 vripper-0.5.37/vripper.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-04-04 14:26:40.000000 vripper-0.5.37/vripper.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 14:26:40.000000 vripper-0.5.37/vripper.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-04 14:26:40.000000 vripper-0.5.37/vripper.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-04 14:26:40.000000 vripper-0.5.37/vripper.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.389199 vripper-0.5.38/
+-rw-r--r--   0 runner    (1001) docker     (123)     4229 2023-04-06 13:33:57.389199 vripper-0.5.38/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3906 2023-04-06 13:33:50.000000 vripper-0.5.38/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:33:57.389199 vripper-0.5.38/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      776 2023-04-06 13:33:50.000000 vripper-0.5.38/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.381199 vripper-0.5.38/vripper/
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.381199 vripper-0.5.38/vripper/download/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2301 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/gdlwrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/imagedownloader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5582 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/postdownloader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1443 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/postprogress.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/threaddownloader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1303 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/download/threadprogress.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.381199 vripper-0.5.38/vripper/enum/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/enum/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/enum/downloadmode.py
+-rw-r--r--   0 runner    (1001) docker     (123)       66 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/enum/outputformat.py
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/enum/processingpriority.py
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/error.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.385199 vripper-0.5.38/vripper/forum/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.385199 vripper-0.5.38/vripper/forum/provider/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1633 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/buondua.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/dirtyship.py
+-rw-r--r--   0 runner    (1001) docker     (123)      776 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/nlegs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      871 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/superbeautygirlx.py
+-rw-r--r--   0 runner    (1001) docker     (123)      764 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/thaihotmodels.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/v2ph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1993 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/provider/vipergirls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/forum/threadfactory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.385199 vripper-0.5.38/vripper/model/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/model/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      648 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/model/vimage.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/model/vparams.py
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/model/vpost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      336 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/model/vthread.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.389199 vripper-0.5.38/vripper/parser/
+-rw-r--r--   0 runner    (1001) docker     (123)      423 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1197 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/_common.py
+-rw-r--r--   0 runner    (1001) docker     (123)      520 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/_def.py
+-rw-r--r--   0 runner    (1001) docker     (123)      118 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/acidimg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      201 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/damimage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      328 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/dirtyship.py
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imagebam.py
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imagedecode.py
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imagenimage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imageporter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      306 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imagetwist.py
+-rw-r--r--   0 runner    (1001) docker     (123)      357 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imagevenue.py
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imagezilla.py
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgbabes.py
+-rw-r--r--   0 runner    (1001) docker     (123)      249 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgbox.py
+-rw-r--r--   0 runner    (1001) docker     (123)      543 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgclick.py
+-rw-r--r--   0 runner    (1001) docker     (123)      228 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgflare.py
+-rw-r--r--   0 runner    (1001) docker     (123)      520 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imghit.py
+-rw-r--r--   0 runner    (1001) docker     (123)       99 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgmoney.py
+-rw-r--r--   0 runner    (1001) docker     (123)      120 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgproof.py
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgspice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgtaxi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      176 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgtown.py
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/imgzeus.py
+-rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/nlegs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/photolot.py
+-rw-r--r--   0 runner    (1001) docker     (123)      189 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/picstate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      121 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/picszsite.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/pixhost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/pixxxelscc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/postimgcc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/turboimagehost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/uplimg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/parser/viprim.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.389199 vripper-0.5.38/vripper/postprocess/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/postprocess/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2598 2023-04-06 13:33:50.000000 vripper-0.5.38/vripper/postprocess/imgproc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:33:57.381199 vripper-0.5.38/vripper.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4229 2023-04-06 13:33:57.000000 vripper-0.5.38/vripper.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-04-06 13:33:57.000000 vripper-0.5.38/vripper.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:33:57.000000 vripper-0.5.38/vripper.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 13:33:57.000000 vripper-0.5.38/vripper.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-06 13:33:57.000000 vripper-0.5.38/vripper.egg-info/top_level.txt
```

### Comparing `vripper-0.5.37/PKG-INFO` & `vripper-0.5.38/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vripper
-Version: 0.5.37
+Version: 0.5.38
 Summary: A Python implementation of VRipper
 Home-page: UNKNOWN
 Author: vka
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
```

### Comparing `vripper-0.5.37/README.md` & `vripper-0.5.38/README.md`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/setup.py` & `vripper-0.5.38/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 long_description = long_description.replace(" [here](vripper/parser).", ":\n\n" + get_bullet_points())
 
 setuptools.setup(
     name="vripper",
-    version="0.5.37",
+    version="0.5.38",
     author="vka",
     description="A Python implementation of VRipper",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=setuptools.find_packages(exclude=("test",)),
     classifiers=[
         "Programming Language :: Python :: 3",
```

### Comparing `vripper-0.5.37/vripper/download/gdlwrapper.py` & `vripper-0.5.38/vripper/download/gdlwrapper.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/download/imagedownloader.py` & `vripper-0.5.38/vripper/download/imagedownloader.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/download/postdownloader.py` & `vripper-0.5.38/vripper/download/postdownloader.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/download/postprogress.py` & `vripper-0.5.38/vripper/download/postprogress.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/download/threaddownloader.py` & `vripper-0.5.38/vripper/download/threaddownloader.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/download/threadprogress.py` & `vripper-0.5.38/vripper/download/threadprogress.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/error.py` & `vripper-0.5.38/vripper/error.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/provider/buondua.py` & `vripper-0.5.38/vripper/forum/provider/buondua.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/provider/dirtyship.py` & `vripper-0.5.38/vripper/forum/provider/dirtyship.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/provider/nlegs.py` & `vripper-0.5.38/vripper/forum/provider/nlegs.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/provider/superbeautygirlx.py` & `vripper-0.5.38/vripper/forum/provider/superbeautygirlx.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/provider/thaihotmodels.py` & `vripper-0.5.38/vripper/forum/provider/thaihotmodels.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/provider/vipergirls.py` & `vripper-0.5.38/vripper/forum/provider/vipergirls.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/forum/threadfactory.py` & `vripper-0.5.38/vripper/forum/threadfactory.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/model/vimage.py` & `vripper-0.5.38/vripper/model/vimage.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/model/vparams.py` & `vripper-0.5.38/vripper/model/vparams.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/parser/_common.py` & `vripper-0.5.38/vripper/parser/_common.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/parser/_def.py` & `vripper-0.5.38/vripper/parser/_def.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/parser/imgclick.py` & `vripper-0.5.38/vripper/parser/imgclick.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/parser/imghit.py` & `vripper-0.5.38/vripper/parser/imghit.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/parser/nlegs.py` & `vripper-0.5.38/vripper/parser/nlegs.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper/postprocess/imgproc.py` & `vripper-0.5.38/vripper/postprocess/imgproc.py`

 * *Files identical despite different names*

### Comparing `vripper-0.5.37/vripper.egg-info/PKG-INFO` & `vripper-0.5.38/vripper.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vripper
-Version: 0.5.37
+Version: 0.5.38
 Summary: A Python implementation of VRipper
 Home-page: UNKNOWN
 Author: vka
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: Operating System :: OS Independent
```

### Comparing `vripper-0.5.37/vripper.egg-info/SOURCES.txt` & `vripper-0.5.38/vripper.egg-info/SOURCES.txt`

 * *Files identical despite different names*

