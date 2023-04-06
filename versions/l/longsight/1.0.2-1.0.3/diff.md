# Comparing `tmp/longsight-1.0.2.tar.gz` & `tmp/longsight-1.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "longsight-1.0.2.tar", last modified: Mon Apr  3 09:28:36 2023, max compression
+gzip compressed data, was "longsight-1.0.3.tar", last modified: Thu Apr  6 09:56:32 2023, max compression
```

## Comparing `longsight-1.0.2.tar` & `longsight-1.0.3.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-03 09:28:36.429096 longsight-1.0.2/
--rw-rw-r--   0 martin    (1000) martin    (1000)     1054 2023-01-26 10:26:21.000000 longsight-1.0.2/LICENSE.md
--rw-rw-r--   0 martin    (1000) martin    (1000)     7377 2023-04-03 09:28:36.429096 longsight-1.0.2/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)     5506 2023-03-31 16:08:22.000000 longsight-1.0.2/README.md
--rw-rw-r--   0 martin    (1000) martin    (1000)     1028 2023-04-03 09:28:29.000000 longsight-1.0.2/pyproject.toml
--rw-rw-r--   0 martin    (1000) martin    (1000)     1010 2023-04-03 09:28:36.429096 longsight-1.0.2/setup.cfg
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-03 09:28:36.429096 longsight-1.0.2/src/
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-03 09:28:36.429096 longsight-1.0.2/src/longsight/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-03-29 16:56:16.000000 longsight-1.0.2/src/longsight/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    10334 2023-04-03 09:27:50.000000 longsight-1.0.2/src/longsight/instrumentation.py
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-03 09:28:36.429096 longsight-1.0.2/src/longsight.egg-info/
--rw-rw-r--   0 martin    (1000) martin    (1000)     7377 2023-04-03 09:28:36.000000 longsight-1.0.2/src/longsight.egg-info/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)      318 2023-04-03 09:28:36.000000 longsight-1.0.2/src/longsight.egg-info/SOURCES.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-03 09:28:36.000000 longsight-1.0.2/src/longsight.egg-info/dependency_links.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)      130 2023-04-03 09:28:36.000000 longsight-1.0.2/src/longsight.egg-info/requires.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)       10 2023-04-03 09:28:36.000000 longsight-1.0.2/src/longsight.egg-info/top_level.txt
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-03 09:28:36.429096 longsight-1.0.2/tests/
--rw-rw-r--   0 martin    (1000) martin    (1000)     6998 2023-03-31 15:41:47.000000 longsight-1.0.2/tests/test_instrumentation.py
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 09:56:32.645798 longsight-1.0.3/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1054 2023-01-26 10:26:21.000000 longsight-1.0.3/LICENSE.md
+-rw-rw-r--   0 martin    (1000) martin    (1000)     7876 2023-04-06 09:56:32.645798 longsight-1.0.3/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)     6005 2023-04-06 09:56:07.000000 longsight-1.0.3/README.md
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1028 2023-04-06 09:23:32.000000 longsight-1.0.3/pyproject.toml
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1010 2023-04-06 09:56:32.645798 longsight-1.0.3/setup.cfg
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 09:56:32.645798 longsight-1.0.3/src/
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 09:56:32.645798 longsight-1.0.3/src/longsight/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-03-29 16:56:16.000000 longsight-1.0.3/src/longsight/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    11959 2023-04-06 09:50:50.000000 longsight-1.0.3/src/longsight/instrumentation.py
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 09:56:32.645798 longsight-1.0.3/src/longsight.egg-info/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     7876 2023-04-06 09:56:32.000000 longsight-1.0.3/src/longsight.egg-info/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)      318 2023-04-06 09:56:32.000000 longsight-1.0.3/src/longsight.egg-info/SOURCES.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 09:56:32.000000 longsight-1.0.3/src/longsight.egg-info/dependency_links.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)      130 2023-04-06 09:56:32.000000 longsight-1.0.3/src/longsight.egg-info/requires.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)       10 2023-04-06 09:56:32.000000 longsight-1.0.3/src/longsight.egg-info/top_level.txt
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 09:56:32.645798 longsight-1.0.3/tests/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     6998 2023-03-31 15:41:47.000000 longsight-1.0.3/tests/test_instrumentation.py
```

### Comparing `longsight-1.0.2/LICENSE.md` & `longsight-1.0.3/LICENSE.md`

 * *Files identical despite different names*

### Comparing `longsight-1.0.2/PKG-INFO` & `longsight-1.0.3/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: longsight
-Version: 1.0.2
+Version: 1.0.3
 Summary: This library implements a range of common logging functions.
 Home-page: https://gitlab.com/crossref/labs/distrunner
 Author: Martin Paul Eve
 Author-email: meve@crossref.org
 Maintainer-email: Martin Paul Eve <meve@crossref.org>
 License: Copyright &copy; 2023 Crossref
         
