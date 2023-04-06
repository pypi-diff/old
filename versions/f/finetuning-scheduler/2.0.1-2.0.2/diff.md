# Comparing `tmp/finetuning-scheduler-2.0.1.tar.gz` & `tmp/finetuning-scheduler-2.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "finetuning-scheduler-2.0.1.tar", last modified: Wed Apr  5 17:27:24 2023, max compression
+gzip compressed data, was "finetuning-scheduler-2.0.2.tar", last modified: Thu Apr  6 21:15:19 2023, max compression
```

## Comparing `finetuning-scheduler-2.0.1.tar` & `finetuning-scheduler-2.0.2.tar`

### file list

```diff
@@ -1,91 +1,97 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.338562 finetuning-scheduler-2.0.1/.actions/
--rw-r--r--   0 runner    (1001) docker     (122)     6935 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/.actions/assistant.py
--rw-r--r--   0 runner    (1001) docker     (122)    13735 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/CHANGELOG.md
--rw-r--r--   0 runner    (1001) docker     (122)     2666 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/CITATION.cff
--rw-r--r--   0 runner    (1001) docker     (122)    11349 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)      569 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)    11344 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)    10897 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/README.md
--rw-r--r--   0 runner    (1001) docker     (122)       21 2023-04-05 17:27:15.000000 finetuning-scheduler-2.0.1/SECURITY.md
--rw-r--r--   0 runner    (1001) docker     (122)     2404 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.338562 finetuning-scheduler-2.0.1/requirements/
--rw-r--r--   0 runner    (1001) docker     (122)      228 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/base.txt
--rw-r--r--   0 runner    (1001) docker     (122)      150 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/cli.txt
--rw-r--r--   0 runner    (1001) docker     (122)      438 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/devel.txt
--rw-r--r--   0 runner    (1001) docker     (122)      473 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/docs.txt
--rw-r--r--   0 runner    (1001) docker     (122)       84 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/examples.txt
--rw-r--r--   0 runner    (1001) docker     (122)       94 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/extra.txt
--rw-r--r--   0 runner    (1001) docker     (122)      179 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/ipynb.txt
--rw-r--r--   0 runner    (1001) docker     (122)      252 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/standalone_base.txt
--rw-r--r--   0 runner    (1001) docker     (122)      145 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements/test.txt
--rw-r--r--   0 runner    (1001) docker     (122)       27 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (122)     6840 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.338562 finetuning-scheduler-2.0.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/finetuning_scheduler/
--rw-r--r--   0 runner    (1001) docker     (122)     2099 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/__about__.py
--rw-r--r--   0 runner    (1001) docker     (122)     1851 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    45364 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/fts.py
--rw-r--r--   0 runner    (1001) docker     (122)    88554 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/fts_supporters.py
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/py.typed
--rw-r--r--   0 runner    (1001) docker     (122)     5129 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/setup_tools.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/
--rw-r--r--   0 runner    (1001) docker     (122)      835 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    12618 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/base.py
--rw-r--r--   0 runner    (1001) docker     (122)    40200 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/fsdp.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)    11344 2023-04-05 17:27:24.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     3156 2023-04-05 17:27:24.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-05 17:27:24.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-05 17:27:24.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (122)     1269 2023-04-05 17:27:24.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       34 2023-04-05 17:27:24.000000 finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/fts_examples/
--rw-r--r--   0 runner    (1001) docker     (122)      195 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/fts_examples/legacy/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     6933 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/cli_experiment_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/
--rw-r--r--   0 runner    (1001) docker     (122)      498 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/RteBoolqModule_ft_schedule_deberta_base.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      650 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.338562 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/
--rw-r--r--   0 runner    (1001) docker     (122)     1503 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     2002 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     2047 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.342562 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/
--rw-r--r--   0 runner    (1001) docker     (122)     1136 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/explicit_reinit_lr.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1169 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1524 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1011 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/fts_defaults.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      683 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/fts_explicit.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      559 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/fts_implicit.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      340 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/nofts_baseline.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     6848 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/fts_fsdp_superglue.py
--rw-r--r--   0 runner    (1001) docker     (122)    17901 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/fts_superglue.py
--rw-r--r--   0 runner    (1001) docker     (122)    18350 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/legacy/patched_adamw.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/src/fts_examples/stable/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     7788 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/cli_experiment_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/
--rw-r--r--   0 runner    (1001) docker     (122)      498 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/RteBoolqModule_ft_schedule_deberta_base.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      650 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.338562 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/
--rw-r--r--   0 runner    (1001) docker     (122)     1423 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     2234 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     2345 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/
--rw-r--r--   0 runner    (1001) docker     (122)     1136 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/explicit_reinit_lr.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1169 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1524 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     1011 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/fts_defaults.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      683 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/fts_explicit.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      559 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/fts_implicit.yaml
--rw-r--r--   0 runner    (1001) docker     (122)      340 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/config/nofts_baseline.yaml
--rw-r--r--   0 runner    (1001) docker     (122)     4545 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/extended_profiler.py
--rw-r--r--   0 runner    (1001) docker     (122)    15557 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/src/fts_examples/stable/fts_superglue.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-05 17:27:24.346562 finetuning-scheduler-2.0.1/tests/
--rw-r--r--   0 runner    (1001) docker     (122)    88646 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/tests/test_finetuning_scheduler_callback.py
--rw-r--r--   0 runner    (1001) docker     (122)    35986 2023-04-05 17:27:16.000000 finetuning-scheduler-2.0.1/tests/test_fsdp.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.472727 finetuning-scheduler-2.0.2/.actions/
+-rw-r--r--   0 runner    (1001) docker     (122)     6935 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/.actions/assistant.py
+-rw-r--r--   0 runner    (1001) docker     (122)    14615 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/CHANGELOG.md
+-rw-r--r--   0 runner    (1001) docker     (122)     2764 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/CITATION.cff
+-rw-r--r--   0 runner    (1001) docker     (122)    11349 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)      569 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)    11482 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    11035 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)       21 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/SECURITY.md
+-rw-r--r--   0 runner    (1001) docker     (122)     2405 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.472727 finetuning-scheduler-2.0.2/requirements/
+-rw-r--r--   0 runner    (1001) docker     (122)      228 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/base.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       95 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/cli.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      438 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/devel.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      473 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/docs.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       84 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/examples.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       94 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/extra.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      179 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/ipynb.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      252 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/standalone_base.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      145 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements/test.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       27 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/setup.cfg
+-rwxr-xr-x   0 runner    (1001) docker     (122)     6919 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.468727 finetuning-scheduler-2.0.2/src/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.472727 finetuning-scheduler-2.0.2/src/finetuning_scheduler/
+-rw-r--r--   0 runner    (1001) docker     (122)     2099 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/__about__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      674 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    49224 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/fts.py
+-rw-r--r--   0 runner    (1001) docker     (122)   101936 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/fts_supporters.py
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/py.typed
+-rw-r--r--   0 runner    (1001) docker     (122)     5129 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/setup_tools.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/
+-rw-r--r--   0 runner    (1001) docker     (122)      835 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    14803 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/base.py
+-rw-r--r--   0 runner    (1001) docker     (122)    40034 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/fsdp.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1623 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler/types.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)    11482 2023-04-06 21:15:19.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     3555 2023-04-06 21:15:19.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 21:15:19.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 21:15:19.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (122)     1364 2023-04-06 21:15:19.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       34 2023-04-06 21:15:19.000000 finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/fts_examples/
+-rw-r--r--   0 runner    (1001) docker     (122)      195 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/fts_examples/legacy/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6933 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/cli_experiment_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/
+-rw-r--r--   0 runner    (1001) docker     (122)      498 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/RteBoolqModule_ft_schedule_deberta_base.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      650 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.468727 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/
+-rw-r--r--   0 runner    (1001) docker     (122)     1503 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     2002 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     2047 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/
+-rw-r--r--   0 runner    (1001) docker     (122)     1136 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/explicit_reinit_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1169 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1524 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1011 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/fts_defaults.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      683 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/fts_explicit.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      559 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/fts_implicit.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      340 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/nofts_baseline.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     6848 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/fts_fsdp_superglue.py
+-rw-r--r--   0 runner    (1001) docker     (122)    17790 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/fts_superglue.py
+-rw-r--r--   0 runner    (1001) docker     (122)    18350 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/legacy/patched_adamw.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.476727 finetuning-scheduler-2.0.2/src/fts_examples/stable/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7788 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/cli_experiment_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/
+-rw-r--r--   0 runner    (1001) docker     (122)      498 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/RteBoolqModule_ft_schedule_deberta_base.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      650 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.468727 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/
+-rw-r--r--   0 runner    (1001) docker     (122)     1423 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     2234 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     2345 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/
+-rw-r--r--   0 runner    (1001) docker     (122)     1136 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/explicit_reinit_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1145 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1524 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_optim_lr/
+-rw-r--r--   0 runner    (1001) docker     (122)     1457 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_optim_lr/explicit_reinit_optim_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1242 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_optim_lr/fts_explicit_reinit_optim_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1745 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_optim_lr/fts_implicit_reinit_optim_lr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1788 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_optim_lr/fts_implicit_reinit_optim_lr_use_curr.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     1011 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/fts_defaults.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      683 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/fts_explicit.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      559 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/fts_implicit.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)      340 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/config/nofts_baseline.yaml
+-rw-r--r--   0 runner    (1001) docker     (122)     4545 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/extended_profiler.py
+-rw-r--r--   0 runner    (1001) docker     (122)    15557 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/src/fts_examples/stable/fts_superglue.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:15:19.480727 finetuning-scheduler-2.0.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)   108541 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/tests/test_finetuning_scheduler_callback.py
+-rw-r--r--   0 runner    (1001) docker     (122)    40054 2023-04-06 21:15:10.000000 finetuning-scheduler-2.0.2/tests/test_fsdp.py
```

### Comparing `finetuning-scheduler-2.0.1/.actions/assistant.py` & `finetuning-scheduler-2.0.2/.actions/assistant.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/CHANGELOG.md` & `finetuning-scheduler-2.0.2/CHANGELOG.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,29 @@
 # Changelog
 
 All notable changes to this project will be documented in this file.
 
 The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).
 
