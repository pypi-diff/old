# Comparing `tmp/ml-starter-0.0.1.tar.gz` & `tmp/ml-starter-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ml-starter-0.0.1.tar", last modified: Thu Apr  6 20:16:10 2023, max compression
+gzip compressed data, was "ml-starter-0.0.2.tar", last modified: Thu Apr  6 21:24:47 2023, max compression
```

## Comparing `ml-starter-0.0.1.tar` & `ml-starter-0.0.2.tar`

### file list

```diff
@@ -1,148 +1,179 @@
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.173687 ml-starter-0.0.1/
--rw-r--r--   0 bbolte     (501) staff       (20)      113 2023-04-06 20:08:04.000000 ml-starter-0.0.1/MANIFEST.in
--rw-r--r--   0 bbolte     (501) staff       (20)     4285 2023-04-06 20:16:10.173788 ml-starter-0.0.1/PKG-INFO
--rw-r--r--   0 bbolte     (501) staff       (20)     3773 2023-04-06 20:14:27.000000 ml-starter-0.0.1/README.md
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.062976 ml-starter-0.0.1/ml/
--rw-r--r--   0 bbolte     (501) staff       (20)     2834 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)        5 2023-04-06 20:08:42.000000 ml-starter-0.0.1/ml/__version__.txt
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.068542 ml-starter-0.0.1/ml/core/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/core/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)      224 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/core/common_types.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3332 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/core/config.py
--rw-r--r--   0 bbolte     (501) staff       (20)     5356 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/core/env.py
--rw-r--r--   0 bbolte     (501) staff       (20)    23463 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/core/registry.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2068 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/core/state.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.073043 ml-starter-0.0.1/ml/loggers/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/loggers/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4905 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/loggers/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2726 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/loggers/meter.py
--rw-r--r--   0 bbolte     (501) staff       (20)    31809 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/loggers/multi.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4235 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/loggers/stdout.py
--rw-r--r--   0 bbolte     (501) staff       (20)     8960 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/loggers/tensorboard.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.079764 ml-starter-0.0.1/ml/lr_schedulers/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/lr_schedulers/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1916 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/lr_schedulers/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)      474 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/lr_schedulers/constant.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1734 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/lr_schedulers/cosine.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2342 2023-02-16 01:32:05.000000 ml-starter-0.0.1/ml/lr_schedulers/cosine_decay.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1639 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/lr_schedulers/linear.py
--rw-r--r--   0 bbolte     (501) staff       (20)      719 2023-02-16 01:32:05.000000 ml-starter-0.0.1/ml/lr_schedulers/linear_no_decay.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.081005 ml-starter-0.0.1/ml/lr_schedulers/scripts/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/lr_schedulers/scripts/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1897 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/lr_schedulers/scripts/plot.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.086283 ml-starter-0.0.1/ml/models/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/models/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2060 2023-02-16 22:55:25.000000 ml-starter-0.0.1/ml/models/activations.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2948 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/models/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3271 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/models/init.py
--rw-r--r--   0 bbolte     (501) staff       (20)    11127 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/models/norms.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.093321 ml-starter-0.0.1/ml/optimizers/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/optimizers/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1164 2023-04-06 01:12:00.000000 ml-starter-0.0.1/ml/optimizers/adam.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3057 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/optimizers/adamw.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3347 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/optimizers/adan.py
--rw-r--r--   0 bbolte     (501) staff       (20)      903 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/optimizers/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1120 2023-02-16 01:32:05.000000 ml-starter-0.0.1/ml/optimizers/sgd.py
--rw-r--r--   0 bbolte     (501) staff       (20)     6094 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/optimizers/shampoo.py
--rw-r--r--   0 bbolte     (501) staff       (20)      297 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/optimizers/types.py
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/py.typed
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.100802 ml-starter-0.0.1/ml/scripts/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/scripts/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2815 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/scripts/cli.py
--rw-r--r--   0 bbolte     (501) staff       (20)      641 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/scripts/compiler.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2438 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/scripts/create.py
--rw-r--r--   0 bbolte     (501) staff       (20)      465 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/scripts/mp_train.py
--rw-r--r--   0 bbolte     (501) staff       (20)      768 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/scripts/stage.py
--rw-r--r--   0 bbolte     (501) staff       (20)      722 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/scripts/train.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.104153 ml-starter-0.0.1/ml/tasks/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/tasks/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)    17502 2023-04-05 04:24:37.000000 ml-starter-0.0.1/ml/tasks/base.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.113800 ml-starter-0.0.1/ml/tasks/datasets/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/tasks/datasets/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1569 2023-03-02 19:48:07.000000 ml-starter-0.0.1/ml/tasks/datasets/async_iterable.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3778 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/tasks/datasets/clippify.py
--rw-r--r--   0 bbolte     (501) staff       (20)     7256 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/tasks/datasets/collate.py
--rw-r--r--   0 bbolte     (501) staff       (20)     8725 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/tasks/datasets/error_handling.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.117859 ml-starter-0.0.1/ml/tasks/datasets/impl/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-11-30 19:06:11.000000 ml-starter-0.0.1/ml/tasks/datasets/impl/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2160 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/datasets/impl/kinetics.py
--rw-r--r--   0 bbolte     (501) staff       (20)     5273 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/datasets/impl/pretraining.py
--rw-r--r--   0 bbolte     (501) staff       (20)      302 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/datasets/impl/types.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1232 2023-03-02 19:48:07.000000 ml-starter-0.0.1/ml/tasks/datasets/impl/utils.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2345 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/tasks/datasets/multi_iter.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1552 2023-02-16 21:55:34.000000 ml-starter-0.0.1/ml/tasks/datasets/samplers.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4439 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/tasks/datasets/streaming.py
--rw-r--r--   0 bbolte     (501) staff       (20)     6687 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/tasks/datasets/transforms.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1451 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/datasets/video_file.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.121818 ml-starter-0.0.1/ml/tasks/environments/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/environments/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1599 2023-04-05 04:24:37.000000 ml-starter-0.0.1/ml/tasks/environments/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1612 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/tasks/environments/utils.py
--rw-r--r--   0 bbolte     (501) staff       (20)    13112 2023-04-06 03:20:49.000000 ml-starter-0.0.1/ml/tasks/environments/worker.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.123011 ml-starter-0.0.1/ml/tasks/losses/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-12-01 22:00:43.000000 ml-starter-0.0.1/ml/tasks/losses/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)      931 2023-04-05 04:24:37.000000 ml-starter-0.0.1/ml/tasks/losses/reduce.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.128093 ml-starter-0.0.1/ml/tasks/rl/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/rl/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)    13501 2023-04-06 03:20:49.000000 ml-starter-0.0.1/ml/tasks/rl/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3108 2023-04-05 04:24:37.000000 ml-starter-0.0.1/ml/tasks/rl/replay.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.129426 ml-starter-0.0.1/ml/tasks/sl/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/sl/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1223 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/tasks/sl/base.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.136109 ml-starter-0.0.1/ml/trainers/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/trainers/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)    16412 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4395 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/ddp.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.141801 ml-starter-0.0.1/ml/trainers/mixins/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/trainers/mixins/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4737 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/mixins/cpu_stats.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.146746 ml-starter-0.0.1/ml/trainers/mixins/device/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/trainers/mixins/device/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1413 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/trainers/mixins/device/auto.py
--rw-r--r--   0 bbolte     (501) staff       (20)     7516 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/mixins/device/base.py
--rw-r--r--   0 bbolte     (501) staff       (20)      534 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/trainers/mixins/device/cpu.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1356 2023-04-06 03:20:49.000000 ml-starter-0.0.1/ml/trainers/mixins/device/gpu.py
--rw-r--r--   0 bbolte     (501) staff       (20)      775 2023-04-06 03:20:49.000000 ml-starter-0.0.1/ml/trainers/mixins/device/metal.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4144 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/mixins/gpu_stats.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2935 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/mixins/grad_clipping.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3148 2023-04-06 03:20:49.000000 ml-starter-0.0.1/ml/trainers/mixins/mixed_precision.py
--rw-r--r--   0 bbolte     (501) staff       (20)     5536 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/mixins/profiler.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1262 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/mixins/step_wrapper.py
--rw-r--r--   0 bbolte     (501) staff       (20)     8638 2023-04-05 04:24:37.000000 ml-starter-0.0.1/ml/trainers/rl.py
--rw-r--r--   0 bbolte     (501) staff       (20)    10088 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/sl.py
--rw-r--r--   0 bbolte     (501) staff       (20)    10349 2023-04-05 04:42:06.000000 ml-starter-0.0.1/ml/trainers/slurm.py
--rw-r--r--   0 bbolte     (501) staff       (20)    11073 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/trainers/vanilla.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.167815 ml-starter-0.0.1/ml/utils/
--rw-r--r--   0 bbolte     (501) staff       (20)        0 2022-10-14 14:50:17.000000 ml-starter-0.0.1/ml/utils/__init__.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2864 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/utils/argparse.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2582 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/utils/atomic.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1580 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/utils/augmentation.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4608 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/utils/caching.py
--rw-r--r--   0 bbolte     (501) staff       (20)      977 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/utils/call_train.py
--rw-r--r--   0 bbolte     (501) staff       (20)      162 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/utils/checks.py
--rw-r--r--   0 bbolte     (501) staff       (20)     3009 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/utils/cli.py
--rw-r--r--   0 bbolte     (501) staff       (20)     1059 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/utils/colors.py
--rw-r--r--   0 bbolte     (501) staff       (20)    12052 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/utils/compiler.py
--rw-r--r--   0 bbolte     (501) staff       (20)      683 2023-02-16 01:32:05.000000 ml-starter-0.0.1/ml/utils/data.py
--rw-r--r--   0 bbolte     (501) staff       (20)      820 2023-02-16 01:32:05.000000 ml-starter-0.0.1/ml/utils/datetime.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2180 2023-03-02 19:48:07.000000 ml-starter-0.0.1/ml/utils/distributed.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2388 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/utils/large_models.py
--rw-r--r--   0 bbolte     (501) staff       (20)     4346 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/utils/logging.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2525 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/utils/meter.py
--rw-r--r--   0 bbolte     (501) staff       (20)      259 2023-02-16 01:32:06.000000 ml-starter-0.0.1/ml/utils/networking.py
--rw-r--r--   0 bbolte     (501) staff       (20)      426 2023-04-06 20:08:04.000000 ml-starter-0.0.1/ml/utils/paths.py
--rw-r--r--   0 bbolte     (501) staff       (20)      317 2023-03-02 21:50:13.000000 ml-starter-0.0.1/ml/utils/random.py
--rw-r--r--   0 bbolte     (501) staff       (20)     2394 2023-03-30 04:55:03.000000 ml-starter-0.0.1/ml/utils/timer.py
--rw-r--r--   0 bbolte     (501) staff       (20)    14152 2023-04-04 17:32:06.000000 ml-starter-0.0.1/ml/utils/video.py
-drwxr-xr-x   0 bbolte     (501) staff       (20)        0 2023-04-06 20:16:10.173098 ml-starter-0.0.1/ml_starter.egg-info/
--rw-r--r--   0 bbolte     (501) staff       (20)     4285 2023-04-06 20:16:09.000000 ml-starter-0.0.1/ml_starter.egg-info/PKG-INFO
--rw-r--r--   0 bbolte     (501) staff       (20)     3127 2023-04-06 20:16:10.000000 ml-starter-0.0.1/ml_starter.egg-info/SOURCES.txt
--rw-r--r--   0 bbolte     (501) staff       (20)        1 2023-04-06 20:16:09.000000 ml-starter-0.0.1/ml_starter.egg-info/dependency_links.txt
--rw-r--r--   0 bbolte     (501) staff       (20)       75 2023-04-06 20:16:09.000000 ml-starter-0.0.1/ml_starter.egg-info/entry_points.txt
--rw-r--r--   0 bbolte     (501) staff       (20)      146 2023-04-06 20:16:09.000000 ml-starter-0.0.1/ml_starter.egg-info/requires.txt
--rw-r--r--   0 bbolte     (501) staff       (20)        3 2023-04-06 20:16:09.000000 ml-starter-0.0.1/ml_starter.egg-info/top_level.txt
--rw-r--r--   0 bbolte     (501) staff       (20)     1387 2023-04-06 03:20:49.000000 ml-starter-0.0.1/pyproject.toml
--rw-r--r--   0 bbolte     (501) staff       (20)       56 2023-04-06 20:08:04.000000 ml-starter-0.0.1/requirements-dev.txt
--rw-r--r--   0 bbolte     (501) staff       (20)      127 2023-04-06 20:08:04.000000 ml-starter-0.0.1/requirements.txt
--rw-r--r--   0 bbolte     (501) staff       (20)      230 2023-04-06 20:16:10.174394 ml-starter-0.0.1/setup.cfg
--rw-r--r--   0 bbolte     (501) staff       (20)     1173 2023-04-06 20:14:29.000000 ml-starter-0.0.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.899175 ml-starter-0.0.2/
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-04-06 21:24:36.000000 ml-starter-0.0.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 21:24:47.899175 ml-starter-0.0.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3773 2023-04-06 21:24:36.000000 ml-starter-0.0.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.859175 ml-starter-0.0.2/ml/
+-rw-r--r--   0 runner    (1001) docker     (123)     2834 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/__version__.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.859175 ml-starter-0.0.2/ml/core/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/core/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      224 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/core/common_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3332 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/core/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5356 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/core/env.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23463 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/core/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/core/state.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.863175 ml-starter-0.0.2/ml/loggers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/loggers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4905 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/loggers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2726 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/loggers/meter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31809 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/loggers/multi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/loggers/stdout.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/loggers/tensorboard.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.863175 ml-starter-0.0.2/ml/lr_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      474 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/constant.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1734 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/cosine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2342 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/cosine_decay.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/linear.py
+-rw-r--r--   0 runner    (1001) docker     (123)      719 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/linear_no_decay.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.863175 ml-starter-0.0.2/ml/lr_schedulers/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1897 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/lr_schedulers/scripts/plot.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.867175 ml-starter-0.0.2/ml/models/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2060 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/models/activations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2948 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/models/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3271 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/models/init.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11127 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/models/norms.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.867175 ml-starter-0.0.2/ml/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/adam.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3057 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/adamw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3347 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/adan.py
+-rw-r--r--   0 runner    (1001) docker     (123)      903 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/sgd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6094 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/shampoo.py
+-rw-r--r--   0 runner    (1001) docker     (123)      297 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/optimizers/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.871175 ml-starter-0.0.2/ml/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2815 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2431 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/create.py
+-rw-r--r--   0 runner    (1001) docker     (123)      465 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/mp_train.py
+-rw-r--r--   0 runner    (1001) docker     (123)      768 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/stage.py
+-rw-r--r--   0 runner    (1001) docker     (123)      722 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/scripts/train.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.871175 ml-starter-0.0.2/ml/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17502 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.875175 ml-starter-0.0.2/ml/tasks/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/async_iterable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3778 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/clippify.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7256 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/collate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8725 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/error_handling.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.875175 ml-starter-0.0.2/ml/tasks/datasets/impl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/impl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2160 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/impl/kinetics.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5273 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/impl/pretraining.py
+-rw-r--r--   0 runner    (1001) docker     (123)      302 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/impl/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1232 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/impl/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2345 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/multi_iter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1552 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/samplers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4439 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/streaming.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6687 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/transforms.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/datasets/video_file.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.875175 ml-starter-0.0.2/ml/tasks/environments/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/environments/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1599 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/environments/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1612 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/environments/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13383 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/environments/worker.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/tasks/losses/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      931 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/losses/reduce.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/tasks/rl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/rl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13501 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/rl/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3108 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/rl/replay.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/tasks/sl/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/sl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1223 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/tasks/sl/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.855174 ml-starter-0.0.2/ml/templates/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/cpp/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/MANIFEST.in
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.851174 ml-starter-0.0.2/ml/templates/cpp/project/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/cpp/project/cpp/
+-rw-r--r--   0 runner    (1001) docker     (123)      326 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/project/cpp/CMakeLists.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/
+-rw-r--r--   0 runner    (1001) docker     (123)     1132 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/CMakeLists.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/ops/
+-rw-r--r--   0 runner    (1001) docker     (123)     1357 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      278 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/ops/nucleus_sampling.h
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/torch_ops.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/project/cpp/torch_ops/torch_ops.h
+-rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/cpp/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/empty/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/empty/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/empty/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/empty/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/image/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/image/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/image/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/image/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.879175 ml-starter-0.0.2/ml/templates/rl/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/rl/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/rl/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/rl/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.883175 ml-starter-0.0.2/ml/templates/video/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/video/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/video/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       70 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/templates/video/requirements.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.887175 ml-starter-0.0.2/ml/trainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16412 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4395 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/ddp.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.887175 ml-starter-0.0.2/ml/trainers/mixins/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4737 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/cpu_stats.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.891175 ml-starter-0.0.2/ml/trainers/mixins/device/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/device/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1413 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/device/auto.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7516 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/device/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      534 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/device/cpu.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/device/gpu.py
+-rw-r--r--   0 runner    (1001) docker     (123)      775 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/device/metal.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4144 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/gpu_stats.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2935 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/grad_clipping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3148 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/mixed_precision.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5536 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/profiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1262 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/mixins/step_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8638 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/rl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10088 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/sl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10349 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/slurm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11073 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/trainers/vanilla.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.895175 ml-starter-0.0.2/ml/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2864 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/argparse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2582 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/atomic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1580 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/augmentation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4608 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/caching.py
+-rw-r--r--   0 runner    (1001) docker     (123)      977 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/call_train.py
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/checks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3009 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1059 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/colors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12052 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      820 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/datetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2180 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/distributed.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/large_models.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4346 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2525 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/meter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      259 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/networking.py
+-rw-r--r--   0 runner    (1001) docker     (123)      426 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/paths.py
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/random.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2394 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/timer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14152 2023-04-06 21:24:36.000000 ml-starter-0.0.2/ml/utils/video.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:47.899175 ml-starter-0.0.2/ml_starter.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 21:24:47.000000 ml-starter-0.0.2/ml_starter.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3975 2023-04-06 21:24:47.000000 ml-starter-0.0.2/ml_starter.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:24:47.000000 ml-starter-0.0.2/ml_starter.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-04-06 21:24:47.000000 ml-starter-0.0.2/ml_starter.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 21:24:47.000000 ml-starter-0.0.2/ml_starter.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        3 2023-04-06 21:24:47.000000 ml-starter-0.0.2/ml_starter.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1387 2023-04-06 21:24:36.000000 ml-starter-0.0.2/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       56 2023-04-06 21:24:36.000000 ml-starter-0.0.2/requirements-dev.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      127 2023-04-06 21:24:36.000000 ml-starter-0.0.2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-06 21:24:47.899175 ml-starter-0.0.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1172 2023-04-06 21:24:36.000000 ml-starter-0.0.2/setup.py
```

### Comparing `ml-starter-0.0.1/PKG-INFO` & `ml-starter-0.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Metadata-Version: 2.1
 Name: ml-starter
