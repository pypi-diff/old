# Comparing `tmp/kiss_icp-0.2.3.tar.gz` & `tmp/kiss_icp-0.2.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kiss_icp-0.2.3.tar", last modified: Sun Mar 26 09:20:14 2023, max compression
+gzip compressed data, was "kiss_icp-0.2.5.tar", last modified: Thu Apr  6 16:45:05 2023, max compression
```

## Comparing `kiss_icp-0.2.3.tar` & `kiss_icp-0.2.5.tar`

### file list

```diff
@@ -1,62 +1,63 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/
--rw-r--r--   0 runner    (1001) docker     (123)     2019 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/CMakeLists.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3789 2023-03-26 09:20:14.942531 kiss_icp-0.2.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2692 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.934531 kiss_icp-0.2.3/kiss_icp/
--rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/kiss_icp/config/
--rw-r--r--   0 runner    (1001) docker     (123)     1225 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/config/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4007 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/config/parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/kiss_icp/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)     2605 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2761 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/apollo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3698 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/boreas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4192 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/generic.py
--rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/kitti.py
--rw-r--r--   0 runner    (1001) docker     (123)    16194 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/kitti_raw.py
--rw-r--r--   0 runner    (1001) docker     (123)     4379 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/mulran.py
--rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/ncd.py
--rw-r--r--   0 runner    (1001) docker     (123)     5254 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/nclt.py
--rw-r--r--   0 runner    (1001) docker     (123)     5667 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/nuscenes.py
--rw-r--r--   0 runner    (1001) docker     (123)     6297 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/ouster.py
--rw-r--r--   0 runner    (1001) docker     (123)     2896 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/paris_luco.py
--rw-r--r--   0 runner    (1001) docker     (123)     3586 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/rosbag.py
--rw-r--r--   0 runner    (1001) docker     (123)     3834 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/rosbag2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3556 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/datasets/tum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1891 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/deskew.py
--rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/kiss_icp.py
--rw-r--r--   0 runner    (1001) docker     (123)     2971 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     8580 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     1860 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/preprocess.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/kiss_icp/pybind/
--rw-r--r--   0 runner    (1001) docker     (123)     2218 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pybind/CMakeLists.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pybind/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5215 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pybind/kiss_icp_pybind.cpp
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/kiss_icp/pybind/pybind11/
--rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pybind/pybind11/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1358 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pybind/pybind11/pybind11.cmake
--rw-r--r--   0 runner    (1001) docker     (123)     5753 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/pybind/stl_vector_eigen.h
--rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/registration.py
--rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/threshold.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/kiss_icp/tools/
--rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6643 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/tools/cmd.py
--rw-r--r--   0 runner    (1001) docker     (123)     3082 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/tools/pipeline_results.py
--rw-r--r--   0 runner    (1001) docker     (123)     8064 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/tools/point_cloud2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1319 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/tools/progress_bar.py
--rw-r--r--   0 runner    (1001) docker     (123)     9045 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/tools/visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1427 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/kiss_icp/voxelization.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-26 09:20:14.938531 kiss_icp-0.2.3/kiss_icp.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3789 2023-03-26 09:20:14.000000 kiss_icp-0.2.3/kiss_icp.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-03-26 09:20:14.000000 kiss_icp-0.2.3/kiss_icp.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-26 09:20:14.000000 kiss_icp-0.2.3/kiss_icp.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-03-26 09:20:14.000000 kiss_icp-0.2.3/kiss_icp.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-26 09:20:14.000000 kiss_icp-0.2.3/kiss_icp.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-26 09:20:14.000000 kiss_icp-0.2.3/kiss_icp.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-03-26 09:20:14.942531 kiss_icp-0.2.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-03-26 09:20:02.000000 kiss_icp-0.2.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/
+-rw-r--r--   0 runner    (1001) docker     (123)     2019 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/CMakeLists.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3789 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2692 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.977389 kiss_icp-0.2.5/kiss_icp/
+-rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.977389 kiss_icp-0.2.5/kiss_icp/config/
+-rw-r--r--   0 runner    (1001) docker     (123)     1225 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/config/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4007 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/config/parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)     2605 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2761 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/apollo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3698 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/boreas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4192 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4566 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/kitti.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16194 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/kitti_raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3982 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/mcap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4379 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/mulran.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/ncd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5254 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/nclt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5667 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/nuscenes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6297 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/ouster.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2896 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/paris_luco.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3690 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/rosbag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3834 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/rosbag2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3556 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/tum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1891 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/deskew.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/kiss_icp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2971 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8587 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1860 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/preprocess.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/pybind/
+-rw-r--r--   0 runner    (1001) docker     (123)     2218 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/CMakeLists.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5215 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/kiss_icp_pybind.cpp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/pybind/pybind11/
+-rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/pybind11/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/pybind11/pybind11.cmake
+-rw-r--r--   0 runner    (1001) docker     (123)     5753 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/stl_vector_eigen.h
+-rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/registration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/threshold.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6643 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/cmd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3082 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/pipeline_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7523 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/point_cloud2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1319 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/progress_bar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9045 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1427 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/voxelization.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.977389 kiss_icp-0.2.5/kiss_icp.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3789 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1397 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/setup.py
```

### Comparing `kiss_icp-0.2.3/CMakeLists.txt` & `kiss_icp-0.2.5/CMakeLists.txt`

 * *Files 2% similar despite different names*

```diff
@@ -16,16 +16,16 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
-cmake_minimum_required(VERSION 3.16...3.24)
-project(kiss_icp_pybind VERSION 0.2.3 LANGUAGES CXX)
+cmake_minimum_required(VERSION 3.16...3.26)
+project(kiss_icp_pybind VERSION 0.2.5 LANGUAGES CXX)
 
 # Set build type
 set(CMAKE_BUILD_TYPE Release)
 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
 set(CMAKE_POSITION_INDEPENDENT_CODE ON)
 
 if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../cpp/kiss_icp/)
