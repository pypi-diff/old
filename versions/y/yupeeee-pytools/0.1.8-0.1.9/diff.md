# Comparing `tmp/yupeeee-pytools-0.1.8.tar.gz` & `tmp/yupeeee-pytools-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "yupeeee-pytools-0.1.8.tar", last modified: Wed Mar 15 03:48:07 2023, max compression
+gzip compressed data, was "yupeeee-pytools-0.1.9.tar", last modified: Tue Mar 21 23:56:22 2023, max compression
```

## Comparing `yupeeee-pytools-0.1.8.tar` & `yupeeee-pytools-0.1.9.tar`

### file list

```diff
@@ -1,64 +1,64 @@
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.868617 yupeeee-pytools-0.1.8/
--rw-rw-rw-   0        0        0     1086 2023-03-04 20:14:07.000000 yupeeee-pytools-0.1.8/LICENSE
--rw-rw-rw-   0        0        0      838 2023-03-15 03:48:07.868617 yupeeee-pytools-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0      589 2023-03-15 03:47:33.000000 yupeeee-pytools-0.1.8/README.md
--rw-rw-rw-   0        0        0       42 2023-03-15 03:48:07.868617 yupeeee-pytools-0.1.8/setup.cfg
--rw-rw-rw-   0        0        0      886 2023-03-15 03:47:33.000000 yupeeee-pytools-0.1.8/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.528340 yupeeee-pytools-0.1.8/src/
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.559583 yupeeee-pytools-0.1.8/src/yupeeee_pytools/
--rw-rw-rw-   0        0        0      205 2023-03-03 06:08:12.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.575204 yupeeee-pytools-0.1.8/src/yupeeee_pytools/attacks/
--rw-rw-rw-   0        0        0       26 2023-03-04 20:13:06.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/attacks/__init__.py
--rw-rw-rw-   0        0        0     4699 2023-03-05 12:54:06.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/attacks/ifgsm.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.653324 yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/
--rw-rw-rw-   0        0        0       87 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/__init__.py
--rw-rw-rw-   0        0        0     2792 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/base.py
--rw-rw-rw-   0        0        0     4458 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/classification.py
--rw-rw-rw-   0        0        0     1240 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/config.py
--rw-rw-rw-   0        0        0     1275 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/normalize.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.653324 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/
--rw-rw-rw-   0        0        0       55 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.747328 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/
--rw-rw-rw-   0        0        0       72 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/__init__.py
--rw-rw-rw-   0        0        0     7878 2023-03-15 03:46:54.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/base.py
--rw-rw-rw-   0        0        0     8695 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/config.py
--rw-rw-rw-   0        0        0     2161 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/model.py
--rw-rw-rw-   0        0        0      882 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/preprocess.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.762679 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/
--rw-rw-rw-   0        0        0      101 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/__init__.py
--rw-rw-rw-   0        0        0      395 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/activation.py
--rw-rw-rw-   0        0        0     1269 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/base.py
--rw-rw-rw-   0        0        0     2016 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/common.py
--rw-rw-rw-   0        0        0      185 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/config.py
--rw-rw-rw-   0        0        0     1842 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/normalization.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.793901 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/
--rw-rw-rw-   0        0        0      181 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/__init__.py
--rw-rw-rw-   0        0        0     3713 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/dictools.py
--rw-rw-rw-   0        0        0      968 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/imgtools.py
--rw-rw-rw-   0        0        0      591 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/linalgtools.py
--rw-rw-rw-   0        0        0     4416 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/listools.py
--rw-rw-rw-   0        0        0     2299 2023-03-04 20:13:06.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/misctools.py
--rw-rw-rw-   0        0        0      966 2023-03-04 07:10:05.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/pathtools.py
--rw-rw-rw-   0        0        0      237 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/randtools.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.837333 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/
--rw-rw-rw-   0        0        0      158 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/__init__.py
--rw-rw-rw-   0        0        0     8921 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/base.py
--rw-rw-rw-   0        0        0      478 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/criterion.py
--rw-rw-rw-   0        0        0      475 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/dataloader.py
--rw-rw-rw-   0        0        0     2298 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/lr_scheduler.py
--rw-rw-rw-   0        0        0     3912 2023-03-03 15:10:06.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/lr_warmup.py
--rw-rw-rw-   0        0        0     1926 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/optimizer.py
--rw-rw-rw-   0        0        0      522 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/trainer.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.868617 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/
--rw-rw-rw-   0        0        0       49 2023-03-14 23:05:27.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/__init__.py
--rw-rw-rw-   0        0        0      463 2023-03-14 23:18:50.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/common.py
--rw-rw-rw-   0        0        0      298 2023-03-15 00:32:06.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/config.py
--rw-rw-rw-   0        0        0     3085 2023-03-15 00:22:54.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/direction.py
--rw-rw-rw-   0        0        0     1344 2023-03-14 23:52:03.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/footprint.py
--rw-rw-rw-   0        0        0     5540 2023-03-15 03:28:40.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/travel.py
-drwxrwxrwx   0        0        0        0 2023-03-15 03:48:07.559583 yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/
--rw-rw-rw-   0        0        0      838 2023-03-15 03:48:07.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1986 2023-03-15 03:48:07.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-15 03:48:07.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0      130 2023-03-15 03:48:07.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/requires.txt
--rw-rw-rw-   0        0        0       16 2023-03-15 03:48:07.000000 yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:22.172546 yupeeee-pytools-0.1.9/
+-rw-rw-rw-   0        0        0     1086 2023-03-04 20:14:07.000000 yupeeee-pytools-0.1.9/LICENSE
+-rw-rw-rw-   0        0        0      838 2023-03-21 23:56:22.172546 yupeeee-pytools-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0      589 2023-03-21 23:56:08.000000 yupeeee-pytools-0.1.9/README.md
+-rw-rw-rw-   0        0        0       42 2023-03-21 23:56:22.172546 yupeeee-pytools-0.1.9/setup.cfg
+-rw-rw-rw-   0        0        0      886 2023-03-21 23:56:08.000000 yupeeee-pytools-0.1.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.094049 yupeeee-pytools-0.1.9/src/
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.126028 yupeeee-pytools-0.1.9/src/yupeeee_pytools/
+-rw-rw-rw-   0        0        0      205 2023-03-03 06:08:12.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.245300 yupeeee-pytools-0.1.9/src/yupeeee_pytools/attacks/
+-rw-rw-rw-   0        0        0       26 2023-03-04 20:13:06.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/attacks/__init__.py
+-rw-rw-rw-   0        0        0     4699 2023-03-05 12:54:06.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/attacks/ifgsm.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.516577 yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/
+-rw-rw-rw-   0        0        0       87 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/__init__.py
+-rw-rw-rw-   0        0        0     2792 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/base.py
+-rw-rw-rw-   0        0        0     4458 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/classification.py
+-rw-rw-rw-   0        0        0     1240 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/config.py
+-rw-rw-rw-   0        0        0     1275 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/normalize.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.572576 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/
+-rw-rw-rw-   0        0        0       55 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/__init__.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.804384 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/
+-rw-rw-rw-   0        0        0       72 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/__init__.py
+-rw-rw-rw-   0        0        0     7953 2023-03-15 07:22:47.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/base.py
+-rw-rw-rw-   0        0        0     8695 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/config.py
+-rw-rw-rw-   0        0        0     2161 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/model.py
+-rw-rw-rw-   0        0        0      882 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/preprocess.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:21.080187 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/
+-rw-rw-rw-   0        0        0      101 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/__init__.py
+-rw-rw-rw-   0        0        0      395 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/activation.py
+-rw-rw-rw-   0        0        0     1269 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/base.py
+-rw-rw-rw-   0        0        0     2016 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/common.py
+-rw-rw-rw-   0        0        0      185 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/config.py
+-rw-rw-rw-   0        0        0     1842 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/normalization.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:21.479664 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/
+-rw-rw-rw-   0        0        0      181 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/__init__.py
+-rw-rw-rw-   0        0        0     3713 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/dictools.py
+-rw-rw-rw-   0        0        0      968 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/imgtools.py
+-rw-rw-rw-   0        0        0      591 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/linalgtools.py
+-rw-rw-rw-   0        0        0     4416 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/listools.py
+-rw-rw-rw-   0        0        0     2299 2023-03-04 20:13:06.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/misctools.py
+-rw-rw-rw-   0        0        0      966 2023-03-04 07:10:05.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/pathtools.py
+-rw-rw-rw-   0        0        0      237 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/randtools.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:21.876742 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/
+-rw-rw-rw-   0        0        0      158 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/__init__.py
+-rw-rw-rw-   0        0        0     8921 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/base.py
+-rw-rw-rw-   0        0        0      478 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/criterion.py
+-rw-rw-rw-   0        0        0      475 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/dataloader.py
+-rw-rw-rw-   0        0        0     2298 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/lr_scheduler.py
+-rw-rw-rw-   0        0        0     3912 2023-03-03 15:10:06.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/lr_warmup.py
+-rw-rw-rw-   0        0        0     1926 2023-03-03 05:35:17.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/optimizer.py
+-rw-rw-rw-   0        0        0      522 2023-03-04 04:58:36.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/trainer.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:22.116557 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/
+-rw-rw-rw-   0        0        0       49 2023-03-14 23:05:27.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/__init__.py
+-rw-rw-rw-   0        0        0      463 2023-03-14 23:18:50.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/common.py
+-rw-rw-rw-   0        0        0      298 2023-03-15 00:32:06.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/config.py
+-rw-rw-rw-   0        0        0     3320 2023-03-21 21:53:31.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/direction.py
+-rw-rw-rw-   0        0        0     1610 2023-03-21 21:53:31.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/footprint.py
+-rw-rw-rw-   0        0        0     5540 2023-03-15 03:28:40.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/travel.py
+drwxrwxrwx   0        0        0        0 2023-03-21 23:56:20.181991 yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/
+-rw-rw-rw-   0        0        0      838 2023-03-21 23:56:19.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1986 2023-03-21 23:56:20.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-21 23:56:19.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      130 2023-03-21 23:56:19.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       16 2023-03-21 23:56:19.000000 yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/top_level.txt
```

### Comparing `yupeeee-pytools-0.1.8/LICENSE` & `yupeeee-pytools-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/PKG-INFO` & `yupeeee-pytools-0.1.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yupeeee-pytools
-Version: 0.1.8
+Version: 0.1.9
 Home-page: https://github.com/yupeeee/PyTools
 Author: Juyeop Kim
 Author-email: juyeopkim@yonsei.ac.kr
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
@@ -13,17 +13,17 @@
 PyTools is a Python package based on PyTorch.
 
 ---
 
 
 ## Installation
 
