# Comparing `tmp/sxs-2022.4.4.tar.gz` & `tmp/sxs-2022.4.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sxs-2022.4.4.tar", max compression
+gzip compressed data, was "sxs-2022.4.5.tar", max compression
```

## Comparing `sxs-2022.4.4.tar` & `sxs-2022.4.5.tar`

### file list

```diff
@@ -1,85 +1,85 @@
--rw-r--r--   0        0        0     1080 2023-03-22 15:08:57.766780 sxs-2022.4.4/LICENSE
--rw-r--r--   0        0        0     5785 2023-03-22 15:08:57.766780 sxs-2022.4.4/README.md
--rw-r--r--   0        0        0     2653 2023-03-22 15:10:27.706827 sxs-2022.4.4/pyproject.toml
--rw-r--r--   0        0        0     2337 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/__init__.py
--rw-r--r--   0        0        0    14761 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/caltechdata/__init__.py
--rw-r--r--   0        0        0     4914 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/caltechdata/catalog.py
--rw-r--r--   0        0        0    21546 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/caltechdata/login.py
--rw-r--r--   0        0        0      205 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/catalog/__init__.py
--rw-r--r--   0        0        0    26481 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/catalog/catalog.py
--rw-r--r--   0        0        0     4734 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/catalog/create.py
--rw-r--r--   0        0        0    10830 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/catalog/description.py
--rw-r--r--   0        0        0    11405 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/handlers.py
--rw-r--r--   0        0        0    16277 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/horizons/__init__.py
--rw-r--r--   0        0        0     3642 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/horizons/spec_horizons_h5.py
--rw-r--r--   0        0        0     6536 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/horizons/xor_multishuffle_bzip2.py
--rw-r--r--   0        0        0      149 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/metadata/__init__.py
--rw-r--r--   0        0        0    27679 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/metadata/metadata.py
--rw-r--r--   0        0        0    25867 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/time_series.py
--rw-r--r--   0        0        0     4280 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/utilities/__init__.py
--rw-r--r--   0        0        0    13205 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/utilities/bitwise.py
--rw-r--r--   0        0        0     1336 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/utilities/decimation/__init__.py
--rw-r--r--   0        0        0     4335 2023-03-22 15:08:57.766780 sxs-2022.4.4/sxs/utilities/decimation/greedy_spline.py
--rw-r--r--   0        0        0     5357 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/decimation/linear_bisection.py
--rw-r--r--   0        0        0     6272 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/decimation/peak_greed.py
--rw-r--r--   0        0        0     1881 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/decimation/suppression.py
--rw-r--r--   0        0        0      695 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/dicts.py
--rw-r--r--   0        0        0     4488 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/downloads.py
--rw-r--r--   0        0        0     4517 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/files.py
--rw-r--r--   0        0        0     2620 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/formats.py
--rw-r--r--   0        0        0     8431 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/inspire.py
--rw-r--r--   0        0        0     1085 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/__init__.py
--rw-r--r--   0        0        0    12386 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/comparisons.py
--rw-r--r--   0        0        0    10447 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/conversion.py
--rw-r--r--   0        0        0     3732 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/dataset.py
--rw-r--r--   0        0        0    10447 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/horizons.py
--rw-r--r--   0        0        0    12385 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/metadata.py
--rw-r--r--   0        0        0     2799 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/waveform_amp_phase.py
--rw-r--r--   0        0        0     1929 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/lvcnr/waveforms.py
--rw-r--r--   0        0        0      812 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/monotonicity.py
--rw-r--r--   0        0        0     1473 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/pretty_print.py
--rw-r--r--   0        0        0      391 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/__init__.py
--rw-r--r--   0        0        0     8591 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/ads.py
--rw-r--r--   0        0        0     4264 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/arxiv.py
--rw-r--r--   0        0        0     1657 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/fairchild_report.py
--rw-r--r--   0        0        0     8431 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/inspire.py
--rw-r--r--   0        0        0    31018 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/journal_abbreviations.py
--rw-r--r--   0        0        0      418 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/references/references.py
--rw-r--r--   0        0        0     6727 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/select.py
--rw-r--r--   0        0        0     9676 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/sxs_directories.py
--rw-r--r--   0        0        0     3026 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/sxs_identifiers.py
--rw-r--r--   0        0        0     1850 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/utilities/url.py
--rw-r--r--   0        0        0      962 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/__init__.py
--rw-r--r--   0        0        0    12394 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/alignment.py
--rw-r--r--   0        0        0      126 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/corotating_paired_xor.py
--rw-r--r--   0        0        0     7763 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/memory.py
--rw-r--r--   0        0        0     5253 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/mode_utilities.py
--rw-r--r--   0        0        0    20427 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/nrar.py
--rw-r--r--   0        0        0    24057 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/rotating_paired_diff_multishuffle_bzip2.py
--rw-r--r--   0        0        0     2345 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/rotating_paired_xor_multishuffle_bzip2.py
--rw-r--r--   0        0        0     9124 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/transformations.py
--rw-r--r--   0        0        0      180 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/waveform_grid.py
--rw-r--r--   0        0        0     1299 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/waveform_mixin.py
--rw-r--r--   0        0        0    44544 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/waveform_modes.py
--rw-r--r--   0        0        0      182 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/waveforms/waveform_signal.py
--rw-r--r--   0        0        0    25890 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/__init__.py
--rw-r--r--   0        0        0      217 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/api/__init__.py
--rw-r--r--   0        0        0    36877 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/api/deposit.py
--rw-r--r--   0        0        0    18007 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/api/login.py
--rw-r--r--   0        0        0     3689 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/api/records.py
--rw-r--r--   0        0        0    28737 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/catalog.py
--rw-r--r--   0        0        0     2573 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/creators.py
--rw-r--r--   0        0        0     4491 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/simannex.py
--rw-r--r--   0        0        0     8381 2023-03-22 15:08:57.770780 sxs-2022.4.4/sxs/zenodo/surrogatemodeling.py
--rw-r--r--   0        0        0        1 2023-03-22 15:08:57.770780 sxs-2022.4.4/tests/__init__.py
--rw-r--r--   0        0        0     9174 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/conftest.py
--rw-r--r--   0        0        0     1462 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_catalog.py
--rw-r--r--   0        0        0     2098 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_horizons.py
--rw-r--r--   0        0        0     3135 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_loader.py
--rw-r--r--   0        0        0     1097 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_metadata.py
--rw-r--r--   0        0        0    13883 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_time_series.py
--rw-r--r--   0        0        0     1515 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_transformations.py
--rw-r--r--   0        0        0    10703 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_utilities.py
--rw-r--r--   0        0        0     7016 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_waveform_rotations.py
--rw-r--r--   0        0        0    11516 2023-03-22 15:08:57.774780 sxs-2022.4.4/tests/test_waveforms.py
--rw-r--r--   0        0        0     8417 1970-01-01 00:00:00.000000 sxs-2022.4.4/PKG-INFO
+-rw-r--r--   0        0        0     1080 2023-04-06 18:08:28.821729 sxs-2022.4.5/LICENSE
+-rw-r--r--   0        0        0     5785 2023-04-06 18:08:28.821729 sxs-2022.4.5/README.md
+-rw-r--r--   0        0        0     2653 2023-04-06 18:10:11.986228 sxs-2022.4.5/pyproject.toml
+-rw-r--r--   0        0        0     2337 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/__init__.py
+-rw-r--r--   0        0        0    14761 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/caltechdata/__init__.py
+-rw-r--r--   0        0        0     4914 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/caltechdata/catalog.py
+-rw-r--r--   0        0        0    21546 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/caltechdata/login.py
+-rw-r--r--   0        0        0      205 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/catalog/__init__.py
+-rw-r--r--   0        0        0    26481 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/catalog/catalog.py
+-rw-r--r--   0        0        0     4734 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/catalog/create.py
+-rw-r--r--   0        0        0    10830 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/catalog/description.py
+-rw-r--r--   0        0        0    11405 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/handlers.py
+-rw-r--r--   0        0        0    16277 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/horizons/__init__.py
+-rw-r--r--   0        0        0     3642 2023-04-06 18:08:28.821729 sxs-2022.4.5/sxs/horizons/spec_horizons_h5.py
+-rw-r--r--   0        0        0     6536 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/horizons/xor_multishuffle_bzip2.py
+-rw-r--r--   0        0        0      149 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/metadata/__init__.py
+-rw-r--r--   0        0        0    27679 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/metadata/metadata.py
+-rw-r--r--   0        0        0    25867 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/time_series.py
+-rw-r--r--   0        0        0     4280 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/__init__.py
+-rw-r--r--   0        0        0    13205 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/bitwise.py
+-rw-r--r--   0        0        0     1336 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/decimation/__init__.py
+-rw-r--r--   0        0        0     4335 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/decimation/greedy_spline.py
+-rw-r--r--   0        0        0     5357 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/decimation/linear_bisection.py
+-rw-r--r--   0        0        0     6272 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/decimation/peak_greed.py
+-rw-r--r--   0        0        0     1881 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/decimation/suppression.py
+-rw-r--r--   0        0        0      695 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/dicts.py
+-rw-r--r--   0        0        0     4488 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/downloads.py
+-rw-r--r--   0        0        0     4517 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/files.py
+-rw-r--r--   0        0        0     2620 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/formats.py
+-rw-r--r--   0        0        0     8431 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/inspire.py
+-rw-r--r--   0        0        0     1085 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/__init__.py
+-rw-r--r--   0        0        0    12386 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/comparisons.py
+-rw-r--r--   0        0        0    10447 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/conversion.py
+-rw-r--r--   0        0        0     3732 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/dataset.py
+-rw-r--r--   0        0        0    10447 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/horizons.py
+-rw-r--r--   0        0        0    12385 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/metadata.py
+-rw-r--r--   0        0        0     2799 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/waveform_amp_phase.py
+-rw-r--r--   0        0        0     1929 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/lvcnr/waveforms.py
+-rw-r--r--   0        0        0      812 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/monotonicity.py
+-rw-r--r--   0        0        0     1473 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/pretty_print.py
+-rw-r--r--   0        0        0      391 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/__init__.py
+-rw-r--r--   0        0        0     8591 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/ads.py
+-rw-r--r--   0        0        0     4264 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/arxiv.py
+-rw-r--r--   0        0        0     1657 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/fairchild_report.py
+-rw-r--r--   0        0        0     8431 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/inspire.py
+-rw-r--r--   0        0        0    31018 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/journal_abbreviations.py
+-rw-r--r--   0        0        0      418 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/references/references.py
+-rw-r--r--   0        0        0     6727 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/select.py
+-rw-r--r--   0        0        0     9676 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/sxs_directories.py
+-rw-r--r--   0        0        0     3026 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/sxs_identifiers.py
+-rw-r--r--   0        0        0     1850 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/utilities/url.py
+-rw-r--r--   0        0        0      962 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/__init__.py
+-rw-r--r--   0        0        0    12394 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/alignment.py
+-rw-r--r--   0        0        0      126 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/corotating_paired_xor.py
+-rw-r--r--   0        0        0     7763 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/memory.py
+-rw-r--r--   0        0        0     5253 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/mode_utilities.py
+-rw-r--r--   0        0        0    20427 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/nrar.py
+-rw-r--r--   0        0        0    24057 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/rotating_paired_diff_multishuffle_bzip2.py
+-rw-r--r--   0        0        0     2345 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/rotating_paired_xor_multishuffle_bzip2.py
+-rw-r--r--   0        0        0     9124 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/transformations.py
+-rw-r--r--   0        0        0      180 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/waveform_grid.py
+-rw-r--r--   0        0        0     1299 2023-04-06 18:08:28.825729 sxs-2022.4.5/sxs/waveforms/waveform_mixin.py
+-rw-r--r--   0        0        0    44544 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/waveforms/waveform_modes.py
+-rw-r--r--   0        0        0      182 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/waveforms/waveform_signal.py
+-rw-r--r--   0        0        0    25890 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/__init__.py
+-rw-r--r--   0        0        0      217 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/api/__init__.py
+-rw-r--r--   0        0        0    36877 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/api/deposit.py
+-rw-r--r--   0        0        0    18007 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/api/login.py
+-rw-r--r--   0        0        0     3689 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/api/records.py
+-rw-r--r--   0        0        0    28737 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/catalog.py
+-rw-r--r--   0        0        0     2573 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/creators.py
+-rw-r--r--   0        0        0     4491 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/simannex.py
+-rw-r--r--   0        0        0     8381 2023-04-06 18:08:28.829729 sxs-2022.4.5/sxs/zenodo/surrogatemodeling.py
+-rw-r--r--   0        0        0        1 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/__init__.py
+-rw-r--r--   0        0        0     9174 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/conftest.py
+-rw-r--r--   0        0        0     1462 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_catalog.py
+-rw-r--r--   0        0        0     2098 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_horizons.py
+-rw-r--r--   0        0        0     3135 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_loader.py
+-rw-r--r--   0        0        0     1097 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_metadata.py
+-rw-r--r--   0        0        0    13883 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_time_series.py
+-rw-r--r--   0        0        0     1515 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_transformations.py
+-rw-r--r--   0        0        0    10703 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_utilities.py
+-rw-r--r--   0        0        0     7016 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_waveform_rotations.py
+-rw-r--r--   0        0        0    11516 2023-04-06 18:08:28.829729 sxs-2022.4.5/tests/test_waveforms.py
+-rw-r--r--   0        0        0     8468 1970-01-01 00:00:00.000000 sxs-2022.4.5/PKG-INFO
```

### Comparing `sxs-2022.4.4/LICENSE` & `sxs-2022.4.5/LICENSE`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/README.md` & `sxs-2022.4.5/README.md`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/pyproject.toml` & `sxs-2022.4.5/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,19 +1,19 @@
 [tool.poetry]
 name = "sxs"
