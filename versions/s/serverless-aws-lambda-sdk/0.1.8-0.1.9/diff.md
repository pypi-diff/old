# Comparing `tmp/serverless-aws-lambda-sdk-0.1.8.tar.gz` & `tmp/serverless-aws-lambda-sdk-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/console/console/python/packages/dist/.tmp-nsm0n0iw/serverless-aws-lambda-sdk-0.1.8.tar", last modified: Thu Mar 16 09:52:39 2023, max compression
+gzip compressed data, was "/home/runner/work/console/console/python/packages/dist/.tmp-qkqvef4t/serverless-aws-lambda-sdk-0.1.9.tar", last modified: Mon Mar 20 13:46:39 2023, max compression
```

## Comparing `serverless-aws-lambda-sdk-0.1.8.tar` & `serverless-aws-lambda-sdk-0.1.9.tar`

### file list

```diff
@@ -1,33 +1,34 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      688 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1034 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/
--rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      814 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/instrument/
--rw-r--r--   0 runner    (1001) docker     (123)     6561 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/instrument/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/instrument/lib/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/instrument/lib/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5177 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/base.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      225 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/exec_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     2361 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/wrapper.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/trace_spans/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/trace_spans/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1264 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/trace_spans/aws_lambda.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      954 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:52:39.000000 serverless-aws-lambda-sdk-0.1.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/tests/test_assertions.py
--rw-r--r--   0 runner    (1001) docker     (123)     6385 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/tests/test_instrument.py
--rw-r--r--   0 runner    (1001) docker     (123)     6610 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/tests/test_internal_extension.py
--rw-r--r--   0 runner    (1001) docker     (123)     5629 2023-03-16 09:52:16.000000 serverless-aws-lambda-sdk-0.1.8/tests/test_internal_extension_wrapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      688 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1034 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/
+-rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      814 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/instrument/
+-rw-r--r--   0 runner    (1001) docker     (123)     7962 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/instrument/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/instrument/lib/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/instrument/lib/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5142 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/base.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      647 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/exec_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2293 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/wrapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/trace_spans/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/trace_spans/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1264 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/trace_spans/aws_lambda.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1255 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1000 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-20 13:46:39.000000 serverless-aws-lambda-sdk-0.1.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1768 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/tests/test_assertions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8710 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/tests/test_instrument.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6596 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/tests/test_internal_extension.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/tests/test_internal_extension_exec_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5559 2023-03-20 13:46:19.000000 serverless-aws-lambda-sdk-0.1.9/tests/test_internal_extension_wrapper.py
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/PKG-INFO` & `serverless-aws-lambda-sdk-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: serverless-aws-lambda-sdk
-Version: 0.1.8
+Version: 0.1.9
 Summary: Serverless AWS Lambda SDK for Python
 Author: serverlessinc
 Project-URL: changelog, https://github.com/serverless/console/blob/main/python/packages/aws-lambda-sdk/CHANGELOG.md
 Project-URL: documentation, https://github.com/serverless/console/tree/main/python/packages/aws-lambda-sdk
 Project-URL: homepage, https://www.serverless.com/console
 Project-URL: repository, https://github.com/serverless/console
 Requires-Python: >=3.7
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/README.md` & `serverless-aws-lambda-sdk-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `serverless-aws-lambda-sdk-0.1.8/pyproject.toml` & `serverless-aws-lambda-sdk-0.1.9/pyproject.toml`

 * *Files 10% similar despite different names*

```diff
@@ -3,22 +3,22 @@
 requires = [
     "setuptools>=65.6.3",
     "wheel>=0.38.4",
 ]
 
 [project]
 name = "serverless-aws-lambda-sdk"
-version = "0.1.8"
+version = "0.1.9"
 description = "Serverless AWS Lambda SDK for Python"
 readme = "README.md"
 authors = [{ name = "serverlessinc" }]
 requires-python = ">=3.7"
 dependencies = [
-    "serverless-sdk~=0.3.0",
-    "serverless-sdk-schema~=0.1.0",
+    "serverless-sdk~=0.3.3",
+    "serverless-sdk-schema~=0.1.1",
     "strenum~=0.4",
     "typing-extensions~=4.5", # included in Python 3.8 - 3.11
 ]
 [project.optional-dependencies]
 tests = [
     "black>=22.12",
     "pytest>=7.2",
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/__init__.py` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/__init__.py`

 * *Files identical despite different names*

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/base.py` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/base.py`

 * *Files identical despite different names*

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/instrument/__init__.py` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/instrument/__init__.py`

 * *Files 17% similar despite different names*

```diff
@@ -1,28 +1,27 @@
 from __future__ import annotations
 import os
 import time
