# Comparing `tmp/azure-core-1.8.2.zip` & `tmp/azure-core-1.9.0.zip`

## zipinfo {}

```diff
@@ -1,127 +1,128 @@
-Zip file size: 220024 bytes, number of entries: 125
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/samples/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/doc/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/tests/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/
--rw-r--r--  2.0 unx    19899 b- defN 20-Oct-05 15:35 azure-core-1.8.2/CLIENT_LIBRARY_DEVELOPER.md
--rw-r--r--  2.0 unx       67 b- defN 20-Oct-05 15:36 azure-core-1.8.2/setup.cfg
--rw-r--r--  2.0 unx    10515 b- defN 20-Oct-05 15:35 azure-core-1.8.2/CHANGELOG.md
--rw-r--r--  2.0 unx     6131 b- defN 20-Oct-05 15:35 azure-core-1.8.2/README.md
--rw-r--r--  2.0 unx     2631 b- defN 20-Oct-05 15:35 azure-core-1.8.2/setup.py
--rw-r--r--  2.0 unx      161 b- defN 20-Oct-05 15:35 azure-core-1.8.2/MANIFEST.in
--rw-r--r--  2.0 unx    20707 b- defN 20-Oct-05 15:36 azure-core-1.8.2/PKG-INFO
--rw-r--r--  2.0 unx     6449 b- defN 20-Oct-05 15:35 azure-core-1.8.2/samples/test_example_sansio.py
--rw-r--r--  2.0 unx     7324 b- defN 20-Oct-05 15:35 azure-core-1.8.2/samples/test_example_sync.py
--rw-r--r--  2.0 unx     1465 b- defN 20-Oct-05 15:35 azure-core-1.8.2/samples/conftest.py
--rw-r--r--  2.0 unx      892 b- defN 20-Oct-05 15:35 azure-core-1.8.2/samples/README.md
--rw-r--r--  2.0 unx     8197 b- defN 20-Oct-05 15:35 azure-core-1.8.2/samples/test_example_async.py
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/
--rw-r--r--  2.0 unx       80 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/__init__.py
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/pipeline/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/tracing/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/polling/
--rw-r--r--  2.0 unx      657 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/credentials_async.py
--rw-r--r--  2.0 unx     1506 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/_match_conditions.py
--rw-r--r--  2.0 unx     4673 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/paging.py
--rw-r--r--  2.0 unx     4456 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/_pipeline_client.py
--rw-r--r--  2.0 unx      492 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/_version.py
--rw-r--r--  2.0 unx     5609 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/configuration.py
--rw-r--r--  2.0 unx    16027 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/exceptions.py
--rw-r--r--  2.0 unx     5818 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/async_paging.py
--rw-r--r--  2.0 unx     4541 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/_pipeline_client_async.py
--rw-r--r--  2.0 unx     2273 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/credentials.py
--rw-r--r--  2.0 unx    13656 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/settings.py
--rw-r--r--  2.0 unx        0 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/py.typed
--rw-r--r--  2.0 unx     1710 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/__init__.py
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/pipeline/policies/
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/pipeline/transport/
--rw-r--r--  2.0 unx     1610 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/_tools_async.py
--rw-r--r--  2.0 unx     8284 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/_base.py
--rw-r--r--  2.0 unx     8716 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/_base_async.py
--rw-r--r--  2.0 unx     1636 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/_tools.py
--rw-r--r--  2.0 unx     7277 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/__init__.py
--rw-r--r--  2.0 unx     4581 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_authentication.py
--rw-r--r--  2.0 unx     5596 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_distributed_tracing.py
--rw-r--r--  2.0 unx     3405 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_custom_hook.py
--rw-r--r--  2.0 unx     3317 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_utils.py
--rw-r--r--  2.0 unx     8040 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_retry_async.py
--rw-r--r--  2.0 unx     7097 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_redirect.py
--rw-r--r--  2.0 unx     1733 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_authentication_async.py
--rw-r--r--  2.0 unx     6021 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_base.py
--rw-r--r--  2.0 unx     3080 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_base_async.py
--rw-r--r--  2.0 unx     3360 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_redirect_async.py
--rw-r--r--  2.0 unx    26918 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_universal.py
--rw-r--r--  2.0 unx    19939 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/_retry.py
--rw-r--r--  2.0 unx     2729 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/policies/__init__.py
--rw-r--r--  2.0 unx     9637 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_requests_trio.py
--rw-r--r--  2.0 unx     2326 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_base_requests_async.py
--rw-r--r--  2.0 unx    34222 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_base.py
--rw-r--r--  2.0 unx     6388 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_base_async.py
--rw-r--r--  2.0 unx     8673 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_requests_asyncio.py
--rw-r--r--  2.0 unx     2549 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/__init__.py
--rw-r--r--  2.0 unx    12855 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_aiohttp.py
--rw-r--r--  2.0 unx    11427 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/pipeline/transport/_requests_basic.py
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/azure/core/tracing/ext/
--rw-r--r--  2.0 unx     3539 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/tracing/decorator_async.py
--rw-r--r--  2.0 unx     7105 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/tracing/_abstract_span.py
--rw-r--r--  2.0 unx     3600 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/tracing/decorator.py
--rw-r--r--  2.0 unx     3969 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/tracing/common.py
--rw-r--r--  2.0 unx      298 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/tracing/__init__.py
--rw-r--r--  2.0 unx        0 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/tracing/ext/__init__.py
--rw-r--r--  2.0 unx     5001 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/polling/async_base_polling.py
--rw-r--r--  2.0 unx     7412 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/polling/_async_poller.py
--rw-r--r--  2.0 unx    20230 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/polling/base_polling.py
--rw-r--r--  2.0 unx     1728 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/polling/__init__.py
--rw-r--r--  2.0 unx    11087 b- defN 20-Oct-05 15:35 azure-core-1.8.2/azure/core/polling/_poller.py
--rw-r--r--  2.0 unx      901 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.core.rst
--rw-r--r--  2.0 unx      159 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.core.pipeline.policies.rst
--rw-r--r--  2.0 unx      644 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.core.tracing.rst
--rw-r--r--  2.0 unx      160 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.rst
--rw-r--r--  2.0 unx      129 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.core.polling.rst
--rw-r--r--  2.0 unx      237 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.core.pipeline.rst
--rw-r--r--  2.0 unx      162 b- defN 20-Oct-05 15:35 azure-core-1.8.2/doc/azure.core.pipeline.transport.rst
-drwxr-xr-x  2.0 unx        0 b- stor 20-Oct-05 15:36 azure-core-1.8.2/tests/azure_core_asynctests/
--rw-r--r--  2.0 unx     4949 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_paging.py
--rw-r--r--  2.0 unx     6496 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_tracing_decorator.py
--rw-r--r--  2.0 unx     3073 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_stream_generator.py
--rw-r--r--  2.0 unx     9337 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_exceptions.py
--rw-r--r--  2.0 unx    39464 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_basic_transport.py
--rw-r--r--  2.0 unx     2608 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_error_map.py
--rw-r--r--  2.0 unx    12701 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_universal_pipeline.py
--rw-r--r--  2.0 unx     2666 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_request_id_policy.py
--rw-r--r--  2.0 unx     8074 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_settings.py
--rw-r--r--  2.0 unx     7985 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_authentication.py
--rw-r--r--  2.0 unx     8575 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_retry_policy.py
--rw-r--r--  2.0 unx     3365 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_requests_universal.py
--rw-r--r--  2.0 unx     1549 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_user_agent_policy.py
--rw-r--r--  2.0 unx     1796 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/conftest.py
--rw-r--r--  2.0 unx    11096 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_http_logging_policy.py
--rw-r--r--  2.0 unx     6618 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/tracing_common.py
--rw-r--r--  2.0 unx     3428 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_custom_hook_policy.py
--rw-r--r--  2.0 unx     8091 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_polling.py
--rw-r--r--  2.0 unx     9419 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_tracing_policy.py
--rw-r--r--  2.0 unx    12055 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_pipeline.py
--rw-r--r--  2.0 unx    24302 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/test_base_polling.py
--rw-r--r--  2.0 unx     4040 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_universal_http.py
--rw-r--r--  2.0 unx     4143 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_paging.py
--rw-r--r--  2.0 unx     3493 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_stream_generator.py
--rw-r--r--  2.0 unx    32879 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_basic_transport.py
--rw-r--r--  2.0 unx     1313 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_request_trio.py
--rw-r--r--  2.0 unx     1250 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_request_asyncio.py
--rw-r--r--  2.0 unx     6902 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_authentication.py
--rw-r--r--  2.0 unx     6637 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_tracing_decorator_async.py
--rw-r--r--  2.0 unx     9023 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_retry_policy.py
--rw-r--r--  2.0 unx    22996 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_async_base_polling.py
--rw-r--r--  2.0 unx     6918 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_polling.py
--rw-r--r--  2.0 unx    11143 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_http_logging_policy_async.py
--rw-r--r--  2.0 unx     7679 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/test_pipeline.py
--rw-r--r--  2.0 unx     1303 b- defN 20-Oct-05 15:35 azure-core-1.8.2/tests/azure_core_asynctests/__init__.py
--rw-r--r--  2.0 unx        1 b- defN 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/not-zip-safe
--rw-r--r--  2.0 unx      134 b- defN 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/requires.txt
--rw-r--r--  2.0 unx        6 b- defN 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/top_level.txt
--rw-r--r--  2.0 unx     3741 b- defN 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/SOURCES.txt
--rw-r--r--  2.0 unx    20707 b- defN 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/PKG-INFO
--rw-r--r--  2.0 unx        1 b- defN 20-Oct-05 15:36 azure-core-1.8.2/azure_core.egg-info/dependency_links.txt
-125 files, 755669 bytes uncompressed, 198526 bytes compressed:  73.7%
+Zip file size: 222783 bytes, number of entries: 126
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/tests/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/doc/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/samples/
+-rw-r--r--  2.0 unx    21119 b- defN 20-Nov-09 19:01 azure-core-1.9.0/PKG-INFO
+-rw-r--r--  2.0 unx      161 b- defN 20-Nov-09 19:00 azure-core-1.9.0/MANIFEST.in
+-rw-r--r--  2.0 unx    10831 b- defN 20-Nov-09 19:00 azure-core-1.9.0/CHANGELOG.md
+-rw-r--r--  2.0 unx     2631 b- defN 20-Nov-09 19:00 azure-core-1.9.0/setup.py
+-rw-r--r--  2.0 unx     6131 b- defN 20-Nov-09 19:00 azure-core-1.9.0/README.md
+-rw-r--r--  2.0 unx    19899 b- defN 20-Nov-09 19:00 azure-core-1.9.0/CLIENT_LIBRARY_DEVELOPER.md
+-rw-r--r--  2.0 unx       67 b- defN 20-Nov-09 19:01 azure-core-1.9.0/setup.cfg
+-rw-r--r--  2.0 unx        1 b- defN 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/dependency_links.txt
+-rw-r--r--  2.0 unx    21119 b- defN 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/PKG-INFO
+-rw-r--r--  2.0 unx      134 b- defN 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/requires.txt
+-rw-r--r--  2.0 unx     3807 b- defN 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/SOURCES.txt
+-rw-r--r--  2.0 unx        1 b- defN 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/not-zip-safe
+-rw-r--r--  2.0 unx        6 b- defN 20-Nov-09 19:01 azure-core-1.9.0/azure_core.egg-info/top_level.txt
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/tests/azure_core_asynctests/
+-rw-r--r--  2.0 unx     6618 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/tracing_common.py
+-rw-r--r--  2.0 unx     1549 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_user_agent_policy.py
+-rw-r--r--  2.0 unx     3365 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_requests_universal.py
+-rw-r--r--  2.0 unx     3073 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_stream_generator.py
+-rw-r--r--  2.0 unx     2666 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_request_id_policy.py
+-rw-r--r--  2.0 unx     7985 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_authentication.py
+-rw-r--r--  2.0 unx     8575 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_retry_policy.py
+-rw-r--r--  2.0 unx     5645 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_paging.py
+-rw-r--r--  2.0 unx     9419 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_tracing_policy.py
+-rw-r--r--  2.0 unx    24426 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_base_polling.py
+-rw-r--r--  2.0 unx    39464 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_basic_transport.py
+-rw-r--r--  2.0 unx     2608 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_error_map.py
+-rw-r--r--  2.0 unx    12701 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_universal_pipeline.py
+-rw-r--r--  2.0 unx    12055 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_pipeline.py
+-rw-r--r--  2.0 unx     9787 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_exceptions.py
+-rw-r--r--  2.0 unx     1796 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/conftest.py
+-rw-r--r--  2.0 unx    11096 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_http_logging_policy.py
+-rw-r--r--  2.0 unx     8074 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_settings.py
+-rw-r--r--  2.0 unx     8767 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_polling.py
+-rw-r--r--  2.0 unx     6496 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_tracing_decorator.py
+-rw-r--r--  2.0 unx     3428 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/test_custom_hook_policy.py
+-rw-r--r--  2.0 unx    23114 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_async_base_polling.py
+-rw-r--r--  2.0 unx     1303 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/__init__.py
+-rw-r--r--  2.0 unx     1250 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_request_asyncio.py
+-rw-r--r--  2.0 unx     3493 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_stream_generator.py
+-rw-r--r--  2.0 unx    11143 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_http_logging_policy_async.py
+-rw-r--r--  2.0 unx     6902 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_authentication.py
+-rw-r--r--  2.0 unx     9023 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_retry_policy.py
+-rw-r--r--  2.0 unx     4912 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_paging.py
+-rw-r--r--  2.0 unx    32879 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_basic_transport.py
+-rw-r--r--  2.0 unx     4040 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_universal_http.py
+-rw-r--r--  2.0 unx     7679 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_pipeline.py
+-rw-r--r--  2.0 unx     6637 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_tracing_decorator_async.py
+-rw-r--r--  2.0 unx     1313 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_request_trio.py
+-rw-r--r--  2.0 unx     7644 b- defN 20-Nov-09 19:00 azure-core-1.9.0/tests/azure_core_asynctests/test_polling.py
+-rw-r--r--  2.0 unx      237 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.core.pipeline.rst
+-rw-r--r--  2.0 unx      129 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.core.polling.rst
+-rw-r--r--  2.0 unx      644 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.core.tracing.rst
+-rw-r--r--  2.0 unx      160 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.rst
+-rw-r--r--  2.0 unx      162 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.core.pipeline.transport.rst
+-rw-r--r--  2.0 unx      159 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.core.pipeline.policies.rst
+-rw-r--r--  2.0 unx      901 b- defN 20-Nov-09 19:00 azure-core-1.9.0/doc/azure.core.rst
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/
+-rw-r--r--  2.0 unx       80 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/__init__.py
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/pipeline/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/polling/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/tracing/
+-rw-r--r--  2.0 unx     5609 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/configuration.py
+-rw-r--r--  2.0 unx     2273 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/credentials.py
+-rw-r--r--  2.0 unx     1710 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/__init__.py
+-rw-r--r--  2.0 unx      657 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/credentials_async.py
+-rw-r--r--  2.0 unx     4456 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/_pipeline_client.py
+-rw-r--r--  2.0 unx     4892 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/paging.py
+-rw-r--r--  2.0 unx     6037 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/async_paging.py
+-rw-r--r--  2.0 unx     1506 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/_match_conditions.py
+-rw-r--r--  2.0 unx     4541 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/_pipeline_client_async.py
+-rw-r--r--  2.0 unx    13656 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/settings.py
+-rw-r--r--  2.0 unx      492 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/_version.py
+-rw-r--r--  2.0 unx    16475 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/exceptions.py
+-rw-r--r--  2.0 unx        0 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/py.typed
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/pipeline/transport/
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/pipeline/policies/
+-rw-r--r--  2.0 unx     7277 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/__init__.py
+-rw-r--r--  2.0 unx     1610 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/_tools_async.py
+-rw-r--r--  2.0 unx     1636 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/_tools.py
+-rw-r--r--  2.0 unx     8284 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/_base.py
+-rw-r--r--  2.0 unx     8716 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/_base_async.py
+-rw-r--r--  2.0 unx     2549 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/__init__.py
+-rw-r--r--  2.0 unx     2112 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_bigger_block_size_http_adapters.py
+-rw-r--r--  2.0 unx     2326 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_base_requests_async.py
+-rw-r--r--  2.0 unx    11506 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_requests_basic.py
+-rw-r--r--  2.0 unx    12819 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_aiohttp.py
+-rw-r--r--  2.0 unx    34279 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_base.py
+-rw-r--r--  2.0 unx     6388 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_base_async.py
+-rw-r--r--  2.0 unx     8682 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_requests_asyncio.py
+-rw-r--r--  2.0 unx     9634 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/transport/_requests_trio.py
+-rw-r--r--  2.0 unx     3405 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_custom_hook.py
+-rw-r--r--  2.0 unx     3360 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_redirect_async.py
+-rw-r--r--  2.0 unx    19939 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_retry.py
+-rw-r--r--  2.0 unx     4581 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_authentication.py
+-rw-r--r--  2.0 unx     2729 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/__init__.py
+-rw-r--r--  2.0 unx    26918 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_universal.py
+-rw-r--r--  2.0 unx     7097 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_redirect.py
+-rw-r--r--  2.0 unx     8040 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_retry_async.py
+-rw-r--r--  2.0 unx     6022 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_base.py
+-rw-r--r--  2.0 unx     1733 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_authentication_async.py
+-rw-r--r--  2.0 unx     3080 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_base_async.py
+-rw-r--r--  2.0 unx     3317 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_utils.py
+-rw-r--r--  2.0 unx     5596 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/pipeline/policies/_distributed_tracing.py
+-rw-r--r--  2.0 unx     7923 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/polling/_async_poller.py
+-rw-r--r--  2.0 unx     1728 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/polling/__init__.py
+-rw-r--r--  2.0 unx    20261 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/polling/base_polling.py
+-rw-r--r--  2.0 unx    11615 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/polling/_poller.py
+-rw-r--r--  2.0 unx     5033 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/polling/async_base_polling.py
+drwxr-xr-x  2.0 unx        0 b- stor 20-Nov-09 19:01 azure-core-1.9.0/azure/core/tracing/ext/
+-rw-r--r--  2.0 unx     7105 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/tracing/_abstract_span.py
+-rw-r--r--  2.0 unx      298 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/tracing/__init__.py
+-rw-r--r--  2.0 unx     3969 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/tracing/common.py
+-rw-r--r--  2.0 unx     3539 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/tracing/decorator_async.py
+-rw-r--r--  2.0 unx     3600 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/tracing/decorator.py
+-rw-r--r--  2.0 unx        0 b- defN 20-Nov-09 19:00 azure-core-1.9.0/azure/core/tracing/ext/__init__.py
+-rw-r--r--  2.0 unx     6449 b- defN 20-Nov-09 19:00 azure-core-1.9.0/samples/test_example_sansio.py
+-rw-r--r--  2.0 unx     8197 b- defN 20-Nov-09 19:00 azure-core-1.9.0/samples/test_example_async.py
+-rw-r--r--  2.0 unx     7324 b- defN 20-Nov-09 19:00 azure-core-1.9.0/samples/test_example_sync.py
+-rw-r--r--  2.0 unx     1465 b- defN 20-Nov-09 19:00 azure-core-1.9.0/samples/conftest.py
+-rw-r--r--  2.0 unx      892 b- defN 20-Nov-09 19:00 azure-core-1.9.0/samples/README.md
+126 files, 764641 bytes uncompressed, 201045 bytes compressed:  73.7%
```

