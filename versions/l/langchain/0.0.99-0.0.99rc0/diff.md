# Comparing `tmp/langchain-0.0.99.tar.gz` & `tmp/langchain-0.0.99rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "langchain-0.0.99.tar", max compression
+gzip compressed data, was "langchain-0.0.99rc0.tar", max compression
```

## Comparing `langchain-0.0.99.tar` & `langchain-0.0.99rc0.tar`

### file list

```diff
@@ -1,311 +1,317 @@
--rw-r--r--   0        0        0     1069 2023-03-02 15:26:16.382847 langchain-0.0.99/LICENSE
--rw-r--r--   0        0        0     4759 2023-03-02 15:26:16.382847 langchain-0.0.99/README.md
--rw-r--r--   0        0        0     2497 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/__init__.py
--rw-r--r--   0        0        0     1340 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/__init__.py
--rw-r--r--   0        0        0    21152 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent.py
--rw-r--r--   0        0        0     1368 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/__init__.py
--rw-r--r--   0        0        0      364 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/base.py
--rw-r--r--   0        0        0       19 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/csv/__init__.py
--rw-r--r--   0        0        0      603 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/csv/base.py
--rw-r--r--   0        0        0       18 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/json/__init__.py
--rw-r--r--   0        0        0     1517 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/json/base.py
--rw-r--r--   0        0        0     1819 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/json/prompt.py
--rw-r--r--   0        0        0      603 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/json/toolkit.py
--rw-r--r--   0        0        0       26 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/openapi/__init__.py
--rw-r--r--   0        0        0     1565 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/openapi/base.py
--rw-r--r--   0        0        0     1744 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/openapi/prompt.py
--rw-r--r--   0        0        0     2310 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/openapi/toolkit.py
--rw-r--r--   0        0        0       22 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/pandas/__init__.py
--rw-r--r--   0        0        0     1615 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/pandas/base.py
--rw-r--r--   0        0        0      295 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/pandas/prompt.py
--rw-r--r--   0        0        0        0 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/python/__init__.py
--rw-r--r--   0        0        0     1112 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/python/base.py
--rw-r--r--   0        0        0      513 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/python/prompt.py
--rw-r--r--   0        0        0       17 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/sql/__init__.py
--rw-r--r--   0        0        0     1608 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/sql/base.py
--rw-r--r--   0        0        0     1213 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/sql/prompt.py
--rw-r--r--   0        0        0     1079 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/sql/toolkit.py
--rw-r--r--   0        0        0       56 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/__init__.py
--rw-r--r--   0        0        0     1988 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/base.py
--rw-r--r--   0        0        0      834 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/prompt.py
--rw-r--r--   0        0        0     2918 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/toolkit.py
--rw-r--r--   0        0        0       75 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/conversational/__init__.py
--rw-r--r--   0        0        0     4475 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/conversational/base.py
--rw-r--r--   0        0        0     1859 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/conversational/prompt.py
--rw-r--r--   0        0        0     2549 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/initialize.py
--rw-r--r--   0        0        0     9031 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/load_tools.py
--rw-r--r--   0        0        0     3909 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/loading.py
--rw-r--r--   0        0        0       86 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/mrkl/__init__.py
--rw-r--r--   0        0        0     7159 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/mrkl/base.py
--rw-r--r--   0        0        0      641 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/mrkl/prompt.py
--rw-r--r--   0        0        0       76 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/react/__init__.py
--rw-r--r--   0        0        0     5155 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/react/base.py
--rw-r--r--   0        0        0     1923 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/react/textworld_prompt.py
--rw-r--r--   0        0        0     6229 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/react/wiki_prompt.py
--rw-r--r--   0        0        0      106 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/self_ask_with_search/__init__.py
--rw-r--r--   0        0        0     3286 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/self_ask_with_search/base.py
--rw-r--r--   0        0        0     1921 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/self_ask_with_search/prompt.py
--rw-r--r--   0        0        0     3603 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/agents/tools.py
--rw-r--r--   0        0        0     5086 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/cache.py
--rw-r--r--   0        0        0     2109 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/__init__.py
--rw-r--r--   0        0        0    21582 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/base.py
--rw-r--r--   0        0        0     2938 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/openai_info.py
--rw-r--r--   0        0        0     4604 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/shared.py
--rw-r--r--   0        0        0     3120 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/stdout.py
--rw-r--r--   0        0        0     2170 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/streaming_stdout.py
--rw-r--r--   0        0        0     2898 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/streamlit.py
--rw-r--r--   0        0        0      465 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/tracers/__init__.py
--rw-r--r--   0        0        0    11282 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/tracers/base.py
--rw-r--r--   0        0        0     3994 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/tracers/langchain.py
--rw-r--r--   0        0        0     2047 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/callbacks/tracers/schemas.py
--rw-r--r--   0        0        0     2170 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/__init__.py
--rw-r--r--   0        0        0       84 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/api/__init__.py
--rw-r--r--   0        0        0     3813 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/api/base.py
--rw-r--r--   0        0        0     2452 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/api/news_docs.py
--rw-r--r--   0        0        0     3399 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/api/open_meteo_docs.py
--rw-r--r--   0        0        0     1026 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/api/prompt.py
--rw-r--r--   0        0        0     1537 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/api/tmdb_docs.py
--rw-r--r--   0        0        0    11436 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/base.py
--rw-r--r--   0        0        0       49 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/chat_vector_db/__init__.py
--rw-r--r--   0        0        0     4519 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/chat_vector_db/base.py
--rw-r--r--   0        0        0      689 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/chat_vector_db/prompts.py
--rw-r--r--   0        0        0       43 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/combine_documents/__init__.py
--rw-r--r--   0        0        0     3442 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/combine_documents/base.py
--rw-r--r--   0        0        0     7914 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/combine_documents/map_reduce.py
--rw-r--r--   0        0        0     5461 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/combine_documents/map_rerank.py
--rw-r--r--   0        0        0     5929 2023-03-02 15:26:16.430848 langchain-0.0.99/langchain/chains/combine_documents/refine.py
--rw-r--r--   0        0        0     4193 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/combine_documents/stuff.py
--rw-r--r--   0        0        0      107 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/constitutional_ai/__init__.py
--rw-r--r--   0        0        0     4543 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/constitutional_ai/base.py
--rw-r--r--   0        0        0      265 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/constitutional_ai/models.py
--rw-r--r--   0        0        0     7293 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/constitutional_ai/prompts.py
--rw-r--r--   0        0        0       71 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/conversation/__init__.py
--rw-r--r--   0        0        0     2239 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/conversation/base.py
--rw-r--r--   0        0        0    18515 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/conversation/memory.py
--rw-r--r--   0        0        0     8582 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/conversation/prompt.py
--rw-r--r--   0        0        0       49 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/graph_qa/__init__.py
--rw-r--r--   0        0        0     2625 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/graph_qa/base.py
--rw-r--r--   0        0        0     1224 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/graph_qa/prompts.py
--rw-r--r--   0        0        0       75 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/hyde/__init__.py
--rw-r--r--   0        0        0     2478 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/hyde/base.py
--rw-r--r--   0        0        0     1908 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/hyde/prompts.py
--rw-r--r--   0        0        0     7459 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm.py
--rw-r--r--   0        0        0       88 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_bash/__init__.py
--rw-r--r--   0        0        0     2475 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_bash/base.py
--rw-r--r--   0        0        0      818 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_bash/prompt.py
--rw-r--r--   0        0        0      139 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_checker/__init__.py
--rw-r--r--   0        0        0     3139 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_checker/base.py
--rw-r--r--   0        0        0     1120 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_checker/prompt.py
--rw-r--r--   0        0        0      143 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_math/__init__.py
--rw-r--r--   0        0        0     3009 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_math/base.py
--rw-r--r--   0        0        0     1031 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_math/prompt.py
--rw-r--r--   0        0        0     2521 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_requests.py
--rw-r--r--   0        0        0      352 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_summarization_checker/__init__.py
--rw-r--r--   0        0        0     4269 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_summarization_checker/base.py
--rw-r--r--   0        0        0      654 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_summarization_checker/prompts/are_all_true_prompt.txt
--rw-r--r--   0        0        0      377 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_summarization_checker/prompts/check_facts.txt
--rw-r--r--   0        0        0      128 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_summarization_checker/prompts/create_facts.txt
--rw-r--r--   0        0        0      417 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/llm_summarization_checker/prompts/revise_summary.txt
--rw-r--r--   0        0        0    19407 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/loading.py
--rw-r--r--   0        0        0     2512 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/mapreduce.py
--rw-r--r--   0        0        0     2602 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/moderation.py
--rw-r--r--   0        0        0       96 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/natbot/__init__.py
--rw-r--r--   0        0        0     3026 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/natbot/base.py
--rw-r--r--   0        0        0    15382 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/natbot/crawler.py
--rw-r--r--   0        0        0     4984 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/natbot/prompt.py
--rw-r--r--   0        0        0       94 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/pal/__init__.py
--rw-r--r--   0        0        0     2906 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/pal/base.py
--rw-r--r--   0        0        0     2645 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/pal/colored_object_prompt.py
--rw-r--r--   0        0        0     4301 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/pal/math_prompt.py
--rw-r--r--   0        0        0      173 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/__init__.py
--rw-r--r--   0        0        0     4524 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/base.py
--rw-r--r--   0        0        0     6314 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/loading.py
--rw-r--r--   0        0        0     6966 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/map_reduce_prompt.py
--rw-r--r--   0        0        0     1313 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/refine_prompts.py
--rw-r--r--   0        0        0     6576 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/stuff_prompt.py
--rw-r--r--   0        0        0     2117 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/qa_with_sources/vector_db.py
--rw-r--r--   0        0        0     7085 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/question_answering/__init__.py
--rw-r--r--   0        0        0     6635 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/question_answering/map_reduce_prompt.py
--rw-r--r--   0        0        0     1608 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/question_answering/map_rerank_prompt.py
--rw-r--r--   0        0        0     1089 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/question_answering/refine_prompts.py
--rw-r--r--   0        0        0      394 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/question_answering/stuff_prompt.py
--rw-r--r--   0        0        0     4712 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/sequential.py
--rw-r--r--   0        0        0       47 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/sql_database/__init__.py
--rw-r--r--   0        0        0     6408 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/sql_database/base.py
--rw-r--r--   0        0        0     1629 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/sql_database/prompt.py
--rw-r--r--   0        0        0     5036 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/summarize/__init__.py
--rw-r--r--   0        0        0      233 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/summarize/map_reduce_prompt.py
--rw-r--r--   0        0        0      803 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/summarize/refine_prompts.py
--rw-r--r--   0        0        0      233 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/summarize/stuff_prompt.py
--rw-r--r--   0        0        0     1018 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/transform.py
--rw-r--r--   0        0        0       62 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/vector_db_qa/__init__.py
--rw-r--r--   0        0        0     6044 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/vector_db_qa/base.py
--rw-r--r--   0        0        0      394 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/chains/vector_db_qa/prompt.py
--rw-r--r--   0        0        0      689 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/docker-compose.yaml
--rw-r--r--   0        0        0      190 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/docstore/__init__.py
--rw-r--r--   0        0        0      700 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/docstore/base.py
--rw-r--r--   0        0        0     1262 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/docstore/document.py
--rw-r--r--   0        0        0      972 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/docstore/in_memory.py
--rw-r--r--   0        0        0     1377 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/docstore/wikipedia.py
--rw-r--r--   0        0        0     3601 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/__init__.py
--rw-r--r--   0        0        0     1247 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/airbyte_json.py
--rw-r--r--   0        0        0      584 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/azlyrics.py
--rw-r--r--   0        0        0      794 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/base.py
--rw-r--r--   0        0        0      562 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/college_confidential.py
--rw-r--r--   0        0        0     1097 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/conllu.py
--rw-r--r--   0        0        0     1941 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/directory.py
--rw-r--r--   0        0        0      429 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/docx.py
--rw-r--r--   0        0        0      415 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/email.py
--rw-r--r--   0        0        0     2550 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/evernote.py
--rw-r--r--   0        0        0     1816 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/facebook_chat.py
--rw-r--r--   0        0        0     1215 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/gcs_directory.py
--rw-r--r--   0        0        0     1509 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/gcs_file.py
--rw-r--r--   0        0        0     2066 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/gitbook.py
--rw-r--r--   0        0        0     5195 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/googledrive.py
--rw-r--r--   0        0        0      979 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/gutenberg.py
--rw-r--r--   0        0        0     2062 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/hn.py
--rw-r--r--   0        0        0      408 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/html.py
--rw-r--r--   0        0        0     6775 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/ifixit.py
--rw-r--r--   0        0        0      438 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/image.py
--rw-r--r--   0        0        0      511 2023-03-02 15:26:16.434848 langchain-0.0.99/langchain/document_loaders/imsdb.py
--rw-r--r--   0        0        0     3490 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/notebook.py
--rw-r--r--   0        0        0      758 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/notion.py
--rw-r--r--   0        0        0      756 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/obsidian.py
--rw-r--r--   0        0        0      903 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/online_pdf.py
--rw-r--r--   0        0        0     1152 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/paged_pdf.py
--rw-r--r--   0        0        0     1257 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/pdf.py
--rw-r--r--   0        0        0     1668 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/powerpoint.py
--rw-r--r--   0        0        0     1194 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/readthedocs.py
--rw-r--r--   0        0        0      744 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/roam.py
--rw-r--r--   0        0        0     1083 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/s3_directory.py
--rw-r--r--   0        0        0     1109 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/s3_file.py
--rw-r--r--   0        0        0      872 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/srt.py
--rw-r--r--   0        0        0     1710 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/telegram.py
--rw-r--r--   0        0        0      580 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/text.py
--rw-r--r--   0        0        0     3114 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/unstructured.py
--rw-r--r--   0        0        0     1059 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/url.py
--rw-r--r--   0        0        0     1017 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/web_base.py
--rw-r--r--   0        0        0     1666 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/word_document.py
--rw-r--r--   0        0        0     2682 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/document_loaders/youtube.py
--rw-r--r--   0        0        0     1822 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/__init__.py
--rw-r--r--   0        0        0      395 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/base.py
--rw-r--r--   0        0        0     2489 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/cohere.py
--rw-r--r--   0        0        0     4545 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/huggingface.py
--rw-r--r--   0        0        0     3752 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/huggingface_hub.py
--rw-r--r--   0        0        0     6452 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/openai.py
--rw-r--r--   0        0        0     3844 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/self_hosted.py
--rw-r--r--   0        0        0     6692 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/self_hosted_hugging_face.py
--rw-r--r--   0        0        0     2182 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/embeddings/tensorflow_hub.py
--rw-r--r--   0        0        0       51 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/evaluation/__init__.py
--rw-r--r--   0        0        0      251 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/evaluation/qa/__init__.py
--rw-r--r--   0        0        0     1940 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/evaluation/qa/eval_chain.py
--rw-r--r--   0        0        0      623 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/evaluation/qa/eval_prompt.py
--rw-r--r--   0        0        0      583 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/evaluation/qa/generate_chain.py
--rw-r--r--   0        0        0      724 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/evaluation/qa/generate_prompt.py
--rw-r--r--   0        0        0      749 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/example_generator.py
--rw-r--r--   0        0        0      981 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/formatting.py
--rw-r--r--   0        0        0      128 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/graphs/__init__.py
--rw-r--r--   0        0        0     3439 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/graphs/networkx_graph.py
--rw-r--r--   0        0        0      203 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/__init__.py
--rw-r--r--   0        0        0     1029 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/graph.py
--rw-r--r--   0        0        0       49 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/prompts/__init__.py
--rw-r--r--   0        0        0     1947 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/prompts/entity_extraction.py
--rw-r--r--   0        0        0     1152 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/prompts/entity_summarization.py
--rw-r--r--   0        0        0     1584 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/prompts/knowledge_triplet_extraction.py
--rw-r--r--   0        0        0     2606 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/indexes/vectorstore.py
--rw-r--r--   0        0        0     1092 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/input.py
--rw-r--r--   0        0        0     2356 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/__init__.py
--rw-r--r--   0        0        0     4815 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/ai21.py
--rw-r--r--   0        0        0     9259 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/aleph_alpha.py
--rw-r--r--   0        0        0     6417 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/anthropic.py
--rw-r--r--   0        0        0     4152 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/bananadev.py
--rw-r--r--   0        0        0    13392 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/base.py
--rw-r--r--   0        0        0     3628 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/cerebriumai.py
--rw-r--r--   0        0        0     4279 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/cohere.py
--rw-r--r--   0        0        0     3066 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/deepinfra.py
--rw-r--r--   0        0        0      717 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/fake.py
--rw-r--r--   0        0        0     3534 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/forefrontai.py
--rw-r--r--   0        0        0     4967 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/gooseai.py
--rw-r--r--   0        0        0     4940 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/huggingface_endpoint.py
--rw-r--r--   0        0        0     4308 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/huggingface_hub.py
--rw-r--r--   0        0        0     5760 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/huggingface_pipeline.py
--rw-r--r--   0        0        0     1250 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/loading.py
--rw-r--r--   0        0        0     1746 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/manifest.py
--rw-r--r--   0        0        0     3085 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/modal.py
--rw-r--r--   0        0        0     5010 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/nlpcloud.py
--rw-r--r--   0        0        0    25553 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/openai.py
--rw-r--r--   0        0        0     5082 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/petals.py
--rw-r--r--   0        0        0     2787 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/promptlayer_openai.py
--rw-r--r--   0        0        0     7533 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/self_hosted.py
--rw-r--r--   0        0        0     7435 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/self_hosted_hugging_face.py
--rw-r--r--   0        0        0     4418 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/stochasticai.py
--rw-r--r--   0        0        0      259 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/utils.py
--rw-r--r--   0        0        0     5015 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/llms/writer.py
--rw-r--r--   0        0        0     3230 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/model_laboratory.py
--rw-r--r--   0        0        0      496 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/__init__.py
--rw-r--r--   0        0        0     7525 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/base.py
--rw-r--r--   0        0        0      429 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/example_selector/__init__.py
--rw-r--r--   0        0        0      526 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/example_selector/base.py
--rw-r--r--   0        0        0     2433 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/example_selector/length_based.py
--rw-r--r--   0        0        0     3733 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/example_selector/ngram_overlap.py
--rw-r--r--   0        0        0     6840 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/example_selector/semantic_similarity.py
--rw-r--r--   0        0        0     4399 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/few_shot.py
--rw-r--r--   0        0        0     5436 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/few_shot_with_templates.py
--rw-r--r--   0        0        0     5908 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/loading.py
--rw-r--r--   0        0        0     4290 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/prompts/prompt.py
--rw-r--r--   0        0        0        0 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/py.typed
--rw-r--r--   0        0        0      816 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/python.py
--rw-r--r--   0        0        0     2831 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/requests.py
--rw-r--r--   0        0        0     1099 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/schema.py
--rw-r--r--   0        0        0      119 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/serpapi.py
--rw-r--r--   0        0        0      401 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/server.py
--rw-r--r--   0        0        0     8647 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/sql_database.py
--rw-r--r--   0        0        0    12904 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/text_splitter.py
--rw-r--r--   0        0        0      166 2023-03-02 15:26:16.438848 langchain-0.0.99/langchain/tools/__init__.py
--rw-r--r--   0        0        0     3985 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/base.py
--rw-r--r--   0        0        0       31 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/bing_search/__init__.py
--rw-r--r--   0        0        0      773 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/bing_search/tool.py
--rw-r--r--   0        0        0       33 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/google_search/__init__.py
--rw-r--r--   0        0        0     1558 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/google_search/tool.py
--rw-r--r--   0        0        0     2213 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/ifttt.py
--rw-r--r--   0        0        0       43 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/interaction/__init__.py
--rw-r--r--   0        0        0      681 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/interaction/tool.py
--rw-r--r--   0        0        0       46 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/json/__init__.py
--rw-r--r--   0        0        0     3604 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/json/tool.py
--rw-r--r--   0        0        0        0 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/python/__init__.py
--rw-r--r--   0        0        0     2831 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/python/tool.py
--rw-r--r--   0        0        0       52 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/requests/__init__.py
--rw-r--r--   0        0        0     4961 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/requests/tool.py
--rw-r--r--   0        0        0       49 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/sql_database/__init__.py
--rw-r--r--   0        0        0      550 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/sql_database/prompt.py
--rw-r--r--   0        0        0     4163 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/sql_database/tool.py
--rw-r--r--   0        0        0       51 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/vectorstore/__init__.py
--rw-r--r--   0        0        0     3082 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/vectorstore/tool.py
--rw-r--r--   0        0        0       33 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/wolfram_alpha/__init__.py
--rw-r--r--   0        0        0      891 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/tools/wolfram_alpha/tool.py
--rw-r--r--   0        0        0      793 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/__init__.py
--rw-r--r--   0        0        0     1135 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/bash.py
--rw-r--r--   0        0        0     3333 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/bing_search.py
--rw-r--r--   0        0        0     4834 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/google_search.py
--rw-r--r--   0        0        0     3309 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/google_serper.py
--rw-r--r--   0        0        0     1582 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/loading.py
--rw-r--r--   0        0        0    11962 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/searx_search.py
--rw-r--r--   0        0        0     5154 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/serpapi.py
--rw-r--r--   0        0        0     1989 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utilities/wolfram_alpha.py
--rw-r--r--   0        0        0      689 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/utils.py
--rw-r--r--   0        0        0      863 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/__init__.py
--rw-r--r--   0        0        0    11988 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/atlas.py
--rw-r--r--   0        0        0     4159 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/base.py
--rw-r--r--   0        0        0     8270 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/chroma.py
--rw-r--r--   0        0        0     7676 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/deeplake.py
--rw-r--r--   0        0        0     6859 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/elastic_vector_search.py
--rw-r--r--   0        0        0    11101 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/faiss.py
--rw-r--r--   0        0        0    16140 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/milvus.py
--rw-r--r--   0        0        0    13583 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/opensearch_vector_search.py
--rw-r--r--   0        0        0     8551 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/pinecone.py
--rw-r--r--   0        0        0    13234 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/qdrant.py
--rw-r--r--   0        0        0     1227 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/utils.py
--rw-r--r--   0        0        0     3433 2023-03-02 15:26:16.442848 langchain-0.0.99/langchain/vectorstores/weaviate.py
--rw-r--r--   0        0        0     3894 2023-03-02 15:26:16.446848 langchain-0.0.99/pyproject.toml
--rw-r--r--   0        0        0     9039 1970-01-01 00:00:00.000000 langchain-0.0.99/setup.py
--rw-r--r--   0        0        0     7698 1970-01-01 00:00:00.000000 langchain-0.0.99/PKG-INFO
+-rw-r--r--   0        0        0     1069 2023-02-08 19:01:44.077010 langchain-0.0.99rc0/LICENSE
+-rw-r--r--   0        0        0     4759 2023-02-08 19:01:44.077118 langchain-0.0.99rc0/README.md
+-rw-r--r--   0        0        0     2497 2023-02-27 06:10:52.978388 langchain-0.0.99rc0/langchain/__init__.py
+-rw-r--r--   0        0        0     1340 2023-03-01 06:26:30.792774 langchain-0.0.99rc0/langchain/agents/__init__.py
+-rw-r--r--   0        0        0    21152 2023-03-01 03:50:13.734144 langchain-0.0.99rc0/langchain/agents/agent.py
+-rw-r--r--   0        0        0     1368 2023-03-01 06:26:30.793031 langchain-0.0.99rc0/langchain/agents/agent_toolkits/__init__.py
+-rw-r--r--   0        0        0      364 2023-03-01 03:50:13.734472 langchain-0.0.99rc0/langchain/agents/agent_toolkits/base.py
+-rw-r--r--   0        0        0       19 2023-03-01 06:26:30.793170 langchain-0.0.99rc0/langchain/agents/agent_toolkits/csv/__init__.py
+-rw-r--r--   0        0        0      603 2023-03-01 06:26:30.793290 langchain-0.0.99rc0/langchain/agents/agent_toolkits/csv/base.py
+-rw-r--r--   0        0        0       18 2023-03-01 03:50:13.734674 langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/__init__.py
+-rw-r--r--   0        0        0     1517 2023-03-01 03:50:13.734856 langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/base.py
+-rw-r--r--   0        0        0     1819 2023-03-01 03:50:13.735036 langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/prompt.py
+-rw-r--r--   0        0        0      603 2023-03-01 03:50:13.735200 langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/toolkit.py
+-rw-r--r--   0        0        0       26 2023-03-01 03:50:13.735362 langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/__init__.py
+-rw-r--r--   0        0        0     1565 2023-03-01 03:50:13.735541 langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/base.py
+-rw-r--r--   0        0        0     1744 2023-03-01 03:50:13.735754 langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/prompt.py
+-rw-r--r--   0        0        0     2310 2023-03-01 03:50:13.735891 langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/toolkit.py
+-rw-r--r--   0        0        0       22 2023-03-01 06:26:30.793412 langchain-0.0.99rc0/langchain/agents/agent_toolkits/pandas/__init__.py
+-rw-r--r--   0        0        0     1615 2023-03-01 06:26:30.793530 langchain-0.0.99rc0/langchain/agents/agent_toolkits/pandas/base.py
+-rw-r--r--   0        0        0      295 2023-03-01 06:26:30.793643 langchain-0.0.99rc0/langchain/agents/agent_toolkits/pandas/prompt.py
+-rw-r--r--   0        0        0        0 2023-03-01 03:50:13.735920 langchain-0.0.99rc0/langchain/agents/agent_toolkits/python/__init__.py
+-rw-r--r--   0        0        0     1112 2023-03-01 06:26:30.793804 langchain-0.0.99rc0/langchain/agents/agent_toolkits/python/base.py
+-rw-r--r--   0        0        0      513 2023-03-01 03:50:13.736302 langchain-0.0.99rc0/langchain/agents/agent_toolkits/python/prompt.py
+-rw-r--r--   0        0        0       17 2023-03-01 03:50:13.736464 langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/__init__.py
+-rw-r--r--   0        0        0     1608 2023-03-01 03:50:13.736559 langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/base.py
+-rw-r--r--   0        0        0     1236 2023-03-01 03:50:13.736740 langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/prompt.py
+-rw-r--r--   0        0        0     1079 2023-03-01 03:50:13.736850 langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/toolkit.py
+-rw-r--r--   0        0        0       56 2023-03-01 03:50:13.737054 langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/__init__.py
+-rw-r--r--   0        0        0     1988 2023-03-01 03:50:13.737268 langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/base.py
+-rw-r--r--   0        0        0      834 2023-03-01 03:50:13.737451 langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/prompt.py
+-rw-r--r--   0        0        0     2918 2023-03-01 03:50:13.737661 langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/toolkit.py
+-rw-r--r--   0        0        0       75 2023-02-08 19:01:44.107045 langchain-0.0.99rc0/langchain/agents/conversational/__init__.py
+-rw-r--r--   0        0        0     4475 2023-02-27 06:10:52.980870 langchain-0.0.99rc0/langchain/agents/conversational/base.py
+-rw-r--r--   0        0        0     1859 2023-02-08 19:01:44.107173 langchain-0.0.99rc0/langchain/agents/conversational/prompt.py
+-rw-r--r--   0        0        0     2549 2023-02-27 06:10:52.981124 langchain-0.0.99rc0/langchain/agents/initialize.py
+-rw-r--r--   0        0        0     9031 2023-03-01 03:50:13.737825 langchain-0.0.99rc0/langchain/agents/load_tools.py
+-rw-r--r--   0        0        0     3909 2023-02-08 19:01:44.107347 langchain-0.0.99rc0/langchain/agents/loading.py
+-rw-r--r--   0        0        0       86 2023-02-08 19:01:44.107414 langchain-0.0.99rc0/langchain/agents/mrkl/__init__.py
+-rw-r--r--   0        0        0     7159 2023-02-27 06:10:52.981695 langchain-0.0.99rc0/langchain/agents/mrkl/base.py
+-rw-r--r--   0        0        0      641 2023-02-27 01:53:41.912189 langchain-0.0.99rc0/langchain/agents/mrkl/prompt.py
+-rw-r--r--   0        0        0       76 2023-02-08 19:01:44.107609 langchain-0.0.99rc0/langchain/agents/react/__init__.py
+-rw-r--r--   0        0        0     5155 2023-02-27 06:10:52.982099 langchain-0.0.99rc0/langchain/agents/react/base.py
+-rw-r--r--   0        0        0     1923 2023-02-08 19:01:44.107722 langchain-0.0.99rc0/langchain/agents/react/textworld_prompt.py
+-rw-r--r--   0        0        0     6229 2023-02-08 19:01:44.107784 langchain-0.0.99rc0/langchain/agents/react/wiki_prompt.py
+-rw-r--r--   0        0        0      106 2023-02-08 19:01:44.107859 langchain-0.0.99rc0/langchain/agents/self_ask_with_search/__init__.py
+-rw-r--r--   0        0        0     3286 2023-02-27 06:10:52.982406 langchain-0.0.99rc0/langchain/agents/self_ask_with_search/base.py
+-rw-r--r--   0        0        0     1921 2023-02-08 19:01:44.107964 langchain-0.0.99rc0/langchain/agents/self_ask_with_search/prompt.py
+-rw-r--r--   0        0        0     3603 2023-02-27 06:10:52.982685 langchain-0.0.99rc0/langchain/agents/tools.py
+-rw-r--r--   0        0        0     5086 2023-02-27 22:44:33.825519 langchain-0.0.99rc0/langchain/cache.py
+-rw-r--r--   0        0        0     2109 2023-02-08 19:01:44.108163 langchain-0.0.99rc0/langchain/callbacks/__init__.py
+-rw-r--r--   0        0        0    21582 2023-02-27 06:10:52.983557 langchain-0.0.99rc0/langchain/callbacks/base.py
+-rw-r--r--   0        0        0     2938 2023-02-27 06:10:52.983968 langchain-0.0.99rc0/langchain/callbacks/openai_info.py
+-rw-r--r--   0        0        0     4604 2023-02-27 06:10:52.984138 langchain-0.0.99rc0/langchain/callbacks/shared.py
+-rw-r--r--   0        0        0     3120 2023-02-27 06:10:52.984457 langchain-0.0.99rc0/langchain/callbacks/stdout.py
+-rw-r--r--   0        0        0     2170 2023-02-27 06:10:52.984905 langchain-0.0.99rc0/langchain/callbacks/streaming_stdout.py
+-rw-r--r--   0        0        0     2898 2023-02-27 06:10:52.985054 langchain-0.0.99rc0/langchain/callbacks/streamlit.py
+-rw-r--r--   0        0        0      465 2023-02-08 19:01:44.108515 langchain-0.0.99rc0/langchain/callbacks/tracers/__init__.py
+-rw-r--r--   0        0        0    11282 2023-02-27 06:10:52.985204 langchain-0.0.99rc0/langchain/callbacks/tracers/base.py
+-rw-r--r--   0        0        0     3994 2023-02-08 19:01:44.108627 langchain-0.0.99rc0/langchain/callbacks/tracers/langchain.py
+-rw-r--r--   0        0        0     2047 2023-02-08 19:01:44.108672 langchain-0.0.99rc0/langchain/callbacks/tracers/schemas.py
+-rw-r--r--   0        0        0     2045 2023-03-01 18:24:28.323248 langchain-0.0.99rc0/langchain/chains/__init__.py
+-rw-r--r--   0        0        0       84 2023-02-08 19:01:44.108814 langchain-0.0.99rc0/langchain/chains/api/__init__.py
+-rw-r--r--   0        0        0     3813 2023-03-01 03:50:13.738075 langchain-0.0.99rc0/langchain/chains/api/base.py
+-rw-r--r--   0        0        0     2452 2023-02-08 19:01:44.108935 langchain-0.0.99rc0/langchain/chains/api/news_docs.py
+-rw-r--r--   0        0        0     3399 2023-02-08 19:01:44.108990 langchain-0.0.99rc0/langchain/chains/api/open_meteo_docs.py
+-rw-r--r--   0        0        0     1026 2023-02-08 19:01:44.109049 langchain-0.0.99rc0/langchain/chains/api/prompt.py
+-rw-r--r--   0        0        0     1537 2023-02-08 19:01:44.109097 langchain-0.0.99rc0/langchain/chains/api/tmdb_docs.py
+-rw-r--r--   0        0        0    11436 2023-02-27 06:10:52.985700 langchain-0.0.99rc0/langchain/chains/base.py
+-rw-r--r--   0        0        0       49 2023-02-08 19:01:44.109227 langchain-0.0.99rc0/langchain/chains/chat_vector_db/__init__.py
+-rw-r--r--   0        0        0     4519 2023-02-27 06:10:52.985930 langchain-0.0.99rc0/langchain/chains/chat_vector_db/base.py
+-rw-r--r--   0        0        0      689 2023-02-08 19:01:44.109330 langchain-0.0.99rc0/langchain/chains/chat_vector_db/prompts.py
+-rw-r--r--   0        0        0       43 2023-02-08 19:01:44.109395 langchain-0.0.99rc0/langchain/chains/combine_documents/__init__.py
+-rw-r--r--   0        0        0     3442 2023-02-27 06:10:52.986254 langchain-0.0.99rc0/langchain/chains/combine_documents/base.py
+-rw-r--r--   0        0        0     7914 2023-02-27 06:10:52.986528 langchain-0.0.99rc0/langchain/chains/combine_documents/map_reduce.py
+-rw-r--r--   0        0        0     5461 2023-02-27 06:10:52.986699 langchain-0.0.99rc0/langchain/chains/combine_documents/map_rerank.py
+-rw-r--r--   0        0        0     5929 2023-02-27 06:10:52.986877 langchain-0.0.99rc0/langchain/chains/combine_documents/refine.py
+-rw-r--r--   0        0        0     4193 2023-02-27 06:10:52.987133 langchain-0.0.99rc0/langchain/chains/combine_documents/stuff.py
+-rw-r--r--   0        0        0      107 2023-02-27 06:10:52.987255 langchain-0.0.99rc0/langchain/chains/constitutional_ai/__init__.py
+-rw-r--r--   0        0        0     4543 2023-02-27 06:10:52.987310 langchain-0.0.99rc0/langchain/chains/constitutional_ai/base.py
+-rw-r--r--   0        0        0      265 2023-02-27 06:10:52.987495 langchain-0.0.99rc0/langchain/chains/constitutional_ai/models.py
+-rw-r--r--   0        0        0     7293 2023-02-27 06:10:52.987661 langchain-0.0.99rc0/langchain/chains/constitutional_ai/prompts.py
+-rw-r--r--   0        0        0       71 2023-02-08 19:01:44.109768 langchain-0.0.99rc0/langchain/chains/conversation/__init__.py
+-rw-r--r--   0        0        0     2239 2023-02-08 19:01:44.109823 langchain-0.0.99rc0/langchain/chains/conversation/base.py
+-rw-r--r--   0        0        0    16116 2023-03-02 01:45:54.316258 langchain-0.0.99rc0/langchain/chains/conversation/memory.py
+-rw-r--r--   0        0        0     8582 2023-02-14 04:32:19.326357 langchain-0.0.99rc0/langchain/chains/conversation/prompt.py
+-rw-r--r--   0        0        0       49 2023-02-14 04:32:19.326502 langchain-0.0.99rc0/langchain/chains/graph_qa/__init__.py
+-rw-r--r--   0        0        0     2625 2023-02-14 04:32:19.326643 langchain-0.0.99rc0/langchain/chains/graph_qa/base.py
+-rw-r--r--   0        0        0     1224 2023-02-14 04:32:19.326940 langchain-0.0.99rc0/langchain/chains/graph_qa/prompts.py
+-rw-r--r--   0        0        0       75 2023-02-08 19:01:44.110042 langchain-0.0.99rc0/langchain/chains/hyde/__init__.py
+-rw-r--r--   0        0        0     2478 2023-02-08 19:01:44.110086 langchain-0.0.99rc0/langchain/chains/hyde/base.py
+-rw-r--r--   0        0        0     1908 2023-02-08 19:01:44.110133 langchain-0.0.99rc0/langchain/chains/hyde/prompts.py
+-rw-r--r--   0        0        0     7459 2023-02-27 06:10:52.988019 langchain-0.0.99rc0/langchain/chains/llm.py
+-rw-r--r--   0        0        0       88 2023-02-08 19:01:44.110262 langchain-0.0.99rc0/langchain/chains/llm_bash/__init__.py
+-rw-r--r--   0        0        0     2475 2023-02-08 19:01:44.110324 langchain-0.0.99rc0/langchain/chains/llm_bash/base.py
+-rw-r--r--   0        0        0      818 2023-02-08 19:01:44.110376 langchain-0.0.99rc0/langchain/chains/llm_bash/prompt.py
+-rw-r--r--   0        0        0      139 2023-02-08 19:01:44.110447 langchain-0.0.99rc0/langchain/chains/llm_checker/__init__.py
+-rw-r--r--   0        0        0     3139 2023-02-08 19:01:44.110511 langchain-0.0.99rc0/langchain/chains/llm_checker/base.py
+-rw-r--r--   0        0        0     1120 2023-02-08 19:01:44.110555 langchain-0.0.99rc0/langchain/chains/llm_checker/prompt.py
+-rw-r--r--   0        0        0      143 2023-02-08 19:01:44.110625 langchain-0.0.99rc0/langchain/chains/llm_math/__init__.py
+-rw-r--r--   0        0        0     3009 2023-02-08 19:01:44.110669 langchain-0.0.99rc0/langchain/chains/llm_math/base.py
+-rw-r--r--   0        0        0     1031 2023-02-08 19:01:44.110717 langchain-0.0.99rc0/langchain/chains/llm_math/prompt.py
+-rw-r--r--   0        0        0     2521 2023-03-01 03:50:13.738266 langchain-0.0.99rc0/langchain/chains/llm_requests.py
+-rw-r--r--   0        0        0    19407 2023-02-27 06:10:52.988271 langchain-0.0.99rc0/langchain/chains/loading.py
+-rw-r--r--   0        0        0     2512 2023-02-08 19:01:44.110932 langchain-0.0.99rc0/langchain/chains/mapreduce.py
+-rw-r--r--   0        0        0     2602 2023-02-08 19:01:44.110995 langchain-0.0.99rc0/langchain/chains/moderation.py
+-rw-r--r--   0        0        0       96 2023-02-08 19:01:44.111095 langchain-0.0.99rc0/langchain/chains/natbot/__init__.py
+-rw-r--r--   0        0        0     3026 2023-02-08 19:01:44.111183 langchain-0.0.99rc0/langchain/chains/natbot/base.py
+-rw-r--r--   0        0        0    15382 2023-02-08 19:01:44.111266 langchain-0.0.99rc0/langchain/chains/natbot/crawler.py
+-rw-r--r--   0        0        0     4984 2023-02-08 19:01:44.111338 langchain-0.0.99rc0/langchain/chains/natbot/prompt.py
+-rw-r--r--   0        0        0       94 2023-02-08 19:01:44.111415 langchain-0.0.99rc0/langchain/chains/pal/__init__.py
+-rw-r--r--   0        0        0     2906 2023-02-08 19:01:44.111467 langchain-0.0.99rc0/langchain/chains/pal/base.py
+-rw-r--r--   0        0        0     2645 2023-02-08 19:01:44.111517 langchain-0.0.99rc0/langchain/chains/pal/colored_object_prompt.py
+-rw-r--r--   0        0        0     4301 2023-02-08 19:01:44.111575 langchain-0.0.99rc0/langchain/chains/pal/math_prompt.py
+-rw-r--r--   0        0        0      173 2023-02-08 19:01:44.111656 langchain-0.0.99rc0/langchain/chains/qa_with_sources/__init__.py
+-rw-r--r--   0        0        0     4524 2023-02-08 19:01:44.111749 langchain-0.0.99rc0/langchain/chains/qa_with_sources/base.py
+-rw-r--r--   0        0        0     6314 2023-02-08 19:01:44.111808 langchain-0.0.99rc0/langchain/chains/qa_with_sources/loading.py
+-rw-r--r--   0        0        0     6966 2023-02-08 19:01:44.111986 langchain-0.0.99rc0/langchain/chains/qa_with_sources/map_reduce_prompt.py
+-rw-r--r--   0        0        0     1313 2023-02-08 19:01:44.112036 langchain-0.0.99rc0/langchain/chains/qa_with_sources/refine_prompts.py
+-rw-r--r--   0        0        0     6576 2023-02-08 19:01:44.112091 langchain-0.0.99rc0/langchain/chains/qa_with_sources/stuff_prompt.py
+-rw-r--r--   0        0        0     2117 2023-02-08 19:01:44.112153 langchain-0.0.99rc0/langchain/chains/qa_with_sources/vector_db.py
+-rw-r--r--   0        0        0     7085 2023-02-27 06:10:52.988536 langchain-0.0.99rc0/langchain/chains/question_answering/__init__.py
+-rw-r--r--   0        0        0     6635 2023-02-08 19:01:44.112316 langchain-0.0.99rc0/langchain/chains/question_answering/map_reduce_prompt.py
+-rw-r--r--   0        0        0     1608 2023-02-08 19:01:44.112367 langchain-0.0.99rc0/langchain/chains/question_answering/map_rerank_prompt.py
+-rw-r--r--   0        0        0     1089 2023-02-08 19:01:44.112416 langchain-0.0.99rc0/langchain/chains/question_answering/refine_prompts.py
+-rw-r--r--   0        0        0      394 2023-02-08 19:01:44.112461 langchain-0.0.99rc0/langchain/chains/question_answering/stuff_prompt.py
+-rw-r--r--   0        0        0     4712 2023-02-08 19:01:44.112516 langchain-0.0.99rc0/langchain/chains/sequential.py
+-rw-r--r--   0        0        0       47 2023-02-08 19:01:44.112579 langchain-0.0.99rc0/langchain/chains/sql_database/__init__.py
+-rw-r--r--   0        0        0     6408 2023-02-08 19:01:44.112689 langchain-0.0.99rc0/langchain/chains/sql_database/base.py
+-rw-r--r--   0        0        0     1629 2023-02-27 06:10:52.988773 langchain-0.0.99rc0/langchain/chains/sql_database/prompt.py
+-rw-r--r--   0        0        0     5036 2023-02-10 16:03:25.807176 langchain-0.0.99rc0/langchain/chains/summarize/__init__.py
+-rw-r--r--   0        0        0      233 2023-02-08 19:01:44.112966 langchain-0.0.99rc0/langchain/chains/summarize/map_reduce_prompt.py
+-rw-r--r--   0        0        0      803 2023-02-08 19:01:44.113015 langchain-0.0.99rc0/langchain/chains/summarize/refine_prompts.py
+-rw-r--r--   0        0        0      233 2023-02-08 19:01:44.113081 langchain-0.0.99rc0/langchain/chains/summarize/stuff_prompt.py
+-rw-r--r--   0        0        0     1018 2023-02-08 19:01:44.113131 langchain-0.0.99rc0/langchain/chains/transform.py
+-rw-r--r--   0        0        0       62 2023-02-08 19:01:44.113196 langchain-0.0.99rc0/langchain/chains/vector_db_qa/__init__.py
+-rw-r--r--   0        0        0     6044 2023-02-27 06:10:52.989024 langchain-0.0.99rc0/langchain/chains/vector_db_qa/base.py
+-rw-r--r--   0        0        0      394 2023-02-21 06:58:15.282552 langchain-0.0.99rc0/langchain/chains/vector_db_qa/prompt.py
+-rw-r--r--   0        0        0        0 2023-03-01 22:14:26.353541 langchain-0.0.99rc0/langchain/chat/__init__.py
+-rw-r--r--   0        0        0     1100 2023-03-02 01:38:20.718625 langchain-0.0.99rc0/langchain/chat/base.py
+-rw-r--r--   0        0        0     3189 2023-03-02 01:43:46.880452 langchain-0.0.99rc0/langchain/chat/chat_vector_db.py
+-rw-r--r--   0        0        0     2032 2023-03-02 01:43:23.728628 langchain-0.0.99rc0/langchain/chat/conversation.py
+-rw-r--r--   0        0        0     1495 2023-03-02 01:43:55.699713 langchain-0.0.99rc0/langchain/chat/memory.py
+-rw-r--r--   0        0        0     2830 2023-03-02 01:43:23.726794 langchain-0.0.99rc0/langchain/chat/question_answering.py
+-rw-r--r--   0        0        0     3995 2023-03-02 01:38:20.719456 langchain-0.0.99rc0/langchain/chat/vector_db_qa.py
+-rw-r--r--   0        0        0        0 2023-03-01 21:35:39.441162 langchain-0.0.99rc0/langchain/chat_models/__init__.py
+-rw-r--r--   0        0        0     1331 2023-03-02 01:44:14.967001 langchain-0.0.99rc0/langchain/chat_models/base.py
+-rw-r--r--   0        0        0     5709 2023-03-02 01:38:20.723206 langchain-0.0.99rc0/langchain/chat_models/openai.py
+-rw-r--r--   0        0        0      689 2023-02-08 19:01:44.113337 langchain-0.0.99rc0/langchain/docker-compose.yaml
+-rw-r--r--   0        0        0      190 2023-02-08 19:01:44.113406 langchain-0.0.99rc0/langchain/docstore/__init__.py
+-rw-r--r--   0        0        0      700 2023-02-08 19:01:44.113453 langchain-0.0.99rc0/langchain/docstore/base.py
+-rw-r--r--   0        0        0     1262 2023-02-08 19:01:44.113497 langchain-0.0.99rc0/langchain/docstore/document.py
+-rw-r--r--   0        0        0      972 2023-02-08 19:01:44.113551 langchain-0.0.99rc0/langchain/docstore/in_memory.py
+-rw-r--r--   0        0        0     1377 2023-02-08 19:01:44.113602 langchain-0.0.99rc0/langchain/docstore/wikipedia.py
+-rw-r--r--   0        0        0     3601 2023-02-28 06:07:09.769619 langchain-0.0.99rc0/langchain/document_loaders/__init__.py
+-rw-r--r--   0        0        0     1247 2023-02-11 06:56:05.009475 langchain-0.0.99rc0/langchain/document_loaders/airbyte_json.py
+-rw-r--r--   0        0        0      584 2023-02-27 06:10:52.989583 langchain-0.0.99rc0/langchain/document_loaders/azlyrics.py
+-rw-r--r--   0        0        0      794 2023-02-08 19:01:44.113722 langchain-0.0.99rc0/langchain/document_loaders/base.py
+-rw-r--r--   0        0        0      562 2023-02-27 06:10:52.989790 langchain-0.0.99rc0/langchain/document_loaders/college_confidential.py
+-rw-r--r--   0        0        0     1097 2023-02-27 22:44:33.825782 langchain-0.0.99rc0/langchain/document_loaders/conllu.py
+-rw-r--r--   0        0        0     1809 2023-02-27 06:10:52.990221 langchain-0.0.99rc0/langchain/document_loaders/directory.py
+-rw-r--r--   0        0        0      429 2023-02-14 04:32:19.327699 langchain-0.0.99rc0/langchain/document_loaders/docx.py
+-rw-r--r--   0        0        0      415 2023-02-14 04:32:19.328119 langchain-0.0.99rc0/langchain/document_loaders/email.py
+-rw-r--r--   0        0        0     2550 2023-02-27 06:10:52.990383 langchain-0.0.99rc0/langchain/document_loaders/evernote.py
+-rw-r--r--   0        0        0     1816 2023-02-27 06:10:52.990549 langchain-0.0.99rc0/langchain/document_loaders/facebook_chat.py
+-rw-r--r--   0        0        0     1215 2023-02-08 19:01:44.113912 langchain-0.0.99rc0/langchain/document_loaders/gcs_directory.py
+-rw-r--r--   0        0        0     1509 2023-02-08 19:01:44.113970 langchain-0.0.99rc0/langchain/document_loaders/gcs_file.py
+-rw-r--r--   0        0        0     2066 2023-02-27 06:10:52.990735 langchain-0.0.99rc0/langchain/document_loaders/gitbook.py
+-rw-r--r--   0        0        0     5195 2023-02-27 06:10:52.990934 langchain-0.0.99rc0/langchain/document_loaders/googledrive.py
+-rw-r--r--   0        0        0      979 2023-02-08 20:56:32.962972 langchain-0.0.99rc0/langchain/document_loaders/gutenberg.py
+-rw-r--r--   0        0        0     2062 2023-02-27 06:10:52.991090 langchain-0.0.99rc0/langchain/document_loaders/hn.py
+-rw-r--r--   0        0        0      408 2023-02-14 04:32:19.328368 langchain-0.0.99rc0/langchain/document_loaders/html.py
+-rw-r--r--   0        0        0     6775 2023-02-28 06:07:09.769713 langchain-0.0.99rc0/langchain/document_loaders/ifixit.py
+-rw-r--r--   0        0        0      438 2023-02-27 22:44:33.825898 langchain-0.0.99rc0/langchain/document_loaders/image.py
+-rw-r--r--   0        0        0      511 2023-02-27 06:10:52.991224 langchain-0.0.99rc0/langchain/document_loaders/imsdb.py
+-rw-r--r--   0        0        0     3490 2023-02-27 06:10:52.991534 langchain-0.0.99rc0/langchain/document_loaders/notebook.py
+-rw-r--r--   0        0        0      758 2023-02-08 19:01:44.114121 langchain-0.0.99rc0/langchain/document_loaders/notion.py
+-rw-r--r--   0        0        0      756 2023-02-08 19:01:44.114172 langchain-0.0.99rc0/langchain/document_loaders/obsidian.py
+-rw-r--r--   0        0        0      903 2023-02-27 06:10:52.991813 langchain-0.0.99rc0/langchain/document_loaders/online_pdf.py
+-rw-r--r--   0        0        0     1152 2023-02-27 06:10:52.991964 langchain-0.0.99rc0/langchain/document_loaders/paged_pdf.py
+-rw-r--r--   0        0        0     1257 2023-02-14 04:32:19.328774 langchain-0.0.99rc0/langchain/document_loaders/pdf.py
+-rw-r--r--   0        0        0     1668 2023-02-27 06:10:52.992104 langchain-0.0.99rc0/langchain/document_loaders/powerpoint.py
+-rw-r--r--   0        0        0     1194 2023-02-09 15:53:14.540224 langchain-0.0.99rc0/langchain/document_loaders/readthedocs.py
+-rw-r--r--   0        0        0      744 2023-02-08 19:01:44.114346 langchain-0.0.99rc0/langchain/document_loaders/roam.py
+-rw-r--r--   0        0        0     1083 2023-02-08 19:01:44.114393 langchain-0.0.99rc0/langchain/document_loaders/s3_directory.py
+-rw-r--r--   0        0        0     1109 2023-02-08 19:01:44.114439 langchain-0.0.99rc0/langchain/document_loaders/s3_file.py
+-rw-r--r--   0        0        0      872 2023-02-27 06:10:52.992539 langchain-0.0.99rc0/langchain/document_loaders/srt.py
+-rw-r--r--   0        0        0     1710 2023-02-27 06:10:52.992957 langchain-0.0.99rc0/langchain/document_loaders/telegram.py
+-rw-r--r--   0        0        0      580 2023-02-11 22:17:11.595214 langchain-0.0.99rc0/langchain/document_loaders/text.py
+-rw-r--r--   0        0        0     3114 2023-02-27 06:10:52.993191 langchain-0.0.99rc0/langchain/document_loaders/unstructured.py
+-rw-r--r--   0        0        0     1059 2023-02-10 18:19:18.391979 langchain-0.0.99rc0/langchain/document_loaders/url.py
+-rw-r--r--   0        0        0     1017 2023-02-27 06:10:52.993406 langchain-0.0.99rc0/langchain/document_loaders/web_base.py
+-rw-r--r--   0        0        0     1666 2023-02-27 06:10:52.993579 langchain-0.0.99rc0/langchain/document_loaders/word_document.py
+-rw-r--r--   0        0        0     2682 2023-02-27 06:10:52.993805 langchain-0.0.99rc0/langchain/document_loaders/youtube.py
+-rw-r--r--   0        0        0     1822 2023-02-27 06:10:52.994033 langchain-0.0.99rc0/langchain/embeddings/__init__.py
+-rw-r--r--   0        0        0      395 2023-02-08 19:01:44.114648 langchain-0.0.99rc0/langchain/embeddings/base.py
+-rw-r--r--   0        0        0     2489 2023-02-27 06:10:52.994244 langchain-0.0.99rc0/langchain/embeddings/cohere.py
+-rw-r--r--   0        0        0     4545 2023-02-27 06:10:52.994385 langchain-0.0.99rc0/langchain/embeddings/huggingface.py
+-rw-r--r--   0        0        0     3752 2023-02-08 19:01:44.114823 langchain-0.0.99rc0/langchain/embeddings/huggingface_hub.py
+-rw-r--r--   0        0        0     6452 2023-02-27 06:10:52.994617 langchain-0.0.99rc0/langchain/embeddings/openai.py
+-rw-r--r--   0        0        0     3844 2023-02-27 06:10:52.996371 langchain-0.0.99rc0/langchain/embeddings/self_hosted.py
+-rw-r--r--   0        0        0     6692 2023-02-27 06:10:52.996546 langchain-0.0.99rc0/langchain/embeddings/self_hosted_hugging_face.py
+-rw-r--r--   0        0        0     2182 2023-02-08 19:01:44.114907 langchain-0.0.99rc0/langchain/embeddings/tensorflow_hub.py
+-rw-r--r--   0        0        0       51 2023-02-08 19:01:44.114974 langchain-0.0.99rc0/langchain/evaluation/__init__.py
+-rw-r--r--   0        0        0      251 2023-02-08 19:01:44.115044 langchain-0.0.99rc0/langchain/evaluation/qa/__init__.py
+-rw-r--r--   0        0        0     1940 2023-02-27 06:10:52.996708 langchain-0.0.99rc0/langchain/evaluation/qa/eval_chain.py
+-rw-r--r--   0        0        0      623 2023-02-08 19:01:44.115151 langchain-0.0.99rc0/langchain/evaluation/qa/eval_prompt.py
+-rw-r--r--   0        0        0      583 2023-02-08 19:01:44.115190 langchain-0.0.99rc0/langchain/evaluation/qa/generate_chain.py
+-rw-r--r--   0        0        0      724 2023-02-08 19:01:44.115236 langchain-0.0.99rc0/langchain/evaluation/qa/generate_prompt.py
+-rw-r--r--   0        0        0      749 2023-02-08 19:01:44.115280 langchain-0.0.99rc0/langchain/example_generator.py
+-rw-r--r--   0        0        0      981 2023-02-08 19:01:44.115323 langchain-0.0.99rc0/langchain/formatting.py
+-rw-r--r--   0        0        0      128 2023-02-14 04:32:19.329530 langchain-0.0.99rc0/langchain/graphs/__init__.py
+-rw-r--r--   0        0        0     3439 2023-02-27 06:10:52.996972 langchain-0.0.99rc0/langchain/graphs/networkx_graph.py
+-rw-r--r--   0        0        0      203 2023-02-27 22:44:33.826038 langchain-0.0.99rc0/langchain/indexes/__init__.py
+-rw-r--r--   0        0        0     1029 2023-02-14 04:32:19.330286 langchain-0.0.99rc0/langchain/indexes/graph.py
+-rw-r--r--   0        0        0       49 2023-02-14 04:32:19.330424 langchain-0.0.99rc0/langchain/indexes/prompts/__init__.py
+-rw-r--r--   0        0        0     1947 2023-02-14 04:32:19.330744 langchain-0.0.99rc0/langchain/indexes/prompts/entity_extraction.py
+-rw-r--r--   0        0        0     1152 2023-02-14 04:32:19.330951 langchain-0.0.99rc0/langchain/indexes/prompts/entity_summarization.py
+-rw-r--r--   0        0        0     1584 2023-02-14 04:32:19.331096 langchain-0.0.99rc0/langchain/indexes/prompts/knowledge_triplet_extraction.py
+-rw-r--r--   0        0        0     2606 2023-02-27 22:44:33.826136 langchain-0.0.99rc0/langchain/indexes/vectorstore.py
+-rw-r--r--   0        0        0     1092 2023-02-08 19:01:44.115379 langchain-0.0.99rc0/langchain/input.py
+-rw-r--r--   0        0        0     2356 2023-03-01 20:14:47.144124 langchain-0.0.99rc0/langchain/llms/__init__.py
+-rw-r--r--   0        0        0     4815 2023-02-27 06:10:52.997490 langchain-0.0.99rc0/langchain/llms/ai21.py
+-rw-r--r--   0        0        0     9259 2023-02-27 06:10:52.997568 langchain-0.0.99rc0/langchain/llms/aleph_alpha.py
+-rw-r--r--   0        0        0     6417 2023-02-27 06:10:52.997889 langchain-0.0.99rc0/langchain/llms/anthropic.py
+-rw-r--r--   0        0        0     4152 2023-02-27 22:44:33.826283 langchain-0.0.99rc0/langchain/llms/bananadev.py
+-rw-r--r--   0        0        0    13034 2023-02-27 06:10:52.998330 langchain-0.0.99rc0/langchain/llms/base.py
+-rw-r--r--   0        0        0     3628 2023-02-27 06:10:52.998487 langchain-0.0.99rc0/langchain/llms/cerebriumai.py
+-rw-r--r--   0        0        0     4279 2023-02-27 06:10:52.998707 langchain-0.0.99rc0/langchain/llms/cohere.py
+-rw-r--r--   0        0        0     3066 2023-02-27 06:10:52.998948 langchain-0.0.99rc0/langchain/llms/deepinfra.py
+-rw-r--r--   0        0        0      717 2023-02-11 23:15:01.625878 langchain-0.0.99rc0/langchain/llms/fake.py
+-rw-r--r--   0        0        0     3534 2023-02-27 06:10:52.999098 langchain-0.0.99rc0/langchain/llms/forefrontai.py
+-rw-r--r--   0        0        0     4967 2023-02-27 06:10:52.999224 langchain-0.0.99rc0/langchain/llms/gooseai.py
+-rw-r--r--   0        0        0     4940 2023-02-27 06:10:52.999455 langchain-0.0.99rc0/langchain/llms/huggingface_endpoint.py
+-rw-r--r--   0        0        0     4308 2023-02-27 06:10:52.999639 langchain-0.0.99rc0/langchain/llms/huggingface_hub.py
+-rw-r--r--   0        0        0     5760 2023-02-27 06:10:52.999886 langchain-0.0.99rc0/langchain/llms/huggingface_pipeline.py
+-rw-r--r--   0        0        0     1250 2023-02-08 19:01:44.115935 langchain-0.0.99rc0/langchain/llms/loading.py
+-rw-r--r--   0        0        0     1746 2023-02-08 19:01:44.115985 langchain-0.0.99rc0/langchain/llms/manifest.py
+-rw-r--r--   0        0        0     3085 2023-02-27 06:10:52.999984 langchain-0.0.99rc0/langchain/llms/modal.py
+-rw-r--r--   0        0        0     5010 2023-02-27 06:10:53.000114 langchain-0.0.99rc0/langchain/llms/nlpcloud.py
+-rw-r--r--   0        0        0    24158 2023-03-01 20:14:47.144575 langchain-0.0.99rc0/langchain/llms/openai.py
+-rw-r--r--   0        0        0     5082 2023-02-27 06:10:53.000513 langchain-0.0.99rc0/langchain/llms/petals.py
+-rw-r--r--   0        0        0     2787 2023-02-27 06:10:53.000608 langchain-0.0.99rc0/langchain/llms/promptlayer_openai.py
+-rw-r--r--   0        0        0     7533 2023-02-27 06:10:53.000791 langchain-0.0.99rc0/langchain/llms/self_hosted.py
+-rw-r--r--   0        0        0     7435 2023-02-27 06:10:53.000975 langchain-0.0.99rc0/langchain/llms/self_hosted_hugging_face.py
+-rw-r--r--   0        0        0     4418 2023-02-27 06:10:53.001084 langchain-0.0.99rc0/langchain/llms/stochasticai.py
+-rw-r--r--   0        0        0      259 2023-02-08 19:01:44.116162 langchain-0.0.99rc0/langchain/llms/utils.py
+-rw-r--r--   0        0        0     5015 2023-02-27 06:10:53.001299 langchain-0.0.99rc0/langchain/llms/writer.py
+-rw-r--r--   0        0        0        0 2023-03-01 21:24:48.689979 langchain-0.0.99rc0/langchain/memory/__init__.py
+-rw-r--r--   0        0        0      620 2023-03-02 01:40:56.772413 langchain-0.0.99rc0/langchain/memory/chat_memory.py
+-rw-r--r--   0        0        0      238 2023-03-02 01:40:45.454157 langchain-0.0.99rc0/langchain/memory/utils.py
+-rw-r--r--   0        0        0     3230 2023-02-08 19:01:44.116216 langchain-0.0.99rc0/langchain/model_laboratory.py
+-rw-r--r--   0        0        0      496 2023-02-08 19:01:44.116284 langchain-0.0.99rc0/langchain/prompts/__init__.py
+-rw-r--r--   0        0        0     7426 2023-03-01 18:24:28.323834 langchain-0.0.99rc0/langchain/prompts/base.py
+-rw-r--r--   0        0        0      429 2023-02-08 19:01:44.116420 langchain-0.0.99rc0/langchain/prompts/example_selector/__init__.py
+-rw-r--r--   0        0        0      526 2023-02-08 19:01:44.116475 langchain-0.0.99rc0/langchain/prompts/example_selector/base.py
+-rw-r--r--   0        0        0     2433 2023-02-27 06:10:53.001522 langchain-0.0.99rc0/langchain/prompts/example_selector/length_based.py
+-rw-r--r--   0        0        0     3733 2023-02-08 19:01:44.116605 langchain-0.0.99rc0/langchain/prompts/example_selector/ngram_overlap.py
+-rw-r--r--   0        0        0     6840 2023-02-27 06:10:53.001786 langchain-0.0.99rc0/langchain/prompts/example_selector/semantic_similarity.py
+-rw-r--r--   0        0        0     4399 2023-03-01 03:50:11.708446 langchain-0.0.99rc0/langchain/prompts/few_shot.py
+-rw-r--r--   0        0        0     5436 2023-03-01 03:50:11.708678 langchain-0.0.99rc0/langchain/prompts/few_shot_with_templates.py
+-rw-r--r--   0        0        0     5908 2023-02-27 06:10:53.002029 langchain-0.0.99rc0/langchain/prompts/loading.py
+-rw-r--r--   0        0        0     4240 2023-03-01 18:24:28.324108 langchain-0.0.99rc0/langchain/prompts/prompt.py
+-rw-r--r--   0        0        0        0 2023-02-08 19:01:44.116973 langchain-0.0.99rc0/langchain/py.typed
+-rw-r--r--   0        0        0      816 2023-03-01 04:38:31.717984 langchain-0.0.99rc0/langchain/python.py
+-rw-r--r--   0        0        0     2831 2023-03-01 03:50:13.738833 langchain-0.0.99rc0/langchain/requests.py
+-rw-r--r--   0        0        0     1886 2023-03-02 01:38:20.343529 langchain-0.0.99rc0/langchain/schema.py
+-rw-r--r--   0        0        0      119 2023-02-27 06:10:53.006075 langchain-0.0.99rc0/langchain/serpapi.py
+-rw-r--r--   0        0        0      401 2023-02-08 19:01:44.117270 langchain-0.0.99rc0/langchain/server.py
+-rw-r--r--   0        0        0     8647 2023-03-01 03:50:13.738960 langchain-0.0.99rc0/langchain/sql_database.py
+-rw-r--r--   0        0        0    12904 2023-02-27 06:10:53.007177 langchain-0.0.99rc0/langchain/text_splitter.py
+-rw-r--r--   0        0        0      166 2023-02-27 06:10:53.007552 langchain-0.0.99rc0/langchain/tools/__init__.py
+-rw-r--r--   0        0        0     3985 2023-03-01 03:50:13.740690 langchain-0.0.99rc0/langchain/tools/base.py
+-rw-r--r--   0        0        0       31 2023-02-27 06:10:53.007931 langchain-0.0.99rc0/langchain/tools/bing_search/__init__.py
+-rw-r--r--   0        0        0      773 2023-02-27 06:10:53.012031 langchain-0.0.99rc0/langchain/tools/bing_search/tool.py
+-rw-r--r--   0        0        0       33 2023-02-27 06:10:53.012169 langchain-0.0.99rc0/langchain/tools/google_search/__init__.py
+-rw-r--r--   0        0        0     1558 2023-02-27 06:10:53.012480 langchain-0.0.99rc0/langchain/tools/google_search/tool.py
+-rw-r--r--   0        0        0     2213 2023-02-28 23:09:59.374168 langchain-0.0.99rc0/langchain/tools/ifttt.py
+-rw-r--r--   0        0        0       43 2023-02-27 06:10:53.013076 langchain-0.0.99rc0/langchain/tools/interaction/__init__.py
+-rw-r--r--   0        0        0      681 2023-02-27 06:10:53.013311 langchain-0.0.99rc0/langchain/tools/interaction/tool.py
+-rw-r--r--   0        0        0       46 2023-03-01 03:50:13.740761 langchain-0.0.99rc0/langchain/tools/json/__init__.py
+-rw-r--r--   0        0        0     3604 2023-03-01 03:50:13.740940 langchain-0.0.99rc0/langchain/tools/json/tool.py
+-rw-r--r--   0        0        0        0 2023-03-01 03:50:13.740967 langchain-0.0.99rc0/langchain/tools/python/__init__.py
+-rw-r--r--   0        0        0     2830 2023-03-01 06:26:30.794085 langchain-0.0.99rc0/langchain/tools/python/tool.py
+-rw-r--r--   0        0        0       52 2023-03-01 03:50:13.741253 langchain-0.0.99rc0/langchain/tools/requests/__init__.py
+-rw-r--r--   0        0        0     4961 2023-03-01 03:50:13.741454 langchain-0.0.99rc0/langchain/tools/requests/tool.py
+-rw-r--r--   0        0        0       49 2023-03-01 03:50:13.741606 langchain-0.0.99rc0/langchain/tools/sql_database/__init__.py
+-rw-r--r--   0        0        0      550 2023-03-01 03:50:13.741752 langchain-0.0.99rc0/langchain/tools/sql_database/prompt.py
+-rw-r--r--   0        0        0     4163 2023-03-01 03:50:13.741872 langchain-0.0.99rc0/langchain/tools/sql_database/tool.py
+-rw-r--r--   0        0        0       51 2023-03-01 03:50:13.742089 langchain-0.0.99rc0/langchain/tools/vectorstore/__init__.py
+-rw-r--r--   0        0        0     3082 2023-03-01 03:50:13.742406 langchain-0.0.99rc0/langchain/tools/vectorstore/tool.py
+-rw-r--r--   0        0        0       33 2023-02-27 06:10:53.013366 langchain-0.0.99rc0/langchain/tools/wolfram_alpha/__init__.py
+-rw-r--r--   0        0        0      891 2023-02-27 06:10:53.013615 langchain-0.0.99rc0/langchain/tools/wolfram_alpha/tool.py
+-rw-r--r--   0        0        0      793 2023-02-27 06:10:53.013895 langchain-0.0.99rc0/langchain/utilities/__init__.py
+-rw-r--r--   0        0        0     1135 2023-02-08 19:01:44.117575 langchain-0.0.99rc0/langchain/utilities/bash.py
+-rw-r--r--   0        0        0     3333 2023-02-08 19:01:44.117642 langchain-0.0.99rc0/langchain/utilities/bing_search.py
+-rw-r--r--   0        0        0     4834 2023-02-27 06:10:53.014142 langchain-0.0.99rc0/langchain/utilities/google_search.py
+-rw-r--r--   0        0        0     3309 2023-02-27 06:10:53.014412 langchain-0.0.99rc0/langchain/utilities/google_serper.py
+-rw-r--r--   0        0        0     1582 2023-02-27 06:10:53.014509 langchain-0.0.99rc0/langchain/utilities/loading.py
+-rw-r--r--   0        0        0    11962 2023-02-27 06:10:53.014755 langchain-0.0.99rc0/langchain/utilities/searx_search.py
+-rw-r--r--   0        0        0     5154 2023-02-27 06:10:53.015002 langchain-0.0.99rc0/langchain/utilities/serpapi.py
+-rw-r--r--   0        0        0     1989 2023-02-27 06:10:53.015219 langchain-0.0.99rc0/langchain/utilities/wolfram_alpha.py
+-rw-r--r--   0        0        0      689 2023-02-08 19:01:44.117885 langchain-0.0.99rc0/langchain/utils.py
+-rw-r--r--   0        0        0      863 2023-02-27 22:44:33.826409 langchain-0.0.99rc0/langchain/vectorstores/__init__.py
+-rw-r--r--   0        0        0    11988 2023-03-01 18:24:28.324520 langchain-0.0.99rc0/langchain/vectorstores/atlas.py
+-rw-r--r--   0        0        0     4159 2023-02-27 06:13:27.028739 langchain-0.0.99rc0/langchain/vectorstores/base.py
+-rw-r--r--   0        0        0     8270 2023-03-01 18:24:28.325242 langchain-0.0.99rc0/langchain/vectorstores/chroma.py
+-rw-r--r--   0        0        0     7676 2023-03-01 18:24:28.326282 langchain-0.0.99rc0/langchain/vectorstores/deeplake.py
+-rw-r--r--   0        0        0     6859 2023-02-27 06:10:53.016197 langchain-0.0.99rc0/langchain/vectorstores/elastic_vector_search.py
+-rw-r--r--   0        0        0    11101 2023-03-01 18:24:28.326951 langchain-0.0.99rc0/langchain/vectorstores/faiss.py
+-rw-r--r--   0        0        0    16140 2023-03-01 18:24:28.327699 langchain-0.0.99rc0/langchain/vectorstores/milvus.py
+-rw-r--r--   0        0        0    13583 2023-02-27 06:10:53.016807 langchain-0.0.99rc0/langchain/vectorstores/opensearch_vector_search.py
+-rw-r--r--   0        0        0     8551 2023-03-01 18:24:28.328161 langchain-0.0.99rc0/langchain/vectorstores/pinecone.py
+-rw-r--r--   0        0        0     8182 2023-03-01 18:24:28.329002 langchain-0.0.99rc0/langchain/vectorstores/qdrant.py
+-rw-r--r--   0        0        0     1227 2023-02-08 19:01:44.118493 langchain-0.0.99rc0/langchain/vectorstores/utils.py
+-rw-r--r--   0        0        0     3433 2023-03-01 18:24:28.329805 langchain-0.0.99rc0/langchain/vectorstores/weaviate.py
+-rw-r--r--   0        0        0     3872 2023-03-02 02:03:47.274663 langchain-0.0.99rc0/pyproject.toml
+-rw-r--r--   0        0        0     7636 1970-01-01 00:00:00.000000 langchain-0.0.99rc0/PKG-INFO
```

### Comparing `langchain-0.0.99/LICENSE` & `langchain-0.0.99rc0/LICENSE`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/README.md` & `langchain-0.0.99rc0/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -38,15 +38,15 @@
 ## 📖 Documentation
 
 Please see [here](https://langchain.readthedocs.io/en/latest/?) for full documentation on:
 
 - Getting started (installation, setting up the environment, simple examples)
 - How-To examples (demos, integrations, helper functions)
 - Reference (full API docs)
-- Resources (high-level explanation of core concepts)
+  Resources (high-level explanation of core concepts)
 
 ## 🚀 What can this help with?
 
 There are six main areas that LangChain is designed to help with.
 These are, in increasing order of complexity:
 
 **📃 LLMs and Prompts:**
```

