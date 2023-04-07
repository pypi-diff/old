# Comparing `tmp/miv_os-0.3.0.post2.tar.gz` & `tmp/miv_os-0.3.0b0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "miv_os-0.3.0.post2.tar", max compression
+gzip compressed data, was "miv_os-0.3.0b0.tar", max compression
```

## Comparing `miv_os-0.3.0.post2.tar` & `miv_os-0.3.0b0.tar`

### file list

```diff
@@ -1,138 +1,100 @@
--rw-r--r--   0        0        0     1068 2023-02-17 02:51:17.972520 miv_os-0.3.0.post2/LICENSE
--rw-r--r--   0        0        0     2642 2023-02-17 02:51:17.972721 miv_os-0.3.0.post2/README.md
--rw-r--r--   0        0        0      380 2023-02-17 02:49:11.755963 miv_os-0.3.0.post2/miv/__init__.py
--rw-r--r--   0        0        0        0 2023-02-17 02:50:08.291815 miv_os-0.3.0.post2/miv/coding/__init__.py
--rw-r--r--   0        0        0        0 2023-02-17 02:50:08.291892 miv_os-0.3.0.post2/miv/coding/spatial/__init__.py
--rw-r--r--   0        0        0      257 2023-02-17 02:50:08.322053 miv_os-0.3.0.post2/miv/coding/temporal/__init__.py
--rw-r--r--   0        0        0     4260 2023-01-31 04:15:17.268239 miv_os-0.3.0.post2/miv/coding/temporal/decoding.py
--rw-r--r--   0        0        0     8163 2023-03-08 06:34:33.244608 miv_os-0.3.0.post2/miv/coding/temporal/encoding.py
--rw-r--r--   0        0        0     2378 2023-02-17 02:50:08.302197 miv_os-0.3.0.post2/miv/coding/temporal/lyon.py
--rw-r--r--   0        0        0     8744 2023-01-31 04:15:17.241778 miv_os-0.3.0.post2/miv/coding/temporal/main.py
--rw-r--r--   0        0        0      638 2023-02-17 02:51:05.255599 miv_os-0.3.0.post2/miv/coding/temporal/protocol.py
--rw-r--r--   0        0        0     4974 2023-02-17 02:50:09.362560 miv_os-0.3.0.post2/miv/coding/temporal/spiker.py
--rw-r--r--   0        0        0     4098 2023-01-31 04:15:17.174065 miv_os-0.3.0.post2/miv/coding/temporal/tbr.py
--rw-r--r--   0        0        0        0 2023-02-27 18:21:57.703061 miv_os-0.3.0.post2/miv/core/__init__.py
--rw-r--r--   0        0        0      357 2023-04-02 20:42:52.416666 miv_os-0.3.0.post2/miv/core/datatype/__init__.py
--rw-r--r--   0        0        0      491 2023-03-10 08:24:34.880051 miv_os-0.3.0.post2/miv/core/datatype/collapsable.py
--rw-r--r--   0        0        0     2811 2023-03-06 15:59:56.073711 miv_os-0.3.0.post2/miv/core/datatype/events.py
--rw-r--r--   0        0        0      617 2023-03-05 23:23:55.095361 miv_os-0.3.0.post2/miv/core/datatype/protocol.py
--rw-r--r--   0        0        0     1108 2023-04-02 23:17:52.095754 miv_os-0.3.0.post2/miv/core/datatype/pure_python.py
--rw-r--r--   0        0        0     2847 2023-04-05 14:20:59.047803 miv_os-0.3.0.post2/miv/core/datatype/signal.py
--rw-r--r--   0        0        0     5973 2023-04-05 14:20:59.136699 miv_os-0.3.0.post2/miv/core/datatype/spikestamps.py
--rw-r--r--   0        0        0     3294 2023-04-01 01:20:55.125214 miv_os-0.3.0.post2/miv/core/functools.py
--rw-r--r--   0        0        0       83 2023-03-28 18:36:25.661988 miv_os-0.3.0.post2/miv/core/operator/__init__.py
--rw-r--r--   0        0        0     6566 2023-04-02 18:33:56.727123 miv_os-0.3.0.post2/miv/core/operator/cachable.py
--rw-r--r--   0        0        0     3500 2023-03-18 22:58:10.546676 miv_os-0.3.0.post2/miv/core/operator/callback.py
--rw-r--r--   0        0        0     5891 2023-04-02 23:18:00.943170 miv_os-0.3.0.post2/miv/core/operator/chainable.py
--rw-r--r--   0        0        0     4118 2023-04-05 15:25:42.981482 miv_os-0.3.0.post2/miv/core/operator/operator.py
--rw-r--r--   0        0        0     2505 2023-04-05 15:25:42.981813 miv_os-0.3.0.post2/miv/core/pipeline.py
--rw-r--r--   0        0        0     2602 2023-04-04 20:33:12.510303 miv_os-0.3.0.post2/miv/core/policy.py
--rw-r--r--   0        0        0     5001 2023-02-27 18:22:02.785552 miv_os-0.3.0.post2/miv/core/spikestamps.py
--rw-r--r--   0        0        0     3571 2023-04-01 05:30:41.811137 miv_os-0.3.0.post2/miv/core/wrapper.py
--rw-r--r--   0        0        0      298 2023-02-17 19:46:01.162545 miv_os-0.3.0.post2/miv/datasets/__init__.py
--rw-r--r--   0        0        0      856 2023-02-17 02:49:59.835874 miv_os-0.3.0.post2/miv/datasets/criticality.py
--rw-r--r--   0        0        0     1924 2023-04-01 05:30:41.812866 miv_os-0.3.0.post2/miv/datasets/openephys_sample.py
--rw-r--r--   0        0        0     2616 2023-02-20 19:27:13.602817 miv_os-0.3.0.post2/miv/datasets/optogenetic.py
--rw-r--r--   0        0        0        0 2023-02-17 02:49:19.591516 miv_os-0.3.0.post2/miv/datasets/protocol.py
--rw-r--r--   0        0        0     2190 2023-02-20 19:27:13.604343 miv_os-0.3.0.post2/miv/datasets/ttl_events.py
--rw-r--r--   0        0        0     8869 2023-04-01 04:24:17.494662 miv_os-0.3.0.post2/miv/datasets/utils.py
--rw-r--r--   0        0        0        0 2023-02-20 19:27:13.604621 miv_os-0.3.0.post2/miv/io/__init__.py
--rw-r--r--   0        0        0       31 2023-02-20 19:27:13.605455 miv_os-0.3.0.post2/miv/io/asdf/__init__.py
--rw-r--r--   0        0        0     1478 2023-04-01 05:30:41.815894 miv_os-0.3.0.post2/miv/io/asdf/asdf.py
--rw-r--r--   0        0        0      366 2023-02-17 02:50:18.810939 miv_os-0.3.0.post2/miv/io/file/__init__.py
--rw-r--r--   0        0        0    13907 2023-02-17 02:50:18.822068 miv_os-0.3.0.post2/miv/io/file/read.py
--rw-r--r--   0        0        0    18207 2023-02-17 02:51:04.365296 miv_os-0.3.0.post2/miv/io/file/write.py
--rw-r--r--   0        0        0       32 2023-02-17 02:51:06.069502 miv_os-0.3.0.post2/miv/io/intan/__init__.py
--rw-r--r--   0        0        0    12176 2023-03-26 23:26:52.438679 miv_os-0.3.0.post2/miv/io/intan/data.py
--rw-r--r--   0        0        0    41764 2023-02-22 20:49:17.911050 miv_os-0.3.0.post2/miv/io/intan/rhs.py
--rw-r--r--   0        0        0       74 2023-02-20 19:27:13.608834 miv_os-0.3.0.post2/miv/io/openephys/__init__.py
--rw-r--r--   0        0        0    13601 2023-04-01 05:30:41.844249 miv_os-0.3.0.post2/miv/io/openephys/binary.py
--rw-r--r--   0        0        0    26358 2023-03-06 16:40:02.926119 miv_os-0.3.0.post2/miv/io/openephys/data.py
--rw-r--r--   0        0        0      809 2023-02-17 02:51:19.193218 miv_os-0.3.0.post2/miv/io/protocol.py
--rw-r--r--   0        0        0       72 2023-02-17 02:50:15.108187 miv_os-0.3.0.post2/miv/io/serial/__init__.py
--rw-r--r--   0        0        0     3689 2023-02-17 02:51:05.267655 miv_os-0.3.0.post2/miv/io/serial/arduino.py
--rw-r--r--   0        0        0     2931 2023-02-17 02:51:05.287606 miv_os-0.3.0.post2/miv/io/serial/stimjim.py
--rw-r--r--   0        0        0      120 2023-02-20 19:27:13.611092 miv_os-0.3.0.post2/miv/machinary/README.md
--rw-r--r--   0        0        0     2424 2023-02-20 19:27:13.611267 miv_os-0.3.0.post2/miv/machinary/convert_open_ephys_to_miv.py
--rw-r--r--   0        0        0     2578 2023-03-02 21:17:42.423245 miv_os-0.3.0.post2/miv/machinary/miv_extract_spiketrain.py
--rw-r--r--   0        0        0     4049 2023-03-28 18:36:25.665859 miv_os-0.3.0.post2/miv/mea/__init__.py
--rw-r--r--   0        0        0     1227 2023-04-06 17:58:21.223735 miv_os-0.3.0.post2/miv/mea/base.py
--rw-r--r--   0        0        0     7163 2023-03-18 22:58:10.548820 miv_os-0.3.0.post2/miv/mea/channel_mapping.py
--rw-r--r--   0        0        0     1916 2023-04-02 18:17:06.015023 miv_os-0.3.0.post2/miv/mea/grid.py
--rw-r--r--   0        0        0      971 2023-04-02 20:42:52.426567 miv_os-0.3.0.post2/miv/mea/protocol.py
--rw-r--r--   0        0        0     2050 2023-04-04 04:34:40.395498 miv_os-0.3.0.post2/miv/mea/unstructured.py
--rw-r--r--   0        0        0        0 2023-02-17 02:48:47.210081 miv_os-0.3.0.post2/miv/py.typed
--rw-r--r--   0        0        0        0 2023-02-17 02:46:54.913196 miv_os-0.3.0.post2/miv/signal/__init__.py
--rw-r--r--   0        0        0       41 2023-02-21 02:46:09.810799 miv_os-0.3.0.post2/miv/signal/events/__init__.py
--rw-r--r--   0        0        0     6473 2023-03-07 13:30:05.094683 miv_os-0.3.0.post2/miv/signal/events/waveform.py
--rw-r--r--   0        0        0      187 2023-02-25 05:44:59.740634 miv_os-0.3.0.post2/miv/signal/filter/__init__.py
--rw-r--r--   0        0        0     4195 2023-03-31 20:44:22.867624 miv_os-0.3.0.post2/miv/signal/filter/butter_bandpass_filter.py
--rw-r--r--   0        0        0     2372 2023-02-22 00:29:27.022325 miv_os-0.3.0.post2/miv/signal/filter/median_filter.py
--rw-r--r--   0        0        0     2287 2023-04-05 15:22:50.317443 miv_os-0.3.0.post2/miv/signal/filter/notch_filter.py
--rw-r--r--   0        0        0      638 2023-02-20 19:27:13.614284 miv_os-0.3.0.post2/miv/signal/filter/protocol.py
--rw-r--r--   0        0        0       52 2023-02-17 02:49:56.641590 miv_os-0.3.0.post2/miv/signal/generator/__init__.py
--rw-r--r--   0        0        0     1958 2023-02-17 02:49:59.611712 miv_os-0.3.0.post2/miv/signal/generator/spike_generation.py
--rw-r--r--   0        0        0      173 2023-02-17 02:51:25.478478 miv_os-0.3.0.post2/miv/signal/similarity/__init__.py
--rw-r--r--   0        0        0        0 2023-02-17 02:51:24.283504 miv_os-0.3.0.post2/miv/signal/similarity/distance.py
--rw-r--r--   0        0        0     2353 2023-02-17 02:51:24.298353 miv_os-0.3.0.post2/miv/signal/similarity/dtw.py
--rw-r--r--   0        0        0        0 2023-02-17 02:51:24.273574 miv_os-0.3.0.post2/miv/signal/similarity/protocol.py
--rw-r--r--   0        0        0     2726 2023-02-17 02:51:25.550561 miv_os-0.3.0.post2/miv/signal/similarity/simple.py
--rw-r--r--   0        0        0      120 2023-02-17 02:48:47.211402 miv_os-0.3.0.post2/miv/signal/spike/__init__.py
--rw-r--r--   0        0        0    11830 2023-04-01 05:30:41.847197 miv_os-0.3.0.post2/miv/signal/spike/detection.py
--rw-r--r--   0        0        0     1108 2023-02-17 02:48:47.212004 miv_os-0.3.0.post2/miv/signal/spike/protocol.py
--rw-r--r--   0        0        0    11935 2023-04-01 05:30:41.857614 miv_os-0.3.0.post2/miv/signal/spike/sorting.py
--rw-r--r--   0        0        0      315 2023-03-06 04:34:05.311150 miv_os-0.3.0.post2/miv/statistics/__init__.py
--rw-r--r--   0        0        0     2864 2023-03-17 22:43:20.793121 miv_os-0.3.0.post2/miv/statistics/burst.py
--rw-r--r--   0        0        0      108 2023-02-24 02:44:54.770327 miv_os-0.3.0.post2/miv/statistics/connectivity/__init__.py
--rw-r--r--   0        0        0     2412 2023-04-01 01:11:17.555945 miv_os-0.3.0.post2/miv/statistics/connectivity/centrality.py
--rw-r--r--   0        0        0    12742 2023-04-02 18:30:14.726055 miv_os-0.3.0.post2/miv/statistics/connectivity/connectivity.py
--rw-r--r--   0        0        0      157 2023-03-05 23:05:56.017548 miv_os-0.3.0.post2/miv/statistics/connectivity/utils.py
--rw-r--r--   0        0        0     2729 2016-01-14 23:36:10.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/asdf2toraster.m
--rw-r--r--   0        0        0     8109 2016-02-16 22:02:16.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/avgshapes.m
--rw-r--r--   0        0        0     6924 2023-03-20 02:17:16.035552 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/avprops.m
--rw-r--r--   0        0        0    11012 2016-04-14 20:33:44.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/avpropvals.m
--rw-r--r--   0        0        0     9767 2016-04-15 02:28:44.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/avshapecollapse.m
--rw-r--r--   0        0        0     5541 2016-04-15 02:30:20.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/avshapecollapsestd.m
--rw-r--r--   0        0        0     8353 2016-01-14 23:39:16.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/bethelattice.m
--rw-r--r--   0        0        0     4737 2016-02-24 14:31:04.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/brestimate.m
--rw-r--r--   0        0        0    10561 2016-01-14 23:40:06.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/cbmodel.m
--rw-r--r--   0        0        0     7960 2016-04-15 18:13:44.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/complexity/complexity.m
--rw-r--r--   0        0        0    10001 2016-02-16 20:48:24.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/complexity/complexityexamples.m
--rw-r--r--   0        0        0     3744 2016-04-15 18:27:40.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/complexity/democomplexity.m
--rw-r--r--   0        0        0     4460 2016-04-15 02:16:02.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/demoempdata.m
--rw-r--r--   0        0        0     7503 2016-04-13 18:44:34.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/demoplotting.m
--rw-r--r--   0        0        0     3859 2016-01-14 23:48:08.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/demotruncdist.m
--rw-r--r--   0        0        0     2954 2023-03-17 22:11:24.083798 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/findAvas.m
--rw-r--r--   0        0        0     8498 2016-04-25 21:47:22.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/gendata.m
--rw-r--r--   0        0        0     5023 2016-01-14 23:42:28.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/mymnrnd.m
--rw-r--r--   0        0        0     6910 2016-04-13 19:30:28.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/pldist.m
--rw-r--r--   0        0        0     6142 2016-04-16 02:18:02.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/plmle.m
--rw-r--r--   0        0        0     7468 2016-04-14 03:10:42.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/plparams.m
--rw-r--r--   0        0        0    17251 2016-04-14 20:00:34.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/plplottool.m
--rw-r--r--   0        0        0    10759 2016-04-25 21:50:38.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/pvcalc.m
--rw-r--r--   0        0        0    13447 2016-04-14 20:37:36.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/randomizeasdf2.m
--rw-r--r--   0        0        0     5745 2016-01-14 23:45:24.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/rastertoasdf2.m
--rw-r--r--   0        0        0     3233 2016-01-14 23:45:42.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/rebin.m
--rw-r--r--   0        0        0      897 2014-10-17 18:15:36.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/rldecode.m
--rw-r--r--   0        0        0   144450 2015-08-31 16:05:10.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/sample_data.mat
--rw-r--r--   0        0        0     6202 2016-01-14 23:46:12.000000 miv_os-0.3.0.post2/miv/statistics/criticality/CritAnalysisSoftwarePackage2016-04-25/sizegivdurwls.m
--rw-r--r--   0        0        0       60 2023-03-17 23:58:48.759075 miv_os-0.3.0.post2/miv/statistics/criticality/__init__.py
--rw-r--r--   0        0        0    12898 2023-04-05 14:14:10.251199 miv_os-0.3.0.post2/miv/statistics/criticality/avalanche_analysis.py
--rw-r--r--   0        0        0    17848 2023-04-06 17:24:18.874748 miv_os-0.3.0.post2/miv/statistics/info_theory.py
--rw-r--r--   0        0        0     1546 2023-02-17 02:50:01.180711 miv_os-0.3.0.post2/miv/statistics/pairwise_causality.py
--rw-r--r--   0        0        0     7067 2023-03-26 23:26:52.364112 miv_os-0.3.0.post2/miv/statistics/peristimulus_analysis.py
--rw-r--r--   0        0        0     2201 2023-03-03 15:34:43.907404 miv_os-0.3.0.post2/miv/statistics/signal_statistics.py
--rw-r--r--   0        0        0     8256 2023-03-29 05:04:28.344659 miv_os-0.3.0.post2/miv/statistics/spiketrain_statistics.py
--rw-r--r--   0        0        0      407 2023-02-20 19:27:13.615772 miv_os-0.3.0.post2/miv/typing.py
--rw-r--r--   0        0        0      252 2023-03-27 22:04:36.585080 miv_os-0.3.0.post2/miv/visualization/__init__.py
--rw-r--r--   0        0        0     4508 2023-04-07 03:39:00.304684 miv_os-0.3.0.post2/miv/visualization/activity.py
--rw-r--r--   0        0        0     4196 2023-03-03 16:32:29.123962 miv_os-0.3.0.post2/miv/visualization/causality.py
--rw-r--r--   0        0        0     5056 2023-02-17 02:50:09.430625 miv_os-0.3.0.post2/miv/visualization/connectivity.py
--rw-r--r--   0        0        0     1228 2023-02-17 02:49:28.749021 miv_os-0.3.0.post2/miv/visualization/event.py
--rw-r--r--   0        0        0     3196 2023-02-17 02:50:08.331531 miv_os-0.3.0.post2/miv/visualization/fft_domain.py
--rw-r--r--   0        0        0     6497 2023-03-29 06:10:44.532416 miv_os-0.3.0.post2/miv/visualization/raw_signal.py
--rw-r--r--   0        0        0     1586 2023-04-01 01:20:55.194893 miv_os-0.3.0.post2/miv/visualization/test.py
--rw-r--r--   0        0        0      625 2023-03-28 18:36:25.671409 miv_os-0.3.0.post2/miv/visualization/utils.py
--rw-r--r--   0        0        0     6139 2023-04-07 03:40:31.480943 miv_os-0.3.0.post2/pyproject.toml
--rw-r--r--   0        0        0    64350 1970-01-01 00:00:00.000000 miv_os-0.3.0.post2/setup.py
--rw-r--r--   0        0        0     5471 1970-01-01 00:00:00.000000 miv_os-0.3.0.post2/PKG-INFO
+-rw-r--r--   0        0        0     1068 2023-02-17 02:51:17.972520 miv_os-0.3.0b0/LICENSE
+-rw-r--r--   0        0        0     2642 2023-02-17 02:51:17.972721 miv_os-0.3.0b0/README.md
+-rw-r--r--   0        0        0      380 2023-02-17 02:49:11.755963 miv_os-0.3.0b0/miv/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-17 02:50:08.291815 miv_os-0.3.0b0/miv/coding/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-17 02:50:08.291892 miv_os-0.3.0b0/miv/coding/spatial/__init__.py
+-rw-r--r--   0        0        0      257 2023-02-17 02:50:08.322053 miv_os-0.3.0b0/miv/coding/temporal/__init__.py
+-rw-r--r--   0        0        0     4260 2023-01-31 04:15:17.268239 miv_os-0.3.0b0/miv/coding/temporal/decoding.py
+-rw-r--r--   0        0        0     8163 2023-03-08 06:34:33.244608 miv_os-0.3.0b0/miv/coding/temporal/encoding.py
+-rw-r--r--   0        0        0     2378 2023-02-17 02:50:08.302197 miv_os-0.3.0b0/miv/coding/temporal/lyon.py
+-rw-r--r--   0        0        0     8744 2023-01-31 04:15:17.241778 miv_os-0.3.0b0/miv/coding/temporal/main.py
+-rw-r--r--   0        0        0      638 2023-02-17 02:51:05.255599 miv_os-0.3.0b0/miv/coding/temporal/protocol.py
+-rw-r--r--   0        0        0     4974 2023-02-17 02:50:09.362560 miv_os-0.3.0b0/miv/coding/temporal/spiker.py
+-rw-r--r--   0        0        0     4098 2023-01-31 04:15:17.174065 miv_os-0.3.0b0/miv/coding/temporal/tbr.py
+-rw-r--r--   0        0        0        0 2023-02-27 18:21:57.703061 miv_os-0.3.0b0/miv/core/__init__.py
+-rw-r--r--   0        0        0      313 2023-03-06 15:59:20.486368 miv_os-0.3.0b0/miv/core/datatype/__init__.py
+-rw-r--r--   0        0        0      491 2023-03-10 08:24:34.880051 miv_os-0.3.0b0/miv/core/datatype/collapsable.py
+-rw-r--r--   0        0        0     2811 2023-03-06 15:59:56.073711 miv_os-0.3.0b0/miv/core/datatype/events.py
+-rw-r--r--   0        0        0      617 2023-03-05 23:23:55.095361 miv_os-0.3.0b0/miv/core/datatype/protocol.py
+-rw-r--r--   0        0        0     2688 2023-03-10 23:54:13.548657 miv_os-0.3.0b0/miv/core/datatype/signal.py
+-rw-r--r--   0        0        0     5691 2023-03-12 15:22:13.842894 miv_os-0.3.0b0/miv/core/datatype/spikestamps.py
+-rw-r--r--   0        0        0       41 2023-02-20 19:27:13.593964 miv_os-0.3.0b0/miv/core/operator/__init__.py
+-rw-r--r--   0        0        0     5913 2023-03-11 00:34:08.858097 miv_os-0.3.0b0/miv/core/operator/cachable.py
+-rw-r--r--   0        0        0     3409 2023-03-07 13:30:07.627809 miv_os-0.3.0b0/miv/core/operator/callback.py
+-rw-r--r--   0        0        0     5648 2023-03-11 05:27:12.356307 miv_os-0.3.0b0/miv/core/operator/chainable.py
+-rw-r--r--   0        0        0     4186 2023-03-10 07:44:12.323002 miv_os-0.3.0b0/miv/core/operator/operator.py
+-rw-r--r--   0        0        0     2345 2023-03-11 05:26:22.985246 miv_os-0.3.0b0/miv/core/pipeline.py
+-rw-r--r--   0        0        0     1926 2023-03-11 04:47:38.525067 miv_os-0.3.0b0/miv/core/policy.py
+-rw-r--r--   0        0        0     5001 2023-02-27 18:22:02.785552 miv_os-0.3.0b0/miv/core/spikestamps.py
+-rw-r--r--   0        0        0     3580 2023-03-11 04:54:57.232715 miv_os-0.3.0b0/miv/core/wrapper.py
+-rw-r--r--   0        0        0      298 2023-02-17 19:46:01.162545 miv_os-0.3.0b0/miv/datasets/__init__.py
+-rw-r--r--   0        0        0      856 2023-02-17 02:49:59.835874 miv_os-0.3.0b0/miv/datasets/criticality.py
+-rw-r--r--   0        0        0     1924 2023-02-20 20:33:34.897648 miv_os-0.3.0b0/miv/datasets/openephys_sample.py
+-rw-r--r--   0        0        0     2616 2023-02-20 19:27:13.602817 miv_os-0.3.0b0/miv/datasets/optogenetic.py
+-rw-r--r--   0        0        0        0 2023-02-17 02:49:19.591516 miv_os-0.3.0b0/miv/datasets/protocol.py
+-rw-r--r--   0        0        0     2190 2023-02-20 19:27:13.604343 miv_os-0.3.0b0/miv/datasets/ttl_events.py
+-rw-r--r--   0        0        0     8869 2023-02-20 21:24:09.427622 miv_os-0.3.0b0/miv/datasets/utils.py
+-rw-r--r--   0        0        0        0 2023-02-20 19:27:13.604621 miv_os-0.3.0b0/miv/io/__init__.py
+-rw-r--r--   0        0        0       31 2023-02-20 19:27:13.605455 miv_os-0.3.0b0/miv/io/asdf/__init__.py
+-rw-r--r--   0        0        0     1255 2023-03-11 00:36:16.967801 miv_os-0.3.0b0/miv/io/asdf/asdf.py
+-rw-r--r--   0        0        0      366 2023-02-17 02:50:18.810939 miv_os-0.3.0b0/miv/io/file/__init__.py
+-rw-r--r--   0        0        0    13907 2023-02-17 02:50:18.822068 miv_os-0.3.0b0/miv/io/file/read.py
+-rw-r--r--   0        0        0    18207 2023-02-17 02:51:04.365296 miv_os-0.3.0b0/miv/io/file/write.py
+-rw-r--r--   0        0        0       32 2023-02-17 02:51:06.069502 miv_os-0.3.0b0/miv/io/intan/__init__.py
+-rw-r--r--   0        0        0    10647 2023-03-10 23:55:11.501897 miv_os-0.3.0b0/miv/io/intan/data.py
+-rw-r--r--   0        0        0    41764 2023-02-22 20:49:17.911050 miv_os-0.3.0b0/miv/io/intan/rhs.py
+-rw-r--r--   0        0        0       74 2023-02-20 19:27:13.608834 miv_os-0.3.0b0/miv/io/openephys/__init__.py
+-rw-r--r--   0        0        0    13397 2023-02-22 09:41:26.965813 miv_os-0.3.0b0/miv/io/openephys/binary.py
+-rw-r--r--   0        0        0    26358 2023-03-06 16:40:02.926119 miv_os-0.3.0b0/miv/io/openephys/data.py
+-rw-r--r--   0        0        0      809 2023-02-17 02:51:19.193218 miv_os-0.3.0b0/miv/io/protocol.py
+-rw-r--r--   0        0        0       72 2023-02-17 02:50:15.108187 miv_os-0.3.0b0/miv/io/serial/__init__.py
+-rw-r--r--   0        0        0     3689 2023-02-17 02:51:05.267655 miv_os-0.3.0b0/miv/io/serial/arduino.py
+-rw-r--r--   0        0        0     2931 2023-02-17 02:51:05.287606 miv_os-0.3.0b0/miv/io/serial/stimjim.py
+-rw-r--r--   0        0        0      120 2023-02-20 19:27:13.611092 miv_os-0.3.0b0/miv/machinary/README.md
+-rw-r--r--   0        0        0     2424 2023-02-20 19:27:13.611267 miv_os-0.3.0b0/miv/machinary/convert_open_ephys_to_miv.py
+-rw-r--r--   0        0        0     2578 2023-03-02 21:17:42.423245 miv_os-0.3.0b0/miv/machinary/miv_extract_spiketrain.py
+-rw-r--r--   0        0        0     3983 2023-03-04 19:18:22.432586 miv_os-0.3.0b0/miv/mea/__init__.py
+-rw-r--r--   0        0        0     6930 2023-03-11 00:56:34.850636 miv_os-0.3.0b0/miv/mea/channel_mapping.py
+-rw-r--r--   0        0        0     1812 2023-02-17 02:51:05.231919 miv_os-0.3.0b0/miv/mea/grid.py
+-rw-r--r--   0        0        0      622 2023-02-17 02:49:59.807405 miv_os-0.3.0b0/miv/mea/protocol.py
+-rw-r--r--   0        0        0        0 2023-02-17 02:48:47.210081 miv_os-0.3.0b0/miv/py.typed
+-rw-r--r--   0        0        0        0 2023-02-17 02:46:54.913196 miv_os-0.3.0b0/miv/signal/__init__.py
+-rw-r--r--   0        0        0       41 2023-02-21 02:46:09.810799 miv_os-0.3.0b0/miv/signal/events/__init__.py
+-rw-r--r--   0        0        0     6473 2023-03-07 13:30:05.094683 miv_os-0.3.0b0/miv/signal/events/waveform.py
+-rw-r--r--   0        0        0      187 2023-02-25 05:44:59.740634 miv_os-0.3.0b0/miv/signal/filter/__init__.py
+-rw-r--r--   0        0        0     4195 2023-02-22 05:11:37.530437 miv_os-0.3.0b0/miv/signal/filter/butter_bandpass_filter.py
+-rw-r--r--   0        0        0     2372 2023-02-22 00:29:27.022325 miv_os-0.3.0b0/miv/signal/filter/median_filter.py
+-rw-r--r--   0        0        0     2287 2023-02-25 05:51:49.714072 miv_os-0.3.0b0/miv/signal/filter/notch_filter.py
+-rw-r--r--   0        0        0      638 2023-02-20 19:27:13.614284 miv_os-0.3.0b0/miv/signal/filter/protocol.py
+-rw-r--r--   0        0        0       52 2023-02-17 02:49:56.641590 miv_os-0.3.0b0/miv/signal/generator/__init__.py
+-rw-r--r--   0        0        0     1958 2023-02-17 02:49:59.611712 miv_os-0.3.0b0/miv/signal/generator/spike_generation.py
+-rw-r--r--   0        0        0      173 2023-02-17 02:51:25.478478 miv_os-0.3.0b0/miv/signal/similarity/__init__.py
+-rw-r--r--   0        0        0        0 2023-02-17 02:51:24.283504 miv_os-0.3.0b0/miv/signal/similarity/distance.py
+-rw-r--r--   0        0        0     2353 2023-02-17 02:51:24.298353 miv_os-0.3.0b0/miv/signal/similarity/dtw.py
+-rw-r--r--   0        0        0        0 2023-02-17 02:51:24.273574 miv_os-0.3.0b0/miv/signal/similarity/protocol.py
+-rw-r--r--   0        0        0     2726 2023-02-17 02:51:25.550561 miv_os-0.3.0b0/miv/signal/similarity/simple.py
+-rw-r--r--   0        0        0      120 2023-02-17 02:48:47.211402 miv_os-0.3.0b0/miv/signal/spike/__init__.py
+-rw-r--r--   0        0        0    10841 2023-03-12 14:51:25.125434 miv_os-0.3.0b0/miv/signal/spike/detection.py
+-rw-r--r--   0        0        0     1108 2023-02-17 02:48:47.212004 miv_os-0.3.0b0/miv/signal/spike/protocol.py
+-rw-r--r--   0        0        0    11915 2023-03-06 21:43:47.625733 miv_os-0.3.0b0/miv/signal/spike/sorting.py
+-rw-r--r--   0        0        0      315 2023-03-06 04:34:05.311150 miv_os-0.3.0b0/miv/statistics/__init__.py
+-rw-r--r--   0        0        0     2709 2023-02-17 02:50:06.691974 miv_os-0.3.0b0/miv/statistics/burst.py
+-rw-r--r--   0        0        0      108 2023-02-24 02:44:54.770327 miv_os-0.3.0b0/miv/statistics/connectivity/__init__.py
+-rw-r--r--   0        0        0     2563 2023-02-25 05:41:10.744303 miv_os-0.3.0b0/miv/statistics/connectivity/centrality.py
+-rw-r--r--   0        0        0    12313 2023-03-10 07:18:20.512357 miv_os-0.3.0b0/miv/statistics/connectivity/connectivity.py
+-rw-r--r--   0        0        0      157 2023-03-05 23:05:56.017548 miv_os-0.3.0b0/miv/statistics/connectivity/utils.py
+-rw-r--r--   0        0        0    17218 2023-03-12 15:22:14.044735 miv_os-0.3.0b0/miv/statistics/info_theory.py
+-rw-r--r--   0        0        0     1546 2023-02-17 02:50:01.180711 miv_os-0.3.0b0/miv/statistics/pairwise_causality.py
+-rw-r--r--   0        0        0     5820 2023-03-11 00:37:12.841595 miv_os-0.3.0b0/miv/statistics/peristimulus_analysis.py
+-rw-r--r--   0        0        0     2201 2023-03-03 15:34:43.907404 miv_os-0.3.0b0/miv/statistics/signal_statistics.py
+-rw-r--r--   0        0        0     8122 2023-03-07 13:31:44.493732 miv_os-0.3.0b0/miv/statistics/spiketrain_statistics.py
+-rw-r--r--   0        0        0      407 2023-02-20 19:27:13.615772 miv_os-0.3.0b0/miv/typing.py
+-rw-r--r--   0        0        0      211 2023-02-21 19:20:56.779632 miv_os-0.3.0b0/miv/visualization/__init__.py
+-rw-r--r--   0        0        0     4196 2023-03-03 16:32:29.123962 miv_os-0.3.0b0/miv/visualization/causality.py
+-rw-r--r--   0        0        0     5056 2023-02-17 02:50:09.430625 miv_os-0.3.0b0/miv/visualization/connectivity.py
+-rw-r--r--   0        0        0     1228 2023-02-17 02:49:28.749021 miv_os-0.3.0b0/miv/visualization/event.py
+-rw-r--r--   0        0        0     3196 2023-02-17 02:50:08.331531 miv_os-0.3.0b0/miv/visualization/fft_domain.py
+-rw-r--r--   0        0        0     3866 2023-02-17 02:49:59.864336 miv_os-0.3.0b0/miv/visualization/raw_signal.py
+-rw-r--r--   0        0        0     6090 2023-03-12 15:49:16.790908 miv_os-0.3.0b0/pyproject.toml
+-rw-r--r--   0        0        0     5231 1970-01-01 00:00:00.000000 miv_os-0.3.0b0/setup.py
+-rw-r--r--   0        0        0     5416 1970-01-01 00:00:00.000000 miv_os-0.3.0b0/PKG-INFO
```

### Comparing `miv_os-0.3.0.post2/LICENSE` & `miv_os-0.3.0b0/LICENSE`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/README.md` & `miv_os-0.3.0b0/README.md`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/decoding.py` & `miv_os-0.3.0b0/miv/coding/temporal/decoding.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/encoding.py` & `miv_os-0.3.0b0/miv/coding/temporal/encoding.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/lyon.py` & `miv_os-0.3.0b0/miv/coding/temporal/lyon.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/main.py` & `miv_os-0.3.0b0/miv/coding/temporal/main.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/protocol.py` & `miv_os-0.3.0b0/miv/coding/temporal/protocol.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/spiker.py` & `miv_os-0.3.0b0/miv/coding/temporal/spiker.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/coding/temporal/tbr.py` & `miv_os-0.3.0b0/miv/coding/temporal/tbr.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/core/datatype/events.py` & `miv_os-0.3.0b0/miv/core/datatype/events.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/core/datatype/protocol.py` & `miv_os-0.3.0b0/miv/core/datatype/protocol.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/core/datatype/signal.py` & `miv_os-0.3.0b0/miv/core/datatype/signal.py`

 * *Files 4% similar despite different names*

```diff
@@ -37,35 +37,33 @@
 
     def __post_init__(self):
         self.data = np.asarray(self.data)
         assert len(self.data.shape) == 2, "Signal must be 2D array"
 
     @property
     def number_of_channels(self) -> int:
-        """Number of channels in the signal."""
         return self.data.shape[self._CHANNELAXIS]
 
     def __getitem__(self, i: int) -> SignalType:
         return self.data[:, i]  # TODO: Fix to row-major
 
     def select(self, indices: Tuple[int, ...]) -> "Signal":
-        """Select channels by indices."""
+        """
+        Select channels by indices.
+        """
         return Signal(self.data[:, indices], self.timestamps, self.rate)
 
     def get_start_time(self):
-        """Get the start time of the signal."""
         return self.timestamps.min()
 
     def get_end_time(self):
-        """Get the end time of the signal."""
         return self.timestamps.max()
 
     @property
     def shape(self) -> Tuple[int, int]:
-        """Shape of the signal."""
         return self.data.shape
 
     def append(self, value) -> None:
         """Append a channels to the end of the existing signal."""
         assert value.shape[self._SIGNALAXIS] == self.data.shape[self._SIGNALAXIS]
         self.data = np.append(self.data, value, axis=self._CHANNELAXIS)
```

### Comparing `miv_os-0.3.0.post2/miv/core/datatype/spikestamps.py` & `miv_os-0.3.0b0/miv/core/datatype/spikestamps.py`

 * *Files 2% similar despite different names*

```diff
@@ -33,15 +33,14 @@
         super().__init__()
         if iterable is None:  # Default
             iterable = []
         self.data = iterable
 
     @property
     def number_of_channels(self) -> int:
