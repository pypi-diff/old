# Comparing `tmp/nvitop-1.1.0.tar.gz` & `tmp/nvitop-1.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nvitop-1.1.0.tar", last modified: Fri Apr  7 14:18:22 2023, max compression
+gzip compressed data, was "nvitop-1.1.1.tar", last modified: Fri Apr  7 14:47:08 2023, max compression
```

## Comparing `nvitop-1.1.0.tar` & `nvitop-1.1.1.tar`

### file list

```diff
@@ -1,69 +1,69 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.894419 nvitop-1.1.0/
--rw-r--r--   0 runner    (1001) docker     (122)    35149 2023-04-07 14:15:38.000000 nvitop-1.1.0/COPYING
--rw-r--r--   0 runner    (1001) docker     (122)    11368 2023-04-07 14:15:38.000000 nvitop-1.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)       98 2023-04-07 14:15:38.000000 nvitop-1.1.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)    75962 2023-04-07 14:18:22.894419 nvitop-1.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)    73788 2023-04-07 14:15:38.000000 nvitop-1.1.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.886419 nvitop-1.1.0/nvitop/
--rw-r--r--   0 runner    (1001) docker     (122)     1540 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)      245 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.886419 nvitop-1.1.0/nvitop/api/
--rw-r--r--   0 runner    (1001) docker     (122)    11368 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)     1772 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    33446 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/collector.py
--rw-r--r--   0 runner    (1001) docker     (122)   105902 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/device.py
--rw-r--r--   0 runner    (1001) docker     (122)     3242 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/host.py
--rw-r--r--   0 runner    (1001) docker     (122)    37357 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/libcuda.py
--rw-r--r--   0 runner    (1001) docker     (122)    42646 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/libcudart.py
--rw-r--r--   0 runner    (1001) docker     (122)    28144 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/libnvml.py
--rw-r--r--   0 runner    (1001) docker     (122)    39522 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/process.py
--rw-r--r--   0 runner    (1001) docker     (122)    21954 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/api/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.890419 nvitop-1.1.0/nvitop/callbacks/
--rw-r--r--   0 runner    (1001) docker     (122)    11368 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)      758 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     7620 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/keras.py
--rw-r--r--   0 runner    (1001) docker     (122)      916 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/lightning.py
--rw-r--r--   0 runner    (1001) docker     (122)     7531 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/pytorch_lightning.py
--rw-r--r--   0 runner    (1001) docker     (122)     1592 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/tensorboard.py
--rw-r--r--   0 runner    (1001) docker     (122)     2604 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/callbacks/utils.py
--rw-r--r--   0 runner    (1001) docker     (122)    16186 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.890419 nvitop-1.1.0/nvitop/gui/
--rw-r--r--   0 runner    (1001) docker     (122)    35149 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/COPYING
--rw-r--r--   0 runner    (1001) docker     (122)      317 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.894419 nvitop-1.1.0/nvitop/gui/library/
--rw-r--r--   0 runner    (1001) docker     (122)     1145 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     7072 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/device.py
--rw-r--r--   0 runner    (1001) docker     (122)     8122 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/displayable.py
--rw-r--r--   0 runner    (1001) docker     (122)    12436 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/history.py
--rw-r--r--   0 runner    (1001) docker     (122)    11686 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/keybinding.py
--rw-r--r--   0 runner    (1001) docker     (122)     8790 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/libcurses.py
--rw-r--r--   0 runner    (1001) docker     (122)    12729 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/messagebox.py
--rw-r--r--   0 runner    (1001) docker     (122)     3331 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/mouse.py
--rw-r--r--   0 runner    (1001) docker     (122)     3704 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/process.py
--rw-r--r--   0 runner    (1001) docker     (122)     4694 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/selection.py
--rw-r--r--   0 runner    (1001) docker     (122)     2494 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/utils.py
--rw-r--r--   0 runner    (1001) docker     (122)     7175 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/library/widestring.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.894419 nvitop-1.1.0/nvitop/gui/screens/
--rw-r--r--   0 runner    (1001) docker     (122)      422 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     8495 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/environ.py
--rw-r--r--   0 runner    (1001) docker     (122)     4562 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/help.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.894419 nvitop-1.1.0/nvitop/gui/screens/main/
--rw-r--r--   0 runner    (1001) docker     (122)    10011 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/main/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    22158 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/main/device.py
--rw-r--r--   0 runner    (1001) docker     (122)    16519 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/main/host.py
--rw-r--r--   0 runner    (1001) docker     (122)    24592 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/main/process.py
--rw-r--r--   0 runner    (1001) docker     (122)    22108 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/metrics.py
--rw-r--r--   0 runner    (1001) docker     (122)    20506 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/screens/treeview.py
--rw-r--r--   0 runner    (1001) docker     (122)    12396 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/gui/ui.py
--rw-r--r--   0 runner    (1001) docker     (122)    18501 2023-04-07 14:15:38.000000 nvitop-1.1.0/nvitop/select.py
--rw-r--r--   0 runner    (1001) docker     (122)     3827 2023-04-07 14:18:14.000000 nvitop-1.1.0/nvitop/version.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:18:22.886419 nvitop-1.1.0/nvitop.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)    75962 2023-04-07 14:18:22.000000 nvitop-1.1.0/nvitop.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     1470 2023-04-07 14:18:22.000000 nvitop-1.1.0/nvitop.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 14:18:22.000000 nvitop-1.1.0/nvitop.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       71 2023-04-07 14:18:22.000000 nvitop-1.1.0/nvitop.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (122)      698 2023-04-07 14:18:22.000000 nvitop-1.1.0/nvitop.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        7 2023-04-07 14:18:22.000000 nvitop-1.1.0/nvitop.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)     4638 2023-04-07 14:15:38.000000 nvitop-1.1.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 14:18:22.894419 nvitop-1.1.0/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (122)     1783 2023-04-07 14:15:38.000000 nvitop-1.1.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.074974 nvitop-1.1.1/
+-rw-r--r--   0 runner    (1001) docker     (122)    35149 2023-04-07 14:44:55.000000 nvitop-1.1.1/COPYING
+-rw-r--r--   0 runner    (1001) docker     (122)    11368 2023-04-07 14:44:55.000000 nvitop-1.1.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)       98 2023-04-07 14:44:55.000000 nvitop-1.1.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)    75962 2023-04-07 14:47:08.074974 nvitop-1.1.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    73788 2023-04-07 14:44:55.000000 nvitop-1.1.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.070974 nvitop-1.1.1/nvitop/
+-rw-r--r--   0 runner    (1001) docker     (122)     1540 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      245 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.070974 nvitop-1.1.1/nvitop/api/
+-rw-r--r--   0 runner    (1001) docker     (122)    11368 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     1772 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    33446 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/collector.py
+-rw-r--r--   0 runner    (1001) docker     (122)   105902 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/device.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3242 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/host.py
+-rw-r--r--   0 runner    (1001) docker     (122)    37357 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/libcuda.py
+-rw-r--r--   0 runner    (1001) docker     (122)    42646 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/libcudart.py
+-rw-r--r--   0 runner    (1001) docker     (122)    28144 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/libnvml.py
+-rw-r--r--   0 runner    (1001) docker     (122)    39522 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/process.py
+-rw-r--r--   0 runner    (1001) docker     (122)    21954 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/api/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.070974 nvitop-1.1.1/nvitop/callbacks/
+-rw-r--r--   0 runner    (1001) docker     (122)    11368 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)      758 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7620 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/keras.py
+-rw-r--r--   0 runner    (1001) docker     (122)      916 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/lightning.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7531 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/pytorch_lightning.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1592 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/tensorboard.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2604 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/callbacks/utils.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16186 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.074974 nvitop-1.1.1/nvitop/gui/
+-rw-r--r--   0 runner    (1001) docker     (122)    35149 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/COPYING
+-rw-r--r--   0 runner    (1001) docker     (122)      317 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.074974 nvitop-1.1.1/nvitop/gui/library/
+-rw-r--r--   0 runner    (1001) docker     (122)     1145 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7494 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/device.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8122 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/displayable.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12436 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/history.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11686 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/keybinding.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8790 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/libcurses.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12729 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/messagebox.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3331 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/mouse.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3704 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/process.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4694 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/selection.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2494 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/utils.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7175 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/library/widestring.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.074974 nvitop-1.1.1/nvitop/gui/screens/
+-rw-r--r--   0 runner    (1001) docker     (122)      422 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8495 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/environ.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4562 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/help.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.074974 nvitop-1.1.1/nvitop/gui/screens/main/
+-rw-r--r--   0 runner    (1001) docker     (122)    10011 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/main/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    22158 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/main/device.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16519 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/main/host.py
+-rw-r--r--   0 runner    (1001) docker     (122)    24592 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/main/process.py
+-rw-r--r--   0 runner    (1001) docker     (122)    22108 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (122)    20506 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/screens/treeview.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12396 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/gui/ui.py
+-rw-r--r--   0 runner    (1001) docker     (122)    18501 2023-04-07 14:44:55.000000 nvitop-1.1.1/nvitop/select.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3827 2023-04-07 14:47:01.000000 nvitop-1.1.1/nvitop/version.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 14:47:08.070974 nvitop-1.1.1/nvitop.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)    75962 2023-04-07 14:47:08.000000 nvitop-1.1.1/nvitop.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1470 2023-04-07 14:47:08.000000 nvitop-1.1.1/nvitop.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 14:47:08.000000 nvitop-1.1.1/nvitop.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       71 2023-04-07 14:47:08.000000 nvitop-1.1.1/nvitop.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      698 2023-04-07 14:47:08.000000 nvitop-1.1.1/nvitop.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        7 2023-04-07 14:47:08.000000 nvitop-1.1.1/nvitop.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)     4638 2023-04-07 14:44:55.000000 nvitop-1.1.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 14:47:08.074974 nvitop-1.1.1/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (122)     1783 2023-04-07 14:44:55.000000 nvitop-1.1.1/setup.py
```

### Comparing `nvitop-1.1.0/COPYING` & `nvitop-1.1.1/COPYING`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/LICENSE` & `nvitop-1.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/PKG-INFO` & `nvitop-1.1.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 4d65 7461 6461 7461 2d56 6572 7369 6f6e  Metadata-Version
 00000010: 3a20 322e 310a 4e61 6d65 3a20 6e76 6974  : 2.1.Name: nvit
 00000020: 6f70 0a56 6572 7369 6f6e 3a20 312e 312e  op.Version: 1.1.
-00000030: 300a 5375 6d6d 6172 793a 2041 6e20 696e  0.Summary: An in
+00000030: 310a 5375 6d6d 6172 793a 2041 6e20 696e  1.Summary: An in
 00000040: 7465 7261 6374 6976 6520 4e56 4944 4941  teractive NVIDIA
 00000050: 2d47 5055 2070 726f 6365 7373 2076 6965  -GPU process vie
 00000060: 7765 7220 616e 6420 6265 796f 6e64 2c20  wer and beyond, 
 00000070: 7468 6520 6f6e 652d 7374 6f70 2073 6f6c  the one-stop sol
 00000080: 7574 696f 6e20 666f 7220 4750 5520 7072  ution for GPU pr
 00000090: 6f63 6573 7320 6d61 6e61 6765 6d65 6e74  ocess management
 000000a0: 2e0a 4175 7468 6f72 2d65 6d61 696c 3a20  ..Author-email: 
@@ -796,15 +796,15 @@
 000031b0: 7468 6520 6c61 7465 7374 2076 6572 7369  the latest versi
 000031c0: 6f6e 2066 726f 6d20 4769 7448 7562 2028  on from GitHub (
 000031d0: 215b 436f 6d6d 6974 2043 6f75 6e74 5d28  ![Commit Count](
 000031e0: 6874 7470 733a 2f2f 696d 672e 7368 6965  https://img.shie
 000031f0: 6c64 732e 696f 2f67 6974 6875 622f 636f  lds.io/github/co
 00003200: 6d6d 6974 732d 7369 6e63 652f 5875 6568  mmits-since/Xueh
 00003210: 6169 5061 6e2f 6e76 6974 6f70 2f76 312e  aiPan/nvitop/v1.
-00003220: 312e 3029 293a 0a0a 6060 6062 6173 680a  1.0)):..```bash.
+00003220: 312e 3129 293a 0a0a 6060 6062 6173 680a  1.1)):..```bash.
 00003230: 7069 7033 2069 6e73 7461 6c6c 2067 6974  pip3 install git
 00003240: 2b68 7474 7073 3a2f 2f67 6974 6875 622e  +https://github.
 00003250: 636f 6d2f 5875 6568 6169 5061 6e2f 6e76  com/XuehaiPan/nv
 00003260: 6974 6f70 2e67 6974 2365 6767 3d6e 7669  itop.git#egg=nvi
 00003270: 746f 700a 6060 600a 0a4f 722c 2063 6c6f  top.```..Or, clo
 00003280: 6e65 2074 6869 7320 7265 706f 2061 6e64  ne this repo and
 00003290: 2069 6e73 7461 6c6c 206d 616e 7561 6c6c   install manuall
