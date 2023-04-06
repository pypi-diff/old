# Comparing `tmp/gpt_index-0.5.8.tar.gz` & `tmp/gpt_index-0.5.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gpt_index-0.5.8.tar", last modified: Wed Apr  5 07:00:36 2023, max compression
+gzip compressed data, was "gpt_index-0.5.9.tar", last modified: Thu Apr  6 17:07:28 2023, max compression
```

## Comparing `gpt_index-0.5.8.tar` & `gpt_index-0.5.9.tar`

### file list

```diff
@@ -1,348 +1,354 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.525562 gpt_index-0.5.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-04-05 07:00:10.000000 gpt_index-0.5.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       68 2023-04-05 07:00:10.000000 gpt_index-0.5.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4444 2023-04-05 07:00:36.525562 gpt_index-0.5.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-04-05 07:00:10.000000 gpt_index-0.5.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.489561 gpt_index-0.5.8/gpt_index/
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/VERSION
--rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/async_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.489561 gpt_index-0.5.8/gpt_index/composability/
--rw-r--r--   0 runner    (1001) docker     (123)      216 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/composability/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      169 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/composability/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/composability/joint_qa_summary.py
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.489561 gpt_index-0.5.8/gpt_index/data_structs/
--rw-r--r--   0 runner    (1001) docker     (123)      367 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12371 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/data_structs.py
--rw-r--r--   0 runner    (1001) docker     (123)    12308 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/data_structs_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)     4746 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/node_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)     2669 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/struct_type.py
--rw-r--r--   0 runner    (1001) docker     (123)      906 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1028 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/data_structs/table_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)     7407 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/docstore.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/embeddings/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/embeddings/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7648 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/embeddings/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/embeddings/langchain.py
--rw-r--r--   0 runner    (1001) docker     (123)    10101 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/embeddings/openai.py
--rw-r--r--   0 runner    (1001) docker     (123)      559 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/embeddings/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/evaluation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4407 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/evaluation/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/img_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/
--rw-r--r--   0 runner    (1001) docker     (123)      532 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14702 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/common/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/common/struct_store/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common/struct_store/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8083 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common/struct_store/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      776 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common/struct_store/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common/struct_store/sql.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/common_tree/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common_tree/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7132 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/common_tree/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/composability/
--rw-r--r--   0 runner    (1001) docker     (123)      178 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/composability/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9096 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/composability/graph.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/empty/
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/empty/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2146 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/empty/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2164 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/empty/query.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.493561 gpt_index-0.5.8/gpt_index/indices/keyword_table/
--rw-r--r--   0 runner    (1001) docker     (123)      637 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/keyword_table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7034 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/keyword_table/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     6255 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/keyword_table/query.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/keyword_table/rake_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      838 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/keyword_table/simple_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2260 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/keyword_table/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/knowledge_graph/
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/knowledge_graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8015 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/knowledge_graph/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     9583 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/knowledge_graph/query.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/list/
--rw-r--r--   0 runner    (1001) docker     (123)      319 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/list/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3593 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/list/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3079 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/list/embedding_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     1529 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/list/query.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/postprocessor/
--rw-r--r--   0 runner    (1001) docker     (123)      453 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/postprocessor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/postprocessor/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    11855 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/postprocessor/node.py
--rw-r--r--   0 runner    (1001) docker     (123)     8452 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/prompt_helper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/query/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14837 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/embedding_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/query/query_combiner/
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_combiner/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8731 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_combiner/base.py
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_combiner/prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)    12964 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_runner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/query/query_transform/
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_transform/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9131 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_transform/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5916 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/query_transform/prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)     4834 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/query/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     4017 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/response/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/response/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15563 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/response/builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     3294 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/service_context.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.497561 gpt_index-0.5.8/gpt_index/indices/struct_store/
--rw-r--r--   0 runner    (1001) docker     (123)      608 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2103 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5751 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/container_builder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2612 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/pandas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4743 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/pandas_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     8037 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/sql.py
--rw-r--r--   0 runner    (1001) docker     (123)     6656 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/struct_store/sql_query.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/indices/tree/
--rw-r--r--   0 runner    (1001) docker     (123)      452 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5151 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5481 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/embedding_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     7020 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/inserter.py
--rw-r--r--   0 runner    (1001) docker     (123)    14238 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/leaf_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/retrieve_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     2215 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/tree/summarize_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     1999 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/indices/vector_store/
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/vector_store/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9988 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/vector_store/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3246 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/vector_store/base_query.py
--rw-r--r--   0 runner    (1001) docker     (123)     9420 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/vector_store/queries.py
--rw-r--r--   0 runner    (1001) docker     (123)    23180 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/indices/vector_store/vector_indices.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/langchain_helpers/
--rw-r--r--   0 runner    (1001) docker     (123)       39 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/langchain_helpers/agents/
--rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/agents/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/agents/agents.py
--rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/agents/toolkits.py
--rw-r--r--   0 runner    (1001) docker     (123)     2997 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/agents/tools.py
--rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/chain_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     7565 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/memory_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     3299 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/sql_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)    17456 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/langchain_helpers/text_splitter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/llm_predictor/
--rw-r--r--   0 runner    (1001) docker     (123)      250 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/llm_predictor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10587 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/llm_predictor/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4269 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/llm_predictor/chatgpt.py
--rw-r--r--   0 runner    (1001) docker     (123)     2270 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/llm_predictor/structured.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/logger/
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/logger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      995 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/logger/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/node_parser/
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/node_parser/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      526 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/node_parser/interface.py
--rw-r--r--   0 runner    (1001) docker     (123)     3596 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/node_parser/node_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1846 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/node_parser/simple.py
--rw-r--r--   0 runner    (1001) docker     (123)     4980 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/old_docstore.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.501561 gpt_index-0.5.8/gpt_index/optimization/
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/optimization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4238 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/optimization/optimizer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.505561 gpt_index-0.5.8/gpt_index/output_parsers/
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/output_parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      611 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/output_parsers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/output_parsers/guardrails.py
--rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/output_parsers/langchain.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.505561 gpt_index-0.5.8/gpt_index/playground/
--rw-r--r--   0 runner    (1001) docker     (123)      200 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/playground/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5627 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/playground/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.505561 gpt_index-0.5.8/gpt_index/prompts/
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6622 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1967 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/chat_prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/default_prompt_selectors.py
--rw-r--r--   0 runner    (1001) docker     (123)    10841 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/default_prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)      992 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/prompt_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     7681 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/prompts/prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.505561 gpt_index-0.5.8/gpt_index/readers/
--rw-r--r--   0 runner    (1001) docker     (123)     2699 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      657 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.505561 gpt_index-0.5.8/gpt_index/readers/chatgpt_plugin/
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/chatgpt_plugin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2107 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/chatgpt_plugin/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3891 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/chroma.py
--rw-r--r--   0 runner    (1001) docker     (123)     3322 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/database.py
--rw-r--r--   0 runner    (1001) docker     (123)     4977 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/discord_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)     7399 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/download.py
--rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/elasticsearch.py
--rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/faiss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.509561 gpt_index-0.5.8/gpt_index/readers/file/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8414 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1342 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/base_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1627 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/docs_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/epub_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/image_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3614 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/markdown_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3160 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/mbox_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3943 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/slides_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     3355 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/tabular_parser.py
--rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/file/video_audio.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.509561 gpt_index-0.5.8/gpt_index/readers/github_readers/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/github_readers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11686 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/github_readers/github_api_client.py
--rw-r--r--   0 runner    (1001) docker     (123)    15914 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/github_readers/github_repository_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)     5471 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/github_readers/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.509561 gpt_index-0.5.8/gpt_index/readers/google_readers/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/google_readers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5655 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/google_readers/gdocs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4985 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/google_readers/gsheets.py
--rw-r--r--   0 runner    (1001) docker     (123)     3704 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/json.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.509561 gpt_index-0.5.8/gpt_index/readers/make_com/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/make_com/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/make_com/wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/mbox.py
--rw-r--r--   0 runner    (1001) docker     (123)     2256 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/mongo.py
--rw-r--r--   0 runner    (1001) docker     (123)     5675 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/notion.py
--rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/obsidian.py
--rw-r--r--   0 runner    (1001) docker     (123)     2762 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/pinecone.py
--rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/qdrant.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.509561 gpt_index-0.5.8/gpt_index/readers/schema/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/schema/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/schema/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7888 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/slack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.509561 gpt_index-0.5.8/gpt_index/readers/steamship/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/steamship/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/steamship/file_reader.py
--rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/string_iterable.py
--rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/twitter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.513562 gpt_index-0.5.8/gpt_index/readers/weaviate/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/weaviate/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9754 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/weaviate/data_structs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3982 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/weaviate/reader.py
--rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/weaviate/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7983 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/web.py
--rw-r--r--   0 runner    (1001) docker     (123)      977 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/wikipedia.py
--rw-r--r--   0 runner    (1001) docker     (123)     1251 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/readers/youtube_transcript.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.513562 gpt_index-0.5.8/gpt_index/response/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/response/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2031 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/response/notebook_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3131 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/response/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/response/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2766 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/schema.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.513562 gpt_index-0.5.8/gpt_index/token_counter/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/token_counter/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/token_counter/mock_chain_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)      720 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/token_counter/mock_embed_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     2872 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/token_counter/token_counter.py
--rw-r--r--   0 runner    (1001) docker     (123)      906 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/token_counter/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.513562 gpt_index-0.5.8/gpt_index/tools/
--rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/tools/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      723 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/tools/file_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    11294 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/tools/migrate_v1_to_v2.py
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     5296 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/gpt_index/vector_stores/
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5447 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/chatgpt_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)     4164 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/chroma.py
--rw-r--r--   0 runner    (1001) docker     (123)     3923 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/faiss.py
--rw-r--r--   0 runner    (1001) docker     (123)     6661 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/opensearch.py
--rw-r--r--   0 runner    (1001) docker     (123)     7372 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/pinecone.py
--rw-r--r--   0 runner    (1001) docker     (123)     6935 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/qdrant.py
--rw-r--r--   0 runner    (1001) docker     (123)     3517 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/simple.py
--rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/types.py
--rw-r--r--   0 runner    (1001) docker     (123)     3766 2023-04-05 07:00:10.000000 gpt_index-0.5.8/gpt_index/vector_stores/weaviate.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.489561 gpt_index-0.5.8/gpt_index.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4444 2023-04-05 07:00:36.000000 gpt_index-0.5.8/gpt_index.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     9816 2023-04-05 07:00:36.000000 gpt_index-0.5.8/gpt_index.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 07:00:36.000000 gpt_index-0.5.8/gpt_index.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       87 2023-04-05 07:00:36.000000 gpt_index-0.5.8/gpt_index.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-05 07:00:36.000000 gpt_index-0.5.8/gpt_index.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-05 07:00:10.000000 gpt_index-0.5.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 07:00:36.525562 gpt_index-0.5.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1031 2023-04-05 07:00:10.000000 gpt_index-0.5.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/embeddings/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/embeddings/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2435 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/embeddings/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/embedding/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/embedding/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5974 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/embedding/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/empty/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/empty/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/empty/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/keyword_table/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/keyword_table/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8042 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/keyword_table/test_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/keyword_table/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/knowledge_graph/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/knowledge_graph/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10707 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/knowledge_graph/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/list/
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/list/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16178 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/list/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/postprocessor/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/postprocessor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3263 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/postprocessor/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.517562 gpt_index-0.5.8/tests/indices/query/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/indices/query/query_transform/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/query_transform/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      265 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/query_transform/mock_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/query_transform/test_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3168 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/test_query_bundle.py
--rw-r--r--   0 runner    (1001) docker     (123)     1591 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/test_query_runner.py
--rw-r--r--   0 runner    (1001) docker     (123)    26263 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/query/test_recursive.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/indices/struct_store/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/struct_store/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14242 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/struct_store/test_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/struct_store/test_pandas.py
--rw-r--r--   0 runner    (1001) docker     (123)     1934 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/test_node_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7175 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/test_prompt_helper.py
--rw-r--r--   0 runner    (1001) docker     (123)     6006 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/test_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     3905 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/test_save_load.py
--rw-r--r--   0 runner    (1001) docker     (123)      461 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/indices/tree/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/tree/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/tree/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/indices/vector_store/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/vector_store/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    24161 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/vector_store/test_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4815 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/indices/vector_store/test_pinecone.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/langchain_helpers/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/langchain_helpers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3424 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/langchain_helpers/test_text_splitter.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/llm_predictor/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/llm_predictor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1542 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/llm_predictor/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/logger/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/logger/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1242 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/logger/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/mock_utils/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/mock_utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1144 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/mock_utils/mock_decorator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/mock_utils/mock_predict.py
--rw-r--r--   0 runner    (1001) docker     (123)     2251 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/mock_utils/mock_prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)      618 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/mock_utils/mock_text_splitter.py
--rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/mock_utils/mock_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.521561 gpt_index-0.5.8/tests/optimization/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/optimization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2460 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/optimization/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.525562 gpt_index-0.5.8/tests/output_parsers/
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/output_parsers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/output_parsers/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.525562 gpt_index-0.5.8/tests/playground/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/playground/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4351 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/playground/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.525562 gpt_index-0.5.8/tests/prompts/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/prompts/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4653 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/prompts/test_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.525562 gpt_index-0.5.8/tests/readers/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/readers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11332 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/readers/test_file.py
--rw-r--r--   0 runner    (1001) docker     (123)     1771 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/readers/test_json.py
--rw-r--r--   0 runner    (1001) docker     (123)      337 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/readers/test_string_iterable.py
--rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/test_docstore.py
--rw-r--r--   0 runner    (1001) docker     (123)     2654 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/test_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 07:00:36.525562 gpt_index-0.5.8/tests/token_predictor/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/token_predictor/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1875 2023-04-05 07:00:10.000000 gpt_index-0.5.8/tests/token_predictor/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-04-06 17:07:13.000000 gpt_index-0.5.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       68 2023-04-06 17:07:13.000000 gpt_index-0.5.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4444 2023-04-06 17:07:28.037129 gpt_index-0.5.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4219 2023-04-06 17:07:13.000000 gpt_index-0.5.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.005128 gpt_index-0.5.9/gpt_index/
+-rw-r--r--   0 runner    (1001) docker     (123)        6 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/VERSION
+-rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/async_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.005128 gpt_index-0.5.9/gpt_index/composability/
+-rw-r--r--   0 runner    (1001) docker     (123)      216 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/composability/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      169 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/composability/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/composability/joint_qa_summary.py
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.009129 gpt_index-0.5.9/gpt_index/data_structs/
+-rw-r--r--   0 runner    (1001) docker     (123)      367 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12371 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/data_structs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12263 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/data_structs_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4746 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/node_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2669 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/struct_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)      906 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1028 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/data_structs/table_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7407 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/docstore.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.009129 gpt_index-0.5.9/gpt_index/embeddings/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/embeddings/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7648 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/embeddings/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      932 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/embeddings/langchain.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10101 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/embeddings/openai.py
+-rw-r--r--   0 runner    (1001) docker     (123)      559 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/embeddings/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.009129 gpt_index-0.5.9/gpt_index/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/evaluation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4407 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/evaluation/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      544 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/img_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.009129 gpt_index-0.5.9/gpt_index/indices/
+-rw-r--r--   0 runner    (1001) docker     (123)      532 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15261 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.009129 gpt_index-0.5.9/gpt_index/indices/common/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.009129 gpt_index-0.5.9/gpt_index/indices/common/struct_store/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common/struct_store/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8083 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common/struct_store/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      776 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common/struct_store/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2619 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common/struct_store/sql.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/common_tree/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common_tree/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7132 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/common_tree/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/composability/
+-rw-r--r--   0 runner    (1001) docker     (123)      178 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/composability/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10557 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/composability/graph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2376 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/composability/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/empty/
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/empty/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2146 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/empty/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2164 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/empty/query.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/keyword_table/
+-rw-r--r--   0 runner    (1001) docker     (123)      637 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/keyword_table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7034 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/keyword_table/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6255 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/keyword_table/query.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/keyword_table/rake_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      838 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/keyword_table/simple_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2260 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/keyword_table/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/knowledge_graph/
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/knowledge_graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8015 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/knowledge_graph/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9583 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/knowledge_graph/query.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/list/
+-rw-r--r--   0 runner    (1001) docker     (123)      319 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/list/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3593 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/list/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3079 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/list/embedding_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1529 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/list/query.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/postprocessor/
+-rw-r--r--   0 runner    (1001) docker     (123)      453 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/postprocessor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/postprocessor/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11855 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/postprocessor/node.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8452 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/prompt_helper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/query/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14837 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2577 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/embedding_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.013129 gpt_index-0.5.9/gpt_index/indices/query/query_combiner/
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_combiner/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8731 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_combiner/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_combiner/prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13237 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_runner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/indices/query/query_transform/
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_transform/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9131 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_transform/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5916 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/query_transform/prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4834 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/query/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4017 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/indices/response/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/response/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15563 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/response/builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3294 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/service_context.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/indices/struct_store/
+-rw-r--r--   0 runner    (1001) docker     (123)      608 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2103 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5751 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/container_builder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2612 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/pandas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4743 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/pandas_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8037 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/sql.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6656 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/struct_store/sql_query.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/indices/tree/
+-rw-r--r--   0 runner    (1001) docker     (123)      452 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5151 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5481 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/embedding_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7020 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/inserter.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14238 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/leaf_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1786 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/retrieve_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2215 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/tree/summarize_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1999 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/indices/vector_store/
+-rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/vector_store/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10324 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/vector_store/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3764 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/vector_store/base_query.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17138 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/indices/vector_store/vector_indices.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/langchain_helpers/
+-rw-r--r--   0 runner    (1001) docker     (123)       39 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/langchain_helpers/agents/
+-rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/agents/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/agents/agents.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1130 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/agents/toolkits.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2997 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/agents/tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)      248 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/chain_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7565 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/memory_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3299 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/sql_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17456 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/langchain_helpers/text_splitter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.017129 gpt_index-0.5.9/gpt_index/llm_predictor/
+-rw-r--r--   0 runner    (1001) docker     (123)      250 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/llm_predictor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10587 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/llm_predictor/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4269 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/llm_predictor/chatgpt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2270 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/llm_predictor/structured.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.021129 gpt_index-0.5.9/gpt_index/logger/
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/logger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      995 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/logger/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.021129 gpt_index-0.5.9/gpt_index/node_parser/
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/node_parser/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      526 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/node_parser/interface.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3596 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/node_parser/node_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1846 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/node_parser/simple.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4980 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/old_docstore.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.021129 gpt_index-0.5.9/gpt_index/optimization/
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/optimization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4238 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/optimization/optimizer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.021129 gpt_index-0.5.9/gpt_index/output_parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/output_parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      611 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/output_parsers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2740 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/output_parsers/guardrails.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1826 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/output_parsers/langchain.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.021129 gpt_index-0.5.9/gpt_index/playground/
+-rw-r--r--   0 runner    (1001) docker     (123)      200 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/playground/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5627 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/playground/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.021129 gpt_index-0.5.9/gpt_index/prompts/
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6622 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1967 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/chat_prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/default_prompt_selectors.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10841 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/default_prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)      992 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/prompt_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7681 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/prompts/prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/
+-rw-r--r--   0 runner    (1001) docker     (123)     2699 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      657 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/chatgpt_plugin/
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/chatgpt_plugin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2107 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/chatgpt_plugin/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3891 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/chroma.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3322 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/database.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4977 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/discord_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7399 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/download.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2388 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/elasticsearch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2474 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/faiss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/file/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8414 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1342 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/base_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1627 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/docs_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1316 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/epub_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4102 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/image_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3614 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/markdown_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3160 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/mbox_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3943 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/slides_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3355 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/tabular_parser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/file/video_audio.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/github_readers/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/github_readers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11686 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/github_readers/github_api_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15914 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/github_readers/github_repository_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5471 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/github_readers/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/google_readers/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/google_readers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5655 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/google_readers/gdocs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4985 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/google_readers/gsheets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3704 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/json.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/make_com/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/make_com/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1688 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/make_com/wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/mbox.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2256 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/mongo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5675 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/notion.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/obsidian.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2762 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/pinecone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3275 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/qdrant.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/schema/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/schema/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/schema/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7888 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/slack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/steamship/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/steamship/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3494 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/steamship/file_reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)      978 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/string_iterable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/twitter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.025128 gpt_index-0.5.9/gpt_index/readers/weaviate/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/weaviate/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9754 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/weaviate/data_structs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3982 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/weaviate/reader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1865 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/weaviate/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7983 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/web.py
+-rw-r--r--   0 runner    (1001) docker     (123)      977 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/wikipedia.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1251 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/readers/youtube_transcript.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/gpt_index/response/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/response/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2031 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/response/notebook_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3131 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/response/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      262 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/response/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2766 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/schema.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/gpt_index/token_counter/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/token_counter/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4652 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/token_counter/mock_chain_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)      720 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/token_counter/mock_embed_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2872 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/token_counter/token_counter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      906 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/token_counter/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/gpt_index/tools/
+-rw-r--r--   0 runner    (1001) docker     (123)       13 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/tools/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      723 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/tools/file_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11294 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/tools/migrate_v1_to_v2.py
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5296 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/gpt_index/vector_stores/
+-rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5678 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/chatgpt_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4402 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/chroma.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4486 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/faiss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6882 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/opensearch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8801 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/pinecone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7158 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/qdrant.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2548 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3645 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/simple.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1645 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4094 2023-04-06 17:07:13.000000 gpt_index-0.5.9/gpt_index/vector_stores/weaviate.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.005128 gpt_index-0.5.9/gpt_index.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4444 2023-04-06 17:07:27.000000 gpt_index-0.5.9/gpt_index.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    10010 2023-04-06 17:07:27.000000 gpt_index-0.5.9/gpt_index.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 17:07:27.000000 gpt_index-0.5.9/gpt_index.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       87 2023-04-06 17:07:27.000000 gpt_index-0.5.9/gpt_index.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 17:07:27.000000 gpt_index-0.5.9/gpt_index.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-04-06 17:07:13.000000 gpt_index-0.5.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 17:07:28.037129 gpt_index-0.5.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1031 2023-04-06 17:07:13.000000 gpt_index-0.5.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/tests/embeddings/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/embeddings/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2435 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/embeddings/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/tests/indices/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/tests/indices/composability/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/composability/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/composability/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.029128 gpt_index-0.5.9/tests/indices/embedding/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/embedding/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5974 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/embedding/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/empty/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/empty/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1164 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/empty/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/keyword_table/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/keyword_table/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8042 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/keyword_table/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/keyword_table/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/knowledge_graph/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/knowledge_graph/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10707 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/knowledge_graph/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/list/
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/list/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16178 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/list/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/postprocessor/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/postprocessor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3263 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/postprocessor/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/query/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/query/query_transform/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/query_transform/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      265 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/query_transform/mock_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1508 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/query_transform/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13778 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/test_compose.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20758 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/test_compose_vector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3168 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/test_query_bundle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1591 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/query/test_query_runner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/struct_store/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/struct_store/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14242 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/struct_store/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/struct_store/test_pandas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1934 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/test_node_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7175 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/test_prompt_helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6006 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/test_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3905 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/test_save_load.py
+-rw-r--r--   0 runner    (1001) docker     (123)      461 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/tree/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/tree/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12182 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/tree/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/indices/vector_store/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/vector_store/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24161 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/vector_store/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3267 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/vector_store/test_pinecone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1690 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/indices/vector_store/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/langchain_helpers/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/langchain_helpers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3424 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/langchain_helpers/test_text_splitter.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/llm_predictor/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/llm_predictor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1542 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/llm_predictor/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.033128 gpt_index-0.5.9/tests/logger/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/logger/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1242 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/logger/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/mock_utils/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/mock_utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1144 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/mock_utils/mock_decorator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4725 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/mock_utils/mock_predict.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2251 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/mock_utils/mock_prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)      618 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/mock_utils/mock_text_splitter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      737 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/mock_utils/mock_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/optimization/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/optimization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2460 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/optimization/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/output_parsers/
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/output_parsers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1505 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/output_parsers/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/playground/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/playground/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4351 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/playground/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/prompts/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/prompts/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4653 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/prompts/test_base.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/readers/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/readers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11332 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/readers/test_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1771 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/readers/test_json.py
+-rw-r--r--   0 runner    (1001) docker     (123)      337 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/readers/test_string_iterable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1403 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/test_docstore.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2654 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/test_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 17:07:28.037129 gpt_index-0.5.9/tests/token_predictor/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/token_predictor/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1875 2023-04-06 17:07:13.000000 gpt_index-0.5.9/tests/token_predictor/test_base.py
```

### Comparing `gpt_index-0.5.8/LICENSE` & `gpt_index-0.5.9/LICENSE`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/PKG-INFO` & `gpt_index-0.5.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt_index
-Version: 0.5.8
+Version: 0.5.9
 Summary: Interface between LLMs and your data
 Home-page: https://github.com/jerryjliu/gpt_index
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # 🗂️ LlamaIndex 🦙 (GPT Index)
```