-        """Number of channels"""
         return len(self.data)
 
     def __setitem__(self, index, item):
         self.data[index] = item
 
     def __getitem__(self, index):
         return self.data[index]
@@ -110,24 +109,17 @@
         return Spikestamps(
             [
                 np.array(sorted(list(filter(lambda x: t_start <= x <= t_end, arr))))
                 for arr in self.data
             ]
         )
 
-    def select(self, indices, keepdims: bool = True):
+    def select(self, indices):
         """Select channels by indices."""
-        if keepdims:
-            data = [
-                self.data[idx] if idx in indices else []
-                for idx in range(self.number_of_channels)
-            ]
-            return Spikestamps(data)
-        else:
-            return Spikestamps([self.data[idx] for idx in indices])
+        return Spikestamps([self.data[idx] for idx in indices])
 
     def neo(self):
         """Cast to neo.SpikeTrain"""
         import neo
 
         t_start = self.get_first_spikestamp()
         t_stop = self.get_last_spikestamp()
```

### Comparing `miv_os-0.3.0.post2/miv/core/operator/cachable.py` & `miv_os-0.3.0b0/miv/core/operator/cachable.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,37 +1,29 @@
 from __future__ import annotations
 
 __doc__ = """
 """
-__all__ = [
-    "_CacherProtocol",
-    "_Jsonable",
-    "_Cachable",
-    "DataclassCacher",
-    "FunctionalCacher",
-]
+__all__ = ["_Cachable", "DataclassCacher", "FunctionalCacher"]
 
 from typing import TYPE_CHECKING, Any, Generator, Literal, Protocol, Union
 
 import collections
 import dataclasses
 import functools
 import glob
 import itertools
 import json
 import os
 import pathlib
 import pickle as pkl
 
-import numpy as np
-
 if TYPE_CHECKING:
     from miv.core.datatype import DataTypes
 
-CACHE_POLICY = Literal["AUTO", "ON", "OFF", "MUST"]
+CACHE_POLICY = Literal["AUTO", "ON", "OFF"]
 
 
 class _CacherProtocol(Protocol):
     @property
     def cache_dir(self) -> str | pathlib.Path:
         ...
 
@@ -57,19 +49,14 @@
         ...
 
     def check_cached(self) -> bool:
         """Check if the current configuration is the same as the cached one."""
         ...
 
 
-class _Jsonable(Protocol):
-    def to_json(self) -> dict[str, Any]:
-        ...
-
-
 class _Cachable(Protocol):
     @property
     def analysis_path(self) -> str | pathlib.Path:
         ...
 
     @property
     def cacher(self) -> _CacherProtocol:
@@ -116,70 +103,78 @@
 
     def save_cache(self, values, idx):
         raise NotImplementedError(
             "If you are using SkipCache, you should not be calling this method."
         )
 
 
-def when_policy_is(*allowed_policy):
+def when_policy_is(*policy):
     def decorator(func):
-        # @functools.wraps(func) # TODO: fix this
-        def wrapper(self, *args, **kwargs):
-            if self.policy in allowed_policy:
-                return func(self, *args, **kwargs)
+        @functools.wraps(func)
+        def wrapper(*args, **kwargs):
+            self = args[0]
+            if self.policy in policy:
+                return func(*args, **kwargs)
             else:
                 return False
 
         return wrapper
 
     return decorator
 
 
 def when_initialized(func):  # TODO: refactor
-    # @functools.wraps(func) # TODO: fix this
-    def wrapper(self, *args, **kwargs):
+    @functools.wraps(func)
+    def wrapper(*args, **kwargs):
+        self = args[0]
         if self.cache_dir is None:
             return False
         else:
-            return func(self, *args, **kwargs)
+            return func(*args, **kwargs)
 
     return wrapper
 
 
 class BaseCacher:
     def __init__(self, parent):
         super().__init__()
-        self.policy: CACHE_POLICY = "AUTO"  # TODO: make this a property
+        self.cache_policy: CACHE_POLICY = "AUTO"  # TODO: make this a property
         self.parent = parent
         self.cache_dir = None  # TODO: Public. Make proper setter
         self.cache_tag = "data"
 
     @property
+    def policy(self) -> CACHE_POLICY:
+        return self.cache_policy
+
+    @policy.setter
+    def policy(self, v) -> CACHE_POLICY:
+        self.cache_policy = v
+
+    @property
     def config_filename(self) -> str:
         return os.path.join(self.cache_dir, "config.json")
 
     def cache_filename(self, idx) -> str:
         index = idx if isinstance(idx, str) else f"{idx:04}"
         return os.path.join(self.cache_dir, f"cache_{self.cache_tag}_{index}.pkl")
 
-    @when_policy_is("ON", "AUTO", "MUST")
+    @when_policy_is("ON", "AUTO")
     @when_initialized
     def save_cache(self, values, idx=0) -> bool:
         os.makedirs(self.cache_dir, exist_ok=True)
         with open(self.cache_filename(idx), "wb") as f:
             pkl.dump(values, f)
         return True
 
 
 class DataclassCacher(BaseCacher):
-    @when_policy_is("ON", "AUTO", "MUST")
+    @when_policy_is("ON", "AUTO")
     @when_initialized
     def check_cached(self) -> bool:
-        if self.policy == "MUST":
-            return True
         current_config = self._compile_configuration_as_dict()
         cached_config = self._load_configuration_from_cache()
         if cached_config is None:
             flag = False
         else:
             flag = current_config == cached_config  # TODO: fix this
         return flag
@@ -187,54 +182,41 @@
     def _load_configuration_from_cache(self) -> dict:
         if os.path.exists(self.config_filename):
             with open(self.config_filename) as f:
                 return json.load(f)
         return None
 
     def _compile_configuration_as_dict(self) -> dict:
-        config = dataclasses.asdict(self.parent, dict_factory=collections.OrderedDict)
-        for key in config.keys():
-            if isinstance(config[key], np.ndarray):
-                config[key] = config[key].tostring()
-            elif hasattr(config[key], "to_json"):
-                config[key] = config[key].to_json()
-        return config
+        return dataclasses.asdict(self.parent, dict_factory=collections.OrderedDict)
 
-    @when_policy_is("ON", "AUTO", "MUST")
+    @when_policy_is("ON", "AUTO")
     @when_initialized
     def save_config(self):
         config = self._compile_configuration_as_dict()
         os.makedirs(self.cache_dir, exist_ok=True)
-        try:
-            with open(self.config_filename, "w") as f:
-                json.dump(config, f, indent=4)
-        except (TypeError, OverflowError):
-            raise TypeError(
-                "Some property of caching objects are not JSON serializable."
-            )
+        with open(self.config_filename, "w") as f:
+            json.dump(config, f, indent=4)
         return True
 
     @when_initialized
     def load_cached(self) -> Generator[DataTypes, None, None]:
         paths = glob.glob(self.cache_filename("*"))
         for path in paths:
             with open(path, "rb") as f:
                 yield pkl.load(f)
 
 
 class FunctionalCacher(BaseCacher):
-    @when_policy_is("ON", "AUTO", "MUST")
+    @when_policy_is("ON", "AUTO")
     @when_initialized
     def check_cached(self) -> bool:
-        if self.policy == "MUST":  # TODO: fix this, remove redundancy
-            return True
         flag = os.path.exists(self.cache_filename(0))
         return flag
 
-    @when_policy_is("ON", "AUTO", "MUST")
+    @when_policy_is("ON", "AUTO")
     @when_initialized
     def save_config(self):
         pass
 
     @when_initialized
     def load_cached(self) -> Generator[DataTypes, None, None]:
         path = glob.glob(self.cache_filename(0))[0]
```

### Comparing `miv_os-0.3.0.post2/miv/core/operator/callback.py` & `miv_os-0.3.0b0/miv/core/operator/callback.py`

 * *Files 9% similar despite different names*

```diff
@@ -62,15 +62,14 @@
 
 class BaseCallbackMixin:
     def __init__(self):
         super().__init__()
         self._callback_before_run = []
         self._callback_after_run = []
         self._callback_plot = []
-        self.skip_plotting: bool = False
 
     def __lshift__(self, right: Callable) -> SelfCallback:
         if right.__name__.startswith(
             "__prepend"
         ):  # TODO: need better way to prepend callbacks
             self._callback_before_run.append(right)
             return self
@@ -102,16 +101,14 @@
 
     def plot(
         self,
         show: bool = False,
         save_path: Optional[Union[bool, str, pathlib.Path]] = None,
         dry_run: bool = False,
     ):
-        if self.skip_plotting:
-            return
         if save_path is True:
             os.makedirs(self.analysis_path, exist_ok=True)
             save_path = self.analysis_path
         plotters = get_methods_from_feature_classes_by_startswith_str(self, "plot")
         if dry_run:
             for plotter in plotters:
                 print(f"dry run: {plotter}")
```

### Comparing `miv_os-0.3.0.post2/miv/core/operator/chainable.py` & `miv_os-0.3.0b0/miv/core/operator/chainable.py`

 * *Files 12% similar despite different names*

```diff
@@ -58,20 +58,18 @@
         """Print summary of downstream network structures."""
         ...
 
 
 class BaseChainingMixin:
     """
     Base mixin to create chaining structure between objects.
-
-    Need further implementation of: output, tag
     """
 
-    def __init__(self, *args, **kwargs):
-        super().__init__(*args, **kwargs)
+    def __init__(self):
+        super().__init__()
         self._downstream_list: list[_Chainable] = []
         self._upstream_list: list[_Chainable] = []
 
         self._output: DataTypes | None = None
 
     def __rshift__(self, right: _Chainable) -> _Chainable:
         self._downstream_list.append(right)
@@ -169,33 +167,29 @@
         """
         Topological sort of the graph.
         Raise RuntimeError if there is a loop in the graph.
         """
         # TODO: Make it free function
         upstream = self._get_upstream_topology()
 
