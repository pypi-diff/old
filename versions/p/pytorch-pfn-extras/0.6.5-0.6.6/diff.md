# Comparing `tmp/pytorch-pfn-extras-0.6.5.tar.gz` & `tmp/pytorch-pfn-extras-0.6.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytorch-pfn-extras-0.6.5.tar", last modified: Tue Feb 28 12:34:17 2023, max compression
+gzip compressed data, was "pytorch-pfn-extras-0.6.6.tar", last modified: Thu Apr  6 09:18:57 2023, max compression
```

## Comparing `pytorch-pfn-extras-0.6.5.tar` & `pytorch-pfn-extras-0.6.6.tar`

### file list

```diff
@@ -1,150 +1,201 @@
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.864606 pytorch-pfn-extras-0.6.5/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1068 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/LICENSE
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      290 2023-02-28 12:34:17.864606 pytorch-pfn-extras-0.6.5/PKG-INFO
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2354 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/README.md
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      294 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pyproject.toml
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.540606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1327 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/__init__.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.560606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_cupy/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      410 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_cupy/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)       24 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_cupy/_cupy_stub.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     5181 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_tensor.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      259 2022-04-26 07:32:51.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_torch_version.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)       22 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_version.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     9286 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/config.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1128 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/config_types.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.564606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/cuda/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      226 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/cuda/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2159 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/cuda/_allocator.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.576606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataloaders/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      130 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataloaders/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)       84 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataloaders/dataloader.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1081 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataloaders/utils.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.580606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      246 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1896 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/shared_dataset.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.612606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      550 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1058 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_asmode.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     3901 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_concat.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2150 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_join.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2071 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_slice.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)    10171 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_transform.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2677 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_utils.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      809 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_with_converter.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1735 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/delegate_dataset.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     5345 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/from_data.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)    11172 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/tabular_dataset.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.624606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      302 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1688 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/_dataset_util.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2343 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/_distributed_validation_sampler.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2518 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/_initialize.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     8371 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/engine.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.636606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      386 2022-04-26 07:32:51.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     3917 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/_code_block.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    16860 2022-04-26 07:32:51.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/_handler.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    15822 2022-04-26 07:32:51.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/_logic.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1695 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/logging.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.636606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      747 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/__init__.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.656606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)        0 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     4622 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/ensure_shape.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     3928 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/extended_sequential.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     8081 2022-07-21 07:03:14.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     3109 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy_batchnorm.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2139 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy_conv.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1355 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy_linear.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.664606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/parallel/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)       87 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/parallel/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    13350 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/parallel/distributed.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.696606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      870 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     3645 2022-07-21 07:03:14.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_as_output.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1021 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_constants.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      951 2022-07-21 07:03:14.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_globals.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     3548 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_grad.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    14777 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/annotate.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    17339 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/export_testcase.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1231 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/load.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.700606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/pfto_exporter/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)       60 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/pfto_exporter/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    42285 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/pfto_exporter/export.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     3470 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/strip_large_tensor.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1129 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/symbolic_registry.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     4779 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/unstrip_tensor.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.712606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/profiler/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      360 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/profiler/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2963 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/profiler/_record.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    11611 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/profiler/_time_summary.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)        0 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/py.typed
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    15212 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/reporting.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.724606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      267 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      380 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_map.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      846 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_registry.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    17556 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_runtime.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2572 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_to.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      504 2022-12-02 09:10:40.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/torchscript.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.752606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1026 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     6564 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_evaluator.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1531 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_manager_protocol.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    14943 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_trainer.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      458 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_transform_model.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2929 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_trigger_util.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      716 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_util.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    10467 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extension.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.812606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2520 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    19200 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/_snapshot.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     4490 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/best_value.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    17521 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/evaluator.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1393 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/fail_on_non_number.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    10517 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/log_report.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2579 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/lr_scheduler.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     3666 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/micro_average.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     7484 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/parameter_statistics.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     8454 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/plot_report.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     6878 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/print_report.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2167 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/print_report_notebook.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     6041 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/profile_report.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     4062 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/progress_bar.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     5494 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/progress_bar_notebook.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)    14630 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/slack.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)       81 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/snapshot_writers.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     4372 2022-04-26 07:32:51.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/util.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2023 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/value_observation.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    15270 2022-07-07 07:28:15.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/variable_statistics_plot.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)    27890 2022-08-26 01:23:21.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/manager.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1146 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/metrics.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      493 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/trigger.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.832606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      772 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     5064 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/early_stopping_trigger.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2876 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/interval_trigger.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     2399 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/manual_schedule_trigger.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     5041 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/minmax_value_trigger.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1654 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/once_trigger.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      965 2021-10-26 09:39:17.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/time_trigger.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.840606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/utils/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      110 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/utils/__init__.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     1982 2022-02-10 08:07:42.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/utils/checkpoint.py
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)    27997 2023-02-28 12:32:12.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/utils/comparer.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.860606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)      689 2021-09-30 10:01:36.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/__init__.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     3068 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_parallel_writer.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     5454 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_queue_writer.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     1591 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_simple_writer.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)     2800 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_tensorboard_writer.py
--rw-rw-r--   0 maehashi  (2180) maehashi  (2180)    12856 2022-02-24 07:34:02.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_writer_base.py
-drwxr-xr-x   0 maehashi  (2180) maehashi  (2180)        0 2023-02-28 12:34:17.556606 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras.egg-info/
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      290 2023-02-28 12:34:17.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras.egg-info/PKG-INFO
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)     5499 2023-02-28 12:34:17.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras.egg-info/SOURCES.txt
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)        1 2023-02-28 12:34:17.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras.egg-info/dependency_links.txt
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)       98 2023-02-28 12:34:17.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras.egg-info/requires.txt
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)       19 2023-02-28 12:34:17.000000 pytorch-pfn-extras-0.6.5/pytorch_pfn_extras.egg-info/top_level.txt
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      709 2023-02-28 12:34:17.868605 pytorch-pfn-extras-0.6.5/setup.cfg
--rw-r--r--   0 maehashi  (2180) maehashi  (2180)      802 2022-07-21 07:03:12.000000 pytorch-pfn-extras-0.6.5/setup.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1068 2021-03-09 06:27:52.000000 pytorch-pfn-extras-0.6.6/LICENSE
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      337 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/PKG-INFO
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2354 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/README.md
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      294 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pyproject.toml
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1327 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/__init__.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_cupy/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      410 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_cupy/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       24 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_cupy/_cupy_stub.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5181 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_tensor.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      259 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_torch_version.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       22 2023-04-06 09:18:27.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_version.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     9286 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/config.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1128 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/config_types.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/cuda/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      226 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/cuda/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2159 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/cuda/_allocator.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataloaders/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      130 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataloaders/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       84 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataloaders/dataloader.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1081 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataloaders/utils.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      246 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1896 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/shared_dataset.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      550 2020-09-04 02:31:31.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1058 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_asmode.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3901 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_concat.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2150 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_join.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2071 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_slice.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    10171 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_transform.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2677 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_utils.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      809 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_with_converter.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1735 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/delegate_dataset.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5345 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/from_data.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    11172 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/tabular_dataset.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      302 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1688 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/_dataset_util.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2343 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/_distributed_validation_sampler.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2518 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/_initialize.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     8371 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/engine.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      401 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3917 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/_code_block.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    16860 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/_handler.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    19078 2023-04-06 09:09:10.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/_logic.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1712 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/logging.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      747 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/__init__.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2020-05-12 06:46:24.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     4622 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/ensure_shape.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3928 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/extended_sequential.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     8081 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3109 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy_batchnorm.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2139 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy_conv.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1355 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy_linear.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/parallel/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       87 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/parallel/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    13350 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/parallel/distributed.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.963830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      989 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     4392 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_as_output.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1021 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_constants.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      951 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_globals.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3568 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_grad.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      659 2023-03-06 02:09:36.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_helper.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    21962 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_lax.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    14777 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/annotate.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    17459 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/export_testcase.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1231 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/load.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.963830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/pfto_exporter/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       60 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/pfto_exporter/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    42905 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/pfto_exporter/export.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3470 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/strip_large_tensor.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1129 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/symbolic_registry.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     4784 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/unstrip_tensor.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.963830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/profiler/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      360 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/profiler/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2963 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/profiler/_record.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    11611 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/profiler/_time_summary.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/py.typed
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    15212 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/reporting.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.963830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      267 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1739 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_autocast.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      380 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_map.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      846 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_registry.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    17535 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_runtime.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2572 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_to.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      504 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/torchscript.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.963830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1026 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     6564 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_evaluator.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1531 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_manager_protocol.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    14943 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_trainer.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      458 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_transform_model.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2929 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_trigger_util.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      716 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_util.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    10472 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extension.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2520 2023-03-06 02:09:36.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    19200 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/_snapshot.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     4490 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/best_value.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    17521 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/evaluator.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1393 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/fail_on_non_number.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    10517 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/log_report.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2579 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/lr_scheduler.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3666 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/micro_average.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     7484 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/parameter_statistics.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     8454 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/plot_report.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     6878 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/print_report.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2167 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/print_report_notebook.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     6041 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/profile_report.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     4062 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/progress_bar.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5494 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/progress_bar_notebook.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    14630 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/slack.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       81 2020-05-12 06:46:24.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/snapshot_writers.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     4372 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/util.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2023 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/value_observation.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    15270 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/variable_statistics_plot.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    27923 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/manager.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1146 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/metrics.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      493 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/trigger.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      772 2020-05-12 06:46:24.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5064 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/early_stopping_trigger.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2876 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/interval_trigger.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2399 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/manual_schedule_trigger.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5041 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/minmax_value_trigger.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1654 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/once_trigger.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      965 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/time_trigger.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      110 2023-04-03 06:31:42.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2022-03-04 05:54:25.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/_is_notebook.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2015 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/checkpoint.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    28023 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/comparer.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      689 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3068 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_parallel_writer.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5454 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_queue_writer.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1591 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_simple_writer.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2828 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_tensorboard_writer.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    12856 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_writer_base.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.959830 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras.egg-info/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      337 2023-04-06 09:18:57.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras.egg-info/PKG-INFO
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     8076 2023-04-06 09:18:57.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras.egg-info/SOURCES.txt
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        1 2023-04-06 09:18:57.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras.egg-info/dependency_links.txt
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       98 2023-04-06 09:18:57.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras.egg-info/requires.txt
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)       19 2023-04-06 09:18:57.000000 pytorch-pfn-extras-0.6.6/pytorch_pfn_extras.egg-info/top_level.txt
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      709 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/setup.cfg
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      802 2022-12-27 05:10:31.000000 pytorch-pfn-extras-0.6.6/setup.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.955830 pytorch-pfn-extras-0.6.6/tests/
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2020-05-12 06:46:24.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/__init__.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/cuda_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/cuda_tests/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2869 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/cuda_tests/test_allocator.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataloader_test/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataloader_test/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1147 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataloader_test/test_dataloader.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.967830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2020-09-04 02:31:31.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/__init__.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2020-09-04 02:31:31.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1288 2020-09-04 02:31:31.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/dummy_dataset.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1104 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_asmode.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3022 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_concat.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      650 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_delegate_dataset.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    11731 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_from_data.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2972 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_join.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     7949 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_slice.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2997 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_tabular_dataset.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     7563 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_transform.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     1125 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_with_converter.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      986 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/tabular_tests/test_with_torch_dataloader.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      863 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/dataset_tests/test_shared_dataset.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2020-05-12 06:46:24.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/__init__.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2020-05-12 06:46:24.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     8094 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/test_extended_sequential.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     5685 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/test_lazy.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      963 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/test_lazy_batchnorm.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      926 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/test_lazy_conv.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      405 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/modules_tests/test_lazy_linear.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/parallel_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/parallel_tests/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     9362 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/nn_tests/parallel_tests/test_distributed.py
+drwxrwxr-x   0 ecastill  (2428) ecastill  (2428)        0 2023-04-06 09:18:57.971830 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/profiler_tests/
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)        0 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/profiler_tests/__init__.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     2816 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/profiler_tests/test_time_summary.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     9794 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_config.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3386 2021-07-29 07:52:35.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_config_types.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    19653 2023-04-06 07:19:19.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_handler.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      695 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_logging.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)    14959 2022-11-01 08:10:34.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_reporter.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)     3002 2023-01-26 08:06:57.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_tensor.py
+-rw-rw-r--   0 ecastill  (2428) ecastill  (2428)      615 2023-01-26 08:07:04.000000 pytorch-pfn-extras-0.6.6/tests/pytorch_pfn_extras_tests/test_writing.py
```

### Comparing `pytorch-pfn-extras-0.6.5/LICENSE` & `pytorch-pfn-extras-0.6.6/LICENSE`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/README.md` & `pytorch-pfn-extras-0.6.6/README.md`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/_tensor.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/_tensor.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/config.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/config.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/config_types.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/config_types.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/cuda/_allocator.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/cuda/_allocator.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataloaders/utils.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataloaders/utils.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/shared_dataset.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/shared_dataset.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_asmode.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_asmode.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_concat.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_concat.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_join.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_join.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_slice.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_slice.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_transform.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_transform.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_utils.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_utils.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/_with_converter.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/_with_converter.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/delegate_dataset.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/delegate_dataset.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/from_data.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/from_data.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/dataset/tabular/tabular_dataset.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/dataset/tabular/tabular_dataset.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/_dataset_util.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/_dataset_util.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/_distributed_validation_sampler.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/_distributed_validation_sampler.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/distributed/_initialize.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/distributed/_initialize.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/engine.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/engine.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/_code_block.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/_code_block.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/_handler.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/_handler.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/handler/_logic.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/handler/_logic.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,27 +1,22 @@
 import contextlib
