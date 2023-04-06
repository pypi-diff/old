# Comparing `tmp/airbyte-cdk-0.9.4.tar.gz` & `tmp/airbyte-cdk-0.9.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "airbyte-cdk-0.9.4.tar", last modified: Thu Nov 17 19:35:32 2022, max compression
+gzip compressed data, was "airbyte-cdk-0.9.5.tar", last modified: Fri Nov 18 17:17:27 2022, max compression
```

## Comparing `airbyte-cdk-0.9.4.tar` & `airbyte-cdk-0.9.5.tar`

### file list

```diff
@@ -1,296 +1,296 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/
--rw-r--r--   0 root         (0) root         (0)     1051 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/LICENSE.txt
--rw-r--r--   0 root         (0) root         (0)     4992 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     4105 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.559841 airbyte-cdk-0.9.4/airbyte_cdk/
--rw-r--r--   0 root         (0) root         (0)      262 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3548 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/connector.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.559841 airbyte-cdk-0.9.4/airbyte_cdk/destinations/
--rw-r--r--   0 root         (0) root         (0)      126 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/destinations/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5420 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/destinations/destination.py
--rw-r--r--   0 root         (0) root         (0)     6902 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/entrypoint.py
--rw-r--r--   0 root         (0) root         (0)     1125 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/exception_handler.py
--rw-r--r--   0 root         (0) root         (0)     3985 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/logger.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.559841 airbyte-cdk-0.9.4/airbyte_cdk/models/
--rw-r--r--   0 root         (0) root         (0)      103 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/models/__init__.py
--rw-r--r--   0 root         (0) root         (0)    18012 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/models/airbyte_protocol.py
--rw-r--r--   0 root         (0) root         (0)     2729 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/models/well_known_types.py
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/py.typed
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.559841 airbyte-cdk-0.9.4/airbyte_cdk/sources/
--rw-r--r--   0 root         (0) root         (0)      218 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/__init__.py
--rw-r--r--   0 root         (0) root         (0)    15181 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/abstract_source.py
--rw-r--r--   0 root         (0) root         (0)      856 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/config.py
--rw-r--r--   0 root         (0) root         (0)    10469 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/connector_state_manager.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.563841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.563841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/
--rw-r--r--   0 root         (0) root         (0)      201 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)      745 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/declarative_authenticator.py
--rw-r--r--   0 root         (0) root         (0)     5234 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/oauth.py
--rw-r--r--   0 root         (0) root         (0)     4438 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/token.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.563841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/checks/
--rw-r--r--   0 root         (0) root         (0)      274 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/checks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2469 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/checks/check_stream.py
--rw-r--r--   0 root         (0) root         (0)     1368 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/checks/connection_checker.py
--rw-r--r--   0 root         (0) root         (0)     3305 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/create_partial.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.563841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/datetime/
--rw-r--r--   0 root         (0) root         (0)      177 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/datetime/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1737 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/datetime/datetime_parser.py
--rw-r--r--   0 root         (0) root         (0)     4118 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/datetime/min_max_datetime.py
--rw-r--r--   0 root         (0) root         (0)     1452 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/declarative_source.py
--rw-r--r--   0 root         (0) root         (0)     6648 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/declarative_stream.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.563841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/decoders/
--rw-r--r--   0 root         (0) root         (0)      247 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/decoders/__init__.py
--rw-r--r--   0 root         (0) root         (0)      702 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/decoders/decoder.py
--rw-r--r--   0 root         (0) root         (0)      692 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/decoders/json_decoder.py
--rw-r--r--   0 root         (0) root         (0)      299 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/exceptions.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.567841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/
--rw-r--r--   0 root         (0) root         (0)      478 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2858 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/dpath_extractor.py
--rw-r--r--   0 root         (0) root         (0)     1178 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/http_selector.py
--rw-r--r--   0 root         (0) root         (0)      784 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/record_extractor.py
--rw-r--r--   0 root         (0) root         (0)     1428 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/record_filter.py
--rw-r--r--   0 root         (0) root         (0)     1787 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/record_selector.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.567841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/
--rw-r--r--   0 root         (0) root         (0)      437 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1771 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/filters.py
--rw-r--r--   0 root         (0) root         (0)     1864 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolated_boolean.py
--rw-r--r--   0 root         (0) root         (0)     1825 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolated_mapping.py
--rw-r--r--   0 root         (0) root         (0)     2441 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolated_string.py
--rw-r--r--   0 root         (0) root         (0)      929 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolation.py
--rw-r--r--   0 root         (0) root         (0)     2634 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/jinja.py
--rw-r--r--   0 root         (0) root         (0)     2331 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/macros.py
--rw-r--r--   0 root         (0) root         (0)     9907 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/manifest_declarative_source.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.567841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5073 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/class_types_registry.py
--rw-r--r--   0 root         (0) root         (0)     3767 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/default_implementation_registry.py
--rw-r--r--   0 root         (0) root         (0)    14466 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/factory.py
--rw-r--r--   0 root         (0) root         (0)     6115 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/manifest_reference_resolver.py
--rw-r--r--   0 root         (0) root         (0)      292 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/undefined_reference_exception.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.567841 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/
--rw-r--r--   0 root         (0) root         (0)      364 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.571842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/
--rw-r--r--   0 root         (0) root         (0)      717 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.571842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/
--rw-r--r--   0 root         (0) root         (0)      875 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1343 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/constant_backoff_strategy.py
--rw-r--r--   0 root         (0) root         (0)     1206 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/exponential_backoff_strategy.py
--rw-r--r--   0 root         (0) root         (0)     1125 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/header_helper.py
--rw-r--r--   0 root         (0) root         (0)     1520 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_time_from_header_backoff_strategy.py
--rw-r--r--   0 root         (0) root         (0)     2615 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_until_time_from_header_backoff_strategy.py
--rw-r--r--   0 root         (0) root         (0)      765 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategy.py
--rw-r--r--   0 root         (0) root         (0)     2349 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/composite_error_handler.py
--rw-r--r--   0 root         (0) root         (0)     5800 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/default_error_handler.py
--rw-r--r--   0 root         (0) root         (0)      989 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/error_handler.py
--rw-r--r--   0 root         (0) root         (0)     4610 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/http_response_filter.py
--rw-r--r--   0 root         (0) root         (0)      405 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/response_action.py
--rw-r--r--   0 root         (0) root         (0)     2595 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/response_status.py
--rw-r--r--   0 root         (0) root         (0)     7363 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/http_requester.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.571842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/
--rw-r--r--   0 root         (0) root         (0)      541 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6945 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/default_paginator.py
--rw-r--r--   0 root         (0) root         (0)     1908 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/no_pagination.py
--rw-r--r--   0 root         (0) root         (0)     1832 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/paginator.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.571842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/
--rw-r--r--   0 root         (0) root         (0)      483 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2971 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/cursor_pagination_strategy.py
--rw-r--r--   0 root         (0) root         (0)     1158 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/offset_increment.py
--rw-r--r--   0 root         (0) root         (0)     1130 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/page_increment.py
--rw-r--r--   0 root         (0) root         (0)     1023 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/pagination_strategy.py
--rw-r--r--   0 root         (0) root         (0)     1501 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_option.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.571842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/
--rw-r--r--   0 root         (0) root         (0)      410 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2269 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_input_provider.py
--rw-r--r--   0 root         (0) root         (0)     4521 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_options_provider.py
--rw-r--r--   0 root         (0) root         (0)     2693 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/request_options_provider.py
--rw-r--r--   0 root         (0) root         (0)     5285 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/requester.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.571842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/retrievers/
--rw-r--r--   0 root         (0) root         (0)      269 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/retrievers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2098 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/retrievers/retriever.py
--rw-r--r--   0 root         (0) root         (0)    18891 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/retrievers/simple_retriever.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/
--rw-r--r--   0 root         (0) root         (0)      404 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1838 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/default_schema_loader.py
--rw-r--r--   0 root         (0) root         (0)     3949 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/json_file_schema_loader.py
--rw-r--r--   0 root         (0) root         (0)      448 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/schema_loader.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/spec/
--rw-r--r--   0 root         (0) root         (0)      141 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/spec/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1246 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/spec/spec.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/
--rw-r--r--   0 root         (0) root         (0)      780 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4354 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/cartesian_product_stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)    12046 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/datetime_stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)     5046 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/list_stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)     1910 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/single_slice.py
--rw-r--r--   0 root         (0) root         (0)     1597 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)     7125 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/substream_slicer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/
--rw-r--r--   0 root         (0) root         (0)      919 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4499 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/add_fields.py
--rw-r--r--   0 root         (0) root         (0)     2104 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/remove_fields.py
--rw-r--r--   0 root         (0) root         (0)     1162 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/transformation.py
--rw-r--r--   0 root         (0) root         (0)      482 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/types.py
--rw-r--r--   0 root         (0) root         (0)     1684 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/yaml_declarative_source.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/deprecated/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/deprecated/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3524 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/deprecated/base_source.py
--rw-r--r--   0 root         (0) root         (0)     3560 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/deprecated/client.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/singer/
--rw-r--r--   0 root         (0) root         (0)      246 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/singer/__init__.py
--rw-r--r--   0 root         (0) root         (0)    15649 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/singer/singer_helpers.py
--rw-r--r--   0 root         (0) root         (0)     8526 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/singer/source.py
--rw-r--r--   0 root         (0) root         (0)     4279 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/source.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.575842 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/
--rw-r--r--   0 root         (0) root         (0)      176 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10007 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/core.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.579841 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/
--rw-r--r--   0 root         (0) root         (0)      261 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.579841 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/
--rw-r--r--   0 root         (0) root         (0)      432 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)      819 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/core.py
--rw-r--r--   0 root         (0) root         (0)     3472 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/oauth.py
--rw-r--r--   0 root         (0) root         (0)     1940 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/token.py
--rw-r--r--   0 root         (0) root         (0)     1334 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/exceptions.py
--rw-r--r--   0 root         (0) root         (0)    20382 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/http.py
--rw-r--r--   0 root         (0) root         (0)     2662 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/rate_limiting.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.579841 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/
--rw-r--r--   0 root         (0) root         (0)      304 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4594 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_oauth.py
--rw-r--r--   0 root         (0) root         (0)      961 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_token.py
--rw-r--r--   0 root         (0) root         (0)     2555 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/oauth.py
--rw-r--r--   0 root         (0) root         (0)     2456 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/token.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.579841 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/
--rw-r--r--   0 root         (0) root         (0)      118 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)      244 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/casing.py
--rw-r--r--   0 root         (0) root         (0)      714 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/catalog_helpers.py
--rw-r--r--   0 root         (0) root         (0)     1702 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/record_helper.py
--rw-r--r--   0 root         (0) root         (0)     7428 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/schema_helpers.py
--rw-r--r--   0 root         (0) root         (0)     3151 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/schema_models.py
--rw-r--r--   0 root         (0) root         (0)     9488 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/transform.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.579841 airbyte-cdk-0.9.4/airbyte_cdk/utils/
--rw-r--r--   0 root         (0) root         (0)      152 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2894 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/utils/airbyte_secrets_utils.py
--rw-r--r--   0 root         (0) root         (0)     2377 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/utils/event_timing.py
--rw-r--r--   0 root         (0) root         (0)     3216 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/airbyte_cdk/utils/traced_exception.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.559841 airbyte-cdk-0.9.4/airbyte_cdk.egg-info/
--rw-r--r--   0 root         (0) root         (0)     4992 2022-11-17 19:35:32.000000 airbyte-cdk-0.9.4/airbyte_cdk.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)    13724 2022-11-17 19:35:32.000000 airbyte-cdk-0.9.4/airbyte_cdk.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-11-17 19:35:32.000000 airbyte-cdk-0.9.4/airbyte_cdk.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      320 2022-11-17 19:35:32.000000 airbyte-cdk-0.9.4/airbyte_cdk.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       23 2022-11-17 19:35:32.000000 airbyte-cdk-0.9.4/airbyte_cdk.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      145 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2208 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.555842 airbyte-cdk-0.9.4/unit_tests/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.579841 airbyte-cdk-0.9.4/unit_tests/destinations/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/destinations/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10269 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/destinations/test_destination.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.583841 airbyte-cdk-0.9.4/unit_tests/singer/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/singer/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1762 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/singer/test_singer_helpers.py
--rw-r--r--   0 root         (0) root         (0)     4442 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/singer/test_singer_source.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.583841 airbyte-cdk-0.9.4/unit_tests/sources/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.583841 airbyte-cdk-0.9.4/unit_tests/sources/declarative/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.583841 airbyte-cdk-0.9.4/unit_tests/sources/declarative/auth/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3395 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/auth/test_oauth.py
--rw-r--r--   0 root         (0) root         (0)     3666 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/auth/test_token_auth.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.583841 airbyte-cdk-0.9.4/unit_tests/sources/declarative/checks/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/checks/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1783 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/checks/test_check_stream.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.583841 airbyte-cdk-0.9.4/unit_tests/sources/declarative/decoders/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/decoders/__init__.py
--rw-r--r--   0 root         (0) root         (0)      590 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/decoders/test_json_decoder.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.587842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1765 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/test_dpath_extractor.py
--rw-r--r--   0 root         (0) root         (0)     2314 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/test_record_filter.py
--rw-r--r--   0 root         (0) root         (0)     3254 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/test_record_selector.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.587842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1472 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_filters.py
--rw-r--r--   0 root         (0) root         (0)     1869 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_interpolated_boolean.py
--rw-r--r--   0 root         (0) root         (0)     1350 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_interpolated_mapping.py
--rw-r--r--   0 root         (0) root         (0)      884 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_interpolated_string.py
--rw-r--r--   0 root         (0) root         (0)     2546 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_jinja.py
--rw-r--r--   0 root         (0) root         (0)      679 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_macros.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.587842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/iterators/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/iterators/__init__.py
--rw-r--r--   0 root         (0) root         (0)      380 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/iterators/test_only_once.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.587842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/parsers/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/parsers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4396 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/parsers/test_manifest_reference_resolver.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.587842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.587842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1505 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_constant_backoff.py
--rw-r--r--   0 root         (0) root         (0)     1281 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_exponential_backoff.py
--rw-r--r--   0 root         (0) root         (0)     1763 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_header_helper.py
--rw-r--r--   0 root         (0) root         (0)     1647 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_time_from_header.py
--rw-r--r--   0 root         (0) root         (0)     3053 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_until_time_from_header.py
--rw-r--r--   0 root         (0) root         (0)     3884 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_composite_error_handler.py
--rw-r--r--   0 root         (0) root         (0)     7224 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_default_error_handler.py
--rw-r--r--   0 root         (0) root         (0)     4408 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_http_response_filter.py
--rw-r--r--   0 root         (0) root         (0)     1971 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_response_status.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2886 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_cursor_pagination_strategy.py
--rw-r--r--   0 root         (0) root         (0)     7516 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_default_paginator.py
--rw-r--r--   0 root         (0) root         (0)      332 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_no_paginator.py
--rw-r--r--   0 root         (0) root         (0)     1162 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_offset_increment.py
--rw-r--r--   0 root         (0) root         (0)     1148 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_page_increment.py
--rw-r--r--   0 root         (0) root         (0)     1576 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_request_option.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/request_options/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/request_options/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5595 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/request_options/test_interpolated_request_options_provider.py
--rw-r--r--   0 root         (0) root         (0)     4411 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/test_http_requester.py
--rw-r--r--   0 root         (0) root         (0)     1682 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/test_interpolated_request_input_provider.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/retrievers/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/retrievers/__init__.py
--rw-r--r--   0 root         (0) root         (0)    17096 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/retrievers/test_simple_retriever.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/
--rw-r--r--   0 root         (0) root         (0)      134 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/source_test/
--rw-r--r--   0 root         (0) root         (0)      118 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/source_test/SourceTest.py
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/source_test/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1091 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/test_default_schema_loader.py
--rw-r--r--   0 root         (0) root         (0)     1209 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/test_json_file_schema_loader.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/states/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/states/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/
--rw-r--r--   0 root         (0) root         (0)       61 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/__init__.py
--rw-r--r--   0 root         (0) root         (0)     9277 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_cartesian_product_stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)    27258 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_datetime_stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)     5720 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_list_stream_slicer.py
--rw-r--r--   0 root         (0) root         (0)    10479 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_substream_slicer.py
--rw-r--r--   0 root         (0) root         (0)     2594 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_create_partial.py
--rw-r--r--   0 root         (0) root         (0)     2760 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_declarative_stream.py
--rw-r--r--   0 root         (0) root         (0)    37220 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_factory.py
--rw-r--r--   0 root         (0) root         (0)    35020 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_manifest_declarative_source.py
--rw-r--r--   0 root         (0) root         (0)     5100 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_yaml_declarative_source.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.591842 airbyte-cdk-0.9.4/unit_tests/sources/streams/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/auth/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)     5672 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/auth/test_auth.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/requests_native_auth/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/requests_native_auth/__init__.py
--rw-r--r--   0 root         (0) root         (0)     6899 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/requests_native_auth/test_requests_native_auth.py
--rw-r--r--   0 root         (0) root         (0)    19656 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/http/test_http.py
--rw-r--r--   0 root         (0) root         (0)     5059 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/streams/test_streams_core.py
--rw-r--r--   0 root         (0) root         (0)    37665 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/test_abstract_source.py
--rw-r--r--   0 root         (0) root         (0)     2477 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/test_config.py
--rw-r--r--   0 root         (0) root         (0)    24264 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/test_connector_state_manager.py
--rw-r--r--   0 root         (0) root         (0)    18420 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/sources/test_source.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-17 19:35:32.595842 airbyte-cdk-0.9.4/unit_tests/utils/
--rw-r--r--   0 root         (0) root         (0)        0 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/utils/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4886 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/utils/test_secret_utils.py
--rw-r--r--   0 root         (0) root         (0)     4198 2022-11-17 19:33:20.000000 airbyte-cdk-0.9.4/unit_tests/utils/test_traced_exception.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:27.002035 airbyte-cdk-0.9.5/
+-rw-r--r--   0 root         (0) root         (0)     1051 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/LICENSE.txt
+-rw-r--r--   0 root         (0) root         (0)     4992 2022-11-18 17:17:27.002035 airbyte-cdk-0.9.5/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     4105 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.966035 airbyte-cdk-0.9.5/airbyte_cdk/
+-rw-r--r--   0 root         (0) root         (0)      262 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3548 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/connector.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.966035 airbyte-cdk-0.9.5/airbyte_cdk/destinations/
+-rw-r--r--   0 root         (0) root         (0)      126 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/destinations/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5420 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/destinations/destination.py
+-rw-r--r--   0 root         (0) root         (0)     6902 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/entrypoint.py
+-rw-r--r--   0 root         (0) root         (0)     1125 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/exception_handler.py
+-rw-r--r--   0 root         (0) root         (0)     3985 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/logger.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.966035 airbyte-cdk-0.9.5/airbyte_cdk/models/
+-rw-r--r--   0 root         (0) root         (0)      103 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/models/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    18012 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/models/airbyte_protocol.py
+-rw-r--r--   0 root         (0) root         (0)     2729 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/models/well_known_types.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/py.typed
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.970035 airbyte-cdk-0.9.5/airbyte_cdk/sources/
+-rw-r--r--   0 root         (0) root         (0)      218 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    15181 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/abstract_source.py
+-rw-r--r--   0 root         (0) root         (0)      856 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/config.py
+-rw-r--r--   0 root         (0) root         (0)    10469 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/connector_state_manager.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.970035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.970035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/
+-rw-r--r--   0 root         (0) root         (0)      201 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      745 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/declarative_authenticator.py
+-rw-r--r--   0 root         (0) root         (0)     5234 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/oauth.py
+-rw-r--r--   0 root         (0) root         (0)     4438 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/token.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.970035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/checks/
+-rw-r--r--   0 root         (0) root         (0)      274 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/checks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2469 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/checks/check_stream.py
+-rw-r--r--   0 root         (0) root         (0)     1368 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/checks/connection_checker.py
+-rw-r--r--   0 root         (0) root         (0)     3305 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/create_partial.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.970035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/datetime/
+-rw-r--r--   0 root         (0) root         (0)      177 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/datetime/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1737 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/datetime/datetime_parser.py
+-rw-r--r--   0 root         (0) root         (0)     4118 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/datetime/min_max_datetime.py
+-rw-r--r--   0 root         (0) root         (0)     1452 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/declarative_source.py
+-rw-r--r--   0 root         (0) root         (0)     6648 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/declarative_stream.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.970035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/decoders/
+-rw-r--r--   0 root         (0) root         (0)      247 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/decoders/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      702 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/decoders/decoder.py
+-rw-r--r--   0 root         (0) root         (0)      692 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/decoders/json_decoder.py
+-rw-r--r--   0 root         (0) root         (0)      299 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/exceptions.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.974035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/
+-rw-r--r--   0 root         (0) root         (0)      478 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2858 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/dpath_extractor.py
+-rw-r--r--   0 root         (0) root         (0)     1178 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/http_selector.py
+-rw-r--r--   0 root         (0) root         (0)      784 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/record_extractor.py
+-rw-r--r--   0 root         (0) root         (0)     1428 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/record_filter.py
+-rw-r--r--   0 root         (0) root         (0)     1787 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/record_selector.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.974035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/
+-rw-r--r--   0 root         (0) root         (0)      437 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1771 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/filters.py
+-rw-r--r--   0 root         (0) root         (0)     1864 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolated_boolean.py
+-rw-r--r--   0 root         (0) root         (0)     1825 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolated_mapping.py
+-rw-r--r--   0 root         (0) root         (0)     2441 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolated_string.py
+-rw-r--r--   0 root         (0) root         (0)      929 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolation.py
+-rw-r--r--   0 root         (0) root         (0)     2634 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/jinja.py
+-rw-r--r--   0 root         (0) root         (0)     2670 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/macros.py
+-rw-r--r--   0 root         (0) root         (0)     9907 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/manifest_declarative_source.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.974035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5073 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/class_types_registry.py
+-rw-r--r--   0 root         (0) root         (0)     3767 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/default_implementation_registry.py
+-rw-r--r--   0 root         (0) root         (0)    14466 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/factory.py
+-rw-r--r--   0 root         (0) root         (0)     6115 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/manifest_reference_resolver.py
+-rw-r--r--   0 root         (0) root         (0)      292 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/undefined_reference_exception.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.974035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/
+-rw-r--r--   0 root         (0) root         (0)      364 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.978035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/
+-rw-r--r--   0 root         (0) root         (0)      717 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.978035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/
+-rw-r--r--   0 root         (0) root         (0)      875 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1343 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/constant_backoff_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     1206 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/exponential_backoff_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     1125 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/header_helper.py
+-rw-r--r--   0 root         (0) root         (0)     1520 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_time_from_header_backoff_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     2615 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_until_time_from_header_backoff_strategy.py
+-rw-r--r--   0 root         (0) root         (0)      765 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     2349 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/composite_error_handler.py
+-rw-r--r--   0 root         (0) root         (0)     5800 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/default_error_handler.py
+-rw-r--r--   0 root         (0) root         (0)      989 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/error_handler.py
+-rw-r--r--   0 root         (0) root         (0)     4610 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/http_response_filter.py
+-rw-r--r--   0 root         (0) root         (0)      405 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/response_action.py
+-rw-r--r--   0 root         (0) root         (0)     2595 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/response_status.py
+-rw-r--r--   0 root         (0) root         (0)     7363 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/http_requester.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.978035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/
+-rw-r--r--   0 root         (0) root         (0)      541 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6945 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/default_paginator.py
+-rw-r--r--   0 root         (0) root         (0)     1908 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/no_pagination.py
+-rw-r--r--   0 root         (0) root         (0)     1832 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/paginator.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.978035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/
+-rw-r--r--   0 root         (0) root         (0)      483 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2971 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/cursor_pagination_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     1158 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/offset_increment.py
+-rw-r--r--   0 root         (0) root         (0)     1130 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/page_increment.py
+-rw-r--r--   0 root         (0) root         (0)     1023 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/pagination_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     1501 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_option.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.978035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/
+-rw-r--r--   0 root         (0) root         (0)      410 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2269 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_input_provider.py
+-rw-r--r--   0 root         (0) root         (0)     4521 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_options_provider.py
+-rw-r--r--   0 root         (0) root         (0)     2693 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/request_options_provider.py
+-rw-r--r--   0 root         (0) root         (0)     5285 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/requester.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.978035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/retrievers/
+-rw-r--r--   0 root         (0) root         (0)      269 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/retrievers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2098 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/retrievers/retriever.py
+-rw-r--r--   0 root         (0) root         (0)    18891 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/retrievers/simple_retriever.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/
+-rw-r--r--   0 root         (0) root         (0)      404 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1838 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/default_schema_loader.py
+-rw-r--r--   0 root         (0) root         (0)     3949 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/json_file_schema_loader.py
+-rw-r--r--   0 root         (0) root         (0)      448 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/schema_loader.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/spec/
+-rw-r--r--   0 root         (0) root         (0)      141 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/spec/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1246 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/spec/spec.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/
+-rw-r--r--   0 root         (0) root         (0)      780 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4354 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/cartesian_product_stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)    12046 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/datetime_stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)     5046 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/list_stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)     1910 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/single_slice.py
+-rw-r--r--   0 root         (0) root         (0)     1597 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)     7125 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/substream_slicer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/
+-rw-r--r--   0 root         (0) root         (0)      919 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4499 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/add_fields.py
+-rw-r--r--   0 root         (0) root         (0)     2104 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/remove_fields.py
+-rw-r--r--   0 root         (0) root         (0)     1162 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/transformation.py
+-rw-r--r--   0 root         (0) root         (0)      482 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/types.py
+-rw-r--r--   0 root         (0) root         (0)     1684 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/yaml_declarative_source.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/deprecated/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/deprecated/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3524 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/deprecated/base_source.py
+-rw-r--r--   0 root         (0) root         (0)     3560 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/deprecated/client.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/singer/
+-rw-r--r--   0 root         (0) root         (0)      246 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/singer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    15649 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/singer/singer_helpers.py
+-rw-r--r--   0 root         (0) root         (0)     8526 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/singer/source.py
+-rw-r--r--   0 root         (0) root         (0)     4279 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/source.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.982035 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/
+-rw-r--r--   0 root         (0) root         (0)      176 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10007 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/core.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.986035 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/
+-rw-r--r--   0 root         (0) root         (0)      261 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.986035 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/
+-rw-r--r--   0 root         (0) root         (0)      432 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      819 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/core.py
+-rw-r--r--   0 root         (0) root         (0)     3472 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/oauth.py
+-rw-r--r--   0 root         (0) root         (0)     1940 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/token.py
+-rw-r--r--   0 root         (0) root         (0)     1334 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/exceptions.py
+-rw-r--r--   0 root         (0) root         (0)    20382 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/http.py
+-rw-r--r--   0 root         (0) root         (0)     2662 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/rate_limiting.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.986035 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/
+-rw-r--r--   0 root         (0) root         (0)      304 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4594 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_oauth.py
+-rw-r--r--   0 root         (0) root         (0)      961 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_token.py
+-rw-r--r--   0 root         (0) root         (0)     2555 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/oauth.py
+-rw-r--r--   0 root         (0) root         (0)     2456 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/token.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.986035 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/
+-rw-r--r--   0 root         (0) root         (0)      118 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      244 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/casing.py
+-rw-r--r--   0 root         (0) root         (0)      714 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/catalog_helpers.py
+-rw-r--r--   0 root         (0) root         (0)     1702 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/record_helper.py
+-rw-r--r--   0 root         (0) root         (0)     7428 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/schema_helpers.py
+-rw-r--r--   0 root         (0) root         (0)     3151 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/schema_models.py
+-rw-r--r--   0 root         (0) root         (0)     9488 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/transform.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.986035 airbyte-cdk-0.9.5/airbyte_cdk/utils/
+-rw-r--r--   0 root         (0) root         (0)      152 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2894 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/utils/airbyte_secrets_utils.py
+-rw-r--r--   0 root         (0) root         (0)     2377 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/utils/event_timing.py
+-rw-r--r--   0 root         (0) root         (0)     3216 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/airbyte_cdk/utils/traced_exception.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.966035 airbyte-cdk-0.9.5/airbyte_cdk.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     4992 2022-11-18 17:17:26.000000 airbyte-cdk-0.9.5/airbyte_cdk.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)    13724 2022-11-18 17:17:26.000000 airbyte-cdk-0.9.5/airbyte_cdk.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-11-18 17:17:26.000000 airbyte-cdk-0.9.5/airbyte_cdk.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      320 2022-11-18 17:17:26.000000 airbyte-cdk-0.9.5/airbyte_cdk.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       23 2022-11-18 17:17:26.000000 airbyte-cdk-0.9.5/airbyte_cdk.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      145 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2022-11-18 17:17:27.002035 airbyte-cdk-0.9.5/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2208 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.966035 airbyte-cdk-0.9.5/unit_tests/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.986035 airbyte-cdk-0.9.5/unit_tests/destinations/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/destinations/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10269 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/destinations/test_destination.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/singer/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/singer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1762 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/singer/test_singer_helpers.py
+-rw-r--r--   0 root         (0) root         (0)     4442 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/singer/test_singer_source.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/sources/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/auth/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/auth/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3395 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/auth/test_oauth.py
+-rw-r--r--   0 root         (0) root         (0)     3666 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/auth/test_token_auth.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/checks/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/checks/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1783 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/checks/test_check_stream.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/decoders/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/decoders/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      590 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/decoders/test_json_decoder.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.990035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1765 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/test_dpath_extractor.py
+-rw-r--r--   0 root         (0) root         (0)     2314 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/test_record_filter.py
+-rw-r--r--   0 root         (0) root         (0)     3254 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/test_record_selector.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.994035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1472 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_filters.py
+-rw-r--r--   0 root         (0) root         (0)     1869 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_interpolated_boolean.py
+-rw-r--r--   0 root         (0) root         (0)     1350 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_interpolated_mapping.py
+-rw-r--r--   0 root         (0) root         (0)      884 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_interpolated_string.py
+-rw-r--r--   0 root         (0) root         (0)     2546 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_jinja.py
+-rw-r--r--   0 root         (0) root         (0)     1007 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_macros.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.994035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/iterators/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/iterators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      380 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/iterators/test_only_once.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.994035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/parsers/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/parsers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4396 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/parsers/test_manifest_reference_resolver.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.994035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.994035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.994035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1505 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_constant_backoff.py
+-rw-r--r--   0 root         (0) root         (0)     1281 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_exponential_backoff.py
+-rw-r--r--   0 root         (0) root         (0)     1763 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_header_helper.py
+-rw-r--r--   0 root         (0) root         (0)     1647 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_time_from_header.py
+-rw-r--r--   0 root         (0) root         (0)     3053 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_until_time_from_header.py
+-rw-r--r--   0 root         (0) root         (0)     3884 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_composite_error_handler.py
+-rw-r--r--   0 root         (0) root         (0)     7224 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_default_error_handler.py
+-rw-r--r--   0 root         (0) root         (0)     4408 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_http_response_filter.py
+-rw-r--r--   0 root         (0) root         (0)     1971 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_response_status.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2886 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_cursor_pagination_strategy.py
+-rw-r--r--   0 root         (0) root         (0)     7516 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_default_paginator.py
+-rw-r--r--   0 root         (0) root         (0)      332 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_no_paginator.py
+-rw-r--r--   0 root         (0) root         (0)     1162 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_offset_increment.py
+-rw-r--r--   0 root         (0) root         (0)     1148 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_page_increment.py
+-rw-r--r--   0 root         (0) root         (0)     1576 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_request_option.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/request_options/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/request_options/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5595 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/request_options/test_interpolated_request_options_provider.py
+-rw-r--r--   0 root         (0) root         (0)     4411 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/test_http_requester.py
+-rw-r--r--   0 root         (0) root         (0)     1682 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/test_interpolated_request_input_provider.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/retrievers/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/retrievers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    17096 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/retrievers/test_simple_retriever.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/
+-rw-r--r--   0 root         (0) root         (0)      134 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/source_test/
+-rw-r--r--   0 root         (0) root         (0)      118 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/source_test/SourceTest.py
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/source_test/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1091 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/test_default_schema_loader.py
+-rw-r--r--   0 root         (0) root         (0)     1209 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/test_json_file_schema_loader.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/states/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/states/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/
+-rw-r--r--   0 root         (0) root         (0)       61 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     9277 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_cartesian_product_stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)    27258 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_datetime_stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)     5720 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_list_stream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)    10479 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_substream_slicer.py
+-rw-r--r--   0 root         (0) root         (0)     2594 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_create_partial.py
+-rw-r--r--   0 root         (0) root         (0)     2760 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_declarative_stream.py
+-rw-r--r--   0 root         (0) root         (0)    37220 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_factory.py
+-rw-r--r--   0 root         (0) root         (0)    35020 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_manifest_declarative_source.py
+-rw-r--r--   0 root         (0) root         (0)     5100 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_yaml_declarative_source.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/streams/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:26.998035 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:27.002035 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/auth/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/auth/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     5672 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/auth/test_auth.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:27.002035 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/requests_native_auth/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/requests_native_auth/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     6899 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/requests_native_auth/test_requests_native_auth.py
+-rw-r--r--   0 root         (0) root         (0)    19656 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/http/test_http.py
+-rw-r--r--   0 root         (0) root         (0)     5059 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/streams/test_streams_core.py
+-rw-r--r--   0 root         (0) root         (0)    37665 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/test_abstract_source.py
+-rw-r--r--   0 root         (0) root         (0)     2477 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/test_config.py
+-rw-r--r--   0 root         (0) root         (0)    24264 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/test_connector_state_manager.py
+-rw-r--r--   0 root         (0) root         (0)    18420 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/sources/test_source.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-18 17:17:27.002035 airbyte-cdk-0.9.5/unit_tests/utils/
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/utils/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4886 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/utils/test_secret_utils.py
+-rw-r--r--   0 root         (0) root         (0)     4198 2022-11-18 17:15:12.000000 airbyte-cdk-0.9.5/unit_tests/utils/test_traced_exception.py
```

### Comparing `airbyte-cdk-0.9.4/LICENSE.txt` & `airbyte-cdk-0.9.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/PKG-INFO` & `airbyte-cdk-0.9.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: airbyte-cdk
-Version: 0.9.4
+Version: 0.9.5
 Summary: A framework for writing Airbyte Connectors.
 Home-page: https://github.com/airbytehq/airbyte
 Author: Airbyte
 Author-email: contact@airbyte.io
 License: MIT
 Project-URL: Documentation, https://docs.airbyte.io/
 Project-URL: Source, https://github.com/airbytehq/airbyte
