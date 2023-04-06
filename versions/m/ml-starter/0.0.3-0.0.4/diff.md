# Comparing `tmp/ml-starter-0.0.3.tar.gz` & `tmp/ml-starter-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ml-starter-0.0.3.tar", last modified: Thu Apr  6 22:27:05 2023, max compression
+gzip compressed data, was "ml-starter-0.0.4.tar", last modified: Thu Apr  6 23:42:51 2023, max compression
```

## Comparing `ml-starter-0.0.3.tar` & `ml-starter-0.0.4.tar`

### file list

```diff
@@ -1,325 +1,352 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.750173 ml-starter-0.0.3/
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-04-06 22:26:55.000000 ml-starter-0.0.3/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 22:27:05.750173 ml-starter-0.0.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3773 2023-04-06 22:26:55.000000 ml-starter-0.0.3/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.722173 ml-starter-0.0.3/ml/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/__version__.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2834 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/api.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.726173 ml-starter-0.0.3/ml/core/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/core/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      224 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/core/common_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     3332 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/core/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     5356 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/core/env.py
--rw-r--r--   0 runner    (1001) docker     (123)    23463 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/core/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/core/state.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.726173 ml-starter-0.0.3/ml/loggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/loggers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4905 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/loggers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2726 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/loggers/meter.py
--rw-r--r--   0 runner    (1001) docker     (123)    31809 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/loggers/multi.py
--rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/loggers/stdout.py
--rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/loggers/tensorboard.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.726173 ml-starter-0.0.3/ml/lr_schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/constant.py
--rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/cosine.py
--rw-r--r--   0 runner    (1001) docker     (123)     2342 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/cosine_decay.py
--rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/linear.py
--rw-r--r--   0 runner    (1001) docker     (123)      719 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/linear_no_decay.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.726173 ml-starter-0.0.3/ml/lr_schedulers/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1897 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/lr_schedulers/scripts/plot.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.726173 ml-starter-0.0.3/ml/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2060 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/models/activations.py
--rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/models/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/models/init.py
--rw-r--r--   0 runner    (1001) docker     (123)    11127 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/models/norms.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/adam.py
--rw-r--r--   0 runner    (1001) docker     (123)     3057 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/adamw.py
--rw-r--r--   0 runner    (1001) docker     (123)     3347 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/adan.py
--rw-r--r--   0 runner    (1001) docker     (123)      903 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/sgd.py
--rw-r--r--   0 runner    (1001) docker     (123)     6094 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/shampoo.py
--rw-r--r--   0 runner    (1001) docker     (123)      297 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/optimizers/types.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2815 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/compiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     2431 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/create.py
--rw-r--r--   0 runner    (1001) docker     (123)      465 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/mp_train.py
--rw-r--r--   0 runner    (1001) docker     (123)      768 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/stage.py
--rw-r--r--   0 runner    (1001) docker     (123)      722 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/scripts/train.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17502 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/tasks/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/async_iterable.py
--rw-r--r--   0 runner    (1001) docker     (123)     3778 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/clippify.py
--rw-r--r--   0 runner    (1001) docker     (123)     7256 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/collate.py
--rw-r--r--   0 runner    (1001) docker     (123)     8725 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/error_handling.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/tasks/datasets/impl/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/impl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2160 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/impl/kinetics.py
--rw-r--r--   0 runner    (1001) docker     (123)     5273 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/impl/pretraining.py
--rw-r--r--   0 runner    (1001) docker     (123)      302 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/impl/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/impl/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/multi_iter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/samplers.py
--rw-r--r--   0 runner    (1001) docker     (123)     4439 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/streaming.py
--rw-r--r--   0 runner    (1001) docker     (123)     6687 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/transforms.py
--rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/datasets/video_file.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/tasks/environments/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/environments/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1599 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/environments/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/environments/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    13383 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/environments/worker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/tasks/losses/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      931 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/losses/reduce.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.730173 ml-starter-0.0.3/ml/tasks/rl/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/rl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13501 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/rl/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3108 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/rl/replay.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/tasks/sl/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/sl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/tasks/sl/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/
--rwxr-xr-x   0 runner    (1001) docker     (123)     1337 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/copy_empty.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1905 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/configs/
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/configs/template.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/cpp/
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/CMakeLists.txt
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/
--rw-r--r--   0 runner    (1001) docker     (123)     1132 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/CMakeLists.txt
--rw-r--r--   0 runner    (1001) docker     (123)      703 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/ops/
--rw-r--r--   0 runner    (1001) docker     (123)     1357 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.h
--rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/torch_ops.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/torch_ops.h
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/loggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/loggers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/lr_schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/lr_schedulers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      467 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/models/template.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/optimizers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/scripts/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      897 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/tasks/template.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/project/trainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/project/trainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     8833 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.734173 ml-starter-0.0.3/ml/templates/cpp/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/cpp/tests/test_cpp_extension.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/configs/
--rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/configs/template.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/loggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/loggers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/lr_schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/lr_schedulers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      467 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/models/template.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/optimizers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/scripts/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      897 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/tasks/template.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/project/trainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/project/trainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/empty/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/empty/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/configs/
--rw-r--r--   0 runner    (1001) docker     (123)      278 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/configs/image_demo.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/loggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/loggers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/lr_schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/lr_schedulers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2024 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/models/resnet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/optimizers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/scripts/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2481 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/tasks/image_demo.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/project/trainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/project/trainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.738173 ml-starter-0.0.3/ml/templates/image/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)     1414 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/image/tests/test_instantiate_configs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/configs/
--rw-r--r--   0 runner    (1001) docker     (123)      588 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/configs/rl_demo.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/loggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/loggers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/lr_schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/lr_schedulers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3929 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/models/a2c.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/optimizers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/scripts/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6039 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/tasks/rl_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3270 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/tasks/rl_demo_env.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/project/trainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/project/trainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/rl/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/rl/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/
--rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/configs/
--rw-r--r--   0 runner    (1001) docker     (123)      258 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/configs/video_demo.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/project/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/project/loggers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/loggers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/project/lr_schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/lr_schedulers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/project/models/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/models/video_resnet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.742173 ml-starter-0.0.3/ml/templates/video/project/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/optimizers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/templates/video/project/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/scripts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/scripts/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/templates/video/project/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1942 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/tasks/video_demo.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/templates/video/project/trainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/project/trainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)       70 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/templates/video/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/templates/video/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/trainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16412 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4395 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/ddp.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/trainers/mixins/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4737 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/cpu_stats.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.746173 ml-starter-0.0.3/ml/trainers/mixins/device/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/device/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/device/auto.py
--rw-r--r--   0 runner    (1001) docker     (123)     7516 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/device/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/device/cpu.py
--rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/device/gpu.py
--rw-r--r--   0 runner    (1001) docker     (123)      775 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/device/metal.py
--rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/gpu_stats.py
--rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/grad_clipping.py
--rw-r--r--   0 runner    (1001) docker     (123)     3148 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/mixed_precision.py
--rw-r--r--   0 runner    (1001) docker     (123)     5536 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/profiler.py
--rw-r--r--   0 runner    (1001) docker     (123)     1262 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/mixins/step_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     8638 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/rl.py
--rw-r--r--   0 runner    (1001) docker     (123)    10088 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/sl.py
--rw-r--r--   0 runner    (1001) docker     (123)    10349 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/slurm.py
--rw-r--r--   0 runner    (1001) docker     (123)    11073 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/trainers/vanilla.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.750173 ml-starter-0.0.3/ml/utils/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2864 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/argparse.py
--rw-r--r--   0 runner    (1001) docker     (123)     2582 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/atomic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1580 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/augmentation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4608 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/caching.py
--rw-r--r--   0 runner    (1001) docker     (123)      977 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/call_train.py
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/checks.py
--rw-r--r--   0 runner    (1001) docker     (123)     3009 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/colors.py
--rw-r--r--   0 runner    (1001) docker     (123)    12052 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/compiler.py
--rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/data.py
--rw-r--r--   0 runner    (1001) docker     (123)      820 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/datetime.py
--rw-r--r--   0 runner    (1001) docker     (123)     2180 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/distributed.py
--rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/large_models.py
--rw-r--r--   0 runner    (1001) docker     (123)     4346 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/logging.py
--rw-r--r--   0 runner    (1001) docker     (123)     2525 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/meter.py
--rw-r--r--   0 runner    (1001) docker     (123)      259 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/networking.py
--rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/paths.py
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/random.py
--rw-r--r--   0 runner    (1001) docker     (123)     2394 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/timer.py
--rw-r--r--   0 runner    (1001) docker     (123)    14152 2023-04-06 22:26:55.000000 ml-starter-0.0.3/ml/utils/video.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:27:05.750173 ml-starter-0.0.3/ml_starter.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 22:27:05.000000 ml-starter-0.0.3/ml_starter.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     7830 2023-04-06 22:27:05.000000 ml-starter-0.0.3/ml_starter.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 22:27:05.000000 ml-starter-0.0.3/ml_starter.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-06 22:27:05.000000 ml-starter-0.0.3/ml_starter.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 22:27:05.000000 ml-starter-0.0.3/ml_starter.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        3 2023-04-06 22:27:05.000000 ml-starter-0.0.3/ml_starter.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1446 2023-04-06 22:26:55.000000 ml-starter-0.0.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 22:26:55.000000 ml-starter-0.0.3/requirements-dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)      127 2023-04-06 22:26:55.000000 ml-starter-0.0.3/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-06 22:27:05.750173 ml-starter-0.0.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1217 2023-04-06 22:26:55.000000 ml-starter-0.0.3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.346527 ml-starter-0.0.4/
+-rw-r--r--   0 runner    (1001) docker     (123)      192 2023-04-06 23:42:41.000000 ml-starter-0.0.4/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 23:42:51.346527 ml-starter-0.0.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3773 2023-04-06 23:42:41.000000 ml-starter-0.0.4/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.298526 ml-starter-0.0.4/ml/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/__version__.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2834 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/api.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.298526 ml-starter-0.0.4/ml/core/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/core/common_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3332 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/core/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5356 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/core/env.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23463 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/core/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/core/state.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.302526 ml-starter-0.0.4/ml/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/loggers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4905 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/loggers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2726 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/loggers/meter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31809 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/loggers/multi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/loggers/stdout.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/loggers/tensorboard.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.302526 ml-starter-0.0.4/ml/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/constant.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/cosine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2342 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/cosine_decay.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/linear.py
+-rw-r--r--   0 runner    (1001) docker     (123)      719 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/linear_no_decay.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.302526 ml-starter-0.0.4/ml/lr_schedulers/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1897 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/lr_schedulers/scripts/plot.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.302526 ml-starter-0.0.4/ml/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2060 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/models/activations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/models/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/models/init.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11127 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/models/norms.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.302526 ml-starter-0.0.4/ml/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/adam.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3057 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/adamw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3347 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/adan.py
+-rw-r--r--   0 runner    (1001) docker     (123)      903 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/sgd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6094 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/shampoo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      297 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/optimizers/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.302526 ml-starter-0.0.4/ml/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2815 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2431 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/create.py
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/mp_train.py
+-rw-r--r--   0 runner    (1001) docker     (123)      768 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/stage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      722 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/scripts/train.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.306526 ml-starter-0.0.4/ml/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17502 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/tasks/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/async_iterable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3778 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/clippify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7256 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/collate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8725 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/error_handling.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/tasks/datasets/impl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/impl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2160 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/impl/kinetics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5273 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/impl/pretraining.py
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/impl/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/impl/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/multi_iter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/samplers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4439 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/streaming.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6687 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/datasets/video_file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/tasks/environments/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/environments/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1599 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/environments/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/environments/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13383 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/environments/worker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/tasks/losses/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      931 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/losses/reduce.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/tasks/rl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/rl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13501 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/rl/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3108 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/rl/replay.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/tasks/sl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/sl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/tasks/sl/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.310526 ml-starter-0.0.4/ml/templates/
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1337 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/copy_empty.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/.clang-format
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/.darglint
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/.env
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1905 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/configs/template.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/project/cpp/
+-rw-r--r--   0 runner    (1001) docker     (123)       47 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/CMakeLists.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/
+-rw-r--r--   0 runner    (1001) docker     (123)     1132 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/CMakeLists.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      703 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/ops/
+-rw-r--r--   0 runner    (1001) docker     (123)     1357 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.h
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/torch_ops.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/torch_ops.h
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/project/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/loggers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.314526 ml-starter-0.0.4/ml/templates/cpp/project/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/lr_schedulers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/cpp/project/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      467 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/models/template.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/cpp/project/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/optimizers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/cpp/project/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/scripts/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/cpp/project/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      897 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/tasks/template.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/cpp/project/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/project/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     8833 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/cpp/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/cpp/tests/test_cpp_extension.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.318526 ml-starter-0.0.4/ml/templates/empty/
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.darglint
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.env
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/.github/
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.github/pull_request_template.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      727 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.github/workflows/core-checks.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.gitignore
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/.vscode/
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.vscode/extensions.json
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/.vscode/settings.json
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)      272 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/configs/template.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/loggers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/lr_schedulers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      467 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/models/template.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/optimizers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/scripts/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      897 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/tasks/template.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/project/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/project/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.322526 ml-starter-0.0.4/ml/templates/empty/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/empty/tests/test_dummy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/.darglint
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/.env
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/configs/image_demo.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/loggers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/lr_schedulers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2024 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/models/resnet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/optimizers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/scripts/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2481 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/tasks/image_demo.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.326526 ml-starter-0.0.4/ml/templates/image/project/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/project/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/image/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1594 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/image/tests/test_instantiate_configs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/.darglint
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/.env
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)      588 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/configs/rl_demo.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/project/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/loggers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/project/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/lr_schedulers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/project/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3929 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/models/a2c.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.330526 ml-starter-0.0.4/ml/templates/rl/project/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/optimizers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/rl/project/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/scripts/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/rl/project/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6039 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/tasks/rl_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3270 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/tasks/rl_demo_env.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/rl/project/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/project/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/rl/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/rl/tests/test_dummy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/video/
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/.darglint
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/.env
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/video/configs/
+-rw-r--r--   0 runner    (1001) docker     (123)      258 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/configs/video_demo.yaml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.334526 ml-starter-0.0.4/ml/templates/video/project/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/loggers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/lr_schedulers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1649 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/models/video_resnet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/optimizers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      222 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/scripts/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1942 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/tasks/video_demo.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/project/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/project/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1439 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       70 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      810 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/templates/video/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/templates/video/tests/test_dummy.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.338527 ml-starter-0.0.4/ml/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16412 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4395 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/ddp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.342527 ml-starter-0.0.4/ml/trainers/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4737 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/cpu_stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.342527 ml-starter-0.0.4/ml/trainers/mixins/device/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/device/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/device/auto.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7516 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/device/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/device/cpu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/device/gpu.py
+-rw-r--r--   0 runner    (1001) docker     (123)      775 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/device/metal.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/gpu_stats.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/grad_clipping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3148 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/mixed_precision.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5536 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1262 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/mixins/step_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8638 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/rl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10088 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/sl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10349 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/slurm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11073 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/trainers/vanilla.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.346527 ml-starter-0.0.4/ml/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2864 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/argparse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2582 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/atomic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1580 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/augmentation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4608 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/caching.py
+-rw-r--r--   0 runner    (1001) docker     (123)      977 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/call_train.py
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/checks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3009 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/colors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12052 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      820 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2180 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/distributed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/large_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4346 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2525 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/meter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      259 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/networking.py
+-rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/paths.py
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/random.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2394 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14152 2023-04-06 23:42:41.000000 ml-starter-0.0.4/ml/utils/video.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 23:42:51.346527 ml-starter-0.0.4/ml_starter.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 23:42:51.000000 ml-starter-0.0.4/ml_starter.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8604 2023-04-06 23:42:51.000000 ml-starter-0.0.4/ml_starter.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 23:42:51.000000 ml-starter-0.0.4/ml_starter.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-06 23:42:51.000000 ml-starter-0.0.4/ml_starter.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 23:42:51.000000 ml-starter-0.0.4/ml_starter.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        3 2023-04-06 23:42:51.000000 ml-starter-0.0.4/ml_starter.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1446 2023-04-06 23:42:41.000000 ml-starter-0.0.4/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 23:42:41.000000 ml-starter-0.0.4/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-04-06 23:42:41.000000 ml-starter-0.0.4/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-06 23:42:51.346527 ml-starter-0.0.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1217 2023-04-06 23:42:41.000000 ml-starter-0.0.4/setup.py
```

### Comparing `ml-starter-0.0.3/PKG-INFO` & `ml-starter-0.0.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ml-starter
-Version: 0.0.3
+Version: 0.0.4
 Summary: ML project template repository
 Home-page: https://github.com/codekansas/ml-starter
 Author: Benjamin Bolte
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `ml-starter-0.0.3/README.md` & `ml-starter-0.0.4/README.md`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/api.py` & `ml-starter-0.0.4/ml/api.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/core/config.py` & `ml-starter-0.0.4/ml/core/config.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/core/env.py` & `ml-starter-0.0.4/ml/core/env.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/core/registry.py` & `ml-starter-0.0.4/ml/core/registry.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/core/state.py` & `ml-starter-0.0.4/ml/core/state.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/loggers/base.py` & `ml-starter-0.0.4/ml/loggers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/loggers/meter.py` & `ml-starter-0.0.4/ml/loggers/meter.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/loggers/multi.py` & `ml-starter-0.0.4/ml/loggers/multi.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/loggers/stdout.py` & `ml-starter-0.0.4/ml/loggers/stdout.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/loggers/tensorboard.py` & `ml-starter-0.0.4/ml/loggers/tensorboard.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/lr_schedulers/base.py` & `ml-starter-0.0.4/ml/lr_schedulers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/lr_schedulers/cosine.py` & `ml-starter-0.0.4/ml/lr_schedulers/cosine.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/lr_schedulers/cosine_decay.py` & `ml-starter-0.0.4/ml/lr_schedulers/cosine_decay.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/lr_schedulers/linear.py` & `ml-starter-0.0.4/ml/lr_schedulers/linear.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/lr_schedulers/linear_no_decay.py` & `ml-starter-0.0.4/ml/lr_schedulers/linear_no_decay.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/lr_schedulers/scripts/plot.py` & `ml-starter-0.0.4/ml/lr_schedulers/scripts/plot.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/models/activations.py` & `ml-starter-0.0.4/ml/models/activations.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/models/base.py` & `ml-starter-0.0.4/ml/models/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/models/init.py` & `ml-starter-0.0.4/ml/models/init.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/models/norms.py` & `ml-starter-0.0.4/ml/models/norms.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/optimizers/adam.py` & `ml-starter-0.0.4/ml/optimizers/adam.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/optimizers/adamw.py` & `ml-starter-0.0.4/ml/optimizers/adamw.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/optimizers/adan.py` & `ml-starter-0.0.4/ml/optimizers/adan.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/optimizers/base.py` & `ml-starter-0.0.4/ml/optimizers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/optimizers/sgd.py` & `ml-starter-0.0.4/ml/optimizers/sgd.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/optimizers/shampoo.py` & `ml-starter-0.0.4/ml/optimizers/shampoo.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/scripts/cli.py` & `ml-starter-0.0.4/ml/scripts/cli.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/scripts/compiler.py` & `ml-starter-0.0.4/ml/scripts/compiler.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/scripts/create.py` & `ml-starter-0.0.4/ml/scripts/create.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/scripts/stage.py` & `ml-starter-0.0.4/ml/scripts/stage.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/scripts/train.py` & `ml-starter-0.0.4/ml/scripts/train.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/base.py` & `ml-starter-0.0.4/ml/tasks/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/async_iterable.py` & `ml-starter-0.0.4/ml/tasks/datasets/async_iterable.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/clippify.py` & `ml-starter-0.0.4/ml/tasks/datasets/clippify.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/collate.py` & `ml-starter-0.0.4/ml/tasks/datasets/collate.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/error_handling.py` & `ml-starter-0.0.4/ml/tasks/datasets/error_handling.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/impl/kinetics.py` & `ml-starter-0.0.4/ml/tasks/datasets/impl/kinetics.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/impl/pretraining.py` & `ml-starter-0.0.4/ml/tasks/datasets/impl/pretraining.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/impl/utils.py` & `ml-starter-0.0.4/ml/tasks/datasets/impl/utils.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/multi_iter.py` & `ml-starter-0.0.4/ml/tasks/datasets/multi_iter.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/samplers.py` & `ml-starter-0.0.4/ml/tasks/datasets/samplers.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/streaming.py` & `ml-starter-0.0.4/ml/tasks/datasets/streaming.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/transforms.py` & `ml-starter-0.0.4/ml/tasks/datasets/transforms.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/datasets/video_file.py` & `ml-starter-0.0.4/ml/tasks/datasets/video_file.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/environments/base.py` & `ml-starter-0.0.4/ml/tasks/environments/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/environments/utils.py` & `ml-starter-0.0.4/ml/tasks/environments/utils.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/environments/worker.py` & `ml-starter-0.0.4/ml/tasks/environments/worker.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/losses/reduce.py` & `ml-starter-0.0.4/ml/tasks/losses/reduce.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/rl/base.py` & `ml-starter-0.0.4/ml/tasks/rl/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/rl/replay.py` & `ml-starter-0.0.4/ml/tasks/rl/replay.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/tasks/sl/base.py` & `ml-starter-0.0.4/ml/tasks/sl/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/copy_empty.py` & `ml-starter-0.0.4/ml/templates/copy_empty.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/Makefile` & `ml-starter-0.0.4/ml/templates/cpp/Makefile`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/CMakeLists.txt` & `ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/CMakeLists.txt`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/__init__.py` & `ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/__init__.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.cpp` & `ml-starter-0.0.4/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.cpp`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/project/tasks/template.py` & `ml-starter-0.0.4/ml/templates/cpp/project/tasks/template.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/pyproject.toml` & `ml-starter-0.0.4/ml/templates/cpp/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/setup.py` & `ml-starter-0.0.4/ml/templates/cpp/setup.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/cpp/tests/conftest.py` & `ml-starter-0.0.4/ml/templates/cpp/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/empty/Makefile` & `ml-starter-0.0.4/ml/templates/empty/Makefile`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/empty/project/tasks/template.py` & `ml-starter-0.0.4/ml/templates/empty/project/tasks/template.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/empty/pyproject.toml` & `ml-starter-0.0.4/ml/templates/empty/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/empty/setup.py` & `ml-starter-0.0.4/ml/templates/empty/setup.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/empty/tests/conftest.py` & `ml-starter-0.0.4/ml/templates/empty/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/Makefile` & `ml-starter-0.0.4/ml/templates/image/Makefile`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/project/models/resnet.py` & `ml-starter-0.0.4/ml/templates/image/project/models/resnet.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/project/tasks/image_demo.py` & `ml-starter-0.0.4/ml/templates/image/project/tasks/image_demo.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/pyproject.toml` & `ml-starter-0.0.4/ml/templates/image/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/setup.py` & `ml-starter-0.0.4/ml/templates/image/setup.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/tests/conftest.py` & `ml-starter-0.0.4/ml/templates/image/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/image/tests/test_instantiate_configs.py` & `ml-starter-0.0.4/ml/templates/image/tests/test_instantiate_configs.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,33 +1,39 @@
 import os
 from pathlib import Path
 
-import ml.api as ml
 import pytest
+from ml.core.env import set_project_root
 from ml.core.registry import Objects
 from ml.utils.cli import parse_cli
 from omegaconf import DictConfig
 
+import project
+from project.scripts.cli import PROJECT_ROOT
+
 # Be mindful that these configs are supposed to run regularly in CI
 # and therefore should not be too expensive.
 CONFIGS_TO_CHECK: list[list[str]] = [
     ["configs/image_demo.yaml", "model.pretrained=False"],
 ]
 
 
 @pytest.mark.parametrize("config_paths", CONFIGS_TO_CHECK)
 @pytest.mark.slow()
 def test_instantiate_configs(config_paths: list[str], tmpdir: Path) -> None:
     # Resolves config paths.
-    config_parent_dir = Path(ml.__path__[0]).parent
+    config_parent_dir = Path(project.__path__[0]).parent
     config_paths_absolute = [
         str((config_parent_dir / config_path).resolve()) if (config_parent_dir / config_path).exists() else config_path
         for config_path in config_paths
     ]
 
+    # Adds the project's root directory.
+    set_project_root(Path(PROJECT_ROOT).resolve())
+
     def create_and_set(key: str) -> None:
         env_dir = Path(tmpdir / key)
         env_dir.mkdir(parents=True, exist_ok=True)
         os.environ[key] = str(env_dir)
 
     # Resolves various environment variables.
     create_and_set("RUN_DIR")
```