-        # pos = dict()  # FIXME: Operators are not hashable
-        key = []
-        pos = []
+        pos = dict()
         ind = 0
         tsort = []
 
         while len(upstream) > 0:
-            key.append(upstream[-1])
-            pos.append(ind)
-            # pos[upstream[-1]] = ind
+            pos[upstream[-1]] = ind
             tsort.append(upstream[-1])
             ind += 1
             upstream.pop()
         for source in tsort:
             for up in source.iterate_upstream():
-                if up not in key:
+                if up not in pos:
                     continue
-                before = pos[key.index(source)]
-                after = pos[key.index(up)]
+                before = pos[source]
+                after = pos[up]
 
                 # If parent vertex does not appear first
                 if before > after:
                     raise RuntimeError(
                         f"Found loop in operation stream: node {source} is already in the upstream : {up}."
                     )
```

### Comparing `miv_os-0.3.0.post2/miv/core/operator/operator.py` & `miv_os-0.3.0b0/miv/core/operator/operator.py`

 * *Files 6% similar despite different names*

```diff
@@ -111,32 +111,33 @@
         - Cache includes:
             - All results from callback
     """
 
     def __init__(self):
         super().__init__()
         self._output: DataTypes | None = None
+        assert self.tag != ""
+        self.analysis_path = os.path.join(
+            "results", self.tag.replace(" ", "_")
+        )  # Default analysis path
+
         self.runner = VanillaRunner()
         self.cacher = DataclassCacher(self)
 
-        assert self.tag != ""
-        self.set_save_path("results")  # Default analysis path
-
     def set_caching_policy(self, cacher: _CacherProtocol):
         self.cacher = cacher(self)
 
-    def set_save_path(self, path: str | pathlib.Path):
-        self.analysis_path = os.path.join(path, self.tag.replace(" ", "_"))
-        self.cacher.cache_dir = os.path.join(self.analysis_path, ".cache")
-
     def receive(self) -> list[DataTypes]:
         return [node.output for node in self.iterate_upstream()]
 
     @property
     def output(self) -> list[DataTypes]:
+        # FIXME: Run graph upstream? what about the order??
+        if self._output is None:
+            raise RuntimeError(f"{self} is not yet executed.")
         self._execute()
         return self._output  # TODO: Just use upstream caller instead of .output
 
     def _execute(self):
         args: list[DataTypes] = self.receive()  # Receive data from upstream
         # TODO : implement pre-run callback
         # args = self.callback_before_run(args)
@@ -145,21 +146,20 @@
         else:
             output = self.runner(self.__call__, args)
         # Post Processing
         self._output = self.callback_after_run(output)
 
     def run(
         self,
-        save_path: str | pathlib.Path | None = None,
+        save_path: str | pathlib.Path,
         dry_run: bool = False,
-        skip_plot: bool = False,
+        cache_dir: str | pathlib.Path = ".cache",
     ) -> None:
         # Execute the module
-        if save_path is not None:
-            self.set_save_path(save_path)
+        self.analysis_path = os.path.join(save_path, self.tag.replace(" ", "_"))
+        self.cacher.cache_dir = os.path.join(self.analysis_path, cache_dir)
 
         if dry_run:
             print("Dry run: ", self.__class__.__name__)
             return
         self._execute()
-        if not skip_plot:
-            self.plot(show=False, save_path=True, dry_run=dry_run)
+        self.plot(show=False, save_path=True, dry_run=dry_run)
```

### Comparing `miv_os-0.3.0.post2/miv/core/pipeline.py` & `miv_os-0.3.0b0/miv/core/pipeline.py`

 * *Files 4% similar despite different names*

```diff
@@ -35,15 +35,14 @@
     def __init__(self, node: _Chainable):
         self.execution_order: List[_Runnable] = node.topological_sort()
 
     def run(
         self,
         working_directory: Optional[Union[str, pathlib.Path]] = "./results",
         no_cache: bool = False,
-        skip_plot: bool = False,
         dry_run: bool = False,
         verbose: bool = False,  # Use logging
     ):
         """
         Run the pipeline.
 
         Parameters
@@ -58,23 +57,19 @@
             If True, the pipeline will log debugging informations. By default False
         """
         for node in self.execution_order:
             if verbose:
                 print("Running: ", node)
             if hasattr(node, "cacher"):
                 node.cacher.cache_policy = "OFF" if no_cache else "AUTO"
-            node.run(dry_run=dry_run, save_path=working_directory, skip_plot=skip_plot)
+            node.run(dry_run=dry_run, save_path=working_directory)
         if verbose:
             print("Pipeline done:")
             self.summarize()
             print("-" * 46)
 
     def summarize(self):
         strs = []
         strs.append("Execution order:")
         for i, op in enumerate(self.execution_order):
             strs.append(f"{i}: {op}")
         return "\n".join(strs)
-
-    def export(self, working_directory: Optional[Union[str, pathlib.Path]]):
-        # TODO
-        pass
```

### Comparing `miv_os-0.3.0.post2/miv/core/policy.py` & `miv_os-0.3.0b0/miv/core/policy.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,15 +1,14 @@
 __all__ = [
     "_Runnable",
     "_RunnerProtocol",
     "VanillaRunner",
     "SupportMultiprocessing",
     "MultiprocessingRunner",
     "InternallyMultiprocessing",
-    "StrictMPIRunner",
 ]
 
 from typing import Any, Callable, Generator, Optional, Protocol, Union
 
 import multiprocessing
 import pathlib
 from dataclasses import dataclass
@@ -66,48 +65,19 @@
                 "Multiprocessing for operator with no generator input is not supported yet. Please use VanillaRunner for this operator."
             )
         else:
             with multiprocessing.Pool(self.num_proc) as p:
                 yield from p.imap(func, inputs)
 
 
-class StrictMPIRunner:
-    def __init__(self):
-        from mpi4py import MPI
-
-        self.comm = MPI.COMM_WORLD
-        self.root = 0
-
-    def set_comm(self, comm):
-        self.comm = comm
-
-    def set_root(self, root: int):
-        self.root = root
-
-    def get_rank(self):
-        return self.comm.Get_rank()
-
-    def get_size(self):
-        return self.comm.Get_size()
-
-    def get_root(self):
-        return self.root
-
-    def is_root(self):
-        return self.get_rank() == self.root
-
-    def __call__(self, func, inputs=None, **kwargs):
-        if inputs is None:
-            output = func()
-        else:
-            output = func(*inputs)
-        return output
+class StrictMPI:
+    pass
 
 
-class SupportMPI(StrictMPIRunner):
+class SupportMPI(StrictMPI):
     pass
 
 
 class SupportMultiprocessing:
     pass
```

### Comparing `miv_os-0.3.0.post2/miv/core/spikestamps.py` & `miv_os-0.3.0b0/miv/core/spikestamps.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/core/wrapper.py` & `miv_os-0.3.0b0/miv/core/wrapper.py`

 * *Files 6% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 
 def wrap_cacher(cache_tag):
     """
     Decorator to wrap the function to use cacher.
     """
 
     def decorator(func):
-        # @functools.wraps(func)
+        @functools.wraps(func)
         def wrapper(*args, **kwargs):
             if not hasattr(wrapper, "cache_tag"):
                 setattr(wrapper, "cache_tag", cache_tag)
             self: Operator = args[0]
             self.cacher.cache_tag = wrapper.cache_tag
             if self.cacher.check_cached():
                 return next(self.cacher.load_cached())
@@ -54,41 +54,39 @@
     """
     If all input arguments are generator, then the output will be a generator.
 
     TODO: Fix to accomodate free functions
     Current implementation only works for class methods.
     """
 
-    # @functools.wraps(func)
-    def wrapper(self, *args, **kwargs):
+    @functools.wraps(func)
+    def wrapper(*args, **kwargs):
+        self: Operator = args[0]
         is_all_generator = all(inspect.isgenerator(v) for v in args[1:]) and all(
             inspect.isgenerator(v) for v in kwargs.values()
         )
         if is_all_generator:
-            if self.cacher.check_cached():
 
-                def generator_func(*args, **kwargs):
+            def generator_func(*args, **kwargs):
+                if self.cacher.check_cached():
                     yield from self.cacher.load_cached()
-
-            else:
-
-                def generator_func(*args, **kwargs):
+                else:
                     for idx, zip_arg in enumerate(zip(*args)):
                         result = func(self, *zip_arg, **kwargs)
                         self.cacher.save_cache(result, idx)
                         yield result
                     else:
                         self.cacher.save_config()
 
-            return generator_func(*args, **kwargs)
+            return generator_func(*(args[1:]), **kwargs)
         else:
             if self.cacher.check_cached():
                 return next(self.cacher.load_cached())
             else:
-                result = func(self, *args, **kwargs)
+                result = func(*args, **kwargs)
                 self.cacher.save_cache(result)
                 self.cacher.save_config()
             return result
 
     return wrapper
 
 
@@ -104,14 +102,15 @@
         )
 
         @dataclass
         class LambdaClass(_LambdaClass, OperatorMixin):
             tag: str = name
 
             def __call__(self, *args, **kwargs):
+                print(type(args[0]))
                 return func(self, *args)
 
             def __post_init__(self):
                 _LambdaClass.__init__(self, **params)
                 OperatorMixin.__init__(self)
 
         LambdaClass.__name__ = name
```

### Comparing `miv_os-0.3.0.post2/miv/datasets/criticality.py` & `miv_os-0.3.0b0/miv/datasets/criticality.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/datasets/openephys_sample.py` & `miv_os-0.3.0b0/miv/datasets/openephys_sample.py`

 * *Files 8% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 def load_data(progbar_disable: bool = False):  # pragma: no cover
     """
     Loads the sample recorded data from OpenEphys aquisition system. `Direct Download <https://uofi.box.com/shared/static/daagmwebzfdl1jjgfhjzzhof2if44m04.zip>`_
 
     Total size: 21.2 kB (compressed)
 
-    File hash: ab1b282a2560e75263188dc2bab56b019bb83ea12aa63692c9560c6e8281de29
+    File hash: 3b687d1dfb2f4538a75e7d57d360f76acea6b62ebc178c435fb3ed7999bf65ce
 
     Examples
     --------
         >>> from miv.datasets.ttl_events import load_data
         >>> experiments: miv.io.DataManager = load_data()
         datasets/ttl_recording/sample_event_recording
             0: <miv.io.data.Data object at 0x7fec71c99fa0>
@@ -49,15 +49,15 @@
         >>> experiments: miv.io.DataManager = datasets.openephys_sample.load_data()
 
     """
 
     subdir = "OpenEphys"
     base_url = "https://uofi.box.com/shared/static/daagmwebzfdl1jjgfhjzzhof2if44m04.zip"
     file = "OpenEphys_Sample_64MEA.zip"
-    file_hash = "ab1b282a2560e75263188dc2bab56b019bb83ea12aa63692c9560c6e8281de29"
+    file_hash = "3b687d1dfb2f4538a75e7d57d360f76acea6b62ebc178c435fb3ed7999bf65ce"
 
     path = get_file(
         file_url=base_url,
         directory=subdir,
         fname=file,
         file_hash=file_hash,
         archive_format="zip",
```

### Comparing `miv_os-0.3.0.post2/miv/datasets/optogenetic.py` & `miv_os-0.3.0b0/miv/datasets/optogenetic.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/datasets/ttl_events.py` & `miv_os-0.3.0b0/miv/datasets/ttl_events.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/datasets/utils.py` & `miv_os-0.3.0b0/miv/datasets/utils.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/asdf/asdf.py` & `miv_os-0.3.0b0/miv/io/asdf/asdf.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,16 +1,12 @@
 __doc__ = """
 ASDF file type loader
 
-author: tvarley
-        djhavert
-
-.. autoclass:: miv.io.asdf.asdf.DataASDF
-   :members:
-
+@author: tvarley
+         djhavert
 """
 __all__ = ["DataASDF"]
 
 import os
 import sys
 
 import numpy as np
@@ -18,23 +14,15 @@
 from scipy.io import loadmat
 
 from miv.core.datatype import Spikestamps
 from miv.core.operator import DataLoaderMixin
 
 
 class DataASDF(DataLoaderMixin):
-    """ASDF file type loader"""
-
     def __init__(self, data_path, rate: float):  # pragma: no cover
-        """
-        Constructor
-
-        :param data_path: path to data file
-        :param rate: sampling rate
-        """
         self.data_path = data_path
         self.rate = rate
 
     def load(self):  # pragma: no cover
         """
         Load data from ASDF file
         """
```

### Comparing `miv_os-0.3.0.post2/miv/io/file/read.py` & `miv_os-0.3.0b0/miv/io/file/read.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/file/write.py` & `miv_os-0.3.0b0/miv/io/file/write.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/intan/data.py` & `miv_os-0.3.0b0/miv/io/intan/data.py`

 * *Files 12% similar despite different names*

```diff
@@ -101,49 +101,27 @@
     def _generator_by_channel_name(self, name: str, progress_bar: bool = False):
         if not self.check_path_validity():
             raise FileNotFoundError("Data directory does not have all necessary files.")
         files = self.get_recording_files()
         # Get sampling rate from setting file
         setting_path = os.path.join(self.data_path, "settings.xml")
         sampling_rate = int(ET.parse(setting_path).getroot().attrib["SampleRateHertz"])
-        active_channels, total = self._get_active_channels()
         # Read each files
         for filename in tqdm(files, disable=not progress_bar):
             result, data_present = rhs.load_file(filename)
             assert data_present, f"Data does not present: {filename=}."
             assert not hasattr(result, name), f"No {name} in the file ({filename=})."
 
-            signal = np.asarray(result[name])
-            if total != signal.shape[0]:
-                _signal = np.zeros([total, signal.shape[1]], dtype=signal.dtype)
-                _signal[active_channels, :] = signal
-                signal = _signal
-
+            # signal_group = result["amplifier_channels"]
             yield Signal(
-                data=signal.T,
+                data=np.asarray(result[name]).T,
                 timestamps=np.asarray(result["t"]),
                 rate=sampling_rate,
             )
 
-    def _get_active_channels(self, group_prefix=("A", "B", "C", "D")):
-        setting_path = os.path.join(self.data_path, "settings.xml")
-        root = ET.parse(setting_path).getroot()
-        total = 0
-        active_channels = []
-        for child in root:
-            if child.tag != "SignalGroup":
-                continue
-            if child.attrib["Prefix"] not in group_prefix:
-                continue
-            for channel in child:
-                if channel.attrib["Enabled"] == "True":
-                    active_channels.append(total)
-                total += 1
-        return np.array(active_channels), total
-
     def check_path_validity(self):
         """
         Check if necessary files exist in the directory.
 
         - Check `rhs` file exists.
         - Check `settings.xml` file exists.
 
@@ -163,35 +141,14 @@
         return True
 
     def get_recording_files(self):
         paths = glob(os.path.join(self.data_path, "*.rhs"), recursive=True)
         paths.sort()
         return paths
 