-Version: 0.0.1
+Version: 0.0.2
 Summary: ML project template repository
-Home-page: https://github.com/codekansas/ml-template
+Home-page: https://github.com/codekansas/ml-starter
 Author: Benjamin Bolte
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.10
```

### Comparing `ml-starter-0.0.1/README.md` & `ml-starter-0.0.2/README.md`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/__init__.py` & `ml-starter-0.0.2/ml/__init__.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/core/config.py` & `ml-starter-0.0.2/ml/core/config.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/core/env.py` & `ml-starter-0.0.2/ml/core/env.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/core/registry.py` & `ml-starter-0.0.2/ml/core/registry.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/core/state.py` & `ml-starter-0.0.2/ml/core/state.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/loggers/base.py` & `ml-starter-0.0.2/ml/loggers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/loggers/meter.py` & `ml-starter-0.0.2/ml/loggers/meter.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/loggers/multi.py` & `ml-starter-0.0.2/ml/loggers/multi.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/loggers/stdout.py` & `ml-starter-0.0.2/ml/loggers/stdout.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/loggers/tensorboard.py` & `ml-starter-0.0.2/ml/loggers/tensorboard.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/lr_schedulers/base.py` & `ml-starter-0.0.2/ml/lr_schedulers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/lr_schedulers/cosine.py` & `ml-starter-0.0.2/ml/lr_schedulers/cosine.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/lr_schedulers/cosine_decay.py` & `ml-starter-0.0.2/ml/lr_schedulers/cosine_decay.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/lr_schedulers/linear.py` & `ml-starter-0.0.2/ml/lr_schedulers/linear.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/lr_schedulers/linear_no_decay.py` & `ml-starter-0.0.2/ml/lr_schedulers/linear_no_decay.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/lr_schedulers/scripts/plot.py` & `ml-starter-0.0.2/ml/lr_schedulers/scripts/plot.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/models/activations.py` & `ml-starter-0.0.2/ml/models/activations.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/models/base.py` & `ml-starter-0.0.2/ml/models/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/models/init.py` & `ml-starter-0.0.2/ml/models/init.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/models/norms.py` & `ml-starter-0.0.2/ml/models/norms.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/optimizers/adam.py` & `ml-starter-0.0.2/ml/optimizers/adam.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/optimizers/adamw.py` & `ml-starter-0.0.2/ml/optimizers/adamw.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/optimizers/adan.py` & `ml-starter-0.0.2/ml/optimizers/adan.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/optimizers/base.py` & `ml-starter-0.0.2/ml/optimizers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/optimizers/sgd.py` & `ml-starter-0.0.2/ml/optimizers/sgd.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/optimizers/shampoo.py` & `ml-starter-0.0.2/ml/optimizers/shampoo.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/scripts/cli.py` & `ml-starter-0.0.2/ml/scripts/cli.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/scripts/compiler.py` & `ml-starter-0.0.2/ml/scripts/compiler.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/scripts/create.py` & `ml-starter-0.0.2/ml/scripts/create.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import sys
 from pathlib import Path
 
 from ml.utils.colors import colorize
 
 
 def get_template_choices() -> dict[str, Path]:
-    root_dir = Path(__file__).parent.parent.parent / "templates"
+    root_dir = Path(__file__).parent.parent / "templates"
     template_choices = {}
     for template_dir in root_dir.iterdir():
         if template_dir.is_dir() and (template_dir / "setup.py").exists():
             template_choices[template_dir.name] = template_dir
     return template_choices
```