+import dataclasses
 from typing import Any, Dict, Generator, Iterable, Mapping, Optional
 import warnings
 
-from pytorch_pfn_extras.handler._code_block import forward, update_parameters
-
-_amp_enabled = False
+import torch
 
-
-try:
-    import torch.cuda.amp
-    _amp_enabled = torch.cuda.is_available() and hasattr(
-        torch.cuda.amp, 'autocast')
-except ImportError:
-    pass
+from pytorch_pfn_extras.handler._code_block import forward, update_parameters
+from pytorch_pfn_extras.runtime import _autocast
 
 
+# Deprecated: kept for backward compatibility of user code
 @contextlib.contextmanager
 def torch_autocast(enabled: bool = True) -> Generator[None, None, None]:
-    if _amp_enabled:
+    if _autocast._cuda_amp_available:
         with torch.cuda.amp.autocast(enabled):  # type: ignore[no-untyped-call]
             yield
     else:
         yield
 
 
 def _normalize_outputs(outputs: Any) -> Dict[str, Any]:
@@ -173,35 +168,40 @@
         Args:
             model_name (str): Name of the model. Default is ``'main'``.
             options (dict, optional): The configuration options.
 
                 * ``'backward_outputs'`` (list of str):
                     A list of names of outputs that require compution of
                     the gradient.
