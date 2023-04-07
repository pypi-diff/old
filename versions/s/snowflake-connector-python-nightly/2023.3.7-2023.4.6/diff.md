# Comparing `tmp/snowflake-connector-python-nightly-2023.3.7.tar.gz` & `tmp/snowflake-connector-python-nightly-2023.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "snowflake-connector-python-nightly-2023.3.7.tar", last modified: Tue Mar  7 04:07:04 2023, max compression
+gzip compressed data, was "snowflake-connector-python-nightly-2023.4.6.tar", last modified: Thu Apr  6 04:07:01 2023, max compression
```

## Comparing `snowflake-connector-python-nightly-2023.3.7.tar` & `snowflake-connector-python-nightly-2023.4.6.tar`

### file list

```diff
@@ -1,199 +1,200 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.213137 snowflake-connector-python-nightly-2023.3.7/
--rw-r--r--   0 runner    (1001) docker     (123)     1480 2023-03-07 04:06:48.000000 snowflake-connector-python-nightly-2023.3.7/CONTRIBUTING.md
--rw-r--r--   0 runner    (1001) docker     (123)    45096 2023-03-07 04:06:48.000000 snowflake-connector-python-nightly-2023.3.7/DESCRIPTION.md
--rw-r--r--   0 runner    (1001) docker     (123)    11365 2023-03-07 04:06:48.000000 snowflake-connector-python-nightly-2023.3.7/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      578 2023-03-07 04:06:48.000000 snowflake-connector-python-nightly-2023.3.7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)      457 2023-03-07 04:06:49.000000 snowflake-connector-python-nightly-2023.3.7/NOTICE
--rw-r--r--   0 runner    (1001) docker     (123)     2142 2023-03-07 04:07:04.213137 snowflake-connector-python-nightly-2023.3.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3045 2023-03-07 04:06:49.000000 snowflake-connector-python-nightly-2023.3.7/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      308 2023-03-07 04:06:49.000000 snowflake-connector-python-nightly-2023.3.7/SECURITY.md
--rw-r--r--   0 runner    (1001) docker     (123)      696 2023-03-07 04:06:49.000000 snowflake-connector-python-nightly-2023.3.7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     3056 2023-03-07 04:07:04.213137 snowflake-connector-python-nightly-2023.3.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     8234 2023-03-07 04:06:49.000000 snowflake-connector-python-nightly-2023.3.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.197137 snowflake-connector-python-nightly-2023.3.7/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.193137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.201137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/
--rw-r--r--   0 runner    (1001) docker     (123)     1692 2023-03-07 04:06:50.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/_sql_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     4888 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/arrow_context.py
--rw-r--r--   0 runner    (1001) docker     (123)     6959 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/arrow_iterator.pyx
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.201137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/
--rw-r--r--   0 runner    (1001) docker     (123)      991 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    27245 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     6999 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/by_plugin.py
--rw-r--r--   0 runner    (1001) docker     (123)     1016 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/default.py
--rw-r--r--   0 runner    (1001) docker     (123)     2006 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/idtoken.py
--rw-r--r--   0 runner    (1001) docker     (123)     6369 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/keypair.py
--rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/oauth.py
--rw-r--r--   0 runner    (1001) docker     (123)    10609 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/okta.py
--rw-r--r--   0 runner    (1001) docker     (123)     1955 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/usrpwdmfa.py
--rw-r--r--   0 runner    (1001) docker     (123)    13573 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/webbrowser.py
--rw-r--r--   0 runner    (1001) docker     (123)     9873 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/azure_storage_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/bind_upload_agent.py
--rw-r--r--   0 runner    (1001) docker     (123)    20410 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     2894 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/compat.py
--rw-r--r--   0 runner    (1001) docker     (123)    63767 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)    30347 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/connection_diagnostic.py
--rw-r--r--   0 runner    (1001) docker     (123)     8702 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    25717 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter.py
--rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter_issue23517.py
--rw-r--r--   0 runner    (1001) docker     (123)      437 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter_null.py
--rw-r--r--   0 runner    (1001) docker     (123)     7633 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter_snowsql.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.193137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.205137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/
--rw-r--r--   0 runner    (1001) docker     (123)      651 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      555 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)      565 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      512 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)    14375 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.hpp
--rw-r--r--   0 runner    (1001) docker     (123)      443 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowIterator.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowIterator.hpp
--rw-r--r--   0 runner    (1001) docker     (123)    34612 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     5606 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DateConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DateConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     1625 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     1032 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      800 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)      472 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/IColumnConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)      240 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/IntConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     1687 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/IntConverter.hpp
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.205137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/
--rw-r--r--   0 runner    (1001) docker     (123)      218 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Common.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     2335 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Common.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     1457 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      939 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      884 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.hpp
--rw-r--r--   0 runner    (1001) docker     (123)      649 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/StringConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)      555 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/StringConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)      241 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     1838 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeConverter.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     9470 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     4063 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.hpp
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.205137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Util/
--rw-r--r--   0 runner    (1001) docker     (123)      470 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Util/macros.hpp
--rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Util/time.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     2269 2023-03-07 04:06:53.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Util/time.hpp
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.205137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/Logging/
--rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/Logging/logging.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     1280 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/Logging/logging.hpp
--rw-r--r--   0 runner    (1001) docker     (123)    54238 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cursor.py
--rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/dbapi.py
--rw-r--r--   0 runner    (1001) docker     (123)      615 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/description.py
--rw-r--r--   0 runner    (1001) docker     (123)     9376 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/encryption_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/errorcode.py
--rw-r--r--   0 runner    (1001) docker     (123)    19004 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)      184 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/feature.py
--rw-r--r--   0 runner    (1001) docker     (123)     3245 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/file_compression_type.py
--rw-r--r--   0 runner    (1001) docker     (123)    46365 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/file_transfer_agent.py
--rw-r--r--   0 runner    (1001) docker     (123)     5427 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/file_util.py
--rw-r--r--   0 runner    (1001) docker     (123)    16071 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/gcs_storage_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     2802 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/gzip_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2919 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/local_storage_client.py
--rw-r--r--   0 runner    (1001) docker     (123)    39670 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/network.py
--rw-r--r--   0 runner    (1001) docker     (123)    18430 2023-03-07 04:06:51.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ocsp_asn1crypto.py
--rw-r--r--   0 runner    (1001) docker     (123)    68441 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ocsp_snowflake.py
--rw-r--r--   0 runner    (1001) docker     (123)     4672 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/options.py
--rw-r--r--   0 runner    (1001) docker     (123)    15817 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/pandas_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/proxy.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    24989 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/result_batch.py
--rw-r--r--   0 runner    (1001) docker     (123)     8796 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/result_set.py
--rw-r--r--   0 runner    (1001) docker     (123)    21830 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/s3_storage_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     5343 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/secret_detector.py
--rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/sfbinaryformat.py
--rw-r--r--   0 runner    (1001) docker     (123)    12449 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/sfdatetime.py
--rw-r--r--   0 runner    (1001) docker     (123)     4302 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/snow_logging.py
--rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/sqlstate.py
--rw-r--r--   0 runner    (1001) docker     (123)      813 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ssd_internal_keys.py
--rw-r--r--   0 runner    (1001) docker     (123)     4559 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ssl_wrap_socket.py
--rw-r--r--   0 runner    (1001) docker     (123)    16890 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/storage_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     8861 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/telemetry.py
--rw-r--r--   0 runner    (1001) docker     (123)    18837 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/telemetry_oob.py
--rw-r--r--   0 runner    (1001) docker     (123)      982 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/test_util.py
--rw-r--r--   0 runner    (1001) docker     (123)     2795 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/time_util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.205137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/dump_certs.py
--rw-r--r--   0 runner    (1001) docker     (123)     4575 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/dump_ocsp_response.py
--rw-r--r--   0 runner    (1001) docker     (123)     6601 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/dump_ocsp_response_cache.py
--rw-r--r--   0 runner    (1001) docker     (123)     2119 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/probe_connection.py
--rw-r--r--   0 runner    (1001) docker     (123)    10324 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/util_text.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.205137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.209137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/
--rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     4751 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      440 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1397 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/_internal_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    21313 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/adapters.py
--rw-r--r--   0 runner    (1001) docker     (123)     6377 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/api.py
--rw-r--r--   0 runner    (1001) docker     (123)    10187 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/auth.py
--rw-r--r--   0 runner    (1001) docker     (123)      429 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/certs.py
--rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/compat.py
--rw-r--r--   0 runner    (1001) docker     (123)    18560 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/cookies.py
--rw-r--r--   0 runner    (1001) docker     (123)     3813 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3885 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/help.py
--rw-r--r--   0 runner    (1001) docker     (123)      733 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/hooks.py
--rw-r--r--   0 runner    (1001) docker     (123)    35230 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/models.py
--rw-r--r--   0 runner    (1001) docker     (123)    30180 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/sessions.py
--rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/status_codes.py
--rw-r--r--   0 runner    (1001) docker     (123)     2912 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/structures.py
--rw-r--r--   0 runner    (1001) docker     (123)    33230 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.209137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/
--rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)     2763 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10811 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/_collections.py
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)    20070 2023-03-07 04:06:54.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)    39093 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/connectionpool.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.209137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      957 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_appengine_environ.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.209137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17632 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/bindings.py
--rw-r--r--   0 runner    (1001) docker     (123)    13922 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/low_level.py
--rw-r--r--   0 runner    (1001) docker     (123)    11010 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/appengine.py
--rw-r--r--   0 runner    (1001) docker     (123)     4538 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/ntlmpool.py
--rw-r--r--   0 runner    (1001) docker     (123)    16385 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/pyopenssl.py
--rw-r--r--   0 runner    (1001) docker     (123)    34416 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/securetransport.py
--rw-r--r--   0 runner    (1001) docker     (123)     7097 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/socks.py
--rw-r--r--   0 runner    (1001) docker     (123)     8217 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     8579 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/fields.py
--rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/filepost.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.209137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.209137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/backports/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/backports/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/backports/makefile.py
--rw-r--r--   0 runner    (1001) docker     (123)    34665 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/six.py
--rw-r--r--   0 runner    (1001) docker     (123)    19786 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/poolmanager.py
--rw-r--r--   0 runner    (1001) docker     (123)     5985 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/request.py
--rw-r--r--   0 runner    (1001) docker     (123)    28276 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/response.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.213137 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/
--rw-r--r--   0 runner    (1001) docker     (123)     1155 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4901 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/connection.py
--rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/proxy.py
--rw-r--r--   0 runner    (1001) docker     (123)      498 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/queue.py
--rw-r--r--   0 runner    (1001) docker     (123)     4225 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/request.py
--rw-r--r--   0 runner    (1001) docker     (123)     3510 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/response.py
--rw-r--r--   0 runner    (1001) docker     (123)    22001 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/retry.py
--rw-r--r--   0 runner    (1001) docker     (123)    17165 2023-03-07 04:06:55.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/ssl_.py
--rw-r--r--   0 runner    (1001) docker     (123)     5758 2023-03-07 04:06:56.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/ssl_match_hostname.py
--rw-r--r--   0 runner    (1001) docker     (123)     6895 2023-03-07 04:06:56.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/ssltransport.py
--rw-r--r--   0 runner    (1001) docker     (123)    10003 2023-03-07 04:06:56.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/timeout.py
--rw-r--r--   0 runner    (1001) docker     (123)    14270 2023-03-07 04:06:56.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/url.py
--rw-r--r--   0 runner    (1001) docker     (123)     5403 2023-03-07 04:06:56.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/wait.py
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-07 04:06:52.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-07 04:07:04.213137 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2142 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8794 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      322 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      623 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-03-07 04:07:04.000000 snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/
+-rw-r--r--   0 runner    (1001) docker     (123)     1479 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (123)    45999 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/DESCRIPTION.md
+-rw-r--r--   0 runner    (1001) docker     (123)    11365 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      578 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)      457 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/NOTICE
+-rw-r--r--   0 runner    (1001) docker     (123)     2142 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3045 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      308 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/SECURITY.md
+-rw-r--r--   0 runner    (1001) docker     (123)      696 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     3056 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     8269 2023-04-06 04:06:53.000000 snowflake-connector-python-nightly-2023.4.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.941984 snowflake-connector-python-nightly-2023.4.6/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.941984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.945984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/
+-rw-r--r--   0 runner    (1001) docker     (123)     1693 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/_sql_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4888 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/arrow_context.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6959 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/arrow_iterator.pyx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.945984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/
+-rw-r--r--   0 runner    (1001) docker     (123)      991 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27245 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6999 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/by_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1016 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/default.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2006 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/idtoken.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6369 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/keypair.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/oauth.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10609 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/okta.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1955 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/usrpwdmfa.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14011 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/webbrowser.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9873 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/azure_storage_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2355 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/bind_upload_agent.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20410 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2894 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/compat.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63767 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30347 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/connection_diagnostic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8703 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25717 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2822 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter_issue23517.py
+-rw-r--r--   0 runner    (1001) docker     (123)      437 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter_null.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7633 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter_snowsql.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.941984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.949984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/
+-rw-r--r--   0 runner    (1001) docker     (123)      651 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)      565 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      512 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)    14375 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)      443 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowIterator.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1793 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowIterator.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)    34612 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     5606 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DateConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DateConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1625 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1032 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      800 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)      472 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/IColumnConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)      240 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/IntConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1687 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/IntConverter.hpp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.949984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/
+-rw-r--r--   0 runner    (1001) docker     (123)      218 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Common.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     2335 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Common.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1457 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      939 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      884 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)      649 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/StringConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)      555 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/StringConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)      241 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1838 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeConverter.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     9470 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     4063 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.hpp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.949984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Util/
+-rw-r--r--   0 runner    (1001) docker     (123)      470 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Util/macros.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)     2013 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Util/time.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     2269 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Util/time.hpp
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.949984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/Logging/
+-rw-r--r--   0 runner    (1001) docker     (123)     3008 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/Logging/logging.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     1280 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/Logging/logging.hpp
+-rw-r--r--   0 runner    (1001) docker     (123)    54567 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cursor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/dbapi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      615 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/description.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9376 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/encryption_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2646 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/errorcode.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19004 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)      184 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/feature.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3246 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/file_compression_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)    46618 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/file_transfer_agent.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5427 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/file_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16068 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/gcs_storage_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2802 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/gzip_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2919 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/local_storage_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39670 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/network.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18430 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ocsp_asn1crypto.py
+-rw-r--r--   0 runner    (1001) docker     (123)    68441 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ocsp_snowflake.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4672 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16333 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/pandas_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1582 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/proxy.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    24990 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/result_batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8797 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/result_set.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21830 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/s3_storage_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5343 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/secret_detector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/sfbinaryformat.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12449 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/sfdatetime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4313 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/snow_logging.py
+-rw-r--r--   0 runner    (1001) docker     (123)      432 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/sqlstate.py
+-rw-r--r--   0 runner    (1001) docker     (123)      813 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ssd_internal_keys.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4559 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ssl_wrap_socket.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17320 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/storage_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8861 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/telemetry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18837 2023-04-06 04:06:54.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/telemetry_oob.py
+-rw-r--r--   0 runner    (1001) docker     (123)      982 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/test_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2795 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/time_util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.949984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/dump_certs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4575 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/dump_ocsp_response.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6601 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/dump_ocsp_response_cache.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2119 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/probe_connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1021 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/url_util.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10405 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/util_text.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.949984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.953984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/
+-rw-r--r--   0 runner    (1001) docker     (123)    10142 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     4751 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      440 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1397 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/_internal_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21313 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/adapters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6377 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10187 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)      429 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/certs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1451 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/compat.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18560 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/cookies.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3813 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3885 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/help.py
+-rw-r--r--   0 runner    (1001) docker     (123)      733 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/hooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35230 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30180 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/sessions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4235 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/status_codes.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2912 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/structures.py
+-rw-r--r--   0 runner    (1001) docker     (123)    33230 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.953984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     2763 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10811 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/_collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20070 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    39093 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/connectionpool.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.953984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      957 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_appengine_environ.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17632 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/bindings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13922 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/low_level.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11010 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/appengine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4538 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/ntlmpool.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16385 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/pyopenssl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34416 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/securetransport.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7097 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/socks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8217 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8579 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/filepost.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/backports/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/backports/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1417 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/backports/makefile.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34665 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/six.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19786 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/poolmanager.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5985 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/request.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28276 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/response.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/
+-rw-r--r--   0 runner    (1001) docker     (123)     1155 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4901 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/connection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1605 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/proxy.py
+-rw-r--r--   0 runner    (1001) docker     (123)      498 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4225 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3510 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/response.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22001 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/retry.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17165 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/ssl_.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5758 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/ssl_match_hostname.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6895 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/ssltransport.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10003 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/timeout.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14270 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/url.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5403 2023-04-06 04:06:56.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/wait.py
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-04-06 04:06:55.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 04:07:01.957984 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2142 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8830 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      322 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      623 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 04:07:01.000000 snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/top_level.txt
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/CONTRIBUTING.md` & `snowflake-connector-python-nightly-2023.4.6/CONTRIBUTING.md`

 * *Files 0% similar despite different names*

```diff
@@ -16,15 +16,15 @@
 ## I'd like to contribute the bug fix or feature myself
 
 We encourage everyone to first open an issue to discuss any feature work or bug fixes with one of the maintainers.
 This should help guide contributors through potential pitfalls.
 
 ### Setup a development environment
 
