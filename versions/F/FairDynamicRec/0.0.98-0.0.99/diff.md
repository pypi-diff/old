# Comparing `tmp/FairDynamicRec-0.0.98.tar.gz` & `tmp/FairDynamicRec-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "FairDynamicRec-0.0.98.tar", last modified: Sun Feb 12 11:28:42 2023, max compression
+gzip compressed data, was "FairDynamicRec-0.0.99.tar", last modified: Thu Feb 23 14:19:48 2023, max compression
```

## Comparing `FairDynamicRec-0.0.98.tar` & `FairDynamicRec-0.0.99.tar`

### file list

```diff
@@ -1,78 +1,79 @@
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.420729 FairDynamicRec-0.0.98/
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.300842 FairDynamicRec-0.0.98/FairDynamicRec.egg-info/
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      514 2023-02-12 11:28:42.000000 FairDynamicRec-0.0.98/FairDynamicRec.egg-info/PKG-INFO
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3145 2023-02-12 11:28:42.000000 FairDynamicRec-0.0.98/FairDynamicRec.egg-info/SOURCES.txt
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)        1 2023-02-12 11:28:42.000000 FairDynamicRec-0.0.98/FairDynamicRec.egg-info/dependency_links.txt
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       67 2023-02-12 11:28:42.000000 FairDynamicRec-0.0.98/FairDynamicRec.egg-info/requires.txt
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       17 2023-02-12 11:28:42.000000 FairDynamicRec-0.0.98/FairDynamicRec.egg-info/top_level.txt
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      237 2022-01-06 11:18:18.000000 FairDynamicRec-0.0.98/MANIFEST.in
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      514 2023-02-12 11:28:42.420306 FairDynamicRec-0.0.98/PKG-INFO
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)        0 2022-01-06 10:26:04.000000 FairDynamicRec-0.0.98/README.rst
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.342046 FairDynamicRec-0.0.98/fair_dynamic_rec/
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     8196 2022-12-30 13:18:42.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/.DS_Store
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)        0 2021-12-09 12:48:03.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/__init__.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3627 2023-02-11 13:25:16.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/__main__.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)  7635559 2022-12-20 12:41:02.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/cb1.txt
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)  4204707 2022-12-20 12:41:02.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/cb2.txt
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)  7714442 2022-12-13 17:03:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/cb3.txt
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.371791 FairDynamicRec-0.0.98/fair_dynamic_rec/core/
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     8196 2022-12-30 13:18:42.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/.DS_Store
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       51 2021-12-09 12:54:22.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/__init__.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    26875 2022-12-30 11:51:00.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/config_cmd.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    25699 2022-12-20 11:55:54.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/data_cmd.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    14046 2022-01-11 14:38:41.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/metric_cmd.py
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.406811 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    10244 2022-12-30 16:05:46.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/.DS_Store
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     5469 2022-12-30 15:45:24.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/abstract_ranker.py
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     4471 2019-09-05 15:52:55.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/abstract_ranker.pyc
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    18316 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    15974 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb_itemweighting.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11643 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     9839 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit_itemweigting.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2321 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2348 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound_itemweighting.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     5486 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_hybrid_lsb_linucb.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3308 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_linear_submodular_bandit.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     7166 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_linear_thompson_sampling.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2757 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_linear_upper_confidence_bound.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11556 2022-12-30 21:02:45.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/factor_ucb.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    12105 2022-12-21 07:34:40.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/factor_ucb1.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     8453 2022-11-06 19:46:58.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/factor_ucb2.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    17900 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     9748 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb_1.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3059 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/kl_upper_confidence_bound.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11356 2023-02-12 11:28:24.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_neighbor_bandit.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     9973 2023-02-11 13:25:16.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_neighbor_bandit1.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    13882 2022-11-06 14:09:18.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_submodular_bandit.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     5903 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_submodular_bandit_1.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     5500 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_submodular_bandit_2.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3273 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2125 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_1.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1822 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_2.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1087 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/lsb_random.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2288 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/naive_epsilon_greedy.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2247 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/naive_greedy.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      751 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/random.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1989 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/thompson_sampling.py
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.412037 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.412680 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulator/
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1951 2021-12-30 19:06:24.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulator/cascade_model.py
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     7827 2021-04-21 08:24:34.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulators.py
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     4608 2019-09-05 15:52:55.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulators.pyc
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      249 2022-10-24 08:58:36.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/environment.py
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)    37564 2023-02-06 09:51:39.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/simulation.py
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     9426 2021-04-06 22:02:50.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/simulation_hybrid.py
--rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     8056 2021-04-20 20:50:52.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/simulation_naive.py
-drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-12 11:28:42.419272 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     6148 2021-12-17 21:05:22.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/.DS_Store
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      106 2021-12-22 21:40:07.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/data_handler.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      963 2022-01-06 11:23:11.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/errors.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     4216 2022-01-06 11:23:11.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/files.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1777 2022-02-15 17:47:57.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/online_logistic_regression.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2311 2023-02-06 09:51:39.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/outputs.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3521 2022-12-11 11:50:21.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/ranker_utils.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3027 2022-05-06 20:42:20.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/utils.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2790 2022-01-06 11:23:11.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/xml_utils.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2753 2022-01-10 18:13:58.000000 FairDynamicRec-0.0.98/fair_dynamic_rec/core/visualization_cmd.py
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       38 2023-02-12 11:28:42.420884 FairDynamicRec-0.0.98/setup.cfg
--rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1116 2023-02-12 11:28:40.000000 FairDynamicRec-0.0.98/setup.py
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.905870 FairDynamicRec-0.0.99/
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.785147 FairDynamicRec-0.0.99/FairDynamicRec.egg-info/
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      514 2023-02-23 14:19:48.000000 FairDynamicRec-0.0.99/FairDynamicRec.egg-info/PKG-INFO
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3202 2023-02-23 14:19:48.000000 FairDynamicRec-0.0.99/FairDynamicRec.egg-info/SOURCES.txt
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)        1 2023-02-23 14:19:48.000000 FairDynamicRec-0.0.99/FairDynamicRec.egg-info/dependency_links.txt
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       67 2023-02-23 14:19:48.000000 FairDynamicRec-0.0.99/FairDynamicRec.egg-info/requires.txt
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       17 2023-02-23 14:19:48.000000 FairDynamicRec-0.0.99/FairDynamicRec.egg-info/top_level.txt
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      237 2022-01-06 11:18:18.000000 FairDynamicRec-0.0.99/MANIFEST.in
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      514 2023-02-23 14:19:48.905639 FairDynamicRec-0.0.99/PKG-INFO
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)        0 2022-01-06 10:26:04.000000 FairDynamicRec-0.0.99/README.rst
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.825830 FairDynamicRec-0.0.99/fair_dynamic_rec/
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     8196 2022-12-30 13:18:42.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/.DS_Store
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)        0 2021-12-09 12:48:03.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/__init__.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3627 2023-02-23 14:19:16.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/__main__.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)  7635559 2022-12-20 12:41:02.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/cb1.txt
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)  4204707 2022-12-20 12:41:02.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/cb2.txt
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)  7714442 2022-12-13 17:03:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/cb3.txt
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.853407 FairDynamicRec-0.0.99/fair_dynamic_rec/core/
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     8196 2023-02-12 19:01:00.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/.DS_Store
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       51 2021-12-09 12:54:22.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/__init__.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    26875 2022-12-30 11:51:00.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/config_cmd.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    25699 2022-12-20 11:55:54.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/data_cmd.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    14046 2022-01-11 14:38:41.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/metric_cmd.py
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.892509 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    10244 2022-12-30 16:05:46.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/.DS_Store
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     5469 2022-12-30 15:45:24.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/abstract_ranker.py
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     4471 2019-09-05 15:52:55.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/abstract_ranker.pyc
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    18316 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    15974 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb_itemweighting.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11643 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     9839 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit_itemweigting.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2321 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2348 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound_itemweighting.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     5486 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_hybrid_lsb_linucb.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3308 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_linear_submodular_bandit.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     7166 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_linear_thompson_sampling.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2757 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_linear_upper_confidence_bound.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11556 2022-12-30 21:02:45.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/factor_ucb.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    12105 2022-12-21 07:34:40.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/factor_ucb1.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     8453 2022-11-06 19:46:58.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/factor_ucb2.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    17900 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     9748 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb_1.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3059 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/kl_upper_confidence_bound.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11392 2023-02-23 14:16:17.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_neighbor_bandit.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     9973 2023-02-11 13:25:16.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_neighbor_bandit1.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    11370 2023-02-12 19:00:13.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_neighbor_bandit3.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)    13882 2022-11-06 14:09:18.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_submodular_bandit.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     5903 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_submodular_bandit_1.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     5500 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_submodular_bandit_2.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3273 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2125 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_1.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1822 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_2.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1087 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/lsb_random.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2288 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/naive_epsilon_greedy.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2247 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/naive_greedy.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      751 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/random.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1989 2022-11-05 11:33:31.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/thompson_sampling.py
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.897704 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.898435 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulator/
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1951 2021-12-30 19:06:24.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulator/cascade_model.py
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     7827 2021-04-21 08:24:34.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulators.py
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     4608 2019-09-05 15:52:55.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulators.pyc
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      249 2022-10-24 08:58:36.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/environment.py
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)    37809 2023-02-23 12:52:27.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/simulation.py
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     9426 2021-04-06 22:02:50.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/simulation_hybrid.py
+-rwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)     8056 2021-04-20 20:50:52.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/simulation_naive.py
+drwxr-xr-x   0 m.mansouryuva.nl   (501) staff       (20)        0 2023-02-23 14:19:48.905074 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     6148 2021-12-17 21:05:22.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/.DS_Store
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      106 2021-12-22 21:40:07.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/data_handler.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)      963 2022-01-06 11:23:11.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/errors.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     4216 2022-01-06 11:23:11.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/files.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1777 2022-02-15 17:47:57.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/online_logistic_regression.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2311 2023-02-06 09:51:39.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/outputs.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3521 2022-12-11 11:50:21.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/ranker_utils.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     3027 2022-05-06 20:42:20.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/utils.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2790 2022-01-06 11:23:11.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/xml_utils.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     2753 2022-01-10 18:13:58.000000 FairDynamicRec-0.0.99/fair_dynamic_rec/core/visualization_cmd.py
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)       38 2023-02-23 14:19:48.905950 FairDynamicRec-0.0.99/setup.cfg
+-rw-r--r--   0 m.mansouryuva.nl   (501) staff       (20)     1116 2023-02-23 14:19:16.000000 FairDynamicRec-0.0.99/setup.py
```

### Comparing `FairDynamicRec-0.0.98/FairDynamicRec.egg-info/PKG-INFO` & `FairDynamicRec-0.0.99/FairDynamicRec.egg-info/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: FairDynamicRec
-Version: 0.0.98
+Version: 0.0.99
 Summary: The FairDynamicRec project aims to facilitate recommender system experiments in dynamic setting where system is operating over time.
 Home-page: UNKNOWN
 Author: Masoud Mansoury
 Author-email: masoodmansoury@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `FairDynamicRec-0.0.98/FairDynamicRec.egg-info/SOURCES.txt` & `FairDynamicRec-0.0.99/FairDynamicRec.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -35,14 +35,15 @@
 fair_dynamic_rec/core/rankers/factor_ucb1.py
 fair_dynamic_rec/core/rankers/factor_ucb2.py
 fair_dynamic_rec/core/rankers/hybrid_lsb_linucb.py
 fair_dynamic_rec/core/rankers/hybrid_lsb_linucb_1.py
 fair_dynamic_rec/core/rankers/kl_upper_confidence_bound.py
 fair_dynamic_rec/core/rankers/linear_neighbor_bandit.py
 fair_dynamic_rec/core/rankers/linear_neighbor_bandit1.py
+fair_dynamic_rec/core/rankers/linear_neighbor_bandit3.py
 fair_dynamic_rec/core/rankers/linear_submodular_bandit.py
 fair_dynamic_rec/core/rankers/linear_submodular_bandit_1.py
 fair_dynamic_rec/core/rankers/linear_submodular_bandit_2.py
 fair_dynamic_rec/core/rankers/linear_upper_confidence_bound.py
 fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_1.py
 fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_2.py
 fair_dynamic_rec/core/rankers/lsb_random.py
```