+import sys
 import json
 from functools import wraps
 from typing import List, Optional, Any
-import logging
 from typing_extensions import Final
-
+import random
 from .. import serverlessSdk
 from ..base import Handler
 from ..trace_spans.aws_lambda import reset as reset_aws_lambda_span
 from serverless_sdk_schema import TracePayload
+from serverless_sdk.lib.trace import TraceSpan
 import base64
 
 
-logger = logging.getLogger(__name__)
-
-
 def debug_log(msg):
-    return logger.debug(f"⚡ SDK: {msg}")
+    if serverlessSdk._is_debug_mode:
+        print(f"⚡ SDK: {msg}", file=sys.stderr)
 
 
 __all__: Final[List[str]] = [
     "instrument",
 ]
 
 
@@ -80,35 +79,72 @@
                 + "or pass it with the options\n"
             )
         serverlessSdk.trace_spans.aws_lambda_initialization.close()
 
     def _captured_event_handler(self, captured_event):
         serverlessSdk._captured_events.append(captured_event)
 
-    def _report_trace(self):
+    def _report_trace(self, is_error_outcome: bool):
+        is_sampled_out = (
+            (not is_error_outcome)
+            and (not serverlessSdk._is_debug_mode)
+            and (not serverlessSdk._is_dev_mode)
+            and (
+                not [
+                    e
+                    for e in serverlessSdk._captured_events
+                    if e.name
+                    in [
+                        "telemetry.error.generated.v1",
+                        "telemetry.warning.generated.v1",
+                    ]
+                ]
+            )
+            and random.random() > 0.2
+        )
+
+        def _map_span(span: TraceSpan) -> Optional[TraceSpan]:
+            nonlocal is_sampled_out
+            core_trace_span_names = [
+                "aws.lambda",
+                "aws.lambda.initialization",
+                "aws.lambda.invocation",
+            ]
+            if is_sampled_out and span.name not in core_trace_span_names:
+                return None
+            span_payload = span.to_protobuf_dict()
+            del span_payload["input"]
+            del span_payload["output"]
+            return span_payload
+
         payload_dct = {
+            "isSampledOut": is_sampled_out or None,
             "slsTags": {
                 "orgId": serverlessSdk.org_id,
                 "service": os.environ.get("AWS_LAMBDA_FUNCTION_NAME", None),
                 "sdk": {
                     "name": serverlessSdk.name,
                     "version": serverlessSdk.version,
                 },
             },
-            "spans": [s.to_protobuf_dict() for s in self.aws_lambda.spans],
-            "events": [e.to_protobuf_dict() for e in serverlessSdk._captured_events],
-            "customTags": json.dumps(serverlessSdk._custom_tags),
+            "spans": [s for s in map(_map_span, self.aws_lambda.spans) if s],
+            "events": [e.to_protobuf_dict() for e in serverlessSdk._captured_events]
+            if not is_sampled_out
+            else [],
+            "customTags": json.dumps(serverlessSdk._custom_tags)
+            if not is_sampled_out
+            else None,
         }
         payload = _get_payload(payload_dct)
         print(
             f"SERVERLESS_TELEMETRY.T.{base64.b64encode(payload.SerializeToString()).decode('utf-8')}"
         )
 
     def _close_trace(self, outcome: str, outcomeResult: Optional[Any] = None):
-        self.isRootSpanReset = False
+        self.is_root_span_reset = False
         try:
             end_time = time.perf_counter_ns()
             is_error_outcome = outcome.startswith("error:")
 
             self.aws_lambda.tags["aws.lambda.outcome"] = _resolve_outcome_enum_value(
                 outcome
             )
@@ -123,32 +159,34 @@
                 )
 
             if serverlessSdk.trace_spans.aws_lambda_invocation:
                 serverlessSdk.trace_spans.aws_lambda_invocation.close(end_time=end_time)
 
             self.aws_lambda.close(end_time=end_time)
 