### Comparing `ml-starter-0.0.1/ml/scripts/stage.py` & `ml-starter-0.0.2/ml/scripts/stage.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/scripts/train.py` & `ml-starter-0.0.2/ml/scripts/train.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/base.py` & `ml-starter-0.0.2/ml/tasks/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/async_iterable.py` & `ml-starter-0.0.2/ml/tasks/datasets/async_iterable.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/clippify.py` & `ml-starter-0.0.2/ml/tasks/datasets/clippify.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/collate.py` & `ml-starter-0.0.2/ml/tasks/datasets/collate.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/error_handling.py` & `ml-starter-0.0.2/ml/tasks/datasets/error_handling.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/impl/kinetics.py` & `ml-starter-0.0.2/ml/tasks/datasets/impl/kinetics.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/impl/pretraining.py` & `ml-starter-0.0.2/ml/tasks/datasets/impl/pretraining.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/impl/utils.py` & `ml-starter-0.0.2/ml/tasks/datasets/impl/utils.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/multi_iter.py` & `ml-starter-0.0.2/ml/tasks/datasets/multi_iter.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/samplers.py` & `ml-starter-0.0.2/ml/tasks/datasets/samplers.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/streaming.py` & `ml-starter-0.0.2/ml/tasks/datasets/streaming.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/transforms.py` & `ml-starter-0.0.2/ml/tasks/datasets/transforms.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/datasets/video_file.py` & `ml-starter-0.0.2/ml/tasks/datasets/video_file.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/environments/base.py` & `ml-starter-0.0.2/ml/tasks/environments/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/environments/utils.py` & `ml-starter-0.0.2/ml/tasks/environments/utils.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/environments/worker.py` & `ml-starter-0.0.2/ml/tasks/environments/worker.py`

 * *Files 2% similar despite different names*