```

### Comparing `airbyte-cdk-0.9.4/README.md` & `airbyte-cdk-0.9.5/README.md`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/connector.py` & `airbyte-cdk-0.9.5/airbyte_cdk/connector.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/destinations/destination.py` & `airbyte-cdk-0.9.5/airbyte_cdk/destinations/destination.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/entrypoint.py` & `airbyte-cdk-0.9.5/airbyte_cdk/entrypoint.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/exception_handler.py` & `airbyte-cdk-0.9.5/airbyte_cdk/exception_handler.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/logger.py` & `airbyte-cdk-0.9.5/airbyte_cdk/logger.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/models/airbyte_protocol.py` & `airbyte-cdk-0.9.5/airbyte_cdk/models/airbyte_protocol.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/models/well_known_types.py` & `airbyte-cdk-0.9.5/airbyte_cdk/models/well_known_types.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/abstract_source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/abstract_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/config.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/config.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/connector_state_manager.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/connector_state_manager.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/declarative_authenticator.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/declarative_authenticator.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/oauth.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/oauth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/auth/token.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/auth/token.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/checks/check_stream.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/checks/check_stream.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/checks/connection_checker.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/checks/connection_checker.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/create_partial.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/create_partial.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/datetime/datetime_parser.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/datetime/datetime_parser.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/datetime/min_max_datetime.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/datetime/min_max_datetime.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/declarative_source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/declarative_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/declarative_stream.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/declarative_stream.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/decoders/decoder.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/decoders/decoder.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/decoders/json_decoder.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/decoders/json_decoder.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/dpath_extractor.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/dpath_extractor.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/http_selector.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/http_selector.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/record_extractor.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/record_extractor.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/record_filter.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/record_filter.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/extractors/record_selector.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/extractors/record_selector.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/filters.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/filters.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolated_boolean.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolated_boolean.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolated_mapping.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolated_mapping.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolated_string.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolated_string.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/interpolation.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/interpolation.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/jinja.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/jinja.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/interpolation/macros.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/interpolation/macros.py`

 * *Files 14% similar despite different names*