### Comparing `FairDynamicRec-0.0.98/PKG-INFO` & `FairDynamicRec-0.0.99/PKG-INFO`

 * *Files 21% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: FairDynamicRec
-Version: 0.0.98
+Version: 0.0.99
 Summary: The FairDynamicRec project aims to facilitate recommender system experiments in dynamic setting where system is operating over time.
 Home-page: UNKNOWN
 Author: Masoud Mansoury
 Author-email: masoodmansoury@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/.DS_Store` & `FairDynamicRec-0.0.99/fair_dynamic_rec/.DS_Store`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/__main__.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/__main__.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/cb1.txt` & `FairDynamicRec-0.0.99/fair_dynamic_rec/cb1.txt`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/cb2.txt` & `FairDynamicRec-0.0.99/fair_dynamic_rec/cb2.txt`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/cb3.txt` & `FairDynamicRec-0.0.99/fair_dynamic_rec/cb3.txt`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/.DS_Store` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/.DS_Store`

 * *Files 12% similar despite different names*

```diff
@@ -291,39 +291,39 @@
 00001220: 2f3b 525f 6b6c 6d6e 6f88 0000 0000 0000  /;R_klmno.......
 00001230: 0101 0000 0000 0000 000d 0000 0000 0000  ................
 00001240: 0000 0000 0000 0000 0089 0000 0007 0072  ...............r
 00001250: 0061 006e 006b 0065 0072 0073 6963 7670  .a.n.k.e.r.sicvp
 00001260: 626c 6f62 0000 01cd 6270 6c69 7374 3030  blob....bplist00
 00001270: df10 1001 0203 0405 0607 0809 0a0b 0c0d  ................
 00001280: 0e0f 1011 1213 1114 1115 1615 1718 1519  ................
-00001290: 121b 1c5f 1013 6261 636b 6772 6f75 6e64  ..._..background
-000012a0: 436f 6c6f 7242 6c75 655f 100f 7368 6f77  ColorBlue_..show
-000012b0: 4963 6f6e 5072 6576 6965 7758 7465 7874  IconPreviewXtext
-000012c0: 5369 7a65 5f10 1262 6163 6b67 726f 756e  Size_..backgroun
-000012d0: 6443 6f6c 6f72 5265 645e 6261 636b 6772  dColorRed^backgr
-000012e0: 6f75 6e64 5479 7065 5f10 1462 6163 6b67  oundType_..backg
-000012f0: 726f 756e 6443 6f6c 6f72 4772 6565 6e5b  roundColorGreen[
-00001300: 6772 6964 4f66 6673 6574 585f 100f 7363  gridOffsetX_..sc
-00001310: 726f 6c6c 506f 7369 7469 6f6e 595b 6772  rollPositionY[gr
-00001320: 6964 4f66 6673 6574 595c 7368 6f77 4974  idOffsetY\showIt
-00001330: 656d 496e 666f 5f10 1276 6965 774f 7074  emInfo_..viewOpt
-00001340: 696f 6e73 5665 7273 696f 6e5f 100f 7363  ionsVersion_..sc
-00001350: 726f 6c6c 506f 7369 7469 6f6e 5859 6172  rollPositionXYar
-00001360: 7261 6e67 6542 795d 6c61 6265 6c4f 6e42  rangeBy]labelOnB
-00001370: 6f74 746f 6d58 6963 6f6e 5369 7a65 5b67  ottomXiconSize[g
+00001290: 1a1a 1c5f 1013 6261 636b 6772 6f75 6e64  ..._..background
+000012a0: 436f 6c6f 7242 6c75 6558 6963 6f6e 5369  ColorBlueXiconSi
+000012b0: 7a65 5874 6578 7453 697a 655f 1012 6261  zeXtextSize_..ba
+000012c0: 636b 6772 6f75 6e64 436f 6c6f 7252 6564  ckgroundColorRed
+000012d0: 5e62 6163 6b67 726f 756e 6454 7970 655f  ^backgroundType_
+000012e0: 1014 6261 636b 6772 6f75 6e64 436f 6c6f  ..backgroundColo
+000012f0: 7247 7265 656e 5b67 7269 644f 6666 7365  rGreen[gridOffse
+00001300: 7458 5f10 0f73 6372 6f6c 6c50 6f73 6974  tX_..scrollPosit
+00001310: 696f 6e59 5b67 7269 644f 6666 7365 7459  ionY[gridOffsetY
+00001320: 5c73 686f 7749 7465 6d49 6e66 6f5f 1012  \showItemInfo_..
+00001330: 7669 6577 4f70 7469 6f6e 7356 6572 7369  viewOptionsVersi
+00001340: 6f6e 5f10 0f73 6372 6f6c 6c50 6f73 6974  on_..scrollPosit
+00001350: 696f 6e58 5961 7272 616e 6765 4279 5d6c  ionXYarrangeBy]l
+00001360: 6162 656c 4f6e 426f 7474 6f6d 5f10 0f73  abelOnBottom_..s
+00001370: 686f 7749 636f 6e50 7265 7669 6577 5b67  howIconPreview[g
 00001380: 7269 6453 7061 6369 6e67 233f f000 0000  ridSpacing#?....
-00001390: 0000 0009 2340 2800 0000 0000 0010 0023  ....#@(........#
-000013a0: 0000 0000 0000 0000 2340 6ac0 0000 0000  ........#@j.....
-000013b0: 0008 1400 0000 0000 0000 0000 0000 0000  ................
-000013c0: 0000 0154 6e61 6d65 0923 4050 0000 0000  ...Tname.#@P....
-000013d0: 0000 2340 4b00 0000 0000 0000 0800 2b00  ..#@K.........+.
-000013e0: 4100 5300 5c00 7100 8000 9700 a300 b500  A.S.\.q.........
-000013f0: c100 ce00 e300 f500 ff01 0d01 1601 2201  ..............".
-00001400: 2b01 2c01 3501 3701 4001 4901 4a01 5b01  +.,.5.7.@.I.J.[.
-00001410: 6001 6101 6a00 0000 0000 0002 0100 0000  `.a.j...........
+00001390: 0000 0023 4050 0000 0000 0000 2340 2800  ...#@P......#@(.
+000013a0: 0000 0000 0010 0023 0000 0000 0000 0000  .......#........
+000013b0: 2340 75f8 0000 0000 0008 1400 0000 0000  #@u.............
+000013c0: 0000 0000 0000 0000 0000 0154 6e61 6d65  ...........Tname
+000013d0: 0909 2340 4b00 0000 0000 0000 0800 2b00  ..#@K.........+.
+000013e0: 4100 4a00 5300 6800 7700 8e00 9a00 ac00  A.J.S.h.w.......
+000013f0: b800 c500 da00 ec00 f601 0401 1601 2201  ..............".
+00001400: 2b01 3401 3d01 3f01 4801 5101 5201 6301  +.4.=.?.H.Q.R.c.
+00001410: 6801 6901 6a00 0000 0000 0002 0100 0000  h.i.j...........
 00001420: 0000 0000 1d00 0000 0000 0000 0000 0000  ................
 00001430: 0000 0001 7300 0000 0700 7200 6100 6e00  ....s.....r.a.n.
 00001440: 6b00 6500 7200 7376 5372 6e6c 6f6e 6700  k.e.r.svSrnlong.
 00001450: 0000 0100 0000 0a00 7300 6900 6d00 7500  ........s.i.m.u.
 00001460: 6c00 6100 7400 6f00 7200 7349 6c6f 6362  l.a.t.o.r.sIlocb
 00001470: 6c6f 6200 0000 1000 0002 6700 0000 2eff  lob.......g.....
 00001480: ffff ffff ff00 0000 0000 0a00 7300 6900  ............s.i.