## zipnote {}

```diff
@@ -1,376 +1,379 @@
-Filename: azure-core-1.8.2/
+Filename: azure-core-1.9.0/
 Comment: 
 
-Filename: azure-core-1.8.2/samples/
+Filename: azure-core-1.9.0/azure_core.egg-info/
 Comment: 
 
-Filename: azure-core-1.8.2/azure/
+Filename: azure-core-1.9.0/tests/
 Comment: 
 
-Filename: azure-core-1.8.2/doc/
+Filename: azure-core-1.9.0/doc/
 Comment: 
 
-Filename: azure-core-1.8.2/tests/
+Filename: azure-core-1.9.0/azure/
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/
+Filename: azure-core-1.9.0/samples/
 Comment: 
 
-Filename: azure-core-1.8.2/CLIENT_LIBRARY_DEVELOPER.md
+Filename: azure-core-1.9.0/PKG-INFO
 Comment: 
 
-Filename: azure-core-1.8.2/setup.cfg
+Filename: azure-core-1.9.0/MANIFEST.in
 Comment: 
 
-Filename: azure-core-1.8.2/CHANGELOG.md
+Filename: azure-core-1.9.0/CHANGELOG.md
 Comment: 
 
-Filename: azure-core-1.8.2/README.md
+Filename: azure-core-1.9.0/setup.py
 Comment: 
 
-Filename: azure-core-1.8.2/setup.py
+Filename: azure-core-1.9.0/README.md
 Comment: 
 
-Filename: azure-core-1.8.2/MANIFEST.in
+Filename: azure-core-1.9.0/CLIENT_LIBRARY_DEVELOPER.md
 Comment: 
 
-Filename: azure-core-1.8.2/PKG-INFO
+Filename: azure-core-1.9.0/setup.cfg
 Comment: 
 
-Filename: azure-core-1.8.2/samples/test_example_sansio.py
+Filename: azure-core-1.9.0/azure_core.egg-info/dependency_links.txt
 Comment: 
 
-Filename: azure-core-1.8.2/samples/test_example_sync.py
+Filename: azure-core-1.9.0/azure_core.egg-info/PKG-INFO
 Comment: 
 
-Filename: azure-core-1.8.2/samples/conftest.py
+Filename: azure-core-1.9.0/azure_core.egg-info/requires.txt
 Comment: 
 
-Filename: azure-core-1.8.2/samples/README.md
+Filename: azure-core-1.9.0/azure_core.egg-info/SOURCES.txt
 Comment: 
 
-Filename: azure-core-1.8.2/samples/test_example_async.py
+Filename: azure-core-1.9.0/azure_core.egg-info/not-zip-safe
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/
+Filename: azure-core-1.9.0/azure_core.egg-info/top_level.txt
 Comment: 
 
-Filename: azure-core-1.8.2/azure/__init__.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/
+Filename: azure-core-1.9.0/tests/tracing_common.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/
+Filename: azure-core-1.9.0/tests/test_user_agent_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/polling/
+Filename: azure-core-1.9.0/tests/test_requests_universal.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/credentials_async.py
+Filename: azure-core-1.9.0/tests/test_stream_generator.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/_match_conditions.py
+Filename: azure-core-1.9.0/tests/test_request_id_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/paging.py
+Filename: azure-core-1.9.0/tests/test_authentication.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/_pipeline_client.py
+Filename: azure-core-1.9.0/tests/test_retry_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/_version.py
+Filename: azure-core-1.9.0/tests/test_paging.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/configuration.py
+Filename: azure-core-1.9.0/tests/test_tracing_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/exceptions.py
+Filename: azure-core-1.9.0/tests/test_base_polling.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/async_paging.py
+Filename: azure-core-1.9.0/tests/test_basic_transport.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/_pipeline_client_async.py
+Filename: azure-core-1.9.0/tests/test_error_map.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/credentials.py
+Filename: azure-core-1.9.0/tests/test_universal_pipeline.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/settings.py
+Filename: azure-core-1.9.0/tests/test_pipeline.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/py.typed
+Filename: azure-core-1.9.0/tests/test_exceptions.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/__init__.py
+Filename: azure-core-1.9.0/tests/conftest.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/
+Filename: azure-core-1.9.0/tests/test_http_logging_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/
+Filename: azure-core-1.9.0/tests/test_settings.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/_tools_async.py
+Filename: azure-core-1.9.0/tests/test_polling.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/_base.py
+Filename: azure-core-1.9.0/tests/test_tracing_decorator.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/_base_async.py
+Filename: azure-core-1.9.0/tests/test_custom_hook_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/_tools.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_async_base_polling.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/__init__.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_authentication.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_request_asyncio.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_distributed_tracing.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_stream_generator.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_custom_hook.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_http_logging_policy_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_utils.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_authentication.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_retry_async.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_retry_policy.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_redirect.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_paging.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_authentication_async.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_basic_transport.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_base.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_universal_http.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_base_async.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_pipeline.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_redirect_async.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_tracing_decorator_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_universal.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_request_trio.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/_retry.py
+Filename: azure-core-1.9.0/tests/azure_core_asynctests/test_polling.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/policies/__init__.py
+Filename: azure-core-1.9.0/doc/azure.core.pipeline.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_requests_trio.py
+Filename: azure-core-1.9.0/doc/azure.core.polling.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_base_requests_async.py
+Filename: azure-core-1.9.0/doc/azure.core.tracing.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_base.py
+Filename: azure-core-1.9.0/doc/azure.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_base_async.py
+Filename: azure-core-1.9.0/doc/azure.core.pipeline.transport.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_requests_asyncio.py
+Filename: azure-core-1.9.0/doc/azure.core.pipeline.policies.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/__init__.py
+Filename: azure-core-1.9.0/doc/azure.core.rst
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_aiohttp.py
+Filename: azure-core-1.9.0/azure/core/
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/pipeline/transport/_requests_basic.py
+Filename: azure-core-1.9.0/azure/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/ext/
+Filename: azure-core-1.9.0/azure/core/pipeline/
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/decorator_async.py
+Filename: azure-core-1.9.0/azure/core/polling/
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/_abstract_span.py
+Filename: azure-core-1.9.0/azure/core/tracing/
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/decorator.py
+Filename: azure-core-1.9.0/azure/core/configuration.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/common.py
+Filename: azure-core-1.9.0/azure/core/credentials.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/__init__.py
+Filename: azure-core-1.9.0/azure/core/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/tracing/ext/__init__.py
+Filename: azure-core-1.9.0/azure/core/credentials_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/polling/async_base_polling.py
+Filename: azure-core-1.9.0/azure/core/_pipeline_client.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/polling/_async_poller.py
+Filename: azure-core-1.9.0/azure/core/paging.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/polling/base_polling.py
+Filename: azure-core-1.9.0/azure/core/async_paging.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/polling/__init__.py
+Filename: azure-core-1.9.0/azure/core/_match_conditions.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure/core/polling/_poller.py
+Filename: azure-core-1.9.0/azure/core/_pipeline_client_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.core.rst
+Filename: azure-core-1.9.0/azure/core/settings.py
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.core.pipeline.policies.rst
+Filename: azure-core-1.9.0/azure/core/_version.py
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.core.tracing.rst
+Filename: azure-core-1.9.0/azure/core/exceptions.py
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.rst
+Filename: azure-core-1.9.0/azure/core/py.typed
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.core.polling.rst
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.core.pipeline.rst
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/
 Comment: 
 
-Filename: azure-core-1.8.2/doc/azure.core.pipeline.transport.rst
+Filename: azure-core-1.9.0/azure/core/pipeline/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/
+Filename: azure-core-1.9.0/azure/core/pipeline/_tools_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_paging.py
+Filename: azure-core-1.9.0/azure/core/pipeline/_tools.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_tracing_decorator.py
+Filename: azure-core-1.9.0/azure/core/pipeline/_base.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_stream_generator.py
+Filename: azure-core-1.9.0/azure/core/pipeline/_base_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_exceptions.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_basic_transport.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_bigger_block_size_http_adapters.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_error_map.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_base_requests_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_universal_pipeline.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_requests_basic.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_request_id_policy.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_aiohttp.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_settings.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_base.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_authentication.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_base_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_retry_policy.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_requests_asyncio.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_requests_universal.py
+Filename: azure-core-1.9.0/azure/core/pipeline/transport/_requests_trio.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_user_agent_policy.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_custom_hook.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/conftest.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_redirect_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_http_logging_policy.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_retry.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/tracing_common.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_authentication.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_custom_hook_policy.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_polling.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_universal.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_tracing_policy.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_redirect.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_pipeline.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_retry_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/test_base_polling.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_base.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_universal_http.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_authentication_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_paging.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_base_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_stream_generator.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_utils.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_basic_transport.py
+Filename: azure-core-1.9.0/azure/core/pipeline/policies/_distributed_tracing.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_request_trio.py
+Filename: azure-core-1.9.0/azure/core/polling/_async_poller.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_request_asyncio.py
+Filename: azure-core-1.9.0/azure/core/polling/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_authentication.py
+Filename: azure-core-1.9.0/azure/core/polling/base_polling.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_tracing_decorator_async.py
+Filename: azure-core-1.9.0/azure/core/polling/_poller.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_retry_policy.py
+Filename: azure-core-1.9.0/azure/core/polling/async_base_polling.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_async_base_polling.py
+Filename: azure-core-1.9.0/azure/core/tracing/ext/
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_polling.py
+Filename: azure-core-1.9.0/azure/core/tracing/_abstract_span.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_http_logging_policy_async.py
+Filename: azure-core-1.9.0/azure/core/tracing/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/test_pipeline.py
+Filename: azure-core-1.9.0/azure/core/tracing/common.py
 Comment: 
 
-Filename: azure-core-1.8.2/tests/azure_core_asynctests/__init__.py
+Filename: azure-core-1.9.0/azure/core/tracing/decorator_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/not-zip-safe
+Filename: azure-core-1.9.0/azure/core/tracing/decorator.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/requires.txt
+Filename: azure-core-1.9.0/azure/core/tracing/ext/__init__.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/top_level.txt
+Filename: azure-core-1.9.0/samples/test_example_sansio.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/SOURCES.txt
+Filename: azure-core-1.9.0/samples/test_example_async.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/PKG-INFO
+Filename: azure-core-1.9.0/samples/test_example_sync.py
 Comment: 
 
-Filename: azure-core-1.8.2/azure_core.egg-info/dependency_links.txt
+Filename: azure-core-1.9.0/samples/conftest.py
+Comment: 
+
+Filename: azure-core-1.9.0/samples/README.md
 Comment: 
 
 Zip file comment:
```