```diff
@@ -92,9 +92,21 @@
 
     :param num_days: number of days to add to current date time
     :return: datetime formatted as RFC3339
     """
     return (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=num_days)).strftime("%Y-%m-%dT%H:%M:%S.%f%z")
 
 
-_macros_list = [now_local, now_utc, today_utc, timestamp, max, day_delta]
+def format_datetime(dt: Union[str, datetime.datetime], format: str):
+    """
+    Converts datetime to another format
+
+    Usage:
+    `"{{ format_datetime(config.start_date, '%Y-%m-%d') }}"`
+    """
+    if isinstance(dt, datetime.datetime):
+        return dt.strftime(format)
+    return parser.parse(dt).strftime(format)
+
+
+_macros_list = [now_local, now_utc, today_utc, timestamp, max, day_delta, format_datetime]
 macros = {f.__name__: f for f in _macros_list}
```

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/manifest_declarative_source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/manifest_declarative_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/class_types_registry.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/class_types_registry.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/default_implementation_registry.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/default_implementation_registry.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/factory.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/factory.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/parsers/manifest_reference_resolver.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/parsers/manifest_reference_resolver.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/__init__.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/__init__.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/__init__.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/__init__.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/constant_backoff_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/constant_backoff_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/exponential_backoff_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/exponential_backoff_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/header_helper.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/header_helper.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_time_from_header_backoff_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_time_from_header_backoff_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_until_time_from_header_backoff_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategies/wait_until_time_from_header_backoff_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/backoff_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/composite_error_handler.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/composite_error_handler.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/default_error_handler.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/default_error_handler.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/error_handler.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/error_handler.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/http_response_filter.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/http_response_filter.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/error_handlers/response_status.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/error_handlers/response_status.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/http_requester.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/http_requester.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/__init__.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/__init__.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/default_paginator.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/default_paginator.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/no_pagination.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/no_pagination.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/paginator.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/paginator.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/cursor_pagination_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/cursor_pagination_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/offset_increment.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/offset_increment.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/page_increment.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/page_increment.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/paginators/strategies/pagination_strategy.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/paginators/strategies/pagination_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_option.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_option.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_input_provider.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_input_provider.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_options_provider.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/interpolated_request_options_provider.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/request_options/request_options_provider.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/request_options/request_options_provider.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/requesters/requester.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/requesters/requester.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/retrievers/retriever.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/retrievers/retriever.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/retrievers/simple_retriever.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/retrievers/simple_retriever.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/default_schema_loader.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/default_schema_loader.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/schema/json_file_schema_loader.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/schema/json_file_schema_loader.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/spec/spec.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/spec/spec.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/__init__.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/__init__.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/cartesian_product_stream_slicer.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/cartesian_product_stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/datetime_stream_slicer.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/datetime_stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/list_stream_slicer.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/list_stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/single_slice.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/single_slice.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/stream_slicer.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/stream_slicers/substream_slicer.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/stream_slicers/substream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/__init__.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/__init__.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/add_fields.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/add_fields.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/remove_fields.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/remove_fields.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/transformations/transformation.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/transformations/transformation.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/declarative/yaml_declarative_source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/declarative/yaml_declarative_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/deprecated/base_source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/deprecated/base_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/deprecated/client.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/deprecated/client.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/singer/singer_helpers.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/singer/singer_helpers.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/singer/source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/singer/source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/source.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/core.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/core.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/core.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/core.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/oauth.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/oauth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/auth/token.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/auth/token.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/exceptions.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/exceptions.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/http.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/http.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/rate_limiting.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/rate_limiting.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_oauth.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_oauth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_token.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/abstract_token.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/oauth.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/oauth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/streams/http/requests_native_auth/token.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/streams/http/requests_native_auth/token.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/catalog_helpers.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/catalog_helpers.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/record_helper.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/record_helper.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/schema_helpers.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/schema_helpers.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/schema_models.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/schema_models.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/sources/utils/transform.py` & `airbyte-cdk-0.9.5/airbyte_cdk/sources/utils/transform.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/utils/airbyte_secrets_utils.py` & `airbyte-cdk-0.9.5/airbyte_cdk/utils/airbyte_secrets_utils.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/utils/event_timing.py` & `airbyte-cdk-0.9.5/airbyte_cdk/utils/event_timing.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk/utils/traced_exception.py` & `airbyte-cdk-0.9.5/airbyte_cdk/utils/traced_exception.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk.egg-info/PKG-INFO` & `airbyte-cdk-0.9.5/airbyte_cdk.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: airbyte-cdk
-Version: 0.9.4
+Version: 0.9.5
 Summary: A framework for writing Airbyte Connectors.
 Home-page: https://github.com/airbytehq/airbyte
 Author: Airbyte
 Author-email: contact@airbyte.io
 License: MIT
 Project-URL: Documentation, https://docs.airbyte.io/
 Project-URL: Source, https://github.com/airbytehq/airbyte