### Comparing `gpt_index-0.5.8/README.md` & `gpt_index-0.5.9/README.md`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/__init__.py` & `gpt_index-0.5.9/gpt_index/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/composability/joint_qa_summary.py` & `gpt_index-0.5.9/gpt_index/composability/joint_qa_summary.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/data_structs/data_structs.py` & `gpt_index-0.5.9/gpt_index/data_structs/data_structs.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/data_structs/data_structs_v2.py` & `gpt_index-0.5.9/gpt_index/data_structs/data_structs_v2.py`

 * *Files 1% similar despite different names*

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

### Comparing `gpt_index-0.5.8/gpt_index/data_structs/node_v2.py` & `gpt_index-0.5.9/gpt_index/data_structs/node_v2.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/data_structs/struct_type.py` & `gpt_index-0.5.9/gpt_index/data_structs/struct_type.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/data_structs/table.py` & `gpt_index-0.5.9/gpt_index/data_structs/table.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/data_structs/table_v2.py` & `gpt_index-0.5.9/gpt_index/data_structs/table_v2.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/docstore.py` & `gpt_index-0.5.9/gpt_index/docstore.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/embeddings/base.py` & `gpt_index-0.5.9/gpt_index/embeddings/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/embeddings/langchain.py` & `gpt_index-0.5.9/gpt_index/embeddings/langchain.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/embeddings/openai.py` & `gpt_index-0.5.9/gpt_index/embeddings/openai.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/embeddings/utils.py` & `gpt_index-0.5.9/gpt_index/embeddings/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/evaluation/base.py` & `gpt_index-0.5.9/gpt_index/evaluation/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/img_utils.py` & `gpt_index-0.5.9/gpt_index/img_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/__init__.py` & `gpt_index-0.5.9/gpt_index/indices/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/base.py` & `gpt_index-0.5.9/gpt_index/indices/base.py`

 * *Files 6% similar despite different names*

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