### Comparing `langchain-0.0.99/langchain/__init__.py` & `langchain-0.0.99rc0/langchain/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/__init__.py` & `langchain-0.0.99rc0/langchain/agents/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent.py` & `langchain-0.0.99rc0/langchain/agents/agent.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/__init__.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/csv/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/csv/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/json/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/json/prompt.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/json/toolkit.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/json/toolkit.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/openapi/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/openapi/prompt.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/openapi/toolkit.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/openapi/toolkit.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/pandas/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/pandas/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/python/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/python/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/python/prompt.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/python/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/sql/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/sql/prompt.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/prompt.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # flake8: noqa
 
 SQL_PREFIX = """You are an agent designed to interact with a SQL database.
 Given an input question, create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer.
-Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results.
+Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most {top_k} results using the LIMIT clause.
 You can order the results by a relevant column to return the most interesting examples in the database.
 Never query for all the columns from a specific table, only ask for a the few relevant columns given the question.
 You have access to tools for interacting with the database.
 Only use the below tools. Only use the information returned by the below tools to construct your final answer.
 You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.
 
 DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
```

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/sql/toolkit.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/sql/toolkit.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/base.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/prompt.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/agent_toolkits/vectorstore/toolkit.py` & `langchain-0.0.99rc0/langchain/agents/agent_toolkits/vectorstore/toolkit.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/conversational/base.py` & `langchain-0.0.99rc0/langchain/agents/conversational/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/conversational/prompt.py` & `langchain-0.0.99rc0/langchain/agents/conversational/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/initialize.py` & `langchain-0.0.99rc0/langchain/agents/initialize.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/load_tools.py` & `langchain-0.0.99rc0/langchain/agents/load_tools.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/loading.py` & `langchain-0.0.99rc0/langchain/agents/loading.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/mrkl/base.py` & `langchain-0.0.99rc0/langchain/agents/mrkl/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/mrkl/prompt.py` & `langchain-0.0.99rc0/langchain/agents/mrkl/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/react/base.py` & `langchain-0.0.99rc0/langchain/agents/react/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/react/textworld_prompt.py` & `langchain-0.0.99rc0/langchain/agents/react/textworld_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/react/wiki_prompt.py` & `langchain-0.0.99rc0/langchain/agents/react/wiki_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/self_ask_with_search/base.py` & `langchain-0.0.99rc0/langchain/agents/self_ask_with_search/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/self_ask_with_search/prompt.py` & `langchain-0.0.99rc0/langchain/agents/self_ask_with_search/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/agents/tools.py` & `langchain-0.0.99rc0/langchain/agents/tools.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/cache.py` & `langchain-0.0.99rc0/langchain/cache.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/__init__.py` & `langchain-0.0.99rc0/langchain/callbacks/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/base.py` & `langchain-0.0.99rc0/langchain/callbacks/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/openai_info.py` & `langchain-0.0.99rc0/langchain/callbacks/openai_info.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/shared.py` & `langchain-0.0.99rc0/langchain/callbacks/shared.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/stdout.py` & `langchain-0.0.99rc0/langchain/callbacks/stdout.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/streaming_stdout.py` & `langchain-0.0.99rc0/langchain/callbacks/streaming_stdout.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/streamlit.py` & `langchain-0.0.99rc0/langchain/callbacks/streamlit.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/tracers/base.py` & `langchain-0.0.99rc0/langchain/callbacks/tracers/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/tracers/langchain.py` & `langchain-0.0.99rc0/langchain/callbacks/tracers/langchain.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/callbacks/tracers/schemas.py` & `langchain-0.0.99rc0/langchain/callbacks/tracers/schemas.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/__init__.py` & `langchain-0.0.99rc0/langchain/chains/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,14 @@
 from langchain.chains.graph_qa.base import GraphQAChain
 from langchain.chains.hyde.base import HypotheticalDocumentEmbedder
 from langchain.chains.llm import LLMChain
 from langchain.chains.llm_bash.base import LLMBashChain
 from langchain.chains.llm_checker.base import LLMCheckerChain
 from langchain.chains.llm_math.base import LLMMathChain
 from langchain.chains.llm_requests import LLMRequestsChain
-from langchain.chains.llm_summarization_checker.base import LLMSummarizationCheckerChain
 from langchain.chains.loading import load_chain
 from langchain.chains.mapreduce import MapReduceChain
 from langchain.chains.moderation import OpenAIModerationChain
 from langchain.chains.pal.base import PALChain
 from langchain.chains.qa_with_sources.base import QAWithSourcesChain
 from langchain.chains.qa_with_sources.vector_db import VectorDBQAWithSourcesChain
 from langchain.chains.sequential import SequentialChain, SimpleSequentialChain
@@ -27,15 +26,14 @@
 from langchain.chains.vector_db_qa.base import VectorDBQA
 
 __all__ = [
     "ConversationChain",
     "LLMChain",
     "LLMBashChain",
     "LLMCheckerChain",
-    "LLMSummarizationCheckerChain",
     "LLMMathChain",
     "PALChain",
     "QAWithSourcesChain",
     "SQLDatabaseChain",
     "SequentialChain",
     "SimpleSequentialChain",
     "VectorDBQA",
```

### Comparing `langchain-0.0.99/langchain/chains/api/base.py` & `langchain-0.0.99rc0/langchain/chains/api/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/api/news_docs.py` & `langchain-0.0.99rc0/langchain/chains/api/news_docs.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/api/open_meteo_docs.py` & `langchain-0.0.99rc0/langchain/chains/api/open_meteo_docs.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/api/prompt.py` & `langchain-0.0.99rc0/langchain/chains/api/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/api/tmdb_docs.py` & `langchain-0.0.99rc0/langchain/chains/api/tmdb_docs.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/base.py` & `langchain-0.0.99rc0/langchain/chains/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/chat_vector_db/base.py` & `langchain-0.0.99rc0/langchain/chains/chat_vector_db/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/chat_vector_db/prompts.py` & `langchain-0.0.99rc0/langchain/chains/chat_vector_db/prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/combine_documents/base.py` & `langchain-0.0.99rc0/langchain/chains/combine_documents/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/combine_documents/map_reduce.py` & `langchain-0.0.99rc0/langchain/chains/combine_documents/map_reduce.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/combine_documents/map_rerank.py` & `langchain-0.0.99rc0/langchain/chains/combine_documents/map_rerank.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/combine_documents/refine.py` & `langchain-0.0.99rc0/langchain/chains/combine_documents/refine.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/combine_documents/stuff.py` & `langchain-0.0.99rc0/langchain/chains/combine_documents/stuff.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/constitutional_ai/base.py` & `langchain-0.0.99rc0/langchain/chains/constitutional_ai/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/constitutional_ai/prompts.py` & `langchain-0.0.99rc0/langchain/chains/constitutional_ai/prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/conversation/base.py` & `langchain-0.0.99rc0/langchain/chains/conversation/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/conversation/memory.py` & `langchain-0.0.99rc0/langchain/chains/conversation/memory.py`

 * *Files 11% similar despite different names*

```diff
@@ -13,15 +13,18 @@
 from langchain.chains.llm import LLMChain
 from langchain.graphs.networkx_graph import (
     NetworkxEntityGraph,
     get_entities,
     parse_triples,
 )
 from langchain.llms.base import BaseLLM
+from langchain.memory.chat_memory import ChatMemory
+from langchain.memory.utils import get_buffer_string
 from langchain.prompts.base import BasePromptTemplate
+from langchain.schema import ChatMessage
 
 
 def _get_prompt_input_key(inputs: Dict[str, Any], memory_variables: List[str]) -> str:
     # "stop" is a special key that can be passed as input but is not used to
     # format the prompt.
     prompt_input_keys = list(set(inputs).difference(memory_variables + ["stop"]))
     if len(prompt_input_keys) != 1:
@@ -69,119 +72,110 @@
 
     def clear(self) -> None:
         """Clear context from this session for every memory."""
         for memory in self.memories:
             memory.clear()
 
 
-class ConversationBufferMemory(Memory, BaseModel):
-    """Buffer for storing conversation memory."""
-
+class ChatMemoryMixin(Memory):
+    chat_memory: ChatMemory
     human_prefix: str = "Human"
     ai_prefix: str = "AI"
-    """Prefix to use for AI generated responses."""
-    buffer: str = ""
     output_key: Optional[str] = None
     input_key: Optional[str] = None
-    memory_key: str = "history"  #: :meta private:
-
-    @property
-    def memory_variables(self) -> List[str]:
-        """Will always return list of memory variables.
 