```diff
@@ -181,22 +181,25 @@
         num_workers: int,
     ) -> Sequence["AsyncEnvironmentWorker[RLState, RLAction]"]:
         manager = mp.Manager()
         return [cls(env, manager, rank=rank, world_size=num_workers) for rank in range(num_workers)]
 
     def cleanup(self) -> None:
         logger.debug("Cleaning up task...")
-        self.send_action("close")
-        self._proc.join(timeout=self.cleanup_time)
-        if self._proc.is_alive():
-            logger.warning("Process failed to finish after %.2f seconds; killing", self.cleanup_time)
-            if isinstance(self._proc, threading.Thread):
-                self._proc._stop()
-            else:
-                self._proc.kill()
+        try:
+            self.send_action("close")
+            self._proc.join(timeout=self.cleanup_time)
+            if self._proc.is_alive():
+                logger.warning("Process failed to finish after %.2f seconds; killing", self.cleanup_time)
+                if isinstance(self._proc, threading.Thread):
+                    self._proc._stop()
+                else:
+                    self._proc.kill()
+        except Exception:
+            logger.exception("Exception while cleaning up task")
 
     @classmethod
     def _thread(
         cls,
         env: "Environment[RLState, RLAction]",
         seed: int,
         action_queue: "Queue[RLAction | SpecialAction]",
@@ -337,20 +340,23 @@
             for env_id, (worker, action_queue) in enumerate(zip(workers, self.action_queues))
         ]
         for proc in self._procs:
             proc.start()
 
     def cleanup(self) -> None:
         logger.debug("Cleaning up worker pool...")
-        clear_queue(self.state_queue)
-        for action_queue in self.action_queues:
-            clear_queue(action_queue)
-            action_queue.put("close")
-        for proc in self._procs:
-            proc.join()
+        try:
+            clear_queue(self.state_queue)
+            for action_queue in self.action_queues:
+                clear_queue(action_queue)
+                action_queue.put("close")
+            for proc in self._procs:
+                proc.join()
+        except Exception:
+            logger.exception("Exception while cleaning up worker pool")
 
     def reset(self) -> None:
         clear_queue(self.state_queue)
         for action_queue in self.action_queues:
             clear_queue(action_queue)
             action_queue.put("reset")
```

