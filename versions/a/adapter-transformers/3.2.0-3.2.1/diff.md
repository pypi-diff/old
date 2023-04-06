# Comparing `tmp/adapter-transformers-3.2.0.tar.gz` & `tmp/adapter-transformers-3.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "adapter-transformers-3.2.0.tar", last modified: Fri Mar  3 13:48:09 2023, max compression
+gzip compressed data, was "adapter-transformers-3.2.1.tar", last modified: Thu Apr  6 21:08:04 2023, max compression
```

## Comparing `adapter-transformers-3.2.0.tar` & `adapter-transformers-3.2.1.tar`

### file list

```diff
@@ -1,1454 +1,1454 @@
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.618223 adapter-transformers-3.2.0/
--rw-r--r--   0 hsterz     (501) staff       (20)    11446 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/LICENSE
--rw-r--r--   0 hsterz     (501) staff       (20)       16 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/MANIFEST.in
--rw-r--r--   0 hsterz     (501) staff       (20)     8806 2023-03-03 13:48:09.618348 adapter-transformers-3.2.0/PKG-INFO
--rw-r--r--   0 hsterz     (501) staff       (20)     6626 2023-02-27 16:08:57.000000 adapter-transformers-3.2.0/README.md
--rw-r--r--   0 hsterz     (501) staff       (20)       57 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/pyproject.toml
--rw-r--r--   0 hsterz     (501) staff       (20)      817 2023-03-03 13:48:09.618712 adapter-transformers-3.2.0/setup.cfg
--rw-r--r--   0 hsterz     (501) staff       (20)    15804 2023-03-03 13:34:41.000000 adapter-transformers-3.2.0/setup.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.272430 adapter-transformers-3.2.0/src/
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.296919 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/
--rw-r--r--   0 hsterz     (501) staff       (20)     8806 2023-03-03 13:48:09.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/PKG-INFO
--rw-r--r--   0 hsterz     (501) staff       (20)    68639 2023-03-03 13:48:09.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/SOURCES.txt
--rw-r--r--   0 hsterz     (501) staff       (20)        1 2023-03-03 13:48:09.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/dependency_links.txt
--rw-r--r--   0 hsterz     (501) staff       (20)       81 2023-03-03 13:48:09.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/entry_points.txt
--rw-r--r--   0 hsterz     (501) staff       (20)        1 2023-01-11 19:07:11.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/not-zip-safe
--rw-r--r--   0 hsterz     (501) staff       (20)     6766 2023-03-03 13:48:09.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/requires.txt
--rw-r--r--   0 hsterz     (501) staff       (20)       13 2023-03-03 13:48:09.000000 adapter-transformers-3.2.0/src/adapter_transformers.egg-info/top_level.txt
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.317088 adapter-transformers-3.2.0/src/transformers/
--rwxr-xr-x   0 hsterz     (501) staff       (20)   249393 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6568 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/activations.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4313 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/activations_tf.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.322302 adapter-transformers-3.2.0/src/transformers/adapters/
--rw-r--r--   0 hsterz     (501) staff       (20)     7275 2023-03-03 13:34:44.000000 adapter-transformers-3.2.0/src/transformers/adapters/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7707 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/composition.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37267 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/configuration.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4553 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/context.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15810 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/head_utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.323156 adapter-transformers-3.2.0/src/transformers/adapters/heads/
--rw-r--r--   0 hsterz     (501) staff       (20)      151 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/heads/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    35900 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/heads/base.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6281 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/heads/dependency_parsing.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7138 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/heads/language_modeling.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8742 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/hub_mixin.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28475 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/layer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33112 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/loading.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16292 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/lora.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.325526 adapter-transformers-3.2.0/src/transformers/adapters/mixins/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1332 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/albert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1766 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/bart.py
--rw-r--r--   0 hsterz     (501) staff       (20)      923 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/beit.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1236 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1797 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1107 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/distilbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2300 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1029 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/gpt2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1029 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/gptj.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1383 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/t5.py
--rw-r--r--   0 hsterz     (501) staff       (20)      951 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/mixins/vit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    54590 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/adapters/model_mixin.py
--rw-r--r--   0 hsterz     (501) staff       (20)    30755 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/modeling.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.325700 adapter-transformers-3.2.0/src/transformers/adapters/models/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/__init__.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.326001 adapter-transformers-3.2.0/src/transformers/adapters/models/albert/
--rw-r--r--   0 hsterz     (501) staff       (20)     1133 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/albert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7750 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/albert/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.326337 adapter-transformers-3.2.0/src/transformers/adapters/models/auto/
--rw-r--r--   0 hsterz     (501) staff       (20)     1312 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/auto/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2794 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/auto/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.326693 adapter-transformers-3.2.0/src/transformers/adapters/models/bart/
--rw-r--r--   0 hsterz     (501) staff       (20)     1194 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/bart/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9588 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/bart/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.327057 adapter-transformers-3.2.0/src/transformers/adapters/models/beit/
--rw-r--r--   0 hsterz     (501) staff       (20)     1129 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/beit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4156 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/beit/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.327549 adapter-transformers-3.2.0/src/transformers/adapters/models/bert/
--rw-r--r--   0 hsterz     (501) staff       (20)     1194 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/bert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11517 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/bert/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.327942 adapter-transformers-3.2.0/src/transformers/adapters/models/bert_generation/
--rw-r--r--   0 hsterz     (501) staff       (20)     1149 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/bert_generation/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5883 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/bert_generation/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.328342 adapter-transformers-3.2.0/src/transformers/adapters/models/deberta/
--rw-r--r--   0 hsterz     (501) staff       (20)     1135 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/deberta/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6627 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/deberta/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.328735 adapter-transformers-3.2.0/src/transformers/adapters/models/debertaV2/
--rw-r--r--   0 hsterz     (501) staff       (20)     1139 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/debertaV2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7613 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/debertaV2/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.329113 adapter-transformers-3.2.0/src/transformers/adapters/models/distilbert/
--rw-r--r--   0 hsterz     (501) staff       (20)     1218 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/distilbert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11758 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/distilbert/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.329578 adapter-transformers-3.2.0/src/transformers/adapters/models/gpt2/
--rw-r--r--   0 hsterz     (501) staff       (20)     1194 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/gpt2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8569 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/gpt2/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.329935 adapter-transformers-3.2.0/src/transformers/adapters/models/gptj/
--rw-r--r--   0 hsterz     (501) staff       (20)     1129 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/gptj/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7516 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/gptj/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.330345 adapter-transformers-3.2.0/src/transformers/adapters/models/mbart/
--rw-r--r--   0 hsterz     (501) staff       (20)     1198 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/mbart/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9571 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/mbart/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.330732 adapter-transformers-3.2.0/src/transformers/adapters/models/roberta/
--rw-r--r--   0 hsterz     (501) staff       (20)     1206 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/roberta/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11589 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/roberta/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.331102 adapter-transformers-3.2.0/src/transformers/adapters/models/t5/
--rw-r--r--   0 hsterz     (501) staff       (20)     1186 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/t5/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8402 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/t5/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.331469 adapter-transformers-3.2.0/src/transformers/adapters/models/vit/
--rw-r--r--   0 hsterz     (501) staff       (20)     1127 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/vit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4043 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/vit/adapter_model.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.331846 adapter-transformers-3.2.0/src/transformers/adapters/models/xlm_roberta/
--rw-r--r--   0 hsterz     (501) staff       (20)     1218 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/xlm_roberta/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1048 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/models/xlm_roberta/adapter_model.py
--rw-r--r--   0 hsterz     (501) staff       (20)    30155 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/prefix_tuning.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12728 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/adapters/trainer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4207 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/training.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32713 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.332207 adapter-transformers-3.2.0/src/transformers/adapters/wrappers/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/wrappers/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3919 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/adapters/wrappers/configuration.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.333595 adapter-transformers-3.2.0/src/transformers/benchmark/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/benchmark/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10753 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/benchmark/benchmark.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3891 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_args.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4736 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_args_tf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6425 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_args_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13066 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_tf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37621 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.336863 adapter-transformers-3.2.0/src/transformers/commands/
--rw-r--r--   0 hsterz     (501) staff       (20)      923 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/commands/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11064 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/add_new_model.py
--rw-r--r--   0 hsterz     (501) staff       (20)    67351 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/commands/add_new_model_like.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7856 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/convert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1860 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/commands/download.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3319 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/commands/env.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8001 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/lfs.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19003 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/commands/pt_to_tf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4249 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/run.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8027 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/serving.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6329 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/train.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2047 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/transformers_cli.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7124 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/commands/user.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    49830 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/configuration_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20903 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/convert_graph_to_onnx.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    16632 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/convert_pytorch_checkpoint_to_tf2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    46337 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/convert_slow_tokenizer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     4982 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/convert_slow_tokenizers_checkpoints_to_fast.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2899 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/convert_tf_hub_seq_to_seq_bert_to_pytorch.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.337884 adapter-transformers-3.2.0/src/transformers/data/
--rw-r--r--   0 hsterz     (501) staff       (20)     1594 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    76779 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/data/data_collator.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.338683 adapter-transformers-3.2.0/src/transformers/data/datasets/
--rw-r--r--   0 hsterz     (501) staff       (20)     1080 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/data/datasets/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6165 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/datasets/glue.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23723 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/datasets/language_modeling.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9220 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/datasets/squad.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.338997 adapter-transformers-3.2.0/src/transformers/data/metrics/
--rw-r--r--   0 hsterz     (501) staff       (20)     3776 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/metrics/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    29698 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/data/metrics/squad_metrics.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.339990 adapter-transformers-3.2.0/src/transformers/data/processors/
--rw-r--r--   0 hsterz     (501) staff       (20)     1185 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/data/processors/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23219 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/processors/glue.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33154 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/processors/squad.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13829 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/processors/utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3489 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/processors/xnli.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3433 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/data/test_generation_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12907 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/debug_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15835 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/deepspeed.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1756 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/dependency_versions_check.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3401 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/dependency_versions_table.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19064 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/dynamic_module_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17982 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/feature_extraction_sequence_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    26314 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/feature_extraction_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3738 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/file_utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.343131 adapter-transformers-3.2.0/src/transformers/generation/
--rw-r--r--   0 hsterz     (501) staff       (20)     9479 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19097 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/beam_constraints.py
--rw-r--r--   0 hsterz     (501) staff       (20)    42653 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/beam_search.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36470 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/configuration_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10839 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/flax_logits_process.py
--rw-r--r--   0 hsterz     (501) staff       (20)    42338 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/flax_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    43968 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/logits_process.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5510 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/stopping_criteria.py
--rw-r--r--   0 hsterz     (501) staff       (20)    27539 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/tf_logits_process.py
--rw-r--r--   0 hsterz     (501) staff       (20)   156300 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/tf_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)   212677 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation/utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1118 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation_flax_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1109 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation_tf_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1126 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/generation_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18952 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/hf_argparser.py
--rw-r--r--   0 hsterz     (501) staff       (20)    24681 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/image_processing_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    29183 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/image_transforms.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22352 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/image_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    65749 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/integrations.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20709 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/keras_callbacks.py
--rw-r--r--   0 hsterz     (501) staff       (20)    34991 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modelcard.py
--rw-r--r--   0 hsterz     (501) staff       (20)    38967 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/modeling_flax_outputs.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15034 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/modeling_flax_pytorch_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    54824 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modeling_flax_utils.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    85679 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modeling_outputs.py
--rw-r--r--   0 hsterz     (501) staff       (20)    54504 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modeling_tf_outputs.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21162 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modeling_tf_pytorch_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)   151710 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modeling_tf_utils.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   163219 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/modeling_utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.343524 adapter-transformers-3.2.0/src/transformers/models/
--rw-r--r--   0 hsterz     (501) staff       (20)     3334 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/__init__.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.346513 adapter-transformers-3.2.0/src/transformers/models/albert/
--rw-r--r--   0 hsterz     (501) staff       (20)     5653 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/albert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8567 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/albert/configuration_albert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2183 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/albert/convert_albert_original_tf_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    62818 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/albert/modeling_albert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    40773 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/albert/modeling_flax_albert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    67264 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/albert/modeling_tf_albert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15428 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/albert/tokenization_albert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10814 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/albert/tokenization_albert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.347371 adapter-transformers-3.2.0/src/transformers/models/altclip/
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2334 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/altclip/__init__.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    16597 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/altclip/configuration_altclip.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    78432 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/altclip/modeling_altclip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6444 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/altclip/processing_altclip.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.348327 adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2678 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5649 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/configuration_audio_spectrogram_transformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11052 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/convert_audio_spectrogram_transformer_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8308 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/feature_extraction_audio_spectrogram_transformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    26058 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/modeling_audio_spectrogram_transformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.350749 adapter-transformers-3.2.0/src/transformers/models/auto/
--rw-r--r--   0 hsterz     (501) staff       (20)    14165 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36525 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/auto_factory.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    39581 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/configuration_auto.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18660 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/feature_extraction_auto.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19712 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/image_processing_auto.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    50608 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/modeling_auto.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13498 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/modeling_flax_auto.py
--rw-r--r--   0 hsterz     (501) staff       (20)    24852 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/modeling_tf_auto.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15137 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/processing_auto.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37596 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/auto/tokenization_auto.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.353412 adapter-transformers-3.2.0/src/transformers/models/bart/
--rw-r--r--   0 hsterz     (501) staff       (20)     4504 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bart/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18992 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bart/configuration_bart.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5647 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    92301 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bart/modeling_bart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    82685 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bart/modeling_flax_bart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    77193 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bart/modeling_tf_bart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17972 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bart/tokenization_bart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13803 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bart/tokenization_bart_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.353884 adapter-transformers-3.2.0/src/transformers/models/barthez/
--rw-r--r--   0 hsterz     (501) staff       (20)     2020 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/barthez/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13192 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/barthez/tokenization_barthez.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8899 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/barthez/tokenization_barthez_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.354196 adapter-transformers-3.2.0/src/transformers/models/bartpho/
--rw-r--r--   0 hsterz     (501) staff       (20)     1533 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bartpho/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14218 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bartpho/tokenization_bartpho.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.355819 adapter-transformers-3.2.0/src/transformers/models/beit/
--rw-r--r--   0 hsterz     (501) staff       (20)     3460 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/beit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9641 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/beit/configuration_beit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16496 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/beit/convert_beit_unilm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/beit/feature_extraction_beit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    24737 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/beit/image_processing_beit.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    55360 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/beit/modeling_beit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37004 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/beit/modeling_flax_beit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.358803 adapter-transformers-3.2.0/src/transformers/models/bert/
--rw-r--r--   0 hsterz     (501) staff       (20)     6228 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10149 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert/configuration_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10490 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_original_tf2_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2159 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4101 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_pytorch_checkpoint_to_original_tf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7606 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_token_dropping_original_tf2_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    86400 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert/modeling_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    63605 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert/modeling_flax_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    93219 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert/modeling_tf_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    24516 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/tokenization_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14870 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/tokenization_bert_fast.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11009 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert/tokenization_bert_tf.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.359775 adapter-transformers-3.2.0/src/transformers/models/bert_generation/
--rw-r--r--   0 hsterz     (501) staff       (20)     2446 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert_generation/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6227 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert_generation/configuration_bert_generation.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    49793 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert_generation/modeling_bert_generation.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7139 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert_generation/tokenization_bert_generation.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.360155 adapter-transformers-3.2.0/src/transformers/models/bert_japanese/
--rw-r--r--   0 hsterz     (501) staff       (20)     1224 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bert_japanese/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    39624 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bert_japanese/tokenization_bert_japanese.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.360598 adapter-transformers-3.2.0/src/transformers/models/bertweet/
--rw-r--r--   0 hsterz     (501) staff       (20)     1130 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bertweet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    27205 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bertweet/tokenization_bertweet.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.362485 adapter-transformers-3.2.0/src/transformers/models/big_bird/
--rw-r--r--   0 hsterz     (501) staff       (20)     4745 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8305 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/configuration_big_bird.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2494 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/convert_bigbird_original_tf_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   142147 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/modeling_big_bird.py
--rw-r--r--   0 hsterz     (501) staff       (20)   106503 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/modeling_flax_big_bird.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14684 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/tokenization_big_bird.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11365 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/big_bird/tokenization_big_bird_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.363550 adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/
--rw-r--r--   0 hsterz     (501) staff       (20)     2487 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19801 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/configuration_bigbird_pegasus.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6295 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/convert_bigbird_pegasus_tf_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   147127 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/modeling_bigbird_pegasus.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.365644 adapter-transformers-3.2.0/src/transformers/models/biogpt/
--rw-r--r--   0 hsterz     (501) staff       (20)     2096 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/biogpt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6600 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/biogpt/configuration_biogpt.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    10579 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/biogpt/convert_biogpt_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    32805 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/biogpt/modeling_biogpt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13737 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/biogpt/tokenization_biogpt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.366601 adapter-transformers-3.2.0/src/transformers/models/bit/
--rw-r--r--   0 hsterz     (501) staff       (20)     2452 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5868 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bit/configuration_bit.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5955 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bit/convert_bit_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16153 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bit/image_processing_bit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32427 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bit/modeling_bit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.368280 adapter-transformers-3.2.0/src/transformers/models/blenderbot/
--rw-r--r--   0 hsterz     (501) staff       (20)     4202 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19015 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/configuration_blenderbot.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3702 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/convert_blenderbot_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    76930 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/modeling_blenderbot.py
--rw-r--r--   0 hsterz     (501) staff       (20)    64957 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/modeling_flax_blenderbot.py
--rw-r--r--   0 hsterz     (501) staff       (20)    70073 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/modeling_tf_blenderbot.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19479 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/tokenization_blenderbot.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14196 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot/tokenization_blenderbot_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.370206 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/
--rw-r--r--   0 hsterz     (501) staff       (20)     4434 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18478 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/configuration_blenderbot_small.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    75703 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/modeling_blenderbot_small.py
--rw-r--r--   0 hsterz     (501) staff       (20)    65922 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/modeling_flax_blenderbot_small.py
--rw-r--r--   0 hsterz     (501) staff       (20)    69400 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/modeling_tf_blenderbot_small.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8647 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/tokenization_blenderbot_small.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4057 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/tokenization_blenderbot_small_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.371814 adapter-transformers-3.2.0/src/transformers/models/blip/
--rw-r--r--   0 hsterz     (501) staff       (20)     2845 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18239 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/configuration_blip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6980 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/convert_blip_original_pytorch_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13922 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/image_processing_blip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    62303 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/modeling_blip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    41581 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/modeling_blip_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6152 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/blip/processing_blip.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.372819 adapter-transformers-3.2.0/src/transformers/models/bloom/
--rw-r--r--   0 hsterz     (501) staff       (20)     2670 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bloom/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10792 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bloom/configuration_bloom.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10313 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bloom/convert_bloom_original_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    56666 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/bloom/modeling_bloom.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7263 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bloom/tokenization_bloom_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.373117 adapter-transformers-3.2.0/src/transformers/models/bort/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/bort/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14057 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/bort/convert_bort_original_gluonnlp_checkpoint_to_pytorch.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.374000 adapter-transformers-3.2.0/src/transformers/models/byt5/
--rw-r--r--   0 hsterz     (501) staff       (20)     1113 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/byt5/__init__.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2120 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/byt5/convert_byt5_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10726 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/byt5/tokenization_byt5.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.375750 adapter-transformers-3.2.0/src/transformers/models/camembert/
--rw-r--r--   0 hsterz     (501) staff       (20)     4614 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/camembert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7734 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/camembert/configuration_camembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    73249 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/camembert/modeling_camembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    80894 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/camembert/modeling_tf_camembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13580 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/camembert/tokenization_camembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8657 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/camembert/tokenization_camembert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.377085 adapter-transformers-3.2.0/src/transformers/models/canine/
--rw-r--r--   0 hsterz     (501) staff       (20)     2443 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/canine/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6477 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/canine/configuration_canine.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2118 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/canine/convert_canine_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    73780 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/canine/modeling_canine.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9275 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/canine/tokenization_canine.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.378354 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/
--rw-r--r--   0 hsterz     (501) staff       (20)     3090 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19075 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/configuration_chinese_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5070 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/convert_chinese_clip_original_pytorch_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1247 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/feature_extraction_chinese_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15803 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/image_processing_chinese_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    73449 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/modeling_chinese_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6754 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/chinese_clip/processing_chinese_clip.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.380790 adapter-transformers-3.2.0/src/transformers/models/clip/
--rw-r--r--   0 hsterz     (501) staff       (20)     5198 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17889 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/configuration_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5248 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/clip/convert_clip_original_pytorch_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/feature_extraction_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16184 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/image_processing_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    58772 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/modeling_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    45841 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/modeling_flax_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    57673 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/modeling_tf_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6821 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/processing_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20441 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/tokenization_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6955 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clip/tokenization_clip_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.381925 adapter-transformers-3.2.0/src/transformers/models/clipseg/
--rw-r--r--   0 hsterz     (501) staff       (20)     2350 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clipseg/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17992 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clipseg/configuration_clipseg.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11124 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clipseg/convert_clipseg_original_pytorch_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    64567 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clipseg/modeling_clipseg.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7838 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/clipseg/processing_clipseg.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.383034 adapter-transformers-3.2.0/src/transformers/models/codegen/
--rw-r--r--   0 hsterz     (501) staff       (20)     2614 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/codegen/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10548 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/codegen/configuration_codegen.py
--rw-r--r--   0 hsterz     (501) staff       (20)    31438 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/codegen/modeling_codegen.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15112 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/codegen/tokenization_codegen.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10506 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/codegen/tokenization_codegen_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.384224 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/
--rw-r--r--   0 hsterz     (501) staff       (20)     2996 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12597 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/configuration_conditional_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15946 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/convert_conditional_detr_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1251 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/feature_extraction_conditional_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    72489 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/image_processing_conditional_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)   127554 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/conditional_detr/modeling_conditional_detr.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.386499 adapter-transformers-3.2.0/src/transformers/models/convbert/
--rw-r--r--   0 hsterz     (501) staff       (20)     4240 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7311 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/configuration_convbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2108 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/convert_convbert_original_tf1_checkpoint_to_pytorch_and_tf2.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    59172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/modeling_convbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    56248 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/modeling_tf_convbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21308 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/tokenization_convbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8764 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/convbert/tokenization_convbert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.388108 adapter-transformers-3.2.0/src/transformers/models/convnext/
--rw-r--r--   0 hsterz     (501) staff       (20)     3355 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5834 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/configuration_convnext.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10234 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/convert_convnext_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1200 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/feature_extraction_convnext.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15130 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/image_processing_convnext.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    22560 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/modeling_convnext.py
--rw-r--r--   0 hsterz     (501) staff       (20)    25063 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/convnext/modeling_tf_convnext.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.388749 adapter-transformers-3.2.0/src/transformers/models/cpm/
--rw-r--r--   0 hsterz     (501) staff       (20)     1987 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/cpm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15153 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/cpm/tokenization_cpm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10679 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/cpm/tokenization_cpm_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.390142 adapter-transformers-3.2.0/src/transformers/models/ctrl/
--rw-r--r--   0 hsterz     (501) staff       (20)     2859 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/ctrl/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5170 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/ctrl/configuration_ctrl.py
--rw-r--r--   0 hsterz     (501) staff       (20)    34887 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/ctrl/modeling_ctrl.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37094 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/ctrl/modeling_tf_ctrl.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8498 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/ctrl/tokenization_ctrl.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.391524 adapter-transformers-3.2.0/src/transformers/models/cvt/
--rw-r--r--   0 hsterz     (501) staff       (20)     2605 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/cvt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6859 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/cvt/configuration_cvt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13579 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/cvt/convert_cvt_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28913 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/cvt/modeling_cvt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37443 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/cvt/modeling_tf_cvt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.394609 adapter-transformers-3.2.0/src/transformers/models/data2vec/
--rw-r--r--   0 hsterz     (501) staff       (20)     5104 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16244 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/configuration_data2vec_audio.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7419 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/configuration_data2vec_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9432 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/configuration_data2vec_vision.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10858 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/convert_data2vec_audio_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9613 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/convert_data2vec_text_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    15350 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/convert_data2vec_vision_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    65791 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_data2vec_audio.py
--rw-r--r--   0 hsterz     (501) staff       (20)    72297 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_data2vec_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)    52885 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_data2vec_vision.py
--rw-r--r--   0 hsterz     (501) staff       (20)    62599 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_tf_data2vec_vision.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.396885 adapter-transformers-3.2.0/src/transformers/models/deberta/
--rw-r--r--   0 hsterz     (501) staff       (20)     3848 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deberta/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9388 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deberta/configuration_deberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    61036 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deberta/modeling_deberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    62889 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deberta/modeling_tf_deberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19780 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deberta/tokenization_deberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13417 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deberta/tokenization_deberta_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.398832 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/
--rw-r--r--   0 hsterz     (501) staff       (20)     4070 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9174 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/configuration_deberta_v2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    71361 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/modeling_deberta_v2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    68994 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/modeling_tf_deberta_v2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21719 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/tokenization_deberta_v2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10996 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deberta_v2/tokenization_deberta_v2_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.399575 adapter-transformers-3.2.0/src/transformers/models/decision_transformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2332 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/decision_transformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7923 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/decision_transformer/configuration_decision_transformer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    43376 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/decision_transformer/modeling_decision_transformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.401383 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/
--rw-r--r--   0 hsterz     (501) staff       (20)     2767 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13658 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/configuration_deformable_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9493 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/convert_deformable_detr_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1244 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/feature_extraction_deformable_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    59943 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/image_processing_deformable_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1635 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/load_custom.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   118536 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deformable_detr/modeling_deformable_detr.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.403343 adapter-transformers-3.2.0/src/transformers/models/deit/
--rw-r--r--   0 hsterz     (501) staff       (20)     3657 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5960 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deit/configuration_deit.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9231 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/deit/convert_deit_timm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deit/feature_extraction_deit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14941 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deit/image_processing_deit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    38237 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deit/modeling_deit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    45314 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/deit/modeling_tf_deit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.405384 adapter-transformers-3.2.0/src/transformers/models/detr/
--rw-r--r--   0 hsterz     (501) staff       (20)     2606 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12253 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/configuration_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13577 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/convert_detr_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18373 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/convert_detr_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/feature_extraction_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    80473 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/image_processing_detr.py
--rw-r--r--   0 hsterz     (501) staff       (20)   111431 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/detr/modeling_detr.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.405846 adapter-transformers-3.2.0/src/transformers/models/dialogpt/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/dialogpt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1537 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dialogpt/convert_dialogpt_original_pytorch_checkpoint_to_pytorch.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.406587 adapter-transformers-3.2.0/src/transformers/models/dinat/
--rw-r--r--   0 hsterz     (501) staff       (20)     2020 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dinat/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7230 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dinat/configuration_dinat.py
--rw-r--r--   0 hsterz     (501) staff       (20)    42176 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dinat/modeling_dinat.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.409424 adapter-transformers-3.2.0/src/transformers/models/distilbert/
--rw-r--r--   0 hsterz     (501) staff       (20)     5338 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6977 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/configuration_distilbert.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    52049 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/modeling_distilbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32622 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/modeling_flax_distilbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    47551 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/modeling_tf_distilbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23037 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/tokenization_distilbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10707 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/distilbert/tokenization_distilbert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.409763 adapter-transformers-3.2.0/src/transformers/models/dit/
--rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9436 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dit/convert_dit_unilm_to_pytorch.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.411544 adapter-transformers-3.2.0/src/transformers/models/donut/
--rw-r--r--   0 hsterz     (501) staff       (20)     2626 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/donut/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6177 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/donut/configuration_donut_swin.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9324 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/donut/convert_donut_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1179 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/donut/feature_extraction_donut.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20167 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/donut/image_processing_donut.py
--rw-r--r--   0 hsterz     (501) staff       (20)    43503 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/donut/modeling_donut_swin.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8066 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/donut/processing_donut.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.413423 adapter-transformers-3.2.0/src/transformers/models/dpr/
--rw-r--r--   0 hsterz     (501) staff       (20)     4706 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7261 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/configuration_dpr.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6097 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/convert_dpr_original_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28857 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/modeling_dpr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33628 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/modeling_tf_dpr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19821 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/tokenization_dpr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20207 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dpr/tokenization_dpr_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.414851 adapter-transformers-3.2.0/src/transformers/models/dpt/
--rw-r--r--   0 hsterz     (501) staff       (20)     2615 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11301 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/configuration_dpt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13008 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/convert_dpt_hybrid_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11797 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/convert_dpt_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1165 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/feature_extraction_dpt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18288 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/image_processing_dpt.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    54914 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/dpt/modeling_dpt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.416053 adapter-transformers-3.2.0/src/transformers/models/efficientformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2746 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/efficientformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7658 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/efficientformer/configuration_efficientformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9383 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/efficientformer/convert_efficientformer_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16451 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/efficientformer/image_processing_efficientformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33328 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/efficientformer/modeling_efficientformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.418333 adapter-transformers-3.2.0/src/transformers/models/electra/
--rw-r--r--   0 hsterz     (501) staff       (20)     5428 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/electra/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9926 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/electra/configuration_electra.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2862 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/electra/convert_electra_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    75862 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/electra/modeling_electra.py
--rw-r--r--   0 hsterz     (501) staff       (20)    62253 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/electra/modeling_flax_electra.py
--rw-r--r--   0 hsterz     (501) staff       (20)    75779 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/electra/modeling_tf_electra.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22115 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/electra/tokenization_electra.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10494 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/electra/tokenization_electra_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.419465 adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/
--rw-r--r--   0 hsterz     (501) staff       (20)     2622 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4880 2023-02-27 16:08:55.000000 adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/configuration_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36403 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    43810 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/modeling_flax_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36312 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/modeling_tf_encoder_decoder.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.420045 adapter-transformers-3.2.0/src/transformers/models/ernie/
--rw-r--r--   0 hsterz     (501) staff       (20)     2502 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/ernie/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8883 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/ernie/configuration_ernie.py
--rw-r--r--   0 hsterz     (501) staff       (20)    84316 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/ernie/modeling_ernie.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.422376 adapter-transformers-3.2.0/src/transformers/models/esm/
--rw-r--r--   0 hsterz     (501) staff       (20)     3149 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/esm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14752 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/configuration_esm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18476 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/convert_esm.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    56453 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/modeling_esm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    86755 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/modeling_esmfold.py
--rw-r--r--   0 hsterz     (501) staff       (20)    65295 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/modeling_tf_esm.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.425453 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/
--rw-r--r--   0 hsterz     (501) staff       (20)      461 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14396 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/chunk_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3764 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/data_transforms.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8376 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/feats.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3708 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/loss.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11490 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/protein.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37969 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/residue_constants.py
--rw-r--r--   0 hsterz     (501) staff       (20)    41122 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/rigid_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4798 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/tensor_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5607 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/esm/tokenization_esm.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.427239 adapter-transformers-3.2.0/src/transformers/models/flaubert/
--rw-r--r--   0 hsterz     (501) staff       (20)     3659 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/flaubert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11705 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/flaubert/configuration_flaubert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    57835 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flaubert/modeling_flaubert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    56750 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flaubert/modeling_tf_flaubert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    24039 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/flaubert/tokenization_flaubert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.429567 adapter-transformers-3.2.0/src/transformers/models/flava/
--rw-r--r--   0 hsterz     (501) staff       (20)     3201 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flava/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    30829 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flava/configuration_flava.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3428 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/flava/convert_dalle_to_flava_codebook.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4372 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/flava/convert_flava_original_pytorch_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1201 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flava/feature_extraction_flava.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36921 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flava/image_processing_flava.py
--rw-r--r--   0 hsterz     (501) staff       (20)    96550 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flava/modeling_flava.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6773 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/flava/processing_flava.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.430966 adapter-transformers-3.2.0/src/transformers/models/fnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     3350 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/fnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5838 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/fnet/configuration_fnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6912 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/fnet/convert_fnet_original_flax_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    49516 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/fnet/modeling_fnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15646 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/fnet/tokenization_fnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8557 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/fnet/tokenization_fnet_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.432419 adapter-transformers-3.2.0/src/transformers/models/fsmt/
--rw-r--r--   0 hsterz     (501) staff       (20)     1846 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/fsmt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10578 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/fsmt/configuration_fsmt.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    11265 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/fsmt/convert_fsmt_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    58257 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/fsmt/modeling_fsmt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20145 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/fsmt/tokenization_fsmt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.434321 adapter-transformers-3.2.0/src/transformers/models/funnel/
--rw-r--r--   0 hsterz     (501) staff       (20)     4297 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9141 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/configuration_funnel.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2335 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/convert_funnel_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    69844 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/modeling_funnel.py
--rw-r--r--   0 hsterz     (501) staff       (20)    74284 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/modeling_tf_funnel.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23461 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/tokenization_funnel.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11793 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/funnel/tokenization_funnel_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.435641 adapter-transformers-3.2.0/src/transformers/models/git/
--rw-r--r--   0 hsterz     (501) staff       (20)     2059 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/git/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12726 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/git/configuration_git.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21976 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/git/convert_git_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    68444 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/git/modeling_git.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5486 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/git/processing_git.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.436939 adapter-transformers-3.2.0/src/transformers/models/glpn/
--rw-r--r--   0 hsterz     (501) staff       (20)     2592 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/glpn/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6182 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/glpn/configuration_glpn.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8574 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/glpn/convert_glpn_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/glpn/feature_extraction_glpn.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8920 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/glpn/image_processing_glpn.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    31526 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/glpn/modeling_glpn.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.438971 adapter-transformers-3.2.0/src/transformers/models/gpt2/
--rw-r--r--   0 hsterz     (501) staff       (20)     4771 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12142 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/configuration_gpt2.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2532 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/convert_gpt2_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    31961 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/modeling_flax_gpt2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    70802 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/modeling_gpt2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    55948 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/modeling_tf_gpt2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14416 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/tokenization_gpt2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8045 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/tokenization_gpt2_fast.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3764 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt2/tokenization_gpt2_tf.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.440361 adapter-transformers-3.2.0/src/transformers/models/gpt_neo/
--rw-r--r--   0 hsterz     (501) staff       (20)     2729 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neo/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11823 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neo/configuration_gpt_neo.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2589 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neo/convert_gpt_neo_mesh_tf_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28080 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neo/modeling_flax_gpt_neo.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    39924 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neo/modeling_gpt_neo.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.441403 adapter-transformers-3.2.0/src/transformers/models/gpt_neox/
--rw-r--r--   0 hsterz     (501) staff       (20)     2512 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5791 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox/configuration_gpt_neox.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    31473 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox/modeling_gpt_neox.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5788 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox/tokenization_gpt_neox_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.442426 adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/
--rw-r--r--   0 hsterz     (501) staff       (20)     2325 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5946 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/configuration_gpt_neox_japanese.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    32478 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/modeling_gpt_neox_japanese.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17327 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/tokenization_gpt_neox_japanese.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.443334 adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/
--rw-r--r--   0 hsterz     (501) staff       (20)     1533 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8157 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/convert_megatron_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13176 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/tokenization_gpt_sw3.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.444664 adapter-transformers-3.2.0/src/transformers/models/gptj/
--rw-r--r--   0 hsterz     (501) staff       (20)     3451 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gptj/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9220 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/gptj/configuration_gptj.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28519 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gptj/modeling_flax_gptj.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    49074 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gptj/modeling_gptj.py
--rw-r--r--   0 hsterz     (501) staff       (20)    47336 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/gptj/modeling_tf_gptj.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.445512 adapter-transformers-3.2.0/src/transformers/models/graphormer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2081 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/graphormer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6198 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/graphormer/collating_graphormer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10611 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/graphormer/configuration_graphormer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    35706 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/graphormer/modeling_graphormer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.446972 adapter-transformers-3.2.0/src/transformers/models/groupvit/
--rw-r--r--   0 hsterz     (501) staff       (20)     3046 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/groupvit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17703 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/groupvit/configuration_groupvit.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9775 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/groupvit/convert_groupvit_nvlab_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    68255 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/groupvit/modeling_groupvit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    82458 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/groupvit/modeling_tf_groupvit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.447806 adapter-transformers-3.2.0/src/transformers/models/herbert/
--rw-r--r--   0 hsterz     (501) staff       (20)     1643 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/herbert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    25124 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/herbert/tokenization_herbert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6549 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/herbert/tokenization_herbert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.449726 adapter-transformers-3.2.0/src/transformers/models/hubert/
--rw-r--r--   0 hsterz     (501) staff       (20)     2707 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14568 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/configuration_hubert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8942 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/convert_distilhubert_original_s3prl_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10380 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/convert_hubert_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2895 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/convert_hubert_original_s3prl_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    57931 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/modeling_hubert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    71597 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/hubert/modeling_tf_hubert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.451616 adapter-transformers-3.2.0/src/transformers/models/ibert/
--rw-r--r--   0 hsterz     (501) staff       (20)     2257 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/ibert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7472 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/ibert/configuration_ibert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    57138 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/ibert/modeling_ibert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    30075 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/ibert/quant_modules.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.453248 adapter-transformers-3.2.0/src/transformers/models/imagegpt/
--rw-r--r--   0 hsterz     (501) staff       (20)     2829 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/imagegpt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8866 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/imagegpt/configuration_imagegpt.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2691 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/imagegpt/convert_imagegpt_original_tf2_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1200 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/imagegpt/feature_extraction_imagegpt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10758 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/imagegpt/image_processing_imagegpt.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    53896 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/imagegpt/modeling_imagegpt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.454692 adapter-transformers-3.2.0/src/transformers/models/jukebox/
--rw-r--r--   0 hsterz     (501) staff       (20)     2255 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/jukebox/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    27959 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/jukebox/configuration_jukebox.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11781 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/jukebox/convert_jukebox.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   119829 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/jukebox/modeling_jukebox.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18055 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/jukebox/tokenization_jukebox.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.456199 adapter-transformers-3.2.0/src/transformers/models/layoutlm/
--rw-r--r--   0 hsterz     (501) staff       (20)     3958 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8547 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlm/configuration_layoutlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    61124 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlm/modeling_layoutlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    69222 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlm/modeling_tf_layoutlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21136 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlm/tokenization_layoutlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8966 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlm/tokenization_layoutlm_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.458328 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/
--rw-r--r--   0 hsterz     (501) staff       (20)     3610 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11246 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/configuration_layoutlmv2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1195 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/feature_extraction_layoutlmv2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11928 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/image_processing_layoutlmv2.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    61474 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/modeling_layoutlmv2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9233 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/processing_layoutlmv2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    71868 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/tokenization_layoutlmv2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    38070 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/tokenization_layoutlmv2_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.460763 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/
--rw-r--r--   0 hsterz     (501) staff       (20)     4683 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13365 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/configuration_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1195 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/feature_extraction_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17477 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/image_processing_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)    61268 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/modeling_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)    71537 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/modeling_tf_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9084 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/processing_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)    72805 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/tokenization_layoutlmv3.py
--rw-r--r--   0 hsterz     (501) staff       (20)    40179 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/tokenization_layoutlmv3_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.461950 adapter-transformers-3.2.0/src/transformers/models/layoutxlm/
--rw-r--r--   0 hsterz     (501) staff       (20)     2208 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/layoutxlm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7910 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutxlm/processing_layoutxlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    57664 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutxlm/tokenization_layoutxlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    39909 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/layoutxlm/tokenization_layoutxlm_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.464372 adapter-transformers-3.2.0/src/transformers/models/led/
--rw-r--r--   0 hsterz     (501) staff       (20)     3179 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/led/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7632 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/led/configuration_led.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   140035 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/led/modeling_led.py
--rw-r--r--   0 hsterz     (501) staff       (20)   118555 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/led/modeling_tf_led.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20397 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/led/tokenization_led.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14862 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/led/tokenization_led_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.465571 adapter-transformers-3.2.0/src/transformers/models/levit/
--rw-r--r--   0 hsterz     (501) staff       (20)     2679 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/levit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5930 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/levit/configuration_levit.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6270 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/levit/convert_levit_timm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1204 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/levit/feature_extraction_levit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17245 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/levit/image_processing_levit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    29583 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/levit/modeling_levit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.466180 adapter-transformers-3.2.0/src/transformers/models/lilt/
--rw-r--r--   0 hsterz     (501) staff       (20)     2080 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/lilt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6877 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/lilt/configuration_lilt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    53707 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/lilt/modeling_lilt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.468387 adapter-transformers-3.2.0/src/transformers/models/longformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     4367 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10523 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/configuration_longformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3027 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/convert_longformer_original_pytorch_lightning_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   114649 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/modeling_longformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)   126969 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/modeling_tf_longformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18732 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/tokenization_longformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14526 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/longformer/tokenization_longformer_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.469455 adapter-transformers-3.2.0/src/transformers/models/longt5/
--rw-r--r--   0 hsterz     (501) staff       (20)     2717 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/longt5/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8481 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/longt5/configuration_longt5.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11088 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/longt5/convert_longt5x_checkpoint_to_flax.py
--rw-r--r--   0 hsterz     (501) staff       (20)   105585 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/longt5/modeling_flax_longt5.py
--rw-r--r--   0 hsterz     (501) staff       (20)   105023 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/longt5/modeling_longt5.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.471037 adapter-transformers-3.2.0/src/transformers/models/luke/
--rw-r--r--   0 hsterz     (501) staff       (20)     2554 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/luke/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6553 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/luke/configuration_luke.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7468 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/luke/convert_luke_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)   103505 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/luke/modeling_luke.py
--rw-r--r--   0 hsterz     (501) staff       (20)    85384 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/luke/tokenization_luke.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.472960 adapter-transformers-3.2.0/src/transformers/models/lxmert/
--rw-r--r--   0 hsterz     (501) staff       (20)     3567 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9510 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/configuration_lxmert.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2109 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/convert_lxmert_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    64980 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/modeling_lxmert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    64272 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/modeling_tf_lxmert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20859 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/tokenization_lxmert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8436 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/lxmert/tokenization_lxmert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.474298 adapter-transformers-3.2.0/src/transformers/models/m2m_100/
--rw-r--r--   0 hsterz     (501) staff       (20)     2163 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/m2m_100/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13559 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/m2m_100/configuration_m2m_100.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3159 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/m2m_100/convert_m2m100_original_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    65752 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/m2m_100/modeling_m2m_100.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17152 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/m2m_100/tokenization_m2m_100.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.476763 adapter-transformers-3.2.0/src/transformers/models/marian/
--rw-r--r--   0 hsterz     (501) staff       (20)     3615 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/marian/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18557 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/marian/configuration_marian.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36254 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/marian/convert_marian_tatoeba_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    26746 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/marian/convert_marian_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    64217 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/marian/modeling_flax_marian.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    82999 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/marian/modeling_marian.py
--rw-r--r--   0 hsterz     (501) staff       (20)    69909 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/marian/modeling_tf_marian.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17415 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/marian/tokenization_marian.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.478722 adapter-transformers-3.2.0/src/transformers/models/markuplm/
--rw-r--r--   0 hsterz     (501) staff       (20)     3014 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7581 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/configuration_markuplm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6400 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/feature_extraction_markuplm.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    58000 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/modeling_markuplm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6346 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/processing_markuplm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    69721 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/tokenization_markuplm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    42802 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/markuplm/tokenization_markuplm_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.479821 adapter-transformers-3.2.0/src/transformers/models/mask2former/
--rw-r--r--   0 hsterz     (501) staff       (20)     2528 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mask2former/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11032 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mask2former/configuration_mask2former.py
--rw-r--r--   0 hsterz     (501) staff       (20)    45711 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mask2former/convert_mask2former_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    51413 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mask2former/image_processing_mask2former.py
--rw-r--r--   0 hsterz     (501) staff       (20)   117435 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mask2former/modeling_mask2former.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.482872 adapter-transformers-3.2.0/src/transformers/models/maskformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     3116 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9434 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/configuration_maskformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6883 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/configuration_maskformer_swin.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32240 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/convert_maskformer_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20748 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/convert_maskformer_resnet_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20337 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/convert_maskformer_swin_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1225 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/feature_extraction_maskformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    54066 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/image_processing_maskformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    89146 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/modeling_maskformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    41270 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/maskformer/modeling_maskformer_swin.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.484862 adapter-transformers-3.2.0/src/transformers/models/mbart/
--rw-r--r--   0 hsterz     (501) staff       (20)     4574 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18386 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/configuration_mbart.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3035 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/convert_mbart_original_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    75068 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/modeling_flax_mbart.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    91818 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/modeling_mbart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    71027 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/modeling_tf_mbart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14713 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/tokenization_mbart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11915 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mbart/tokenization_mbart_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.485453 adapter-transformers-3.2.0/src/transformers/models/mbart50/
--rw-r--r--   0 hsterz     (501) staff       (20)     2018 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mbart50/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16665 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mbart50/tokenization_mbart50.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12198 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mbart50/tokenization_mbart50_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.486755 adapter-transformers-3.2.0/src/transformers/models/mctct/
--rw-r--r--   0 hsterz     (501) staff       (20)     2413 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mctct/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9305 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mctct/configuration_mctct.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16222 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mctct/feature_extraction_mctct.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    34053 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mctct/modeling_mctct.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5928 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mctct/processing_mctct.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.487642 adapter-transformers-3.2.0/src/transformers/models/megatron_bert/
--rw-r--r--   0 hsterz     (501) staff       (20)     2677 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_bert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6572 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_bert/configuration_megatron_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13689 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    83515 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_bert/modeling_megatron_bert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.488588 adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/
--rw-r--r--   0 hsterz     (501) staff       (20)      801 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36287 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/checkpoint_reshaping_and_interoperability.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13632 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/convert_megatron_gpt2_checkpoint.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.489133 adapter-transformers-3.2.0/src/transformers/models/mluke/
--rw-r--r--   0 hsterz     (501) staff       (20)     1527 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mluke/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10186 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mluke/convert_mluke_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    81139 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mluke/tokenization_mluke.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.489779 adapter-transformers-3.2.0/src/transformers/models/mmbt/
--rw-r--r--   0 hsterz     (501) staff       (20)     1650 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mmbt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1605 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mmbt/configuration_mmbt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18887 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mmbt/modeling_mmbt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.491770 adapter-transformers-3.2.0/src/transformers/models/mobilebert/
--rw-r--r--   0 hsterz     (501) staff       (20)     4775 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8585 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/configuration_mobilebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2200 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/convert_mobilebert_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    70780 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/modeling_mobilebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    76785 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/modeling_tf_mobilebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20742 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/tokenization_mobilebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8376 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilebert/tokenization_mobilebert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.492884 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/
--rw-r--r--   0 hsterz     (501) staff       (20)     2906 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5237 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/configuration_mobilenet_v1.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4948 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/convert_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1222 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/feature_extraction_mobilenet_v1.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16205 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/image_processing_mobilenet_v1.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    18777 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/modeling_mobilenet_v1.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.494198 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/
--rw-r--r--   0 hsterz     (501) staff       (20)     3001 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7361 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/configuration_mobilenet_v2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6412 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/convert_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1222 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/feature_extraction_mobilenet_v2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18652 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/image_processing_mobilenet_v2.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    34752 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/modeling_mobilenet_v2.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.495684 adapter-transformers-3.2.0/src/transformers/models/mobilevit/
--rw-r--r--   0 hsterz     (501) staff       (20)     3663 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8400 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/configuration_mobilevit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12418 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/convert_mlcvnets_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1207 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/feature_extraction_mobilevit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16743 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/image_processing_mobilevit.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    40503 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/modeling_mobilevit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    46610 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mobilevit/modeling_tf_mobilevit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.497654 adapter-transformers-3.2.0/src/transformers/models/mpnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     4046 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mpnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5442 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mpnet/configuration_mpnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    42985 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mpnet/modeling_mpnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    53088 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mpnet/modeling_tf_mpnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22022 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mpnet/tokenization_mpnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8930 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mpnet/tokenization_mpnet_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.498884 adapter-transformers-3.2.0/src/transformers/models/mt5/
--rw-r--r--   0 hsterz     (501) staff       (20)     3465 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mt5/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7587 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mt5/configuration_mt5.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4178 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mt5/modeling_flax_mt5.py
--rw-r--r--   0 hsterz     (501) staff       (20)    88845 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mt5/modeling_mt5.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3325 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mt5/modeling_tf_mt5.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.500079 adapter-transformers-3.2.0/src/transformers/models/mvp/
--rw-r--r--   0 hsterz     (501) staff       (20)     2707 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mvp/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8510 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mvp/configuration_mvp.py
--rw-r--r--   0 hsterz     (501) staff       (20)    95195 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/mvp/modeling_mvp.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16814 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mvp/tokenization_mvp.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12079 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/mvp/tokenization_mvp_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.500700 adapter-transformers-3.2.0/src/transformers/models/nat/
--rw-r--r--   0 hsterz     (501) staff       (20)     1984 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/nat/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6864 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/nat/configuration_nat.py
--rw-r--r--   0 hsterz     (501) staff       (20)    40412 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/nat/modeling_nat.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.501308 adapter-transformers-3.2.0/src/transformers/models/nezha/
--rw-r--r--   0 hsterz     (501) staff       (20)     2441 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nezha/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5226 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/nezha/configuration_nezha.py
--rw-r--r--   0 hsterz     (501) staff       (20)    75338 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/nezha/modeling_nezha.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.501931 adapter-transformers-3.2.0/src/transformers/models/nllb/
--rw-r--r--   0 hsterz     (501) staff       (20)     2039 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nllb/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19325 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nllb/tokenization_nllb.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16313 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nllb/tokenization_nllb_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.502756 adapter-transformers-3.2.0/src/transformers/models/nystromformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2545 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nystromformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6622 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nystromformer/configuration_nystromformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4198 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/nystromformer/convert_nystromformer_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    49115 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/nystromformer/modeling_nystromformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.504571 adapter-transformers-3.2.0/src/transformers/models/oneformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2573 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/oneformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12604 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/oneformer/configuration_oneformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    50722 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/oneformer/convert_to_hf_oneformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    55690 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/oneformer/image_processing_oneformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)   141959 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/oneformer/modeling_oneformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9493 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/oneformer/processing_oneformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.505844 adapter-transformers-3.2.0/src/transformers/models/openai/
--rw-r--r--   0 hsterz     (501) staff       (20)     3829 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/openai/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7331 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/openai/configuration_openai.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2666 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/openai/convert_openai_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    38025 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/openai/modeling_openai.py
--rw-r--r--   0 hsterz     (501) staff       (20)    40827 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/openai/modeling_tf_openai.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15034 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/openai/tokenization_openai.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3046 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/openai/tokenization_openai_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.507049 adapter-transformers-3.2.0/src/transformers/models/opt/
--rw-r--r--   0 hsterz     (501) staff       (20)     3148 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/opt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7244 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/opt/configuration_opt.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3018 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/opt/convert_opt_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    31549 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/opt/modeling_flax_opt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    56984 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/opt/modeling_opt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    46429 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/opt/modeling_tf_opt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.509112 adapter-transformers-3.2.0/src/transformers/models/owlvit/
--rw-r--r--   0 hsterz     (501) staff       (20)     3086 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17352 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/configuration_owlvit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13925 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/convert_owlvit_original_flax_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1186 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/feature_extraction_owlvit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23834 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/image_processing_owlvit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    77112 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/modeling_owlvit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11095 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/owlvit/processing_owlvit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.510959 adapter-transformers-3.2.0/src/transformers/models/pegasus/
--rw-r--r--   0 hsterz     (501) staff       (20)     4282 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7692 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/configuration_pegasus.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5362 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/convert_pegasus_tf_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    66012 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/modeling_flax_pegasus.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    81895 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/modeling_pegasus.py
--rw-r--r--   0 hsterz     (501) staff       (20)    70993 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/modeling_tf_pegasus.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13708 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/tokenization_pegasus.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9936 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus/tokenization_pegasus_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.511629 adapter-transformers-3.2.0/src/transformers/models/pegasus_x/
--rw-r--r--   0 hsterz     (501) staff       (20)     2036 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus_x/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8618 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus_x/configuration_pegasus_x.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    79258 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/pegasus_x/modeling_pegasus_x.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.513484 adapter-transformers-3.2.0/src/transformers/models/perceiver/
--rw-r--r--   0 hsterz     (501) staff       (20)     3464 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12098 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/configuration_perceiver.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21293 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/convert_perceiver_haiku_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1207 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/feature_extraction_perceiver.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15612 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/image_processing_perceiver.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   145934 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/modeling_perceiver.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8945 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/perceiver/tokenization_perceiver.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.514232 adapter-transformers-3.2.0/src/transformers/models/phobert/
--rw-r--r--   0 hsterz     (501) staff       (20)     1126 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/phobert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13557 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/phobert/tokenization_phobert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.515677 adapter-transformers-3.2.0/src/transformers/models/plbart/
--rw-r--r--   0 hsterz     (501) staff       (20)     2600 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/plbart/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8718 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/plbart/configuration_plbart.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3553 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/plbart/convert_plbart_original_checkpoint_to_torch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    82743 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/plbart/modeling_plbart.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21655 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/plbart/tokenization_plbart.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.517320 adapter-transformers-3.2.0/src/transformers/models/poolformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2794 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/poolformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5802 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/poolformer/configuration_poolformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7973 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/poolformer/convert_poolformer_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1214 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/poolformer/feature_extraction_poolformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18379 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/poolformer/image_processing_poolformer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    18074 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/poolformer/modeling_poolformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.520289 adapter-transformers-3.2.0/src/transformers/models/prophetnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     2328 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/prophetnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9061 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/prophetnet/configuration_prophetnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7055 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/prophetnet/convert_prophetnet_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)   114040 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/prophetnet/modeling_prophetnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21285 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/prophetnet/tokenization_prophetnet.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.520988 adapter-transformers-3.2.0/src/transformers/models/qdqbert/
--rw-r--r--   0 hsterz     (501) staff       (20)     2573 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/qdqbert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5894 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/qdqbert/configuration_qdqbert.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    77254 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/qdqbert/modeling_qdqbert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.523447 adapter-transformers-3.2.0/src/transformers/models/rag/
--rw-r--r--   0 hsterz     (501) staff       (20)     2597 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rag/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8799 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rag/configuration_rag.py
--rw-r--r--   0 hsterz     (501) staff       (20)    85993 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/rag/modeling_rag.py
--rw-r--r--   0 hsterz     (501) staff       (20)    87645 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/rag/modeling_tf_rag.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28512 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rag/retrieval_rag.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4576 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rag/tokenization_rag.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.524995 adapter-transformers-3.2.0/src/transformers/models/realm/
--rw-r--r--   0 hsterz     (501) staff       (20)     2846 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/realm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8742 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/realm/configuration_realm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    84554 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/realm/modeling_realm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6380 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/realm/retrieval_realm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    25483 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/realm/tokenization_realm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14580 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/realm/tokenization_realm_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.526362 adapter-transformers-3.2.0/src/transformers/models/reformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     3310 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/reformer/__init__.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    13462 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/reformer/configuration_reformer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     7818 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/reformer/convert_reformer_trax_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   115075 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/reformer/modeling_reformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7314 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/reformer/tokenization_reformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4824 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/reformer/tokenization_reformer_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.527886 adapter-transformers-3.2.0/src/transformers/models/regnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     2698 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/regnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4087 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/regnet/configuration_regnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11793 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/regnet/convert_regnet_seer_10b_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18738 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/regnet/convert_regnet_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17533 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/regnet/modeling_regnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21006 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/regnet/modeling_tf_regnet.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.529888 adapter-transformers-3.2.0/src/transformers/models/rembert/
--rw-r--r--   0 hsterz     (501) staff       (20)     4685 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7449 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/configuration_rembert.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2208 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/convert_rembert_tf_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    68009 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/modeling_rembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    76231 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/modeling_tf_rembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10491 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/tokenization_rembert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10432 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/rembert/tokenization_rembert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.530951 adapter-transformers-3.2.0/src/transformers/models/resnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     2796 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/resnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5330 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/resnet/configuration_resnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7310 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/resnet/convert_resnet_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19433 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/resnet/modeling_resnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20470 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/resnet/modeling_tf_resnet.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.532051 adapter-transformers-3.2.0/src/transformers/models/retribert/
--rw-r--r--   0 hsterz     (501) staff       (20)     2521 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/retribert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5404 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/retribert/configuration_retribert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9462 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/retribert/modeling_retribert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22023 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/retribert/tokenization_retribert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9014 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/retribert/tokenization_retribert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.534377 adapter-transformers-3.2.0/src/transformers/models/roberta/
--rw-r--r--   0 hsterz     (501) staff       (20)     5262 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7877 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/configuration_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8002 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/convert_roberta_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    56957 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/modeling_flax_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    73943 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/modeling_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    79324 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/modeling_tf_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17956 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/tokenization_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13674 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roberta/tokenization_roberta_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.535545 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/
--rw-r--r--   0 hsterz     (501) staff       (20)     5562 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8023 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/configuration_roberta_prelayernorm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2975 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/convert_roberta_prelayernorm_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    60529 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/modeling_flax_roberta_prelayernorm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    74674 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/modeling_roberta_prelayernorm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    82354 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/modeling_tf_roberta_prelayernorm.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.536762 adapter-transformers-3.2.0/src/transformers/models/roc_bert/
--rw-r--r--   0 hsterz     (501) staff       (20)     3083 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roc_bert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8656 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roc_bert/configuration_roc_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    93089 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roc_bert/modeling_roc_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    50427 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roc_bert/tokenization_roc_bert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.539215 adapter-transformers-3.2.0/src/transformers/models/roformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     5504 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7710 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/configuration_roformer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2240 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/convert_roformer_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    39460 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/modeling_flax_roformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    69448 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/modeling_roformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    62090 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/modeling_tf_roformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23274 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/tokenization_roformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8277 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/tokenization_roformer_fast.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2652 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/roformer/tokenization_utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.540669 adapter-transformers-3.2.0/src/transformers/models/segformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     3847 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7636 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/configuration_segformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17108 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/convert_segformer_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1207 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/feature_extraction_segformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21425 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/image_processing_segformer.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    35488 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/modeling_segformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    37967 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/segformer/modeling_tf_segformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.541664 adapter-transformers-3.2.0/src/transformers/models/sew/
--rw-r--r--   0 hsterz     (501) staff       (20)     1949 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/sew/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14047 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/sew/configuration_sew.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12744 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/sew/convert_sew_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    52363 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/sew/modeling_sew.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.542875 adapter-transformers-3.2.0/src/transformers/models/sew_d/
--rw-r--r--   0 hsterz     (501) staff       (20)     1975 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/sew_d/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16038 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/sew_d/configuration_sew_d.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13574 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/sew_d/convert_sew_d_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    73091 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/sew_d/modeling_sew_d.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.544275 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/
--rw-r--r--   0 hsterz     (501) staff       (20)     2208 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5087 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/configuration_speech_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14760 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/convert_mbart_wav2vec2_seq2seq_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11984 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/convert_speech_to_text_wav2vec2_seq2seq_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    45066 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/modeling_flax_speech_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32889 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/modeling_speech_encoder_decoder.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.545881 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/
--rw-r--r--   0 hsterz     (501) staff       (20)     4415 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9509 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/configuration_speech_to_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4509 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/convert_s2t_fairseq_to_tfms.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11492 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/feature_extraction_speech_to_text.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    67018 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/modeling_speech_to_text.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    69768 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/modeling_tf_speech_to_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4817 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/processing_speech_to_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11653 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text/tokenization_speech_to_text.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.546942 adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/
--rw-r--r--   0 hsterz     (501) staff       (20)     2337 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6280 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/configuration_speech_to_text_2.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    46179 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/modeling_speech_to_text_2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4789 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/processing_speech_to_text_2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9217 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/tokenization_speech_to_text_2.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.548178 adapter-transformers-3.2.0/src/transformers/models/splinter/
--rw-r--r--   0 hsterz     (501) staff       (20)     2703 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/splinter/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6119 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/splinter/configuration_splinter.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    53606 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/splinter/modeling_splinter.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22013 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/splinter/tokenization_splinter.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9656 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/splinter/tokenization_splinter_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.549118 adapter-transformers-3.2.0/src/transformers/models/squeezebert/
--rw-r--r--   0 hsterz     (501) staff       (20)     3167 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/squeezebert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7909 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/squeezebert/configuration_squeezebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    45098 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/squeezebert/modeling_squeezebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21327 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/squeezebert/tokenization_squeezebert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9396 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/squeezebert/tokenization_squeezebert_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.550679 adapter-transformers-3.2.0/src/transformers/models/swin/
--rw-r--r--   0 hsterz     (501) staff       (20)     2911 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7829 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin/configuration_swin.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6643 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin/convert_swin_simmim_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5817 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/swin/convert_swin_timm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    59833 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin/modeling_swin.py
--rw-r--r--   0 hsterz     (501) staff       (20)    65478 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin/modeling_tf_swin.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.551723 adapter-transformers-3.2.0/src/transformers/models/swin2sr/
--rw-r--r--   0 hsterz     (501) staff       (20)     2485 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin2sr/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6904 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin2sr/configuration_swin2sr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11355 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin2sr/convert_swin2sr_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7762 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin2sr/image_processing_swin2sr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    51633 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swin2sr/modeling_swin2sr.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.552678 adapter-transformers-3.2.0/src/transformers/models/swinv2/
--rw-r--r--   0 hsterz     (501) staff       (20)     2075 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/swinv2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6521 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swinv2/configuration_swinv2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7699 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/swinv2/convert_swinv2_timm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    60852 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/swinv2/modeling_swinv2.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.553785 adapter-transformers-3.2.0/src/transformers/models/switch_transformers/
--rw-r--r--   0 hsterz     (501) staff       (20)     2655 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/switch_transformers/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10086 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/switch_transformers/configuration_switch_transformers.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7649 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/switch_transformers/convert_big_switch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7593 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/switch_transformers/convert_switch_transformers_original_flax_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    89256 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/switch_transformers/modeling_switch_transformers.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.556325 adapter-transformers-3.2.0/src/transformers/models/t5/
--rw-r--r--   0 hsterz     (501) staff       (20)     4439 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/t5/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7430 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/t5/configuration_t5.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2120 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/t5/convert_t5_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10537 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    10365 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/t5/convert_t5x_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    74020 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/t5/modeling_flax_t5.py
--rw-r--r--   0 hsterz     (501) staff       (20)    87946 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/t5/modeling_t5.py
--rw-r--r--   0 hsterz     (501) staff       (20)    75551 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/t5/modeling_tf_t5.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15155 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/t5/tokenization_t5.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10586 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/t5/tokenization_t5_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.557088 adapter-transformers-3.2.0/src/transformers/models/table_transformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2233 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/table_transformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12559 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/table_transformer/configuration_table_transformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15090 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/table_transformer/convert_table_transformer_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    92611 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/table_transformer/modeling_table_transformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.559917 adapter-transformers-3.2.0/src/transformers/models/tapas/
--rw-r--r--   0 hsterz     (501) staff       (20)     3123 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/tapas/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12900 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/tapas/configuration_tapas.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5049 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/tapas/convert_tapas_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)   111502 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/tapas/modeling_tapas.py
--rw-r--r--   0 hsterz     (501) staff       (20)   108613 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/tapas/modeling_tf_tapas.py
--rw-r--r--   0 hsterz     (501) staff       (20)   120557 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/tapas/tokenization_tapas.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.560626 adapter-transformers-3.2.0/src/transformers/models/tapex/
--rw-r--r--   0 hsterz     (501) staff       (20)     1138 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/tapex/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    65000 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/tapex/tokenization_tapex.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.561315 adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2277 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11563 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/configuration_time_series_transformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    92619 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/modeling_time_series_transformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.562326 adapter-transformers-3.2.0/src/transformers/models/timesformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2033 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/timesformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5667 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/timesformer/configuration_timesformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10188 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/timesformer/convert_timesformer_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32941 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/timesformer/modeling_timesformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.563351 adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2284 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7651 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/configuration_trajectory_transformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3139 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    26128 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/modeling_trajectory_transformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.565269 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/
--rw-r--r--   0 hsterz     (501) staff       (20)     3353 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7894 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/configuration_transfo_xl.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     4916 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/convert_transfo_xl_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    47146 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_tf_transfo_xl.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7597 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_tf_transfo_xl_utilities.py
--rw-r--r--   0 hsterz     (501) staff       (20)    55824 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_transfo_xl.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10675 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_transfo_xl_utilities.py
--rw-r--r--   0 hsterz     (501) staff       (20)    30487 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/transfo_xl/tokenization_transfo_xl.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.566146 adapter-transformers-3.2.0/src/transformers/models/trocr/
--rw-r--r--   0 hsterz     (501) staff       (20)     1989 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/trocr/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6975 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/trocr/configuration_trocr.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10163 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/trocr/convert_trocr_unilm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    47404 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/trocr/modeling_trocr.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5687 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/trocr/processing_trocr.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.566964 adapter-transformers-3.2.0/src/transformers/models/unispeech/
--rw-r--r--   0 hsterz     (501) staff       (20)     2189 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16969 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech/configuration_unispeech.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11340 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech/convert_unispeech_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    70135 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech/modeling_unispeech.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.567914 adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/
--rw-r--r--   0 hsterz     (501) staff       (20)     2438 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18392 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/configuration_unispeech_sat.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4870 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/convert_unispeech_original_s3prl_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9289 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/convert_unispeech_sat_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    83730 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/modeling_unispeech_sat.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.569066 adapter-transformers-3.2.0/src/transformers/models/upernet/
--rw-r--r--   0 hsterz     (501) staff       (20)     1743 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/upernet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5438 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/upernet/configuration_upernet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10271 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/upernet/convert_convnext_upernet_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14026 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/upernet/convert_swin_upernet_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17158 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/upernet/modeling_upernet.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.570104 adapter-transformers-3.2.0/src/transformers/models/van/
--rw-r--r--   0 hsterz     (501) staff       (20)     1935 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/van/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4834 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/van/configuration_van.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10386 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/van/convert_van_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21547 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/van/modeling_van.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.571217 adapter-transformers-3.2.0/src/transformers/models/videomae/
--rw-r--r--   0 hsterz     (501) staff       (20)     2690 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/videomae/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6717 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/videomae/configuration_videomae.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12398 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/videomae/convert_videomae_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1200 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/videomae/feature_extraction_videomae.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17326 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/videomae/image_processing_videomae.py
--rw-r--r--   0 hsterz     (501) staff       (20)    44439 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/videomae/modeling_videomae.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.572585 adapter-transformers-3.2.0/src/transformers/models/vilt/
--rw-r--r--   0 hsterz     (501) staff       (20)     2996 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6928 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/configuration_vilt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12878 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/convert_vilt_original_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/feature_extraction_vilt.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22924 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/image_processing_vilt.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    64920 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/modeling_vilt.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6020 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vilt/processing_vilt.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.574167 adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/
--rw-r--r--   0 hsterz     (501) staff       (20)     2798 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8785 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/configuration_vision_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    41659 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/modeling_flax_vision_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    38296 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/modeling_tf_vision_encoder_decoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    35014 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/modeling_vision_encoder_decoder.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.575312 adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/
--rw-r--r--   0 hsterz     (501) staff       (20)     2410 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5289 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)    26682 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/modeling_flax_vision_text_dual_encoder.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    25326 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6977 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/processing_vision_text_dual_encoder.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.576431 adapter-transformers-3.2.0/src/transformers/models/visual_bert/
--rw-r--r--   0 hsterz     (501) staff       (20)     2406 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/visual_bert/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7941 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/visual_bert/configuration_visual_bert.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5158 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/models/visual_bert/convert_visual_bert_original_pytorch_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    69863 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/visual_bert/modeling_visual_bert.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.578468 adapter-transformers-3.2.0/src/transformers/models/vit/
--rw-r--r--   0 hsterz     (501) staff       (20)     3769 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5835 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/configuration_vit.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8868 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit/convert_dino_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10206 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit/convert_vit_timm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1165 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/feature_extraction_vit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13293 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/image_processing_vit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    25335 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/modeling_flax_vit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33758 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/modeling_tf_vit.py
--rw-r--r--   0 hsterz     (501) staff       (20)    36262 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit/modeling_vit.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.579351 adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/
--rw-r--r--   0 hsterz     (501) staff       (20)     2487 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7222 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/configuration_vit_hybrid.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13413 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/convert_vit_hybrid_timm_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16173 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/image_processing_vit_hybrid.py
--rw-r--r--   0 hsterz     (501) staff       (20)    31784 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/modeling_vit_hybrid.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.580346 adapter-transformers-3.2.0/src/transformers/models/vit_mae/
--rw-r--r--   0 hsterz     (501) staff       (20)     2599 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit_mae/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6567 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_mae/configuration_vit_mae.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7532 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit_mae/convert_vit_mae_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    49403 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_mae/modeling_tf_vit_mae.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    43357 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_mae/modeling_vit_mae.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.581280 adapter-transformers-3.2.0/src/transformers/models/vit_msn/
--rw-r--r--   0 hsterz     (501) staff       (20)     1954 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit_msn/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5061 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit_msn/configuration_vit_msn.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9857 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/vit_msn/convert_msn_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    29825 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/vit_msn/modeling_vit_msn.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.583518 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/
--rw-r--r--   0 hsterz     (501) staff       (20)     4214 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19604 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/configuration_wav2vec2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11206 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/convert_wav2vec2_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4838 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/convert_wav2vec2_original_s3prl_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11205 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/feature_extraction_wav2vec2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    57334 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/modeling_flax_wav2vec2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    72232 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/modeling_tf_wav2vec2.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    92946 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/modeling_wav2vec2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7136 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/processing_wav2vec2.py
--rw-r--r--   0 hsterz     (501) staff       (20)    38899 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2/tokenization_wav2vec2.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.584899 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/
--rw-r--r--   0 hsterz     (501) staff       (20)     2546 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    20727 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/configuration_wav2vec2_conformer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13382 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/convert_wav2vec2_conformer_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    95389 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/modeling_wav2vec2_conformer.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.585359 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_phoneme/
--rw-r--r--   0 hsterz     (501) staff       (20)     1164 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_phoneme/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    25933 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.585728 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_with_lm/
--rw-r--r--   0 hsterz     (501) staff       (20)     1152 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_with_lm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    26839 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wav2vec2_with_lm/processing_wav2vec2_with_lm.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.586869 adapter-transformers-3.2.0/src/transformers/models/wavlm/
--rw-r--r--   0 hsterz     (501) staff       (20)     2130 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wavlm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18413 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wavlm/configuration_wavlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8581 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wavlm/convert_wavlm_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4814 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/wavlm/convert_wavlm_original_s3prl_checkpoint_to_pytorch.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    77406 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/wavlm/modeling_wavlm.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.588895 adapter-transformers-3.2.0/src/transformers/models/whisper/
--rw-r--r--   0 hsterz     (501) staff       (20)     3100 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12993 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/configuration_whisper.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7657 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/convert_openai_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22952 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/english_normalizer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13330 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/feature_extraction_whisper.py
--rw-r--r--   0 hsterz     (501) staff       (20)    64909 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/modeling_tf_whisper.py
--rw-r--r--   0 hsterz     (501) staff       (20)    59102 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/modeling_whisper.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3744 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/processing_whisper.py
--rw-r--r--   0 hsterz     (501) staff       (20)    27452 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/whisper/tokenization_whisper.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.589906 adapter-transformers-3.2.0/src/transformers/models/x_clip/
--rw-r--r--   0 hsterz     (501) staff       (20)     2224 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/x_clip/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    17775 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/x_clip/configuration_x_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)    18077 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/x_clip/convert_x_clip_original_pytorch_to_hf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    67297 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/x_clip/modeling_x_clip.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6839 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/x_clip/processing_x_clip.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.591647 adapter-transformers-3.2.0/src/transformers/models/xglm/
--rw-r--r--   0 hsterz     (501) staff       (20)     4079 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6054 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/configuration_xglm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2325 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/convert_xglm_original_ckpt_to_trfms.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33623 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/modeling_flax_xglm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    44177 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/modeling_tf_xglm.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    45212 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/modeling_xglm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13276 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/tokenization_xglm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8032 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xglm/tokenization_xglm_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.593382 adapter-transformers-3.2.0/src/transformers/models/xlm/
--rw-r--r--   0 hsterz     (501) staff       (20)     3463 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11974 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm/configuration_xlm.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     2946 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm/convert_xlm_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    55940 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm/modeling_tf_xlm.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    54942 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm/modeling_xlm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    34979 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm/tokenization_xlm.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.594335 adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     2786 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9124 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/configuration_xlm_prophetnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)   118071 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/modeling_xlm_prophetnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13907 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/tokenization_xlm_prophetnet.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.596331 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/
--rw-r--r--   0 hsterz     (501) staff       (20)     5996 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8345 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/configuration_xlm_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    58614 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/modeling_flax_xlm_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    81329 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/modeling_tf_xlm_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    75680 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14284 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10263 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/tokenization_xlm_roberta_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.597033 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/
--rw-r--r--   0 hsterz     (501) staff       (20)     2576 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7594 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/configuration_xlm_roberta_xl.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8228 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/convert_xlm_roberta_xl_original_pytorch_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    70196 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/modeling_xlm_roberta_xl.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.599285 adapter-transformers-3.2.0/src/transformers/models/xlnet/
--rw-r--r--   0 hsterz     (501) staff       (20)     4459 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11142 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/configuration_xlnet.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)     3688 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/convert_xlnet_original_tf_checkpoint_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    77793 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/modeling_tf_xlnet.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    93010 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/modeling_xlnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15990 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/tokenization_xlnet.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10025 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/xlnet/tokenization_xlnet_fast.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.600666 adapter-transformers-3.2.0/src/transformers/models/yolos/
--rw-r--r--   0 hsterz     (501) staff       (20)     2571 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/yolos/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7790 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/yolos/configuration_yolos.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11275 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/yolos/convert_yolos_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1179 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/yolos/feature_extraction_yolos.py
--rw-r--r--   0 hsterz     (501) staff       (20)    53221 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/yolos/image_processing_yolos.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    58802 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/yolos/modeling_yolos.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.601621 adapter-transformers-3.2.0/src/transformers/models/yoso/
--rw-r--r--   0 hsterz     (501) staff       (20)     2282 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/yoso/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6901 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/yoso/configuration_yoso.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4116 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/models/yoso/convert_yoso_pytorch_to_pytorch.py
--rw-r--r--   0 hsterz     (501) staff       (20)    55127 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/models/yoso/modeling_yoso.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.604081 adapter-transformers-3.2.0/src/transformers/onnx/
--rw-r--r--   0 hsterz     (501) staff       (20)     1563 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/onnx/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9353 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/onnx/__main__.py
--rw-r--r--   0 hsterz     (501) staff       (20)    32531 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/onnx/config.py
--rw-r--r--   0 hsterz     (501) staff       (20)    21583 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/onnx/convert.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28303 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/onnx/features.py
--rw-r--r--   0 hsterz     (501) staff       (20)     3625 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/onnx/utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    27775 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/optimization.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16558 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/optimization_tf.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.609732 adapter-transformers-3.2.0/src/transformers/pipelines/
--rwxr-xr-x   0 hsterz     (501) staff       (20)    41801 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6695 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/audio_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8095 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/audio_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    34553 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/automatic_speech_recognition.py
--rw-r--r--   0 hsterz     (501) staff       (20)    49295 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/base.py
--rw-r--r--   0 hsterz     (501) staff       (20)    13596 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/conversational.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4260 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/depth_estimation.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22458 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/document_question_answering.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4690 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/feature_extraction.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10687 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/fill_mask.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4942 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/image_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)     8056 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/image_segmentation.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4882 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/image_to_text.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7475 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/object_detection.py
--rw-r--r--   0 hsterz     (501) staff       (20)    12624 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/pt_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    29389 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/question_answering.py
--rw-r--r--   0 hsterz     (501) staff       (20)    19893 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/table_question_answering.py
--rw-r--r--   0 hsterz     (501) staff       (20)    16759 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/text2text_generation.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10042 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/text_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14479 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/text_generation.py
--rw-r--r--   0 hsterz     (501) staff       (20)    22806 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/token_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5012 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/video_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5970 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/visual_question_answering.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11983 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/zero_shot_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)     6010 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/zero_shot_image_classification.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9033 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pipelines/zero_shot_object_detection.py
--rw-r--r--   0 hsterz     (501) staff       (20)    10857 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/processing_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11218 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/pytorch_utils.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.610407 adapter-transformers-3.2.0/src/transformers/sagemaker/
--rw-r--r--   0 hsterz     (501) staff       (20)      901 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/sagemaker/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     1044 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/sagemaker/trainer_sm.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5411 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/sagemaker/training_args_sm.py
--rw-r--r--   0 hsterz     (501) staff       (20)    58008 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/testing_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2639 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/tf_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    39944 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/tokenization_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)   179682 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/tokenization_utils_base.py
--rw-r--r--   0 hsterz     (501) staff       (20)    33226 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/tokenization_utils_fast.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)   176752 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/trainer.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23845 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/trainer_callback.py
--rw-r--r--   0 hsterz     (501) staff       (20)    46985 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/trainer_pt_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11729 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/trainer_seq2seq.py
--rw-r--r--   0 hsterz     (501) staff       (20)    34693 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/trainer_tf.py
--rw-r--r--   0 hsterz     (501) staff       (20)    23896 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/trainer_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    89763 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/training_args.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2901 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/training_args_seq2seq.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14190 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/training_args_tf.py
-drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-03-03 13:48:09.618053 adapter-transformers-3.2.0/src/transformers/utils/
--rw-r--r--   0 hsterz     (501) staff       (20)     6293 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/__init__.py
--rw-r--r--   0 hsterz     (501) staff       (20)     7489 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/bitsandbytes.py
--rw-r--r--   0 hsterz     (501) staff       (20)      172 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/constants.py
--rw-r--r--   0 hsterz     (501) staff       (20)    39982 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/doc.py
--rw-r--r--   0 hsterz     (501) staff       (20)      391 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_detectron2_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)    28808 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_flax_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)      309 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_keras_nlp_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)   162054 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_pt_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)      342 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_sentencepiece_and_speech_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)      301 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_sentencepiece_and_tokenizers_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)     5064 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_sentencepiece_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)      647 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_speech_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)      321 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_tensorflow_text_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)    63396 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_tf_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2970 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_timm_and_vision_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9910 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_tokenizers_objects.py
--rw-r--r--   0 hsterz     (501) staff       (20)    11412 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/dummy_vision_objects.py
--rwxr-xr-x   0 hsterz     (501) staff       (20)    45404 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/fx.py
--rw-r--r--   0 hsterz     (501) staff       (20)    15863 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/generic.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4971 2023-01-11 18:45:51.000000 adapter-transformers-3.2.0/src/transformers/utils/hp_naming.py
--rw-r--r--   0 hsterz     (501) staff       (20)    47555 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/hub.py
--rw-r--r--   0 hsterz     (501) staff       (20)    40353 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/import_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)     9643 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/logging.py
--rw-r--r--   0 hsterz     (501) staff       (20)     2300 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/model_parallel_utils.py
--rw-r--r--   0 hsterz     (501) staff       (20)    14831 2023-03-03 13:26:11.000000 adapter-transformers-3.2.0/src/transformers/utils/notebook.py
--rw-r--r--   0 hsterz     (501) staff       (20)    50686 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/sentencepiece_model_pb2.py
--rw-r--r--   0 hsterz     (501) staff       (20)     4518 2023-02-21 21:41:49.000000 adapter-transformers-3.2.0/src/transformers/utils/versions.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.024329 adapter-transformers-3.2.1/
+-rw-r--r--   0 hsterz     (501) staff       (20)    11446 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/LICENSE
+-rw-r--r--   0 hsterz     (501) staff       (20)       16 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/MANIFEST.in
+-rw-r--r--   0 hsterz     (501) staff       (20)     8808 2023-04-06 21:08:04.024558 adapter-transformers-3.2.1/PKG-INFO
+-rw-r--r--   0 hsterz     (501) staff       (20)     6627 2023-03-31 13:08:45.000000 adapter-transformers-3.2.1/README.md
+-rw-r--r--   0 hsterz     (501) staff       (20)       57 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/pyproject.toml
+-rw-r--r--   0 hsterz     (501) staff       (20)      817 2023-04-06 21:08:04.024969 adapter-transformers-3.2.1/setup.cfg
+-rw-r--r--   0 hsterz     (501) staff       (20)    15800 2023-04-06 20:50:35.000000 adapter-transformers-3.2.1/setup.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.603439 adapter-transformers-3.2.1/src/
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.627565 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/
+-rw-r--r--   0 hsterz     (501) staff       (20)     8808 2023-04-06 21:08:03.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/PKG-INFO
+-rw-r--r--   0 hsterz     (501) staff       (20)    68639 2023-04-06 21:08:03.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/SOURCES.txt
+-rw-r--r--   0 hsterz     (501) staff       (20)        1 2023-04-06 21:08:03.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/dependency_links.txt
+-rw-r--r--   0 hsterz     (501) staff       (20)       81 2023-04-06 21:08:03.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/entry_points.txt
+-rw-r--r--   0 hsterz     (501) staff       (20)        1 2023-01-11 19:07:11.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/not-zip-safe
+-rw-r--r--   0 hsterz     (501) staff       (20)     6730 2023-04-06 21:08:03.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/requires.txt
+-rw-r--r--   0 hsterz     (501) staff       (20)       13 2023-04-06 21:08:03.000000 adapter-transformers-3.2.1/src/adapter_transformers.egg-info/top_level.txt
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.649979 adapter-transformers-3.2.1/src/transformers/
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   249393 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6568 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/activations.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4313 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/activations_tf.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.656633 adapter-transformers-3.2.1/src/transformers/adapters/
+-rw-r--r--   0 hsterz     (501) staff       (20)     7275 2023-04-06 20:50:31.000000 adapter-transformers-3.2.1/src/transformers/adapters/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7707 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/composition.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37267 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/configuration.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4553 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/context.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15810 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/head_utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.657675 adapter-transformers-3.2.1/src/transformers/adapters/heads/
+-rw-r--r--   0 hsterz     (501) staff       (20)      151 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/heads/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    35900 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/heads/base.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6281 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/heads/dependency_parsing.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7138 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/heads/language_modeling.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8742 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/hub_mixin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28475 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/layer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33112 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/loading.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17245 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/lora.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.661022 adapter-transformers-3.2.1/src/transformers/adapters/mixins/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1332 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/albert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1766 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/bart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      923 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/beit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1236 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1797 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1107 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/distilbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2300 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1029 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/gpt2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1029 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/gptj.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1383 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/t5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      951 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/mixins/vit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    55639 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/model_mixin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    31468 2023-03-31 13:53:03.000000 adapter-transformers-3.2.1/src/transformers/adapters/modeling.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.661241 adapter-transformers-3.2.1/src/transformers/adapters/models/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/__init__.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.661604 adapter-transformers-3.2.1/src/transformers/adapters/models/albert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1133 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/albert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7750 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/albert/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.662160 adapter-transformers-3.2.1/src/transformers/adapters/models/auto/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1312 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/auto/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2794 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/auto/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.663919 adapter-transformers-3.2.1/src/transformers/adapters/models/bart/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1194 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/bart/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9588 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/bart/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.664500 adapter-transformers-3.2.1/src/transformers/adapters/models/beit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1129 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/beit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4156 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/beit/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.664957 adapter-transformers-3.2.1/src/transformers/adapters/models/bert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1194 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/bert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11517 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/bert/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.665372 adapter-transformers-3.2.1/src/transformers/adapters/models/bert_generation/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1149 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/bert_generation/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5883 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/bert_generation/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.665766 adapter-transformers-3.2.1/src/transformers/adapters/models/deberta/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1135 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/deberta/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6627 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/deberta/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.666300 adapter-transformers-3.2.1/src/transformers/adapters/models/debertaV2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1139 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/debertaV2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7613 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/debertaV2/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.666698 adapter-transformers-3.2.1/src/transformers/adapters/models/distilbert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1218 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/distilbert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11758 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/distilbert/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.667075 adapter-transformers-3.2.1/src/transformers/adapters/models/gpt2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1194 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/gpt2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8569 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/gpt2/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.667957 adapter-transformers-3.2.1/src/transformers/adapters/models/gptj/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1129 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/gptj/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7516 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/gptj/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.668486 adapter-transformers-3.2.1/src/transformers/adapters/models/mbart/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1198 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/mbart/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9571 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/mbart/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.669362 adapter-transformers-3.2.1/src/transformers/adapters/models/roberta/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1206 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/roberta/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11589 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/roberta/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.669796 adapter-transformers-3.2.1/src/transformers/adapters/models/t5/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1186 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/t5/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8402 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/t5/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.670200 adapter-transformers-3.2.1/src/transformers/adapters/models/vit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1127 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/vit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4043 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/vit/adapter_model.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.670586 adapter-transformers-3.2.1/src/transformers/adapters/models/xlm_roberta/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1218 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/xlm_roberta/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1048 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/models/xlm_roberta/adapter_model.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    30155 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/prefix_tuning.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12763 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/trainer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4207 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/training.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32743 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/adapters/utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.670966 adapter-transformers-3.2.1/src/transformers/adapters/wrappers/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/adapters/wrappers/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4022 2023-03-31 13:53:03.000000 adapter-transformers-3.2.1/src/transformers/adapters/wrappers/configuration.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.672450 adapter-transformers-3.2.1/src/transformers/benchmark/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/benchmark/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10753 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/benchmark/benchmark.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3891 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_args.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4736 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_args_tf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6425 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_args_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13066 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_tf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37621 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.676205 adapter-transformers-3.2.1/src/transformers/commands/
+-rw-r--r--   0 hsterz     (501) staff       (20)      923 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/commands/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11064 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/commands/add_new_model.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    67351 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/commands/add_new_model_like.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7856 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/commands/convert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1860 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/commands/download.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3319 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/commands/env.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8001 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/commands/lfs.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19003 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/commands/pt_to_tf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4249 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/commands/run.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8027 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/commands/serving.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6329 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/commands/train.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2047 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/commands/transformers_cli.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7124 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/commands/user.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    49830 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/configuration_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20903 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/convert_graph_to_onnx.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    16632 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/convert_pytorch_checkpoint_to_tf2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    46337 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/convert_slow_tokenizer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     4982 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/convert_slow_tokenizers_checkpoints_to_fast.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2899 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/convert_tf_hub_seq_to_seq_bert_to_pytorch.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.677325 adapter-transformers-3.2.1/src/transformers/data/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1594 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    76779 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/data_collator.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.678226 adapter-transformers-3.2.1/src/transformers/data/datasets/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1080 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/datasets/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6165 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/datasets/glue.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23723 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/datasets/language_modeling.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9220 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/datasets/squad.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.678644 adapter-transformers-3.2.1/src/transformers/data/metrics/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3776 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/metrics/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    29698 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/data/metrics/squad_metrics.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.680631 adapter-transformers-3.2.1/src/transformers/data/processors/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1185 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/processors/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23219 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/data/processors/glue.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33154 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/processors/squad.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13829 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/data/processors/utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3489 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/data/processors/xnli.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3433 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/data/test_generation_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12907 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/debug_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15835 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/deepspeed.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1756 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/dependency_versions_check.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3395 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/dependency_versions_table.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19064 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/dynamic_module_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17982 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/feature_extraction_sequence_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    26314 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/feature_extraction_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3738 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/file_utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.684878 adapter-transformers-3.2.1/src/transformers/generation/
+-rw-r--r--   0 hsterz     (501) staff       (20)     9479 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19097 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/beam_constraints.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    42653 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/beam_search.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36470 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/configuration_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10839 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/flax_logits_process.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    42338 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/flax_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    43968 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/logits_process.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5510 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/generation/stopping_criteria.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    27539 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/tf_logits_process.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   156300 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/tf_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   212677 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/generation/utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1118 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/generation_flax_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1109 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/generation_tf_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1126 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/generation_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18952 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/hf_argparser.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    24681 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/image_processing_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    29183 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/image_transforms.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22352 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/image_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    65749 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/integrations.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20709 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/keras_callbacks.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    34991 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modelcard.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    38967 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/modeling_flax_outputs.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15034 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modeling_flax_pytorch_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    54824 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modeling_flax_utils.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    85679 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modeling_outputs.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    54504 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/modeling_tf_outputs.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21162 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modeling_tf_pytorch_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   151710 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modeling_tf_utils.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   163219 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/modeling_utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.685346 adapter-transformers-3.2.1/src/transformers/models/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3334 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/__init__.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.688163 adapter-transformers-3.2.1/src/transformers/models/albert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5653 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8567 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/configuration_albert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2183 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/convert_albert_original_tf_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    62818 2023-03-31 13:15:30.000000 adapter-transformers-3.2.1/src/transformers/models/albert/modeling_albert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    40773 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/modeling_flax_albert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    67264 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/modeling_tf_albert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15428 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/tokenization_albert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10814 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/albert/tokenization_albert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.689291 adapter-transformers-3.2.1/src/transformers/models/altclip/
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2334 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/altclip/__init__.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    16597 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/altclip/configuration_altclip.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    78432 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/altclip/modeling_altclip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6444 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/altclip/processing_altclip.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.691494 adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2678 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5649 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/configuration_audio_spectrogram_transformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11052 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/convert_audio_spectrogram_transformer_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8308 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/feature_extraction_audio_spectrogram_transformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    26058 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/modeling_audio_spectrogram_transformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.694285 adapter-transformers-3.2.1/src/transformers/models/auto/
+-rw-r--r--   0 hsterz     (501) staff       (20)    14165 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36525 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/auto_factory.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    39581 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/configuration_auto.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18660 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/feature_extraction_auto.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19712 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/image_processing_auto.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    50608 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/modeling_auto.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13498 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/modeling_flax_auto.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    24852 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/modeling_tf_auto.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15137 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/processing_auto.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37596 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/auto/tokenization_auto.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.697173 adapter-transformers-3.2.1/src/transformers/models/bart/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4504 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18992 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/configuration_bart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5647 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    92345 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/modeling_bart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    82685 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/modeling_flax_bart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    77193 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/modeling_tf_bart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17972 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/tokenization_bart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13803 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bart/tokenization_bart_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.697781 adapter-transformers-3.2.1/src/transformers/models/barthez/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2020 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/barthez/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13192 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/barthez/tokenization_barthez.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8899 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/barthez/tokenization_barthez_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.698192 adapter-transformers-3.2.1/src/transformers/models/bartpho/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1533 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bartpho/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14218 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bartpho/tokenization_bartpho.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.700269 adapter-transformers-3.2.1/src/transformers/models/beit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3460 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/beit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9641 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/beit/configuration_beit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16496 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/beit/convert_beit_unilm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/beit/feature_extraction_beit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    24737 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/beit/image_processing_beit.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    55360 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/beit/modeling_beit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37004 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/beit/modeling_flax_beit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.704676 adapter-transformers-3.2.1/src/transformers/models/bert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     6228 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10149 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/configuration_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10490 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_original_tf2_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2159 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4101 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_pytorch_checkpoint_to_original_tf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7606 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_token_dropping_original_tf2_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    86400 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/modeling_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    63605 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/modeling_flax_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    93219 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/modeling_tf_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    24516 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/tokenization_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14870 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/tokenization_bert_fast.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11009 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert/tokenization_bert_tf.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.705658 adapter-transformers-3.2.1/src/transformers/models/bert_generation/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2446 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert_generation/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6227 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert_generation/configuration_bert_generation.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    49793 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert_generation/modeling_bert_generation.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7139 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert_generation/tokenization_bert_generation.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.706105 adapter-transformers-3.2.1/src/transformers/models/bert_japanese/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1224 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert_japanese/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    39624 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bert_japanese/tokenization_bert_japanese.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.706611 adapter-transformers-3.2.1/src/transformers/models/bertweet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1130 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bertweet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    27205 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bertweet/tokenization_bertweet.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.708911 adapter-transformers-3.2.1/src/transformers/models/big_bird/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4745 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8305 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/configuration_big_bird.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2494 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/convert_bigbird_original_tf_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   142147 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/modeling_big_bird.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   106503 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/modeling_flax_big_bird.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14684 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/tokenization_big_bird.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11365 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/big_bird/tokenization_big_bird_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.710079 adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2487 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19801 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/configuration_bigbird_pegasus.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6295 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/convert_bigbird_pegasus_tf_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   147127 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/modeling_bigbird_pegasus.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.712284 adapter-transformers-3.2.1/src/transformers/models/biogpt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2096 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/biogpt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6600 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/biogpt/configuration_biogpt.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    10579 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/biogpt/convert_biogpt_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    32805 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/biogpt/modeling_biogpt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13737 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/biogpt/tokenization_biogpt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.713623 adapter-transformers-3.2.1/src/transformers/models/bit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2452 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5868 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bit/configuration_bit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5955 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bit/convert_bit_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16153 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bit/image_processing_bit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32427 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/bit/modeling_bit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.717591 adapter-transformers-3.2.1/src/transformers/models/blenderbot/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4202 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19015 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/configuration_blenderbot.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3702 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/convert_blenderbot_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    76930 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/modeling_blenderbot.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    64957 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/modeling_flax_blenderbot.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    70073 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/modeling_tf_blenderbot.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19479 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/tokenization_blenderbot.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14196 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot/tokenization_blenderbot_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.719718 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4434 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18478 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/configuration_blenderbot_small.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    75703 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/modeling_blenderbot_small.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    65922 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/modeling_flax_blenderbot_small.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    69400 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/modeling_tf_blenderbot_small.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8647 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/tokenization_blenderbot_small.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4057 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/tokenization_blenderbot_small_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.721563 adapter-transformers-3.2.1/src/transformers/models/blip/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2845 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18239 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/configuration_blip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6980 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/convert_blip_original_pytorch_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13922 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/image_processing_blip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    62303 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/modeling_blip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    41581 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/modeling_blip_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6152 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/blip/processing_blip.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.723238 adapter-transformers-3.2.1/src/transformers/models/bloom/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2670 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bloom/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10792 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bloom/configuration_bloom.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10313 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bloom/convert_bloom_original_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    56666 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bloom/modeling_bloom.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7263 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bloom/tokenization_bloom_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.723621 adapter-transformers-3.2.1/src/transformers/models/bort/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/bort/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14057 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/bort/convert_bort_original_gluonnlp_checkpoint_to_pytorch.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.724390 adapter-transformers-3.2.1/src/transformers/models/byt5/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1113 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/byt5/__init__.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2120 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/byt5/convert_byt5_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10726 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/byt5/tokenization_byt5.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.726037 adapter-transformers-3.2.1/src/transformers/models/camembert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4614 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/camembert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7734 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/camembert/configuration_camembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    73249 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/camembert/modeling_camembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    80894 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/camembert/modeling_tf_camembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13580 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/camembert/tokenization_camembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8657 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/camembert/tokenization_camembert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.727388 adapter-transformers-3.2.1/src/transformers/models/canine/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2443 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/canine/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6477 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/canine/configuration_canine.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2118 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/canine/convert_canine_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    73780 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/canine/modeling_canine.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9275 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/canine/tokenization_canine.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.729400 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3090 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19075 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/configuration_chinese_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5070 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/convert_chinese_clip_original_pytorch_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1247 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/feature_extraction_chinese_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15803 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/image_processing_chinese_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    73449 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/modeling_chinese_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6754 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/chinese_clip/processing_chinese_clip.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.733501 adapter-transformers-3.2.1/src/transformers/models/clip/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5198 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17889 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/configuration_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5248 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/convert_clip_original_pytorch_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/clip/feature_extraction_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16184 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/image_processing_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    58772 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/modeling_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    45841 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/modeling_flax_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    57673 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/modeling_tf_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6821 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/clip/processing_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20441 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/tokenization_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6955 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clip/tokenization_clip_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.735062 adapter-transformers-3.2.1/src/transformers/models/clipseg/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2350 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clipseg/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17992 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clipseg/configuration_clipseg.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11124 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clipseg/convert_clipseg_original_pytorch_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    64567 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/clipseg/modeling_clipseg.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7838 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/clipseg/processing_clipseg.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.736185 adapter-transformers-3.2.1/src/transformers/models/codegen/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2614 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/codegen/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10548 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/codegen/configuration_codegen.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    31438 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/codegen/modeling_codegen.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15112 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/codegen/tokenization_codegen.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10506 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/codegen/tokenization_codegen_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.737629 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2996 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12597 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/configuration_conditional_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15946 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/convert_conditional_detr_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1251 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/feature_extraction_conditional_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    72489 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/image_processing_conditional_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   127554 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/conditional_detr/modeling_conditional_detr.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.740644 adapter-transformers-3.2.1/src/transformers/models/convbert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4240 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7311 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/configuration_convbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2108 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/convert_convbert_original_tf1_checkpoint_to_pytorch_and_tf2.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    59172 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/modeling_convbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    56248 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/modeling_tf_convbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21308 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/tokenization_convbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8764 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convbert/tokenization_convbert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.742629 adapter-transformers-3.2.1/src/transformers/models/convnext/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3355 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5834 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/configuration_convnext.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10234 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/convert_convnext_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1200 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/feature_extraction_convnext.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15130 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/image_processing_convnext.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    22560 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/modeling_convnext.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    25063 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/convnext/modeling_tf_convnext.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.743306 adapter-transformers-3.2.1/src/transformers/models/cpm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1987 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cpm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15153 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cpm/tokenization_cpm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10679 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cpm/tokenization_cpm_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.744754 adapter-transformers-3.2.1/src/transformers/models/ctrl/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2859 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ctrl/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5170 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ctrl/configuration_ctrl.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    34887 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ctrl/modeling_ctrl.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37094 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ctrl/modeling_tf_ctrl.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8498 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ctrl/tokenization_ctrl.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.746139 adapter-transformers-3.2.1/src/transformers/models/cvt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2605 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cvt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6859 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cvt/configuration_cvt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13579 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cvt/convert_cvt_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28913 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cvt/modeling_cvt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37443 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/cvt/modeling_tf_cvt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.749388 adapter-transformers-3.2.1/src/transformers/models/data2vec/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5104 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16244 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/configuration_data2vec_audio.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7419 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/configuration_data2vec_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9432 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/configuration_data2vec_vision.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10858 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/convert_data2vec_audio_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9613 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/convert_data2vec_text_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    15350 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/convert_data2vec_vision_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    65791 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_data2vec_audio.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    72297 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_data2vec_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    52885 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_data2vec_vision.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    62599 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_tf_data2vec_vision.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.751423 adapter-transformers-3.2.1/src/transformers/models/deberta/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3848 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9388 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta/configuration_deberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    61036 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta/modeling_deberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    62889 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta/modeling_tf_deberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19780 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta/tokenization_deberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13417 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta/tokenization_deberta_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.753105 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4070 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9174 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/configuration_deberta_v2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    71361 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/modeling_deberta_v2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    68994 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/modeling_tf_deberta_v2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21719 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/tokenization_deberta_v2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10996 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deberta_v2/tokenization_deberta_v2_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.753790 adapter-transformers-3.2.1/src/transformers/models/decision_transformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2332 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/decision_transformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7923 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/decision_transformer/configuration_decision_transformer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    43376 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/decision_transformer/modeling_decision_transformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.755873 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2767 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13658 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/configuration_deformable_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9493 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/convert_deformable_detr_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1244 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/feature_extraction_deformable_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    59943 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/image_processing_deformable_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1635 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/load_custom.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   118536 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deformable_detr/modeling_deformable_detr.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.758244 adapter-transformers-3.2.1/src/transformers/models/deit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3657 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5960 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deit/configuration_deit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9231 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deit/convert_deit_timm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/deit/feature_extraction_deit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14941 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deit/image_processing_deit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    38237 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/deit/modeling_deit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    45314 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/deit/modeling_tf_deit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.760344 adapter-transformers-3.2.1/src/transformers/models/detr/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2606 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/detr/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12253 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/detr/configuration_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13577 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/detr/convert_detr_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18373 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/detr/convert_detr_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/detr/feature_extraction_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    80473 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/detr/image_processing_detr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   111431 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/detr/modeling_detr.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.760839 adapter-transformers-3.2.1/src/transformers/models/dialogpt/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/models/dialogpt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1537 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/dialogpt/convert_dialogpt_original_pytorch_checkpoint_to_pytorch.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.761515 adapter-transformers-3.2.1/src/transformers/models/dinat/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2020 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dinat/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7230 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dinat/configuration_dinat.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    42176 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dinat/modeling_dinat.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.764117 adapter-transformers-3.2.1/src/transformers/models/distilbert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5338 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6977 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/configuration_distilbert.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    52049 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/modeling_distilbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32622 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/modeling_flax_distilbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    47551 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/modeling_tf_distilbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23037 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/tokenization_distilbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10707 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/distilbert/tokenization_distilbert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.765801 adapter-transformers-3.2.1/src/transformers/models/dit/
+-rw-r--r--   0 hsterz     (501) staff       (20)        0 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/dit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9436 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dit/convert_dit_unilm_to_pytorch.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.772008 adapter-transformers-3.2.1/src/transformers/models/donut/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2626 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/donut/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6177 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/donut/configuration_donut_swin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9324 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/donut/convert_donut_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1179 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/donut/feature_extraction_donut.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20167 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/donut/image_processing_donut.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    43503 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/donut/modeling_donut_swin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8066 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/donut/processing_donut.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.774894 adapter-transformers-3.2.1/src/transformers/models/dpr/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4706 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7261 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/configuration_dpr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6097 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/convert_dpr_original_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28857 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/modeling_dpr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33628 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/modeling_tf_dpr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19821 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/tokenization_dpr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20207 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpr/tokenization_dpr_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.777372 adapter-transformers-3.2.1/src/transformers/models/dpt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2615 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11301 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/configuration_dpt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13008 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/convert_dpt_hybrid_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11797 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/convert_dpt_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1165 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/feature_extraction_dpt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18288 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/image_processing_dpt.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    54914 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/dpt/modeling_dpt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.778905 adapter-transformers-3.2.1/src/transformers/models/efficientformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2746 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/efficientformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7658 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/efficientformer/configuration_efficientformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9383 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/efficientformer/convert_efficientformer_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16451 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/efficientformer/image_processing_efficientformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33328 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/efficientformer/modeling_efficientformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.781570 adapter-transformers-3.2.1/src/transformers/models/electra/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5428 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/electra/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9926 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/electra/configuration_electra.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2862 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/electra/convert_electra_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    75862 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/electra/modeling_electra.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    62253 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/electra/modeling_flax_electra.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    75779 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/electra/modeling_tf_electra.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22115 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/electra/tokenization_electra.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10494 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/electra/tokenization_electra_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.783312 adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2622 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4880 2023-03-31 13:08:43.000000 adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/configuration_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36403 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    43810 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/modeling_flax_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36312 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/modeling_tf_encoder_decoder.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.784050 adapter-transformers-3.2.1/src/transformers/models/ernie/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2502 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ernie/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8883 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ernie/configuration_ernie.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    84316 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ernie/modeling_ernie.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.785793 adapter-transformers-3.2.1/src/transformers/models/esm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3149 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14752 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/configuration_esm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18476 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/convert_esm.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    56453 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/modeling_esm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    86755 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/modeling_esmfold.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    65295 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/modeling_tf_esm.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.788465 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/
+-rw-r--r--   0 hsterz     (501) staff       (20)      461 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14396 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/chunk_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3764 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/data_transforms.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8376 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/feats.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3708 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/loss.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11490 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/protein.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37969 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/residue_constants.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    41122 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/rigid_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4798 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/tensor_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5607 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/esm/tokenization_esm.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.789686 adapter-transformers-3.2.1/src/transformers/models/flaubert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3659 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flaubert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11705 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flaubert/configuration_flaubert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    57835 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flaubert/modeling_flaubert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    56750 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flaubert/modeling_tf_flaubert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    24039 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flaubert/tokenization_flaubert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.791720 adapter-transformers-3.2.1/src/transformers/models/flava/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3201 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flava/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    30829 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flava/configuration_flava.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3428 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/flava/convert_dalle_to_flava_codebook.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4372 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/flava/convert_flava_original_pytorch_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1201 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/flava/feature_extraction_flava.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36921 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flava/image_processing_flava.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    96550 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flava/modeling_flava.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6773 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/flava/processing_flava.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.793105 adapter-transformers-3.2.1/src/transformers/models/fnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3350 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5838 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fnet/configuration_fnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6912 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fnet/convert_fnet_original_flax_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    49516 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fnet/modeling_fnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15646 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fnet/tokenization_fnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8557 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fnet/tokenization_fnet_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.794219 adapter-transformers-3.2.1/src/transformers/models/fsmt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1846 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fsmt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10578 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fsmt/configuration_fsmt.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    11265 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fsmt/convert_fsmt_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    58257 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fsmt/modeling_fsmt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20145 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/fsmt/tokenization_fsmt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.796445 adapter-transformers-3.2.1/src/transformers/models/funnel/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4297 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9141 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/configuration_funnel.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2335 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/convert_funnel_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    69844 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/modeling_funnel.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    74284 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/modeling_tf_funnel.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23461 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/tokenization_funnel.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11793 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/funnel/tokenization_funnel_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.797537 adapter-transformers-3.2.1/src/transformers/models/git/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2059 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/git/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12726 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/git/configuration_git.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21976 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/git/convert_git_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    68444 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/git/modeling_git.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5486 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/git/processing_git.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.798995 adapter-transformers-3.2.1/src/transformers/models/glpn/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2592 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/glpn/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6182 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/glpn/configuration_glpn.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8574 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/glpn/convert_glpn_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/glpn/feature_extraction_glpn.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8920 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/glpn/image_processing_glpn.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    31526 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/glpn/modeling_glpn.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.801705 adapter-transformers-3.2.1/src/transformers/models/gpt2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4771 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12142 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/configuration_gpt2.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2532 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/convert_gpt2_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    31961 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/modeling_flax_gpt2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    70919 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/modeling_gpt2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    55948 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/modeling_tf_gpt2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14416 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/tokenization_gpt2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8045 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/tokenization_gpt2_fast.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3764 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt2/tokenization_gpt2_tf.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.802985 adapter-transformers-3.2.1/src/transformers/models/gpt_neo/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2729 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neo/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11823 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neo/configuration_gpt_neo.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2589 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neo/convert_gpt_neo_mesh_tf_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28080 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neo/modeling_flax_gpt_neo.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    39924 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neo/modeling_gpt_neo.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.803892 adapter-transformers-3.2.1/src/transformers/models/gpt_neox/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2512 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5791 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox/configuration_gpt_neox.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    31473 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox/modeling_gpt_neox.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5788 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox/tokenization_gpt_neox_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.804939 adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2325 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5946 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/configuration_gpt_neox_japanese.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    32478 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/modeling_gpt_neox_japanese.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17327 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/tokenization_gpt_neox_japanese.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.805617 adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1533 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8157 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/convert_megatron_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13176 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/tokenization_gpt_sw3.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.806642 adapter-transformers-3.2.1/src/transformers/models/gptj/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3451 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gptj/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9220 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gptj/configuration_gptj.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28519 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gptj/modeling_flax_gptj.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    49074 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gptj/modeling_gptj.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    47336 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/gptj/modeling_tf_gptj.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.807494 adapter-transformers-3.2.1/src/transformers/models/graphormer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2081 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/graphormer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6198 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/graphormer/collating_graphormer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10611 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/graphormer/configuration_graphormer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    35706 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/graphormer/modeling_graphormer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.808733 adapter-transformers-3.2.1/src/transformers/models/groupvit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3046 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/groupvit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17703 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/groupvit/configuration_groupvit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9775 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/groupvit/convert_groupvit_nvlab_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    68255 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/groupvit/modeling_groupvit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    82458 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/groupvit/modeling_tf_groupvit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.809777 adapter-transformers-3.2.1/src/transformers/models/herbert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1643 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/herbert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    25124 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/herbert/tokenization_herbert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6549 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/herbert/tokenization_herbert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.811519 adapter-transformers-3.2.1/src/transformers/models/hubert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2707 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14568 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/configuration_hubert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8942 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/convert_distilhubert_original_s3prl_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10380 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/convert_hubert_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2895 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/convert_hubert_original_s3prl_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    57931 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/modeling_hubert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    71597 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/hubert/modeling_tf_hubert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.812844 adapter-transformers-3.2.1/src/transformers/models/ibert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2257 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ibert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7472 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ibert/configuration_ibert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    57138 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/ibert/modeling_ibert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    30075 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/ibert/quant_modules.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.814136 adapter-transformers-3.2.1/src/transformers/models/imagegpt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2829 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/imagegpt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8866 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/imagegpt/configuration_imagegpt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2691 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/imagegpt/convert_imagegpt_original_tf2_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1200 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/imagegpt/feature_extraction_imagegpt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10758 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/imagegpt/image_processing_imagegpt.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    53896 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/imagegpt/modeling_imagegpt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.815764 adapter-transformers-3.2.1/src/transformers/models/jukebox/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2255 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/jukebox/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    27959 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/jukebox/configuration_jukebox.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11781 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/jukebox/convert_jukebox.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   119829 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/jukebox/modeling_jukebox.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18055 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/jukebox/tokenization_jukebox.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.817134 adapter-transformers-3.2.1/src/transformers/models/layoutlm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3958 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8547 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlm/configuration_layoutlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    61124 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlm/modeling_layoutlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    69222 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlm/modeling_tf_layoutlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21136 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlm/tokenization_layoutlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8966 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlm/tokenization_layoutlm_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.821166 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3610 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11246 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/configuration_layoutlmv2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1195 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/feature_extraction_layoutlmv2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11928 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/image_processing_layoutlmv2.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    61474 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/modeling_layoutlmv2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9233 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/processing_layoutlmv2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    71868 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/tokenization_layoutlmv2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    38070 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/tokenization_layoutlmv2_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.832089 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4683 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13365 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/configuration_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1195 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/feature_extraction_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17477 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/image_processing_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    61268 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/modeling_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    71537 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/modeling_tf_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9084 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/processing_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    72805 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/tokenization_layoutlmv3.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    40179 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/tokenization_layoutlmv3_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.833189 adapter-transformers-3.2.1/src/transformers/models/layoutxlm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2208 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutxlm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7910 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutxlm/processing_layoutxlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    57664 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutxlm/tokenization_layoutxlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    39909 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/layoutxlm/tokenization_layoutxlm_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.835140 adapter-transformers-3.2.1/src/transformers/models/led/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3179 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/led/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7632 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/led/configuration_led.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   140035 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/led/modeling_led.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   118555 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/led/modeling_tf_led.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20397 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/led/tokenization_led.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14862 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/led/tokenization_led_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.837594 adapter-transformers-3.2.1/src/transformers/models/levit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2679 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/levit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5930 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/levit/configuration_levit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6270 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/levit/convert_levit_timm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1204 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/levit/feature_extraction_levit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17245 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/levit/image_processing_levit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    29583 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/levit/modeling_levit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.838466 adapter-transformers-3.2.1/src/transformers/models/lilt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2080 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lilt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6877 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lilt/configuration_lilt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    53707 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lilt/modeling_lilt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.840222 adapter-transformers-3.2.1/src/transformers/models/longformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4367 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10523 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/configuration_longformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3027 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/convert_longformer_original_pytorch_lightning_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   114649 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/modeling_longformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   126969 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/modeling_tf_longformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18732 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/tokenization_longformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14526 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longformer/tokenization_longformer_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.841916 adapter-transformers-3.2.1/src/transformers/models/longt5/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2717 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longt5/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8481 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longt5/configuration_longt5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11088 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longt5/convert_longt5x_checkpoint_to_flax.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   105585 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longt5/modeling_flax_longt5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   105023 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/longt5/modeling_longt5.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.843357 adapter-transformers-3.2.1/src/transformers/models/luke/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2554 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/luke/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6553 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/luke/configuration_luke.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7468 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/luke/convert_luke_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   103505 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/luke/modeling_luke.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    85384 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/luke/tokenization_luke.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.845555 adapter-transformers-3.2.1/src/transformers/models/lxmert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3567 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9510 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/configuration_lxmert.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2109 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/convert_lxmert_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    64980 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/modeling_lxmert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    64272 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/modeling_tf_lxmert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20859 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/tokenization_lxmert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8436 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/lxmert/tokenization_lxmert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.846855 adapter-transformers-3.2.1/src/transformers/models/m2m_100/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2163 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/m2m_100/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13559 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/m2m_100/configuration_m2m_100.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3159 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/m2m_100/convert_m2m100_original_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    65752 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/m2m_100/modeling_m2m_100.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17152 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/m2m_100/tokenization_m2m_100.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.849025 adapter-transformers-3.2.1/src/transformers/models/marian/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3615 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18557 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/configuration_marian.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36254 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/convert_marian_tatoeba_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    26746 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/convert_marian_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    64217 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/modeling_flax_marian.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    82999 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/modeling_marian.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    69909 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/modeling_tf_marian.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17415 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/marian/tokenization_marian.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.852293 adapter-transformers-3.2.1/src/transformers/models/markuplm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3014 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7581 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/configuration_markuplm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6400 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/feature_extraction_markuplm.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    58000 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/modeling_markuplm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6346 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/processing_markuplm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    69721 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/tokenization_markuplm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    42802 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/markuplm/tokenization_markuplm_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.854526 adapter-transformers-3.2.1/src/transformers/models/mask2former/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2528 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mask2former/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11032 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mask2former/configuration_mask2former.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    45711 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mask2former/convert_mask2former_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    51413 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mask2former/image_processing_mask2former.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   117435 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mask2former/modeling_mask2former.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.858034 adapter-transformers-3.2.1/src/transformers/models/maskformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3116 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9434 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/configuration_maskformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6883 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/configuration_maskformer_swin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32240 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/convert_maskformer_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20748 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/convert_maskformer_resnet_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20337 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/convert_maskformer_swin_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1225 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/feature_extraction_maskformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    54066 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/image_processing_maskformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    89146 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/modeling_maskformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    41270 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/maskformer/modeling_maskformer_swin.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.860473 adapter-transformers-3.2.1/src/transformers/models/mbart/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4574 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18386 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/configuration_mbart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3035 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/convert_mbart_original_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    75068 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/modeling_flax_mbart.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    91862 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/modeling_mbart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    71027 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/modeling_tf_mbart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14713 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/tokenization_mbart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11915 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart/tokenization_mbart_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.861743 adapter-transformers-3.2.1/src/transformers/models/mbart50/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2018 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart50/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16665 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart50/tokenization_mbart50.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12198 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mbart50/tokenization_mbart50_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.863836 adapter-transformers-3.2.1/src/transformers/models/mctct/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2413 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mctct/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9305 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mctct/configuration_mctct.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16222 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mctct/feature_extraction_mctct.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    34053 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mctct/modeling_mctct.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5928 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mctct/processing_mctct.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.864977 adapter-transformers-3.2.1/src/transformers/models/megatron_bert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2677 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_bert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6572 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_bert/configuration_megatron_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13689 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    83515 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_bert/modeling_megatron_bert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.865766 adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/
+-rw-r--r--   0 hsterz     (501) staff       (20)      801 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36287 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/checkpoint_reshaping_and_interoperability.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13632 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/convert_megatron_gpt2_checkpoint.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.866464 adapter-transformers-3.2.1/src/transformers/models/mluke/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1527 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mluke/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10186 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mluke/convert_mluke_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    81139 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mluke/tokenization_mluke.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.867263 adapter-transformers-3.2.1/src/transformers/models/mmbt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1650 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mmbt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1605 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/mmbt/configuration_mmbt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18887 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/mmbt/modeling_mmbt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.869635 adapter-transformers-3.2.1/src/transformers/models/mobilebert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4775 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8585 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/configuration_mobilebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2200 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/convert_mobilebert_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    70780 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/modeling_mobilebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    76785 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/modeling_tf_mobilebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20742 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/tokenization_mobilebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8376 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilebert/tokenization_mobilebert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.870828 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2906 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5237 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/configuration_mobilenet_v1.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4948 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/convert_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1222 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/feature_extraction_mobilenet_v1.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16205 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/image_processing_mobilenet_v1.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    18777 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/modeling_mobilenet_v1.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.872615 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3001 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7361 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/configuration_mobilenet_v2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6412 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/convert_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1222 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/feature_extraction_mobilenet_v2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18652 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/image_processing_mobilenet_v2.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    34752 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/modeling_mobilenet_v2.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.873965 adapter-transformers-3.2.1/src/transformers/models/mobilevit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3663 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8400 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/configuration_mobilevit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12418 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/convert_mlcvnets_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1207 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/feature_extraction_mobilevit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16743 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/image_processing_mobilevit.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    40503 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/modeling_mobilevit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    46610 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mobilevit/modeling_tf_mobilevit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.875569 adapter-transformers-3.2.1/src/transformers/models/mpnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4046 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mpnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5442 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/mpnet/configuration_mpnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    42985 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mpnet/modeling_mpnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    53088 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mpnet/modeling_tf_mpnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22022 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mpnet/tokenization_mpnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8930 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mpnet/tokenization_mpnet_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.876988 adapter-transformers-3.2.1/src/transformers/models/mt5/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3465 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mt5/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7587 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mt5/configuration_mt5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4178 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mt5/modeling_flax_mt5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    88845 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mt5/modeling_mt5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3325 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/mt5/modeling_tf_mt5.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.878235 adapter-transformers-3.2.1/src/transformers/models/mvp/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2707 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mvp/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8510 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mvp/configuration_mvp.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    95195 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mvp/modeling_mvp.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16814 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mvp/tokenization_mvp.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12079 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/mvp/tokenization_mvp_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.878963 adapter-transformers-3.2.1/src/transformers/models/nat/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1984 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nat/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6864 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nat/configuration_nat.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    40412 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nat/modeling_nat.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.880022 adapter-transformers-3.2.1/src/transformers/models/nezha/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2441 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nezha/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5226 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nezha/configuration_nezha.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    75338 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nezha/modeling_nezha.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.880823 adapter-transformers-3.2.1/src/transformers/models/nllb/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2039 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nllb/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19325 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nllb/tokenization_nllb.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16313 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nllb/tokenization_nllb_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.881754 adapter-transformers-3.2.1/src/transformers/models/nystromformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2545 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nystromformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6622 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nystromformer/configuration_nystromformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4198 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/nystromformer/convert_nystromformer_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    49115 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/nystromformer/modeling_nystromformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.883867 adapter-transformers-3.2.1/src/transformers/models/oneformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2573 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/oneformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12604 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/oneformer/configuration_oneformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    50722 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/oneformer/convert_to_hf_oneformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    55690 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/oneformer/image_processing_oneformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   141959 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/oneformer/modeling_oneformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9493 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/oneformer/processing_oneformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.886607 adapter-transformers-3.2.1/src/transformers/models/openai/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3829 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/openai/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7331 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/openai/configuration_openai.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2666 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/openai/convert_openai_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    38025 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/openai/modeling_openai.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    40827 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/openai/modeling_tf_openai.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15034 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/openai/tokenization_openai.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3046 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/openai/tokenization_openai_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.888253 adapter-transformers-3.2.1/src/transformers/models/opt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3148 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/opt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7244 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/opt/configuration_opt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3018 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/opt/convert_opt_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    31549 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/opt/modeling_flax_opt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    56984 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/opt/modeling_opt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    46429 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/opt/modeling_tf_opt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.890067 adapter-transformers-3.2.1/src/transformers/models/owlvit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3086 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17352 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/configuration_owlvit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13925 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/convert_owlvit_original_flax_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1186 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/feature_extraction_owlvit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23834 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/image_processing_owlvit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    77112 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/modeling_owlvit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11095 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/owlvit/processing_owlvit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.892272 adapter-transformers-3.2.1/src/transformers/models/pegasus/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4282 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7692 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/configuration_pegasus.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5362 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/convert_pegasus_tf_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    66012 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/modeling_flax_pegasus.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    81895 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/modeling_pegasus.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    70993 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/modeling_tf_pegasus.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13708 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/tokenization_pegasus.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9936 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus/tokenization_pegasus_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.892929 adapter-transformers-3.2.1/src/transformers/models/pegasus_x/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2036 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus_x/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8618 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus_x/configuration_pegasus_x.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    79258 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/pegasus_x/modeling_pegasus_x.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.894558 adapter-transformers-3.2.1/src/transformers/models/perceiver/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3464 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12098 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/configuration_perceiver.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21293 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/convert_perceiver_haiku_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1207 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/feature_extraction_perceiver.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15612 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/image_processing_perceiver.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   145934 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/modeling_perceiver.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8945 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/perceiver/tokenization_perceiver.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.894888 adapter-transformers-3.2.1/src/transformers/models/phobert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1126 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/phobert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13557 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/phobert/tokenization_phobert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.896872 adapter-transformers-3.2.1/src/transformers/models/plbart/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2600 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/plbart/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8718 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/plbart/configuration_plbart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3553 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/plbart/convert_plbart_original_checkpoint_to_torch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    82743 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/plbart/modeling_plbart.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21655 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/plbart/tokenization_plbart.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.898388 adapter-transformers-3.2.1/src/transformers/models/poolformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2794 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/poolformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5802 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/poolformer/configuration_poolformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7973 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/poolformer/convert_poolformer_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1214 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/poolformer/feature_extraction_poolformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18379 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/poolformer/image_processing_poolformer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    18074 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/poolformer/modeling_poolformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.899612 adapter-transformers-3.2.1/src/transformers/models/prophetnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2328 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/prophetnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9061 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/prophetnet/configuration_prophetnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7055 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/prophetnet/convert_prophetnet_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   114040 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/prophetnet/modeling_prophetnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21285 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/prophetnet/tokenization_prophetnet.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.900247 adapter-transformers-3.2.1/src/transformers/models/qdqbert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2573 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/qdqbert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5894 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/qdqbert/configuration_qdqbert.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    77254 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/qdqbert/modeling_qdqbert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.901783 adapter-transformers-3.2.1/src/transformers/models/rag/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2597 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rag/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8799 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rag/configuration_rag.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    85993 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rag/modeling_rag.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    87645 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rag/modeling_tf_rag.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28512 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/rag/retrieval_rag.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4576 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/rag/tokenization_rag.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.903402 adapter-transformers-3.2.1/src/transformers/models/realm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2846 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/realm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8742 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/realm/configuration_realm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    84554 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/realm/modeling_realm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6380 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/realm/retrieval_realm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    25483 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/realm/tokenization_realm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14580 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/realm/tokenization_realm_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.904713 adapter-transformers-3.2.1/src/transformers/models/reformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3310 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/reformer/__init__.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    13462 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/reformer/configuration_reformer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     7818 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/reformer/convert_reformer_trax_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   115075 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/reformer/modeling_reformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7314 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/reformer/tokenization_reformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4824 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/reformer/tokenization_reformer_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.906128 adapter-transformers-3.2.1/src/transformers/models/regnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2698 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/regnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4087 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/regnet/configuration_regnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11793 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/regnet/convert_regnet_seer_10b_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18738 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/regnet/convert_regnet_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17533 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/regnet/modeling_regnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21006 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/regnet/modeling_tf_regnet.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.908414 adapter-transformers-3.2.1/src/transformers/models/rembert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4685 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7449 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/configuration_rembert.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2208 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/convert_rembert_tf_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    68009 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/modeling_rembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    76231 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/modeling_tf_rembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10491 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/tokenization_rembert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10432 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/rembert/tokenization_rembert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.909849 adapter-transformers-3.2.1/src/transformers/models/resnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2796 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/resnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5330 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/resnet/configuration_resnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7310 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/resnet/convert_resnet_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19433 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/resnet/modeling_resnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20470 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/resnet/modeling_tf_resnet.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.911981 adapter-transformers-3.2.1/src/transformers/models/retribert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2521 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/retribert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5404 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/retribert/configuration_retribert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9462 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/retribert/modeling_retribert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22023 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/retribert/tokenization_retribert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9014 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/retribert/tokenization_retribert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.915746 adapter-transformers-3.2.1/src/transformers/models/roberta/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5262 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7877 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/configuration_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8002 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/convert_roberta_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    56957 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/modeling_flax_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    73943 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/modeling_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    79324 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/modeling_tf_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17956 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/tokenization_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13674 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta/tokenization_roberta_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.917407 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5562 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8023 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/configuration_roberta_prelayernorm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2975 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/convert_roberta_prelayernorm_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    60529 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/modeling_flax_roberta_prelayernorm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    74674 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/modeling_roberta_prelayernorm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    82354 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/modeling_tf_roberta_prelayernorm.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.918633 adapter-transformers-3.2.1/src/transformers/models/roc_bert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3083 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roc_bert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8656 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roc_bert/configuration_roc_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    93089 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roc_bert/modeling_roc_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    50427 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roc_bert/tokenization_roc_bert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.921137 adapter-transformers-3.2.1/src/transformers/models/roformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5504 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7710 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/configuration_roformer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2240 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/convert_roformer_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    39460 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/modeling_flax_roformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    69448 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/modeling_roformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    62090 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/modeling_tf_roformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23274 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/tokenization_roformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8277 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/tokenization_roformer_fast.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2652 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/roformer/tokenization_utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.923480 adapter-transformers-3.2.1/src/transformers/models/segformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3847 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7636 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/configuration_segformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17108 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/convert_segformer_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1207 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/feature_extraction_segformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21425 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/image_processing_segformer.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    35488 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/modeling_segformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    37967 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/segformer/modeling_tf_segformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.926030 adapter-transformers-3.2.1/src/transformers/models/sew/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1949 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14047 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew/configuration_sew.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12744 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew/convert_sew_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    52363 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew/modeling_sew.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.927868 adapter-transformers-3.2.1/src/transformers/models/sew_d/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1975 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew_d/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16038 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew_d/configuration_sew_d.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13574 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew_d/convert_sew_d_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    73091 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/sew_d/modeling_sew_d.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.930245 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2208 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5087 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/configuration_speech_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14760 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/convert_mbart_wav2vec2_seq2seq_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11984 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/convert_speech_to_text_wav2vec2_seq2seq_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    45066 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/modeling_flax_speech_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32889 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/modeling_speech_encoder_decoder.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.932635 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4415 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9509 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/configuration_speech_to_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4509 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/convert_s2t_fairseq_to_tfms.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11492 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/feature_extraction_speech_to_text.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    67018 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/modeling_speech_to_text.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    69768 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/modeling_tf_speech_to_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4817 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/processing_speech_to_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11653 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text/tokenization_speech_to_text.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.934537 adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2337 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6280 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/configuration_speech_to_text_2.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    46179 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/modeling_speech_to_text_2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4789 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/processing_speech_to_text_2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9217 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/tokenization_speech_to_text_2.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.935885 adapter-transformers-3.2.1/src/transformers/models/splinter/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2703 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/splinter/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6119 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/splinter/configuration_splinter.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    53606 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/splinter/modeling_splinter.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22013 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/splinter/tokenization_splinter.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9656 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/splinter/tokenization_splinter_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.936965 adapter-transformers-3.2.1/src/transformers/models/squeezebert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3167 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/squeezebert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7909 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/squeezebert/configuration_squeezebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    45098 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/squeezebert/modeling_squeezebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21327 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/squeezebert/tokenization_squeezebert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9396 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/squeezebert/tokenization_squeezebert_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.938341 adapter-transformers-3.2.1/src/transformers/models/swin/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2911 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7829 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin/configuration_swin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6643 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin/convert_swin_simmim_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5817 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin/convert_swin_timm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    59833 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin/modeling_swin.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    65478 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin/modeling_tf_swin.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.940638 adapter-transformers-3.2.1/src/transformers/models/swin2sr/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2485 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin2sr/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6904 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin2sr/configuration_swin2sr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11355 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin2sr/convert_swin2sr_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7762 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swin2sr/image_processing_swin2sr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    51633 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/swin2sr/modeling_swin2sr.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.943049 adapter-transformers-3.2.1/src/transformers/models/swinv2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2075 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swinv2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6521 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swinv2/configuration_swinv2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7699 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swinv2/convert_swinv2_timm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    60852 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/swinv2/modeling_swinv2.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.945566 adapter-transformers-3.2.1/src/transformers/models/switch_transformers/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2655 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/switch_transformers/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10086 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/switch_transformers/configuration_switch_transformers.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7649 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/switch_transformers/convert_big_switch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7593 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/switch_transformers/convert_switch_transformers_original_flax_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    89256 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/switch_transformers/modeling_switch_transformers.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.948933 adapter-transformers-3.2.1/src/transformers/models/t5/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4439 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7430 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/configuration_t5.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2120 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/t5/convert_t5_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10537 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    10365 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/convert_t5x_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    74020 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/modeling_flax_t5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    87946 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/modeling_t5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    75551 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/modeling_tf_t5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15155 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/tokenization_t5.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10586 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/t5/tokenization_t5_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.950104 adapter-transformers-3.2.1/src/transformers/models/table_transformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2233 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/table_transformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12559 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/table_transformer/configuration_table_transformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15090 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/table_transformer/convert_table_transformer_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    92611 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/table_transformer/modeling_table_transformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.954693 adapter-transformers-3.2.1/src/transformers/models/tapas/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3123 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapas/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12900 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapas/configuration_tapas.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5049 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/tapas/convert_tapas_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   111502 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapas/modeling_tapas.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   108613 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapas/modeling_tf_tapas.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   120557 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapas/tokenization_tapas.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.955231 adapter-transformers-3.2.1/src/transformers/models/tapex/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1138 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapex/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    65000 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/tapex/tokenization_tapex.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.955924 adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2277 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11563 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/configuration_time_series_transformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    92619 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/modeling_time_series_transformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.957275 adapter-transformers-3.2.1/src/transformers/models/timesformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2033 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/timesformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5667 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/timesformer/configuration_timesformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10188 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/timesformer/convert_timesformer_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32941 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/timesformer/modeling_timesformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.958183 adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2284 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7651 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/configuration_trajectory_transformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3139 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    26128 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/modeling_trajectory_transformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.960072 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3353 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7894 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/configuration_transfo_xl.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     4916 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/convert_transfo_xl_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    47146 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_tf_transfo_xl.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7597 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_tf_transfo_xl_utilities.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    55824 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_transfo_xl.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10675 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_transfo_xl_utilities.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    30487 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/transfo_xl/tokenization_transfo_xl.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.961120 adapter-transformers-3.2.1/src/transformers/models/trocr/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1989 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trocr/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6975 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trocr/configuration_trocr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10163 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trocr/convert_trocr_unilm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    47404 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/trocr/modeling_trocr.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5687 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/trocr/processing_trocr.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.961941 adapter-transformers-3.2.1/src/transformers/models/unispeech/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2189 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16969 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech/configuration_unispeech.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11340 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech/convert_unispeech_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    70135 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech/modeling_unispeech.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.963004 adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2438 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18392 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/configuration_unispeech_sat.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4870 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/convert_unispeech_original_s3prl_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9289 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/convert_unispeech_sat_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    83730 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/modeling_unispeech_sat.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.964842 adapter-transformers-3.2.1/src/transformers/models/upernet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1743 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/upernet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5438 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/upernet/configuration_upernet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10271 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/upernet/convert_convnext_upernet_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14026 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/upernet/convert_swin_upernet_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17158 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/upernet/modeling_upernet.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.965597 adapter-transformers-3.2.1/src/transformers/models/van/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1935 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/van/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4834 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/van/configuration_van.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10386 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/van/convert_van_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21547 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/van/modeling_van.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.966808 adapter-transformers-3.2.1/src/transformers/models/videomae/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2690 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/videomae/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6717 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/videomae/configuration_videomae.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12398 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/videomae/convert_videomae_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1200 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/videomae/feature_extraction_videomae.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17326 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/videomae/image_processing_videomae.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    44439 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/videomae/modeling_videomae.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.968335 adapter-transformers-3.2.1/src/transformers/models/vilt/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2996 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6928 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/configuration_vilt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12878 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/convert_vilt_original_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1172 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/feature_extraction_vilt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22924 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/image_processing_vilt.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    64920 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/modeling_vilt.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6020 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vilt/processing_vilt.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.969641 adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2798 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8785 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/configuration_vision_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    41659 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/modeling_flax_vision_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    38296 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/modeling_tf_vision_encoder_decoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    35014 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/modeling_vision_encoder_decoder.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.970958 adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2410 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5289 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    26682 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/modeling_flax_vision_text_dual_encoder.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    25326 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6977 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/processing_vision_text_dual_encoder.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.972031 adapter-transformers-3.2.1/src/transformers/models/visual_bert/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2406 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/visual_bert/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7941 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/visual_bert/configuration_visual_bert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5158 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/models/visual_bert/convert_visual_bert_original_pytorch_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    69863 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/visual_bert/modeling_visual_bert.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.974035 adapter-transformers-3.2.1/src/transformers/models/vit/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3769 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5835 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/configuration_vit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8868 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/convert_dino_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10206 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/convert_vit_timm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1165 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/vit/feature_extraction_vit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13293 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/image_processing_vit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    25335 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/modeling_flax_vit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33758 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/modeling_tf_vit.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    36262 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit/modeling_vit.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.975057 adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2487 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7222 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/configuration_vit_hybrid.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13413 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/convert_vit_hybrid_timm_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16173 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/image_processing_vit_hybrid.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    31784 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/modeling_vit_hybrid.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.976329 adapter-transformers-3.2.1/src/transformers/models/vit_mae/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2599 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_mae/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6567 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_mae/configuration_vit_mae.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7532 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_mae/convert_vit_mae_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    49403 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/vit_mae/modeling_tf_vit_mae.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    43357 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_mae/modeling_vit_mae.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.977089 adapter-transformers-3.2.1/src/transformers/models/vit_msn/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1954 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_msn/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5061 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_msn/configuration_vit_msn.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9857 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_msn/convert_msn_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    29825 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/vit_msn/modeling_vit_msn.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.980271 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4214 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19604 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/configuration_wav2vec2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11206 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/convert_wav2vec2_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4838 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/convert_wav2vec2_original_s3prl_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11205 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/feature_extraction_wav2vec2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    57334 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/modeling_flax_wav2vec2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    72232 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/modeling_tf_wav2vec2.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    92946 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/modeling_wav2vec2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7136 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/processing_wav2vec2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    38899 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2/tokenization_wav2vec2.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.981393 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2546 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    20727 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/configuration_wav2vec2_conformer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13382 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/convert_wav2vec2_conformer_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    95389 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/modeling_wav2vec2_conformer.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.982246 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_phoneme/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1164 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_phoneme/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    25933 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.982757 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_with_lm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1152 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_with_lm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    26839 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/wav2vec2_with_lm/processing_wav2vec2_with_lm.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.984160 adapter-transformers-3.2.1/src/transformers/models/wavlm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2130 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wavlm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18413 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wavlm/configuration_wavlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8581 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wavlm/convert_wavlm_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4814 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/wavlm/convert_wavlm_original_s3prl_checkpoint_to_pytorch.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    77406 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/wavlm/modeling_wavlm.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.989230 adapter-transformers-3.2.1/src/transformers/models/whisper/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3100 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12993 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/configuration_whisper.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7657 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/convert_openai_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22952 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/english_normalizer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13330 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/feature_extraction_whisper.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    64909 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/modeling_tf_whisper.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    59102 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/modeling_whisper.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3744 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/processing_whisper.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    27452 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/whisper/tokenization_whisper.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.993952 adapter-transformers-3.2.1/src/transformers/models/x_clip/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2224 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/x_clip/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    17775 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/x_clip/configuration_x_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    18077 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/x_clip/convert_x_clip_original_pytorch_to_hf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    67297 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/x_clip/modeling_x_clip.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6839 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/x_clip/processing_x_clip.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.996789 adapter-transformers-3.2.1/src/transformers/models/xglm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4079 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6054 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/configuration_xglm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2325 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/convert_xglm_original_ckpt_to_trfms.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33623 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/modeling_flax_xglm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    44177 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/modeling_tf_xglm.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    45212 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/modeling_xglm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13276 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/tokenization_xglm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8032 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xglm/tokenization_xglm_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:03.998970 adapter-transformers-3.2.1/src/transformers/models/xlm/
+-rw-r--r--   0 hsterz     (501) staff       (20)     3463 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11974 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm/configuration_xlm.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     2946 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm/convert_xlm_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    55940 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/xlm/modeling_tf_xlm.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    54942 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm/modeling_xlm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    34979 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm/tokenization_xlm.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.000261 adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2786 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9124 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/configuration_xlm_prophetnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   118071 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/modeling_xlm_prophetnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13907 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/tokenization_xlm_prophetnet.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.002073 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/
+-rw-r--r--   0 hsterz     (501) staff       (20)     5996 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8345 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/configuration_xlm_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    58614 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/modeling_flax_xlm_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    81329 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/modeling_tf_xlm_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    75680 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14284 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10263 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/tokenization_xlm_roberta_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.003135 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2576 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7594 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/configuration_xlm_roberta_xl.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8228 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/convert_xlm_roberta_xl_original_pytorch_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    70196 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/modeling_xlm_roberta_xl.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.005185 adapter-transformers-3.2.1/src/transformers/models/xlnet/
+-rw-r--r--   0 hsterz     (501) staff       (20)     4459 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11142 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/configuration_xlnet.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)     3688 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/convert_xlnet_original_tf_checkpoint_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    77793 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/modeling_tf_xlnet.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    93010 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/modeling_xlnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15990 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/tokenization_xlnet.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10025 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/xlnet/tokenization_xlnet_fast.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.006687 adapter-transformers-3.2.1/src/transformers/models/yolos/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2571 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yolos/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7790 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yolos/configuration_yolos.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11275 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yolos/convert_yolos_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1179 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/models/yolos/feature_extraction_yolos.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    53221 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yolos/image_processing_yolos.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    58802 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yolos/modeling_yolos.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.007513 adapter-transformers-3.2.1/src/transformers/models/yoso/
+-rw-r--r--   0 hsterz     (501) staff       (20)     2282 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yoso/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6901 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yoso/configuration_yoso.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4116 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yoso/convert_yoso_pytorch_to_pytorch.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    55127 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/models/yoso/modeling_yoso.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.009918 adapter-transformers-3.2.1/src/transformers/onnx/
+-rw-r--r--   0 hsterz     (501) staff       (20)     1563 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/onnx/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9353 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/onnx/__main__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    32531 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/onnx/config.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    21583 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/onnx/convert.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28303 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/onnx/features.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     3625 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/onnx/utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    27775 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/optimization.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16558 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/optimization_tf.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.016144 adapter-transformers-3.2.1/src/transformers/pipelines/
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    41801 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6695 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/audio_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8095 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/pipelines/audio_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    34553 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/automatic_speech_recognition.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    49295 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/base.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    13596 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/pipelines/conversational.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4260 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/depth_estimation.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22458 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/document_question_answering.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4690 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/feature_extraction.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10687 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/pipelines/fill_mask.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4942 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/image_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     8056 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/image_segmentation.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4882 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/image_to_text.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7475 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/object_detection.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    12624 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/pt_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    29389 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/question_answering.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    19893 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/table_question_answering.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    16759 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/text2text_generation.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10042 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/pipelines/text_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14479 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/text_generation.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    22806 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/token_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5012 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/video_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5970 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/visual_question_answering.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11983 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/pipelines/zero_shot_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     6010 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/zero_shot_image_classification.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9033 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pipelines/zero_shot_object_detection.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    10857 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/processing_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11218 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/pytorch_utils.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.016816 adapter-transformers-3.2.1/src/transformers/sagemaker/
+-rw-r--r--   0 hsterz     (501) staff       (20)      901 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/sagemaker/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     1044 2023-01-11 18:45:51.000000 adapter-transformers-3.2.1/src/transformers/sagemaker/trainer_sm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5411 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/sagemaker/training_args_sm.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    58008 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/testing_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2639 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/tf_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    39944 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/tokenization_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   179682 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/tokenization_utils_base.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    33226 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/tokenization_utils_fast.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)   176752 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/trainer.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23845 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/trainer_callback.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    46985 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/trainer_pt_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11729 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/trainer_seq2seq.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    34693 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/trainer_tf.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    23896 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/trainer_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    89763 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/training_args.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2901 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/training_args_seq2seq.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14190 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/training_args_tf.py
+drwxr-xr-x   0 hsterz     (501) staff       (20)        0 2023-04-06 21:08:04.024016 adapter-transformers-3.2.1/src/transformers/utils/
+-rw-r--r--   0 hsterz     (501) staff       (20)     6293 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/__init__.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     7489 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/bitsandbytes.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      172 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/constants.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    39982 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/doc.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      391 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_detectron2_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    28808 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_flax_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      309 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_keras_nlp_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)   162054 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_pt_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      342 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_sentencepiece_and_speech_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      301 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_sentencepiece_and_tokenizers_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     5064 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_sentencepiece_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      647 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_speech_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)      321 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_tensorflow_text_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    63396 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_tf_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2970 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_timm_and_vision_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9910 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_tokenizers_objects.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    11412 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/dummy_vision_objects.py
+-rwxr-xr-x   0 hsterz     (501) staff       (20)    45404 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/fx.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    15863 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/generic.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4971 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/hp_naming.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    47555 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/hub.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    40353 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/import_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     9643 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/logging.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     2300 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/model_parallel_utils.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    14831 2023-03-08 18:59:04.000000 adapter-transformers-3.2.1/src/transformers/utils/notebook.py
+-rw-r--r--   0 hsterz     (501) staff       (20)    50686 2023-04-06 20:15:05.000000 adapter-transformers-3.2.1/src/transformers/utils/sentencepiece_model_pb2.py
+-rw-r--r--   0 hsterz     (501) staff       (20)     4518 2023-02-21 21:41:49.000000 adapter-transformers-3.2.1/src/transformers/utils/versions.py
```

### Comparing `adapter-transformers-3.2.0/LICENSE` & `adapter-transformers-3.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/PKG-INFO` & `adapter-transformers-3.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 Metadata-Version: 2.1
 Name: adapter-transformers