## Comparing `azure-core-1.8.2/CLIENT_LIBRARY_DEVELOPER.md` & `azure-core-1.9.0/CLIENT_LIBRARY_DEVELOPER.md`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/CHANGELOG.md` & `azure-core-1.9.0/CHANGELOG.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,22 @@
 
 # Release History
 
+## 1.9.0 (2020-11-09)
+
+### Features
+
+- Add a `continuation_token` attribute to the base `AzureError` exception, and set this value for errors raised
+  during paged or long-running operations.
+
+### Bug Fixes
+
+- Set retry_interval to 1 second instead of 1000 seconds (thanks **vbarbaresi** for contributing)  #14357
+
+
 ## 1.8.2 (2020-10-05)
 
 ### Bug Fixes
 
 - Fixed bug to allow polling in the case of parameterized endpoints with relative polling urls  #14097
```

## Comparing `azure-core-1.8.2/README.md` & `azure-core-1.9.0/README.md`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/setup.py` & `azure-core-1.9.0/setup.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/PKG-INFO` & `azure-core-1.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: azure-core
-Version: 1.8.2
+Version: 1.9.0
 Summary: Microsoft Azure Core Library for Python
 Home-page: https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core
 Author: Microsoft Corporation
 Author-email: azpysdkhelp@microsoft.com
 License: MIT License
 Description: 
         # Azure Core shared client library for Python
@@ -154,14 +154,26 @@
         
         <!-- LINKS -->
         [package]: https://pypi.org/project/azure-core/
         
         
         # Release History
         
+        ## 1.9.0 (2020-11-09)
+        
+        ### Features
+        
+        - Add a `continuation_token` attribute to the base `AzureError` exception, and set this value for errors raised
+          during paged or long-running operations.
+        
+        ### Bug Fixes
+        
+        - Set retry_interval to 1 second instead of 1000 seconds (thanks **vbarbaresi** for contributing)  #14357
+        
+        
         ## 1.8.2 (2020-10-05)
         
         ### Bug Fixes
         
         - Fixed bug to allow polling in the case of parameterized endpoints with relative polling urls  #14097
```

