# Comparing `tmp/kikuchipy-0.8.3.tar.gz` & `tmp/kikuchipy-0.8.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "kikuchipy-0.8.3.tar", last modified: Thu Mar 23 11:01:39 2023, max compression
+gzip compressed data, was "kikuchipy-0.8.4.tar", last modified: Fri Apr  7 13:46:12 2023, max compression
```

## Comparing `kikuchipy-0.8.3.tar` & `kikuchipy-0.8.4.tar`

### file list

```diff
@@ -1,261 +1,261 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.090846 kikuchipy-0.8.3/
--rw-r--r--   0 runner    (1001) docker     (123)    51549 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/CHANGELOG.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7406 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/CODE_OF_CONDUCT.rst
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (123)    35141 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      290 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     9488 2023-03-23 11:01:39.090846 kikuchipy-0.8.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7887 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     3540 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/RELEASE.rst
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/environment.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.062846 kikuchipy-0.8.3/kikuchipy/
--rw-r--r--   0 runner    (1001) docker     (123)     3980 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.062846 kikuchipy-0.8.3/kikuchipy/_rotation/
--rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_rotation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.062846 kikuchipy-0.8.3/kikuchipy/_rotation/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_rotation/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_rotation/tests/test_rotation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.062846 kikuchipy-0.8.3/kikuchipy/_util/
--rw-r--r--   0 runner    (1001) docker     (123)     1100 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5622 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/_deprecated.py
--rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/_transfer_axes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.062846 kikuchipy-0.8.3/kikuchipy/_util/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5319 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/tests/test_deprecated.py
--rw-r--r--   0 runner    (1001) docker     (123)    10912 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/tests/test_import.py
--rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/_util/tests/test_logging.py
--rw-r--r--   0 runner    (1001) docker     (123)    14809 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.066846 kikuchipy-0.8.3/kikuchipy/data/
--rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27984 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     9147 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/_registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.066846 kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/
--rw-r--r--   0 runner    (1001) docker     (123)    16614 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/create_bruker_h5ebsd_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    73176 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/patterns.h5
--rw-r--r--   0 runner    (1001) docker     (123)    59696 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/patterns_roi.h5
--rw-r--r--   0 runner    (1001) docker     (123)    55824 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/patterns_roi_nonrectangular.h5
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.066846 kikuchipy-0.8.3/kikuchipy/data/edax_binary/
--rw-r--r--   0 runner    (1001) docker     (123)     2460 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/edax_binary/create_dummy_edax_binary_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    32416 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/edax_binary/edax_binary.up1
--rw-r--r--   0 runner    (1001) docker     (123)    72042 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/edax_binary/edax_binary.up2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.066846 kikuchipy-0.8.3/kikuchipy/data/edax_h5ebsd/
--rw-r--r--   0 runner    (1001) docker     (123)   938661 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/edax_h5ebsd/patterns.h5
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.066846 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/
--rw-r--r--   0 runner    (1001) docker     (123)   351168 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/EBSD_TEST_Ni.h5
--rw-r--r--   0 runner    (1001) docker     (123)     2724 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/create_dummy_emsoft_ebsd_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    35624 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/simulated_ebsd.h5
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/
--rw-r--r--   0 runner    (1001) docker     (123)      506 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/BetheParameters.nml
--rw-r--r--   0 runner    (1001) docker     (123)     2480 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/convert_emsoft_ebsd_masterpattern_file_uint8_gzip.py
--rw-r--r--   0 runner    (1001) docker     (123)     2669 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/create_dummy_emsoft_ebsd_master_pattern_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    61872 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/master_patterns.h5
--rw-r--r--   0 runner    (1001) docker     (123)    12680 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni.xtal
--rw-r--r--   0 runner    (1001) docker     (123)     1658 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_ebsdmaster.nml
--rw-r--r--   0 runner    (1001) docker     (123)    19638 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc.out
--rw-r--r--   0 runner    (1001) docker     (123)   908492 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc_mp_20kv_uint8_gzip_opts9.h5
--rw-r--r--   0 runner    (1001) docker     (123)     2109 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mcopencl.nml
--rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mp.out
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/emsoft_ecp_master_pattern/
--rw-r--r--   0 runner    (1001) docker     (123)     2572 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ecp_master_pattern/create_dummy_emsoft_ecp_master_pattern_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    62296 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_ecp_master_pattern/ecp_master_pattern.h5
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/emsoft_tkd_master_pattern/
--rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_tkd_master_pattern/create_dummy_emsoft_tkd_master_pattern_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    61600 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/emsoft_tkd_master_pattern/tkd_master_pattern.h5
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/kikuchipy_h5ebsd/
--rw-r--r--   0 runner    (1001) docker     (123)   149400 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/kikuchipy_h5ebsd/patterns.h5
--rw-r--r--   0 runner    (1001) docker     (123)    46480 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/kikuchipy_h5ebsd/patterns_nochunks.h5
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/nordif/
--rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Background acquisition pattern.bmp
--rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Background calibration pattern.bmp
--rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Calibration (294,532).bmp
--rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Calibration (425,447).bmp
--rw-r--r--   0 runner    (1001) docker     (123)    32400 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Pattern.dat
--rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Setting.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1460 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Setting_bad1.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Setting_bad2.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1580 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/nordif/Setting_bad3.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/oxford_binary/
--rw-r--r--   0 runner    (1001) docker     (123)     2487 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/oxford_binary/create_dummy_oxford_binary_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    32786 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/oxford_binary/patterns.ebsp
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.070846 kikuchipy-0.8.3/kikuchipy/data/oxford_h5ebsd/
--rw-r--r--   0 runner    (1001) docker     (123)     4902 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/oxford_h5ebsd/create_oxford_h5ebsd_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    59152 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/oxford_h5ebsd/patterns.h5oina
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/data/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/data/tests/test_data.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/detectors/
--rw-r--r--   0 runner    (1001) docker     (123)     1435 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/detectors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14225 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/detectors/calibration.py
--rw-r--r--   0 runner    (1001) docker     (123)    67124 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/detectors/ebsd_detector.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/detectors/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/detectors/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4691 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/detectors/tests/test_calibration.py
--rw-r--r--   0 runner    (1001) docker     (123)    39863 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/detectors/tests/test_ebsd_detector.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/draw/
--rw-r--r--   0 runner    (1001) docker     (123)     1454 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1947 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/_navigators.py
--rw-r--r--   0 runner    (1001) docker     (123)     4944 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/_plot_pattern_positions_in_map.py
--rw-r--r--   0 runner    (1001) docker     (123)     1237 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/colors.py
--rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/markers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/draw/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1067 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/tests/test_colors.py
--rw-r--r--   0 runner    (1001) docker     (123)    10741 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/tests/test_markers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/tests/test_navigators.py
--rw-r--r--   0 runner    (1001) docker     (123)     5101 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/draw/tests/test_plot_pattern_positions_in_map.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/filters/
--rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/filters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5915 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/filters/fft_barnes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/filters/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/filters/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5895 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/filters/tests/test_fft_barnes.py
--rw-r--r--   0 runner    (1001) docker     (123)    15640 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/filters/tests/test_window.py
--rw-r--r--   0 runner    (1001) docker     (123)    17866 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/filters/window.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/generators/
--rw-r--r--   0 runner    (1001) docker     (123)     1410 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/generators/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/generators/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/generators/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10012 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/generators/tests/test_virtual_bse_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    13349 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/generators/virtual_bse_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     2188 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/hyperspy_extension.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/imaging/
--rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/imaging/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.074846 kikuchipy-0.8.3/kikuchipy/imaging/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/imaging/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9960 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/imaging/tests/test_virtual_bse_imager.py
--rw-r--r--   0 runner    (1001) docker     (123)    16325 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/imaging/vbse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.078846 kikuchipy-0.8.3/kikuchipy/indexing/
--rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7893 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_dictionary_indexing.py
--rw-r--r--   0 runner    (1001) docker     (123)    12343 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_hough_indexing.py
--rw-r--r--   0 runner    (1001) docker     (123)    13895 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_merge_crystal_maps.py
--rw-r--r--   0 runner    (1001) docker     (123)     5356 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_orientation_similarity_map.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.078846 kikuchipy-0.8.3/kikuchipy/indexing/_refinement/
--rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_refinement/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6589 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_refinement/_objective_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)    43952 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_refinement/_refinement.py
--rw-r--r--   0 runner    (1001) docker     (123)    21304 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/_refinement/_solvers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.078846 kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/
--rw-r--r--   0 runner    (1001) docker     (123)     1141 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8146 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/_normalized_cross_correlation.py
--rw-r--r--   0 runner    (1001) docker     (123)     6297 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/_normalized_dot_product.py
--rw-r--r--   0 runner    (1001) docker     (123)     8831 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/_similarity_metric.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.078846 kikuchipy-0.8.3/kikuchipy/indexing/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7741 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/tests/test_dictionary_indexing.py
--rw-r--r--   0 runner    (1001) docker     (123)    39413 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/tests/test_ebsd_refinement.py
--rw-r--r--   0 runner    (1001) docker     (123)    22250 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/tests/test_merge_crystal_maps.py
--rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/tests/test_orientation_similarity_map.py
--rw-r--r--   0 runner    (1001) docker     (123)     2034 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/indexing/tests/test_similarity_metrics.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.078846 kikuchipy-0.8.3/kikuchipy/io/
--rw-r--r--   0 runner    (1001) docker     (123)     1217 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14667 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/_util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.082846 kikuchipy-0.8.3/kikuchipy/io/plugins/
--rw-r--r--   0 runner    (1001) docker     (123)     1750 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10790 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/_emsoft_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)    16167 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     8571 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/bruker_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     6490 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/ebsd_directory.py
--rw-r--r--   0 runner    (1001) docker     (123)     8266 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/edax_binary.py
--rw-r--r--   0 runner    (1001) docker     (123)     6762 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/edax_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     6682 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     3103 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_ebsd_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     3091 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_ecp_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     3100 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_tkd_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)    17736 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/kikuchipy_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)    14826 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/nordif.py
--rw-r--r--   0 runner    (1001) docker     (123)     3873 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/nordif_calibration_patterns.py
--rw-r--r--   0 runner    (1001) docker     (123)    19627 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/oxford_binary.py
--rw-r--r--   0 runner    (1001) docker     (123)     7276 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/oxford_h5ebsd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.082846 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      923 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2076 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_bruker_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_ebsd_directory.py
--rw-r--r--   0 runner    (1001) docker     (123)     3326 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_edax_binary.py
--rw-r--r--   0 runner    (1001) docker     (123)     2116 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_edax_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     4002 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)     4388 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_ebsd_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     1378 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_ecp_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     4587 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     1454 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_tkd_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)    14640 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_kikuchipy_h5ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)    13546 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_nordif.py
--rw-r--r--   0 runner    (1001) docker     (123)     3803 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_nordif_calibration_patterns.py
--rw-r--r--   0 runner    (1001) docker     (123)     4514 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_oxford_binary.py
--rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_oxford_h5ebsd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.082846 kikuchipy-0.8.3/kikuchipy/io/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5374 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/tests/test_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     2105 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/io/tests/test_util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.082846 kikuchipy-0.8.3/kikuchipy/pattern/
--rw-r--r--   0 runner    (1001) docker     (123)     1913 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/pattern/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    25808 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/pattern/_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     5411 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/pattern/chunk.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.082846 kikuchipy-0.8.3/kikuchipy/pattern/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/pattern/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6248 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/pattern/tests/test_chunk.py
--rw-r--r--   0 runner    (1001) docker     (123)    18683 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/pattern/tests/test_pattern.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.086846 kikuchipy-0.8.3/kikuchipy/projections/
--rw-r--r--   0 runner    (1001) docker     (123)     1829 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3772 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/gnomonic_projection.py
--rw-r--r--   0 runner    (1001) docker     (123)     2882 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/hesse_normal_form.py
--rw-r--r--   0 runner    (1001) docker     (123)     6081 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/lambert_projection.py
--rw-r--r--   0 runner    (1001) docker     (123)     4557 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/spherical_projection.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.086846 kikuchipy-0.8.3/kikuchipy/projections/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3627 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/tests/test_gnomonic_projection.py
--rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/tests/test_hesse_normal_form.py
--rw-r--r--   0 runner    (1001) docker     (123)     5392 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/tests/test_lambert_projection.py
--rw-r--r--   0 runner    (1001) docker     (123)     2316 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/projections/tests/test_spherical_projection.py
--rw-r--r--   0 runner    (1001) docker     (123)     1296 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/release.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.086846 kikuchipy-0.8.3/kikuchipy/signals/
--rw-r--r--   0 runner    (1001) docker     (123)     2042 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13111 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/_kikuchi_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)    22408 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/_kikuchipy_signal.py
--rw-r--r--   0 runner    (1001) docker     (123)   131049 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)    18279 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/ebsd_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     6670 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/ecp_master_pattern.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.086846 kikuchipy-0.8.3/kikuchipy/signals/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    87955 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/test_ebsd.py
--rw-r--r--   0 runner    (1001) docker     (123)    12409 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/test_ebsd_hough_indexing.py
--rw-r--r--   0 runner    (1001) docker     (123)    27376 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/test_ebsd_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     6329 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/test_ecp_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/test_kikuchi_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     5180 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/tests/test_virtual_bse_image.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.086846 kikuchipy-0.8.3/kikuchipy/signals/util/
--rw-r--r--   0 runner    (1001) docker     (123)     1520 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5685 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/_crystal_map.py
--rw-r--r--   0 runner    (1001) docker     (123)    11236 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/_dask.py
--rw-r--r--   0 runner    (1001) docker     (123)     1932 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)    10639 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/_map_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)    22702 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/_master_pattern.py
--rw-r--r--   0 runner    (1001) docker     (123)     3140 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/_overwrite_hyperspy_methods.py
--rw-r--r--   0 runner    (1001) docker     (123)     3537 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/array_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.090846 kikuchipy-0.8.3/kikuchipy/signals/util/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2343 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/tests/test_array_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     5001 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/tests/test_dask.py
--rw-r--r--   0 runner    (1001) docker     (123)     2503 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/util/tests/test_overwrite_hyperspy_methods.py
--rw-r--r--   0 runner    (1001) docker     (123)     3972 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/signals/virtual_bse_image.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.090846 kikuchipy-0.8.3/kikuchipy/simulations/
--rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/_kikuchi_pattern_features.py
--rw-r--r--   0 runner    (1001) docker     (123)    26644 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/_kikuchi_pattern_simulation.py
--rw-r--r--   0 runner    (1001) docker     (123)    27443 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/kikuchi_pattern_simulator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.090846 kikuchipy-0.8.3/kikuchipy/simulations/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      708 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11778 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/tests/test_kikuchi_pattern_simulation.py
--rw-r--r--   0 runner    (1001) docker     (123)    14664 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/kikuchipy/simulations/tests/test_kikuchi_pattern_simulator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-23 11:01:39.062846 kikuchipy-0.8.3/kikuchipy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     9488 2023-03-23 11:01:39.000000 kikuchipy-0.8.3/kikuchipy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8949 2023-03-23 11:01:39.000000 kikuchipy-0.8.3/kikuchipy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-23 11:01:39.000000 kikuchipy-0.8.3/kikuchipy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       44 2023-03-23 11:01:39.000000 kikuchipy-0.8.3/kikuchipy.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-03-23 11:01:39.000000 kikuchipy-0.8.3/kikuchipy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-03-23 11:01:39.000000 kikuchipy-0.8.3/kikuchipy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-23 11:01:38.000000 kikuchipy-0.8.3/kikuchipy.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      837 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/readthedocs.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      879 2023-03-23 11:01:39.090846 kikuchipy-0.8.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     6144 2023-03-23 11:01:27.000000 kikuchipy-0.8.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.219895 kikuchipy-0.8.4/
+-rw-r--r--   0 runner    (1001) docker     (123)    52167 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/CHANGELOG.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     7406 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/CODE_OF_CONDUCT.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/CONTRIBUTING.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    35141 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      290 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     9502 2023-04-07 13:46:12.219895 kikuchipy-0.8.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7889 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     3540 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/RELEASE.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/environment.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.171895 kikuchipy-0.8.4/kikuchipy/
+-rw-r--r--   0 runner    (1001) docker     (123)     3980 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy/_rotation/
+-rw-r--r--   0 runner    (1001) docker     (123)     4455 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_rotation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy/_rotation/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_rotation/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_rotation/tests/test_rotation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy/_util/
+-rw-r--r--   0 runner    (1001) docker     (123)     1100 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5622 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/_deprecated.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1618 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/_transfer_axes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy/_util/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5319 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/tests/test_deprecated.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10912 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/tests/test_import.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/_util/tests/test_logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14809 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy/data/
+-rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27984 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9147 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/_registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/
+-rw-r--r--   0 runner    (1001) docker     (123)    16614 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/create_bruker_h5ebsd_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    73176 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/patterns.h5
+-rw-r--r--   0 runner    (1001) docker     (123)    59696 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/patterns_roi.h5
+-rw-r--r--   0 runner    (1001) docker     (123)    55824 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/patterns_roi_nonrectangular.h5
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.179895 kikuchipy-0.8.4/kikuchipy/data/edax_binary/
+-rw-r--r--   0 runner    (1001) docker     (123)     2460 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/edax_binary/create_dummy_edax_binary_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32416 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/edax_binary/edax_binary.up1
+-rw-r--r--   0 runner    (1001) docker     (123)    72042 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/edax_binary/edax_binary.up2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.179895 kikuchipy-0.8.4/kikuchipy/data/edax_h5ebsd/
+-rw-r--r--   0 runner    (1001) docker     (123)   938661 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/edax_h5ebsd/patterns.h5
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.179895 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/
+-rw-r--r--   0 runner    (1001) docker     (123)   351168 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/EBSD_TEST_Ni.h5
+-rw-r--r--   0 runner    (1001) docker     (123)     2724 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/create_dummy_emsoft_ebsd_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35624 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/simulated_ebsd.h5
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.183895 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/
+-rw-r--r--   0 runner    (1001) docker     (123)      506 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/BetheParameters.nml
+-rw-r--r--   0 runner    (1001) docker     (123)     2480 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/convert_emsoft_ebsd_masterpattern_file_uint8_gzip.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2669 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/create_dummy_emsoft_ebsd_master_pattern_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61872 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/master_patterns.h5
+-rw-r--r--   0 runner    (1001) docker     (123)    12680 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni.xtal
+-rw-r--r--   0 runner    (1001) docker     (123)     1658 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_ebsdmaster.nml
+-rw-r--r--   0 runner    (1001) docker     (123)    19638 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc.out
+-rw-r--r--   0 runner    (1001) docker     (123)   908492 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc_mp_20kv_uint8_gzip_opts9.h5
+-rw-r--r--   0 runner    (1001) docker     (123)     2109 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mcopencl.nml
+-rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mp.out
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.183895 kikuchipy-0.8.4/kikuchipy/data/emsoft_ecp_master_pattern/
+-rw-r--r--   0 runner    (1001) docker     (123)     2572 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ecp_master_pattern/create_dummy_emsoft_ecp_master_pattern_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    62296 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_ecp_master_pattern/ecp_master_pattern.h5
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.187895 kikuchipy-0.8.4/kikuchipy/data/emsoft_tkd_master_pattern/
+-rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_tkd_master_pattern/create_dummy_emsoft_tkd_master_pattern_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    61600 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/emsoft_tkd_master_pattern/tkd_master_pattern.h5
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.187895 kikuchipy-0.8.4/kikuchipy/data/kikuchipy_h5ebsd/
+-rw-r--r--   0 runner    (1001) docker     (123)   149400 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/kikuchipy_h5ebsd/patterns.h5
+-rw-r--r--   0 runner    (1001) docker     (123)    46480 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/kikuchipy_h5ebsd/patterns_nochunks.h5
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.187895 kikuchipy-0.8.4/kikuchipy/data/nordif/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Background acquisition pattern.bmp
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Background calibration pattern.bmp
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Calibration (294,532).bmp
+-rwxr-xr-x   0 runner    (1001) docker     (123)     4678 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Calibration (425,447).bmp
+-rw-r--r--   0 runner    (1001) docker     (123)    32400 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Pattern.dat
+-rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Setting.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1460 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Setting_bad1.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Setting_bad2.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1580 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/nordif/Setting_bad3.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.187895 kikuchipy-0.8.4/kikuchipy/data/oxford_binary/
+-rw-r--r--   0 runner    (1001) docker     (123)     2487 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/oxford_binary/create_dummy_oxford_binary_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32786 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/oxford_binary/patterns.ebsp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.187895 kikuchipy-0.8.4/kikuchipy/data/oxford_h5ebsd/
+-rw-r--r--   0 runner    (1001) docker     (123)     4902 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/oxford_h5ebsd/create_oxford_h5ebsd_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    59152 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/oxford_h5ebsd/patterns.h5oina
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.187895 kikuchipy-0.8.4/kikuchipy/data/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/data/tests/test_data.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.191895 kikuchipy-0.8.4/kikuchipy/detectors/
+-rw-r--r--   0 runner    (1001) docker     (123)     1435 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/detectors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14225 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/detectors/calibration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    67124 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/detectors/ebsd_detector.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.191895 kikuchipy-0.8.4/kikuchipy/detectors/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/detectors/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4691 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/detectors/tests/test_calibration.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39863 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/detectors/tests/test_ebsd_detector.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.191895 kikuchipy-0.8.4/kikuchipy/draw/
+-rw-r--r--   0 runner    (1001) docker     (123)     1454 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1947 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/_navigators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4944 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/_plot_pattern_positions_in_map.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1237 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/colors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/markers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.191895 kikuchipy-0.8.4/kikuchipy/draw/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1067 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/tests/test_colors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10741 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/tests/test_markers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/tests/test_navigators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5101 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/draw/tests/test_plot_pattern_positions_in_map.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/filters/
+-rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/filters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5915 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/filters/fft_barnes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/filters/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/filters/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5895 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/filters/tests/test_fft_barnes.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15640 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/filters/tests/test_window.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17866 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/filters/window.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/generators/
+-rw-r--r--   0 runner    (1001) docker     (123)     1410 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/generators/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/generators/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/generators/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10012 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/generators/tests/test_virtual_bse_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13349 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/generators/virtual_bse_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2188 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/hyperspy_extension.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/imaging/
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/imaging/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/imaging/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/imaging/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9960 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/imaging/tests/test_virtual_bse_imager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16325 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/imaging/vbse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.195895 kikuchipy-0.8.4/kikuchipy/indexing/
+-rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7893 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_dictionary_indexing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12343 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_hough_indexing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13895 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_merge_crystal_maps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5356 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_orientation_similarity_map.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.199895 kikuchipy-0.8.4/kikuchipy/indexing/_refinement/
+-rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_refinement/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6589 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_refinement/_objective_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44415 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_refinement/_refinement.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21304 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/_refinement/_solvers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.199895 kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)     1141 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8146 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/_normalized_cross_correlation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6297 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/_normalized_dot_product.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8831 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/_similarity_metric.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.199895 kikuchipy-0.8.4/kikuchipy/indexing/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7741 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/tests/test_dictionary_indexing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    47403 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/tests/test_ebsd_refinement.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22250 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/tests/test_merge_crystal_maps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2282 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/tests/test_orientation_similarity_map.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2034 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/indexing/tests/test_similarity_metrics.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.199895 kikuchipy-0.8.4/kikuchipy/io/
+-rw-r--r--   0 runner    (1001) docker     (123)     1217 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14667 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2498 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/_util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.203895 kikuchipy-0.8.4/kikuchipy/io/plugins/
+-rw-r--r--   0 runner    (1001) docker     (123)     1750 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10790 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/_emsoft_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16167 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8571 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/bruker_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6490 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/ebsd_directory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8266 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/edax_binary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6762 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/edax_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6682 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3103 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_ebsd_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3091 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_ecp_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3100 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_tkd_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17736 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/kikuchipy_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14826 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/nordif.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3873 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/nordif_calibration_patterns.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19627 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/oxford_binary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7276 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/oxford_h5ebsd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.207895 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      923 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2076 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_bruker_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_ebsd_directory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3326 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_edax_binary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2116 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_edax_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4002 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4388 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_ebsd_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1378 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_ecp_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4587 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1454 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_tkd_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14640 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_kikuchipy_h5ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13546 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_nordif.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3803 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_nordif_calibration_patterns.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4514 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_oxford_binary.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1701 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_oxford_h5ebsd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.207895 kikuchipy-0.8.4/kikuchipy/io/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5374 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/tests/test_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2105 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/io/tests/test_util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.207895 kikuchipy-0.8.4/kikuchipy/pattern/
+-rw-r--r--   0 runner    (1001) docker     (123)     1913 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/pattern/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25808 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/pattern/_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5411 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/pattern/chunk.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.207895 kikuchipy-0.8.4/kikuchipy/pattern/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/pattern/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6248 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/pattern/tests/test_chunk.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18683 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/pattern/tests/test_pattern.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.211895 kikuchipy-0.8.4/kikuchipy/projections/
+-rw-r--r--   0 runner    (1001) docker     (123)     1829 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3772 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/gnomonic_projection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2882 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/hesse_normal_form.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6081 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/lambert_projection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4557 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/spherical_projection.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.211895 kikuchipy-0.8.4/kikuchipy/projections/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3627 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/tests/test_gnomonic_projection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/tests/test_hesse_normal_form.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5392 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/tests/test_lambert_projection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2316 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/projections/tests/test_spherical_projection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1296 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/release.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.211895 kikuchipy-0.8.4/kikuchipy/signals/
+-rw-r--r--   0 runner    (1001) docker     (123)     2042 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13111 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/_kikuchi_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22408 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/_kikuchipy_signal.py
+-rw-r--r--   0 runner    (1001) docker     (123)   131373 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18279 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/ebsd_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6670 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/ecp_master_pattern.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.215895 kikuchipy-0.8.4/kikuchipy/signals/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    87955 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/test_ebsd.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12409 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/test_ebsd_hough_indexing.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27376 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/test_ebsd_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6329 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/test_ecp_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1587 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/test_kikuchi_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5180 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/tests/test_virtual_bse_image.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.215895 kikuchipy-0.8.4/kikuchipy/signals/util/
+-rw-r--r--   0 runner    (1001) docker     (123)     1520 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6000 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/_crystal_map.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11236 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/_dask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1932 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10639 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/_map_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22702 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/_master_pattern.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3140 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/_overwrite_hyperspy_methods.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3537 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/array_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.215895 kikuchipy-0.8.4/kikuchipy/signals/util/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2343 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/tests/test_array_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5001 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/tests/test_dask.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2503 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/util/tests/test_overwrite_hyperspy_methods.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3972 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/signals/virtual_bse_image.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.219895 kikuchipy-0.8.4/kikuchipy/simulations/
+-rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/_kikuchi_pattern_features.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26644 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/_kikuchi_pattern_simulation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27443 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/kikuchi_pattern_simulator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.219895 kikuchipy-0.8.4/kikuchipy/simulations/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      708 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11778 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/tests/test_kikuchi_pattern_simulation.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14664 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/kikuchipy/simulations/tests/test_kikuchi_pattern_simulator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 13:46:12.175895 kikuchipy-0.8.4/kikuchipy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     9502 2023-04-07 13:46:12.000000 kikuchipy-0.8.4/kikuchipy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8949 2023-04-07 13:46:12.000000 kikuchipy-0.8.4/kikuchipy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:46:12.000000 kikuchipy-0.8.4/kikuchipy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       44 2023-04-07 13:46:12.000000 kikuchipy-0.8.4/kikuchipy.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-04-07 13:46:12.000000 kikuchipy-0.8.4/kikuchipy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 13:46:12.000000 kikuchipy-0.8.4/kikuchipy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 13:46:11.000000 kikuchipy-0.8.4/kikuchipy.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      837 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/readthedocs.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      879 2023-04-07 13:46:12.219895 kikuchipy-0.8.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     6156 2023-04-07 13:45:58.000000 kikuchipy-0.8.4/setup.py
```

### Comparing `kikuchipy-0.8.3/CHANGELOG.rst` & `kikuchipy-0.8.4/CHANGELOG.rst`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,38 @@
 =========
 Changelog
 =========
 
-kikuchipy is a library for processing, simulating, and analyzing electron backscatter
+kikuchipy is a library for processing, simulating and indexing of electron backscatter
 diffraction (EBSD) patterns in Python, built on the tools for multi-dimensional data
 analysis provided by the HyperSpy library: https://kikuchipy.org.
 
 All user facing changes to this project are documented in this file. The format is based
 on `Keep a Changelog <https://keepachangelog.com/en/1.1.0>`__, and this project tries
 its best to adhere to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`__.
 
 List entries are sorted in descending chronological order. Contributors to each release
 were listed in alphabetical order by first name until version 0.7.0.
 
+0.8.4 (2023-04-07)
+==================
+
+Fixed
+-----
+- Points considered not-indexed in a crystal map are maintained after EBSD refinement.
+  (`#632 <https://github.com/pyxem/kikuchipy/pull/632>`_)
+
+Changed
+-------
+- EBSD detector returned from combined EBSD and projection center (PC) refinement now
+  has PC values equal to the number of indexed points, accounting for points not being
+  in the data, navigation mask *and* points considered as not-indexed. This means that
+  it might not have a 2D navigation shape, even though the returned crystal map has.
+  (`#632 <https://github.com/pyxem/kikuchipy/pull/632>`_)
+
 0.8.3 (2023-03-23)
 ==================
 
 Changed
 -------
 - ``EBSD.hough_indexing()`` info message now informs that the given projection center is
   in Bruker's convention. (`#628 <https://github.com/pyxem/kikuchipy/pull/628>`_)
