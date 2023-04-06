# Comparing `tmp/ephysiopy-1.8.96.tar.gz` & `tmp/ephysiopy-1.8.97.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ephysiopy-1.8.96.tar", last modified: Wed Apr  5 09:35:17 2023, max compression
+gzip compressed data, was "ephysiopy-1.8.97.tar", last modified: Thu Apr  6 14:50:32 2023, max compression
```

## Comparing `ephysiopy-1.8.96.tar` & `ephysiopy-1.8.97.tar`

### file list

```diff
@@ -1,64 +1,64 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/
--rw-r--r--   0 runner    (1001) docker     (123)     1065 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2812 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.466949 ephysiopy-1.8.96/ephysiopy/
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/__about__.py
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.466949 ephysiopy-1.8.96/ephysiopy/axona/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/axona/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19336 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/axona/axonaIO.py
--rw-r--r--   0 runner    (1001) docker     (123)    11999 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/axona/file_headers.py
--rw-r--r--   0 runner    (1001) docker     (123)     1364 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/axona/tetrode_dict.py
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/axona/tintcolours.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/ephysiopy/common/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    31243 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/binning.py
--rw-r--r--   0 runner    (1001) docker     (123)    21358 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/ephys_generic.py
--rw-r--r--   0 runner    (1001) docker     (123)    40221 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/fieldcalcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7148 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/gridcell.py
--rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/mle_von_mises_vals.py
--rw-r--r--   0 runner    (1001) docker     (123)    49463 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/phasecoding.py
--rw-r--r--   0 runner    (1001) docker     (123)    24931 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/rhythmicity.py
--rw-r--r--   0 runner    (1001) docker     (123)    28784 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/spikecalcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7121 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/statscalcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     7227 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/common/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/ephysiopy/format_converters/
--rw-r--r--   0 runner    (1001) docker     (123)    19711 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/format_converters/OE_Axona.py
--rw-r--r--   0 runner    (1001) docker     (123)     5930 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/format_converters/OE_numpy.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/format_converters/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/ephysiopy/io/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21614 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/io/recording.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/ephysiopy/openephys2py/
--rw-r--r--   0 runner    (1001) docker     (123)     6651 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/openephys2py/KiloSort.py
--rw-r--r--   0 runner    (1001) docker     (123)    10490 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/openephys2py/OESettings.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/openephys2py/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/ephysiopy/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      626 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_axona_headers.py
--rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_axona_io.py
--rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_binning.py
--rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_dacq2py.py
--rw-r--r--   0 runner    (1001) docker     (123)     9325 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_ephys_generic.py
--rw-r--r--   0 runner    (1001) docker     (123)     5073 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_fieldcalcs.py
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_gridcell.py
--rw-r--r--   0 runner    (1001) docker     (123)      149 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_openephys.py
--rw-r--r--   0 runner    (1001) docker     (123)     3092 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_phasecoding.py
--rw-r--r--   0 runner    (1001) docker     (123)     2014 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_rhythmicity.py
--rw-r--r--   0 runner    (1001) docker     (123)     3726 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_spikecalcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2062 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_statscalcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/tests/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/ephysiopy/visualise/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/visualise/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    31481 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/ephysiopy/visualise/plotting.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 09:35:17.466949 ephysiopy-1.8.96/ephysiopy.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-04-05 09:35:17.000000 ephysiopy-1.8.96/ephysiopy.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-04-05 09:35:17.000000 ephysiopy-1.8.96/ephysiopy.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 09:35:17.000000 ephysiopy-1.8.96/ephysiopy.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-05 09:35:17.000000 ephysiopy-1.8.96/ephysiopy.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-05 09:35:17.000000 ephysiopy-1.8.96/ephysiopy.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       79 2023-04-05 09:35:17.470949 ephysiopy-1.8.96/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-05 09:35:11.000000 ephysiopy-1.8.96/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.900210 ephysiopy-1.8.97/
+-rw-r--r--   0 runner    (1001) docker     (123)     1065 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-04-06 14:50:32.900210 ephysiopy-1.8.97/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2812 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy/
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/__about__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy/axona/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/axona/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19336 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/axona/axonaIO.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11999 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/axona/file_headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1364 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/axona/tetrode_dict.py
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/axona/tintcolours.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy/common/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31243 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/binning.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21358 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/ephys_generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    40221 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/fieldcalcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7148 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/gridcell.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/mle_von_mises_vals.py
+-rw-r--r--   0 runner    (1001) docker     (123)    49463 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/phasecoding.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24931 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/rhythmicity.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28784 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/spikecalcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7121 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/statscalcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7227 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/common/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy/format_converters/
+-rw-r--r--   0 runner    (1001) docker     (123)    19711 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/format_converters/OE_Axona.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5930 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/format_converters/OE_numpy.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/format_converters/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy/io/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21861 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/io/recording.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy/openephys2py/
+-rw-r--r--   0 runner    (1001) docker     (123)     6651 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/openephys2py/KiloSort.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10490 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/openephys2py/OESettings.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/openephys2py/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.900210 ephysiopy-1.8.97/ephysiopy/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      626 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_axona_headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_axona_io.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4100 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_binning.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3423 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_dacq2py.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9325 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_ephys_generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5073 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_fieldcalcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_gridcell.py
+-rw-r--r--   0 runner    (1001) docker     (123)      149 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_openephys.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3092 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_phasecoding.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2014 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_rhythmicity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3726 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_spikecalcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2062 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_statscalcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2113 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/tests/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.900210 ephysiopy-1.8.97/ephysiopy/visualise/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/visualise/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31481 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/ephysiopy/visualise/plotting.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 14:50:32.896209 ephysiopy-1.8.97/ephysiopy.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-04-06 14:50:32.000000 ephysiopy-1.8.97/ephysiopy.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-04-06 14:50:32.000000 ephysiopy-1.8.97/ephysiopy.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 14:50:32.000000 ephysiopy-1.8.97/ephysiopy.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-06 14:50:32.000000 ephysiopy-1.8.97/ephysiopy.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 14:50:32.000000 ephysiopy-1.8.97/ephysiopy.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       79 2023-04-06 14:50:32.900210 ephysiopy-1.8.97/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      981 2023-04-06 14:50:24.000000 ephysiopy-1.8.97/setup.py
```

### Comparing `ephysiopy-1.8.96/LICENSE` & `ephysiopy-1.8.97/LICENSE`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/PKG-INFO` & `ephysiopy-1.8.97/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ephysiopy
-Version: 1.8.96
+Version: 1.8.97
 Summary: Analysis of electrophysiology data
 Home-page: https://github.com/rhayman/ephysiopy
 Author: Robin Hayman
 Author-email: robin.hayman@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `ephysiopy-1.8.96/README.md` & `ephysiopy-1.8.97/README.md`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/axona/axonaIO.py` & `ephysiopy-1.8.97/ephysiopy/axona/axonaIO.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/axona/file_headers.py` & `ephysiopy-1.8.97/ephysiopy/axona/file_headers.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/axona/tetrode_dict.py` & `ephysiopy-1.8.97/ephysiopy/axona/tetrode_dict.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/axona/tintcolours.py` & `ephysiopy-1.8.97/ephysiopy/axona/tintcolours.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/binning.py` & `ephysiopy-1.8.97/ephysiopy/common/binning.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/ephys_generic.py` & `ephysiopy-1.8.97/ephysiopy/common/ephys_generic.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/fieldcalcs.py` & `ephysiopy-1.8.97/ephysiopy/common/fieldcalcs.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/gridcell.py` & `ephysiopy-1.8.97/ephysiopy/common/gridcell.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/mle_von_mises_vals.py` & `ephysiopy-1.8.97/ephysiopy/common/mle_von_mises_vals.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/phasecoding.py` & `ephysiopy-1.8.97/ephysiopy/common/phasecoding.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/rhythmicity.py` & `ephysiopy-1.8.97/ephysiopy/common/rhythmicity.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/spikecalcs.py` & `ephysiopy-1.8.97/ephysiopy/common/spikecalcs.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/statscalcs.py` & `ephysiopy-1.8.97/ephysiopy/common/statscalcs.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/common/utils.py` & `ephysiopy-1.8.97/ephysiopy/common/utils.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/format_converters/OE_Axona.py` & `ephysiopy-1.8.97/ephysiopy/format_converters/OE_Axona.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/format_converters/OE_numpy.py` & `ephysiopy-1.8.97/ephysiopy/format_converters/OE_numpy.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/io/recording.py` & `ephysiopy-1.8.97/ephysiopy/io/recording.py`

 * *Files 1% similar despite different names*

