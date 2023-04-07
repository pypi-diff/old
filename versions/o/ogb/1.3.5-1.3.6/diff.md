# Comparing `tmp/ogb-1.3.5.tar.gz` & `tmp/ogb-1.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/ogb-1.3.5.tar", last modified: Wed Nov  2 22:00:25 2022, max compression
+gzip compressed data, was "dist/ogb-1.3.6.tar", last modified: Fri Apr  7 05:58:40 2023, max compression
```

## Comparing `ogb-1.3.5.tar` & `ogb-1.3.6.tar`

### file list

```diff
@@ -1,64 +1,64 @@
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.367133 ogb-1.3.5/
--rw-r--r--   0 weihua     (502) staff       (20)      108 2019-12-13 08:19:32.000000 ogb-1.3.5/MANIFEST.in
--rw-r--r--   0 weihua     (502) staff       (20)     6918 2022-11-02 22:00:25.366836 ogb-1.3.5/PKG-INFO
--rw-r--r--   0 weihua     (502) staff       (20)     5348 2022-11-02 21:58:36.000000 ogb-1.3.5/README.md
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.335785 ogb-1.3.5/ogb/
--rw-r--r--   0 weihua     (502) staff       (20)       32 2020-02-25 21:31:46.000000 ogb-1.3.5/ogb/__init__.py
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.342341 ogb-1.3.5/ogb/graphproppred/
--rw-r--r--   0 weihua     (502) staff       (20)      302 2020-04-23 06:14:29.000000 ogb-1.3.5/ogb/graphproppred/__init__.py
--rw-r--r--   0 weihua     (502) staff       (20)     7790 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/graphproppred/dataset.py
--rw-r--r--   0 weihua     (502) staff       (20)     9731 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/graphproppred/dataset_dgl.py
--rw-r--r--   0 weihua     (502) staff       (20)     8431 2022-08-20 10:58:08.000000 ogb-1.3.5/ogb/graphproppred/dataset_pyg.py
--rw-r--r--   0 weihua     (502) staff       (20)    13182 2022-11-02 21:57:41.000000 ogb-1.3.5/ogb/graphproppred/evaluate.py
--rw-r--r--   0 weihua     (502) staff       (20)     4343 2021-03-01 04:51:36.000000 ogb-1.3.5/ogb/graphproppred/make_master_file.py
--rw-r--r--   0 weihua     (502) staff       (20)     2786 2021-03-01 04:52:01.000000 ogb-1.3.5/ogb/graphproppred/master.csv
--rw-r--r--   0 weihua     (502) staff       (20)     1669 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/graphproppred/mol_encoder.py
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.346721 ogb-1.3.5/ogb/io/
--rw-r--r--   0 weihua     (502) staff       (20)       38 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/io/__init__.py
--rw-r--r--   0 weihua     (502) staff       (20)     3240 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/io/read_graph_dgl.py
--rw-r--r--   0 weihua     (502) staff       (20)     3542 2022-02-23 05:12:57.000000 ogb-1.3.5/ogb/io/read_graph_pyg.py
--rw-r--r--   0 weihua     (502) staff       (20)    24084 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/io/read_graph_raw.py
--rw-r--r--   0 weihua     (502) staff       (20)    28886 2022-08-20 10:58:08.000000 ogb-1.3.5/ogb/io/save_dataset.py
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.352815 ogb-1.3.5/ogb/linkproppred/
--rw-r--r--   0 weihua     (502) staff       (20)      258 2020-04-23 06:14:29.000000 ogb-1.3.5/ogb/linkproppred/__init__.py
--rw-r--r--   0 weihua     (502) staff       (20)     7630 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/linkproppred/dataset.py
--rw-r--r--   0 weihua     (502) staff       (20)     7161 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/linkproppred/dataset_dgl.py
--rw-r--r--   0 weihua     (502) staff       (20)     7348 2022-08-20 10:58:08.000000 ogb-1.3.5/ogb/linkproppred/dataset_pyg.py
--rw-r--r--   0 weihua     (502) staff       (20)    15352 2022-11-02 21:57:41.000000 ogb-1.3.5/ogb/linkproppred/evaluate.py
--rw-r--r--   0 weihua     (502) staff       (20)     6451 2022-08-20 10:58:08.000000 ogb-1.3.5/ogb/linkproppred/make_master_file.py
--rw-r--r--   0 weihua     (502) staff       (20)     1231 2022-08-20 10:58:08.000000 ogb-1.3.5/ogb/linkproppred/master.csv
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.359431 ogb-1.3.5/ogb/lsc/
--rw-r--r--   0 weihua     (502) staff       (20)      722 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/__init__.py
--rw-r--r--   0 weihua     (502) staff       (20)     7115 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/mag240m.py
--rw-r--r--   0 weihua     (502) staff       (20)     8331 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/pcqm4m.py
--rw-r--r--   0 weihua     (502) staff       (20)     6141 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/pcqm4m_dgl.py
--rw-r--r--   0 weihua     (502) staff       (20)     4511 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/pcqm4m_pyg.py
--rw-r--r--   0 weihua     (502) staff       (20)     8673 2021-09-29 04:30:33.000000 ogb-1.3.5/ogb/lsc/pcqm4mv2.py
--rw-r--r--   0 weihua     (502) staff       (20)     6087 2022-02-23 05:12:57.000000 ogb-1.3.5/ogb/lsc/pcqm4mv2_dgl.py
--rw-r--r--   0 weihua     (502) staff       (20)     4448 2021-09-29 04:30:27.000000 ogb-1.3.5/ogb/lsc/pcqm4mv2_pyg.py
--rw-r--r--   0 weihua     (502) staff       (20)     1027 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/utils.py
--rw-r--r--   0 weihua     (502) staff       (20)    10389 2021-09-29 04:29:02.000000 ogb-1.3.5/ogb/lsc/wikikg90m.py
--rw-r--r--   0 weihua     (502) staff       (20)    10445 2022-11-02 21:57:41.000000 ogb-1.3.5/ogb/lsc/wikikg90mv2.py
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.363219 ogb-1.3.5/ogb/nodeproppred/
--rw-r--r--   0 weihua     (502) staff       (20)      258 2020-04-23 06:14:29.000000 ogb-1.3.5/ogb/nodeproppred/__init__.py
--rw-r--r--   0 weihua     (502) staff       (20)     8676 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/nodeproppred/dataset.py
--rw-r--r--   0 weihua     (502) staff       (20)    10270 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/nodeproppred/dataset_dgl.py
--rw-r--r--   0 weihua     (502) staff       (20)     9182 2022-08-20 10:58:08.000000 ogb-1.3.5/ogb/nodeproppred/dataset_pyg.py
--rw-r--r--   0 weihua     (502) staff       (20)     7042 2022-11-02 21:57:41.000000 ogb-1.3.5/ogb/nodeproppred/evaluate.py
--rw-r--r--   0 weihua     (502) staff       (20)     4402 2021-03-01 04:48:50.000000 ogb-1.3.5/ogb/nodeproppred/make_master_file.py
--rw-r--r--   0 weihua     (502) staff       (20)     1034 2021-03-01 04:49:00.000000 ogb-1.3.5/ogb/nodeproppred/master.csv
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.366006 ogb-1.3.5/ogb/utils/
--rw-r--r--   0 weihua     (502) staff       (20)       67 2020-12-29 17:38:59.000000 ogb-1.3.5/ogb/utils/__init__.py
--rw-r--r--   0 weihua     (502) staff       (20)     6795 2019-12-05 01:47:18.000000 ogb-1.3.5/ogb/utils/features.py
--rw-r--r--   0 weihua     (502) staff       (20)     1934 2020-12-29 17:38:59.000000 ogb-1.3.5/ogb/utils/mol.py
--rw-r--r--   0 weihua     (502) staff       (20)     1188 2020-09-12 18:51:57.000000 ogb-1.3.5/ogb/utils/torch_util.py
--rw-r--r--   0 weihua     (502) staff       (20)     2456 2020-03-15 02:25:47.000000 ogb-1.3.5/ogb/utils/url.py
--rw-r--r--   0 weihua     (502) staff       (20)      621 2022-11-02 21:58:10.000000 ogb-1.3.5/ogb/version.py
-drwxr-xr-x   0 weihua     (502) staff       (20)        0 2022-11-02 22:00:25.337299 ogb-1.3.5/ogb.egg-info/
--rw-r--r--   0 weihua     (502) staff       (20)     6918 2022-11-02 22:00:25.000000 ogb-1.3.5/ogb.egg-info/PKG-INFO
--rw-r--r--   0 weihua     (502) staff       (20)     1329 2022-11-02 22:00:25.000000 ogb-1.3.5/ogb.egg-info/SOURCES.txt
--rw-r--r--   0 weihua     (502) staff       (20)        1 2022-11-02 22:00:25.000000 ogb-1.3.5/ogb.egg-info/dependency_links.txt
--rw-r--r--   0 weihua     (502) staff       (20)      120 2022-11-02 22:00:25.000000 ogb-1.3.5/ogb.egg-info/requires.txt
--rw-r--r--   0 weihua     (502) staff       (20)        4 2022-11-02 22:00:25.000000 ogb-1.3.5/ogb.egg-info/top_level.txt
--rw-r--r--   0 weihua     (502) staff       (20)       38 2022-11-02 22:00:25.367216 ogb-1.3.5/setup.cfg
--rw-r--r--   0 weihua     (502) staff       (20)     1636 2021-03-21 22:33:58.000000 ogb-1.3.5/setup.py
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.697394 ogb-1.3.6/
+-rw-r--r--   0 weihua     (502) staff       (20)      108 2023-04-07 05:51:15.000000 ogb-1.3.6/MANIFEST.in
+-rw-r--r--   0 weihua     (502) staff       (20)     6918 2023-04-07 05:58:40.696922 ogb-1.3.6/PKG-INFO
+-rw-r--r--   0 weihua     (502) staff       (20)     5348 2023-04-07 05:57:06.000000 ogb-1.3.6/README.md
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.662126 ogb-1.3.6/ogb/
+-rw-r--r--   0 weihua     (502) staff       (20)       32 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/__init__.py
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.669908 ogb-1.3.6/ogb/graphproppred/
+-rw-r--r--   0 weihua     (502) staff       (20)      302 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/__init__.py
+-rw-r--r--   0 weihua     (502) staff       (20)     7811 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/dataset.py
+-rw-r--r--   0 weihua     (502) staff       (20)     9752 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/dataset_dgl.py
+-rw-r--r--   0 weihua     (502) staff       (20)     8452 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/dataset_pyg.py
+-rw-r--r--   0 weihua     (502) staff       (20)    13203 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/evaluate.py
+-rw-r--r--   0 weihua     (502) staff       (20)     4343 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/make_master_file.py
+-rw-r--r--   0 weihua     (502) staff       (20)     2786 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/master.csv
+-rw-r--r--   0 weihua     (502) staff       (20)     1669 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/graphproppred/mol_encoder.py
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.674595 ogb-1.3.6/ogb/io/
+-rw-r--r--   0 weihua     (502) staff       (20)       38 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/io/__init__.py
+-rw-r--r--   0 weihua     (502) staff       (20)     3240 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/io/read_graph_dgl.py
+-rw-r--r--   0 weihua     (502) staff       (20)     3542 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/io/read_graph_pyg.py
+-rw-r--r--   0 weihua     (502) staff       (20)    24084 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/io/read_graph_raw.py
+-rw-r--r--   0 weihua     (502) staff       (20)    28886 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/io/save_dataset.py
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.680395 ogb-1.3.6/ogb/linkproppred/
+-rw-r--r--   0 weihua     (502) staff       (20)      258 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/__init__.py
+-rw-r--r--   0 weihua     (502) staff       (20)     7651 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/dataset.py
+-rw-r--r--   0 weihua     (502) staff       (20)     7182 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/dataset_dgl.py
+-rw-r--r--   0 weihua     (502) staff       (20)     7369 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/dataset_pyg.py
+-rw-r--r--   0 weihua     (502) staff       (20)    15373 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/evaluate.py
+-rw-r--r--   0 weihua     (502) staff       (20)     6450 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/make_master_file.py
+-rw-r--r--   0 weihua     (502) staff       (20)     1231 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/linkproppred/master.csv
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.685711 ogb-1.3.6/ogb/lsc/
+-rw-r--r--   0 weihua     (502) staff       (20)      722 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/__init__.py
+-rw-r--r--   0 weihua     (502) staff       (20)     7115 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/mag240m.py
+-rw-r--r--   0 weihua     (502) staff       (20)     8331 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/pcqm4m.py
+-rw-r--r--   0 weihua     (502) staff       (20)     6141 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/pcqm4m_dgl.py
+-rw-r--r--   0 weihua     (502) staff       (20)     4511 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/pcqm4m_pyg.py
+-rw-r--r--   0 weihua     (502) staff       (20)     8673 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/pcqm4mv2.py
+-rw-r--r--   0 weihua     (502) staff       (20)     6087 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/pcqm4mv2_dgl.py
+-rw-r--r--   0 weihua     (502) staff       (20)     4448 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/pcqm4mv2_pyg.py
+-rw-r--r--   0 weihua     (502) staff       (20)     1027 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/utils.py
+-rw-r--r--   0 weihua     (502) staff       (20)    10389 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/wikikg90m.py
+-rw-r--r--   0 weihua     (502) staff       (20)    10445 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/lsc/wikikg90mv2.py
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.690334 ogb-1.3.6/ogb/nodeproppred/
+-rw-r--r--   0 weihua     (502) staff       (20)      258 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/__init__.py
+-rw-r--r--   0 weihua     (502) staff       (20)     8697 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/dataset.py
+-rw-r--r--   0 weihua     (502) staff       (20)    10291 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/dataset_dgl.py
+-rw-r--r--   0 weihua     (502) staff       (20)     9203 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/dataset_pyg.py
+-rw-r--r--   0 weihua     (502) staff       (20)     7063 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/evaluate.py
+-rw-r--r--   0 weihua     (502) staff       (20)     4402 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/make_master_file.py
+-rw-r--r--   0 weihua     (502) staff       (20)     1034 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/nodeproppred/master.csv
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.695812 ogb-1.3.6/ogb/utils/
+-rw-r--r--   0 weihua     (502) staff       (20)       67 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/utils/__init__.py
+-rw-r--r--   0 weihua     (502) staff       (20)     6818 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/utils/features.py
+-rw-r--r--   0 weihua     (502) staff       (20)     1934 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/utils/mol.py
+-rw-r--r--   0 weihua     (502) staff       (20)     1188 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/utils/torch_util.py
+-rw-r--r--   0 weihua     (502) staff       (20)     2456 2023-04-07 05:51:15.000000 ogb-1.3.6/ogb/utils/url.py
+-rw-r--r--   0 weihua     (502) staff       (20)      621 2023-04-07 05:56:42.000000 ogb-1.3.6/ogb/version.py
+drwxr-xr-x   0 weihua     (502) staff       (20)        0 2023-04-07 05:58:40.664128 ogb-1.3.6/ogb.egg-info/
+-rw-r--r--   0 weihua     (502) staff       (20)     6918 2023-04-07 05:58:40.000000 ogb-1.3.6/ogb.egg-info/PKG-INFO
+-rw-r--r--   0 weihua     (502) staff       (20)     1329 2023-04-07 05:58:40.000000 ogb-1.3.6/ogb.egg-info/SOURCES.txt
+-rw-r--r--   0 weihua     (502) staff       (20)        1 2023-04-07 05:58:40.000000 ogb-1.3.6/ogb.egg-info/dependency_links.txt
+-rw-r--r--   0 weihua     (502) staff       (20)      120 2023-04-07 05:58:40.000000 ogb-1.3.6/ogb.egg-info/requires.txt
+-rw-r--r--   0 weihua     (502) staff       (20)        4 2023-04-07 05:58:40.000000 ogb-1.3.6/ogb.egg-info/top_level.txt
+-rw-r--r--   0 weihua     (502) staff       (20)       38 2023-04-07 05:58:40.697671 ogb-1.3.6/setup.cfg
+-rw-r--r--   0 weihua     (502) staff       (20)     1636 2023-04-07 05:51:15.000000 ogb-1.3.6/setup.py
```

### Comparing `ogb-1.3.5/PKG-INFO` & `ogb-1.3.6/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ogb
-Version: 1.3.5
+Version: 1.3.6
 Summary: Open Graph Benchmark
 Home-page: https://github.com/snap-stanford/ogb
 Author: OGB Team
 Author-email: ogb@cs.stanford.edu
 License: MIT
 Description: <p align='center'>
           <img width='40%' src='https://snap-stanford.github.io/ogb-web/assets/img/OGB_rectangle.png' />
