# Comparing `tmp/xturing-0.0.8.tar.gz` & `tmp/xturing-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "xturing-0.0.8.tar", last modified: Tue Apr  4 15:35:31 2023, max compression
+gzip compressed data, was "xturing-0.0.9.tar", last modified: Thu Apr  6 13:16:21 2023, max compression
```

## Comparing `xturing-0.0.8.tar` & `xturing-0.0.9.tar`

### file list

```diff
@@ -1,105 +1,108 @@
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.888508 xturing-0.0.8/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    11357 2023-03-20 07:53:44.000000 xturing-0.0.8/LICENSE
--rw-r--r--   0 sarthaklangde   (501) staff       (20)       34 2023-03-29 09:34:15.000000 xturing-0.0.8/MANIFEST.in
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    21066 2023-04-04 15:35:31.888176 xturing-0.0.8/PKG-INFO
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     6625 2023-04-03 17:26:37.000000 xturing-0.0.8/README.md
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2127 2023-04-04 15:35:22.000000 xturing-0.0.8/pyproject.toml
--rw-r--r--   0 sarthaklangde   (501) staff       (20)       38 2023-04-04 15:35:31.888592 xturing-0.0.8/setup.cfg
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.834767 xturing-0.0.8/src/
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.842461 xturing-0.0.8/src/xturing/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)       22 2023-04-04 15:35:22.000000 xturing-0.0.8/src/xturing/__about__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      438 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/__init__.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.850276 xturing-0.0.8/src/xturing/cli/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      561 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/cli/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2042 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/cli/api.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      989 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/cli/chat.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      131 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/cli/ui.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.853490 xturing-0.0.8/src/xturing/config/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      569 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/config/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      972 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/config/config_data_classes.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2503 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/config/finetuning_config.yaml
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2627 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/config/generation_config.yaml
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1502 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/config/read_config.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.856598 xturing-0.0.8/src/xturing/datasets/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      436 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/datasets/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      199 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/datasets/base.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     8111 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/datasets/instruction_dataset.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      222 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/datasets/text2image_dataset.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1830 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/datasets/text_dataset.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.862563 xturing-0.0.8/src/xturing/engines/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     3076 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      272 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/engines/base.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1740 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/bloom_engine.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     6083 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/engines/causal.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1832 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/cerebras_engine.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      730 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/engines/distilgpt2_engine.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1644 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/galactica_engine.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1468 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/gpt2_engine.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2805 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/gptj_engine.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.863261 xturing-0.0.8/src/xturing/engines/gptj_utils/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/engines/gptj_utils/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     7690 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/engines/gptj_utils/gptj.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     3664 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/engines/llama_engine.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.864316 xturing-0.0.8/src/xturing/engines/llama_utils/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)       65 2023-03-26 14:55:44.000000 xturing-0.0.8/src/xturing/engines/llama_utils/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    44486 2023-03-26 14:55:44.000000 xturing-0.0.8/src/xturing/engines/llama_utils/llama.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1672 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/engines/opt_engine.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.867630 xturing-0.0.8/src/xturing/model_apis/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      864 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/model_apis/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1827 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/model_apis/ai21.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      573 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/model_apis/base.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1847 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/model_apis/cohere.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     4600 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/model_apis/openai.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.873067 xturing-0.0.8/src/xturing/models/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2483 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2067 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/models/base.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1084 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/bloom.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     7132 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/causal.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1135 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/cerebras.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      579 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/distilgpt2.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1152 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/galactica.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1033 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/gpt2.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1067 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/gptj.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1097 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/llama.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1050 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/models/opt.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      542 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/models/stable_diffusion.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.875739 xturing-0.0.8/src/xturing/preprocessors/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      137 2023-03-26 14:55:44.000000 xturing-0.0.8/src/xturing/preprocessors/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      484 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/preprocessors/base.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     4582 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/preprocessors/instruction_collator.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2252 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/preprocessors/text_collator.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      642 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/registry.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.878893 xturing-0.0.8/src/xturing/self_instruct/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/self_instruct/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     9891 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/self_instruct/bootstrap_instructions.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     5490 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/self_instruct/generate_instances.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     3737 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/self_instruct/identify_if_classification.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    14280 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/self_instruct/prepare_for_finetuning.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2108 2023-04-03 18:00:10.000000 xturing-0.0.8/src/xturing/self_instruct/prepare_seed_tasks.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.880077 xturing-0.0.8/src/xturing/self_instruct/templates/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     3580 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/self_instruct/templates/clf_task_template.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    12674 2023-03-29 10:14:08.000000 xturing-0.0.8/src/xturing/self_instruct/templates/instance_gen_template.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.882009 xturing-0.0.8/src/xturing/trainers/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)       78 2023-03-26 14:55:44.000000 xturing-0.0.8/src/xturing/trainers/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      233 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/trainers/base.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     5683 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/trainers/lightning_trainer.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.882826 xturing-0.0.8/src/xturing/ui/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/ui/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    13646 2023-04-03 17:19:47.000000 xturing-0.0.8/src/xturing/ui/playground.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.887388 xturing-0.0.8/src/xturing/utils/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/utils/__init__.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      215 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/utils/external_loggers.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     3013 2023-04-03 17:26:37.000000 xturing-0.0.8/src/xturing/utils/hub.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      304 2023-03-26 14:55:44.000000 xturing-0.0.8/src/xturing/utils/interactive.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2147 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/utils/logging.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      621 2023-03-24 13:26:24.000000 xturing-0.0.8/src/xturing/utils/loss_fns.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     1366 2023-04-03 17:19:41.000000 xturing-0.0.8/src/xturing/utils/notebooks.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     6980 2023-04-03 18:00:10.000000 xturing-0.0.8/src/xturing/utils/text_splitter.py
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     3803 2023-04-04 15:31:51.000000 xturing-0.0.8/src/xturing/utils/utils.py
-drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-04 15:35:31.846873 xturing-0.0.8/src/xturing.egg-info/
--rw-r--r--   0 sarthaklangde   (501) staff       (20)    21066 2023-04-04 15:35:31.000000 xturing-0.0.8/src/xturing.egg-info/PKG-INFO
--rw-r--r--   0 sarthaklangde   (501) staff       (20)     2892 2023-04-04 15:35:31.000000 xturing-0.0.8/src/xturing.egg-info/SOURCES.txt
--rw-r--r--   0 sarthaklangde   (501) staff       (20)        1 2023-04-04 15:35:31.000000 xturing-0.0.8/src/xturing.egg-info/dependency_links.txt
--rw-r--r--   0 sarthaklangde   (501) staff       (20)       48 2023-04-04 15:35:31.000000 xturing-0.0.8/src/xturing.egg-info/entry_points.txt
--rw-r--r--   0 sarthaklangde   (501) staff       (20)      204 2023-04-04 15:35:31.000000 xturing-0.0.8/src/xturing.egg-info/requires.txt
--rw-r--r--   0 sarthaklangde   (501) staff       (20)        8 2023-04-04 15:35:31.000000 xturing-0.0.8/src/xturing.egg-info/top_level.txt
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.495084 xturing-0.0.9/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    11357 2023-03-20 07:53:44.000000 xturing-0.0.9/LICENSE
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       34 2023-03-29 09:34:15.000000 xturing-0.0.9/MANIFEST.in
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    21067 2023-04-06 13:16:21.494447 xturing-0.0.9/PKG-INFO
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     6626 2023-04-05 17:10:03.000000 xturing-0.0.9/README.md
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2135 2023-04-06 13:15:31.000000 xturing-0.0.9/pyproject.toml
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       38 2023-04-06 13:16:21.495257 xturing-0.0.9/setup.cfg
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.436669 xturing-0.0.9/src/
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.441722 xturing-0.0.9/src/xturing/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       22 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/__about__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      438 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/__init__.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.449702 xturing-0.0.9/src/xturing/cli/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      561 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/cli/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2042 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/cli/api.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      989 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/cli/chat.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      131 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/cli/ui.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.452891 xturing-0.0.9/src/xturing/config/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      569 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/config/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      972 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/config/config_data_classes.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2503 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/config/finetuning_config.yaml
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2627 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/config/generation_config.yaml
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1502 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/config/read_config.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.456789 xturing-0.0.9/src/xturing/datasets/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      436 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/datasets/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      199 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/datasets/base.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     8179 2023-04-05 17:10:03.000000 xturing-0.0.9/src/xturing/datasets/instruction_dataset.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      222 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/datasets/text2image_dataset.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1830 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/datasets/text_dataset.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.465559 xturing-0.0.9/src/xturing/engines/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     3076 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/engines/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      272 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/engines/base.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1871 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/bloom_engine.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     6273 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/causal.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1923 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/cerebras_engine.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      804 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/distilgpt2_engine.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1755 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/galactica_engine.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1446 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/gpt2_engine.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2912 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/gptj_engine.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.466532 xturing-0.0.9/src/xturing/engines/gptj_utils/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/engines/gptj_utils/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     7690 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/engines/gptj_utils/gptj.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     3647 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/llama_engine.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.468647 xturing-0.0.9/src/xturing/engines/llama_utils/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       65 2023-03-26 14:55:44.000000 xturing-0.0.9/src/xturing/engines/llama_utils/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    44486 2023-03-26 14:55:44.000000 xturing-0.0.9/src/xturing/engines/llama_utils/llama.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.471063 xturing-0.0.9/src/xturing/engines/lora_engine/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       73 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/lora_engine/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    33454 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/lora_engine/lora.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1830 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/engines/opt_engine.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.474463 xturing-0.0.9/src/xturing/model_apis/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      864 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/model_apis/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1827 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/model_apis/ai21.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      573 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/model_apis/base.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1847 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/model_apis/cohere.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     4600 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/model_apis/openai.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.480404 xturing-0.0.9/src/xturing/models/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2483 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2067 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/models/base.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1084 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/bloom.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     7132 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/causal.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1135 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/cerebras.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      579 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/distilgpt2.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1152 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/galactica.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1033 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/gpt2.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1067 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/gptj.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1097 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/llama.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1050 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/models/opt.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      542 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/models/stable_diffusion.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.482792 xturing-0.0.9/src/xturing/preprocessors/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      137 2023-03-26 14:55:44.000000 xturing-0.0.9/src/xturing/preprocessors/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      484 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/preprocessors/base.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     4582 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/preprocessors/instruction_collator.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2252 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/preprocessors/text_collator.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      642 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/registry.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.485328 xturing-0.0.9/src/xturing/self_instruct/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/self_instruct/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     9891 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/self_instruct/bootstrap_instructions.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     5490 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/self_instruct/generate_instances.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     3737 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/self_instruct/identify_if_classification.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    14280 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/self_instruct/prepare_for_finetuning.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2198 2023-04-05 17:10:03.000000 xturing-0.0.9/src/xturing/self_instruct/prepare_seed_tasks.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.486519 xturing-0.0.9/src/xturing/self_instruct/templates/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     3580 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/self_instruct/templates/clf_task_template.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    12674 2023-03-29 10:14:08.000000 xturing-0.0.9/src/xturing/self_instruct/templates/instance_gen_template.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.488270 xturing-0.0.9/src/xturing/trainers/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       78 2023-03-26 14:55:44.000000 xturing-0.0.9/src/xturing/trainers/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      233 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/trainers/base.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     5856 2023-04-06 13:15:31.000000 xturing-0.0.9/src/xturing/trainers/lightning_trainer.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.488937 xturing-0.0.9/src/xturing/ui/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/ui/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    13646 2023-04-03 17:19:47.000000 xturing-0.0.9/src/xturing/ui/playground.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.493432 xturing-0.0.9/src/xturing/utils/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)        0 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/utils/__init__.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      215 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/utils/external_loggers.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     3013 2023-04-03 17:26:37.000000 xturing-0.0.9/src/xturing/utils/hub.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      304 2023-03-26 14:55:44.000000 xturing-0.0.9/src/xturing/utils/interactive.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2147 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/utils/logging.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      621 2023-03-24 13:26:24.000000 xturing-0.0.9/src/xturing/utils/loss_fns.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     1366 2023-04-03 17:19:41.000000 xturing-0.0.9/src/xturing/utils/notebooks.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     6980 2023-04-05 17:10:03.000000 xturing-0.0.9/src/xturing/utils/text_splitter.py
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     3803 2023-04-05 17:10:03.000000 xturing-0.0.9/src/xturing/utils/utils.py
+drwxr-xr-x   0 sarthaklangde   (501) staff       (20)        0 2023-04-06 13:16:21.445406 xturing-0.0.9/src/xturing.egg-info/
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)    21067 2023-04-06 13:16:21.000000 xturing-0.0.9/src/xturing.egg-info/PKG-INFO
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)     2976 2023-04-06 13:16:21.000000 xturing-0.0.9/src/xturing.egg-info/SOURCES.txt
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)        1 2023-04-06 13:16:21.000000 xturing-0.0.9/src/xturing.egg-info/dependency_links.txt
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)       48 2023-04-06 13:16:21.000000 xturing-0.0.9/src/xturing.egg-info/entry_points.txt
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)      212 2023-04-06 13:16:21.000000 xturing-0.0.9/src/xturing.egg-info/requires.txt
+-rw-r--r--   0 sarthaklangde   (501) staff       (20)        8 2023-04-06 13:16:21.000000 xturing-0.0.9/src/xturing.egg-info/top_level.txt
```

### Comparing `xturing-0.0.8/LICENSE` & `xturing-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/PKG-INFO` & `xturing-0.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xturing
-Version: 0.0.8
+Version: 0.0.9
 Summary: Fine-tuning, evaluation and data generation for LLMs
 Author-email: Glenn Ko <glenn@stochastic.ai>, Yuji Chai <yuji.chai@stochastic.ai>, Roman Ageev <roman.ageev@stochastic.ai>, Toan Do <toan.do@stochastic.ai>, Marcos R M <marcos.rm@stochastic.ai>, Sarthak Langde <sarthak.langde@stochastic.ai>, Riccardo Romagnoli <riccardo.romagnoli@stochastic.ai>, Subhash G N <subhash.gn@stochastic.ai>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
         
            TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