-        :meta private:
-        """
-        return [self.memory_key]
-
-    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
-        """Return history buffer."""
-        return {self.memory_key: self.buffer}
+    @root_validator(pre=True)
+    def add_chat_memory(cls, values: Dict) -> Dict:
+        """Add chat memory data structure."""
+        human_prefix = values.get("human_prefix", "Human")
+        ai_prefix = values.get("ai_prefix", "AI")
+        values["chat_memory"] = ChatMemory(
+            human_prefix=human_prefix, ai_prefix=ai_prefix
+        )
+        return values
 
     def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
         """Save context from this conversation to buffer."""
         if self.input_key is None:
             prompt_input_key = _get_prompt_input_key(inputs, self.memory_variables)
         else:
             prompt_input_key = self.input_key
         if self.output_key is None:
             if len(outputs) != 1:
                 raise ValueError(f"One output key expected, got {outputs.keys()}")
             output_key = list(outputs.keys())[0]
         else:
             output_key = self.output_key
-        human = f"{self.human_prefix}: " + inputs[prompt_input_key]
-        ai = f"{self.ai_prefix}: " + outputs[output_key]
-        self.buffer += "\n" + "\n".join([human, ai])
+        self.chat_memory.add_user_message(inputs[prompt_input_key])
+        self.chat_memory.add_ai_message(outputs[output_key])
 
     def clear(self) -> None:
         """Clear memory contents."""
-        self.buffer = ""
+        self.chat_memory.clear()
 
 
-class ConversationBufferWindowMemory(Memory, BaseModel):
+class ConversationBufferMemory(ChatMemoryMixin, BaseModel):
     """Buffer for storing conversation memory."""
 
-    human_prefix: str = "Human"
-    ai_prefix: str = "AI"
-    """Prefix to use for AI generated responses."""
-    buffer: List[str] = Field(default_factory=list)
     memory_key: str = "history"  #: :meta private:
-    output_key: Optional[str] = None
-    input_key: Optional[str] = None
-    k: int = 5
+
+    @property
+    def buffer(self) -> str:
+        """String buffer of memory."""
+        return get_buffer_string(self.chat_memory.messages)
 
     @property
     def memory_variables(self) -> List[str]:
         """Will always return list of memory variables.
 
         :meta private:
         """
         return [self.memory_key]
 
     def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
         """Return history buffer."""
-        return {self.memory_key: "\n".join(self.buffer[-self.k :])}
+        return {self.memory_key: self.buffer}
 
-    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
-        """Save context from this conversation to buffer."""
-        if self.input_key is None:
-            prompt_input_key = _get_prompt_input_key(inputs, self.memory_variables)
-        else:
-            prompt_input_key = self.input_key
-        if self.output_key is None:
-            if len(outputs) != 1:
-                raise ValueError(f"One output key expected, got {outputs.keys()}")
-            output_key = list(outputs.keys())[0]
-        else:
-            output_key = self.output_key
-        human = f"{self.human_prefix}: " + inputs[prompt_input_key]
-        ai = f"{self.ai_prefix}: " + outputs[output_key]
-        self.buffer.append("\n".join([human, ai]))
 
-    def clear(self) -> None:
-        """Clear memory contents."""
-        self.buffer = []
+class ConversationBufferWindowMemory(ChatMemoryMixin, BaseModel):
+    """Buffer for storing conversation memory."""
+
+    memory_key: str = "history"  #: :meta private:
+    k: int = 5
+
+    @property
+    def buffer(self) -> List[ChatMessage]:
+        """String buffer of memory."""
+        return self.chat_memory.messages
+
+    @property
+    def memory_variables(self) -> List[str]:
+        """Will always return list of memory variables.
+
+        :meta private:
+        """
+        return [self.memory_key]
+
+    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
+        """Return history buffer."""
+        return {self.memory_key: get_buffer_string(self.buffer[-self.k * 2 :])}
 
 
 # For legacy naming reasons
 ConversationalBufferWindowMemory = ConversationBufferWindowMemory
 
 
-class ConversationSummaryMemory(Memory, BaseModel):
+class ConversationSummaryMemory(ChatMemoryMixin, BaseModel):
     """Conversation summarizer to memory."""
 
     buffer: str = ""
-    human_prefix: str = "Human"
-    ai_prefix: str = "AI"
     """Prefix to use for AI generated responses."""
     llm: BaseLLM
     prompt: BasePromptTemplate = SUMMARY_PROMPT
     memory_key: str = "history"  #: :meta private:
-    output_key: Optional[str] = None
-    input_key: Optional[str] = None
 
     @property
     def memory_variables(self) -> List[str]:
         """Will always return list of memory variables.
 
         :meta private:
         """
@@ -201,53 +195,42 @@
                 "Got unexpected prompt input variables. The prompt expects "
                 f"{prompt_variables}, but it should have {expected_keys}."
             )
         return values
 
     def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
         """Save context from this conversation to buffer."""
-        if self.input_key is None:
-            prompt_input_key = _get_prompt_input_key(inputs, self.memory_variables)
-        else:
-            prompt_input_key = self.input_key
-        if self.output_key is None:
-            if len(outputs) != 1:
-                raise ValueError(f"One output key expected, got {outputs.keys()}")
-            output_key = list(outputs.keys())[0]
-        else:
-            output_key = self.output_key
-        human = f"{self.human_prefix}: {inputs[prompt_input_key]}"
-        ai = f"{self.ai_prefix}: {outputs[output_key]}"
-        new_lines = "\n".join([human, ai])
+        super().save_context(inputs, outputs)
+        new_lines = get_buffer_string(self.chat_memory.messages[-2:])
         chain = LLMChain(llm=self.llm, prompt=self.prompt)
         self.buffer = chain.predict(summary=self.buffer, new_lines=new_lines)
 
     def clear(self) -> None:
         """Clear memory contents."""
+        super().clear()
         self.buffer = ""
 
 
-class ConversationEntityMemory(Memory, BaseModel):
+class ConversationEntityMemory(ChatMemoryMixin, BaseModel):
     """Entity extractor & summarizer to memory."""
 
-    buffer: List[str] = []
-    human_prefix: str = "Human"
-    ai_prefix: str = "AI"
     """Prefix to use for AI generated responses."""
     llm: BaseLLM
     entity_extraction_prompt: BasePromptTemplate = ENTITY_EXTRACTION_PROMPT
     entity_summarization_prompt: BasePromptTemplate = ENTITY_SUMMARIZATION_PROMPT
-    output_key: Optional[str] = None
-    input_key: Optional[str] = None
     store: Dict[str, Optional[str]] = {}
     entity_cache: List[str] = []
     k: int = 3
     chat_history_key: str = "history"
 
     @property
+    def buffer(self) -> List[ChatMessage]:
+        return self.chat_memory.messages
+
+    @property
     def memory_variables(self) -> List[str]:
         """Will always return list of memory variables.
 
         :meta private:
         """
         return ["entities", self.chat_history_key]
 
@@ -255,163 +238,135 @@
         """Return history buffer."""
         chain = LLMChain(llm=self.llm, prompt=self.entity_extraction_prompt)
         if self.input_key is None:
             prompt_input_key = _get_prompt_input_key(inputs, self.memory_variables)
         else:
             prompt_input_key = self.input_key
         output = chain.predict(
-            history="\n".join(self.buffer[-self.k :]),
+            history=get_buffer_string(self.buffer[-self.k * 2 :]),
             input=inputs[prompt_input_key],
         )
         if output.strip() == "NONE":
             entities = []
         else:
             entities = [w.strip() for w in output.split(",")]
         entity_summaries = {}
         for entity in entities:
             entity_summaries[entity] = self.store.get(entity, "")
         self.entity_cache = entities
         return {
-            self.chat_history_key: "\n".join(self.buffer[-self.k :]),
+            self.chat_history_key: get_buffer_string(self.buffer[-self.k * 2 :]),
             "entities": entity_summaries,
         }
 
     def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
         """Save context from this conversation to buffer."""
+        super().save_context(inputs, outputs)
         if self.input_key is None:
             prompt_input_key = _get_prompt_input_key(inputs, self.memory_variables)
         else:
             prompt_input_key = self.input_key
-        if self.output_key is None:
-            if len(outputs) != 1:
-                raise ValueError(f"One output key expected, got {outputs.keys()}")
-            output_key = list(outputs.keys())[0]
-        else:
-            output_key = self.output_key
-        human = f"{self.human_prefix}: " + inputs[prompt_input_key]
-        ai = f"{self.ai_prefix}: " + outputs[output_key]
         for entity in self.entity_cache:
             chain = LLMChain(llm=self.llm, prompt=self.entity_summarization_prompt)
             # key value store for entity
             existing_summary = self.store.get(entity, "")
             output = chain.predict(
                 summary=existing_summary,
-                history="\n".join(self.buffer[-self.k :]),
+                history=get_buffer_string(self.buffer[-self.k * 2 :]),
                 input=inputs[prompt_input_key],
                 entity=entity,
             )
             self.store[entity] = output.strip()
-        new_lines = "\n".join([human, ai])
-        self.buffer.append(new_lines)
 
     def clear(self) -> None:
         """Clear memory contents."""
-        self.buffer = []
+        self.chat_memory.clear()
         self.store = {}
 
 
-class ConversationSummaryBufferMemory(Memory, BaseModel):
+class ConversationSummaryBufferMemory(ChatMemoryMixin, BaseModel):
     """Buffer with summarizer for storing conversation memory."""
 
-    buffer: List[str] = Field(default_factory=list)
     max_token_limit: int = 2000
     moving_summary_buffer: str = ""
     llm: BaseLLM
     prompt: BasePromptTemplate = SUMMARY_PROMPT
     memory_key: str = "history"
-    human_prefix: str = "Human"
-    ai_prefix: str = "AI"
-    """Prefix to use for AI generated responses."""
-    output_key: Optional[str] = None
-    input_key: Optional[str] = None
+
+    @property
+    def buffer(self) -> List[ChatMessage]:
+        return self.chat_memory.messages
 
     @property
     def memory_variables(self) -> List[str]:
         """Will always return list of memory variables.
 
         :meta private:
         """
         return [self.memory_key]
 
     def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
         """Return history buffer."""
         if self.moving_summary_buffer == "":
-            return {self.memory_key: "\n".join(self.buffer)}
-        memory_val = self.moving_summary_buffer + "\n" + "\n".join(self.buffer)
+            return {self.memory_key: get_buffer_string(self.buffer)}
+        memory_val = self.moving_summary_buffer + "\n" + get_buffer_string(self.buffer)
         return {self.memory_key: memory_val}
 
     @root_validator()
     def validate_prompt_input_variables(cls, values: Dict) -> Dict:
         """Validate that prompt input variables are consistent."""
         prompt_variables = values["prompt"].input_variables
         expected_keys = {"summary", "new_lines"}
         if expected_keys != set(prompt_variables):
             raise ValueError(
                 "Got unexpected prompt input variables. The prompt expects "
                 f"{prompt_variables}, but it should have {expected_keys}."
             )
         return values
 
-    def get_num_tokens_list(self, arr: List[str]) -> List[int]:
+    def get_num_tokens_list(self, arr: List[ChatMessage]) -> List[int]:
         """Get list of number of tokens in each string in the input array."""
-        return [self.llm.get_num_tokens(x) for x in arr]
+        return [self.llm.get_num_tokens(get_buffer_string([x])) for x in arr]
 
     def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
         """Save context from this conversation to buffer."""
-        if self.input_key is None:
-            prompt_input_key = _get_prompt_input_key(inputs, self.memory_variables)
-        else:
-            prompt_input_key = self.input_key
-        if self.output_key is None:
-            if len(outputs) != 1:
-                raise ValueError(f"One output key expected, got {outputs.keys()}")
-            output_key = list(outputs.keys())[0]
-        else:
-            output_key = self.output_key
-        human = f"{self.human_prefix}: {inputs[prompt_input_key]}"
-        ai = f"{self.ai_prefix}: {outputs[output_key]}"
-        new_lines = "\n".join([human, ai])
-        self.buffer.append(new_lines)
+        super().save_context(inputs, outputs)
         # Prune buffer if it exceeds max token limit
-        curr_buffer_length = sum(self.get_num_tokens_list(self.buffer))
+        buffer = self.chat_memory.messages
+        curr_buffer_length = sum(self.get_num_tokens_list(buffer))
         if curr_buffer_length > self.max_token_limit:
             pruned_memory = []
             while curr_buffer_length > self.max_token_limit:
-                pruned_memory.append(self.buffer.pop(0))
-                curr_buffer_length = sum(self.get_num_tokens_list(self.buffer))
+                pruned_memory.append(buffer.pop(0))
+                curr_buffer_length = sum(self.get_num_tokens_list(buffer))
             chain = LLMChain(llm=self.llm, prompt=self.prompt)
             self.moving_summary_buffer = chain.predict(
-                summary=self.moving_summary_buffer, new_lines=("\n".join(pruned_memory))
+                summary=self.moving_summary_buffer,
+                new_lines=(get_buffer_string(pruned_memory)),
             )
 
     def clear(self) -> None:
         """Clear memory contents."""
-        self.buffer = []
+        super().clear()
         self.moving_summary_buffer = ""
 
 
-class ConversationKGMemory(Memory, BaseModel):
+class ConversationKGMemory(ChatMemoryMixin, BaseModel):
     """Knowledge graph memory for storing conversation memory.
 
     Integrates with external knowledge graph to store and retrieve
     information about knowledge triples in the conversation.
     """
 
     k: int = 2
-    buffer: List[str] = Field(default_factory=list)
     kg: NetworkxEntityGraph = Field(default_factory=NetworkxEntityGraph)
     knowledge_extraction_prompt: BasePromptTemplate = KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT
     entity_extraction_prompt: BasePromptTemplate = ENTITY_EXTRACTION_PROMPT
     llm: BaseLLM
     """Number of previous utterances to include in the context."""
-    human_prefix: str = "Human"
-    ai_prefix: str = "AI"
-    """Prefix to use for AI generated responses."""
-    output_key: Optional[str] = None
-    input_key: Optional[str] = None
     memory_key: str = "history"  #: :meta private:
 
     def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
         """Return history buffer."""
         entities = self._get_current_entities(inputs)
         summaries = {}
         for entity in entities:
@@ -450,38 +405,34 @@
         return self.output_key
 
     def _get_current_entities(self, inputs: Dict[str, Any]) -> List[str]:
         """Get the current entities in the conversation."""
         prompt_input_key = self._get_prompt_input_key(inputs)
         chain = LLMChain(llm=self.llm, prompt=self.entity_extraction_prompt)
         output = chain.predict(
-            history="\n".join(self.buffer[-self.k :]),
+            history=get_buffer_string(self.chat_memory.messages[-self.k :]),
             input=inputs[prompt_input_key],
         )
         return get_entities(output)
 
     def _get_and_update_kg(self, inputs: Dict[str, Any]) -> None:
         """Get and update knowledge graph from the conversation history."""
         chain = LLMChain(llm=self.llm, prompt=self.knowledge_extraction_prompt)
         prompt_input_key = self._get_prompt_input_key(inputs)
         output = chain.predict(
-            history="\n".join(self.buffer[-self.k :]),
+            history=get_buffer_string(self.chat_memory.messages[-self.k :]),
             input=inputs[prompt_input_key],
             verbose=True,
         )
         knowledge = parse_triples(output)
         for triple in knowledge:
             self.kg.add_triple(triple)
 
     def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
         """Save context from this conversation to buffer."""
+        super().save_context(inputs, outputs)
         self._get_and_update_kg(inputs)
-        prompt_input_key = self._get_prompt_input_key(inputs)
-        output_key = self._get_prompt_output_key(outputs)
-        human = f"{self.human_prefix}: {inputs[prompt_input_key]}"
-        ai = f"{self.ai_prefix}: {outputs[output_key]}"
-        new_lines = "\n".join([human.strip(), ai.strip()])
-        self.buffer.append(new_lines)
 
     def clear(self) -> None:
         """Clear memory contents."""
-        return self.kg.clear()
+        super().clear()
+        self.kg.clear()
```

### Comparing `langchain-0.0.99/langchain/chains/conversation/prompt.py` & `langchain-0.0.99rc0/langchain/chains/conversation/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/graph_qa/base.py` & `langchain-0.0.99rc0/langchain/chains/graph_qa/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/graph_qa/prompts.py` & `langchain-0.0.99rc0/langchain/chains/graph_qa/prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/hyde/base.py` & `langchain-0.0.99rc0/langchain/chains/hyde/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/hyde/prompts.py` & `langchain-0.0.99rc0/langchain/chains/hyde/prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm.py` & `langchain-0.0.99rc0/langchain/chains/llm.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_bash/base.py` & `langchain-0.0.99rc0/langchain/chains/llm_bash/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_bash/prompt.py` & `langchain-0.0.99rc0/langchain/chains/llm_bash/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_checker/base.py` & `langchain-0.0.99rc0/langchain/chains/llm_checker/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_checker/prompt.py` & `langchain-0.0.99rc0/langchain/chains/llm_checker/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_math/base.py` & `langchain-0.0.99rc0/langchain/chains/llm_math/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_math/prompt.py` & `langchain-0.0.99rc0/langchain/chains/llm_math/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/llm_requests.py` & `langchain-0.0.99rc0/langchain/chains/llm_requests.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/loading.py` & `langchain-0.0.99rc0/langchain/chains/loading.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/mapreduce.py` & `langchain-0.0.99rc0/langchain/chains/mapreduce.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/moderation.py` & `langchain-0.0.99rc0/langchain/chains/moderation.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/natbot/base.py` & `langchain-0.0.99rc0/langchain/chains/natbot/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/natbot/crawler.py` & `langchain-0.0.99rc0/langchain/chains/natbot/crawler.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/natbot/prompt.py` & `langchain-0.0.99rc0/langchain/chains/natbot/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/pal/base.py` & `langchain-0.0.99rc0/langchain/chains/pal/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/pal/colored_object_prompt.py` & `langchain-0.0.99rc0/langchain/chains/pal/colored_object_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/pal/math_prompt.py` & `langchain-0.0.99rc0/langchain/chains/pal/math_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/qa_with_sources/base.py` & `langchain-0.0.99rc0/langchain/chains/qa_with_sources/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/qa_with_sources/loading.py` & `langchain-0.0.99rc0/langchain/chains/qa_with_sources/loading.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/qa_with_sources/map_reduce_prompt.py` & `langchain-0.0.99rc0/langchain/chains/qa_with_sources/map_reduce_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/qa_with_sources/refine_prompts.py` & `langchain-0.0.99rc0/langchain/chains/qa_with_sources/refine_prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/qa_with_sources/stuff_prompt.py` & `langchain-0.0.99rc0/langchain/chains/qa_with_sources/stuff_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/qa_with_sources/vector_db.py` & `langchain-0.0.99rc0/langchain/chains/qa_with_sources/vector_db.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/question_answering/__init__.py` & `langchain-0.0.99rc0/langchain/chains/question_answering/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/question_answering/map_reduce_prompt.py` & `langchain-0.0.99rc0/langchain/chains/question_answering/map_reduce_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/question_answering/map_rerank_prompt.py` & `langchain-0.0.99rc0/langchain/chains/question_answering/map_rerank_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/question_answering/refine_prompts.py` & `langchain-0.0.99rc0/langchain/chains/question_answering/refine_prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/sequential.py` & `langchain-0.0.99rc0/langchain/chains/sequential.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/sql_database/base.py` & `langchain-0.0.99rc0/langchain/chains/sql_database/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/sql_database/prompt.py` & `langchain-0.0.99rc0/langchain/chains/sql_database/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/summarize/__init__.py` & `langchain-0.0.99rc0/langchain/chains/summarize/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/summarize/refine_prompts.py` & `langchain-0.0.99rc0/langchain/chains/summarize/refine_prompts.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/transform.py` & `langchain-0.0.99rc0/langchain/chains/transform.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/chains/vector_db_qa/base.py` & `langchain-0.0.99rc0/langchain/chains/vector_db_qa/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/docker-compose.yaml` & `langchain-0.0.99rc0/langchain/docker-compose.yaml`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/docstore/base.py` & `langchain-0.0.99rc0/langchain/docstore/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/docstore/document.py` & `langchain-0.0.99rc0/langchain/docstore/document.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/docstore/in_memory.py` & `langchain-0.0.99rc0/langchain/docstore/in_memory.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/docstore/wikipedia.py` & `langchain-0.0.99rc0/langchain/docstore/wikipedia.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/__init__.py` & `langchain-0.0.99rc0/langchain/document_loaders/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/airbyte_json.py` & `langchain-0.0.99rc0/langchain/document_loaders/airbyte_json.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/azlyrics.py` & `langchain-0.0.99rc0/langchain/document_loaders/azlyrics.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/base.py` & `langchain-0.0.99rc0/langchain/document_loaders/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/college_confidential.py` & `langchain-0.0.99rc0/langchain/document_loaders/college_confidential.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/conllu.py` & `langchain-0.0.99rc0/langchain/document_loaders/conllu.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/directory.py` & `langchain-0.0.99rc0/langchain/document_loaders/directory.py`

 * *Files 14% similar despite different names*

```diff
@@ -26,30 +26,27 @@
     def __init__(
         self,
         path: str,
         glob: str = "**/[!.]*",
         silent_errors: bool = False,
         load_hidden: bool = False,
         loader_cls: FILE_LOADER_TYPE = UnstructuredFileLoader,
-        recursive: bool = False,
     ):
         """Initialize with path to directory and how to glob over it."""
         self.path = path
         self.glob = glob
         self.load_hidden = load_hidden
         self.loader_cls = loader_cls
         self.silent_errors = silent_errors
-        self.recursive = recursive
 
     def load(self) -> List[Document]:
         """Load documents."""
         p = Path(self.path)
         docs = []
-        items = p.rglob(self.glob) if self.recursive else p.glob(self.glob)
-        for i in items:
+        for i in p.glob(self.glob):
             if i.is_file():
                 if _is_visible(i.relative_to(p)) or self.load_hidden:
                     try:
                         sub_docs = self.loader_cls(str(i)).load()
                         docs.extend(sub_docs)
                     except Exception as e:
                         if self.silent_errors:
```

### Comparing `langchain-0.0.99/langchain/document_loaders/evernote.py` & `langchain-0.0.99rc0/langchain/document_loaders/evernote.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/facebook_chat.py` & `langchain-0.0.99rc0/langchain/document_loaders/facebook_chat.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/gcs_directory.py` & `langchain-0.0.99rc0/langchain/document_loaders/gcs_directory.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/gcs_file.py` & `langchain-0.0.99rc0/langchain/document_loaders/gcs_file.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/gitbook.py` & `langchain-0.0.99rc0/langchain/document_loaders/gitbook.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/googledrive.py` & `langchain-0.0.99rc0/langchain/document_loaders/googledrive.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/gutenberg.py` & `langchain-0.0.99rc0/langchain/document_loaders/gutenberg.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/hn.py` & `langchain-0.0.99rc0/langchain/document_loaders/hn.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/ifixit.py` & `langchain-0.0.99rc0/langchain/document_loaders/ifixit.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/notebook.py` & `langchain-0.0.99rc0/langchain/document_loaders/notebook.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/notion.py` & `langchain-0.0.99rc0/langchain/document_loaders/notion.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/obsidian.py` & `langchain-0.0.99rc0/langchain/document_loaders/obsidian.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/online_pdf.py` & `langchain-0.0.99rc0/langchain/document_loaders/online_pdf.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/paged_pdf.py` & `langchain-0.0.99rc0/langchain/document_loaders/paged_pdf.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/pdf.py` & `langchain-0.0.99rc0/langchain/document_loaders/pdf.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/powerpoint.py` & `langchain-0.0.99rc0/langchain/document_loaders/powerpoint.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/readthedocs.py` & `langchain-0.0.99rc0/langchain/document_loaders/readthedocs.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/roam.py` & `langchain-0.0.99rc0/langchain/document_loaders/roam.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/s3_directory.py` & `langchain-0.0.99rc0/langchain/document_loaders/s3_directory.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/s3_file.py` & `langchain-0.0.99rc0/langchain/document_loaders/s3_file.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/srt.py` & `langchain-0.0.99rc0/langchain/document_loaders/srt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/telegram.py` & `langchain-0.0.99rc0/langchain/document_loaders/telegram.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/text.py` & `langchain-0.0.99rc0/langchain/document_loaders/text.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/unstructured.py` & `langchain-0.0.99rc0/langchain/document_loaders/unstructured.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/url.py` & `langchain-0.0.99rc0/langchain/document_loaders/url.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/web_base.py` & `langchain-0.0.99rc0/langchain/document_loaders/web_base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/word_document.py` & `langchain-0.0.99rc0/langchain/document_loaders/word_document.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/document_loaders/youtube.py` & `langchain-0.0.99rc0/langchain/document_loaders/youtube.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/__init__.py` & `langchain-0.0.99rc0/langchain/embeddings/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/cohere.py` & `langchain-0.0.99rc0/langchain/embeddings/cohere.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/huggingface.py` & `langchain-0.0.99rc0/langchain/embeddings/huggingface.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/huggingface_hub.py` & `langchain-0.0.99rc0/langchain/embeddings/huggingface_hub.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/openai.py` & `langchain-0.0.99rc0/langchain/embeddings/openai.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/self_hosted.py` & `langchain-0.0.99rc0/langchain/embeddings/self_hosted.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/self_hosted_hugging_face.py` & `langchain-0.0.99rc0/langchain/embeddings/self_hosted_hugging_face.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/embeddings/tensorflow_hub.py` & `langchain-0.0.99rc0/langchain/embeddings/tensorflow_hub.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/evaluation/qa/eval_chain.py` & `langchain-0.0.99rc0/langchain/evaluation/qa/eval_chain.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/evaluation/qa/eval_prompt.py` & `langchain-0.0.99rc0/langchain/evaluation/qa/eval_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/evaluation/qa/generate_chain.py` & `langchain-0.0.99rc0/langchain/evaluation/qa/generate_chain.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/evaluation/qa/generate_prompt.py` & `langchain-0.0.99rc0/langchain/evaluation/qa/generate_prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/example_generator.py` & `langchain-0.0.99rc0/langchain/example_generator.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/formatting.py` & `langchain-0.0.99rc0/langchain/formatting.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/graphs/networkx_graph.py` & `langchain-0.0.99rc0/langchain/graphs/networkx_graph.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/indexes/graph.py` & `langchain-0.0.99rc0/langchain/indexes/graph.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/indexes/prompts/entity_extraction.py` & `langchain-0.0.99rc0/langchain/indexes/prompts/entity_extraction.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/indexes/prompts/entity_summarization.py` & `langchain-0.0.99rc0/langchain/indexes/prompts/entity_summarization.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/indexes/prompts/knowledge_triplet_extraction.py` & `langchain-0.0.99rc0/langchain/indexes/prompts/knowledge_triplet_extraction.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/indexes/vectorstore.py` & `langchain-0.0.99rc0/langchain/indexes/vectorstore.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/input.py` & `langchain-0.0.99rc0/langchain/input.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/__init__.py` & `langchain-0.0.99rc0/langchain/llms/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/ai21.py` & `langchain-0.0.99rc0/langchain/llms/ai21.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/aleph_alpha.py` & `langchain-0.0.99rc0/langchain/llms/aleph_alpha.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/anthropic.py` & `langchain-0.0.99rc0/langchain/llms/anthropic.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/bananadev.py` & `langchain-0.0.99rc0/langchain/llms/bananadev.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/base.py` & `langchain-0.0.99rc0/langchain/llms/base.py`

 * *Files 2% similar despite different names*

```diff
@@ -315,18 +315,14 @@
     with LLMs, rather than expect the user to implement the full _generate method.
     """
 
     @abstractmethod
     def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
         """Run the LLM on the given prompt and input."""
 
