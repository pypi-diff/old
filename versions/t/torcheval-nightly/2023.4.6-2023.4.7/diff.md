# Comparing `tmp/torcheval-nightly-2023.4.6.tar.gz` & `tmp/torcheval-nightly-2023.4.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/torcheval-nightly-2023.4.6.tar", last modified: Thu Apr  6 11:51:52 2023, max compression
+gzip compressed data, was "dist/torcheval-nightly-2023.4.7.tar", last modified: Fri Apr  7 12:04:27 2023, max compression
```

## Comparing `torcheval-nightly-2023.4.6.tar` & `torcheval-nightly-2023.4.7.tar`

### file list

```diff
@@ -1,131 +1,131 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/
--rw-r--r--   0 runner    (1001) docker     (123)     1534 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     8439 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7611 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2735 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)     3158 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/
--rw-r--r--   0 runner    (1001) docker     (123)      681 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/auc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/cat.py
--rw-r--r--   0 runner    (1001) docker     (123)     1758 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/max.py
--rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/mean.py
--rw-r--r--   0 runner    (1001) docker     (123)     1756 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/min.py
--rw-r--r--   0 runner    (1001) docker     (123)     2832 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/sum.py
--rw-r--r--   0 runner    (1001) docker     (123)     4178 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/throughput.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/
--rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16298 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/accuracy.py
--rw-r--r--   0 runner    (1001) docker     (123)    18405 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/auprc.py
--rw-r--r--   0 runner    (1001) docker     (123)    10056 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/auroc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5738 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/binary_normalized_entropy.py
--rw-r--r--   0 runner    (1001) docker     (123)    10899 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/binned_auprc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9472 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/binned_auroc.py
--rw-r--r--   0 runner    (1001) docker     (123)    10216 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/binned_precision_recall_curve.py
--rw-r--r--   0 runner    (1001) docker     (123)    11825 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/confusion_matrix.py
--rw-r--r--   0 runner    (1001) docker     (123)     8384 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/f1_score.py
--rw-r--r--   0 runner    (1001) docker     (123)     8215 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/precision.py
--rw-r--r--   0 runner    (1001) docker     (123)    12720 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/precision_recall_curve.py
--rw-r--r--   0 runner    (1001) docker     (123)     9289 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/recall.py
--rw-r--r--   0 runner    (1001) docker     (123)     7078 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/classification/recall_at_fixed_precision.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/
--rw-r--r--   0 runner    (1001) docker     (123)     2828 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/
--rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3365 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/auc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2227 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/mean.py
--rw-r--r--   0 runner    (1001) docker     (123)     1799 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/sum.py
--rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/throughput.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/
--rw-r--r--   0 runner    (1001) docker     (123)     2755 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    19539 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/accuracy.py
--rw-r--r--   0 runner    (1001) docker     (123)    17027 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/auprc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9916 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/auroc.py
--rw-r--r--   0 runner    (1001) docker     (123)     5890 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binary_normalized_entropy.py
--rw-r--r--   0 runner    (1001) docker     (123)    12104 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binned_auprc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9716 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binned_auroc.py
--rw-r--r--   0 runner    (1001) docker     (123)    10046 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binned_precision_recall_curve.py
--rw-r--r--   0 runner    (1001) docker     (123)    10385 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/confusion_matrix.py
--rw-r--r--   0 runner    (1001) docker     (123)     9917 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/f1_score.py
--rw-r--r--   0 runner    (1001) docker     (123)     9124 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/precision.py
--rw-r--r--   0 runner    (1001) docker     (123)    13183 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/precision_recall_curve.py
--rw-r--r--   0 runner    (1001) docker     (123)     9145 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/recall.py
--rw-r--r--   0 runner    (1001) docker     (123)     6547 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/recall_at_fixed_precision.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/image/
--rw-r--r--   0 runner    (1001) docker     (123)      355 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/image/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2773 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/image/psnr.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3816 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/click_through_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1245 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/frequency.py
--rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/hit_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/num_collisions.py
--rw-r--r--   0 runner    (1001) docker     (123)     2231 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/reciprocal_rank.py
--rw-r--r--   0 runner    (1001) docker     (123)     4128 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/weighted_calibration.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/
--rw-r--r--   0 runner    (1001) docker     (123)      529 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5301 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/mean_squared_error.py
--rw-r--r--   0 runner    (1001) docker     (123)     6327 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/r2_score.py
--rw-r--r--   0 runner    (1001) docker     (123)     1258 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/tensor_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/
--rw-r--r--   0 runner    (1001) docker     (123)      792 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5682 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/bleu.py
--rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/helper.py
--rw-r--r--   0 runner    (1001) docker     (123)     5102 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/perplexity.py
--rw-r--r--   0 runner    (1001) docker     (123)     4134 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/word_error_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3061 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/word_information_lost.py
--rw-r--r--   0 runner    (1001) docker     (123)     3422 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/word_information_preserved.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/image/
--rw-r--r--   0 runner    (1001) docker     (123)      345 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/image/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4490 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/image/psnr.py
--rw-r--r--   0 runner    (1001) docker     (123)    11586 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/metric.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/ranking/
--rw-r--r--   0 runner    (1001) docker     (123)      622 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/ranking/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4246 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/ranking/click_through_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/ranking/hit_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/ranking/reciprocal_rank.py
--rw-r--r--   0 runner    (1001) docker     (123)     5012 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/ranking/weighted_calibration.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/regression/
--rw-r--r--   0 runner    (1001) docker     (123)      423 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/regression/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5107 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/regression/mean_squared_error.py
--rw-r--r--   0 runner    (1001) docker     (123)     6052 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/regression/r2_score.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5089 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/bleu.py
--rw-r--r--   0 runner    (1001) docker     (123)     4720 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/perplexity.py
--rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/word_error_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/word_information_lost.py
--rw-r--r--   0 runner    (1001) docker     (123)     3882 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/text/word_information_preserved.py
--rw-r--r--   0 runner    (1001) docker     (123)    21319 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/toolkit.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/
--rw-r--r--   0 runner    (1001) docker     (123)      822 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9395 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/auroc.py
--rw-r--r--   0 runner    (1001) docker     (123)     8461 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/click_through_rate.py
--rw-r--r--   0 runner    (1001) docker     (123)    10575 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/mean_squared_error.py
--rw-r--r--   0 runner    (1001) docker     (123)    12591 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/normalized_entropy.py
--rw-r--r--   0 runner    (1001) docker     (123)     9601 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/metrics/window/weighted_calibration.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/tools/
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11325 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/tools/flops.py
--rw-r--r--   0 runner    (1001) docker     (123)    27774 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/tools/module_summary.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2680 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/utils/random_data.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval/utils/test_utils/
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/utils/test_utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4501 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/utils/test_utils/dummy_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)    14997 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/utils/test_utils/metric_class_tester.py
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-04-06 11:49:06.000000 torcheval-nightly-2023.4.6/torcheval/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     8439 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4844 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      158 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:51:52.000000 torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/zip-safe
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/
+-rw-r--r--   0 runner    (1001) docker     (123)     1534 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     8439 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     7611 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2735 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)     3158 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/
+-rw-r--r--   0 runner    (1001) docker     (123)      681 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3939 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/auc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2857 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/cat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1758 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/max.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/mean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1756 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/min.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2832 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/sum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4178 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/throughput.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/
+-rw-r--r--   0 runner    (1001) docker     (123)     2580 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16298 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/accuracy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18405 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/auprc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10056 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/auroc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5738 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/binary_normalized_entropy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10899 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/binned_auprc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9472 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/binned_auroc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10216 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/binned_precision_recall_curve.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11825 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/confusion_matrix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8384 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/f1_score.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8215 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/precision.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12720 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/precision_recall_curve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9289 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/recall.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7078 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/classification/recall_at_fixed_precision.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/
+-rw-r--r--   0 runner    (1001) docker     (123)     2828 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/
+-rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3365 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/auc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2227 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/mean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1799 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/sum.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1527 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/throughput.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/
+-rw-r--r--   0 runner    (1001) docker     (123)     2755 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19539 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/accuracy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17027 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/auprc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9916 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/auroc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5890 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binary_normalized_entropy.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12104 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binned_auprc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9716 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binned_auroc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10046 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binned_precision_recall_curve.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10385 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/confusion_matrix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9917 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/f1_score.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9124 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/precision.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13183 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/precision_recall_curve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9145 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/recall.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6547 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/recall_at_fixed_precision.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/image/
+-rw-r--r--   0 runner    (1001) docker     (123)      355 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/image/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2773 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/image/psnr.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3816 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/click_through_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1245 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/frequency.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/hit_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/num_collisions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2231 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/reciprocal_rank.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4128 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/weighted_calibration.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/
+-rw-r--r--   0 runner    (1001) docker     (123)      529 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5301 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/mean_squared_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6327 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/r2_score.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1258 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/tensor_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/
+-rw-r--r--   0 runner    (1001) docker     (123)      792 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5682 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/bleu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2390 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5102 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/perplexity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4134 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/word_error_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3061 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/word_information_lost.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3422 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/word_information_preserved.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/image/
+-rw-r--r--   0 runner    (1001) docker     (123)      345 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/image/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4490 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/image/psnr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11586 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/metric.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/ranking/
+-rw-r--r--   0 runner    (1001) docker     (123)      622 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/ranking/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4246 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/ranking/click_through_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3414 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/ranking/hit_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3519 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/ranking/reciprocal_rank.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5012 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/ranking/weighted_calibration.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/regression/
+-rw-r--r--   0 runner    (1001) docker     (123)      423 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/regression/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5107 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/regression/mean_squared_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6052 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/regression/r2_score.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/
+-rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5089 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/bleu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4720 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/perplexity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3321 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/word_error_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/word_information_lost.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3882 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/text/word_information_preserved.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21319 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/toolkit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/
+-rw-r--r--   0 runner    (1001) docker     (123)      822 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9395 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/auroc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8461 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/click_through_rate.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10575 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/mean_squared_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12591 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/normalized_entropy.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9601 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/metrics/window/weighted_calibration.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11325 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/tools/flops.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27774 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/tools/module_summary.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2680 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/utils/random_data.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval/utils/test_utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/utils/test_utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4501 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/utils/test_utils/dummy_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14997 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/utils/test_utils/metric_class_tester.py
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-04-07 12:01:46.000000 torcheval-nightly-2023.4.7/torcheval/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     8439 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4844 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      158 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 12:04:27.000000 torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/zip-safe
```

### Comparing `torcheval-nightly-2023.4.6/LICENSE` & `torcheval-nightly-2023.4.7/LICENSE`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/PKG-INFO` & `torcheval-nightly-2023.4.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: torcheval-nightly
-Version: 2023.4.6
+Version: 2023.4.7
 Summary: A library for providing a simple interface to create new metrics and an easy-to-use toolkit for metric computations and checkpointing.
 Home-page: https://github.com/pytorch/torcheval
 Author: torcheval team
 Author-email: yicongd@fb.com
 License: BSD-3
 Keywords: pytorch,evaluation,metrics
 Classifier: Development Status :: 2 - Pre-Alpha
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: torcheval-nightly Version: 2023.4.6 Summary: A
+Metadata-Version: 2.1 Name: torcheval-nightly Version: 2023.4.7 Summary: A
 library for providing a simple interface to create new metrics and an easy-to-
 use toolkit for metric computations and checkpointing. Home-page: https://
 github.com/pytorch/torcheval Author: torcheval team Author-email:
 yicongd@fb.com License: BSD-3 Keywords: pytorch,evaluation,metrics Classifier:
 Development Status :: 2 - Pre-Alpha Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Science/Research Classifier: License :: OSI
 Approved :: BSD License Classifier: Programming Language :: Python :: 3
```