-version = "2022.4.4"
+version = "2022.4.5"
 description = "Interface to data produced by the Simulating eXtreme Spacetimes collaboration"
 readme = "README.md"
 license = "MIT"
 authors = ["Michael Boyle <michael.oliver.boyle@gmail.com>"]
 homepage = "https://github.com/sxs-collaboration/sxs"
 include = ["tests"]
 
 [tool.poetry.dependencies]
-python = ">=3.8,<3.11"
+python = ">=3.8,<3.12"
 numpy = "^1.20"
 scipy = "^1.0"
 numba = {version = ">=0.55", markers = "implementation_name == 'cpython'"}
 mkapi = {version = "1.0.13", optional = true, python = ">=3.7"}
 quaternionic = "^1.0"
 spherical = "^1.0"
 h5py = "^3"
```

### Comparing `sxs-2022.4.4/sxs/__init__.py` & `sxs-2022.4.5/sxs/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/caltechdata/__init__.py` & `sxs-2022.4.5/sxs/caltechdata/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/caltechdata/catalog.py` & `sxs-2022.4.5/sxs/caltechdata/catalog.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/caltechdata/login.py` & `sxs-2022.4.5/sxs/caltechdata/login.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/catalog/catalog.py` & `sxs-2022.4.5/sxs/catalog/catalog.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/catalog/create.py` & `sxs-2022.4.5/sxs/catalog/create.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/catalog/description.py` & `sxs-2022.4.5/sxs/catalog/description.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/handlers.py` & `sxs-2022.4.5/sxs/handlers.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/horizons/__init__.py` & `sxs-2022.4.5/sxs/horizons/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/horizons/spec_horizons_h5.py` & `sxs-2022.4.5/sxs/horizons/spec_horizons_h5.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/horizons/xor_multishuffle_bzip2.py` & `sxs-2022.4.5/sxs/horizons/xor_multishuffle_bzip2.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/metadata/metadata.py` & `sxs-2022.4.5/sxs/metadata/metadata.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/time_series.py` & `sxs-2022.4.5/sxs/time_series.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/__init__.py` & `sxs-2022.4.5/sxs/utilities/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/bitwise.py` & `sxs-2022.4.5/sxs/utilities/bitwise.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/decimation/__init__.py` & `sxs-2022.4.5/sxs/utilities/decimation/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/decimation/greedy_spline.py` & `sxs-2022.4.5/sxs/utilities/decimation/greedy_spline.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/decimation/linear_bisection.py` & `sxs-2022.4.5/sxs/utilities/decimation/linear_bisection.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/decimation/peak_greed.py` & `sxs-2022.4.5/sxs/utilities/decimation/peak_greed.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/decimation/suppression.py` & `sxs-2022.4.5/sxs/utilities/decimation/suppression.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/dicts.py` & `sxs-2022.4.5/sxs/utilities/dicts.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/downloads.py` & `sxs-2022.4.5/sxs/utilities/downloads.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/files.py` & `sxs-2022.4.5/sxs/utilities/files.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/formats.py` & `sxs-2022.4.5/sxs/utilities/formats.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/inspire.py` & `sxs-2022.4.5/sxs/utilities/inspire.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/__init__.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/comparisons.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/comparisons.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/conversion.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/conversion.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/dataset.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/dataset.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/horizons.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/horizons.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/metadata.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/metadata.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/waveform_amp_phase.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/waveform_amp_phase.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/lvcnr/waveforms.py` & `sxs-2022.4.5/sxs/utilities/lvcnr/waveforms.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/monotonicity.py` & `sxs-2022.4.5/sxs/utilities/monotonicity.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/pretty_print.py` & `sxs-2022.4.5/sxs/utilities/pretty_print.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/references/ads.py` & `sxs-2022.4.5/sxs/utilities/references/ads.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/references/arxiv.py` & `sxs-2022.4.5/sxs/utilities/references/arxiv.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/references/fairchild_report.py` & `sxs-2022.4.5/sxs/utilities/references/fairchild_report.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/references/inspire.py` & `sxs-2022.4.5/sxs/utilities/references/inspire.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/references/journal_abbreviations.py` & `sxs-2022.4.5/sxs/utilities/references/journal_abbreviations.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/select.py` & `sxs-2022.4.5/sxs/utilities/select.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/sxs_directories.py` & `sxs-2022.4.5/sxs/utilities/sxs_directories.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/sxs_identifiers.py` & `sxs-2022.4.5/sxs/utilities/sxs_identifiers.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/utilities/url.py` & `sxs-2022.4.5/sxs/utilities/url.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/__init__.py` & `sxs-2022.4.5/sxs/waveforms/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/alignment.py` & `sxs-2022.4.5/sxs/waveforms/alignment.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/memory.py` & `sxs-2022.4.5/sxs/waveforms/memory.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/mode_utilities.py` & `sxs-2022.4.5/sxs/waveforms/mode_utilities.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/nrar.py` & `sxs-2022.4.5/sxs/waveforms/nrar.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/rotating_paired_diff_multishuffle_bzip2.py` & `sxs-2022.4.5/sxs/waveforms/rotating_paired_diff_multishuffle_bzip2.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/rotating_paired_xor_multishuffle_bzip2.py` & `sxs-2022.4.5/sxs/waveforms/rotating_paired_xor_multishuffle_bzip2.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/transformations.py` & `sxs-2022.4.5/sxs/waveforms/transformations.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/waveform_mixin.py` & `sxs-2022.4.5/sxs/waveforms/waveform_mixin.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/waveforms/waveform_modes.py` & `sxs-2022.4.5/sxs/waveforms/waveform_modes.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/__init__.py` & `sxs-2022.4.5/sxs/zenodo/__init__.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/api/deposit.py` & `sxs-2022.4.5/sxs/zenodo/api/deposit.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/api/login.py` & `sxs-2022.4.5/sxs/zenodo/api/login.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/api/records.py` & `sxs-2022.4.5/sxs/zenodo/api/records.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/catalog.py` & `sxs-2022.4.5/sxs/zenodo/catalog.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/creators.py` & `sxs-2022.4.5/sxs/zenodo/creators.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/simannex.py` & `sxs-2022.4.5/sxs/zenodo/simannex.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/sxs/zenodo/surrogatemodeling.py` & `sxs-2022.4.5/sxs/zenodo/surrogatemodeling.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/conftest.py` & `sxs-2022.4.5/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_catalog.py` & `sxs-2022.4.5/tests/test_catalog.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_horizons.py` & `sxs-2022.4.5/tests/test_horizons.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_loader.py` & `sxs-2022.4.5/tests/test_loader.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_metadata.py` & `sxs-2022.4.5/tests/test_metadata.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_time_series.py` & `sxs-2022.4.5/tests/test_time_series.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_transformations.py` & `sxs-2022.4.5/tests/test_transformations.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_utilities.py` & `sxs-2022.4.5/tests/test_utilities.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_waveform_rotations.py` & `sxs-2022.4.5/tests/test_waveform_rotations.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/tests/test_waveforms.py` & `sxs-2022.4.5/tests/test_waveforms.py`

 * *Files identical despite different names*

### Comparing `sxs-2022.4.4/PKG-INFO` & `sxs-2022.4.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,21 +1,22 @@
 Metadata-Version: 2.1
 Name: sxs
-Version: 2022.4.4
+Version: 2022.4.5
 Summary: Interface to data produced by the Simulating eXtreme Spacetimes collaboration
 Home-page: https://github.com/sxs-collaboration/sxs
 License: MIT
 Author: Michael Boyle
 Author-email: michael.oliver.boyle@gmail.com
-Requires-Python: >=3.8,<3.11
+Requires-Python: >=3.8,<3.12
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Provides-Extra: ecosystem
 Provides-Extra: mkapi
 Provides-Extra: mkdocs
 Provides-Extra: pymdown-extensions
 Requires-Dist: black (>=22.1) ; implementation_name == "cpython"
 Requires-Dist: caltechdata-api (>=0.3.0,<0.4.0)
 Requires-Dist: corner (>=2.1.0,<3.0.0) ; extra == "ecosystem"
```

