# Comparing `tmp/coffea-0.7.8.tar.gz` & `tmp/coffea-0.7.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/coffea-0.7.8.tar", last modified: Fri Oct  1 23:54:04 2021, max compression
+gzip compressed data, was "dist/coffea-0.7.9.tar", last modified: Sat Oct 30 19:05:15 2021, max compression
```

## Comparing `coffea-0.7.8.tar` & `coffea-0.7.9.tar`

### file list

```diff
@@ -1,118 +1,119 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/
--rw-r--r--   0 runner    (1001) docker     (121)     1508 2021-10-01 23:54:01.000000 coffea-0.7.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)       77 2021-10-01 23:54:01.000000 coffea-0.7.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     4326 2021-10-01 23:54:04.000000 coffea-0.7.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     4281 2021-10-01 23:54:01.000000 coffea-0.7.8/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/
--rw-r--r--   0 runner    (1001) docker     (121)     1992 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    12310 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/analysis_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/btag_tools/
--rw-r--r--   0 runner    (1001) docker     (121)      276 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/btag_tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     8893 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/btag_tools/btagscalefactor.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/hist/
--rw-r--r--   0 runner    (1001) docker     (121)     1108 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/hist/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2048 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/hist/export.py
--rw-r--r--   0 runner    (1001) docker     (121)    57204 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/hist/hist_tools.py
--rw-r--r--   0 runner    (1001) docker     (121)    39129 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/hist/plot.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/jetmet_tools/
--rw-r--r--   0 runner    (1001) docker     (121)    17711 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/CorrectedJetsFactory.py
--rw-r--r--   0 runner    (1001) docker     (121)     6179 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/CorrectedMETFactory.py
--rw-r--r--   0 runner    (1001) docker     (121)     7335 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/FactorizedJetCorrector.py
--rw-r--r--   0 runner    (1001) docker     (121)     4974 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/JECStack.py
--rw-r--r--   0 runner    (1001) docker     (121)     5700 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/JetCorrectionUncertainty.py
--rw-r--r--   0 runner    (1001) docker     (121)     5380 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/JetResolution.py
--rw-r--r--   0 runner    (1001) docker     (121)     5350 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/JetResolutionScaleFactor.py
--rw-r--r--   0 runner    (1001) docker     (121)      774 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/jetmet_tools/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/lookup_tools/
--rw-r--r--   0 runner    (1001) docker     (121)      281 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3638 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/csv_converters.py
--rw-r--r--   0 runner    (1001) docker     (121)     3611 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/dense_evaluated_lookup.py
--rw-r--r--   0 runner    (1001) docker     (121)     2366 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/dense_lookup.py
--rw-r--r--   0 runner    (1001) docker     (121)     2778 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/dense_mapped_lookup.py
--rw-r--r--   0 runner    (1001) docker     (121)     7482 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/doublecrystalball.py
--rw-r--r--   0 runner    (1001) docker     (121)     2261 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/evaluator.py
--rw-r--r--   0 runner    (1001) docker     (121)     6613 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/extractor.py
--rw-r--r--   0 runner    (1001) docker     (121)     4651 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/jec_uncertainty_lookup.py
--rw-r--r--   0 runner    (1001) docker     (121)     4705 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/jersf_lookup.py
--rw-r--r--   0 runner    (1001) docker     (121)     7649 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/jme_standard_function.py
--rw-r--r--   0 runner    (1001) docker     (121)     3340 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/json_converters.py
--rw-r--r--   0 runner    (1001) docker     (121)     1825 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/lookup_base.py
--rw-r--r--   0 runner    (1001) docker     (121)     8374 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/rochester_lookup.py
--rw-r--r--   0 runner    (1001) docker     (121)     1555 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/root_converters.py
--rw-r--r--   0 runner    (1001) docker     (121)    24129 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lookup_tools/txt_converters.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/lumi_tools/
--rw-r--r--   0 runner    (1001) docker     (121)      343 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lumi_tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     5905 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/lumi_tools/lumi_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/nanoevents/
--rw-r--r--   0 runner    (1001) docker     (121)      413 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    14638 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/factory.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/nanoevents/mapping/
--rw-r--r--   0 runner    (1001) docker     (121)      552 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/mapping/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3703 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/mapping/base.py
--rw-r--r--   0 runner    (1001) docker     (121)     7308 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/mapping/parquet.py
--rw-r--r--   0 runner    (1001) docker     (121)     3071 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/mapping/preloaded.py
--rw-r--r--   0 runner    (1001) docker     (121)     5510 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/mapping/uproot.py
--rw-r--r--   0 runner    (1001) docker     (121)     2257 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/mapping/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/nanoevents/methods/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2789 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/base.py
--rw-r--r--   0 runner    (1001) docker     (121)     2205 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/candidate.py
--rw-r--r--   0 runner    (1001) docker     (121)     4497 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/delphes.py
--rw-r--r--   0 runner    (1001) docker     (121)    12907 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/nanoaod.py
--rw-r--r--   0 runner    (1001) docker     (121)     5867 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/physlite.py
--rw-r--r--   0 runner    (1001) docker     (121)    27616 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/methods/vector.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/nanoevents/schemas/
--rw-r--r--   0 runner    (1001) docker     (121)      335 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3679 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/base.py
--rw-r--r--   0 runner    (1001) docker     (121)    13023 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/delphes.py
--rw-r--r--   0 runner    (1001) docker     (121)    13256 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/nanoaod.py
--rw-r--r--   0 runner    (1001) docker     (121)     5075 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/physlite.py
--rw-r--r--   0 runner    (1001) docker     (121)     3833 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/schema.py
--rw-r--r--   0 runner    (1001) docker     (121)     6329 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/schemas/treemaker.py
--rw-r--r--   0 runner    (1001) docker     (121)     9737 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/transforms.py
--rw-r--r--   0 runner    (1001) docker     (121)      351 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/nanoevents/util.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/
--rw-r--r--   0 runner    (1001) docker     (121)     3650 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    11333 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/accumulator.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/dask/
--rw-r--r--   0 runner    (1001) docker     (121)     2072 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/dask/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3551 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/dataframe.py
--rw-r--r--   0 runner    (1001) docker     (121)    53026 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/executor.py
--rw-r--r--   0 runner    (1001) docker     (121)     9659 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/helpers.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/parsl/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/parsl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2174 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/parsl/condor_config.py
--rw-r--r--   0 runner    (1001) docker     (121)     2177 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/parsl/detail.py
--rw-r--r--   0 runner    (1001) docker     (121)     1835 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/parsl/slurm_config.py
--rw-r--r--   0 runner    (1001) docker     (121)      502 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/parsl/timeout.py
--rw-r--r--   0 runner    (1001) docker     (121)     1653 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/processor.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/servicex/
--rw-r--r--   0 runner    (1001) docker     (121)     1736 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/servicex/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2143 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/servicex/analysis.py
--rw-r--r--   0 runner    (1001) docker     (121)     3019 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/servicex/dask_executor.py
--rw-r--r--   0 runner    (1001) docker     (121)     5029 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/servicex/data_source.py
--rw-r--r--   0 runner    (1001) docker     (121)     6539 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/servicex/executor.py
--rw-r--r--   0 runner    (1001) docker     (121)     2628 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/servicex/local_executor.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/spark/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/spark/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4251 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/spark/detail.py
--rw-r--r--   0 runner    (1001) docker     (121)     6325 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/spark/spark_executor.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/templates/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/templates/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      975 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/templates/spark.py.tmpl
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea/processor/test_items/
--rw-r--r--   0 runner    (1001) docker     (121)     2465 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/test_items/NanoEventsProcessor.py
--rw-r--r--   0 runner    (1001) docker     (121)     2096 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/test_items/NanoTestProcessor.py
--rw-r--r--   0 runner    (1001) docker     (121)     1109 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/test_items/NanoTestProcessorPandas.py
--rw-r--r--   0 runner    (1001) docker     (121)      247 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/test_items/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    33343 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/processor/work_queue_tools.py
--rw-r--r--   0 runner    (1001) docker     (121)     2944 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/util.py
--rw-r--r--   0 runner    (1001) docker     (121)     1676 2021-10-01 23:54:01.000000 coffea-0.7.8/coffea/version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4326 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3355 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      651 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        7 2021-10-01 23:54:04.000000 coffea-0.7.8/coffea.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      165 2021-10-01 23:54:04.000000 coffea-0.7.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     4872 2021-10-01 23:54:01.000000 coffea-0.7.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/
+-rw-r--r--   0 runner    (1001) docker     (121)     1508 2021-10-30 19:05:11.000000 coffea-0.7.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)       77 2021-10-30 19:05:11.000000 coffea-0.7.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     4326 2021-10-30 19:05:15.000000 coffea-0.7.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     4281 2021-10-30 19:05:11.000000 coffea-0.7.9/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/
+-rw-r--r--   0 runner    (1001) docker     (121)     1992 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12310 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/analysis_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/btag_tools/
+-rw-r--r--   0 runner    (1001) docker     (121)      276 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/btag_tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8893 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/btag_tools/btagscalefactor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/hist/
+-rw-r--r--   0 runner    (1001) docker     (121)     1108 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/hist/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2048 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/hist/export.py
+-rw-r--r--   0 runner    (1001) docker     (121)    57204 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/hist/hist_tools.py
+-rw-r--r--   0 runner    (1001) docker     (121)    39129 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/hist/plot.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/jetmet_tools/
+-rw-r--r--   0 runner    (1001) docker     (121)    17711 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/CorrectedJetsFactory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6179 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/CorrectedMETFactory.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7335 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/FactorizedJetCorrector.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4974 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/JECStack.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5700 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/JetCorrectionUncertainty.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5380 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/JetResolution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5350 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/JetResolutionScaleFactor.py
+-rw-r--r--   0 runner    (1001) docker     (121)      774 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/jetmet_tools/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/lookup_tools/
+-rw-r--r--   0 runner    (1001) docker     (121)      281 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      551 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/correctionlib_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3638 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/csv_converters.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3611 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/dense_evaluated_lookup.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2366 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/dense_lookup.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2778 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/dense_mapped_lookup.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7482 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/doublecrystalball.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2504 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/evaluator.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6721 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/extractor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4651 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/jec_uncertainty_lookup.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4705 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/jersf_lookup.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7649 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/jme_standard_function.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3662 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/json_converters.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1825 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/lookup_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8374 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/rochester_lookup.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1555 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/root_converters.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24129 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lookup_tools/txt_converters.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/lumi_tools/
+-rw-r--r--   0 runner    (1001) docker     (121)      343 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lumi_tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5905 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/lumi_tools/lumi_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/nanoevents/
+-rw-r--r--   0 runner    (1001) docker     (121)      413 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14638 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/factory.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/nanoevents/mapping/
+-rw-r--r--   0 runner    (1001) docker     (121)      552 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/mapping/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3703 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/mapping/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7308 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/mapping/parquet.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3071 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/mapping/preloaded.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5510 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/mapping/uproot.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2257 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/mapping/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/nanoevents/methods/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2789 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2205 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/candidate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4497 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/delphes.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12907 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/nanoaod.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5867 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/physlite.py
+-rw-r--r--   0 runner    (1001) docker     (121)    27616 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/methods/vector.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/nanoevents/schemas/
+-rw-r--r--   0 runner    (1001) docker     (121)      335 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3679 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/base.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13023 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/delphes.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13256 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/nanoaod.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5075 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/physlite.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3833 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6531 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/schemas/treemaker.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9737 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/transforms.py
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/nanoevents/util.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/
+-rw-r--r--   0 runner    (1001) docker     (121)     3650 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11333 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/accumulator.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/dask/
+-rw-r--r--   0 runner    (1001) docker     (121)     2072 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/dask/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3551 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/dataframe.py
+-rw-r--r--   0 runner    (1001) docker     (121)    54963 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/executor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9659 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/helpers.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/parsl/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/parsl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2174 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/parsl/condor_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2177 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/parsl/detail.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1835 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/parsl/slurm_config.py
+-rw-r--r--   0 runner    (1001) docker     (121)      502 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/parsl/timeout.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1653 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/processor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/servicex/
+-rw-r--r--   0 runner    (1001) docker     (121)     1736 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/servicex/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2143 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/servicex/analysis.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3479 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/servicex/dask_executor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5029 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/servicex/data_source.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6539 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/servicex/executor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2628 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/servicex/local_executor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/spark/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/spark/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4251 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/spark/detail.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6325 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/spark/spark_executor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/templates/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/templates/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      975 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/templates/spark.py.tmpl
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea/processor/test_items/
+-rw-r--r--   0 runner    (1001) docker     (121)     2465 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/test_items/NanoEventsProcessor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2096 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/test_items/NanoTestProcessor.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1109 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/test_items/NanoTestProcessorPandas.py
+-rw-r--r--   0 runner    (1001) docker     (121)      247 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/test_items/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    35706 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/processor/work_queue_tools.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2944 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/util.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1676 2021-10-30 19:05:11.000000 coffea-0.7.9/coffea/version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     4326 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3400 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      675 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        7 2021-10-30 19:05:15.000000 coffea-0.7.9/coffea.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      165 2021-10-30 19:05:15.000000 coffea-0.7.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     4903 2021-10-30 19:05:11.000000 coffea-0.7.9/setup.py
```

### Comparing `coffea-0.7.8/LICENSE` & `coffea-0.7.9/LICENSE`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/PKG-INFO` & `coffea-0.7.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coffea
-Version: 0.7.8
+Version: 0.7.9
 Summary: Tools for doing Collider HEP style analysis with columnar operations
 Home-page: https://github.com/CoffeaTeam/coffea
 Author: Lindsey Gray (Fermilab)
 Author-email: lagray@fnal.gov
 Maintainer: Lindsey Gray (Fermilab)
 Maintainer-email: lagray@fnal.gov
 License: BSD 3-clause
```