```

### Comparing `kiss_icp-0.2.3/LICENSE` & `kiss_icp-0.2.5/LICENSE`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/PKG-INFO` & `kiss_icp-0.2.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kiss_icp
-Version: 0.2.3
+Version: 0.2.5
 Summary: Simple yet effective 3D LiDAR-Odometry registration pipeline
 Home-page: https://github.com/PRBonn/kiss-icp
 Author: Ignacio Vizzo
 Author-email: ignaciovizzo@gmail.com
 License: MIT
 Keywords: SLAM,LiDAR,Odometry,Localization
 Classifier: Operating System :: Unix
```

### Comparing `kiss_icp-0.2.3/README.md` & `kiss_icp-0.2.5/README.md`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/__init__.py` & `kiss_icp-0.2.5/kiss_icp/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -16,8 +16,8 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
-__version__ = "0.2.3"
+__version__ = "0.2.5"
```

### Comparing `kiss_icp-0.2.3/kiss_icp/config/__init__.py` & `kiss_icp-0.2.5/kiss_icp/config/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/config/config.py` & `kiss_icp-0.2.5/kiss_icp/config/config.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/config/parser.py` & `kiss_icp-0.2.5/kiss_icp/config/parser.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/__init__.py` & `kiss_icp-0.2.5/kiss_icp/datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/apollo.py` & `kiss_icp-0.2.5/kiss_icp/datasets/apollo.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/boreas.py` & `kiss_icp-0.2.5/kiss_icp/datasets/boreas.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/generic.py` & `kiss_icp-0.2.5/kiss_icp/datasets/generic.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/kitti.py` & `kiss_icp-0.2.5/kiss_icp/datasets/kitti.py`

 * *Files 8% similar despite different names*

```diff
@@ -81,14 +81,18 @@
         n = poses.shape[0]
         poses = np.concatenate(
             (poses, np.zeros((n, 3), dtype=np.float32), np.ones((n, 1), dtype=np.float32)), axis=1
         )
         poses = poses.reshape((n, 4, 4))  # [N, 4, 4]
         return _lidar_pose_gt(poses)
 
+    def get_frames_timestamps(self) -> np.ndarray:
+        timestamps = np.loadtxt(os.path.join(self.kitti_sequence_dir, "times.txt")).reshape(-1, 1)
+        return timestamps
+
     @staticmethod
     def read_calib_file(file_path: str) -> dict:
         calib_dict = {}
         with open(file_path, "r") as calib_file:
             for line in calib_file.readlines():
                 tokens = line.split(" ")
                 if tokens[0] == "calib_time:":
```

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/kitti_raw.py` & `kiss_icp-0.2.5/kiss_icp/datasets/kitti_raw.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/mulran.py` & `kiss_icp-0.2.5/kiss_icp/datasets/mulran.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/ncd.py` & `kiss_icp-0.2.5/kiss_icp/datasets/ncd.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/nclt.py` & `kiss_icp-0.2.5/kiss_icp/datasets/nclt.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/nuscenes.py` & `kiss_icp-0.2.5/kiss_icp/datasets/nuscenes.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/ouster.py` & `kiss_icp-0.2.5/kiss_icp/datasets/ouster.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/paris_luco.py` & `kiss_icp-0.2.5/kiss_icp/datasets/paris_luco.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/rosbag.py` & `kiss_icp-0.2.5/kiss_icp/datasets/rosbag.py`

 * *Files 4% similar despite different names*