-    def get_stimulation_events(self):  # TODO: refactor
-        minimum_stimulation_length = 0.010
-        data = self.get_stimulation()
-        stim = data.data
-        timestamps = data.timestamps
-        # sampling_rate = data.rate
-        stimulated_channels = np.where(np.abs(stim).sum(axis=0))[0]
-        if len(stimulated_channels) == 0:
-            return None
-        stimulated_channel = stimulated_channels[0]
-        stim = stim[:, stimulated_channel]
-
-        events = ~np.isclose(stim, 0)
-        eventstrain = timestamps[np.where(events)[0]]
-        ref = np.concatenate(
-            [[True], np.diff(eventstrain) > minimum_stimulation_length]
-        )
-        eventstrain = eventstrain[ref]
-        ret = Spikestamps([eventstrain])  # TODO: use datatype.Events
-        return ret
-
     # Disable
     def load_ttl_event(self):
         raise AttributeError("DataIntan does not have laod_ttl_event method")
 
 
 class DataIntanTriggered(DataIntan):
     """
@@ -202,57 +159,43 @@
     def __init__(
         self,
         data_path,  # FIXME: argument order with intan.DATA
         index: int = 0,
         trigger_key: str = "board_adc_data",
         trigger_index: int = 0,
         trigger_threshold_voltage=1.0,
-        progress_bar: bool = False,
         *args,
         **kwargs,
     ):
         super().__init__(data_path=data_path, *args, **kwargs)
         self.index = index
         self.trigger_key = trigger_key
         self.trigger_index = trigger_index
         self.trigger_threshold_voltage = trigger_threshold_voltage
-        self.progress_bar = progress_bar
-
-    def __len__(self):
-        groups = self._trigger_grouping()
-        return len(groups)
 
     def __getitem__(self, index):
-        groups = self._trigger_grouping()
-        if len(groups) <= index:
-            raise IndexError(
-                f"Index exceeds the number of triggered recordings ({len(groups)})."
-            )
         return DataIntanTriggered(
             data_path=self.data_path,
             index=index,
             trigger_key=self.trigger_key,
             trigger_index=self.trigger_index,
             trigger_threshold_voltage=self.trigger_threshold_voltage,
-            progress_bar=self.progress_bar,
         )
 
     @wrap_cacher(cache_tag="trigger_grouping")
-    def _trigger_grouping(self):
+    def _trigger_grouping(self, paths):
         def _find_sequence(arr):
             if arr.size == 0:
                 return arr
             return arr[np.concatenate([np.array([True]), arr[1:] - 1 != arr[:-1]])]
 
-        paths = DataIntan.get_recording_files(self)
-
         group_files = []
         group = {"paths": [], "start index": [], "end index": []}
         status = 0
-        for file in tqdm(paths, disable=not self.progress_bar):
+        for file in paths:
             result, _ = rhs.load_file(file)
             time = result["t"]
             adc_data = result[self.trigger_key][self.trigger_index]
             diff_adc_data = adc_data[1:] - adc_data[:-1]
             # TODO: Something can be done better
             recording_on = _find_sequence(
                 np.where(diff_adc_data > self.trigger_threshold_voltage)[0]
@@ -290,40 +233,56 @@
                     raise ValueError(
                         f"Something went wrong with the trigger signal. {len(recording_on)=} {len(recording_off)=}"
                     )
 
         return group_files
 
     def get_recording_files(self):
-        groups = self._trigger_grouping()
+        paths = DataIntan.get_recording_files(self)
+        groups = self._trigger_grouping(paths)
         return groups[self.index]["paths"]
 
     def _generator_by_channel_name(self, name: str, progress_bar: bool = False):
         if not self.check_path_validity():
             raise FileNotFoundError("Data directory does not have all necessary files.")
-        groups = self._trigger_grouping()
+        groups = self._trigger_grouping(None)  # Should be cached
         files = groups[self.index]["paths"]
         sindex = groups[self.index]["start index"]
         eindex = groups[self.index]["end index"]
         # Get sampling rate from setting file
         setting_path = os.path.join(self.data_path, "settings.xml")
         sampling_rate = int(ET.parse(setting_path).getroot().attrib["SampleRateHertz"])
-        active_channels, total = self._get_active_channels()
         # Read each files
         for filename, sidx, eidx in tqdm(
             zip(files, sindex, eindex), disable=not progress_bar
         ):
             result, data_present = rhs.load_file(filename)
             assert data_present, f"Data does not present: {filename=}."
             assert not hasattr(result, name), f"No {name} in the file ({filename=})."
 
-            signal = np.asarray(result[name])
-            if total != signal.shape[0]:
-                _signal = np.zeros([total, signal.shape[1]], dtype=signal.dtype)
-                _signal[active_channels, :] = signal
-                signal = _signal
-
+            # signal_group = result["amplifier_channels"]
             yield Signal(
-                data=signal.T[sidx:eidx, :],
+                data=np.asarray(result[name]).T[sidx:eidx, :],
                 timestamps=np.asarray(result["t"])[sidx:eidx],
                 rate=sampling_rate,
             )
+
+    def get_stimulation_events(self):  # TODO: refactor
+        minimum_stimulation_length = 0.010
+        data = self.get_stimulation()
+        stim = data.data
+        timestamps = data.timestamps
+        # sampling_rate = data.rate
+        stimulated_channels = np.where(np.abs(stim).sum(axis=0))[0]
+        if len(stimulated_channels) == 0:
+            return None
+        stimulated_channel = stimulated_channels[0]
+        stim = stim[:, stimulated_channel]
+
+        events = ~np.isclose(stim, 0)
+        eventstrain = timestamps[np.where(events)[0]]
+        ref = np.concatenate(
+            [[True], np.diff(eventstrain) > minimum_stimulation_length]
+        )
+        eventstrain = eventstrain[ref]
+        ret = Spikestamps([eventstrain])  # TODO: use datatype.Events
+        return ret
```

### Comparing `miv_os-0.3.0.post2/miv/io/intan/rhs.py` & `miv_os-0.3.0b0/miv/io/intan/rhs.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/openephys/binary.py` & `miv_os-0.3.0b0/miv/io/openephys/binary.py`

 * *Files 2% similar despite different names*

```diff
@@ -283,22 +283,16 @@
     # load structure information dictionary
     info_file: str = os.path.join(folder, "structure.oebin")
     info: Dict[str, Any] = oebin_read(info_file)
     num_channels: int = info["continuous"][0]["num_channels"]
     sampling_rate: float = float(info["continuous"][0]["sample_rate"])
     # channel_info: Dict[str, Any] = info["continuous"][0]["channels"]
 
-    _old_oe_version = False
-    if "GUI version" in info:
-        version = info["GUI version"]
-        v_major, v_minor, v_sub = list(map(int, version.split(".")))[:3]
-        _old_oe_version = v_major == 0 and v_minor <= 5  # Legacy
-    signal, timestamps = load_continuous_data(
-        file_path[0], num_channels, sampling_rate, _old_oe_version=_old_oe_version
-    )
+    # TODO: maybe need to support multiple continuous.dat files in the future
+    signal, timestamps = load_continuous_data(file_path[0], num_channels, sampling_rate)
     if num_fragments is None:
         num_fragments = int(max(timestamps.shape[0] // sampling_rate // (60 + 1), 1))
     fragmented_signal = np.array_split(signal, num_fragments, axis=0)[
         start_index:end_index
     ]
     fragmented_timestamps = np.array_split(timestamps, num_fragments)[
         start_index:end_index
@@ -329,15 +323,14 @@
 
 def load_continuous_data(
     data_path: str,
     num_channels: int,
     sampling_rate: float,
     timestamps_path: Optional[str] = None,
     _recorded_dtype: Union[np.dtype, str] = "int16",
-    _old_oe_version: bool = False,
 ):
     """
     Load single continous data file and return timestamps and raw data in numpy array.
     Typical `data_path` from OpenEphys has a name `continuous.dat`.
 
     .. note::
         The output data is raw-data without unit conversion. In order to convert the unit
@@ -388,13 +381,12 @@
         timestamps_path = os.path.join(dirname, "timestamps.npy")
 
     # Get timestamps
     if os.path.exists(timestamps_path):
         timestamps = np.asarray(
             np.load(timestamps_path)
         )  # TODO: check if npy file includes dtype. else, add "dtype=np.float32"
-        if _old_oe_version:
-            timestamps = timestamps / float(sampling_rate)
+        # timestamps /= float(sampling_rate)  # TODO(beyond 0.3.0) As of OpenEphys 0.6, this line is no-longer necessary.
     else:  # If timestamps_path doesn't exist, deduce the stamps
         timestamps = np.array(range(0, length)) / sampling_rate
 
     return raw_data, timestamps
```

### Comparing `miv_os-0.3.0.post2/miv/io/openephys/data.py` & `miv_os-0.3.0b0/miv/io/openephys/data.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/protocol.py` & `miv_os-0.3.0b0/miv/io/protocol.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/serial/arduino.py` & `miv_os-0.3.0b0/miv/io/serial/arduino.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/io/serial/stimjim.py` & `miv_os-0.3.0b0/miv/io/serial/stimjim.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/machinary/convert_open_ephys_to_miv.py` & `miv_os-0.3.0b0/miv/machinary/convert_open_ephys_to_miv.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/machinary/miv_extract_spiketrain.py` & `miv_os-0.3.0b0/miv/machinary/miv_extract_spiketrain.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/mea/__init__.py` & `miv_os-0.3.0b0/miv/mea/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,12 +1,10 @@
 import numpy as np
 
 from miv.mea.grid import *