### Comparing `coffea-0.7.8/README.rst` & `coffea-0.7.9/README.rst`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/__init__.py` & `coffea-0.7.9/coffea/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/analysis_tools.py` & `coffea-0.7.9/coffea/analysis_tools.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/btag_tools/btagscalefactor.py` & `coffea-0.7.9/coffea/btag_tools/btagscalefactor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/hist/__init__.py` & `coffea-0.7.9/coffea/hist/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/hist/export.py` & `coffea-0.7.9/coffea/hist/export.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/hist/hist_tools.py` & `coffea-0.7.9/coffea/hist/hist_tools.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/hist/plot.py` & `coffea-0.7.9/coffea/hist/plot.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/CorrectedJetsFactory.py` & `coffea-0.7.9/coffea/jetmet_tools/CorrectedJetsFactory.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/CorrectedMETFactory.py` & `coffea-0.7.9/coffea/jetmet_tools/CorrectedMETFactory.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/FactorizedJetCorrector.py` & `coffea-0.7.9/coffea/jetmet_tools/FactorizedJetCorrector.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/JECStack.py` & `coffea-0.7.9/coffea/jetmet_tools/JECStack.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/JetCorrectionUncertainty.py` & `coffea-0.7.9/coffea/jetmet_tools/JetCorrectionUncertainty.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/JetResolution.py` & `coffea-0.7.9/coffea/jetmet_tools/JetResolution.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/JetResolutionScaleFactor.py` & `coffea-0.7.9/coffea/jetmet_tools/JetResolutionScaleFactor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/jetmet_tools/__init__.py` & `coffea-0.7.9/coffea/jetmet_tools/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/csv_converters.py` & `coffea-0.7.9/coffea/lookup_tools/csv_converters.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/dense_evaluated_lookup.py` & `coffea-0.7.9/coffea/lookup_tools/dense_evaluated_lookup.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/dense_lookup.py` & `coffea-0.7.9/coffea/lookup_tools/dense_lookup.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/dense_mapped_lookup.py` & `coffea-0.7.9/coffea/lookup_tools/dense_mapped_lookup.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/doublecrystalball.py` & `coffea-0.7.9/coffea/lookup_tools/doublecrystalball.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/evaluator.py` & `coffea-0.7.9/coffea/lookup_tools/evaluator.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,21 +1,24 @@
-from .dense_lookup import dense_lookup
-from .dense_evaluated_lookup import dense_evaluated_lookup
-from .jme_standard_function import jme_standard_function
-from .jersf_lookup import jersf_lookup
-from .jec_uncertainty_lookup import jec_uncertainty_lookup
-from .rochester_lookup import rochester_lookup
+from coffea.lookup_tools.dense_lookup import dense_lookup
+from coffea.lookup_tools.dense_evaluated_lookup import dense_evaluated_lookup
+from coffea.lookup_tools.jme_standard_function import jme_standard_function
+from coffea.lookup_tools.jersf_lookup import jersf_lookup
+from coffea.lookup_tools.jec_uncertainty_lookup import jec_uncertainty_lookup
+from coffea.lookup_tools.rochester_lookup import rochester_lookup
+from coffea.lookup_tools.correctionlib_wrapper import correctionlib_wrapper
+
 
 lookup_types = {
     "dense_lookup": dense_lookup,
     "dense_evaluated_lookup": dense_evaluated_lookup,
     "jme_standard_function": jme_standard_function,
     "jersf_lookup": jersf_lookup,
     "jec_uncertainty_lookup": jec_uncertainty_lookup,
     "rochester_lookup": rochester_lookup,
+    "correctionlib_wrapper": correctionlib_wrapper,
 }
 
 
 class evaluator(object):
     """
     The evaluator class serves as a single point of extry for
     looking up values of histograms and other functions read in
```

### Comparing `coffea-0.7.8/coffea/lookup_tools/extractor.py` & `coffea-0.7.9/coffea/lookup_tools/extractor.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,21 +1,28 @@
 from __future__ import print_function
 import os
 
 from coffea.lookup_tools.evaluator import evaluator
 
 from coffea.lookup_tools.root_converters import convert_histo_root_file
 from coffea.lookup_tools.csv_converters import convert_btag_csv_file
-from coffea.lookup_tools.json_converters import convert_histo_json_file
+from coffea.lookup_tools.json_converters import (
+    convert_histo_json_file,
+    convert_correctionlib_file,
+)
 from coffea.lookup_tools.txt_converters import *
 
 file_converters = {
     "root": {"default": convert_histo_root_file, "histo": convert_histo_root_file},
     "csv": {"default": convert_btag_csv_file, "btag": convert_btag_csv_file},
-    "json": {"default": convert_histo_json_file, "histo": convert_histo_json_file},
+    "json": {
+        "default": convert_histo_json_file,
+        "histo": convert_histo_json_file,
+        "corr": convert_correctionlib_file,
+    },
     "txt": {
         "default": convert_jec_txt_file,
         "jec": convert_jec_txt_file,
         "jersf": convert_jersf_txt_file,
         "jr": convert_jr_txt_file,
         "junc": convert_junc_txt_file,
         "ea": convert_effective_area_file,
```

### Comparing `coffea-0.7.8/coffea/lookup_tools/jec_uncertainty_lookup.py` & `coffea-0.7.9/coffea/lookup_tools/jec_uncertainty_lookup.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/jersf_lookup.py` & `coffea-0.7.9/coffea/lookup_tools/jersf_lookup.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/jme_standard_function.py` & `coffea-0.7.9/coffea/lookup_tools/jme_standard_function.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/json_converters.py` & `coffea-0.7.9/coffea/lookup_tools/json_converters.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,23 +1,29 @@
-from ..util import numpy as np
+from ..util import numpy
+import correctionlib
 import json
 
 
+def is_gz_file(filename):
+    with open(filename, "rb") as f:
+        return f.read(2) == b"\x1f\x8b"
+
+
 def extract_json_histo_structure(parselevel, axis_names, axes):
     if "value" in parselevel.keys():
         return
     name = list(parselevel)[0].split(":")[0]
     bins_pairs = [
         key.split(":")[-1].strip("[]").split(",") for key in parselevel.keys()
     ]
     bins = []
     for pair in bins_pairs:
         bins.extend([float(val) for val in pair])
     bins.sort()
-    bins = np.unique(np.array(bins))
+    bins = numpy.unique(numpy.array(bins))
     axis_names.append(name.encode())
     axes[axis_names[-1]] = bins
     extract_json_histo_structure(parselevel[list(parselevel)[0]], axis_names, axes)
 
 
 def extract_json_histo_values(parselevel, binlows, values, val_names):
     if "value" in parselevel.keys():
@@ -62,17 +68,17 @@
             names_and_valnames[histname] = val_names
 
     wrapped_up = {}
     for name, axes in names_and_axes.items():
         theshape = tuple([axes[axis].size - 1 for axis in names_and_orders[name]])
         valsdict = {}
         for vname in names_and_valnames[histname]:
-            valsdict[vname] = np.zeros(shape=theshape).flatten()
-        flatidx = np.arange(np.zeros(shape=theshape).size)
-        binidx = np.unravel_index(flatidx, shape=theshape)
+            valsdict[vname] = numpy.zeros(shape=theshape).flatten()
+        flatidx = numpy.arange(numpy.zeros(shape=theshape).size)
+        binidx = numpy.unravel_index(flatidx, shape=theshape)
         for vname in valsdict:
             for iflat in flatidx:
                 binlows = []
                 for idim, axis in enumerate(names_and_orders[name]):
                     binlows.append(axes[axis][binidx[idim][iflat]])
                 thevals = names_and_binvalues[name][tuple(binlows)]
                 valsdict[vname][iflat] = thevals[vname]
@@ -82,7 +88,13 @@
             bins_in_order.append(axes[axis])
         for vname in valsdict:
             wrapped_up[(name + "_" + vname, "dense_lookup")] = (
                 valsdict[vname],
                 tuple(bins_in_order),
             )
     return wrapped_up
+
+
+def convert_correctionlib_file(filename):
+    cset = correctionlib.CorrectionSet.from_file(filename)
+
+    return {(key, "correctionlib_wrapper"): (cset[key],) for key in cset.keys()}
```

### Comparing `coffea-0.7.8/coffea/lookup_tools/lookup_base.py` & `coffea-0.7.9/coffea/lookup_tools/lookup_base.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/rochester_lookup.py` & `coffea-0.7.9/coffea/lookup_tools/rochester_lookup.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/root_converters.py` & `coffea-0.7.9/coffea/lookup_tools/root_converters.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lookup_tools/txt_converters.py` & `coffea-0.7.9/coffea/lookup_tools/txt_converters.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/lumi_tools/lumi_tools.py` & `coffea-0.7.9/coffea/lumi_tools/lumi_tools.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/factory.py` & `coffea-0.7.9/coffea/nanoevents/factory.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/mapping/__init__.py` & `coffea-0.7.9/coffea/nanoevents/mapping/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/mapping/base.py` & `coffea-0.7.9/coffea/nanoevents/mapping/base.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/mapping/parquet.py` & `coffea-0.7.9/coffea/nanoevents/mapping/parquet.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/mapping/preloaded.py` & `coffea-0.7.9/coffea/nanoevents/mapping/preloaded.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/mapping/uproot.py` & `coffea-0.7.9/coffea/nanoevents/mapping/uproot.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/mapping/util.py` & `coffea-0.7.9/coffea/nanoevents/mapping/util.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/methods/base.py` & `coffea-0.7.9/coffea/nanoevents/methods/base.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/methods/candidate.py` & `coffea-0.7.9/coffea/nanoevents/methods/candidate.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/methods/delphes.py` & `coffea-0.7.9/coffea/nanoevents/methods/delphes.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/methods/nanoaod.py` & `coffea-0.7.9/coffea/nanoevents/methods/nanoaod.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/methods/physlite.py` & `coffea-0.7.9/coffea/nanoevents/methods/physlite.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/methods/vector.py` & `coffea-0.7.9/coffea/nanoevents/methods/vector.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/schemas/base.py` & `coffea-0.7.9/coffea/nanoevents/schemas/base.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/schemas/delphes.py` & `coffea-0.7.9/coffea/nanoevents/schemas/delphes.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/schemas/nanoaod.py` & `coffea-0.7.9/coffea/nanoevents/schemas/nanoaod.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/schemas/physlite.py` & `coffea-0.7.9/coffea/nanoevents/schemas/physlite.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/schemas/schema.py` & `coffea-0.7.9/coffea/nanoevents/schemas/schema.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/nanoevents/schemas/treemaker.py` & `coffea-0.7.9/coffea/nanoevents/schemas/treemaker.py`

 * *Files 4% similar despite different names*

```diff
@@ -37,14 +37,18 @@
     def __init__(self, base_form):
         super().__init__(base_form)
         self._form["contents"] = self._build_collections(self._form["contents"])
 
     def _build_collections(self, branch_forms):
         # Turn any special classes into the appropriate awkward form
         composite_objects = list(set(k.split("/")[0] for k in branch_forms if "/" in k))
+
+        composite_behavior = {  # Dictionary for overriding the default behavior
+            "Tracks": "LorentzVector"
+        }
         for objname in composite_objects:
             # grab the * from "objname/objname.*"
             components = set(
                 k[2 * len(objname) + 2 :]
                 for k in branch_forms
                 if k.startswith(objname + "/")
             )
@@ -64,30 +68,30 @@
                             f"{objname}/{objname}.fCoordinates.fPhi"
                         ),
                         "energy": branch_forms.pop(
                             f"{objname}/{objname}.fCoordinates.fE"
                         ),
                     },
                     objname,
-                    "PtEtaPhiELorentzVector",
+                    composite_behavior.get(objname, "PtEtaPhiELorentzVector"),
                 )
                 branch_forms[objname] = form
             elif components == {
                 "fCoordinates.fX",
                 "fCoordinates.fY",
                 "fCoordinates.fZ",
             }:
                 form = zip_forms(
                     {
                         "x": branch_forms.pop(f"{objname}/{objname}.fCoordinates.fX"),
                         "y": branch_forms.pop(f"{objname}/{objname}.fCoordinates.fY"),
                         "z": branch_forms.pop(f"{objname}/{objname}.fCoordinates.fZ"),
                     },
                     objname,
-                    "Point",
+                    composite_behavior.get(objname, "ThreeVector"),
                 )
                 branch_forms[objname] = form
             else:
                 raise ValueError(
                     f"Unrecognized class with split branches: {components}"
                 )
```

### Comparing `coffea-0.7.8/coffea/nanoevents/transforms.py` & `coffea-0.7.9/coffea/nanoevents/transforms.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/__init__.py` & `coffea-0.7.9/coffea/processor/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/accumulator.py` & `coffea-0.7.9/coffea/processor/accumulator.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/dask/__init__.py` & `coffea-0.7.9/coffea/processor/dask/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/dataframe.py` & `coffea-0.7.9/coffea/processor/dataframe.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/executor.py` & `coffea-0.7.9/coffea/processor/executor.py`

 * *Files 2% similar despite different names*

```diff
@@ -113,14 +113,15 @@
                     self.filename,
                     self.treename,
                     start,
                     stop,
                     self.metadata["uuid"],
                     user_meta,
                 )
+            return target_chunksize
         else:
             n = max(round(self.metadata["numentries"] / target_chunksize), 1)
             actual_chunksize = math.ceil(self.metadata["numentries"] / n)
 
             start = 0
             while start < self.metadata["numentries"]:
                 stop = min(self.metadata["numentries"], start + actual_chunksize)
@@ -131,15 +132,27 @@
                     start,
                     stop,
                     self.metadata["uuid"],
                     user_meta,
                 )
                 start = stop
                 if dynamic_chunksize and next_chunksize:
-                    actual_chunksize = next_chunksize
+                    n = max(
+                        math.ceil(
+                            (self.metadata["numentries"] - start) / next_chunksize
+                        ),
+                        1,
+                    )
+                    actual_chunksize = math.ceil(
+                        (self.metadata["numentries"] - start) / n
+                    )
+            if dynamic_chunksize and next_chunksize:
+                return next_chunksize
+            else:
+                return target_chunksize
 
 
 @dataclass(unsafe_hash=True)
 class WorkItem:
     dataset: str
     filename: str
     treename: str
@@ -305,22 +318,39 @@
             Number of cores for work queue task. If unset, use a whole worker.
         memory : int
             Amount of memory (in MB) for work queue task. If unset, use a whole worker.
         disk : int
             Amount of disk space (in MB) for work queue task. If unset, use a whole worker.
         gpus : int
             Number of GPUs to allocate to each task.  If unset, use zero.
-        resources_mode : one of 'fixed', or 'auto'. Default is 'fixed'.
+        resource_monitor : str
+            If given, one of 'off', 'measure', or 'watchdog'. Default is 'off'.
+            - 'off': turns off resource monitoring. Overriden if resources_mode
+                     is not set to 'fixed'.
+            - 'measure': turns on resource monitoring for Work Queue. The
+                        resources used per task are measured.
+            - 'watchdog': in addition to measuring resources, tasks are terminated if they
+                        go above the cores, memory, or disk specified.
+        resources_mode : str
+            one of 'fixed', 'max-seen', or 'max-throughput'. Default is 'fixed'.
+            Sets the strategy to automatically allocate resources to tasks.
             - 'fixed': allocate cores, memory, and disk specified for each task.
-            - 'auto': use cores, memory, and disk as maximum values to allocate.
-                    Useful when the resources used by a task are not known, as
-                    it lets work queue find an efficient value for maximum
-                    throughput.
-        resource_monitor : bool
-            If true, (false is the default) turns on resource monitoring for Work Queue.
+            - 'max-seen' or 'auto': use the cores, memory, and disk given as maximum values to allocate,
+                          but first try each task by allocating the maximum values seen. Leads
+                          to a good compromise between parallelism and number of retries.
+            - 'max-throughput': Like max-seen, but first tries the task with an
+                          allocation that maximizes overall throughput.
+            If resources_mode is other than 'fixed', preprocessing and
+            accumulation tasks always use the 'max-seen' strategy, as the
+            former tasks always use the same resources, the latter has a
+            distribution of resources that increases over time.
+        split_on_exhaustion: bool
+            Whether to split a processing task in half according to its chunksize when it exhausts its
+            the cores, memory, or disk allocated to it. If False, a task that exhausts resources
+            permanently fails. Default is True.
         fast_terminate_workers: int
             Terminate workers on which tasks have been running longer than average.
             The time limit is computed by multiplying the average runtime of tasks
             by the value of 'fast_terminate_workers'. Since there are
             legitimately slow tasks, no task may trigger fast termination in
             two distinct workers. Less than 1 disables it.
 
@@ -385,16 +415,17 @@
     debug_log: Optional[str] = None
     stats_log: Optional[str] = None
     transactions_log: Optional[str] = None
     password_file: Optional[str] = None
     environment_file: Optional[str] = None
     extra_input_files: List = field(default_factory=list)
     wrapper: Optional[str] = shutil.which("python_package_run")
-    resource_monitor: bool = False
-    resources_mode: str = "fixed"
+    resource_monitor: Optional[str] = "off"
+    resources_mode: Optional[str] = "fixed"
+    split_on_exhaustion: Optional[bool] = True
     fast_terminate_workers: Optional[int] = None
     cores: Optional[int] = None
     memory: Optional[int] = None
     disk: Optional[int] = None
     gpus: Optional[int] = None
     chunks_per_accum: int = 10
     chunks_accum_in_mem: int = 2
@@ -1046,17 +1077,18 @@
             elif not self.skipbadfiles:
                 raise RuntimeError("Metadata for file {} could not be accessed.")
         return final_fileset
 
     def _chunk_generator(self, fileset: Dict, treename: str) -> Generator:
         if self.format == "root":
             if self.maxchunks is None:
+                last_chunksize = self.chunksize
                 for filemeta in fileset:
-                    yield from filemeta.chunks(
-                        self.chunksize,
+                    last_chunksize = yield from filemeta.chunks(
+                        last_chunksize,
                         self.align_clusters,
                         self.dynamic_chunksize,
                     )
             else:
                 # get just enough file info to compute chunking
                 nchunks = defaultdict(int)
                 chunks = []
@@ -1150,14 +1182,15 @@
                         # patch back filename into item
                         item = WorkItem(**dict(asdict(item), filename=filename))
                         rados_parquet_options["ceph_config_path"] = ceph_config_path
 
                     factory = NanoEventsFactory.from_parquet(
                         file=item.filename,
                         treepath=item.treename,
+                        schemaclass=self.schema,
                         metadata=metadata,
                         rados_parquet_options=rados_parquet_options,
                     )
                     events = factory.events()
             else:
                 raise ValueError(
                     "Expected schema to derive from nanoevents.BaseSchema, instead got %r"
```

### Comparing `coffea-0.7.8/coffea/processor/helpers.py` & `coffea-0.7.9/coffea/processor/helpers.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/parsl/condor_config.py` & `coffea-0.7.9/coffea/processor/parsl/condor_config.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/parsl/detail.py` & `coffea-0.7.9/coffea/processor/parsl/detail.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/parsl/slurm_config.py` & `coffea-0.7.9/coffea/processor/parsl/slurm_config.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/processor.py` & `coffea-0.7.9/coffea/processor/processor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/servicex/__init__.py` & `coffea-0.7.9/coffea/processor/servicex/__init__.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/servicex/analysis.py` & `coffea-0.7.9/coffea/processor/servicex/analysis.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/servicex/dask_executor.py` & `coffea-0.7.9/coffea/processor/servicex/local_executor.py`

 * *Files 24% similar despite different names*

```diff
@@ -22,51 +22,44 @@
 # FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 # DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 # CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 # OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 # OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 from typing import Callable, Dict, Optional
-from dask.distributed import Client
-from .executor import run_coffea_processor, Executor
+from .executor import Executor, run_coffea_processor
 
 
-class DaskExecutor(Executor):
-    def __init__(self, client_addr: Optional[str] = None):
-        """Create a Dask executor to process the analysis
-
-        Args:
-            client_addr (Optional[str]): If `None` then create a local cluster that runs in-process.
-                                         Otherwise connect to an already existing cluster.
-        """
-        self.is_local = client_addr is None
-        self.dask = (
-            Client(threads_per_worker=10, asynchronous=True)
-            if self.is_local
-            else Client(client_addr, asynchronous=True)
-        )
+class LocalExecutor(Executor):
+    def __init__(self):
+        pass
 
     def get_result_file_stream(self, datasource, title):
-        if self.is_local:
-            return datasource.stream_result_files(title)
-        else:
-            return datasource.stream_result_file_urls(title)
+        return datasource.stream_result_files(title)
 
     def run_async_analysis(
         self,
         file_url: str,
         tree_name: Optional[str],
         data_type: str,
         meta_data: Dict[str, str],
         process_func: Callable,
     ):
-        """Create a dask future for a dask task to run the analysis."""
-        data_result = self.dask.submit(
-            run_coffea_processor,
+        # TODO: Do we need a second routine here? Can we just use this one?
+        return self._async_analysis(
             events_url=file_url,
             tree_name=tree_name,
             data_type=data_type,
             meta_data=meta_data,
-            proc=process_func,
+            process_func=process_func,
         )
 
-        return data_result
+    async def _async_analysis(
+        self, events_url, tree_name, data_type, meta_data, process_func
+    ):
+        return run_coffea_processor(
+            events_url=events_url,
+            tree_name=tree_name,
+            data_type=data_type,
+            meta_data=meta_data,
+            proc=process_func,
+        )
```

### Comparing `coffea-0.7.8/coffea/processor/servicex/data_source.py` & `coffea-0.7.9/coffea/processor/servicex/data_source.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/servicex/executor.py` & `coffea-0.7.9/coffea/processor/servicex/executor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/spark/detail.py` & `coffea-0.7.9/coffea/processor/spark/detail.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/spark/spark_executor.py` & `coffea-0.7.9/coffea/processor/spark/spark_executor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/templates/spark.py.tmpl` & `coffea-0.7.9/coffea/processor/templates/spark.py.tmpl`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/test_items/NanoEventsProcessor.py` & `coffea-0.7.9/coffea/processor/test_items/NanoEventsProcessor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/test_items/NanoTestProcessor.py` & `coffea-0.7.9/coffea/processor/test_items/NanoTestProcessor.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/test_items/NanoTestProcessorPandas.py` & `coffea-0.7.9/coffea/processor/test_items/NanoTestProcessorPandas.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/processor/work_queue_tools.py` & `coffea-0.7.9/coffea/processor/work_queue_tools.py`

 * *Files 4% similar despite different names*

```diff
@@ -8,14 +8,15 @@
 import signal
 
 from os.path import basename, join
 
 import math
 import numpy
 import scipy
+import random
 
 from tqdm.auto import tqdm
 
 from .executor import (
     WorkItem,
     _compression_wrapper,
     _decompress,
@@ -91,36 +92,39 @@
 class CoffeaWQTask(Task):
     def __init__(
         self, fn_wrapper, infile_function, item_args, itemid, tmpdir, exec_defaults
     ):
         self.itemid = itemid
 
         self.py_result = ResultUnavailable()
+        self._stdout = None
 
         self.clevel = exec_defaults["compression"]
 
         self.fn_wrapper = fn_wrapper
         self.infile_function = infile_function
 
         self.infile_args = join(tmpdir, "args_{}.p".format(self.itemid))
-        self.infile_output = join(tmpdir, "out_{}.p".format(self.itemid))
+        self.outfile_output = join(tmpdir, "out_{}.p".format(self.itemid))
+        self.outfile_stdout = join(tmpdir, "stdout_{}.p".format(self.itemid))
 
         self.retries = exec_defaults["retries"]
 
         with open(self.infile_args, "wb") as wf:
             dill.dump(item_args, wf)
 
         super().__init__(
             self.remote_command(env_file=exec_defaults["environment_file"])
         )
 
         self.specify_input_file(fn_wrapper, "fn_wrapper", cache=False)
         self.specify_input_file(infile_function, "function.p", cache=False)
         self.specify_input_file(self.infile_args, "args.p", cache=False)
-        self.specify_output_file(self.infile_output, "output.p", cache=False)
+        self.specify_output_file(self.outfile_output, "output.p", cache=False)
+        self.specify_output_file(self.outfile_stdout, "stdout.log", cache=False)
 
         for f in exec_defaults["extra_input_files"]:
             self.specify_input_file(f, cache=True)
 
         if exec_defaults["x509_proxy"]:
             self.specify_input_file(exec_defaults["x509_proxy"], cache=True)
 
@@ -133,54 +137,62 @@
     def __len__(self):
         return self.size
 
     def __str__(self):
         return str(self.itemid)
 
     def remote_command(self, env_file=None):
-        fn_command = "python fn_wrapper function.p args.p output.p"
+        fn_command = "python fn_wrapper function.p args.p output.p >stdout.log 2>&1"
         command = fn_command
 
         if env_file:
-            wrap = './py_wrapper -d -e env_file -u "$WORK_QUEUE_SANDBOX"/{}-env -- {}'
-            command = wrap.format(basename(env_file), fn_command)
+            wrap = (
+                './py_wrapper -d -e env_file -u "$WORK_QUEUE_SANDBOX"/{}-env-{} -- {}'
+            )
+            command = wrap.format(basename(env_file), os.getpid(), fn_command)
 
         return command
 
     @property
     def std_output(self):
-        return super().output
+        if not self._stdout:
+            try:
+                with open(self.outfile_stdout, "r") as rf:
+                    self._stdout = rf.read()
+            except Exception:
+                self._stdout = None
+        return self._stdout
 
     def _has_result(self):
         return not (
             self.py_result is None or isinstance(self.py_result, ResultUnavailable)
         )
 
-    # use output to return python result, rathern than stdout are regular wq
+    # use output to return python result, rathern than stdout as regular wq
     @property
     def output(self):
         if not self._has_result():
             try:
-                with open(self.infile_output, "rb") as rf:
+                with open(self.outfile_output, "rb") as rf:
                     result = dill.load(rf)
                     if self.clevel is not None:
                         result = _decompress(result)
                     self.py_result = result
             except Exception as e:
                 self.py_result = ResultUnavailable(e)
         return self.py_result
 
     def cleanup_inputs(self):
         os.remove(self.infile_args)
 
     def cleanup_outputs(self):
-        os.remove(self.infile_output)
+        os.remove(self.outfile_output)
 
     def resubmit(self, tmpdir, exec_defaults):
-        if self.retries < 1:
+        if self.retries < 1 or not exec_defaults["split_on_exhaustion"]:
             raise RuntimeError(
                 "item {} failed permanently. No more retries left.".format(self.itemid)
             )
 
         resubmissions = []
         if self.result == wq.WORK_QUEUE_RESULT_RESOURCE_EXHAUSTION:
             _vprint("splitting {} to reduce resource consumption.", self.itemid)
@@ -188,17 +200,18 @@
         else:
             t = self.clone(tmpdir, exec_defaults)
             t.retries = self.retries - 1
             resubmissions = [t]
 
         for t in resubmissions:
             _vprint(
-                "resubmitting {} partly as {}. {} attempt(s) left.",
+                "resubmitting {} partly as {} with {} events. {} attempt(s) left.",
                 self.itemid,
                 t.itemid,
+                len(t),
                 t.retries,
             )
             _wq_queue.submit(t)
 
     def clone(self, tmpdir, exec_defaults):
         raise NotImplementedError
 
@@ -357,44 +370,46 @@
 
     def split(self, tmpdir, exec_defaults):
         total = len(self.item)
 
         if total < 2:
             raise RuntimeError("processing task cannot be split any further.")
 
-        middle = self.item.entrystart + int(total / 2)
-
-        item_a = WorkItem(
-            self.item.dataset,
-            self.item.filename,
-            self.item.treename,
-            self.item.entrystart,
-            middle,
-            self.item.fileuuid,
-            self.item.usermeta,
-        )
+        # if the chunksize was updated to be less than total, then use that.
+        # Otherwise, just partition the task in two.
+        target_chunksize = exec_defaults["updated_chunksize"]
+        if total <= target_chunksize:
+            target_chunksize = math.ceil(total / 2)
+
+        n = max(math.ceil(total / target_chunksize), 1)
+        actual_chunksize = int(math.ceil(total / n))
+
+        splits = []
+        start = self.item.entrystart
+        while start < self.item.entrystop:
+            stop = min(self.item.entrystop, start + actual_chunksize)
+
+            w = WorkItem(
+                self.item.dataset,
+                self.item.filename,
+                self.item.treename,
+                start,
+                stop,
+                self.item.fileuuid,
+                self.item.usermeta,
+            )
 
-        item_b = WorkItem(
-            self.item.dataset,
-            self.item.filename,
-            self.item.treename,
-            middle,
-            self.item.entrystop,
-            self.item.fileuuid,
-            self.item.usermeta,
-        )
+            t = self.__class__(
+                self.fn_wrapper, self.infile_function, w, tmpdir, exec_defaults
+            )
 
-        task_a = self.__class__(
-            self.fn_wrapper, self.infile_function, item_a, tmpdir, exec_defaults
-        )
-        task_b = self.__class__(
-            self.fn_wrapper, self.infile_function, item_b, tmpdir, exec_defaults
-        )
+            start = stop
+            splits.append(t)
 
-        return [task_a, task_b]
+        return splits
 
     def debug_info(self):
         i = self.item
         msg = super().debug_info()
         return "{} {}".format(
             (i.dataset, i.filename, i.treename, i.entrystart, i.entrystop), msg
         )
@@ -417,24 +432,24 @@
         if not itemid:
             itemid = "accum_{}".format(AccumCoffeaWQTask.tasks_counter)
 
         self.tasks_to_accumulate = tasks_to_accumulate
         self.size = sum(len(t) for t in self.tasks_to_accumulate)
 
         args = [exec_defaults["chunks_accum_in_mem"], exec_defaults["compression"]]
-        args = args + [[basename(t.infile_output) for t in self.tasks_to_accumulate]]
+        args = args + [[basename(t.outfile_output) for t in self.tasks_to_accumulate]]
 
         super().__init__(
             fn_wrapper, infile_function, args, itemid, tmpdir, exec_defaults
         )
 
         self.specify_category("accumulating")
 
         for t in self.tasks_to_accumulate:
-            self.specify_input_file(t.infile_output, cache=False)
+            self.specify_input_file(t.outfile_output, cache=False)
 
     def cleanup_inputs(self):
         super().cleanup_inputs()
         # cleanup files associated with results already accumulated
         for t in self.tasks_to_accumulate:
             t.cleanup_outputs()
 
@@ -565,29 +580,40 @@
     tasks_to_accumulate = []
 
     # ensure items looks like a generator
     if isinstance(items, list):
         items = iter(items)
 
     items_total = exec_defaults["events_total"]
+
+    # "chunksize" is the original chunksize passed to the executor. Always used
+    # if dynamic_chunksize is not given.
     chunksize = exec_defaults["chunksize"]
 
+    # keep a record of the latest computed chunksize, if any
+    exec_defaults["updated_chunksize"] = exec_defaults["chunksize"]
+
     progress_bars = _make_progress_bars(exec_defaults)
 
     signal.signal(signal.SIGINT, _handle_early_terminate)
 
     # Main loop of executor
     while (not early_terminate and items_done < items_total) or not _wq_queue.empty():
         while (
             items_submitted < items_total and _wq_queue.hungry() and not early_terminate
         ):
             update_chunksize = (
                 items_submitted > 0 and exec_defaults["dynamic_chunksize"]
             )
             if update_chunksize:
+                _vprint(
+                    "current chunksize {}",
+                    _compute_chunksize(task_reports, exec_defaults, sample=False),
+                )
+
                 chunksize = _compute_chunksize(task_reports, exec_defaults)
 
             task = _submit_proc_task(
                 fn_wrapper,
                 infile_function,
                 items,
                 chunksize,
@@ -693,15 +719,15 @@
                 len(tasks_to_accumulate)
             )
         )
 
     _vprint("Performing final accumulation...")
 
     accumulator = accumulate_result_files(
-        2, compression, [t.infile_output for t in tasks_to_accumulate], accumulator
+        2, compression, [t.outfile_output for t in tasks_to_accumulate], accumulator
     )
     for t in tasks_to_accumulate:
         t.cleanup_outputs()
     return accumulator
 
 
 def _work_queue_preprocessing(
@@ -752,23 +778,49 @@
         default_resources["disk"] = exec_defaults["disk"]
     if exec_defaults["gpus"]:
         default_resources["gpus"] = exec_defaults["gpus"]
 
     # Enable monitoring and auto resource consumption, if desired:
     _wq_queue.tune("category-steady-n-tasks", 3)
 
-    if exec_defaults["resource_monitor"] or exec_defaults["resources_mode"] == "auto":
-        _wq_queue.enable_monitoring()
+    monitor_enabled = False
+
+    # if resource_monitor is given, and not 'off', then monitoring is activated.
+    # anything other than 'measure' is assumed to be 'watchdog' mode, where in
+    # addition to measuring resources, tasks are killed if they go over their
+    # resources.
+    if exec_defaults["resource_monitor"] and exec_defaults["resource_monitor"] != "off":
+        monitor_enabled = True
+        _wq_queue.enable_monitoring(
+            watchdog=(exec_defaults["resource_monitor"] != "measure")
+        )
+
+    # activate monitoring as a watchdog if it has not been explicitely
+    # activated and we are using an automatic resource allocation.
+    if not monitor_enabled:
+        if (
+            exec_defaults["resources_mode"]
+            and exec_defaults["resources_mode"] != "fixed"
+        ):
+            _wq_queue.enable_monitoring(watchdog=True)
 
     for category in "default preprocessing processing accumulating".split():
         _wq_queue.specify_category_max_resources(category, default_resources)
 
-        if exec_defaults["resources_mode"] == "auto":
+        if exec_defaults["resources_mode"] != "fixed":
             _wq_queue.specify_category_mode(category, wq.WORK_QUEUE_ALLOCATION_MODE_MAX)
 
+            if (
+                category == "processing"
+                and exec_defaults["resources_mode"] == "max-throughput"
+            ):
+                _wq_queue.specify_category_mode(
+                    category, wq.WORK_QUEUE_ALLOCATION_MODE_MAX_THROUGHPUT
+                )
+
         # enable fast termination of workers
         if (
             exec_defaults["fast_terminate_workers"]
             and exec_defaults["fast_terminate_workers"] > 1
         ):
             _wq_queue.activate_fast_abort_category(
                 category, exec_defaults["fast_terminate_workers"]
@@ -782,14 +834,15 @@
     chunksize,
     update_chunksize,
     tmpdir,
     exec_defaults,
 ):
     if update_chunksize:
         item = items.send(chunksize)
+        exec_defaults["updated_chunksize"] = chunksize
     else:
         item = next(items)
 
     task = ProcCoffeaWQTask(fn_wrapper, infile_function, item, tmpdir, exec_defaults)
     task_id = _wq_queue.submit(task)
     _vprint(
         "submitted processing task id {} item {}, with {} events",
@@ -915,15 +968,15 @@
 
 
 def _make_progress_bars(exec_defaults):
     items_total = exec_defaults["events_total"]
     status = exec_defaults["status"]
     unit = exec_defaults["unit"]
     bar_format = exec_defaults["bar_format"]
-    chunksize = exec_defaults["chunksize"]
+    chunksize = exec_defaults["updated_chunksize"]
     chunks_per_accum = exec_defaults["chunks_per_accum"]
 
     submit_bar = tqdm(
         total=items_total,
         disable=not status,
         unit=unit,
         desc="Submitted",
@@ -938,15 +991,15 @@
         desc="Processing",
         bar_format=bar_format,
     )
 
     accumulated_bar = tqdm(
         total=1 + int(items_total / (chunksize * chunks_per_accum)),
         disable=not status,
-        unit="tasks",
+        unit="task",
         desc="Accumulated",
         bar_format=bar_format,
     )
 
     return {
         "submit": submit_bar,
         "process": processed_bar,
@@ -984,19 +1037,18 @@
         msg = format_str.format(*args, **kwargs)
         self.print(msg)
 
 
 _vprint = VerbosePrint()
 
 
-def _ceil_to_pow2(value):
+def _floor_to_pow2(value):
     if value < 1:
         return 1
-
-    return pow(2, math.ceil(math.log2(value)))
+    return pow(2, math.floor(math.log2(value)))
 
 
 def _compute_chunksize(task_reports, exec_defaults, sample=True):
     targets = exec_defaults["dynamic_chunksize"]
 
     chunksize_default = exec_defaults["chunksize"]
     chunksize_time = None
@@ -1018,44 +1070,42 @@
     candidate_sizes = [c for c in [chunksize_time, chunksize_memory] if c]
     if candidate_sizes:
         chunksize = min(candidate_sizes)
     else:
         chunksize = chunksize_default
 
     try:
-        chunksize = _ceil_to_pow2(chunksize)
-        exp = math.ceil(math.log2(chunksize))
+        chunksize = int(_floor_to_pow2(chunksize))
         if sample:
-            # round-up to nearest power of 2, minus 0, 1 or 2 power to better sample the space.
-            exp += numpy.random.choice([-2, -1, 0])
-        else:
-            # on average, this what we would get as the average of all the sampling
-            # this is useful when reporting the final chunksize used.
-            exp += -1
-
-        exp = max(0, exp)
-        chunksize = int(math.pow(2, exp))
+            # sample between value found and one minue, to better explore the
+            # space.  we take advantage of the fact that the function that
+            # generates chunks tries to have equally sized work units per file.
+            # Most files have a different number of events, which is unlikely
+            # to be a multiple of the chunsize computed. Just in case all files
+            # have a multiple of the chunsize, we return chunksize - 1 half the
+            # time.
+            chunksize = random.choice([chunksize, max(chunksize - 1, 1)])
     except ValueError:
         chunksize = chunksize_default
 
     return chunksize
 
 
 def _compute_chunksize_target(target, pairs):
     # if no info to compute dynamic chunksize (e.g. they info is -1), return nothing
     if len(pairs) < 1 or pairs[0][0] < 0:
         return None
 
     avgs = [e / max(1, target) for (target, e) in pairs]
     quantiles = numpy.quantile(avgs, [0.25, 0.5, 0.75], interpolation="nearest")
 
-    # remove outliers outside the 25%---75% range
+    # remove outliers below the 25%
     pairs_filtered = []
     for (i, avg) in enumerate(avgs):
-        if avg >= quantiles[0] and avg <= quantiles[-1]:
+        if avg >= quantiles[0]:
             pairs_filtered.append(pairs[i])
 
     try:
         # separate into time, numevents arrays
         slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(
             [rep[0] for rep in pairs_filtered],
             [rep[1] for rep in pairs_filtered],
```

### Comparing `coffea-0.7.8/coffea/util.py` & `coffea-0.7.9/coffea/util.py`

 * *Files identical despite different names*

### Comparing `coffea-0.7.8/coffea/version.py` & `coffea-0.7.9/coffea/version.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,12 +26,12 @@
 # SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 # CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 # OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 # OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 
 import re
 
-__version__ = "0.7.8"
+__version__ = "0.7.9"
 version = __version__
 version_info = tuple(re.split(r"[-\.]", __version__))
 
 del re
```

### Comparing `coffea-0.7.8/coffea.egg-info/PKG-INFO` & `coffea-0.7.9/coffea.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coffea
-Version: 0.7.8
+Version: 0.7.9
 Summary: Tools for doing Collider HEP style analysis with columnar operations
 Home-page: https://github.com/CoffeaTeam/coffea
 Author: Lindsey Gray (Fermilab)
 Author-email: lagray@fnal.gov
 Maintainer: Lindsey Gray (Fermilab)
 Maintainer-email: lagray@fnal.gov
 License: BSD 3-clause
```

### Comparing `coffea-0.7.8/coffea.egg-info/SOURCES.txt` & `coffea-0.7.9/coffea.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -23,14 +23,15 @@
 coffea/jetmet_tools/FactorizedJetCorrector.py
 coffea/jetmet_tools/JECStack.py
 coffea/jetmet_tools/JetCorrectionUncertainty.py
 coffea/jetmet_tools/JetResolution.py
 coffea/jetmet_tools/JetResolutionScaleFactor.py
 coffea/jetmet_tools/__init__.py
 coffea/lookup_tools/__init__.py
+coffea/lookup_tools/correctionlib_wrapper.py
 coffea/lookup_tools/csv_converters.py
 coffea/lookup_tools/dense_evaluated_lookup.py
 coffea/lookup_tools/dense_lookup.py
 coffea/lookup_tools/dense_mapped_lookup.py
 coffea/lookup_tools/doublecrystalball.py
 coffea/lookup_tools/evaluator.py
 coffea/lookup_tools/extractor.py
```

### Comparing `coffea-0.7.8/coffea.egg-info/requires.txt` & `coffea-0.7.9/coffea.egg-info/requires.txt`

 * *Files 22% similar despite different names*

```diff
@@ -1,11 +1,12 @@
-awkward>=1.3.0
-uproot>=4.1.3
+awkward<2,>=1.5.1
+uproot>=4.1.6
 uproot3-methods>=0.10.0
 uproot3>=3.14.1
+correctionlib>=2.0.0
 pyarrow>=1.0.0
 fsspec
 matplotlib>=3
 numba>=0.50.0
 numpy>=1.16.0
 scipy>=1.1.0
 tqdm>=4.27.0
```

### Comparing `coffea-0.7.8/setup.py` & `coffea-0.7.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -52,18 +52,19 @@
     # =======================
     # """
 
     return description[start:stop].strip()  # before + + after
 
 
 INSTALL_REQUIRES = [
-    "awkward>=1.3.0",
-    "uproot>=4.1.3",
+    "awkward>=1.5.1,<2",
+    "uproot>=4.1.6",
     "uproot3-methods>=0.10.0",
     "uproot3>=3.14.1",
+    "correctionlib>=2.0.0",
     "pyarrow>=1.0.0",
     "fsspec",
     "matplotlib>=3",
     "numba>=0.50.0",
     "numpy>=1.16.0",
     "scipy>=1.1.0",
     "tqdm>=4.27.0",
```