### Comparing `ml-starter-0.0.3/ml/templates/rl/Makefile` & `ml-starter-0.0.4/ml/templates/rl/Makefile`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/configs/rl_demo.yaml` & `ml-starter-0.0.4/ml/templates/rl/configs/rl_demo.yaml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/project/models/a2c.py` & `ml-starter-0.0.4/ml/templates/rl/project/models/a2c.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/project/tasks/rl_demo.py` & `ml-starter-0.0.4/ml/templates/rl/project/tasks/rl_demo.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/project/tasks/rl_demo_env.py` & `ml-starter-0.0.4/ml/templates/rl/project/tasks/rl_demo_env.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/pyproject.toml` & `ml-starter-0.0.4/ml/templates/rl/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/setup.py` & `ml-starter-0.0.4/ml/templates/rl/setup.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/rl/tests/conftest.py` & `ml-starter-0.0.4/ml/templates/rl/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/video/Makefile` & `ml-starter-0.0.4/ml/templates/video/Makefile`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/video/project/models/video_resnet.py` & `ml-starter-0.0.4/ml/templates/video/project/models/video_resnet.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/video/project/tasks/video_demo.py` & `ml-starter-0.0.4/ml/templates/video/project/tasks/video_demo.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/video/pyproject.toml` & `ml-starter-0.0.4/ml/templates/video/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/video/setup.py` & `ml-starter-0.0.4/ml/templates/video/setup.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/templates/video/tests/conftest.py` & `ml-starter-0.0.4/ml/templates/video/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/base.py` & `ml-starter-0.0.4/ml/trainers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/ddp.py` & `ml-starter-0.0.4/ml/trainers/ddp.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/cpu_stats.py` & `ml-starter-0.0.4/ml/trainers/mixins/cpu_stats.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/device/auto.py` & `ml-starter-0.0.4/ml/trainers/mixins/device/auto.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/device/base.py` & `ml-starter-0.0.4/ml/trainers/mixins/device/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/device/cpu.py` & `ml-starter-0.0.4/ml/trainers/mixins/device/cpu.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/device/gpu.py` & `ml-starter-0.0.4/ml/trainers/mixins/device/gpu.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/device/metal.py` & `ml-starter-0.0.4/ml/trainers/mixins/device/metal.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/gpu_stats.py` & `ml-starter-0.0.4/ml/trainers/mixins/gpu_stats.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/grad_clipping.py` & `ml-starter-0.0.4/ml/trainers/mixins/grad_clipping.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/mixed_precision.py` & `ml-starter-0.0.4/ml/trainers/mixins/mixed_precision.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/profiler.py` & `ml-starter-0.0.4/ml/trainers/mixins/profiler.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/mixins/step_wrapper.py` & `ml-starter-0.0.4/ml/trainers/mixins/step_wrapper.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/rl.py` & `ml-starter-0.0.4/ml/trainers/rl.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/sl.py` & `ml-starter-0.0.4/ml/trainers/sl.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/slurm.py` & `ml-starter-0.0.4/ml/trainers/slurm.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/trainers/vanilla.py` & `ml-starter-0.0.4/ml/trainers/vanilla.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/argparse.py` & `ml-starter-0.0.4/ml/utils/argparse.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/atomic.py` & `ml-starter-0.0.4/ml/utils/atomic.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/augmentation.py` & `ml-starter-0.0.4/ml/utils/augmentation.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/caching.py` & `ml-starter-0.0.4/ml/utils/caching.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/call_train.py` & `ml-starter-0.0.4/ml/utils/call_train.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/cli.py` & `ml-starter-0.0.4/ml/utils/cli.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/colors.py` & `ml-starter-0.0.4/ml/utils/colors.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/compiler.py` & `ml-starter-0.0.4/ml/utils/compiler.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/data.py` & `ml-starter-0.0.4/ml/utils/data.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/datetime.py` & `ml-starter-0.0.4/ml/utils/datetime.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/distributed.py` & `ml-starter-0.0.4/ml/utils/distributed.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/large_models.py` & `ml-starter-0.0.4/ml/utils/large_models.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/logging.py` & `ml-starter-0.0.4/ml/utils/logging.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/meter.py` & `ml-starter-0.0.4/ml/utils/meter.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/timer.py` & `ml-starter-0.0.4/ml/utils/timer.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml/utils/video.py` & `ml-starter-0.0.4/ml/utils/video.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/ml_starter.egg-info/PKG-INFO` & `ml-starter-0.0.4/ml_starter.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ml-starter
-Version: 0.0.3
+Version: 0.0.4
 Summary: ML project template repository
 Home-page: https://github.com/codekansas/ml-starter
 Author: Benjamin Bolte
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `ml-starter-0.0.3/ml_starter.egg-info/SOURCES.txt` & `ml-starter-0.0.4/ml_starter.egg-info/SOURCES.txt`

 * *Files 11% similar despite different names*