-                * ``'autocast'`` (bool):
-                    If ``True``, ``torch.cuda.amp.autocast`` is enabled.
-                    Default is ``False``.
+                * ``'autocast'`` (bool or dict):
+                    If ``True``, ``torch.autocast`` (or ``torch.cuda.amp.autocast`` for PyTorch 1.9 or earlier) is enabled,
+                    using ``{"enabled": True, "device_type": "cuda"}``
+                    as autocast options.
+                    The default is ``False`` which corresponds to the following options
+                    ``{"enabled": False, "device_type": "cuda"}``.
+                    If dict, options are passed to ``torch.autocast``.
                 * ``'grad_scaler'`` (torch.cuda.amp.GradScaler):
                     A gradient scaler that outputs are applied to.
         """
         super().__init__(options)
         self.model_name = model_name
 
     def consume_options(self, options: Dict[str, Any]) -> None:
         super().consume_options(options)
 
         self.backward_outputs = options.pop('backward_outputs', None)
         self._grad_scaler = options.pop('grad_scaler', None)
-        self._autocast = options.pop('autocast', False)
-        self._backward_fn = options.pop('backward_function', None)
 
-        if not _amp_enabled:
-            if self._grad_scaler is not None or self._autocast:
-                raise RuntimeError('Requested AMP features but torch.cuda.amp'
-                                   ' is not enabled')
+        self._backward_fn = options.pop('backward_function', None)
+        autocast_options = options.get("autocast", False)
+        if isinstance(autocast_options, bool):
+            autocast_options = {"enabled": autocast_options, "device_type": "cuda"}
+        self._autocast = _autocast._AutocastManager(
+            autocast_options, self._grad_scaler is not None
+        )
 
         if self._grad_scaler is not None:
             if not isinstance(self._grad_scaler, torch.cuda.amp.GradScaler):
                 raise RuntimeError('grad_scaler should be a '
                                    'torch.cuda.amp.GradScaler object')
 
     def _forward(self, model: torch.nn.Module, batch: Any) -> Any:
@@ -286,15 +286,15 @@
             optimizers (dict of torch.optim.Optimizer):
                 The optimizers.
             batch_idx (int):
                 Number of training steps already finished.
             batch (torch.Tensor, list of torch.Tensor, dict of torch.Tensor):
                 Input tensors feeded to the model of the current step.
         """