@@ -241,15 +241,15 @@
 ensuring data privacy and security.
 
 With `xturing` you can,
 - Ingest data from different sources and preprocess them to a format LLMs can understand
 - Scale from single to multiple GPUs for faster fine-tuning
 - Leverage memory-efficient techniques (i.e. LoRA fine-tuning) to reduce your hardware costs by up to 90% of the time
 - Explore different fine-tuning methods and benchmark them to find the best performing model
-- Evalate fine-tuned models on well-defined metrics for in-depth analysis
+- Evaluate fine-tuned models on well-defined metrics for in-depth analysis
 
 <br>
 <p align="center">
   <a href="https://pypi.org/project/xturing/">
     <img src="https://img.shields.io/pypi/v/xturing?style=for-the-badge" />
   </a>
   <a href="https://xturing.stochastic.ai/">
```

### Comparing `xturing-0.0.8/README.md` & `xturing-0.0.9/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 ensuring data privacy and security.
 
 With `xturing` you can,
 - Ingest data from different sources and preprocess them to a format LLMs can understand
 - Scale from single to multiple GPUs for faster fine-tuning
 - Leverage memory-efficient techniques (i.e. LoRA fine-tuning) to reduce your hardware costs by up to 90% of the time
 - Explore different fine-tuning methods and benchmark them to find the best performing model