```

### Comparing `kikuchipy-0.8.3/CODE_OF_CONDUCT.rst` & `kikuchipy-0.8.4/CODE_OF_CONDUCT.rst`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/LICENSE` & `kikuchipy-0.8.4/LICENSE`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/PKG-INFO` & `kikuchipy-0.8.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: kikuchipy
-Version: 0.8.3
-Summary: Processing and analysis of electron backscatter diffraction (EBSD) patterns.
+Version: 0.8.4
+Summary: Processing, simulating and indexing of electron backscatter diffraction (EBSD) patterns.
 Home-page: https://kikuchipy.org
 Download-URL: https://pypi.python.org/pypi/kikuchipy
 Author: kikuchipy developers
 Author-email: hakon.w.anes@ntnu.no
 Maintainer: Håkon Wiik Ånes
 Maintainer-email: hakon.w.anes@ntnu.no
 License: GPLv3+
@@ -39,16 +39,16 @@
 
 <div align="center">
   <a href="https://kikuchipy.org">
     <img width="60%" src="https://raw.githubusercontent.com/pyxem/kikuchipy/develop/doc/_static/logo/plasma_banner.png">
   </a>
 </div>
 
-kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and analyzing electron
-backscatter diffraction (EBSD) patterns in Python, built on the tools for
+kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and indexing of
+electron backscatter diffraction (EBSD) patterns in Python, built on the tools for
 multi-dimensional data analysis provided by the HyperSpy library.
 
 | Deployment    | [![PyPI version](https://img.shields.io/pypi/v/kikuchipy.svg?logo=python&logoColor=white)](https://pypi.org/project/kikuchipy/) | [![Anaconda version](https://img.shields.io/conda/vn/conda-forge/kikuchipy.svg?logo=conda-forge&logoColor=white)](https://anaconda.org/conda-forge/kikuchipy)|
 | :- | :- | :- |
 | **Build status**  | [![Test status](https://github.com/pyxem/kikuchipy/actions/workflows/tests.yml/badge.svg)](https://github.com/pyxem/kikuchipy/actions/workflows/tests.yml) |
 | **Documentation** | [![Documentation status](https://readthedocs.org/projects/kikuchipy/badge/?version=latest)](https://kikuchipy.org/en/latest/) | [![Launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyxem/kikuchipy/HEAD) |
 | **Metrics**       | [![Coverage status](https://coveralls.io/repos/github/pyxem/kikuchipy/badge.svg?branch=develop)](https://coveralls.io/github/pyxem/kikuchipy?branch=develop) |
```

#### html2text {}

```diff
@@ -1,33 +1,34 @@
-Metadata-Version: 2.1 Name: kikuchipy Version: 0.8.3 Summary: Processing and
-analysis of electron backscatter diffraction (EBSD) patterns. Home-page: https:
-//kikuchipy.org Download-URL: https://pypi.python.org/pypi/kikuchipy Author:
-kikuchipy developers Author-email: hakon.w.anes@ntnu.no Maintainer: HÃ¥kon Wiik
-Ãnes Maintainer-email: hakon.w.anes@ntnu.no License: GPLv3+ Project-URL: Bug
-Tracker, https://github.com/pyxem/kikuchipy/issues Project-URL: Documentation,
-https://kikuchipy.org Project-URL: Source Code, https://github.com/pyxem/
-kikuchipy Keywords: EBSD,electron backscatter diffraction,EBSP,electron
-backscatter pattern,BKD,backscatter kikuchi diffraction,SEM,scanning electron
-microscopy,kikuchi pattern,dictionary indexing Platform: "Linux" Platform:
-"MacOS X" Platform: "Windows" Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.7 Classifier: Programming
-Language :: Python :: 3.8 Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10 Classifier: Development
-Status :: 4 - Beta Classifier: Intended Audience :: Science/Research
-Classifier: License :: OSI Approved :: GNU General Public License v3 or later
-(GPLv3+) Classifier: Natural Language :: English Classifier: Operating System
-:: OS Independent Classifier: Topic :: Scientific/Engineering Classifier: Topic
-:: Scientific/Engineering :: Physics Requires-Python: >=3.7 Description-
-Content-Type: text/markdown Provides-Extra: doc Provides-Extra: tests Provides-
-Extra: all Provides-Extra: viz Provides-Extra: dev License-File: LICENSE
+Metadata-Version: 2.1 Name: kikuchipy Version: 0.8.4 Summary: Processing,
+simulating and indexing of electron backscatter diffraction (EBSD) patterns.
+Home-page: https://kikuchipy.org Download-URL: https://pypi.python.org/pypi/
+kikuchipy Author: kikuchipy developers Author-email: hakon.w.anes@ntnu.no
+Maintainer: HÃ¥kon Wiik Ãnes Maintainer-email: hakon.w.anes@ntnu.no License:
+GPLv3+ Project-URL: Bug Tracker, https://github.com/pyxem/kikuchipy/issues
+Project-URL: Documentation, https://kikuchipy.org Project-URL: Source Code,
+https://github.com/pyxem/kikuchipy Keywords: EBSD,electron backscatter
+diffraction,EBSP,electron backscatter pattern,BKD,backscatter kikuchi
+diffraction,SEM,scanning electron microscopy,kikuchi pattern,dictionary
+indexing Platform: "Linux" Platform: "MacOS X" Platform: "Windows" Classifier:
+Programming Language :: Python :: 3 Classifier: Programming Language :: Python
+:: 3.7 Classifier: Programming Language :: Python :: 3.8 Classifier:
+Programming Language :: Python :: 3.9 Classifier: Programming Language ::
+Python :: 3.10 Classifier: Development Status :: 4 - Beta Classifier: Intended
+Audience :: Science/Research Classifier: License :: OSI Approved :: GNU General
+Public License v3 or later (GPLv3+) Classifier: Natural Language :: English
+Classifier: Operating System :: OS Independent Classifier: Topic :: Scientific/
+Engineering Classifier: Topic :: Scientific/Engineering :: Physics Requires-
+Python: >=3.7 Description-Content-Type: text/markdown Provides-Extra: doc
+Provides-Extra: tests Provides-Extra: all Provides-Extra: viz Provides-Extra:
+dev License-File: LICENSE
  [https://raw.githubusercontent.com/pyxem/kikuchipy/develop/doc/_static/logo/
                               plasma_banner.png]
-kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and analyzing
-electron backscatter diffraction (EBSD) patterns in Python, built on the tools
-for multi-dimensional data analysis provided by the HyperSpy library. |
+kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and indexing
+of electron backscatter diffraction (EBSD) patterns in Python, built on the
+tools for multi-dimensional data analysis provided by the HyperSpy library. |
 Deployment | [![PyPI version](https://img.shields.io/pypi/v/
 kikuchipy.svg?logo=python&logoColor=white)](https://pypi.org/project/kikuchipy/
 ) | [![Anaconda version](https://img.shields.io/conda/vn/conda-forge/
 kikuchipy.svg?logo=conda-forge&logoColor=white)](https://anaconda.org/conda-
 forge/kikuchipy)| | :- | :- | :- | | **Build status** | [![Test status](https:/
 /github.com/pyxem/kikuchipy/actions/workflows/tests.yml/badge.svg)](https://
 github.com/pyxem/kikuchipy/actions/workflows/tests.yml) | | **Documentation** |
```

### Comparing `kikuchipy-0.8.3/README.md` & `kikuchipy-0.8.4/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 <div align="center">
   <a href="https://kikuchipy.org">
     <img width="60%" src="https://raw.githubusercontent.com/pyxem/kikuchipy/develop/doc/_static/logo/plasma_banner.png">
   </a>
 </div>
 
-kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and analyzing electron
-backscatter diffraction (EBSD) patterns in Python, built on the tools for
+kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and indexing of
+electron backscatter diffraction (EBSD) patterns in Python, built on the tools for
 multi-dimensional data analysis provided by the HyperSpy library.
 
 | Deployment    | [![PyPI version](https://img.shields.io/pypi/v/kikuchipy.svg?logo=python&logoColor=white)](https://pypi.org/project/kikuchipy/) | [![Anaconda version](https://img.shields.io/conda/vn/conda-forge/kikuchipy.svg?logo=conda-forge&logoColor=white)](https://anaconda.org/conda-forge/kikuchipy)|
 | :- | :- | :- |
 | **Build status**  | [![Test status](https://github.com/pyxem/kikuchipy/actions/workflows/tests.yml/badge.svg)](https://github.com/pyxem/kikuchipy/actions/workflows/tests.yml) |
 | **Documentation** | [![Documentation status](https://readthedocs.org/projects/kikuchipy/badge/?version=latest)](https://kikuchipy.org/en/latest/) | [![Launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyxem/kikuchipy/HEAD) |
 | **Metrics**       | [![Coverage status](https://coveralls.io/repos/github/pyxem/kikuchipy/badge.svg?branch=develop)](https://coveralls.io/github/pyxem/kikuchipy?branch=develop) |
```

#### html2text {}

```diff
@@ -1,12 +1,12 @@
  [https://raw.githubusercontent.com/pyxem/kikuchipy/develop/doc/_static/logo/
                               plasma_banner.png]
-kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and analyzing
-electron backscatter diffraction (EBSD) patterns in Python, built on the tools
-for multi-dimensional data analysis provided by the HyperSpy library. |
+kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and indexing
+of electron backscatter diffraction (EBSD) patterns in Python, built on the
+tools for multi-dimensional data analysis provided by the HyperSpy library. |
 Deployment | [![PyPI version](https://img.shields.io/pypi/v/
 kikuchipy.svg?logo=python&logoColor=white)](https://pypi.org/project/kikuchipy/
 ) | [![Anaconda version](https://img.shields.io/conda/vn/conda-forge/
 kikuchipy.svg?logo=conda-forge&logoColor=white)](https://anaconda.org/conda-
 forge/kikuchipy)| | :- | :- | :- | | **Build status** | [![Test status](https:/
 /github.com/pyxem/kikuchipy/actions/workflows/tests.yml/badge.svg)](https://
 github.com/pyxem/kikuchipy/actions/workflows/tests.yml) | | **Documentation** |
```

### Comparing `kikuchipy-0.8.3/RELEASE.rst` & `kikuchipy-0.8.4/RELEASE.rst`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/__init__.py` & `kikuchipy-0.8.4/kikuchipy/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_rotation/__init__.py` & `kikuchipy-0.8.4/kikuchipy/_rotation/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_rotation/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/_rotation/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_rotation/tests/test_rotation.py` & `kikuchipy-0.8.4/kikuchipy/_rotation/tests/test_rotation.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/__init__.py` & `kikuchipy-0.8.4/kikuchipy/_util/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/_deprecated.py` & `kikuchipy-0.8.4/kikuchipy/_util/_deprecated.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/_transfer_axes.py` & `kikuchipy-0.8.4/kikuchipy/_util/_transfer_axes.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/_util/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/tests/test_deprecated.py` & `kikuchipy-0.8.4/kikuchipy/_util/tests/test_deprecated.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/tests/test_import.py` & `kikuchipy-0.8.4/kikuchipy/_util/tests/test_import.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/_util/tests/test_logging.py` & `kikuchipy-0.8.4/kikuchipy/_util/tests/test_logging.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/conftest.py` & `kikuchipy-0.8.4/kikuchipy/conftest.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/__init__.py` & `kikuchipy-0.8.4/kikuchipy/data/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/_data.py` & `kikuchipy-0.8.4/kikuchipy/data/_data.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/_registry.py` & `kikuchipy-0.8.4/kikuchipy/data/_registry.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/create_bruker_h5ebsd_file.py` & `kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/create_bruker_h5ebsd_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/patterns.h5` & `kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/patterns.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/patterns_roi.h5` & `kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/patterns_roi.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/bruker_h5ebsd/patterns_roi_nonrectangular.h5` & `kikuchipy-0.8.4/kikuchipy/data/bruker_h5ebsd/patterns_roi_nonrectangular.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/edax_binary/create_dummy_edax_binary_file.py` & `kikuchipy-0.8.4/kikuchipy/data/edax_binary/create_dummy_edax_binary_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/edax_binary/edax_binary.up1` & `kikuchipy-0.8.4/kikuchipy/data/edax_binary/edax_binary.up1`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/edax_binary/edax_binary.up2` & `kikuchipy-0.8.4/kikuchipy/data/edax_binary/edax_binary.up2`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/edax_h5ebsd/patterns.h5` & `kikuchipy-0.8.4/kikuchipy/data/edax_h5ebsd/patterns.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/EBSD_TEST_Ni.h5` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/EBSD_TEST_Ni.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/create_dummy_emsoft_ebsd_file.py` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/create_dummy_emsoft_ebsd_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd/simulated_ebsd.h5` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd/simulated_ebsd.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/convert_emsoft_ebsd_masterpattern_file_uint8_gzip.py` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/convert_emsoft_ebsd_masterpattern_file_uint8_gzip.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/create_dummy_emsoft_ebsd_master_pattern_file.py` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/create_dummy_emsoft_ebsd_master_pattern_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/master_patterns.h5` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/master_patterns.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni.xtal` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni.xtal`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_ebsdmaster.nml` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_ebsdmaster.nml`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc.out` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc.out`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc_mp_20kv_uint8_gzip_opts9.h5` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mc_mp_20kv_uint8_gzip_opts9.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mcopencl.nml` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mcopencl.nml`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mp.out` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ebsd_master_pattern/ni_mp.out`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ecp_master_pattern/create_dummy_emsoft_ecp_master_pattern_file.py` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ecp_master_pattern/create_dummy_emsoft_ecp_master_pattern_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_ecp_master_pattern/ecp_master_pattern.h5` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_ecp_master_pattern/ecp_master_pattern.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_tkd_master_pattern/create_dummy_emsoft_tkd_master_pattern_file.py` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_tkd_master_pattern/create_dummy_emsoft_tkd_master_pattern_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/emsoft_tkd_master_pattern/tkd_master_pattern.h5` & `kikuchipy-0.8.4/kikuchipy/data/emsoft_tkd_master_pattern/tkd_master_pattern.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/kikuchipy_h5ebsd/patterns.h5` & `kikuchipy-0.8.4/kikuchipy/data/kikuchipy_h5ebsd/patterns.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/kikuchipy_h5ebsd/patterns_nochunks.h5` & `kikuchipy-0.8.4/kikuchipy/data/kikuchipy_h5ebsd/patterns_nochunks.h5`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Background acquisition pattern.bmp` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Background acquisition pattern.bmp`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Background calibration pattern.bmp` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Background calibration pattern.bmp`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Calibration (294,532).bmp` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Calibration (294,532).bmp`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Calibration (425,447).bmp` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Calibration (425,447).bmp`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Pattern.dat` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Pattern.dat`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Setting.txt` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Setting.txt`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Setting_bad1.txt` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Setting_bad1.txt`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Setting_bad2.txt` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Setting_bad2.txt`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/nordif/Setting_bad3.txt` & `kikuchipy-0.8.4/kikuchipy/data/nordif/Setting_bad3.txt`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/oxford_binary/create_dummy_oxford_binary_file.py` & `kikuchipy-0.8.4/kikuchipy/data/oxford_binary/create_dummy_oxford_binary_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/oxford_binary/patterns.ebsp` & `kikuchipy-0.8.4/kikuchipy/data/oxford_binary/patterns.ebsp`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/oxford_h5ebsd/create_oxford_h5ebsd_file.py` & `kikuchipy-0.8.4/kikuchipy/data/oxford_h5ebsd/create_oxford_h5ebsd_file.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/oxford_h5ebsd/patterns.h5oina` & `kikuchipy-0.8.4/kikuchipy/data/oxford_h5ebsd/patterns.h5oina`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/data/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/data/tests/test_data.py` & `kikuchipy-0.8.4/kikuchipy/data/tests/test_data.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/detectors/__init__.py` & `kikuchipy-0.8.4/kikuchipy/detectors/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/detectors/calibration.py` & `kikuchipy-0.8.4/kikuchipy/detectors/calibration.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/detectors/ebsd_detector.py` & `kikuchipy-0.8.4/kikuchipy/detectors/ebsd_detector.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/detectors/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/detectors/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/detectors/tests/test_calibration.py` & `kikuchipy-0.8.4/kikuchipy/detectors/tests/test_calibration.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/detectors/tests/test_ebsd_detector.py` & `kikuchipy-0.8.4/kikuchipy/detectors/tests/test_ebsd_detector.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/__init__.py` & `kikuchipy-0.8.4/kikuchipy/draw/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/_navigators.py` & `kikuchipy-0.8.4/kikuchipy/draw/_navigators.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/_plot_pattern_positions_in_map.py` & `kikuchipy-0.8.4/kikuchipy/draw/_plot_pattern_positions_in_map.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/colors.py` & `kikuchipy-0.8.4/kikuchipy/draw/colors.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/markers.py` & `kikuchipy-0.8.4/kikuchipy/draw/markers.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/draw/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/tests/test_colors.py` & `kikuchipy-0.8.4/kikuchipy/draw/tests/test_colors.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/tests/test_markers.py` & `kikuchipy-0.8.4/kikuchipy/draw/tests/test_markers.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/tests/test_navigators.py` & `kikuchipy-0.8.4/kikuchipy/draw/tests/test_navigators.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/draw/tests/test_plot_pattern_positions_in_map.py` & `kikuchipy-0.8.4/kikuchipy/draw/tests/test_plot_pattern_positions_in_map.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/filters/__init__.py` & `kikuchipy-0.8.4/kikuchipy/filters/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/filters/fft_barnes.py` & `kikuchipy-0.8.4/kikuchipy/filters/fft_barnes.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/filters/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/filters/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/filters/tests/test_fft_barnes.py` & `kikuchipy-0.8.4/kikuchipy/filters/tests/test_fft_barnes.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/filters/tests/test_window.py` & `kikuchipy-0.8.4/kikuchipy/filters/tests/test_window.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/filters/window.py` & `kikuchipy-0.8.4/kikuchipy/filters/window.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/generators/__init__.py` & `kikuchipy-0.8.4/kikuchipy/generators/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/generators/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/generators/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/generators/tests/test_virtual_bse_generator.py` & `kikuchipy-0.8.4/kikuchipy/generators/tests/test_virtual_bse_generator.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/generators/virtual_bse_generator.py` & `kikuchipy-0.8.4/kikuchipy/generators/virtual_bse_generator.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/hyperspy_extension.yaml` & `kikuchipy-0.8.4/kikuchipy/hyperspy_extension.yaml`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/imaging/__init__.py` & `kikuchipy-0.8.4/kikuchipy/imaging/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/imaging/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/imaging/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/imaging/tests/test_virtual_bse_imager.py` & `kikuchipy-0.8.4/kikuchipy/imaging/tests/test_virtual_bse_imager.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/imaging/vbse.py` & `kikuchipy-0.8.4/kikuchipy/imaging/vbse.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/__init__.py` & `kikuchipy-0.8.4/kikuchipy/indexing/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_dictionary_indexing.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_dictionary_indexing.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_hough_indexing.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_hough_indexing.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_merge_crystal_maps.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_merge_crystal_maps.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_orientation_similarity_map.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_orientation_similarity_map.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_refinement/__init__.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_refinement/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_refinement/_objective_functions.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_refinement/_objective_functions.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_refinement/_refinement.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_refinement/_refinement.py`

 * *Files 1% similar despite different names*

```diff
@@ -23,29 +23,29 @@
 import sys
 from time import time
 from typing import Callable, Optional, Tuple, Union
 
 from dask.diagnostics import ProgressBar
 import dask.array as da
 import numpy as np
-from orix.crystal_map import create_coordinate_arrays, CrystalMap, PhaseList
+from orix.crystal_map import create_coordinate_arrays, CrystalMap, Phase, PhaseList
 from orix.quaternion import Rotation
 import scipy.optimize
 
 from kikuchipy.indexing._refinement._solvers import (
     _refine_orientation_solver_nlopt,
     _refine_orientation_solver_scipy,
     _refine_orientation_pc_solver_nlopt,
     _refine_orientation_pc_solver_scipy,
     _refine_pc_solver_nlopt,
     _refine_pc_solver_scipy,
 )
 from kikuchipy.indexing._refinement import SUPPORTED_OPTIMIZATION_METHODS
 from kikuchipy.pattern import rescale_intensity
-from kikuchipy.signals.util._crystal_map import _get_points_in_data_in_xmap
+from kikuchipy.signals.util._crystal_map import _get_indexed_points_in_data_in_xmap
 from kikuchipy.signals.util._master_pattern import (
     _get_direction_cosines_from_detector,
 )
 
 
 def compute_refine_orientation_results(
     results: da.Array,
@@ -80,23 +80,30 @@
     -------
     xmap_refined
         Crystal map with refined orientations, scores, the number of
         function evaluations and the pseudo-symmetry index if
         ``pseudo_symmetry_checked=True``. See the docstring of
         ``refine_orientation()`` for details.
     """
-    points_to_refine, phase_id, *_ = _get_points_in_data_in_xmap(xmap, navigation_mask)
+    points_to_refine, is_in_data, phase_id, _ = _get_indexed_points_in_data_in_xmap(
+        xmap, navigation_mask
+    )
 
     nav_size = points_to_refine.size
     nav_size_in_data = points_to_refine.sum()
 
-    xmap_kw = _get_crystal_map_parameters(xmap, nav_size, pseudo_symmetry_checked)
-    xmap_kw["phase_list"] = PhaseList(phases=master_pattern.phase, ids=phase_id)
+    xmap_kw = _get_crystal_map_parameters(
+        xmap, nav_size, master_pattern.phase, phase_id, pseudo_symmetry_checked
+    )
     xmap_kw["phase_id"][points_to_refine] = phase_id
 
+    is_indexed = np.zeros_like(is_in_data)
+    is_indexed[xmap.is_in_data] = xmap.is_indexed
+    xmap_kw["phase_id"][~is_indexed] = -1
+
     print(f"Refining {nav_size_in_data} orientation(s):", file=sys.stdout)
     time_start = time()
     with ProgressBar():
         res = results.compute()
     total_time = time() - time_start
     patterns_per_second = nav_size_in_data / total_time
     print(f"Refinement speed: {patterns_per_second:.5f} patterns/s", file=sys.stdout)
@@ -106,15 +113,15 @@
     res = np.array(res)
     xmap_kw["prop"]["scores"][points_to_refine] = res[:, 0]
     xmap_kw["prop"]["num_evals"][points_to_refine] = res[:, 1]
     xmap_kw["rotations"][points_to_refine] = Rotation.from_euler(res[:, 2:5]).data
     if pseudo_symmetry_checked:
         xmap_kw["prop"]["pseudo_symmetry_index"][points_to_refine] = res[:, 5]
 
-    xmap_refined = CrystalMap(is_in_data=points_to_refine, **xmap_kw)
+    xmap_refined = CrystalMap(is_in_data=is_in_data, **xmap_kw)
 
     return xmap_refined
 
 
 def compute_refine_projection_center_results(
     results: da.Array,
     detector: "EBSDDetector",
@@ -146,15 +153,15 @@
     new_scores
         Score array.
     new_detector
         EBSD detector with refined projection center parameters.
     num_evals
         Number of function evaluations per pattern.
     """
-    points_to_refine, _, mask_is_continuous, mask_shape = _get_points_in_data_in_xmap(
+    (points_to_refine, *_, mask_shape) = _get_indexed_points_in_data_in_xmap(
         xmap, navigation_mask
     )
     nav_size_in_data = points_to_refine.sum()
 
     new_detector = detector.deepcopy()
 
     print(f"Refining {nav_size_in_data} projection center(s):", file=sys.stdout)
@@ -167,15 +174,15 @@
 
     # Extract data: n x (score, number of evaluations, PCx, PCy, PCz)
     res = np.array(res)
     scores = res[:, 0]
     num_evals = res[:, 1].astype(np.int32)
     new_pc = res[:, 2:]
 
-    if mask_is_continuous:
+    if mask_shape is not None:
         scores = scores.reshape(mask_shape)
         num_evals = num_evals.reshape(mask_shape)
         new_pc = new_pc.reshape(mask_shape + (3,))
 
     new_detector.pc = new_pc
 
     return scores, new_detector, num_evals
@@ -231,26 +238,31 @@
 
     See Also
     --------
     kikuchipy.signals.EBSD.refine_orientation_projection_center
     """
     (
         points_to_refine,
+        is_in_data,
         phase_id,
-        mask_is_continuous,
         mask_shape,
-    ) = _get_points_in_data_in_xmap(xmap, navigation_mask)
+    ) = _get_indexed_points_in_data_in_xmap(xmap, navigation_mask)
 
     nav_size = points_to_refine.size
     nav_size_in_data = points_to_refine.sum()
 
-    xmap_kw = _get_crystal_map_parameters(xmap, nav_size, pseudo_symmetry_checked)
-    xmap_kw["phase_list"] = PhaseList(phases=master_pattern.phase, ids=phase_id)
+    xmap_kw = _get_crystal_map_parameters(
+        xmap, nav_size, master_pattern.phase, phase_id, pseudo_symmetry_checked
+    )
     xmap_kw["phase_id"][points_to_refine] = phase_id
 
+    is_indexed = np.zeros_like(is_in_data)
+    is_indexed[xmap.is_in_data] = xmap.is_indexed
+    xmap_kw["phase_id"][~is_indexed] = -1
+
     new_detector = detector.deepcopy()
 
     print(
         f"Refining {nav_size_in_data} orientation(s) and projection center(s):",
         file=sys.stdout,
     )
     time_start = time()
@@ -265,50 +277,56 @@
     res = np.array(res)
     xmap_kw["prop"]["scores"][points_to_refine] = res[:, 0]
     xmap_kw["prop"]["num_evals"][points_to_refine] = res[:, 1]
     xmap_kw["rotations"][points_to_refine] = Rotation.from_euler(res[:, 2:5]).data
     if pseudo_symmetry_checked:
         xmap_kw["prop"]["pseudo_symmetry_index"][points_to_refine] = res[:, 8]
 
-    xmap_refined = CrystalMap(is_in_data=points_to_refine, **xmap_kw)
+    xmap_refined = CrystalMap(is_in_data=is_in_data, **xmap_kw)
 
     new_pc = res[:, 5:8]
-    if mask_is_continuous:
+    if mask_shape is not None:
         new_pc = new_pc.reshape(mask_shape + (3,))
     new_detector.pc = new_pc
 
     return xmap_refined, new_detector
 
 
 def _get_crystal_map_parameters(
     xmap: CrystalMap,
     nav_size: int,
+    master_pattern_phase: Phase,
+    phase_id: int,
     pseudo_symmetry_checked: bool = False,
 ) -> dict:
     step_sizes = ()
     for step_size in [xmap.dy, xmap.dx]:
         if step_size != 0:
             step_sizes += (step_size,)
 
     xmap_dict, _ = create_coordinate_arrays(xmap.shape, step_sizes=step_sizes)
     xmap_dict.update(
         {
             "rotations": Rotation.identity((nav_size,)),
             "phase_id": np.zeros(nav_size, dtype=np.int32),
+            "phase_list": PhaseList(phases=master_pattern_phase, ids=phase_id),
             "scan_unit": xmap.scan_unit,
             "prop": {
                 "scores": np.zeros(nav_size, dtype=np.float64),
                 "num_evals": np.zeros(nav_size, dtype=np.int32),
             },
         }
     )
 
     if pseudo_symmetry_checked:
         xmap_dict["prop"]["pseudo_symmetry_index"] = np.zeros(nav_size, dtype=np.int32)
 
+    if "not_indexed" in xmap.phases.names:
+        xmap_dict["phase_list"].add_not_indexed()
+
     return xmap_dict
 
 
 # -------------------------- Refine orientation ---------------------- #
 
 
 def _refine_orientation(
```

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/_refinement/_solvers.py` & `kikuchipy-0.8.4/kikuchipy/indexing/_refinement/_solvers.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/__init__.py` & `kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/_normalized_cross_correlation.py` & `kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/_normalized_cross_correlation.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/_normalized_dot_product.py` & `kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/_normalized_dot_product.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/similarity_metrics/_similarity_metric.py` & `kikuchipy-0.8.4/kikuchipy/indexing/similarity_metrics/_similarity_metric.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/indexing/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/tests/test_dictionary_indexing.py` & `kikuchipy-0.8.4/kikuchipy/indexing/tests/test_dictionary_indexing.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/tests/test_ebsd_refinement.py` & `kikuchipy-0.8.4/kikuchipy/indexing/tests/test_ebsd_refinement.py`

 * *Files 11% similar despite different names*

```diff
@@ -665,14 +665,116 @@
         # Global: Differential evolution
         _ = s.refine_orientation(
             method="differential_evolution",
             navigation_mask=nav_mask,
             **ref_kw,
         )
 
+    def test_refine_orientation_not_indexed_case1(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining crystal map with some points considered
+        not-indexed (phase ID of -1).
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap[1, 2].phase_id = -1
+
+        ref_kw = dict(detector=s.detector, master_pattern=self.mp, energy=20)
+
+        xmap_ref = s.refine_orientation(xmap, **ref_kw)
+
+        assert xmap_ref.size == 9
+        assert np.allclose(xmap_ref.is_in_data, xmap.is_in_data)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id)
+        assert "not_indexed" in xmap_ref.phases.names
+
+    def test_refine_orientation_not_indexed_case2(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining crystal map with some points considered
+        not-indexed (phase ID of -1) within a navigation mask.
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap[1, 2].phase_id = -1
+
+        nav_mask = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0], dtype=bool)
+        xmap_ref = s.refine_orientation(
+            xmap, s.detector, self.mp, 20, navigation_mask=nav_mask.reshape(xmap.shape)
+        )
+
+        assert xmap_ref.size == 7
+        assert np.allclose(xmap_ref.is_in_data, ~nav_mask)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id[~nav_mask])
+        assert "not_indexed" in xmap_ref.phases.names
+
+    def test_refine_orientation_not_indexed_case3(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining crystal map with some points considered
+        not-indexed (phase ID of -1) outside a navigation mask.
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap[1, 2].phase_id = -1
+
+        nav_mask = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0], dtype=bool)
+        xmap_ref = s.refine_orientation(
+            xmap,
+            s.detector,
+            self.mp,
+            20,
+            navigation_mask=nav_mask.reshape((3, 3)),
+        )
+
+        assert xmap_ref.size == 8
+        assert np.allclose(xmap_ref.is_in_data, ~nav_mask)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id[~nav_mask])
+        assert "not_indexed" not in xmap_ref.phases_in_data.names
+
+    def test_refine_orientation_not_indexed_case4(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining crystal map with some points considered
+        not-indexed (phase ID of -1) and not in the data.
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap.is_in_data[[5, 7]] = False
+        xmap.phases.add_not_indexed()
+        xmap[0, 0].phase_id = -1
+
+        xmap_ref = s.refine_orientation(xmap, s.detector, self.mp, 20)
+
+        assert xmap_ref.size == 7
+        assert np.allclose(xmap_ref.is_in_data, xmap.is_in_data)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id)
+        assert "not_indexed" in xmap_ref.phases_in_data.names
+
 
 class TestEBSDRefinePC(EBSDRefineTestSetup):
     @pytest.mark.parametrize(
         "ebsd_with_axes_and_random_data, detector, method_kwargs, trust_region",
         [
             (
                 ((4,), (3, 4), True, np.float32),
@@ -1104,7 +1206,114 @@
 
         # Global: Differential evolution
         _, _ = s.refine_orientation_projection_center(
             method="differential_evolution",
             navigation_mask=nav_mask,
             **ref_kw,
         )
+
+    def test_refine_orientation_pc_not_indexed_case1(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining orientations and PC with one point
+        considered not-indexed (phase ID of -1).
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap[1, 2].phase_id = -1
+
+        xmap_ref, det_ref = s.refine_orientation_projection_center(
+            xmap, s.detector, self.mp, 20
+        )
+
+        assert xmap_ref.size == 9
+        assert np.all(xmap_ref.is_in_data)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id)
+        assert "not_indexed" in xmap_ref.phases.names
+        assert det_ref.navigation_shape == (8,)
+
+    def test_refine_orientation_pc_not_indexed_case2(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining orientations and PC with one point
+        considered not-indexed (phase ID of -1) within a navigation
+        mask.
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap[1, 2].phase_id = -1
+
+        nav_mask = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0], dtype=bool)
+        xmap_ref, det_ref = s.refine_orientation_projection_center(
+            xmap, s.detector, self.mp, 20, navigation_mask=nav_mask.reshape(xmap.shape)
+        )
+
+        assert xmap_ref.size == 7
+        assert np.allclose(xmap_ref.is_in_data, ~nav_mask)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id[~nav_mask])
+        assert "not_indexed" in xmap_ref.phases.names
+        assert det_ref.navigation_shape == (6,)
+
+    def test_refine_orientation_pc_not_indexed_case3(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining orientations and PC with one point
+        considered not-indexed (phase ID of -1) outside a navigation
+        mask.
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap[1, 2].phase_id = -1
+
+        nav_mask = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0], dtype=bool)
+        xmap_ref, det_ref = s.refine_orientation_projection_center(
+            xmap, s.detector, self.mp, 20, navigation_mask=nav_mask.reshape((3, 3))
+        )
+
+        assert xmap_ref.size == 8
+        assert np.allclose(xmap_ref.is_in_data, ~nav_mask)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id[~nav_mask])
+        assert "not_indexed" not in xmap_ref.phases_in_data.names
+        assert det_ref.navigation_shape == (8,)
+
+    def test_refine_orientation_pc_not_indexed_case4(
+        self, dummy_signal, get_single_phase_xmap
+    ):
+        """Test refinining orientations and PCs with one point
+        considered not-indexed (phase ID of -1) and some points not in
+        the data.
+        """
+        s = dummy_signal
+        xmap = get_single_phase_xmap(
+            nav_shape=s._navigation_shape_rc,
+            rotations_per_point=1,
+            step_sizes=tuple(a.scale for a in s.axes_manager.navigation_axes)[::-1],
+        )
+        xmap.phases.add_not_indexed()
+        xmap.is_in_data[[5, 7]] = False
+        xmap.phases.add_not_indexed()
+        xmap[0, 0].phase_id = -1
+
+        xmap_ref, det_ref = s.refine_orientation_projection_center(
+            xmap, s.detector, self.mp, 20
+        )
+
+        assert xmap_ref.size == 7
+        assert np.allclose(xmap_ref.is_in_data, xmap.is_in_data)
+        assert np.allclose(xmap_ref.phase_id, xmap.phase_id)
+        assert "not_indexed" in xmap_ref.phases_in_data.names
+        assert det_ref.navigation_shape == (6,)
```

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/tests/test_merge_crystal_maps.py` & `kikuchipy-0.8.4/kikuchipy/indexing/tests/test_merge_crystal_maps.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/tests/test_orientation_similarity_map.py` & `kikuchipy-0.8.4/kikuchipy/indexing/tests/test_orientation_similarity_map.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/indexing/tests/test_similarity_metrics.py` & `kikuchipy-0.8.4/kikuchipy/indexing/tests/test_similarity_metrics.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/__init__.py` & `kikuchipy-0.8.4/kikuchipy/io/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/_io.py` & `kikuchipy-0.8.4/kikuchipy/io/_io.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/_util.py` & `kikuchipy-0.8.4/kikuchipy/io/_util.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/__init__.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/_emsoft_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/_emsoft_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/bruker_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/bruker_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/ebsd_directory.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/ebsd_directory.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/edax_binary.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/edax_binary.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/edax_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/edax_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_ebsd_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_ebsd_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_ecp_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_ecp_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/emsoft_tkd_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/emsoft_tkd_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/kikuchipy_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/kikuchipy_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/nordif.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/nordif.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/nordif_calibration_patterns.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/nordif_calibration_patterns.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/oxford_binary.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/oxford_binary.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/oxford_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/oxford_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_bruker_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_bruker_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_ebsd_directory.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_ebsd_directory.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_edax_binary.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_edax_binary.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_edax_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_edax_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_ebsd_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_ebsd_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_ecp_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_ecp_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_emsoft_tkd_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_emsoft_tkd_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_kikuchipy_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_kikuchipy_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_nordif.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_nordif.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_nordif_calibration_patterns.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_nordif_calibration_patterns.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_oxford_binary.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_oxford_binary.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/plugins/tests/test_oxford_h5ebsd.py` & `kikuchipy-0.8.4/kikuchipy/io/plugins/tests/test_oxford_h5ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/io/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/tests/test_io.py` & `kikuchipy-0.8.4/kikuchipy/io/tests/test_io.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/io/tests/test_util.py` & `kikuchipy-0.8.4/kikuchipy/io/tests/test_util.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/pattern/__init__.py` & `kikuchipy-0.8.4/kikuchipy/pattern/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/pattern/_pattern.py` & `kikuchipy-0.8.4/kikuchipy/pattern/_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/pattern/chunk.py` & `kikuchipy-0.8.4/kikuchipy/pattern/chunk.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/pattern/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/pattern/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/pattern/tests/test_chunk.py` & `kikuchipy-0.8.4/kikuchipy/pattern/tests/test_chunk.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/pattern/tests/test_pattern.py` & `kikuchipy-0.8.4/kikuchipy/pattern/tests/test_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/__init__.py` & `kikuchipy-0.8.4/kikuchipy/projections/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/gnomonic_projection.py` & `kikuchipy-0.8.4/kikuchipy/projections/gnomonic_projection.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/hesse_normal_form.py` & `kikuchipy-0.8.4/kikuchipy/projections/hesse_normal_form.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/lambert_projection.py` & `kikuchipy-0.8.4/kikuchipy/projections/lambert_projection.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/spherical_projection.py` & `kikuchipy-0.8.4/kikuchipy/projections/spherical_projection.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/projections/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/tests/test_gnomonic_projection.py` & `kikuchipy-0.8.4/kikuchipy/projections/tests/test_gnomonic_projection.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/tests/test_hesse_normal_form.py` & `kikuchipy-0.8.4/kikuchipy/projections/tests/test_hesse_normal_form.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/tests/test_lambert_projection.py` & `kikuchipy-0.8.4/kikuchipy/projections/tests/test_lambert_projection.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/projections/tests/test_spherical_projection.py` & `kikuchipy-0.8.4/kikuchipy/projections/tests/test_spherical_projection.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/release.py` & `kikuchipy-0.8.4/kikuchipy/release.py`

 * *Files 8% similar despite different names*

```diff
@@ -33,8 +33,8 @@
 ]
 license = "GPLv3+"
 maintainer = "Håkon Wiik Ånes"
 maintainer_email = "hakon.w.anes@ntnu.no"
 name = "kikuchipy"
 platforms = ["Linux", "MacOS X", "Windows"]
 status = "Development"
-version = "0.8.3"
+version = "0.8.4"
```

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/__init__.py` & `kikuchipy-0.8.4/kikuchipy/signals/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/_kikuchi_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/_kikuchi_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/_kikuchipy_signal.py` & `kikuchipy-0.8.4/kikuchipy/signals/_kikuchipy_signal.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/ebsd.py` & `kikuchipy-0.8.4/kikuchipy/signals/ebsd.py`

 * *Files 0% similar despite different names*

```diff
@@ -79,15 +79,15 @@
     get_chunking,
     _get_chunk_overlap_depth,
     _rechunk_learning_results,
     _update_learning_results,
 )
 from kikuchipy.signals.util._detector import _detector_is_compatible_with_signal
 from kikuchipy.signals.util._crystal_map import (
-    _get_points_in_data_in_xmap,
+    _get_indexed_points_in_data_in_xmap,
     _equal_phase,
     _xmap_is_compatible_with_signal,
 )
 from kikuchipy.signals.util._map_helper import (
     _get_neighbour_dot_product_matrices,
     _get_average_dot_product_map,
 )
@@ -2320,14 +2320,18 @@
         See Also
         --------
         scipy.optimize, refine_orientation,
         refine_orientation_projection_center
 
         Notes
         -----
+        If the crystal map to refine contains points marked as not
+        indexed, the returned detector might not have a 2D navigation
+        shape.
+
         *NLopt* is for now an optional dependency, see
         :ref:`optional-dependencies` for details. Be aware that *NLopt*
         does not fail gracefully. If continued use of *NLopt* proves
         stable enough, its implementation of the Nelder-Mead algorithm
         might become the default.
         """
         points_to_refine = self._check_refinement_parameters(
@@ -2525,14 +2529,18 @@
 
         See Also
         --------
         scipy.optimize, refine_orientation, refine_projection_center
 
         Notes
         -----
+        If the crystal map to refine contains points marked as not
+        indexed, the returned detector might not have a 2D navigation
+        shape.
+
         The method attempts to refine the orientations and projection
         center at the same time for each map point. The optimization
         landscape is sloppy :cite:`pang2020global`, where the
         orientation and PC can make up for each other. Thus, it is
         possible that the parameters that yield the highest similarity
         are incorrect. As always, it is left to the user to ensure that
         the output is reasonable.
@@ -2921,15 +2929,15 @@
 
         _ = _xmap_is_compatible_with_signal(
             xmap=xmap, navigation_axes=am.navigation_axes[::-1], raise_if_not=True
         )
 
         # Checks navigation mask shape and whether there is only one
         # phase ID in points to refine
-        points_to_refine, phase_id, *_ = _get_points_in_data_in_xmap(
+        points_to_refine, _, phase_id, _ = _get_indexed_points_in_data_in_xmap(
             xmap, navigation_mask
         )
 
         master_pattern._is_suitable_for_projection(raise_if_not=True)
 
         xmap_phase = xmap.phases_in_data[phase_id]
         mp_phase = master_pattern.phase
```

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/ebsd_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/ebsd_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/ecp_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/ecp_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/test_ebsd.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/test_ebsd.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/test_ebsd_hough_indexing.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/test_ebsd_hough_indexing.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/test_ebsd_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/test_ebsd_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/test_ecp_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/test_ecp_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/test_kikuchi_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/test_kikuchi_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/tests/test_virtual_bse_image.py` & `kikuchipy-0.8.4/kikuchipy/signals/tests/test_virtual_bse_image.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/__init__.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/_dask.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/_dask.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/_detector.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/_detector.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/_map_helper.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/_map_helper.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/_master_pattern.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/_master_pattern.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/_overwrite_hyperspy_methods.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/_overwrite_hyperspy_methods.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/array_tools.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/array_tools.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/tests/test_array_tools.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/tests/test_array_tools.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/tests/test_dask.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/tests/test_dask.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/util/tests/test_overwrite_hyperspy_methods.py` & `kikuchipy-0.8.4/kikuchipy/signals/util/tests/test_overwrite_hyperspy_methods.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/signals/virtual_bse_image.py` & `kikuchipy-0.8.4/kikuchipy/signals/virtual_bse_image.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/__init__.py` & `kikuchipy-0.8.4/kikuchipy/simulations/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/_kikuchi_pattern_features.py` & `kikuchipy-0.8.4/kikuchipy/simulations/_kikuchi_pattern_features.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/_kikuchi_pattern_simulation.py` & `kikuchipy-0.8.4/kikuchipy/simulations/_kikuchi_pattern_simulation.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/kikuchi_pattern_simulator.py` & `kikuchipy-0.8.4/kikuchipy/simulations/kikuchi_pattern_simulator.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/tests/__init__.py` & `kikuchipy-0.8.4/kikuchipy/simulations/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/tests/test_kikuchi_pattern_simulation.py` & `kikuchipy-0.8.4/kikuchipy/simulations/tests/test_kikuchi_pattern_simulation.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy/simulations/tests/test_kikuchi_pattern_simulator.py` & `kikuchipy-0.8.4/kikuchipy/simulations/tests/test_kikuchi_pattern_simulator.py`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy.egg-info/PKG-INFO` & `kikuchipy-0.8.4/kikuchipy.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 Metadata-Version: 2.1
 Name: kikuchipy
-Version: 0.8.3
-Summary: Processing and analysis of electron backscatter diffraction (EBSD) patterns.
+Version: 0.8.4
+Summary: Processing, simulating and indexing of electron backscatter diffraction (EBSD) patterns.
 Home-page: https://kikuchipy.org
 Download-URL: https://pypi.python.org/pypi/kikuchipy
 Author: kikuchipy developers
 Author-email: hakon.w.anes@ntnu.no
 Maintainer: Håkon Wiik Ånes
 Maintainer-email: hakon.w.anes@ntnu.no
 License: GPLv3+
@@ -39,16 +39,16 @@
 
 <div align="center">
   <a href="https://kikuchipy.org">
     <img width="60%" src="https://raw.githubusercontent.com/pyxem/kikuchipy/develop/doc/_static/logo/plasma_banner.png">
   </a>
 </div>
 
-kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and analyzing electron
-backscatter diffraction (EBSD) patterns in Python, built on the tools for
+kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and indexing of
+electron backscatter diffraction (EBSD) patterns in Python, built on the tools for
 multi-dimensional data analysis provided by the HyperSpy library.
 
 | Deployment    | [![PyPI version](https://img.shields.io/pypi/v/kikuchipy.svg?logo=python&logoColor=white)](https://pypi.org/project/kikuchipy/) | [![Anaconda version](https://img.shields.io/conda/vn/conda-forge/kikuchipy.svg?logo=conda-forge&logoColor=white)](https://anaconda.org/conda-forge/kikuchipy)|
 | :- | :- | :- |
 | **Build status**  | [![Test status](https://github.com/pyxem/kikuchipy/actions/workflows/tests.yml/badge.svg)](https://github.com/pyxem/kikuchipy/actions/workflows/tests.yml) |
 | **Documentation** | [![Documentation status](https://readthedocs.org/projects/kikuchipy/badge/?version=latest)](https://kikuchipy.org/en/latest/) | [![Launch binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyxem/kikuchipy/HEAD) |
 | **Metrics**       | [![Coverage status](https://coveralls.io/repos/github/pyxem/kikuchipy/badge.svg?branch=develop)](https://coveralls.io/github/pyxem/kikuchipy?branch=develop) |
```

#### html2text {}

```diff
@@ -1,33 +1,34 @@
-Metadata-Version: 2.1 Name: kikuchipy Version: 0.8.3 Summary: Processing and
-analysis of electron backscatter diffraction (EBSD) patterns. Home-page: https:
-//kikuchipy.org Download-URL: https://pypi.python.org/pypi/kikuchipy Author:
-kikuchipy developers Author-email: hakon.w.anes@ntnu.no Maintainer: HÃ¥kon Wiik
-Ãnes Maintainer-email: hakon.w.anes@ntnu.no License: GPLv3+ Project-URL: Bug
-Tracker, https://github.com/pyxem/kikuchipy/issues Project-URL: Documentation,
-https://kikuchipy.org Project-URL: Source Code, https://github.com/pyxem/
-kikuchipy Keywords: EBSD,electron backscatter diffraction,EBSP,electron
-backscatter pattern,BKD,backscatter kikuchi diffraction,SEM,scanning electron
-microscopy,kikuchi pattern,dictionary indexing Platform: "Linux" Platform:
-"MacOS X" Platform: "Windows" Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.7 Classifier: Programming
-Language :: Python :: 3.8 Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10 Classifier: Development
-Status :: 4 - Beta Classifier: Intended Audience :: Science/Research
-Classifier: License :: OSI Approved :: GNU General Public License v3 or later
-(GPLv3+) Classifier: Natural Language :: English Classifier: Operating System
-:: OS Independent Classifier: Topic :: Scientific/Engineering Classifier: Topic
-:: Scientific/Engineering :: Physics Requires-Python: >=3.7 Description-
-Content-Type: text/markdown Provides-Extra: doc Provides-Extra: tests Provides-
-Extra: all Provides-Extra: viz Provides-Extra: dev License-File: LICENSE
+Metadata-Version: 2.1 Name: kikuchipy Version: 0.8.4 Summary: Processing,
+simulating and indexing of electron backscatter diffraction (EBSD) patterns.
+Home-page: https://kikuchipy.org Download-URL: https://pypi.python.org/pypi/
+kikuchipy Author: kikuchipy developers Author-email: hakon.w.anes@ntnu.no
+Maintainer: HÃ¥kon Wiik Ãnes Maintainer-email: hakon.w.anes@ntnu.no License:
+GPLv3+ Project-URL: Bug Tracker, https://github.com/pyxem/kikuchipy/issues
+Project-URL: Documentation, https://kikuchipy.org Project-URL: Source Code,
+https://github.com/pyxem/kikuchipy Keywords: EBSD,electron backscatter
+diffraction,EBSP,electron backscatter pattern,BKD,backscatter kikuchi
+diffraction,SEM,scanning electron microscopy,kikuchi pattern,dictionary
+indexing Platform: "Linux" Platform: "MacOS X" Platform: "Windows" Classifier:
+Programming Language :: Python :: 3 Classifier: Programming Language :: Python
+:: 3.7 Classifier: Programming Language :: Python :: 3.8 Classifier:
+Programming Language :: Python :: 3.9 Classifier: Programming Language ::
+Python :: 3.10 Classifier: Development Status :: 4 - Beta Classifier: Intended
+Audience :: Science/Research Classifier: License :: OSI Approved :: GNU General
+Public License v3 or later (GPLv3+) Classifier: Natural Language :: English
+Classifier: Operating System :: OS Independent Classifier: Topic :: Scientific/
+Engineering Classifier: Topic :: Scientific/Engineering :: Physics Requires-
+Python: >=3.7 Description-Content-Type: text/markdown Provides-Extra: doc
+Provides-Extra: tests Provides-Extra: all Provides-Extra: viz Provides-Extra:
+dev License-File: LICENSE
  [https://raw.githubusercontent.com/pyxem/kikuchipy/develop/doc/_static/logo/
                               plasma_banner.png]
-kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and analyzing
-electron backscatter diffraction (EBSD) patterns in Python, built on the tools
-for multi-dimensional data analysis provided by the HyperSpy library. |
+kikuchipy [ki-ko-chi-pai] is a library for processing, simulating and indexing
+of electron backscatter diffraction (EBSD) patterns in Python, built on the
+tools for multi-dimensional data analysis provided by the HyperSpy library. |
 Deployment | [![PyPI version](https://img.shields.io/pypi/v/
 kikuchipy.svg?logo=python&logoColor=white)](https://pypi.org/project/kikuchipy/
 ) | [![Anaconda version](https://img.shields.io/conda/vn/conda-forge/
 kikuchipy.svg?logo=conda-forge&logoColor=white)](https://anaconda.org/conda-
 forge/kikuchipy)| | :- | :- | :- | | **Build status** | [![Test status](https:/
 /github.com/pyxem/kikuchipy/actions/workflows/tests.yml/badge.svg)](https://
 github.com/pyxem/kikuchipy/actions/workflows/tests.yml) | | **Documentation** |
```

### Comparing `kikuchipy-0.8.3/kikuchipy.egg-info/SOURCES.txt` & `kikuchipy-0.8.4/kikuchipy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/kikuchipy.egg-info/requires.txt` & `kikuchipy-0.8.4/kikuchipy.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/readthedocs.yaml` & `kikuchipy-0.8.4/readthedocs.yaml`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/setup.cfg` & `kikuchipy-0.8.4/setup.cfg`

 * *Files identical despite different names*

### Comparing `kikuchipy-0.8.3/setup.py` & `kikuchipy-0.8.4/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -93,16 +93,16 @@
     # Package description
     name=NAME,
     version=VERSION,
     license=LICENSE,
     url="https://kikuchipy.org",
     python_requires=">=3.7",
     description=(
-        "Processing and analysis of electron backscatter diffraction (EBSD) "
-        "patterns."
+        "Processing, simulating and indexing of electron backscatter diffraction "
+        "(EBSD) patterns."
     ),
     long_description=open("README.md", encoding="utf-8").read(),
     long_description_content_type="text/markdown",
     classifiers=[
         "Programming Language :: Python :: 3",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
```