```

### Comparing `nvitop-1.1.0/README.md` & `nvitop-1.1.1/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -660,15 +660,15 @@
 00002930: 6c20 7468 6520 6c61 7465 7374 2076 6572  l the latest ver
 00002940: 7369 6f6e 2066 726f 6d20 4769 7448 7562  sion from GitHub
 00002950: 2028 215b 436f 6d6d 6974 2043 6f75 6e74   (![Commit Count
 00002960: 5d28 6874 7470 733a 2f2f 696d 672e 7368  ](https://img.sh
 00002970: 6965 6c64 732e 696f 2f67 6974 6875 622f  ields.io/github/
 00002980: 636f 6d6d 6974 732d 7369 6e63 652f 5875  commits-since/Xu
 00002990: 6568 6169 5061 6e2f 6e76 6974 6f70 2f76  ehaiPan/nvitop/v
-000029a0: 312e 312e 3029 293a 0a0a 6060 6062 6173  1.1.0)):..```bas
+000029a0: 312e 312e 3129 293a 0a0a 6060 6062 6173  1.1.1)):..```bas
 000029b0: 680a 7069 7033 2069 6e73 7461 6c6c 2067  h.pip3 install g
 000029c0: 6974 2b68 7474 7073 3a2f 2f67 6974 6875  it+https://githu
 000029d0: 622e 636f 6d2f 5875 6568 6169 5061 6e2f  b.com/XuehaiPan/
 000029e0: 6e76 6974 6f70 2e67 6974 2365 6767 3d6e  nvitop.git#egg=n
 000029f0: 7669 746f 700a 6060 600a 0a4f 722c 2063  vitop.```..Or, c
 00002a00: 6c6f 6e65 2074 6869 7320 7265 706f 2061  lone this repo a
 00002a10: 6e64 2069 6e73 7461 6c6c 206d 616e 7561  nd install manua
```

