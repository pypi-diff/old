# Comparing `tmp/textgen-0.1.7.tar.gz` & `tmp/textgen-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "textgen-0.1.7.tar", last modified: Mon Nov 28 04:00:54 2022, max compression
+gzip compressed data, was "textgen-0.1.8.tar", last modified: Fri Apr  7 09:20:39 2023, max compression
```

## Comparing `textgen-0.1.7.tar` & `textgen-0.1.8.tar`

### file list

```diff
@@ -1,64 +1,64 @@
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.222367 textgen-0.1.7/
--rw-r--r--   0 xuming     (501) staff       (20)    11357 2021-08-05 02:59:06.000000 textgen-0.1.7/LICENSE
--rw-r--r--   0 xuming     (501) staff       (20)    26535 2022-11-28 04:00:54.222825 textgen-0.1.7/PKG-INFO
--rw-r--r--   0 xuming     (501) staff       (20)    22182 2022-11-27 06:14:50.000000 textgen-0.1.7/README.md
--rw-r--r--   0 xuming     (501) staff       (20)      309 2022-11-28 04:00:54.223645 textgen-0.1.7/setup.cfg
--rw-r--r--   0 xuming     (501) staff       (20)     1356 2022-11-28 03:49:38.000000 textgen-0.1.7/setup.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.126855 textgen-0.1.7/textgen/
--rw-r--r--   0 xuming     (501) staff       (20)     1291 2022-11-28 03:51:10.000000 textgen-0.1.7/textgen/__init__.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.145789 textgen-0.1.7/textgen/augment/
--rw-r--r--   0 xuming     (501) staff       (20)      133 2022-06-30 07:59:18.000000 textgen-0.1.7/textgen/augment/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)     1493 2022-05-09 11:34:10.000000 textgen-0.1.7/textgen/augment/sentence_level_augment.py
--rw-r--r--   0 xuming     (501) staff       (20)     3384 2022-09-26 07:08:57.000000 textgen-0.1.7/textgen/augment/text_augment.py
--rw-r--r--   0 xuming     (501) staff       (20)     2256 2022-07-04 08:00:34.000000 textgen-0.1.7/textgen/augment/tokenizer.py
--rw-r--r--   0 xuming     (501) staff       (20)     1971 2021-08-05 02:59:06.000000 textgen-0.1.7/textgen/augment/translate_api.py
--rw-r--r--   0 xuming     (501) staff       (20)    13027 2022-09-26 07:39:41.000000 textgen-0.1.7/textgen/augment/word_level_augment.py
--rw-r--r--   0 xuming     (501) staff       (20)     1240 2022-05-09 11:34:10.000000 textgen-0.1.7/textgen/augment/word_vocab.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.150234 textgen-0.1.7/textgen/config/
--rw-r--r--   0 xuming     (501) staff       (20)      140 2021-08-05 02:59:06.000000 textgen-0.1.7/textgen/config/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)     1845 2022-06-30 03:18:51.000000 textgen-0.1.7/textgen/config/global_args.py
--rw-r--r--   0 xuming     (501) staff       (20)    12871 2022-09-13 02:20:38.000000 textgen-0.1.7/textgen/config/model_args.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.152904 textgen-0.1.7/textgen/custom_models/
--rwxr-xr-x   0 xuming     (501) staff       (20)        0 2021-08-05 02:59:06.000000 textgen-0.1.7/textgen/custom_models/__init__.py
--rwxr-xr-x   0 xuming     (501) staff       (20)    32645 2022-08-24 03:27:39.000000 textgen-0.1.7/textgen/custom_models/models.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.157554 textgen-0.1.7/textgen/data/
--rwxr-xr-x   0 xuming     (501) staff       (20)    48098 2019-08-25 14:57:21.000000 textgen-0.1.7/textgen/data/HowNetPOSWord.txt
--rw-r--r--   0 xuming     (501) staff       (20)    17438 2021-10-25 11:27:11.000000 textgen-0.1.7/textgen/data/stopwords.txt
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.164772 textgen-0.1.7/textgen/language_generation/
--rwxr-xr-x   0 xuming     (501) staff       (20)      292 2021-08-05 02:59:06.000000 textgen-0.1.7/textgen/language_generation/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)    10056 2022-07-05 07:48:33.000000 textgen-0.1.7/textgen/language_generation/language_generation_model.py
--rw-r--r--   0 xuming     (501) staff       (20)     2829 2022-06-14 12:08:00.000000 textgen-0.1.7/textgen/language_generation/language_generation_utils.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.177204 textgen-0.1.7/textgen/language_modeling/
--rwxr-xr-x   0 xuming     (501) staff       (20)      407 2022-09-10 06:38:25.000000 textgen-0.1.7/textgen/language_modeling/__init__.py
--rwxr-xr-x   0 xuming     (501) staff       (20)    56833 2022-09-09 11:41:34.000000 textgen-0.1.7/textgen/language_modeling/language_modeling_model.py
--rw-r--r--   0 xuming     (501) staff       (20)     8938 2022-06-14 12:08:00.000000 textgen-0.1.7/textgen/language_modeling/language_modeling_utils.py
--rw-r--r--   0 xuming     (501) staff       (20)    65595 2022-11-27 05:36:55.000000 textgen-0.1.7/textgen/language_modeling/songnet_model.py
--rw-r--r--   0 xuming     (501) staff       (20)    17103 2022-11-28 03:49:38.000000 textgen-0.1.7/textgen/language_modeling/songnet_utils.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.184424 textgen-0.1.7/textgen/question_answering/
--rwxr-xr-x   0 xuming     (501) staff       (20)      287 2021-08-05 02:59:06.000000 textgen-0.1.7/textgen/question_answering/__init__.py
--rwxr-xr-x   0 xuming     (501) staff       (20)    61756 2022-09-09 11:41:34.000000 textgen-0.1.7/textgen/question_answering/question_answering_model.py
--rwxr-xr-x   0 xuming     (501) staff       (20)    77131 2022-06-14 12:36:04.000000 textgen-0.1.7/textgen/question_answering/question_answering_utils.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.202822 textgen-0.1.7/textgen/seq2seq/
--rwxr-xr-x   0 xuming     (501) staff       (20)      313 2022-08-07 03:00:11.000000 textgen-0.1.7/textgen/seq2seq/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)    73298 2022-09-09 11:41:34.000000 textgen-0.1.7/textgen/seq2seq/bart_seq2seq_model.py
--rw-r--r--   0 xuming     (501) staff       (20)    18559 2022-06-19 09:29:30.000000 textgen-0.1.7/textgen/seq2seq/bart_seq2seq_utils.py
--rw-r--r--   0 xuming     (501) staff       (20)    23456 2022-08-25 03:06:56.000000 textgen-0.1.7/textgen/seq2seq/conv_seq2seq_model.py
--rw-r--r--   0 xuming     (501) staff       (20)     4345 2022-05-10 10:48:02.000000 textgen-0.1.7/textgen/seq2seq/data_reader.py
--rw-r--r--   0 xuming     (501) staff       (20)    19319 2022-08-25 03:06:56.000000 textgen-0.1.7/textgen/seq2seq/seq2seq_model.py
--rw-r--r--   0 xuming     (501) staff       (20)    10741 2022-06-15 12:49:21.000000 textgen-0.1.7/textgen/seq2seq/seq2seq_trainer.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.216496 textgen-0.1.7/textgen/t5/
--rwxr-xr-x   0 xuming     (501) staff       (20)      272 2022-08-23 06:18:39.000000 textgen-0.1.7/textgen/t5/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)    50493 2022-11-16 12:03:51.000000 textgen-0.1.7/textgen/t5/copyt5_model.py
--rw-r--r--   0 xuming     (501) staff       (20)     6917 2022-11-16 13:02:34.000000 textgen-0.1.7/textgen/t5/copyt5_utils.py
--rw-r--r--   0 xuming     (501) staff       (20)    50541 2022-11-16 12:03:51.000000 textgen-0.1.7/textgen/t5/t5_model.py
--rw-r--r--   0 xuming     (501) staff       (20)     7146 2022-11-17 02:54:45.000000 textgen-0.1.7/textgen/t5/t5_utils.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.220869 textgen-0.1.7/textgen/unsup_generation/
--rw-r--r--   0 xuming     (501) staff       (20)      246 2022-09-06 02:24:58.000000 textgen-0.1.7/textgen/unsup_generation/__init__.py
--rw-r--r--   0 xuming     (501) staff       (20)     3456 2022-09-26 07:01:36.000000 textgen-0.1.7/textgen/unsup_generation/tgls_model.py
--rw-r--r--   0 xuming     (501) staff       (20)    27678 2022-09-06 02:29:56.000000 textgen-0.1.7/textgen/unsup_generation/tgls_util.py
-drwxr-xr-x   0 xuming     (501) staff       (20)        0 2022-11-28 04:00:54.133352 textgen-0.1.7/textgen.egg-info/
--rw-r--r--   0 xuming     (501) staff       (20)    26535 2022-11-28 04:00:53.000000 textgen-0.1.7/textgen.egg-info/PKG-INFO
--rw-r--r--   0 xuming     (501) staff       (20)     1663 2022-11-28 04:00:53.000000 textgen-0.1.7/textgen.egg-info/SOURCES.txt
--rw-r--r--   0 xuming     (501) staff       (20)        1 2022-11-28 04:00:53.000000 textgen-0.1.7/textgen.egg-info/dependency_links.txt
--rw-r--r--   0 xuming     (501) staff       (20)      128 2022-11-28 04:00:53.000000 textgen-0.1.7/textgen.egg-info/requires.txt
--rw-r--r--   0 xuming     (501) staff       (20)        8 2022-11-28 04:00:53.000000 textgen-0.1.7/textgen.egg-info/top_level.txt
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.889828 textgen-0.1.8/
+-rw-r--r--   0 xuming     (501) staff       (20)    11357 2021-08-05 02:59:06.000000 textgen-0.1.8/LICENSE
+-rw-r--r--   0 xuming     (501) staff       (20)    26585 2023-04-07 09:20:39.890673 textgen-0.1.8/PKG-INFO
+-rw-r--r--   0 xuming     (501) staff       (20)    22208 2023-03-26 02:30:43.000000 textgen-0.1.8/README.md
+-rw-r--r--   0 xuming     (501) staff       (20)      309 2023-04-07 09:20:39.893100 textgen-0.1.8/setup.cfg
+-rw-r--r--   0 xuming     (501) staff       (20)     1395 2023-04-07 02:35:13.000000 textgen-0.1.8/setup.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.829813 textgen-0.1.8/textgen/
+-rw-r--r--   0 xuming     (501) staff       (20)     1288 2023-04-07 02:35:13.000000 textgen-0.1.8/textgen/__init__.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.839844 textgen-0.1.8/textgen/augment/
+-rw-r--r--   0 xuming     (501) staff       (20)      133 2022-06-30 07:59:18.000000 textgen-0.1.8/textgen/augment/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)     1493 2022-05-09 11:34:10.000000 textgen-0.1.8/textgen/augment/sentence_level_augment.py
+-rw-r--r--   0 xuming     (501) staff       (20)     3384 2022-09-26 07:08:57.000000 textgen-0.1.8/textgen/augment/text_augment.py
+-rw-r--r--   0 xuming     (501) staff       (20)     2256 2022-07-04 08:00:34.000000 textgen-0.1.8/textgen/augment/tokenizer.py
+-rw-r--r--   0 xuming     (501) staff       (20)     1971 2021-08-05 02:59:06.000000 textgen-0.1.8/textgen/augment/translate_api.py
+-rw-r--r--   0 xuming     (501) staff       (20)    13027 2022-09-26 07:39:41.000000 textgen-0.1.8/textgen/augment/word_level_augment.py
+-rw-r--r--   0 xuming     (501) staff       (20)     1240 2022-05-09 11:34:10.000000 textgen-0.1.8/textgen/augment/word_vocab.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.843073 textgen-0.1.8/textgen/chatglm/
+-rw-r--r--   0 xuming     (501) staff       (20)       80 2023-03-26 02:30:43.000000 textgen-0.1.8/textgen/chatglm/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)    26069 2023-04-07 08:08:24.000000 textgen-0.1.8/textgen/chatglm/chatglm_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     5884 2023-04-07 06:57:13.000000 textgen-0.1.8/textgen/chatglm/chatglm_utils.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.845533 textgen-0.1.8/textgen/config/
+-rw-r--r--   0 xuming     (501) staff       (20)      140 2021-08-05 02:59:06.000000 textgen-0.1.8/textgen/config/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)     1845 2022-06-30 03:18:51.000000 textgen-0.1.8/textgen/config/global_args.py
+-rw-r--r--   0 xuming     (501) staff       (20)    12292 2023-04-07 08:08:24.000000 textgen-0.1.8/textgen/config/model_args.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.847246 textgen-0.1.8/textgen/custom_models/
+-rwxr-xr-x   0 xuming     (501) staff       (20)        0 2021-08-05 02:59:06.000000 textgen-0.1.8/textgen/custom_models/__init__.py
+-rwxr-xr-x   0 xuming     (501) staff       (20)    32645 2022-08-24 03:27:39.000000 textgen-0.1.8/textgen/custom_models/models.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.850267 textgen-0.1.8/textgen/data/
+-rwxr-xr-x   0 xuming     (501) staff       (20)    48098 2019-08-25 14:57:21.000000 textgen-0.1.8/textgen/data/HowNetPOSWord.txt
+-rw-r--r--   0 xuming     (501) staff       (20)    17438 2021-10-25 11:27:11.000000 textgen-0.1.8/textgen/data/stopwords.txt
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.854199 textgen-0.1.8/textgen/language_generation/
+-rwxr-xr-x   0 xuming     (501) staff       (20)      292 2021-08-05 02:59:06.000000 textgen-0.1.8/textgen/language_generation/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)    10056 2022-07-05 07:48:33.000000 textgen-0.1.8/textgen/language_generation/language_generation_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     2829 2022-06-14 12:08:00.000000 textgen-0.1.8/textgen/language_generation/language_generation_utils.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.862985 textgen-0.1.8/textgen/language_modeling/
+-rwxr-xr-x   0 xuming     (501) staff       (20)      407 2022-09-10 06:38:25.000000 textgen-0.1.8/textgen/language_modeling/__init__.py
+-rwxr-xr-x   0 xuming     (501) staff       (20)    56833 2022-09-09 11:41:34.000000 textgen-0.1.8/textgen/language_modeling/language_modeling_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     8938 2022-06-14 12:08:00.000000 textgen-0.1.8/textgen/language_modeling/language_modeling_utils.py
+-rw-r--r--   0 xuming     (501) staff       (20)    65595 2022-11-27 05:36:55.000000 textgen-0.1.8/textgen/language_modeling/songnet_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)    17103 2022-12-05 07:28:16.000000 textgen-0.1.8/textgen/language_modeling/songnet_utils.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.873459 textgen-0.1.8/textgen/seq2seq/
+-rwxr-xr-x   0 xuming     (501) staff       (20)      313 2022-08-07 03:00:11.000000 textgen-0.1.8/textgen/seq2seq/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)    73298 2022-09-09 11:41:34.000000 textgen-0.1.8/textgen/seq2seq/bart_seq2seq_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)    18559 2022-06-19 09:29:30.000000 textgen-0.1.8/textgen/seq2seq/bart_seq2seq_utils.py
+-rw-r--r--   0 xuming     (501) staff       (20)    23456 2022-08-25 03:06:56.000000 textgen-0.1.8/textgen/seq2seq/conv_seq2seq_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     4345 2022-05-10 10:48:02.000000 textgen-0.1.8/textgen/seq2seq/data_reader.py
+-rw-r--r--   0 xuming     (501) staff       (20)    19319 2022-08-25 03:06:56.000000 textgen-0.1.8/textgen/seq2seq/seq2seq_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)    10741 2022-06-15 12:49:21.000000 textgen-0.1.8/textgen/seq2seq/seq2seq_trainer.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.881625 textgen-0.1.8/textgen/t5/
+-rwxr-xr-x   0 xuming     (501) staff       (20)      272 2022-08-23 06:18:39.000000 textgen-0.1.8/textgen/t5/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)    50493 2022-11-16 12:03:51.000000 textgen-0.1.8/textgen/t5/copyt5_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     6917 2022-11-16 13:02:34.000000 textgen-0.1.8/textgen/t5/copyt5_utils.py
+-rw-r--r--   0 xuming     (501) staff       (20)    50541 2023-02-16 08:10:32.000000 textgen-0.1.8/textgen/t5/t5_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)     7146 2022-11-17 02:54:45.000000 textgen-0.1.8/textgen/t5/t5_utils.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.888068 textgen-0.1.8/textgen/unsup_generation/
+-rw-r--r--   0 xuming     (501) staff       (20)      246 2022-09-06 02:24:58.000000 textgen-0.1.8/textgen/unsup_generation/__init__.py
+-rw-r--r--   0 xuming     (501) staff       (20)     3456 2022-09-26 07:01:36.000000 textgen-0.1.8/textgen/unsup_generation/tgls_model.py
+-rw-r--r--   0 xuming     (501) staff       (20)    27678 2022-09-06 02:29:56.000000 textgen-0.1.8/textgen/unsup_generation/tgls_util.py
+drwxr-xr-x   0 xuming     (501) staff       (20)        0 2023-04-07 09:20:39.833383 textgen-0.1.8/textgen.egg-info/
+-rw-r--r--   0 xuming     (501) staff       (20)    26585 2023-04-07 09:20:39.000000 textgen-0.1.8/textgen.egg-info/PKG-INFO
+-rw-r--r--   0 xuming     (501) staff       (20)     1608 2023-04-07 09:20:39.000000 textgen-0.1.8/textgen.egg-info/SOURCES.txt
+-rw-r--r--   0 xuming     (501) staff       (20)        1 2023-04-07 09:20:39.000000 textgen-0.1.8/textgen.egg-info/dependency_links.txt
+-rw-r--r--   0 xuming     (501) staff       (20)      145 2023-04-07 09:20:39.000000 textgen-0.1.8/textgen.egg-info/requires.txt
+-rw-r--r--   0 xuming     (501) staff       (20)        8 2023-04-07 09:20:39.000000 textgen-0.1.8/textgen.egg-info/top_level.txt
```

### Comparing `textgen-0.1.7/LICENSE` & `textgen-0.1.8/LICENSE`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/PKG-INFO` & `textgen-0.1.8/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: textgen
-Version: 0.1.7
+Version: 0.1.8
 Summary: Text Generation Model
 Home-page: https://github.com/shibing624/textgen
 Author: XuMing
 Author-email: xuming624@qq.com
 License: Apache 2.0
 Description: [![PyPI version](https://badge.fury.io/py/textgen.svg)](https://badge.fury.io/py/textgen)
         [![Downloads](https://pepy.tech/badge/textgen)](https://pepy.tech/project/textgen)
@@ -19,56 +19,62 @@
         
         🌈 Implementation of Text Generation models.
         
         **textgen**实现了多种文本生成模型，包括：UDA、GPT2、Seq2Seq、BART、T5、SongNet等模型，开箱即用。
         
         **Guide**
         
-        - [Question](#Question)
-        - [Solution](#Solution)
         - [Feature](#Feature)
         - [Install](#install)
         - [Usage](#usage)
         - [Contact](#Contact)
         - [Reference](#reference)
         
-        # Question
-        
-        文本生成，文本数据增强怎么做？
-        
-        # Solution
-        ## 文本生成模型
+        # Feature
+        ## 文本生成
         
-        1. Seq2Seq、ConvSeq2Seq、BART
-        2. GPT2、SongNet
-        3. T5、CopyT5
+        1. seq2seq: Seq2Seq、ConvSeq2Seq、BART
+        2. language_modeling: GPT2、SongNet
+        3. t5: T5、CopyT5
+        4. question_answering: BERT、XLNet
+        5. chatglm: ChatGLM
         
         ## 文本扩增
         ### 词粒度扩增
         1. UDA，非核心词替换
         2. EDA，简单数据增强技术：相似词、同义词替换，随机词插入、删除、替换
         
         ### 句粒度扩增
         1. 回译（BT, Back Translate）：中文-英文-中文
         2. GPT2模型续写：短文本->长文本
         3. BART摘要模型：长文本->短文本
         4. TGLS：无监督相似文本生成模型
         
-        
-        # Feature
-        
+        ## 功能列表
         - [UDA(非核心词替换)/EDA](textgen/augment/word_level_augment.py)：本项目参考Google的UDA(非核心词替换)算法和EDA算法，基于TF-IDF将句子中部分不重要词替换为同义词，随机词插入、删除、替换等方法，产生新的文本，实现了文本扩增
         - [BT(回译)](textgen/augment/sentence_level_augment.py)：本项目基于百度翻译API实现了回译功能，先把中文句子翻译为英文，再把英文翻译为新的中文
         - [Seq2Seq](textgen/seq2seq)：本项目基于PyTorch实现了Seq2Seq、ConvSeq2Seq、BART模型的训练和预测，可以用于文本翻译、对话生成、摘要生成等文本生成任务
         - [T5](textgen/t5)：本项目基于PyTorch实现了T5和CopyT5模型训练和预测，可以用于文本翻译、对话生成、对联生成、文案撰写等文本生成任务
         - [GPT2](textgen/language_modeling)：本项目基于PyTorch实现了GTP2模型训练和预测，可以用于文章生成、对联生成等文本生成任务
         - [SongNet](textgen/language_modeling/songnet_model.py)：本项目基于PyTorch实现了SongNet模型训练和预测，可以用于规范格式的诗词、歌词等文本生成任务
         - [TGLS](textgen/unsup_generation)：本项目实现了[TGLS](https://www.jiqizhixin.com/articles/2020-08-11-5)无监督相似文本生成模型，是一种“先搜索后学习”的文本生成方法，通过反复迭代学习候选集，最终模型能生成类似候选集的高质量相似文本
         
         
+        ## Release Models
+        release基于`textgen`训练的中文模型，模型已经release到HuggingFace models，指定模型名称`textgen`会自动下载模型，可直接使用。
+        
+        |Model|Arch|Intro|Training|Inference|
+        |:-- |:--- |:--- |:--- |:--- |
+        |[shibing624/prompt-t5-base-chinese](https://huggingface.co/shibing624/prompt-t5-base-chinese)|T5|中文NLP多任务Prompt模型|[prompt-t5-base-chinese.md](https://github.com/shibing624/textgen/blob/main/docs/prompt-t5-base-chinese.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_prompt_demo.py)|
+        |[shibing624/t5-chinese-couplet](https://huggingface.co/shibing624/t5-chinese-couplet)|T5|fine-tuned中文对联后的模型|[对联生成模型调研](https://github.com/shibing624/textgen/blob/main/docs/%E5%AF%B9%E8%81%94%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%AF%94.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_couplet_demo.py)|
+        |[shibing624/songnet-base-chinese](https://huggingface.co/shibing624/songnet-base-chinese)|SongNet|SongNet预训练模型|-|-|
+        |[shibing624/songnet-base-chinese-songci](https://huggingface.co/shibing624/songnet-base-chinese-songci)|SongNet|fine-tuned宋词后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_songci_demo.py)|
+        |[shibing624/songnet-base-chinese-couplet](https://huggingface.co/shibing624/songnet-base-chinese-couplet)|SongNet|fine-tuned对联后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_couplet_demo.py)|
+        
+        
         # Demo
         
         HuggingFace Demo: https://huggingface.co/spaces/shibing624/chinese-couplet-generate
         
         ![](docs/hf.png)
         
         run example: [examples/gradio_demo.py](examples/gradio_demo.py) to see the demo:
@@ -260,22 +266,14 @@
         output:
         ```shell
         inputs: ['什么是ai', '你是什么类型的计算机', '你知道热力学吗']
         outputs: ['人工智能有两个广义的定义,任何拟人的机械,如在卡雷尔capeks', '我的程序运行在Python,所以我在任何电脑上工作!', '什么是热力学']
         ```
         
         
-        ### T5 模型应用
-        
-        release基于T5的fine-tuned后的中文模型，模型全部release到HuggingFace models，`textgen`可自动下载，可直接使用。
-        
-        |Model|Arch|Intro|Training|Inference|
-        |:-- |:--- |:--- |:--- |:--- |
-        |[shibing624/prompt-t5-base-chinese](https://huggingface.co/shibing624/prompt-t5-base-chinese)|T5|中文NLP多任务Prompt模型|[prompt-t5-base-chinese.md](https://github.com/shibing624/textgen/blob/main/docs/prompt-t5-base-chinese.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_prompt_demo.py)|
-        |[shibing624/t5-chinese-couplet](https://huggingface.co/shibing624/t5-chinese-couplet)|T5|fine-tuned中文对联后的模型|[对联生成模型调研](https://github.com/shibing624/textgen/blob/main/docs/%E5%AF%B9%E8%81%94%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%AF%94.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_couplet_demo.py)|
         
         
         ## GPT2 模型
         
         ### 中文GPT2 - 文章生成
         
         使用中文数据集（段落格式，`\n`间隔），训练GPT2模型，可以用于诗歌生成、文章生成等任务。
@@ -300,23 +298,14 @@
         ## SongNet 模型
         
         格式控制的文本生成模型，paper见[SongNet: Rigid Formats Controlled Text Generation](https://arxiv.org/abs/2004.08022)，
         适用于强韵律格式要求的诗歌、对联、歌词生成等任务。
         
         example: [examples/language_generation/training_zh_songnet_demo.py](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)
         
-        ### SongNet 模型应用
-        
-        release基于SongNet的中文模型，模型全部release到HuggingFace models，`textgen`可自动下载，可直接使用。
-        
-        |Model|Arch|Intro|Training|Inference|
-        |:-- |:--- |:--- |:--- |:--- |
-        |[shibing624/songnet-base-chinese](https://huggingface.co/shibing624/songnet-base-chinese)|SongNet|SongNet预训练模型|-|-|
-        |[shibing624/songnet-base-chinese-songci](https://huggingface.co/shibing624/songnet-base-chinese-songci)|SongNet|fine-tuned宋词后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_songci_demo.py)|
-        |[shibing624/songnet-base-chinese-couplet](https://huggingface.co/shibing624/songnet-base-chinese-couplet)|SongNet|fine-tuned对联后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_couplet_demo.py)|
         
         
         ## Keyword Text Augmentation(EDA/UDA)
         
         example: [examples/text_augmentation_demo.py](examples/text_augmentation_demo.py)
         
         ```python