-- Evalate fine-tuned models on well-defined metrics for in-depth analysis
+- Evaluate fine-tuned models on well-defined metrics for in-depth analysis
 
 <br>
 <p align="center">
   <a href="https://pypi.org/project/xturing/">
     <img src="https://img.shields.io/pypi/v/xturing?style=for-the-badge" />
   </a>
   <a href="https://xturing.stochastic.ai/">
```

#### html2text {}

```diff
@@ -6,16 +6,16 @@
 xTuring makes it simple to build and control LLMs. The entire process can be
 done inside your computer or in your private cloud, ensuring data privacy and
 security. With `xturing` you can, - Ingest data from different sources and
 preprocess them to a format LLMs can understand - Scale from single to multiple
 GPUs for faster fine-tuning - Leverage memory-efficient techniques (i.e. LoRA
 fine-tuning) to reduce your hardware costs by up to 90% of the time - Explore
 different fine-tuning methods and benchmark them to find the best performing
-model - Evalate fine-tuned models on well-defined metrics for in-depth analysis
-
+model - Evaluate fine-tuned models on well-defined metrics for in-depth
+analysis
      [https://img.shields.io/pypi/v/xturing?style=for-the-badge] [https://
 img.shields.io/badge/Documentation-blue?logo=GitBook&logoColor=white&style=for-
  the-badge] [https://img.shields.io/badge/Chat-FFFFFF?logo=discord&style=for-
                                   the-badge]
 
 ## CLI playground [.github/cli-playground.gif] ## UI playground [.github/ui-
 playground2.gif] ## âï¸ Installation ```bash pip install xturing ```
