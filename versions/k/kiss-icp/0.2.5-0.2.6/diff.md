# Comparing `tmp/kiss_icp-0.2.5.tar.gz` & `tmp/kiss_icp-0.2.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kiss_icp-0.2.5.tar", last modified: Thu Apr  6 16:45:05 2023, max compression
+gzip compressed data, was "kiss_icp-0.2.6.tar", last modified: Fri Apr  7 13:17:13 2023, max compression
```

## Comparing `kiss_icp-0.2.5.tar` & `kiss_icp-0.2.6.tar`

### file list

```diff
@@ -1,63 +1,62 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/
--rw-r--r--   0 runner    (1001) docker     (123)     2019 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/CMakeLists.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3789 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2692 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.977389 kiss_icp-0.2.5/kiss_icp/
--rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.977389 kiss_icp-0.2.5/kiss_icp/config/
--rw-r--r--   0 runner    (1001) docker     (123)     1225 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/config/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4007 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/config/parser.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)     2605 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2761 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/apollo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3698 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/boreas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4192 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/generic.py
--rw-r--r--   0 runner    (1001) docker     (123)     4566 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/kitti.py
--rw-r--r--   0 runner    (1001) docker     (123)    16194 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/kitti_raw.py
--rw-r--r--   0 runner    (1001) docker     (123)     3982 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/mcap.py
--rw-r--r--   0 runner    (1001) docker     (123)     4379 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/mulran.py
--rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/ncd.py
--rw-r--r--   0 runner    (1001) docker     (123)     5254 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/nclt.py
--rw-r--r--   0 runner    (1001) docker     (123)     5667 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/nuscenes.py
--rw-r--r--   0 runner    (1001) docker     (123)     6297 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/ouster.py
--rw-r--r--   0 runner    (1001) docker     (123)     2896 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/paris_luco.py
--rw-r--r--   0 runner    (1001) docker     (123)     3690 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/rosbag.py
--rw-r--r--   0 runner    (1001) docker     (123)     3834 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/rosbag2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3556 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/datasets/tum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1891 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/deskew.py
--rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/kiss_icp.py
--rw-r--r--   0 runner    (1001) docker     (123)     2971 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/metrics.py
--rw-r--r--   0 runner    (1001) docker     (123)     8587 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pipeline.py
--rw-r--r--   0 runner    (1001) docker     (123)     1860 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/preprocess.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/pybind/
--rw-r--r--   0 runner    (1001) docker     (123)     2218 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/CMakeLists.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5215 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/kiss_icp_pybind.cpp
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/pybind/pybind11/
--rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/pybind11/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/pybind11/pybind11.cmake
--rw-r--r--   0 runner    (1001) docker     (123)     5753 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/pybind/stl_vector_eigen.h
--rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/registration.py
--rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/threshold.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/kiss_icp/tools/
--rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6643 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/cmd.py
--rw-r--r--   0 runner    (1001) docker     (123)     3082 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/pipeline_results.py
--rw-r--r--   0 runner    (1001) docker     (123)     7523 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/point_cloud2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1319 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/progress_bar.py
--rw-r--r--   0 runner    (1001) docker     (123)     9045 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/tools/visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)     1427 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/kiss_icp/voxelization.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:45:05.977389 kiss_icp-0.2.5/kiss_icp.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3789 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1397 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 16:45:05.000000 kiss_icp-0.2.5/kiss_icp.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 16:45:05.981389 kiss_icp-0.2.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-04-06 16:44:54.000000 kiss_icp-0.2.5/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/
+-rw-r--r--   0 runner    (1001) docker     (123)     2019 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/CMakeLists.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1126 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5829 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4732 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.424140 kiss_icp-0.2.6/kiss_icp/
+-rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.424140 kiss_icp-0.2.6/kiss_icp/config/
+-rw-r--r--   0 runner    (1001) docker     (123)     1225 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/config/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4007 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/config/parser.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/kiss_icp/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)     2605 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2761 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/apollo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3698 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/boreas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4192 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4566 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/kitti.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16194 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/kitti_raw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4469 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/mcap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4379 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/mulran.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4276 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/ncd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5254 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/nclt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5667 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/nuscenes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6297 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/ouster.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2896 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/paris_luco.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4892 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/rosbag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3556 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/datasets/tum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1891 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/deskew.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3917 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/kiss_icp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2971 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1819 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/metrics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8587 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pipeline.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1860 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/preprocess.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/kiss_icp/pybind/
+-rw-r--r--   0 runner    (1001) docker     (123)     2218 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pybind/CMakeLists.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pybind/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5215 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pybind/kiss_icp_pybind.cpp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/kiss_icp/pybind/pybind11/
+-rw-r--r--   0 runner    (1001) docker     (123)     1684 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pybind/pybind11/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1374 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pybind/pybind11/pybind11.cmake
+-rw-r--r--   0 runner    (1001) docker     (123)     5753 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/pybind/stl_vector_eigen.h
+-rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/registration.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2307 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/threshold.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/kiss_icp/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)     1166 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7959 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/tools/cmd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3082 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/tools/pipeline_results.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7427 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/tools/point_cloud2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1319 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/tools/progress_bar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9045 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/tools/visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1427 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/kiss_icp/voxelization.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:17:13.424140 kiss_icp-0.2.6/kiss_icp.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5829 2023-04-07 13:17:13.000000 kiss_icp-0.2.6/kiss_icp.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1368 2023-04-07 13:17:13.000000 kiss_icp-0.2.6/kiss_icp.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:17:13.000000 kiss_icp-0.2.6/kiss_icp.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-07 13:17:13.000000 kiss_icp-0.2.6/kiss_icp.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-07 13:17:13.000000 kiss_icp-0.2.6/kiss_icp.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 13:17:13.000000 kiss_icp-0.2.6/kiss_icp.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-07 13:17:13.428140 kiss_icp-0.2.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     3115 2023-04-07 13:17:01.000000 kiss_icp-0.2.6/setup.py
```

### Comparing `kiss_icp-0.2.5/CMakeLists.txt` & `kiss_icp-0.2.6/CMakeLists.txt`

 * *Files 2% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 cmake_minimum_required(VERSION 3.16...3.26)
-project(kiss_icp_pybind VERSION 0.2.5 LANGUAGES CXX)
+project(kiss_icp_pybind VERSION 0.2.6 LANGUAGES CXX)
 
 # Set build type
 set(CMAKE_BUILD_TYPE Release)
 set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
 set(CMAKE_POSITION_INDEPENDENT_CODE ON)
 
 if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/../cpp/kiss_icp/)
```