+## [2.0.2] - 2023-04-06
+
+### Added
+
+- Beta support for [optimizer reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/optimizer_reinitialization.html). Resolves [#6](https://github.com/speediedan/finetuning-scheduler/issues/6)
+- Use structural typing for Fine-Tuning Scheduler supported optimizers with ``ParamGroupAddable``
+- Support for ``jsonargparse`` version ``4.20.1``
+
+### Changed
+
+- During schedule phase transitions, the latest LR state will be restored before proceeding with the next phase configuration and execution (mostly relevant to lr scheduler and optimizer reinitialization but also improves configuration when restoring best checkpoints across multiple depths)
+
+### Fixed
+
+- Allow sharded optimizers ``ZeroRedundancyOptimizer`` to be properly reconfigured if necessary in the context of ``enforce_phase0_params`` set to ``True``.
+
 
 ## [2.0.1] - 2023-04-05
 
 ### Added
 
 - Support for PyTorch Lightning 2.0.1
 - Lightning support for ``use_orig_params`` via ([#16733](https://github.com/Lightning-AI/lightning/pull/16733))
```

### Comparing `finetuning-scheduler-2.0.1/CITATION.cff` & `finetuning-scheduler-2.0.2/CITATION.cff`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 message: "If you want to cite this extension, feel free to use this 😊"
 title: "Fine-Tuning Scheduler"
 abstract: "A PyTorch Lightning extension that enhances model experimentation with flexible fine-tuning schedules."
 date-released: 2022-02-04
 authors:
   - family-names: "Dale"
     given-names: "Dan"
-version: 2.0.0
+version: 2.0.2
 identifiers:
   - description: "Fine-Tuning Scheduler (all versions)"
     type: doi
     value: 10.5281/zenodo.6463952
   - description: "Fine-Tuning Scheduler (v0.1.1)"
     type: doi
     value: 10.5281/zenodo.6463992
@@ -67,14 +67,17 @@
     value: 10.5281/zenodo.7569501
   - description: "Fine-Tuning Scheduler (v0.4.1)"
     type: doi
     value: 10.5281/zenodo.7734581
   - description: "Fine-Tuning Scheduler (v2.0.0)"
     type: doi
     value: 10.5281/zenodo.7738722
+  - description: "Fine-Tuning Scheduler (v2.0.1)"
+    type: doi
+    value: 10.5281/zenodo.7803180
 license: "Apache-2.0"
 url: "https://finetuning-scheduler.readthedocs.io/"
 repository-code: "https://github.com/speediedan/finetuning-scheduler"
 keywords:
   - machine learning
   - deep learning
   - artificial intelligence
```

### Comparing `finetuning-scheduler-2.0.1/LICENSE` & `finetuning-scheduler-2.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/MANIFEST.in` & `finetuning-scheduler-2.0.2/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/PKG-INFO` & `finetuning-scheduler-2.0.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: finetuning-scheduler
-Version: 2.0.1
+Version: 2.0.2
 Summary: A PyTorch Lightning extension that enhances model experimentation with flexible fine-tuning schedules.
 Home-page: https://github.com/speediedan/finetuning-scheduler
 Download-URL: https://github.com/speediedan/finetuning-scheduler
 Author: Dan Dale
 Author-email: danny.dale@gmail.com
 License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/speediedan/finetuning-scheduler/issues
@@ -33,39 +33,39 @@
 Provides-Extra: cli
 Provides-Extra: dev
 Provides-Extra: all
 License-File: LICENSE
 
 <div align="center">
 
-<img src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.1/docs/source/_static/images/logos/logo_fts.png" width="401px">
+<img src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.2/docs/source/_static/images/logos/logo_fts.png" width="401px">
 
 **A PyTorch Lightning extension that enhances model experimentation with flexible fine-tuning schedules.**
 
 ______________________________________________________________________
 
 <p align="center">
   <a href="https://finetuning-scheduler.readthedocs.io/en/stable/">Docs</a> •
   <a href="#Setup">Setup</a> •
   <a href="#examples">Examples</a> •
   <a href="#community">Community</a>
 </p>
 
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/finetuning-scheduler)](https://pypi.org/project/finetuning-scheduler/)
 [![PyPI Status](https://badge.fury.io/py/finetuning-scheduler.svg)](https://badge.fury.io/py/finetuning-scheduler)\
-[![codecov](https://codecov.io/gh/speediedan/finetuning-scheduler/release/2.0.1/graph/badge.svg?flag=gpu)](https://codecov.io/gh/speediedan/finetuning-scheduler)
+[![codecov](https://codecov.io/gh/speediedan/finetuning-scheduler/release/2.0.2/graph/badge.svg?flag=gpu)](https://codecov.io/gh/speediedan/finetuning-scheduler)
 [![ReadTheDocs](https://readthedocs.org/projects/finetuning-scheduler/badge/?version=latest)](https://finetuning-scheduler.readthedocs.io/en/stable/)
 [![DOI](https://zenodo.org/badge/455666112.svg)](https://zenodo.org/badge/latestdoi/455666112)
 [![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/speediedan/finetuning-scheduler/blob/master/LICENSE)
 
 </div>
 
 ______________________________________________________________________
 
-<img width="300px" src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.1/docs/source/_static/images/fts/fts_explicit_loss_anim.gif" alt="FinetuningScheduler explicit loss animation" align="right"/>
+<img width="300px" src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.2/docs/source/_static/images/fts/fts_explicit_loss_anim.gif" alt="FinetuningScheduler explicit loss animation" align="right"/>
 
 [FinetuningScheduler](https://finetuning-scheduler.readthedocs.io/en/stable/api/finetuning_scheduler.fts.html#finetuning_scheduler.fts.FinetuningScheduler) is simple to use yet powerful, offering a number of features that facilitate model research and exploration:
 
 - easy specification of flexible fine-tuning schedules with explicit or regex-based parameter selection
   - implicit schedules for initial/naive model exploration
   - explicit schedules for performance tuning, fine-grained behavioral experimentation and computational efficiency
 - automatic restoration of best per-phase checkpoints driven by iterative application of early-stopping criteria to each fine-tuning phase
@@ -117,32 +117,33 @@
 
 ### Scheduled Fine-Tuning For SuperGLUE
 
 - [Notebook-based Tutorial](https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/finetuning-scheduler.html)
 - [CLI-based Tutorial](https://finetuning-scheduler.readthedocs.io/en/stable/#example-scheduled-fine-tuning-for-superglue)
 - [FSDP Scheduled Fine-Tuning](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/fsdp_scheduled_fine_tuning.html)
 - [LR Scheduler Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/lr_scheduler_reinitialization.html) (advanced)
+- [Optimizer Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/optimizer_reinitialization.html) (advanced)
 
 ______________________________________________________________________
 
 ## Continuous Integration
 
 Fine-Tuning Scheduler is rigorously tested across multiple CPUs, GPUs and against major Python and PyTorch versions. Each Fine-Tuning Scheduler minor release (major.minor.patch) is paired with a Lightning minor release (e.g. Fine-Tuning Scheduler 2.0 depends upon Lightning 2.0).
 
 To ensure maximum stability, the latest Lightning patch release fully tested with Fine-Tuning Scheduler is set as a maximum dependency in Fine-Tuning Scheduler's requirements.txt (e.g. \<= 1.7.1). If you'd like to test a specific Lightning patch version greater than that currently in Fine-Tuning Scheduler's requirements.txt, it will likely work but you should install Fine-Tuning Scheduler from source and update the requirements.txt as desired.
 
 <details>
   <summary>Current build statuses for Fine-Tuning Scheduler </summary>
 
 | System / (PyTorch/Python ver) |                                                                                                         1.11/3.8                                                                                                         |                                                                                                              2.0.0/3.8, 2.0.0/3.10                                                                                                               |
 | :---------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
-|      Linux \[GPUs\*\*\]       |                                                                                                            -                                                                                                             | [![Build Status](https://dev.azure.com//speediedan/finetuning-scheduler/_apis/build/status/Multi-GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.1)](https://dev.azure.com/speediedan/finetuning-scheduler/_build/latest?definitionId=2&branchName=refs%2Ftags%2F2.0.1) |
-|     Linux (Ubuntu 20.04)      | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
-|           OSX (11)            | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
-|        Windows (2022)         | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
+|      Linux \[GPUs\*\*\]       |                                                                                                            -                                                                                                             | [![Build Status](https://dev.azure.com//speediedan/finetuning-scheduler/_apis/build/status/Multi-GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.2)](https://dev.azure.com/speediedan/finetuning-scheduler/_build/latest?definitionId=2&branchName=refs%2Ftags%2F2.0.2) |
+|     Linux (Ubuntu 20.04)      | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
+|           OSX (11)            | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
+|        Windows (2022)         | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
 
 - \*\* tests run on two RTX 2070s
 
 </details>
 
 ## Community
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: finetuning-scheduler Version: 2.0.1 Summary: A
+Metadata-Version: 2.1 Name: finetuning-scheduler Version: 2.0.2 Summary: A
 PyTorch Lightning extension that enhances model experimentation with flexible
 fine-tuning schedules. Home-page: https://github.com/speediedan/finetuning-
 scheduler Download-URL: https://github.com/speediedan/finetuning-scheduler
 Author: Dan Dale Author-email: danny.dale@gmail.com License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/speediedan/finetuning-scheduler/
 issues Project-URL: Documentation, https://finetuning-scheduler.readthedocs.io/
 en/latest/ Project-URL: Source Code, https://github.com/speediedan/finetuning-
@@ -16,24 +16,24 @@
 Apache Software License Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3 Classifier: Programming
 Language :: Python :: 3.8 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10 Requires-Python: >=3.8
 Description-Content-Type: text/markdown Provides-Extra: examples Provides-
 Extra: extra Provides-Extra: test Provides-Extra: ipynb Provides-Extra: cli
 Provides-Extra: dev Provides-Extra: all License-File: LICENSE
-  [https://github.com/speediedan/finetuning-scheduler/raw/v2.0.1/docs/source/
+  [https://github.com/speediedan/finetuning-scheduler/raw/v2.0.2/docs/source/
     _static/images/logos/logo_fts.png] **A PyTorch Lightning extension that
      enhances model experimentation with flexible fine-tuning schedules.**
     ______________________________________________________________________
                    Docs â¢ Setup â¢ Examples â¢ Community
  [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/finetuning-
   scheduler)](https://pypi.org/project/finetuning-scheduler/) [![PyPI Status]
 (https://badge.fury.io/py/finetuning-scheduler.svg)](https://badge.fury.io/py/
 finetuning-scheduler)\ [![codecov](https://codecov.io/gh/speediedan/finetuning-
-   scheduler/release/2.0.1/graph/badge.svg?flag=gpu)](https://codecov.io/gh/
+   scheduler/release/2.0.2/graph/badge.svg?flag=gpu)](https://codecov.io/gh/
    speediedan/finetuning-scheduler) [![ReadTheDocs](https://readthedocs.org/
    projects/finetuning-scheduler/badge/?version=latest)](https://finetuning-
     scheduler.readthedocs.io/en/stable/) [![DOI](https://zenodo.org/badge/
    455666112.svg)](https://zenodo.org/badge/latestdoi/455666112) [![license]
     (https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://
         github.com/speediedan/finetuning-scheduler/blob/master/LICENSE)
 ______________________________________________________________________
@@ -75,15 +75,17 @@
 Examples ### Scheduled Fine-Tuning For SuperGLUE - [Notebook-based Tutorial]
 (https://pytorch-lightning.readthedocs.io/en/stable/notebooks/
 lightning_examples/finetuning-scheduler.html) - [CLI-based Tutorial](https://
 finetuning-scheduler.readthedocs.io/en/stable/#example-scheduled-fine-tuning-
 for-superglue) - [FSDP Scheduled Fine-Tuning](https://finetuning-
 scheduler.readthedocs.io/en/stable/advanced/fsdp_scheduled_fine_tuning.html) -
 [LR Scheduler Reinitialization](https://finetuning-scheduler.readthedocs.io/en/
-stable/advanced/lr_scheduler_reinitialization.html) (advanced)
+stable/advanced/lr_scheduler_reinitialization.html) (advanced) - [Optimizer
+Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/
+advanced/optimizer_reinitialization.html) (advanced)
 ______________________________________________________________________ ##
 Continuous Integration Fine-Tuning Scheduler is rigorously tested across
 multiple CPUs, GPUs and against major Python and PyTorch versions. Each Fine-
 Tuning Scheduler minor release (major.minor.patch) is paired with a Lightning
 minor release (e.g. Fine-Tuning Scheduler 2.0 depends upon Lightning 2.0). To
 ensure maximum stability, the latest Lightning patch release fully tested with
 Fine-Tuning Scheduler is set as a maximum dependency in Fine-Tuning Scheduler's
@@ -97,33 +99,33 @@
 -------------------------------------------------------------------------------
 -----------------------------------------------: | :---------------------------
 -------------------------------------------------------------------------------
 -------------------------------------------------------------------------------
 -----------------------------------------------------: | | Linux \[GPUs\*\*\] |
 - | [![Build Status](https://dev.azure.com//speediedan/finetuning-scheduler/
 _apis/build/status/Multi-
-GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.1)](https://
+GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.2)](https://
 dev.azure.com/speediedan/finetuning-scheduler/_build/
-latest?definitionId=2&branchName=refs%2Ftags%2F2.0.1) | | Linux (Ubuntu 20.04)
+latest?definitionId=2&branchName=refs%2Ftags%2F2.0.2) | | Linux (Ubuntu 20.04)
 | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/
-workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/
+workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/
 finetuning-scheduler/actions/workflows/ci_test-full.yml) | [![Test](https://
 github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/
-badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/
+badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/
 actions/workflows/ci_test-full.yml) | | OSX (11) | [![Test](https://github.com/
 speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/
-badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/
+badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/
 actions/workflows/ci_test-full.yml) | [![Test](https://github.com/speediedan/
-finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)]
+finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)]
 (https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-
 full.yml) | | Windows (2022) | [![Test](https://github.com/speediedan/
-finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)]
+finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)]
 (https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-
 full.yml) | [![Test](https://github.com/speediedan/finetuning-scheduler/
-actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/
+actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/
 speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) | - \*\*
 tests run on two RTX 2070s  ## Community Fine-Tuning Scheduler is developed and
 maintained by the community in close communication with the [Lightning team]
 (https://pytorch-lightning.readthedocs.io/en/stable/governance.html). Thanks to
 everyone in the community for their tireless effort building and improving the
 immensely useful core Lightning project. PR's welcome! Please see the
 [contributing guidelines](https://finetuning-scheduler.readthedocs.io/en/
```

### Comparing `finetuning-scheduler-2.0.1/README.md` & `finetuning-scheduler-2.0.2/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -126,14 +126,15 @@
 
 ### Scheduled Fine-Tuning For SuperGLUE
 
 - [Notebook-based Tutorial](https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/finetuning-scheduler.html)
 - [CLI-based Tutorial](https://finetuning-scheduler.readthedocs.io/en/stable/#example-scheduled-fine-tuning-for-superglue)
 - [FSDP Scheduled Fine-Tuning](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/fsdp_scheduled_fine_tuning.html)
 - [LR Scheduler Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/lr_scheduler_reinitialization.html) (advanced)
+- [Optimizer Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/optimizer_reinitialization.html) (advanced)
 
 ______________________________________________________________________
 
 ## Continuous Integration
 
 Fine-Tuning Scheduler is rigorously tested across multiple CPUs, GPUs and against major Python and PyTorch versions. Each Fine-Tuning Scheduler minor release (major.minor.patch) is paired with a Lightning minor release (e.g. Fine-Tuning Scheduler 2.0 depends upon Lightning 2.0).
```

#### html2text {}

```diff
@@ -67,15 +67,17 @@
 Examples ### Scheduled Fine-Tuning For SuperGLUE - [Notebook-based Tutorial]
 (https://pytorch-lightning.readthedocs.io/en/stable/notebooks/
 lightning_examples/finetuning-scheduler.html) - [CLI-based Tutorial](https://
 finetuning-scheduler.readthedocs.io/en/stable/#example-scheduled-fine-tuning-
 for-superglue) - [FSDP Scheduled Fine-Tuning](https://finetuning-
 scheduler.readthedocs.io/en/stable/advanced/fsdp_scheduled_fine_tuning.html) -
 [LR Scheduler Reinitialization](https://finetuning-scheduler.readthedocs.io/en/
-stable/advanced/lr_scheduler_reinitialization.html) (advanced)
+stable/advanced/lr_scheduler_reinitialization.html) (advanced) - [Optimizer
+Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/
+advanced/optimizer_reinitialization.html) (advanced)
 ______________________________________________________________________ ##
 Continuous Integration Fine-Tuning Scheduler is rigorously tested across
 multiple CPUs, GPUs and against major Python and PyTorch versions. Each Fine-
 Tuning Scheduler minor release (major.minor.patch) is paired with a Lightning
 minor release (e.g. Fine-Tuning Scheduler 2.0 depends upon Lightning 2.0). To
 ensure maximum stability, the latest Lightning patch release fully tested with
 Fine-Tuning Scheduler is set as a maximum dependency in Fine-Tuning Scheduler's
```

### Comparing `finetuning-scheduler-2.0.1/pyproject.toml` & `finetuning-scheduler-2.0.2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -69,14 +69,15 @@
 # TODO: the goal is for this to be empty
 #[[tool.mypy.overrides]]
 # the list can be generated with:
 # mypy | tr ':' ' ' |  awk '{print $1}' | sort | uniq | sed 's/\.py//g' | sed 's|\/|\.|g' | xargs -I {} echo '"{}",'
 # module = []
 # ignore_errors = "True"
 
+
 [tool.coverage.report]
 exclude_lines = [
     "pragma: no cover",
     "warnings",
     "pass",
     "rank_zero_warn",
     "raise NotImplementedError",
```

### Comparing `finetuning-scheduler-2.0.1/setup.py` & `finetuning-scheduler-2.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -81,14 +81,15 @@
         license=about.__license__,
         packages=setuptools.find_namespace_packages(where="src"),
         package_dir={"": "src"},
         package_data={
             "fts_examples.stable.config": ["*.yaml"],
             "fts_examples.stable.config.advanced.fsdp": ["*.yaml"],
             "fts_examples.stable.config.advanced.reinit_lr": ["*.yaml"],
+            "fts_examples.stable.config.advanced.reinit_optim_lr": ["*.yaml"],
             "fts_examples.legacy.config": ["*.yaml"],
             "fts_examples.legacy.config.advanced.fsdp": ["*.yaml"],
             "fts_examples.legacy.config.advanced.reinit_lr": ["*.yaml"],
         },
         include_package_data=True,
         long_description=long_description,
         long_description_content_type="text/markdown",
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/__about__.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/__about__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import time
 
 _this_year = time.strftime("%Y")
-__version__ = "2.0.1"
+__version__ = "2.0.2"
 __author__ = "Dan Dale"
 __author_email__ = "danny.dale@gmail.com"
 __license__ = "Apache-2.0"
 __copyright__ = f"Copyright (c) 2021-{_this_year}, {__author__}"
 __homepage__ = "https://github.com/speediedan/finetuning-scheduler"
 __docs_url__ = "https://finetuning-scheduler.readthedocs.io/en/latest/"
 # this has to be simple string, see: https://github.com/pypa/twine/issues/522
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/fts.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/fts.py`

 * *Files 4% similar despite different names*

```diff
@@ -15,36 +15,36 @@
 
 Used to implement flexible fine-tuning training schedules
 
 """
 import logging
 from copy import deepcopy
 from pprint import pformat
-from typing import Any, Dict, Optional, Sequence, Union
+from typing import Any, Dict, Optional, Sequence, Tuple, Union
 
 import lightning.pytorch as pl
 import torch
 from lightning.fabric.utilities import rank_zero_info
 from lightning.fabric.utilities.distributed import ReduceOp
 from lightning.pytorch.callbacks import BaseFinetuning
 from lightning.pytorch.strategies.strategy import Strategy
 from lightning.pytorch.trainer.states import TrainerFn
 from lightning.pytorch.utilities.exceptions import MisconfigurationException
 from lightning.pytorch.utilities.rank_zero import rank_zero_debug, rank_zero_warn
-from torch.optim.optimizer import Optimizer
 
 from finetuning_scheduler.fts_supporters import (
     CallbackDepMixin,
     FTSEarlyStopping,
     FTSState,
     ScheduleImplMixin,
     ScheduleParsingMixin,
     STRATEGY_ADAPTERS,
 )
 from finetuning_scheduler.strategy_adapters.base import StrategyAdapter
+from finetuning_scheduler.types import ParamGroupAddable
 
 log = logging.getLogger(__name__)
 
 
 class FinetuningScheduler(ScheduleImplMixin, ScheduleParsingMixin, CallbackDepMixin, BaseFinetuning):
     r"""
     This callback enables flexible, multi-phase, scheduled fine-tuning of foundation models. Gradual
@@ -95,14 +95,15 @@
         self,
         ft_schedule: Optional[Union[str, dict]] = None,
         max_depth: int = -1,
         base_max_lr: float = 1e-5,
         restore_best: bool = True,
         gen_ft_sched_only: bool = False,
         epoch_transitions_only: bool = False,
+        reinit_optim_cfg: Optional[Dict] = None,
         reinit_lr_cfg: Optional[Dict] = None,
         strategy_adapter_cfg: Optional[Dict] = None,
         custom_strategy_adapter: Optional[Dict[str, str]] = None,
         allow_untested: bool = False,
         apply_lambdas_new_pgs: bool = False,
         logging_level: int = logging.INFO,
         enforce_phase0_params: bool = True,
@@ -136,34 +137,53 @@
             epoch_transitions_only: If ``True``, use epoch-driven stopping criteria exclusively (rather than composing
                 :class:`~finetuning_scheduler.fts_supporters.FTSEarlyStopping` and
                 epoch-driven criteria which is the default). If using this mode, an epoch-driven transition
                 (``max_transition_epoch`` >= 0) must be specified for each phase. If unspecified,
                 ``max_transition_epoch`` defaults to -1 for each phase which signals the application of
                 :class:`~finetuning_scheduler.fts_supporters.FTSEarlyStopping` criteria only.
                 epoch_transitions_only defaults to ``False``.
+            reinit_optim_cfg: An optimizer reinitialization configuration dictionary consisting of at minimum a nested
+                ``optimizer_init`` dictionary with a ``class_path`` key specifying the class of the optimizer to be
+                instantiated. Optionally, an ``init_args`` dictionary of arguments with which to initialize the
+                optimizer may be included. A ``reinit_lr_cfg`` configuration can also be specified concurrently. By way
+                of example, one could configure this dictionary via the
+                :external+pl:class:`~lightning.pytorch.cli.LightningCLI` with the following:
+
+                .. code-block:: yaml
+
+                    reinit_optim_cfg:
+                        optimizer_init:
+                            class_path: torch.optim.SGD
+                            init_args:
+                                lr: 1.0e-05
+                                momentum: 0.9
+                                weight_decay: 1.0e-06
+
             reinit_lr_cfg: A lr scheduler reinitialization configuration dictionary consisting of at minimum a nested
                 ``lr_scheduler_init`` dictionary with a ``class_path`` key specifying the class of the lr scheduler
                 to be instantiated. Optionally, an ``init_args`` dictionary of arguments to initialize the lr scheduler
                 with may be included. Additionally, one may optionally include arguments to pass to PyTorch Lightning's
                 lr scheduler configuration :class:`~lightning.pytorch.utilities.types.LRSchedulerConfig` in the
-                ``pl_lrs_cfg`` dictionary. By way of example, one could configure this dictionary via the
+                ``pl_lrs_cfg`` dictionary. A ``reinit_optim_cfg`` configuration can also be specified concurrently. By
+                way of example, one could configure this dictionary via the
                 :external+pl:class:`~lightning.pytorch.cli.LightningCLI` with the following:
 
                 .. code-block:: yaml
 
                     reinit_lr_cfg:
                         lr_scheduler_init:
                             class_path: torch.optim.lr_scheduler.StepLR
                             init_args:
                                 step_size: 1
                                 gamma: 0.7
                             pl_lrs_cfg:
                                 interval: epoch
                                 frequency: 1
                                 name: Implicit_Reinit_LR_Scheduler
+                            use_current_optimizer_pg_lrs: true
 
             allow_untested: If ``True``, allows the use of custom or unsupported training strategies and lr schedulers
                 (e.g. ``single_tpu``, ``MyCustomStrategy``, ``MyCustomLRScheduler``) . Defaults to ``False``.
 
                 .. note:: Custom or officially unsupported strategies and lr schedulers can be used by setting
                     :paramref:`~finetuning_scheduler.fts.FinetuningScheduler.allow_untested` to ``True``.
 
@@ -224,20 +244,22 @@
         self._fts_state = FTSState()
         self.max_depth = max_depth
         self.restore_best = restore_best
         self.ft_schedule = ft_schedule
         self.base_max_lr = base_max_lr
         self.gen_ft_sched_only = gen_ft_sched_only
         self.epoch_transitions_only = epoch_transitions_only
+        self.reinit_optim_cfg = reinit_optim_cfg
         self.reinit_lr_cfg = reinit_lr_cfg
         self.strategy_adapter_cfg = strategy_adapter_cfg or {}
         self.custom_strategy_adapter = custom_strategy_adapter
         self.allow_untested = allow_untested
         self.apply_lambdas_new_pgs = apply_lambdas_new_pgs
         self.enforce_phase0_params = enforce_phase0_params
+        self._has_reinit_schedule = False
         rz_logger = logging.getLogger("lightning.pytorch.utilities.rank_zero")
         rz_logger.setLevel(logging_level)
 
     @property
     def curr_depth(self) -> int:
         """Index of the fine-tuning schedule depth currently being trained.
 
@@ -288,20 +310,30 @@
 
         .. note::
 
             The :class:`~finetuning_scheduler.fts.FinetuningScheduler` callback initially
             only supports single-schedule/optimizer fine-tuning configurations
         """
         assert self.pl_module.trainer is not None
+        pre_reinit_state = self._save_pre_reinit_lr_state(self.pl_module.trainer)
         if not self._fts_state._resume_fit_from_ckpt:
             if self.restore_best:
                 self.restore_best_ckpt()
-                self.step_pg(depth=self.curr_depth, optimizer=self.pl_module.trainer.optimizers[0])
+                self.step_pg(
+                    depth=self.curr_depth,
+                    optimizer=self.pl_module.trainer.optimizers[0],
+                    pre_reinit_state=pre_reinit_state,
+                )
             else:
-                self.step_pg(depth=self.curr_depth, optimizer=self.pl_module.trainer.optimizers[0], depth_sync=False)
+                self.step_pg(
+                    depth=self.curr_depth,
+                    optimizer=self.pl_module.trainer.optimizers[0],
+                    depth_sync=False,
+                    pre_reinit_state=pre_reinit_state,
+                )
         else:
             self.thaw_to_depth()
         if self.depth_remaining == 0 and not self.epoch_transitions_only:
             assert self.pl_module.trainer.early_stopping_callback is not None
             self.pl_module.trainer.early_stopping_callback.final_phase = True  # type: ignore[attr-defined]
         assert self._fts_state._ft_sync_objects is not None
         if self._fts_state._resume_fit_from_ckpt:
@@ -316,95 +348,137 @@
             max_epochs_msg = f"`max_epochs` ({self.pl_module.trainer.fit_loop.max_epochs}) is reached."
             composition_msg = "the early stopping conditions are met or " + max_epochs_msg
             rank_zero_info(
                 f"Given the current configuration of `max_depth` ({self.max_depth}), this training session"
                 f" will now end when {max_epochs_msg if self.epoch_transitions_only else composition_msg}"
             )
 
-    def step_pg(self, optimizer: Optimizer, depth: int, depth_sync: bool = True) -> None:
+    def step_pg(
+        self,
+        optimizer: ParamGroupAddable,
+        depth: int,
+        depth_sync: bool = True,
+        pre_reinit_state: Optional[Tuple] = None,
+    ) -> None:
         """Configure optimizer parameter groups for the next scheduled fine-tuning level, adding parameter groups
         beyond the restored optimizer state up to
-        :paramref:`~finetuning_scheduler.fts.FinetuningScheduler.current_depth`
+        :paramref:`~finetuning_scheduler.fts.FinetuningScheduler.current_depth` and reinitializing the optimizer and/or
+        learning rate scheduler as configured.
 
         Args:
-            optimizer (:external+torch:class:`~torch.optim.Optimizer`): The
-                :external+torch:class:`~torch.optim.Optimizer` to which parameter groups will be configured and added.
+            optimizer (:class:`~finetuning_scheduler.types.ParamGroupAddable`): The supported optimizer instance to
+                which parameter groups will be configured and added.
             depth: The maximum index of the fine-tuning schedule for which to configure the optimizer parameter
                 groups.
             depth_sync: If ``True``, configure optimizer parameter groups for all depth indices greater
                 than the restored checkpoint. If ``False``, configure groups only for the specified depth. Defaults to
                 ``True``.
         """
         next_tl: Dict = {}
         assert isinstance(self.ft_schedule, dict)
         assert isinstance(self.pl_module, pl.LightningModule)
         assert isinstance(self.pl_module.trainer, pl.Trainer)
-        if depth_sync:
-            thaw_layers = {d: tl for d, tl in self.ft_schedule.items() if d > self._fts_state._best_ckpt_depth}.items()
+        # if the target depth is 0, implicit optimizer reinitialization should not be executed
+        new_optimizer_cfg = (
+            (self.reinit_optim_cfg or self.ft_schedule[depth].get("new_optimizer", None)) if depth > 0 else None
+        )
+        restored_depth = -1 if new_optimizer_cfg else self._fts_state._best_ckpt_depth
+        if depth_sync or new_optimizer_cfg:
+            thaw_layers = {d: tl for d, tl in self.ft_schedule.items() if d > restored_depth}.items()
         else:
             thaw_layers = {depth: self.ft_schedule[depth]}.items()
         for i, orig_next_tl in thaw_layers:
             next_tl = deepcopy(orig_next_tl)
             if i <= depth:
                 next_tl["params"] = self.strategy_adapter.fts_optim_transform(next_tl["params"])
                 _, self._fts_state._curr_thawed_params = self.strategy_adapter.exec_ft_phase(
                     self.pl_module, thaw_pl=next_tl["params"]
                 )
-                FinetuningScheduler.add_optimizer_groups(
-                    module=self.pl_module,
-                    optimizer=optimizer,
-                    thawed_pl=next_tl["params"],
-                    lr=next_tl.get("lr", optimizer.defaults["lr"]),
-                    no_decay=getattr(self.pl_module, "no_decay", None),
-                    apply_lambdas=self.apply_lambdas_new_pgs,
-                )
-                new_scheduler_cfg = self.reinit_lr_cfg or next_tl.get("new_lr_scheduler", None)
-                if new_scheduler_cfg:
-                    self.reinit_lr_scheduler(
-                        new_lr_scheduler=new_scheduler_cfg, trainer=self.pl_module.trainer, optimizer=optimizer
+                if new_optimizer_cfg and i == 0:
+                    # If reinitializing the optimizer, we need to re-add the initial parameter groups (phase 0)
+                    optimizer = self.reinit_optimizer(
+                        new_optimizer=new_optimizer_cfg, trainer=self.pl_module.trainer, init_params=next_tl["params"]
                     )
                 else:
-                    if self.pl_module.trainer.lr_scheduler_configs:
-                        for config in self.pl_module.trainer.lr_scheduler_configs:
-                            show_warn_lambdas = (
-                                hasattr(config.scheduler, "lr_lambdas")
-                                and config.scheduler.lr_lambdas[-1] is not None  # type: ignore[union-attr]
-                                and not self.apply_lambdas_new_pgs
-                            )
-                            if show_warn_lambdas:
-                                rank_zero_warn(
-                                    "The lr scheduler used in this phase has lr_lambdas but will use a "
-                                    "configured lr for new parameter groups because `apply_lambdas_new_pgs` is "
-                                    "set to the default of `False`. If you would like new groups to have lr "
-                                    "lambdas applied, set `apply_lambdas_new_pgs` to `True`."
-                                )
+                    # Add pgs and configure the learning rate scheduler using the current optimizer/schedule
+                    self._add_pgs_config_lrs(optimizer, next_tl, depth, depth == i, pre_reinit_state)
+
+    def _add_pgs_config_lrs(
+        self,
+        optimizer: ParamGroupAddable,
+        next_tl: Dict,
+        depth: int,
+        is_target_depth: bool,
+        pre_reinit_state: Optional[Tuple],
+    ) -> None:
+        """Add optimizer parameter groups and potentially reinitialize/reconfigure the learning rate scheduler
+        according to a given schedule phase configuration.
+
+        Args:
+            optimizer (:class:`~finetuning_scheduler.types.ParamGroupAddable`): The supported optimizer instance to
+                which parameter groups will be configured and added.
+            next_tl (Dict): A dictionary containing the schedule configuration associated with the current phase
+                context.
+            depth (int): The current target depth.
+            is_target_depth (bool): Whether this restoration stage is the current target depth.
+            pre_reinit_state (Tuple): Contingent on restoration context, lr scheduler and optimizer lr state to restore.
+        """
+        # if the target depth is 0, lr scheduler reinitialization should not be executed
+        new_scheduler_cfg = (self.reinit_lr_cfg or next_tl.get("new_lr_scheduler", None)) if depth > 0 else None
+        if is_target_depth and depth > 0:
+            # NB: The latest optimizer and lr scheduler lr state will be re-applied to all existing param groups before
+            # implementing the next phase.
+            assert pre_reinit_state
+            self._restore_latest_lr_state(*pre_reinit_state)
+        FinetuningScheduler.add_optimizer_groups(
+            module=self.pl_module,
+            optimizer=optimizer,
+            thawed_pl=next_tl["params"],
+            lr=next_tl.get("lr", optimizer.defaults["lr"]),
+            no_decay=getattr(self.pl_module, "no_decay", None),
+            apply_lambdas=self.apply_lambdas_new_pgs,
+        )
+        if new_scheduler_cfg:
+            self.reinit_lr_scheduler(
+                new_lr_scheduler=new_scheduler_cfg, trainer=self.pl_module.trainer, optimizer=optimizer
+            )
+        else:
+            self._maybe_warn_lr_lambdas()
+
+    def _maybe_warn_lr_lambdas(self) -> None:
+        """If appropriate, warn the user that `lr_lambdas` will not be applied given the current configuration."""
+        if self.pl_module.trainer.lr_scheduler_configs:
+            for config in self.pl_module.trainer.lr_scheduler_configs:
+                show_warn_lambdas = (
+                    hasattr(config.scheduler, "lr_lambdas")
+                    and config.scheduler.lr_lambdas[-1] is not None  # type: ignore[union-attr]
+                    and not self.apply_lambdas_new_pgs
+                )
+                if show_warn_lambdas:
+                    rank_zero_warn(
+                        "The lr scheduler used in this phase has lr_lambdas but will use a "
+                        "configured lr for new parameter groups because `apply_lambdas_new_pgs` is "
+                        "set to the default of `False`. If you would like new groups to have lr "
+                        "lambdas applied, set `apply_lambdas_new_pgs` to `True`."
+                    )
 
     def restore_best_ckpt(self) -> None:
         """Restore the current best model checkpoint, according to
         :paramref:`~finetuning_scheduler.fts_supporters.FTSCheckpoint.best_model_path`"""
         assert self.pl_module.trainer is not None
         # wait for all processes to be ready to restore ckpt before restoring
         self.pl_module.trainer.strategy.barrier("setup_next_level")
         # if restarting across multiple depths, need to ensure we're restoring optimizer state appropriately
         # by resetting optimizer groups and allowing state dict to be reset commensurate w/ ckpt state
         for opt_idx, optimizer in enumerate(self.pl_module.trainer.optimizers):
             optimizer.param_groups = BaseFinetuning._apply_mapping_to_param_groups(
                 self._fts_state._fts_ckpt_metadata["best_ckpt_pgs"][opt_idx], dict(self.pl_module.named_parameters())
             )
-            if hasattr(optimizer, "consolidate_state_dict"):
-                # for optimizers that shard their states like (e.g. ZeroRedundancyOptimizer, OSS), we need to clear
-                # local optimizer partition caches and repartition to support restoring across multiple depths
-                partition_params = (
-                    optimizer._partition_parameters
-                    if callable(optimizer._partition_parameters)
-                    else optimizer.partition_parameters
-                )
-                optimizer._clear_cache()
-                optimizer.optim.param_groups = partition_params()[optimizer.rank]
-                optimizer._sync_param_groups(optimizer.optim.param_groups, optimizer.param_groups)
+            if self.strategy_adapter.using_sharded_optimizer:
+                ScheduleImplMixin._repartition_sharded_optim(optimizer)
         # we're restoring everything but callbacks and loops, otherwise, checkpoint_connector.restore() could be used
         assert self.pl_module.trainer.checkpoint_callback is not None
         checkpoint_path = self.pl_module.trainer.checkpoint_callback.best_model_path  # type: ignore[attr-defined]
         self.pl_module.trainer._checkpoint_connector.resume_start(checkpoint_path=checkpoint_path)
         self.pl_module.trainer._checkpoint_connector.restore_datamodule()
         self.pl_module.trainer._checkpoint_connector.restore_model()
         # we need to override checkpoint_connector.restore_training_state() to bypass loop restoration
@@ -431,18 +505,22 @@
             try:
                 # enable strategy adapters to restore optimizer if `Strategy.lightning_restore_optimizer` is overridden
                 self.strategy_adapter.on_before_restore_optimizers_and_lrs()
                 # restore optimizers and schedulers state
                 checkpoint_connector.restore_optimizers_and_schedulers()
             except KeyError:
                 assert isinstance(self.ft_schedule, dict)
-                if self.ft_schedule[self.curr_depth].get("new_lr_scheduler", None):
+                if self._has_reinit_schedule:
                     rank_zero_warn(
-                        "incompatible checkpoint detected but attempting to proceed with next phase of training since "
-                        "we're reinitializing the lr scheduler."
+                        "Incompatible checkpoint detected when attempting to restore the optimizer and/or lr "
+                        "scheduler from a previous phase. Attempting to proceed with next phase of training since this "
+                        "schedule reinitializes the optimizer and/or lr scheduler.\n"
+                        "HINT: If subsequent errors are encountered, you can either set ``restore_best`` to ``False`` "
+                        "or alter your reinitialization schedule for the relevant training components (i.e. optimizer, "
+                        "lr scheduler)."
                     )
 
     def _reduce_transition(self, strategy: Strategy, decision: bool) -> bool:
         """Reduce a transition decision across all world processes (effectively a global `any` collective)
 
         Args:
             strategy (Strategy): The PL :external+pl:class:`~lightning.pytorch.strategies.Strategy` context to use.
@@ -715,26 +793,28 @@
         for opt_idx, optimizer in enumerate(trainer.optimizers):
             num_saved_groups = (
                 len(self._internal_optimizer_metadata[opt_idx]) if opt_idx in self._internal_optimizer_metadata else 0
             )
             current_param_groups = optimizer.param_groups
             self._store(pl_module, opt_idx, num_saved_groups, current_param_groups)
 
-    def on_before_zero_grad(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule", optimizer: Optimizer) -> None:
+    def on_before_zero_grad(
+        self, trainer: "pl.Trainer", pl_module: "pl.LightningModule", optimizer: ParamGroupAddable
+    ) -> None:
         """Afer the latest optimizer step, update the
         :attr:`~finetuning_scheduler.fts.FinetuningScheduler._fts_state`, incrementing the
         global fine-tuning steps taken
 
         Args:
             trainer (:external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer`): The
                 :external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer` object
             pl_module  (:external+pl:class:`~lightning.pytorch.core.module.LightningModule`): The
                 :external+pl:class:`~lightning.pytorch.core.module.LightningModule` object
-            optimizer (:external+torch:class:`~torch.optim.Optimizer`): The
-                :external+torch:class:`~torch.optim.Optimizer` to which parameter groups will be configured and added.
+            optimizer (:class:`~finetuning_scheduler.types.ParamGroupAddable`): The supported optimizer instance to
+                which parameter groups will be configured and added.
         """
         self._fts_state._ft_global_steps += 1
 
     def on_train_end(self, trainer: "pl.Trainer", pl_module: "pl.LightningModule") -> None:
         """Synchronize internal :attr:`~finetuning_scheduler.fts.FinetuningScheduler._fts_state` on end of training
         to ensure final training state is consistent with epoch semantics.
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/fts_supporters.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/fts_supporters.py`

 * *Files 11% similar despite different names*

```diff
@@ -21,42 +21,42 @@
 import os
 import pathlib
 import re
 import warnings
 from abc import ABC, abstractmethod
 from collections import Counter, defaultdict
 from collections.abc import KeysView
-from copy import copy
+from copy import copy, deepcopy
 from dataclasses import dataclass, field, fields
 from functools import reduce
 from pprint import pformat
 from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
 
 import lightning.pytorch as pl
 import torch
 import yaml
 from lightning.fabric.utilities import rank_zero_info, rank_zero_only, rank_zero_warn
 from lightning.fabric.utilities.cloud_io import get_filesystem
 from lightning.fabric.utilities.distributed import _distributed_available
-from lightning.fabric.utilities.types import _TORCH_LRSCHEDULER, ReduceLROnPlateau
 from lightning.pytorch.callbacks import Callback
 from lightning.pytorch.callbacks.early_stopping import EarlyStopping
 from lightning.pytorch.callbacks.lr_monitor import LearningRateMonitor
 from lightning.pytorch.callbacks.model_checkpoint import ModelCheckpoint
 from lightning.pytorch.core.optimizer import _MockOptimizer
 from lightning.pytorch.trainer.states import TrainerFn
 from lightning.pytorch.utilities import find_shared_parameters
 from lightning.pytorch.utilities.exceptions import MisconfigurationException
 from lightning.pytorch.utilities.rank_zero import rank_zero_debug
 from lightning.pytorch.utilities.types import LRSchedulerConfig
 from torch import Tensor
+from torch.distributed.optim import ZeroRedundancyOptimizer
 from torch.nn import Module
-from torch.optim.optimizer import Optimizer
 
 from finetuning_scheduler.strategy_adapters.fsdp import FSDPStrategyAdapter, StrategyAdapter
+from finetuning_scheduler.types import FTSLRSchedulerType, FTSLRSchedulerTypeTuple, ParamGroupAddable
 
 log = logging.getLogger(__name__)
 
 CALLBACK_DEP_PARENTS = {"ModelCheckpoint": ModelCheckpoint, "EarlyStopping": EarlyStopping}
 CALLBACK_ATTRS = ("ft_schedule", "max_depth")
 TARGET_CALLBACK_REF = "FinetuningScheduler"
 STRATEGY_ADAPTERS = {"fsdp": FSDPStrategyAdapter}
@@ -85,31 +85,14 @@
         self._fts_ckpt_metadata = {
             "current_ckpt_depth": self._curr_depth,
             "best_ckpt_depth": self._best_ckpt_depth,
             "best_ckpt_pgs": {},
         }
 
 
-# todo: improve FTSLRSchedulerType naming/typing once corresponding changes made upstream in pytorch-lightning
-supported_lrs = [
-    "LambdaLR",
-    "MultiplicativeLR",
-    "StepLR",
-    "MultiStepLR",
-    "ExponentialLR",
-    "CosineAnnealingLR",
-    "ReduceLROnPlateau",
-    "CosineAnnealingWarmRestarts",
-    "ConstantLR",
-    "LinearLR",
-]
-FTSLRSchedulerTypeTuple = tuple(getattr(torch.optim.lr_scheduler, lr_class) for lr_class in supported_lrs)
-FTSLRSchedulerType = Union[Type[_TORCH_LRSCHEDULER], Type[ReduceLROnPlateau]]
-
-
 class CallbackResolverMixin(ABC):
     """Give user-provided callbacks with the ability to connect to another user-provided callback.
 
     This resolution logic is provided in order to avoid callback-dependent trainer attributes (e.g.
     trainer.finetuningscheduler_callback)
     """
 
@@ -506,31 +489,35 @@
                 raise ValueError(key)
         return super().construct_mapping(node, deep)
 
 
 class ScheduleParsingMixin(ABC):
     """Functionality for parsing and validating fine-tuning schedules."""
 
+    SANITY_CHK_ITERABLE = (torch.nn.Parameter(torch.empty(1)),)
+    VALID_REINIT_ATTR = ("reinit_lr_cfg", "reinit_optim_cfg")
+    VALID_REINIT_KEYS = ("new_lr_scheduler", "new_optimizer")
     # proper initialization of these variables should be done in the child class
     pl_module: pl.LightningModule
     ft_schedule: Optional[Union[str, dict]]
+    reinit_optim_cfg: Optional[Dict]
     reinit_lr_cfg: Optional[Dict]
 
     def _validate_ft_sched(self) -> Tuple[int, int]:
         """Ensure the explicitly specified fine-tuning schedule has a valid configuration.
 
         Returns:
             Tuple[int, int]: A tuple of ints specifying:
                 1. The depth of the final scheduled phase
                 2. The maximum epoch watermark explicitly specified in the schedule
         """
         max_epoch_wm = -1
         max_phase = 0
         self._validate_schedule_keys()
-        self._validate_lr_scheduler_cfg()
+        self._validate_reinit_cfg()
         named_params = dict(self.pl_module.named_parameters()).keys()
         model_shared_params = find_shared_parameters(self.pl_module)
         msp_ref = tuple((model_shared_params, set(itertools.chain(*model_shared_params))))
         for depth in self.ft_schedule.keys():  # type: ignore[union-attr]
             max_phase = max(max_phase, depth)
             self._parse_phase(depth, named_params, msp_ref)
             if depth > 0:
@@ -595,105 +582,149 @@
         if self.pl_module.automatic_optimization:
             if "interval" in pl_lrs_cfg and pl_lrs_cfg["interval"] not in ("step", "epoch"):
                 raise MisconfigurationException(
                     'The "interval" key in lr scheduler dict must be "step" or "epoch"'
                     f' but is "{pl_lrs_cfg["interval"]}"'
                 )
 
+    def _common_reinit_key_validation(self, target_sched: Dict, target_key: str, depth: Optional[int] = None) -> None:
+        """Key validation common to all reinitialzation configuration dictionaries.
+
+        Args:
+            target_sched (Dict): The provided reinitialization configuration for either an implicit mode fine-tuning
+                schedule or for a given explicity mode fine-tuning phase.
+            target_key (str): The expected reinitialization key for the current parsing context.
+            depth (Optional[int], optional): If parsing an explicit schedule, the current phase. Defaults to None.
+
+        Raises:
+            MisconfigurationException: If a valid reinitialization key is missing in the reinitialization configuration.
+            MisconfigurationException: If the configuration provided in valid reinitialization key but did not specify
+                a `class_path` for the class to be instantiated.
+        """
+        if target_key not in target_sched.keys():
+            phase_specific_msg = "" if not depth else f"for phase {depth}"
+            key_specific_msg = "a lr scheduler" if target_key == "lr_scheduler_init" else "an optimizer"
+            raise MisconfigurationException(
+                f"Specifying {key_specific_msg} configuration to reinitialize with requires a valid configuration "
+                f"dictionary be provided via a `{target_key}` key but no such key was found " + phase_specific_msg + "."
+            )
+        if not target_sched[target_key].get("class_path"):
+            phase_specific_msg = "the specified config." if not depth else f"the specified phase ({depth})."
+            raise MisconfigurationException(
+                f"Specifying `{target_key}` requires at least a  `class_path` to be specified but this is not the case "
+                "for " + phase_specific_msg
+            )
+
+    def _optimizer_reinit_key_validation(self, target_sched: Dict, depth: Optional[int] = None) -> None:
+        """Validate the keys in a given lr scheduler reinitialization configuration.
+
+        Args:
+            target_sched (Dict): The provided optimizer reinitialization configuration for either an implicit mode
+                fine-tuning schedule (passed via `reinit_optim_cfg`) or for a given explicity mode fine-tuning phase
+                (passed via `new_optimizer` for a given phase)
+            depth (Optional[int], optional): If parsing an explicit schedule, the current phase. Defaults to None.
+        """
+        self._common_reinit_key_validation(target_sched, "optimizer_init", depth)
+        optimizer_init = target_sched.get("optimizer_init")
+        assert optimizer_init
+        self._optimizer_sanity_chk(optimizer_init)
+
     def _lr_scheduler_reinit_key_validation(self, target_sched: Dict, depth: Optional[int] = None) -> None:
-        """Validate the keys in a given lr reinitialization configuration.
+        """Validate the keys in a given lr scheduler reinitialization configuration.
 
         Args:
             target_sched (Dict): The provided lr scheduler reinitialization configuration for either an implicit mode
                 fine-tuning schedule (passed via `reinit_lr_cfg`) or for a given explicity mode fine-tuning phase
                 (passed via `new_lr_scheduler` for a given phase)
             depth (Optional[int], optional): If parsing an explicit schedule, the current phase. Defaults to None.
 
         Raises:
             MisconfigurationException: If an `init_pg_lrs` key is provided in implicit mode training
                 (via `reinit_lr_cfg`).
-            MisconfigurationException: If an `lr_scheduler_init` key is missing in the lr scheduler reinitialization
-                configuration.
-            MisconfigurationException: If the configuration provided in `lr_scheduler_init` does not specify a
-                `class_path` for the lr scheduler to be instantiated.
         """
+        self._common_reinit_key_validation(target_sched, "lr_scheduler_init", depth)
         implicit_chk = bool(self.reinit_lr_cfg)
         if "init_pg_lrs" in target_sched.keys() and implicit_chk:
             raise MisconfigurationException(
                 "Specifying a `init_pg_lrs` key in the lr scheduler configuration passed via `reinit_lr_cfg` (i.e. "
                 "implicit mode training) is not a valid configuration since the same lr scheduler configuration "
                 "is intended to be reinitialized at every fine-tuning phase with implicit mode fine-tuning."
             )
-        # validate lr_scheduler_init config
-        if "lr_scheduler_init" not in target_sched.keys():
-            phase_specific_msg = "" if not depth else f"for phase {depth}"
-            raise MisconfigurationException(
-                "Specifying a lr scheduler configuration to reinitialize with requires a valid lr scheduler "
-                "configuration dictionary be provided via a `lr_scheduler_init` key but no such key was found "
-                + phase_specific_msg
-                + "."
-            )
         # if we're passing pl lr scheduler configuration, validate the keys
         if "pl_lrs_cfg" in target_sched.keys():
             self._pl_lrs_validation(pl_lrs_cfg=target_sched["pl_lrs_cfg"])
-        if not target_sched["lr_scheduler_init"].get("class_path"):
-            phase_specific_msg = "the specified lr schedule config." if not depth else f"the specified phase ({depth})."
-            raise MisconfigurationException(
-                "Specifying an `lr_scheduler_init` requires at least a  `class_path` to be specified "
-                "but this is not the case for " + phase_specific_msg
+        if (
+            "use_current_optimizer_pg_lrs" in target_sched.keys()
+            and target_sched["use_current_optimizer_pg_lrs"]
+            and "init_pg_lrs" not in target_sched.keys()
+        ):
+            info_msg = (
+                "Since `use_current_optimizer_pg_lrs` has been set to `True`, lr scheduler reinitializations "
+                f"associated with phase {depth} will use the current optimizer `lr`s rather than defaulting "
+                "to the existing optimizer's `initial_lr` configuration for existing parameter groups."
             )
+            rank_zero_info(info_msg)
         if "init_pg_lrs" in target_sched.keys():
             warn_msg = (
                 "Found an `init_pg_lrs` key in the specified lr scheduler reinitialization config. Remember to "
                 "ensure the number of specified parameter groups matches the number of parameter groups created in "
                 "in previous phases. This aspect of the optimization path is not currently fully simulated on "
                 "`FinetuningScheduler` initialization so is left to the user to validate."
             )
             assert depth
             ScheduleParsingMixin._parse_reint_pg_lrs(depth=depth, init_pg_lrs=target_sched["init_pg_lrs"])
             rank_zero_warn(warn_msg)
         lr_scheduler_init = target_sched.get("lr_scheduler_init")
         assert lr_scheduler_init
         self._lr_scheduler_sanity_chk(lr_scheduler_init, implicit_chk)
 
-    def _lr_scheduler_init_validation(self, lr_reinit_phases: Dict) -> None:
-        """Trigger lr scheduler reinitialization configuration validation for all provided configurations. This
-        will be a single configuration for implicit mode fine-tuning or n configurations for explicit mode.
+    def _reinit_validation(self, reinit_cfg: Dict) -> None:
+        """Trigger reinitialization configuration validation for all provided configurations. This will be a single
+        configuration for implicit mode fine-tuning or n configurations for explicit mode.
 
         Args:
-            lr_reinit_phases (Dict): Dictionary of lr scheduler reinitialization configurations to parse/validate
-        """
-        if self.reinit_lr_cfg:
-            self._lr_scheduler_reinit_key_validation(lr_reinit_phases)
-        else:
-            for k, lr_cfg in lr_reinit_phases.items():
-                self._lr_scheduler_reinit_key_validation(lr_cfg, k)
+            reinit_cfg (Dict): An lr scheduler and/or optimizer reinitialization configuration to parse/validate
+        """
+        reinit_validation_funcs = (self._lr_scheduler_reinit_key_validation, self._optimizer_reinit_key_validation)
+        for (rk, rp), rattr, rfunc in zip(
+            reinit_cfg.items(), ScheduleParsingMixin.VALID_REINIT_ATTR, reinit_validation_funcs
+        ):
+            if getattr(self, rattr):
+                rfunc(reinit_cfg[rk])
+            else:
+                for k, r_cfg in rp.items():
+                    rfunc(r_cfg, k)
 
-    def _validate_lr_scheduler_cfg(self) -> None:
-        """Orchestrate lr scheduler reinitialization configuration validation.
+    def _validate_reinit_cfg(self) -> None:
+        """Orchestrate optimizer and lr scheduler reinitialization configuration validation.
 
         Raises:
-            MisconfigurationException: If a `new_lr_scheduler` configuration is passed to the initial training phase.
+            MisconfigurationException: If a `new_optimizer` or `new_lr_scheduler` configuration is passed to the initial
+                training phase.
         """
         assert isinstance(self.ft_schedule, Dict)
-        lr_reinit_phases = self.reinit_lr_cfg or {
-            k: self.ft_schedule[k].get("new_lr_scheduler")
-            for k in self.ft_schedule.keys()
-            if self.ft_schedule[k].get("new_lr_scheduler")
-        }
-        if not lr_reinit_phases:
-            return  # no further validation needed since there is no lr scheduler reinitialization configuration
+        reinit_cfg = {}
+        for reinit_k, attr in zip(ScheduleParsingMixin.VALID_REINIT_KEYS, ScheduleParsingMixin.VALID_REINIT_ATTR):
+            reinit_cfg[reinit_k] = getattr(self, attr) or {
+                k: self.ft_schedule[k].get(reinit_k)
+                for k in self.ft_schedule.keys()
+                if self.ft_schedule[k].get(reinit_k)
+            }
+        if not any(reinit_cfg.values()):
+            return  # no further validation needed since there is no reinitialization configuration
+        self._has_reinit_schedule = True  # schedules that reinitialize require special handling in some contexts
         assert self.pl_module.trainer is not None
         assert self.pl_module.trainer.log_dir is not None
-        if 0 in lr_reinit_phases.keys():
-            raise MisconfigurationException(
-                "You have specified a `new_lr_scheduler` for the initial training phase which is an invalid "
-                "configuration. The initial lr_scheduler configuration should be passed to your LightningModule."
-            )
-        self._lr_scheduler_init_validation(lr_reinit_phases)
+        for rk, rp in reinit_cfg.items():
+            if isinstance(rp, dict) and 0 in rp.keys():
+                raise MisconfigurationException(
+                    f"You have specified a `{rk}` reinitialization directive for the initial training phase which is an"
+                    "invalid configuration. The initial configuration should be passed to your LightningModule."
+                )
+        self._reinit_validation(reinit_cfg)
 
     def _convert_phase_keys(self) -> None:
         """Ensures phase keys are integers, converting them to integers if possible and raising an error otherwise.
 
         Raises:
             MisconfigurationException: If the phase keys provided in the schedule are not convertible to integers.
         """
@@ -863,28 +894,115 @@
         dup_params = list(params.elements())
         if dup_params:
             raise MisconfigurationException(
                 f"Phases are not disjoint. The following parameters are specified in "
                 f"multiple phases: {', '.join(dup_params)}"
             )
 
-    def reinit_lr_scheduler(self, new_lr_scheduler: Dict, trainer: pl.Trainer, optimizer: Optimizer) -> None:
+    def _reinit_phase0_pgs(self, thawed_pl: List) -> List:
+        """Reconstruct the parameter groups associated with phase 0 of the schedule.
+
+        Args:
+            thawed_pl (List): A list of parameter names from which to construct the initial parameter groups.
+
+        Returns:
+            List: A list of one or two new parameter groups (contingent on the module's use of ``no_decay``)
+        """
+        no_decay = getattr(self.pl_module, "no_decay", None)
+        if no_decay:
+            pgs = [
+                {
+                    "params": [
+                        p
+                        for n, p in self.pl_module.named_parameters()
+                        if not any(nd in n for nd in no_decay) and n in thawed_pl and p.requires_grad
+                    ]
+                },
+                {
+                    "params": [
+                        p
+                        for n, p in self.pl_module.named_parameters()
+                        if any(nd in n for nd in no_decay) and n in thawed_pl and p.requires_grad
+                    ],
+                    "weight_decay": 0.0,
+                },
+            ]
+        else:
+            pgs = [{"params": [p for n, p in self.pl_module.named_parameters() if n in thawed_pl and p.requires_grad]}]
+        return pgs
+
+    def _save_pre_reinit_lr_state(self, trainer: pl.Trainer) -> Tuple[Dict, List]:
+        """Capture the existing lr state for all parameter groups associated with previous depths to enable
+        restoration during the next phase transition.
+
+        Args:
+            trainer (pl.Trainer): The :external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer` object.
+
+        Returns:
+            Tuple[Dict, List]: The lr state to restore from the current lr scheduler and the most recent `lr`s for
+                parameter groups associated with the current phases's optimizer.
+        """
+        curr_lr_state = {}
+        if trainer.lr_scheduler_configs:
+            curr_lr_state = deepcopy(trainer.lr_scheduler_configs[0].scheduler.state_dict())
+        prev_optimizer_lrs = copy([group["lr"] for group in trainer.strategy.optimizers[0].param_groups])
+        return curr_lr_state, prev_optimizer_lrs
+
+    def reinit_optimizer(self, new_optimizer: Dict, trainer: pl.Trainer, init_params: List) -> ParamGroupAddable:
+        """Reinitialize the optimizer, using a validated optimizer reinitialization configuration.
+
+        Args:
+            new_optimizer (Dict): A dictionary defining the new optimizer configuration to be initialized.
+            trainer (pl.Trainer): The :external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer` object.
+            init_params (List): The list of parameter names with which to initialize the new optimizer.
+
+        Returns:
+            ParamGroupAddable: A handle for the newly reinitialized optimizer.
+        """
+        optimizer_init = new_optimizer["optimizer_init"]
+        prev_optim_repr = repr(trainer.strategy.optimizers[0])
+        optimizer_class = self._import_reinit_class(optimizer_init, reinit_target="optimizer")
+        reinit_pgs = self._reinit_phase0_pgs(thawed_pl=init_params)
+        new_optimizer_handle = optimizer_class(reinit_pgs, **optimizer_init.get("init_args", {}))
+        # If the user or optimizer doesn't set `initial_lr` keys, add them based on the initial lr values.
+        # The latest LR state will still be set in subsequent phases, but this allows subsequent lr scheduler
+        # reinitializations to access an `initial_lr` for the existing optimizer if desired (important for consistency
+        # with lr scheduler-only reinitializations).
+        for group in new_optimizer_handle.param_groups:
+            group["initial_lr"] = group.get("initial_lr", group["lr"])
+        trainer.strategy.optimizers = [new_optimizer_handle]
+        if trainer.lr_scheduler_configs:
+            trainer.lr_scheduler_configs[0].scheduler.optimizer = new_optimizer_handle
+        self._maybe_trace_reinit("optimizer", prev_optim_repr, repr(trainer.strategy.optimizers[0]))
+        return new_optimizer_handle
+
+    def reinit_lr_scheduler(self, new_lr_scheduler: Dict, trainer: pl.Trainer, optimizer: ParamGroupAddable) -> None:
         """Reinitialize the learning rate scheduler, using a validated learning rate scheduler configuration and
         wrapping the existing optimizer.
 
         Args:
             new_lr_scheduler (Dict): A dictionary defining the new lr scheduler configuration to be initialized.
             trainer (pl.Trainer): The :external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer` object.
-            optimizer (:external+torch:class:`~torch.optim.Optimizer`): The
-                :external+torch:class:`~torch.optim.Optimizer` around which the new lr scheduler will be wrapped.
+            optimizer (:class:`~finetuning_scheduler.types.ParamGroupAddable`): A supported optimizer instance around
+                which the new lr scheduler will be wrapped.
         """
+        ################################################################################################################
+        # The following precedence governs the configuration of existing parameter group `lr`s when reinitializing an LR
+        # scheduler:
+        #   1. User-provided `lr`s from the `init_pg_lrs` directive if it exists
+        #   2. Existing optimizer `lr`s if ``use_current_optimizer_pg_lrs`` is set to ``True``
+        #   3. The ``initial_lr`` of the current optimizer parameter groups by default
+        #   4. The existing optimizer `lr`s if ``use_current_optimizer_pg_lrs`` is not set to ``True`` but the relevant
+        #      parameter group does not have an ``initial_lr`` key
+        ################################################################################################################
         lr_scheduler_init = new_lr_scheduler["lr_scheduler_init"]
-        lrs_class = self._import_lr_scheduler(lr_scheduler_init)
-        # unless overridden by user directive, reset optimizer pg lrs to initial before wrapping in new scheduler
-        curr_optimizer_lrs = [group.get("initial_lr", group["lr"]) for group in optimizer.param_groups]
+        prev_lrs_repr = repr(trainer.lr_scheduler_configs[0])
+        lrs_class = self._import_reinit_class(lr_scheduler_init, reinit_target="lr_scheduler")
+        existing_lr_key = "initial_lr" if not new_lr_scheduler.get("use_current_optimizer_pg_lrs", None) else "lr"
+        curr_optimizer_lrs = [group.get(existing_lr_key, group["lr"]) for group in optimizer.param_groups]
         reset_init_pg_lrs = True if new_lr_scheduler.get("init_pg_lrs", None) else False
         initial_optimizer_lrs = new_lr_scheduler.get("init_pg_lrs", curr_optimizer_lrs)
         for _, data in enumerate(zip(optimizer.param_groups, initial_optimizer_lrs)):
             param_group, lr = data
             param_group["lr"] = lr
             if reset_init_pg_lrs:
                 param_group["initial_lr"] = lr
@@ -893,14 +1011,29 @@
         new_lrs_config = LRSchedulerConfig(
             scheduler=lrs_class(
                 optimizer=optimizer, **lr_scheduler_init.get("init_args", {})
             ),  # type: ignore[arg-type]
             **new_lr_scheduler.get("pl_lrs_cfg", {}),
         )
         trainer.strategy.lr_scheduler_configs = [new_lrs_config]
+        self._maybe_trace_reinit("lr scheduler", prev_lrs_repr, repr(trainer.lr_scheduler_configs[0]))
+
+    def _maybe_trace_reinit(self, target_type: str, prev_repr: str, new_repr: str) -> None:
+        """Trace valid optimizer and lr scheduler transitions (including intermediate restorations).
+
+        Args:
+            target_type (str): The type of object being reinitialized.
+            prev_repr (str): A representation of the state of the target object before reinitialization.
+            new_repr (str): A representation of the state of the target object after reinitialization.
+        """
+        reinit_msg = f"Fine-Tuning Scheduler has reinitialized the {target_type} as directed:{os.linesep}"
+        rank_zero_debug(
+            reinit_msg + f"Previous {target_type} state:`{prev_repr}`{os.linesep}"
+            f"New {target_type} state: `{new_repr}`{os.linesep}"
+        )
 
     @staticmethod
     def _parse_reint_pg_lrs(depth: int, init_pg_lrs: List) -> None:
         """Parse/Define per-phase base-learning rate overrides for an lr scheduler reinitialization.
 
         Args:
             depth (int): the current schedule depth being evaluated
@@ -942,40 +1075,65 @@
             else:
                 warn_msg = (
                     "Allowing untested scheduler"
                     f" '{type(lr_class)}' because ``allow_untested`` is ``True``."  # type: ignore[attr-defined]
                 )
                 rank_zero_warn(warn_msg)
 
-    def _import_lr_scheduler(self, lr_scheduler_init: Dict) -> FTSLRSchedulerType:
-        """Import the lr scheduler specified in the provided `lr_scheduler_init` configuration.
+    def _is_supported_reinit_optimizer(self, optim_class: Union[Any, ParamGroupAddable]) -> None:
+        """Evaulate whether the provided optimizer is currently supported in the context of optimizer
+        reinitialization.
 
         Args:
-            lr_scheduler_init (Dict): The user-provided lr scheduler reinitialization configuration.
+            optim_class (ParamGroupAddable): The optimizer class to be inspected for support.
 
         Raises:
-            MisconfigurationException: If the specified LR scheduler cannot be imported successfully.
+            MisconfigurationException: If the provided optimizer class is known to be currently unsupported in the
+                context of optimizer reinitialization.
+        """
+        if issubclass(optim_class, ZeroRedundancyOptimizer):
+            error_msg = (
+                f"The provided optimizer ({optim_class}) is not currently supported by FinetuningScheduler in the"
+                " context of optimizer reinitialization. Please use a currently supported torch optimizer (or subclass"
+                " thereof) from those provided in `torch.optim`: https://pytorch.org/docs/stable/optim.html#algorithms."
+            )
+            rank_zero_warn(error_msg)
+            raise MisconfigurationException(error_msg)
+
+    def _import_reinit_class(
+        self, reinit_cfg: Dict, reinit_target: str
+    ) -> Union[FTSLRSchedulerType, ParamGroupAddable]:
+        """Import the reinitialization class (lr scheduler or optimizer) specified in the provided reinitialization
+        configuration.
+
+        Args:
+            reinit_cfg (Dict): The user-provided reinitialization configuration.
+            reinit_target (str): The reinitialization target, currently "optimizer" or "lr_scheduler".
+
+        Raises:
+            MisconfigurationException: If the specified class cannot be imported successfully.
 
         Returns:
-            FTSLRSchedulerType: The lr scheduler class to be instantiated.
+            Union[FTSLRSchedulerType, ParamGroupAddable]: The class to reinitialize.
         """
         try:
-            class_module, class_name = lr_scheduler_init["class_path"].rsplit(".", 1)
+            class_module, class_name = reinit_cfg["class_path"].rsplit(".", 1)
             module = __import__(class_module, fromlist=[class_name])
-            lrs_class = getattr(module, class_name)
-            self._is_supported_lr(lrs_class)
+            reinit_class = getattr(module, class_name)
+            if reinit_target == "lr_scheduler":
+                self._is_supported_lr(reinit_class)
         except (ImportError, AttributeError) as err:
             error_msg = (
-                f"Could not import specified LR scheduler class using class_path ({lr_scheduler_init['class_path']}) "
-                f"Recieved the following error while importing: {err}. Please validate specified `class_path` before "
-                "resubmitting."
+                "Could not import specified reinitialization configuration class using class_path "
+                f"({reinit_cfg['class_path']}). Recieved the following error while importing: {err}. Please validate "
+                "specified `class_path` before resubmitting."
             )
             rank_zero_warn(error_msg)
             raise MisconfigurationException(error_msg)
-        return lrs_class
+        return reinit_class
 
     @staticmethod
     def _import_strategy_adapter(strategy_key: str, adapter_map: Dict[str, str]) -> Type[StrategyAdapter]:
         """Import the custom strategy adapter specified in the ``custom_strategy_adapter`` configuration.
 
         Args:
             qualname (Dict): The user-provided custom strategy adapter fully qualified class name.
@@ -1004,28 +1162,56 @@
                 f" name ({qualname}). Recieved the following error while importing: {err}. Please validate specified"
                 " path."
             )
             rank_zero_warn(error_msg)
             raise MisconfigurationException(error_msg)
         return custom_strategy_adapter_cls
 
+    def _optimizer_sanity_chk(self, optimizer_init: Dict) -> None:
+        """Before beginning execution of defined fine-tuning schedule, perform a sanity check of the specified
+        optimizer reinitialization configuration. To the extent reasonable (i.e. without simulating the entire
+        training path), if the provided optimizer reinitialization configuration is expected to fail, it is user-
+        friendly to provide this feedback to the user before training begins.
+
+        Args:
+            optimizer_init (Dict): The user-provided optimizer reinitialization configuration.
+
+        Raises:
+            MisconfigurationException: If a valid and supported scheduler cannot be instantiated with the specified
+                init args.
+        """
+        optimizer_class = self._import_reinit_class(optimizer_init, reinit_target="optimizer")
+        self._is_supported_reinit_optimizer(optimizer_class)
+        test_optimizer_init = copy(optimizer_init.get("init_args", {}))
+        try:
+            test_optimizer = optimizer_class(ScheduleParsingMixin.SANITY_CHK_ITERABLE, **test_optimizer_init)
+        except Exception as err:
+            error_msg = (
+                "Could not configure the specified optimizer class using the `init_args` "
+                f"({optimizer_init['init_args']}). Recieved the following error while sanity checking schedule "
+                f"phases: {err}. Please validate specified `init_args` before resubmitting."
+            )
+            rank_zero_warn(error_msg)
+            raise MisconfigurationException(error_msg)
+        assert isinstance(test_optimizer, ParamGroupAddable)
+
     def _lr_scheduler_sanity_chk(self, lr_scheduler_init: Dict, is_implicit_mode: bool = False) -> None:
         """Before beginning execution of defined fine-tuning schedule, perform a sanity check of the specified lr
         scheduler reinitialization configuration. To the extent reasonable (i.e. without simulating the entire
         training path), if the provided lr scheduler reinitialization configuration is expected to fail, it is
         user-friendly to provide this feedback to the user before training begins.
 
         Args:
             lr_scheduler_init (Dict): The user-provided lr scheduler reinitialization configuration.
 
         Raises:
             MisconfigurationException: If a valid and supported scheduler cannot be instantiated with the specified
                 init args.
         """
-        lrs_class = self._import_lr_scheduler(lr_scheduler_init)
+        lrs_class = self._import_reinit_class(lr_scheduler_init, reinit_target="lr_scheduler")
         if lr_scheduler_init.get("init_args") and "optimizer" in lr_scheduler_init.get("init_args", {}).keys():
             warn_msg = (
                 f"Found an `optimizer` key in the provided `lr_scheduler_init`: {lr_scheduler_init['init_args']} "
                 f"Note that the existing optimizer and all associated parameter groups will be used when "
                 "reinitializing the lr schedule using the specified scheduler so the provided `optimizer` key will "
                 "have no effect."
             )
@@ -1060,14 +1246,15 @@
 
 class ScheduleImplMixin(ABC):
     """Functionality for generating and executing fine-tuning schedules."""
 
     # proper initialization of these variables should be done in the child class
     pl_module: pl.LightningModule
     ft_schedule: Optional[Union[str, dict]]
+    reinit_optim_cfg: Optional[Dict]
     reinit_lr_cfg: Optional[Dict]
     max_depth: int
     _fts_state: FTSState
     PHASE_0_DIVERGENCE_MSG = (
         "After executing the provided `configure_optimizers` method, the optimizer state differs from the configuration"
         " FinetuningScheduler expected at the beginning of scheduled fine-tuning (phase 0).\n"
     )
@@ -1272,30 +1459,66 @@
         for i, next_tl in self.ft_schedule.items():  # type: ignore[union-attr]
             if i <= depth:
                 _, self._fts_state._curr_thawed_params = self.strategy_adapter.exec_ft_phase(
                     self.pl_module, thaw_pl=self.strategy_adapter.fts_optim_transform(next_tl["params"])
                 )
 
     @staticmethod
+    def _repartition_sharded_optim(optimizer: ParamGroupAddable) -> None:
+        """Repartition and reset a sharded optimizer state.
+
+        Args:
+            optimizer (ParamGroupAddable): The target optimizer to repartition.
+        """
+        # For optimizers that shard their states like (e.g. ZeroRedundancyOptimizer), one use case for this method is
+        # to clear local optimizer partition caches and repartition to support restoring across multiple depths
+        partition_params = (
+            optimizer._partition_parameters
+            if callable(optimizer._partition_parameters)
+            else optimizer.partition_parameters
+        )
+        optimizer._clear_cache()
+        optimizer.optim.param_groups = partition_params()[optimizer.rank]
+        optimizer._sync_param_groups(optimizer.optim.param_groups, optimizer.param_groups)
+
+    def _restore_latest_lr_state(self, curr_lr_state: Dict, prev_optimizer_lrs: List) -> None:
+        """Adapt the existing lr state for all parameter groups associated with previous depths (new groups for the
+        current phase should use the schedule or new optimizer defaults).
+
+        Args:
+            curr_lr_state (Dict): The lr state to restore from the current lr scheduler (captured prior to mutation
+            associated with adding groups to the new optimizer)
+            prev_optimizer_lrs (List): The most recent `lr`s for parameter groups associated with the previous optimizer
+        """
+        trainer = self.pl_module.trainer
+        if trainer.lr_scheduler_configs:  # type: ignore[union-attr]
+            for lrs_cfg in trainer.lr_scheduler_configs:  # type: ignore[union-attr]
+                lrs_cfg.scheduler.load_state_dict(curr_lr_state)
+        for _, data in enumerate(zip(trainer.strategy.optimizers[0].param_groups, prev_optimizer_lrs)):
+            param_group, lr = data
+            param_group["lr"] = lr
+        rank_zero_debug("Current LR state restored for previous depth parameter groups.")
+
+    @staticmethod
     def add_optimizer_groups(
         module: Module,
-        optimizer: Optimizer,
+        optimizer: ParamGroupAddable,
         thawed_pl: List,
         no_decay: Optional[list] = None,
         lr: Optional[float] = None,
         apply_lambdas: bool = False,
     ) -> None:
         """Add optimizer parameter groups associated with the next scheduled fine-tuning depth/level and extend the
         relevent :paramref:`~pytorch_lighting.trainer.trainer.Trainer.lr_scheduler_configs`.
 
         Args:
             module (:class:`~torch.nn.Module`): The :class:`~torch.nn.Module` from which the target optimizer parameters
                 will be read.
-            optimizer (:external+torch:class:`~torch.optim.Optimizer`): The
-                :external+torch:class:`~torch.optim.Optimizer` to which parameter groups will be configured and added.
+            optimizer (:class:`~finetuning_scheduler.types.ParamGroupAddable`): The supported optimizer instance to
+                which parameter groups will be configured and added.
             thawed_pl: The list of thawed/unfrozen parameters that should be added to the new parameter group(s)
             no_decay: A list of parameters that should always have weight_decay set to 0. e.g.:
                 ["bias", "LayerNorm.weight"]. Defaults to ``None``.
             lr: The initial learning rate for the new parameter group(s). If not specified,
                 the ``lr`` of the first scheduled fine-tuning depth will be used. Defaults to ``None``.
             apply_lambdas: Whether to apply lr lambdas to newly added groups. Defaults to False.
 
@@ -1323,24 +1546,24 @@
                         if hasattr(scheduler, "lr_lambdas"):
                             scheduler.lr_lambdas.extend([scheduler.lr_lambdas[-1]] * added_pgs)
             else:
                 _ = ScheduleImplMixin._add_groups(no_decay, optimizer, module, thawed_pl, phase_lr)
 
     @staticmethod
     def _add_groups(
-        no_decay: Optional[list], optimizer: Optimizer, module: Module, thawed_pl: List, phase_lr: float
+        no_decay: Optional[list], optimizer: ParamGroupAddable, module: Module, thawed_pl: List, phase_lr: float
     ) -> int:
         """The actual addition of optimizer groups is done here, separated from ``add_optimizer_groups`` to
         accommodate corner cases where FTS is being used without an lr scheduler configuration.
 
         Args:
             no_decay: A list of parameters that should always have weight_decay set to 0. e.g.:
                 ["bias", "LayerNorm.weight"]. Defaults to ``None``.
-            optimizer (:external+torch:class:`~torch.optim.Optimizer`): The
-                :external+torch:class:`~torch.optim.Optimizer` to which parameter groups will be configured and added.
+            optimizer (:class:`~finetuning_scheduler.types.ParamGroupAddable`): The supported optimizer instance to
+                which parameter groups will be configured and added.
             module (:class:`~torch.nn.Module`): The :class:`~torch.nn.Module` from which the target optimizer parameters
                 will be read.
             thawed_pl: The list of thawed/unfrozen parameters that should be added to the new parameter group(s)
             phase_lr (float): The initial learning rate for the new parameter group(s).
 
         Returns:
             int: The number of optimizer parameter groups that were added.
@@ -1465,15 +1688,15 @@
         return w_msg
 
     def _validate_opt_init(self) -> None:
         """Validate the user-initialized optimizer state (necessary for fine-tuning phase 0) and warn user if
         appropriate.
 
         Args:
-            optimizer (Optimizer): The optimizer initialized.
+            optimizer (ParamGroupAddable): The optimizer initialized.
             ft_schedule (Dict): The fine-tuning schedule to be inspected vis-a-vis the optimizer state.
         """
         no_grad_cnt, init_ft_cnt, total_ft_cnt, param_diff_summary = self._inspect_fts_opt_state()
         if param_diff_summary or no_grad_cnt > 0:
             if self.enforce_phase0_params:
                 # implemented in `StrategyAdapter` since override behavior may be strategy-dependent in the future
                 self.strategy_adapter.phase0_optimizer_override()
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/setup_tools.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/setup_tools.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/__init__.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/__init__.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/base.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/base.py`

 * *Files 19% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 
 """
 from functools import partialmethod
 from pprint import pformat as pfmt
 from typing import Callable, List, Optional, Tuple
 
 from lightning.fabric.utilities import rank_zero_info
+from lightning.fabric.utilities.imports import _TORCH_GREATER_EQUAL_1_13
 from lightning.fabric.utilities.types import ReduceLROnPlateau
 from lightning.pytorch import LightningModule, Trainer
 from lightning.pytorch.callbacks import Callback
 from lightning.pytorch.strategies.strategy import Strategy
 from lightning.pytorch.utilities.rank_zero import rank_zero_debug
 from torch.nn import Module
 
@@ -84,14 +85,23 @@
 
         Returns:
             Strategy: The :external+pl:class:`~lightning.pytorch.strategies.Strategy` in use.
         """
         assert self.pl_module._trainer is not None
         return self.pl_module._trainer.strategy
 
+    @property
+    def using_sharded_optimizer(self) -> bool:
+        """Whether the currently used optimizer is a supported sharded optimizer.
+
+        Returns:
+            bool: Returns ``True`` if the current optimizer is a supported sharded optimizer.
+        """
+        return hasattr(self.pl_module.trainer.optimizers[0], "consolidate_state_dict")
+
     def on_before_init_fts(self) -> None:
         """Hook executed in :class:`~finetuning_scheduler.fts.FinetuningScheduler` setup immediately before
         :meth:`~finetuning_scheduler.fts_supporters.ScheduleImplMixin.init_fts`
         """
 
     def on_after_init_fts(self) -> None:
         """Hook executed in :class:`~finetuning_scheduler.fts.FinetuningScheduler` setup immediately after
@@ -111,46 +121,43 @@
     def on_before_restore_optimizers_and_lrs(self) -> None:
         """Hook executed immediately before :class:`~finetuning_scheduler.fts.FinetuningScheduler` restores
         optimizers and schedulers."""
 
     def fts_optim_transform(self, orig_pl: List, inspect_only: bool = False) -> List:
         """A method that can be overridden by a :class:`~finetuning_scheduler.strategy_adapters.StrategyAdapter` if
         a :external+pl:class:`~lightning.pytorch.strategies.Strategy` performs parameter transformations that cause
-        the current :external+torch:class:`~torch.optim.Optimizer`'s view of parameter names to diverge from the
-        original parameter names. By default, no transformation of schedule parameter names is required for
-        optimizer operations.
+        the current optimizer's view of parameter names to diverge from the original parameter names. By default,
+        no transformation of schedule parameter names is required for optimizer operations.
 
         Args:
             orig_pl (List): The original parameter name list before a given
                 :external+pl:class:`~lightning.pytorch.strategies.Strategy`'s transformation of them.
             inspect_only (bool): Whether to use the specified transform in read-only (i.e. ``inspect_only``) mode,
                 avoiding any persistent state transformation that may accompany normal usage. Typically useful for state
                 inspection and validation contexts.
 
         Returns:
-            List: A transformed parameter name list that matches the current
-                :external+torch:class:`~torch.optim.Optimizer`'s view of them after a given
+            List: A transformed parameter name list that matches the current optimizer's view of them after a given
                 :external+pl:class:`~lightning.pytorch.strategies.Strategy`'s transformation of the original parameter
                 names.
         """
         return orig_pl
 
     def logical_param_translation(self, param_names: List) -> List:
         """Effectively the reverse transformation of
         :meth:`~finetuning_scheduler.strategy_adapters.StrategyAdapter.fts_optim_transform`. Can be overridden by a
         :class:`~finetuning_scheduler.strategy_adapters.StrategyAdapter` if a
         :external+pl:class:`~lightning.pytorch.strategies.Strategy` performs parameter transformations that cause the
-        original user view of parameter names to diverge from the current
-        :external+torch:class:`~torch.optim.Optimizer`'s view. By default, no transformation of
-        :external+torch:class:`~torch.optim.Optimizer` parameter names is required.
+        original user view of parameter names to diverge from the current optimizer's view. By default, no
+        transformation of optimizer parameter names is required.
 
         Args:
-            param_names (List): A parameter name list from the current :external+torch:class:`~torch.optim.Optimizer`'s
-                view of them after a :external+pl:class:`~lightning.pytorch.strategies.Strategy`'s transformation of the
-                original parameter names.
+            param_names (List): A parameter name list from the current optimizer's view of them after a
+                :external+pl:class:`~lightning.pytorch.strategies.Strategy`'s transformation of the original parameter
+                names.
 
         Returns:
             List: The original parameter name list before a given
                 :external+pl:class:`~lightning.pytorch.strategies.Strategy`'s transformation.
         """
         return param_names
 
@@ -167,40 +174,72 @@
                 currently supported by FTS, this list will have only a single element in this verison.)
         """
         orig_num_pgs = []
         for optimizer in trainer.optimizers:
             orig_num_pgs.append(len(optimizer.param_groups))
             optimizer.param_groups = []
         for lrs_cfg in trainer.lr_scheduler_configs:
-            lrs_cfg.scheduler.base_lrs = []
+            lrs_cfg.scheduler.last_epoch = -1
+            if not isinstance(lrs_cfg.scheduler, ReduceLROnPlateau):
+                lrs_cfg.scheduler.base_lrs = []
         return orig_num_pgs
 
+    def _reconfigure_optimizer_for_phase0(self, trainer: Trainer) -> None:
+        """Reconfigure optimizer state to comport with the scheduled phase 0.
+
+        Args:
+            trainer (Trainer): The :external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer` object.
+        """
+        if self.using_sharded_optimizer:
+            # update the parent (sharded) optimizer defaults with the wrapped optimizer defaults to ensure they are
+            # included in our newly configured param groups
+            trainer.optimizers[0].defaults.update(trainer.optimizers[0].optim.defaults)
+        # thaw only params scheduled in phase 0
+        self.fts_handle.step_pg(depth=self.fts_handle.curr_depth, optimizer=trainer.optimizers[0], depth_sync=False)
+        if self.using_sharded_optimizer:
+            # update internal sharded optimizer state with the new set of parameters
+            trainer.optimizers[0]._verify_and_init_params([p for p in self.pl_module.parameters() if p.requires_grad])
+            # repartition the sharded optimizer state
+            self.fts_handle._repartition_sharded_optim(trainer.optimizers[0])
+
+    def _reconfigure_lrs_for_phase0(self, trainer: Trainer, orig_num_pgs: List) -> None:
+        """Reconfigure lr scheduler state to comport with the scheduled phase 0.
+
+        Args:
+            trainer (Trainer): The :external+pl:class:`~lightning.pytorch.trainer.trainer.Trainer` object.
+            orig_num_pgs (List): A list of the number of parameter groups pruned for each optimizer (since only a single
+                optimizer is currently supported by FTS, this list will have only a single element in this verison.)
+        """
+        # since we may have added parameter groups (e.g. implementing ``no_decay`` for user), we need to reinitialize
+        # certain lr_scheduler variables (including type-dependent ones like ``min_lrs`` and ``lr_lambdas``)
+        if trainer.lr_scheduler_configs:
+            for lrs_cfg in trainer.lr_scheduler_configs:
+                if _TORCH_GREATER_EQUAL_1_13 and not isinstance(lrs_cfg.scheduler, ReduceLROnPlateau):
+                    lrs_cfg.scheduler._initial_step()
+                lrs_cfg.scheduler._last_lr = [group["lr"] for group in lrs_cfg.scheduler.optimizer.param_groups]
+                if isinstance(lrs_cfg.scheduler, ReduceLROnPlateau):
+                    lrs_cfg.scheduler.min_lrs = lrs_cfg.scheduler.min_lrs[orig_num_pgs[0] :]
+                elif hasattr(lrs_cfg.scheduler, "lr_lambdas"):
+                    lrs_cfg.scheduler.lr_lambdas = lrs_cfg.scheduler.lr_lambdas[orig_num_pgs[0] :]
+
     def phase0_optimizer_override(self) -> None:
         """Reconfigure the user-configured optimizer (configured via `configure_optimizers`) to optimize the
         parameters (and only those parameters) scheduled to be optimized in phase 0 of the current fine-tuning
         schedule.
 
         Reconfiguration only takes place here if FTS discovers the set of parameters to be initially thawed and present
         in the optimizer differs from the parameters specified in phase 0. Only the parameters included in the optimizer
         are affected; the choice of optimizer, lr_scheduler etc. remains unaltered.
         """
         trainer = self.pl_module.trainer
         orig_num_pgs = StrategyAdapter._clean_optim_lr_pgs(trainer)
         # refreeze in case user has thawed parameters not present in phase 0
         self.fts_handle.freeze_before_training(self.pl_module)
-        # thaw only params scheduled in phase 0
-        self.fts_handle.step_pg(depth=self.fts_handle.curr_depth, optimizer=trainer.optimizers[0], depth_sync=False)
-        # since we may have added parameter groups (e.g. implementing ``no_decay`` for user), we need to reinitialize
-        # certain lr_scheduler variables (including type-dependent ones like ``min_lrs`` and ``lr_lambdas``)
-        for lrs_cfg in trainer.lr_scheduler_configs:
-            lrs_cfg.scheduler._last_lr = [group["lr"] for group in lrs_cfg.scheduler.optimizer.param_groups]
-            if isinstance(lrs_cfg.scheduler, ReduceLROnPlateau):
-                lrs_cfg.scheduler.min_lrs = lrs_cfg.scheduler.min_lrs[orig_num_pgs[0] :]
-            elif hasattr(lrs_cfg.scheduler, "lr_lambdas"):
-                lrs_cfg.scheduler.lr_lambdas = lrs_cfg.scheduler.lr_lambdas[orig_num_pgs[0] :]
+        self._reconfigure_optimizer_for_phase0(trainer)
+        self._reconfigure_lrs_for_phase0(trainer, orig_num_pgs)
         p0_override_msg = self.fts_handle.PHASE_0_DIVERGENCE_MSG + (
             "Since `enforce_phase0_params` is currently set to `True` (the default), FinetuningScheduler has"
             " reconfigured the optimizer to optimize the parameters (and only those parameters) scheduled to be"
             " optimized in phase 0 of the current fine-tuning schedule.\n\n"
         )
         rank_zero_info(p0_override_msg)
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler/strategy_adapters/fsdp.py` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler/strategy_adapters/fsdp.py`

 * *Files 2% similar despite different names*

```diff
@@ -236,29 +236,27 @@
         else:
             rank_zero_debug(
                 "Since FSDP has been configured with `use_orig_params` set to `True`, "
                 "restoring model parameters but bypassing restoration of optimizer state."
             )
 
     def fts_optim_transform(self, orig_pl: List, inspect_only: bool = False) -> List:
-        """Because FSDP performs parameter transformations that cause the current.
-
-        :external+torch:class:`~torch.optim.Optimizer`'s view of parameter names to diverge from the original parameter
-        names, this parameter transformation is required for optimizer operations.
+        """Because FSDP performs parameter transformations that cause the current optimizer's view of parameter
+        names to diverge from the original parameter names, this parameter transformation is required for optimizer
+        operations.
 
         Args:
             orig_pl (List): The original parameter name list before FSDP's transformation of them.
             inspect_only (bool): Whether to use the specified transform in read-only (i.e. ``inspect_only``) mode,
                 avoiding any persistent state transformation that may accompany normal usage. Typically useful for state
                 inspection and validation contexts.
 
         Returns:
-            List: A transformed parameter name list that matches the current
-            :external+torch:class:`~torch.optim.Optimizer`'s view of them after FSDP's transformation of the original
-            parameter names.
+            List: A transformed parameter name list that matches the current optimizer's view of them after FSDP's
+                transformation of the original parameter names.
         """
         return self.fsdp_param_transform(orig_pl, inspect_only)
 
     def fsdp_param_transform(self, orig_thaw_pl: List, inspect_only: bool) -> List:
         """The parameter transformation function currently used by
         :meth:`~finetuning_scheduler.strategy_adapters.FSDPStrategyAdapter.fts_optim_transform` to transform original
         parameter lists for optimizer operations.
@@ -266,17 +264,16 @@
         Args:
             orig_thaw_pl (List): The original parameter name list before FSDP's transformation of them.
             inspect_only (bool): Whether to use the specified transform in read-only (i.e. ``inspect_only``) mode,
                 avoiding any persistent state transformation that may accompany normal usage. Typically useful for state
                 inspection and validation contexts.
 
         Returns:
-            List: A transformed parameter name list that matches the current
-            :external+torch:class:`~torch.optim.Optimizer`'s view of them after FSDP's transformation of the original
-            parameter names.
+            List: A transformed parameter name list that matches the current optimizer's view of them after FSDP's
+                transformation of the original parameter names.
         """
         flat_next_tl = {self._fsdp_unflat_to_flat_mapping[p] for p in orig_thaw_pl}
         if self._use_orig_params and not inspect_only:
             self._flat_param_thaw(flat_next_tl)
         return [n for n, p in self.pl_module.named_parameters() if p in flat_next_tl]
 
     def _flat_param_thaw(self, flat_next_tl: Set) -> None:
@@ -311,16 +308,16 @@
         )
 
     def logical_param_translation(self, param_names: List) -> List:
         """Effectively the reverse transformation of
         :meth:`~finetuning_scheduler.strategy_adapters.FSDPStrategyAdapter.fts_optim_transform`.
 
         Args:
-            param_names (List): A parameter name list from the current :external+torch:class:`~torch.optim.Optimizer`'s
-                view of them after FSDP's transformation of the original parameter names.
+            param_names (List): A parameter name list from the current optimizer's view of them after FSDP's
+                transformation of the original parameter names.
 
         Returns:
             List: The original parameter name list before a given FSDP's transformation.
         """
         logical_param_names = []
         for n, p in self.pl_module.named_parameters():
             if n in param_names:
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/PKG-INFO` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: finetuning-scheduler
-Version: 2.0.1
+Version: 2.0.2
 Summary: A PyTorch Lightning extension that enhances model experimentation with flexible fine-tuning schedules.
 Home-page: https://github.com/speediedan/finetuning-scheduler
 Download-URL: https://github.com/speediedan/finetuning-scheduler
 Author: Dan Dale
 Author-email: danny.dale@gmail.com
 License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/speediedan/finetuning-scheduler/issues
@@ -33,39 +33,39 @@
 Provides-Extra: cli
 Provides-Extra: dev
 Provides-Extra: all
 License-File: LICENSE
 
 <div align="center">
 
-<img src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.1/docs/source/_static/images/logos/logo_fts.png" width="401px">
+<img src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.2/docs/source/_static/images/logos/logo_fts.png" width="401px">
 
 **A PyTorch Lightning extension that enhances model experimentation with flexible fine-tuning schedules.**
 
 ______________________________________________________________________
 
 <p align="center">
   <a href="https://finetuning-scheduler.readthedocs.io/en/stable/">Docs</a> •
   <a href="#Setup">Setup</a> •
   <a href="#examples">Examples</a> •
   <a href="#community">Community</a>
 </p>
 
 [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/finetuning-scheduler)](https://pypi.org/project/finetuning-scheduler/)
 [![PyPI Status](https://badge.fury.io/py/finetuning-scheduler.svg)](https://badge.fury.io/py/finetuning-scheduler)\
-[![codecov](https://codecov.io/gh/speediedan/finetuning-scheduler/release/2.0.1/graph/badge.svg?flag=gpu)](https://codecov.io/gh/speediedan/finetuning-scheduler)
+[![codecov](https://codecov.io/gh/speediedan/finetuning-scheduler/release/2.0.2/graph/badge.svg?flag=gpu)](https://codecov.io/gh/speediedan/finetuning-scheduler)
 [![ReadTheDocs](https://readthedocs.org/projects/finetuning-scheduler/badge/?version=latest)](https://finetuning-scheduler.readthedocs.io/en/stable/)
 [![DOI](https://zenodo.org/badge/455666112.svg)](https://zenodo.org/badge/latestdoi/455666112)
 [![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/speediedan/finetuning-scheduler/blob/master/LICENSE)
 
 </div>
 
 ______________________________________________________________________
 
-<img width="300px" src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.1/docs/source/_static/images/fts/fts_explicit_loss_anim.gif" alt="FinetuningScheduler explicit loss animation" align="right"/>
+<img width="300px" src="https://github.com/speediedan/finetuning-scheduler/raw/v2.0.2/docs/source/_static/images/fts/fts_explicit_loss_anim.gif" alt="FinetuningScheduler explicit loss animation" align="right"/>
 
 [FinetuningScheduler](https://finetuning-scheduler.readthedocs.io/en/stable/api/finetuning_scheduler.fts.html#finetuning_scheduler.fts.FinetuningScheduler) is simple to use yet powerful, offering a number of features that facilitate model research and exploration:
 
 - easy specification of flexible fine-tuning schedules with explicit or regex-based parameter selection
   - implicit schedules for initial/naive model exploration
   - explicit schedules for performance tuning, fine-grained behavioral experimentation and computational efficiency
 - automatic restoration of best per-phase checkpoints driven by iterative application of early-stopping criteria to each fine-tuning phase
@@ -117,32 +117,33 @@
 
 ### Scheduled Fine-Tuning For SuperGLUE
 
 - [Notebook-based Tutorial](https://pytorch-lightning.readthedocs.io/en/stable/notebooks/lightning_examples/finetuning-scheduler.html)
 - [CLI-based Tutorial](https://finetuning-scheduler.readthedocs.io/en/stable/#example-scheduled-fine-tuning-for-superglue)
 - [FSDP Scheduled Fine-Tuning](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/fsdp_scheduled_fine_tuning.html)
 - [LR Scheduler Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/lr_scheduler_reinitialization.html) (advanced)
+- [Optimizer Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/advanced/optimizer_reinitialization.html) (advanced)
 
 ______________________________________________________________________
 
 ## Continuous Integration
 
 Fine-Tuning Scheduler is rigorously tested across multiple CPUs, GPUs and against major Python and PyTorch versions. Each Fine-Tuning Scheduler minor release (major.minor.patch) is paired with a Lightning minor release (e.g. Fine-Tuning Scheduler 2.0 depends upon Lightning 2.0).
 
 To ensure maximum stability, the latest Lightning patch release fully tested with Fine-Tuning Scheduler is set as a maximum dependency in Fine-Tuning Scheduler's requirements.txt (e.g. \<= 1.7.1). If you'd like to test a specific Lightning patch version greater than that currently in Fine-Tuning Scheduler's requirements.txt, it will likely work but you should install Fine-Tuning Scheduler from source and update the requirements.txt as desired.
 
 <details>
   <summary>Current build statuses for Fine-Tuning Scheduler </summary>
 
 | System / (PyTorch/Python ver) |                                                                                                         1.11/3.8                                                                                                         |                                                                                                              2.0.0/3.8, 2.0.0/3.10                                                                                                               |
 | :---------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
-|      Linux \[GPUs\*\*\]       |                                                                                                            -                                                                                                             | [![Build Status](https://dev.azure.com//speediedan/finetuning-scheduler/_apis/build/status/Multi-GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.1)](https://dev.azure.com/speediedan/finetuning-scheduler/_build/latest?definitionId=2&branchName=refs%2Ftags%2F2.0.1) |
-|     Linux (Ubuntu 20.04)      | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
-|           OSX (11)            | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
-|        Windows (2022)         | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
+|      Linux \[GPUs\*\*\]       |                                                                                                            -                                                                                                             | [![Build Status](https://dev.azure.com//speediedan/finetuning-scheduler/_apis/build/status/Multi-GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.2)](https://dev.azure.com/speediedan/finetuning-scheduler/_build/latest?definitionId=2&branchName=refs%2Ftags%2F2.0.2) |
+|     Linux (Ubuntu 20.04)      | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
+|           OSX (11)            | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
+|        Windows (2022)         | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) |             [![Test](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml)             |
 
 - \*\* tests run on two RTX 2070s
 
 </details>
 
 ## Community
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: finetuning-scheduler Version: 2.0.1 Summary: A
+Metadata-Version: 2.1 Name: finetuning-scheduler Version: 2.0.2 Summary: A
 PyTorch Lightning extension that enhances model experimentation with flexible
 fine-tuning schedules. Home-page: https://github.com/speediedan/finetuning-
 scheduler Download-URL: https://github.com/speediedan/finetuning-scheduler
 Author: Dan Dale Author-email: danny.dale@gmail.com License: Apache-2.0
 Project-URL: Bug Tracker, https://github.com/speediedan/finetuning-scheduler/
 issues Project-URL: Documentation, https://finetuning-scheduler.readthedocs.io/
 en/latest/ Project-URL: Source Code, https://github.com/speediedan/finetuning-
@@ -16,24 +16,24 @@
 Apache Software License Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3 Classifier: Programming
 Language :: Python :: 3.8 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10 Requires-Python: >=3.8
 Description-Content-Type: text/markdown Provides-Extra: examples Provides-
 Extra: extra Provides-Extra: test Provides-Extra: ipynb Provides-Extra: cli
 Provides-Extra: dev Provides-Extra: all License-File: LICENSE
-  [https://github.com/speediedan/finetuning-scheduler/raw/v2.0.1/docs/source/
+  [https://github.com/speediedan/finetuning-scheduler/raw/v2.0.2/docs/source/
     _static/images/logos/logo_fts.png] **A PyTorch Lightning extension that
      enhances model experimentation with flexible fine-tuning schedules.**
     ______________________________________________________________________
                    Docs â¢ Setup â¢ Examples â¢ Community
  [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/finetuning-
   scheduler)](https://pypi.org/project/finetuning-scheduler/) [![PyPI Status]
 (https://badge.fury.io/py/finetuning-scheduler.svg)](https://badge.fury.io/py/
 finetuning-scheduler)\ [![codecov](https://codecov.io/gh/speediedan/finetuning-
-   scheduler/release/2.0.1/graph/badge.svg?flag=gpu)](https://codecov.io/gh/
+   scheduler/release/2.0.2/graph/badge.svg?flag=gpu)](https://codecov.io/gh/
    speediedan/finetuning-scheduler) [![ReadTheDocs](https://readthedocs.org/
    projects/finetuning-scheduler/badge/?version=latest)](https://finetuning-
     scheduler.readthedocs.io/en/stable/) [![DOI](https://zenodo.org/badge/
    455666112.svg)](https://zenodo.org/badge/latestdoi/455666112) [![license]
     (https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://
         github.com/speediedan/finetuning-scheduler/blob/master/LICENSE)
 ______________________________________________________________________
@@ -75,15 +75,17 @@
 Examples ### Scheduled Fine-Tuning For SuperGLUE - [Notebook-based Tutorial]
 (https://pytorch-lightning.readthedocs.io/en/stable/notebooks/
 lightning_examples/finetuning-scheduler.html) - [CLI-based Tutorial](https://
 finetuning-scheduler.readthedocs.io/en/stable/#example-scheduled-fine-tuning-
 for-superglue) - [FSDP Scheduled Fine-Tuning](https://finetuning-
 scheduler.readthedocs.io/en/stable/advanced/fsdp_scheduled_fine_tuning.html) -
 [LR Scheduler Reinitialization](https://finetuning-scheduler.readthedocs.io/en/
-stable/advanced/lr_scheduler_reinitialization.html) (advanced)
+stable/advanced/lr_scheduler_reinitialization.html) (advanced) - [Optimizer
+Reinitialization](https://finetuning-scheduler.readthedocs.io/en/stable/
+advanced/optimizer_reinitialization.html) (advanced)
 ______________________________________________________________________ ##
 Continuous Integration Fine-Tuning Scheduler is rigorously tested across
 multiple CPUs, GPUs and against major Python and PyTorch versions. Each Fine-
 Tuning Scheduler minor release (major.minor.patch) is paired with a Lightning
 minor release (e.g. Fine-Tuning Scheduler 2.0 depends upon Lightning 2.0). To
 ensure maximum stability, the latest Lightning patch release fully tested with
 Fine-Tuning Scheduler is set as a maximum dependency in Fine-Tuning Scheduler's
@@ -97,33 +99,33 @@
 -------------------------------------------------------------------------------
 -----------------------------------------------: | :---------------------------
 -------------------------------------------------------------------------------
 -------------------------------------------------------------------------------
 -----------------------------------------------------: | | Linux \[GPUs\*\*\] |
 - | [![Build Status](https://dev.azure.com//speediedan/finetuning-scheduler/
 _apis/build/status/Multi-
-GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.1)](https://
+GPU%20&%20Example%20Tests?branchName=refs%2Ftags%2F2.0.2)](https://
 dev.azure.com/speediedan/finetuning-scheduler/_build/
-latest?definitionId=2&branchName=refs%2Ftags%2F2.0.1) | | Linux (Ubuntu 20.04)
+latest?definitionId=2&branchName=refs%2Ftags%2F2.0.2) | | Linux (Ubuntu 20.04)
 | [![Test](https://github.com/speediedan/finetuning-scheduler/actions/
-workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/speediedan/
+workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/speediedan/
 finetuning-scheduler/actions/workflows/ci_test-full.yml) | [![Test](https://
 github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/
-badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/
+badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/
 actions/workflows/ci_test-full.yml) | | OSX (11) | [![Test](https://github.com/
 speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml/
-badge.svg?tag=2.0.1)](https://github.com/speediedan/finetuning-scheduler/
+badge.svg?tag=2.0.2)](https://github.com/speediedan/finetuning-scheduler/
 actions/workflows/ci_test-full.yml) | [![Test](https://github.com/speediedan/
-finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)]
+finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)]
 (https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-
 full.yml) | | Windows (2022) | [![Test](https://github.com/speediedan/
-finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)]
+finetuning-scheduler/actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)]
 (https://github.com/speediedan/finetuning-scheduler/actions/workflows/ci_test-
 full.yml) | [![Test](https://github.com/speediedan/finetuning-scheduler/
-actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.1)](https://github.com/
+actions/workflows/ci_test-full.yml/badge.svg?tag=2.0.2)](https://github.com/
 speediedan/finetuning-scheduler/actions/workflows/ci_test-full.yml) | - \*\*
 tests run on two RTX 2070s  ## Community Fine-Tuning Scheduler is developed and
 maintained by the community in close communication with the [Lightning team]
 (https://pytorch-lightning.readthedocs.io/en/stable/governance.html). Thanks to
 everyone in the community for their tireless effort building and improving the
 immensely useful core Lightning project. PR's welcome! Please see the
 [contributing guidelines](https://finetuning-scheduler.readthedocs.io/en/
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/SOURCES.txt` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/SOURCES.txt`

 * *Files 16% similar despite different names*

```diff
@@ -19,14 +19,15 @@
 requirements/test.txt
 src/finetuning_scheduler/__about__.py
 src/finetuning_scheduler/__init__.py
 src/finetuning_scheduler/fts.py
 src/finetuning_scheduler/fts_supporters.py
 src/finetuning_scheduler/py.typed
 src/finetuning_scheduler/setup_tools.py
+src/finetuning_scheduler/types.py
 src/finetuning_scheduler.egg-info/PKG-INFO
 src/finetuning_scheduler.egg-info/SOURCES.txt
 src/finetuning_scheduler.egg-info/dependency_links.txt
 src/finetuning_scheduler.egg-info/not-zip-safe
 src/finetuning_scheduler.egg-info/requires.txt
 src/finetuning_scheduler.egg-info/top_level.txt
 src/finetuning_scheduler/strategy_adapters/__init__.py
@@ -62,9 +63,13 @@
 src/fts_examples/stable/config/nofts_baseline.yaml
 src/fts_examples/stable/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml
 src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml
 src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml
 src/fts_examples/stable/config/advanced/reinit_lr/explicit_reinit_lr.yaml
 src/fts_examples/stable/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml
 src/fts_examples/stable/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml
+src/fts_examples/stable/config/advanced/reinit_optim_lr/explicit_reinit_optim_lr.yaml
+src/fts_examples/stable/config/advanced/reinit_optim_lr/fts_explicit_reinit_optim_lr.yaml
+src/fts_examples/stable/config/advanced/reinit_optim_lr/fts_implicit_reinit_optim_lr.yaml
+src/fts_examples/stable/config/advanced/reinit_optim_lr/fts_implicit_reinit_optim_lr_use_curr.yaml
 tests/test_finetuning_scheduler_callback.py
 tests/test_fsdp.py
```

### Comparing `finetuning-scheduler-2.0.1/src/finetuning_scheduler.egg-info/requires.txt` & `finetuning-scheduler-2.0.2/src/finetuning_scheduler.egg-info/requires.txt`

 * *Files 15% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 lightning<2.0.2,>=2.0.0
 torch>=1.11.0
 
 [all]
 rich!=10.15.0.a,>=10.14.0
-jsonargparse[signatures]<4.18.0,>=4.15.2
+jsonargparse[signatures]!=4.18.0,!=4.19.0,!=4.20.0,>=4.15.2
 omegaconf>=2.1.0
 hydra-core>=1.1.0
 coverage>=6.4
 codecov>=2.1
 pytest>=6.0
 pytest-rerunfailures>=10.2
 twine==3.2
@@ -22,21 +22,21 @@
 evaluate
 transformers>=4.18.0
 scikit-learn
 sentencepiece
 tensorboardX>=2.2
 
 [cli]
-jsonargparse[signatures]<4.18.0,>=4.15.2
+jsonargparse[signatures]!=4.18.0,!=4.19.0,!=4.20.0,>=4.15.2
 omegaconf>=2.1.0
 hydra-core>=1.1.0
 
 [dev]
 rich!=10.15.0.a,>=10.14.0
-jsonargparse[signatures]<4.18.0,>=4.15.2
+jsonargparse[signatures]!=4.18.0,!=4.19.0,!=4.20.0,>=4.15.2
 omegaconf>=2.1.0
 hydra-core>=1.1.0
 coverage>=6.4
 codecov>=2.1
 pytest>=6.0
 pytest-rerunfailures>=10.2
 twine==3.2
@@ -51,21 +51,21 @@
 [examples]
 datasets
 evaluate
 transformers>=4.18.0
 scikit-learn
 sentencepiece
 tensorboardX>=2.2
-jsonargparse[signatures]<4.18.0,>=4.15.2
+jsonargparse[signatures]!=4.18.0,!=4.19.0,!=4.20.0,>=4.15.2
 omegaconf>=2.1.0
 hydra-core>=1.1.0
 
 [extra]
 rich!=10.15.0.a,>=10.14.0
-jsonargparse[signatures]<4.18.0,>=4.15.2
+jsonargparse[signatures]!=4.18.0,!=4.19.0,!=4.20.0,>=4.15.2
 omegaconf>=2.1.0
 hydra-core>=1.1.0
 
 [ipynb]
 ipython[notebook]
 jupytext>=1.10
 nbval>=0.9.6
```

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/cli_experiment_utils.py` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/cli_experiment_utils.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/explicit_reinit_lr.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/explicit_reinit_lr.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/fts_defaults.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/fts_defaults.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/fts_explicit.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/fts_explicit.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/config/fts_implicit.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/config/fts_implicit.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/fts_fsdp_superglue.py` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/fts_fsdp_superglue.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/fts_superglue.py` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/fts_superglue.py`

 * *Files 2% similar despite different names*

```diff
@@ -279,15 +279,14 @@
         self.log("val_loss", val_loss, prog_bar=True, sync_dist=True)
         metric_dict = self.metric.compute(predictions=preds, references=labels)
         self.log_dict(metric_dict, prog_bar=True, sync_dist=True)
 
     def on_validation_epoch_end(self):
         self.validation_step_outputs.clear()
 
-    # TODO: remove this function for 2.0 example version once `enforce_p0_params` is leveraged in optim config
     def _init_param_groups(self) -> List[Dict]:
         """Initialize the parameter groups. Used to ensure weight_decay is not applied to our specified bias
         parameters when we initialize the optimizer.
 
         Returns:
             List[Dict]: A list of parameter group dictionaries.
         """
```

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/legacy/patched_adamw.py` & `finetuning-scheduler-2.0.2/src/fts_examples/legacy/patched_adamw.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/cli_experiment_utils.py` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/cli_experiment_utils.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/RteBoolqModule_ft_schedule_deberta_base_fsdp.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/fts_ddp_fsdp_baseline_profile.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_offload_profile.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/fsdp/fts_fsdp_awp_overrides_profile.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/explicit_reinit_lr.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/explicit_reinit_lr.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/fts_explicit_reinit_lr.yaml`

 * *Files 6% similar despite different names*

```diff
@@ -11,15 +11,15 @@
       frequency: 1
       name: Explicit_Reinit_LR_Scheduler
 trainer:
   callbacks:
   - class_path: lightning.pytorch.callbacks.LearningRateMonitor
   - class_path: finetuning_scheduler.FinetuningScheduler
     init_args:
-      ft_schedule: ./src/fts_examples/stable/config/advanced/reinit_lr/explicit_reinit_lr.yaml
+      ft_schedule: ./config/advanced/reinit_lr/explicit_reinit_lr.yaml
       max_depth: 2
       restore_best: false  # disable restore_best for lr pattern clarity
   - class_path: finetuning_scheduler.FTSCheckpoint
     init_args:
       save_top_k: 1
       monitor: val_loss
       verbose: true
```

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/advanced/reinit_lr/fts_implicit_reinit_lr.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/fts_defaults.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/fts_defaults.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/fts_explicit.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/fts_explicit.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/config/fts_implicit.yaml` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/config/fts_implicit.yaml`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/extended_profiler.py` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/extended_profiler.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/src/fts_examples/stable/fts_superglue.py` & `finetuning-scheduler-2.0.2/src/fts_examples/stable/fts_superglue.py`

 * *Files identical despite different names*

### Comparing `finetuning-scheduler-2.0.1/tests/test_finetuning_scheduler_callback.py` & `finetuning-scheduler-2.0.2/tests/test_finetuning_scheduler_callback.py`

 * *Files 18% similar despite different names*

```diff
@@ -18,14 +18,15 @@
 from typing import Any, Dict, List, Optional, Tuple
 
 import numpy as np
 import pytest
 import torch
 import torch.nn.functional as F
 import yaml
+from lightning.fabric.utilities import rank_zero_only
 from lightning.fabric.utilities.cloud_io import get_filesystem
 from lightning.pytorch import LightningModule, seed_everything, Trainer
 from lightning.pytorch.callbacks import Callback, EarlyStopping, LearningRateFinder, LearningRateMonitor
 from lightning.pytorch.strategies import StrategyRegistry
 from lightning.pytorch.strategies.single_device import SingleDeviceStrategy
 from lightning.pytorch.utilities.exceptions import MisconfigurationException
 from torch import nn, Tensor
@@ -42,14 +43,18 @@
 
 
 def get_fts(trainer: "Trainer") -> Callback:
     fts_resolver.connect_callback(trainer, reconnect=True)
     return fts_resolver.finetuningscheduler_callback
 
 
+def nones(num_n) -> Tuple:  # to help dedup config
+    return (None,) * num_n
+
+
 class AverageDataset(Dataset):
     def __init__(self, dataset_len=300, sequence_len=100):
         self.dataset_len = dataset_len
         self.sequence_len = sequence_len
         self.input_seq = torch.randn(dataset_len, sequence_len, 10)
         top, bottom = self.input_seq.chunk(2, -1)
         self.output_seq = top + bottom.roll(shifts=1, dims=-1)
@@ -228,23 +233,27 @@
     testing of scheduled finetuning."""
 
     def __init__(
         self,
         expected_state: Optional[Dict] = None,
         lrs_state: Optional[Dict] = None,
         mock_strategy: Optional[str] = None,
+        state_log_dir: Optional[str] = None,  # used to generate results from test config changes (w/o state assertions)
         *args,
         **kwargs,
     ):
         super().__init__(*args, **kwargs)
         self.expected_state = expected_state
         self.lrs_state = lrs_state
         self.mock_strategy = mock_strategy
+        self.state_log_dir = state_log_dir
         self.best_ckpt_test_weight = None
         self.restored_best_cnt = 0
+        self.dev_expected_states = {}
+        self.dev_lrs_states = {}
 
     def setup(self, trainer, pl_module, stage: Optional[str] = None) -> None:
         if self.mock_strategy:
             trainer._accelerator_connector._strategy_flag = MOCK_STRATEGY_MAPPING[self.mock_strategy][0]
             self.allow_untested = MOCK_STRATEGY_MAPPING[self.mock_strategy][1]
             self.custom_strategy_adapter = MOCK_STRATEGY_MAPPING[self.mock_strategy][2]
         super().setup(trainer, pl_module, stage)
@@ -277,30 +286,113 @@
             len(self._fts_state._fts_ckpt_metadata["best_ckpt_pgs"]),
             len(self._fts_state._curr_thawed_params),
             len(self._internal_optimizer_metadata[0]),
             trainer.checkpoint_callback.current_ckpt_depth,
             trainer.checkpoint_callback.best_ckpt_depth,
         )
         lrs_state = tuple(round(pg["lr"], 9) for pg in trainer.optimizers[0].param_groups)
-        if self.expected_state:
-            assert current_state == self.expected_state[state_key]
-        if self.lrs_state:
-            assert lrs_state == self.lrs_state[state_key]
+        self.inspect_or_assert(current_state, lrs_state, state_key)
+
+    def on_train_end(self, trainer, pl_module) -> None:
+        if self.state_log_dir:
+            self.log_dev_state()
+
+    def inspect_or_assert(self, current_state, lrs_state, state_key) -> None:
+        if not self.state_log_dir:
+            if self.expected_state:
+                # if the number of trainable params mod our world size is 0, the state should be the same on all ranks
+                assert current_state == self.expected_state[state_key]
+            if self.lrs_state:
+                assert lrs_state == self.lrs_state[state_key]
+        else:
+            self.dev_expected_states[state_key] = current_state
+            self.dev_lrs_states[state_key] = lrs_state
         if self.restore_best:
             assert self.restored_best_cnt == self.curr_depth
         else:
             assert self.restored_best_cnt == 0
 
+    @rank_zero_only
+    def log_dev_state(self) -> None:
+        dump_path = Path(self.state_log_dir)
+        state_log = dump_path / "dev_state_log.yaml"
+        fs = get_filesystem(state_log)
+        with fs.open(state_log, "w", newline="") as fp:
+            for dev_d in [self.dev_expected_states, self.dev_lrs_states]:
+                fp.write(os.linesep)
+                for k, v in dev_d.items():  # control formatting precisely to allow copy/paste expected output
+                    fp.write(f"{' ' * 8}{k}: {v},{os.linesep}")
+
 
 class FitStartOnlyFTS(TestFinetuningScheduler):
     def on_fit_start(self, trainer, pl_module) -> None:
         super().on_fit_start(trainer, pl_module)
         raise SystemExit()
 
 
+class OptInspectFTS(TestFinetuningScheduler):
+    def on_train_epoch_start(self, trainer, pl_module):
+        super(TestFinetuningScheduler, self).on_train_epoch_start(trainer, pl_module)
+        state_key = trainer.current_epoch
+        current_state = (
+            self.curr_depth,
+            self.depth_remaining,
+            self._fts_state._ft_epoch,
+            self._fts_state._fts_ckpt_metadata["current_ckpt_depth"],
+            self._fts_state._fts_ckpt_metadata["best_ckpt_depth"],
+            len(self._fts_state._fts_ckpt_metadata["best_ckpt_pgs"]),
+            len(self._fts_state._curr_thawed_params),
+            len(self._internal_optimizer_metadata[0]),
+            trainer.checkpoint_callback.current_ckpt_depth,
+            trainer.checkpoint_callback.best_ckpt_depth,
+            len(trainer.optimizers[0].param_groups),
+            tuple(len(pg["params"]) for pg in trainer.optimizers[0].param_groups),
+            trainer.optimizers[0].__class__.__name__,
+            trainer.fit_loop.epoch_loop.automatic_optimization.optim_progress.optimizer_steps,
+            trainer.optimizers[0].defaults["lr"],
+        )
+        lrs_state = tuple(round(pg["lr"], 9) for pg in trainer.optimizers[0].param_groups)
+        self.inspect_or_assert(current_state, lrs_state, state_key)
+
+    def on_train_end(self, trainer, pl_module) -> None:
+        assert self._fts_state._ft_sync_objects is not None
+        self.sync(self._fts_state._ft_sync_objects, self._fts_state._ft_sync_props)
+        assert self.depth_remaining == 0
+        assert self.curr_depth == 3
+        assert self.curr_depth == self.max_depth
+        if self.state_log_dir:
+            self.log_dev_state()
+
+
+class ZeroOptInspectFTS(OptInspectFTS):
+    def on_train_epoch_start(self, trainer, pl_module):
+        super(TestFinetuningScheduler, self).on_train_epoch_start(trainer, pl_module)
+        state_key = trainer.current_epoch
+        partition_cache = getattr(trainer.optimizers[0], "_partition_parameters_cache", None)
+        current_state = (
+            self.curr_depth,
+            self.depth_remaining,
+            self._fts_state._ft_epoch,
+            self._fts_state._fts_ckpt_metadata["current_ckpt_depth"],
+            self._fts_state._fts_ckpt_metadata["best_ckpt_depth"],
+            len(self._fts_state._fts_ckpt_metadata["best_ckpt_pgs"]),
+            len(self._fts_state._curr_thawed_params),
+            len(self._internal_optimizer_metadata[0]),
+            trainer.checkpoint_callback.current_ckpt_depth,
+            trainer.checkpoint_callback.best_ckpt_depth,
+            len(trainer.optimizers[0].param_groups),
+            tuple(len(pg["params"]) for pg in trainer.optimizers[0].param_groups),
+            len(trainer.optimizers[0]._all_params),
+            tuple(tuple(len(pg["params"]) for pg in pgs) for _, pgs in enumerate(partition_cache)),
+            tuple(len(pg["params"]) for pg in trainer.optimizers[0].optim.param_groups),
+        )
+        lrs_state = tuple(round(pg["lr"], 9) for pg in trainer.optimizers[0].param_groups)
+        self.inspect_or_assert(current_state, lrs_state, state_key)
+
+
 class MultiOptFTSBoringModel(FinetuningSchedulerBoringModel):
     def configure_optimizers(self):
         self.automatic_optimization = False
         parameters = list(filter(lambda x: x.requires_grad, self.parameters()))
         optimizer0 = torch.optim.SGD(parameters, lr=1e-3)
         optimizer1 = torch.optim.SGD(parameters, lr=1e-3)
         return [optimizer0, optimizer1]
@@ -326,22 +418,23 @@
             lr_scheduler = self.cust_init_lr(optimizer)
         else:
             lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.7)
         return [optimizer], [lr_scheduler]
 
 
 class FTSZeroRedundancyOptimizerModel(FinetuningSchedulerBoringModel):
-    def __init__(self, test_overlap: Optional[bool] = False, *args, **kwargs):
+    def __init__(self, test_overlap: Optional[bool] = False, enf_p0: Optional[bool] = False, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.test_overlap = test_overlap
+        self.enf_p0 = enf_p0
 
     def configure_optimizers(self):
-        parameters = list(filter(lambda x: x.requires_grad, self.parameters()))
+        params = list(filter(lambda x: x.requires_grad, self.parameters())) if not self.enf_p0 else self.parameters()
         optimizer = ZeroRedundancyOptimizer(
-            parameters, optimizer_class=torch.optim.Adam, lr=0.1, overlap_with_ddp=self.test_overlap
+            params, optimizer_class=torch.optim.AdamW, lr=0.1, overlap_with_ddp=self.test_overlap
         )
         lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.7)
         return [optimizer], [lr_scheduler]
 
 
 class NonDynamicLossBoringModel(FinetuningSchedulerBoringModel):
     def val_loss(self, batch, prediction):
@@ -391,15 +484,15 @@
 def ckpt_set(tmpdir_factory) -> Dict:
     """A fixture that generates a 'best' and 'kth' checkpoint to be used in scheduled fine-tuning resumption
     testing."""
     seed_everything(42)
     callbacks = [
         FinetuningScheduler(max_depth=1),
         FTSEarlyStopping(monitor="val_loss", patience=1, min_delta=0.001),
-        FTSCheckpoint(monitor="val_loss", verbose=True, save_top_k=3),
+        FTSCheckpoint(monitor="val_loss", verbose=True, save_top_k=2),
     ]
     model = FinetuningSchedulerBoringModel()
     trainer = Trainer(default_root_dir=tmpdir_factory.getbasetemp(), callbacks=callbacks, devices=1)
     trainer.fit(model)
     return {"best": trainer.checkpoint_callback.best_model_path, "kth": trainer.checkpoint_callback.kth_best_model_path}
 
 
@@ -413,26 +506,39 @@
     tmpdir = tmpdir_factory.getbasetemp()
     trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
     # unmod_schedule_file = tmpdir / "lightning_logs" / "version_0" / f"{model.__class__.__name__}_ft_schedule.yaml"]
     unmod_schedule_file = Path(trainer.log_dir) / f"{model.__class__.__name__}_ft_schedule.yaml"
     with pytest.raises(SystemExit):
         trainer.fit(model)
     mod_sched_dict = get_fts(trainer).load_yaml_schedule(unmod_schedule_file)
+    reinit_optim_sched_dict = deepcopy(mod_sched_dict)
     reinitlr_sched_dict = deepcopy(mod_sched_dict)
     lambdalr_sched_dict = deepcopy(mod_sched_dict)
     rlrop_sched_dict = deepcopy(mod_sched_dict)
     mod_sched_dict[0]["params"].extend(mod_sched_dict.pop(1)["params"])
     mod_sched_dict[0]["max_transition_epoch"] = 3
     mod_sched_dict[1] = mod_sched_dict.pop(2)
     mod_sched_dict[1]["lr"] = 1e-06
     mod_sched_dict[2] = mod_sched_dict.pop(3)
     mod_sched_dict[2]["params"] = ["layer.0.*"]
     epoch_only_sched = deepcopy(mod_sched_dict)
     epoch_only_sched[1]["max_transition_epoch"] = 2
     epoch_only_sched[2]["max_transition_epoch"] = 2
+    reinit_optim_sched_dict[1]["new_optimizer"] = {
+        "optimizer_init": {
+            "class_path": "torch.optim.Adam",
+            "init_args": {"lr": 2.1e-04},
+        },
+    }
+    reinit_optim_sched_dict[2]["new_optimizer"] = {
+        "optimizer_init": {
+            "class_path": "torch.optim.SGD",
+            "init_args": {"lr": 2.0e-03, "momentum": 0.9, "weight_decay": 2.0e-06},
+        }
+    }
     reinitlr_sched_dict[1]["new_lr_scheduler"] = {
         "lr_scheduler_init": {
             "class_path": "torch.optim.lr_scheduler.StepLR",
             "init_args": {"step_size": 1, "gamma": 0.7, "verbose": True},
         },
         "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
     }
@@ -441,14 +547,44 @@
         "lr_scheduler_init": {
             "class_path": "torch.optim.lr_scheduler.CosineAnnealingWarmRestarts",
             "init_args": {"T_0": 1, "T_mult": 2, "eta_min": 1.0e-07},
         },
         "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
         "init_pg_lrs": [1.0e-06, 2.0e-06],
     }
+    reinitlr_optim_sched_dict = deepcopy(reinitlr_sched_dict)
+    reinitlr_optim_sched_dict[1]["new_optimizer"] = deepcopy(reinit_optim_sched_dict[1]["new_optimizer"])
+    reinitlr_optim_sched_dict[2]["new_optimizer"] = deepcopy(reinit_optim_sched_dict[2]["new_optimizer"])
+    reinitlr_optim_sched_dict[2]["new_lr_scheduler"] = {
+        "lr_scheduler_init": {
+            "class_path": "torch.optim.lr_scheduler.StepLR",
+            "init_args": {"step_size": 1, "gamma": 0.2, "verbose": True},
+        },
+        "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
+    }
+    reinitlr_optim_use_curr_sched_dict = deepcopy(reinitlr_optim_sched_dict)
+    reinitlr_optim_use_curr_sched_dict[2]["new_lr_scheduler"]["use_current_optimizer_pg_lrs"] = True
+    reinitlr_optim_lambdalr_sched = deepcopy(reinitlr_optim_sched_dict)
+    reinitlr_optim_lambdalr_sched[1]["new_lr_scheduler"] = {
+        "lr_scheduler_init": {
+            "class_path": "tests.helpers.boring_model.LinearWarmupLR",
+            "init_args": {"num_warmup_steps": 100, "num_training_steps": 1000},
+        },
+        "pl_lrs_cfg": {"interval": "step", "frequency": 1, "name": "Custom_Reinit_LR"},
+    }
+    del reinitlr_optim_lambdalr_sched[2]["new_lr_scheduler"]
+    reinitlr_optim_rlrop_sched = deepcopy(reinitlr_optim_lambdalr_sched)
+    reinitlr_optim_rlrop_sched[1]["new_lr_scheduler"] = {
+        "lr_scheduler_init": {
+            "class_path": "torch.optim.lr_scheduler.ReduceLROnPlateau",
+            "init_args": {"patience": 1, "min_lr": [2.0e-07, 1.0e-07]},
+        },
+        "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "monitor": "val_loss", "name": "Custom_Reinit_LR"},
+        "init_pg_lrs": [1.5e-06],
+    }
     lambdalr_sched_dict[1]["new_lr_scheduler"] = {
         "lr_scheduler_init": {
             "class_path": "tests.helpers.boring_model.LinearWarmupLR",
             "init_args": {"num_warmup_steps": 100, "num_training_steps": 1000},
         },
         "pl_lrs_cfg": {"interval": "step", "frequency": 1, "name": "Custom_Reinit_LR"},
     }
@@ -484,14 +620,19 @@
     return (
         unmod_schedule_file,
         mod_sched_dict,
         epoch_only_sched,
         reinitlr_sched_dict,
         lambdalr_sched_dict,
         rlrop_sched_dict,
+        reinit_optim_sched_dict,
+        reinitlr_optim_sched_dict,
+        reinitlr_optim_lambdalr_sched,
+        reinitlr_optim_rlrop_sched,
+        reinitlr_optim_use_curr_sched_dict,
     )
 
 
 @pytest.fixture(scope="function")
 def invalid_schedules(tmpdir_factory) -> Dict:
     """A fixture that generates a dictionary of invalid schedules for testing."""
     valid_sched_start = """
@@ -619,14 +760,36 @@
   new_lr_scheduler:
     lr_scheduler_init:
       class_path: torch.optim.lr_scheduler.StepLR
       init_args:
         step_size: 1
         whoops: 0
 """
+    optim_init_fail = """
+1:
+  params:
+  - layer.1.bias
+  - layer.1.weight
+  new_optimizer:
+    optimizer_init:
+      class_path: torch.optim.Adam
+      init_args:
+        whoops: 0
+"""
+    unsupported_optim_reinit = """
+1:
+  params:
+  - layer.1.bias
+  - layer.1.weight
+  new_optimizer:
+    optimizer_init:
+      class_path: torch.distributed.optim.ZeroRedundancyOptimizer
+      init_args:
+        optimizer_class: torch.optim.AdamW
+"""
     extra_plrs_key = """
 1:
   params:
   - layer.1.bias
   - layer.1.weight
   new_lr_scheduler:
     lr_scheduler_init:
@@ -708,14 +871,16 @@
     invalid_sched["invalid_plrs"] = valid_sched_start + invalid_plrs_cfg
     invalid_sched["missing_lrs_init"] = valid_sched_start + missing_lrs_init
     invalid_sched["no_cpath"] = valid_sched_start + no_lrs_class_path
     invalid_sched["newlr_in0"] = newlrs_in_phase0
     invalid_sched["nonfl_lr_init"] = valid_sched_start + nonfloat_init_pg_lrs
     invalid_sched["imp_lrs_fail"] = valid_sched_start + lrs_import_fail
     invalid_sched["lrs_init_fail"] = valid_sched_start + lrs_init_fail
+    invalid_sched["optim_init_fail"] = valid_sched_start + optim_init_fail
+    invalid_sched["unsupported_optim_reinit"] = valid_sched_start + unsupported_optim_reinit
     invalid_sched["extra_plrs_key"] = valid_sched_start + extra_plrs_key
     invalid_sched["rlrop_missing_mon"] = valid_sched_start + rlrop_missing_mon
     invalid_sched["num_pg_w"] = valid_sched_start + num_pg_match
     invalid_sched["ext_opt_key"] = valid_sched_start + extra_optimizer_key
     invalid_sched["non_conv_int"] = valid_sched_start + non_integer_conv_phase + valid_sched_end
     invalid_sched["cflict_reinit"] = valid_sched_start + valid_depth1  # pass a valid schedule but conflicting fts arg
     invalid_sched["valid_nonint"] = valid_sched_start + valid_nonint  # pass a valid sched that needs silent conversion
@@ -868,52 +1033,59 @@
 ENFORCE_P0_LR_STATE = {
     "step_lr": {
         0: (0.001, 0.001),
         1: (0.0007, 0.0007),
         2: (0.00049, 0.00049),
         3: (0.000343, 0.000343),
         4: (0.0002401, 0.0002401),
-        5: (0.0002401, 0.0002401, 1e-05, 1e-05),
-        6: (0.0002401, 0.0002401, 1e-05, 1e-05, 1e-05, 1e-05),
+        5: (0.00016807, 0.00016807, 1e-05, 1e-05),
+        6: (0.000117649, 0.000117649, 7e-06, 7e-06, 1e-05, 1e-05),
     },
     "rlrop": {
         0: (0.001, 0.001),
         1: (0.001, 0.001),
         2: (0.001, 0.001),
         3: (0.001, 0.001),
         4: (0.001, 0.001),
         5: (0.001, 0.001, 1e-05, 1e-05),
         6: (0.001, 0.001, 1e-05, 1e-05, 1e-05, 1e-05),
     },
     # note we are testing before the initial lambda lr execution in epoch 0
     "lr_lambdas": {
-        0: (0.001, 0.001),
+        0: (0.0, 0.0),
         1: (0.000213333, 0.000213333),
         2: (0.000426667, 0.000426667),
         3: (0.00064, 0.00064),
         4: (0.000853333, 0.000853333),
-        5: (0.000853333, 0.000853333, 1e-05, 1e-05),
-        6: (0.000853333, 0.000853333, 1e-05, 1e-05, 1e-05, 1e-05),
+        5: (0.000971429, 0.000971429, 1e-05, 1e-05),
+        6: (0.00088, 0.00088, 8.8e-06, 8.8e-06, 1e-05, 1e-05),
     },
 }
 
 
 @pytest.mark.parametrize(
     "init_lr_key, p0_params",
-    [(None, ["layer.0.weight", "layer.0.bias"]), ("rlrop", None), ("lr_lambdas", None)],
+    [
+        pytest.param(None, ["layer.0.weight", "layer.0.bias"], marks=RunIf(min_torch="1.13")),
+        ("rlrop", None),
+        pytest.param("lr_lambdas", None, marks=RunIf(min_torch="1.13")),
+    ],
     ids=["step_lr", "rlrop", "lr_lambdas"],
 )
 def test_finetuningscheduling_enforce_p0(tmpdir, init_lr_key, p0_params):
     """Inspect the scheduled fine-tuning training path to ensure thawing schedule phase 0 is enforced."""
     seed_everything(42)
     model = EnforcePhase0CfgOptimBoringModel(no_decay=["bias"], init_lr_key=init_lr_key, p0_params=p0_params)
     init_lr_key = init_lr_key or "step_lr"
     callbacks = [
         TestFinetuningScheduler(
-            expected_state=ENFORCE_P0_INTRAFIT_STATE["default"], lrs_state=ENFORCE_P0_LR_STATE[init_lr_key], max_depth=2
+            expected_state=ENFORCE_P0_INTRAFIT_STATE["default"],
+            lrs_state=ENFORCE_P0_LR_STATE[init_lr_key],
+            max_depth=2,
+            # state_log_dir=tmpdir,
         ),
         FTSEarlyStopping(monitor="val_loss", patience=1),
         LearningRateMonitor(),
     ]
     trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
     trainer.fit(model)
     finetuningscheduler_callback = get_fts(trainer)
@@ -1245,97 +1417,390 @@
     assert (
         callbacks_dict[TestFinetuningScheduler]
         < callbacks_dict[LearningRateMonitor]
         < callbacks_dict[ExplicitLossFTSCheckpoint]
     )
 
 
+IMP_REINIT_OPTIM_CFG = {"optimizer_init": {"class_path": "torch.optim.Adam", "init_args": {"lr": 2.2e-04}}}
+
+
+IMP_REINIT_LR_OPTIM_CFG = {
+    "lr_scheduler_init": {
+        "class_path": "torch.optim.lr_scheduler.StepLR",
+        "init_args": {"step_size": 1, "gamma": 0.5, "verbose": True},
+    },
+    "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
+}
+IMP_REINIT_LR_OPTIM_USE_CURR_CFG = deepcopy(IMP_REINIT_LR_OPTIM_CFG)
+IMP_REINIT_LR_OPTIM_USE_CURR_CFG["use_current_optimizer_pg_lrs"] = True
+
+
+COMMON_LR_INIT_PATH = {
+    0: (0.001,),
+    1: (0.0007,),
+    2: (0.00049,),
+    3: (0.000343,),
+}
+COMMON_OPTIM_INIT_PATH = {
+    0: (0, 3, 0, 0, 0, 0, 2, 1, 0, 0, 1, (2,), "SGD", 0, 0.001),
+    1: (0, 3, 1, 0, 0, 1, 2, 1, 0, 0, 1, (2,), "SGD", 64, 0.001),
+    2: (0, 3, 2, 0, 0, 1, 2, 1, 0, 0, 1, (2,), "SGD", 128, 0.001),
+    3: (0, 3, 3, 0, 0, 1, 2, 1, 0, 0, 1, (2,), "SGD", 192, 0.001),
+}
+
+EXPECTED_REINIT_OPTIM_LR_STATE = {
+    (False, False, False): {
+        **COMMON_LR_INIT_PATH,
+        4: (0.00022, 1e-05),
+        5: (0.00011, 5e-06),
+        6: (0.00022, 1e-05, 1e-05),
+        7: (0.00011, 5e-06, 5e-06),
+        8: (0.00022, 1e-05, 1e-05, 1e-05),
+        9: (0.00011, 5e-06, 5e-06, 5e-06),
+    },
+    (True, False, False): {
+        **COMMON_LR_INIT_PATH,
+        4: (0.00021, 1e-05),
+        5: (0.000147, 7e-06),
+        6: (0.002, 1e-05, 3e-06),
+        7: (0.0004, 2e-06, 6e-07),
+        8: (8e-05, 4e-07, 1.2e-07, 1e-05),
+        9: (1.6e-05, 8e-08, 2.4e-08, 2e-06),
+    },
+    (True, True, False): {
+        **COMMON_LR_INIT_PATH,
+        4: (0.0002401, 1e-05),
+        5: (0.00016807, 7e-06),
+        6: (0.000117649, 4.9e-06, 1e-05),
+        7: (8.2354e-05, 3.43e-06, 7e-06),
+        8: (5.7648e-05, 2.401e-06, 4.9e-06, 1e-05),
+        9: (4.0354e-05, 1.681e-06, 3.43e-06, 7e-06),
+    },
+    (False, True, False): {
+        **COMMON_LR_INIT_PATH,
+        4: (0.0002401, 1e-05),
+        5: (0.00016807, 7e-06),
+        6: (0.000117649, 4.9e-06, 1e-05),
+        7: (8.2354e-05, 3.43e-06, 7e-06),
+        8: (5.7648e-05, 2.401e-06, 4.9e-06, 1e-05),
+        9: (4.0354e-05, 1.681e-06, 3.43e-06, 7e-06),
+    },
+    (True, False, True): {
+        **COMMON_LR_INIT_PATH,
+        4: (0.00021, 1e-05),
+        5: (0.000147, 7e-06),
+        6: (0.0001029, 4.9e-06, 3e-06),
+        7: (2.058e-05, 9.8e-07, 6e-07),
+        8: (4.116e-06, 1.96e-07, 1.2e-07, 1e-05),
+        9: (8.23e-07, 3.9e-08, 2.4e-08, 2e-06),
+    },
+    (False, False, True): {
+        **COMMON_LR_INIT_PATH,
+        4: (0.0002401, 1e-05),
+        5: (0.00012005, 5e-06),
+        6: (6.0025e-05, 2.5e-06, 1e-05),
+        7: (3.0012e-05, 1.25e-06, 5e-06),
+        8: (1.5006e-05, 6.25e-07, 2.5e-06, 1e-05),
+        9: (7.503e-06, 3.13e-07, 1.25e-06, 5e-06),
+    },
+}
+
+EXPECTED_REINIT_OPTIM_STATE = {
+    (False, False, False): {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00022),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00022),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "Adam", 384, 0.00022),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "Adam", 448, 0.00022),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "Adam", 512, 0.00022),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "Adam", 576, 0.00022),
+    },
+    (True, False, False): {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00021),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00021),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 384, 0.002),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 448, 0.002),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 512, 0.002),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 576, 0.002),
+    },
+    (True, True, False): {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00021),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00021),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 384, 0.002),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 448, 0.002),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 512, 0.002),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 576, 0.002),
+    },
+    (False, True, False): {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00022),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00022),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "Adam", 384, 0.00022),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "Adam", 448, 0.00022),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "Adam", 512, 0.00022),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "Adam", 576, 0.00022),
+    },
+    (True, False, True): {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00021),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00021),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 384, 0.002),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 448, 0.002),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 512, 0.002),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 576, 0.002),
+    },
+    (False, False, True): {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00022),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00022),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "Adam", 384, 0.00022),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "Adam", 448, 0.00022),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "Adam", 512, 0.00022),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "Adam", 576, 0.00022),
+    },
+}
+
+
+@pytest.mark.parametrize(
+    "explicit_mode, reinit_optim_only, use_curr_optim_pg",
+    [
+        pytest.param(True, True, False, id="explicit_optim"),
+        pytest.param(True, False, False, id="explicit_optimlr"),
+        pytest.param(False, True, False, id="implicit_optim"),
+        pytest.param(False, False, False, id="implicit_optimlr"),
+        pytest.param(True, False, True, id="explicit_optimlr_use_curr"),
+        pytest.param(False, False, True, id="implicit_optimlr_use_curr"),
+    ],
+)
+def test_finetuningscheduling_reinit_optim(
+    tmpdir, boring_ft_schedule, explicit_mode: bool, reinit_optim_only: bool, use_curr_optim_pg: bool
+):
+    """Inspect optimizer state within the training process to ensure it is taking the expected path in both
+    explicit and implict fine-tuning modes."""
+    seed_everything(42)
+    reinit_optim_cfg, reinit_lr_cfg = None, None
+    if explicit_mode:
+        if reinit_optim_only:
+            ft_schedule = boring_ft_schedule[6]
+        else:
+            ft_schedule = boring_ft_schedule[10] if use_curr_optim_pg else boring_ft_schedule[7]
+    else:  # implicit mode tests
+        reinit_optim_cfg = IMP_REINIT_OPTIM_CFG
+        if not reinit_optim_only:
+            reinit_lr_cfg = IMP_REINIT_LR_OPTIM_USE_CURR_CFG if use_curr_optim_pg else IMP_REINIT_LR_OPTIM_CFG
+        ft_schedule = None
+
+    model = FinetuningSchedulerBoringModel(diverge_on_epoch=1)
+    callbacks = [
+        OptInspectFTS(
+            expected_state=EXPECTED_REINIT_OPTIM_STATE[(explicit_mode, reinit_optim_only, use_curr_optim_pg)],
+            lrs_state=EXPECTED_REINIT_OPTIM_LR_STATE[(explicit_mode, reinit_optim_only, use_curr_optim_pg)],
+            reinit_optim_cfg=reinit_optim_cfg,
+            reinit_lr_cfg=reinit_lr_cfg,
+            ft_schedule=ft_schedule,
+            logging_level=DEBUG,
+            # state_log_dir=tmpdir,
+        ),
+        FTSEarlyStopping(monitor="val_loss", patience=2),
+    ]
+    trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
+    trainer.fit(model)
+    finetuningscheduler_callback = get_fts(trainer)
+    assert finetuningscheduler_callback.depth_remaining == 0
+    assert finetuningscheduler_callback.curr_depth == 3
+    assert finetuningscheduler_callback.curr_depth == finetuningscheduler_callback.max_depth
+
+
+EXPECTED_REINIT_OPTIM_LR_NODECAY_STATE = {
+    **COMMON_LR_INIT_PATH,
+    4: (0.00021, 0.00021, 1e-05, 1e-05),
+    5: (0.000147, 0.000147, 7e-06, 7e-06),
+    6: (0.002, 0.002, 1e-05, 1e-05, 3e-06, 3e-06),
+    7: (0.0004, 0.0004, 2e-06, 2e-06, 6e-07, 6e-07),
+    8: (8e-05, 8e-05, 4e-07, 4e-07, 1.2e-07, 1e-05, 1e-05),
+    9: (1.6e-05, 1.6e-05, 8e-08, 8e-08, 2.4e-08, 2e-06, 2e-06),
+}
+
+EXPECTED_REINIT_OPTIM_NODECAY_STATE = {
+    **COMMON_OPTIM_INIT_PATH,
+    4: (1, 2, 4, 0, 0, 1, 4, 4, 0, 0, 4, (1, 1, 1, 1), "Adam", 256, 0.00021),
+    5: (1, 2, 5, 0, 0, 1, 4, 4, 0, 0, 4, (1, 1, 1, 1), "Adam", 320, 0.00021),
+    6: (2, 1, 6, 0, 0, 1, 6, 6, 0, 0, 6, (1, 1, 1, 1, 1, 1), "SGD", 384, 0.002),
+    7: (2, 1, 7, 0, 0, 1, 6, 6, 0, 0, 6, (1, 1, 1, 1, 1, 1), "SGD", 448, 0.002),
+    8: (3, 0, 8, 0, 0, 1, 8, 7, 0, 0, 7, (2, 1, 1, 1, 1, 1, 1), "SGD", 512, 0.002),
+    9: (3, 0, 9, 0, 0, 1, 8, 7, 0, 0, 7, (2, 1, 1, 1, 1, 1, 1), "SGD", 576, 0.002),
+}
+
+
+def test_finetuningscheduling_reinit_optimlr_nodecay(tmpdir, boring_ft_schedule):
+    """Inspect optimizer state within the training process to ensure it is taking the expected path in both
+    explicit and implict fine-tuning modes."""
+    seed_everything(42)
+    no_decay = ["bias"]
+    ft_schedule = boring_ft_schedule[7]
+    model = FinetuningSchedulerBoringModel(diverge_on_epoch=1, no_decay=no_decay)
+    callbacks = [
+        OptInspectFTS(
+            expected_state=EXPECTED_REINIT_OPTIM_NODECAY_STATE,
+            lrs_state=EXPECTED_REINIT_OPTIM_LR_NODECAY_STATE,
+            ft_schedule=ft_schedule,
+            logging_level=DEBUG,
+            # state_log_dir=tmpdir,
+        ),
+        FTSEarlyStopping(monitor="val_loss", patience=2),
+    ]
+    trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
+    trainer.fit(model)
+    finetuningscheduler_callback = get_fts(trainer)
+    assert finetuningscheduler_callback.depth_remaining == 0
+    assert finetuningscheduler_callback.curr_depth == 3
+    assert finetuningscheduler_callback.curr_depth == finetuningscheduler_callback.max_depth
+
+
+EXPECTED_REINIT_OPTIM_SPEC_STATE = {
+    "reinit_optim_only_lambdalr": {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00021),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00021),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 384, 0.002),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 448, 0.002),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 512, 0.002),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 576, 0.002),
+    },
+    "reinit_optim_only_rlrop": {
+        **COMMON_OPTIM_INIT_PATH,
+        4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 256, 0.00021),
+        5: (1, 2, 5, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), "Adam", 320, 0.00021),
+        6: (2, 1, 6, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 384, 0.002),
+        7: (2, 1, 7, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), "SGD", 448, 0.002),
+        8: (3, 0, 8, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 512, 0.002),
+        9: (3, 0, 9, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), "SGD", 576, 0.002),
+    },
+}
+
+
+EXPECTED_REINIT_OPTIM_LR_SPEC_STATE = {
+    "reinit_optim_only_lambdalr": {
+        **COMMON_LR_INIT_PATH,
+        4: (0.0, 0.0),  # our lambdalr at step 0, base_lr set via optim `initial_lr`=0.00021 (for pg 0, 1e-05 for pg 1)
+        5: (0.0001344, 6.4e-06),  # after 64 steps out of 100 warmup, 0.64 the way to 0.00021 (for pg 0)
+        6: (0.000203467, 9.689e-06, 3e-06),  # after 128 steps, lambda lr returns 0.9688... of the base 0.00021
+        7: (0.000188533, 8.978e-06, 2.693e-06),  # after 192 steps, lambda lr returns 0.8977... of the base 0.00021
+        8: (0.0001736, 8.267e-06, 2.48e-06, 1e-05),  # after 256 steps proper lambda lr
+        9: (0.000158667, 7.556e-06, 2.267e-06, 7.556e-06),  # after 320 steps proper lambda lr
+    },
+    "reinit_optim_only_rlrop": {
+        **COMMON_LR_INIT_PATH,
+        4: (1.5e-06, 1e-05),
+        5: (1.5e-06, 1e-05),
+        6: (1.5e-06, 1e-05, 3e-06),
+        7: (2e-07, 1e-06, 3e-07),  # did not improve so lr reduced
+        8: (2e-07, 1e-06, 3e-07, 1e-05),
+        9: (2e-07, 1e-06, 3e-07, 1e-05),  # DID improve from best so lr is not reduced
+    },
+}
+
+
+@pytest.mark.parametrize(
+    "reinit_optim_lr_key, ft_sched_idx",
+    [
+        ("reinit_optim_only_lambdalr", 8),
+        ("reinit_optim_only_rlrop", 9),
+    ],
+    ids=["reinit_optim_only_lambdalr", "reinit_optim_only_rlrop"],
+)
+def test_finetuningscheduling_reinit_optim_special_lr(tmpdir, boring_ft_schedule, reinit_optim_lr_key, ft_sched_idx):
+    """Inspect optimizer state within the training process to ensure it is taking the expected path in both
+    explicit and implict fine-tuning modes."""
+    seed_everything(42)
+    ft_schedule = boring_ft_schedule[ft_sched_idx]
+
+    model = FinetuningSchedulerBoringModel(diverge_on_epoch=1)
+    callbacks = [
+        OptInspectFTS(
+            expected_state=EXPECTED_REINIT_OPTIM_SPEC_STATE[reinit_optim_lr_key],
+            lrs_state=EXPECTED_REINIT_OPTIM_LR_SPEC_STATE[reinit_optim_lr_key],
+            ft_schedule=ft_schedule,
+            logging_level=DEBUG,
+            # state_log_dir=tmpdir,
+        ),
+        FTSEarlyStopping(monitor="val_loss", patience=2),
+    ]
+    trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
+    trainer.fit(model)
+    finetuningscheduler_callback = get_fts(trainer)
+    assert finetuningscheduler_callback.depth_remaining == 0
+    assert finetuningscheduler_callback.curr_depth == 3
+    assert finetuningscheduler_callback.curr_depth == finetuningscheduler_callback.max_depth
+
+
 IMP_REINIT_LR_CFG = {
     "lr_scheduler_init": {
         "class_path": "torch.optim.lr_scheduler.StepLR",
         "init_args": {"step_size": 1, "gamma": 0.7, "verbose": True},
     },
     "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
 }
 
 
 EXPECTED_LR_STATE = {
-    (False, False): {
-        "max_depth": 3,
-        0: (0.001,),
-        1: (0.0007,),
-        2: (0.00049,),
-        3: (0.000343,),
-        4: (0.0002401,),
-        5: (0.0002401, 1e-05),
-        6: (0.0002401, 1e-05, 1e-05),
-        7: (0.0002401, 1e-05, 1e-05, 1e-05),
-    },
-    (True, False): {
-        "max_depth": 2,
-        0: (0.001,),
-        1: (0.0007,),
-        2: (0.00049,),
-        3: (0.000343, 1e-06),
-        4: (0.0002401, 7e-07),
-        5: (0.0002401, 7e-07, 1e-05),
-    },
-    (True, True): {
+    (True): {
         "max_depth": 3,
         0: (0.001,),
         1: (0.0007,),
         2: (0.00049,),
         3: (0.000343,),
         4: (0.0002401,),
         5: (0.001, 1e-05),
         6: (1e-06, 2e-06, 3e-06),
         7: (1e-06, 2e-06, 3e-06, 1e-05),
     },
-    (False, True): {
+    (False): {
         "max_depth": 3,
         0: (0.001,),
         1: (0.0007,),
         2: (0.00049,),
         3: (0.000343,),
         4: (0.0002401,),
         5: (0.001, 1e-05),
         6: (0.001, 1e-05, 1e-05),
         7: (0.001, 1e-05, 1e-05, 1e-05),
     },
 }
 
 
-@pytest.mark.parametrize("reinit_lr", [True, False], ids=["reinit_lr", "default"])
 @pytest.mark.parametrize("explicit_mode", [True, False], ids=["explicit", "implicit"])
-def test_finetuningscheduling_reinitlr(tmpdir, boring_ft_schedule, explicit_mode: bool, reinit_lr: bool):
+def test_finetuningscheduling_reinitlr(tmpdir, boring_ft_schedule, explicit_mode: bool):
     """Inspect learning rate scheduler state within the training process to ensure it is taking the expected path
     in both explicit and implict fine-tuning modes."""
     seed_everything(42)
-    reinit_lr_cfg = None
+    reinit_lr_cfg, ft_schedule = None, None
     if explicit_mode:
-        ft_schedule = boring_ft_schedule[3] if reinit_lr else boring_ft_schedule[1]
+        ft_schedule = boring_ft_schedule[3]
     else:
-        if reinit_lr:
-            reinit_lr_cfg = IMP_REINIT_LR_CFG
-        ft_schedule = None
+        reinit_lr_cfg = IMP_REINIT_LR_CFG
 
     model = FinetuningSchedulerBoringModel()
     callbacks = [
         TestFinetuningScheduler(
-            lrs_state=EXPECTED_LR_STATE[(explicit_mode, reinit_lr)],
+            lrs_state=EXPECTED_LR_STATE[(explicit_mode)],
             reinit_lr_cfg=reinit_lr_cfg,
             ft_schedule=ft_schedule,
+            # state_log_dir=tmpdir,
         ),
         FTSEarlyStopping(monitor="val_loss", patience=1),
     ]
     trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
     trainer.fit(model)
     finetuningscheduler_callback = get_fts(trainer)
     assert finetuningscheduler_callback.depth_remaining == 0
-    assert finetuningscheduler_callback.curr_depth == EXPECTED_LR_STATE[(explicit_mode, reinit_lr)]["max_depth"]
+    assert finetuningscheduler_callback.curr_depth == EXPECTED_LR_STATE[(explicit_mode)]["max_depth"]
     assert finetuningscheduler_callback.curr_depth == finetuningscheduler_callback.max_depth
 
 
 IMP_REINIT_LAMBDALR_CFG = {
     "lr_scheduler_init": {
         "class_path": "tests.helpers.boring_model.LinearWarmupLR",
         "init_args": {"num_warmup_steps": 100, "num_training_steps": 1000},
@@ -1350,26 +1815,26 @@
         0: (0.001,),
         1: (0.0007,),
         2: (0.00049,),
         3: (0.000343,),
         4: (0.0002401,),
         5: (0.0, 0.0),
         6: (0.0, 0.0, 0.0),
-        7: (0.0, 0.0, 0.0, 0.0),
+        7: (6.4e-07, 1.28e-06, 1.229e-06, 6.4e-06),
     },
     (True, False): {
         "max_depth": 3,
         0: (0.001,),
         1: (0.0007,),
         2: (0.00049,),
         3: (0.000343,),
         4: (0.0002401,),
         5: (0.0, 0.0),
         6: (0.0, 0.0, 0.0),
-        7: (0.0, 0.0, 0.0, 1e-05),
+        7: (6.4e-07, 1.28e-06, 1.92e-06, 1e-05),
     },
     (False, False): {
         "max_depth": 3,
         0: (0.001,),
         1: (0.0007,),
         2: (0.00049,),
         3: (0.000343,),
@@ -1380,16 +1845,16 @@
     },
 }
 
 
 @pytest.mark.parametrize(
     "explicit_mode, lam_mode, w_expected",
     [
-        (True, True, ("incompatible checkpoint detected",)),
-        (True, False, ("incompatible checkpoint detected", "this phase has lr_lambdas")),
+        (True, True, ("Incompatible checkpoint detected",)),
+        (True, False, ("Incompatible checkpoint detected", "this phase has lr_lambdas")),
         (False, False, None),
     ],
     ids=["explicit_extend_lams", "explicit_nonew_lams", "imp_lamlr"],
 )
 def test_finetuningscheduling_reinitlr_lambda(
     tmpdir, recwarn, boring_ft_schedule, explicit_mode: bool, lam_mode: bool, w_expected
 ):
@@ -1407,14 +1872,15 @@
     model = FinetuningSchedulerBoringModel()
     callbacks = [
         TestFinetuningScheduler(
             lrs_state=EXPECTED_LAMBDALR_STATE[(explicit_mode, lam_mode)],
             reinit_lr_cfg=reinit_lr_cfg,
             ft_schedule=ft_schedule,
             apply_lambdas_new_pgs=lam_mode,
+            # state_log_dir=tmpdir,
         ),
         FTSEarlyStopping(monitor="val_loss", patience=1),
     ]
     trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1)
     trainer.fit(model)
     finetuningscheduler_callback = get_fts(trainer)
     assert finetuningscheduler_callback.depth_remaining == 0
@@ -1451,22 +1917,22 @@
         0: (0.001,),
         1: (0.001,),
         2: (0.001,),
         3: (0.001,),
         4: (0.001,),
         5: (0.001,),
         6: (0.0001,),
-        7: (0.001, 1e-05),
-        8: (0.001, 1e-05),
-        9: (0.001, 1e-05),
-        10: (0.0001, 1e-06),
-        11: (0.001, 1e-05, 1e-05),
-        12: (0.001, 1e-05, 1e-05),
-        13: (0.001, 1e-05, 1e-05),
-        14: (0.0001, 1e-06, 1e-06),
+        7: (0.0001, 1e-05),
+        8: (0.0001, 1e-05),
+        9: (0.0001, 1e-05),
+        10: (1e-05, 1e-06),
+        11: (1e-05, 1e-05, 1e-05),
+        12: (1e-05, 1e-05, 1e-05),
+        13: (1e-05, 1e-05, 1e-05),
+        14: (1e-06, 1e-06, 1e-06),
     },
 }
 
 
 @pytest.mark.parametrize(
     "explicit_mode, es_patience, init_lr_key, max_epochs, w_expected",
     [
@@ -1499,14 +1965,15 @@
     model = FinetuningSchedulerBoringModel(diverge_on_epoch=2, init_lr_key=init_lr_key)
     callbacks = [
         TestFinetuningScheduler(
             lrs_state=EXPECTED_RLROP_STATE[(explicit_mode,)],
             reinit_lr_cfg=reinit_lr_cfg,
             ft_schedule=ft_schedule,
             max_depth=2,
+            # state_log_dir=tmpdir,
         ),
         FTSEarlyStopping(monitor="val_loss", patience=es_patience),
     ]
     trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, devices=1, max_epochs=max_epochs)
     trainer.fit(model)
     finetuningscheduler_callback = get_fts(trainer)
     assert finetuningscheduler_callback.depth_remaining == 0
@@ -1709,19 +2176,21 @@
         ("dup_key", ("Duplicate key", None)),
         ("lr_phase0", ("A lr for fine-tuning phase 0", None)),
         ("invalid_lr", ("convertable to a float", None)),
         ("unsupp_rlrs", ("provided lr scheduler", None)),
         ("invalid_plrs", ("key in lr scheduler dict must be", None)),
         ("missing_lrs_init", ("configuration to reinitialize with requires", None)),
         ("no_cpath", ("`lr_scheduler_init` requires at least a  `class_", None)),
-        ("newlr_in0", ("specified a `new_lr_scheduler` for the initial", None)),
+        ("newlr_in0", ("reinitialization directive for the initial", None)),
         ("nonfl_lr_init", ("Not all of the lrs specified", None)),
-        ("imp_lrs_fail", ("Could not import specified LR scheduler", None)),
+        ("imp_lrs_fail", ("Could not import specified reinitialization", None)),
         ("lrs_init_fail", ("Could not configure the specified LR scheduler", None)),
+        ("optim_init_fail", ("Could not configure the specified optimizer", None)),
         ("cflict_reinit", ("Specifying both `ft_schedule` and `reinit_lr_cfg` is an invalid", None)),
+        ("unsupported_optim_reinit", ("context of optimizer reinitialization", None)),
         ("valid_nonint", (None, None)),
         ("extra_plrs_key", ("Found unsupported keys in the lr scheduler dict", None)),
         ("rlrop_missing_mon", ("must include a monitor", None)),
         ("num_pg_w", ("ensure the number of specified parameter groups matches", None)),
         ("ext_opt_key", ("the existing optimizer and all associated parameter", None)),
         ("non_integer", ("had non-integer keys", None)),
         ("non_conv_int", ("not convertible to", None)),
@@ -1737,15 +2206,17 @@
         "invalid_plrs",
         "missing_lrs_init",
         "no_cpath",
         "newlr_in0",
         "nonfl_lr_init",
         "imp_lrs_fail",
         "lrs_init_fail",
+        "optim_init_fail",
         "cflict_reinit",
+        "unsupported_optim_reinit",
         "valid_nonint",
         "extra_plrs_key",
         "rlrop_missing_mon",
         "num_pg_w",
         "ext_opt_key",
         "non_int",
         "non_conv_int",
@@ -1949,60 +2420,34 @@
     3: (0, 3, 3, 0, 0, 1, 2, 1, 0, 0, 1, (2,), 2, ((1,), (1,)), (1,)),
     4: (1, 2, 4, 0, 0, 1, 4, 2, 0, 0, 2, (2, 2), 2, ((1, 1), (1, 1)), (1, 1)),
     5: (2, 1, 5, 0, 0, 1, 6, 3, 0, 0, 3, (2, 2, 2), 2, ((1, 1, 1), (1, 1, 1)), (1, 1, 1)),
     6: (3, 0, 6, 0, 0, 1, 8, 4, 0, 0, 4, (2, 2, 2, 2), 2, ((1, 1, 1, 1), (1, 1, 1, 1)), (1, 1, 1, 1)),
 }
 
 
-class OptInspectFTS(TestFinetuningScheduler):
-    def on_train_epoch_start(self, trainer, pl_module):
-        super(TestFinetuningScheduler, self).on_train_epoch_start(trainer, pl_module)
-        state_key = trainer.current_epoch
-        partition_cache = trainer.optimizers[0]._partition_parameters_cache
-        current_state = (
-            self.curr_depth,
-            self.depth_remaining,
-            self._fts_state._ft_epoch,
-            self._fts_state._fts_ckpt_metadata["current_ckpt_depth"],
-            self._fts_state._fts_ckpt_metadata["best_ckpt_depth"],
-            len(self._fts_state._fts_ckpt_metadata["best_ckpt_pgs"]),
-            len(self._fts_state._curr_thawed_params),
-            len(self._internal_optimizer_metadata[0]),
-            trainer.checkpoint_callback.current_ckpt_depth,
-            trainer.checkpoint_callback.best_ckpt_depth,
-            len(trainer.optimizers[0].param_groups),
-            tuple(len(pg["params"]) for pg in trainer.optimizers[0].param_groups),
-            len(trainer.optimizers[0]._all_params),
-            tuple(tuple(len(pg["params"]) for pg in pgs) for _, pgs in enumerate(partition_cache)),
-            tuple(len(pg["params"]) for pg in trainer.optimizers[0].optim.param_groups),
-        )
-        if self.expected_state:
-            # given the number of trainable params mod our world size is 0, the state should be the same on all ranks
-            assert current_state == self.expected_state[state_key]
-
-    def on_train_end(self, trainer, pl_module) -> None:
-        super(TestFinetuningScheduler, self).on_train_end(trainer, pl_module)
-        assert self._fts_state._ft_sync_objects is not None
-        self.sync(self._fts_state._ft_sync_objects, self._fts_state._ft_sync_props)
-        assert self.depth_remaining == 0
-        assert self.curr_depth == 3
-        assert self.curr_depth == self.max_depth
-
-
 @RunIf(min_cuda_gpus=2, skip_windows=True)
-@pytest.mark.parametrize("strategy", (pytest.param("ddp", marks=RunIf(standalone=True)), "ddp_spawn"))
-def test_fts_zero_opt_support(monkeypatch, tmpdir, strategy):
+@pytest.mark.parametrize(
+    "strategy, enf_p0",
+    [
+        pytest.param("ddp", None, marks=RunIf(standalone=True)),
+        ("ddp_spawn", None),
+        pytest.param("ddp", True, marks=RunIf(standalone=True)),
+    ],
+    ids=["ddp_noenfp0", "spawn_noenfp0", "ddp_enfp0"],
+)
+def test_fts_zero_opt_support(monkeypatch, tmpdir, strategy, enf_p0):
     """Inspect scheduled fine-tuning state within the training process to ensure it is taking the expected path in
     both restore_best modes."""
     monkeypatch.setenv("MKL_THREADING_LAYER", "GNU")
     seed_everything(42)
-
-    model = FTSZeroRedundancyOptimizerModel()
+    model = FTSZeroRedundancyOptimizerModel(enf_p0=enf_p0)
     callbacks = [
-        OptInspectFTS(expected_state=EXPECTED_OPTIMIZER_STATE),
+        ZeroOptInspectFTS(
+            expected_state=EXPECTED_OPTIMIZER_STATE,
+        ),
         FTSEarlyStopping(monitor="val_loss", patience=1),
     ]
     trainer = Trainer(default_root_dir=tmpdir, callbacks=callbacks, accelerator="gpu", devices=2, strategy=strategy)
     trainer.fit(model)
 
 
 @pytest.mark.parametrize(
```

### Comparing `finetuning-scheduler-2.0.1/tests/test_fsdp.py` & `finetuning-scheduler-2.0.2/tests/test_fsdp.py`

 * *Files 6% similar despite different names*

```diff
@@ -30,14 +30,15 @@
 from tests.helpers.boring_model import RandomDataset, unexpected_warns, unmatched_warns
 from tests.helpers.runif import RunIf
 from tests.test_finetuning_scheduler_callback import (
     EXPECTED_WARNS,
     ExplicitLossFTSCheckpoint,
     FinetuningSchedulerBoringModel,
     get_fts,
+    nones,
     TestFinetuningScheduler,
 )
 
 _distributed_available = torch.distributed.is_available()
 _min_fsdp_available = _TORCH_GREATER_EQUAL_1_13 and _distributed_available
 
 if _min_fsdp_available:
@@ -106,14 +107,54 @@
     fsdp_sched_dict = deepcopy(mod_sched_dict)
     fsdp_sched_dict[0]["params"] = ["layer.(4|2).*"]
     fsdp_gen_sched_dict = deepcopy(fsdp_sched_dict)
     fsdp_gen_sched_dict[0]["params"] = ["layer.(7|5).*"]
     fsdp_gen_sched_dict[0]["max_transition_epoch"] = 1
     fsdp_gen_sched_dict[1]["params"] = ["layer.[1-4].*"]
     fsdp_gen_sched_dict[1]["max_transition_epoch"] = 2
+    fsdp_reinit_optim_sched_dict = deepcopy(fsdp_gen_sched_dict)
+    fsdp_reinitlr_sched_dict = deepcopy(fsdp_gen_sched_dict)
+    fsdp_reinit_optim_sched_dict[1]["new_optimizer"] = {
+        "optimizer_init": {
+            "class_path": "torch.optim.Adam",
+            "init_args": {"lr": 2.1e-04},
+        },
+    }
+    fsdp_reinit_optim_sched_dict[2]["new_optimizer"] = {
+        "optimizer_init": {
+            "class_path": "torch.optim.SGD",
+            "init_args": {"lr": 2.0e-03, "momentum": 0.9, "weight_decay": 2.0e-06},
+        }
+    }
+    fsdp_reinitlr_sched_dict[1]["new_lr_scheduler"] = {
+        "lr_scheduler_init": {
+            "class_path": "torch.optim.lr_scheduler.StepLR",
+            "init_args": {"step_size": 1, "gamma": 0.7, "verbose": True},
+        },
+        "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
+    }
+    fsdp_reinitlr_sched_dict[2]["lr"] = 3.0e-06
+    fsdp_reinitlr_sched_dict[2]["new_lr_scheduler"] = {
+        "lr_scheduler_init": {
+            "class_path": "torch.optim.lr_scheduler.CosineAnnealingWarmRestarts",
+            "init_args": {"T_0": 1, "T_mult": 2, "eta_min": 1.0e-07},
+        },
+        "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
+        "init_pg_lrs": [1.0e-06, 2.0e-06],
+    }
+    fsdp_reinitlr_optim_sched_dict = deepcopy(fsdp_reinitlr_sched_dict)
+    fsdp_reinitlr_optim_sched_dict[1]["new_optimizer"] = deepcopy(fsdp_reinit_optim_sched_dict[1]["new_optimizer"])
+    fsdp_reinitlr_optim_sched_dict[2]["new_optimizer"] = deepcopy(fsdp_reinit_optim_sched_dict[2]["new_optimizer"])
+    fsdp_reinitlr_optim_sched_dict[2]["new_lr_scheduler"] = {
+        "lr_scheduler_init": {
+            "class_path": "torch.optim.lr_scheduler.StepLR",
+            "init_args": {"step_size": 1, "gamma": 0.2, "verbose": True},
+        },
+        "pl_lrs_cfg": {"interval": "epoch", "frequency": 1, "name": "Custom_Reinit_LR"},
+    }
     fsdp_bn_gen_sched_dict = deepcopy(fsdp_gen_sched_dict)
     fsdp_bn_gen_sched_dict[0]["params"] = ["layer.(8|[4-6]).*"]
     fsdp_bn_gen_sched_dict[1]["params"] = ["layer.[1-3].*"]
     fsdp_shared_param_sched_dict = deepcopy(fsdp_gen_sched_dict)
     fsdp_shared_param_sched_dict[0]["params"] = ["layer.(7|4).*", "layer.5.weight", "layer.5.bias"]
     fsdp_shared_param_sched_dict[1]["params"] = ["layer.2.*", "layer.3.weight", "layer.3.bias"]
     fsdp_shared_param_sched_dict[2]["params"] = ["layer.[0-1].*"]
@@ -137,14 +178,15 @@
         fsdp_nondis_mod_sched_dict,
         fsdp_bn_gen_sched_dict,
         fsdp_shared_param_sched_dict,
         fsdp_adam_gen_sched_dict,
         fsdp_nondis_mod_ex_sched_dict,
         fsdp_ext_gen_sched_dict,
         fsdp_epoch_only_sched,
+        fsdp_reinitlr_optim_sched_dict,
     )
 
 
 @pytest.fixture(scope="function")
 def fsdp_ckpt(tmpdir_factory, fsdp_ft_schedules) -> Dict:
     """A fixture that generates a checkpoint with a sharded model."""
     seed_everything(42)
@@ -407,24 +449,40 @@
 
 class FSDPTestFinetuningScheduler(TestFinetuningScheduler):
     def state_dict(self) -> Dict[str, Any]:
         return super(TestFinetuningScheduler, self).state_dict()
 
     def restore_best_ckpt(self) -> None:
         super(TestFinetuningScheduler, self).restore_best_ckpt()
+        self.restored_best_cnt += 1
 
     def on_train_epoch_start(self, trainer, pl_module):
         super(TestFinetuningScheduler, self).on_train_epoch_start(trainer, pl_module)
         state_key = trainer.current_epoch
         current_state = (
             len(self._fts_state._curr_thawed_params),
             len(self.strategy_adapter.logical_param_translation(self._fts_state._curr_thawed_params)),
         )
-        if self.expected_state:
-            assert current_state == self.expected_state[state_key]
+        lrs_state = tuple(round(pg["lr"], 9) for pg in trainer.optimizers[0].param_groups)
+        self.inspect_or_assert(current_state, lrs_state, state_key)
+
+
+class FSDPOptInspectFTS(FSDPTestFinetuningScheduler):
+    def on_train_epoch_start(self, trainer, pl_module):
+        super(TestFinetuningScheduler, self).on_train_epoch_start(trainer, pl_module)
+        state_key = trainer.current_epoch
+        current_state = (
+            len(self._fts_state._curr_thawed_params),
+            len(self.strategy_adapter.logical_param_translation(self._fts_state._curr_thawed_params)),
+            trainer.optimizers[0].__class__.__name__,
+            trainer.fit_loop.epoch_loop.automatic_optimization.optim_progress.optimizer_steps,
+            trainer.optimizers[0].defaults["lr"],
+        )
+        lrs_state = tuple(round(pg["lr"], 9) for pg in trainer.optimizers[0].param_groups)
+        self.inspect_or_assert(current_state, lrs_state, state_key)
 
 
 # model aliases
 base_model = FTSBaseFSDPModel
 nond_loss_adam_model = NonDynamicLossAdamFSDPModel
 cust_model = FTSCsmFSDPModel
 wrapped_model = AlreadyWrappedFSDPModel
@@ -512,66 +570,66 @@
 }
 test_use_orig = {"use_orig_params": True}
 
 # trainer configuration alias
 max_epoch_5 = {"max_epochs": 5}
 max_epoch_4 = {"max_epochs": 4}
 
-# fts config alias
+# fts config aliases
 epoch_t_only = {
     "epoch_transitions_only": True,
     "test_es": "disable",
     "test_ckpt": ExplicitLossFTSCheckpoint(monitor="val_loss", verbose=True),
 }
+opt_inspect = {"test_fts": FSDPOptInspectFTS}
 
 # expected training path aliases
 path_default = {0: (2, 4), 1: (6, 12), 2: (7, 14)}
 path_default_orig = {0: (4, 4), 1: (12, 12), 2: (14, 14)}
 path_default_orig_eo_dyn = {0: (4, 4), 1: (12, 12), 2: (14, 14), 3: (14, 14)}
 path_ignore_p_uo = {0: (4, 4), 1: (12, 12), 2: (14, 14)}
 path_8_14 = {0: (2, 4), 1: (7, 12), 2: (8, 14)}
 path_8_16 = {0: (4, 8), 1: (7, 14), 2: (8, 16)}
 path_5_10 = {0: (2, 4), 1: (3, 6), 2: (5, 10)}
 path_ext_7_14 = {0: (2, 4), 1: (2, 4), 2: (6, 12), 3: (6, 12), 4: (7, 14)}
 path_ext_8_16 = {0: (3, 6), 1: (7, 14), 2: (8, 16)}
-
-
-# to help dedup config
-def nones(num_n) -> Tuple:
-    return (None,) * num_n
+path_optimlr_reinit = {0: (2, 4, "SGD", 0, 0.1), 1: (6, 12, "Adam", 32, 0.00021), 2: (7, 14, "SGD", 64, 0.002)}
+lrs_path_default = {0: (0.1,), 1: (0.07, 1e-06), 2: (0.049, 7e-07, 1e-05)}
+lrs_path_optimlr_reinit = {0: (0.1,), 1: (0.00021, 1e-06), 2: (0.002, 1e-06, 3e-06)}
 
 
 EXPECTED_FSDP_FTS_RESULTS = {
-    "cust_awp_noprec": (path_default, *nones(2)),
-    "cust_awp_noprec_use_orig": (path_default_orig, *nones(2)),
-    "cust_awp_noprec_dynamo_use_orig": (path_default_orig_eo_dyn, *nones(2)),
-    "cust_awp_mwp_parity": (path_default, *nones(2)),
-    "override_csm_noprec": (path_default, *nones(2)),
+    "cust_awp_noprec": (path_default, *nones(3)),
+    "cust_awp_noprec_use_orig": (path_default_orig, *nones(3)),
+    "cust_awp_noprec_dynamo_use_orig": (path_default_orig_eo_dyn, *nones(3)),
+    "cust_awp_mwp_reinitlr_optim": (path_optimlr_reinit, ("Incompatible check",), None, lrs_path_optimlr_reinit),
+    "cust_awp_mwp_parity": (path_default, *nones(3)),
+    "override_csm_noprec": (path_default, *nones(3)),
     # TODO: once PyTorch deprecates ``ignored_modules``, check for that deprecation warning in this test
-    "cust_awp_nop_ignore_m_no_ofld": (path_8_14, *nones(2)),
-    "cust_awp_nop_ignore_p_no_ofld_uo": (path_ignore_p_uo, *nones(2)),
-    "unsupp_torch_version": ({}, None, "is supported from PyTorch"),
-    "non_disjoint_phase_fsdp_params": ({}, None, "do not have disjoint FSDP-flattened parameter"),
-    "non_disjoint_phase_mods": ({}, None, "not have disjoint"),
-    "non_disjoint_excluded_ft_params": ({}, None, "parameters not included in"),
-    "already_fsdp_wrapped": ({}, None, "already wrapped by FSDP"),
-    "no_fsdp_params_p0": ({}, None, "one or more FSDP"),
-    "warn_unsupp_nodecay": ({}, "will now be unset", None),
-    "unmatched_awp_overrides": ({}, None, "did not match any named modules"),
-    "cust_awp_prec": (path_default, *nones(2)),
-    "cust_awp_prec_pt1x": (path_default, *nones(2)),
-    "enforceP0_cust_awp_prec": (path_default, *nones(2)),
+    "cust_awp_nop_ignore_m_no_ofld": (path_8_14, *nones(3)),
+    "cust_awp_nop_ignore_p_no_ofld_uo": (path_ignore_p_uo, *nones(3)),
+    "unsupp_torch_version": ({}, None, "is supported from PyTorch", None),
+    "non_disjoint_phase_fsdp_params": ({}, None, "do not have disjoint FSDP-flattened parameter", None),
+    "non_disjoint_phase_mods": ({}, None, "not have disjoint", None),
+    "non_disjoint_excluded_ft_params": ({}, None, "parameters not included in", None),
+    "already_fsdp_wrapped": ({}, None, "already wrapped by FSDP", None),
+    "no_fsdp_params_p0": ({}, None, "one or more FSDP", None),
+    "warn_unsupp_nodecay": ({}, "will now be unset", *nones(2)),
+    "unmatched_awp_overrides": ({}, None, "did not match any named modules", None),
+    "cust_awp_prec": (path_default, *nones(3)),
+    "cust_awp_prec_pt1x": (path_default, *nones(3)),
+    "enforceP0_cust_awp_prec": (path_default, *nones(3)),
     # "batch_norm_auto_prec": (path_8_16, "Both mixed precision", None),  # _dynamo/allowed_functions.py suppresses
-    "batch_norm_auto_prec": (path_8_16, None, None),
-    "shared_params_auto_prec": (path_5_10, ("Pruning explicitly specified",), None),
-    "override_csm_adam_noprec": (path_ext_7_14, *nones(2)),
-    "cust_awp_overrides_prec": (path_default, *nones(2)),
-    "cust_awp_overrides_prec_ext": (path_ext_8_16, *nones(2)),
-    "warn_ignore_awp_override": ({}, "will be unset and not applied", None),
-    "cust_noprec_resume": (path_default, *nones(2)),
+    "batch_norm_auto_prec": (path_8_16, *nones(3)),
+    "shared_params_auto_prec": (path_5_10, ("Pruning explicitly specified",), *nones(2)),
+    "override_csm_adam_noprec": (path_ext_7_14, *nones(3)),
+    "cust_awp_overrides_prec": (path_default, *nones(3)),
+    "cust_awp_overrides_prec_ext": (path_ext_8_16, *nones(3)),
+    "warn_ignore_awp_override": ({}, "will be unset and not applied", *nones(2)),
+    "cust_noprec_resume": (path_default, *nones(3)),
 }
 
 
 @RunIf(min_cuda_gpus=2, skip_windows=True, standalone=True, min_torch="1.13")
 @pytest.mark.parametrize(
     "model_cfg_key, model_cls, auto_wrap_policy, use_precision, ft_sched_idx, model_cfg, strategy_adapter_cfg, fts_cfg,\
           trainer_cfg, strategy_cfg",
@@ -598,14 +656,26 @@
             None,
             epoch_t_only,
             max_epoch_4,
             test_use_orig,
             marks=RunIf(min_torch="2.0"),
         ),
         pytest.param(
+            "cust_awp_mwp_reinitlr_optim",
+            base_model,
+            awp_mwp_parity,
+            True,
+            8,
+            unwrap_7_mp,
+            None,
+            opt_inspect,
+            *nones(2),
+            marks=RunIf(min_torch="2.0"),
+        ),
+        pytest.param(
             "cust_awp_mwp_parity",
             base_model,
             awp_mwp_parity,
             True,
             0,
             unwrap_7_mp,
             *nones(4),
@@ -655,14 +725,15 @@
         ("cust_awp_overrides_prec_ext", ext_model, cust_ext_awp, True, 6, wrap_ext_mp, awp_7_8, *nones(3)),
         ("warn_ignore_awp_override", cust_model, None, False, 0, unwrap_7, awp_7, *nones(3)),
     ],
     ids=[
         "cust_awp_noprec",
         "cust_awp_noprec_use_orig",
         "cust_awp_noprec_dynamo_use_orig",
+        "cust_awp_mwp_reinitlr_optim",
         "cust_awp_mwp_parity",
         "override_csm_noprec",
         "cust_awp_nop_ignore_m_no_ofld",
         "cust_awp_nop_ignore_p_no_ofld_uo",
         "unsupp_torch_version",
         "non_disjoint_phase_fsdp_params",
         "non_disjoint_phase_mods",
@@ -695,22 +766,32 @@
     strategy_adapter_cfg,
     fts_cfg,
     trainer_cfg,
     strategy_cfg,
 ):
     """Conservative (end-to-end) set of tests for FTS support of FSDP."""
     cfg = init_test_cfg(model_cfg_key, model_cfg, fts_cfg, trainer_cfg, strategy_cfg, use_precision)
-    fts_state, warns_expected, exception_expected, model_cfg, fts_cfg, trainer_cfg, strategy_cfg, precision_opts = cfg
+    (
+        fts_state,
+        lrs_state,
+        warns_expected,
+        exception_expected,
+        model_cfg,
+        fts_cfg,
+        trainer_cfg,
+        strategy_cfg,
+        precision_opts,
+    ) = cfg
     seed_everything(42)
     use_dynamo = True if model_cfg.pop("use_dynamo", None) else False
     model = model_cls(**model_cfg)
     strategy_cfg = load_ignore_directives(strategy_cfg, model)
     ft_sched = fsdp_ft_schedules[ft_sched_idx]
-    test_cfg = init_fts_cfg(fts_state, strategy_adapter_cfg, fts_cfg)
-    callbacks = callbacks_cfg(FSDPTestFinetuningScheduler, ft_sched, test_cfg, {"patience": 2}, {"save_top_k": 3})
+    test_cfg, fts_cls = init_fts_cfg(fts_state, lrs_state, strategy_adapter_cfg, fts_cfg, tmpdir)
+    callbacks = callbacks_cfg(fts_cls, ft_sched, test_cfg, {"patience": 2}, {"save_top_k": 3})
     strategy = FSDPStrategy(auto_wrap_policy=auto_wrap_policy, **strategy_cfg)
     trainer = configure_trainer(tmpdir, strategy, callbacks, {**trainer_cfg, **precision_opts})
     configured_model = torch.compile(model) if use_dynamo else model
     if exception_expected:
         gen_exceptions(trainer, configured_model, model_cfg_key, exception_expected)
     else:
         trainer.fit(configured_model)
@@ -755,26 +836,43 @@
             with pytest.raises(MisconfigurationException, match=exception_expected):
                 trainer.fit(model)
     else:
         with pytest.raises(MisconfigurationException, match=exception_expected):
             trainer.fit(model)
 
 
-def init_fts_cfg(fts_state, strategy_adapter_cfg, fts_cfg):
-    def_fts_cfg = {"logging_level": DEBUG, "expected_state": fts_state, "strategy_adapter_cfg": strategy_adapter_cfg}
+def init_fts_cfg(fts_state, lrs_state, strategy_adapter_cfg, fts_cfg, tmpdir):
+    def_fts_cfg = {
+        "logging_level": DEBUG,
+        "expected_state": fts_state,
+        "lrs_state": lrs_state,
+        "strategy_adapter_cfg": strategy_adapter_cfg,
+        # "state_log_dir": tmpdir
+    }
+    fts_cls = fts_cfg.pop("test_fts") if fts_cfg and fts_cfg.get("test_fts") else FSDPTestFinetuningScheduler
     test_cfg = {**fts_cfg, **def_fts_cfg}
-    return test_cfg
+    return test_cfg, fts_cls
 
 
 def init_test_cfg(model_cfg_key, model_cfg, fts_cfg, trainer_cfg, strategy_cfg, use_precision):
     expected_state = EXPECTED_FSDP_FTS_RESULTS[model_cfg_key]
-    fts_state, warns_expected, exception_expected = expected_state
+    fts_state, warns_expected, exception_expected, lrs_state = expected_state
     init_cfg = model_cfg, fts_cfg, trainer_cfg, strategy_cfg, use_precision
     model_cfg, fts_cfg, trainer_cfg, strategy_cfg, precision_opts = map_component_cfgs(*init_cfg)
-    return fts_state, warns_expected, exception_expected, model_cfg, fts_cfg, trainer_cfg, strategy_cfg, precision_opts
+    return (
+        fts_state,
+        lrs_state,
+        warns_expected,
+        exception_expected,
+        model_cfg,
+        fts_cfg,
+        trainer_cfg,
+        strategy_cfg,
+        precision_opts,
+    )
 
 
 def map_component_cfgs(model_cfg, fts_cfg, trainer_cfg, strategy_cfg, use_precision):
     trainer_cfg = trainer_cfg or {"max_epochs": 3}
     model_cfg = model_cfg or {}
     fts_cfg = fts_cfg or {}
     strategy_cfg = strategy_cfg or {"cpu_offload": True}
```