-Latest version: 0.1.8
+Latest version: 0.1.9
 ```
-pip install yupeeee-pytools==0.1.8
+pip install yupeeee-pytools==0.1.9
 ```
 
 Manual installation of PyTorch is required.\
 https://pytorch.org/get-started/locally/
 
 
 ### Requirements
```

### Comparing `yupeeee-pytools-0.1.8/README.md` & `yupeeee-pytools-0.1.9/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -3,17 +3,17 @@
 PyTools is a Python package based on PyTorch.
 
 ---
 
 
 ## Installation
 
-Latest version: 0.1.8
+Latest version: 0.1.9
 ```
-pip install yupeeee-pytools==0.1.8
+pip install yupeeee-pytools==0.1.9
 ```
 
 Manual installation of PyTorch is required.\
 https://pytorch.org/get-started/locally/
 
 
 ### Requirements
```

### Comparing `yupeeee-pytools-0.1.8/setup.py` & `yupeeee-pytools-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 this_directory = Path(__file__).parent
 long_description = (this_directory / "README.md").read_text()
 
 
 setup(
     name="yupeeee-pytools",
-    version="0.1.8",
+    version="0.1.9",
     description="",
     long_description=long_description,
     long_description_content_type="text/markdown",
     author="Juyeop Kim",
     author_email="juyeopkim@yonsei.ac.kr",
     url="https://github.com/yupeeee/PyTools",
     license="MIT",
```

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/attacks/ifgsm.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/attacks/ifgsm.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/base.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/base.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/classification.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/classification.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/config.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/config.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/datasets/normalize.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/datasets/normalize.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/base.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -106,15 +106,15 @@
 
         self.softmax = nn.Softmax(dim=-1)
 
     def __call__(
             self,
             data: Any,
     ) -> Any:
-        return self.model(data).detach()
+        return self.model(getattr(data, self.machine)()).detach()
 
     def load_model(
             self,
     ) -> Any:
         assert self.name in imagenet_models
 
         if self.name in list_of_pytorch_imagenet_models:
@@ -183,15 +183,15 @@
             if (
                     not isinstance(module, nn.Sequential)
                     and not isinstance(module, nn.ModuleList)
             ):
                 hooks.append(module.register_forward_hook(hook))
 
         self.model.apply(register_hook)
-        self.model(dummy_data)
+        self.model(getattr(dummy_data, self.machine)())
 
         for hook in hooks:
             hook.remove()
 
         return layers
 
     def x_ray(
@@ -224,15 +224,15 @@
             if (
                     not isinstance(module, nn.Sequential)
                     and not isinstance(module, nn.ModuleList)
             ):
                 hooks.append(module.register_forward_hook(hook))
 
         self.model.apply(register_hook)
-        self.model(data)
+        self.model(getattr(data, self.machine)())
 
         for hook in hooks:
             hook.remove()
 
         return inputs, outputs
 
     def grad_cam(
```

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/config.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/config.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/model.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/model.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/classification/preprocess.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/classification/preprocess.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/base.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/base.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/common.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/common.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/models/replace/normalization.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/models/replace/normalization.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/dictools.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/dictools.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/imgtools.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/imgtools.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/linalgtools.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/linalgtools.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/listools.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/listools.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/misctools.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/misctools.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/tools/pathtools.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/tools/pathtools.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/base.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/base.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/lr_scheduler.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/lr_scheduler.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/lr_warmup.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/lr_warmup.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/optimizer.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/optimizer.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/train/trainer.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/train/trainer.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/direction.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/direction.py`

 * *Files 10% similar despite different names*

```diff
@@ -25,14 +25,25 @@
 
     else:
         raise ValueError
 
     return normalized.reshape(shape)
 
 
+# def cw_direction(
+#         data: torch.Tensor,
+#         targets: torch.Tensor,
+#         model,
+#         normalize: str = None,
+#         seed: int = None,
+#         use_cuda: bool = False,
+# ) -> torch.Tensor:
+# TBD
+
+
 def fgsm_direction(
         data: torch.Tensor,
         targets: torch.Tensor,
         model,
         normalize: str = None,
         seed: int = None,
         use_cuda: bool = False,
```

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/footprint.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/footprint.py`

 * *Files 9% similar despite different names*

```diff
@@ -33,23 +33,33 @@
             model=model,
             use_cuda=use_cuda,
         )
 
     def generate_footprints(
             self,
             data: torch.Tensor,
-            directions: torch.Tensor,
-            epsilons: torch.Tensor,
+            direction: torch.Tensor,
+            epsilon: torch.Tensor,
     ):
-        from ..tools import repeat_tensor
+        data = data.unsqueeze(dim=0)
 
-        _data = repeat_tensor(
-            tensor=data,
-            repeat=self.step + 1,
-            dim=0,
-        )
+        if epsilon < 0:
+            return None, None, None
 
-        _directions = repeat_tensor(
-            tensor=directions,
-            repeat=self.step + 1,
-            dim=0,
-        )
+        footprints = []
+        # TBD
+
+        # from ..tools import repeat_tensor
+        #
+        # _data = repeat_tensor(
+        #     tensor=data,
+        #     repeat=self.step + 1,
+        #     dim=0,
+        # )
+        #
+        # _directions = repeat_tensor(
+        #     tensor=directions,
+        #     repeat=self.step + 1,
+        #     dim=0,
+        # ).reshape(self.step + 1, -1)
+        #
+        # _epsilons = torch.diag(epsilons)
```

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools/travel/travel.py` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools/travel/travel.py`

 * *Files identical despite different names*

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/PKG-INFO` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: yupeeee-pytools
-Version: 0.1.8
+Version: 0.1.9
 Home-page: https://github.com/yupeeee/PyTools
 Author: Juyeop Kim
 Author-email: juyeopkim@yonsei.ac.kr
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
@@ -13,17 +13,17 @@
 PyTools is a Python package based on PyTorch.
 
 ---
 
 
 ## Installation
 
-Latest version: 0.1.8
+Latest version: 0.1.9
 ```
-pip install yupeeee-pytools==0.1.8
+pip install yupeeee-pytools==0.1.9
 ```
 
 Manual installation of PyTorch is required.\
 https://pytorch.org/get-started/locally/
 
 
 ### Requirements
```

### Comparing `yupeeee-pytools-0.1.8/src/yupeeee_pytools.egg-info/SOURCES.txt` & `yupeeee-pytools-0.1.9/src/yupeeee_pytools.egg-info/SOURCES.txt`

 * *Files identical despite different names*