```

### Comparing `xturing-0.0.8/pyproject.toml` & `xturing-0.0.9/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "xturing"
-version = "0.0.8"
+version = "0.0.9"
 description = "Fine-tuning, evaluation and data generation for LLMs"
 
 authors = [
     { name = "Glenn Ko", email = "glenn@stochastic.ai" },
     { name = "Yuji Chai", email = "yuji.chai@stochastic.ai" },
     { name = "Roman Ageev", email = "roman.ageev@stochastic.ai" },
     { name = "Toan Do", email = "toan.do@stochastic.ai" },
@@ -42,15 +42,15 @@
 ]
 dependencies = [
     "torch >= 1.9.0",
     "pytorch-lightning",
     "transformers==4.27.3",
     "datasets",
     "evaluate",
-    "peft",
+    "bitsandbytes",
     "sentencepiece",
     "deepspeed",
     "gradio",
     "bitsandbytes",
     "click",
     "wget",
     "ai21",
```

### Comparing `xturing-0.0.8/src/xturing/cli/__init__.py` & `xturing-0.0.9/src/xturing/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/cli/api.py` & `xturing-0.0.9/src/xturing/cli/api.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/cli/chat.py` & `xturing-0.0.9/src/xturing/cli/chat.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/config/__init__.py` & `xturing-0.0.9/src/xturing/config/__init__.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/config/config_data_classes.py` & `xturing-0.0.9/src/xturing/config/config_data_classes.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/config/finetuning_config.yaml` & `xturing-0.0.9/src/xturing/config/finetuning_config.yaml`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/config/generation_config.yaml` & `xturing-0.0.9/src/xturing/config/generation_config.yaml`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/config/read_config.py` & `xturing-0.0.9/src/xturing/config/read_config.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/datasets/instruction_dataset.py` & `xturing-0.0.9/src/xturing/datasets/instruction_dataset.py`

 * *Files 2% similar despite different names*

```diff
@@ -201,34 +201,35 @@
         chunk_size=8000,
         num_samples_per_chunk=5,
         use_self_instruct=False,
     ):
         txt_dir = extract_text_from_directory(path)
         prepare_seed_tasks.prepare_seed_tasks(
             txt_dir,
-            "finance_seed_tasks.jsonl",
+            "generated_tasks.jsonl",
             engine,
             chunk_size,
             num_samples_per_chunk,
         )
+        print(f"The generated data is stored in generated_tasks.jsonl file")
 
         if use_self_instruct:
             instruction_dataset = InstructionDataset.generate_dataset(
-                "finance_seed_tasks.jsonl",
+                "generated_tasks.jsonl",
                 engine,
                 num_instructions,
                 num_instructions_for_finetuning,
                 num_prompt_instructions,
             )
             return instruction_dataset
         else:
             instructions = []
             outputs = []
             texts = []
-            with open("finance_seed_tasks.jsonl") as f:
+            with open("generated_tasks.jsonl") as f:
                 for line in f:
                     data = json.loads(line)
                     instructions.append(data["instruction"])
                     outputs.append(data["instances"][0]["output"])
                     texts.append("")
             data_dict = {
                 "train": {"instruction": instructions, "text": texts, "target": outputs}
```

### Comparing `xturing-0.0.8/src/xturing/datasets/text_dataset.py` & `xturing-0.0.9/src/xturing/datasets/text_dataset.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/engines/__init__.py` & `xturing-0.0.9/src/xturing/engines/__init__.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/engines/bloom_engine.py` & `xturing-0.0.9/src/xturing/engines/opt_engine.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,51 +1,55 @@
+import os
 from pathlib import Path
 from typing import Optional, Union
 
 from xturing.engines.causal import CausalEngine, CausalLoraEngine
 
 
-class BloomEngine(CausalEngine):
-    config_name: str = "bloom_engine"
+class OPTEngine(CausalEngine):
+    config_name: str = "opt_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
-        super().__init__(model_name="bigscience/bloom-1b1", weights_path=weights_path)
+        super().__init__(model_name="facebook/opt-1.3b", weights_path=weights_path)
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
-class BloomLoraEngine(CausalLoraEngine):
-    config_name: str = "bloom_lora_engine"
+class OPTLoraEngine(CausalLoraEngine):
+    config_name: str = "opt_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
-        super().__init__(model_name="bigscience/bloom-1b1", weights_path=weights_path)
+        super().__init__(
+            model_name="facebook/opt-1.3b",
+            weights_path=weights_path,
+            target_modules=["q_proj", "v_proj"],
+        )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
-class BloomInt8Engine(CausalEngine):
-    config_name: str = "bloom_int8_engine"
+class OPTInt8Engine(CausalEngine):
+    config_name: str = "opt_int8_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="bigscience/bloom-1b1",
-            weights_path=weights_path,
-            load_8bit=True,
+            model_name="facebook/opt-1.3b", weights_path=weights_path, load_8bit=True
         )
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
-class BloomLoraInt8Engine(CausalLoraEngine):
-    config_name: str = "bloom_lora_int8_engine"
+class OPTLoraInt8Engine(CausalLoraEngine):
+    config_name: str = "opt_lora_int8_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="bigscience/bloom-1b1",
+            model_name="facebook/opt-1.3b",
             weights_path=weights_path,
             load_8bit=True,