### Comparing `nvitop-1.1.0/nvitop/__init__.py` & `nvitop-1.1.1/nvitop/__init__.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/LICENSE` & `nvitop-1.1.1/nvitop/api/LICENSE`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/__init__.py` & `nvitop-1.1.1/nvitop/api/__init__.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/collector.py` & `nvitop-1.1.1/nvitop/api/collector.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/device.py` & `nvitop-1.1.1/nvitop/api/device.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/host.py` & `nvitop-1.1.1/nvitop/api/host.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/libcuda.py` & `nvitop-1.1.1/nvitop/api/libcuda.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/libcudart.py` & `nvitop-1.1.1/nvitop/api/libcudart.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/libnvml.py` & `nvitop-1.1.1/nvitop/api/libnvml.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/process.py` & `nvitop-1.1.1/nvitop/api/process.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/api/utils.py` & `nvitop-1.1.1/nvitop/api/utils.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/LICENSE` & `nvitop-1.1.1/nvitop/callbacks/LICENSE`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/__init__.py` & `nvitop-1.1.1/nvitop/callbacks/__init__.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/keras.py` & `nvitop-1.1.1/nvitop/callbacks/keras.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/lightning.py` & `nvitop-1.1.1/nvitop/callbacks/lightning.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/pytorch_lightning.py` & `nvitop-1.1.1/nvitop/callbacks/pytorch_lightning.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/tensorboard.py` & `nvitop-1.1.1/nvitop/callbacks/tensorboard.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/callbacks/utils.py` & `nvitop-1.1.1/nvitop/callbacks/utils.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/cli.py` & `nvitop-1.1.1/nvitop/cli.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/COPYING` & `nvitop-1.1.1/nvitop/gui/COPYING`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/__init__.py` & `nvitop-1.1.1/nvitop/gui/library/__init__.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/device.py` & `nvitop-1.1.1/nvitop/gui/library/device.py`

 * *Files 6% similar despite different names*