@@ -56,22 +56,35 @@
     
     @router.get("/path")
     @instrument()
     async def a_route(request: Request, instrumentation):
         instrumentation.logger.info("Hello, World!")
         return {"message": "Hello, World!"}
 
-Alternatively, you can also log to CloudWatch instead of locally (note also that the decorator works on both async and synchronous functions):
+Alternatively, you can also log to CloudWatch instead of locally from any function (note also that the decorator works on both async and synchronous functions and is _not_ limited to FastAPI functions):
 
     from longsight.instrumentation import instrument
 
-    @instrument(cloudwatch_push=True)
-    def a_function(instrumentation):
+    @instrumentation.instrument(
+    cloudwatch_push=True,
+    log_stream_name="martin-test-stream-name",
+    log_group_name="martin-test-group-name",
+    namespace="martin-test-namespace",
+    )
+    def a_function(instrumentation, log_stream_name="martin-test-stream-name",
+    log_group_name="martin-test-group-name",):
         instrumentation.logger.info("Hello, World!")
-        return
+        instrumentation.logger.info("A second log line")
+        instrumentation.add_metric_point(
+            metric_name="test_metric",
+            dimensions=[{"Name": "Environment", "Value": "Production"}],
+            metric_value=1,
+            unit="Count",
+            time_stamp=datetime.now(),
+        )
 
 Longsight can also create AWS objects for you to reuse throughout your project, centralizing AWS code:
 
     from longsight.instrumentation import instrument
 
     @instrument(create_aws=True, bucket="my-bucket")
     def a_function(instrumentation):
@@ -114,28 +127,27 @@
 
 This setup is done automatically if you use the decorators.
 
 ## Context Managers
 The Instrumentation context manager provides functionality for instrumenting routes with metrics and logging. To use the context manager, create an instance of the Instrumentation class and use it as a context manager:
 
     from fastapi import FastAPI
-    from longsight.instrumentation import Instrumentation, Metrics, Logger
+    from longsight.instrumentation import Instrumentation
     
     app = FastAPI()
     
     @app.get("/")
     async def root(request: Request):
         with Instrumentation(
                         aws_connector=aws_connector,
                         fastapi_app=fastapi_app,
                         request=request) as instrumentation:
             instrumentation.logger.info("Handling request")
-            instrumentation.metrics.put_metric("RequestCount", 1)
             return {"message": "Hello, World!"}
 