-    async def _acall(self, prompt: str, stop: Optional[List[str]] = None) -> str:
-        """Run the LLM on the given prompt and input."""
-        raise NotImplementedError("Async generation not implemented for this LLM.")
-
     def _generate(
         self, prompts: List[str], stop: Optional[List[str]] = None
     ) -> LLMResult:
         """Run the LLM on the given prompt and input."""
         # TODO: add caching here.
         generations = []
         for prompt in prompts:
@@ -334,12 +330,8 @@
             generations.append([Generation(text=text)])
         return LLMResult(generations=generations)
 
     async def _agenerate(
         self, prompts: List[str], stop: Optional[List[str]] = None
     ) -> LLMResult:
         """Run the LLM on the given prompt and input."""
-        generations = []
-        for prompt in prompts:
-            text = await self._acall(prompt, stop=stop)
-            generations.append([Generation(text=text)])
-        return LLMResult(generations=generations)
+        raise NotImplementedError("Async generation not implemented for this LLM.")
```

### Comparing `langchain-0.0.99/langchain/llms/cerebriumai.py` & `langchain-0.0.99rc0/langchain/llms/cerebriumai.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/cohere.py` & `langchain-0.0.99rc0/langchain/llms/cohere.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/deepinfra.py` & `langchain-0.0.99rc0/langchain/llms/deepinfra.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/fake.py` & `langchain-0.0.99rc0/langchain/llms/fake.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/forefrontai.py` & `langchain-0.0.99rc0/langchain/llms/forefrontai.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/gooseai.py` & `langchain-0.0.99rc0/langchain/llms/gooseai.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/huggingface_endpoint.py` & `langchain-0.0.99rc0/langchain/llms/huggingface_endpoint.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/huggingface_hub.py` & `langchain-0.0.99rc0/langchain/llms/huggingface_hub.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/huggingface_pipeline.py` & `langchain-0.0.99rc0/langchain/llms/huggingface_pipeline.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/loading.py` & `langchain-0.0.99rc0/langchain/llms/loading.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/manifest.py` & `langchain-0.0.99rc0/langchain/llms/manifest.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/modal.py` & `langchain-0.0.99rc0/langchain/llms/modal.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/nlpcloud.py` & `langchain-0.0.99rc0/langchain/llms/nlpcloud.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/openai.py` & `langchain-0.0.99rc0/langchain/llms/openai.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,8 @@
 """Wrapper around OpenAI APIs."""