### Comparing `gpt_index-0.5.8/gpt_index/indices/common/struct_store/base.py` & `gpt_index-0.5.9/gpt_index/indices/common/struct_store/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/common/struct_store/schema.py` & `gpt_index-0.5.9/gpt_index/indices/common/struct_store/schema.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/common/struct_store/sql.py` & `gpt_index-0.5.9/gpt_index/indices/common/struct_store/sql.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/common_tree/base.py` & `gpt_index-0.5.9/gpt_index/indices/common_tree/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/composability/graph.py` & `gpt_index-0.5.9/gpt_index/indices/composability/graph.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,19 +1,27 @@
 """Composability graphs."""
 
 import json
 from typing import Any, Dict, List, Optional, Sequence, Type, Union, cast
 
-from gpt_index.constants import DOCSTORE_KEY, INDEX_STRUCT_KEY
+from gpt_index.constants import (
+    ADDITIONAL_QUERY_CONTEXT_KEY,
+    DOCSTORE_KEY,
+    INDEX_STRUCT_KEY,
+)
 from gpt_index.data_structs.data_structs_v2 import CompositeIndex
 from gpt_index.data_structs.data_structs_v2 import V2IndexStruct
 from gpt_index.data_structs.data_structs_v2 import V2IndexStruct as IndexStruct
 from gpt_index.data_structs.node_v2 import IndexNode, DocumentRelationship
 from gpt_index.docstore import DocumentStore
 from gpt_index.indices.base import BaseGPTIndex