```diff
@@ -76,14 +76,28 @@
 
     @property
     def snapshot(self) -> Snapshot:
         if self._snapshot is None:
             self.as_snapshot()
         return self._snapshot
 
+    def mig_devices(self):
+        mig_devices = []
+
+        if self.is_mig_mode_enabled():
+            for mig_index in range(self.max_mig_device_count()):
+                try:
+                    mig_device = MigDevice(index=(self.index, mig_index))
+                except libnvml.NVMLError:
+                    break
+                else:
+                    mig_devices.append(mig_device)
+
+        return mig_devices
+
     fan_speed = ttl_cache(ttl=5.0)(DeviceBase.fan_speed)
     temperature = ttl_cache(ttl=5.0)(DeviceBase.temperature)
     power_usage = ttl_cache(ttl=5.0)(DeviceBase.power_usage)
     display_active = ttl_cache(ttl=5.0)(DeviceBase.display_active)
     display_mode = ttl_cache(ttl=5.0)(DeviceBase.display_mode)
     current_driver_model = ttl_cache(ttl=5.0)(DeviceBase.current_driver_model)
     persistence_mode = ttl_cache(ttl=5.0)(DeviceBase.persistence_mode)
```

### Comparing `nvitop-1.1.0/nvitop/gui/library/displayable.py` & `nvitop-1.1.1/nvitop/gui/library/displayable.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/history.py` & `nvitop-1.1.1/nvitop/gui/library/history.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/keybinding.py` & `nvitop-1.1.1/nvitop/gui/library/keybinding.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/libcurses.py` & `nvitop-1.1.1/nvitop/gui/library/libcurses.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/messagebox.py` & `nvitop-1.1.1/nvitop/gui/library/messagebox.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/mouse.py` & `nvitop-1.1.1/nvitop/gui/library/mouse.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/process.py` & `nvitop-1.1.1/nvitop/gui/library/process.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/selection.py` & `nvitop-1.1.1/nvitop/gui/library/selection.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/utils.py` & `nvitop-1.1.1/nvitop/gui/library/utils.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/library/widestring.py` & `nvitop-1.1.1/nvitop/gui/library/widestring.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/environ.py` & `nvitop-1.1.1/nvitop/gui/screens/environ.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/help.py` & `nvitop-1.1.1/nvitop/gui/screens/help.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/main/__init__.py` & `nvitop-1.1.1/nvitop/gui/screens/main/__init__.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/main/device.py` & `nvitop-1.1.1/nvitop/gui/screens/main/device.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/main/host.py` & `nvitop-1.1.1/nvitop/gui/screens/main/host.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/main/process.py` & `nvitop-1.1.1/nvitop/gui/screens/main/process.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/metrics.py` & `nvitop-1.1.1/nvitop/gui/screens/metrics.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/screens/treeview.py` & `nvitop-1.1.1/nvitop/gui/screens/treeview.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/gui/ui.py` & `nvitop-1.1.1/nvitop/gui/ui.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/select.py` & `nvitop-1.1.1/nvitop/select.py`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop/version.py` & `nvitop-1.1.1/nvitop/version.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 # ==============================================================================
 """An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management."""
 
