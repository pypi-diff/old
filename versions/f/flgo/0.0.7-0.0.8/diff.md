# Comparing `tmp/flgo-0.0.7.tar.gz` & `tmp/flgo-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flgo-0.0.7.tar", last modified: Sun Apr  2 03:16:18 2023, max compression
+gzip compressed data, was "flgo-0.0.8.tar", last modified: Thu Apr  6 17:47:50 2023, max compression
```

## Comparing `flgo-0.0.7.tar` & `flgo-0.0.8.tar`

### file list

```diff
@@ -1,189 +1,190 @@
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1091 2023-03-21 13:46:37.000000 flgo-0.0.7/LICENSE
--rw-rw-r--   0 wz        (1001) wz        (1001)      486 2023-04-02 03:16:18.885519 flgo-0.0.7/PKG-INFO
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-03-21 13:46:37.000000 flgo-0.0.7/README.md
--rw-rw-r--   0 wz        (1001) wz        (1001)      591 2023-04-02 03:16:00.000000 flgo-0.0.7/pyproject.toml
--rw-rw-r--   0 wz        (1001) wz        (1001)       38 2023-04-02 03:16:18.885519 flgo-0.0.7/setup.cfg
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.873520 flgo-0.0.7/src/
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.877519 flgo-0.0.7/src/flgo/
--rw-rw-r--   0 wz        (1001) wz        (1001)      536 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.877519 flgo-0.0.7/src/flgo/algorithm/
--rw-rw-r--   0 wz        (1001) wz        (1001)     3744 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/TiFL.py
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     3318 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/afl.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     2208 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedasync.py
--rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedavg.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    27278 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedbase.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     2554 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedbuff.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     3381 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedfv.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     2690 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedmgda+.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1226 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/fedprox.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1800 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/mifa.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1485 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/powerofchoice.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1035 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/qfedavg.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     3252 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/scaffold.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    11465 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/algorithm/vflbase.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/
--rw-rw-r--   0 wz        (1001) wz        (1001)       41 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cifar100_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1526 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cifar100_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      845 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cifar100_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cifar100_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      957 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cifar100_classification/model/cnn.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     5298 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cifar100_classification/model/resnet18.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cifar10_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1690 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cifar10_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      829 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cifar10_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cifar10_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      895 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cifar10_classification/model/cnn.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      897 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cifar10_classification/model/mlp.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/
--rw-rw-r--   0 wz        (1001) wz        (1001)       82 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      748 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      825 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/model/GCN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      807 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      727 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/model/GCN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/
--rw-rw-r--   0 wz        (1001) wz        (1001)       78 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      736 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      825 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/model/GCN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)       82 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      794 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      727 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/GCN.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      730 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/GraphSAGE_1.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     4070 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/GraphSage.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/emnist_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)      195 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/emnist_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1148 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/benchmark/emnist_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/emnist_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1037 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/emnist_classification/model/cnn.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      709 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/emnist_classification/model/mlp.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      748 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1258 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/model/GCN.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1581 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/model/GIN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/fashion_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)      194 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/fashion_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      818 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/fashion_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/fashion_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      578 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/fashion_classification/model/lr.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/femnist_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/femnist_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     5750 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/femnist_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/leaf_reddit/
--rw-rw-r--   0 wz        (1001) wz        (1001)       87 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/leaf_reddit/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    10084 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/leaf_reddit/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/leaf_reddit/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      980 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/leaf_reddit/model/stackedlstm.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/leaf_sent140/
--rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/leaf_sent140/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    11333 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/leaf_sent140/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/leaf_sent140/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1278 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/leaf_sent140/model/stackedlstm.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/mnist_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1668 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/mnist_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      809 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/mnist_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/mnist_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1031 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/mnist_classification/model/cnn.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      801 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/mnist_classification/model/mlp.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)       84 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      742 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1260 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/model/GCN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/
--rw-rw-r--   0 wz        (1001) wz        (1001)       80 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      742 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      824 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/model/GCN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)       84 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      801 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      726 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/model/GCN.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)      100 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    15279 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.881519 flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     2169 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/model/stackedlstm.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/svhn_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1690 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/svhn_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     2438 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/svhn_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/svhn_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      895 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/svhn_classification/model/cnn.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      897 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/svhn_classification/model/mlp.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/synthetic_regression/
--rw-rw-r--   0 wz        (1001) wz        (1001)       76 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/synthetic_regression/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     3927 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/synthetic_regression/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/synthetic_regression/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)      555 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/synthetic_regression/model/lr.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/
--rw-rw-r--   0 wz        (1001) wz        (1001)      108 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    12909 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/base.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/centralize/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/centralize/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/horizontal/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/horizontal/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     7537 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/horizontal/image_classification.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/vertical/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/cv/vertical/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     5613 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/graph_classification.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     7709 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/link_prediction.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     7346 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/node_classification.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/nlp/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/nlp/__init__.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/nlp/horizontal/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/nlp/horizontal/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/nlp/horizontal/text_prediction.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    19844 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/partition.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/toolkits/tabular/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/tabular/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     2085 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/toolkits/visualization.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/
--rw-rw-r--   0 wz        (1001) wz        (1001)       87 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     7202 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/core.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/model/
--rw-rw-r--   0 wz        (1001) wz        (1001)     1162 2023-04-02 03:14:39.000000 flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/model/mlp.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/experiment/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/experiment/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    20239 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/experiment/analyzer.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     4408 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/experiment/device_scheduler.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/experiment/logger/
--rw-rw-r--   0 wz        (1001) wz        (1001)    87090 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/experiment/logger/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    36840 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/experiment/logger/config.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    59394 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/experiment/logger/handlers.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1485 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/experiment/logger/simple_logger.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1077 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/experiment/logger/tune_logger.py
--rw-rw-r--   0 wz        (1001) wz        (1001)      959 2023-04-02 03:14:38.000000 flgo-0.0.7/src/flgo/experiment/logger/vertical_logger.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/system_simulator/
--rw-rw-r--   0 wz        (1001) wz        (1001)     3016 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/system_simulator/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    18523 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/system_simulator/base.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    15544 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/system_simulator/default_simulator.py
--rw-rw-r--   0 wz        (1001) wz        (1001)     1037 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/system_simulator/my_simulator.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    17529 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/system_simulator/phone_simulator.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/src/flgo/utils/
--rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/utils/__init__.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    39657 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/utils/fflow.py
--rw-rw-r--   0 wz        (1001) wz        (1001)    16169 2023-04-02 03:14:37.000000 flgo-0.0.7/src/flgo/utils/fmodule.py
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.877519 flgo-0.0.7/src/flgo.egg-info/
--rw-rw-r--   0 wz        (1001) wz        (1001)      486 2023-04-02 03:16:18.000000 flgo-0.0.7/src/flgo.egg-info/PKG-INFO
--rw-rw-r--   0 wz        (1001) wz        (1001)     5877 2023-04-02 03:16:18.000000 flgo-0.0.7/src/flgo.egg-info/SOURCES.txt
--rw-rw-r--   0 wz        (1001) wz        (1001)        1 2023-04-02 03:16:18.000000 flgo-0.0.7/src/flgo.egg-info/dependency_links.txt
--rw-rw-r--   0 wz        (1001) wz        (1001)        5 2023-04-02 03:16:18.000000 flgo-0.0.7/src/flgo.egg-info/top_level.txt
-drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-02 03:16:18.885519 flgo-0.0.7/tests/
--rw-rw-r--   0 wz        (1001) wz        (1001)      947 2023-03-21 13:46:37.000000 flgo-0.0.7/tests/test.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1091 2023-03-21 13:46:37.000000 flgo-0.0.8/LICENSE
+-rw-rw-r--   0 wz        (1001) wz        (1001)      485 2023-04-06 17:47:49.993871 flgo-0.0.8/PKG-INFO
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-03-21 13:46:37.000000 flgo-0.0.8/README.md
+-rw-rw-r--   0 wz        (1001) wz        (1001)      590 2023-04-06 17:47:34.000000 flgo-0.0.8/pyproject.toml
+-rw-rw-r--   0 wz        (1001) wz        (1001)       38 2023-04-06 17:47:49.993871 flgo-0.0.8/setup.cfg
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.981871 flgo-0.0.8/src/
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.985871 flgo-0.0.8/src/flgo/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      635 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/algorithm/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     3749 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/TiFL.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     3337 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/afl.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2383 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedasync.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedavg.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    31560 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedbase.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2554 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedbuff.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2258 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedfa.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     3381 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedfv.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2690 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedmgda+.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1364 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/fedprox.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1800 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/mifa.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1478 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/powerofchoice.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1282 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/qfedavg.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     3396 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/scaffold.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    11512 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/algorithm/vflbase.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1920 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/benchmark/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    15858 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/benchmark/base.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cifar100_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1526 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar100_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      845 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar100_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cifar100_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      957 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar100_classification/model/cnn.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     5298 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar100_classification/model/resnet18.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cifar10_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1690 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar10_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      829 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar10_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cifar10_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      895 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar10_classification/model/cnn.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      897 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cifar10_classification/model/mlp.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       82 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      748 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      825 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/model/GCN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      807 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      727 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/model/GCN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       78 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      736 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      825 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/model/GCN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       82 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      794 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      727 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/GCN.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      730 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/GraphSAGE_1.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     4070 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/GraphSage.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/emnist_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      195 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/emnist_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1205 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/emnist_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/emnist_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1037 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/emnist_classification/model/cnn.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      709 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/emnist_classification/model/mlp.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      748 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1258 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/model/GCN.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1581 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/model/GIN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/fashion_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      194 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/fashion_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      818 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/fashion_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/fashion_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      578 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/fashion_classification/model/lr.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/femnist_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/femnist_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     5751 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/femnist_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/leaf_reddit/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       87 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/leaf_reddit/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    10075 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/leaf_reddit/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/leaf_reddit/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      980 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/leaf_reddit/model/stackedlstm.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/leaf_sent140/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       86 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/leaf_sent140/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    11324 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/leaf_sent140/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/leaf_sent140/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1278 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/leaf_sent140/model/stackedlstm.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/mnist_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1668 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/mnist_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      809 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/mnist_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/mnist_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1031 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/mnist_classification/model/cnn.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      801 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/mnist_classification/model/mlp.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       84 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      742 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1260 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/model/GCN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       80 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      742 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      824 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/model/GCN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       84 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      801 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      726 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/model/GCN.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      100 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    15270 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.989871 flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2169 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/model/stackedlstm.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/svhn_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      195 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/svhn_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1222 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/svhn_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/svhn_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      895 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/svhn_classification/model/cnn.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      897 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/svhn_classification/model/mlp.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/synthetic_regression/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       76 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/synthetic_regression/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     3918 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/synthetic_regression/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/synthetic_regression/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      555 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/synthetic_regression/model/lr.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      150 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/centralize/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/centralize/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/horizontal/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/horizontal/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     9110 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/horizontal/image_classification.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/vertical/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/cv/vertical/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     5245 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/graph_classification.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     7700 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/link_prediction.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     7337 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/node_classification.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/nlp/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/nlp/__init__.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/nlp/horizontal/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/nlp/horizontal/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/nlp/horizontal/text_prediction.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    20144 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/partition.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/toolkits/tabular/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/tabular/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2465 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/toolkits/visualization.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       87 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     7193 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/core.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/model/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1162 2023-04-06 17:45:37.000000 flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/model/mlp.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/experiment/
+-rw-rw-r--   0 wz        (1001) wz        (1001)       62 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/experiment/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    26973 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/experiment/analyzer.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     6628 2023-04-06 17:45:35.000000 flgo-0.0.8/src/flgo/experiment/device_scheduler.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/experiment/logger/
+-rw-rw-r--   0 wz        (1001) wz        (1001)    87170 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/experiment/logger/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    36840 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/experiment/logger/config.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    59394 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/experiment/logger/handlers.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1587 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/experiment/logger/simple_logger.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)      967 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/experiment/logger/tune_logger.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1023 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/experiment/logger/vertical_logger.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/simulator/
+-rw-rw-r--   0 wz        (1001) wz        (1001)     2981 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/simulator/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    23835 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/simulator/base.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    16615 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/simulator/default_simulator.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)     1030 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/simulator/my_simulator.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    17522 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/simulator/phone_simulator.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/src/flgo/utils/
+-rw-rw-r--   0 wz        (1001) wz        (1001)        0 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/utils/__init__.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    40666 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/utils/fflow.py
+-rw-rw-r--   0 wz        (1001) wz        (1001)    28136 2023-04-06 17:45:36.000000 flgo-0.0.8/src/flgo/utils/fmodule.py
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.985871 flgo-0.0.8/src/flgo.egg-info/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      485 2023-04-06 17:47:49.000000 flgo-0.0.8/src/flgo.egg-info/PKG-INFO
+-rw-rw-r--   0 wz        (1001) wz        (1001)     5861 2023-04-06 17:47:49.000000 flgo-0.0.8/src/flgo.egg-info/SOURCES.txt
+-rw-rw-r--   0 wz        (1001) wz        (1001)        1 2023-04-06 17:47:49.000000 flgo-0.0.8/src/flgo.egg-info/dependency_links.txt
+-rw-rw-r--   0 wz        (1001) wz        (1001)        5 2023-04-06 17:47:49.000000 flgo-0.0.8/src/flgo.egg-info/top_level.txt
+drwxrwxr-x   0 wz        (1001) wz        (1001)        0 2023-04-06 17:47:49.993871 flgo-0.0.8/tests/
+-rw-rw-r--   0 wz        (1001) wz        (1001)      947 2023-03-21 13:46:37.000000 flgo-0.0.8/tests/test.py
```

### Comparing `flgo-0.0.7/LICENSE` & `flgo-0.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/__init__.py` & `flgo-0.0.8/src/flgo/__init__.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,13 +1,16 @@
 from .utils.fflow import init, gen_task_by_config, gen_task_by_para, tune, run_in_parallel, multi_init_and_run
 
 gen_task = gen_task_by_config
 communicator = None
 
 class VirtualCommunicator:
+    """
+    Communicator that simulates the communication phase between any two objects
+    """
     def __init__(self, objects):
         self.objects_map = {obj.id:obj for obj in objects}
         self.objects = objects
 
     def request(self, source, target, package):
         # send package to the target object with `package` and `mtype`, and then listen from it
         return self.objects_map[target].message_handler(package)
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/TiFL.py` & `flgo-0.0.8/src/flgo/algorithm/TiFL.py`

 * *Files 1% similar despite different names*

```diff
@@ -47,15 +47,15 @@
         if self.tiers is None: self.tiers =  self.profiling_and_tiering()
         if (self.current_round-1)%self.I==0 and self.current_round-1>=self.I:
             self.change_probs()
         self.selected_clients = self.sample()
         models = self.communicate(self.selected_clients)['model']
         self.model = self.aggregate(models)
         # update accuracy of each tier