### Comparing `kiss_icp-0.2.5/LICENSE` & `kiss_icp-0.2.6/LICENSE`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/__init__.py` & `kiss_icp-0.2.6/kiss_icp/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -16,8 +16,8 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
-__version__ = "0.2.5"
+__version__ = "0.2.6"
```

### Comparing `kiss_icp-0.2.5/kiss_icp/config/__init__.py` & `kiss_icp-0.2.6/kiss_icp/config/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/config/config.py` & `kiss_icp-0.2.6/kiss_icp/config/config.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/config/parser.py` & `kiss_icp-0.2.6/kiss_icp/config/parser.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/__init__.py` & `kiss_icp-0.2.6/kiss_icp/datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/apollo.py` & `kiss_icp-0.2.6/kiss_icp/datasets/apollo.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/boreas.py` & `kiss_icp-0.2.6/kiss_icp/datasets/boreas.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/generic.py` & `kiss_icp-0.2.6/kiss_icp/datasets/generic.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/kitti.py` & `kiss_icp-0.2.6/kiss_icp/datasets/kitti.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/kitti_raw.py` & `kiss_icp-0.2.6/kiss_icp/datasets/kitti_raw.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/mcap.py` & `kiss_icp-0.2.6/kiss_icp/datasets/mcap.py`

 * *Files 23% similar despite different names*

```diff
@@ -35,16 +35,16 @@
             print("mcap plugins not installed: 'pip install mcap-ros2-support'")
             exit(1)
 
         from kiss_icp.tools.point_cloud2 import read_point_cloud
 
         # we expect `data_dir` param to be a path to the .mcap file, so rename for clarity
         assert os.path.isfile(data_dir), "mcap dataloader expects an existing MCAP file"