```diff
@@ -497,26 +497,30 @@
             # the older way:
             acq_method = "Neuropix-PXI-[0-9][0-9][0-9]."
             APdata_match = (exp_name / rec_name /
                             "continuous" / (acq_method + "0"))
             LFPdata_match = (exp_name / rec_name /
                              "continuous" / (acq_method + "1"))
             # the new way:
-            Rawdata_match = (exp_name / rec_name / 
+            Rawdata_match = (exp_name / rec_name /
                              "continuous" / (acq_method + "Probe[A-Z]"))
         elif self.rec_kind == RecordingKind.FPGA:
             acq_method = "Rhythm_FPGA-[0-9][0-9][0-9]."
             APdata_match = (exp_name / rec_name /
                             "continuous" / (acq_method + "0"))
             LFPdata_match = (exp_name / rec_name /
                              "continuous" / (acq_method + "1"))
+            Rawdata_match = (exp_name / rec_name /
+                             "continuous" / (acq_method + "Probe[A-Z]"))
         else:
             acq_method = "Acquisition_Board-[0-9][0-9][0-9].*"
             APdata_match = exp_name / rec_name / "continuous" / acq_method
             LFPdata_match = exp_name / rec_name / "continuous" / acq_method
+            Rawdata_match = (exp_name / rec_name /
+                             "continuous" / (acq_method + "Probe[A-Z]"))
         Events_match = (
             # only dealing with a single TTL channel at the moment
             exp_name / rec_name / "events" / acq_method / "TTL"
         )
 
         if pname_root is None:
             pname_root = self.pname_root
```