-        valid_accs = np.array(self.global_test('valid')['accuracy'])
+        valid_accs = np.array(self.global_test(flag='valid')['accuracy'])
         for t in self.tiers:
             self.tiers[t]['accuracy'] = (valid_accs[self.tiers[t]['clients']]).mean()
         return
 
     def sample(self):
         probs = [self.tiers[t]['prob'] for t in self.tiers.keys()]
         while True:
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/afl.py` & `flgo-0.0.8/src/flgo/algorithm/afl.py`

 * *Files 9% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 
 import flgo.utils.fmodule as fmodule
 from flgo.algorithm.fedbase import BasicServer, BasicClient
 import numpy as np
 import copy
 import collections
 
+
 class Server(BasicServer):
     def initialize(self, *args, **kwargs):
         self.init_algo_para({'learning_rate_lambda': 0.01})
         self.dynamic_lambdas = np.ones(self.num_clients) * 1.0 / self.num_clients
         self.learning_rate = self.option['learning_rate']
         self.result_model = copy.deepcopy(self.model)
 
@@ -60,25 +61,27 @@
             client_metrics = c.test(self.result_model, flag)
             for met_name, met_val in client_metrics.items():
                 all_metrics[met_name].append(met_val)
         return all_metrics
 
     def test(self, model=None, flag='test'):
         if model == None: model = self.result_model
-        data = self.test_data if flag=='test' else self.valid_data
-        if data is None: return {}
+        data = self.test_data if flag == 'test' else self.valid_data
+        if data is None:
+            return {}
         else:
-            return self.calculator.test(model, self.test_data, batch_size = self.option['test_batch_size'])
+            return self.calculator.test(model, self.test_data, batch_size=self.option['test_batch_size'])
+
 
 class Client(BasicClient):
     def reply(self, svr_pkg):
         model = self.unpack(svr_pkg)
         train_loss = self.test(model, 'train')['loss']
         self.train(model)
         cpkg = self.pack(model, train_loss)
         return cpkg
 
     def pack(self, model, loss):
         return {
             "model": model,
             "loss": loss,
-        }
+        }
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/fedasync.py` & `flgo-0.0.8/src/flgo/algorithm/fedasync.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,34 +1,42 @@
 """This is a non-official implementation of 'Asynchronous Federated Optimization' (http://arxiv.org/abs/1903.03934). """
 from .fedbase import BasicServer
 from .fedbase import BasicClient as Client
 
+
 class Server(BasicServer):
     def initialize(self):
-        self.init_algo_para({'period':20, 'alpha': 0.6, 'mu':0.005, 'flag':'constant', 'hinge_a':10, 'hinge_b':6, 'poly_a':0.5})
+        self.init_algo_para(
+            {'period': 20, 'alpha': 0.6, 'mu': 0.005, 'flag': 'constant', 'hinge_a': 10, 'hinge_b': 6, 'poly_a': 0.5})
         self.tolerance_for_latency = 1000
         self.client_taus = [0 for _ in self.clients]
 
     def iterate(self):
         # Scheduler periodically triggers the idle clients to locally train the model
-        self.selected_clients = self.sample() if (self.gv.clock.current_time%self.period)==0 or self.gv.clock.current_time==1 else []
-        if len(self.selected_clients)>0:
-            self.gv.logger.info('Select clients {} at time {}'.format(self.selected_clients, self.gv.clock.current_time))
+        if (self.gv.clock.current_time % self.period) == 0 or self.gv.clock.current_time == 1:
+            self.selected_clients = self.sample()
+        else:
+            self.selected_clients = []
+        if len(self.selected_clients) > 0:
+            self.gv.logger.info(
+                'Select clients {} at time {}'.format(self.selected_clients, self.gv.clock.current_time))
         # Record the timestamp of the selected clients
         for cid in self.selected_clients: self.client_taus[cid] = self.current_round
         # Check the currently received models
         res = self.communicate(self.selected_clients, asynchronous=True)
         received_models = res['model']
         received_client_ids = res['__cid']
         if len(received_models) > 0:
-            self.gv.logger.info('Receive new models from clients {} at time {}'.format(received_client_ids, self.gv.clock.current_time))
+            self.gv.logger.info(
+                'Receive new models from clients {} at time {}'.format(received_client_ids, self.gv.clock.current_time))
             # averaging the simultaneously received models at the current moment
             taus = [self.client_taus[cid] for cid in received_client_ids]
             alpha_ts = [self.alpha * self.s(self.current_round - tau) for tau in taus]
-            currently_updated_models = [(1-alpha_t)*self.model+alpha_t*model_k for alpha_t, model_k in zip(alpha_ts, received_models) ]
+            currently_updated_models = [(1 - alpha_t) * self.model + alpha_t * model_k for alpha_t, model_k in
+                                        zip(alpha_ts, received_models)]
             self.model = self.aggregate(currently_updated_models)
         return len(received_models) > 0
 
     def s(self, delta_tau):
         if self.flag == 'constant':
             return 1
         elif self.flag == 'hinge':
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/fedbase.py` & `flgo-0.0.8/src/flgo/algorithm/fedbase.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,98 +1,163 @@
-import numpy as np
-from flgo.utils import fmodule
-import copy
-import flgo.system_simulator.base as ss
 import math
+import copy
 import collections
-import torch.multiprocessing as mp
+
 import torch
+import torch.multiprocessing as mp
+import numpy as np
+
+from flgo.utils import fmodule
+import flgo.simulator.base as ss
+
 
+# The BasicParty
 class BasicParty:
     def __init__(self, *args, **kwargs):
-        self.actions = {}
-        self.id = None
+        self.actions = {}  # the message-action map that is used to customize the communication process
+        self.id = None  # the id for communicating
+        self._object_map = collections.defaultdict(lambda:None) # mapping objects according to their ids
 
     def register_action_to_mtype(self, action_name: str, mtype):
-        """
-        Register an existing instance method as the action to the message type.
+        r"""
+        Register an existing method as the action corresponding to the message type.
+
         Args:
             action_name: the name of the instance method
             mtype: the message type
         """
         if action_name not in self.__dict__.keys():
             raise NotImplementedError("There is no method named `{}` in the class instance.".format(action_name))
         self.actions[mtype] = self.__dict__[action_name]
 
     def message_handler(self, package):
-        """
+        r"""
         Handling the received message by excuting the corresponding action.
+
         Args:
-            package: the package received from other parties (i.e. the content of the message)
-            mtype: the message type
+            package (dict): the package received from other parties (i.e. the content of the message)
+
         Returns:
             action_reult
         """
         try:
             mtype = package['__mtype__']
         except:
             raise KeyError("__mtype__ must be a key of the package")
         if mtype not in self.actions.keys():
             raise NotImplementedError("There is no action corresponding to message type {}.".format(mtype))
         return self.actions[mtype](package)
 
-    def set_data(self, data, flag='train') -> None:
-        setattr(self, flag+'_data', data)
-        if flag=='train':
+    def set_data(self, data, flag:str='train') -> None:
+        r"""
+        Set self's attibute 'xxx_data' to be data where xxx is the flag. For example,
+        after calling self.set_data([1,2,3], 'test'), self.test_data will be [1,2,3].
+        Particularly, If the flag is 'train', the batchsize and the num_steps will be
+        reset.
+
+        Args:
+            data: anything
+            flag (str): the name of the data
+        """
+        setattr(self, flag + '_data', data)
+        if flag == 'train':
             self.datavol = len(data)
             if hasattr(self, 'batch_size'):
                 # reset batch_size
-                if self.batch_size<0: self.batch_size = len(self.train_data)
-                elif self.batch_size>=1: self.batch_size = int(self.batch_size)
-                else: self.batch_size = int(self.datavol * self.batch_size)
+                if self.batch_size < 0:
+                    self.batch_size = len(self.train_data)
+                elif self.batch_size >= 1:
+                    self.batch_size = int(self.batch_size)
+                else:
+                    self.batch_size = int(self.datavol * self.batch_size)
             # reset num_steps
             if hasattr(self, 'num_steps') and hasattr(self, 'num_epochs'):
                 if self.num_steps > 0:
-                    self.num_epochs = 1.0 * self.num_steps/(math.ceil(self.datavol / self.batch_size))
+                    self.num_epochs = 1.0 * self.num_steps / (math.ceil(self.datavol / self.batch_size))
                 else:
                     self.num_steps = self.num_epochs * math.ceil(self.datavol / self.batch_size)
 
-    def register_parties(self, parties):
-        # set the accessible parties
-        self.parties = parties
+    def set_model(self, model, model_name: str = 'model'):
+        r"""
+        Set self's attibute 'model_name' to be model. For example,
+        after calling self.set_model(my_model, 'model'), self.model will be my_model.
+        """
+        # set self.__dict__[model_name] = model
+        setattr(self, model_name, model)
+
+    def set_id(self, id=None):
+        r"""
+        Set self's attibute 'id' to be id where self.id = id
+        """
+        if id is not None:
+            self.id = id
+
+    def register_objects(self, parties:list, parties_name='parties'):
+        r"""
+        Set self's attribute party_names (e.g. parties as default) to be parties if
+        self has no attribute named party_names. Otherwise, parties will be extend to
+        the attribute party_names of self.
+        
+        Args:
+            parties (list): a list of objects
+            parties_name (str): the name of attribute to store parties
+
+        Example::
+            >>> a = BasicParty()
+            >>> b = BasicParty()
+            >>> c = BasicParty()
+            >>> a.register_objects([b, c], 'parties')
+            >>> a.parties # will be [b,c]
+            >>> d = BasicParty()
+            >>> a.register_objects([d], 'parties')
+            >>> a.parties # will be [b,c,d]
+        """
+        if type(parties) is not list:
+            raise TypeError("parties should be a list")
+        if not hasattr(self, parties_name):
+            setattr(self, parties_name, parties)
+        else:
+            tmp = getattr(self, parties_name)
+            if tmp is None: tmp = []
+            elif type(tmp) is not list: tmp = list(tmp)
+            tmp.extend(parties)
+            setattr(self, parties_name, tmp)
+        self._object_map.update({p.id:p for p in parties if p.id is not None})
 
     def communicate_with(self, target_id, package={}):
-        """
-        Pack the information that is needed for client_id to improve the global model
+        r"""
+        Send the package to target object according to its id, and receive the response from it
+
         Args:
-            client_id (int): the id of the client to communicate with
-            package (dict): the package to be sended to the client
-            mtype (anytype): the type of the message that is used to decide the action of the client
+            target_id (int): the id of the object to communicate with
+            package (dict): the package to be sended to the object
         Returns:
-            client_package (dict): the reply from the client and will be 'None' if losing connection
+            client_package (dict): the reply from the target object and will be 'None' if losing connection
         """
         return self.gv.communicator.request(self.id, target_id, package)
 
     def initialize(self, *args, **kwargs):
+        r"""API for customizing the initializing process of the object"""
         return
 
 class BasicServer(BasicParty):
     def __init__(self, option={}):
         super().__init__()
-        self.test_data=None
+        self.test_data = None
         self.valid_data = None
         self.train_data = None
         self.model = None
+        self.clients = []
         # basic configuration
         self.task = option['task']
         self.eval_interval = option['eval_interval']
-        self.num_parallels= option['num_parallels']
+        self.num_parallels = option['num_parallels']
         # server calculator
         self.device = self.gv.apply_for_device() if not option['server_with_cpu'] else torch.device('cpu')
-        self.calculator = self.gv.TaskCalculator(self.device, optimizer_name = option['optimizer'])
+        self.calculator = self.gv.TaskCalculator(self.device, optimizer_name=option['optimizer'])
         # hyper-parameters during training process
         self.num_rounds = option['num_rounds']
         self.num_steps = option['num_steps']
         self.num_epochs = option['num_epochs']
         self.proportion = option['proportion']
         self.decay_rate = option['learning_rate_decay']
         self.lr_scheduler_type = option['lr_scheduler']
@@ -106,27 +171,25 @@
         self.current_round = 1
         # all options
         self.option = option
         self.id = -1
 
     def run(self):
         """
-        Start the federated learning symtem where the global model is trained iteratively.
+        Running the FL symtem where the global model is trained and evaluated iteratively.
         """
         self.gv.logger.time_start('Total Time Cost')
         self.gv.logger.info("--------------Initial Evaluation--------------")
         self.gv.logger.time_start('Eval Time Cost')
         self.gv.logger.log_once()
         self.gv.logger.time_end('Eval Time Cost')
         while self.current_round <= self.num_rounds:
             self.gv.clock.step()
             # iterate
-            self.gv.logger.time_start('Iterate Time Cost')
             updated = self.iterate()
-            self.gv.logger.time_end('Iterate Time Cost')
             # using logger to evaluate the model if the model is updated
             if updated is True or updated is None:
                 self.gv.logger.info("--------------Round {}--------------".format(self.current_round))
                 # check log interval
                 if self.gv.logger.check_if_log(self.current_round, self.eval_interval):
                     self.gv.logger.time_start('Eval Time Cost')
                     self.gv.logger.log_once()
@@ -140,59 +203,49 @@
         self.gv.logger.time_end('Total Time Cost')
         # save results as .json file
         self.gv.logger.save_output_as_json()
         return
 
     def iterate(self):
         """
-        The standard iteration of each federated round that contains three
+        The standard iteration of each federated communication round that contains three
         necessary procedure in FL: client selection, communication and model aggregation.
-        Args:
+
         Returns:
+            False if the global model is not updated in this iteration
         """
         # sample clients: MD sampling as default
         self.selected_clients = self.sample()
         # training
         models = self.communicate(self.selected_clients)['model']
         # aggregate: pk = 1/K as default where K=len(selected_clients)
         self.model = self.aggregate(models)
-        return len(models)>0
+        return len(models) > 0
 
     @ss.with_dropout
     @ss.with_clock
     def communicate(self, selected_clients, mtype=0, asynchronous=False):
         """
         The whole simulating communication procedure with the selected clients.
         This part supports for simulating the client dropping out.
+
         Args:
             selected_clients (list of int): the clients to communicate with
             mtype (anytype): type of message
             asynchronous (bool): asynchronous communciation or synchronous communcation
+
         Returns:
             :the unpacked response from clients that is created ny self.unpack()
         """
         packages_received_from_clients = []
         received_package_buffer = {}
         communicate_clients = list(set(selected_clients))
         # prepare packages for clients
         for cid in communicate_clients:
             received_package_buffer[cid] = None
-        # try:
-        #     for cid in communicate_clients:
-        #         self.sending_package_buffer[cid] = self.pack(cid, mtype)
-        #         self.sending_package_buffer[cid]['__mtype__'] = mtype
-        # except Exception as e:
-        #     if str(self.device) != 'cpu':
-        #         self.model.to(torch.device('cpu'))
-        #         for cid in communicate_clients:
-        #             self.sending_package_buffer[cid] = self.pack(cid, mtype)
-        #             self.sending_package_buffer[cid]['__mtype__'] = mtype
-        #         self.model.to(self.device)
-        #     else:
-        #         raise e
         # communicate with selected clients
         if self.num_parallels <= 1:
             # computing iteratively
             for client_id in communicate_clients:
                 server_pkg = self.pack(cid, mtype)
                 server_pkg['__mtype__'] = mtype
                 response_from_client_id = self.communicate_with(client_id, package=server_pkg)
@@ -205,231 +258,296 @@
                 server_pkg['__mtype__'] = mtype
                 self.clients[client_id].update_device(self.gv.apply_for_device())
                 args = (int(client_id), server_pkg)
                 packages_received_from_clients.append(pool.apply_async(self.communicate_with, args=args))
             pool.close()
             pool.join()
             packages_received_from_clients = list(map(lambda x: x.get(), packages_received_from_clients))
-        for i,cid in enumerate(communicate_clients): received_package_buffer[cid] = packages_received_from_clients[i]
-        packages_received_from_clients = [received_package_buffer[cid] for cid in selected_clients if received_package_buffer[cid]]
+        for i, cid in enumerate(communicate_clients): received_package_buffer[cid] = packages_received_from_clients[i]
+        packages_received_from_clients = [received_package_buffer[cid] for cid in selected_clients if
+                                          received_package_buffer[cid]]
         self.received_clients = selected_clients
         return self.unpack(packages_received_from_clients)
-    
+
     @ss.with_latency
     def communicate_with(self, target_id, package={}):
+        r"""Communicate with the object under system simulator that simulates the
+        network latency. Send the package to target object according to its id,
+        and receive the response from it
+
+        Args:
+            target_id (int): the id of the object to communicate with
+            package (dict): the package to be sended to the object
+
+        Returns:
+            client_package (dict): the reply from the target object and
+            will be 'None' if losing connection
+        """
         return super(BasicServer, self).communicate_with(target_id, package)
-    
-    
+
     def pack(self, client_id, mtype=0, *args, **kwargs):
-        """
+        r"""
         Pack the necessary information for the client's local training.
         Any operations of compression or encryption should be done here.
+
         Args:
             client_id (int): the id of the client to communicate with
+            mtype: the message type
+
         Returns:
-            a dict that only contains the global model as default.
+            a dict contains necessary information (e.g. a copy of the global model as default)
         """
         return {
-            "model" : copy.deepcopy(self.model),
+            "model": copy.deepcopy(self.model),
         }
 
     def unpack(self, packages_received_from_clients):
-        """
+        r"""
         Unpack the information from the received packages. Return models and losses as default.
+
         Args:
-            packages_received_from_clients (list of dict):
+            packages_received_from_clients (list): a list of packages
+
         Returns::
             res (dict): collections.defaultdict that contains several lists of the clients' reply
         """
-        if len(packages_received_from_clients)==0: return collections.defaultdict(list)
-        res = {pname:[] for pname in packages_received_from_clients[0]}
+        if len(packages_received_from_clients) == 0: return collections.defaultdict(list)
+        res = {pname: [] for pname in packages_received_from_clients[0]}
         for cpkg in packages_received_from_clients:
             for pname, pval in cpkg.items():
                 res[pname].append(pval)
         return res
 
     def global_lr_scheduler(self, current_round):
-        """
+        r"""
         Control the step size (i.e. learning rate) of local training
         Args:
             current_round (int): the current communication round
         """
         if self.lr_scheduler_type == -1:
             return
         elif self.lr_scheduler_type == 0:
             """eta_{round+1} = DecayRate * eta_{round}"""
-            self.lr*=self.decay_rate
+            self.lr *= self.decay_rate
             for c in self.clients:
                 c.set_learning_rate(self.lr)
         elif self.lr_scheduler_type == 1:
             """eta_{round+1} = eta_0/(round+1)"""
-            self.lr = self.option['learning_rate']*1.0/(current_round+1)
+            self.lr = self.option['learning_rate'] * 1.0 / (current_round + 1)
             for c in self.clients:
                 c.set_learning_rate(self.lr)
 
     @ss.with_availability
     def sample(self):
-        """Sample the clients.
-        Args:
+        r"""
+        Sample the clients. There are three types of sampling manners:
+        full sample, uniform sample without replacement, and MDSample
+        with replacement. Particularly, if 'available' is in self.sample_option,
+        the server will only sample from currently available clients.
+
         Returns:
             a list of the ids of the selected clients
+
+        Example::
+            >>> selected_clients=self.sample()
+            >>> selected_clients
+            >>> # The selected_clients is a list of clients' ids
         """
-        all_clients = self.available_clients if 'available' in self.sample_option else [cid for cid in range(self.num_clients)]
+        all_clients = self.available_clients if 'available' in self.sample_option else [cid for cid in
+                                                                                        range(self.num_clients)]
         # full sampling with unlimited communication resources of the server
         if 'full' in self.sample_option:
             return all_clients
         # sample clients
         elif 'uniform' in self.sample_option:
             # original sample proposed by fedavg
-            selected_clients = list(np.random.choice(all_clients, min(self.clients_per_round, len(all_clients)), replace=False)) if len(all_clients)>0 else []
+            selected_clients = list(
+                np.random.choice(all_clients, min(self.clients_per_round, len(all_clients)), replace=False)) if len(
+                all_clients) > 0 else []
         elif 'md' in self.sample_option:
             # the default setting that is introduced by FedProx, where the clients are sampled with the probability in proportion to their local data sizes
             local_data_vols = [self.clients[cid].datavol for cid in all_clients]
             total_data_vol = sum(local_data_vols)
-            p = np.array(local_data_vols)/total_data_vol
-            selected_clients = list(np.random.choice(all_clients, self.clients_per_round, replace=True, p=p)) if len(all_clients)>0 else []
+            p = np.array(local_data_vols) / total_data_vol
+            selected_clients = list(np.random.choice(all_clients, self.clients_per_round, replace=True, p=p)) if len(
+                all_clients) > 0 else []
         return selected_clients
 
     def aggregate(self, models: list, *args, **kwargs):
-        """
-        Aggregate the locally improved models.
-        Args:
-            models (list): a list of local models
-        Returns:
-            the averaged result
+        r"""
+        Aggregate the locally trained models into the new one. The aggregation
+        will be according to self.aggregate_option where
+
         pk = nk/n where n=self.data_vol
         K = |S_t|
         N = |S|
         -------------------------------------------------------------------------------------------------------------------------
          weighted_scale                 |uniform (default)          |weighted_com (original fedavg)   |other
         ==========================================================================================================================
         N/K * Σpk * model_k             |1/K * Σmodel_k             |(1-Σpk) * w_old + Σpk * model_k  |Σ(pk/Σpk) * model_k
+
+
+        Args:
+            models (list): a list of local models
+
+        Returns:
+            the aggregated model
+
+        Example::
+            >>> models = [m1, m2] # m1, m2 are models with the same architecture
+            >>> m_new = self.aggregate(models)
         """
         if len(models) == 0: return self.model
         local_data_vols = [c.datavol for c in self.clients]
         total_data_vol = sum(local_data_vols)
         if self.aggregation_option == 'weighted_scale':
-            p = [1.0 * local_data_vols[cid] /total_data_vol for cid in self.received_clients]
+            p = [1.0 * local_data_vols[cid] / total_data_vol for cid in self.received_clients]
             K = len(models)
             N = self.num_clients
             return fmodule._model_sum([model_k * pk for model_k, pk in zip(models, p)]) * N / K
         elif self.aggregation_option == 'uniform':
             return fmodule._model_average(models)
         elif self.aggregation_option == 'weighted_com':
             p = [1.0 * local_data_vols[cid] / total_data_vol for cid in self.received_clients]
             w = fmodule._model_sum([model_k * pk for model_k, pk in zip(models, p)])
-            return (1.0-sum(p))*self.model + w
+            return (1.0 - sum(p)) * self.model + w
         else:
             p = [1.0 * local_data_vols[cid] / total_data_vol for cid in self.received_clients]
             sump = sum(p)
-            p = [pk/sump for pk in p]
+            p = [pk / sump for pk in p]
             return fmodule._model_sum([model_k * pk for model_k, pk in zip(models, p)])
 
-    def global_test(self, flag='valid'):
-        """
-        Validate accuracies and losses on clients' local datasets
+    def global_test(self, model=None, flag:str='valid'):
+        r"""
+        Collect local testing result of all the clients.
+
         Args:
-            dataflag (str): choose train data or valid data to evaluate
+            model (flgo.utils.fmodule.FModule|torch.nn.Module): the model to be sevaluated
+            flag (str): choose the data to evaluate the model
+
         Returns:
-            metrics (dict): a dict contains the lists of each metric_value of the clients
+            metrics (dict): a dict contains key-value pairs like (metric_name,
+            the lists of metric results of the clients)
         """
+        if model is None: model=self.model
         all_metrics = collections.defaultdict(list)
         for c in self.clients:
-            client_metrics = c.test(self.model, flag)
+            client_metrics = c.test(model, flag)
             for met_name, met_val in client_metrics.items():
                 all_metrics[met_name].append(met_val)
         return all_metrics
 
-    def test(self, model=None, flag='test'):
-        """
+    def test(self, model=None, flag:str='test'):
+        r"""
         Evaluate the model on the test dataset owned by the server.
+
         Args:
             model (flgo.utils.fmodule.FModule): the model need to be evaluated
+            flag (str): choose the data to evaluate the model
+
         Returns::
-            metrics (dict): specified by the task during running time (e.g. metric = [mean_accuracy, mean_loss] when the task is classification)
+            metrics (dict): the dict contains the evaluating results
         """
-        if model is None: model=self.model
-        if flag == 'valid': dataset = self.valid_data
-        elif flag == 'test': dataset = self.test_data
-        else: dataset = self.train_data
-        if dataset is None: return {}
+        if model is None: model = self.model
+        dataset = getattr(self, flag+'_data') if hasattr(self, flag+'_data') else None
+        if dataset is None:
+            return {}
         else:
-            return self.calculator.test(model, dataset, batch_size = self.option['test_batch_size'], num_workers = self.option['num_workers'], pin_memory = self.option['pin_memory'])
+            return self.calculator.test(model, dataset, batch_size=self.option['test_batch_size'],
+                                        num_workers=self.option['num_workers'], pin_memory=self.option['pin_memory'])
 
     def init_algo_para(self, algo_para: dict):
         """
         Initialize the algorithm-dependent hyper-parameters for the server and all the clients.
+
         Args:
             algo_paras (dict): the dict that defines the hyper-parameters (i.e. name, value and type) for the algorithm.
 
-        Example 1:
-            calling `self.init_algo_para({'u':0.1})` will set the attributions `server.u` and `c.u` as 0.1 with type float where `c` is an instance of `CLient`.
+        Example::
+            >>> # s is an instance of Server and s.clients are instances of Client
+            >>> s.u # will raise error
+            >>> [c.u for c in s.clients] # will raise errors too
+            >>> s.init_algo_para({'u': 0.1})
+            >>> s.u # will be 0.1
+            >>> [c.u for c in s.clients] # will be [0.1, 0.1,..., 0.1]
+
         Note:
             Once `option['algo_para']` is not `None`, the value of the pre-defined hyperparameters will be replaced by the list of values in `option['algo_para']`,
             which requires the length of `option['algo_para']` is equal to the length of `algo_paras`
         """
         self.algo_para = algo_para
-        if len(self.algo_para)==0: return
+        if len(self.algo_para) == 0: return
         # initialize algorithm-dependent hyperparameters from the input options
         if self.option['algo_para'] is not None:
             # assert len(self.algo_para) == len(self.option['algo_para'])
             keys = list(self.algo_para.keys())
-            for i,pv in enumerate(self.option['algo_para']):
-                if i==len(self.option['algo_para']): break
+            for i, pv in enumerate(self.option['algo_para']):
+                if i == len(self.option['algo_para']): break
                 para_name = keys[i]
                 try:
                     self.algo_para[para_name] = type(self.algo_para[para_name])(pv)
                 except:
                     self.algo_para[para_name] = pv
         # register the algorithm-dependent hyperparameters as the attributes of the server and all the clients
         for para_name, value in self.algo_para.items():
             self.__setattr__(para_name, value)
-            for c in self.clients:
-                c.__setattr__(para_name, value)
+            for p in self._object_map.values():
+                p.__setattr__(para_name, value)
         return
 
     def get_tolerance_for_latency(self):
+        r"""
+        Get the tolerance for latency of waiting for clients' responses
+
+        Returns:
+            a int number (i.e. self.tolerance_for_latency)
+        """
         return self.tolerance_for_latency
 
     def wait_time(self, t=1):
+        r"""
+        Wait for the time of the virtual clock to pass t units
+        """
         ss.clock.step(t)
         return
 
     @property
     def available_clients(self):
         """
-        Return all the available clients at current round.
-        Args:
-        Returns:: a list of indices of currently available clients
+        Return all the available clients at the current round.
+
+        Returns:
+            a list of indices of currently available clients
         """
         return [cid for cid in range(self.num_clients) if self.clients[cid].is_idle()]
 
     def register_clients(self, clients):
         """
-        register self.clients=clients
+        Regiser clients to self.clients, and update related attributes (e.g. self.num_clients)
+        
         Args:
-            clients (list of Client()): clients
-        Returns:: a list of indices of currently available clients
+            clients (list): a list of objects
         """
-        self.clients = clients
+        self.register_objects(clients, 'clients')
         self.num_clients = len(clients)
         for cid, c in enumerate(self.clients):
             c.client_id = cid
-        for c in self.clients:c.register_server(self)
+        for c in self.clients: c.register_server(self)
         self.clients_per_round = max(int(self.num_clients * self.proportion), 1)
         self.selected_clients = []
         self.dropped_clients = []
 
+
 class BasicClient(BasicParty):
     def __init__(self, option={}):
         super().__init__()
         self.id = None
         # create local dataset
         self.data_loader = None
-        self.test_data=None
+        self.test_data = None
         self.valid_data = None
         self.train_data = None
         self.model = None
         # local calculator
         self.device = self.gv.apply_for_device()
         self.calculator = self.gv.TaskCalculator(self.device, option['optimizer'])
         # hyper-parameters for training
@@ -449,191 +567,216 @@
         self._latency = 0
         # server
         self.server = None
         # actions of different message type
         self.option = option
         self.actions = {0: self.reply}
 
-    def initialize(self):
-        # to be implemented for customized initializing operations
-        return
-
     @ss.with_completeness
     @fmodule.with_multi_gpus
     def train(self, model):
-        """
-        Standard local training procedure. Train the transmitted model with local training dataset.
+        r"""
+        Standard local training procedure. Train the transmitted model with
+        local training dataset.
+
         Args:
             model (FModule): the global model
-        Returns:
         """
         model.train()
-        optimizer = self.calculator.get_optimizer(model, lr=self.learning_rate, weight_decay=self.weight_decay, momentum=self.momentum)
+        optimizer = self.calculator.get_optimizer(model, lr=self.learning_rate, weight_decay=self.weight_decay,
+                                                  momentum=self.momentum)
         for iter in range(self.num_steps):
             # get a batch of data
             batch_data = self.get_batch_data()
             model.zero_grad()
             # calculate the loss of the model on batched dataset through task-specified calculator
             loss = self.calculator.compute_loss(model, batch_data)['loss']
             loss.backward()
             optimizer.step()
         return
 
-    @ fmodule.with_multi_gpus
+    @fmodule.with_multi_gpus
     def test(self, model, flag='valid'):
-        """
-        Evaluate the model with local data (e.g. training data or validating data).
+        r"""
+        Evaluate the model on the dataset owned by the client
+
         Args:
-            model (FModule):
-            dataflag (str): choose the dataset to be evaluated on
+            model (flgo.utils.fmodule.FModule): the model need to be evaluated
+            flag (str): choose the data to evaluate the model
+
         Returns:
-            metric (dict): specified by the task during running time (e.g. metric = [mean_accuracy, mean_loss] when the task is classification)
+            metric (dict): the evaluating results (e.g. metric = {'loss':1.02})
         """
-        if flag == 'valid': dataset = self.valid_data
-        elif flag == 'test': dataset = self.test_data
-        else: dataset = self.train_data
-        if dataset is not None:
-            return self.calculator.test(model, dataset, self.test_batch_size, self.option['num_workers'])
-        else:
-            return {}
+        dataset = getattr(self, flag + '_data') if hasattr(self, flag + '_data') else None
+        if dataset is None: return {}
+        return self.calculator.test(model, dataset, self.test_batch_size, self.option['num_workers'])
+
 
     def unpack(self, received_pkg):
-        """
+        r"""
         Unpack the package received from the server
+
         Args:
             received_pkg (dict): a dict contains the global model as default
+
         Returns:
-            the unpacked information that can be rewritten
+            the unpacked information
         """
         # unpack the received package
         return received_pkg['model']
 
     def reply(self, svr_pkg):
-        """
-        Reply to server with the transmitted package.
-        The whole local procedure should be planned here.
-        The standard form consists of three procedure:
-        unpacking the server_package to obtain the global model,
-        training the global model, and finally packing the updated
-        model into client_package.
+        r"""
+        Reply a package to the server. The whole local procedure should be defined here.
+        The standard form consists of three procedure: unpacking the
+        server_package to obtain the global model, training the global model,
+        and finally packing the updated model into client_package.
+
         Args:
             svr_pkg (dict): the package received from the server
+
         Returns:
             client_pkg (dict): the package to be send to the server
         """
         model = self.unpack(svr_pkg)
         self.train(model)
         cpkg = self.pack(model)
         return cpkg
 
     def pack(self, model, *args, **kwargs):
-        """
+        r"""
         Packing the package to be send to the server. The operations of compression
         of encryption of the package should be done here.
+
         Args:
             model: the locally trained model
-        Returns
+
+        Returns:
             package: a dict that contains the necessary information for the server
         """
         return {
-            "model" : model,
+            "model": model,
         }
 
     def is_idle(self):
-        """
-        Check if the client is active to participate training.
-        Args:
+        r"""
+        Check if the client is available to participate training.
+
         Returns:
-            True if the client is active according to the active_rate else False
+            True if the client is available according to the active_rate else False
         """
-        return self.gv.simulator.client_states[self.id]=='idle'
+        return self.gv.simulator.client_states[self.id] == 'idle'
 
     def is_dropped(self):
-        """
+        r"""
         Check if the client drops out during communicating.
-        Args:
+
         Returns:
             True if the client was being dropped
         """
-        return self.gv.simulator.client_states[self.id]=='dropped'
+        return self.gv.simulator.client_states[self.id] == 'dropped'
 
     def is_working(self):
-        return self.gv.simulator.client_states[self.id]=='working'
+        r"""
+        Check if the client is training the model.
 
-    def train_loss(self, model):
-        """
-        Get the task specified loss of the model on local training data
-        Args: model:
         Returns:
+            True if the client is working
         """
-        return self.test(model,'train')['loss']
 
-    def valid_loss(self, model):
-        """
-        Get the task specified loss of the model on local validating data
-        Args: model:
+        return self.gv.simulator.client_states[self.id] == 'working'
+
+    def train_loss(self, model):
+        r"""
+        Get the loss value of the model on local training data
+
+        Args:
+            model (flgo.utils.fmodule.FModule|torch.nn.Module): model
+
         Returns:
+            the training loss of model on self's training data
         """
-        return self.test(model)['loss']
+        return self.test(model, 'train')['loss']
+
+    def valid_loss(self, model):
+        r"""
+        Get the loss value of the model on local validating data
+
+        Args:
+            model (flgo.utils.fmodule.FModule|torch.nn.Module): model
 
-    def set_model(self, model):
-        """
-        set self.model
-        Args: model:
         Returns:
+            the validation loss of model on self's validation data
         """
-        self.model = model
+        return self.test(model)['loss']
 
     def register_server(self, server=None):
+        r"""
+        Register the server to self.server
+        """
+        self.register_objects([server], 'server_list')
         if server is not None:
             self.server = server
 
     def set_local_epochs(self, epochs=None):
+        r"""
+        Set local training epochs
+        """
         if epochs is None: return
         self.epochs = epochs
-        self.num_steps = self.epochs * math.ceil(len(self.train_data)/self.batch_size)
+        self.num_steps = self.epochs * math.ceil(len(self.train_data) / self.batch_size)
         return
 
     def set_batch_size(self, batch_size=None):
+        r"""
+        Set local training batch size
+
+        Args:
+            batch_size (int): the training batch size
+        """
         if batch_size is None: return
         self.batch_size = batch_size
 
-    def set_learning_rate(self, lr = None):
+    def set_learning_rate(self, lr=None):
         """
-        set the learning rate of local training
-        Args: lr:
-        Returns:
+        Set the learning rate of local training
+        Args:
+            lr (float): a real number
         """
         self.learning_rate = lr if lr else self.learning_rate
 
     def get_time_response(self):
         """
         Get the latency amount of the client
-        Returns: self.latency_amount if client not dropping out
+
+        Returns:
+            self.latency_amount if client not dropping out
         """
         return np.inf if self.dropped else self.time_response
 
     def get_batch_data(self):
         """
-        Get the batch of data
+        Get the batch of training data
         Returns:
             a batch of data
         """
         try:
             batch_data = next(self.data_loader)
         except Exception as e:
-            self.data_loader = iter(self.calculator.get_dataloader(self.train_data, batch_size=self.batch_size, num_workers=self.loader_num_workers, pin_memory=self.option['pin_memory']))
+            self.data_loader = iter(self.calculator.get_dataloader(self.train_data, batch_size=self.batch_size,
+                                                                   num_workers=self.loader_num_workers,
+                                                                   pin_memory=self.option['pin_memory']))
             batch_data = next(self.data_loader)
         # clear local DataLoader when finishing local training
-        self.current_steps = (self.current_steps+1) % self.num_steps
-        if self.current_steps == 0:self.data_loader = None
+        self.current_steps = (self.current_steps + 1) % self.num_steps
+        if self.current_steps == 0: self.data_loader = None
         return batch_data
 
     def update_device(self, dev):
         """
-        Update running-time GPU device to the inputted dev, including change the client's device and the task_calculator's device
+        Update running-time GPU device to dev
+
         Args:
             dev (torch.device): target dev
-        Returns:
         """
         self.device = dev
         self.calculator = self.gv.TaskCalculator(dev, self.calculator.optimizer_name)
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/fedbuff.py` & `flgo-0.0.8/src/flgo/algorithm/fedbuff.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/algorithm/fedfv.py` & `flgo-0.0.8/src/flgo/algorithm/fedfv.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/algorithm/fedmgda+.py` & `flgo-0.0.8/src/flgo/algorithm/fedmgda+.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/algorithm/fedprox.py` & `flgo-0.0.8/src/flgo/algorithm/fedprox.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,7 +1,11 @@
+"""
+This is a non-official implementation of 'Federated Optimization in Heterogeneous
+Networks' (http://arxiv.org/abs/1812.06127)
+"""
 from flgo.algorithm.fedbase import BasicServer, BasicClient
 import copy
 import torch
 from flgo.utils import fmodule
 
 class Server(BasicServer):
     def initialize(self, *args, **kwargs):
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/mifa.py` & `flgo-0.0.8/src/flgo/algorithm/mifa.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/algorithm/powerofchoice.py` & `flgo-0.0.8/src/flgo/algorithm/powerofchoice.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 """
 This is a non-official implementation of 'Client Selection in Federated Learning:
 Convergence Analysis and Power-of-Choice Selection Strategies' (https://arxiv.org/abs/2010.01243).
 """
 import numpy as np
 from flgo.algorithm.fedavg import Client
 from flgo.algorithm.fedbase import BasicServer
-import flgo.system_simulator.base as ss
+import flgo.simulator.base as ss
 
 class Server(BasicServer):
     def initialize(self, *args, **kwargs):
         self.init_algo_para({'d': self.num_clients})
 
     @ss.with_availability
     def sample(self):
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/scaffold.py` & `flgo-0.0.8/src/flgo/algorithm/scaffold.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,11 @@
+"""
+This is a non-official implementation of Scaffold proposed in 'Stochastic
+Controlled Averaging for Federated Learning' (ICML 2020).
+"""
 from flgo.algorithm.fedbase import BasicServer, BasicClient
 import copy
 from flgo.utils import fmodule
 import torch
 
 class Server(BasicServer):
     def initialize(self, *args, **kwargs):
```

