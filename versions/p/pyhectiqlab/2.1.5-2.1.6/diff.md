# Comparing `tmp/pyhectiqlab-2.1.5.tar.gz` & `tmp/pyhectiqlab-2.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/hectiq-lab/hectiq-lab/python-client/dist/.tmp-ta154wiv/pyhectiqlab-2.1.5.tar", last modified: Mon Apr  3 19:51:20 2023, max compression
+gzip compressed data, was "/home/runner/work/hectiq-lab/hectiq-lab/python-client/dist/.tmp-w7uoxhue/pyhectiqlab-2.1.6.tar", last modified: Thu Apr  6 18:59:59 2023, max compression
```

## Comparing `pyhectiqlab-2.1.5.tar` & `pyhectiqlab-2.1.6.tar`

### file list

```diff
@@ -1,68 +1,68 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/
--rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab/
--rwxr-xr-x   0 runner    (1001) docker     (123)      145 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5588 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)     3125 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     1621 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/buffer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab/callbacks/
--rwxr-xr-x   0 runner    (1001) docker     (123)       32 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/callbacks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3898 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/callbacks/keras.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab/cli/
--rwxr-xr-x   0 runner    (1001) docker     (123)      115 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6269 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/cli/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/cli/main.py
--rw-r--r--   0 runner    (1001) docker     (123)     4279 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/config_template.py
--rw-r--r--   0 runner    (1001) docker     (123)     5648 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/datasets.py
--rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/decorators.py
--rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/events_manager.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     4629 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     5643 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/mlmodels.py
--rw-r--r--   0 runner    (1001) docker     (123)     5068 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/notebooks.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    15602 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/ops.py
--rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/paper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1487 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/pulse.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    29731 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/run.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      349 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/settings.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      736 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/stream.py
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/timer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2492 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/upload.py
--rw-r--r--   0 runner    (1001) docker     (123)     3127 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6280 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyhectiqlab/watermark.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1404 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-03 19:50:59.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/pyhectiqlab.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1412 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/artifacts/
--rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/artifacts/test_img1.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)    21603 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/artifacts/test_img2.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)     2937 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/create_run.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/dataset/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/dataset/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/dataset/imgs/
--rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/dataset/imgs/test_img1.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)    21603 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/dataset/imgs/test_img2.jpeg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/mlmodel/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/mlmodel/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/mlmodel/imgs/
--rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/mlmodel/imgs/test_img1.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)    21603 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/mlmodel/imgs/test_img2.jpeg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-03 19:51:20.000000 pyhectiqlab-2.1.5/tests/step_artifacts/
--rw-r--r--   0 runner    (1001) docker     (123)   158372 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/step_artifacts/step1.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)   165197 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/step_artifacts/step2.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)   726799 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/step_artifacts/step3.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)   172506 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/step_artifacts/step4.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)   165748 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/step_artifacts/step8.jpeg
--rw-r--r--   0 runner    (1001) docker     (123)   153112 2023-04-03 19:50:54.000000 pyhectiqlab-2.1.5/tests/step_artifacts/step9.jpeg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/
+-rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      145 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5588 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3125 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1621 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/buffer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab/callbacks/
+-rwxr-xr-x   0 runner    (1001) docker     (123)       32 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/callbacks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3898 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/callbacks/keras.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab/cli/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      115 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6269 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/cli/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)       65 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/cli/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4279 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/config_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5648 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/datasets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1340 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/decorators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/events_manager.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4629 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5643 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/mlmodels.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5068 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/notebooks.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    15602 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/ops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/paper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1487 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/pulse.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    29886 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/run.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      349 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/settings.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      736 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/stream.py
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2492 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/upload.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3127 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6318 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyhectiqlab/watermark.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1404 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:59:39.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/pyhectiqlab.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      122 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1412 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/artifacts/
+-rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/artifacts/test_img1.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)    21603 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/artifacts/test_img2.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)     2937 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/create_run.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/dataset/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/dataset/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/dataset/imgs/
+-rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/dataset/imgs/test_img1.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)    21603 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/dataset/imgs/test_img2.jpeg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/mlmodel/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/mlmodel/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/mlmodel/imgs/
+-rw-r--r--   0 runner    (1001) docker     (123)     7210 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/mlmodel/imgs/test_img1.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)    21603 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/mlmodel/imgs/test_img2.jpeg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:59:59.000000 pyhectiqlab-2.1.6/tests/step_artifacts/
+-rw-r--r--   0 runner    (1001) docker     (123)   158372 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/step_artifacts/step1.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)   165197 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/step_artifacts/step2.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)   726799 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/step_artifacts/step3.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)   172506 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/step_artifacts/step4.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)   165748 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/step_artifacts/step8.jpeg
+-rw-r--r--   0 runner    (1001) docker     (123)   153112 2023-04-06 18:59:35.000000 pyhectiqlab-2.1.6/tests/step_artifacts/step9.jpeg
```

### Comparing `pyhectiqlab-2.1.5/LICENSE` & `pyhectiqlab-2.1.6/LICENSE`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/PKG-INFO` & `pyhectiqlab-2.1.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyhectiqlab
-Version: 2.1.5
+Version: 2.1.6
 Summary: Python client to use the Hectiq Lab
 Home-page: https://lab.hectiq.ai
 Author: Edward Laurence
 Author-email: edwardl@hectiq.ai
 Keywords: pip requirements imports
 Classifier: Programming Language :: Python :: 3
 Classifier: Intended Audience :: Developers
```

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/apps.py` & `pyhectiqlab-2.1.6/pyhectiqlab/apps.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/auth.py` & `pyhectiqlab-2.1.6/pyhectiqlab/auth.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/buffer.py` & `pyhectiqlab-2.1.6/pyhectiqlab/buffer.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/callbacks/keras.py` & `pyhectiqlab-2.1.6/pyhectiqlab/callbacks/keras.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/cli/auth.py` & `pyhectiqlab-2.1.6/pyhectiqlab/cli/auth.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/config.py` & `pyhectiqlab-2.1.6/pyhectiqlab/config.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/config_template.py` & `pyhectiqlab-2.1.6/pyhectiqlab/config_template.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/datasets.py` & `pyhectiqlab-2.1.6/pyhectiqlab/datasets.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/decorators.py` & `pyhectiqlab-2.1.6/pyhectiqlab/decorators.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/events_manager.py` & `pyhectiqlab-2.1.6/pyhectiqlab/events_manager.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/metrics.py` & `pyhectiqlab-2.1.6/pyhectiqlab/metrics.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/mlmodels.py` & `pyhectiqlab-2.1.6/pyhectiqlab/mlmodels.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/notebooks.py` & `pyhectiqlab-2.1.6/pyhectiqlab/notebooks.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/ops.py` & `pyhectiqlab-2.1.6/pyhectiqlab/ops.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/paper.py` & `pyhectiqlab-2.1.6/pyhectiqlab/paper.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/pulse.py` & `pyhectiqlab-2.1.6/pyhectiqlab/pulse.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/run.py` & `pyhectiqlab-2.1.6/pyhectiqlab/run.py`

 * *Files 1% similar despite different names*

```diff
@@ -448,29 +448,33 @@
     @action_method
     def add_package_versions(self, packages: Optional[dict] =None, with_sys: bool = True, with_python: bool = True, with_git: bool = True):
         """Save the version of the imported packages.
 
         Usage:
         add_package_versions(globals())
         """