-The Instrumentation context manager automatically logs the start and end of the request, and provides an instance of the Logger and Metrics classes for logging and metrics. The Logger and Metrics classes are provided by the aws_lambda_powertools package.
+The Instrumentation context manager automatically logs the start and end of the request, and provides an instance of the Logger classes for logging and metrics. The Logger classes are provided by the aws_lambda_powertools package.
 
 # Credits
 * [.gitignore](https://github.com/github/gitignore) from Github.
 * [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/2.10.0/) by Amazon.
 
 &copy; Crossref 2023
```

### Comparing `longsight-1.0.2/README.md` & `longsight-1.0.3/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -30,22 +30,35 @@
     
     @router.get("/path")
     @instrument()
     async def a_route(request: Request, instrumentation):
         instrumentation.logger.info("Hello, World!")
         return {"message": "Hello, World!"}
 
-Alternatively, you can also log to CloudWatch instead of locally (note also that the decorator works on both async and synchronous functions):
+Alternatively, you can also log to CloudWatch instead of locally from any function (note also that the decorator works on both async and synchronous functions and is _not_ limited to FastAPI functions):
 
     from longsight.instrumentation import instrument
 
-    @instrument(cloudwatch_push=True)
-    def a_function(instrumentation):
+    @instrumentation.instrument(
+    cloudwatch_push=True,
+    log_stream_name="martin-test-stream-name",
+    log_group_name="martin-test-group-name",
+    namespace="martin-test-namespace",
+    )
+    def a_function(instrumentation, log_stream_name="martin-test-stream-name",
+    log_group_name="martin-test-group-name",):
         instrumentation.logger.info("Hello, World!")
-        return
+        instrumentation.logger.info("A second log line")
+        instrumentation.add_metric_point(
+            metric_name="test_metric",
+            dimensions=[{"Name": "Environment", "Value": "Production"}],
+            metric_value=1,
+            unit="Count",
+            time_stamp=datetime.now(),
+        )
 
 Longsight can also create AWS objects for you to reuse throughout your project, centralizing AWS code:
 
     from longsight.instrumentation import instrument
 
     @instrument(create_aws=True, bucket="my-bucket")
     def a_function(instrumentation):
@@ -88,28 +101,27 @@
 
 This setup is done automatically if you use the decorators.
 
 ## Context Managers
 The Instrumentation context manager provides functionality for instrumenting routes with metrics and logging. To use the context manager, create an instance of the Instrumentation class and use it as a context manager:
 
     from fastapi import FastAPI
-    from longsight.instrumentation import Instrumentation, Metrics, Logger
+    from longsight.instrumentation import Instrumentation
     
     app = FastAPI()
     
     @app.get("/")
     async def root(request: Request):
         with Instrumentation(
                         aws_connector=aws_connector,
                         fastapi_app=fastapi_app,
                         request=request) as instrumentation:
             instrumentation.logger.info("Handling request")
-            instrumentation.metrics.put_metric("RequestCount", 1)
             return {"message": "Hello, World!"}
 
-The Instrumentation context manager automatically logs the start and end of the request, and provides an instance of the Logger and Metrics classes for logging and metrics. The Logger and Metrics classes are provided by the aws_lambda_powertools package.
+The Instrumentation context manager automatically logs the start and end of the request, and provides an instance of the Logger classes for logging and metrics. The Logger classes are provided by the aws_lambda_powertools package.
 
 # Credits
 * [.gitignore](https://github.com/github/gitignore) from Github.
 * [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/2.10.0/) by Amazon.
 
 &copy; Crossref 2023
```

### Comparing `longsight-1.0.2/pyproject.toml` & `longsight-1.0.3/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "longsight"
-version = "1.0.2"
+version = "1.0.3"
 description = "This library implements a range of common logging functions."
 readme = "README.md"
 requires-python = ">=3.8"
 license = {file = "LICENSE.md"}
 keywords = ["distributed computing"]
 authors = [
   {email = "meve@crossref.org"},
```

### Comparing `longsight-1.0.2/setup.cfg` & `longsight-1.0.3/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = longsight
-version = 1.0.2
+version = 1.0.3
 description = This library implements a range of common logging functions.
 url = https://gitlab.com/crossref/labs/distrunner
 author = Martin Paul Eve
 author_email = meve@crossref.org
 license = MIT
 classifiers = 
 	Intended Audience :: Developers
```

### Comparing `longsight-1.0.2/src/longsight/instrumentation.py` & `longsight-1.0.3/src/longsight/instrumentation.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,13 @@
 import functools
 import inspect
 import logging
 from contextlib import AbstractContextManager, contextmanager
 from contextvars import ContextVar
+from datetime import datetime
 from logging import LogRecord
 from types import TracebackType
 from typing import Callable
 from typing import Optional
 from typing import Type
 from uuid import uuid4
 
@@ -22,39 +23,28 @@
 
 
 correlation_id: ContextVar[Optional[str]] = ContextVar(
     "correlation_id", default=None
 )
 
 logger: Logger = Logger()
-metrics: Metrics = Metrics(namespace="default")
 
 
 class LoggerRouteHandler(APIRoute):
     def get_route_handler(self) -> Callable:
         original_route_handler = super().get_route_handler()
 
         async def route_handler(request: Request) -> Response:
             ctx = {
                 "path": request.url.path,
                 "route": self.path,
                 "method": request.method,
             }
             logger.append_keys(fastapi=ctx)
 
-            with single_metric(
-                name="RequestCount",
-                unit=MetricUnit.Count,
-                value=1,
-                namespace=metrics.namespace,
-            ) as metric:
-                metric.add_dimension(
-                    name="route", value=f"{request.method} {self.path}"
-                )
-
             return await original_route_handler(request)
 
         return route_handler
 
 
 class CorrelationIdFilter(logging.Filter):
     """Logging filter to attach correlation IDs to log records"""
@@ -133,24 +123,26 @@
 
 def instrument(
     bucket: str = "",
     create_aws=False,
     cloudwatch_push=False,
     log_group_name: str = "",
     log_stream_name: str = "",
+    namespace: str = "namespace",
 ):
     """
     This is a decorator that will instrument a method and provide AWS access
     if desired.
     :param bucket: the bucket for the AWSClient to use.
     :param create_aws: whether to create an AWSClient
     :param cloudwatch_push: whether to push metrics to CloudWatch. Note that
     setting this to true will create an AWSClient
     :param log_group_name: the log group name to use for the logger
     :param log_stream_name: the log stream name to use for the logger
+    :param namespace: the namespace to use for the metrics
     :return: the wrapped function
     """
 
     def wrap(f):
         @contextmanager
         def wrapping_logic(*args, **kwargs):
             from claws import aws_utils
@@ -173,14 +165,15 @@
             with Instrumentation(
                 aws_connector=aws_connector,
                 fastapi_app=fastapi_app,
                 request=fastapi_request,
                 cloudwatch_push=cloudwatch_push,
                 log_group_name=log_group_name,
                 log_stream_name=log_stream_name,
+                namespace=namespace,
             ) as metric_logger:
                 if hasattr(aws_context, "aws_request_id"):
                     metric_logger.logger.info(
                         f"Set correlation ID to AWS "
                         f"requestId: {aws_context.aws_request_id}"
                     )
 
@@ -227,35 +220,86 @@
         __exc_value: BaseException,
         __traceback: TracebackType,
     ) -> bool:
         if __exc_value:
             self.logger.error(f"Request shutdown with error: {__exc_value}.")
             raise __exc_value
 
+        try:
+            if len(self._metrics) > 0 and self._cloudwatch_push:
+                self._aws_connector.cloudwatch_client.put_metric_data(
+                    Namespace=self._namespace, MetricData=self._metrics
+                )
+                self.logger.info(
+                    f"Pushed {len(self._metrics)} custom "
+                    f"metrics to CloudWatch"
+                )
+            elif not self._cloudwatch_push:
+                self.logger.info("Not pushing metrics to CloudWatch")
+            else:
+                self.logger.info("No metrics to push to CloudWatch")
+        except Exception as e:
+            self.logger.warning(
+                f"Failed to send metrics to CloudWatch ({e}): {self._metrics}"
+            )
+
         return True
 
+    def add_metric_point(
+        self,
+        metric_name: str,
+        dimensions: list[dict],
+        time_stamp: datetime,
+        metric_value: int,
+        unit: str,
+    ):
+        """
+        Add a metric point to the list of metrics to send to CloudWatch.
+        :param metric_name: the name of the metric
+        :param dimensions: associated dimensions
+        :param time_stamp: the timestamp of the metric point
+        :param metric_value: the value of the metric point
+        :param unit: the unit of the metric point
+        :return: None
+        """
+
+        # documentation for how we build this can be found at:
+        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/put_metric_data.html
+        MetricData = {
+            "MetricName": metric_name,
+            "Timestamp": time_stamp,
+            "Value": metric_value,
+            "Unit": unit,
+            "StorageResolution": 60,  # one or 60
+        }
+
+        if dimensions:
+            MetricData["Dimensions"] = dimensions
+
+        self._metrics.append(MetricData)
+
     def __init__(
         self,
         aws_connector: aws_utils.AWSConnector = None,
         namespace: str = "LabsAPI",
         fastapi_app=None,
         request: Request = None,
         cloudwatch_push: bool = False,
         log_group_name: str = "",
         log_stream_name: str = "",
     ):
-        metrics.namespace = namespace
+        self._metrics = []
         self._aws_connector = aws_connector
         self._namespace = namespace
         self._app = fastapi_app
         self._log_group_name = log_group_name
         self._log_stream_name = log_stream_name
+        self._cloudwatch_push = cloudwatch_push
 
         self._logger: Logger = logger
-        self._metrics: Metrics = metrics
         self._tracer: Tracer = Tracer()
 
         self._logger.addFilter(CorrelationIdFilter())
 
         if self._aws_connector:
             self._aws_connector.instrumentation = self
```

### Comparing `longsight-1.0.2/src/longsight.egg-info/PKG-INFO` & `longsight-1.0.3/src/longsight.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: longsight
-Version: 1.0.2
+Version: 1.0.3
 Summary: This library implements a range of common logging functions.
 Home-page: https://gitlab.com/crossref/labs/distrunner
 Author: Martin Paul Eve
 Author-email: meve@crossref.org
 Maintainer-email: Martin Paul Eve <meve@crossref.org>
 License: Copyright &copy; 2023 Crossref
         
@@ -56,22 +56,35 @@
     
     @router.get("/path")
     @instrument()
     async def a_route(request: Request, instrumentation):
         instrumentation.logger.info("Hello, World!")
         return {"message": "Hello, World!"}
 
-Alternatively, you can also log to CloudWatch instead of locally (note also that the decorator works on both async and synchronous functions):
+Alternatively, you can also log to CloudWatch instead of locally from any function (note also that the decorator works on both async and synchronous functions and is _not_ limited to FastAPI functions):
 
     from longsight.instrumentation import instrument
 
-    @instrument(cloudwatch_push=True)
-    def a_function(instrumentation):
+    @instrumentation.instrument(
+    cloudwatch_push=True,
+    log_stream_name="martin-test-stream-name",
+    log_group_name="martin-test-group-name",
+    namespace="martin-test-namespace",
+    )
+    def a_function(instrumentation, log_stream_name="martin-test-stream-name",
+    log_group_name="martin-test-group-name",):
         instrumentation.logger.info("Hello, World!")
-        return
+        instrumentation.logger.info("A second log line")
+        instrumentation.add_metric_point(
+            metric_name="test_metric",
+            dimensions=[{"Name": "Environment", "Value": "Production"}],
+            metric_value=1,
+            unit="Count",
+            time_stamp=datetime.now(),
+        )
 
 Longsight can also create AWS objects for you to reuse throughout your project, centralizing AWS code:
 
     from longsight.instrumentation import instrument
 
     @instrument(create_aws=True, bucket="my-bucket")
     def a_function(instrumentation):
@@ -114,28 +127,27 @@
 
 This setup is done automatically if you use the decorators.
 
 ## Context Managers
 The Instrumentation context manager provides functionality for instrumenting routes with metrics and logging. To use the context manager, create an instance of the Instrumentation class and use it as a context manager:
 
     from fastapi import FastAPI
-    from longsight.instrumentation import Instrumentation, Metrics, Logger
+    from longsight.instrumentation import Instrumentation
     
     app = FastAPI()
     
     @app.get("/")
     async def root(request: Request):
         with Instrumentation(
                         aws_connector=aws_connector,
                         fastapi_app=fastapi_app,
                         request=request) as instrumentation:
             instrumentation.logger.info("Handling request")
-            instrumentation.metrics.put_metric("RequestCount", 1)
             return {"message": "Hello, World!"}
 
-The Instrumentation context manager automatically logs the start and end of the request, and provides an instance of the Logger and Metrics classes for logging and metrics. The Logger and Metrics classes are provided by the aws_lambda_powertools package.
+The Instrumentation context manager automatically logs the start and end of the request, and provides an instance of the Logger classes for logging and metrics. The Logger classes are provided by the aws_lambda_powertools package.
 
 # Credits
 * [.gitignore](https://github.com/github/gitignore) from Github.
 * [AWS Lambda Powertools](https://awslabs.github.io/aws-lambda-powertools-python/2.10.0/) by Amazon.
 
 &copy; Crossref 2023
```

### Comparing `longsight-1.0.2/tests/test_instrumentation.py` & `longsight-1.0.3/tests/test_instrumentation.py`

 * *Files identical despite different names*

