# Comparing `tmp/artistml-sdk-0.2.1.dev9296519.tar.gz` & `tmp/artistml-sdk-0.2.1.dev9751808.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "artistml-sdk-0.2.1.dev9296519.tar", last modified: Thu Apr  6 12:06:27 2023, max compression
+gzip compressed data, was "artistml-sdk-0.2.1.dev9751808.tar", last modified: Sat Dec 24 02:28:37 2022, max compression
```

## Comparing `artistml-sdk-0.2.1.dev9296519.tar` & `artistml-sdk-0.2.1.dev9751808.tar`

### file list

```diff
@@ -1,154 +1,237 @@
--rw-rw-r--   0     1001     1001       14 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/README.md
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/__init__.py
--rw-rw-r--   0     1001     1001    10756 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2.py
--rw-rw-r--   0     1001     1001    21166 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2.pyi
--rw-rw-r--   0     1001     1001    12546 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     3469 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/py.typed
--rw-rw-r--   0     1001     1001     8538 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2.py
--rw-rw-r--   0     1001     1001    16288 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2.pyi
--rw-rw-r--   0     1001     1001    10769 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     3900 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/py.typed
--rw-rw-r--   0     1001     1001     2987 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/types_pb2.py
--rw-rw-r--   0     1001     1001     7563 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/types_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/types_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/types_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/__init__.py
--rw-rw-r--   0     1001     1001      986 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/enums_pb2.py
--rw-rw-r--   0     1001     1001      165 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/enums_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/enums_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/enums_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     2286 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_pb2.py
--rw-rw-r--   0     1001     1001     2654 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001    10683 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2.py
--rw-rw-r--   0     1001     1001    19803 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2.pyi
--rw-rw-r--   0     1001     1001    16286 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     5544 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/__init__.py
--rw-rw-r--   0     1001     1001     3666 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/hacker_service_pb2.py
--rw-rw-r--   0     1001     1001     5409 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/hacker_service_pb2.pyi
--rw-rw-r--   0     1001     1001     2648 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/hacker_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001      951 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/hacker_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/__init__.py
--rw-rw-r--   0     1001     1001     2145 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_pb2.py
--rw-rw-r--   0     1001     1001     2710 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     8767 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2.py
--rw-rw-r--   0     1001     1001    15953 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2.pyi
--rw-rw-r--   0     1001     1001    13083 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     4714 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001    10204 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2.py
--rw-rw-r--   0     1001     1001    20752 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2.pyi
--rw-rw-r--   0     1001     1001    10690 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     3077 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     2524 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_pb2.py
--rw-rw-r--   0     1001     1001     3498 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     8203 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2.py
--rw-rw-r--   0     1001     1001    15427 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2.pyi
--rw-rw-r--   0     1001     1001    12621 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     4453 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/py.typed
--rw-rw-r--   0     1001     1001     2173 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_pb2.py
--rw-rw-r--   0     1001     1001     3067 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     7953 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2.py
--rw-rw-r--   0     1001     1001    15015 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2.pyi
--rw-rw-r--   0     1001     1001    12159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     4192 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/py.typed
--rw-rw-r--   0     1001     1001     1892 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_pb2.py
--rw-rw-r--   0     1001     1001     2571 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     7744 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_service_pb2.py
--rw-rw-r--   0     1001     1001    14927 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_service_pb2.pyi
--rw-rw-r--   0     1001     1001    12045 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.py
--rw-rw-r--   0     1001     1001     4134 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/__init__.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/__init__.py
--rw-rw-r--   0     1001     1001     1327 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/chat_pb2.py
--rw-rw-r--   0     1001     1001      856 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/chat_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/chat_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/chat_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001     1168 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/hello_pb2.py
--rw-rw-r--   0     1001     1001      691 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/hello_pb2.pyi
--rw-rw-r--   0     1001     1001      159 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/hello_pb2_grpc.py
--rw-rw-r--   0     1001     1001       76 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/hello_pb2_grpc.pyi
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/py.typed
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/py.typed
--rw-rw-r--   0     1001     1001      253 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/__init__.py
--rw-rw-r--   0 root         (0) root         (0)     2255 2023-04-06 12:06:25.205651 artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/argo.py
--rw-rw-r--   0     1001     1001     3386 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/assoc.py
--rw-rw-r--   0     1001     1001      928 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/echo.py
--rw-rw-r--   0     1001     1001    17111 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/muses.py
--rw-rw-r--   0     1001     1001     2110 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/tag.py
--rw-rw-r--   0     1001     1001      903 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/__init__.py
--rw-rw-r--   0     1001     1001      269 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/__init__.py
--rw-rw-r--   0     1001     1001     3535 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/grpc_channel.py
--rw-rw-r--   0     1001     1001     1207 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/grpc_client.py
--rw-rw-r--   0     1001     1001      835 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/grpc_invoke_wrapper.py
--rw-rw-r--   0     1001     1001       43 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/__init__.py
--rw-rw-r--   0     1001     1001      476 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/_kfp.py
--rw-rw-r--   0     1001     1001     1101 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/argo.py
--rw-rw-r--   0     1001     1001      354 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/assoc.py
--rw-rw-r--   0     1001     1001      399 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/echo.py
--rw-rw-r--   0     1001     1001      871 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/muses.py
--rw-rw-r--   0     1001     1001      372 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/tag.py
--rw-rw-r--   0     1001     1001      541 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/lib/__init__.py
--rw-rw-r--   0     1001     1001     2358 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/lib/_argo_model.py
--rw-rw-r--   0     1001     1001     1945 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/lib/_config.py
--rw-rw-r--   0     1001     1001      936 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/lib/_protobuf_message.py
--rw-rw-r--   0     1001     1001      316 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/lib/_yaml.py
--rw-rw-r--   0     1001     1001      271 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/logger/__init__.py
--rw-rw-r--   0     1001     1001     9218 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/artistml_sdk/logger/logger.py
--rw-rw-r--   0     1001     1001     1938 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/pyproject.toml
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/.gitkeep
--rw-rw-r--   0     1001     1001       57 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/pipeline_spec.yaml
--rw-rw-r--   0 root         (0) root         (0)      941 2023-04-06 12:06:25.209651 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/test_argo_client.py
--rw-rw-r--   0     1001     1001     1694 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/test_assoc_client.py
--rw-rw-r--   0     1001     1001     1089 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/test_mlflow.py
--rw-rw-r--   0     1001     1001    10185 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/test_muses_client.py
--rw-rw-r--   0     1001     1001      910 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/test_tag_client.py
--rw-rw-r--   0     1001     1001      509 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/clients/workflow.yaml
--rw-rw-r--   0     1001     1001     1057 2023-04-01 05:20:07.166535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/gateway/_grpc_clients/test_kfp_client.py
--rw-rw-r--   0     1001     1001     5383 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/gateway/_grpc_clients/test_kfp_compiler.py
--rw-rw-r--   0     1001     1001     9382 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/gateway/_grpc_clients/test_kfp_compiler.yaml
--rw-rw-r--   0     1001     1001      521 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/skills/README.md
--rw-rw-r--   0 root         (0) root         (0)     2618 2023-04-06 12:06:25.221651 artistml-sdk-0.2.1.dev9296519/tests/integration_test/skills/test_skill.py
--rw-rw-r--   0     1001     1001       36 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/integration_test/test_gitkeep.py
--rw-rw-r--   0     1001     1001        0 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/unit_test/.gitkeep
--rw-rw-r--   0     1001     1001      115 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/unit_test/clients/test_echo_client.py
--rw-rw-r--   0     1001     1001      121 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/unit_test/clients/test_muses_client.py
--rw-rw-r--   0     1001     1001      767 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/unit_test/thirdparty/kfp/test_kfp_compiler.py
--rw-rw-r--   0     1001     1001    39027 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/unit_test/thirdparty/langchain/state_of_the_union.txt
--rw-rw-r--   0     1001     1001     3654 2023-04-01 05:20:07.170535 artistml-sdk-0.2.1.dev9296519/tests/unit_test/thirdparty/langchain/test_langchain.py
--rw-------   0 root         (0) root         (0)      218 2023-04-06 12:06:27.885632 artistml-sdk-0.2.1.dev9296519/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)       14 2022-11-19 02:44:16.595681 artistml-sdk-0.2.1.dev9751808/README.md
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-19 02:44:16.595870 artistml-sdk-0.2.1.dev9751808/artistml_sdk/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      120 2022-12-24 02:28:28.681184 artistml-sdk-0.2.1.dev9751808/artistml_sdk/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:13.646754 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      125 2022-12-24 02:28:28.722713 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:13.762190 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/__init__.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:13.821368 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:26.014340 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10666 2022-12-21 12:18:12.935822 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    20808 2022-12-21 12:18:12.936473 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    12546 2022-12-21 08:27:26.110926 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     3469 2022-12-21 08:27:26.158982 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.146386 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.268138 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      132 2022-12-24 02:28:28.931243 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.274992 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:26.176105 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      135 2022-12-24 02:28:28.949018 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1790 2022-12-24 02:28:28.962181 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/__pycache__/types_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.345548 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/py.typed
+-rw-r--r--   0 root         (0) root         (0)     2601 2022-12-21 08:27:26.204234 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/types_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     6338 2022-12-21 08:27:26.222109 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/types_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:26.281454 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/types_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:26.365041 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/types_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.437986 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      130 2022-12-24 02:28:28.736695 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.600230 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:26.397368 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      133 2022-12-24 02:28:28.752237 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1752 2022-12-24 02:28:28.765195 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/__pycache__/greeting_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     6746 2022-12-24 02:28:28.910271 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/__pycache__/greeting_service_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     7757 2022-12-24 02:28:29.198046 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/__pycache__/greeting_service_pb2_grpc.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      986 2022-12-21 08:27:26.420090 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/enums_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      165 2022-12-21 08:27:26.437207 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/enums_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:26.469348 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/enums_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:26.496515 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/enums_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     2286 2022-12-21 08:27:26.515697 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     2654 2022-12-21 08:27:26.533186 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:26.576954 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:26.601146 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)    10683 2022-12-21 08:27:26.668158 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    19803 2022-12-21 08:27:26.721912 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    16286 2022-12-21 08:27:26.876425 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     5544 2022-12-21 08:27:26.906117 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.652006 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.687658 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      131 2022-12-24 02:28:29.225876 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:14.781318 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:26.921018 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      134 2022-12-24 02:28:29.242185 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1762 2022-12-24 02:28:29.296804 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/component_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     5697 2022-12-24 02:28:29.281361 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/component_service_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     6513 2022-12-24 02:28:29.265686 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/component_service_pb2_grpc.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     6667 2022-12-24 02:28:29.697976 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/flow_service_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     5599 2022-12-24 02:28:29.681858 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/flow_service_pb2_grpc.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1875 2022-12-24 02:28:29.775663 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/method_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     5182 2022-12-24 02:28:29.762652 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/method_service_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     6291 2022-12-24 02:28:29.737099 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/__pycache__/method_service_pb2_grpc.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     2210 2022-12-21 08:27:27.000552 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     2834 2022-12-21 08:27:27.116044 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:27.149748 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:27.178089 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     8767 2022-12-21 08:27:27.208380 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    15953 2022-12-21 08:27:27.339986 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    13083 2022-12-21 08:27:27.420658 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     4714 2022-12-21 08:27:27.455675 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)    10521 2022-12-21 12:18:12.938076 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    21250 2022-12-21 12:18:12.939171 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    10690 2022-12-21 08:27:27.587354 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     3077 2022-12-21 08:27:27.621352 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     2524 2022-12-21 08:27:27.650215 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     3498 2022-12-21 08:27:27.667297 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:27.692395 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:27.708015 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     8203 2022-12-21 08:27:27.734089 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    15427 2022-12-21 08:27:27.757250 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    12621 2022-12-21 08:27:27.789305 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     4453 2022-12-21 08:27:27.856059 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.003856 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/py.typed
+-rw-r--r--   0 root         (0) root         (0)     2292 2022-12-21 12:18:12.939741 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     2936 2022-12-21 12:18:12.940070 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:27.991959 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:28.026922 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     7953 2022-12-21 08:27:28.058122 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    15015 2022-12-21 08:27:28.113708 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    12159 2022-12-21 08:27:28.154791 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     4192 2022-12-21 08:27:28.202490 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.038027 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      129 2022-12-24 02:28:29.827866 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.051894 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:28.209803 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      132 2022-12-24 02:28:29.857385 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1454 2022-12-24 02:28:29.872486 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/__pycache__/tag_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     4831 2022-12-24 02:28:29.962607 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/__pycache__/tag_service_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     6045 2022-12-24 02:28:29.948476 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/__pycache__/tag_service_pb2_grpc.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.220847 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/py.typed
+-rw-r--r--   0 root         (0) root         (0)     1892 2022-12-21 08:27:28.272867 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     2571 2022-12-21 08:27:28.298377 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:28.331369 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:28.372746 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     7744 2022-12-21 08:27:28.403617 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    14927 2022-12-21 08:27:28.457793 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    12045 2022-12-21 08:27:28.506043 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     4134 2022-12-21 08:27:28.552810 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.244474 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      136 2022-12-24 02:28:28.846697 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:21.347409 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      145 2022-12-24 02:28:28.861116 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1173 2022-12-24 02:28:28.873446 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/__pycache__/chat_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1017 2022-12-24 02:28:28.886314 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/__pycache__/hello_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1327 2022-12-21 08:27:21.441692 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/chat_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      856 2022-12-21 08:27:21.496994 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/chat_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:21.555380 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/chat_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:21.592065 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/chat_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     1168 2022-12-21 08:27:21.640328 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/hello_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      691 2022-12-21 08:27:21.682184 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/hello_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:21.712365 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/hello_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:21.783361 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/hello_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.283819 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:21.799468 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      143 2022-12-24 02:28:29.313808 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)    25100 2022-12-24 02:28:29.330575 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/__pycache__/pipeline_spec_pb2.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     4675 2022-12-21 08:27:21.852362 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/cache_key_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     7414 2022-12-21 08:27:21.891050 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/cache_key_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:21.954620 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/cache_key_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:21.997900 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/cache_key_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)    45900 2022-12-21 08:27:22.186497 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/pipeline_spec_pb2.py
+-rw-r--r--   0 root         (0) root         (0)   127785 2022-12-21 08:27:22.351198 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/pipeline_spec_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:22.415594 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/pipeline_spec_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:22.502628 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/pipeline_spec_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.322430 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpapi/py.typed
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:22.547360 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2494 2022-12-21 08:27:22.661890 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/auth_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     3120 2022-12-21 08:27:22.697963 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/auth_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)     2716 2022-12-21 08:27:22.764427 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/auth_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)      755 2022-12-21 08:27:22.812389 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/auth_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     1631 2022-12-21 08:27:22.858904 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/error_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     1654 2022-12-21 08:27:22.885022 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/error_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:22.911475 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/error_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:22.934798 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/error_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     6779 2022-12-21 08:27:22.971340 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/experiment_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     9310 2022-12-21 08:27:22.995544 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/experiment_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    11954 2022-12-21 08:27:23.022020 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/experiment_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     4045 2022-12-21 08:27:23.046222 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/experiment_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     3280 2022-12-21 08:27:23.066898 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/filter_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     8218 2022-12-21 08:27:23.087463 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/filter_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)     3335 2022-12-21 08:27:23.117279 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/filter_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     1314 2022-12-21 08:27:23.131126 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/filter_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     2044 2022-12-21 08:27:23.153289 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/healthz_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      720 2022-12-21 08:27:23.184247 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/healthz_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)     2735 2022-12-21 08:27:23.203423 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/healthz_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)      851 2022-12-21 08:27:23.219155 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/healthz_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     7802 2022-12-21 08:27:23.251987 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/job_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    15115 2022-12-21 08:27:23.273738 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/job_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    10878 2022-12-21 08:27:23.304291 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/job_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     3152 2022-12-21 08:27:23.332287 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/job_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     1250 2022-12-21 08:27:23.385486 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/parameter_pb2.py
+-rw-r--r--   0 root         (0) root         (0)      739 2022-12-21 08:27:23.426487 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/parameter_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:23.530109 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/parameter_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:23.596686 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/parameter_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)    12472 2022-12-21 08:27:23.639715 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    20600 2022-12-21 08:27:23.794952 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    23234 2022-12-21 08:27:24.027021 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     8113 2022-12-21 08:27:24.060323 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     2632 2022-12-21 08:27:24.389436 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_spec_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     4699 2022-12-21 08:27:24.418072 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_spec_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:24.457095 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_spec_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:24.665613 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/pipeline_spec_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.521076 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/py.typed
+-rw-r--r--   0 root         (0) root         (0)     2629 2022-12-21 08:27:24.712733 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/report_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     1364 2022-12-21 08:27:24.759388 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/report_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)     4585 2022-12-21 08:27:24.821188 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/report_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     1193 2022-12-21 08:27:24.892680 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/report_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     2145 2022-12-21 08:27:24.925688 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/resource_reference_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     3587 2022-12-21 08:27:24.987840 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/resource_reference_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)      159 2022-12-21 08:27:25.020555 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/resource_reference_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)       76 2022-12-21 08:27:25.094155 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/resource_reference_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)    11517 2022-12-21 08:27:25.164983 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/run_pb2.py
+-rw-r--r--   0 root         (0) root         (0)    22612 2022-12-21 08:27:25.224620 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/run_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)    17824 2022-12-21 08:27:25.309209 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/run_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     5354 2022-12-21 08:27:25.361895 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/run_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     3768 2022-12-21 08:27:25.425467 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/task_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     6629 2022-12-21 08:27:25.489048 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/task_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)     4351 2022-12-21 08:27:25.572003 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/task_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)     1356 2022-12-21 08:27:25.622616 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/task_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)     2840 2022-12-21 08:27:25.695886 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/visualization_pb2.py
+-rw-r--r--   0 root         (0) root         (0)     3874 2022-12-21 08:27:25.748459 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/visualization_pb2.pyi
+-rw-r--r--   0 root         (0) root         (0)     2914 2022-12-21 08:27:25.804419 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/visualization_pb2_grpc.py
+-rw-r--r--   0 root         (0) root         (0)      869 2022-12-21 08:27:25.874078 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/visualization_pb2_grpc.pyi
+-rw-r--r--   0 root         (0) root         (0)        0 2022-12-21 08:27:15.255062 artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/py.typed
+-rw-r--r--   0 root         (0) root         (0)      156 2022-12-14 04:52:54.814198 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      287 2022-12-24 02:28:28.694604 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1365 2022-12-24 02:28:28.704594 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/__pycache__/echo.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     9622 2022-12-24 02:28:29.989688 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/__pycache__/muses.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     2323 2022-12-24 02:28:30.708105 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/__pycache__/tag.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      928 2022-12-17 05:13:27.958600 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/echo.py
+-rw-r--r--   0 root         (0) root         (0)    12647 2022-12-21 12:18:12.941184 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/muses.py
+-rw-r--r--   0 root         (0) root         (0)     2110 2022-12-16 15:05:29.633698 artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/tag.py
+-rw-r--r--   0 root         (0) root         (0)      945 2022-12-14 04:52:54.815436 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1057 2022-12-24 02:28:29.016434 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      269 2022-12-06 10:58:41.636870 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      358 2022-12-24 02:28:29.032367 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     3879 2022-12-24 02:28:29.059700 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/__pycache__/grpc_channel.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1786 2022-12-24 02:28:29.048452 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/__pycache__/grpc_client.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1434 2022-12-24 02:28:29.157947 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/__pycache__/grpc_invoke_wrapper.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     3535 2022-12-06 10:58:41.636997 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/grpc_channel.py
+-rw-r--r--   0 root         (0) root         (0)     1207 2022-12-11 03:51:44.858613 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/grpc_client.py
+-rw-r--r--   0 root         (0) root         (0)      835 2022-12-06 10:58:41.637287 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/grpc_invoke_wrapper.py
+-rw-r--r--   0 root         (0) root         (0)       43 2022-12-06 10:58:41.637540 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      190 2022-12-24 02:28:29.170767 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      899 2022-12-24 02:28:29.182445 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/__pycache__/echo.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1354 2022-12-24 02:28:29.208338 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/__pycache__/muses.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      874 2022-12-24 02:28:29.914697 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/__pycache__/tag.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      397 2022-12-20 08:19:34.915427 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/echo.py
+-rw-r--r--   0 root         (0) root         (0)      742 2022-12-21 12:18:12.941716 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/muses.py
+-rw-r--r--   0 root         (0) root         (0)      370 2022-12-20 08:19:34.918300 artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/tag.py
+-rw-r--r--   0 root         (0) root         (0)      309 2022-12-18 12:47:05.432971 artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      384 2022-12-24 02:28:30.673077 artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     1003 2022-12-24 02:28:30.686440 artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/__pycache__/_protobuf_message.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      629 2022-12-24 02:28:30.696679 artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/__pycache__/_yaml.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)      865 2022-12-18 12:47:05.433312 artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/_protobuf_message.py
+-rw-r--r--   0 root         (0) root         (0)      316 2022-12-21 12:18:12.941953 artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/_yaml.py
+-rw-r--r--   0 root         (0) root         (0)      271 2022-12-06 10:58:41.637906 artistml-sdk-0.2.1.dev9751808/artistml_sdk/logger/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      366 2022-12-24 02:28:29.106974 artistml-sdk-0.2.1.dev9751808/artistml_sdk/logger/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     8007 2022-12-24 02:28:29.124750 artistml-sdk-0.2.1.dev9751808/artistml_sdk/logger/__pycache__/logger.cpython-38.pyc
+-rw-r--r--   0 root         (0) root         (0)     9218 2022-12-06 10:58:41.638060 artistml-sdk-0.2.1.dev9751808/artistml_sdk/logger/logger.py
+-rw-r--r--   0 root         (0) root         (0)     3240 2022-12-23 15:34:34.182728 artistml-sdk-0.2.1.dev9751808/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-19 02:44:16.597303 artistml-sdk-0.2.1.dev9751808/tests/.gitkeep
+-rw-r--r--   0 root         (0) root         (0)      291 2022-12-11 03:51:44.860270 artistml-sdk-0.2.1.dev9751808/tests/integration_test/clients/test_echo_client.py
+-rw-r--r--   0 root         (0) root         (0)     5507 2022-12-21 12:18:12.942336 artistml-sdk-0.2.1.dev9751808/tests/integration_test/clients/test_muses_client.py
+-rw-r--r--   0 root         (0) root         (0)      714 2022-12-18 05:59:44.306887 artistml-sdk-0.2.1.dev9751808/tests/integration_test/clients/test_tag_client.py
+-rw-r--r--   0 root         (0) root         (0)       36 2022-12-10 08:36:37.344655 artistml-sdk-0.2.1.dev9751808/tests/integration_test/test_gitkeep.py
+-rw-r--r--   0 root         (0) root         (0)        0 2022-11-19 02:44:16.597485 artistml-sdk-0.2.1.dev9751808/tests/unit_test/.gitkeep
+-rw-r--r--   0 root         (0) root         (0)      115 2022-12-11 03:51:44.860773 artistml-sdk-0.2.1.dev9751808/tests/unit_test/clients/test_echo_client.py
+-rw-r--r--   0 root         (0) root         (0)      121 2022-12-11 03:51:44.861253 artistml-sdk-0.2.1.dev9751808/tests/unit_test/clients/test_muses_client.py
+-rw-r--r--   0 root         (0) root         (0)      728 2022-12-18 12:47:05.435837 artistml-sdk-0.2.1.dev9751808/tests/unit_test/thirdparty/kfp/test_kfp_compiler.py
+-rw-------   0 root         (0) root         (0)      211 2022-12-24 02:28:38.975661 artistml-sdk-0.2.1.dev9751808/PKG-INFO
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2.py`

 * *Files 1% similar despite different names*

```diff
@@ -14,15 +14,15 @@
 from ...common.v1 import types_pb2 as common_dot_v1_dot_types__pb2
 from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
 from google.api import client_pb2 as google_dot_api_dot_client__pb2
 from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
 from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61ssoc/v1/assoc_service.proto\x12\x08\x61ssoc.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"S\n\x12\x43reateAssocRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12%\n\x05\x61ssoc\x18\x02 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x05\x61ssoc\"n\n\x13\x43reateAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xd2\x01\n\x12UpdateAssocRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12\x13\n\x05to_id\x18\x02 \x01(\x03R\x04toId\x12*\n\x06\x61_type\x18\x03 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12%\n\x05\x61ssoc\x18\x04 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x05\x61ssoc\x12;\n\x0bupdate_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"n\n\x13UpdateAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xa2\x02\n\x11ListAssocsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12@\n\roption_filter\x18\x05 \x01(\x0b\x32\x1b.assoc.v1.AssocOptionFilterR\x0coptionFilter\"\x96\x02\n\x12ListAssocsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12>\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32$.assoc.v1.ListAssocsResponse.DetailsR\x07\x64\x65tails\x1a\x91\x01\n\x07\x44\x65tails\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x0f.assoc.v1.AssocR\x05items\x12>\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x1b.assoc.v1.ListAssocsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\"n\n\x12\x44\x65leteAssocRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12\x13\n\x05to_id\x18\x02 \x01(\x03R\x04toId\x12*\n\x06\x61_type\x18\x03 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\"n\n\x13\x44\x65leteAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xad\x01\n\x13\x44\x65leteAssocsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12@\n\roption_filter\x18\x03 \x01(\x0b\x32\x1b.assoc.v1.AssocOptionFilterR\x0coptionFilter\"^\n\x14\x44\x65leteAssocsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails\"Y\n\x12\x43ountAssocsRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12*\n\x06\x61_type\x18\x02 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\"]\n\x13\x43ountAssocsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x01(\x03R\x07\x64\x65tails\"k\n\x0fGetAssocRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12*\n\x06\x61_type\x18\x02 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12\x13\n\x05to_id\x18\x03 \x01(\x03R\x04toId\"k\n\x10GetAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xf7\x01\n\x05\x41ssoc\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x17\n\x07\x66rom_id\x18\x04 \x01(\x03R\x06\x66romId\x12\x13\n\x05to_id\x18\x05 \x01(\x03R\x04toId\x12*\n\x06\x61_type\x18\x06 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12\x12\n\x04meta\x18\x07 \x01(\tR\x04meta:6\xea\x41\x33\n$github.com.artistml.apis/AssocEntity\x12\x0b\x61ssocs/{id}\"o\n\x11\x41ssocOptionFilter\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12*\n\x06\x61_type\x18\x02 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12\x15\n\x06to_ids\x18\x03 \x03(\x03R\x05toIds*\xb7\x02\n\tAssocType\x12\x1a\n\x16\x41SSOC_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x41SSOC_TYPE_TAGBY\x10\x01\x12\x14\n\x10\x41SSOC_TYPE_TAGTO\x10\x02\x12\x19\n\x15\x41SSOC_TYPE_CREATED_BY\x10\x03\x12\x1b\n\x17\x41SSOC_TYPE_CREATED_WITH\x10\x04\x12\x1b\n\x17\x41SSOC_TYPE_INHERIT_FROM\x10\x05\x12\x18\n\x14\x41SSOC_TYPE_EXTEND_TO\x10\x06\x12\x1b\n\x17\x41SSOC_TYPE_FLOW_HISTORY\x10\x07\x12\x1b\n\x17\x41SSOC_TYPE_HISTORY_FLOW\x10\x08\x12\x1b\n\x17\x41SSOC_TYPE_CREATE_TOKEN\x10\t\x12\x1c\n\x18\x41SSOC_TYPE_TOKEN_CREATED\x10\n2\xe4\x06\n\x0c\x41ssocService\x12t\n\x0b\x43reateAssoc\x12\x1c.assoc.v1.CreateAssocRequest\x1a\x1d.assoc.v1.CreateAssocResponse\"(\xda\x41\x0cparent,assoc\x82\xd3\xe4\x93\x02\x13\"\n/v1/assocs:\x05\x61ssoc\x12\x82\x01\n\x0bUpdateAssoc\x12\x1c.assoc.v1.UpdateAssocRequest\x1a\x1d.assoc.v1.UpdateAssocResponse\"6\x82\xd3\xe4\x93\x02\x30\x32+/v1/assocs/{from_id=*}/{a_type=*}/{to_id=*}:\x01*\x12h\n\nListAssocs\x12\x1b.assoc.v1.ListAssocsRequest\x1a\x1c.assoc.v1.ListAssocsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v1/assocs/resources:\x01*\x12}\n\x0b\x44\x65leteAssoc\x12\x1c.assoc.v1.DeleteAssocRequest\x1a\x1d.assoc.v1.DeleteAssocResponse\"1\x82\xd3\xe4\x93\x02+*)/v1/assocs/{from_id=*}/{a_type=*}/{to_id}\x12\x64\n\x0c\x44\x65leteAssocs\x12\x1d.assoc.v1.DeleteAssocsRequest\x1a\x1e.assoc.v1.DeleteAssocsResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x32\n/v1/assocs:\x01*\x12u\n\x0b\x43ountAssocs\x12\x1c.assoc.v1.CountAssocsRequest\x1a\x1d.assoc.v1.CountAssocsResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/assocs/{from_id=*}/{a_type=*}\x12v\n\x08GetAssoc\x12\x19.assoc.v1.GetAssocRequest\x1a\x1a.assoc.v1.GetAssocResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v1/assocs/{from_id=*}/{a_type=*}/{to_id=*}\x1a\x1b\xca\x41\x18github.com/artistml/apisB.Z,github.com/artistml/apis/go/assoc/v1;assocv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61ssoc/v1/assoc_service.proto\x12\x08\x61ssoc.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\"S\n\x12\x43reateAssocRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12%\n\x05\x61ssoc\x18\x02 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x05\x61ssoc\"n\n\x13\x43reateAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xd2\x01\n\x12UpdateAssocRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12\x13\n\x05to_id\x18\x02 \x01(\x03R\x04toId\x12*\n\x06\x61_type\x18\x03 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12%\n\x05\x61ssoc\x18\x04 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x05\x61ssoc\x12;\n\x0bupdate_mask\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"n\n\x13UpdateAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xa2\x02\n\x11ListAssocsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12@\n\roption_filter\x18\x05 \x01(\x0b\x32\x1b.assoc.v1.AssocOptionFilterR\x0coptionFilter\"\x96\x02\n\x12ListAssocsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12>\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32$.assoc.v1.ListAssocsResponse.DetailsR\x07\x64\x65tails\x1a\x91\x01\n\x07\x44\x65tails\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x0f.assoc.v1.AssocR\x05items\x12>\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x1b.assoc.v1.ListAssocsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\"n\n\x12\x44\x65leteAssocRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12\x13\n\x05to_id\x18\x02 \x01(\x03R\x04toId\x12*\n\x06\x61_type\x18\x03 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\"n\n\x13\x44\x65leteAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xad\x01\n\x13\x44\x65leteAssocsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12@\n\roption_filter\x18\x03 \x01(\x0b\x32\x1b.assoc.v1.AssocOptionFilterR\x0coptionFilter\"^\n\x14\x44\x65leteAssocsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails\"Y\n\x12\x43ountAssocsRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12*\n\x06\x61_type\x18\x02 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\"]\n\x13\x43ountAssocsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x01(\x03R\x07\x64\x65tails\"k\n\x0fGetAssocRequest\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12*\n\x06\x61_type\x18\x02 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12\x13\n\x05to_id\x18\x03 \x01(\x03R\x04toId\"k\n\x10GetAssocResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12)\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0f.assoc.v1.AssocR\x07\x64\x65tails\"\xf7\x01\n\x05\x41ssoc\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x17\n\x07\x66rom_id\x18\x04 \x01(\x03R\x06\x66romId\x12\x13\n\x05to_id\x18\x05 \x01(\x03R\x04toId\x12*\n\x06\x61_type\x18\x06 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12\x12\n\x04meta\x18\x07 \x01(\tR\x04meta:6\xea\x41\x33\n$github.com.artistml.apis/AssocEntity\x12\x0b\x61ssocs/{id}\"o\n\x11\x41ssocOptionFilter\x12\x17\n\x07\x66rom_id\x18\x01 \x01(\x03R\x06\x66romId\x12*\n\x06\x61_type\x18\x02 \x01(\x0e\x32\x13.assoc.v1.AssocTypeR\x05\x61Type\x12\x15\n\x06to_ids\x18\x03 \x03(\x03R\x05toIds*\xfc\x01\n\tAssocType\x12\x1a\n\x16\x41SSOC_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x41SSOC_TYPE_TAGBY\x10\x01\x12\x14\n\x10\x41SSOC_TYPE_TAGTO\x10\x02\x12\x19\n\x15\x41SSOC_TYPE_CREATED_BY\x10\x03\x12\x1b\n\x17\x41SSOC_TYPE_CREATED_WITH\x10\x04\x12\x1b\n\x17\x41SSOC_TYPE_INHERIT_FROM\x10\x05\x12\x18\n\x14\x41SSOC_TYPE_EXTEND_TO\x10\x06\x12\x1b\n\x17\x41SSOC_TYPE_FLOW_HISTORY\x10\x07\x12\x1b\n\x17\x41SSOC_TYPE_HISTORY_FLOW\x10\x08\x32\xe4\x06\n\x0c\x41ssocService\x12t\n\x0b\x43reateAssoc\x12\x1c.assoc.v1.CreateAssocRequest\x1a\x1d.assoc.v1.CreateAssocResponse\"(\xda\x41\x0cparent,assoc\x82\xd3\xe4\x93\x02\x13\"\n/v1/assocs:\x05\x61ssoc\x12\x82\x01\n\x0bUpdateAssoc\x12\x1c.assoc.v1.UpdateAssocRequest\x1a\x1d.assoc.v1.UpdateAssocResponse\"6\x82\xd3\xe4\x93\x02\x30\x32+/v1/assocs/{from_id=*}/{a_type=*}/{to_id=*}:\x01*\x12h\n\nListAssocs\x12\x1b.assoc.v1.ListAssocsRequest\x1a\x1c.assoc.v1.ListAssocsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v1/assocs/resources:\x01*\x12}\n\x0b\x44\x65leteAssoc\x12\x1c.assoc.v1.DeleteAssocRequest\x1a\x1d.assoc.v1.DeleteAssocResponse\"1\x82\xd3\xe4\x93\x02+*)/v1/assocs/{from_id=*}/{a_type=*}/{to_id}\x12\x64\n\x0c\x44\x65leteAssocs\x12\x1d.assoc.v1.DeleteAssocsRequest\x1a\x1e.assoc.v1.DeleteAssocsResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x32\n/v1/assocs:\x01*\x12u\n\x0b\x43ountAssocs\x12\x1c.assoc.v1.CountAssocsRequest\x1a\x1d.assoc.v1.CountAssocsResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/assocs/{from_id=*}/{a_type=*}\x12v\n\x08GetAssoc\x12\x19.assoc.v1.GetAssocRequest\x1a\x1a.assoc.v1.GetAssocResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v1/assocs/{from_id=*}/{a_type=*}/{to_id=*}\x1a\x1b\xca\x41\x18github.com/artistml/apisB.Z,github.com/artistml/apis/go/assoc/v1;assocv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'assoc.v1.assoc_service_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   DESCRIPTOR._serialized_options = b'Z,github.com/artistml/apis/go/assoc/v1;assocv1'
@@ -41,15 +41,15 @@
   _ASSOCSERVICE.methods_by_name['DeleteAssocs']._options = None
   _ASSOCSERVICE.methods_by_name['DeleteAssocs']._serialized_options = b'\202\323\344\223\002\0172\n/v1/assocs:\001*'
   _ASSOCSERVICE.methods_by_name['CountAssocs']._options = None
   _ASSOCSERVICE.methods_by_name['CountAssocs']._serialized_options = b'\202\323\344\223\002#\022!/v1/assocs/{from_id=*}/{a_type=*}'
   _ASSOCSERVICE.methods_by_name['GetAssoc']._options = None
   _ASSOCSERVICE.methods_by_name['GetAssoc']._serialized_options = b'\202\323\344\223\002-\022+/v1/assocs/{from_id=*}/{a_type=*}/{to_id=*}'
   _ASSOCTYPE._serialized_start=2541
-  _ASSOCTYPE._serialized_end=2852
+  _ASSOCTYPE._serialized_end=2793
   _CREATEASSOCREQUEST._serialized_start=181
   _CREATEASSOCREQUEST._serialized_end=264
   _CREATEASSOCRESPONSE._serialized_start=266
   _CREATEASSOCRESPONSE._serialized_end=376
   _UPDATEASSOCREQUEST._serialized_start=379
   _UPDATEASSOCREQUEST._serialized_end=589
   _UPDATEASSOCRESPONSE._serialized_start=591
@@ -76,10 +76,10 @@
   _GETASSOCREQUEST._serialized_end=2066
   _GETASSOCRESPONSE._serialized_start=2068
   _GETASSOCRESPONSE._serialized_end=2175
   _ASSOC._serialized_start=2178
   _ASSOC._serialized_end=2425
   _ASSOCOPTIONFILTER._serialized_start=2427
   _ASSOCOPTIONFILTER._serialized_end=2538
-  _ASSOCSERVICE._serialized_start=2855
-  _ASSOCSERVICE._serialized_end=3723
+  _ASSOCSERVICE._serialized_start=2796
+  _ASSOCSERVICE._serialized_end=3664
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2.pyi`

 * *Files 5% similar despite different names*

```diff
@@ -40,20 +40,14 @@
 
     ASSOC_TYPE_FLOW_HISTORY: _AssocType.ValueType  # 7
     """an history version flow of itself, to_id is the version generated with timestamp."""
 
     ASSOC_TYPE_HISTORY_FLOW: _AssocType.ValueType  # 8
     """version of an flow, from_id is the generated by backend when an object has a new version, to_id is the id of this flow."""
 
-    ASSOC_TYPE_CREATE_TOKEN: _AssocType.ValueType  # 9
-    """user_id create token_id."""
-
-    ASSOC_TYPE_TOKEN_CREATED: _AssocType.ValueType  # 10
-    """token_id created by user_id."""
-
 class AssocType(_AssocType, metaclass=_AssocTypeEnumTypeWrapper):
     """type of association, type should be defined in pair, eg:
      ASSOC_TYPE_TAGBY = 1;
      ASSOC_TYPE_TAGTO = 2;
     """
     pass
 
@@ -78,20 +72,14 @@
 
 ASSOC_TYPE_FLOW_HISTORY: AssocType.ValueType  # 7
 """an history version flow of itself, to_id is the version generated with timestamp."""
 
 ASSOC_TYPE_HISTORY_FLOW: AssocType.ValueType  # 8
 """version of an flow, from_id is the generated by backend when an object has a new version, to_id is the id of this flow."""
 
-ASSOC_TYPE_CREATE_TOKEN: AssocType.ValueType  # 9
-"""user_id create token_id."""
-
-ASSOC_TYPE_TOKEN_CREATED: AssocType.ValueType  # 10
-"""token_id created by user_id."""
-
 global___AssocType = AssocType
 
 
 class CreateAssocRequest(google.protobuf.message.Message):
     """Request message for [AssocService.CreateAssoc][v1.AssocService.CreateAssoc]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARENT_FIELD_NUMBER: builtins.int
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/assoc/v1/assoc_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,74 +1,71 @@
 # -*- coding: utf-8 -*-
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
-# source: auth/v1/token_service.proto
+# source: muses/v1/run_service.proto
 """Generated protocol buffer code."""
 from google.protobuf.internal import builder as _builder
 from google.protobuf import descriptor as _descriptor
 from google.protobuf import descriptor_pool as _descriptor_pool
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
 
 from ...common.v1 import types_pb2 as common_dot_v1_dot_types__pb2
 from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
 from google.api import client_pb2 as google_dot_api_dot_client__pb2
-from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
 from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
-from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
+from ...muses.v1 import run_pb2 as muses_dot_v1_dot_run__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61uth/v1/token_service.proto\x12\x07\x61uth.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe5\x03\n\x05Token\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x30\n\x07payload\x18\x04 \x01(\x0b\x32\x16.auth.v1.Token.PayloadR\x07payload\x1a\xa2\x02\n\x07Payload\x12\x12\n\x04uuid\x18\x01 \x01(\tR\x04uuid\x12\x17\n\x07user_id\x18\x02 \x01(\x03R\x06userId\x12\x37\n\tissued_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08issuedAt\x12\x39\n\nexpired_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiredAt\x12\x1a\n\x08\x64uration\x18\x05 \x01(\x03R\x08\x64uration\x12\x30\n\ttime_unit\x18\x06 \x01(\x0e\x32\x13.common.v1.TimeUnitR\x08timeUnit\x12\x12\n\x04name\x18\x07 \x01(\tR\x04name\x12\x14\n\x05token\x18\x08 \x01(\tR\x05token:;\xea\x41\x38\n$github.com.artistml.apis/TokenEntity\x12\x10\x61uth/tokens/{id}\",\n\x11TokenOptionFilter\x12\x17\n\x07user_id\x18\x01 \x01(\x03R\x06userId\"R\n\x12\x43reateTokenRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12$\n\x05token\x18\x02 \x01(\x0b\x32\x0e.auth.v1.TokenR\x05token\"m\n\x13\x43reateTokenResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.auth.v1.TokenR\x07\x64\x65tails\"r\n\x0fGetTokenRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x37\n\tread_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"j\n\x10GetTokenResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.auth.v1.TokenR\x07\x64\x65tails\"\xa1\x02\n\x11ListTokensRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12?\n\roption_filter\x18\x05 \x01(\x0b\x32\x1a.auth.v1.TokenOptionFilterR\x0coptionFilter\"\x93\x02\n\x12ListTokensResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12=\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32#.auth.v1.ListTokensResponse.DetailsR\x07\x64\x65tails\x1a\x8f\x01\n\x07\x44\x65tails\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x0e.auth.v1.TokenR\x05items\x12=\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x1a.auth.v1.ListTokensRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\"<\n\x12\x44\x65leteTokenRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\"m\n\x13\x44\x65leteTokenResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.auth.v1.TokenR\x07\x64\x65tails\"\xac\x01\n\x13\x44\x65leteTokensRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12?\n\roption_filter\x18\x03 \x01(\x0b\x32\x1a.auth.v1.TokenOptionFilterR\x0coptionFilter\"^\n\x14\x44\x65leteTokensResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails2\x8b\x05\n\x0cTokenService\x12\x80\x01\n\x0b\x43reateToken\x12\x1b.auth.v1.CreateTokenRequest\x1a\x1c.auth.v1.CreateTokenResponse\"6\xda\x41\x0cparent,token\x82\xd3\xe4\x93\x02!\"\x18/v1/{parent=auth}/tokens:\x05token\x12t\n\x08GetToken\x12\x18.auth.v1.GetTokenRequest\x1a\x19.auth.v1.GetTokenResponse\"3\xda\x41\tparent,id\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=auth}/tokens/{id=*}\x12t\n\nListTokens\x12\x1a.auth.v1.ListTokensRequest\x1a\x1b.auth.v1.ListTokensResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/{parent=auth}/tokens/resources:\x01*\x12}\n\x0b\x44\x65leteToken\x12\x1b.auth.v1.DeleteTokenRequest\x1a\x1c.auth.v1.DeleteTokenResponse\"3\xda\x41\tparent,id\x82\xd3\xe4\x93\x02!*\x1f/v1/{parent=auth}/tokens/{id=*}\x12p\n\x0c\x44\x65leteTokens\x12\x1c.auth.v1.DeleteTokensRequest\x1a\x1d.auth.v1.DeleteTokensResponse\"#\x82\xd3\xe4\x93\x02\x1d\x32\x18/v1/{parent=auth}/tokens:\x01*\x1a\x1b\xca\x41\x18github.com/artistml/apisB,Z*github.com/artistml/apis/go/auth/v1;authv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1amuses/v1/run_service.proto\x12\x08muses.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a google/protobuf/field_mask.proto\x1a\x12muses/v1/run.proto\"K\n\x10\x43reateRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1f\n\x03run\x18\x02 \x01(\x0b\x32\r.muses.v1.RunR\x03run\"j\n\x11\x43reateRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"p\n\rGetRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x37\n\tread_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"g\n\x0eGetRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"\x88\x01\n\x10UpdateRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1f\n\x03run\x18\x02 \x01(\x0b\x32\r.muses.v1.RunR\x03run\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"j\n\x11UpdateRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"\x9e\x02\n\x0fListRunsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12>\n\roption_filter\x18\x05 \x01(\x0b\x32\x19.muses.v1.RunOptionFilterR\x0coptionFilter\"\x8e\x02\n\x10ListRunsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12<\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\".muses.v1.ListRunsResponse.DetailsR\x07\x64\x65tails\x1a\x8d\x01\n\x07\x44\x65tails\x12#\n\x05items\x18\x01 \x03(\x0b\x32\r.muses.v1.RunR\x05items\x12<\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x19.muses.v1.ListRunsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\":\n\x10\x44\x65leteRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\"j\n\x11\x44\x65leteRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"\xa9\x01\n\x11\x44\x65leteRunsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12>\n\roption_filter\x18\x03 \x01(\x0b\x32\x19.muses.v1.RunOptionFilterR\x0coptionFilter\"\\\n\x12\x44\x65leteRunsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails2\x88\x06\n\nRunService\x12y\n\tCreateRun\x12\x1a.muses.v1.CreateRunRequest\x1a\x1b.muses.v1.CreateRunResponse\"3\xda\x41\nparent,run\x82\xd3\xe4\x93\x02 \"\x19/v1/{parent=flows/*}/runs:\x03run\x12q\n\x06GetRun\x12\x17.muses.v1.GetRunRequest\x1a\x18.muses.v1.GetRunResponse\"4\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\"\x12 /v1/{parent=flows/*}/runs/{id=*}\x12\x90\x01\n\tUpdateRun\x12\x1a.muses.v1.UpdateRunRequest\x1a\x1b.muses.v1.UpdateRunResponse\"J\xda\x41\x16parent,run,update_mask\x82\xd3\xe4\x93\x02+2$/v1/{parent=flows/*}/runs/{run.id=*}:\x03run\x12q\n\x08ListRuns\x12\x19.muses.v1.ListRunsRequest\x1a\x1a.muses.v1.ListRunsResponse\".\x82\xd3\xe4\x93\x02(\"#/v1/{parent=flows/*}/runs/resources:\x01*\x12z\n\tDeleteRun\x12\x1a.muses.v1.DeleteRunRequest\x1a\x1b.muses.v1.DeleteRunResponse\"4\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\"* /v1/{parent=flows/*}/runs/{id=*}\x12m\n\nDeleteRuns\x12\x1b.muses.v1.DeleteRunsRequest\x1a\x1c.muses.v1.DeleteRunsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x32\x19/v1/{parent=flows/*}/runs:\x01*\x1a\x1b\xca\x41\x18github.com/artistml/apisB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
-_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth.v1.token_service_pb2', globals())
+_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'muses.v1.run_service_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
-  DESCRIPTOR._serialized_options = b'Z*github.com/artistml/apis/go/auth/v1;authv1'
-  _TOKEN._options = None
-  _TOKEN._serialized_options = b'\352A8\n$github.com.artistml.apis/TokenEntity\022\020auth/tokens/{id}'
-  _TOKENSERVICE._options = None
-  _TOKENSERVICE._serialized_options = b'\312A\030github.com/artistml/apis'
-  _TOKENSERVICE.methods_by_name['CreateToken']._options = None
-  _TOKENSERVICE.methods_by_name['CreateToken']._serialized_options = b'\332A\014parent,token\202\323\344\223\002!\"\030/v1/{parent=auth}/tokens:\005token'
-  _TOKENSERVICE.methods_by_name['GetToken']._options = None
-  _TOKENSERVICE.methods_by_name['GetToken']._serialized_options = b'\332A\tparent,id\202\323\344\223\002!\022\037/v1/{parent=auth}/tokens/{id=*}'
-  _TOKENSERVICE.methods_by_name['ListTokens']._options = None
-  _TOKENSERVICE.methods_by_name['ListTokens']._serialized_options = b'\202\323\344\223\002\'\"\"/v1/{parent=auth}/tokens/resources:\001*'
-  _TOKENSERVICE.methods_by_name['DeleteToken']._options = None
-  _TOKENSERVICE.methods_by_name['DeleteToken']._serialized_options = b'\332A\tparent,id\202\323\344\223\002!*\037/v1/{parent=auth}/tokens/{id=*}'
-  _TOKENSERVICE.methods_by_name['DeleteTokens']._options = None
-  _TOKENSERVICE.methods_by_name['DeleteTokens']._serialized_options = b'\202\323\344\223\002\0352\030/v1/{parent=auth}/tokens:\001*'
-  _TOKEN._serialized_start=213
-  _TOKEN._serialized_end=698
-  _TOKEN_PAYLOAD._serialized_start=347
-  _TOKEN_PAYLOAD._serialized_end=637
-  _TOKENOPTIONFILTER._serialized_start=700
-  _TOKENOPTIONFILTER._serialized_end=744
-  _CREATETOKENREQUEST._serialized_start=746
-  _CREATETOKENREQUEST._serialized_end=828
-  _CREATETOKENRESPONSE._serialized_start=830
-  _CREATETOKENRESPONSE._serialized_end=939
-  _GETTOKENREQUEST._serialized_start=941
-  _GETTOKENREQUEST._serialized_end=1055
-  _GETTOKENRESPONSE._serialized_start=1057
-  _GETTOKENRESPONSE._serialized_end=1163
-  _LISTTOKENSREQUEST._serialized_start=1166
-  _LISTTOKENSREQUEST._serialized_end=1455
-  _LISTTOKENSRESPONSE._serialized_start=1458
-  _LISTTOKENSRESPONSE._serialized_end=1733
-  _LISTTOKENSRESPONSE_DETAILS._serialized_start=1590
-  _LISTTOKENSRESPONSE_DETAILS._serialized_end=1733
-  _DELETETOKENREQUEST._serialized_start=1735
-  _DELETETOKENREQUEST._serialized_end=1795
-  _DELETETOKENRESPONSE._serialized_start=1797
-  _DELETETOKENRESPONSE._serialized_end=1906
-  _DELETETOKENSREQUEST._serialized_start=1909
-  _DELETETOKENSREQUEST._serialized_end=2081
-  _DELETETOKENSRESPONSE._serialized_start=2083
-  _DELETETOKENSRESPONSE._serialized_end=2177
-  _TOKENSERVICE._serialized_start=2180
-  _TOKENSERVICE._serialized_end=2831
+  DESCRIPTOR._serialized_options = b'Z,github.com/artistml/apis/go/muses/v1;musesv1'
+  _RUNSERVICE._options = None
+  _RUNSERVICE._serialized_options = b'\312A\030github.com/artistml/apis'
+  _RUNSERVICE.methods_by_name['CreateRun']._options = None
+  _RUNSERVICE.methods_by_name['CreateRun']._serialized_options = b'\332A\nparent,run\202\323\344\223\002 \"\031/v1/{parent=flows/*}/runs:\003run'
+  _RUNSERVICE.methods_by_name['GetRun']._options = None
+  _RUNSERVICE.methods_by_name['GetRun']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\"\022 /v1/{parent=flows/*}/runs/{id=*}'
+  _RUNSERVICE.methods_by_name['UpdateRun']._options = None
+  _RUNSERVICE.methods_by_name['UpdateRun']._serialized_options = b'\332A\026parent,run,update_mask\202\323\344\223\002+2$/v1/{parent=flows/*}/runs/{run.id=*}:\003run'
+  _RUNSERVICE.methods_by_name['ListRuns']._options = None
+  _RUNSERVICE.methods_by_name['ListRuns']._serialized_options = b'\202\323\344\223\002(\"#/v1/{parent=flows/*}/runs/resources:\001*'
+  _RUNSERVICE.methods_by_name['DeleteRun']._options = None
+  _RUNSERVICE.methods_by_name['DeleteRun']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\"* /v1/{parent=flows/*}/runs/{id=*}'
+  _RUNSERVICE.methods_by_name['DeleteRuns']._options = None
+  _RUNSERVICE.methods_by_name['DeleteRuns']._serialized_options = b'\202\323\344\223\002\0362\031/v1/{parent=flows/*}/runs:\001*'
+  _CREATERUNREQUEST._serialized_start=172
+  _CREATERUNREQUEST._serialized_end=247
+  _CREATERUNRESPONSE._serialized_start=249
+  _CREATERUNRESPONSE._serialized_end=355
+  _GETRUNREQUEST._serialized_start=357
+  _GETRUNREQUEST._serialized_end=469
+  _GETRUNRESPONSE._serialized_start=471
+  _GETRUNRESPONSE._serialized_end=574
+  _UPDATERUNREQUEST._serialized_start=577
+  _UPDATERUNREQUEST._serialized_end=713
+  _UPDATERUNRESPONSE._serialized_start=715
+  _UPDATERUNRESPONSE._serialized_end=821
+  _LISTRUNSREQUEST._serialized_start=824
+  _LISTRUNSREQUEST._serialized_end=1110
+  _LISTRUNSRESPONSE._serialized_start=1113
+  _LISTRUNSRESPONSE._serialized_end=1383
+  _LISTRUNSRESPONSE_DETAILS._serialized_start=1242
+  _LISTRUNSRESPONSE_DETAILS._serialized_end=1383
+  _DELETERUNREQUEST._serialized_start=1385
+  _DELETERUNREQUEST._serialized_end=1443
+  _DELETERUNRESPONSE._serialized_start=1445
+  _DELETERUNRESPONSE._serialized_end=1551
+  _DELETERUNSREQUEST._serialized_start=1554
+  _DELETERUNSREQUEST._serialized_end=1723
+  _DELETERUNSRESPONSE._serialized_start=1725
+  _DELETERUNSRESPONSE._serialized_end=1817
+  _RUNSERVICE._serialized_start=1820
+  _RUNSERVICE._serialized_end=2596
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2.pyi`

 * *Files 10% similar despite different names*

```diff
@@ -4,225 +4,196 @@
 """
 import builtins
 import ...common.v1.types_pb2
 import google.protobuf.descriptor
 import google.protobuf.field_mask_pb2
 import google.protobuf.internal.containers
 import google.protobuf.message
-import google.protobuf.timestamp_pb2
+import ...tag.v1.tag_pb2
 import typing
 import typing_extensions
 
 DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
 
-class Token(google.protobuf.message.Message):
+class CreateTagRequest(google.protobuf.message.Message):
+    """Request message for [TagService.CreateTag][v1.TagService.CreateTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
-    class Payload(google.protobuf.message.Message):
-        DESCRIPTOR: google.protobuf.descriptor.Descriptor
-        UUID_FIELD_NUMBER: builtins.int
-        USER_ID_FIELD_NUMBER: builtins.int
-        ISSUED_AT_FIELD_NUMBER: builtins.int
-        EXPIRED_AT_FIELD_NUMBER: builtins.int
-        DURATION_FIELD_NUMBER: builtins.int
-        TIME_UNIT_FIELD_NUMBER: builtins.int
-        NAME_FIELD_NUMBER: builtins.int
-        TOKEN_FIELD_NUMBER: builtins.int
-        uuid: typing.Text
-        """Save in database only, generated when create token."""
-
-        user_id: builtins.int
-        """Save in database only, obtained by interceptor."""
-
-        @property
-        def issued_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
-            """Output only."""
-            pass
-        @property
-        def expired_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
-            """Output only."""
-            pass
-        duration: builtins.int
-        """Input only."""
-
-        time_unit: common.v1.types_pb2.TimeUnit.ValueType
-        """Input only."""
-
-        name: typing.Text
-        token: typing.Text
-        """Output when create only."""
-
-        def __init__(self,
-            *,
-            uuid: typing.Text = ...,
-            user_id: builtins.int = ...,
-            issued_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
-            expired_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
-            duration: builtins.int = ...,
-            time_unit: common.v1.types_pb2.TimeUnit.ValueType = ...,
-            name: typing.Text = ...,
-            token: typing.Text = ...,
-            ) -> None: ...
-        def HasField(self, field_name: typing_extensions.Literal["expired_at",b"expired_at","issued_at",b"issued_at"]) -> builtins.bool: ...
-        def ClearField(self, field_name: typing_extensions.Literal["duration",b"duration","expired_at",b"expired_at","issued_at",b"issued_at","name",b"name","time_unit",b"time_unit","token",b"token","user_id",b"user_id","uuid",b"uuid"]) -> None: ...
-
-    ID_FIELD_NUMBER: builtins.int
-    CREATE_AT_FIELD_NUMBER: builtins.int
-    UPDATE_AT_FIELD_NUMBER: builtins.int
-    PAYLOAD_FIELD_NUMBER: builtins.int
-    id: builtins.int
-    """auto increase id."""
-
-    create_at: typing.Text
-    """Output only. Timestamp when this Dataset was created, convert to local
-    timezone string.
-    """
-
-    update_at: typing.Text
-    """Output only. Timestamp when this Dataset was last updated, convert to local
-    timezone string.
+    PARENT_FIELD_NUMBER: builtins.int
+    TAG_FIELD_NUMBER: builtins.int
+    parent: typing.Text
+    """The path of the Tag's parent resource, if exists.
+    Format: ``
     """
 
     @property
-    def payload(self) -> global___Token.Payload: ...
+    def tag(self) -> tag.v1.tag_pb2.Tag:
+        """Required. The Tag to create."""
+        pass
     def __init__(self,
         *,
-        id: builtins.int = ...,
-        create_at: typing.Text = ...,
-        update_at: typing.Text = ...,
-        payload: typing.Optional[global___Token.Payload] = ...,
+        parent: typing.Text = ...,
+        tag: typing.Optional[tag.v1.tag_pb2.Tag] = ...,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions.Literal["payload",b"payload"]) -> builtins.bool: ...
-    def ClearField(self, field_name: typing_extensions.Literal["create_at",b"create_at","id",b"id","payload",b"payload","update_at",b"update_at"]) -> None: ...
-global___Token = Token
+    def HasField(self, field_name: typing_extensions.Literal["tag",b"tag"]) -> builtins.bool: ...
+    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","tag",b"tag"]) -> None: ...
+global___CreateTagRequest = CreateTagRequest
 
-class TokenOptionFilter(google.protobuf.message.Message):
+class CreateTagResponse(google.protobuf.message.Message):
+    """Response message for [TagService.CreateTag][v1.TagService.CreateTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
-    USER_ID_FIELD_NUMBER: builtins.int
-    user_id: builtins.int
+    CODE_FIELD_NUMBER: builtins.int
+    MESSAGE_FIELD_NUMBER: builtins.int
+    DETAILS_FIELD_NUMBER: builtins.int
+    code: builtins.int
+    """status code."""
+
+    message: typing.Text
+    """error message."""
+
+    @property
+    def details(self) -> tag.v1.tag_pb2.Tag:
+        """response data."""
+        pass
     def __init__(self,
         *,
-        user_id: builtins.int = ...,
+        code: builtins.int = ...,
+        message: typing.Text = ...,
+        details: typing.Optional[tag.v1.tag_pb2.Tag] = ...,
         ) -> None: ...
-    def ClearField(self, field_name: typing_extensions.Literal["user_id",b"user_id"]) -> None: ...
-global___TokenOptionFilter = TokenOptionFilter
+    def HasField(self, field_name: typing_extensions.Literal["details",b"details"]) -> builtins.bool: ...
+    def ClearField(self, field_name: typing_extensions.Literal["code",b"code","details",b"details","message",b"message"]) -> None: ...
+global___CreateTagResponse = CreateTagResponse
 
-class CreateTokenRequest(google.protobuf.message.Message):
-    """Request message for [TokenService.CreateToken][v1.TokenService.CreateToken]."""
+class GetTagRequest(google.protobuf.message.Message):
+    """Request message for [TagService.GetTag][v1.TagService.GetTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARENT_FIELD_NUMBER: builtins.int
-    TOKEN_FIELD_NUMBER: builtins.int
+    ID_FIELD_NUMBER: builtins.int
+    READ_MASK_FIELD_NUMBER: builtins.int
     parent: typing.Text
-    """The path of the Token's parent resource, if exists.
-    Format: `auth`
+    """The path of the Tag's parent resource, if exists.
+    Format: ``
     """
 
+    id: builtins.int
+    """Required. The id of the Tag in database."""
+
     @property
-    def token(self) -> global___Token:
-        """Required. The Token to create."""
+    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
+        """Mask specifying which fields to read."""
         pass
     def __init__(self,
         *,
         parent: typing.Text = ...,
-        token: typing.Optional[global___Token] = ...,
+        id: builtins.int = ...,
+        read_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions.Literal["token",b"token"]) -> builtins.bool: ...
-    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","token",b"token"]) -> None: ...
-global___CreateTokenRequest = CreateTokenRequest
+    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
+    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
+global___GetTagRequest = GetTagRequest
 
-class CreateTokenResponse(google.protobuf.message.Message):
-    """Response message for [TokenService.CreateToken][v1.TokenService.CreateToken]."""
+class GetTagResponse(google.protobuf.message.Message):
+    """Response message for [TagService.GetTag][v1.TagService.GetTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     CODE_FIELD_NUMBER: builtins.int
     MESSAGE_FIELD_NUMBER: builtins.int
     DETAILS_FIELD_NUMBER: builtins.int
     code: builtins.int
     """status code."""
 
     message: typing.Text
     """error message."""
 
     @property
-    def details(self) -> global___Token:
+    def details(self) -> tag.v1.tag_pb2.Tag:
         """response data."""
         pass
     def __init__(self,
         *,
         code: builtins.int = ...,
         message: typing.Text = ...,
-        details: typing.Optional[global___Token] = ...,
+        details: typing.Optional[tag.v1.tag_pb2.Tag] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["details",b"details"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["code",b"code","details",b"details","message",b"message"]) -> None: ...
-global___CreateTokenResponse = CreateTokenResponse
+global___GetTagResponse = GetTagResponse
 
-class GetTokenRequest(google.protobuf.message.Message):
-    """Request message for [TokenService.GetToken][v1.TokenService.GetToken]."""
+class UpdateTagRequest(google.protobuf.message.Message):
+    """Request message for [TagService.UpdateTag][v1.TagService.UpdateTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARENT_FIELD_NUMBER: builtins.int
-    ID_FIELD_NUMBER: builtins.int
-    READ_MASK_FIELD_NUMBER: builtins.int
+    TAG_FIELD_NUMBER: builtins.int
+    UPDATE_MASK_FIELD_NUMBER: builtins.int
     parent: typing.Text
-    """The path of the Token's parent resource, if exists.
-    Format: `auth`
+    """The path of the Tag's parent resource, if exists.
+    Format: ``
     """
 
-    id: builtins.int
-    """Required. The id of the Token in database."""
-
     @property
-    def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
-        """Mask specifying which fields to read."""
+    def tag(self) -> tag.v1.tag_pb2.Tag:
+        """Required. The Tag which replaces the resource on the server."""
+        pass
+    @property
+    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
+        """Required. The update mask applies to the resource.
+        For the `FieldMask` definition, see [google.protobuf.FieldMask][google.protobuf.FieldMask].
+        Updatable fields:
+
+          * `id`
+          * `update_at`
+          * `create_at`
+        """
         pass
     def __init__(self,
         *,
         parent: typing.Text = ...,
-        id: builtins.int = ...,
-        read_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
+        tag: typing.Optional[tag.v1.tag_pb2.Tag] = ...,
+        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions.Literal["read_mask",b"read_mask"]) -> builtins.bool: ...
-    def ClearField(self, field_name: typing_extensions.Literal["id",b"id","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
-global___GetTokenRequest = GetTokenRequest
+    def HasField(self, field_name: typing_extensions.Literal["tag",b"tag","update_mask",b"update_mask"]) -> builtins.bool: ...
+    def ClearField(self, field_name: typing_extensions.Literal["parent",b"parent","tag",b"tag","update_mask",b"update_mask"]) -> None: ...
+global___UpdateTagRequest = UpdateTagRequest
 
-class GetTokenResponse(google.protobuf.message.Message):
-    """Response message for [TokenService.GetToken][v1.TokenService.GetToken]."""
+class UpdateTagResponse(google.protobuf.message.Message):
+    """Response message for [TagService.UpdateTag][v1.TagService.UpdateTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     CODE_FIELD_NUMBER: builtins.int
     MESSAGE_FIELD_NUMBER: builtins.int
     DETAILS_FIELD_NUMBER: builtins.int
     code: builtins.int
     """status code."""
 
     message: typing.Text
     """error message."""
 
     @property
-    def details(self) -> global___Token:
+    def details(self) -> tag.v1.tag_pb2.Tag:
         """response data."""
         pass
     def __init__(self,
         *,
         code: builtins.int = ...,
         message: typing.Text = ...,
-        details: typing.Optional[global___Token] = ...,
+        details: typing.Optional[tag.v1.tag_pb2.Tag] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["details",b"details"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["code",b"code","details",b"details","message",b"message"]) -> None: ...
-global___GetTokenResponse = GetTokenResponse
+global___UpdateTagResponse = UpdateTagResponse
 
-class ListTokensRequest(google.protobuf.message.Message):
-    """Request message for [TokenService.ListTokens][v1.TokenService.ListTokens]."""
+class ListTagsRequest(google.protobuf.message.Message):
+    """Request message for [TagService.ListTags][v1.TagService.ListTags]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARENT_FIELD_NUMBER: builtins.int
     COMMON_OPTION_FIELD_NUMBER: builtins.int
     COMMON_FILTER_FIELD_NUMBER: builtins.int
     READ_MASK_FIELD_NUMBER: builtins.int
     OPTION_FILTER_FIELD_NUMBER: builtins.int
     parent: typing.Text
-    """The path of the Token's parent resource, if exists.
-    Format: `auth`
+    """The path of the Tag's parent resource, if exists.
+    Format: ``
     """
 
     @property
     def common_option(self) -> common.v1.types_pb2.CommonOption:
         """common list option."""
         pass
     @property
@@ -230,52 +201,52 @@
         """common list filter."""
         pass
     @property
     def read_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
         """Mask specifying which fields to read."""
         pass
     @property
-    def option_filter(self) -> global___TokenOptionFilter:
-        """option filter struct for list Token."""
+    def option_filter(self) -> tag.v1.tag_pb2.TagOptionFilter:
+        """option filter struct for list Tag."""
         pass
     def __init__(self,
         *,
         parent: typing.Text = ...,
         common_option: typing.Optional[common.v1.types_pb2.CommonOption] = ...,
         common_filter: typing.Optional[common.v1.types_pb2.CommonFilter] = ...,
         read_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
-        option_filter: typing.Optional[global___TokenOptionFilter] = ...,
+        option_filter: typing.Optional[tag.v1.tag_pb2.TagOptionFilter] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["common_filter",b"common_filter","common_option",b"common_option","option_filter",b"option_filter","read_mask",b"read_mask"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["common_filter",b"common_filter","common_option",b"common_option","option_filter",b"option_filter","parent",b"parent","read_mask",b"read_mask"]) -> None: ...
-global___ListTokensRequest = ListTokensRequest
+global___ListTagsRequest = ListTagsRequest
 
-class ListTokensResponse(google.protobuf.message.Message):
-    """Response message for [TokenService.ListTokens][v1.TokenService.ListTokens]."""
+class ListTagsResponse(google.protobuf.message.Message):
+    """Response message for [TagService.ListTags][v1.TagService.ListTags]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     class Details(google.protobuf.message.Message):
         DESCRIPTOR: google.protobuf.descriptor.Descriptor
         ITEMS_FIELD_NUMBER: builtins.int
         NEXT_REQUEST_FIELD_NUMBER: builtins.int
         TOTAL_COUNT_FIELD_NUMBER: builtins.int
         @property
-        def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Token]:
-            """A list of Tokens that matches the specified filter in the request."""
+        def items(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tag.v1.tag_pb2.Tag]:
+            """A list of Tags that matches the specified filter in the request."""
             pass
         @property
-        def next_request(self) -> global___ListTokensRequest:
+        def next_request(self) -> global___ListTagsRequest:
             """next request."""
             pass
         total_count: builtins.int
         """total items count of this filter."""
 
         def __init__(self,
             *,
-            items: typing.Optional[typing.Iterable[global___Token]] = ...,
-            next_request: typing.Optional[global___ListTokensRequest] = ...,
+            items: typing.Optional[typing.Iterable[tag.v1.tag_pb2.Tag]] = ...,
+            next_request: typing.Optional[global___ListTagsRequest] = ...,
             total_count: builtins.int = ...,
             ) -> None: ...
         def HasField(self, field_name: typing_extensions.Literal["next_request",b"next_request"]) -> builtins.bool: ...
         def ClearField(self, field_name: typing_extensions.Literal["items",b"items","next_request",b"next_request","total_count",b"total_count"]) -> None: ...
 
     CODE_FIELD_NUMBER: builtins.int
     MESSAGE_FIELD_NUMBER: builtins.int
@@ -283,106 +254,106 @@
     code: builtins.int
     """status code."""
 
     message: typing.Text
     """error message."""
 
     @property
-    def details(self) -> global___ListTokensResponse.Details: ...
+    def details(self) -> global___ListTagsResponse.Details: ...
     def __init__(self,
         *,
         code: builtins.int = ...,
         message: typing.Text = ...,
-        details: typing.Optional[global___ListTokensResponse.Details] = ...,
+        details: typing.Optional[global___ListTagsResponse.Details] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["details",b"details"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["code",b"code","details",b"details","message",b"message"]) -> None: ...
-global___ListTokensResponse = ListTokensResponse
+global___ListTagsResponse = ListTagsResponse
 
-class DeleteTokenRequest(google.protobuf.message.Message):
-    """Request message for [TokenService.DeleteToken][v1.TokenService.DeleteToken]."""
+class DeleteTagRequest(google.protobuf.message.Message):
+    """Request message for [TagService.DeleteTag][v1.TagService.DeleteTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARENT_FIELD_NUMBER: builtins.int
     ID_FIELD_NUMBER: builtins.int
     parent: typing.Text
-    """The path of the Token's parent resource, if exists.
-    Format: `auth`
+    """The path of the Tag's parent resource, if exists.
+    Format: ``
     """
 
     id: builtins.int
-    """Required. The resource name of the Token to delete.
+    """Required. The resource name of the Tag to delete.
     Format:
-    `auth/tokens/{id}`
+    `tags/{id}`
     """
 
     def __init__(self,
         *,
         parent: typing.Text = ...,
         id: builtins.int = ...,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions.Literal["id",b"id","parent",b"parent"]) -> None: ...
-global___DeleteTokenRequest = DeleteTokenRequest
+global___DeleteTagRequest = DeleteTagRequest
 
-class DeleteTokenResponse(google.protobuf.message.Message):
-    """Response message for [TokenService.DeleteToken][v1.TokenService.DeleteToken]."""
+class DeleteTagResponse(google.protobuf.message.Message):
+    """Response message for [TagService.DeleteTag][v1.TagService.DeleteTag]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     CODE_FIELD_NUMBER: builtins.int
     MESSAGE_FIELD_NUMBER: builtins.int
     DETAILS_FIELD_NUMBER: builtins.int
     code: builtins.int
     """status code."""
 
     message: typing.Text
     """error message."""
 
     @property
-    def details(self) -> global___Token:
+    def details(self) -> tag.v1.tag_pb2.Tag:
         """response data."""
         pass
     def __init__(self,
         *,
         code: builtins.int = ...,
         message: typing.Text = ...,
-        details: typing.Optional[global___Token] = ...,
+        details: typing.Optional[tag.v1.tag_pb2.Tag] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["details",b"details"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["code",b"code","details",b"details","message",b"message"]) -> None: ...
-global___DeleteTokenResponse = DeleteTokenResponse
+global___DeleteTagResponse = DeleteTagResponse
 
-class DeleteTokensRequest(google.protobuf.message.Message):
-    """Request message for [TokenService.DeleteTokens][v1.TokenService.DeleteTokens]."""
+class DeleteTagsRequest(google.protobuf.message.Message):
+    """Request message for [TagService.DeleteTags][v1.TagService.DeleteTags]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARENT_FIELD_NUMBER: builtins.int
     COMMON_FILTER_FIELD_NUMBER: builtins.int
     OPTION_FILTER_FIELD_NUMBER: builtins.int
     parent: typing.Text
-    """The path of the Token's parent resource, if exists.
-    Format: `auth`
+    """The path of the Tag's parent resource, if exists.
+    Format: ``
     """
 
     @property
     def common_filter(self) -> common.v1.types_pb2.CommonFilter:
-        """use common filter to delete Token"""
+        """use common filter to delete Tag"""
         pass
     @property
-    def option_filter(self) -> global___TokenOptionFilter:
-        """option filter struct for delete Token items."""
+    def option_filter(self) -> tag.v1.tag_pb2.TagOptionFilter:
+        """option filter struct for delete Tag items."""
         pass
     def __init__(self,
         *,
         parent: typing.Text = ...,
         common_filter: typing.Optional[common.v1.types_pb2.CommonFilter] = ...,
-        option_filter: typing.Optional[global___TokenOptionFilter] = ...,
+        option_filter: typing.Optional[tag.v1.tag_pb2.TagOptionFilter] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["common_filter",b"common_filter","option_filter",b"option_filter"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["common_filter",b"common_filter","option_filter",b"option_filter","parent",b"parent"]) -> None: ...
-global___DeleteTokensRequest = DeleteTokensRequest
+global___DeleteTagsRequest = DeleteTagsRequest
 
-class DeleteTokensResponse(google.protobuf.message.Message):
-    """Response message for [TokenService.DeleteTokens][v1.TokenService.DeleteTokens]."""
+class DeleteTagsResponse(google.protobuf.message.Message):
+    """Response message for [TagService.DeleteTags][v1.TagService.DeleteTags]."""
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     CODE_FIELD_NUMBER: builtins.int
     MESSAGE_FIELD_NUMBER: builtins.int
     DETAILS_FIELD_NUMBER: builtins.int
     code: builtins.int
     """status code."""
 
@@ -396,8 +367,8 @@
     def __init__(self,
         *,
         code: builtins.int = ...,
         message: typing.Text = ...,
         details: typing.Optional[typing.Iterable[builtins.int]] = ...,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions.Literal["code",b"code","details",b"details","message",b"message"]) -> None: ...
-global___DeleteTokensResponse = DeleteTokensResponse
+global___DeleteTagsResponse = DeleteTagsResponse
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/auth/v1/token_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,269 +1,240 @@
 # Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
 """Client and server classes corresponding to protobuf-defined services."""
 import grpc
 
-from ...auth.v1 import token_service_pb2 as auth_dot_v1_dot_token__service__pb2
+from ...muses.v1 import flow_service_pb2 as muses_dot_v1_dot_flow__service__pb2
 
 
-class TokenServiceStub(object):
-    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
-    info: {
-    title: "Token Service"
-    version: "1.0"
-    contact: {
-    name: "Token Service"
-    url: "http://github.com/artistml/apis"
-    }
-    }
-    host: "github.com/artistml/apis"
-    base_path: "/auth/v1/token"
-    schemes: HTTP
-    schemes: HTTPS
-    consumes: "application/json"
-    produces: "application/json"
-    external_docs: {
-    description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/auth/v1/token"
-    }
-    };
-
-    The service that handles the CRUD of Token.
+class FlowServiceStub(object):
+    """The service that handles the CRUD of Flow.
     """
 
     def __init__(self, channel):
         """Constructor.
 
         Args:
             channel: A grpc.Channel.
         """
-        self.CreateToken = channel.unary_unary(
-                '/auth.v1.TokenService/CreateToken',
-                request_serializer=auth_dot_v1_dot_token__service__pb2.CreateTokenRequest.SerializeToString,
-                response_deserializer=auth_dot_v1_dot_token__service__pb2.CreateTokenResponse.FromString,
+        self.CreateFlow = channel.unary_unary(
+                '/muses.v1.FlowService/CreateFlow',
+                request_serializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowResponse.FromString,
                 )
-        self.GetToken = channel.unary_unary(
-                '/auth.v1.TokenService/GetToken',
-                request_serializer=auth_dot_v1_dot_token__service__pb2.GetTokenRequest.SerializeToString,
-                response_deserializer=auth_dot_v1_dot_token__service__pb2.GetTokenResponse.FromString,
+        self.GetFlow = channel.unary_unary(
+                '/muses.v1.FlowService/GetFlow',
+                request_serializer=muses_dot_v1_dot_flow__service__pb2.GetFlowRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_flow__service__pb2.GetFlowResponse.FromString,
                 )
-        self.ListTokens = channel.unary_unary(
-                '/auth.v1.TokenService/ListTokens',
-                request_serializer=auth_dot_v1_dot_token__service__pb2.ListTokensRequest.SerializeToString,
-                response_deserializer=auth_dot_v1_dot_token__service__pb2.ListTokensResponse.FromString,
+        self.UpdateFlow = channel.unary_unary(
+                '/muses.v1.FlowService/UpdateFlow',
+                request_serializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowResponse.FromString,
                 )
-        self.DeleteToken = channel.unary_unary(
-                '/auth.v1.TokenService/DeleteToken',
-                request_serializer=auth_dot_v1_dot_token__service__pb2.DeleteTokenRequest.SerializeToString,
-                response_deserializer=auth_dot_v1_dot_token__service__pb2.DeleteTokenResponse.FromString,
+        self.ListFlows = channel.unary_unary(
+                '/muses.v1.FlowService/ListFlows',
+                request_serializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsResponse.FromString,
                 )
-        self.DeleteTokens = channel.unary_unary(
-                '/auth.v1.TokenService/DeleteTokens',
-                request_serializer=auth_dot_v1_dot_token__service__pb2.DeleteTokensRequest.SerializeToString,
-                response_deserializer=auth_dot_v1_dot_token__service__pb2.DeleteTokensResponse.FromString,
+        self.DeleteFlow = channel.unary_unary(
+                '/muses.v1.FlowService/DeleteFlow',
+                request_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowResponse.FromString,
+                )
+        self.DeleteFlows = channel.unary_unary(
+                '/muses.v1.FlowService/DeleteFlows',
+                request_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsResponse.FromString,
                 )
 
 
-class TokenServiceServicer(object):
-    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
-    info: {
-    title: "Token Service"
-    version: "1.0"
-    contact: {
-    name: "Token Service"
-    url: "http://github.com/artistml/apis"
-    }
-    }
-    host: "github.com/artistml/apis"
-    base_path: "/auth/v1/token"
-    schemes: HTTP
-    schemes: HTTPS
-    consumes: "application/json"
-    produces: "application/json"
-    external_docs: {
-    description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/auth/v1/token"
-    }
-    };
-
-    The service that handles the CRUD of Token.
+class FlowServiceServicer(object):
+    """The service that handles the CRUD of Flow.
     """
 
-    def CreateToken(self, request, context):
-        """Creates a Token.
+    def CreateFlow(self, request, context):
+        """Creates a Flow.
+        """
+        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
+        context.set_details('Method not implemented!')
+        raise NotImplementedError('Method not implemented!')
+
+    def GetFlow(self, request, context):
+        """Gets a Flow.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def GetToken(self, request, context):
-        """Gets a Token.
+    def UpdateFlow(self, request, context):
+        """Updates a Flow.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def ListTokens(self, request, context):
-        """Lists Tokens in a Location.
+    def ListFlows(self, request, context):
+        """Lists Flows in a Location.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteToken(self, request, context):
-        """Deletes a Token.
+    def DeleteFlow(self, request, context):
+        """Deletes a Flow.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteTokens(self, request, context):
-        """Batch delete Token by filter.
+    def DeleteFlows(self, request, context):
+        """Batch delete Flow by filter.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
 
-def add_TokenServiceServicer_to_server(servicer, server):
+def add_FlowServiceServicer_to_server(servicer, server):
     rpc_method_handlers = {
-            'CreateToken': grpc.unary_unary_rpc_method_handler(
-                    servicer.CreateToken,
-                    request_deserializer=auth_dot_v1_dot_token__service__pb2.CreateTokenRequest.FromString,
-                    response_serializer=auth_dot_v1_dot_token__service__pb2.CreateTokenResponse.SerializeToString,
+            'CreateFlow': grpc.unary_unary_rpc_method_handler(
+                    servicer.CreateFlow,
+                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowResponse.SerializeToString,
             ),
-            'GetToken': grpc.unary_unary_rpc_method_handler(
-                    servicer.GetToken,
-                    request_deserializer=auth_dot_v1_dot_token__service__pb2.GetTokenRequest.FromString,
-                    response_serializer=auth_dot_v1_dot_token__service__pb2.GetTokenResponse.SerializeToString,
+            'GetFlow': grpc.unary_unary_rpc_method_handler(
+                    servicer.GetFlow,
+                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.GetFlowRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_flow__service__pb2.GetFlowResponse.SerializeToString,
             ),
-            'ListTokens': grpc.unary_unary_rpc_method_handler(
-                    servicer.ListTokens,
-                    request_deserializer=auth_dot_v1_dot_token__service__pb2.ListTokensRequest.FromString,
-                    response_serializer=auth_dot_v1_dot_token__service__pb2.ListTokensResponse.SerializeToString,
+            'UpdateFlow': grpc.unary_unary_rpc_method_handler(
+                    servicer.UpdateFlow,
+                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowResponse.SerializeToString,
             ),
-            'DeleteToken': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteToken,
-                    request_deserializer=auth_dot_v1_dot_token__service__pb2.DeleteTokenRequest.FromString,
-                    response_serializer=auth_dot_v1_dot_token__service__pb2.DeleteTokenResponse.SerializeToString,
+            'ListFlows': grpc.unary_unary_rpc_method_handler(
+                    servicer.ListFlows,
+                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsResponse.SerializeToString,
             ),
-            'DeleteTokens': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteTokens,
-                    request_deserializer=auth_dot_v1_dot_token__service__pb2.DeleteTokensRequest.FromString,
-                    response_serializer=auth_dot_v1_dot_token__service__pb2.DeleteTokensResponse.SerializeToString,
+            'DeleteFlow': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteFlow,
+                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowResponse.SerializeToString,
+            ),
+            'DeleteFlows': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteFlows,
+                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsResponse.SerializeToString,
             ),
     }
     generic_handler = grpc.method_handlers_generic_handler(
-            'auth.v1.TokenService', rpc_method_handlers)
+            'muses.v1.FlowService', rpc_method_handlers)
     server.add_generic_rpc_handlers((generic_handler,))
 
 
  # This class is part of an EXPERIMENTAL API.
-class TokenService(object):
-    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
-    info: {
-    title: "Token Service"
-    version: "1.0"
-    contact: {
-    name: "Token Service"
-    url: "http://github.com/artistml/apis"
-    }
-    }
-    host: "github.com/artistml/apis"
-    base_path: "/auth/v1/token"
-    schemes: HTTP
-    schemes: HTTPS
-    consumes: "application/json"
-    produces: "application/json"
-    external_docs: {
-    description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/auth/v1/token"
-    }
-    };
-
-    The service that handles the CRUD of Token.
+class FlowService(object):
+    """The service that handles the CRUD of Flow.
     """
 
     @staticmethod
-    def CreateToken(request,
+    def CreateFlow(request,
+            target,
+            options=(),
+            channel_credentials=None,
+            call_credentials=None,
+            insecure=False,
+            compression=None,
+            wait_for_ready=None,
+            timeout=None,
+            metadata=None):
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/CreateFlow',
+            muses_dot_v1_dot_flow__service__pb2.CreateFlowRequest.SerializeToString,
+            muses_dot_v1_dot_flow__service__pb2.CreateFlowResponse.FromString,
+            options, channel_credentials,
+            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
+
+    @staticmethod
+    def GetFlow(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/auth.v1.TokenService/CreateToken',
-            auth_dot_v1_dot_token__service__pb2.CreateTokenRequest.SerializeToString,
-            auth_dot_v1_dot_token__service__pb2.CreateTokenResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/GetFlow',
+            muses_dot_v1_dot_flow__service__pb2.GetFlowRequest.SerializeToString,
+            muses_dot_v1_dot_flow__service__pb2.GetFlowResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def GetToken(request,
+    def UpdateFlow(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/auth.v1.TokenService/GetToken',
-            auth_dot_v1_dot_token__service__pb2.GetTokenRequest.SerializeToString,
-            auth_dot_v1_dot_token__service__pb2.GetTokenResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/UpdateFlow',
+            muses_dot_v1_dot_flow__service__pb2.UpdateFlowRequest.SerializeToString,
+            muses_dot_v1_dot_flow__service__pb2.UpdateFlowResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def ListTokens(request,
+    def ListFlows(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/auth.v1.TokenService/ListTokens',
-            auth_dot_v1_dot_token__service__pb2.ListTokensRequest.SerializeToString,
-            auth_dot_v1_dot_token__service__pb2.ListTokensResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/ListFlows',
+            muses_dot_v1_dot_flow__service__pb2.ListFlowsRequest.SerializeToString,
+            muses_dot_v1_dot_flow__service__pb2.ListFlowsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteToken(request,
+    def DeleteFlow(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/auth.v1.TokenService/DeleteToken',
-            auth_dot_v1_dot_token__service__pb2.DeleteTokenRequest.SerializeToString,
-            auth_dot_v1_dot_token__service__pb2.DeleteTokenResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/DeleteFlow',
+            muses_dot_v1_dot_flow__service__pb2.DeleteFlowRequest.SerializeToString,
+            muses_dot_v1_dot_flow__service__pb2.DeleteFlowResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteTokens(request,
+    def DeleteFlows(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/auth.v1.TokenService/DeleteTokens',
-            auth_dot_v1_dot_token__service__pb2.DeleteTokensRequest.SerializeToString,
-            auth_dot_v1_dot_token__service__pb2.DeleteTokensResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/DeleteFlows',
+            muses_dot_v1_dot_flow__service__pb2.DeleteFlowsRequest.SerializeToString,
+            muses_dot_v1_dot_flow__service__pb2.DeleteFlowsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/common/v1/types_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/common/v1/types_pb2.py`

 * *Files 10% similar despite different names*

```diff
@@ -10,26 +10,24 @@
 
 _sym_db = _symbol_database.Default()
 
 
 from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ommon/v1/types.proto\x12\tcommon.v1\x1a\x19google/protobuf/any.proto\"h\n\x08Response\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12.\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyR\x07\x64\x65tails\"\x9a\x01\n\x0c\x43ommonOption\x12\x12\n\x04page\x18\x01 \x01(\x05R\x04page\x12\x12\n\x04size\x18\x02 \x01(\x05R\x04size\x12\x16\n\x06\x63ursor\x18\x03 \x01(\tR\x06\x63ursor\x12\x14\n\x05query\x18\x04 \x01(\tR\x05query\x12\x19\n\x08order_by\x18\x05 \x01(\tR\x07orderBy\x12\x19\n\x08group_by\x18\x06 \x01(\tR\x07groupBy\"\xa9\x01\n\x0c\x43ommonFilter\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x1b\n\thigh_time\x18\x02 \x01(\tR\x08highTime\x12\x19\n\x08low_time\x18\x03 \x01(\tR\x07lowTime\x12\x1f\n\x0b\x65xclude_ids\x18\x04 \x03(\x03R\nexcludeIds\x12\x1f\n\x0binclude_ids\x18\x05 \x03(\x03R\nincludeIds*\xd7\x01\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x17\n\x12\x43ODE_GENERAL_ERROR\x10\xe8\x07\x12\x1a\n\x15\x43ODE_INVALID_ARGUMENT\x10\xeb\x07\x12\x13\n\x0e\x43ODE_NOT_FOUND\x10\xed\x07\x12\x18\n\x13\x43ODE_ALREADY_EXISTS\x10\xee\x07\x12\x1b\n\x16\x43ODE_GENERAL_SQL_ERROR\x10\xd0\x0f\x12\x15\n\x10\x43ODE_SQL_NO_ROWS\x10\xd1\x0f\x12!\n\x1c\x43ODE_K8S_NOT_ENOUGH_RESOURCE\x10\xb8\x17*\xb5\x01\n\x08TimeUnit\x12\x19\n\x15TIME_UNIT_UNSPECIFIED\x10\x00\x12\x14\n\x10TIME_UNIT_SECOND\x10\x01\x12\x14\n\x10TIME_UNIT_MINUTE\x10\x02\x12\x12\n\x0eTIME_UNIT_HOUR\x10\x03\x12\x11\n\rTIME_UNIT_DAY\x10\x04\x12\x12\n\x0eTIME_UNIT_WEEK\x10\x05\x12\x13\n\x0fTIME_UNIT_MONTH\x10\x06\x12\x12\n\x0eTIME_UNIT_YEAR\x10\x07\x42\x30Z.github.com/artistml/apis/go/common/v1;commonv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x63ommon/v1/types.proto\x12\tcommon.v1\x1a\x19google/protobuf/any.proto\"h\n\x08Response\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12.\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyR\x07\x64\x65tails\"\x9a\x01\n\x0c\x43ommonOption\x12\x12\n\x04page\x18\x01 \x01(\x05R\x04page\x12\x12\n\x04size\x18\x02 \x01(\x05R\x04size\x12\x16\n\x06\x63ursor\x18\x03 \x01(\tR\x06\x63ursor\x12\x14\n\x05query\x18\x04 \x01(\tR\x05query\x12\x19\n\x08order_by\x18\x05 \x01(\tR\x07orderBy\x12\x19\n\x08group_by\x18\x06 \x01(\tR\x07groupBy\"\xa9\x01\n\x0c\x43ommonFilter\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x1b\n\thigh_time\x18\x02 \x01(\tR\x08highTime\x12\x19\n\x08low_time\x18\x03 \x01(\tR\x07lowTime\x12\x1f\n\x0b\x65xclude_ids\x18\x04 \x03(\x03R\nexcludeIds\x12\x1f\n\x0binclude_ids\x18\x05 \x03(\x03R\nincludeIds*\xd7\x01\n\x04\x43ode\x12\x14\n\x10\x43ODE_UNSPECIFIED\x10\x00\x12\x17\n\x12\x43ODE_GENERAL_ERROR\x10\xe8\x07\x12\x1a\n\x15\x43ODE_INVALID_ARGUMENT\x10\xeb\x07\x12\x13\n\x0e\x43ODE_NOT_FOUND\x10\xed\x07\x12\x18\n\x13\x43ODE_ALREADY_EXISTS\x10\xee\x07\x12\x1b\n\x16\x43ODE_GENERAL_SQL_ERROR\x10\xd0\x0f\x12\x15\n\x10\x43ODE_SQL_NO_ROWS\x10\xd1\x0f\x12!\n\x1c\x43ODE_K8S_NOT_ENOUGH_RESOURCE\x10\xb8\x17\x42\x30Z.github.com/artistml/apis/go/common/v1;commonv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.v1.types_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   DESCRIPTOR._serialized_options = b'Z.github.com/artistml/apis/go/common/v1;commonv1'
   _CODE._serialized_start=499
   _CODE._serialized_end=714
-  _TIMEUNIT._serialized_start=717
-  _TIMEUNIT._serialized_end=898
   _RESPONSE._serialized_start=63
   _RESPONSE._serialized_end=167
   _COMMONOPTION._serialized_start=170
   _COMMONOPTION._serialized_end=324
   _COMMONFILTER._serialized_start=327
   _COMMONFILTER._serialized_end=496
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/enums_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/enums_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/echo/v1/greeting_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/hacker/v1/hacker_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/auth_pb2_grpc.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,70 +1,67 @@
 # Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
 """Client and server classes corresponding to protobuf-defined services."""
 import grpc
 
-from ...hacker.v1 import hacker_service_pb2 as hacker_dot_v1_dot_hacker__service__pb2
+from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
+from ...thirdparty.kfpbackend import auth_pb2 as thirdparty_dot_kfpbackend_dot_auth__pb2
 
 
-class HackerServiceStub(object):
-    """The service that handles the CRUD of Hacker.
-    """
+class AuthServiceStub(object):
+    """Missing associated documentation comment in .proto file."""
 
     def __init__(self, channel):
         """Constructor.
 
         Args:
             channel: A grpc.Channel.
         """
-        self.CreateHacker = channel.unary_unary(
-                '/hacker.v1.HackerService/CreateHacker',
-                request_serializer=hacker_dot_v1_dot_hacker__service__pb2.CreateHackerRequest.SerializeToString,
-                response_deserializer=hacker_dot_v1_dot_hacker__service__pb2.CreateHackerResponse.FromString,
+        self.Authorize = channel.unary_unary(
+                '/thirdparty.kfpbackend.AuthService/Authorize',
+                request_serializer=thirdparty_dot_kfpbackend_dot_auth__pb2.AuthorizeRequest.SerializeToString,
+                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                 )
 
 
-class HackerServiceServicer(object):
-    """The service that handles the CRUD of Hacker.
-    """
+class AuthServiceServicer(object):
+    """Missing associated documentation comment in .proto file."""
 
-    def CreateHacker(self, request, context):
-        """Creates a Hacker.
-        """
+    def Authorize(self, request, context):
+        """Missing associated documentation comment in .proto file."""
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
 
-def add_HackerServiceServicer_to_server(servicer, server):
+def add_AuthServiceServicer_to_server(servicer, server):
     rpc_method_handlers = {
-            'CreateHacker': grpc.unary_unary_rpc_method_handler(
-                    servicer.CreateHacker,
-                    request_deserializer=hacker_dot_v1_dot_hacker__service__pb2.CreateHackerRequest.FromString,
-                    response_serializer=hacker_dot_v1_dot_hacker__service__pb2.CreateHackerResponse.SerializeToString,
+            'Authorize': grpc.unary_unary_rpc_method_handler(
+                    servicer.Authorize,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_auth__pb2.AuthorizeRequest.FromString,
+                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
             ),
     }
     generic_handler = grpc.method_handlers_generic_handler(
-            'hacker.v1.HackerService', rpc_method_handlers)
+            'thirdparty.kfpbackend.AuthService', rpc_method_handlers)
     server.add_generic_rpc_handlers((generic_handler,))
 
 
  # This class is part of an EXPERIMENTAL API.
-class HackerService(object):
-    """The service that handles the CRUD of Hacker.
-    """
+class AuthService(object):
+    """Missing associated documentation comment in .proto file."""
 
     @staticmethod
-    def CreateHacker(request,
+    def Authorize(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/hacker.v1.HackerService/CreateHacker',
-            hacker_dot_v1_dot_hacker__service__pb2.CreateHackerRequest.SerializeToString,
-            hacker_dot_v1_dot_hacker__service__pb2.CreateHackerResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.AuthService/Authorize',
+            thirdparty_dot_kfpbackend_dot_auth__pb2.AuthorizeRequest.SerializeToString,
+            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_pb2.py`

 * *Files 24% similar despite different names*

```diff
@@ -8,25 +8,25 @@
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
 
 from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
-from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
+from ...thirdparty.kfpapi import pipeline_spec_pb2 as thirdparty_dot_kfpapi_dot_pipeline__spec__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18muses/v1/component.proto\x12\x08muses.v1\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xe3\x02\n\tComponent\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x35\n\tcomponent\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructR\tcomponent\x12<\n\rexecutor_spec\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructR\x0c\x65xecutorSpec\x12\x17\n\x07node_id\x18\x08 \x01(\tR\x06nodeId:H\xea\x41\x45\n(github.com.artistml.apis/ComponentEntity\x12\x19methods/*/components/{id}\"\x17\n\x15\x43omponentOptionFilterB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18muses/v1/component.proto\x12\x08muses.v1\x1a\x19google/api/resource.proto\x1a%thirdparty/kfpapi/pipeline_spec.proto\"\x8d\x03\n\tComponent\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12>\n\tcomponent\x18\x06 \x01(\x0b\x32 .thirdparty.kfpapi.ComponentSpecR\tcomponent\x12]\n\rexecutor_spec\x18\x07 \x01(\x0b\x32\x38.thirdparty.kfpapi.PipelineDeploymentConfig.ExecutorSpecR\x0c\x65xecutorSpec\x12\x17\n\x07node_id\x18\x08 \x01(\tR\x06nodeId:H\xea\x41\x45\n(github.com.artistml.apis/ComponentEntity\x12\x19methods/*/components/{id}\"\x17\n\x15\x43omponentOptionFilterB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'muses.v1.component_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   DESCRIPTOR._serialized_options = b'Z,github.com/artistml/apis/go/muses/v1;musesv1'
   _COMPONENT._options = None
   _COMPONENT._serialized_options = b'\352AE\n(github.com.artistml.apis/ComponentEntity\022\031methods/*/components/{id}'
-  _COMPONENT._serialized_start=96
-  _COMPONENT._serialized_end=451
-  _COMPONENTOPTIONFILTER._serialized_start=453
-  _COMPONENTOPTIONFILTER._serialized_end=476
+  _COMPONENT._serialized_start=105
+  _COMPONENT._serialized_end=502
+  _COMPONENTOPTIONFILTER._serialized_start=504
+  _COMPONENTOPTIONFILTER._serialized_end=527
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_pb2.pyi`

 * *Files 20% similar despite different names*

```diff
@@ -1,30 +1,47 @@
 """
 @generated by mypy-protobuf.  Do not edit manually!
 isort:skip_file
 """
 import builtins
 import google.protobuf.descriptor
+import google.protobuf.internal.containers
 import google.protobuf.message
-import google.protobuf.struct_pb2
+import ...muses.v1.component_pb2
+import ...tag.v1.tag_pb2
 import typing
 import typing_extensions
 
 DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
 
-class Component(google.protobuf.message.Message):
+class Method(google.protobuf.message.Message):
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
+    class ComponentsEntry(google.protobuf.message.Message):
+        DESCRIPTOR: google.protobuf.descriptor.Descriptor
+        KEY_FIELD_NUMBER: builtins.int
+        VALUE_FIELD_NUMBER: builtins.int
+        key: typing.Text
+        @property
+        def value(self) -> muses.v1.component_pb2.Component: ...
+        def __init__(self,
+            *,
+            key: typing.Text = ...,
+            value: typing.Optional[muses.v1.component_pb2.Component] = ...,
+            ) -> None: ...
+        def HasField(self, field_name: typing_extensions.Literal["value",b"value"]) -> builtins.bool: ...
+        def ClearField(self, field_name: typing_extensions.Literal["key",b"key","value",b"value"]) -> None: ...
+
     ID_FIELD_NUMBER: builtins.int
     CREATE_AT_FIELD_NUMBER: builtins.int
     UPDATE_AT_FIELD_NUMBER: builtins.int
     NAME_FIELD_NUMBER: builtins.int
     DESCRIPTION_FIELD_NUMBER: builtins.int
-    COMPONENT_FIELD_NUMBER: builtins.int
-    EXECUTOR_SPEC_FIELD_NUMBER: builtins.int
-    NODE_ID_FIELD_NUMBER: builtins.int
+    INFER_API_FIELD_NUMBER: builtins.int
+    COMPONENTS_FIELD_NUMBER: builtins.int
+    TAGS_FIELD_NUMBER: builtins.int
     id: builtins.int
     """auto increase id."""
 
     create_at: typing.Text
     """Output only. Timestamp when this Dataset was created, convert to local timezone string."""
 
     update_at: typing.Text
@@ -32,41 +49,44 @@
 
     name: typing.Text
     """unique name for method."""
 
     description: typing.Text
     """description for method."""
 
+    infer_api: typing.Text
+    """Inference API"""
+
     @property
-    def component(self) -> google.protobuf.struct_pb2.Struct:
-        """component structure load from pipeline_spec."""
+    def components(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, muses.v1.component_pb2.Component]:
+        """唯一：/{域名}/{method-name}
+        name -> Component
+        """
         pass
     @property
-    def executor_spec(self) -> google.protobuf.struct_pb2.Struct:
-        """executor_spec load from pipeline_spec."""
-        pass
-    node_id: typing.Text
-    """Node identification, outputOnly.
-    Generate by backend with timestamp, which every time you fetch for the same
-    component will get different one.
-    """
-
+    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[tag.v1.tag_pb2.Tag]: ...
     def __init__(self,
         *,
         id: builtins.int = ...,
         create_at: typing.Text = ...,
         update_at: typing.Text = ...,
         name: typing.Text = ...,
         description: typing.Text = ...,
-        component: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
-        executor_spec: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
-        node_id: typing.Text = ...,
+        infer_api: typing.Text = ...,
+        components: typing.Optional[typing.Mapping[typing.Text, muses.v1.component_pb2.Component]] = ...,
+        tags: typing.Optional[typing.Iterable[tag.v1.tag_pb2.Tag]] = ...,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions.Literal["component",b"component","executor_spec",b"executor_spec"]) -> builtins.bool: ...
-    def ClearField(self, field_name: typing_extensions.Literal["component",b"component","create_at",b"create_at","description",b"description","executor_spec",b"executor_spec","id",b"id","name",b"name","node_id",b"node_id","update_at",b"update_at"]) -> None: ...
-global___Component = Component
+    def ClearField(self, field_name: typing_extensions.Literal["components",b"components","create_at",b"create_at","description",b"description","id",b"id","infer_api",b"infer_api","name",b"name","tags",b"tags","update_at",b"update_at"]) -> None: ...
+global___Method = Method
 
-class ComponentOptionFilter(google.protobuf.message.Message):
+class MethodOptionFilter(google.protobuf.message.Message):
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
+    TAG_ID_FIELD_NUMBER: builtins.int
+    tag_id: builtins.int
+    """Filter Method by tag id."""
+
     def __init__(self,
+        *,
+        tag_id: builtins.int = ...,
         ) -> None: ...
-global___ComponentOptionFilter = ComponentOptionFilter
+    def ClearField(self, field_name: typing_extensions.Literal["tag_id",b"tag_id"]) -> None: ...
+global___MethodOptionFilter = MethodOptionFilter
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2.py`

 * *Files 4% similar despite different names*

```diff
@@ -14,17 +14,18 @@
 from ...common.v1 import types_pb2 as common_dot_v1_dot_types__pb2
 from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
 from google.api import client_pb2 as google_dot_api_dot_client__pb2
 from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
 from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
 from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
 from ...muses.v1 import component_pb2 as muses_dot_v1_dot_component__pb2
+from ...thirdparty.kfpapi import pipeline_spec_pb2 as thirdparty_dot_kfpapi_dot_pipeline__spec__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmuses/v1/flow_service.proto\x12\x08muses.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x18muses/v1/component.proto\"O\n\x11\x43reateFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\"\n\x04\x66low\x18\x02 \x01(\x0b\x32\x0e.muses.v1.FlowR\x04\x66low\"l\n\x12\x43reateFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\x8b\x01\n\x0eGetFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x37\n\tread_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\"i\n\x0fGetFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\x8c\x01\n\x11UpdateFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\"\n\x04\x66low\x18\x02 \x01(\x0b\x32\x0e.muses.v1.FlowR\x04\x66low\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"l\n\x12UpdateFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\xa0\x02\n\x10ListFlowsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12?\n\roption_filter\x18\x05 \x01(\x0b\x32\x1a.muses.v1.FlowOptionFilterR\x0coptionFilter\"\x92\x02\n\x11ListFlowsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12=\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32#.muses.v1.ListFlowsResponse.DetailsR\x07\x64\x65tails\x1a\x8f\x01\n\x07\x44\x65tails\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x0e.muses.v1.FlowR\x05items\x12=\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x1a.muses.v1.ListFlowsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\";\n\x11\x44\x65leteFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\"l\n\x12\x44\x65leteFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\xab\x01\n\x12\x44\x65leteFlowsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12?\n\roption_filter\x18\x03 \x01(\x0b\x32\x1a.muses.v1.FlowOptionFilterR\x0coptionFilter\"]\n\x13\x44\x65leteFlowsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails\"\xe8\x03\n\x04\x46low\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x18\n\x07version\x18\x05 \x01(\tR\x07version\x12<\n\rresource_spec\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructR\x0cresourceSpec\x12+\n\x11parallelism_limit\x18\x07 \x01(\x05R\x10parallelismLimit\x12>\n\ncomponents\x18\x08 \x03(\x0b\x32\x1e.muses.v1.Flow.ComponentsEntryR\ncomponents\x12\x33\n\nparameters\x18\t \x03(\x0b\x32\x13.muses.v1.ParameterR\nparameters\x1aR\n\x0f\x43omponentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x13.muses.v1.ComponentR\x05value:\x02\x38\x01:4\xea\x41\x31\n#github.com.artistml.apis/FlowEntity\x12\nflows/{id}\"\xdd\x01\n\tParameter\x12:\n\tparameter\x18\x01 \x01(\x0b\x32\x1c.muses.v1.ComponentParameterR\tparameter\x12I\n\x10parent_parameter\x18\x02 \x01(\x0b\x32\x1c.muses.v1.ComponentParameterH\x00R\x0fparentParameter\x12@\n\x0eparameter_spec\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructH\x00R\rparameterSpecB\x07\n\x05value\"L\n\x12\x43omponentParameter\x12\x17\n\x07node_id\x18\x01 \x01(\tR\x06nodeId\x12\x1d\n\nparam_name\x18\x02 \x01(\tR\tparamName\"1\n\x10\x46lowOptionFilter\x12\x1d\n\nhistory_id\x18\x01 \x01(\x03R\thistoryId2\xc0\x05\n\x0b\x46lowService\x12n\n\nCreateFlow\x12\x1b.muses.v1.CreateFlowRequest\x1a\x1c.muses.v1.CreateFlowResponse\"%\xda\x41\x0bparent,flow\x82\xd3\xe4\x93\x02\x11\"\t/v1/flows:\x04\x66low\x12\x64\n\x07GetFlow\x12\x18.muses.v1.GetFlowRequest\x1a\x19.muses.v1.GetFlowResponse\"$\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/flows/{id=*}\x12\x86\x01\n\nUpdateFlow\x12\x1b.muses.v1.UpdateFlowRequest\x1a\x1c.muses.v1.UpdateFlowResponse\"=\xda\x41\x17parent,flow,update_mask\x82\xd3\xe4\x93\x02\x1d\x32\x15/v1/flows/{flow.id=*}:\x04\x66low\x12\x64\n\tListFlows\x12\x1a.muses.v1.ListFlowsRequest\x1a\x1b.muses.v1.ListFlowsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/flows/resources:\x01*\x12m\n\nDeleteFlow\x12\x1b.muses.v1.DeleteFlowRequest\x1a\x1c.muses.v1.DeleteFlowResponse\"$\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\x12*\x10/v1/flows/{id=*}\x12`\n\x0b\x44\x65leteFlows\x12\x1c.muses.v1.DeleteFlowsRequest\x1a\x1d.muses.v1.DeleteFlowsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x32\t/v1/flows:\x01*\x1a\x1b\xca\x41\x18github.com/artistml/apisB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bmuses/v1/flow_service.proto\x12\x08muses.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x18muses/v1/component.proto\x1a%thirdparty/kfpapi/pipeline_spec.proto\"O\n\x11\x43reateFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\"\n\x04\x66low\x18\x02 \x01(\x0b\x32\x0e.muses.v1.FlowR\x04\x66low\"l\n\x12\x43reateFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\x8b\x01\n\x0eGetFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x37\n\tread_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\"i\n\x0fGetFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\x8c\x01\n\x11UpdateFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\"\n\x04\x66low\x18\x02 \x01(\x0b\x32\x0e.muses.v1.FlowR\x04\x66low\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"l\n\x12UpdateFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\xa0\x02\n\x10ListFlowsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12?\n\roption_filter\x18\x05 \x01(\x0b\x32\x1a.muses.v1.FlowOptionFilterR\x0coptionFilter\"\x92\x02\n\x11ListFlowsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12=\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32#.muses.v1.ListFlowsResponse.DetailsR\x07\x64\x65tails\x1a\x8f\x01\n\x07\x44\x65tails\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x0e.muses.v1.FlowR\x05items\x12=\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x1a.muses.v1.ListFlowsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\";\n\x11\x44\x65leteFlowRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\"l\n\x12\x44\x65leteFlowResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12(\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0e.muses.v1.FlowR\x07\x64\x65tails\"\xab\x01\n\x12\x44\x65leteFlowsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12?\n\roption_filter\x18\x03 \x01(\x0b\x32\x1a.muses.v1.FlowOptionFilterR\x0coptionFilter\"]\n\x13\x44\x65leteFlowsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails\"\x9f\x04\n\x04\x46low\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x18\n\x07version\x18\x05 \x01(\tR\x07version\x12s\n\rresource_spec\x18\x06 \x01(\x0b\x32N.thirdparty.kfpapi.PipelineDeploymentConfig.PipelineContainerSpec.ResourceSpecR\x0cresourceSpec\x12+\n\x11parallelism_limit\x18\x07 \x01(\x05R\x10parallelismLimit\x12>\n\ncomponents\x18\x08 \x03(\x0b\x32\x1e.muses.v1.Flow.ComponentsEntryR\ncomponents\x12\x33\n\nparameters\x18\t \x03(\x0b\x32\x13.muses.v1.ParameterR\nparameters\x1aR\n\x0f\x43omponentsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x13.muses.v1.ComponentR\x05value:\x02\x38\x01:4\xea\x41\x31\n#github.com.artistml.apis/FlowEntity\x12\nflows/{id}\"\xb0\x02\n\tParameter\x12:\n\tparameter\x18\x01 \x01(\x0b\x32\x1c.muses.v1.ComponentParameterR\tparameter\x12\x34\n\x08\x63onstant\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueH\x00R\x08\x63onstant\x12I\n\x10parent_parameter\x18\x03 \x01(\x0b\x32\x1c.muses.v1.ComponentParameterH\x00R\x0fparentParameter\x12]\n\x0eparameter_spec\x18\x04 \x01(\x0b\x32\x34.thirdparty.kfpapi.ComponentInputsSpec.ParameterSpecH\x00R\rparameterSpecB\x07\n\x05value\"L\n\x12\x43omponentParameter\x12\x17\n\x07node_id\x18\x01 \x01(\tR\x06nodeId\x12\x1d\n\nparam_name\x18\x02 \x01(\tR\tparamName\"1\n\x10\x46lowOptionFilter\x12\x1d\n\nhistory_id\x18\x01 \x01(\x03R\thistoryId2\xc0\x05\n\x0b\x46lowService\x12n\n\nCreateFlow\x12\x1b.muses.v1.CreateFlowRequest\x1a\x1c.muses.v1.CreateFlowResponse\"%\xda\x41\x0bparent,flow\x82\xd3\xe4\x93\x02\x11\"\t/v1/flows:\x04\x66low\x12\x64\n\x07GetFlow\x12\x18.muses.v1.GetFlowRequest\x1a\x19.muses.v1.GetFlowResponse\"$\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/flows/{id=*}\x12\x86\x01\n\nUpdateFlow\x12\x1b.muses.v1.UpdateFlowRequest\x1a\x1c.muses.v1.UpdateFlowResponse\"=\xda\x41\x17parent,flow,update_mask\x82\xd3\xe4\x93\x02\x1d\x32\x15/v1/flows/{flow.id=*}:\x04\x66low\x12\x64\n\tListFlows\x12\x1a.muses.v1.ListFlowsRequest\x1a\x1b.muses.v1.ListFlowsResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/v1/flows/resources:\x01*\x12m\n\nDeleteFlow\x12\x1b.muses.v1.DeleteFlowRequest\x1a\x1c.muses.v1.DeleteFlowResponse\"$\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\x12*\x10/v1/flows/{id=*}\x12`\n\x0b\x44\x65leteFlows\x12\x1c.muses.v1.DeleteFlowsRequest\x1a\x1d.muses.v1.DeleteFlowsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x32\t/v1/flows:\x01*\x1a\x1b\xca\x41\x18github.com/artistml/apisB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
 _builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'muses.v1.flow_service_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
   DESCRIPTOR._serialized_options = b'Z,github.com/artistml/apis/go/muses/v1;musesv1'
@@ -42,46 +43,46 @@
   _FLOWSERVICE.methods_by_name['UpdateFlow']._serialized_options = b'\332A\027parent,flow,update_mask\202\323\344\223\002\0352\025/v1/flows/{flow.id=*}:\004flow'
   _FLOWSERVICE.methods_by_name['ListFlows']._options = None
   _FLOWSERVICE.methods_by_name['ListFlows']._serialized_options = b'\202\323\344\223\002\030\"\023/v1/flows/resources:\001*'
   _FLOWSERVICE.methods_by_name['DeleteFlow']._options = None
   _FLOWSERVICE.methods_by_name['DeleteFlow']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\022*\020/v1/flows/{id=*}'
   _FLOWSERVICE.methods_by_name['DeleteFlows']._options = None
   _FLOWSERVICE.methods_by_name['DeleteFlows']._serialized_options = b'\202\323\344\223\002\0162\t/v1/flows:\001*'
-  _CREATEFLOWREQUEST._serialized_start=236
-  _CREATEFLOWREQUEST._serialized_end=315
-  _CREATEFLOWRESPONSE._serialized_start=317
-  _CREATEFLOWRESPONSE._serialized_end=425
-  _GETFLOWREQUEST._serialized_start=428
-  _GETFLOWREQUEST._serialized_end=567
-  _GETFLOWRESPONSE._serialized_start=569
-  _GETFLOWRESPONSE._serialized_end=674
-  _UPDATEFLOWREQUEST._serialized_start=677
-  _UPDATEFLOWREQUEST._serialized_end=817
-  _UPDATEFLOWRESPONSE._serialized_start=819
-  _UPDATEFLOWRESPONSE._serialized_end=927
-  _LISTFLOWSREQUEST._serialized_start=930
-  _LISTFLOWSREQUEST._serialized_end=1218
-  _LISTFLOWSRESPONSE._serialized_start=1221
-  _LISTFLOWSRESPONSE._serialized_end=1495
-  _LISTFLOWSRESPONSE_DETAILS._serialized_start=1352
-  _LISTFLOWSRESPONSE_DETAILS._serialized_end=1495
-  _DELETEFLOWREQUEST._serialized_start=1497
-  _DELETEFLOWREQUEST._serialized_end=1556
-  _DELETEFLOWRESPONSE._serialized_start=1558
-  _DELETEFLOWRESPONSE._serialized_end=1666
-  _DELETEFLOWSREQUEST._serialized_start=1669
-  _DELETEFLOWSREQUEST._serialized_end=1840
-  _DELETEFLOWSRESPONSE._serialized_start=1842
-  _DELETEFLOWSRESPONSE._serialized_end=1935
-  _FLOW._serialized_start=1938
-  _FLOW._serialized_end=2426
-  _FLOW_COMPONENTSENTRY._serialized_start=2290
-  _FLOW_COMPONENTSENTRY._serialized_end=2372
-  _PARAMETER._serialized_start=2429
-  _PARAMETER._serialized_end=2650
-  _COMPONENTPARAMETER._serialized_start=2652
-  _COMPONENTPARAMETER._serialized_end=2728
-  _FLOWOPTIONFILTER._serialized_start=2730
-  _FLOWOPTIONFILTER._serialized_end=2779
-  _FLOWSERVICE._serialized_start=2782
-  _FLOWSERVICE._serialized_end=3486
+  _CREATEFLOWREQUEST._serialized_start=275
+  _CREATEFLOWREQUEST._serialized_end=354
+  _CREATEFLOWRESPONSE._serialized_start=356
+  _CREATEFLOWRESPONSE._serialized_end=464
+  _GETFLOWREQUEST._serialized_start=467
+  _GETFLOWREQUEST._serialized_end=606
+  _GETFLOWRESPONSE._serialized_start=608
+  _GETFLOWRESPONSE._serialized_end=713
+  _UPDATEFLOWREQUEST._serialized_start=716
+  _UPDATEFLOWREQUEST._serialized_end=856
+  _UPDATEFLOWRESPONSE._serialized_start=858
+  _UPDATEFLOWRESPONSE._serialized_end=966
+  _LISTFLOWSREQUEST._serialized_start=969
+  _LISTFLOWSREQUEST._serialized_end=1257
+  _LISTFLOWSRESPONSE._serialized_start=1260
+  _LISTFLOWSRESPONSE._serialized_end=1534
+  _LISTFLOWSRESPONSE_DETAILS._serialized_start=1391
+  _LISTFLOWSRESPONSE_DETAILS._serialized_end=1534
+  _DELETEFLOWREQUEST._serialized_start=1536
+  _DELETEFLOWREQUEST._serialized_end=1595
+  _DELETEFLOWRESPONSE._serialized_start=1597
+  _DELETEFLOWRESPONSE._serialized_end=1705
+  _DELETEFLOWSREQUEST._serialized_start=1708
+  _DELETEFLOWSREQUEST._serialized_end=1879
+  _DELETEFLOWSRESPONSE._serialized_start=1881
+  _DELETEFLOWSRESPONSE._serialized_end=1974
+  _FLOW._serialized_start=1977
+  _FLOW._serialized_end=2520
+  _FLOW_COMPONENTSENTRY._serialized_start=2384
+  _FLOW_COMPONENTSENTRY._serialized_end=2466
+  _PARAMETER._serialized_start=2523
+  _PARAMETER._serialized_end=2827
+  _COMPONENTPARAMETER._serialized_start=2829
+  _COMPONENTPARAMETER._serialized_end=2905
+  _FLOWOPTIONFILTER._serialized_start=2907
+  _FLOWOPTIONFILTER._serialized_end=2956
+  _FLOWSERVICE._serialized_start=2959
+  _FLOWSERVICE._serialized_end=3663
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2.pyi`

 * *Files 2% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 import ...common.v1.types_pb2
 import google.protobuf.descriptor
 import google.protobuf.field_mask_pb2
 import google.protobuf.internal.containers
 import google.protobuf.message
 import google.protobuf.struct_pb2
 import ...muses.v1.component_pb2
+import ...thirdparty.kfpapi.pipeline_spec_pb2
 import typing
 import typing_extensions
 
 DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
 
 class CreateFlowRequest(google.protobuf.message.Message):
     """Request message for [FlowService.CreateFlow][v1.FlowService.CreateFlow]."""
@@ -417,15 +418,15 @@
     name: typing.Text
     """Name for flow."""
 
     version: typing.Text
     """Version for flow."""
 
     @property
-    def resource_spec(self) -> google.protobuf.struct_pb2.Struct:
+    def resource_spec(self) -> thirdparty.kfpapi.pipeline_spec_pb2.PipelineDeploymentConfig.PipelineContainerSpec.ResourceSpec:
         """Resource config for flow."""
         pass
     parallelism_limit: builtins.int
     """Parallelism limit of job;"""
 
     @property
     def components(self) -> google.protobuf.internal.containers.MessageMap[typing.Text, muses.v1.component_pb2.Component]:
@@ -436,54 +437,58 @@
     def __init__(self,
         *,
         id: builtins.int = ...,
         create_at: typing.Text = ...,
         update_at: typing.Text = ...,
         name: typing.Text = ...,
         version: typing.Text = ...,
-        resource_spec: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
+        resource_spec: typing.Optional[thirdparty.kfpapi.pipeline_spec_pb2.PipelineDeploymentConfig.PipelineContainerSpec.ResourceSpec] = ...,
         parallelism_limit: builtins.int = ...,
         components: typing.Optional[typing.Mapping[typing.Text, muses.v1.component_pb2.Component]] = ...,
         parameters: typing.Optional[typing.Iterable[global___Parameter]] = ...,
         ) -> None: ...
     def HasField(self, field_name: typing_extensions.Literal["resource_spec",b"resource_spec"]) -> builtins.bool: ...
     def ClearField(self, field_name: typing_extensions.Literal["components",b"components","create_at",b"create_at","id",b"id","name",b"name","parallelism_limit",b"parallelism_limit","parameters",b"parameters","resource_spec",b"resource_spec","update_at",b"update_at","version",b"version"]) -> None: ...
 global___Flow = Flow
 
 class Parameter(google.protobuf.message.Message):
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     PARAMETER_FIELD_NUMBER: builtins.int
+    CONSTANT_FIELD_NUMBER: builtins.int
     PARENT_PARAMETER_FIELD_NUMBER: builtins.int
     PARAMETER_SPEC_FIELD_NUMBER: builtins.int
     @property
     def parameter(self) -> global___ComponentParameter: ...
     @property
+    def constant(self) -> google.protobuf.struct_pb2.Value:
+        """Constant value which is determined in compile time."""
+        pass
+    @property
     def parent_parameter(self) -> global___ComponentParameter: ...
     @property
-    def parameter_spec(self) -> google.protobuf.struct_pb2.Struct:
+    def parameter_spec(self) -> thirdparty.kfpapi.pipeline_spec_pb2.ComponentInputsSpec.ParameterSpec:
         """parameter generate by kfp."""
         pass
     def __init__(self,
         *,
         parameter: typing.Optional[global___ComponentParameter] = ...,
+        constant: typing.Optional[google.protobuf.struct_pb2.Value] = ...,
         parent_parameter: typing.Optional[global___ComponentParameter] = ...,
-        parameter_spec: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
+        parameter_spec: typing.Optional[thirdparty.kfpapi.pipeline_spec_pb2.ComponentInputsSpec.ParameterSpec] = ...,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions.Literal["parameter",b"parameter","parameter_spec",b"parameter_spec","parent_parameter",b"parent_parameter","value",b"value"]) -> builtins.bool: ...
-    def ClearField(self, field_name: typing_extensions.Literal["parameter",b"parameter","parameter_spec",b"parameter_spec","parent_parameter",b"parent_parameter","value",b"value"]) -> None: ...
-    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["parent_parameter","parameter_spec"]]: ...
+    def HasField(self, field_name: typing_extensions.Literal["constant",b"constant","parameter",b"parameter","parameter_spec",b"parameter_spec","parent_parameter",b"parent_parameter","value",b"value"]) -> builtins.bool: ...
+    def ClearField(self, field_name: typing_extensions.Literal["constant",b"constant","parameter",b"parameter","parameter_spec",b"parameter_spec","parent_parameter",b"parent_parameter","value",b"value"]) -> None: ...
+    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["constant","parent_parameter","parameter_spec"]]: ...
 global___Parameter = Parameter
 
 class ComponentParameter(google.protobuf.message.Message):
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     NODE_ID_FIELD_NUMBER: builtins.int
     PARAM_NAME_FIELD_NUMBER: builtins.int
     node_id: typing.Text
-    """empty string if param_name is from root.input_definitions"""
-
     param_name: typing.Text
     def __init__(self,
         *,
         node_id: typing.Text = ...,
         param_name: typing.Text = ...,
         ) -> None: ...
     def ClearField(self, field_name: typing_extensions.Literal["node_id",b"node_id","param_name",b"param_name"]) -> None: ...
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,240 +1,303 @@
 # Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
 """Client and server classes corresponding to protobuf-defined services."""
 import grpc
 
-from ...muses.v1 import flow_service_pb2 as muses_dot_v1_dot_flow__service__pb2
+from ...muses.v1 import run_service_pb2 as muses_dot_v1_dot_run__service__pb2
 
 
-class FlowServiceStub(object):
-    """The service that handles the CRUD of Flow.
+class RunServiceStub(object):
+    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
+    info: {
+    title: "Run Service"
+    version: "1.0"
+    contact: {
+    name: "Run Service"
+    url: "http://github.com/artistml/apis"
+    }
+    }
+    host: "github.com/artistml/apis"
+    base_path: "/muses/v1/run"
+    schemes: HTTP
+    schemes: HTTPS
+    consumes: "application/json"
+    produces: "application/json"
+    external_docs: {
+    description: "API specification in Markdown",
+    url: "http://github.com/artistml/apis/muses/v1/run"
+    }
+    };
+
+    The service that handles the CRUD of Run.
     """
 
     def __init__(self, channel):
         """Constructor.
 
         Args:
             channel: A grpc.Channel.
         """
-        self.CreateFlow = channel.unary_unary(
-                '/muses.v1.FlowService/CreateFlow',
-                request_serializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowResponse.FromString,
-                )
-        self.GetFlow = channel.unary_unary(
-                '/muses.v1.FlowService/GetFlow',
-                request_serializer=muses_dot_v1_dot_flow__service__pb2.GetFlowRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_flow__service__pb2.GetFlowResponse.FromString,
-                )
-        self.UpdateFlow = channel.unary_unary(
-                '/muses.v1.FlowService/UpdateFlow',
-                request_serializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowResponse.FromString,
-                )
-        self.ListFlows = channel.unary_unary(
-                '/muses.v1.FlowService/ListFlows',
-                request_serializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsResponse.FromString,
-                )
-        self.DeleteFlow = channel.unary_unary(
-                '/muses.v1.FlowService/DeleteFlow',
-                request_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowResponse.FromString,
-                )
-        self.DeleteFlows = channel.unary_unary(
-                '/muses.v1.FlowService/DeleteFlows',
-                request_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsResponse.FromString,
+        self.CreateRun = channel.unary_unary(
+                '/muses.v1.RunService/CreateRun',
+                request_serializer=muses_dot_v1_dot_run__service__pb2.CreateRunRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_run__service__pb2.CreateRunResponse.FromString,
+                )
+        self.GetRun = channel.unary_unary(
+                '/muses.v1.RunService/GetRun',
+                request_serializer=muses_dot_v1_dot_run__service__pb2.GetRunRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_run__service__pb2.GetRunResponse.FromString,
+                )
+        self.UpdateRun = channel.unary_unary(
+                '/muses.v1.RunService/UpdateRun',
+                request_serializer=muses_dot_v1_dot_run__service__pb2.UpdateRunRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_run__service__pb2.UpdateRunResponse.FromString,
+                )
+        self.ListRuns = channel.unary_unary(
+                '/muses.v1.RunService/ListRuns',
+                request_serializer=muses_dot_v1_dot_run__service__pb2.ListRunsRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_run__service__pb2.ListRunsResponse.FromString,
+                )
+        self.DeleteRun = channel.unary_unary(
+                '/muses.v1.RunService/DeleteRun',
+                request_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunResponse.FromString,
+                )
+        self.DeleteRuns = channel.unary_unary(
+                '/muses.v1.RunService/DeleteRuns',
+                request_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsRequest.SerializeToString,
+                response_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsResponse.FromString,
                 )
 
 
-class FlowServiceServicer(object):
-    """The service that handles the CRUD of Flow.
+class RunServiceServicer(object):
+    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
+    info: {
+    title: "Run Service"
+    version: "1.0"
+    contact: {
+    name: "Run Service"
+    url: "http://github.com/artistml/apis"
+    }
+    }
+    host: "github.com/artistml/apis"
+    base_path: "/muses/v1/run"
+    schemes: HTTP
+    schemes: HTTPS
+    consumes: "application/json"
+    produces: "application/json"
+    external_docs: {
+    description: "API specification in Markdown",
+    url: "http://github.com/artistml/apis/muses/v1/run"
+    }
+    };
+
+    The service that handles the CRUD of Run.
     """
 
-    def CreateFlow(self, request, context):
-        """Creates a Flow.
+    def CreateRun(self, request, context):
+        """Creates a Run.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def GetFlow(self, request, context):
-        """Gets a Flow.
+    def GetRun(self, request, context):
+        """Gets a Run.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def UpdateFlow(self, request, context):
-        """Updates a Flow.
+    def UpdateRun(self, request, context):
+        """Updates a Run.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def ListFlows(self, request, context):
-        """Lists Flows in a Location.
+    def ListRuns(self, request, context):
+        """Lists Runs in a Location.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteFlow(self, request, context):
-        """Deletes a Flow.
+    def DeleteRun(self, request, context):
+        """Deletes a Run.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteFlows(self, request, context):
-        """Batch delete Flow by filter.
+    def DeleteRuns(self, request, context):
+        """Batch delete Run by filter.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
 
-def add_FlowServiceServicer_to_server(servicer, server):
+def add_RunServiceServicer_to_server(servicer, server):
     rpc_method_handlers = {
-            'CreateFlow': grpc.unary_unary_rpc_method_handler(
-                    servicer.CreateFlow,
-                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_flow__service__pb2.CreateFlowResponse.SerializeToString,
-            ),
-            'GetFlow': grpc.unary_unary_rpc_method_handler(
-                    servicer.GetFlow,
-                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.GetFlowRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_flow__service__pb2.GetFlowResponse.SerializeToString,
-            ),
-            'UpdateFlow': grpc.unary_unary_rpc_method_handler(
-                    servicer.UpdateFlow,
-                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_flow__service__pb2.UpdateFlowResponse.SerializeToString,
-            ),
-            'ListFlows': grpc.unary_unary_rpc_method_handler(
-                    servicer.ListFlows,
-                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_flow__service__pb2.ListFlowsResponse.SerializeToString,
-            ),
-            'DeleteFlow': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteFlow,
-                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowResponse.SerializeToString,
-            ),
-            'DeleteFlows': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteFlows,
-                    request_deserializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_flow__service__pb2.DeleteFlowsResponse.SerializeToString,
+            'CreateRun': grpc.unary_unary_rpc_method_handler(
+                    servicer.CreateRun,
+                    request_deserializer=muses_dot_v1_dot_run__service__pb2.CreateRunRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_run__service__pb2.CreateRunResponse.SerializeToString,
+            ),
+            'GetRun': grpc.unary_unary_rpc_method_handler(
+                    servicer.GetRun,
+                    request_deserializer=muses_dot_v1_dot_run__service__pb2.GetRunRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_run__service__pb2.GetRunResponse.SerializeToString,
+            ),
+            'UpdateRun': grpc.unary_unary_rpc_method_handler(
+                    servicer.UpdateRun,
+                    request_deserializer=muses_dot_v1_dot_run__service__pb2.UpdateRunRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_run__service__pb2.UpdateRunResponse.SerializeToString,
+            ),
+            'ListRuns': grpc.unary_unary_rpc_method_handler(
+                    servicer.ListRuns,
+                    request_deserializer=muses_dot_v1_dot_run__service__pb2.ListRunsRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_run__service__pb2.ListRunsResponse.SerializeToString,
+            ),
+            'DeleteRun': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteRun,
+                    request_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunResponse.SerializeToString,
+            ),
+            'DeleteRuns': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteRuns,
+                    request_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsRequest.FromString,
+                    response_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsResponse.SerializeToString,
             ),
     }
     generic_handler = grpc.method_handlers_generic_handler(
-            'muses.v1.FlowService', rpc_method_handlers)
+            'muses.v1.RunService', rpc_method_handlers)
     server.add_generic_rpc_handlers((generic_handler,))
 
 
  # This class is part of an EXPERIMENTAL API.
-class FlowService(object):
-    """The service that handles the CRUD of Flow.
+class RunService(object):
+    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
+    info: {
+    title: "Run Service"
+    version: "1.0"
+    contact: {
+    name: "Run Service"
+    url: "http://github.com/artistml/apis"
+    }
+    }
+    host: "github.com/artistml/apis"
+    base_path: "/muses/v1/run"
+    schemes: HTTP
+    schemes: HTTPS
+    consumes: "application/json"
+    produces: "application/json"
+    external_docs: {
+    description: "API specification in Markdown",
+    url: "http://github.com/artistml/apis/muses/v1/run"
+    }
+    };
+
+    The service that handles the CRUD of Run.
     """
 
     @staticmethod
-    def CreateFlow(request,
+    def CreateRun(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/CreateFlow',
-            muses_dot_v1_dot_flow__service__pb2.CreateFlowRequest.SerializeToString,
-            muses_dot_v1_dot_flow__service__pb2.CreateFlowResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/CreateRun',
+            muses_dot_v1_dot_run__service__pb2.CreateRunRequest.SerializeToString,
+            muses_dot_v1_dot_run__service__pb2.CreateRunResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def GetFlow(request,
+    def GetRun(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/GetFlow',
-            muses_dot_v1_dot_flow__service__pb2.GetFlowRequest.SerializeToString,
-            muses_dot_v1_dot_flow__service__pb2.GetFlowResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/GetRun',
+            muses_dot_v1_dot_run__service__pb2.GetRunRequest.SerializeToString,
+            muses_dot_v1_dot_run__service__pb2.GetRunResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def UpdateFlow(request,
+    def UpdateRun(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/UpdateFlow',
-            muses_dot_v1_dot_flow__service__pb2.UpdateFlowRequest.SerializeToString,
-            muses_dot_v1_dot_flow__service__pb2.UpdateFlowResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/UpdateRun',
+            muses_dot_v1_dot_run__service__pb2.UpdateRunRequest.SerializeToString,
+            muses_dot_v1_dot_run__service__pb2.UpdateRunResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def ListFlows(request,
+    def ListRuns(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/ListFlows',
-            muses_dot_v1_dot_flow__service__pb2.ListFlowsRequest.SerializeToString,
-            muses_dot_v1_dot_flow__service__pb2.ListFlowsResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/ListRuns',
+            muses_dot_v1_dot_run__service__pb2.ListRunsRequest.SerializeToString,
+            muses_dot_v1_dot_run__service__pb2.ListRunsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteFlow(request,
+    def DeleteRun(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/DeleteFlow',
-            muses_dot_v1_dot_flow__service__pb2.DeleteFlowRequest.SerializeToString,
-            muses_dot_v1_dot_flow__service__pb2.DeleteFlowResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/DeleteRun',
+            muses_dot_v1_dot_run__service__pb2.DeleteRunRequest.SerializeToString,
+            muses_dot_v1_dot_run__service__pb2.DeleteRunResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteFlows(request,
+    def DeleteRuns(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.FlowService/DeleteFlows',
-            muses_dot_v1_dot_flow__service__pb2.DeleteFlowsRequest.SerializeToString,
-            muses_dot_v1_dot_flow__service__pb2.DeleteFlowsResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/DeleteRuns',
+            muses_dot_v1_dot_run__service__pb2.DeleteRunsRequest.SerializeToString,
+            muses_dot_v1_dot_run__service__pb2.DeleteRunsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/flow_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/method_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_pb2.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,32 +1,31 @@
 # -*- coding: utf-8 -*-
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
-# source: muses/v1/run.proto
+# source: tag/v1/tag.proto
 """Generated protocol buffer code."""
 from google.protobuf.internal import builder as _builder
 from google.protobuf import descriptor as _descriptor
 from google.protobuf import descriptor_pool as _descriptor_pool
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
 
 from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
-from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12muses/v1/run.proto\x12\x08muses.v1\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\"\x9f\x03\n\x03Run\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x17\n\x07\x66low_id\x18\x04 \x01(\x03R\x06\x66lowId\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name\x12\x31\n\x07trigger\x18\x06 \x01(\x0b\x32\x17.google.protobuf.StructR\x07trigger\x12<\n\rpipeline_spec\x18\x07 \x01(\x0b\x32\x17.google.protobuf.StructR\x0cpipelineSpec\x12\x36\n\nrun_detail\x18\x08 \x01(\x0b\x32\x17.google.protobuf.StructR\trunDetail\x12\x1e\n\nexperiment\x18\t \x01(\tR\nexperiment\x12\x1c\n\tnamespace\x18\n \x01(\tR\tnamespace::\xea\x41\x37\n\"github.com.artistml.apis/RunEntity\x12\x11\x66lows/*/runs/{id}\"\x11\n\x0fRunOptionFilterB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10tag/v1/tag.proto\x12\x06tag.v1\x1a\x19google/api/resource.proto\"\x96\x02\n\x03Tag\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x12\n\x04icon\x18\x05 \x01(\tR\x04icon\x12\x1d\n\nfont_color\x18\x06 \x01(\tR\tfontColor\x12!\n\x0cinherit_from\x18\x07 \x01(\x03R\x0binheritFrom\x12\'\n\x08\x63hildren\x18\x08 \x03(\x0b\x32\x0b.tag.v1.TagR\x08\x63hildren:2\xea\x41/\n\"github.com.artistml.apis/TagEntity\x12\ttags/{id}\"4\n\x0fTagOptionFilter\x12!\n\x0cinherit_from\x18\x01 \x01(\x03R\x0binheritFromB*Z(github.com/artistml/apis/go/tag/v1;tagv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
-_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'muses.v1.run_pb2', globals())
+_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tag.v1.tag_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
-  DESCRIPTOR._serialized_options = b'Z,github.com/artistml/apis/go/muses/v1;musesv1'
-  _RUN._options = None
-  _RUN._serialized_options = b'\352A7\n\"github.com.artistml.apis/RunEntity\022\021flows/*/runs/{id}'
-  _RUN._serialized_start=90
-  _RUN._serialized_end=505
-  _RUNOPTIONFILTER._serialized_start=507
-  _RUNOPTIONFILTER._serialized_end=524
+  DESCRIPTOR._serialized_options = b'Z(github.com/artistml/apis/go/tag/v1;tagv1'
+  _TAG._options = None
+  _TAG._serialized_options = b'\352A/\n\"github.com.artistml.apis/TagEntity\022\ttags/{id}'
+  _TAG._serialized_start=56
+  _TAG._serialized_end=334
+  _TAGOPTIONFILTER._serialized_start=336
+  _TAGOPTIONFILTER._serialized_end=388
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/component_pb2.pyi`

 * *Files 21% similar despite different names*

```diff
@@ -1,78 +1,72 @@
 """
 @generated by mypy-protobuf.  Do not edit manually!
 isort:skip_file
 """
 import builtins
 import google.protobuf.descriptor
 import google.protobuf.message
-import google.protobuf.struct_pb2
+import ...thirdparty.kfpapi.pipeline_spec_pb2
 import typing
 import typing_extensions
 
 DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
 
-class Run(google.protobuf.message.Message):
+class Component(google.protobuf.message.Message):
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     ID_FIELD_NUMBER: builtins.int
     CREATE_AT_FIELD_NUMBER: builtins.int
     UPDATE_AT_FIELD_NUMBER: builtins.int
-    FLOW_ID_FIELD_NUMBER: builtins.int
     NAME_FIELD_NUMBER: builtins.int
-    TRIGGER_FIELD_NUMBER: builtins.int
-    PIPELINE_SPEC_FIELD_NUMBER: builtins.int
-    RUN_DETAIL_FIELD_NUMBER: builtins.int
-    EXPERIMENT_FIELD_NUMBER: builtins.int
-    NAMESPACE_FIELD_NUMBER: builtins.int
+    DESCRIPTION_FIELD_NUMBER: builtins.int
+    COMPONENT_FIELD_NUMBER: builtins.int
+    EXECUTOR_SPEC_FIELD_NUMBER: builtins.int
+    NODE_ID_FIELD_NUMBER: builtins.int
     id: builtins.int
     """auto increase id."""
 
     create_at: typing.Text
     """Output only. Timestamp when this Dataset was created, convert to local timezone string."""
 
     update_at: typing.Text
     """Output only. Timestamp when this Dataset was last updated, convert to local timezone string."""
 
-    flow_id: builtins.int
     name: typing.Text
-    """Unique name for run, defined by user or generate for scheduler job."""
+    """unique name for method."""
+
+    description: typing.Text
+    """description for method."""
 
     @property
-    def trigger(self) -> google.protobuf.struct_pb2.Struct:
-        """Runner config."""
-        pass
-    @property
-    def pipeline_spec(self) -> google.protobuf.struct_pb2.Struct:
-        """Definition of the input parameters and artifacts of the flow."""
+    def component(self) -> thirdparty.kfpapi.pipeline_spec_pb2.ComponentSpec:
+        """component structure load from pipeline_spec."""
         pass
     @property
-    def run_detail(self) -> google.protobuf.struct_pb2.Struct:
-        """The output from kfp."""
+    def executor_spec(self) -> thirdparty.kfpapi.pipeline_spec_pb2.PipelineDeploymentConfig.ExecutorSpec:
+        """executor_spec load from pipeline_spec."""
         pass
-    experiment: typing.Text
-    """Create run in this experiment, experiment will be create if it does not exists."""
-
-    namespace: typing.Text
-    """Namespace that bind to experiment and run."""
+    node_id: typing.Text
+    """Node identification, outputOnly.
+    Generate by backend with timestamp, which every time you fetch for the same
+    component will get different one.
+    """
 
     def __init__(self,
         *,
         id: builtins.int = ...,
         create_at: typing.Text = ...,
         update_at: typing.Text = ...,
-        flow_id: builtins.int = ...,
         name: typing.Text = ...,
-        trigger: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
-        pipeline_spec: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
-        run_detail: typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
-        experiment: typing.Text = ...,
-        namespace: typing.Text = ...,
+        description: typing.Text = ...,
+        component: typing.Optional[thirdparty.kfpapi.pipeline_spec_pb2.ComponentSpec] = ...,
+        executor_spec: typing.Optional[thirdparty.kfpapi.pipeline_spec_pb2.PipelineDeploymentConfig.ExecutorSpec] = ...,
+        node_id: typing.Text = ...,
         ) -> None: ...
-    def HasField(self, field_name: typing_extensions.Literal["pipeline_spec",b"pipeline_spec","run_detail",b"run_detail","trigger",b"trigger"]) -> builtins.bool: ...
-    def ClearField(self, field_name: typing_extensions.Literal["create_at",b"create_at","experiment",b"experiment","flow_id",b"flow_id","id",b"id","name",b"name","namespace",b"namespace","pipeline_spec",b"pipeline_spec","run_detail",b"run_detail","trigger",b"trigger","update_at",b"update_at"]) -> None: ...
-global___Run = Run
+    def HasField(self, field_name: typing_extensions.Literal["component",b"component","executor_spec",b"executor_spec"]) -> builtins.bool: ...
+    def ClearField(self, field_name: typing_extensions.Literal["component",b"component","create_at",b"create_at","description",b"description","executor_spec",b"executor_spec","id",b"id","name",b"name","node_id",b"node_id","update_at",b"update_at"]) -> None: ...
+global___Component = Component
 
-class RunOptionFilter(google.protobuf.message.Message):
+class ComponentOptionFilter(google.protobuf.message.Message):
     DESCRIPTOR: google.protobuf.descriptor.Descriptor
     def __init__(self,
         ) -> None: ...
-global___RunOptionFilter = RunOptionFilter
+global___ComponentOptionFilter = ComponentOptionFilter
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,71 +1,71 @@
 # -*- coding: utf-8 -*-
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
-# source: muses/v1/run_service.proto
+# source: tag/v1/tag_service.proto
 """Generated protocol buffer code."""
 from google.protobuf.internal import builder as _builder
 from google.protobuf import descriptor as _descriptor
 from google.protobuf import descriptor_pool as _descriptor_pool
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
 
 from ...common.v1 import types_pb2 as common_dot_v1_dot_types__pb2
 from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
 from google.api import client_pb2 as google_dot_api_dot_client__pb2
 from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
-from ...muses.v1 import run_pb2 as muses_dot_v1_dot_run__pb2
+from ...tag.v1 import tag_pb2 as tag_dot_v1_dot_tag__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1amuses/v1/run_service.proto\x12\x08muses.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a google/protobuf/field_mask.proto\x1a\x12muses/v1/run.proto\"K\n\x10\x43reateRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1f\n\x03run\x18\x02 \x01(\x0b\x32\r.muses.v1.RunR\x03run\"j\n\x11\x43reateRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"p\n\rGetRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x37\n\tread_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"g\n\x0eGetRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"\x88\x01\n\x10UpdateRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1f\n\x03run\x18\x02 \x01(\x0b\x32\r.muses.v1.RunR\x03run\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"j\n\x11UpdateRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"\x9e\x02\n\x0fListRunsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12>\n\roption_filter\x18\x05 \x01(\x0b\x32\x19.muses.v1.RunOptionFilterR\x0coptionFilter\"\x8e\x02\n\x10ListRunsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12<\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\".muses.v1.ListRunsResponse.DetailsR\x07\x64\x65tails\x1a\x8d\x01\n\x07\x44\x65tails\x12#\n\x05items\x18\x01 \x03(\x0b\x32\r.muses.v1.RunR\x05items\x12<\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x19.muses.v1.ListRunsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\":\n\x10\x44\x65leteRunRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\"j\n\x11\x44\x65leteRunResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\'\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\r.muses.v1.RunR\x07\x64\x65tails\"\xa9\x01\n\x11\x44\x65leteRunsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12>\n\roption_filter\x18\x03 \x01(\x0b\x32\x19.muses.v1.RunOptionFilterR\x0coptionFilter\"\\\n\x12\x44\x65leteRunsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails2\x88\x06\n\nRunService\x12y\n\tCreateRun\x12\x1a.muses.v1.CreateRunRequest\x1a\x1b.muses.v1.CreateRunResponse\"3\xda\x41\nparent,run\x82\xd3\xe4\x93\x02 \"\x19/v1/{parent=flows/*}/runs:\x03run\x12q\n\x06GetRun\x12\x17.muses.v1.GetRunRequest\x1a\x18.muses.v1.GetRunResponse\"4\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\"\x12 /v1/{parent=flows/*}/runs/{id=*}\x12\x90\x01\n\tUpdateRun\x12\x1a.muses.v1.UpdateRunRequest\x1a\x1b.muses.v1.UpdateRunResponse\"J\xda\x41\x16parent,run,update_mask\x82\xd3\xe4\x93\x02+2$/v1/{parent=flows/*}/runs/{run.id=*}:\x03run\x12q\n\x08ListRuns\x12\x19.muses.v1.ListRunsRequest\x1a\x1a.muses.v1.ListRunsResponse\".\x82\xd3\xe4\x93\x02(\"#/v1/{parent=flows/*}/runs/resources:\x01*\x12z\n\tDeleteRun\x12\x1a.muses.v1.DeleteRunRequest\x1a\x1b.muses.v1.DeleteRunResponse\"4\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\"* /v1/{parent=flows/*}/runs/{id=*}\x12m\n\nDeleteRuns\x12\x1b.muses.v1.DeleteRunsRequest\x1a\x1c.muses.v1.DeleteRunsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x32\x19/v1/{parent=flows/*}/runs:\x01*\x1a\x1b\xca\x41\x18github.com/artistml/apisB.Z,github.com/artistml/apis/go/muses/v1;musesv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18tag/v1/tag_service.proto\x12\x06tag.v1\x1a\x15\x63ommon/v1/types.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a google/protobuf/field_mask.proto\x1a\x10tag/v1/tag.proto\"I\n\x10\x43reateTagRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1d\n\x03tag\x18\x02 \x01(\x0b\x32\x0b.tag.v1.TagR\x03tag\"h\n\x11\x43reateTagResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12%\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0b.tag.v1.TagR\x07\x64\x65tails\"p\n\rGetTagRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\x12\x37\n\tread_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\"e\n\x0eGetTagResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12%\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0b.tag.v1.TagR\x07\x64\x65tails\"\x86\x01\n\x10UpdateTagRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x1d\n\x03tag\x18\x02 \x01(\x0b\x32\x0b.tag.v1.TagR\x03tag\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"h\n\x11UpdateTagResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12%\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0b.tag.v1.TagR\x07\x64\x65tails\"\x9c\x02\n\x0fListTagsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_option\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonOptionR\x0c\x63ommonOption\x12<\n\rcommon_filter\x18\x03 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12<\n\roption_filter\x18\x05 \x01(\x0b\x32\x17.tag.v1.TagOptionFilterR\x0coptionFilter\"\x88\x02\n\x10ListTagsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12:\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32 .tag.v1.ListTagsResponse.DetailsR\x07\x64\x65tails\x1a\x89\x01\n\x07\x44\x65tails\x12!\n\x05items\x18\x01 \x03(\x0b\x32\x0b.tag.v1.TagR\x05items\x12:\n\x0cnext_request\x18\x02 \x01(\x0b\x32\x17.tag.v1.ListTagsRequestR\x0bnextRequest\x12\x1f\n\x0btotal_count\x18\x03 \x01(\x05R\ntotalCount\":\n\x10\x44\x65leteTagRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12\x0e\n\x02id\x18\x02 \x01(\x03R\x02id\"h\n\x11\x44\x65leteTagResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12%\n\x07\x64\x65tails\x18\x03 \x01(\x0b\x32\x0b.tag.v1.TagR\x07\x64\x65tails\"\xa7\x01\n\x11\x44\x65leteTagsRequest\x12\x16\n\x06parent\x18\x01 \x01(\tR\x06parent\x12<\n\rcommon_filter\x18\x02 \x01(\x0b\x32\x17.common.v1.CommonFilterR\x0c\x63ommonFilter\x12<\n\roption_filter\x18\x03 \x01(\x0b\x32\x17.tag.v1.TagOptionFilterR\x0coptionFilter\"\\\n\x12\x44\x65leteTagsResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\x05R\x04\x63ode\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x03 \x03(\x03R\x07\x64\x65tails2\x89\x05\n\nTagService\x12\x64\n\tCreateTag\x12\x18.tag.v1.CreateTagRequest\x1a\x19.tag.v1.CreateTagResponse\"\"\xda\x41\nparent,tag\x82\xd3\xe4\x93\x02\x0f\"\x08/v1/tags:\x03tag\x12\\\n\x06GetTag\x12\x15.tag.v1.GetTagRequest\x1a\x16.tag.v1.GetTagResponse\"#\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/tags/{id=*}\x12{\n\tUpdateTag\x12\x18.tag.v1.UpdateTagRequest\x1a\x19.tag.v1.UpdateTagResponse\"9\xda\x41\x16parent,tag,update_mask\x82\xd3\xe4\x93\x02\x1a\x32\x13/v1/tags/{tag.id=*}:\x03tag\x12\\\n\x08ListTags\x12\x17.tag.v1.ListTagsRequest\x1a\x18.tag.v1.ListTagsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/tags/resources:\x01*\x12\x65\n\tDeleteTag\x12\x18.tag.v1.DeleteTagRequest\x1a\x19.tag.v1.DeleteTagResponse\"#\xda\x41\tparent,id\x82\xd3\xe4\x93\x02\x11*\x0f/v1/tags/{id=*}\x12X\n\nDeleteTags\x12\x19.tag.v1.DeleteTagsRequest\x1a\x1a.tag.v1.DeleteTagsResponse\"\x13\x82\xd3\xe4\x93\x02\r2\x08/v1/tags:\x01*\x1a\x1b\xca\x41\x18github.com/artistml/apisB*Z(github.com/artistml/apis/go/tag/v1;tagv1b\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
-_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'muses.v1.run_service_pb2', globals())
+_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tag.v1.tag_service_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
-  DESCRIPTOR._serialized_options = b'Z,github.com/artistml/apis/go/muses/v1;musesv1'
-  _RUNSERVICE._options = None
-  _RUNSERVICE._serialized_options = b'\312A\030github.com/artistml/apis'
-  _RUNSERVICE.methods_by_name['CreateRun']._options = None
-  _RUNSERVICE.methods_by_name['CreateRun']._serialized_options = b'\332A\nparent,run\202\323\344\223\002 \"\031/v1/{parent=flows/*}/runs:\003run'
-  _RUNSERVICE.methods_by_name['GetRun']._options = None
-  _RUNSERVICE.methods_by_name['GetRun']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\"\022 /v1/{parent=flows/*}/runs/{id=*}'
-  _RUNSERVICE.methods_by_name['UpdateRun']._options = None
-  _RUNSERVICE.methods_by_name['UpdateRun']._serialized_options = b'\332A\026parent,run,update_mask\202\323\344\223\002+2$/v1/{parent=flows/*}/runs/{run.id=*}:\003run'
-  _RUNSERVICE.methods_by_name['ListRuns']._options = None
-  _RUNSERVICE.methods_by_name['ListRuns']._serialized_options = b'\202\323\344\223\002(\"#/v1/{parent=flows/*}/runs/resources:\001*'
-  _RUNSERVICE.methods_by_name['DeleteRun']._options = None
-  _RUNSERVICE.methods_by_name['DeleteRun']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\"* /v1/{parent=flows/*}/runs/{id=*}'
-  _RUNSERVICE.methods_by_name['DeleteRuns']._options = None
-  _RUNSERVICE.methods_by_name['DeleteRuns']._serialized_options = b'\202\323\344\223\002\0362\031/v1/{parent=flows/*}/runs:\001*'
-  _CREATERUNREQUEST._serialized_start=172
-  _CREATERUNREQUEST._serialized_end=247
-  _CREATERUNRESPONSE._serialized_start=249
-  _CREATERUNRESPONSE._serialized_end=355
-  _GETRUNREQUEST._serialized_start=357
-  _GETRUNREQUEST._serialized_end=469
-  _GETRUNRESPONSE._serialized_start=471
-  _GETRUNRESPONSE._serialized_end=574
-  _UPDATERUNREQUEST._serialized_start=577
-  _UPDATERUNREQUEST._serialized_end=713
-  _UPDATERUNRESPONSE._serialized_start=715
-  _UPDATERUNRESPONSE._serialized_end=821
-  _LISTRUNSREQUEST._serialized_start=824
-  _LISTRUNSREQUEST._serialized_end=1110
-  _LISTRUNSRESPONSE._serialized_start=1113
-  _LISTRUNSRESPONSE._serialized_end=1383
-  _LISTRUNSRESPONSE_DETAILS._serialized_start=1242
-  _LISTRUNSRESPONSE_DETAILS._serialized_end=1383
-  _DELETERUNREQUEST._serialized_start=1385
-  _DELETERUNREQUEST._serialized_end=1443
-  _DELETERUNRESPONSE._serialized_start=1445
-  _DELETERUNRESPONSE._serialized_end=1551
-  _DELETERUNSREQUEST._serialized_start=1554
-  _DELETERUNSREQUEST._serialized_end=1723
-  _DELETERUNSRESPONSE._serialized_start=1725
-  _DELETERUNSRESPONSE._serialized_end=1817
-  _RUNSERVICE._serialized_start=1820
-  _RUNSERVICE._serialized_end=2596
+  DESCRIPTOR._serialized_options = b'Z(github.com/artistml/apis/go/tag/v1;tagv1'
+  _TAGSERVICE._options = None
+  _TAGSERVICE._serialized_options = b'\312A\030github.com/artistml/apis'
+  _TAGSERVICE.methods_by_name['CreateTag']._options = None
+  _TAGSERVICE.methods_by_name['CreateTag']._serialized_options = b'\332A\nparent,tag\202\323\344\223\002\017\"\010/v1/tags:\003tag'
+  _TAGSERVICE.methods_by_name['GetTag']._options = None
+  _TAGSERVICE.methods_by_name['GetTag']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\021\022\017/v1/tags/{id=*}'
+  _TAGSERVICE.methods_by_name['UpdateTag']._options = None
+  _TAGSERVICE.methods_by_name['UpdateTag']._serialized_options = b'\332A\026parent,tag,update_mask\202\323\344\223\002\0322\023/v1/tags/{tag.id=*}:\003tag'
+  _TAGSERVICE.methods_by_name['ListTags']._options = None
+  _TAGSERVICE.methods_by_name['ListTags']._serialized_options = b'\202\323\344\223\002\027\"\022/v1/tags/resources:\001*'
+  _TAGSERVICE.methods_by_name['DeleteTag']._options = None
+  _TAGSERVICE.methods_by_name['DeleteTag']._serialized_options = b'\332A\tparent,id\202\323\344\223\002\021*\017/v1/tags/{id=*}'
+  _TAGSERVICE.methods_by_name['DeleteTags']._options = None
+  _TAGSERVICE.methods_by_name['DeleteTags']._serialized_options = b'\202\323\344\223\002\r2\010/v1/tags:\001*'
+  _CREATETAGREQUEST._serialized_start=166
+  _CREATETAGREQUEST._serialized_end=239
+  _CREATETAGRESPONSE._serialized_start=241
+  _CREATETAGRESPONSE._serialized_end=345
+  _GETTAGREQUEST._serialized_start=347
+  _GETTAGREQUEST._serialized_end=459
+  _GETTAGRESPONSE._serialized_start=461
+  _GETTAGRESPONSE._serialized_end=562
+  _UPDATETAGREQUEST._serialized_start=565
+  _UPDATETAGREQUEST._serialized_end=699
+  _UPDATETAGRESPONSE._serialized_start=701
+  _UPDATETAGRESPONSE._serialized_end=805
+  _LISTTAGSREQUEST._serialized_start=808
+  _LISTTAGSREQUEST._serialized_end=1092
+  _LISTTAGSRESPONSE._serialized_start=1095
+  _LISTTAGSRESPONSE._serialized_end=1359
+  _LISTTAGSRESPONSE_DETAILS._serialized_start=1222
+  _LISTTAGSRESPONSE_DETAILS._serialized_end=1359
+  _DELETETAGREQUEST._serialized_start=1361
+  _DELETETAGREQUEST._serialized_end=1419
+  _DELETETAGRESPONSE._serialized_start=1421
+  _DELETETAGRESPONSE._serialized_end=1525
+  _DELETETAGSREQUEST._serialized_start=1528
+  _DELETETAGSREQUEST._serialized_end=1695
+  _DELETETAGSRESPONSE._serialized_start=1697
+  _DELETETAGSRESPONSE._serialized_end=1789
+  _TAGSERVICE._serialized_start=1792
+  _TAGSERVICE._serialized_end=2441
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,303 +1,303 @@
 # Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
 """Client and server classes corresponding to protobuf-defined services."""
 import grpc
 
-from ...muses.v1 import run_service_pb2 as muses_dot_v1_dot_run__service__pb2
+from ...tag.v1 import tag_service_pb2 as tag_dot_v1_dot_tag__service__pb2
 
 
-class RunServiceStub(object):
+class TagServiceStub(object):
     """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
     info: {
-    title: "Run Service"
+    title: "Tag Service"
     version: "1.0"
     contact: {
-    name: "Run Service"
+    name: "Tag Service"
     url: "http://github.com/artistml/apis"
     }
     }
     host: "github.com/artistml/apis"
-    base_path: "/muses/v1/run"
+    base_path: "/tag/v1/tag"
     schemes: HTTP
     schemes: HTTPS
     consumes: "application/json"
     produces: "application/json"
     external_docs: {
     description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/muses/v1/run"
+    url: "http://github.com/artistml/apis/tag/v1/tag"
     }
     };
 
-    The service that handles the CRUD of Run.
+    The service that handles the CRUD of Tag.
     """
 
     def __init__(self, channel):
         """Constructor.
 
         Args:
             channel: A grpc.Channel.
         """
-        self.CreateRun = channel.unary_unary(
-                '/muses.v1.RunService/CreateRun',
-                request_serializer=muses_dot_v1_dot_run__service__pb2.CreateRunRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_run__service__pb2.CreateRunResponse.FromString,
+        self.CreateTag = channel.unary_unary(
+                '/tag.v1.TagService/CreateTag',
+                request_serializer=tag_dot_v1_dot_tag__service__pb2.CreateTagRequest.SerializeToString,
+                response_deserializer=tag_dot_v1_dot_tag__service__pb2.CreateTagResponse.FromString,
                 )
-        self.GetRun = channel.unary_unary(
-                '/muses.v1.RunService/GetRun',
-                request_serializer=muses_dot_v1_dot_run__service__pb2.GetRunRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_run__service__pb2.GetRunResponse.FromString,
+        self.GetTag = channel.unary_unary(
+                '/tag.v1.TagService/GetTag',
+                request_serializer=tag_dot_v1_dot_tag__service__pb2.GetTagRequest.SerializeToString,
+                response_deserializer=tag_dot_v1_dot_tag__service__pb2.GetTagResponse.FromString,
                 )
-        self.UpdateRun = channel.unary_unary(
-                '/muses.v1.RunService/UpdateRun',
-                request_serializer=muses_dot_v1_dot_run__service__pb2.UpdateRunRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_run__service__pb2.UpdateRunResponse.FromString,
+        self.UpdateTag = channel.unary_unary(
+                '/tag.v1.TagService/UpdateTag',
+                request_serializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagRequest.SerializeToString,
+                response_deserializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagResponse.FromString,
                 )
-        self.ListRuns = channel.unary_unary(
-                '/muses.v1.RunService/ListRuns',
-                request_serializer=muses_dot_v1_dot_run__service__pb2.ListRunsRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_run__service__pb2.ListRunsResponse.FromString,
+        self.ListTags = channel.unary_unary(
+                '/tag.v1.TagService/ListTags',
+                request_serializer=tag_dot_v1_dot_tag__service__pb2.ListTagsRequest.SerializeToString,
+                response_deserializer=tag_dot_v1_dot_tag__service__pb2.ListTagsResponse.FromString,
                 )
-        self.DeleteRun = channel.unary_unary(
-                '/muses.v1.RunService/DeleteRun',
-                request_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunResponse.FromString,
+        self.DeleteTag = channel.unary_unary(
+                '/tag.v1.TagService/DeleteTag',
+                request_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagRequest.SerializeToString,
+                response_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagResponse.FromString,
                 )
-        self.DeleteRuns = channel.unary_unary(
-                '/muses.v1.RunService/DeleteRuns',
-                request_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsRequest.SerializeToString,
-                response_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsResponse.FromString,
+        self.DeleteTags = channel.unary_unary(
+                '/tag.v1.TagService/DeleteTags',
+                request_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsRequest.SerializeToString,
+                response_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsResponse.FromString,
                 )
 
 
-class RunServiceServicer(object):
+class TagServiceServicer(object):
     """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
     info: {
-    title: "Run Service"
+    title: "Tag Service"
     version: "1.0"
     contact: {
-    name: "Run Service"
+    name: "Tag Service"
     url: "http://github.com/artistml/apis"
     }
     }
     host: "github.com/artistml/apis"
-    base_path: "/muses/v1/run"
+    base_path: "/tag/v1/tag"
     schemes: HTTP
     schemes: HTTPS
     consumes: "application/json"
     produces: "application/json"
     external_docs: {
     description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/muses/v1/run"
+    url: "http://github.com/artistml/apis/tag/v1/tag"
     }
     };
 
-    The service that handles the CRUD of Run.
+    The service that handles the CRUD of Tag.
     """
 
-    def CreateRun(self, request, context):
-        """Creates a Run.
+    def CreateTag(self, request, context):
+        """Creates a Tag.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def GetRun(self, request, context):
-        """Gets a Run.
+    def GetTag(self, request, context):
+        """Gets a Tag.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def UpdateRun(self, request, context):
-        """Updates a Run.
+    def UpdateTag(self, request, context):
+        """Updates a Tag.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def ListRuns(self, request, context):
-        """Lists Runs in a Location.
+    def ListTags(self, request, context):
+        """Lists Tags in a Location.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteRun(self, request, context):
-        """Deletes a Run.
+    def DeleteTag(self, request, context):
+        """Deletes a Tag.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteRuns(self, request, context):
-        """Batch delete Run by filter.
+    def DeleteTags(self, request, context):
+        """Batch delete Tag by filter.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
 
-def add_RunServiceServicer_to_server(servicer, server):
+def add_TagServiceServicer_to_server(servicer, server):
     rpc_method_handlers = {
-            'CreateRun': grpc.unary_unary_rpc_method_handler(
-                    servicer.CreateRun,
-                    request_deserializer=muses_dot_v1_dot_run__service__pb2.CreateRunRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_run__service__pb2.CreateRunResponse.SerializeToString,
+            'CreateTag': grpc.unary_unary_rpc_method_handler(
+                    servicer.CreateTag,
+                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.CreateTagRequest.FromString,
+                    response_serializer=tag_dot_v1_dot_tag__service__pb2.CreateTagResponse.SerializeToString,
             ),
-            'GetRun': grpc.unary_unary_rpc_method_handler(
-                    servicer.GetRun,
-                    request_deserializer=muses_dot_v1_dot_run__service__pb2.GetRunRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_run__service__pb2.GetRunResponse.SerializeToString,
+            'GetTag': grpc.unary_unary_rpc_method_handler(
+                    servicer.GetTag,
+                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.GetTagRequest.FromString,
+                    response_serializer=tag_dot_v1_dot_tag__service__pb2.GetTagResponse.SerializeToString,
             ),
-            'UpdateRun': grpc.unary_unary_rpc_method_handler(
-                    servicer.UpdateRun,
-                    request_deserializer=muses_dot_v1_dot_run__service__pb2.UpdateRunRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_run__service__pb2.UpdateRunResponse.SerializeToString,
+            'UpdateTag': grpc.unary_unary_rpc_method_handler(
+                    servicer.UpdateTag,
+                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagRequest.FromString,
+                    response_serializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagResponse.SerializeToString,
             ),
-            'ListRuns': grpc.unary_unary_rpc_method_handler(
-                    servicer.ListRuns,
-                    request_deserializer=muses_dot_v1_dot_run__service__pb2.ListRunsRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_run__service__pb2.ListRunsResponse.SerializeToString,
+            'ListTags': grpc.unary_unary_rpc_method_handler(
+                    servicer.ListTags,
+                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.ListTagsRequest.FromString,
+                    response_serializer=tag_dot_v1_dot_tag__service__pb2.ListTagsResponse.SerializeToString,
             ),
-            'DeleteRun': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteRun,
-                    request_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunResponse.SerializeToString,
+            'DeleteTag': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteTag,
+                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagRequest.FromString,
+                    response_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagResponse.SerializeToString,
             ),
-            'DeleteRuns': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteRuns,
-                    request_deserializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsRequest.FromString,
-                    response_serializer=muses_dot_v1_dot_run__service__pb2.DeleteRunsResponse.SerializeToString,
+            'DeleteTags': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteTags,
+                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsRequest.FromString,
+                    response_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsResponse.SerializeToString,
             ),
     }
     generic_handler = grpc.method_handlers_generic_handler(
-            'muses.v1.RunService', rpc_method_handlers)
+            'tag.v1.TagService', rpc_method_handlers)
     server.add_generic_rpc_handlers((generic_handler,))
 
 
  # This class is part of an EXPERIMENTAL API.
-class RunService(object):
+class TagService(object):
     """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
     info: {
-    title: "Run Service"
+    title: "Tag Service"
     version: "1.0"
     contact: {
-    name: "Run Service"
+    name: "Tag Service"
     url: "http://github.com/artistml/apis"
     }
     }
     host: "github.com/artistml/apis"
-    base_path: "/muses/v1/run"
+    base_path: "/tag/v1/tag"
     schemes: HTTP
     schemes: HTTPS
     consumes: "application/json"
     produces: "application/json"
     external_docs: {
     description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/muses/v1/run"
+    url: "http://github.com/artistml/apis/tag/v1/tag"
     }
     };
 
-    The service that handles the CRUD of Run.
+    The service that handles the CRUD of Tag.
     """
 
     @staticmethod
-    def CreateRun(request,
+    def CreateTag(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/CreateRun',
-            muses_dot_v1_dot_run__service__pb2.CreateRunRequest.SerializeToString,
-            muses_dot_v1_dot_run__service__pb2.CreateRunResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/CreateTag',
+            tag_dot_v1_dot_tag__service__pb2.CreateTagRequest.SerializeToString,
+            tag_dot_v1_dot_tag__service__pb2.CreateTagResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def GetRun(request,
+    def GetTag(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/GetRun',
-            muses_dot_v1_dot_run__service__pb2.GetRunRequest.SerializeToString,
-            muses_dot_v1_dot_run__service__pb2.GetRunResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/GetTag',
+            tag_dot_v1_dot_tag__service__pb2.GetTagRequest.SerializeToString,
+            tag_dot_v1_dot_tag__service__pb2.GetTagResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def UpdateRun(request,
+    def UpdateTag(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/UpdateRun',
-            muses_dot_v1_dot_run__service__pb2.UpdateRunRequest.SerializeToString,
-            muses_dot_v1_dot_run__service__pb2.UpdateRunResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/UpdateTag',
+            tag_dot_v1_dot_tag__service__pb2.UpdateTagRequest.SerializeToString,
+            tag_dot_v1_dot_tag__service__pb2.UpdateTagResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def ListRuns(request,
+    def ListTags(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/ListRuns',
-            muses_dot_v1_dot_run__service__pb2.ListRunsRequest.SerializeToString,
-            muses_dot_v1_dot_run__service__pb2.ListRunsResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/ListTags',
+            tag_dot_v1_dot_tag__service__pb2.ListTagsRequest.SerializeToString,
+            tag_dot_v1_dot_tag__service__pb2.ListTagsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteRun(request,
+    def DeleteTag(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/DeleteRun',
-            muses_dot_v1_dot_run__service__pb2.DeleteRunRequest.SerializeToString,
-            muses_dot_v1_dot_run__service__pb2.DeleteRunResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/DeleteTag',
+            tag_dot_v1_dot_tag__service__pb2.DeleteTagRequest.SerializeToString,
+            tag_dot_v1_dot_tag__service__pb2.DeleteTagResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteRuns(request,
+    def DeleteTags(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/muses.v1.RunService/DeleteRuns',
-            muses_dot_v1_dot_run__service__pb2.DeleteRunsRequest.SerializeToString,
-            muses_dot_v1_dot_run__service__pb2.DeleteRunsResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/DeleteTags',
+            tag_dot_v1_dot_tag__service__pb2.DeleteTagsRequest.SerializeToString,
+            tag_dot_v1_dot_tag__service__pb2.DeleteTagsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/muses/v1/run_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/auth_pb2.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,31 +1,36 @@
 # -*- coding: utf-8 -*-
 # Generated by the protocol buffer compiler.  DO NOT EDIT!
-# source: tag/v1/tag.proto
+# source: thirdparty/kfpbackend/auth.proto
 """Generated protocol buffer code."""
 from google.protobuf.internal import builder as _builder
 from google.protobuf import descriptor as _descriptor
 from google.protobuf import descriptor_pool as _descriptor_pool
 from google.protobuf import symbol_database as _symbol_database
 # @@protoc_insertion_point(imports)
 
 _sym_db = _symbol_database.Default()
 
 
-from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
+from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
+from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
 
 
-DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10tag/v1/tag.proto\x12\x06tag.v1\x1a\x19google/api/resource.proto\"\x96\x02\n\x03Tag\x12\x0e\n\x02id\x18\x01 \x01(\x03R\x02id\x12\x1b\n\tcreate_at\x18\x02 \x01(\tR\x08\x63reateAt\x12\x1b\n\tupdate_at\x18\x03 \x01(\tR\x08updateAt\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12\x12\n\x04icon\x18\x05 \x01(\tR\x04icon\x12\x1d\n\nfont_color\x18\x06 \x01(\tR\tfontColor\x12!\n\x0cinherit_from\x18\x07 \x01(\x03R\x0binheritFrom\x12\'\n\x08\x63hildren\x18\x08 \x03(\x0b\x32\x0b.tag.v1.TagR\x08\x63hildren:2\xea\x41/\n\"github.com.artistml.apis/TagEntity\x12\ttags/{id}\"4\n\x0fTagOptionFilter\x12!\n\x0cinherit_from\x18\x01 \x01(\x03R\x0binheritFromB*Z(github.com/artistml/apis/go/tag/v1;tagv1b\x06proto3')
+DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n thirdparty/kfpbackend/auth.proto\x12\x15thirdparty.kfpbackend\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xb5\x02\n\x10\x41uthorizeRequest\x12\x1c\n\tnamespace\x18\x01 \x01(\tR\tnamespace\x12O\n\tresources\x18\x02 \x01(\x0e\x32\x31.thirdparty.kfpbackend.AuthorizeRequest.ResourcesR\tresources\x12@\n\x04verb\x18\x03 \x01(\x0e\x32,.thirdparty.kfpbackend.AuthorizeRequest.VerbR\x04verb\"2\n\tResources\x12\x18\n\x14UNASSIGNED_RESOURCES\x10\x00\x12\x0b\n\x07VIEWERS\x10\x01\"<\n\x04Verb\x12\x13\n\x0fUNASSIGNED_VERB\x10\x00\x12\n\n\x06\x43REATE\x10\x01\x12\x07\n\x03GET\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x32w\n\x0b\x41uthService\x12h\n\tAuthorize\x12\'.thirdparty.kfpbackend.AuthorizeRequest\x1a\x16.google.protobuf.Empty\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/apis/v1beta1/authB@Z>github.com/kubeflow/pipelines/backend/api/go_client;kfpbackendb\x06proto3')
 
 _builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
-_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tag.v1.tag_pb2', globals())
+_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thirdparty.kfpbackend.auth_pb2', globals())
 if _descriptor._USE_C_DESCRIPTORS == False:
 
   DESCRIPTOR._options = None
-  DESCRIPTOR._serialized_options = b'Z(github.com/artistml/apis/go/tag/v1;tagv1'
-  _TAG._options = None
-  _TAG._serialized_options = b'\352A/\n\"github.com.artistml.apis/TagEntity\022\ttags/{id}'
-  _TAG._serialized_start=56
-  _TAG._serialized_end=334
-  _TAGOPTIONFILTER._serialized_start=336
-  _TAGOPTIONFILTER._serialized_end=388
+  DESCRIPTOR._serialized_options = b'Z>github.com/kubeflow/pipelines/backend/api/go_client;kfpbackend'
+  _AUTHSERVICE.methods_by_name['Authorize']._options = None
+  _AUTHSERVICE.methods_by_name['Authorize']._serialized_options = b'\202\323\344\223\002\024\022\022/apis/v1beta1/auth'
+  _AUTHORIZEREQUEST._serialized_start=119
+  _AUTHORIZEREQUEST._serialized_end=428
+  _AUTHORIZEREQUEST_RESOURCES._serialized_start=316
+  _AUTHORIZEREQUEST_RESOURCES._serialized_end=366
+  _AUTHORIZEREQUEST_VERB._serialized_start=368
+  _AUTHORIZEREQUEST_VERB._serialized_end=428
+  _AUTHSERVICE._serialized_start=430
+  _AUTHSERVICE._serialized_end=549
 # @@protoc_insertion_point(module_scope)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/kfpbackend/job_pb2_grpc.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,303 +1,238 @@
 # Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
 """Client and server classes corresponding to protobuf-defined services."""
 import grpc
 
-from ...tag.v1 import tag_service_pb2 as tag_dot_v1_dot_tag__service__pb2
+from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
+from ...thirdparty.kfpbackend import job_pb2 as thirdparty_dot_kfpbackend_dot_job__pb2
 
 
-class TagServiceStub(object):
-    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
-    info: {
-    title: "Tag Service"
-    version: "1.0"
-    contact: {
-    name: "Tag Service"
-    url: "http://github.com/artistml/apis"
-    }
-    }
-    host: "github.com/artistml/apis"
-    base_path: "/tag/v1/tag"
-    schemes: HTTP
-    schemes: HTTPS
-    consumes: "application/json"
-    produces: "application/json"
-    external_docs: {
-    description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/tag/v1/tag"
-    }
-    };
-
-    The service that handles the CRUD of Tag.
-    """
+class JobServiceStub(object):
+    """Missing associated documentation comment in .proto file."""
 
     def __init__(self, channel):
         """Constructor.
 
         Args:
             channel: A grpc.Channel.
         """
-        self.CreateTag = channel.unary_unary(
-                '/tag.v1.TagService/CreateTag',
-                request_serializer=tag_dot_v1_dot_tag__service__pb2.CreateTagRequest.SerializeToString,
-                response_deserializer=tag_dot_v1_dot_tag__service__pb2.CreateTagResponse.FromString,
+        self.CreateJob = channel.unary_unary(
+                '/thirdparty.kfpbackend.JobService/CreateJob',
+                request_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.CreateJobRequest.SerializeToString,
+                response_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.Job.FromString,
                 )
-        self.GetTag = channel.unary_unary(
-                '/tag.v1.TagService/GetTag',
-                request_serializer=tag_dot_v1_dot_tag__service__pb2.GetTagRequest.SerializeToString,
-                response_deserializer=tag_dot_v1_dot_tag__service__pb2.GetTagResponse.FromString,
+        self.GetJob = channel.unary_unary(
+                '/thirdparty.kfpbackend.JobService/GetJob',
+                request_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.GetJobRequest.SerializeToString,
+                response_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.Job.FromString,
                 )
-        self.UpdateTag = channel.unary_unary(
-                '/tag.v1.TagService/UpdateTag',
-                request_serializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagRequest.SerializeToString,
-                response_deserializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagResponse.FromString,
+        self.ListJobs = channel.unary_unary(
+                '/thirdparty.kfpbackend.JobService/ListJobs',
+                request_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.ListJobsRequest.SerializeToString,
+                response_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.ListJobsResponse.FromString,
                 )
-        self.ListTags = channel.unary_unary(
-                '/tag.v1.TagService/ListTags',
-                request_serializer=tag_dot_v1_dot_tag__service__pb2.ListTagsRequest.SerializeToString,
-                response_deserializer=tag_dot_v1_dot_tag__service__pb2.ListTagsResponse.FromString,
+        self.EnableJob = channel.unary_unary(
+                '/thirdparty.kfpbackend.JobService/EnableJob',
+                request_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.EnableJobRequest.SerializeToString,
+                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                 )
-        self.DeleteTag = channel.unary_unary(
-                '/tag.v1.TagService/DeleteTag',
-                request_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagRequest.SerializeToString,
-                response_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagResponse.FromString,
+        self.DisableJob = channel.unary_unary(
+                '/thirdparty.kfpbackend.JobService/DisableJob',
+                request_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.DisableJobRequest.SerializeToString,
+                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                 )
-        self.DeleteTags = channel.unary_unary(
-                '/tag.v1.TagService/DeleteTags',
-                request_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsRequest.SerializeToString,
-                response_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsResponse.FromString,
+        self.DeleteJob = channel.unary_unary(
+                '/thirdparty.kfpbackend.JobService/DeleteJob',
+                request_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.DeleteJobRequest.SerializeToString,
+                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                 )
 
 
-class TagServiceServicer(object):
-    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
-    info: {
-    title: "Tag Service"
-    version: "1.0"
-    contact: {
-    name: "Tag Service"
-    url: "http://github.com/artistml/apis"
-    }
-    }
-    host: "github.com/artistml/apis"
-    base_path: "/tag/v1/tag"
-    schemes: HTTP
-    schemes: HTTPS
-    consumes: "application/json"
-    produces: "application/json"
-    external_docs: {
-    description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/tag/v1/tag"
-    }
-    };
+class JobServiceServicer(object):
+    """Missing associated documentation comment in .proto file."""
 
-    The service that handles the CRUD of Tag.
-    """
-
-    def CreateTag(self, request, context):
-        """Creates a Tag.
+    def CreateJob(self, request, context):
+        """Creates a new job.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def GetTag(self, request, context):
-        """Gets a Tag.
+    def GetJob(self, request, context):
+        """Finds a specific job by ID.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def UpdateTag(self, request, context):
-        """Updates a Tag.
+    def ListJobs(self, request, context):
+        """Finds all jobs.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def ListTags(self, request, context):
-        """Lists Tags in a Location.
+    def EnableJob(self, request, context):
+        """Restarts a job that was previously stopped. All runs associated with the job will continue.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteTag(self, request, context):
-        """Deletes a Tag.
+    def DisableJob(self, request, context):
+        """Stops a job and all its associated runs. The job is not deleted.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
-    def DeleteTags(self, request, context):
-        """Batch delete Tag by filter.
+    def DeleteJob(self, request, context):
+        """Deletes a job.
         """
         context.set_code(grpc.StatusCode.UNIMPLEMENTED)
         context.set_details('Method not implemented!')
         raise NotImplementedError('Method not implemented!')
 
 
-def add_TagServiceServicer_to_server(servicer, server):
+def add_JobServiceServicer_to_server(servicer, server):
     rpc_method_handlers = {
-            'CreateTag': grpc.unary_unary_rpc_method_handler(
-                    servicer.CreateTag,
-                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.CreateTagRequest.FromString,
-                    response_serializer=tag_dot_v1_dot_tag__service__pb2.CreateTagResponse.SerializeToString,
-            ),
-            'GetTag': grpc.unary_unary_rpc_method_handler(
-                    servicer.GetTag,
-                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.GetTagRequest.FromString,
-                    response_serializer=tag_dot_v1_dot_tag__service__pb2.GetTagResponse.SerializeToString,
-            ),
-            'UpdateTag': grpc.unary_unary_rpc_method_handler(
-                    servicer.UpdateTag,
-                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagRequest.FromString,
-                    response_serializer=tag_dot_v1_dot_tag__service__pb2.UpdateTagResponse.SerializeToString,
-            ),
-            'ListTags': grpc.unary_unary_rpc_method_handler(
-                    servicer.ListTags,
-                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.ListTagsRequest.FromString,
-                    response_serializer=tag_dot_v1_dot_tag__service__pb2.ListTagsResponse.SerializeToString,
-            ),
-            'DeleteTag': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteTag,
-                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagRequest.FromString,
-                    response_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagResponse.SerializeToString,
-            ),
-            'DeleteTags': grpc.unary_unary_rpc_method_handler(
-                    servicer.DeleteTags,
-                    request_deserializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsRequest.FromString,
-                    response_serializer=tag_dot_v1_dot_tag__service__pb2.DeleteTagsResponse.SerializeToString,
+            'CreateJob': grpc.unary_unary_rpc_method_handler(
+                    servicer.CreateJob,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.CreateJobRequest.FromString,
+                    response_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.Job.SerializeToString,
+            ),
+            'GetJob': grpc.unary_unary_rpc_method_handler(
+                    servicer.GetJob,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.GetJobRequest.FromString,
+                    response_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.Job.SerializeToString,
+            ),
+            'ListJobs': grpc.unary_unary_rpc_method_handler(
+                    servicer.ListJobs,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.ListJobsRequest.FromString,
+                    response_serializer=thirdparty_dot_kfpbackend_dot_job__pb2.ListJobsResponse.SerializeToString,
+            ),
+            'EnableJob': grpc.unary_unary_rpc_method_handler(
+                    servicer.EnableJob,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.EnableJobRequest.FromString,
+                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
+            ),
+            'DisableJob': grpc.unary_unary_rpc_method_handler(
+                    servicer.DisableJob,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.DisableJobRequest.FromString,
+                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
+            ),
+            'DeleteJob': grpc.unary_unary_rpc_method_handler(
+                    servicer.DeleteJob,
+                    request_deserializer=thirdparty_dot_kfpbackend_dot_job__pb2.DeleteJobRequest.FromString,
+                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
             ),
     }
     generic_handler = grpc.method_handlers_generic_handler(
-            'tag.v1.TagService', rpc_method_handlers)
+            'thirdparty.kfpbackend.JobService', rpc_method_handlers)
     server.add_generic_rpc_handlers((generic_handler,))
 
 
  # This class is part of an EXPERIMENTAL API.
-class TagService(object):
-    """option (grpc.gateway.protoc_gen_swagger.options.openapiv2_swagger) = {
-    info: {
-    title: "Tag Service"
-    version: "1.0"
-    contact: {
-    name: "Tag Service"
-    url: "http://github.com/artistml/apis"
-    }
-    }
-    host: "github.com/artistml/apis"
-    base_path: "/tag/v1/tag"
-    schemes: HTTP
-    schemes: HTTPS
-    consumes: "application/json"
-    produces: "application/json"
-    external_docs: {
-    description: "API specification in Markdown",
-    url: "http://github.com/artistml/apis/tag/v1/tag"
-    }
-    };
-
-    The service that handles the CRUD of Tag.
-    """
+class JobService(object):
+    """Missing associated documentation comment in .proto file."""
 
     @staticmethod
-    def CreateTag(request,
+    def CreateJob(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/CreateTag',
-            tag_dot_v1_dot_tag__service__pb2.CreateTagRequest.SerializeToString,
-            tag_dot_v1_dot_tag__service__pb2.CreateTagResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.JobService/CreateJob',
+            thirdparty_dot_kfpbackend_dot_job__pb2.CreateJobRequest.SerializeToString,
+            thirdparty_dot_kfpbackend_dot_job__pb2.Job.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def GetTag(request,
+    def GetJob(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/GetTag',
-            tag_dot_v1_dot_tag__service__pb2.GetTagRequest.SerializeToString,
-            tag_dot_v1_dot_tag__service__pb2.GetTagResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.JobService/GetJob',
+            thirdparty_dot_kfpbackend_dot_job__pb2.GetJobRequest.SerializeToString,
+            thirdparty_dot_kfpbackend_dot_job__pb2.Job.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def UpdateTag(request,
+    def ListJobs(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/UpdateTag',
-            tag_dot_v1_dot_tag__service__pb2.UpdateTagRequest.SerializeToString,
-            tag_dot_v1_dot_tag__service__pb2.UpdateTagResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.JobService/ListJobs',
+            thirdparty_dot_kfpbackend_dot_job__pb2.ListJobsRequest.SerializeToString,
+            thirdparty_dot_kfpbackend_dot_job__pb2.ListJobsResponse.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def ListTags(request,
+    def EnableJob(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/ListTags',
-            tag_dot_v1_dot_tag__service__pb2.ListTagsRequest.SerializeToString,
-            tag_dot_v1_dot_tag__service__pb2.ListTagsResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.JobService/EnableJob',
+            thirdparty_dot_kfpbackend_dot_job__pb2.EnableJobRequest.SerializeToString,
+            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteTag(request,
+    def DisableJob(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/DeleteTag',
-            tag_dot_v1_dot_tag__service__pb2.DeleteTagRequest.SerializeToString,
-            tag_dot_v1_dot_tag__service__pb2.DeleteTagResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.JobService/DisableJob',
+            thirdparty_dot_kfpbackend_dot_job__pb2.DisableJobRequest.SerializeToString,
+            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
 
     @staticmethod
-    def DeleteTags(request,
+    def DeleteJob(request,
             target,
             options=(),
             channel_credentials=None,
             call_credentials=None,
             insecure=False,
             compression=None,
             wait_for_ready=None,
             timeout=None,
             metadata=None):
-        return grpc.experimental.unary_unary(request, target, '/tag.v1.TagService/DeleteTags',
-            tag_dot_v1_dot_tag__service__pb2.DeleteTagsRequest.SerializeToString,
-            tag_dot_v1_dot_tag__service__pb2.DeleteTagsResponse.FromString,
+        return grpc.experimental.unary_unary(request, target, '/thirdparty.kfpbackend.JobService/DeleteJob',
+            thirdparty_dot_kfpbackend_dot_job__pb2.DeleteJobRequest.SerializeToString,
+            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
             options, channel_credentials,
             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/tag/v1/tag_service_pb2_grpc.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/chat_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/chat_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/chat_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/chat_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/hello_pb2.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/hello_pb2.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/apis/thirdparty/greeting/hello_pb2.pyi` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/apis/thirdparty/greeting/hello_pb2.pyi`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/echo.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/echo.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/muses.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/muses.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import tempfile
 from typing import Callable
+from typing import Final
 
-# import kfp_server_api
-from google.protobuf.struct_pb2 import Struct
+from kfp import compiler
+from kfp import components
 
 from ..apis.common.v1.types_pb2 import CommonFilter
 from ..apis.common.v1.types_pb2 import CommonOption
 from ..apis.muses.v1.component_pb2 import Component
 from ..apis.muses.v1.component_pb2 import ComponentOptionFilter
 from ..apis.muses.v1.component_service_pb2 import CreateComponentRequest
 from ..apis.muses.v1.component_service_pb2 import CreateComponentResponse
@@ -42,51 +43,35 @@
 from ..apis.muses.v1.method_service_pb2 import CreateMethodResponse
 from ..apis.muses.v1.method_service_pb2 import DeleteMethodRequest
 from ..apis.muses.v1.method_service_pb2 import DeleteMethodResponse
 from ..apis.muses.v1.method_service_pb2 import ListMethodsRequest
 from ..apis.muses.v1.method_service_pb2 import ListMethodsResponse
 from ..apis.muses.v1.method_service_pb2 import UpdateMethodRequest
 from ..apis.muses.v1.method_service_pb2 import UpdateMethodResponse
-from ..apis.muses.v1.run_pb2 import Run
-from ..apis.muses.v1.run_pb2 import RunOptionFilter
-from ..apis.muses.v1.run_service_pb2 import CreateRunRequest
-from ..apis.muses.v1.run_service_pb2 import CreateRunResponse
-from ..apis.muses.v1.run_service_pb2 import DeleteRunRequest
-from ..apis.muses.v1.run_service_pb2 import DeleteRunResponse
-from ..apis.muses.v1.run_service_pb2 import DeleteRunsResponse
-from ..apis.muses.v1.run_service_pb2 import GetRunRequest
-from ..apis.muses.v1.run_service_pb2 import GetRunResponse
-from ..apis.muses.v1.run_service_pb2 import ListRunsRequest
-from ..apis.muses.v1.run_service_pb2 import ListRunsResponse
-from ..apis.muses.v1.run_service_pb2 import UpdateRunRequest
-from ..apis.muses.v1.run_service_pb2 import UpdateRunResponse
-
-# from ..gateway import kfp_client
+from ..apis.thirdparty.kfpapi.pipeline_spec_pb2 import ComponentSpec
+from ..apis.thirdparty.kfpapi.pipeline_spec_pb2 import PipelineDeploymentConfig
+from ..apis.thirdparty.kfpapi.pipeline_spec_pb2 import PipelineSpec
 from ..gateway import muses_client
 from ..gateway import try_request_grpc
 from ..lib import convert_message
 from ..lib import read_message
-from ..lib import write_message
-
-# from kfp import compiler
-# from kfp import components
 
-# _cmplr: Final[compiler.Compiler] = compiler.Compiler()
+_cmplr: Final[compiler.Compiler] = compiler.Compiler()
 
 
 class MusesClient:
 
     @property
     def _stub(self):
+        """
+        The function returns the client object
+        :return: The client object
+        """
         return muses_client
 
-    @property
-    def _kfp_client(self):
-        return kfp_client
-
     @try_request_grpc
     def create_component(
         self,
         component: Component,
     ) -> CreateComponentResponse:
         request: CreateComponentRequest = CreateComponentRequest(
             component=component, )
@@ -95,47 +80,47 @@
     def create_component_from_file(
         self,
         yaml_path: str,
     ) -> CreateComponentResponse:
         component: Component = read_message(yaml_path, Component)
         return self.create_component(component=component)
 
-    # def create_component_from_function(
-    #     self,
-    #     func: Callable,
-    # ) -> CreateComponentResponse:
-    #     _, filepath = tempfile.mkstemp(suffix=".yaml")
-    #     _cmplr.compile(
-    #         func,
-    #         package_path=filepath,
-    #     )
-    #     return self.create_component_from_kfp_file(yaml_path=filepath)
-
-    # @try_request_grpc
-    # def create_component_from_kfp_file(
-    #     self,
-    #     yaml_path: str,
-    # ) -> CreateComponentResponse:
-    #     component_spec = components.load_component_from_file(
-    #         yaml_path).component_spec
-    #     name = component_spec.name
-    #     pipe_spec: Struct = read_message(yaml_path, Struct)
-    #     component = pipe_spec.components[
-    #         pipe_spec.root.dag.tasks[name].component_ref.name]
-    #     exec_spec: Struct = convert_message(
-    #         pipe_spec.deployment_spec["executors"][component.executor_label],
-    #         Struct,
-    #     )
-    #     request: CreateComponentRequest = CreateComponentRequest(
-    #         component=Component(
-    #             name=name,
-    #             component=component,
-    #             executor_spec=exec_spec,
-    #         ), )
-    #     return self._stub.component.CreateComponent(request)
+    def create_component_from_function(
+        self,
+        func: Callable,
+    ) -> CreateComponentResponse:
+        _, filepath = tempfile.mkstemp(suffix=".yaml")
+        _cmplr.compile(
+            func,
+            package_path=filepath,
+        )
+        return self.create_component_from_kfp_file(yaml_path=filepath)
+
+    @try_request_grpc
+    def create_component_from_kfp_file(
+        self,
+        yaml_path: str,
+    ) -> CreateComponentResponse:
+        component_spec = components.load_component_from_file(
+            yaml_path).component_spec
+        name = component_spec.name
+        pipe_spec: PipelineSpec = read_message(yaml_path, PipelineSpec)
+        component = pipe_spec.components[
+            pipe_spec.root.dag.tasks[name].component_ref.name]
+        exec_spec: PipelineDeploymentConfig.ExecutorSpec = convert_message(
+            pipe_spec.deployment_spec["executors"][component.executor_label],
+            PipelineDeploymentConfig.ExecutorSpec,
+        )
+        request: CreateComponentRequest = CreateComponentRequest(
+            component=Component(
+                name=name,
+                component=component,
+                executor_spec=exec_spec,
+            ), )
+        return self._stub.component.CreateComponent(request)
 
     @try_request_grpc
     def get_component(
         self,
         id: int,
     ) -> GetComponentResponse:
         return self._stub.component.GetComponent(GetComponentRequest(id=id), )
@@ -236,62 +221,49 @@
     def create_flow_from_file(
         self,
         yaml_path: str,
     ) -> CreateFlowResponse:
         flow: Flow = read_message(yaml_path, Flow)
         return self.create_flow(flow=flow)
 
-    # def create_flow_from_function(
-    #     self,
-    #     func: Callable,
-    # ) -> CreateFlowResponse:
-    #     _, filepath = tempfile.mkstemp(suffix=".yaml")
-    #     _cmplr.compile(
-    #         func,
-    #         package_path=filepath,
-    #     )
-    #     return self.create_flow_from_kfp_file(yaml_path=filepath)
+    def create_flow_from_function(
+        self,
+        func: Callable,
+    ) -> CreateFlowResponse:
+        _, filepath = tempfile.mkstemp(suffix=".yaml")
+        _cmplr.compile(
+            func,
+            package_path=filepath,
+        )
+        return self.create_flow_from_kfp_file(yaml_path=filepath)
 
     @try_request_grpc
     def create_flow_from_kfp_file(
         self,
         yaml_path: str,
     ) -> CreateFlowResponse:
-        pipe_spec: Struct = read_message(yaml_path, Struct)
-        deploy_config: Struct = convert_message(
+        pipe_spec: PipelineSpec = read_message(yaml_path, PipelineSpec)
+        deploy_config: PipelineDeploymentConfig = convert_message(
             pipe_spec.deployment_spec,
-            Struct,
+            PipelineDeploymentConfig,
         )
         comps = []
         parameters = []
-        for param_name, parameter_spec in pipe_spec.root.input_definitions.parameters.items(
-        ):
-            # 添加全局参数
-            parameters.append(
-                Parameter(
-                    parameter=ComponentParameter(
-                        node_id="",
-                        param_name=param_name,
-                    ),
-                    parameter_spec=parameter_spec,
-                ), )
         for comp_name, comp in pipe_spec.root.dag.tasks.items():
             for param_name, param in comp.inputs.parameters.items():
                 if param.component_input_parameter:
                     # 直接从flow传递的参数
                     parameters.append(
                         Parameter(
                             parameter=ComponentParameter(
                                 node_id=comp_name,
                                 param_name=param_name,
                             ),
-                            parent_parameter=ComponentParameter(
-                                node_id="",
-                                param_name=param.component_input_parameter,
-                            ),
+                            parameter_spec=pipe_spec.root.input_definitions.
+                            parameters[param.component_input_parameter],
                         ), )
                     continue
                 if param.task_output_parameter:
                     parameters.append(
                         Parameter(
                             parameter=ComponentParameter(
                                 node_id=comp_name,
@@ -301,35 +273,31 @@
                                 node_id=param.task_output_parameter.
                                 producer_task,
                                 param_name=param.task_output_parameter.
                                 output_parameter_key,
                             ),
                         ), )
 
-            component_spec: Struct = pipe_spec.components[
+            component_spec: ComponentSpec = pipe_spec.components[
                 comp.component_ref.name]
-            executor_spec: Struct = deploy_config.executors[
+            executor_spec: PipelineDeploymentConfig.ExecutorSpec = deploy_config.executors[
                 component_spec.executor_label]
             comps.append(
                 self.create_component(
                     Component(name=comp_name,
                               component=component_spec,
                               executor_spec=executor_spec,
                               node_id=comp_name)).details)
 
-        flow = Flow(
+        request: CreateFlowRequest = CreateFlowRequest(flow=Flow(
             name=pipe_spec.pipeline_info.name,
             parameters=parameters,
             components={c.node_id: c
                         for c in comps},
-        )
-        _, filepath = tempfile.mkstemp(suffix=".yaml")
-        write_message(flow, filepath)
-        write_message(flow, "local/flow.yaml")
-        request: CreateFlowRequest = CreateFlowRequest(flow=flow, )
+        ), )
         return self._stub.flow.CreateFlow(request)
 
     @try_request_grpc
     def get_flow(
         self,
         id: int,
     ) -> GetFlowResponse:
@@ -370,126 +338,7 @@
         option_filter: FlowOptionFilter = None,
     ) -> DeleteFlowsResponse:
         return self._stub.flow.DeleteFlows(
             DeleteFlowsRequest(
                 common_filter=common_filter,
                 option_filter=option_filter,
             ), )
-
-    @try_request_grpc
-    def create_run(
-        self,
-        run: Run,
-    ) -> CreateRunResponse:
-        return self._stub.run.CreateRun(CreateRunRequest(run=run, ), )
-
-    @try_request_grpc
-    def create_run_from_file(
-        self,
-        yaml_path: str,
-        trigger: Struct,
-        pipeline_spec: Struct,
-        experiment: str,
-        namespace: str,
-    ) -> CreateRunResponse:
-        resp = self.create_flow_from_file(yaml_path=yaml_path)
-        return self.create_run(run=Run(
-            flow_id=resp.details.id,
-            trigger=trigger,
-            pipeline_spec=pipeline_spec,
-            experiment=experiment,
-            namespace=namespace,
-        ))
-
-    @try_request_grpc
-    def create_run_from_function(
-        self,
-        func: Callable,
-        trigger: Struct,
-        pipeline_spec: Struct,
-        experiment: str,
-        namespace: str,
-    ) -> CreateRunResponse:
-        resp = self.create_flow_from_function(func=func)
-        return self.create_run(run=Run(
-            flow_id=resp.details.id,
-            trigger=trigger,
-            pipeline_spec=pipeline_spec,
-            experiment=experiment,
-            namespace=namespace,
-        ))
-
-    @try_request_grpc
-    def create_run_from_kfp_file(
-        self,
-        yaml_path: str,
-        trigger: Struct,
-        pipeline_spec: Struct,
-        experiment: str,
-        namespace: str,
-    ) -> CreateRunResponse:
-        resp = self.create_flow_from_kfp_file(yaml_path)
-        return self.create_run(run=Run(
-            flow_id=resp.details.id,
-            trigger=trigger,
-            pipeline_spec=pipeline_spec,
-            experiment=experiment,
-            namespace=namespace,
-        ))
-
-    @try_request_grpc
-    def get_run(
-        self,
-        id: int,
-    ) -> GetRunResponse:
-        return self._stub.run.GetRun(GetRunRequest(id=id, ), )
-
-    @try_request_grpc
-    def update_run(
-        self,
-        run: Run,
-    ) -> UpdateRunResponse:
-        return self._stub.run.UpdateRun(UpdateRunRequest(run=run, ), )
-
-    @try_request_grpc
-    def delete_run(
-        self,
-        id: int,
-    ) -> DeleteRunResponse:
-        return self._stub.run.DeleteRun(DeleteRunRequest(id=id, ), )
-
-    @try_request_grpc
-    def list_runs(
-        self,
-        common_option: CommonOption,
-        common_filter: CommonFilter,
-        option_filter: RunOptionFilter,
-    ) -> ListRunsResponse:
-        return self._stub.run.ListRuns(
-            ListRunsRequest(
-                common_filter=common_filter,
-                common_option=common_option,
-                option_filter=option_filter,
-            ), )
-
-    @try_request_grpc
-    def delete_runs(
-        self,
-        option_filter: RunOptionFilter,
-        common_filter: CommonFilter,
-    ) -> DeleteRunsResponse:
-        return self._stub.run.DeleteRuns(
-            DeleteRunRequest(
-                common_filter=common_filter,
-                option_filter=option_filter,
-            ), )
-
-    # @try_request_grpc
-    # def get_run_result(
-    #     self,
-    #     run_id: str,
-    #     timeout: int,
-    # ) -> kfp_server_api.ApiRun:
-    #     return self._kfp_client.api_client.wait_for_run_completion(
-    #         run_id=run_id,
-    #         timeout=timeout,
-    #     )
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/clients/tag.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/clients/tag.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/__init__.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/__init__.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,32 +1,30 @@
+'''
+Author: ksice ksice.xt@gmail.com
+Date: 2022-12-12 10:35:30
+LastEditors: ksice ksice.xt@gmail.com
+LastEditTime: 2022-12-12 11:26:48
+FilePath: /artistml/artistml-sdk/artistml_sdk/gateway/__init__.py
+Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
+'''
 from typing import Final
 
 from ._core import Error
 from ._core import GrpcClient
 from ._core import RPCResponseError
 from ._core import try_request_grpc
-
-# from ._grpc_clients._kfp import KfpClient
-from ._grpc_clients.argo import ArgoClient
-from ._grpc_clients.assoc import AssocClient
 from ._grpc_clients.echo import EchoClient
 from ._grpc_clients.muses import MusesClient
 from ._grpc_clients.tag import TagClient
 
 echo_client: Final[EchoClient] = EchoClient()
 muses_client: Final[MusesClient] = MusesClient()
 tag_client: Final[TagClient] = TagClient()
-assoc_client: Final[AssocClient] = AssocClient()
-# kfp_client: Final[KfpClient] = KfpClient()
-argo_client: Final[ArgoClient] = ArgoClient()
 __all__ = [
     "GrpcClient",
     "Error",
     "RPCResponseError",
     "try_request_grpc",
     "echo_client",
     "muses_client",
     "tag_client",
-    "assoc_client",
-    # "kfp_client",
-    "argo_client",
 ]
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/grpc_channel.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/grpc_channel.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/grpc_client.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/grpc_client.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_core/grpc_invoke_wrapper.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_core/grpc_invoke_wrapper.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/gateway/_grpc_clients/muses.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/gateway/_grpc_clients/muses.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,15 +1,15 @@
+"""client for AutomlServer"""
 from __future__ import annotations
 
 from typing import final
 
 from ...apis.muses.v1.component_service_pb2_grpc import ComponentServiceStub
 from ...apis.muses.v1.flow_service_pb2_grpc import FlowServiceStub
 from ...apis.muses.v1.method_service_pb2_grpc import MethodServiceStub
-from ...apis.muses.v1.run_service_pb2_grpc import RunServiceStub
 from .._core import GrpcClient
 
 
 @final
 class MusesClient(GrpcClient):
 
     def __init__(self):
@@ -22,11 +22,7 @@
     @property
     def method(self) -> MethodServiceStub:
         return self._stub(MethodServiceStub)
 
     @property
     def flow(self) -> FlowServiceStub:
         return self._stub(FlowServiceStub)
-
-    @property
-    def run(self) -> RunServiceStub:
-        return self._stub(RunServiceStub)
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/lib/_protobuf_message.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/lib/_protobuf_message.py`

 * *Files 10% similar despite different names*

```diff
@@ -6,34 +6,24 @@
 from ._yaml import load_yaml
 from ._yaml import write_yaml
 
 
 def read_message(
     yaml_path: str, message_type: Type[google.protobuf.message.Message]
 ) -> google.protobuf.message.Message:
-    return json_format.ParseDict(
-        load_yaml(yaml_path),
-        message_type(),
-    )
+    return json_format.ParseDict(load_yaml(yaml_path), message_type())
 
 
 def write_message(message: google.protobuf.message.Message, yaml_path: str):
     write_yaml(
-        json_format.MessageToDict(
-            message,
-            preserving_proto_field_name=True,
-        ),
-        yaml_path,
-    )
+        json_format.MessageToDict(message, preserving_proto_field_name=True),
+        yaml_path)
 
 
 def convert_message(
     src_message: google.protobuf.message.Message,
     tar_type: Type[google.protobuf.message.Message]
 ) -> google.protobuf.message.Message:
     return json_format.ParseDict(
-        json_format.MessageToDict(
-            src_message,
-            preserving_proto_field_name=True,
-        ),
-        tar_type(),
-    )
+        json_format.MessageToDict(src_message,
+                                  preserving_proto_field_name=True),
+        tar_type())
```

### Comparing `artistml-sdk-0.2.1.dev9296519/artistml_sdk/logger/logger.py` & `artistml-sdk-0.2.1.dev9751808/artistml_sdk/logger/logger.py`

 * *Files identical despite different names*

### Comparing `artistml-sdk-0.2.1.dev9296519/pyproject.toml` & `artistml-sdk-0.2.1.dev9751808/pyproject.toml`

 * *Files 22% similar despite different names*

```diff
@@ -3,16 +3,79 @@
     { name = "pypi", url = "https://pypi.tuna.tsinghua.edu.cn/simple", verify_ssl = false },
 ]
 includes = [
     "artistml_sdk",
     "artistml_sdk/**/*",
 ]
 
-[tool.pdm.resolution.overrides]
-pyyaml = "<7,>=6"
+[tool.pdm.dev-dependencies]
+artistml_sdk = [
+    "pytest>=7.2.0",
+    "autoflake>=2.0.0",
+    "isort>=5.11.1",
+    "yapf>=0.32.0",
+    "coverage[toml]<6.4",
+    "setuptools-scm>=6.4.2",
+    "pytest-cov<3.0.0,>=2.12.1",
+    "googleapis-common-protos==1.56.0",
+    "grpcio==1.46.0",
+    "typing-extensions==4.2.0",
+    "protoc-gen-swagger>=0.1.0",
+    "protoc-gen-validate==0.9.0",
+    "grpcio-tools==1.46.0",
+    "certifi==2021.10.8",
+    "protobuf==3.20.1",
+    "psutil>=5.9.4",
+    "pyyaml==5.4.1",
+    "kfp==2.0.0-beta.1",
+    "google>=3.0.0",
+    "absl-py==1.0.0",
+    "attrs==21.4.0",
+    "cachetools==5.0.0",
+    "charset-normalizer==2.0.12",
+    "click==8.1.3",
+    "cloudpickle==2.0.0",
+    "deprecated==1.2.13",
+    "docstring-parser==0.14.1",
+    "fire==0.4.0",
+    "google-api-core==2.7.3",
+    "google-auth==2.6.6",
+    "google-cloud-core==2.3.0",
+    "google-cloud-storage==2.3.0",
+    "google-crc32c==1.3.0",
+    "google-resumable-media==2.3.2",
+    "idna==3.3",
+    "importlib-metadata>=4.11.4",
+    "jsonschema==3.2.0",
+    "kfp-pipeline-spec==0.1.14",
+    "kfp-server-api==2.0.0a2",
+    "oauthlib==3.2.0",
+    "pyasn1==0.4.8",
+    "pyasn1-modules==0.2.8",
+    "pyrsistent==0.18.1",
+    "python-dateutil==2.8.2",
+    "requests==2.27.1",
+    "requests-oauthlib==1.3.1",
+    "requests-toolbelt==0.9.1",
+    "rsa==4.8",
+    "six==1.16.0",
+    "strip-hints==0.1.10",
+    "tabulate==0.8.9",
+    "termcolor==1.1.0",
+    "typer==0.4.1",
+    "uritemplate==3.0.1",
+    "urllib3==1.26.9",
+    "websocket-client==1.3.2",
+    "wheel==0.37.1",
+    "wrapt==1.14.1",
+    "zipp==3.8.0",
+    "kubernetes==18.20.0",
+    "packaging==21.3",
+    "Jinja2<2.12,>=2.11",
+]
 
 [tool.pdm.version]
 source = "file"
 path = "scm_version.toml"
 
 [tool.setuptools.packages.find]
 where = [
@@ -79,33 +142,20 @@
 [project]
 name = "artistml-sdk"
 dynamic = []
 description = ""
 authors = [
     { name = "sylvan", email = "sylvan2future@gmail.com" },
 ]
-dependencies = [
-    "pytest>=7.2.0",
-    "autoflake>=2.0.0",
-    "isort>=5.11.1",
-    "yapf>=0.32.0",
-    "coverage[toml]<6.4",
-    "setuptools-scm>=6.4.2",
-    "pytest-cov<3.0.0,>=2.12.1",
-    "mlflow>=1.30.0",
-    "argo-workflows==6.3.0rc2",
-    "grpcio>=1.51.3",
-    "psutil>=5.9.4",
-    "google-api-core>=2.11.0",
-]
-requires-python = ">=3.8.1,<4.0"
+dependencies = []
+requires-python = ">=3.8"
 readme = "README.md"
-version = "0.2.1.dev9296519"
+version = "0.2.1.dev9751808"
 
 [project.license]
 text = "ArtistML"
 
 [build-system]
 requires = [
-    "pdm-pep517<=1.0.6",
+    "pdm-pep517>=1.0",
 ]
 build-backend = "pdm.pep517.api"
```