-from miv.mea.protocol import *
-from miv.mea.unstructured import *
 
 mea_map = {
     "64_upper_half_intanRHD_stim": np.array(
         [
             [-1, 2, 4, 6, 23, 20, 18],
             [10, 9, 3, 5, 24, 19, -1],
             [12, 11, 1, 7, 22, -1, -1],
```

### Comparing `miv_os-0.3.0.post2/miv/mea/base.py` & `miv_os-0.3.0b0/miv/mea/grid.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,50 +1,62 @@
-__doc__ = """ Base mixin for MEA classes. """
+__all__ = ["GridMEA"]
 
 from typing import Tuple
 
-import matplotlib.gridspec as gridspec
-import matplotlib.pyplot as plt
+import matplotlib
 import numpy as np
-import pandas as pd
 
-from miv.core.operator import BaseChainingMixin
+from miv.mea.protocol import MEAGeometryProtocol
 
 
-class MEAMixin(BaseChainingMixin):
-    """Base mixin for MEA classes.
-
-    Functional module.
-
-    Comply with the following interface:
-        MEAGeometryProtocol
+class GridMEA:
     """
+    A class representing a grid-based multi-electrode array (MEA).
 
-    def __init__(self, tag: str = "mea", *args, **kwargs):
-        super().__init__(*args, **kwargs)
-        self.tag = tag
-        self.runner = None
+    Example
+    -------
+    For example, you could create an instance of the GridMEA class like this:
+    literal blocks::
+
+        nrow = 10
+        ncol = 20
+        xid = np.arange(nrow * ncol) % ncol
+        yid = np.arange(nrow * ncol) // ncol
+        mea = GridMEA(nrow, ncol, xid, yid)
+
+    Attributes
+    ----------
+    nrow: int
+        The number of rows in the grid.
+    ncol: int
+        The number of columns in the grid.
+    xid: np.ndarray
+        A NumPy array containing the x-coordinates of the electrodes in the grid.
+    yid: np.ndarray
+        A NumPy array containing the y-coordinates of the electrodes in the grid.
+    """
 
-    def get_xy(self, idx: int) -> Tuple[float, float]:
-        """Given node index, return xy coordinate"""
-        raise NotImplementedError
+    def __init__(self, nrow: int, ncol: int, xid: np.ndarray, yid: np.ndarray):
+        self.nrow = nrow
+        self.ncol = ncol
+        self.xid = xid
+        self.yid = yid
 
-    def save(self, path: str) -> None:
+    def get_closest_node(self, x: float, y: float) -> int:  # pragma: no cover
+        """Given xy coordinate, return closest node idx"""
         raise NotImplementedError
 
-    def load(self, path: str) -> None:
+    def get_xy(self, idx: int) -> Tuple[float, float]:  # pragma: no cover
+        """Given node index, return xy coordinate"""
         raise NotImplementedError
 
-    def view(self) -> plt.Figure:
+    def view(self) -> matplotlib.pyplot.Figure:  # pragma: no cover
         """Simplified view of MEA orientation"""
         raise NotImplementedError
 
-    @property
-    def output(self):
-        return self
-
-    def run(self, **kwargs):
-        pass
+    def save(self, path: str) -> None:  # pragma: no cover
+        """Export MEA information"""
+        raise NotImplementedError
 
-    def map_data(self, vector: np.ndarray) -> np.ndarray:
-        """Map data (1-D array) to MEA (2-D array or N-D array)"""
+    def load(self, path: str) -> None:  # pragma: no cover
+        """Import MEA from external source"""
         raise NotImplementedError
```

### Comparing `miv_os-0.3.0.post2/miv/mea/channel_mapping.py` & `miv_os-0.3.0b0/miv/mea/channel_mapping.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,18 +31,14 @@
         rhs_32_4 = rhs_32.copy()
         rhs_32_4[rhs_32_4 != -1] += 32 * 0
         self.intan_map = np.concatenate(
             [rhs_32_1, rhs_32_2, rhs_32_3, rhs_32_4], axis=0
         )
 
         self.mea = mea_map[map_key]
-        self.mea_intan = np.zeros_like(self.mea, dtype=np.int_) - 1
-        for channel in range(128):
-            oe_channel = self.channel_mapping(channel, reverse=True)
-            self.mea_intan[self.mea == oe_channel] = channel
 
     def channel_mapping(self, channel, reverse=False):
         """
 
         Parameters
         ----------
         channel : int or str
```

### Comparing `miv_os-0.3.0.post2/miv/signal/events/waveform.py` & `miv_os-0.3.0b0/miv/signal/events/waveform.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/filter/butter_bandpass_filter.py` & `miv_os-0.3.0b0/miv/signal/filter/butter_bandpass_filter.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/filter/median_filter.py` & `miv_os-0.3.0b0/miv/signal/filter/median_filter.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/filter/notch_filter.py` & `miv_os-0.3.0b0/miv/signal/filter/notch_filter.py`

 * *Files 0% similar despite different names*

```diff
@@ -46,15 +46,15 @@
 
         Returns
         -------
         Signal
 
         """
         rate = signal.rate
-        b, a = sps.iirnotch(w0=self.f0, Q=self.Q, fs=rate)
+        b, a = sps.iirnotch(f0=self.f0, Q=self.Q, fs=rate)
         y = signal.data.copy()
         num_channel = signal.number_of_channels
         for ch in range(num_channel):
             y[:, ch], h = sps.freqz(b, a, signal.data[:, ch])
         return Signal(data=y, timestamps=signal.timestamps, rate=rate)
 
     def __post_init__(self):
```

### Comparing `miv_os-0.3.0.post2/miv/signal/filter/protocol.py` & `miv_os-0.3.0b0/miv/signal/filter/protocol.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/generator/spike_generation.py` & `miv_os-0.3.0b0/miv/signal/generator/spike_generation.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/similarity/dtw.py` & `miv_os-0.3.0b0/miv/signal/similarity/dtw.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/similarity/simple.py` & `miv_os-0.3.0b0/miv/signal/similarity/simple.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/spike/detection.py` & `miv_os-0.3.0b0/miv/signal/spike/detection.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,14 +1,18 @@
 __doc__ = """
 
+Spike Detection
+###############
+
 Code Example::
 
     detection = ThresholdCutoff(cutoff=3.5)
     spiketrains = detection(signal, timestamps, sampling_rate)
 
+
 .. currentmodule:: miv.signal.spike
 
 .. autosummary::
    :nosignatures:
    :toctree: _toctree/DetectionAPI
 
    SpikeDetectionProtocol
@@ -16,32 +20,29 @@
 
 """
 __all__ = ["ThresholdCutoff", "query_firing_rate_between"]
 
 from typing import Any, Dict, Generator, Iterable, List, Optional, Tuple, Union
 
 import csv
-import functools
 import inspect
-import logging
-import multiprocessing
 import os
 import pathlib
 from dataclasses import dataclass
 
 import matplotlib.pyplot as plt
 import neo
 import numpy as np
 import quantities as pq
 from tqdm import tqdm
 
 from miv.core.datatype import Signal, Spikestamps
 from miv.core.operator import OperatorMixin
 from miv.core.policy import InternallyMultiprocessing
-from miv.core.wrapper import wrap_cacher
+from miv.core.wrapper import wrap_generator_to_generator
 from miv.statistics import firing_rates
 from miv.typing import SignalType, SpikestampsType, TimestampsType
 
 
 @dataclass
 class ThresholdCutoff(OperatorMixin):
     """ThresholdCutoff
@@ -74,46 +75,28 @@
     tag: str = "spike detection"
     progress_bar: bool = False
     units: str = "sec"
     return_neotype: bool = False  # TODO: Remove, shift to spikestamps datatype
 
     num_proc: int = 1
 
-    # @wrap_generator_to_generator
-    @wrap_cacher(cache_tag="spikestamps")
+    # @wrap_output_generator_collapse(Spikestamps)
+    @wrap_generator_to_generator
     def __call__(self, signal: SignalType) -> SpikestampsType:
         """Execute threshold-cutoff method and return spike stamps
 
         Parameters
         ----------
         signal : Signal
 
         Returns
         -------
         spiketrain_list : List[SpikestampsType]
 
         """
-        if not inspect.isgenerator(
-            signal
-        ):  # TODO: Refactor in multiprocessing-enabling decorator
-            return self._detection(signal)
-        else:
-            collapsed_result = Spikestamps()
-            # with multiprocessing.Pool(self.num_proc) as pool:
-            #    #for result in pool.map(functools.partial(ThresholdCutoff._detection, self=self), signal):
-            #    inputs = list(signal)
-            #    print(inputs)
-            #    for result in pool.map(self._detection, inputs): # TODO: Something is not correct here. Check memory usage.
-            #        collapsed_result.extend(spiketrain)
-            for sig in signal:  # TODO: mp
-                collapsed_result.extend(self._detection(sig))
-            return collapsed_result
-
-    # @staticmethod
-    def _detection(self, signal: SignalType):
         # Spike detection for each channel
         spiketrain_list = []
         num_channels = signal.number_of_channels  # type: ignore
         timestamps = signal.timestamps
         rate = signal.rate
         for channel in tqdm(range(num_channels), disable=not self.progress_bar):
             array = signal[channel]  # type: ignore
@@ -134,20 +117,29 @@
                     units=self.units,  # TODO: make this compatible to other units
                     t_stop=timestamps.max(),
                     t_start=timestamps.min(),
                 )
                 spiketrain_list.append(spiketrain)
             else:
                 spiketrain_list.append(spikestamp.astype(np.float_))
-        spikestamps = Spikestamps(spiketrain_list)
-        return spikestamps
+        return Spikestamps(spiketrain_list)
 
     def __post_init__(self):
         super().__init__()
 
+    def after_run_collapse_spiketrain(
+        self, spiketrains: Union[Generator[Spikestamps, None, None], Spikestamps]
+    ):
+        if not inspect.isgenerator(spiketrains):
+            return spiketrains
+        collapsed_result = Spikestamps()
+        for spiketrain in spiketrains:
+            collapsed_result.extend(spiketrain)
+        return collapsed_result
+
     def _compute_spike_threshold(
         self, signal: SignalType, cutoff: float = 5.0, use_mad: bool = True
     ) -> (
         float
     ):  # TODO: make this function compatible to array of cutoffs (for each channel)
         """
         Returns the threshold for the spike detection given an array of signal.
@@ -233,42 +225,28 @@
         return np.array(aligned_spikes)
 
     def plot_spiketrain(
         self,
         spikestamps,
         show: bool = False,
         save_path: Optional[pathlib.Path] = None,
+        ax: Optional[plt.Axes] = None,
     ) -> plt.Axes:
         """
-        Plot spike train in raster
+        Plot spike train
         """
-        t0 = spikestamps.get_first_spikestamp()
-        tf = spikestamps.get_last_spikestamp()
-
-        # TODO: REFACTOR. Make single plot, and change xlim
-        term = 60
-        n_terms = int(np.ceil((tf - t0) / term))
-        if n_terms == 0:
-            # TODO: Warning message
-            return None
-        for idx in range(n_terms):
-            spikes = spikestamps.get_view(
-                idx * term + t0, min((idx + 1) * term + t0, tf)
-            )
+        if ax is None:
             fig, ax = plt.subplots(figsize=(16, 6))
-            ax.eventplot(spikes)
-            ax.set_xlabel("Time (s)")
-            ax.set_ylabel("Channel")
-            if save_path is not None:
-                plt.savefig(os.path.join(save_path, f"spiketrain_raster_{idx:03d}.png"))
-            if not show:
-                plt.close("all")
+        ax.eventplot(spikestamps, color="r")
+        ax.set_xlabel("Time (s)")
+        ax.set_ylabel("Channel")
+        if save_path is not None:
+            plt.savefig(os.path.join(save_path, "spiketrain_raster.png"))
         if show:
             plt.show()
-            plt.close("all")
         return ax
 
     def plot_firing_rate_histogram(self, spikestamps, show=False, save_path=None):
         """Plot firing rate histogram"""
         threshold = 3
 
         rates = firing_rates(spikestamps)["rates"]
@@ -336,8 +314,9 @@
     Returns
     -------
     Spikestamps
         Mask of channels with firing rates between min_firing_rate and max_firing_rate
     """
     rates = np.array(firing_rates(spikestamps)["rates"])
     masks = np.logical_and(rates >= min_firing_rate, rates <= max_firing_rate)
+    print(f"masked: {len(masks)}: {masks}")
     return np.where(masks)[0]
```

### Comparing `miv_os-0.3.0.post2/miv/signal/spike/protocol.py` & `miv_os-0.3.0b0/miv/signal/spike/protocol.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/signal/spike/sorting.py` & `miv_os-0.3.0b0/miv/signal/spike/sorting.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 __doc__ = """
 
 Typical spike-sorting procedure can be described in three steps: (1) spike detection, (2) feature decomposition, and (3) clustering.
-We provide separate module to perform spike-detection; see :ref:`here <api/detection:Spike Detection>`.
+We provide separate module to perform spike-detection; see :ref:`here <api/signal:Spike Detection>`.
 
 We provide `SpikeSorting` module that composes *feature-decomposition* method and *unsupervised-clustering* method.
 A commonly used feature-decomposition method includes PCA or wavelet decomposition.
 For clustering method, one implemented few commonly appearing methods from the literatures (listed below).
 Additionally, one can use out-of-the-box clustering modules from `sklearn`.
 
 .. note:: Depending on the method of clustering, there might be an additional step to find optimum number of cluster.
 
 .. currentmodule:: miv.signal.spike
 
-.. autoclass:: miv.signal.spike.SpikeSorting
+.. autoclass:: SpikeSorting
    :members:
 
 Available Feature Extractor
 ###########################
 
 .. autosummary::
    :toctree: _toctree/SpikeSortingAPI
```

### Comparing `miv_os-0.3.0.post2/miv/statistics/burst.py` & `miv_os-0.3.0b0/miv/statistics/burst.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,49 +1,46 @@
-__all__ = ["burst"]
-
 import os
 
 import matplotlib.pyplot as plt
 import numpy as np
 
 from miv.statistics.spiketrain_statistics import interspike_intervals
 from miv.typing import SpikestampsType
 
 
-def burst(spiketrains: SpikestampsType, channel: int, min_isi: float, min_len: int):
+def burst(spiketrains: SpikestampsType, channel: float, min_isi: float, min_len: float):
     """
-    Calculates parameters critical to characterize bursting phenomenon on a single channel. [1]_
-    Bursting is defined as the occurence of a specified number of spikes (usually >10), with a small interspike interval (usually < 100ms) [2]_, [3]_
+    Calculates parameters critical to characterize bursting phenomenon on a single channel
+    Bursting is defined as the occurence of a specified number of spikes (usually >10), with a small interspike interval (usually < 100ms) [1]_, [2]_
 
     Parameters
     ----------
     spikes : SpikestampsType
        Single spike-stamps
-    channel : int
+    Channel : float
        Channel to analyze
     min_isi : float
        Minimum Interspike Interval (in seconds) to be considered as bursting [standard = 0.1]
-    min_len : int
+    min_len : float
        Minimum number of simultaneous spikes to be considered as bursting [standard = 10]
 
     Returns
     -------
     start_time: float
        The time instances when a burst starts
     burst_duration: float
        The time duration of a particular burst
     burst_len: float
        Number of spikes in a particular burst
     burst_rate: float
        firing rates corresponding to particular bursts
 
-    .. [1] Beggs, John M., and Mark A. Plenz. "Neuronal bursting in cortical circuits." Journal of Neuroscience 23 (2003): 11167-11177.
-    .. [2] Chiappalone, Michela, et al. "Burst detection algorithms for the analysis of spatio-temporal patterns
+    .. [1] Chiappalone, Michela, et al. "Burst detection algorithms for the analysis of spatio-temporal patterns
     in cortical networks of neurons." Neurocomputing 65 (2005): 653-662.
-    .. [3] Eisenman, Lawrence N., et al. "Quantification of bursting and synchrony in cultured
+    .. [2] Eisenman, Lawrence N., et al. "Quantification of bursting and synchrony in cultured
     hippocampal neurons." Journal of neurophysiology 114.2 (2015): 1059-1071.
     """
 
     spike_interval = interspike_intervals(spiketrains[channel])
     assert spike_interval.all() > 0, "Inter Spike Interval cannot be zero"
     burst_spike = (spike_interval <= min_isi).astype(
         np.bool_
```

### Comparing `miv_os-0.3.0.post2/miv/statistics/connectivity/centrality.py` & `miv_os-0.3.0b0/miv/statistics/connectivity/centrality.py`

 * *Files 8% similar despite different names*

```diff
@@ -26,15 +26,15 @@
         for j in range(self.mea_map.shape[1]):
             center = self.mea_map[i, j]
             if center < 0:
                 continue
             if center not in channels:
                 continue
             G.add_node(center)
-            pos[center] = (j, -i)
+            pos[center] = (j, i)
 
     for source in range(n_nodes):
         if channels[source] not in self.mea_map:
             continue
         for target in range(n_nodes):
             if channels[target] not in self.mea_map or target not in channels:
                 continue
@@ -47,33 +47,31 @@
             G.add_edge(channels[source], channels[target], weight=conn)
 
     # Plotting
     nodes = G.nodes()
     centrality = nx.eigenvector_centrality_numpy(G, weight="weight")
     colors = [centrality[n] for n in nodes]
 
-    vmin = np.min(list(centrality.values()))
-    vmax = np.max(list(centrality.values()))
-    v = np.max(np.abs([vmin, vmax]))
+    # mean = np.nanmean(metric_matrix)
+    # std = np.nanstd(metric_matrix)
+    # vmin = max(0.0, mean - 2 * std)
+    # vmax = mean + 2 * std
+
+    # fig = plt.figure()
+    # plt.imshow(nx.adjacency_matrix(G, weight="weight").todense())
+    # if save_path is not None:
+    #    plt.savefig(os.path.join(save_path, "connection_matrix.png"))
 
     fig = plt.figure()
     ax = plt.gca()
 
     # nx.draw_networkx_edges(G, pos, alpha=0.2, ax=ax)
     nc = nx.draw_networkx_nodes(
-        G,
-        pos,
-        nodelist=nodes,
-        node_color=colors,
-        node_size=100,
-        cmap=plt.cm.RdBu,
-        ax=ax,
-        vmin=-v,
-        vmax=v,
-    )
+        G, pos, nodelist=nodes, node_color=colors, node_size=100, cmap=plt.cm.jet, ax=ax
+    )  # , vmin=0, vmax=0.5)
     for node, (x_coord, y_coord) in pos.items():
         ax.text(x_coord - 0.1, y_coord - 0.1, str(node))
     fig.colorbar(nc, ax=ax)
 
     if save_path is not None:
         plt.savefig(os.path.join(save_path, "eigenvector_centrality.png"))
     if show:
```

### Comparing `miv_os-0.3.0.post2/miv/statistics/connectivity/connectivity.py` & `miv_os-0.3.0b0/miv/statistics/connectivity/connectivity.py`

 * *Files 11% similar despite different names*

```diff
@@ -15,15 +15,14 @@
 import pathlib
 import pickle as pkl
 from dataclasses import dataclass
 
 import matplotlib.pyplot as plt
 import networkx as nx
 import numpy as np
-import pyinform
 import pyinform.transferentropy as pyte
 import quantities as pq
 import scipy.stats as spst
 from tqdm import tqdm
 
 from miv.core.datatype import Signal, Spikestamps
 from miv.core.operator import OperatorMixin
@@ -58,22 +57,21 @@
         Random seed. If None, use random seed, by default None
     """
 
     mea: str = None
     channels: Optional[List[int]] = None
     bin_size: float = 0.001
     tag: str = "directional connectivity analysis"
-    progress_bar: bool = False
+    progress_bar: bool = True
 
     skip_surrogate: bool = False
 
     # Surrogate parameters
     surrogate_N: int = 30
     p_threshold: float = 0.05
-    H_threshold: float = 1e-2
     seed: int = None
     num_proc: int = 1
 
     def __post_init__(self):
         super().__init__()
         if isinstance(self.mea, str):
             self.mea_map = mea_map[self.mea]
@@ -90,18 +88,18 @@
         """
 
         binned_spiketrain: Signal = spikestamps.binning(bin_size=self.bin_size)
 
         # Channel Selection
         if self.channels is None:
             n_nodes = binned_spiketrain.number_of_channels
-            channels = tuple(range(n_nodes))
+            channels = list(range(n_nodes))
         else:
             n_nodes = len(self.channels)
-            channels = tuple(self.channels)
+            channels = self.channels
             binned_spiketrain = binned_spiketrain.select(channels)
 
         # Get adjacency matrix based on transfer entropy
         adj_matrix = np.zeros([n_nodes, n_nodes], dtype=np.bool_)  # source -> target
         connectivity_metric_matrix = np.zeros(
             [n_nodes, n_nodes], dtype=np.float_
         )  # source -> target
@@ -111,28 +109,52 @@
             self._get_connection_info,
             binned_spiketrain=binned_spiketrain,
             channels=channels,
             mea=self.mea_map,
             skip_surrogate=self.skip_surrogate,
             surrogate_N=self.surrogate_N,
             seed=self.seed,
-            H_threshold=self.H_threshold,
         )
         with mp.Pool(self.num_proc) as pool:
             for idx, result in enumerate(
                 tqdm(
                     pool.imap(func, pairs),
                     total=len(pairs),
                     disable=not self.progress_bar,
                 )
             ):
                 i, j = pairs[idx]
                 adj_matrix[i, j] = result[0] < self.p_threshold
                 connectivity_metric_matrix[i, j] = result[1]
 
+        # for sidx, source in tqdm(
+        #     enumerate(channels), disable=not self.progress_bar, total=len(channels)
+        # ):
+        #     if source not in self.mea_map:
+        #         continue
+        #     p_values = []
+        #     metric_values = []
+        #     for tidx, target in tqdm(
+        #         enumerate(channels),
+        #         disable=not self.progress_bar,
+        #         leave=False,
+        #         total=len(channels),
+        #     ):
+        #         if source != target and target in self.mea_map:
+        #             source_binned_spiketrain = binned_spiketrain[sidx]
+        #             target_binned_spiketrain = binned_spiketrain[tidx]
+        #             p, metrics = self._get_connection_info(
+        #                 source_binned_spiketrain, target_binned_spiketrain
+        #             )
+        #         else:
+        #             p, metrics = 1, 0
+        #         p_values.append(p)
+        #         metric_values.append(metrics)
+        #     adj_matrix[sidx] = np.array(p_values) < self.p_threshold
+        #     connectivity_metric_matrix[sidx] = np.array(metric_values)
         connection_ratio = adj_matrix.sum() / adj_matrix.ravel().shape[0]
 
         info = dict(
             adjacency_matrix=adj_matrix,
             connectivity_matrix=connectivity_metric_matrix,
             connection_ratio=connection_ratio,
         )
@@ -143,123 +165,77 @@
     def _surrogate_t_test(
         source, target, skip_surrogate=False, surrogate_N=30, seed=None
     ):
         """
         Surrogate t-test
         """
         # Function configuration. TODO: Make this dependency injection
-        te_history = 21
+        func = pyte.transfer_entropy
+        te_history = 4
         sublength = 64
         stride = 8
 
         assert (
             source.shape[0] == target.shape[0]
         ), f"source.shape={source.shape}, target.shape={target.shape}"
         assert (
             source.shape[0] - sublength > 0
         ), f"source.shape[0]={source.shape[0]}, sublength={sublength}"
 
         rng = np.random.default_rng(seed)  # TODO take rng instead
 
-        func = pyte.transfer_entropy
-        te = func(source, target, te_history)
-        normalizer = pyinform.entropyrate.entropy_rate(
-            target, k=te_history, local=False
-        )
-        if np.isclose(normalizer, 0.0):
-            return 0.0, [0.0]
-        te = te / normalizer
+        tes = []
+        for start_index in np.arange(0, source.shape[0] - sublength, stride):
+            end_index = start_index + sublength
+            te = func(
+                source[start_index:end_index], target[start_index:end_index], te_history
+            )
+            tes.append(te)
 
         surrogate_tes = []
-        if skip_surrogate:
-            return te, surrogate_tes
-        for _ in range(surrogate_N):
-            surrogate_source = source.copy()
-            rng.shuffle(surrogate_source)
-            for start_index in np.arange(0, source.shape[0] - sublength, stride):
-                end_index = start_index + sublength
-                surr_te = func(
-                    surrogate_source[start_index:end_index],
-                    target[start_index:end_index],
-                    te_history,
-                )
-                surrogate_tes.append(surr_te / normalizer)
+        if not skip_surrogate:
+            for _ in range(surrogate_N):
+                surrogate_source = source.copy()
+                rng.shuffle(surrogate_source)
+                for start_index in np.arange(0, source.shape[0] - sublength, stride):
+                    end_index = start_index + sublength
+                    surr_te = func(
+                        surrogate_source[start_index:end_index],
+                        target[start_index:end_index],
+                        te_history,
+                    )
+                    surrogate_tes.append(surr_te)
 
-        return te, surrogate_tes
+        return tes, surrogate_tes
 
     @staticmethod
     def _get_connection_info(
-        pair,
-        binned_spiketrain,
-        channels,
-        mea,
-        skip_surrogate,
-        surrogate_N,
-        seed,
-        H_threshold,
+        pair, binned_spiketrain, channels, mea, skip_surrogate, surrogate_N, seed
     ):
         """
         Get connection information
         """
         sid, tid = pair
         if sid == tid:
             return 1, 0
         if channels[sid] not in mea or channels[tid] not in mea:
             return 1, 0
         source = binned_spiketrain[sid]
         target = binned_spiketrain[tid]
-        te, surrogate_te_list = DirectedConnectivity._surrogate_t_test(
+        te_list, surrogate_te_list = DirectedConnectivity._surrogate_t_test(
             source,
             target,
             skip_surrogate=skip_surrogate,
             surrogate_N=surrogate_N,
             seed=seed,
         )
-        if te < H_threshold:
-            return 1, 0
-        if skip_surrogate:
-            return 1, te
-        t_value, p_value = spst.ttest_1samp(surrogate_te_list, te, nan_policy="omit")
-        return p_value, te
-
-    def plot_adjacency_matrix(self, result, save_path=None, show=False):
-        connectivity_metric_matrix = result["connectivity_matrix"]
-
-        fig, ax = plt.subplots(figsize=(12, 12))
-        im = ax.imshow(connectivity_metric_matrix, cmap="gray_r", vmin=0, vmax=1)
-        ax.set_xlabel("Source")
-        ax.set_ylabel("Target")
-        ax.set_title("Transfer Entropy")
-        plt.colorbar(im, ax=ax)
-
-        if save_path is not None:
-            plt.savefig(os.path.join(save_path, "te.png"))
-
-        if show:
-            plt.show()
-
-        plt.close(fig)
-
-    def plot_transfer_entropy_histogram(self, result, save_path=None, show=False):
-        connectivity_metric_matrix = result["connectivity_matrix"]
-
-        fig, ax = plt.subplots(figsize=(12, 12))
-        ax.hist(connectivity_metric_matrix, bins=100)
-        ax.set_xlabel("transfer entropy")
-        ax.set_ylabel("count")
-        ax.set_title("Transfer Entropy Histogram")
-        ax.set_xlim([-0.1, 1.1])
-
-        if save_path is not None:
-            plt.savefig(os.path.join(save_path, "te_histogram.png"))
-
-        if show:
-            plt.show()
-
-        plt.close(fig)
+        t_value, p_value = spst.ttest_ind(
+            te_list, surrogate_te_list, equal_var=False, nan_policy="omit"
+        )
+        return p_value, np.mean(te_list)
 
     def plot_nodewise_connectivity(
         self,
         result: Any,
         save_path: Union[str, pathlib.Path] = None,
         show: bool = False,
     ):
@@ -339,15 +315,15 @@
         pos = {}
         for i in range(self.mea_map.shape[0]):
             for j in range(self.mea_map.shape[1]):
                 center = self.mea_map[i, j]
                 if center < 0:
                     continue
                 G_1.add_node(center)
-                pos[center] = (j, -i)
+                pos[center] = (j, i)
 
         if boolean_connectivity:
             for idx, conn in enumerate(connectivity):
                 if idx == self_index:
                     continue  # No self-connection
                 if idx not in self.mea_map:
                     continue  # No connection if node does not exist
@@ -370,44 +346,35 @@
                 else:
                     G_1.add_edge(idx, self_index, weight=conn)
 
         # Numbering
         # edge_weights = [G_1[u][v]['weight'] if 'weight' in G_1[u][v] else 0.0 for u, v in G_1.edges()]
         plt.figure()
         widths = nx.get_edge_attributes(G_1, "weight")
+        # print(list(widths.items()))
         nx.draw(G_1, pos)
-        if boolean_connectivity:
-            nx.draw_networkx_edges(
-                G_1,
-                pos,
-                edgelist=widths.keys(),
-                ax=plt.gca(),
-            )
-        else:
-            nx.draw_networkx_edges(
-                G_1,
-                pos,
-                edgelist=widths.keys(),
-                edge_color=list(widths.values()),
-                edge_cmap=plt.cm.gray_r,
-                edge_vmin=0.0,
-                edge_vmax=1.0,
-                ax=plt.gca(),
-            )
+        nx.draw_networkx_edges(
+            G_1,
+            pos,
+            edgelist=widths.keys(),
+            width=list(widths.values()),
+            alpha=0.5,
+            edge_color="lightblue",
+            ax=plt.gca(),
+        )
         nx.draw_networkx_labels(
             G_1,
             pos,
             labels=dict(zip(G_1.nodes(), G_1.nodes())),
             font_color="white",
             ax=plt.gca(),
         )
         # for node, (x_coord, y_coord) in pos.items():
         #    plt.text(x_coord - 0.1, y_coord - 0.1, str(node))
 
         plt.savefig(savename)
         plt.close()
 
 
-# TODO
 # @dataclass
 # class UndirectedConnectivity(OperatorMixin):
 #    pass
```

### Comparing `miv_os-0.3.0.post2/miv/statistics/info_theory.py` & `miv_os-0.3.0b0/miv/statistics/info_theory.py`

 * *Files 4% similar despite different names*

```diff
@@ -22,15 +22,14 @@
 import matplotlib.pyplot as plt
 import neo
 import numpy as np
 import pyinform
 import quantities as pq
 import scipy
 import scipy.signal
-from tqdm import tqdm
 
 from miv.core.datatype import Spikestamps
 from miv.statistics.spiketrain_statistics import binned_spiketrain
 
 INFO_METRICS_TAG = Literal["self", "pair", "all"]  # Pragma: no cover
 
 
@@ -117,15 +116,15 @@
         Shannon entropy for the given channel
 
     """
     bin_spike = spiketrains.binning(bin_size=bin_size, t_start=t_start, t_end=t_end)
     prob_spike = (
         bin_spike.data.sum(axis=bin_spike._SIGNALAXIS, keepdims=True)
         / bin_spike.shape[bin_spike._SIGNALAXIS]
-    ).astype(np.float_)
+    )
     prob_no_spike = 1 - prob_spike
     shannon_entropy = -(
         prob_spike * np.log2(prob_spike) + prob_no_spike * np.log2(prob_no_spike)
     )
     return shannon_entropy
 
 
@@ -174,15 +173,15 @@
     spiketrains: Spikestamps,
     history: float,
     bin_size: float,
     t_start: Optional[float] = None,
     t_end: Optional[float] = None,
 ):
     """
-    Estimates the entropy rate for a each channel recording using the binned spiketrain
+    Estimates the entropy rate for a single channel recording using the binned spiketrain
 
     Parameters
     ----------
     spiketrains : Spikestamps
         Single spike-stamps
     history : int
         history length
@@ -197,22 +196,20 @@
     -------
     entropy rate: float
         entropy rate for the given channel
 
     """
     assert history > 0, "history length should be a finite positive value"
     bin_spike = spiketrains.binning(bin_size=bin_size, t_start=t_start, t_end=t_end)