@@ -36,16 +36,16 @@
           <img width='70%' src='https://snap-stanford.github.io/ogb-web/assets/img/dataset_overview.png' />
         </p>
         
         OGB is an on-going effort, and we are planning to increase our coverage in the future.
         
         ## Installation
         You can install OGB using Python's package manager `pip`.
-        **If you have previously installed ogb, please make sure you update the version to 1.3.5.**
-        The release note is available [here](https://github.com/snap-stanford/ogb/releases/tag/1.3.5).
+        **If you have previously installed ogb, please make sure you update the version to 1.3.6.**
+        The release note is available [here](https://github.com/snap-stanford/ogb/releases/tag/1.3.6).
         
         #### Requirements
          - Python>=3.6
          - PyTorch>=1.6
          - DGL>=0.5.0 or torch-geometric>=2.0.2
          - Numpy>=1.16.0
          - pandas>=0.24.0
@@ -57,15 +57,15 @@
         The recommended way to install OGB is using Python's package manager pip:
         ```bash
         pip install ogb
         ```
         
         ```bash
         python -c "import ogb; print(ogb.__version__)"
-        # This should print "1.3.5". Otherwise, please update the version by
+        # This should print "1.3.6". Otherwise, please update the version by
         pip install -U ogb
         ```
         
         
         #### From source
         You can also install OGB from source. This is recommended if you want to contribute to OGB.
         ```bash
```

### Comparing `ogb-1.3.5/README.md` & `ogb-1.3.6/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -28,16 +28,16 @@
   <img width='70%' src='https://snap-stanford.github.io/ogb-web/assets/img/dataset_overview.png' />
 </p>
 
 OGB is an on-going effort, and we are planning to increase our coverage in the future.
 
 ## Installation
 You can install OGB using Python's package manager `pip`.
-**If you have previously installed ogb, please make sure you update the version to 1.3.5.**
-The release note is available [here](https://github.com/snap-stanford/ogb/releases/tag/1.3.5).
+**If you have previously installed ogb, please make sure you update the version to 1.3.6.**
+The release note is available [here](https://github.com/snap-stanford/ogb/releases/tag/1.3.6).
 
 #### Requirements
  - Python>=3.6
  - PyTorch>=1.6
  - DGL>=0.5.0 or torch-geometric>=2.0.2
  - Numpy>=1.16.0
  - pandas>=0.24.0
@@ -49,15 +49,15 @@
 The recommended way to install OGB is using Python's package manager pip:
 ```bash
 pip install ogb
 ```
 
 ```bash
 python -c "import ogb; print(ogb.__version__)"
-# This should print "1.3.5". Otherwise, please update the version by
+# This should print "1.3.6". Otherwise, please update the version by
 pip install -U ogb
 ```
 
 
 #### From source
 You can also install OGB from source. This is recommended if you want to contribute to OGB.
 ```bash
```

### Comparing `ogb-1.3.5/ogb/graphproppred/dataset.py` & `ogb-1.3.6/ogb/graphproppred/dataset.py`

 * *Files 1% similar despite different names*

```diff
@@ -19,15 +19,15 @@
         self.name = name ## original name, e.g., ogbg-hib
         
         if meta_dict is None:
             self.dir_name = '_'.join(name.split('-')) ## replace hyphen with underline, e.g., ogbg_hiv
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/graphproppred/dataset_dgl.py` & `ogb-1.3.6/ogb/graphproppred/dataset_dgl.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,15 +28,15 @@
             # If so, use that one.
             if osp.exists(osp.join(root, self.dir_name + '_dgl')):
                 self.dir_name = self.dir_name + '_dgl'
 
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/graphproppred/dataset_pyg.py` & `ogb-1.3.6/ogb/graphproppred/dataset_pyg.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,15 +28,15 @@
             # If so, use that one.
             if osp.exists(osp.join(root, self.dir_name + '_pyg')):
                 self.dir_name = self.dir_name + '_pyg'
 
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/graphproppred/evaluate.py` & `ogb-1.3.6/ogb/graphproppred/evaluate.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     torch = None
 
 ### Evaluator for graph classification
 class Evaluator:
     def __init__(self, name):
         self.name = name
 
-        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
         if not self.name in meta_info:
             print(self.name)
             error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
             error_mssg += 'Available datasets are as follows:\n'
             error_mssg += '\n'.join(meta_info.keys())
             raise ValueError(error_mssg)
```

### Comparing `ogb-1.3.5/ogb/graphproppred/make_master_file.py` & `ogb-1.3.6/ogb/graphproppred/make_master_file.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/graphproppred/master.csv` & `ogb-1.3.6/ogb/graphproppred/master.csv`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/graphproppred/mol_encoder.py` & `ogb-1.3.6/ogb/graphproppred/mol_encoder.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/io/read_graph_dgl.py` & `ogb-1.3.6/ogb/io/read_graph_dgl.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/io/read_graph_pyg.py` & `ogb-1.3.6/ogb/io/read_graph_pyg.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/io/read_graph_raw.py` & `ogb-1.3.6/ogb/io/read_graph_raw.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/io/save_dataset.py` & `ogb-1.3.6/ogb/io/save_dataset.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/linkproppred/dataset.py` & `ogb-1.3.6/ogb/linkproppred/dataset.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,15 +19,15 @@
         self.name = name ## original name, e.g., ogbl-ppa
         
         if meta_dict is None:
             self.dir_name = '_'.join(name.split('-')) ## replace hyphen with underline, e.g., ogbl_ppa
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/linkproppred/dataset_dgl.py` & `ogb-1.3.6/ogb/linkproppred/dataset_dgl.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,15 @@
             # If so, use that one.
             if osp.exists(osp.join(root, self.dir_name + '_dgl')):
                 self.dir_name = self.dir_name + '_dgl'
 
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/linkproppred/dataset_pyg.py` & `ogb-1.3.6/ogb/linkproppred/dataset_pyg.py`

 * *Files 0% similar despite different names*

```diff
@@ -27,15 +27,15 @@
             # If so, use that one.
             if osp.exists(osp.join(root, self.dir_name + '_pyg')):
                 self.dir_name = self.dir_name + '_pyg'
 
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/linkproppred/evaluate.py` & `ogb-1.3.6/ogb/linkproppred/evaluate.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     torch = None
 
 ### Evaluator for link property prediction
 class Evaluator:
     def __init__(self, name):
         self.name = name
 
-        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
         if not self.name in meta_info:
             print(self.name)
             error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
             error_mssg += 'Available datasets are as follows:\n'
             error_mssg += '\n'.join(meta_info.keys())
             raise ValueError(error_mssg)
 
@@ -241,20 +241,20 @@
             y_pred_pos is an array with shape (batch size, )
         '''
 
 
         if type_info == 'torch':
             # calculate ranks
             y_pred_pos = y_pred_pos.view(-1, 1)
-            # optimistic rank: "how many negatives have at least the positive score?"
+            # optimistic rank: "how many negatives have a larger score than the positive?"
             # ~> the positive is ranked first among those with equal score
-            optimistic_rank = (y_pred_neg >= y_pred_pos).sum(dim=1)
-            # pessimistic rank: "how many negatives have a larger score than the positive?"
+            optimistic_rank = (y_pred_neg > y_pred_pos).sum(dim=1)
+            # pessimistic rank: "how many negatives have at least the positive score?"
             # ~> the positive is ranked last among those with equal score
-            pessimistic_rank = (y_pred_neg > y_pred_pos).sum(dim=1)
+            pessimistic_rank = (y_pred_neg >= y_pred_pos).sum(dim=1)
             ranking_list = 0.5 * (optimistic_rank + pessimistic_rank) + 1
             hits1_list = (ranking_list <= 1).to(torch.float)
             hits3_list = (ranking_list <= 3).to(torch.float)
             hits10_list = (ranking_list <= 10).to(torch.float)
             mrr_list = 1./ranking_list.to(torch.float)
 
             return {'hits@1_list': hits1_list,
```

### Comparing `ogb-1.3.5/ogb/linkproppred/make_master_file.py` & `ogb-1.3.6/ogb/linkproppred/make_master_file.py`

 * *Files 0% similar despite different names*

```diff
@@ -108,15 +108,15 @@
 dataset_dict[name] = {'eval metric': 'rocauc', 'task type': 'link prediction'}
 dataset_dict[name]['download_name'] = 'vessel'
 dataset_dict[name]['version'] = 1
 dataset_dict[name]['url'] = 'http://snap.stanford.edu/ogb/data/linkproppred/'+dataset_dict[name]['download_name']+'.zip'
 ## For undirected grarph, we only store one directional information. This flag allows us to add inverse edge at pre-processing time
 dataset_dict[name]['add_inverse_edge'] = False 
 dataset_dict[name]['has_node_attr'] = True
-dataset_dict[name]['has_edge_attr'] = False
+dataset_dict[name]['has_edge_attr'] = True
 dataset_dict[name]['split'] = 'spatial'
 dataset_dict[name]['additional node files'] = 'None'
 dataset_dict[name]['additional edge files'] = 'None'
 dataset_dict[name]['is hetero'] = False
 dataset_dict[name]['binary'] = True
```

### Comparing `ogb-1.3.5/ogb/linkproppred/master.csv` & `ogb-1.3.6/ogb/linkproppred/master.csv`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/__init__.py` & `ogb-1.3.6/ogb/lsc/__init__.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/mag240m.py` & `ogb-1.3.6/ogb/lsc/mag240m.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/pcqm4m.py` & `ogb-1.3.6/ogb/lsc/pcqm4m.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/pcqm4m_dgl.py` & `ogb-1.3.6/ogb/lsc/pcqm4m_dgl.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/pcqm4m_pyg.py` & `ogb-1.3.6/ogb/lsc/pcqm4m_pyg.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/pcqm4mv2.py` & `ogb-1.3.6/ogb/lsc/pcqm4mv2.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/pcqm4mv2_dgl.py` & `ogb-1.3.6/ogb/lsc/pcqm4mv2_dgl.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/pcqm4mv2_pyg.py` & `ogb-1.3.6/ogb/lsc/pcqm4mv2_pyg.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/utils.py` & `ogb-1.3.6/ogb/lsc/utils.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/wikikg90m.py` & `ogb-1.3.6/ogb/lsc/wikikg90m.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/lsc/wikikg90mv2.py` & `ogb-1.3.6/ogb/lsc/wikikg90mv2.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/nodeproppred/dataset.py` & `ogb-1.3.6/ogb/nodeproppred/dataset.py`

 * *Files 1% similar despite different names*

```diff
@@ -22,15 +22,15 @@
         self.name = name ## original name, e.g., ogbn-proteins
         
         if meta_dict is None:
             self.dir_name = '_'.join(name.split('-')) ## replace hyphen with underline, e.g., ogbn_proteins
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/nodeproppred/dataset_dgl.py` & `ogb-1.3.6/ogb/nodeproppred/dataset_dgl.py`

 * *Files 0% similar despite different names*

```diff
@@ -28,15 +28,15 @@
             # If so, use that one.
             if osp.exists(osp.join(root, self.dir_name + '_dgl')):
                 self.dir_name = self.dir_name + '_dgl'
 
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/nodeproppred/dataset_pyg.py` & `ogb-1.3.6/ogb/nodeproppred/dataset_pyg.py`

 * *Files 2% similar despite different names*

```diff
@@ -28,15 +28,15 @@
             # If so, use that one.
             if osp.exists(osp.join(root, self.dir_name + '_pyg')):
                 self.dir_name = self.dir_name + '_pyg'
 
             self.original_root = root
             self.root = osp.join(root, self.dir_name)
             
-            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+            master = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
             if not self.name in master:
                 error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
                 error_mssg += 'Available datasets are as follows:\n'
                 error_mssg += '\n'.join(master.keys())
                 raise ValueError(error_mssg)
             self.meta_info = master[self.name]
```

### Comparing `ogb-1.3.5/ogb/nodeproppred/evaluate.py` & `ogb-1.3.6/ogb/nodeproppred/evaluate.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     torch = None
 
 ### Evaluator for node property prediction
 class Evaluator:
     def __init__(self, name):
         self.name = name
 
-        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col = 0)
+        meta_info = pd.read_csv(os.path.join(os.path.dirname(__file__), 'master.csv'), index_col=0, keep_default_na=False)
         if not self.name in meta_info:
             print(self.name)
             error_mssg = 'Invalid dataset name {}.\n'.format(self.name)
             error_mssg += 'Available datasets are as follows:\n'
             error_mssg += '\n'.join(meta_info.keys())
             raise ValueError(error_mssg)
```

### Comparing `ogb-1.3.5/ogb/nodeproppred/make_master_file.py` & `ogb-1.3.6/ogb/nodeproppred/make_master_file.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/nodeproppred/master.csv` & `ogb-1.3.6/ogb/nodeproppred/master.csv`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/utils/features.py` & `ogb-1.3.6/ogb/utils/features.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 # allowable multiple choice node and edge features 
 allowable_features = {
     'possible_atomic_num_list' : list(range(1, 119)) + ['misc'],
     'possible_chirality_list' : [
         'CHI_UNSPECIFIED',
         'CHI_TETRAHEDRAL_CW',
         'CHI_TETRAHEDRAL_CCW',
-        'CHI_OTHER'
+        'CHI_OTHER',
+        'misc'
     ],
     'possible_degree_list' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'misc'],
     'possible_formal_charge_list' : [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 'misc'],
     'possible_numH_list' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 'misc'],
     'possible_number_radical_e_list': [0, 1, 2, 3, 4, 'misc'],
     'possible_hybridization_list' : [
         'SP', 'SP2', 'SP3', 'SP3D', 'SP3D2', 'misc'
@@ -53,15 +54,15 @@
     """
     Converts rdkit atom object to feature list of indices
     :param mol: rdkit atom object
     :return: list
     """
     atom_feature = [
             safe_index(allowable_features['possible_atomic_num_list'], atom.GetAtomicNum()),
-            allowable_features['possible_chirality_list'].index(str(atom.GetChiralTag())),
+            safe_index(allowable_features['possible_chirality_list'], str(atom.GetChiralTag())),
             safe_index(allowable_features['possible_degree_list'], atom.GetTotalDegree()),
             safe_index(allowable_features['possible_formal_charge_list'], atom.GetFormalCharge()),
             safe_index(allowable_features['possible_numH_list'], atom.GetTotalNumHs()),
             safe_index(allowable_features['possible_number_radical_e_list'], atom.GetNumRadicalElectrons()),
             safe_index(allowable_features['possible_hybridization_list'], str(atom.GetHybridization())),
             allowable_features['possible_is_aromatic_list'].index(atom.GetIsAromatic()),
             allowable_features['possible_is_in_ring_list'].index(atom.IsInRing()),
@@ -159,8 +160,8 @@
     }
 
     return feature_dict
 # # uses same bond as bond_to_feature_vector test
 # bond_feature_dict = bond_feature_vector_to_dict(bond_feature)
 # assert bond_feature_dict['bond_type'] == 'DOUBLE'
 # assert bond_feature_dict['bond_stereo'] == 'STEREOE'
-# assert bond_feature_dict['is_conjugated'] == False
+# assert bond_feature_dict['is_conjugated'] == False
```

### Comparing `ogb-1.3.5/ogb/utils/mol.py` & `ogb-1.3.6/ogb/utils/mol.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/utils/torch_util.py` & `ogb-1.3.6/ogb/utils/torch_util.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/utils/url.py` & `ogb-1.3.6/ogb/utils/url.py`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/ogb/version.py` & `ogb-1.3.6/ogb/version.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import os
 import logging
 from threading import Thread
 
-__version__ = '1.3.5'
+__version__ = '1.3.6'
 
 try:
     os.environ['OUTDATED_IGNORE'] = '1'
     from outdated import check_outdated  # noqa
 except ImportError:
     check_outdated = None
```

### Comparing `ogb-1.3.5/ogb.egg-info/PKG-INFO` & `ogb-1.3.6/ogb.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ogb
-Version: 1.3.5
+Version: 1.3.6
 Summary: Open Graph Benchmark
 Home-page: https://github.com/snap-stanford/ogb
 Author: OGB Team
 Author-email: ogb@cs.stanford.edu
 License: MIT
 Description: <p align='center'>
           <img width='40%' src='https://snap-stanford.github.io/ogb-web/assets/img/OGB_rectangle.png' />
@@ -36,16 +36,16 @@
           <img width='70%' src='https://snap-stanford.github.io/ogb-web/assets/img/dataset_overview.png' />
         </p>
         
         OGB is an on-going effort, and we are planning to increase our coverage in the future.
         
         ## Installation
         You can install OGB using Python's package manager `pip`.
-        **If you have previously installed ogb, please make sure you update the version to 1.3.5.**
-        The release note is available [here](https://github.com/snap-stanford/ogb/releases/tag/1.3.5).
+        **If you have previously installed ogb, please make sure you update the version to 1.3.6.**
+        The release note is available [here](https://github.com/snap-stanford/ogb/releases/tag/1.3.6).
         
         #### Requirements
          - Python>=3.6
          - PyTorch>=1.6
          - DGL>=0.5.0 or torch-geometric>=2.0.2
          - Numpy>=1.16.0
          - pandas>=0.24.0
@@ -57,15 +57,15 @@
         The recommended way to install OGB is using Python's package manager pip:
         ```bash
         pip install ogb
         ```
         
         ```bash
         python -c "import ogb; print(ogb.__version__)"
-        # This should print "1.3.5". Otherwise, please update the version by
+        # This should print "1.3.6". Otherwise, please update the version by
         pip install -U ogb
         ```
         
         
         #### From source
         You can also install OGB from source. This is recommended if you want to contribute to OGB.
         ```bash
```

### Comparing `ogb-1.3.5/ogb.egg-info/SOURCES.txt` & `ogb-1.3.6/ogb.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `ogb-1.3.5/setup.py` & `ogb-1.3.6/setup.py`

 * *Files identical despite different names*