-from __future__ import annotations
-
 import logging
 import sys
 from typing import (
     Any,
     Callable,
     Dict,
     Generator,
@@ -21,15 +19,15 @@
     before_sleep_log,
     retry,
     retry_if_exception_type,
     stop_after_attempt,
     wait_exponential,
 )
 
-from langchain.llms.base import BaseLLM
+from langchain.llms.base import LLM, BaseLLM
 from langchain.schema import Generation, LLMResult
 from langchain.utils import get_from_dict_or_env
 
 logger = logging.getLogger(__name__)
 
 
 def update_token_usage(
@@ -61,61 +59,14 @@
                 "finish_reason": None,
                 "logprobs": None,
             }
         ]
     }
 
 
-def _create_retry_decorator(llm: Union[BaseOpenAI, OpenAIChat]) -> Callable[[Any], Any]:
-    import openai
-
-    min_seconds = 4
-    max_seconds = 10
-    # Wait 2^x * 1 second between each retry starting with
-    # 4 seconds, then up to 10 seconds, then 10 seconds afterwards
-    return retry(
-        reraise=True,
-        stop=stop_after_attempt(llm.max_retries),
-        wait=wait_exponential(multiplier=1, min=min_seconds, max=max_seconds),
-        retry=(
-            retry_if_exception_type(openai.error.Timeout)
-            | retry_if_exception_type(openai.error.APIError)
-            | retry_if_exception_type(openai.error.APIConnectionError)
-            | retry_if_exception_type(openai.error.RateLimitError)
-            | retry_if_exception_type(openai.error.ServiceUnavailableError)
-        ),
-        before_sleep=before_sleep_log(logger, logging.WARNING),
-    )
-
-
-def completion_with_retry(llm: Union[BaseOpenAI, OpenAIChat], **kwargs: Any) -> Any:
-    """Use tenacity to retry the completion call."""
-    retry_decorator = _create_retry_decorator(llm)
-
-    @retry_decorator
-    def _completion_with_retry(**kwargs: Any) -> Any:
-        return llm.client.create(**kwargs)
-
-    return _completion_with_retry(**kwargs)
-
-
-async def acompletion_with_retry(
-    llm: Union[BaseOpenAI, OpenAIChat], **kwargs: Any
-) -> Any:
-    """Use tenacity to retry the async completion call."""
-    retry_decorator = _create_retry_decorator(llm)
-
-    @retry_decorator
-    async def _completion_with_retry(**kwargs: Any) -> Any:
-        # Use OpenAI's async api https://github.com/openai/openai-python#async-api
-        return await llm.client.acreate(**kwargs)
-
-    return await _completion_with_retry(**kwargs)
-
-
 class BaseOpenAI(BaseLLM, BaseModel):
     """Wrapper around OpenAI large language models.
 
     To use, you should have the ``openai`` python package installed, and the
     environment variable ``OPENAI_API_KEY`` set with your API key.
 
     Any parameters that are valid to be passed to the openai.create call can be passed
@@ -219,14 +170,56 @@
             "n": self.n,
             "best_of": self.best_of,
             "request_timeout": self.request_timeout,
             "logit_bias": self.logit_bias,
         }
         return {**normal_params, **self.model_kwargs}
 
+    def _create_retry_decorator(self) -> Callable[[Any], Any]:
+        import openai
+
+        min_seconds = 4
+        max_seconds = 10
+        # Wait 2^x * 1 second between each retry starting with
+        # 4 seconds, then up to 10 seconds, then 10 seconds afterwards
+        return retry(
+            reraise=True,
+            stop=stop_after_attempt(self.max_retries),
+            wait=wait_exponential(multiplier=1, min=min_seconds, max=max_seconds),
+            retry=(
+                retry_if_exception_type(openai.error.Timeout)
+                | retry_if_exception_type(openai.error.APIError)
+                | retry_if_exception_type(openai.error.APIConnectionError)
+                | retry_if_exception_type(openai.error.RateLimitError)
+                | retry_if_exception_type(openai.error.ServiceUnavailableError)
+            ),
+            before_sleep=before_sleep_log(logger, logging.WARNING),
+        )
+
+    def completion_with_retry(self, **kwargs: Any) -> Any:
+        """Use tenacity to retry the completion call."""
+        retry_decorator = self._create_retry_decorator()
+
+        @retry_decorator
+        def _completion_with_retry(**kwargs: Any) -> Any:
+            return self.client.create(**kwargs)
+
+        return _completion_with_retry(**kwargs)
+
+    async def acompletion_with_retry(self, **kwargs: Any) -> Any:
+        """Use tenacity to retry the async completion call."""
+        retry_decorator = self._create_retry_decorator()
+
+        @retry_decorator
+        async def _completion_with_retry(**kwargs: Any) -> Any:
+            # Use OpenAI's async api https://github.com/openai/openai-python#async-api
+            return await self.client.acreate(**kwargs)
+
+        return await _completion_with_retry(**kwargs)
+
     def _generate(
         self, prompts: List[str], stop: Optional[List[str]] = None
     ) -> LLMResult:
         """Call out to OpenAI's endpoint with k unique prompts.
 
         Args:
             prompts: The prompts to pass into the model.