@@ -434,14 +423,28 @@
         - Issue(建议)
           ：[![GitHub issues](https://img.shields.io/github/issues/shibing624/textgen.svg)](https://github.com/shibing624/textgen/issues)
         - 邮件我：xuming: xuming624@qq.com
         - 微信我： 加我*微信号：xuming624, 备注：姓名-公司名-NLP* 进NLP交流群。
         
         <img src="docs/wechat.jpeg" width="200" />
         
+        
+        # Citation
+        
+        如果你在研究中使用了textgen，请按如下格式引用：
+        
+        ```latex
+        @misc{textgen,
+          title={textgen: Text Generation Tool},
+          author={Xu Ming},
+          year={2021},
+          howpublished={\url{https://github.com/shibing624/textgen}},
+        }
+        ```
+        
         # License
         
         授权协议为 [The Apache License 2.0](/LICENSE)，可免费用做商业用途。请在产品说明中附加textgen的链接和授权协议。
         
         # Contribute
         
         项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：
```

### Comparing `textgen-0.1.7/README.md` & `textgen-0.1.8/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -11,56 +11,62 @@
 
 🌈 Implementation of Text Generation models.
 
 **textgen**实现了多种文本生成模型，包括：UDA、GPT2、Seq2Seq、BART、T5、SongNet等模型，开箱即用。
 
 **Guide**
 
-- [Question](#Question)
-- [Solution](#Solution)
 - [Feature](#Feature)
 - [Install](#install)
 - [Usage](#usage)
 - [Contact](#Contact)
 - [Reference](#reference)
 
-# Question
-
-文本生成，文本数据增强怎么做？
-
-# Solution
-## 文本生成模型
+# Feature
+## 文本生成
 
-1. Seq2Seq、ConvSeq2Seq、BART
-2. GPT2、SongNet
-3. T5、CopyT5
+1. seq2seq: Seq2Seq、ConvSeq2Seq、BART
+2. language_modeling: GPT2、SongNet
+3. t5: T5、CopyT5
+4. question_answering: BERT、XLNet
+5. chatglm: ChatGLM
 
 ## 文本扩增
 ### 词粒度扩增
 1. UDA，非核心词替换
 2. EDA，简单数据增强技术：相似词、同义词替换，随机词插入、删除、替换
 
 ### 句粒度扩增
 1. 回译（BT, Back Translate）：中文-英文-中文
 2. GPT2模型续写：短文本->长文本
 3. BART摘要模型：长文本->短文本
 4. TGLS：无监督相似文本生成模型
 
-
-# Feature
-
+## 功能列表
 - [UDA(非核心词替换)/EDA](textgen/augment/word_level_augment.py)：本项目参考Google的UDA(非核心词替换)算法和EDA算法，基于TF-IDF将句子中部分不重要词替换为同义词，随机词插入、删除、替换等方法，产生新的文本，实现了文本扩增
 - [BT(回译)](textgen/augment/sentence_level_augment.py)：本项目基于百度翻译API实现了回译功能，先把中文句子翻译为英文，再把英文翻译为新的中文
 - [Seq2Seq](textgen/seq2seq)：本项目基于PyTorch实现了Seq2Seq、ConvSeq2Seq、BART模型的训练和预测，可以用于文本翻译、对话生成、摘要生成等文本生成任务
 - [T5](textgen/t5)：本项目基于PyTorch实现了T5和CopyT5模型训练和预测，可以用于文本翻译、对话生成、对联生成、文案撰写等文本生成任务
 - [GPT2](textgen/language_modeling)：本项目基于PyTorch实现了GTP2模型训练和预测，可以用于文章生成、对联生成等文本生成任务
 - [SongNet](textgen/language_modeling/songnet_model.py)：本项目基于PyTorch实现了SongNet模型训练和预测，可以用于规范格式的诗词、歌词等文本生成任务
 - [TGLS](textgen/unsup_generation)：本项目实现了[TGLS](https://www.jiqizhixin.com/articles/2020-08-11-5)无监督相似文本生成模型，是一种“先搜索后学习”的文本生成方法，通过反复迭代学习候选集，最终模型能生成类似候选集的高质量相似文本
 
 
+## Release Models
+release基于`textgen`训练的中文模型，模型已经release到HuggingFace models，指定模型名称`textgen`会自动下载模型，可直接使用。
+
+|Model|Arch|Intro|Training|Inference|
+|:-- |:--- |:--- |:--- |:--- |
+|[shibing624/prompt-t5-base-chinese](https://huggingface.co/shibing624/prompt-t5-base-chinese)|T5|中文NLP多任务Prompt模型|[prompt-t5-base-chinese.md](https://github.com/shibing624/textgen/blob/main/docs/prompt-t5-base-chinese.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_prompt_demo.py)|
+|[shibing624/t5-chinese-couplet](https://huggingface.co/shibing624/t5-chinese-couplet)|T5|fine-tuned中文对联后的模型|[对联生成模型调研](https://github.com/shibing624/textgen/blob/main/docs/%E5%AF%B9%E8%81%94%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%AF%94.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_couplet_demo.py)|
+|[shibing624/songnet-base-chinese](https://huggingface.co/shibing624/songnet-base-chinese)|SongNet|SongNet预训练模型|-|-|
+|[shibing624/songnet-base-chinese-songci](https://huggingface.co/shibing624/songnet-base-chinese-songci)|SongNet|fine-tuned宋词后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_songci_demo.py)|
+|[shibing624/songnet-base-chinese-couplet](https://huggingface.co/shibing624/songnet-base-chinese-couplet)|SongNet|fine-tuned对联后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_couplet_demo.py)|
+
+
 # Demo
 
 HuggingFace Demo: https://huggingface.co/spaces/shibing624/chinese-couplet-generate
 
 ![](docs/hf.png)
 
 run example: [examples/gradio_demo.py](examples/gradio_demo.py) to see the demo:
@@ -252,22 +258,14 @@
 output:
 ```shell
 inputs: ['什么是ai', '你是什么类型的计算机', '你知道热力学吗']
 outputs: ['人工智能有两个广义的定义,任何拟人的机械,如在卡雷尔capeks', '我的程序运行在Python,所以我在任何电脑上工作!', '什么是热力学']
 ```
 
 
-### T5 模型应用
-
-release基于T5的fine-tuned后的中文模型，模型全部release到HuggingFace models，`textgen`可自动下载，可直接使用。
-
-|Model|Arch|Intro|Training|Inference|
-|:-- |:--- |:--- |:--- |:--- |
-|[shibing624/prompt-t5-base-chinese](https://huggingface.co/shibing624/prompt-t5-base-chinese)|T5|中文NLP多任务Prompt模型|[prompt-t5-base-chinese.md](https://github.com/shibing624/textgen/blob/main/docs/prompt-t5-base-chinese.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_prompt_demo.py)|
-|[shibing624/t5-chinese-couplet](https://huggingface.co/shibing624/t5-chinese-couplet)|T5|fine-tuned中文对联后的模型|[对联生成模型调研](https://github.com/shibing624/textgen/blob/main/docs/%E5%AF%B9%E8%81%94%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%AF%94.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_couplet_demo.py)|
 
 
 ## GPT2 模型
 
 ### 中文GPT2 - 文章生成
 
 使用中文数据集（段落格式，`\n`间隔），训练GPT2模型，可以用于诗歌生成、文章生成等任务。
@@ -292,23 +290,14 @@
 ## SongNet 模型
 
 格式控制的文本生成模型，paper见[SongNet: Rigid Formats Controlled Text Generation](https://arxiv.org/abs/2004.08022)，
 适用于强韵律格式要求的诗歌、对联、歌词生成等任务。
 
 example: [examples/language_generation/training_zh_songnet_demo.py](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)
 
-### SongNet 模型应用
-
-release基于SongNet的中文模型，模型全部release到HuggingFace models，`textgen`可自动下载，可直接使用。
-
-|Model|Arch|Intro|Training|Inference|
-|:-- |:--- |:--- |:--- |:--- |
-|[shibing624/songnet-base-chinese](https://huggingface.co/shibing624/songnet-base-chinese)|SongNet|SongNet预训练模型|-|-|
-|[shibing624/songnet-base-chinese-songci](https://huggingface.co/shibing624/songnet-base-chinese-songci)|SongNet|fine-tuned宋词后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_songci_demo.py)|
-|[shibing624/songnet-base-chinese-couplet](https://huggingface.co/shibing624/songnet-base-chinese-couplet)|SongNet|fine-tuned对联后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_couplet_demo.py)|
 
 
 ## Keyword Text Augmentation(EDA/UDA)
 
 example: [examples/text_augmentation_demo.py](examples/text_augmentation_demo.py)
 
 ```python
@@ -426,14 +415,28 @@
 - Issue(建议)
   ：[![GitHub issues](https://img.shields.io/github/issues/shibing624/textgen.svg)](https://github.com/shibing624/textgen/issues)
 - 邮件我：xuming: xuming624@qq.com
 - 微信我： 加我*微信号：xuming624, 备注：姓名-公司名-NLP* 进NLP交流群。
 
 <img src="docs/wechat.jpeg" width="200" />
 
+
+# Citation
+
+如果你在研究中使用了textgen，请按如下格式引用：
+
+```latex
+@misc{textgen,
+  title={textgen: Text Generation Tool},
+  author={Xu Ming},
+  year={2021},
+  howpublished={\url{https://github.com/shibing624/textgen}},
+}
+```
+
 # License
 
 授权协议为 [The Apache License 2.0](/LICENSE)，可免费用做商业用途。请在产品说明中附加textgen的链接和授权协议。
 
 # Contribute
 
 项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：
```

### Comparing `textgen-0.1.7/setup.py` & `textgen-0.1.8/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from setuptools import setup, find_packages
 
 with open('README.md', 'r', encoding='utf-8') as f:
     readme = f.read()
 
 setup(
     name='textgen',
-    version='0.1.7',
+    version='0.1.8',
     description='Text Generation Model',
     long_description=readme,
     long_description_content_type='text/markdown',
     author='XuMing',
     author_email='xuming624@qq.com',
     url='https://github.com/shibing624/textgen',
     license="Apache 2.0",
@@ -34,14 +34,16 @@
         'text2vec',
         'tensorboard',
         'tqdm>=4.47.0',
         'pandas',
         'wandb>=0.10.32',
         'sacremoses',
         'Rouge',
+        'cpm_kernels',
+        'peft',
     ],
     packages=find_packages(exclude=['tests']),
     package_dir={'textgen': 'textgen'},
     package_data={
         'textgen': ['*.*', 'data/*'],
     }
 )
```

### Comparing `textgen-0.1.7/textgen/__init__.py` & `textgen-0.1.8/textgen/__init__.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,33 +1,36 @@
 # -*- coding: utf-8 -*-
 """
 @author:XuMing(xuming624@qq.com)
 @description: 
 """
 
-__version__ = '0.1.7'
+__version__ = '0.1.8'
 
 from textgen.augment.text_augment import TextAugment
 
 from textgen.config.model_args import LanguageGenerationArgs
 from textgen.language_generation.language_generation_model import LanguageGenerationModel
 
 from textgen.config.model_args import LanguageModelingArgs
 from textgen.language_modeling.language_modeling_model import LanguageModelingModel
+
 from textgen.config.model_args import SongNetArgs
 from textgen.language_modeling.songnet_model import SongNetModel
 from textgen.language_modeling.songnet_utils import SongNetTokenizer, snapshot_download
 
-from textgen.config.model_args import QuestionAnsweringArgs
-from textgen.question_answering.question_answering_model import QuestionAnsweringModel
-
 from textgen.config.model_args import Seq2SeqArgs
-from textgen.seq2seq.bart_seq2seq_model import BartSeq2SeqModel
 from textgen.seq2seq.seq2seq_model import Seq2SeqModel
 from textgen.seq2seq.conv_seq2seq_model import ConvSeq2SeqModel
+from textgen.seq2seq.bart_seq2seq_model import BartSeq2SeqModel
 
-from textgen.config.model_args import T5Args, CopyT5Args
+from textgen.config.model_args import T5Args
 from textgen.t5.t5_model import T5Model
+
+from textgen.config.model_args import CopyT5Args
 from textgen.t5.copyt5_model import CopyT5Model
 from textgen.t5.copyt5_utils import ZHTokenizer
 
 from textgen.unsup_generation.tgls_model import TglsModel
+
+from textgen.chatglm.chatglm_model import ChatGlmModel
+from textgen.config.model_args import ChatGlmArgs
```

### Comparing `textgen-0.1.7/textgen/augment/sentence_level_augment.py` & `textgen-0.1.8/textgen/augment/sentence_level_augment.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/augment/text_augment.py` & `textgen-0.1.8/textgen/augment/text_augment.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/augment/tokenizer.py` & `textgen-0.1.8/textgen/augment/tokenizer.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/augment/translate_api.py` & `textgen-0.1.8/textgen/augment/translate_api.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/augment/word_level_augment.py` & `textgen-0.1.8/textgen/augment/word_level_augment.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/augment/word_vocab.py` & `textgen-0.1.8/textgen/augment/word_vocab.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/config/global_args.py` & `textgen-0.1.8/textgen/config/global_args.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/config/model_args.py` & `textgen-0.1.8/textgen/config/model_args.py`

 * *Files 11% similar despite different names*

```diff
@@ -2,18 +2,18 @@
 """
 @author:XuMing(xuming624@qq.com)
 @description: refer https://github.com/ThilinaRajapakse/simpletransformers
 """
 import json
 import os
 import sys
-import warnings
+from loguru import logger
 from dataclasses import asdict, dataclass, field
 from multiprocessing import cpu_count
-
+from typing import Optional
 from torch.utils.data import Dataset
 
 
 def get_default_process_count():
     process_count = cpu_count() - 2 if cpu_count() > 2 else 1
     if sys.platform == "win32":
         process_count = min(process_count, 61)
@@ -114,49 +114,38 @@
 
     def get_args_for_saving(self):
         args_for_saving = {key: value for key, value in asdict(self).items() if key not in self.not_saved_args}
         return args_for_saving
 
     def save(self, output_dir):
         os.makedirs(output_dir, exist_ok=True)
-        with open(os.path.join(output_dir, "model_args.json"), "w") as f:
+        with open(os.path.join(output_dir, "model_args.json"), "w", encoding='utf-8') as f:
             args_dict = self.get_args_for_saving()
+            if args_dict['dataset_class'] is not None and not isinstance(args_dict["dataset_class"], str):
+                args_dict['dataset_class'] = type(args_dict['dataset_class']).__name__
             if args_dict["tokenizer_type"] is not None and not isinstance(args_dict["tokenizer_type"], str):
                 args_dict["tokenizer_type"] = type(args_dict["tokenizer_type"]).__name__
             json.dump(args_dict, f)
 
     def load(self, input_dir):
         if input_dir:
             model_args_file = os.path.join(input_dir, "model_args.json")
             if os.path.isfile(model_args_file):
-                with open(model_args_file, "r") as f:
+                with open(model_args_file, "r", encoding='utf-8') as f:
                     model_args = json.load(f)
-
+                if model_args["dataset_class"]:
+                    logger.warning(
+                        "This model was trained using a custom dataset_class."
+                        "This cannot be loaded automatically and must be specified in the model args"
+                        "when loading the model."
+                    )
                 self.update_from_dict(model_args)
 
 
 @dataclass
-class QuestionAnsweringArgs(ModelArgs):
-    """
-    Model args for a QuestionAnsweringModel
-    """
-
-    model_class: str = "QuestionAnsweringModel"
-    doc_stride: int = 384
-    early_stopping_metric: str = "correct"
-    early_stopping_metric_minimize: bool = False
-    lazy_loading: bool = False
-    max_answer_length: int = 100
-    max_query_length: int = 64
-    n_best_size: int = 20
-    null_score_diff_threshold: float = 0.0
-    special_tokens_list: list = field(default_factory=list)
-
-
-@dataclass
 class T5Args(ModelArgs):
     """
     Model args for a T5Model
     """
 
     model_class: str = "T5Model"
     dataset_class: Dataset = None
@@ -238,37 +227,14 @@
     vocab_size: int = None
     clean_text: bool = True
     handle_chinese_chars: bool = True
     special_tokens_list: list = field(default_factory=list)
     strip_accents: bool = True
     local_rank: int = -1
 
-    def save(self, output_dir):
-        os.makedirs(output_dir, exist_ok=True)
-        with open(os.path.join(output_dir, "model_args.json"), "w") as f:
-            args_dict = self.get_args_for_saving()
-            if args_dict["dataset_class"] is not None:
-                args_dict["dataset_class"] = type(args_dict["dataset_class"]).__name__
-            # json.dump(self.get_args_for_saving(), f)
-            json.dump(args_dict, f)
-
-    def load(self, input_dir):
-        if input_dir:
-            model_args_file = os.path.join(input_dir, "model_args.json")
-            if os.path.isfile(model_args_file):
-                with open(model_args_file, "r") as f:
-                    model_args = json.load(f)
-                if model_args["dataset_class"]:
-                    warnings.warn(
-                        "This model was trained using a custom dataset_class."
-                        "This cannot be loaded automatically and must be specified in the model args"
-                        "when loading the model."
-                    )
-                self.update_from_dict(model_args)
-
 
 @dataclass
 class Seq2SeqArgs(ModelArgs):
     """
     Model args for a Seq2SeqModel
     """
 
@@ -293,36 +259,14 @@
     save_knowledge_dataset: bool = True
     save_knowledge_dataset_with_checkpoints: bool = False
     split_text_character: str = " "
     split_text_n: int = 100
     src_lang: str = "en_XX"
     tgt_lang: str = "ro_RO"
 
-    def save(self, output_dir):
-        os.makedirs(output_dir, exist_ok=True)
-        with open(os.path.join(output_dir, "model_args.json"), "w") as f:
-            args_dict = self.get_args_for_saving()
-            if args_dict["dataset_class"] is not None:
-                args_dict["dataset_class"] = type(args_dict["dataset_class"]).__name__
-            json.dump(args_dict, f)
-
-    def load(self, input_dir):
-        if input_dir:
-            model_args_file = os.path.join(input_dir, "model_args.json")
-            if os.path.isfile(model_args_file):
-                with open(model_args_file, "r") as f:
-                    model_args = json.load(f)
-                if model_args["dataset_class"]:
-                    warnings.warn(
-                        "This model was trained using a custom dataset_class."
-                        "This cannot be loaded automatically and must be specified in the model args"
-                        "when loading the model."
-                    )
-                self.update_from_dict(model_args)
-
 
 @dataclass
 class LanguageGenerationArgs(ModelArgs):
     """
     Model args for a LanguageGenerationModel
     """
 
@@ -381,7 +325,53 @@
     ff_embed_dim: int = 3072
     num_heads: int = 12
     num_layers: int = 12
     dropout: float = 0.2
     warmup_ratio: float = 0.05
     weight_decay: float = 0.0
     smoothing_factor: float = 0.1
+
+
+@dataclass
+class ChatGlmArgs(ModelArgs):
+    """
+    Model args for a ChatGLMModel
+    """
+
+    model_class: str = "ChatGlmArgs"
+    dataset_class: Dataset = None
+    fp16: bool = True
+    int8: bool = False
+    quantization_bit:int = None  # if use quantization bit, set 4, else None
+    debug: bool = False
+    max_seq_length: int = 256  # max length of input sequence
+    max_length = 384  # max length of the sequence to be generated
+    do_sample: bool = True
+    early_stopping: bool = True
+    evaluate_generated_text: bool = False
+    length_penalty: float = 2.0
+    num_beams: int = 1
+    num_return_sequences: int = 1
+    repetition_penalty: float = 1.0
+    temperature: float = 0.95
+    special_tokens_list: list = field(default_factory=list)
+    top_k: float = None
+    top_p: float = 0.7
+    model_name_or_path: Optional[str] = field(default="THUDM/chatglm-6b")
+    dataset_name_or_path: Optional[str] = field(default="shibing624/alpaca-zh")
+    use_lora: bool = True
+    lora_name: str = field(default="adapter_model.bin")
+    lora_rank: int = field(default=8)
+    lora_alpha = 32
+    lora_dropout = 0.1
+    lora_target_modules = ["query_key_value"]
+    lora_bias = "none"
+    only_lora_state_dict: bool = False
+    num_train_epochs = 1
+    max_steps = -1
+    per_device_train_batch_size = 2
+    gradient_accumulation_steps = 1
+    save_total_limit = 2
+    remove_unused_columns = False
+    logging_steps = 50
+    resume_from_checkpoint:str = None
+
```

### Comparing `textgen-0.1.7/textgen/custom_models/models.py` & `textgen-0.1.8/textgen/custom_models/models.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/data/HowNetPOSWord.txt` & `textgen-0.1.8/textgen/data/HowNetPOSWord.txt`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/data/stopwords.txt` & `textgen-0.1.8/textgen/data/stopwords.txt`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/language_generation/language_generation_model.py` & `textgen-0.1.8/textgen/language_generation/language_generation_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/language_generation/language_generation_utils.py` & `textgen-0.1.8/textgen/language_generation/language_generation_utils.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/language_modeling/language_modeling_model.py` & `textgen-0.1.8/textgen/language_modeling/language_modeling_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/language_modeling/language_modeling_utils.py` & `textgen-0.1.8/textgen/language_modeling/language_modeling_utils.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/language_modeling/songnet_model.py` & `textgen-0.1.8/textgen/language_modeling/songnet_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/language_modeling/songnet_utils.py` & `textgen-0.1.8/textgen/language_modeling/songnet_utils.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/question_answering/question_answering_model.py` & `textgen-0.1.8/textgen/t5/t5_model.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,407 +1,201 @@
 # -*- coding: utf-8 -*-
 """
 @author:XuMing(xuming624@qq.com)
 @description: refer https://github.com/ThilinaRajapakse/simpletransformers
 """
 
-import json
-import logging
 import math
 import os
 import random
 import warnings
 from dataclasses import asdict
-from multiprocessing import cpu_count
+from multiprocessing import Pool
 
 import numpy as np
 import pandas as pd
 import torch
-from scipy.stats import pearsonr
-from sklearn.metrics import (
-    confusion_matrix,
-    label_ranking_average_precision_score,
-    matthews_corrcoef,
-    mean_squared_error,
-)
+from loguru import logger
+from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
 from torch.utils.tensorboard import SummaryWriter
-from torch.utils.data import DataLoader, RandomSampler, SequentialSampler, TensorDataset
-from torch.utils.data.distributed import DistributedSampler
 from tqdm.auto import tqdm, trange
+from transformers import ByT5Tokenizer
+from transformers import MT5Config, MT5ForConditionalGeneration
+from transformers import T5Config, T5ForConditionalGeneration, T5Tokenizer
+from transformers.optimization import AdamW, Adafactor
 from transformers.optimization import (
     get_constant_schedule,
     get_constant_schedule_with_warmup,
     get_linear_schedule_with_warmup,
     get_cosine_schedule_with_warmup,
     get_cosine_with_hard_restarts_schedule_with_warmup,
     get_polynomial_decay_schedule_with_warmup,
 )
-from transformers.optimization import AdamW, Adafactor
-from transformers import (
-    AlbertConfig,
-    AlbertForQuestionAnswering,
-    AlbertTokenizer,
-    AutoConfig,
-    AutoModelForQuestionAnswering,
-    AutoTokenizer,
-    BartConfig,
-    BartForQuestionAnswering,
-    BartTokenizer,
-    BertConfig,
-    BertForQuestionAnswering,
-    BertTokenizer,
-    CamembertConfig,
-    CamembertForQuestionAnswering,
-    CamembertTokenizer,
-    DistilBertConfig,
-    DistilBertForQuestionAnswering,
-    DistilBertTokenizer,
-    ElectraConfig,
-    ElectraTokenizer,
-    LongformerConfig,
-    LongformerForQuestionAnswering,
-    LongformerTokenizer,
-    MPNetConfig,
-    MPNetForQuestionAnswering,
-    MPNetTokenizer,
-    MobileBertConfig,
-    MobileBertForQuestionAnswering,
-    MobileBertTokenizer,
-    RobertaConfig,
-    RobertaForQuestionAnswering,
-    RobertaTokenizer,
-    SqueezeBertConfig,
-    SqueezeBertForQuestionAnswering,
-    SqueezeBertTokenizer,
-    WEIGHTS_NAME,
-    XLMConfig,
-    XLMForQuestionAnswering,
-    XLMRobertaConfig,
-    XLMRobertaTokenizer,
-    XLMTokenizer,
-    XLNetConfig,
-    XLNetForQuestionAnswering,
-    XLNetTokenizer,
-)
 
-from textgen.config.model_args import QuestionAnsweringArgs
-from textgen.custom_models.models import ElectraForQuestionAnswering, XLMRobertaForQuestionAnswering
-from textgen.question_answering.question_answering_utils import (
-    LazyQuestionAnsweringDataset,
-    RawResult,
-    RawResultExtended,
-    build_examples,
-    get_best_predictions,
-    get_best_predictions_extended,
-    get_examples,
-    load_hf_dataset,
-    squad_convert_examples_to_features,
-    to_list,
-    write_predictions,
-    write_predictions_extended,
-)
-from loguru import logger
+from textgen.config.model_args import T5Args
+from textgen.t5.t5_utils import T5Dataset, load_hf_dataset
 
 try:
     import wandb
 
     wandb_available = True
 except ImportError:
     wandb_available = False
 
 has_cuda = torch.cuda.is_available()
 os.environ["TOKENIZERS_PARALLELISM"] = "FALSE"
 os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
 
 
-class QuestionAnsweringModel:
+def chunks(lst, n):
+    """Yield successive n-sized chunks from lst."""
+    for i in range(0, len(lst), n):
+        yield lst[i: i + n]
+
+
+MODEL_CLASSES = {
+    "t5": (T5Config, T5ForConditionalGeneration),
+    "mt5": (MT5Config, MT5ForConditionalGeneration),
+    "byt5": (T5Config, T5ForConditionalGeneration),
+}
+
+
+class T5Model:
     def __init__(
-            self, model_type, model_name, args=None, use_cuda=has_cuda, cuda_device=-1, **kwargs
+            self,
+            model_type,
+            model_name,
+            args=None,
+            tokenizer=None,
+            use_cuda=has_cuda,
+            cuda_device=-1,
+            **kwargs,
     ):
+
         """
-        Initializes a QuestionAnsweringModel model.
+        Initializes a T5Model model.
 
         Args:
-            model_type: The type of model (bert, xlnet, xlm, distilbert)
-            model_name: Default Transformer model name or path to a directory containing Transformer model file (pytorch_nodel.bin).
-            args (optional): Default args will be used if this parameter is not provided. If provided,
-                it should be a dict containing the args that should be changed in the default args'
+            model_type: The type of model (t5, mt5, byt5)
+            model_name: The exact architecture and trained weights to use. This may be a Hugging Face Transformers compatible pre-trained model, a community model, or the path to a directory containing model files.
+            args (optional): Default args will be used if this parameter is not provided. If provided, it should be a dict containing the args that should be changed in the default args.
             use_cuda (optional): Use GPU if available. Setting to False will force model to use CPU only.
             cuda_device (optional): Specific GPU that should be used. Will use the first available GPU by default.
+            **kwargs (optional): For providing proxies, force_download, resume_download, cache_dir and other options specific to the 'from_pretrained' implementation where this will be supplied.
         """  # noqa: ignore flake8"
 
-        MODEL_CLASSES = {
-            "albert": (AlbertConfig, AlbertForQuestionAnswering, AlbertTokenizer),
-            "auto": (AutoConfig, AutoModelForQuestionAnswering, AutoTokenizer),
-            "bart": (BartConfig, BartForQuestionAnswering, BartTokenizer),
-            "bert": (BertConfig, BertForQuestionAnswering, BertTokenizer),
-            "camembert": (
-                CamembertConfig,
-                CamembertForQuestionAnswering,
-                CamembertTokenizer,
-            ),
-            "distilbert": (
-                DistilBertConfig,
-                DistilBertForQuestionAnswering,
-                DistilBertTokenizer,
-            ),
-            "electra": (ElectraConfig, ElectraForQuestionAnswering, ElectraTokenizer),
-            "longformer": (
-                LongformerConfig,
-                LongformerForQuestionAnswering,
-                LongformerTokenizer,
-            ),
-            "mobilebert": (
-                MobileBertConfig,
-                MobileBertForQuestionAnswering,
-                MobileBertTokenizer,
-            ),
-            "mpnet": (MPNetConfig, MPNetForQuestionAnswering, MPNetTokenizer),
-            "roberta": (RobertaConfig, RobertaForQuestionAnswering, RobertaTokenizer),
-            "squeezebert": (
-                SqueezeBertConfig,
-                SqueezeBertForQuestionAnswering,
-                SqueezeBertTokenizer,
-            ),
-            "xlm": (XLMConfig, XLMForQuestionAnswering, XLMTokenizer),
-            "xlmroberta": (
-                XLMRobertaConfig,
-                XLMRobertaForQuestionAnswering,
-                XLMRobertaTokenizer,
-            ),
-            "xlnet": (XLNetConfig, XLNetForQuestionAnswering, XLNetTokenizer),
-        }
-
         self.args = self._load_model_args(model_name)
 
         if isinstance(args, dict):
             self.args.update_from_dict(args)
-        elif isinstance(args, QuestionAnsweringArgs):
+        elif isinstance(args, T5Args):
             self.args = args
 
         self.is_sweeping = False
 
         if self.args.manual_seed:
             random.seed(self.args.manual_seed)
             np.random.seed(self.args.manual_seed)
             torch.manual_seed(self.args.manual_seed)
             if self.args.n_gpu > 0:
                 torch.cuda.manual_seed_all(self.args.manual_seed)
 
-        if not use_cuda:
-            self.args.fp16 = False
-
-        config_class, model_class, tokenizer_class = MODEL_CLASSES[model_type]
-        self.config = config_class.from_pretrained(model_name, **self.args.config)
-        if not self.args.quantized_model:
-            self.model = model_class.from_pretrained(
-                model_name, config=self.config, **kwargs
-            )
-        else:
-            quantized_weights = torch.load(
-                os.path.join(model_name, "pytorch_model.bin")
-            )
-            self.model = model_class.from_pretrained(
-                None, config=self.config, state_dict=quantized_weights
-            )
-
-        if self.args.dynamic_quantize:
-            self.model = torch.quantization.quantize_dynamic(
-                self.model, {torch.nn.Linear}, dtype=torch.qint8
-            )
-        if self.args.quantized_model:
-            self.model.load_state_dict(quantized_weights)
-        if self.args.dynamic_quantize:
-            self.args.quantized_model = True
-
         if use_cuda:
             if torch.cuda.is_available():
                 if cuda_device == -1:
                     self.device = torch.device("cuda")
                 else:
                     self.device = torch.device(f"cuda:{cuda_device}")
             else:
                 raise ValueError(
                     "'use_cuda' set to True when cuda is unavailable."
-                    " Make sure CUDA is available or set use_cuda=False."
+                    "Make sure CUDA is available or set `use_cuda=False`."
                 )
         else:
             self.device = "cpu"
         logger.debug(f"Device: {self.device}")
 
         self.results = {}
 
-        if self.args.fp16:
-            try:
-                from torch.cuda import amp
-            except AttributeError:
-                raise AttributeError(
-                    "fp16 requires Pytorch >= 1.6. Please update Pytorch or turn off fp16."
-                )
+        config_class, model_class = MODEL_CLASSES[model_type]
+
+        if model_name is None:
+            self.config = self.args.config
+            self.model = model_class(config=self.config)
+        else:
+            self.config = config_class.from_pretrained(model_name, **self.args.config)
+            self.model = model_class.from_pretrained(model_name, config=self.config)
 
-        if model_type == "auto":
-            self.tokenizer = tokenizer_class.from_pretrained(model_name, **kwargs)
+        if isinstance(tokenizer, T5Tokenizer):
+            self.tokenizer = tokenizer
+            self.model.resize_token_embeddings(len(self.tokenizer))
+        elif model_type == "byt5":
+            self.tokenizer = ByT5Tokenizer.from_pretrained(model_name, truncate=True)
         else:
-            self.tokenizer = tokenizer_class.from_pretrained(
-                model_name, do_lower_case=self.args.do_lower_case, **kwargs
+            self.tokenizer = T5Tokenizer.from_pretrained(model_name, truncate=True)
+
+        if self.args.dynamic_quantize:
+            self.model = torch.quantization.quantize_dynamic(
+                self.model, {torch.nn.Linear}, dtype=torch.qint8
             )
 
+        if not use_cuda:
+            self.args.fp16 = False
+
         if self.args.special_tokens_list:
             self.tokenizer.add_tokens(
                 self.args.special_tokens_list, special_tokens=True
             )
             self.model.resize_token_embeddings(len(self.tokenizer))
 
-        self.args.model_name = model_name
         self.args.model_type = model_type
+        if model_name is None:
+            self.args.model_name = "T5_from_scratch"
+        else:
+            self.args.model_name = model_name
 
-        self.wandb_run_id = None
         if self.args.wandb_project and not wandb_available:
             warnings.warn(
                 "wandb_project specified but wandb is not available. Wandb disabled."
             )
             self.args.wandb_project = None
 
-    def load_and_cache_examples(
-            self, examples, evaluate=False, no_cache=False, output_examples=False
-    ):
-        """
-        Converts a list of examples to a TensorDataset containing InputFeatures. Caches the InputFeatures.
-
-        Utility function for train() and eval() methods. Not intended to be used directly.
-        """
-
-        tokenizer = self.tokenizer
-        args = self.args
-
-        if not no_cache:
-            no_cache = args.no_cache
-
-        if not no_cache:
-            os.makedirs(self.args.cache_dir, exist_ok=True)
-
-        examples = get_examples(examples, is_training=not evaluate)
-
-        mode = "dev" if evaluate else "train"
-        cached_features_file = os.path.join(
-            args.cache_dir,
-            "cached_{}_{}_{}_{}".format(
-                mode, args.model_type, args.max_seq_length, len(examples)
-            ),
-        )
-
-        if os.path.exists(cached_features_file) and (
-                (not args.reprocess_input_data and not no_cache)
-                or (mode == "dev" and args.use_cached_eval_features)
-        ):
-            features = torch.load(cached_features_file)
-            logger.info(f" Features loaded from cache at {cached_features_file}")
-
-            # Convert to Tensors and build dataset
-            all_input_ids = torch.tensor(
-                [f.input_ids for f in features], dtype=torch.long
-            )
-            all_attention_masks = torch.tensor(
-                [f.attention_mask for f in features], dtype=torch.long
-            )
-            all_token_type_ids = torch.tensor(
-                [f.token_type_ids for f in features], dtype=torch.long
-            )
-            all_cls_index = torch.tensor(
-                [f.cls_index for f in features], dtype=torch.long
-            )
-            all_p_mask = torch.tensor([f.p_mask for f in features], dtype=torch.float)
-            all_is_impossible = torch.tensor(
-                [f.is_impossible for f in features], dtype=torch.float
-            )
-
-            if mode == "dev":
-                all_feature_index = torch.arange(
-                    all_input_ids.size(0), dtype=torch.long
-                )
-                dataset = TensorDataset(
-                    all_input_ids,
-                    all_attention_masks,
-                    all_token_type_ids,
-                    all_feature_index,
-                    all_cls_index,
-                    all_p_mask,
-                )
-            else:
-                all_start_positions = torch.tensor(
-                    [f.start_position for f in features], dtype=torch.long
-                )
-                all_end_positions = torch.tensor(
-                    [f.end_position for f in features], dtype=torch.long
-                )
-                dataset = TensorDataset(
-                    all_input_ids,
-                    all_attention_masks,
-                    all_token_type_ids,
-                    all_start_positions,
-                    all_end_positions,
-                    all_cls_index,
-                    all_p_mask,
-                    all_is_impossible,
-                )
-        else:
-            logger.info(" Converting to features started.")
-
-            features, dataset = squad_convert_examples_to_features(
-                examples=examples,
-                tokenizer=tokenizer,
-                max_seq_length=args.max_seq_length,
-                doc_stride=args.doc_stride,
-                max_query_length=args.max_query_length,
-                is_training=not evaluate,
-                tqdm_enabled=not args.silent,
-                threads=args.process_count,
-                args=args,
-            )
-
-            if not no_cache:
-                torch.save(features, cached_features_file)
-
-        if output_examples:
-            return dataset, examples, features
-        return dataset
-
     def train_model(
             self,
             train_data,
-            output_dir=False,
+            output_dir=None,
             show_running_loss=True,
             args=None,
             eval_data=None,
             verbose=True,
             **kwargs,
     ):
         """
         Trains the model using 'train_data'
 
         Args:
-            train_data: Path to JSON file containing training data OR list of Python dicts in the correct format. The model will be trained on this data.
+            train_data: Pandas DataFrame containing the 3 columns - `prefix`, `input_text`, `target_text`.
+                        - `prefix`: A string indicating the task to perform. (E.g. `"question"`, `"stsb"`)
+                        - `input_text`: The input text sequence. `prefix` is automatically prepended to form the full input. (<prefix>: <input_text>)
+                        - `target_text`: The target sequence
             output_dir: The directory where model files will be saved. If not given, self.args.output_dir will be used.
             show_running_loss (optional): Set to False to prevent running loss from being printed to console. Defaults to True.
             args (optional): Optional changes to the args dict of the model. Any changes made will persist for the model.
-            eval_data (optional): Path to JSON file containing evaluation data against which evaluation will be performed when evaluate_during_training is enabled.
-                Is required if evaluate_during_training is enabled.
+            eval_data (optional): A DataFrame against which evaluation will be performed when evaluate_during_training is enabled. Is required if evaluate_during_training is enabled.
             **kwargs: Additional metrics that should be used. Pass in the metrics as keyword arguments (name of metric: function to use).
-                A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions.
+                        A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions. Both inputs
+                        will be lists of strings. Note that this will slow down training significantly as the predicted sequences need to be generated.
+
         Returns:
             global_step: Number of global steps trained
             training_details: Average training loss if evaluate_during_training is False or full training progress scores if evaluate_during_training is True
         """  # noqa: ignore flake8"
 
         if args:
             self.args.update_from_dict(args)
-
-        if self.args.silent:
-            show_running_loss = False
-
         if self.args.evaluate_during_training and eval_data is None:
             raise ValueError(
                 "evaluate_during_training is enabled but eval_data is not specified."
                 " Pass eval_data to model.train_model() if using evaluate_during_training."
             )
 
         if not output_dir:
@@ -410,58 +204,40 @@
         if (
                 os.path.exists(output_dir)
                 and os.listdir(output_dir)
                 and not self.args.overwrite_output_dir
         ):
             raise ValueError(
                 "Output directory ({}) already exists and is not empty."
-                "Use --overwrite_output_dir to overcome.".format(output_dir)
+                " Set args.overwrite_output_dir = True to overcome.".format(output_dir)
             )
 
         self._move_model_to_device()
 
-        if self.args.use_hf_datasets:
-            train_dataset = load_hf_dataset(
-                train_data, self.tokenizer, self.args, is_training=True
-            )
-        elif self.args.lazy_loading:
-            if isinstance(train_data, str):
-                train_dataset = LazyQuestionAnsweringDataset(
-                    train_data, self.tokenizer, self.args
-                )
-            else:
-                raise ValueError(
-                    "Input must be given as a path to a file when using lazy loading"
-                )
-        else:
-            if isinstance(train_data, str):
-                with open(train_data, "r", encoding=self.args.encoding) as f:
-                    train_examples = json.load(f)
-            else:
-                train_examples = train_data
-
-            train_dataset = self.load_and_cache_examples(train_examples)
+        train_dataset = self.load_and_cache_examples(train_data, verbose=verbose)
 
         os.makedirs(output_dir, exist_ok=True)
 
         global_step, training_details = self.train(
             train_dataset,
             output_dir,
             show_running_loss=show_running_loss,
             eval_data=eval_data,
+            verbose=verbose,
             **kwargs,
         )
 
         self.save_model(model=self.model)
 
-        logger.info(
-            " Training of {} model complete. Saved to {}.".format(
-                self.args.model_type, output_dir
+        if verbose:
+            logger.info(
+                " Training of {} model complete. Saved to {}.".format(
+                    self.args.model_name, output_dir
+                )
             )
-        )
 
         return global_step, training_details
 
     def train(
             self,
             train_dataset,
             output_dir,
@@ -474,29 +250,38 @@
         Trains the model on train_dataset.
 
         Utility function to be used by the train_model() method. Not intended to be used directly.
         """
 
         model = self.model
         args = self.args
+        device = self.device
 
         tb_writer = SummaryWriter(log_dir=args.tensorboard_dir)
         train_sampler = RandomSampler(train_dataset)
         train_dataloader = DataLoader(
             train_dataset,
             sampler=train_sampler,
             batch_size=args.train_batch_size,
             num_workers=self.args.dataloader_num_workers,
         )
 
-        t_total = (
-                len(train_dataloader)
-                // args.gradient_accumulation_steps
-                * args.num_train_epochs
-        )
+        if args.max_steps > 0:
+            t_total = args.max_steps
+            args.num_train_epochs = (
+                    args.max_steps
+                    // (len(train_dataloader) // args.gradient_accumulation_steps)
+                    + 1
+            )
+        else:
+            t_total = (
+                    len(train_dataloader)
+                    // args.gradient_accumulation_steps
+                    * args.num_train_epochs
+            )
 
         no_decay = ["bias", "LayerNorm.weight"]
 
         optimizer_grouped_parameters = []
         custom_parameter_names = set()
         for group in self.args.custom_parameter_groups:
             params = group.pop("params")
@@ -623,17 +408,32 @@
                 lr_end=args.polynomial_decay_schedule_lr_end,
                 power=args.polynomial_decay_schedule_power,
             )
 
         else:
             raise ValueError("{} is not a valid scheduler.".format(args.scheduler))
 
+        if (
+                args.model_name
+                and os.path.isfile(os.path.join(args.model_name, "optimizer.pt"))
+                and os.path.isfile(os.path.join(args.model_name, "scheduler.pt"))
+        ):
+            # Load in optimizer and scheduler states
+            optimizer.load_state_dict(
+                torch.load(os.path.join(args.model_name, "optimizer.pt"))
+            )
+            scheduler.load_state_dict(
+                torch.load(os.path.join(args.model_name, "scheduler.pt"))
+            )
+
         if args.n_gpu > 1:
             model = torch.nn.DataParallel(model)
 
+        logger.info(" Training started")
+
         global_step = 0
         training_progress_scores = None
         tr_loss, logging_loss = 0.0, 0.0
         model.zero_grad()
         train_iterator = trange(
             int(args.num_train_epochs), desc="Epoch", disable=args.silent, mininterval=0
         )
@@ -641,15 +441,15 @@
         best_eval_metric = None
         early_stopping_counter = 0
         steps_trained_in_current_epoch = 0
         epochs_trained = 0
 
         if args.model_name and os.path.exists(args.model_name):
             try:
-                # set global_step to global_step of last saved checkpoint from model path
+                # set global_step to gobal_step of last saved checkpoint from model path
                 checkpoint_suffix = args.model_name.split("/")[-1].split("-")
                 if len(checkpoint_suffix) > 2:
                     checkpoint_suffix = checkpoint_suffix[1]
                 else:
                     checkpoint_suffix = checkpoint_suffix[-1]
                 global_step = int(checkpoint_suffix)
                 epochs_trained = global_step // (
@@ -685,15 +485,15 @@
             self.wandb_run_id = wandb.run.id
 
         if args.fp16:
             from torch.cuda import amp
 
             scaler = amp.GradScaler()
 
-        for _ in train_iterator:
+        for current_epoch in train_iterator:
             model.train()
             if epochs_trained > 0:
                 epochs_trained -= 1
                 continue
             train_iterator.set_description(
                 f"Epoch {epoch_number + 1} of {args.num_train_epochs}"
             )
@@ -788,15 +588,20 @@
                         )
 
                     if args.evaluate_during_training and (
                             args.evaluate_during_training_steps > 0
                             and global_step % args.evaluate_during_training_steps == 0
                     ):
                         # Only evaluate when single GPU otherwise metrics may not average well
-                        results, _ = self.eval_model(eval_data, verbose=False, **kwargs)
+                        results = self.eval_model(
+                            eval_data,
+                            verbose=verbose and args.evaluate_during_training_verbose,
+                            silent=args.evaluate_during_training_silent,
+                            **kwargs,
+                        )
                         for key, value in results.items():
                             try:
                                 tb_writer.add_scalar(
                                     "eval_{}".format(key), value, global_step
                                 )
                             except (NotImplementedError, AssertionError):
                                 pass
@@ -933,20 +738,26 @@
                 output_dir, "checkpoint-{}-epoch-{}".format(global_step, epoch_number)
             )
 
             if args.save_model_every_epoch:
                 self.save_model(output_dir_current, optimizer, scheduler, model=model)
 
             if args.evaluate_during_training and args.evaluate_each_epoch:
-                results, _ = self.eval_model(eval_data, verbose=False, **kwargs)
-
-                self.save_model(
-                    output_dir_current, optimizer, scheduler, results=results
+                results = self.eval_model(
+                    eval_data,
+                    verbose=verbose and args.evaluate_during_training_verbose,
+                    silent=args.evaluate_during_training_silent,
+                    **kwargs,
                 )
 
+                if args.save_eval_checkpoints:
+                    self.save_model(
+                        output_dir_current, optimizer, scheduler, results=results
+                    )
+
                 training_progress_scores["global_step"].append(global_step)
                 training_progress_scores["train_loss"].append(current_loss)
                 for key in results:
                     training_progress_scores[key].append(results[key])
                 report = pd.DataFrame(training_progress_scores)
                 report.to_csv(
                     os.path.join(args.output_dir, "training_progress_scores.csv"),
@@ -1058,476 +869,323 @@
             global_step,
             tr_loss / global_step
             if not self.args.evaluate_during_training
             else training_progress_scores,
         )
 
     def eval_model(
-            self, eval_data, output_dir=None, verbose=False, verbose_logging=False, **kwargs
+            self, eval_data, output_dir=None, verbose=True, silent=False, **kwargs
     ):
         """
         Evaluates the model on eval_data. Saves results to output_dir.
 
         Args:
-            eval_data: Path to JSON file containing evaluation data OR list of Python dicts in the correct format. The model will be evaluated on this data.
+            eval_data: Pandas DataFrame containing the 3 columns - `prefix`, `input_text`, `target_text`.
+                        - `prefix`: A string indicating the task to perform. (E.g. `"question"`, `"stsb"`)
+                        - `input_text`: The input text sequence. `prefix` is automatically prepended to form the full input. (<prefix>: <input_text>)
+                        - `target_text`: The target sequence
             output_dir: The directory where model files will be saved. If not given, self.args.output_dir will be used.
             verbose: If verbose, results will be printed to the console on completion of evaluation.
-            verbose_logging: Log info related to feature conversion and writing predictions.
+            silent: If silent, tqdm progress bars will be hidden.
             **kwargs: Additional metrics that should be used. Pass in the metrics as keyword arguments (name of metric: function to use).
-                A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions.
-
+                        A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions. Both inputs
+                        will be lists of strings. Note that this will slow down evaluation significantly as the predicted sequences need to be generated.
         Returns:
-            result: Dictionary containing evaluation results. (correct, similar, incorrect)
-            text: A dictionary containing the 3 dictionaries correct_text, similar_text (the predicted answer is a substring of the correct answer or vise versa), incorrect_text.
+            results: Dictionary containing evaluation results.
         """  # noqa: ignore flake8"
 
         if not output_dir:
             output_dir = self.args.output_dir
 
         self._move_model_to_device()
 
-        all_predictions, all_nbest_json, scores_diff_json, eval_loss = self.evaluate(
-            eval_data, output_dir, verbose_logging=verbose
+        eval_dataset = self.load_and_cache_examples(
+            eval_data, evaluate=True, verbose=verbose, silent=silent
         )
+        os.makedirs(output_dir, exist_ok=True)
 
-        if isinstance(eval_data, str):
-            with open(eval_data, "r", encoding=self.args.encoding) as f:
-                truth = json.load(f)
-        else:
-            truth = eval_data
+        result = self.evaluate(
+            eval_dataset, output_dir, verbose=verbose, silent=silent, **kwargs
+        )
+        self.results.update(result)
 
-        result, texts = self.calculate_results(truth, all_predictions, **kwargs)
-        result["eval_loss"] = eval_loss
+        if self.args.evaluate_generated_text:
+            if self.args.preprocess_inputs:
+                to_predict = [
+                    prefix + ": " + input_text
+                    for prefix, input_text in zip(
+                        eval_data["prefix"], eval_data["input_text"]
+                    )
+                ]
+            else:
+                to_predict = [
+                    prefix + input_text
+                    for prefix, input_text in zip(
+                        eval_data["prefix"], eval_data["input_text"]
+                    )
+                ]
+            preds = self.predict(to_predict)
 
-        self.results.update(result)
+            result = self.compute_metrics(
+                eval_data["target_text"].tolist(), preds, **kwargs
+            )
+            self.results.update(result)
 
         if verbose:
             logger.info(self.results)
 
-        return result, texts
+        return self.results
 
-    def evaluate(self, eval_data, output_dir, verbose_logging=False):
+    def evaluate(self, eval_dataset, output_dir, verbose=True, silent=False, **kwargs):
         """
-        Evaluates the model on eval_data.
+        Evaluates the model on eval_dataset.
 
         Utility function to be used by the eval_model() method. Not intended to be used directly.
         """
-        tokenizer = self.tokenizer
+
         model = self.model
         args = self.args
+        eval_output_dir = output_dir
+        device = self.device
 
-        if isinstance(eval_data, str):
-            with open(eval_data, "r", encoding=self.args.encoding) as f:
-                eval_examples = json.load(f)
-        else:
-            eval_examples = eval_data
-
-        eval_dataset, examples, features = self.load_and_cache_examples(
-            eval_examples, evaluate=True, output_examples=True
-        )
+        results = {}
 
         eval_sampler = SequentialSampler(eval_dataset)
         eval_dataloader = DataLoader(
             eval_dataset, sampler=eval_sampler, batch_size=args.eval_batch_size
         )
 
+        if args.n_gpu > 1:
+            model = torch.nn.DataParallel(model)
+
         eval_loss = 0.0
         nb_eval_steps = 0
         model.eval()
 
-        if args.n_gpu > 1:
-            model = torch.nn.DataParallel(model)
-
         if self.args.fp16:
             from torch.cuda import amp
 
-        all_results = []
         for batch in tqdm(
-                eval_dataloader, disable=args.silent, desc="Running Evaluation"
+                eval_dataloader, disable=args.silent or silent, desc="Running Evaluation"
         ):
-            batch = tuple(t.to(self.device) for t in batch)
-
+            inputs = self._get_inputs_dict(batch)
             with torch.no_grad():
-                inputs = {
-                    "input_ids": batch[0],
-                    "attention_mask": batch[1],
-                    "token_type_ids": batch[2],
-                }
-
-                if self.args.model_type in [
-                    "xlm",
-                    "roberta",
-                    "distilbert",
-                    "camembert",
-                    "electra",
-                    "xlmroberta",
-                    "bart",
-                ]:
-                    del inputs["token_type_ids"]
-
-                example_indices = batch[3]
-
-                if args.model_type in ["xlnet", "xlm"]:
-                    inputs.update({"cls_index": batch[4], "p_mask": batch[5]})
-
                 if self.args.fp16:
                     with amp.autocast():
                         outputs = model(**inputs)
-                        eval_loss += outputs[0].mean().item()
+                        loss = outputs[0]
                 else:
                     outputs = model(**inputs)
-                    eval_loss += outputs[0].mean().item()
-
-                for i, example_index in enumerate(example_indices):
-                    eval_feature = features[example_index.item()]
-                    unique_id = int(eval_feature.unique_id)
-                    if args.model_type in ["xlnet", "xlm"]:
-                        # XLNet uses a more complex post-processing procedure
-                        result = RawResultExtended(
-                            unique_id=unique_id,
-                            start_top_log_probs=to_list(outputs[0][i]),
-                            start_top_index=to_list(outputs[1][i]),
-                            end_top_log_probs=to_list(outputs[2][i]),
-                            end_top_index=to_list(outputs[3][i]),
-                            cls_logits=to_list(outputs[4][i]),
-                        )
-                    else:
-                        result = RawResult(
-                            unique_id=unique_id,
-                            start_logits=to_list(outputs[0][i]),
-                            end_logits=to_list(outputs[1][i]),
-                        )
-                    all_results.append(result)
-
+                    loss = outputs[0]
+                if self.args.n_gpu > 1:
+                    loss = loss.mean()
+                eval_loss += loss.item()
             nb_eval_steps += 1
 
         eval_loss = eval_loss / nb_eval_steps
 
-        prefix = "test"
-        os.makedirs(output_dir, exist_ok=True)
-
-        output_prediction_file = os.path.join(
-            output_dir, "predictions_{}.json".format(prefix)
-        )
-        output_nbest_file = os.path.join(
-            output_dir, "nbest_predictions_{}.json".format(prefix)
-        )
-        output_null_log_odds_file = os.path.join(
-            output_dir, "null_odds_{}.json".format(prefix)
-        )
+        results["eval_loss"] = eval_loss
 
-        if args.model_type in ["xlnet", "xlm"]:
-            # XLNet uses a more complex post-processing procedure
-            (
-                all_predictions,
-                all_nbest_json,
-                scores_diff_json,
-            ) = write_predictions_extended(
-                examples,
-                features,
-                all_results,
-                args.n_best_size,
-                args.max_answer_length,
-                output_prediction_file,
-                output_nbest_file,
-                output_null_log_odds_file,
-                eval_data,
-                model.config.start_n_top,
-                model.config.end_n_top,
-                True,
-                tokenizer,
-                verbose_logging,
-            )
-        else:
-            all_predictions, all_nbest_json, scores_diff_json = write_predictions(
-                examples,
-                features,
-                all_results,
-                args.n_best_size,
-                args.max_answer_length,
-                False,
-                output_prediction_file,
-                output_nbest_file,
-                output_null_log_odds_file,
-                verbose_logging,
-                True,
-                args.null_score_diff_threshold,
-            )
+        output_eval_file = os.path.join(eval_output_dir, "eval_results.txt")
+        with open(output_eval_file, "w") as writer:
+            for key in sorted(results.keys()):
+                writer.write("{} = {}\n".format(key, str(results[key])))
 
-        return all_predictions, all_nbest_json, scores_diff_json, eval_loss
+        return results
 
-    def predict(self, to_predict, n_best_size=None):
+    def predict(self, to_predict, split_on_space=False):
         """
-        Performs predictions on a list of python dicts containing contexts and qas.
+        Performs predictions on a list of text.
 
         Args:
-            to_predict: A python list of python dicts containing contexts and questions to be sent to the model for prediction.
-                        E.g: predict([
-                            {
-                                'context': "Some context as a demo",
-                                'qas': [
-                                    {'id': '0', 'question': 'What is the context here?'},
-                                    {'id': '1', 'question': 'What is this for?'}
-                                ]
-                            }
-                        ])
-            n_best_size (Optional): Number of predictions to return. args.n_best_size will be used if not specified.
+            to_predict: A python list of text (str) to be sent to the model for prediction. Note that the prefix should be prepended to the text.
+            split_on_space (optional): If True, input is english string, if False, input is chinese string.
 
         Returns:
-            list: A python list  of dicts containing the predicted answer/answers, and id for each question in to_predict.
-            list: A python list  of dicts containing the predicted probability/probabilities, and id for each question in to_predict.
+            preds: A python list of the generated sequences.
         """  # noqa: ignore flake8"
-        tokenizer = self.tokenizer
-        device = self.device
-        model = self.model
-        args = self.args
-
-        if not n_best_size:
-            n_best_size = args.n_best_size
 
         self._move_model_to_device()
 
-        eval_examples = build_examples(to_predict)
-        eval_dataset, examples, features = self.load_and_cache_examples(
-            eval_examples, evaluate=True, output_examples=True, no_cache=True
-        )
-
-        eval_sampler = SequentialSampler(eval_dataset)
-        eval_dataloader = DataLoader(
-            eval_dataset, sampler=eval_sampler, batch_size=args.eval_batch_size
-        )
-
-        model.eval()
-
-        if args.n_gpu > 1:
-            model = torch.nn.DataParallel(model)
-
-        if self.args.fp16:
-            from torch.cuda import amp
-
-        all_results = []
+        all_outputs = []
+        # Batching
         for batch in tqdm(
-                eval_dataloader, disable=args.silent, desc="Running Prediction"
+                [
+                    to_predict[i: i + self.args.eval_batch_size]
+                    for i in range(0, len(to_predict), self.args.eval_batch_size)
+                ],
+                desc="Generating outputs",
+                disable=self.args.silent,
         ):
-            batch = tuple(t.to(self.device) for t in batch)
-
-            with torch.no_grad():
-                inputs = {
-                    "input_ids": batch[0],
-                    "attention_mask": batch[1],
-                    "token_type_ids": batch[2],
-                }
-
-                if self.args.model_type in [
-                    "xlm",
-                    "roberta",
-                    "distilbert",
-                    "camembert",
-                    "electra",
-                    "xlmroberta",
-                    "bart",
-                ]:
-                    del inputs["token_type_ids"]
-
-                example_indices = batch[3]
-
-                if args.model_type in ["xlnet", "xlm"]:
-                    inputs.update({"cls_index": batch[4], "p_mask": batch[5]})
-
-                if self.args.fp16:
-                    with amp.autocast():
-                        outputs = model(**inputs)
+            input_batch = self.tokenizer.prepare_seq2seq_batch(
+                src_texts=batch,
+                max_length=self.args.max_seq_length,
+                padding="max_length",
+                return_tensors="pt",
+                truncation=True,
+            )
+            input_ids = input_batch["input_ids"]
+            attention_mask = input_batch["attention_mask"]
+
+            input_ids = input_ids.to(self.device)
+            attention_mask = attention_mask.to(self.device)
+
+            outputs = self.model.generate(
+                input_ids=input_ids,
+                attention_mask=attention_mask,
+                num_beams=self.args.num_beams,
+                max_length=self.args.max_length,
+                length_penalty=self.args.length_penalty,
+                early_stopping=self.args.early_stopping,
+                repetition_penalty=self.args.repetition_penalty,
+                do_sample=self.args.do_sample,
+                top_k=self.args.top_k,
+                top_p=self.args.top_p,
+                num_return_sequences=self.args.num_return_sequences,
+            )
+            all_outputs.extend(outputs.cpu().numpy())
+
+        if self.args.use_multiprocessed_decoding:
+            self.model.to("cpu")
+            with Pool(self.args.process_count) as p:
+                if self.args.multiprocessing_chunksize == -1:
+                    chunksize = max(
+                        len(all_outputs) // (self.args.process_count * 2), 500
+                    )
                 else:
-                    outputs = model(**inputs)
-
-                for i, example_index in enumerate(example_indices):
-                    eval_feature = features[example_index.item()]
-                    unique_id = int(eval_feature.unique_id)
-                    if args.model_type in ["xlnet", "xlm"]:
-                        # XLNet uses a more complex post-processing procedure
-                        result = RawResultExtended(
-                            unique_id=unique_id,
-                            start_top_log_probs=to_list(outputs[0][i]),
-                            start_top_index=to_list(outputs[1][i]),
-                            end_top_log_probs=to_list(outputs[2][i]),
-                            end_top_index=to_list(outputs[3][i]),
-                            cls_logits=to_list(outputs[4][i]),
-                        )
-                    else:
-                        result = RawResult(
-                            unique_id=unique_id,
-                            start_logits=to_list(outputs[0][i]),
-                            end_logits=to_list(outputs[1][i]),
-                        )
-                    all_results.append(result)
-
-        if args.model_type in ["xlnet", "xlm"]:
-            answers = get_best_predictions_extended(
-                examples,
-                features,
-                all_results,
-                n_best_size,
-                args.max_answer_length,
-                model.config.start_n_top,
-                model.config.end_n_top,
-                True,
-                tokenizer,
-                args.null_score_diff_threshold,
-            )
+                    chunksize = self.args.multiprocessing_chunksize
+                outputs = list(
+                    tqdm(
+                        p.imap(self._decode, all_outputs, chunksize=chunksize),
+                        total=len(all_outputs),
+                        desc="Decoding outputs",
+                        disable=self.args.silent,
+                    )
+                )
+            self._move_model_to_device()
         else:
-            answers = get_best_predictions(
-                examples,
-                features,
-                all_results,
-                n_best_size,
-                args.max_answer_length,
-                False,
-                False,
-                True,
-                False,
-            )
-
-        answer_list = [
-            {"id": answer["id"], "answer": answer["answer"][:-1]} for answer in answers
-        ]
-        probability_list = [
-            {"id": answer["id"], "probability": answer["probability"][:-1]}
-            for answer in answers
-        ]
-
-        return answer_list, probability_list
-
-    def calculate_results(self, truth, predictions, **kwargs):
-        truth_dict = {}
-        questions_dict = {}
-        for item in truth:
-            for answer in item["qas"]:
-                if answer["answers"]:
-                    truth_dict[answer["id"]] = answer["answers"][0]["text"]
-                else:
-                    truth_dict[answer["id"]] = ""
-                questions_dict[answer["id"]] = answer["question"]
+            outputs = [
+                self.tokenizer.decode(
+                    output_id,
+                    skip_special_tokens=self.args.skip_special_tokens,
+                    clean_up_tokenization_spaces=True,
+                )
+                for output_id in all_outputs
+            ]
+        if not split_on_space:
+            outputs = [''.join(gen_text.split(' ')) for gen_text in outputs]
+        if self.args.num_return_sequences > 1:
+            return [
+                outputs[i: i + self.args.num_return_sequences]
+                for i in range(0, len(outputs), self.args.num_return_sequences)
+            ]
+        else:
+            return outputs
 
-        correct = 0
-        incorrect = 0
-        similar = 0
-        correct_text = {}
-        incorrect_text = {}
-        similar_text = {}
-        predicted_answers = []
-        true_answers = []
-
-        for q_id, answer in truth_dict.items():
-            predicted_answers.append(predictions[q_id])
-            true_answers.append(answer)
-            if predictions[q_id].strip() == answer.strip():
-                correct += 1
-                correct_text[q_id] = answer
-            elif (
-                    predictions[q_id].strip() in answer.strip()
-                    or answer.strip() in predictions[q_id].strip()
-            ):
-                similar += 1
-                similar_text[q_id] = {
-                    "truth": answer,
-                    "predicted": predictions[q_id],
-                    "question": questions_dict[q_id],
-                }
-            else:
-                incorrect += 1
-                incorrect_text[q_id] = {
-                    "truth": answer,
-                    "predicted": predictions[q_id],
-                    "question": questions_dict[q_id],
-                }
+    def _decode(self, output_id):
+        return self.tokenizer.decode(
+            output_id,
+            skip_special_tokens=self.args.skip_special_tokens,
+            clean_up_tokenization_spaces=True,
+        )
 
-        extra_metrics = {}
-        for metric, func in kwargs.items():
-            extra_metrics[metric] = func(true_answers, predicted_answers)
+    def compute_metrics(self, labels, preds, **kwargs):
+        """
+        Computes the evaluation metrics for the model predictions.
 
-        result = {
-            "correct": correct,
-            "similar": similar,
-            "incorrect": incorrect,
-            **extra_metrics,
-        }
+        Args:
+            labels: List of target sequences
+            preds: List of model generated outputs
+            **kwargs: Custom metrics that should be used. Pass in the metrics as keyword arguments (name of metric: function to use).
+                        A metric function should take in two parameters. The first parameter will be the true labels, and the second parameter will be the predictions. Both inputs
+                        will be lists of strings. Note that this will slow down evaluation significantly as the predicted sequences need to be generated.
 
-        texts = {
-            "correct_text": correct_text,
-            "similar_text": similar_text,
-            "incorrect_text": incorrect_text,
-        }
+        Returns:
+            result: Dictionary containing evaluation results.
+        """  # noqa: ignore flake8"
+        assert len(labels) == len(preds)
+
+        results = {}
+        for metric, func in kwargs.items():
+            results[metric] = func(labels, preds)
 
-        return result, texts
+        return results
 
     def _move_model_to_device(self):
         self.model.to(self.device)
 
-    def _get_last_metrics(self, metric_values):
-        return {metric: values[-1] for metric, values in metric_values.items()}
-
     def _get_inputs_dict(self, batch):
         if self.args.use_hf_datasets:
-            inputs = {key: value.to(self.device) for key, value in batch.items()}
-
-            if self.args.model_type in [
-                "xlm",
-                "roberta",
-                "distilbert",
-                "camembert",
-                "electra",
-                "xlmroberta",
-                "bart",
-            ]:
-                del inputs["token_type_ids"]
-            if self.args.model_type not in ["xlnet", "xlm"]:
-                del inputs["cls_index"]
-                del inputs["p_mask"]
+            inputs = {**batch, "labels": batch["input_ids"]}
 
-            return inputs
+            return {key: value.to(self.device) for key, value in inputs.items()}
         else:
             batch = tuple(t.to(self.device) for t in batch)
+
+            input_ids = batch[0]
+            attention_mask = batch[1]
+            labels = batch[2]
+            labels[labels == self.tokenizer.pad_token_id] = -100
+
             inputs = {
-                "input_ids": batch[0],
-                "attention_mask": batch[1],
-                "token_type_ids": batch[2],
-                "start_positions": batch[3],
-                "end_positions": batch[4],
+                "input_ids": input_ids,
+                "attention_mask": attention_mask,
+                "labels": labels,
             }
 
-            if self.args.model_type in [
-                "xlm",
-                "roberta",
-                "distilbert",
-                "camembert",
-                "electra",
-                "xlmroberta",
-                "bart",
-            ]:
-                del inputs["token_type_ids"]
+            return inputs
 
-            if self.args.model_type in ["xlnet", "xlm"]:
-                inputs.update({"cls_index": batch[5], "p_mask": batch[6]})
+    def load_and_cache_examples(
+            self, data, evaluate=False, no_cache=False, verbose=True, silent=False
+    ):
+        """
+        Creates a T5Dataset from data.
 
-            return inputs
+        Utility function for train() and eval() methods. Not intended to be used directly.
+        """
+
+        tokenizer = self.tokenizer
+        args = self.args
+
+        if not no_cache:
+            no_cache = args.no_cache
+
+        if not no_cache:
+            os.makedirs(self.args.cache_dir, exist_ok=True)
+
+        mode = "dev" if evaluate else "train"
+
+        if self.args.use_hf_datasets:
+            dataset = load_hf_dataset(data, tokenizer, self.args)
+            return dataset
+        elif args.dataset_class:
+            CustomDataset = args.dataset_class
+            return CustomDataset(tokenizer, args, data, mode)
+        else:
+            return T5Dataset(
+                tokenizer,
+                self.args,
+                data,
+                mode,
+            )
 
     def _create_training_progress_scores(self, **kwargs):
         extra_metrics = {key: [] for key in kwargs}
         training_progress_scores = {
             "global_step": [],
-            "correct": [],
-            "similar": [],
-            "incorrect": [],
-            "train_loss": [],
             "eval_loss": [],
+            "train_loss": [],
             **extra_metrics,
         }
 
         return training_progress_scores
 
+    def _get_last_metrics(self, metric_values):
+        return {metric: values[-1] for metric, values in metric_values.items()}
+
     def save_model(
             self, output_dir=None, optimizer=None, scheduler=None, model=None, results=None
     ):
         if not output_dir:
             output_dir = self.args.output_dir
         os.makedirs(output_dir, exist_ok=True)
 
@@ -1553,13 +1211,13 @@
                     writer.write("{} = {}\n".format(key, str(results[key])))
 
     def save_model_args(self, output_dir):
         os.makedirs(output_dir, exist_ok=True)
         self.args.save(output_dir)
 
     def _load_model_args(self, input_dir):
-        args = QuestionAnsweringArgs()
+        args = T5Args()
         args.load(input_dir)
         return args
 
     def get_named_parameters(self):
         return [n for n, p in self.model.named_parameters()]
```

### Comparing `textgen-0.1.7/textgen/seq2seq/bart_seq2seq_model.py` & `textgen-0.1.8/textgen/seq2seq/bart_seq2seq_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/seq2seq/bart_seq2seq_utils.py` & `textgen-0.1.8/textgen/seq2seq/bart_seq2seq_utils.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/seq2seq/conv_seq2seq_model.py` & `textgen-0.1.8/textgen/seq2seq/conv_seq2seq_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/seq2seq/data_reader.py` & `textgen-0.1.8/textgen/seq2seq/data_reader.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/seq2seq/seq2seq_model.py` & `textgen-0.1.8/textgen/seq2seq/seq2seq_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/seq2seq/seq2seq_trainer.py` & `textgen-0.1.8/textgen/seq2seq/seq2seq_trainer.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/t5/copyt5_model.py` & `textgen-0.1.8/textgen/t5/copyt5_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/t5/copyt5_utils.py` & `textgen-0.1.8/textgen/t5/copyt5_utils.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/t5/t5_utils.py` & `textgen-0.1.8/textgen/t5/t5_utils.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/unsup_generation/tgls_model.py` & `textgen-0.1.8/textgen/unsup_generation/tgls_model.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen/unsup_generation/tgls_util.py` & `textgen-0.1.8/textgen/unsup_generation/tgls_util.py`

 * *Files identical despite different names*

### Comparing `textgen-0.1.7/textgen.egg-info/PKG-INFO` & `textgen-0.1.8/textgen.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: textgen
-Version: 0.1.7
+Version: 0.1.8
 Summary: Text Generation Model
 Home-page: https://github.com/shibing624/textgen
 Author: XuMing
 Author-email: xuming624@qq.com
 License: Apache 2.0
 Description: [![PyPI version](https://badge.fury.io/py/textgen.svg)](https://badge.fury.io/py/textgen)
         [![Downloads](https://pepy.tech/badge/textgen)](https://pepy.tech/project/textgen)
@@ -19,56 +19,62 @@
         
         🌈 Implementation of Text Generation models.
         
         **textgen**实现了多种文本生成模型，包括：UDA、GPT2、Seq2Seq、BART、T5、SongNet等模型，开箱即用。
         
         **Guide**
         
-        - [Question](#Question)
-        - [Solution](#Solution)
         - [Feature](#Feature)
         - [Install](#install)
         - [Usage](#usage)
         - [Contact](#Contact)
         - [Reference](#reference)
         
-        # Question
-        
-        文本生成，文本数据增强怎么做？
-        
-        # Solution
-        ## 文本生成模型
+        # Feature
+        ## 文本生成
         
-        1. Seq2Seq、ConvSeq2Seq、BART
-        2. GPT2、SongNet
-        3. T5、CopyT5
+        1. seq2seq: Seq2Seq、ConvSeq2Seq、BART
+        2. language_modeling: GPT2、SongNet
+        3. t5: T5、CopyT5
+        4. question_answering: BERT、XLNet
+        5. chatglm: ChatGLM
         
         ## 文本扩增
         ### 词粒度扩增
         1. UDA，非核心词替换
         2. EDA，简单数据增强技术：相似词、同义词替换，随机词插入、删除、替换
         
         ### 句粒度扩增
         1. 回译（BT, Back Translate）：中文-英文-中文
         2. GPT2模型续写：短文本->长文本
         3. BART摘要模型：长文本->短文本
         4. TGLS：无监督相似文本生成模型
         
-        
-        # Feature
-        
+        ## 功能列表
         - [UDA(非核心词替换)/EDA](textgen/augment/word_level_augment.py)：本项目参考Google的UDA(非核心词替换)算法和EDA算法，基于TF-IDF将句子中部分不重要词替换为同义词，随机词插入、删除、替换等方法，产生新的文本，实现了文本扩增
         - [BT(回译)](textgen/augment/sentence_level_augment.py)：本项目基于百度翻译API实现了回译功能，先把中文句子翻译为英文，再把英文翻译为新的中文
         - [Seq2Seq](textgen/seq2seq)：本项目基于PyTorch实现了Seq2Seq、ConvSeq2Seq、BART模型的训练和预测，可以用于文本翻译、对话生成、摘要生成等文本生成任务
         - [T5](textgen/t5)：本项目基于PyTorch实现了T5和CopyT5模型训练和预测，可以用于文本翻译、对话生成、对联生成、文案撰写等文本生成任务
         - [GPT2](textgen/language_modeling)：本项目基于PyTorch实现了GTP2模型训练和预测，可以用于文章生成、对联生成等文本生成任务
         - [SongNet](textgen/language_modeling/songnet_model.py)：本项目基于PyTorch实现了SongNet模型训练和预测，可以用于规范格式的诗词、歌词等文本生成任务
         - [TGLS](textgen/unsup_generation)：本项目实现了[TGLS](https://www.jiqizhixin.com/articles/2020-08-11-5)无监督相似文本生成模型，是一种“先搜索后学习”的文本生成方法，通过反复迭代学习候选集，最终模型能生成类似候选集的高质量相似文本
         
         
+        ## Release Models
+        release基于`textgen`训练的中文模型，模型已经release到HuggingFace models，指定模型名称`textgen`会自动下载模型，可直接使用。
+        
+        |Model|Arch|Intro|Training|Inference|
+        |:-- |:--- |:--- |:--- |:--- |
+        |[shibing624/prompt-t5-base-chinese](https://huggingface.co/shibing624/prompt-t5-base-chinese)|T5|中文NLP多任务Prompt模型|[prompt-t5-base-chinese.md](https://github.com/shibing624/textgen/blob/main/docs/prompt-t5-base-chinese.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_prompt_demo.py)|
+        |[shibing624/t5-chinese-couplet](https://huggingface.co/shibing624/t5-chinese-couplet)|T5|fine-tuned中文对联后的模型|[对联生成模型调研](https://github.com/shibing624/textgen/blob/main/docs/%E5%AF%B9%E8%81%94%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%AF%94.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_couplet_demo.py)|
+        |[shibing624/songnet-base-chinese](https://huggingface.co/shibing624/songnet-base-chinese)|SongNet|SongNet预训练模型|-|-|
+        |[shibing624/songnet-base-chinese-songci](https://huggingface.co/shibing624/songnet-base-chinese-songci)|SongNet|fine-tuned宋词后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_songci_demo.py)|
+        |[shibing624/songnet-base-chinese-couplet](https://huggingface.co/shibing624/songnet-base-chinese-couplet)|SongNet|fine-tuned对联后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_couplet_demo.py)|
+        
+        
         # Demo
         
         HuggingFace Demo: https://huggingface.co/spaces/shibing624/chinese-couplet-generate
         
         ![](docs/hf.png)
         
         run example: [examples/gradio_demo.py](examples/gradio_demo.py) to see the demo:
@@ -260,22 +266,14 @@
         output:
         ```shell
         inputs: ['什么是ai', '你是什么类型的计算机', '你知道热力学吗']
         outputs: ['人工智能有两个广义的定义,任何拟人的机械,如在卡雷尔capeks', '我的程序运行在Python,所以我在任何电脑上工作!', '什么是热力学']
         ```
         
         
-        ### T5 模型应用
-        
-        release基于T5的fine-tuned后的中文模型，模型全部release到HuggingFace models，`textgen`可自动下载，可直接使用。
-        
-        |Model|Arch|Intro|Training|Inference|
-        |:-- |:--- |:--- |:--- |:--- |
-        |[shibing624/prompt-t5-base-chinese](https://huggingface.co/shibing624/prompt-t5-base-chinese)|T5|中文NLP多任务Prompt模型|[prompt-t5-base-chinese.md](https://github.com/shibing624/textgen/blob/main/docs/prompt-t5-base-chinese.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_prompt_demo.py)|
-        |[shibing624/t5-chinese-couplet](https://huggingface.co/shibing624/t5-chinese-couplet)|T5|fine-tuned中文对联后的模型|[对联生成模型调研](https://github.com/shibing624/textgen/blob/main/docs/%E5%AF%B9%E8%81%94%E7%94%9F%E6%88%90%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%AF%94.md)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/t5_couplet_demo.py)|
         
         
         ## GPT2 模型
         
         ### 中文GPT2 - 文章生成
         
         使用中文数据集（段落格式，`\n`间隔），训练GPT2模型，可以用于诗歌生成、文章生成等任务。
@@ -300,23 +298,14 @@
         ## SongNet 模型
         
         格式控制的文本生成模型，paper见[SongNet: Rigid Formats Controlled Text Generation](https://arxiv.org/abs/2004.08022)，
         适用于强韵律格式要求的诗歌、对联、歌词生成等任务。
         
         example: [examples/language_generation/training_zh_songnet_demo.py](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)
         
-        ### SongNet 模型应用
-        
-        release基于SongNet的中文模型，模型全部release到HuggingFace models，`textgen`可自动下载，可直接使用。
-        
-        |Model|Arch|Intro|Training|Inference|
-        |:-- |:--- |:--- |:--- |:--- |
-        |[shibing624/songnet-base-chinese](https://huggingface.co/shibing624/songnet-base-chinese)|SongNet|SongNet预训练模型|-|-|
-        |[shibing624/songnet-base-chinese-songci](https://huggingface.co/shibing624/songnet-base-chinese-songci)|SongNet|fine-tuned宋词后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_songci_demo.py)|
-        |[shibing624/songnet-base-chinese-couplet](https://huggingface.co/shibing624/songnet-base-chinese-couplet)|SongNet|fine-tuned对联后的模型|[training script](https://github.com/shibing624/textgen/blob/main/examples/language_generation/training_zh_songnet_demo.py)|[predict script](https://github.com/shibing624/textgen/blob/main/examples/songnet_couplet_demo.py)|
         
         
         ## Keyword Text Augmentation(EDA/UDA)
         
         example: [examples/text_augmentation_demo.py](examples/text_augmentation_demo.py)
         
         ```python
@@ -434,14 +423,28 @@
         - Issue(建议)
           ：[![GitHub issues](https://img.shields.io/github/issues/shibing624/textgen.svg)](https://github.com/shibing624/textgen/issues)
         - 邮件我：xuming: xuming624@qq.com
         - 微信我： 加我*微信号：xuming624, 备注：姓名-公司名-NLP* 进NLP交流群。
         
         <img src="docs/wechat.jpeg" width="200" />
         
+        
+        # Citation
+        
+        如果你在研究中使用了textgen，请按如下格式引用：
+        
+        ```latex
+        @misc{textgen,
+          title={textgen: Text Generation Tool},
+          author={Xu Ming},
+          year={2021},
+          howpublished={\url{https://github.com/shibing624/textgen}},
+        }
+        ```
+        
         # License
         
         授权协议为 [The Apache License 2.0](/LICENSE)，可免费用做商业用途。请在产品说明中附加textgen的链接和授权协议。
         
         # Contribute
         
         项目代码还很粗糙，如果大家对代码有所改进，欢迎提交回本项目，在提交之前，注意以下两点：
```

### Comparing `textgen-0.1.7/textgen.egg-info/SOURCES.txt` & `textgen-0.1.8/textgen.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -11,14 +11,17 @@
 textgen/augment/__init__.py
 textgen/augment/sentence_level_augment.py
 textgen/augment/text_augment.py
 textgen/augment/tokenizer.py
 textgen/augment/translate_api.py
 textgen/augment/word_level_augment.py
 textgen/augment/word_vocab.py
+textgen/chatglm/__init__.py
+textgen/chatglm/chatglm_model.py
+textgen/chatglm/chatglm_utils.py
 textgen/config/__init__.py
 textgen/config/global_args.py
 textgen/config/model_args.py
 textgen/custom_models/__init__.py
 textgen/custom_models/models.py
 textgen/data/HowNetPOSWord.txt
 textgen/data/stopwords.txt
@@ -26,17 +29,14 @@
 textgen/language_generation/language_generation_model.py
 textgen/language_generation/language_generation_utils.py
 textgen/language_modeling/__init__.py
 textgen/language_modeling/language_modeling_model.py
 textgen/language_modeling/language_modeling_utils.py
 textgen/language_modeling/songnet_model.py
 textgen/language_modeling/songnet_utils.py
-textgen/question_answering/__init__.py
-textgen/question_answering/question_answering_model.py
-textgen/question_answering/question_answering_utils.py
 textgen/seq2seq/__init__.py
 textgen/seq2seq/bart_seq2seq_model.py
 textgen/seq2seq/bart_seq2seq_utils.py
 textgen/seq2seq/conv_seq2seq_model.py
 textgen/seq2seq/data_reader.py
 textgen/seq2seq/seq2seq_model.py
 textgen/seq2seq/seq2seq_trainer.py
```