-__version__ = '1.1.0'
+__version__ = '1.1.1'
 __license__ = 'GPLv3'
 __author__ = __maintainer__ = 'Xuehai Pan'
 __email__ = 'XuehaiPan@pku.edu.cn'
 __release__ = True
 
 if not __release__:
     import os
```

### Comparing `nvitop-1.1.0/nvitop.egg-info/PKG-INFO` & `nvitop-1.1.1/nvitop.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 00000000: 4d65 7461 6461 7461 2d56 6572 7369 6f6e  Metadata-Version
 00000010: 3a20 322e 310a 4e61 6d65 3a20 6e76 6974  : 2.1.Name: nvit
 00000020: 6f70 0a56 6572 7369 6f6e 3a20 312e 312e  op.Version: 1.1.
-00000030: 300a 5375 6d6d 6172 793a 2041 6e20 696e  0.Summary: An in
+00000030: 310a 5375 6d6d 6172 793a 2041 6e20 696e  1.Summary: An in
 00000040: 7465 7261 6374 6976 6520 4e56 4944 4941  teractive NVIDIA
 00000050: 2d47 5055 2070 726f 6365 7373 2076 6965  -GPU process vie
 00000060: 7765 7220 616e 6420 6265 796f 6e64 2c20  wer and beyond, 
 00000070: 7468 6520 6f6e 652d 7374 6f70 2073 6f6c  the one-stop sol
 00000080: 7574 696f 6e20 666f 7220 4750 5520 7072  ution for GPU pr
 00000090: 6f63 6573 7320 6d61 6e61 6765 6d65 6e74  ocess management
 000000a0: 2e0a 4175 7468 6f72 2d65 6d61 696c 3a20  ..Author-email: 