+from gpt_index.indices.composability.utils import (
+    load_query_context_from_dict,
+    save_query_context_to_dict,
+)
 from gpt_index.indices.query.query_runner import QueryRunner
 from gpt_index.indices.query.query_transform.base import BaseQueryTransform
 from gpt_index.indices.query.schema import QueryBundle, QueryConfig
 from gpt_index.indices.service_context import ServiceContext
 from gpt_index.response.schema import RESPONSE_TYPE
 
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
         from gpt_index.indices.registry import load_index_struct_from_dict
 
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

### Comparing `gpt_index-0.5.8/gpt_index/indices/empty/base.py` & `gpt_index-0.5.9/gpt_index/indices/empty/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/empty/query.py` & `gpt_index-0.5.9/gpt_index/indices/empty/query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/keyword_table/__init__.py` & `gpt_index-0.5.9/gpt_index/indices/keyword_table/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/keyword_table/base.py` & `gpt_index-0.5.9/gpt_index/indices/keyword_table/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/keyword_table/query.py` & `gpt_index-0.5.9/gpt_index/indices/keyword_table/query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/keyword_table/rake_base.py` & `gpt_index-0.5.9/gpt_index/indices/keyword_table/rake_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/keyword_table/simple_base.py` & `gpt_index-0.5.9/gpt_index/indices/keyword_table/simple_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/keyword_table/utils.py` & `gpt_index-0.5.9/gpt_index/indices/keyword_table/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/knowledge_graph/base.py` & `gpt_index-0.5.9/gpt_index/indices/knowledge_graph/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/knowledge_graph/query.py` & `gpt_index-0.5.9/gpt_index/indices/knowledge_graph/query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/list/base.py` & `gpt_index-0.5.9/gpt_index/indices/list/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/list/embedding_query.py` & `gpt_index-0.5.9/gpt_index/indices/list/embedding_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/list/query.py` & `gpt_index-0.5.9/gpt_index/indices/list/query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/postprocessor/node.py` & `gpt_index-0.5.9/gpt_index/indices/postprocessor/node.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/prompt_helper.py` & `gpt_index-0.5.9/gpt_index/indices/prompt_helper.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/base.py` & `gpt_index-0.5.9/gpt_index/indices/query/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/embedding_utils.py` & `gpt_index-0.5.9/gpt_index/indices/query/embedding_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/query_combiner/base.py` & `gpt_index-0.5.9/gpt_index/indices/query/query_combiner/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/query_runner.py` & `gpt_index-0.5.9/gpt_index/indices/query/query_runner.py`

 * *Files 4% similar despite different names*

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
 
         from gpt_index.indices.registry import INDEX_STRUT_TYPE_TO_QUERY_MAP
 
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

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/query_transform/base.py` & `gpt_index-0.5.9/gpt_index/indices/query/query_transform/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/query_transform/prompts.py` & `gpt_index-0.5.9/gpt_index/indices/query/query_transform/prompts.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/query/schema.py` & `gpt_index-0.5.9/gpt_index/indices/query/schema.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/registry.py` & `gpt_index-0.5.9/gpt_index/indices/registry.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/response/builder.py` & `gpt_index-0.5.9/gpt_index/indices/response/builder.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/service_context.py` & `gpt_index-0.5.9/gpt_index/indices/service_context.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/__init__.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/base.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/container_builder.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/container_builder.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/pandas.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/pandas.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/pandas_query.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/pandas_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/sql.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/sql.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/struct_store/sql_query.py` & `gpt_index-0.5.9/gpt_index/indices/struct_store/sql_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/tree/base.py` & `gpt_index-0.5.9/gpt_index/indices/tree/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/tree/embedding_query.py` & `gpt_index-0.5.9/gpt_index/indices/tree/embedding_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/tree/inserter.py` & `gpt_index-0.5.9/gpt_index/indices/tree/inserter.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/tree/leaf_query.py` & `gpt_index-0.5.9/gpt_index/indices/tree/leaf_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/tree/retrieve_query.py` & `gpt_index-0.5.9/gpt_index/indices/tree/retrieve_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/tree/summarize_query.py` & `gpt_index-0.5.9/gpt_index/indices/tree/summarize_query.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/utils.py` & `gpt_index-0.5.9/gpt_index/indices/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/vector_store/__init__.py` & `gpt_index-0.5.9/gpt_index/indices/vector_store/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/indices/vector_store/base.py` & `gpt_index-0.5.9/gpt_index/indices/vector_store/base.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,22 +3,26 @@
 An index that that is built on top of an existing vector store.
 
 """
 
 from typing import Any, Dict, List, Optional, Sequence, Set, Tuple
 
 from gpt_index.async_utils import run_async_tasks
-from gpt_index.constants import VECTOR_STORE_CONFIG_DICT_KEY
+from gpt_index.constants import VECTOR_STORE_KEY
 from gpt_index.data_structs.data_structs_v2 import IndexDict
-from gpt_index.data_structs.node_v2 import Node
+from gpt_index.data_structs.node_v2 import ImageNode, IndexNode, Node
 from gpt_index.indices.base import BaseGPTIndex, QueryMap
 from gpt_index.indices.query.schema import QueryMode
 from gpt_index.indices.service_context import ServiceContext
 from gpt_index.indices.vector_store.base_query import GPTVectorStoreIndexQuery
 from gpt_index.token_counter.token_counter import llm_token_counter
+from gpt_index.vector_stores.registry import (
+    load_vector_store_from_dict,
+    save_vector_store_to_dict,
+)
 from gpt_index.vector_stores.simple import SimpleVectorStore
 from gpt_index.vector_stores.types import NodeEmbeddingResult, VectorStore
 
 
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

### Comparing `gpt_index-0.5.8/gpt_index/indices/vector_store/base_query.py` & `gpt_index-0.5.9/gpt_index/indices/vector_store/base_query.py`

 * *Files 14% similar despite different names*

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

### Comparing `gpt_index-0.5.8/gpt_index/indices/vector_store/vector_indices.py` & `gpt_index-0.5.9/gpt_index/indices/vector_store/vector_indices.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 """Deprecated vector store indices."""
 
-from typing import Any, Dict, Optional, Sequence, Type, cast
+from typing import Any, Dict, Optional, Sequence, Type
 
 from requests.adapters import Retry
 
 from gpt_index.data_structs.data_structs_v2 import (
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
 from gpt_index.data_structs.node_v2 import Node
-from gpt_index.indices.base import BaseGPTIndex, QueryMap
-from gpt_index.indices.query.schema import QueryMode
-from gpt_index.indices.vector_store.queries import (
-    ChatGPTRetrievalPluginQuery,
-    GPTChromaIndexQuery,
-    GPTFaissIndexQuery,
-    GPTOpensearchIndexQuery,
-    GPTPineconeIndexQuery,
-    GPTQdrantIndexQuery,
-    GPTSimpleVectorIndexQuery,
-    GPTWeaviateIndexQuery,
-)
+from gpt_index.indices.base import BaseGPTIndex
 from gpt_index.indices.service_context import ServiceContext
 from gpt_index.indices.vector_store.base import GPTVectorStoreIndex
 from gpt_index.vector_stores import (
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

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/agents/__init__.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/agents/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/agents/agents.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/agents/agents.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/agents/toolkits.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/agents/toolkits.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/agents/tools.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/agents/tools.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/memory_wrapper.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/memory_wrapper.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/sql_wrapper.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/sql_wrapper.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/langchain_helpers/text_splitter.py` & `gpt_index-0.5.9/gpt_index/langchain_helpers/text_splitter.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/llm_predictor/base.py` & `gpt_index-0.5.9/gpt_index/llm_predictor/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/llm_predictor/chatgpt.py` & `gpt_index-0.5.9/gpt_index/llm_predictor/chatgpt.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/llm_predictor/structured.py` & `gpt_index-0.5.9/gpt_index/llm_predictor/structured.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/logger/base.py` & `gpt_index-0.5.9/gpt_index/logger/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/node_parser/interface.py` & `gpt_index-0.5.9/gpt_index/node_parser/interface.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/node_parser/node_utils.py` & `gpt_index-0.5.9/gpt_index/node_parser/node_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/node_parser/simple.py` & `gpt_index-0.5.9/gpt_index/node_parser/simple.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/old_docstore.py` & `gpt_index-0.5.9/gpt_index/old_docstore.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/optimization/optimizer.py` & `gpt_index-0.5.9/gpt_index/optimization/optimizer.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/output_parsers/base.py` & `gpt_index-0.5.9/gpt_index/output_parsers/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/output_parsers/guardrails.py` & `gpt_index-0.5.9/gpt_index/output_parsers/guardrails.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/output_parsers/langchain.py` & `gpt_index-0.5.9/gpt_index/output_parsers/langchain.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/playground/base.py` & `gpt_index-0.5.9/gpt_index/playground/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/prompts/base.py` & `gpt_index-0.5.9/gpt_index/prompts/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/prompts/chat_prompts.py` & `gpt_index-0.5.9/gpt_index/prompts/chat_prompts.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/prompts/default_prompt_selectors.py` & `gpt_index-0.5.9/gpt_index/prompts/default_prompt_selectors.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/prompts/default_prompts.py` & `gpt_index-0.5.9/gpt_index/prompts/default_prompts.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/prompts/prompt_type.py` & `gpt_index-0.5.9/gpt_index/prompts/prompt_type.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/prompts/prompts.py` & `gpt_index-0.5.9/gpt_index/prompts/prompts.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/__init__.py` & `gpt_index-0.5.9/gpt_index/readers/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/base.py` & `gpt_index-0.5.9/gpt_index/readers/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/chatgpt_plugin/base.py` & `gpt_index-0.5.9/gpt_index/readers/chatgpt_plugin/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/chroma.py` & `gpt_index-0.5.9/gpt_index/readers/chroma.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/database.py` & `gpt_index-0.5.9/gpt_index/readers/database.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/discord_reader.py` & `gpt_index-0.5.9/gpt_index/readers/discord_reader.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/download.py` & `gpt_index-0.5.9/gpt_index/readers/download.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/elasticsearch.py` & `gpt_index-0.5.9/gpt_index/readers/elasticsearch.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/faiss.py` & `gpt_index-0.5.9/gpt_index/readers/faiss.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/base.py` & `gpt_index-0.5.9/gpt_index/readers/file/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/base_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/base_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/docs_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/docs_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/epub_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/epub_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/image_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/image_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/markdown_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/markdown_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/mbox_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/mbox_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/slides_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/slides_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/tabular_parser.py` & `gpt_index-0.5.9/gpt_index/readers/file/tabular_parser.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/file/video_audio.py` & `gpt_index-0.5.9/gpt_index/readers/file/video_audio.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/github_readers/github_api_client.py` & `gpt_index-0.5.9/gpt_index/readers/github_readers/github_api_client.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/github_readers/github_repository_reader.py` & `gpt_index-0.5.9/gpt_index/readers/github_readers/github_repository_reader.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/github_readers/utils.py` & `gpt_index-0.5.9/gpt_index/readers/github_readers/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/google_readers/gdocs.py` & `gpt_index-0.5.9/gpt_index/readers/google_readers/gdocs.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/google_readers/gsheets.py` & `gpt_index-0.5.9/gpt_index/readers/google_readers/gsheets.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/json.py` & `gpt_index-0.5.9/gpt_index/readers/json.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/make_com/wrapper.py` & `gpt_index-0.5.9/gpt_index/readers/make_com/wrapper.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/mbox.py` & `gpt_index-0.5.9/gpt_index/readers/mbox.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/mongo.py` & `gpt_index-0.5.9/gpt_index/readers/mongo.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/notion.py` & `gpt_index-0.5.9/gpt_index/readers/notion.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/obsidian.py` & `gpt_index-0.5.9/gpt_index/readers/obsidian.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/pinecone.py` & `gpt_index-0.5.9/gpt_index/readers/pinecone.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/qdrant.py` & `gpt_index-0.5.9/gpt_index/readers/qdrant.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/schema/base.py` & `gpt_index-0.5.9/gpt_index/readers/schema/base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/slack.py` & `gpt_index-0.5.9/gpt_index/readers/slack.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/steamship/file_reader.py` & `gpt_index-0.5.9/gpt_index/readers/steamship/file_reader.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/string_iterable.py` & `gpt_index-0.5.9/gpt_index/readers/string_iterable.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/twitter.py` & `gpt_index-0.5.9/gpt_index/readers/twitter.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/weaviate/data_structs.py` & `gpt_index-0.5.9/gpt_index/readers/weaviate/data_structs.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/weaviate/reader.py` & `gpt_index-0.5.9/gpt_index/readers/weaviate/reader.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/weaviate/utils.py` & `gpt_index-0.5.9/gpt_index/readers/weaviate/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/web.py` & `gpt_index-0.5.9/gpt_index/readers/web.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/wikipedia.py` & `gpt_index-0.5.9/gpt_index/readers/wikipedia.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/readers/youtube_transcript.py` & `gpt_index-0.5.9/gpt_index/readers/youtube_transcript.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/response/notebook_utils.py` & `gpt_index-0.5.9/gpt_index/response/notebook_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/response/schema.py` & `gpt_index-0.5.9/gpt_index/response/schema.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/schema.py` & `gpt_index-0.5.9/gpt_index/schema.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/token_counter/mock_chain_wrapper.py` & `gpt_index-0.5.9/gpt_index/token_counter/mock_chain_wrapper.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/token_counter/mock_embed_model.py` & `gpt_index-0.5.9/gpt_index/token_counter/mock_embed_model.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/token_counter/token_counter.py` & `gpt_index-0.5.9/gpt_index/token_counter/token_counter.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/token_counter/utils.py` & `gpt_index-0.5.9/gpt_index/token_counter/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/tools/file_utils.py` & `gpt_index-0.5.9/gpt_index/tools/file_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/tools/migrate_v1_to_v2.py` & `gpt_index-0.5.9/gpt_index/tools/migrate_v1_to_v2.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/utils.py` & `gpt_index-0.5.9/gpt_index/utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/__init__.py` & `gpt_index-0.5.9/gpt_index/vector_stores/__init__.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/chatgpt_plugin.py` & `gpt_index-0.5.9/gpt_index/vector_stores/chatgpt_plugin.py`

 * *Files 6% similar despite different names*

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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/chroma.py` & `gpt_index-0.5.9/gpt_index/vector_stores/chroma.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 """Chroma vector store."""
 import logging
 import math
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 from gpt_index.data_structs.node_v2 import DocumentRelationship, Node
 from gpt_index.utils import truncate_text
 from gpt_index.vector_stores.types import (
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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/faiss.py` & `gpt_index-0.5.9/gpt_index/vector_stores/faiss.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """Faiss Vector store index.
 
 An index that that is built on top of an existing vector store.
 
 """
 
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 import numpy as np
 
 from gpt_index.vector_stores.types import (
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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/opensearch.py` & `gpt_index-0.5.9/gpt_index/vector_stores/opensearch.py`

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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/qdrant.py` & `gpt_index-0.5.9/gpt_index/vector_stores/qdrant.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """Qdrant vector store index.
 
 An index that is built on top of an existing Qdrant collection.
 
 """
 import logging
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 from gpt_index.data_structs.node_v2 import DocumentRelationship, Node
 from gpt_index.utils import get_new_id
 from gpt_index.vector_stores.types import (
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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/simple.py` & `gpt_index-0.5.9/gpt_index/vector_stores/simple.py`

 * *Files 4% similar despite different names*

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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/types.py` & `gpt_index-0.5.9/gpt_index/vector_stores/types.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """Vector store index types."""
 
 
 from dataclasses import dataclass
-from typing import Any, List, Optional, Protocol
+from typing import Any, Dict, List, Optional, Protocol, runtime_checkable
 
 from gpt_index.data_structs.node_v2 import Node
 
 
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

### Comparing `gpt_index-0.5.8/gpt_index/vector_stores/weaviate.py` & `gpt_index-0.5.9/gpt_index/vector_stores/weaviate.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 """Weaviate Vector store index.
 
 An index that that is built on top of an existing vector store.
 
 """
 
-from typing import Any, List, Optional, cast
+from typing import Any, Dict, List, Optional, cast
 
 from gpt_index.readers.weaviate.data_structs import WeaviateNode
 from gpt_index.readers.weaviate.utils import get_default_class_prefix
 from gpt_index.vector_stores.types import (
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

### Comparing `gpt_index-0.5.8/gpt_index.egg-info/PKG-INFO` & `gpt_index-0.5.9/gpt_index.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gpt-index
-Version: 0.5.8
+Version: 0.5.9
 Summary: Interface between LLMs and your data
 Home-page: https://github.com/jerryjliu/gpt_index
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # 🗂️ LlamaIndex 🦙 (GPT Index)
```

### Comparing `gpt_index-0.5.8/gpt_index.egg-info/SOURCES.txt` & `gpt_index-0.5.9/gpt_index.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -47,14 +47,15 @@
 gpt_index/indices/common/struct_store/base.py
 gpt_index/indices/common/struct_store/schema.py
 gpt_index/indices/common/struct_store/sql.py
 gpt_index/indices/common_tree/__init__.py
 gpt_index/indices/common_tree/base.py
 gpt_index/indices/composability/__init__.py
 gpt_index/indices/composability/graph.py
+gpt_index/indices/composability/utils.py
 gpt_index/indices/empty/__init__.py
 gpt_index/indices/empty/base.py
 gpt_index/indices/empty/query.py
 gpt_index/indices/keyword_table/__init__.py
 gpt_index/indices/keyword_table/base.py
 gpt_index/indices/keyword_table/query.py
 gpt_index/indices/keyword_table/rake_base.py
@@ -96,15 +97,14 @@
 gpt_index/indices/tree/inserter.py
 gpt_index/indices/tree/leaf_query.py
 gpt_index/indices/tree/retrieve_query.py
 gpt_index/indices/tree/summarize_query.py
 gpt_index/indices/vector_store/__init__.py
 gpt_index/indices/vector_store/base.py
 gpt_index/indices/vector_store/base_query.py
-gpt_index/indices/vector_store/queries.py
 gpt_index/indices/vector_store/vector_indices.py
 gpt_index/langchain_helpers/__init__.py
 gpt_index/langchain_helpers/chain_wrapper.py
 gpt_index/langchain_helpers/memory_wrapper.py
 gpt_index/langchain_helpers/sql_wrapper.py
 gpt_index/langchain_helpers/text_splitter.py
 gpt_index/langchain_helpers/agents/__init__.py
@@ -202,56 +202,61 @@
 gpt_index/vector_stores/__init__.py
 gpt_index/vector_stores/chatgpt_plugin.py
 gpt_index/vector_stores/chroma.py
 gpt_index/vector_stores/faiss.py
 gpt_index/vector_stores/opensearch.py
 gpt_index/vector_stores/pinecone.py
 gpt_index/vector_stores/qdrant.py
+gpt_index/vector_stores/registry.py
 gpt_index/vector_stores/simple.py
 gpt_index/vector_stores/types.py
 gpt_index/vector_stores/weaviate.py
 tests/__init__.py
 tests/test_docstore.py
 tests/test_utils.py
 tests/embeddings/__init__.py
 tests/embeddings/test_base.py
 tests/indices/__init__.py
 tests/indices/test_node_utils.py
 tests/indices/test_prompt_helper.py
 tests/indices/test_response.py
 tests/indices/test_save_load.py
 tests/indices/test_utils.py
+tests/indices/composability/__init__.py
+tests/indices/composability/test_utils.py
 tests/indices/embedding/__init__.py
 tests/indices/embedding/test_base.py
 tests/indices/empty/__init__.py
 tests/indices/empty/test_base.py
 tests/indices/keyword_table/__init__.py
 tests/indices/keyword_table/test_base.py
 tests/indices/keyword_table/test_utils.py
 tests/indices/knowledge_graph/__init__.py
 tests/indices/knowledge_graph/test_base.py
 tests/indices/list/__init__.py
 tests/indices/list/test_base.py
 tests/indices/postprocessor/__init__.py
 tests/indices/postprocessor/test_base.py
 tests/indices/query/__init__.py
+tests/indices/query/test_compose.py
+tests/indices/query/test_compose_vector.py
 tests/indices/query/test_query_bundle.py
 tests/indices/query/test_query_runner.py
-tests/indices/query/test_recursive.py
 tests/indices/query/query_transform/__init__.py
 tests/indices/query/query_transform/mock_utils.py
 tests/indices/query/query_transform/test_base.py
 tests/indices/struct_store/__init__.py
 tests/indices/struct_store/test_base.py
 tests/indices/struct_store/test_pandas.py
 tests/indices/tree/__init__.py
 tests/indices/tree/test_base.py
 tests/indices/vector_store/__init__.py
 tests/indices/vector_store/test_base.py
 tests/indices/vector_store/test_pinecone.py
+tests/indices/vector_store/utils.py
 tests/langchain_helpers/__init__.py
 tests/langchain_helpers/test_text_splitter.py
 tests/llm_predictor/__init__.py
 tests/llm_predictor/test_base.py
 tests/logger/__init__.py
 tests/logger/test_base.py
 tests/mock_utils/__init__.py
```

### Comparing `gpt_index-0.5.8/setup.py` & `gpt_index-0.5.9/setup.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/embeddings/test_base.py` & `gpt_index-0.5.9/tests/embeddings/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/embedding/test_base.py` & `gpt_index-0.5.9/tests/indices/embedding/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/empty/test_base.py` & `gpt_index-0.5.9/tests/indices/empty/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/keyword_table/test_base.py` & `gpt_index-0.5.9/tests/indices/keyword_table/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/keyword_table/test_utils.py` & `gpt_index-0.5.9/tests/indices/keyword_table/test_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/knowledge_graph/test_base.py` & `gpt_index-0.5.9/tests/indices/knowledge_graph/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/list/test_base.py` & `gpt_index-0.5.9/tests/indices/list/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/postprocessor/test_base.py` & `gpt_index-0.5.9/tests/indices/postprocessor/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/query/query_transform/test_base.py` & `gpt_index-0.5.9/tests/indices/query/query_transform/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/query/test_query_bundle.py` & `gpt_index-0.5.9/tests/indices/query/test_query_bundle.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/query/test_query_runner.py` & `gpt_index-0.5.9/tests/indices/query/test_query_runner.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/query/test_recursive.py` & `gpt_index-0.5.9/tests/indices/query/test_compose_vector.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,35 +1,34 @@
 """Test recursive queries."""
 
+import pytest
 import asyncio
 from pathlib import Path
+import sys
 from tempfile import TemporaryDirectory
 from typing import Any, Dict, List, Tuple, cast
-from unittest.mock import patch
-
-import pytest
+from unittest.mock import MagicMock, patch
 
 from gpt_index.data_structs.data_structs_v2 import V2IndexStruct
 from gpt_index.data_structs.struct_type import IndexStructType
 from gpt_index.embeddings.openai import OpenAIEmbedding
 from gpt_index.indices.composability.graph import ComposableGraph
 from gpt_index.indices.keyword_table.simple_base import GPTSimpleKeywordTableIndex
-from gpt_index.indices.list.base import GPTListIndex
 from gpt_index.indices.query.schema import QueryConfig, QueryMode
-from gpt_index.indices.tree.base import GPTTreeIndex
-from gpt_index.indices.vector_store.vector_indices import GPTSimpleVectorIndex
+from gpt_index.indices.vector_store.vector_indices import (
+    GPTPineconeIndex,
+    GPTSimpleVectorIndex,
+)
 from gpt_index.langchain_helpers.chain_wrapper import (
-    LLMChain,
-    LLMMetadata,
     LLMPredictor,
 )
 from gpt_index.langchain_helpers.text_splitter import TokenTextSplitter
 from gpt_index.readers.schema.base import Document
+from tests.indices.vector_store.utils import MockPineconeIndex
 from tests.mock_utils.mock_predict import (
-    mock_llmchain_predict,
     mock_llmpredictor_predict,
 )
 from tests.mock_utils.mock_prompts import (
     MOCK_INSERT_PROMPT,
     MOCK_KEYWORD_EXTRACT_PROMPT,
     MOCK_QUERY_KEYWORD_EXTRACT_PROMPT,
     MOCK_QUERY_PROMPT,
@@ -52,14 +51,15 @@
         "list": {
             "text_qa_template": MOCK_TEXT_QA_PROMPT,
         },
         "table": {
             "keyword_extract_template": MOCK_KEYWORD_EXTRACT_PROMPT,
         },
         "vector": {},
+        "pinecone": {},
     }
     query_configs = [
         QueryConfig(
             index_struct_type=IndexStructType.TREE,
             query_mode=QueryMode.DEFAULT,
             query_kwargs={
                 "query_template": MOCK_QUERY_PROMPT,
@@ -89,14 +89,23 @@
             query_mode=QueryMode.DEFAULT,
             query_kwargs={
                 "text_qa_template": MOCK_TEXT_QA_PROMPT,
                 "refine_template": MOCK_REFINE_PROMPT,
                 "similarity_top_k": 1,
             },
         ),
+        QueryConfig(
+            index_struct_type=IndexStructType.PINECONE,
+            query_mode=QueryMode.DEFAULT,
+            query_kwargs={
+                "text_qa_template": MOCK_TEXT_QA_PROMPT,
+                "refine_template": MOCK_REFINE_PROMPT,
+                "similarity_top_k": 1,
+            },
+        ),
     ]
     return index_kwargs, query_configs
 
 
 @pytest.fixture
 def documents() -> List[Document]:
     """Get documents."""
@@ -109,263 +118,14 @@
         Document("This is a test."),
         Document("This is another test."),
         Document("This is a test v2."),
     ]
     return docs
 
 
-@patch.object(TokenTextSplitter, "split_text", side_effect=mock_token_splitter_newline)
-@patch.object(LLMPredictor, "predict", side_effect=mock_llmpredictor_predict)
-@patch.object(LLMPredictor, "total_tokens_used", return_value=0)
-@patch.object(LLMPredictor, "__init__", return_value=None)
-def test_recursive_query_list_tree(
-    _mock_init: Any,
-    _mock_total_tokens_used: Any,
-    _mock_predict: Any,
-    _mock_split_text: Any,
-    documents: List[Document],
-    struct_kwargs: Dict,
-) -> None:
-    """Test query."""
-    index_kwargs, query_configs = struct_kwargs
-    list_kwargs = index_kwargs["list"]
-    tree_kwargs = index_kwargs["tree"]
-    # try building a list for every two, then a tree
-    list1 = GPTListIndex.from_documents(documents[0:2], **list_kwargs)
-    list2 = GPTListIndex.from_documents(documents[2:4], **list_kwargs)
-    list3 = GPTListIndex.from_documents(documents[4:6], **list_kwargs)
-    list4 = GPTListIndex.from_documents(documents[6:8], **list_kwargs)
-
-    summary1 = "summary1"
-    summary2 = "summary2"
-    summary3 = "summary3"
-    summary4 = "summary4"
-    summaries = [summary1, summary2, summary3, summary4]
-
-    # there are two root nodes in this tree: one containing [list1, list2]
-    # and the other containing [list3, list4]
-    graph = ComposableGraph.from_indices(
-        GPTTreeIndex,
-        [
-            list1,
-            list2,
-            list3,
-            list4,
-        ],
-        index_summaries=summaries,
-        **tree_kwargs
-    )
-    assert isinstance(graph, ComposableGraph)
-    query_str = "What is?"
-    # query should first pick the left root node, then pick list1
-    # within list1, it should go through the first document and second document
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == (
-        "What is?:What is?:This is a test v2.:This is another test."
-    )
-
-
-@patch.object(TokenTextSplitter, "split_text", side_effect=mock_token_splitter_newline)
-@patch.object(LLMPredictor, "predict", side_effect=mock_llmpredictor_predict)
-@patch.object(LLMPredictor, "total_tokens_used", return_value=0)
-@patch.object(LLMPredictor, "__init__", return_value=None)
-def test_recursive_query_tree_list(
-    _mock_init: Any,
-    _mock_total_tokens_used: Any,
-    _mock_predict: Any,
-    _mock_split_text: Any,
-    documents: List[Document],
-    struct_kwargs: Dict,
-) -> None:
-    """Test query."""
-    index_kwargs, query_configs = struct_kwargs
-    list_kwargs = index_kwargs["list"]
-    tree_kwargs = index_kwargs["tree"]
-    # try building a tree for a group of 4, then a list
-    # use a diff set of documents
-    tree1 = GPTTreeIndex.from_documents(documents[2:6], **tree_kwargs)
-    tree2 = GPTTreeIndex.from_documents(documents[:2] + documents[6:], **tree_kwargs)
-    summaries = [
-        "tree_summary1",
-        "tree_summary2",
-    ]
-
-    # there are two root nodes in this tree: one containing [list1, list2]
-    # and the other containing [list3, list4]
-    graph = ComposableGraph.from_indices(
-        GPTListIndex, [tree1, tree2], index_summaries=summaries, **list_kwargs
-    )
-    assert isinstance(graph, ComposableGraph)
-    query_str = "What is?"
-    # query should first pick the left root node, then pick list1
-    # within list1, it should go through the first document and second document
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == (
-        "What is?:What is?:This is a test.:What is?:This is a test v2."
-    )
-
-
-@patch.object(TokenTextSplitter, "split_text", side_effect=mock_token_splitter_newline)
-@patch.object(LLMPredictor, "predict", side_effect=mock_llmpredictor_predict)
-@patch.object(LLMPredictor, "total_tokens_used", return_value=0)
-@patch.object(LLMPredictor, "__init__", return_value=None)
-def test_recursive_query_table_list(
-    _mock_init: Any,
-    _mock_total_tokens_used: Any,
-    _mock_predict: Any,
-    _mock_split_text: Any,
-    documents: List[Document],
-    struct_kwargs: Dict,
-) -> None:
-    """Test query."""
-    index_kwargs, query_configs = struct_kwargs
-    list_kwargs = index_kwargs["list"]
-    table_kwargs = index_kwargs["table"]
-    # try building a tree for a group of 4, then a list
-    # use a diff set of documents
-    table1 = GPTSimpleKeywordTableIndex.from_documents(documents[4:6], **table_kwargs)
-    table2 = GPTSimpleKeywordTableIndex.from_documents(documents[2:3], **table_kwargs)
-    summaries = [
-        "table_summary1",
-        "table_summary2",
-    ]
-
-    graph = ComposableGraph.from_indices(
-        GPTListIndex, [table1, table2], index_summaries=summaries, **list_kwargs
-    )
-    assert isinstance(graph, ComposableGraph)
-    query_str = "World?"
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == ("World?:World?:Hello world.:None")
-
-    query_str = "Test?"
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == ("Test?:Test?:This is a test.:Test?:This is a test.")
-
-    # test serialize and then back
-    with TemporaryDirectory() as tmpdir:
-        graph.save_to_disk(str(Path(tmpdir) / "tmp.json"))
-        graph = ComposableGraph.load_from_disk(str(Path(tmpdir) / "tmp.json"))
-        response = graph.query(query_str, query_configs=query_configs)
-        assert str(response) == ("Test?:Test?:This is a test.:Test?:This is a test.")
-
-
-@patch.object(TokenTextSplitter, "split_text", side_effect=mock_token_splitter_newline)
-@patch.object(LLMPredictor, "predict", side_effect=mock_llmpredictor_predict)
-@patch.object(LLMPredictor, "total_tokens_used", return_value=0)
-@patch.object(LLMPredictor, "__init__", return_value=None)
-def test_recursive_query_list_table(
-    _mock_init: Any,
-    _mock_total_tokens_used: Any,
-    _mock_predict: Any,
-    _mock_split_text: Any,
-    documents: List[Document],
-    struct_kwargs: Dict,
-) -> None:
-    """Test query."""
-    index_kwargs, query_configs = struct_kwargs
-    list_kwargs = index_kwargs["list"]
-    table_kwargs = index_kwargs["table"]
-    # try building a tree for a group of 4, then a list
-    # use a diff set of documents
-    # try building a list for every two, then a tree
-    list1 = GPTListIndex.from_documents(documents[0:2], **list_kwargs)
-    list2 = GPTListIndex.from_documents(documents[2:4], **list_kwargs)
-    list3 = GPTListIndex.from_documents(documents[4:6], **list_kwargs)
-    list4 = GPTListIndex.from_documents(documents[6:8], **list_kwargs)
-    summaries = [
-        "foo bar",
-        "apple orange",
-        "toronto london",
-        "cat dog",
-    ]
-
-    graph = ComposableGraph.from_indices(
-        GPTSimpleKeywordTableIndex,
-        [list1, list2, list3, list4],
-        index_summaries=summaries,
-        **table_kwargs
-    )
-    assert isinstance(graph, ComposableGraph)
-    query_str = "Foo?"
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == ("Foo?:Foo?:This is a test v2.:This is another test.")
-    query_str = "Orange?"
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == ("Orange?:Orange?:This is a test.:Hello world.")
-    query_str = "Cat?"
-    response = graph.query(query_str, query_configs=query_configs)
-    assert str(response) == ("Cat?:Cat?:This is another test.:This is a test v2.")
-
-    # test serialize and then back
-    # use composable graph struct
-    with TemporaryDirectory() as tmpdir:
-        graph.save_to_disk(str(Path(tmpdir) / "tmp.json"))
-        graph = ComposableGraph.load_from_disk(str(Path(tmpdir) / "tmp.json"))
-        response = graph.query(query_str, query_configs=query_configs)
-        assert str(response) == ("Cat?:Cat?:This is another test.:This is a test v2.")
-
-
-@patch.object(LLMChain, "predict", side_effect=mock_llmchain_predict)
-@patch("gpt_index.llm_predictor.base.OpenAI")
-@patch.object(LLMPredictor, "get_llm_metadata", return_value=LLMMetadata())
-@patch.object(LLMChain, "__init__", return_value=None)
-def test_recursive_query_list_tree_token_count(
-    _mock_init: Any,
-    _mock_llm_metadata: Any,
-    _mock_llmchain: Any,
-    _mock_predict: Any,
-    documents: List[Document],
-    struct_kwargs: Dict,
-) -> None:
-    """Test query."""
-    index_kwargs, query_configs = struct_kwargs
-    list_kwargs = index_kwargs["list"]
-    tree_kwargs = index_kwargs["tree"]
-    # try building a list for every two, then a tree
-    list1 = GPTListIndex.from_documents(documents[0:2], **list_kwargs)
-    list2 = GPTListIndex.from_documents(documents[2:4], **list_kwargs)
-    list3 = GPTListIndex.from_documents(documents[4:6], **list_kwargs)
-    list4 = GPTListIndex.from_documents(documents[6:8], **list_kwargs)
-
-    summary1 = "summary1"
-    summary2 = "summary2"
-    summary3 = "summary3"
-    summary4 = "summary4"
-    summaries = [summary1, summary2, summary3, summary4]
-
-    # there are two root nodes in this tree: one containing [list1, list2]
-    # and the other containing [list3, list4]
-    # import pdb; pdb.set_trace()
-    graph = ComposableGraph.from_indices(
-        GPTTreeIndex,
-        [
-            list1,
-            list2,
-            list3,
-            list4,
-        ],
-        index_summaries=summaries,
-        **tree_kwargs
-    )
-    assert isinstance(graph, ComposableGraph)
-    # first pass prompt is "summary1\nsummary2\n" (6 tokens),
-    # response is the mock response (10 tokens)
-    # total is 16 tokens, multiply by 2 to get the total
-    assert graph.service_context.llm_predictor.total_tokens_used == 32
-
-    query_str = "What is?"
-    # query should first pick the left root node, then pick list1
-    # within list1, it should go through the first document and second document
-    start_token_ct = graph.service_context.llm_predictor.total_tokens_used
-    graph.query(query_str, query_configs=query_configs)
-    # prompt is which is 35 tokens, plus 10 for the mock response
-    assert graph.service_context.llm_predictor.total_tokens_used - start_token_ct == 45
-
-
 def mock_get_query_embedding(query: str) -> List[float]:
     """Mock get query embedding."""
     if query == "Foo?":
         return [0, 0, 1, 0, 0]
     elif query == "Orange?":
         return [0, 1, 0, 0, 0]
     elif query == "Cat?":
@@ -693,7 +453,114 @@
     # test serialize and then back
     # use composable graph struct
     with TemporaryDirectory() as tmpdir:
         graph.save_to_disk(str(Path(tmpdir) / "tmp.json"))
         graph = ComposableGraph.load_from_disk(str(Path(tmpdir) / "tmp.json"))
         response = graph.query(query_str, query_configs=query_configs)
         assert str(response) == ("Cat?:Cat?:This is a test v2.")
+
+
+@patch.object(TokenTextSplitter, "split_text", side_effect=mock_token_splitter_newline)
+@patch.object(LLMPredictor, "predict", side_effect=mock_llmpredictor_predict)
+@patch.object(LLMPredictor, "total_tokens_used", return_value=0)
+@patch.object(LLMPredictor, "__init__", return_value=None)
+@patch.object(
+    OpenAIEmbedding, "_get_text_embedding", side_effect=mock_get_text_embedding
+)
+@patch.object(
+    OpenAIEmbedding, "_get_text_embeddings", side_effect=mock_get_text_embeddings
+)
+@patch.object(
+    OpenAIEmbedding, "get_query_embedding", side_effect=mock_get_query_embedding
+)
+def test_recursive_query_pinecone_pinecone(
+    _mock_query_embed: Any,
+    _mock_get_text_embeds: Any,
+    _mock_get_text_embed: Any,
+    _mock_init: Any,
+    _mock_total_tokens_used: Any,
+    _mock_predict: Any,
+    _mock_split_text: Any,
+    documents: List[Document],
+    struct_kwargs: Dict,
+) -> None:
+    """Test composing pinecone index on top of pinecone index."""
+    # NOTE: mock pinecone import
+    sys.modules["pinecone"] = MagicMock()
+    # NOTE: mock pinecone index, use separate instances
+    #       to make testing easier
+    pinecone_index1 = MockPineconeIndex()
+    pinecone_index2 = MockPineconeIndex()
+    pinecone_index3 = MockPineconeIndex()
+    pinecone_index4 = MockPineconeIndex()
+    pinecone_index5 = MockPineconeIndex()
+
+    index_kwargs, query_configs = struct_kwargs
+    pinecone_kwargs = index_kwargs["pinecone"]
+    # try building a tree for a group of 4, then a list
+    # use a diff set of documents
+    # try building a list for every two, then a tree
+    pinecone1 = GPTPineconeIndex.from_documents(
+        documents[0:2], pinecone_index=pinecone_index1, **pinecone_kwargs
+    )
+    pinecone2 = GPTPineconeIndex.from_documents(
+        documents[2:4], pinecone_index=pinecone_index2, **pinecone_kwargs
+    )
+    pinecone3 = GPTPineconeIndex.from_documents(
+        documents[4:6], pinecone_index=pinecone_index3, **pinecone_kwargs
+    )
+    pinecone4 = GPTPineconeIndex.from_documents(
+        documents[6:8], pinecone_index=pinecone_index4, **pinecone_kwargs
+    )
+
+    summary1 = "foo bar"
+    summary2 = "apple orange"
+    summary3 = "toronto london"
+    summary4 = "cat dog"
+    summaries = [summary1, summary2, summary3, summary4]
+
+    graph = ComposableGraph.from_indices(
+        GPTPineconeIndex,
+        [pinecone1, pinecone2, pinecone3, pinecone4],
+        index_summaries=summaries,
+        pinecone_index=pinecone_index5,
+        **pinecone_kwargs
+    )
+    query_str = "Foo?"
+    response = graph.query(query_str, query_configs=query_configs)
+    assert str(response) == ("Foo?:Foo?:This is another test.")
+    query_str = "Orange?"
+    response = graph.query(query_str, query_configs=query_configs)
+    assert str(response) == ("Orange?:Orange?:This is a test.")
+    query_str = "Cat?"
+    response = graph.query(query_str, query_configs=query_configs)
+    assert str(response) == ("Cat?:Cat?:This is a test v2.")
+
+    # test serialize and then back
+    # use composable graph struct
+    with TemporaryDirectory() as tmpdir:
+        graph.save_to_disk(str(Path(tmpdir) / "tmp.json"))
+        query_context_kwargs = {
+            index_id: {"vector_store": {"pinecone_index": pinecone_index}}
+            for index_id, pinecone_index in zip(
+                [
+                    pinecone1.index_struct.index_id,
+                    pinecone2.index_struct.index_id,
+                    pinecone3.index_struct.index_id,
+                    pinecone4.index_struct.index_id,
+                    graph.index_struct.root_id,
+                ],
+                [
+                    pinecone_index1,
+                    pinecone_index2,
+                    pinecone_index3,
+                    pinecone_index4,
+                    pinecone_index5,
+                ],
+            )
+        }
+        print(query_context_kwargs)
+        graph = ComposableGraph.load_from_disk(
+            str(Path(tmpdir) / "tmp.json"), query_context_kwargs=query_context_kwargs
+        )
+        response = graph.query(query_str, query_configs=query_configs)
+        assert str(response) == ("Cat?:Cat?:This is a test v2.")
```

### Comparing `gpt_index-0.5.8/tests/indices/struct_store/test_base.py` & `gpt_index-0.5.9/tests/indices/struct_store/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/struct_store/test_pandas.py` & `gpt_index-0.5.9/tests/indices/struct_store/test_pandas.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/test_node_utils.py` & `gpt_index-0.5.9/tests/indices/test_node_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/test_prompt_helper.py` & `gpt_index-0.5.9/tests/indices/test_prompt_helper.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/test_response.py` & `gpt_index-0.5.9/tests/indices/test_response.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/test_save_load.py` & `gpt_index-0.5.9/tests/indices/test_save_load.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/tree/test_base.py` & `gpt_index-0.5.9/tests/indices/tree/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/indices/vector_store/test_base.py` & `gpt_index-0.5.9/tests/indices/vector_store/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/langchain_helpers/test_text_splitter.py` & `gpt_index-0.5.9/tests/langchain_helpers/test_text_splitter.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/llm_predictor/test_base.py` & `gpt_index-0.5.9/tests/llm_predictor/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/logger/test_base.py` & `gpt_index-0.5.9/tests/logger/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/mock_utils/mock_decorator.py` & `gpt_index-0.5.9/tests/mock_utils/mock_decorator.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/mock_utils/mock_predict.py` & `gpt_index-0.5.9/tests/mock_utils/mock_predict.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/mock_utils/mock_prompts.py` & `gpt_index-0.5.9/tests/mock_utils/mock_prompts.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/mock_utils/mock_text_splitter.py` & `gpt_index-0.5.9/tests/mock_utils/mock_text_splitter.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/mock_utils/mock_utils.py` & `gpt_index-0.5.9/tests/mock_utils/mock_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/optimization/test_base.py` & `gpt_index-0.5.9/tests/optimization/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/output_parsers/test_base.py` & `gpt_index-0.5.9/tests/output_parsers/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/playground/test_base.py` & `gpt_index-0.5.9/tests/playground/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/prompts/test_base.py` & `gpt_index-0.5.9/tests/prompts/test_base.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/readers/test_file.py` & `gpt_index-0.5.9/tests/readers/test_file.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/readers/test_json.py` & `gpt_index-0.5.9/tests/readers/test_json.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/test_docstore.py` & `gpt_index-0.5.9/tests/test_docstore.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/test_utils.py` & `gpt_index-0.5.9/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `gpt_index-0.5.8/tests/token_predictor/test_base.py` & `gpt_index-0.5.9/tests/token_predictor/test_base.py`

 * *Files identical despite different names*

