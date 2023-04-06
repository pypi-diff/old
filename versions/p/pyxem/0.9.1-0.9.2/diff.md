# Comparing `tmp/pyxem-0.9.1.tar.gz` & `tmp/pyxem-0.9.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pyxem-0.9.1.tar", last modified: Tue Sep  3 13:25:52 2019, max compression
+gzip compressed data, was "dist/pyxem-0.9.2.tar", last modified: Fri Sep 13 12:00:40 2019, max compression
```

## Comparing `pyxem-0.9.1.tar` & `pyxem-0.9.2.tar`

### file list

```diff
@@ -1,103 +1,103 @@
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/
--rw-r--r--   0 pc494     (1000) pc494     (1000)    35141 2019-01-23 16:04:31.000000 pyxem-0.9.1/LICENSE
--rw-rw-r--   0 pc494     (1000) pc494     (1000)       16 2019-04-26 13:57:33.000000 pyxem-0.9.1/MANIFEST.in
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2433 2019-09-03 13:25:52.000000 pyxem-0.9.1/PKG-INFO
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1460 2019-07-24 14:55:30.000000 pyxem-0.9.1/README.rst
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2231 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/__init__.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/components/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/components/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3821 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/components/diffraction_component.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3896 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/components/scalable_reference_pattern.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/generators/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/generators/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    21397 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/generators/calibration_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     4557 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/generators/displacement_gradient_tensor_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    10851 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/generators/indexation_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    12321 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/generators/subpixelrefinement_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5640 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/generators/vdf_generator.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/io_plugins/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1898 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/io_plugins/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    20689 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/io_plugins/mib.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/libraries/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/libraries/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2574 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/libraries/calibration_library.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/signals/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3670 2019-09-03 09:35:00.000000 pyxem-0.9.1/pyxem/signals/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    12050 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/crystallographic_map.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5408 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/diffraction1d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    23559 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/diffraction2d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    10092 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/diffraction_vectors.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5615 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/electron_diffraction1d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     7028 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/electron_diffraction2d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     8838 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/signals/indexation_results.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3242 2019-09-03 09:35:00.000000 pyxem-0.9.1/pyxem/signals/tensor_field.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1108 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/signals/vdf_image.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5869 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/conftest.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/test_components/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_components/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2362 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_components/test_diffraction_component.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1871 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/tests/test_components/test_scalable_reference_pattern.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/test_generators/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_generators/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     9298 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/tests/test_generators/test_calibration_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5707 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/tests/test_generators/test_displacement_gradient_tensor_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     7003 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_generators/test_indexation_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5475 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/tests/test_generators/test_subpixelrefinement_generator.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     4278 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/tests/test_generators/test_vdf_generator.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/test_library/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_library/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2281 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_library/test_calibration_library.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/test_physical/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_physical/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2962 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_physical/test_marker_plotting.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3411 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/tests/test_physical/test_orientation_mapping_nonphys.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    11632 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_physical/test_orientation_mapping_phys.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2262 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/tests/test_physical/test_strain_mapping.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/test_signals/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_signals/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     8873 2019-05-09 15:00:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_crystallographic_map.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3107 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_diffraction1d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3101 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_diffraction2d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     6581 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_diffraction_vectors.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     4805 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_electron_diffraction1d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    17193 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_electron_diffraction2d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3100 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_indexation_results.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1038 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_diffraction1d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1032 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_diffraction2d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1019 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_electron_diffraction1d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1067 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_electron_diffraction2d.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5352 2019-08-16 12:54:08.000000 pyxem-0.9.1/pyxem/tests/test_signals/test_tensor_field.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/tests/test_utils/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_utils/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2693 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_calibration_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     5750 2019-09-03 09:35:00.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_expt_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     4330 2019-06-04 10:40:16.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_indexation_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     4158 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_io_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3185 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_peakfinders2D.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2380 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_subpixel_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3773 2019-06-04 10:40:16.000000 pyxem-0.9.1/pyxem/tests/test_utils/test_vector_utils.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem/utils/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-07-16 10:29:13.000000 pyxem-0.9.1/pyxem/utils/__init__.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     7654 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/utils/calibration_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    14242 2019-09-03 09:35:00.000000 pyxem-0.9.1/pyxem/utils/expt_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    21125 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/utils/indexation_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     6264 2019-09-03 11:23:19.000000 pyxem-0.9.1/pyxem/utils/io_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    11547 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/utils/peakfinder2D_gui.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)    12236 2019-09-03 09:35:28.000000 pyxem-0.9.1/pyxem/utils/peakfinders2D.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2645 2019-04-19 09:18:45.000000 pyxem-0.9.1/pyxem/utils/plot.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2430 2019-07-24 14:55:30.000000 pyxem-0.9.1/pyxem/utils/sim_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3147 2019-04-26 13:57:33.000000 pyxem-0.9.1/pyxem/utils/subpixel_refinements_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     1029 2019-06-28 12:30:08.000000 pyxem-0.9.1/pyxem/utils/vdf_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     8447 2019-07-24 14:55:00.000000 pyxem-0.9.1/pyxem/utils/vector_utils.py
--rw-rw-r--   0 pc494     (1000) pc494     (1000)      337 2019-09-03 09:48:33.000000 pyxem-0.9.1/pyxem/version.py
-drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem.egg-info/
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2433 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem.egg-info/PKG-INFO
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     3311 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem.egg-info/SOURCES.txt
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        1 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem.egg-info/dependency_links.txt
--rw-rw-r--   0 pc494     (1000) pc494     (1000)       95 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem.egg-info/requires.txt
--rw-rw-r--   0 pc494     (1000) pc494     (1000)        6 2019-09-03 13:25:52.000000 pyxem-0.9.1/pyxem.egg-info/top_level.txt
--rw-rw-r--   0 pc494     (1000) pc494     (1000)       38 2019-09-03 13:25:52.000000 pyxem-0.9.1/setup.cfg
--rw-rw-r--   0 pc494     (1000) pc494     (1000)     2142 2019-09-03 09:48:13.000000 pyxem-0.9.1/setup.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/
+-rw-r--r--   0 pc494     (1000) pc494     (1000)    35141 2019-01-23 16:04:31.000000 pyxem-0.9.2/LICENSE
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)       16 2019-04-26 13:57:33.000000 pyxem-0.9.2/MANIFEST.in
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2433 2019-09-13 12:00:40.000000 pyxem-0.9.2/PKG-INFO
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1460 2019-07-24 14:55:30.000000 pyxem-0.9.2/README.rst
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2231 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/__init__.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/components/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/components/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3821 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/components/diffraction_component.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3896 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/components/scalable_reference_pattern.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/generators/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/generators/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    21397 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/generators/calibration_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     4557 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/generators/displacement_gradient_tensor_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    10851 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/generators/indexation_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    12321 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/generators/subpixelrefinement_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5640 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/generators/vdf_generator.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/io_plugins/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1898 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/io_plugins/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    20689 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/io_plugins/mib.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/libraries/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/libraries/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2574 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/libraries/calibration_library.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/signals/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3670 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/signals/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    12050 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/signals/crystallographic_map.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5408 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/signals/diffraction1d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    23559 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/signals/diffraction2d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    10092 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/signals/diffraction_vectors.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5615 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/signals/electron_diffraction1d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     7028 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/signals/electron_diffraction2d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     8838 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/signals/indexation_results.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3242 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/signals/tensor_field.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1108 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/signals/vdf_image.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5869 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/conftest.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/test_components/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_components/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2362 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_components/test_diffraction_component.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1871 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/tests/test_components/test_scalable_reference_pattern.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/test_generators/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_generators/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     9298 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_generators/test_calibration_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5707 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_generators/test_displacement_gradient_tensor_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     7003 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_generators/test_indexation_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5475 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_generators/test_subpixelrefinement_generator.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     4278 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/tests/test_generators/test_vdf_generator.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/test_library/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_library/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2281 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_library/test_calibration_library.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/test_physical/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_physical/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2962 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_physical/test_marker_plotting.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3411 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_physical/test_orientation_mapping_nonphys.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    11632 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_physical/test_orientation_mapping_phys.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2262 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_physical/test_strain_mapping.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/test_signals/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_signals/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     8873 2019-05-09 15:00:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_crystallographic_map.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3107 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_diffraction1d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3101 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_diffraction2d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     6581 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_diffraction_vectors.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     4805 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_electron_diffraction1d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    17193 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_electron_diffraction2d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3100 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_indexation_results.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1038 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_diffraction1d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1032 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_diffraction2d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1019 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_electron_diffraction1d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1067 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_electron_diffraction2d.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5352 2019-08-16 12:54:08.000000 pyxem-0.9.2/pyxem/tests/test_signals/test_tensor_field.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/tests/test_utils/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        0 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_utils/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2693 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_calibration_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     5750 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_expt_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     4330 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_indexation_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     4158 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_io_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3185 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_peakfinders2D.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2380 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_subpixel_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3773 2019-06-04 10:40:16.000000 pyxem-0.9.2/pyxem/tests/test_utils/test_vector_utils.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem/utils/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)      714 2019-07-16 10:29:13.000000 pyxem-0.9.2/pyxem/utils/__init__.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     7654 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/utils/calibration_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    14242 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/utils/expt_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    21125 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/utils/indexation_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     6264 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/utils/io_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    11547 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/utils/peakfinder2D_gui.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)    12236 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/utils/peakfinders2D.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2645 2019-04-19 09:18:45.000000 pyxem-0.9.2/pyxem/utils/plot.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2430 2019-07-24 14:55:30.000000 pyxem-0.9.2/pyxem/utils/sim_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3147 2019-04-26 13:57:33.000000 pyxem-0.9.2/pyxem/utils/subpixel_refinements_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     1029 2019-06-28 12:30:08.000000 pyxem-0.9.2/pyxem/utils/vdf_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     8447 2019-07-24 14:55:00.000000 pyxem-0.9.2/pyxem/utils/vector_utils.py
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)      337 2019-09-13 11:46:57.000000 pyxem-0.9.2/pyxem/version.py
+drwxrwxr-x   0 pc494     (1000) pc494     (1000)        0 2019-09-13 12:00:40.000000 pyxem-0.9.2/pyxem.egg-info/
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2433 2019-09-13 12:00:39.000000 pyxem-0.9.2/pyxem.egg-info/PKG-INFO
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     3311 2019-09-13 12:00:39.000000 pyxem-0.9.2/pyxem.egg-info/SOURCES.txt
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        1 2019-09-13 12:00:39.000000 pyxem-0.9.2/pyxem.egg-info/dependency_links.txt
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)       83 2019-09-13 12:00:39.000000 pyxem-0.9.2/pyxem.egg-info/requires.txt
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)        6 2019-09-13 12:00:39.000000 pyxem-0.9.2/pyxem.egg-info/top_level.txt
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)       38 2019-09-13 12:00:40.000000 pyxem-0.9.2/setup.cfg
+-rw-rw-r--   0 pc494     (1000) pc494     (1000)     2109 2019-09-13 11:46:57.000000 pyxem-0.9.2/setup.py
```

### Comparing `pyxem-0.9.1/LICENSE` & `pyxem-0.9.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/PKG-INFO` & `pyxem-0.9.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: pyxem
-Version: 0.9.1
+Version: 0.9.2
 Summary: Crystallographic Diffraction Microscopy in Python.
 Home-page: https://github.com/pyxem/pyxem
 Author: Duncan Johnstone
 Author-email: dnj23@cam.ac.uk
 License: GPLv3
 Description: |Travis|_ |AppVeyor|_ |Coveralls|_ |pypi_version|_  |doi|_