```

### Comparing `airbyte-cdk-0.9.4/airbyte_cdk.egg-info/SOURCES.txt` & `airbyte-cdk-0.9.5/airbyte_cdk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/setup.py` & `airbyte-cdk-0.9.5/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 HERE = pathlib.Path(__file__).parent
 
 # The text of the README file
 README = (HERE / "README.md").read_text()
 
 setup(
     name="airbyte-cdk",
-    version="0.9.4",
+    version="0.9.5",
     description="A framework for writing Airbyte Connectors.",
     long_description=README,
     long_description_content_type="text/markdown",
     author="Airbyte",
     author_email="contact@airbyte.io",
     license="MIT",
     url="https://github.com/airbytehq/airbyte",
```

### Comparing `airbyte-cdk-0.9.4/unit_tests/destinations/test_destination.py` & `airbyte-cdk-0.9.5/unit_tests/destinations/test_destination.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/singer/test_singer_helpers.py` & `airbyte-cdk-0.9.5/unit_tests/singer/test_singer_helpers.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/singer/test_singer_source.py` & `airbyte-cdk-0.9.5/unit_tests/singer/test_singer_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/auth/test_oauth.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/auth/test_oauth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/auth/test_token_auth.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/auth/test_token_auth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/checks/test_check_stream.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/checks/test_check_stream.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/decoders/test_json_decoder.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/decoders/test_json_decoder.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/test_dpath_extractor.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/test_dpath_extractor.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/test_record_filter.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/test_record_filter.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/extractors/test_record_selector.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/extractors/test_record_selector.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_filters.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_filters.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_interpolated_boolean.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_interpolated_boolean.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_interpolated_mapping.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_interpolated_mapping.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_interpolated_string.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_interpolated_string.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/interpolation/test_jinja.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/interpolation/test_jinja.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/parsers/test_manifest_reference_resolver.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/parsers/test_manifest_reference_resolver.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_constant_backoff.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_constant_backoff.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_exponential_backoff.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_exponential_backoff.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_header_helper.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_header_helper.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_time_from_header.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_time_from_header.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_until_time_from_header.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/backoff_strategies/test_wait_until_time_from_header.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_composite_error_handler.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_composite_error_handler.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_default_error_handler.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_default_error_handler.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_http_response_filter.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_http_response_filter.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/error_handlers/test_response_status.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/error_handlers/test_response_status.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_cursor_pagination_strategy.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_cursor_pagination_strategy.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_default_paginator.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_default_paginator.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_offset_increment.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_offset_increment.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_page_increment.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_page_increment.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/paginators/test_request_option.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/paginators/test_request_option.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/request_options/test_interpolated_request_options_provider.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/request_options/test_interpolated_request_options_provider.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/test_http_requester.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/test_http_requester.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/requesters/test_interpolated_request_input_provider.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/requesters/test_interpolated_request_input_provider.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/retrievers/test_simple_retriever.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/retrievers/test_simple_retriever.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/test_default_schema_loader.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/test_default_schema_loader.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/schema/test_json_file_schema_loader.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/schema/test_json_file_schema_loader.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_cartesian_product_stream_slicer.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_cartesian_product_stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_datetime_stream_slicer.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_datetime_stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_list_stream_slicer.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_list_stream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/stream_slicers/test_substream_slicer.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/stream_slicers/test_substream_slicer.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_create_partial.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_create_partial.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_declarative_stream.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_declarative_stream.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_factory.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_factory.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_manifest_declarative_source.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_manifest_declarative_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/declarative/test_yaml_declarative_source.py` & `airbyte-cdk-0.9.5/unit_tests/sources/declarative/test_yaml_declarative_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/streams/http/auth/test_auth.py` & `airbyte-cdk-0.9.5/unit_tests/sources/streams/http/auth/test_auth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/streams/http/requests_native_auth/test_requests_native_auth.py` & `airbyte-cdk-0.9.5/unit_tests/sources/streams/http/requests_native_auth/test_requests_native_auth.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/streams/http/test_http.py` & `airbyte-cdk-0.9.5/unit_tests/sources/streams/http/test_http.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/streams/test_streams_core.py` & `airbyte-cdk-0.9.5/unit_tests/sources/streams/test_streams_core.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/test_abstract_source.py` & `airbyte-cdk-0.9.5/unit_tests/sources/test_abstract_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/test_config.py` & `airbyte-cdk-0.9.5/unit_tests/sources/test_config.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/test_connector_state_manager.py` & `airbyte-cdk-0.9.5/unit_tests/sources/test_connector_state_manager.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/sources/test_source.py` & `airbyte-cdk-0.9.5/unit_tests/sources/test_source.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/utils/test_secret_utils.py` & `airbyte-cdk-0.9.5/unit_tests/utils/test_secret_utils.py`

 * *Files identical despite different names*

### Comparing `airbyte-cdk-0.9.4/unit_tests/utils/test_traced_exception.py` & `airbyte-cdk-0.9.5/unit_tests/utils/test_traced_exception.py`

 * *Files identical despite different names*