-        with torch_autocast(enabled=self._autocast):
+        with self._autocast.autocast():
             optimizers[self.model_name].zero_grad()
             outs = self._forward(models[self.model_name], batch)
             to_back_outs = _normalize_outputs(outs)
             if self._grad_scaler is not None:
                 assert (
                     len(to_back_outs) == 1
                 ), "loss scaling with multiple outputs is not supported"
@@ -460,7 +460,84 @@
             batch_idx (int): Number of steps already finished.
             batch (torch.Tensor, list of torch.Tensor, dict of torch.Tensor):
                 Input tensors feeded to the model of the current step.
         """
         model = models[self.model_name]
         outs = forward(model)(batch)
         return outs
+
+
+@dataclasses.dataclass
+class ClousureModelOutput:
+    outs: Any
+    loss: torch.Tensor
+
+    def __float__(self) -> float:
+        return float(self.loss)
+
+
+class ClousureLogic(Logic):
+
+    def consume_options(self, options: Dict[str, Any]) -> None:
+        super().consume_options(options)
+        if self._grad_scaler is not None:
+            raise RuntimeError('torch.cuda.amp.GradScaler does not support clousure step mode.')
+
+    def train_step(
+            self,
+            models: Mapping[str, torch.nn.Module],
+            optimizers: Mapping[str, torch.optim.Optimizer],
+            batch_idx: int,
+            batch: Any,
+    ) -> Any:
+        """A method invokes the model forward and backward passes and performs an optimization step.
+
+        Args:
+            models (dict of torch.nn.Module):
+                The models.
+            optimizers (dict of torch.optim.Optimizer):
+                The optimizers.
+            batch_idx (int):
+                Number of training steps already finished.
+            batch (torch.Tensor, list of torch.Tensor, dict of torch.Tensor):
+                Input tensors feeded to the model of the current step.
+        """
+        def clousure() -> ClousureModelOutput:
+            with self._autocast.autocast():
+                optimizers[self.model_name].zero_grad()
+                outs = self._forward(models[self.model_name], batch)
+            to_back_outs = _normalize_outputs(outs)
+            if len(to_back_outs) > 1:
+                raise RuntimeError("Clousure step with multiple outputs is not supported.")
+            elif len(to_back_outs) == 0:
+                raise RuntimeError("No backward target found.")
+
+            self._backward(to_back_outs)
+            loss, = to_back_outs.values()
+            return ClousureModelOutput(
+                outs=outs,
+                loss=loss,
+            )
+
+        optimizer = optimizers[self.model_name]
+        clousure_model_output: ClousureModelOutput = optimizer.step(clousure)  # type: ignore
+        if not isinstance(clousure_model_output, ClousureModelOutput):
+            raise RuntimeError(f"{type(clousure_model_output)} type object returned from optimizer.step with clousure. optimizer.step is expected to return ppe.handler.ClousureModelOutput.")
+        return clousure_model_output.outs
+
+    def train_step_optimizers(
+            self,
+            models: Mapping[str, torch.nn.Module],
+            optimizers: Mapping[str, torch.optim.Optimizer],
+            batch_idx: int,
+    ) -> None:
+        """In clousure mode, the stepping of the optimizer cannot be changed.
+
+        If you want to change the stepping of the optimizer, please use the normal Logic class.
+
+        Args:
+            optimizers (dict of torch.optim.Optimizer):
+                The optimizers.
+            batch_idx (int):
+                Number of steps already finished.
+        """
+        pass
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/logging.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/logging.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
         filename: Optional[str] = None,
         level: str = 'ERROR',
         format: str = _logger_format
 ) -> None:
     global _logger
     filename = os.environ.get('PPE_LOG_FILENAME', filename)
     if filename is None:
-        handler = logging.StreamHandler()
+        handler: logging.Handler = logging.StreamHandler()
     else:
         handler = logging.FileHandler(filename)
     handler.setFormatter(logging.Formatter(format))
     # To dynamically change the level if needed
     # basicConfig does not allow to change the level right after
     _logger = logging.getLogger(_logger_name)
     level = os.environ.get('PPE_LOG_LEVEL', level)
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/ensure_shape.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/ensure_shape.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/extended_sequential.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/extended_sequential.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy_batchnorm.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy_batchnorm.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy_conv.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy_conv.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/modules/lazy_linear.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/modules/lazy_linear.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/nn/parallel/distributed.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/nn/parallel/distributed.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -7,10 +7,12 @@
     from pytorch_pfn_extras.onnx.export_testcase import LARGE_TENSOR_DATA_THRESHOLD  # NOQA
     from pytorch_pfn_extras.onnx.annotate import annotate  # NOQA
     from pytorch_pfn_extras.onnx.annotate import apply_annotation  # NOQA
     from pytorch_pfn_extras.onnx.annotate import scoped_anchor  # NOQA
     from pytorch_pfn_extras.onnx._as_output import as_output  # NOQA
     from pytorch_pfn_extras.onnx._grad import grad  # NOQA
     from pytorch_pfn_extras.onnx.load import load_model  # NOQA
+    from pytorch_pfn_extras.onnx._helper import no_grad  # NOQA
+    import pytorch_pfn_extras.onnx._lax as lax  # NOQA
     available = True
 except ImportError:
     available = False
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_as_output.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_as_output.py`

 * *Files 26% similar despite different names*

```diff
@@ -94,16 +94,43 @@
     try:
         yield module, _outputs.outputs
     finally:
         # onnx_graph = _outputs.add_outputs_to_model(onnx_graph)
         _outputs.outputs = None
 
 
-def as_output(name: str, value: torch.Tensor) -> torch.Tensor:
+# Add Identity function to prevent constant folding in torch.onnx
+class _ExplicitIdentity(torch.autograd.Function):
+    @staticmethod
+    def forward(  # type: ignore
+        ctx: Any,
+        x: torch.Tensor,
+    ) -> torch.Tensor:
+        return x.clone()
+
+    @staticmethod
+    def backward(  # type: ignore
+        ctx: Any,
+        dx: torch.Tensor,
+    ) -> torch.Tensor:
+        return dx
+
+    @staticmethod
+    def symbolic(g, x):  # type: ignore
+        return g.op("Identity", x)
+
+
+def as_output(
+        name: str, value: torch.Tensor, add_identity: bool = True
+) -> torch.Tensor:
     if torch.jit.is_scripting():  # type: ignore[no-untyped-call]
         warnings.warn(
             '`as_output` seen in TorchScript compilation. The value is no '
             'longer an output in the exported onnx.')
         return value
     if hasattr(_outputs, "outputs") and _outputs.outputs is not None:
+        if add_identity:
+            value = _ExplicitIdentity.apply(value)  # type: ignore[no-untyped-call]
         _outputs.outputs.add(name, value)
+        if add_identity:
+            value = _ExplicitIdentity.apply(value)  # type: ignore[no-untyped-call]
     return value
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_constants.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_constants.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_globals.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_globals.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/_grad.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/_grad.py`

 * *Files 3% similar despite different names*

```diff
@@ -42,15 +42,15 @@
         assert only_inputs, "only_inputs=False case is not supported now"
 
         input_names = []
         inputs_l = list(inputs)
         for i, input in enumerate(inputs):
             input_name = f"Gradient_x_{i}_{n_grad_call}"
             input_names.append(input_name)
-            inputs_l[i] = as_output(input_name, input)
+            inputs_l[i] = as_output(input_name, input, add_identity=False)
 
         class _Gradient(torch.autograd.Function):
             @staticmethod
             def forward(  # type: ignore
                 ctx: Any,
                 output: torch.Tensor,
                 grad_output: Optional[torch.Tensor],
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/annotate.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/annotate.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/export_testcase.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/export_testcase.py`

 * *Files 2% similar despite different names*

```diff
@@ -16,14 +16,15 @@
 import torch.autograd
 from torch.onnx import OperatorExportTypes
 from torch.onnx.utils import \
     _export as torch_export, _model_to_graph as torch_model_to_graph
 
 from pytorch_pfn_extras.onnx import _as_output as as_output
 from pytorch_pfn_extras.onnx import _grad as grad
+from pytorch_pfn_extras.onnx import _lax as lax
 from pytorch_pfn_extras.onnx.annotate import init_annotate
 from pytorch_pfn_extras.onnx.strip_large_tensor import \
     LARGE_TENSOR_DATA_THRESHOLD
 from pytorch_pfn_extras.onnx.strip_large_tensor import is_large_tensor
 from pytorch_pfn_extras.onnx.strip_large_tensor import _strip_raw_data
 from pytorch_pfn_extras.onnx.strip_large_tensor import \
     _strip_large_initializer_raw_data
@@ -188,25 +189,27 @@
                 def no_op(*args: Any) -> None:
                     pass
 
                 torch.onnx.log = no_op  # type: ignore[attr-defined]
         kwargs['verbose'] = True
     with init_annotate(model, opset_ver) as ann, \
             as_output.trace(model) as (model, outputs), \
-            grad.init_grad_state():
+            grad.init_grad_state(), \
+            lax.init_lax_state():
         if use_pfto:
             outs = pfto_export(
                 model, args, bytesio, **kwargs)
         else:
             outs = _export_util(
                 model, args, bytesio, return_output=return_output, **kwargs)
         onnx_graph = onnx.load(io.BytesIO(bytesio.getvalue()))
         onnx_graph = ann.set_annotate(onnx_graph)
         onnx_graph = ann.reorg_anchor(onnx_graph)
         outputs.add_outputs_to_model(onnx_graph)
+        lax.postprocess(onnx_graph)
         if strip_doc_string:
             for node in onnx_graph.graph.node:
                 node.doc_string = b''
 
     if strip_large_tensor_data:
         _strip_large_initializer_raw_data(onnx_graph, large_tensor_threshold)
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/load.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/load.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/pfto_exporter/export.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/pfto_exporter/export.py`

 * *Files 5% similar despite different names*

```diff
@@ -70,22 +70,22 @@
     ret.denotation = repr(t).upper()
 
     if t.kind() == "ListType":
         ret.sequence_type.elem_type.CopyFrom(_type_to_proto(cast(torch._C.TensorType, t.getElementType())))
         return ret
 
     if t.kind() == "IntType":
-        ret.tensor_type.elem_type = onnx.TensorProto.DataType.INT64
+        ret.tensor_type.elem_type = onnx.TensorProto.DataType.INT64  # type: ignore[attr-defined]
         ret.tensor_type.shape.CopyFrom(onnx.TensorShapeProto())
         return ret
 
     assert t.kind() == "TensorType", f"Not Tensor type(actual: {t.kind()}): {t}"
 
     if t.scalarType() is None:
-        ret.tensor_type.elem_type = onnx.TensorProto.DataType.UNDEFINED
+        ret.tensor_type.elem_type = onnx.TensorProto.DataType.UNDEFINED  # type: ignore[attr-defined]
     else:
         ret.tensor_type.elem_type = int(  # type: ignore
             sym_hel.cast_pytorch_to_onnx[t.scalarType()]  # type: ignore[index]
         )
 
     ret.tensor_type.shape.CopyFrom(onnx.TensorShapeProto())
     if t.sizes() is not None:
@@ -120,23 +120,25 @@
 ```
 {torch_node.sourceRange()}
 ```
 """
 
 
 torch_dtype_to_onnx_data_type = {
-    torch.float32: onnx.TensorProto.DataType.FLOAT,
-    torch.uint8: onnx.TensorProto.DataType.UINT8,
-    torch.int8: onnx.TensorProto.DataType.INT8,
-    torch.int16: onnx.TensorProto.DataType.INT16,
-    torch.int32: onnx.TensorProto.DataType.INT32,
-    torch.int64: onnx.TensorProto.DataType.INT64,
-    torch.bool: onnx.TensorProto.DataType.BOOL,
-    torch.float64: onnx.TensorProto.DataType.DOUBLE,
-    torch.float16: onnx.TensorProto.DataType.FLOAT16,
+    torch.float32: onnx.TensorProto.DataType.FLOAT,  # type: ignore[attr-defined]
+    torch.uint8: onnx.TensorProto.DataType.UINT8,  # type: ignore[attr-defined]
+    torch.int8: onnx.TensorProto.DataType.INT8,  # type: ignore[attr-defined]
+    torch.int16: onnx.TensorProto.DataType.INT16,  # type: ignore[attr-defined]
+    torch.int32: onnx.TensorProto.DataType.INT32,  # type: ignore[attr-defined]
+    torch.int64: onnx.TensorProto.DataType.INT64,  # type: ignore[attr-defined]
+    torch.bool: onnx.TensorProto.DataType.BOOL,  # type: ignore[attr-defined]
+    torch.float64: onnx.TensorProto.DataType.DOUBLE,  # type: ignore[attr-defined]
+    torch.float16: onnx.TensorProto.DataType.FLOAT16,  # type: ignore[attr-defined]
+    torch.complex64: onnx.TensorProto.DataType.COMPLEX64,  # type: ignore[attr-defined]
+    torch.complex128: onnx.TensorProto.DataType.COMPLEX128,  # type: ignore[attr-defined]
 }
 
 
 def _apply_tensor_info_to_value_info(v: onnx.ValueInfoProto, t: torch.Tensor) -> None:
     v.type.tensor_type.elem_type = torch_dtype_to_onnx_data_type[t.dtype]
     v.type.tensor_type.shape.ClearField("dim")
     for i in t.shape:
@@ -161,14 +163,15 @@
     enable_onnx_checker: bool = True
     onnx_shape_inference: bool = True
     onnx_strict_mode: bool = False
     onnx_check_type: bool = False
     onnx_data_prop: bool = True
     onnx_lowprecision_cast: bool = True
     onnx_peephole: bool = True
+    onnx_scalar_type_analysis: bool = True
     fixed_batch_size: bool = False
 
     input_names: Optional[List[str]] = None
     output_names: Optional[List[str]] = None
     do_constant_folding: bool = True
     operator_export_type: OperatorExportTypes = OperatorExportTypes.ONNX
     keep_initializers_as_inputs: bool = False
@@ -335,18 +338,19 @@
             graph, self.dynamic_axes or {}, input_names
         )
 
         return graph
 
     # ONNX level graph optimizer
     def optimize_onnx(self, graph: torch._C.Graph) -> torch._C.Graph:
-        if pytorch_pfn_extras.requires("1.9.0"):
-            run_jit_pass(torch._C._jit_pass_onnx_scalar_type_analysis, graph, self.onnx_lowprecision_cast, self.opset_version)
-        else:
-            run_jit_pass(torch._C._jit_pass_onnx_scalar_type_analysis, graph)
+        if self.onnx_scalar_type_analysis:
+            if pytorch_pfn_extras.requires("1.9.0"):
+                run_jit_pass(torch._C._jit_pass_onnx_scalar_type_analysis, graph, self.onnx_lowprecision_cast, self.opset_version)
+            else:
+                run_jit_pass(torch._C._jit_pass_onnx_scalar_type_analysis, graph)
 
         if self.do_constant_folding and self.opset_version in pytorch_pfn_extras.onnx._constants.onnx_constant_folding_opsets:
             folded: Dict[str, torch.IValue] = torch._C._jit_pass_onnx_constant_fold(  # type: ignore[attr-defined]
                 graph, self.vars, self.opset_version
             )
             # Replace input with constant nodes
             input_table: Dict[str, torch._C.Value] = {i.debugName(): i for i in graph.inputs()}