### Comparing `torcheval-nightly-2023.4.6/README.md` & `torcheval-nightly-2023.4.7/README.md`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/setup.py` & `torcheval-nightly-2023.4.7/setup.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/auc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/auc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/cat.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/cat.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/max.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/max.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/mean.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/mean.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/min.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/min.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/sum.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/sum.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/aggregation/throughput.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/aggregation/throughput.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/accuracy.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/accuracy.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/auprc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/auprc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/auroc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/auroc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/binary_normalized_entropy.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/binary_normalized_entropy.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/binned_auprc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/binned_auprc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/binned_auroc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/binned_auroc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/binned_precision_recall_curve.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/binned_precision_recall_curve.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/confusion_matrix.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/confusion_matrix.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/f1_score.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/f1_score.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/precision.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/precision.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/precision_recall_curve.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/precision_recall_curve.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/recall.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/recall.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/classification/recall_at_fixed_precision.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/classification/recall_at_fixed_precision.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/auc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/auc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/mean.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/mean.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/sum.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/sum.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/aggregation/throughput.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/aggregation/throughput.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/accuracy.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/accuracy.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/auprc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/auprc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/auroc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/auroc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binary_normalized_entropy.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binary_normalized_entropy.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binned_auprc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binned_auprc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binned_auroc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binned_auroc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/binned_precision_recall_curve.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/binned_precision_recall_curve.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/confusion_matrix.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/confusion_matrix.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/f1_score.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/f1_score.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/precision.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/precision.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/precision_recall_curve.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/precision_recall_curve.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/recall.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/recall.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/classification/recall_at_fixed_precision.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/classification/recall_at_fixed_precision.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/image/psnr.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/image/psnr.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/click_through_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/click_through_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/frequency.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/frequency.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/hit_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/hit_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/num_collisions.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/num_collisions.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/reciprocal_rank.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/reciprocal_rank.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/ranking/weighted_calibration.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/ranking/weighted_calibration.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/mean_squared_error.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/mean_squared_error.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/regression/r2_score.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/regression/r2_score.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/tensor_utils.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/tensor_utils.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/bleu.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/bleu.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/helper.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/helper.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/perplexity.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/perplexity.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/word_error_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/word_error_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/word_information_lost.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/word_information_lost.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/functional/text/word_information_preserved.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/functional/text/word_information_preserved.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/image/psnr.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/image/psnr.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/metric.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/metric.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/ranking/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/ranking/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/ranking/click_through_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/ranking/click_through_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/ranking/hit_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/ranking/hit_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/ranking/reciprocal_rank.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/ranking/reciprocal_rank.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/ranking/weighted_calibration.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/ranking/weighted_calibration.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/regression/mean_squared_error.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/regression/mean_squared_error.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/regression/r2_score.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/regression/r2_score.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/text/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/text/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/text/bleu.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/text/bleu.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/text/perplexity.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/text/perplexity.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/text/word_error_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/text/word_error_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/text/word_information_lost.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/text/word_information_lost.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/text/word_information_preserved.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/text/word_information_preserved.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/toolkit.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/toolkit.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/window/__init__.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/window/__init__.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/window/auroc.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/window/auroc.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/window/click_through_rate.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/window/click_through_rate.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/window/mean_squared_error.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/window/mean_squared_error.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/window/normalized_entropy.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/window/normalized_entropy.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/metrics/window/weighted_calibration.py` & `torcheval-nightly-2023.4.7/torcheval/metrics/window/weighted_calibration.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/tools/flops.py` & `torcheval-nightly-2023.4.7/torcheval/tools/flops.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/tools/module_summary.py` & `torcheval-nightly-2023.4.7/torcheval/tools/module_summary.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/utils/random_data.py` & `torcheval-nightly-2023.4.7/torcheval/utils/random_data.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/utils/test_utils/dummy_metric.py` & `torcheval-nightly-2023.4.7/torcheval/utils/test_utils/dummy_metric.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/utils/test_utils/metric_class_tester.py` & `torcheval-nightly-2023.4.7/torcheval/utils/test_utils/metric_class_tester.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval/version.py` & `torcheval-nightly-2023.4.7/torcheval/version.py`

 * *Files identical despite different names*