-    entropy_rate = []
+    entropy_rate = np.zeros((bin_spike.shape[bin_spike._CHANNELAXIS],))
     for idx, bin_spike_channel in enumerate(bin_spike):
-        entropy_rate.append(
-            pyinform.entropyrate.entropy_rate(bin_spike_channel, k=history, local=True)[
-                0
-            ]
+        entropy_rate[idx] = pyinform.entropyrate.entropy_rate(
+            bin_spike_channel, k=history
         )
-    return np.asarray(entropy_rate), bin_spike  # TODO: return single type
+    return entropy_rate
 
 
 @tag_info_metrics("self")
 def active_information(
     spiketrains: Spikestamps,
     history: float,
     bin_size: float,
@@ -248,74 +245,14 @@
         active_information[idx] = pyinform.activeinfo.active_info(
             bin_spike_channel, k=history
         )
     return active_information
 
 
 @tag_info_metrics("pair")
-def transfer_entropy(
-    spiketrains: Spikestamps,
-    history: float,
-    bin_size: float,
-    t_start: Optional[float] = None,
-    t_end: Optional[float] = None,
-):
-    """
-    Estimates the transfer entropy for the pair of electorde recordings (X & Y) using the binned spiketrains and history
-
-    Parameters
-    ----------
-    spiketrains : Spikestamps
-        Single spike-stamps
-    history : float
-        history length
-    t_start : float
-        Binning start time
-    t_end : float
-        Binning end time
-    bin_size : float
-        bin size in seconds
-
-    Returns
-    -------
-    transfer_entropy: float
-        Transfer_entropy for the given pair of electrodes
-
-    """
-    assert history > 0, "history length should be a finite positive value"
-    bin_spike = spiketrains.binning(bin_size=bin_size, t_start=t_start, t_end=t_end)
-
-    transfer_entropy_matrix = np.zeros(
-        [bin_spike.number_of_channels, bin_spike.number_of_channels]
-    )
-    for channelx in tqdm(range(bin_spike.number_of_channels)):
-        for channely in tqdm(range(bin_spike.number_of_channels), leave=False):
-            bin_spike_x = bin_spike[channelx]
-            bin_spike_y = bin_spike[channely]
-
-            # np.random.shuffle(bin_spike_x)
-
-            normalizer = pyinform.entropyrate.entropy_rate(
-                bin_spike_y, k=history, local=False
-            )
-            # normalizer = pyinform.mutualinfo.mutual_info(bin_spike_x, bin_spike_y, local=False)
-
-            transfer_entropy = pyinform.transferentropy.transfer_entropy(
-                bin_spike_x, bin_spike_y, k=history, local=False
-            )
-            if np.isclose(normalizer, 0):
-                transfer_entropy_matrix[channelx, channely] = 0
-            else:
-                transfer_entropy_matrix[channelx, channely] = (
-                    transfer_entropy / normalizer
-                )
-    return transfer_entropy_matrix
-
-
-@tag_info_metrics("pair")
 def mutual_information(
     spiketrains: Spikestamps,
     channelx: float,
     channely: float,
     bin_size: float,
     t_start: Optional[float] = None,
     t_end: Optional[float] = None,
@@ -530,14 +467,62 @@
         spiketrains, channely, t_start, t_end, bin_size
     )
     cross_entropy = -np.sum(spike_dist_x * np.log2(spike_dist_y))
     return cross_entropy
 
 
 @tag_info_metrics("pair")
+def transfer_entropy(
+    spiketrains: Spikestamps,
+    channelx: float,
+    channely: float,
+    history: float,
+    bin_size: float,
+    t_start: Optional[float] = None,
+    t_end: Optional[float] = None,
+):
+    """
+    Estimates the transfer entropy for the pair of electorde recordings (X & Y) using the binned spiketrains and history
+
+    Parameters
+    ----------
+    spiketrains : Spikestamps
+        Single spike-stamps
+    channelx : float
+        electrode/channel X
+    channely : float
+        electrode/channel Y
+    history : float
+        history length
+    t_start : float
+        Binning start time
+    t_end : float
+        Binning end time
+    bin_size : float
+        bin size in seconds
+
+    Returns
+    -------
+    transfer_entropy: float
+        Transfer_entropy for the given pair of electrodes
+
+    """
+    assert t_start < t_end, "start time cannot be equal or greater than end time"
+    assert bin_size > 0, "bin_size should be a finite positive value"
+    assert history > 0, "history length should be a finite positive value"
+
+    bin_spike_x = binned_spiketrain(spiketrains, channelx, t_start, t_end, bin_size)
+    bin_spike_y = binned_spiketrain(spiketrains, channely, t_start, t_end, bin_size)
+    transfer_entropy = pyinform.transferentropy.transfer_entropy(
+        bin_spike_x, bin_spike_y, k=history
+    )
+    return transfer_entropy
+
+
+@tag_info_metrics("pair")
 def partial_information_decomposition(
     spiketrains: Spikestamps,
     channelx: float,
     channely: float,
     channelz: float,
     bin_size: float,
     t_start: Optional[float] = None,
```

### Comparing `miv_os-0.3.0.post2/miv/statistics/pairwise_causality.py` & `miv_os-0.3.0b0/miv/statistics/pairwise_causality.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/statistics/peristimulus_analysis.py` & `miv_os-0.3.0b0/miv/statistics/peristimulus_analysis.py`

 * *Files 11% similar despite different names*

```diff
@@ -73,50 +73,48 @@
     def __post_init__(self):
         super().__init__()
         if isinstance(self.mea, str):
             self.mea_map = mea_map[self.mea]
         else:
             self.mea_map = mea_map["64_intanRHD"]
 
-    # @wrap_cacher("psth")
+    @wrap_cacher("psth")
     def __call__(self, events: Spikestamps, spikestamps: Spikestamps):
-        # TODO: Change events datatype to be Event, not Spikestamps
         n_time = int(np.ceil(self.interval / self.binsize))
         time_axis = np.linspace(0, self.interval, n_time)
-        psth = np.zeros((spikestamps.number_of_channels, n_time), dtype=np.float_)
+        psth = np.zeros((spikestamps.number_of_channels, n_time))
         for t_start in events[0]:
             t_end = t_start + n_time * self.binsize
             bst = spikestamps.binning(
                 self.binsize,
                 t_start=t_start + self.stimulus_length,
                 t_end=t_end + self.stimulus_length,
-                return_count=False,
             )
             for channel in range(spikestamps.number_of_channels):
                 psth[channel] += bst[channel][:n_time]
-        psth /= len(events[0])
+        psth /= len(events)
         psth /= self.binsize
         return Signal(data=psth.T, timestamps=time_axis, rate=1.0 / self.binsize)
 
     def plot_psth_in_grid_map(self, psth, show=False, save_path=None):
         mea_map = self.mea_map
         nrow, ncol = mea_map.shape
         fig, axes = plt.subplots(
-            nrow, ncol, figsize=(ncol * 4, nrow * 4), sharex=True, sharey=True
+            nrow, ncol, figsize=(nrow * 4, ncol * 4), sharex=True, sharey=True
         )
         for channel in range(psth.number_of_channels):
             p = psth[channel]
             time = psth.timestamps
             if channel not in mea_map:
                 continue
             w = np.where(mea_map == channel)
             r = w[0][0]
             c = w[1][0]
             axes[r][c].plot(time, p)
-            axes[r][c].set_title(f"channel {channel}")
+            axes[r][c].set_title(f"channel {channel+1}")
         # Bottom row
         for i in range(ncol):
             axes[-1, i].set_xlabel("time (s)")
 
         # Left row
         for i in range(nrow):
             axes[i, 0].set_ylabel("mean (channels) spike rate per bin")
@@ -160,82 +158,42 @@
         psths,
         show=False,
         save_path=None,
     ):
         mea_map = self.mea_map
         nrow, ncol = mea_map.shape
         fig, axes = plt.subplots(
-            nrow, ncol, figsize=(ncol * 4, nrow * 4), sharex=True, sharey=True
+            nrow, ncol, figsize=(nrow * 4, ncol * 4), sharex=True, sharey=True
         )
         for idx, psth in enumerate(psths):
+            print(idx)
+            print(psth.shape)
             for channel in range(psth.number_of_channels):
                 p = psth[channel]
                 time = psth.timestamps
                 if channel not in mea_map:
                     continue
                 w = np.where(mea_map == channel)
                 r = w[0][0]
                 c = w[1][0]
                 axes[r][c].plot(time, p, label=f"PSTH {idx}")
-                axes[r][c].set_title(f"channel {channel}")
+                axes[r][c].set_title(f"channel {channel+1}")
         # Bottom row
         for i in range(ncol):
             axes[-1, i].set_xlabel("time (s)")
 
         # Left row
         for i in range(nrow):
-            axes[i, 0].set_ylabel("mean spike/bin")
+            axes[i, 0].set_ylabel("mean (channels) spike rate per bin")
 
         # Legend
         for i, j in itertools.product(range(nrow), range(ncol)):
             axes[i, j].legend()
 
         plt.suptitle("PSTH: stimulating electrode")
 
         if show:
             plt.show()
         if save_path is not None:
             plt.savefig(os.path.join(save_path, "psth.png"))
 
         return axes
-
-    def plot_psth_area_trend(
-        self,
-        psths,
-        show=False,
-        save_path=None,
-    ):
-        mea_map = self.mea_map
-        nrow, ncol = mea_map.shape
-        fig, axes = plt.subplots(
-            nrow, ncol, figsize=(ncol * 4, nrow * 4), sharex=True, sharey=True
-        )
-        for channel in range(psths[0].number_of_channels):
-            if channel not in mea_map:
-                continue
-            w = np.where(mea_map == channel)
-            r = w[0][0]
-            c = w[1][0]
-
-            hist = []
-            for idx, psth in enumerate(psths):
-                p = psth[channel]
-                time = psth.timestamps
-                hist.append(np.trapz(p, time))
-            axes[r][c].plot(hist)
-            axes[r][c].set_title(f"channel {channel}")
-        # Bottom row
-        for i in range(ncol):
-            axes[-1, i].set_xlabel("data points")
-
-        # Left row
-        for i in range(nrow):
-            axes[i, 0].set_ylabel("Area under PSTH")
-
-        plt.suptitle("PSTH Trend")
-
-        if show:
-            plt.show()
-        if save_path is not None:
-            plt.savefig(os.path.join(save_path, "psth_trend.png"))
-
-        return axes
```

### Comparing `miv_os-0.3.0.post2/miv/statistics/signal_statistics.py` & `miv_os-0.3.0b0/miv/statistics/signal_statistics.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/statistics/spiketrain_statistics.py` & `miv_os-0.3.0b0/miv/statistics/spiketrain_statistics.py`

 * *Files 8% similar despite different names*

```diff
@@ -5,15 +5,15 @@
     "coefficient_variation",
     "binned_spiketrain",  # Deprecated: Remove in the future version ^0.3.0
     "fano_factor",
     "decay_spike_counts",
     "spike_counts_with_kernel",
 ]
 
-from typing import Any, Callable, Dict, Iterable, List, Optional, Union
+from typing import Any, Dict, Iterable, List, Optional, Union
 
 import datetime
 import os
 from dataclasses import dataclass
 
 import elephant.statistics
 import matplotlib.pyplot as plt
@@ -66,20 +66,16 @@
     }
 
 
 @dataclass
 class MFRComparison(OperatorMixin):
     recording_duration: float = None
     tag: str = "Mean Firing Rate Comparison"