### Comparing `flgo-0.0.7/src/flgo/algorithm/vflbase.py` & `flgo-0.0.8/src/flgo/algorithm/vflbase.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,15 @@
-from .fedbase import BasicParty, BasicServer
+from .fedbase import BasicParty
 import collections
 import torch
 import torch.multiprocessing as mp
 
 class PassiveParty(BasicParty):
     def __init__(self, option):
+        super().__init__()
         self.option = option
         self.actions = {0: self.forward, 1:self.backward, 2:self.forward_test}
         self.id = None
         # create local dataset
         self.data_loader = None
         # local calculator
         self.device = self.gv.apply_for_device()
@@ -55,14 +56,15 @@
         dataset = tmp[package['data_type']]
         # select samples in batch
         self.activation = self.local_module(dataset.get_batch_by_id(batch_ids)[0].to(self.device))
         return {'activation': self.activation}
 
 class ActiveParty(PassiveParty):
     def __init__(self, option):
+        super().__init__(option)
         self.actions = {0: self.forward, 1: self.backward,2:self.forward_test}
         self.device = torch.device('cpu') if option['server_with_cpu'] else self.gv.apply_for_device()
         self.calculator = self.gv.TaskCalculator(self.device, optimizer_name = option['optimizer'])
         # basic configuration
         self.task = option['task']
         self.eval_interval = option['eval_interval']
         self.num_parallels = option['num_parallels']
@@ -239,8 +241,8 @@
                     party.local_module.train()
                 else:
                     party.local_module.eval()
             if hasattr(party, 'global_module') and party.global_module is not None:
                 if mode == 'train':
                     party.global_module.train()
                 else:
-                    party.global_module.eval()
+                    party.global_module.eval()
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar100_classification/__init__.py` & `flgo-0.0.8/src/flgo/benchmark/cifar100_classification/__init__.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar100_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/cifar100_classification/core.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,9 +7,9 @@
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BuiltinClassGenerator):
     def __init__(self, rawdata_path=os.path.join(flgo.benchmark.path,'RAW_DATA', 'CIFAR10')):
         super(TaskGenerator, self).__init__('cifar100_classification', rawdata_path, builtin_class, transforms)
 
 class TaskPipe(BuiltinClassPipe):
-    def __init__(self, task_name):
-        super(TaskPipe, self).__init__(task_name, builtin_class, transforms)
+    def __init__(self, task_path):
+        super(TaskPipe, self).__init__(task_path, builtin_class, transforms)
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar100_classification/model/cnn.py` & `flgo-0.0.8/src/flgo/benchmark/cifar100_classification/model/cnn.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar100_classification/model/resnet18.py` & `flgo-0.0.8/src/flgo/benchmark/cifar100_classification/model/resnet18.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar10_classification/__init__.py` & `flgo-0.0.8/src/flgo/benchmark/cifar10_classification/__init__.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar10_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/cifar10_classification/core.py`

 * *Files 13% similar despite different names*

```diff
@@ -7,9 +7,9 @@
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BuiltinClassGenerator):
     def __init__(self, rawdata_path=os.path.join(flgo.benchmark.path,'RAW_DATA', 'CIFAR10')):
         super(TaskGenerator, self).__init__('cifar10_classification', rawdata_path, torchvision.datasets.CIFAR10, transforms)
 
 class TaskPipe(BuiltinClassPipe):