+            target_modules=["q_proj", "v_proj"],
         )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
```

### Comparing `xturing-0.0.8/src/xturing/engines/causal.py` & `xturing-0.0.9/src/xturing/engines/causal.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,20 +1,24 @@
 import os
 from pathlib import Path
 from typing import Any, List, Optional, Union
 
 import evaluate
 import torch
-from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_int8_training
 from transformers import AutoModelForCausalLM, AutoTokenizer
 
 from xturing.config import DEFAULT_DEVICE, DEFAULT_DTYPE
+from xturing.config.read_config import exists_xturing_config_file
 from xturing.engines.base import BaseEngine
+from xturing.engines.lora_engine import (
+    LoraConfig,
+    LoraModel,
+    prepare_model_for_int8_training,
+)
 from xturing.utils.loss_fns import CrossEntropyLoss
-from xturing.config.read_config import exists_xturing_config_file
 
 
 class CausalEngine(BaseEngine):
     def __init__(
         self,
         *,
         model_name: Optional[str] = None,
@@ -122,38 +126,45 @@
         load_8bit: Optional[bool] = False,
         target_modules: Optional[Union[List[str], str]] = None,
     ):
         # The base model should always be loaded from the original model
         # That's why weights_path is None. If not model.eval() will fail later
         super().__init__(
             model_name=model_name,
-            weights_path=None if exists_xturing_config_file(weights_path) else weights_path,
+            weights_path=None
+            if exists_xturing_config_file(weights_path)
+            else weights_path,
             model=model,
             tokenizer=tokenizer,
             load_8bit=load_8bit,
         )
 
         # The model before applying LoRA
         self.base_model = self.model
 
-        peft_config = LoraConfig(
+        lora_config = LoraConfig(
             r=8,
             lora_alpha=32,
             target_modules=target_modules,
             lora_dropout=0.05,
             bias="none",
-            task_type="CAUSAL_LM",
+            inference_mode=False,
         )
-        self.model = get_peft_model(self.base_model, peft_config)
+
+        if len(target_modules) == 1:
+            lora_config.fan_in_fan_out = True
+            lora_config.enable_lora = [True, False, True]
+
+        self.model = LoraModel(lora_config, self.base_model)
 
         if weights_path is not None and exists_xturing_config_file(weights_path):
             model_weights_path = str(Path(weights_path).resolve() / "pytorch_model.bin")
             self.model.load_state_dict(
                 torch.load(
-                    model_weights_path, map_location=torch.device(DEFAULT_DEVICE)
+                    model_weights_path  # , map_location=torch.device(DEFAULT_DEVICE)
                 )
             )
         else:
             self.model.print_trainable_parameters()
 
         self.loss_fct = CrossEntropyLoss()
```

### Comparing `xturing-0.0.8/src/xturing/engines/cerebras_engine.py` & `xturing-0.0.9/src/xturing/engines/cerebras_engine.py`

 * *Files 13% similar despite different names*

```diff
@@ -17,15 +17,17 @@
 
 
 class CerebrasLoraEngine(CausalLoraEngine):
     config_name: str = "cerebras_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="cerebras/Cerebras-GPT-1.3B", weights_path=weights_path
+            model_name="cerebras/Cerebras-GPT-1.3B",
+            weights_path=weights_path,
+            target_modules=["c_attn"],
         )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
 class CerebrasInt8Engine(CausalEngine):
@@ -45,11 +47,12 @@
     config_name: str = "cerebras_lora_int8_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
             model_name="cerebras/Cerebras-GPT-1.3B",
             weights_path=weights_path,
             load_8bit=True,
+            target_modules=["c_attn"],
         )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
```

### Comparing `xturing-0.0.8/src/xturing/engines/distilgpt2_engine.py` & `xturing-0.0.9/src/xturing/engines/distilgpt2_engine.py`

 * *Files 9% similar despite different names*

```diff
@@ -13,10 +13,14 @@
         self.tokenizer.pad_token = self.tokenizer.eos_token
 
 
 class DistilGPT2LoraEngine(CausalLoraEngine):
     config_name: str = "distilgpt2_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
-        super().__init__(model_name="distilgpt2", weights_path=weights_path)
+        super().__init__(
+            model_name="distilgpt2",
+            weights_path=weights_path,
+            target_modules=["c_attn"],
+        )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
```

### Comparing `xturing-0.0.8/src/xturing/engines/galactica_engine.py` & `xturing-0.0.9/src/xturing/engines/galactica_engine.py`

 * *Files 8% similar despite different names*

```diff
@@ -17,15 +17,17 @@
 
 
 class GalacticaLoraEngine(CausalLoraEngine):
     config_name: str = "galactica_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="facebook/galactica-6.7b", weights_path=weights_path