-    channels: List[int] = None
 
     def __call__(self, pre_spiketrains: Spikestamps, post_spiketrains: Spikestamps):
-        assert (
-            pre_spiketrains.number_of_channels == post_spiketrains.number_of_channels
-        ), f"Number of channels does not match: {pre_spiketrains.number_of_channels} vs {post_spiketrains.number_of_channels}"
         pre_rates = firing_rates(pre_spiketrains)["rates"]
         post_rates = firing_rates(post_spiketrains)["rates"]
         if self.recording_duration is None:
             self.recording_duration = max(
                 pre_spiketrains.get_last_spikestamp(),
                 post_spiketrains.get_last_spikestamp(),
             ) - min(
@@ -90,18 +86,14 @@
 
     def __post_init__(self):
         super().__init__()
 
     def plot_mfr_comparison(self, output, show=False, save_path=None):
         MFR_pre, MFR_post = output
 
-        if self.channels is not None:
-            MFR_pre = MFR_pre[self.channels]
-            MFR_post = MFR_post[self.channels]
-
         MFR = np.geomspace(1e-1, 1e2)
         kl = 7
         ku = 7
         sigma = (
             np.sqrt(np.mean([MFR_pre, MFR_post]) * self.recording_duration)
             / self.recording_duration
         )
@@ -180,62 +172,72 @@
     """
     interspike = self.interspike_intervals()
     return np.std(interspike) / np.mean(interspike)
 
 
 def fano_factor(
     spiketrains: SpikestampsType,
-    bin_size: float = 0.002,
-    t_start: Optional[float] = None,
-    t_end: Optional[float] = None,
+    channel: float,  # TODO: the function should be independent of channel.
+    t_start: float,
+    t_end: float,
+    n_bins: float,
 ):
     """
     Calculates the Fano factor for given signal by dividing it into the specified number of bins
 
     Parameters
     ----------
     spiketrains : SpikestampsType
         Single spike-stamps
-    bin_size : int
-        Size of the bin in second. Default is 2ms
+    channel : float
+        electrode/channel
     t_start : float
         Binning start time
     t_end : float
         Binning end time
+    n_bins : float
+        Number of bins
 
     Returns
     -------
         fano_fac: float
         fanofactor for the specified channel and conditions
 
     """
-    bin_spike = spiketrains.binning(
-        bin_size=bin_size, t_start=t_start, t_end=t_end, return_count=True
-    )
-    fano_factor = np.zeros(bin_spike.number_of_channels, dtype=np.float_)
-    for channel in range(bin_spike.number_of_channels):
-        array = bin_spike[channel]
-        if np.sum(array) == 0:
-            fano_factor[channel] = np.nan
-        fano_factor[channel] = np.var(array) / np.mean(array)
-    return fano_factor
+    raise NotImplementedError("This function is not implemented yet.")
+    assert (
+        t_start < t_end
+    ), f"End time {t_end} cannot be smaller or equal to start time {t_start}."
+    assert n_bins > 0, "Number of bins should be a positive integer"
+    bin_spike = spiketrains.get_view(t_start, t_end).binning(bin_size=0.002)
+    assert np.sum(bin_spike) != 0, "The channel has no spikes"
+    large_bin = []
+    bin_length = np.int32(np.size(bin_spike) / n_bins)
+    count = 0
+    for i in range(n_bins):
+        large_bin.append(np.sum(bin_spike[count : count + bin_length]))
+        count += bin_length
+    bin_array = np.array(large_bin)
+    fano_fac = np.var(bin_array) / np.mean(bin_array)
+
+    return fano_fac
 
 
 def decay_spike_counts(
     spiketrain, probe_times, amplitude=1.0, decay_rate=5, batchsize=256
 ):
     """
     decay_spike_counts.
 
     Both spiketrain and probe_times should be a 1-d array representing time.
 
     Parameters
     ----------
     spiketrain :
-        Single-channel spiketrain
+        spiketrain
     probe_times :
         probe_times
     amplitude :
         amplitude
     decay_rate :
         decay_rate
     batchsize :
@@ -257,18 +259,17 @@
         exponent[mask] = 0
         decay_count = np.exp(-decay_rate * exponent)
         decay_count[mask] = 0
         result += decay_count.sum(axis=0)
     return result
 
 
-def spike_counts_with_kernel(spiketrain, probe_times, kernel: Callable, batchsize=32):
+def spike_counts_with_kernel(spiketrain, probe_times, kernel, batchsize=32):
     if len(spiketrain) == 0:
         return np.zeros_like(probe_times)
-    spiketrain = np.asarray(spiketrain)
 
     batchsize = min(spiketrain.shape[0], batchsize)
     num_sections = spiketrain.shape[0] // batchsize + (
         1 if spiketrain.shape[0] % batchsize > 0 else 0
     )
 
     result = np.zeros_like(probe_times)
```

### Comparing `miv_os-0.3.0.post2/miv/visualization/causality.py` & `miv_os-0.3.0b0/miv/visualization/causality.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/visualization/connectivity.py` & `miv_os-0.3.0b0/miv/visualization/connectivity.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/visualization/event.py` & `miv_os-0.3.0b0/miv/visualization/event.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/miv/visualization/fft_domain.py` & `miv_os-0.3.0b0/miv/visualization/fft_domain.py`

 * *Files identical despite different names*

### Comparing `miv_os-0.3.0.post2/pyproject.toml` & `miv_os-0.3.0b0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 # Poetry pyproject.toml: https://python-poetry.org/docs/pyproject/
 [build-system]
 requires = ["poetry_core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
 
 [tool.poetry]
 name = "MiV-OS"
-version = "0.3.0.post2"
+version = "0.3.0-beta.0"
 description = "Python software for analysis and computing framework used in MiV project."
 readme = "README.md"
 authors = ["GazzolaLab <skim449@illinois.edu>"]
 license = "MIT"
 repository = "https://github.com/GazzolaLab/MiV-OS"
 homepage = "https://mindinvitro.illinois.edu"
 documentation = "https://miv-os.readthedocs.io"
 keywords = ["neuroscience", "statistics", "data-analysis", "electrophysiology", "neurophysiology"]
 
 # Pypi classifiers: https://pypi.org/classifiers/
 classifiers = [
-  "Development Status :: 4 - Beta",
+  "Development Status :: 3 - Alpha",
   "Intended Audience :: Science/Research",
   "Intended Audience :: Education",
   "Operating System :: OS Independent",
   "License :: OSI Approved :: MIT License",
   "Programming Language :: Python :: 3",
   "Programming Language :: Python :: 3.8",
   "Programming Language :: Python :: 3.9",
@@ -51,15 +51,15 @@
 quantities = "^0.13.0"
 scikit-learn = "^1.1.1"
 seaborn = ">=0.11.2,<0.13.0"
 tqdm = "^4.64.0"
 numpy = "^1.23.2"
 viziphant = "^0.2.0"
 Sphinx = {version = "^5.3.0", optional = true}
-pydata-sphinx-theme = {version = "^0.13", optional = true}
+pydata-sphinx-theme = {version = ">=0.9,<0.13", optional = true}
 readthedocs-sphinx-search = {version = "^0.1.2", optional = true}
 sphinx-autodoc-typehints = {version = "^1.19.1", optional = true}
 myst-parser = {version = "^0.18.1", optional = true}
 numpydoc = {version = "^1.4.0", optional = true}
 sphinx-togglebutton = {version = "^0.3.2", optional = true}
 sphinx-copybutton = {version = "^0.5.0", optional = true}
 sphinxcontrib-mermaid = {version = "^0.8.1", optional = true}
@@ -71,15 +71,14 @@
 pyvis = ">=0.2.1,<0.4.0"
 #lyon = { git = "https://github.com/sciforce/lyon.git", rev = "91dd700", optional = true}
 click = "^8.1.3"
 pyserial = {version = "^3.5", optional = true}
 numba = "^0.56.4"
 machinable = "^4.0"
 coverage = "^7.1.0"
-opencv-python = "^4.7.0.72"
 
 [tool.poetry.dev-dependencies]
 black = "^22.8.0"
 isort = {extras = ["colors"], version = "^5.10.1"}
 mypy = "^1.0.1"
 mypy-extensions = "^1.0.0"
 pre-commit = "^3.0.4"
@@ -207,15 +206,14 @@
     "pragma: no cover",
     "TODO",
 
     # Don't complain if non-runnable code isn't run:
     "if 0:",
     "if __name__ == __main__:",
     "def __repr__",
-    '''def plot_'.*':''',
     "if self.debug:",
     "if settings.DEBUG",
     "if TYPE_CHECKING:",
     "raise AssertionError",
     "raise NotImplementedError",
     '''class '.*\bProtocol\)':''',
     ''''@(abc\.)?'abstractmethod''',
@@ -226,11 +224,11 @@
 
 
 [tool.coverage.run]
 branch = true
 omit = [
     "*/.local/*",
 	"setup.py",
-    "*/__init__.py",
+#"*/__init__.py",
     "miv/io/intan/rhs.py",# not part of the dev target
     "miv/io/asdf/asdf.py",# not part of the dev target
 ]
```

### Comparing `miv_os-0.3.0.post2/PKG-INFO` & `miv_os-0.3.0b0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 Metadata-Version: 2.1
 Name: miv-os
-Version: 0.3.0.post2
+Version: 0.3.0b0
 Summary: Python software for analysis and computing framework used in MiV project.
 Home-page: https://mindinvitro.illinois.edu
 License: MIT
 Keywords: neuroscience,statistics,data-analysis,electrophysiology,neurophysiology
 Author: GazzolaLab
 Author-email: skim449@illinois.edu
 Requires-Python: >=3.8,<3.11
-Classifier: Development Status :: 4 - Beta
+Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Education
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
@@ -35,17 +35,16 @@
 Requires-Dist: matplotlib (>=3.5.2,<4.0.0)
 Requires-Dist: myst-nb (>=0.17.1,<0.18.0) ; extra == "docs"
 Requires-Dist: myst-parser (>=0.18.1,<0.19.0) ; extra == "docs"
 Requires-Dist: neo (>=0.11.0,<0.12.0)
 Requires-Dist: numba (>=0.56.4,<0.57.0)
 Requires-Dist: numpy (>=1.23.2,<2.0.0)
 Requires-Dist: numpydoc (>=1.4.0,<2.0.0) ; extra == "docs"
-Requires-Dist: opencv-python (>=4.7.0.72,<5.0.0.0)
 Requires-Dist: pandas (>=1.4.2,<2.0.0)
-Requires-Dist: pydata-sphinx-theme (>=0.13,<0.14) ; extra == "docs"
+Requires-Dist: pydata-sphinx-theme (>=0.9,<0.13) ; extra == "docs"
 Requires-Dist: pyinform (>=0.2.0,<0.3.0)
 Requires-Dist: pyserial (>=3.5,<4.0) ; extra == "experiment"
 Requires-Dist: pyvis (>=0.2.1,<0.4.0)
 Requires-Dist: quantities (>=0.13.0,<0.14.0)
 Requires-Dist: readthedocs-sphinx-search (>=0.1.2,<0.2.0) ; extra == "docs"
 Requires-Dist: scikit-learn (>=1.1.1,<2.0.0)
 Requires-Dist: scipy (>=1.9.1,<2.0.0)
```