@@ -831,16 +835,16 @@
         self.log("ONNX graph", self.g)
 
         onnx_nodes, onnx_vars, val_tab = self.generate_proto_nodes(self.g, {}, {})
 
         def onnx_value(v: torch._C.Value, name: ONNXValueID) -> onnx.ValueInfoProto:
             return onnx.helper.make_value_info(
                 name,
-                None if v.type() is None else _type_to_proto(cast(torch._C.TensorType, v.type())),
-                doc_string=None if self.strip_doc_string else repr(v),
+                onnx.TypeProto() if v.type() is None else _type_to_proto(cast(torch._C.TensorType, v.type())),
+                doc_string="" if self.strip_doc_string else repr(v),
             )
 
         def apply_dynamic_axes_info(out: onnx.ValueInfoProto, k: str) -> None:
             assert isinstance(self.dynamic_axes, dict)
             info = self.dynamic_axes.get(k, None)
             if info is None:
                 return None
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/strip_large_tensor.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/strip_large_tensor.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/symbolic_registry.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/symbolic_registry.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/onnx/unstrip_tensor.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/onnx/unstrip_tensor.py`

 * *Files 1% similar despite different names*

```diff
@@ -53,15 +53,15 @@
     for node in graph.node:
         for attr in node.attribute:
             if attr.HasField("g"):
                 _unstrip_graph(attr.g)
 
 
 def _unstrip_onnx_from_path(path: Path) -> onnx.GraphProto:
-    onnx_graph = onnx.load(path, load_external_data=False)
+    onnx_graph = onnx.load(str(path), load_external_data=False)
     _unstrip_graph(onnx_graph.graph)
     return onnx_graph
 
 
 def _unstrip_tensor_from_path(path: Path) -> onnx.TensorProto:
     onnx_tensor = onnx.TensorProto()
     with open(path, "rb") as fp:
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/profiler/_record.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/profiler/_record.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/profiler/_time_summary.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/profiler/_time_summary.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/reporting.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/reporting.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_registry.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_registry.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_runtime.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_runtime.py`

 * *Files 4% similar despite different names*

```diff
@@ -4,40 +4,19 @@
 from typing import (
     Any, Dict, Generator, Iterable, Optional, Set, Tuple, Union, TYPE_CHECKING
 )
 
 import torch
 
 from pytorch_pfn_extras.handler._code_block import CodeBlock
+from pytorch_pfn_extras.runtime import _autocast
 
 if TYPE_CHECKING:
     from pytorch_pfn_extras.training import Evaluator, Trainer
 
-_amp_enabled = False
-
-
-try:
-    import torch.cuda.amp
-
-    _amp_enabled = torch.cuda.is_available() and hasattr(
-        torch.cuda.amp, "autocast"
-    )
-except ImportError:
-    pass
-
-
-@contextlib.contextmanager
-def _autocast(enabled: bool = True) -> Generator[None, None, None]:
-    if _amp_enabled:
-        with torch.cuda.amp.autocast(enabled):  # type: ignore[no-untyped-call]
-            yield
-    else:
-        yield
-
-
 _RUNTIME_TAG_NAME = "_ppe_runtime"
 
 DeviceLike = Union[str, torch.device]
 
 
 class BaseRuntime:
     """A base class for collections of device-specific callback functions.
@@ -332,34 +311,37 @@
     """A collections of callback functions for the devices that PyTorch
     supports by default.
 
     Args:
         device_spec (torch.device or str): The device.
         options (dict, optional): The configuration options.
 
-            * ``'autocast'`` (bool):
+            * ``'autocast'`` (bool or dict):
                 If ``True``, ``torch.cuda.amp.autocast`` is enabled.