-    def __init__(self, task_name):
-        super(TaskPipe, self).__init__(task_name, torchvision.datasets.CIFAR10, transforms)
+    def __init__(self, task_path):
+        super(TaskPipe, self).__init__(task_path, torchvision.datasets.CIFAR10, transforms)
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar10_classification/model/cnn.py` & `flgo-0.0.8/src/flgo/benchmark/cifar10_classification/model/cnn.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cifar10_classification/model/mlp.py` & `flgo-0.0.8/src/flgo/benchmark/cifar10_classification/model/mlp.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/core.py` & `flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/citeseer_link_prediction/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/citeseer_link_prediction/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/citeseer_node_classification/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/citeseer_node_classification/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/core.py` & `flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cora_link_prediction/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/cora_link_prediction/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cora_node_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/cora_node_classification/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/GraphSAGE_1.py` & `flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/GraphSAGE_1.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/cora_node_classification/model/GraphSage.py` & `flgo-0.0.8/src/flgo/benchmark/cora_node_classification/model/GraphSage.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/emnist_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/emnist_classification/core.py`

 * *Files 12% similar despite different names*

```diff
@@ -4,15 +4,16 @@
 import os.path
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BuiltinClassGenerator):
     def __init__(self, rawdata_path=os.path.join(flgo.benchmark.path,'RAW_DATA', 'EMNIST'), split='byclass'):
         super(TaskGenerator, self).__init__('emnist_classification', rawdata_path, torchvision.datasets.EMNIST, torchvision.transforms.Compose([torchvision.transforms.ToTensor(),]))
         self.split = split
+        self.additional_option = {'split': self.split}
 
     def load_data(self):
         self.train_data = torchvision.datasets.EMNIST(root=self.rawdata_path, split = self.split, download=True, train=True, transform=self.transform)
         self.test_data = torchvision.datasets.EMNIST(root=self.rawdata_path, split = self.split, download=True, train=False, transform=self.transform)
 
 class TaskPipe(BuiltinClassPipe):
-    def __init__(self, task_name):
-        super(TaskPipe, self).__init__(task_name, torchvision.datasets.EMNIST, torchvision.transforms.Compose([torchvision.transforms.ToTensor(),]))
+    def __init__(self, task_path):
+        super(TaskPipe, self).__init__(task_path, torchvision.datasets.EMNIST, torchvision.transforms.Compose([torchvision.transforms.ToTensor(), ]))
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/emnist_classification/model/cnn.py` & `flgo-0.0.8/src/flgo/benchmark/emnist_classification/model/cnn.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/emnist_classification/model/mlp.py` & `flgo-0.0.8/src/flgo/benchmark/emnist_classification/model/mlp.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/enzymes_graph_classification/model/GIN.py` & `flgo-0.0.8/src/flgo/benchmark/enzymes_graph_classification/model/GIN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/fashion_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/fashion_classification/core.py`

 * *Files 13% similar despite different names*

```diff
@@ -7,9 +7,9 @@
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BuiltinClassGenerator):
     def __init__(self, rawdata_path=os.path.join(flgo.benchmark.path,'RAW_DATA', 'FASHION')):
         super(TaskGenerator, self).__init__('fashion_classification',rawdata_path , builtin_class, transforms)
 
 class TaskPipe(BuiltinClassPipe):
-    def __init__(self, task_name):
-        super(TaskPipe, self).__init__(task_name, builtin_class, transforms)
+    def __init__(self, task_path):
+        super(TaskPipe, self).__init__(task_path, builtin_class, transforms)
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/fashion_classification/model/lr.py` & `flgo-0.0.8/src/flgo/benchmark/fashion_classification/model/lr.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/femnist_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/femnist_classification/core.py`

 * *Files 2% similar despite different names*

```diff
@@ -122,9 +122,9 @@
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BuiltinClassGenerator):
     def __init__(self, rawdata_path=os.path.join(flgo.benchmark.path,'RAW_DATA', 'MNIST')):
         super(TaskGenerator, self).__init__('femnist_classification', rawdata_path, FEMNIST, torchvision.transforms.Compose([torchvision.transforms.ToTensor(),]))
 
 class TaskPipe(BuiltinClassPipe):
-    def __init__(self, task_name):
-        super(TaskPipe, self).__init__(task_name, FEMNIST, torchvision.transforms.Compose([torchvision.transforms.ToTensor(),]))
+    def __init__(self, task_path):
+        super(TaskPipe, self).__init__(task_path, FEMNIST, torchvision.transforms.Compose([torchvision.transforms.ToTensor(), ]))
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/leaf_reddit/core.py` & `flgo-0.0.8/src/flgo/benchmark/leaf_reddit/core.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 import torch
 from torchvision.datasets import utils
 
 import json
 from torch.utils.data import Dataset
 
 from flgo.benchmark.toolkits import BasicTaskGenerator
-from flgo.benchmark.toolkits.base import BasicTaskPipe, BasicTaskCalculator
+from flgo.benchmark.base import BasicTaskPipe, BasicTaskCalculator
 
 
 def download_from_url(url= None, filepath = '.'):
     """Download dataset from url to filepath."""
     if url:
         urllib.request.urlretrieve(url, filepath)
     return filepath
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/leaf_reddit/model/stackedlstm.py` & `flgo-0.0.8/src/flgo/benchmark/leaf_reddit/model/stackedlstm.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/leaf_sent140/core.py` & `flgo-0.0.8/src/flgo/benchmark/leaf_sent140/core.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import urllib
 import zipfile
 import torch
 from torch.utils.data import Dataset
 import flgo.benchmark
 import os.path
 from flgo.benchmark.toolkits import BasicTaskGenerator, BasicTaskCalculator
-from flgo.benchmark.toolkits.base import XYHorizontalTaskPipe as TaskPipe, BasicTaskPipe
+from flgo.benchmark.base import XYHorizontalTaskPipe as TaskPipe, BasicTaskPipe
 import collections
 import re
 import os
 import os.path
 import json
 import csv
 import numpy as np
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/leaf_sent140/model/stackedlstm.py` & `flgo-0.0.8/src/flgo/benchmark/leaf_sent140/model/stackedlstm.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/mnist_classification/__init__.py` & `flgo-0.0.8/src/flgo/benchmark/mnist_classification/__init__.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/mnist_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/mnist_classification/core.py`

 * *Files 12% similar despite different names*

```diff
@@ -8,9 +8,9 @@
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BuiltinClassGenerator):
     def __init__(self, rawdata_path=os.path.join(flgo.benchmark.path,'RAW_DATA', 'MNIST')):
         super(TaskGenerator, self).__init__('mnist_classification', rawdata_path, builtin_class, transforms)
 
 class TaskPipe(BuiltinClassPipe):
-    def __init__(self, task_name):
-        super(TaskPipe, self).__init__(task_name, builtin_class, transforms)
+    def __init__(self, task_path):
+        super(TaskPipe, self).__init__(task_path, builtin_class, transforms)
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/mnist_classification/model/cnn.py` & `flgo-0.0.8/src/flgo/benchmark/mnist_classification/model/cnn.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/mnist_classification/model/mlp.py` & `flgo-0.0.8/src/flgo/benchmark/mnist_classification/model/mlp.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/mutag_graph_classification/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/mutag_graph_classification/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/core.py` & `flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/pubmed_link_prediction/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/pubmed_link_prediction/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/core.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/pubmed_node_classification/model/GCN.py` & `flgo-0.0.8/src/flgo/benchmark/pubmed_node_classification/model/GCN.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/core.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import urllib
 import zipfile
 import torch
 from torch.utils.data import TensorDataset, Dataset
 from flgo.benchmark.toolkits import BasicTaskGenerator, BasicTaskCalculator
-from flgo.benchmark.toolkits.base import BasicTaskPipe
+from flgo.benchmark.base import BasicTaskPipe
 import collections
 import re
 import os
 import os.path
 import json
 import flgo.benchmark
 import os.path
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/shakespeare_classification/model/stackedlstm.py` & `flgo-0.0.8/src/flgo/benchmark/shakespeare_classification/model/stackedlstm.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/svhn_classification/model/cnn.py` & `flgo-0.0.8/src/flgo/benchmark/svhn_classification/model/cnn.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/svhn_classification/model/mlp.py` & `flgo-0.0.8/src/flgo/benchmark/svhn_classification/model/mlp.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/synthetic_regression/core.py` & `flgo-0.0.8/src/flgo/benchmark/synthetic_regression/core.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 import numpy as np
-from flgo.benchmark.toolkits.base import *
+from flgo.benchmark.base import *
 from flgo.benchmark.toolkits.cv.horizontal.image_classification import GeneralCalculator
 from flgo.benchmark.toolkits.partition import BasicPartitioner
 TaskPipe = XYHorizontalTaskPipe
 TaskCalculator = GeneralCalculator
 
 class TaskGenerator(BasicTaskGenerator):
     def __init__(self, alpha=0.0, beta=0.0, num_clients=30, imbalance=0.0, mean_datavol=400, dimension=60, num_classes=10, *args, **kwargs):
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/synthetic_regression/model/lr.py` & `flgo-0.0.8/src/flgo/benchmark/synthetic_regression/model/lr.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/base.py` & `flgo-0.0.8/src/flgo/benchmark/base.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,19 +1,25 @@
 import importlib
 import shutil
 from abc import ABCMeta, abstractmethod
 import random
+import os
+try:
+    import ujson as json
+except:
+    import json
 import matplotlib.pyplot as plt
 import numpy as np
-import os
 import torch
 from torch.utils.data import Dataset
-import json
 
 class AbstractTaskGenerator(metaclass=ABCMeta):
+    r"""
+    Abstract Task Generator
+    """
     @abstractmethod
     def load_data(self, *args, **kwarg):
         """Load the original data into memory that can be partitioned"""
         pass
 
     @abstractmethod
     def partition(self, *args, **kwarg):
@@ -26,62 +32,80 @@
     def generate(self, *args, **kwarg):
         """Load and partition the data, and then generate the necessary
         information about the federated task (e.g. path, partition way, ...)"""
         pass
 
 
 class AbstractTaskPipe(metaclass=ABCMeta):
+    r"""
+    Abstract Task Pipe
+    """
     @abstractmethod
     def save_task(self, *args, **kwargs):
         """Save a federated task created by TaskGenerator as a static file on the disk"""
         pass
 
     @abstractmethod
     def load_task(self, *args, **kwargs):
         """Load a federated task from disk"""
         pass
 
 
 class AbstractTaskCalculator(metaclass=ABCMeta):
+    r"""
+    Abstract Task Calculator
+    """
     @abstractmethod
     def to_device(self, *args, **kwargs):
+        """Put the data into the gpu device"""
         pass
 
     @abstractmethod
     def get_dataloader(self, *args, **kwargs):
+        """Return a data loader that splits the input data into batches"""
         pass
 
     @abstractmethod
     def test(self, model, data, *args, **kwargs):
+        """Evaluate the model on the data"""
         pass
 
     @abstractmethod
     def compute_loss(self, model, data, *args, **kwargs):
+        """Compute the loss of the model on the data to complete the forward process"""
         pass
 
     @abstractmethod
     def get_optimizer(self, model, *args, **kwargs):
+        """Return the optimizer on the parameters of the model"""
         pass
 
 class BasicTaskGenerator(AbstractTaskGenerator):
-    def __init__(self, benchmark, rawdata_path):
+    r"""
+        Load the original dataset and partition the
+        original dataset into local data
+    """
+    def __init__(self, benchmark:str, rawdata_path:str):
         """
         Args:
-            benchmark: the name of the ML task to be converted
-            rawdata_path: the dictionary of the original dataset
+            benchmark (str): the name of the federated task
+            rawdata_path (str): the dictionary of the original dataset
         """
         # basic attribution
         self.benchmark = benchmark
         self.rawdata_path = rawdata_path
         # optional attribution
         self.partitioner = None
         self.train_data = None
         self.test_data = None
         self.task_name = None
         self.para = {}
+        self.additional_option = {}
+        self.train_additional_option = {}
+        self.test_additional_option = {}
 
     def generate(self, *args, **kwarg):
         """The whole process to generate federated task. """
         # load data
         self.load_data()
         # partition
         self.partition()
@@ -90,18 +114,19 @@
         return
 
     def load_data(self, *args, **kwargs):
         """Download and load dataset into memory."""
         raise NotImplementedError
 
     def partition(self, *args, **kwargs):
-        """Partition the data"""
+        """Partition the data into different local datasets"""
         return
 
     def register_partitioner(self, partitioner=None):
+        """Register the partitioner as self's data partitioner"""
         self.partitioner = partitioner
 
     def init_para(self, para_list=None):
         pnames = list(self.para.keys())
         if para_list is not None:
             for i, pv in enumerate(para_list):
                 pname = pnames[i]
@@ -110,38 +135,62 @@
                 except:
                     self.para[pname] = pv
         for pname, pv in self.para.items():
             self.__setattr__(pname, pv)
         return
 
     def get_task_name(self):
+        r"""
+        Create the default name of the task
+        """
         if not hasattr(self.partitioner, 'num_parties') and hasattr(self.partitioner, 'num_clients'):
             self.partitioner.num_parties = self.partitioner.num_clients
         else: self.partitioner.num_parties = 'unknown'
         return '_'.join(['B-' + self.benchmark, 'P-' + str(self.partitioner), 'N-' + str(self.partitioner.num_parties)])
 
 class BasicTaskPipe(AbstractTaskPipe):
+    r"""
+    Store the partition information of TaskGenerator into the disk
+    when generating federated tasks.
+
+    Load the original dataset and the partition information to
+    create the federated scenario when optimizing models
+    """
     TaskDataset = None
 
     def __init__(self, task_path):
+        r"""
+        Args:
+            task_path (str): the path of the federated task
+        """
         self.task_path = task_path
         if os.path.exists(os.path.join(self.task_path, 'data.json')):
             with open(os.path.join(self.task_path, 'data.json'), 'r') as inf:
                 self.feddata = json.load(inf)
 
     def save_task(self, generator):
-        # Construct `feddata` and store it into the disk for recover the partitioned datasets again from it
+        """Construct `feddata` and store it into the disk for recovering
+        the partitioned datasets again from it"""
         raise NotImplementedError
 
     def load_data(self, running_time_option) -> dict:
-        # Load the data and process it to the format that can be distributed to different objects
+        """Load the data and process it to the format that can be distributed
+        to different objects"""
         raise NotImplementedError
 
     def generate_objects(self, running_time_option, algorithm, scene='horizontal') -> list:
-        # Generate the virtual objects (i.e. coordinators and participants) in the FL system
+        r"""
+        Generate the virtual objects (i.e. coordinators and participants)
+        in the FL system
+
+        Args:
+            running_time_option (dict): the option (i.e. configuration)
+            algorithm (module|class): algorithm
+            scene (str): horizontal or vertical
+        """
         if scene=='horizontal':
             # init clients
             Client = algorithm.Client
             clients = [Client(running_time_option) for _ in range(len(self.feddata['client_names']))]
             for cid, c in enumerate(clients):
                 c.id = cid
                 c.name = self.feddata['client_names'][cid]
@@ -162,70 +211,110 @@
             for pid, pname in enumerate(self.feddata['party_names']):
                 is_active = self.feddata[pname]['data']['with_label']
                 obj = ActiveParty(running_time_option) if is_active else PassiveParty(running_time_option)
                 obj.id = pid
                 obj.name = pname
                 objects.append(obj)
             for party in objects:
-                party.register_parties(objects)
+                party.register_objects(objects)
         return objects
 
     def save_info(self, generator):
+        r"""
+        Save the basic information of the generated task into the disk
+        """
         info = {'benchmark': '.'.join(generator.__module__.split('.')[:-1])}
         info['scene'] = generator.scene if hasattr(generator, 'scene') else 'unknown'
         info['num_clients'] = generator.num_clients if hasattr(generator, 'num_clients') else (generator.num_parties if hasattr(self, 'num_parties') else 'unknown')
         with open(os.path.join(self.task_path, 'info'), 'w') as outf:
             json.dump(info, outf)
 
     def load_task(self, running_time_option, *args, **kwargs):
+        r"""
+        Load the generated task into disk and create objects in the federated
+        scenario.
+        """
         task_data = self.load_data(running_time_option)
         objects = self.generate_objects(running_time_option)
         self.distribute(task_data, objects)
         return objects
 
     def distribute(self, task_data: dict, objects: list):
+        r"""
+        Distribute the loaded local datasets to different objects in
+        the federated scenario
+        """
         for ob in objects:
             ob_data = task_data[ob.name]
             for data_name, data in ob_data.items():
                 ob.set_data(data, data_name)
 
     def split_dataset(self, dataset, p=0.0):
+        r"""
+        Split the dataset into two parts.
+
+        Args:
+            dataset (torch.utils.data.Dataset): the dataset to be splitted
+            p (float): the ratio of the splitting
+
+        Returns:
+            The two split parts
+        """
         if p == 0: return dataset, None
         s1 = int(len(dataset) * p)
         s2 = len(dataset) - s1
         return torch.utils.data.random_split(dataset, [s2, s1])
 
     def task_exists(self):
-        """Check whether the task already exists."""
+        r"""
+        Check whether the task already exists.
+
+        Returns:
+            True if the task already exists
+        """
         return os.path.exists(self.task_path)
 
     def remove_task(self):
-        "remove the task"
+        r"""Remove this task"""
         if self.task_exists():
             shutil.rmtree(self.task_path)
         return
 
     def create_task_architecture(self):
         """Create the directories of the task."""
         if not self.task_exists():
             os.mkdir(self.task_path)
             os.mkdir(os.path.join(self.task_path, 'record'))
             os.mkdir(os.path.join(self.task_path, 'log'))
         else:
             raise FileExistsError("federated task {} already exists!".format(self.task_path))
 
-    def save_figure(self):
-        plt.savefig(os.path.join(self.task_path, 'res.png'))
-
     def gen_client_names(self, num_clients):
+        r"""
+        Generate the names of clients
+
+        Returns:
+            a list of strings
+        """
         return [('Client{:0>' + str(len(str(num_clients))) + 'd}').format(i) for i in range(num_clients)]
 
 
 class BasicTaskCalculator(AbstractTaskCalculator):
+    r"""
+    Support task-specific computation when optimizing models, such
+    as putting data into device, computing loss, evaluating models,
+    and creating the data loader
+    """
+
     def __init__(self, device, optimizer_name='sgd'):
+        r"""
+        Args:
+            device (torch.device): device
+            optimizer_name (str): the name of the optimizer
+        """
         self.device = device
         self.optimizer_name = optimizer_name
         self.criterion = None
         self.DataLoader = None
 
     def to_device(self, data, *args, **kwargs):
         return NotImplementedError
@@ -236,14 +325,26 @@
     def test(self, model, data, *args, **kwargs):
         return NotImplementedError
 
     def compute_loss(self, model, data, *args, **kwargs):
         return NotImplementedError
 
     def get_optimizer(self, model=None, lr=0.1, weight_decay=0, momentum=0):
+        r"""
+        Create optimizer of the model parameters
+
+        Args:
+            model (torch.nn.Module): model
+            lr (float): learning rate
+            weight_decay (float): the weight_decay coefficient
+            momentum (float): the momentum coefficient
+
+        Returns:
+            the optimizer
+        """
         OPTIM = getattr(importlib.import_module('torch.optim'), self.optimizer_name)
         filter_fn = filter(lambda p: p.requires_grad, model.parameters())
         if self.optimizer_name.lower() == 'sgd':
             return OPTIM(filter_fn, lr=lr, momentum=momentum, weight_decay=weight_decay)
         elif self.optimizer_name.lower() in ['adam', 'rmsprop', 'adagrad']:
             return OPTIM(filter_fn, lr=lr, weight_decay=weight_decay)
         else:
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/cv/horizontal/image_classification.py` & `flgo-0.0.8/src/flgo/benchmark/toolkits/cv/horizontal/image_classification.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,28 +1,47 @@
 import random
 import torch.utils.data
 import json