```

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/config_cmd.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/config_cmd.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/data_cmd.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/data_cmd.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/metric_cmd.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/metric_cmd.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/.DS_Store` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/.DS_Store`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/abstract_ranker.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/abstract_ranker.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/abstract_ranker.pyc` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/abstract_ranker.pyc`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb_itemweighting.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_hybrid_lsb_linucb_itemweighting.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit_itemweigting.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_submodular_bandit_itemweigting.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound_itemweighting.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ea_linear_upper_confidence_bound_itemweighting.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_hybrid_lsb_linucb.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_hybrid_lsb_linucb.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_linear_submodular_bandit.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_linear_submodular_bandit.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_linear_thompson_sampling.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_linear_thompson_sampling.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/ears_linear_upper_confidence_bound.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/ears_linear_upper_confidence_bound.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/factor_ucb.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/factor_ucb.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/factor_ucb1.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/factor_ucb1.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/factor_ucb2.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/factor_ucb2.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb_1.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/hybrid_lsb_linucb_1.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/kl_upper_confidence_bound.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/kl_upper_confidence_bound.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_neighbor_bandit.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_neighbor_bandit.py`

 * *Files 1% similar despite different names*

```diff
@@ -168,15 +168,16 @@
             if self.d.sum() != 0:
                 self.U = np.dot(np.dot(self.CInv, self.d), self.EInv)
                 self.U = self.U / np.sqrt(np.sum(self.U ** 2))
 
             self.n_samples[user] += len(_clicks)
             self.n_clicks[user] += sum(_clicks)
 
-            # self.writeParams(round)
+            if round % 1000 == 0:
+                self.writeParams(round)
 
     def __collect_feedback(self, click, ranking):
         """
         :param y:
         :return: the last observed position.
         """
         # With  Cascade assumption, only the first click counts.
```

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_neighbor_bandit1.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_neighbor_bandit1.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_submodular_bandit.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_submodular_bandit.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_submodular_bandit_1.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_submodular_bandit_1.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_submodular_bandit_2.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_submodular_bandit_2.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_1.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_1.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_2.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/linear_upper_confidence_bound_2.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/lsb_random.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/lsb_random.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/naive_epsilon_greedy.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/naive_epsilon_greedy.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/naive_greedy.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/naive_greedy.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/random.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/random.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/rankers/thompson_sampling.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/rankers/thompson_sampling.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulator/cascade_model.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulator/cascade_model.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulators.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulators.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/click_simulators.pyc` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/click_simulators.pyc`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/simulation.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/simulation.py`

 * *Files 0% similar despite different names*

```diff
@@ -176,18 +176,22 @@
                 # self.optimal_scores[:, dataObj.feature_data['test_item_topical_features'].shape[1]:] = dataObj.feature_data['test_item_latent_features'][ranking]
                 delta[:, dataObj.feature_data['test_item_topical_features'].shape[1]:] = dataObj.feature_data['train_item_latent_features'][ranking]
                 optimal_scores[i, :] = self.user_features[i].dot(delta.T)
             return optimal_rankings, optimal_scores
         elif config.optimal_ranker == 'item_similarity':
             self.item_sim_matrix = cosine_similarity(dataObj.test_data.T)
             np.fill_diagonal(self.item_sim_matrix, 0)