## Comparing `azure-core-1.8.2/samples/test_example_sansio.py` & `azure-core-1.9.0/samples/test_example_sansio.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/samples/test_example_sync.py` & `azure-core-1.9.0/samples/test_example_sync.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/samples/conftest.py` & `azure-core-1.9.0/samples/conftest.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/samples/README.md` & `azure-core-1.9.0/samples/README.md`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/samples/test_example_async.py` & `azure-core-1.9.0/samples/test_example_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/credentials_async.py` & `azure-core-1.9.0/azure/core/credentials_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/_match_conditions.py` & `azure-core-1.9.0/azure/core/_match_conditions.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/paging.py` & `azure-core-1.9.0/azure/core/paging.py`

 * *Files 3% similar despite different names*

```diff
@@ -30,14 +30,16 @@
     TypeVar,
     Iterator,
     Iterable,
     Tuple,
 )
 import logging
 
+from .exceptions import AzureError
+
 
 _LOGGER = logging.getLogger(__name__)
 
 ReturnType = TypeVar("ReturnType")
 ResponseType = TypeVar("ResponseType")
 
 
@@ -66,16 +68,21 @@
         """Return 'self'."""
         return self
 
     def __next__(self):
         # type: () -> Iterator[ReturnType]
         if self.continuation_token is None and self._did_a_call_already:
             raise StopIteration("End of paging")
+        try:
+            self._response = self._get_next(self.continuation_token)
+        except AzureError as error:
+            if not error.continuation_token:
+                error.continuation_token = self.continuation_token
+            raise
 
-        self._response = self._get_next(self.continuation_token)
         self._did_a_call_already = True
 
         self.continuation_token, self._current_page = self._extract_data(self._response)
 
         return iter(self._current_page)
 
     next = __next__  # Python 2 compatibility.
```

## Comparing `azure-core-1.8.2/azure/core/_pipeline_client.py` & `azure-core-1.9.0/azure/core/_pipeline_client.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/configuration.py` & `azure-core-1.9.0/azure/core/configuration.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/exceptions.py` & `azure-core-1.9.0/azure/core/exceptions.py`

 * *Files 8% similar despite different names*