-            self._report_trace()
+            self._report_trace(is_error_outcome)
             self._clear_root_span()
             debug_log(
                 "Overhead duration: Internal response:"
                 + f"{int((time.perf_counter_ns() - end_time) / 1000_000)}ms"
             )
 
-        except Exception:
-            logging.exception("Error while closing the trace.")
+        except Exception as ex:
+            serverlessSdk._report_error(ex)
+            if not self.is_root_span_reset:
+                self._clear_root_span()
 
     def _clear_root_span(self):
         reset_aws_lambda_span()
         del self.aws_lambda.id
         del self.aws_lambda.trace_id
         del self.aws_lambda.end_time
         serverlessSdk._captured_events = []
         serverlessSdk._custom_tags.clear()
-        self.isRootSpanReset = True
+        self.is_root_span_reset = True
 
     def instrument(self, user_handler: Handler) -> Handler:
         @wraps(user_handler)
         def stub(event, context):
             request_start_time = time.perf_counter_ns()
             self.current_invocation_id += 1
             try:
@@ -162,16 +200,16 @@
                         "aws.lambda.invocation", start_time=request_start_time
                     )
                 )
 
                 diff = int((time.perf_counter_ns() - request_start_time) / 1000_000)
                 debug_log("Overhead duration: Internal request:" + f"{diff}ms")
 
-            except Exception:
-                logger.exception("Unhandled exception during instrumentation.")
+            except Exception as ex:
+                serverlessSdk._report_error(ex)
                 return user_handler(event, context)
 
             # Invocation of customer code
             try:
                 result = user_handler(event, context)
                 self._close_trace("success", result)
                 return result
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/base.py` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/base.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 from __future__ import annotations
-import logging
 from os import environ
 from pathlib import Path
 from typing import Optional, Tuple
 from importlib import import_module
 import sys
 import time
 
@@ -38,27 +37,22 @@
 HANDLER: Final[Optional[str]] = environ.get(Env.HANDLER)
 
 # The directory that contains the function code.
 LAMBDA_TASK_ROOT: Final[Optional[str]] = environ.get(Env.LAMBDA_TASK_ROOT)
 
 # Serverless env vars
 SLS_ORG_ID: Final[Optional[str]] = environ.get(Env.SLS_ORG_ID)
-SLS_SDK_DEBUG: Final[Optional[str]] = environ.get(Env.SLS_SDK_DEBUG)
+_is_debug_mode: Final[bool] = bool(environ.get(Env.SLS_SDK_DEBUG))
 
 DEFAULT_TASK_ROOT: Final[str] = "/var/task"
 
 
-logger = logging.getLogger(__name__)
-
-if SLS_SDK_DEBUG:
-    logger.setLevel(logging.DEBUG)
-
-
 def debug_log(msg):
-    return logger.debug(f"⚡ SDK: {msg}")
+    if _is_debug_mode:
+        print(f"⚡ SDK: {msg}", file=sys.stderr)
 
 
 def initialize(handler: Optional[str] = HANDLER):
     """Checks handler is an importable function, inits env variables for the handler.
 
     If handler is not importable, or it is not a callable function,
     returns immediately. In that case, env variables are not modified and
@@ -71,18 +65,19 @@
         process_start_time = time.perf_counter_ns()
         environ[Env.PROCESS_START_TIME] = str(process_start_time)
 
         # AWS Lambda Python runtime converts forward slashes to dots.
         handler = handler.replace("/", ".")
 
         if not SLS_ORG_ID:
-            logger.error(
+            print(
                 "Serverless SDK Warning: "
                 "Cannot instrument function: "
                 'Missing "SLS_ORG_ID" environment variable',
+                file=sys.stderr,
             )
             return
 
         debug_log("Wrapper initialization")
 
         task_root = Path(LAMBDA_TASK_ROOT).resolve()
         if not task_root.exists():
@@ -139,12 +134,13 @@
         environ[Env.HANDLER] = NEW_HANDLER
 
         end = time.perf_counter_ns()
         ms = round((end - process_start_time) / NS_IN_MS)
 
         debug_log(f"Overhead duration: Internal initialization: {ms}ms")
     except Exception:
-        logger.exception(
+        print(
             "Fatal Serverless SDK Error: "
             "Please report at https://github.com/serverless/console/issues: "
-            "Internal extension setup failed."
+            "Internal extension setup failed.",
+            file=sys.stderr,
         )
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/internal_extension/wrapper.py` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/internal_extension/wrapper.py`

 * *Files 5% similar despite different names*

```diff
@@ -56,16 +56,15 @@
         from .. import serverlessSdk
 
         sdk = serverlessSdk
 
     try:
         sdk._initialize()
     except Exception as ex:
-        # TODO: call _reportError on sdk
-        logging.error(ex)
+        sdk._report_error(ex)
 
     return sdk
 
 
 def _check_original_handler_and_reset_vars() -> str:
     origin = environ.get(Env.ORIGIN_HANDLER)
 
@@ -79,19 +78,18 @@
         raise HandlerNotFound(f"{Env.HANDLER} is not set.")
 
 
 def _get_instrumented_handler() -> Handler:
     _check_original_handler_and_reset_vars()
 
     handler = _get_handler_function()
-    _get_sdk()
+    sdk = _get_sdk()
 
     try:
         instrumenter = Instrumenter()
         return instrumenter.instrument(handler)
     except Exception as ex:
-        # TODO: call _reportError on sdk
-        logging.error(ex)
+        sdk._report_error(ex)
         return handler
 
 
 handler: Final[Handler] = _get_instrumented_handler()
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk/trace_spans/aws_lambda.py` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk/trace_spans/aws_lambda.py`

 * *Files identical despite different names*

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/PKG-INFO` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: serverless-aws-lambda-sdk
-Version: 0.1.8
+Version: 0.1.9
 Summary: Serverless AWS Lambda SDK for Python
 Author: serverlessinc
 Project-URL: changelog, https://github.com/serverless/console/blob/main/python/packages/aws-lambda-sdk/CHANGELOG.md
 Project-URL: documentation, https://github.com/serverless/console/tree/main/python/packages/aws-lambda-sdk
 Project-URL: homepage, https://www.serverless.com/console
 Project-URL: repository, https://github.com/serverless/console
 Requires-Python: >=3.7
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/serverless_aws_lambda_sdk.egg-info/SOURCES.txt` & `serverless-aws-lambda-sdk-0.1.9/serverless_aws_lambda_sdk.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -17,8 +17,9 @@
 serverless_aws_lambda_sdk/internal_extension/exec_wrapper.py
 serverless_aws_lambda_sdk/internal_extension/wrapper.py
 serverless_aws_lambda_sdk/trace_spans/__init__.py
 serverless_aws_lambda_sdk/trace_spans/aws_lambda.py
 tests/test_assertions.py
 tests/test_instrument.py
 tests/test_internal_extension.py
+tests/test_internal_extension_exec_wrapper.py
 tests/test_internal_extension_wrapper.py
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/tests/test_assertions.py` & `serverless-aws-lambda-sdk-0.1.9/tests/test_assertions.py`

 * *Files identical despite different names*

### Comparing `serverless-aws-lambda-sdk-0.1.8/tests/test_internal_extension.py` & `serverless-aws-lambda-sdk-0.1.9/tests/test_internal_extension.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,8 @@
 from __future__ import annotations
-import pytest
 import os
 
 from typing_extensions import Final
 from pathlib import Path
 
 import importlib
```

### Comparing `serverless-aws-lambda-sdk-0.1.8/tests/test_internal_extension_wrapper.py` & `serverless-aws-lambda-sdk-0.1.9/tests/test_internal_extension_wrapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,15 +20,14 @@
 
 HANDLER_MODULE_DIR: Final[str] = str(Path(__file__).parent.resolve())
 
 
 def test_raises_exception_when_handler_is_not_set(reset_sdk):
     # given
     from serverless_aws_lambda_sdk.exceptions import HandlerNotFound
-    from serverless_aws_lambda_sdk.internal_extension.base import Env
 
     env = dict(os.environ)
     reset_sdk.setattr(os, "environ", env)
 
     # when
     with pytest.raises(HandlerNotFound):
         from serverless_aws_lambda_sdk.internal_extension import wrapper
```