### Comparing `torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/PKG-INFO` & `torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: torcheval-nightly
-Version: 2023.4.6
+Version: 2023.4.7
 Summary: A library for providing a simple interface to create new metrics and an easy-to-use toolkit for metric computations and checkpointing.
 Home-page: https://github.com/pytorch/torcheval
 Author: torcheval team
 Author-email: yicongd@fb.com
 License: BSD-3
 Keywords: pytorch,evaluation,metrics
 Classifier: Development Status :: 2 - Pre-Alpha
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: torcheval-nightly Version: 2023.4.6 Summary: A
+Metadata-Version: 2.1 Name: torcheval-nightly Version: 2023.4.7 Summary: A
 library for providing a simple interface to create new metrics and an easy-to-
 use toolkit for metric computations and checkpointing. Home-page: https://
 github.com/pytorch/torcheval Author: torcheval team Author-email:
 yicongd@fb.com License: BSD-3 Keywords: pytorch,evaluation,metrics Classifier:
 Development Status :: 2 - Pre-Alpha Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Science/Research Classifier: License :: OSI
 Approved :: BSD License Classifier: Programming Language :: Python :: 3
```

### Comparing `torcheval-nightly-2023.4.6/torcheval_nightly.egg-info/SOURCES.txt` & `torcheval-nightly-2023.4.7/torcheval_nightly.egg-info/SOURCES.txt`

 * *Files identical despite different names*