```diff
@@ -42,26 +42,30 @@
         self.bagfile = data_dir
         self.bag = rosbag.Bag(data_dir, mode="r")
         self.topic = self.check_topic(topic)
 
         # Get an iterable
         self.n_scans = self.bag.get_message_count(topic_filters=self.topic)
         self.msgs = self.bag.read_messages(topics=[self.topic])
+        self.timestamps = []
 
         # Visualization Options
         self.use_global_visualizer = True
 
     def __len__(self):
         return self.n_scans
 
     def __getitem__(self, idx):
-        # TODO: implemnt [idx], expose field_names
-        _, msg, _ = next(self.msgs)
+        _, msg, time = next(self.msgs)
+        self.timestamps.append(time.to_sec())
         return self.read_point_cloud(msg)
 
+    def get_frames_timestamps(self) -> list:
+        return self.timestamps
+
     def check_topic(self, topic: str) -> str:
         # when user specified the topic don't check
         if topic:
             return topic
 
         # Extract all PointCloud2 msg topics from the bagfile
         point_cloud_topics = [
```

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/rosbag2.py` & `kiss_icp-0.2.5/kiss_icp/datasets/rosbag2.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/datasets/tum.py` & `kiss_icp-0.2.5/kiss_icp/datasets/tum.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/deskew.py` & `kiss_icp-0.2.5/kiss_icp/deskew.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/kiss_icp.py` & `kiss_icp-0.2.5/kiss_icp/kiss_icp.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/mapping.py` & `kiss_icp-0.2.5/kiss_icp/mapping.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/metrics.py` & `kiss_icp-0.2.5/kiss_icp/metrics.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/pipeline.py` & `kiss_icp-0.2.5/kiss_icp/pipeline.py`

 * *Files 1% similar despite different names*

```diff
@@ -121,15 +121,15 @@
     def save_poses_tum_format(filename, poses, timestamps):
         def _to_tum_format(poses, timestamps):
             tum_data = []
             with contextlib.suppress(ValueError):
                 for idx in range(len(poses)):
                     tx, ty, tz = poses[idx][:3, -1].flatten()
                     qw, qx, qy, qz = Quaternion(matrix=poses[idx], atol=0.01).elements