+            model_name="facebook/galactica-6.7b",
+            weights_path=weights_path,
+            target_modules=["q_proj", "v_proj"],
         )
 
         self.tokenizer.eos_token_id = 2
         self.tokenizer.pad_token_id = 1
 
 
 class GalacticaInt8Engine(CausalEngine):
@@ -45,11 +47,12 @@
     config_name: str = "galactica_lora_int8_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
             model_name="facebook/galactica-6.7b",
             weights_path=weights_path,
             load_8bit=True,
+            target_modules=["q_proj", "v_proj"],
         )
 
         self.tokenizer.eos_token_id = 2
         self.tokenizer.pad_token_id = 1
```

### Comparing `xturing-0.0.8/src/xturing/engines/gpt2_engine.py` & `xturing-0.0.9/src/xturing/engines/gpt2_engine.py`

 * *Files 6% similar despite different names*

```diff
@@ -13,15 +13,17 @@
         self.tokenizer.pad_token = self.tokenizer.eos_token
 
 
 class GPT2LoraEngine(CausalLoraEngine):
     config_name: str = "gpt2_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
-        super().__init__(model_name="gpt2", weights_path=weights_path)
+        super().__init__(
+            model_name="gpt2", weights_path=weights_path, target_modules=["c_attn"]
+        )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
 
 
 class GPT2Int8Engine(CausalEngine):
     config_name: str = "gpt2_engine_int8"
 
@@ -37,10 +39,9 @@
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
             model_name="gpt2",
             weights_path=weights_path,
             load_8bit=True,
             target_modules=["c_attn"],
         )
-        super().__init__(model_name="gpt2", weights_path=weights_path)
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
```

### Comparing `xturing-0.0.8/src/xturing/engines/gptj_engine.py` & `xturing-0.0.9/src/xturing/engines/gptj_engine.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 import os
 from pathlib import Path
 from typing import Optional, Union
 
 import torch
 import transformers
-from peft import prepare_model_for_int8_training
 from transformers import AutoModelForCausalLM, AutoTokenizer
 
 from xturing.engines.causal import CausalEngine, CausalLoraEngine
 from xturing.engines.gptj_utils.gptj import GPTJAttention
+from xturing.engines.lora_engine import prepare_model_for_int8_training
 
 
 class GPTJEngine(CausalEngine):
     config_name: str = "gptj_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
@@ -23,15 +23,17 @@
 
 
 class GPTJLoraEngine(CausalLoraEngine):
     config_name: str = "gptj_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="philschmid/gpt-j-6B-fp16-sharded", weights_path=weights_path
+            model_name="philschmid/gpt-j-6B-fp16-sharded",
+            weights_path=weights_path,
+            target_modules=["q_proj", "v_proj"],
         )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
 
 
 class GPTJInt8Engine(CausalEngine):
     config_name: str = "gptj_int8_engine"
@@ -40,15 +42,17 @@
         transformers.models.gptj.modeling_gptj.GPTJAttention = GPTJAttention
 
         device_map = {"": int(os.environ.get("LOCAL_RANK") or 0)}
         model = AutoModelForCausalLM.from_pretrained(
             "philschmid/gpt-j-6B-fp16-sharded", load_in_8bit=True, device_map=device_map
         )
 
-        tokenizer = AutoTokenizer.from_pretrained("philschmid/gpt-j-6B-fp16-sharded")
+        tokenizer = AutoTokenizer.from_pretrained(
+            "philschmid/gpt-j-6B-fp16-sharded"
+        )
         tokenizer.pad_token = self.tokenizer.eos_token
         super().__init__(
             weights_path=weights_path, model=model, tokenizer=tokenizer, load_8bit=True
         )
 
 
 class GPTJLoraInt8Engine(CausalLoraEngine):
```

### Comparing `xturing-0.0.8/src/xturing/engines/gptj_utils/gptj.py` & `xturing-0.0.9/src/xturing/engines/gptj_utils/gptj.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/engines/llama_engine.py` & `xturing-0.0.9/src/xturing/engines/llama_engine.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,18 +1,16 @@
-import math
 import os
 from pathlib import Path
-from shutil import copyfile
 from typing import Any, Dict, List, Optional, Tuple, Union
 
 import torch
-from peft import prepare_model_for_int8_training
 
 from xturing.engines.causal import CausalEngine, CausalLoraEngine
 from xturing.engines.llama_utils import LlamaConfig, LlamaForCausalLM, LlamaTokenizer
+from xturing.engines.lora_engine import prepare_model_for_int8_training
 
 
 class LLamaEngine(CausalEngine):
     config_name: str = "llama_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         model_name = "aleksickx/llama-7b-hf"
```

### Comparing `xturing-0.0.8/src/xturing/engines/llama_utils/llama.py` & `xturing-0.0.9/src/xturing/engines/llama_utils/llama.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/engines/opt_engine.py` & `xturing-0.0.9/src/xturing/engines/bloom_engine.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,48 +1,56 @@
-import os
 from pathlib import Path
 from typing import Optional, Union
 
 from xturing.engines.causal import CausalEngine, CausalLoraEngine
 
 