### Comparing `ephysiopy-1.8.96/ephysiopy/openephys2py/KiloSort.py` & `ephysiopy-1.8.97/ephysiopy/openephys2py/KiloSort.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/openephys2py/OESettings.py` & `ephysiopy-1.8.97/ephysiopy/openephys2py/OESettings.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/conftest.py` & `ephysiopy-1.8.97/ephysiopy/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_axona_headers.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_axona_headers.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_axona_io.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_axona_io.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_binning.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_binning.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_dacq2py.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_dacq2py.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_ephys_generic.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_ephys_generic.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_fieldcalcs.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_fieldcalcs.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_gridcell.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_gridcell.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_phasecoding.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_phasecoding.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_rhythmicity.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_rhythmicity.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_spikecalcs.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_spikecalcs.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_statscalcs.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_statscalcs.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/tests/test_utils.py` & `ephysiopy-1.8.97/ephysiopy/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy/visualise/plotting.py` & `ephysiopy-1.8.97/ephysiopy/visualise/plotting.py`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/ephysiopy.egg-info/PKG-INFO` & `ephysiopy-1.8.97/ephysiopy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ephysiopy
-Version: 1.8.96
+Version: 1.8.97
 Summary: Analysis of electrophysiology data
 Home-page: https://github.com/rhayman/ephysiopy
 Author: Robin Hayman
 Author-email: robin.hayman@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `ephysiopy-1.8.96/ephysiopy.egg-info/SOURCES.txt` & `ephysiopy-1.8.97/ephysiopy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ephysiopy-1.8.96/setup.py` & `ephysiopy-1.8.97/setup.py`

 * *Files identical despite different names*