+        self.sequence_id = os.path.basename(data_dir).split(".")[0]
         mcap_file = str(data_dir)
-        self.data_dir = os.path.dirname(data_dir)
 
         self.bag = make_reader(open(mcap_file, "rb"))
         self.summary = self.bag.get_summary()
         self.topic = self.check_topic(topic)
         self.n_scans = self._get_n_scans()
         self.msgs = read_ros2_messages(mcap_file, topics=topic)
         self.read_point_cloud = read_point_cloud
@@ -65,33 +65,47 @@
         return sum(
             count
             for (id, count) in self.summary.statistics.channel_message_counts.items()
             if self.summary.channels[id].topic == self.topic
         )
 
     def check_topic(self, topic: str) -> str:
-        # when user specified the topic don't check
-        if topic:
-            return topic
-
         # Extract schema id from the .mcap file that encodes the PointCloud2 msg
         schema_id = [
             schema.id
             for schema in self.summary.schemas.values()
             if schema.name == "sensor_msgs/msg/PointCloud2"
         ][0]
 
-        point_cloud_channels = [
-            channel for channel in self.summary.channels.values() if channel.schema_id == schema_id
+        point_cloud_topics = [
+            channel.topic
+            for channel in self.summary.channels.values()
+            if channel.schema_id == schema_id
         ]
-        if len(point_cloud_channels) == 0:
-            print("[ERROR] Your mcap does not contain any sensor_msgs/msg/PointCloud2 topic")
-        if len(point_cloud_channels) == 1:
-            return point_cloud_channels[0].topic
-        if len(point_cloud_channels) > 1:
-            print("Multiple sensor_msgs/msg/PointCloud2 topics available.")
-            print("Please select one of the following topics with the --topic flag")
+
+        def print_available_topics_and_exit():
             print(50 * "-")
-            for channel in point_cloud_channels:
-                print(f"--topic {channel.topic}")
+            for t in point_cloud_topics:
+                print(f"--topic {t}")
             print(50 * "-")
-        sys.exit(1)
+            sys.exit(1)
+
+        if topic and topic in point_cloud_topics:
+            return topic
+        # when user specified the topic check that exists
+        if topic and topic not in point_cloud_topics:
+            print(
+                f'[ERROR] Dataset does not containg any msg with the topic name "{topic}". '
+                "Please select one of the following topics with the --topic flag"
+            )
+            print_available_topics_and_exit()
+        if len(point_cloud_topics) > 1:
+            print(
+                "Multiple sensor_msgs/msg/PointCloud2 topics available."
+                "Please select one of the following topics with the --topic flag"
+            )
+            print_available_topics_and_exit()
+
+        if len(point_cloud_topics) == 0:
+            print("[ERROR] Your dataset does not contain any sensor_msgs/msg/PointCloud2 topic")
+        if len(point_cloud_topics) == 1:
+            return point_cloud_topics[0]
```

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/mulran.py` & `kiss_icp-0.2.6/kiss_icp/datasets/mulran.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/ncd.py` & `kiss_icp-0.2.6/kiss_icp/datasets/ncd.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/nclt.py` & `kiss_icp-0.2.6/kiss_icp/datasets/nclt.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/nuscenes.py` & `kiss_icp-0.2.6/kiss_icp/datasets/nuscenes.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/ouster.py` & `kiss_icp-0.2.6/kiss_icp/datasets/ouster.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/paris_luco.py` & `kiss_icp-0.2.6/kiss_icp/datasets/paris_luco.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/rosbag.py` & `kiss_icp-0.2.6/kiss_icp/datasets/rosbag.py`

 * *Files 22% similar despite different names*

```diff
@@ -19,76 +19,107 @@
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
 import os
 from pathlib import Path
 import sys
+from typing import Sequence
+
+import natsort
 
 
 class RosbagDataset:
-    def __init__(self, data_dir: Path, topic: str, *_, **__):
+    def __init__(self, data_dir: Sequence[Path], topic: str, *_, **__):
+        """ROS1 / ROS2 bagfile dataloader.
+
+        It can take either one ROS2 bag file or one or more ROS1 bag files belonging to a split bag.
+        The reader will replay ROS1 split bags in correct timestamp order.
+
+        TODO: Merge mcap and rosbag dataloaders into 1
+        """
         try:
-            import rosbag
+            from rosbags.highlevel import AnyReader
         except ModuleNotFoundError:
-            print('python rosbag is not installed, run "sudo apt install python3-rosbag"')
+            print('rosbags library not installed, run "pip install -U rosbags"')
             sys.exit(1)
 
         from kiss_icp.tools.point_cloud2 import read_point_cloud
 
         self.read_point_cloud = read_point_cloud
-        self.sequence_id = os.path.basename(data_dir).split(".")[0]
 
-        # bagfile
-        self.bagfile = data_dir
-        self.bag = rosbag.Bag(data_dir, mode="r")
+        # FIXME: This is quite hacky, trying to guess if we have multiple .bag, one or a dir
+        if isinstance(data_dir, Path):
+            self.sequence_id = os.path.basename(data_dir).split(".")[0]
+            self.bag = AnyReader([data_dir])
+        else:
+            self.sequence_id = os.path.basename(data_dir[0]).split(".")[0]
+            self.bag = AnyReader(data_dir)
+            print("Reading multiple .bag files in directory:")
+            print("\n".join(natsort.natsorted([path.name for path in self.bag.paths])))
+        self.bag.open()
         self.topic = self.check_topic(topic)
+        self.n_scans = self.bag.topics[self.topic].msgcount
 
-        # Get an iterable
-        self.n_scans = self.bag.get_message_count(topic_filters=self.topic)
-        self.msgs = self.bag.read_messages(topics=[self.topic])
+        # limit connections to selected topic
+        connections = [x for x in self.bag.connections if x.topic == self.topic]
+        self.msgs = self.bag.messages(connections=connections)
         self.timestamps = []
 
         # Visualization Options
         self.use_global_visualizer = True
 
+    def __del__(self):
+        if hasattr(self, "bag"):
+            self.bag.close()
+
     def __len__(self):
         return self.n_scans
 
     def __getitem__(self, idx):
-        _, msg, time = next(self.msgs)
-        self.timestamps.append(time.to_sec())
+        connection, timestamp, rawdata = next(self.msgs)
+        self.timestamps.append(self.to_sec(timestamp))
+        msg = self.bag.deserialize(rawdata, connection.msgtype)
         return self.read_point_cloud(msg)
 
+    @staticmethod
+    def to_sec(nsec: int):
+        return float(nsec) / 1e9
+
     def get_frames_timestamps(self) -> list:
         return self.timestamps
 
     def check_topic(self, topic: str) -> str:
-        # when user specified the topic don't check
-        if topic:
-            return topic
-
         # Extract all PointCloud2 msg topics from the bagfile
         point_cloud_topics = [
-            topic
-            for topic in self.bag.get_type_and_topic_info().topics.items()
-            if topic[1].msg_type == "sensor_msgs/PointCloud2"
+            topic[0]
+            for topic in self.bag.topics.items()
+            if topic[1].msgtype == "sensor_msgs/msg/PointCloud2"
         ]
 
-        if len(point_cloud_topics) == 1:
-            # this is the string topic name, go figure out
-            return point_cloud_topics[0][0]
+        def print_available_topics_and_exit():
+            print(50 * "-")
+            for t in point_cloud_topics:
+                print(f"--topic {t}")
+            print(50 * "-")
+            sys.exit(1)
 
-        # In any other case we consider this an error
-        if len(point_cloud_topics) == 0:
-            print("[ERROR] Your bagfile does not contain any sensor_msgs/PointCloud2 topic")
+        if topic and topic in point_cloud_topics:
+            return topic
+        # when user specified the topic check that exists
+        if topic and topic not in point_cloud_topics:
+            print(
+                f'[ERROR] Dataset does not containg any msg with the topic name "{topic}". '
+                "Please select one of the following topics with the --topic flag"
+            )
+            print_available_topics_and_exit()
         if len(point_cloud_topics) > 1:
-            print("Multiple sensor_msgs/PointCloud2 topics available.")
-            print("Please provide one of the following topics with the --topic flag")
-            for topic_tuple in point_cloud_topics:
-                print(50 * "-")
-                print(f"Topic   {topic_tuple[0]}")
-                print(f"\tType      {topic_tuple[1].msg_type}")
-                print(f"\tMessages  {topic_tuple[1].message_count}")
-                print(f"\tFrequency {topic_tuple[1].frequency}")
-            print(50 * "-")
-        sys.exit(1)
+            print(
+                "Multiple sensor_msgs/msg/PointCloud2 topics available."
+                "Please select one of the following topics with the --topic flag"
+            )
+            print_available_topics_and_exit()
+
+        if len(point_cloud_topics) == 0:
+            print("[ERROR] Your dataset does not contain any sensor_msgs/msg/PointCloud2 topic")
+        if len(point_cloud_topics) == 1:
+            return point_cloud_topics[0]
```

### Comparing `kiss_icp-0.2.5/kiss_icp/datasets/tum.py` & `kiss_icp-0.2.6/kiss_icp/datasets/tum.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/deskew.py` & `kiss_icp-0.2.6/kiss_icp/deskew.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/kiss_icp.py` & `kiss_icp-0.2.6/kiss_icp/kiss_icp.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/mapping.py` & `kiss_icp-0.2.6/kiss_icp/mapping.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/metrics.py` & `kiss_icp-0.2.6/kiss_icp/metrics.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pipeline.py` & `kiss_icp-0.2.6/kiss_icp/pipeline.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/preprocess.py` & `kiss_icp-0.2.6/kiss_icp/preprocess.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pybind/CMakeLists.txt` & `kiss_icp-0.2.6/kiss_icp/pybind/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pybind/__init__.py` & `kiss_icp-0.2.6/kiss_icp/pybind/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pybind/kiss_icp_pybind.cpp` & `kiss_icp-0.2.6/kiss_icp/pybind/kiss_icp_pybind.cpp`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pybind/pybind11/LICENSE` & `kiss_icp-0.2.6/kiss_icp/pybind/pybind11/LICENSE`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pybind/pybind11/pybind11.cmake` & `kiss_icp-0.2.6/kiss_icp/pybind/pybind11/pybind11.cmake`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/pybind/stl_vector_eigen.h` & `kiss_icp-0.2.6/kiss_icp/pybind/stl_vector_eigen.h`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/registration.py` & `kiss_icp-0.2.6/kiss_icp/registration.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/threshold.py` & `kiss_icp-0.2.6/kiss_icp/threshold.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/tools/__init__.py` & `kiss_icp-0.2.6/kiss_icp/tools/__init__.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/tools/cmd.py` & `kiss_icp-0.2.6/kiss_icp/tools/cmd.py`

 * *Files 15% similar despite different names*

```diff
@@ -16,26 +16,53 @@
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 # SOFTWARE.
+import glob
+import os
 from pathlib import Path
 from typing import Optional
 
 import typer
 
 from kiss_icp.datasets import (
     available_dataloaders,
     sequence_dataloaders,
     supported_file_extensions,
 )
 
 
+def guess_dataloader(data: Path, default_dataloader: str):
+    """Guess which dataloader to use in case the user didn't specify with --dataloader flag.
+
+    TODO: Avoid having to return again the data Path. But when guessing multiple .bag files or the
+    metadata.yaml file, we need to change the Path specifed by the user.
+    """
+    if data.is_file():
+        if data.name == "metadata.yaml":
+            return "rosbag", data.parent  # database is in directory, not in .yml
+        if data.name.split(".")[-1] in "bag":
+            return "rosbag", data
+        if data.name.split(".")[-1] == "pcap":
+            return "ouster", data
+        if data.name.split(".")[-1] == "mcap":
+            return "mcap", data
+    elif data.is_dir():
+        if (data / "metadata.yaml").exists():
+            # a directory with a metadata.yaml must be a ROS2 bagfile
+            return "rosbag", data
+        bagfiles = [Path(path) for path in glob.glob(os.path.join(data, "*.bag"))]
+        if len(bagfiles) > 0:
+            return "rosbag", bagfiles
+    return default_dataloader
+
+
 def version_callback(value: bool):
     if value:
         import kiss_icp
 
         print(f"KISS-ICP Version: {kiss_icp.__version__}")
         raise typer.Exit()
 
@@ -45,29 +72,35 @@
     if value not in dl:
         raise typer.BadParameter(f"Supported dataloaders are:\n{', '.join(dl)}")
     return value
 
 
 app = typer.Typer(add_completion=False, rich_markup_mode="rich")
 
-# Remove the clutter for the help
+# Remove from the help those dataloaders we explicitly say how to use
 _available_dl_help = available_dataloaders()
 _available_dl_help.remove("generic")
+_available_dl_help.remove("mcap")
+_available_dl_help.remove("ouster")
+_available_dl_help.remove("rosbag")
 
 docstring = f"""
 :kiss: KISS-ICP, a simple yet effective LiDAR-Odometry estimation pipeline :kiss:\n
 \b
 [bold green]Examples: [/bold green]
 # Process all pointclouds in the given <data-dir> \[{", ".join(supported_file_extensions())}]
 $ kiss_icp_pipeline --visualize <data-dir>:open_file_folder:
 
-# Process a given rosbag file
-$ kiss_icp_pipeline --topic /cloud_node --visualize <path-to-my-rosbag.bag>:page_facing_up:
+# Process a given [bold]ROS1/ROS2 [/bold]rosbag file (directory:open_file_folder:, ".bag":page_facing_up:, or "metadata.yaml":page_facing_up:)
+$ kiss_icp_pipeline --visualize <path-to-my-rosbag>[:open_file_folder:/:page_facing_up:]
+
+# Process [bold]mcap [/bold] recording
+$ kiss_icp_pipeline --visualize <path-to-file.mcap>:page_facing_up:
 
-# Process Ouster pcap recording (requires ouster-sdk Python package installed)
+# Process [bold]Ouster pcap[/bold] recording (requires ouster-sdk Python package installed)
 $ kiss_icp_pipeline --visualize <path-to-ouster.pcap>:page_facing_up: \[--meta <path-to-metadata.json>:page_facing_up:]
 
 # Use a more specific dataloader: {", ".join(_available_dl_help)}
 $ kiss_icp_pipeline --dataloader kitti --sequence 07 --visualize <path-to-kitti-root>:open_file_folder:
 """
 
 
@@ -164,21 +197,16 @@
     ),
 ):
     # Validate some options
     if dataloader in sequence_dataloaders() and sequence is None:
         print('You must specify a sequence "--sequence"')
         raise typer.Exit(code=1)
 
-    if data.is_file():
-        # Check if the main source is a bagfile, then automatically fallback to RosbagDataset
-        if data.name.split(".")[-1] == "bag":
-            dataloader = "rosbag"
-        # or to Ouster pcap dataloader
-        elif data.name.split(".")[-1] == "pcap":
-            dataloader = "ouster"
+    # Attempt to guess some common file extensions to avoid using the --dataloader flag
+    dataloader, data = guess_dataloader(data, default_dataloader="generic")
 
     # Lazy-loading for faster CLI
     from kiss_icp.datasets import dataset_factory
     from kiss_icp.pipeline import OdometryPipeline
 
     OdometryPipeline(
         dataset=dataset_factory(
```

### Comparing `kiss_icp-0.2.5/kiss_icp/tools/pipeline_results.py` & `kiss_icp-0.2.6/kiss_icp/tools/pipeline_results.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/tools/point_cloud2.py` & `kiss_icp-0.2.6/kiss_icp/tools/point_cloud2.py`

 * *Files 4% similar despite different names*

```diff
@@ -28,25 +28,23 @@
 
 """
 This file is based on https://github.com/ros2/common_interfaces/blob/4bac182a0a582b5e6b784d9fa9f0dabc1aca4d35/sensor_msgs_py/sensor_msgs_py/point_cloud2.py
 All rights reserved to the original authors: Tim Field and Florian Vahl.
 """
 
 import sys
+from typing import Iterable, List, Optional, Tuple
+
 import numpy as np
-from typing import Iterable, Optional, List, Tuple
 
 try:
     from rosbags.typesys.types import sensor_msgs__msg__PointField as PointField
     from rosbags.typesys.types import sensor_msgs__msg__PointCloud2 as PointCloud2
-except ImportError:
-    try:
-        from sensor_msgs.msg import PointCloud2, PointField
-    except ImportError as e:
-        raise ImportError("Neither 'rosbags' nor 'sensor_msgs' was found on pythonpath") from e
+except ImportError as e:
+    raise ImportError('rosbags library not installed, run "pip install -U rosbags"') from e
 
 
 _DATATYPES = {}
 _DATATYPES[PointField.INT8] = np.dtype(np.int8)
 _DATATYPES[PointField.UINT8] = np.dtype(np.uint8)
 _DATATYPES[PointField.INT16] = np.dtype(np.int16)
 _DATATYPES[PointField.UINT16] = np.dtype(np.uint16)
```

### Comparing `kiss_icp-0.2.5/kiss_icp/tools/progress_bar.py` & `kiss_icp-0.2.6/kiss_icp/tools/progress_bar.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/tools/visualizer.py` & `kiss_icp-0.2.6/kiss_icp/tools/visualizer.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp/voxelization.py` & `kiss_icp-0.2.6/kiss_icp/voxelization.py`

 * *Files identical despite different names*

### Comparing `kiss_icp-0.2.5/kiss_icp.egg-info/SOURCES.txt` & `kiss_icp-0.2.6/kiss_icp.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -34,15 +34,14 @@
 kiss_icp/datasets/mulran.py
 kiss_icp/datasets/ncd.py
 kiss_icp/datasets/nclt.py
 kiss_icp/datasets/nuscenes.py
 kiss_icp/datasets/ouster.py
 kiss_icp/datasets/paris_luco.py
 kiss_icp/datasets/rosbag.py
-kiss_icp/datasets/rosbag2.py
 kiss_icp/datasets/tum.py
 kiss_icp/pybind/CMakeLists.txt
 kiss_icp/pybind/__init__.py
 kiss_icp/pybind/kiss_icp_pybind.cpp
 kiss_icp/pybind/stl_vector_eigen.h
 kiss_icp/pybind/pybind11/LICENSE
 kiss_icp/pybind/pybind11/pybind11.cmake
```

### Comparing `kiss_icp-0.2.5/setup.cfg` & `kiss_icp-0.2.6/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = kiss_icp
-version = 0.2.5
+version = 0.2.6
 author = Ignacio Vizzo
 author_email = ignaciovizzo@gmail.com
 description = Simple yet effective 3D LiDAR-Odometry registration pipeline
 long_description = file:README.md,
 long_description_content_type = text/markdown
 url = https://github.com/PRBonn/kiss-icp
 license = MIT
```

### Comparing `kiss_icp-0.2.5/setup.py` & `kiss_icp-0.2.6/setup.py`

 * *Files identical despite different names*