@@ -796,15 +796,15 @@
 000031b0: 7468 6520 6c61 7465 7374 2076 6572 7369  the latest versi
 000031c0: 6f6e 2066 726f 6d20 4769 7448 7562 2028  on from GitHub (
 000031d0: 215b 436f 6d6d 6974 2043 6f75 6e74 5d28  ![Commit Count](
 000031e0: 6874 7470 733a 2f2f 696d 672e 7368 6965  https://img.shie
 000031f0: 6c64 732e 696f 2f67 6974 6875 622f 636f  lds.io/github/co
 00003200: 6d6d 6974 732d 7369 6e63 652f 5875 6568  mmits-since/Xueh
 00003210: 6169 5061 6e2f 6e76 6974 6f70 2f76 312e  aiPan/nvitop/v1.
-00003220: 312e 3029 293a 0a0a 6060 6062 6173 680a  1.0)):..```bash.
+00003220: 312e 3129 293a 0a0a 6060 6062 6173 680a  1.1)):..```bash.
 00003230: 7069 7033 2069 6e73 7461 6c6c 2067 6974  pip3 install git
 00003240: 2b68 7474 7073 3a2f 2f67 6974 6875 622e  +https://github.
 00003250: 636f 6d2f 5875 6568 6169 5061 6e2f 6e76  com/XuehaiPan/nv
 00003260: 6974 6f70 2e67 6974 2365 6767 3d6e 7669  itop.git#egg=nvi
 00003270: 746f 700a 6060 600a 0a4f 722c 2063 6c6f  top.```..Or, clo
 00003280: 6e65 2074 6869 7320 7265 706f 2061 6e64  ne this repo and
 00003290: 2069 6e73 7461 6c6c 206d 616e 7561 6c6c   install manuall
```

### Comparing `nvitop-1.1.0/nvitop.egg-info/SOURCES.txt` & `nvitop-1.1.1/nvitop.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/nvitop.egg-info/requires.txt` & `nvitop-1.1.1/nvitop.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/pyproject.toml` & `nvitop-1.1.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `nvitop-1.1.0/setup.py` & `nvitop-1.1.1/setup.py`

 * *Files identical despite different names*