-                    tum_data.append([timestamps[idx], tx, ty, tz, qx, qy, qz, qw])
+                    tum_data.append([float(timestamps[idx]), tx, ty, tz, qx, qy, qz, qw])
             return np.array(tum_data).astype(np.float64)
 
         np.savetxt(fname=f"{filename}_tum.txt", X=_to_tum_format(poses, timestamps), fmt="%.4f")
 
     def _calibrate_poses(self, poses):
         return (
             self._dataset.apply_calibration(poses)
```

### Comparing `kiss_icp-0.2.3/kiss_icp/preprocess.py` & `kiss_icp-0.2.5/kiss_icp/preprocess.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/pybind/CMakeLists.txt` & `kiss_icp-0.2.5/kiss_icp/pybind/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/pybind/__init__.py` & `kiss_icp-0.2.5/kiss_icp/pybind/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/pybind/kiss_icp_pybind.cpp` & `kiss_icp-0.2.5/kiss_icp/pybind/kiss_icp_pybind.cpp`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/pybind/pybind11/LICENSE` & `kiss_icp-0.2.5/kiss_icp/pybind/pybind11/LICENSE`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/pybind/pybind11/pybind11.cmake` & `kiss_icp-0.2.5/kiss_icp/pybind/pybind11/pybind11.cmake`

 * *Files 6% similar despite different names*

```diff
@@ -18,11 +18,10 @@
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 include(FetchContent)
 
-FetchContent_Declare(
-  ext_pybind11 PREFIX pybind11
-  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.10.0.tar.gz)
+FetchContent_Declare(ext_pybind11 PREFIX pybind11
+                     URL https://github.com/pybind/pybind11/archive/refs/tags/v2.10.0.tar.gz)
 FetchContent_MakeAvailable(ext_pybind11)
```

### Comparing `kiss_icp-0.2.3/kiss_icp/pybind/stl_vector_eigen.h` & `kiss_icp-0.2.5/kiss_icp/pybind/stl_vector_eigen.h`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/registration.py` & `kiss_icp-0.2.5/kiss_icp/registration.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/threshold.py` & `kiss_icp-0.2.5/kiss_icp/threshold.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/tools/__init__.py` & `kiss_icp-0.2.5/kiss_icp/tools/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/tools/cmd.py` & `kiss_icp-0.2.5/kiss_icp/tools/cmd.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/tools/pipeline_results.py` & `kiss_icp-0.2.5/kiss_icp/tools/pipeline_results.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/tools/point_cloud2.py` & `kiss_icp-0.2.5/kiss_icp/tools/point_cloud2.py`

 * *Files 8% similar despite different names*

```diff
@@ -75,36 +75,36 @@
             break
 
     points_structured = read_points(msg, field_names=field_names)
     points = np.column_stack(
         [points_structured["x"], points_structured["y"], points_structured["z"]]
     )
 
+    # Remove nan if any
+    points = points[~np.any(np.isnan(points), axis=1)]
+
     if t_field:
         timestamps = points_structured[t_field]
         timestamps = timestamps / np.max(timestamps) if t_field != "time" else timestamps
     else:
         timestamps = np.ones(points.shape[0])
     return points.astype(np.float64), timestamps
 
 
 def read_points(
     cloud: PointCloud2,
     field_names: Optional[List[str]] = None,
-    skip_nans: bool = False,
     uvs: Optional[Iterable] = None,
     reshape_organized_cloud: bool = False,
 ) -> np.ndarray:
     """
     Read points from a sensor_msgs.PointCloud2 message.
     :param cloud: The point cloud to read from sensor_msgs.PointCloud2.
     :param field_names: The names of fields to read. If None, read all fields.
                         (Type: Iterable, Default: None)
-    :param skip_nans: If True, then don't return any point with a NaN value.
-                      (Type: Bool, Default: False)
     :param uvs: If specified, then only return the points at the given
         coordinates. (Type: Iterable, Default: None)
     :param reshape_organized_cloud: Returns the array as an 2D organized point cloud if set.
     :return: Structured NumPy array containing all points.
     """
     # Cast bytes to numpy array
     points = np.ndarray(
@@ -121,24 +121,14 @@
         # Mask fields
         points = points[list(field_names)]
 
     # Swap array if byte order does not match
     if bool(sys.byteorder != "little") != bool(cloud.is_bigendian):
         points = points.byteswap(inplace=True)
 
-    # Check if we want to drop points with nan values
-    if skip_nans and not cloud.is_dense:
-        # Init mask which selects all points
-        not_nan_mask = np.ones(len(points), dtype=bool)
-        for field_name in points.dtype.names:
-            # Only keep points without any non values in the mask
-            not_nan_mask = np.logical_and(not_nan_mask, ~np.isnan(points[field_name]))
-        # Select these points
-        points = points[not_nan_mask]
-
     # Select points indexed by the uvs field
     if uvs is not None:
         # Don't convert to numpy array if it is already one
         if not isinstance(uvs, np.ndarray):
             uvs = np.fromiter(uvs, int)
         # Index requested points
         points = points[uvs]
```

### Comparing `kiss_icp-0.2.3/kiss_icp/tools/progress_bar.py` & `kiss_icp-0.2.5/kiss_icp/tools/progress_bar.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/tools/visualizer.py` & `kiss_icp-0.2.5/kiss_icp/tools/visualizer.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp/voxelization.py` & `kiss_icp-0.2.5/kiss_icp/voxelization.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.3/kiss_icp.egg-info/PKG-INFO` & `kiss_icp-0.2.5/kiss_icp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: kiss-icp
-Version: 0.2.3
+Version: 0.2.5
 Summary: Simple yet effective 3D LiDAR-Odometry registration pipeline
 Home-page: https://github.com/PRBonn/kiss-icp
 Author: Ignacio Vizzo
 Author-email: ignaciovizzo@gmail.com
 License: MIT
 Keywords: SLAM,LiDAR,Odometry,Localization
 Classifier: Operating System :: Unix
```

### Comparing `kiss_icp-0.2.3/kiss_icp.egg-info/SOURCES.txt` & `kiss_icp-0.2.5/kiss_icp.egg-info/SOURCES.txt`

 * *Files 13% similar despite different names*

```diff
@@ -26,14 +26,15 @@
 kiss_icp/config/parser.py
 kiss_icp/datasets/__init__.py
 kiss_icp/datasets/apollo.py
 kiss_icp/datasets/boreas.py
 kiss_icp/datasets/generic.py
 kiss_icp/datasets/kitti.py
 kiss_icp/datasets/kitti_raw.py
+kiss_icp/datasets/mcap.py
 kiss_icp/datasets/mulran.py
 kiss_icp/datasets/ncd.py
 kiss_icp/datasets/nclt.py
 kiss_icp/datasets/nuscenes.py
 kiss_icp/datasets/ouster.py
 kiss_icp/datasets/paris_luco.py
 kiss_icp/datasets/rosbag.py
```

### Comparing `kiss_icp-0.2.3/setup.cfg` & `kiss_icp-0.2.5/setup.cfg`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = kiss_icp
-version = 0.2.3
+version = 0.2.5
 author = Ignacio Vizzo
 author_email = ignaciovizzo@gmail.com
 description = Simple yet effective 3D LiDAR-Odometry registration pipeline
 long_description = file:README.md,
 long_description_content_type = text/markdown
 url = https://github.com/PRBonn/kiss-icp
 license = MIT
```

### Comparing `kiss_icp-0.2.3/setup.py` & `kiss_icp-0.2.5/setup.py`

 * *Files identical despite different names*