```diff
@@ -75,24 +75,29 @@
 ml/tasks/losses/reduce.py
 ml/tasks/rl/__init__.py
 ml/tasks/rl/base.py
 ml/tasks/rl/replay.py
 ml/tasks/sl/__init__.py
 ml/tasks/sl/base.py
 ml/templates/copy_empty.py
+ml/templates/cpp/.clang-format
+ml/templates/cpp/.darglint
+ml/templates/cpp/.env
+ml/templates/cpp/.gitignore
 ml/templates/cpp/MANIFEST.in
 ml/templates/cpp/Makefile
 ml/templates/cpp/README.md
 ml/templates/cpp/pyproject.toml
 ml/templates/cpp/requirements-dev.txt
 ml/templates/cpp/requirements.txt
 ml/templates/cpp/setup.cfg
 ml/templates/cpp/setup.py
 ml/templates/cpp/configs/template.yaml
 ml/templates/cpp/project/__init__.py
+ml/templates/cpp/project/cpp/.gitignore
 ml/templates/cpp/project/cpp/CMakeLists.txt
 ml/templates/cpp/project/cpp/__init__.py
 ml/templates/cpp/project/cpp/torch_ops/CMakeLists.txt
 ml/templates/cpp/project/cpp/torch_ops/__init__.py
 ml/templates/cpp/project/cpp/torch_ops/torch_ops.cpp
 ml/templates/cpp/project/cpp/torch_ops/torch_ops.h
 ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.cpp
@@ -105,35 +110,46 @@
 ml/templates/cpp/project/scripts/__init__.py
 ml/templates/cpp/project/scripts/cli.py
 ml/templates/cpp/project/tasks/__init__.py
 ml/templates/cpp/project/tasks/template.py
 ml/templates/cpp/project/trainers/__init__.py
 ml/templates/cpp/tests/conftest.py
 ml/templates/cpp/tests/test_cpp_extension.py
+ml/templates/empty/.darglint
+ml/templates/empty/.env
+ml/templates/empty/.gitignore
 ml/templates/empty/MANIFEST.in
 ml/templates/empty/Makefile
 ml/templates/empty/README.md
 ml/templates/empty/pyproject.toml
 ml/templates/empty/requirements-dev.txt
 ml/templates/empty/requirements.txt
 ml/templates/empty/setup.cfg
 ml/templates/empty/setup.py
+ml/templates/empty/.github/pull_request_template.md
+ml/templates/empty/.github/workflows/core-checks.yml
+ml/templates/empty/.vscode/extensions.json
+ml/templates/empty/.vscode/settings.json
 ml/templates/empty/configs/template.yaml
 ml/templates/empty/project/__init__.py
 ml/templates/empty/project/loggers/__init__.py
 ml/templates/empty/project/lr_schedulers/__init__.py
 ml/templates/empty/project/models/__init__.py
 ml/templates/empty/project/models/template.py
 ml/templates/empty/project/optimizers/__init__.py
 ml/templates/empty/project/scripts/__init__.py
 ml/templates/empty/project/scripts/cli.py
 ml/templates/empty/project/tasks/__init__.py
 ml/templates/empty/project/tasks/template.py
 ml/templates/empty/project/trainers/__init__.py
 ml/templates/empty/tests/conftest.py
+ml/templates/empty/tests/test_dummy.py
+ml/templates/image/.darglint
+ml/templates/image/.env
+ml/templates/image/.gitignore
 ml/templates/image/MANIFEST.in
 ml/templates/image/Makefile
 ml/templates/image/README.md
 ml/templates/image/pyproject.toml
 ml/templates/image/requirements-dev.txt
 ml/templates/image/requirements.txt
 ml/templates/image/setup.cfg
@@ -148,14 +164,17 @@
 ml/templates/image/project/scripts/__init__.py
 ml/templates/image/project/scripts/cli.py
 ml/templates/image/project/tasks/__init__.py
 ml/templates/image/project/tasks/image_demo.py
 ml/templates/image/project/trainers/__init__.py
 ml/templates/image/tests/conftest.py
 ml/templates/image/tests/test_instantiate_configs.py
+ml/templates/rl/.darglint
+ml/templates/rl/.env
+ml/templates/rl/.gitignore
 ml/templates/rl/MANIFEST.in
 ml/templates/rl/Makefile
 ml/templates/rl/README.md
 ml/templates/rl/pyproject.toml
 ml/templates/rl/requirements-dev.txt
 ml/templates/rl/requirements.txt
 ml/templates/rl/setup.cfg
@@ -170,14 +189,18 @@
 ml/templates/rl/project/scripts/__init__.py
 ml/templates/rl/project/scripts/cli.py
 ml/templates/rl/project/tasks/__init__.py
 ml/templates/rl/project/tasks/rl_demo.py
 ml/templates/rl/project/tasks/rl_demo_env.py
 ml/templates/rl/project/trainers/__init__.py
 ml/templates/rl/tests/conftest.py
+ml/templates/rl/tests/test_dummy.py
+ml/templates/video/.darglint
+ml/templates/video/.env
+ml/templates/video/.gitignore
 ml/templates/video/MANIFEST.in
 ml/templates/video/Makefile
 ml/templates/video/README.md
 ml/templates/video/pyproject.toml
 ml/templates/video/requirements-dev.txt
 ml/templates/video/requirements.txt
 ml/templates/video/setup.cfg
@@ -191,14 +214,15 @@
 ml/templates/video/project/optimizers/__init__.py
 ml/templates/video/project/scripts/__init__.py
 ml/templates/video/project/scripts/cli.py
 ml/templates/video/project/tasks/__init__.py
 ml/templates/video/project/tasks/video_demo.py
 ml/templates/video/project/trainers/__init__.py
 ml/templates/video/tests/conftest.py
+ml/templates/video/tests/test_dummy.py
 ml/trainers/__init__.py
 ml/trainers/base.py
 ml/trainers/ddp.py
 ml/trainers/rl.py
 ml/trainers/sl.py
 ml/trainers/slurm.py
 ml/trainers/vanilla.py
```

### Comparing `ml-starter-0.0.3/pyproject.toml` & `ml-starter-0.0.4/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.3/setup.py` & `ml-starter-0.0.4/setup.py`

 * *Files identical despite different names*

