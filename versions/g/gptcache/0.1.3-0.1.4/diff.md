# Comparing `tmp/gptcache-0.1.3.tar.gz` & `tmp/gptcache-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gptcache-0.1.3.tar", last modified: Thu Apr  6 02:22:47 2023, max compression
+gzip compressed data, was "gptcache-0.1.4.tar", last modified: Thu Apr  6 09:07:49 2023, max compression
```

## Comparing `gptcache-0.1.3.tar` & `gptcache-0.1.4.tar`

### file list

```diff
@@ -1,59 +1,60 @@
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.765907 gptcache-0.1.3/
--rw-r--r--   0 derek      (501) staff       (20)     1068 2023-04-05 13:14:02.000000 gptcache-0.1.3/LICENSE
--rw-r--r--   0 derek      (501) staff       (20)    13479 2023-04-06 02:22:47.765329 gptcache-0.1.3/PKG-INFO
--rw-r--r--   0 derek      (501) staff       (20)    12934 2023-04-06 02:17:21.000000 gptcache-0.1.3/README.md
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.638417 gptcache-0.1.3/gptcache/
--rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 11:32:02.000000 gptcache-0.1.3/gptcache/__init__.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.651844 gptcache-0.1.3/gptcache/adapter/
--rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 11:32:02.000000 gptcache-0.1.3/gptcache/adapter/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)     3652 2023-04-05 05:01:43.000000 gptcache-0.1.3/gptcache/adapter/adapter.py
--rw-r--r--   0 derek      (501) staff       (20)      539 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/adapter/langchain_llms.py
--rw-r--r--   0 derek      (501) staff       (20)     2599 2023-04-03 09:13:30.000000 gptcache-0.1.3/gptcache/adapter/openai.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.659937 gptcache-0.1.3/gptcache/cache/
--rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 11:32:02.000000 gptcache-0.1.3/gptcache/cache/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)     4007 2023-04-05 16:40:11.000000 gptcache-0.1.3/gptcache/cache/data_manager.py
--rw-r--r--   0 derek      (501) staff       (20)     1373 2023-04-04 15:55:01.000000 gptcache-0.1.3/gptcache/cache/eviction.py
--rw-r--r--   0 derek      (501) staff       (20)     2841 2023-04-05 13:14:02.000000 gptcache-0.1.3/gptcache/cache/factory.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.665106 gptcache-0.1.3/gptcache/cache/scalar_data/
--rw-r--r--   0 derek      (501) staff       (20)      775 2023-04-05 13:14:02.000000 gptcache-0.1.3/gptcache/cache/scalar_data/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)      846 2023-04-05 13:14:02.000000 gptcache-0.1.3/gptcache/cache/scalar_data/base.py
--rw-r--r--   0 derek      (501) staff       (20)     4293 2023-04-05 13:14:02.000000 gptcache-0.1.3/gptcache/cache/scalar_data/sqlalchemy.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.676002 gptcache-0.1.3/gptcache/cache/vector_data/
--rw-r--r--   0 derek      (501) staff       (20)      581 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/cache/vector_data/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)      623 2023-04-04 14:06:45.000000 gptcache-0.1.3/gptcache/cache/vector_data/base.py
--rw-r--r--   0 derek      (501) staff       (20)     1642 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/cache/vector_data/chroma.py
--rw-r--r--   0 derek      (501) staff       (20)     1601 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/cache/vector_data/faiss.py
--rw-r--r--   0 derek      (501) staff       (20)     5868 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/cache/vector_data/milvus.py
--rw-r--r--   0 derek      (501) staff       (20)     3739 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/core.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.693027 gptcache-0.1.3/gptcache/embedding/
--rw-r--r--   0 derek      (501) staff       (20)      914 2023-04-06 02:06:31.000000 gptcache-0.1.3/gptcache/embedding/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)     1731 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/embedding/cohere.py
--rw-r--r--   0 derek      (501) staff       (20)     2364 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/embedding/huggingface.py
--rw-r--r--   0 derek      (501) staff       (20)     2285 2023-04-06 02:06:31.000000 gptcache-0.1.3/gptcache/embedding/onnx.py
--rw-r--r--   0 derek      (501) staff       (20)     1904 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/embedding/openai.py
--rw-r--r--   0 derek      (501) staff       (20)     1478 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/embedding/sbert.py
--rw-r--r--   0 derek      (501) staff       (20)       51 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/embedding/string.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.702285 gptcache-0.1.3/gptcache/processor/
--rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 16:45:13.000000 gptcache-0.1.3/gptcache/processor/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)      162 2023-04-04 13:16:14.000000 gptcache-0.1.3/gptcache/processor/post.py
--rw-r--r--   0 derek      (501) staff       (20)      454 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/processor/pre.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.726718 gptcache-0.1.3/gptcache/similarity_evaluation/
--rw-r--r--   0 derek      (501) staff       (20)      228 2023-04-06 02:06:31.000000 gptcache-0.1.3/gptcache/similarity_evaluation/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)      825 2023-04-05 05:10:00.000000 gptcache-0.1.3/gptcache/similarity_evaluation/np.py
--rw-r--r--   0 derek      (501) staff       (20)     2908 2023-04-05 16:49:20.000000 gptcache-0.1.3/gptcache/similarity_evaluation/onnx.py
--rw-r--r--   0 derek      (501) staff       (20)      219 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/similarity_evaluation/similarity_evaluation.py
--rw-r--r--   0 derek      (501) staff       (20)      646 2023-04-05 12:40:20.000000 gptcache-0.1.3/gptcache/similarity_evaluation/simple.py
--rw-r--r--   0 derek      (501) staff       (20)      281 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/similarity_evaluation/string.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.764046 gptcache-0.1.3/gptcache/utils/
--rw-r--r--   0 derek      (501) staff       (20)     2982 2023-04-06 02:06:31.000000 gptcache-0.1.3/gptcache/utils/__init__.py
--rw-r--r--   0 derek      (501) staff       (20)      382 2023-04-06 02:08:54.000000 gptcache-0.1.3/gptcache/utils/dependency_control.py
--rw-r--r--   0 derek      (501) staff       (20)      508 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/utils/error.py
--rw-r--r--   0 derek      (501) staff       (20)      706 2023-04-04 16:37:34.000000 gptcache-0.1.3/gptcache/utils/lazy_import.py
-drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 02:22:47.644450 gptcache-0.1.3/gptcache.egg-info/
--rw-r--r--   0 derek      (501) staff       (20)    13479 2023-04-06 02:22:46.000000 gptcache-0.1.3/gptcache.egg-info/PKG-INFO
--rw-r--r--   0 derek      (501) staff       (20)     1418 2023-04-06 02:22:47.000000 gptcache-0.1.3/gptcache.egg-info/SOURCES.txt
--rw-r--r--   0 derek      (501) staff       (20)        1 2023-04-06 02:22:46.000000 gptcache-0.1.3/gptcache.egg-info/dependency_links.txt
--rw-r--r--   0 derek      (501) staff       (20)       24 2023-04-06 02:22:46.000000 gptcache-0.1.3/gptcache.egg-info/requires.txt
--rw-r--r--   0 derek      (501) staff       (20)        9 2023-04-06 02:22:46.000000 gptcache-0.1.3/gptcache.egg-info/top_level.txt
--rw-r--r--   0 derek      (501) staff       (20)       38 2023-04-06 02:22:47.766078 gptcache-0.1.3/setup.cfg
--rw-r--r--   0 derek      (501) staff       (20)     1115 2023-04-06 02:22:37.000000 gptcache-0.1.3/setup.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.999656 gptcache-0.1.4/
+-rw-r--r--   0 derek      (501) staff       (20)     1068 2023-04-05 13:14:02.000000 gptcache-0.1.4/LICENSE
+-rw-r--r--   0 derek      (501) staff       (20)    13519 2023-04-06 09:07:48.998927 gptcache-0.1.4/PKG-INFO
+-rw-r--r--   0 derek      (501) staff       (20)    12981 2023-04-06 08:05:48.000000 gptcache-0.1.4/README.md
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.914717 gptcache-0.1.4/gptcache/
+-rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 11:32:02.000000 gptcache-0.1.4/gptcache/__init__.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.923202 gptcache-0.1.4/gptcache/adapter/
+-rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 11:32:02.000000 gptcache-0.1.4/gptcache/adapter/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)     3652 2023-04-05 05:01:43.000000 gptcache-0.1.4/gptcache/adapter/adapter.py
+-rw-r--r--   0 derek      (501) staff       (20)      539 2023-04-05 16:49:20.000000 gptcache-0.1.4/gptcache/adapter/langchain_llms.py
+-rw-r--r--   0 derek      (501) staff       (20)     2599 2023-04-03 09:13:30.000000 gptcache-0.1.4/gptcache/adapter/openai.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.929750 gptcache-0.1.4/gptcache/cache/
+-rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 11:32:02.000000 gptcache-0.1.4/gptcache/cache/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)     5227 2023-04-06 08:03:27.000000 gptcache-0.1.4/gptcache/cache/data_manager.py
+-rw-r--r--   0 derek      (501) staff       (20)     1539 2023-04-06 08:03:27.000000 gptcache-0.1.4/gptcache/cache/eviction.py
+-rw-r--r--   0 derek      (501) staff       (20)     5754 2023-04-06 08:03:27.000000 gptcache-0.1.4/gptcache/cache/factory.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.934586 gptcache-0.1.4/gptcache/cache/scalar_data/
+-rw-r--r--   0 derek      (501) staff       (20)      775 2023-04-05 13:14:02.000000 gptcache-0.1.4/gptcache/cache/scalar_data/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)      903 2023-04-06 08:03:27.000000 gptcache-0.1.4/gptcache/cache/scalar_data/base.py
+-rw-r--r--   0 derek      (501) staff       (20)     4498 2023-04-06 08:03:27.000000 gptcache-0.1.4/gptcache/cache/scalar_data/sqlalchemy.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.947205 gptcache-0.1.4/gptcache/cache/vector_data/
+-rw-r--r--   0 derek      (501) staff       (20)      581 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/cache/vector_data/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)      623 2023-04-04 14:06:45.000000 gptcache-0.1.4/gptcache/cache/vector_data/base.py
+-rw-r--r--   0 derek      (501) staff       (20)     1642 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/cache/vector_data/chroma.py
+-rw-r--r--   0 derek      (501) staff       (20)     1601 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/cache/vector_data/faiss.py
+-rw-r--r--   0 derek      (501) staff       (20)     5864 2023-04-06 08:03:27.000000 gptcache-0.1.4/gptcache/cache/vector_data/milvus.py
+-rw-r--r--   0 derek      (501) staff       (20)     5756 2023-04-06 07:43:19.000000 gptcache-0.1.4/gptcache/core.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.961802 gptcache-0.1.4/gptcache/embedding/
+-rw-r--r--   0 derek      (501) staff       (20)     1083 2023-04-06 06:28:19.000000 gptcache-0.1.4/gptcache/embedding/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)     1731 2023-04-05 16:49:20.000000 gptcache-0.1.4/gptcache/embedding/cohere.py
+-rw-r--r--   0 derek      (501) staff       (20)     1591 2023-04-06 06:28:19.000000 gptcache-0.1.4/gptcache/embedding/fasttext.py
+-rw-r--r--   0 derek      (501) staff       (20)     2364 2023-04-05 16:49:20.000000 gptcache-0.1.4/gptcache/embedding/huggingface.py
+-rw-r--r--   0 derek      (501) staff       (20)     2285 2023-04-06 02:06:31.000000 gptcache-0.1.4/gptcache/embedding/onnx.py
+-rw-r--r--   0 derek      (501) staff       (20)     1904 2023-04-05 16:49:20.000000 gptcache-0.1.4/gptcache/embedding/openai.py
+-rw-r--r--   0 derek      (501) staff       (20)     1478 2023-04-05 16:49:20.000000 gptcache-0.1.4/gptcache/embedding/sbert.py
+-rw-r--r--   0 derek      (501) staff       (20)       51 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/embedding/string.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.969173 gptcache-0.1.4/gptcache/processor/
+-rw-r--r--   0 derek      (501) staff       (20)        0 2023-04-01 16:45:13.000000 gptcache-0.1.4/gptcache/processor/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)      162 2023-04-04 13:16:14.000000 gptcache-0.1.4/gptcache/processor/post.py
+-rw-r--r--   0 derek      (501) staff       (20)      454 2023-04-05 16:49:20.000000 gptcache-0.1.4/gptcache/processor/pre.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.992497 gptcache-0.1.4/gptcache/similarity_evaluation/
+-rw-r--r--   0 derek      (501) staff       (20)      228 2023-04-06 02:06:31.000000 gptcache-0.1.4/gptcache/similarity_evaluation/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)      646 2023-04-06 07:42:46.000000 gptcache-0.1.4/gptcache/similarity_evaluation/distance.py
+-rw-r--r--   0 derek      (501) staff       (20)      283 2023-04-06 07:42:46.000000 gptcache-0.1.4/gptcache/similarity_evaluation/exact_match.py
+-rw-r--r--   0 derek      (501) staff       (20)      825 2023-04-05 05:10:00.000000 gptcache-0.1.4/gptcache/similarity_evaluation/np.py
+-rw-r--r--   0 derek      (501) staff       (20)     2950 2023-04-06 07:05:05.000000 gptcache-0.1.4/gptcache/similarity_evaluation/onnx.py
+-rw-r--r--   0 derek      (501) staff       (20)      219 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/similarity_evaluation/similarity_evaluation.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.998211 gptcache-0.1.4/gptcache/utils/
+-rw-r--r--   0 derek      (501) staff       (20)     3171 2023-04-06 06:28:19.000000 gptcache-0.1.4/gptcache/utils/__init__.py
+-rw-r--r--   0 derek      (501) staff       (20)      382 2023-04-06 02:08:54.000000 gptcache-0.1.4/gptcache/utils/dependency_control.py
+-rw-r--r--   0 derek      (501) staff       (20)      508 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/utils/error.py
+-rw-r--r--   0 derek      (501) staff       (20)      706 2023-04-04 16:37:34.000000 gptcache-0.1.4/gptcache/utils/lazy_import.py
+drwxr-xr-x   0 derek      (501) staff       (20)        0 2023-04-06 09:07:48.918600 gptcache-0.1.4/gptcache.egg-info/
+-rw-r--r--   0 derek      (501) staff       (20)    13519 2023-04-06 09:07:48.000000 gptcache-0.1.4/gptcache.egg-info/PKG-INFO
+-rw-r--r--   0 derek      (501) staff       (20)     1456 2023-04-06 09:07:48.000000 gptcache-0.1.4/gptcache.egg-info/SOURCES.txt
+-rw-r--r--   0 derek      (501) staff       (20)        1 2023-04-06 09:07:48.000000 gptcache-0.1.4/gptcache.egg-info/dependency_links.txt
+-rw-r--r--   0 derek      (501) staff       (20)       24 2023-04-06 09:07:48.000000 gptcache-0.1.4/gptcache.egg-info/requires.txt
+-rw-r--r--   0 derek      (501) staff       (20)        9 2023-04-06 09:07:48.000000 gptcache-0.1.4/gptcache.egg-info/top_level.txt
+-rw-r--r--   0 derek      (501) staff       (20)       38 2023-04-06 09:07:48.999785 gptcache-0.1.4/setup.cfg
+-rw-r--r--   0 derek      (501) staff       (20)     1108 2023-04-06 09:07:44.000000 gptcache-0.1.4/setup.py
```

### Comparing `gptcache-0.1.3/LICENSE` & `gptcache-0.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/PKG-INFO` & `gptcache-0.1.4/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,39 +1,32 @@
-Metadata-Version: 2.1
-Name: gptcache
-Version: 0.1.3
-Summary: GPT Cache, a powerful caching library that can be used to speed up and lower the cost of chat applications that rely on the LLM service. GPT Cache works as a memcache for AIGC applications, similar to how Redis works for traditional applications.
-Home-page: https://github.com/zilliztech/gptcache
-Author: SimFG
-Author-email: bang.fu@zilliz.com
-License: http://www.apache.org/licenses/LICENSE-2.0
-Requires-Python: >=3.8.1
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
-# GPT Cache
+# GPTCache : A Library for Creating Semantic Cache to Store Responses from LLM Queries
+Boost LLM API Speed by 100x ⚡, Slash Costs by 10x 💰
 
 [![Release](https://img.shields.io/pypi/v/gptcache?label=Release&color)](https://pypi.org/project/gptcache/)
 [![CI](https://github.com/zilliztech/gptcache/actions/workflows/CI_main.yaml/badge.svg)](https://github.com/zilliztech/gptcache/actions/workflows/CI_main.yaml)
 [![pip download](https://img.shields.io/pypi/dm/gptcache.svg?color=bright-green)](https://pypi.org/project/gptcache/)
 [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit/)
 [![Discord](https://dcbadge.vercel.app/api/server/Q8C6WEjSWV?compact=true&style=flat)](https://discord.gg/Q8C6WEjSWV)
 
-## 🤠 What is GPT Cache?
+## Quick Install
+
+`pip install gptcache`
+
+## 🤠 What is GPTCache?
 
-Large Language Models (LLMs) are a promising and transformative technology that has rapidly advanced in recent years. These models are capable of generating natural language text and have numerous applications, including chatbots, language translation, and creative writing. However, as the size of these models increases, so do the costs and performance requirements needed to utilize them effectively. This has led to significant challenges in developing on top of large models such as ChatGPT.
+ChatGPT and various large language models (LLMs) possess remarkable adaptability, facilitating the creation of numerous applications. However, ChatGPT might exhibit slow response times, especially when dealing with a significant number of requests. Moreover, as your application grows in popularity and encounters higher traffic levels, the expenses related to ChatGPT API calls can become substantial. 
 
 To address this issue, we have developed GPT Cache, a project that focuses on caching responses from language models, also known as a semantic cache. The system offers two major benefits:
 
 1. Quick response to user requests: the caching system provides faster response times compared to large model inference, resulting in lower latency and faster response to user requests.
 2. Reduced service costs: most LLM services are currently charged based on the number of tokens. If user requests hit the cache, it can reduce the number of requests and lower service costs.
 
 ## 🤔 Why would GPT Cache be helpful?
 
-A good analogy for GptCache is to think of it as a more semantic version of Redis. In GptCache, hits are not limited to exact matches, but rather also include prompts and context similar to previous queries. We believe that the traditional cache design still works for AIGC applications for the following reasons:
+A good analogy for GptCache is to think of it as a more semantic version of Redis. In GptCache, hits are not limited to exact matches, but rather also include prompts and context similar to previous queries. We believe that the traditional cache design still works for AIGC applications due to the following reasons:
 
 - Locality is present everywhere. Like traditional application systems, AIGC applications also face similar hot topics. For instance, ChatGPT itself may be a popular topic among programmers.
 - For purpose-built SaaS services, users tend to ask questions within a specific domain, with both temporal and spatial locality.
 - By utilizing vector similarity search, it is possible to find a similarity relationship between questions and answers at a relatively low cost.
 
 We provide [benchmarks](https://github.com/zilliztech/gpt-cache/blob/main/examples/benchmark/benchmark_sqlite_faiss_onnx.py) to illustrate the concept. In semantic caching, there are three key measurement dimensions: false positives, false negatives, and hit latency. With the plugin-style implementation, users can easily tradeoff these three measurements according to their needs.
 
@@ -62,21 +55,21 @@
 # install the repo
 pip install -r requirements.txt
 python setup.py install
 ```
 
 ### example usage
 
-These examples will help you understand how to use exact and similar matching in caching. 
+These examples will help you understand how to use exact and similar matching with caching. 
 
-And before running the example, **make sure** the OPENAI_API_KEY environment variable is set by executing `echo $OPENAI_API_KEY`. 
+Before running the example, **make sure** the OPENAI_API_KEY environment variable is set by executing `echo $OPENAI_API_KEY`. 
 
-If it is not already set, it can be set by using `OPENAI_API_KEY=YOUR_API_KEY`. 
+If it is not already set, it can be set by using `export OPENAI_API_KEY=YOUR_API_KEY` on Unix/Linux/MacOS systems or `set OPENAI_API_KEY=YOUR_API_KEY` on Windows systems. 
 
-> It's important to note that this method is only effective temporarily, so if you want a permanent effect, you'll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at `/etc/profile`.
+> It is important to note that this method is only effective temporarily, so if you want a permanent effect, you'll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at `/etc/profile`.
 
 <details>
 
 <summary> Click to <strong>SHOW</strong> example code </summary>
 
 #### OpenAI API original usage
 
@@ -160,21 +153,21 @@
 
 def response_text(openai_resp):
     return openai_resp['choices'][0]['message']['content']
 
 from gptcache.core import cache
 from gptcache.adapter import openai
 from gptcache.embedding import Onnx
-from gptcache.cache.factory import get_ss_data_manager
-from gptcache.similarity_evaluation.simple import SearchDistanceEvaluation
+from gptcache.cache.factory import get_data_manager
+from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation
 
 print("Cache loading.....")
 
 onnx = Onnx()
-data_manager = get_ss_data_manager("sqlite", "faiss", dimension=onnx.dimension())
+data_manager = get_data_manager("sqlite", "faiss", dimension=onnx.dimension)
 cache.init(
     embedding_func=onnx.to_embeddings,
     data_manager=data_manager,
     similarity_evaluation=SearchDistanceEvaluation(),
     )
 cache.set_openai_key()
 
@@ -182,28 +175,27 @@
     "what's github",
     "can you explain what GitHub is",
     "can you tell me more about GitHub"
     "what is the purpose of GitHub"
 ]
 
 for question in questions:
-    for _ in range(2):
-        start_time = time.time()
-        response = openai.ChatCompletion.create(
-            model='gpt-3.5-turbo',
-            messages=[
-                {
-                    'role': 'user',
-                    'content': question
-                }
-            ],
-        )
-        print(f'Question: {question}')
-        print("Time consuming: {:.2f}s".format(time.time() - start_time))
-        print(f'Answer: {response_text(response)}\n')
+    start_time = time.time()
+    response = openai.ChatCompletion.create(
+        model='gpt-3.5-turbo',
+        messages=[
+            {
+                'role': 'user',
+                'content': question
+            }
+        ],
+    )
+    print(f'Question: {question}')
+    print("Time consuming: {:.2f}s".format(time.time() - start_time))
+    print(f'Answer: {response_text(response)}\n')
 ```
 
 </details>
 
 To use GPTCache exclusively, only the following lines of code are required, and there is no need to modify any existing code.
 
 ```python
@@ -212,15 +204,14 @@
 
 cache.init()
 cache.set_openai_key()
 ```
 
 More Docs：
 
-- [System Design, how it was constructed](docs/system.md)
 - [Features, all features currently supported by the cache](docs/feature.md)
 - [Examples, learn better custom caching](examples/README.md)
 
 ## 🤗 Modules
 
 ![GPTCache Struct](docs/GPTCacheStructure.png)
 
@@ -228,15 +219,15 @@
 The LLM Adapter is designed to integrate different LLM models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for ChatGPT integration.
   - [x] Support OpenAI chatGPT API.
   - [ ] Support other LLMs, such as Hugging Face Hub, Bard, Anthropic, and self-hosted models like LLaMa.
 - **Embedding Generator**: 
 This module is created to extract embeddings from requests for similarity search. GPTCache offers a generic interface that supports multiple embedding APIs, and presents a range of solutions to choose from. 
   - [x] Disable embedding. This will turn GPTCache into a keyword-matching cache.
   - [x] Support OpenAI embedding API.
-  - [x] Support [ONNX](https://onnx.ai/) with the paraphrase-albert-small-v2-onnx model.
+  - [x] Support [ONNX](https://onnx.ai/) with the GPTCache/paraphrase-albert-onnx model.
   - [x] Support [Hugging Face](https://huggingface.co/) embedding API.
   - [x] Support [Cohere](https://docs.cohere.ai/reference/embed) embedding API.
   - [ ] Support [fastText](https://fasttext.cc) embedding API.
   - [x] Support [SentenceTransformers](https://www.sbert.net) embedding API.
   - [ ] Support other embedding apis
 - **Cache Storage**:
 **Cache Storage** is where the response from LLMs, such as ChatGPT, is stored. Cached responses are retrieved to assist in evaluating similarity and are returned to the requester if there is a good semantic match. At present, GPTCache supports SQLite and offers a universally accessible interface for extension of this module.
@@ -245,15 +236,15 @@
   - [x] Support [MySQL](https://www.mysql.com/).
   - [x] Support [MariaDB](https://mariadb.org/).
   - [x] Support [SQL Server](https://www.microsoft.com/en-us/sql-server/).
   - [x] Support [Oracle](https://www.oracle.com/).
   - [ ] Support [MongoDB](https://www.mongodb.com/).
   - [ ] Support [Redis](https://redis.io/).
   - [ ] Support [Minio](https://min.io/).
-  - [ ] Support [Habse](https://hbase.apache.org//).
+  - [ ] Support [HBase](https://hbase.apache.org/).
   - [ ] Support [ElasticSearch](https://www.elastic.co/)
   - [ ] Support [zincsearch](https://zinc.dev/)
   - [ ] Support other storages
 - **Vector Store**:
 The **Vector Store** module helps find the K most similar requests from the input request's extracted embedding. The results can help assess similarity. GPTCache provides a user-friendly interface that supports various vector stores, including Milvus, Zilliz Cloud, and FAISS. More options will be available in the future.
   - [x] Support [Milvus](https://milvus.io/).
   - [x] Support [Zilliz Cloud](https://cloud.zilliz.com/).
@@ -268,15 +259,15 @@
   Currently, GPTCache makes decisions about evictions based solely on the number of lines. This approach can result in inaccurate resource evaluation and may cause out-of-memory (OOM) errors. We are actively investigating and developing a more sophisticated strategy.
     - [x] LRU eviction policy
     - [x] FIFO eviction policy
     - [ ] More complicated eviction policies
 - **Similarity Evaluator**: 
 This module collects data from both the **Cache Storage** and **Vector Store**, and uses various strategies to determine the similarity between the input request and the requests from the **Vector Store**. Based on this similarity, it determines whether a request matches the cache. GPTCache provides a standardized interface for integrating various strategies, along with a collection of implementations to use. The following similarity definitions are currently supported or will be supported in the future:
   - [x] The distance we obtain from the **Vector Store**.
-  - [x] A model-based similarity determined using the albert_duplicate model from [ONNX](https://onnx.ai/).
+  - [x] A model-based similarity determined using the GPTCache/albert-duplicate-onnx model from [ONNX](https://onnx.ai/).
   - [x] Exact matches between the input request and the requests obtained from the **Vector Store**.
   - [x] Distance represented by applying linalg.norm from numpy to the embeddings.
   - [ ] BM25 and other similarity measurements
   - [ ] Support other models
  
   
   **Note**:Not all combinations of different modules may be compatible with each other. For instance, if we disable the **Embedding Extractor**, the **Vector Store** may not function as intended. We are currently working on implementing a combination sanity check for **GPTCache**.
```

### Comparing `gptcache-0.1.3/README.md` & `gptcache-0.1.4/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,27 +1,44 @@
-# GPT Cache
+Metadata-Version: 2.1
+Name: gptcache
+Version: 0.1.4
+Summary: GPT Cache, a powerful caching library that can be used to speed up and lower the cost of chat applications that rely on the LLM service. GPT Cache works as a memcache for AIGC applications, similar to how Redis works for traditional applications.
+Home-page: https://github.com/zilliztech/GPTCache
+Author: SimFG
+Author-email: bang.fu@zilliz.com
+License: https://opensource.org/license/mit/
+Requires-Python: >=3.8.1
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
+# GPTCache : A Library for Creating Semantic Cache to Store Responses from LLM Queries
+Boost LLM API Speed by 100x ⚡, Slash Costs by 10x 💰
 
 [![Release](https://img.shields.io/pypi/v/gptcache?label=Release&color)](https://pypi.org/project/gptcache/)
 [![CI](https://github.com/zilliztech/gptcache/actions/workflows/CI_main.yaml/badge.svg)](https://github.com/zilliztech/gptcache/actions/workflows/CI_main.yaml)
 [![pip download](https://img.shields.io/pypi/dm/gptcache.svg?color=bright-green)](https://pypi.org/project/gptcache/)
 [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit/)
 [![Discord](https://dcbadge.vercel.app/api/server/Q8C6WEjSWV?compact=true&style=flat)](https://discord.gg/Q8C6WEjSWV)
 
-## 🤠 What is GPT Cache?
+## Quick Install
+
+`pip install gptcache`
+
+## 🤠 What is GPTCache?
 
-Large Language Models (LLMs) are a promising and transformative technology that has rapidly advanced in recent years. These models are capable of generating natural language text and have numerous applications, including chatbots, language translation, and creative writing. However, as the size of these models increases, so do the costs and performance requirements needed to utilize them effectively. This has led to significant challenges in developing on top of large models such as ChatGPT.
+ChatGPT and various large language models (LLMs) possess remarkable adaptability, facilitating the creation of numerous applications. However, ChatGPT might exhibit slow response times, especially when dealing with a significant number of requests. Moreover, as your application grows in popularity and encounters higher traffic levels, the expenses related to ChatGPT API calls can become substantial. 
 
 To address this issue, we have developed GPT Cache, a project that focuses on caching responses from language models, also known as a semantic cache. The system offers two major benefits:
 
 1. Quick response to user requests: the caching system provides faster response times compared to large model inference, resulting in lower latency and faster response to user requests.
 2. Reduced service costs: most LLM services are currently charged based on the number of tokens. If user requests hit the cache, it can reduce the number of requests and lower service costs.
 
 ## 🤔 Why would GPT Cache be helpful?
 
-A good analogy for GptCache is to think of it as a more semantic version of Redis. In GptCache, hits are not limited to exact matches, but rather also include prompts and context similar to previous queries. We believe that the traditional cache design still works for AIGC applications for the following reasons:
+A good analogy for GptCache is to think of it as a more semantic version of Redis. In GptCache, hits are not limited to exact matches, but rather also include prompts and context similar to previous queries. We believe that the traditional cache design still works for AIGC applications due to the following reasons:
 
 - Locality is present everywhere. Like traditional application systems, AIGC applications also face similar hot topics. For instance, ChatGPT itself may be a popular topic among programmers.
 - For purpose-built SaaS services, users tend to ask questions within a specific domain, with both temporal and spatial locality.
 - By utilizing vector similarity search, it is possible to find a similarity relationship between questions and answers at a relatively low cost.
 
 We provide [benchmarks](https://github.com/zilliztech/gpt-cache/blob/main/examples/benchmark/benchmark_sqlite_faiss_onnx.py) to illustrate the concept. In semantic caching, there are three key measurement dimensions: false positives, false negatives, and hit latency. With the plugin-style implementation, users can easily tradeoff these three measurements according to their needs.
 
@@ -50,21 +67,21 @@
 # install the repo
 pip install -r requirements.txt
 python setup.py install
 ```
 
 ### example usage
 
-These examples will help you understand how to use exact and similar matching in caching. 
+These examples will help you understand how to use exact and similar matching with caching. 
 
-And before running the example, **make sure** the OPENAI_API_KEY environment variable is set by executing `echo $OPENAI_API_KEY`. 
+Before running the example, **make sure** the OPENAI_API_KEY environment variable is set by executing `echo $OPENAI_API_KEY`. 
 
-If it is not already set, it can be set by using `OPENAI_API_KEY=YOUR_API_KEY`. 
+If it is not already set, it can be set by using `export OPENAI_API_KEY=YOUR_API_KEY` on Unix/Linux/MacOS systems or `set OPENAI_API_KEY=YOUR_API_KEY` on Windows systems. 
 
-> It's important to note that this method is only effective temporarily, so if you want a permanent effect, you'll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at `/etc/profile`.
+> It is important to note that this method is only effective temporarily, so if you want a permanent effect, you'll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at `/etc/profile`.
 
 <details>
 
 <summary> Click to <strong>SHOW</strong> example code </summary>
 
 #### OpenAI API original usage
 
@@ -148,21 +165,21 @@
 
 def response_text(openai_resp):
     return openai_resp['choices'][0]['message']['content']
 
 from gptcache.core import cache
 from gptcache.adapter import openai
 from gptcache.embedding import Onnx
-from gptcache.cache.factory import get_ss_data_manager
-from gptcache.similarity_evaluation.simple import SearchDistanceEvaluation
+from gptcache.cache.factory import get_data_manager
+from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation
 
 print("Cache loading.....")
 
 onnx = Onnx()
-data_manager = get_ss_data_manager("sqlite", "faiss", dimension=onnx.dimension())
+data_manager = get_data_manager("sqlite", "faiss", dimension=onnx.dimension)
 cache.init(
     embedding_func=onnx.to_embeddings,
     data_manager=data_manager,
     similarity_evaluation=SearchDistanceEvaluation(),
     )
 cache.set_openai_key()
 
@@ -170,28 +187,27 @@
     "what's github",
     "can you explain what GitHub is",
     "can you tell me more about GitHub"
     "what is the purpose of GitHub"
 ]
 
 for question in questions:
-    for _ in range(2):
-        start_time = time.time()
-        response = openai.ChatCompletion.create(
-            model='gpt-3.5-turbo',
-            messages=[
-                {
-                    'role': 'user',
-                    'content': question
-                }
-            ],
-        )
-        print(f'Question: {question}')
-        print("Time consuming: {:.2f}s".format(time.time() - start_time))
-        print(f'Answer: {response_text(response)}\n')
+    start_time = time.time()
+    response = openai.ChatCompletion.create(
+        model='gpt-3.5-turbo',
+        messages=[
+            {
+                'role': 'user',
+                'content': question
+            }
+        ],
+    )
+    print(f'Question: {question}')
+    print("Time consuming: {:.2f}s".format(time.time() - start_time))
+    print(f'Answer: {response_text(response)}\n')
 ```
 
 </details>
 
 To use GPTCache exclusively, only the following lines of code are required, and there is no need to modify any existing code.
 
 ```python
@@ -200,15 +216,14 @@
 
 cache.init()
 cache.set_openai_key()
 ```
 
 More Docs：
 
-- [System Design, how it was constructed](docs/system.md)
 - [Features, all features currently supported by the cache](docs/feature.md)
 - [Examples, learn better custom caching](examples/README.md)
 
 ## 🤗 Modules
 
 ![GPTCache Struct](docs/GPTCacheStructure.png)
 
@@ -216,15 +231,15 @@
 The LLM Adapter is designed to integrate different LLM models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for ChatGPT integration.
   - [x] Support OpenAI chatGPT API.
   - [ ] Support other LLMs, such as Hugging Face Hub, Bard, Anthropic, and self-hosted models like LLaMa.
 - **Embedding Generator**: 
 This module is created to extract embeddings from requests for similarity search. GPTCache offers a generic interface that supports multiple embedding APIs, and presents a range of solutions to choose from. 
   - [x] Disable embedding. This will turn GPTCache into a keyword-matching cache.
   - [x] Support OpenAI embedding API.
-  - [x] Support [ONNX](https://onnx.ai/) with the paraphrase-albert-small-v2-onnx model.
+  - [x] Support [ONNX](https://onnx.ai/) with the GPTCache/paraphrase-albert-onnx model.
   - [x] Support [Hugging Face](https://huggingface.co/) embedding API.
   - [x] Support [Cohere](https://docs.cohere.ai/reference/embed) embedding API.
   - [ ] Support [fastText](https://fasttext.cc) embedding API.
   - [x] Support [SentenceTransformers](https://www.sbert.net) embedding API.
   - [ ] Support other embedding apis
 - **Cache Storage**:
 **Cache Storage** is where the response from LLMs, such as ChatGPT, is stored. Cached responses are retrieved to assist in evaluating similarity and are returned to the requester if there is a good semantic match. At present, GPTCache supports SQLite and offers a universally accessible interface for extension of this module.
@@ -233,15 +248,15 @@
   - [x] Support [MySQL](https://www.mysql.com/).
   - [x] Support [MariaDB](https://mariadb.org/).
   - [x] Support [SQL Server](https://www.microsoft.com/en-us/sql-server/).
   - [x] Support [Oracle](https://www.oracle.com/).
   - [ ] Support [MongoDB](https://www.mongodb.com/).
   - [ ] Support [Redis](https://redis.io/).
   - [ ] Support [Minio](https://min.io/).
-  - [ ] Support [Habse](https://hbase.apache.org//).
+  - [ ] Support [HBase](https://hbase.apache.org/).
   - [ ] Support [ElasticSearch](https://www.elastic.co/)
   - [ ] Support [zincsearch](https://zinc.dev/)
   - [ ] Support other storages
 - **Vector Store**:
 The **Vector Store** module helps find the K most similar requests from the input request's extracted embedding. The results can help assess similarity. GPTCache provides a user-friendly interface that supports various vector stores, including Milvus, Zilliz Cloud, and FAISS. More options will be available in the future.
   - [x] Support [Milvus](https://milvus.io/).
   - [x] Support [Zilliz Cloud](https://cloud.zilliz.com/).
@@ -256,15 +271,15 @@
   Currently, GPTCache makes decisions about evictions based solely on the number of lines. This approach can result in inaccurate resource evaluation and may cause out-of-memory (OOM) errors. We are actively investigating and developing a more sophisticated strategy.
     - [x] LRU eviction policy
     - [x] FIFO eviction policy
     - [ ] More complicated eviction policies
 - **Similarity Evaluator**: 
 This module collects data from both the **Cache Storage** and **Vector Store**, and uses various strategies to determine the similarity between the input request and the requests from the **Vector Store**. Based on this similarity, it determines whether a request matches the cache. GPTCache provides a standardized interface for integrating various strategies, along with a collection of implementations to use. The following similarity definitions are currently supported or will be supported in the future:
   - [x] The distance we obtain from the **Vector Store**.
-  - [x] A model-based similarity determined using the albert_duplicate model from [ONNX](https://onnx.ai/).
+  - [x] A model-based similarity determined using the GPTCache/albert-duplicate-onnx model from [ONNX](https://onnx.ai/).
   - [x] Exact matches between the input request and the requests obtained from the **Vector Store**.
   - [x] Distance represented by applying linalg.norm from numpy to the embeddings.
   - [ ] BM25 and other similarity measurements
   - [ ] Support other models
  
   
   **Note**:Not all combinations of different modules may be compatible with each other. For instance, if we disable the **Embedding Extractor**, the **Vector Store** may not function as intended. We are currently working on implementing a combination sanity check for **GPTCache**.
```

### Comparing `gptcache-0.1.3/gptcache/adapter/adapter.py` & `gptcache-0.1.4/gptcache/adapter/adapter.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/adapter/langchain_llms.py` & `gptcache-0.1.4/gptcache/adapter/langchain_llms.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/adapter/openai.py` & `gptcache-0.1.4/gptcache/adapter/openai.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/cache/eviction.py` & `gptcache-0.1.4/gptcache/cache/eviction.py`

 * *Files 12% similar despite different names*

```diff
@@ -2,17 +2,18 @@
 
 
 class EvictionManager:
     MAX_MARK_COUNT = 5000
     MAX_MARK_RATE = 0.1
     BATCH_SIZE = 100000
 
-    def __init__(self, scalar_storage, vector_base):
+    def __init__(self, scalar_storage, vector_base, policy="LRU"):
         self._scalar_storage = scalar_storage
         self._vector_base = vector_base
+        self._policy = policy
 
     def check_evict(self):
         mark_count = self._scalar_storage.count(state=-1)
         all_count = self._scalar_storage.count(is_all=True)
         if mark_count > self.MAX_MARK_COUNT or mark_count / all_count > self.MAX_MARK_RATE:
             return True
         return False
@@ -30,10 +31,13 @@
         while offset < count:
             data = self._scalar_storage.get_embedding_data(offset, self.BATCH_SIZE)
             np_data = [np.frombuffer(d[0], np.float32) for d in data]
             self._vector_base.rebuild(np_data)
             offset += self.BATCH_SIZE
 
     def soft_evict(self, count):
-        marked_keys = self._scalar_storage.get_old_access(count)
+        if self._policy == "FIFO":
+            marked_keys = self._scalar_storage.get_old_create(count)
+        else:
+            marked_keys = self._scalar_storage.get_old_access(count)
         marked_keys = [i[0] for i in marked_keys]
         self._scalar_storage.update_state(marked_keys)
```

### Comparing `gptcache-0.1.3/gptcache/cache/scalar_data/__init__.py` & `gptcache-0.1.4/gptcache/cache/scalar_data/__init__.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/cache/scalar_data/base.py` & `gptcache-0.1.4/gptcache/cache/vector_data/base.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,41 +1,36 @@
-from abc import ABCMeta, abstractmethod
+from abc import ABC, abstractmethod
+from typing import List
+from enum import Enum
 
-import numpy as np
 
-TABLE_NAME = 'cache_table'
-TABLE_NAME_SEQ = 'cache_table_sequence'
+class ClearStrategy(Enum):
+    REBUILD = 0
+    DELETE = 1
 
 
-class ScalarStorage(metaclass=ABCMeta):
-    """
-    BaseStorage for scalar data.
-    """
-    @abstractmethod
-    def init(self, **kwargs): pass
-
-    @abstractmethod
-    def create(self, **kwargs): pass
-
-    @abstractmethod
-    def insert(self, key, data, reply, embedding_data: np.ndarray = None): pass
+class VectorBase(ABC):
 
-    @abstractmethod
-    def get_data_by_id(self, key): pass
+    def init(self, **kwargs):
+        pass
 
     @abstractmethod
-    def get_embedding_data(self, limit, offset): pass
+    def add(self, key: str, data: 'ndarray'):
+        pass
 
     @abstractmethod
-    def remove_by_state(self): pass
+    def search(self, data: 'ndarray'):
+        pass
 
     @abstractmethod
-    def update_access_time(self, keys): pass
+    def clear_strategy(self):
+        pass    
 
-    @abstractmethod
-    def update_state(self, keys): pass
+    def rebuild(self) -> bool:
+        raise NotImplementedError
 
-    @abstractmethod
-    def count(self): pass
+    def delete(self, ids) -> bool:
+        raise NotImplementedError
 
     @abstractmethod
-    def close(self): pass
+    def close(self):
+        pass
```

### Comparing `gptcache-0.1.3/gptcache/cache/scalar_data/sqlalchemy.py` & `gptcache-0.1.4/gptcache/cache/scalar_data/sqlalchemy.py`

 * *Files 7% similar despite different names*

```diff
@@ -4,64 +4,67 @@
 import numpy as np
 from datetime import datetime
 from sqlalchemy import func, create_engine, Column, Sequence
 from sqlalchemy.types import String, DateTime, LargeBinary, Integer
 from sqlalchemy.orm import sessionmaker
 from sqlalchemy.ext.declarative import declarative_base
 
-from .base import ScalarStorage, TABLE_NAME, TABLE_NAME_SEQ
+from .base import CacheStorage
 
 Base = declarative_base()
 
 
-class CacheTable(Base):
-    """
-    cache_table
-    """
-    __tablename__ = TABLE_NAME
+def get_model(table_name, db_type):
+    class CacheTable(Base):
+        """
+        cache_table
+        """
+        __tablename__ = table_name
+        __table_args__ = {'extend_existing': True}
+
+        uid = Column(Integer, primary_key=True, autoincrement=True)
+        id = Column(String(500), nullable=False)
+        data = Column(String(1000), nullable=False)
+        reply = Column(String(1000), nullable=False)
+        create_on = Column(DateTime, default=datetime.now)
+        last_access = Column(DateTime, default=datetime.now)
+        embedding_data = Column(LargeBinary, nullable=True)
+        state = Column(Integer, default=0)
+
+    class CacheTableSequence(Base):
+        """
+        cache_table sequence
+        """
+        __tablename__ = table_name
+        __table_args__ = {'extend_existing': True}
+
+        uid = Column(Integer, Sequence('id_seq', start=1), primary_key=True, autoincrement=True)
+        id = Column(String(500), nullable=False)
+        data = Column(String(1000), nullable=False)
+        reply = Column(String(1000), nullable=False)
+        create_on = Column(DateTime, default=datetime.now)
+        last_access = Column(DateTime, default=datetime.now)
+        embedding_data = Column(LargeBinary, nullable=True)
+        state = Column(Integer, default=0)
+
+    if db_type == 'oracle':
+        return CacheTableSequence
+    else:
+        return CacheTable
 
-    uid = Column(Integer, primary_key=True, autoincrement=True)
-    id = Column(String(500), nullable=False)
-    data = Column(String(1000), nullable=False)
-    reply = Column(String(1000), nullable=False)
-    create_on = Column(DateTime, default=datetime.now)
-    last_access = Column(DateTime, default=datetime.now)
-    embedding_data = Column(LargeBinary, nullable=True)
-    state = Column(Integer, default=0)
 
-
-class CacheTableSequence(Base):
-    """
-    cache_table_sequence
-    """
-    __tablename__ = TABLE_NAME_SEQ
-
-    uid = Column(Integer, Sequence('id_seq', start=1), primary_key=True, autoincrement=True)
-    id = Column(String(500), nullable=False)
-    data = Column(String(1000), nullable=False)
-    reply = Column(String(1000), nullable=False)
-    create_on = Column(DateTime, default=datetime.now)
-    last_access = Column(DateTime, default=datetime.now)
-    embedding_data = Column(LargeBinary, nullable=True)
-    state = Column(Integer, default=0)
-
-
-class SQLDataBase(ScalarStorage):
+class SQLDataBase(CacheStorage):
     """
     Using sqlalchemy to manage SQLite, PostgreSQL, MySQL, MariaDB, SQL Server and Oracle.
     """
-    def __init__(self, url: str = 'sqlite:///./gpt_cache.db', db_type: str = 'sqlite'):
+    def __init__(self, db_type: str = 'sqlite', url: str = 'sqlite:///./gptcache.db', table_name: str = 'gptcache'):
         self._url = url
         self._engine = None
         self._session = None
-        self._db_type = db_type
-        if self._db_type == 'oracle':
-            self._model = CacheTableSequence
-        else:
-            self._model = CacheTable
+        self._model = get_model(table_name, db_type)
         self.init()
 
     def init(self):
         self._engine = create_engine(self._url)
         Session = sessionmaker(bind=self._engine)
         self._session = Session()
         self.create()
@@ -71,18 +74,14 @@
 
     def insert(self, key, data, reply, embedding_data: np.ndarray = None):
         embedding_data = embedding_data.tobytes()
         model_obj = self._model(id=key, data=data, reply=reply, embedding_data=embedding_data)
         self._session.add(model_obj)
         self._session.commit()
 
-    def get_data_by_ids(self, keys):
-        res = self._session.query(self._model.data, self._model.reply).filter(self._model.id.in_(keys)).filter(self._model.state == 0).all()
-        return res
-
     def get_data_by_id(self, key):
         res = self._session.query(self._model.data, self._model.reply).filter(self._model.id == key).filter(self._model.state == 0).first()
         return res
 
     def get_ids_by_state(self, state):
         res = self._session.query(self._model.id).filter(self._model.state == state).all()
         return res
@@ -92,25 +91,28 @@
         return res
 
     def update_access_time(self, key):
         self._session.query(self._model).filter(self._model.id == key).update({'last_access': datetime.now()})
         self._session.commit()
 
     def get_old_access(self, count):
-        res = self._session.query(self._model.id).order_by(self._model.last_access.asc()).limit(count).all()
+        res = self._session.query(self._model.id).order_by(self._model.last_access.asc()).filter(self._model.state == 0).limit(count).all()
         return res
 
-    def update_state(self, keys, state: int = -1):
-        self._session.query(self._model).filter(self._model.id.in_(keys)).update({'state': state})
+    def get_old_create(self, count):
+        res = self._session.query(self._model.id).order_by(self._model.create_on.asc()).filter(self._model.state == 0).limit(count).all()
+        return res
+
+    def update_state(self, keys):
+        self._session.query(self._model).filter(self._model.id.in_(keys)).update({'state': -1})
         self._session.commit()
 
     def remove_by_state(self):
-        res = self._session.query(self._model).filter(self._model.state == -1).delete()
+        self._session.query(self._model).filter(self._model.state == -1).delete()
         self._session.commit()
-        return res
 
     def count(self, state: int = 0, is_all: bool = False):
         if is_all:
             return self._session.query(func.count(self._model.id)).scalar()
         return self._session.query(func.count(self._model.id)).filter(self._model.state == state).scalar()
 
     def close(self):
```

### Comparing `gptcache-0.1.3/gptcache/cache/vector_data/__init__.py` & `gptcache-0.1.4/gptcache/cache/vector_data/__init__.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/cache/vector_data/chroma.py` & `gptcache-0.1.4/gptcache/cache/vector_data/chroma.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/cache/vector_data/faiss.py` & `gptcache-0.1.4/gptcache/cache/vector_data/faiss.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/cache/vector_data/milvus.py` & `gptcache-0.1.4/gptcache/cache/vector_data/milvus.py`

 * *Files 1% similar despite different names*

```diff
@@ -141,15 +141,15 @@
 
         search_tuples = []
         for query_row in query_result:
             search_tuples.append((pks[query_row["pk"]], np.array(query_row["embedding"])))
         return search_tuples
 
     def clear_strategy(self):
-        return ClearStrategy.DELETE    
+        return ClearStrategy.DELETE
 
     def delete(self, ids):
         pks = ",".join(['"' + x + '"' for x in ids])
         self.col.delete(f"pk in [{pks}]")
 
     def close(self):
         self.col.flush(_async=True)
```

### Comparing `gptcache-0.1.3/gptcache/embedding/__init__.py` & `gptcache-0.1.4/gptcache/embedding/__init__.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 
-__all__ = ['OpenAI', 'Huggingface', 'SBERT', 'Cohere', 'Onnx']
+__all__ = ['OpenAI', 'Huggingface', 'SBERT', 'Cohere', 'Onnx', 'FastText']
 
 
 from gptcache.utils.lazy_import import LazyImport
 
 openai = LazyImport('openai', globals(), 'gptcache.embedding.openai')
 huggingface = LazyImport('huggingface', globals(), 'gptcache.embedding.huggingface')
 sbert = LazyImport('sbert', globals(), 'gptcache.embedding.sbert')
 onnx = LazyImport('onnx', globals(), 'gptcache.embedding.onnx')
 cohere = LazyImport('cohere', globals(), 'gptcache.embedding.cohere')
+fasttext = LazyImport('fasttext', globals(), 'gptcache.embedding.fasttext')
 
 
 def Cohere(model="large", api_key=None):
     return cohere.Cohere(model, api_key)
 
 def OpenAI(model="text-embedding-ada-002", api_key=None):
     return openai.OpenAI(model, api_key)
@@ -21,7 +22,10 @@
     return huggingface.Huggingface(model)
 
 def SBERT(model="all-MiniLM-L6-v2"):
     return sbert.SBERT(model)
 
 def Onnx(model="GPTCache/paraphrase-albert-onnx"):
     return onnx.Onnx(model)
+
+def FastText(model="large", dim=None):
+    return fasttext.FastText(model, dim)
```

### Comparing `gptcache-0.1.3/gptcache/embedding/cohere.py` & `gptcache-0.1.4/gptcache/embedding/cohere.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/embedding/huggingface.py` & `gptcache-0.1.4/gptcache/embedding/huggingface.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/embedding/onnx.py` & `gptcache-0.1.4/gptcache/embedding/onnx.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/embedding/openai.py` & `gptcache-0.1.4/gptcache/embedding/openai.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/embedding/sbert.py` & `gptcache-0.1.4/gptcache/embedding/sbert.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/similarity_evaluation/np.py` & `gptcache-0.1.4/gptcache/similarity_evaluation/np.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/similarity_evaluation/onnx.py` & `gptcache-0.1.4/gptcache/similarity_evaluation/onnx.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,13 @@
-from gptcache.utils import import_onnxruntime, import_huggingface_hub
+from gptcache.utils import import_onnxruntime, import_huggingface_hub, import_huggingface
 from .similarity_evaluation import SimilarityEvaluation
+
 import_onnxruntime()
 import_huggingface_hub()
+import_huggingface()
 import numpy as np
 import os
 from transformers import AutoTokenizer
 from pathlib import Path
 from huggingface_hub import hf_hub_download
 from typing import List
 import onnxruntime
```

### Comparing `gptcache-0.1.3/gptcache/similarity_evaluation/simple.py` & `gptcache-0.1.4/gptcache/similarity_evaluation/distance.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache/utils/__init__.py` & `gptcache-0.1.4/gptcache/utils/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,14 @@
 __all__ = ['import_pymilvus', 'import_huggingface_hub',
            'import_faiss', 'import_chromadb',
            'import_sqlalchemy', 'import_sql_client',
            'import_huggingface', 'import_torch',
-           'import_sbert', 'import_onnxruntime', 'import_cohere' ]
+           'import_sbert', 'import_onnxruntime',
+           'import_cohere', 'import_fasttext'
+           ]
 from .dependency_control import prompt_install
 
 
 # pylint: disable=unused-import
 # pylint: disable=ungrouped-imports
 # pragma: no cover
 def import_pymilvus():
@@ -26,14 +28,21 @@
 def import_cohere():
     try:
         import cohere
     except ModuleNotFoundError:
         prompt_install('cohere')
         import cohere
 
+def import_fasttext():
+    try:
+        import fasttext
+    except ModuleNotFoundError:
+        prompt_install('fasttext')
+        import fasttext
+
 def import_huggingface():
     try:
         import transformers
     except ModuleNotFoundError as e:
         prompt_install('transformers')
         import transformers
```

### Comparing `gptcache-0.1.3/gptcache/utils/lazy_import.py` & `gptcache-0.1.4/gptcache/utils/lazy_import.py`

 * *Files identical despite different names*

### Comparing `gptcache-0.1.3/gptcache.egg-info/PKG-INFO` & `gptcache-0.1.4/gptcache.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,39 +1,44 @@
 Metadata-Version: 2.1
 Name: gptcache
-Version: 0.1.3
+Version: 0.1.4
 Summary: GPT Cache, a powerful caching library that can be used to speed up and lower the cost of chat applications that rely on the LLM service. GPT Cache works as a memcache for AIGC applications, similar to how Redis works for traditional applications.
-Home-page: https://github.com/zilliztech/gptcache
+Home-page: https://github.com/zilliztech/GPTCache
 Author: SimFG
 Author-email: bang.fu@zilliz.com
-License: http://www.apache.org/licenses/LICENSE-2.0
+License: https://opensource.org/license/mit/
 Requires-Python: >=3.8.1
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
-# GPT Cache
+# GPTCache : A Library for Creating Semantic Cache to Store Responses from LLM Queries
+Boost LLM API Speed by 100x ⚡, Slash Costs by 10x 💰
 
 [![Release](https://img.shields.io/pypi/v/gptcache?label=Release&color)](https://pypi.org/project/gptcache/)
 [![CI](https://github.com/zilliztech/gptcache/actions/workflows/CI_main.yaml/badge.svg)](https://github.com/zilliztech/gptcache/actions/workflows/CI_main.yaml)
 [![pip download](https://img.shields.io/pypi/dm/gptcache.svg?color=bright-green)](https://pypi.org/project/gptcache/)
 [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/mit/)
 [![Discord](https://dcbadge.vercel.app/api/server/Q8C6WEjSWV?compact=true&style=flat)](https://discord.gg/Q8C6WEjSWV)
 
-## 🤠 What is GPT Cache?
+## Quick Install
 
-Large Language Models (LLMs) are a promising and transformative technology that has rapidly advanced in recent years. These models are capable of generating natural language text and have numerous applications, including chatbots, language translation, and creative writing. However, as the size of these models increases, so do the costs and performance requirements needed to utilize them effectively. This has led to significant challenges in developing on top of large models such as ChatGPT.
+`pip install gptcache`
+
+## 🤠 What is GPTCache?
+
+ChatGPT and various large language models (LLMs) possess remarkable adaptability, facilitating the creation of numerous applications. However, ChatGPT might exhibit slow response times, especially when dealing with a significant number of requests. Moreover, as your application grows in popularity and encounters higher traffic levels, the expenses related to ChatGPT API calls can become substantial. 
 
 To address this issue, we have developed GPT Cache, a project that focuses on caching responses from language models, also known as a semantic cache. The system offers two major benefits:
 
 1. Quick response to user requests: the caching system provides faster response times compared to large model inference, resulting in lower latency and faster response to user requests.
 2. Reduced service costs: most LLM services are currently charged based on the number of tokens. If user requests hit the cache, it can reduce the number of requests and lower service costs.
 
 ## 🤔 Why would GPT Cache be helpful?
 
-A good analogy for GptCache is to think of it as a more semantic version of Redis. In GptCache, hits are not limited to exact matches, but rather also include prompts and context similar to previous queries. We believe that the traditional cache design still works for AIGC applications for the following reasons:
+A good analogy for GptCache is to think of it as a more semantic version of Redis. In GptCache, hits are not limited to exact matches, but rather also include prompts and context similar to previous queries. We believe that the traditional cache design still works for AIGC applications due to the following reasons:
 
 - Locality is present everywhere. Like traditional application systems, AIGC applications also face similar hot topics. For instance, ChatGPT itself may be a popular topic among programmers.
 - For purpose-built SaaS services, users tend to ask questions within a specific domain, with both temporal and spatial locality.
 - By utilizing vector similarity search, it is possible to find a similarity relationship between questions and answers at a relatively low cost.
 
 We provide [benchmarks](https://github.com/zilliztech/gpt-cache/blob/main/examples/benchmark/benchmark_sqlite_faiss_onnx.py) to illustrate the concept. In semantic caching, there are three key measurement dimensions: false positives, false negatives, and hit latency. With the plugin-style implementation, users can easily tradeoff these three measurements according to their needs.
 
@@ -62,21 +67,21 @@
 # install the repo
 pip install -r requirements.txt
 python setup.py install
 ```
 
 ### example usage
 
-These examples will help you understand how to use exact and similar matching in caching. 
+These examples will help you understand how to use exact and similar matching with caching. 
 
-And before running the example, **make sure** the OPENAI_API_KEY environment variable is set by executing `echo $OPENAI_API_KEY`. 
+Before running the example, **make sure** the OPENAI_API_KEY environment variable is set by executing `echo $OPENAI_API_KEY`. 
 
-If it is not already set, it can be set by using `OPENAI_API_KEY=YOUR_API_KEY`. 
+If it is not already set, it can be set by using `export OPENAI_API_KEY=YOUR_API_KEY` on Unix/Linux/MacOS systems or `set OPENAI_API_KEY=YOUR_API_KEY` on Windows systems. 
 
-> It's important to note that this method is only effective temporarily, so if you want a permanent effect, you'll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at `/etc/profile`.
+> It is important to note that this method is only effective temporarily, so if you want a permanent effect, you'll need to modify the environment variable configuration file. For instance, on a Mac, you can modify the file located at `/etc/profile`.
 
 <details>
 
 <summary> Click to <strong>SHOW</strong> example code </summary>
 
 #### OpenAI API original usage
 
@@ -160,21 +165,21 @@
 
 def response_text(openai_resp):
     return openai_resp['choices'][0]['message']['content']
 
 from gptcache.core import cache
 from gptcache.adapter import openai
 from gptcache.embedding import Onnx
-from gptcache.cache.factory import get_ss_data_manager
-from gptcache.similarity_evaluation.simple import SearchDistanceEvaluation
+from gptcache.cache.factory import get_data_manager
+from gptcache.similarity_evaluation.distance import SearchDistanceEvaluation
 
 print("Cache loading.....")
 
 onnx = Onnx()
-data_manager = get_ss_data_manager("sqlite", "faiss", dimension=onnx.dimension())
+data_manager = get_data_manager("sqlite", "faiss", dimension=onnx.dimension)
 cache.init(
     embedding_func=onnx.to_embeddings,
     data_manager=data_manager,
     similarity_evaluation=SearchDistanceEvaluation(),
     )
 cache.set_openai_key()
 
@@ -182,28 +187,27 @@
     "what's github",
     "can you explain what GitHub is",
     "can you tell me more about GitHub"
     "what is the purpose of GitHub"
 ]
 
 for question in questions:
-    for _ in range(2):
-        start_time = time.time()
-        response = openai.ChatCompletion.create(
-            model='gpt-3.5-turbo',
-            messages=[
-                {
-                    'role': 'user',
-                    'content': question
-                }
-            ],
-        )
-        print(f'Question: {question}')
-        print("Time consuming: {:.2f}s".format(time.time() - start_time))
-        print(f'Answer: {response_text(response)}\n')
+    start_time = time.time()
+    response = openai.ChatCompletion.create(
+        model='gpt-3.5-turbo',
+        messages=[
+            {
+                'role': 'user',
+                'content': question
+            }
+        ],
+    )
+    print(f'Question: {question}')
+    print("Time consuming: {:.2f}s".format(time.time() - start_time))
+    print(f'Answer: {response_text(response)}\n')
 ```
 
 </details>
 
 To use GPTCache exclusively, only the following lines of code are required, and there is no need to modify any existing code.
 
 ```python
@@ -212,15 +216,14 @@
 
 cache.init()
 cache.set_openai_key()
 ```
 
 More Docs：
 
-- [System Design, how it was constructed](docs/system.md)
 - [Features, all features currently supported by the cache](docs/feature.md)
 - [Examples, learn better custom caching](examples/README.md)
 
 ## 🤗 Modules
 
 ![GPTCache Struct](docs/GPTCacheStructure.png)
 
@@ -228,15 +231,15 @@
 The LLM Adapter is designed to integrate different LLM models by unifying their APIs and request protocols. GPTCache offers a standardized interface for this purpose, with current support for ChatGPT integration.
   - [x] Support OpenAI chatGPT API.
   - [ ] Support other LLMs, such as Hugging Face Hub, Bard, Anthropic, and self-hosted models like LLaMa.
 - **Embedding Generator**: 
 This module is created to extract embeddings from requests for similarity search. GPTCache offers a generic interface that supports multiple embedding APIs, and presents a range of solutions to choose from. 
   - [x] Disable embedding. This will turn GPTCache into a keyword-matching cache.
   - [x] Support OpenAI embedding API.
-  - [x] Support [ONNX](https://onnx.ai/) with the paraphrase-albert-small-v2-onnx model.
+  - [x] Support [ONNX](https://onnx.ai/) with the GPTCache/paraphrase-albert-onnx model.
   - [x] Support [Hugging Face](https://huggingface.co/) embedding API.
   - [x] Support [Cohere](https://docs.cohere.ai/reference/embed) embedding API.
   - [ ] Support [fastText](https://fasttext.cc) embedding API.
   - [x] Support [SentenceTransformers](https://www.sbert.net) embedding API.
   - [ ] Support other embedding apis
 - **Cache Storage**:
 **Cache Storage** is where the response from LLMs, such as ChatGPT, is stored. Cached responses are retrieved to assist in evaluating similarity and are returned to the requester if there is a good semantic match. At present, GPTCache supports SQLite and offers a universally accessible interface for extension of this module.
@@ -245,15 +248,15 @@
   - [x] Support [MySQL](https://www.mysql.com/).
   - [x] Support [MariaDB](https://mariadb.org/).
   - [x] Support [SQL Server](https://www.microsoft.com/en-us/sql-server/).
   - [x] Support [Oracle](https://www.oracle.com/).
   - [ ] Support [MongoDB](https://www.mongodb.com/).
   - [ ] Support [Redis](https://redis.io/).
   - [ ] Support [Minio](https://min.io/).
-  - [ ] Support [Habse](https://hbase.apache.org//).
+  - [ ] Support [HBase](https://hbase.apache.org/).
   - [ ] Support [ElasticSearch](https://www.elastic.co/)
   - [ ] Support [zincsearch](https://zinc.dev/)
   - [ ] Support other storages
 - **Vector Store**:
 The **Vector Store** module helps find the K most similar requests from the input request's extracted embedding. The results can help assess similarity. GPTCache provides a user-friendly interface that supports various vector stores, including Milvus, Zilliz Cloud, and FAISS. More options will be available in the future.
   - [x] Support [Milvus](https://milvus.io/).
   - [x] Support [Zilliz Cloud](https://cloud.zilliz.com/).
@@ -268,15 +271,15 @@
   Currently, GPTCache makes decisions about evictions based solely on the number of lines. This approach can result in inaccurate resource evaluation and may cause out-of-memory (OOM) errors. We are actively investigating and developing a more sophisticated strategy.
     - [x] LRU eviction policy
     - [x] FIFO eviction policy
     - [ ] More complicated eviction policies
 - **Similarity Evaluator**: 
 This module collects data from both the **Cache Storage** and **Vector Store**, and uses various strategies to determine the similarity between the input request and the requests from the **Vector Store**. Based on this similarity, it determines whether a request matches the cache. GPTCache provides a standardized interface for integrating various strategies, along with a collection of implementations to use. The following similarity definitions are currently supported or will be supported in the future:
   - [x] The distance we obtain from the **Vector Store**.
-  - [x] A model-based similarity determined using the albert_duplicate model from [ONNX](https://onnx.ai/).
+  - [x] A model-based similarity determined using the GPTCache/albert-duplicate-onnx model from [ONNX](https://onnx.ai/).
   - [x] Exact matches between the input request and the requests obtained from the **Vector Store**.
   - [x] Distance represented by applying linalg.norm from numpy to the embeddings.
   - [ ] BM25 and other similarity measurements
   - [ ] Support other models
  
   
   **Note**:Not all combinations of different modules may be compatible with each other. For instance, if we disable the **Embedding Extractor**, the **Vector Store** may not function as intended. We are currently working on implementing a combination sanity check for **GPTCache**.
```

### Comparing `gptcache-0.1.3/gptcache.egg-info/SOURCES.txt` & `gptcache-0.1.4/gptcache.egg-info/SOURCES.txt`

 * *Files 14% similar despite different names*

```diff
@@ -22,25 +22,26 @@
 gptcache/cache/vector_data/__init__.py
 gptcache/cache/vector_data/base.py
 gptcache/cache/vector_data/chroma.py
 gptcache/cache/vector_data/faiss.py
 gptcache/cache/vector_data/milvus.py
 gptcache/embedding/__init__.py
 gptcache/embedding/cohere.py
+gptcache/embedding/fasttext.py
 gptcache/embedding/huggingface.py
 gptcache/embedding/onnx.py
 gptcache/embedding/openai.py
 gptcache/embedding/sbert.py
 gptcache/embedding/string.py
 gptcache/processor/__init__.py
 gptcache/processor/post.py
 gptcache/processor/pre.py
 gptcache/similarity_evaluation/__init__.py
+gptcache/similarity_evaluation/distance.py
+gptcache/similarity_evaluation/exact_match.py
 gptcache/similarity_evaluation/np.py
 gptcache/similarity_evaluation/onnx.py
 gptcache/similarity_evaluation/similarity_evaluation.py
-gptcache/similarity_evaluation/simple.py
-gptcache/similarity_evaluation/string.py
 gptcache/utils/__init__.py
 gptcache/utils/dependency_control.py
 gptcache/utils/error.py
 gptcache/utils/lazy_import.py
```

### Comparing `gptcache-0.1.3/setup.py` & `gptcache-0.1.4/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -13,20 +13,20 @@
             if require.strip() and not require.startswith('#')
         ]
 
 
 setuptools.setup(
     name="gptcache",
     packages=find_packages(),
-    version="0.1.3",
+    version="0.1.4",
     author="SimFG",
     author_email="bang.fu@zilliz.com",
     description="GPT Cache, a powerful caching library that can be used to speed up and lower the cost of chat "
                 "applications that rely on the LLM service. GPT Cache works as a memcache for AIGC applications, "
                 "similar to how Redis works for traditional applications.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     install_requires=parse_requirements('requirements.txt'),
-    url="https://github.com/zilliztech/gptcache",
-    license='http://www.apache.org/licenses/LICENSE-2.0',
+    url="https://github.com/zilliztech/GPTCache",
+    license='https://opensource.org/license/mit/',
     python_requires='>=3.8.1',
 )
```