```

### Comparing `pyxem-0.9.1/README.rst` & `pyxem-0.9.2/README.rst`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/__init__.py` & `pyxem-0.9.2/pyxem/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/components/__init__.py` & `pyxem-0.9.2/pyxem/components/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/components/diffraction_component.py` & `pyxem-0.9.2/pyxem/components/diffraction_component.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/components/scalable_reference_pattern.py` & `pyxem-0.9.2/pyxem/components/scalable_reference_pattern.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/generators/__init__.py` & `pyxem-0.9.2/pyxem/generators/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/generators/calibration_generator.py` & `pyxem-0.9.2/pyxem/generators/calibration_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/generators/displacement_gradient_tensor_generator.py` & `pyxem-0.9.2/pyxem/generators/displacement_gradient_tensor_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/generators/indexation_generator.py` & `pyxem-0.9.2/pyxem/generators/indexation_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/generators/subpixelrefinement_generator.py` & `pyxem-0.9.2/pyxem/generators/subpixelrefinement_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/generators/vdf_generator.py` & `pyxem-0.9.2/pyxem/generators/vdf_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/io_plugins/__init__.py` & `pyxem-0.9.2/pyxem/io_plugins/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/io_plugins/mib.py` & `pyxem-0.9.2/pyxem/io_plugins/mib.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/libraries/__init__.py` & `pyxem-0.9.2/pyxem/libraries/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/libraries/calibration_library.py` & `pyxem-0.9.2/pyxem/libraries/calibration_library.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/__init__.py` & `pyxem-0.9.2/pyxem/signals/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/crystallographic_map.py` & `pyxem-0.9.2/pyxem/signals/crystallographic_map.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/diffraction1d.py` & `pyxem-0.9.2/pyxem/signals/diffraction1d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/diffraction2d.py` & `pyxem-0.9.2/pyxem/signals/diffraction2d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/diffraction_vectors.py` & `pyxem-0.9.2/pyxem/signals/diffraction_vectors.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/electron_diffraction1d.py` & `pyxem-0.9.2/pyxem/signals/electron_diffraction1d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/electron_diffraction2d.py` & `pyxem-0.9.2/pyxem/signals/electron_diffraction2d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/indexation_results.py` & `pyxem-0.9.2/pyxem/signals/indexation_results.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/tensor_field.py` & `pyxem-0.9.2/pyxem/signals/tensor_field.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/signals/vdf_image.py` & `pyxem-0.9.2/pyxem/signals/vdf_image.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/__init__.py` & `pyxem-0.9.2/pyxem/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/conftest.py` & `pyxem-0.9.2/pyxem/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_components/test_diffraction_component.py` & `pyxem-0.9.2/pyxem/tests/test_components/test_diffraction_component.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_components/test_scalable_reference_pattern.py` & `pyxem-0.9.2/pyxem/tests/test_components/test_scalable_reference_pattern.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_generators/test_calibration_generator.py` & `pyxem-0.9.2/pyxem/tests/test_generators/test_calibration_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_generators/test_displacement_gradient_tensor_generator.py` & `pyxem-0.9.2/pyxem/tests/test_generators/test_displacement_gradient_tensor_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_generators/test_indexation_generator.py` & `pyxem-0.9.2/pyxem/tests/test_generators/test_indexation_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_generators/test_subpixelrefinement_generator.py` & `pyxem-0.9.2/pyxem/tests/test_generators/test_subpixelrefinement_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_generators/test_vdf_generator.py` & `pyxem-0.9.2/pyxem/tests/test_generators/test_vdf_generator.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_library/test_calibration_library.py` & `pyxem-0.9.2/pyxem/tests/test_library/test_calibration_library.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_physical/test_marker_plotting.py` & `pyxem-0.9.2/pyxem/tests/test_physical/test_marker_plotting.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_physical/test_orientation_mapping_nonphys.py` & `pyxem-0.9.2/pyxem/tests/test_physical/test_orientation_mapping_nonphys.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_physical/test_orientation_mapping_phys.py` & `pyxem-0.9.2/pyxem/tests/test_physical/test_orientation_mapping_phys.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_physical/test_strain_mapping.py` & `pyxem-0.9.2/pyxem/tests/test_physical/test_strain_mapping.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_crystallographic_map.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_crystallographic_map.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_diffraction1d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_diffraction1d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_diffraction2d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_diffraction2d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_diffraction_vectors.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_diffraction_vectors.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_electron_diffraction1d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_electron_diffraction1d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_electron_diffraction2d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_electron_diffraction2d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_indexation_results.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_indexation_results.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_diffraction1d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_diffraction1d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_diffraction2d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_diffraction2d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_electron_diffraction1d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_electron_diffraction1d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_lazy_electron_diffraction2d.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_lazy_electron_diffraction2d.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_signals/test_tensor_field.py` & `pyxem-0.9.2/pyxem/tests/test_signals/test_tensor_field.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_calibration_utils.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_calibration_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_expt_utils.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_expt_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_indexation_utils.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_indexation_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_io_utils.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_io_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_peakfinders2D.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_peakfinders2D.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_subpixel_utils.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_subpixel_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/tests/test_utils/test_vector_utils.py` & `pyxem-0.9.2/pyxem/tests/test_utils/test_vector_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/__init__.py` & `pyxem-0.9.2/pyxem/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/calibration_utils.py` & `pyxem-0.9.2/pyxem/utils/calibration_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/expt_utils.py` & `pyxem-0.9.2/pyxem/utils/expt_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/indexation_utils.py` & `pyxem-0.9.2/pyxem/utils/indexation_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/io_utils.py` & `pyxem-0.9.2/pyxem/utils/io_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/peakfinder2D_gui.py` & `pyxem-0.9.2/pyxem/utils/peakfinder2D_gui.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/peakfinders2D.py` & `pyxem-0.9.2/pyxem/utils/peakfinders2D.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/plot.py` & `pyxem-0.9.2/pyxem/utils/plot.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/sim_utils.py` & `pyxem-0.9.2/pyxem/utils/sim_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/subpixel_refinements_utils.py` & `pyxem-0.9.2/pyxem/utils/subpixel_refinements_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/vdf_utils.py` & `pyxem-0.9.2/pyxem/utils/vdf_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem/utils/vector_utils.py` & `pyxem-0.9.2/pyxem/utils/vector_utils.py`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/pyxem.egg-info/PKG-INFO` & `pyxem-0.9.2/pyxem.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: pyxem
-Version: 0.9.1
+Version: 0.9.2
 Summary: Crystallographic Diffraction Microscopy in Python.
 Home-page: https://github.com/pyxem/pyxem
 Author: Duncan Johnstone
 Author-email: dnj23@cam.ac.uk
 License: GPLv3
 Description: |Travis|_ |AppVeyor|_ |Coveralls|_ |pypi_version|_  |doi|_
```

### Comparing `pyxem-0.9.1/pyxem.egg-info/SOURCES.txt` & `pyxem-0.9.2/pyxem.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pyxem-0.9.1/setup.py` & `pyxem-0.9.2/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -46,16 +46,15 @@
 
     packages=find_packages(),
     # adjust the tabbing
     install_requires=[
       'scikit-image >= 0.15.0',   # exclude_border argument in peak_finder laplacian (PR #436)
       'matplotlib >= 3.1.1' ,     # 3.1.0 failed
       'scikit-learn >= 0.19',     # reason unknown
-      'hyperspy >= 1.3',          # 1.2 fails, (NTU Workshop - May 2019)
-      'diffsims',
-      'numpy == 1.16.5'           # as discussed in #466
+      'hyperspy >= 1.5.2',        # freeing up our numpy version, see Release Notes for hyperspy.
+      'diffsims'
       ],
     package_data={
         "": ["LICENSE", "readme.rst",],
         "pyxem": ["*.py"],
     },
 )
```