-        water = Watermark()
-        versions = {}
-        if with_python:
-            versions["python"] = water.get_pyversions()
-        if with_sys:
-            versions["system"] = water.get_sysinfo()
-        if packages:
-            versions["packages"] = water.get_all_import_versions(packages)
-        if with_git:
-            git_info = water.get_git_info()
-            if git_info:
-                versions["git"] = water.get_git_info()
+        try:
+            water = Watermark()
+            versions = {}
+            if with_python:
+                versions["python"] = water.get_pyversions()
+            if with_sys:
+                versions["system"] = water.get_sysinfo()
+            if packages:
+                versions["packages"] = water.get_all_import_versions(packages)
+            if with_git:
+                git_info = water.get_git_info()
+                if git_info:
+                    versions["git"] = water.get_git_info()
 
-        args = (self._id, self._project_path, versions)
-        self.events_manager.add_event("push_package_versions", args)
+            args = (self._id, self._project_path, versions)
+            self.events_manager.add_event("push_package_versions", args)
+        except:
+            print("Could not add package versions.")
+            pass
 
     @write_method
     @action_method
     def add_package_repo_state(self, package: str = None):
         """Save the branch/commit/origin of the git repo in which
         a package is located.
```

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/stream.py` & `pyhectiqlab-2.1.6/pyhectiqlab/stream.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/upload.py` & `pyhectiqlab-2.1.6/pyhectiqlab/upload.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/utils.py` & `pyhectiqlab-2.1.6/pyhectiqlab/utils.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab/watermark.py` & `pyhectiqlab-2.1.6/pyhectiqlab/watermark.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,13 @@
 import platform
 import types
-from git import Repo, InvalidGitRepositoryError
+try:
+    from git import Repo, InvalidGitRepositoryError
+except ImportError:
+    pass
 from multiprocessing import cpu_count
 import subprocess
 import importlib
 import inspect
 import socket
 
 try:
```

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab.egg-info/PKG-INFO` & `pyhectiqlab-2.1.6/pyhectiqlab.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pyhectiqlab
-Version: 2.1.5
+Version: 2.1.6
 Summary: Python client to use the Hectiq Lab
 Home-page: https://lab.hectiq.ai
 Author: Edward Laurence
 Author-email: edwardl@hectiq.ai
 Keywords: pip requirements imports
 Classifier: Programming Language :: Python :: 3
 Classifier: Intended Audience :: Developers
```

### Comparing `pyhectiqlab-2.1.5/pyhectiqlab.egg-info/SOURCES.txt` & `pyhectiqlab-2.1.6/pyhectiqlab.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/setup.py` & `pyhectiqlab-2.1.6/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
 from setuptools import setup, find_packages
-__version__ = '2.1.5'
+__version__ = '2.1.6'
 
 with open('README.md', encoding='utf-8') as f:
     readme = f.read()
 
 requirements = [
     "requests",
     "tqdm",
```

### Comparing `pyhectiqlab-2.1.5/tests/artifacts/test_img1.jpeg` & `pyhectiqlab-2.1.6/tests/artifacts/test_img1.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/artifacts/test_img2.jpeg` & `pyhectiqlab-2.1.6/tests/artifacts/test_img2.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/create_run.py` & `pyhectiqlab-2.1.6/tests/create_run.py`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/dataset/imgs/test_img1.jpeg` & `pyhectiqlab-2.1.6/tests/dataset/imgs/test_img1.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/dataset/imgs/test_img2.jpeg` & `pyhectiqlab-2.1.6/tests/dataset/imgs/test_img2.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/mlmodel/imgs/test_img1.jpeg` & `pyhectiqlab-2.1.6/tests/mlmodel/imgs/test_img1.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/mlmodel/imgs/test_img2.jpeg` & `pyhectiqlab-2.1.6/tests/mlmodel/imgs/test_img2.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/step_artifacts/step1.jpeg` & `pyhectiqlab-2.1.6/tests/step_artifacts/step1.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/step_artifacts/step2.jpeg` & `pyhectiqlab-2.1.6/tests/step_artifacts/step2.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/step_artifacts/step3.jpeg` & `pyhectiqlab-2.1.6/tests/step_artifacts/step3.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/step_artifacts/step4.jpeg` & `pyhectiqlab-2.1.6/tests/step_artifacts/step4.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/step_artifacts/step8.jpeg` & `pyhectiqlab-2.1.6/tests/step_artifacts/step8.jpeg`

 * *Files identical despite different names*

### Comparing `pyhectiqlab-2.1.5/tests/step_artifacts/step9.jpeg` & `pyhectiqlab-2.1.6/tests/step_artifacts/step9.jpeg`

 * *Files identical despite different names*