-            probs = dataObj.test_data.dot(self.item_sim_matrix)
+            self.item_sim_matrix = self.item_sim_matrix / self.item_sim_matrix.sum(axis=0)
+            self.item_sim_matrix[np.isnan(self.item_sim_matrix)] = 0
+            self.similarity_probs = dataObj.test_data.dot(self.item_sim_matrix)
+
+            # probs = dataObj.test_data.dot(self.item_sim_matrix)
             # probs = (probs-np.min(probs))/(np.max(probs)-np.min(probs))
             # self.similarity_probs = probs/np.sqrt(np.sum(probs**2))
-            self.similarity_probs = normalize(probs, axis=1, norm='l1')*100
+            # self.similarity_probs = normalize(probs, axis=1, norm='l1')*100
             # row_max = np.tile(np.amax(probs, axis=1).reshape(dataObj.test_data.shape[0],1), (1,dataObj.test_data.shape[1]))
             # row_min = np.tile(np.amin(probs, axis=1).reshape(dataObj.test_data.shape[0],1), (1,dataObj.test_data.shape[1]))
             # self.similarity_probs = (probs - row_min) / (row_max - row_min)
             optimal_rankings = np.argsort(-self.similarity_probs)[:, :config.list_size]
             # batch_item_features = np.take(self.item_sim_matrix, optimal_rankings, axis=0)
             n_users = dataObj.n_users #self.user_features.shape[0]
             optimal_scores = np.zeros((n_users, config.list_size))
```

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/simulation_hybrid.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/simulation_hybrid.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/simulators/simulation_naive.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/simulators/simulation_naive.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/.DS_Store` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/.DS_Store`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/errors.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/errors.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/files.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/files.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/online_logistic_regression.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/online_logistic_regression.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/outputs.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/outputs.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/ranker_utils.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/ranker_utils.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/utils.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/utils.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/util/xml_utils.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/util/xml_utils.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/fair_dynamic_rec/core/visualization_cmd.py` & `FairDynamicRec-0.0.99/fair_dynamic_rec/core/visualization_cmd.py`

 * *Files identical despite different names*

### Comparing `FairDynamicRec-0.0.98/setup.py` & `FairDynamicRec-0.0.99/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.rst", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="FairDynamicRec",
-    version="0.0.98",
+    version="0.0.99",
 	scripts=['fair_dynamic_rec/__main__.py'] ,
     author="Masoud Mansoury",
     author_email="masoodmansoury@gmail.com",
     description=
     "The FairDynamicRec project aims to facilitate recommender system experiments in dynamic setting where system is operating over time.",
     long_description=long_description,
     long_description_content_type="text/markdown",
```