-                Default is ``False``.
+                using ``{"enabled": True, "device_type": "cuda"}``
+                as autocast options.
+                Default is ``False`` which corresponds to the following options
+                ``{"enabled": False, "device_type": "cuda"}``
+                dict type. If dict, Options to pass to ``torch.autocast``.
+                Includes ``device_type``, ``dtype`` among others.
             * ``'grad_scaler'`` (torch.cuda.amp.GradScaler):
                 A gradient scaler that outputs are applied to.
     """
 
     def __init__(
         self, device_spec: DeviceLike, options: Dict[str, Any],
     ) -> None:
         super().__init__(device_spec, options)
         self._grad_scaler = options.get("grad_scaler", None)
-        self._autocast = options.get("autocast", False)
-        if not _amp_enabled:
-            if self._grad_scaler is not None or self._autocast:
-                raise RuntimeError(
-                    "Requested AMP features but torch.cuda.amp"
-                    " is not enabled"
-                )
-
+        autocast_options = options.get("autocast", False)
+        if isinstance(autocast_options, bool):
+            autocast_options = {"enabled": autocast_options, "device_type": "cuda"}
+        self._autocast = _autocast._AutocastManager(
+            autocast_options, self._grad_scaler is not None
+        )
         if self._grad_scaler is not None:
             if not isinstance(self._grad_scaler, torch.cuda.amp.GradScaler):
                 raise RuntimeError(
                     "grad_scaler should be a "
                     "torch.cuda.amp.GradScaler object"
                 )
 
@@ -442,15 +424,15 @@
             def _scale(x: torch.Tensor) -> torch.Tensor:
                 return self._grad_scaler.scale(x)  # type: ignore[no-any-return]
 
         for optimizer in code_block.optimizers:
             optimizer.zero_grad()
 
         # with autocast
-        with _autocast(enabled=self._autocast):
+        with self._autocast.autocast():
             out = code_block.func(**batch)
 
         # codeblocks return Dicts-per-se so it is not necessary to normalize
         if code_block.backprop:
             if code_block.backprop_from is None:
                 for v in out.values():
                     if (
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/runtime/_to.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/runtime/_to.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_evaluator.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_evaluator.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_manager_protocol.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_manager_protocol.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_trainer.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_trainer.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_trigger_util.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_trigger_util.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/_util.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/_util.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extension.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extension.py`

 * *Files 1% similar despite different names*

```diff
@@ -137,15 +137,15 @@
     def state_dict(self) -> Dict[str, Any]:
         """Serializes the extension state.
 
         It is called when a manager that owns this extension is serialized. It
         serializes nothing by default.
 
         """
-        pass
+        return {}
 
     def load_state_dict(self, to_load: Dict[str, Any]) -> None:
         pass
 
 
 class _WrappedExtension(Extension):
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/_snapshot.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/_snapshot.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/best_value.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/best_value.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/evaluator.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/evaluator.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/fail_on_non_number.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/fail_on_non_number.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/log_report.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/log_report.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/lr_scheduler.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/lr_scheduler.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/micro_average.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/micro_average.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/parameter_statistics.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/parameter_statistics.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/plot_report.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/plot_report.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/print_report.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/print_report.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/print_report_notebook.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/print_report_notebook.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/profile_report.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/profile_report.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/progress_bar.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/progress_bar.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/progress_bar_notebook.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/progress_bar_notebook.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/slack.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/slack.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/util.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/util.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/value_observation.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/value_observation.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/extensions/variable_statistics_plot.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/extensions/variable_statistics_plot.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/manager.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/manager.py`

 * *Files 0% similar despite different names*

```diff
@@ -459,15 +459,15 @@
         return False
 
     def _finalize_extensions(self) -> None:
         for _, entry in self.extensions:
             # Some mock objects for tests give errors
             # if we use `getattr`
             try:
-                if entry.extension.finalize:
+                if entry.extension.finalize:  # type: ignore[truthy-function]
                     entry.extension.finalize(self)
             except AttributeError:
                 pass
 
     def state_dict(
             self,
     ) -> Dict[str, Any]:
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/metrics.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/metrics.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/early_stopping_trigger.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/early_stopping_trigger.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/interval_trigger.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/interval_trigger.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/manual_schedule_trigger.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/manual_schedule_trigger.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/minmax_value_trigger.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/minmax_value_trigger.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/once_trigger.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/once_trigger.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/training/triggers/time_trigger.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/training/triggers/time_trigger.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/utils/checkpoint.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/checkpoint.py`

 * *Files 6% similar despite different names*

```diff
@@ -43,8 +43,8 @@
 
 def checkpoint(function: torch.nn.Module, *args: Any, **kwargs: Any) -> Any:
     # Hack to mix *args with **kwargs in a python 2.7-compliant way
     preserve = kwargs.pop('preserve_rng_state', True)
     if kwargs:
         raise ValueError(
             'Unexpected keyword arguments: ' + ','.join(arg for arg in kwargs))
-    return _CheckpointFunction.apply(function, preserve, *args)
+    return _CheckpointFunction.apply(function, preserve, *args)  # type: ignore[no-untyped-call]
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/utils/comparer.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/utils/comparer.py`

 * *Files 0% similar despite different names*

```diff
@@ -725,15 +725,15 @@
         n_workers = len(self._engines)
         self._barrier = threading.Barrier(n_workers)
         self._semaphore = threading.Semaphore(
             n_workers if self._concurrency is None else self._concurrency)
         with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
             futures = []
             for _, (engine, args, kwargs) in self._engines.items():
-                futures.append(executor.submit(self._run_engine, engine, args, kwargs))
+                futures.append(executor.submit(self._run_engine, engine, args, kwargs))  # type: ignore[arg-type]
             for future in concurrent.futures.as_completed(futures):
                 future.result()
 
 
 def intermediate_value(name: str, value: torch.Tensor) -> None:
     if not hasattr(_thread_local, 'handler'):
         return
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/__init__.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_parallel_writer.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_parallel_writer.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_queue_writer.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_queue_writer.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_simple_writer.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_simple_writer.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_tensorboard_writer.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_tensorboard_writer.py`

 * *Files 3% similar despite different names*

```diff
@@ -70,15 +70,15 @@
         if isinstance(target, list):
             stats_cpu = target[-1]
 
         if not isinstance(stats_cpu, dict):
             raise TypeError('target must be dict or list of dicts')
         keys = stats_cpu.keys()
         if self._stats is not None:
-            keys = self._stats
+            keys = self._stats  # type: ignore[assignment]
         for key in keys:
             value = stats_cpu[key]
             self._writer.add_scalar(  # type: ignore[no-untyped-call]
                 key, value, stats_cpu['iteration'])
 
     def finalize(self) -> None:
         if self._writer is not None:
```

### Comparing `pytorch-pfn-extras-0.6.5/pytorch_pfn_extras/writing/_writer_base.py` & `pytorch-pfn-extras-0.6.6/pytorch_pfn_extras/writing/_writer_base.py`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/setup.cfg` & `pytorch-pfn-extras-0.6.6/setup.cfg`

 * *Files identical despite different names*

### Comparing `pytorch-pfn-extras-0.6.5/setup.py` & `pytorch-pfn-extras-0.6.6/setup.py`

 * *Files identical despite different names*