-What is a development environment? It's a [virtualenv](https://virtualenv.pypa.io) that has all of neccessary
+What is a development environment? It's a [virtualenv](https://virtualenv.pypa.io) that has all of necessary
 dependencies installed with `snowflake-connector-python` installed as an editable package.
 
 Setting up a development environment is super easy with this [one simple tox command](https://tox.wiki/en/latest/example/devenv.html).
 
 ```shell
 tox --devenv venv37 -e py37
 . venv37/bin/activate
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/DESCRIPTION.md` & `snowflake-connector-python-nightly-2023.4.6/DESCRIPTION.md`

 * *Files 2% similar despite different names*

```diff
@@ -4,14 +4,29 @@
 Snowflake Documentation is available at:
 https://docs.snowflake.com/
 
 Source code is also available at: https://github.com/snowflakedb/snowflake-connector-python
 
 # Release Notes
 
+- v3.0.3(TBD)
+
+  - Fixed a bug that prints error in logs for GET command on GCS.
+  - Added a parameter that allows users to skip file uploads to stage if file exists on stage and contents of the file match.
+  - Fixed a bug when writing a Pandas Dataframe with non-default index.
+
+- v3.0.2(March 23, 2023)
+
+  - Fixed a memory leak in the logging module of the Cython extension.
+  - Fixed a bug where the `put` command on AWS raised `AttributeError` when uploading file composed of multiple parts.
+  - Fixed a bug of incorrect type hints of `SnowflakeCursor.fetch_arrow_all` and `SnowflakeCursor.fetchall`.
+  - Fixed a bug where `snowflake.connector.util_text.split_statements` swallows the final line break in the case when there are no space between lines.
+  - Improved logging to mask tokens in case of errors.
+  - Validate SSO URL before opening it in the browser for External browser authenticator.
+
 - v3.0.1(February 28, 2023)
 
   - Improved the robustness of OCSP response caching to handle errors in cases of serialization and deserialization.
   - Updated async_executes method's doc-string.
   - Errors raised now have a query field that contains the SQL query that caused them when available.
   - Fixed a bug where MFA token caching would refuse to work until restarted instead of reauthenticating.
   - Replaced the dependency on setuptools in favor of packaging.
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/LICENSE.txt` & `snowflake-connector-python-nightly-2023.4.6/LICENSE.txt`

 * *Files 1% similar despite different names*

```diff
@@ -183,15 +183,15 @@
       replaced with your own identifying information. (Don't include
       the brackets!)  The text should be enclosed in the appropriate
       comment syntax for the file format. We also recommend that a
       file or class name and description of purpose be included on the
       same "printed page" as the copyright notice for easier
       identification within third-party archives.
 
-   Copyright (c) 2013-2019 Snowflake Computing, Inc.
+   Copyright (c) 2013-2023 Snowflake Computing, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/MANIFEST.in` & `snowflake-connector-python-nightly-2023.4.6/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/PKG-INFO` & `snowflake-connector-python-nightly-2023.4.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: snowflake-connector-python-nightly
-Version: 2023.3.7
+Version: 2023.4.6
 Summary: Nigthly build of Snowflake Connector for Python
 Home-page: https://www.snowflake.com/
 Author: Snowflake, Inc
 Author-email: snowflake-python-libraries-dl@snowflake.com
 License: Apache-2.0
 Project-URL: Documentation, https://docs.snowflake.com/en/user-guide/python-connector.html
 Project-URL: Source, https://github.com/keller00/snowflake-connector-python-nightlies/
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/README.md` & `snowflake-connector-python-nightly-2023.4.6/README.md`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/pyproject.toml` & `snowflake-connector-python-nightly-2023.4.6/pyproject.toml`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/setup.cfg` & `snowflake-connector-python-nightly-2023.4.6/setup.cfg`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/setup.py` & `snowflake-connector-python-nightly-2023.4.6/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -45,32 +45,33 @@
     import numpy
     import pyarrow
     from Cython.Build import cythonize
     from Cython.Distutils import build_ext
 
     _ABLE_TO_COMPILE_EXTENSIONS = True
 except ImportError:
-    warnings.warn("Cannot compile native C code, because of a missing build dependency")
+    warnings.warn(
+        "Cannot compile native C code, because of a missing build dependency",
+        stacklevel=1,
+    )
     _ABLE_TO_COMPILE_EXTENSIONS = False
 
 if _ABLE_TO_COMPILE_EXTENSIONS:
-
     pyarrow_version = tuple(int(x) for x in pyarrow.__version__.split("."))
     extensions = cythonize(
         [
             Extension(
                 name="snowflake.connector.arrow_iterator",
                 sources=[os.path.join(CONNECTOR_SRC_DIR, "arrow_iterator.pyx")],
             ),
         ],
         compile_time_env=dict(ARROW_LESS_THAN_8=pyarrow_version < (8,)),
     )
 
     class MyBuildExt(build_ext):
-
         # list of libraries that will be bundled with python connector,
         # this list should be carefully examined when pyarrow lib is
         # upgraded
         arrow_libs_to_copy = {
             "linux": [
                 "libarrow.so.1000",
                 "libarrow_dataset.so.1000",
@@ -203,11 +204,11 @@
                 ret.append(source)
 
             return ret
 
     cmd_class = {"build_ext": MyBuildExt}
 
 setup(
-    version="2023.03.07",
+    version="2023.04.06",
     ext_modules=extensions,
     cmdclass=cmd_class,
 )
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/__init__.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
+
 # Python Db API v2
 #
 from __future__ import annotations
 
 apilevel = "2.0"
 threadsafety = 2
 paramstyle = "pyformat"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/_sql_util.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/_sql_util.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import re
 
 from .constants import FileTransferType
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/arrow_context.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/arrow_context.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import decimal
 import time
 from datetime import datetime, timedelta, tzinfo
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/arrow_iterator.pyx` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/arrow_iterator.pyx`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 # distutils: language = c++
 # cython: language_level=3
 
 from cpython.ref cimport PyObject
 from cython.operator cimport dereference
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/__init__.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from ._auth import Auth, get_public_key_fingerprint, get_token_from_private_key
 from .by_plugin import AuthByPlugin, AuthType
 from .default import AuthByDefault
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/_auth.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/_auth.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import codecs
 import copy
 import json
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/by_plugin.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/by_plugin.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 """This module implements the base class for authenticator classes.
 
 Note:
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/default.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/default.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from typing import Any
 
 from .by_plugin import AuthByPlugin, AuthType
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/idtoken.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/idtoken.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from typing import TYPE_CHECKING, Any
 
 from ..network import ID_TOKEN_AUTHENTICATOR
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/keypair.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/keypair.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import base64
 import hashlib
 import os
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/oauth.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/oauth.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from typing import Any
 
 from ..network import OAUTH_AUTHENTICATOR
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/okta.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/okta.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import json
 import logging
 from typing import TYPE_CHECKING, Any
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/usrpwdmfa.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/usrpwdmfa.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 from typing import TYPE_CHECKING, Any
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/auth/webbrowser.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/auth/webbrowser.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import json
 import logging
 import os
@@ -19,23 +19,25 @@
     HTTP_HEADER_ACCEPT,
     HTTP_HEADER_CONTENT_TYPE,
     HTTP_HEADER_SERVICE_NAME,
     HTTP_HEADER_USER_AGENT,
 )
 from ..errorcode import (
     ER_IDP_CONNECTION_ERROR,
+    ER_INVALID_VALUE,
     ER_NO_HOSTNAME_FOUND,
     ER_UNABLE_TO_OPEN_BROWSER,
 )
 from ..errors import OperationalError
 from ..network import (
     CONTENT_TYPE_APPLICATION_JSON,
     EXTERNAL_BROWSER_AUTHENTICATOR,
     PYTHON_CONNECTOR_USER_AGENT,
 )
+from ..url_util import is_valid_url
 from . import Auth
 from .by_plugin import AuthByPlugin, AuthType
 
 if TYPE_CHECKING:
     from .. import SnowflakeConnection
 
 logger = logging.getLogger(__name__)
@@ -127,26 +129,37 @@
                         errno=ER_NO_HOSTNAME_FOUND,
                     )
                 else:
                     raise ex
             socket_connection.listen(0)  # no backlog
             callback_port = socket_connection.getsockname()[1]
 
+            logger.debug("step 1: query GS to obtain SSO url")
+            sso_url = self._get_sso_url(
+                conn, authenticator, service_name, account, callback_port, user
+            )
+
+            logger.debug("Validate SSO URL")
+            if not is_valid_url(sso_url):
+                self._handle_failure(
+                    conn=conn,
+                    ret={
+                        "code": ER_INVALID_VALUE,
+                        "message": (f"The SSO URL provided {sso_url} is invalid"),
+                    },
+                )
+                return
+
             print(
                 "Initiating login request with your identity provider. A "
                 "browser window should have opened for you to complete the "
                 "login. If you can't see it, check existing browser windows, "
                 "or your OS settings. Press CTRL+C to abort and try again..."
             )
 
-            logger.debug("step 1: query GS to obtain SSO url")
-            sso_url = self._get_sso_url(
-                conn, authenticator, service_name, account, callback_port, user
-            )
-
             logger.debug("step 2: open a browser")
             print(f"Going to open: {sso_url} to authenticate...")
             if not self._webbrowser.open_new(sso_url):
                 print(
                     "We were unable to open a browser window for you, "
                     "please open the url above manually then paste the "
                     "URL you are redirected to into the terminal."
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/azure_storage_client.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/azure_storage_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import json
 import os
 import xml.etree.ElementTree as ET
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/bind_upload_agent.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/bind_upload_agent.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import uuid
 from io import BytesIO
 from logging import getLogger
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cache.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cache.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import datetime
 import logging
 import os
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/compat.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/compat.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import collections.abc
 import decimal
 import html
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/connection.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/connection.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 import os
 import re
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/connection_diagnostic.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/connection_diagnostic.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import base64
 import ipaddress
 import json
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/constants.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/constants.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
+
 from __future__ import annotations
 
 from collections import defaultdict
 from enum import Enum, auto, unique
 from typing import TYPE_CHECKING, Any, Callable, DefaultDict, NamedTuple
 
 from .options import pyarrow as pa
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import binascii
 import decimal
 import time
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter_issue23517.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter_issue23517.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from datetime import datetime, time, timedelta, tzinfo
 from functools import partial
 from logging import getLogger
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/converter_snowsql.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/converter_snowsql.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import time
 from datetime import date, datetime, timedelta
 from logging import getLogger
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.cpp`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "BinaryConverter.hpp"
 #include <memory>
 
 namespace sf
 {
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BinaryConverter.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_BINARYCONVERTER_HPP
 #define PC_BINARYCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include "logging.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.cpp`

 * *Files 27% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "BooleanConverter.hpp"
 #include <memory>
 
 namespace sf
 {
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/BooleanConverter.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_BOOLEANCONVERTER_HPP
 #define PC_BOOLEANCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include <memory>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "CArrowChunkIterator.hpp"
 #include "SnowflakeType.hpp"
 #include "IntConverter.hpp"
 #include "StringConverter.hpp"
 #include "FloatConverter.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowChunkIterator.hpp`

 * *Files 3% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_ARROWCHUNKITERATOR_HPP
 #define PC_ARROWCHUNKITERATOR_HPP
 
 #include "CArrowIterator.hpp"
 #include "IColumnConverter.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowIterator.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowIterator.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_ARROWITERATOR_HPP
 #define PC_ARROWITERATOR_HPP
 
 #include "Python/Common.hpp"
 #include "logging.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "CArrowTableIterator.hpp"
 #include "SnowflakeType.hpp"
 #include "Python/Common.hpp"
 #include "Util/time.hpp"
 #include <memory>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/CArrowTableIterator.hpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_ARROWTABLEITERATOR_HPP
 #define PC_ARROWTABLEITERATOR_HPP
 
 #include "CArrowIterator.hpp"
 #include <string>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DateConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DateConverter.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "DateConverter.hpp"
 #include "Python/Helpers.hpp"
 #include <memory>
 
 namespace sf
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DateConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DateConverter.hpp`

 * *Files 8% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_DATECONVERTER_HPP
 #define PC_DATECONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include "Python/Common.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.cpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "Python/Common.hpp"
 #include "DecimalConverter.hpp"
 #include "Python/Helpers.hpp"
 #include <memory>
 #include <string>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/DecimalConverter.hpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_DECIMALCONVERTER_HPP
 #define PC_DECIMALCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include "Python/Common.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "FloatConverter.hpp"
 #include <memory>
 
 namespace sf
 {
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/FloatConverter.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_FLOATCONVERTER_HPP
 #define PC_FLOATCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include <memory>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/IntConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/IntConverter.hpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_INTCONVERTER_HPP
 #define PC_INTCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include <memory>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Common.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Common.hpp`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_PYTHON_COMMON_HPP
 #define PC_PYTHON_COMMON_HPP
 
 // Support for not having PY_SSIZE_T_CLEAN defined will end in Python 3.10. It causes
 //  argument parsing to not accept integers, leaving only Py_ssize_t as an option
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.cpp`

 * *Files 7% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "Helpers.hpp"
 #include "Common.hpp"
 #include <string>
 
 namespace sf
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Python/Helpers.hpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_PYTHON_HELPERS_HPP
 #define PC_PYTHON_HELPERS_HPP
 
 #include "logging.hpp"
 #include <string>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.cpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "SnowflakeType.hpp"
 
 namespace sf
 {
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/SnowflakeType.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_SNOWFLAKETYPE_HPP
 #define PC_SNOWFLAKETYPE_HPP
 
 #include <string>
 #include <algorithm>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/StringConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/StringConverter.cpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "StringConverter.hpp"
 #include <memory>
 
 namespace sf
 {
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/StringConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/StringConverter.hpp`

 * *Files 14% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_STRINGCONVERTER_HPP
 #define PC_STRINGCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include "logging.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeConverter.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_TIMECONVERTER_HPP
 #define PC_TIMECONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include "Python/Common.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "TimeStampConverter.hpp"
 #include "Python/Helpers.hpp"
 #include "Util/time.hpp"
 
 #include <cstdint>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/TimeStampConverter.hpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_TIMESTAMPCONVERTER_HPP
 #define PC_TIMESTAMPCONVERTER_HPP
 
 #include "IColumnConverter.hpp"
 #include "Python/Common.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Util/time.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Util/time.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "time.hpp"
 
 namespace sf
 {
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/ArrowIterator/Util/time.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/ArrowIterator/Util/time.hpp`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_UTIL_TIME_HPP
 #define PC_UTIL_TIME_HPP
 
 #include <string>
 #include "Python/Common.hpp"
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/Logging/logging.cpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/Logging/logging.cpp`

 * *Files 10% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #include "logging.hpp"
 #include "Python/Helpers.hpp"
 #include <cstdio>
 
 namespace sf
@@ -42,19 +42,25 @@
   }
 
   PyObject *logger = m_pyLogger.get();
   py::UniqueRef keywords(PyDict_New());
   py::UniqueRef call_log(PyObject_GetAttrString(logger, "log"));
 
   // prepare keyword args for snow_logger
-  PyDict_SetItemString(keywords.get(), "level", Py_BuildValue("i", level));
-  PyDict_SetItemString(keywords.get(), "path_name", Py_BuildValue("s", path_name));
-  PyDict_SetItemString(keywords.get(), "func_name", Py_BuildValue("s", func_name));
-  PyDict_SetItemString(keywords.get(), "line_num", Py_BuildValue("i", line_num));
-  PyDict_SetItemString(keywords.get(), "msg", Py_BuildValue("s", msg));
+  py::UniqueRef level_ref(Py_BuildValue("i", level));
+  py::UniqueRef path_name_ref(Py_BuildValue("s", path_name));
+  py::UniqueRef func_name_ref(Py_BuildValue("s", func_name));
+  py::UniqueRef line_num_ref(Py_BuildValue("i", line_num));
+  py::UniqueRef msg_ref(Py_BuildValue("s", msg));
+
+  PyDict_SetItemString(keywords.get(), "level", level_ref.get());
+  PyDict_SetItemString(keywords.get(), "path_name", path_name_ref.get());
+  PyDict_SetItemString(keywords.get(), "func_name", func_name_ref.get());
+  PyDict_SetItemString(keywords.get(), "line_num", line_num_ref.get());
+  PyDict_SetItemString(keywords.get(), "msg", msg_ref.get());
 
   // call snow_logging.SnowLogger.log()
   PyObject_Call(call_log.get(), Py_BuildValue("()"), keywords.get());
 }
 
 
 void Logger::debug(const char *path_name, const char *func_name, int line_num, const char *format, ...)
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cpp/Logging/logging.hpp` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cpp/Logging/logging.hpp`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 //
-// Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+// Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 //
 
 #ifndef PC_LOGGING_HPP
 #define PC_LOGGING_HPP
 
 #include "Python/Common.hpp"
 #include <string>
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/cursor.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/cursor.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import collections
 import logging
 import re
@@ -626,14 +626,15 @@
         _statement_params: dict[str, str] | None = None,
         _is_internal: bool = False,
         _describe_only: bool = False,
         _no_results: bool = False,
         _is_put_get: bool | None = None,
         _raise_put_get_error: bool = True,
         _force_put_overwrite: bool = False,
+        _skip_upload_on_content_match: bool = False,
         file_stream: IO[bytes] | None = None,
         num_statements: int | None = None,
     ) -> Self | dict[str, Any] | None:
         """Executes a command/query.
 
         Args:
             command: The SQL command to be executed.
@@ -656,14 +657,16 @@
             _no_results: This flag tells the back-end to not return the result, just fire the query and return the
                 response returned by Snowflake's server.
             _use_ijson: This flag doesn't do anything as ijson support has ended.
             _is_put_get: Force decision of this SQL query being a PUT, or GET command. This is detected otherwise.
             _raise_put_get_error: Whether to raise PUT and GET errors.
             _force_put_overwrite: If the SQL query is a PUT, then this flag can force overwriting of an already
                 existing file on stage.
+            _skip_upload_on_content_match: If the SQL query is a PUT with overwrite enabled, then this flag will skip upload
+                if the file contents match to ease concurrent uploads.
             file_stream: File-like object to be uploaded with PUT
             num_statements: Query level parameter submitted in _statement_params constraining exact number of
             statements being submitted (or 0 if submitting an uncounted number) when using a multi-statement query.
 
         Returns:
             The cursor itself, or None if some error happened, or the response returned
             by Snowflake if the _no_results flag is on.
@@ -794,14 +797,15 @@
                     get_callback=_get_callback,
                     get_azure_callback=_get_azure_callback,
                     get_callback_output_stream=_get_callback_output_stream,
                     show_progress_bar=_show_progress_bar,
                     raise_put_get_error=_raise_put_get_error,
                     force_put_overwrite=_force_put_overwrite
                     or data.get("overwrite", False),
+                    skip_upload_on_content_match=_skip_upload_on_content_match,
                     source_from_stream=file_stream,
                     multipart_threshold=data.get("threshold"),
                     use_s3_regional_url=self._connection.enable_stage_s3_privatelink_for_us_east_1,
                 )
                 sf_file_transfer_agent.execute()
                 data = sf_file_transfer_agent.result()
                 self._total_rowcount = len(data["rowset"]) if "rowset" in data else -1
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/dbapi.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/dbapi.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 """This module implements some constructors and singletons as required by the DB API v2.0 (PEP-249)."""
 
 from __future__ import annotations
 
 import datetime
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/description.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/description.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 """Various constants."""
 
 from __future__ import annotations
 
 import platform
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/encryption_util.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/encryption_util.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import base64
 import json
 import os
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/errorcode.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/errorcode.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 # network
 ER_FAILED_TO_CONNECT_TO_DB = 250001
 ER_CONNECTION_IS_CLOSED = 250002
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/errors.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/errors.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 import os
 import re
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/file_compression_type.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/file_compression_type.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
+
 from __future__ import annotations
 
 from typing import NamedTuple
 
 
 class CompressionType(NamedTuple):
     name: str
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/file_transfer_agent.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/file_transfer_agent.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import binascii
 import glob
 import mimetypes
@@ -131,14 +131,15 @@
     src_compression_type: CompressionType | None = None
     dst_compression_type: CompressionType = None
     require_compress: bool = False
     dst_file_name: str | None = None
     dst_file_size: int = -1
     intermediate_stream: IO[bytes] | None = None
     src_stream: IO[bytes] | None = None
+    skip_upload_on_content_match: bool = False
     # Specific to Downloads only
     local_location: str | None = None
 
 
 def _update_progress(
     file_name: str,
     start_time: float,
@@ -317,14 +318,15 @@
         put_callback_output_stream: IO[str] = sys.stdout,
         get_callback: type[SnowflakeProgressPercentage] | None = None,
         get_azure_callback: type[SnowflakeProgressPercentage] | None = None,
         get_callback_output_stream: IO[str] = sys.stdout,
         show_progress_bar: bool = True,
         raise_put_get_error: bool = True,
         force_put_overwrite: bool = True,
+        skip_upload_on_content_match: bool = False,
         multipart_threshold: int | None = None,
         source_from_stream: IO[bytes] | None = None,
         use_s3_regional_url: bool = False,
     ) -> None:
         self._cursor = cursor
         self._command = command
         self._ret = ret
@@ -341,14 +343,15 @@
         # when we have not checked whether we should use accelerate, this boolean is None
         # _use_accelerate_endpoint in SnowflakeFileTransferAgent could be passed to each SnowflakeS3RestClient
         # so we could avoid check accelerate configuration for each S3 client created for each file meta.
         self._use_accelerate_endpoint: bool | None = None
         self._raise_put_get_error = raise_put_get_error
         self._show_progress_bar = show_progress_bar
         self._force_put_overwrite = force_put_overwrite
+        self._skip_upload_on_content_match = skip_upload_on_content_match
         self._source_from_stream = source_from_stream
         # The list of self-sufficient file metas that are sent to
         # remote storage clients to get operated on.
         self._file_metadata: list[SnowflakeFileMeta] = []
         self._results: list[SnowflakeFileMeta] = []
         self._multipart_threshold = multipart_threshold or 67108864  # Historical value
         self._use_s3_regional_url = use_s3_regional_url
@@ -372,14 +375,15 @@
 
         if self._stage_location_type == LOCAL_FS:
             if not os.path.isdir(self._stage_info["location"]):
                 os.makedirs(self._stage_info["location"])
 
         for m in self._file_metadata:
             m.overwrite = self._overwrite
+            m.skip_upload_on_content_match = self._skip_upload_on_content_match
             m.sfagent = self
             if self._stage_location_type != LOCAL_FS:
                 m.put_callback = self._put_callback
                 m.put_azure_callback = self._put_azure_callback
                 m.put_callback_output_stream = self._put_callback_output_stream
                 m.get_callback = self._get_callback
                 m.get_azure_callback = self._get_azure_callback
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/file_util.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/file_util.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import base64
 import gzip
 import os
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/gcs_storage_client.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/gcs_storage_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import json
 import os
 from logging import getLogger
@@ -213,15 +213,15 @@
         meta.gcs_file_header_encryption_metadata = encryption_metadata
 
     def finish_download(self) -> None:
         super().finish_download()
         # Sadly, we can only determine the src file size after we've
         # downloaded it, unlike the other cloud providers where the
         # metadata can be read beforehand.
-        self.meta.src_file_size = os.path.getsize(self.intermediate_dst_path)
+        self.meta.src_file_size = os.path.getsize(self.full_dst_file_name)
 
     def _update_presigned_url(self) -> None:
         """Updates the file metas with presigned urls if any.
 
         Currently only the file metas generated for PUT/GET on a GCP account need the presigned urls.
         """
         logger.debug("Updating presigned url")
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/gzip_decoder.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/gzip_decoder.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import io
 import subprocess
 import zlib
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/local_storage_client.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/local_storage_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import os
 from logging import getLogger
 from math import ceil
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/network.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/network.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import collections
 import contextlib
 import gzip
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ocsp_asn1crypto.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ocsp_asn1crypto.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import os
 import platform
 import sys
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ocsp_snowflake.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ocsp_snowflake.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import codecs
 import json
 import os
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/options.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/options.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import importlib
 import sys
 import warnings
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/pandas_tools.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/pandas_tools.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import collections.abc
 import os
 import warnings
@@ -28,21 +28,23 @@
         sqlalchemy = None
 
 T = TypeVar("T", bound=collections.abc.Sequence)
 
 logger = getLogger(__name__)
 
 
-def chunk_helper(lst: T, n: int) -> Iterator[tuple[int, T]]:
+def chunk_helper(
+    lst: pandas.DataFrame, n: int
+) -> Iterator[tuple[int, pandas.DataFrame]]:
     """Helper generator to chunk a sequence efficiently with current index like if enumerate was called on sequence."""
     if len(lst) == 0:
         yield 0, lst
         return
     for i in range(0, len(lst), n):
-        yield int(i / n), lst[i : i + n]
+        yield int(i / n), lst.iloc[i : i + n]
 
 
 def build_location_helper(
     database: str | None, schema: str | None, name: str, quote_identifiers: bool
 ) -> str:
     """Helper to format table/stage/file format's location."""
     if quote_identifiers:
@@ -166,14 +168,27 @@
         raise ValueError(
             "Unsupported table type. Expected table types: temp/temporary, transient"
         )
 
     if chunk_size is None:
         chunk_size = len(df)
 
+    if not (
+        isinstance(df.index, pandas.RangeIndex)
+        and 1 == df.index.step
+        and 0 == df.index.start
+    ):
+        warnings.warn(
+            f"Pandas Dataframe has non-standard index of type {str(type(df.index))} which will not be written."
+            f" Consider changing the index to pd.RangeIndex(start=0,...,step=1) or "
+            f"call reset_index() to keep index as column(s)",
+            UserWarning,
+            stacklevel=2,
+        )
+
     cursor = conn.cursor()
     stage_location = build_location_helper(
         database=database,
         schema=schema,
         name=random_string(),
         quote_identifiers=quote_identifiers,
     )
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/proxy.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/proxy.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import os
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/result_batch.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/result_batch.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
+
 from __future__ import annotations
 
 import abc
 import io
 import json
 import time
 from base64 import b64decode
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/result_set.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/result_set.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
+
 from __future__ import annotations
 
 from collections import deque
 from concurrent.futures import Future
 from concurrent.futures.thread import ThreadPoolExecutor
 from logging import getLogger
 from typing import TYPE_CHECKING, Any, Callable, Deque, Iterable, Iterator
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/s3_storage_client.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/s3_storage_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import binascii
 import re
 import xml.etree.ElementTree as ET
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/secret_detector.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/secret_detector.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 """The secret detector detects sensitive information.
 
 It masks secrets that might be leaked from two potential avenues
     1. Out of Band Telemetry
     2. Logging
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/sfbinaryformat.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/sfbinaryformat.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from base64 import b16decode, b16encode, standard_b64encode
 
 from .errors import InternalError
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/sfdatetime.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/sfdatetime.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import time
 from collections import namedtuple
 from datetime import date, datetime, timedelta
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/snow_logging.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/snow_logging.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 import warnings
 from collections.abc import Mapping
@@ -63,15 +63,15 @@
         func_name: str | None = None,
         *args: Any,
         **kwargs: Any,
     ) -> None:
         warnings.warn(
             "The 'warn' method is deprecated, " "use 'warning' instead",
             DeprecationWarning,
-            2,
+            stacklevel=2,
         )
         self.warning(msg, path_name, func_name, *args, **kwargs)
 
     def error(  # type: ignore[override]
         self,
         msg: str,
         path_name: str | None = None,
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ssd_internal_keys.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ssd_internal_keys.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from binascii import unhexlify
 
 # key version
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/ssl_wrap_socket.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/ssl_wrap_socket.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 #
 # SSL wrap socket for PyOpenSSL.
 # Mostly copied from
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/storage_client.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/storage_client.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import os
 import shutil
 import tempfile
@@ -182,16 +182,19 @@
         """
         pass
 
     def preprocess(self) -> None:
         meta = self.meta
         logger.debug(f"Preprocessing {meta.src_file_name}")
 
+        file_header = self.get_file_header(
+            meta.dst_file_name
+        )  # check if file exists on remote
         if not meta.overwrite:
-            self.get_file_header(meta.dst_file_name)  # Check if file exists on remote
+            self.get_digest()  # self.get_file_header needs digest for multiparts upload when aws is used.
             if meta.result_status == ResultStatus.UPLOADED:
                 # Skipped
                 logger.debug(
                     f'file already exists location="{self.stage_info["location"]}", '
                     f'file_name="{meta.dst_file_name}"'
                 )
                 meta.dst_file_size = 0
@@ -199,14 +202,22 @@
                 self.preprocessed = True
                 return
         # Uploading
         if meta.require_compress:
             self.compress()
         self.get_digest()
 
+        if (
+            meta.skip_upload_on_content_match
+            and file_header
+            and meta.sha256_digest == file_header.digest
+        ):
+            logger.debug(f"same file contents for {meta.name}, skipping upload")
+            meta.result_status = ResultStatus.SKIPPED
+
         self.preprocessed = True
 
     def prepare_upload(self) -> None:
         meta = self.meta
 
         if not self.preprocessed:
             self.preprocess()
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/telemetry.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/telemetry.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 from enum import Enum, unique
 from threading import Lock
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/telemetry_oob.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/telemetry_oob.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import datetime
 import json
 import logging
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/test_util.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/test_util.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 import os
 from typing import cast
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/time_util.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/time_util.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import random
 import time
 from logging import getLogger
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/dump_certs.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/dump_certs.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import os
 import sys
 from os import path
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/dump_ocsp_response.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/dump_ocsp_response.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import time
 from os import path
 from time import gmtime, strftime
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/dump_ocsp_response_cache.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/dump_ocsp_response_cache.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import json
 import sys
 from datetime import datetime
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/tool/probe_connection.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/tool/probe_connection.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 from socket import gaierror, gethostbyname_ex
 
 from asn1crypto import ocsp
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/util_text.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/util_text.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 #!/usr/bin/env python
 #
-# Copyright (c) 2012-2021 Snowflake Computing Inc. All rights reserved.
+# Copyright (c) 2012-2023 Snowflake Computing Inc. All rights reserved.
 #
 
 from __future__ import annotations
 
 import logging
 import random
 import re
@@ -142,14 +142,16 @@
                     col += 1
                     col0 = col
                 elif line[col:].startswith("--"):
                     statement.append((line[col0:col], True))
                     if not remove_comments:
                         # keep the comment
                         statement.append((line[col:], False))
+                    else:
+                        statement.append(("\n", True))
                     col = len_line + 1
                     col0 = col
                 elif line[col:].startswith("/*") and not line[col0:].startswith(
                     "file://"
                 ):
                     if not remove_comments:
                         statement.append((line[col0 : col + 2], False))
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/LICENSE` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/LICENSE`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/__init__.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/__init__.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/_internal_utils.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/_internal_utils.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/adapters.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/adapters.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/api.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/api.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/auth.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/auth.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/compat.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/compat.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/cookies.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/cookies.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/exceptions.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/exceptions.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/help.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/help.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/hooks.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/hooks.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/models.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/models.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/sessions.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/sessions.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/status_codes.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/status_codes.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/structures.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/structures.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/requests/utils.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/requests/utils.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/LICENSE.txt` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/__init__.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/__init__.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/_collections.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/_collections.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/connection.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/connection.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/connectionpool.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/connectionpool.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_appengine_environ.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_appengine_environ.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/bindings.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/bindings.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/low_level.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/_securetransport/low_level.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/appengine.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/appengine.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/ntlmpool.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/ntlmpool.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/pyopenssl.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/pyopenssl.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/securetransport.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/securetransport.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/contrib/socks.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/contrib/socks.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/exceptions.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/exceptions.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/fields.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/fields.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/filepost.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/filepost.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/backports/makefile.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/backports/makefile.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/packages/six.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/packages/six.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/poolmanager.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/poolmanager.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/request.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/request.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/response.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/response.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/__init__.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/__init__.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/connection.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/connection.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/proxy.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/proxy.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/request.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/request.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/response.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/response.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/retry.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/retry.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/ssl_.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/ssl_.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/ssl_match_hostname.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/ssl_match_hostname.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/ssltransport.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/ssltransport.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/timeout.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/timeout.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/url.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/url.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake/connector/vendored/urllib3/util/wait.py` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake/connector/vendored/urllib3/util/wait.py`

 * *Files identical despite different names*

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/PKG-INFO` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: snowflake-connector-python-nightly
-Version: 2023.3.7
+Version: 2023.4.6
 Summary: Nigthly build of Snowflake Connector for Python
 Home-page: https://www.snowflake.com/
 Author: Snowflake, Inc
 Author-email: snowflake-python-libraries-dl@snowflake.com
 License: Apache-2.0
 Project-URL: Documentation, https://docs.snowflake.com/en/user-guide/python-connector.html
 Project-URL: Source, https://github.com/keller00/snowflake-connector-python-nightlies/
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/SOURCES.txt` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -54,14 +54,15 @@
 src/snowflake/connector/ssd_internal_keys.py
 src/snowflake/connector/ssl_wrap_socket.py
 src/snowflake/connector/storage_client.py
 src/snowflake/connector/telemetry.py
 src/snowflake/connector/telemetry_oob.py
 src/snowflake/connector/test_util.py
 src/snowflake/connector/time_util.py
+src/snowflake/connector/url_util.py
 src/snowflake/connector/util_text.py
 src/snowflake/connector/version.py
 src/snowflake/connector/auth/__init__.py
 src/snowflake/connector/auth/_auth.py
 src/snowflake/connector/auth/by_plugin.py
 src/snowflake/connector/auth/default.py
 src/snowflake/connector/auth/idtoken.py
```

### Comparing `snowflake-connector-python-nightly-2023.3.7/src/snowflake_connector_python_nightly.egg-info/requires.txt` & `snowflake-connector-python-nightly-2023.4.6/src/snowflake_connector_python_nightly.egg-info/requires.txt`

 * *Files identical despite different names*

