# Comparing `tmp/llama_index-0.5.8.tar.gz` & `tmp/llama_index-0.5.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "llama_index-0.5.8.tar", last modified: Wed Apr  5 07:06:12 2023, max compression
+gzip compressed data, was "llama_index-0.5.9.tar", last modified: Thu Apr  6 17:13:08 2023, max compression
```

## Comparing `llama_index-0.5.8.tar` & `llama_index-0.5.9.tar`

### file list

```diff
@@ -1,261 +1,259 @@
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.825454 llama_index-0.5.8/
--rw-r--r--   0 jerryliu   (501) staff       (20)     1064 2023-04-05 07:06:12.000000 llama_index-0.5.8/LICENSE
--rw-r--r--   0 jerryliu   (501) staff       (20)       73 2023-04-05 07:06:12.000000 llama_index-0.5.8/MANIFEST.in
--rw-r--r--   0 jerryliu   (501) staff       (20)     4447 2023-04-05 07:06:12.825276 llama_index-0.5.8/PKG-INFO
--rw-r--r--   0 jerryliu   (501) staff       (20)     4219 2023-04-05 07:06:12.000000 llama_index-0.5.8/README.md
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.804703 llama_index-0.5.8/llama_index/
--rw-r--r--   0 jerryliu   (501) staff       (20)        6 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/VERSION
--rw-r--r--   0 jerryliu   (501) staff       (20)     4468 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      322 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/async_utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.805423 llama_index-0.5.8/llama_index/composability/
--rw-r--r--   0 jerryliu   (501) staff       (20)      220 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/composability/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      171 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/composability/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2654 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/composability/joint_qa_summary.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      242 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/constants.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.806138 llama_index-0.5.8/llama_index/data_structs/
--rw-r--r--   0 jerryliu   (501) staff       (20)      373 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    12377 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/data_structs.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    12314 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/data_structs_v2.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      264 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/node_mapping.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4748 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/node_v2.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2669 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/struct_type.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      908 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/table.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1032 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/data_structs/table_v2.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7415 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/docstore.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.806581 llama_index-0.5.8/llama_index/embeddings/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/embeddings/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7650 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/embeddings/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      934 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/embeddings/langchain.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    10103 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/embeddings/openai.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      559 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/embeddings/utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.806754 llama_index-0.5.8/llama_index/evaluation/
--rw-r--r--   0 jerryliu   (501) staff       (20)      118 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/evaluation/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4409 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/evaluation/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      544 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/img_utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.807304 llama_index-0.5.8/llama_index/indices/
--rw-r--r--   0 jerryliu   (501) staff       (20)      542 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    14728 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/base.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.807397 llama_index-0.5.8/llama_index/indices/common/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common/__init__.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.807755 llama_index-0.5.8/llama_index/indices/common/struct_store/
--rw-r--r--   0 jerryliu   (501) staff       (20)       19 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common/struct_store/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     8107 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common/struct_store/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      776 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common/struct_store/schema.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2629 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common/struct_store/sql.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.807937 llama_index-0.5.8/llama_index/indices/common_tree/
--rw-r--r--   0 jerryliu   (501) staff       (20)       19 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common_tree/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7146 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/common_tree/base.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.808122 llama_index-0.5.8/llama_index/indices/composability/
--rw-r--r--   0 jerryliu   (501) staff       (20)      180 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/composability/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     9122 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/composability/graph.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.808404 llama_index-0.5.8/llama_index/indices/empty/
--rw-r--r--   0 jerryliu   (501) staff       (20)      202 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/empty/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2158 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/empty/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2178 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/empty/query.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.808944 llama_index-0.5.8/llama_index/indices/keyword_table/
--rw-r--r--   0 jerryliu   (501) staff       (20)      645 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/keyword_table/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7054 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/keyword_table/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     6271 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/keyword_table/query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      650 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/keyword_table/rake_base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      844 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/keyword_table/simple_base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2264 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/keyword_table/utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.809222 llama_index-0.5.8/llama_index/indices/knowledge_graph/
--rw-r--r--   0 jerryliu   (501) staff       (20)      279 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/knowledge_graph/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     8029 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/knowledge_graph/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     9601 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/knowledge_graph/query.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.809575 llama_index-0.5.8/llama_index/indices/list/
--rw-r--r--   0 jerryliu   (501) staff       (20)      325 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/list/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3611 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/list/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3089 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/list/embedding_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1539 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/list/query.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.809844 llama_index-0.5.8/llama_index/indices/postprocessor/
--rw-r--r--   0 jerryliu   (501) staff       (20)      457 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/postprocessor/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)       83 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/postprocessor/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    11871 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/postprocessor/node.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     8464 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/prompt_helper.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.810299 llama_index-0.5.8/llama_index/indices/query/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    14869 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2581 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/embedding_utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.810572 llama_index-0.5.8/llama_index/indices/query/query_combiner/
--rw-r--r--   0 jerryliu   (501) staff       (20)      140 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_combiner/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     8753 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_combiner/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)       30 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_combiner/prompts.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    12990 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_runner.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.810844 llama_index-0.5.8/llama_index/indices/query/query_transform/
--rw-r--r--   0 jerryliu   (501) staff       (20)      281 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_transform/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     9145 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_transform/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5920 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/query_transform/prompts.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4834 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/query/schema.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4045 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/registry.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.811028 llama_index-0.5.8/llama_index/indices/response/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/response/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    15585 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/response/builder.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3310 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/service_context.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.811719 llama_index-0.5.8/llama_index/indices/struct_store/
--rw-r--r--   0 jerryliu   (501) staff       (20)      616 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2115 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5765 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/container_builder.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2624 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/pandas.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4755 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/pandas_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     8059 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/sql.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     6674 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/struct_store/sql_query.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.812399 llama_index-0.5.8/llama_index/indices/tree/
--rw-r--r--   0 jerryliu   (501) staff       (20)      460 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5179 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5493 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/embedding_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7034 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/inserter.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    14258 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/leaf_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1798 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/retrieve_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2229 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/tree/summarize_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2005 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.812960 llama_index-0.5.8/llama_index/indices/vector_store/
--rw-r--r--   0 jerryliu   (501) staff       (20)      720 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/vector_store/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    10010 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/vector_store/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3264 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/vector_store/base_query.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     9428 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/vector_store/queries.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    23198 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/indices/vector_store/vector_indices.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.813552 llama_index-0.5.8/llama_index/langchain_helpers/
--rw-r--r--   0 jerryliu   (501) staff       (20)       39 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/__init__.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.814033 llama_index-0.5.8/llama_index/langchain_helpers/agents/
--rw-r--r--   0 jerryliu   (501) staff       (20)      555 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/agents/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2989 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/agents/agents.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1132 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/agents/toolkits.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3001 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/agents/tools.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      252 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/chain_wrapper.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7571 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/memory_wrapper.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3299 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/sql_wrapper.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    17458 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/langchain_helpers/text_splitter.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.814524 llama_index-0.5.8/llama_index/llm_predictor/
--rw-r--r--   0 jerryliu   (501) staff       (20)      254 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/llm_predictor/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    10593 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/llm_predictor/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4275 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/llm_predictor/chatgpt.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2274 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/llm_predictor/structured.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.814770 llama_index-0.5.8/llama_index/logger/
--rw-r--r--   0 jerryliu   (501) staff       (20)       95 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/logger/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      995 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/logger/base.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.815300 llama_index-0.5.8/llama_index/node_parser/
--rw-r--r--   0 jerryliu   (501) staff       (20)      184 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/node_parser/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      530 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/node_parser/interface.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3606 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/node_parser/node_utils.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1856 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/node_parser/simple.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4984 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/old_docstore.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.815689 llama_index-0.5.8/llama_index/optimization/
--rw-r--r--   0 jerryliu   (501) staff       (20)      144 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/optimization/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4248 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/optimization/optimizer.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.816239 llama_index-0.5.8/llama_index/output_parsers/
--rw-r--r--   0 jerryliu   (501) staff       (20)      230 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/output_parsers/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      611 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/output_parsers/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2742 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/output_parsers/guardrails.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1828 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/output_parsers/langchain.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.816475 llama_index-0.5.8/llama_index/playground/
--rw-r--r--   0 jerryliu   (501) staff       (20)      202 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/playground/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5637 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/playground/base.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.817294 llama_index-0.5.8/llama_index/prompts/
--rw-r--r--   0 jerryliu   (501) staff       (20)       87 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     6626 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1969 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/chat_prompts.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1134 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/default_prompt_selectors.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    10843 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/default_prompts.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      992 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/prompt_type.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7685 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/prompts/prompts.py
--rw-r--r--   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/py.typed
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.819236 llama_index-0.5.8/llama_index/readers/
--rw-r--r--   0 jerryliu   (501) staff       (20)     2749 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      659 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/base.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.819428 llama_index-0.5.8/llama_index/readers/chatgpt_plugin/
--rw-r--r--   0 jerryliu   (501) staff       (20)      145 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/chatgpt_plugin/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2111 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/chatgpt_plugin/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3895 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/chroma.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3328 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/database.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4981 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/discord_reader.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7413 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/download.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2392 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/elasticsearch.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2478 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/faiss.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.820408 llama_index-0.5.8/llama_index/readers/file/
--rw-r--r--   0 jerryliu   (501) staff       (20)       19 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     8436 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1342 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/base_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1629 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/docs_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1318 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/epub_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4106 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/image_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3616 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/markdown_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3162 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/mbox_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3945 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/slides_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3357 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/tabular_parser.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1770 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/file/video_audio.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.820787 llama_index-0.5.8/llama_index/readers/github_readers/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/github_readers/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    11686 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/github_readers/github_api_client.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    15928 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/github_readers/github_repository_reader.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5473 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/github_readers/utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.821141 llama_index-0.5.8/llama_index/readers/google_readers/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/google_readers/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5659 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/google_readers/gdocs.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4989 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/google_readers/gsheets.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3708 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/json.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.821266 llama_index-0.5.8/llama_index/readers/llamahub_modules/
--rw-r--r--   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/llamahub_modules/__init__.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.821490 llama_index-0.5.8/llama_index/readers/make_com/
--rw-r--r--   0 jerryliu   (501) staff       (20)       19 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/make_com/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1696 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/make_com/wrapper.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1261 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/mbox.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2260 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/mongo.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5679 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/notion.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1601 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/obsidian.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2766 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/pinecone.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3279 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/qdrant.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.821706 llama_index-0.5.8/llama_index/readers/schema/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/schema/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1214 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/schema/base.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7892 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/slack.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.821962 llama_index-0.5.8/llama_index/readers/steamship/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/steamship/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3498 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/steamship/file_reader.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      984 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/string_iterable.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1918 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/twitter.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.822670 llama_index-0.5.8/llama_index/readers/weaviate/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/weaviate/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     9784 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/weaviate/data_structs.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3986 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/weaviate/reader.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1867 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/weaviate/utils.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7987 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/web.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      981 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/wikipedia.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1255 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/readers/youtube_transcript.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.823116 llama_index-0.5.8/llama_index/response/
--rw-r--r--   0 jerryliu   (501) staff       (20)       19 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/response/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2039 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/response/notebook_utils.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3135 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/response/schema.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      262 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/response/utils.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2768 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/schema.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.823673 llama_index-0.5.8/llama_index/token_counter/
--rw-r--r--   0 jerryliu   (501) staff       (20)       17 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/token_counter/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4664 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/token_counter/mock_chain_wrapper.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      722 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/token_counter/mock_embed_model.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     2874 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/token_counter/token_counter.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      908 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/token_counter/utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.824016 llama_index-0.5.8/llama_index/tools/
--rw-r--r--   0 jerryliu   (501) staff       (20)       13 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/tools/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)      723 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/tools/file_utils.py
--rw-r--r--   0 jerryliu   (501) staff       (20)    11340 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/tools/migrate_v1_to_v2.py
--rw-r--r--   0 jerryliu   (501) staff       (20)       81 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/types.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5296 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/utils.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.825107 llama_index-0.5.8/llama_index/vector_stores/
--rw-r--r--   0 jerryliu   (501) staff       (20)      859 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/__init__.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     5451 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/chatgpt_plugin.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     4170 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/chroma.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3925 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/faiss.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     6665 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/opensearch.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     7376 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/pinecone.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     6941 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/qdrant.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3521 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/simple.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     1503 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/types.py
--rw-r--r--   0 jerryliu   (501) staff       (20)     3776 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index/vector_stores/weaviate.py
-drwxr-xr-x   0 jerryliu   (501) staff       (20)        0 2023-04-05 07:06:12.805148 llama_index-0.5.8/llama_index.egg-info/
--rw-r--r--   0 jerryliu   (501) staff       (20)     4447 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index.egg-info/PKG-INFO
--rw-r--r--   0 jerryliu   (501) staff       (20)     8074 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index.egg-info/SOURCES.txt
--rw-r--r--   0 jerryliu   (501) staff       (20)        1 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index.egg-info/dependency_links.txt
--rw-r--r--   0 jerryliu   (501) staff       (20)       87 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index.egg-info/requires.txt
--rw-r--r--   0 jerryliu   (501) staff       (20)       12 2023-04-05 07:06:12.000000 llama_index-0.5.8/llama_index.egg-info/top_level.txt
--rw-r--r--   0 jerryliu   (501) staff       (20)       38 2023-04-05 07:06:12.825515 llama_index-0.5.8/setup.cfg
--rw-r--r--   0 jerryliu   (501) staff       (20)     1121 2023-04-05 07:06:12.000000 llama_index-0.5.8/setup.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.211702 llama_index-0.5.9/
+-rw-r--r--   0 suo        (501) staff       (20)     1064 2023-04-06 17:13:07.000000 llama_index-0.5.9/LICENSE
+-rw-r--r--   0 suo        (501) staff       (20)       73 2023-04-06 17:13:07.000000 llama_index-0.5.9/MANIFEST.in
+-rw-r--r--   0 suo        (501) staff       (20)     4449 2023-04-06 17:13:08.211372 llama_index-0.5.9/PKG-INFO
+-rw-r--r--   0 suo        (501) staff       (20)     4221 2023-04-06 17:13:07.000000 llama_index-0.5.9/README.md
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.157193 llama_index-0.5.9/llama_index/
+-rw-r--r--   0 suo        (501) staff       (20)        6 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/VERSION
+-rw-r--r--   0 suo        (501) staff       (20)     4468 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      322 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/async_utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.159590 llama_index-0.5.9/llama_index/composability/
+-rw-r--r--   0 suo        (501) staff       (20)      220 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/composability/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      171 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/composability/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     2654 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/composability/joint_qa_summary.py
+-rw-r--r--   0 suo        (501) staff       (20)      277 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/constants.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.161752 llama_index-0.5.9/llama_index/data_structs/
+-rw-r--r--   0 suo        (501) staff       (20)      373 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    12377 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/data_structs.py
+-rw-r--r--   0 suo        (501) staff       (20)    12269 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/data_structs_v2.py
+-rw-r--r--   0 suo        (501) staff       (20)     4748 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/node_v2.py
+-rw-r--r--   0 suo        (501) staff       (20)     2669 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/struct_type.py
+-rw-r--r--   0 suo        (501) staff       (20)      908 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/table.py
+-rw-r--r--   0 suo        (501) staff       (20)     1032 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/data_structs/table_v2.py
+-rw-r--r--   0 suo        (501) staff       (20)     7415 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/docstore.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.163201 llama_index-0.5.9/llama_index/embeddings/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/embeddings/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     7650 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/embeddings/base.py
+-rw-r--r--   0 suo        (501) staff       (20)      934 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/embeddings/langchain.py
+-rw-r--r--   0 suo        (501) staff       (20)    10103 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/embeddings/openai.py
+-rw-r--r--   0 suo        (501) staff       (20)      559 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/embeddings/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.163751 llama_index-0.5.9/llama_index/evaluation/
+-rw-r--r--   0 suo        (501) staff       (20)      118 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/evaluation/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     4409 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/evaluation/base.py
+-rw-r--r--   0 suo        (501) staff       (20)      544 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/img_utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.165499 llama_index-0.5.9/llama_index/indices/
+-rw-r--r--   0 suo        (501) staff       (20)      542 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    15287 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/base.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.165775 llama_index-0.5.9/llama_index/indices/common/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common/__init__.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.166860 llama_index-0.5.9/llama_index/indices/common/struct_store/
+-rw-r--r--   0 suo        (501) staff       (20)       19 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common/struct_store/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     8107 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common/struct_store/base.py
+-rw-r--r--   0 suo        (501) staff       (20)      776 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common/struct_store/schema.py
+-rw-r--r--   0 suo        (501) staff       (20)     2629 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common/struct_store/sql.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.167399 llama_index-0.5.9/llama_index/indices/common_tree/
+-rw-r--r--   0 suo        (501) staff       (20)       19 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common_tree/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     7146 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/common_tree/base.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.168222 llama_index-0.5.9/llama_index/indices/composability/
+-rw-r--r--   0 suo        (501) staff       (20)      180 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/composability/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    10585 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/composability/graph.py
+-rw-r--r--   0 suo        (501) staff       (20)     2382 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/composability/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.169141 llama_index-0.5.9/llama_index/indices/empty/
+-rw-r--r--   0 suo        (501) staff       (20)      202 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/empty/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     2158 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/empty/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     2178 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/empty/query.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.170793 llama_index-0.5.9/llama_index/indices/keyword_table/
+-rw-r--r--   0 suo        (501) staff       (20)      645 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/keyword_table/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     7054 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/keyword_table/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     6271 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/keyword_table/query.py
+-rw-r--r--   0 suo        (501) staff       (20)      650 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/keyword_table/rake_base.py
+-rw-r--r--   0 suo        (501) staff       (20)      844 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/keyword_table/simple_base.py
+-rw-r--r--   0 suo        (501) staff       (20)     2264 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/keyword_table/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.171611 llama_index-0.5.9/llama_index/indices/knowledge_graph/
+-rw-r--r--   0 suo        (501) staff       (20)      279 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/knowledge_graph/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     8029 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/knowledge_graph/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     9601 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/knowledge_graph/query.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.172721 llama_index-0.5.9/llama_index/indices/list/
+-rw-r--r--   0 suo        (501) staff       (20)      325 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/list/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     3611 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/list/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     3089 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/list/embedding_query.py
+-rw-r--r--   0 suo        (501) staff       (20)     1539 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/list/query.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.173536 llama_index-0.5.9/llama_index/indices/postprocessor/
+-rw-r--r--   0 suo        (501) staff       (20)      457 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/postprocessor/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)       83 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/postprocessor/base.py
+-rw-r--r--   0 suo        (501) staff       (20)    11871 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/postprocessor/node.py
+-rw-r--r--   0 suo        (501) staff       (20)     8464 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/prompt_helper.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.174860 llama_index-0.5.9/llama_index/indices/query/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    14869 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     2581 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/embedding_utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.175855 llama_index-0.5.9/llama_index/indices/query/query_combiner/
+-rw-r--r--   0 suo        (501) staff       (20)      140 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_combiner/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     8753 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_combiner/base.py
+-rw-r--r--   0 suo        (501) staff       (20)       30 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_combiner/prompts.py
+-rw-r--r--   0 suo        (501) staff       (20)    13263 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_runner.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.176660 llama_index-0.5.9/llama_index/indices/query/query_transform/
+-rw-r--r--   0 suo        (501) staff       (20)      281 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_transform/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     9145 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_transform/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     5920 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/query_transform/prompts.py
+-rw-r--r--   0 suo        (501) staff       (20)     4834 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/query/schema.py
+-rw-r--r--   0 suo        (501) staff       (20)     4045 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/registry.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.177175 llama_index-0.5.9/llama_index/indices/response/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/response/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    15585 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/response/builder.py
+-rw-r--r--   0 suo        (501) staff       (20)     3310 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/service_context.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.178881 llama_index-0.5.9/llama_index/indices/struct_store/
+-rw-r--r--   0 suo        (501) staff       (20)      616 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     2115 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     5765 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/container_builder.py
+-rw-r--r--   0 suo        (501) staff       (20)     2624 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/pandas.py
+-rw-r--r--   0 suo        (501) staff       (20)     4755 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/pandas_query.py
+-rw-r--r--   0 suo        (501) staff       (20)     8059 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/sql.py
+-rw-r--r--   0 suo        (501) staff       (20)     6674 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/struct_store/sql_query.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.180512 llama_index-0.5.9/llama_index/indices/tree/
+-rw-r--r--   0 suo        (501) staff       (20)      460 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     5179 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     5493 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/embedding_query.py
+-rw-r--r--   0 suo        (501) staff       (20)     7034 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/inserter.py
+-rw-r--r--   0 suo        (501) staff       (20)    14258 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/leaf_query.py
+-rw-r--r--   0 suo        (501) staff       (20)     1798 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/retrieve_query.py
+-rw-r--r--   0 suo        (501) staff       (20)     2229 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/tree/summarize_query.py
+-rw-r--r--   0 suo        (501) staff       (20)     2005 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.181398 llama_index-0.5.9/llama_index/indices/vector_store/
+-rw-r--r--   0 suo        (501) staff       (20)      720 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/vector_store/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    10348 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/vector_store/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     3782 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/vector_store/base_query.py
+-rw-r--r--   0 suo        (501) staff       (20)    17152 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/indices/vector_store/vector_indices.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.182799 llama_index-0.5.9/llama_index/langchain_helpers/
+-rw-r--r--   0 suo        (501) staff       (20)       39 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/__init__.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.183971 llama_index-0.5.9/llama_index/langchain_helpers/agents/
+-rw-r--r--   0 suo        (501) staff       (20)      555 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/agents/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     2989 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/agents/agents.py
+-rw-r--r--   0 suo        (501) staff       (20)     1132 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/agents/toolkits.py
+-rw-r--r--   0 suo        (501) staff       (20)     3001 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/agents/tools.py
+-rw-r--r--   0 suo        (501) staff       (20)      252 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/chain_wrapper.py
+-rw-r--r--   0 suo        (501) staff       (20)     7571 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/memory_wrapper.py
+-rw-r--r--   0 suo        (501) staff       (20)     3299 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/sql_wrapper.py
+-rw-r--r--   0 suo        (501) staff       (20)    17458 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/langchain_helpers/text_splitter.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.184997 llama_index-0.5.9/llama_index/llm_predictor/
+-rw-r--r--   0 suo        (501) staff       (20)      254 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/llm_predictor/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    10593 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/llm_predictor/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     4275 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/llm_predictor/chatgpt.py
+-rw-r--r--   0 suo        (501) staff       (20)     2274 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/llm_predictor/structured.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.185680 llama_index-0.5.9/llama_index/logger/
+-rw-r--r--   0 suo        (501) staff       (20)       95 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/logger/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      995 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/logger/base.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.186773 llama_index-0.5.9/llama_index/node_parser/
+-rw-r--r--   0 suo        (501) staff       (20)      184 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/node_parser/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      530 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/node_parser/interface.py
+-rw-r--r--   0 suo        (501) staff       (20)     3606 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/node_parser/node_utils.py
+-rw-r--r--   0 suo        (501) staff       (20)     1856 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/node_parser/simple.py
+-rw-r--r--   0 suo        (501) staff       (20)     4984 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/old_docstore.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.187243 llama_index-0.5.9/llama_index/optimization/
+-rw-r--r--   0 suo        (501) staff       (20)      144 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/optimization/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     4248 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/optimization/optimizer.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.188171 llama_index-0.5.9/llama_index/output_parsers/
+-rw-r--r--   0 suo        (501) staff       (20)      230 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/output_parsers/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      611 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/output_parsers/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     2742 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/output_parsers/guardrails.py
+-rw-r--r--   0 suo        (501) staff       (20)     1828 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/output_parsers/langchain.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.188630 llama_index-0.5.9/llama_index/playground/
+-rw-r--r--   0 suo        (501) staff       (20)      202 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/playground/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     5637 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/playground/base.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.190240 llama_index-0.5.9/llama_index/prompts/
+-rw-r--r--   0 suo        (501) staff       (20)       87 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     6626 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     1969 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/chat_prompts.py
+-rw-r--r--   0 suo        (501) staff       (20)     1134 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/default_prompt_selectors.py
+-rw-r--r--   0 suo        (501) staff       (20)    10843 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/default_prompts.py
+-rw-r--r--   0 suo        (501) staff       (20)      992 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/prompt_type.py
+-rw-r--r--   0 suo        (501) staff       (20)     7685 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/prompts/prompts.py
+-rw-r--r--   0 suo        (501) staff       (20)        0 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/py.typed
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.195649 llama_index-0.5.9/llama_index/readers/
+-rw-r--r--   0 suo        (501) staff       (20)     2749 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      659 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/base.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.196182 llama_index-0.5.9/llama_index/readers/chatgpt_plugin/
+-rw-r--r--   0 suo        (501) staff       (20)      145 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/chatgpt_plugin/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     2111 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/chatgpt_plugin/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     3895 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/chroma.py
+-rw-r--r--   0 suo        (501) staff       (20)     3328 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/database.py
+-rw-r--r--   0 suo        (501) staff       (20)     4981 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/discord_reader.py
+-rw-r--r--   0 suo        (501) staff       (20)     7413 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/download.py
+-rw-r--r--   0 suo        (501) staff       (20)     2392 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/elasticsearch.py
+-rw-r--r--   0 suo        (501) staff       (20)     2478 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/faiss.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.199072 llama_index-0.5.9/llama_index/readers/file/
+-rw-r--r--   0 suo        (501) staff       (20)       19 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     8436 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     1342 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/base_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     1629 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/docs_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     1318 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/epub_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     4106 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/image_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     3616 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/markdown_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     3162 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/mbox_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     3945 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/slides_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     3357 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/tabular_parser.py
+-rw-r--r--   0 suo        (501) staff       (20)     1770 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/file/video_audio.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.200089 llama_index-0.5.9/llama_index/readers/github_readers/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/github_readers/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)    11686 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/github_readers/github_api_client.py
+-rw-r--r--   0 suo        (501) staff       (20)    15928 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/github_readers/github_repository_reader.py
+-rw-r--r--   0 suo        (501) staff       (20)     5473 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/github_readers/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.200857 llama_index-0.5.9/llama_index/readers/google_readers/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/google_readers/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     5659 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/google_readers/gdocs.py
+-rw-r--r--   0 suo        (501) staff       (20)     4989 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/google_readers/gsheets.py
+-rw-r--r--   0 suo        (501) staff       (20)     3708 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/json.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.201395 llama_index-0.5.9/llama_index/readers/make_com/
+-rw-r--r--   0 suo        (501) staff       (20)       19 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/make_com/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     1696 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/make_com/wrapper.py
+-rw-r--r--   0 suo        (501) staff       (20)     1261 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/mbox.py
+-rw-r--r--   0 suo        (501) staff       (20)     2260 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/mongo.py
+-rw-r--r--   0 suo        (501) staff       (20)     5679 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/notion.py
+-rw-r--r--   0 suo        (501) staff       (20)     1601 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/obsidian.py
+-rw-r--r--   0 suo        (501) staff       (20)     2766 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/pinecone.py
+-rw-r--r--   0 suo        (501) staff       (20)     3279 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/qdrant.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.201931 llama_index-0.5.9/llama_index/readers/schema/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/schema/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     1214 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/schema/base.py
+-rw-r--r--   0 suo        (501) staff       (20)     7892 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/slack.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.202453 llama_index-0.5.9/llama_index/readers/steamship/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/steamship/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     3498 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/steamship/file_reader.py
+-rw-r--r--   0 suo        (501) staff       (20)      984 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/string_iterable.py
+-rw-r--r--   0 suo        (501) staff       (20)     1918 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/twitter.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.203527 llama_index-0.5.9/llama_index/readers/weaviate/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/weaviate/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     9784 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/weaviate/data_structs.py
+-rw-r--r--   0 suo        (501) staff       (20)     3986 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/weaviate/reader.py
+-rw-r--r--   0 suo        (501) staff       (20)     1867 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/weaviate/utils.py
+-rw-r--r--   0 suo        (501) staff       (20)     7987 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/web.py
+-rw-r--r--   0 suo        (501) staff       (20)      981 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/wikipedia.py
+-rw-r--r--   0 suo        (501) staff       (20)     1255 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/readers/youtube_transcript.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.204720 llama_index-0.5.9/llama_index/response/
+-rw-r--r--   0 suo        (501) staff       (20)       19 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/response/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     2039 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/response/notebook_utils.py
+-rw-r--r--   0 suo        (501) staff       (20)     3135 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/response/schema.py
+-rw-r--r--   0 suo        (501) staff       (20)      262 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/response/utils.py
+-rw-r--r--   0 suo        (501) staff       (20)     2768 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/schema.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.206186 llama_index-0.5.9/llama_index/token_counter/
+-rw-r--r--   0 suo        (501) staff       (20)       17 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/token_counter/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     4664 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/token_counter/mock_chain_wrapper.py
+-rw-r--r--   0 suo        (501) staff       (20)      722 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/token_counter/mock_embed_model.py
+-rw-r--r--   0 suo        (501) staff       (20)     2874 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/token_counter/token_counter.py
+-rw-r--r--   0 suo        (501) staff       (20)      908 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/token_counter/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.207038 llama_index-0.5.9/llama_index/tools/
+-rw-r--r--   0 suo        (501) staff       (20)       13 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/tools/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)      723 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/tools/file_utils.py
+-rw-r--r--   0 suo        (501) staff       (20)    11340 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/tools/migrate_v1_to_v2.py
+-rw-r--r--   0 suo        (501) staff       (20)       81 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/types.py
+-rw-r--r--   0 suo        (501) staff       (20)     5296 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/utils.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.210989 llama_index-0.5.9/llama_index/vector_stores/
+-rw-r--r--   0 suo        (501) staff       (20)      859 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/__init__.py
+-rw-r--r--   0 suo        (501) staff       (20)     5682 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/chatgpt_plugin.py
+-rw-r--r--   0 suo        (501) staff       (20)     4408 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/chroma.py
+-rw-r--r--   0 suo        (501) staff       (20)     4488 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/faiss.py
+-rw-r--r--   0 suo        (501) staff       (20)     6886 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/opensearch.py
+-rw-r--r--   0 suo        (501) staff       (20)     8805 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/pinecone.py
+-rw-r--r--   0 suo        (501) staff       (20)     7164 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/qdrant.py
+-rw-r--r--   0 suo        (501) staff       (20)     2568 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/registry.py
+-rw-r--r--   0 suo        (501) staff       (20)     3649 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/simple.py
+-rw-r--r--   0 suo        (501) staff       (20)     1647 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/types.py
+-rw-r--r--   0 suo        (501) staff       (20)     4104 2023-04-06 17:13:07.000000 llama_index-0.5.9/llama_index/vector_stores/weaviate.py
+drwxr-xr-x   0 suo        (501) staff       (20)        0 2023-04-06 17:13:08.158709 llama_index-0.5.9/llama_index.egg-info/
+-rw-r--r--   0 suo        (501) staff       (20)     4449 2023-04-06 17:13:08.000000 llama_index-0.5.9/llama_index.egg-info/PKG-INFO
+-rw-r--r--   0 suo        (501) staff       (20)     8021 2023-04-06 17:13:08.000000 llama_index-0.5.9/llama_index.egg-info/SOURCES.txt
+-rw-r--r--   0 suo        (501) staff       (20)        1 2023-04-06 17:13:08.000000 llama_index-0.5.9/llama_index.egg-info/dependency_links.txt
+-rw-r--r--   0 suo        (501) staff       (20)       87 2023-04-06 17:13:08.000000 llama_index-0.5.9/llama_index.egg-info/requires.txt
+-rw-r--r--   0 suo        (501) staff       (20)       12 2023-04-06 17:13:08.000000 llama_index-0.5.9/llama_index.egg-info/top_level.txt
+-rw-r--r--   0 suo        (501) staff       (20)       38 2023-04-06 17:13:08.211782 llama_index-0.5.9/setup.cfg
+-rw-r--r--   0 suo        (501) staff       (20)     1121 2023-04-06 17:13:07.000000 llama_index-0.5.9/setup.py
```

### Comparing `llama_index-0.5.8/LICENSE` & `llama_index-0.5.9/LICENSE`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/PKG-INFO` & `llama_index-0.5.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: llama_index
-Version: 0.5.8
+Version: 0.5.9
 Summary: Interface between LLMs and your data.
 Home-page: https://github.com/jerryjliu/gpt_index
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # 🗂️ LlamaIndex 🦙 (GPT Index)
@@ -115,11 +115,11 @@
 
 ```
 @software{Liu_LlamaIndex_2022,
 author = {Liu, Jerry},
 doi = {10.5281/zenodo.1234},
 month = {11},
 title = {{LlamaIndex}},
-url = {https://github.com/jerryjliu/gpt_index},
+url = {https://github.com/jerryjliu/llama_index},
 year = {2022}
 }
 ```
```

### Comparing `llama_index-0.5.8/README.md` & `llama_index-0.5.9/README.md`

 * *Files 1% similar despite different names*

```diff
@@ -106,11 +106,11 @@
 
 ```
 @software{Liu_LlamaIndex_2022,
 author = {Liu, Jerry},
 doi = {10.5281/zenodo.1234},
 month = {11},
 title = {{LlamaIndex}},
-url = {https://github.com/jerryjliu/gpt_index},
+url = {https://github.com/jerryjliu/llama_index},
 year = {2022}
 }
 ```
```

### Comparing `llama_index-0.5.8/llama_index/__init__.py` & `llama_index-0.5.9/llama_index/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/composability/joint_qa_summary.py` & `llama_index-0.5.9/llama_index/composability/joint_qa_summary.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/data_structs/data_structs.py` & `llama_index-0.5.9/llama_index/data_structs/data_structs.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/data_structs/data_structs_v2.py` & `llama_index-0.5.9/llama_index/data_structs/data_structs_v2.py`

 * *Files 0% similar despite different names*

```diff
@@ -196,15 +196,15 @@
             self.doc_id_dict[node.ref_doc_id].append(vector_id)
 
         return vector_id
 
     def delete(self, doc_id: str) -> None:
         """Delete a Node."""
         if doc_id not in self.doc_id_dict:
-            raise ValueError("doc_id not found in doc_id_dict")
+            return
         for vector_id in self.doc_id_dict[doc_id]:
             del self.nodes_dict[vector_id]
         del self.doc_id_dict[doc_id]
 
     @classmethod
     def get_type(cls) -> IndexStructType:
         """Get type."""
```

### Comparing `llama_index-0.5.8/llama_index/data_structs/node_v2.py` & `llama_index-0.5.9/llama_index/data_structs/node_v2.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/data_structs/struct_type.py` & `llama_index-0.5.9/llama_index/data_structs/struct_type.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/data_structs/table.py` & `llama_index-0.5.9/llama_index/data_structs/table.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/data_structs/table_v2.py` & `llama_index-0.5.9/llama_index/data_structs/table_v2.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/docstore.py` & `llama_index-0.5.9/llama_index/docstore.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/embeddings/base.py` & `llama_index-0.5.9/llama_index/embeddings/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/embeddings/langchain.py` & `llama_index-0.5.9/llama_index/embeddings/langchain.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/embeddings/openai.py` & `llama_index-0.5.9/llama_index/embeddings/openai.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/embeddings/utils.py` & `llama_index-0.5.9/llama_index/embeddings/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/evaluation/base.py` & `llama_index-0.5.9/llama_index/evaluation/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/img_utils.py` & `llama_index-0.5.9/llama_index/img_utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/__init__.py` & `llama_index-0.5.9/llama_index/indices/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/base.py` & `llama_index-0.5.9/llama_index/indices/base.py`

 * *Files 4% similar despite different names*

```diff
@@ -190,14 +190,24 @@
                 refreshed_documents[i] = True
             elif existing_doc_hash is None:
                 self.insert(document, **update_kwargs.pop("insert_kwargs", {}))
                 refreshed_documents[i] = True
 
         return refreshed_documents
 
+    @property
+    def query_context(self) -> Dict[str, Any]:
+        """Additional context necessary for making a query.
+
+        This should capture any index-specific clients, services, etc,
+        that's not captured by index struct, docstore, and service context.
+        For example, a vector store index would pass vector store.
+        """
+        return {}
+
     def _preprocess_query(self, mode: QueryMode, query_kwargs: Dict) -> None:
         """Preprocess query.
 
         This allows subclasses to pass in additional query kwargs
         to query, for instance arguments that are shared between the
         index and the query class. By default, this does nothing.
         This also allows subclasses to do validation.
@@ -231,14 +241,15 @@
             index_struct_type=self._index_struct.get_type(),
             query_mode=mode_enum,
             query_kwargs=query_kwargs,
         )
         query_runner = QueryRunner(
             index_struct=self._index_struct,
             service_context=self._service_context,
+            query_context={self._index_struct.index_id: self.query_context},
             docstore=self._docstore,
             query_configs=[query_config],
             query_transform=query_transform,
             recursive=False,
             use_async=use_async,
         )
         return query_runner.query(query_str)
@@ -272,17 +283,18 @@
         # TODO: pass in query config directly
         query_config = QueryConfig(
             index_struct_type=self._index_struct.get_type(),
             query_mode=mode_enum,
             query_kwargs=query_kwargs,
         )
         query_runner = QueryRunner(
-            self._index_struct,
-            self._service_context,
-            self._docstore,
+            index_struct=self._index_struct,
+            service_context=self._service_context,
+            query_context={self._index_struct.index_id: self.query_context},
+            docstore=self._docstore,
             query_configs=[query_config],
             query_transform=query_transform,
             recursive=False,
             use_async=use_async,
         )
         return await query_runner.aquery(query_str)
```

### Comparing `llama_index-0.5.8/llama_index/indices/common/struct_store/base.py` & `llama_index-0.5.9/llama_index/indices/common/struct_store/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/common/struct_store/schema.py` & `llama_index-0.5.9/llama_index/indices/common/struct_store/schema.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/common/struct_store/sql.py` & `llama_index-0.5.9/llama_index/indices/common/struct_store/sql.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/common_tree/base.py` & `llama_index-0.5.9/llama_index/indices/common_tree/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/composability/graph.py` & `llama_index-0.5.9/llama_index/indices/composability/graph.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,19 +1,27 @@
 """Composability graphs."""
 
 import json
 from typing import Any, Dict, List, Optional, Sequence, Type, Union, cast
 
-from llama_index.constants import DOCSTORE_KEY, INDEX_STRUCT_KEY
+from llama_index.constants import (
+    ADDITIONAL_QUERY_CONTEXT_KEY,
+    DOCSTORE_KEY,
+    INDEX_STRUCT_KEY,
+)
 from llama_index.data_structs.data_structs_v2 import CompositeIndex
 from llama_index.data_structs.data_structs_v2 import V2IndexStruct
 from llama_index.data_structs.data_structs_v2 import V2IndexStruct as IndexStruct
 from llama_index.data_structs.node_v2 import IndexNode, DocumentRelationship
 from llama_index.docstore import DocumentStore
 from llama_index.indices.base import BaseGPTIndex
+from llama_index.indices.composability.utils import (
+    load_query_context_from_dict,
+    save_query_context_to_dict,
+)
 from llama_index.indices.query.query_runner import QueryRunner
 from llama_index.indices.query.query_transform.base import BaseQueryTransform
 from llama_index.indices.query.schema import QueryBundle, QueryConfig
 from llama_index.indices.service_context import ServiceContext
 from llama_index.response.schema import RESPONSE_TYPE
 
 # TMP: refactor query config type
@@ -24,19 +32,22 @@
     """Composable graph."""
 
     def __init__(
         self,
         index_struct: CompositeIndex,
         docstore: DocumentStore,
         service_context: Optional[ServiceContext] = None,
+        query_context: Optional[Dict[str, Dict[str, Any]]] = None,
+        **kwargs: Any,
     ) -> None:
         """Init params."""
         self._docstore = docstore
         self._index_struct = index_struct
         self._service_context = service_context or ServiceContext.from_defaults()
+        self._query_context = query_context or {}
 
     @property
     def index_struct(self) -> CompositeIndex:
         return self._index_struct
 
     @property
     def service_context(self) -> ServiceContext:
@@ -44,39 +55,38 @@
 
     @classmethod
     def from_index_structs_and_docstores(
         cls,
         all_index_structs: Dict[str, IndexStruct],
         root_id: str,
         docstores: Sequence[DocumentStore],
-        **kwargs: Any,
+        query_context: Optional[Dict[str, Dict[str, Any]]] = None,
+        service_context: Optional[ServiceContext] = None,
     ) -> "ComposableGraph":
         composite_index_struct = CompositeIndex(
             all_index_structs=all_index_structs,
             root_id=root_id,
         )
         merged_docstore = DocumentStore.merge(docstores)
         return cls(
-            index_struct=composite_index_struct, docstore=merged_docstore, **kwargs
+            index_struct=composite_index_struct,
+            docstore=merged_docstore,
+            query_context=query_context,
+            service_context=service_context,
         )
 
     @classmethod
     def from_indices(
         cls,
         root_index_cls: Type[BaseGPTIndex],
         children_indices: Sequence[BaseGPTIndex],
         index_summaries: Optional[Sequence[str]] = None,
         **kwargs: Any,
     ) -> "ComposableGraph":  # type: ignore
-        """Create composable graph using this index class as the root.
-
-        NOTE: this is mostly syntactic sugar,
-        roughly equivalent to directly calling `ComposableGraph.from_indices`.
-
-        """
+        """Create composable graph using this index class as the root."""
         if index_summaries is None:
             for index in children_indices:
                 if index.index_struct.summary is None:
                     raise ValueError(
                         "Summary must be set for children indices. If the index does "
                         "a summary (through index.index_struct.summary), then it must "
                         "be specified with then `index_summaries` "
@@ -112,35 +122,44 @@
             **kwargs,
         )
         # type: ignore
         all_indices: List[BaseGPTIndex] = cast(List[BaseGPTIndex], children_indices) + [
             root_index
         ]
 
+        # collect query context, e.g. vector stores
+        query_context: Dict[str, Dict[str, Any]] = {}
+        for index in list(children_indices) + [root_index]:
+            assert isinstance(index.index_struct, V2IndexStruct)
+            index_id = index.index_struct.index_id
+            query_context[index_id] = index.query_context
+
         return cls.from_index_structs_and_docstores(
             all_index_structs={
                 index.index_struct.index_id: index.index_struct for index in all_indices
             },
             root_id=root_index.index_struct.index_id,
             docstores=[index.docstore for index in all_indices],
             service_context=root_index.service_context,
+            query_context=query_context,
         )
 
     def query(
         self,
         query_str: Union[str, QueryBundle],
         query_configs: Optional[List[QUERY_CONFIG_TYPE]] = None,
         query_transform: Optional[BaseQueryTransform] = None,
         service_context: Optional[ServiceContext] = None,
     ) -> RESPONSE_TYPE:
         """Query the index."""
         service_context = service_context or self._service_context
         query_runner = QueryRunner(
             index_struct=self._index_struct,
             service_context=service_context,
+            query_context=self._query_context,
             docstore=self._docstore,
             query_configs=query_configs,
             query_transform=query_transform,
             recursive=True,
         )
         return query_runner.query(query_str)
 
@@ -152,14 +171,15 @@
         service_context: Optional[ServiceContext] = None,
     ) -> RESPONSE_TYPE:
         """Query the index."""
         service_context = service_context or self._service_context
         query_runner = QueryRunner(
             index_struct=self._index_struct,
             service_context=service_context,
+            query_context=self._query_context,
             docstore=self._docstore,
             query_configs=query_configs,
             query_transform=query_transform,
             recursive=True,
         )
         return await query_runner.aquery(query_str)
 
@@ -189,19 +209,32 @@
         Returns:
             BaseGPTIndex: The loaded index.
 
         """
         # lazy load registry
         from llama_index.indices.registry import load_index_struct_from_dict
 
-        result_dict = json.loads(index_string)
-        index_struct = load_index_struct_from_dict(result_dict["index_struct"])
-        docstore = DocumentStore.load_from_dict(result_dict["docstore"])
+        result_dict: Dict[str, Any] = json.loads(index_string)
+        index_struct = load_index_struct_from_dict(result_dict[INDEX_STRUCT_KEY])
+        docstore = DocumentStore.load_from_dict(result_dict[DOCSTORE_KEY])
+
+        # NOTE: this allows users to pass in kwargs at load time
+        #       e.g. passing in vector store client
+        query_context_kwargs = kwargs.pop("query_context_kwargs", None)
+        query_context = load_query_context_from_dict(
+            result_dict.get(ADDITIONAL_QUERY_CONTEXT_KEY, {}),
+            query_context_kwargs=query_context_kwargs,
+        )
         assert isinstance(index_struct, CompositeIndex)
-        return cls(index_struct, docstore, **kwargs)
+        return cls(
+            index_struct=index_struct,
+            docstore=docstore,
+            query_context=query_context,
+            **kwargs,
+        )
 
     @classmethod
     def load_from_disk(cls, save_path: str, **kwargs: Any) -> "ComposableGraph":
         """Load index from disk.
 
         This method loads the index from a JSON file stored on disk. The index data
         structure itself is preserved completely. If the index is defined over
@@ -227,14 +260,17 @@
         Args:
             save_path (str): The save_path of the file.
 
         """
         out_dict: Dict[str, Any] = {
             INDEX_STRUCT_KEY: self._index_struct.to_dict(),
             DOCSTORE_KEY: self._docstore.serialize_to_dict(),
+            ADDITIONAL_QUERY_CONTEXT_KEY: save_query_context_to_dict(
+                self._query_context
+            ),
         }
         return json.dumps(out_dict)
 
     def save_to_disk(self, save_path: str, **save_kwargs: Any) -> None:
         """Save to file.
 
         This method stores the index into a JSON file stored on disk.
```

### Comparing `llama_index-0.5.8/llama_index/indices/empty/base.py` & `llama_index-0.5.9/llama_index/indices/empty/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/empty/query.py` & `llama_index-0.5.9/llama_index/indices/empty/query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/keyword_table/__init__.py` & `llama_index-0.5.9/llama_index/indices/keyword_table/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/keyword_table/base.py` & `llama_index-0.5.9/llama_index/indices/keyword_table/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/keyword_table/query.py` & `llama_index-0.5.9/llama_index/indices/keyword_table/query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/keyword_table/rake_base.py` & `llama_index-0.5.9/llama_index/indices/keyword_table/rake_base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/keyword_table/simple_base.py` & `llama_index-0.5.9/llama_index/indices/keyword_table/simple_base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/keyword_table/utils.py` & `llama_index-0.5.9/llama_index/indices/keyword_table/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/knowledge_graph/base.py` & `llama_index-0.5.9/llama_index/indices/knowledge_graph/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/knowledge_graph/query.py` & `llama_index-0.5.9/llama_index/indices/knowledge_graph/query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/list/base.py` & `llama_index-0.5.9/llama_index/indices/list/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/list/embedding_query.py` & `llama_index-0.5.9/llama_index/indices/list/embedding_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/list/query.py` & `llama_index-0.5.9/llama_index/indices/list/query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/postprocessor/node.py` & `llama_index-0.5.9/llama_index/indices/postprocessor/node.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/prompt_helper.py` & `llama_index-0.5.9/llama_index/indices/prompt_helper.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/query/base.py` & `llama_index-0.5.9/llama_index/indices/query/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/query/embedding_utils.py` & `llama_index-0.5.9/llama_index/indices/query/embedding_utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/query/query_combiner/base.py` & `llama_index-0.5.9/llama_index/indices/query/query_combiner/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/query/query_runner.py` & `llama_index-0.5.9/llama_index/indices/query/query_runner.py`

 * *Files 2% similar despite different names*

```diff
@@ -81,25 +81,27 @@
     """
 
     def __init__(
         self,
         index_struct: IndexStruct,
         service_context: ServiceContext,
         docstore: DocumentStore,
+        query_context: Dict[str, Dict[str, Any]],
         query_configs: Optional[List[QUERY_CONFIG_TYPE]] = None,
         query_transform: Optional[BaseQueryTransform] = None,
         query_combiner: Optional[BaseQueryCombiner] = None,
         recursive: bool = False,
         use_async: bool = False,
     ) -> None:
         """Init params."""
         # data and services
         self._index_struct = index_struct
         self._service_context = service_context
         self._docstore = docstore
+        self._query_context = query_context
 
         # query configurations and transformation
         self._query_config_map = _get_query_config_map(query_configs)
         self._query_transform = query_transform or IdentityQueryTransform()
         self._query_combiner = query_combiner
 
         # additional configs
@@ -160,14 +162,19 @@
         config = self._query_config_map.get(index_struct)
         mode = config.query_mode
 
         from llama_index.indices.registry import INDEX_STRUT_TYPE_TO_QUERY_MAP
 
         query_cls = INDEX_STRUT_TYPE_TO_QUERY_MAP[index_struct_type][mode]
         query_kwargs = self._get_query_kwargs(config)
+
+        # Inject additional query context into query kwargs
+        query_context = self._query_context.get(index_struct.index_id, {})
+        query_kwargs.update(query_context)
+
         query_obj = query_cls(
             index_struct=index_struct,
             docstore=self._docstore,
             **query_kwargs,
         )
 
         return query_obj
@@ -205,15 +212,15 @@
         self,
         node_with_score: NodeWithScore,
         query_bundle: QueryBundle,
         level: int,
     ) -> Tuple[NodeWithScore, List[NodeWithScore]]:
         """Fetch nodes.
 
-        Usees existing node if it's not an index node.
+        Uses existing node if it's not an index node.
         Otherwise fetch response from corresponding index.
 
         """
         if isinstance(node_with_score.node, IndexNode):
             index_node = node_with_score.node
             # recursive call
             response = self.query(query_bundle, index_node.index_id, level + 1)
```

### Comparing `llama_index-0.5.8/llama_index/indices/query/query_transform/base.py` & `llama_index-0.5.9/llama_index/indices/query/query_transform/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/query/query_transform/prompts.py` & `llama_index-0.5.9/llama_index/indices/query/query_transform/prompts.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/query/schema.py` & `llama_index-0.5.9/llama_index/indices/query/schema.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/registry.py` & `llama_index-0.5.9/llama_index/indices/registry.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/response/builder.py` & `llama_index-0.5.9/llama_index/indices/response/builder.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/service_context.py` & `llama_index-0.5.9/llama_index/indices/service_context.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/__init__.py` & `llama_index-0.5.9/llama_index/indices/struct_store/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/base.py` & `llama_index-0.5.9/llama_index/indices/struct_store/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/container_builder.py` & `llama_index-0.5.9/llama_index/indices/struct_store/container_builder.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/pandas.py` & `llama_index-0.5.9/llama_index/indices/struct_store/pandas.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/pandas_query.py` & `llama_index-0.5.9/llama_index/indices/struct_store/pandas_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/sql.py` & `llama_index-0.5.9/llama_index/indices/struct_store/sql.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/struct_store/sql_query.py` & `llama_index-0.5.9/llama_index/indices/struct_store/sql_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/tree/base.py` & `llama_index-0.5.9/llama_index/indices/tree/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/tree/embedding_query.py` & `llama_index-0.5.9/llama_index/indices/tree/embedding_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/tree/inserter.py` & `llama_index-0.5.9/llama_index/indices/tree/inserter.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/tree/leaf_query.py` & `llama_index-0.5.9/llama_index/indices/tree/leaf_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/tree/retrieve_query.py` & `llama_index-0.5.9/llama_index/indices/tree/retrieve_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/tree/summarize_query.py` & `llama_index-0.5.9/llama_index/indices/tree/summarize_query.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/utils.py` & `llama_index-0.5.9/llama_index/indices/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/vector_store/__init__.py` & `llama_index-0.5.9/llama_index/indices/vector_store/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/indices/vector_store/base.py` & `llama_index-0.5.9/llama_index/indices/vector_store/base.py`

 * *Files 4% similar despite different names*

```diff
@@ -3,22 +3,26 @@
 An index that that is built on top of an existing vector store.
 
 """
 
 from typing import Any, Dict, List, Optional, Sequence, Set, Tuple
 
 from llama_index.async_utils import run_async_tasks
-from llama_index.constants import VECTOR_STORE_CONFIG_DICT_KEY
+from llama_index.constants import VECTOR_STORE_KEY
 from llama_index.data_structs.data_structs_v2 import IndexDict
-from llama_index.data_structs.node_v2 import Node
+from llama_index.data_structs.node_v2 import ImageNode, IndexNode, Node
 from llama_index.indices.base import BaseGPTIndex, QueryMap
 from llama_index.indices.query.schema import QueryMode
 from llama_index.indices.service_context import ServiceContext
 from llama_index.indices.vector_store.base_query import GPTVectorStoreIndexQuery
 from llama_index.token_counter.token_counter import llm_token_counter
+from llama_index.vector_stores.registry import (
+    load_vector_store_from_dict,
+    save_vector_store_to_dict,
+)
 from llama_index.vector_stores.simple import SimpleVectorStore
 from llama_index.vector_stores.types import NodeEmbeddingResult, VectorStore
 
 
 class GPTVectorStoreIndex(BaseGPTIndex[IndexDict]):
     """Base GPT Vector Store Index.
 
@@ -174,20 +178,27 @@
         embedding_results = self._get_node_embedding_results(
             nodes,
             set(),
         )
 
         new_ids = self._vector_store.add(embedding_results)
 
-        # if the vector store doesn't store text, we need to add the nodes to the
-        # index struct and document store
         if not self._vector_store.stores_text:
+            # NOTE: if the vector store doesn't store text,
+            # we need to add the nodes to the index struct and document store
             for result, new_id in zip(embedding_results, new_ids):
                 index_struct.add_node(result.node, text_id=new_id)
                 self._docstore.add_documents([result.node], allow_update=True)
+        else:
+            # NOTE: if the vector store keeps text,
+            # we only need to add image and index nodes
+            for result, new_id in zip(embedding_results, new_ids):
+                if isinstance(result.node, (ImageNode, IndexNode)):
+                    index_struct.add_node(result.node, text_id=new_id)
+                    self._docstore.add_documents([result.node], allow_update=True)
 
     def _build_index_from_nodes(self, nodes: Sequence[Node]) -> IndexDict:
         """Build index from nodes."""
         index_struct = self.index_struct_cls()
         if self._use_async:
             tasks = [self._async_add_nodes_to_index(index_struct, nodes)]
             run_async_tasks(tasks)
@@ -242,18 +253,18 @@
         Args:
             index_string (str): The index string (in JSON-format).
 
         Returns:
             BaseGPTIndex: The loaded index.
 
         """
-        config_dict = {}
-        if VECTOR_STORE_CONFIG_DICT_KEY in result_dict:
-            config_dict = result_dict[VECTOR_STORE_CONFIG_DICT_KEY]
-        return super().load_from_dict(result_dict, **config_dict, **kwargs)
+        vector_store = load_vector_store_from_dict(
+            result_dict[VECTOR_STORE_KEY], **kwargs
+        )
+        return super().load_from_dict(result_dict, vector_store=vector_store, **kwargs)
 
     def save_to_dict(self, **save_kwargs: Any) -> dict:
         """Save to string.
 
         This method stores the index into a JSON string.
 
         NOTE: save_to_string should not be used for indices composed on top
@@ -261,15 +272,13 @@
         `save_to_string` and `load_from_string` on that instead.
 
         Returns:
             dict: The JSON dict of the index.
 
         """
         out_dict = super().save_to_dict()
-        out_dict[VECTOR_STORE_CONFIG_DICT_KEY] = self._vector_store.config_dict
+        out_dict[VECTOR_STORE_KEY] = save_vector_store_to_dict(self._vector_store)
         return out_dict
 
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        super()._preprocess_query(mode, query_kwargs)
-        # NOTE: Pass along vector store instance to query objects
-        # TODO: refactor this to be more explicit
-        query_kwargs["vector_store"] = self._vector_store
+    @property
+    def query_context(self) -> Dict[str, Any]:
+        return {"vector_store": self._vector_store}
```

### Comparing `llama_index-0.5.8/llama_index/indices/vector_store/base_query.py` & `llama_index-0.5.9/llama_index/indices/vector_store/base_query.py`

 * *Files 15% similar despite different names*

```diff
@@ -65,23 +65,32 @@
                 [],
                 self._similarity_top_k,
                 self._doc_ids,
                 query_str=query_bundle.query_str,
             )
 
         if query_result.nodes is None:
+            # NOTE: vector store does not keep text and returns node indices.
+            # Need to recover all nodes from docstore
             if query_result.ids is None:
                 raise ValueError(
                     "Vector store query result should return at "
                     "least one of nodes or ids."
                 )
             assert isinstance(self._index_struct, IndexDict)
             node_ids = [self._index_struct.nodes_dict[idx] for idx in query_result.ids]
             nodes = self._docstore.get_nodes(node_ids)
             query_result.nodes = nodes
+        else:
+            # NOTE: vector store keeps text, returns nodes.
+            # Only need to recover image or index nodes from docstore
+            for i in range(len(query_result.nodes)):
+                node_id = query_result.nodes[i].get_doc_id()
+                if node_id in self._docstore.docs:
+                    query_result.nodes[i] = self._docstore.get_node(node_id)
 
         log_vector_store_query_result(query_result)
 
         if similarity_tracker is not None and query_result.similarities is not None:
             for node, similarity in zip(query_result.nodes, query_result.similarities):
                 similarity_tracker.add(node, similarity)
```

### Comparing `llama_index-0.5.8/llama_index/indices/vector_store/vector_indices.py` & `llama_index-0.5.9/llama_index/indices/vector_store/vector_indices.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 """Deprecated vector store indices."""
 
-from typing import Any, Dict, Optional, Sequence, Type, cast
+from typing import Any, Dict, Optional, Sequence, Type
 
 from requests.adapters import Retry
 
 from llama_index.data_structs.data_structs_v2 import (
     ChatGPTRetrievalPluginIndexDict,
     ChromaIndexDict,
     FaissIndexDict,
@@ -12,26 +12,15 @@
     OpensearchIndexDict,
     PineconeIndexDict,
     QdrantIndexDict,
     SimpleIndexDict,
     WeaviateIndexDict,
 )
 from llama_index.data_structs.node_v2 import Node
-from llama_index.indices.base import BaseGPTIndex, QueryMap
-from llama_index.indices.query.schema import QueryMode
-from llama_index.indices.vector_store.queries import (
-    ChatGPTRetrievalPluginQuery,
-    GPTChromaIndexQuery,
-    GPTFaissIndexQuery,
-    GPTOpensearchIndexQuery,
-    GPTPineconeIndexQuery,
-    GPTQdrantIndexQuery,
-    GPTSimpleVectorIndexQuery,
-    GPTWeaviateIndexQuery,
-)
+from llama_index.indices.base import BaseGPTIndex
 from llama_index.indices.service_context import ServiceContext
 from llama_index.indices.vector_store.base import GPTVectorStoreIndex
 from llama_index.vector_stores import (
     ChatGPTRetrievalPluginClient,
     ChromaVectorStore,
     FaissVectorStore,
     PineconeVectorStore,
@@ -67,56 +56,26 @@
     index_struct_cls: Type[IndexDict] = SimpleIndexDict
 
     def __init__(
         self,
         nodes: Optional[Sequence[Node]] = None,
         index_struct: Optional[IndexDict] = None,
         service_context: Optional[ServiceContext] = None,
-        simple_vector_store_data_dict: Optional[dict] = None,
+        vector_store: Optional[SimpleVectorStore] = None,
         **kwargs: Any,
     ) -> None:
         """Init params."""
-        # TODO: temporary hack to "infer" vector store from
-        # index struct if index_struct exists
-        if index_struct is not None and len(index_struct.embeddings_dict) > 0:
-            simple_vector_store_data_dict = {
-                "embedding_dict": index_struct.embeddings_dict,
-            }
-
-        vector_store = SimpleVectorStore(
-            simple_vector_store_data_dict=simple_vector_store_data_dict
-        )
-
         super().__init__(
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
-        # TODO: Temporary hack to also store embeddings in index_struct
-        embedding_dict = vector_store._data.embedding_dict
-        self._index_struct.embeddings_dict = embedding_dict
-
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTSimpleVectorIndexQuery,
-            QueryMode.EMBEDDING: GPTSimpleVectorIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(SimpleVectorStore, self._vector_store)
-        query_kwargs["simple_vector_store_data_dict"] = vector_store._data
-
 
 class GPTFaissIndex(GPTVectorStoreIndex):
     """GPT Faiss Index.
 
     The GPTFaissIndex is a data structure where nodes are keyed by
     embeddings, and those embeddings are stored within a Faiss index.
     During index construction, the document texts are chunked up,
@@ -154,29 +113,14 @@
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
     @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTFaissIndexQuery,
-            QueryMode.EMBEDDING: GPTFaissIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(FaissVectorStore, self._vector_store)
-        query_kwargs["faiss_index"] = vector_store._faiss_index
-
-    @classmethod
     def load_from_disk(
         cls, save_path: str, faiss_index_save_path: Optional[str] = None, **kwargs: Any
     ) -> "BaseGPTIndex":
         """Load index from disk.
 
         This method loads the index from a JSON file stored on disk. The index data
         structure itself is preserved completely. If the index is defined over
@@ -256,69 +200,50 @@
 
     index_struct_cls: Type[IndexDict] = PineconeIndexDict
 
     def __init__(
         self,
         nodes: Optional[Sequence[Node]] = None,
         pinecone_index: Optional[Any] = None,
+        index_name: Optional[str] = None,
+        environment: Optional[str] = None,
         metadata_filters: Optional[Dict[str, Any]] = None,
         pinecone_kwargs: Optional[Dict] = None,
         insert_kwargs: Optional[Dict] = None,
         query_kwargs: Optional[Dict] = None,
         delete_kwargs: Optional[Dict] = None,
         index_struct: Optional[IndexDict] = None,
         service_context: Optional[ServiceContext] = None,
+        vector_store: Optional[PineconeVectorStore] = None,
         **kwargs: Any,
     ) -> None:
         """Init params."""
-        if pinecone_index is None:
-            raise ValueError("pinecone_index is required.")
-        if pinecone_kwargs is None:
-            pinecone_kwargs = {}
-
-        vector_store = kwargs.pop(
-            "vector_store",
-            PineconeVectorStore(
+        pinecone_kwargs = pinecone_kwargs or {}
+
+        if vector_store is None:
+            vector_store = PineconeVectorStore(
                 pinecone_index=pinecone_index,
+                index_name=index_name,
+                environment=environment,
                 metadata_filters=metadata_filters,
                 pinecone_kwargs=pinecone_kwargs,
                 insert_kwargs=insert_kwargs,
                 query_kwargs=query_kwargs,
                 delete_kwargs=delete_kwargs,
-            ),
-        )
+            )
+        assert vector_store is not None
 
         super().__init__(
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTPineconeIndexQuery,
-            QueryMode.EMBEDDING: GPTPineconeIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(PineconeVectorStore, self._vector_store)
-        query_kwargs["pinecone_index"] = vector_store._pinecone_index
-        query_kwargs["metadata_filters"] = vector_store._metadata_filters
-        query_kwargs["pinecone_kwargs"] = vector_store._pinecone_kwargs
-        query_kwargs["insert_kwargs"] = vector_store._insert_kwargs
-        query_kwargs["query_kwargs"] = vector_store._query_kwargs
-        query_kwargs["delete_kwargs"] = vector_store._delete_kwargs
-
 
 class GPTWeaviateIndex(GPTVectorStoreIndex):
     """GPT Weaviate Index.
 
     The GPTWeaviateIndex is a data structure where nodes are keyed by
     embeddings, and those embeddings are stored within a Weaviate index.
     During index construction, the document texts are chunked up,
@@ -356,30 +281,14 @@
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTWeaviateIndexQuery,
-            QueryMode.EMBEDDING: GPTWeaviateIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(WeaviateVectorStore, self._vector_store)
-        query_kwargs["weaviate_client"] = vector_store._client
-        query_kwargs["class_prefix"] = vector_store._class_prefix
-
 
 class GPTQdrantIndex(GPTVectorStoreIndex):
     """GPT Qdrant Index.
 
     The GPTQdrantIndex is a data structure where nodes are keyed by
     embeddings, and those embeddings are stored within a Qdrant collection.
     During index construction, the document texts are chunked up,
@@ -419,30 +328,14 @@
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTQdrantIndexQuery,
-            QueryMode.EMBEDDING: GPTQdrantIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(QdrantVectorStore, self._vector_store)
-        query_kwargs["client"] = vector_store._client
-        query_kwargs["collection_name"] = vector_store._collection_name
-
 
 class GPTChromaIndex(GPTVectorStoreIndex):
     """GPT Chroma Index.
 
     The GPTChromaIndex is a data structure where nodes are keyed by
     embeddings, and those embeddings are stored within a Chroma collection.
     During index construction, the document texts are chunked up,
@@ -479,29 +372,14 @@
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTChromaIndexQuery,
-            QueryMode.EMBEDDING: GPTChromaIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(ChromaVectorStore, self._vector_store)
-        query_kwargs["chroma_collection"] = vector_store._collection
-
 
 class GPTOpensearchIndex(GPTVectorStoreIndex):
     """GPT Opensearch Index.
 
     The GPTOpensearchIndex is a data structure where nodes are keyed by
     embeddings, and those embeddings are stored in a document that is indexed
     with its embedding as well as its textual data (text field is defined in
@@ -542,29 +420,14 @@
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
 
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: GPTOpensearchIndexQuery,
-            QueryMode.EMBEDDING: GPTOpensearchIndexQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(OpensearchVectorStore, self._vector_store)
-        query_kwargs["client"] = vector_store._client
-
 
 class ChatGPTRetrievalPluginIndex(GPTVectorStoreIndex):
     """ChatGPTRetrievalPlugin index.
 
     This index directly interfaces with any server that hosts
     the ChatGPT Retrieval Plugin interface:
     https://github.com/openai/chatgpt-retrieval-plugin.
@@ -605,25 +468,7 @@
         super().__init__(
             nodes=nodes,
             index_struct=index_struct,
             service_context=service_context,
             vector_store=vector_store,
             **kwargs,
         )
-
-    @classmethod
-    def get_query_map(self) -> QueryMap:
-        """Get query map."""
-        return {
-            QueryMode.DEFAULT: ChatGPTRetrievalPluginQuery,
-            QueryMode.EMBEDDING: ChatGPTRetrievalPluginQuery,
-        }
-
-    def _preprocess_query(self, mode: QueryMode, query_kwargs: Any) -> None:
-        """Preprocess query."""
-        super()._preprocess_query(mode, query_kwargs)
-        del query_kwargs["vector_store"]
-        vector_store = cast(ChatGPTRetrievalPluginClient, self._vector_store)
-        query_kwargs["endpoint_url"] = vector_store._endpoint_url
-        query_kwargs["bearer_token"] = vector_store._bearer_token
-        query_kwargs["retries"] = vector_store._retries
-        query_kwargs["batch_size"] = vector_store._batch_size
```

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/agents/__init__.py` & `llama_index-0.5.9/llama_index/langchain_helpers/agents/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/agents/agents.py` & `llama_index-0.5.9/llama_index/langchain_helpers/agents/agents.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/agents/toolkits.py` & `llama_index-0.5.9/llama_index/langchain_helpers/agents/toolkits.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/agents/tools.py` & `llama_index-0.5.9/llama_index/langchain_helpers/agents/tools.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/memory_wrapper.py` & `llama_index-0.5.9/llama_index/langchain_helpers/memory_wrapper.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/sql_wrapper.py` & `llama_index-0.5.9/llama_index/langchain_helpers/sql_wrapper.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/langchain_helpers/text_splitter.py` & `llama_index-0.5.9/llama_index/langchain_helpers/text_splitter.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/llm_predictor/base.py` & `llama_index-0.5.9/llama_index/llm_predictor/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/llm_predictor/chatgpt.py` & `llama_index-0.5.9/llama_index/llm_predictor/chatgpt.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/llm_predictor/structured.py` & `llama_index-0.5.9/llama_index/llm_predictor/structured.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/logger/base.py` & `llama_index-0.5.9/llama_index/logger/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/node_parser/interface.py` & `llama_index-0.5.9/llama_index/node_parser/interface.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/node_parser/node_utils.py` & `llama_index-0.5.9/llama_index/node_parser/node_utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/node_parser/simple.py` & `llama_index-0.5.9/llama_index/node_parser/simple.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/old_docstore.py` & `llama_index-0.5.9/llama_index/old_docstore.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/optimization/optimizer.py` & `llama_index-0.5.9/llama_index/optimization/optimizer.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/output_parsers/base.py` & `llama_index-0.5.9/llama_index/output_parsers/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/output_parsers/guardrails.py` & `llama_index-0.5.9/llama_index/output_parsers/guardrails.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/output_parsers/langchain.py` & `llama_index-0.5.9/llama_index/output_parsers/langchain.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/playground/base.py` & `llama_index-0.5.9/llama_index/playground/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/prompts/base.py` & `llama_index-0.5.9/llama_index/prompts/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/prompts/chat_prompts.py` & `llama_index-0.5.9/llama_index/prompts/chat_prompts.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/prompts/default_prompt_selectors.py` & `llama_index-0.5.9/llama_index/prompts/default_prompt_selectors.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/prompts/default_prompts.py` & `llama_index-0.5.9/llama_index/prompts/default_prompts.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/prompts/prompt_type.py` & `llama_index-0.5.9/llama_index/prompts/prompt_type.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/prompts/prompts.py` & `llama_index-0.5.9/llama_index/prompts/prompts.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/__init__.py` & `llama_index-0.5.9/llama_index/readers/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/base.py` & `llama_index-0.5.9/llama_index/readers/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/chatgpt_plugin/base.py` & `llama_index-0.5.9/llama_index/readers/chatgpt_plugin/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/chroma.py` & `llama_index-0.5.9/llama_index/readers/chroma.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/database.py` & `llama_index-0.5.9/llama_index/readers/database.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/discord_reader.py` & `llama_index-0.5.9/llama_index/readers/discord_reader.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/download.py` & `llama_index-0.5.9/llama_index/readers/download.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/elasticsearch.py` & `llama_index-0.5.9/llama_index/readers/elasticsearch.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/faiss.py` & `llama_index-0.5.9/llama_index/readers/faiss.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/base.py` & `llama_index-0.5.9/llama_index/readers/file/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/base_parser.py` & `llama_index-0.5.9/llama_index/readers/file/base_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/docs_parser.py` & `llama_index-0.5.9/llama_index/readers/file/docs_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/epub_parser.py` & `llama_index-0.5.9/llama_index/readers/file/epub_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/image_parser.py` & `llama_index-0.5.9/llama_index/readers/file/image_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/markdown_parser.py` & `llama_index-0.5.9/llama_index/readers/file/markdown_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/mbox_parser.py` & `llama_index-0.5.9/llama_index/readers/file/mbox_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/slides_parser.py` & `llama_index-0.5.9/llama_index/readers/file/slides_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/tabular_parser.py` & `llama_index-0.5.9/llama_index/readers/file/tabular_parser.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/file/video_audio.py` & `llama_index-0.5.9/llama_index/readers/file/video_audio.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/github_readers/github_api_client.py` & `llama_index-0.5.9/llama_index/readers/github_readers/github_api_client.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/github_readers/github_repository_reader.py` & `llama_index-0.5.9/llama_index/readers/github_readers/github_repository_reader.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/github_readers/utils.py` & `llama_index-0.5.9/llama_index/readers/github_readers/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/google_readers/gdocs.py` & `llama_index-0.5.9/llama_index/readers/google_readers/gdocs.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/google_readers/gsheets.py` & `llama_index-0.5.9/llama_index/readers/google_readers/gsheets.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/json.py` & `llama_index-0.5.9/llama_index/readers/json.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/make_com/wrapper.py` & `llama_index-0.5.9/llama_index/readers/make_com/wrapper.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/mbox.py` & `llama_index-0.5.9/llama_index/readers/mbox.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/mongo.py` & `llama_index-0.5.9/llama_index/readers/mongo.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/notion.py` & `llama_index-0.5.9/llama_index/readers/notion.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/obsidian.py` & `llama_index-0.5.9/llama_index/readers/obsidian.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/pinecone.py` & `llama_index-0.5.9/llama_index/readers/pinecone.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/qdrant.py` & `llama_index-0.5.9/llama_index/readers/qdrant.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/schema/base.py` & `llama_index-0.5.9/llama_index/readers/schema/base.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/slack.py` & `llama_index-0.5.9/llama_index/readers/slack.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/steamship/file_reader.py` & `llama_index-0.5.9/llama_index/readers/steamship/file_reader.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/string_iterable.py` & `llama_index-0.5.9/llama_index/readers/string_iterable.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/twitter.py` & `llama_index-0.5.9/llama_index/readers/twitter.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/weaviate/data_structs.py` & `llama_index-0.5.9/llama_index/readers/weaviate/data_structs.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/weaviate/reader.py` & `llama_index-0.5.9/llama_index/readers/weaviate/reader.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/weaviate/utils.py` & `llama_index-0.5.9/llama_index/readers/weaviate/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/web.py` & `llama_index-0.5.9/llama_index/readers/web.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/wikipedia.py` & `llama_index-0.5.9/llama_index/readers/wikipedia.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/readers/youtube_transcript.py` & `llama_index-0.5.9/llama_index/readers/youtube_transcript.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/response/notebook_utils.py` & `llama_index-0.5.9/llama_index/response/notebook_utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/response/schema.py` & `llama_index-0.5.9/llama_index/response/schema.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/schema.py` & `llama_index-0.5.9/llama_index/schema.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/token_counter/mock_chain_wrapper.py` & `llama_index-0.5.9/llama_index/token_counter/mock_chain_wrapper.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/token_counter/mock_embed_model.py` & `llama_index-0.5.9/llama_index/token_counter/mock_embed_model.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/token_counter/token_counter.py` & `llama_index-0.5.9/llama_index/token_counter/token_counter.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/token_counter/utils.py` & `llama_index-0.5.9/llama_index/token_counter/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/tools/file_utils.py` & `llama_index-0.5.9/llama_index/tools/file_utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/tools/migrate_v1_to_v2.py` & `llama_index-0.5.9/llama_index/tools/migrate_v1_to_v2.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/utils.py` & `llama_index-0.5.9/llama_index/utils.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/vector_stores/__init__.py` & `llama_index-0.5.9/llama_index/vector_stores/__init__.py`

 * *Files identical despite different names*

### Comparing `llama_index-0.5.8/llama_index/vector_stores/chatgpt_plugin.py` & `llama_index-0.5.9/llama_index/vector_stores/chatgpt_plugin.py`

 * *Files 7% similar despite different names*

```diff
@@ -77,23 +77,31 @@
         self._bearer_token = bearer_token or os.getenv("BEARER_TOKEN")
         self._retries = retries
         self._batch_size = batch_size
 
         self._s = requests.Session()
         self._s.mount("http://", HTTPAdapter(max_retries=self._retries))
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "VectorStore":
+        return cls(**config_dict)
+
     @property
     def client(self) -> None:
         """Get client."""
         return None
 
     @property
     def config_dict(self) -> dict:
         """Get config dict."""
-        return {"batch_size": self._batch_size}
+        return {
+            "endpoint_url": self._endpoint_url,
+            "batch_size": self._batch_size,
+            "retries": self._retries,
+        }
 
     def add(
         self,
         embedding_results: List[NodeEmbeddingResult],
     ) -> List[str]:
         """Add embedding_results to index."""
         headers = {"Authorization": f"Bearer {self._bearer_token}"}
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/chroma.py` & `llama_index-0.5.9/llama_index/vector_stores/chroma.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 """Chroma vector store."""
 import logging
 import math
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 from llama_index.data_structs.node_v2 import DocumentRelationship, Node
 from llama_index.utils import truncate_text
 from llama_index.vector_stores.types import (
     NodeEmbeddingResult,
     VectorStore,
     VectorStoreQueryResult,
@@ -39,14 +39,20 @@
             import chromadb  # noqa: F401
         except ImportError:
             raise ImportError(import_err_msg)
         from chromadb.api.models.Collection import Collection
 
         self._collection = cast(Collection, chroma_collection)
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "VectorStore":
+        if "chroma_collection" not in config_dict:
+            raise ValueError("Missing chroma collection!")
+        return cls(**config_dict)
+
     @property
     def config_dict(self) -> dict:
         """Return config dict."""
         return {}
 
     def add(self, embedding_results: List[NodeEmbeddingResult]) -> List[str]:
         """Add embedding results to index.
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/faiss.py` & `llama_index-0.5.9/llama_index/vector_stores/faiss.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """Faiss Vector store index.
 
 An index that that is built on top of an existing vector store.
 
 """
 
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 import numpy as np
 
 from llama_index.vector_stores.types import (
     NodeEmbeddingResult,
     VectorStore,
     VectorStoreQueryResult,
@@ -26,35 +26,45 @@
     Args:
         faiss_index (faiss.Index): Faiss index instance
 
     """
 
     stores_text: bool = False
 
-    def __init__(
-        self,
-        faiss_index: Any,
-    ) -> None:
+    def __init__(self, faiss_index: Any, save_path: Optional[str] = None) -> None:
         """Initialize params."""
         import_err_msg = """
             `faiss` package not found. For instructions on
             how to install `faiss` please visit
             https://github.com/facebookresearch/faiss/wiki/Installing-Faiss
         """
         try:
             import faiss  # noqa: F401
         except ImportError:
             raise ImportError(import_err_msg)
 
         self._faiss_index = cast(faiss.Index, faiss_index)
+        self._save_path = save_path or "./faiss.json"
+
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "FaissVectorStore":
+        if "faiss_index" in config_dict:
+            return cls(**config_dict)
+        else:
+            save_path = config_dict.get("save_path", None)
+            if save_path is not None:
+                return cls.load(save_path=save_path)
+            else:
+                raise ValueError("Missing both faiss index and save path!")
 
     @property
     def config_dict(self) -> dict:
         """Return config dict."""
-        return {}
+        self.save(self._save_path)
+        return {"save_path": self._save_path}
 
     def add(
         self,
         embedding_results: List[NodeEmbeddingResult],
     ) -> List[str]:
         """Add embedding results to index.
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/opensearch.py` & `llama_index-0.5.9/llama_index/vector_stores/opensearch.py`

 * *Files 8% similar despite different names*

```diff
@@ -152,14 +152,20 @@
         import_err_msg = "`httpx` package not found, please run `pip install httpx`"
         try:
             import httpx  # noqa: F401
         except ImportError:
             raise ImportError(import_err_msg)
         self._client = client
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "VectorStore":
+        if "client" not in config_dict:
+            raise ValueError("Missing Opensearch client!")
+        return cls(**config_dict)
+
     @property
     def client(self) -> Any:
         """Get client."""
         return self._client
 
     @property
     def config_dict(self) -> dict:
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/qdrant.py` & `llama_index-0.5.9/llama_index/vector_stores/qdrant.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """Qdrant vector store index.
 
 An index that is built on top of an existing Qdrant collection.
 
 """
 import logging
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 from llama_index.data_structs.node_v2 import DocumentRelationship, Node
 from llama_index.utils import get_new_id
 from llama_index.vector_stores.types import (
     NodeEmbeddingResult,
     VectorStore,
     VectorStoreQueryResult,
@@ -42,20 +42,26 @@
         )
         try:
             import qdrant_client  # noqa: F401
         except ImportError:
             raise ImportError(import_err_msg)
 
         if client is None:
-            raise ValueError("client cannot be None.")
+            raise ValueError("Missing Qdrant client!")
 
         self._client = cast(qdrant_client.QdrantClient, client)
         self._collection_name = collection_name
         self._collection_initialized = self._collection_exists(collection_name)
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "VectorStore":
+        if "client" not in config_dict:
+            raise ValueError("Missing Qdrant client!")
+        return cls(**config_dict)
+
     @property
     def config_dict(self) -> dict:
         """Return config dict."""
         return {
             "collection_name": self._collection_name,
         }
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/simple.py` & `llama_index-0.5.9/llama_index/vector_stores/simple.py`

 * *Files 3% similar despite different names*

```diff
@@ -47,14 +47,18 @@
     ) -> None:
         """Initialize params."""
         if simple_vector_store_data_dict is None:
             self._data = SimpleVectorStoreData()
         else:
             self._data = SimpleVectorStoreData.from_dict(simple_vector_store_data_dict)
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "SimpleVectorStore":
+        return cls(**config_dict)
+
     @property
     def client(self) -> None:
         """Get client."""
         return None
 
     @property
     def config_dict(self) -> dict:
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/types.py` & `llama_index-0.5.9/llama_index/vector_stores/types.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """Vector store index types."""
 
 
 from dataclasses import dataclass
-from typing import Any, List, Optional, Protocol
+from typing import Any, Dict, List, Optional, Protocol, runtime_checkable
 
 from llama_index.data_structs.node_v2 import Node
 
 
 @dataclass
 class NodeEmbeddingResult:
     """Node embedding result.
@@ -30,20 +30,25 @@
     """Vector store query result."""
 
     nodes: Optional[List[Node]] = None
     similarities: Optional[List[float]] = None
     ids: Optional[List[str]] = None
 
 
+@runtime_checkable
 class VectorStore(Protocol):
     """Abstract vector store protocol."""
 
     stores_text: bool
     is_embedding_query: bool = True
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "VectorStore":
+        ...
+
     @property
     def client(self) -> Any:
         """Get client."""
         ...
 
     @property
     def config_dict(self) -> dict:
```

### Comparing `llama_index-0.5.8/llama_index/vector_stores/weaviate.py` & `llama_index-0.5.9/llama_index/vector_stores/weaviate.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """Weaviate Vector store index.
 
 An index that that is built on top of an existing vector store.
 
 """
 
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 from llama_index.readers.weaviate.data_structs import WeaviateNode
 from llama_index.readers.weaviate.utils import get_default_class_prefix
 from llama_index.vector_stores.types import (
     NodeEmbeddingResult,
     VectorStore,
     VectorStoreQueryResult,
@@ -45,24 +45,33 @@
         )
         try:
             import weaviate  # noqa: F401
             from weaviate import Client  # noqa: F401
         except ImportError:
             raise ImportError(import_err_msg)
 
+        if weaviate_client is None:
+            raise ValueError("Missing Weaviate client!")
+
         self._client = cast(Client, weaviate_client)
         # validate class prefix starts with a capital letter
         if class_prefix is not None and not class_prefix[0].isupper():
             raise ValueError(
                 "Class prefix must start with a capital letter, e.g. 'Gpt'"
             )
         self._class_prefix = class_prefix or get_default_class_prefix()
         # try to create schema
         WeaviateNode.create_schema(self._client, self._class_prefix)
 
+    @classmethod
+    def from_dict(cls, config_dict: Dict[str, Any]) -> "VectorStore":
+        if "weaviate_client" not in config_dict:
+            raise ValueError("Missing Weaviate client!")
+        return cls(**config_dict)
+
     @property
     def client(self) -> Any:
         """Get client."""
         return self._client
 
     @property
     def config_dict(self) -> dict:
```

### Comparing `llama_index-0.5.8/llama_index.egg-info/PKG-INFO` & `llama_index-0.5.9/llama_index.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: llama-index
-Version: 0.5.8
+Version: 0.5.9
 Summary: Interface between LLMs and your data.
 Home-page: https://github.com/jerryjliu/gpt_index
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # 🗂️ LlamaIndex 🦙 (GPT Index)
@@ -115,11 +115,11 @@
 
 ```
 @software{Liu_LlamaIndex_2022,
 author = {Liu, Jerry},
 doi = {10.5281/zenodo.1234},
 month = {11},
 title = {{LlamaIndex}},
-url = {https://github.com/jerryjliu/gpt_index},
+url = {https://github.com/jerryjliu/llama_index},
 year = {2022}
 }
 ```
```

### Comparing `llama_index-0.5.8/llama_index.egg-info/SOURCES.txt` & `llama_index-0.5.9/llama_index.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -20,15 +20,14 @@
 llama_index.egg-info/top_level.txt
 llama_index/composability/__init__.py
 llama_index/composability/base.py
 llama_index/composability/joint_qa_summary.py
 llama_index/data_structs/__init__.py
 llama_index/data_structs/data_structs.py
 llama_index/data_structs/data_structs_v2.py
-llama_index/data_structs/node_mapping.py
 llama_index/data_structs/node_v2.py
 llama_index/data_structs/struct_type.py
 llama_index/data_structs/table.py
 llama_index/data_structs/table_v2.py
 llama_index/embeddings/__init__.py
 llama_index/embeddings/base.py
 llama_index/embeddings/langchain.py
@@ -47,14 +46,15 @@
 llama_index/indices/common/struct_store/base.py
 llama_index/indices/common/struct_store/schema.py
 llama_index/indices/common/struct_store/sql.py
 llama_index/indices/common_tree/__init__.py
 llama_index/indices/common_tree/base.py
 llama_index/indices/composability/__init__.py
 llama_index/indices/composability/graph.py
+llama_index/indices/composability/utils.py
 llama_index/indices/empty/__init__.py
 llama_index/indices/empty/base.py
 llama_index/indices/empty/query.py
 llama_index/indices/keyword_table/__init__.py
 llama_index/indices/keyword_table/base.py
 llama_index/indices/keyword_table/query.py
 llama_index/indices/keyword_table/rake_base.py
@@ -96,15 +96,14 @@
 llama_index/indices/tree/inserter.py
 llama_index/indices/tree/leaf_query.py
 llama_index/indices/tree/retrieve_query.py
 llama_index/indices/tree/summarize_query.py
 llama_index/indices/vector_store/__init__.py
 llama_index/indices/vector_store/base.py
 llama_index/indices/vector_store/base_query.py
-llama_index/indices/vector_store/queries.py
 llama_index/indices/vector_store/vector_indices.py
 llama_index/langchain_helpers/__init__.py
 llama_index/langchain_helpers/chain_wrapper.py
 llama_index/langchain_helpers/memory_wrapper.py
 llama_index/langchain_helpers/sql_wrapper.py
 llama_index/langchain_helpers/text_splitter.py
 llama_index/langchain_helpers/agents/__init__.py
@@ -173,15 +172,14 @@
 llama_index/readers/github_readers/__init__.py
 llama_index/readers/github_readers/github_api_client.py
 llama_index/readers/github_readers/github_repository_reader.py
 llama_index/readers/github_readers/utils.py
 llama_index/readers/google_readers/__init__.py
 llama_index/readers/google_readers/gdocs.py
 llama_index/readers/google_readers/gsheets.py
-llama_index/readers/llamahub_modules/__init__.py
 llama_index/readers/make_com/__init__.py
 llama_index/readers/make_com/wrapper.py
 llama_index/readers/schema/__init__.py
 llama_index/readers/schema/base.py
 llama_index/readers/steamship/__init__.py
 llama_index/readers/steamship/file_reader.py
 llama_index/readers/weaviate/__init__.py
@@ -203,10 +201,11 @@
 llama_index/vector_stores/__init__.py
 llama_index/vector_stores/chatgpt_plugin.py
 llama_index/vector_stores/chroma.py
 llama_index/vector_stores/faiss.py
 llama_index/vector_stores/opensearch.py
 llama_index/vector_stores/pinecone.py
 llama_index/vector_stores/qdrant.py
+llama_index/vector_stores/registry.py
 llama_index/vector_stores/simple.py
 llama_index/vector_stores/types.py
 llama_index/vector_stores/weaviate.py
```

### Comparing `llama_index-0.5.8/setup.py` & `llama_index-0.5.9/setup.py`

 * *Files identical despite different names*