### Comparing `ml-starter-0.0.1/ml/tasks/losses/reduce.py` & `ml-starter-0.0.2/ml/tasks/losses/reduce.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/rl/base.py` & `ml-starter-0.0.2/ml/tasks/rl/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/rl/replay.py` & `ml-starter-0.0.2/ml/tasks/rl/replay.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/tasks/sl/base.py` & `ml-starter-0.0.2/ml/tasks/sl/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/base.py` & `ml-starter-0.0.2/ml/trainers/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/ddp.py` & `ml-starter-0.0.2/ml/trainers/ddp.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/cpu_stats.py` & `ml-starter-0.0.2/ml/trainers/mixins/cpu_stats.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/device/auto.py` & `ml-starter-0.0.2/ml/trainers/mixins/device/auto.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/device/base.py` & `ml-starter-0.0.2/ml/trainers/mixins/device/base.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/device/cpu.py` & `ml-starter-0.0.2/ml/trainers/mixins/device/cpu.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/device/gpu.py` & `ml-starter-0.0.2/ml/trainers/mixins/device/gpu.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/device/metal.py` & `ml-starter-0.0.2/ml/trainers/mixins/device/metal.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/gpu_stats.py` & `ml-starter-0.0.2/ml/trainers/mixins/gpu_stats.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/grad_clipping.py` & `ml-starter-0.0.2/ml/trainers/mixins/grad_clipping.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/mixed_precision.py` & `ml-starter-0.0.2/ml/trainers/mixins/mixed_precision.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/profiler.py` & `ml-starter-0.0.2/ml/trainers/mixins/profiler.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/mixins/step_wrapper.py` & `ml-starter-0.0.2/ml/trainers/mixins/step_wrapper.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/rl.py` & `ml-starter-0.0.2/ml/trainers/rl.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/sl.py` & `ml-starter-0.0.2/ml/trainers/sl.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/slurm.py` & `ml-starter-0.0.2/ml/trainers/slurm.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/trainers/vanilla.py` & `ml-starter-0.0.2/ml/trainers/vanilla.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/argparse.py` & `ml-starter-0.0.2/ml/utils/argparse.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/atomic.py` & `ml-starter-0.0.2/ml/utils/atomic.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/augmentation.py` & `ml-starter-0.0.2/ml/utils/augmentation.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/caching.py` & `ml-starter-0.0.2/ml/utils/caching.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/call_train.py` & `ml-starter-0.0.2/ml/utils/call_train.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/cli.py` & `ml-starter-0.0.2/ml/utils/cli.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/colors.py` & `ml-starter-0.0.2/ml/utils/colors.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/compiler.py` & `ml-starter-0.0.2/ml/utils/compiler.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/data.py` & `ml-starter-0.0.2/ml/utils/data.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/datetime.py` & `ml-starter-0.0.2/ml/utils/datetime.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/distributed.py` & `ml-starter-0.0.2/ml/utils/distributed.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/large_models.py` & `ml-starter-0.0.2/ml/utils/large_models.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/logging.py` & `ml-starter-0.0.2/ml/utils/logging.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/meter.py` & `ml-starter-0.0.2/ml/utils/meter.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/timer.py` & `ml-starter-0.0.2/ml/utils/timer.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml/utils/video.py` & `ml-starter-0.0.2/ml/utils/video.py`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/ml_starter.egg-info/PKG-INFO` & `ml-starter-0.0.2/ml_starter.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 Metadata-Version: 2.1
 Name: ml-starter
-Version: 0.0.1
+Version: 0.0.2
 Summary: ML project template repository
-Home-page: https://github.com/codekansas/ml-template
+Home-page: https://github.com/codekansas/ml-starter
 Author: Benjamin Bolte
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.10
```

### Comparing `ml-starter-0.0.1/pyproject.toml` & `ml-starter-0.0.2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `ml-starter-0.0.1/setup.py` & `ml-starter-0.0.2/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -19,15 +19,15 @@
 
 
 setup(
     name="ml-starter",
     version=version,
     description="ML project template repository",
     author="Benjamin Bolte",
-    url="https://github.com/codekansas/ml-template",
+    url="https://github.com/codekansas/ml-starter",
     long_description=long_description,
     long_description_content_type="text/markdown",
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
         "License :: OSI Approved :: MIT License",
```