-Version: 3.2.0
+Version: 3.2.1
 Summary: A friendly fork of HuggingFace's Transformers, adding Adapters to PyTorch language models
 Home-page: https://github.com/adapter-hub/adapter-transformers
 Author: Jonas Pfeiffer, Andreas Rücklé, Clifton Poth, Hannah Sterz, Leon Engländer, based on work by the HuggingFace team and community
 Author-email: pfeiffer@ukp.tu-darmstadt.de
 License: Apache
 Keywords: NLP deep learning transformer pytorch BERT adapters
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Education
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
-Requires-Python: >=3.7.0
+Requires-Python: >=3.8.0
 Description-Content-Type: text/markdown
 Provides-Extra: ja
 Provides-Extra: sklearn
 Provides-Extra: tf
 Provides-Extra: tf-cpu
 Provides-Extra: torch
 Provides-Extra: accelerate
@@ -98,15 +98,15 @@
 `adapter-transformers` is an extension of [HuggingFace's Transformers](https://github.com/huggingface/transformers) library, integrating adapters into state-of-the-art language models by incorporating **[AdapterHub](https://adapterhub.ml)**, a central repository for pre-trained adapter modules.
 
 _💡 Important: This library can be used as a drop-in replacement for HuggingFace Transformers and regularly synchronizes new upstream changes.
 Thus, most files in this repository are direct copies from the HuggingFace Transformers source, modified only with changes required for the adapter implementations._
 
 ## Installation
 
-`adapter-transformers` currently supports **Python 3.7+** and **PyTorch 1.3.1+**.
+`adapter-transformers` currently supports **Python 3.8+** and **PyTorch 1.12.1+**.
 After [installing PyTorch](https://pytorch.org/get-started/locally/), you can install `adapter-transformers` from PyPI ...
 
 ```
 pip install -U adapter-transformers
 ```
 
 ... or from source by cloning the repository:
```

### Comparing `adapter-transformers-3.2.0/README.md` & `adapter-transformers-3.2.1/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -32,15 +32,15 @@
 `adapter-transformers` is an extension of [HuggingFace's Transformers](https://github.com/huggingface/transformers) library, integrating adapters into state-of-the-art language models by incorporating **[AdapterHub](https://adapterhub.ml)**, a central repository for pre-trained adapter modules.
 
 _💡 Important: This library can be used as a drop-in replacement for HuggingFace Transformers and regularly synchronizes new upstream changes.
 Thus, most files in this repository are direct copies from the HuggingFace Transformers source, modified only with changes required for the adapter implementations._
 
 ## Installation
 
-`adapter-transformers` currently supports **Python 3.7+** and **PyTorch 1.3.1+**.
+`adapter-transformers` currently supports **Python 3.8+** and **PyTorch 1.12.1+**.
 After [installing PyTorch](https://pytorch.org/get-started/locally/), you can install `adapter-transformers` from PyPI ...
 
 ```
 pip install -U adapter-transformers
 ```
 
 ... or from source by cloning the repository:
```

### Comparing `adapter-transformers-3.2.0/setup.cfg` & `adapter-transformers-3.2.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/setup.py` & `adapter-transformers-3.2.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -142,15 +142,15 @@
     "psutil",
     "pyyaml>=5.1",
     "pydantic",
     "pytest",
     "pytest-subtests",
     "pytest-timeout",
     "pytest-xdist",
-    "python>=3.7.0",
+    "python>=3.8.0",
     "ray[tune]",
     "myst-parser",
     "regex!=2019.12.17",
     "requests",
     "rjieba",
     "rouge-score!=0.0.7,!=0.0.8,!=0.1,!=0.1.1",
     "sacrebleu>=1.4.12,<2.0.0",
@@ -172,15 +172,15 @@
     "tensorflow-cpu>=2.4,<2.12",
     "tensorflow>=2.4,<2.12",
     "tensorflow-text",
     "tf2onnx",
     "timeout-decorator",
     "timm",
     "tokenizers>=0.11.1,!=0.11.3,<0.14",
-    "torch>=1.7,!=1.12.0",
+    "torch>=1.12.1",
     "torchaudio",
     "pyctcdecode>=0.4.0",
     "tqdm>=4.27",
     "unidic>=1.0.2",
     "unidic_lite>=1.0.7",
     "uvicorn",
     "beautifulsoup4",
@@ -249,14 +249,15 @@
             "",
         ]
         target = "src/transformers/dependency_versions_table.py"
         print(f"updating {target}")
         with open(target, "w", encoding="utf-8", newline="\n") as f:
             f.write("\n".join(content))
 
+
 extras = {}
 
 extras["ja"] = deps_list("fugashi", "ipadic", "unidic_lite", "unidic", "sudachipy", "sudachidict_core", "rhoknp")
 extras["sklearn"] = deps_list("scikit-learn")
 
 extras["tf"] = deps_list("tensorflow", "onnxconverter-common", "tf2onnx", "tensorflow-text", "keras-nlp")
 extras["tf-cpu"] = deps_list("tensorflow-cpu", "onnxconverter-common", "tf2onnx", "tensorflow-text", "keras-nlp")
@@ -427,15 +428,15 @@
     deps["requests"],  # for downloading models over HTTPS
     deps["tokenizers"],
     deps["tqdm"],  # progress bars in model download and training scripts
 ]
 
 setup(
     name="adapter-transformers",
-    version="3.2.0",
+    version="3.2.1",
     author="Jonas Pfeiffer, Andreas Rücklé, Clifton Poth, Hannah Sterz, Leon Engländer, based on work by the HuggingFace team and community",
     author_email="pfeiffer@ukp.tu-darmstadt.de",
     description="A friendly fork of HuggingFace's Transformers, adding Adapters to PyTorch language models",
     long_description=open("README.md", "r", encoding="utf-8").read(),
     long_description_content_type="text/markdown",
     keywords="NLP deep learning transformer pytorch BERT adapters",
     license="Apache",
@@ -443,24 +444,24 @@
     package_dir={"": "src"},
     packages=find_packages("src"),
     include_package_data=True,
     package_data={"transformers": ["*.cu", "*.cpp", "*.cuh", "*.h", "*.pyx"]},
     zip_safe=False,
     extras_require=extras,
     entry_points={"console_scripts": ["transformers-cli=transformers.commands.transformers_cli:main"]},
-    python_requires=">=3.7.0",
+    python_requires=">=3.8.0",
     install_requires=install_requires,
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Intended Audience :: Developers",
         "Intended Audience :: Education",
         "Intended Audience :: Science/Research",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
         "Programming Language :: Python :: 3",
-        "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
+        "Programming Language :: Python :: 3.10",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
     ],
     cmdclass={"deps_table_update": DepsTableUpdateCommand},
 )
```

### Comparing `adapter-transformers-3.2.0/src/adapter_transformers.egg-info/PKG-INFO` & `adapter-transformers-3.2.1/src/adapter_transformers.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,28 +1,28 @@
 Metadata-Version: 2.1
 Name: adapter-transformers
-Version: 3.2.0
+Version: 3.2.1
 Summary: A friendly fork of HuggingFace's Transformers, adding Adapters to PyTorch language models
 Home-page: https://github.com/adapter-hub/adapter-transformers
 Author: Jonas Pfeiffer, Andreas Rücklé, Clifton Poth, Hannah Sterz, Leon Engländer, based on work by the HuggingFace team and community
 Author-email: pfeiffer@ukp.tu-darmstadt.de
 License: Apache
 Keywords: NLP deep learning transformer pytorch BERT adapters
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Education
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
-Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
-Requires-Python: >=3.7.0
+Requires-Python: >=3.8.0
 Description-Content-Type: text/markdown
 Provides-Extra: ja
 Provides-Extra: sklearn
 Provides-Extra: tf
 Provides-Extra: tf-cpu
 Provides-Extra: torch
 Provides-Extra: accelerate
@@ -98,15 +98,15 @@
 `adapter-transformers` is an extension of [HuggingFace's Transformers](https://github.com/huggingface/transformers) library, integrating adapters into state-of-the-art language models by incorporating **[AdapterHub](https://adapterhub.ml)**, a central repository for pre-trained adapter modules.
 
 _💡 Important: This library can be used as a drop-in replacement for HuggingFace Transformers and regularly synchronizes new upstream changes.
 Thus, most files in this repository are direct copies from the HuggingFace Transformers source, modified only with changes required for the adapter implementations._
 
 ## Installation
 
-`adapter-transformers` currently supports **Python 3.7+** and **PyTorch 1.3.1+**.
+`adapter-transformers` currently supports **Python 3.8+** and **PyTorch 1.12.1+**.
 After [installing PyTorch](https://pytorch.org/get-started/locally/), you can install `adapter-transformers` from PyPI ...
 
 ```
 pip install -U adapter-transformers
 ```
 
 ... or from source by cloning the repository:
```

### Comparing `adapter-transformers-3.2.0/src/adapter_transformers.egg-info/SOURCES.txt` & `adapter-transformers-3.2.1/src/adapter_transformers.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/adapter_transformers.egg-info/requires.txt` & `adapter-transformers-3.2.1/src/adapter_transformers.egg-info/requires.txt`

 * *Files 5% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 
 [all]
 tensorflow<2.12,>=2.4
 onnxconverter-common
 tf2onnx
 tensorflow-text
 keras-nlp>=0.3.1
-torch!=1.12.0,>=1.7
+torch>=1.12.1
 jax!=0.3.2,<=0.3.6,>=0.2.8
 jaxlib<=0.3.6,>=0.1.65
 flax>=0.4.1
 optax>=0.0.8
 sentencepiece!=0.1.92,>=0.1.91
 protobuf<=3.20.2
 tokenizers!=0.11.3,<0.14,>=0.11.1
@@ -85,15 +85,15 @@
 
 [dev]
 tensorflow<2.12,>=2.4
 onnxconverter-common
 tf2onnx
 tensorflow-text
 keras-nlp>=0.3.1
-torch!=1.12.0,>=1.7
+torch>=1.12.1
 jax!=0.3.2,<=0.3.6,>=0.2.8
 jaxlib<=0.3.6,>=0.1.65
 flax>=0.4.1
 optax>=0.0.8
 sentencepiece!=0.1.92,>=0.1.91
 protobuf<=3.20.2
 tokenizers!=0.11.3,<0.14,>=0.11.1
@@ -220,15 +220,15 @@
 protobuf<=3.20.2
 sacremoses
 rjieba
 safetensors>=0.2.1
 beautifulsoup4
 faiss-cpu
 cookiecutter==1.7.3
-torch!=1.12.0,>=1.7
+torch>=1.12.1
 sentencepiece!=0.1.92,>=0.1.91
 tokenizers!=0.11.3,<0.14,>=0.11.1
 torchaudio
 librosa
 pyctcdecode>=0.4.0
 phonemizer
 kenlm
@@ -262,15 +262,15 @@
 
 [docs]
 tensorflow<2.12,>=2.4
 onnxconverter-common
 tf2onnx
 tensorflow-text
 keras-nlp>=0.3.1
-torch!=1.12.0,>=1.7
+torch>=1.12.1
 jax!=0.3.2,<=0.3.6,>=0.2.8
 jaxlib<=0.3.6,>=0.1.65
 flax>=0.4.1
 optax>=0.0.8
 sentencepiece!=0.1.92,>=0.1.91
 protobuf<=3.20.2
 tokenizers!=0.11.3,<0.14,>=0.11.1
@@ -447,15 +447,15 @@
 [timm]
 timm
 
 [tokenizers]
 tokenizers!=0.11.3,<0.14,>=0.11.1
 
 [torch]
-torch!=1.12.0,>=1.7
+torch>=1.12.1
 
 [torch-speech]
 torchaudio
 librosa
 pyctcdecode>=0.4.0
 phonemizer
 kenlm
@@ -466,15 +466,15 @@
 importlib_metadata
 numpy>=1.17
 packaging>=20.0
 protobuf<=3.20.2
 regex!=2019.12.17
 requests
 sentencepiece!=0.1.92,>=0.1.91
-torch!=1.12.0,>=1.7
+torch>=1.12.1
 tokenizers!=0.11.3,<0.14,>=0.11.1
 tqdm>=4.27
 
 [video]
 decord==0.6.0
 
 [vision]
```

### Comparing `adapter-transformers-3.2.0/src/transformers/__init__.py` & `adapter-transformers-3.2.1/src/transformers/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/activations.py` & `adapter-transformers-3.2.1/src/transformers/activations.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/activations_tf.py` & `adapter-transformers-3.2.1/src/transformers/activations_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
-__version__ = "3.2.0"
+__version__ = "3.2.1"
 
 from typing import TYPE_CHECKING
 
 from ..utils import _LazyModule
 
 
 _import_structure = {
```

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/composition.py` & `adapter-transformers-3.2.1/src/transformers/adapters/composition.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/configuration.py` & `adapter-transformers-3.2.1/src/transformers/adapters/configuration.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/context.py` & `adapter-transformers-3.2.1/src/transformers/adapters/context.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/head_utils.py` & `adapter-transformers-3.2.1/src/transformers/adapters/head_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/heads/base.py` & `adapter-transformers-3.2.1/src/transformers/adapters/heads/base.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/heads/dependency_parsing.py` & `adapter-transformers-3.2.1/src/transformers/adapters/heads/dependency_parsing.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/heads/language_modeling.py` & `adapter-transformers-3.2.1/src/transformers/adapters/heads/language_modeling.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/hub_mixin.py` & `adapter-transformers-3.2.1/src/transformers/adapters/hub_mixin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/layer.py` & `adapter-transformers-3.2.1/src/transformers/adapters/layer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/loading.py` & `adapter-transformers-3.2.1/src/transformers/adapters/loading.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/lora.py` & `adapter-transformers-3.2.1/src/transformers/adapters/lora.py`

 * *Files 8% similar despite different names*

```diff
@@ -150,31 +150,45 @@
         if adapter_name in self.loras:
             return self.loras[adapter_name]
         else:
             return None
 
 
 class Linear(LoRALayer, nn.Linear):
-    # LoRA implemented in a dense layer
+    """
+    LoRA implementation for Linear layer.
+
+    Args:
+        fan_in_fan_out (bool, optional):
+            Set this to True if the layer to replace stores weight like (fan_in, fan_out). Defaults to False.
+        no_init_bias (bool, optional): Use this to add a bias that is not initialized by PyTorch. Defaults to False.
+
+    """
+
     def __init__(
         self,
         in_features: int,
         out_features: int,
         location_key: str,
         config: PretrainedConfig,
         attn_key: str = None,
-        fan_in_fan_out: bool = False,  # Set this to True if the layer to replace stores weight like (fan_in, fan_out)
+        fan_in_fan_out: bool = False,
+        no_init_bias: bool = False,
         **kwargs
     ):
+        if no_init_bias and "bias" not in kwargs:
+            kwargs["bias"] = False
         LoRALayer.__init__(self, location_key, config, in_features, out_features, **kwargs)
 
         self.attn_key = attn_key
         self.fan_in_fan_out = fan_in_fan_out
         if fan_in_fan_out:
             self.weight.data = torch.t(self.weight.data)
+        if no_init_bias:
+            self.bias = nn.Parameter(torch.empty(out_features))
 
     def _check_lora_location(self, config: LoRAConfig):
         return self.attn_key is None or self.attn_key in config.attn_matrices
 
     def _get_lora_shapes(self, config: LoRAConfig):
         return (config.r, self.in_features), (self.out_features, config.r)
 
@@ -248,29 +262,43 @@
                 else:
                     raise ValueError(f"Invalid adapter setup. Cannot use {adapter_setup} with LoRA.")
 
         return F.linear(x, T(self.weight), bias=self.bias)
 
 
 class MergedLinear(LoRALayer, nn.Linear):
-    # LoRA implemented in a dense layer
+    """
+    LoRA implementation for merged attention layer layer.
+
+    Args:
+        fan_in_fan_out (bool, optional):
+            Set this to True if the layer to replace stores weight like (fan_in, fan_out). Defaults to False.
+        no_init_bias (bool, optional): Use this to add a bias that is not initialized by PyTorch. Defaults to False.
+
+    """
+
     def __init__(
         self,
         in_features: int,
         out_features: int,
         location_key: str,
         config: PretrainedConfig,
         fan_in_fan_out: bool = False,
+        no_init_bias: bool = False,
         **kwargs
     ):
+        if no_init_bias and "bias" not in kwargs:
+            kwargs["bias"] = False
         LoRALayer.__init__(self, location_key, config, in_features, out_features, **kwargs)
 
         self.fan_in_fan_out = fan_in_fan_out
         if fan_in_fan_out:
             self.weight.data = self.weight.data.T
+        if no_init_bias:
+            self.bias = nn.Parameter(torch.empty(out_features))
 
     def get_n_heads(self, lora: Union[LoRA, LoRAConfig]):
         return len(set(lora.attn_matrices))
 
     def _get_lora_shapes(self, config: LoRAConfig):
         n_heads = self.get_n_heads(config)
         return (config.r * n_heads, self.in_features), (
```

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/albert.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/albert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/bart.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/bart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/beit.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/beit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/bert.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/clip.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/distilbert.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/distilbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/gpt2.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/gpt2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/gptj.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/gptj.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/t5.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/t5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/mixins/vit.py` & `adapter-transformers-3.2.1/src/transformers/adapters/mixins/vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/model_mixin.py` & `adapter-transformers-3.2.1/src/transformers/adapters/model_mixin.py`

 * *Files 1% similar despite different names*

```diff
@@ -18,18 +18,18 @@
     get_adapter_config_hash,
 )
 from .context import AdapterSetup, ForwardContext
 from .hub_mixin import PushAdapterToHubMixin
 from .layer import AdapterLayer, AdapterLayerBase
 from .loading import AdapterFusionLoader, AdapterLoader, PredictionHeadLoader, WeightsLoader
 from .lora import LoRALayer
-from .modeling import Adapter, GLOWCouplingBlock, NICECouplingBlock
+from .modeling import Adapter, GLOWCouplingBlock, NICECouplingBlock, init_shared_parameters
 from .prefix_tuning import PrefixTuningPool, PrefixTuningShim
 from .utils import EMBEDDING_FILE, TOKENIZER_PATH, inherit_doc
-from .wrappers.configuration import wrap_config
+from .wrappers.configuration import SUBMODEL_NAMES, wrap_config
 
 
 logger = logging.getLogger(__name__)
 
 
 class InvertibleAdaptersMixin:
     """Mixin for Transformer models adding invertible adapters."""
@@ -491,20 +491,38 @@
         if set_active:
             self.set_active_adapters(adapter_name)
 
     def _add_adapter_weights(self, adapter_name: str):
         """Helper method that performs the actual parameter additions when adding a new adapter."""
         self.apply_to_adapter_layers(lambda i, layer: layer.add_adapter(adapter_name, i))
         # PHM Layer
-        if self.config.adapters.match(adapter_name, AdapterConfig, location_key="phm_layer"):
+        adapter_config = self.config.adapters.match(adapter_name, AdapterConfig, location_key="phm_layer")
+        if adapter_config:
             adapter_module = list(self.get_adapter(adapter_name)[0].values())[0]
             # if multiple adapters with same location key exist they are returned as a modulelist
             if isinstance(adapter_module, nn.ModuleList):
                 adapter_module = adapter_module[0]
-            self.base_model.shared_parameters[adapter_name] = adapter_module.adapter_down[0].init_shared_parameters()
+            if adapter_config["shared_phm_rule"] or adapter_config["shared_W_phm"]:
+                if self.config.model_type in SUBMODEL_NAMES:
+                    hidden_sizes = [
+                        getattr(self.config, key).hidden_size for key in SUBMODEL_NAMES[self.config.model_type]
+                    ]
+                    if all(hidden_sizes[0] == h for h in hidden_sizes):
+                        self.base_model.shared_parameters[adapter_name] = init_shared_parameters(
+                            adapter_config, hidden_sizes[0], self.device
+                        )
+                    else:
+                        raise ValueError(
+                            "The model has different hidden sizes {}. Sharing comapcter weights is only possible if"
+                            " the hidden_sizes match.".format(hidden_sizes)
+                        )
+                else:
+                    self.base_model.shared_parameters[adapter_name] = init_shared_parameters(
+                        adapter_config, self.config.hidden_size, self.device
+                    )
         # Prefix Tuning
         for module in self.modules():
             if isinstance(module, PrefixTuningPool):
                 module.confirm_prefix(adapter_name)
         if isinstance(self, InvertibleAdaptersMixin) or isinstance(self, InvertibleAdaptersWrapperMixin):
             self.add_invertible_adapter(adapter_name)
```

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/modeling.py` & `adapter-transformers-3.2.1/src/transformers/adapters/modeling.py`

 * *Files 5% similar despite different names*

```diff
@@ -564,14 +564,15 @@
         assert config["phm_c_init"] in ["normal", "uniform"]
         assert (
             in_features % config["phm_dim"] == 0
         ), f"Argument `in_features`={in_features} is not divisble be `phm_dim`{config['phm_dim']}"
         assert (
             out_features % config["phm_dim"] == 0
         ), f"Argument `out_features`={out_features} is not divisble be `phm_dim`{config['phm_dim']}"
+        self.config = config
         self.name = adapter_name
         self.in_features = in_features
         self.out_features = out_features
         self.position = position
         self.learn_phm = config["learn_phm"]
         self.phm_dim = config["phm_dim"]
         self._in_feats_per_axis = in_features // config["phm_dim"]
@@ -612,50 +613,26 @@
                 )
         if self.bias_flag:
             self.b = nn.Parameter(torch.Tensor(out_features))
         else:
             self.register_parameter("b", None)
         self.reset_parameters()
 
-    def init_W(self, W_left=None, W_right=None, W=None):
+    def _init_W(self, W_left=None, W_right=None, W=None):
         if self.factorized_phm_W:
             W_left = W_left if W_left is not None else self.W_left
             W_right = W_right if W_right is not None else self.W_right
+            return init_W(self.config, W_left, W_right, W)
         else:
             W = W if W is not None else self.W
-        if self.w_init == "glorot-normal":
-            if self.factorized_phm_W:
-                for i in range(self.phm_dim):
-                    W_left.data[i] = nn.init.xavier_normal_(W_left.data[i])
-                    W_right.data[i] = nn.init.xavier_normal_(W_right.data[i])
-            else:
-                for i in range(self.phm_dim):
-                    W.data[i] = nn.init.xavier_normal_(W.data[i])
-        elif self.w_init == "glorot-uniform":
-            if self.factorized_phm_W:
-                for i in range(self.phm_dim):
-                    W_left.data[i] = nn.init.xavier_uniform_(W_left.data[i])
-                    W_right.data[i] = nn.init.xavier_uniform_(W_right.data[i])
-            else:
-                for i in range(self.phm_dim):
-                    W.data[i] = nn.init.xavier_uniform_(W.data[i])
-        elif self.w_init == "normal":
-            if self.factorized_phm_W:
-                for i in range(self.phm_dim):
-                    W_left.data[i].normal_(mean=0, std=self.phm_init_range)
-                    W_right.data[i].normal_(mean=0, std=self.phm_init_range)
-            else:
-                for i in range(self.phm_dim):
-                    W.data[i].normal_(mean=0, std=self.phm_init_range)
-        else:
-            raise ValueError
+            return init_W(self.config, W_left, W_right, W)
 
     def reset_parameters(self):
         if not self.shared_W_phm:
-            self.init_W()
+            self._init_W()
 
         if self.bias_flag:
             self.b.data = torch.zeros_like(self.b.data)
 
         if not self.shared_phm_rule:
             if self.factorized_phm_rule:
                 if self.c_init == "uniform":
@@ -719,58 +696,105 @@
         H = kronecker_product(phm_rule, W).sum(0)
 
         y = torch.matmul(input=x, other=H)
         if self.b is not None:
             y += self.b
         return y
 
-    def init_shared_parameters(self):
-        parameters = nn.ParameterDict()
-        if self.shared_W_phm:
-            if self.factorized_phm_W:
-                W_down_left = torch.Tensor(size=(self.phm_dim, self._in_feats_per_axis, self.phm_rank))
-                W_down_right = torch.Tensor(size=(self.phm_dim, self.phm_rank, self._out_feats_per_axis))
-                W_up_left = torch.Tensor(size=(self.phm_dim, self._out_feats_per_axis, self.phm_rank))
-                W_up_right = torch.Tensor(size=(self.phm_dim, self.phm_rank, self._in_feats_per_axis))
-                self.init_W(W_left=W_down_left, W_right=W_down_right)
-                self.init_W(W_left=W_up_left, W_right=W_up_right)
-                parameters["W_down_left"] = nn.Parameter(W_down_left, requires_grad=True)
-                parameters["W_down_right"] = nn.Parameter(W_down_right, requires_grad=True)
-                parameters["W_up_left"] = nn.Parameter(W_up_left, requires_grad=True)
-                parameters["W_up_right"] = nn.Parameter(W_up_right, requires_grad=True)
-            else:
-                W_down = torch.Tensor(size=(self.phm_dim, self._in_feats_per_axis, self._out_feats_per_axis))
-                W_up = torch.Tensor(size=(self.phm_dim, self._out_feats_per_axis, self._in_feats_per_axis))
-                self.init_W(W=W_down)
-                self.init_W(W=W_up)
-                parameters["W_down"] = nn.Parameter(W_down, requires_grad=True)
-                parameters["W_up"] = nn.Parameter(W_up, requires_grad=True)
-        if self.shared_phm_rule:
-            if self.factorized_phm_rule:
-                phm_rule_left = nn.Parameter(
-                    torch.FloatTensor(self.phm_dim, self.phm_dim, 1).to(self.device), requires_grad=self.learn_phm
-                )
-                phm_rule_right = nn.Parameter(
-                    torch.FloatTensor(self.phm_dim, 1, self.phm_dim).to(self.device), requires_grad=self.learn_phm
-                )
-                if self.c_init == "normal":
-                    phm_rule_left.data.normal_(mean=0, std=self.phm_init_range)
-                    phm_rule_right.data.normal_(mean=0, std=self.phm_init_range)
-                elif self.c_init == "uniform":
-                    phm_rule_left.data.uniform_(-1, 1)
-                    phm_rule_right.data.uniform_(-1, 1)
-                else:
-                    raise NotImplementedError
-                parameters["phm_rule_left"] = phm_rule_left
-                parameters["phm_rule_right"] = phm_rule_right
-            else:
-                phm_rule = nn.Parameter(
-                    torch.FloatTensor(self.phm_dim, self.phm_dim, self.phm_dim), requires_grad=self.learn_phm
-                )
-                if self.c_init == "normal":
-                    phm_rule.data.normal_(mean=0, std=self.phm_init_range)
-                elif self.c_init == "uniform":
-                    phm_rule.data.uniform_(-1, 1)
-                else:
-                    raise NotImplementedError
-                parameters["phm_rule"] = phm_rule
-        return parameters
+
+def init_shared_parameters(config, in_features, device):
+    """
+    Create and initialize the parameters shared by all compacter modules
+    """
+    parameters = nn.ParameterDict()
+    if config["shared_W_phm"]:
+        if config["factorized_phm_W"]:
+            out_features = in_features // config["reduction_factor"]
+            _in_feats_per_axis = in_features // config["phm_dim"]
+            _out_feats_per_axis = out_features // config["phm_dim"]
+            W_down_left = torch.Tensor(size=(config["phm_dim"], _in_feats_per_axis, config["phm_rank"]))
+            W_down_right = torch.Tensor(size=(config["phm_dim"], config["phm_rank"], _out_feats_per_axis))
+            W_up_left = torch.Tensor(size=(config["phm_dim"], _out_feats_per_axis, config["phm_rank"]))
+            W_up_right = torch.Tensor(size=(config["phm_dim"], config["phm_rank"], _in_feats_per_axis))
+            init_W(config, W_left=W_down_left, W_right=W_down_right)
+            init_W(config, W_left=W_up_left, W_right=W_up_right)
+            parameters["W_down_left"] = nn.Parameter(W_down_left, requires_grad=True)
+            parameters["W_down_right"] = nn.Parameter(W_down_right, requires_grad=True)
+            parameters["W_up_left"] = nn.Parameter(W_up_left, requires_grad=True)
+            parameters["W_up_right"] = nn.Parameter(W_up_right, requires_grad=True)
+        else:
+            W_down = torch.Tensor(size=(config["phm_dim"], _in_feats_per_axis, _out_feats_per_axis))
+            W_up = torch.Tensor(size=(config["phm_dim"], _out_feats_per_axis, _in_feats_per_axis))
+            init_W(config, W=W_down)
+            init_W(config, W=W_up)
+            parameters["W_down"] = nn.Parameter(W_down, requires_grad=True)
+            parameters["W_up"] = nn.Parameter(W_up, requires_grad=True)
+    if config["shared_phm_rule"]:
+        if config["factorized_phm_rule"]:
+            phm_rule_left = nn.Parameter(
+                torch.FloatTensor(config["phm_dim"], config["phm_dim"], 1).to(device),
+                requires_grad=config["learn_phm"],
+            )
+            phm_rule_right = nn.Parameter(
+                torch.FloatTensor(config["phm_dim"], 1, config["phm_dim"]).to(device),
+                requires_grad=config["learn_phm"],
+            )
+            if config["phm_c_init"] == "normal":
+                phm_rule_left.data.normal_(mean=0, std=config["phm_init_range"])
+                phm_rule_right.data.normal_(mean=0, std=config["phm_init_range"])
+            elif config["phm_c_init"] == "uniform":
+                phm_rule_left.data.uniform_(-1, 1)
+                phm_rule_right.data.uniform_(-1, 1)
+            else:
+                raise NotImplementedError
+            parameters["phm_rule_left"] = phm_rule_left
+            parameters["phm_rule_right"] = phm_rule_right
+        else:
+            phm_rule = nn.Parameter(
+                torch.FloatTensor(config["phm_dim"], config["phm_dim"], config["phm_dim"]),
+                requires_grad=config["learn_phm"],
+            )
+            if config["phm_c_init"] == "normal":
+                phm_rule.data.normal_(mean=0, std=config["phm_init_range"])
+            elif config["phm_c_init"] == "uniform":
+                phm_rule.data.uniform_(-1, 1)
+            else:
+                raise NotImplementedError
+            parameters["phm_rule"] = phm_rule
+    return parameters
+
+
+def init_W(config, W_left=None, W_right=None, W=None):
+    """
+    Initialize the weights for the compacter module or the shared parameters
+    """
+    if config["factorized_phm_W"]:
+        W_left = W_left
+        W_right = W_right
+    else:
+        W = W
+    if config["hypercomplex_nonlinearity"]:
+        if config["factorized_phm_W"]:
+            for i in range(config["phm_dim"]):
+                W_left.data[i] = nn.init.xavier_normal_(W_left.data[i])
+                W_right.data[i] = nn.init.xavier_normal_(W_right.data[i])
+        else:
+            for i in range(config["phm_dim"]):
+                W.data[i] = nn.init.xavier_normal_(W.data[i])
+    elif config["hypercomplex_nonlinearity"] == "glorot-uniform":
+        if config["factorized_phm_W"]:
+            for i in range(config["phm_dim"]):
+                W_left.data[i] = nn.init.xavier_uniform_(W_left.data[i])
+                W_right.data[i] = nn.init.xavier_uniform_(W_right.data[i])
+        else:
+            for i in range(config["phm_dim"]):
+                W.data[i] = nn.init.xavier_uniform_(W.data[i])
+    elif config["hypercomplex_nonlinearity"] == "normal":
+        if config["factorized_phm_W"]:
+            for i in range(config["phm_dim"]):
+                W_left.data[i].normal_(mean=0, std=config["phm_init_range"])
+                W_right.data[i].normal_(mean=0, std=config["phm_init_range"])
+        else:
+            for i in range(config["phm_dim"]):
+                W.data[i].normal_(mean=0, std=config["phm_init_range"])
+    else:
+        raise ValueError
```

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/albert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/albert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/albert/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/albert/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/auto/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/auto/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/auto/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/auto/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/bart/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/bart/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/bart/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/bart/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/beit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/beit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/beit/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/beit/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/bert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/bert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/bert/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/bert/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/bert_generation/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/bert_generation/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/bert_generation/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/bert_generation/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/deberta/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/deberta/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/deberta/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/deberta/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/debertaV2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/debertaV2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/debertaV2/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/debertaV2/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/distilbert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/distilbert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/distilbert/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/distilbert/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/gpt2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/gpt2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/gpt2/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/gpt2/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/gptj/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/gptj/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/gptj/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/gptj/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/mbart/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/mbart/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/mbart/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/mbart/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/roberta/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/roberta/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/roberta/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/roberta/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/t5/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/t5/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/t5/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/t5/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/vit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/vit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/vit/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/vit/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/xlm_roberta/__init__.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/xlm_roberta/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/models/xlm_roberta/adapter_model.py` & `adapter-transformers-3.2.1/src/transformers/adapters/models/xlm_roberta/adapter_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/prefix_tuning.py` & `adapter-transformers-3.2.1/src/transformers/adapters/prefix_tuning.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/trainer.py` & `adapter-transformers-3.2.1/src/transformers/adapters/trainer.py`

 * *Files 1% similar despite different names*

```diff
@@ -178,14 +178,15 @@
                     "yield to errors or unwanted behaviors."
                 )
 
         if args.deepspeed:
             # will be resumed in deepspeed_init
             pass
         else:
+            adapter_loaded = False
             if os.path.isdir(resume_from_checkpoint):
                 adapter_loaded = self._load_adapters(resume_from_checkpoint)
                 self._load_adapter_fusions(resume_from_checkpoint)
                 # Save all heads for a model with heads
                 if hasattr(self.model, "heads"):
                     self._load_heads(resume_from_checkpoint)
```

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/training.py` & `adapter-transformers-3.2.1/src/transformers/adapters/training.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/utils.py` & `adapter-transformers-3.2.1/src/transformers/adapters/utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -404,15 +404,16 @@
     # Now match each adapter config against the regex
     adapter_configs = []
     for config_string_chunk in config_string_chunks:
         match = re.match(ADAPTER_CONFIG_STRING_PATTERN, config_string_chunk.strip())
         if not match or not match.group("name"):
             raise ValueError(f"Invalid adapter config string format: '{config_string_chunk}'.")
         name = match.group("name")
-        if kvs := match.group("kvs"):
+        if match.group("kvs"):
+            kvs = match.group("kvs")
             # Replace "=" with ":" in key-value pairs for valid Python dict
             kvs = re.sub(r"(\w+)=", r"'\1':", kvs)
         else:
             kvs = ""
         # Now evaluate key-value pairs as Python dict
         try:
             config_kwargs = ast.literal_eval("{" + kvs + "}")
```

### Comparing `adapter-transformers-3.2.0/src/transformers/adapters/wrappers/configuration.py` & `adapter-transformers-3.2.1/src/transformers/adapters/wrappers/configuration.py`

 * *Files 3% similar despite different names*

```diff
@@ -52,14 +52,15 @@
         "num_hidden_layers": "num_layers",
         "hidden_dropout_prob": "dropout_rate",
         "attention_probs_dropout_prob": "dropout_rate",
     },
     "vit": {},
     "xlm_roberta": {},
 }
+SUBMODEL_NAMES = {"clip": ["vision_config", "text_config"], "encoder-decoder": ["encoder", "decoder"]}
 
 
 def wrap_config(config: PretrainedConfig) -> PretrainedConfig:
     """
     Makes required changes to a model config class to allow usage with adapters.
 
     Args:
```

### Comparing `adapter-transformers-3.2.0/src/transformers/benchmark/benchmark.py` & `adapter-transformers-3.2.1/src/transformers/benchmark/benchmark.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_args.py` & `adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_args.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_args_tf.py` & `adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_args_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_args_utils.py` & `adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_args_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_tf.py` & `adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/benchmark/benchmark_utils.py` & `adapter-transformers-3.2.1/src/transformers/benchmark/benchmark_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/__init__.py` & `adapter-transformers-3.2.1/src/transformers/commands/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/add_new_model.py` & `adapter-transformers-3.2.1/src/transformers/commands/add_new_model.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/add_new_model_like.py` & `adapter-transformers-3.2.1/src/transformers/commands/add_new_model_like.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/convert.py` & `adapter-transformers-3.2.1/src/transformers/commands/convert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/download.py` & `adapter-transformers-3.2.1/src/transformers/commands/download.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/env.py` & `adapter-transformers-3.2.1/src/transformers/commands/env.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/lfs.py` & `adapter-transformers-3.2.1/src/transformers/commands/lfs.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/pt_to_tf.py` & `adapter-transformers-3.2.1/src/transformers/commands/pt_to_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/run.py` & `adapter-transformers-3.2.1/src/transformers/commands/run.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/serving.py` & `adapter-transformers-3.2.1/src/transformers/commands/serving.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/train.py` & `adapter-transformers-3.2.1/src/transformers/commands/train.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/transformers_cli.py` & `adapter-transformers-3.2.1/src/transformers/commands/transformers_cli.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/commands/user.py` & `adapter-transformers-3.2.1/src/transformers/commands/user.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/configuration_utils.py` & `adapter-transformers-3.2.1/src/transformers/configuration_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/convert_graph_to_onnx.py` & `adapter-transformers-3.2.1/src/transformers/convert_graph_to_onnx.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/convert_pytorch_checkpoint_to_tf2.py` & `adapter-transformers-3.2.1/src/transformers/convert_pytorch_checkpoint_to_tf2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/convert_slow_tokenizer.py` & `adapter-transformers-3.2.1/src/transformers/convert_slow_tokenizer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/convert_slow_tokenizers_checkpoints_to_fast.py` & `adapter-transformers-3.2.1/src/transformers/convert_slow_tokenizers_checkpoints_to_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/convert_tf_hub_seq_to_seq_bert_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/convert_tf_hub_seq_to_seq_bert_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/__init__.py` & `adapter-transformers-3.2.1/src/transformers/data/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/data_collator.py` & `adapter-transformers-3.2.1/src/transformers/data/data_collator.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/datasets/__init__.py` & `adapter-transformers-3.2.1/src/transformers/data/datasets/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/datasets/glue.py` & `adapter-transformers-3.2.1/src/transformers/data/datasets/glue.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/datasets/language_modeling.py` & `adapter-transformers-3.2.1/src/transformers/data/datasets/language_modeling.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/datasets/squad.py` & `adapter-transformers-3.2.1/src/transformers/data/datasets/squad.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/metrics/__init__.py` & `adapter-transformers-3.2.1/src/transformers/data/metrics/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/metrics/squad_metrics.py` & `adapter-transformers-3.2.1/src/transformers/data/metrics/squad_metrics.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/processors/__init__.py` & `adapter-transformers-3.2.1/src/transformers/data/processors/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/processors/glue.py` & `adapter-transformers-3.2.1/src/transformers/data/processors/glue.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/processors/squad.py` & `adapter-transformers-3.2.1/src/transformers/data/processors/squad.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/processors/utils.py` & `adapter-transformers-3.2.1/src/transformers/data/processors/utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/processors/xnli.py` & `adapter-transformers-3.2.1/src/transformers/data/processors/xnli.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/data/test_generation_utils.py` & `adapter-transformers-3.2.1/src/transformers/data/test_generation_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/debug_utils.py` & `adapter-transformers-3.2.1/src/transformers/debug_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/deepspeed.py` & `adapter-transformers-3.2.1/src/transformers/deepspeed.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/dependency_versions_check.py` & `adapter-transformers-3.2.1/src/transformers/dependency_versions_check.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/dependency_versions_table.py` & `adapter-transformers-3.2.1/src/transformers/dependency_versions_table.py`

 * *Files 1% similar despite different names*

```diff
@@ -48,15 +48,15 @@
     "psutil": "psutil",
     "pyyaml": "pyyaml>=5.1",
     "pydantic": "pydantic",
     "pytest": "pytest",
     "pytest-subtests": "pytest-subtests",
     "pytest-timeout": "pytest-timeout",
     "pytest-xdist": "pytest-xdist",
-    "python": "python>=3.7.0",
+    "python": "python>=3.8.0",
     "ray[tune]": "ray[tune]",
     "myst-parser": "myst-parser",
     "regex": "regex!=2019.12.17",
     "requests": "requests",
     "rjieba": "rjieba",
     "rouge-score": "rouge-score!=0.0.7,!=0.0.8,!=0.1,!=0.1.1",
     "sacrebleu": "sacrebleu>=1.4.12,<2.0.0",
@@ -78,15 +78,15 @@
     "tensorflow-cpu": "tensorflow-cpu>=2.4,<2.12",
     "tensorflow": "tensorflow>=2.4,<2.12",
     "tensorflow-text": "tensorflow-text",
     "tf2onnx": "tf2onnx",
     "timeout-decorator": "timeout-decorator",
     "timm": "timm",
     "tokenizers": "tokenizers>=0.11.1,!=0.11.3,<0.14",
-    "torch": "torch>=1.7,!=1.12.0",
+    "torch": "torch>=1.12.1",
     "torchaudio": "torchaudio",
     "pyctcdecode": "pyctcdecode>=0.4.0",
     "tqdm": "tqdm>=4.27",
     "unidic": "unidic>=1.0.2",
     "unidic_lite": "unidic_lite>=1.0.7",
     "uvicorn": "uvicorn",
     "beautifulsoup4": "beautifulsoup4",
```

### Comparing `adapter-transformers-3.2.0/src/transformers/dynamic_module_utils.py` & `adapter-transformers-3.2.1/src/transformers/dynamic_module_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/feature_extraction_sequence_utils.py` & `adapter-transformers-3.2.1/src/transformers/feature_extraction_sequence_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/feature_extraction_utils.py` & `adapter-transformers-3.2.1/src/transformers/feature_extraction_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/file_utils.py` & `adapter-transformers-3.2.1/src/transformers/file_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/__init__.py` & `adapter-transformers-3.2.1/src/transformers/generation/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/beam_constraints.py` & `adapter-transformers-3.2.1/src/transformers/generation/beam_constraints.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/beam_search.py` & `adapter-transformers-3.2.1/src/transformers/generation/beam_search.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/configuration_utils.py` & `adapter-transformers-3.2.1/src/transformers/generation/configuration_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/flax_logits_process.py` & `adapter-transformers-3.2.1/src/transformers/generation/flax_logits_process.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/flax_utils.py` & `adapter-transformers-3.2.1/src/transformers/generation/flax_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/logits_process.py` & `adapter-transformers-3.2.1/src/transformers/generation/logits_process.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/stopping_criteria.py` & `adapter-transformers-3.2.1/src/transformers/generation/stopping_criteria.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/tf_logits_process.py` & `adapter-transformers-3.2.1/src/transformers/generation/tf_logits_process.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/tf_utils.py` & `adapter-transformers-3.2.1/src/transformers/generation/tf_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation/utils.py` & `adapter-transformers-3.2.1/src/transformers/generation/utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation_flax_utils.py` & `adapter-transformers-3.2.1/src/transformers/generation_flax_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation_tf_utils.py` & `adapter-transformers-3.2.1/src/transformers/generation_tf_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/generation_utils.py` & `adapter-transformers-3.2.1/src/transformers/generation_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/hf_argparser.py` & `adapter-transformers-3.2.1/src/transformers/hf_argparser.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/image_processing_utils.py` & `adapter-transformers-3.2.1/src/transformers/image_processing_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/image_transforms.py` & `adapter-transformers-3.2.1/src/transformers/image_transforms.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/image_utils.py` & `adapter-transformers-3.2.1/src/transformers/image_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/integrations.py` & `adapter-transformers-3.2.1/src/transformers/integrations.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/keras_callbacks.py` & `adapter-transformers-3.2.1/src/transformers/keras_callbacks.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modelcard.py` & `adapter-transformers-3.2.1/src/transformers/modelcard.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_flax_outputs.py` & `adapter-transformers-3.2.1/src/transformers/modeling_flax_outputs.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_flax_pytorch_utils.py` & `adapter-transformers-3.2.1/src/transformers/modeling_flax_pytorch_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_flax_utils.py` & `adapter-transformers-3.2.1/src/transformers/modeling_flax_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_outputs.py` & `adapter-transformers-3.2.1/src/transformers/modeling_outputs.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_tf_outputs.py` & `adapter-transformers-3.2.1/src/transformers/modeling_tf_outputs.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_tf_pytorch_utils.py` & `adapter-transformers-3.2.1/src/transformers/modeling_tf_pytorch_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_tf_utils.py` & `adapter-transformers-3.2.1/src/transformers/modeling_tf_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/modeling_utils.py` & `adapter-transformers-3.2.1/src/transformers/modeling_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/configuration_albert.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/configuration_albert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/convert_albert_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/convert_albert_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/modeling_albert.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/modeling_albert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/modeling_flax_albert.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/modeling_flax_albert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/modeling_tf_albert.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/modeling_tf_albert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/tokenization_albert.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/tokenization_albert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/albert/tokenization_albert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/albert/tokenization_albert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/altclip/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/altclip/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/altclip/configuration_altclip.py` & `adapter-transformers-3.2.1/src/transformers/models/altclip/configuration_altclip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/altclip/modeling_altclip.py` & `adapter-transformers-3.2.1/src/transformers/models/altclip/modeling_altclip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/altclip/processing_altclip.py` & `adapter-transformers-3.2.1/src/transformers/models/altclip/processing_altclip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/configuration_audio_spectrogram_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/configuration_audio_spectrogram_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/convert_audio_spectrogram_transformer_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/convert_audio_spectrogram_transformer_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/feature_extraction_audio_spectrogram_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/feature_extraction_audio_spectrogram_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/audio_spectrogram_transformer/modeling_audio_spectrogram_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/audio_spectrogram_transformer/modeling_audio_spectrogram_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/auto_factory.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/auto_factory.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/configuration_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/configuration_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/feature_extraction_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/feature_extraction_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/image_processing_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/image_processing_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/modeling_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/modeling_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/modeling_flax_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/modeling_flax_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/modeling_tf_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/modeling_tf_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/processing_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/processing_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/auto/tokenization_auto.py` & `adapter-transformers-3.2.1/src/transformers/models/auto/tokenization_auto.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/configuration_bart.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/configuration_bart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/convert_bart_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/modeling_bart.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/modeling_bart.py`

 * *Files 0% similar despite different names*

```diff
@@ -411,16 +411,16 @@
             self.embed_dim,
             config.decoder_attention_heads,
             dropout=config.attention_dropout,
             is_decoder=True,
             location_key="cross",
         )
         self.encoder_attn_layer_norm = nn.LayerNorm(self.embed_dim)
-        self.fc1 = nn.Linear(self.embed_dim, config.decoder_ffn_dim)
-        self.fc2 = nn.Linear(config.decoder_ffn_dim, self.embed_dim)
+        self.fc1 = LoRALinear(self.embed_dim, config.encoder_ffn_dim, "intermediate", config)
+        self.fc2 = LoRALinear(config.encoder_ffn_dim, self.embed_dim, "output", config)
         self.final_layer_norm = nn.LayerNorm(self.embed_dim)
 
         self._init_adapter_modules()
 
     def forward(
         self,
         hidden_states: torch.Tensor,
```

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/modeling_flax_bart.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/modeling_flax_bart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/modeling_tf_bart.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/modeling_tf_bart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/tokenization_bart.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/tokenization_bart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bart/tokenization_bart_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/bart/tokenization_bart_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/barthez/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/barthez/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/barthez/tokenization_barthez.py` & `adapter-transformers-3.2.1/src/transformers/models/barthez/tokenization_barthez.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/barthez/tokenization_barthez_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/barthez/tokenization_barthez_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bartpho/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bartpho/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bartpho/tokenization_bartpho.py` & `adapter-transformers-3.2.1/src/transformers/models/bartpho/tokenization_bartpho.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/configuration_beit.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/configuration_beit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/convert_beit_unilm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/convert_beit_unilm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/feature_extraction_beit.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/feature_extraction_beit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/image_processing_beit.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/image_processing_beit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/modeling_beit.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/modeling_beit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/beit/modeling_flax_beit.py` & `adapter-transformers-3.2.1/src/transformers/models/beit/modeling_flax_beit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/configuration_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/configuration_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_original_tf2_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_original_tf2_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_pytorch_checkpoint_to_original_tf.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_pytorch_checkpoint_to_original_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/convert_bert_token_dropping_original_tf2_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/convert_bert_token_dropping_original_tf2_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/modeling_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/modeling_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/modeling_flax_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/modeling_flax_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/modeling_tf_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/modeling_tf_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/tokenization_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/tokenization_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/tokenization_bert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/tokenization_bert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert/tokenization_bert_tf.py` & `adapter-transformers-3.2.1/src/transformers/models/bert/tokenization_bert_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert_generation/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bert_generation/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert_generation/configuration_bert_generation.py` & `adapter-transformers-3.2.1/src/transformers/models/bert_generation/configuration_bert_generation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert_generation/modeling_bert_generation.py` & `adapter-transformers-3.2.1/src/transformers/models/bert_generation/modeling_bert_generation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert_generation/tokenization_bert_generation.py` & `adapter-transformers-3.2.1/src/transformers/models/bert_generation/tokenization_bert_generation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert_japanese/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bert_japanese/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bert_japanese/tokenization_bert_japanese.py` & `adapter-transformers-3.2.1/src/transformers/models/bert_japanese/tokenization_bert_japanese.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bertweet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bertweet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bertweet/tokenization_bertweet.py` & `adapter-transformers-3.2.1/src/transformers/models/bertweet/tokenization_bertweet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/configuration_big_bird.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/configuration_big_bird.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/convert_bigbird_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/convert_bigbird_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/modeling_big_bird.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/modeling_big_bird.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/modeling_flax_big_bird.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/modeling_flax_big_bird.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/tokenization_big_bird.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/tokenization_big_bird.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/big_bird/tokenization_big_bird_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/big_bird/tokenization_big_bird_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/configuration_bigbird_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/configuration_bigbird_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/convert_bigbird_pegasus_tf_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/convert_bigbird_pegasus_tf_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bigbird_pegasus/modeling_bigbird_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/bigbird_pegasus/modeling_bigbird_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/biogpt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/biogpt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/biogpt/configuration_biogpt.py` & `adapter-transformers-3.2.1/src/transformers/models/biogpt/configuration_biogpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/biogpt/convert_biogpt_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/biogpt/convert_biogpt_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/biogpt/modeling_biogpt.py` & `adapter-transformers-3.2.1/src/transformers/models/biogpt/modeling_biogpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/biogpt/tokenization_biogpt.py` & `adapter-transformers-3.2.1/src/transformers/models/biogpt/tokenization_biogpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bit/configuration_bit.py` & `adapter-transformers-3.2.1/src/transformers/models/bit/configuration_bit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bit/convert_bit_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bit/convert_bit_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bit/image_processing_bit.py` & `adapter-transformers-3.2.1/src/transformers/models/bit/image_processing_bit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bit/modeling_bit.py` & `adapter-transformers-3.2.1/src/transformers/models/bit/modeling_bit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/configuration_blenderbot.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/configuration_blenderbot.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/convert_blenderbot_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/convert_blenderbot_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/modeling_blenderbot.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/modeling_blenderbot.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/modeling_flax_blenderbot.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/modeling_flax_blenderbot.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/modeling_tf_blenderbot.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/modeling_tf_blenderbot.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/tokenization_blenderbot.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/tokenization_blenderbot.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot/tokenization_blenderbot_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot/tokenization_blenderbot_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/configuration_blenderbot_small.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/configuration_blenderbot_small.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/modeling_blenderbot_small.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/modeling_blenderbot_small.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/modeling_flax_blenderbot_small.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/modeling_flax_blenderbot_small.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/modeling_tf_blenderbot_small.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/modeling_tf_blenderbot_small.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/tokenization_blenderbot_small.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/tokenization_blenderbot_small.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blenderbot_small/tokenization_blenderbot_small_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/blenderbot_small/tokenization_blenderbot_small_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/configuration_blip.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/configuration_blip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/convert_blip_original_pytorch_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/convert_blip_original_pytorch_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/image_processing_blip.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/image_processing_blip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/modeling_blip.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/modeling_blip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/modeling_blip_text.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/modeling_blip_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/blip/processing_blip.py` & `adapter-transformers-3.2.1/src/transformers/models/blip/processing_blip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bloom/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/bloom/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bloom/configuration_bloom.py` & `adapter-transformers-3.2.1/src/transformers/models/bloom/configuration_bloom.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bloom/convert_bloom_original_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bloom/convert_bloom_original_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bloom/modeling_bloom.py` & `adapter-transformers-3.2.1/src/transformers/models/bloom/modeling_bloom.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bloom/tokenization_bloom_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/bloom/tokenization_bloom_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/bort/convert_bort_original_gluonnlp_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/bort/convert_bort_original_gluonnlp_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/byt5/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/byt5/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/byt5/convert_byt5_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/byt5/convert_byt5_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/byt5/tokenization_byt5.py` & `adapter-transformers-3.2.1/src/transformers/models/byt5/tokenization_byt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/camembert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/camembert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/camembert/configuration_camembert.py` & `adapter-transformers-3.2.1/src/transformers/models/camembert/configuration_camembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/camembert/modeling_camembert.py` & `adapter-transformers-3.2.1/src/transformers/models/camembert/modeling_camembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/camembert/modeling_tf_camembert.py` & `adapter-transformers-3.2.1/src/transformers/models/camembert/modeling_tf_camembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/camembert/tokenization_camembert.py` & `adapter-transformers-3.2.1/src/transformers/models/camembert/tokenization_camembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/camembert/tokenization_camembert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/camembert/tokenization_camembert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/canine/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/canine/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/canine/configuration_canine.py` & `adapter-transformers-3.2.1/src/transformers/models/canine/configuration_canine.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/canine/convert_canine_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/canine/convert_canine_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/canine/modeling_canine.py` & `adapter-transformers-3.2.1/src/transformers/models/canine/modeling_canine.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/canine/tokenization_canine.py` & `adapter-transformers-3.2.1/src/transformers/models/canine/tokenization_canine.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/configuration_chinese_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/configuration_chinese_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/convert_chinese_clip_original_pytorch_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/convert_chinese_clip_original_pytorch_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/feature_extraction_chinese_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/feature_extraction_chinese_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/image_processing_chinese_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/image_processing_chinese_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/modeling_chinese_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/modeling_chinese_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/chinese_clip/processing_chinese_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/chinese_clip/processing_chinese_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/configuration_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/configuration_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/convert_clip_original_pytorch_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/convert_clip_original_pytorch_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/feature_extraction_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/feature_extraction_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/image_processing_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/image_processing_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/modeling_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/modeling_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/modeling_flax_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/modeling_flax_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/modeling_tf_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/modeling_tf_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/processing_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/processing_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/tokenization_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/tokenization_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clip/tokenization_clip_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/clip/tokenization_clip_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clipseg/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/clipseg/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clipseg/configuration_clipseg.py` & `adapter-transformers-3.2.1/src/transformers/models/clipseg/configuration_clipseg.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clipseg/convert_clipseg_original_pytorch_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/clipseg/convert_clipseg_original_pytorch_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clipseg/modeling_clipseg.py` & `adapter-transformers-3.2.1/src/transformers/models/clipseg/modeling_clipseg.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/clipseg/processing_clipseg.py` & `adapter-transformers-3.2.1/src/transformers/models/clipseg/processing_clipseg.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/codegen/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/codegen/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/codegen/configuration_codegen.py` & `adapter-transformers-3.2.1/src/transformers/models/codegen/configuration_codegen.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/codegen/modeling_codegen.py` & `adapter-transformers-3.2.1/src/transformers/models/codegen/modeling_codegen.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/codegen/tokenization_codegen.py` & `adapter-transformers-3.2.1/src/transformers/models/codegen/tokenization_codegen.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/codegen/tokenization_codegen_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/codegen/tokenization_codegen_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/conditional_detr/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/conditional_detr/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/conditional_detr/configuration_conditional_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/conditional_detr/configuration_conditional_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/conditional_detr/convert_conditional_detr_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/conditional_detr/convert_conditional_detr_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/conditional_detr/feature_extraction_conditional_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/conditional_detr/feature_extraction_conditional_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/conditional_detr/image_processing_conditional_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/conditional_detr/image_processing_conditional_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/conditional_detr/modeling_conditional_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/conditional_detr/modeling_conditional_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/configuration_convbert.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/configuration_convbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/convert_convbert_original_tf1_checkpoint_to_pytorch_and_tf2.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/convert_convbert_original_tf1_checkpoint_to_pytorch_and_tf2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/modeling_convbert.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/modeling_convbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/modeling_tf_convbert.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/modeling_tf_convbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/tokenization_convbert.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/tokenization_convbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convbert/tokenization_convbert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/convbert/tokenization_convbert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/configuration_convnext.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/configuration_convnext.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/convert_convnext_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/convert_convnext_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/feature_extraction_convnext.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/feature_extraction_convnext.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/image_processing_convnext.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/image_processing_convnext.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/modeling_convnext.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/modeling_convnext.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/convnext/modeling_tf_convnext.py` & `adapter-transformers-3.2.1/src/transformers/models/convnext/modeling_tf_convnext.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cpm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/cpm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cpm/tokenization_cpm.py` & `adapter-transformers-3.2.1/src/transformers/models/cpm/tokenization_cpm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cpm/tokenization_cpm_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/cpm/tokenization_cpm_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ctrl/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/ctrl/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ctrl/configuration_ctrl.py` & `adapter-transformers-3.2.1/src/transformers/models/ctrl/configuration_ctrl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ctrl/modeling_ctrl.py` & `adapter-transformers-3.2.1/src/transformers/models/ctrl/modeling_ctrl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ctrl/modeling_tf_ctrl.py` & `adapter-transformers-3.2.1/src/transformers/models/ctrl/modeling_tf_ctrl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ctrl/tokenization_ctrl.py` & `adapter-transformers-3.2.1/src/transformers/models/ctrl/tokenization_ctrl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cvt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/cvt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cvt/configuration_cvt.py` & `adapter-transformers-3.2.1/src/transformers/models/cvt/configuration_cvt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cvt/convert_cvt_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/cvt/convert_cvt_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cvt/modeling_cvt.py` & `adapter-transformers-3.2.1/src/transformers/models/cvt/modeling_cvt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/cvt/modeling_tf_cvt.py` & `adapter-transformers-3.2.1/src/transformers/models/cvt/modeling_tf_cvt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/configuration_data2vec_audio.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/configuration_data2vec_audio.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/configuration_data2vec_text.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/configuration_data2vec_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/configuration_data2vec_vision.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/configuration_data2vec_vision.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/convert_data2vec_audio_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/convert_data2vec_audio_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/convert_data2vec_text_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/convert_data2vec_text_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/convert_data2vec_vision_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/convert_data2vec_vision_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_data2vec_audio.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_data2vec_audio.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_data2vec_text.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_data2vec_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_data2vec_vision.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_data2vec_vision.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/data2vec/modeling_tf_data2vec_vision.py` & `adapter-transformers-3.2.1/src/transformers/models/data2vec/modeling_tf_data2vec_vision.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta/configuration_deberta.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta/configuration_deberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta/modeling_deberta.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta/modeling_deberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta/modeling_tf_deberta.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta/modeling_tf_deberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta/tokenization_deberta.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta/tokenization_deberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta/tokenization_deberta_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta/tokenization_deberta_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta_v2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta_v2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta_v2/configuration_deberta_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta_v2/configuration_deberta_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta_v2/modeling_deberta_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta_v2/modeling_deberta_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta_v2/modeling_tf_deberta_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta_v2/modeling_tf_deberta_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta_v2/tokenization_deberta_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta_v2/tokenization_deberta_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deberta_v2/tokenization_deberta_v2_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/deberta_v2/tokenization_deberta_v2_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/decision_transformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/decision_transformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/decision_transformer/configuration_decision_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/decision_transformer/configuration_decision_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/decision_transformer/modeling_decision_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/decision_transformer/modeling_decision_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/configuration_deformable_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/configuration_deformable_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/convert_deformable_detr_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/convert_deformable_detr_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/feature_extraction_deformable_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/feature_extraction_deformable_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/image_processing_deformable_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/image_processing_deformable_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/load_custom.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/load_custom.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deformable_detr/modeling_deformable_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/deformable_detr/modeling_deformable_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/configuration_deit.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/configuration_deit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/convert_deit_timm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/convert_deit_timm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/feature_extraction_deit.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/feature_extraction_deit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/image_processing_deit.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/image_processing_deit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/modeling_deit.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/modeling_deit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/deit/modeling_tf_deit.py` & `adapter-transformers-3.2.1/src/transformers/models/deit/modeling_tf_deit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/configuration_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/configuration_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/convert_detr_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/convert_detr_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/convert_detr_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/convert_detr_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/feature_extraction_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/feature_extraction_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/image_processing_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/image_processing_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/detr/modeling_detr.py` & `adapter-transformers-3.2.1/src/transformers/models/detr/modeling_detr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dialogpt/convert_dialogpt_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/dialogpt/convert_dialogpt_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dinat/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/dinat/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dinat/configuration_dinat.py` & `adapter-transformers-3.2.1/src/transformers/models/dinat/configuration_dinat.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dinat/modeling_dinat.py` & `adapter-transformers-3.2.1/src/transformers/models/dinat/modeling_dinat.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/configuration_distilbert.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/configuration_distilbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/modeling_distilbert.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/modeling_distilbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/modeling_flax_distilbert.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/modeling_flax_distilbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/modeling_tf_distilbert.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/modeling_tf_distilbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/tokenization_distilbert.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/tokenization_distilbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/distilbert/tokenization_distilbert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/distilbert/tokenization_distilbert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dit/convert_dit_unilm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/dit/convert_dit_unilm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/configuration_donut_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/configuration_donut_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/convert_donut_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/convert_donut_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/feature_extraction_donut.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/feature_extraction_donut.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/image_processing_donut.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/image_processing_donut.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/modeling_donut_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/modeling_donut_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/donut/processing_donut.py` & `adapter-transformers-3.2.1/src/transformers/models/donut/processing_donut.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/configuration_dpr.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/configuration_dpr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/convert_dpr_original_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/convert_dpr_original_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/modeling_dpr.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/modeling_dpr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/modeling_tf_dpr.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/modeling_tf_dpr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/tokenization_dpr.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/tokenization_dpr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpr/tokenization_dpr_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/dpr/tokenization_dpr_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/configuration_dpt.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/configuration_dpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/convert_dpt_hybrid_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/convert_dpt_hybrid_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/convert_dpt_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/convert_dpt_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/feature_extraction_dpt.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/feature_extraction_dpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/image_processing_dpt.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/image_processing_dpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/dpt/modeling_dpt.py` & `adapter-transformers-3.2.1/src/transformers/models/dpt/modeling_dpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/efficientformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/efficientformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/efficientformer/configuration_efficientformer.py` & `adapter-transformers-3.2.1/src/transformers/models/efficientformer/configuration_efficientformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/efficientformer/convert_efficientformer_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/efficientformer/convert_efficientformer_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/efficientformer/image_processing_efficientformer.py` & `adapter-transformers-3.2.1/src/transformers/models/efficientformer/image_processing_efficientformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/efficientformer/modeling_efficientformer.py` & `adapter-transformers-3.2.1/src/transformers/models/efficientformer/modeling_efficientformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/configuration_electra.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/configuration_electra.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/convert_electra_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/convert_electra_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/modeling_electra.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/modeling_electra.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/modeling_flax_electra.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/modeling_flax_electra.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/modeling_tf_electra.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/modeling_tf_electra.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/tokenization_electra.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/tokenization_electra.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/electra/tokenization_electra_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/electra/tokenization_electra_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/configuration_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/configuration_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/modeling_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/modeling_flax_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/modeling_flax_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/encoder_decoder/modeling_tf_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/encoder_decoder/modeling_tf_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ernie/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/ernie/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ernie/configuration_ernie.py` & `adapter-transformers-3.2.1/src/transformers/models/ernie/configuration_ernie.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ernie/modeling_ernie.py` & `adapter-transformers-3.2.1/src/transformers/models/ernie/modeling_ernie.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/configuration_esm.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/configuration_esm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/convert_esm.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/convert_esm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/modeling_esm.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/modeling_esm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/modeling_esmfold.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/modeling_esmfold.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/modeling_tf_esm.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/modeling_tf_esm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/chunk_utils.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/chunk_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/data_transforms.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/data_transforms.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/feats.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/feats.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/loss.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/loss.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/protein.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/protein.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/residue_constants.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/residue_constants.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/rigid_utils.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/rigid_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/openfold_utils/tensor_utils.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/openfold_utils/tensor_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/esm/tokenization_esm.py` & `adapter-transformers-3.2.1/src/transformers/models/esm/tokenization_esm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flaubert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/flaubert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flaubert/configuration_flaubert.py` & `adapter-transformers-3.2.1/src/transformers/models/flaubert/configuration_flaubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flaubert/modeling_flaubert.py` & `adapter-transformers-3.2.1/src/transformers/models/flaubert/modeling_flaubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flaubert/modeling_tf_flaubert.py` & `adapter-transformers-3.2.1/src/transformers/models/flaubert/modeling_tf_flaubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flaubert/tokenization_flaubert.py` & `adapter-transformers-3.2.1/src/transformers/models/flaubert/tokenization_flaubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/configuration_flava.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/configuration_flava.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/convert_dalle_to_flava_codebook.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/convert_dalle_to_flava_codebook.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/convert_flava_original_pytorch_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/convert_flava_original_pytorch_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/feature_extraction_flava.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/feature_extraction_flava.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/image_processing_flava.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/image_processing_flava.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/modeling_flava.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/modeling_flava.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/flava/processing_flava.py` & `adapter-transformers-3.2.1/src/transformers/models/flava/processing_flava.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/fnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fnet/configuration_fnet.py` & `adapter-transformers-3.2.1/src/transformers/models/fnet/configuration_fnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fnet/convert_fnet_original_flax_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/fnet/convert_fnet_original_flax_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fnet/modeling_fnet.py` & `adapter-transformers-3.2.1/src/transformers/models/fnet/modeling_fnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fnet/tokenization_fnet.py` & `adapter-transformers-3.2.1/src/transformers/models/fnet/tokenization_fnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fnet/tokenization_fnet_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/fnet/tokenization_fnet_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fsmt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/fsmt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fsmt/configuration_fsmt.py` & `adapter-transformers-3.2.1/src/transformers/models/fsmt/configuration_fsmt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fsmt/convert_fsmt_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/fsmt/convert_fsmt_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fsmt/modeling_fsmt.py` & `adapter-transformers-3.2.1/src/transformers/models/fsmt/modeling_fsmt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/fsmt/tokenization_fsmt.py` & `adapter-transformers-3.2.1/src/transformers/models/fsmt/tokenization_fsmt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/configuration_funnel.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/configuration_funnel.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/convert_funnel_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/convert_funnel_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/modeling_funnel.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/modeling_funnel.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/modeling_tf_funnel.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/modeling_tf_funnel.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/tokenization_funnel.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/tokenization_funnel.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/funnel/tokenization_funnel_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/funnel/tokenization_funnel_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/git/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/git/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/git/configuration_git.py` & `adapter-transformers-3.2.1/src/transformers/models/git/configuration_git.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/git/convert_git_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/git/convert_git_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/git/modeling_git.py` & `adapter-transformers-3.2.1/src/transformers/models/git/modeling_git.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/git/processing_git.py` & `adapter-transformers-3.2.1/src/transformers/models/git/processing_git.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/glpn/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/glpn/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/glpn/configuration_glpn.py` & `adapter-transformers-3.2.1/src/transformers/models/glpn/configuration_glpn.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/glpn/convert_glpn_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/glpn/convert_glpn_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/glpn/feature_extraction_glpn.py` & `adapter-transformers-3.2.1/src/transformers/models/glpn/feature_extraction_glpn.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/glpn/image_processing_glpn.py` & `adapter-transformers-3.2.1/src/transformers/models/glpn/image_processing_glpn.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/glpn/modeling_glpn.py` & `adapter-transformers-3.2.1/src/transformers/models/glpn/modeling_glpn.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/configuration_gpt2.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/configuration_gpt2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/convert_gpt2_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/convert_gpt2_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/modeling_flax_gpt2.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/modeling_flax_gpt2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/modeling_gpt2.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/modeling_gpt2.py`

 * *Files 0% similar despite different names*

```diff
@@ -166,14 +166,15 @@
         else:
             self.c_attn = LoRAMergedLinear(
                 self.embed_dim,
                 3 * self.embed_dim,
                 "selfattn",
                 config,
                 fan_in_fan_out=True,
+                no_init_bias=True,
             )
         self.c_proj = Conv1D(self.embed_dim, self.embed_dim)
 
         self.attn_dropout = nn.Dropout(config.attn_pdrop)
         self.resid_dropout = nn.Dropout(config.resid_pdrop)
 
         self.pruned_heads = set()
@@ -362,16 +363,20 @@
 
 
 class GPT2MLP(nn.Module):
     def __init__(self, intermediate_size, config):
         super().__init__()
         embed_dim = config.hidden_size
         # Order of dimension inputs to LORALinear reversed compared to Conv1D
-        self.c_fc = LoRALinear(embed_dim, intermediate_size, "intermediate", config, fan_in_fan_out=True)
-        self.c_proj = LoRALinear(intermediate_size, embed_dim, "output", config, fan_in_fan_out=True)
+        self.c_fc = LoRALinear(
+            embed_dim, intermediate_size, "intermediate", config, fan_in_fan_out=True, no_init_bias=True
+        )
+        self.c_proj = LoRALinear(
+            intermediate_size, embed_dim, "output", config, fan_in_fan_out=True, no_init_bias=True
+        )
         self.act = ACT2FN[config.activation_function]
         self.dropout = nn.Dropout(config.resid_pdrop)
 
     def forward(self, hidden_states: Optional[Tuple[torch.FloatTensor]]) -> torch.FloatTensor:
         hidden_states = self.c_fc(hidden_states)
         hidden_states = self.act(hidden_states)
         hidden_states = self.c_proj(hidden_states)
```

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/modeling_tf_gpt2.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/modeling_tf_gpt2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/tokenization_gpt2.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/tokenization_gpt2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/tokenization_gpt2_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/tokenization_gpt2_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt2/tokenization_gpt2_tf.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt2/tokenization_gpt2_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neo/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neo/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neo/configuration_gpt_neo.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neo/configuration_gpt_neo.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neo/convert_gpt_neo_mesh_tf_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neo/convert_gpt_neo_mesh_tf_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neo/modeling_flax_gpt_neo.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neo/modeling_flax_gpt_neo.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neo/modeling_gpt_neo.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neo/modeling_gpt_neo.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox/configuration_gpt_neox.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox/configuration_gpt_neox.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox/modeling_gpt_neox.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox/modeling_gpt_neox.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox/tokenization_gpt_neox_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox/tokenization_gpt_neox_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/configuration_gpt_neox_japanese.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/configuration_gpt_neox_japanese.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/modeling_gpt_neox_japanese.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/modeling_gpt_neox_japanese.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_neox_japanese/tokenization_gpt_neox_japanese.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_neox_japanese/tokenization_gpt_neox_japanese.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/convert_megatron_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/convert_megatron_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gpt_sw3/tokenization_gpt_sw3.py` & `adapter-transformers-3.2.1/src/transformers/models/gpt_sw3/tokenization_gpt_sw3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gptj/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/gptj/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gptj/configuration_gptj.py` & `adapter-transformers-3.2.1/src/transformers/models/gptj/configuration_gptj.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gptj/modeling_flax_gptj.py` & `adapter-transformers-3.2.1/src/transformers/models/gptj/modeling_flax_gptj.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gptj/modeling_gptj.py` & `adapter-transformers-3.2.1/src/transformers/models/gptj/modeling_gptj.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/gptj/modeling_tf_gptj.py` & `adapter-transformers-3.2.1/src/transformers/models/gptj/modeling_tf_gptj.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/graphormer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/graphormer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/graphormer/collating_graphormer.py` & `adapter-transformers-3.2.1/src/transformers/models/graphormer/collating_graphormer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/graphormer/configuration_graphormer.py` & `adapter-transformers-3.2.1/src/transformers/models/graphormer/configuration_graphormer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/graphormer/modeling_graphormer.py` & `adapter-transformers-3.2.1/src/transformers/models/graphormer/modeling_graphormer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/groupvit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/groupvit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/groupvit/configuration_groupvit.py` & `adapter-transformers-3.2.1/src/transformers/models/groupvit/configuration_groupvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/groupvit/convert_groupvit_nvlab_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/groupvit/convert_groupvit_nvlab_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/groupvit/modeling_groupvit.py` & `adapter-transformers-3.2.1/src/transformers/models/groupvit/modeling_groupvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/groupvit/modeling_tf_groupvit.py` & `adapter-transformers-3.2.1/src/transformers/models/groupvit/modeling_tf_groupvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/herbert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/herbert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/herbert/tokenization_herbert.py` & `adapter-transformers-3.2.1/src/transformers/models/herbert/tokenization_herbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/herbert/tokenization_herbert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/herbert/tokenization_herbert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/configuration_hubert.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/configuration_hubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/convert_distilhubert_original_s3prl_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/convert_distilhubert_original_s3prl_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/convert_hubert_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/convert_hubert_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/convert_hubert_original_s3prl_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/convert_hubert_original_s3prl_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/modeling_hubert.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/modeling_hubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/hubert/modeling_tf_hubert.py` & `adapter-transformers-3.2.1/src/transformers/models/hubert/modeling_tf_hubert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ibert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/ibert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ibert/configuration_ibert.py` & `adapter-transformers-3.2.1/src/transformers/models/ibert/configuration_ibert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ibert/modeling_ibert.py` & `adapter-transformers-3.2.1/src/transformers/models/ibert/modeling_ibert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/ibert/quant_modules.py` & `adapter-transformers-3.2.1/src/transformers/models/ibert/quant_modules.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/imagegpt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/imagegpt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/imagegpt/configuration_imagegpt.py` & `adapter-transformers-3.2.1/src/transformers/models/imagegpt/configuration_imagegpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/imagegpt/convert_imagegpt_original_tf2_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/imagegpt/convert_imagegpt_original_tf2_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/imagegpt/feature_extraction_imagegpt.py` & `adapter-transformers-3.2.1/src/transformers/models/imagegpt/feature_extraction_imagegpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/imagegpt/image_processing_imagegpt.py` & `adapter-transformers-3.2.1/src/transformers/models/imagegpt/image_processing_imagegpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/imagegpt/modeling_imagegpt.py` & `adapter-transformers-3.2.1/src/transformers/models/imagegpt/modeling_imagegpt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/jukebox/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/jukebox/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/jukebox/configuration_jukebox.py` & `adapter-transformers-3.2.1/src/transformers/models/jukebox/configuration_jukebox.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/jukebox/convert_jukebox.py` & `adapter-transformers-3.2.1/src/transformers/models/jukebox/convert_jukebox.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/jukebox/modeling_jukebox.py` & `adapter-transformers-3.2.1/src/transformers/models/jukebox/modeling_jukebox.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/jukebox/tokenization_jukebox.py` & `adapter-transformers-3.2.1/src/transformers/models/jukebox/tokenization_jukebox.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlm/configuration_layoutlm.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlm/configuration_layoutlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlm/modeling_layoutlm.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlm/modeling_layoutlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlm/modeling_tf_layoutlm.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlm/modeling_tf_layoutlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlm/tokenization_layoutlm.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlm/tokenization_layoutlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlm/tokenization_layoutlm_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlm/tokenization_layoutlm_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/configuration_layoutlmv2.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/configuration_layoutlmv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/feature_extraction_layoutlmv2.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/feature_extraction_layoutlmv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/image_processing_layoutlmv2.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/image_processing_layoutlmv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/modeling_layoutlmv2.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/modeling_layoutlmv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/processing_layoutlmv2.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/processing_layoutlmv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/tokenization_layoutlmv2.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/tokenization_layoutlmv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv2/tokenization_layoutlmv2_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv2/tokenization_layoutlmv2_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/configuration_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/configuration_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/feature_extraction_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/feature_extraction_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/image_processing_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/image_processing_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/modeling_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/modeling_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/modeling_tf_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/modeling_tf_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/processing_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/processing_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/tokenization_layoutlmv3.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/tokenization_layoutlmv3.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutlmv3/tokenization_layoutlmv3_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutlmv3/tokenization_layoutlmv3_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutxlm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutxlm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutxlm/processing_layoutxlm.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutxlm/processing_layoutxlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutxlm/tokenization_layoutxlm.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutxlm/tokenization_layoutxlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/layoutxlm/tokenization_layoutxlm_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/layoutxlm/tokenization_layoutxlm_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/led/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/led/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/led/configuration_led.py` & `adapter-transformers-3.2.1/src/transformers/models/led/configuration_led.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/led/modeling_led.py` & `adapter-transformers-3.2.1/src/transformers/models/led/modeling_led.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/led/modeling_tf_led.py` & `adapter-transformers-3.2.1/src/transformers/models/led/modeling_tf_led.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/led/tokenization_led.py` & `adapter-transformers-3.2.1/src/transformers/models/led/tokenization_led.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/led/tokenization_led_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/led/tokenization_led_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/levit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/levit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/levit/configuration_levit.py` & `adapter-transformers-3.2.1/src/transformers/models/levit/configuration_levit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/levit/convert_levit_timm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/levit/convert_levit_timm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/levit/feature_extraction_levit.py` & `adapter-transformers-3.2.1/src/transformers/models/levit/feature_extraction_levit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/levit/image_processing_levit.py` & `adapter-transformers-3.2.1/src/transformers/models/levit/image_processing_levit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/levit/modeling_levit.py` & `adapter-transformers-3.2.1/src/transformers/models/levit/modeling_levit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lilt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/lilt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lilt/configuration_lilt.py` & `adapter-transformers-3.2.1/src/transformers/models/lilt/configuration_lilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lilt/modeling_lilt.py` & `adapter-transformers-3.2.1/src/transformers/models/lilt/modeling_lilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/configuration_longformer.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/configuration_longformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/convert_longformer_original_pytorch_lightning_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/convert_longformer_original_pytorch_lightning_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/modeling_longformer.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/modeling_longformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/modeling_tf_longformer.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/modeling_tf_longformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/tokenization_longformer.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/tokenization_longformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longformer/tokenization_longformer_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/longformer/tokenization_longformer_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longt5/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/longt5/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longt5/configuration_longt5.py` & `adapter-transformers-3.2.1/src/transformers/models/longt5/configuration_longt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longt5/convert_longt5x_checkpoint_to_flax.py` & `adapter-transformers-3.2.1/src/transformers/models/longt5/convert_longt5x_checkpoint_to_flax.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longt5/modeling_flax_longt5.py` & `adapter-transformers-3.2.1/src/transformers/models/longt5/modeling_flax_longt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/longt5/modeling_longt5.py` & `adapter-transformers-3.2.1/src/transformers/models/longt5/modeling_longt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/luke/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/luke/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/luke/configuration_luke.py` & `adapter-transformers-3.2.1/src/transformers/models/luke/configuration_luke.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/luke/convert_luke_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/luke/convert_luke_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/luke/modeling_luke.py` & `adapter-transformers-3.2.1/src/transformers/models/luke/modeling_luke.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/luke/tokenization_luke.py` & `adapter-transformers-3.2.1/src/transformers/models/luke/tokenization_luke.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/configuration_lxmert.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/configuration_lxmert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/convert_lxmert_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/convert_lxmert_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/modeling_lxmert.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/modeling_lxmert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/modeling_tf_lxmert.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/modeling_tf_lxmert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/tokenization_lxmert.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/tokenization_lxmert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/lxmert/tokenization_lxmert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/lxmert/tokenization_lxmert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/m2m_100/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/m2m_100/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/m2m_100/configuration_m2m_100.py` & `adapter-transformers-3.2.1/src/transformers/models/m2m_100/configuration_m2m_100.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/m2m_100/convert_m2m100_original_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/m2m_100/convert_m2m100_original_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/m2m_100/modeling_m2m_100.py` & `adapter-transformers-3.2.1/src/transformers/models/m2m_100/modeling_m2m_100.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/m2m_100/tokenization_m2m_100.py` & `adapter-transformers-3.2.1/src/transformers/models/m2m_100/tokenization_m2m_100.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/configuration_marian.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/configuration_marian.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/convert_marian_tatoeba_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/convert_marian_tatoeba_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/convert_marian_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/convert_marian_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/modeling_flax_marian.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/modeling_flax_marian.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/modeling_marian.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/modeling_marian.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/modeling_tf_marian.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/modeling_tf_marian.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/marian/tokenization_marian.py` & `adapter-transformers-3.2.1/src/transformers/models/marian/tokenization_marian.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/configuration_markuplm.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/configuration_markuplm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/feature_extraction_markuplm.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/feature_extraction_markuplm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/modeling_markuplm.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/modeling_markuplm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/processing_markuplm.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/processing_markuplm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/tokenization_markuplm.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/tokenization_markuplm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/markuplm/tokenization_markuplm_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/markuplm/tokenization_markuplm_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mask2former/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mask2former/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mask2former/configuration_mask2former.py` & `adapter-transformers-3.2.1/src/transformers/models/mask2former/configuration_mask2former.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mask2former/convert_mask2former_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mask2former/convert_mask2former_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mask2former/image_processing_mask2former.py` & `adapter-transformers-3.2.1/src/transformers/models/mask2former/image_processing_mask2former.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mask2former/modeling_mask2former.py` & `adapter-transformers-3.2.1/src/transformers/models/mask2former/modeling_mask2former.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/configuration_maskformer.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/configuration_maskformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/configuration_maskformer_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/configuration_maskformer_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/convert_maskformer_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/convert_maskformer_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/convert_maskformer_resnet_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/convert_maskformer_resnet_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/convert_maskformer_swin_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/convert_maskformer_swin_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/feature_extraction_maskformer.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/feature_extraction_maskformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/image_processing_maskformer.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/image_processing_maskformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/modeling_maskformer.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/modeling_maskformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/maskformer/modeling_maskformer_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/maskformer/modeling_maskformer_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/configuration_mbart.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/configuration_mbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/convert_mbart_original_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/convert_mbart_original_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/modeling_flax_mbart.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/modeling_flax_mbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/modeling_mbart.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/modeling_mbart.py`

 * *Files 0% similar despite different names*

```diff
@@ -408,16 +408,16 @@
             self.embed_dim,
             config.decoder_attention_heads,
             dropout=config.attention_dropout,
             is_decoder=True,
             location_key="cross",
         )
         self.encoder_attn_layer_norm = nn.LayerNorm(self.embed_dim)
-        self.fc1 = nn.Linear(self.embed_dim, config.decoder_ffn_dim)
-        self.fc2 = nn.Linear(config.decoder_ffn_dim, self.embed_dim)
+        self.fc1 = LoRALinear(self.embed_dim, config.encoder_ffn_dim, "intermediate", config)
+        self.fc2 = LoRALinear(config.encoder_ffn_dim, self.embed_dim, "output", config)
         self.final_layer_norm = nn.LayerNorm(self.embed_dim)
 
         self._init_adapter_modules()
 
     def forward(
         self,
         hidden_states: torch.Tensor,
```

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/modeling_tf_mbart.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/modeling_tf_mbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/tokenization_mbart.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/tokenization_mbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart/tokenization_mbart_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart/tokenization_mbart_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart50/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart50/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart50/tokenization_mbart50.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart50/tokenization_mbart50.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mbart50/tokenization_mbart50_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/mbart50/tokenization_mbart50_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mctct/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mctct/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mctct/configuration_mctct.py` & `adapter-transformers-3.2.1/src/transformers/models/mctct/configuration_mctct.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mctct/feature_extraction_mctct.py` & `adapter-transformers-3.2.1/src/transformers/models/mctct/feature_extraction_mctct.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mctct/modeling_mctct.py` & `adapter-transformers-3.2.1/src/transformers/models/mctct/modeling_mctct.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mctct/processing_mctct.py` & `adapter-transformers-3.2.1/src/transformers/models/mctct/processing_mctct.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_bert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_bert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_bert/configuration_megatron_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_bert/configuration_megatron_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_bert/convert_megatron_bert_checkpoint.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_bert/modeling_megatron_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_bert/modeling_megatron_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/checkpoint_reshaping_and_interoperability.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/checkpoint_reshaping_and_interoperability.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/megatron_gpt2/convert_megatron_gpt2_checkpoint.py` & `adapter-transformers-3.2.1/src/transformers/models/megatron_gpt2/convert_megatron_gpt2_checkpoint.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mluke/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mluke/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mluke/convert_mluke_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mluke/convert_mluke_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mluke/tokenization_mluke.py` & `adapter-transformers-3.2.1/src/transformers/models/mluke/tokenization_mluke.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mmbt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mmbt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mmbt/configuration_mmbt.py` & `adapter-transformers-3.2.1/src/transformers/models/mmbt/configuration_mmbt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mmbt/modeling_mmbt.py` & `adapter-transformers-3.2.1/src/transformers/models/mmbt/modeling_mmbt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/configuration_mobilebert.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/configuration_mobilebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/convert_mobilebert_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/convert_mobilebert_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/modeling_mobilebert.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/modeling_mobilebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/modeling_tf_mobilebert.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/modeling_tf_mobilebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/tokenization_mobilebert.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/tokenization_mobilebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilebert/tokenization_mobilebert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilebert/tokenization_mobilebert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/configuration_mobilenet_v1.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/configuration_mobilenet_v1.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/convert_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/convert_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/feature_extraction_mobilenet_v1.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/feature_extraction_mobilenet_v1.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/image_processing_mobilenet_v1.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/image_processing_mobilenet_v1.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v1/modeling_mobilenet_v1.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v1/modeling_mobilenet_v1.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/configuration_mobilenet_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/configuration_mobilenet_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/convert_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/convert_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/feature_extraction_mobilenet_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/feature_extraction_mobilenet_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/image_processing_mobilenet_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/image_processing_mobilenet_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilenet_v2/modeling_mobilenet_v2.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilenet_v2/modeling_mobilenet_v2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/configuration_mobilevit.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/configuration_mobilevit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/convert_mlcvnets_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/convert_mlcvnets_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/feature_extraction_mobilevit.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/feature_extraction_mobilevit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/image_processing_mobilevit.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/image_processing_mobilevit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/modeling_mobilevit.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/modeling_mobilevit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mobilevit/modeling_tf_mobilevit.py` & `adapter-transformers-3.2.1/src/transformers/models/mobilevit/modeling_tf_mobilevit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mpnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mpnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mpnet/configuration_mpnet.py` & `adapter-transformers-3.2.1/src/transformers/models/mpnet/configuration_mpnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mpnet/modeling_mpnet.py` & `adapter-transformers-3.2.1/src/transformers/models/mpnet/modeling_mpnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mpnet/modeling_tf_mpnet.py` & `adapter-transformers-3.2.1/src/transformers/models/mpnet/modeling_tf_mpnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mpnet/tokenization_mpnet.py` & `adapter-transformers-3.2.1/src/transformers/models/mpnet/tokenization_mpnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mpnet/tokenization_mpnet_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/mpnet/tokenization_mpnet_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mt5/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mt5/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mt5/configuration_mt5.py` & `adapter-transformers-3.2.1/src/transformers/models/mt5/configuration_mt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mt5/modeling_flax_mt5.py` & `adapter-transformers-3.2.1/src/transformers/models/mt5/modeling_flax_mt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mt5/modeling_mt5.py` & `adapter-transformers-3.2.1/src/transformers/models/mt5/modeling_mt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mt5/modeling_tf_mt5.py` & `adapter-transformers-3.2.1/src/transformers/models/mt5/modeling_tf_mt5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mvp/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/mvp/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mvp/configuration_mvp.py` & `adapter-transformers-3.2.1/src/transformers/models/mvp/configuration_mvp.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mvp/modeling_mvp.py` & `adapter-transformers-3.2.1/src/transformers/models/mvp/modeling_mvp.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mvp/tokenization_mvp.py` & `adapter-transformers-3.2.1/src/transformers/models/mvp/tokenization_mvp.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/mvp/tokenization_mvp_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/mvp/tokenization_mvp_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nat/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/nat/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nat/configuration_nat.py` & `adapter-transformers-3.2.1/src/transformers/models/nat/configuration_nat.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nat/modeling_nat.py` & `adapter-transformers-3.2.1/src/transformers/models/nat/modeling_nat.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nezha/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/nezha/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nezha/configuration_nezha.py` & `adapter-transformers-3.2.1/src/transformers/models/nezha/configuration_nezha.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nezha/modeling_nezha.py` & `adapter-transformers-3.2.1/src/transformers/models/nezha/modeling_nezha.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nllb/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/nllb/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nllb/tokenization_nllb.py` & `adapter-transformers-3.2.1/src/transformers/models/nllb/tokenization_nllb.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nllb/tokenization_nllb_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/nllb/tokenization_nllb_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nystromformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/nystromformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nystromformer/configuration_nystromformer.py` & `adapter-transformers-3.2.1/src/transformers/models/nystromformer/configuration_nystromformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nystromformer/convert_nystromformer_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/nystromformer/convert_nystromformer_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/nystromformer/modeling_nystromformer.py` & `adapter-transformers-3.2.1/src/transformers/models/nystromformer/modeling_nystromformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/oneformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/oneformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/oneformer/configuration_oneformer.py` & `adapter-transformers-3.2.1/src/transformers/models/oneformer/configuration_oneformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/oneformer/convert_to_hf_oneformer.py` & `adapter-transformers-3.2.1/src/transformers/models/oneformer/convert_to_hf_oneformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/oneformer/image_processing_oneformer.py` & `adapter-transformers-3.2.1/src/transformers/models/oneformer/image_processing_oneformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/oneformer/modeling_oneformer.py` & `adapter-transformers-3.2.1/src/transformers/models/oneformer/modeling_oneformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/oneformer/processing_oneformer.py` & `adapter-transformers-3.2.1/src/transformers/models/oneformer/processing_oneformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/configuration_openai.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/configuration_openai.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/convert_openai_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/convert_openai_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/modeling_openai.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/modeling_openai.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/modeling_tf_openai.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/modeling_tf_openai.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/tokenization_openai.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/tokenization_openai.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/openai/tokenization_openai_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/openai/tokenization_openai_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/opt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/opt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/opt/configuration_opt.py` & `adapter-transformers-3.2.1/src/transformers/models/opt/configuration_opt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/opt/convert_opt_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/opt/convert_opt_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/opt/modeling_flax_opt.py` & `adapter-transformers-3.2.1/src/transformers/models/opt/modeling_flax_opt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/opt/modeling_opt.py` & `adapter-transformers-3.2.1/src/transformers/models/opt/modeling_opt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/opt/modeling_tf_opt.py` & `adapter-transformers-3.2.1/src/transformers/models/opt/modeling_tf_opt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/configuration_owlvit.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/configuration_owlvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/convert_owlvit_original_flax_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/convert_owlvit_original_flax_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/feature_extraction_owlvit.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/feature_extraction_owlvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/image_processing_owlvit.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/image_processing_owlvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/modeling_owlvit.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/modeling_owlvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/owlvit/processing_owlvit.py` & `adapter-transformers-3.2.1/src/transformers/models/owlvit/processing_owlvit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/configuration_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/configuration_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/convert_pegasus_tf_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/convert_pegasus_tf_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/modeling_flax_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/modeling_flax_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/modeling_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/modeling_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/modeling_tf_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/modeling_tf_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/tokenization_pegasus.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/tokenization_pegasus.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus/tokenization_pegasus_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus/tokenization_pegasus_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus_x/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus_x/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus_x/configuration_pegasus_x.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus_x/configuration_pegasus_x.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/pegasus_x/modeling_pegasus_x.py` & `adapter-transformers-3.2.1/src/transformers/models/pegasus_x/modeling_pegasus_x.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/configuration_perceiver.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/configuration_perceiver.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/convert_perceiver_haiku_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/convert_perceiver_haiku_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/feature_extraction_perceiver.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/feature_extraction_perceiver.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/image_processing_perceiver.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/image_processing_perceiver.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/modeling_perceiver.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/modeling_perceiver.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/perceiver/tokenization_perceiver.py` & `adapter-transformers-3.2.1/src/transformers/models/perceiver/tokenization_perceiver.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/phobert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/phobert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/phobert/tokenization_phobert.py` & `adapter-transformers-3.2.1/src/transformers/models/phobert/tokenization_phobert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/plbart/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/plbart/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/plbart/configuration_plbart.py` & `adapter-transformers-3.2.1/src/transformers/models/plbart/configuration_plbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/plbart/convert_plbart_original_checkpoint_to_torch.py` & `adapter-transformers-3.2.1/src/transformers/models/plbart/convert_plbart_original_checkpoint_to_torch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/plbart/modeling_plbart.py` & `adapter-transformers-3.2.1/src/transformers/models/plbart/modeling_plbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/plbart/tokenization_plbart.py` & `adapter-transformers-3.2.1/src/transformers/models/plbart/tokenization_plbart.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/poolformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/poolformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/poolformer/configuration_poolformer.py` & `adapter-transformers-3.2.1/src/transformers/models/poolformer/configuration_poolformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/poolformer/convert_poolformer_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/poolformer/convert_poolformer_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/poolformer/feature_extraction_poolformer.py` & `adapter-transformers-3.2.1/src/transformers/models/poolformer/feature_extraction_poolformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/poolformer/image_processing_poolformer.py` & `adapter-transformers-3.2.1/src/transformers/models/poolformer/image_processing_poolformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/poolformer/modeling_poolformer.py` & `adapter-transformers-3.2.1/src/transformers/models/poolformer/modeling_poolformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/prophetnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/prophetnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/prophetnet/configuration_prophetnet.py` & `adapter-transformers-3.2.1/src/transformers/models/prophetnet/configuration_prophetnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/prophetnet/convert_prophetnet_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/prophetnet/convert_prophetnet_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/prophetnet/modeling_prophetnet.py` & `adapter-transformers-3.2.1/src/transformers/models/prophetnet/modeling_prophetnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/prophetnet/tokenization_prophetnet.py` & `adapter-transformers-3.2.1/src/transformers/models/prophetnet/tokenization_prophetnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/qdqbert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/qdqbert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/qdqbert/configuration_qdqbert.py` & `adapter-transformers-3.2.1/src/transformers/models/qdqbert/configuration_qdqbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/qdqbert/modeling_qdqbert.py` & `adapter-transformers-3.2.1/src/transformers/models/qdqbert/modeling_qdqbert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rag/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/rag/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rag/configuration_rag.py` & `adapter-transformers-3.2.1/src/transformers/models/rag/configuration_rag.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rag/modeling_rag.py` & `adapter-transformers-3.2.1/src/transformers/models/rag/modeling_rag.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rag/modeling_tf_rag.py` & `adapter-transformers-3.2.1/src/transformers/models/rag/modeling_tf_rag.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rag/retrieval_rag.py` & `adapter-transformers-3.2.1/src/transformers/models/rag/retrieval_rag.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rag/tokenization_rag.py` & `adapter-transformers-3.2.1/src/transformers/models/rag/tokenization_rag.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/realm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/realm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/realm/configuration_realm.py` & `adapter-transformers-3.2.1/src/transformers/models/realm/configuration_realm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/realm/modeling_realm.py` & `adapter-transformers-3.2.1/src/transformers/models/realm/modeling_realm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/realm/retrieval_realm.py` & `adapter-transformers-3.2.1/src/transformers/models/realm/retrieval_realm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/realm/tokenization_realm.py` & `adapter-transformers-3.2.1/src/transformers/models/realm/tokenization_realm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/realm/tokenization_realm_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/realm/tokenization_realm_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/reformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/reformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/reformer/configuration_reformer.py` & `adapter-transformers-3.2.1/src/transformers/models/reformer/configuration_reformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/reformer/convert_reformer_trax_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/reformer/convert_reformer_trax_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/reformer/modeling_reformer.py` & `adapter-transformers-3.2.1/src/transformers/models/reformer/modeling_reformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/reformer/tokenization_reformer.py` & `adapter-transformers-3.2.1/src/transformers/models/reformer/tokenization_reformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/reformer/tokenization_reformer_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/reformer/tokenization_reformer_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/regnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/regnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/regnet/configuration_regnet.py` & `adapter-transformers-3.2.1/src/transformers/models/regnet/configuration_regnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/regnet/convert_regnet_seer_10b_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/regnet/convert_regnet_seer_10b_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/regnet/convert_regnet_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/regnet/convert_regnet_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/regnet/modeling_regnet.py` & `adapter-transformers-3.2.1/src/transformers/models/regnet/modeling_regnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/regnet/modeling_tf_regnet.py` & `adapter-transformers-3.2.1/src/transformers/models/regnet/modeling_tf_regnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/configuration_rembert.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/configuration_rembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/convert_rembert_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/convert_rembert_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/modeling_rembert.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/modeling_rembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/modeling_tf_rembert.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/modeling_tf_rembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/tokenization_rembert.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/tokenization_rembert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/rembert/tokenization_rembert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/rembert/tokenization_rembert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/resnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/resnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/resnet/configuration_resnet.py` & `adapter-transformers-3.2.1/src/transformers/models/resnet/configuration_resnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/resnet/convert_resnet_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/resnet/convert_resnet_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/resnet/modeling_resnet.py` & `adapter-transformers-3.2.1/src/transformers/models/resnet/modeling_resnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/resnet/modeling_tf_resnet.py` & `adapter-transformers-3.2.1/src/transformers/models/resnet/modeling_tf_resnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/retribert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/retribert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/retribert/configuration_retribert.py` & `adapter-transformers-3.2.1/src/transformers/models/retribert/configuration_retribert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/retribert/modeling_retribert.py` & `adapter-transformers-3.2.1/src/transformers/models/retribert/modeling_retribert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/retribert/tokenization_retribert.py` & `adapter-transformers-3.2.1/src/transformers/models/retribert/tokenization_retribert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/retribert/tokenization_retribert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/retribert/tokenization_retribert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/configuration_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/configuration_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/convert_roberta_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/convert_roberta_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/modeling_flax_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/modeling_flax_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/modeling_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/modeling_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/modeling_tf_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/modeling_tf_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/tokenization_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/tokenization_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta/tokenization_roberta_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta/tokenization_roberta_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/configuration_roberta_prelayernorm.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/configuration_roberta_prelayernorm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/convert_roberta_prelayernorm_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/convert_roberta_prelayernorm_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/modeling_flax_roberta_prelayernorm.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/modeling_flax_roberta_prelayernorm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/modeling_roberta_prelayernorm.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/modeling_roberta_prelayernorm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roberta_prelayernorm/modeling_tf_roberta_prelayernorm.py` & `adapter-transformers-3.2.1/src/transformers/models/roberta_prelayernorm/modeling_tf_roberta_prelayernorm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roc_bert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/roc_bert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roc_bert/configuration_roc_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/roc_bert/configuration_roc_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roc_bert/modeling_roc_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/roc_bert/modeling_roc_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roc_bert/tokenization_roc_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/roc_bert/tokenization_roc_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/configuration_roformer.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/configuration_roformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/convert_roformer_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/convert_roformer_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/modeling_flax_roformer.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/modeling_flax_roformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/modeling_roformer.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/modeling_roformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/modeling_tf_roformer.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/modeling_tf_roformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/tokenization_roformer.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/tokenization_roformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/tokenization_roformer_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/tokenization_roformer_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/roformer/tokenization_utils.py` & `adapter-transformers-3.2.1/src/transformers/models/roformer/tokenization_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/configuration_segformer.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/configuration_segformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/convert_segformer_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/convert_segformer_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/feature_extraction_segformer.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/feature_extraction_segformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/image_processing_segformer.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/image_processing_segformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/modeling_segformer.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/modeling_segformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/segformer/modeling_tf_segformer.py` & `adapter-transformers-3.2.1/src/transformers/models/segformer/modeling_tf_segformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/sew/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew/configuration_sew.py` & `adapter-transformers-3.2.1/src/transformers/models/sew/configuration_sew.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew/convert_sew_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/sew/convert_sew_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew/modeling_sew.py` & `adapter-transformers-3.2.1/src/transformers/models/sew/modeling_sew.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew_d/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/sew_d/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew_d/configuration_sew_d.py` & `adapter-transformers-3.2.1/src/transformers/models/sew_d/configuration_sew_d.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew_d/convert_sew_d_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/sew_d/convert_sew_d_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/sew_d/modeling_sew_d.py` & `adapter-transformers-3.2.1/src/transformers/models/sew_d/modeling_sew_d.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/configuration_speech_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/configuration_speech_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/convert_mbart_wav2vec2_seq2seq_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/convert_mbart_wav2vec2_seq2seq_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/convert_speech_to_text_wav2vec2_seq2seq_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/convert_speech_to_text_wav2vec2_seq2seq_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/modeling_flax_speech_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/modeling_flax_speech_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_encoder_decoder/modeling_speech_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_encoder_decoder/modeling_speech_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/configuration_speech_to_text.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/configuration_speech_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/convert_s2t_fairseq_to_tfms.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/convert_s2t_fairseq_to_tfms.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/feature_extraction_speech_to_text.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/feature_extraction_speech_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/modeling_speech_to_text.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/modeling_speech_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/modeling_tf_speech_to_text.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/modeling_tf_speech_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/processing_speech_to_text.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/processing_speech_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text/tokenization_speech_to_text.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text/tokenization_speech_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/configuration_speech_to_text_2.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/configuration_speech_to_text_2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/modeling_speech_to_text_2.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/modeling_speech_to_text_2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/processing_speech_to_text_2.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/processing_speech_to_text_2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/speech_to_text_2/tokenization_speech_to_text_2.py` & `adapter-transformers-3.2.1/src/transformers/models/speech_to_text_2/tokenization_speech_to_text_2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/splinter/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/splinter/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/splinter/configuration_splinter.py` & `adapter-transformers-3.2.1/src/transformers/models/splinter/configuration_splinter.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/splinter/modeling_splinter.py` & `adapter-transformers-3.2.1/src/transformers/models/splinter/modeling_splinter.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/splinter/tokenization_splinter.py` & `adapter-transformers-3.2.1/src/transformers/models/splinter/tokenization_splinter.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/splinter/tokenization_splinter_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/splinter/tokenization_splinter_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/squeezebert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/squeezebert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/squeezebert/configuration_squeezebert.py` & `adapter-transformers-3.2.1/src/transformers/models/squeezebert/configuration_squeezebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/squeezebert/modeling_squeezebert.py` & `adapter-transformers-3.2.1/src/transformers/models/squeezebert/modeling_squeezebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/squeezebert/tokenization_squeezebert.py` & `adapter-transformers-3.2.1/src/transformers/models/squeezebert/tokenization_squeezebert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/squeezebert/tokenization_squeezebert_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/squeezebert/tokenization_squeezebert_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/swin/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin/configuration_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/swin/configuration_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin/convert_swin_simmim_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/swin/convert_swin_simmim_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin/convert_swin_timm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/swin/convert_swin_timm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin/modeling_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/swin/modeling_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin/modeling_tf_swin.py` & `adapter-transformers-3.2.1/src/transformers/models/swin/modeling_tf_swin.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin2sr/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/swin2sr/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin2sr/configuration_swin2sr.py` & `adapter-transformers-3.2.1/src/transformers/models/swin2sr/configuration_swin2sr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin2sr/convert_swin2sr_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/swin2sr/convert_swin2sr_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin2sr/image_processing_swin2sr.py` & `adapter-transformers-3.2.1/src/transformers/models/swin2sr/image_processing_swin2sr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swin2sr/modeling_swin2sr.py` & `adapter-transformers-3.2.1/src/transformers/models/swin2sr/modeling_swin2sr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swinv2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/swinv2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swinv2/configuration_swinv2.py` & `adapter-transformers-3.2.1/src/transformers/models/swinv2/configuration_swinv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swinv2/convert_swinv2_timm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/swinv2/convert_swinv2_timm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/swinv2/modeling_swinv2.py` & `adapter-transformers-3.2.1/src/transformers/models/swinv2/modeling_swinv2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/switch_transformers/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/switch_transformers/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/switch_transformers/configuration_switch_transformers.py` & `adapter-transformers-3.2.1/src/transformers/models/switch_transformers/configuration_switch_transformers.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/switch_transformers/convert_big_switch.py` & `adapter-transformers-3.2.1/src/transformers/models/switch_transformers/convert_big_switch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/switch_transformers/convert_switch_transformers_original_flax_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/switch_transformers/convert_switch_transformers_original_flax_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/switch_transformers/modeling_switch_transformers.py` & `adapter-transformers-3.2.1/src/transformers/models/switch_transformers/modeling_switch_transformers.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/configuration_t5.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/configuration_t5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/convert_t5_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/convert_t5_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/convert_t5x_checkpoint_to_flax.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/convert_t5x_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/convert_t5x_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/modeling_flax_t5.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/modeling_flax_t5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/modeling_t5.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/modeling_t5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/modeling_tf_t5.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/modeling_tf_t5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/tokenization_t5.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/tokenization_t5.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/t5/tokenization_t5_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/t5/tokenization_t5_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/table_transformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/table_transformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/table_transformer/configuration_table_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/table_transformer/configuration_table_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/table_transformer/convert_table_transformer_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/table_transformer/convert_table_transformer_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/table_transformer/modeling_table_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/table_transformer/modeling_table_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapas/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/tapas/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapas/configuration_tapas.py` & `adapter-transformers-3.2.1/src/transformers/models/tapas/configuration_tapas.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapas/convert_tapas_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/tapas/convert_tapas_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapas/modeling_tapas.py` & `adapter-transformers-3.2.1/src/transformers/models/tapas/modeling_tapas.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapas/modeling_tf_tapas.py` & `adapter-transformers-3.2.1/src/transformers/models/tapas/modeling_tf_tapas.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapas/tokenization_tapas.py` & `adapter-transformers-3.2.1/src/transformers/models/tapas/tokenization_tapas.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapex/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/tapex/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/tapex/tokenization_tapex.py` & `adapter-transformers-3.2.1/src/transformers/models/tapex/tokenization_tapex.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/configuration_time_series_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/configuration_time_series_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/time_series_transformer/modeling_time_series_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/time_series_transformer/modeling_time_series_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/timesformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/timesformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/timesformer/configuration_timesformer.py` & `adapter-transformers-3.2.1/src/transformers/models/timesformer/configuration_timesformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/timesformer/convert_timesformer_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/timesformer/convert_timesformer_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/timesformer/modeling_timesformer.py` & `adapter-transformers-3.2.1/src/transformers/models/timesformer/modeling_timesformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/configuration_trajectory_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/configuration_trajectory_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/convert_trajectory_transformer_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trajectory_transformer/modeling_trajectory_transformer.py` & `adapter-transformers-3.2.1/src/transformers/models/trajectory_transformer/modeling_trajectory_transformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/configuration_transfo_xl.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/configuration_transfo_xl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/convert_transfo_xl_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/convert_transfo_xl_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_tf_transfo_xl.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_tf_transfo_xl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_tf_transfo_xl_utilities.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_tf_transfo_xl_utilities.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_transfo_xl.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_transfo_xl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/modeling_transfo_xl_utilities.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/modeling_transfo_xl_utilities.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/transfo_xl/tokenization_transfo_xl.py` & `adapter-transformers-3.2.1/src/transformers/models/transfo_xl/tokenization_transfo_xl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trocr/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/trocr/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trocr/configuration_trocr.py` & `adapter-transformers-3.2.1/src/transformers/models/trocr/configuration_trocr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trocr/convert_trocr_unilm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/trocr/convert_trocr_unilm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trocr/modeling_trocr.py` & `adapter-transformers-3.2.1/src/transformers/models/trocr/modeling_trocr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/trocr/processing_trocr.py` & `adapter-transformers-3.2.1/src/transformers/models/trocr/processing_trocr.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech/configuration_unispeech.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech/configuration_unispeech.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech/convert_unispeech_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech/convert_unispeech_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech/modeling_unispeech.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech/modeling_unispeech.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/configuration_unispeech_sat.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/configuration_unispeech_sat.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/convert_unispeech_original_s3prl_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/convert_unispeech_original_s3prl_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/convert_unispeech_sat_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/convert_unispeech_sat_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/unispeech_sat/modeling_unispeech_sat.py` & `adapter-transformers-3.2.1/src/transformers/models/unispeech_sat/modeling_unispeech_sat.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/upernet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/upernet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/upernet/configuration_upernet.py` & `adapter-transformers-3.2.1/src/transformers/models/upernet/configuration_upernet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/upernet/convert_convnext_upernet_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/upernet/convert_convnext_upernet_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/upernet/convert_swin_upernet_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/upernet/convert_swin_upernet_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/upernet/modeling_upernet.py` & `adapter-transformers-3.2.1/src/transformers/models/upernet/modeling_upernet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/van/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/van/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/van/configuration_van.py` & `adapter-transformers-3.2.1/src/transformers/models/van/configuration_van.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/van/convert_van_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/van/convert_van_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/van/modeling_van.py` & `adapter-transformers-3.2.1/src/transformers/models/van/modeling_van.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/videomae/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/videomae/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/videomae/configuration_videomae.py` & `adapter-transformers-3.2.1/src/transformers/models/videomae/configuration_videomae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/videomae/convert_videomae_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/videomae/convert_videomae_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/videomae/feature_extraction_videomae.py` & `adapter-transformers-3.2.1/src/transformers/models/videomae/feature_extraction_videomae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/videomae/image_processing_videomae.py` & `adapter-transformers-3.2.1/src/transformers/models/videomae/image_processing_videomae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/videomae/modeling_videomae.py` & `adapter-transformers-3.2.1/src/transformers/models/videomae/modeling_videomae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/configuration_vilt.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/configuration_vilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/convert_vilt_original_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/convert_vilt_original_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/feature_extraction_vilt.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/feature_extraction_vilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/image_processing_vilt.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/image_processing_vilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/modeling_vilt.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/modeling_vilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vilt/processing_vilt.py` & `adapter-transformers-3.2.1/src/transformers/models/vilt/processing_vilt.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/configuration_vision_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/configuration_vision_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/modeling_flax_vision_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/modeling_flax_vision_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/modeling_tf_vision_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/modeling_tf_vision_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_encoder_decoder/modeling_vision_encoder_decoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_encoder_decoder/modeling_vision_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/configuration_vision_text_dual_encoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/modeling_flax_vision_text_dual_encoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/modeling_flax_vision_text_dual_encoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/modeling_vision_text_dual_encoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vision_text_dual_encoder/processing_vision_text_dual_encoder.py` & `adapter-transformers-3.2.1/src/transformers/models/vision_text_dual_encoder/processing_vision_text_dual_encoder.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/visual_bert/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/visual_bert/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/visual_bert/configuration_visual_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/visual_bert/configuration_visual_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/visual_bert/convert_visual_bert_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/visual_bert/convert_visual_bert_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/visual_bert/modeling_visual_bert.py` & `adapter-transformers-3.2.1/src/transformers/models/visual_bert/modeling_visual_bert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/configuration_vit.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/configuration_vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/convert_dino_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/convert_dino_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/convert_vit_timm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/convert_vit_timm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/feature_extraction_vit.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/feature_extraction_vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/image_processing_vit.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/image_processing_vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/modeling_flax_vit.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/modeling_flax_vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/modeling_tf_vit.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/modeling_tf_vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit/modeling_vit.py` & `adapter-transformers-3.2.1/src/transformers/models/vit/modeling_vit.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/configuration_vit_hybrid.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/configuration_vit_hybrid.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/convert_vit_hybrid_timm_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/convert_vit_hybrid_timm_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/image_processing_vit_hybrid.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/image_processing_vit_hybrid.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_hybrid/modeling_vit_hybrid.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_hybrid/modeling_vit_hybrid.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_mae/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_mae/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_mae/configuration_vit_mae.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_mae/configuration_vit_mae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_mae/convert_vit_mae_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_mae/convert_vit_mae_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_mae/modeling_tf_vit_mae.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_mae/modeling_tf_vit_mae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_mae/modeling_vit_mae.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_mae/modeling_vit_mae.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_msn/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_msn/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_msn/configuration_vit_msn.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_msn/configuration_vit_msn.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_msn/convert_msn_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_msn/convert_msn_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/vit_msn/modeling_vit_msn.py` & `adapter-transformers-3.2.1/src/transformers/models/vit_msn/modeling_vit_msn.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/configuration_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/configuration_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/convert_wav2vec2_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/convert_wav2vec2_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/convert_wav2vec2_original_s3prl_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/convert_wav2vec2_original_s3prl_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/feature_extraction_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/feature_extraction_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/modeling_flax_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/modeling_flax_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/modeling_tf_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/modeling_tf_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/modeling_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/modeling_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/processing_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/processing_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2/tokenization_wav2vec2.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2/tokenization_wav2vec2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/configuration_wav2vec2_conformer.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/configuration_wav2vec2_conformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/convert_wav2vec2_conformer_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/convert_wav2vec2_conformer_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_conformer/modeling_wav2vec2_conformer.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_conformer/modeling_wav2vec2_conformer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_phoneme/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_phoneme/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_phoneme/tokenization_wav2vec2_phoneme.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_with_lm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_with_lm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wav2vec2_with_lm/processing_wav2vec2_with_lm.py` & `adapter-transformers-3.2.1/src/transformers/models/wav2vec2_with_lm/processing_wav2vec2_with_lm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wavlm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/wavlm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wavlm/configuration_wavlm.py` & `adapter-transformers-3.2.1/src/transformers/models/wavlm/configuration_wavlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wavlm/convert_wavlm_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/wavlm/convert_wavlm_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wavlm/convert_wavlm_original_s3prl_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/wavlm/convert_wavlm_original_s3prl_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/wavlm/modeling_wavlm.py` & `adapter-transformers-3.2.1/src/transformers/models/wavlm/modeling_wavlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/configuration_whisper.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/configuration_whisper.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/convert_openai_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/convert_openai_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/english_normalizer.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/english_normalizer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/feature_extraction_whisper.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/feature_extraction_whisper.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/modeling_tf_whisper.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/modeling_tf_whisper.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/modeling_whisper.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/modeling_whisper.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/processing_whisper.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/processing_whisper.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/whisper/tokenization_whisper.py` & `adapter-transformers-3.2.1/src/transformers/models/whisper/tokenization_whisper.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/x_clip/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/x_clip/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/x_clip/configuration_x_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/x_clip/configuration_x_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/x_clip/convert_x_clip_original_pytorch_to_hf.py` & `adapter-transformers-3.2.1/src/transformers/models/x_clip/convert_x_clip_original_pytorch_to_hf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/x_clip/modeling_x_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/x_clip/modeling_x_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/x_clip/processing_x_clip.py` & `adapter-transformers-3.2.1/src/transformers/models/x_clip/processing_x_clip.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/configuration_xglm.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/configuration_xglm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/convert_xglm_original_ckpt_to_trfms.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/convert_xglm_original_ckpt_to_trfms.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/modeling_flax_xglm.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/modeling_flax_xglm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/modeling_tf_xglm.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/modeling_tf_xglm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/modeling_xglm.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/modeling_xglm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/tokenization_xglm.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/tokenization_xglm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xglm/tokenization_xglm_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/xglm/tokenization_xglm_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm/configuration_xlm.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm/configuration_xlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm/convert_xlm_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm/convert_xlm_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm/modeling_tf_xlm.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm/modeling_tf_xlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm/modeling_xlm.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm/modeling_xlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm/tokenization_xlm.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm/tokenization_xlm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/configuration_xlm_prophetnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/configuration_xlm_prophetnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/modeling_xlm_prophetnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/modeling_xlm_prophetnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_prophetnet/tokenization_xlm_prophetnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_prophetnet/tokenization_xlm_prophetnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/configuration_xlm_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/configuration_xlm_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/modeling_flax_xlm_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/modeling_flax_xlm_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/modeling_tf_xlm_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/modeling_tf_xlm_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/modeling_xlm_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/tokenization_xlm_roberta.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta/tokenization_xlm_roberta_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta/tokenization_xlm_roberta_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/configuration_xlm_roberta_xl.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/configuration_xlm_roberta_xl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/convert_xlm_roberta_xl_original_pytorch_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/convert_xlm_roberta_xl_original_pytorch_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlm_roberta_xl/modeling_xlm_roberta_xl.py` & `adapter-transformers-3.2.1/src/transformers/models/xlm_roberta_xl/modeling_xlm_roberta_xl.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/configuration_xlnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/configuration_xlnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/convert_xlnet_original_tf_checkpoint_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/convert_xlnet_original_tf_checkpoint_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/modeling_tf_xlnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/modeling_tf_xlnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/modeling_xlnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/modeling_xlnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/tokenization_xlnet.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/tokenization_xlnet.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/xlnet/tokenization_xlnet_fast.py` & `adapter-transformers-3.2.1/src/transformers/models/xlnet/tokenization_xlnet_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yolos/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/yolos/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yolos/configuration_yolos.py` & `adapter-transformers-3.2.1/src/transformers/models/yolos/configuration_yolos.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yolos/convert_yolos_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/yolos/convert_yolos_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yolos/feature_extraction_yolos.py` & `adapter-transformers-3.2.1/src/transformers/models/yolos/feature_extraction_yolos.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yolos/image_processing_yolos.py` & `adapter-transformers-3.2.1/src/transformers/models/yolos/image_processing_yolos.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yolos/modeling_yolos.py` & `adapter-transformers-3.2.1/src/transformers/models/yolos/modeling_yolos.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yoso/__init__.py` & `adapter-transformers-3.2.1/src/transformers/models/yoso/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yoso/configuration_yoso.py` & `adapter-transformers-3.2.1/src/transformers/models/yoso/configuration_yoso.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yoso/convert_yoso_pytorch_to_pytorch.py` & `adapter-transformers-3.2.1/src/transformers/models/yoso/convert_yoso_pytorch_to_pytorch.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/models/yoso/modeling_yoso.py` & `adapter-transformers-3.2.1/src/transformers/models/yoso/modeling_yoso.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/onnx/__init__.py` & `adapter-transformers-3.2.1/src/transformers/onnx/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/onnx/__main__.py` & `adapter-transformers-3.2.1/src/transformers/onnx/__main__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/onnx/config.py` & `adapter-transformers-3.2.1/src/transformers/onnx/config.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/onnx/convert.py` & `adapter-transformers-3.2.1/src/transformers/onnx/convert.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/onnx/features.py` & `adapter-transformers-3.2.1/src/transformers/onnx/features.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/onnx/utils.py` & `adapter-transformers-3.2.1/src/transformers/onnx/utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/optimization.py` & `adapter-transformers-3.2.1/src/transformers/optimization.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/optimization_tf.py` & `adapter-transformers-3.2.1/src/transformers/optimization_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/__init__.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/audio_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/audio_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/audio_utils.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/audio_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/automatic_speech_recognition.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/automatic_speech_recognition.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/base.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/base.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/conversational.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/conversational.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/depth_estimation.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/depth_estimation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/document_question_answering.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/document_question_answering.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/feature_extraction.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/feature_extraction.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/fill_mask.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/fill_mask.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/image_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/image_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/image_segmentation.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/image_segmentation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/image_to_text.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/image_to_text.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/object_detection.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/object_detection.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/pt_utils.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/pt_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/question_answering.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/question_answering.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/table_question_answering.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/table_question_answering.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/text2text_generation.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/text2text_generation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/text_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/text_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/text_generation.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/text_generation.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/token_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/token_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/video_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/video_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/visual_question_answering.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/visual_question_answering.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/zero_shot_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/zero_shot_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/zero_shot_image_classification.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/zero_shot_image_classification.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pipelines/zero_shot_object_detection.py` & `adapter-transformers-3.2.1/src/transformers/pipelines/zero_shot_object_detection.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/processing_utils.py` & `adapter-transformers-3.2.1/src/transformers/processing_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/pytorch_utils.py` & `adapter-transformers-3.2.1/src/transformers/pytorch_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/sagemaker/__init__.py` & `adapter-transformers-3.2.1/src/transformers/sagemaker/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/sagemaker/trainer_sm.py` & `adapter-transformers-3.2.1/src/transformers/sagemaker/trainer_sm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/sagemaker/training_args_sm.py` & `adapter-transformers-3.2.1/src/transformers/sagemaker/training_args_sm.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/testing_utils.py` & `adapter-transformers-3.2.1/src/transformers/testing_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/tf_utils.py` & `adapter-transformers-3.2.1/src/transformers/tf_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/tokenization_utils.py` & `adapter-transformers-3.2.1/src/transformers/tokenization_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/tokenization_utils_base.py` & `adapter-transformers-3.2.1/src/transformers/tokenization_utils_base.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/tokenization_utils_fast.py` & `adapter-transformers-3.2.1/src/transformers/tokenization_utils_fast.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/trainer.py` & `adapter-transformers-3.2.1/src/transformers/trainer.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/trainer_callback.py` & `adapter-transformers-3.2.1/src/transformers/trainer_callback.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/trainer_pt_utils.py` & `adapter-transformers-3.2.1/src/transformers/trainer_pt_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/trainer_seq2seq.py` & `adapter-transformers-3.2.1/src/transformers/trainer_seq2seq.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/trainer_tf.py` & `adapter-transformers-3.2.1/src/transformers/trainer_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/trainer_utils.py` & `adapter-transformers-3.2.1/src/transformers/trainer_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/training_args.py` & `adapter-transformers-3.2.1/src/transformers/training_args.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/training_args_seq2seq.py` & `adapter-transformers-3.2.1/src/transformers/training_args_seq2seq.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/training_args_tf.py` & `adapter-transformers-3.2.1/src/transformers/training_args_tf.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/__init__.py` & `adapter-transformers-3.2.1/src/transformers/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/bitsandbytes.py` & `adapter-transformers-3.2.1/src/transformers/utils/bitsandbytes.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/doc.py` & `adapter-transformers-3.2.1/src/transformers/utils/doc.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_flax_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_flax_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_pt_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_pt_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_sentencepiece_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_sentencepiece_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_speech_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_speech_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_tf_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_tf_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_timm_and_vision_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_timm_and_vision_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_tokenizers_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_tokenizers_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/dummy_vision_objects.py` & `adapter-transformers-3.2.1/src/transformers/utils/dummy_vision_objects.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/fx.py` & `adapter-transformers-3.2.1/src/transformers/utils/fx.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/generic.py` & `adapter-transformers-3.2.1/src/transformers/utils/generic.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/hp_naming.py` & `adapter-transformers-3.2.1/src/transformers/utils/hp_naming.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/hub.py` & `adapter-transformers-3.2.1/src/transformers/utils/hub.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/import_utils.py` & `adapter-transformers-3.2.1/src/transformers/utils/import_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/logging.py` & `adapter-transformers-3.2.1/src/transformers/utils/logging.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/model_parallel_utils.py` & `adapter-transformers-3.2.1/src/transformers/utils/model_parallel_utils.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/notebook.py` & `adapter-transformers-3.2.1/src/transformers/utils/notebook.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/sentencepiece_model_pb2.py` & `adapter-transformers-3.2.1/src/transformers/utils/sentencepiece_model_pb2.py`

 * *Files identical despite different names*

### Comparing `adapter-transformers-3.2.0/src/transformers/utils/versions.py` & `adapter-transformers-3.2.1/src/transformers/utils/versions.py`

 * *Files identical despite different names*