-from flgo.benchmark.toolkits.base import *
+from flgo.benchmark.base import *
 
 class BuiltinClassGenerator(BasicTaskGenerator):
+    r"""
+    Generator for the dataset in torchvision.datasets.
+
+    Args:
+        benchmark (str): the name of the benchmark
+        rawdata_path (str): the path storing the raw data
+        builtin_class (class): class in torchvision.datasets
+        transform (torchvision.transforms.*): the transform
+    """
     def __init__(self, benchmark, rawdata_path, builtin_class, transform=None):
         super(BuiltinClassGenerator, self).__init__(benchmark, rawdata_path)
         self.builtin_class = builtin_class
         self.transform = transform
         self.additional_option = {}
+        self.train_additional_option = {}
+        self.test_additional_option = {}
 
     def load_data(self):
         self.train_data = self.builtin_class(root=self.rawdata_path, download=True, train=True, transform=self.transform)
         self.test_data = self.builtin_class(root=self.rawdata_path, download=True, train=False, transform=self.transform)
 
     def partition(self):
         self.local_datas = self.partitioner(self.train_data)
         self.num_clients = len(self.local_datas)
 
 class BuiltinClassPipe(BasicTaskPipe):
+    r"""
+    TaskPipe for the dataset in torchvision.datasets.
+
+    Args:
+        task_path (str): the path of the task
+        builtin_class (class): class in torchvision.datasets
+        transform (torchvision.transforms.*): the transform
+    """
     class TaskDataset(torch.utils.data.Subset):
         def __init__(self, dataset, indices, perturbation=None, pin_memory=False):
             super().__init__(dataset, indices)
             self.dataset = dataset
             self.indices = indices
             self.perturbation = {idx:p for idx, p in zip(indices, perturbation)} if perturbation is not None else None
             self.pin_memory = pin_memory
@@ -43,32 +62,43 @@
                 if self.perturbation is None:
                     if isinstance(idx, list):
                         return self.dataset[[self.indices[i] for i in idx]]
                     return self.dataset[self.indices[idx]]
                 else:
                     return self.dataset[self.indices[idx]][0] + self.perturbation[self.indices[idx]],  self.dataset[self.indices[idx]][1]
 
-    def __init__(self, task_name, buildin_class, transform=None):
-        super(BuiltinClassPipe, self).__init__(task_name)
+    def __init__(self, task_path, buildin_class, transform=None):
+        super(BuiltinClassPipe, self).__init__(task_path)
         self.builtin_class = buildin_class
         self.transform = transform
 
     def save_task(self, generator):
         client_names = self.gen_client_names(len(generator.local_datas))
-        feddata = {'client_names': client_names, 'server_data': list(range(len(generator.test_data))),  'rawdata_path': generator.rawdata_path, 'additional_option': generator.additional_option}
+        feddata = {'client_names': client_names, 'server_data': list(range(len(generator.test_data))),  'rawdata_path': generator.rawdata_path, 'additional_option': generator.additional_option, 'train_additional_option':generator.train_additional_option, 'test_additional_option':generator.test_additional_option,}
         for cid in range(len(client_names)): feddata[client_names[cid]] = {'data': generator.local_datas[cid],}
         if hasattr(generator.partitioner, 'local_perturbation'): feddata['local_perturbation'] = generator.partitioner.local_perturbation
         with open(os.path.join(self.task_path, 'data.json'), 'w') as outf:
             json.dump(feddata, outf)
         return
 
     def load_data(self, running_time_option) -> dict:
         # load the datasets
-        train_data = self.builtin_class(root=self.feddata['rawdata_path'], download=True, train=True, transform=self.transform, **self.feddata['additional_option'])
-        test_data = self.builtin_class(root=self.feddata['rawdata_path'], download=True, train=False, transform=self.transform, **self.feddata['additional_option'])
+        train_default_init_para = {'root': self.feddata['rawdata_path'], 'download':True, 'train':True, 'transform':self.transform}
+        test_default_init_para = {'root': self.feddata['rawdata_path'], 'download':True, 'train':False, 'transform':self.transform}
+        if 'additional_option' in self.feddata.keys():
+            train_default_init_para.update(self.feddata['additional_option'])
+            test_default_init_para.update(self.feddata['additional_option'])
+        if 'train_additional_option' in self.feddata.keys(): train_default_init_para.update(self.feddata['train_additional_option'])
+        if 'test_additional_option' in self.feddata.keys(): test_default_init_para.update(self.feddata['test_additional_option'])
+        train_pop_key = [k for k in train_default_init_para.keys() if k not in self.builtin_class.__init__.__annotations__]
+        test_pop_key = [k for k in test_default_init_para.keys() if k not in self.builtin_class.__init__.__annotations__]
+        for k in train_pop_key: train_default_init_para.pop(k)
+        for k in test_pop_key: test_default_init_para.pop(k)
+        train_data = self.builtin_class(**train_default_init_para)
+        test_data = self.builtin_class(**test_default_init_para)
         test_data = self.TaskDataset(test_data, list(range(len(test_data))), None, running_time_option['pin_memory'])
         # rearrange data for server
         server_data_test, server_data_valid = self.split_dataset(test_data, running_time_option['test_holdout'])
         task_data = {'server': {'test': server_data_test, 'valid': server_data_valid}}
         # rearrange data for clients
         local_perturbation = self.feddata['local_perturbation'] if 'local_perturbation' in self.feddata.keys() else [None for _ in self.feddata['client_names']]
         for cid, cname in enumerate(self.feddata['client_names']):
@@ -79,14 +109,21 @@
                 cdata_valid, cdata_test = self.split_dataset(cdata_valid, 0.5)
             else:
                 cdata_test = None
             task_data[cname] = {'train':cdata_train, 'valid':cdata_valid, 'test': cdata_test}
         return task_data
 
 class GeneralCalculator(BasicTaskCalculator):
+    r"""
+    Calculator for the dataset in torchvision.datasets.
+
+    Args:
+        device (torch.device): device
+        optimizer_name (str): the name of the optimizer
+    """
     def __init__(self, device, optimizer_name='sgd'):
         super(GeneralCalculator, self).__init__(device, optimizer_name)
         self.criterion = torch.nn.CrossEntropyLoss()
         self.DataLoader = torch.utils.data.DataLoader
 
     def compute_loss(self, model, data):
         """
@@ -129,19 +166,7 @@
     def to_device(self, data):
         return data[0].to(self.device), data[1].to(self.device)
 
     def get_dataloader(self, dataset, batch_size=64, shuffle=True, num_workers=0, pin_memory=False, drop_last=False):
         if self.DataLoader == None:
             raise NotImplementedError("DataLoader Not Found.")
         return self.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers, pin_memory=pin_memory, drop_last=drop_last)
-
-class GeneralGenerator(BasicTaskGenerator):
-    def __init__(self, benchmark, rawdata_path):
-        super(GeneralGenerator, self).__init__(benchmark, rawdata_path)
-        return
-
-    def load_data(self):
-        pass
-
-    def partition(self):
-        return self.partitioner(self.train_data)
-
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/graph_classification.py` & `flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/graph_classification.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,24 +1,14 @@
-import community.community_louvain
-import torch
-from community import community_louvain
 from torch import Tensor
 from torch_geometric.data import Data, DataLoader
-from torch_geometric.datasets import Planetoid
-import torch_geometric.transforms as T
-from torch_geometric.utils import train_test_split_edges, mask_to_index, index_to_mask, from_networkx
 
-import torch_geometric.utils
 import collections
 import numpy as np
-import os
-import json
 
-from flgo.benchmark.toolkits.base import *
-import networkx as nx
+from flgo.benchmark.base import *
 
 from flgo.benchmark.toolkits import BasicTaskPipe, BasicTaskCalculator
 
 
 class GraphClassificationTaskGen(BasicTaskGenerator):
     def __init__(self, benchmark, rawdata_path, builtin_class, dataset_name, transforms=None):
         super(GraphClassificationTaskGen, self).__init__(benchmark, rawdata_path)
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/link_prediction.py` & `flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/link_prediction.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import networkx as nx
 import torch_geometric
 from torch_geometric.transforms import RandomLinkSplit
 from torch_geometric.utils import negative_sampling, from_networkx
 import torch_geometric.utils
 import collections
 
-from flgo.benchmark.toolkits.base import *
+from flgo.benchmark.base import *
 
 
 class LinkPredicitonTaskGenenerator(BasicTaskGenerator):
     def __init__(self, benchmark, rawdata_path, builtin_class, dataset_name, transforms=None, num_clients=10):
         super(LinkPredicitonTaskGenenerator, self).__init__(benchmark, rawdata_path)
         self.builtin_class = builtin_class
         self.dataset_name = dataset_name
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/graph/horizontal/node_classification.py` & `flgo-0.0.8/src/flgo/benchmark/toolkits/graph/horizontal/node_classification.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 import community.community_louvain
 import torch_geometric.transforms as T
 from torch_geometric.utils import mask_to_index, index_to_mask, from_networkx
 import torch_geometric.utils
 import collections
-from flgo.benchmark.toolkits.base import *
+from flgo.benchmark.base import *
 import networkx as nx
 
 
 class NodeClassificationTaskGen(BasicTaskGenerator):
     def __init__(self, benchmark, rawdata_path, builtin_class, dataset_name, transforms=None, num_clients=10):
         super(NodeClassificationTaskGen, self).__init__(benchmark, rawdata_path)
         self.builtin_class = builtin_class
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/partition.py` & `flgo-0.0.8/src/flgo/benchmark/toolkits/partition.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,19 +32,29 @@
     task generator of different benchmarks. By overwriting __call__ method, different partitioners
     can be realized. The input of __call__ is usually a dataset.
     """
     def __call__(self, *args, **kwargs):
         return
 
     def register_generator(self, generator):
-        """Register the generator as an attribute that is accessible"""
+        r"""Register the generator as an self's attribute"""
         self.generator = generator
 
     def data_imbalance_generator(self, num_clients, datasize, imbalance=0):
-        """Split a data size into several parts"""
+        r"""
+        Split the data size into several parts
+
+        Args:
+            num_clients (int): the number of clients
+            datasize (int): the total data size
+            imbalance (float): the degree of data imbalance across clients
+
+        Returns:
+            a list of integer numbers that represents local data sizes
+        """
         if imbalance == 0:
             samples_per_client = [int(datasize / num_clients) for _ in range(num_clients)]
             for _ in range(datasize % num_clients): samples_per_client[_] += 1
         else:
             imbalance = max(0.1, imbalance)
             sigma = imbalance
             mean_datasize = datasize / num_clients
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/toolkits/visualization.py` & `flgo-0.0.8/src/flgo/benchmark/toolkits/visualization.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,15 +1,23 @@
 import matplotlib.pyplot as plt
 import random
 import matplotlib.colors
 import collections
 import numpy as np
 import os
 
-def visualize_by_class(generator, partitioner):
+def visualize_by_class(generator, partitioner, task_path:str):
+    r"""
+    Visualize the partitioned dataset and save the figure
+
+    Args:
+        generator (flgo.benchmark.toolkits.BasicTaskGenerator): task generator
+        partitioner (flgo.benchmark.toolkits.partition.BasicPartitioner): partitioner
+        task_path (str): the path storing the figure
+    """
     all_labels = [d[-1] for d in generator.train_data]
     num_classes = len(set(all_labels))
     ax = plt.subplots()
     colors = [key for key in matplotlib.colors.CSS4_COLORS.keys()]
     random.shuffle(colors)
     client_height = 1
     if hasattr(partitioner, 'dirichlet_dist'):
@@ -36,8 +44,9 @@
             for lbi in range(num_classes):
                 plt.fill_between([offset, offset + lb_counter[lbi]], y_bottom, y_top, facecolor=colors[lbi])
                 offset += lb_counter[lbi]
     plt.xlim(0, max(data_columns))
     plt.ylim(-0.5, generator.partitioner.num_parties - 0.5)
     plt.ylabel('Client ID')
     plt.xlabel('Number of Samples')
+    plt.savefig(os.path.join(task_path, 'res.png'))
     plt.show()
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/core.py` & `flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/core.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from flgo.benchmark.mnist_classification.core import builtin_class, transforms
-from flgo.benchmark.toolkits.base import BasicTaskPipe, BasicTaskCalculator
+from flgo.benchmark.base import BasicTaskPipe, BasicTaskCalculator
 from flgo.benchmark.toolkits.cv.horizontal.image_classification import BuiltinClassGenerator
 import torch
 import os.path
 from torch.utils.data import Dataset
 import flgo
 import random
 import json
```

### Comparing `flgo-0.0.7/src/flgo/benchmark/vertical_mnist_classification/model/mlp.py` & `flgo-0.0.8/src/flgo/benchmark/vertical_mnist_classification/model/mlp.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/experiment/analyzer.py` & `flgo-0.0.8/src/flgo/experiment/analyzer.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 r"""
 This module is to analyze the training results saved by Logger. To use this module,
-a analysis plan must be designed as a dict that contains three parts:
-    Selector: select the records according to the task, algorithm and options of the task
-    Painter: draw graphic of the selected records
-    Table: output some statistic of the selected records on the console
+a analysis plan should be designed (i.e. dict):
+    *Selector*: select the records according to the task, algorithm and options of the task
+    *Painter*: draw graphic of the selected records
+    *Table*: output some statistic of the selected records on the console
 
 The basic usage is to build a plan dict and pass it to flgo.experiment.analyzer
 >>> # plan = {'Selector':..., 'Painter':..., 'Table':...,}
 >>> flgo.experiment.analyzer.show(plan)
 
 The following three examples show how to build a customized plan:
 
@@ -46,14 +46,15 @@
 """
 import argparse
 import math
 import random
 import numpy as np
 import matplotlib.pyplot as plt
 import yaml
+import uuid
 import os
 import collections
 import copy
 import matplotlib as mpl
 import prettytable as pt
 import json
 from flgo.utils.fflow import load_configuration
@@ -73,22 +74,31 @@
         'availability': 'AVL',
         'connectivity': 'CN',
         'completeness': 'CP',
         'responsiveness': 'RS',
     }
 
 class Record:
+    r"""
+    Read the record that is stored by each runner into the memory according
+    to the task and the name.
+
+    Args:
+        task (str): the path of the task
+        name (str): the name of the saved record
+    """
     def __init__(self, task, name):
         self.task = task
         self.name = name
         self.rec_path = os.path.join(task, 'record', name)
         with open(self.rec_path, 'r') as inf:
             s_inf = inf.read()
             rec = json.loads(s_inf)
         self.data = rec
+        self.datas = [self.data]
         self.set_communication_round()
         self.set_client_id()
 
     def set_communication_round(self):
         num_rounds = self.data['option']['num_rounds']
         eval_interval = self.data['option']['eval_interval']
         x = [0]
@@ -121,36 +131,67 @@
     def get_key_from_name(self, key):
         if key == '': return ''
         value_start = self.name.find('_' + key) + len(key) + 1
         value_end = self.name.find('_', value_start)
         return self.name[value_start:value_end]
 
     @classmethod
-    def group_records(cls, rec_list: list):
+    def create_group(cls, rec_list: list):
+        r"""
+        Organize the records in rec_list into a group-level Record,
+        where there will be a new attribute named Record.datas. And
+        the values in Record.data will be replaced by the mean values
+        of that in Record.datas
+
+        Args:
+            rec_list (list): a list of Record(...)
+
+        Returns:
+            a new group-level Record
+        """
         if len(rec_list) == 0: return None
         r = copy.deepcopy(rec_list[0])
         r.datas = [rec.data for rec in rec_list]
         for key in r.data.keys():
             if key == 'option': continue
-            if type(r.data[key]) is list:
-                ave_data = np.array([np.array(rdata[key]) for rdata in r.datas])
-                r.data[key] = ave_data.mean(axis=0)
+            try:
+                if type(r.data[key]) is list:
+                    ave_data = np.array([np.array(rdata[key]) for rdata in r.datas])
+                    r.data[key] = ave_data.mean(axis=0)
+            except:
+                continue
         return r
 ############################## Selector ##############################
 class Selector:
+    r"""
+    Filter the records and read them into memory accoring to customized settings
+    
+    Args:
+        selector_config (dict): the dictionary that is used to filter records
+
+    Example::
+        >>> task='./my_task'
+        >>> selector = Selector({'task':task, 'header':['fedavg'], 'filter':{'lr':0.1}})
+        >>> selector.records[task]
+        >>> # selector.records is a dict where selector.records[task] is a list
+        >>> # of the records that pass the filter
+    """
     def __init__(self, selector_config):
         self.config = selector_config
         self.tasks = [selector_config['task']] if type(selector_config['task']) is not list else selector_config['task']
         self.headers = selector_config['header'] if type(selector_config['header']) is list else [selector_config['header']]
         self.filter = selector_config['filter'] if 'filter' in selector_config.keys() else {}
         self.legend_with = selector_config['legend_with'] if 'legend_with' in selector_config.keys() else []
         self.rec_names = self.scan()
         self.records = self.read_records(self.rec_names)
+        tmp = list(self.records.values())
+        self.all_records = []
+        for ti in tmp: self.all_records.extend(ti)
         try:
-            self.group_names, self.grouped_records = self.group_records_by_seed()
+            self.grouped_records, self.group_names, = self.group_records()
         except Exception() as e:
             print(e)
 
     def scan(self):
         res = {}
         for task in self.tasks:
             path = os.path.join(task, 'record')
@@ -195,32 +236,53 @@
             for record_name in rec_names[task]:
                 if record_name in files:
                     record = Record(task, record_name)
                     record.set_legend(self.legend_with)
                     res[task].append(record)
         return res
 
-    def group_records_by_seed(self):
-        group_names = {task:[] for task in self.rec_names}
-        grouped_records = {task:[] for task in self.rec_names}
-        for task in self.rec_names:
-            groups = collections.defaultdict(list)
-            for rec in self.records[task]:
-                s = rec.name.find('_S')
-                g = rec.name[:s] + rec.name[rec.name.find('_', s+1):]
-                groups[g].append(rec)
-            for g in groups:
-                group_names[task].append(g)
-                grouped_records[task].append(Record.group_records(groups[g]))
-        # aggregate different records within the same group
-        return group_names, grouped_records
+    def group_records(self, key=['seed']):
+        if type(key) is not list: key=[key]
+        groups = collections.defaultdict(list)
+        for rec in self.all_records:
+            group_name = '.'.join([str(rec.data['option'][k]) for k in rec.data['option'].keys() if k not in key])
+            groups[group_name].append(rec)
+        res = []
+        for g in groups:
+            res.append(Record.create_group(groups[g]))
+        return res, list(groups.keys())
 
 ##############################  Painter ##############################
 class PaintObject:
-    def __init__(self, rec: dict, args: dict,  obj_option: dict, draw_func: str):
+    r"""
+    The basic PaintObject. Each PaintObject should inherent from this class.
+    And the method self.draw should be overwritten if necessary.
+
+    Args:
+        rec (Record): the record
+        args (dict): the painting arguments
+        obj_option (dict): the personal option for each object
+        draw_func (str): optional, the function name. All the subclass of this class won't claim this parameter.
+
+    Example::
+        >>> class GroupCurve(PaintObject):
+        ...     def __init__(self, rec, args,  obj_option):
+        ...         super(GroupCurve, self).__init__(rec, args, obj_option, '')
+        ...
+        ...     def draw(self, ax):
+        ...         x = self.rec.data[self.args['x']]
+        ...         ykey = self.args['y']
+        ...         mean_y = self.rec.data[ykey]
+        ...         min_y = np.min(np.array([d[ykey] for d in self.rec.datas]), axis=0)
+        ...         max_y = np.max(np.array([d[ykey] for d in self.rec.datas]), axis=0)
+        ...         ax.plot(x, mean_y, label=self.rec.data['label'])
+        ...         ax.fill_between(x, max_y, min_y, alpha=0.3)
+        ...         ax.legend()
+    """
+    def __init__(self, rec: Record, args: dict,  obj_option: dict, draw_func: str):
         self.rec = rec
         self.args = args
         self.obj_option = obj_option
         self.draw_func = draw_func
         self.para = (rec.data[v] for v in args.values())
         self.with_legend = True
 
@@ -229,33 +291,38 @@
             eval('ax.'+str(self.draw_func)+'(*self.para, **self.obj_option)')
         else:
             eval('ax.' + str(self.draw_func) + '(*self.para, **self.obj_option, label=self.rec.data["label"])')
         if self.with_legend: eval('ax.legend()')
         return
 
 class Curve(PaintObject):
+    """Curve Object"""
     def __init__(self, rec, args,  obj_option):
         super(Curve, self).__init__(rec, args, obj_option, 'plot')
 
 class Bar(PaintObject):
+    """Bar Object"""
     def __init__(self, rec, args,  obj_option):
         super(Bar, self).__init__(rec, args, obj_option, 'bar')
 
 class Scatter(PaintObject):
+    """Scatter Obejct"""
     def __init__(self, rec, args,  obj_option):
         super(Scatter, self).__init__(rec, args, obj_option, 'scatter')
 
 class Trace2D(PaintObject):
+    """Trace Object"""
     def __init__(self, rec, args,  obj_option):
         super(Trace2D, self).__init__(rec, args, obj_option, '')
 
     def draw(self, ax):
         pass
 
 class GroupCurve(PaintObject):
+    """Group Curve Object"""
     def __init__(self, rec, args,  obj_option):
         super(GroupCurve, self).__init__(rec, args, obj_option, '')
 
     def draw(self, ax):
         x = self.rec.data[self.args['x']]
         ykey = self.args['y']
         mean_y = self.rec.data[ykey]
@@ -265,29 +332,51 @@
         ax.fill_between(x, max_y, min_y, alpha=0.3)
         ax.legend()
 
 class GroupBar(Bar):
     pass
 
 class Painter:
-    def __init__(self, painter_config: dict, records: list, save_figure=False):
-        self.config = painter_config
+    r"""
+    Draw the information in records into figures
+
+    Args:
+        records (list): a list of instances of Record(...)
+        save_text (bool): whether to store the figures into the disk
+        path (str): the storing path
+        format (str): the storing format
+    """
+    def __init__(self, records: list, save_figure=False, path:str='.', format='png'):
         self.records = records
         self.save_figure = save_figure
-
-    def generate_obj_option(self, raw_obj_option: dict):
-        for k in raw_obj_option:
-            if type(raw_obj_option[k]) is list:
-                assert len(raw_obj_option[k]) >= len(self.records)
-                raw_obj_option[k] = raw_obj_option[k][:len(self.records)]
-            else:
-                raw_obj_option[k] = [raw_obj_option[k] for _ in self.records]
-        return [{k:v[i] for k,v in raw_obj_option.items()} for i in range(len(self.records))]
+        self.path = path
+        self.format = format
 
     def create_figure(self, object_class, fig_config):
+        r"""
+        Create figure according to the PaintObject and figure configurations.
+        For each record k, a PaintObject(record, object_option) will be created
+        for later drawing. Then, a figure will be created by fig_option and all 
+        the PaintObject will be put onto the figure. 
+        The fig_config should be a dict like:
+            {
+                'args':{...}, # ploting arguments for each record
+                'obj_option':{...}, # assign each PaintObject with different attributes like color, label...
+                'fig_option':{...}, # the options of the figure such as title, xlabel, xlim, no_legend
+            }
+        
+        Args:
+            object_class (class|str): the types of the obejct to be drawed
+            fig_config (dict): the drawing configuration
+
+        Example::
+            >>> p=Painter(records)
+            >>> p.create_figure(Curve, {'args':{'x':'communication_round', 'y':'valid_loss'}})
+        """
+        object_class = eval(object_class) if type(object_class) is str else object_class
         if 'split' in  fig_config.keys():
             cols = fig_config['split']['cols'] if 'cols' in fig_config['split'] else 4
             rows = int(math.ceil(len(self.records)/cols))
             cols = min(len(self.records), cols)
             if 'figsize' in fig_config['split']:
                 new_fig_size = (fig_config['split']['figsize'][0], fig_config['split']['figsize'][1])
             else:
@@ -298,15 +387,15 @@
                 axs = axs.reshape(-1)
             else:
                 axs = [axs]
         else:
             fig, ax = plt.subplots()
             axs = [ax for _ in self.records]
         args = fig_config['args']
-        obj_options = self.generate_obj_option(fig_config['obj_option']) if 'obj_option' in fig_config.keys() else [{} for _ in self.records]
+        obj_options = self._generate_obj_option(fig_config['obj_option']) if 'obj_option' in fig_config.keys() else [{} for _ in self.records]
         objects = [object_class(rec, args, obj_option) for rec, obj_option in zip(self.records, obj_options)]
         for ob,axi in zip(objects, axs):
             ob.draw(axi)
         if 'fig_option' in fig_config.keys():
             if 'no_legend' in fig_config['fig_option'].keys():
                 for obj in objects: obj.with_legend = False
             for option_name in fig_config['fig_option']:
@@ -319,159 +408,291 @@
                         for ax in axs:
                             eval('ax.set_'+option_name+"({})".format(fig_config['fig_option'][option_name]))
                 else:
                     if type(fig_config['fig_option'][option_name]) is str:
                         eval('plt.'+option_name+"('{}')".format(fig_config['fig_option'][option_name]))
                     else:
                         eval('plt.' + option_name + "({})".format(fig_config['fig_option'][option_name]))
+        filename = None
+        if self.save_figure:
+            filename = str(uuid.uuid4())+'.'+self.format
+            plt.savefig(os.path.join(self.path, filename))
         plt.show()
+        return filename
 
-    def run(self, group=False):
-        for object_class_string in self.config.keys():
-            object_class = eval(object_class_string)
-            con1 = object_class_string.startswith('Group') and group
-            con2 = not object_class_string.startswith('Group') and not group
-            if con1 or con2:
-                for fig_config in self.config[object_class_string]:
-                    self.create_figure(object_class, fig_config)
+    def _generate_obj_option(self, raw_obj_option: dict):
+        for k in raw_obj_option:
+            if type(raw_obj_option[k]) is list:
+                assert len(raw_obj_option[k]) >= len(self.records)
+                raw_obj_option[k] = raw_obj_option[k][:len(self.records)]
+            else:
+                raw_obj_option[k] = [raw_obj_option[k] for _ in self.records]
+        return [{k:v[i] for k,v in raw_obj_option.items()} for i in range(len(self.records))]
 
 ############################# Table ##############################
 def min_value(record,  col_option):
+    r"""
+    Get minimal value. The col_option should be like
+        {'x': key of record.data}
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     return np.min(record.data[col_option['x']])
 
 def max_value(record,  col_option):
+    r"""
+    Get maximal value.The col_option should be like
+        {'x': key of record.data}
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     return np.max(record.data[col_option['x']])
 
 def variance(record, col_option):
+    r"""
+    Get variance. The col_option should be like
+        {'x': key of record.data}
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     return np.var(record.data[col_option['x']])
 
 def std_value(record, col_option):
+    r"""
+    Get standard deviation. The col_option should be like
+        {'x': key of record.data}
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     return np.std(record.data[col_option['x']])
 
 def mean_value(record, col_option):
+    r"""
+    Get mean value. The col_option should be like
+        {'x': key of record.data}
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     return np.mean(record.data[col_option['x']])
 
 def final_value(record, col_option):
+    r"""
+    Get final value. The col_option should be like
+        {'x': key of record.data}
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     return record.data[col_option['x']][-1]
 
 def optimal_x_by_y(record, col_option):
+    r"""
+    Get the value of y where the value of x is the optimal.
+    The col_option should be like
+        {
+        'x': key of record.data,
+        'y': key of record.data,
+        'flag': 'min' or 'max'
+        }
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     if 'flag' not in col_option.keys(): col_option['flag'] = 'min'
     if col_option['flag']=='min': f = np.argmin
     else: f=np.argmax
     tmp = f(record.data[col_option['y']])
     return record.data[col_option['x']][tmp]
 
 def group_optimal_value(record, col_option):
+    r"""
+    Get the grouped optimal value. The col_option should be like
+        {
+        'x': key of record.data,
+        'flag': 'min' or 'max'
+        }
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     if 'flag' not in col_option.keys(): col_option['flag'] = 'min'
     if col_option['flag']=='min': f = np.min
     else: f=np.max
     minvs = np.array([f(rdata[col_option['x']]) for rdata in record.datas])
     mean_v = np.mean(minvs)
     std_v = np.std(minvs)
     return "{:.4f} ± {:.4f}".format(mean_v, std_v)
 
 def group_optimal_x_by_y(record, col_option):
+    r"""
+    Get the grouped value of y where the grouped value of x is the optimal.
+    The col_option should be like
+        {
+        'x': key of record.data,
+        'y': key of record.data,
+        'flag': 'min' or 'max'
+        }
+
+    Args:
+        record (Record): the record
+        col_option (dict): column option
+
+    Returns:
+        the column value
+    """
     if 'flag' not in col_option.keys(): col_option['flag'] = 'min'
     if col_option['flag']=='min': f = np.argmin
     else: f=np.argmax
     vs = []
     for rdata in record.datas:
         tmp = f(rdata[col_option['y']])
         vs.append(rdata[col_option['x']][tmp])
     mean_v = np.mean(vs)
     std_v = np.std(vs)
     return "{:.4f} ± {:.4f}".format(mean_v, std_v)
 
 class Table:
-    def __init__(self, table_config, records, save_text=False):
-        self.config = table_config
+    r"""
+    Organize the information in records into a table.
+    
+    Args:
+        records (list): a list of instances of Record(...)
+        save_text (bool): whether to store the table into the disk
+        path (str): the storing path
+    """
+    def __init__(self, records:list, save_text:bool=False, path:str='.'):
         self.records = records
         self.save_text = save_text
+        self.path = path
         self.tb = pt.PrettyTable()
+        self.tb.add_column('Task', [r.data['option']['task'] for r in self.records])
         self.tb.add_column('Record', [r.data['label'] for r in self.records])
+        self.tb.float_format = "3.4"
         self.sort_key = None
 
-    def set_title(self, title):
-        self.tb.title = title
-
-    def create_column(self, funcname, col_option):
+    def add_column(self, func, col_option):
+        r"""
+        Add a column to this table. For each record $Record_k$, its value $v_k$
+        in this column is v_k=func(Record_k, col_option), where func can be 
+        arbitrarily customized.
+
+        Args:
+            func (func|str): the name of the function or the function
+            col_option (dict|str): the option of the column to index data in each record
+
+        Example::
+            >>> tb = Table(records)
+            >>> tb.add_column(min_value, col_option={'x':'valid_loss'})
+            >>> tb.print()
+        """
+        func = eval(func) if type(func) is str else func
+        col_option = {'x': col_option} if type(col_option) is not dict else col_option
         column = []
         for rec in self.records:
-            column.append(eval(funcname+'(rec, col_option)'))
+            column.append(func(rec, col_option))
         if 'name' in col_option.keys():
             fieldname = col_option['name']
         else:
             fieldname = '-'.join([str(v) for k,v in col_option.items() if k!='sort'])
-            fieldname = funcname + '-' + fieldname
+            fieldname = func.__name__ + '-' + fieldname
         self.tb.add_column(fieldname=fieldname, column=column)
         if 'sort' in col_option.keys(): self.tb.sortby = fieldname
 
-    def run(self, group=False):
-        for funcname in self.config:
-            con1 = funcname.startswith('group') and group
-            con2 = not funcname.startswith('group') and not group
-            if con1 or con2:
-                col_options = self.config[funcname]
-                if type(col_options) is not list: col_options = [col_options]
-                for col in col_options:
-                    if type(col) is not dict: col_option = {'x': col_option}
-                    else: col_option = col
-                    self.create_column(funcname, col_option)
-        self.tb.float_format = "3.4"
-        print(self.tb)
-
-#################################################################
-def read_option():
-    parser = argparse.ArgumentParser()
-    parser.add_argument('--config', help='the configuration of result analysis;', type=str, default='res_config.yml')
-    parser.add_argument('--save_figure', help='set True to save the plotted figures', action="store_true", default=False)
-    parser.add_argument('--save_text', help='set True to save the printed tables', type=float, default=0)
-    parser.add_argument('--seed', help='seed for random initialization;', type=int, default=0)
-    try: option = vars(parser.parse_args())
-    except IOError as msg: parser.error(str(msg))
-    random.seed(option['seed'])
-    np.random.seed(option['seed'])
-    return option
+    def set_title(self, title):
+        self.tb.title = title
 
-def show(config, save_figure=False, save_text=False, seed=0):
+    def print(self):
+        r"""Print and store the table"""
+        if self.save_text:
+            with open(os.path.join(self.path, str(uuid.uuid4())+'.txt'), 'w') as outf:
+                outf.write(self.tb.__repr__())
+        print(self)
+
+    def __repr__(self):
+        return self.tb.__repr__()
+
+def show(config, save_figure=False, save_text=False, path='.', seed=0):
+    r"""
+    Show the results according to analysis configuration.
+
+    Args:
+        config (dict|str): the analysis plan
+        save_figure (bool): whether to save figures
+        save_text (bool): whether to save table as .txt file
+        path (str): the path to store the results
+        seed (int): random seed
+
+    Example::
+        >>> import flgo.experiment.analyzer as al
+        >>> # only records of fedavg running on the task 'my_task' with learning rate lr<=0.01 will be selected
+        >>> selector_config = {'task':'./my_task', 'header':['fedavg'], 'filter':['LR':'<=0.1']}
+        >>> # draw the learning curve on the validation dataset
+        >>> painter_config = {'Curve':[{'args':{'x':'communication_round', 'y':'valid_loss'}}]}
+        >>> # show the minimal value of validation loss
+        >>> table_config = {'min_value':[{'x':'valid_loss'}]}
+        >>> # create analysis plan
+        >>> analysis_plan = {'Selector':selector_config, 'Painter':painter_config, 'Table':table_config}
+        >>> # call this function
+        >>> al.show(analysis_plan)
+    """
+    random.seed(seed)
+    np.random.seed(seed)
     option = load_configuration(config)
-    # with open(config) as f:
-    #     option = yaml.load(f, Loader=yaml.FullLoader)
     record_selector = Selector(option['Selector'])
     if 'Painter' in option.keys():
-        for task in record_selector.records:
-            p = Painter(option['Painter'], record_selector.records[task])
-            p.run()
-        for task in record_selector.grouped_records:
-            p = Painter(option['Painter'], record_selector.grouped_records[task])
-            p.run(group=True)
+        painter = Painter(record_selector.all_records, save_figure=save_figure, path=path)
+        group_painter = Painter(record_selector.grouped_records, save_figure=save_figure, path=path)
+        for object_class_string in option['Painter'].keys():
+            figs = option['Painter'][object_class_string] if type(option['Painter'][object_class_string]) is list else [option['Painter'][object_class_string]]
+            grouped = ('Group' in object_class_string)
+            p = group_painter if grouped else painter
+            for fig_config in figs:
+                p.create_figure(object_class_string, fig_config)
+
     if 'Table' in option.keys():
-        for task in record_selector.records:
-            tb = Table(option['Table'], record_selector.records[task])
-            tb.set_title(task)
-            tb.run()
-        for task in record_selector.grouped_records:
-            tb = Table(option['Table'], record_selector.grouped_records[task])
-            tb.set_title(task)
-            tb.run(group=True)
-
-if __name__ == '__main__':
-    option = read_option()
-    with open(option['config']) as f:
-        cfg = yaml.load(f, Loader=yaml.FullLoader)
-    record_selector = Selector(cfg['Selector'])
-    if 'Painter' in cfg.keys():
-        for task in record_selector.records:
-            p = Painter(cfg['Painter'], record_selector.records[task])
-            p.run()
-        for task in record_selector.grouped_records:
-            p = Painter(cfg['Painter'], record_selector.grouped_records[task])
-            p.run(group=True)
-    if 'Table' in cfg.keys():
-        for task in record_selector.records:
-            tb = Table(cfg['Table'], record_selector.records[task])
-            tb.set_title(task)
-            tb.run()
-        for task in record_selector.grouped_records:
-            tb = Table(cfg['Table'], record_selector.grouped_records[task])
-            tb.set_title(task)
-            tb.run(group=True)
+        tb = Table(record_selector.all_records, save_text=save_text, path=path)
+        group_tb = Table(record_selector.grouped_records, save_text=save_text, path=path)
+        for funcname in option['Table']:
+            columns = option['Table'][funcname] if type(option['Table'][funcname]) is list else [option['Table'][funcname]]
+            grouped = ('group' in funcname)
+            ctb = group_tb if grouped else tb
+            for col_option in columns:
+                ctb.add_column(funcname, col_option)
+        tb.print()
+        group_tb.print()
```

### Comparing `flgo-0.0.7/src/flgo/experiment/logger/__init__.py` & `flgo-0.0.8/src/flgo/experiment/logger/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -2133,14 +2133,15 @@
     def __init__(self, task, option, *args, **kwargs):
         self.task_path = task
         self.option = option
         super(BasicLogger, self).__init__(*args, **kwargs)
         self.output = collections.defaultdict(list)
         self.output['option'] = option
         self.current_round = -1
+        self.objects = []
         self.temp = "{:<30s}{:.4f}"
         self.time_costs = []
         self.time_buf = {}
         self.formatter = Formatter('%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s')
         self.handler_list = []
         self.overwrite = not self.option['no_overwrite']
         if not self.option['no_log_console']:
@@ -2178,14 +2179,15 @@
     def time_end(self, key=''):
         """Create a timestamp that ends the event 'key' and print the time interval of the event."""
         if key not in [k for k in self.time_buf.keys()]:
             raise RuntimeError("Timer end before start.")
         else:
             self.time_buf[key][-1] = time.time() - self.time_buf[key][-1]
             self.info("{:<30s}{:.4f}".format(key + ":", self.time_buf[key][-1]) + 's')
+            return self.time_buf[key][-1]
 
     def save_output_as_json(self, filepath=None):
         """Save the self.output as .json file"""
         if len(self.output) == 0: return
         self.organize_output()
         self.output_to_jsonable_dict()
         if filepath is None:
@@ -2312,20 +2314,20 @@
         # calculate the testing metrics on testing dataset owned by coordinator
         test_metric = self.coordinator.test()
         for met_name, met_val in test_metric.items():
             self.output['test_' + met_name].append(met_val)
         # calculate weighted averaging of metrics on training datasets across participants
         local_data_vols = [c.datavol for c in self.participants]
         total_data_vol = sum(local_data_vols)
-        train_metrics = self.coordinator.global_test('train')
+        train_metrics = self.coordinator.global_test(flag='train')
         for met_name, met_val in train_metrics.items():
             self.output['train_' + met_name + '_dist'].append(met_val)
             self.output['train_' + met_name].append(1.0 * sum([client_vol * client_met for client_vol, client_met in zip(local_data_vols, met_val)]) / total_data_vol)
         # calculate weighted averaging and other statistics of metrics on validation datasets across clients
-        valid_metrics = self.coordinator.global_test('valid')
+        valid_metrics = self.coordinator.global_test(flag='valid')
         for met_name, met_val in valid_metrics.items():
             self.output['valid_'+met_name+'_dist'].append(met_val)
             self.output['valid_' + met_name].append(1.0 * sum([client_vol * client_met for client_vol, client_met in zip(local_data_vols, met_val)]) / total_data_vol)
             self.output['mean_valid_' + met_name].append(np.mean(met_val))
             self.output['std_valid_' + met_name].append(np.std(met_val))
         # output to stdout
         self.show_current_output()
```

### Comparing `flgo-0.0.7/src/flgo/experiment/logger/config.py` & `flgo-0.0.8/src/flgo/experiment/logger/config.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/experiment/logger/handlers.py` & `flgo-0.0.8/src/flgo/experiment/logger/handlers.py`

 * *Files identical despite different names*

### Comparing `flgo-0.0.7/src/flgo/experiment/logger/simple_logger.py` & `flgo-0.0.8/src/flgo/experiment/logger/simple_logger.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 from flgo.experiment.logger import BasicLogger
 import numpy as np
-import flgo.system_simulator.base as ss
+import flgo.simulator.base as ss
 
 class SimpleLogger(BasicLogger):
+    r"""Simple Logger. Only evaluating model performance on testing dataset and validation dataset."""
     def initialize(self):
         """This method is used to record the stastic variables that won't change across rounds (e.g. local data size)"""
         for c in self.participants:
             self.output['client_datavol'].append(len(c.train_data))
 
     """This logger only records metrics on validation dataset"""
     def log_once(self, *args, **kwargs):
         self.info('Current_time:{}'.format(self.clock.current_time))
         self.output['time'].append(self.clock.current_time)
         test_metric = self.coordinator.test()
         for met_name, met_val in test_metric.items():
             self.output['test_' + met_name].append(met_val)
-        valid_metrics = self.coordinator.global_test('valid')
+        valid_metrics = self.coordinator.global_test(flag='valid')
         local_data_vols = [c.datavol for c in self.participants]
         total_data_vol = sum(local_data_vols)
         for met_name, met_val in valid_metrics.items():
             self.output['valid_'+met_name+'_dist'].append(met_val)
             self.output['valid_' + met_name].append(1.0 * sum([client_vol * client_met for client_vol, client_met in zip(local_data_vols, met_val)]) / total_data_vol)
             self.output['mean_valid_' + met_name].append(np.mean(met_val))
             self.output['std_valid_' + met_name].append(np.std(met_val))
```

### Comparing `flgo-0.0.7/src/flgo/experiment/logger/tune_logger.py` & `flgo-0.0.8/src/flgo/experiment/logger/vertical_logger.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,22 +1,20 @@
 from flgo.experiment.logger import BasicLogger
 
-import numpy as np
-
-class TuneLogger(BasicLogger):
-    def __init__(self,  task, option,*args, **kwargs):
-        super().__init__(task, option, *args, **kwargs)
+class VerticalLogger(BasicLogger):
+    r"""Vertical Logger. Vertical FL should use this Logger"""
+    def initialize(self):
+        """This method is used to record the stastic variables that won't change across rounds (e.g. local data size)"""
+        for c in self.participants:
+            self.output['client_datavol'].append(len(c.train_data))
 
     """This logger only records metrics on validation dataset"""
     def log_once(self, *args, **kwargs):
-        if self.scene == 'horizontal':
-            valid_metrics = self.coordinator.global_test('valid')
-            local_data_vols = [c.datavol for c in self.participants]
-            total_data_vol = sum(local_data_vols)
-            for met_name, met_val in valid_metrics.items():
-                self.output['valid_' + met_name].append(1.0 * sum([client_vol * client_met for client_vol, client_met in zip(local_data_vols, met_val)]) / total_data_vol)
-        elif self.scene == 'vertical':
-            valid_metrics = self.coordinator.test('valid')
-            for met_name, met_val in valid_metrics.items():
-                self.output['valid_' + met_name].append(met_val)
-        # output to stdout
+        self.info('Current_time:{}'.format(self.clock.current_time))
+        self.output['time'].append(self.clock.current_time)
+        test_metric = self.coordinator.test('test')
+        valid_metric = self.coordinator.test('valid')
+        for met_name, met_val in test_metric.items():
+            self.output['test_' + met_name].append(met_val)
+        for met_name, met_test in valid_metric.items():
+            self.output['valid_' + met_name].append(met_val)
         self.show_current_output()
```

### Comparing `flgo-0.0.7/src/flgo/system_simulator/__init__.py` & `flgo-0.0.8/src/flgo/simulator/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -9,15 +9,15 @@
                     upload imcomplete model updates (i.e. only training for a few steps).
     4) connectivity: the clients who promise to complete training may suffer accidients so that the server may lose
                     connections with these client who will never return the currently trained local model.
 We build up a client state machine to simulate the four types of system heterogeneity, and provide high-level
 APIs to allow customized system heterogeneity simulation.
 
 Example 1: How to customize the system heterogeneity?
->>> class MySimulator(flgo.system_simulator.base.BasicSimulator):
+>>> class MySimulator(flgo.simulator.base.BasicSimulator):
 ...     def update_client_availability(self):
 ...         # update the variable 'prob_available' and 'prob_unavailable' for all the clients
 ...         self.set_variable(self.all_clients, 'prob_available', [0.9 for _ in self.all_clients])
 ...         self.set_variable(self.all_clients, 'prob_unavailable', [0.1 for _ in self.all_clients])
 ...
 ...     def update_client_connectivity(self, client_ids):
 ...         # update the variable 'prob_drop' for clients in client_ids
@@ -30,11 +30,11 @@
 ...     def update_client_completeness(self, client_ids, *args, **kwargs):
 ...         # update the variable 'working_amount' for clients in client_ids
 ...         self.set_variable(client_ids, 'working_amount',  [max(int(self.clients[cid].num_steps*np.random.rand()), 1) for cid in client_ids])
 >>> r = flgo.init(task, algorithm=fedavg, Simulator=MySimulator)
 >>> # The runner r will be runned under the customized system heterogeneity, where the clients' states will be flushed by
 >>> # MySimulator.update_client_xxx at each moment of the virtual clock or particular events happen (i.e. a client was selected)
 
-We also provide some preset Simulator like flgo.system_simulator.DefaultSimulator and flgo.system_simulator.
+We also provide some preset Simulator like flgo.simulator.DefaultSimulator and flgo.simulator.
 """
-from flgo.system_simulator.default_simulator import Simulator as DefaultSimulator
-from flgo.system_simulator.phone_simulator import Simulator as PhoneSimulator
+from flgo.simulator.default_simulator import Simulator as DefaultSimulator
+from flgo.simulator.phone_simulator import Simulator as PhoneSimulator
```

### Comparing `flgo-0.0.7/src/flgo/system_simulator/default_simulator.py` & `flgo-0.0.8/src/flgo/simulator/default_simulator.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,44 @@
-from flgo.system_simulator.base import BasicSimulator
+r"""
+This simulator supports for the following system heterogeneity:
+
+availability_modes = {
+    'IDL': ideal_client_availability,
+    'YMF': y_max_first_client_availability,
+    'MDF': more_data_first_client_availability,
+    'LDF': less_data_first_client_availability,
+    'YFF': y_fewer_first_client_availability,
+    'HOMO': homogeneous_client_availability,
+    'LN': lognormal_client_availability,
+    'SLN': sin_lognormal_client_availability,
+    'YC': y_cycle_client_availability,
+}
+
+connectivity_modes = {
+    'IDL': ideal_client_connectivity,
+    'HOMO': homogeneous_client_connectivity,
+}
+
+completeness_modes = {
+    'IDL': ideal_client_completeness,
+    'PDU': part_dynamic_uniform_client_completeness,
+    'FSU': full_static_unifrom_client_completeness,
+    'ADU': arbitrary_dynamic_unifrom_client_completeness,
+    'ASU': arbitrary_static_unifrom_client_completeness,
+}
+
+responsiveness_modes = {
+    'IDL': ideal_client_responsiveness,
+    'LN': lognormal_client_responsiveness,
+    'UNI': uniform_client_responsiveness,
+}
+
+"""
+
+from flgo.simulator.base import BasicSimulator
 import random
 import numpy as np
 import collections
 
 ################################### Initial Availability Mode ##########################################
 def ideal_client_availability(simulator, *args, **kwargs):
     probs1 = [1. for _ in simulator.clients]
```

### Comparing `flgo-0.0.7/src/flgo/system_simulator/my_simulator.py` & `flgo-0.0.8/src/flgo/simulator/my_simulator.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from flgo.system_simulator.base import BasicSimulator
+from flgo.simulator.base import BasicSimulator
 import numpy as np
 class Simulator(BasicSimulator):
     def update_client_connectivity(self, client_ids):
         probs = [0.1 for _ in client_ids]
         self.set_variable(client_ids, 'prob_drop', probs)
 
     def update_client_availability(self):
```

### Comparing `flgo-0.0.7/src/flgo/system_simulator/phone_simulator.py` & `flgo-0.0.8/src/flgo/simulator/phone_simulator.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 import copy
-from flgo.system_simulator.base import BasicSimulator
+from flgo.simulator.base import BasicSimulator
 import os
 import zipfile
 import pandas as pd
 import urllib
 import numpy as np
 import re
 import random
```

### Comparing `flgo-0.0.7/src/flgo/utils/fflow.py` & `flgo-0.0.8/src/flgo/utils/fflow.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,79 +1,102 @@
 import collections
+import sys
 import copy
 import multiprocessing
-import signal
 import time
+import itertools
+import argparse
+import importlib
+import random
+import os
+import os.path
+import warnings
+try:
+    import ujson as json
+except:
+    import json
 try:
     from collections import Iterable
 except ImportError:
     from collections.abc import Iterable
+
 import numpy as np
 import torch
-import os.path
-import json
-import flgo.system_simulator
-import flgo.system_simulator.default_simulator
-import flgo.system_simulator.base
+try:
+    import yaml
+except ModuleNotFoundError:
+    warnings.warn("Module pyyaml is not installed. The configuration cannot be loaded by .yml file.")
+
+import flgo.simulator
+import flgo.simulator.default_simulator
+import flgo.simulator.base
 import flgo.utils.fmodule
 import flgo.experiment.logger.simple_logger
 import flgo.experiment.logger.tune_logger
 import flgo.experiment.logger.vertical_logger
 import flgo.experiment.logger
 import flgo.experiment.device_scheduler
-from flgo.system_simulator.base import BasicSimulator
+from flgo.simulator.base import BasicSimulator
 import flgo.benchmark.toolkits.partition
 import flgo.algorithm
-import itertools
-import argparse
-import importlib
-import random
-import os
-import warnings
-try:
-    import yaml
-except ModuleNotFoundError:
-    warnings.warn("Module pyyaml is not installed. The configuration cannot be loaded by .yml file.")
-import sys
 
-sample_list=['uniform', 'md', 'full', 'uniform_available', 'md_available', 'full_available']
-agg_list=['uniform', 'weighted_scale', 'weighted_com']
-optimizer_list=['SGD', 'Adam', 'RMSprop', 'Adagrad']
-default_option_dict = {'pretrain': '', 'sample': 'md', 'aggregate': 'uniform', 'num_rounds': 20, 'proportion': 0.2, 'learning_rate_decay': 0.998, 'lr_scheduler': -1, 'early_stop': -1, 'num_epochs': 5, 'num_steps': -1, 'learning_rate': 0.1, 'batch_size': 64.0, 'optimizer': 'SGD', 'momentum': 0, 'weight_decay': 0, 'algo_para': [], 'train_holdout': 0.1, 'test_holdout': 0.0, 'seed': 0, 'gpu': [], 'server_with_cpu': False, 'num_parallels': 1, 'num_workers': 0, 'pin_memory':False,'test_batch_size': 512, 'simulator': 'default_simulator', 'availability': 'IDL', 'connectivity': 'IDL', 'completeness': 'IDL', 'responsiveness': 'IDL', 'logger': 'basic_logger', 'log_level': 'INFO', 'log_file': False, 'no_log_console': False, 'no_overwrite': False, 'eval_interval': 1}
+
+sample_list=['uniform', 'md', 'full', 'uniform_available', 'md_available', 'full_available'] # sampling options for the default sampling method in flgo.algorihtm.fedbase
+agg_list=['uniform', 'weighted_scale', 'weighted_com'] # aggregation options for the default aggregating method in flgo.algorihtm.fedbase
+optimizer_list=['SGD', 'Adam', 'RMSprop', 'Adagrad'] # supported optimizers
+default_option_dict = {'pretrain': '', 'sample': 'md', 'aggregate': 'uniform', 'num_rounds': 20, 'proportion': 0.2, 'learning_rate_decay': 0.998, 'lr_scheduler': -1, 'early_stop': -1, 'num_epochs': 5, 'num_steps': -1, 'learning_rate': 0.1, 'batch_size': 64.0, 'optimizer': 'SGD', 'momentum': 0, 'weight_decay': 0, 'algo_para': [], 'train_holdout': 0.1, 'test_holdout': 0.0, 'local_test':False,'seed': 0, 'gpu': [], 'server_with_cpu': False, 'num_parallels': 1, 'num_workers': 0, 'pin_memory':False,'test_batch_size': 512,'pin_memory':False ,'simulator': 'default_simulator', 'availability': 'IDL', 'connectivity': 'IDL', 'completeness': 'IDL', 'responsiveness': 'IDL', 'logger': 'basic_logger', 'log_level': 'INFO', 'log_file': False, 'no_log_console': False, 'no_overwrite': False, 'eval_interval': 1}
 
 class GlobalVariable:
-    """this class is to create a buffer space for sharing variables across different parties for each runner respectively in a single machine"""
+    """This class is to create a shared space for sharing variables across
+    different parties for each runner"""
+
     def __init__(self):
         self.logger = None
         self.simulator = None
         self.clock = None
         self.dev_list = None
         self.TaskCalculator = None
         self.TaskPipe = None
         self.crt_dev = 0
 
     def apply_for_device(self):
-        """apply for a new device from currently available ones (i.e. devices in self.dev_list)"""
+        r"""
+        Apply for a new device from currently available ones (i.e. devices in self.dev_list)
+
+        Returns:
+            GPU device (i.e. torch.device)
+        """
         if self.dev_list is None: return None
         dev = self.dev_list[self.crt_dev]
         self.crt_dev = (self.crt_dev + 1) % len(self.dev_list)
         return dev
 
 def setup_seed(seed):
-    """fix all the random seed used in numpy, torch and random module"""
+    r"""
+    Fix all the random seed used in numpy, torch and random module
+
+    Args:
+        seed (int): the random seed
+    """
     random.seed(1+seed)
     np.random.seed(21+seed)
     os.environ['PYTHONHASHSEED'] = str(seed)
     torch.manual_seed(12+seed)
     torch.cuda.manual_seed_all(123+seed)
     torch.backends.cudnn.enabled = False
     torch.backends.cudnn.deterministic = True
 
 def read_option_from_command():
-    """load configuration for flgo.init from command lines"""
+    r"""
+    Generate running-time configurations for flgo.init with default values from command lines
+
+    Returns:
+        a dict of option (i.e. configuration)
+    """
+
     parser = argparse.ArgumentParser()
     """Training Options"""
     # basic settings
     # methods of server side for sampling and aggregating
     parser.add_argument('--sample', help='methods for sampling clients', type=str, choices=sample_list, default='md')
     parser.add_argument('--aggregate', help='methods for aggregating models', type=str, choices=agg_list, default='uniform')
     # hyper-parameters of training in server side
@@ -125,36 +148,46 @@
     except IOError as msg: parser.error(str(msg))
     for key in option.keys():
         if option[key] is None:
             option[key]=[]
     return option
 
 def load_configuration(config={}):
-    """load configuration for yml file or dict"""
+    r"""
+    Load configurations from .yml file or dict.
+
+    Args:
+        config (dict|str): the configurations
+
+    Returns:
+        a dict of option (i.e. configuration)
+    """
     if type(config) is str and config.endswith('.yml'):
         with open(config) as f:
             option = yaml.load(f, Loader=yaml.FullLoader)
         return option
     elif type(config) is dict:
         return config
+    else:
+        raise TypeError('The input config should be either a dict or a filename.')
 
 def gen_task_by_para(benchmark, bmk_para:dict={}, Partitioner=None, par_para:dict={}, task_path: str='', rawdata_path:str='', seed:int=0):
     r"""
     Generate a federated task according to the parameters of this function. The formats and meanings of the inputs are listed as below:
 
-        benchmark (python package || str): the benchmark package or the module path of it
+    Args:
+        benchmark (package|str): the benchmark package or the module path of it
         bmk_para (dict): the customized parameter dict of the method TaskGenerator.__init__() of the benchmark
-        Partitioner (class || str): the class of the Partitioner or the name of the Partitioner that was realized in flgo.benchmark.toolkits.partition
+        Partitioner (flgo.benchmark.toolkits.partition.BasicPartitioner|str): the class of the Partitioner or the name of the Partitioner that was realized in flgo.benchmark.toolkits.partition
         par_para (dict): the customized parameter dict of the method Partitioner.__init__()
         task_path (str): the path to store the generated task
         rawdata_path (str): where the raw data will be downloaded\stored
         seed (int): the random seed used to generate the task
-    Returns:
 
-    Example:
+    Example::
         >>> import flgo
         >>> import flgo.benchmark.mnist_classification as mnist
         >>> from flgo.benchmark.toolkits.partition import IIDPartitioner
         >>> # GENERATE TASK BY PASSING THE MODULE OF BENCHMARK AND THE CLASS OF THE PARTITIOENR
         >>> flgo.gen_task_by_para(benchmark=mnist, Partitioner = IIDPartitioner, par_para={'num_clients':100}, task_path='./mnist_gen_by_para1')
         >>> # GENERATE THE SAME TASK BY PASSING THE STRING
         >>> flgo.gen_task_by_para(benchmark='flgo.benchmark.mnist_classification', Partitioner='IIDPartitioner', par_para={'num_clients':100}, task_path='./mnist_gen_by_para2')
@@ -196,30 +229,28 @@
     except Exception as e:
         print(e)
         task_pipe.remove_task()
         print("Failed to saving splited dataset.")
     # save visualization
     try:
         visualize_func = getattr(benchmark,'visualize')
