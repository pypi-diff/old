# Comparing `tmp/pepperize.cdk-route53-health-check-0.0.98.tar.gz` & `tmp/pepperize.cdk-route53-health-check-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pepperize.cdk-route53-health-check-0.0.98.tar", last modified: Tue Dec  6 12:31:57 2022, max compression
+gzip compressed data, was "pepperize.cdk-route53-health-check-0.0.99.tar", last modified: Tue Dec  6 12:37:55 2022, max compression
```

## Comparing `pepperize.cdk-route53-health-check-0.0.98.tar` & `pepperize.cdk-route53-health-check-0.0.99.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:31:57.884089 pepperize.cdk-route53-health-check-0.0.98/
--rw-r--r--   0 runner    (1001) docker     (123)     1078 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     9466 2022-12-06 12:31:57.884089 pepperize.cdk-route53-health-check-0.0.98/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     8430 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-06 12:31:57.884089 pepperize.cdk-route53-health-check-0.0.98/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1951 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:31:57.880089 pepperize.cdk-route53-health-check-0.0.98/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:31:57.884089 pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     9466 2022-12-06 12:31:57.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      604 2022-12-06 12:31:57.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 12:31:57.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-06 12:31:57.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2022-12-06 12:31:57.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:31:57.884089 pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/
--rw-r--r--   0 runner    (1001) docker     (123)   115150 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:31:57.884089 pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/_jsii/
--rw-r--r--   0 runner    (1001) docker     (123)      441 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/_jsii/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)   228564 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/_jsii/cdk-route53-health-check@0.0.98.jsii.tgz
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 12:31:45.000000 pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:37:55.949994 pepperize.cdk-route53-health-check-0.0.99/
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     9466 2022-12-06 12:37:55.949994 pepperize.cdk-route53-health-check-0.0.99/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     8430 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2022-12-06 12:37:55.949994 pepperize.cdk-route53-health-check-0.0.99/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1951 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:37:55.945994 pepperize.cdk-route53-health-check-0.0.99/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:37:55.949994 pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     9466 2022-12-06 12:37:55.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      604 2022-12-06 12:37:55.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 12:37:55.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      111 2022-12-06 12:37:55.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2022-12-06 12:37:55.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:37:55.949994 pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/
+-rw-r--r--   0 runner    (1001) docker     (123)   119102 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-06 12:37:55.949994 pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/_jsii/
+-rw-r--r--   0 runner    (1001) docker     (123)      441 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/_jsii/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)   228564 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/_jsii/cdk-route53-health-check@0.0.99.jsii.tgz
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-06 12:37:33.000000 pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/py.typed
```

### Comparing `pepperize.cdk-route53-health-check-0.0.98/LICENSE` & `pepperize.cdk-route53-health-check-0.0.99/LICENSE`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-route53-health-check-0.0.98/PKG-INFO` & `pepperize.cdk-route53-health-check-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-route53-health-check
-Version: 0.0.98
+Version: 0.0.99
 Summary: Create Route53 HealthChecks to monitor TCP, HTTP, HTTPS endpoints, CloudWatch Alarms and other Route53 HealthChecks.
 Home-page: https://github.com/pepperize/cdk-route53-health-check.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-route53-health-check.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-route53-health-check-0.0.98/README.md` & `pepperize.cdk-route53-health-check-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `pepperize.cdk-route53-health-check-0.0.98/setup.py` & `pepperize.cdk-route53-health-check-0.0.99/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import json
 import setuptools
 
 kwargs = json.loads(
     """
 {
     "name": "pepperize.cdk-route53-health-check",
-    "version": "0.0.98",
+    "version": "0.0.99",
     "description": "Create Route53 HealthChecks to monitor TCP, HTTP, HTTPS endpoints, CloudWatch Alarms and other Route53 HealthChecks.",
     "license": "MIT",
     "url": "https://github.com/pepperize/cdk-route53-health-check.git",
     "long_description_content_type": "text/markdown",
     "author": "Patrick Florek<patrick.florek@gmail.com>",
     "bdist_wheel": {
         "universal": true
@@ -22,15 +22,15 @@
     },
     "packages": [
         "pepperize_cdk_route53_health_check",
         "pepperize_cdk_route53_health_check._jsii"
     ],
     "package_data": {
         "pepperize_cdk_route53_health_check._jsii": [
-            "cdk-route53-health-check@0.0.98.jsii.tgz"
+            "cdk-route53-health-check@0.0.99.jsii.tgz"
         ],
         "pepperize_cdk_route53_health_check": [
             "py.typed"
         ]
     },
     "python_requires": "~=3.7",
     "install_requires": [
```

### Comparing `pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/PKG-INFO` & `pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pepperize.cdk-route53-health-check
-Version: 0.0.98
+Version: 0.0.99
 Summary: Create Route53 HealthChecks to monitor TCP, HTTP, HTTPS endpoints, CloudWatch Alarms and other Route53 HealthChecks.
 Home-page: https://github.com/pepperize/cdk-route53-health-check.git
 Author: Patrick Florek<patrick.florek@gmail.com>
 License: MIT
 Project-URL: Source, https://github.com/pepperize/cdk-route53-health-check.git
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `pepperize.cdk-route53-health-check-0.0.98/src/pepperize.cdk_route53_health_check.egg-info/SOURCES.txt` & `pepperize.cdk-route53-health-check-0.0.99/src/pepperize.cdk_route53_health_check.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -7,8 +7,8 @@
 src/pepperize.cdk_route53_health_check.egg-info/SOURCES.txt
 src/pepperize.cdk_route53_health_check.egg-info/dependency_links.txt
 src/pepperize.cdk_route53_health_check.egg-info/requires.txt
 src/pepperize.cdk_route53_health_check.egg-info/top_level.txt
 src/pepperize_cdk_route53_health_check/__init__.py
 src/pepperize_cdk_route53_health_check/py.typed
 src/pepperize_cdk_route53_health_check/_jsii/__init__.py
-src/pepperize_cdk_route53_health_check/_jsii/cdk-route53-health-check@0.0.98.jsii.tgz
+src/pepperize_cdk_route53_health_check/_jsii/cdk-route53-health-check@0.0.99.jsii.tgz
```

### Comparing `pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/__init__.py` & `pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -212,18 +212,18 @@
 import publication
 import typing_extensions
 
 from typeguard import check_type
 
 from ._jsii import *
 
-import aws_cdk
-import aws_cdk.aws_cloudwatch
-import aws_cdk.aws_route53
-import constructs
+import aws_cdk as _aws_cdk_ceddda9d
+import aws_cdk.aws_cloudwatch as _aws_cdk_aws_cloudwatch_ceddda9d
+import aws_cdk.aws_route53 as _aws_cdk_aws_route53_ceddda9d
+import constructs as _constructs_77d1e7e8
 
 
 @jsii.data_type(
     jsii_type="@pepperize/cdk-route53-health-check.AlarmHealthCheckProps",
     jsii_struct_bases=[],
     name_mapping={
         "alarm": "alarm",
@@ -232,55 +232,47 @@
         "inverted": "inverted",
     },
 )
 class AlarmHealthCheckProps:
     def __init__(
         self,
         *,
-        alarm: aws_cdk.aws_cloudwatch.IAlarm,
+        alarm: _aws_cdk_aws_cloudwatch_ceddda9d.IAlarm,
         health_check_name: typing.Optional[builtins.str] = None,
         insufficient_data_health_status: typing.Optional["InsufficientDataHealthStatus"] = None,
         inverted: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''
         :param alarm: The alarm that Route53 monitors.
         :param health_check_name: The display name of this Route53 HealthCheck.
         :param insufficient_data_health_status: The status to assign to the HealthCheck when CloudWatch has insufficient data about the metric.
         :param inverted: Whether to invert the status of the Route53 health check status.
         '''
         if __debug__:
-            def stub(
-                *,
-                alarm: aws_cdk.aws_cloudwatch.IAlarm,
-                health_check_name: typing.Optional[builtins.str] = None,
-                insufficient_data_health_status: typing.Optional[InsufficientDataHealthStatus] = None,
-                inverted: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__639153b296f45bd8c248c52158a6493c4845bdb55b7de3975f909413a7b84ae2)
             check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
             check_type(argname="argument health_check_name", value=health_check_name, expected_type=type_hints["health_check_name"])
             check_type(argname="argument insufficient_data_health_status", value=insufficient_data_health_status, expected_type=type_hints["insufficient_data_health_status"])
             check_type(argname="argument inverted", value=inverted, expected_type=type_hints["inverted"])
-        self._values: typing.Dict[str, typing.Any] = {
+        self._values: typing.Dict[builtins.str, typing.Any] = {
             "alarm": alarm,
         }
         if health_check_name is not None:
             self._values["health_check_name"] = health_check_name
         if insufficient_data_health_status is not None:
             self._values["insufficient_data_health_status"] = insufficient_data_health_status
         if inverted is not None:
             self._values["inverted"] = inverted
 
     @builtins.property
-    def alarm(self) -> aws_cdk.aws_cloudwatch.IAlarm:
+    def alarm(self) -> _aws_cdk_aws_cloudwatch_ceddda9d.IAlarm:
         '''The alarm that Route53 monitors.'''
         result = self._values.get("alarm")
         assert result is not None, "Required property 'alarm' is missing"
-        return typing.cast(aws_cdk.aws_cloudwatch.IAlarm, result)
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.IAlarm, result)
 
     @builtins.property
     def health_check_name(self) -> typing.Optional[builtins.str]:
         '''The display name of this Route53 HealthCheck.'''
         result = self._values.get("health_check_name")
         return typing.cast(typing.Optional[builtins.str], result)
 
@@ -332,28 +324,20 @@
         '''
         :param child_health_checks: The list of HealthCheck that monitors other Route53 HealthChecks.
         :param health_check_name: The display name of this Route53 HealthCheck.
         :param health_threshold: The number of child HealthChecks that Amazon Route53 must consider healthy.
         :param inverted: Whether to invert the status of the Route53 health check status.
         '''
         if __debug__:
-            def stub(
-                *,
-                child_health_checks: typing.Optional[typing.Sequence[IHealthCheck]] = None,
-                health_check_name: typing.Optional[builtins.str] = None,
-                health_threshold: typing.Optional[jsii.Number] = None,
-                inverted: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__50716ab3df3dce42fb0a3b896e69290109228794f9a6daa26dea7eb00d9625fd)
             check_type(argname="argument child_health_checks", value=child_health_checks, expected_type=type_hints["child_health_checks"])
             check_type(argname="argument health_check_name", value=health_check_name, expected_type=type_hints["health_check_name"])
             check_type(argname="argument health_threshold", value=health_threshold, expected_type=type_hints["health_threshold"])
             check_type(argname="argument inverted", value=inverted, expected_type=type_hints["inverted"])
-        self._values: typing.Dict[str, typing.Any] = {}
+        self._values: typing.Dict[builtins.str, typing.Any] = {}
         if child_health_checks is not None:
             self._values["child_health_checks"] = child_health_checks
         if health_check_name is not None:
             self._values["health_check_name"] = health_check_name
         if health_threshold is not None:
             self._values["health_threshold"] = health_threshold
         if inverted is not None:
@@ -444,46 +428,29 @@
         :param protocol: The protocol that Route53 uses to communicate with the endpoint. An IP address must be specified if protocol TCP Default: HTTPS
         :param regions: The list of regions from which Route53 health checkers check the endpoint. If omitted Route53 performs checks from all health checker regions.
         :param request_interval: The number of seconds between the time that Route53 gets a response from your endpoint and the time that it sends the next health check request. Each Route53 health checker makes requests at this interval. Provide a number between 10 and 30. If you choose an interval of 10 and there are 15 health checkers, the endpoint will receive approximately 1 request per second. Can't be changed after HealthCheck is deployed
         :param resource_path: The path for HTTP or HTTPS health checks. Provide a string between 1 and 255 length.
         :param search_string: The search string for HTTP or HTTPS health checks. Route53 will search in the response body. Provide a string between 1 and 255 length.
         '''
         if __debug__:
-            def stub(
-                *,
-                domain_name: typing.Optional[builtins.str] = None,
-                enable_sni: typing.Optional[builtins.bool] = None,
-                failure_threshold: typing.Optional[jsii.Number] = None,
-                health_check_name: typing.Optional[builtins.str] = None,
-                inverted: typing.Optional[builtins.bool] = None,
-                ip_address: typing.Optional[builtins.str] = None,
-                latency_graphs: typing.Optional[builtins.bool] = None,
-                port: typing.Optional[jsii.Number] = None,
-                protocol: typing.Optional[Protocol] = None,
-                regions: typing.Optional[typing.Sequence[HealthCheckerRegions]] = None,
-                request_interval: typing.Optional[jsii.Number] = None,
-                resource_path: typing.Optional[builtins.str] = None,
-                search_string: typing.Optional[builtins.str] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__de064cce147a8183cdbdbedceafe764868f4f6e90a0f2301d6c340bdea374acc)
             check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
             check_type(argname="argument enable_sni", value=enable_sni, expected_type=type_hints["enable_sni"])
             check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
             check_type(argname="argument health_check_name", value=health_check_name, expected_type=type_hints["health_check_name"])
             check_type(argname="argument inverted", value=inverted, expected_type=type_hints["inverted"])
             check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
             check_type(argname="argument latency_graphs", value=latency_graphs, expected_type=type_hints["latency_graphs"])
             check_type(argname="argument port", value=port, expected_type=type_hints["port"])
             check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
             check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
             check_type(argname="argument request_interval", value=request_interval, expected_type=type_hints["request_interval"])
             check_type(argname="argument resource_path", value=resource_path, expected_type=type_hints["resource_path"])
             check_type(argname="argument search_string", value=search_string, expected_type=type_hints["search_string"])
-        self._values: typing.Dict[str, typing.Any] = {}
+        self._values: typing.Dict[builtins.str, typing.Any] = {}
         if domain_name is not None:
             self._values["domain_name"] = domain_name
         if enable_sni is not None:
             self._values["enable_sni"] = enable_sni
         if failure_threshold is not None:
             self._values["failure_threshold"] = failure_threshold
         if health_check_name is not None:
@@ -668,15 +635,15 @@
     @jsii.member(jsii_name="healthCheckId")
     def health_check_id(self) -> builtins.str:
         ...
 
     @jsii.member(jsii_name="failover")
     def failover(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
         failover: typing.Optional[Failover] = None,
     ) -> None:
         '''Sets ``this.healthCheckId`` as the value for ``HealthCheckId`` on the given RecordSet.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
@@ -687,15 +654,15 @@
         :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
         '''
         ...
 
     @jsii.member(jsii_name="failoverPrimary")
     def failover_primary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: The Route53 RecordSet to configure failover.
@@ -704,15 +671,15 @@
         :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
         '''
         ...
 
     @jsii.member(jsii_name="failoverSecondary")
     def failover_secondary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: The Route53 RecordSet to configure failover.
@@ -727,19 +694,19 @@
         self,
         metric_name: builtins.str,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Return the given named metric for this HealthCheck.
 
         :param metric_name: -
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
@@ -754,19 +721,19 @@
     def metric_health_check_status(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Route53 health checkers report that the HealthCheck is healthy or unhealthy.
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
@@ -784,184 +751,155 @@
     @jsii.member(jsii_name="healthCheckId")
     def health_check_id(self) -> builtins.str:
         return typing.cast(builtins.str, jsii.get(self, "healthCheckId"))
 
     @jsii.member(jsii_name="failover")
     def failover(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
         failover: typing.Optional[Failover] = None,
     ) -> None:
         '''Sets ``this.healthCheckId`` as the value for ``HealthCheckId`` on the given RecordSet.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: The Route53 RecordSet to configure failover.
         :param evaluate_target_health: Inherit the health of the referenced Alias RecordSet Target.
         :param failover: Sets ``PRIMARY`` or ``SECONDARY`` as the value for ``Failover`` on the given RecordSet.
 
         :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-                failover: typing.Optional[Failover] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__2b9a7ef656bb36af63e231e6e622e3a89c0b5a9ba6072c906dd908b331ad6f3e)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
             check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
         return typing.cast(None, jsii.invoke(self, "failover", [record_set, evaluate_target_health, failover]))
 
     @jsii.member(jsii_name="failoverPrimary")
     def failover_primary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: The Route53 RecordSet to configure failover.
         :param evaluate_target_health: Inherit the health of the referenced Alias RecordSet Target.
 
         :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__0077249ccf33344d454a3b96c20660322fed1daab0fcf9b06bb70bbaa03f0f63)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverPrimary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="failoverSecondary")
     def failover_secondary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: The Route53 RecordSet to configure failover.
         :param evaluate_target_health: Inherit the health of the referenced Alias RecordSet Target.
 
         :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__54b4362695c796799be2a98452ad465f86a45fddba2695215ae8271abb48935e)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverSecondary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="metric")
     def metric(
         self,
         metric_name: builtins.str,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Return the given named metric for this HealthCheck.
 
         :param metric_name: -
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
         if __debug__:
-            def stub(
-                metric_name: builtins.str,
-                *,
-                account: typing.Optional[builtins.str] = None,
-                color: typing.Optional[builtins.str] = None,
-                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
-                label: typing.Optional[builtins.str] = None,
-                period: typing.Optional[aws_cdk.Duration] = None,
-                region: typing.Optional[builtins.str] = None,
-                statistic: typing.Optional[builtins.str] = None,
-                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__79618bf48b4b6a7108b5e008672bcdf3b1533e9e51c76cef2397c6efbe3f9362)
             check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metric", [metric_name, props]))
 
     @jsii.member(jsii_name="metricHealthCheckStatus")
     def metric_health_check_status(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Route53 health checkers report that the HealthCheck is healthy or unhealthy.
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
 
 # Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
 typing.cast(typing.Any, IHealthCheck).__jsii_proxy_class__ = lambda : _IHealthCheckProxy
 
 
 @jsii.enum(
     jsii_type="@pepperize/cdk-route53-health-check.InsufficientDataHealthStatus"
@@ -980,17 +918,17 @@
     '''The protocol that Route53 uses to communicate with the endpoint.'''
 
     HTTP = "HTTP"
     HTTPS = "HTTPS"
     TCP = "TCP"
 
 
-@jsii.implements(IHealthCheck, aws_cdk.ITaggable)
+@jsii.implements(IHealthCheck, _aws_cdk_ceddda9d.ITaggable)
 class AlarmHealthCheck(
-    aws_cdk.Resource,
+    _aws_cdk_ceddda9d.Resource,
     metaclass=jsii.JSIIMeta,
     jsii_type="@pepperize/cdk-route53-health-check.AlarmHealthCheck",
 ):
     '''Create a Route53 HealthCheck that monitors a CloudWatch Alarm.
 
     Example Example::
 
@@ -1003,42 +941,32 @@
 
     :link: https://docs.aws.amazon.com/de_de/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#aws-resource-route53-healthcheck-properties
     :resource: AWS::Route53::HealthCheck
     '''
 
     def __init__(
         self,
-        scope: constructs.Construct,
+        scope: _constructs_77d1e7e8.Construct,
         id: builtins.str,
         *,
-        alarm: aws_cdk.aws_cloudwatch.IAlarm,
+        alarm: _aws_cdk_aws_cloudwatch_ceddda9d.IAlarm,
         health_check_name: typing.Optional[builtins.str] = None,
         insufficient_data_health_status: typing.Optional[InsufficientDataHealthStatus] = None,
         inverted: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''
         :param scope: -
         :param id: -
         :param alarm: The alarm that Route53 monitors.
         :param health_check_name: The display name of this Route53 HealthCheck.
         :param insufficient_data_health_status: The status to assign to the HealthCheck when CloudWatch has insufficient data about the metric.
         :param inverted: Whether to invert the status of the Route53 health check status.
         '''
         if __debug__:
-            def stub(
-                scope: constructs.Construct,
-                id: builtins.str,
-                *,
-                alarm: aws_cdk.aws_cloudwatch.IAlarm,
-                health_check_name: typing.Optional[builtins.str] = None,
-                insufficient_data_health_status: typing.Optional[InsufficientDataHealthStatus] = None,
-                inverted: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__d36aac16420758dbfbae42930ff169755dabea5542db39a095016eb2b327c192)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = AlarmHealthCheckProps(
             alarm=alarm,
             health_check_name=health_check_name,
             insufficient_data_health_status=insufficient_data_health_status,
             inverted=inverted,
@@ -1046,220 +974,185 @@
 
         jsii.create(self.__class__, self, [scope, id, props])
 
     @jsii.member(jsii_name="fromHealthCheckId")
     @builtins.classmethod
     def from_health_check_id(
         cls,
-        scope: constructs.Construct,
+        scope: _constructs_77d1e7e8.Construct,
         id: builtins.str,
         health_check_id: builtins.str,
     ) -> IHealthCheck:
         '''Import an existing Route53 HealthCheck.
 
         :param scope: -
         :param id: -
         :param health_check_id: -
         '''
         if __debug__:
-            def stub(
-                scope: constructs.Construct,
-                id: builtins.str,
-                health_check_id: builtins.str,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__1645a3096c6ae2781a8b3260b0cef1717dd64e6744f32d4fc79afaaf27469079)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
             check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
         return typing.cast(IHealthCheck, jsii.sinvoke(cls, "fromHealthCheckId", [scope, id, health_check_id]))
 
     @jsii.member(jsii_name="failover")
     def failover(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
         failover: typing.Optional[Failover] = None,
     ) -> None:
         '''Sets ``this.healthCheckId`` as the value for ``HealthCheckId`` on the given RecordSet.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         :param failover: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-                failover: typing.Optional[Failover] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__2e5389aa439d069566e7e936cbf4e65349b34326f21b2eb38ade9884cc66264d)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
             check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
         return typing.cast(None, jsii.invoke(self, "failover", [record_set, evaluate_target_health, failover]))
 
     @jsii.member(jsii_name="failoverPrimary")
     def failover_primary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__8f8fff8075d51aefe0aa9ef527518785d6d1276bab52157b4a46002fb79fa604)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverPrimary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="failoverSecondary")
     def failover_secondary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__46569cbabbd12efb41e94e511762c2da422bff9d63a76f34b1dd8125015e8851)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverSecondary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="metric")
     def metric(
         self,
         metric_name: builtins.str,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Return the given named metric for this HealthCheck.
 
         :param metric_name: -
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
         if __debug__:
-            def stub(
-                metric_name: builtins.str,
-                *,
-                account: typing.Optional[builtins.str] = None,
-                color: typing.Optional[builtins.str] = None,
-                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
-                label: typing.Optional[builtins.str] = None,
-                period: typing.Optional[aws_cdk.Duration] = None,
-                region: typing.Optional[builtins.str] = None,
-                statistic: typing.Optional[builtins.str] = None,
-                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__187d734344904617703d13b5c61336d6100026fac957ff594e33406201a71ecf)
             check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metric", [metric_name, props]))
 
     @jsii.member(jsii_name="metricHealthCheckStatus")
     def metric_health_check_status(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Route53 health checkers report that the HealthCheck is healthy or unhealthy.
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
 
     @builtins.property
     @jsii.member(jsii_name="healthCheckId")
     def health_check_id(self) -> builtins.str:
         return typing.cast(builtins.str, jsii.get(self, "healthCheckId"))
 
     @builtins.property
     @jsii.member(jsii_name="tags")
-    def tags(self) -> aws_cdk.TagManager:
+    def tags(self) -> _aws_cdk_ceddda9d.TagManager:
         '''TagManager to set, remove and format tags.'''
-        return typing.cast(aws_cdk.TagManager, jsii.get(self, "tags"))
+        return typing.cast(_aws_cdk_ceddda9d.TagManager, jsii.get(self, "tags"))
 
 
-@jsii.implements(IHealthCheck, aws_cdk.ITaggable)
+@jsii.implements(IHealthCheck, _aws_cdk_ceddda9d.ITaggable)
 class CalculatedHealthCheck(
-    aws_cdk.Resource,
+    _aws_cdk_ceddda9d.Resource,
     metaclass=jsii.JSIIMeta,
     jsii_type="@pepperize/cdk-route53-health-check.CalculatedHealthCheck",
 ):
     '''Create a Route53 HealthCheck that monitors other Route53 HealthChecks.
 
     Example Example::
 
@@ -1272,15 +1165,15 @@
 
     :link: https://docs.aws.amazon.com/de_de/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#aws-resource-route53-healthcheck-properties
     :resource: AWS::Route53::HealthCheck
     '''
 
     def __init__(
         self,
-        scope: constructs.Construct,
+        scope: _constructs_77d1e7e8.Construct,
         id: builtins.str,
         *,
         child_health_checks: typing.Optional[typing.Sequence[IHealthCheck]] = None,
         health_check_name: typing.Optional[builtins.str] = None,
         health_threshold: typing.Optional[jsii.Number] = None,
         inverted: typing.Optional[builtins.bool] = None,
     ) -> None:
@@ -1289,25 +1182,15 @@
         :param id: -
         :param child_health_checks: The list of HealthCheck that monitors other Route53 HealthChecks.
         :param health_check_name: The display name of this Route53 HealthCheck.
         :param health_threshold: The number of child HealthChecks that Amazon Route53 must consider healthy.
         :param inverted: Whether to invert the status of the Route53 health check status.
         '''
         if __debug__:
-            def stub(
-                scope: constructs.Construct,
-                id: builtins.str,
-                *,
-                child_health_checks: typing.Optional[typing.Sequence[IHealthCheck]] = None,
-                health_check_name: typing.Optional[builtins.str] = None,
-                health_threshold: typing.Optional[jsii.Number] = None,
-                inverted: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__6e89ac4b4326bbea34bfcd777269070151a02d03c8ec165a615703a3f5c55fbd)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = CalculatedHealthCheckProps(
             child_health_checks=child_health_checks,
             health_check_name=health_check_name,
             health_threshold=health_threshold,
             inverted=inverted,
@@ -1315,271 +1198,234 @@
 
         jsii.create(self.__class__, self, [scope, id, props])
 
     @jsii.member(jsii_name="fromHealthCheckId")
     @builtins.classmethod
     def from_health_check_id(
         cls,
-        scope: constructs.Construct,
+        scope: _constructs_77d1e7e8.Construct,
         id: builtins.str,
         health_check_id: builtins.str,
     ) -> IHealthCheck:
         '''Import an existing Route53 HealthCheck.
 
         :param scope: -
         :param id: -
         :param health_check_id: -
         '''
         if __debug__:
-            def stub(
-                scope: constructs.Construct,
-                id: builtins.str,
-                health_check_id: builtins.str,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__7146e8b74d3712e9672b89bad119949b0f1375b151e56eb489dac453df8f07f4)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
             check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
         return typing.cast(IHealthCheck, jsii.sinvoke(cls, "fromHealthCheckId", [scope, id, health_check_id]))
 
     @jsii.member(jsii_name="addChildHealthCheck")
     def add_child_health_check(self, health_check: IHealthCheck) -> None:
         '''
         :param health_check: -
         '''
         if __debug__:
-            def stub(health_check: IHealthCheck) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__d05c787a0958f9d792f576cda74c0ea46b48cab3cad3e6807b0f0a8b7bb28ac0)
             check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
         return typing.cast(None, jsii.invoke(self, "addChildHealthCheck", [health_check]))
 
     @jsii.member(jsii_name="failover")
     def failover(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
         failover: typing.Optional[Failover] = None,
     ) -> None:
         '''Sets ``this.healthCheckId`` as the value for ``HealthCheckId`` on the given RecordSet.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         :param failover: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-                failover: typing.Optional[Failover] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__39e445238411f86cda816c1dbec8a8a947492a1c72f0f83ebc34f4173b344762)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
             check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
         return typing.cast(None, jsii.invoke(self, "failover", [record_set, evaluate_target_health, failover]))
 
     @jsii.member(jsii_name="failoverPrimary")
     def failover_primary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__b42ad6740de959a833a7924f057498b25cde1240d07fd4791afb57d376583884)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverPrimary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="failoverSecondary")
     def failover_secondary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__13b0b996d65cf686be1c503fa589a2837077c6e3f31e19a2fac0ea8389548fcf)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverSecondary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="metric")
     def metric(
         self,
         metric_name: builtins.str,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Return the given named metric for this HealthCheck.
 
         :param metric_name: -
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
         if __debug__:
-            def stub(
-                metric_name: builtins.str,
-                *,
-                account: typing.Optional[builtins.str] = None,
-                color: typing.Optional[builtins.str] = None,
-                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
-                label: typing.Optional[builtins.str] = None,
-                period: typing.Optional[aws_cdk.Duration] = None,
-                region: typing.Optional[builtins.str] = None,
-                statistic: typing.Optional[builtins.str] = None,
-                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__9e12d39d9bbdf50f9bd221c15c0e36c980dd676ea1cdcd69f1743156da8adb0a)
             check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metric", [metric_name, props]))
 
     @jsii.member(jsii_name="metricChildHealthCheckHealthyCount")
     def metric_child_health_check_healthy_count(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''The number of ChildHealthChecks that are healthy that Route53 is monitoring.
 
         Valid statistics: Average (recommended), Minimum, Maximum
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricChildHealthCheckHealthyCount", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricChildHealthCheckHealthyCount", [props]))
 
     @jsii.member(jsii_name="metricHealthCheckStatus")
     def metric_health_check_status(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Route53 health checkers report that the HealthCheck is healthy or unhealthy.
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
 
     @builtins.property
     @jsii.member(jsii_name="healthCheckId")
     def health_check_id(self) -> builtins.str:
         return typing.cast(builtins.str, jsii.get(self, "healthCheckId"))
 
     @builtins.property
     @jsii.member(jsii_name="tags")
-    def tags(self) -> aws_cdk.TagManager:
+    def tags(self) -> _aws_cdk_ceddda9d.TagManager:
         '''TagManager to set, remove and format tags.'''
-        return typing.cast(aws_cdk.TagManager, jsii.get(self, "tags"))
+        return typing.cast(_aws_cdk_ceddda9d.TagManager, jsii.get(self, "tags"))
 
 
-@jsii.implements(IHealthCheck, aws_cdk.ITaggable)
+@jsii.implements(IHealthCheck, _aws_cdk_ceddda9d.ITaggable)
 class EndpointHealthCheck(
-    aws_cdk.Resource,
+    _aws_cdk_ceddda9d.Resource,
     metaclass=jsii.JSIIMeta,
     jsii_type="@pepperize/cdk-route53-health-check.EndpointHealthCheck",
 ):
     '''Create a Route53 HealthCheck that monitors an endpoint either by domain name or by IP address.
 
     Example Example::
 
@@ -1600,15 +1446,15 @@
 
     :link: https://docs.aws.amazon.com/de_de/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#aws-resource-route53-healthcheck-properties
     :resource: AWS::Route53::HealthCheck
     '''
 
     def __init__(
         self,
-        scope: constructs.Construct,
+        scope: _constructs_77d1e7e8.Construct,
         id: builtins.str,
         *,
         domain_name: typing.Optional[builtins.str] = None,
         enable_sni: typing.Optional[builtins.bool] = None,
         failure_threshold: typing.Optional[jsii.Number] = None,
         health_check_name: typing.Optional[builtins.str] = None,
         inverted: typing.Optional[builtins.bool] = None,
@@ -1635,34 +1481,15 @@
         :param protocol: The protocol that Route53 uses to communicate with the endpoint. An IP address must be specified if protocol TCP Default: HTTPS
         :param regions: The list of regions from which Route53 health checkers check the endpoint. If omitted Route53 performs checks from all health checker regions.
         :param request_interval: The number of seconds between the time that Route53 gets a response from your endpoint and the time that it sends the next health check request. Each Route53 health checker makes requests at this interval. Provide a number between 10 and 30. If you choose an interval of 10 and there are 15 health checkers, the endpoint will receive approximately 1 request per second. Can't be changed after HealthCheck is deployed
         :param resource_path: The path for HTTP or HTTPS health checks. Provide a string between 1 and 255 length.
         :param search_string: The search string for HTTP or HTTPS health checks. Route53 will search in the response body. Provide a string between 1 and 255 length.
         '''
         if __debug__:
-            def stub(
-                scope: constructs.Construct,
-                id: builtins.str,
-                *,
-                domain_name: typing.Optional[builtins.str] = None,
-                enable_sni: typing.Optional[builtins.bool] = None,
-                failure_threshold: typing.Optional[jsii.Number] = None,
-                health_check_name: typing.Optional[builtins.str] = None,
-                inverted: typing.Optional[builtins.bool] = None,
-                ip_address: typing.Optional[builtins.str] = None,
-                latency_graphs: typing.Optional[builtins.bool] = None,
-                port: typing.Optional[jsii.Number] = None,
-                protocol: typing.Optional[Protocol] = None,
-                regions: typing.Optional[typing.Sequence[HealthCheckerRegions]] = None,
-                request_interval: typing.Optional[jsii.Number] = None,
-                resource_path: typing.Optional[builtins.str] = None,
-                search_string: typing.Optional[builtins.str] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__ce4c878d5c215d6b92e5a4681d2a3918ab898f350d63beb38250050c2b0fbd6d)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
         props = EndpointHealthCheckProps(
             domain_name=domain_name,
             enable_sni=enable_sni,
             failure_threshold=failure_threshold,
             health_check_name=health_check_name,
@@ -1679,220 +1506,185 @@
 
         jsii.create(self.__class__, self, [scope, id, props])
 
     @jsii.member(jsii_name="fromHealthCheckId")
     @builtins.classmethod
     def from_health_check_id(
         cls,
-        scope: constructs.Construct,
+        scope: _constructs_77d1e7e8.Construct,
         id: builtins.str,
         health_check_id: builtins.str,
     ) -> IHealthCheck:
         '''Import an existing Route53 HealthCheck.
 
         :param scope: -
         :param id: -
         :param health_check_id: -
         '''
         if __debug__:
-            def stub(
-                scope: constructs.Construct,
-                id: builtins.str,
-                health_check_id: builtins.str,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__d63b1664cc6df185e3a013bd30f67e9c593be3877e84e39df05b9300eb8cd565)
             check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
             check_type(argname="argument id", value=id, expected_type=type_hints["id"])
             check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
         return typing.cast(IHealthCheck, jsii.sinvoke(cls, "fromHealthCheckId", [scope, id, health_check_id]))
 
     @jsii.member(jsii_name="failover")
     def failover(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
         failover: typing.Optional[Failover] = None,
     ) -> None:
         '''Sets ``this.healthCheckId`` as the value for ``HealthCheckId`` on the given RecordSet.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         :param failover: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-                failover: typing.Optional[Failover] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__f98787d45fd0ad7a6aeb5bfa65c81f2cc37f84ea7322dd28edffabfa481fd7aa)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
             check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
         return typing.cast(None, jsii.invoke(self, "failover", [record_set, evaluate_target_health, failover]))
 
     @jsii.member(jsii_name="failoverPrimary")
     def failover_primary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__bd1a620a38e733e1cd1d39178c742a88d132ea4c23f1959b1205551b3857daa4)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverPrimary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="failoverSecondary")
     def failover_secondary(
         self,
-        record_set: aws_cdk.aws_route53.RecordSet,
+        record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
         evaluate_target_health: typing.Optional[builtins.bool] = None,
     ) -> None:
         '''Sets ``PRIMARY`` as the value for ``Failover`` on the given RecordSet. Additionally, sets ``this.healthCheckId`` as the value for ``HealthCheckId``.
 
         Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets
 
         :param record_set: -
         :param evaluate_target_health: -
         '''
         if __debug__:
-            def stub(
-                record_set: aws_cdk.aws_route53.RecordSet,
-                evaluate_target_health: typing.Optional[builtins.bool] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__7adf6d93f0936e5fb0846f9c7d0349d6350b5a09a906631d8104dac41a745cd8)
             check_type(argname="argument record_set", value=record_set, expected_type=type_hints["record_set"])
             check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
         return typing.cast(None, jsii.invoke(self, "failoverSecondary", [record_set, evaluate_target_health]))
 
     @jsii.member(jsii_name="metric")
     def metric(
         self,
         metric_name: builtins.str,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Return the given named metric for this HealthCheck.
 
         :param metric_name: -
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
         if __debug__:
-            def stub(
-                metric_name: builtins.str,
-                *,
-                account: typing.Optional[builtins.str] = None,
-                color: typing.Optional[builtins.str] = None,
-                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
-                label: typing.Optional[builtins.str] = None,
-                period: typing.Optional[aws_cdk.Duration] = None,
-                region: typing.Optional[builtins.str] = None,
-                statistic: typing.Optional[builtins.str] = None,
-                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-            ) -> None:
-                ...
-            type_hints = typing.get_type_hints(stub)
+            type_hints = typing.get_type_hints(_typecheckingstub__9fc326233fa994ef17d91bc6d6111617414c5ce213e1025911e76fac9c834594)
             check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metric", [metric_name, props]))
 
     @jsii.member(jsii_name="metricConnectionTime")
     def metric_connection_time(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''The time in milliseconds that it took Route53 health checkers to establish a TCP connection with the endpoint.
 
         Valid statistics: Average (recommended), Minimum, Maximum
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricConnectionTime", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricConnectionTime", [props]))
 
     @jsii.member(jsii_name="metricHealthCheckPercentageHealthy")
     def metric_health_check_percentage_healthy(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''The percentage of Route53 health checkers that report that the status of the health check is healthy.
 
         LatencyGraphs has to be enabled
 
         Valid statistics: Average (recommended), Minimum, Maximum
 
         :param account: Account which this metric comes from. Default: - Deployment account.
@@ -1900,152 +1692,152 @@
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricHealthCheckPercentageHealthy", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricHealthCheckPercentageHealthy", [props]))
 
     @jsii.member(jsii_name="metricHealthCheckStatus")
     def metric_health_check_status(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''Route53 health checkers report that the HealthCheck is healthy or unhealthy.
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricHealthCheckStatus", [props]))
 
     @jsii.member(jsii_name="metricSSLHandshakeTime")
     def metric_ssl_handshake_time(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''The time in milliseconds that it took Route53 health checkers to complete the SSL/TLS handshake.
 
         Valid statistics: Average, Minimum, Maximum
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricSSLHandshakeTime", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricSSLHandshakeTime", [props]))
 
     @jsii.member(jsii_name="metricTimeToFirstByte")
     def metric_time_to_first_byte(
         self,
         *,
         account: typing.Optional[builtins.str] = None,
         color: typing.Optional[builtins.str] = None,
         dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
         label: typing.Optional[builtins.str] = None,
-        period: typing.Optional[aws_cdk.Duration] = None,
+        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
         region: typing.Optional[builtins.str] = None,
         statistic: typing.Optional[builtins.str] = None,
-        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
-    ) -> aws_cdk.aws_cloudwatch.Metric:
+        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
         '''The time in milliseconds that it took Route53 health checkers to receive the first byte of the response to an HTTP or HTTPS request.
 
         Valid statistics: Average (recommended), Minimum, Maximum
 
         :param account: Account which this metric comes from. Default: - Deployment account.
         :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
         :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
         :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
         :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
         :param region: Region which this metric comes from. Default: - Deployment region.
         :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" Default: Average
         :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
         '''
-        props = aws_cdk.aws_cloudwatch.MetricOptions(
+        props = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
             account=account,
             color=color,
             dimensions_map=dimensions_map,
             label=label,
             period=period,
             region=region,
             statistic=statistic,
             unit=unit,
         )
 
-        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metricTimeToFirstByte", [props]))
+        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricTimeToFirstByte", [props]))
 
     @builtins.property
     @jsii.member(jsii_name="healthCheckId")
     def health_check_id(self) -> builtins.str:
         return typing.cast(builtins.str, jsii.get(self, "healthCheckId"))
 
     @builtins.property
     @jsii.member(jsii_name="tags")
-    def tags(self) -> aws_cdk.TagManager:
+    def tags(self) -> _aws_cdk_ceddda9d.TagManager:
         '''TagManager to set, remove and format tags.'''
-        return typing.cast(aws_cdk.TagManager, jsii.get(self, "tags"))
+        return typing.cast(_aws_cdk_ceddda9d.TagManager, jsii.get(self, "tags"))
 
 
 __all__ = [
     "AlarmHealthCheck",
     "AlarmHealthCheckProps",
     "CalculatedHealthCheck",
     "CalculatedHealthCheckProps",
@@ -2055,7 +1847,269 @@
     "HealthCheckerRegions",
     "IHealthCheck",
     "InsufficientDataHealthStatus",
     "Protocol",
 ]
 
 publication.publish()
+
+def _typecheckingstub__639153b296f45bd8c248c52158a6493c4845bdb55b7de3975f909413a7b84ae2(
+    *,
+    alarm: _aws_cdk_aws_cloudwatch_ceddda9d.IAlarm,
+    health_check_name: typing.Optional[builtins.str] = None,
+    insufficient_data_health_status: typing.Optional[InsufficientDataHealthStatus] = None,
+    inverted: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__50716ab3df3dce42fb0a3b896e69290109228794f9a6daa26dea7eb00d9625fd(
+    *,
+    child_health_checks: typing.Optional[typing.Sequence[IHealthCheck]] = None,
+    health_check_name: typing.Optional[builtins.str] = None,
+    health_threshold: typing.Optional[jsii.Number] = None,
+    inverted: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__de064cce147a8183cdbdbedceafe764868f4f6e90a0f2301d6c340bdea374acc(
+    *,
+    domain_name: typing.Optional[builtins.str] = None,
+    enable_sni: typing.Optional[builtins.bool] = None,
+    failure_threshold: typing.Optional[jsii.Number] = None,
+    health_check_name: typing.Optional[builtins.str] = None,
+    inverted: typing.Optional[builtins.bool] = None,
+    ip_address: typing.Optional[builtins.str] = None,
+    latency_graphs: typing.Optional[builtins.bool] = None,
+    port: typing.Optional[jsii.Number] = None,
+    protocol: typing.Optional[Protocol] = None,
+    regions: typing.Optional[typing.Sequence[HealthCheckerRegions]] = None,
+    request_interval: typing.Optional[jsii.Number] = None,
+    resource_path: typing.Optional[builtins.str] = None,
+    search_string: typing.Optional[builtins.str] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__2b9a7ef656bb36af63e231e6e622e3a89c0b5a9ba6072c906dd908b331ad6f3e(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+    failover: typing.Optional[Failover] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__0077249ccf33344d454a3b96c20660322fed1daab0fcf9b06bb70bbaa03f0f63(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__54b4362695c796799be2a98452ad465f86a45fddba2695215ae8271abb48935e(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__79618bf48b4b6a7108b5e008672bcdf3b1533e9e51c76cef2397c6efbe3f9362(
+    metric_name: builtins.str,
+    *,
+    account: typing.Optional[builtins.str] = None,
+    color: typing.Optional[builtins.str] = None,
+    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
+    label: typing.Optional[builtins.str] = None,
+    period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
+    region: typing.Optional[builtins.str] = None,
+    statistic: typing.Optional[builtins.str] = None,
+    unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__d36aac16420758dbfbae42930ff169755dabea5542db39a095016eb2b327c192(
+    scope: _constructs_77d1e7e8.Construct,
+    id: builtins.str,
+    *,
+    alarm: _aws_cdk_aws_cloudwatch_ceddda9d.IAlarm,
+    health_check_name: typing.Optional[builtins.str] = None,
+    insufficient_data_health_status: typing.Optional[InsufficientDataHealthStatus] = None,
+    inverted: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__1645a3096c6ae2781a8b3260b0cef1717dd64e6744f32d4fc79afaaf27469079(
+    scope: _constructs_77d1e7e8.Construct,
+    id: builtins.str,
+    health_check_id: builtins.str,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__2e5389aa439d069566e7e936cbf4e65349b34326f21b2eb38ade9884cc66264d(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+    failover: typing.Optional[Failover] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__8f8fff8075d51aefe0aa9ef527518785d6d1276bab52157b4a46002fb79fa604(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__46569cbabbd12efb41e94e511762c2da422bff9d63a76f34b1dd8125015e8851(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__187d734344904617703d13b5c61336d6100026fac957ff594e33406201a71ecf(
+    metric_name: builtins.str,
+    *,
+    account: typing.Optional[builtins.str] = None,
+    color: typing.Optional[builtins.str] = None,
+    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
+    label: typing.Optional[builtins.str] = None,
+    period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
+    region: typing.Optional[builtins.str] = None,
+    statistic: typing.Optional[builtins.str] = None,
+    unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__6e89ac4b4326bbea34bfcd777269070151a02d03c8ec165a615703a3f5c55fbd(
+    scope: _constructs_77d1e7e8.Construct,
+    id: builtins.str,
+    *,
+    child_health_checks: typing.Optional[typing.Sequence[IHealthCheck]] = None,
+    health_check_name: typing.Optional[builtins.str] = None,
+    health_threshold: typing.Optional[jsii.Number] = None,
+    inverted: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__7146e8b74d3712e9672b89bad119949b0f1375b151e56eb489dac453df8f07f4(
+    scope: _constructs_77d1e7e8.Construct,
+    id: builtins.str,
+    health_check_id: builtins.str,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__d05c787a0958f9d792f576cda74c0ea46b48cab3cad3e6807b0f0a8b7bb28ac0(
+    health_check: IHealthCheck,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__39e445238411f86cda816c1dbec8a8a947492a1c72f0f83ebc34f4173b344762(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+    failover: typing.Optional[Failover] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__b42ad6740de959a833a7924f057498b25cde1240d07fd4791afb57d376583884(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__13b0b996d65cf686be1c503fa589a2837077c6e3f31e19a2fac0ea8389548fcf(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__9e12d39d9bbdf50f9bd221c15c0e36c980dd676ea1cdcd69f1743156da8adb0a(
+    metric_name: builtins.str,
+    *,
+    account: typing.Optional[builtins.str] = None,
+    color: typing.Optional[builtins.str] = None,
+    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
+    label: typing.Optional[builtins.str] = None,
+    period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
+    region: typing.Optional[builtins.str] = None,
+    statistic: typing.Optional[builtins.str] = None,
+    unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__ce4c878d5c215d6b92e5a4681d2a3918ab898f350d63beb38250050c2b0fbd6d(
+    scope: _constructs_77d1e7e8.Construct,
+    id: builtins.str,
+    *,
+    domain_name: typing.Optional[builtins.str] = None,
+    enable_sni: typing.Optional[builtins.bool] = None,
+    failure_threshold: typing.Optional[jsii.Number] = None,
+    health_check_name: typing.Optional[builtins.str] = None,
+    inverted: typing.Optional[builtins.bool] = None,
+    ip_address: typing.Optional[builtins.str] = None,
+    latency_graphs: typing.Optional[builtins.bool] = None,
+    port: typing.Optional[jsii.Number] = None,
+    protocol: typing.Optional[Protocol] = None,
+    regions: typing.Optional[typing.Sequence[HealthCheckerRegions]] = None,
+    request_interval: typing.Optional[jsii.Number] = None,
+    resource_path: typing.Optional[builtins.str] = None,
+    search_string: typing.Optional[builtins.str] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__d63b1664cc6df185e3a013bd30f67e9c593be3877e84e39df05b9300eb8cd565(
+    scope: _constructs_77d1e7e8.Construct,
+    id: builtins.str,
+    health_check_id: builtins.str,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__f98787d45fd0ad7a6aeb5bfa65c81f2cc37f84ea7322dd28edffabfa481fd7aa(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+    failover: typing.Optional[Failover] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__bd1a620a38e733e1cd1d39178c742a88d132ea4c23f1959b1205551b3857daa4(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__7adf6d93f0936e5fb0846f9c7d0349d6350b5a09a906631d8104dac41a745cd8(
+    record_set: _aws_cdk_aws_route53_ceddda9d.RecordSet,
+    evaluate_target_health: typing.Optional[builtins.bool] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
+
+def _typecheckingstub__9fc326233fa994ef17d91bc6d6111617414c5ce213e1025911e76fac9c834594(
+    metric_name: builtins.str,
+    *,
+    account: typing.Optional[builtins.str] = None,
+    color: typing.Optional[builtins.str] = None,
+    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
+    label: typing.Optional[builtins.str] = None,
+    period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
+    region: typing.Optional[builtins.str] = None,
+    statistic: typing.Optional[builtins.str] = None,
+    unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
+) -> None:
+    """Type checking stubs"""
+    pass
```

### Comparing `pepperize.cdk-route53-health-check-0.0.98/src/pepperize_cdk_route53_health_check/_jsii/cdk-route53-health-check@0.0.98.jsii.tgz` & `pepperize.cdk-route53-health-check-0.0.99/src/pepperize_cdk_route53_health_check/_jsii/cdk-route53-health-check@0.0.99.jsii.tgz`

 * *Files 15% similar despite different names*

#### Comparing `cdk-route53-health-check@0.0.98.jsii.tgz-content` & `cdk-route53-health-check@0.0.99.jsii.tgz-content`

##### package/.jsii

###### Pretty-printed

 * *Similarity: 0.9444444444444444%*

 * *Differences: {"'fingerprint'": "'iAf5UFzej6L58HmFRJ50S6pBtOLuAplH1zR6x2ZfbZw='", "'version'": "'0.0.99'"}*

```diff
@@ -3097,15 +3097,15 @@
             }
         }
     },
     "description": "Create Route53 HealthChecks to monitor TCP, HTTP, HTTPS endpoints, CloudWatch Alarms and other Route53 HealthChecks.",
     "docs": {
         "stability": "stable"
     },
-    "fingerprint": "CWLEw6VTdlrswbXFqVyUMtXRR61VXZsrkfOe4C+B+GI=",
+    "fingerprint": "iAf5UFzej6L58HmFRJ50S6pBtOLuAplH1zR6x2ZfbZw=",
     "homepage": "https://github.com/pepperize/cdk-route53-health-check.git",
     "jsiiVersion": "1.72.0 (build 4b8828b)",
     "keywords": [
         "AWS",
         "Alarm",
         "CDK",
         "Calculated",
@@ -4929,9 +4929,9 @@
                     "name": "TCP"
                 }
             ],
             "name": "Protocol",
             "symbolId": "src/endpoint-health-check:Protocol"
         }
     },
-    "version": "0.0.98"
+    "version": "0.0.99"
 }
```

##### package/lib/alarm-health-check.js

###### js-beautify {}

```diff
@@ -52,15 +52,15 @@
         }
     }
 }
 exports.AlarmHealthCheck = AlarmHealthCheck;
 _a = JSII_RTTI_SYMBOL_1;
 AlarmHealthCheck[_a] = {
     fqn: "@pepperize/cdk-route53-health-check.AlarmHealthCheck",
-    version: "0.0.98"
+    version: "0.0.99"
 };
 var InsufficientDataHealthStatus;
 (function(InsufficientDataHealthStatus) {
     /**
      * Route53 considers the health check to be healthy.
      */
     InsufficientDataHealthStatus["HEALTHY"] = "Healthy";
```

##### package/lib/calculated-health-check.js

###### js-beautify {}

```diff
@@ -66,10 +66,10 @@
         this.childHealthChecks.push(healthCheck);
     }
 }
 exports.CalculatedHealthCheck = CalculatedHealthCheck;
 _a = JSII_RTTI_SYMBOL_1;
 CalculatedHealthCheck[_a] = {
     fqn: "@pepperize/cdk-route53-health-check.CalculatedHealthCheck",
-    version: "0.0.98"
+    version: "0.0.99"
 };
 //# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiY2FsY3VsYXRlZC1oZWFsdGgtY2hlY2suanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyIuLi9zcmMvY2FsY3VsYXRlZC1oZWFsdGgtY2hlY2sudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7Ozs7QUFBQSw2Q0FBc0Q7QUFDdEQseURBQXlEO0FBQ3pELG1EQUFtRDtBQUVuRCxpREFBbUY7QUFDbkYsMkRBQXNEO0FBYXREOzs7Ozs7Ozs7Ozs7Ozs7R0FlRztBQUNILE1BQWEscUJBQXNCLFNBQVEsOEJBQWU7SUFLeEQsWUFBWSxLQUFnQixFQUFFLEVBQVUsRUFBRSxLQUFpQztRQUN6RSxLQUFLLENBQUMsS0FBSyxFQUFFLEVBQUUsQ0FBQyxDQUFDO1FBRWpCLElBQUksQ0FBQyxpQkFBaUIsR0FBRyxLQUFLLENBQUMsaUJBQWlCLElBQUksRUFBRSxDQUFDO1FBRXZELElBQUksSUFBSSxDQUFDLGlCQUFpQixDQUFDLE1BQU0sR0FBRyxHQUFHLEVBQUU7WUFDdkMseUJBQVcsQ0FBQyxFQUFFLENBQUMsSUFBSSxDQUFDLENBQUMsUUFBUSxDQUFDLDhDQUE4QyxDQUFDLENBQUM7U0FDL0U7UUFFRCxJQUFJLFNBQVMsSUFBSSxLQUFLLENBQUMsZUFBZSxJQUFJLEtBQUssQ0FBQyxlQUFlLEdBQUcsR0FBRyxFQUFFO1lBQ3JFLHlCQUFXLENBQUMsRUFBRSxDQUFDLElBQUksQ0FBQyxDQUFDLFFBQVEsQ0FBQyw0Q0FBNEMsQ0FBQyxDQUFDO1NBQzdFO1FBRUQsTUFBTSxRQUFRLEdBQUcsSUFBSSxPQUFPLENBQUMsY0FBYyxDQUFDLElBQUksRUFBRSxVQUFVLEVBQUU7WUFDNUQsaUJBQWlCLEVBQUU7Z0JBQ2pCLGlCQUFpQixFQUFFLGtCQUFJLENBQUMsSUFBSSxDQUFDO29CQUMzQixPQUFPLEVBQUUsR0FBRyxFQUFFLENBQUMsSUFBSSxDQUFDLGlCQUFpQixDQUFDLEdBQUcsQ0FBQyxDQUFDLFdBQVcsRUFBRSxFQUFFLENBQUMsV0FBVyxDQUFDLGFBQWEsQ0FBQztpQkFDdEYsQ0FBQztnQkFDRixlQUFlLEVBQUUsS0FBSyxDQUFDLGVBQWU7Z0JBQ3RDLElBQUksRUFBRSxtQ0FBZSxDQUFDLFVBQVU7YUFDakM7WUFDRCxlQUFlLEVBQUUsSUFBSSxDQUFDLElBQUksQ0FBQyxZQUFZO1NBQ3hDLENBQUMsQ0FBQztRQUVILElBQUksQ0FBQyxhQUFhLEdBQUcsUUFBUSxDQUFDLGlCQUFpQixDQUFDO1FBRWhELElBQUksS0FBSyxDQUFDLGVBQWUsRUFBRTtZQUN6QixrQkFBSSxDQUFDLEVBQUUsQ0FBQyxJQUFJLENBQUMsQ0FBQyxHQUFHLENBQUMsTUFBTSxFQUFFLEtBQUssQ0FBQyxlQUFlLENBQUMsQ0FBQztTQUNsRDtJQUNILENBQUM7SUFFRDs7OztPQUlHO0lBQ0ksa0NBQWtDLENBQUMsS0FBZ0M7UUFDeEUsT0FBTyxJQUFJLENBQUMsTUFBTSxDQUFDLDhCQUE4QixFQUFFLEVBQUUsU0FBUyxFQUFFLFVBQVUsQ0FBQyxTQUFTLENBQUMsT0FBTyxFQUFFLEdBQUcsS0FBSyxFQUFFLENBQUMsQ0FBQztJQUM1RyxDQUFDO0lBRU0sbUJBQW1CLENBQUMsV0FBeUI7UUFDbEQsSUFBSSxDQUFDLGlCQUFpQixDQUFDLElBQUksQ0FBQyxXQUFXLENBQUMsQ0FBQztJQUMzQyxDQUFDOztBQS9DSCxzREFnREMiLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBBbm5vdGF0aW9ucywgTGF6eSwgVGFncyB9IGZyb20gXCJhd3MtY2RrLWxpYlwiO1xuaW1wb3J0ICogYXMgY2xvdWR3YXRjaCBmcm9tIFwiYXdzLWNkay1saWIvYXdzLWNsb3Vkd2F0Y2hcIjtcbmltcG9ydCAqIGFzIHJvdXRlNTMgZnJvbSBcImF3cy1jZGstbGliL2F3cy1yb3V0ZTUzXCI7XG5pbXBvcnQgeyBDb25zdHJ1Y3QgfSBmcm9tIFwiY29uc3RydWN0c1wiO1xuaW1wb3J0IHsgSGVhbHRoQ2hlY2tCYXNlLCBIZWFsdGhDaGVja09wdGlvbnMsIElIZWFsdGhDaGVjayB9IGZyb20gXCIuL2hlYWx0aC1jaGVja1wiO1xuaW1wb3J0IHsgSGVhbHRoQ2hlY2tUeXBlIH0gZnJvbSBcIi4vaGVhbHRoLWNoZWNrLXR5cGVcIjtcblxuZXhwb3J0IGludGVyZmFjZSBDYWxjdWxhdGVkSGVhbHRoQ2hlY2tQcm9wcyBleHRlbmRzIEhlYWx0aENoZWNrT3B0aW9ucyB7XG4gIC8qKlxuICAgKiBUaGUgbGlzdCBvZiBIZWFsdGhDaGVjayB0aGF0IG1vbml0b3JzIG90aGVyIFJvdXRlNTMgSGVhbHRoQ2hlY2tzLlxuICAgKi9cbiAgcmVhZG9ubHkgY2hpbGRIZWFsdGhDaGVja3M/OiBJSGVhbHRoQ2hlY2tbXTtcbiAgLyoqXG4gICAqIFRoZSBudW1iZXIgb2YgY2hpbGQgSGVhbHRoQ2hlY2tzIHRoYXQgQW1hem9uIFJvdXRlNTMgbXVzdCBjb25zaWRlciBoZWFsdGh5XG4gICAqL1xuICByZWFkb25seSBoZWFsdGhUaHJlc2hvbGQ/OiBudW1iZXI7XG59XG5cbi8qKlxuICogQ3JlYXRlIGEgUm91dGU1MyBIZWFsdGhDaGVjayB0aGF0IG1vbml0b3JzIG90aGVyIFJvdXRlNTMgSGVhbHRoQ2hlY2tzLlxuICpcbiAqIDxiPkV4YW1wbGU8L2I+XG4gKiBgYGB0eXBlc2NyaXB0XG4gKiBjb25zdCBoZWFsdGhDaGVjayA9IG5ldyBFbmRwb2ludEhlYWx0aENoZWNrKHN0YWNrLCBcIkhlYWx0aENoZWNrXCIsIHtcbiAqICAgZG9tYWluTmFtZTogXCJwZXBwZXJpemUuY29tXCIsXG4gKiB9KTtcbiAqIG5ldyBDYWxjdWxhdGVkSGVhbHRoQ2hlY2soc3RhY2ssIFwiQ2FsY3VsYXRlZEhlYWx0aENoZWNrXCIsIHtcbiAqICAgY2hpbGRIZWFsdGhDaGVja3M6IFtoZWFsdGhDaGVja10sXG4gKiB9KTtcbiAqIGBgYFxuICogQGxpbmsgaHR0cHM6Ly9kb2NzLmF3cy5hbWF6b24uY29tL2RlX2RlL0FXU0Nsb3VkRm9ybWF0aW9uL2xhdGVzdC9Vc2VyR3VpZGUvYXdzLXJlc291cmNlLXJvdXRlNTMtaGVhbHRoY2hlY2suaHRtbCNhd3MtcmVzb3VyY2Utcm91dGU1My1oZWFsdGhjaGVjay1wcm9wZXJ0aWVzXG4gKlxuICogQHJlc291cmNlIEFXUzo6Um91dGU1Mzo6SGVhbHRoQ2hlY2tcbiAqL1xuZXhwb3J0IGNsYXNzIENhbGN1bGF0ZWRIZWFsdGhDaGVjayBleHRlbmRzIEhlYWx0aENoZWNrQmFzZSB7XG4gIHB1YmxpYyByZWFkb25seSBoZWFsdGhDaGVja0lkOiBzdHJpbmc7XG5cbiAgcHJpdmF0ZSBjaGlsZEhlYWx0aENoZWNrczogSUhlYWx0aENoZWNrW107XG5cbiAgY29uc3RydWN0b3Ioc2NvcGU6IENvbnN0cnVjdCwgaWQ6IHN0cmluZywgcHJvcHM6IENhbGN1bGF0ZWRIZWFsdGhDaGVja1Byb3BzKSB7XG4gICAgc3VwZXIoc2NvcGUsIGlkKTtcblxuICAgIHRoaXMuY2hpbGRIZWFsdGhDaGVja3MgPSBwcm9wcy5jaGlsZEhlYWx0aENoZWNrcyA/PyBbXTtcblxuICAgIGlmICh0aGlzLmNoaWxkSGVhbHRoQ2hlY2tzLmxlbmd0aCA+IDI1Nikge1xuICAgICAgQW5ub3RhdGlvbnMub2YodGhpcykuYWRkRXJyb3IoXCJDaGlsZEhlYWx0aENoZWNrcyBoYXMgdG8gYmUgc21hbGxlciB0aGFuIDI1NlwiKTtcbiAgICB9XG5cbiAgICBpZiAodW5kZWZpbmVkICE9IHByb3BzLmhlYWx0aFRocmVzaG9sZCAmJiBwcm9wcy5oZWFsdGhUaHJlc2hvbGQgPiAyNTYpIHtcbiAgICAgIEFubm90YXRpb25zLm9mKHRoaXMpLmFkZEVycm9yKFwiSGVhbHRoVGhyZXNob2xkIGhhcyB0byBiZSBzbWFsbGVyIHRoYW4gMjU2XCIpO1xuICAgIH1cblxuICAgIGNvbnN0IHJlc291cmNlID0gbmV3IHJvdXRlNTMuQ2ZuSGVhbHRoQ2hlY2sodGhpcywgXCJSZXNvdXJjZVwiLCB7XG4gICAgICBoZWFsdGhDaGVja0NvbmZpZzoge1xuICAgICAgICBjaGlsZEhlYWx0aENoZWNrczogTGF6eS5saXN0KHtcbiAgICAgICAgICBwcm9kdWNlOiAoKSA9PiB0aGlzLmNoaWxkSGVhbHRoQ2hlY2tzLm1hcCgoaGVhbHRoQ2hlY2spID0+IGhlYWx0aENoZWNrLmhlYWx0aENoZWNrSWQpLFxuICAgICAgICB9KSxcbiAgICAgICAgaGVhbHRoVGhyZXNob2xkOiBwcm9wcy5oZWFsdGhUaHJlc2hvbGQsXG4gICAgICAgIHR5cGU6IEhlYWx0aENoZWNrVHlwZS5DQUxDVUxBVEVELFxuICAgICAgfSxcbiAgICAgIGhlYWx0aENoZWNrVGFnczogdGhpcy50YWdzLnJlbmRlcmVkVGFncyxcbiAgICB9KTtcblxuICAgIHRoaXMuaGVhbHRoQ2hlY2tJZCA9IHJlc291cmNlLmF0dHJIZWFsdGhDaGVja0lkO1xuXG4gICAgaWYgKHByb3BzLmhlYWx0aENoZWNrTmFtZSkge1xuICAgICAgVGFncy5vZih0aGlzKS5hZGQoXCJOYW1lXCIsIHByb3BzLmhlYWx0aENoZWNrTmFtZSk7XG4gICAgfVxuICB9XG5cbiAgLyoqXG4gICAqIFRoZSBudW1iZXIgb2YgQ2hpbGRIZWFsdGhDaGVja3MgdGhhdCBhcmUgaGVhbHRoeSB0aGF0IFJvdXRlNTMgaXMgbW9uaXRvcmluZy5cbiAgICpcbiAgICogVmFsaWQgc3RhdGlzdGljczogQXZlcmFnZSAocmVjb21tZW5kZWQpLCBNaW5pbXVtLCBNYXhpbXVtXG4gICAqL1xuICBwdWJsaWMgbWV0cmljQ2hpbGRIZWFsdGhDaGVja0hlYWx0aHlDb3VudChwcm9wcz86IGNsb3Vkd2F0Y2guTWV0cmljT3B0aW9ucyk6IGNsb3Vkd2F0Y2guTWV0cmljIHtcbiAgICByZXR1cm4gdGhpcy5tZXRyaWMoXCJDaGlsZEhlYWx0aENoZWNrSGVhbHRoeUNvdW50XCIsIHsgc3RhdGlzdGljOiBjbG91ZHdhdGNoLlN0YXRpc3RpYy5BVkVSQUdFLCAuLi5wcm9wcyB9KTtcbiAgfVxuXG4gIHB1YmxpYyBhZGRDaGlsZEhlYWx0aENoZWNrKGhlYWx0aENoZWNrOiBJSGVhbHRoQ2hlY2spIHtcbiAgICB0aGlzLmNoaWxkSGVhbHRoQ2hlY2tzLnB1c2goaGVhbHRoQ2hlY2spO1xuICB9XG59XG4iXX0=
```

##### package/lib/endpoint-health-check.js

###### js-beautify {}

```diff
@@ -184,15 +184,15 @@
         });
     }
 }
 exports.EndpointHealthCheck = EndpointHealthCheck;
 _a = JSII_RTTI_SYMBOL_1;
 EndpointHealthCheck[_a] = {
     fqn: "@pepperize/cdk-route53-health-check.EndpointHealthCheck",
-    version: "0.0.98"
+    version: "0.0.99"
 };
 /**
  * The protocol that Route53 uses to communicate with the endpoint.
  */
 var Protocol;
 (function(Protocol) {
     Protocol["HTTP"] = "HTTP";
```

##### package/package.json

###### Pretty-printed

 * *Similarity: 0.9722222222222222%*

 * *Differences: {"'version'": "'0.0.99'"}*

```diff
@@ -154,9 +154,9 @@
         "test": "npx projen test",
         "test:watch": "npx projen test:watch",
         "unbump": "npx projen unbump",
         "watch": "npx projen watch"
     },
     "stability": "stable",
     "types": "lib/index.d.ts",
-    "version": "0.0.98"
+    "version": "0.0.99"
 }
```