```diff
@@ -188,30 +188,33 @@
     """Base exception for all errors.
 
     :param message: The message object stringified as 'message' attribute
     :keyword error: The original exception if any
     :paramtype error: Exception
 
     :ivar inner_exception: The exception passed with the 'error' kwarg
-    :type inner_exception: Exception
+    :vartype inner_exception: Exception
     :ivar exc_type: The exc_type from sys.exc_info()
     :ivar exc_value: The exc_value from sys.exc_info()
     :ivar exc_traceback: The exc_traceback from sys.exc_info()
     :ivar exc_msg: A string formatting of message parameter, exc_type and exc_value
     :ivar str message: A stringified version of the message parameter
+    :ivar str continuation_token: A token reference to continue an incomplete operation. This value is optional
+     and will be `None` where continuation is either unavailable or not applicable.
     """
 
     def __init__(self, message, *args, **kwargs):
         self.inner_exception = kwargs.get("error")
         self.exc_type, self.exc_value, self.exc_traceback = sys.exc_info()
         self.exc_type = (
             self.exc_type.__name__ if self.exc_type else type(self.inner_exception)
         )
         self.exc_msg = "{}, {}: {}".format(message, self.exc_type, self.exc_value)
         self.message = str(message)
+        self.continuation_token = kwargs.get('continuation_token')
         super(AzureError, self).__init__(self.message, *args)
 
     def raise_with_traceback(self):
         try:
             raise super(AzureError, self).with_traceback(self.exc_traceback)
         except AttributeError:
             self.__traceback__ = self.exc_traceback
@@ -240,19 +243,23 @@
 
     :param message: HttpResponse's error message
     :type message: string
     :param response: The response that triggered the exception.
     :type response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
 
     :ivar reason: The HTTP response reason
-    :type reason: str
+    :vartype reason: str
     :ivar status_code: HttpResponse's status code
-    :type status_code: int
+    :vartype status_code: int
     :ivar response: The response that triggered the exception.
-    :type response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
+    :vartype response: ~azure.core.pipeline.transport.HttpResponse or ~azure.core.pipeline.transport.AsyncHttpResponse
+    :ivar model: The request body/response body model
+    :vartype model: ~msrest.serialization.Model
+    :ivar error: The formatted error
+    :vartype error: ODataV4Format
     """
 
     def __init__(self, message=None, response=None, **kwargs):
         # Don't want to document this one yet.
         error_format = kwargs.get("error_format", ODataV4Format)
 
         self.reason = None
```

## Comparing `azure-core-1.8.2/azure/core/async_paging.py` & `azure-core-1.9.0/azure/core/async_paging.py`

 * *Files 8% similar despite different names*

```diff
@@ -31,14 +31,16 @@
     TypeVar,
     Callable,
     Tuple,
     Optional,
     Awaitable,
 )
 
+from .exceptions import AzureError
+
 
 _LOGGER = logging.getLogger(__name__)
 
 ReturnType = TypeVar("ReturnType")
 ResponseType = TypeVar("ResponseType")
 
 __all__ = [
@@ -89,16 +91,21 @@
         self._did_a_call_already = False
         self._response = None
         self._current_page = None
 
     async def __anext__(self):
         if self.continuation_token is None and self._did_a_call_already:
             raise StopAsyncIteration("End of paging")
+        try:
+            self._response = await self._get_next(self.continuation_token)
+        except AzureError as error:
+            if not error.continuation_token:
+                error.continuation_token = self.continuation_token
+            raise
 
-        self._response = await self._get_next(self.continuation_token)
         self._did_a_call_already = True
 
         self.continuation_token, self._current_page = await self._extract_data(
             self._response
         )
 
         # If current_page was a sync list, wrap it async-like
```

## Comparing `azure-core-1.8.2/azure/core/_pipeline_client_async.py` & `azure-core-1.9.0/azure/core/_pipeline_client_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/credentials.py` & `azure-core-1.9.0/azure/core/credentials.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/settings.py` & `azure-core-1.9.0/azure/core/settings.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/__init__.py` & `azure-core-1.9.0/azure/core/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/_tools_async.py` & `azure-core-1.9.0/azure/core/pipeline/_tools_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/_base.py` & `azure-core-1.9.0/azure/core/pipeline/_base.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/_base_async.py` & `azure-core-1.9.0/azure/core/pipeline/_base_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/_tools.py` & `azure-core-1.9.0/azure/core/pipeline/_tools.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/__init__.py` & `azure-core-1.9.0/azure/core/pipeline/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_authentication.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_authentication.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_distributed_tracing.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_distributed_tracing.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_custom_hook.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_custom_hook.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_utils.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_utils.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_retry_async.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_retry_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_redirect.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_redirect.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_authentication_async.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_authentication_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_base.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_base.py`

 * *Files 0% similar despite different names*

```diff
@@ -77,15 +77,15 @@
         """
 
 
 class SansIOHTTPPolicy(Generic[HTTPRequestType, HTTPResponseType]):
     """Represents a sans I/O policy.
 
     SansIOHTTPPolicy is a base class for policies that only modify or
-    mutate a request based on the HTTP specification, and do no depend
+    mutate a request based on the HTTP specification, and do not depend
     on the specifics of any particular transport. SansIOHTTPPolicy
     subclasses will function in either a Pipeline or an AsyncPipeline,
     and can act either before the request is done, or after.
     You can optionally make these methods coroutines (or return awaitable objects)
     but they will then be tied to AsyncPipeline usage.
     """
```

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_base_async.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_base_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_redirect_async.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_redirect_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_universal.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_universal.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/_retry.py` & `azure-core-1.9.0/azure/core/pipeline/policies/_retry.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/policies/__init__.py` & `azure-core-1.9.0/azure/core/pipeline/policies/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_requests_trio.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_requests_trio.py`

 * *Files 1% similar despite different names*

```diff
@@ -91,15 +91,15 @@
                 raise StopAsyncIteration()
             except (requests.exceptions.ChunkedEncodingError,
                     requests.exceptions.ConnectionError):
                 retry_total -= 1
                 if retry_total <= 0:
                     retry_active = False
                 else:
-                    await trio.sleep(1000)
+                    await trio.sleep(1)
                     headers = {'range': 'bytes=' + str(self.downloaded) + '-'}
                     resp = self.pipeline.run(self.request, stream=True, headers=headers)
                     if resp.status_code == 416:
                         raise
                     try:
                         chunk = await trio.to_thread.run_sync(
                             _iterate_response_content,
```

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_base_requests_async.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_base_requests_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_base.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_base.py`

 * *Files 0% similar despite different names*

```diff
@@ -73,14 +73,15 @@
     PipelineContext,
 )
 from .._tools import await_result as _await_result
 
 
 if TYPE_CHECKING:
     from ..policies import SansIOHTTPPolicy
+    from collections.abc import MutableMapping
 
 HTTPResponseType = TypeVar("HTTPResponseType")
 HTTPRequestType = TypeVar("HTTPRequestType")
 PipelineType = TypeVar("PipelineType")
 
 _LOGGER = logging.getLogger(__name__)
 
@@ -509,15 +510,15 @@
     """
 
     def __init__(self, request, internal_response, block_size=None):
         # type: (HttpRequest, Any, Optional[int]) -> None
         self.request = request
         self.internal_response = internal_response
         self.status_code = None  # type: Optional[int]
-        self.headers = {}  # type: Dict[str, str]
+        self.headers = {}  # type: MutableMapping[str, str]
         self.reason = None  # type: Optional[str]
         self.content_type = None  # type: Optional[str]
         self.block_size = block_size or 4096  # Default to same as Requests
 
     def body(self):
         # type: () -> bytes
         """Return the whole body as bytes in memory.
```

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_base_async.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_base_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_requests_asyncio.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_requests_asyncio.py`

 * *Files 0% similar despite different names*

```diff
@@ -153,15 +153,15 @@
     def __len__(self):
         return self.content_length
 
     async def __anext__(self):
         loop = _get_running_loop()
         retry_active = True
         retry_total = 3
-        retry_interval = 1000
+        retry_interval = 1  # 1 second
         while retry_active:
             try:
                 chunk = await loop.run_in_executor(
                     None,
                     _iterate_response_content,
                     self.iter_content_func,
                 )
```

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/__init__.py` & `azure-core-1.9.0/azure/core/pipeline/transport/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_aiohttp.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_aiohttp.py`

 * *Files 0% similar despite different names*

```diff
@@ -25,14 +25,15 @@
 # --------------------------------------------------------------------------
 from typing import Any, Optional, AsyncIterator as AsyncIteratorType
 from collections.abc import AsyncIterator
 
 import logging
 import asyncio
 import aiohttp
+from multidict import CIMultiDict
 
 from requests.exceptions import (
     ChunkedEncodingError,
     StreamConsumedError)
 
 from azure.core.configuration import ConnectionConfiguration
 from azure.core.exceptions import ServiceRequestError, ServiceResponseError
@@ -212,15 +213,15 @@
 
     def __len__(self):
         return self.content_length
 
     async def __anext__(self):
         retry_active = True
         retry_total = 3
-        retry_interval = 1000
+        retry_interval = 1  # 1 second
         while retry_active:
             try:
                 chunk = await self.response.internal_response.content.read(self.block_size)
                 if not chunk:
                     raise _ResponseStopIteration()
                 self.downloaded += self.block_size
                 return chunk
@@ -260,15 +261,15 @@
     :param block_size: block size of data sent over connection.
     :type block_size: int
     """
     def __init__(self, request: HttpRequest, aiohttp_response: aiohttp.ClientResponse, block_size=None) -> None:
         super(AioHttpTransportResponse, self).__init__(request, aiohttp_response, block_size=block_size)
         # https://aiohttp.readthedocs.io/en/stable/client_reference.html#aiohttp.ClientResponse
         self.status_code = aiohttp_response.status
-        self.headers = aiohttp_response.headers
+        self.headers = CIMultiDict(aiohttp_response.headers)
         self.reason = aiohttp_response.reason
         self.content_type = aiohttp_response.headers.get('content-type')
         self._body = None
 
     def body(self) -> bytes:
         """Return the whole body as bytes in memory.
         """
@@ -303,10 +304,9 @@
     def __getstate__(self):
         # Be sure body is loaded in memory, otherwise not pickable and let it throw
         self.body()
 
         state = self.__dict__.copy()
         # Remove the unpicklable entries.
         state['internal_response'] = None  # aiohttp response are not pickable (see headers comments)
-        from multidict import CIMultiDict  # I know it's importable since aiohttp is loaded
         state['headers'] = CIMultiDict(self.headers)  # MultiDictProxy is not pickable
         return state
```

## Comparing `azure-core-1.8.2/azure/core/pipeline/transport/_requests_basic.py` & `azure-core-1.9.0/azure/core/pipeline/transport/_requests_basic.py`

 * *Files 3% similar despite different names*

```diff
@@ -39,14 +39,15 @@
 from . import HttpRequest # pylint: disable=unused-import
 
 from ._base import (
     HttpTransport,
     HttpResponse,
     _HttpResponseBase
 )
+from ._bigger_block_size_http_adapters import BiggerBlockSizeHTTPAdapter
 
 PipelineType = TypeVar("PipelineType")
 
 _LOGGER = logging.getLogger(__name__)
 
 
 class _RequestsTransportResponseBase(_HttpResponseBase):
@@ -113,15 +114,15 @@
 
     def __iter__(self):
         return self
 
     def __next__(self):
         retry_active = True
         retry_total = 3
-        retry_interval = 1000
+        retry_interval = 1  # 1 second
         while retry_active:
             try:
                 chunk = next(self.iter_content_func)
                 if not chunk:
                     raise StopIteration()
                 self.downloaded += self.block_size
                 return chunk
@@ -209,15 +210,15 @@
         # type: (requests.Session) -> None
         """Init session level configuration of requests.
 
         This is initialization I want to do once only on a session.
         """
         session.trust_env = self._use_env_settings
         disable_retries = Retry(total=False, redirect=False, raise_on_status=False)
-        adapter = requests.adapters.HTTPAdapter(max_retries=disable_retries)
+        adapter = BiggerBlockSizeHTTPAdapter(max_retries=disable_retries)
         for p in self._protocols:
             session.mount(p, adapter)
 
     def open(self):
         if not self.session and self._session_owner:
             self.session = requests.Session()
             self._init_session(self.session)
```

## Comparing `azure-core-1.8.2/azure/core/tracing/decorator_async.py` & `azure-core-1.9.0/azure/core/tracing/decorator_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/tracing/_abstract_span.py` & `azure-core-1.9.0/azure/core/tracing/_abstract_span.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/tracing/decorator.py` & `azure-core-1.9.0/azure/core/tracing/decorator.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/tracing/common.py` & `azure-core-1.9.0/azure/core/tracing/common.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/polling/async_base_polling.py` & `azure-core-1.9.0/azure/core/polling/async_base_polling.py`

 * *Files 2% similar despite different names*

```diff
@@ -39,31 +39,34 @@
 class AsyncLROBasePolling(LROBasePolling):
     """A subclass or LROBasePolling that redefine "run" as async.
     """
 
     async def run(self):  # pylint:disable=invalid-overridden-method
         try:
             await self._poll()
+
         except BadStatus as err:
             self._status = "Failed"
             raise HttpResponseError(
-                response=self._pipeline_response.http_response, error=err
+                response=self._pipeline_response.http_response,
+                error=err
             )
 
         except BadResponse as err:
             self._status = "Failed"
             raise HttpResponseError(
                 response=self._pipeline_response.http_response,
                 message=str(err),
-                error=err,
+                error=err
             )
 
         except OperationFailed as err:
             raise HttpResponseError(
-                response=self._pipeline_response.http_response, error=err
+                response=self._pipeline_response.http_response,
+                error=err
             )
 
     async def _poll(self):  # pylint:disable=invalid-overridden-method
         """Poll status of operation so long as operation is incomplete and
         we have an endpoint to query.
 
         :param callable update_cmd: The function to call to retrieve the
```

## Comparing `azure-core-1.8.2/azure/core/polling/_async_poller.py` & `azure-core-1.9.0/azure/core/polling/_async_poller.py`

 * *Files 11% similar despite different names*

```diff
@@ -19,22 +19,26 @@
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 #
 # --------------------------------------------------------------------------
+import logging
 from collections.abc import Awaitable
 from typing import Callable, Any, Tuple, Generic, TypeVar, Generator
 
+from ..exceptions import AzureError
 from ._poller import NoPolling as _NoPolling
 
 
 PollingReturnType = TypeVar("PollingReturnType")
 
+_LOGGER = logging.getLogger(__name__)
+
 
 class AsyncPollingMethod(Generic[PollingReturnType]):
     """ABC class for polling method.
     """
     def initialize(self, client: Any, initial_response: Any, deserialization_callback: Any) -> None:
         raise NotImplementedError("This method needs to be implemented")
 
@@ -173,15 +177,24 @@
         return self.result().__await__()
 
     async def wait(self) -> None:
         """Wait on the long running operation.
 
         :raises ~azure.core.exceptions.HttpResponseError: Server problem with the query.
         """
-        await self._polling_method.run()
+        try:
+            await self._polling_method.run()
+        except AzureError as error:
+            if not error.continuation_token:
+                try:
+                    error.continuation_token = self.continuation_token()
+                except Exception as err:  # pylint: disable=broad-except
+                    _LOGGER.warning("Unable to retrieve continuation token: %s", err)
+                    error.continuation_token = None
+            raise
         self._done = True
 
     def done(self) -> bool:
         """Check status of the long running operation.
 
         :returns: 'True' if the process has completed, else 'False'.
         :rtype: bool
```

## Comparing `azure-core-1.8.2/azure/core/polling/base_polling.py` & `azure-core-1.9.0/azure/core/polling/base_polling.py`

 * *Files 0% similar despite different names*

```diff
@@ -45,15 +45,14 @@
 
 
 try:
     ABC = abc.ABC
 except AttributeError:  # Python 2.7, abc exists, but not ABC
     ABC = abc.ABCMeta("ABC", (object,), {"__slots__": ()})  # type: ignore
 
-
 _FINISHED = frozenset(["succeeded", "canceled", "failed"])
 _FAILED = frozenset(["canceled", "failed"])
 _SUCCEEDED = frozenset(["succeeded"])
 
 def _finished(status):
     if hasattr(status, "value"):
         status = status.value
@@ -477,31 +476,34 @@
         # Restore the transport in the context
         initial_response.context.transport = client._pipeline._transport  # pylint: disable=protected-access
         return client, initial_response, deserialization_callback
 
     def run(self):
         try:
             self._poll()
+
         except BadStatus as err:
             self._status = "Failed"
             raise HttpResponseError(
-                response=self._pipeline_response.http_response, error=err
+                response=self._pipeline_response.http_response,
+                error=err
             )
 
         except BadResponse as err:
             self._status = "Failed"
             raise HttpResponseError(
                 response=self._pipeline_response.http_response,
                 message=str(err),
-                error=err,
+                error=err
             )
 
         except OperationFailed as err:
             raise HttpResponseError(
-                response=self._pipeline_response.http_response, error=err
+                response=self._pipeline_response.http_response,
+                error=err
             )
 
     def _poll(self):
         """Poll status of operation so long as operation is incomplete and
         we have an endpoint to query.
 
         :param callable update_cmd: The function to call to retrieve the
```

## Comparing `azure-core-1.8.2/azure/core/polling/__init__.py` & `azure-core-1.9.0/azure/core/polling/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure/core/polling/_poller.py` & `azure-core-1.9.0/azure/core/polling/_poller.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,31 +20,35 @@
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 # IN THE SOFTWARE.
 #
 # --------------------------------------------------------------------------
 import base64
+import logging
 import threading
 import uuid
 try:
     from urlparse import urlparse # type: ignore # pylint: disable=unused-import
 except ImportError:
     from urllib.parse import urlparse
 
 from typing import TYPE_CHECKING, TypeVar, Generic
+from azure.core.exceptions import AzureError
 from azure.core.tracing.decorator import distributed_trace
 from azure.core.tracing.common import with_current_context
 
 if TYPE_CHECKING:
     from typing import Any, Callable, Union, List, Optional, Tuple
 
 
 PollingReturnType = TypeVar("PollingReturnType")
 
+_LOGGER = logging.getLogger(__name__)
+
 
 class PollingMethod(Generic[PollingReturnType]):
     """ABC class for polling method.
     """
     def initialize(self, client, initial_response, deserialization_callback):
         # type: (Any, Any, Any) -> None
         raise NotImplementedError("This method needs to be implemented")
@@ -182,16 +186,25 @@
         On completion, runs any callbacks.
 
         :param callable update_cmd: The API request to check the status of
          the operation.
         """
         try:
             self._polling_method.run()
-        except Exception as err: #pylint: disable=broad-except
-            self._exception = err
+        except AzureError as error:
+            if not error.continuation_token:
+                try:
+                    error.continuation_token = self.continuation_token()
+                except Exception as err:  # pylint: disable=broad-except
+                    _LOGGER.warning("Unable to retrieve continuation token: %s", err)
+                    error.continuation_token = None
+
+            self._exception = error
+        except Exception as error:  # pylint: disable=broad-except
+            self._exception = error
 
         finally:
             self._done.set()
 
         callbacks, self._callbacks = self._callbacks, []
         while callbacks:
             for call in callbacks:
```

## Comparing `azure-core-1.8.2/doc/azure.core.rst` & `azure-core-1.9.0/doc/azure.core.rst`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/doc/azure.core.tracing.rst` & `azure-core-1.9.0/doc/azure.core.tracing.rst`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_paging.py` & `azure-core-1.9.0/tests/test_paging.py`

 * *Files 9% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 #
 #--------------------------------------------------------------------------
 
 from azure.core.paging import ItemPaged
+from azure.core.exceptions import HttpResponseError
 
 import pytest
 
 
 class TestPaging(object):
 
     def test_basic_paging(self):
@@ -138,7 +139,25 @@
             }
         def extract_data(response):
             return response['nextLink'], iter(response['value'] or [])
 
         pager = ItemPaged(get_next, extract_data)
         output = repr(pager)
         assert output.startswith('<iterator object azure.core.paging.ItemPaged at')
+
+    def test_paging_continue_on_error(self):
+        def get_next(continuation_token=None):
+            if not continuation_token:
+                return {
+                    'nextLink': 'foo',
+                    'value': ['bar']
+                }
+            else:
+                raise HttpResponseError()
+        def extract_data(response):
+            return response['nextLink'], iter(response['value'] or [])
+        
+        pager = ItemPaged(get_next, extract_data)
+        assert next(pager) == 'bar'
+        with pytest.raises(HttpResponseError) as err:
+            next(pager)
+        assert err.value.continuation_token == 'foo'
```

## Comparing `azure-core-1.8.2/tests/test_tracing_decorator.py` & `azure-core-1.9.0/tests/test_tracing_decorator.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_stream_generator.py` & `azure-core-1.9.0/tests/test_stream_generator.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_exceptions.py` & `azure-core-1.9.0/tests/test_exceptions.py`

 * *Files 6% similar despite different names*

```diff
@@ -95,14 +95,24 @@
         assert str(error) == "Specific error message"
         assert error.message == "Specific error message"
         assert error.response is None
         assert error.reason is None
         assert error.error is None
         assert error.status_code is None
 
+    def test_error_continuation_token(self):
+        error = HttpResponseError(message="Specific error message", continuation_token='foo')
+        assert str(error) == "Specific error message"
+        assert error.message == "Specific error message"
+        assert error.response is None
+        assert error.reason is None
+        assert error.error is None
+        assert error.status_code is None
+        assert error.continuation_token == 'foo'
+
     def test_deserialized_httpresponse_error_code(self):
         """This is backward compat support of autorest azure-core (KV 4.0.0, Storage 12.0.0).
 
         Do NOT adapt this test unless you know what you're doing.
         """
         message = {
             "error": {
```

## Comparing `azure-core-1.8.2/tests/test_basic_transport.py` & `azure-core-1.9.0/tests/test_basic_transport.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_error_map.py` & `azure-core-1.9.0/tests/test_error_map.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_universal_pipeline.py` & `azure-core-1.9.0/tests/test_universal_pipeline.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_request_id_policy.py` & `azure-core-1.9.0/tests/test_request_id_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_settings.py` & `azure-core-1.9.0/tests/test_settings.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_authentication.py` & `azure-core-1.9.0/tests/test_authentication.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_retry_policy.py` & `azure-core-1.9.0/tests/test_retry_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_requests_universal.py` & `azure-core-1.9.0/tests/test_requests_universal.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_user_agent_policy.py` & `azure-core-1.9.0/tests/test_user_agent_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/conftest.py` & `azure-core-1.9.0/tests/conftest.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_http_logging_policy.py` & `azure-core-1.9.0/tests/test_http_logging_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/tracing_common.py` & `azure-core-1.9.0/tests/tracing_common.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_custom_hook_policy.py` & `azure-core-1.9.0/tests/test_custom_hook_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_polling.py` & `azure-core-1.9.0/tests/test_polling.py`

 * *Files 4% similar despite different names*

```diff
@@ -29,14 +29,15 @@
 except ImportError:
     import mock
 
 import pytest
 import six
 
 from azure.core import PipelineClient
+from azure.core.exceptions import ServiceResponseError
 from azure.core.polling import *
 from azure.core.polling.base_polling import (
     LROBasePolling, LocationPolling
 )
 from msrest.serialization import Model
 from azure.core.pipeline import PipelineResponse
 from azure.core.pipeline.transport import HttpResponse
@@ -234,7 +235,26 @@
 
     method = NoPollingError()
     poller = LROPoller(client, initial_response, deserialization_callback, method)
 
     with pytest.raises(ValueError) as excinfo:
         poller.result()
     assert "Something bad happened" in str(excinfo.value)
+
+
+def test_poller_error_continuation(client):
+
+    class NoPollingError(PollingTwoSteps):
+        def run(self):
+            raise ServiceResponseError("Something bad happened")
+
+    initial_response = "Initial response"
+    def deserialization_callback(response):
+        return "Treated: "+response
+
+    method = NoPollingError()
+    poller = LROPoller(client, initial_response, deserialization_callback, method)
+
+    with pytest.raises(ServiceResponseError) as excinfo:
+        poller.result()
+    assert "Something bad happened" in str(excinfo.value)
+    assert excinfo.value.continuation_token == "Initial response"
```

## Comparing `azure-core-1.8.2/tests/test_tracing_policy.py` & `azure-core-1.9.0/tests/test_tracing_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_pipeline.py` & `azure-core-1.9.0/tests/test_pipeline.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/test_base_polling.py` & `azure-core-1.9.0/tests/test_base_polling.py`

 * *Files 1% similar despite different names*

```diff
@@ -19,18 +19,20 @@
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 #
 #--------------------------------------------------------------------------
+import base64
 import datetime
 import json
 import re
 import types
+import pickle
 import platform
 import unittest
 import six
 try:
     from unittest import mock
 except ImportError:
     import mock
@@ -46,14 +48,15 @@
 from azure.core import PipelineClient
 from azure.core.pipeline import PipelineResponse, Pipeline, PipelineContext
 from azure.core.pipeline.transport import RequestsTransportResponse, HttpTransport
 
 from azure.core.polling.base_polling import LROBasePolling
 from azure.core.pipeline.policies._utils import _FixedOffset
 
+
 class SimpleResource:
     """An implementation of Python 3 SimpleNamespace.
     Used to deserialize resource objects from response bodies where
     no particular object type has been specified.
     """
 
     def __init__(self, **kwargs):
@@ -309,15 +312,15 @@
     @staticmethod
     def mock_send(method, status, headers=None, body=RESPONSE_BODY):
         if headers is None:
             headers = {}
         response = Response()
         response._content_consumed = True
         response._content = json.dumps(body).encode('ascii') if body is not None else None
-        response.request = mock.create_autospec(Request)
+        response.request = Request()
         response.request.method = method
         response.request.url = RESOURCE_URL
         response.request.headers = {
             'x-ms-client-request-id': '67f4dd4e-6262-45e1-8bed-5c45cf23b6d9'
         }
         response.status_code = status
         response.headers = headers
@@ -665,13 +668,14 @@
         POLLING_STATUS = 203
         response = TestBasePolling.mock_send(
             'POST', 202,
             {'location': LOCATION_URL})
         poll = LROPoller(CLIENT, response,
             TestBasePolling.mock_outputs,
             LROBasePolling(0))
-        with pytest.raises(HttpResponseError): # TODO: Node.js raises on deserialization
+        with pytest.raises(HttpResponseError) as error: # TODO: Node.js raises on deserialization
             poll.result()
+        assert error.value.continuation_token == base64.b64encode(pickle.dumps(response)).decode('ascii')
 
         LOCATION_BODY = json.dumps({ 'name': TEST_NAME })
         POLLING_STATUS = 200
```

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_universal_http.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_universal_http.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_paging.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_paging.py`

 * *Files 24% similar despite different names*

```diff
@@ -23,14 +23,15 @@
 # THE SOFTWARE.
 #
 #--------------------------------------------------------------------------
 
 from typing import AsyncIterator, TypeVar, List
 
 from azure.core.async_paging import AsyncItemPaged, AsyncList
+from azure.core.exceptions import HttpResponseError
 
 import pytest
 
 
 T = TypeVar("T")
 
 
@@ -116,7 +117,27 @@
         async def extract_data(response):
             return response['nextLink'], AsyncList(response['value'] or [])
 
         pager = AsyncItemPaged(get_next, extract_data)
         result_iterated = await _as_list(pager)
 
         assert len(result_iterated) == 0
+
+
+    @pytest.mark.asyncio
+    async def test_paging_continue_on_error(self):
+        async def get_next(continuation_token=None):
+            if not continuation_token:
+                return {
+                    'nextLink': 'foo',
+                    'value': ['bar']
+                }
+            else:
+                raise HttpResponseError()
+        async def extract_data(response):
+            return response['nextLink'], iter(response['value'] or [])
+        
+        pager = AsyncItemPaged(get_next, extract_data)
+        assert await pager.__anext__() == 'bar'
+        with pytest.raises(HttpResponseError) as err:
+            await pager.__anext__()
+        assert err.value.continuation_token == 'foo'
```

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_stream_generator.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_stream_generator.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_basic_transport.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_basic_transport.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_request_trio.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_request_trio.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_request_asyncio.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_request_asyncio.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_authentication.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_authentication.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_tracing_decorator_async.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_tracing_decorator_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_retry_policy.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_retry_policy.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_async_base_polling.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_async_base_polling.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,16 +19,17 @@
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 #
 #--------------------------------------------------------------------------
-
+import base64
 import json
+import pickle
 import re
 import types
 import unittest
 try:
     from unittest import mock
 except ImportError:
     import mock
@@ -286,15 +287,15 @@
     @staticmethod
     def mock_send(method, status, headers=None, body=RESPONSE_BODY):
         if headers is None:
             headers = {}
         response = Response()
         response._content_consumed = True
         response._content = json.dumps(body).encode('ascii') if body is not None else None
-        response.request = mock.create_autospec(Request)
+        response.request = Request()
         response.request.method = method
         response.request.url = RESOURCE_URL
         response.request.headers = {
             'x-ms-client-request-id': '67f4dd4e-6262-45e1-8bed-5c45cf23b6d9'
         }
         response.status_code = status
         response.headers = headers
@@ -656,13 +657,14 @@
     POLLING_STATUS = 203
     response = TestBasePolling.mock_send(
         'POST', 202,
         {'location': LOCATION_URL})
     poll = async_poller(CLIENT, response,
         TestBasePolling.mock_outputs,
         AsyncLROBasePolling(0))
-    with pytest.raises(HttpResponseError): # TODO: Node.js raises on deserialization
+    with pytest.raises(HttpResponseError) as error: # TODO: Node.js raises on deserialization
         await poll
+    assert error.value.continuation_token == base64.b64encode(pickle.dumps(response)).decode('ascii')
 
     LOCATION_BODY = json.dumps({ 'name': TEST_NAME })
     POLLING_STATUS = 200
```

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_polling.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_polling.py`

 * *Files 17% similar despite different names*

```diff
@@ -30,14 +30,15 @@
 except ImportError:
     import mock
 
 import pytest
 
 from azure.core import AsyncPipelineClient
 from azure.core.polling import *
+from azure.core.exceptions import ServiceResponseError
 from msrest.serialization import Model
 
 
 @pytest.fixture
 def client():
     # The poller itself don't use it, so we don't need something functionnal
     return AsyncPipelineClient("https://baseurl")
@@ -193,7 +194,27 @@
 
     method = NoPollingError()
     poller = AsyncLROPoller(client, initial_response, deserialization_callback, method)
 
     with pytest.raises(ValueError) as excinfo:
         await poller.result()
     assert "Something bad happened" in str(excinfo.value)
+
+
+@pytest.mark.asyncio
+async def test_async_poller_error_continuation(client):
+
+    class NoPollingError(PollingTwoSteps):
+        async def run(self):
+            raise ServiceResponseError("Something bad happened")
+
+    initial_response = "Initial response"
+    def deserialization_callback(response):
+        return "Treated: "+response
+
+    method = NoPollingError()
+    poller = AsyncLROPoller(client, initial_response, deserialization_callback, method)
+
+    with pytest.raises(ServiceResponseError) as excinfo:
+        await poller.result()
+    assert "Something bad happened" in str(excinfo.value)
+    assert excinfo.value.continuation_token == "Initial response"
```

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_http_logging_policy_async.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_http_logging_policy_async.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/test_pipeline.py` & `azure-core-1.9.0/tests/azure_core_asynctests/test_pipeline.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/tests/azure_core_asynctests/__init__.py` & `azure-core-1.9.0/tests/azure_core_asynctests/__init__.py`

 * *Files identical despite different names*

## Comparing `azure-core-1.8.2/azure_core.egg-info/SOURCES.txt` & `azure-core-1.9.0/azure_core.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -37,14 +37,15 @@
 azure/core/pipeline/policies/_universal.py
 azure/core/pipeline/policies/_utils.py
 azure/core/pipeline/transport/__init__.py
 azure/core/pipeline/transport/_aiohttp.py
 azure/core/pipeline/transport/_base.py
 azure/core/pipeline/transport/_base_async.py
 azure/core/pipeline/transport/_base_requests_async.py
+azure/core/pipeline/transport/_bigger_block_size_http_adapters.py
 azure/core/pipeline/transport/_requests_asyncio.py
 azure/core/pipeline/transport/_requests_basic.py
 azure/core/pipeline/transport/_requests_trio.py
 azure/core/polling/__init__.py
 azure/core/polling/_async_poller.py
 azure/core/polling/_poller.py
 azure/core/polling/async_base_polling.py
```

## Comparing `azure-core-1.8.2/azure_core.egg-info/PKG-INFO` & `azure-core-1.9.0/azure_core.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: azure-core
-Version: 1.8.2
+Version: 1.9.0
 Summary: Microsoft Azure Core Library for Python
 Home-page: https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/core/azure-core
 Author: Microsoft Corporation
 Author-email: azpysdkhelp@microsoft.com
 License: MIT License
 Description: 
         # Azure Core shared client library for Python
@@ -154,14 +154,26 @@
         
         <!-- LINKS -->
         [package]: https://pypi.org/project/azure-core/
         
         
         # Release History
         
+        ## 1.9.0 (2020-11-09)
+        
+        ### Features
+        
+        - Add a `continuation_token` attribute to the base `AzureError` exception, and set this value for errors raised
+          during paged or long-running operations.
+        
+        ### Bug Fixes
+        
+        - Set retry_interval to 1 second instead of 1000 seconds (thanks **vbarbaresi** for contributing)  #14357
+        
+        
         ## 1.8.2 (2020-10-05)
         
         ### Bug Fixes
         
         - Fixed bug to allow polling in the case of parameterized endpoints with relative polling urls  #14097
```