-        visualize_func(task_generator, partitioner)
-        task_pipe.save_figure()
+        visualize_func(task_generator, partitioner, task_path)
     except:
         pass
 
 def gen_task_by_config(config={}, task_path:str='', rawdata_path:str='', seed:int=0):
     r"""
     Generate a federated task that is specified by the benchmark information and the partition information, where the generated task will be stored in the task_path and the raw data will be downloaded into the rawdata_path.
 
         config (dict || str): configuration is either a dict contains parameters or a filename of a .yml file
         task_path (str): where the generated task will be stored
         rawdata_path (str): where the raw data will be downloaded\stored
         seed (int): the random seed used to generate the task
-    Returns:
 
-    Example:
+    Example::
         >>> import flgo
         >>> config = {'benchmark':{'name':'flgo.benchmark.mnist_classification'}, 'partitioner':{'name':'IIDParitioner', 'para':{'num_clients':100}}}
         >>> flgo.gen_task(config, './my_mnist_iid')
         >>> # The task will be stored as `my_mnist_iid` in the current working dictionary
     """
     # setup random seed
     random.seed(3 + seed)
@@ -237,15 +268,15 @@
             if 'name' not in gen_option['partitioner'].keys():
                 gen_option['benchmark']['para'].update(gen_option['partitioner']['para'])
     # init generator
     if rawdata_path!='': gen_option['benchmark']['para']['rawdata_path']=rawdata_path
     if type(gen_option['benchmark']['name']) is str:
         bmk_core = importlib.import_module('.'.join([gen_option['benchmark']['name'], 'core']))
     elif hasattr(gen_option['benchmark']['name'], '__path__'):
-        bmk_core = gen_option['benchmark']['name'].core
+        bmk_core = getattr(gen_option['benchmark']['name'],'core')
     else:
         raise RuntimeError("The value of parameter config['benchmark']['name'] should be either a string or a python package.")
     task_generator = getattr(bmk_core, 'TaskGenerator')(**gen_option['benchmark']['para'])
     # create partitioner for generator if specified
     if 'partitioner' in gen_option.keys() and 'name' in gen_option['partitioner'].keys():
         Partitioner = gen_option['partitioner']['name']
         if type(Partitioner) is str:
@@ -276,34 +307,35 @@
     except Exception as e:
         print(e)
         task_pipe.remove_task()
         print("Failed to saving splited dataset.")
     # save visualization
     try:
         visualize_func = getattr(importlib.import_module(gen_option['benchmark']['name']),'visualize')
-        visualize_func(task_generator, partitioner)
-        task_pipe.save_figure()
+        visualize_func(task_generator, partitioner, task_path)
     except:
         pass
 
-def init(task: str, algorithm, option = {}, model=None, Logger: flgo.experiment.logger.BasicLogger = None, Simulator: BasicSimulator=flgo.system_simulator.DefaultSimulator, scene='horizontal'):
+def init(task: str, algorithm, option = {}, model=None, Logger: flgo.experiment.logger.BasicLogger = None, Simulator: BasicSimulator=flgo.simulator.DefaultSimulator, scene='horizontal'):
     r"""
     Initialize a runner in FLGo, which is to optimize a model on a specific task (i.e. IID-mnist-of-100-clients) by the selected federated algorithm.
 
+    Args:
         task (str): the dictionary of the federated task
-        algorithm (module || class): the algorithm will be used to optimize the model in federated manner, which must contain pre-defined attributions (e.g. algorithm.Server and algorithm.Client for horizontal federated learning)
-        option (dict || str): the configurations of training, environment, algorithm, logger and simulator
-        model (module || class): the model module that contains two methods: model.init_local_module(object) and model.init_global_module(object)
-        Logger (class): the class of the logger inherited from flgo.experiment.logger.BasicLogger
-        Simulator (class): the class of the simulator inherited from flgo.system_simulator.BasicSimulator
+        algorithm (module|class): the algorithm will be used to optimize the model in federated manner, which must contain pre-defined attributions (e.g. algorithm.Server and algorithm.Client for horizontal federated learning)
+        option (dict|str): the configurations of training, environment, algorithm, logger and simulator
+        model (module|class): the model module that contains two methods: model.init_local_module(object) and model.init_global_module(object)
+        Logger (flgo.experiment.logger.BasicLogger): the class of the logger inherited from flgo.experiment.logger.BasicLogger
+        Simulator (flgo.simulator.base.BasicSimulator): the class of the simulator inherited from flgo.simulator.BasicSimulator
         scene (str): 'horizontal' or 'vertical' in current version of FLGo
+
     Returns:
         runner: the object instance that has the method runner.run()
 
-    Example:
+    Example::
         >>> import flgo
         >>> from flgo.algorithm import fedavg
         >>> from flgo.experiment.logger.simple_logger import SimpleLogger
         >>> # create task 'mnist_iid' by flgo.gen_task('gen_config.yml', 'mnist_iid') if there exists no such task
         >>> if os.path.exists('mnist_iid'): flgo.gen_task({'benchmark':{'name':'flgo.benchmark.mnist_classification'}, 'partitioner':{'name':'IIDPartitioner','para':{'num_clients':100}}}, 'mnist_iid')
         >>> # create runner
         >>> fedavg_runner = flgo.init('mnist_iid', algorithm=fedavg, option = {'num_rounds':20, 'gpu':[0], 'learning_rate':0.1})
@@ -371,56 +403,67 @@
             setattr(C, 'gv', gv)
             tmp.append(c)
         except:
             continue
     objects = task_pipe.generate_objects(option, algorithm, scene=scene)
     task_pipe.distribute(task_data, objects)
 
-    for c in tmp:
-        try:
-            C = getattr(algorithm, c)
-            delattr(C, 'gv')
-        except:
-            continue
-
     # init model
     if hasattr(model, 'init_local_module'):
         for object in objects:
             model.init_local_module(object)
     if hasattr(model, 'init_global_module'):
         for object in objects:
             model.init_global_module(object)
 
     # init communicator
     gv.communicator = flgo.VirtualCommunicator(objects)
 
     for ob in objects: ob.initialize()
 
-    # if scene=='horizontal':
-    #     objects[0].__class__.communicate_with = flgo.system_simulator.base.with_latency(objects[0].__class__.communicate_with)
     # init virtual system environment
     gv.logger.info('Use `{}` as the system simulator'.format(str(Simulator)))
-    flgo.system_simulator.base.random_seed_gen = flgo.system_simulator.base.seed_generator(option['seed'])
-    gv.clock = flgo.system_simulator.base.ElemClock()
+    flgo.simulator.base.random_seed_gen = flgo.simulator.base.seed_generator(option['seed'])
+    gv.clock = flgo.simulator.base.ElemClock()
     gv.simulator = Simulator(objects, option)
     gv.clock.register_simulator(simulator=gv.simulator)
 
     gv.logger.register_variable(coordinator=objects[0], participants=objects[1:], option=option, clock=gv.clock, scene=scene, objects = objects)
     gv.logger.initialize()
     gv.logger.info('Ready to start.')
 
     # register global variables for objects
+    for c in tmp:
+        try:
+            C = getattr(algorithm, c)
+            delattr(C, 'gv')
+        except:
+            continue
     for ob in objects:
         ob.gv = gv
     gv.simulator.gv = gv
     gv.clock.gv = gv
     gv.logger.gv = gv
     return objects[0]
 
 def _call_by_process(task, algorithm_name,  opt, model_name, Logger, Simulator, scene, send_end):
+    r"""
+    This function is used to create a seperate child process.
+
+    Args:
+        task (str): the path of the task
+        algorithm_name (str): the module name of algorithm
+        opt (dict): option
+        model_name (str): the module name of model
+        Logger (flgo.experiment.logger.BasicLogger): the class of the logger
+        Simulator (flgo.simulator.base.BasicSimulator): the class of the simulator inherited from flgo.simulator.BasicSimulator
+        scene (str): horizontal or vertical
+        send_end (connection.Connection): the return of multiprocess.Pipe(...) that is used to pass data to the parent process
+    """
+
     pid = os.getpid()
     sys.stdout = open(os.devnull, 'w')
     if model_name is None: model = None
     else:
         try:
             model = importlib.import_module(model_name)
         except:
@@ -435,28 +478,25 @@
         res = (os.path.join(runner.gv.logger.get_output_path(), runner.gv.logger.get_output_name()), pid)
         send_end.send(res)
     except Exception as e:
         s = 'Process {} exits with error:" {}". '.format(pid, str(e))
         res = (opt, s, pid)
         send_end.send(res)
 
-def get_available_device(device_ids):
-    # dev_handlers = [pynvml.nvmlDeviceGetHandleByIndex(dev_id) for dev_id in device_ids]
-    return random.choice(device_ids)
 
-def tune(task: str, algorithm, option: dict = {}, model=None, Logger: flgo.experiment.logger.BasicLogger = flgo.experiment.logger.tune_logger.TuneLogger, Simulator: BasicSimulator=flgo.system_simulator.DefaultSimulator, scene='horizontal', scheduler=None):
+def tune(task: str, algorithm, option: dict = {}, model=None, Logger: flgo.experiment.logger.BasicLogger = flgo.experiment.logger.tune_logger.TuneLogger, Simulator: BasicSimulator=flgo.simulator.DefaultSimulator, scene='horizontal', scheduler=None):
     """
-        Tune hyper-parameters for one task and one algorithm in parallel.
+        Tune hyper-parameters for the specific (task, algorithm, model) in parallel.
         Args:
             task (str): the dictionary of the federated task
-            algorithm (module || class): the algorithm will be used to optimize the model in federated manner, which must contain pre-defined attributions (e.g. algorithm.Server and algorithm.Client for horizontal federated learning)
+            algorithm (module|class): the algorithm will be used to optimize the model in federated manner, which must contain pre-defined attributions (e.g. algorithm.Server and algorithm.Client for horizontal federated learning)
             option (dict): the dict whose values should be of type list to construct the combinations
-            model (module || class): the model module that contains two methods: model.init_local_module(object) and model.init_global_module(object)
+            model (module|class): the model module that contains two methods: model.init_local_module(object) and model.init_global_module(object)
             Logger (class): the class of the logger inherited from flgo.experiment.logger.BasicLogger
-            Simulator (class): the class of the simulator inherited from flgo.system_simulator.BasicSimulator
+            Simulator (class): the class of the simulator inherited from flgo.simulator.BasicSimulator
             scene (str): 'horizontal' or 'vertical' in current version of FLGo
             scheduler (instance of flgo.experiment.device_scheduler.BasicScheduler): GPU scheduler that schedules GPU by checking their availability
         """
     # generate combinations of hyper-parameters
     if 'gpu' in option.keys():
         device_ids = option['gpu']
         option.pop('gpu')
@@ -479,27 +519,29 @@
         if k=='gpu': continue
         print("{}\t|{}".format(k,v))
     print('-----------------------------------------------')
     op_round = np.argmin(outputs[optimal_idx]['valid_loss'])
     if 'eval_interval' in option.keys(): op_round = option['eval_interval']*op_round
     print('The minimal validation loss occurs at the round {}'.format(op_round))
 
-def run_in_parallel(task: str, algorithm, options:list = [], model=None, devices = [], Logger:flgo.experiment.logger.BasicLogger = flgo.experiment.logger.simple_logger.SimpleLogger, Simulator=flgo.system_simulator.DefaultSimulator, scene='horizontal', scheduler = None):
+def run_in_parallel(task: str, algorithm, options:list = [], model=None, devices = [], Logger:flgo.experiment.logger.BasicLogger = flgo.experiment.logger.simple_logger.SimpleLogger, Simulator=flgo.simulator.DefaultSimulator, scene='horizontal', scheduler = None):
     """
     Run different groups of hyper-parameters for one task and one algorithm in parallel.
+
     Args:
         task (str): the dictionary of the federated task
-        algorithm (module || class): the algorithm will be used to optimize the model in federated manner, which must contain pre-defined attributions (e.g. algorithm.Server and algorithm.Client for horizontal federated learning)
+        algorithm (module|class): the algorithm will be used to optimize the model in federated manner, which must contain pre-defined attributions (e.g. algorithm.Server and algorithm.Client for horizontal federated learning)
         options (list): the configurations of different groups of hyper-parameters
-        model (module || class): the model module that contains two methods: model.init_local_module(object) and model.init_global_module(object)
+        model (module|class): the model module that contains two methods: model.init_local_module(object) and model.init_global_module(object)
         devices (list): the list of IDs of devices
         Logger (class): the class of the logger inherited from flgo.experiment.logger.BasicLogger
-        Simulator (class): the class of the simulator inherited from flgo.system_simulator.BasicSimulator
+        Simulator (class): the class of the simulator inherited from flgo.simulator.BasicSimulator
         scene (str): 'horizontal' or 'vertical' in current version of FLGo
         scheduler (instance of flgo.experiment.device_scheduler.BasicScheduler): GPU scheduler that schedules GPU by checking their availability
+
     Returns:
         the returns of _call_by_process
     """
     try:
         # init multiprocess
         torch.multiprocessing.set_start_method('spawn', force=True)
         torch.multiprocessing.set_sharing_strategy('file_system')
@@ -554,21 +596,24 @@
             rec = json.loads(s_inf)
         res.append(rec)
     return res
 
 def multi_init_and_run(runner_args:list, devices = [], scheduler=None):
     r"""
     Create multiple runners and run in parallel
-    param:
+
+    Args:
         runner_args (list): each element in runner_args should be either a dict or a tuple or parameters
         devices (list): a list of gpu id
-        scheduler (class flgo.experiment.device_scheduler.BasicScheduler): GPU scheduler
-    return:
+        scheduler (flgo.experiment.device_scheduler.BasicScheduler(...)): GPU scheduler
+
+    Returns:
         a list of output results of runners
-    Example:
+
+    Example::
         >>> from flgo.algorithm import fedavg, fedprox, scaffold
         >>> # create task 'mnist_iid' by flgo.gen_task if there exists no such task
         >>> task='./mnist_iid'
         >>> if os.path.exists(task): flgo.gen_task({'benchmark':{'name':'flgo.benchmark.mnist_classification'}, 'partitioner':{'name':'IIDPartitioner','para':{'num_clients':100}}}, task)
         >>> algos = [fedavg, fedprox, scaffold]
         >>> flgo.multi_init_and_run([{'task':task, 'algorithm':algo} for algo in algos], devices=[0])
     """
@@ -611,22 +656,22 @@
                 else:
                     model_name = tmp['model']
             tmp['model'] = model_name
             if tmp['Logger'] is None:
                 tmp['Logger'] = flgo.experiment.logger.simple_logger.SimpleLogger
             algorithm_name = tmp['algorithm'].__name__ if (not hasattr(tmp['algorithm'], '__module__') and hasattr(tmp['algorithm'], '__name__')) else tmp['algorithm']
             if tmp['Simulator'] is None:
-                tmp['Simulator'] = flgo.system_simulator.DefaultSimulator
+                tmp['Simulator'] = flgo.simulator.DefaultSimulator
             if tmp['scene'] is None:
                 tmp['scene'] = 'horizontal'
             args.append(list(tmp.values()))
     elif type(runner_args[0]) is tuple or type(runner_args[0]) is list:
         for a in runner_args:
             if len(a)<2: raise RuntimeError('the args of runner should at least contain task and algorithm.')
-            default_args = [None, None, default_option_dict, None, flgo.experiment.logger.simple_logger.SimpleLogger, flgo.system_simulator.DefaultSimulator, 'horizontal']
+            default_args = [None, None, default_option_dict, None, flgo.experiment.logger.simple_logger.SimpleLogger, flgo.simulator.DefaultSimulator, 'horizontal']
             for aid in range(len(a)):
                 if aid==0:
                     default_args[aid] = a[aid]
                 if aid==1:
                     algorithm = a[aid]
                     algorithm_name = algorithm.__name__ if (not hasattr(algorithm, '__module__') and hasattr(algorithm, '__name__')) else algorithm
                     default_args[aid] = algorithm_name
```

### Comparing `flgo-0.0.7/src/flgo.egg-info/SOURCES.txt` & `flgo-0.0.8/src/flgo.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -9,23 +9,25 @@
 src/flgo/algorithm/TiFL.py
 src/flgo/algorithm/__init__.py
 src/flgo/algorithm/afl.py
 src/flgo/algorithm/fedasync.py
 src/flgo/algorithm/fedavg.py
 src/flgo/algorithm/fedbase.py
 src/flgo/algorithm/fedbuff.py
+src/flgo/algorithm/fedfa.py
 src/flgo/algorithm/fedfv.py
 src/flgo/algorithm/fedmgda+.py
 src/flgo/algorithm/fedprox.py
 src/flgo/algorithm/mifa.py
 src/flgo/algorithm/powerofchoice.py
 src/flgo/algorithm/qfedavg.py
 src/flgo/algorithm/scaffold.py
 src/flgo/algorithm/vflbase.py
 src/flgo/benchmark/__init__.py
+src/flgo/benchmark/base.py
 src/flgo/benchmark/cifar100_classification/__init__.py
 src/flgo/benchmark/cifar100_classification/core.py
 src/flgo/benchmark/cifar100_classification/model/cnn.py
 src/flgo/benchmark/cifar100_classification/model/resnet18.py
 src/flgo/benchmark/cifar10_classification/__init__.py
 src/flgo/benchmark/cifar10_classification/core.py
 src/flgo/benchmark/cifar10_classification/model/cnn.py
@@ -83,15 +85,14 @@
 src/flgo/benchmark/svhn_classification/core.py
 src/flgo/benchmark/svhn_classification/model/cnn.py
 src/flgo/benchmark/svhn_classification/model/mlp.py
 src/flgo/benchmark/synthetic_regression/__init__.py
 src/flgo/benchmark/synthetic_regression/core.py
 src/flgo/benchmark/synthetic_regression/model/lr.py
 src/flgo/benchmark/toolkits/__init__.py
-src/flgo/benchmark/toolkits/base.py
 src/flgo/benchmark/toolkits/partition.py
 src/flgo/benchmark/toolkits/visualization.py
 src/flgo/benchmark/toolkits/cv/__init__.py
 src/flgo/benchmark/toolkits/cv/centralize/__init__.py
 src/flgo/benchmark/toolkits/cv/horizontal/__init__.py
 src/flgo/benchmark/toolkits/cv/horizontal/image_classification.py
 src/flgo/benchmark/toolkits/cv/vertical/__init__.py
@@ -112,16 +113,16 @@
 src/flgo/experiment/device_scheduler.py
 src/flgo/experiment/logger/__init__.py
 src/flgo/experiment/logger/config.py
 src/flgo/experiment/logger/handlers.py
 src/flgo/experiment/logger/simple_logger.py
 src/flgo/experiment/logger/tune_logger.py
 src/flgo/experiment/logger/vertical_logger.py
-src/flgo/system_simulator/__init__.py
-src/flgo/system_simulator/base.py
-src/flgo/system_simulator/default_simulator.py
-src/flgo/system_simulator/my_simulator.py
-src/flgo/system_simulator/phone_simulator.py
+src/flgo/simulator/__init__.py
+src/flgo/simulator/base.py
+src/flgo/simulator/default_simulator.py
+src/flgo/simulator/my_simulator.py
+src/flgo/simulator/phone_simulator.py
 src/flgo/utils/__init__.py
 src/flgo/utils/fflow.py
 src/flgo/utils/fmodule.py
 tests/test.py
```

### Comparing `flgo-0.0.7/tests/test.py` & `flgo-0.0.8/tests/test.py`

 * *Files identical despite different names*