-class OPTEngine(CausalEngine):
-    config_name: str = "opt_engine"
+class BloomEngine(CausalEngine):
+    config_name: str = "bloom_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
-        super().__init__(model_name="facebook/opt-1.3b", weights_path=weights_path)
+        super().__init__(model_name="bigscience/bloom-1b1", weights_path=weights_path)
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
-class OPTLoraEngine(CausalLoraEngine):
-    config_name: str = "opt_lora_engine"
+class BloomLoraEngine(CausalLoraEngine):
+    config_name: str = "bloom_lora_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
-        super().__init__(model_name="facebook/opt-1.3b", weights_path=weights_path)
+        super().__init__(
+            model_name="bigscience/bloom-1b1",
+            weights_path=weights_path,
+            target_modules=["query_key_value"],
+        )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
-class OPTInt8Engine(CausalEngine):
-    config_name: str = "opt_int8_engine"
+class BloomInt8Engine(CausalEngine):
+    config_name: str = "bloom_int8_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="facebook/opt-1.3b", weights_path=weights_path, load_8bit=True
+            model_name="bigscience/bloom-1b1",
+            weights_path=weights_path,
+            load_8bit=True,
         )
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
 
 
-class OPTLoraInt8Engine(CausalLoraEngine):
-    config_name: str = "opt_lora_int8_engine"
+class BloomLoraInt8Engine(CausalLoraEngine):
+    config_name: str = "bloom_lora_int8_engine"
 
     def __init__(self, weights_path: Optional[Union[str, Path]] = None):
         super().__init__(
-            model_name="facebook/opt-1.3b", weights_path=weights_path, load_8bit=True
+            model_name="bigscience/bloom-1b1",
+            weights_path=weights_path,
+            load_8bit=True,
+            target_modules=["query_key_value"],
         )
 
         self.tokenizer.pad_token = self.tokenizer.eos_token
         self.tokenizer.pad_token_id = self.tokenizer.eos_token_id
```

### Comparing `xturing-0.0.8/src/xturing/model_apis/__init__.py` & `xturing-0.0.9/src/xturing/model_apis/__init__.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/model_apis/ai21.py` & `xturing-0.0.9/src/xturing/model_apis/ai21.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/model_apis/base.py` & `xturing-0.0.9/src/xturing/model_apis/base.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/model_apis/cohere.py` & `xturing-0.0.9/src/xturing/model_apis/cohere.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/model_apis/openai.py` & `xturing-0.0.9/src/xturing/model_apis/openai.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/__init__.py` & `xturing-0.0.9/src/xturing/models/__init__.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/base.py` & `xturing-0.0.9/src/xturing/models/base.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/bloom.py` & `xturing-0.0.9/src/xturing/models/bloom.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/causal.py` & `xturing-0.0.9/src/xturing/models/causal.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/cerebras.py` & `xturing-0.0.9/src/xturing/models/cerebras.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/distilgpt2.py` & `xturing-0.0.9/src/xturing/models/distilgpt2.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/galactica.py` & `xturing-0.0.9/src/xturing/models/galactica.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/gpt2.py` & `xturing-0.0.9/src/xturing/models/gpt2.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/gptj.py` & `xturing-0.0.9/src/xturing/models/gptj.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/llama.py` & `xturing-0.0.9/src/xturing/models/llama.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/opt.py` & `xturing-0.0.9/src/xturing/models/opt.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/models/stable_diffusion.py` & `xturing-0.0.9/src/xturing/models/stable_diffusion.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/preprocessors/instruction_collator.py` & `xturing-0.0.9/src/xturing/preprocessors/instruction_collator.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/preprocessors/text_collator.py` & `xturing-0.0.9/src/xturing/preprocessors/text_collator.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/registry.py` & `xturing-0.0.9/src/xturing/registry.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/self_instruct/bootstrap_instructions.py` & `xturing-0.0.9/src/xturing/self_instruct/bootstrap_instructions.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/self_instruct/generate_instances.py` & `xturing-0.0.9/src/xturing/self_instruct/generate_instances.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/self_instruct/identify_if_classification.py` & `xturing-0.0.9/src/xturing/self_instruct/identify_if_classification.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/self_instruct/prepare_for_finetuning.py` & `xturing-0.0.9/src/xturing/self_instruct/prepare_for_finetuning.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/self_instruct/prepare_seed_tasks.py` & `xturing-0.0.9/src/xturing/self_instruct/prepare_seed_tasks.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,52 +1,55 @@
 import ast
 import json
 import os
 from typing import List
 
-import openai
+from tqdm import tqdm
 
 from xturing.model_apis import TextGenerationAPI
 from xturing.utils.text_splitter import RecursiveCharacterTextSplitter
 
 
 def instruction_input_suggest(
     original_text: str,
     engine: TextGenerationAPI,
     chunk_size: int = 8000,
     num_samples_per_chunk=7,
 ):
     text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size)
 
     texts = text_splitter.split_text(original_text)
-    print(f"Split the document into {len(texts)} parts")
+    # print(f"Split the document into {len(texts)} parts")
 
     questions = []
     answers = []
     for text in texts:
         prompt = f"""Given  a document. Suggest {num_samples_per_chunk} questions that could be asked related to the document. Generate a comprehensive and informative answer (but no more than 80 words) for each question.
             Document: {text}
             """
 
         outputs = engine.get_completion(prompts=[prompt])
         pairs = outputs.split("\n\n")
         for pair in pairs:
-            question, answer = pair.split("\n")
-            questions.append(question[3:])
-            answers.append(answer)
+            try:
+                question, answer = pair.split("\n")
+                questions.append(question[3:])
+                answers.append(answer)
+            except:
+                continue
     assert len(questions) == len(answers)
     return questions, answers
 
 
 def prepare_seed_tasks(
     data_path, seed_path, engine, chunk_size=8000, num_samples_per_chunk=7
 ):
     instructions = []
     outputs = []