@@ -250,26 +243,26 @@
         _keys = {"completion_tokens", "prompt_tokens", "total_tokens"}
         for _prompts in sub_prompts:
             if self.streaming:
                 if len(_prompts) > 1:
                     raise ValueError("Cannot stream results with multiple prompts.")
                 params["stream"] = True
                 response = _streaming_response_template()
-                for stream_resp in completion_with_retry(
-                    self, prompt=_prompts, **params
+                for stream_resp in self.completion_with_retry(
+                    prompt=_prompts, **params
                 ):
                     self.callback_manager.on_llm_new_token(
                         stream_resp["choices"][0]["text"],
                         verbose=self.verbose,
                         logprobs=stream_resp["choices"][0]["logprobs"],
                     )
                     _update_response(response, stream_resp)
                 choices.extend(response["choices"])
             else:
-                response = completion_with_retry(self, prompt=_prompts, **params)
+                response = self.completion_with_retry(prompt=_prompts, **params)
                 choices.extend(response["choices"])
             if not self.streaming:
                 # Can't update token usage if streaming
                 update_token_usage(_keys, response, token_usage)
         return self.create_llm_result(choices, prompts, token_usage)
 
     async def _agenerate(
@@ -285,16 +278,16 @@
         _keys = {"completion_tokens", "prompt_tokens", "total_tokens"}
         for _prompts in sub_prompts:
             if self.streaming:
                 if len(_prompts) > 1:
                     raise ValueError("Cannot stream results with multiple prompts.")
                 params["stream"] = True
                 response = _streaming_response_template()
-                async for stream_resp in await acompletion_with_retry(
-                    self, prompt=_prompts, **params
+                async for stream_resp in await self.acompletion_with_retry(
+                    prompt=_prompts, **params
                 ):
                     if self.callback_manager.is_async:
                         await self.callback_manager.on_llm_new_token(
                             stream_resp["choices"][0]["text"],
                             verbose=self.verbose,
                             logprobs=stream_resp["choices"][0]["logprobs"],
                         )
@@ -303,15 +296,15 @@
                             stream_resp["choices"][0]["text"],
                             verbose=self.verbose,
                             logprobs=stream_resp["choices"][0]["logprobs"],
                         )
                     _update_response(response, stream_resp)
                 choices.extend(response["choices"])
             else:
-                response = await acompletion_with_retry(self, prompt=_prompts, **params)
+                response = await self.acompletion_with_retry(prompt=_prompts, **params)
                 choices.extend(response["choices"])
             if not self.streaming:
                 # Can't update token usage if streaming
                 update_token_usage(_keys, response, token_usage)
         return self.create_llm_result(choices, prompts, token_usage)
 
     def get_sub_prompts(
@@ -518,42 +511,39 @@
         }
 
     @property
     def _invocation_params(self) -> Dict[str, Any]:
         return {**{"engine": self.deployment_name}, **super()._invocation_params}
 
 
-class OpenAIChat(BaseLLM, BaseModel):
+class OpenAIChat(LLM, BaseModel):
     """Wrapper around OpenAI Chat large language models.
 
     To use, you should have the ``openai`` python package installed, and the
     environment variable ``OPENAI_API_KEY`` set with your API key.
 
     Any parameters that are valid to be passed to the openai.create call can be passed
     in, even if not explicitly saved on this class.
 
     Example:
         .. code-block:: python
 
-            from langchain.llms import OpenAIChat
-            openaichat = OpenAIChat(model_name="gpt-3.5-turbo")
+            from langchain.llms import OpenAI
+            openai = OpenAI(model_name="gpt-3.5-turbo")
     """
 
     client: Any  #: :meta private:
     model_name: str = "gpt-3.5-turbo"
     """Model name to use."""
     model_kwargs: Dict[str, Any] = Field(default_factory=dict)
     """Holds any model parameters valid for `create` call not explicitly specified."""
     openai_api_key: Optional[str] = None
     max_retries: int = 6
     """Maximum number of retries to make when generating."""
     prefix_messages: List = Field(default_factory=list)
-    """Series of messages for Chat input."""
-    streaming: bool = False
-    """Whether to stream the results or not."""
 
     class Config:
         """Configuration for this pydantic object."""
 
         extra = Extra.ignore
 
     @root_validator(pre=True)
@@ -596,90 +586,54 @@
         return values
 
     @property
     def _default_params(self) -> Dict[str, Any]:
         """Get the default parameters for calling OpenAI API."""
         return self.model_kwargs
 
-    def _get_chat_params(
-        self, prompts: List[str], stop: Optional[List[str]] = None
-    ) -> Tuple:
-        if len(prompts) > 1:
-            raise ValueError(
-                f"OpenAIChat currently only supports single prompt, got {prompts}"
-            )
-        messages = self.prefix_messages + [{"role": "user", "content": prompts[0]}]
+    def _create_retry_decorator(self) -> Callable[[Any], Any]:
+        import openai
+
+        min_seconds = 4
+        max_seconds = 10
+        # Wait 2^x * 1 second between each retry starting with
+        # 4 seconds, then up to 10 seconds, then 10 seconds afterwards
+        return retry(
+            reraise=True,
+            stop=stop_after_attempt(self.max_retries),
+            wait=wait_exponential(multiplier=1, min=min_seconds, max=max_seconds),
+            retry=(
+                retry_if_exception_type(openai.error.Timeout)
+                | retry_if_exception_type(openai.error.APIError)
+                | retry_if_exception_type(openai.error.APIConnectionError)
+                | retry_if_exception_type(openai.error.RateLimitError)
+                | retry_if_exception_type(openai.error.ServiceUnavailableError)
+            ),
+            before_sleep=before_sleep_log(logger, logging.WARNING),
+        )
+
+    def completion_with_retry(self, **kwargs: Any) -> Any:
+        """Use tenacity to retry the completion call."""
+        retry_decorator = self._create_retry_decorator()
+
+        @retry_decorator
+        def _completion_with_retry(**kwargs: Any) -> Any:
+            return self.client.create(**kwargs)
+
+        return _completion_with_retry(**kwargs)
+
+    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
+        messages = self.prefix_messages + [{"role": "user", "content": prompt}]
         params: Dict[str, Any] = {**{"model": self.model_name}, **self._default_params}
         if stop is not None:
             if "stop" in params:
                 raise ValueError("`stop` found in both the input and default params.")
             params["stop"] = stop
-        return messages, params
-
-    def _generate(
-        self, prompts: List[str], stop: Optional[List[str]] = None
-    ) -> LLMResult:
-        messages, params = self._get_chat_params(prompts, stop)
-        if self.streaming:
-            response = ""
-            params["stream"] = True
-            for stream_resp in completion_with_retry(self, messages=messages, **params):
-                token = stream_resp["choices"][0]["delta"].get("content", "")
-                response += token
-                self.callback_manager.on_llm_new_token(
-                    token,
-                    verbose=self.verbose,
-                )
-            return LLMResult(
-                generations=[[Generation(text=response)]],
-            )
-        else:
-            full_response = completion_with_retry(self, messages=messages, **params)
-            return LLMResult(
-                generations=[
-                    [Generation(text=full_response["choices"][0]["message"]["content"])]
-                ],
-                llm_output={"token_usage": full_response["usage"]},
-            )
-
-    async def _agenerate(
-        self, prompts: List[str], stop: Optional[List[str]] = None
-    ) -> LLMResult:
-        messages, params = self._get_chat_params(prompts, stop)
-        if self.streaming:
-            response = ""
-            params["stream"] = True
-            async for stream_resp in await acompletion_with_retry(
-                self, messages=messages, **params
-            ):
-                token = stream_resp["choices"][0]["delta"].get("content", "")
-                response += token
-                if self.callback_manager.is_async:
-                    await self.callback_manager.on_llm_new_token(
-                        token,
-                        verbose=self.verbose,
-                    )
-                else:
-                    self.callback_manager.on_llm_new_token(
-                        token,
-                        verbose=self.verbose,
-                    )
-            return LLMResult(
-                generations=[[Generation(text=response)]],
-            )
-        else:
-            full_response = await acompletion_with_retry(
-                self, messages=messages, **params
-            )
-            return LLMResult(
-                generations=[
-                    [Generation(text=full_response["choices"][0]["message"]["content"])]
-                ],
-                llm_output={"token_usage": full_response["usage"]},
-            )
+        response = self.completion_with_retry(messages=messages, **params)
+        return response["choices"][0]["message"]["content"]
 
     @property
     def _identifying_params(self) -> Mapping[str, Any]:
         """Get the identifying parameters."""
         return {**{"model_name": self.model_name}, **self._default_params}
 
     @property
```

### Comparing `langchain-0.0.99/langchain/llms/petals.py` & `langchain-0.0.99rc0/langchain/llms/petals.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/promptlayer_openai.py` & `langchain-0.0.99rc0/langchain/llms/promptlayer_openai.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/self_hosted.py` & `langchain-0.0.99rc0/langchain/llms/self_hosted.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/self_hosted_hugging_face.py` & `langchain-0.0.99rc0/langchain/llms/self_hosted_hugging_face.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/stochasticai.py` & `langchain-0.0.99rc0/langchain/llms/stochasticai.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/llms/writer.py` & `langchain-0.0.99rc0/langchain/llms/writer.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/model_laboratory.py` & `langchain-0.0.99rc0/langchain/model_laboratory.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/base.py` & `langchain-0.0.99rc0/langchain/prompts/base.py`

 * *Files 4% similar despite different names*

```diff
@@ -42,19 +42,16 @@
             f"Invalid template format. Got `{template_format}`;"
             f" should be one of {valid_formats}"
         )
     dummy_inputs = {input_variable: "foo" for input_variable in input_variables}
     try:
         formatter_func = DEFAULT_FORMATTER_MAPPING[template_format]
         formatter_func(template, **dummy_inputs)
-    except KeyError as e:
-        raise ValueError(
-            "Invalid prompt schema; check for mismatched or missing input parameters. "
-            + str(e)
-        )
+    except KeyError:
+        raise ValueError("Invalid prompt schema.")
 
 
 class BaseOutputParser(BaseModel, ABC):
     """Class to parse the output of an LLM call."""
 
     @abstractmethod
     def parse(self, text: str) -> Union[str, List[str], Dict[str, str]]:
```

### Comparing `langchain-0.0.99/langchain/prompts/example_selector/base.py` & `langchain-0.0.99rc0/langchain/prompts/example_selector/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/example_selector/length_based.py` & `langchain-0.0.99rc0/langchain/prompts/example_selector/length_based.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/example_selector/ngram_overlap.py` & `langchain-0.0.99rc0/langchain/prompts/example_selector/ngram_overlap.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/example_selector/semantic_similarity.py` & `langchain-0.0.99rc0/langchain/prompts/example_selector/semantic_similarity.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/few_shot.py` & `langchain-0.0.99rc0/langchain/prompts/few_shot.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/few_shot_with_templates.py` & `langchain-0.0.99rc0/langchain/prompts/few_shot_with_templates.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/loading.py` & `langchain-0.0.99rc0/langchain/prompts/loading.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/prompts/prompt.py` & `langchain-0.0.99rc0/langchain/prompts/prompt.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,13 +1,12 @@
 """Prompt schema definition."""
 from __future__ import annotations
 
-from pathlib import Path
 from string import Formatter
-from typing import Any, Dict, List, Union
+from typing import Any, Dict, List
 
 from pydantic import BaseModel, Extra, root_validator
 
 from langchain.prompts.base import (
     DEFAULT_FORMATTER_MAPPING,
     BasePromptTemplate,
     check_valid_template,
@@ -102,26 +101,26 @@
             The final prompt generated.
         """
         template = example_separator.join([prefix, *examples, suffix])
         return cls(input_variables=input_variables, template=template)
 
     @classmethod
     def from_file(
-        cls, template_file: Union[str, Path], input_variables: List[str]
+        cls, template_file: str, input_variables: List[str]
     ) -> PromptTemplate:
         """Load a prompt from a file.
 
         Args:
             template_file: The path to the file containing the prompt template.
             input_variables: A list of variable names the final prompt template
                 will expect.
         Returns:
             The prompt loaded from the file.
         """
-        with open(str(template_file), "r") as f:
+        with open(template_file, "r") as f:
             template = f.read()
         return cls(input_variables=input_variables, template=template)
 
     @classmethod
     def from_template(cls, template: str) -> PromptTemplate:
         """Load a prompt template from a template."""
         input_variables = {
```

### Comparing `langchain-0.0.99/langchain/python.py` & `langchain-0.0.99rc0/langchain/python.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/requests.py` & `langchain-0.0.99rc0/langchain/requests.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/sql_database.py` & `langchain-0.0.99rc0/langchain/sql_database.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/text_splitter.py` & `langchain-0.0.99rc0/langchain/text_splitter.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/base.py` & `langchain-0.0.99rc0/langchain/tools/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/bing_search/tool.py` & `langchain-0.0.99rc0/langchain/tools/bing_search/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/google_search/tool.py` & `langchain-0.0.99rc0/langchain/tools/google_search/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/ifttt.py` & `langchain-0.0.99rc0/langchain/tools/ifttt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/interaction/tool.py` & `langchain-0.0.99rc0/langchain/tools/interaction/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/json/tool.py` & `langchain-0.0.99rc0/langchain/tools/json/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/python/tool.py` & `langchain-0.0.99rc0/langchain/tools/python/tool.py`

 * *Files 2% similar despite different names*

```diff
@@ -47,15 +47,15 @@
     )
     globals: Optional[Dict] = Field(default_factory=dict)
     locals: Optional[Dict] = Field(default_factory=dict)
 
     @root_validator(pre=True)
     def validate_python_version(cls, values: Dict) -> Dict:
         """Validate valid python version."""
-        if sys.version_info < (3, 9):
+        if sys.version_info[0] <= 8:
             raise ValueError(
                 "This tool relies on Python 3.9 or higher "
                 "(as it uses new functionality in the `ast` module, "
                 f"you have Python version: {sys.version}"
             )
         return values
```

### Comparing `langchain-0.0.99/langchain/tools/requests/tool.py` & `langchain-0.0.99rc0/langchain/tools/requests/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/sql_database/prompt.py` & `langchain-0.0.99rc0/langchain/tools/sql_database/prompt.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/sql_database/tool.py` & `langchain-0.0.99rc0/langchain/tools/sql_database/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/vectorstore/tool.py` & `langchain-0.0.99rc0/langchain/tools/vectorstore/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/tools/wolfram_alpha/tool.py` & `langchain-0.0.99rc0/langchain/tools/wolfram_alpha/tool.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/__init__.py` & `langchain-0.0.99rc0/langchain/utilities/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/bash.py` & `langchain-0.0.99rc0/langchain/utilities/bash.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/bing_search.py` & `langchain-0.0.99rc0/langchain/utilities/bing_search.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/google_search.py` & `langchain-0.0.99rc0/langchain/utilities/google_search.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/google_serper.py` & `langchain-0.0.99rc0/langchain/utilities/google_serper.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/loading.py` & `langchain-0.0.99rc0/langchain/utilities/loading.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/searx_search.py` & `langchain-0.0.99rc0/langchain/utilities/searx_search.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/serpapi.py` & `langchain-0.0.99rc0/langchain/utilities/serpapi.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utilities/wolfram_alpha.py` & `langchain-0.0.99rc0/langchain/utilities/wolfram_alpha.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/utils.py` & `langchain-0.0.99rc0/langchain/utils.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/__init__.py` & `langchain-0.0.99rc0/langchain/vectorstores/__init__.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/atlas.py` & `langchain-0.0.99rc0/langchain/vectorstores/atlas.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/base.py` & `langchain-0.0.99rc0/langchain/vectorstores/base.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/chroma.py` & `langchain-0.0.99rc0/langchain/vectorstores/chroma.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/deeplake.py` & `langchain-0.0.99rc0/langchain/vectorstores/deeplake.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/elastic_vector_search.py` & `langchain-0.0.99rc0/langchain/vectorstores/elastic_vector_search.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/faiss.py` & `langchain-0.0.99rc0/langchain/vectorstores/faiss.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/milvus.py` & `langchain-0.0.99rc0/langchain/vectorstores/milvus.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/opensearch_vector_search.py` & `langchain-0.0.99rc0/langchain/vectorstores/opensearch_vector_search.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/pinecone.py` & `langchain-0.0.99rc0/langchain/vectorstores/pinecone.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/utils.py` & `langchain-0.0.99rc0/langchain/vectorstores/utils.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/langchain/vectorstores/weaviate.py` & `langchain-0.0.99rc0/langchain/vectorstores/weaviate.py`

 * *Files identical despite different names*

### Comparing `langchain-0.0.99/pyproject.toml` & `langchain-0.0.99rc0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "langchain"
-version = "0.0.99"
+version = "0.0.99rc0"
 description = "Building applications with LLMs through composability"
 authors = []
 license = "MIT"
 readme = "README.md"
 repository = "https://www.github.com/hwchase17/langchain"
 
 [tool.poetry.scripts]
@@ -31,15 +31,15 @@
 jinja2 = {version = "^3", optional = true}
 tiktoken = {version = "^0", optional = true, python="^3.9"}
 pinecone-client = {version = "^2", optional = true}
 weaviate-client = {version = "^3", optional = true}
 google-api-python-client = {version = "2.70.0", optional = true}
 wolframalpha = {version = "5.0.0", optional = true}
 anthropic = {version = "^0.2.2", optional = true}
-qdrant-client = {version = "^1.0.4", optional = true, python = ">=3.8.1,<3.12"}
+qdrant-client = {version = "^0.11.7", optional = true}
 dataclasses-json = "^0.5.7"
 tensorflow-text = {version = "^2.11.0", optional = true, python = "^3.10, <3.12"}
 tenacity = "^8.1.0"
 cohere = {version = "^3", optional = true}
 openai = {version = "^0", optional = true}
 nlpcloud = {version = "^1", optional = true}
 nomic = {version = "^1.0.43", optional = true}
```

### Comparing `langchain-0.0.99/PKG-INFO` & `langchain-0.0.99rc0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: langchain
-Version: 0.0.99
+Version: 0.0.99rc0
 Summary: Building applications with LLMs through composability
 Home-page: https://www.github.com/hwchase17/langchain
 License: MIT
 Requires-Python: >=3.8.1,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
@@ -34,15 +34,15 @@
 Requires-Dist: nomic (>=1.0.43,<2.0.0) ; extra == "all"
 Requires-Dist: numpy (>=1,<2)
 Requires-Dist: openai (>=0,<1) ; extra == "llms" or extra == "all"
 Requires-Dist: opensearch-py (>=2.0.0,<3.0.0) ; extra == "all"
 Requires-Dist: pinecone-client (>=2,<3) ; extra == "all"
 Requires-Dist: pydantic (>=1,<2)
 Requires-Dist: pypdf (>=3.4.0,<4.0.0) ; extra == "all"
-Requires-Dist: qdrant-client (>=1.0.4,<2.0.0) ; (python_full_version >= "3.8.1" and python_version < "3.12") and (extra == "all")
+Requires-Dist: qdrant-client (>=0.11.7,<0.12.0) ; extra == "all"
 Requires-Dist: redis (>=4,<5) ; extra == "all"
 Requires-Dist: requests (>=2,<3)
 Requires-Dist: sentence-transformers (>=2,<3) ; extra == "all"
 Requires-Dist: spacy (>=3,<4) ; extra == "all"
 Requires-Dist: tenacity (>=8.1.0,<9.0.0)
 Requires-Dist: tensorflow-text (>=2.11.0,<3.0.0) ; (python_version >= "3.10" and python_version < "3.12") and (extra == "all")
 Requires-Dist: tiktoken (>=0,<1) ; (python_version >= "3.9" and python_version < "4.0") and (extra == "all")
@@ -94,15 +94,15 @@
 ## 📖 Documentation
 
 Please see [here](https://langchain.readthedocs.io/en/latest/?) for full documentation on:
 
 - Getting started (installation, setting up the environment, simple examples)
 - How-To examples (demos, integrations, helper functions)
 - Reference (full API docs)
-- Resources (high-level explanation of core concepts)
+  Resources (high-level explanation of core concepts)
 
 ## 🚀 What can this help with?
 
 There are six main areas that LangChain is designed to help with.
 These are, in increasing order of complexity:
 
 **📃 LLMs and Prompts:**
```