-    for file in os.listdir(data_path):
+    for file in tqdm(os.listdir(data_path)):
         if file[-4:] != ".txt":
             continue
         with open(os.path.join(data_path, file)) as f:
             text = f.read()
 
         pairs = instruction_input_suggest(
             text, engine, chunk_size, num_samples_per_chunk
```

### Comparing `xturing-0.0.8/src/xturing/self_instruct/templates/clf_task_template.py` & `xturing-0.0.9/src/xturing/self_instruct/templates/clf_task_template.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/self_instruct/templates/instance_gen_template.py` & `xturing-0.0.9/src/xturing/self_instruct/templates/instance_gen_template.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/trainers/lightning_trainer.py` & `xturing-0.0.9/src/xturing/trainers/lightning_trainer.py`

 * *Files 8% similar despite different names*

```diff
@@ -22,26 +22,28 @@
         self,
         model_engine: BaseEngine,
         train_dataset: BaseDataset,
         preprocessor: Optional[BasePreprocessor] = None,
         batch_size: int = 2,
         learning_rate: float = 5e-5,
         optimizer_name: str = "adamw",
+        saved_path: str = "saved_model",
     ):
         super().__init__()
         self.model_engine = model_engine
         self.pytorch_model = self.model_engine.model
         self.train_dataset = train_dataset
         self.preprocessor = preprocessor
 
         # Hyperparameters
         self.batch_size = batch_size
         self.learning_rate = learning_rate
 
         self.optimizer_name = optimizer_name
+        self.saved_path = saved_path
 
         self.losses = []
 
     def configure_optimizers(self):
         if self.optimizer_name == "adamw":
             optimizer = torch.optim.AdamW(
                 self.pytorch_model.parameters(), lr=self.learning_rate
@@ -75,14 +77,17 @@
         self.log("loss", loss.item(), prog_bar=True)
 
         return loss
 
     def validation_step(self, batch, batch_idx):
         return self.model_engine.validation_step(batch)
 
+    def on_save_checkpoint(self, checkpoint):
+        self.model_engine.save(self.saved_path)
+
 
 class LightningTrainer:
     config_name: str = "lightning_trainer"
 
     def __init__(
         self,
         model_engine: BaseEngine,
```

### Comparing `xturing-0.0.8/src/xturing/ui/playground.py` & `xturing-0.0.9/src/xturing/ui/playground.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/utils/hub.py` & `xturing-0.0.9/src/xturing/utils/hub.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/utils/logging.py` & `xturing-0.0.9/src/xturing/utils/logging.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/utils/loss_fns.py` & `xturing-0.0.9/src/xturing/utils/loss_fns.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/utils/notebooks.py` & `xturing-0.0.9/src/xturing/utils/notebooks.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/utils/text_splitter.py` & `xturing-0.0.9/src/xturing/utils/text_splitter.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing/utils/utils.py` & `xturing-0.0.9/src/xturing/utils/utils.py`

 * *Files identical despite different names*

### Comparing `xturing-0.0.8/src/xturing.egg-info/PKG-INFO` & `xturing-0.0.9/src/xturing.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xturing
-Version: 0.0.8
+Version: 0.0.9
 Summary: Fine-tuning, evaluation and data generation for LLMs
 Author-email: Glenn Ko <glenn@stochastic.ai>, Yuji Chai <yuji.chai@stochastic.ai>, Roman Ageev <roman.ageev@stochastic.ai>, Toan Do <toan.do@stochastic.ai>, Marcos R M <marcos.rm@stochastic.ai>, Sarthak Langde <sarthak.langde@stochastic.ai>, Riccardo Romagnoli <riccardo.romagnoli@stochastic.ai>, Subhash G N <subhash.gn@stochastic.ai>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
         
            TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
@@ -241,15 +241,15 @@
 ensuring data privacy and security.
 
 With `xturing` you can,
 - Ingest data from different sources and preprocess them to a format LLMs can understand
 - Scale from single to multiple GPUs for faster fine-tuning
 - Leverage memory-efficient techniques (i.e. LoRA fine-tuning) to reduce your hardware costs by up to 90% of the time
 - Explore different fine-tuning methods and benchmark them to find the best performing model
-- Evalate fine-tuned models on well-defined metrics for in-depth analysis
+- Evaluate fine-tuned models on well-defined metrics for in-depth analysis
 
 <br>
 <p align="center">
   <a href="https://pypi.org/project/xturing/">
     <img src="https://img.shields.io/pypi/v/xturing?style=for-the-badge" />
   </a>
   <a href="https://xturing.stochastic.ai/">
```

### Comparing `xturing-0.0.8/src/xturing.egg-info/SOURCES.txt` & `xturing-0.0.9/src/xturing.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -36,14 +36,16 @@
 src/xturing/engines/gptj_engine.py
 src/xturing/engines/llama_engine.py
 src/xturing/engines/opt_engine.py
 src/xturing/engines/gptj_utils/__init__.py
 src/xturing/engines/gptj_utils/gptj.py
 src/xturing/engines/llama_utils/__init__.py
 src/xturing/engines/llama_utils/llama.py
+src/xturing/engines/lora_engine/__init__.py
+src/xturing/engines/lora_engine/lora.py
 src/xturing/model_apis/__init__.py
 src/xturing/model_apis/ai21.py
 src/xturing/model_apis/base.py
 src/xturing/model_apis/cohere.py
 src/xturing/model_apis/openai.py
 src/xturing/models/__init__.py
 src/xturing/models/base.py
```

